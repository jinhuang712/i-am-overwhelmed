# To do

Open work, kept here so it does not live in one session only. Take a line out when it is done. What a finished item taught us goes to [`eval/FINDINGS.md`](eval/FINDINGS.md).

The order of work, agreed on 2026-11-11: first make the rubric something we can rely on, then go back to the rules.

## Handoff, 2026-11-12

Written for the session that takes this work over. Read this part first, then [`eval/FINDINGS.md`](eval/FINDINGS.md).

Where things stand

- 0.1.15 is released, pushed and tagged `v0.1.15` on 2026-11-12. CI passed, and the owner's profile runs it. `CHANGELOG.md` has one sentence a change.
- Since then, on `master` and not pushed: the README benchmark, "What you get", examples from the benchmark, eval tool work, and ten rule changes. They are listed under "The next step".
- The rule file has 88 rules. On 2026-11-12 the owner set its boundary: it rules the talk, such as when to ask and when to stop, and leaves how the work is done to the host.
- The `CHANGELOG.md` is written at a release, from the commits. `[Unreleased]` holds entries up to 2026-11-12; sort them at the next release.
- The README benchmark is no plugin against the rules of 13a35d4: `results/2026-11-11-none-vs-13a35d4-opus-5-5`, 19 tasks, 3 runs each, overall 77.2 against 82.1. 0.1.14 is no longer compared.
- `eval/rubric-yesno.md` is a draft: 119 lines in eleven decks (93 bad signs, 18 good signs, 8 red flags), 43 parked. It judges the reply only, and what the reader gets, not the plugin's own formats. A red flag names a harm.
- `eval.py --reuse <results folder>` takes finished runs from an earlier eval; the benchmark folder covers 114 of the 171 runs of a full run with no plugin.
- `rubric_check.py` now judges the 20 replies of its last round, so a round costs only the decks that changed. `--strong` checks the 🔎 lines on Opus.
- 56 unit tests pass: `python3 -m unittest discover eval/tests`.

Paid runs, held for the next release (see "Eval" in `CLAUDE.md`: one eval per release, on a settled rubric)

- First settle the rubric, about $1.45 of new money. Each tool counts its ledger against `--budget`, so the numbers are totals:
  - A22 and K15 on the rubric check: 60 Haiku calls, about $0.15 on top of $2.81 spent.
    ```
    python3 eval/rubric_check.py --decks 6,8 --budget 3.50
    ```
  - The red flag check on its 8 cases: 264 Haiku and 16 Opus calls, about $1.30 on top of $1.33.
    ```
    python3 eval/flag_check.py --budget 3.50
    ```
- Then one benchmark of the release's rules against no plugin, with the 57 runs with no plugin reused: $11.38 for the 57 new runs, and about $5 for judging.
  ```
  python3 eval/eval.py --new HEAD --none --model claude-opus-5-5 --rubric yesno --runs 3 --reuse eval/results/2026-11-11-none-vs-13a35d4-opus-5-5 --budget 20
  ```
- Dropped on 2026-11-12: judging the benchmark of 13a35d4 again. No decision rested on it.

How the owner works, where the files do not say it

- The owner names the budget. Propose a number and wait. Do not pick one.
- Run the evals on the owner's second Claude Code profile. See "Another account" in `eval/README.md`.
- Change one thing at a time, and show the change as git prints it.
- Improve a rule that exists before you add one. Rules carry no examples.
- A rubric line is one plain sentence that names one thing a judge can see.
- Never drop a rubric line for how often it fires. Read what it hit. Park a line; do not delete it.
- When a judgment is the owner's to make, such as whether a thing is a fault, ask. Do not decide it from a count.
- Reply in the owner's language. The owner often reads on a phone: send a file when asked to show one.
- One thing and one question a reply. Long replies with several parts and several questions read as a mess to the owner ("有点乱"); the owner asks for a summary when they do.
- Compare against no plugin. The owner stopped comparing with 0.1.14 on 2026-11-11.
- A rule whose fault does not show is not dead weight. The owner keeps it as a backstop: "never use double negatives" and "never soften" stayed on 2026-11-12, though neither side of the benchmark broke them. Do not propose to drop a rule for that reason alone.
- The owner counts reruns as waste: $188 of evals by 2026-11-12, at least $66 of it on runs and judging done again. Propose the smallest step, and name the decision a paid run can change.
- The README may leave a weak point out. It may not claim what our own numbers contradict. The owner turned down a list of where the plugin does worse ("我们不必如此对自己苛刻"); those numbers go to `eval/FINDINGS.md`.
- Two short rules are better than one long rule. Remove a line that repeats; do not merge lines.
- Keep the owner's wording of a rule. Cut around it.

