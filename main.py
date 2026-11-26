#!/usr/bin/env python3
"""Write one funny line: a home Wi-Fi router excusing itself for
dropping the connection at the exact climax of a movie.

Stdlib only. Writes a single line to /output/entry.txt.
"""

import os

LINE = (
    "Six years of 4K and not one thank-you, so when the killer "
    "finally turned around, I took my break too."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
