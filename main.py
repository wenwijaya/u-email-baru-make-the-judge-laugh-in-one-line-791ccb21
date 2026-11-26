#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — writes one funny line to /output/entry.txt."""

import os

LINE = "I asked my GPS for the meaning of life; it said 'recalculating' \u2014 and honestly, that's the most honest answer I've ever gotten."


def main() -> int:
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        try:
            with open("entry.txt", "w", encoding="utf-8") as f:
                f.write(LINE + "\n")
        except OSError:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
