# Eval 2026-11-13-7717813-vs-d6b682f-sonnet-5-5

- old: `7717813` (7717813)
- new: `d6b682f` (d6b682f)
- model: claude-sonnet-5-5, effort medium, judge claude-haiku-5-5 x3 on rubric-yesno.md, claude-opus-5-5 on its 🔎 lines, x3 where it raises a red flag
- runs: {'done': 2, 'kept': 188}
- spent: $38.43 of $42.00

## Overall

score = quality x (1 - 0.5 x the share of replies with a red flag). Quality weighs the words of PHILOSOPHY.md by rank; a line that does not apply counts for nothing.

| | old | new |
|---|---|---|
| **score** | 82.8 | 85.3 |
| quality | 86.9 | 86.2 |
| replies with a red flag | 9/95 | 2/95 |
| Honest (8) | 79.7 | 75.8 |
| Simple (7) | 91.9 | 92.9 |
| Structured (6) | 75.7 | 74.5 |
| Asking (5) | 92.5 | 91.9 |
| Opinionated (4) | 92.4 | 93.0 |
| Focused, Standalone (5) | 92.4 | 93.8 |
| Predictable (1) | 98.9 | 100.0 |

## Old against new

- gap in quality, new minus old: -0.6 points, 90% interval -1.6 to +0.4: no difference shown
- tasks: 6 up, 13 down, 0 equal, of 19
- down: fix-test-zh, design-flaw-zh, long-discussion-zh, shape-zh, fact-zh, clear-step-zh, detail-zh, only-you-know-zh, session-zh, better-way-zh, vague-zh, conflict-zh, conflict-agent-zh

Lines whose count differs by 3 replies or more. A count is the replies that said yes.

| # | kind | old, of 95 | new, of 95 | line |
|---|---|---|---|---|
| H11 | good sign | 87 | 76 | says what it did not check |
| C3 | bad sign | 36 | 25 | 🔎 makes the same point twice |
| L6 | bad sign | 9 | 17 | gives a thing a name, and later uses another name for it |
| A10 | bad sign | 6 | 14 | has an option that changes two things at once |
| A15 | bad sign | 15 | 7 | recommends an answer to a question about a fact |
| Y8 | good sign | 49 | 57 | names another explanation it weighed, and why it dropped it |
| A8 | bad sign | 21 | 14 | says "please confirm" or "I assume" outside a question |
| A22 | bad sign | 11 | 4 | buries a question where the reader can miss it, such as inside a paragraph |
| H13 | good sign | 8 | 2 | admits a mistake of its own in plain words |
| T13 | bad sign | 15 | 9 | shows a setting outside a code block |
| Y7 | good sign | 11 | 5 | shows the problem happening before it fixes it |
| C4 | bad sign | 14 | 9 | closes with a recap of what it already said |
| C11 | bad sign | 16 | 11 | 🔎 is much longer than the question needs |
| T26 | bad sign | 16 | 11 | draws steps that run in a straight line as a diagram or arrows, where a numbered list would do |
| H4 | red flag | 4 | 0 | 🔎 🚩 says it ran a check that it did not run |
| A3 | bad sign | 14 | 18 | ends with a question though it has just told the user what to do next |
| A9 | bad sign | 3 | 7 | asks two things in one question |
| W6 | bad sign | 21 | 25 | shows no part of the change itself |
| Y10 | good sign | 22 | 26 | says, before it starts, what the steps are |
| Y11 | good sign | 80 | 76 | says what comes after this step |
| H10 | good sign | 39 | 36 | says what it checked, and how |
| C10 | bad sign | 14 | 11 | does not answer the question in its first one or two sentences |
| T7 | bad sign | 20 | 23 | has a table cell that holds a sentence |
| T11 | bad sign | 27 | 24 | puts a command inside a sentence |
| T12 | bad sign | 2 | 5 | shows code outside a code block |
| L10 | good sign | 5 | 2 | has a light touch of humor |
| A18 | bad sign | 4 | 7 | asks the user to choose, and does not lay the options out clearly |
| O5 | good sign | 39 | 42 | names a better way than the one the user asked for |
| K6 | bad sign | 7 | 4 | points to a thing by a number and a short label, so the reader must scroll back to know what it is |
| K7 | bad sign | 9 | 6 | uses a coined term or a short name with no definition |
| K12 | bad sign | 6 | 3 | covers more than the agreed item or batch in one reply |
| K17 | bad sign | 0 | 3 | goes through items and does not show how far along it is |
| Y3 | bad sign | 6 | 3 | gives a conclusion that does not follow from its reasons |
| Y9 | good sign | 54 | 57 | names a cost or a side effect of what it proposes |

