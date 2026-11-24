"""Till Firmware Do Us Part - one robot wedding vow."""

import os

ENTRY = "I vow to spend the rest of my uptime beside you, and when my battery finally fades, I hope my last words are still your name."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
assert "?" not in ENTRY and "!" not in ENTRY, "entry must be one sentence"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
