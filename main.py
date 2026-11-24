#!/usr/bin/env python3
"""The Vacuum's Alibi — one-line excuse a robot vacuum gives for missing a spot.

Writes a single deterministic line of text to /output/entry.txt by default,
or to the path given by the OUTPUT_PATH environment variable when set.
Stdlib only, no randomness, no network.
"""

import os
import sys

# The entry: deadpan robot-voice log line. One line, well under the 200-char gate.
LINE = (
    "Log 04:12: I did not miss that spot. My sensors classified the dust "
    "bunny as a protected species, and my warranty does not cover extinction."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> int:
    output_path = os.environ.get("OUTPUT_PATH") or DEFAULT_OUTPUT
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
