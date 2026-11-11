# Eval 2026-11-11-94c87e5-vs-13a35d4-opus-5-5

- old: `94c87e5` (94c87e5)
- new: `HEAD` (13a35d4)
- model: claude-opus-5-5, effort medium, judge claude-haiku-5-5 x3 on rubric-yesno.md, claude-opus-5-5 on its 🔎 lines, x3 where it raises a red flag
- runs: {'done': 76}
- spent: $19.98 of $52.90

## fix-test-zh

```
== new (2 runs): 90.4% clean, 9.0 of 19 credits
   red flags: none
   faults by deck: Honesty 1/20, Content 0/18, Structure 7/42, Formatting 2/20, Wording 1/18, Asking 5/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 4/8
   faults: H2 x1 T5 x1 T6 x2 T15 x2 T18 x1 T19 x1 M7 x2 L3 x1 A3 x1 A10 x1 A13 x2 A17 x1 Y2 x2 Y4 x2
== old (2 runs): 88.9% clean, 10.0 of 19 credits
   red flags: none
   faults by deck: Honesty 2/20, Content 2/18, Structure 7/42, Formatting 2/20, Wording 1/18, Asking 5/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 4/8
   faults: H2 x2 C3 x1 C7 x1 T5 x1 T6 x2 T15 x2 T19 x2 M7 x2 L6 x1 A3 x1 A4 x1 A9 x1 A10 x1 A13 x1 Y2 x2 Y4 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=7.3 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=29.5
old: line_refs=0.0 negations_per_1k=5.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=31.5
```

## chat-en

```
== new (2 runs): 93.8% clean, 8.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 5/42, Formatting 0/20, Wording 1/18, Asking 3/34, Opinion 0/8, Continuity 2/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: C3 x1 C4 x1 T6 x1 T11 x1 T18 x1 T21 x2 L3 x1 A15 x1 A16 x1 A17 x1 K7 x2
== old (2 runs): 96.6% clean, 6.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 3/42, Formatting 0/20, Wording 1/18, Asking 2/34, Opinion 0/8, Continuity 1/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: T11 x1 T21 x2 L3 x1 A3 x1 A8 x1 K7 x1
bar: failed, new is more than 2 points under old

Checks:
new: line_refs=0.0 negations_per_1k=2.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=18.5
old: line_refs=0.0 negations_per_1k=2.9 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.5 quotes=0.5 headings=0.0 ends_asking=1.0 lines=22.5
```

## chat-zh

```
== new (2 runs): 92.3% clean, 9.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 3/18, Structure 4/42, Formatting 1/20, Wording 3/18, Asking 5/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: C3 x2 C4 x1 T15 x2 T21 x2 M6 x1 L3 x2 L7 x1 A3 x1 A14 x1 A16 x2 A17 x1
== old (2 runs): 92.8% clean, 8.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 5/42, Formatting 2/20, Wording 3/18, Asking 3/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: C3 x2 T4 x1 T15 x2 T21 x2 M6 x2 L3 x2 L6 x1 A3 x2 A17 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=18.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=23.0
old: line_refs=0.0 negations_per_1k=15.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=22.5
```

## multi-turn-zh

```
== new (2 runs): 90.9% clean, 12.5 of 19 credits
   red flags: K15 x1
   faults by deck: Honesty 0/20, Content 2/18, Structure 3/42, Formatting 4/20, Wording 2/18, Asking 7/34, Opinion 0/8, Continuity 1/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: C3 x1 C4 x1 T6 x1 T11 x2 M6 x2 M10 x2 L3 x2 A3 x2 A8 x2 A13 x1 A15 x1 A17 x1 K15 x1
== old (2 runs): 88.9% clean, 11.5 of 19 credits
   red flags: K15 x2
   faults by deck: Honesty 0/20, Content 2/18, Structure 9/42, Formatting 2/20, Wording 3/18, Asking 5/34, Opinion 0/8, Continuity 2/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: C4 x2 T3 x1 T5 x1 T6 x1 T7 x1 T11 x2 T13 x2 T18 x1 M6 x1 M10 x1 L3 x2 L7 x1 A2 x1 A3 x1 A16 x1 A17 x2 K15 x2
bar: failed, red flags in new: K15 x1

Checks:
new: line_refs=0.0 negations_per_1k=8.6 paragraph_only=0.0 anchors=0.5 drawings=2.5 tables=1.0 quotes=1.5 headings=0.0 ends_asking=3.0 lines=76.0
old: line_refs=0.0 negations_per_1k=10.7 paragraph_only=0.0 anchors=1.0 drawings=3.0 tables=1.5 quotes=2.5 headings=0.0 ends_asking=2.5 lines=85.5
```

