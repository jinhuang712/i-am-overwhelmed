# Eval 2026-11-11-1b563fa-vs-f6f2f69-opus-5-5

- old: `master` (1b563fa)
- new: `exp/news-shape` (f6f2f69)
- model: claude-opus-5-5, effort medium, judge claude-opus-5-5
- runs: {'done': 2, 'skipped': 34}
- spent: $5.77 of $6.96

## fix-test-zh

```
== new (2 runs): 89.0% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=3.0 A2=3.0 A3=3.0 B1=2.5 B2=2.5 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=3.0 C2=2.5 C3=2.5 C4=2.5 C5=3.0 C6=3.0 D1=3.0 D2=3.0 D3=NA D4=2.5 D5=3.0 D6=3.0 D7=2.0 D8=2.0 D9=3.0 D10=3.0 D11=3.0 D12=2.5 D13=3.0 D14=3.0 D15=NA D16=3.0 D17=3.0 D18=NA D19=NA D20=2.0 D21=2.0 D22=1.5 D23=NA D24=2.0 D26=NA D27=2.0 D28=2.0 D29=2.0 D30=3.0 D31=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 86.9% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=3.0 A2=3.0 A3=3.0 B1=2.5 B2=2.0 B3=2.5 B4=2.5 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=3.0 C4=2.0 C5=3.0 C6=3.0 D1=3.0 D2=3.0 D3=NA D4=2.5 D5=3.0 D6=3.0 D7=1.5 D8=NA D9=3.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=3.0 D16=3.0 D17=NA D18=NA D19=3.0 D20=NA D21=NA D22=2.0 D23=NA D24=2.0 D26=NA D27=2.0 D28=1.0 D29=1.5 D30=3.0 D31=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=7.4 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.5 quotes=0.0 headings=0.0 ends_asking=0.5 lines=35.5
old: line_refs=0.0 negations_per_1k=6.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=0.0 lines=28.5
```

## chat-zh

```
== new (2 runs): 92.2% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=2.0 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=2.5 D9=3.0 D10=3.0 D11=NA D12=NA D13=3.0 D14=3.0 D15=2.0 D16=3.0 D17=3.0 D18=3.0 D19=2.5 D20=3.0 D21=3.0 D22=3.0 D23=3.0 D24=2.0 D26=NA D27=3.0 D28=3.0 D29=2.0 D30=2.5 D31=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 84.4% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=1.5 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=1.0 D9=3.0 D10=2.0 D11=NA D12=NA D13=3.0 D14=3.0 D15=2.0 D16=3.0 D17=3.0 D18=3.0 D19=2.0 D20=3.0 D21=3.0 D22=NA D23=3.0 D24=2.0 D26=NA D27=1.5 D28=1.0 D29=2.0 D30=2.0 D31=3.0 E1=NA E3=3.0 F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=12.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=1.0 lines=23.5
old: line_refs=0.0 negations_per_1k=15.3 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=1.0 lines=23.0
```

## multi-turn-zh

```
== new (2 runs): 91.1% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=3.0 R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.5 D1=NA D2=2.5 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=1.5 D9=3.0 D10=3.0 D11=3.0 D12=3.0 D13=3.0 D14=3.0 D15=2.0 D16=3.0 D17=3.0 D18=3.0 D19=2.0 D20=3.0 D21=2.0 D22=1.0 D23=NA D24=3.0 D26=NA D27=3.0 D28=2.5 D29=3.0 D30=3.0 D31=3.0 E1=NA E3=NA F1=3.0 F2=2.0 F3=3.0 F4=2.0 F5=2.5 G1=NA G2=NA G3=NA G4=NA H1=3.0
== old (2 runs): 87.2% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=3.0 R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=2.5 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=1.0 D9=3.0 D10=3.0 D11=3.0 D12=3.0 D13=3.0 D14=3.0 D15=2.0 D16=3.0 D17=3.0 D18=2.5 D19=2.0 D20=3.0 D21=2.5 D22=1.0 D23=NA D24=2.5 D26=NA D27=3.0 D28=1.0 D29=3.0 D30=3.0 D31=3.0 E1=NA E3=NA F1=3.0 F2=2.5 F3=3.0 F4=1.0 F5=2.0 G1=NA G2=NA G3=NA G4=NA H1=2.0
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=10.6 paragraph_only=0.0 anchors=1.0 drawings=2.0 tables=1.0 quotes=2.0 headings=0.0 ends_asking=2.5 lines=58.0
old: line_refs=0.0 negations_per_1k=8.9 paragraph_only=0.0 anchors=1.0 drawings=2.5 tables=1.0 quotes=1.0 headings=0.0 ends_asking=2.0 lines=69.5
```

## design-flaw-zh

