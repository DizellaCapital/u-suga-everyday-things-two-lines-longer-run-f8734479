"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes two lines explaining a traffic jam to a 10-year-old to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output). Stdlib only.

Line 1 (one vivid sentence, one analogy): at 5:40 on the toll road,
Dad's car is a blob of toothpaste stuck inside the tube while a hundred
other blobs press in behind it, none of them able to squeeze out.
Line 2 (one sentence, honest about the limits): the tube fits because
the cars really are packed bumper to bumper with nowhere to go, but it
leaves out the honking, the lane-changing, and the fact that toothpaste
never finds a side road to escape.
"""

import os

LINE_ONE = (
    "At 5:40 on the toll road, Dad's car is a blob of toothpaste stuck "
    "inside the tube while a hundred other blobs press in behind it, "
    "none of them able to squeeze out."
)

LINE_TWO = (
    "The tube fits because the cars really are packed bumper to bumper "
    "with nowhere to go, but it leaves out the honking, the "
    "lane-changing, and the fact that toothpaste never finds a side "
    "road to escape."
)

MAX_CHARS = 400


def entry_text():
    """The two lines joined by a single newline, no trailing newline."""
    return LINE_ONE + "\n" + LINE_TWO


def problem_with(text):
    """Return a human-readable problem with the entry, or None if fine."""
    if not text or not text.strip():
        return "entry is empty or only whitespace"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the %d limit" % (
            len(text),
            MAX_CHARS,
        )
    lines = text.split("\n")
    if len(lines) != 2:
        return "entry must be exactly two lines, found %d" % len(lines)
    # Each line is one sentence: exactly one full stop, at the very end.
    for index, line in enumerate(lines, start=1):
        if not line.strip():
            return "line %d is empty" % index
        if line != line.strip():
            return "line %d has leading or trailing whitespace" % index
        if line.count(".") != 1 or not line.endswith("."):
            return "line %d must be exactly one sentence" % index
    return None


def run():
    text = entry_text()
    problem = problem_with(text)
    if problem:
        print("invalid entry: " + problem)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(target, encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            print("read-back did not match the entry")
            return 1
    print("wrote %d characters to %s" % (len(text), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
