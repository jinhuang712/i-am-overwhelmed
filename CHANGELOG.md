# Changelog

All notable changes to this project are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Eval: `eval/eval.py` compares two versions in one command, with automatic blind judging, free mechanical checks, a new many-items task, and rubric items for the new reply rules.
- Eval: a required `--budget` covers runs and judging, with a cap on every call, a ledger, `--dry-run`, and resume. Results stay usable when the budget stops a run.
- Replies: go one thing at a time. Many items get a summary first, then an offer to go through them one by one or in batches, with overall progress in every reply. Several questions at once: pick the main one and offer the rest.

### Changed
- Eval moved from `examples/eval/` to `eval/`.
- `CLAUDE.md`: rewritten in the rule's own tagged format, with a map and rules for writing, changing, testing and releasing.

### Fixed
- Conflicts between rules: file links apply outside code blocks, the URL space rule applies to bare URLs, and a reply ends in a fixed order: next step, question, options, reasons.

## [0.1.10] - 2026-11-03

### Added
- Wordings: a new section. Phrase things positively, use fewer connectives, never use double negatives, never chain parallel clauses in one sentence. The light touch of humor moves here.
- Honesty: report finished work truthfully. It replaces "summarize the work".
- Formatting: each tool gets a `[WHEN]` case: bullets, tables, ASCII trees, diagrams, arrow waterfalls for cause and effect, mind maps. Commands, code and settings go in their own code block.
- Asking: one question per reply, explained first. Four types: multiple choice with 2 to 4 options, open, ranking, yes/no.

### Changed
- Replies: Simple is a very simple explanation; Detailed covers one thing only.
- Formatting: one point per bullet instead of one sentence. Folders become links too. Line numbers are banned in any form, even where other instructions ask for them. The bare-ID rule moves here from Replies.
- Asking: only multiple choice carries a recommendation; its reasons are bullets.

## [0.1.9] - 2026-11-03

### Added
- Honesty: say what you actually verified.
- Replies: when we drift from the original goal, say so. Suggest a next step at the end when there is one the user can take. Maybe a light touch of humor.
- Replies: questions with a short answer use Simple mode, defined as a few lines with no headings. Detailed mode uses headings.
- Formatting: never reply in paragraphs only. One sentence per bullet, preferably `- **key**: description`. Table cells are words and phrases. Code blocks hold snippets, not chunks. ASCII diagrams, trees and mind maps are listed as tools.
- Formatting: when you changed code or text, show the key change in a `diff` block.
- An A/B eval in `examples/eval/`: tasks, a rubric, and scripts to run, blind and score versions.

### Changed
- The rules (not About Me) and the Codex copy are rewritten as flat bullets tagged `[YES]`, `[NO]`, `[MAYBE]` or `[WHEN]`, in that order within each section. `[WHEN]` lines read "situation: what to do".
- Asking is split into three `[WHEN]` rules: where the question goes, recommending an option, and giving the reason.

## [0.1.8] - 2026-10-28

### Changed
- The recommended option of a question is marked with ✅ right after its letter. The reason goes in a separate section underneath the options list.

## [0.1.7] - 2026-10-28

### Changed
- New assumption under About Me: the user easily loses track of the bigger picture.
- Emoji also show your attitude, not only meaning.
- The four plugin-on examples are re-recorded with 0.1.7, and both READMEs name the model each example ran on.
- Options of a question are a Markdown bullet list (`- A. …`), so they render as a list.

## [0.1.6] - 2026-10-28

### Added
- A Formatting section, split out of Replies, in the rule file and the Codex copy.
- Reply rules for file names (linked), URLs (spaced, long ones as short links), line numbers (quote code instead) and small diffs (`diff` blocks).
- Emoji with fixed meanings (✅ recommended, ❌ error, ⚠️ ❗ 🚨 by strength, and more).
- A Formatting row in the rules table of both READMEs.

## [0.1.5] - 2026-10-25

### Changed
- The opinion rule is shorter: "I want your opinion."

## [0.1.4] - 2026-10-25

### Added
- A References section in both READMEs.
- `plugin/evals/` (`zh-chat`, `zh-agent`) so the language check can be re-run with `claude plugin eval`.

### Changed
- New rule under About Me: assume the user wants your opinion, not just the facts.
- The first line of `README.zh-CN.md` is now "一套不让你过载的回复规则", because the earlier wording read like a translation.

## [0.1.3] - 2026-10-25

### Changed
- The description now says "easy to read and structured": "A reply rule that keeps answers easy to read and structured, stays honest, and avoids overwhelming you." It changes everywhere the 0.1.2 description was.

## [0.1.2] - 2026-10-25

### Changed
- One description everywhere: "A reply rule that keeps answers easy to read, stays honest, and avoids overwhelming you." It is in `plugin.json`, `marketplace.json`, the output style's frontmatter and the first line of both READMEs, and it no longer puts Claude Code first.
- README shows complete, untrimmed output, re-run with the 0.1.1 rules and with `CLAUDE.md` files disabled on both sides.
- `examples/` has the new raw outputs, the first batch, and all 20 repeat runs. It lists the misses.

## [0.1.1] - 2026-10-25

### Removed
- The Research and Development sections of the output style. They are work habits, not reply rules, so the plugin now holds reply rules only: about me, honesty, replies and asking. I moved the two sections to my own `~/.claude/CLAUDE.md`.

### Fixed
- The README rules table said "one question". The rule only says that questions go last.

## [0.1.0] - 2026-10-25

First public release.

### Added
- The plugin: my personal preferences, loaded as a forced output style (`plugin/output-styles/i-am-overwhelmed.md`) so they are in the system prompt of every session.
- `README.md` and `README.zh-CN.md`, built on real before-and-after output.
- `examples/`: the raw outputs behind the README, the fixture, and what to know before trusting them.
