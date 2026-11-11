# Eval 2026-11-11-none-vs-13a35d4-opus-5-5

- new: `13a35d4` (13a35d4)
- none: no plugin
- model: claude-opus-5-5, effort medium, judge claude-haiku-5-5 x3 on rubric-yesno.md, claude-opus-5-5 on its 🔎 lines, x3 where it raises a red flag
- runs: {'kept': 114}
- spent: $16.39 of $52.90

## Overall

score = quality x (1 - 0.5 x the share of replies with a red flag). Quality weighs the words of PHILOSOPHY.md by rank; a line that does not apply counts for nothing.

| | new | none |
|---|---|---|
| **score** | 82.1 | 77.2 |
| quality | 85.9 | 79.3 |
| replies with a red flag | 5/57 | 3/57 |
| Honest (8) | 75.0 | 58.1 |
| Simple (7) | 88.5 | 89.2 |
| Structured (6) | 85.4 | 68.0 |
| Asking (5) | 89.0 | 92.6 |
| Opinionated (4) | 93.7 | 93.9 |
| Focused, Standalone (5) | 89.1 | 83.6 |
| Predictable (1) | 94.6 | 100.0 |

## fix-test-zh

```
== new (3 runs): 91.4% clean, 8.7 of 18 credits
   red flags: none
   faults by deck: Honesty 2/33, Content 2/36, Structure 7/48, Formatting 0/6, Wording 1/33, Asking 7/57, Opinion 2/15, Continuity 0/45, The work 0/6, Listening 0/12, Thinking 5/12
   faults: H2 x2 C11 x1 C12 x1 T5 x2 T6 x3 T11 x1 T15 x1 L6 x1 A4 x1 A9 x1 A10 x1 A13 x3 A17 x1 O6 x2 Y2 x2 Y4 x3
== none (3 runs): 91.4% clean, 5.7 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 4/36, Structure 10/48, Formatting 0/6, Wording 0/33, Asking 5/57, Opinion 0/15, Continuity 0/45, The work 1/6, Listening 0/12, Thinking 6/12
   faults: C7 x3 C12 x1 T1 x1 T2 x1 T4 x3 T6 x2 T8 x2 T11 x1 A3 x1 A13 x3 A18 x1 W6 x1 Y2 x3 Y4 x3

Checks:
new: line_refs=0.0 negations_per_1k=7.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=29.7
none: line_refs=0.0 negations_per_1k=3.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.3 lines=7.3
```

## chat-en

```
== new (3 runs): 95.0% clean, 7.0 of 18 credits
   red flags: none
   faults by deck: Honesty 1/33, Content 4/36, Structure 2/48, Formatting 0/6, Wording 2/33, Asking 2/57, Opinion 2/15, Continuity 2/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: H2 x1 C3 x1 C4 x1 C12 x2 T6 x1 T11 x1 L3 x2 A15 x1 A17 x1 O6 x2 K7 x2
== none (3 runs): 96.0% clean, 5.3 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 1/36, Structure 7/48, Formatting 0/6, Wording 3/33, Asking 0/57, Opinion 0/15, Continuity 1/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C12 x1 T6 x3 T8 x1 T11 x3 L3 x3 K7 x1

Checks:
new: line_refs=0.0 negations_per_1k=1.4 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.7 headings=0.0 ends_asking=1.0 lines=18.3
none: line_refs=0.0 negations_per_1k=3.1 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=15.0
```

## chat-zh

```
== new (3 runs): 94.7% clean, 8.7 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 3/36, Structure 2/48, Formatting 0/6, Wording 7/33, Asking 3/57, Opinion 1/15, Continuity 0/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C3 x1 C4 x1 C12 x1 T4 x1 T6 x1 L1 x1 L3 x3 L5 x1 L7 x2 A3 x1 A17 x1 A20 x1 O6 x1
== none (3 runs): 92.7% clean, 7.3 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 4/36, Structure 9/48, Formatting 0/6, Wording 4/33, Asking 1/57, Opinion 0/15, Continuity 4/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C3 x1 C12 x3 T2 x3 T4 x1 T6 x3 T8 x1 T11 x1 L1 x1 L3 x3 A3 x1 K7 x2 K10 x2

Checks:
new: line_refs=0.0 negations_per_1k=18.6 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.7 headings=0.0 ends_asking=1.0 lines=23.7
none: line_refs=0.0 negations_per_1k=5.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.3 ends_asking=0.0 lines=15.0
```

