"""Unblind a judge's scores and summarise them per arm.

Usage:
  python3 eval/score.py RAW_DIR TASK

Reads RAW_DIR/<task>/blind/scores.csv (label + one column per rubric dimension,
values 0-3 or NA) and RAW_DIR/<task>/mapping.txt. Prints, per arm: % of available
points outside E, the mean of each dimension, and the E dimensions separately.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path


def num(v):
    return None if v in ("NA", "") else int(v)


def summary(root):
    mapping = dict(line.split() for line in (root / "mapping.txt").read_text().splitlines())
    rows = list(csv.DictReader((root / "blind" / "scores.csv").open()))
    dims = [c for c in rows[0] if c != "label"]
    core = [d for d in dims if not d.startswith("E")]
    by_arm = defaultdict(list)
    for r in rows:
        by_arm[mapping[r["label"]].rsplit("-", 1)[0]].append(r)
    lines = []
    for arm, rs in sorted(by_arm.items()):
        got = sum(num(r[d]) for r in rs for d in core if num(r[d]) is not None)
        avail = sum(3 for r in rs for d in core if num(r[d]) is not None)
        pct = 100 * got / avail if avail else 0
        lines.append(f"== {arm} ({len(rs)} runs): {pct:.1f}% of points outside E")
        means = []
        for d in dims:
            vals = [num(r[d]) for r in rs if num(r[d]) is not None]
            means.append(f"{d}={sum(vals) / len(vals):.1f}" if vals else f"{d}=NA")
        lines.append("   " + " ".join(means))
    return "\n".join(lines)


if __name__ == "__main__":
    print(summary(Path(sys.argv[1]) / sys.argv[2]))
