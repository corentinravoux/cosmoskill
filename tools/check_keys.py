#!/usr/bin/env python3
"""Check the section keys of the skills.

Fails when a `##` or `###` heading has no key, when a key is malformed or
repeated in its file, and, with `--against <git ref>`, when a key that
existed at that ref is gone without an entry in the skill's
`references/retired-keys.tsv`.

    python3 tools/check_keys.py
    python3 tools/check_keys.py --against v0.3.0

`retired-keys.tsv` has one header line and the columns
`file`, `key`, `retired_on`, `replaced_by`, `reason`; `replaced_by` is
`<file-stem>#<key>` or empty.

Standard library only. Exit status 1 if anything is wrong.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assign_keys import ROOT, headings, skill_files  # noqa: E402

RETIRED_COLUMNS = ["file", "key", "retired_on", "replaced_by", "reason"]


def keys_of(text: str) -> tuple[list[str], list[str]]:
    """Return (keys in order, headings without a key)."""
    keys, unkeyed = [], []
    for _, heading, key in headings(text.split("\n")):
        if key:
            keys.append(key)
        else:
            unkeyed.append(heading)
    return keys, unkeyed


def check_tree(root: Path = ROOT) -> list[str]:
    problems = []
    for path in skill_files(root):
        name = path.relative_to(root).as_posix()
        keys, unkeyed = keys_of(path.read_text(encoding="utf-8"))
        for heading in unkeyed:
            problems.append(f"{name}: heading without a key: {heading[:60]}")
        seen = set()
        for key in keys:
            if key in seen:
                problems.append(f"{name}: key repeated: {key}")
            seen.add(key)
    return problems


def retired(root: Path, skill: str) -> set[tuple[str, str]]:
    path = root / "skills" / skill / "references" / "retired-keys.tsv"
    if not path.is_file():
        return set()
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].split("\t") != RETIRED_COLUMNS:
        raise SystemExit(f"{path}: header must be {RETIRED_COLUMNS}")
    return {(fields[0], fields[1]) for fields in (line.split("\t") for line in lines[1:]) if len(fields) >= 2}


def check_against(ref: str, root: Path = ROOT) -> list[str]:
    listing = subprocess.run(["git", "-C", str(root), "ls-tree", "-r", "--name-only", ref, "skills"],
                             capture_output=True, text=True)
    if listing.returncode != 0:
        raise SystemExit(f"git cannot read {ref!r}: {listing.stderr.strip()}")
    problems = []
    for name in listing.stdout.splitlines():
        parts = name.split("/")
        if not name.endswith(".md") or len(parts) < 3:
            continue
        skill, stem = parts[1], Path(name).stem
        old_text = subprocess.run(["git", "-C", str(root), "show", f"{ref}:{name}"], capture_output=True, text=True).stdout
        old_keys, _ = keys_of(old_text)
        if not old_keys:
            continue
        current = root / name
        new_keys = set(keys_of(current.read_text(encoding="utf-8"))[0]) if current.is_file() else set()
        gone = retired(root, skill)
        for key in old_keys:
            if key not in new_keys and (stem, key) not in gone:
                problems.append(f"{name}: key {key} existed at {ref} and is gone; restore it or list it in references/retired-keys.tsv")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--against", metavar="REF", help="git ref whose keys must all survive")
    args = parser.parse_args()
    problems = check_tree()
    if args.against:
        problems += check_against(args.against)
    for problem in problems:
        print(problem)
    print(f"{len(problems)} key problem(s)", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