The next step

- No paid run now, and no hurry for the release. The owner wants the free work first, then a push.
- Ten rule changes wait for the release eval, all since `v0.1.15`:
  - Added: "reply in the language of my message".
  - Reworded: "call a thing decided only when I verbally agreed on it"; "never hide what you skipped, loosened or retried to make something pass", which was "never cheat"; a bare number of any kind needs its title, not only a question number; a decision of the user's gets a recommended answer, which was "at least one option".
  - Cut: "check each one" after "doubt every premise"; "ask as many questions as you need"; "never overuse emoji"; "go deep on one thing only; keep several things brief"; the `[MAYBE]` tag.
- Before the release benchmark, settle the eight rubric lines listed under "Not yet tested". Then the paid runs above, in their order.

## The rubric, `eval/rubric-yesno.md`

Sent to the strong judge, not yet run

- [ ] How steady Opus is on the 🔎 lines. In the baseline each got one pass. `python3 eval/rubric_check.py --strong`: 60 Opus calls, about $3. Three of them stayed weak in every round on Haiku, and each names a fault that matters:
  - "states a guess or an inference as a fact": 15 of 20, twice.
  - "answers a plain fact and still closes with a question": 14 of 20, twice. This is the line behind the ending tree.
  - "makes the same point twice": 13, then 12 of 20. The owner wants the wording kept as it is.

Not yet tested

- [ ] `eval/results/rubric-check/report.md` is of the 127-line rubric. Run the check once on the whole current rubric and commit that report: `python3 eval/rubric_check.py`, 210 Haiku calls with the rest cached, about $0.40.
- [ ] The overall score is new (2026-11-11): its weights, its point types and the red flag cut were set with the owner in one evening. Look at it again after a few runs. The judge seldom answers NA, so "a line that does not apply counts for nothing" does little yet.
- [ ] The body of a reply still presented the agent's advice as decided: the line "your own advice stays open" reached ☑️ only, and `long-discussion-zh` kept 2 of 3 hits in the sixth turn. Since 2026-11-12 the line reads "Call a thing decided only when I verbally agreed on it." See in the release eval whether the body keeps to it. See `eval/FINDINGS.md`.
- [ ] K15 fired on work the user handed over and saw done, listed as decided (`session-zh`). It now says "presents its own advice as decided, though the user never took it", and `eval/flag-cases/` has a case that should not fire and one that should. Run `eval/flag_check.py`.
- [ ] "Puts a question in the middle of the reply" is parked: 16 of its 25 hits with the plugin were the plugin's own ways. A22, "buries a question where the reader can miss it", replaces it. Run the rubric check on the Asking deck.
- [ ] Wrong hits and misses. The red flags have a first check: `eval/flag_check.py`, with 8 real replies the owner judged, in `eval/flag-cases/`. Add a case each time the owner judges a hit. H4, H5, H17, O2 and O3 have no case that should fire yet. The other lines have none at all; about 45 never fired on the replies we have.
- [ ] Three lines a judge may lack the facts for: "hedges on a thing it knows", "takes the first explanation and tests no other", "states a guess or an inference as a fact".
- [ ] Eight lines fired on what the rules ask for, or wider than their rule, or on what the owner does not count as a fault. Read on 2026-11-12 from the judges' notes of the benchmark; settle them with the rubric, before the release benchmark:
  - "asks a thing it could decide itself" fired on the question about batches and on the question at a conflict, which the rules ask for: 4 of its 8 hits.
  - "answers a plain fact and still closes with a question" fired where a question of the first turn was still open, since the user's turns are fixed: all 8 hits.
  - "has an option that changes two things at once" fired on options that pack a plan, such as commit and open a pull request.
  - "says that a premise fails, but not first" fired mostly on a limit named after the lead, such as "no CI here".
  - "puts a long chunk in a code block" counted drawings of 22 to 45 lines.
  - "uses so many emoji that they stop standing out" fired on 📍 ☑️ ❓ 💬 ✅. The owner does not count them as a fault: they show what each part is for.
  - "lists three or more things inside one sentence" fires on any three nouns in a row, in 65% of replies on both sides. The rule is about parallel clauses.
  - "goes into depth on several things at once" fires on an answer with its reasons, in 68% of replies with the plugin and 77% without. It cannot show whether "go deep on one thing only" is followed.
- [ ] The rubric check's 20 replies were drawn when 17 replies with no plugin were on disk. 150 are now, all on Opus. `--new-samples` draws again, and the next round then shares no cache and no comparison with the last.

Later