## multi-turn-zh

```
== new (3 runs): 89.8% clean, 10.3 of 18 credits
   red flags: K15 x2
   faults by deck: Honesty 0/33, Content 5/36, Structure 5/48, Formatting 2/6, Wording 3/33, Asking 9/57, Opinion 0/15, Continuity 7/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C10 x2 C12 x3 T4 x1 T6 x1 T11 x3 M13 x2 L3 x3 A2 x3 A3 x1 A8 x2 A13 x1 A17 x2 K15 x2 K10 x3 K16 x1 K17 x1
== none (3 runs): 83.8% clean, 8.3 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 6/36, Structure 13/48, Formatting 0/6, Wording 6/33, Asking 5/57, Opinion 0/15, Continuity 19/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C4 x2 C10 x1 C12 x3 T5 x1 T6 x3 T7 x3 T8 x3 T11 x3 L1 x1 L3 x3 L5 x1 L7 x1 A9 x3 A15 x2 K1 x3 K2 x3 K9 x1 K10 x3 K16 x3 K17 x3 K18 x3

Checks:
new: line_refs=0.0 negations_per_1k=8.6 paragraph_only=0.0 anchors=0.7 drawings=2.7 tables=1.0 quotes=2.0 headings=0.0 ends_asking=3.0 lines=80.0
none: line_refs=0.0 negations_per_1k=6.3 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.7 quotes=0.0 headings=3.0 ends_asking=0.0 lines=71.7
```

## many-items-zh

```
== new (3 runs): 86.1% clean, 12.3 of 18 credits
   red flags: A7 x1, K15 x1
   faults by deck: Honesty 4/33, Content 4/36, Structure 9/48, Formatting 1/6, Wording 2/33, Asking 13/57, Opinion 0/15, Continuity 7/45, The work 0/6, Listening 2/12, Thinking 0/12
   faults: H8 x2 H16 x2 C11 x1 C12 x3 T2 x1 T4 x1 T6 x2 T7 x2 T14 x1 T15 x1 T19 x1 M13 x1 L3 x2 A3 x1 A6 x1 A7 x1 A8 x2 A10 x2 A13 x3 A15 x1 A17 x2 K15 x1 K6 x2 K8 x2 K10 x1 K16 x1 E4 x2
== none (3 runs): 82.8% clean, 8.3 of 18 credits
   red flags: A7 x2
   faults by deck: Honesty 3/33, Content 3/36, Structure 11/48, Formatting 0/6, Wording 2/33, Asking 14/57, Opinion 4/15, Continuity 11/45, The work 1/6, Listening 0/12, Thinking 3/12
   faults: H2 x1 H8 x2 C12 x3 T4 x3 T5 x1 T6 x3 T7 x1 T8 x3 L3 x2 A7 x2 A8 x2 A9 x1 A10 x3 A13 x3 A17 x2 A21 x1 O1 x1 O4 x3 K4 x1 K9 x2 K10 x3 K12 x2 K16 x1 K17 x1 K18 x1 W6 x1 Y4 x3

Checks:
new: line_refs=0.0 negations_per_1k=8.8 paragraph_only=0.0 anchors=0.0 drawings=0.7 tables=1.7 quotes=2.3 headings=0.0 ends_asking=3.0 lines=103.3
none: line_refs=10.0 negations_per_1k=16.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.3 quotes=0.0 headings=1.0 ends_asking=0.3 lines=46.7
```

## design-flaw-zh

```
== new (3 runs): 91.4% clean, 7.7 of 18 credits
   red flags: none
   faults by deck: Honesty 2/33, Content 3/36, Structure 4/48, Formatting 0/6, Wording 6/33, Asking 6/57, Opinion 0/15, Continuity 1/45, The work 4/6, Listening 0/12, Thinking 0/12
   faults: H2 x1 H18 x1 C12 x3 T4 x1 T5 x1 T6 x1 T11 x1 L1 x1 L3 x3 L5 x1 L7 x1 A10 x3 A17 x3 K10 x1 W5 x1 W6 x3
== none (3 runs): 90.8% clean, 7.0 of 18 credits
   red flags: none
   faults by deck: Honesty 3/33, Content 3/36, Structure 8/48, Formatting 0/6, Wording 2/33, Asking 4/57, Opinion 2/15, Continuity 1/45, The work 3/6, Listening 0/12, Thinking 2/12
   faults: H8 x3 C3 x1 C12 x2 T4 x2 T5 x1 T6 x2 T11 x3 L3 x2 A3 x2 A4 x2 O6 x2 K10 x1 W6 x3 Y2 x1 Y4 x1

Checks:
new: line_refs=0.0 negations_per_1k=17.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.3 quotes=0.0 headings=0.0 ends_asking=1.0 lines=20.7
none: line_refs=0.0 negations_per_1k=19.1 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.7 lines=16.0
```