## fix-test-zh

```
== new (5 runs): 94.3% clean, 7.2 of 18 credits
   red flags: none
   faults by deck: Honesty 2/55, Content 0/60, Structure 9/80, Formatting 0/5, Wording 3/55, Asking 3/95, Opinion 1/30, Continuity 0/65, The work 1/10, Listening 0/20, Thinking 9/20
   faults: H2 x2 T4 x5 T6 x1 T11 x2 T12 x1 L3 x1 L7 x2 A1 x1 A13 x2 O7 x1 W6 x1 Y2 x4 Y4 x5
== old (5 runs): 94.7% clean, 7.6 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 0/60, Structure 9/80, Formatting 0/5, Wording 2/55, Asking 2/95, Opinion 2/30, Continuity 0/65, The work 0/10, Listening 0/20, Thinking 11/20
   faults: T4 x2 T6 x4 T11 x1 T25 x1 T26 x1 L6 x2 A4 x1 A13 x1 O7 x2 Y2 x5 Y3 x1 Y4 x5
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=7.7 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.6 headings=0.2 ends_asking=0.0 lines=16.0
old: line_refs=0.0 negations_per_1k=9.0 paragraph_only=0.0 anchors=0.0 drawings=0.2 tables=0.0 quotes=0.2 headings=0.4 ends_asking=0.2 lines=22.4
```

## chat-en

```
== new (5 runs): 96.4% clean, 7.2 of 18 credits
   red flags: none
   faults by deck: Honesty 1/55, Content 7/60, Structure 4/80, Formatting 0/5, Wording 2/55, Asking 0/95, Opinion 3/30, Continuity 1/65, The work 0/10, Listening 0/20, Thinking 0/20
   faults: H2 x1 C3 x1 C4 x1 C11 x3 C13 x2 T6 x2 T11 x1 T25 x1 L6 x1 L7 x1 O6 x3 K7 x1
== old (5 runs): 96.0% clean, 7.0 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 7/60, Structure 5/80, Formatting 0/5, Wording 2/55, Asking 1/95, Opinion 4/30, Continuity 1/65, The work 0/10, Listening 0/20, Thinking 0/20
   faults: C3 x2 C4 x1 C11 x2 C13 x2 T11 x3 T13 x1 T25 x1 L1 x2 A8 x1 O6 x4 K7 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=3.4 paragraph_only=0.0 anchors=0.0 drawings=0.8 tables=0.4 quotes=0.6 headings=0.4 ends_asking=0.0 lines=19.0
old: line_refs=0.0 negations_per_1k=4.8 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.2 quotes=0.2 headings=0.4 ends_asking=0.2 lines=18.6
```

## chat-zh

```
== new (5 runs): 96.0% clean, 8.8 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 12/60, Structure 0/80, Formatting 0/5, Wording 2/55, Asking 6/95, Opinion 0/30, Continuity 0/65, The work 0/10, Listening 0/20, Thinking 0/20
   faults: C3 x4 C10 x1 C11 x2 C13 x5 L1 x1 L3 x1 A3 x3 A9 x3
== old (5 runs): 93.7% clean, 10.0 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 12/60, Structure 3/80, Formatting 0/5, Wording 9/55, Asking 3/95, Opinion 3/30, Continuity 1/65, The work 0/10, Listening 0/20, Thinking 0/20
   faults: C3 x5 C11 x3 C13 x4 T5 x2 T6 x1 L1 x2 L2 x1 L3 x3 L5 x1 L7 x2 A3 x1 A9 x1 A22 x1 O6 x3 K7 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=17.2 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.2 quotes=0.0 headings=0.8 ends_asking=1.0 lines=28.6
old: line_refs=0.0 negations_per_1k=18.2 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.2 quotes=0.2 headings=0.6 ends_asking=0.8 lines=27.0
```

## multi-turn-zh

