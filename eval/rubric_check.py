"""Check the rubric itself: is every line stable, and does it tell replies apart?

Usage:
  python3 eval/rubric_check.py --dry-run
  python3 eval/rubric_check.py --budget USD [--samples N] [--passes K] [--decks 3,6]
  python3 eval/rubric_check.py --strong --budget USD   (the 🔎 lines, on the strong judge)

It does not run any task. It takes replies that earlier evals left on disk, in
eval/results/*/raw/*/blind/, and has a cheap judge answer every line of
rubric-yesno.md for them, several times.

For each line the report gives:
  stable   on how many samples all passes agreed on Y or not Y (N and NA count as one answer)
  fires    on how many samples the majority answer was Y
  NA       on how many samples the majority answer was NA

Every answer is kept in a cache, keyed by the deck's text, the samples and the pass.
After a deck is edited, the same command judges only that deck again. The samples are
the ones of the last check, listed in raw/samples.txt, so rounds compare the same
replies; --new-samples draws them again from what is on disk now.

Work files go to eval/results/rubric-check/raw/, which git ignores. Every finished call prints a
line and adds it to raw/progress.log, so a run can be followed with `tail -f`.
"""
import argparse
import collections
import json
import random
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from yesno import RUBRIC, STRONG_CAP, ask, for_judges, read_decks, split_decks  # noqa: E402

HERE = Path(__file__).parent
RESULTS = HERE / "results"
OUT = RESULTS / "rubric-check"
SAMPLES = OUT / "raw" / "samples.txt"
PER_CALL = 2  # Samples in one judge call.
CALL_CAP = 0.06  # USD one call may cost.


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


def saved_samples(path=SAMPLES, results=RESULTS):
    """The samples of the last check, or None when there is no list or a reply on it is gone."""
    if not path.exists():
        return None
    found = []
    for line in path.read_text().splitlines():
        model, arm, task, rel = line.split(" ", 3)
        if not (results / rel).exists():
            return None
        found.append({"path": results / rel, "task": task, "arm": arm, "model": model, "result": rel.split("/")[0]})
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


class Spend:
    def __init__(self, limit, ledger):
        self.limit, self.ledger, self.lock = limit, ledger, threading.Lock()
        self.spent = 0.0
        if ledger.exists():
            self.spent = sum(json.loads(line)["cost"] for line in ledger.read_text().splitlines())

    def hold(self, amount):
        with self.lock:
            if self.spent + amount > self.limit:
                return False
            self.spent += amount
            return True

    def settle(self, held, cost, **record):
        with self.lock:
            self.spent += cost - held
            with self.ledger.open("a") as f:
                f.write(json.dumps({**record, "cost": cost}) + "\n")


class Progress:
    """Print one line for every finished call, and keep the same lines in a file to follow."""

    def __init__(self, total, path):
        self.total, self.path, self.done, self.lock = total, path, 0, threading.Lock()
        path.write_text("")

    def step(self, status, deck, spend):
        with self.lock:
            self.done += 1
            spent = f" ${spend.spent:.2f}" if spend else ""
            line = f"{self.done}/{self.total} {100 * self.done // self.total}%{spent} {status}: {deck}"
            print(line, flush=True)
            with self.path.open("a") as f:
                f.write(line + "\n")


def judge(deck, batch, k, model, cache, spend, cap=CALL_CAP):
    """Return (status, one {id: answer} per sample of the batch)."""
    labelled = [(f"S{n:02d}", s["path"].read_text()) for n, s in enumerate(batch, 1)]
    status, answers = ask(deck, labelled, k, model, cap, cache, spend)
    return status, [answers[label] for label, _ in labelled] if answers else None


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
                # N and NA both say "the reply did not do it". Only a flip to or from Y is a real disagreement.
                same += len({v == "Y" for v in got}) == 1
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
           f"earlier evals\n- judge: {model}, {passes} passes\n- stable: on {100 * stable:.0f}% of the answers all passes "
           f"agreed on Y or not Y\n- spent so far: ${spent:.2f}\n"]
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
    p.add_argument("--model", help="the judge (default claude-haiku-5-5, or claude-opus-5-5 with --strong)")
    p.add_argument("--strong", action="store_true",
                   help="judge only the 🔎 lines, as one deck the way an eval sends them to the strong judge. "
                        "The report goes to report-strong.md")
    p.add_argument("--decks", help="numbers of the decks to judge, such as 3,6 (default all)")
    p.add_argument("--new-samples", action="store_true",
                   help="draw the samples again from what is on disk, instead of the ones of the last check")
    p.add_argument("-j", type=int, default=8)
    a = p.parse_args()
    if a.budget is None and not a.dry_run:
        p.error("--budget is required for a real run; use --dry-run to see the plan")

    whole = read_decks(RUBRIC.read_text())
    if a.decks:
        keep = {int(n) for n in a.decks.split(",")}
        whole = [d for n, d in enumerate(whole, 1) if n in keep]
    model = a.model or ("claude-opus-5-5" if a.strong else "claude-haiku-5-5")
    decks = for_judges(whole)[1] if a.strong else split_decks(whole)
    cap = STRONG_CAP if a.strong else CALL_CAP
    samples = None if a.new_samples else saved_samples()
    if samples is not None and len(samples) == a.samples:
        print(f"samples: the {len(samples)} of the last check")
    else:
        samples = pick(all_samples(), a.samples)
        print(f"samples: {len(samples)} drawn from what is on disk")
    samples.sort(key=lambda s: s["path"].stat().st_size)
    batches = [samples[i:i + PER_CALL] for i in range(0, len(samples), PER_CALL)]
    cache = OUT / "raw" / "cache"
    cache.mkdir(parents=True, exist_ok=True)
    spend = None if a.dry_run else Spend(a.budget, OUT / "raw" / "ledger.jsonl")

    jobs = [(d, b, k) for k in range(a.passes) for d in decks for b in batches]
    progress = None if a.dry_run else Progress(len(jobs), OUT / "raw" / "progress.log")

    def one(j):
        got = judge(j[0], j[1], j[2], model, cache, spend, cap)
        if progress:
            progress.step(got[0], j[0]["name"], spend)
        return got

    with ThreadPoolExecutor(a.j) as ex:
        results = list(ex.map(one, jobs))
    counts = collections.Counter(status for status, _ in results)
    print(f"plan: {len(decks)} decks x {len(batches)} batches x {a.passes} passes = {len(jobs)} calls, {model}")
    print("calls:", dict(counts))
    if spend is None:
        print(f"to run: {counts['planned']} calls, at most ${counts['planned'] * cap:.2f}")
        return

    index = {id(s): n for n, s in enumerate(samples)}
    votes = collections.defaultdict(list)
    for (_, batch, _), (_, answers) in zip(jobs, results):
        if answers:
            for s, row in zip(batch, answers):
                for line_id, v in row.items():
                    votes[(line_id, index[id(s)])].append(v)
    rows = summarise(decks, samples, votes, a.passes)
    (OUT / ("report-strong.md" if a.strong else "report.md")).write_text(report(rows, samples, a.passes, model, spend.spent))
    SAMPLES.write_text("\n".join(
        f"{s['model']} {s['arm']} {s['task']} {s['path'].relative_to(RESULTS)}" for s in samples) + "\n")
    print(f"spent ${spend.spent:.2f} of ${a.budget:.2f}. Report: {OUT / 'report.md'}")


if __name__ == "__main__":
    main()
