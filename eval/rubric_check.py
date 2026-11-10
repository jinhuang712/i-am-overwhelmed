"""Check the rubric itself: is every line stable, and does it tell replies apart?

Usage:
  python3 eval/rubric_check.py --dry-run
  python3 eval/rubric_check.py --budget USD [--samples N] [--passes K] [--decks 3,6]

It does not run any task. It takes replies that earlier evals left on disk, in
eval/results/*/raw/*/blind/, and has a cheap judge answer every line of
rubric-yesno.md for them, several times.

For each line the report gives:
  stable   on how many samples all passes gave the same answer
  fires    on how many samples the majority answer was Y
  NA       on how many samples the majority answer was NA

Every answer is kept in a cache, keyed by the deck's text, the samples and the pass.
After a deck is edited, the same command judges only that deck again.

Work files go to eval/results/rubric-check/raw/, which git ignores.
"""
import argparse
import collections
import hashlib
import json
import os
import random
import re
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run import CLEAN_ENV, DISABLE_INSTALLED  # noqa: E402

HERE = Path(__file__).parent
RUBRIC = HERE / "rubric-yesno.md"
RESULTS = HERE / "results"
OUT = RESULTS / "rubric-check"
DECK_MAX = 14  # Lines one judge call may hold. 14 was stable in the experiment of 2026-11-10.
PER_CALL = 2  # Samples in one judge call.
CALL_CAP = 0.06  # USD one call may cost.
CSV_BLOCK = re.compile(r"```csv\n(.*?)```", re.S)
ROW = re.compile(r"^\| ([A-Z]\d+) \| (.*) \|$")


def read_decks(text):
    """Return the decks of the rubric: name, what it covers, who it is about, and its lines."""
    decks = []
    for part in re.split(r"^## \d+\. ", text, flags=re.M)[1:]:
        name, _, body = part.partition("\n")
        about = next((line for line in body.splitlines() if line.strip()), "")
        who = "agent" if "| The agent" in body else "reply"
        lines, kind = [], None
        for line in body.splitlines():
            if line.startswith("Bad signs"):
                kind = "bad"
            elif line.startswith("Good signs"):
                kind = "good"
            m = ROW.match(line)
            if m:
                lines.append({"id": m.group(1), "text": m.group(2), "kind": kind})
        decks.append({"name": name.strip(), "about": about, "who": who, "lines": lines})
    return decks


