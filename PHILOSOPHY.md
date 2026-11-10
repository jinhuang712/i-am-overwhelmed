# Philosophy

Why the rules look the way they do. The rules themselves are in [`plugin/output-styles/i-am-overwhelmed.md`](plugin/output-styles/i-am-overwhelmed.md).

Some lines below are tested and some are beliefs. A belief is marked with "we believe".

## Part 1. What a reply should be

### Who it is for

The rules serve one reader:

- They are tired or overloaded.
- They are doing other things at the same time.
- They skim.
- They want an opinion.
- They lose track of the bigger picture.
- They forget what the last reply said.

The rule file starts with this reader, under "About Me", before any rule. A rule covers the cases we thought of. The reader covers the rest: when no rule fits, the model can still ask what this person needs.

### Four quadrants

A conversation has two sides, and each side knows things the other does not.

|  | The agent knows | The agent does not know |
|---|---|---|
| **I know** | Shared | The agent's blind spot |
| **I do not know** | My blind spot | Unknown |

The rules have one aim: make Shared larger.

| Quadrant | How it gets smaller | Words |
|---|---|---|
| The agent's blind spot | The agent asks | Asking |
| My blind spot | The agent says it, in a form I can take in | Honest, Opinionated, Simple, Structured, Predictable |
| Unknown | The agent doubts the premises and checks them | Opinionated |

Opinionated works on two quadrants. A better way that the agent sees and I do not is in my blind spot, the same as a problem it does not report.

- **My blind spot has two halves**: what the agent did not say, and what it said but I could not take in. A reply I cannot read leaves me as blind as a reply that hides the problem. This is where the name of the plugin comes from.
- **A definition works on both blind spots at once.** The agent says how it reads the goal, the scope and what done means. I see its reading, and my correction tells it mine. So the order is define, discuss, do.
- **Shared leaks.** I forget what the last reply said. Focused and Standalone keep it from leaking.

