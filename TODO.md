# To do

Open work, kept here so it does not live in one session only. Take a line out when it is done. What a finished item taught us goes to [`eval/FINDINGS.md`](eval/FINDINGS.md).

The order of work, agreed on 2026-11-11: first make the rubric something we can rely on, then go back to the rules.

## Handoff, 2026-11-11

Written for the session that takes this work over. Read this part first, then [`eval/FINDINGS.md`](eval/FINDINGS.md).

Where things stand

- 0.1.15 is released on `master` on 2026-11-12, and nothing since 0.1.14 is pushed. The owner said to wait with the push.
- The rules changed in about 25 places from 0.1.14 to 0.1.15. `CHANGELOG.md` has one sentence a change.
- `eval/rubric-yesno.md` is the new rubric, a draft: 119 lines in eleven decks (93 bad signs, 18 good signs, 8 red flags), 43 parked. It judges the reply only, and what the reader gets, not the plugin's own formats. A red flag names a harm.
- The report opens with one overall score per arm. See "Reading a report" in `eval/README.md`.
- The comparison the owner keeps is no plugin against the latest rules: `results/2026-11-11-none-vs-13a35d4-opus-5-5`, 3 runs each, overall 77.2 against 82.1. 0.1.14 is no longer compared.
- A smoke run of all 19 tasks came through on Haiku for $0.17.
- 49 unit tests pass: `python3 -m unittest discover eval/tests`.

Waiting for the owner's word

- The checks of the rubric changes of the night, about $2 together: `eval/rubric_check.py --decks 6,8` for A22 and K15, `eval/flag_check.py` on its 8 cases, then judge `results/2026-11-11-none-vs-13a35d4-opus-5-5` again from the cache.

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

The next step

- Ask the owner for the budget of the checks above.

## The rubric, `eval/rubric-yesno.md`

Sent to the strong judge, not yet run

- [ ] Three lines stayed weak in every round on Haiku, and each names a fault that matters. They are marked 🔎 now. See how steady Opus is on them:
  - "states a guess or an inference as a fact": 15 of 20, twice.
  - "answers a plain fact and still closes with a question": 14 of 20, twice. This is the line behind the ending tree.
  - "makes the same point twice": 13, then 12 of 20. The owner wants the wording kept as it is.

Not yet tested

- [ ] `eval/results/rubric-check/report.md` is of the 127-line rubric. Run the check once on the whole current rubric, about $1, and commit that report.
- [ ] The overall score is new (2026-11-11): its weights, its point types and the red flag cut were set with the owner in one evening. Look at it again after a few runs. The judge seldom answers NA, so "a line that does not apply counts for nothing" does little yet.
- [ ] The body of a reply still presents the agent's advice as decided. The line "your own advice stays open" reaches ☑️ only: `long-discussion-zh` kept 2 of 3 hits in the sixth turn, before and after it. See `eval/FINDINGS.md`.
- [ ] K15 fired on work the user handed over and saw done, listed as decided (`session-zh`). It now says "presents its own advice as decided, though the user never took it", and `eval/flag-cases/` has a case that should not fire and one that should. Run `eval/flag_check.py`.
- [ ] "Puts a question in the middle of the reply" is parked: 16 of its 25 hits with the plugin were the plugin's own ways. A22, "buries a question where the reader can miss it", replaces it. Run the rubric check on the Asking deck.
- [ ] Wrong hits and misses. The red flags have a first check: `eval/flag_check.py`, with 6 real replies the owner judged, in `eval/flag-cases/`. Add a case each time the owner judges a hit. H4, H5, H17, O2 and O3 have no case that should fire yet. The other lines have none at all; about 45 never fired on the replies we have.
- [ ] The lines marked 🔎 got one pass of Opus each in the baseline. Check how stable Opus is on them.
- [ ] Three lines a judge may lack the facts for: "hedges on a thing it knows", "takes the first explanation and tests no other", "states a guess or an inference as a fact".
- [ ] More replies with no plugin. Only 17 are on disk, all on Opus.

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

- [ ] Reply in the language of the user's message. In `fix-test-zh` the reply with no plugin came back in English in 3 of 3 runs, to a Chinese prompt; the plugin's replies were in Chinese. The owner counts a reply in another language as a red flag. Add the rule to the output style and `codex/AGENTS.md` together.

Conflicts the agent reported in real sessions

The rules ask the agent to stop and name any instructions that conflict, these rules included. Each report is a lead: write it here, then fix the scope of the rules it names.

- [ ] None yet.

Carried over from the evals of 2026-11-10

- [ ] "Anything you did not check is a guess" held in part: the next run still stated two inferences as facts. No change for now; one run is the evidence, and the rule is plain.
- [ ] "Never put a command inside a sentence" worked on one task and not on another. No change for now; the wording is not the cause.
- [ ] A ✅ on a question that can be read as a fact or as a decision. No change; the owner read the tree and kept it.
- [ ] The rule file grew from 961 words in 0.1.13 to over 1,400, with three trees. Look for lines to remove.
- [ ] Rules against other instructions. Checked on 2026-11-11 against the owner's global CLAUDE.md, this project's, Claude Code's own, and the skills loaded in that session. Two real conflicts, both about the form of a reply: line numbers (the rule says the plugin wins) and a skill that asks with a built-in question tool (not settled). Other skills and other projects were not read.

Open questions

- [ ] How much does the plugin help beyond its own formats? On the old rubric it was 65% against 88%. On the draft rubric, on replies that were not matched by task, the two groups were level.
- [ ] The owner has not yet worked for some days with the rules of 2026-11-10. Scan the real sessions again against the baseline of that morning: trees 7%, replies that end with a question 87%, "simpler" asked 15 times in 4 days.
- [ ] Sonnet and Codex: every eval since 2026-11-10 ran on Opus.

## The eval tool

- [ ] The two trap tasks ran once, on Haiku, in a smoke run, and both stopped at the conflict. They have not run on the model we measure, and have not been judged.
- [ ] On Haiku, 📍 opened every reply of the compound task as if it were a heading, though the big picture had not changed. See whether the stronger models do the same with the new 📍 block.
- [ ] The cap of 16,000 output tokens a reply has not been seen to stop a reply.
- [ ] A task with a `CLAUDE.md` that collides with the plugin. The tool turns `CLAUDE.md` off today.
- [ ] A watch on `raw/progress.log` that reports each quarter of a run to the owner.
- [ ] The account email still reaches every session, and a run's saved session keeps it; a judge's no longer is saved. A run with an API key under `--bare` might avoid it; not tried.
- [ ] `eval/rubric.md`, the old scale, still judges what the agent did (R1, R6, section A). The owner set the scope to the reply on 2026-11-11.
- [ ] Reuse is by hand: copy the run folders in, and a higher `--runs` adds new runs next to them. A flag that names the runs to reuse would save the copying.

## Release and upkeep

- [ ] Nothing since 0.1.14 is pushed, 0.1.15 included. The owner said to wait.
