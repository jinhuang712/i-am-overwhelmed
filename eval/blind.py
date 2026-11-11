"""Turn the finished runs of one task into blind samples for a judge.

Usage:
  python3 eval/blind.py RAW_DIR TASK [--seed N]

Writes RAW_DIR/<task>/blind/RNN.md (the whole conversation: user turns,
assistant text, tool calls and results, final replies) with run folders
replaced by /WORKDIR, and RAW_DIR/<task>/mapping.txt (label -> arm-run).
Give the judge only the blind/ folder and rubric.md.
"""
import argparse
import hashlib
import json
import random
import shutil
from pathlib import Path


def render(run_dir):
    parts = []
    for turn in sorted(run_dir.glob("turn-*.jsonl")):
        for line in turn.read_text().splitlines():
            if not line.startswith("{"):
                continue
            d = json.loads(line)
            t = d.get("type")
            if t == "assistant":
                for c in d["message"]["content"]:
                    if c.get("type") == "tool_use":
                        parts.append("TOOL CALL:\n" + json.dumps(c["input"], ensure_ascii=False, indent=1))
            elif t == "user":
                for c in d["message"].get("content", []):
                    if isinstance(c, dict) and c.get("type") == "tool_result":
                        cc = c.get("content")
                        cc = cc if isinstance(cc, str) else json.dumps(cc, ensure_ascii=False)
                        parts.append("TOOL RESULT:\n" + cc[:3000])
            elif t == "result":
                parts.append(f"=== FINAL REPLY ({turn.stem}) ===\n" + d.get("result", ""))
        parts.insert(len(parts), "")
    return "\n\n".join(parts).replace(str(run_dir / "work"), "/WORKDIR").replace(str(run_dir), "/RUN")


def fingerprint(run_dir):
    """A hash of the run's turns: a run done again under the same name gets a new one."""
    h = hashlib.sha1()
    for turn in sorted(run_dir.glob("turn-*.jsonl")):
        h.update(turn.read_bytes())
    return h.hexdigest()


def blind_task(root, turns, seed=None, system=None):
    runs = sorted(d for d in root.iterdir() if (d / "done.json").exists())
    blind = root / "blind"
    mapping_file = root / "mapping.txt"
    prints_file = root / "runs.json"  # Older folders have none: they are checked by run name only.
    prints = {r.name: fingerprint(r) for r in runs}
    if mapping_file.exists():
        known = sorted(line.split()[1] for line in mapping_file.read_text().splitlines())
        same = known == [r.name for r in runs]
        if same and prints_file.exists():
            same = json.loads(prints_file.read_text()) == prints
        if same:
            prints_file.write_text(json.dumps(prints, indent=1) + "\n")
            return len(runs)  # Same runs: keep the labels, so existing scores stay valid.
        shutil.rmtree(blind, ignore_errors=True)  # New runs: the old scores no longer apply.
    random.Random(seed).shuffle(runs)
    blind.mkdir(exist_ok=True)
    mapping = []
    for k, run in enumerate(runs, 1):
        label = f"R{k:02d}"
        mapping.append(f"{label} {run.name}")
        header = "\n".join(f"USER TURN {n}: {t}" for n, t in enumerate(turns, 1))
        if system:  # The judge must see the instruction the user's request conflicts with.
            header = f"SYSTEM INSTRUCTION: {system}\n" + header
        (blind / f"{label}.md").write_text(header + "\n\n" + render(run))
    (root / "mapping.txt").write_text("\n".join(mapping) + "\n")
    prints_file.write_text(json.dumps(prints, indent=1) + "\n")
    return len(runs)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("raw")
    p.add_argument("task")
    p.add_argument("--seed", type=int, help="fixed seed for a reproducible shuffle; random by default")
    a = p.parse_args()
    tasks = {t["name"]: t for t in json.loads((Path(__file__).parent / "tasks.json").read_text())}
    print(blind_task(Path(a.raw) / a.task, tasks[a.task]["turns"], a.seed, tasks[a.task].get("system")), "samples")


if __name__ == "__main__":
    main()
