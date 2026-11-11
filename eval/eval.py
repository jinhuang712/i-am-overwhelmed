"""Compare two versions of the plugin in one command, under a spending limit.

Usage:
  python3 eval/eval.py --old REF [--new REF] --budget USD [options]
  python3 eval/eval.py --old REF --dry-run
  python3 eval/eval.py --smoke --budget USD            (try the tool first: every task once, cheap model, no judging)
  python3 eval/eval.py --old REF --none --budget USD   (adds an arm with no plugin)

Every task in tasks.json names the most one run of it may cost, and the limits add
up to the most the eval can cost. --budget is the limit for the whole eval, judging
included, and it is required for a real run. Run the same command again to resume: finished runs are kept, and
the money they cost still counts against the limit.

Results go to eval/results/<date>-<old>-vs-<new>-<model>/. raw/ is git-ignored.
"""
import argparse
import json
import shutil
import subprocess
import threading
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

from blind import blind_task
from budget import Budget, estimate, past_costs
from checks import summary as check_summary
from judge import judge_task
from run import REPO, run_one
from yesno import FLAG_PASSES, RUBRIC as YESNO_RUBRIC, judge_task as judge_yesno, read_decks
from score import summary as score_summary
from score import summary_yesno as yesno_summary

HERE = Path(__file__).parent
JUDGE_PER_TASK = 0.30  # Kept back for judging, for each task.
JUDGE_PER_TASK_YESNO = 0.50  # The same for --rubric yesno: about 90 cheap calls and a few strong ones.
JUDGE_MAX_SHARE = 0.5  # Judging never reserves more than this part of the budget.


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
    p.add_argument("--old", help="git ref of the baseline")
    p.add_argument("--smoke", action="store_true",
                   help="try the tool before a full run: every task once, the new arm only, on the cheap model, "
                        "with no judging. It catches a plugin that does not load, a task that runs away, a bad path")
    p.add_argument("--new", default="HEAD", help="git ref to compare (default HEAD)")
    p.add_argument("--none", action="store_true", help="add a third arm that runs with no plugin")
    p.add_argument("--budget", type=float, help="USD limit for the whole eval")
    p.add_argument("--dry-run", action="store_true", help="show the plan and the estimate, spend nothing")
    p.add_argument("--model", default="claude-sonnet-5-5")
    p.add_argument("--effort", default="medium")
    p.add_argument("--rubric", choices=["scale", "yesno"], default="scale",
                   help="scale: rubric.md, scored 0 to 3 by one judge. yesno: rubric-yesno.md, cut into decks, "
                        "answered several times by a cheap judge, with the majority counted")
    p.add_argument("--judge-model", default="claude-opus-5-5", help="the judge for scale, and for the 🔎 lines of yesno")
    p.add_argument("--cheap-judge", default="claude-haiku-5-5", help="the judge for the decks of yesno")
    p.add_argument("--passes", type=int, default=3, help="yesno: times the cheap judge answers a deck")
    p.add_argument("--strong-passes", type=int, default=1, help="yesno: times the strong judge answers the 🔎 lines")
    p.add_argument("--judge-effort", default="medium")
    p.add_argument("--runs", type=int, default=5, help="runs per arm per task")
    p.add_argument("--tasks", help="comma-separated task names (default all)")
    p.add_argument("-j", type=int, default=6, help="parallel runs")
    p.add_argument("--seed", type=int, help="fixed shuffle for the blind labels")
    p.add_argument("--out", help="results folder (default derived from refs and model)")
    a = p.parse_args()
    if a.smoke:
        a.old, a.runs, a.model, a.none = a.new, 1, a.cheap_judge, False
    if not a.old:
        p.error("--old is required, except with --smoke")
    if a.budget is None and not a.dry_run:
        p.error("--budget is required for a real run; use --dry-run to see the estimate")
    return a


