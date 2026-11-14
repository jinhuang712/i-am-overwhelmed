# Changelog

All notable changes to this project are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [0.1.17] - 2026-11-14

### Added
- Replies: one template names every block of a reply, says what each holds and when it is due, and takes in five rules that had a condition of their own: a failed premise, going through items, a changed big picture, drift and a fitting topic.
- Replies: a tree decides what one reply covers: Detailed, Simple (a minimal reply for a thing that is really simple) or Default.
- Replies: `<findings>` also holds what the agent did, so the report of finished work has a place.
- Structure: a tree on where the wide characters sit says how to line a drawing up.
- Structure: every drawn rule has its own heading at the end of its section, and every section opens with one sentence that says why its rules are there.
- Eval: `eval/rubric-yesno.md` opens with its formats, how to write a line, its families and its score, and `eval.py` judges with it by default.
- Eval: the report has a part "Old against new": the quality gap with a 90% interval, the tasks up and down, and the lines whose count moved.
- Eval: new rubric lines for a simple question answered in several sections, one answer to a choice that has others, and steps in a row drawn as a diagram.
- Eval: `eval/FINDINGS.md` records the trial of the kinds of parts and the comparison of the rules with tags against the rules without, on Sonnet 5.5.

### Changed
- Recommending: the tree holds where the pick goes and its reasons, in place of two rules with the same trigger.
- Structure: steps that run in a straight line are a numbered list, not a drawing.
- Structure: the lists of shapes and of question types use the bold key.
- Replies: "call a thing decided only when I verbally agreed on it" moves under the 📍 block, which it is about.
- Eval: the rubric parks the lines that opposed the new rules or fired on most replies, and the check of all 117 lines is on record.
- Docs: PHILOSOPHY, `CLAUDE.md` and the READMEs follow the new rules and say why `[WHEN]` went.

### Removed
- The `[WHEN]` tag: its rules became branches of trees, lines of the template, or `[YES]` and `[NO]`, so the rule file has two tags.
- Replies: "a few lines", and the rules on a task with many items, on several questions and on "more on one thing", which the tree on what one reply covers now holds.
- Replies: the "define, discuss, do" tree; the definition is a line of the template.
- Replies: "put reminders that need no emphasis in a blockquote", which the note in the template already says.

## [0.1.16] - 2026-11-12

### Added
- Replies: reply in the language of the user's message.
- README: a benchmark badge and section with the latest score against no plugin.
- README: "What you get" adds what the owner noticed beyond the replies: the agent's work changes too.
- Eval: `--reuse` takes the finished runs of an earlier results folder, matched by plugin files and model.
- Eval: `rubric_check.py --strong` checks the 🔎 lines on the strong judge.

### Changed
- Replies: a thing is decided only when the user agreed on it in words; the line no longer echoes the 📍 template.
- Asking: a decision of the user's gets a recommended answer, so a yes or no question carries the agent's view too.
- Formatting: a bare number of any kind needs its title, such as a step or an item, not only a question number.
- Honesty: the line on cheating is about the reply now: never hide what you skipped, loosened or retried to make something pass.
- Challenge: "doubt every premise" no longer adds "check each one"; how the work is done is left to the host.
- README: "What you get" keeps to what the benchmark shows, and no longer says "less to read".
- README: the examples come from the benchmark of 2026-11-11, the first run of each side, on Opus 5.5. The English README drops the CI example, which the eval has in Chinese only.
- Eval: the rubric check judges the replies of its last round; a failed judge call keeps what it said; a dry run says what a resume keeps.

### Removed
- Formatting: "never overuse emoji".
- The `[MAYBE]` tag, which no rule used.
- Replies: "go deep on one thing only; keep several things brief"; "one thing at a time" stays.
- Asking: "ask as many questions as you need"; several questions are still allowed.
- README: "The rules" and "What actually changes". "Tune it" links the rule file instead.

## [0.1.15] - 2026-11-12

### Added
- Honesty: stop when instructions conflict, and go by a tree: follow an answer the user gave before, or an instruction that says it wins, or ask.
- Honesty: never soften a thing to spare the user's feelings.
- Challenge: say what you would and would not do, and name a better way when you see one.
- Replies: every reply has a shape, drawn as a template: a lead that answers on its own, parts in order of importance, then the ending. It comes from news writing.
- Replies: define, discuss, do, drawn as a tree. An undefined task gets a definition first; a clear one is announced, then done.
- Replies: say what changed since the last reply.
- Replies: count as decided only what the user decided. The agent's own advice stays open until the user takes it.
- Structure: a list gets its count first, and a command never sits inside a sentence.
- Wordings: plain written language, the verb itself, checkable claims, numbers with what they compare with, and one name for one thing.
- Asking: ask only what changes the next step and only the user can answer.
- Asking: every question starts with 💬, and a recommended option comes first.
- Docs: `PHILOSOPHY.md` gains parts on the four quadrants, emotion in the emoji and news writing. New files: `eval/FINDINGS.md` and `TODO.md`.
- Eval: a yes or no rubric, `rubric-yesno.md`, with red flags and one overall score per arm. `rubric_check.py` and `flag_check.py` check the rubric itself.
- Eval: `--smoke`, `--none` for an arm with no plugin, a budget per task, sessions clean of the runner's setup, and tasks for the new rules.

### Changed
- Honesty: a guess is anything you did not check. Mark it where you make it, say what you checked where you state it, and say what you did not do.
- Challenge keeps to doubt, and a premise that fails is said first.
- Replies: the 📍 line is a short block, one item a line.
- Replies: when the user asks about several things, the reply answers the main one and lists the rest, with no offer.
- Structure: every command, code, setting or output goes in a code block. Backquotes are for short names, and quotes go in blockquotes, word for word.
- Structure: an arrow waterfall is only for a chain of causes and effects. The part of a bullet after its key is one whole sentence.
- Wordings: say things straight, and cut every word that carries nothing while keeping sentences whole. Humor is a plain `[YES]`.
- Formatting: emotion goes in the emoji to keep the words plain. A file name is a link every time it is named.
- Asking: the end of a reply follows a tree. A plain answer ends with no question, and a clear step is taken, not asked.
- Asking: a tree says when to recommend. A decision of the user's gets a recommendation; a fact only the user knows does not.
- Asking: one thing in one question, with its context first. "A fact only I know is asked" moves here from Challenge.
- README and `PHILOSOPHY.md`: the eight words are in order of importance.

### Fixed
- Install: `install-claude.sh` updates a plugin that is already installed.
- Eval: a run fails when the session did not load its arm's plugin.

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
