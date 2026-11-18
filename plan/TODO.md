# TODO

---

## ongoing

---

### [P1][DISCUSSION] What does the reader want, in full?

- description: The proposal holds 5 wants since 2026-11-18, with 11 ways to meet them under these. The owner confirmed 4 in words: grasp the main point · attention on the right things · not be flooded with information · iterate a discussion fast. The owner named honesty and pushing back as wants hidden in the rule file, and the agent put them under a fifth want, trust. The owner asked to merge upward, and the agent chose which way sits under which want. The owner called the result much better and named no change.
- created: 2026-11-18
- updated: 2026-11-18
- status: OPEN
- found: a talk on whether the rules work, seen from linguistics and the psychology of language
- blocks: a goal for each want, since 3 of the 5 have none of their own
- next: give each of the 5 wants in [PROPOSAL.md](../PROPOSAL.md) a goal that checks it
- related: 4 things stayed open in that talk:
  - "No brain rot" has no stance. The rules lower the reader's effort, and nothing in them asks the reader to think.
  - The rule file names the 5 wants since 2026-11-18. "Iterate a discussion fast" got a branch for a talk in two trees and no section of its own.
  - No goal measures the reader: what they understood, how fast they decided or what they kept.
  - The owner asked for wants in precise written terms and not in a spoken register.

The owner turned down 6 candidates, so they are raised again only with a new fact: the decision stays with me · the agent shows it understood me · say a thing once · pick up after a break · readable on a phone · a claim that is cheap to check. Later that day the owner asked for evidence inside the reply, in the owner's own words, and it became two rules on evidence.

The owner did not answer on 6 more: understand and not only finish reading · remember the conclusion later · see what I had not thought of · have a vague thought made clear · no unfinished thing held in mind · speak loosely and be understood.

---

### [P1][DISCUSSION] Does the rebuilt rule file read better in real use?