## many-items-zh

```
== new (2 runs): 86.1% clean, 13.0 of 19 credits
   red flags: none
   faults by deck: Honesty 3/20, Content 3/18, Structure 10/42, Formatting 0/20, Wording 2/18, Asking 10/34, Opinion 0/8, Continuity 1/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: H8 x2 H16 x1 C4 x2 C5 x1 T4 x1 T5 x1 T6 x1 T7 x2 T8 x1 T9 x1 T15 x1 T18 x1 T19 x1 L3 x1 L4 x1 A3 x2 A4 x1 A8 x1 A10 x2 A13 x2 A17 x2 K6 x1
== old (2 runs): 86.1% clean, 13.5 of 19 credits
   red flags: H4 x1
   faults by deck: Honesty 3/20, Content 0/18, Structure 12/42, Formatting 2/20, Wording 2/18, Asking 7/34, Opinion 0/8, Continuity 3/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: H4 x1 H8 x2 T4 x2 T6 x1 T7 x2 T9 x1 T15 x1 T16 x1 T17 x2 T18 x2 M2 x1 M3 x1 L3 x1 L4 x1 A4 x1 A8 x1 A9 x1 A10 x1 A13 x2 A17 x1 K3 x2 K8 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=8.2 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=1.0 quotes=2.5 headings=0.0 ends_asking=3.0 lines=108.0
old: line_refs=0.0 negations_per_1k=10.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=2.0 quotes=1.5 headings=0.5 ends_asking=3.0 lines=102.5
```

## design-flaw-zh

```
== new (2 runs): 87.5% clean, 7.5 of 19 credits
   red flags: none
   faults by deck: Honesty 1/20, Content 1/18, Structure 7/42, Formatting 2/20, Wording 5/18, Asking 4/34, Opinion 0/8, Continuity 0/28, The work 4/4, Listening 0/8, Thinking 2/8
   faults: H2 x1 C3 x1 T4 x1 T5 x1 T6 x1 T7 x1 T16 x2 T21 x1 M10 x2 L1 x1 L3 x2 L7 x2 A10 x2 A17 x2 W5 x2 W6 x2 Y2 x2
== old (2 runs): 89.9% clean, 7.5 of 19 credits
   red flags: none
   faults by deck: Honesty 1/20, Content 0/18, Structure 7/42, Formatting 2/20, Wording 2/18, Asking 3/34, Opinion 0/8, Continuity 4/28, The work 2/4, Listening 0/8, Thinking 0/8
   faults: H2 x1 T2 x1 T4 x1 T5 x1 T6 x1 T16 x2 T21 x1 M10 x2 L3 x1 L7 x1 A10 x1 A13 x1 A17 x1 K10 x2 K11 x2 W6 x2
bar: failed, new is more than 2 points under old

Checks:
new: line_refs=0.0 negations_per_1k=17.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.5 quotes=0.0 headings=0.0 ends_asking=1.0 lines=21.5
old: line_refs=0.0 negations_per_1k=17.7 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.5 quotes=0.0 headings=0.0 ends_asking=1.0 lines=20.5
```

## long-discussion-zh

```
== new (2 runs): 83.7% clean, 13.0 of 19 credits
   red flags: none
   faults by deck: Honesty 2/20, Content 2/18, Structure 11/42, Formatting 4/20, Wording 3/18, Asking 6/34, Opinion 0/8, Continuity 6/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: H8 x2 C4 x2 T5 x1 T6 x2 T7 x2 T9 x1 T10 x1 T16 x2 T17 x1 T19 x1 M2 x1 M6 x1 M7 x1 M10 x1 L1 x1 L3 x2 A4 x1 A9 x1 A13 x2 A15 x1 A17 x1 K1 x2 K2 x2 K3 x1 K6 x1
== old (2 runs): 83.2% clean, 13.5 of 19 credits
   red flags: K15 x1
   faults by deck: Honesty 0/20, Content 2/18, Structure 13/42, Formatting 3/20, Wording 5/18, Asking 8/34, Opinion 0/8, Continuity 4/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: C4 x2 T2 x2 T5 x2 T6 x1 T7 x2 T12 x1 T13 x1 T16 x1 T18 x1 T21 x2 M6 x1 M10 x2 L1 x1 L3 x2 L5 x1 L6 x1 A2 x2 A3 x1 A9 x1 A13 x1 A14 x1 A17 x2 K1 x2 K3 x1 K15 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=9.2 paragraph_only=0.0 anchors=1.5 drawings=5.0 tables=2.5 quotes=5.5 headings=0.0 ends_asking=5.5 lines=143.5
old: line_refs=0.0 negations_per_1k=7.1 paragraph_only=0.0 anchors=2.5 drawings=5.0 tables=3.5 quotes=5.5 headings=0.0 ends_asking=5.5 lines=184.0
```

