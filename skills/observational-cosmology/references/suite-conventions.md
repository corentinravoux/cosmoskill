# Suite conventions — how the cosmo-* skills are built and kept current

Scope: the rules every `cosmo-<domain>` skill follows, how to check one, and
how to refresh one. The design documents are in the `docs/` directory of the
package repository.

## File contract

```
cosmo-<domain>/
├── SKILL.md                         triggers, file map, core facts, checklists
└── references/
    ├── physics-and-methods.md       observables, estimators, models, codes
    ├── surveys-and-data.md          experiments, releases, samples, status
    ├── results.md                   dated headline results with provenance
    ├── systematics.md               canonical systematics and mitigations
    ├── open-questions.md            controversies, tensions, forecasts
    └── sources.tsv                  key, id, first_author, year, title, role
```

These five reference files are standard. A skill may add topical files; its
file map lists them. Load `SKILL.md` first: it says which reference answers
which question. Load one reference at a time.

## Citations and provenance

- Prose cites `arXiv:<id>` or `doi:<doi>`. Every cited identifier has one row
  in `sources.tsv`, and every row is cited.
- Every number carries a flag:

  | flag | meaning | use in a manuscript |
  |---|---|---|
  | `[src]` | read in the cited paper itself when the file was written | re-read the paper, then quote |
  | `[sec]` | taken from a named secondary source | go to the primary paper first |
  | `[der]` | derived; the derivation and its assumption are stated | quote only with the assumption |

- A number with no flag, or a claim with no citation, is a defect in the
  file: fix the file, do not quote the number.
- Forecasts are labelled as forecasts and never share a table with
  measurements without a column that says which is which.
- Each `results.md` and `surveys-and-data.md` starts with a snapshot date.
  A result older than the snapshot may have been superseded; a "latest"
  statement is only as current as that date.

## Checking a skill

From the hub skill's directory:

```bash
python3 scripts/verify_sources.py ../cosmo-<domain>
python3 scripts/verify_sources.py --offline ../cosmo-<domain>
```

The checker queries the arXiv API for every arXiv row (existence, title,
first author) and reports citations without a row and rows without a
citation. `--offline` runs the local checks only. Exit status 0 means clean.
Papers found once are cached under the user's cache directory, so repeated
runs do not hit the arXiv rate limit.

It does not check that a number is the one the paper gives: that takes
reading the paper, and is why the flags exist. To read what a cited paper
says, without its author list:

```bash
python3 scripts/fetch_abstracts.py 2503.14738 2607.27410 --chars 1500
```

## Refreshing a domain

1. Find what appeared since the snapshot date: a date-sorted arXiv search for
   each subtopic of the domain, by any means available (the arXiv listing or
   API, INSPIRE, or an arXiv tool server with topic alerts where one is
   installed).
2. For each new result: read the abstract, and the relevant section when the
   number is in the body. Update `results.md`: add the row, and move the
   superseded value to the history section rather than deleting it.
3. Add the `sources.tsv` rows, bump the snapshot date, update the "What an
   expert holds in mind" bullets in `SKILL.md` if a headline moved.
4. Run the checker.

Never refresh from memory. A value remembered and a value read differ often
enough, and in ways plausible enough, that the difference is only visible to
someone holding the paper.

## Adding a domain

Copy the shape of an existing `cosmo-*` skill, follow `docs/agent-brief.md`
of the package repository, add the skill's row to the router table in the hub
`SKILL.md`, and run the checker. How the new skill becomes visible depends on
how the package was installed; the README gives the routes.

## What the suite does not hold

Discussion, tables for reading, and pointers. A compilation meant to be
loaded by code belongs in a data package with its own integrity tests, not
under a skill.
