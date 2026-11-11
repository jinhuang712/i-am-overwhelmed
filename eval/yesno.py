"""Judge blind samples with the rubric of yes or no questions, rubric-yesno.md.

The rubric is cut into decks of related lines. A deck goes to a cheap judge several
times, and the majority answer counts. Lines marked 🔎 go to a strong judge, and
lines marked ⚙️ are answered by a script in checks.py.

N and NA both mean "the reply did not do it", so an answer is stored as Y or N.
Every call is cached in the task's blind/ folder: a resume asks only what is missing.
"""
import collections
import hashlib
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from checks import scripted_answer
from run import ISOLATE, clean_env

RUBRIC = Path(__file__).parent / "rubric-yesno.md"
DECK_MAX = 14  # Lines one call may hold. 14 was stable in the experiment of 2026-11-10.
PER_CALL = 2  # Samples in one call.
CHEAP_CAP = 0.06  # USD one call to the cheap judge may cost.
STRONG_CAP = 0.40  # USD one call to the strong judge may cost.
STRONG_DECK = "Checked against the transcript"
CSV_BLOCK = re.compile(r"```csv\n(.*?)```", re.S)
ROW = re.compile(r"^\| ([A-Z]\d+) \| (.*) \|$")


def read_decks(text):
    """Return the decks of the rubric: name, what it covers, who it is about, and its lines."""
    decks = []
    text = text.split("\n## Parked")[0]  # Parked lines are kept in the file and not scored.
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
                lines.append({"id": m.group(1), "text": m.group(2), "kind": kind, "deck": name.strip(),
                              "flag": "🚩" in m.group(2), "strong": "🔎" in m.group(2),
                              "script": "⚙️" in m.group(2)})
        decks.append({"name": name.strip(), "about": about, "who": who, "lines": lines})
    return decks


