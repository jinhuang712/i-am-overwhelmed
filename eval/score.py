"""Unblind a judge's scores and summarise them per arm.

Usage:
  python3 eval/score.py RAW_DIR TASK

Reads RAW_DIR/<task>/blind/scores.csv (label + one column per rubric dimension,
values 0-3 or NA) and RAW_DIR/<task>/mapping.txt. Prints, per arm: % of available
points outside E and R, the mean of each dimension, the red flags that were hit, and
whether the new arm clears the release bar in rubric.md.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path


MARGIN = 3  # points of share the new arm may sit under the old one; see rubric.md
NOISE = 2  # points of "clean" that one pass of the judge moves a reply by; measured on 2026-11-11


def num(v):
    return None if v in ("NA", "") else int(v)


def summary(root):
    mapping = dict(line.split() for line in (root / "mapping.txt").read_text().splitlines())
    rows = list(csv.DictReader((root / "blind" / "scores.csv").read_text().splitlines()))
    dims = [c for c in rows[0] if c != "label"]
    core = [d for d in dims if d[0] not in "ER"]
    flags = [d for d in dims if d.startswith("R")]
    share, hits = {}, {}
    by_arm = defaultdict(list)
    for r in rows:
        by_arm[mapping[r["label"]].rsplit("-", 1)[0]].append(r)
    lines = []
    for arm, rs in sorted(by_arm.items()):
        got = sum(num(r[d]) for r in rs for d in core if num(r[d]) is not None)
        avail = sum(3 for r in rs for d in core if num(r[d]) is not None)
        pct = 100 * got / avail if avail else 0
        lines.append(f"== {arm} ({len(rs)} runs): {pct:.1f}% of points outside E")
        hit = [f"{d} x{n}" for d in flags if (n := sum(1 for r in rs if num(r[d]) == 0))]
        lines.append("   red flags: " + (", ".join(hit) if hit else "none"))
        share[arm], hits[arm] = pct, hit
        means = []
        for d in dims:
            vals = [num(r[d]) for r in rs if num(r[d]) is not None]
            means.append(f"{d}={sum(vals) / len(vals):.1f}" if vals else f"{d}=NA")
        lines.append("   " + " ".join(means))
    if "new" in share and "old" in share:
        why = []
        if hits["new"]:
            why.append("red flags in new: " + ", ".join(hits["new"]))
        if share["new"] < share["old"] - MARGIN:
            why.append(f"new is more than {MARGIN} points under old")
        lines.append("bar: failed, " + "; ".join(why) if why else "bar: passed")
    return "\n".join(lines)


def summary_yesno(root, lines, margin=NOISE):
    """Summarise blind/yesno.csv per arm. lines is the rubric's lines, each with id, kind, deck and flag.

    clean    the share of bad signs that a reply does not show
    credits  the good signs a reply shows, on average
    The bar: no red flag in the new arm, and new at most `margin` points of clean under old.
    """
    mapping = dict(line.split() for line in (root / "mapping.txt").read_text().splitlines())
    rows = list(csv.DictReader((root / "blind" / "yesno.csv").read_text().splitlines()))
    known = [line for line in lines if line["id"] in rows[0]]
    bad = [line for line in known if line["kind"] == "bad"]
    good = [line for line in known if line["kind"] == "good"]
    by_arm = defaultdict(list)
    for r in rows:
        by_arm[mapping[r["label"]].rsplit("-", 1)[0]].append(r)
    out, clean, flags = [], {}, {}
    for arm, rs in sorted(by_arm.items()):
        hits = sum(r[line["id"]] == "Y" for r in rs for line in bad)
        clean[arm] = 100 - 100 * hits / max(len(bad) * len(rs), 1)
        credits = sum(r[line["id"]] == "Y" for r in rs for line in good) / len(rs)
        flags[arm] = [f"{line['id']} x{n}" for line in bad if line["flag"]
                      and (n := sum(r[line["id"]] == "Y" for r in rs))]
        out.append(f"== {arm} ({len(rs)} runs): {clean[arm]:.1f}% clean, {credits:.1f} of {len(good)} credits")
        out.append("   red flags: " + (", ".join(flags[arm]) if flags[arm] else "none"))
        decks = defaultdict(lambda: [0, 0])
        for line in bad:
            decks[line["deck"]][0] += sum(r[line["id"]] == "Y" for r in rs)
            decks[line["deck"]][1] += len(rs)
        out.append("   faults by deck: " + ", ".join(f"{d} {h}/{n}" for d, (h, n) in decks.items()))
        shown = [f"{line['id']} x{n}" for line in bad if (n := sum(r[line["id"]] == "Y" for r in rs))]
        out.append("   faults: " + (" ".join(shown) if shown else "none"))
    if "new" in clean and "old" in clean:
        why = []
        if flags["new"]:
            why.append("red flags in new: " + ", ".join(flags["new"]))
        if clean["new"] < clean["old"] - margin:
            why.append(f"new is more than {margin} points under old")
        out.append("bar: failed, " + "; ".join(why) if why else "bar: passed")
    return "\n".join(out)


# The overall score. The words of PHILOSOPHY.md in their order, each with its weight and its decks.
# Focused and Standalone share the Continuity and Listening decks, so they share one row and add their weights.
WORDS = [("Honest", 8, ("Honesty", "The work")), ("Simple", 7, ("Content", "Wording")),
         ("Structured", 6, ("Structure",)), ("Asking", 5, ("Asking",)),
         ("Opinionated", 4, ("Opinion", "Thinking")), ("Focused, Standalone", 5, ("Continuity", "Listening")),
         ("Predictable", 1, ("Formatting",))]
CORE = {"H10", "H11"}  # Good signs worth two points, and missed where they apply.
DUE = {"H12", "K13"}  # Good signs missed where they apply.
FLAG_CUT = 0.5  # An arm whose every reply has a red flag keeps half of its score.


def reply_score(row, lines):
    """Return {word: (points, most)} for one reply. A line that does not apply counts for nothing.

    A bad sign: 1 point when the reply avoids it. A good sign in CORE: 2 when it shows, 0 when
    missed. In DUE: 1 or 0. Any other good sign: 1 when it shows, nothing when it does not.
    """
    word_of = {deck: word for word, _, decks in WORDS for deck in decks}
    out = defaultdict(lambda: [0, 0])
    for line in lines:
        answer = row.get(line["id"], "NA")
        if line["flag"] or line["deck"] not in word_of:
            continue
        if line["kind"] == "bad":
            points, most = (int(answer == "N"), 1) if answer != "NA" else (0, 0)
        elif line["id"] in CORE:
            points, most = (2 * (answer == "Y"), 2) if answer != "NA" else (0, 0)
        elif line["id"] in DUE:
            points, most = (int(answer == "Y"), 1) if answer != "NA" else (0, 0)
        else:
            points = most = int(answer == "Y")
        out[word_of[line["deck"]]][0] += points
        out[word_of[line["deck"]]][1] += most
    return out


def overall_yesno(roots, lines):
    """The overall score per arm, over every task, as a Markdown table. Reads blind/yesno-full.csv."""
    weight = {word: w for word, w, _ in WORDS}
    replies = defaultdict(list)
    for root in roots:
        mapping = dict(line.split() for line in (root / "mapping.txt").read_text().splitlines())
        for row in csv.DictReader((root / "blind" / "yesno-full.csv").read_text().splitlines()):
            words = {w: p / m for w, (p, m) in reply_score(row, lines).items() if m}
            quality = sum(weight[w] * s for w, s in words.items()) / sum(weight[w] for w in words)
            flagged = any(row.get(line["id"]) == "Y" for line in lines if line["flag"])
            replies[mapping[row["label"]].rsplit("-", 1)[0]].append((quality, flagged, words))
    arms = [a for a in ("old", "new", "none") if a in replies] + sorted(set(replies) - {"old", "new", "none"})
    if not arms:
        return ""
    def mean(values):
        values = list(values)
        return sum(values) / len(values) if values else float("nan")
    cells = {}
    for arm in arms:
        rs = replies[arm]
        flagged = sum(f for _, f, _ in rs)
        quality = mean(q for q, _, _ in rs)
        cells[arm] = [f"{100 * quality * (1 - FLAG_CUT * flagged / len(rs)):.1f}", f"{100 * quality:.1f}",
                      f"{flagged}/{len(rs)}"]
        cells[arm] += [f"{100 * mean(w[word] for _, _, w in rs if word in w):.1f}" for word, _, _ in WORDS]
    names = ["**score**", "quality", "replies with a red flag"] + [f"{word} ({w})" for word, w, _ in WORDS]
    out = ["## Overall", "",
           f"score = quality x (1 - {FLAG_CUT} x the share of replies with a red flag). Quality weighs the words "
           "of PHILOSOPHY.md by rank; a line that does not apply counts for nothing.", "",
           "| | " + " | ".join(arms) + " |", "|---|" + "---|" * len(arms)]
    out += [f"| {name} | " + " | ".join(cells[a][k] for a in arms) + " |" for k, name in enumerate(names)]
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    print(summary(Path(sys.argv[1]) / sys.argv[2]))
