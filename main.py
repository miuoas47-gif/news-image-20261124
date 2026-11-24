#!/usr/bin/env python3
"""24 November 2026 in One Image — entrypoint.

Copies the entry image (entry.png, held at the repository root) to
$MAKEFUN_OUTPUT_DIR/entry.png. Takes no arguments, uses no network, and
is deterministic: a copy is byte-identical on every run.
"""

import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)
    # Verify the copy is byte-identical to the source image.
    with open(SRC, "rb") as f:
        source_bytes = f.read()
    with open(dest, "rb") as f:
        copied_bytes = f.read()
    assert copied_bytes == source_bytes, "entry.png copy differs from source"
    print(f"wrote {dest} ({len(copied_bytes)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
