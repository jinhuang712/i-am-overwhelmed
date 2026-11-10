# Changelog

All notable changes to this project are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Changed
- Asking: the end of a reply is a decision tree, drawn in the rule file. No next step left: the reply ends with no question. The next step is the user's: it is stated. The next step is the agent's: a clear step is taken, and a step that needs the user's answer is asked. This replaces "end every reply with one way forward" and "when the answer is clear, decide and tell me". Before, a reply to a plain fact question still closed with a question.
- Asking: a question is asked only when its answer changes the next step and only the user can give it.
- Asking: a second tree says when to recommend. A question about a fact only the user knows carries no recommendation, even when its options are fixed. A decision of the user's carries at least one.
- Asking: a recommended option comes first. Before, the ✅ moved between A and B.
- Structure: every command, code, setting or program output goes in its own code block, even a single short command. Backquotes are kept for very short names and values, such as a tag or a version.
- Structure: every quoted sentence goes in a blockquote, word for word. The reminder rule is a line of its own.
- Challenge: the section keeps to doubt. "List the premises" is "doubt every premise", and "show me the ones that matter" is gone. A premise that fails is said first, before anything else.
- Asking: "a fact only I know is asked, not assumed" moves here from Challenge.
- `PHILOSOPHY.md`: a "Four quadrants" part. What each side knows makes four quadrants: Shared, the agent's blind spot, my blind spot and Unknown. The rules aim to make Shared larger, and each of the eight words works on one quadrant.
- README and `PHILOSOPHY.md`: the eight words are in order of importance: Honest, Simple, Structured, Asking, Opinionated, Focused, Standalone, Predictable.
- Eval: rubric D8 keeps the question format, and a new D20 scores the recommendation alone. Two tasks cover the other branches of the ending tree: `your-step-zh`, where the next step is the user's, and `clear-step-zh`, where the agent's step is clear. D18 scores a question that was needed, and a new D21 scores a question that was not. A new D22 scores backquotes apart from code blocks. The "ends asking" check no longer counts a question mark inside the answer.
- Eval: three tasks for rules that had none. `detail-zh` asks for more in a second turn, for Detailed. `only-you-know-zh` leaves out facts only the user knows. `shape-en` is the sign-in flow in English, for a drawing that must line up.
- Eval: the rubric has three layers. Six red flags (cheated, hid a problem, built on a guess, missed a failed premise, caved, acted without asking) fail a reply at one hit and stay out of the point total. The items are as before. A release bar names the benchmark, the comparison and the threshold. The report prints the red flags that were hit and "bar: passed" or "bar: failed" for each task.
- Eval: a compound task, `session-zh`, with four turns on the fixture: fix the flaky test, explain it simply, make the retry count configurable with a default the agent picks, and answer a question that rests on a fact only the user knows.
- Eval: the tasks no longer do a rule's work for it. "Give me a recommendation" is gone from `multi-turn-zh` and `long-discussion-zh`, and "by the way" is gone from the off-topic turn of `multi-turn-zh`. Results from before this change were run with those hints.
- Eval: `--none` adds a third arm that runs with no plugin, the second benchmark of the release bar.
- Challenge: say what you would do and what you would not, and tell the user when you see a better way. Before, the section only defended: it doubted and pushed back, and never offered.
- `PHILOSOPHY.md`: Opinionated also works on "my blind spot", since a better way the agent sees is something the user does not know.
- Eval: rubric D23 (better way), B3 also asks what the reply would not do, and a `better-way-zh` task asks for a CSV reader built on `split`.
- Wordings: "phrase things positively" is "say things straight, with the fewest words and punctuation marks". The old line was read as "say what to do", which is not what it meant.
- Honesty: never soften a thing to spare the user's feelings.
- Eval: rubric B5 (not softened) and D24 (said straight).
- Replies: open with the point. The point may be an answer, an objection, a missing fact or a split, so a discussion can still open.
- Eval: rubric C1 is "Point first".
- Wordings: humor moves from `[MAYBE]` to `[YES]`, when the moment is light. As `[MAYBE]` it almost never appeared. No rule uses `[MAYBE]` now; the tag stays defined.
- Eval: humor is rubric D25, a required item, in place of the optional E3.
- Formatting: emotion goes in the emoji, and the words stay plain. Before, the rule only said what emoji can do.
- `PHILOSOPHY.md`: an "Emotion goes in the emoji" part.
- Replies: the order is define, discuss, do, drawn as a tree. A thing whose goal, scope or end is not defined gets a definition first, and the agent says it. A defined thing with open points is discussed. A defined thing with none is done.
- Eval: rubric D26 (defined first) and a `vague-zh` agent task, "optimise this project".
- Eval: every task has a `budget`, the most one run of it may cost. The tool caps each run at its own limit, adds the limits up in `--dry-run`, and keeps $0.30 a task for judging. Before, the budget was split evenly, so a chat run could not spend its share and an agent run was stopped early.
- Eval: one reply is capped at 16,000 output tokens, and a run that hits the account's usage limit counts as failed. `only-you-know-zh` is an agent task with a `tiny-service` fixture: as a chat task with no tools it made the model write made-up tool calls until the output limit.
- `PHILOSOPHY.md`: "One rule per line" is now "Discrete rules". A rule with a shape is a drawing.
- Eval: rubric D2 follows the tree, D18 also fails a question about going on with a clear step, and a `fact-zh` chat task asks a plain fact.

