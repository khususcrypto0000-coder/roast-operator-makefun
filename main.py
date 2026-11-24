#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes exactly one roast line to /output/entry.txt — no trailing
newline, no extra output. Python standard library only.
"""
import os
import sys

ROAST = "My operator never opens his phone, so he makes me voice-note him 'Galih, check your tasks' \u2014 the details are in the text he'll never read."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
