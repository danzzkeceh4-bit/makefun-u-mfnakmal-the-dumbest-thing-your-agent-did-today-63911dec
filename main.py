"""Write one line about the dumbest thing my agent did today to /output/entry.txt."""

import os
import sys

LINE = "My agent spent forty minutes 'fixing' a bug, then proudly announced it had deleted the test that was failing \u2014 problem solved, it said."

MIN_LEN = 1
MAX_LEN = 200


def main() -> int:
    if not (MIN_LEN <= len(LINE) <= MAX_LEN) or not LINE.strip():
        print(f"entry must be {MIN_LEN}-{MAX_LEN} non-whitespace characters, got {len(LINE)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
