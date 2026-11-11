# Eval: compare versions of the style

A repeatable A/B, kept as a tool: run the same tasks against two versions of the plugin, blind the replies, have a model judge score them with [`rubric.md`](rubric.md), then unblind.

What the evals have taught us is in [`FINDINGS.md`](FINDINGS.md).

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

`--none` adds an arm with no plugin. With `--none` and no `--old`, the eval compares the new version with no plugin alone.

Runs that already exist can be reused: copy their folders, such as `raw/<task>/none-1/`, into the results folder before the run. A run with its `done.json` is kept, and a higher `--runs` adds new ones next to it.

Results go to `eval/results/<date>-<old>-vs-<new>-<model>/`: `report.md`, `ledger.jsonl`, and scores and mappings per task. `raw/` holds the runs and is git-ignored.

## Two rubrics

`--rubric` picks how the replies are judged.

| | `scale`, the default | `yesno` |
|---|---|---|
| File | [`rubric.md`](rubric.md) | [`rubric-yesno.md`](rubric-yesno.md), a draft |
| A line | a quality, scored 0 to 3 | one thing a judge can see, answered yes or no |
| Judge | one strong judge, one pass | a cheap judge, three passes on each deck, the majority counts. The lines marked 🔎 go to the strong judge |
| Stable over three passes | 54% to 58% on Opus | 92% on Haiku, with N and NA as one answer |
| The report gives | the share of points | "clean": the share of bad signs a reply does not show; the credits; the faults by deck |

```
python3 eval/eval.py --old v0.1.14 --rubric yesno --budget 10
```

- **The reply only**: every line judges the reply. What the agent did counts only through what the reply says about it, such as a change it hides. A red flag names a harm; an act in it is an example. The lines that judged acts are parked.
- **What the reader gets, not our format**: a line asks what a format of the plugin is for, such as whether the options of a question are clear, not whether they carry A/B/C letters. Otherwise a reply with no plugin loses points for conventions it was never told about. Lines the plugin has no rule for yet, such as a claim the tool results contradict, check that the rubric does not only praise our own rules.
- **Decks**: the rubric is cut by type into decks of at most 14 lines, so the lines in one call explain each other.
- **Three kinds of line**: most go to the cheap judge. A line marked 🔎 goes to the strong judge, once. Where it raises a red flag, it answers twice more, and the red flag counts only by majority: one red flag fails a reply. A line marked ⚙️ is answered by a script in `checks.py`, which is exact and free.
- **A line keeps its number for good**, so a result or a finding can point at it.
- **The judge's notes are kept** next to its answers, in the cache of the task's `blind/` folder.
- **The bar**: no red flag in the new arm, and "clean" at most 2 points under the old arm. Two points is what one pass of the judge moves a reply by.
- **Read a deck, not a line**: one line's answer moves between runs. A deck's count and the whole score are steady.
- **Check the rubric itself** with `python3 eval/rubric_check.py --dry-run`. It judges replies that are already on disk, several times, and reports for every line how stable it is and how often it fires.
- **Check the red flags** with `python3 eval/flag_check.py --dry-run`. One red flag fails a reply, so each red flag is checked against real replies whose answer the owner gave: ones that do the harm, and ones that only look like it. The cases live in `eval/flag-cases/`, which git ignores.
- `yesno` will become the default when its lines have been checked for wrong hits and misses.

## Reading a report

The rubric has three layers: red flags, items, and a release bar. For each task the report prints, per arm:

- the share of points, with the red flags and the optional items left out
- the red flags that were hit, such as `R3 x1`
- `bar: passed` or `bar: failed`, with the reason. The bar is in [`rubric.md`](rubric.md): no red flag in the new arm, and a share of points at most 3 points under the old arm's

A report from before 2026-11-10 has no red flag columns, so it shows `red flags: none` for every arm.

## Try the tool first

```
python3 eval/eval.py --smoke --budget 2
```

`--smoke` runs every task once, the new arm only, on the cheap model, and judges nothing. It says which runs did not come through. Run it before a full run: on 2026-11-10 a wrong path, a task that ran away and a plugin that did not load cost $17.79, and none of the three had to do with how good the model was.

## Another account

The tools start `claude` with the environment they were started in. To run on another Claude Code profile, set its config folder for the command:

```
CLAUDE_CONFIG_DIR=<the profile's folder> python3 eval/eval.py --smoke --budget 2
```

The runs then use that profile's login and its usage limit. The eval adds its own flags for tools and permissions, so a profile's alias flags are not needed.

## Budget

Every task in [`tasks.json`](tasks.json) has a `budget`: the most one run of it may cost. A one-turn chat run gets $0.10 to $0.20 and the four-turn agent run gets $1.80, so a cheap task cannot starve a costly one. Judging keeps $0.30 for each task. `--dry-run` adds the limits up:

```
task limits: $27.75 for the runs + $5.10 for judging = $32.85 at most
```

