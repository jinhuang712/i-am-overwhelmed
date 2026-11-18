# 001. The rule file has two tags and no `[WHEN]`

Decided: 2026-11-13

---

## The problem

A `[WHEN]` rule read "situation: what to do". It left the model to say whether the situation holds, and the model often said no. The owner saw "Simple would mislead me" and "it fits the topic" seldom acted on.

---

## The choice

The rule file has `[YES]` for "do it" and `[NO]` for "never do it". Of the 20 rules that had `[WHEN]`, 12 went into trees and into the template of a reply, 7 became a `[YES]` or a `[NO]`, and 1 was dropped.

---

## Not chosen

2 other ways:

- **Keep `[WHEN]`**: its rules were the ones least followed.
- **A fourth tag, `[MAYBE]`**: no rule used it, so it left with 0.1.16.

---

## Consequences

A condition that names a state of the talk still needs the model's judgement. The change gave it a place and not a proof. The last seven rules were reworded with no eval.
