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
  - "Iterate a discussion fast" is a want with no section of the rule file written for it.
  - No goal measures the reader: what they understood, how fast they decided or what they kept.
  - The owner asked for wants in precise written terms and not in a spoken register.

The owner turned down 6 candidates, so they are raised again only with a new fact: the decision stays with me · the agent shows it understood me · say a thing once · pick up after a break · readable on a phone · a claim that is cheap to check. Later that day the owner asked for evidence inside the reply, in the owner's own words, and that point stands under "What lets the reader scan a reply?".

The owner did not answer on 6 more: understand and not only finish reading · remember the conclusion later · see what I had not thought of · have a vague thought made clear · no unfinished thing held in mind · speak loosely and be understood.

---

### [P1][DISCUSSION] What lets the reader scan a reply?

- description: The owner could not scan the agent's replies on 2026-11-18 and had to read each one to the end. In the talk that followed the owner stated what a reply needs. No rule was changed.
- created: 2026-11-18
- status: OPEN
- found: a talk in which the agent tried four forms of reply and the owner said how each one read
- next: the owner called the talk done on 2026-11-18 and asked how to land it. The agent drafted the rule lines, and the owner has to settle their wording.
- related: [PROPOSAL.md](../PROPOSAL.md) names the want as "Grasp the main point"

The owner stated 14 points:

- **Sections**: A reply must have sections, and each section must have a heading.
- **Emoji on a heading**: A heading needs a mark that helps to scan, such as an emoji. The rules ask for emoji to mark meaning and say nothing about headings.
- **Drawings and tables**: Diagrams, tables and other structured forms matter.
- **Blockquotes**: A blockquote for what is not the key information makes the rest stand out.
- **Structure carries the rest**: Honesty and pushing back are hard to see without structure, since reading prose is tiring.
- **No parallelism**: The owner dislikes all three kinds: parallel clauses in one sentence · the same frame over several sentences · a short antithesis.
- **Condense or structure**: A row of like things becomes one word that names their kind, or a list. The owner's example is "roast meats" in place of four dishes.
- **Direction before detail**: A reply states the direction in one sentence, such as "cut the number of test cases and remove the dead ones". A long account of each case has a low density of information.
- **Short sentences**: A long sentence is tiring in a terminal. It runs to the end of the line and wraps, with many marks of punctuation inside.
- **Evidence in the reply**: A decision maker needs the evidence, so the original text and the output belong in the reply as a blockquote or a code block. The diff is done well and is far from enough.
- **Density over length**: Length is no problem and the count of lines is no great problem. The largest problem is a low density of information.
- **A recap that grows with the task**: On a very long task one sentence is not enough. The recap then shows where the task stands, such as its progress, in a structured form.
- **No hard sentences**: A sentence with a clause nested inside it is as tiring as a long one.
- **A rigorous written register**: The agent's style is still close to speech and carries a tone of deference. The owner wants the written register of a rigorous large company. Weaker models show the fault more, and they correct it when told.

The four forms the agent tried:

| Form | The owner's reading |
|---|---|
| Four to five headed sections with a table and three options | "有点懵" |
| One heading and paragraphs | like an essay |
| One heading and bullets with bold keys | sections are needed |
| Emoji headings with a table, a drawing and a blockquote | much better, and easy to scan |

6 things are open:

- Whether the emoji on a heading shows the kind of section with a fixed meaning. The agent asked and the owner did not answer.
- Why a reply with two or three sections felt like too many. The agent's guess is the count of blocks against the length, and the owner did not confirm it.
- Whether "say the upper level" is a stance for the philosophy. The owner asked for it three times that day: the merged wants, the one word for a row of things, and the direction before the detail.
- How to ask for short sentences. A limit of one comma a bullet was tried on 2026-11-03: most bullets broke it and replies read as cramped. In this session 29% of the agent's 596 sentences ran over 40 characters, and 21% had three or more marks inside.
- How to ask for evidence. Of the rules on quotes, code blocks and diffs, only the diff rule says that a thing must be shown and names its moment: "each time you changed code or text". The others say how to set a thing that is shown.
- How to ask for the register and name no genre. Each time "press release" was in the instruction, the model brought the dateline and the PR voice with it.

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

The owner also weighed 3 lines for About Me. "Long lines and long sentences tire me" stands without the word "terminal". The owner turned down the lines on deciding with evidence and on density: they say what the agent should do, and About Me holds what the reader is, which lies outside the rules. The owner also sent "I'm the one who decides" to the tagged rules. The owner then chose two lines for About Me: "Long lines and long sentences tire me." and "I don't follow your work line by line." The owner asked for a third, on the lines of "Details overwhelm me": too much detail keeps the owner from deciding, and a direction is easier to decide on, since the owner knows their own goals, non-goals, thoughts and wants best. Its wording is open.

---

### [P1][DISCUSSION] Do the rules fit a talk as well as a report?

- description: The owner asked the agent how it sees the rules as their owner. The agent's view is that the rules make a good standard for a report and a weak one for a talk. The owner called the view mostly right.
- created: 2026-11-18
- status: OPEN
- found: three times that day the owner had to say "let us discuss first" while the agent kept ending on options and on a next step
- next: discuss it after the structure of a reply is settled
- related: [How does a reply open a discussion?](#p2discussion-how-does-a-reply-open-a-discussion)

The agent named 5 things, and none is agreed in detail:

- **No branch for a talk**: The tree that ends a reply has "the step is clear" and "it needs my answer". It has no way to stay in a talk.
- **Coverage by content only**: The tree on what one reply covers looks at how complex the content is, and not at whether the reader waits for a result or thinks a thing through.
- **Four ways to look back**: The recap, "say what changed", "say again what I need" and the background all look back.
- **Few rules that cut**: The agent counted six or seven rules that ask for less, in a rough count.
- **Rules with no want**: A few rules trace to none of the five wants, such as no line numbers and spaces at a bare URL.

The README's benchmark still counts "puts headings on an answer, though nobody asked for more detail" as a fault, at 46% with no plugin and 0% with it. The rules ask for a heading on every part since 0.1.18.

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