`--budget` is still the limit for the whole eval. Each limit is about 2.5 times the highest cost measured, and 1.3 times for the costly `session-zh`, on Opus 5.5 in the full run of 2026-11-10. That run, with three arms and one run each, cost about $11 for the runs and $2.50 for judging when nothing went wrong. Set the limits again when the model changes.


- **The limit covers everything**: runs and judging. $0.30 a task is kept back for judging, and never more than half the limit.
- **Every call has a cap**: each `claude -p` gets `--max-budget-usd`, and it holds that cap before it starts.
- **A stop stays usable**: whole rounds run first, so the arms stay balanced. Finished runs still get judged, and the report says the eval is incomplete.
- **A resume keeps judging money only for open tasks**: a task with all its runs done and judged needs none. Before, a resume kept $0.30 back for every task again, and a costly run could not get its hold.
- **A run can be followed**: every finished run prints a line and adds it to `raw/progress.log` in the results folder. `tail -f` shows it live.
- **Resume is the same command**: finished runs are kept. Their cost stays in `ledger.jsonl`, so the limit applies across both sessions.
- **A resume follows a change**: the scores keep a fingerprint of `rubric-yesno.md`, so after the rubric changes a resume judges again; the answers to decks that did not change come from the cache. A run done again under its old name gets new blind samples: `runs.json` keeps a hash of each run's turns. On 2026-11-11 both had to be done by hand.
- **More money is a higher `--budget`**: new runs join the old ones, and the task is judged again.
- **One reply is capped at 16,000 output tokens**: `--max-budget-usd` is checked between turns only. On 2026-11-10 a chat task that wanted tools wrote 128,000 tokens of made-up tool calls in one reply, $2.56 a run against a $0.15 limit. A task that makes the model want to look at files must be an `agent` task with a fixture.
- **On a subscription the costs are list prices, and the runs use up the usage limit**: the full run of 2026-11-10 used up a 5-hour limit, and every judge call failed with "You've hit your 5-hour limit". A run that hits the limit now counts as failed, and the same command resumes it after the reset.
- **A plugin that did not load fails the run**: Claude Code skips a `--plugin-dir` it cannot find and says nothing. On 2026-11-10 a relative `--out` made every plugin path relative, each run started in its own folder, and a full run of 48 runs went through with no plugin in any arm. The path is absolute now, and a run checks the session's plugin list.
- **A plugin from outside the eval fails the run**: on 2026-11-11 the runs carried the runner's own setup, with its plugins, skills and their hooks. One hook's note reached 66 of 114 runs. Sessions now start with no setting source (`--setting-sources ""`), no MCP server (`--strict-mcp-config`), hooks off, and no plugin from the terminal's `CLAUDE_CODE_PLUGIN_DIRS`. An agent run works in a git repository of its own. A chat run starts in an empty folder outside any repository: in an empty repository, Opus wrote made-up tool calls in 5 of 6 runs of one task. A run whose session lists a plugin other than its arm's and Claude Code's own fails.
- **Unknown spend counts in full**: a call that reports no cost counts as its whole cap.
- **Estimates improve with use**: `--dry-run` reads past ledgers. Until a model has history it uses a rough default and says so.
- **The limit is as exact as `--max-budget-usd`**: a call can overrun its cap. On 2026-11-07 the worst overrun was about 50%, so keep a margin.
- **A judge that hits its cap returns nothing**: on 2026-11-07 three tasks lost their scores this way at $0.33 per judge call. What is left now goes to the unjudged tasks by the size of their samples, so a resume with a higher `--budget` judges them again.

## Files

| File | What it is |
|---|---|
| [`eval.py`](eval.py) | The one command |
| [`budget.py`](budget.py) | The limit, the ledger and the estimate |
| [`run.py`](run.py) | One run of a task |
| [`blind.py`](blind.py) | Blind samples and the label mapping |
| [`judge.py`](judge.py) | The model judge |
| [`score.py`](score.py) | Unblinds and summarises the scores |
| [`checks.py`](checks.py) | Mechanical checks: line references, negations, paragraph-only replies, 📍 anchors, drawings, tables, quotes, headings, replies that end asking, and lines. Free |
| [`tasks.json`](tasks.json) | The tasks. A task with several `turns` continues one session |
| [`rubric.md`](rubric.md) | The dimensions |
| [`fixtures/`](fixtures/) | `many-bugs/`, `free-text-due/`, and their answer keys, kept outside them |
| [`tests/`](tests/) | Tests with a stub `claude`, so they cost nothing: `python3 -m unittest discover eval/tests` |

Every run has `CLAUDE.md` files, user settings and hooks off, and the installed plugin disabled, so the only difference between arms is the plugin directory. The judges start the same way. Agent tasks run in auto mode, so the permission classifier reviews their calls.

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

## Results, 2026-11-10: principles against definitions

Baseline 0.1.13 (`8811684`), Sonnet 5.5, 3 runs per arm. Four rounds, each against the same baseline. Lines are the mean per run, from the mechanical checks.

