#!/usr/bin/env python3
"""Read an arXiv paper: its abstract, its outline, one section, or the lines around a term.

This is the tool for level 4: checking a number in the paper it is cited
from. The body is read from the public HTML rendering of the paper
(arxiv.org/html, then ar5iv as a fallback) and printed as plain text. The
abstract comes from the arXiv API and exists for every paper.

    fetch_paper.py 2503.14739 --abstract
    fetch_paper.py 2503.14739 2607.27410 --abstract     several at once
    fetch_paper.py 2503.14739 --outline
    fetch_paper.py 2503.14739 --section "Results"
    fetch_paper.py 2503.14739 --grep "8.632" --context 2
    fetch_paper.py 2503.14739 --grep "D_H" --grep "r_d" --max 5

`--section` takes a number from the outline or part of a title. `--grep`
takes plain text, not a pattern; several are combined with "and" on the same
paragraph. Mathematics is printed from the rendering's LaTeX annotations,
so a number written in a formula is found as it appears in the source.

Not every paper has an HTML rendering (older submissions, PDF-only ones). The
script then says so and exits with status 2: `--abstract` still works, and
the PDF can be read by other means.

Standard library only.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_sources import unreachable  # noqa: E402

SOURCES = ["https://arxiv.org/html/{id}", "https://ar5iv.labs.arxiv.org/html/{id}"]
API = "https://export.arxiv.org/api/query"
ATOM = {"a": "http://www.w3.org/2005/Atom"}
CACHE = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "cosmo-skill-verify" / "papers"
ARXIV_ID = re.compile(r"^(?:\d{4}\.\d{4,5}|[a-z][a-z\-]+(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?$")
BLOCK = {"p", "div", "li", "tr", "figcaption", "caption", "blockquote", "table", "section", "article", "dt", "dd"}
HEADING = {"h1", "h2", "h3", "h4", "h5", "h6"}
SKIP = {"script", "style", "nav", "header", "footer", "button", "svg"}
ATTEMPTS = 4


class Paper(HTMLParser):
    """Turn the rendering into a list of (kind, level, text) blocks."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks: list[tuple[str, int, str]] = []
        self.buffer: list[str] = []
        self.skip = 0
        self.math = 0
        self.heading = 0
        self.annotation = False

    def flush(self, kind="text", level=0):
        text = " ".join("".join(self.buffer).split())
        self.buffer = []
        if text:
            self.blocks.append((kind, level, text))

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag in SKIP:
            self.skip += 1
        elif tag == "math":
            self.math += 1
            source = attributes.get("alttext")
            if source and not self.skip:
                self.buffer.append(f" {source} ")
        elif tag == "annotation" and attributes.get("encoding") == "application/x-tex":
            self.annotation = True
        elif tag in HEADING:
            self.flush()
            self.heading = int(tag[1])
        elif tag in BLOCK or tag == "br":
            self.flush()
        elif tag in ("td", "th"):
            self.buffer.append(" | ")

    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
        elif tag == "math":
            self.math = max(0, self.math - 1)
        elif tag == "annotation":
            self.annotation = False
        elif tag in HEADING:
            self.flush("heading", self.heading)
            self.heading = 0
        elif tag in BLOCK:
            self.flush()

    def handle_data(self, data):
        if self.skip or self.math or self.annotation:
            return
        self.buffer.append(data)


def parse(document: str) -> list[tuple[str, int, str]]:
    parser = Paper()
    parser.feed(document)
    parser.flush()
    return parser.blocks


def no_route(ident: str, error) -> None:
    print(f"arXiv cannot be reached from this machine ({error}); do not retry. "
          f"Read https://arxiv.org/abs/{ident} with a web tool if you have one; "
          "otherwise say that L4 was required and not done.", file=sys.stderr)


def download(ident: str, refresh: bool) -> tuple[str, str]:
    cached = CACHE / (ident.replace("/", "_") + ".html")
    if cached.is_file() and not refresh:
        return cached.read_text(encoding="utf-8"), "cache"
    last = ""
    blocked = 0
    for template in SOURCES:
        url = template.format(id=ident)
        for attempt in range(ATTEMPTS):
            try:
                request = urllib.request.Request(url, headers={"User-Agent": "cosmo-skill-verify/1.0"})
                with urllib.request.urlopen(request, timeout=60) as response:
                    document = response.read().decode("utf-8", errors="replace")
                if len(document) < 5000 or "ltx_" not in document:
                    last = f"{url}: no rendering of the paper at this address"
                    break
                try:
                    CACHE.mkdir(parents=True, exist_ok=True)
                    cached.write_text(document, encoding="utf-8")
                except OSError:
                    pass
                return document, url
            except urllib.error.HTTPError as error:
                last = f"{url}: HTTP {error.code}"
                blocked += unreachable(error)
                if error.code in (429, 503):
                    time.sleep(15 * (attempt + 1))
                    continue
                break
            except (urllib.error.URLError, TimeoutError) as error:
                last = f"{url}: {error}"
                if unreachable(error):
                    blocked += 1
                    break
                time.sleep(5 * (attempt + 1))
    if blocked == len(SOURCES):
        no_route(ident, last)
        raise SystemExit(3)
    raise SystemExit(f"no HTML rendering could be read for {ident} ({last}); "
                     "use --abstract, or the PDF")


