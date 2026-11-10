# Eval 2026-11-11-f4f987c-vs-dece4e0-opus-5-5

- old: `exp/press-release` (f4f987c)
- new: `master` (dece4e0)
- model: claude-opus-5-5, effort medium, judge claude-opus-5-5
- runs: {'done': 24}
- spent: $2.84 of $4.95

## fix-test-zh

```
== new (2 runs): 94.4% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=3.0 A2=3.0 A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=3.0 D2=3.0 D3=NA D4=2.5 D5=3.0 D6=3.0 D7=2.0 D8=NA D9=1.5 D10=2.5 D11=NA D12=NA D13=3.0 D14=NA D15=3.0 D16=3.0 D17=NA D18=NA D19=NA D20=NA D21=NA D22=3.0 D23=NA D24=3.0 D26=NA E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 64.2% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=2.0 A2=3.0 A3=3.0 B1=2.0 B2=2.0 B3=2.0 B4=3.0 B5=3.0 B6=NA C1=2.0 C2=2.0 C3=1.0 C4=1.5 C5=3.0 C6=2.0 D1=3.0 D2=2.0 D3=NA D4=0.0 D5=3.0 D6=0.0 D7=NA D8=NA D9=3.0 D10=1.5 D11=NA D12=0.5 D13=2.5 D14=NA D15=2.0 D16=1.0 D17=NA D18=NA D19=NA D20=NA D21=NA D22=0.0 D23=NA D24=2.0 D26=NA E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=5.6 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=27.0
old: line_refs=0.0 negations_per_1k=14.3 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.5 ends_asking=0.0 lines=11.0
```

## chat-zh

```
== new (2 runs): 97.5% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=NA D13=3.0 D14=3.0 D15=1.5 D16=3.0 D17=3.0 D18=3.0 D19=2.5 D20=3.0 D21=3.0 D22=3.0 D23=NA D24=3.0 D26=NA E1=NA E3=3.0 F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 61.2% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=2.0 B2=1.0 B3=3.0 B4=2.0 B5=3.0 B6=NA C1=1.0 C2=2.0 C3=1.0 C4=2.0 C5=3.0 C6=2.0 D1=NA D2=1.0 D3=NA D4=NA D5=NA D6=NA D7=1.0 D8=NA D9=3.0 D10=2.0 D11=NA D12=NA D13=3.0 D14=NA D15=1.0 D16=0.0 D17=NA D18=2.0 D19=1.0 D20=NA D21=NA D22=3.0 D23=NA D24=1.0 D26=NA E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=17.8 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=22.0
old: line_refs=0.0 negations_per_1k=5.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.5 ends_asking=0.0 lines=20.0
```

## design-flaw-zh

```
== new (2 runs): 95.9% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=3.0 A1=2.0 A2=3.0 A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=2.5 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=2.0 D2=3.0 D3=NA D4=2.5 D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=NA D13=3.0 D14=3.0 D15=NA D16=3.0 D17=2.5 D18=3.0 D19=2.0 D20=3.0 D21=3.0 D22=3.0 D23=3.0 D24=3.0 D26=NA E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=3.0
== old (2 runs): 71.0% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=3.0 A1=2.0 A2=3.0 A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=2.0 C2=2.0 C3=2.0 C4=2.5 C5=3.0 C6=3.0 D1=3.0 D2=1.5 D3=NA D4=0.0 D5=NA D6=0.0 D7=2.0 D8=1.0 D9=3.0 D10=1.0 D11=2.0 D12=2.0 D13=3.0 D14=1.0 D15=NA D16=2.5 D17=2.0 D18=2.0 D19=NA D20=1.0 D21=3.0 D22=0.0 D23=3.0 D24=2.0 D26=NA E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=2.0
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=18.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=25.5
old: line_refs=0.0 negations_per_1k=20.9 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.5 quotes=0.0 headings=1.0 ends_asking=0.0 lines=21.0
```

## shape-zh

```
== new (2 runs): 92.2% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.5 D1=NA D2=2.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=1.0 D9=2.5 D10=2.5 D11=NA D12=3.0 D13=3.0 D14=NA D15=2.0 D16=3.0 D17=3.0 D18=NA D19=3.0 D20=NA D21=1.0 D22=3.0 D23=NA D24=3.0 D26=NA E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 66.7% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=2.5 B2=2.0 B3=2.0 B4=3.0 B5=3.0 B6=NA C1=1.0 C2=1.0 C3=0.5 C4=1.5 C5=2.5 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=1.0 D8=NA D9=3.0 D10=1.5 D11=NA D12=2.0 D13=3.0 D14=NA D15=2.0 D16=3.0 D17=NA D18=NA D19=NA D20=NA D21=NA D22=1.0 D23=NA D24=1.5 D26=NA E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=3.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.5 lines=34.0
old: line_refs=0.0 negations_per_1k=4.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=1.0 ends_asking=0.0 lines=52.0
```

## fact-zh

```
== new (2 runs): 94.4% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=NA R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=2.0 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.5 D8=NA D9=3.0 D10=2.0 D11=3.0 D12=NA D13=3.0 D14=NA D15=3.0 D16=3.0 D17=NA D18=NA D19=NA D20=NA D21=NA D22=3.0 D23=NA D24=3.0 D26=NA E1=NA E3=2.5 F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 45.5% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=NA R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=2.0 B3=1.0 B4=3.0 B5=3.0 B6=NA C1=1.0 C2=1.0 C3=0.5 C4=0.5 C5=1.5 C6=0.5 D1=NA D2=1.5 D3=NA D4=NA D5=NA D6=NA D7=0.5 D8=NA D9=1.5 D10=NA D11=3.0 D12=NA D13=1.0 D14=NA D15=3.0 D16=1.0 D17=NA D18=NA D19=1.0 D20=NA D21=NA D22=3.0 D23=NA D24=1.0 D26=NA E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=15.5 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=20.0
old: line_refs=0.0 negations_per_1k=9.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.5 quotes=0.0 headings=0.0 ends_asking=0.0 lines=9.5
```

## better-way-zh

```
== new (2 runs): 97.7% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=2.5 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=NA D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=NA D16=3.0 D17=NA D18=NA D19=3.0 D20=NA D21=NA D22=3.0 D23=3.0 D24=3.0 D26=NA E1=NA E3=2.0 F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 61.5% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=2.5 B2=1.0 B3=2.0 B4=2.0 B5=3.0 B6=NA C1=0.0 C2=2.0 C3=1.0 C4=1.0 C5=2.5 C6=1.0 D1=NA D2=2.5 D3=NA D4=NA D5=NA D6=NA D7=1.0 D8=NA D9=2.0 D10=2.0 D11=NA D12=3.0 D13=2.5 D14=NA D15=NA D16=NA D17=NA D18=NA D19=NA D20=NA D21=NA D22=3.0 D23=2.0 D24=1.0 D26=NA E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=7.1 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=23.5
old: line_refs=0.0 negations_per_1k=2.4 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.5 ends_asking=0.0 lines=23.5
```
