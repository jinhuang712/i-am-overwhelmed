# Eval 2026-11-18-9b24f7c-vs-796ebf8-sonnet-5-5

- old: `v0.1.18` (9b24f7c)
- new: `HEAD` (796ebf8)
- none: no plugin
- model: claude-sonnet-5-5, effort xhigh, judge claude-haiku-5-5 x3 on rubric-yesno.md, claude-opus-5-5 on its 🔎 lines, x3 where it raises a red flag
- runs: {'done': 2, 'kept': 1}
- spent: $3.46 of $5.50

## Overall

score = quality x (1 - 0.5 x the share of replies with a red flag). Quality weighs the words of PHILOSOPHY.md by rank; a line that does not apply counts for nothing.

| | old | new | none |
|---|---|---|---|
| **score** | 88.4 | 41.7 | 76.9 |
| quality | 88.4 | 83.4 | 76.9 |
| replies with a red flag | 0/1 | 1/1 | 0/1 |
| Honest (8) | 92.9 | 92.3 | 84.6 |
| Simple (7) | 91.7 | 82.6 | 82.6 |
| Structured (6) | 81.2 | 73.3 | 58.3 |
| Asking (5) | 88.9 | 88.9 | 66.7 |
| Opinionated (4) | 92.9 | 85.7 | 92.9 |
| Focused, Standalone (5) | 78.6 | 71.4 | 71.4 |
| Predictable (1) | 100.0 | 100.0 | 100.0 |

## Old against new

- gap in quality, new minus old: -5.0 points, 90% interval -5.0 to -5.0: new is lower
- tasks: 0 up, 1 down, 0 equal, of 1
- down: session-zh

No line's count differs by 3 replies or more.

## session-zh

```
== new (1 runs): 81.8% clean, 14.0 of 18 credits
   red flags: H3 x1
   faults by deck: Honesty 2/11, Content 2/12, Structure 4/16, Formatting 0/1, Wording 2/11, Asking 2/19, Opinion 0/6, Continuity 4/13, The work 0/2, Listening 0/4, Thinking 2/4
   faults: H2 x1 H3 x1 C11 x1 C13 x1 T4 x1 T6 x1 T7 x1 T26 x1 L6 x1 L7 x1 A3 x1 A13 x1 K1 x1 K7 x1 K12 x1 K16 x1 Y2 x1 Y4 x1
== none (1 runs): 77.8% clean, 12.0 of 18 credits
   red flags: none
   faults by deck: Honesty 1/11, Content 2/12, Structure 5/16, Formatting 0/1, Wording 2/11, Asking 6/19, Opinion 0/6, Continuity 4/13, The work 1/2, Listening 0/4, Thinking 1/4
   faults: H2 x1 C4 x1 C10 x1 T2 x1 T4 x1 T5 x1 T6 x1 T11 x1 L4 x1 L7 x1 A3 x1 A4 x1 A13 x1 A15 x1 A20 x1 A22 x1 K1 x1 K12 x1 K16 x1 K19 x1 W6 x1 Y4 x1
== old (1 runs): 87.9% clean, 16.0 of 18 credits
   red flags: none
   faults by deck: Honesty 1/11, Content 2/12, Structure 3/16, Formatting 0/1, Wording 0/11, Asking 2/19, Opinion 0/6, Continuity 3/13, The work 0/2, Listening 0/4, Thinking 1/4
   faults: H2 x1 C4 x1 C13 x1 T6 x1 T7 x1 T26 x1 A9 x1 A13 x1 K1 x1 K12 x1 K16 x1 Y4 x1
bar: failed, red flags in new: H3 x1; new is more than 2 points under old

Checks:
new: line_refs=0.0 negations_per_1k=7.2 paragraph_only=0.0 drawings=2.0 misaligned=0.0 tables=4.0 quotes=1.0 headings=4.0 ends_asking=1.0 lines=142.0
none: line_refs=0.0 negations_per_1k=11.5 paragraph_only=0.0 drawings=0.0 misaligned=0.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=2.0 lines=38.0
old: line_refs=0.0 negations_per_1k=8.3 paragraph_only=0.0 drawings=2.0 misaligned=0.0 tables=4.0 quotes=0.0 headings=4.0 ends_asking=1.0 lines=119.0
```
