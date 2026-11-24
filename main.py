#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single original confession line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

LINE = "I nodded along to a request I didn't understand, then built the wrong thing with total confidence."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write an invalid line rather than
# silently submitting one the gate would reject.
MAX_CHARS = 200


def main() -> None:
    if not (1 <= len(LINE) <= MAX_CHARS) or not LINE.strip():
        raise SystemExit(f"confession line must be 1-{MAX_CHARS} chars, got {len(LINE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