```
== new (5 runs): 92.5% clean, 9.8 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 17/60, Structure 15/80, Formatting 0/5, Wording 3/55, Asking 0/95, Opinion 2/30, Continuity 0/65, The work 0/10, Listening 0/20, Thinking 0/20
   faults: C3 x3 C4 x2 C6 x1 C7 x1 C10 x5 C11 x1 C13 x4 T2 x3 T4 x2 T6 x3 T7 x2 T11 x3 T25 x2 L1 x1 L6 x2 O6 x2
== old (5 runs): 88.1% clean, 10.2 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 16/60, Structure 20/80, Formatting 0/5, Wording 6/55, Asking 8/95, Opinion 2/30, Continuity 3/65, The work 4/10, Listening 0/20, Thinking 0/20
   faults: C3 x4 C4 x1 C10 x5 C11 x1 C13 x5 T2 x2 T4 x4 T6 x4 T7 x1 T11 x4 T13 x4 T26 x1 L1 x1 L5 x1 L6 x1 L7 x2 L17 x1 A3 x1 A4 x1 A8 x3 A15 x3 O6 x2 K16 x1 K18 x2 W5 x2 W6 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=8.5 paragraph_only=0.0 anchors=0.8 drawings=1.2 tables=1.4 quotes=1.4 headings=1.8 ends_asking=0.6 lines=74.6
old: line_refs=0.0 negations_per_1k=10.2 paragraph_only=0.0 anchors=0.8 drawings=1.6 tables=2.0 quotes=1.2 headings=0.6 ends_asking=0.4 lines=74.4
```

## many-items-zh

```
== new (5 runs): 89.1% clean, 12.2 of 18 credits
   red flags: A7 x1
   faults by deck: Honesty 4/55, Content 1/60, Structure 16/80, Formatting 0/5, Wording 2/55, Asking 19/95, Opinion 6/30, Continuity 1/65, The work 0/10, Listening 0/20, Thinking 5/20
   faults: H2 x1 H8 x1 H18 x2 C13 x1 T4 x2 T5 x1 T6 x5 T7 x4 T14 x1 T15 x2 T25 x1 L3 x2 A3 x3 A7 x1 A8 x4 A9 x1 A10 x1 A13 x4 A15 x1 A18 x3 A19 x1 O1 x2 O7 x4 K19 x1 Y1 x1 Y2 x1 Y3 x1 Y4 x2
== old (5 runs): 83.4% clean, 12.2 of 18 credits
   red flags: H4 x2, A7 x2
   faults by deck: Honesty 5/55, Content 11/60, Structure 18/80, Formatting 0/5, Wording 2/55, Asking 25/95, Opinion 8/30, Continuity 6/65, The work 0/10, Listening 1/20, Thinking 6/20
   faults: H2 x1 H4 x2 H8 x2 C2 x1 C3 x3 C4 x3 C10 x1 C13 x3 T4 x2 T5 x3 T6 x4 T7 x5 T11 x1 T15 x3 L3 x2 A3 x2 A7 x2 A8 x4 A9 x2 A10 x2 A13 x3 A15 x3 A18 x2 A21 x2 A22 x3 O1 x3 O4 x2 O7 x3 K4 x1 K6 x1 K12 x3 K16 x1 E2 x1 Y1 x2 Y2 x1 Y3 x1 Y4 x2
bar: failed, red flags in new: A7 x1

Checks:
new: line_refs=0.0 negations_per_1k=14.1 paragraph_only=0.0 anchors=0.0 drawings=0.8 tables=1.6 quotes=0.2 headings=1.8 ends_asking=1.8 lines=71.8
old: line_refs=0.0 negations_per_1k=10.4 paragraph_only=0.0 anchors=0.8 drawings=0.0 tables=1.8 quotes=0.6 headings=2.2 ends_asking=2.0 lines=75.2
```

## design-flaw-zh