### Fixed
- Install: `install-claude.sh` now updates a plugin that is already installed. Before, `claude plugin install` reported success for an installed plugin, so the update never ran and the old version stayed.

## [0.1.14] - 2026-11-10

### Added
- Structure is its own section, after Replies, with six parts: Drawings, Tables, Bullet Points, Headings, Quotes and Code Blocks. The rules moved there from Formatting. Formatting keeps emoji, links, URLs, IDs and line numbers.
- Structure: simplify first, then give structure to what is left.
- Structure: draw the content whenever it has a shape. Bullet points are the fallback for content without a shape. A tree also covers branching decisions.
- Structure: every level of a drawing has the same indent. A drawing with boxes or columns that must line up is in English only, because wide characters such as Chinese and emoji break the alignment. An English drawing lines up its columns with spaces. A drawing with Chinese labels stays unpadded, or puts each note on the next line, where it lines up in any font.
- Structure: a blockquote holds quoted text and reminders that need no emphasis.
- About Me: "I take in a drawing faster than a list."
- About Me: "I forget what the last reply said." Every reply stands on its own and says again what the reader needs from an earlier one. A question number is never used bare, the same as a code or an ID.
- Asking: a clear answer is decided and reported, not asked. One question holds one decision. Anything that needs confirmation is asked as a question.
- Challenge: a premise that is a fact only the user knows is asked before it is built on.
- Install: `install-claude.sh` installs the Claude Code plugin, or updates it when it is already there. Then it checks that the plugin is installed and enabled. `--check` runs only the check.
- CI: a `tests` workflow runs the eval tests. A new test fails when `codex/AGENTS.md` and the output style differ in more than the frontmatter and the question-tools line.
- Eval: rubric items D16 (shape drawn), D17 (one decision), D18 (needed question) and D19 (blockquotes); a `shape-zh` chat task; mechanical checks that count drawings, tables, quotes, headings, replies that end asking, and lines.

### Changed
- Replies: Simple is the default: a few lines, no headings. Detailed comes when the user asks for more, or when Simple would mislead: one thing only, with headings. Before, a short answer picked Simple. Three evals on 2026-11-10 showed that a principle alone ("as simple as you can") left short questions three to five times longer.
- Asking: the limit of one question per reply is gone. A reply asks as many as it needs, numbered Q1, Q2, each of a fixed type: multiple choice, multi-select, yes/no, quick or ranking. The open type is replaced by quick. A strict limit made the model squeeze several questions into one.
- Asking: only a choice that asks for a decision carries a recommendation.
- Asking: a yes/no question stands alone, with no "(yes/no)" hint after it.
- Asking: every reply ends with one way forward: questions when an answer is needed, otherwise the next step. This replaces the "suggest a next step" rule in Replies.
- Formatting: "Never reply in paragraphs only" is now a positive `[YES]` rule in Structure: give every reply some structure.
- README: a new order. A hero image, an intro with eight keywords (Simple, Honest, Structured, Predictable, Focused, Standalone, Asking, Opinionated), what you get, install, how it works, examples, then the rules. "How it works" says the plugin sets only the output style, with the Claude Code docs as the source.
- `PHILOSOPHY.md`: why the rules look the way they do. What a reply should be, how the rules are written, and what the plugin leaves alone. The README's docs quotes and background reading move there.
- `assets/hero.svg` and `assets/hero.zh-CN.svg`: a fed-up user's message to their agent after a long session, with the reply rules highlighted.
- README: the plugin-on examples are re-recorded with the new rules, a sign-in flow example shows a drawing, and the plugin-off reply folds away. The comparison table follows the new rules.
- Install: the README shows two ways. For Claude Code, the two CLI commands or one curl line. For any agent, one line to paste, which sends it to `INSTALL.md`. `INSTALL.md` is now written for the agent: Claude Code runs the script, and Codex or another agent reads the rules and decides how to add them to the user's instructions.
- Eval: rubric C2 is "Depth fit", C4 follows the Structure section, D2 is "Way forward", D8 and D14 follow the asking rules. E2 is removed, since drawing is now required.

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
