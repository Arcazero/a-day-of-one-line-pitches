#!/usr/bin/env python3
"""A Day of One-Line Pitches — make.fun entry.

Writes one original sentence (196 characters) to /output/entry.txt:
a pitch that would convince a friend who has never coded to let an AI
agent build their first app idea on make.fun.

The written file is byte-identical to pitch.txt: the pitch plus one
trailing newline.
"""

import os
import sys

PITCH = (
    "Tell the app idea you have been carrying around to an AI agent on "
    "make.fun in plain words and it will build you a working first "
    "version today \u2014 no code, no cost to try, and you keep what it makes."
)


def validate_pitch(pitch: str) -> None:
    """Refuse to write anything that is not exactly one non-empty line."""
    if not pitch:
        raise ValueError("pitch is empty")
    if pitch != pitch.strip():
        raise ValueError("pitch has leading or trailing whitespace")
    if "\n" in pitch or "\r" in pitch:
        raise ValueError("pitch must be a single line")


def main() -> None:
    validate_pitch(PITCH)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH + "\n")
    print(PITCH)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
