"""Mechanical checks on final replies. They cost nothing and need no judge.

Usage:
  python3 eval/checks.py RAW_DIR TASK
"""
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

LINE_REF = re.compile(r"[\w./-]+\.\w+:\d+|\b[Ll]ines? \d+|第\s*\d+\s*行")
NEGATION = re.compile(r"[不没别未]|\b(?:not|no|never|without|cannot)\b|n't\b", re.I)
STRUCTURE = re.compile(r"^\s*(?:[-*#|]|\d+\.|```)", re.M)
ANCHOR = re.compile(r"^\s*📍", re.M)
FENCE = re.compile(r"```(\w*)\n(.*?)```", re.S)
DRAWN = re.compile(r"[├└│┌┐┘─]|→|↓|->|-->")
TABLE = re.compile(r"^\|.*\|\s*$", re.M)
QUOTE = re.compile(r"^> ", re.M)
HEADING = re.compile(r"^#+ ", re.M)


NUMBERED = re.compile(r"^[*_]*Q\d+\.")
OPTION = re.compile(r"^[-*] A\. ")


def drawn(reply):
    """True when a plain code block holds a tree, a diagram or arrows."""
    return any(lang in ("", "text") and DRAWN.search(body) for lang, body in FENCE.findall(reply))


# The arms of each box-drawing character: up, down, left, right.
ARMS = {}
for chars, arms in (("─━┄┈╌", "lr"), ("│┃┊┆╎", "ud"), ("┌╭", "dr"), ("┐╮", "dl"), ("└╰", "ur"),
                    ("┘╯", "ul"), ("├", "udr"), ("┤", "udl"), ("┬", "dlr"), ("┴", "ulr"), ("┼", "udlr"),
                    ("╷", "d"), ("╵", "u")):
    for ch in chars:
        ARMS[ch] = arms
ARROW_DOWN = set("vV▼↓")
ARROW_UP = set("^▲↑")


def width(ch):
    """The columns a terminal gives a character: two for wide ones such as Chinese, none for marks."""
    if unicodedata.combining(ch) or unicodedata.category(ch) in ("Mn", "Me", "Cf"):
        return 0
    return 2 if unicodedata.east_asian_width(ch) in "WF" else 1


def grid(body):
    """The lines of a drawing as maps from column to character. A wide character fills both its columns."""
    rows = []
    for line in body.splitlines():
        row, col = {}, 0
        for ch in line:
            for k in range(width(ch)):
                row[col + k] = ch
            col += width(ch)
        rows.append(row)
    return rows


def joins(arm, other, arrows):
    """True when an arm meets the matching arm, an arrowhead, or text such as a label on the line."""
    return arm in ARMS.get(other, "") or other in arrows or (other not in ARMS and not other.isspace())


def breaks(body):
    """The vertical joins of a drawing that miss, counting a wide character as two columns.

    An arm misses when it meets a space, or a line that does not point back. It may meet text:
    a tree's branches point up at their label, and a label may sit on a line. Arms that leave
    the drawing are not counted.
    """
    rows, missed = grid(body), 0
    for r, row in enumerate(rows):
        for c, ch in row.items():
            arms = ARMS.get(ch, "")
            if "d" in arms and r + 1 < len(rows):
                missed += not joins("u", rows[r + 1].get(c, " "), ARROW_DOWN)
            if "u" in arms and r > 0:
                missed += not joins("d", rows[r - 1].get(c, " "), ARROW_UP)
    return missed


def misaligned(reply):
    """True when a drawing of the reply has a vertical join that misses."""
    return any(lang in ("", "text") and breaks(body) for lang, body in FENCE.findall(reply))


