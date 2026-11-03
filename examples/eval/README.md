# Eval: compare versions of the style

A small, repeatable A/B: run the same tasks against two or more versions of the plugin, blind the replies, have a judge score them with [`rubric.md`](rubric.md), then unblind.

## Files

| File | What it is |
|---|---|
| [`tasks.json`](tasks.json) | The tasks. `agent` tasks run with tools in a copy of a fixture; `chat` tasks run with no tools. A task with several `turns` continues one session. |
| [`rubric.md`](rubric.md) | 28 dimensions in six groups: task outcome, honesty, skimmability, reply rules, optional touches, multi-turn. |
| [`run.py`](run.py) | Runs every task × arm × run with `claude -p`. |
| [`blind.py`](blind.py) | Shuffles one task's runs into `blind/RNN.md` and writes `mapping.txt`. |
| [`score.py`](score.py) | Joins the judge's `blind/scores.csv` with `mapping.txt` and prints per-arm results. |

## Run it

```bash
# 1. An arm is NAME=PLUGIN_DIR. Export the old version from git:
mkdir -p /tmp/arms/old && git archive master plugin | tar -x -C /tmp/arms/old

# 2. Run (5 runs per task per arm, 6 at a time)
python3 examples/eval/run.py /tmp/out old=/tmp/arms/old/plugin new=plugin --runs 5 -j 6

# 3. Blind one task
python3 examples/eval/blind.py /tmp/out multi-turn-zh

# 4. Give a judge (another model session) rubric.md and /tmp/out/<task>/blind/ only.
#    It writes /tmp/out/<task>/blind/scores.csv: label + one column per dimension (0-3 or NA).

# 5. Unblind
python3 examples/eval/score.py /tmp/out multi-turn-zh
```

Every run has `CLAUDE.md` files off and the installed plugin disabled, so the only difference between arms is the plugin directory. Model and effort default to `claude-sonnet-5-5` and `medium`.

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

## Caveats

- The judge is a model and the rubric is written from the style's own rules, so it favours whichever version states those rules more directly. Read the quotes, not just the totals.
- 5 runs per arm are samples, not measurements.
