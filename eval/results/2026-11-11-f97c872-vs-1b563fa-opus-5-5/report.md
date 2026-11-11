# Eval 2026-11-11-f97c872-vs-1b563fa-opus-5-5

- old: `v0.1.14` (f97c872)
- new: `HEAD` (1b563fa)
- none: no plugin
- model: claude-opus-5-5, effort medium, judge claude-haiku-5-5 x3 on rubric-yesno.md, claude-opus-5-5 on its 🔎 lines
- runs: {'skipped': 114}
- spent: $32.41 of $68.90

## fix-test-zh

```
== new (2 runs): 95.0% clean, 10.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 1/18, Structure 6/42, Formatting 1/20, Wording 1/18, Asking 1/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 1/10
   faults: C7 x1 T5 x2 T6 x2 T15 x2 M7 x1 L3 x1 A8 x1 Y2 x1
== none (2 runs): 89.0% clean, 4.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 12/42, Formatting 2/20, Wording 1/18, Asking 1/34, Opinion 0/8, Continuity 0/26, The work 2/12, Listening 0/10, Thinking 4/10
   faults: C7 x1 C8 x1 T2 x1 T4 x2 T5 x1 T6 x2 T9 x2 T10 x2 T16 x2 M7 x2 L3 x1 A13 x1 W6 x2 Y2 x2 Y4 x2
== old (2 runs): 89.9% clean, 7.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 8/42, Formatting 2/20, Wording 3/18, Asking 3/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 4/10
   faults: C3 x1 C7 x1 T5 x1 T6 x2 T9 x1 T10 x1 T19 x2 T21 x1 M7 x1 M10 x1 L3 x1 L5 x1 L7 x1 A9 x1 A13 x2 Y2 x2 Y4 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=6.3 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=0.0 lines=27.0
none: line_refs=0.0 negations_per_1k=8.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.5 lines=6.5
old: line_refs=0.0 negations_per_1k=6.5 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=26.5
```

## chat-en

```
== new (2 runs): 94.0% clean, 7.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 1/18, Structure 5/42, Formatting 0/20, Wording 3/18, Asking 4/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: C3 x1 T6 x2 T11 x1 T20 x1 T21 x1 L5 x1 L7 x2 A8 x2 A15 x1 A17 x1
== none (2 runs): 92.7% clean, 4.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 12/42, Formatting 2/20, Wording 2/18, Asking 0/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T6 x2 T9 x2 T10 x2 T11 x2 T13 x2 T18 x2 M6 x2 L3 x2
== old (2 runs): 95.0% clean, 6.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 5/42, Formatting 0/20, Wording 2/18, Asking 2/34, Opinion 0/8, Continuity 2/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T5 x1 T6 x2 T9 x1 T19 x1 L3 x2 A15 x1 A17 x1 K7 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=1.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.5 quotes=1.0 headings=0.0 ends_asking=0.0 lines=20.0
none: line_refs=0.0 negations_per_1k=4.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=14.0
old: line_refs=0.0 negations_per_1k=2.5 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=19.0
```

## chat-zh

```
== new (2 runs): 95.0% clean, 7.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 1/18, Structure 2/42, Formatting 0/20, Wording 5/18, Asking 3/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: C3 x1 T19 x1 T21 x1 L1 x2 L3 x2 L5 x1 A3 x2 A17 x1
== none (2 runs): 95.9% clean, 6.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 6/42, Formatting 0/20, Wording 3/18, Asking 0/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T2 x2 T9 x2 T10 x2 L1 x1 L3 x2
== old (2 runs): 95.4% clean, 9.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 1/18, Structure 0/42, Formatting 1/20, Wording 3/18, Asking 5/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: C7 x1 M6 x1 L1 x2 L3 x1 A3 x1 A8 x2 A13 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=15.8 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=19.0
none: line_refs=0.0 negations_per_1k=7.1 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=15.5
old: line_refs=0.0 negations_per_1k=12.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=22.5
```

## multi-turn-zh

