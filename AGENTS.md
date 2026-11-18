# AGENTS.md

This file holds what an agent cannot learn by reading the files: how the work goes in this project.

**Read again after a compaction.** When the window is new or was compacted, read the skill what-we-build and every guide in full if it is installed, then every doc in the read order, before anything else.

---

## Tags

A list of tagged lines holds one family, and the sentence before it says which.

| Family | Tag | Means |
|---|---|---|
| Definition | `[YES]` | what a thing is or holds |
| Definition | `[NO]` | what it is not or leaves out |
| Rule | `[MUST]` | required |
| Rule | `[NEVER]` | forbidden |
| Rule | `[BETTER]` | preferred, not required |

The rule file is the product and has tags of its own: there `[YES]` means "do it" and `[NO]` means "never do it". The two rule files keep those tags. Every doc uses the 5 tags above.

---

## Read order

8 docs:

1. [PROPOSAL.md](PROPOSAL.md) says why the project exists and who it is for.
2. [PHILOSOPHY.md](PHILOSOPHY.md) holds the stances and their arguments.
3. [DESIGNS.md](DESIGNS.md) holds the 7 guidelines a rule must meet.
4. [The rule file](plugin/output-styles/i-am-overwhelmed.md) is the product and the contract with the reader.
5. [plan/ROADMAP.md](plan/ROADMAP.md) says where the work stands.
6. [plan/GOALS.md](plan/GOALS.md) holds the checks and their last results.
7. [plan/ISSUES.md](plan/ISSUES.md) holds the agreed work.
8. [plan/TODO.md](plan/TODO.md) holds what nobody has agreed to do yet.

Before work on a rule or on the eval, read [eval/README.md](eval/README.md) and [eval/FINDINGS.md](eval/FINDINGS.md) too.

---

## Layout

12 facts:

- The root holds the reasons and the contract: PROPOSAL · PHILOSOPHY · DESIGNS · README · INSTALL · CHANGELOG.
- [`plan/`](plan/) holds GOALS · ROADMAP · ISSUES · TODO.
- [`specs/decisions/`](specs/decisions/) holds one file per decision in force.
- [`plugin/output-styles/i-am-overwhelmed.md`](plugin/output-styles/i-am-overwhelmed.md) is the rule file and the source of truth.
- [`codex/AGENTS.md`](codex/AGENTS.md) is the rule file for Codex. It is a product file and not this file.
- [`plugin/.claude-plugin/plugin.json`](plugin/.claude-plugin/plugin.json) holds the version.
- [`plugin/evals/`](plugin/evals/) holds the cases of `claude plugin eval`.
- [`install-claude.sh`](install-claude.sh) is the Claude Code installer.
- [`eval/`](eval/) is the A/B tool with a budget, and its README is its handbook.
- [`examples/`](examples/) holds the raw outputs behind the README, and [`assets/`](assets/) holds the hero images of the two READMEs.
- `eval/flag-cases/` and `.local/` are private and git-ignored.
- `CLAUDE.md` loads this file and holds nothing else.

2 checks hold rules of their own, so no rule here repeats them:

- A unit test fails when the two rule files differ in more than the frontmatter and the line on question tools.
- CI runs the unit tests on every push, and the plugin load check when `plugin/` or `.claude-plugin/` changes.

---

## Exceptions

The owner agreed to 5 exceptions to what-we-build on 2026-11-18:

- **No FEATURES.md**: The rule file is the contract with the reader, and a second list of its rules would be a second home for each.
- **No GLOSSARY.md, CONTRIBUTING.md, specs or evidence folder**: Each joins when the project needs it.
- **`eval/README.md` stays as it is**: It is the handbook of the tool, with how it works and its past results.
- **`eval/FINDINGS.md` stays as it is**: It is the running record of what the evals taught us, and the skill has no doc for one.
- **`README.zh-CN.md` mirrors `README.md`**: A change to one changes the other in the same commit.

---

## While you work

5 rules of the skill:

- [MUST] follow these rules strictly unless the user rejects one.
- [MUST] read every doc you work on in full.
- [NEVER] give a doc to a subagent to read or write.
- [NEVER] use a script or a search in place of reading a doc in full.
- [NEVER] check the goals for a small change.

Work meets 14 cases. Follow every branch that applies, since several can hold at once:

```
What is happening?
├── The user stops you
│   └── stop at once, with all your agents
├── A doc and something disagree
│   ├── The user says something a doc contradicts
│   │   └── say so before you act
│   └── You find a contradiction
│       ├── tell the user
│       └── pick no side
├── You are about to change something
│   ├── read the doc that owns it first
│   └── The work needs the code
│       └── a subagent may read it
├── You change something
│   ├── check what you touched against the rules
│   ├── You make a choice the DECISIONS guide counts as one
│   │   └── write it down at once
│   ├── You change a fact or a rule
│   │   └── search the docs for what it now contradicts
│   ├── Something in the update tree below happens
│   │   └── update the docs it names in the same change
│   └── The change lands
│       └── before you report, fix what it left behind in the docs and `TODO.md`
├── A piece of work ends
│   ├── The work at hand is done and nothing is next
│   │   └── go through `TODO.md` with the user
│   └── A checkpoint ends or a release is near
│       ├── check the goals it names
│       └── A checkpoint ends
│           └── run the skill's start pass if it is installed
└── Other developers build on the project
    ├── say it may need a wiki
    └── let the user pick its form
```

Read only the docs the work needs.

```
What do you read?
├── Your window is new or was compacted
│   └── read again as the rule at the top says, then every doc in the read order
├── You need to know where things stand
│   └── scan ROADMAP · ISSUES · TODO · GOALS
├── You are about to change something
│   └── What does it change?
│       ├── Why the project exists or how it thinks
│       │   ├── its reason, its wants or who it is for           PROPOSAL
│       │   ├── a stance that steers the whole project           PHILOSOPHY
│       │   └── a commitment a rule must meet                    DESIGNS
│       ├── What it does, and when
│       │   ├── what a reply must say or look like               the rule file, then DESIGNS
│       │   ├── an effect with a test or a number                GOALS
│       │   ├── when it comes or how far along it is             ROADMAP
│       │   ├── agreed work that adds no rule                    ISSUES
│       │   ├── a question nobody has answered                   TODO
│       │   └── what shipped in a release                        CHANGELOG
│       ├── How it is built and checked
│       │   ├── how the eval works or is run                     eval/README
│       │   ├── what an eval taught us                           eval/FINDINGS
│       │   └── a choice between ways                            specs/decisions/
│       └── How it is used and kept
│           ├── what a visitor reads first                       README, both languages
│           ├── how to install it                                INSTALL
│           └── a rule for how the work is done                  AGENTS
└── A doc and something disagree
    └── read the doc that owns the fact and the thing that disagrees with it
```

Update only the docs an event affects.

```
What just happened?
├── A rule was agreed
│   ├── the rule file      both copies
│   ├── CHANGELOG          under Unreleased
│   └── GOALS              the effect it must have
├── Other work was agreed
│   ├── ISSUES             what it is and why
│   └── ROADMAP            when it comes
├── A change was done
│   ├── CHANGELOG          what shipped
│   ├── ROADMAP            its progress
│   ├── ISSUES             without the issue it did
│   ├── eval/README        how the tool works now
│   └── README, INSTALL    how it is used now
├── An eval taught something  eval/FINDINGS, with its date and how strong the evidence is
├── A decision was made       decisions/
├── A question stayed open    TODO
├── A todo was done           delete it from TODO
├── A number moved            GOALS
├── A stance changed          PHILOSOPHY
└── A commitment changed      DESIGNS
```

The project adds 27 rules of its own.

On the rule file:

- [MUST] check a rule change against every guideline in [DESIGNS.md](DESIGNS.md) before you write it.
- [MUST] keep the tested wording of a condition when you move it, since past evals show the wording decides whether a rule is followed.
- [MUST] define a format with a placeholder template, such as `<done>/<total>`.
- [MUST] update `eval/rubric-yesno.md` and `eval/tasks.json` when a rule change alters what the eval covers.

On the eval:

- [MUST] run `python3 eval/eval.py --old <ref> --dry-run` before a real run.
- [MUST] run `python3 eval/eval.py --smoke` before a full run, under a small approved budget.
- [MUST] start a model that has no cost history with a small smoke run.
- [MUST] run `python3 -m unittest discover eval/tests` after changing the eval, which costs nothing.
- [MUST] judge with the yes or no rubric, since the scale in `eval/rubric.md` is frozen.
- [MUST] write a rubric line as the rubric's own part "How to write a line" says.
- [MUST] read the lines of a deck before you add one to it, since a line that says what another says counts a fault twice.
- [MUST] run `python3 eval/rubric_check.py` after changing `eval/rubric-yesno.md`.
- [MUST] run `python3 eval/flag_check.py` after changing a red flag line.
- [MUST] treat eval scores as samples, and read the judge's quotes as well as the totals.
- [MUST] name the decision a paid run can change before it starts, and drop the run when there is none.
- [MUST] run the eval on the rules before a release that changes them.
- [MUST] watch `raw/progress.log` of a paid run and tell the owner at each quarter.
- [MUST] make a task ask one thing, unless it tests a message that asks several.
- [MUST] give a task that makes the agent want to read files the `agent` kind and a fixture.
- [MUST] put the upper instruction in the task's `system` field when a task sets a trap between two instructions.
- [NEVER] spend on a real run without an approved budget.
- [NEVER] eval a single rule change: collect the changes and run one eval per release.
- [NEVER] judge with a rubric that is still changing.
- [NEVER] let a task's words do a rule's work, such as "keep it simple" or "you decide".

On a release:

- [MUST] bump `plugin/.claude-plugin/plugin.json`, move *Unreleased* in the changelog under the new version and name the commit `Release <version>: <summary>`.
- [MUST] keep one description across `plugin.json`, `marketplace.json` and the output style.

On privacy:

- [NEVER] quote `.local/` content in a public file.

---

## How we work

The owner stated 16 ways, where the files do not say them:

- **Budget**: The owner names the budget, so propose a number and wait.
- **Profile**: Run the evals on the owner's second Claude Code profile, as "Another account" in the eval's handbook says.
- **One change**: Change one thing at a time, and show the change as git prints it.
- **Rules**: Improve a rule that exists before you add one, and give a rule no example.
- **Short rules**: Two short rules are better than one long rule, so remove a line that repeats and do not merge lines.
- **The owner's wording**: Keep the owner's wording of a rule, and cut around it.
- **Backstops**: A rule whose fault does not show is not dead weight, so do not propose to drop a rule for that reason alone.
- **Rubric lines**: Never drop a rubric line for how often it fires: read what it hit, and park a line instead of deleting it.
- **Red flag cases**: Add a case to `eval/flag-cases/` each time the owner judges a hit.
- **The owner's judgment**: When a judgment is the owner's to make, such as whether a thing is a fault, ask and do not decide it from a count.
- **Language**: Reply in the owner's language, and send a file when asked to show one, since the owner often reads on a phone.
- **One thing a reply**: Long replies with several parts and several questions read as a mess to the owner.
- **The comparison**: Compare against no plugin.
- **Reruns**: The owner counts reruns as waste, so propose the smallest step. Evals had cost $188 by 2026-11-12, with at least $66 of it on runs and judging done again.
- **The README**: It may leave a weak point out, and it may not claim what our own numbers contradict.
- **Conflicts**: When an agent reports a conflict between instructions in a real session, write it in the TODO as a `DISCUSSION` and fix the scope of the rules it names.

The owner turned down 4 things for the README: a list of where the plugin does worse · a source on each line of "The work feels different" · a credit line · a shorter README.
