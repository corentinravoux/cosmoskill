#!/usr/bin/env python3
"""List the numbers of the skills that do not name their paper and place.

Rule (plan of 2026-10-21, step 5; owner, 2026-10-23): the package gives only
numbers read in a paper, and each names the paper (`arXiv:` or `doi:`
identifier) and the place it was read (section, table, equation, figure,
appendix, footnote, caption or abstract). No number computed by an agent.

A statement is a table row, a list item or a paragraph. A statement that
carries a number is

    ok        it holds an identifier and a place, itself or through the line
              just above its table (a caption such as "From arXiv:..., Table 2:")
    no-place  it holds an identifier but no place
    no-paper  it holds a place but no identifier
    none      it holds neither
    derived   it carries a `[der` flag (any of the above)

What is not counted as a number: years, arXiv identifiers and DOIs (also bare
identifiers in a list), section, table, equation, figure, step, "§" and
reference numbers, list numbering and numbered bold headings, flags in square
brackets, the `Snapshot:` line, level names (L1 to L4), single digits, the
"21" of "21 cm" and of 21cm-named codes. The block written by
`tools/sync_blocks.py` is skipped.

    python3 tools/check_numbers.py                 # one line per skill
    python3 tools/check_numbers.py --skill cosmo-cmb --list
    python3 tools/check_numbers.py --check         # exit 1 above the baseline

`--check` compares the count of statements that are not `ok`, and of
`derived` ones, per skill, with `tools/numbers-baseline.tsv`; a count may go
down, never up. `--write-baseline` rewrites that file from the current
state. Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASELINE = Path(__file__).resolve().parent / "numbers-baseline.tsv"
SKIP_PARTS = {"example-layer"}

IDENT = re.compile(r"arXiv:\s?(\d{4}\.\d{4,5}|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})|doi:\s?\S+", re.I)
# A place is a locator word followed by its number, letter or quoted name ("Sect. 4.2", "Table 3", "App. B",
# 'Sect. "Setup"'), the abstract, or a named section inside a flag ("[src: Conclusions]"). A bare word does not
# count: "figure of merit" or "summary statistics" is not a place (plan of 2026-10-23, step 4.3).
PLACE = re.compile(r"\b(?:Sects?|Sections?|Tables?|Tabs?|Eqs?|Equations?|Figs?|Figures?|Apps?|Appendix|Appendices"
                   r"|footnotes?)\.?\s*(?:[\dIVX]|[A-Z](?![a-z])|[\"“])"
                   r"|\babstract\b"
                   r"|\[(?:src|sec)[^\]]*\b(?:Conclusions?|Summary|Methods|Results|Introduction|main text)\b", re.I)
NUMBER = re.compile(r"(?<![\w.#/\-])[−\-–]?\d+(?:[.,]\d+)?")
NOT_NUMBERS = [
    re.compile(r"arXiv:\S+|doi:\S+", re.I),
    # Bare arXiv identifiers in a list, before the year rule can eat "1867" of "1401.1867".
    re.compile(r"\b\d{4}\.\d{5}\b|\b(?:0[7-9]|1\d)(?:0[1-9]|1[0-2])\.\d{4}\b"),
    re.compile(r"\b(?:Sects?|Sections?|Tables?|Tabs?|Eqs?|Equations?|Figs?|Figures?|Apps?|Appendix|Steps?|Chapter|"
               r"Part|Phase|Run|item|row|column|§)\b\.?\s*[\dA-Z][\dA-Za-z.\-–,]*(?:\s*(?:and|to|–|-)\s*[\dA-Z][\dA-Za-z.\-–]*)?",
               re.I),
    re.compile(r"\[[^\]]*\]"),
    re.compile(r"\b(?:1[89]|20)\d\d-\d\d(?:-\d\d)?\b"),
    re.compile(r"\b(?:1[89]|20)\d\d[a-z]?\b"),
    re.compile(r"\bL[1-4]\b"),
    re.compile(r"`[^`]*`"),
    re.compile(r"\(\d{1,2}\)"),
    re.compile(r"<!--.*?-->"),
    # Labels, not values (2026-10-25): "§12" (the word boundary above misses "§"), reference numbers
    # ("ref. 87"), bare arXiv identifiers in a list ("arXiv:1907.02973, 2007.15994"), the "21" of "21 cm"
    # and of code names (21cmFAST, 21CMMC), and the file's own numbered bold headings ("**9.3 Validation.**").
    re.compile(r"§\s*\d[\d.]*"),
    re.compile(r"\brefs?\.\s*\d+(?:\s*(?:,|and|–|-)\s*\d+)*", re.I),
    re.compile(r"\b21\s?-?cm\w*", re.I),
    re.compile(r"^\*\*\d+(?:\.\d+)+(?=\s+[A-Z])"),
]
BLOCK_START, BLOCK_END = "<!-- cosmoskill:block:start", "<!-- cosmoskill:block:end"
LIST_START = re.compile(r"^(?:[-*+]|\d+[.)])\s+")


def statements(text: str):
    """Yield (first line, last line, statement, caption) for the prose, list items and table rows of a file."""
    lines = text.split("\n")
    buffer, start, end, fenced, caption = [], 0, 0, False, ""
    previous, generated = "", False
    for number, raw in enumerate(lines, 1):
        line = raw.strip()
        # The block written by tools/sync_blocks.py (levels, measured sizes) is generated, not content.
        if line.startswith(BLOCK_START) or line.startswith(BLOCK_END):
            generated = line.startswith(BLOCK_START)
            continue
        if generated:
            continue
        if line.startswith("```") or line.startswith("~~~"):
            fenced = not fenced
            continue
        if fenced or line.startswith("<!-- key") or line.lower().startswith("snapshot:"):
            continue
        if line.startswith("|"):
            if buffer:
                yield start, end, " ".join(buffer), ""
                buffer = []
            if not previous.startswith("|"):
                caption = previous if not previous.startswith("#") else ""
            if not set(line) <= set("|-: "):
                yield number, number, line, caption
            previous = line
            continue
        if line:
            previous = line
        if not line or line.startswith("#") or LIST_START.match(line):
            if buffer:
                yield start, end, " ".join(buffer), ""
            buffer, start = ([LIST_START.sub("", line, count=1)], number) if line and not line.startswith("#") else ([], 0)
            end = number
            continue
        if not buffer:
            start = number
        buffer.append(line)
        end = number
    if buffer:
        yield start, end, " ".join(buffer), ""


def numbers_in(statement: str) -> list[str]:
    text = statement
    for pattern in NOT_NUMBERS:
        text = pattern.sub(" ", text)
    found = []
    for match in NUMBER.finditer(text):
        value = match.group(0).lstrip("−-–")
        if re.fullmatch(r"\d", value):
            continue
        found.append(match.group(0))
    return found


def classify(statement: str, caption: str) -> str:
    context = statement + " " + caption
    has_ident, has_place = bool(IDENT.search(context)), bool(PLACE.search(context))
    if has_ident and has_place:
        return "ok"
    if has_ident:
        return "no-place"
    if has_place:
        return "no-paper"
    return "none"


def skill_files(skill: Path):
    for path in sorted(skill.rglob("*.md")):
        if SKIP_PARTS & set(path.parts) or path.name.startswith("_progress"):
            continue
        yield path


def scan(skill: Path) -> list[dict]:
    found = []
    for path in skill_files(skill):
        for line, last, statement, caption in statements(path.read_text(encoding="utf-8")):
            values = numbers_in(statement)
            if not values:
                continue
            found.append({"file": str(path.relative_to(ROOT)), "line": line, "last": last,
                          "status": classify(statement, caption),
                          "derived": "[der" in statement, "numbers": values, "text": statement})
    return found


def counts(records: list[dict]) -> tuple[int, int, int]:
    return (len(records), sum(record["status"] != "ok" for record in records),
            sum(record["derived"] for record in records))


def read_baseline() -> dict[str, tuple[int, int]]:
    if not BASELINE.is_file():
        return {}
    rows = [line.split("\t") for line in BASELINE.read_text(encoding="utf-8").splitlines()[1:] if line.strip()]
    return {row[0]: (int(row[1]), int(row[2])) for row in rows}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", help="one skill, e.g. cosmo-cmb")
    parser.add_argument("--list", action="store_true", help="print every statement that is not ok, or derived")
    parser.add_argument("--status", choices=["no-place", "no-paper", "none", "derived"], help="with --list: one kind only")
    parser.add_argument("--check", action="store_true", help="exit 1 if a skill is above the baseline")
    parser.add_argument("--write-baseline", action="store_true")
    args = parser.parse_args()

    skills = [ROOT / "skills" / args.skill] if args.skill else sorted(
        path for path in (ROOT / "skills").iterdir() if (path / "references").is_dir())
    baseline, rows, worse = read_baseline(), [], []
    for skill in skills:
        records = scan(skill)
        total, open_, derived = counts(records)
        rows.append((skill.name, open_, derived))
        if args.list:
            for record in records:
                kind = "derived" if record["derived"] else record["status"]
                if kind == "ok" or (args.status and kind != args.status):
                    continue
                print(f"{record['file']}:{record['line']}: {kind}: {', '.join(record['numbers'][:4])} | "
                      f"{record['text'][:160]}")
        elif not args.check and not args.write_baseline:
            print(f"{skill.name:40} {total:5} statements with numbers, {open_:5} without paper and place, "
                  f"{derived:4} derived")
        if args.check and skill.name in baseline:
            before = baseline[skill.name]
            if open_ > before[0] or derived > before[1]:
                worse.append(f"{skill.name}: {open_} without paper and place (baseline {before[0]}), "
                             f"{derived} derived (baseline {before[1]})")
    if args.write_baseline:
        BASELINE.write_text("skill\twithout_paper_and_place\tderived\n"
                            + "".join(f"{name}\t{open_}\t{derived}\n" for name, open_, derived in rows),
                            encoding="utf-8")
        print(f"wrote {BASELINE.relative_to(ROOT)}")
    if args.check:
        for line in worse:
            print(line)
        print(f"{len(worse)} skill(s) above the numbers baseline", file=sys.stderr)
        return 1 if worse else 0
    if not args.list:
        print(f"total: {sum(row[1] for row in rows)} without paper and place, {sum(row[2] for row in rows)} derived",
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