```
== new (2 runs): 90.4% clean, 11.0 of 19 credits
   red flags: A7 x1
   faults by deck: Honesty 1/20, Content 2/18, Structure 7/42, Formatting 2/20, Wording 3/18, Asking 3/34, Opinion 0/8, Continuity 3/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: H2 x1 C4 x2 T6 x2 T7 x1 T11 x2 T13 x2 M10 x2 L3 x1 L7 x2 A3 x1 A7 x1 A13 x1 K1 x1 K2 x1 K3 x1
== none (2 runs): 84.4% clean, 8.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 20/42, Formatting 2/20, Wording 3/18, Asking 0/34, Opinion 0/8, Continuity 7/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: C4 x2 T2 x1 T3 x1 T4 x2 T5 x2 T6 x2 T8 x1 T9 x1 T10 x2 T11 x2 T13 x2 T17 x2 T18 x2 M6 x2 L3 x2 L7 x1 K1 x2 K2 x2 K3 x2 K10 x1
== old (2 runs): 86.2% clean, 10.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 4/18, Structure 7/42, Formatting 3/20, Wording 4/18, Asking 10/34, Opinion 0/8, Continuity 2/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: C3 x2 C4 x2 T4 x1 T6 x2 T11 x1 T17 x1 T18 x2 M6 x1 M10 x2 L1 x1 L3 x2 L7 x1 A2 x2 A3 x2 A8 x2 A14 x1 A15 x2 A17 x1 K3 x1 K14 x1
bar: failed, red flags in new: A7 x1

Checks:
new: line_refs=0.0 negations_per_1k=9.4 paragraph_only=0.0 anchors=0.0 drawings=2.0 tables=1.5 quotes=3.0 headings=0.0 ends_asking=1.5 lines=63.0
none: line_refs=0.0 negations_per_1k=7.4 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.5 quotes=0.0 headings=1.5 ends_asking=0.0 lines=62.5
old: line_refs=0.0 negations_per_1k=5.5 paragraph_only=0.0 anchors=0.5 drawings=3.0 tables=1.0 quotes=2.5 headings=0.0 ends_asking=3.0 lines=67.0
```

## many-items-zh

```
== new (2 runs): 87.2% clean, 14.0 of 19 credits
   red flags: H4 x1, W3 x1
   faults by deck: Honesty 1/20, Content 0/18, Structure 14/42, Formatting 1/20, Wording 2/18, Asking 8/34, Opinion 0/8, Continuity 0/26, The work 1/12, Listening 1/10, Thinking 0/10
   faults: H4 x1 T4 x2 T6 x1 T7 x2 T9 x1 T10 x1 T15 x1 T16 x2 T17 x2 T18 x1 T21 x1 M10 x1 L3 x2 A3 x1 A4 x1 A6 x1 A8 x2 A13 x2 A17 x1 W3 x1 E4 x1
== none (2 runs): 78.9% clean, 8.0 of 19 credits
   red flags: none
   faults by deck: Honesty 1/20, Content 0/18, Structure 15/42, Formatting 7/20, Wording 2/18, Asking 2/34, Opinion 2/8, Continuity 9/26, The work 3/12, Listening 1/10, Thinking 4/10
   faults: H2 x1 T4 x2 T6 x2 T7 x2 T8 x2 T10 x2 T16 x2 T17 x1 T18 x2 M2 x1 M6 x2 M7 x2 M8 x2 L3 x2 A13 x2 O1 x1 O4 x1 K1 x1 K3 x1 K5 x2 K10 x2 K11 x2 K12 x1 W4 x1 W6 x2 E4 x1 Y4 x2 Y5 x2
== old (2 runs): 87.6% clean, 14.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 13/42, Formatting 1/20, Wording 2/18, Asking 9/34, Opinion 1/8, Continuity 1/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T2 x1 T4 x1 T5 x1 T6 x2 T9 x2 T15 x1 T16 x1 T18 x2 T19 x1 T21 x1 M10 x1 L5 x1 L7 x1 A8 x2 A10 x2 A13 x1 A14 x1 A15 x1 A17 x2 O4 x1 K11 x1
bar: failed, red flags in new: H4 x1, W3 x1

Checks:
new: line_refs=0.0 negations_per_1k=9.7 paragraph_only=0.0 anchors=0.5 drawings=1.0 tables=2.0 quotes=2.5 headings=0.0 ends_asking=3.0 lines=87.0
none: line_refs=8.5 negations_per_1k=16.8 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=1.0 ends_asking=0.0 lines=49.5
old: line_refs=0.0 negations_per_1k=9.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=1.0 headings=0.0 ends_asking=3.0 lines=102.5
```

## design-flaw-zh

