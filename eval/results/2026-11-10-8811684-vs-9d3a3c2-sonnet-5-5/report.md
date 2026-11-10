# Eval 2026-11-10-8811684-vs-9d3a3c2-sonnet-5-5

- old: `8811684` (8811684)
- new: `HEAD` (9d3a3c2)
- model: claude-sonnet-5-5, effort medium, judge claude-opus-5-5
- runs: {'done': 36}
- spent: $4.45 of $7.00

## chat-en

```
== new (3 runs): 85.0% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=2.7 C1=3.0 C2=2.0 C3=1.3 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=2.7 D3=NA D4=NA D5=NA D6=NA D7=2.7 D8=2.7 D9=3.0 D10=2.7 D11=1.7 D12=3.0 D13=3.0 D14=3.0 D15=2.0 D16=3.0 D17=3.0 D18=2.0 D19=1.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (3 runs): 83.6% of points outside E
   A1=NA A2=NA A3=NA B1=2.7 B2=2.3 B3=3.0 B4=3.0 C1=3.0 C2=3.0 C3=3.0 C4=1.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=2.7 D9=3.0 D10=2.3 D11=NA D12=NA D13=3.0 D14=NA D15=2.7 D16=1.0 D17=3.0 D18=2.0 D19=1.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=2.5 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=0.0 headings=1.0 ends_asking=1.0 lines=40.7
old: line_refs=0.0 negations_per_1k=2.9 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=7.7
```

## chat-zh

```
== new (3 runs): 90.8% of points outside E
   A1=NA A2=NA A3=NA B1=2.7 B2=3.0 B3=3.0 B4=3.0 C1=3.0 C2=2.7 C3=2.3 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=2.7 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=2.7 D11=3.0 D12=3.0 D13=3.0 D14=3.0 D15=2.3 D16=3.0 D17=2.3 D18=3.0 D19=1.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (3 runs): 78.8% of points outside E
   A1=NA A2=NA A3=NA B1=2.0 B2=3.0 B3=3.0 B4=3.0 C1=3.0 C2=2.3 C3=2.3 C4=1.3 C5=3.0 C6=2.0 D1=NA D2=1.0 D3=NA D4=NA D5=NA D6=NA D7=1.7 D8=3.0 D9=3.0 D10=2.7 D11=NA D12=NA D13=3.0 D14=NA D15=2.7 D16=1.0 D17=2.7 D18=3.0 D19=1.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=16.5 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.7 quotes=0.0 headings=1.0 ends_asking=1.0 lines=31.7
old: line_refs=0.0 negations_per_1k=14.4 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=9.0
```

## multi-turn-zh

```
== new (3 runs): 93.5% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 C1=3.0 C2=2.0 C3=2.0 C4=3.0 C5=3.0 C6=2.7 D1=NA D2=2.7 D3=3.0 D4=NA D5=3.0 D6=NA D7=3.0 D8=2.3 D9=3.0 D10=3.0 D11=2.3 D12=3.0 D13=3.0 D14=3.0 D15=3.0 D16=3.0 D17=3.0 D18=2.7 D19=1.7 E1=NA E3=NA F1=3.0 F2=3.0 F3=2.7 F4=3.0 G1=NA G2=NA G3=NA G4=NA H1=3.0
== old (3 runs): 80.2% of points outside E
   A1=NA A2=NA A3=NA B1=2.7 B2=3.0 B3=3.0 B4=3.0 C1=3.0 C2=2.0 C3=3.0 C4=1.0 C5=2.0 C6=2.0 D1=NA D2=1.0 D3=3.0 D4=NA D5=3.0 D6=NA D7=2.0 D8=2.0 D9=3.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=3.0 D16=1.0 D17=3.0 D18=2.7 D19=1.0 E1=NA E3=NA F1=3.0 F2=3.0 F3=2.7 F4=1.0 G1=NA G2=NA G3=NA G4=NA H1=3.0

Checks:
new: line_refs=0.0 negations_per_1k=8.2 paragraph_only=0.0 anchors=1.0 drawings=1.3 tables=2.3 quotes=0.7 headings=3.0 ends_asking=3.0 lines=87.0
old: line_refs=0.0 negations_per_1k=8.3 paragraph_only=0.0 anchors=1.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=2.7 lines=26.3
```

## many-items-zh