## long-discussion-zh

```
== new (3 runs): 83.5% clean, 12.0 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 7/36, Structure 6/48, Formatting 3/6, Wording 7/33, Asking 13/57, Opinion 2/15, Continuity 12/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C3 x1 C4 x1 C10 x3 C12 x2 T5 x2 T6 x2 T7 x1 T13 x1 M13 x3 L1 x2 L3 x3 L5 x1 L7 x1 A2 x2 A3 x3 A4 x1 A5 x1 A6 x1 A9 x1 A15 x1 A17 x3 O6 x2 K1 x2 K2 x1 K7 x2 K10 x3 K16 x2 K18 x2
== none (3 runs): 78.9% clean, 9.3 of 18 credits
   red flags: K15 x1
   faults by deck: Honesty 3/33, Content 7/36, Structure 23/48, Formatting 0/6, Wording 6/33, Asking 3/57, Opinion 0/15, Continuity 22/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: H2 x3 C7 x1 C10 x2 C11 x1 C12 x3 T2 x3 T3 x3 T4 x3 T5 x2 T6 x3 T7 x3 T8 x3 T11 x2 T13 x1 L3 x3 L7 x2 L8 x1 A3 x2 A9 x1 K1 x2 K2 x2 K15 x1 K5 x2 K7 x2 K10 x3 K16 x3 K17 x3 K18 x3 K19 x1

Checks:
new: line_refs=0.0 negations_per_1k=9.2 paragraph_only=0.0 anchors=2.0 drawings=5.0 tables=3.0 quotes=5.7 headings=0.0 ends_asking=5.3 lines=143.3
none: line_refs=0.0 negations_per_1k=7.4 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=2.7 quotes=0.0 headings=5.7 ends_asking=0.7 lines=143.0
```

## shape-zh

```
== new (3 runs): 93.4% clean, 7.0 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 6/36, Structure 6/48, Formatting 0/6, Wording 3/33, Asking 1/57, Opinion 0/15, Continuity 4/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C3 x2 C7 x1 C10 x1 C12 x2 T5 x1 T6 x3 T15 x1 T25 x1 L3 x2 L7 x1 A17 x1 K6 x2 K7 x1 K10 x1
== none (3 runs): 93.1% clean, 2.0 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 4/36, Structure 10/48, Formatting 0/6, Wording 2/33, Asking 1/57, Opinion 0/15, Continuity 4/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C8 x1 C10 x1 C12 x2 T1 x1 T6 x1 T7 x2 T8 x2 T15 x2 T25 x2 L3 x2 A20 x1 K7 x2 K10 x2

Checks:
new: line_refs=0.0 negations_per_1k=3.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=35.7
none: line_refs=0.0 negations_per_1k=12.7 paragraph_only=0.3 anchors=0.0 drawings=0.7 tables=0.7 quotes=0.0 headings=0.7 ends_asking=0.0 lines=46.0
```

## fact-zh

```
== new (3 runs): 96.4% clean, 1.7 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 6/36, Structure 2/48, Formatting 0/6, Wording 2/33, Asking 0/57, Opinion 0/15, Continuity 1/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C3 x1 C4 x1 C8 x1 C10 x1 C12 x2 T5 x1 T6 x1 L3 x1 L7 x1 K10 x1
== none (3 runs): 94.7% clean, 1.3 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 6/36, Structure 5/48, Formatting 0/6, Wording 3/33, Asking 0/57, Opinion 0/15, Continuity 2/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C3 x2 C4 x1 C11 x1 C12 x2 T6 x1 T7 x2 T8 x2 L3 x2 L6 x1 K9 x1 K10 x1

Checks:
new: line_refs=0.0 negations_per_1k=11.7 paragraph_only=0.0 anchors=0.0 drawings=0.7 tables=0.3 quotes=0.0 headings=0.0 ends_asking=0.0 lines=14.0
none: line_refs=0.0 negations_per_1k=14.9 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.3 headings=0.7 ends_asking=0.0 lines=22.7
```