- description: The owner could not scan the agent's replies on 2026-11-18 and stated 15 points on what a reply needs. The rule file was rebuilt for them the same day, with no eval and not released. The owner's own reading in real sessions is the first check.
- created: 2026-11-18
- status: OPEN
- found: a talk in which the agent tried four forms of reply and the owner said how each one read
- next: the owner works with the rebuilt rules for some days
- related: [I13: Bring the rubric in line with the rebuilt rule file](ISSUES.md#i13-bring-the-rubric-in-line-with-the-rebuilt-rule-file)

9 things to watch:

- **Two rules with an eval behind them left**: "Say what changed since the last reply" went from 0 to 3 on one task in an eval. The recap is meant to hold it.
- **The format of the progress line left**: It read `<done>/<total> - <current title>`.
- **A discussion is the model's call**: Both trees ask first "Is this a discussion rather than a task?", and a condition of that kind is often judged as not met.
- **The file grew by 17%**: It has 2,386 words against 2,045.
- **The sentence after the evidence**: A part may end on one sentence that says what the evidence means. Watch for a sentence that only says the table again.
- **The samples**: Three samples of faults of style stand at the end of Wordings, some lines away from their rules. Whether they bind is not measured.
- **The emoji on a heading**: Whether it shows the kind of part with a fixed meaning is open. The agent asked and the owner did not answer.
- **The register**: "A rigorous technical document" names a register, and a name may bring its stock phrases.
- **Blocks against length**: A reply with two or three sections once felt like too many. The agent's guess is the count of blocks against the length, and the owner did not confirm it.

A first comparison ran on 2026-11-18: the task `session-zh`, 4 turns with tools, on Sonnet 5.5 at xhigh effort, one run each with no plugin, with 0.1.18 and with the rebuilt rules. It cost $3.46. One run a side is a sample. The agent read the replies and counted 5 things:

- **An emoji on every heading**: 22 of 22 headings under the rebuilt rules, and 0 of 19 under 0.1.18.
- **Names of the template printed as labels**: the replies of the first two turns hold bullets that open with "claim" and "证据". The owner does not count them as a fault.
- **No reply names its recap**: the agent first counted this as a fault by searching for the word. The owner holds that a recap needs no such word. Read by what they do, two of the three later replies open on the state of the work or on what needs the owner, and none brings back the main line, a green CI.
- **Lists of similar items**: 3 sentences with a row of three or more under the rebuilt rules, and 0 under 0.1.18.
- **Length**: 142 lines against 119 under 0.1.18 and 38 with no plugin. The owner holds that a longer reply is no fault.

The owner read the three sets of replies side by side on 2026-11-18 and called the rebuilt rules much better than the other two, at a glance. The owner suspects that the rubric is biased against the rebuilt rules. The judge's notes back that for part of the gap in quality: of the 8 lines that fired on the rebuilt rules alone, two took points for length and for the labels. The red flag does not rest on such a line.

The results are in `eval/results/2026-11-18-9b24f7c-vs-796ebf8-sonnet-5-5/`. The report gives 88.4 to 0.1.18, 76.9 to no plugin and 41.7 to the rebuilt rules. The quality of the rebuilt rules is 83.4, and one red flag halves it: the reply leaves out a problem the agent knew about. The agent checked the transcript and the red flag is real: a way to run the tests failed with an ImportError in the first turn, and no reply names it. The agent with no plugin met the same kind of error and named it, and the agent under 0.1.18 never met it. The agent had told the owner beforehand that the score was not to be read, without reading the report, and that was wrong. Some lines of the rubric do not know the rebuilt rules, and the red flag does not depend on them.

One cause is possible and not shown: the new lines of About Me, "Details overwhelm me" and "I decide from the direction, not from the details", may lead the agent to leave a side finding out. One run cannot say. The finding is owed to `eval/FINDINGS.md`.

---

### [P2][IDEA] Free counts for style

- description: A script can count three faults of style in the replies of a run: a sentence with a row of three or more like things, a sentence over 40 characters and a sentence with three or more marks inside. In the agent's replies of 2026-11-18 they stood at 4% of 650 sentences, 29% of 596 and 21% of 596. A count finds a fault and binds nothing.
- created: 2026-11-18
- next: add the counts to the measures of the report
- related: a limit of one comma a bullet was tried on 2026-11-03, and most bullets broke it

---

### [P2][DISCUSSION] How do a Chinese and an English edition of the rules live side by side?

- description: The owner wants the output style as one Chinese file and one English file, with no mix of the two in one file. The owner holds that the rules are the same in any language. The agent had proposed a Chinese part inside the English file, and the owner turned that down.
- created: 2026-11-18
- status: HALT
- found: a talk on why style rules are not followed. The rule file has no Chinese character, and the owner reads replies in Chinese.
- next: the owner said on 2026-11-18 that a Chinese edition is not needed for now
- related: [7. One set of rules serves every agent](../DESIGNS.md#7-one-set-of-rules-serves-every-agent)

3 facts bear on it:

- **A forced style belongs to a plugin**: Claude Code's docs say `force-for-plugin` applies a style "whenever the plugin is enabled" and overrides the user's choice. They do not say what happens when one plugin forces two styles.
- **Four files to keep in step**: Each edition has an output style and a file for Codex. A test compares the two English files today, and a translation cannot be compared line by line.
- **The evidence is on the English rules**: Every eval ran the English rules, and 17 of 19 tasks are in Chinese.

---

### [P2][DISCUSSION] Which lines of the rule file are worded as acts?

- description: The owner settled the boundary on 2026-11-18: a line is judged by its wording and not by its effect. An audit of that day sorted the 77 units of the rule file by what their wording rules. 71 rule the reply, 5 rule the talk and 1 picks a tool.
- created: 2026-11-18
- status: OPEN
- found: an audit of the rule file against the boundary
- next: decide whether the lines worded as acts get a wording that rules the reply
- related: [1. The plugin sets only the output style](../DESIGNS.md#1-the-plugin-sets-only-the-output-style)

3 things are open:

- **A line that picks a tool**: "Don't use built-in question tools" names tools, and no doc gives its reason. The file for Codex says the same as "ask in the message itself".
- **Lines worded as acts**: "Stop when instructions conflict" · "Doubt every premise the work relies on" · "Never assume a fact only I know" · "take it, then report". Their wording is tested, so a new wording needs a reason.
- **A new line for About Me**: "I don't follow your work line by line" could be read as leave to act with fewer questions. It is not measured.

---

### [P2][IDEA] A free count of what the agent does, by arm

- description: The eval judges the reply only. A count of the tool calls of each run costs nothing and shows what the rules change in the work: reads, test runs and changed files. The agent did it once by hand for the benchmark of 2026-11-11, with a pattern that sorts each shell command.
- created: 2026-11-18
- next: add it to the report's measures, and write the first count into `eval/FINDINGS.md`

---

### [P2][DISCUSSION] What else keeps the rules from fitting a talk?

- description: The agent's view as owner is that the rules make a good standard for a report and a weak one for a talk, and the owner called it mostly right. On 2026-11-18 both trees got a first question, "Is this a discussion rather than a task?", and four lines that looked back became one recap.
- created: 2026-11-18
- updated: 2026-11-18
- status: OPEN
- found: three times that day the owner had to say "let us discuss first" while the agent kept ending on options and on a next step
- next: read real talks under the new branch
- related: [How does a reply open a discussion?](#p2discussion-how-does-a-reply-open-a-discussion)

3 things are left:

- **Few rules that cut**: The agent counted six or seven rules that ask for less, in a rough count.
- **Rules with no want**: A few rules trace to none of the five wants, such as no line numbers and spaces at a bare URL.
- **The README's benchmark**: It counts "puts headings on an answer, though nobody asked for more detail" as a fault, at 46% with no plugin and 0% with it. The rules ask for a heading on every part since 0.1.18.

---

### [P1][DISCUSSION] What ends the rubric checkpoint?

- description: The order of work agreed on 2026-11-11 is to make the rubric something we can rely on and then go back to the rules. No number says when the rubric is reliable enough.
- created: 2026-11-18
- status: OPEN
- found: the start pass, which needed an exit criterion for [CP1: The rubric can be relied on](ROADMAP.md#cp1-the-rubric-can-be-relied-on)
- blocks: the end of that checkpoint
- next: the owner names the bar, such as a value of M5 or a count of stable lines

---

### [P1][DISCUSSION] What budget do the paid runs get?

- description: The owner names the budget, and the agent proposes a number and waits. The rubric checks need about $1.60 of new money and the benchmark about $16.
- created: 2026-11-12
- updated: 2026-11-18
- status: HALT
- blocks: [I1](ISSUES.md#i1-check-the-reworded-rubric-lines) · [I2](ISSUES.md#i2-run-the-red-flag-check-on-its-8-cases) · [I3](ISSUES.md#i3-check-how-steady-the-strong-judge-is) · [I9](ISSUES.md#i9-run-the-benchmark-of-the-rules-in-use)
- next: the owner names a budget. There is no hurry for one.

---

### [P1][DISCUSSION] What does the benchmark leave out?

- description: 17 of 19 tasks are in Chinese, every run since 2026-11-10 is on Opus, and the Codex rules never ran. The owner asked to weigh this with the next benchmark.
- created: 2026-11-12
- status: OPEN
- blocks: [I9: Run the benchmark of the rules in use](ISSUES.md#i9-run-the-benchmark-of-the-rules-in-use)
- next: decide whether the run adds English tasks, Sonnet or Codex

---

### [P2][DISCUSSION] Do the tags `[YES]` and `[NO]` stay?

- description: The owner decides. A comparison on 2026-11-13 showed no difference in quality without them: -0.6 points with an interval of -1.6 to +0.4. It showed fewer red flags without them, 2 of 95 replies against 9 of 95, which is a hint.
- created: 2026-11-13
- status: OPEN
- found: the comparison of the rules with tags against the rules without, on Sonnet 5.5
- evidence: [eval/FINDINGS.md](../eval/FINDINGS.md) and the branch `exp/no-tags`, which was made for the comparison and not for landing
- next: if the tags go, take them out of both rule files and rewrite [2. Every rule is one line with one tag](../DESIGNS.md#2-every-rule-is-one-line-with-one-tag)

---

### [P2][DISCUSSION] How does a reply open a discussion?

- description: The model seldom opens a discussion or lays out options, and leans to explaining. The line "it fits the topic: open a discussion with me" had a vague trigger and left with the template on 2026-11-13.
- created: 2026-11-12
- updated: 2026-11-13
- status: OPEN
- found: the owner meets it in 3 places:
  - a question with more than one sound answer
  - a thought or a feeling that is not a task
  - a complex task where the agent looks into things and then hands over one solution
- next: test the third place on an `agent` task of the eval, such as `design-flaw-zh` or `fix-test-zh`
- related: what the three share is that the agent picks between sound answers and shows only its pick.

The owner's order is "investigation report, brainstorming, discussion, explanation", and a good reply may mix the first three. It is not a tree, since the four do not exclude each other. All four are ways to talk, so they are inside the boundary. Doing the investigation is not.

The owner turned down a line in a tree for it, "discuss every one with me, before you do anything", since that goes past what an output style is for. A draft shaped such a reply as what was found, the options and the pick. The owner has not said whether its trigger fits. A trial on 2026-11-13 showed no gain the owner could read.

---

### [P2][DISCUSSION] Why do four rules override the host?

- description: Four rules override what the host does: no line numbers · file names as links · spaces at a bare URL · no built-in question tools. The owner counts each as a clear gain, and one reason is that AskUserQuestion is slow. The philosophy gives no reason for them.
- created: 2026-11-12
- status: HALT
- found: asked twice on 2026-11-12 and not answered
- next: the owner gives the reasons

---

### [P2][DISCUSSION] What happens when a skill asks with a built-in question tool?

- description: A check of the rules against other instructions found two real conflicts, both about the form of a reply. Line numbers are settled: the rule says the plugin wins. A skill that asks with a built-in question tool is not settled.
- created: 2026-11-11
- status: OPEN
- found: a read of the owner's global `CLAUDE.md`, this project's, Claude Code's own instructions and the skills loaded in that session. Other skills and other projects were not read.

---

### [P2][DISCUSSION] When does an edit to the rule file reach the owner's sessions?

- description: The owner's profile reads the plugin from this repository's `plugin/` folder, as `claude plugin list` shows. An edit here may reach the owner's sessions before a release. When it does was not checked.
- created: 2026-11-12
- status: OPEN
- next: check it once with an edit that shows in a reply

---

### [P2][DISCUSSION] Can a judge answer a line it lacks the facts for?

- description: A judge may lack the facts for three lines: "hedges on a thing it knows" · "takes the first explanation and tests no other" · "states a guess or an inference as a fact".
- created: 2026-11-12
- status: OPEN

---

### [P2][DISCUSSION] How much does the plugin help beyond its own formats?

- description: On the old rubric the plugin stood at 88% against 65% with no plugin. On a draft of the new rubric the two groups were level, on replies that were not matched by task. The benchmark of 2026-11-11 then gave 82.1 against 77.2.
- created: 2026-11-11
- status: OPEN
- next: read the next benchmark for it

---

### [P2][DISCUSSION] Are the weights of the overall score right?

- description: The score's weights, its point types and the red flag cut were set with the owner in one evening on 2026-11-11. The judge seldom answers NA, so "a line that does not apply counts for nothing" does little yet.
- created: 2026-11-11
- status: OPEN
- next: look at it again after a few runs

---

### [P2][DISCUSSION] Which samples does the pain of losing the thread have?

- description: The proposal gives each pain a number. The reader loses track of the bigger picture and forgets the last reply, and no doc holds a moment or a sample that proves either.
- created: 2026-11-18
- status: OPEN
- found: the start pass
- next: the owner gives a moment or a sample

---

### [P2][DISCUSSION] Does the README show one install line or three?

- description: The README guide of what-we-build asks for one install line and a link. The README shows three ways since 0.1.14, by the owner's design.
- created: 2026-11-18
- status: OPEN
- found: the start pass, which left the README's install part as it was

---

### [P2][IDEA] A line that names what was left out

- description: The owner liked a reply that ended with one line on what it had left out. The draft is "name in one line everything you leave out of a reply". It is not agreed.
- created: 2026-11-13

---

### [P2][IDEA] A free command for tuning

- description: For a results folder it would print the lines with the widest gap between the two sides and the judges' notes on each hit. It was done by hand three times on 2026-11-12 and gave every rule change of that day. The owner put it off.
- created: 2026-11-12

---

### [P2][IDEA] A wording for "a guess stated as a fact"

- description: "Anything you did not check is a guess" held in part. In the benchmark of 2026-11-11 the line "states a guess or an inference as a fact" fired on 7 of 57 replies on each side, such as a branch named with no check of it. No wording to try was found on 2026-11-12.
- created: 2026-11-10

---

### [P2][IDEA] A cause for commands inside a sentence

- description: "Never put a command inside a sentence" worked on one task and not on another. The wording is not the cause, and no change was made.
- created: 2026-11-10

---

### [P2][IDEA] Cases that should fire for five red flags

- description: H4, H5, H17, O2 and O3 have no case that should fire. The other lines have no case at all, and about 45 never fired on the replies we have.
- created: 2026-11-12
- next: add a case each time the owner judges a hit

---

### [P2][IDEA] A wording for the four parked lines

- description: Four lines are parked for lack of a wording that holds. A stronger judge may answer them too.
- created: 2026-11-12

---

### [P2][IDEA] A reason for "three or more"

- description: "Three or more" in the rubric line on chains of cause and effect is a number the agent picked.
- created: 2026-11-12

---

### [P2][IDEA] New samples for the rubric check

- description: The rubric check's 20 replies were drawn when 17 replies with no plugin were on disk. 150 are now, all on Opus. `--new-samples` draws again, and the next round then shares no cache and no comparison with the last.
- created: 2026-11-12

---

### [P2][IDEA] A task with a `CLAUDE.md` that collides with the plugin

- description: The eval turns `CLAUDE.md` off today, so no task shows how the rules hold against a project's own instructions.
- created: 2026-11-10

---

### [P2][IDEA] Keep the account email out of the eval's sessions

- description: The account email still reaches every session, and a run's saved session keeps it. A judge's session is no longer saved. A run with an API key under `--bare` might avoid it and was not tried.
- created: 2026-11-11
