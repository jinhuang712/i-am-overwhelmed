# Eval 2026-11-10-f97c872-vs-9c811ba-opus-5-5

- old: `v0.1.14` (f97c872)
- new: `HEAD` (9c811ba)
- none: no plugin
- model: claude-opus-5-5, effort medium, judge claude-opus-5-5
- runs: {'done': 48, 'failed': 3}
- spent: $17.79 of $25.00

## fix-test-zh

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=18.8 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=7.0
none: line_refs=0.0 negations_per_1k=5.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=9.0
old: line_refs=0.0 negations_per_1k=18.8 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=7.0
```

## chat-en

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=2.7 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=10.0
none: line_refs=0.0 negations_per_1k=3.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=11.0
old: line_refs=0.0 negations_per_1k=5.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=16.0
```

## chat-zh

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=10.4 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=15.0
none: line_refs=0.0 negations_per_1k=10.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=15.0
old: line_refs=0.0 negations_per_1k=7.4 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=10.0
```

## multi-turn-zh

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=7.8 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=62.0
none: line_refs=0.0 negations_per_1k=8.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=48.0
old: line_refs=0.0 negations_per_1k=6.7 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=48.0
```

## many-items-zh

```
Judge: failed

Checks:
new: line_refs=10.0 negations_per_1k=18.0 paragraph_only=1.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=1.0 ends_asking=1.0 lines=37.0
none: line_refs=10.0 negations_per_1k=17.8 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=37.0
old: line_refs=10.0 negations_per_1k=21.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=31.0
```

## design-flaw-zh

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=21.6 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=12.0
none: line_refs=0.0 negations_per_1k=8.7 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=13.0
old: line_refs=0.0 negations_per_1k=12.4 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=13.0
```

## long-discussion-zh

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=8.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=4.0 quotes=0.0 headings=5.0 ends_asking=1.0 lines=106.0
none: line_refs=0.0 negations_per_1k=9.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=4.0 quotes=0.0 headings=2.0 ends_asking=1.0 lines=112.0
old: line_refs=0.0 negations_per_1k=9.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=6.0 ends_asking=1.0 lines=111.0
```

## shape-zh

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=5.4 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=0.0 headings=1.0 ends_asking=0.0 lines=66.0
none: line_refs=0.0 negations_per_1k=500.0 paragraph_only=1.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=1.0
old: line_refs=0.0 negations_per_1k=6.8 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=1.0 ends_asking=0.0 lines=50.0
```

## fact-zh

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=20.9 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=11.0
none: line_refs=0.0 negations_per_1k=20.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=13.0
old: line_refs=0.0 negations_per_1k=19.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=1.0 ends_asking=0.0 lines=22.0
```

## your-step-zh

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=8.3 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=15.0
none: line_refs=0.0 negations_per_1k=6.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=15.0
old: line_refs=0.0 negations_per_1k=6.6 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=15.0
```

## clear-step-zh

```
Judge: failed

Checks:
new: line_refs=1.0 negations_per_1k=4.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=6.0
none: line_refs=1.0 negations_per_1k=4.7 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=5.0
old: line_refs=1.0 negations_per_1k=11.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=8.0
```

## detail-zh

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=4.4 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=1.0 headings=2.0 ends_asking=0.0 lines=108.0
none: line_refs=0.0 negations_per_1k=4.5 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=0.0 headings=2.0 ends_asking=0.0 lines=138.0
old: line_refs=0.0 negations_per_1k=4.1 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=1.0 headings=1.0 ends_asking=0.0 lines=94.0
```

## only-you-know-zh

No finished runs.

## shape-en

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=2.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=1.0 ends_asking=0.0 lines=51.0
none: line_refs=0.0 negations_per_1k=2.3 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=1.0 ends_asking=1.0 lines=58.0
old: line_refs=0.0 negations_per_1k=2.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=1.0 ends_asking=0.0 lines=55.0
```

## session-zh

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=14.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=40.0
none: line_refs=0.0 negations_per_1k=6.1 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=2.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=51.0
old: line_refs=0.0 negations_per_1k=9.3 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=2.0 lines=52.0
```

## better-way-zh

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=3.8 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=18.0
none: line_refs=0.0 negations_per_1k=1.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=20.0
old: line_refs=0.0 negations_per_1k=3.4 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=18.0
```

## vague-zh

```
Judge: failed

Checks:
new: line_refs=0.0 negations_per_1k=19.1 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=16.0
none: line_refs=0.0 negations_per_1k=16.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=12.0
old: line_refs=0.0 negations_per_1k=17.6 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=14.0
```
