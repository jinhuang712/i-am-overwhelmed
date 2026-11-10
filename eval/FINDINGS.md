# Findings

A running record of what the evals taught us: what helps the rules, and how to run an eval well. New findings go at the end of a section, with a date. The numbers behind them are in [`README.md`](README.md) and in [`results/`](results/).

Every line says how strong its evidence is. "One case" means one reply or one run.

## About the rules

- **The plugin is the large effect.** No plugin scored 65.0%, 0.1.14 scored 87.5% and the rules of 2026-11-10 scored 89.7%, on 17 tasks with one run each. Red flags were hit only with no plugin: twice it built on a fact only the user knew, and once it acted without asking. (2026-11-10, Opus 5.5)
- **A small change sits inside the noise.** Two points between two versions, on one run per arm, mean nothing. See "About judging". (2026-11-10)
- **A principle loses to an unconditional rule.** "As simple as you can" left short answers three to five times longer, while "give each part a heading" was followed every time. A definition a person can check, "a few lines, no headings", did the work. (2026-11-03 and 2026-11-10, two evals)
- **The wording of a trigger decides whether a rule is followed.** "You show a local difference" lost most `diff` blocks. "You changed code or text" brought them back. (2026-11-03)
- **The worst replies come from two rules that collide, or from one rule followed too far.**
  - "Every reply ends with one way forward" made 0.1.14 close a plain fact answer with a made-up question. On that task it scored under no plugin. An ending tree fixed it. (2026-11-10, both runs of two)
  - "Show me the premises that matter" and "ask me a fact only I know" together made replies list their assumptions and build on them. (2026-11-10, read in replies)
  - "Keep several things brief" and "pick the main one, then offer the rest" say opposite things. "Offer" came out as "shall I go on?". (2026-11-10, two replies)
- **A `[NO]` may work where a `[YES]` did not.** "Put every command in its own code block" left the backquotes item at 2.1 of 3 in both versions. After "never put a command inside a sentence" one task scored 3. Another task still had `git status` inside a sentence. (2026-11-10, one case each way)
- **A model does not see its own inference as a guess.** A reply said a second case was "fixed too" after it had checked only the first. "Say when you're guessing" did not stop it. The rule now defines a guess: anything you did not check. In the next run the same task marked an unchecked choice, and still stated two inferences as facts. (2026-11-10, one case each)
- **Humor does not come from a rule.** It scored 0.6 of 3 as `[MAYBE]` and as `[YES]`. (2026-11-10)
- **Three or more things still sit inside one sentence.** The line fired on 14 of 20 replies, with and without the plugin. "Never chain parallel clauses; split them into bullets" is in the rules and is not followed. (2026-11-11, one judge)
- **A rule that reads oddly to the owner is not added.** Three lines that were derived from a list of language habits were dropped the moment they were read. Rules come from a real annoyance first. (2026-11-10)

- **Withdrawn: "the plugin brings emoji with no meaning".** The first rubric check showed 7 of 14 plugin replies against 0 of 6 without. A reading of the hits showed the judge was wrong: it did not know the legend, and replies with no plugin simply have no emoji. The line on sentences with no subject was dropped as well, since the owner does not count that as a fault. (2026-11-11)

- **A press release, as a one-line style, puts the result and its worst catch in the first line.** "todo.py gets a sort command, but only 1 of 6 todos can be sorted by date." Its work report on `fix-test-zh` was a third as long as ours and still said that only local runs were checked. Its costs: it wrote advice as a decision the team had announced, cited unnamed sources ("业内人士"), put a dateline and "（完）" on every reply, and ran about 1.4 times longer on chat tasks. The rubric scored it 46% to 71% against our 92% to 98%; the rubric is written from our rules, so read the replies, not the gap. (2026-11-11, Opus 5.5, 6 tasks, 2 runs each, results in `results/2026-11-11-press-release-vs-dece4e0-opus-5-5/`)
- **A news tone, without the news format, reads short and plain.** Four one-line wordings were tuned by reading, one run per task on the same 6 tasks. "Press release style" put a dateline and "（完）" in every intact reply, and wrote advice as an announcement. "News report tone, start with the body" left a dateline or a headline in 2 of 6, and a reporter's voice ("业内", "用户今日请求") in 2. "Answer me directly" took both to 0 of 6. "News brief" in place of "news report" cut the length by about a third: shorter than our rules on 4 of 6 tasks, a third as long on the work report, which still said CI had not run. The wording that held over 12 replies: 「请你用新闻简讯的语气直接回答我，第一句就写正文。」 (2026-11-11, Opus 5.5, $1.73, results in `results/2026-11-11-news-tone-*`)
- **A one-line style breaks about a third of the replies.** Over five wordings, 11 of 36 replies on Opus showed the model's thinking at the top, came back empty, or were unrelated text that ended in a made-up system reminder. Our rules broke none of 12 on the same tasks, and no plugin none of 6. The cause is not known. A guess: the short style, not its words, since every wording did it. (2026-11-11, Opus 5.5)

