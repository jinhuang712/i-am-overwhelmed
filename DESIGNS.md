# Designs

A user's message goes in and a reply comes out. Between them sits one file of rules, which the host adds to the agent's instructions on every request. The design is that file: who it is written for, how a rule in it is built, and what it leaves alone.

i-am-overwhelmed is designed around 7 guidelines:

1. **The plugin sets only the output style**: It adds no hooks, skills, tools or `CLAUDE.md`.
2. **Every rule is one line with one tag**: A rule with a shape is a drawing under its own heading.
3. **A condition sits where it applies**: It lives in a tree, in the template of a reply or in a rule on every such thing.
4. **The rule file follows its own rules**: It is easy to skim and speaks in the first person.
5. **Every line pays for itself**: The file is sent with every request.
6. **The rules are in our own words**: They name no genre and copy no standard.
7. **One set of rules serves every agent**: A host gets a line of its own only where it needs one.

---

## 1. The plugin sets only the output style

Claude Code splits the job three ways: `CLAUDE.md` for what the agent should know, an output style for how it responds, and a hook for anything that has to be guaranteed. The plugin is the middle one. Its output style keeps Claude Code's own coding instructions and stays after a compaction.

```
Claude Code
├── system prompt
│   ├── coding instructions    kept as they are
│   └── output style           the one thing this plugin sets
├── CLAUDE.md                  untouched
└── hooks, skills, tools       untouched
```

A line is judged by its wording and not by its effect. It belongs when it says what a reply holds or how the talk goes, whatever follows in the work.

The cost is that nothing is guaranteed: most replies follow the rules, and not all.

**Ask**: Can a line of the rule file do it, and is it worded as a rule for the reply?

- **Stance**:
  - [The rules are about the conversation, and the work stays with the model](PHILOSOPHY.md#what-do-the-rules-leave-alone)
  - [A rule says what a reply must hold, and the work changes to meet it](PHILOSOPHY.md#how-does-a-rule-on-the-reply-reach-the-work)

---

## 2. Every rule is one line with one tag

A rule carries `[YES]` for "do it" or `[NO]` for "never do it". A tag forces a rule to be concrete, tells the model what kind of rule it reads, and fixes its strength. One rule can be added, removed, compared and tested alone, and a person can check a reply against the list one line at a time.

A rule with a shape, such as branching decisions, is a drawing. It has its own heading at the end of its section and no tag. One sentence before it says why it is there and then what to do with it.

The cost is that a rule cannot carry an example or a nuance. A rule that needs either becomes a tree or is cut.

**Ask**: Is it one line that a person can check a reply against?

- **Stance**: [A principle comes first, and a definition comes only when a test shows the principle is not followed](PHILOSOPHY.md#how-strict-is-a-rule)
- **Decisions**:
  - [001: The rule file has two tags and no `[WHEN]`](specs/decisions/001-two-tags-and-no-when.md)
  - [006: A drawn rule has its own heading and no tag](specs/decisions/006-a-drawn-rule-has-its-own-heading.md)

---

## 3. A condition sits where it applies

A condition names one moment, such as "each time you changed code or text", and never a catalogue of cases. It lives in 1 of 3 places: a tree, the template of a reply, or a `[YES]` on every such thing. A line that leaves the model to say whether a situation holds is often judged as not met.

The cost is that a condition about the state of the talk, such as "we drift from the original goal", still needs the model's judgement. The design gives it a place and not a proof.

**Ask**: Where is the one moment this applies, and which tree or template line holds it?

- **Stance**: [The rules are about the conversation, and the work stays with the model](PHILOSOPHY.md#what-do-the-rules-leave-alone)
- **Decisions**:
  - [001: The rule file has two tags and no `[WHEN]`](specs/decisions/001-two-tags-and-no-when.md)
  - [002: One template names every block of a reply](specs/decisions/002-one-template-names-every-block.md)
  - [003: A tree decides what one reply covers](specs/decisions/003-a-tree-decides-what-one-reply-covers.md)
  - [004: A recap takes the place of the big picture block](specs/decisions/004-a-recap-takes-the-place-of-the-big-picture-block.md)
  - [008: Every part of a reply is built as a heading, a claim and its evidence](specs/decisions/008-every-part-is-a-heading-a-claim-and-its-evidence.md)
  - [009: A discussion has its own branch in two trees](specs/decisions/009-a-talk-has-its-own-branch.md)

---

## 4. The rule file follows its own rules

The file is easy to skim, it says what to do, and it speaks in the first person: "tell me" and not "tell the user". Every section opens with one sentence in the reader's own voice that says why its rules are there. Rules are phrased positively. We believe a model copies the manner of its instructions.

The cost is that the file cannot explain itself at length. The reasons live in the philosophy.

**Ask**: Would this line pass as part of a reply under these rules?

- **Stance**: [The reader's own reading is the strongest signal](PHILOSOPHY.md#how-do-we-know-a-rule-works)

---

## 5. Every line pays for itself

The file is sent with every request, so every line has a cost. A new rule goes into a rule that exists whenever it can. Two short rules are better than one long rule, and a line that repeats another is removed.

The cost is that a fault which shows up once gets no rule of its own.

**Ask**: Which line that exists can hold it?

- **Stance**: [A reply is also context](PHILOSOPHY.md#who-else-reads-a-reply)
- **Decisions**:
  - [010: The rule file names the reader's five wants](specs/decisions/010-the-rule-file-names-five-wants.md)

---

## 6. The rules are in our own words

The rules say what to do in plain words of our own. They use the standard term for a thing and coin no phrase, since the agent is to follow them into a rigorous register. They are inspired by ASD-STE100 and copy none of its text. They name no genre: every time "press release" was in the instruction, the model brought the dateline and the PR voice with it. A rule that needs Chinese is written natively in a technical register.

The cost is that a reader cannot look a rule up in a standard.

**Ask**: Does the line name a genre or copy a source?

- **Stance**: [Short means no empty words, not no grammar](PHILOSOPHY.md#what-carries-over-from-news-writing)

---

## 7. One set of rules serves every agent

The rules are agent-neutral. The file for Codex differs from the output style in 2 places only: the frontmatter and the line on question tools.

The cost is that a rule cannot lean on a feature that only one host has.

**Ask**: Does this line hold for an agent other than Claude Code?

- **Stance**: [The reader comes before any rule](PHILOSOPHY.md#who-are-the-rules-for)
