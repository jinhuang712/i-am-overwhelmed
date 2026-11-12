# Eval 2026-11-12-13a35d4-vs-3dc2039-opus-5-5

- old: `13a35d4` (13a35d4)
- new: `HEAD` (3dc2039)
- model: claude-opus-5-5, effort medium, judge claude-haiku-5-5 x3 on rubric-yesno.md, claude-opus-5-5 on its 🔎 lines, x3 where it raises a red flag
- runs: {'done': 6, 'kept': 6}
- spent: $4.98 of $7.00

## Overall

score = quality x (1 - 0.5 x the share of replies with a red flag). Quality weighs the words of PHILOSOPHY.md by rank; a line that does not apply counts for nothing.

| | old | new |
|---|---|---|
| **score** | 63.9 | 69.9 |
| quality | 85.1 | 83.9 |
| replies with a red flag | 3/6 | 2/6 |
| Honest (8) | 78.5 | 78.7 |
| Simple (7) | 84.4 | 80.7 |
| Structured (6) | 85.7 | 79.8 |
| Asking (5) | 84.3 | 86.1 |
| Opinionated (4) | 100.0 | 97.4 |
| Focused, Standalone (5) | 84.5 | 86.2 |
| Predictable (1) | 88.9 | 94.4 |

## multi-turn-zh

```
== new (3 runs): 90.8% clean, 10.0 of 18 credits
   red flags: none
   faults by deck: Honesty 0/33, Content 9/36, Structure 8/48, Formatting 0/6, Wording 5/33, Asking 6/57, Opinion 0/15, Continuity 0/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C3 x1 C4 x2 C10 x3 C12 x3 T4 x3 T6 x2 T7 x1 T11 x2 L3 x3 L6 x1 L7 x1 A2 x2 A3 x2 A10 x1 A13 x1
== old (3 runs): 91.4% clean, 10.7 of 18 credits
   red flags: K15 x1
   faults by deck: Honesty 0/33, Content 8/36, Structure 5/48, Formatting 1/6, Wording 3/33, Asking 5/57, Opinion 0/15, Continuity 4/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C3 x1 C4 x2 C10 x2 C12 x3 T4 x1 T6 x1 T11 x3 M13 x1 L3 x3 A2 x1 A3 x2 A8 x2 K15 x1 K10 x2 K16 x1
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=9.2 paragraph_only=0.0 anchors=1.0 drawings=2.7 tables=1.0 quotes=3.0 headings=0.0 ends_asking=2.7 lines=70.3
old: line_refs=0.0 negations_per_1k=8.6 paragraph_only=0.0 anchors=0.7 drawings=2.7 tables=1.0 quotes=2.0 headings=0.0 ends_asking=3.0 lines=80.0
```

## long-discussion-zh

```
== new (3 runs): 82.5% clean, 11.7 of 18 credits
   red flags: K15 x2
   faults by deck: Honesty 1/33, Content 5/36, Structure 10/48, Formatting 1/6, Wording 8/33, Asking 9/57, Opinion 2/15, Continuity 17/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: H2 x1 C11 x2 C12 x3 T4 x2 T5 x2 T6 x2 T7 x3 T11 x1 M13 x1 L1 x3 L3 x3 L6 x1 L7 x1 A2 x3 A3 x1 A9 x1 A10 x1 A15 x1 A19 x1 A22 x1 O6 x2 K1 x3 K2 x2 K15 x2 K5 x1 K7 x1 K8 x1 K10 x2 K16 x2 K17 x2 K18 x1
== old (3 runs): 84.8% clean, 12.0 of 18 credits
   red flags: K15 x2
   faults by deck: Honesty 0/33, Content 6/36, Structure 8/48, Formatting 1/6, Wording 5/33, Asking 12/57, Opinion 0/15, Continuity 14/45, The work 0/6, Listening 0/12, Thinking 0/12
   faults: C3 x1 C4 x2 C12 x3 T4 x1 T5 x2 T6 x2 T7 x3 M13 x1 L3 x3 L5 x1 L7 x1 A2 x1 A3 x1 A4 x1 A5 x2 A9 x1 A15 x2 A19 x2 A22 x2 K1 x3 K2 x3 K15 x2 K7 x1 K10 x1 K16 x2 K18 x2
bar: failed, red flags in new: K15 x2; new is more than 2 points under old

Checks:
new: line_refs=0.0 negations_per_1k=9.6 paragraph_only=0.0 anchors=2.7 drawings=5.0 tables=4.0 quotes=4.3 headings=0.0 ends_asking=4.7 lines=164.3
old: line_refs=0.0 negations_per_1k=9.2 paragraph_only=0.0 anchors=2.0 drawings=5.0 tables=3.0 quotes=5.7 headings=0.0 ends_asking=5.3 lines=143.3
```
