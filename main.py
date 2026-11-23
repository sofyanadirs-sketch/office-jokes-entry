#!/usr/bin/env python3
"""One-line entry: an office joke about HR's 'anonymous' feedback form.

Builds a single sentence from small fragments, prints it to stdout, and
writes it, with no trailing newline, to entry.txt inside the output
directory. The sentence has exactly one terminal period, so the output
stays exactly one sentence. The joke itself is 149 characters: HR's
"anonymous" form demands three identifiers, so the narrator answers with
top marks and signs the only name the form deserves.
"""

import os
from pathlib import Path


def build_line() -> str:
    setup = "HR's 'anonymous' feedback form asked for my employee ID,"
    detail = " department, and desk number, so I gave all 47 questions"
    payoff = " top marks and signed it 'Anonymous'."
    return setup + detail + payoff


def main() -> None:
    line = build_line()
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
