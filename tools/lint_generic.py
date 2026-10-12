#!/usr/bin/env python3
"""Fail when the package names one person's machine, tools or voice.

cosmoskill is a general package. This lint keeps machine paths and
single-user references out of what is shipped: the skills, the README, the
plugin manifests, the documents and the tools.

    python3 tools/lint_generic.py            # the repository
    python3 tools/lint_generic.py <path>...  # given files or directories

Patterns live in tools/lint-patterns.txt. Exit status 1 if anything matches.
Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATTERNS = Path(__file__).resolve().parent / "lint-patterns.txt"
DEFAULT_SCOPE = ["skills", "README.md", ".claude-plugin", "docs", "tools", "tests", ".github", "LICENSE"]
TEXT_SUFFIXES = {".md", ".tsv", ".py", ".json", ".yml", ".yaml", ".txt", ".sh", ""}
# Files that must be able to name the forbidden strings.
SELF = {
    "tools/lint-patterns.txt",
    "tools/lint_generic.py",
    # The plan of the generalising pass lists the patterns it removes.
    "docs/history/2026-10-12-phase1-generalise-plan.md",
}
SELF_PREFIXES = ("tests/fixtures/lint/",)
# Under this prefix the "name" class is allowed: it is the record of the
# single-user build. Machine paths stay forbidden there too.
HISTORY = "docs/history/"


def load_patterns() -> list[tuple[str, re.Pattern]]:
    patterns = []
    for line in PATTERNS.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        kind, expression = line.split("\t", 1)
        patterns.append((kind, re.compile(expression)))
    return patterns


def candidates(paths: list[Path]) -> list[Path]:
    found: list[Path] = []
    for path in paths:
        if path.is_dir():
            found += sorted(p for p in path.rglob("*") if p.is_file() and ".git" not in p.parts)
        elif path.is_file():
            found.append(path)
    return [p for p in found if p.suffix in TEXT_SUFFIXES and "__pycache__" not in p.parts]


def relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def lint(paths: list[Path], skip_fixtures: bool = True) -> list[str]:
    patterns = load_patterns()
    problems = []
    for path in candidates(paths):
        name = relative(path)
        if name in SELF or (skip_fixtures and name.startswith(SELF_PREFIXES)):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        in_history = name.startswith(HISTORY)
        for number, line in enumerate(lines, start=1):
            for kind, pattern in patterns:
                if kind == "name" and in_history:
                    continue
                match = pattern.search(line)
                if match:
                    problems.append(f"{name}:{number}: [{kind}] {match.group(0)!r}: {line.strip()[:110]}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--count", action="store_true", help="print one count per file instead of every line")
    args = parser.parse_args()

    # The lint's own fixtures hold the forbidden strings on purpose: they are
    # skipped in a repository run and checked when named explicitly.
    if args.paths:
        problems = lint(args.paths, skip_fixtures=False)
    else:
        problems = lint([ROOT / entry for entry in DEFAULT_SCOPE if (ROOT / entry).exists()])
    if args.count:
        per_file: dict[str, int] = {}
        for problem in problems:
            per_file[problem.split(":", 1)[0]] = per_file.get(problem.split(":", 1)[0], 0) + 1
        for name, count in sorted(per_file.items()):
            print(f"{count:4d}  {name}")
    else:
        for problem in problems:
            print(problem)
    print(f"{len(problems)} line(s) name a person's machine, tools or voice", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
