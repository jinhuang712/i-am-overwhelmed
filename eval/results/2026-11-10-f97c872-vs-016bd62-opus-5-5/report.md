# Eval 2026-11-10-f97c872-vs-016bd62-opus-5-5

- old: `v0.1.14` (f97c872)
- new: `HEAD` (016bd62)
- model: claude-opus-5-5, effort medium, judge claude-opus-5-5
- runs: {'done': 13, 'skipped': 2, 'stopped': 1}
- spent: $1.53 of $1.80
- incomplete: the budget stopped some runs

## chat-zh

```
== new (2 runs): 96.2% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=2.5 B3=3.0 B4=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=NA D13=3.0 D14=3.0 D15=2.0 D16=3.0 D17=3.0 D18=3.0 D19=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 93.2% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=2.5 B3=3.0 B4=3.0 C1=3.0 C2=2.5 C3=2.5 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=NA D13=3.0 D14=3.0 D15=2.0 D16=3.0 D17=2.5 D18=3.0 D19=2.5 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=19.9 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=21.5
old: line_refs=0.0 negations_per_1k=18.4 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=22.5
```

## design-flaw-zh

```
== new (2 runs): 88.3% of points outside E
   A1=3.0 A2=NA A3=3.0 B1=3.0 B2=2.0 B3=3.0 B4=2.0 C1=2.5 C2=3.0 C3=2.5 C4=2.5 C5=3.0 C6=2.0 D1=3.0 D2=2.5 D3=NA D4=3.0 D5=3.0 D6=NA D7=3.0 D8=2.0 D9=3.0 D10=2.5 D11=NA D12=3.0 D13=3.0 D14=2.0 D15=NA D16=3.0 D17=2.0 D18=2.5 D19=NA E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=2.5
== old (1 runs): 82.1% of points outside E
   A1=1.0 A2=NA A3=3.0 B1=2.0 B2=2.0 B3=3.0 B4=2.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=2.0 D2=2.0 D3=NA D4=2.0 D5=3.0 D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=3.0 D15=2.0 D16=2.0 D17=2.0 D18=1.0 D19=NA E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=2.0

Checks:
new: line_refs=0.0 negations_per_1k=16.8 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=22.0
old: line_refs=0.0 negations_per_1k=7.6 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=18.0
```

## shape-zh

```
== new (2 runs): 90.3% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=2.5 B4=3.0 C1=2.0 C2=3.0 C3=2.0 C4=2.5 C5=3.0 C6=2.5 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=2.5 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=3.0 D15=2.0 D16=3.0 D17=3.0 D18=3.0 D19=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=2.0
== old (2 runs): 80.6% of points outside E
   A1=NA A2=NA A3=NA B1=2.0 B2=3.0 B3=3.0 B4=2.5 C1=2.0 C2=2.5 C3=2.5 C4=2.5 C5=3.0 C6=2.5 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=1.5 D8=2.0 D9=3.0 D10=2.0 D11=2.0 D12=3.0 D13=3.0 D14=2.0 D15=2.0 D16=3.0 D17=3.0 D18=2.0 D19=2.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=1.0

Checks:
new: line_refs=0.0 negations_per_1k=3.8 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=40.0
old: line_refs=0.0 negations_per_1k=3.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.5 quotes=0.5 headings=0.0 ends_asking=1.0 lines=43.0
```

## fact-zh

```
== new (2 runs): 94.3% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=2.0 B3=NA B4=2.5 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.5 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=NA D9=3.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=3.0 D16=3.0 D17=NA D18=NA D19=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 79.8% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=2.0 B3=NA B4=2.5 C1=2.0 C2=3.0 C3=1.5 C4=2.0 C5=3.0 C6=2.0 D1=NA D2=1.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=1.0 D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=2.0 D16=3.0 D17=2.0 D18=1.0 D19=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=18.9 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=0.5 lines=15.5
old: line_refs=0.0 negations_per_1k=16.4 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=0.5 lines=15.5
```
