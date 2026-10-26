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
    doc       it holds a `[doc: <URL, path or installed package>, <YYYY-MM-DD>]`
              flag, itself or through its caption: a code fact or a fact from an
              official page, read on that date (owner, 2026-10-26)
    marked    it carries `<!-- num: not a value -->`: its numbers are names,
              notation or pointers, not values (owner, 2026-10-26)
    bad-doc   it holds a `[doc` flag without a source and a valid read date
    old-src   it holds a `[src: …]` or `[sec: …]` flag that names a source other
              than a paper (an installed package, PyPI, GitHub, a checkout, a
              README, documentation, a web page): rewrite it as `[doc]` after
              a re-read. Checked on every statement, with or without a number
              (owner, 2026-10-26)
    stale-doc its oldest `[doc]` read date is more than two years old: re-read
              the source and update the fact and the date (owner, 2026-10-26)
    no-place  it holds an identifier but no place
    no-paper  it holds a place but no identifier
    none      it holds neither
    derived   it carries a `[der` flag (any of the above)

What is not counted as a number: years, arXiv identifiers and DOIs (also bare
identifiers in a list), section, table, equation, figure, step, "§" and
reference numbers, list numbering and numbered bold headings, flags in square
brackets, the `Snapshot:` line, level names (L1 to L4), single digits, the
"21" of "21 cm" and of 21cm-named codes; since 2026-10-26 also catalogue
designations (NGC 4258, 1ES 1553+113), spectral lines named by wavelength
(He I 10830), a short list of field and instrument names (Stripe 82,
LOFAR 2.0) and confidence levels named as such ("68% intervals", "(95%)").
A date without a day ("November 2026", "mid-2027") is not counted (owner,
2026-10-26).
The block written by
`tools/sync_blocks.py` is skipped.

    python3 tools/check_numbers.py                 # one line per skill
    python3 tools/check_numbers.py --skill cosmo-cmb --list
    python3 tools/check_numbers.py --check         # exit 1 above the baseline

`doc` and `marked` statements pass; they are counted apart and listed with
`--list --status doc` (sorted by read date, oldest first) or `--status marked`.

`--check` compares the count of statements that do not pass, and of
`derived` ones, per skill, with `tools/numbers-baseline.tsv`; a count may go
down, never up. `--write-baseline` rewrites that file from the current
state. Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
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
    re.compile(r"§\s*\d[\d.]*(?:\s*[–\-]\s*\d[\d.]*)?"),
    re.compile(r"\brefs?\.\s*\d+(?:\s*(?:,|and|–|-)\s*\d+)*", re.I),
    re.compile(r"\b21\s?-?cm\w*", re.I),
    re.compile(r"^\*\*\d+(?:\.\d+)+(?=\s+[A-Z])"),
    # Names, not values (owner, 2026-10-26, step 2). Each rule removes one number, never a statement.
    # Catalogue designations: "NGC 4258", "1ES 1553+113", "PKS 0405−123", "J1342+0928".
    re.compile(r"\b(?:NGC|IC|UGC|PGC|PKS|1ES|3C|4C|Abell|ESO|Mrk|HE|Q)\s?\d+(?:[.+−\-–]\d+)*|\bJ\d{4}(?:\.\d+)?[+−\-]\d{2,4}"),
    # Spectral lines named by their wavelength: "He I 10830", "Si II 1260", "C IV 1550", "Mg II 2796".
    re.compile(r"\b(?:H|He|C|N|O|Mg|Si|S|Fe|Ca|Na|Al|Ne)\s?(?:I{1,3}V?|IV|VI{0,3}|X)\]?\s?λ?\s?\d{3,5}\b"),
    # Fields and instruments whose name holds a number.
    re.compile(r"\bStripe\s?82\b|\bLOFAR\s?2\.0\b|\bSPTpol\s?500d\b|\bSPTpol\s?100d\b|\bSPT-?SZ\s?2500d\b", re.I),
    # A confidence level named as such: "(68%)", "68% intervals", "95% upper limits", "limits are 95%",
    # "at 95% C.L.". A bare percent ("95% complete", "a purity of 95%") stays a number.
    re.compile(r"(?:\(|\b(?:at|are|is|as|and|or|all|limits?|intervals?|errors?|bounds?|one-tail|two-tail|one-sided|two-sided)\s+)"
               r"(?:68(?:\.3)?|90|95(?:\.4)?|99(?:\.7)?)\s?%(?=\s*(?:\)|,|;|\.|$|and\b|or\b|C\.?L|confidence|credible|"
               r"intervals?|limits?|upper|lower|one-tail|two-tail|symmetric|posterior|ranges?|while|unless))"
               r"|\b(?:68(?:\.3)?|90|95(?:\.4)?|99(?:\.7)?)\s?%\s*(?=(?:C\.?L\.?|confidence|credible|intervals?|"
               r"(?:upper |lower )?limits?|upper|lower|one-tail|two-tail|symmetric)\b)", re.I),
]
# A non-paper source (owner, 2026-10-26): "[doc: https://pypi.org/project/camb/, 2026-10-26]",
# "[doc: installed camb 2.0.4, 2026-10-26]". The source must look like a URL, a path or an installed package.
DOC_FLAG = re.compile(r"\[doc\b[^\]]*\]", re.I)
DOC = re.compile(r"\[doc:\s*(?P<source>[^\]]*?(?:[./]|\binstalled\s)[^\]]*?),\s*(?P<date>20\d\d-[01]\d-[0-3]\d)\s*\]", re.I)
MARKER = "<!-- num: not a value -->"
# A `[doc]` fact must be re-read at least every two years (owner, 2026-10-26).
STALE_AFTER_YEARS = 2
PASSING = {"ok", "doc", "marked"}
# A [src]/[sec] flag is for a paper (or a named secondary paper); a code or web source takes [doc] (owner, 2026-10-26).
OLD_SRC = re.compile(r"\[(?:src|sec):[^\]]*?(?:\b(?:installed|PyPI|pypi|GitHub|github|checkout|context7|README|docs?|"
                     r"documentation|repository|repo|metadata|API|website|web|page)\b|https?://|www\.)[^\]]*\]")