def abstracts(idents: list[str]) -> int:
    """Print first author, title and abstract from the arXiv API."""
    url = f"{API}?{urllib.parse.urlencode({'id_list': ','.join(idents), 'max_results': len(idents)})}"
    payload = None
    for attempt in range(ATTEMPTS + 2):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "cosmo-skill-verify/1.0"})
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = response.read()
            break
        except (urllib.error.URLError, TimeoutError) as error:
            if unreachable(error):
                for ident in idents:
                    no_route(ident, error)
                return 3
            print(f"arXiv API: {error}; retry in {20 * (attempt + 1)} s", file=sys.stderr)
            time.sleep(20 * (attempt + 1))
    if payload is None:
        print("arXiv API unreachable or rate-limited; rerun later", file=sys.stderr)
        return 2
    seen = set()
    for entry in ET.fromstring(payload).findall("a:entry", ATOM):
        link = entry.findtext("a:id", default="", namespaces=ATOM)
        title = entry.findtext("a:title", default="", namespaces=ATOM)
        if "/abs/" not in link or title.strip() == "Error":
            continue
        ident = re.sub(r"v\d+$", "", link.split("/abs/")[1])
        seen.add(ident.lower())
        author = entry.find("a:author", ATOM)
        first = author.findtext("a:name", default="?", namespaces=ATOM).strip() if author is not None else "?"
        text = " ".join(entry.findtext("a:summary", default="", namespaces=ATOM).split())
        print(f"### {ident} | {first} | {' '.join(title.split())}\n{text}\n")
    missing = [ident for ident in idents if re.sub(r"v\d+$", "", ident).lower() not in seen]
    for ident in missing:
        print(f"### {ident} | NOT FOUND on arXiv\n")
    return 1 if missing else 0


def outline(blocks) -> list[tuple[int, int, str]]:
    """Return (block index, level, title) for the headings below the title."""
    return [(index, level, text) for index, (kind, level, text) in enumerate(blocks) if kind == "heading" and level >= 2]


def section(blocks, wanted: str) -> list[tuple[str, int, str]]:
    heads = outline(blocks)
    chosen = None
    if wanted.isdigit() and 1 <= int(wanted) <= len(heads):
        chosen = int(wanted) - 1
    else:
        folded = wanted.lower()
        matches = [n for n, (_, _, title) in enumerate(heads) if folded in title.lower()]
        if matches:
            chosen = matches[0]
    if chosen is None:
        raise SystemExit(f"no section matches {wanted!r}; run with --outline")
    start, level, _ = heads[chosen]
    end = len(blocks)
    for index, other_level, _ in heads[chosen + 1:]:
        if other_level <= level:
            end = index
            break
    return blocks[start:end]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("papers", nargs="+", metavar="paper", help="arXiv identifier, with or without version")
    parser.add_argument("--abstract", action="store_true", help="print the abstract; accepts several papers")
    parser.add_argument("--outline", action="store_true", help="list the sections")
    parser.add_argument("--section", help="print one section: its number in the outline, or part of its title")
    parser.add_argument("--grep", action="append", default=[], help="print paragraphs containing this text; repeat to require several")
    parser.add_argument("--context", type=int, default=0, help="with --grep: paragraphs printed before and after each hit")
    parser.add_argument("--max", type=int, default=12, help="with --grep: hits printed at most (default 12)")
    parser.add_argument("--chars", type=int, default=12000, help="characters printed at most (default 12000)")
    parser.add_argument("--refresh", action="store_true", help="download again instead of using the cached copy")
    args = parser.parse_args()

    for ident in args.papers:
        if not ARXIV_ID.match(ident):
            raise SystemExit(f"{ident!r} is not an arXiv identifier")
    if args.abstract:
        return abstracts(args.papers)
    if len(args.papers) != 1:
        raise SystemExit("the outline, a section or a search take one paper at a time")
    args.paper = args.papers[0]
    try:
        document, origin = download(args.paper, args.refresh)
    except SystemExit as failure:
        if failure.code == 3:
            return 3
        print(failure, file=sys.stderr)
        return 2
    blocks = parse(document)
    title = next((text for kind, level, text in blocks if kind == "heading" and level == 1), "")
    print(f"### {args.paper} | {title} | read from {origin}")

    out: list[str] = []
    if args.outline or not (args.section or args.grep):
        for number, (_, level, text) in enumerate(outline(blocks), start=1):
            out.append(f"{number:3d}. {'  ' * (level - 2)}{text}")
    if args.section:
        for kind, level, text in section(blocks, args.section):
            out.append(f"\n{'#' * level} {text}\n" if kind == "heading" else text)
    if args.grep:
        wanted = [term.lower() for term in args.grep]
        hits = [index for index, (kind, _, text) in enumerate(blocks) if kind == "text" and all(term in text.lower() for term in wanted)]
        shown = set()
        last_heading = ""
        for hit in hits[:args.max]:
            heading = next((text for kind, _, text in reversed(blocks[:hit]) if kind == "heading"), "")
            if heading != last_heading:
                out.append(f"\n[in: {heading}]")
                last_heading = heading
            for index in range(max(0, hit - args.context), min(len(blocks), hit + args.context + 1)):
                if index not in shown and blocks[index][0] == "text":
                    shown.add(index)
                    out.append(("> " if index == hit else "  ") + blocks[index][2])
        out.append(f"\n{len(hits)} paragraph(s) contain {' and '.join(repr(t) for t in args.grep)}"
                   + (f"; first {args.max} shown" if len(hits) > args.max else ""))
    text = html.unescape("\n".join(out))
    if len(text) > args.chars:
        text = text[:args.chars] + f"\n... cut at {args.chars} characters; narrow the request or raise --chars"
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
