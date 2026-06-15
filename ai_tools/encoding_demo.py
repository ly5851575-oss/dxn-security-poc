#!/usr/bin/env python3
"""Safe Base64 encode/decode utility for text data."""

from __future__ import annotations

import argparse
import base64
import binascii
import sys


def encode_text(text: str) -> str:
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


def decode_text(value: str) -> str:
    raw = base64.b64decode(value, validate=True)
    return raw.decode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Encode or decode UTF-8 text using Base64."
    )
    parser.add_argument("mode", choices=("encode", "decode"))
    parser.add_argument("text", help="Text or Base64 value")
    args = parser.parse_args()

    try:
        if args.mode == "encode":
            print(encode_text(args.text))
        else:
            print(decode_text(args.text))
    except (binascii.Error, UnicodeDecodeError) as exc:
        print(f"[ERROR] Invalid Base64/UTF-8 input: {exc}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