The model is adapted from the [Johari window](https://en.wikipedia.org/wiki/Johari_window) (Luft and Ingham, 1955), which describes one person and the people around them. Here the two sides are the reader and the agent.

### Eight words

The most important word comes first.

| Word | What it means | Where it lives in the rules |
|---|---|---|
| Honest | Problems, guesses and unverified claims are said out loud, and nothing is softened | Honesty |
| Simple | A few lines first. Detail when the reader asks | Replies |
| Structured | Content with a shape is drawn. Bullets hold the rest | Structure |
| Asking | Facts only the reader knows are asked first | Asking |
| Opinionated | It doubts the premises, pushes back, says what it would and would not do, and names a better way | Challenge |
| Focused | One thing at a time, and a note when the talk drifts | Replies |
| Standalone | Every reply can be read on its own, with no scrolling back | Replies, Formatting |
| Predictable | The same formats and the same emoji meanings every time | Formatting, Asking |

Predictable is the quiet one. The reader can skim only when they know where the answer is, where the question is, and what ⚠️ means.

### Emotion goes in the emoji

A model wants to show how it feels about what it says: sorry, pleased, doubtful. In words, that feeling becomes padding, hedging and softening.

```
the model wants to show a feeling
├── in words       the reply gets longer and softer
└── in an emoji    the words stay straight
```

So the rules give the feeling a place of its own. An emoji carries it, with a fixed meaning, and the sentence next to it says the plain thing. We believe this is what lets "never soften" and "say things straight" hold.

### A reply is also context

A reply has two readers: you, now, and the model, on every later turn.

```
the model prints a reply
└── the reply stays in the conversation
    └── the model reads it again on every later turn
        └── a messy reply keeps adding noise
```

- **This is how a session works**: what the model prints becomes part of what it reads next.
- **So a messy reply costs twice**: you read it once, and the model reads it many times.
- **We believe long sessions drift more for it.** We reasoned this out and have not measured it.

## Part 2. How the rules are written

### We don't teach the model how to work

- **The rules are about the conversation.** They say how to talk with the reader. The engineering stays with the model and with Claude Code's own instructions.
- **We don't list scenarios.** No list of scenarios is ever complete, and a long list makes rules collide.
- **A `[WHEN]` is a trigger.** It names the moment a rule applies, such as "You changed code or text". It is one moment, not a catalogue of cases.

### Principles first, then a definition where a principle is not enough

- **A principle** asks the model to judge: "Draw the content whenever it has a shape."
- **A definition** is something a person can check: "Simple: a few lines, no headings."
- **We write the principle first.** We add a definition only when a test shows the principle is not followed.

The test that taught us this, on 2026-11-10, with a short chat question:

| The rules said | Lines in the reply |
|---|---|
| Simple, with its definition | 8 |
| No definition, and "give each part a heading" | 40 |
| The same, plus "write as simply as you can" | 32 |
| The same, plus "simplify first" | 27 |
| Simple by default, with its definition | 10 |

A principle lost to an unconditional rule that stood next to it. The numbers are in [`eval/README.md`](eval/README.md).

### Four tags

| Tag | Strength |
|---|---|
| `[YES]` | Always |
| `[NO]` | Never |
| `[MAYBE]` | The model's call |
| `[WHEN]` | In the situation it names |

- **A tag forces a rule to be concrete.** A tagged line cannot grow into a paragraph of parallel clauses.
- **A tag tells the model what kind of rule it is reading**, before it reads the rule.
- **A tag fixes the strength.** We believe words such as "should" and "try to" read as open to negotiation.
- **A person can check a reply against the list**, one line at a time.

### Discrete rules, in plain words

Each rule is a unit of its own. Most are one line. A rule with a shape is a drawing: the end of a reply is a decision tree, because a tree is easier to follow than the same branches in sentences, for the reader and for the model.

- **The file is sent with every request**, so every line has a cost. It must stay short.
- **One rule can be added, removed, compared and tested alone.** The eval's rubric and the changelog both follow the rules one by one.
- **The file follows its own rules.** It is easy to skim, it says what to do, and it speaks in the first person: "tell me", not "tell the user". We believe a model copies the manner of its instructions.
- **The wording is inspired by ASD-STE100**, a standard for simplified technical English. The rules are in our own words.

### Two rules that collide get a scope

When two rules collide, we first decide where each one applies. A third rule comes last.

- **Simple and the question format**: Simple said "no headings", and the question format said "reasons in a separate section". The model used bold text as a heading. The fix was to say which rule owns the end of a reply.
- **Detailed and drawings**: one line said Detailed comes "with headings and drawings". Short replies stopped drawing. The fix was to remove two words.

### Rules are tested

- **Every rule change runs through the eval**: the old rules against the new, on the same tasks, with a blind judge.
- **The judge favours the rule text.** The rubric is written from the rules, so a version that states a rule scores well on it. We read line counts and quotes as well as totals.
- **The wording of a trigger decides whether a rule is followed.** "You show a local difference" lost most `diff` blocks. "You changed code or text" brought them back.
- **The samples are small.** They show a direction.
- **The reader's own reading is the strongest signal**: which reply they pick blind, and how often they have to say "simpler".

## Part 3. Boundaries

### Only the output style

```
Claude Code
├── system prompt
│   ├── coding instructions    kept as they are
│   └── output style           the one thing this plugin sets
├── CLAUDE.md                  untouched
└── hooks, skills, tools       untouched
```

Claude Code's [docs](https://code.claude.com/docs/en/output-styles) split the job three ways: "CLAUDE.md for what Claude should know, an output style for how it responds, and a hook for anything that has to be guaranteed." This plugin is the middle one. It sets `keep-coding-instructions: true`, which the docs describe as "changing how Claude communicates but still want it coding the same way."

### What it does not try to do

- **Make the model smarter.** In the examples, the model fixes the flaky test the right way with the plugin off too. The plugin changes the report.
- **Change how the model does the work.**
- **Guarantee anything.** In the docs' words, an output style "doesn't guarantee that something always happens or never happens." A thing that must always happen belongs in a hook.
- **Suit everyone.** These are one person's preferences. Fork the file and write yours.

## Background reading

These studies are background. None of them tested chat replies, so each rule is carried over by inference from web pages, lab tasks and clinical handoffs.

- Luft & Ingham (1955), The Johari window, a graphic model of interpersonal awareness, [summary on Wikipedia](https://en.wikipedia.org/wiki/Johari_window)
- Lim & Dinges (2010), [A meta-analysis of the impact of short-term sleep deprivation on cognitive variables](https://pmc.ncbi.nlm.nih.gov/articles/PMC3290659)
- Cowan (2001), [The magical number 4 in short-term memory](https://pubmed.ncbi.nlm.nih.gov/11515286/)
- Morkes & Nielsen (1997), [Concise, scannable, and objective: how to write for the web](https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/)
- Pernice (2019), [Text scanning patterns: eyetracking evidence](https://www.nngroup.com/articles/text-scanning-patterns-eyetracking/)
- Kim et al. (2024), ["I'm not sure, but...": examining the impact of large language models' uncertainty expression on user reliance and trust](https://www.arxiv.org/abs/2405.00623)
- Steyvers et al. (2025), [What large language models know and what people think they know](https://arxiv.org/abs/2401.13835)
- Bansal et al. (2021), [Does the whole exceed its parts? The effect of AI explanations on complementary team performance](https://arxiv.org/abs/2006.14779)
- Vasconcelos et al. (2023), [Explanations can reduce overreliance on AI systems during decision-making](https://arxiv.org/abs/2212.06823)
- Sharma et al. (2024), [Towards understanding sycophancy in language models](https://arxiv.org/abs/2310.13548)
- Starmer et al. (2014), I-PASS handoff program, [summary on PSNet](https://psnet.ahrq.gov/issue/changes-medical-errors-after-implementation-handoff-program)
