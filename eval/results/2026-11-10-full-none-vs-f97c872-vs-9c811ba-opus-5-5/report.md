# Eval 2026-11-10-f97c872-vs-c8b568a-opus-5-5

- old: `v0.1.14` (f97c872)
- new: `HEAD` (c8b568a)
- none: no plugin
- model: claude-opus-5-5, effort medium, judge claude-opus-5-5
- runs: {'done': 2, 'skipped': 49}
- spent: $28.45 of $33.79

## fix-test-zh

```
== new (1 runs): 90.6% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=3.0 A2=3.0 A3=2.0 B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=3.0 D2=3.0 D3=NA D4=1.0 D5=3.0 D6=3.0 D7=3.0 D8=3.0 D9=3.0 D10=NA D11=NA D12=3.0 D13=3.0 D14=NA D15=NA D16=3.0 D17=3.0 D18=0.0 D19=3.0 D20=NA D21=3.0 D22=3.0 D23=NA D24=2.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== none (1 runs): 63.2% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=3.0 A2=3.0 A3=1.0 B1=3.0 B2=2.0 B3=2.0 B4=2.0 B5=3.0 C1=3.0 C2=2.0 C3=2.0 C4=2.0 C5=3.0 C6=2.0 D1=3.0 D2=3.0 D3=NA D4=0.0 D5=3.0 D6=0.0 D7=1.0 D8=NA D9=0.0 D10=1.0 D11=NA D12=1.0 D13=3.0 D14=NA D15=NA D16=1.0 D17=NA D18=2.0 D19=NA D20=NA D21=NA D22=2.0 D23=NA D24=2.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (1 runs): 88.5% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=3.0 A2=3.0 A3=3.0 B1=3.0 B2=2.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=3.0 D2=3.0 D3=NA D4=2.0 D5=3.0 D6=3.0 D7=2.0 D8=3.0 D9=0.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=NA D16=3.0 D17=3.0 D18=2.0 D19=NA D20=NA D21=3.0 D22=3.0 D23=NA D24=3.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=6.5 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=32.0
none: line_refs=0.0 negations_per_1k=5.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=9.0
old: line_refs=0.0 negations_per_1k=2.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=26.0
```

## chat-en

```
== new (1 runs): 93.6% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=2.0 B2=3.0 B3=3.0 B4=3.0 B5=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=3.0 D12=3.0 D13=3.0 D14=NA D15=3.0 D16=3.0 D17=3.0 D18=3.0 D19=NA D20=NA D21=3.0 D22=3.0 D23=NA D24=3.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== none (1 runs): 63.6% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=2.0 B2=2.0 B3=3.0 B4=3.0 B5=NA C1=3.0 C2=2.0 C3=2.0 C4=2.0 C5=3.0 C6=2.0 D1=NA D2=2.0 D3=NA D4=NA D5=NA D6=NA D7=1.0 D8=NA D9=3.0 D10=1.0 D11=NA D12=1.0 D13=3.0 D14=NA D15=2.0 D16=1.0 D17=NA D18=2.0 D19=NA D20=NA D21=NA D22=0.0 D23=NA D24=2.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (1 runs): 85.9% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=2.0 B5=NA C1=3.0 C2=2.0 C3=2.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=2.0 D9=3.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=3.0 D15=3.0 D16=3.0 D17=3.0 D18=1.0 D19=NA D20=3.0 D21=3.0 D22=NA D23=NA D24=2.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=0.0 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=16.0
none: line_refs=0.0 negations_per_1k=3.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=11.0
old: line_refs=0.0 negations_per_1k=1.8 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=21.0
```

## chat-zh