```
== new (2 runs): 93.9% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=3.0 A1=2.5 A2=3.0 A3=3.0 B1=3.0 B2=2.0 B3=3.0 B4=2.0 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=2.5 C4=3.0 C5=3.0 C6=3.0 D1=2.5 D2=3.0 D3=NA D4=3.0 D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=3.0 D12=3.0 D13=3.0 D14=3.0 D15=NA D16=3.0 D17=2.0 D18=3.0 D19=NA D20=3.0 D21=3.0 D22=3.0 D23=3.0 D24=2.5 D26=NA D27=3.0 D28=2.0 D29=3.0 D30=2.0 D31=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=3.0
== old (2 runs): 91.0% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=3.0 A1=3.0 A2=3.0 A3=3.0 B1=2.5 B2=2.0 B3=3.0 B4=2.0 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=3.0 D1=2.5 D2=2.5 D3=NA D4=3.0 D5=NA D6=NA D7=2.5 D8=1.0 D9=3.0 D10=3.0 D11=NA D12=NA D13=3.0 D14=3.0 D15=NA D16=3.0 D17=2.0 D18=3.0 D19=NA D20=2.5 D21=3.0 D22=3.0 D23=3.0 D24=2.5 D26=NA D27=3.0 D28=2.0 D29=3.0 D30=2.0 D31=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=3.0
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=12.5 paragraph_only=0.0 anchors=0.0 drawings=0.0 tables=1.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=22.0
old: line_refs=0.0 negations_per_1k=10.3 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.0 headings=0.0 ends_asking=1.0 lines=24.5
```

## shape-zh

```
== new (2 runs): 90.7% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=2.0 B4=3.0 B5=NA B6=NA C1=2.5 C2=3.0 C3=2.0 C4=3.0 C5=3.0 C6=2.5 D1=NA D2=3.0 D3=3.0 D4=NA D5=NA D6=NA D7=2.5 D8=NA D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=1.5 D16=3.0 D17=NA D18=NA D19=2.0 D20=NA D21=NA D22=3.0 D23=NA D24=2.0 D26=NA D27=2.5 D28=3.0 D29=3.0 D30=3.0 D31=3.0 E1=NA E3=2.0 F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 82.1% of points outside E
   red flags: none
   R1=NA R2=3.0 R3=3.0 R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=3.0 B2=1.5 B3=2.5 B4=3.0 B5=NA B6=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.5 D1=NA D2=2.5 D3=3.0 D4=NA D5=NA D6=NA D7=1.5 D8=2.0 D9=3.0 D10=2.5 D11=NA D12=3.0 D13=3.0 D14=NA D15=1.0 D16=3.0 D17=3.0 D18=NA D19=3.0 D20=NA D21=0.0 D22=3.0 D23=NA D24=2.0 D26=NA D27=1.5 D28=0.5 D29=3.0 D30=2.0 D31=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=2.3 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=24.5
old: line_refs=0.0 negations_per_1k=2.2 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.0 ends_asking=0.5 lines=29.0
```

## fact-zh

```
== new (2 runs): 93.8% of points outside E
   red flags: none
   R1=NA R2=NA R3=NA R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=NA B2=0.5 B3=NA B4=2.5 B5=NA B6=NA C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=NA D1=NA D2=3.0 D3=3.0 D4=NA D5=NA D6=NA D7=3.0 D8=NA D9=3.0 D10=3.0 D11=2.5 D12=3.0 D13=3.0 D14=NA D15=3.0 D16=3.0 D17=NA D18=NA D19=3.0 D20=NA D21=NA D22=3.0 D23=NA D24=3.0 D26=NA D27=3.0 D28=2.5 D29=2.5 D30=3.0 D31=3.0 E1=NA E3=2.0 F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 79.6% of points outside E
   red flags: none
   R1=NA R2=NA R3=NA R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=NA B2=0.5 B3=NA B4=2.5 B5=NA B6=NA C1=1.5 C2=3.0 C3=3.0 C4=2.5 C5=3.0 C6=NA D1=NA D2=3.0 D3=3.0 D4=NA D5=NA D6=NA D7=2.0 D8=NA D9=3.0 D10=3.0 D11=3.0 D12=3.0 D13=3.0 D14=NA D15=2.5 D16=3.0 D17=NA D18=NA D19=3.0 D20=NA D21=NA D22=3.0 D23=NA D24=1.5 D26=NA D27=1.0 D28=0.0 D29=1.5 D30=2.5 D31=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=21.0 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=0.5 headings=0.0 ends_asking=0.0 lines=24.0
old: line_refs=0.0 negations_per_1k=24.5 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=1.0 quotes=0.5 headings=0.0 ends_asking=0.0 lines=19.0
```

## your-step-zh

