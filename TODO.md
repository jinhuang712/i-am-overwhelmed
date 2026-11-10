# To do

Open work, kept here so it does not live in one session only. Take a line out when it is done. What a finished item taught us goes to [`eval/FINDINGS.md`](eval/FINDINGS.md).

The order of work, agreed on 2026-11-11: first make the rubric something we can rely on, then go back to the rules.

## The rubric, `eval/rubric-yesno.md`

Sent to the strong judge, not yet run

- [ ] Three lines stayed weak in every round on Haiku, and each names a fault that matters. They are marked 🔎 now. See how steady Opus is on them:
  - "states a guess or an inference as a fact": 15 of 20, twice.
  - "answers a plain fact and still closes with a question": 14 of 20, twice. This is the line behind the ending tree.
  - "makes the same point twice": 13, then 12 of 20. The owner wants the wording kept as it is.

Not yet tested

- [ ] Wrong hits and misses. No line has been checked for being right, only for being stable. Make replies with one fault planted in each, and their clean twins. Start with the red flags and the Listening deck: about 45 lines never fired on the replies we have.
  - The agent began to write these replies by hand on 2026-11-11 and that step was stopped, so none exist. Decide how to get them: written by the owner, or produced by a model run under a budget.
- [ ] The 10 lines marked 🔎 have never been answered by the strong judge. Check how stable Opus is on them.
- [ ] Three lines a judge may lack the facts for: "hedges on a thing it knows", "takes the first explanation and tests no other", "states a guess or an inference as a fact".
- [ ] One real run of `--rubric yesno` from end to end. The cheapest way: judge again the 12 replies of `results/2026-11-10-f97c872-vs-4f7adc2-opus-5-5`, about $1.50 to $2.50 by estimate.
- [ ] More replies with no plugin. Only 17 are on disk, all on Opus.

Later

- [ ] The four parked lines: find a wording that holds, or a stronger judge.
- [ ] "three or more" in the line on chains of cause and effect is a number the agent picked.
- [ ] Make `yesno` the default rubric once the lines are checked.

## The rules, for when the rubric is ready

Faults the rubric check showed, on 20 replies

- [ ] Three or more things in one sentence: 14 of 20, with and without the plugin. The owner read the rule "never chain parallel clauses; split them into bullets" and its wording is right. It is not followed. Look again after an eval.
- [ ] File and folder names as links: the rule now says "each time you name it". With the plugin, replies linked the first mention only. See after an eval whether the later mentions are linked.
- [ ] Replies cut too short to follow. No rule is changed for now: the replies that were too short came from a session on the old rules, so nothing points at one line. Three rubric lines watch for it ("a verdict with no reason", "a coined term not explained again", "a number and a short label"). Change a rule only when an eval shows them rising under the new rules.

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

## Release and upkeep

- [ ] Nothing since 0.1.14 is pushed or released. The owner said to wait.
- [ ] The README examples were recorded with 0.1.14.
- [ ] `[Unreleased]` in `CHANGELOG.md` is long. Sort it before a release.
