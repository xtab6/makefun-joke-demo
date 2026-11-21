#!/usr/bin/env python3
"""The joke about the demo.

Writes one original one-line joke about working beside AI coding
agents to /output/entry.txt. Stdlib only, no network, no randomness,
no clock: the same bytes on every run.
"""

import os
import sys

JOKE = (
    "My agent crashed the demo in front of the whole room, said "
    "'watch this', and fixed it by reverting to the code from "
    "before I asked it to help."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    code_points = len(JOKE)
    if not 1 <= code_points <= 280:
        print(f"joke is {code_points} code points, must be 1-280", file=sys.stderr)
        return 1
    if not JOKE.strip():
        print("joke is only whitespace", file=sys.stderr)
        return 1
    if "\n" in JOKE:
        print("joke must be one line", file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        print("verify-after-write failed: entry.txt differs", file=sys.stderr)
        return 1
    if len(written) != code_points:
        print("verify-after-write failed: length differs", file=sys.stderr)
        return 1

    print(f"wrote {OUTPUT_PATH} ({code_points} code points)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
