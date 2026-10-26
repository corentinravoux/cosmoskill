#!/usr/bin/env python3
"""Show what a refresh of the skills has to cover.

The skills are as current as their snapshot dates, and a `[doc]` fact goes
stale two years after its read date (owner, 2026-10-26; see
`tools/check_numbers.py`). This tool reads both and prints, per skill:

    the oldest and newest `Snapshot:` date of its reference files and
    dossiers, with their age in days;
    the number of `[doc]` facts, the oldest read date, and how many go stale
    within the horizon.

    python3 tools/refresh_status.py                  # one line per skill
    python3 tools/refresh_status.py --due 90         # what a refresh run should cover now
    python3 tools/refresh_status.py --skill cosmo-cmb --due 90

With `--due <days>`, it lists every file whose snapshot is older than that
many days, and every `[doc]` statement that goes stale within that many
days, so a refresh run knows where to start. The refresh procedure itself is
in `skills/observational-cosmology/references/suite-conventions.md`,
"Refreshing a domain". Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_numbers  # noqa: E402

ROOT = check_numbers.ROOT
SNAPSHOT = re.compile(r"\bSnapshot:\s*\**\s*(20\d\d-[01]\d-[0-3]\d)", re.I)


def snapshot(path: Path) -> date | None:
    """The first `Snapshot:` date in the first 20 lines of a file."""
    head = "\n".join(path.read_text(encoding="utf-8").split("\n")[:20])
    match = SNAPSHOT.search(head)
    return date.fromisoformat(match.group(1)) if match else None


def files_with_snapshot(skill: Path) -> list[tuple[Path, date]]:
    found = []
    for part in ("references", "deep"):
        for path in sorted((skill / part).glob("*.md")) if (skill / part).is_dir() else []:
            if path.name.startswith("_"):
                continue
            when = snapshot(path)
            if when:
                found.append((path, when))
    return found


def doc_records(skill: Path) -> list[dict]:
    return [record for record in check_numbers.scan(skill) if record["read"]]


def status(skill: Path, today: date, due: int | None) -> tuple[str, list[str]]:
    files, docs = files_with_snapshot(skill), doc_records(skill)
    horizon = today + timedelta(days=due) if due is not None else None
    stale_soon = [record for record in docs if horizon and
                  date.fromisoformat(record["read"]) < check_numbers.stale_limit(horizon)]
    if files:
        oldest, newest = min(when for _, when in files), max(when for _, when in files)
        snap = f"snapshots {oldest} to {newest} (oldest {(today - oldest).days} days)"
    else:
        snap = "no snapshot dates"
    read = f", oldest read {min(record['read'] for record in docs)}" if docs else ""
    line = f"{skill.name:40} {snap}; {len(docs):3} [doc]{read}"
    if due is not None:
        line += f"; {len(stale_soon)} stale within {due} days"
    details = []
    if due is not None:
        for path, when in files:
            if (today - when).days > due:
                details.append(f"  snapshot {when} ({(today - when).days} days): {path.relative_to(ROOT)}")
        for record in stale_soon:
            details.append(f"  [doc] read {record['read']}: {record['file']}:{record['line']}")
    return line, details


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", help="one skill, e.g. cosmo-cmb")
    parser.add_argument("--due", type=int, help="list files older than, and [doc] facts stale within, this many days")
    parser.add_argument("--today", type=date.fromisoformat, default=date.today(), help=argparse.SUPPRESS)
    args = parser.parse_args()
    skills = [ROOT / "skills" / args.skill] if args.skill else sorted(
        path for path in (ROOT / "skills").iterdir() if (path / "references").is_dir())
    for skill in skills:
        line, details = status(skill, args.today, args.due)
        print(line)
        for detail in details:
            print(detail)
    return 0


if __name__ == "__main__":
    sys.exit(main())
