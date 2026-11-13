# To do

Open work, kept here so it does not live in one session only. Take a line out when it is done. What a finished item taught us goes to [`eval/FINDINGS.md`](eval/FINDINGS.md).

The order of work, agreed on 2026-11-11: first make the rubric something we can rely on, then go back to the rules.

## Handoff, 2026-11-12

Written for the session that takes this work over. Read this part first, then [`eval/FINDINGS.md`](eval/FINDINGS.md).

Where things stand

- 0.1.16 is released, pushed and tagged `v0.1.16` on 2026-11-12. `CHANGELOG.md` has one sentence a change.
- The ten rule changes of 0.1.16 went out with no eval. The owner made this exception to "a release changes rules: run the eval on them first": the next benchmark was not urgent, and the owner wants to work with the new rules first.
- 0.1.16 also has the README benchmark, "What you get", examples from the benchmark, and eval tool work.
- The rule file has 88 rules. On 2026-11-12 the owner set its boundary: it rules the talk, such as when to ask and when to stop, and leaves how the work is done to the host.
- The `CHANGELOG.md` is written at a release, from the commits. It has no `[Unreleased]` part.
- The README benchmark is no plugin against the rules of 13a35d4: `results/2026-11-11-none-vs-13a35d4-opus-5-5`, 19 tasks, 3 runs each, overall 77.2 against 82.1. 0.1.14 is no longer compared.
- `eval/rubric-yesno.md` is the rubric, and the default of `eval.py`, since 2026-11-13: 118 lines in eleven decks (92 bad signs, 18 good signs, 8 red flags), 49 parked. The file says its formats, how to write a line, its families and its score. It judges the reply only, and what the reader gets, not the plugin's own formats. A red flag names a harm. `eval/rubric.md`, the 0 to 3 scale, is frozen.
- `eval.py --reuse <results folder>` takes finished runs from an earlier eval; the benchmark folder covers 114 of the 171 runs of a full run with no plugin.
- `rubric_check.py` now judges the 20 replies of its last round, so a round costs only the decks that changed. `--strong` checks the 🔎 lines on Opus.
- 59 unit tests pass: `python3 -m unittest discover eval/tests`.

Paid runs, held until the owner names a budget (see "Eval" in `CLAUDE.md`: one eval per release, on a settled rubric). They now measure 0.1.16

- First settle the rubric, about $1.45 of new money. Each tool counts its ledger against `--budget`, so the numbers are totals:
  - A22 and K15 on the rubric check: 60 Haiku calls, about $0.15 on top of $2.81 spent.
    ```
    python3 eval/rubric_check.py --decks 6,8 --budget 3.50
    ```
  - The red flag check on its 8 cases: 264 Haiku and 16 Opus calls, about $1.30 on top of $1.33.
    ```
    python3 eval/flag_check.py --budget 3.50
    ```
- Then one benchmark of the rules of 0.1.16 against no plugin, with the 57 runs with no plugin reused: $11.38 for the 57 new runs, and about $5 for judging.
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

- No paid run now, and no hurry for one. 0.1.16 is out and pushed; nothing waits to be pushed but this file's last edit.
- The next benchmark measures the ten rule changes of 0.1.16, which no eval has seen:
  - Added: "reply in the language of my message".
  - Reworded: "call a thing decided only when I verbally agreed on it"; "never hide what you skipped, loosened or retried to make something pass", which was "never cheat"; a bare number of any kind needs its title, not only a question number; a decision of the user's gets a recommended answer, which was "at least one option".
  - Cut: "check each one" after "doubt every premise"; "ask as many questions as you need"; "never overuse emoji"; "go deep on one thing only; keep several things brief"; the `[MAYBE]` tag.
- Before the next benchmark, settle the eight rubric lines listed under "Not yet tested". Then the paid runs above, in their order.

Left open at the end of 2026-11-12, each with its place below

- The owner's real sessions with 0.1.16. Free, and the only signal that needs no judge. See "Open questions".
- The eight rubric lines that measure badly. A rewording is free to draft; its check costs about $1.45. See "Not yet tested".
- The benchmark of 0.1.16, about $16, with what it leaves out: English tasks, Sonnet, Codex. See "Paid runs" and "Release and upkeep".
- The free command for tuning, which the owner put off. See "The eval tool".
- The reasons for the four rules that override the host. Asked twice, not answered. See "Release and upkeep".
- "It fits the topic: open a discussion with me" keeps its vague trigger. The owner wants a thing discussed in full first, and turned down a line in the tree for it ("discuss every one with me, before you do anything"): that goes past what an output style is for.
- A red flag for a reply in a language other than the user's. See "Later".
- Not to be done now, by the owner's word or the agent's advice: a list in the README of where the plugin does worse, a source on each line of "The work feels different", a credit line, a shorter README, a `CONTRIBUTING.md`.

