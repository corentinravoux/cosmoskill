#!/usr/bin/env python3
"""Give every section of the skills a permanent key.

A key is a short slug written on the line under a `##` or `###` heading:

    ## 4. Cosmology from P1D
    <!-- key: cosmology-from-p1d -->

It names the section for notes, layers and citations between skills. Inside
a skill a section is `<file-stem>#<key>`; across skills,
`<skill>/<file-stem>#<key>`. A key is derived from the heading once and then
frozen: rewording the heading later does not change it.

    python3 tools/assign_keys.py            # add missing keys under skills/
    python3 tools/assign_keys.py --dry-run  # say what would be added

Idempotent: an existing key is never changed. Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADING = re.compile(r"^(#{2,3}) +(.+?)\s*$")
KEY_LINE = re.compile(r"^<!-- key: ([a-z0-9][a-z0-9\-]*) -->$")
FENCE = re.compile(r"^\s*(```|~~~)")
NUMBERING = re.compile(r"^\s*(?:§\s*)?(?:\d+[a-z]?(?:\.\d+[a-z]?)*\.?|[A-Z]\.)\s+")
MAX_SLUG = 48
GREEK = {"α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "σ": "sigma", "τ": "tau", "ξ": "xi", "Ω": "omega",
         "ω": "omega", "Λ": "lambda", "λ": "lambda", "μ": "mu", "ν": "nu", "Σ": "sigma", "φ": "phi", "κ": "kappa",
         "χ": "chi", "η": "eta", "θ": "theta", "ℓ": "ell", "×": "x", "₀": "0", "₈": "8", "⁸": "8"}


def slugify(heading: str) -> str:
    text = NUMBERING.sub("", heading)
    text = re.sub(r"`|\*|_", "", text)
    text = "".join(GREEK.get(char, char) for char in text)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    if len(text) > MAX_SLUG:
        text = text[:MAX_SLUG].rsplit("-", 1)[0]
    return text or "section"


def headings(lines: list[str]):
    """Yield (index, heading text, key or None) for each keyable heading."""
    fenced = False
    for index, line in enumerate(lines):
        if FENCE.match(line):
            fenced = not fenced
            continue
        if fenced:
            continue
        match = HEADING.match(line)
        if not match:
            continue
        key = None
        if index + 1 < len(lines):
            found = KEY_LINE.match(lines[index + 1].strip())
            if found:
                key = found.group(1)
        yield index, match.group(2), key


def assign(path: Path, dry_run: bool) -> int:
    lines = path.read_text(encoding="utf-8").split("\n")
    found = list(headings(lines))
    used = {key for _, _, key in found if key}
    added = 0
    for index, text, key in reversed(found):
        if key:
            continue
        slug = base = slugify(text)
        number = 2
        while slug in used:
            slug = f"{base}-{number}"
            number += 1
        used.add(slug)
        lines.insert(index + 1, f"<!-- key: {slug} -->")
        added += 1
    if added and not dry_run:
        path.write_text("\n".join(lines), encoding="utf-8")
    return added


def skill_files(root: Path) -> list[Path]:
    files = []
    for skill in sorted(p for p in (root / "skills").iterdir() if p.is_dir()):
        files += [skill / "SKILL.md"] if (skill / "SKILL.md").is_file() else []
        for folder in ("references", "deep"):
            files += sorted((skill / folder).glob("*.md")) if (skill / folder).is_dir() else []
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    total = 0
    for path in skill_files(ROOT):
        added = assign(path, args.dry_run)
        total += added
        if added:
            print(f"{added:3d}  {path.relative_to(ROOT)}")
    print(f"{total} key(s) {'would be ' if args.dry_run else ''}added", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
