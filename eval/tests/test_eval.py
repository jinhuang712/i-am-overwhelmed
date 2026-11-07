"""Tests with a stub `claude`, so they cost nothing. Run: python3 -m unittest discover eval/tests"""
import json
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

from budget import Budget, estimate, past_costs  # noqa: E402
from checks import measure  # noqa: E402
from judge import dimensions, parse_scores  # noqa: E402

STUB = r'''#!/usr/bin/env python3
import json, os, re, sys, time
prompt = sys.stdin.read()
time.sleep(float(os.environ.get("STUB_SLEEP", "0")))
with open(os.environ["STUB_LOG"], "a") as f:
    f.write(json.dumps(sys.argv[1:]) + "\n")
if "json" in sys.argv and "stream-json" not in sys.argv:
    labels = re.findall(r"=== SAMPLE (R\d+) ===", prompt)
    columns = re.search(r"^Columns: (.*)$", prompt, re.M).group(1)
    rows = [l + ",2" * (columns.count(",")) for l in labels]
    print(json.dumps({"result": "notes\n```csv\n" + columns + "\n" + "\n".join(rows) + "\n```",
                      "total_cost_usd": float(os.environ["STUB_JUDGE_COST"])}))
else:
    print(json.dumps({"type": "result", "result": "- answer", "session_id": "s",
                      "total_cost_usd": float(os.environ["STUB_COST"])}))
'''


def evaluate(tmp, budget, *extra, cost="0.10", judge_cost="0.10", sleep="0"):
    stub = Path(tmp) / "bin"
    stub.mkdir(exist_ok=True)
    (stub / "claude").write_text(STUB)
    (stub / "claude").chmod(stat.S_IRWXU)
    env = {**os.environ, "PATH": f"{stub}:{os.environ['PATH']}", "STUB_LOG": str(Path(tmp) / "log"),
           "STUB_COST": cost, "STUB_JUDGE_COST": judge_cost, "STUB_SLEEP": sleep}
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

    def test_new_runs_replace_stale_scores(self):
        with tempfile.TemporaryDirectory() as tmp:
            evaluate(tmp, 2, cost="0.40", judge_cost="0.10")
            evaluate(tmp, 20, cost="0.40", judge_cost="0.10")
            self.assertEqual(sum(e["kind"] == "judge" for e in ledger(tmp)), 2)
            self.assertIn("== new (4 runs)", (Path(tmp) / "out" / "report.md").read_text())


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

    def test_measure(self):
        m = measure(["see app.py:42 and 第 3 行, not done"])
        self.assertEqual(m["line_refs"], 2)
        self.assertGreater(m["negations_per_1k"], 0)
        self.assertEqual(m["paragraph_only"], 1)


if __name__ == "__main__":
    unittest.main()
