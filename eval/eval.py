"""Compare two versions of the plugin in one command, under a spending limit.

Usage:
  python3 eval/eval.py --old REF [--new REF] --budget USD [options]
  python3 eval/eval.py --old REF --dry-run
  python3 eval/eval.py --old REF --none --budget USD   (adds an arm with no plugin)

--budget is the limit for the whole eval, judging included, and it is required
for a real run. Run the same command again to resume: finished runs are kept, and
the money they cost still counts against the limit.

Results go to eval/results/<date>-<old>-vs-<new>-<model>/. raw/ is git-ignored.
"""
import argparse
import json
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

from blind import blind_task
from budget import Budget, estimate, past_costs
from checks import summary as check_summary
from judge import judge_task
from run import REPO, run_one
from score import summary as score_summary

HERE = Path(__file__).parent
JUDGE_SHARE = 0.25  # Part of the budget kept back for judging.
CAP_FACTOR = 3  # One run may cost this many times its fair share.


def short_sha(ref):
    return subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", ref],
                          capture_output=True, text=True, check=True).stdout.strip()


def export_arm(ref, dest):
    if (dest / "plugin").exists():
        return dest / "plugin"
    dest.mkdir(parents=True, exist_ok=True)
    tar = subprocess.Popen(["git", "-C", str(REPO), "archive", ref, "plugin"], stdout=subprocess.PIPE)
    subprocess.run(["tar", "-x", "-C", str(dest)], stdin=tar.stdout, check=True)
    if tar.wait():
        sys.exit(f"cannot export plugin/ at {ref}")
    return dest / "plugin"


def judge_caps(raw, names, left):
    """Share what is left among the unjudged tasks, by the size of their samples."""
    sizes = {n: sum(s.stat().st_size for s in (raw / n / "blind").glob("R*.md"))
             for n in names if not (raw / n / "blind" / "scores.csv").exists()}
    total = sum(sizes.values()) or 1
    return {n: left * size / total for n, size in sizes.items()}


def parse_args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--old", required=True, help="git ref of the baseline")
    p.add_argument("--new", default="HEAD", help="git ref to compare (default HEAD)")
    p.add_argument("--none", action="store_true", help="add a third arm that runs with no plugin")
    p.add_argument("--budget", type=float, help="USD limit for the whole eval")
    p.add_argument("--dry-run", action="store_true", help="show the plan and the estimate, spend nothing")
    p.add_argument("--model", default="claude-sonnet-5-5")
    p.add_argument("--effort", default="medium")
    p.add_argument("--judge-model", default="claude-opus-5-5")
    p.add_argument("--judge-effort", default="medium")
    p.add_argument("--runs", type=int, default=5, help="runs per arm per task")
    p.add_argument("--tasks", help="comma-separated task names (default all)")
    p.add_argument("-j", type=int, default=6, help="parallel runs")
    p.add_argument("--seed", type=int, help="fixed shuffle for the blind labels")
    p.add_argument("--out", help="results folder (default derived from refs and model)")
    a = p.parse_args()
    if a.budget is None and not a.dry_run:
        p.error("--budget is required for a real run; use --dry-run to see the estimate")
    return a


def main():
    a = parse_args()
    tasks = json.loads((HERE / "tasks.json").read_text())
    if a.tasks:
        tasks = [t for t in tasks if t["name"] in a.tasks.split(",")]
    refs = {"old": a.old, "new": a.new}
    shas = {arm: short_sha(ref) for arm, ref in refs.items()}
    n_arms = len(refs) + (1 if a.none else 0)
    cost, known = estimate(tasks, a.model, n_arms, a.runs, past_costs(HERE / "results"))
    calls = len(tasks) * n_arms * a.runs
    print(f"plan: {calls} runs, {len(tasks)} judge calls, {a.model}")
    print(f"estimate: ${cost:.2f} for the runs, judging extra ({'from past runs' if known else 'rough default, no history'})")
    if a.budget is not None:
        run_pool = a.budget * (1 - JUDGE_SHARE)
        run_cap = run_pool / calls * (CAP_FACTOR if calls > CAP_FACTOR else 1)
        print(f"limit: ${a.budget:.2f}, ${a.budget * JUDGE_SHARE:.2f} of it kept for judging, ${run_cap:.2f} cap per run")
        if cost > run_pool:
            print("warning: the estimate is above the limit, so some runs will be stopped")
        if run_cap < 1.5 * cost / calls:
            print("warning: the cap per run is tight, so runs may fail at the cap")
    if a.dry_run:
        return

    name = f"{date.today()}-{shas['old']}-vs-{shas['new']}-{a.model.removeprefix('claude-')}"
    out = Path(a.out) if a.out else HERE / "results" / name
    raw = out / "raw"
    budget = Budget(a.budget, out / "ledger.jsonl")
    arms = {arm: export_arm(ref, raw / "arms" / arm) for arm, ref in refs.items()}
    if a.none:
        arms["none"] = None

    # Whole rounds come first, so a stop leaves the arms balanced.
    jobs = [(t, arm, plugin, i) for i in range(1, a.runs + 1) for t in tasks for arm, plugin in arms.items()]

    def job(j):
        t, arm, plugin, i = j
        return run_one(t, arm, plugin, i, raw, a.model, a.effort, budget, run_cap, run_pool)

    with ThreadPoolExecutor(a.j) as ex:
        statuses = list(ex.map(job, jobs))
    counts = {s: statuses.count(s) for s in sorted(set(statuses))}
    print("runs:", counts, f"spent ${budget.spent:.2f}", flush=True)

    finished = {t["name"] for t in tasks
                if (raw / t["name"]).exists() and blind_task(raw / t["name"], t["turns"], a.seed)}
    caps = judge_caps(raw, finished, a.budget - budget.spent)

    sections = []
    for t in tasks:
        root = raw / t["name"]
        if t["name"] not in finished:
            sections.append(f"## {t['name']}\n\nNo finished runs.")
            continue
        verdict = judge_task(root, a.judge_model, a.judge_effort, budget, caps.get(t["name"], 0))
        print(f"judge {t['name']}: {verdict}", flush=True)
        text = check_summary(root)
        if (root / "blind" / "scores.csv").exists():
            text = score_summary(root) + "\n\nChecks:\n" + text
            shutil.copy(root / "blind" / "scores.csv", out / f"{t['name']}-scores.csv")
            shutil.copy(root / "mapping.txt", out / f"{t['name']}-mapping.txt")
        else:
            text = f"Judge: {verdict}\n\nChecks:\n" + text
        sections.append(f"## {t['name']}\n\n```\n{text}\n```")

    head = (f"# Eval {name}\n\n- old: `{a.old}` ({shas['old']})\n- new: `{a.new}` ({shas['new']})\n"
            f"{'- none: no plugin' + chr(10) if a.none else ''}"
            f"- model: {a.model}, effort {a.effort}, judge {a.judge_model}\n- runs: {counts}\n"
            f"- spent: ${budget.spent:.2f} of ${a.budget:.2f}\n")
    if "stopped" in counts:
        head += "- incomplete: the budget stopped some runs\n"
    (out / "report.md").write_text(head + "\n" + "\n\n".join(sections) + "\n")
    print(f"spent ${budget.spent:.2f} of ${a.budget:.2f}. Report: {out / 'report.md'}")


if __name__ == "__main__":
    main()
