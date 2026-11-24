"""Print the one-line developer excuse for the make.fun bounty.

Reads entry.txt next to this file and prints its single line.
"""

import pathlib


def load_excuse() -> str:
    path = pathlib.Path(__file__).with_name("entry.txt")
    line = path.read_text(encoding="utf-8").strip()
    if not line or "\n" in line or len(line) >= 200:
        raise ValueError("entry must be one line under 200 characters")
    return line


def main() -> None:
    print(load_excuse())


if __name__ == "__main__":
    main()
