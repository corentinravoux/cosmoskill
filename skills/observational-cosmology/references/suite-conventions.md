# Suite conventions — how the cosmo-* skills are built and kept current

Scope: the rules every `cosmo-<domain>` skill follows, how to check one, and
how to refresh one. The design documents are in the `docs/` directory of the
package repository.

## File contract
<!-- key: file-contract -->

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
<!-- key: citations-and-provenance -->

- Prose cites `arXiv:<id>` or `doi:<doi>`. Every cited identifier has one row
  in `sources.tsv`, and every row is cited.
- Only numbers read in a paper are given (owner, 2026-10-23). Every number
  names its paper (`arXiv:` or `doi:`) and the place it was read, in a flag:

  | flag | meaning | use in a manuscript |
  |---|---|---|
  | `[src: <place>]` | read in the cited paper itself at that place (section, table, equation, figure, footnote or abstract) when the file was written | re-read the paper, then quote |
  | `[sec: <place>]` | taken from a named secondary source at that place | go to the primary paper first |
  | `[doc: <source>, <date>]` | a code fact (version, release date, default) or a facility fact (date, status, count) read on that date at a URL, a repository path or an installed package; not a paper (owner, 2026-10-26); stale two years after the read date, when `tools/check_numbers.py` fails it until it is re-read | re-read the page; quote with its date, it may have changed |
  | `[der]` | reasoning in words drawn from cited results; carries no number | do not quote as a result |

  A statement whose numbers are not values (notation, names, pointers)
  carries `<!-- num: not a value -->`; it holds no result to quote.

- A number without its paper and place, a number computed by an agent, or a
  claim with no citation, is a defect in the file: fix the file, do not
  quote the number. `tools/check_numbers.py` lists them.
- Forecasts are labelled as forecasts and never share a table with
  measurements without a column that says which is which.
- Each `results.md` and `surveys-and-data.md` starts with a snapshot date.
  A result older than the snapshot may have been superseded; a "latest"
  statement is only as current as that date.

## Checking a skill
<!-- key: checking-a-skill -->

From the repository root, which is two levels above the hub skill's
directory:

```bash
python3 skills/observational-cosmology/scripts/verify_sources.py skills/cosmo-<domain>
python3 skills/observational-cosmology/scripts/verify_sources.py --offline skills/*/
```

The checker asks arXiv for every cited paper (existence, title, first
author) and reports citations without a bibliography row and rows without a
citation. `--offline` runs the local checks only. Exit status 0 means clean.
Papers found once are cached under the user's cache directory.

It does not check that a number is the one the paper gives. That is done by
reading the paper, when the number is needed:

```bash
python3 skills/observational-cosmology/scripts/fetch_paper.py 2503.14739 --abstract
python3 skills/observational-cosmology/scripts/fetch_paper.py 2503.14739 --outline
python3 skills/observational-cosmology/scripts/fetch_paper.py 2503.14739 --grep "8.632" --context 1
```

## Refreshing a domain
<!-- key: refreshing-a-domain -->

The field moves monthly; a skill is as current as its snapshot date. The
update cycle below is meant to be run every few months, one domain at a
time. It is the same for the reference files of a domain and for its
specialist dossiers under `deep/`, each of which carries its own snapshot
date.

1. **Read the snapshot date** at the top of the domain's `results.md`.
   `python3 tools/refresh_status.py --due 90` lists, per skill, the files
   older than 90 days and the `[doc]` facts that go stale within 90 days.
2. **Find what appeared since.** For each section of `results.md`, a
   date-sorted arXiv search from the snapshot date on, by any means
   available: the arXiv listing or search, INSPIRE, or an arXiv tool server
   with topic alerts where one is installed. Look also at what cites the
   papers behind the headline values: that is where a superseding result
   shows up.
3. **Read each new result at source**: the abstract, and the section that
   holds the number when the abstract does not. Nothing is written from
   memory.
4. **Edit the files.**
   - `results.md`: add the row; move the value it replaces to the history
     section, marked as superseded, instead of deleting it.
   - `surveys-and-data.md`: new releases, changed dates, changed status.
   - `open-questions.md`: a controversy that moved, a claim that became
     stale.
   - `SKILL.md`: the "What an expert holds in mind" bullets when a headline
     moved, and "Errors that recur" when a common statement became wrong.
   - `sources.tsv`: one row per new paper cited.
5. **Bump the snapshot date** in every file touched.
6. **Keys.** A new section needs a key; an existing key is never renamed.
   A section that is removed is recorded in `references/retired-keys.tsv`,
   because a researcher's notes may be attached to it.
7. **Run the upkeep tools**, from the repository root:

   ```bash
   python3 tools/assign_keys.py                 # keys for new sections
   python3 tools/sync_blocks.py                 # level block and sizes of each SKILL.md
   python3 skills/observational-cosmology/scripts/verify_sources.py skills/cosmo-<domain>
   python3 tools/check_keys.py --against <last release tag or commit>
   python3 -m unittest discover -s tests
   ```

8. **After the domains, the cross-probe files**: `cosmo-tensions-anomalies`
   is a synthesis of the other skills and is updated last, from them; then
   the digest `references/field-state-2026.md` of this hub.
9. **Record what moved** in the commit message: which headline values
   changed, which were superseded.

A researcher with local layers then runs
`python3 skills/observational-cosmology/scripts/layers.py check`, which lists
notes attached to a section the update retired.

Never refresh from memory. A value remembered and a value read differ often
enough, and in ways plausible enough, that the difference is only visible to
someone holding the paper.

## Adding a domain
<!-- key: adding-a-domain -->

Copy the shape of an existing `cosmo-*` skill, follow `docs/agent-brief.md`
of the package repository, add the skill's row to the router table in the hub
`SKILL.md`, and run the upkeep tools of the update cycle. How the new skill
becomes visible depends on how the package was installed; the README gives
the routes.

## What the suite does not hold
<!-- key: what-the-suite-does-not-hold -->

Discussion, tables for reading, and links to sources. It is not a database
of verified numbers: a number needed for a manuscript is read again in the
linked paper. A compilation meant to be loaded by code belongs in a data
package with its own integrity tests, not under a skill.