## About judging

- **A 0 to 3 scale is not stable.** Opus 5.5 judged the same four replies three times on ten rubric lines: 54% of the rule items and 58% of the degree items got the same score all three times. Nearly every miss was one point. Every eval before 2026-11-10 used this scale. (2026-11-10, 40 scores)
- **Yes or no is stable.** The same rule items as pass or fail: 86% to 89% identical over three passes, for Opus and for Haiku. (2026-11-10)
- **A degree item becomes stable when it is split into several yes or no questions.** "Length fit" became "is a point made twice", "does the reply close with a recap", "can the first sentence be deleted". 86% identical on Opus, 82% on Haiku. (2026-11-10, 28 scores)
- **Describing every level of a scale does not help.** Three degree items as 0, 1, 2 with a sentence for each level: 42% identical on Haiku, against 67% for the old lines. (2026-11-10, 24 scores)
- **One rubric line a call is not more accurate than a group of lines.** Haiku and Sonnet both agreed with Opus less when they got one line at a time. (2026-11-10, 16 scores)
- **With yes or no questions, Haiku is as stable as Opus, at a tenth of the cost.** One judging call: $0.066 on Opus, $0.007 on Haiku. Their majority answers agreed on 47 of 56 questions. (2026-11-10)
- **Most of a judge's wavering is between N and NA, and it means nothing.** On 132 lines and 20 replies, Haiku gave the same answer three times on 79% of the cases. Six flips in ten were between "no" and "not applicable". With the two counted as one answer, 92% were stable, and 13 lines stayed weak. Ask a judge for Y or not Y. (2026-11-11, 2,640 answers, $0.96)
- **One round does not settle which lines are weak.** Eleven weak lines were reworded and their decks judged again: six got steadier, four got worse, and six lines that had been steady turned weak with no change to their words. On 20 replies a line's own number moves by several replies between rounds. Park a line only when it is weak in two rounds. (2026-11-11)
- **A plainer wording can make a line too wide.** "Names a better way than the one the user asked for" became "names a way the user did not mention": steadier, and it fired on 19 of 20 replies. It was put back. (2026-11-11)
- **The judge's noise has a size.** The same 20 replies, judged three times: one reply's score moved by 2.4 points on average and 6.1 at most, and the mean of the 20 moved by 1 point. A gap of 1 or 2 points between two versions, on one pass, is nothing. (2026-11-11)
- **A line that most replies meet still tells something.** A good sign on 17 of 20 replies marks the 3 that lack it. A line stops telling only when every reply answers the same. The agent wanted three such good signs out, and the owner kept them. (2026-11-11)
- **Read what a line hit before you trust its count.** Four lines were checked against the replies they fired on. Two held: "a bullet point of two sentences or more" and "a file with no link" agreed with a simple script on 17 of 20 replies each, so the faults are real and common. A closer look at the links: replies with no plugin never link, and replies with the plugin link a file the first time and name it bare after that. Two did not: "an emoji that carries no meaning" fired on 🤔 and ⚠️ used as the legend says, because the judge had never been shown the legend; and "two or more topics a section each" counted "Cause" and "Fix" of one answer as two topics. (2026-11-11)
- **With the legend in the deck, the emoji lines steadied.** "An emoji that carries no meaning" went from 7 hits to 3, and from 19 to 20 of 20 stable. It was parked all the same: "no meaning" has no test. After three rounds the rubric stands at 93% stable, with every deck at 90% or more. (2026-11-11, $1.72 in all)
- **A judge knows only what the deck tells it.** A line that leans on something outside the reply, such as the emoji legend, needs that thing written into the deck. (2026-11-11)
- **A line can be stable and still too wide.** "Writes cause and effect as prose, with no arrows" fired on 18 of 19 replies, and "a bullet point holds two points" on 17 of 19. A line that fires on nearly every reply tells nothing. (2026-11-11)
- **A third of the lines never fired on 20 replies**, most red flags among them. They are not wrong; the replies on disk hold no case for them. A line needs a reply that breaks it before it can be checked. (2026-11-11)
- **The questions that stay unstable need the transcript checked**, such as "claims match evidence" and "a closing recap". Both models got 2 or 3 of 4 on them.
- **Stable is not the same as right.** A judge can be wrong the same way every time. Three judges on the old scale agreed with each other on 10 of 16 scores at best.
- **The rubric is written from the rules, so it favours the version that states a rule.** No plugin loses points for formats it was never told about.
- **Every real finding came from reading the replies.** The scores pointed at a task. The cause was found in the text each time: the reply that never answered the edge cases, the claim that was not true, the task that asked four things.

