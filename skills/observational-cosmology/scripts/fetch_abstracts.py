#!/usr/bin/env python3
"""Print first author, title and abstract for arXiv IDs.

Used when gating or refreshing a cosmo-* skill: read the abstract of a cited
paper and compare it with the number the skill quotes. The author list is
left out on purpose (collaboration papers carry hundreds of names).

    python3 fetch_abstracts.py 2503.14738 2607.27410 [--chars 1500]

Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

API = "https://export.arxiv.org/api/query"
ATOM = {"a": "http://www.w3.org/2005/Atom"}
ATTEMPTS = 6


def query(ids: list[str]) -> bytes:
    url = f"{API}?{urllib.parse.urlencode({'id_list': ','.join(ids), 'max_results': len(ids)})}"
    for attempt in range(ATTEMPTS):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "cosmo-skill-gate/1.0"})
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError) as error:
            wait = 20 * (attempt + 1)
            print(f"arXiv API: {error}; retry in {wait} s", file=sys.stderr)
            time.sleep(wait)
    raise SystemExit("arXiv API unreachable or rate-limited; rerun later")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("ids", nargs="+", help="arXiv IDs, new or old style, without version")
    parser.add_argument("--chars", type=int, default=0, help="truncate each abstract to this many characters")
    args = parser.parse_args()

    seen = set()
    for entry in ET.fromstring(query(args.ids)).findall("a:entry", ATOM):
        link = entry.findtext("a:id", default="", namespaces=ATOM)
        title = entry.findtext("a:title", default="", namespaces=ATOM)
        if "/abs/" not in link or title.strip() == "Error":
            continue
        ident = re.sub(r"v\d+$", "", link.split("/abs/")[1])
        seen.add(ident.lower())
        author = entry.find("a:author", ATOM)
        first = author.findtext("a:name", default="?", namespaces=ATOM).strip() if author is not None else "?"
        abstract = " ".join(entry.findtext("a:summary", default="", namespaces=ATOM).split())
        if args.chars:
            abstract = abstract[:args.chars]
        print(f"### {ident} | {first} | {' '.join(title.split())}\n{abstract}\n")

    missing = [ident for ident in args.ids if ident.lower() not in seen]
    for ident in missing:
        print(f"### {ident} | NOT FOUND on arXiv\n")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
