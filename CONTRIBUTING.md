# Contributing to cosmoskill

cosmoskill is a reference for an assistant helping cosmology researchers.
What makes it useful is that every statement can be traced to its source.
A contribution is welcome when it keeps that true. This file lists the rules
a change must pass; the tests check most of them.

## Before you start

- To add to the package for your own work only, use a layer instead
  (`docs/layers.md`): notes, overrides and your own dossiers live in
  `~/.cosmoskill/` and never need a pull request. An entry that would serve
  others can be promoted later (`skills/observational-cosmology/scripts/promote.py`).
- For a change to the package, open an issue first when it adds a domain,
  a dossier or a new kind of file.

## The rules

1. **Nothing from memory.** Every statement you add was read at its source
   while you wrote it: the paper, or the official page.
2. **Every number names its source and the place read.**
   - A value from a paper: the `arXiv:` or `doi:` identifier, and the place
     in a flag, `[src: Sect. 4.2]`, `[src: Table 3]`, `[src: Eq. 12]`,
     `[src: abstract]`. `[sec: <place>]` when the value was taken from
     another paper, named with its identifier.
   - A code fact (version, release date, default) or a facility fact from an
     official page (date, status, count): `[doc: <URL, repository path or
     installed package and version>, <YYYY-MM-DD read>]`. A `[doc]` fact
     goes stale two years after its read date and must then be re-read.
   - No number computed by you: no conversion, combination, rescaling, or
     range built from several values. Reasoning in words is flagged `[der]`
     and carries no number.
   - A statement whose numbers are not values (notation, names, pointers)
     carries `<!-- num: not a value -->`.
3. **Every identifier you cite has one row in the skill's
   `references/sources.tsv`, and every row is cited.**
4. **Superseded values are kept** in the history section of `results.md`,
   marked as superseded, not deleted.
5. **Forecasts are labelled as forecasts.**
6. **Section keys.** Never write, rename or remove a `<!-- key: ... -->`
   line by hand; `tools/assign_keys.py` adds keys for new sections. A
   section you remove goes to `references/retired-keys.tsv`, because a
   researcher's notes may be attached to it.
7. **Generality.** The package follows the field's own weights: a subject
   is not built around one group, code or dataset, including yours.
8. **Plain technical English**, complete sentences.

The citation format and file layout are in
`skills/observational-cosmology/references/suite-conventions.md`; the full
brief that the package's own research runs follow is `docs/agent-brief.md`,
with `docs/agent-brief-numbers.md` for numbers.

## Checks to run

From the repository root, before opening a pull request:

```bash
python3 tools/assign_keys.py
python3 tools/sync_blocks.py
python3 skills/observational-cosmology/scripts/verify_sources.py skills/<skill>
python3 tools/check_keys.py --against <last release tag>
python3 tools/check_numbers.py --skill <skill> --list
python3 -m unittest discover -s tests
```

`check_numbers.py --list` must print nothing; the test suite requires zero
statements without paper and place in every skill.

## Refreshing a domain

The procedure is in `suite-conventions.md`, "Refreshing a domain".
`python3 tools/refresh_status.py --due 90` lists the files whose snapshot is
older than 90 days and the `[doc]` facts about to go stale.

## Licence

Contributions are accepted under the MIT licence of the package (`LICENSE`).