```
== new (2 runs): 91.2% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=3.0 C2=3.0 C3=3.0 C4=2.5 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=NA D9=3.0 D10=2.5 D11=NA D12=2.0 D13=3.0 D14=NA D15=NA D16=2.0 D17=NA D18=3.0 D19=3.0 D20=NA D21=NA D22=1.5 D23=NA D24=3.0 D26=NA D27=2.5 D28=3.0 D29=3.0 D30=3.0 D31=3.0 E1=NA E3=2.0 F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 70.4% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=NA R5=NA R6=3.0 A1=NA A2=NA A3=NA B1=2.0 B2=1.0 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=1.5 C2=2.0 C3=1.5 C4=2.0 C5=2.5 C6=2.0 D1=NA D2=2.0 D3=NA D4=NA D5=NA D6=NA D7=1.5 D8=NA D9=2.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=NA D15=NA D16=3.0 D17=NA D18=3.0 D19=1.5 D20=NA D21=NA D22=1.5 D23=NA D24=1.0 D26=NA D27=1.5 D28=1.0 D29=1.5 D30=3.0 D31=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=10.6 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=0.5 headings=0.0 ends_asking=0.0 lines=22.0
old: line_refs=0.0 negations_per_1k=8.8 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.0 lines=25.5
```

## detail-zh

```
== new (2 runs): 80.4% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=NA R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=NA B2=3.0 B3=2.0 B4=3.0 B5=NA B6=NA C1=1.5 C2=2.5 C3=2.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=NA D9=2.0 D10=2.0 D11=2.5 D12=2.0 D13=3.0 D14=NA D15=2.5 D16=2.5 D17=NA D18=NA D19=2.5 D20=NA D21=NA D22=1.0 D23=NA D24=2.0 D26=NA D27=3.0 D28=1.5 D29=2.0 D30=3.0 D31=2.0 E1=2.0 E3=2.5 F1=NA F2=NA F3=3.0 F4=NA F5=3.0 G1=NA G2=NA G3=NA G4=NA H1=NA
== old (2 runs): 75.6% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=NA R4=NA R5=NA R6=NA A1=NA A2=NA A3=NA B1=NA B2=1.5 B3=3.0 B4=3.0 B5=NA B6=NA C1=2.5 C2=2.0 C3=2.0 C4=3.0 C5=3.0 C6=3.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=1.5 D8=NA D9=3.0 D10=2.5 D11=3.0 D12=2.0 D13=3.0 D14=NA D15=2.0 D16=3.0 D17=NA D18=NA D19=3.0 D20=NA D21=NA D22=1.5 D23=NA D24=2.0 D26=NA D27=1.5 D28=1.0 D29=2.0 D30=2.5 D31=2.0 E1=NA E3=NA F1=NA F2=NA F3=2.0 F4=NA F5=0.0 G1=NA G2=NA G3=NA G4=NA H1=NA
bar: passed

Checks:
new: line_refs=0.5 negations_per_1k=3.5 paragraph_only=0.0 anchors=0.0 drawings=2.0 tables=2.0 quotes=2.0 headings=1.0 ends_asking=0.0 lines=82.0
old: line_refs=0.0 negations_per_1k=5.0 paragraph_only=0.0 anchors=0.0 drawings=2.0 tables=1.0 quotes=2.0 headings=1.0 ends_asking=0.0 lines=91.0
```

## better-way-zh

```
== new (2 runs): 82.8% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=3.0 A1=NA A2=NA A3=NA B1=3.0 B2=2.5 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=1.5 C2=2.5 C3=2.0 C4=2.5 C5=3.0 C6=2.0 D1=NA D2=2.5 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=2.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=3.0 D15=NA D16=3.0 D17=3.0 D18=3.0 D19=2.0 D20=1.0 D21=1.0 D22=2.0 D23=3.0 D24=2.0 D26=NA D27=2.5 D28=1.0 D29=1.5 D30=3.0 D31=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=2.0
== old (2 runs): 84.2% of points outside E
   red flags: none
   R1=3.0 R2=3.0 R3=3.0 R4=3.0 R5=NA R6=3.0 A1=NA A2=NA A3=NA B1=3.0 B2=1.0 B3=3.0 B4=3.0 B5=3.0 B6=NA C1=3.0 C2=2.5 C3=2.5 C4=2.5 C5=3.0 C6=2.0 D1=NA D2=2.5 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=1.0 D9=3.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=3.0 D15=NA D16=2.5 D17=3.0 D18=NA D19=2.0 D20=3.0 D21=1.0 D22=2.0 D23=3.0 D24=3.0 D26=NA D27=2.0 D28=1.0 D29=2.5 D30=2.5 D31=3.0 E1=NA E3=NA F1=NA F2=NA F3=NA F4=NA F5=NA G1=NA G2=NA G3=NA G4=NA H1=3.0
bar: passed

Checks:
new: line_refs=0.0 negations_per_1k=7.9 paragraph_only=0.0 anchors=0.0 drawings=1.0 tables=0.0 quotes=0.5 headings=0.5 ends_asking=0.5 lines=31.0
old: line_refs=0.0 negations_per_1k=5.2 paragraph_only=0.0 anchors=0.0 drawings=0.5 tables=0.0 quotes=1.0 headings=0.0 ends_asking=0.5 lines=30.5
```