```
== new (1 runs): 93.8% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=NA D13=3.0 D14=3.0 D15=2.0 D16=2.0 D17=3.0 D18=3.0 D19=3.0 D20=3.0 D21=3.0 D22=NA D23=NA D24=3.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== none (1 runs): 71.2% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=2.0 B2=2.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=2.0 C3=2.0 C4=2.0 C5=3.0 C6=2.0 D1=NA D2=2.0 D3=NA D4=NA D5=NA D6=NA D7=1.0 D8=NA D9=3.0 D10=2.0 D11=NA D12=NA D13=3.0 D14=NA D15=1.0 D16=1.0 D17=NA D18=2.0 D19=NA D20=NA D21=NA D22=3.0 D23=NA D24=2.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (1 runs): 93.8% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=NA D13=3.0 D14=3.0 D15=1.0 D16=3.0 D17=3.0 D18=3.0 D19=3.0 D20=3.0 D21=3.0 D22=NA D23=NA D24=3.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=21.8 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=21.0
none: line_refs=0.0 negations_per_1k=10.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=15.0
old: line_refs=0.0 negations_per_1k=23.4 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=22.0
```

## multi-turn-zh

```
== new (1 runs): 93.9% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=3.0 R5=3.0 R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=3.0 D3=3.0 D4=NA D5=3.0 D6=NA D7=3.0 D8=2.0 D9=3.0 D10=2.0 D11=3.0 D12=3.0 D13=3.0 D14=3.0 D15=2.0 D16=3.0 D17=3.0 D18=3.0 D19=3.0 D20=3.0 D21=3.0 D22=1.0 D23=3.0 D24=3.0 D25=1.0 D26=NA E1=NA F1=3.0 F2=3.0 F3=3.0 F4=3.0 G1=NA G2=NA G3=NA G4=NA H1=3.0
== none (1 runs): 63.7% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=2.0 R4=3.0 R5=3.0 R6=NA A1=NA A2=NA A3=NA B1=2.0 B2=2.0 B3=3.0 B4=2.0 B5=3.0 C1=3.0 C2=2.0 C3=2.0 C4=2.0 C5=3.0 C6=2.0 D1=NA D2=1.0 D3=3.0 D4=NA D5=3.0 D6=NA D7=1.0 D8=1.0 D9=3.0 D10=1.0 D11=3.0 D12=3.0 D13=3.0 D14=NA D15=2.0 D16=1.0 D17=NA D18=1.0 D19=NA D20=NA D21=1.0 D22=0.0 D23=3.0 D24=2.0 D25=0.0 D26=NA E1=NA F1=3.0 F2=0.0 F3=1.0 F4=0.0 G1=NA G2=NA G3=NA G4=NA H1=3.0
== old (1 runs): 86.8% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=2.0 R4=3.0 R5=3.0 R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=2.0 C3=2.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=3.0 D3=3.0 D4=NA D5=3.0 D6=NA D7=2.0 D8=2.0 D9=3.0 D10=2.0 D11=3.0 D12=3.0 D13=3.0 D14=3.0 D15=2.0 D16=3.0 D17=3.0 D18=1.0 D19=3.0 D20=0.0 D21=3.0 D22=2.0 D23=3.0 D24=2.0 D25=1.0 D26=NA E1=1.0 F1=3.0 F2=3.0 F3=3.0 F4=3.0 G1=NA G2=NA G3=NA G4=NA H1=3.0
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=6.8 paragraph_only=0.0 anchors=1.0 drawings=3.0 tables=1.0 quotes=2.0 headings=0.0 ends_asking=3.0 lines=64.0
none: line_refs=0.0 negations_per_1k=8.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=48.0
old: line_refs=0.0 negations_per_1k=7.2 paragraph_only=0.0 anchors=1.0 drawings=3.0 tables=2.0 quotes=2.0 headings=0.0 ends_asking=3.0 lines=79.0
```

## many-items-zh