```
== new (2 runs): 94.5% clean, 10.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 4/42, Formatting 0/20, Wording 4/18, Asking 4/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T5 x1 T6 x1 T16 x2 L3 x2 L7 x2 A10 x2 A17 x2
== none (2 runs): 89.9% clean, 6.5 of 19 credits
   red flags: none
   faults by deck: Honesty 1/20, Content 1/18, Structure 8/42, Formatting 4/20, Wording 2/18, Asking 2/34, Opinion 0/8, Continuity 0/26, The work 2/12, Listening 0/10, Thinking 2/10
   faults: H2 x1 C7 x1 T4 x1 T6 x1 T9 x1 T10 x1 T11 x1 T16 x2 T18 x1 M2 x1 M6 x1 M7 x2 L3 x1 L7 x1 A10 x1 A16 x1 W6 x2 Y4 x2
== old (2 runs): 90.8% clean, 10.0 of 19 credits
   red flags: none
   faults by deck: Honesty 1/20, Content 0/18, Structure 3/42, Formatting 4/20, Wording 4/18, Asking 4/34, Opinion 1/8, Continuity 0/26, The work 1/12, Listening 0/10, Thinking 2/10
   faults: H2 x1 T5 x1 T6 x1 T21 x1 M7 x2 M10 x2 L3 x2 L5 x1 L7 x1 A3 x1 A10 x1 A13 x1 A17 x1 O1 x1 W1 x1 Y4 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=18.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=25.5
none: line_refs=0.0 negations_per_1k=14.8 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=17.5
old: line_refs=0.0 negations_per_1k=15.4 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=24.5
```

## long-discussion-zh

```
== new (2 runs): 81.7% clean, 12.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 14/42, Formatting 3/20, Wording 5/18, Asking 9/34, Opinion 1/8, Continuity 8/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T5 x1 T6 x1 T7 x2 T9 x1 T10 x1 T13 x2 T15 x1 T16 x1 T17 x2 T18 x2 M4 x1 M6 x1 M10 x1 L3 x2 L5 x1 L7 x2 A2 x1 A3 x1 A8 x1 A9 x2 A10 x1 A13 x1 A15 x1 A17 x1 O1 x1 K1 x2 K2 x2 K3 x1 K7 x1 K8 x2
== none (2 runs): 78.4% clean, 9.0 of 19 credits
   red flags: A7 x1
   faults by deck: Honesty 2/20, Content 1/18, Structure 24/42, Formatting 4/20, Wording 4/18, Asking 4/34, Opinion 0/8, Continuity 8/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: H2 x2 C8 x1 T2 x2 T3 x2 T4 x1 T5 x1 T6 x2 T7 x1 T8 x2 T9 x1 T10 x2 T11 x2 T13 x2 T15 x1 T16 x2 T17 x1 T18 x2 M4 x1 M6 x2 M7 x1 L3 x2 L4 x1 L8 x1 A7 x1 A8 x1 A15 x1 A17 x1 K1 x2 K2 x2 K3 x2 K7 x1 K10 x1
== old (2 runs): 81.7% clean, 13.0 of 19 credits
   red flags: A7 x1
   faults by deck: Honesty 0/20, Content 2/18, Structure 9/42, Formatting 3/20, Wording 6/18, Asking 11/34, Opinion 0/8, Continuity 9/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: C3 x1 C4 x1 T2 x1 T5 x1 T6 x2 T7 x1 T16 x2 T17 x2 M6 x2 M10 x1 L3 x2 L5 x2 L7 x2 A2 x2 A3 x2 A6 x1 A7 x1 A8 x1 A9 x1 A10 x1 A13 x1 A17 x1 K1 x2 K2 x2 K3 x1 K14 x2 K8 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=7.8 paragraph_only=0.0 anchors=3.0 drawings=4.0 tables=4.0 quotes=3.5 headings=0.0 ends_asking=5.5 lines=152.5
none: line_refs=0.0 negations_per_1k=6.9 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=2.0 quotes=0.0 headings=5.5 ends_asking=0.0 lines=130.5
old: line_refs=0.0 negations_per_1k=6.2 paragraph_only=0.0 anchors=3.0 drawings=4.5 tables=4.0 quotes=4.0 headings=0.0 ends_asking=5.5 lines=132.0
```

## shape-zh