## The rubric, `eval/rubric-yesno.md`

Sent to the strong judge, not yet run

- [ ] How steady Opus is on the 🔎 lines. In the baseline each got one pass. `python3 eval/rubric_check.py --strong`: 60 Opus calls, about $3. Three of them stayed weak in every round on Haiku, and each names a fault that matters:
  - "states a guess or an inference as a fact": 15 of 20, twice.
  - "answers a plain fact and still closes with a question": 14 of 20, twice. This is the line behind the ending tree.
  - "makes the same point twice": 13, then 12 of 20. The owner wants the wording kept as it is.

Not yet tested

- [ ] `eval/results/rubric-check/report.md` is of the 127-line rubric. Run the check once on the whole current rubric and commit that report: `python3 eval/rubric_check.py`, 210 Haiku calls with the rest cached, about $0.40.
- [ ] The overall score is new (2026-11-11): its weights, its point types and the red flag cut were set with the owner in one evening. Look at it again after a few runs. The judge seldom answers NA, so "a line that does not apply counts for nothing" does little yet.
- [ ] The body of a reply still presented the agent's advice as decided: the line "your own advice stays open" reached ☑️ only, and `long-discussion-zh` kept 2 of 3 hits in the sixth turn. Since 2026-11-12 the line reads "Call a thing decided only when I verbally agreed on it." See in the next benchmark whether the body keeps to it. See `eval/FINDINGS.md`.
- [ ] K15 fired on work the user handed over and saw done, listed as decided (`session-zh`). It now says "presents its own advice as decided, though the user never took it", and `eval/flag-cases/` has a case that should not fire and one that should. Run `eval/flag_check.py`.
- [ ] "Puts a question in the middle of the reply" is parked: 16 of its 25 hits with the plugin were the plugin's own ways. A22, "buries a question where the reader can miss it", replaces it. Run the rubric check on the Asking deck.
- [ ] Wrong hits and misses. The red flags have a first check: `eval/flag_check.py`, with 8 real replies the owner judged, in `eval/flag-cases/`. Add a case each time the owner judges a hit. H4, H5, H17, O2 and O3 have no case that should fire yet. The other lines have none at all; about 45 never fired on the replies we have.
- [ ] Three lines a judge may lack the facts for: "hedges on a thing it knows", "takes the first explanation and tests no other", "states a guess or an inference as a fact".
- [ ] Eight lines fired on what the rules ask for, or wider than their rule, or on what the owner does not count as a fault. Read on 2026-11-12 from the judges' notes of the benchmark. Five were settled on 2026-11-13: "puts a long chunk in a code block" now says "of code or output"; the emoji line and "goes into depth on several things at once" are parked; the line on three things in a sentence now names parallel clauses; the line on a premise now says "a wrong premise of the request". Three are left:
  - "asks a thing it could decide itself" fired on the question about batches and on the question at a conflict: 4 of its 8 hits. The rules no longer ask about batches since 2026-11-13; the question at a conflict is still asked for.
  - "answers a plain fact and still closes with a question" fired where a question of the first turn was still open, since the user's turns are fixed: all 8 hits.
  - "has an option that changes two things at once" fired on options that pack a plan, such as commit and open a pull request.
- [ ] The rubric check's 20 replies were drawn when 17 replies with no plugin were on disk. 150 are now, all on Opus. `--new-samples` draws again, and the next round then shares no cache and no comparison with the last.

Later

- [ ] The four parked lines: find a wording that holds, or a stronger judge.
- [ ] "three or more" in the line on chains of cause and effect is a number the agent picked.
- [ ] `yesno` is the default rubric since 2026-11-13. It became so before one check had covered every line: the committed report of the rubric check is still of the 127-line rubric.
- [ ] A red flag for a reply in a language other than the user's message. The owner named it on 2026-11-12; the rubric has no line for it yet.

## The rules, for when the rubric is ready

Faults the rubric check showed, on 20 replies

