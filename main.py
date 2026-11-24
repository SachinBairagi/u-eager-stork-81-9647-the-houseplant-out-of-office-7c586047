#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Pure standard library, fully deterministic:
the same line on every run.
"""

import os

ENTRY = (
    "Out of office. I haven't been watered since March and honestly, "
    "I've never been happier. Complain to the fern."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
