"""Run one task against one version of the plugin, under the budget.

Each run is a fresh `claude -p` session that starts with only what the eval gives
it: CLAUDE.md files off, user settings off (with them the owner's plugins, hooks and
skills), the terminal's plugins off, and the installed copy of the plugin disabled. So
the only difference between arms is the plugin directory. Multi-turn tasks continue the same session with --resume.

Output: RAW/<task>/<arm>-<i>/turn-<k>.jsonl, done.json when the run finished.
"""
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
# Settings for every session, the judges' too. User settings bring the owner's plugins,
# hooks and skills. On 2026-11-11 a hook from one of them spoke in 66 of 114 runs, two
# replies answered it, and two named the owner's company from a skill's name.
SETTINGS = json.dumps({"enabledPlugins": {"i-am-overwhelmed@i-am-overwhelmed": False},
                       "disableAllHooks": True, "autoMemoryEnabled": False})
# No setting source at all, and no MCP server but the ones named: the way spawn-claude starts a child.
ISOLATE = ["--settings", SETTINGS, "--setting-sources", "", "--strict-mcp-config"]
# A judge's session is not saved. Every saved session holds the account's email, and a judge
# is never resumed. A run is saved: a multi-turn task goes on with --resume.
NO_LOG = ["--no-session-persistence"]
# One reply may not run past this many output tokens. --max-budget-usd is checked
# between turns only, so a reply that loops would otherwise run to the model's limit:
# on 2026-11-10 three chat runs wrote 128,000 tokens each, $2.56 a run against a $0.15 cap.
MAX_OUTPUT_TOKENS = "16000"
CLEAN_ENV = {"CLAUDE_CODE_DISABLE_CLAUDE_MDS": "1", "CLAUDE_CODE_MAX_OUTPUT_TOKENS": MAX_OUTPUT_TOKENS}
LIMIT_NOTE = "You've hit your"  # The start of the reply when the account's usage limit is reached.


def clean_env():
    """The environment for a session: the eval's variables, and no plugin the terminal adds."""
    env = {**os.environ, **CLEAN_ENV}
    env.pop("CLAUDE_CODE_PLUGIN_DIRS", None)  # Calm, for one, loads its own plugin through it.
    return env


def fence_off(work):
    """Make the work folder a git repository of its own.

    The folder sits inside this repository. Without its own .git, a `git status` or a
    `git commit` by the agent would act on this repository, and on 2026-11-11 an agent
    read this project's CI file and took it for the fixture's.
    """
    git = ["git", "-C", str(work), "-c", "user.name=eval", "-c", "user.email=eval@example.invalid"]
    for args in (["init", "-q"], ["add", "-A"], ["commit", "-q", "-m", "fixture"]):
        subprocess.run(git + args, capture_output=True)


def chat_folder():
    """Make an empty folder outside any git repository, for a chat run.

    A chat run has no tools. In a repository, even an empty one of its own, Opus took
    "our site" for code to read and wrote made-up tool calls until the cap stopped it:
    on 2026-11-11, 5 of 6 shape-en runs, and 2 of 2 in a probe against 0 of 3 outside.
    """
    return Path(tempfile.mkdtemp(prefix="eval-chat-"))


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


def foreign_plugins(events, plugin_dir):
    """Names of the plugins in the session that are neither this arm's nor Claude Code's own."""
    inits = [e for e in events if e.get("type") == "system" and e.get("subtype") == "init"]
    if not inits:
        return []
    own = os.path.realpath(plugin_dir) if plugin_dir else None
    return [p.get("name") for p in inits[0].get("plugins", [])
            if p.get("path") != "builtin" and os.path.realpath(str(p.get("path"))) != own]


def run_one(task, arm, plugin_dir, i, raw, model, effort, budget, cap, limit):
    """Return one of: done, skipped, stopped, failed."""
    run_dir = raw / task["name"] / f"{arm}-{i}"
    if (run_dir / "done.json").exists():
        return "skipped"
    if not budget.hold(cap, limit):
        return "stopped"
    cost, status, outside = 0.0, "failed", None
    try:
        shutil.rmtree(run_dir, ignore_errors=True)
        run_dir.mkdir(parents=True)
        if task["kind"] == "agent":
            work = run_dir / "work"
            work.mkdir()
            if task.get("fixture"):
                shutil.copytree(REPO / task["fixture"], work, dirs_exist_ok=True)
            fence_off(work)
        else:
            work = outside = chat_folder()
        base =["claude", "-p", "--model", model, "--effort", effort, *ISOLATE,
                "--output-format", "stream-json", "--verbose"]
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
            res = subprocess.run(cmd, cwd=work, env=clean_env(),
                                 input=prompt, capture_output=True, text=True)
            (run_dir / f"turn-{k}.jsonl").write_text(res.stdout)
            events = [json.loads(line) for line in res.stdout.splitlines() if line.startswith("{")]
            results = [e for e in events if e.get("type") == "result"]
            if plugin_dir and not plugin_loaded(events, plugin_dir):
                cost = max(cost, sum(r.get("total_cost_usd") or 0 for r in results))
                (run_dir / "error.txt").write_text(f"the plugin at {plugin_dir} was not loaded")
                return status
            if foreign := foreign_plugins(events, plugin_dir):
                cost = max(cost, sum(r.get("total_cost_usd") or 0 for r in results))
                (run_dir / "error.txt").write_text(f"plugins from outside the eval: {', '.join(foreign)}")
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
        if outside:
            shutil.rmtree(outside, ignore_errors=True)
        budget.settle(cap, cost, kind="run", task=task["name"], arm=arm, run=i,
                      model=model, status=status)
