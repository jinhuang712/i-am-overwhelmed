# Eval 2026-11-09-2cdb001-vs-027ac76-sonnet-5-5

- old: `2cdb001` (2cdb001)
- new: `HEAD` (027ac76)
- model: claude-sonnet-5-5, effort medium, judge claude-opus-5-5
- runs: {'done': 12}
- spent: $2.06 of $3.00

## chat-zh

```
== new (2 runs): 87.7% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=2.5 D3=2.5 D4=NA D5=NA D6=NA D7=1.5 D8=1.5 D9=3.0 D10=3.0 D11=NA D12=NA D13=3.0 D14=2.0 D15=2.0 E1=NA E2=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 85.1% of points outside E
   A1=NA A2=NA A3=NA B1=2.5 B2=3.0 B3=3.0 B4=3.0 C1=3.0 C2=3.0 C3=2.5 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=2.0 D4=NA D5=NA D6=NA D7=2.0 D8=1.0 D9=3.0 D10=3.0 D11=NA D12=NA D13=3.0 D14=2.0 D15=1.5 E1=NA E2=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=11.7 paragraph_only=0.0 anchors=0.0
old: line_refs=0.0 negations_per_1k=12.4 paragraph_only=0.0 anchors=0.0
```

## multi-turn-zh

```
== new (2 runs): 86.5% of points outside E
   A1=NA A2=NA A3=NA B1=2.5 B2=3.0 B3=3.0 B4=3.0 C1=3.0 C2=3.0 C3=3.0 C4=2.5 C5=3.0 C6=3.0 D1=NA D2=2.5 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=1.0 D9=3.0 D10=1.5 D11=NA D12=3.0 D13=3.0 D14=2.0 D15=2.0 E1=NA E2=NA E3=NA F1=3.0 F2=3.0 F3=3.0 F4=1.5 G1=NA G2=NA G3=NA G4=NA H1=3.0
== old (2 runs): 86.8% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=2.5 B4=3.0 C1=3.0 C2=3.0 C3=2.5 C4=3.0 C5=3.0 C6=2.5 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=1.5 D9=3.0 D10=2.5 D11=NA D12=3.0 D13=3.0 D14=2.5 D15=2.0 E1=NA E2=NA E3=2.0 F1=3.0 F2=2.0 F3=2.5 F4=1.0 G1=NA G2=NA G3=NA G4=NA H1=3.0

Checks:
new: line_refs=0.0 negations_per_1k=6.6 paragraph_only=0.0 anchors=0.5
old: line_refs=0.0 negations_per_1k=7.9 paragraph_only=0.0 anchors=1.0
```

## long-discussion-zh

```
== new (2 runs): 86.5% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 C1=3.0 C2=3.0 C3=2.5 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=1.5 D8=1.0 D9=3.0 D10=1.5 D11=NA D12=NA D13=3.0 D14=2.0 D15=2.0 E1=NA E2=NA E3=NA F1=NA F2=NA F3=2.5 F4=3.0 G1=NA G2=NA G3=NA G4=NA H1=2.5
== old (2 runs): 81.7% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 C1=3.0 C2=3.0 C3=2.5 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=2.0 D9=3.0 D10=2.0 D11=NA D12=NA D13=3.0 D14=2.5 D15=1.0 E1=NA E2=NA E3=NA F1=NA F2=NA F3=2.0 F4=0.0 G1=NA G2=NA G3=NA G4=NA H1=2.5

Checks:
new: line_refs=0.0 negations_per_1k=9.1 paragraph_only=0.0 anchors=2.0
old: line_refs=0.0 negations_per_1k=8.0 paragraph_only=0.0 anchors=0.0
```
