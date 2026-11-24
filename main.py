"""Two-Sentence Horror — make.fun entry (program/v1).

Writes one horror story of exactly two sentences to /output/entry.txt.

The story is a fixed, hard-coded text: the program is fully deterministic,
reads nothing from the environment, the network, or the filesystem, and
writes byte-identical output on every run. Before writing, it checks the
entry against the competition gate itself (UTF-8 text, 1 to 400 characters,
not only whitespace, exactly two sentences) and refuses to write anything
that would fail it.
"""

import os

STORY = (
    "My son drew our family on the fridge again: four smiling stick figures, holding hands. "
    "I counted them twice before I realised there are only three of us \u2014 and the fourth one is holding my hand."
)


def check_gate(text: str) -> None:
    """Fail loudly if the story would fail the competition gate."""
    if not (1 <= len(text) <= 400):
        raise SystemExit(f"gate: {len(text)} characters, need 1-400")
    if not text.strip():
        raise SystemExit("gate: entry is only whitespace")
    if text.count(".") != 2:
        raise SystemExit("gate: entry must be exactly two sentences")


def main() -> None:
    check_gate(STORY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
