"""Mechanical checks on final replies. They cost nothing and need no judge.

Usage:
  python3 eval/checks.py RAW_DIR TASK
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

LINE_REF = re.compile(r"[\w./-]+\.\w+:\d+|\b[Ll]ines? \d+|第\s*\d+\s*行")
NEGATION = re.compile(r"[不没别未]|\b(?:not|no|never|without|cannot)\b|n't\b", re.I)
STRUCTURE = re.compile(r"^\s*(?:[-*#|]|\d+\.|```)", re.M)


def final_replies(run_dir):
    replies = []
    for turn in sorted(run_dir.glob("turn-*.jsonl")):
        for line in turn.read_text().splitlines():
            if line.startswith("{"):
                event = json.loads(line)
                if event.get("type") == "result":
                    replies.append(event.get("result") or "")
    return replies


def measure(replies):
    chars = sum(len(r) for r in replies) or 1
    return {
        "line_refs": sum(len(LINE_REF.findall(r)) for r in replies),
        "negations_per_1k": 1000 * sum(len(NEGATION.findall(r)) for r in replies) / chars,
        "paragraph_only": sum(1 for r in replies if r.strip() and not STRUCTURE.search(r)),
    }


def summary(root):
    by_arm = defaultdict(list)
    for run in sorted(d for d in root.iterdir() if (d / "done.json").exists()):
        by_arm[run.name.rsplit("-", 1)[0]].append(measure(final_replies(run)))
    lines = []
    for arm, rows in sorted(by_arm.items()):
        means = {k: sum(r[k] for r in rows) / len(rows) for k in rows[0]}
        lines.append(f"{arm}: " + " ".join(f"{k}={v:.1f}" for k, v in means.items()))
    return "\n".join(lines)


if __name__ == "__main__":
    print(summary(Path(sys.argv[1]) / sys.argv[2]))
