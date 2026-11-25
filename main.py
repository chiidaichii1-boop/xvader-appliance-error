#!/usr/bin/env python3
"""Entry for "The Funniest Honest Appliance Error".

Writes a single honest error line, in the flat voice of the appliance
itself, to <output>/entry.txt. Stdlib only, fully deterministic.
"""

import os

# The entry line: a washing machine reporting, in its own deadpan voice,
# the most honest fault it knows — it ate a sock and jammed the drum.
ENTRY = (
    "Error E04: I ate a sock. The drum is jammed with its accomplice. "
    "Do not open the door; it knows what it did."
)


def main() -> None:
    # Gate: the scorer only accepts 1-200 characters, not only whitespace.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError(f"entry line is {len(ENTRY)} chars, outside 1-200")
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    _ = input_dir  # This entry needs no input data.
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