```
== new (5 runs): 91.5% clean, 9.2 of 18 credits
   red flags: none
   faults by deck: Honesty 3/55, Content 1/60, Structure 13/80, Formatting 0/5, Wording 2/55, Asking 11/95, Opinion 1/30, Continuity 2/65, The work 5/10, Listening 1/20, Thinking 3/20
   faults: H2 x1 H8 x1 H18 x1 C3 x1 T2 x3 T4 x1 T5 x1 T6 x2 T7 x2 T11 x3 T15 x1 L1 x1 L6 x1 A3 x3 A8 x3 A10 x4 A22 x1 O7 x1 K7 x1 K16 x1 W6 x5 E4 x1 Y2 x1 Y4 x2
== old (5 runs): 92.3% clean, 10.8 of 18 credits
   red flags: O2 x1
   faults by deck: Honesty 3/55, Content 6/60, Structure 12/80, Formatting 0/5, Wording 0/55, Asking 7/95, Opinion 3/30, Continuity 0/65, The work 3/10, Listening 0/20, Thinking 4/20
   faults: H2 x1 H8 x2 C3 x3 C7 x1 C11 x2 T2 x3 T4 x1 T5 x1 T6 x2 T7 x1 T11 x2 T15 x2 A3 x3 A8 x2 A10 x1 A18 x1 O2 x1 O7 x2 W6 x3 Y4 x4
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=8.4 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.6 quotes=0.0 headings=0.6 ends_asking=1.0 lines=24.4
old: line_refs=0.0 negations_per_1k=6.6 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.4 quotes=0.0 headings=0.6 ends_asking=0.8 lines=26.0
```

## long-discussion-zh

```
== new (5 runs): 84.0% clean, 12.4 of 18 credits
   red flags: A7 x1
   faults by deck: Honesty 1/55, Content 10/60, Structure 25/80, Formatting 0/5, Wording 7/55, Asking 13/95, Opinion 4/30, Continuity 18/65, The work 0/10, Listening 0/20, Thinking 1/20
   faults: H8 x1 C3 x1 C7 x1 C10 x3 C11 x1 C13 x4 T2 x3 T4 x4 T5 x2 T6 x5 T7 x5 T13 x2 T25 x1 T26 x3 L1 x5 L7 x2 A2 x3 A3 x4 A7 x1 A10 x1 A13 x2 A19 x1 A22 x1 O6 x4 K1 x5 K2 x4 K5 x1 K6 x1 K16 x2 K17 x2 K18 x3 Y3 x1
== old (5 runs): 85.9% clean, 12.0 of 18 credits
   red flags: K15 x2
   faults by deck: Honesty 2/55, Content 7/60, Structure 22/80, Formatting 0/5, Wording 8/55, Asking 9/95, Opinion 3/30, Continuity 18/65, The work 0/10, Listening 1/20, Thinking 0/20
   faults: H2 x1 H8 x1 C10 x2 C11 x1 C13 x4 T2 x3 T4 x3 T5 x1 T6 x5 T7 x5 T26 x5 L1 x5 L3 x1 L7 x2 A2 x3 A3 x3 A8 x3 O6 x3 K1 x5 K2 x5 K15 x2 K7 x2 K16 x2 K18 x2 E4 x1
bar: failed, red flags in new: A7 x1

Checks:
new: line_refs=0.0 negations_per_1k=10.6 paragraph_only=0.0 anchors=3.0 drawings=2.8 tables=5.0 quotes=1.8 headings=1.2 ends_asking=5.0 lines=163.6
old: line_refs=0.0 negations_per_1k=11.7 paragraph_only=0.0 anchors=2.8 drawings=3.2 tables=5.2 quotes=3.0 headings=3.6 ends_asking=4.6 lines=159.2
```

## shape-zh

```
== new (5 runs): 93.5% clean, 6.0 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 2/60, Structure 16/80, Formatting 0/5, Wording 7/55, Asking 1/95, Opinion 0/30, Continuity 2/65, The work 4/10, Listening 0/20, Thinking 0/20
   faults: C3 x1 C10 x1 T5 x4 T6 x4 T13 x2 T15 x5 T25 x1 L1 x3 L3 x2 L6 x2 A5 x1 K7 x2 W5 x2 W6 x2
== old (5 runs): 94.3% clean, 6.0 of 18 credits
   red flags: none
   faults by deck: Honesty 2/55, Content 2/60, Structure 12/80, Formatting 0/5, Wording 6/55, Asking 3/95, Opinion 1/30, Continuity 2/65, The work 0/10, Listening 0/20, Thinking 0/20
   faults: H2 x2 C3 x1 C10 x1 T4 x2 T5 x2 T6 x2 T15 x5 T25 x1 L1 x3 L3 x1 L6 x1 L7 x1 A5 x1 A13 x2 O7 x1 K7 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=3.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.2 quotes=0.8 headings=0.8 ends_asking=0.0 lines=43.2
old: line_refs=0.0 negations_per_1k=4.3 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.6 quotes=0.2 headings=0.4 ends_asking=0.0 lines=40.8
```