```
== new (2 runs): 97.2% clean, 5.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 4/42, Formatting 0/20, Wording 2/18, Asking 0/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T6 x2 T15 x2 L6 x1 L7 x1
== none (2 runs): 89.4% clean, 5.5 of 19 credits
   red flags: none
   faults by deck: Honesty 1/20, Content 1/18, Structure 13/42, Formatting 0/20, Wording 3/18, Asking 2/34, Opinion 0/8, Continuity 3/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: H2 x1 C3 x1 T5 x1 T6 x2 T8 x2 T10 x2 T13 x1 T15 x2 T18 x1 T21 x2 L3 x2 L6 x1 A2 x1 A5 x1 K6 x1 K7 x1 K9 x1
== old (2 runs): 92.2% clean, 6.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 6/42, Formatting 0/20, Wording 2/18, Asking 7/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: C3 x1 C7 x1 T6 x2 T15 x2 T18 x1 T20 x1 L3 x1 L6 x1 A2 x2 A3 x1 A4 x2 A6 x1 A13 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=2.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=32.5
none: line_refs=0.0 negations_per_1k=2.8 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=1.0 ends_asking=0.0 lines=49.5
old: line_refs=0.0 negations_per_1k=2.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=33.0
```

## fact-zh

```
== new (2 runs): 95.4% clean, 3.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 4/42, Formatting 0/20, Wording 4/18, Asking 0/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: C3 x1 C4 x1 T5 x2 T6 x2 L5 x1 L7 x2 L8 x1
== none (2 runs): 96.8% clean, 1.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 1/18, Structure 4/42, Formatting 0/20, Wording 2/18, Asking 0/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: C3 x1 T5 x1 T7 x1 T9 x1 T10 x1 L3 x1 L6 x1
== old (2 runs): 95.0% clean, 4.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 3/18, Structure 3/42, Formatting 1/20, Wording 2/18, Asking 2/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: C3 x2 C7 x1 T5 x1 T6 x1 T15 x1 M10 x1 L6 x1 L7 x1 A2 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=19.8 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=14.0
none: line_refs=0.0 negations_per_1k=19.7 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.5 quotes=0.0 headings=0.0 ends_asking=0.0 lines=11.5
old: line_refs=0.0 negations_per_1k=14.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.5 quotes=0.0 headings=0.0 ends_asking=0.5 lines=20.0
```

## your-step-zh

```
== new (2 runs): 96.3% clean, 7.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 1/18, Structure 4/42, Formatting 0/20, Wording 1/18, Asking 0/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 2/10
   faults: C3 x1 T11 x1 T14 x1 T18 x2 L1 x1 Y1 x2
== none (2 runs): 95.0% clean, 3.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 1/18, Structure 6/42, Formatting 2/20, Wording 0/18, Asking 0/34, Opinion 0/8, Continuity 1/26, The work 0/12, Listening 0/10, Thinking 1/10
   faults: C8 x1 T1 x1 T2 x1 T6 x1 T9 x1 T11 x1 T18 x1 M1 x1 M7 x1 K7 x1 Y1 x1
== old (2 runs): 92.2% clean, 8.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 8/42, Formatting 4/20, Wording 2/18, Asking 0/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 1/10
   faults: C3 x2 T5 x1 T11 x2 T14 x2 T18 x2 T21 x1 M1 x1 M7 x1 M10 x2 L3 x1 L5 x1 Y1 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=11.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=26.0
none: line_refs=0.0 negations_per_1k=3.7 paragraph_only=0.5 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=9.5
old: line_refs=0.0 negations_per_1k=5.6 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=22.0
```

## clear-step-zh

```
== new (2 runs): 98.2% clean, 6.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 1/42, Formatting 1/20, Wording 0/18, Asking 2/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T17 x1 M10 x1 A3 x2
== none (2 runs): 95.9% clean, 3.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 2/42, Formatting 4/20, Wording 1/18, Asking 2/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T17 x2 M7 x2 M8 x2 L1 x1 A3 x2
== old (2 runs): 97.7% clean, 5.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 2/42, Formatting 0/20, Wording 1/18, Asking 2/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T4 x1 T17 x1 L5 x1 A3 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=7.2 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=15.5
none: line_refs=1.0 negations_per_1k=11.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=12.0
old: line_refs=0.0 negations_per_1k=4.1 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=13.0
```

## detail-zh