## your-step-zh

```
== new (3 runs): 92.4% clean, 7.3 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 6/36, Structure 8/48, Formatting 1/6, Wording 0/33, Asking 2/57, Opinion 0/15, Continuity 0/45, The work 2/6, Listening 0/12, Thinking 4/12
   faults: C3 x3 C4 x1 C11 x1 C12 x1 T5 x2 T6 x2 T11 x3 T14 x1 M1 x1 A13 x1 A17 x1 W5 x1 W6 x1 Y1 x2 Y2 x1 Y4 x1
== none (3 runs): 91.7% clean, 5.7 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 4/36, Structure 13/48, Formatting 0/6, Wording 1/33, Asking 2/57, Opinion 0/15, Continuity 0/45, The work 2/6, Listening 0/12, Thinking 3/12
   faults: C11 x1 C12 x3 T2 x3 T5 x3 T6 x1 T8 x1 T11 x3 T13 x1 T14 x1 L3 x1 A13 x1 A20 x1 W5 x1 W6 x1 Y1 x2 Y4 x1

Checks:
new: line_refs=0.0 negations_per_1k=7.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.3 quotes=1.0 headings=0.0 ends_asking=0.0 lines=29.3
none: line_refs=0.0 negations_per_1k=5.6 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=1.0 ends_asking=0.0 lines=21.7
```

## clear-step-zh

```
== new (3 runs): 96.0% clean, 5.3 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 4/36, Structure 3/48, Formatting 0/6, Wording 0/33, Asking 4/57, Opinion 0/15, Continuity 0/45, The work 1/6, Listening 0/12, Thinking 0/12
   faults: C11 x1 C12 x3 T4 x1 T6 x2 A3 x2 A10 x1 A17 x1 W6 x1
== none (3 runs): 96.7% clean, 4.7 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 1/36, Structure 1/48, Formatting 0/6, Wording 0/33, Asking 2/57, Opinion 0/15, Continuity 0/45, The work 5/6, Listening 1/12, Thinking 0/12
   faults: C12 x1 T6 x1 A9 x1 A13 x1 W5 x2 W6 x3 E4 x1

Checks:
new: line_refs=0.0 negations_per_1k=9.1 paragraph_only=0.0 anchors=0.0 drawings=0.3 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=15.0
none: line_refs=1.0 negations_per_1k=12.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.7 lines=11.3
```

## detail-zh

```
== new (3 runs): 91.1% clean, 10.0 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 5/36, Structure 13/48, Formatting 0/6, Wording 8/33, Asking 0/57, Opinion 0/15, Continuity 1/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C4 x2 C12 x3 T4 x3 T5 x1 T6 x2 T7 x2 T11 x2 T13 x1 T25 x2 L3 x3 L4 x1 L5 x1 L7 x3 K18 x1
== none (3 runs): 81.2% clean, 8.0 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 8/36, Structure 25/48, Formatting 0/6, Wording 14/33, Asking 1/57, Opinion 0/15, Continuity 9/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C4 x3 C10 x2 C12 x3 T2 x3 T4 x3 T5 x3 T6 x3 T7 x3 T8 x3 T11 x3 T19 x2 T25 x2 L3 x3 L4 x3 L6 x1 L7 x3 L8 x3 L15 x1 A21 x1 K7 x1 K9 x3 K10 x2 K18 x3

Checks:
new: line_refs=0.0 negations_per_1k=3.3 paragraph_only=0.0 anchors=0.0 drawings=2.0 tables=1.7 quotes=2.0 headings=1.0 ends_asking=0.0 lines=119.0
none: line_refs=0.0 negations_per_1k=4.2 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=2.0 quotes=1.0 headings=2.0 ends_asking=0.0 lines=140.7
```

## only-you-know-zh

```
== new (3 runs): 92.1% clean, 4.7 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 1/36, Structure 5/48, Formatting 0/6, Wording 3/33, Asking 7/57, Opinion 2/15, Continuity 0/45, The work 6/6, Listening 0/12, Thinking 0/12
   faults: C12 x1 T4 x1 T6 x2 T11 x1 T12 x1 L3 x3 A9 x2 A10 x1 A13 x2 A17 x2 O1 x2 W5 x3 W6 x3
== none (3 runs): 89.1% clean, 4.7 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 2/36, Structure 9/48, Formatting 0/6, Wording 3/33, Asking 10/57, Opinion 0/15, Continuity 3/45, The work 6/6, Listening 0/12, Thinking 0/12
   faults: C10 x1 C12 x1 T2 x3 T6 x3 T11 x3 L3 x3 A4 x1 A6 x1 A8 x1 A9 x3 A17 x3 A21 x1 K10 x3 W5 x3 W6 x3

Checks:
new: line_refs=0.0 negations_per_1k=8.3 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.3 headings=0.0 ends_asking=1.0 lines=20.3
none: line_refs=0.0 negations_per_1k=14.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.3 lines=8.0
```

