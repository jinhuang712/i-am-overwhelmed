# TODO

---

## ongoing

---

### [P1][DISCUSSION] What does the reader want, in full?

- description: The proposal holds 5 wants since 2026-11-18, with 11 ways to meet them under these. The owner confirmed 4 in words: grasp the main point · attention on the right things · not be flooded with information · iterate a discussion fast. The owner named honesty and pushing back as wants hidden in the rule file, and the agent put them under a fifth want, trust. The owner asked to merge upward, and the agent chose which way sits under which want. The owner has not confirmed that.
- created: 2026-11-18
- updated: 2026-11-18
- status: OPEN
- found: a talk on whether the rules work, seen from linguistics and the psychology of language
- blocks: the goals that check each want
- next: the owner confirms or corrects the 5 wants in [PROPOSAL.md](../PROPOSAL.md)
- related: 4 things stayed open in that talk:
  - "No brain rot" has no stance. The rules lower the reader's effort, and nothing in them asks the reader to think.
  - "Iterate a discussion fast" is a want with no section of the rule file written for it.
  - No goal measures the reader: what they understood, how fast they decided or what they kept.
  - The owner asked for wants in precise written terms and not in a spoken register.

The owner turned down 6 candidates, so they are raised again only with a new fact: the decision stays with me · the agent shows it understood me · say a thing once · pick up after a break · readable on a phone · a claim that is cheap to check.

The owner did not answer on 6 more: understand and not only finish reading · remember the conclusion later · see what I had not thought of · have a vague thought made clear · no unfinished thing held in mind · speak loosely and be understood.

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
