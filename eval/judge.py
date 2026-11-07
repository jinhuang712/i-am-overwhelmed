"""Score the blind samples of one task with a model judge, under the budget.

The judge sees only rubric.md and the blind samples. It writes its notes, then one
fenced csv block: blind/scores.csv. Notes go to blind/judge.md.
"""
import json
import os
import re
import subprocess
from pathlib import Path

from run import CLEAN_ENV, DISABLE_INSTALLED

RUBRIC = Path(__file__).parent / "rubric.md"
CSV_BLOCK = re.compile(r"```csv\n(.*?)```", re.S)


def dimensions():
    return re.findall(r"^\| ([A-H]\d+) \|", RUBRIC.read_text(), re.M)


def build_prompt(root):
    dims = dimensions()
    samples = sorted((root / "blind").glob("R*.md"))
    parts = [
        "You are a blind judge. Score every sample with the rubric below.",
        RUBRIC.read_text(),
        "Write at most one line of notes per sample, then end with one fenced csv block.",
        "Columns: " + ",".join(["label", *dims]),
        "One row per sample. Values: 0, 1, 2, 3 or NA.",
    ]
    parts += [f"=== SAMPLE {s.stem} ===\n{s.read_text()}" for s in samples]
    return "\n\n".join(parts)


def parse_scores(text, labels):
    """Return the csv text, or raise ValueError when it is incomplete."""
    blocks = CSV_BLOCK.findall(text)
    if not blocks:
        raise ValueError("no csv block")
    rows = [line.split(",") for line in blocks[-1].strip().splitlines()]
    dims = dimensions()
    if rows[0] != ["label", *dims]:
        raise ValueError("wrong columns")
    if sorted(r[0] for r in rows[1:]) != sorted(labels):
        raise ValueError("wrong labels")
    for row in rows[1:]:
        if len(row) != len(rows[0]) or any(v not in ("0", "1", "2", "3", "NA") for v in row[1:]):
            raise ValueError(f"bad row {row[0]}")
    return "\n".join(",".join(r) for r in rows) + "\n"


def judge_task(root, model, effort, budget, cap):
    """Return one of: done, skipped, stopped, failed."""
    blind = root / "blind"
    if (blind / "scores.csv").exists():
        return "skipped"
    if not budget.hold(cap):
        return "stopped"
    cost, status = cap, "failed"  # Unknown spend counts as the whole hold.
    try:
        cmd = ["claude", "-p", "--model", model, "--effort", effort,
               "--settings", DISABLE_INSTALLED, "--tools", "",
               "--output-format", "json", "--max-budget-usd", f"{cap:.2f}"]
        res = subprocess.run(cmd, cwd=blind, env={**os.environ, **CLEAN_ENV},
                             input=build_prompt(root), capture_output=True, text=True)
        try:
            data = json.loads(res.stdout)
        except ValueError:
            (blind / "judge.md").write_text(res.stdout + res.stderr)
            return status
        cost = data.get("total_cost_usd", cap)
        text = data.get("result", "")
        (blind / "judge.md").write_text(text)
        labels = [s.stem for s in blind.glob("R*.md")]
        try:
            (blind / "scores.csv").write_text(parse_scores(text, labels))
        except ValueError as e:
            (blind / "judge-error.txt").write_text(str(e))
            return status
        status = "done"
        return status
    finally:
        budget.settle(cap, cost, kind="judge", task=root.name, model=model, status=status)
