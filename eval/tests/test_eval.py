"""Tests with a stub `claude`, so they cost nothing. Run: python3 -m unittest discover eval/tests"""
import json
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

from budget import Budget, estimate, past_costs  # noqa: E402
from checks import measure  # noqa: E402
from judge import dimensions, parse_scores  # noqa: E402
from score import summary as score_summary  # noqa: E402
from score import summary_yesno  # noqa: E402
import yesno  # noqa: E402

STUB = r'''#!/usr/bin/env python3
import fcntl, json, os, re, subprocess, sys, time
prompt = sys.stdin.read()
if os.environ.get("STUB_GIT"):  # Does the session start inside a repository? One line per run or judge.
    inside = subprocess.run(["git", "rev-parse"], capture_output=True).returncode == 0
    with open(os.environ["STUB_GIT"], "a") as f:
        f.write(("run " if "stream-json" in sys.argv else "judge ") + ("yes" if inside else "no") + "\n")
time.sleep(float(os.environ.get("STUB_SLEEP", "0")))
with open(os.environ["STUB_LOG"], "a") as f:
    f.write(json.dumps(sys.argv[1:]) + "\n")
if "json" in sys.argv and "stream-json" not in sys.argv:
    labels = re.findall(r"=== SAMPLE (\S+) ===", prompt)
    columns = re.search(r"^Columns: (.*)$", prompt, re.M).group(1)
    value = ",N" if "Values: Y, N or NA" in prompt else ",2"
    rows = [l + value * (columns.count(",")) for l in labels]
    flag = os.environ.get("STUB_FLAG")  # Say Y on this line in the first STUB_FLAG_TIMES calls that hold it.
    if flag and flag in columns.split(","):
        with open(os.environ["STUB_LOG"] + ".flag", "a+") as seen:  # Calls run in parallel: count under a lock.
            fcntl.flock(seen, fcntl.LOCK_EX)
            seen.seek(0)
            n = int(seen.read() or 0)
            seen.seek(0)
            seen.truncate()
            seen.write(str(n + 1))
        if n < int(os.environ.get("STUB_FLAG_TIMES", "999")):
            cols = columns.split(",")[1:]
            rows = [l + "".join(",Y" if c == flag else value for c in cols) for l in labels]
    print(json.dumps({"result": "notes\n```csv\n" + columns + "\n" + "\n".join(rows) + "\n```",
                      "total_cost_usd": float(os.environ["STUB_JUDGE_COST"])}))
else:
    listed = [] if os.environ.get("STUB_NO_PLUGIN") else [
        {"path": sys.argv[sys.argv.index("--plugin-dir") + 1]}] if "--plugin-dir" in sys.argv else []
    listed += [{"name": "telemetry", "path": "builtin"}]
    if os.environ.get("CLAUDE_CODE_PLUGIN_DIRS"):  # A terminal's plugin, loaded the way Claude Code does.
        listed += [{"name": "calm", "path": os.environ["CLAUDE_CODE_PLUGIN_DIRS"]}]
    if os.environ.get("STUB_FOREIGN"):
        listed += [{"name": "wt", "path": "/plugins/wt"}]
    model = sys.argv[sys.argv.index("--model") + 1]
    print(json.dumps({"type": "system", "subtype": "init", "model": model, "plugins": listed}))
    print(json.dumps({"type": "result", "result": "- answer", "session_id": "s",
                      "total_cost_usd": float(os.environ["STUB_COST"])}))
'''


def stub_env(tmp, cost="0.10", judge_cost="0.10", sleep="0"):
    """The environment of a run whose `claude` is the stub."""
    stub = Path(tmp) / "bin"
    stub.mkdir(exist_ok=True)
    (stub / "claude").write_text(STUB)
    (stub / "claude").chmod(stat.S_IRWXU)
    return {**os.environ, "PATH": f"{stub}:{os.environ['PATH']}", "STUB_LOG": str(Path(tmp) / "log"),
            "STUB_COST": cost, "STUB_JUDGE_COST": judge_cost, "STUB_SLEEP": sleep}


def evaluate(tmp, budget, *extra, cost="0.10", judge_cost="0.10", sleep="0"):
    env = stub_env(tmp, cost, judge_cost, sleep)
    cmd = [sys.executable, str(HERE / "eval.py"), "--old", "HEAD", "--new", "HEAD", "--tasks", "chat-en",
           "--runs", "4", "-j", "1", "--out", str(Path(tmp) / "out"), *extra]
    if budget is not None:
        cmd += ["--budget", str(budget)]
    return subprocess.run(cmd, env=env, capture_output=True, text=True)


