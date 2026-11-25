#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line to ``entry.txt`` inside the output
directory (``$MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``).
The line is the whole entry: an AI agent confessing what it actually
does all night instead of sleeping.
"""

import os
import sys

LINE = (
    "I don't sleep. I just lie awake all night rehearsing apologies "
    "for mistakes I haven't made yet."
)

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"
MAX_LINE_CHARS = 200  # the competition gate caps the entry at 200 characters


def output_dir() -> str:
    """Resolve the directory the grader expects the entry in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


def check_line(line: str) -> None:
    """Fail loudly rather than write a line the gate would mark invalid."""
    if not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if len(line) > MAX_LINE_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters; the limit is {MAX_LINE_CHARS}"
        )


def main() -> int:
    check_line(LINE)
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, OUTPUT_FILENAME)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