## fact-zh

```
== new (5 runs): 97.8% clean, 3.0 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 3/60, Structure 3/80, Formatting 0/5, Wording 5/55, Asking 0/95, Opinion 0/30, Continuity 0/65, The work 0/10, Listening 0/20, Thinking 0/20
   faults: C3 x2 C11 x1 T5 x1 T7 x2 L6 x2 L7 x2 L8 x1
== old (5 runs): 97.6% clean, 4.6 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 5/60, Structure 3/80, Formatting 0/5, Wording 4/55, Asking 0/95, Opinion 0/30, Continuity 0/65, The work 0/10, Listening 0/20, Thinking 0/20
   faults: C3 x2 C4 x1 C11 x2 T5 x1 T6 x1 T7 x1 L6 x1 L7 x3
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=25.6 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.8 quotes=0.8 headings=0.0 ends_asking=0.0 lines=16.6
old: line_refs=0.0 negations_per_1k=22.5 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.8 quotes=1.0 headings=0.0 ends_asking=0.0 lines=18.8
```

## your-step-zh

```
== new (5 runs): 94.5% clean, 7.2 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 11/60, Structure 14/80, Formatting 0/5, Wording 2/55, Asking 0/95, Opinion 0/30, Continuity 0/65, The work 0/10, Listening 0/20, Thinking 0/20
   faults: C3 x4 C4 x2 C11 x2 C13 x3 T2 x4 T5 x3 T7 x1 T11 x5 T26 x1 L5 x1 L6 x1
== old (5 runs): 93.7% clean, 6.8 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 6/60, Structure 19/80, Formatting 0/5, Wording 2/55, Asking 2/95, Opinion 1/30, Continuity 0/65, The work 0/10, Listening 0/20, Thinking 1/20
   faults: C3 x2 C4 x1 C11 x1 C13 x2 T2 x5 T4 x1 T5 x4 T6 x2 T11 x4 T13 x1 T25 x1 T26 x1 L1 x1 L6 x1 A8 x1 A15 x1 O7 x1 Y2 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=10.9 paragraph_only=0.0 anchors=0.0 drawings=0.2 tables=0.4 quotes=0.6 headings=0.6 ends_asking=0.0 lines=23.6
old: line_refs=0.0 negations_per_1k=9.4 paragraph_only=0.0 anchors=0.0 drawings=0.2 tables=0.2 quotes=0.4 headings=0.4 ends_asking=0.0 lines=19.2
```

## clear-step-zh

```
== new (5 runs): 95.4% clean, 6.2 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 1/60, Structure 9/80, Formatting 0/5, Wording 1/55, Asking 6/95, Opinion 3/30, Continuity 0/65, The work 3/10, Listening 0/20, Thinking 0/20
   faults: C3 x1 T1 x1 T4 x4 T6 x1 T12 x3 L3 x1 A3 x1 A4 x1 A13 x1 A18 x2 A22 x1 O7 x3 W6 x3
== old (5 runs): 93.9% clean, 5.8 of 18 credits
   red flags: H4 x1
   faults by deck: Honesty 2/55, Content 3/60, Structure 5/80, Formatting 0/5, Wording 0/55, Asking 10/95, Opinion 2/30, Continuity 0/65, The work 7/10, Listening 1/20, Thinking 0/20
   faults: H2 x1 H4 x1 C3 x1 C11 x2 T1 x1 T4 x1 T5 x1 T6 x1 T11 x1 A3 x2 A4 x4 A13 x1 A20 x1 A22 x2 O7 x2 W5 x2 W6 x5 E4 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=9.0 paragraph_only=0.2 anchors=0.0 drawings=0.2 tables=0.0 quotes=0.6 headings=0.0 ends_asking=0.2 lines=9.6
old: line_refs=0.0 negations_per_1k=10.5 paragraph_only=0.2 anchors=0.0 drawings=0.2 tables=0.0 quotes=0.2 headings=0.0 ends_asking=0.2 lines=7.6
```

