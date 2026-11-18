# Roadmap

**Current checkpoint**: [CP1: The rubric can be relied on](#cp1-the-rubric-can-be-relied-on). 0.1.18 is released since 2026-11-18, and the rule file rebuilt on that day sits on master unreleased. No eval has seen the rules of the last three releases, and no paid run is under way.

The order was agreed on 2026-11-11: first make the rubric something we can rely on, then go back to the rules.

---

## Summary

```
Roadmap
├── 🟨 CP1: The rubric can be relied on — every line that judges a rule in force is checked
├── ⬜ CP2: The rules in use are measured — one benchmark against no plugin
├── ⬜ CP3: A release whose rules passed the eval — the first since 0.1.15
└── ⬜ CP4: Waiting for a need — work that needs time or a reason
```

---

## CP1: The rubric can be relied on

**Status**: 🟨

The rubric was checked on all 117 lines on 2026-11-13. Since then four lines were reworded, the rule file was rebuilt, and ten lines still waver. The paid checks wait for a budget.

**Delivers** (9):

- [I1: Check the reworded rubric lines](ISSUES.md#i1-check-the-reworded-rubric-lines)
- [I2: Run the red flag check on its 8 cases](ISSUES.md#i2-run-the-red-flag-check-on-its-8-cases)
- [I3: Check how steady the strong judge is](ISSUES.md#i3-check-how-steady-the-strong-judge-is)
- [I4: Settle the ten rubric lines that waver](ISSUES.md#i4-settle-the-ten-rubric-lines-that-waver)
- [I5: Narrow the six rubric lines that fire on what the rules ask](ISSUES.md#i5-narrow-the-six-rubric-lines-that-fire-on-what-the-rules-ask)
- [I6: Bring the rubric in line with the recap](ISSUES.md#i6-bring-the-rubric-in-line-with-the-recap)
- [I7: Write a red flag for a reply in another language](ISSUES.md#i7-write-a-red-flag-for-a-reply-in-another-language)
- [I8: Make the bar of the table of lines a share of the replies](ISSUES.md#i8-make-the-bar-of-the-table-of-lines-a-share-of-the-replies)
- [I13: Bring the rubric in line with the rebuilt rule file](ISSUES.md#i13-bring-the-rubric-in-line-with-the-rebuilt-rule-file)

**Exit criteria** (1):

- **Measures**
  - [M5: Stable answers of the rubric](GOALS.md#m5-stable-answers-of-the-rubric): the value after the checks, with its date

2 open questions:

- [What ends the rubric checkpoint?](TODO.md#p1discussion-what-ends-the-rubric-checkpoint)
- [What budget do the paid runs get?](TODO.md#p1discussion-what-budget-do-the-paid-runs-get)

---

## CP2: The rules in use are measured

**Status**: ⬜

One benchmark runs the rules of `HEAD` against no plugin, and its report is read against every rule change that went out with no eval.

**Delivers** (3):

- [I9: Run the benchmark of the rules in use](ISSUES.md#i9-run-the-benchmark-of-the-rules-in-use)
- [I10: Read the benchmark against the rule changes no eval has seen](ISSUES.md#i10-read-the-benchmark-against-the-rule-changes-no-eval-has-seen)
- [I11: Find out why drift is not said on Sonnet](ISSUES.md#i11-find-out-why-drift-is-not-said-on-sonnet)

**Exit criteria** (3):

- **Comparisons**
  - [C1: Replies with the plugin against replies with none](GOALS.md#c1-replies-with-the-plugin-against-replies-with-none): the result of the run, with its date
- **Measures**
  - [M1: Replies that say what they did not check](GOALS.md#m1-replies-that-say-what-they-did-not-check): the value of the run
  - [M2: Lines of a reply](GOALS.md#m2-lines-of-a-reply): the value of the run

1 open question:

- [What does the benchmark leave out?](TODO.md#p1discussion-what-does-the-benchmark-leave-out)

---

## CP3: A release whose rules passed the eval

**Status**: ⬜

The next release ships rules that ran against the last release first. It carries the rebuilt rule file.

**Exit criteria** (3):

- **Objectives**
  - [O1: A release clears the bar](GOALS.md#o1-a-release-clears-the-bar)
- **Constraints**
  - [R1: The Codex rules match the output style](GOALS.md#r1-the-codex-rules-match-the-output-style)
  - [R2: The plugin loads in Claude Code](GOALS.md#r2-the-plugin-loads-in-claude-code)

---

## CP4: Waiting for a need

**Status**: ⬜

Work that needs time to pass or a reason to start.

**Delivers** (1):

- [I12: Scan the owner's real sessions against the baseline](ISSUES.md#i12-scan-the-owners-real-sessions-against-the-baseline)

**Exit criteria** (1):

- **Do not hold the release**
  - [M3: The owner's real sessions](GOALS.md#m3-the-owners-real-sessions)