def old_src(statement: str) -> bool:
    """A non-paper source in a [src]/[sec] flag; a flag quoted in a code span (a legend) does not count."""
    return bool(OLD_SRC.search(re.sub(r"`[^`]*`", " ", statement)))


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


def doc_dates(text: str) -> list[str]:
    """The read dates of the valid `[doc]` flags in a text; an invalid calendar date does not count."""
    dates = []
    for match in DOC.finditer(text):
        try:
            date.fromisoformat(match.group("date"))
        except ValueError:
            continue
        dates.append(match.group("date"))
    return dates


def stale_limit(today: date) -> date:
    """The oldest read date that is not stale on `today`."""
    try:
        return today.replace(year=today.year - STALE_AFTER_YEARS)
    except ValueError:  # 29 February
        return today.replace(year=today.year - STALE_AFTER_YEARS, day=28)


def classify(statement: str, caption: str, today: date | None = None) -> str:
    context = statement + " " + caption
    if old_src(statement):
        return "old-src"
    if MARKER in statement:
        return "marked"
    if DOC_FLAG.search(statement) or DOC_FLAG.search(caption):
        flags = len(DOC_FLAG.findall(statement)) or len(DOC_FLAG.findall(caption))
        valid = len(doc_dates(statement)) or len(doc_dates(caption))
        if not valid or valid != flags:
            return "bad-doc"
        read = min(doc_dates(statement) or doc_dates(caption))
        return "stale-doc" if date.fromisoformat(read) < stale_limit(today or date.today()) else "doc"
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
            if not values and not old_src(statement):
                continue
            found.append({"file": str(path.relative_to(ROOT)), "line": line, "last": last,
                          "status": classify(statement, caption),
                          "read": min(doc_dates(statement) or doc_dates(caption) or [""]),
                          "derived": "[der" in statement, "numbers": values, "text": statement})
    return found


def counts(records: list[dict]) -> tuple[int, int, int]:
    return (len(records), sum(record["status"] not in PASSING for record in records),
            sum(record["derived"] for record in records))


def read_baseline() -> dict[str, tuple[int, int]]:
    if not BASELINE.is_file():
        return {}
    rows = [line.split("\t") for line in BASELINE.read_text(encoding="utf-8").splitlines()[1:] if line.strip()]
    return {row[0]: (int(row[1]), int(row[2])) for row in rows}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", help="one skill, e.g. cosmo-cmb")
    parser.add_argument("--list", action="store_true", help="print every statement that does not pass, or derived")
    parser.add_argument("--status", choices=["no-place", "no-paper", "none", "bad-doc", "stale-doc", "old-src", "derived", "doc", "marked"],
                        help="with --list: one kind only (doc and marked are listed only when asked)")
    parser.add_argument("--check", action="store_true", help="exit 1 if a skill is above the baseline")
    parser.add_argument("--write-baseline", action="store_true")
    args = parser.parse_args()

    skills = [ROOT / "skills" / args.skill] if args.skill else sorted(
        path for path in (ROOT / "skills").iterdir() if (path / "references").is_dir())
    baseline, rows, worse, listed = read_baseline(), [], [], []
    passed = {"doc": 0, "marked": 0}
    for skill in skills:
        records = scan(skill)
        total, open_, derived = counts(records)
        rows.append((skill.name, open_, derived))
        docs = sum(record["status"] == "doc" for record in records)
        marked = sum(record["status"] == "marked" for record in records)
        passed["doc"] += docs
        passed["marked"] += marked
        if args.list:
            for record in records:
                kind = "derived" if record["derived"] else record["status"]
                wanted = kind == args.status if args.status else kind not in PASSING
                if wanted:
                    listed.append(record | {"kind": kind})
        elif not args.check and not args.write_baseline:
            print(f"{skill.name:40} {total:5} statements with numbers, {open_:5} without paper and place, "
                  f"{derived:4} derived, {docs:4} doc, {marked:4} marked")
    if args.status == "doc":
        listed.sort(key=lambda record: record["read"])
    for record in listed:
        read = f" {record['read']}" if record["kind"] == "doc" else ""
        print(f"{record['file']}:{record['line']}: {record['kind']}{read}: {', '.join(record['numbers'][:4])} | "
              f"{record['text'][:160]}")
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
        print(f"total: {sum(row[1] for row in rows)} without paper and place, {sum(row[2] for row in rows)} derived, "
              f"{passed['doc']} doc, {passed['marked']} marked", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
