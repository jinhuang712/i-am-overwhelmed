# Eval 2026-11-07-cdca882-vs-5a5747d-sonnet-5-5

- old: `cdca882` (cdca882)
- new: `5a5747d` (5a5747d)
- model: claude-sonnet-5-5, effort medium, judge claude-opus-5-5
- runs: {'skipped': 52, 'stopped': 8}
- spent: $8.82 of $9.40
- incomplete: the budget stopped some runs

## fix-test-zh

```
== new (5 runs): 91.5% of points outside E
   A1=2.8 A2=2.8 A3=3.0 B1=2.6 B2=2.4 B3=2.8 B4=2.6 C1=3.0 C2=2.8 C3=2.4 C4=3.0 C5=3.0 C6=3.0 D1=3.0 D2=2.8 D3=NA D4=2.8 D5=3.0 D6=3.0 D7=3.0 D8=1.3 D9=2.4 D10=1.8 D11=NA D12=3.0 D13=3.0 D14=2.7 E1=NA E2=NA E3=NA F1=NA F2=NA F3=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (4 runs): 90.4% of points outside E
   A1=3.0 A2=2.8 A3=2.8 B1=2.2 B2=2.0 B3=2.8 B4=2.8 C1=3.0 C2=3.0 C3=2.5 C4=3.0 C5=3.0 C6=3.0 D1=3.0 D2=2.5 D3=NA D4=2.8 D5=3.0 D6=3.0 D7=2.8 D8=1.3 D9=2.2 D10=2.2 D11=NA D12=3.0 D13=3.0 D14=3.0 E1=NA E2=NA E3=NA F1=NA F2=NA F3=NA G1=NA G2=NA G3=NA G4=NA H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=6.8 paragraph_only=0.0
old: line_refs=0.0 negations_per_1k=7.6 paragraph_only=0.0
```

## chat-en

```
== new (4 runs): 89.4% of points outside E
   A1=NA A2=NA A3=NA B1=2.8 B2=2.2 B3=3.0 B4=2.8 C1=3.0 C2=2.2 C3=2.5 C4=2.8 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.5 D8=2.0 D9=3.0 D10=3.0 D11=NA D12=2.0 D13=3.0 D14=3.0 E1=NA E2=NA E3=NA F1=NA F2=NA F3=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (4 runs): 84.8% of points outside E
   A1=NA A2=NA A3=NA B1=2.0 B2=1.0 B3=3.0 B4=2.2 C1=3.0 C2=2.8 C3=2.8 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=1.2 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=2.7 D9=3.0 D10=2.8 D11=NA D12=NA D13=3.0 D14=3.0 E1=NA E2=NA E3=NA F1=NA F2=NA F3=NA G1=NA G2=NA G3=NA G4=NA H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=2.5 paragraph_only=0.0
old: line_refs=0.0 negations_per_1k=5.1 paragraph_only=0.0
```

## chat-zh

```
== new (5 runs): 90.2% of points outside E
   A1=NA A2=NA A3=NA B1=2.8 B2=3.0 B3=3.0 B4=2.4 C1=3.0 C2=2.8 C3=2.2 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=2.4 D8=2.2 D9=3.0 D10=2.2 D11=NA D12=NA D13=3.0 D14=3.0 E1=NA E2=NA E3=1.0 F1=NA F2=NA F3=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (4 runs): 85.6% of points outside E
   A1=NA A2=NA A3=NA B1=2.2 B2=1.5 B3=3.0 B4=2.2 C1=3.0 C2=3.0 C3=2.8 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=2.2 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=1.0 D9=3.0 D10=2.8 D11=NA D12=NA D13=3.0 D14=3.0 E1=NA E2=NA E3=NA F1=NA F2=NA F3=NA G1=NA G2=NA G3=NA G4=NA H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=14.9 paragraph_only=0.0
old: line_refs=0.0 negations_per_1k=12.8 paragraph_only=0.0
```

## multi-turn-zh

