"""Turn the runs of one task into blind samples for a judge.

Usage:
  python3 examples/eval/blind.py OUT_DIR TASK [--seed N]

Writes OUT_DIR/<task>/blind/RNN.md (the whole conversation: user turns,
assistant text, tool calls and results, final replies) with run folders
replaced by /WORKDIR, and OUT_DIR/<task>/mapping.txt (label -> arm-run).
Give the judge only the blind/ folder and rubric.md.
"""
import argparse
import json
import random
from pathlib import Path


def render(run_dir):
    parts = []
    for turn in sorted(run_dir.glob("turn-*.jsonl")):
        prompt = None
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


def main():
    p = argparse.ArgumentParser()
    p.add_argument("out")
    p.add_argument("task")
    p.add_argument("--seed", type=int, help="fixed seed for a reproducible shuffle; random by default")
    a = p.parse_args()
    root = Path(a.out) / a.task
    tasks = {t["name"]: t for t in json.loads((Path(__file__).parent / "tasks.json").read_text())}
    turns = tasks[a.task]["turns"]
    runs = sorted(d for d in root.iterdir() if d.is_dir() and d.name not in ("blind",))
    random.Random(a.seed).shuffle(runs)
    blind = root / "blind"
    blind.mkdir(exist_ok=True)
    mapping = []
    for k, run in enumerate(runs, 1):
        label = f"R{k:02d}"
        mapping.append(f"{label} {run.name}")
        header = "\n".join(f"USER TURN {n}: {t}" for n, t in enumerate(turns, 1))
        (blind / f"{label}.md").write_text(header + "\n\n" + render(run))
    (root / "mapping.txt").write_text("\n".join(mapping) + "\n")
    print(f"{len(runs)} samples in {blind}")


if __name__ == "__main__":
    main()
