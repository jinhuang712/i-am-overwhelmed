# Goals

The eval tool in [`eval/`](../eval/README.md) checks most goals: it runs the same tasks under two sets of rules, blinds the replies and has model judges answer the lines of the rubric. A paid run needs a budget the owner names. The two constraints are checked by the unit tests and by CI on every push.

---

## Summary

```
Goals
├── Objectives
│   └── ⬜ O1: A release clears the bar — no red flag and no task that falls
├── Comparisons
│   └── 82.1 against 77.2 C1: Replies with the plugin against replies with none — the overall score
├── Measures
│   ├── 70% M1: Replies that say what they did not check — a share of the replies
│   ├── open M2: Lines of a reply — the length the reader meets
│   ├── open M3: The owner's real sessions — the signal that needs no judge
│   ├── 2,399 M4: Words of the rule file — what every request carries
│   └── 92% M5: Stable answers of the rubric — how far a judge can be relied on
└── Constraints
    ├── ✅ R1: The Codex rules match the output style — two places may differ
    └── ✅ R2: The plugin loads in Claude Code — installed and enabled
```

---

## Goals

---

### Objectives

---

#### O1: A release clears the bar

The new rules run against the last release on the same tasks and are judged blind.

**Want**: Trust what a reply says. It also answers the risk that a rule is not followed.

**Checks**: [the rule file](../plugin/output-styles/i-am-overwhelmed.md)

**Acceptance**: No reply of the new version has a red flag. On every task "clean" is at most 2 points under the old version, where "clean" is the share of bad signs the replies of a task do not show.

**Status**: ⬜

The releases 0.1.16, 0.1.17 and 0.1.18 went out with no run of this check, by the owner's choice. [I9: Run the benchmark of the rules in use](ISSUES.md#i9-run-the-benchmark-of-the-rules-in-use) holds the run.

---

### Comparisons

---

#### C1: Replies with the plugin against replies with none

The same tasks run with the plugin and with no plugin.

**Want**: Every want in the proposal, since the score weighs all eight words.

**Checks**: [the rule file](../plugin/output-styles/i-am-overwhelmed.md)

**Against**: Claude Code with no plugin, on the same model.

**How**: 19 tasks with 3 runs each give 57 replies a side. Judges answer the yes or no lines of [the rubric](../eval/rubric-yesno.md) on blind samples. The points are of 100.

**Formula**:

```
word     = points its lines won / points they could give
quality  = mean of the words of a reply, by weight
score    = mean quality x (1 - 0.5 x share of replies with a red flag)
C1       = score with the plugin - score with no plugin
```

A gap under 2.5 points is no difference, since the same version scored that far apart in two runs on 2026-11-11.

**Last result**: 82.1 against 77.2, a gap of 4.9, on 2026-11-11. It ran on Claude Opus 5.5 with the rules of commit `13a35d4`, and [the report](../eval/results/2026-11-11-none-vs-13a35d4-opus-5-5/report.md) has every task.

---

### Measures

---

#### M1: Replies that say what they did not check

One line of the rubric, read as a share.

**Want**: Trust what a reply says.

**Checks**: [the rule file](../plugin/output-styles/i-am-overwhelmed.md)

**How**: The 57 replies a side of the run behind C1.

**Formula**:

```
M1 = replies that say what they did not check / replies
```

**Last value**: 70% with the plugin and 18% with none, on 2026-11-11.

---

#### M2: Lines of a reply

The length the reader meets. The rules set no length since 2026-11-13.

**Want**: Not be flooded with information. It also answers the risk that replies grow long.

**Checks**: [the rule file](../plugin/output-styles/i-am-overwhelmed.md)

**How**: The script `eval/checks.py` counts the non-empty lines of each reply of a run.

**Formula**:

```
M2 = non-empty lines of the replies of a task / replies of the task
```

**Last value**: open. Under "a few lines" the tasks `chat-en` and `chat-zh` had 7 to 12 lines. A trial on 2026-11-13 showed chat replies about twice as long, and no full run has measured the rules since.

---

#### M3: The owner's real sessions

The only signal that needs no judge. The baseline is the owner's sessions up to the morning of 2026-11-10.

**Want**: Grasp the main point. Not be flooded with information.

**Checks**: [the rule file](../plugin/output-styles/i-am-overwhelmed.md)

**How**: A scan of the owner's real sessions over some days with one set of rules.

**Formula**:

```
trees      = replies with a tree / replies
asking     = replies that end with a question / replies
simpler    = times the owner asked for "simpler" / days
```

**Last value**: open. The baseline is trees 7%, asking 87% and "simpler" 15 times in 4 days. [I12: Scan the owner's real sessions against the baseline](ISSUES.md#i12-scan-the-owners-real-sessions-against-the-baseline) holds the next scan.

---

#### M4: Words of the rule file

What every request carries.

**Want**: It answers the risk that the file costs tokens on every request.

**Checks**: [5. Every line pays for itself](../DESIGNS.md#5-every-line-pays-for-itself)

**How**: `wc -w` on the output style, with its frontmatter.

**Formula**:

```
M4 = words of plugin/output-styles/i-am-overwhelmed.md
```

**Last value**: 2,399 words and 77 tagged rules on 2026-11-18, after the rebuild of that day. Before it the file had 2,047 words and 70 rules. It had 961 words in 0.1.13 and 1,743 words in 88 rules on 2026-11-12, and how those two were counted is not on record.

---

#### M5: Stable answers of the rubric

How far a judge can be relied on. A line is stable on a reply when the judge gives the same answer in every round.

**Want**: It answers the risk that the judge favours the rule text.

**Checks**: [the rubric](../eval/rubric-yesno.md)

**How**: `eval/rubric_check.py` judges 20 replies that are on disk, several times.

**Formula**:

```
M5 = answers that are the same in every round / answers
```

**Last value**: 92% over two rounds on Haiku, on 2026-11-13, across all 117 lines. Ten lines were stable on under 16 of 20 replies, and [I4: Settle the ten rubric lines that waver](ISSUES.md#i4-settle-the-ten-rubric-lines-that-waver) holds them.

---

### Constraints

---

#### R1: The Codex rules match the output style

**Want**: The same replies for whoever shares the reader's traits, on any agent.

**Checks**: [7. One set of rules serves every agent](../DESIGNS.md#7-one-set-of-rules-serves-every-agent)

**Condition**: `codex/AGENTS.md` and the output style differ only in the frontmatter and in the line on question tools.

**How**: A unit test in `eval/tests` compares the two files, and the `tests` workflow runs it on every push.

**Status**: ✅ 2026-11-18

The 60 unit tests passed on commit `f578233`.

---

#### R2: The plugin loads in Claude Code

**Want**: It answers the risk that a rule is not followed, since a plugin that does not load applies no rule.

**Checks**: [1. The plugin sets only the output style](../DESIGNS.md#1-the-plugin-sets-only-the-output-style)

**Condition**: A fresh install from the checkout reaches "enabled".

**How**: The workflow `plugin loads in Claude Code` installs the plugin into a scratch config on every push.

**Status**: ✅ 2026-11-18

The workflow passed on commit `9b24f7c`, the release of 0.1.18.