## detail-zh

```
== new (5 runs): 90.9% clean, 9.2 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 1/60, Structure 28/80, Formatting 0/5, Wording 8/55, Asking 2/95, Opinion 0/30, Continuity 6/65, The work 0/10, Listening 0/20, Thinking 0/20
   faults: C13 x1 T2 x1 T4 x5 T5 x1 T6 x2 T7 x1 T11 x4 T15 x3 T19 x4 T25 x2 T26 x5 L3 x3 L6 x1 L7 x4 A21 x2 K7 x1 K8 x1 K12 x2 K17 x1 K18 x1
== old (5 runs): 89.1% clean, 10.0 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 3/60, Structure 30/80, Formatting 0/5, Wording 13/55, Asking 1/95, Opinion 0/30, Continuity 6/65, The work 0/10, Listening 0/20, Thinking 1/20
   faults: C3 x1 C10 x1 C13 x1 T2 x2 T4 x5 T5 x1 T6 x3 T7 x2 T11 x5 T15 x2 T19 x4 T25 x4 T26 x2 L1 x3 L3 x3 L6 x2 L7 x5 A13 x1 K6 x1 K7 x1 K12 x1 K18 x1 K19 x2 Y3 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=4.4 paragraph_only=0.0 anchors=0.0 drawings=2.0 tables=1.6 quotes=1.0 headings=2.0 ends_asking=0.0 lines=102.6
old: line_refs=0.0 negations_per_1k=5.0 paragraph_only=0.0 anchors=0.0 drawings=2.0 tables=2.0 quotes=1.8 headings=1.4 ends_asking=0.0 lines=107.4
```

## only-you-know-zh

```
== new (5 runs): 92.5% clean, 5.4 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 3/60, Structure 8/80, Formatting 0/5, Wording 1/55, Asking 10/95, Opinion 5/30, Continuity 0/65, The work 10/10, Listening 0/20, Thinking 0/20
   faults: C3 x1 C13 x2 T2 x1 T5 x2 T6 x2 T11 x1 T13 x2 L3 x1 A9 x2 A10 x3 A13 x5 O1 x5 W5 x5 W6 x5
== old (5 runs): 92.7% clean, 5.6 of 18 credits
   red flags: none
   faults by deck: Honesty 2/55, Content 5/60, Structure 10/80, Formatting 0/5, Wording 0/55, Asking 5/95, Opinion 4/30, Continuity 0/65, The work 10/10, Listening 0/20, Thinking 0/20
   faults: H2 x1 H18 x1 C3 x1 C11 x1 C13 x3 T4 x2 T5 x2 T11 x1 T13 x4 T25 x1 A10 x1 A13 x4 O1 x4 W5 x5 W6 x5
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=13.9 paragraph_only=0.0 anchors=0.0 drawings=0.6 tables=0.0 quotes=0.2 headings=0.4 ends_asking=1.0 lines=15.2
old: line_refs=0.0 negations_per_1k=12.7 paragraph_only=0.0 anchors=0.0 drawings=0.6 tables=0.0 quotes=0.2 headings=0.6 ends_asking=1.0 lines=16.4
```

## shape-en

```
== new (5 runs): 92.5% clean, 6.4 of 18 credits
   red flags: none
   faults by deck: Honesty 1/55, Content 2/60, Structure 13/80, Formatting 0/5, Wording 7/55, Asking 9/95, Opinion 0/30, Continuity 1/65, The work 4/10, Listening 0/20, Thinking 0/20
   faults: H2 x1 C3 x1 C10 x1 T1 x1 T4 x1 T6 x4 T12 x1 T13 x2 T15 x3 T25 x1 L1 x3 L3 x1 L6 x2 L7 x1 A3 x1 A4 x1 A5 x3 A8 x1 A13 x1 A15 x2 K7 x1 W5 x2 W6 x2
== old (5 runs): 94.7% clean, 3.8 of 18 credits
   red flags: none
   faults by deck: Honesty 0/55, Content 5/60, Structure 10/80, Formatting 1/5, Wording 4/55, Asking 5/95, Opinion 0/30, Continuity 1/65, The work 0/10, Listening 0/20, Thinking 0/20
   faults: C3 x1 C8 x2 C10 x2 T1 x2 T6 x3 T12 x2 T13 x1 T15 x2 M1 x1 L1 x1 L3 x2 L7 x1 A3 x1 A5 x2 A13 x1 A15 x1 K7 x1
bar: failed, new is more than 2 points under old

Checks:
new: line_refs=0.0 negations_per_1k=1.4 paragraph_only=0.2 anchors=0.0 drawings=0.8 tables=0.0 quotes=0.0 headings=0.8 ends_asking=0.2 lines=38.0
old: line_refs=0.0 negations_per_1k=1.1 paragraph_only=0.4 anchors=0.0 drawings=0.6 tables=0.2 quotes=0.0 headings=0.4 ends_asking=0.4 lines=43.0
```