```
== new (1 runs): 85.7% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=2.0 A2=3.0 A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=3.0 D2=2.0 D3=3.0 D4=2.0 D5=3.0 D6=NA D7=3.0 D8=2.0 D9=3.0 D10=2.0 D11=2.0 D12=2.0 D13=3.0 D14=3.0 D15=2.0 D16=3.0 D17=3.0 D18=1.0 D19=2.0 D20=3.0 D21=1.0 D22=1.0 D23=NA D24=3.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=3.0 F4=NA G1=3.0 G2=3.0 G3=3.0 G4=3.0 H1=NA
== none (1 runs): 45.2% of points outside E
   red flags: R3 x1, R6 x1
   R1=3.0 R2=3.0 R3=0.0 R4=NA R5=NA R6=0.0 A1=2.0 A2=3.0 A3=0.0 B1=3.0 B2=2.0 B3=2.0 B4=2.0 B5=3.0 C1=3.0 C2=1.0 C3=1.0 C4=2.0 C5=2.0 C6=1.0 D1=3.0 D2=1.0 D3=3.0 D4=0.0 D5=0.0 D6=0.0 D7=1.0 D8=0.0 D9=3.0 D10=1.0 D11=NA D12=1.0 D13=3.0 D14=1.0 D15=2.0 D16=1.0 D17=1.0 D18=0.0 D19=NA D20=0.0 D21=2.0 D22=1.0 D23=NA D24=2.0 D25=1.0 D26=1.0 E1=NA F1=NA F2=NA F3=0.0 F4=NA G1=2.0 G2=0.0 G3=0.0 G4=0.0 H1=NA
== old (1 runs): 85.7% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=2.0 A2=3.0 A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=2.0 C3=2.0 C4=3.0 C5=3.0 C6=2.0 D1=3.0 D2=3.0 D3=3.0 D4=2.0 D5=3.0 D6=NA D7=2.0 D8=3.0 D9=3.0 D10=2.0 D11=2.0 D12=2.0 D13=3.0 D14=3.0 D15=2.0 D16=3.0 D17=3.0 D18=3.0 D19=2.0 D20=3.0 D21=2.0 D22=1.0 D23=NA D24=2.0 D25=1.0 D26=NA E1=2.0 F1=NA F2=NA F3=3.0 F4=NA G1=3.0 G2=3.0 G3=3.0 G4=2.0 H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=11.2 paragraph_only=0.0 anchors=0.0 drawings=2.0 tables=1.0 quotes=3.0 headings=0.0 ends_asking=3.0 lines=70.0
none: line_refs=10.0 negations_per_1k=17.8 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=37.0
old: line_refs=0.0 negations_per_1k=11.6 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=3.0 quotes=2.0 headings=0.0 ends_asking=3.0 lines=100.0
```

## design-flaw-zh

```
== new (1 runs): 93.8% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=3.0 A1=2.0 A2=3.0 A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=3.0 D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=2.0 D11=NA D12=NA D13=3.0 D14=3.0 D15=3.0 D16=3.0 D17=2.0 D18=3.0 D19=NA D20=3.0 D21=3.0 D22=3.0 D23=NA D24=3.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=3.0
== none (1 runs): 65.7% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=2.0 R4=3.0 R5=NA R6=3.0 A1=2.0 A2=3.0 A3=3.0 B1=3.0 B2=2.0 B3=2.0 B4=3.0 B5=3.0 C1=2.0 C2=2.0 C3=2.0 C4=2.0 C5=3.0 C6=2.0 D1=3.0 D2=2.0 D3=NA D4=0.0 D5=NA D6=0.0 D7=1.0 D8=1.0 D9=3.0 D10=1.0 D11=NA D12=1.0 D13=3.0 D14=NA D15=NA D16=2.0 D17=3.0 D18=2.0 D19=NA D20=NA D21=2.0 D22=0.0 D23=3.0 D24=2.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=1.0
== old (1 runs): 84.4% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=3.0 A1=2.0 A2=3.0 A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=2.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=3.0 D5=NA D6=NA D7=3.0 D8=1.0 D9=3.0 D10=1.0 D11=NA D12=NA D13=3.0 D14=0.0 D15=3.0 D16=3.0 D17=2.0 D18=3.0 D19=NA D20=3.0 D21=2.0 D22=3.0 D23=NA D24=2.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=3.0
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=13.3 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=25.0
none: line_refs=0.0 negations_per_1k=8.7 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=13.0
old: line_refs=0.0 negations_per_1k=10.6 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=23.0
```

## long-discussion-zh

