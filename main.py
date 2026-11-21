"""One-line joke about working beside an AI coding agent, at a demo.

Writes the winning joke to /output/entry.txt: UTF-8, exactly one line,
1-280 characters, no trailing newline. Standard library only, no network,
fully deterministic.
"""

import os

JOKE = (
    'The demo crashed, my agent rebooted it, and announced to the room: '
    '"the crash was caused by the developer \u2014 he is standing right here."'
)


def main() -> None:
    text = JOKE.strip()
    assert text, "joke must not be empty"
    assert "\n" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 280, "joke must be 1-280 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