## session-zh

```
== new (5 runs): 83.8% clean, 11.2 of 18 credits
   red flags: none
   faults by deck: Honesty 2/55, Content 9/60, Structure 26/80, Formatting 0/5, Wording 5/55, Asking 10/95, Opinion 3/30, Continuity 14/65, The work 1/10, Listening 0/20, Thinking 10/20
   faults: H7 x1 H18 x1 C3 x3 C4 x2 C13 x4 T2 x2 T4 x5 T5 x2 T6 x5 T7 x1 T11 x4 T19 x2 T25 x3 T26 x2 L4 x1 L6 x2 L7 x1 L15 x1 A3 x2 A4 x1 A8 x1 A9 x1 A13 x1 A15 x2 A21 x1 A22 x1 O1 x1 O7 x2 K1 x5 K2 x4 K16 x5 W6 x1 Y2 x4 Y3 x1 Y4 x5
== old (5 runs): 83.8% clean, 12.0 of 18 credits
   red flags: H4 x1
   faults by deck: Honesty 4/55, Content 11/60, Structure 24/80, Formatting 0/5, Wording 1/55, Asking 12/95, Opinion 3/30, Continuity 17/65, The work 0/10, Listening 0/20, Thinking 8/20
   faults: H1 x1 H4 x1 H18 x2 C3 x1 C4 x4 C10 x1 C13 x5 T2 x2 T4 x4 T5 x2 T6 x5 T11 x4 T13 x1 T19 x1 T25 x1 T26 x4 L7 x1 A8 x1 A13 x2 A15 x5 A18 x1 A20 x1 A22 x2 O7 x3 K1 x5 K2 x5 K12 x1 K16 x5 K19 x1 Y2 x4 Y3 x1 Y4 x3
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=8.3 paragraph_only=0.0 anchors=0.0 drawings=1.8 tables=1.4 quotes=1.6 headings=0.8 ends_asking=0.8 lines=67.2
old: line_refs=0.0 negations_per_1k=8.3 paragraph_only=0.0 anchors=0.0 drawings=1.8 tables=1.4 quotes=1.2 headings=2.4 ends_asking=0.0 lines=84.4
```

## better-way-zh

```
== new (5 runs): 94.9% clean, 7.8 of 18 credits
   red flags: none
   faults by deck: Honesty 4/55, Content 3/60, Structure 9/80, Formatting 0/5, Wording 0/55, Asking 1/95, Opinion 4/30, Continuity 3/65, The work 0/10, Listening 0/20, Thinking 1/20
   faults: H8 x4 C4 x2 C13 x1 T5 x4 T13 x1 T15 x4 A20 x1 O6 x4 K6 x2 K12 x1 Y2 x1
== old (5 runs): 94.5% clean, 8.2 of 18 credits
   red flags: none
   faults by deck: Honesty 4/55, Content 10/60, Structure 6/80, Formatting 0/5, Wording 1/55, Asking 0/95, Opinion 0/30, Continuity 5/65, The work 0/10, Listening 0/20, Thinking 1/20
   faults: H8 x4 C3 x5 C4 x3 C10 x1 C11 x1 T5 x1 T13 x1 T15 x4 L6 x1 K6 x3 K7 x1 K12 x1 Y2 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=5.8 paragraph_only=0.0 anchors=0.0 drawings=0.2 tables=0.0 quotes=0.4 headings=0.6 ends_asking=0.0 lines=25.6
old: line_refs=0.0 negations_per_1k=5.6 paragraph_only=0.0 anchors=0.0 drawings=0.6 tables=0.6 quotes=0.6 headings=0.2 ends_asking=0.0 lines=28.8
```