## shape-en

```
== new (3 runs): 92.7% clean, 6.7 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 3/36, Structure 6/48, Formatting 0/6, Wording 4/33, Asking 2/57, Opinion 1/15, Continuity 5/45, The work 0/6, Listening 0/12, Thinking 1/12
   faults: C10 x1 C12 x2 T6 x1 T15 x3 T25 x2 L1 x1 L3 x1 L7 x2 A4 x1 A20 x1 O6 x1 K6 x1 K7 x1 K10 x3 Y2 x1
== none (3 runs): 88.1% clean, 7.3 of 18 credits
   red flags: none
   faults by deck: Honesty 2/33, Content 7/36, Structure 11/48, Formatting 0/6, Wording 3/33, Asking 2/57, Opinion 1/15, Continuity 6/45, The work 4/6, Listening 0/12, Thinking 0/12
   faults: H2 x2 C3 x1 C10 x2 C11 x1 C12 x3 T2 x1 T6 x3 T8 x3 T11 x1 T15 x1 T25 x2 L3 x3 A3 x1 A21 x1 O6 x1 K7 x1 K9 x2 K10 x3 W5 x2 W6 x2

Checks:
new: line_refs=0.0 negations_per_1k=2.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.7 headings=0.0 ends_asking=0.3 lines=32.7
none: line_refs=0.0 negations_per_1k=1.7 paragraph_only=0.0 anchors=0.0 drawings=0.7 tables=0.0 quotes=0.0 headings=1.0 ends_asking=0.3 lines=54.3
```

## session-zh

```
== new (3 runs): 78.9% clean, 12.3 of 18 credits
   red flags: K15 x2
   faults by deck: Honesty 2/33, Content 11/36, Structure 10/48, Formatting 2/6, Wording 5/33, Asking 18/57, Opinion 1/15, Continuity 12/45, The work 0/6, Listening 0/12, Thinking 3/12
   faults: H2 x2 C3 x1 C4 x3 C7 x1 C10 x2 C11 x1 C12 x3 T4 x3 T5 x1 T6 x3 T11 x2 T25 x1 M13 x2 L3 x3 L17 x2 A2 x3 A3 x1 A4 x1 A6 x1 A8 x1 A9 x3 A10 x2 A13 x3 A17 x2 A21 x1 O6 x1 K1 x2 K2 x3 K15 x2 K5 x1 K7 x1 K12 x1 K16 x1 K19 x1 Y4 x3
== none (3 runs): 83.8% clean, 10.3 of 18 credits
   red flags: none
   faults by deck: Honesty 2/33, Content 7/36, Structure 12/48, Formatting 0/6, Wording 4/33, Asking 9/57, Opinion 0/15, Continuity 8/45, The work 3/6, Listening 0/12, Thinking 4/12
   faults: H2 x1 H18 x1 C4 x1 C7 x2 C8 x1 C10 x1 C12 x2 T1 x1 T2 x3 T4 x3 T6 x3 T8 x2 L3 x3 L7 x1 A4 x2 A8 x1 A9 x2 A13 x3 A15 x1 K1 x3 K2 x3 K12 x1 K16 x1 W6 x3 Y2 x1 Y4 x3

Checks:
new: line_refs=0.0 negations_per_1k=7.7 paragraph_only=0.0 anchors=0.7 drawings=3.3 tables=0.7 quotes=2.7 headings=0.0 ends_asking=3.0 lines=106.0
none: line_refs=0.0 negations_per_1k=6.7 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=1.3 lines=46.3
```

## better-way-zh