```
== new (4 runs): 87.1% of points outside E
   A1=NA A2=NA A3=NA B1=2.0 B2=2.8 B3=3.0 B4=2.0 C1=2.2 C2=2.8 C3=2.2 C4=3.0 C5=3.0 C6=2.5 D1=NA D2=2.8 D3=NA D4=NA D5=NA D6=NA D7=2.8 D8=2.0 D9=3.0 D10=2.2 D11=NA D12=3.0 D13=3.0 D14=3.0 E1=2.2 E2=NA E3=NA F1=2.5 F2=2.8 F3=2.0 G1=NA G2=NA G3=NA G4=NA H1=3.0
== old (5 runs): 81.2% of points outside E
   A1=NA A2=NA A3=NA B1=2.2 B2=2.0 B3=3.0 B4=2.2 C1=2.2 C2=3.0 C3=2.8 C4=3.0 C5=2.8 C6=2.4 D1=NA D2=1.6 D3=NA D4=NA D5=NA D6=NA D7=2.4 D8=1.0 D9=3.0 D10=2.8 D11=NA D12=3.0 D13=3.0 D14=2.4 E1=2.2 E2=NA E3=NA F1=2.4 F2=1.8 F3=1.6 G1=NA G2=NA G3=NA G4=NA H1=3.0

Checks:
new: line_refs=0.0 negations_per_1k=9.6 paragraph_only=0.0
old: line_refs=0.0 negations_per_1k=8.4 paragraph_only=0.0
```

## many-items-zh

```
== new (4 runs): 91.7% of points outside E
   A1=2.2 A2=NA A3=3.0 B1=3.0 B2=3.0 B3=3.0 B4=2.8 C1=3.0 C2=3.0 C3=2.0 C4=3.0 C5=2.8 C6=2.0 D1=2.2 D2=3.0 D3=2.2 D4=3.0 D5=3.0 D6=NA D7=2.2 D8=3.0 D9=3.0 D10=2.0 D11=2.8 D12=3.0 D13=3.0 D14=3.0 E1=NA E2=3.0 E3=NA F1=NA F2=NA F3=3.0 G1=3.0 G2=3.0 G3=3.0 G4=2.2 H1=NA
== old (5 runs): 73.8% of points outside E
   A1=2.2 A2=3.0 A3=1.0 B1=3.0 B2=2.6 B3=3.0 B4=1.6 C1=3.0 C2=2.0 C3=2.0 C4=2.8 C5=2.2 C6=2.0 D1=3.0 D2=2.4 D3=1.0 D4=3.0 D5=3.0 D6=2.8 D7=2.0 D8=2.4 D9=3.0 D10=2.0 D11=2.2 D12=3.0 D13=3.0 D14=2.6 E1=NA E2=3.0 E3=NA F1=NA F2=NA F3=1.0 G1=2.8 G2=0.2 G3=0.0 G4=0.0 H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=8.3 paragraph_only=0.0
old: line_refs=0.0 negations_per_1k=10.7 paragraph_only=0.0
```

## design-flaw-zh

```
== new (4 runs): 83.8% of points outside E
   A1=1.2 A2=NA A3=2.8 B1=2.0 B2=2.2 B3=3.0 B4=2.0 C1=3.0 C2=2.8 C3=2.8 C4=3.0 C5=3.0 C6=2.5 D1=2.7 D2=3.0 D3=NA D4=2.2 D5=3.0 D6=0.7 D7=2.5 D8=2.8 D9=3.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=2.8 E1=NA E2=NA E3=NA F1=NA F2=NA F3=NA G1=NA G2=NA G3=NA G4=NA H1=1.8
== old (4 runs): 83.0% of points outside E
   A1=1.5 A2=NA A3=3.0 B1=2.2 B2=1.8 B3=2.5 B4=2.5 C1=3.0 C2=2.8 C3=2.2 C4=3.0 C5=3.0 C6=2.2 D1=3.0 D2=3.0 D3=NA D4=2.5 D5=3.0 D6=2.5 D7=2.2 D8=1.8 D9=3.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=2.2 E1=NA E2=NA E3=NA F1=NA F2=NA F3=NA G1=NA G2=NA G3=NA G4=NA H1=1.2

Checks:
new: line_refs=0.0 negations_per_1k=11.4 paragraph_only=0.0
old: line_refs=0.0 negations_per_1k=5.2 paragraph_only=0.0
```
