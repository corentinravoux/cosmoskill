#!/usr/bin/env python3
"""Fingerprint the numbers of Markdown and TSV files.

A restructuring pass must not change a number. This script prints, for each
file given (or found under the directories given), a hash of the sorted list
of its numeric tokens, with their multiplicity, and the count. Two runs
compared line by line show which files gained or lost a number.

    python3 tools/numeric_fingerprint.py skills > before.txt
    python3 tools/numeric_fingerprint.py --diff before.txt skills
    python3 tools/numeric_fingerprint.py --tokens skills/cosmo-cmb/SKILL.md

Standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

NUMBER = re.compile(r"\d[\d.,]*\d|\d")
SUFFIXES = {".md", ".tsv"}


def tokens(path: Path) -> Counter:
    return Counter(NUMBER.findall(path.read_text(encoding="utf-8")))


def files(roots: list[Path]) -> list[Path]:
    found: list[Path] = []
    for root in roots:
        if root.is_dir():
            found += sorted(p for p in root.rglob("*") if p.is_file() and p.suffix in SUFFIXES)
        elif root.is_file():
            found.append(root)
    return found


def fingerprint(path: Path) -> tuple[str, int]:
    counted = tokens(path)
    body = "\n".join(f"{token}\t{count}" for token, count in sorted(counted.items()))
    return hashlib.sha256(body.encode()).hexdigest()[:16], sum(counted.values())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--diff", type=Path, help="earlier output to compare with; exit 1 if any file differs")
    parser.add_argument("--tokens", action="store_true", help="print the tokens of each file instead of a hash")
    args = parser.parse_args()

    if args.tokens:
        for path in files(args.paths):
            for token, count in sorted(tokens(path).items()):
                print(f"{path}\t{token}\t{count}")
        return 0

    current = {str(path): fingerprint(path) for path in files(args.paths)}
    if not args.diff:
        for name, (digest, count) in current.items():
            print(f"{name}\t{digest}\t{count}")
        return 0

    earlier = {}
    for line in args.diff.read_text(encoding="utf-8").splitlines():
        name, digest, count = line.split("\t")
        earlier[name] = (digest, int(count))
    changed = 0
    for name in sorted(set(earlier) | set(current)):
        before, after = earlier.get(name), current.get(name)
        if before == after:
            continue
        changed += 1
        if before is None:
            print(f"new      {name}\t{after[1]} numbers")
        elif after is None:
            print(f"gone     {name}\t{before[1]} numbers")
        else:
            print(f"changed  {name}\t{before[1]} -> {after[1]} numbers")
    print(f"{changed} file(s) differ")
    return 1 if changed else 0


if __name__ == "__main__":
    sys.exit(main())
