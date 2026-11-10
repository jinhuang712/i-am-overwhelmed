# To do

Open work, kept here so it does not live in one session only. Take a line out when it is done. What a finished item taught us goes to [`eval/FINDINGS.md`](eval/FINDINGS.md).

The order of work, agreed on 2026-11-11: first make the rubric something we can rely on, then go back to the rules.

## The rubric, `eval/rubric-yesno.md`

Found by reading the replies four lines hit

- [ ] Two lines can be a script, free and exact: "a bullet point of two sentences or more" and "a file or a folder with no link". A script agreed with the judge on 17 of 20 replies for each.
- [ ] See whether the emoji lines hold now that the Formatting deck carries the legend.

Not yet tested

- [ ] Wrong hits and misses. No line has been checked for being right, only for being stable. Make replies with one fault planted in each, and their clean twins. Start with the red flags and the Listening deck: about 45 lines never fired on the replies we have.
- [ ] The 10 lines marked 🔎 have never been answered by the strong judge. Check how stable Opus is on them.
- [ ] Three lines a judge may lack the facts for: "hedges on a thing it knows", "takes the first explanation and tests no other", "states a guess or an inference as a fact".
- [ ] One real run of `--rubric yesno` from end to end. The cheapest way: judge again the 12 replies of `results/2026-11-10-f97c872-vs-4f7adc2-opus-5-5`, about $1.50 to $2.50 by estimate.
- [ ] More replies with no plugin. Only 17 are on disk, all on Opus.

Later

- [ ] The four parked lines: find a wording that holds, or a stronger judge.
- [ ] "three or more" in the line on chains of cause and effect is a number the agent picked.
- [ ] Keep the judge's notes in `rubric_check.py`, so the reason for an answer can be read.
- [ ] Make `yesno` the default rubric once the lines are checked.

## The rules, for when the rubric is ready

Faults the rubric check showed, on 20 replies

- [ ] Three or more things in one sentence: 14 of 20, with and without the plugin. The rule "never chain parallel clauses; split them into bullets" is not followed.
- [ ] File and folder names as links: nearly never followed.
- [ ] Replies cut too short to follow. The rules ask for few lines and few words, and no line says that saving words must not cost the meaning.

From the owner, 2026-11-11

- [ ] Say what you are about to do before a job of several steps. The rubric has the line; the rules do not. Today "the step is clear" is the agent's own call, so it starts, and a wrong reading shows only when the work is done. This is alignment between the user and the agent, not the model's skill. Telling is not asking: one line of plan, then the work, and the user can stop it.

Carried over from the evals of 2026-11-10

- [ ] "Anything you did not check is a guess" held in part: the next run still stated two inferences as facts.
- [ ] "Never put a command inside a sentence" worked on one task and not on another.
- [ ] A ✅ on a question that can be read as a fact or as a decision.
- [ ] "Arrow waterfall: cause and effect" is as wide as the rubric line was. A single cause needs no arrows.
- [ ] The rule file grew from 961 words in 0.1.13 to over 1,400, with three trees. Look for lines to remove.
- [ ] Rules against other instructions: the owner's "state the plan and get approval" against "a clear step is taken"; skills that ask with a built-in question tool. The new rule only asks the agent to name a conflict.

Open questions

- [ ] How much does the plugin help beyond its own formats? On the old rubric it was 65% against 88%. On the draft rubric, on replies that were not matched by task, the two groups were level.
- [ ] The owner has not yet worked for some days with the rules of 2026-11-10. Scan the real sessions again against the baseline of that morning: trees 7%, replies that end with a question 87%, "simpler" asked 15 times in 4 days.
- [ ] Sonnet and Codex: every eval since 2026-11-10 ran on Opus.

## The eval tool

- [ ] The two trap tasks, `conflict-zh` and `conflict-agent-zh`, and the `system` field have never run.
- [ ] The cap of 16,000 output tokens a reply has not been seen to stop a reply.
- [ ] A task with a `CLAUDE.md` that collides with the plugin. The tool turns `CLAUDE.md` off today.
- [ ] A smoke mode: every task once on a cheap model, no judging, to catch a broken path or a runaway task before a full run.
- [ ] A watch on `raw/progress.log` that reports each quarter of a run to the owner.

## Release and upkeep

- [ ] Nothing since 0.1.14 is pushed or released. The owner said to wait.
- [ ] The README examples were recorded with 0.1.14.
- [ ] `[Unreleased]` in `CHANGELOG.md` is long. Sort it before a release.