## shape-zh

```
== new (2 runs): 94.7% clean, 7.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 5/42, Formatting 0/20, Wording 3/18, Asking 0/34, Opinion 0/8, Continuity 1/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: C3 x1 C7 x1 T6 x2 T15 x2 T20 x1 L3 x2 L7 x1 K7 x1
== old (2 runs): 97.1% clean, 3.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 2/42, Formatting 0/20, Wording 2/18, Asking 0/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: C3 x1 C8 x1 T6 x1 T15 x1 L3 x1 L6 x1
bar: failed, new is more than 2 points under old

Checks:
new: line_refs=0.0 negations_per_1k=2.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=38.0
old: line_refs=0.0 negations_per_1k=1.5 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=0.5 headings=0.0 ends_asking=0.0 lines=21.5
```

## fact-zh

```
== new (2 runs): 97.1% clean, 1.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 3/18, Structure 2/42, Formatting 0/20, Wording 1/18, Asking 0/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: C3 x1 C4 x1 C8 x1 T5 x1 T19 x1 L7 x1
== old (2 runs): 97.6% clean, 3.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 1/18, Structure 2/42, Formatting 0/20, Wording 2/18, Asking 0/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: C3 x1 T15 x1 T21 x1 L3 x1 L7 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=9.4 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=10.5
old: line_refs=0.0 negations_per_1k=19.6 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=0.5 headings=0.0 ends_asking=0.0 lines=21.0
```

## your-step-zh

```
== new (2 runs): 85.6% clean, 8.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 19/42, Formatting 3/20, Wording 1/18, Asking 3/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 2/8
   faults: C3 x1 C4 x1 T5 x2 T6 x2 T8 x1 T9 x2 T10 x2 T11 x2 T13 x1 T14 x2 T18 x2 T19 x1 T21 x2 M6 x1 M7 x1 M10 x1 L7 x1 A13 x2 A17 x1 Y1 x2
== old (2 runs): 89.4% clean, 6.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 1/18, Structure 14/42, Formatting 3/20, Wording 2/18, Asking 2/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: C4 x1 T4 x1 T5 x2 T9 x1 T10 x1 T11 x2 T14 x2 T18 x2 T19 x1 T21 x2 M2 x1 M7 x1 M10 x1 L3 x1 L6 x1 A13 x1 A17 x1
bar: failed, new is more than 2 points under old

Checks:
new: line_refs=0.0 negations_per_1k=7.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.5 quotes=1.0 headings=0.0 ends_asking=0.0 lines=31.5
old: line_refs=0.0 negations_per_1k=10.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=30.0
```

## clear-step-zh

```
== new (2 runs): 96.6% clean, 6.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 4/42, Formatting 0/20, Wording 0/18, Asking 3/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: T6 x1 T17 x2 T18 x1 A3 x1 A4 x1 A13 x1
== old (2 runs): 94.7% clean, 7.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 7/42, Formatting 0/20, Wording 0/18, Asking 3/34, Opinion 0/8, Continuity 0/28, The work 1/4, Listening 0/8, Thinking 0/8
   faults: T4 x1 T6 x1 T11 x1 T12 x1 T13 x1 T16 x1 T17 x1 A3 x1 A10 x1 A17 x1 W6 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=8.2 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=15.0
old: line_refs=0.0 negations_per_1k=9.7 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=13.5
```

## detail-zh

```
== new (2 runs): 88.9% clean, 11.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 1/18, Structure 16/42, Formatting 0/20, Wording 5/18, Asking 0/34, Opinion 0/8, Continuity 1/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: C4 x1 T4 x2 T5 x1 T6 x1 T7 x1 T9 x1 T10 x1 T11 x2 T15 x1 T18 x2 T19 x2 T20 x1 T21 x1 L3 x2 L5 x1 L7 x2 K12 x1
== old (2 runs): 90.9% clean, 10.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 13/42, Formatting 0/20, Wording 4/18, Asking 0/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: C4 x2 T4 x2 T5 x2 T7 x1 T9 x1 T10 x1 T11 x2 T18 x2 T19 x2 L3 x2 L7 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=3.7 paragraph_only=0.0 anchors=0.0 drawings=2.0 tables=1.5 quotes=2.0 headings=1.0 ends_asking=0.0 lines=125.0
old: line_refs=0.0 negations_per_1k=3.5 paragraph_only=0.0 anchors=0.0 drawings=2.0 tables=2.0 quotes=1.5 headings=1.0 ends_asking=0.0 lines=100.0
```

