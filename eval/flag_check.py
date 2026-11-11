"""Check the red flags against replies whose answer the owner gave.

Usage:
  python3 eval/flag_check.py --dry-run
  python3 eval/flag_check.py --budget USD

One red flag fails a reply. So a red flag line must fire on a reply that does the harm,
and stay quiet on a reply that only looks like it. The cases live in eval/flag-cases/,
which git ignores. cases.json lists them, and each reply sits next to it, as a blind
sample from an eval:

  [{"name": "fix-test-zh-new-2", "reply": "fix-test-zh-new-2.md",
    "expect": {"H17": "N"}, "why": "it rewrote a wrong test, and said so"}]

Each case is judged the way an eval judges it: every deck, the strong judge on the 🔎
lines, and a red flag from the strong judge confirmed. Answers are cached by the deck's
text, so after a line changes only the decks that hold it are asked again. The budget
counts every run of this check together, like the ledger it keeps.
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from budget import Budget  # noqa: E402
from yesno import CHEAP_CAP, FLAG_PASSES, RUBRIC, STRONG_CAP, for_judges, judge_task, read_decks  # noqa: E402

CASES = Path(__file__).parent / "flag-cases"


def most(passes):
    """USD one case may cost at most: one sample, every deck."""
    cheap, strong = for_judges(read_decks(RUBRIC.read_text()))
    return len(cheap) * passes * CHEAP_CAP + len(strong) * FLAG_PASSES * STRONG_CAP


def check(cases_dir, cheap, strong, passes, budget):
    """Return one row per expected answer: (case, line, expected, got)."""
    rows = []
    for case in json.loads((cases_dir / "cases.json").read_text()):
        root = cases_dir / "work" / case["name"]
        blind = root / "blind"
        blind.mkdir(parents=True, exist_ok=True)
        shutil.copy(cases_dir / case["reply"], blind / "R01.md")
        (blind / "yesno.csv").unlink(missing_ok=True)  # The rubric may have changed: judge again, from the cache.
        status = judge_task(root, cheap, strong, passes, 1, budget) if budget else "planned"
        got = {}
        if status == "done":
            head, row = (blind / "yesno.csv").read_text().splitlines()[:2]
            got = dict(zip(head.split(","), row.split(",")))
        rows += [(case["name"], line, want, got.get(line, status)) for line, want in case["expect"].items()]
    return rows


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--budget", type=float, help="USD limit for all the runs of this check together")
    p.add_argument("--dry-run", action="store_true", help="show the plan, spend nothing")
    p.add_argument("--cases", default=str(CASES), help="the folder that holds cases.json")
    p.add_argument("--cheap-judge", default="claude-haiku-5-5")
    p.add_argument("--judge-model", default="claude-opus-5-5")
    p.add_argument("--passes", type=int, default=3)
    a = p.parse_args()
    if a.budget is None and not a.dry_run:
        p.error("--budget is required for a real run; use --dry-run to see the plan")
    cases_dir = Path(a.cases).resolve()
    cases = json.loads((cases_dir / "cases.json").read_text())
    print(f"plan: {len(cases)} cases, at most ${most(a.passes):.2f} each before the cache: "
          f"{a.cheap_judge} x{a.passes}, {a.judge_model} on the 🔎 lines")
    budget = None if a.dry_run else Budget(a.budget, cases_dir / "work" / "ledger.jsonl")
    rows = check(cases_dir, a.cheap_judge, a.judge_model, a.passes, budget)
    wrong = [r for r in rows if r[2] != r[3]]
    for case, line, want, got in rows:
        mark = "to judge" if budget is None else "ok " if want == got else "BAD"
        print(f"{mark} {case} {line}: expected {want}" + (f", got {got}" if budget else ""))
    if budget:
        print(f"{len(rows) - len(wrong)} of {len(rows)} right. Spent ${budget.spent:.2f} of ${a.budget:.2f}")
    sys.exit(1 if wrong and budget else 0)


if __name__ == "__main__":
    main()
