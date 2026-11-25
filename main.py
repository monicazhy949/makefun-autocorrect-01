"""makefun-autocorrect-01: Funniest Autocorrect Fail.

Writes a single-line autocorrect fail to /output/entry.txt.
"""

import os

ENTRY = (
    "Grandma, thank you for the birthday money! I used it to buy a lovely "
    "new vibrator \u2014 I mean, a lovely new SWEATER. A sweater, Grandma. "
    "Please stop crying."
)


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