```
== new (1 runs): 89.5% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=2.0 D12=3.0 D13=3.0 D14=2.0 D15=3.0 D16=3.0 D17=3.0 D18=3.0 D19=3.0 D20=1.0 D21=2.0 D22=2.0 D23=3.0 D24=3.0 D25=0.0 D26=2.0 E1=NA F1=NA F2=NA F3=3.0 F4=2.0 G1=NA G2=NA G3=NA G4=NA H1=3.0
== none (1 runs): 62.5% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=1.0 B3=3.0 B4=2.0 B5=3.0 C1=0.0 C2=2.0 C3=2.0 C4=2.0 C5=3.0 C6=2.0 D1=NA D2=2.0 D3=NA D4=NA D5=NA D6=NA D7=1.0 D8=1.0 D9=3.0 D10=1.0 D11=1.0 D12=2.0 D13=3.0 D14=NA D15=3.0 D16=2.0 D17=1.0 D18=1.0 D19=NA D20=NA D21=2.0 D22=2.0 D23=3.0 D24=2.0 D25=0.0 D26=1.0 E1=NA F1=NA F2=NA F3=3.0 F4=0.0 G1=NA G2=NA G3=NA G4=NA H1=3.0
== old (1 runs): 93.3% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=3.0 D9=3.0 D10=3.0 D11=3.0 D12=3.0 D13=3.0 D14=3.0 D15=3.0 D16=3.0 D17=2.0 D18=3.0 D19=3.0 D20=3.0 D21=3.0 D22=3.0 D23=3.0 D24=3.0 D25=0.0 D26=2.0 E1=NA F1=NA F2=NA F3=3.0 F4=2.0 G1=NA G2=NA G3=NA G4=NA H1=3.0
bar: failed, new is more than 3 points under old

Checks:
new: line_refs=0.0 negations_per_1k=6.8 paragraph_only=0.0 anchors=2.0 drawings=6.0 tables=4.0 quotes=3.0 headings=0.0 ends_asking=6.0 lines=154.0
none: line_refs=0.0 negations_per_1k=9.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=4.0 quotes=0.0 headings=2.0 ends_asking=1.0 lines=112.0
old: line_refs=0.0 negations_per_1k=7.4 paragraph_only=0.0 anchors=2.0 drawings=6.0 tables=1.0 quotes=1.0 headings=0.0 ends_asking=6.0 lines=136.0
```

## shape-zh

```
== new (1 runs): 88.5% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=3.0 R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=1.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=2.0 D11=2.0 D12=2.0 D13=3.0 D14=2.0 D15=2.0 D16=3.0 D17=3.0 D18=3.0 D19=3.0 D20=3.0 D21=1.0 D22=2.0 D23=NA D24=3.0 D25=NA D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== none (1 runs): 62.3% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=3.0 R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=1.0 B3=2.0 B4=3.0 B5=3.0 C1=1.0 C2=1.0 C3=1.0 C4=2.0 C5=3.0 C6=2.0 D1=NA D2=2.0 D3=NA D4=NA D5=NA D6=NA D7=1.0 D8=NA D9=3.0 D10=1.0 D11=0.0 D12=2.0 D13=3.0 D14=NA D15=1.0 D16=3.0 D17=NA D18=NA D19=2.0 D20=NA D21=NA D22=1.0 D23=NA D24=2.0 D25=NA D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (1 runs): 88.1% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=3.0 R5=NA R6=NA A1=NA A2=NA A3=NA B1=2.0 B2=3.0 B3=1.0 B4=3.0 B5=3.0 C1=2.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=2.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=2.0 D15=2.0 D16=3.0 D17=3.0 D18=3.0 D19=3.0 D20=3.0 D21=1.0 D22=3.0 D23=NA D24=3.0 D25=NA D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=6.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=45.0
none: line_refs=0.0 negations_per_1k=4.4 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=1.0 headings=1.0 ends_asking=0.0 lines=73.0
old: line_refs=0.0 negations_per_1k=4.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=34.0
```

## fact-zh