- [ ] Three or more things in one sentence: 14 of 20, with and without the plugin. The owner read the rule "never chain parallel clauses; split them into bullets" and its wording is right. It is not followed. Look again after an eval.
- [ ] File and folder names as links: the rule now says "each time you name it". With the plugin, replies linked the first mention only. See after an eval whether the later mentions are linked.
- [ ] Replies cut too short to follow. On 2026-11-13 the owner met it again in a session on 0.1.16 and changed the rules with no eval: "a few lines" is gone, and a tree decides what one reply covers. Three rubric lines still watch for it ("a verdict with no reason", "a coined term not explained again", "a number and a short label"). See in the next benchmark whether they fall.

From the owner, 2026-11-13. The rule changes of this day are on master and not released

- [ ] Length with no limit in the rules. A trial on 2026-11-13 showed chat replies about twice as long as under 0.1.16, and the owner read the longer one as much easier. So the length stays. In the next benchmark, see whether the same holds over all tasks and three runs: `chat-en` and `chat-zh` had 7 to 12 lines under "a few lines".
- [ ] The rubric was rewritten on 2026-11-13, on the owner's word that the agent may. What changed in the lines: T8, K9, K10, K21, M13 and C12 are parked; K20 judges a reply that goes into more than the main item; C13 (a simple question gets several sections), O7 (one answer to a choice that has others) and T26 (steps in a row drawn as a diagram) are new; T2, T15, L3 and O6 are reworded; T1 is answered by a script. The report has a new part, "Old against new". Read the first report that has it, and see whether the interval and the list of lines say what a reader of the replies would say.
- [ ] Headings in a Default reply. The owner said a Default reply may have headings, and that they help. The rules now ask for headings in Detailed only, and say nothing for Default. A draft, "a reply of more than one part: give each part a heading", was used for some replies and not agreed. In the trial of 2026-11-13 the model gave a Default reply headings with no rule that asks for them, and the owner liked that reply. A rule may not be needed.
- [ ] A line that names what was left out. The owner liked a reply that ended with one line on what it had left out. The draft is "name in one line everything you leave out of a reply". Not agreed.
- [ ] The rule file has no `[WHEN]` since 2026-11-13: 69 tagged rules, 57 `[YES]` and 12 `[NO]`, and 7 drawn rules under their own headings. The last seven were reworded with no eval. In the next benchmark, look at the items their old wording had earned: `diff` blocks stood at 3.0 of 3 under "You changed code or text", and the line now ends "each time you changed code or text". `CLAUDE.md` still writes its own rules with `[WHEN]`; the owner's decision was about the rule file.
- [ ] The tree "define, discuss, do" left the rule file on 2026-11-13, three days after it came in. Its one leaf that nothing else said is now `<definition>` in the template of a reply. No eval had scored it: D26 was NA in both reports that list it, since neither ran `vague-zh`. In the next benchmark, run `vague-zh` and read D26 and O4. What went with the tree is the order across a whole task; watch for work that starts on a vague request.
- [ ] The shape template, in since 2026-11-13 with no eval. Watch four things in real use and in the next benchmark: a reply that prints block names as labels (one case in 11); more blockquotes since `<note>` has a name (3 against 1 on one question); `<brief>` in every reply on a weaker model, as Haiku once did with 📍; and whether `<background>` restates the question. The owner asked to keep polishing the template: the next round takes these.
- [ ] `<background>` reads "what I need in mind to follow this reply, or nothing" since 2026-11-13, in the owner's words, and no reply was run under it. What the owner fears: a background that is said when there is nothing to say. What the owner wants it for: a complex matter, or a thing from many replies ago, said again so the reply can be followed. Two earlier wordings were run on four one-turn questions each. With "from earlier in this talk or about the topic", 1 of 4 replies gave one line of topic background. With "when this reply builds on more than the last one", none did, and the owner found that line hard to read. A list of what the block may hold (what happened before, what you should know, earlier terms, related topics) was left out, since each named thing invites the block. No run has shown the block where it is due: that needs a talk of several turns.
- [ ] "It fits the topic: open a discussion with me." The talk about it is not finished. Where the rule comes from: the model seldom opens a discussion or lays out options, and leans to explaining. The owner meets it in three places: a question with more than one sound answer, a thought or a feeling that is not a task, and a complex task where the agent looks into things and then hands over one solution. What the three share: the agent picks between sound answers and shows only its pick. The owner's order is "investigation report, brainstorming, discussion, explanation", and a good reply may mix the first three. It is not a tree: the four do not exclude each other. All four are ways to talk, so they are inside the boundary; doing the investigation is not. The draft, to be written with no `[WHEN]`: a reply that picks between sound answers, where the pick changes what the owner gets, is shaped as `<found>` what you checked and what it showed, `<options>` the sound answers side by side, `<pick>` the one you would choose and why. The owner has not yet said whether that trigger fits. The draft then grew into seven kinds of `<part>` inside the shape block. A trial on 2026-11-13 showed no gain the owner could read. Later that day the owner took the whole template for the sake of order, and the line "it fits the topic" went out with it; see `eval/FINDINGS.md`. What is left: the owner's third place, a complex task with tools, was not tested. An `agent` task of the eval, such as `design-flaw-zh` or `fix-test-zh`, could show it.