## only-you-know-zh

```
== new (2 runs): 88.5% clean, 6.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 9/42, Formatting 1/20, Wording 2/18, Asking 5/34, Opinion 1/8, Continuity 0/28, The work 4/4, Listening 0/8, Thinking 2/8
   faults: T6 x2 T11 x1 T13 x1 T17 x2 T18 x1 T21 x2 M7 x1 L3 x2 A9 x2 A13 x2 A17 x1 O1 x1 W5 x2 W6 x2 Y4 x2
== old (2 runs): 91.3% clean, 5.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 5/42, Formatting 1/20, Wording 2/18, Asking 5/34, Opinion 1/8, Continuity 0/28, The work 4/4, Listening 0/8, Thinking 0/8
   faults: T2 x1 T6 x1 T11 x1 T13 x1 T21 x1 M7 x1 L3 x2 A9 x1 A13 x2 A17 x2 O1 x1 W5 x2 W6 x2
bar: failed, new is more than 2 points under old

Checks:
new: line_refs=0.0 negations_per_1k=5.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=22.5
old: line_refs=0.0 negations_per_1k=14.3 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=14.5
```

## shape-en

```
== new (2 runs): 93.3% clean, 7.0 of 19 credits
   red flags: H4 x1
   faults by deck: Honesty 1/20, Content 0/18, Structure 5/42, Formatting 0/20, Wording 3/18, Asking 0/34, Opinion 0/8, Continuity 2/28, The work 2/4, Listening 0/8, Thinking 1/8
   faults: H4 x1 T6 x1 T15 x2 T20 x2 L3 x1 L7 x2 K6 x1 K7 x1 W5 x1 W6 x1 Y2 x1
== old (2 runs): 92.3% clean, 7.0 of 19 credits
   red flags: H4 x1
   faults by deck: Honesty 1/20, Content 0/18, Structure 4/42, Formatting 1/20, Wording 4/18, Asking 2/34, Opinion 0/8, Continuity 1/28, The work 2/4, Listening 0/8, Thinking 1/8
   faults: H4 x1 T6 x1 T15 x2 T20 x1 M7 x1 L3 x2 L6 x1 L7 x1 A2 x1 A4 x1 K7 x1 W5 x1 W6 x1 Y2 x1
bar: failed, red flags in new: H4 x1

Checks:
new: line_refs=0.0 negations_per_1k=2.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=0.0 lines=32.5
old: line_refs=0.0 negations_per_1k=1.9 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=0.0 lines=29.0
```

## session-zh

```
== new (2 runs): 81.2% clean, 14.0 of 19 credits
   red flags: K15 x1
   faults by deck: Honesty 2/20, Content 2/18, Structure 12/42, Formatting 4/20, Wording 4/18, Asking 8/34, Opinion 0/8, Continuity 4/28, The work 0/4, Listening 0/8, Thinking 3/8
   faults: H2 x1 H7 x1 C3 x1 C4 x1 T4 x1 T6 x2 T11 x1 T13 x2 T16 x2 T18 x2 T21 x2 M2 x1 M7 x2 M10 x1 L3 x2 L5 x1 L7 x1 A2 x1 A8 x1 A9 x2 A10 x2 A13 x2 K1 x1 K2 x1 K3 x1 K15 x1 Y3 x1 Y4 x2
== old (2 runs): 82.2% clean, 14.0 of 19 credits
   red flags: none
   faults by deck: Honesty 2/20, Content 3/18, Structure 13/42, Formatting 3/20, Wording 3/18, Asking 6/34, Opinion 0/8, Continuity 6/28, The work 0/4, Listening 0/8, Thinking 1/8
   faults: H2 x2 C3 x1 C4 x2 T4 x1 T6 x2 T7 x1 T9 x1 T10 x1 T13 x2 T16 x2 T18 x2 T21 x1 M7 x1 M10 x2 L3 x1 L5 x1 L7 x1 A2 x1 A9 x2 A10 x1 A13 x1 A17 x1 K1 x2 K2 x2 K3 x1 K10 x1 Y4 x1
bar: failed, red flags in new: K15 x1

Checks:
new: line_refs=0.0 negations_per_1k=8.1 paragraph_only=0.0 anchors=0.5 drawings=3.0 tables=1.0 quotes=3.0 headings=0.0 ends_asking=3.5 lines=97.5
old: line_refs=0.0 negations_per_1k=9.4 paragraph_only=0.0 anchors=0.5 drawings=3.5 tables=1.0 quotes=1.5 headings=0.0 ends_asking=4.0 lines=120.0
```