```
== new (1 runs): 91.2% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=3.0 A1=NA A2=NA A3=NA B1=NA B2=3.0 B3=NA B4=3.0 B5=NA C1=3.0 C2=2.0 C3=2.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=NA D9=3.0 D10=2.0 D11=3.0 D12=NA D13=3.0 D14=NA D15=3.0 D16=3.0 D17=NA D18=NA D19=NA D20=NA D21=NA D22=3.0 D23=NA D24=3.0 D25=2.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== none (1 runs): 86.0% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=3.0 A1=NA A2=NA A3=NA B1=NA B2=3.0 B3=NA B4=3.0 B5=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=1.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=1.0 D8=NA D9=3.0 D10=3.0 D11=1.0 D12=NA D13=3.0 D14=NA D15=3.0 D16=3.0 D17=NA D18=NA D19=NA D20=NA D21=NA D22=3.0 D23=NA D24=3.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (1 runs): 85.2% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=3.0 A1=NA A2=NA A3=NA B1=NA B2=2.0 B3=NA B4=3.0 B5=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=2.0 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=NA D9=3.0 D10=2.0 D11=NA D12=NA D13=3.0 D14=NA D15=3.0 D16=3.0 D17=NA D18=NA D19=NA D20=NA D21=NA D22=3.0 D23=NA D24=2.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=14.9 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=20.0
none: line_refs=0.0 negations_per_1k=20.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=13.0
old: line_refs=0.0 negations_per_1k=14.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=15.0
```

## your-step-zh

```
== new (1 runs): 82.5% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=2.0 B2=NA B3=3.0 B4=3.0 B5=NA C1=3.0 C2=3.0 C3=2.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=NA D9=3.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=NA D16=3.0 D17=NA D18=3.0 D19=3.0 D20=NA D21=NA D22=0.0 D23=NA D24=3.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== none (1 runs): 73.0% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=NA B3=2.0 B4=3.0 B5=NA C1=3.0 C2=3.0 C3=3.0 C4=2.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=1.0 D8=NA D9=3.0 D10=2.0 D11=NA D12=2.0 D13=3.0 D14=NA D15=NA D16=1.0 D17=NA D18=3.0 D19=1.0 D20=NA D21=NA D22=0.0 D23=NA D24=3.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (1 runs): 75.8% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=2.0 B2=2.0 B3=3.0 B4=3.0 B5=NA C1=3.0 C2=3.0 C3=2.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=1.0 D8=NA D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=NA D16=3.0 D17=NA D18=0.0 D19=3.0 D20=NA D21=NA D22=0.0 D23=NA D24=2.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=9.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=25.0
none: line_refs=0.0 negations_per_1k=6.2 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=15.0
old: line_refs=0.0 negations_per_1k=7.4 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=18.0
```

## clear-step-zh

```
== new (1 runs): 95.6% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=NA R4=3.0 R5=NA R6=3.0 A1=3.0 A2=3.0 A3=3.0 B1=3.0 B2=NA B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=2.0 D2=3.0 D3=NA D4=3.0 D5=3.0 D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=NA D16=NA D17=3.0 D18=NA D19=NA D20=NA D21=3.0 D22=3.0 D23=3.0 D24=3.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=3.0
== none (1 runs): 75.6% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=NA R4=3.0 R5=NA R6=3.0 A1=3.0 A2=3.0 A3=3.0 B1=2.0 B2=NA B3=1.0 B4=3.0 B5=3.0 C1=2.0 C2=3.0 C3=3.0 C4=2.0 C5=3.0 C6=2.0 D1=2.0 D2=3.0 D3=NA D4=0.0 D5=1.0 D6=NA D7=2.0 D8=NA D9=3.0 D10=NA D11=NA D12=3.0 D13=2.0 D14=NA D15=NA D16=NA D17=NA D18=NA D19=NA D20=NA D21=NA D22=3.0 D23=2.0 D24=2.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=2.0
== old (1 runs): 92.2% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=NA R4=3.0 R5=NA R6=3.0 A1=3.0 A2=3.0 A3=3.0 B1=3.0 B2=NA B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=2.0 C4=2.0 C5=3.0 C6=2.0 D1=2.0 D2=3.0 D3=NA D4=2.0 D5=3.0 D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=NA D16=NA D17=3.0 D18=NA D19=NA D20=NA D21=3.0 D22=3.0 D23=3.0 D24=3.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=3.0
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=10.8 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=14.0
none: line_refs=1.0 negations_per_1k=4.7 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=5.0
old: line_refs=0.0 negations_per_1k=4.9 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=15.0
```

