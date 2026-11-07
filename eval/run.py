"""Run one task against one version of the plugin, under the budget.

Each run is a fresh `claude -p` session with CLAUDE.md files off and the installed
copy of the plugin disabled, so the only difference between arms is the plugin
directory. Multi-turn tasks continue the same session with --resume.

Output: RAW/<task>/<arm>-<i>/turn-<k>.jsonl, done.json when the run finished.
"""
import json
import os
import shutil
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DISABLE_INSTALLED = json.dumps({"enabledPlugins": {"i-am-overwhelmed@i-am-overwhelmed": False}})
CLEAN_ENV = {"CLAUDE_CODE_DISABLE_CLAUDE_MDS": "1"}


def run_one(task, arm, plugin_dir, i, raw, model, effort, budget, cap, limit):
    """Return one of: done, skipped, stopped, failed."""
    run_dir = raw / task["name"] / f"{arm}-{i}"
    if (run_dir / "done.json").exists():
        return "skipped"
    if not budget.hold(cap, limit):
        return "stopped"
    cost, status = 0.0, "failed"
    try:
        shutil.rmtree(run_dir, ignore_errors=True)
        work = run_dir / "work"
        work.mkdir(parents=True)
        if task.get("fixture"):
            shutil.copytree(REPO / task["fixture"], work, dirs_exist_ok=True)
        base = ["claude", "-p", "--model", model, "--effort", effort,
                "--settings", DISABLE_INSTALLED, "--plugin-dir", str(plugin_dir),
                "--output-format", "stream-json", "--verbose"]
        if task["kind"] == "agent":
            base += ["--permission-mode", "bypassPermissions"]
        else:
            base += ["--tools", ""]
        session = None
        for k, prompt in enumerate(task["turns"], 1):
            left = max(cap - cost, 0.01)
            cmd = base + ["--max-budget-usd", f"{left:.2f}"]
            cmd += ["--resume", session] if session else []
            # The prompt goes in on stdin: --tools is variadic and would swallow it.
            res = subprocess.run(cmd, cwd=work, env={**os.environ, **CLEAN_ENV},
                                 input=prompt, capture_output=True, text=True)
            (run_dir / f"turn-{k}.jsonl").write_text(res.stdout)
            events = [json.loads(line) for line in res.stdout.splitlines() if line.startswith("{")]
            results = [e for e in events if e.get("type") == "result"]
            if not results or results[-1].get("total_cost_usd") is None:
                cost = max(cost, cap)  # Unknown spend counts as the whole hold.
                (run_dir / "error.txt").write_text(res.stderr[-2000:])
                return status
            cost += results[-1]["total_cost_usd"]
            if results[-1].get("is_error"):
                (run_dir / "error.txt").write_text(str(results[-1].get("subtype")))
                return status
            session = results[-1]["session_id"]
        (run_dir / "done.json").write_text(json.dumps({"cost": cost}))
        status = "done"
        return status
    finally:
        budget.settle(cap, cost, kind="run", task=task["name"], arm=arm, run=i,
                      model=model, status=status)