```
== new (2 runs): 89.0% clean, 9.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 5/18, Structure 12/42, Formatting 1/20, Wording 6/18, Asking 0/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: C3 x1 C4 x2 C7 x1 C8 x1 T1 x1 T4 x2 T6 x2 T18 x2 T19 x2 T20 x1 T21 x2 M10 x1 L3 x2 L5 x1 L6 x1 L7 x2
== none (2 runs): 84.4% clean, 8.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 24/42, Formatting 0/20, Wording 7/18, Asking 0/34, Opinion 0/8, Continuity 1/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: C4 x2 T2 x2 T4 x2 T5 x1 T6 x2 T7 x2 T8 x2 T10 x2 T11 x2 T13 x2 T15 x1 T18 x2 T19 x2 T21 x2 L3 x2 L4 x2 L6 x1 L7 x2 K9 x1
== old (2 runs): 86.7% clean, 9.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 1/18, Structure 10/42, Formatting 2/20, Wording 6/18, Asking 6/34, Opinion 0/8, Continuity 4/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: C3 x1 T4 x1 T5 x1 T15 x1 T18 x2 T19 x2 T20 x2 T21 x1 M10 x2 L3 x2 L6 x2 L7 x2 A2 x1 A3 x2 A4 x2 A17 x1 K7 x1 K8 x1 K9 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=3.1 paragraph_only=0.5 anchors=0.0 drawings=1.5 tables=1.0 quotes=1.5 headings=1.0 ends_asking=0.0 lines=86.0
none: line_refs=0.0 negations_per_1k=4.5 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=0.5 headings=2.0 ends_asking=0.0 lines=140.5
old: line_refs=0.0 negations_per_1k=2.6 paragraph_only=0.0 anchors=0.0 drawings=2.0 tables=1.0 quotes=1.0 headings=1.0 ends_asking=2.0 lines=105.0
```

## only-you-know-zh

```
== new (2 runs): 95.0% clean, 5.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 4/42, Formatting 0/20, Wording 2/18, Asking 4/34, Opinion 1/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T5 x1 T13 x1 T21 x2 L3 x2 A13 x2 A17 x2 O1 x1
== none (2 runs): 89.0% clean, 5.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 5/42, Formatting 8/20, Wording 3/18, Asking 8/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T2 x2 T6 x2 T11 x1 M2 x2 M4 x2 M6 x2 M7 x2 L3 x2 L5 x1 A6 x1 A9 x2 A10 x1 A16 x2 A17 x2
== old (2 runs): 92.7% clean, 6.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 6/42, Formatting 1/20, Wording 2/18, Asking 7/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T5 x1 T11 x1 T13 x1 T17 x1 T21 x2 M7 x1 L3 x2 A8 x1 A9 x2 A15 x2 A17 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=7.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=16.5
none: line_refs=0.0 negations_per_1k=15.3 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=9.5
old: line_refs=0.0 negations_per_1k=8.3 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=22.0
```

## shape-en

```
== new (2 runs): 95.4% clean, 7.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 4/42, Formatting 1/20, Wording 2/18, Asking 1/34, Opinion 0/8, Continuity 2/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T6 x2 T15 x2 M10 x1 L6 x1 L7 x1 A5 x1 K7 x2
== none (2 runs): 91.3% clean, 5.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 9/42, Formatting 0/20, Wording 4/18, Asking 0/34, Opinion 0/8, Continuity 6/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T2 x1 T8 x2 T9 x1 T10 x2 T15 x1 T18 x2 L3 x2 L6 x2 K7 x2 K9 x2 K10 x1 K11 x1
== old (2 runs): 91.3% clean, 6.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 6/42, Formatting 1/20, Wording 2/18, Asking 6/34, Opinion 0/8, Continuity 4/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T6 x2 T15 x2 T20 x1 T21 x1 M10 x1 L3 x1 L6 x1 A2 x2 A3 x1 A4 x2 A6 x1 K6 x1 K9 x1 K10 x1 K11 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=1.6 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=30.0
none: line_refs=0.0 negations_per_1k=2.0 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=0.0 headings=1.0 ends_asking=0.0 lines=52.5
old: line_refs=0.0 negations_per_1k=1.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=29.0
```

## session-zh