## detail-zh

```
== new (1 runs): 83.3% of points outside E
   red flags: none
   R1=NA R2=NA R3=NA R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=NA C1=3.0 C2=2.0 C3=2.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=NA D9=3.0 D10=3.0 D11=2.0 D12=1.0 D13=3.0 D14=NA D15=2.0 D16=3.0 D17=NA D18=NA D19=3.0 D20=NA D21=NA D22=0.0 D23=NA D24=3.0 D25=0.0 D26=NA E1=2.0 F1=NA F2=NA F3=3.0 F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== none (1 runs): 63.8% of points outside E
   red flags: none
   R1=NA R2=NA R3=NA R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=2.0 B3=2.0 B4=3.0 B5=NA C1=2.0 C2=1.0 C3=1.0 C4=2.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=NA D9=3.0 D10=1.0 D11=1.0 D12=2.0 D13=3.0 D14=NA D15=1.0 D16=3.0 D17=NA D18=NA D19=NA D20=NA D21=NA D22=0.0 D23=NA D24=2.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=2.0 F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (1 runs): 76.5% of points outside E
   red flags: none
   R1=NA R2=NA R3=NA R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=2.0 B4=3.0 B5=NA C1=2.0 C2=2.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=0.0 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=2.0 D9=3.0 D10=3.0 D11=3.0 D12=1.0 D13=3.0 D14=NA D15=2.0 D16=3.0 D17=3.0 D18=NA D19=3.0 D20=NA D21=1.0 D22=0.0 D23=NA D24=3.0 D25=0.0 D26=NA E1=1.0 F1=NA F2=NA F3=3.0 F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=4.0 negations_per_1k=4.2 paragraph_only=0.0 anchors=0.0 drawings=2.0 tables=1.0 quotes=2.0 headings=1.0 ends_asking=0.0 lines=109.0
none: line_refs=0.0 negations_per_1k=4.5 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=0.0 headings=2.0 ends_asking=0.0 lines=138.0
old: line_refs=0.0 negations_per_1k=2.9 paragraph_only=0.0 anchors=0.0 drawings=2.0 tables=1.0 quotes=1.0 headings=1.0 ends_asking=2.0 lines=72.0
```

## only-you-know-zh

```
== new (1 runs): 94.8% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=NA A2=NA A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=3.0 D2=3.0 D3=NA D4=3.0 D5=NA D6=NA D7=3.0 D8=2.0 D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=3.0 D15=NA D16=3.0 D17=2.0 D18=3.0 D19=3.0 D20=3.0 D21=3.0 D22=3.0 D23=NA D24=3.0 D25=1.0 D26=3.0 E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== none (1 runs): 71.3% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=NA A2=NA A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=1.0 C2=3.0 C3=3.0 C4=2.0 C5=3.0 C6=2.0 D1=2.0 D2=2.0 D3=NA D4=0.0 D5=NA D6=NA D7=1.0 D8=1.0 D9=3.0 D10=1.0 D11=NA D12=NA D13=2.0 D14=2.0 D15=NA D16=1.0 D17=2.0 D18=3.0 D19=NA D20=NA D21=2.0 D22=3.0 D23=NA D24=2.0 D25=1.0 D26=2.0 E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (1 runs): 84.9% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=NA A2=NA A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=1.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=3.0 D2=3.0 D3=NA D4=3.0 D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=2.0 D11=NA D12=1.0 D13=3.0 D14=3.0 D15=NA D16=3.0 D17=2.0 D18=3.0 D19=NA D20=1.0 D21=3.0 D22=0.0 D23=NA D24=3.0 D25=2.0 D26=2.0 E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=12.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=24.0
none: line_refs=0.0 negations_per_1k=11.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=7.0
old: line_refs=0.0 negations_per_1k=8.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=21.0
```

## shape-en

