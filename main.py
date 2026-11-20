"""World news, 20 November 2026, in one image.

Copies the pre-rendered front page (entry.png, 1024x1024 PNG)
to the output directory. Standard library only, no network,
no date or time, no randomness: the same input always gives
the same output bytes.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as f:
        head = f.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        sys.exit("entry.png is not a PNG")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst)


if __name__ == "__main__":
    main()