From the owner, 2026-11-12

- [ ] The rule "reply in the language of my message" is in since 2026-11-12. See in the next benchmark whether the replies after tool work keep to it: 3 of 122 turns broke it before the rule. See `eval/FINDINGS.md`.

Conflicts the agent reported in real sessions

The rules ask the agent to stop and name any instructions that conflict, these rules included. Each report is a lead: write it here, then fix the scope of the rules it names.

- [ ] None yet.

Carried over from the evals of 2026-11-10

- [ ] "Anything you did not check is a guess" held in part: the next run still stated two inferences as facts. No change for now; one run is the evidence, and the rule is plain. In the benchmark of 2026-11-11, "states a guess or an inference as a fact" fired on 7 of 57 replies on each side, such as a branch named with no check of it. No wording to try was found on 2026-11-12.
- [ ] "Never put a command inside a sentence" worked on one task and not on another. No change for now; the wording is not the cause.
- [ ] A ✅ on a question that can be read as a fact or as a decision. No change; the owner read the tree and kept it.
- [ ] The rule file grew from 961 words in 0.1.13 to 1,775. A pass on 2026-11-12 read every rule against the benchmark's lines and took 91 rules to 88, 1,743 words. Most candidates turned out to be the rubric's problem, not the rule's. See `eval/FINDINGS.md`.
- [ ] In the next benchmark, look at what the cuts of 2026-11-12 did: "asks a thing it could decide itself" (8 of 57 before), a yes or no question with no view of the agent's, an item or a step named by its number alone, and how many emoji a reply carries without "never overuse emoji".
- [ ] Rules against other instructions. Checked on 2026-11-11 against the owner's global CLAUDE.md, this project's, Claude Code's own, and the skills loaded in that session. Two real conflicts, both about the form of a reply: line numbers (the rule says the plugin wins) and a skill that asks with a built-in question tool (not settled). Other skills and other projects were not read.

Open questions

- [ ] How much does the plugin help beyond its own formats? On the old rubric it was 65% against 88%. On the draft rubric, on replies that were not matched by task, the two groups were level.
- [ ] The owner has not yet worked for some days with one set of rules. 0.1.16 runs in the owner's profile since the evening of 2026-11-12; a session started before that keeps the old rules. After some days, scan the real sessions against the baseline of the morning of 2026-11-10: trees 7%, replies that end with a question 87%, "simpler" asked 15 times in 4 days.
- [ ] Sonnet and Codex: every eval since 2026-11-10 ran on Opus.

## The eval tool

- [ ] The two trap tasks ran once, on Haiku, in a smoke run, and both stopped at the conflict. They have not run on the model we measure, and have not been judged.
- [ ] A task with a `CLAUDE.md` that collides with the plugin. The tool turns `CLAUDE.md` off today.
- [ ] The account email still reaches every session, and a run's saved session keeps it; a judge's no longer is saved. A run with an API key under `--bare` might avoid it; not tried.
- [ ] `eval/rubric.md`, the old scale, still judges what the agent did (R1, R6, section A). The owner set the scope to the reply on 2026-11-11.

- [ ] A free command for tuning: for a results folder, the lines with the widest gap between the two sides, and the judges' notes on each hit. It was done by hand three times on 2026-11-12 and gave every rule change of that day. The owner put it off.

## Release and upkeep

- [ ] The owner's profile reads the plugin from this repository's `plugin/` folder (`claude plugin list`). An edit to the rule file here may reach the owner's sessions before a release; when it does was not checked.
- [ ] Four rules override what the host does: no line numbers, file names as links, spaces at a bare URL, no built-in question tools. The owner counts each as a clear gain; one reason is that AskUserQuestion is slow. `PHILOSOPHY.md` gives no reason for them. Asked twice on 2026-11-12, not answered.
- [ ] The benchmark's tasks: 17 of 19 are in Chinese, every run is on Opus, and the Codex rules never ran. Weigh this with the next benchmark.
