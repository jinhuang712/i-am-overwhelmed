# i-am-overwhelmed — Proposal

> A reply rule that keeps answers easy to read and structured, stays honest, and avoids overwhelming you.

---

## In short

You are tired, you are doing three other things, and you skim. Your coding agent answers with a wall of text, and somewhere in it sits the one line you needed.

The answer is a set of rules for the reply: who reads it, what it must say, and what shape it takes.

---

## Why it should exist

A reply I cannot read leaves me as blind as a reply that hides the problem. This is where the name comes from.

What I do not know has two halves: what the agent did not say, and what it said but I could not take in. An agent with no rules fails on both. In the benchmark of 2026-11-11 one prompt asked what happens after a user clicks "Sign in with GitHub". The reply with no rules ran to 50 lines under nine headings. The reply with the rules ran to 32 lines: one sentence that answers, one drawing and the 4 points that matter most.

---

### Pain points

The project eases 4 pains. Each number below comes from the eval of its date, on replies with no plugin.

---

#### A late surprise

The reply does not say what it did not check, so the gap shows up later. 18% of 57 replies said what they did not check, on 2026-11-11.

---

#### A shape written out as text

The content has a shape and the reply spells it out in sentences. 42% of 57 replies wrote a flow as text with no drawing, on 2026-11-11.

---

#### Structure that hides the answer

A short answer comes under headings, and a long list comes with no summary. 46% of 57 replies put headings on an answer though nobody asked for more detail, and 16% gave a long list with no summary first, on 2026-11-11.

---

#### A guess built on

The agent builds on a fact only I know, or acts without asking. In the eval of 2026-11-10, on 17 tasks, replies with no plugin did the first twice and the second once.

---

## The idea

Tell the agent who reads its replies, then give it rules for the talk and leave the work alone.

The reader comes first, so the agent can still ask what this person needs when no rule fits. The rules cover the reply only: what it must say, its order, its drawings, its words and its questions.

---

## What we want

5 wants. The lines under each say how the project meets it.

- **Trust what a reply says**: The reply is candid about what it knows and about where I am wrong.
  - Every conclusion states whether it was verified, not verified or inferred.
  - The reply states what was not done or was skipped as plainly as what was done, and a problem keeps its real weight.
  - A wrong premise or plan of mine is named before anything else, and the agent holds its position until I convince it.
- **Grasp the main point**: The conclusion and the structure reach me before the detail.
  - A reply opens with a conclusion that stands on its own and with its main reason.
  - Headings and drawings show how the content is built, and a mark means the same every time.
- **Keep my attention on the right things**: I know what to look at now and need nothing from further up.
  - Every reply after the first says what my attention should be on now, and a finished thing leaves it.
  - A reply carries what I need to understand it, with no scrolling back.
- **Not be flooded with information**: The amount I read and the cost of reading it stay under my control.
  - One reply handles one thing and lists the rest, and I decide what to open.
  - Sentences are whole and words are plain, with one name for a thing and a natural tone.
- **Iterate a discussion fast**: Each round costs me little and moves the talk forward.
  - Every round ends by saying whose move it is, so I correct or confirm with little input.
  - A question covers only what changes the next step and only I can answer, and it comes with options and a recommendation.

---

## What we don't want

5 things the project refuses to become:

- **A way to make the model smarter**: the model fixes the flaky test the right way with the plugin off too.
- **A set of rules for how the work is done**: the engineering stays with the model and the host's own instructions.
- **A guarantee**: an output style is a set of instructions, and a thing that must always happen belongs in a hook.
- **A style for everyone**: these are one person's preferences, and another reader forks the file.
- **A list of scenarios**: no list of scenarios is ever complete, and a long list makes rules collide.

---

## Who it is for

One reader, and the rule file opens with them. They are tired or overloaded. They are doing other things at the same time. They skim. They want an opinion. They lose track of the bigger picture. They forget what the last reply said. They take in a drawing faster than a list.

Whoever shares these traits gets the same replies. Whoever does not gets a file to fork.

---

## Risks

8 risks:

- **A rule is not followed**: an output style guarantees nothing, so each release is meant to run through the eval first.
- **The judge favours the rule text**: the rubric is written from the rules, so we read line counts and quotes as well as totals.
- **Replies grow long**: chat replies came out about twice as long in a trial on 2026-11-13, and the next benchmark measures it.
- **The file costs tokens on every request**: a new rule goes into a rule that exists whenever it can.
- **Rules collide with other instructions**: the rules ask the agent to stop at a conflict and name it.
- **The evidence is narrow**: 17 of 19 tasks are in Chinese and every run since 2026-11-10 is on Opus.
- **The Codex rules never ran**: no eval has measured them.
- **One reader judges**: the owner's own reading is the strongest signal we have, and it is one person's.