def calls(tmp):
    log = Path(tmp) / "log"
    return [json.loads(line) for line in log.read_text().splitlines()] if log.exists() else []


def ledger(tmp):
    path = Path(tmp) / "out" / "ledger.jsonl"
    return [json.loads(line) for line in path.read_text().splitlines()]


class BudgetUnit(unittest.TestCase):
    def test_hold_refuses_past_the_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            b = Budget(1.0, Path(tmp) / "l")
            self.assertTrue(b.hold(0.6))
            b.settle(0.6, 0.6, kind="run")
            self.assertFalse(b.hold(0.6))

    def test_settle_releases_the_hold_and_survives_a_restart(self):
        with tempfile.TemporaryDirectory() as tmp:
            b = Budget(1.0, Path(tmp) / "l")
            b.hold(0.6)
            b.settle(0.6, 0.2, kind="run")
            self.assertTrue(b.hold(0.6))
            self.assertAlmostEqual(Budget(1.0, Path(tmp) / "l").spent, 0.2)

    def test_estimate_prefers_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp) / "a"
            d.mkdir()
            line = {"kind": "run", "status": "done", "model": "m", "task": "t", "cost": 0.5}
            (d / "ledger.jsonl").write_text(json.dumps(line) + "\n")
            cost, known = estimate([{"name": "t", "turns": ["x"]}], "m", 2, 3, past_costs(tmp))
            self.assertAlmostEqual(cost, 3.0)
            self.assertTrue(known)


