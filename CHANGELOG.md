# Changelog

The project uses [Semantic Versioning](https://semver.org/).

---

## Unreleased

---

## 0.2.0 — 2026-11-18

---

### About Me

- Added: four facts about the reader: long lines and long sentences tire me, I don't follow your work line by line, details overwhelm me, and I decide from the direction.
- Added: a part "What I Want" names the five wants that every rule serves.

---

### Replies

- Changed: every reply after the first opens with a recap of the current state of the work and what requires your attention, in a structured form when the work is long. Before, a reply opened with a 📍 block when the big picture changed: the goal, what you decided and what was open. That block is gone.
- Changed: every part of a reply is built the same way: a heading with an emoji, one sentence that states its conclusion, and the evidence for it in a structured form. One more sentence says what the evidence means, where the evidence does not state it.
- Changed: the section stands in front of Honesty.
- Added: every label in a reply is in the language of your message.
- Changed: "call a thing decided only when I verbally agreed on it" moves under Replies.
- Added: a discussion has its own branch. The agent gives one idea at a time with its assessment, and lets you respond.
- Removed: "say what changed since the last reply", "say again what I need from an earlier reply", and the background and progress lines of the template. The recap holds them now.

---

### Structure

- Added: every heading begins with an emoji that indicates its content.
- Added: one definition of a structured form: a drawing, a table, a list, a blockquote or a code block.

---

### Wordings

- Added: the register of a rigorous technical document, one idea per sentence, and the category term in place of a list of similar items.
- Added: no subordinate clause inside another, and no deferential language.
- Added: three samples of faults of style, in a part of their own at the end of the section.
- Changed: the rule against parallel clauses covers parallel sentences too, and asks for a structured form instead.

---

### All sections

- Changed: the whole rule file is reworded into a rigorous written register, in 79 places. It has no idiom, no figure of speech, no contraction and no "thing" where a term fits. The rules ask for the same as before.
- Changed: 47 sentences that did not read fluently are reworded, such as the line on tags at the top and the sentence above the objectives.
- Changed: two blocks of the template have new names. `<push-backs>` is `<objections>`, and `<pick>` is `<recommendation>`.

---

### Asking

- Added: every question is self-contained.
- Changed: the tree that ends a reply asks first whether this is a discussion rather than a task.

---

### Honesty

- Added: the reply shows the excerpt that supports each claim based on a source or a result.
- Added: the reply reports every unresolved problem, especially any workarounds.
- Removed: "report every finished piece of work truthfully", which the rules on what was verified already hold.

---

### Eval

- Removed: the measure that counted 📍 blocks.

---

### Docs

- Changed: the docs follow one layout: a proposal, designs, decisions, and a plan folder with goals, a roadmap, issues and a todo. `CLAUDE.md` loads `AGENTS.md`.
- Removed: `INSTALL.zh-CN.md`. The Chinese README links `INSTALL.md`.
- Added: `PHILOSOPHY.md` says how a rule on the reply changes what the agent does, with a count of tool calls from the benchmark.
- Added: `PHILOSOPHY.md` says that structure carries the other wants, and that the direction comes before the detail.

---

## 0.1.18 — 2026-11-18

---

### Replies

- Added: every reply starts with one heading that names what it is about, and the template gets a `<title>` line.
- Changed: every part of a reply has a heading, in place of "in Detailed, give each part a heading".

---

### Eval

- Added: `eval/checks.py` finds drawings whose vertical joins miss, counting a wide character as two columns.

---

### Structure

- Changed: when a drawing tool or skill is on hand, it decides how to line up; the tree on wide characters applies only with none.
- Changed: in a tree with wide labels, a note is a child of its label, not a line below it.

---

### Docs

- Changed: README, PHILOSOPHY and the rubric follow the heading rules.

---

## 0.1.17 — 2026-11-14

---

### Replies

- Added: one template names every block of a reply, says what each holds and when it is due, and takes in five rules that had a condition of their own: a failed premise, going through items, a changed big picture, drift and a fitting topic.
- Added: a tree decides what one reply covers: Detailed, Simple (a minimal reply for a thing that is really simple) or Default.
- Added: `<findings>` also holds what the agent did, so the report of finished work has a place.
- Changed: "call a thing decided only when I verbally agreed on it" moves under the 📍 block, which it is about.
- Removed: "a few lines", and the rules on a task with many items, on several questions and on "more on one thing", which the tree on what one reply covers now holds.
- Removed: the "define, discuss, do" tree; the definition is a line of the template.
- Removed: "put reminders that need no emphasis in a blockquote", which the note in the template already says.

---

### Structure

- Added: a tree on where the wide characters sit says how to line a drawing up.
- Added: every drawn rule has its own heading at the end of its section, and every section opens with one sentence that says why its rules are there.
- Changed: steps that run in a straight line are a numbered list, not a drawing.
- Changed: the lists of shapes and of question types use the bold key.

---

### Eval

- Added: `eval/rubric-yesno.md` opens with its formats, how to write a line, its families and its score, and `eval.py` judges with it by default.
- Added: the report has a part "Old against new": the quality gap with a 90% interval, the tasks up and down, and the lines whose count moved.
- Added: new rubric lines for a simple question answered in several sections, one answer to a choice that has others, and steps in a row drawn as a diagram.
- Added: `eval/FINDINGS.md` records the trial of the kinds of parts and the comparison of the rules with tags against the rules without, on Sonnet 5.5.
- Changed: the rubric parks the lines that opposed the new rules or fired on most replies, and the check of all 117 lines is on record.

---

### Recommending

- Changed: the tree holds where the pick goes and its reasons, in place of two rules with the same trigger.

---

### Docs

- Changed: PHILOSOPHY, `CLAUDE.md` and the READMEs follow the new rules and say why `[WHEN]` went.

---

### General

- Removed: The `[WHEN]` tag: its rules became branches of trees, lines of the template, or `[YES]` and `[NO]`, so the rule file has two tags.

---

## 0.1.16 — 2026-11-12

---

### Replies

- Added: reply in the language of the user's message.
- Changed: a thing is decided only when the user agreed on it in words; the line no longer echoes the 📍 template.
- Removed: "go deep on one thing only; keep several things brief"; "one thing at a time" stays.

---

### README

- Added: a benchmark badge and section with the latest score against no plugin.
- Added: "What you get" adds what the owner noticed beyond the replies: the agent's work changes too.
- Changed: "What you get" keeps to what the benchmark shows, and no longer says "less to read".
- Changed: the examples come from the benchmark of 2026-11-11, the first run of each side, on Opus 5.5. The English README drops the CI example, which the eval has in Chinese only.
- Removed: "The rules" and "What actually changes". "Tune it" links the rule file instead.

---

### Eval

- Added: `--reuse` takes the finished runs of an earlier results folder, matched by plugin files and model.
- Added: `rubric_check.py --strong` checks the 🔎 lines on the strong judge.
- Changed: the rubric check judges the replies of its last round; a failed judge call keeps what it said; a dry run says what a resume keeps.

---

### Asking

- Changed: a decision of the user's gets a recommended answer, so a yes or no question carries the agent's view too.
- Removed: "ask as many questions as you need"; several questions are still allowed.

---

### Formatting

- Changed: a bare number of any kind needs its title, such as a step or an item, not only a question number.
- Removed: "never overuse emoji".

---

### Honesty

- Changed: the line on cheating is about the reply now: never hide what you skipped, loosened or retried to make something pass.

---

### Challenge

- Changed: "doubt every premise" no longer adds "check each one"; how the work is done is left to the host.

---

### General

- Removed: The `[MAYBE]` tag, which no rule used.

---

## 0.1.15 — 2026-11-12

---

### Honesty

- Added: stop when instructions conflict, and go by a tree: follow an answer the user gave before, or an instruction that says it wins, or ask.
- Added: never soften a thing to spare the user's feelings.
- Changed: a guess is anything you did not check. Mark it where you make it, say what you checked where you state it, and say what you did not do.

---

### Challenge

- Added: say what you would and would not do, and name a better way when you see one.
- Changed: Challenge keeps to doubt, and a premise that fails is said first.

---

### Replies

- Added: every reply has a shape, drawn as a template: a lead that answers on its own, parts in order of importance, then the ending. It comes from news writing.
- Added: define, discuss, do, drawn as a tree. An undefined task gets a definition first; a clear one is announced, then done.
- Added: say what changed since the last reply.
- Added: count as decided only what the user decided. The agent's own advice stays open until the user takes it.
- Changed: the 📍 line is a short block, one item a line.
- Changed: when the user asks about several things, the reply answers the main one and lists the rest, with no offer.

---

### Structure

- Added: a list gets its count first, and a command never sits inside a sentence.
- Changed: every command, code, setting or output goes in a code block. Backquotes are for short names, and quotes go in blockquotes, word for word.
- Changed: an arrow waterfall is only for a chain of causes and effects. The part of a bullet after its key is one whole sentence.

---

### Wordings

- Added: plain written language, the verb itself, checkable claims, numbers with what they compare with, and one name for one thing.
- Changed: say things straight, and cut every word that carries nothing while keeping sentences whole. Humor is a plain `[YES]`.

---

### Asking

- Added: ask only what changes the next step and only the user can answer.
- Added: every question starts with 💬, and a recommended option comes first.
- Changed: the end of a reply follows a tree. A plain answer ends with no question, and a clear step is taken, not asked.
- Changed: a tree says when to recommend. A decision of the user's gets a recommendation; a fact only the user knows does not.
- Changed: one thing in one question, with its context first. "A fact only I know is asked" moves here from Challenge.

---

### Docs

- Added: `PHILOSOPHY.md` gains parts on the four quadrants, emotion in the emoji and news writing. New files: `eval/FINDINGS.md` and `TODO.md`.
- Changed: README and `PHILOSOPHY.md`: the eight words are in order of importance.

---

### Eval

- Added: a yes or no rubric, `rubric-yesno.md`, with red flags and one overall score per arm. `rubric_check.py` and `flag_check.py` check the rubric itself.
- Added: `--smoke`, `--none` for an arm with no plugin, a budget per task, sessions clean of the runner's setup, and tasks for the new rules.
- Fixed: a run fails when the session did not load its arm's plugin.

---

### Formatting

- Changed: emotion goes in the emoji to keep the words plain. A file name is a link every time it is named.

---

### Install

- Fixed: `install-claude.sh` updates a plugin that is already installed.

---

## 0.1.14 — 2026-11-10

---

### Structure

- Added: Structure is its own section, after Replies, with six parts: Drawings, Tables, Bullet Points, Headings, Quotes and Code Blocks. The rules moved there from Formatting. Formatting keeps emoji, links, URLs, IDs and line numbers.
- Added: simplify first, then give structure to what is left.
- Added: draw the content whenever it has a shape. Bullet points are the fallback for content without a shape. A tree also covers branching decisions.
- Added: every level of a drawing has the same indent. A drawing with boxes or columns that must line up is in English only, because wide characters such as Chinese and emoji break the alignment. An English drawing lines up its columns with spaces. A drawing with Chinese labels stays unpadded, or puts each note on the next line, where it lines up in any font.
- Added: a blockquote holds quoted text and reminders that need no emphasis.

---

### About Me

- Added: "I take in a drawing faster than a list."
- Added: "I forget what the last reply said." Every reply stands on its own and says again what the reader needs from an earlier one. A question number is never used bare, the same as a code or an ID.

---

### Asking

- Added: a clear answer is decided and reported, not asked. One question holds one decision. Anything that needs confirmation is asked as a question.
- Changed: the limit of one question per reply is gone. A reply asks as many as it needs, numbered Q1, Q2, each of a fixed type: multiple choice, multi-select, yes/no, quick or ranking. The open type is replaced by quick. A strict limit made the model squeeze several questions into one.
- Changed: only a choice that asks for a decision carries a recommendation.
- Changed: a yes/no question stands alone, with no "(yes/no)" hint after it.
- Changed: every reply ends with one way forward: questions when an answer is needed, otherwise the next step. This replaces the "suggest a next step" rule in Replies.

---

### Challenge

- Added: a premise that is a fact only the user knows is asked before it is built on.

---

### Install

- Added: `install-claude.sh` installs the Claude Code plugin, or updates it when it is already there. Then it checks that the plugin is installed and enabled. `--check` runs only the check.
- Changed: the README shows two ways. For Claude Code, the two CLI commands or one curl line. For any agent, one line to paste, which sends it to `INSTALL.md`. `INSTALL.md` is now written for the agent: Claude Code runs the script, and Codex or another agent reads the rules and decides how to add them to the user's instructions.

---

### CI

- Added: a `tests` workflow runs the eval tests. A new test fails when `codex/AGENTS.md` and the output style differ in more than the frontmatter and the question-tools line.

---

### Eval

- Added: rubric items D16 (shape drawn), D17 (one decision), D18 (needed question) and D19 (blockquotes); a `shape-zh` chat task; mechanical checks that count drawings, tables, quotes, headings, replies that end asking, and lines.
- Changed: rubric C2 is "Depth fit", C4 follows the Structure section, D2 is "Way forward", D8 and D14 follow the asking rules. E2 is removed, since drawing is now required.

---

### Replies

- Changed: Simple is the default: a few lines, no headings. Detailed comes when the user asks for more, or when Simple would mislead: one thing only, with headings. Before, a short answer picked Simple. Three evals on 2026-11-10 showed that a principle alone ("as simple as you can") left short questions three to five times longer.

---

### Formatting

- Changed: "Never reply in paragraphs only" is now a positive `[YES]` rule in Structure: give every reply some structure.

---

### README

- Changed: a new order. A hero image, an intro with eight keywords (Simple, Honest, Structured, Predictable, Focused, Standalone, Asking, Opinionated), what you get, install, how it works, examples, then the rules. "How it works" says the plugin sets only the output style, with the Claude Code docs as the source.
- Changed: the plugin-on examples are re-recorded with the new rules, a sign-in flow example shows a drawing, and the plugin-off reply folds away. The comparison table follows the new rules.

---

### Docs

- Changed: `PHILOSOPHY.md`: why the rules look the way they do. What a reply should be, how the rules are written, and what the plugin leaves alone. The README's docs quotes and background reading move there.
- Changed: `assets/hero.svg` and `assets/hero.zh-CN.svg`: a fed-up user's message to their agent after a long session, with the reply rules highlighted.

---

## 0.1.13 — 2026-11-09

---

### Replies

- Added: when the big picture changes, the reply opens with `📍 <goal> · decided: <list> · open: <list>`. Drift points back to the goal.

---

### Wordings

- Added: a coined term or short name is defined the first time it appears.

---

### Eval

- Added: rubric D8 accepts yes/no and open questions without options, as the rule allows.
- Added: a `long-discussion-zh` task with a mid-way reversal, rubric items F4 (📍 anchor) and D15 (terms defined), and an `anchors` mechanical check.

---

### Formatting

- Changed: each part of a long reply has a heading, with a Markdown `---` line above each heading after the first, after a blank line. This replaces the `─` title line: a long `─` line wraps on a phone, and it took the heading's place.

---

## 0.1.12 — 2026-11-09

---

### Formatting

- Added: start each part of a long reply with a title line, `───── <title> ─────`, since a Markdown `---` may show as plain text.

---

## 0.1.11 — 2026-11-07

---

### Eval

- Added: `eval/eval.py` compares two versions in one command, with automatic blind judging, free mechanical checks, a new many-items task, and rubric items for the new reply rules.
- Added: a required `--budget` covers runs and judging, with a cap on every call, a ledger, `--dry-run`, and resume. Results stay usable when the budget stops a run.
- Added: a `design-flaw-zh` task and a rubric item for raising a flawed premise first.
- Changed: Eval moved from `examples/eval/` to `eval/`.

---

### Challenge

- Added: a new section. List the premises the work relies on, yours and mine, check each one, and show the ones that matter.

---

### Replies

- Added: go one thing at a time. Many items get a summary first, then an offer to go through them one by one or in batches, with overall progress in every reply. Several questions at once: pick the main one and offer the rest.

---

### General

- Changed: Pushing back, holding a position and opening a discussion move from Honesty to Challenge.
- Fixed: Conflicts between rules: file links apply outside code blocks, the URL space rule applies to bare URLs, and a reply ends in a fixed order: next step, question, options, reasons.

---

### Docs

- Changed: `CLAUDE.md`: rewritten in the rule's own tagged format, with a map and rules for writing, changing, testing and releasing.

---

## 0.1.10 — 2026-11-03

---

### Wordings

- Added: a new section. Phrase things positively, use fewer connectives, never use double negatives, never chain parallel clauses in one sentence. The light touch of humor moves here.

---

### Honesty

- Added: report finished work truthfully. It replaces "summarize the work".

---

### Formatting

- Added: each tool gets a `[WHEN]` case: bullets, tables, ASCII trees, diagrams, arrow waterfalls for cause and effect, mind maps. Commands, code and settings go in their own code block.
- Changed: one point per bullet instead of one sentence. Folders become links too. Line numbers are banned in any form, even where other instructions ask for them. The bare-ID rule moves here from Replies.

---

### Asking

- Added: one question per reply, explained first. Four types: multiple choice with 2 to 4 options, open, ranking, yes/no.
- Changed: only multiple choice carries a recommendation; its reasons are bullets.

---

### Replies

- Changed: Simple is a very simple explanation; Detailed covers one thing only.

---

## 0.1.9 — 2026-11-03

---

### Honesty

- Added: say what you actually verified.

---

### Replies

- Added: when we drift from the original goal, say so. Suggest a next step at the end when there is one the user can take. Maybe a light touch of humor.
- Added: questions with a short answer use Simple mode, defined as a few lines with no headings. Detailed mode uses headings.

---

### Formatting

- Added: never reply in paragraphs only. One sentence per bullet, preferably `- **key**: description`. Table cells are words and phrases. Code blocks hold snippets, not chunks. ASCII diagrams, trees and mind maps are listed as tools.
- Added: when you changed code or text, show the key change in a `diff` block.

---

### General

- Added: An A/B eval in `examples/eval/`: tasks, a rubric, and scripts to run, blind and score versions.
- Changed: The rules (not About Me) and the Codex copy are rewritten as flat bullets tagged `[YES]`, `[NO]`, `[MAYBE]` or `[WHEN]`, in that order within each section. `[WHEN]` lines read "situation: what to do".
- Changed: Asking is split into three `[WHEN]` rules: where the question goes, recommending an option, and giving the reason.

---

## 0.1.8 — 2026-10-28

---

### General

- Changed: The recommended option of a question is marked with ✅ right after its letter. The reason goes in a separate section underneath the options list.

---

## 0.1.7 — 2026-10-28

---

### General

- Changed: New assumption under About Me: the user easily loses track of the bigger picture.
- Changed: Emoji also show your attitude, not only meaning.
- Changed: The four plugin-on examples are re-recorded with 0.1.7, and both READMEs name the model each example ran on.
- Changed: Options of a question are a Markdown bullet list (`- A. …`), so they render as a list.

---

## 0.1.6 — 2026-10-28

---

### General

- Added: A Formatting section, split out of Replies, in the rule file and the Codex copy.
- Added: Reply rules for file names (linked), URLs (spaced, long ones as short links), line numbers (quote code instead) and small diffs (`diff` blocks).
- Added: Emoji with fixed meanings (✅ recommended, ❌ error, ⚠️ ❗ 🚨 by strength, and more).
- Added: A Formatting row in the rules table of both READMEs.

---

## 0.1.5 — 2026-10-25

---

### General

- Changed: The opinion rule is shorter: "I want your opinion."

---

## 0.1.4 — 2026-10-25

---

### General

- Added: A References section in both READMEs.
- Added: `plugin/evals/` (`zh-chat`, `zh-agent`) so the language check can be re-run with `claude plugin eval`.
- Changed: New rule under About Me: assume the user wants your opinion, not just the facts.
- Changed: The first line of `README.zh-CN.md` is now "一套不让你过载的回复规则", because the earlier wording read like a translation.

---

## 0.1.3 — 2026-10-25

---

### General

- Changed: The description now says "easy to read and structured": "A reply rule that keeps answers easy to read and structured, stays honest, and avoids overwhelming you." It changes everywhere the 0.1.2 description was.

---

## 0.1.2 — 2026-10-25

---

### General

- Changed: One description everywhere: "A reply rule that keeps answers easy to read, stays honest, and avoids overwhelming you." It is in `plugin.json`, `marketplace.json`, the output style's frontmatter and the first line of both READMEs, and it no longer puts Claude Code first.
- Changed: README shows complete, untrimmed output, re-run with the 0.1.1 rules and with `CLAUDE.md` files disabled on both sides.
- Changed: `examples/` has the new raw outputs, the first batch, and all 20 repeat runs. It lists the misses.

---

## 0.1.1 — 2026-10-25

---

### General

- Removed: The Research and Development sections of the output style. They are work habits, not reply rules, so the plugin now holds reply rules only: about me, honesty, replies and asking. I moved the two sections to my own `~/.claude/CLAUDE.md`.
- Fixed: The README rules table said "one question". The rule only says that questions go last.

---

## 0.1.0 — 2026-10-25

First public release.

---

### General

- Added: The plugin: my personal preferences, loaded as a forced output style (`plugin/output-styles/i-am-overwhelmed.md`) so they are in the system prompt of every session.
- Added: `README.md` and `README.zh-CN.md`, built on real before-and-after output.
- Added: `examples/`: the raw outputs behind the README, the fixture, and what to know before trusting them.