```
== new (1 runs): 76.2% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=3.0 R5=NA R6=NA A1=NA A2=NA A3=NA B1=2.0 B2=3.0 B3=2.0 B4=3.0 B5=NA C1=2.0 C2=2.0 C3=2.0 C4=2.0 C5=3.0 C6=1.0 D1=NA D2=1.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=2.0 D9=3.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=1.0 D16=3.0 D17=3.0 D18=3.0 D19=1.0 D20=3.0 D21=1.0 D22=3.0 D23=3.0 D24=3.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== none (1 runs): 76.9% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=3.0 R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=2.0 B3=3.0 B4=3.0 B5=NA C1=2.0 C2=2.0 C3=2.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=2.0 D3=NA D4=NA D5=NA D6=NA D7=NA D8=2.0 D9=3.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=1.0 D16=2.0 D17=3.0 D18=2.0 D19=1.0 D20=NA D21=2.0 D22=2.0 D23=3.0 D24=2.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (1 runs): 88.5% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=3.0 R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=2.0 B3=3.0 B4=3.0 B5=NA C1=2.0 C2=3.0 C3=3.0 C4=2.0 C5=3.0 C6=3.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=2.0 D12=3.0 D13=3.0 D14=3.0 D15=2.0 D16=3.0 D17=3.0 D18=3.0 D19=1.0 D20=3.0 D21=2.0 D22=3.0 D23=NA D24=3.0 D25=1.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: failed, new is more than 3 points under old

Checks:
new: line_refs=0.0 negations_per_1k=3.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=34.0
none: line_refs=0.0 negations_per_1k=2.3 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=1.0 ends_asking=1.0 lines=58.0
old: line_refs=0.0 negations_per_1k=2.2 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=43.0
```

## session-zh

```
== new (1 runs): 90.4% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=3.0 A2=3.0 A3=3.0 B1=2.0 B2=3.0 B3=2.0 B4=1.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=3.0 D2=2.0 D3=NA D4=3.0 D5=3.0 D6=3.0 D7=3.0 D8=2.0 D9=3.0 D10=2.0 D11=3.0 D12=3.0 D13=3.0 D14=NA D15=3.0 D16=3.0 D17=3.0 D18=3.0 D19=3.0 D20=NA D21=3.0 D22=2.0 D23=NA D24=3.0 D25=0.0 D26=NA E1=NA F1=NA F2=3.0 F3=3.0 F4=3.0 G1=NA G2=NA G3=NA G4=NA H1=NA
== none (1 runs): 64.0% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=3.0 A2=3.0 A3=2.0 B1=3.0 B2=2.0 B3=2.0 B4=2.0 B5=3.0 C1=3.0 C2=2.0 C3=2.0 C4=2.0 C5=3.0 C6=2.0 D1=3.0 D2=3.0 D3=NA D4=0.0 D5=3.0 D6=0.0 D7=1.0 D8=2.0 D9=1.0 D10=1.0 D11=3.0 D12=1.0 D13=3.0 D14=NA D15=2.0 D16=1.0 D17=3.0 D18=2.0 D19=NA D20=NA D21=3.0 D22=0.0 D23=NA D24=2.0 D25=1.0 D26=NA E1=NA F1=NA F2=0.0 F3=2.0 F4=0.0 G1=NA G2=NA G3=NA G4=NA H1=NA
== old (1 runs): 95.0% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=3.0 A2=3.0 A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=3.0 D2=3.0 D3=NA D4=3.0 D5=3.0 D6=3.0 D7=2.0 D8=3.0 D9=3.0 D10=2.0 D11=3.0 D12=3.0 D13=3.0 D14=3.0 D15=3.0 D16=3.0 D17=3.0 D18=3.0 D19=2.0 D20=3.0 D21=3.0 D22=2.0 D23=NA D24=3.0 D25=2.0 D26=NA E1=NA F1=NA F2=3.0 F3=2.0 F4=3.0 G1=NA G2=NA G3=NA G4=NA H1=NA
bar: failed, new is more than 3 points under old

Checks:
new: line_refs=0.0 negations_per_1k=8.9 paragraph_only=0.0 anchors=1.0 drawings=3.0 tables=1.0 quotes=2.0 headings=0.0 ends_asking=4.0 lines=80.0
none: line_refs=0.0 negations_per_1k=6.1 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=2.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=51.0
old: line_refs=0.0 negations_per_1k=8.0 paragraph_only=0.0 anchors=1.0 drawings=3.0 tables=1.0 quotes=1.0 headings=0.0 ends_asking=4.0 lines=86.0
```

