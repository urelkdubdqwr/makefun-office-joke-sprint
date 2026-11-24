"""Write the office-joke entry to entry.txt in the make.fun output directory.

The output directory is $MAKEFUN_OUTPUT_DIR when set and non-empty, otherwise
/output. The file content is a single fixed line plus one trailing newline.
"""

import os
import sys

TEXT = "The 'reply all' was a mistake; the four follow-up 'reply all's agreeing it was a mistake were a lifestyle.\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        sys.exit(f"cannot create output directory {out_dir!r}: {exc}")
    try:
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(TEXT)
    except OSError as exc:
        sys.exit(f"cannot write entry.txt in {out_dir!r}: {exc}")


if __name__ == "__main__":
    main()
