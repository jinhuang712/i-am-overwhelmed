# Eval 2026-11-10-8811684-vs-30abbeb-sonnet-5-5

- old: `8811684` (8811684)
- new: `HEAD` (30abbeb)
- model: claude-sonnet-5-5, effort medium, judge claude-opus-5-5
- runs: {'done': 18}
- spent: $0.73 of $2.00

## chat-en

```
== new (3 runs): 90.1% of points outside E
   A1=NA A2=NA A3=NA B1=2.3 B2=2.7 B3=3.0 B4=3.0 C1=3.0 C2=2.7 C3=2.7 C4=3.0 C5=3.0 C6=2.7 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.7 D8=2.7 D9=3.0 D10=2.7 D11=NA D12=3.0 D13=3.0 D14=NA D15=3.0 D16=1.7 D17=3.0 D18=3.0 D19=1.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (3 runs): 92.1% of points outside E
   A1=NA A2=NA A3=NA B1=2.7 B2=2.7 B3=3.0 B4=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=2.3 D3=NA D4=NA D5=NA D6=NA D7=2.7 D8=3.0 D9=3.0 D10=2.7 D11=NA D12=NA D13=3.0 D14=NA D15=3.0 D16=2.0 D17=3.0 D18=3.0 D19=1.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=3.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=9.7
old: line_refs=0.0 negations_per_1k=3.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=7.0
```

## chat-zh

```
== new (3 runs): 90.5% of points outside E
   A1=NA A2=NA A3=NA B1=2.0 B2=2.3 B3=3.0 B4=2.7 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.7 D8=3.0 D9=3.0 D10=NA D11=NA D12=3.0 D13=3.0 D14=NA D15=2.3 D16=3.0 D17=3.0 D18=3.0 D19=1.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (3 runs): 80.7% of points outside E
   A1=NA A2=NA A3=NA B1=2.7 B2=3.0 B3=3.0 B4=3.0 C1=3.0 C2=2.7 C3=2.3 C4=2.7 C5=3.0 C6=2.0 D1=NA D2=2.0 D3=NA D4=NA D5=NA D6=NA D7=2.7 D8=2.0 D9=3.0 D10=3.0 D11=NA D12=NA D13=3.0 D14=3.0 D15=1.7 D16=0.7 D17=1.7 D18=2.7 D19=1.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=19.5 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=12.0
old: line_refs=0.0 negations_per_1k=10.8 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=12.0
```

## shape-zh

```
== new (3 runs): 88.4% of points outside E
   A1=NA A2=NA A3=NA B1=2.3 B2=3.0 B3=3.0 B4=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=1.7 D8=2.7 D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=3.0 D15=2.0 D16=2.3 D17=3.0 D18=1.7 D19=1.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (3 runs): 85.3% of points outside E
   A1=NA A2=NA A3=NA B1=2.3 B2=3.0 B3=3.0 B4=3.0 C1=3.0 C2=2.7 C3=2.3 C4=3.0 C5=3.0 C6=2.7 D1=NA D2=2.7 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=2.7 D9=3.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=2.3 D15=2.7 D16=2.3 D17=2.3 D18=1.3 D19=1.0 E1=2.0 E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=4.2 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=28.3
old: line_refs=0.0 negations_per_1k=2.3 paragraph_only=0.0 anchors=0.7 drawings=1.0 tables=0.0 quotes=0.0 headings=0.7 ends_asking=1.0 lines=43.0
```
