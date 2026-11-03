"""Run every task in tasks.json against several versions ("arms") of the plugin.

Usage:
  python3 examples/eval/run.py OUT_DIR ARM=PLUGIN_DIR [ARM=PLUGIN_DIR ...]
      [--runs N] [--tasks a,b] [-j JOBS] [--model M] [--effort E]

Each run is a fresh `claude -p` session with CLAUDE.md files off and the
installed copy of the plugin disabled, so the only difference between arms is
the plugin directory. Multi-turn tasks continue the same session with --resume.

Output: OUT_DIR/<task>/<arm>-<i>/turn-<k>.jsonl, plus work/ for agent tasks.
"""
import argparse
import json
import os
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DISABLE_INSTALLED = json.dumps({"enabledPlugins": {"i-am-overwhelmed@i-am-overwhelmed": False}})


def run_one(task, arm, plugin_dir, i, out, model, effort):
    run_dir = out / task["name"] / f"{arm}-{i}"
    work = run_dir / "work"
    work.mkdir(parents=True, exist_ok=True)
    if task.get("fixture"):
        shutil.copytree(REPO / task["fixture"], work, dirs_exist_ok=True)
    env = {**os.environ, "CLAUDE_CODE_DISABLE_CLAUDE_MDS": "1"}
    base = ["claude", "-p", "--model", model, "--effort", effort,
            "--settings", DISABLE_INSTALLED, "--plugin-dir", str(plugin_dir),
            "--output-format", "stream-json", "--verbose"]
    if task["kind"] == "agent":
        base += ["--permission-mode", "bypassPermissions"]
    else:
        base += ["--tools", ""]
    session = None
    for k, prompt in enumerate(task["turns"], 1):
        # The prompt goes in on stdin: --tools is variadic and would swallow it.
        cmd = base + (["--resume", session] if session else [])
        res = subprocess.run(cmd, cwd=work, env=env, input=prompt, capture_output=True, text=True)
        (run_dir / f"turn-{k}.jsonl").write_text(res.stdout)
        result = [json.loads(l) for l in res.stdout.splitlines() if l.startswith("{")]
        result = [r for r in result if r.get("type") == "result"]
        if not result:
            raise RuntimeError(f"{run_dir} turn {k} failed: {res.stderr[-500:]}")
        session = result[-1]["session_id"]
    return str(run_dir)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("out")
    p.add_argument("arms", nargs="+")
    p.add_argument("--runs", type=int, default=5)
    p.add_argument("--tasks")
    p.add_argument("-j", type=int, default=6)
    p.add_argument("--model", default="claude-sonnet-5-5")
    p.add_argument("--effort", default="medium")
    a = p.parse_args()
    tasks = json.loads((Path(__file__).parent / "tasks.json").read_text())
    if a.tasks:
        tasks = [t for t in tasks if t["name"] in a.tasks.split(",")]
    arms = dict(x.split("=", 1) for x in a.arms)
    out = Path(a.out)
    jobs = [(t, arm, Path(d).resolve(), i, out, a.model, a.effort)
            for t in tasks for arm, d in arms.items() for i in range(1, a.runs + 1)]
    with ThreadPoolExecutor(a.j) as ex:
        for done in ex.map(lambda j: run_one(*j), jobs):
            print("done", done, flush=True)


if __name__ == "__main__":
    main()