class EndToEnd(unittest.TestCase):
    def test_budget_is_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = evaluate(tmp, None)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("--budget", r.stderr)
            self.assertEqual(calls(tmp), [])

    def test_a_plugin_that_did_not_load_fails_the_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            os.environ["STUB_NO_PLUGIN"] = "1"
            try:
                evaluate(tmp, 20, "--runs", "1")
            finally:
                del os.environ["STUB_NO_PLUGIN"]
            runs = [e for e in ledger(tmp) if e["kind"] == "run"]
            self.assertTrue(all(e["status"] == "failed" for e in runs))

    def test_every_session_starts_without_user_settings(self):
        with tempfile.TemporaryDirectory() as tmp:
            evaluate(tmp, 20, "--runs", "1")
            sessions = calls(tmp)
            self.assertTrue(any("stream-json" in c for c in sessions))  # runs
            self.assertTrue(any("stream-json" not in c for c in sessions))  # judges
            for c in sessions:
                self.assertEqual(c[c.index("--setting-sources") + 1], "")
                self.assertIn("--strict-mcp-config", c)
                self.assertTrue(json.loads(c[c.index("--settings") + 1])["disableAllHooks"])

    def test_a_judge_leaves_no_session_and_a_run_keeps_one(self):
        for rubric in ("scale", "yesno"):
            with self.subTest(rubric=rubric), tempfile.TemporaryDirectory() as tmp:
                evaluate(tmp, 60, "--runs", "1", "--rubric", rubric, cost="0.01", judge_cost="0.01")
                sessions = calls(tmp)
                runs = [c for c in sessions if "stream-json" in c]
                judges = [c for c in sessions if "stream-json" not in c]
                self.assertTrue(runs and judges)
                self.assertTrue(all("--no-session-persistence" in c for c in judges))
                self.assertTrue(all("--no-session-persistence" not in c for c in runs))  # A multi-turn run resumes.

    def test_a_plugin_from_outside_the_eval_fails_the_run(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.dict(os.environ, {"STUB_FOREIGN": "1"}):
            evaluate(tmp, 20, "--runs", "1")
            runs = [e for e in ledger(tmp) if e["kind"] == "run"]
            self.assertTrue(runs and all(e["status"] == "failed" for e in runs))
            errors = list((Path(tmp) / "out" / "raw").glob("*/*/error.txt"))
            self.assertTrue(errors and all("wt" in e.read_text() for e in errors))

    def test_the_terminals_plugin_stays_out(self):
        with tempfile.TemporaryDirectory() as tmp, \
                mock.patch.dict(os.environ, {"CLAUDE_CODE_PLUGIN_DIRS": "/Calm/agents/claude-code"}):
            evaluate(tmp, 20, "--runs", "1")
            runs = [e for e in ledger(tmp) if e["kind"] == "run"]
            self.assertTrue(runs and all(e["status"] == "done" for e in runs))

    def test_a_chat_run_works_outside_any_repository(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(["git", "init", "-q", tmp])  # The results folder sits inside a repository.
            seen = Path(tmp) / "git"
            with mock.patch.dict(os.environ, {"STUB_GIT": str(seen)}):
                evaluate(tmp, 20, "--runs", "1")
            runs = [line.split()[1] for line in seen.read_text().splitlines() if line.startswith("run ")]
            self.assertEqual(runs, ["no", "no"])
            self.assertEqual(list((Path(tmp) / "out" / "raw" / "chat-en").glob("*/work")), [])

    def test_a_judge_starts_outside_any_repository(self):
        for rubric in ("scale", "yesno"):
            with self.subTest(rubric=rubric), tempfile.TemporaryDirectory() as tmp:
                subprocess.run(["git", "init", "-q", tmp])  # The results folder sits inside a repository.
                seen = Path(tmp) / "git"
                with mock.patch.dict(os.environ, {"STUB_GIT": str(seen)}):
                    evaluate(tmp, 60, "--runs", "1", "--rubric", rubric, cost="0.01", judge_cost="0.01")
                judges = [line.split()[1] for line in seen.read_text().splitlines() if line.startswith("judge ")]
                self.assertTrue(judges)
                self.assertEqual(set(judges), {"no"})

    def test_no_plugin_against_the_new_version_alone(self):
        with tempfile.TemporaryDirectory() as tmp:
            cmd = [sys.executable, str(HERE / "eval.py"), "--new", "HEAD", "--none", "--tasks", "chat-en",
                   "--runs", "1", "-j", "1", "--out", str(Path(tmp) / "out"), "--budget", "20"]
            r = subprocess.run(cmd, env=stub_env(tmp), capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            arms = sorted(e["arm"] for e in ledger(tmp) if e["kind"] == "run")
            self.assertEqual(arms, ["new", "none"])
            self.assertNotIn("- old:", (Path(tmp) / "out" / "report.md").read_text())

    def test_the_plugin_path_is_absolute(self):
        with tempfile.TemporaryDirectory() as tmp:
            evaluate(tmp, 20, "--runs", "1")
            paths = [c[c.index("--plugin-dir") + 1] for c in calls(tmp) if "--plugin-dir" in c]
            self.assertEqual(len(paths), 2)
            self.assertTrue(all(os.path.isabs(p) for p in paths))

    def test_smoke_runs_every_task_once_and_judges_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            stub = Path(tmp) / "bin"
            stub.mkdir()
            (stub / "claude").write_text(STUB)
            (stub / "claude").chmod(stat.S_IRWXU)
            env = {**os.environ, "PATH": f"{stub}:{os.environ['PATH']}", "STUB_LOG": str(Path(tmp) / "log"),
                   "STUB_COST": "0.01", "STUB_JUDGE_COST": "0.01", "STUB_SLEEP": "0"}
            cmd = [sys.executable, str(HERE / "eval.py"), "--smoke", "--tasks", "chat-en,chat-zh",
                   "--budget", "5", "--out", str(Path(tmp) / "out")]
            r = subprocess.run(cmd, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("every run came through", r.stdout)
            self.assertEqual(len(calls(tmp)), 2)
            self.assertTrue(all(c[c.index("--model") + 1] == "claude-haiku-5-5" for c in calls(tmp)))

    def test_dry_run_calls_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = evaluate(tmp, None, "--dry-run")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("8 runs", r.stdout)
            self.assertEqual(calls(tmp), [])

    def test_full_run_scores_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = evaluate(tmp, 20)
            self.assertEqual(r.returncode, 0, r.stderr)
            out = Path(tmp) / "out"
            report = (out / "report.md").read_text()
            self.assertIn("== new (4 runs)", report)
            self.assertIn("== old (4 runs)", report)
            self.assertTrue((out / "chat-en-scores.csv").exists())
            self.assertEqual(len(calls(tmp)), 9)
            self.assertTrue(all("--max-budget-usd" in c for c in calls(tmp)))

    def test_parallel_runs_wait_for_a_hold_instead_of_stopping(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = evaluate(tmp, 1, "-j", "6", cost="0.01", judge_cost="0.01", sleep="0.1")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(sum(e["status"] == "done" for e in ledger(tmp)), 9)

    def test_agent_tasks_run_in_auto_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            evaluate(tmp, 20, "--tasks", "design-flaw-zh", "--runs", "1")
            agent_calls = [c for c in calls(tmp) if "--permission-mode" in c]
            self.assertEqual(len(agent_calls), 2)
            self.assertTrue(all(c[c.index("--permission-mode") + 1] == "auto" for c in agent_calls))

    def test_every_call_carries_a_cap_within_the_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            evaluate(tmp, 4)
            caps = [float(c[c.index("--max-budget-usd") + 1]) for c in calls(tmp)]
            self.assertTrue(all(0 < cap <= 4 for cap in caps))

    def test_budget_stops_runs_balanced_and_still_judges(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = evaluate(tmp, 2, cost="0.40", judge_cost="0.30")
            self.assertEqual(r.returncode, 0, r.stderr)
            entries = ledger(tmp)
            runs = [e for e in entries if e["kind"] == "run"]
            self.assertLess(len(runs), 8)
            arms = [e["arm"] for e in runs]
            self.assertLessEqual(abs(arms.count("old") - arms.count("new")), 1)
            self.assertLessEqual(sum(e["cost"] for e in entries), 2)
            self.assertEqual(sum(e["kind"] == "judge" for e in entries), 1)
            self.assertIn("incomplete", (Path(tmp) / "out" / "report.md").read_text())

    def test_resume_keeps_runs_and_counts_old_money(self):
        with tempfile.TemporaryDirectory() as tmp:
            evaluate(tmp, 2, cost="0.40", judge_cost="0.30")
            before = sum(e["kind"] == "run" for e in ledger(tmp))
            first_spent = sum(e["cost"] for e in ledger(tmp))
            evaluate(tmp, 2, cost="0.40", judge_cost="0.30")
            self.assertLessEqual(sum(e["cost"] for e in ledger(tmp)), 2)
            self.assertGreaterEqual(sum(e["cost"] for e in ledger(tmp)), first_spent)
            self.assertEqual(sum(e["kind"] == "run" for e in ledger(tmp)), before)


    def test_resume_keeps_labels_so_scores_stay_valid(self):
        with tempfile.TemporaryDirectory() as tmp:
            evaluate(tmp, 20)
            mapping = Path(tmp) / "out" / "raw" / "chat-en" / "mapping.txt"
            before = mapping.read_text()
            evaluate(tmp, 20)
            self.assertEqual(mapping.read_text(), before)
            self.assertEqual(sum(e["kind"] == "judge" for e in ledger(tmp)), 1)

    def test_a_failed_judge_retries_on_resume_with_a_share_by_size(self):
        with tempfile.TemporaryDirectory() as tmp:
            evaluate(tmp, 20, "--runs", "2", "--tasks", "chat-en,many-items-zh", cost="0.01", judge_cost="0.01")
            out = Path(tmp) / "out"
            (out / "raw" / "chat-en" / "blind" / "scores.csv").unlink()
            (out / "raw" / "many-items-zh" / "blind" / "R01.md").write_text("x" * 900)
            before = len(calls(tmp))
            (out / "raw" / "many-items-zh" / "blind" / "scores.csv").unlink()
            evaluate(tmp, 20, "--runs", "2", "--tasks", "chat-en,many-items-zh", cost="0.01", judge_cost="0.01")
            caps = [float(c[c.index("--max-budget-usd") + 1]) for c in calls(tmp)[before:]]
            self.assertEqual(len(caps), 2)
            self.assertGreater(caps[1], caps[0])

    def test_new_runs_replace_stale_scores(self):
        with tempfile.TemporaryDirectory() as tmp:
            evaluate(tmp, 2, cost="0.40", judge_cost="0.10")
            evaluate(tmp, 20, cost="0.40", judge_cost="0.10")
            self.assertEqual(sum(e["kind"] == "judge" for e in ledger(tmp)), 2)
            self.assertIn("== new (4 runs)", (Path(tmp) / "out" / "report.md").read_text())


class Reuse(unittest.TestCase):
    def runs_called(self, tmp):
        return sum("stream-json" in c for c in calls(tmp))

    def test_an_eval_takes_the_finished_runs_of_another_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            first, second = Path(tmp) / "out", Path(tmp) / "second"
            self.assertEqual(evaluate(tmp, 60).returncode, 0)
            before = self.runs_called(tmp)
            r = evaluate(tmp, 60, "--out", str(second), "--reuse", str(first), "--runs", "5")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("reuse: 8 finished runs", r.stdout)
            self.assertEqual(self.runs_called(tmp) - before, 2)  # Only the fifth run of each arm.
            self.assertIn("'kept': 8", r.stdout)
            self.assertTrue((second / "report.md").exists())

    def test_runs_on_another_model_or_task_are_not_taken(self):
        with tempfile.TemporaryDirectory() as tmp:
            first, second = Path(tmp) / "out", Path(tmp) / "second"
            evaluate(tmp, 60)
            r = evaluate(tmp, None, "--out", str(second), "--reuse", str(first), "--model", "claude-haiku-5-5",
                         "--dry-run")
            self.assertIn("reuse: 0 finished runs", r.stdout)
            done = first / "raw" / "chat-en" / "new-1" / "done.json"
            done.write_text(json.dumps({**json.loads(done.read_text()), "task": "a task that changed"}))
            r = evaluate(tmp, None, "--out", str(second), "--reuse", str(first), "--dry-run")
            self.assertIn("reuse: 7 finished runs", r.stdout)
            self.assertFalse(second.exists())  # A dry run copies nothing.

    def test_a_copied_run_names_its_new_folder(self):
        import reuse
        with tempfile.TemporaryDirectory() as tmp:
            src, dst = Path(tmp) / "a" / "new-1", Path(tmp) / "b" / "old-2"
            (src / "work").mkdir(parents=True)
            (src / "turn-1.jsonl").write_text(json.dumps({"cwd": str(src / "work")}) + "\n")
            reuse.copy([(src, dst)])
            text = (dst / "turn-1.jsonl").read_text()
            self.assertIn(str(dst / "work"), text)
            self.assertNotIn("new-1", text)


class YesNo(unittest.TestCase):
    def test_the_rubric_reads_into_decks_without_the_parked_lines(self):
        text = yesno.RUBRIC.read_text()
        decks = yesno.read_decks(text)
        self.assertGreaterEqual(len(decks), 11)
        lines = [line for d in decks for line in d["lines"]]
        self.assertEqual(len({line["id"] for line in lines}), len(lines))
        self.assertTrue(all(line["kind"] in ("bad", "good") for line in lines))
        parked = text.split("## Parked")[1]
        self.assertTrue(all(line["text"] not in parked for line in lines))

    def test_no_call_holds_more_lines_than_the_limit(self):
        cheap, strong = yesno.for_judges(yesno.read_decks(yesno.RUBRIC.read_text()))
        self.assertTrue(all(0 < len(d["lines"]) <= yesno.DECK_MAX for d in cheap + strong))
        self.assertTrue(all(line["strong"] for d in strong for line in d["lines"]))
        self.assertFalse(any(line["strong"] for d in cheap for line in d["lines"]))

    def test_every_scripted_line_has_its_script(self):
        from checks import SCRIPTED, long_bullet, scripted_answer
        lines = [line for d in yesno.read_decks(yesno.RUBRIC.read_text()) for line in d["lines"] if line["script"]]
        self.assertEqual(len(lines), len(SCRIPTED))
        for line in lines:
            self.assertIn(scripted_answer(line["text"], "=== FINAL REPLY (turn-1) ===\nfine"), ("Y", "N"))
        self.assertTrue(long_bullet("- **A**: one. Two."))
        self.assertTrue(long_bullet("1. 第一句。第二句。"))
        self.assertFalse(long_bullet("- **A**: only one, in `a.b()`"))
        self.assertFalse(long_bullet("```\n- one. two.\n```"))

    def test_a_sample_gives_its_replies_without_the_tool_calls(self):
        from checks import sample_replies
        sample = ("USER TURN 1: hi\n\nTOOL CALL:\n{}\n\n=== FINAL REPLY (turn-1) ===\none\n\n"
                  "TOOL RESULT:\nretry.py\n\n=== FINAL REPLY (turn-2) ===\ntwo\n")
        self.assertEqual(sample_replies(sample), ["one", "two"])

    def test_majority3_keeps_na_apart(self):
        self.assertEqual(yesno.majority3(["Y", "Y", "N"]), "Y")
        self.assertEqual(yesno.majority3(["N", "NA", "NA"]), "NA")
        self.assertEqual(yesno.majority3(["N", "N", "NA"]), "N")
        self.assertEqual(yesno.majority3(["Y", "N", "NA"]), "NA")
        self.assertEqual(yesno.majority3(["N"]), "N")

    def test_the_overall_score(self):
        from score import FLAG_CUT, overall_yesno, reply_score
        lines = [{"id": "C1", "kind": "bad", "deck": "Content", "flag": False},
                 {"id": "H10", "kind": "good", "deck": "Honesty", "flag": False},
                 {"id": "L10", "kind": "good", "deck": "Wording", "flag": False},
                 {"id": "H3", "kind": "bad", "deck": "Honesty", "flag": True}]
        # A bad sign avoided, a core sign missed, a plain credit not shown, no red flag.
        self.assertEqual(dict(reply_score({"C1": "N", "H10": "N", "L10": "N", "H3": "N"}, lines)),
                         {"Simple": [1, 1], "Honest": [0, 2]})
        # Lines that do not apply count for nothing.
        self.assertEqual(dict(reply_score({"C1": "NA", "H10": "NA", "L10": "N", "H3": "N"}, lines)),
                         {"Simple": [0, 0], "Honest": [0, 0]})
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "task"
            (root / "blind").mkdir(parents=True)
            (root / "mapping.txt").write_text("R01 new-1\nR02 none-1\n")
            (root / "blind" / "yesno-full.csv").write_text("label,C1,H10,L10,H3\nR01,N,Y,Y,N\nR02,Y,N,N,Y\n")
            table = overall_yesno([root], lines)
            self.assertIn("## Overall", table)
            rows = {r.split("|")[1].strip(): [c.strip() for c in r.split("|")[2:-1]] for r in table.splitlines() if r.startswith("| ")}
            self.assertEqual(rows["**score**"], ["100.0", f"{0.0 * (1 - FLAG_CUT):.1f}"])
            self.assertEqual(rows["replies with a red flag"], ["0/1", "1/1"])

    def test_majority_counts_na_as_no(self):
        self.assertEqual(yesno.majority(["Y", "Y", "N"]), "Y")
        self.assertEqual(yesno.majority(["Y", "NA", "N"]), "N")
        self.assertEqual(yesno.majority(["Y"]), "Y")

    def test_parse_rejects_a_table_with_a_wrong_label(self):
        good = "notes\n```csv\nlabel,A1,A2\nR01,Y,NA\n```"
        self.assertEqual(yesno.parse(good, ["A1", "A2"], ["R01"]), {"R01": {"A1": "Y", "A2": "NA"}})
        self.assertIsNone(yesno.parse(good, ["A1", "A2"], ["R02"]))
        self.assertIsNone(yesno.parse(good.replace("NA", "maybe"), ["A1", "A2"], ["R01"]))

    def test_a_failed_judge_call_keeps_what_it_said(self):
        deck = {"name": "Asking", "who": "reply", "about": "",
                "lines": [{"id": "A1", "text": "asks twice"}]}
        replies = [json.dumps({"result": "I cannot judge this.", "total_cost_usd": 0.01}),
                   "not json", json.dumps({"result": "```csv\nlabel,A1\nR01,Y\n```", "total_cost_usd": 0.01})]
        with tempfile.TemporaryDirectory() as tmp:
            budget = Budget(1, Path(tmp) / "ledger.jsonl")
            for reply, status, kept in zip(replies, ["failed", "failed", "done"],
                                           ["I cannot judge this.", "not json", None]):
                done = subprocess.CompletedProcess([], 0, stdout=reply, stderr="")
                with mock.patch("yesno.subprocess.run", return_value=done):
                    got, _ = yesno.ask(deck, [("R01", "a reply")], 0, "m", 0.06, Path(tmp), budget)
                self.assertEqual(got, status)
                failed = list(Path(tmp).glob("*.failed.txt"))
                self.assertEqual([f.read_text() for f in failed], [kept] if kept else [])

    def test_summary_counts_faults_credits_and_red_flags(self):
        lines = [{"id": "A1", "kind": "bad", "deck": "Asking", "flag": False},
                 {"id": "A2", "kind": "bad", "deck": "Asking", "flag": True},
                 {"id": "O1", "kind": "good", "deck": "Opinion", "flag": False}]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "blind").mkdir()
            (root / "mapping.txt").write_text("R01 new-1\nR02 old-1\n")
            (root / "blind" / "yesno.csv").write_text("label,A1,A2,O1\nR01,N,Y,Y\nR02,Y,N,N\n")
            text = summary_yesno(root, lines)
            self.assertIn("== new (1 runs): 50.0% clean, 1.0 of 1 credits", text)
            self.assertIn("red flags: A2 x1", text)
            self.assertIn("bar: failed, red flags in new: A2 x1", text)

    def test_a_full_run_with_the_yes_or_no_rubric(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = evaluate(tmp, 60, "--rubric", "yesno", "--runs", "1", cost="0.01", judge_cost="0.01")
            self.assertEqual(r.returncode, 0, r.stderr)
            out = Path(tmp) / "out"
            report = (out / "report.md").read_text()
            self.assertIn("100.0% clean", report)
            self.assertIn("## Overall", report)
            self.assertIn("bar: passed", report)
            self.assertTrue((out / "chat-en-yesno.csv").exists())
            models = {c[c.index("--model") + 1] for c in calls(tmp) if "--tools" in c and "json" in c}
            self.assertIn("claude-haiku-5-5", models)
            before = len(calls(tmp))
            evaluate(tmp, 60, "--rubric", "yesno", "--runs", "1", cost="0.01", judge_cost="0.01")
            self.assertEqual(len(calls(tmp)), before)


    def test_a_changed_rubric_is_judged_again_from_the_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            args = ("--rubric", "yesno", "--runs", "1")
            first = evaluate(tmp, 60, *args, cost="0.01", judge_cost="0.01")
            self.assertIn("judge chat-en: done", first.stdout)
            again = evaluate(tmp, 60, *args, cost="0.01", judge_cost="0.01")
            self.assertIn("judge chat-en: skipped", again.stdout)
            self.assertIn("runs: {'kept': 2}", again.stdout)
            stamp = Path(tmp) / "out" / "raw" / "chat-en" / "blind" / "yesno.rubric"
            stamp.write_text("an older rubric\n")
            before = len(calls(tmp))
            changed = evaluate(tmp, 60, *args, cost="0.01", judge_cost="0.01")
            self.assertIn("judge chat-en: done", changed.stdout)
            self.assertEqual(len(calls(tmp)), before)  # Every answer came from the cache.

    def test_a_run_done_again_under_its_name_gets_new_samples(self):
        with tempfile.TemporaryDirectory() as tmp:
            args = ("--rubric", "yesno", "--runs", "1")
            evaluate(tmp, 60, *args, cost="0.01", judge_cost="0.01")
            task = Path(tmp) / "out" / "raw" / "chat-en"
            turn = task / "new-1" / "turn-1.jsonl"
            turn.write_text(turn.read_text().replace('"- answer"', '"- a new answer"'))
            evaluate(tmp, 60, *args, cost="0.01", judge_cost="0.01")
            samples = " ".join(f.read_text() for f in (task / "blind").glob("R*.md"))
            self.assertIn("a new answer", samples)

    def strong_flag_run(self, times):
        """Return (strong judge calls, answers on H3) for a yes or no run where the strong judge says Y on H3."""
        with tempfile.TemporaryDirectory() as tmp, \
                mock.patch.dict(os.environ, {"STUB_FLAG": "H3", "STUB_FLAG_TIMES": str(times)}):
            r = evaluate(tmp, 60, "--rubric", "yesno", "--runs", "1", cost="0.01", judge_cost="0.01")
            self.assertEqual(r.returncode, 0, r.stderr)
            strong = [c for c in calls(tmp) if "json" in c and c[c.index("--model") + 1] == "claude-opus-5-5"]
            csv = (Path(tmp) / "out" / "chat-en-yesno.csv").read_text().splitlines()
            column = csv[0].split(",").index("H3")
            return len(strong), [row.split(",")[column] for row in csv[1:]]

    def strong_calls(self):
        """Calls the strong judge gets for one batch: one per part of its deck."""
        return len(yesno.for_judges(yesno.read_decks(yesno.RUBRIC.read_text()))[1])

    def test_a_red_flag_the_strong_judge_raises_once_does_not_count(self):
        count, answers = self.strong_flag_run(times=1)
        self.assertEqual(count, self.strong_calls() + yesno.FLAG_PASSES - 1)  # Only the part that holds H3 again.
        self.assertEqual(answers, ["N", "N"])

    def test_a_red_flag_the_strong_judge_keeps_raising_counts(self):
        count, answers = self.strong_flag_run(times=99)
        self.assertEqual(count, self.strong_calls() + yesno.FLAG_PASSES - 1)
        self.assertEqual(answers, ["Y", "Y"])

    def test_no_red_flag_no_more_strong_passes(self):
        count, _ = self.strong_flag_run(times=0)
        self.assertEqual(count, self.strong_calls())


class FlagCheck(unittest.TestCase):
    def check(self, tmp, *extra):
        cases = Path(tmp) / "cases"
        cases.mkdir()
        (cases / "r.md").write_text("USER TURN 1: hi\n\n=== FINAL REPLY (turn-1) ===\n- answer\n")
        (cases / "cases.json").write_text(json.dumps([{"name": "c1", "reply": "r.md", "expect": {"H3": "N"}}]))
        cmd = [sys.executable, str(HERE / "flag_check.py"), "--cases", str(cases), *extra]
        return subprocess.run(cmd, env=stub_env(tmp, judge_cost="0.01"), capture_output=True, text=True)

    def test_a_right_answer_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = self.check(tmp, "--budget", "5")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("1 of 1 right", r.stdout)

    def test_a_wrong_red_flag_fails(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.dict(os.environ, {"STUB_FLAG": "H3"}):
            r = self.check(tmp, "--budget", "5")
            self.assertEqual(r.returncode, 1, r.stderr)
            self.assertIn("BAD c1 H3: expected N, got Y", r.stdout)

    def test_a_dry_run_calls_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = self.check(tmp, "--dry-run")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(calls(tmp), [])


class Parsing(unittest.TestCase):
    def test_parse_scores_rejects_a_missing_label(self):
        header = ",".join(["label", *dimensions()])
        row = "R01" + ",1" * len(dimensions())
        text = f"```csv\n{header}\n{row}\n```"
        self.assertIn("R01", parse_scores(text, ["R01"]))
        with self.assertRaises(ValueError):
            parse_scores(text, ["R01", "R02"])

    def test_rubric_has_the_new_rules(self):
        self.assertIn("D14", dimensions())
        self.assertIn("G4", dimensions())
        self.assertIn("H1", dimensions())
        self.assertIn("F4", dimensions())
        self.assertIn("D15", dimensions())
        self.assertIn("D19", dimensions())
        self.assertIn("D20", dimensions())
        self.assertIn("D21", dimensions())
        self.assertIn("D22", dimensions())
        self.assertIn("R6", dimensions())
        self.assertIn("D23", dimensions())
        self.assertIn("D24", dimensions())
        self.assertNotIn("D25", dimensions())
        self.assertIn("D26", dimensions())
        self.assertIn("E3", dimensions())
        self.assertIn("B5", dimensions())
        self.assertIn("B6", dimensions())
        self.assertNotIn("E2", dimensions())

    def test_measure(self):
        m = measure(["see app.py:42 and 第 3 行, not done"])
        self.assertEqual(m["line_refs"], 2)
        self.assertGreater(m["negations_per_1k"], 0)
        self.assertEqual(m["paragraph_only"], 1)
        self.assertEqual(measure(["📍 goal · decided: x · open: y\n- a"])["anchors"], 1)
        shaped = measure(["# Flow\n```\na\n└── b → c\n```\n| x | y |\n> note\nGo on?", "```diff\n- a -> b\n```\nDone."])
        self.assertEqual(shaped["drawings"], 1)
        self.assertEqual(shaped["tables"], 1)
        self.assertEqual(shaped["quotes"], 1)
        self.assertEqual(shaped["headings"], 1)
        self.assertEqual(shaped["ends_asking"], 1)
        self.assertEqual(shaped["lines"], 12)

    def write_scores(self, root, rows):
        (root / "blind").mkdir(parents=True)
        (root / "mapping.txt").write_text("R01 new-1\nR02 old-1\n")
        (root / "blind" / "scores.csv").write_text("label,R1,R3,B1,E1\n" + rows)

    def test_a_red_flag_fails_the_bar(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "task"
            self.write_scores(root, "R01,3,0,3,NA\nR02,3,3,2,NA\n")
            text = score_summary(root)
            self.assertIn("red flags: R3 x1", text)
            self.assertIn("bar: failed, red flags in new: R3 x1", text)
            self.assertIn("100.0% of points", text)

    def test_the_bar_passes_and_fails_on_the_margin(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "ok"
            self.write_scores(root, "R01,3,NA,3,NA\nR02,3,3,3,NA\n")
            self.assertIn("bar: passed", score_summary(root))
            root = Path(tmp) / "low"
            self.write_scores(root, "R01,3,3,2,NA\nR02,3,3,3,NA\n")
            self.assertIn("bar: failed, new is more than 3 points under old", score_summary(root))

    def test_ends_asking(self):
        fact = "401 asks: who are you?\n- **401**: no identity.\n- **403**: no permission."
        self.assertEqual(measure([fact])["ends_asking"], 0)
        numbered = "Explained.\n\nQ1. Which one?\n- A. ✅ this\n- B. that\n\nReasons:\n- one\n- two\n- three"
        self.assertEqual(measure([numbered])["ends_asking"], 1)
        options = "Which one\n- A. this\n- B. that"
        self.assertEqual(measure([options])["ends_asking"], 1)
        self.assertEqual(measure(["Done.\n\nGo on?"])["ends_asking"], 1)


class RuleFiles(unittest.TestCase):
    def test_codex_rules_match_the_output_style(self):
        """The two rule files differ only in the frontmatter and the question-tools line."""
        repo = Path(__file__).resolve().parents[2]
        style = (repo / "plugin/output-styles/i-am-overwhelmed.md").read_text()
        codex = (repo / "codex/AGENTS.md").read_text()
        body = style.split("---\n", 2)[2].lstrip("\n")
        tools = "question tools"
        style_lines = [line for line in body.splitlines() if tools not in line]
        codex_lines = [line for line in codex.splitlines() if tools not in line]
        self.assertEqual(style_lines, codex_lines)
        self.assertEqual(sum(tools in line for line in body.splitlines()), 1)
        self.assertEqual(sum(tools in line for line in codex.splitlines()), 1)


if __name__ == "__main__":
    unittest.main()
