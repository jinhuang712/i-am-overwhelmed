# Changelog

All notable changes to this project are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Install: `install-claude.sh` installs the Claude Code plugin, or updates it when it is already there. Then it checks that the plugin is installed and enabled. `--check` runs only the check.

### Changed
- Install: the README shows two ways. For Claude Code, the two CLI commands or one curl line. For any agent, one line to paste, which sends it to `INSTALL.md`. `INSTALL.md` is now written for the agent: Claude Code runs the script, and Codex or another agent reads the rules and decides how to add them to the user's instructions.
- Formatting: the shape rules are now one principle with examples: draw the content whenever it has a shape (table, ASCII tree, diagram, arrow waterfall, mind map). Bullet points are the fallback for content without a shape. The tree also covers branching decisions.
- About Me: "I take in a drawing faster than a list."
- Asking: three principles on when to ask. A clear answer is decided and reported, not asked. One question holds one decision. Every reply ends with one way forward: a question when a decision is needed, otherwise the next step. This replaces the "suggest a next step" rule in Replies, and the ending-order rule now covers only question, options, reasons.
- Replies: the Simple and Detailed modes are replaced by one principle: go deep on one thing only, keep several things brief. The rule no longer sets line counts or headings, and the separate "short answer: use Simple" rule is removed.
- Replies: the default is the simplest reply that keeps what matters. Detail comes when the user asks for more, or when the simple version would mislead. The 2026-11-10 eval showed short questions growing from 8 lines to 40 without this.
- Asking: the limit of one question per reply is gone. A reply asks as many as it needs, numbered Q1, Q2, each of a fixed type: multiple choice, multi-select, yes/no, quick or ranking. The open type is replaced by quick. A strict limit made the model squeeze several questions into one.
- Asking: anything that needs confirmation is asked as a question. Only a choice that asks for a decision carries a recommendation.
- Challenge: a premise that is a fact only the user knows is asked before it is built on.
- Eval: rubric C2 is now "Depth fit" and checks that principle.
- Eval: rubric D8 and D18 follow the new asking rules.
- Eval: rubric items D16 (shape drawn), D17 (one decision), D18 (needed question) and D19 (blockquotes). E2 is removed, since drawing is now required. C4 follows the Structure section.
- Eval: a `shape-zh` chat task whose answer has a flow and branches.
- Eval: mechanical checks count drawings, tables, quotes, headings, replies that end asking, and lines.
- Structure is its own section, after Replies: the structure, shape, bullet, table-cell and heading rules move there from Formatting, word for word. Formatting keeps the written conventions: emoji, links, URLs, IDs, line numbers and code blocks. Structure has six parts: Drawings, Tables, Bullet Points, Headings, Quotes and Code Blocks. The code-block rules move there from Formatting.
- Structure: simplify first, then give structure to what is left. A second eval on 2026-11-10 showed the simple-by-default rule losing to the structure rules on short questions.
- Structure: every part of a reply gets a heading; the "long reply" condition is gone.
- Structure: a blockquote holds quoted text and reminders that need no emphasis.
- Formatting: "Never reply in paragraphs only" is now a positive `[YES]` rule: every reply has some structure, such as bullets, a table or headings.

## [0.1.13] - 2026-11-09

### Added
- Replies: when the big picture changes, the reply opens with `📍 <goal> · decided: <list> · open: <list>`. Drift points back to the goal.
- Wordings: a coined term or short name is defined the first time it appears.
- Eval: rubric D8 accepts yes/no and open questions without options, as the rule allows.
- Eval: a `long-discussion-zh` task with a mid-way reversal, rubric items F4 (📍 anchor) and D15 (terms defined), and an `anchors` mechanical check.

### Changed
- Formatting: each part of a long reply has a heading, with a Markdown `---` line above each heading after the first, after a blank line. This replaces the `─` title line: a long `─` line wraps on a phone, and it took the heading's place.

## [0.1.12] - 2026-11-09

### Added
- Formatting: start each part of a long reply with a title line, `───── <title> ─────`, since a Markdown `---` may show as plain text.

## [0.1.11] - 2026-11-07

### Added
- Eval: `eval/eval.py` compares two versions in one command, with automatic blind judging, free mechanical checks, a new many-items task, and rubric items for the new reply rules.
- Eval: a required `--budget` covers runs and judging, with a cap on every call, a ledger, `--dry-run`, and resume. Results stay usable when the budget stops a run.
- Challenge: a new section. List the premises the work relies on, yours and mine, check each one, and show the ones that matter.
- Eval: a `design-flaw-zh` task and a rubric item for raising a flawed premise first.
- Replies: go one thing at a time. Many items get a summary first, then an offer to go through them one by one or in batches, with overall progress in every reply. Several questions at once: pick the main one and offer the rest.

### Changed
- Eval moved from `examples/eval/` to `eval/`.
- Pushing back, holding a position and opening a discussion move from Honesty to Challenge.
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