def split_decks(decks, limit=DECK_MAX):
    """Cut a deck that is too long into parts of equal size, so one call never holds too many lines."""
    out = []
    for d in decks:
        if not d["lines"]:
            continue
        parts = -(-len(d["lines"]) // limit)
        size = -(-len(d["lines"]) // parts)
        for k in range(parts):
            name = d["name"] if parts == 1 else f"{d['name']} ({k + 1}/{parts})"
            out.append({**d, "name": name, "lines": d["lines"][k * size:(k + 1) * size]})
    return out


def for_judges(decks):
    """Return (decks for the cheap judge, decks for the strong judge). Lines for a script go to neither."""
    cheap = [{**d, "lines": [line for line in d["lines"] if not line["strong"] and not line["script"]]}
             for d in decks]
    strong = [{"name": STRONG_DECK, "who": "reply",
               "about": "Each line needs the tool calls and results checked against what the reply says.",
               "lines": [line for d in decks for line in d["lines"] if line["strong"] and not line["script"]]}]
    return split_decks(cheap), split_decks(strong)


def prompt(deck, samples):
    """samples is a list of (label, text)."""
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
    parts += [f"=== SAMPLE {label} ===\n{text}" for label, text in samples]
    return "\n\n".join(parts)


def parse(text, ids, labels):
    """Return {label: {id: answer}}, or None when the judge's table is not usable."""
    blocks = CSV_BLOCK.findall(text or "")
    if not blocks:
        return None
    rows = [[c.strip() for c in line.split(",")] for line in blocks[-1].strip().splitlines()]
    if rows[0] != ["label", *ids] or sorted(r[0] for r in rows[1:]) != sorted(labels):
        return None
    if any(len(r) != len(rows[0]) or any(v not in ("Y", "N", "NA") for v in r[1:]) for r in rows[1:]):
        return None
    return {r[0]: dict(zip(ids, r[1:])) for r in rows[1:]}


def ask(deck, samples, k, model, cap, cache, budget):
    """Return (status, answers). status is one of: cached, planned, done, stopped, failed.

    budget is None for a dry run. Otherwise it has hold(amount) and settle(held, cost, **record).
    """
    text = prompt(deck, samples)
    hit = cache / f"{hashlib.sha1(f'{model}\n{k}\n{text}'.encode()).hexdigest()}.json"
    if hit.exists():
        got = json.loads(hit.read_text())
        if isinstance(got, list):  # Written before 2026-11-11: one row per sample, in order.
            got = {s[0]: row for s, row in zip(samples, got)}
        return "cached", got.get("answers", got)  # Newer files also keep the judge's notes.
    if budget is None:
        return "planned", None
    if not budget.hold(cap):
        return "stopped", None
    cost, answers = cap, None  # Unknown spend counts as the whole hold.
    try:
        cmd = ["claude", "-p", "--model", model, "--effort", "medium", *ISOLATE,
               "--tools", "", "--output-format", "json", "--max-budget-usd", f"{cap:.2f}"]
        res = subprocess.run(cmd, cwd=cache, env=clean_env(), input=text,
                             capture_output=True, text=True)
        try:
            data = json.loads(res.stdout)
        except ValueError:
            return "failed", None
        cost = data.get("total_cost_usd", cap)
        answers = parse(data.get("result"), [line["id"] for line in deck["lines"]], [s[0] for s in samples])
        if answers is None:
            return "failed", None
        notes = CSV_BLOCK.sub("", data.get("result") or "").strip()
        hit.write_text(json.dumps({"answers": answers, "notes": notes, "deck": deck["name"]}, ensure_ascii=False))
        return "done", answers
    finally:
        budget.settle(cap, cost, kind="judge", deck=deck["name"], model=model, status="done" if answers else "failed")


def majority(votes):
    """Y when more than half of the passes said Y. N and NA both count as not Y."""
    return "Y" if sum(v == "Y" for v in votes) * 2 > len(votes) else "N"


def judge_task(root, cheap, strong, passes, strong_passes, budget, jobs=8):
    """Judge every blind sample of a task. Return one of: done, skipped, stopped, failed.

    The answers go to blind/yesno.csv only when every call came back, so a half-judged
    task is judged again on the next run, from the cache.
    """
    blind = root / "blind"
    if (blind / "yesno.csv").exists():
        return "skipped"
    samples = [(s.stem, s.read_text()) for s in sorted(blind.glob("R*.md"))]
    if not samples:
        return "failed"
    cache = blind / "yesno-cache"
    cache.mkdir(exist_ok=True)
    decks = read_decks(RUBRIC.read_text())
    cheap_decks, strong_decks = for_judges(decks)
    batches = [samples[i:i + PER_CALL] for i in range(0, len(samples), PER_CALL)]
    calls = [(d, b, k, cheap, CHEAP_CAP) for d in cheap_decks for b in batches for k in range(passes)]
    calls += [(d, b, k, strong, STRONG_CAP) for d in strong_decks for b in batches for k in range(strong_passes)]
    with ThreadPoolExecutor(jobs) as ex:
        results = list(ex.map(lambda c: ask(c[0], c[1], c[2], c[3], c[4], cache, budget), calls))
    statuses = {status for status, _ in results}
    if "stopped" in statuses:
        return "stopped"
    if "failed" in statuses or "planned" in statuses:
        return "failed"
    votes = collections.defaultdict(list)
    for _, answers in results:
        for label, row in (answers or {}).items():
            for line_id, v in row.items():
                votes[(label, line_id)].append(v)
    for d in decks:  # The lines a script answers: exact, and free.
        for line in d["lines"]:
            if line["script"]:
                for label, text in samples:
                    votes[(label, line["id"])] = [scripted_answer(line["text"], text)]
    ids = [line["id"] for d in decks for line in d["lines"]]
    rows = [",".join(["label", *ids])]
    rows += [",".join([label, *(majority(votes[(label, i)]) for i in ids)]) for label, _ in samples]
    (blind / "yesno.csv").write_text("\n".join(rows) + "\n")
    return "done"
