# i-am-overwhelmed

A reply rule for coding agents: answers stay honest, structured and easy to skim. Claude Code comes first, then Codex.

Tags, in this order: `[YES]` do it. `[NO]` never do it. `[MAYBE]` your call, when it fits. `[WHEN]` a situation, written as "situation: what to do".

# Map

```
plugin/output-styles/i-am-overwhelmed.md   the rule, the source of truth
plugin/.claude-plugin/plugin.json          the version
plugin/evals/                              `claude plugin eval` cases
codex/AGENTS.md                            the rule for Codex
PHILOSOPHY.md                              why the rules look the way they do
install-claude.sh                          the Claude Code installer
INSTALL.md                                 install steps, written for the agent
eval/                                      the A/B tool, with a budget
examples/                                  raw outputs behind the README
assets/hero.svg, hero.zh-CN.svg            the hero images of the two READMEs
.local/                                    private, git-ignored
```

# Writing Rules

- [YES] Keep rules discrete: one rule per line, with its tag.
- [WHEN] A rule has a shape, such as branching decisions: draw it, as the rule file asks of a reply.
- [YES] Keep rules agent-neutral, except where a host needs its own line.
- [YES] Write rules in our own words. ASD-STE100 is the inspiration.
- [YES] Define formats with placeholder templates, such as `<done>/<total>`.
- [YES] Name a concrete trigger in every `[WHEN]`. Past evals show the trigger's wording decides whether a rule is followed.
- [YES] Fit a new rule into an existing one when you can.
- [YES] Phrase rules positively. The rule file follows its own rules.
- [NO] Never copy the standard's text into the repo.
- [WHEN] A rule needs Chinese: write it natively, in a technical register.
- [WHEN] Two rules conflict: fix their scope first, then consider a new rule.

# Changing Rules

- [YES] Change the output style and `codex/AGENTS.md` together. They differ only in the frontmatter and the question-tools line.
- [YES] Record every change under `[Unreleased]` in `CHANGELOG.md`.
- [WHEN] A change alters what a section promises: update "The rules" in both READMEs.
- [WHEN] A change alters the thinking behind the rules: update `PHILOSOPHY.md`.
- [WHEN] A change alters the eval's scope: update `eval/rubric.md` and `eval/tasks.json`.

# Eval

- [YES] Run `python3 eval/eval.py --old <ref> --dry-run` before a real run.
- [YES] Run `python3 -m unittest discover eval/tests` after changing the eval. It costs nothing.
- [YES] Treat eval scores as samples. Read the judge's quotes as well as the totals.
- [NO] Never spend on a real run without an approved budget.
- [NO] Never let a task's words do a rule's work, such as "keep it simple" or "you decide".
- [YES] Make a task ask one thing, unless it tests a message that asks several.
- [YES] Give a task that makes the agent want to read files the `agent` kind and a fixture.
- [WHEN] A release changes rules: run the eval on them first.
- [WHEN] A model has no cost history: start with a small smoke run.

# Release

- [YES] Bump `plugin/.claude-plugin/plugin.json`, then move `[Unreleased]` to the new version in `CHANGELOG.md`.
- [YES] Name the commit `Release <version>: <summary>`.
- [YES] Keep one description across `plugin.json`, `marketplace.json` and the output style.
- [WHEN] A change touches `plugin/` or `.claude-plugin/`: expect the plugin load check in CI.
- [WHEN] You push or open a pull request: expect CI to run the eval tests, which also compare the two rule files.

# Privacy

- [YES] Keep private material in `.local/`.
- [YES] Keep `docs/ste-mapping.md` git-ignored.
- [NO] Never quote `.local/` content in a public file.