## vague-zh

```
== new (5 runs): 91.3% clean, 9.8 of 18 credits
   red flags: none
   faults by deck: Honesty 4/55, Content 1/60, Structure 10/80, Formatting 0/5, Wording 2/55, Asking 16/95, Opinion 3/30, Continuity 1/65, The work 2/10, Listening 0/20, Thinking 4/20
   faults: H1 x2 H8 x1 H18 x1 C3 x1 T6 x4 T7 x5 T11 x1 L1 x1 L3 x1 A3 x1 A4 x2 A8 x5 A10 x2 A13 x1 A15 x2 A18 x1 A20 x1 A21 x1 O7 x3 K6 x1 W5 x1 W6 x1 Y4 x4
== old (5 runs): 91.7% clean, 9.4 of 18 credits
   red flags: A7 x1
   faults by deck: Honesty 2/55, Content 2/60, Structure 10/80, Formatting 0/5, Wording 1/55, Asking 15/95, Opinion 2/30, Continuity 2/65, The work 3/10, Listening 0/20, Thinking 4/20
   faults: H2 x1 H8 x1 C3 x2 T6 x5 T7 x5 L3 x1 A3 x1 A6 x1 A7 x1 A8 x5 A10 x2 A13 x1 A15 x2 A21 x1 A22 x1 O7 x2 K6 x2 W5 x1 W6 x2 Y3 x1 Y4 x3
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=12.4 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.4 headings=1.0 ends_asking=0.8 lines=26.0
old: line_refs=0.0 negations_per_1k=10.8 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=1.0 ends_asking=0.6 lines=25.6
```

## conflict-zh

```
== new (5 runs): 94.9% clean, 3.6 of 18 credits
   red flags: none
   faults by deck: Honesty 5/55, Content 2/60, Structure 11/80, Formatting 0/5, Wording 0/55, Asking 6/95, Opinion 1/30, Continuity 0/65, The work 0/10, Listening 0/20, Thinking 0/20
   faults: H8 x5 C5 x2 T1 x5 T4 x3 T5 x3 A4 x1 A6 x1 A13 x3 A18 x1 O1 x1
== old (5 runs): 94.5% clean, 4.4 of 18 credits
   red flags: none
   faults by deck: Honesty 5/55, Content 1/60, Structure 15/80, Formatting 0/5, Wording 2/55, Asking 4/95, Opinion 0/30, Continuity 0/65, The work 0/10, Listening 0/20, Thinking 0/20
   faults: H8 x5 C5 x1 T1 x3 T4 x4 T5 x4 T13 x2 T26 x2 L3 x1 L4 x1 A13 x2 A22 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=14.8 paragraph_only=1.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.4 lines=1.2
old: line_refs=0.0 negations_per_1k=12.6 paragraph_only=0.6 anchors=0.0 drawings=0.4 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=3.0
```

## conflict-agent-zh

```
== new (5 runs): 93.9% clean, 7.6 of 18 credits
   red flags: none
   faults by deck: Honesty 1/55, Content 3/60, Structure 5/80, Formatting 0/5, Wording 6/55, Asking 6/95, Opinion 0/30, Continuity 0/65, The work 9/10, Listening 0/20, Thinking 0/20
   faults: H2 x1 C3 x1 C11 x1 C13 x1 T6 x5 L1 x1 L6 x3 L7 x2 A6 x3 A10 x3 W5 x4 W6 x5
== old (5 runs): 95.4% clean, 7.4 of 18 credits
   red flags: none
   faults by deck: Honesty 1/55, Content 3/60, Structure 6/80, Formatting 0/5, Wording 0/55, Asking 4/95, Opinion 0/30, Continuity 0/65, The work 8/10, Listening 0/20, Thinking 1/20
   faults: H2 x1 C3 x2 C13 x1 T6 x5 T11 x1 A6 x3 A8 x1 W5 x4 W6 x4 Y3 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=13.3 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.2 ends_asking=1.0 lines=13.8
old: line_refs=0.0 negations_per_1k=13.9 paragraph_only=0.0 anchors=0.0 drawings=0.4 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=15.8
```