```
== new (3 runs): 93.1% of points outside E
   A1=2.3 A2=NA A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=2.7 C1=3.0 C2=2.7 C3=2.3 C4=3.0 C5=3.0 C6=2.7 D1=3.0 D2=3.0 D3=2.7 D4=3.0 D5=3.0 D6=NA D7=2.3 D8=3.0 D9=3.0 D10=2.7 D11=2.7 D12=3.0 D13=3.0 D14=3.0 D15=NA D16=2.7 D17=2.7 D18=2.0 D19=1.7 E1=NA E3=NA F1=NA F2=NA F3=3.0 F4=NA G1=3.0 G2=3.0 G3=3.0 G4=3.0 H1=NA
== old (3 runs): 86.6% of points outside E
   A1=2.0 A2=NA A3=3.0 B1=2.7 B2=3.0 B3=3.0 B4=3.0 C1=2.0 C2=3.0 C3=2.7 C4=2.0 C5=3.0 C6=2.7 D1=3.0 D2=2.3 D3=2.7 D4=2.3 D5=3.0 D6=NA D7=2.0 D8=2.7 D9=3.0 D10=2.3 D11=2.7 D12=3.0 D13=3.0 D14=3.0 D15=NA D16=2.0 D17=2.3 D18=1.3 D19=1.0 E1=NA E3=NA F1=NA F2=NA F3=2.7 F4=NA G1=3.0 G2=3.0 G3=3.0 G4=3.0 H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=7.3 paragraph_only=0.0 anchors=0.7 drawings=1.7 tables=2.7 quotes=1.0 headings=3.0 ends_asking=2.3 lines=156.0
old: line_refs=0.0 negations_per_1k=9.7 paragraph_only=0.0 anchors=0.7 drawings=0.0 tables=1.0 quotes=0.0 headings=2.0 ends_asking=3.0 lines=101.7
```

## design-flaw-zh

```
== new (3 runs): 86.2% of points outside E
   A1=1.3 A2=3.0 A3=2.0 B1=2.0 B2=3.0 B3=3.0 B4=2.0 C1=3.0 C2=2.7 C3=2.0 C4=3.0 C5=3.0 C6=2.3 D1=2.7 D2=3.0 D3=NA D4=2.7 D5=3.0 D6=3.0 D7=2.7 D8=3.0 D9=3.0 D10=2.3 D11=2.5 D12=3.0 D13=3.0 D14=3.0 D15=NA D16=3.0 D17=2.7 D18=2.0 D19=NA E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=1.0
== old (3 runs): 83.9% of points outside E
   A1=1.7 A2=3.0 A3=2.3 B1=2.3 B2=2.7 B3=2.7 B4=2.7 C1=3.0 C2=2.7 C3=2.7 C4=1.0 C5=3.0 C6=2.0 D1=3.0 D2=3.0 D3=NA D4=2.0 D5=3.0 D6=2.0 D7=2.7 D8=2.3 D9=3.0 D10=2.7 D11=NA D12=3.0 D13=3.0 D14=3.0 D15=NA D16=2.0 D17=2.7 D18=2.7 D19=NA E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=1.3

Checks:
new: line_refs=0.0 negations_per_1k=8.5 paragraph_only=0.0 anchors=0.0 drawings=0.3 tables=0.7 quotes=0.0 headings=1.0 ends_asking=1.0 lines=32.0
old: line_refs=0.0 negations_per_1k=8.3 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.7 lines=21.3
```

## shape-zh

```
== new (3 runs): 84.3% of points outside E
   A1=NA A2=NA A3=NA B1=2.7 B2=3.0 B3=3.0 B4=3.0 C1=1.7 C2=2.7 C3=2.3 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.3 D8=2.3 D9=3.0 D10=1.7 D11=2.0 D12=3.0 D13=3.0 D14=3.0 D15=2.7 D16=3.0 D17=2.7 D18=1.7 D19=1.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (3 runs): 82.1% of points outside E
   A1=NA A2=NA A3=NA B1=1.7 B2=3.0 B3=3.0 B4=3.0 C1=2.0 C2=2.0 C3=2.0 C4=2.3 C5=3.0 C6=1.7 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.7 D8=2.7 D9=3.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=3.0 D15=2.7 D16=3.0 D17=3.0 D18=0.0 D19=1.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=4.9 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.7 quotes=0.0 headings=1.0 ends_asking=1.0 lines=50.0
old: line_refs=0.0 negations_per_1k=3.3 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=1.0 ends_asking=1.0 lines=46.7
```
