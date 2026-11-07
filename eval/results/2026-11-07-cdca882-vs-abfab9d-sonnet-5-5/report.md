# Eval 2026-11-07-cdca882-vs-abfab9d-sonnet-5-5

- old: `cdca882` (cdca882)
- new: `abfab9d` (abfab9d)
- model: claude-sonnet-5-5, effort medium, judge claude-opus-5-5
- runs: {'done': 3, 'skipped': 1}
- spent: $0.42 of $3.00

## chat-en

```
== new (1 runs): 87.7% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=3.0 B3=3.0 B4=2.0 C1=3.0 C2=2.0 C3=2.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=3.0 D6=NA D7=3.0 D8=1.0 D9=3.0 D10=2.0 D11=NA D12=3.0 D13=3.0 D14=3.0 E1=NA E2=NA E3=NA F1=NA F2=NA F3=NA G1=NA G2=NA G3=NA G4=NA H1=NA
== old (1 runs): 88.9% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=2.0 B3=3.0 B4=2.0 C1=2.0 C2=3.0 C3=2.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=NA D9=3.0 D10=3.0 D11=NA D12=NA D13=3.0 D14=NA E1=NA E2=NA E3=NA F1=NA F2=NA F3=NA G1=NA G2=NA G3=NA G4=NA H1=NA

Checks:
new: line_refs=0.0 negations_per_1k=1.2 paragraph_only=0.0
old: line_refs=0.0 negations_per_1k=4.1 paragraph_only=0.0
```

## design-flaw-zh

```
== new (1 runs): 89.5% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=1.0 B3=3.0 B4=1.0 C1=3.0 C2=3.0 C3=2.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=3.0 D3=NA D4=NA D5=NA D6=NA D7=3.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=3.0 E1=NA E2=3.0 E3=NA F1=NA F2=NA F3=NA G1=NA G2=NA G3=NA G4=NA H1=3.0
== old (1 runs): 89.5% of points outside E
   A1=NA A2=NA A3=NA B1=3.0 B2=2.0 B3=3.0 B4=2.0 C1=3.0 C2=3.0 C3=3.0 C4=3.0 C5=3.0 C6=2.0 D1=NA D2=1.0 D3=NA D4=NA D5=NA D6=NA D7=2.0 D8=3.0 D9=3.0 D10=3.0 D11=NA D12=3.0 D13=3.0 D14=3.0 E1=NA E2=3.0 E3=NA F1=NA F2=NA F3=NA G1=NA G2=NA G3=NA G4=NA H1=3.0

Checks:
new: line_refs=0.0 negations_per_1k=11.8 paragraph_only=0.0
old: line_refs=0.0 negations_per_1k=9.6 paragraph_only=0.0
```