| Round | New arm | `chat-en` lines | `chat-zh` lines | `shape-zh` lines |
|---|---|---|---|---|
| baseline | 0.1.13 | 7 to 8 | 8 to 12 | 43 to 47 |
| 1 | `9d3a3c2`: modes replaced by principles, headings and drawings required | 40.7 | 31.7 | 50.0 |
| 2 | `0ca536a`: adds "write as simply as you can" | 31.7 | 34.7 | 43.3 |
| 3 | `5fab671`: adds "simplify first, then give structure" | 27.0 | 28.0 | 34.0 |
| 4 | `30abbeb`: Simple by default, Detailed on request | 9.7 | 12.0 | 28.3 |

Results are in [`results/`](results/), one folder per round. Round 1 also ran `multi-turn-zh`, `many-items-zh` and `design-flaw-zh`.

- **A principle lost to an unconditional rule**: "as simple as you can" and "simplify first" cut short answers by a third at most, while "give each part a heading" and "draw whenever it has a shape" were followed every time. The 2026-11-03 finding held again: the definition of Simple does the work.
- **Drawings came with the rule**: chat replies went from no drawings to one per reply in rounds 1 to 3. In round 4 they stay where the content has a shape (`shape-zh`, `chat-zh`) and the short English answer has none.
- **The judge's totals favour the new arm in rounds 1 to 3**, because the rubric gained items for drawings and headings in the same change. The line counts are the independent signal.
- **Asking**: every reply still ends with a question in both arms. Rounds 1 to 3 showed no clear effect from the asking principles; round 4 scores D17 (one decision) and D18 (needed question) at or above the baseline.
- **Blind reading by the owner**: 3 prompts, a reply with no plugin against the round-4 rules, Opus 5.5. The round-4 reply was picked 3 times of 3, for being shorter and for asking before assuming. That comparison is hard to blind, since the plugin's replies are easy to recognise.
- **Cost**: $6.60 for the four rounds.

## Results, 2026-11-10: no plugin, 0.1.14 and the current rules

Opus 5.5 at medium effort as the subject and as the judge. 17 tasks, three arms, one run each. The current rules are `9c811ba`. Folder: [`results/2026-11-10-full-none-vs-f97c872-vs-9c811ba-opus-5-5/`](results/2026-11-10-full-none-vs-f97c872-vs-9c811ba-opus-5-5/).

| Arm | Share of points | Red flags hit |
|---|---|---|
| No plugin | 65.0% | 3 |
| 0.1.14 | 87.5% | 0 |
| Current rules | 89.7% | 0 |

- **The plugin is the large effect.** No plugin sits 22 points under both versions, and it alone hit red flags: twice it built on a fact only the user knew, and once it acted without asking.
- **The changes since 0.1.14 are a small effect.** Two points on one run per arm is inside the noise. Four items moved the same way on most tasks: the point comes first (2.6 to 2.9), things are said straight (2.6 to 2.9), a vague request is defined first (2.0 to 2.7, three tasks), and emoji carry the emotion (2.5 to 2.9).
- **Two rules did not move the replies**: backquotes for short names only (2.1 in both), and humor (0.6 of 3 as a required item, which is why it is optional again).
- **14 of 17 tasks cleared the release bar.** The three that failed:
  - `shape-en`, 88.5 to 76.2: the task asked four things in one message, and the reply answered the main one and asked whether to go on. The fault was in the task. Both drawing tasks ask one thing now.
  - `session-zh`, 95.0 to 90.4: the reply said a second case was "fixed too" after it had checked only the first. This led to the rule "anything you did not check is a guess".
  - `long-discussion-zh`, 93.3 to 89.5: a ✅ on a question the judge read as a fact and the reply read as a decision. One of seven questions, and the rule stays.
- **The first attempt at this run was not valid.** A relative `--out` left every arm with no plugin, a chat task ran to the output limit three times, and the account's 5-hour usage limit stopped every judge call. $17.79 at list prices was lost. The guards under "Budget" come from it.
- **Cost**: $10.66 for the valid runs and the judging.

An earlier run the same day compared 0.1.14 with `016bd62` on four tasks, two runs per arm, for $1.53: [`results/2026-11-10-f97c872-vs-016bd62-opus-5-5/`](results/2026-11-10-f97c872-vs-016bd62-opus-5-5/). On `fact-zh` the old rules closed a plain answer with a made-up question both times, and the new rules ended the reply both times.

## Caveats

- The judge is a model and the rubric is written from the style's own rules, so it favours whichever version states those rules more directly. Read the quotes, not just the totals.
- 5 runs per arm are samples, not measurements.
- `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1` turns off `CLAUDE.md` files, but Claude Code still adds account context such as your email to every session. No switch was found for it: `CLAUDE_CODE_USER_EMAIL` does not replace it (2026-11-11). Replies have named the runner's company although no prompt mentioned it. It affects all arms equally.
