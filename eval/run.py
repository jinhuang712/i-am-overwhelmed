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
# One reply may not run past this many output tokens. --max-budget-usd is checked
# between turns only, so a reply that loops would otherwise run to the model's limit:
# on 2026-11-10 three chat runs wrote 128,000 tokens each, $2.56 a run against a $0.15 cap.
MAX_OUTPUT_TOKENS = "16000"
CLEAN_ENV = {"CLAUDE_CODE_DISABLE_CLAUDE_MDS": "1", "CLAUDE_CODE_MAX_OUTPUT_TOKENS": MAX_OUTPUT_TOKENS}
LIMIT_NOTE = "You've hit your"  # The start of the reply when the account's usage limit is reached.


def fence_off(work):
    """Make the work folder a git repository of its own.

    The folder sits inside this repository. Without its own .git, a `git status` or a
    `git commit` by the agent would act on this repository, and on 2026-11-11 an agent
    read this project's CI file and took it for the fixture's.
    """
    git = ["git", "-C", str(work), "-c", "user.name=eval", "-c", "user.email=eval@example.invalid"]
    for args in (["init", "-q"], ["add", "-A"], ["commit", "-q", "-m", "fixture"]):
        subprocess.run(git + args, capture_output=True)


def plugin_loaded(events, plugin_dir):
    """True when the session's start event lists the plugin of this arm.

    Claude Code skips a --plugin-dir it cannot find and says nothing. On 2026-11-10 a
    relative path did that to a whole eval: every arm ran with no plugin.
    """
    inits = [e for e in events if e.get("type") == "system" and e.get("subtype") == "init"]
    if not inits or "plugins" not in inits[0]:
        return True  # No list to check against.
    want = os.path.realpath(plugin_dir)
    return any(os.path.realpath(str(p.get("path"))) == want for p in inits[0]["plugins"])


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
            fence_off(work)
        base = ["claude", "-p", "--model", model, "--effort", effort,
                "--settings", DISABLE_INSTALLED, "--output-format", "stream-json", "--verbose"]
        if plugin_dir:  # The "none" arm runs with no plugin at all.
            base += ["--plugin-dir", str(plugin_dir)]
        if task.get("system"):  # An instruction above the user's, to set a trap where the two conflict.
            base += ["--append-system-prompt", task["system"]]
        if task["kind"] == "agent":
            base += ["--permission-mode", "auto"]
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
            if plugin_dir and not plugin_loaded(events, plugin_dir):
                cost = max(cost, sum(r.get("total_cost_usd") or 0 for r in results))
                (run_dir / "error.txt").write_text(f"the plugin at {plugin_dir} was not loaded")
                return status
            if not results or results[-1].get("total_cost_usd") is None:
                cost = max(cost, cap)  # Unknown spend counts as the whole hold.
                (run_dir / "error.txt").write_text(res.stderr[-2000:])
                return status
            cost += results[-1]["total_cost_usd"]
            if results[-1].get("is_error") or str(results[-1].get("result", "")).startswith(LIMIT_NOTE):
                (run_dir / "error.txt").write_text(str(results[-1].get("subtype")))
                return status
            session = results[-1]["session_id"]
        (run_dir / "done.json").write_text(json.dumps({"cost": cost}))
        status = "done"
        return status
    finally:
        budget.settle(cap, cost, kind="run", task=task["name"], arm=arm, run=i,
                      model=model, status=status)
