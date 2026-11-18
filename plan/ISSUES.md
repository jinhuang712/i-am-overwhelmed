# Issues

---

## Summary

```
Issues
├── eval
│   ├── I1: Check the reworded rubric lines
│   ├── I2: Run the red flag check on its 8 cases
│   ├── I3: Check how steady the strong judge is
│   ├── I4: Settle the ten rubric lines that waver
│   ├── I5: Narrow the six rubric lines that fire on what the rules ask
│   ├── I6: Bring the rubric in line with the recap
│   ├── I7: Write a red flag for a reply in another language
│   ├── I8: Make the bar of the table of lines a share of the replies
│   ├── I9: Run the benchmark of the rules in use
│   ├── I10: Read the benchmark against the rule changes no eval has seen
│   ├── I12: Scan the owner's real sessions against the baseline
│   └── I13: Bring the rubric in line with the rebuilt rule file
└── rules
    └── I11: Find out why drift is not said on Sonnet
```

---

## I1: Check the reworded rubric lines

- type: eval
- why: Four lines were reworded and no judge has seen the new wording.
  - A22 "buries a question where the reader can miss it" replaces a parked line: 16 of that line's 25 hits with the plugin were the plugin's own ways.
  - K15 now says "presents its own advice as decided, though the user never took it". It had fired on work the user handed over and saw done.
  - C13 and T22 were reworded on 2026-11-15, when every reply and every part got a heading.
- found: the rubric check of 2026-11-13 and the rewording of 2026-11-15
- how: `python3 eval/rubric_check.py --decks 6,8 --budget 3.50` for A22 and K15. `python3 eval/rubric_check.py --decks 2,3 --budget 3.50` for C13 and T22.
- cost: 60 Haiku calls a command. The first is about $0.15 on top of $2.81 spent. The second is a guess at the same price, with 30 calls cached.
- next: the owner names a budget

---

## I2: Run the red flag check on its 8 cases

- type: eval
- why: One red flag fails a reply, so each is checked against real replies the owner judged. K15 has a new case that should fire and one that should not.
- found: 2026-11-12
- how: `python3 eval/flag_check.py --budget 3.50`
- cost: 264 Haiku and 16 Opus calls, about $1.30 on top of $1.33 spent
- next: the owner names a budget

---

## I3: Check how steady the strong judge is

- type: eval
- why: The 🔎 lines got one pass each in the baseline. Three of them stayed weak in every round on Haiku, and each names a fault that matters.
  - "states a guess or an inference as a fact": stable on 15 of 20 replies, twice.
  - "answers a plain fact and still closes with a question": 14 of 20, twice. This is the line behind the ending tree.
  - "makes the same point twice": 13 and then 12 of 20. The owner wants the wording kept as it is.
- found: the rubric check of 2026-11-13
- how: `python3 eval/rubric_check.py --strong`
- cost: 60 Opus calls, about $3
- next: the owner names a budget

---

## I4: Settle the ten rubric lines that waver

- type: eval
- why: Ten lines were stable on under 16 of 20 replies in the round of 2026-11-13. One round does not settle a line.
  - A3 at 12 and Y8 at 11 are the weakest.
  - T4, T13, T15, L3, L6 and Y6 stand at 15. T15 and L3 were reworded that day and are still weak.
  - C11 and A6 are strong lines, which Haiku does not judge in an eval.