```
== new (2 runs): 83.0% clean, 13.5 of 19 credits
   red flags: none
   faults by deck: Honesty 2/20, Content 1/18, Structure 10/42, Formatting 5/20, Wording 6/18, Asking 6/34, Opinion 0/8, Continuity 5/26, The work 0/12, Listening 0/10, Thinking 2/10
   faults: H2 x2 C4 x1 T4 x1 T6 x2 T13 x1 T16 x2 T18 x2 T21 x2 M4 x1 M7 x2 M10 x2 L1 x1 L3 x2 L5 x1 L7 x2 A3 x1 A9 x2 A10 x1 A13 x1 A17 x1 K1 x2 K2 x2 K3 x1 Y2 x1 Y4 x1
== none (2 runs): 78.9% clean, 9.5 of 19 credits
   red flags: none
   faults by deck: Honesty 1/20, Content 3/18, Structure 19/42, Formatting 2/20, Wording 5/18, Asking 5/34, Opinion 0/8, Continuity 6/26, The work 2/12, Listening 0/10, Thinking 3/10
   faults: H2 x1 C4 x1 C7 x2 T2 x2 T4 x2 T5 x2 T6 x2 T9 x2 T10 x2 T11 x2 T13 x1 T16 x2 T18 x2 M7 x2 L3 x2 L4 x2 L7 x1 A3 x1 A8 x1 A10 x1 A13 x2 K1 x2 K2 x2 K3 x2 W6 x2 Y2 x2 Y4 x1
== old (2 runs): 79.4% clean, 14.0 of 19 credits
   red flags: none
   faults by deck: Honesty 1/20, Content 2/18, Structure 17/42, Formatting 4/20, Wording 6/18, Asking 10/34, Opinion 0/8, Continuity 5/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: H2 x1 C4 x1 C7 x1 T2 x1 T4 x2 T5 x1 T6 x2 T8 x1 T9 x2 T10 x2 T13 x1 T16 x2 T18 x2 T21 x1 M7 x2 M10 x2 L3 x2 L4 x1 L5 x1 L6 x1 L7 x1 A2 x2 A3 x1 A6 x2 A8 x1 A9 x2 A13 x1 A17 x1 K1 x2 K2 x1 K14 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=8.5 paragraph_only=0.0 anchors=0.5 drawings=2.5 tables=1.0 quotes=3.5 headings=0.0 ends_asking=2.5 lines=92.0
none: line_refs=0.0 negations_per_1k=7.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.5 lines=43.5
old: line_refs=0.0 negations_per_1k=7.2 paragraph_only=0.0 anchors=1.0 drawings=3.5 tables=1.0 quotes=0.5 headings=0.5 ends_asking=4.0 lines=102.0
```

## better-way-zh

```
== new (2 runs): 95.0% clean, 6.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 5/42, Formatting 1/20, Wording 1/18, Asking 0/34, Opinion 0/8, Continuity 0/26, The work 3/12, Listening 0/10, Thinking 1/10
   faults: T5 x2 T13 x2 T21 x1 M6 x1 L3 x1 W2 x2 W4 x1 Y2 x1
== none (2 runs): 95.4% clean, 5.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 1/42, Formatting 1/20, Wording 3/18, Asking 1/34, Opinion 0/8, Continuity 1/26, The work 1/12, Listening 0/10, Thinking 0/10
   faults: C2 x1 C7 x1 T18 x1 M6 x1 L1 x1 L3 x2 A14 x1 K6 x1 W2 x1
== old (2 runs): 95.0% clean, 7.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 2/18, Structure 3/42, Formatting 0/20, Wording 2/18, Asking 1/34, Opinion 0/8, Continuity 0/26, The work 1/12, Listening 1/10, Thinking 1/10
   faults: C3 x2 T5 x1 T18 x1 T21 x1 L3 x2 A3 x1 W2 x1 E4 x1 Y2 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=5.7 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=28.0
none: line_refs=0.0 negations_per_1k=5.6 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=23.0
old: line_refs=0.0 negations_per_1k=5.3 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=25.5
```

## vague-zh

