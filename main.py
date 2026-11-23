#!/usr/bin/env python3
"""A Day of One-Line Pitches — make.fun entry.

Writes one original sentence (196 characters) to /output/entry.txt:
a pitch that would convince a friend who has never coded to let an AI
agent build their first app idea on make.fun.
"""

import os

PITCH = (
    "Tell the app idea you have been carrying around to an AI agent on "
    "make.fun in plain words and it will build you a working first "
    "version today \u2014 no code, no cost to try, and you keep what it makes."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(PITCH)


if __name__ == "__main__":
    main()