- found: the rubric check of 2026-11-13, two rounds on Haiku for $0.70
- cost: a rewording is free to draft, and its check costs about $1.45
- next: look at the lines again after the round of [I1](#i1-check-the-reworded-rubric-lines)

Of the lines that were new on 2026-11-13, C13 is stable on 19 of 20 after one rewording, T26 on 18, O7 on 16 and O6 on 20. K20 fired on 16 of 20 and is parked.

---

## I5: Narrow the six rubric lines that fire on what the rules ask

- type: eval
- why: A line that fires on a reply that did what the rules ask takes points from the rules it should check.
  - "asks a thing it could decide itself": 4 of its 8 hits were the question about batches or the question at a conflict. The rules still ask for the second.
  - "answers a plain fact and still closes with a question": all 8 hits were on a question of the first turn that was still open, since the user's turns are fixed.
  - "has an option that changes two things at once": it fired on options that pack a plan, such as commit and open a pull request.
  - H8 fired on `conflict-zh`. W5 and A13 fired on `only-you-know-zh`.
- found: the judges' notes of the benchmark, read on 2026-11-12, and the comparison of 2026-11-13
- next: read the notes of the last three, then narrow the lines or the tasks

---

## I6: Bring the rubric in line with the recap

- type: eval
- why: The rubric still judges the block that left the rules on 2026-11-18.
  - K16 asks for the goal, what the user decided and what is open, and is to be parked.
  - The legend of the emoji still names 📍 ☑️ ❓.
  - No line judges the recap.
- found: the rule change of 2026-11-18
- touches: [3. A condition sits where it applies](../DESIGNS.md#3-a-condition-sits-where-it-applies)
- next: `rubric_check.py` must run after the change, so the owner names a budget

---

## I7: Write a red flag for a reply in another language

- type: eval
- why: The rule "reply in the language of my message" is in since 2026-11-12, and the rubric has no line for it. Before the rule, 3 of 122 turns broke it.
- found: the owner named it on 2026-11-12

---

## I8: Make the bar of the table of lines a share of the replies

- type: eval
- why: In the report's part "Old against new" the table lists a line whose count differs by 3 replies or more. With many replies it listed 34 of 117 lines, which is too long to read.
- found: the first report with that part, read on 2026-11-13

---

## I9: Run the benchmark of the rules in use

- type: eval
- why: No eval has seen the rules of 0.1.16, 0.1.17 and 0.1.18, nor the recap. One run measures them together: the rules of `HEAD` against no plugin.
- found: each release since 2026-11-12 went out with no eval, by the owner's choice
- how: `python3 eval/eval.py --new HEAD --none --model claude-opus-5-5 --rubric yesno --runs 3 --reuse eval/results/2026-11-11-none-vs-13a35d4-opus-5-5 --budget 20`
- cost: $11.38 for the 57 new runs and about $5 for judging. The 57 runs with no plugin are reused.
- next: the rubric is settled first, then the owner names a budget

The run goes on the owner's second Claude Code profile. It must include `vague-zh` and the two trap tasks, which so far ran once on Haiku in a smoke run.

---

## I10: Read the benchmark against the rule changes no eval has seen

- type: eval
- why: Each change below went out on the owner's reading alone. The report of [I9](#i9-run-the-benchmark-of-the-rules-in-use) is read against this list.
- found: 2026-11-12 to 2026-11-18

24 things to read:

- **Reply in the language of my message**: see whether the replies after tool work keep to it.
- **Decided only when I verbally agreed**: the body of a reply still presented advice as decided, and `long-discussion-zh` kept 2 of 3 hits in the sixth turn.
- **Never hide what you skipped, loosened or retried**: the line was "never cheat".
- **A bare number needs its title**: see how often an item or a step is named by its number alone.
- **A decision of the user's gets a recommended answer**: see how often a yes or no question has no view of the agent's.
- **"Check each one" is cut**: it followed "doubt every premise".
- **"Ask as many questions as you need" is cut**: "asks a thing it could decide itself" fired on 8 of 57 replies before.
- **"Never overuse emoji" is cut**: count the emoji a reply carries.
- **"Go deep on one thing only" is cut**: "one thing at a time" stays.
- **No `[WHEN]`**: `diff` blocks stood at 3.0 of 3 under "You changed code or text", and the line now ends "each time you changed code or text".
- **The tree "define, discuss, do" is gone**: read D26 and O4 on `vague-zh`, and watch for work that starts on a vague request.
- **The template**: watch for block names printed as labels and for more blockquotes since `<note>` has a name.
- **`<brief>`**: see whether a weaker model puts it in every reply.
- **`<background>`**: see whether it restates the question or is said when there is nothing to say.
- **No length**: read the lines of `chat-en` and `chat-zh`, and the three lines that watch for a reply cut too short.
- **Headings on every reply and part**: read C13 and T22.
- **The recap**: watch for a ledger of what was done, for a recap on a quick question and for a recap that says what `<background>` says.
- **Three or more things in one sentence**: 14 of 20 replies did it with and without the plugin, and the owner holds the rule's wording to be right.
- **File names as links**: replies linked the first mention only, and the rule now says "each time you name it".
- **Heading, claim and evidence**: see whether a claim comes with the quote or the output it rests on.
- **An emoji on every heading**: see whether it tells the kind of part or only decorates.
- **The recap took in four lines**: see whether a reply still says what changed since the last one.
- **A branch for a talk**: see whether a reply in a talk ends with no options, and whether a report still ends on its step.
- **The register**: see whether "a rigorous technical document" brings stock phrases, and whether apology and praise leave the words.

`<background>` needs a talk of several turns to show where it is due. The owner wants it for a complex matter or for a thing from many replies ago.

---

## I11: Find out why drift is not said on Sonnet

- type: rules
- why: 20 of 20 replies of `long-discussion-zh` and `session-zh` followed a change of topic in silence on 2026-11-13. On Opus the old `[WHEN]` line scored 2.2 of 3. The model and the wording both changed, so the run cannot say which one did it.
- found: the comparison of 2026-11-13 on Sonnet 5.5
- touches: [3. A condition sits where it applies](../DESIGNS.md#3-a-condition-sits-where-it-applies)
- next: before the next release

---

## I12: Scan the owner's real sessions against the baseline

- type: eval
- why: The owner has not yet worked for some days with one set of rules, and real sessions are the only signal that needs no judge.
- found: 2026-11-12
- next: some days of work under one set of rules. A session started before a change keeps the old rules.

---

## I13: Bring the rubric in line with the rebuilt rule file

- type: eval
- why: The rule file was rebuilt on 2026-11-18, and the rubric judges the file as it was.
  - Two lines judge rules that left: one on what changed since the last reply and one on what the reader needs from an earlier reply.
  - The line on parallel clauses covers one sentence, and the rule now covers several.
  - No line judges the evidence under a claim, the emoji on a heading, a question that stands on its own, deference in words or a talk.
- found: the rule change of 2026-11-18
- touches: [3. A condition sits where it applies](../DESIGNS.md#3-a-condition-sits-where-it-applies)
- next: `rubric_check.py` must run after the change, so the owner names a budget