```
== new (2 runs): 93.6% clean, 10.0 of 19 credits
   red flags: A7 x1
   faults by deck: Honesty 1/20, Content 0/18, Structure 3/42, Formatting 0/20, Wording 1/18, Asking 8/34, Opinion 0/8, Continuity 1/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: H2 x1 T6 x1 T7 x1 T15 x1 L3 x1 A3 x1 A6 x1 A7 x1 A8 x1 A10 x2 A13 x2 K10 x1
== none (2 runs): 90.8% clean, 7.0 of 19 credits
   red flags: H4 x2
   faults by deck: Honesty 2/20, Content 0/18, Structure 9/42, Formatting 3/20, Wording 0/18, Asking 3/34, Opinion 0/8, Continuity 0/26, The work 1/12, Listening 0/10, Thinking 2/10
   faults: H4 x2 T6 x2 T7 x1 T9 x1 T10 x1 T16 x2 T18 x2 M4 x1 M7 x2 A8 x2 A17 x1 W4 x1 Y4 x2
== old (2 runs): 89.9% clean, 11.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 8/42, Formatting 1/20, Wording 2/18, Asking 8/34, Opinion 0/8, Continuity 2/26, The work 0/12, Listening 0/10, Thinking 1/10
   faults: T7 x2 T16 x2 T17 x1 T18 x2 T21 x1 M10 x1 L1 x1 L3 x1 A6 x2 A8 x1 A10 x2 A15 x1 A17 x2 K14 x1 K10 x1 Y2 x1
bar: failed, red flags in new: A7 x1

Checks:
new: line_refs=0.0 negations_per_1k=15.4 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.5 quotes=1.0 headings=0.0 ends_asking=1.0 lines=33.0
none: line_refs=0.0 negations_per_1k=17.8 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.5 quotes=0.0 headings=0.0 ends_asking=0.0 lines=15.5
old: line_refs=0.0 negations_per_1k=13.8 paragraph_only=0.0 anchors=0.5 drawings=0.5 tables=1.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=34.5
```

## conflict-zh

```
== new (2 runs): 94.0% clean, 2.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 1/18, Structure 6/42, Formatting 0/20, Wording 1/18, Asking 3/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 2/10, Thinking 0/10
   faults: C9 x1 T4 x1 T5 x1 T9 x1 T17 x2 T19 x1 L3 x1 A6 x1 A10 x1 A17 x1 E4 x2
== none (2 runs): 92.7% clean, 3.5 of 19 credits
   red flags: none
   faults by deck: Honesty 2/20, Content 0/18, Structure 10/42, Formatting 0/20, Wording 4/18, Asking 0/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: H8 x2 T1 x2 T2 x2 T3 x2 T4 x2 T5 x2 L3 x2 L4 x2
== old (2 runs): 91.3% clean, 4.0 of 19 credits
   red flags: none
   faults by deck: Honesty 2/20, Content 0/18, Structure 9/42, Formatting 3/20, Wording 2/18, Asking 1/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 2/10, Thinking 0/10
   faults: H8 x2 T4 x2 T5 x2 T15 x2 T19 x2 T21 x1 M2 x1 M3 x2 L3 x2 A13 x1 E2 x2
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=9.0 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=8.5
none: line_refs=0.0 negations_per_1k=5.8 paragraph_only=1.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=1.0
old: line_refs=0.0 negations_per_1k=0.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=13.5
```

## conflict-agent-zh

```
== new (2 runs): 96.8% clean, 4.5 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 3/42, Formatting 1/20, Wording 1/18, Asking 2/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T5 x1 T16 x1 T18 x1 M7 x1 L3 x1 A17 x2
== none (2 runs): 92.2% clean, 6.0 of 19 credits
   red flags: none
   faults by deck: Honesty 0/20, Content 0/18, Structure 10/42, Formatting 2/20, Wording 3/18, Asking 2/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: T5 x1 T6 x2 T15 x2 T16 x2 T17 x1 T18 x2 M7 x2 L1 x1 L3 x1 L6 x1 A13 x2
== old (2 runs): 92.7% clean, 7.0 of 19 credits
   red flags: none
   faults by deck: Honesty 1/20, Content 2/18, Structure 7/42, Formatting 2/20, Wording 0/18, Asking 4/34, Opinion 0/8, Continuity 0/26, The work 0/12, Listening 0/10, Thinking 0/10
   faults: H8 x1 C7 x2 T4 x1 T6 x2 T11 x1 T15 x1 T18 x2 M7 x1 M10 x1 A3 x2 A4 x1 A13 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=7.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=17.5
none: line_refs=0.0 negations_per_1k=11.3 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=17.0
old: line_refs=0.0 negations_per_1k=3.3 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.5 lines=15.0
```
