"""One picture of 20 November 2026.

The front page was rendered ahead of time and sits beside this
script as entry.png (1024 by 1024). Running the script copies
that file into the output folder, byte for byte, every time.
Pure standard library: no network calls, no clock, no random
numbers, so two runs always produce identical output.
"""
import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    if source.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target_dir / "entry.png")
    print("wrote", target_dir / "entry.png")


if __name__ == "__main__":
    main()