def main():
    a = parse_args()
    tasks = json.loads((HERE / "tasks.json").read_text())
    if a.tasks:
        tasks = [t for t in tasks if t["name"] in a.tasks.split(",")]
    refs = {"new": a.new} if a.smoke else {"old": a.old, "new": a.new}
    shas = {arm: short_sha(ref) for arm, ref in refs.items()}
    n_arms = len(refs) + (1 if a.none else 0)
    cost, known = estimate(tasks, a.model, n_arms, a.runs, past_costs(HERE / "results"))
    calls = len(tasks) * n_arms * a.runs
    # Every task names the most one run may cost. The limits add up to the most the eval can cost.
    run_sum = sum(t["budget"] for t in tasks) * n_arms * a.runs
    judge_each = 0 if a.smoke else JUDGE_PER_TASK_YESNO if a.rubric == "yesno" else JUDGE_PER_TASK
    judge_sum = judge_each * len(tasks)
    print(f"plan: {calls} runs, {len(tasks)} judge calls, {a.model}")
    print(f"task limits: ${run_sum:.2f} for the runs + ${judge_sum:.2f} for judging = ${run_sum + judge_sum:.2f} at most")
    print(f"estimate: ${cost:.2f} for the runs, judging extra ({'from past runs' if known else 'rough default, no history'})")
    if a.budget is not None:
        judge_pool = min(judge_sum, a.budget * JUDGE_MAX_SHARE)
        run_pool = a.budget - judge_pool
        print(f"limit: ${a.budget:.2f}, ${judge_pool:.2f} of it kept for judging")
        if run_sum > run_pool:
            print("warning: the task limits add up to more than the limit, so late runs may be stopped")
    if a.dry_run:
        return

    name = f"{date.today()}-{shas.get('old', 'smoke')}-vs-{shas['new']}-{a.model.removeprefix('claude-')}"
    # Absolute, because each run starts in its own folder: a relative --plugin-dir would point nowhere.
    out = (Path(a.out) if a.out else HERE / "results" / name).resolve()
    raw = out / "raw"
    budget = Budget(a.budget, out / "ledger.jsonl")
    arms = {arm: export_arm(ref, raw / "arms" / arm) for arm, ref in refs.items()}
    if a.none:
        arms["none"] = None

    score_file = "yesno.csv" if a.rubric == "yesno" else "scores.csv"

    def settled(t):
        """True when every run of the task is done and judged, so it needs no more money."""
        root = raw / t["name"]
        runs_done = all((root / f"{arm}-{i}" / "done.json").exists()
                        for arm in arms for i in range(1, a.runs + 1))
        return runs_done and (root / "blind" / score_file).exists()

    # On a resume, judging money is kept back only for the tasks that still need a judge.
    open_tasks = [t for t in tasks if not settled(t)]
    run_pool = a.budget - min(judge_each * len(open_tasks), a.budget * JUDGE_MAX_SHARE)

    # Whole rounds come first, so a stop leaves the arms balanced.
    jobs = [(t, arm, plugin, i) for i in range(1, a.runs + 1) for t in tasks for arm, plugin in arms.items()]

    done, lock = [0], threading.Lock()
    raw.mkdir(parents=True, exist_ok=True)

    def job(j):
        t, arm, plugin, i = j
        status = run_one(t, arm, plugin, i, raw, a.model, a.effort, budget, min(t["budget"], run_pool), run_pool)
        with lock:  # One line for every finished run, on screen and in progress.log.
            done[0] += 1
            line = f"{done[0]}/{len(jobs)} ${budget.spent:.2f} {status}: {t['name']} {arm}-{i}"
            print(line, flush=True)
            with (raw / "progress.log").open("a") as f:
                f.write(line + "\n")
        return status

    with ThreadPoolExecutor(a.j) as ex:
        statuses = list(ex.map(job, jobs))
    counts = {s: statuses.count(s) for s in sorted(set(statuses))}
    print("runs:", counts, f"spent ${budget.spent:.2f}", flush=True)

    if a.smoke:  # No blind samples and no judge: the point is only whether every run comes through.
        bad = [f"{t['name']} {arm}-{i}: {s}" for (t, arm, _, i), s in zip(jobs, statuses) if s != "done"]
        print("smoke: " + ("every run came through" if not bad else "these runs did not come through"))
        for line in bad:
            print("  " + line)
        print(f"spent ${budget.spent:.2f} of ${a.budget:.2f}. Raw output: {raw}")
        sys.exit(1 if bad else 0)

    finished = {t["name"] for t in tasks
                if (raw / t["name"]).exists() and blind_task(raw / t["name"], t["turns"], a.seed, t.get("system"))}
    caps = judge_caps(raw, finished, a.budget - budget.spent)

    yesno_lines = [line for d in read_decks(YESNO_RUBRIC.read_text()) for line in d["lines"]]
    sections = []
    for t in tasks:
        root = raw / t["name"]
        if t["name"] not in finished:
            sections.append(f"## {t['name']}\n\nNo finished runs.")
            continue
        if a.rubric == "yesno":
            verdict = judge_yesno(root, a.cheap_judge, a.judge_model, a.passes, a.strong_passes, budget)
        else:
            verdict = judge_task(root, a.judge_model, a.judge_effort, budget, caps.get(t["name"], 0))
        print(f"judge {t['name']}: {verdict} ${budget.spent:.2f}", flush=True)
        text = check_summary(root)
        if (root / "blind" / score_file).exists():
            scored = yesno_summary(root, yesno_lines) if a.rubric == "yesno" else score_summary(root)
            text = scored + "\n\nChecks:\n" + text
            shutil.copy(root / "blind" / score_file, out / f"{t['name']}-{score_file}")
            shutil.copy(root / "mapping.txt", out / f"{t['name']}-mapping.txt")
        else:
            text = f"Judge: {verdict}\n\nChecks:\n" + text
        sections.append(f"## {t['name']}\n\n```\n{text}\n```")

    judge_note = (f"{a.cheap_judge} x{a.passes} on rubric-yesno.md, {a.judge_model} on its 🔎 lines, "
                  f"x{FLAG_PASSES} where it raises a red flag"
                  if a.rubric == "yesno" else a.judge_model)
    head = (f"# Eval {name}\n\n- old: `{a.old}` ({shas['old']})\n- new: `{a.new}` ({shas['new']})\n"
            f"{'- none: no plugin' + chr(10) if a.none else ''}"
            f"- model: {a.model}, effort {a.effort}, judge {judge_note}\n- runs: {counts}\n"
            f"- spent: ${budget.spent:.2f} of ${a.budget:.2f}\n")
    if "stopped" in counts:
        head += "- incomplete: the budget stopped some runs\n"
    (out / "report.md").write_text(head + "\n" + "\n\n".join(sections) + "\n")
    print(f"spent ${budget.spent:.2f} of ${a.budget:.2f}. Report: {out / 'report.md'}")


if __name__ == "__main__":
    main()
