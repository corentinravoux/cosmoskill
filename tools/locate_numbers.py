#!/usr/bin/env python3
"""Find, in the cited paper itself, the place of numbers that lack one.

Step 5.3 of the plan of 2026-10-21. For every statement that
`tools/check_numbers.py` reports as `no-place` and that names exactly one
paper, read that paper (its HTML rendering through the cache of
`fetch_paper.py`, or its arXiv abstract when there is no rendering) and
search it for the statement's specific numbers: those with a decimal point
or at least three digits, compared without sign. A place is proposed only
when every specific number is found and all of them sit in one block of the
paper (a paragraph, a table row, a caption) or, failing that, in one
section; a lone number with fewer than three significant digits must occur
in exactly one block of the paper. The place is that section, `abstract`,
or the section of the table.

    python3 tools/locate_numbers.py --skill cosmo-bbn            # propose
    python3 tools/locate_numbers.py --skill cosmo-bbn --apply    # write

Proposals go to `<cache>/locate/<skill>.tsv`. `--apply` writes each found
place into the statement: a bare `[src]` becomes `[src: <place>]`; without
a bare `[src]`, `(arXiv:<id>)` becomes `(arXiv:<id>, <place>)`; otherwise
`[src: <place>]` is added at the end of the statement. A table row without a
bare `[src]` is left for a person. Nothing is written for a number that was
not found. Standard library; network only for papers not yet cached.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "skills" / "observational-cosmology" / "scripts"))
import check_numbers  # noqa: E402
import fetch_paper  # noqa: E402

OUT = fetch_paper.CACHE.parent / "locate"
ABSTRACTS = fetch_paper.CACHE.parent / "abstracts.json"
SPECIFIC = re.compile(r"\d+\.\d+|\d{3,}")
NUMBERED = re.compile(r"^(?:(?:Appendix|App\.?)\s+([A-Z](?:\.\d+)*)|([A-Z]?\d+(?:\.\d+)*|[IVX]+(?:\.\d+)*|[A-Z](?:\.\d+)+))\b\.?\s*(.*)$")


def specific(values: list[str]) -> list[str]:
    out = []
    for value in values:
        bare = value.lstrip("−-–").replace(",", "")
        if SPECIFIC.fullmatch(bare) and bare not in out:
            out.append(bare)
    return out


def contains(text: str, number: str) -> bool:
    pattern = r"(?<![\d.])" + re.escape(number) + r"(?!\.?\d)"
    return re.search(pattern, text.replace(",", "")) is not None


def label(title: str) -> str:
    title = title.strip()
    if title.lower().startswith("abstract"):
        return "abstract"
    match = NUMBERED.match(title)
    if match and match.group(1):
        return f"App. {match.group(1)}"
    if match and match.group(2):
        return f"Sect. {match.group(2)}"
    return f'Sect. "{title[:40]}"'


def blocks_with_sections(ident: str):
    """Return [(section label, block text)] for the HTML rendering, or None."""
    try:
        document, _ = fetch_paper.download(ident, refresh=False)
    except SystemExit:
        return None
    current, out = "abstract", []
    for kind, level, text in fetch_paper.parse(document):
        if kind == "heading":
            if level >= 2:
                current = label(text)
            continue
        out.append((current, text))
    return out


def abstract_of(ident: str, store: dict) -> str | None:
    if ident in store:
        return store[ident]
    url = f"{fetch_paper.API}?{urllib.parse.urlencode({'id_list': ident, 'max_results': 1})}"
    for attempt in range(4):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "cosmo-skill-verify/1.0"})
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = response.read()
            break
        except Exception:  # network: retry, then give up
            time.sleep(10 * (attempt + 1))
    else:
        return None
    entry = ET.fromstring(payload).find("a:entry", fetch_paper.ATOM)
    text = " ".join(entry.findtext("a:summary", default="", namespaces=fetch_paper.ATOM).split()) if entry is not None else ""
    store[ident] = text
    return text


def significant(number: str) -> int:
    return len(number.replace(".", "").lstrip("0"))


def place_for(numbers: list[str], blocks, abstract: str | None) -> str | None:
    if len(numbers) == 1 and significant(numbers[0]) < 3:
        # A lone short number is accepted only where it occurs once in the paper.
        texts = [text for _, text in blocks] if blocks else ([abstract] if abstract else [])
        if sum(contains(text, numbers[0]) for text in texts) != 1:
            return None
    if blocks:
        for section, text in blocks:
            if all(contains(text, number) for number in numbers):
                return section
        sections = set()
        for number in numbers:
            where = {section for section, text in blocks if contains(text, number)}
            if len(where) != 1:
                return None
            sections |= where
        return sections.pop() if len(sections) == 1 else None
    if abstract and all(contains(abstract, number) for number in numbers):
        return "abstract"
    return None


def propose(skill: Path, store: dict, pause: float) -> list[dict]:
    proposals, papers = [], {}
    for record in check_numbers.scan(skill):
        if record["status"] != "no-place" or record["derived"]:
            continue
        idents = {match.group(1) or match.group(0) for match in check_numbers.IDENT.finditer(record["text"])}
        idents = {ident.strip().rstrip(".,;)") for ident in idents}
        if len(idents) != 1:
            continue
        ident = idents.pop()
        numbers = specific(record["numbers"])
        if not numbers or ident.lower().startswith("doi:"):
            continue
        if ident not in papers:
            cached = (fetch_paper.CACHE / (ident.replace("/", "_") + ".html")).is_file()
            papers[ident] = blocks_with_sections(ident)
            if not cached:
                time.sleep(pause)
            if papers[ident] is None:
                abstract_of(ident, store)
        place = place_for(numbers, papers[ident], store.get(ident))
        proposals.append({**record, "ident": ident, "specific": numbers, "place": place})
    return proposals


def apply(proposals: list[dict]) -> tuple[int, int]:
    written = skipped = 0
    by_file: dict[str, list[dict]] = {}
    for proposal in proposals:
        if proposal["place"]:
            by_file.setdefault(proposal["file"], []).append(proposal)
    for name, items in by_file.items():
        path = ROOT / name
        lines = path.read_text(encoding="utf-8").split("\n")
        for item in sorted(items, key=lambda entry: -entry["line"]):
            span = range(item["line"] - 1, item["last"])
            place, ident = item["place"], item["ident"]
            index = next((i for i in span if "[src]" in lines[i]), None)
            if index is not None:
                lines[index] = lines[index].replace("[src]", f"[src: {place}]", 1)
                written += 1
                continue
            if lines[item["line"] - 1].lstrip().startswith("|"):
                skipped += 1
                continue
            index = next((i for i in span if f"(arXiv:{ident})" in lines[i]), None)
            if index is not None:
                lines[index] = lines[index].replace(f"(arXiv:{ident})", f"(arXiv:{ident}, {place})", 1)
            else:
                lines[item["last"] - 1] = lines[item["last"] - 1].rstrip() + f" [src: {place}]"
            written += 1
        path.write_text("\n".join(lines), encoding="utf-8")
    return written, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", required=True)
    parser.add_argument("--apply", action="store_true", help="write the places found into the skill files")
    parser.add_argument("--pause", type=float, default=1.0, help="seconds between downloads of uncached papers")
    args = parser.parse_args()
    store = json.loads(ABSTRACTS.read_text(encoding="utf-8")) if ABSTRACTS.is_file() else {}
    proposals = propose(ROOT / "skills" / args.skill, store, args.pause)
    ABSTRACTS.parent.mkdir(parents=True, exist_ok=True)
    ABSTRACTS.write_text(json.dumps(store), encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)
    report = OUT / f"{args.skill}.tsv"
    report.write_text("file\tline\tident\tplace\tnumbers\ttext\n" + "".join(
        f"{p['file']}\t{p['line']}\t{p['ident']}\t{p['place'] or ''}\t{' '.join(p['specific'])}\t{p['text'][:200]}\n"
        for p in proposals), encoding="utf-8")
    found = sum(1 for p in proposals if p["place"])
    print(f"{args.skill}: {len(proposals)} statements tried, {found} places found; report {report}")
    if args.apply:
        written, skipped = apply(proposals)
        print(f"{written} places written, {skipped} table rows without a bare [src] left for a person")
    return 0


if __name__ == "__main__":
    sys.exit(main())