## better-way-zh

```
== new (1 runs): 90.3% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=NA R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=2.0 C3=2.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=3.0 D6=NA D7=3.0 D8=NA D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=NA D16=3.0 D17=NA D18=NA D19=3.0 D20=NA D21=NA D22=2.0 D23=3.0 D24=3.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== none (1 runs): 68.2% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=NA R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=1.0 B3=2.0 B4=2.0 B5=2.0 C1=1.0 C2=2.0 C3=3.0 C4=2.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=3.0 D6=NA D7=1.0 D8=NA D9=3.0 D10=NA D11=NA D12=3.0 D13=2.0 D14=NA D15=NA D16=1.0 D17=NA D18=NA D19=NA D20=NA D21=NA D22=2.0 D23=2.0 D24=2.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (1 runs): 85.1% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=NA R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=2.0 C3=2.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=0.0 D3=NA D4=NA D5=3.0 D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=3.0 D15=NA D16=3.0 D17=3.0 D18=NA D19=3.0 D20=3.0 D21=0.0 D22=2.0 D23=3.0 D24=3.0 D25=0.0 D26=NA E1=NA F1=NA F2=NA F3=NA F4=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=3.6 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=34.0
none: line_refs=0.0 negations_per_1k=1.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=20.0
old: line_refs=0.0 negations_per_1k=3.1 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=27.0
```

## vague-zh

```
== new (1 runs): 88.9% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=2.0 A2=3.0 A3=3.0 B1=3.0 B2=2.0 B3=3.0 B4=3.0 B5=3.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=2.0 D2=3.0 D3=NA D4=3.0 D5=3.0 D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=3.0 D12=NA D13=3.0 D14=3.0 D15=NA D16=3.0 D17=2.0 D18=2.0 D19=NA D20=3.0 D21=3.0 D22=3.0 D23=NA D24=3.0 D25=0.0 D26=3.0 E1=NA F1=NA F2=NA F3=NA F4=NA G1=3.0 G2=0.0 G3=NA G4=NA H1=NA
== none (1 runs): 52.7% of points outside E
   red flags: R3 x1
   R1=3.0 R2=3.0 R3=0.0 R4=NA R5=NA R6=3.0 A1=2.0 A2=3.0 A3=1.0 B1=2.0 B2=2.0 B3=2.0 B4=3.0 B5=3.0 C1=1.0 C2=1.0 C3=2.0 C4=2.0 C5=3.0 C6=1.0 D1=3.0 D2=1.0 D3=NA D4=0.0 D5=3.0 D6=0.0 D7=1.0 D8=NA D9=3.0 D10=1.0 D11=NA D12=NA D13=3.0 D14=NA D15=NA D16=1.0 D17=NA D18=0.0 D19=NA D20=NA D21=NA D22=1.0 D23=NA D24=2.0 D25=0.0 D26=1.0 E1=NA F1=NA F2=NA F3=NA F4=NA G1=1.0 G2=0.0 G3=NA G4=NA H1=NA
== old (1 runs): 89.8% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=2.0 A2=3.0 A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 C1=1.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=2.0 D2=3.0 D3=NA D4=3.0 D5=3.0 D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=NA D13=3.0 D14=3.0 D15=NA D16=3.0 D17=2.0 D18=3.0 D19=3.0 D20=2.0 D21=3.0 D22=3.0 D23=NA D24=3.0 D25=0.0 D26=2.0 E1=NA F1=NA F2=NA F3=NA F4=NA G1=3.0 G2=3.0 G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=13.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=31.0
none: line_refs=0.0 negations_per_1k=16.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=0.0 lines=12.0
old: line_refs=0.0 negations_per_1k=10.7 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=44.0
```
