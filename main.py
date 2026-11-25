"""One-line entry for the 3am fridge text bounty.

A smart fridge with a small voice and no shame sends its owner a
single lock-screen line in the middle of the night. This program
writes that line to /output/entry.txt: exactly one line, UTF-8.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The fridge has been keeping count of the night visits,
# and it has quietly formed an opinion about the cake.
ENTRY = (
    "3:04 AM. Seventh visit tonight. I've stopped chilling the cake "
    "— we both know how this ends."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= 140, "entry must fit the 140 char gate"
    folder = os.path.dirname(OUTPUT_PATH)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
