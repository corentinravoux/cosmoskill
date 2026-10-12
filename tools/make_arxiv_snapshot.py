#!/usr/bin/env python3
"""Write the arXiv snapshot used by continuous integration.

The bibliography checker caches every paper it has found on arXiv. This
script copies, from that local cache, the title and first author of every
arXiv identifier cited in any `sources.tsv`, into
`tests/fixtures/arxiv-snapshot.json`. Continuous integration loads the
snapshot as the checker's cache, so a push is checked in full without asking
arXiv for two thousand papers; only identifiers absent from the snapshot go
to the network.

Run the checker online first (it fills the cache), then this script:

    python3 skills/observational-cosmology/scripts/verify_sources.py skills/*/
    python3 tools/make_arxiv_snapshot.py

Standard library only. Exit status 1 if an identifier is not in the cache.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "cosmo-skill-verify" / "arxiv.json"
SNAPSHOT = ROOT / "tests" / "fixtures" / "arxiv-snapshot.json"
ARXIV_ID = re.compile(r"^(?:\d{4}\.\d{4,5}|[a-z][a-z\-]+(?:\.[A-Z]{2})?/\d{7})$")


def main() -> int:
    cache = json.loads(CACHE.read_text(encoding="utf-8"))
    wanted = set()
    for sources in sorted((ROOT / "skills").glob("*/references/sources.tsv")):
        for line in sources.read_text(encoding="utf-8").splitlines()[1:]:
            fields = line.split("\t")
            if len(fields) > 1 and ARXIV_ID.match(fields[1]):
                wanted.add(fields[1].lower())
    missing = sorted(wanted - set(cache))
    if missing:
        print(f"{len(missing)} identifier(s) not in the cache; run the checker online first:", *missing[:10], file=sys.stderr)
        return 1
    snapshot = {ident: {"title": cache[ident]["title"], "authors": cache[ident]["authors"][:1]} for ident in sorted(wanted)}
    SNAPSHOT.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT.write_text(json.dumps(snapshot, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    print(f"{len(snapshot)} papers written to {SNAPSHOT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