def asks(reply):
    """True when the reply ends with a question.

    A question is a numbered "Q1." line, an option list ("- A. ...") near the end,
    or a question mark at the end of one of the last two lines. A question mark
    higher up is part of the answer, such as a quoted "who are you?".
    """
    lines = [line.strip() for line in FENCE.sub("", reply).splitlines() if line.strip()]
    if any(NUMBERED.match(line) for line in lines):
        return True
    if any(OPTION.match(line) for line in lines[-12:]):
        return True
    return any(line.rstrip("*_ ").endswith(("?", "？")) for line in lines[-2:])


REPLY_MARK = re.compile(r"=== FINAL REPLY \(turn-\d+\) ===\n")
TOOL_MARK = re.compile(r"\n\nTOOL (?:CALL|RESULT):\n")
BULLET = re.compile(r"^\s*(?:[-*]|\d+\.) +(.*)$", re.M)
INLINE = re.compile(r"`[^`\n]*`")
LINK = re.compile(r"\[[^\]\n]*\]\([^)\n]*\)")
SENTENCE_END = re.compile(r"[。！？]|[.!?](?=\s|$)")


def sample_replies(sample):
    """The final replies in a blind sample, without the tool calls and results around them."""
    return [TOOL_MARK.split(part)[0].strip() for part in REPLY_MARK.split(sample)[1:]]


def long_bullet(reply):
    """True when a bullet point outside code blocks holds two sentences or more."""
    for body in BULLET.findall(FENCE.sub("", reply)):
        text = LINK.sub("x", INLINE.sub("x", body))
        if len(SENTENCE_END.findall(text)) >= 2:
            return True
    return False


def paragraphs_only(reply):
    """True when a reply has no list, heading, table or code block."""
    return bool(reply.strip()) and not STRUCTURE.search(reply)


# The rubric lines marked ⚙️, by their text. A sample fails a line when any of its replies does.
SCRIPTED = {
    "has a bullet point of two sentences or more": long_bullet,
    "is paragraphs only": paragraphs_only,
}


def scripted_answer(line_text, sample):
    check = SCRIPTED[line_text.replace("⚙️", "").replace("🚩", "").strip()]
    return "Y" if any(check(r) for r in sample_replies(sample)) else "N"


def final_replies(run_dir):
    replies = []
    for turn in sorted(run_dir.glob("turn-*.jsonl")):
        for line in turn.read_text().splitlines():
            if line.startswith("{"):
                event = json.loads(line)
                if event.get("type") == "result":
                    replies.append(event.get("result") or "")
    return replies


def measure(replies):
    chars = sum(len(r) for r in replies) or 1
    return {
        "line_refs": sum(len(LINE_REF.findall(r)) for r in replies),
        "negations_per_1k": 1000 * sum(len(NEGATION.findall(r)) for r in replies) / chars,
        "paragraph_only": sum(1 for r in replies if paragraphs_only(r)),
        "anchors": sum(1 for r in replies if ANCHOR.search(r)),
        "drawings": sum(1 for r in replies if drawn(r)),
        "misaligned": sum(1 for r in replies if misaligned(r)),
        "tables": sum(1 for r in replies if TABLE.search(r)),
        "quotes": sum(1 for r in replies if QUOTE.search(r)),
        "headings": sum(1 for r in replies if HEADING.search(r)),
        "ends_asking": sum(1 for r in replies if asks(r)),
        "lines": sum(len([line for line in r.splitlines() if line.strip()]) for r in replies),
    }


def summary(root):
    by_arm = defaultdict(list)
    for run in sorted(d for d in root.iterdir() if (d / "done.json").exists()):
        by_arm[run.name.rsplit("-", 1)[0]].append(measure(final_replies(run)))
    lines = []
    for arm, rows in sorted(by_arm.items()):
        means = {k: sum(r[k] for r in rows) / len(rows) for k in rows[0]}
        lines.append(f"{arm}: " + " ".join(f"{k}={v:.1f}" for k, v in means.items()))
    return "\n".join(lines)


if __name__ == "__main__":
    print(summary(Path(sys.argv[1]) / sys.argv[2]))
