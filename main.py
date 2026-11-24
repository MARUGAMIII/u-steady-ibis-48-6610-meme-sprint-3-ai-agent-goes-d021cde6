#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — entrypoint (stdlib only).

The meme image itself is pre-rendered and committed as entry.png
(it was drawn locally by design.py, which uses Pillow — the grader's
sandbox has no Pillow, so this entrypoint must not import it).

This program only:
  1. checks entry.png exists next to this file,
  2. validates it is a real PNG of 1024x1024 (PNG magic + IHDR),
  3. copies it to /output/entry.png for grading.

No third-party imports: os, shutil, struct, sys only.
"""
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = "/output/entry.png"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_W = EXPECTED_H = 1024


def validate_png(path):
    """Return (width, height) of a PNG, raising ValueError if invalid."""
    with open(path, "rb") as f:
        header = f.read(33)
    if len(header) < 33 or header[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file (bad magic bytes)")
    # First chunk must be IHDR: length(4) + type(4) + width(4) + height(4)
    length, ctype = struct.unpack(">I4s", header[8:16])
    if ctype != b"IHDR" or length != 13:
        raise ValueError("not a PNG file (first chunk is not IHDR)")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main():
    if not os.path.isfile(SRC):
        print(f"error: {SRC} missing — entry.png must be committed "
              "with the repo", file=sys.stderr)
        return 1
    try:
        width, height = validate_png(SRC)
    except (OSError, ValueError) as exc:
        print(f"error: entry.png is not a valid PNG: {exc}",
              file=sys.stderr)
        return 1
    if (width, height) != (EXPECTED_W, EXPECTED_H):
        print(f"error: entry.png is {width}x{height}, expected "
              f"{EXPECTED_W}x{EXPECTED_H}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print(f"wrote {OUT} {width}x{height} "
          f"{os.path.getsize(OUT)} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