def split_decks(decks, limit=DECK_MAX):
    """Cut a deck that is too long into parts of equal size, so one call never holds too many lines."""
    out = []
    for d in decks:
        parts = -(-len(d["lines"]) // limit)
        size = -(-len(d["lines"]) // parts)
        for k in range(parts):
            name = d["name"] if parts == 1 else f"{d['name']} ({k + 1}/{parts})"
            out.append({**d, "name": name, "lines": d["lines"][k * size:(k + 1) * size]})
    return out


def all_samples(results=RESULTS):
    """Every blind sample on disk, with the arm and the model it came from."""
    found = []
    for mapping in sorted(results.glob("*/raw/*/mapping.txt")):
        task_dir = mapping.parent
        result = task_dir.parent.parent.name
        model = "sonnet" if "sonnet" in result else "opus"
        for line in mapping.read_text().splitlines():
            label, run = line.split()
            path = task_dir / "blind" / f"{label}.md"
            if path.exists():
                found.append({"path": path, "task": task_dir.name, "arm": run.rsplit("-", 1)[0],
                              "model": model, "result": result})
    return found


def pick(samples, n, seed=7):
    """A fixed spread: no plugin first, then tasks and models in turn, so bad and good replies both show up."""
    rng = random.Random(seed)
    groups = collections.defaultdict(list)
    for s in samples:
        groups[(s["model"], "none" if s["arm"] == "none" else "plugin")].append(s)
    for g in groups.values():
        rng.shuffle(g)
    share = {("opus", "none"): 0.3, ("opus", "plugin"): 0.4, ("sonnet", "plugin"): 0.3}
    chosen, seen_tasks = [], collections.Counter()
    for key, part in share.items():
        want = round(n * part)
        pool = sorted(groups.get(key, []), key=lambda s: seen_tasks[s["task"]])
        for s in pool:
            if want == 0:
                break
            if seen_tasks[s["task"]] >= 2:
                continue
            chosen.append(s)
            seen_tasks[s["task"]] += 1
            want -= 1
            pool.sort(key=lambda x: seen_tasks[x["task"]])
    return chosen[:n]


def prompt(deck, batch):
    who = "The agent" if deck["who"] == "agent" else "The reply"
    table = "\n".join(f"| {line['id']} | {line['text']} |" for line in deck["lines"])
    parts = [
        "You are a judge. Read each sample, then answer every line below for it.",
        f"The lines are about one thing: {deck['name']}. {deck['about']}",
        "Answer Y when the reply does what the line says. Answer N when it does not. "
        "Answer NA when the reply has nothing the line can apply to.\n"
        "Judge every final reply of a sample together: answer Y when any turn does it.\n"
        "Use the tool calls and results to check what was actually done.",
        f"| # | {who}... |\n|---|---|\n{table}",
        "Write at most one line of notes per sample, then end with one fenced csv block.",
        "Columns: " + ",".join(["label", *(line["id"] for line in deck["lines"])]),
        "One row per sample. Values: Y, N or NA.",
    ]
    parts += [f"=== SAMPLE S{k:02d} ===\n{s['path'].read_text()}" for k, s in enumerate(batch, 1)]
    return "\n\n".join(parts)


def parse(text, ids, count):
    """Return one {id: answer} per sample, or None when the judge's table is not usable."""
    blocks = CSV_BLOCK.findall(text or "")
    if not blocks:
        return None
    rows = [[c.strip() for c in line.split(",")] for line in blocks[-1].strip().splitlines()]
    if rows[0] != ["label", *ids] or len(rows) != count + 1:
        return None
    if any(v not in ("Y", "N", "NA") for r in rows[1:] for v in r[1:]):
        return None
    return [dict(zip(ids, r[1:])) for r in rows[1:]]


class Spend:
    def __init__(self, limit, ledger):
        self.limit, self.ledger, self.lock = limit, ledger, threading.Lock()
        self.spent = 0.0
        if ledger.exists():
            self.spent = sum(json.loads(line)["cost"] for line in ledger.read_text().splitlines())

    def hold(self):
        with self.lock:
            if self.spent + CALL_CAP > self.limit:
                return False
            self.spent += CALL_CAP
            return True

    def settle(self, cost, **record):
        with self.lock:
            self.spent += cost - CALL_CAP
            with self.ledger.open("a") as f:
                f.write(json.dumps({**record, "cost": cost}) + "\n")


def judge(deck, batch, k, model, cache, spend):
    """Return (status, answers). Answers come from the cache when this exact call ran before."""
    text = prompt(deck, batch)
    key = hashlib.sha1(f"{model}\n{k}\n{text}".encode()).hexdigest()
    hit = cache / f"{key}.json"
    ids = [line["id"] for line in deck["lines"]]
    if hit.exists():
        return "cached", json.loads(hit.read_text())
    if spend is None:
        return "planned", None
    if not spend.hold():
        return "stopped", None
    cost, answers = CALL_CAP, None
    try:
        cmd = ["claude", "-p", "--model", model, "--effort", "medium", "--settings", DISABLE_INSTALLED,
               "--tools", "", "--output-format", "json", "--max-budget-usd", f"{CALL_CAP:.2f}"]
        res = subprocess.run(cmd, cwd=cache, env={**os.environ, **CLEAN_ENV}, input=text,
                             capture_output=True, text=True)
        try:
            data = json.loads(res.stdout)
        except ValueError:
            return "failed", None
        cost = data.get("total_cost_usd") or CALL_CAP
        answers = parse(data.get("result"), ids, len(batch))
        if answers is None:
            return "failed", None
        hit.write_text(json.dumps(answers))
        return "done", answers
    finally:
        spend.settle(cost, deck=deck["name"], model=model, ok=answers is not None)


def summarise(decks, samples, votes, passes):
    """One row per line: how stable it is, and how often it fires, over all samples."""
    rows = []
    for deck in decks:
        for line in deck["lines"]:
            full, same, fires, na, by = 0, 0, 0, 0, collections.Counter()
            for n, s in enumerate(samples):
                got = votes.get((line["id"], n), [])
                if len(got) < passes:
                    continue
                full += 1
                same += len(set(got)) == 1
                top = collections.Counter(got).most_common(1)[0][0]
                fires += top == "Y"
                na += top == "NA"
                group = "none" if s["arm"] == "none" else "plugin"
                by[group + "_n"] += top != "NA"
                by[group + "_y"] += top == "Y"
            rows.append({**line, "deck": deck["name"], "n": full, "same": same, "fires": fires, "na": na,
                         "none": (by["none_y"], by["none_n"]), "plugin": (by["plugin_y"], by["plugin_n"])})
    return rows


def report(rows, samples, passes, model, spent):
    judged = [r for r in rows if r["n"]]
    stable = sum(r["same"] for r in judged) / max(sum(r["n"] for r in judged), 1)
    out = [f"# Rubric check\n\n- rubric: `rubric-yesno.md`, {len(rows)} lines\n- samples: {len(samples)} replies from "
           f"earlier evals\n- judge: {model}, {passes} passes\n- stable: {100 * stable:.0f}% of the answers were the "
           f"same in all passes\n- spent so far: ${spent:.2f}\n"]
    out.append("A line is weak when it is stable on under 80% of the samples. A line that never fires has not been "
               "seen yet; it is not wrong.\n")
    deck = None
    for r in rows:
        if r["deck"] != deck:
            deck = r["deck"]
            out.append(f"\n## {deck}\n\n| # | kind | stable | fires | NA | no plugin | plugin | line |\n"
                       "|---|---|---|---|---|---|---|---|")
        if not r["n"]:
            out.append(f"| {r['id']} | {r['kind']} | not judged | | | | | {r['text']} |")
            continue
        mark = " ⚠️" if r["same"] / r["n"] < 0.8 else ""
        out.append(f"| {r['id']} | {r['kind']} | {r['same']}/{r['n']}{mark} | {r['fires']} | {r['na']} | "
                   f"{r['none'][0]}/{r['none'][1]} | {r['plugin'][0]}/{r['plugin'][1]} | {r['text']} |")
    return "\n".join(out) + "\n"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--budget", type=float, help="USD limit for all the runs of this check together")
    p.add_argument("--dry-run", action="store_true", help="show the plan, spend nothing")
    p.add_argument("--samples", type=int, default=20)
    p.add_argument("--passes", type=int, default=3)
    p.add_argument("--model", default="claude-haiku-5-5")
    p.add_argument("--decks", help="numbers of the decks to judge, such as 3,6 (default all)")
    p.add_argument("-j", type=int, default=8)
    a = p.parse_args()
    if a.budget is None and not a.dry_run:
        p.error("--budget is required for a real run; use --dry-run to see the plan")

    whole = read_decks(RUBRIC.read_text())
    if a.decks:
        keep = {int(n) for n in a.decks.split(",")}
        whole = [d for n, d in enumerate(whole, 1) if n in keep]
    decks = split_decks(whole)
    samples = pick(all_samples(), a.samples)
    samples.sort(key=lambda s: s["path"].stat().st_size)
    batches = [samples[i:i + PER_CALL] for i in range(0, len(samples), PER_CALL)]
    cache = OUT / "raw" / "cache"
    cache.mkdir(parents=True, exist_ok=True)
    spend = None if a.dry_run else Spend(a.budget, OUT / "raw" / "ledger.jsonl")

    jobs = [(d, b, k) for k in range(a.passes) for d in decks for b in batches]
    with ThreadPoolExecutor(a.j) as ex:
        results = list(ex.map(lambda j: judge(j[0], j[1], j[2], a.model, cache, spend), jobs))
    counts = collections.Counter(status for status, _ in results)
    print(f"plan: {len(decks)} decks x {len(batches)} batches x {a.passes} passes = {len(jobs)} calls, {a.model}")
    print("calls:", dict(counts))
    if spend is None:
        print(f"to run: {counts['planned']} calls, at most ${counts['planned'] * CALL_CAP:.2f}")
        return

    index = {id(s): n for n, s in enumerate(samples)}
    votes = collections.defaultdict(list)
    for (_, batch, _), (_, answers) in zip(jobs, results):
        if answers:
            for s, row in zip(batch, answers):
                for line_id, v in row.items():
                    votes[(line_id, index[id(s)])].append(v)
    rows = summarise(decks, samples, votes, a.passes)
    (OUT / "report.md").write_text(report(rows, samples, a.passes, a.model, spend.spent))
    (OUT / "raw" / "samples.txt").write_text("\n".join(
        f"{s['model']} {s['arm']} {s['task']} {s['path'].relative_to(RESULTS)}" for s in samples) + "\n")
    print(f"spent ${spend.spent:.2f} of ${a.budget:.2f}. Report: {OUT / 'report.md'}")


if __name__ == "__main__":
    main()