- [ ] The four parked lines: find a wording that holds, or a stronger judge.
- [ ] "three or more" in the line on chains of cause and effect is a number the agent picked.
- [ ] Make `yesno` the default rubric once the lines are checked.
- [ ] A red flag for a reply in a language other than the user's message. The owner named it on 2026-11-12; the rubric has no line for it yet.

## The rules, for when the rubric is ready

Faults the rubric check showed, on 20 replies

- [ ] Three or more things in one sentence: 14 of 20, with and without the plugin. The owner read the rule "never chain parallel clauses; split them into bullets" and its wording is right. It is not followed. Look again after an eval.
- [ ] File and folder names as links: the rule now says "each time you name it". With the plugin, replies linked the first mention only. See after an eval whether the later mentions are linked.
- [ ] Replies cut too short to follow. No rule is changed for now: the replies that were too short came from a session on the old rules, so nothing points at one line. Three rubric lines watch for it ("a verdict with no reason", "a coined term not explained again", "a number and a short label"). Change a rule only when an eval shows them rising under the new rules.

From the owner, 2026-11-12

- [ ] The rule "reply in the language of my message" is in since 2026-11-12. See in the release eval whether the replies after tool work keep to it: 3 of 122 turns broke it before the rule. See `eval/FINDINGS.md`.

Conflicts the agent reported in real sessions

The rules ask the agent to stop and name any instructions that conflict, these rules included. Each report is a lead: write it here, then fix the scope of the rules it names.

- [ ] None yet.

Carried over from the evals of 2026-11-10

- [ ] "Anything you did not check is a guess" held in part: the next run still stated two inferences as facts. No change for now; one run is the evidence, and the rule is plain.
- [ ] "Never put a command inside a sentence" worked on one task and not on another. No change for now; the wording is not the cause.
- [ ] A ✅ on a question that can be read as a fact or as a decision. No change; the owner read the tree and kept it.
- [ ] The rule file grew from 961 words in 0.1.13 to 1,775. A pass on 2026-11-12 read every rule against the benchmark's lines and took 91 rules to 88, 1,743 words. Most candidates turned out to be the rubric's problem, not the rule's. See `eval/FINDINGS.md`.
- [ ] In the release eval, look at what the cuts of 2026-11-12 did: "asks a thing it could decide itself" (8 of 57 before), a yes or no question with no view of the agent's, an item or a step named by its number alone, and how many emoji a reply carries without "never overuse emoji".
- [ ] Rules against other instructions. Checked on 2026-11-11 against the owner's global CLAUDE.md, this project's, Claude Code's own, and the skills loaded in that session. Two real conflicts, both about the form of a reply: line numbers (the rule says the plugin wins) and a skill that asks with a built-in question tool (not settled). Other skills and other projects were not read.

Open questions

- [ ] How much does the plugin help beyond its own formats? On the old rubric it was 65% against 88%. On the draft rubric, on replies that were not matched by task, the two groups were level.
- [ ] The owner has not yet worked for some days with the rules of 2026-11-10. Scan the real sessions again against the baseline of that morning: trees 7%, replies that end with a question 87%, "simpler" asked 15 times in 4 days.
- [ ] Sonnet and Codex: every eval since 2026-11-10 ran on Opus.

## The eval tool

- [ ] The two trap tasks ran once, on Haiku, in a smoke run, and both stopped at the conflict. They have not run on the model we measure, and have not been judged.
- [ ] A task with a `CLAUDE.md` that collides with the plugin. The tool turns `CLAUDE.md` off today.
- [ ] The account email still reaches every session, and a run's saved session keeps it; a judge's no longer is saved. A run with an API key under `--bare` might avoid it; not tried.
- [ ] `eval/rubric.md`, the old scale, still judges what the agent did (R1, R6, section A). The owner set the scope to the reply on 2026-11-11.

- [ ] A free command for tuning: for a results folder, the lines with the widest gap between the two sides, and the judges' notes on each hit. It was done by hand three times on 2026-11-12 and gave every rule change of that day. The owner put it off.

## Release and upkeep

- [ ] `master` is ahead of `origin` with the work since 0.1.15. The owner pushes when the open free work is done.
- [ ] Four rules override what the host does: no line numbers, file names as links, spaces at a bare URL, no built-in question tools. The owner counts each as a clear gain; one reason is that AskUserQuestion is slow. `PHILOSOPHY.md` gives no reason for them. Asked twice on 2026-11-12, not answered.
- [ ] The benchmark's tasks: 17 of 19 are in Chinese, every run is on Opus, and the Codex rules never ran. Weigh this with the release benchmark.