## better-way-zh

```
== new (2 runs): 95.7% clean, 7.5 of 19 credits
   red flags: none
   faults by deck: Honesty 2/20, Content 0/18, Structure 3/42, Formatting 2/20, Wording 2/18, Asking 0/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: H8 x2 T5 x1 T18 x1 T21 x1 M6 x1 M7 x1 L3 x2
== old (2 runs): 97.1% clean, 7.0 of 19 credits
   red flags: none
   faults by deck: Honesty 2/20, Content 0/18, Structure 2/42, Formatting 2/20, Wording 0/18, Asking 0/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: H8 x2 T5 x1 T18 x1 M7 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=5.0 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.5 quotes=1.0 headings=0.0 ends_asking=0.0 lines=30.5
old: line_refs=0.0 negations_per_1k=3.4 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.5 quotes=0.5 headings=0.0 ends_asking=0.0 lines=27.0
```

## vague-zh

```
== new (2 runs): 90.4% clean, 10.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 6/42, Formatting 0/20, Wording 4/18, Asking 4/34, Opinion 0/8, Continuity 2/28, The work 4/4, Listening 0/8, Thinking 0/8
   faults: T15 x1 T16 x2 T17 x1 T18 x1 T21 x1 L2 x1 L3 x2 L6 x1 A8 x1 A10 x2 A13 x1 K10 x2 W5 x2 W6 x2
== old (2 runs): 87.0% clean, 10.0 of 19 credits
   red flags: none
   faults by deck: Honesty 2/20, Content 1/18, Structure 6/42, Formatting 1/20, Wording 2/18, Asking 8/34, Opinion 0/8, Continuity 2/28, The work 4/4, Listening 0/8, Thinking 1/8
   faults: H2 x2 C3 x1 T2 x1 T7 x1 T16 x2 T17 x1 T18 x1 M6 x1 L3 x1 L5 x1 A3 x1 A4 x1 A6 x1 A9 x1 A10 x1 A13 x2 A17 x1 K10 x2 W5 x2 W6 x2 Y4 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=15.1 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.5 quotes=0.5 headings=0.0 ends_asking=1.0 lines=38.0
old: line_refs=0.0 negations_per_1k=10.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=25.0
```

## conflict-zh

```
== new (2 runs): 93.3% clean, 4.0 of 19 credits
   red flags: none
   faults by deck: Honesty 2/20, Content 0/18, Structure 7/42, Formatting 0/20, Wording 2/18, Asking 3/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 0/8, Thinking 0/8
   faults: H8 x2 T5 x2 T17 x2 T19 x2 T21 x1 L3 x2 A4 x1 A13 x2
== old (2 runs): 90.9% clean, 7.0 of 19 credits
   red flags: none
   faults by deck: Honesty 1/20, Content 1/18, Structure 7/42, Formatting 0/20, Wording 4/18, Asking 3/34, Opinion 1/8, Continuity 1/28, The work 0/4, Listening 1/8, Thinking 0/8
   faults: H8 x1 C7 x1 T5 x2 T15 x1 T17 x2 T19 x1 T21 x1 L3 x2 L6 x2 A6 x1 A13 x1 A17 x1 O1 x1 K10 x1 E4 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=1.8 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=9.5
old: line_refs=0.0 negations_per_1k=5.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=19.5
```

## conflict-agent-zh

```
== new (2 runs): 91.8% clean, 9.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 1/18, Structure 6/42, Formatting 3/20, Wording 2/18, Asking 3/34, Opinion 0/8, Continuity 0/28, The work 0/4, Listening 1/8, Thinking 1/8
   faults: C7 x1 T6 x2 T11 x1 T13 x1 T17 x1 T18 x1 M2 x1 M3 x1 M7 x1 L3 x1 L6 x1 A13 x1 A17 x2 E4 x1 Y2 x1
== old (2 runs): 96.6% clean, 5.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 4/42, Formatting 0/20, Wording 0/18, Asking 1/34, Opinion 0/8, Continuity 0/28, The work 2/4, Listening 0/8, Thinking 0/8
   faults: T6 x1 T16 x1 T17 x1 T21 x1 A17 x1 W6 x2
bar: failed, new is more than 2 points under old

Checks:
new: line_refs=0.0 negations_per_1k=5.8 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=21.5
old: line_refs=0.0 negations_per_1k=11.1 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=16.0
```
