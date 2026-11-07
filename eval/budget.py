"""Spending guard for the eval: a ledger of real costs plus holds on running calls.

A call holds its full cap before it starts, so the caps of running calls stay
within the limit. When a call ends, its hold is swapped for the reported cost.
Each cap is enforced by `claude --max-budget-usd`, so the limit is as exact as that flag.
The ledger is a file, so a resumed eval keeps counting the money already spent.
"""
import json
import threading
from collections import defaultdict
from pathlib import Path

DEFAULT_RUN_COST = 0.25  # $4.4 for 40 Sonnet runs, rounded up. Used until history exists.


class Budget:
    def __init__(self, total, ledger):
        self.total = total
        self.ledger = Path(ledger)
        self.lock = threading.Lock()
        self.held = 0.0
        self.spent = 0.0
        if self.ledger.exists():
            self.spent = sum(json.loads(line)["cost"] for line in self.ledger.read_text().splitlines())

    def hold(self, amount, limit=None):
        limit = self.total if limit is None else limit
        with self.lock:
            if self.spent + self.held + amount > limit:
                return False
            self.held += amount
            return True

    def settle(self, held, cost, **record):
        with self.lock:
            self.held -= held
            self.spent += cost
            self.ledger.parent.mkdir(parents=True, exist_ok=True)
            with self.ledger.open("a") as f:
                f.write(json.dumps({**record, "cost": cost}, ensure_ascii=False) + "\n")


def past_costs(results_dir):
    """Mean cost of a finished run, by (model, task) and by model, from past ledgers."""
    samples = defaultdict(list)
    for ledger in Path(results_dir).glob("*/ledger.jsonl"):
        for line in ledger.read_text().splitlines():
            r = json.loads(line)
            if r.get("kind") == "run" and r.get("status") == "done":
                samples[(r["model"], r["task"])].append(r["cost"])
                samples[r["model"]].append(r["cost"])
    return {k: sum(v) / len(v) for k, v in samples.items()}


def estimate(tasks, model, arms, runs, history):
    """Return (estimated run cost, whether every figure came from history)."""
    total, known = 0.0, True
    for t in tasks:
        cost = history.get((model, t["name"]), history.get(model))
        if cost is None:
            cost, known = DEFAULT_RUN_COST * len(t["turns"]), False
        total += cost * arms * runs
    return total, known
