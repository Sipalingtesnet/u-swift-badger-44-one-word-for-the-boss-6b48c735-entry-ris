#!/usr/bin/env python3
"""Write the entry word for "One Word for the Boss".

The judge reads /output/entry.txt exactly as submitted, so this program writes
one word and stops: no newline, no caption, no reasoning, nothing the judge
could mistake for an explanation.

WORD is a literal on purpose. The output must be deterministic and byte for
byte identical on every run, so nothing here is computed, sampled or fetched.
"""

import os

WORD = "Weathervane"

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    # newline="" keeps the platform from translating anything; write() adds
    # no terminator, so the file ends on the final "e".
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
