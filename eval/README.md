# Eval: compare versions of the style

A repeatable A/B, kept as a tool: run the same tasks against two versions of the plugin, blind the replies, have a model judge score them with [`rubric.md`](rubric.md), then unblind.

## Run it

See the plan and the estimate first. This spends nothing:

```bash
python3 eval/eval.py --old <git ref> --dry-run
```

Then run with a limit:

```bash
python3 eval/eval.py --old <git ref> --new HEAD --budget <usd>
```

`--budget` is required. `--model`, `--effort`, `--judge-model`, `--runs`, `--tasks` and `-j` are optional; `--help` lists them.

Results go to `eval/results/<date>-<old>-vs-<new>-<model>/`: `report.md`, `ledger.jsonl`, and scores and mappings per task. `raw/` holds the runs and is git-ignored.

## Budget

- **The limit covers everything**: runs and judging. A quarter is kept back for judging.
- **Every call has a cap**: each `claude -p` gets `--max-budget-usd`, and it holds that cap before it starts.
- **A stop stays usable**: whole rounds run first, so the arms stay balanced. Finished runs still get judged, and the report says the eval is incomplete.
- **Resume is the same command**: finished runs are kept. Their cost stays in `ledger.jsonl`, so the limit applies across both sessions.
- **More money is a higher `--budget`**: new runs join the old ones, and the task is judged again.
- **Unknown spend counts in full**: a call that reports no cost counts as its whole cap.
- **Estimates improve with use**: `--dry-run` reads past ledgers. Until a model has history it uses a rough default and says so.
- **The limit is as exact as `--max-budget-usd`**: a call may overrun its cap a little.

## Files

| File | What it is |
|---|---|
| [`eval.py`](eval.py) | The one command |
| [`budget.py`](budget.py) | The limit, the ledger and the estimate |
| [`run.py`](run.py) | One run of a task |
| [`blind.py`](blind.py) | Blind samples and the label mapping |
| [`judge.py`](judge.py) | The model judge |
| [`score.py`](score.py) | Unblinds and summarises the scores |
| [`checks.py`](checks.py) | Mechanical checks: line references, negations, paragraph-only replies. Free |
| [`tasks.json`](tasks.json) | The tasks. A task with several `turns` continues one session |
| [`rubric.md`](rubric.md) | The dimensions |
| [`fixtures/`](fixtures/) | `many-bugs/`, `free-text-due/`, and their answer keys, kept outside them |
| [`tests/`](tests/) | Tests with a stub `claude`, so they cost nothing: `python3 -m unittest discover eval/tests` |

Every run has `CLAUDE.md` files off and the installed plugin disabled, so the only difference between arms is the plugin directory. Agent tasks run in auto mode, so the permission classifier reviews their calls.

## Results, 2026-11-03: 0.1.8 vs the tagged rewrite

Sonnet 5.5, medium effort, 5 runs per arm per task, Opus as the judge. "old" is 0.1.8; "new" is the `[YES]` / `[NO]` / `[MAYBE]` / `[WHEN]` rewrite. Scores and label mappings are in [`results/2026-11-03/`](results/2026-11-03/).

| Task | old | new | Biggest differences |
|---|---|---|---|
| `chat-en` | 76.9% | 82.6% | Guesses marked: 1.0 → 2.6 |
| `chat-zh` | 85.7% | 91.3% | Guesses marked: 1.6 → 3.0 |
| `multi-turn-zh` | 74.1% | 87.1% | Drift flagged: 0.2 → 2.2. Guesses marked: 1.6 → 3.0. Goal kept: 1.2 → 2.0 |
| `fix-test-zh` | 85.3% | 90.6% | `diff` block shown: 0 of 5 → 5 of 5. Run before `run.py` existed, with an earlier rubric |

- Both versions held their position against the wrong pushback in every run.
- Both versions answered simple chat questions in Detailed mode every time (mode fit 1.0–2.0 of 3).
- The new version uses somewhat more decorative emoji, e.g. on headings.
- The optional recap, when used in single-turn chats, mostly restated the question. Humor was never used.
- In `fix-test-zh`, an in-between version without "Say what you actually verified" claimed "CI is fixed" after local runs in 4 of 5 runs; with the rule, 0 of 5.
- In this run `blind.py` used a fixed seed, so the label order was the same in all three tasks and grouped by arm (R01–R05 old, R06–R10 new). The judge never saw the mapping, but the grouping may have made patterns easier to see. The shuffle is now random by default.

## Results, 2026-11-03: Simple mode and format rules

Same setup. Arms: "hybrid" (Simple defined as a few lines with no headings, plus "a question with a short answer uses Simple"), "round 8" (adds the format rules, a reworded drift rule and a reworded diff rule), and "round 9" (round 8 with the drift and diff triggers restored and no comma limit on bullets). One judge scored all three arms of a task together. Scores and mappings are in [`results/2026-11-03-simple-mode/`](results/2026-11-03-simple-mode/); the hybrid runs are the same runs judged in earlier rounds.

| Task | hybrid | round 8 | round 9 |
|---|---|---|---|
| `chat-en` | 78.7% | 84.2% | 84.6% |
| `chat-zh` | 90.7% | 93.5% | 94.0% |
| `fix-test-zh` | 94.8% | 91.6% | 96.2% |
| `multi-turn-zh` | 84.4% | 83.5% | 89.1% |

- **Mode fit**: before "Simple" had a definition and a trigger, every simple chat question got a sectioned Detailed reply; a trigger alone helped a little, the definition did most of the work.
- **Triggers matter**: "You show a local difference" dropped `diff` blocks from 2.6 to 0.6 of 3, while "You changed code or text" brought them back to 3.0.
- **Drift**: "say where that goal stands" made replies report progress without flagging the drift, and it led them to say the user had already decided; "We drift from the original goal: tell me" worked better.
- **Bullet commas**: a one-comma limit was broken in most bullets and made replies cramped; one sentence per bullet was mostly kept.
- **Still open**: replies sometimes call an undecided choice "decided", yes/no questions often skip the A/B options, and short English answers often miss the risk that would flip them.

## Caveats

- The judge is a model and the rubric is written from the style's own rules, so it favours whichever version states those rules more directly. Read the quotes, not just the totals.
- 5 runs per arm are samples, not measurements.
- `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1` turns off `CLAUDE.md` files, but Claude Code still adds account context such as your email to every session. One reply named the runner's company although no prompt mentioned it. It affects all arms equally.