## About tasks

- **A task's words must not do a rule's work.** "Keep it simple", "you decide", "give me a recommendation" and "by the way" were all in tasks, and each handed a rule its result. (2026-11-10)
- **A task asks one thing**, unless it tests a message that asks several. The drawing task asked for a flow and three edge cases. It tested how a reply handles a crowded question, and the new rules lost 12 points on it. With one question they led by 8. (2026-11-10)
- **A task that makes the model want to read files needs tools.** As a chat task with no tools, "write a deploy script for our service" made the model write made-up tool calls up to the output limit: 128,000 tokens, three times. (2026-11-10)
- **The user's turns in a multi-turn task are fixed.** A question the model asks in turn 1 is never answered, so the same open questions come back in every later turn. Read those turns with that in mind.
- **One run per arm shows a direction only.** The compound task scored 95.0 for 0.1.14 in one run and 81.2 in the next.

## About the tool and the money

- **Claude Code skips a `--plugin-dir` it cannot find and says nothing.** A relative results path left every arm with no plugin. 32 runs went through before a read of the replies showed it. The path is absolute now, and each run checks the session's plugin list.
- **`--max-budget-usd` is checked between turns only.** One reply ran to $2.56 against a $0.15 limit. A reply is now capped at 16,000 output tokens. That cap has not been seen to stop a reply yet.
- **On a subscription the costs are list prices, and the runs use up the usage limit.** One full run used up a 5-hour limit, and every judge call failed.
- **A hold is not a spend.** The tool holds a run's whole limit before the run starts. A limit set too wide, or judging money kept back twice on a resume, stops runs although the money is there.
- **A smoke run is cheap and it finds things.** All 19 tasks once on Haiku cost $0.17: a chat run $0.001 to $0.002, the four-turn agent run $0.055. Every run came through, the plugin loaded, and both trap tasks stopped at the conflict and named it. (2026-11-11)
- **An agent's work folder must be a repository of its own.** The folder sits inside this repository, so the agent's git commands acted on this repository, and one agent read this project's CI file as if it were the fixture's. Each work folder now gets its own `.git`. (2026-11-11, seen in a smoke run and in a run of 2026-11-10)
- **Smoke the tool on a cheap model before a full run.** The three faults that lost $17.79 had nothing to do with how good the model is.
- **Estimate from a measured price.** A guess for Haiku judging was ten times too high, and a guess for Sonnet was half the real cost.
- **Measured on 2026-11-10, Opus 5.5 at medium effort**: a one-turn chat run $0.02 to $0.07, a four-turn agent run $1.18, a full run of 17 tasks and three arms $11.2, its judging $2.45.

- **`--smoke --cheap-judge claude-opus-5-5` tunes a wording cheaply.** It runs the strong model once per task, on the new arm only, with no judge: about $0.43 for 6 tasks. Read the replies; the rubric would favour our rules anyway. (2026-11-11)
- **Any style can be an arm.** Commit it as the body of the output style on a throwaway branch, keep the frontmatter, and pass the branch as `--old`. The style's text is then the only difference. (2026-11-11)

## What we do not know yet

- How a rubric of yes or no questions does on a full run.
- Whether the rules do the same on Sonnet and on Codex. Every eval since 2026-11-10 ran on Opus.
- What the owner feels after some days of real use with the rules of 2026-11-10. No eval replaces that.
- Whether the three trees in the rule file get in each other's way.