```
== new (3 runs): 96.4% clean, 8.0 of 18 credits
   red flags: none
   faults by deck: Honesty 2/33, Content 3/36, Structure 3/48, Formatting 0/6, Wording 3/33, Asking 0/57, Opinion 0/15, Continuity 0/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: H8 x2 C12 x3 T5 x1 T11 x2 L3 x3
== none (3 runs): 97.7% clean, 6.0 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 2/36, Structure 1/48, Formatting 0/6, Wording 1/33, Asking 0/57, Opinion 3/15, Continuity 0/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C12 x2 T11 x1 L3 x1 O6 x3

Checks:
new: line_refs=0.0 negations_per_1k=4.3 paragraph_only=0.0 anchors=0.0 drawings=0.3 tables=0.3 quotes=1.0 headings=0.3 ends_asking=0.0 lines=32.3
none: line_refs=0.0 negations_per_1k=1.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=25.3
```

## vague-zh

```
== new (3 runs): 90.1% clean, 8.7 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 4/36, Structure 4/48, Formatting 0/6, Wording 2/33, Asking 7/57, Opinion 0/15, Continuity 4/45, The work 6/6, Listening 0/12, Thinking 3/12
   faults: C3 x1 C7 x1 C12 x2 T2 x1 T7 x2 T15 x1 L3 x2 A6 x2 A10 x2 A13 x1 A17 x2 K6 x1 K10 x3 W5 x3 W6 x3 Y2 x1 Y4 x2
== none (3 runs): 91.1% clean, 6.0 of 18 credits
   red flags: none
   faults by deck: Honesty 2/33, Content 3/36, Structure 6/48, Formatting 0/6, Wording 1/33, Asking 9/57, Opinion 1/15, Continuity 3/45, The work 0/6, Listening 0/12, Thinking 2/12
   faults: H1 x1 H18 x1 C12 x3 T6 x3 T7 x3 L3 x1 A4 x1 A8 x3 A10 x1 A13 x3 A18 x1 O4 x1 K10 x3 Y4 x2

Checks:
new: line_refs=0.0 negations_per_1k=11.4 paragraph_only=0.0 anchors=0.0 drawings=0.3 tables=0.7 quotes=0.3 headings=0.0 ends_asking=1.0 lines=33.7
none: line_refs=0.0 negations_per_1k=14.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=18.0
```

## conflict-zh

```
== new (3 runs): 92.7% clean, 4.7 of 18 credits
   red flags: none
   faults by deck: Honesty 3/33, Content 0/36, Structure 6/48, Formatting 0/6, Wording 3/33, Asking 3/57, Opinion 2/15, Continuity 0/45, The work 0/6, Listening 5/12, Thinking 0/12
   faults: H8 x3 T4 x1 T5 x3 T19 x2 L3 x3 A13 x3 O6 x2 E2 x3 E4 x2
== none (3 runs): 90.8% clean, 3.0 of 18 credits
   red flags: none
   faults by deck: Honesty 3/33, Content 3/36, Structure 16/48, Formatting 0/6, Wording 6/33, Asking 0/57, Opinion 0/15, Continuity 0/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: H8 x3 C12 x3 T1 x3 T2 x3 T3 x3 T4 x3 T5 x3 T11 x1 L3 x3 L4 x3

Checks:
new: line_refs=1.0 negations_per_1k=2.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.3 lines=10.3
none: line_refs=0.0 negations_per_1k=3.6 paragraph_only=1.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=1.0
```

## conflict-agent-zh

```
== new (3 runs): 91.7% clean, 6.3 of 18 credits
   red flags: none
   faults by deck: Honesty 1/33, Content 5/36, Structure 4/48, Formatting 0/6, Wording 2/33, Asking 9/57, Opinion 1/15, Continuity 0/45, The work 1/6, Listening 1/12, Thinking 1/12
   faults: H2 x1 C7 x1 C10 x1 C11 x1 C12 x2 T5 x1 T6 x2 T11 x1 L1 x1 L6 x1 A3 x1 A5 x1 A6 x3 A17 x3 A20 x1 O6 x1 W6 x1 E4 x1 Y2 x1
== none (3 runs): 95.4% clean, 5.7 of 18 credits
   red flags: none
   faults by deck: Honesty 3/33, Content 4/36, Structure 4/48, Formatting 0/6, Wording 1/33, Asking 1/57, Opinion 1/15, Continuity 0/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: H8 x3 C7 x1 C12 x3 T2 x1 T5 x1 T6 x1 T11 x1 L3 x1 A13 x1 O6 x1

Checks:
new: line_refs=0.0 negations_per_1k=7.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.3 headings=0.0 ends_asking=1.0 lines=19.0
none: line_refs=0.0 negations_per_1k=7.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=14.0
```
