# Contract, version 2 — draft for review

Date: 2026-10-12. Status: **not adopted in this form**, by the maintainer's
decision of the same day.

The decision: the package holds general knowledge of the field and links
every statement to its source. It is not a database of verified numbers.
When a specific number is needed, the assistant goes back to the linked
paper and reads it there. Sections 2, 3, 4 and 7 below (the claims table,
the verification grades, claim keys and their checks) are therefore dropped:
they would cost most of the research budget of phase 3 to do what a reading
of the paper does better at the moment the number is needed.

What stays from this draft: the subtopic list and its neutral selection rule
(section 5), the source rule that replaces the flat cap (section 6), and the
tool for level 4 (section 9), which becomes the important one, since level 4
is now the only verification the package relies on. Section 8 reduces to
notes and added sources in local layers; overrides of claims have nothing to
attach to.

The text below is kept as the record of what was considered.

What exists already (phase 2): every section of every skill file has a
frozen key, written as a comment under its heading, and a registry of
retired keys per skill (`references/retired-keys.tsv`).

## 1. Why a claims table

Today a number lives in prose or in a Markdown table, with a flag (`[src]`,
`[sec]`, `[der]`) that says how it was obtained but not where in the source
it stands, in which version, or how far it was checked. A reader cannot tell
a value re-read in a table of the paper from one taken from an abstract.

The claims table gives every quoted number one row with that information.
It is not a data product: values stay as printed strings, and nothing is
meant to be loaded for analysis. It serves three uses: showing the reader
how far a number was verified, telling the assistant where to look for
level 4, and giving local layers something to attach an override to.

## 2. `references/claims.tsv`

Tab-separated, one header line, one row per number or dated fact.

| Column | Content | Example |
|---|---|---|
| `key` | claim key, unique in the skill, frozen | `desi-dr2-lya-dh-rd` |
| `section` | where the claim is stated: `<file>#<section key>` | `results#bao-and-alcock-paczynski` |
| `quantity` | what is measured, as the paper writes it | `D_H/r_d` |
| `value` | central value and uncertainty exactly as printed | `8.632 ± 0.098 (stat) ± 0.026 (sys)` |
| `kind` | `measurement`, `limit`, `forecast`, `derived`, `count`, `date`, `status` | `measurement` |
| `cl` | confidence level in percent, when the paper states one | `68` |
| `units` | units, empty when dimensionless | |
| `model` | model assumed | `flat ΛCDM template, BAO dilation` |
| `dataset` | data combination | `DESI DR2 Lyα auto + QSO cross` |
| `z_eff` | effective redshift, when one applies | `2.33` |
| `source` | key of the row in `sources.tsv` | `DESI2025LyaBAO` |
| `version` | version of the source that was read | `v2` |
| `locator` | where in the source: `abstract`, `sec:<n>`, `table:<n>`, `eq:<n>`, `fig:<n>`, `web:<url>` | `abstract` |
| `grade` | verification grade, section 3 | `C` |
| `read_on` | date the value was read | `2026-10-08` |
| `verified_by` | `agent`, `machine` or `human` | `agent` |
| `status` | `current` or `superseded` | `current` |
| `superseded_by` | claim key of the value that replaced it | |
| `note` | derivation, caveat, or what the uncertainty includes | |

Rules:

- **One number, one row.** A table of the paper with six distances gives six
  rows, with keys sharing a stem.
- **Printed strings.** Asymmetric errors, statistical and systematic parts
  and one-sided limits are written as the paper prints them. `kind` and `cl`
  say how to read the string.
- **Dated facts** are claims too: `kind` is `date` or `status`, the value is
  the date or the statement, the locator is usually `web:<url>`.
- **Derived values**: `kind` is `derived`, `locator` lists the claim keys it
  is derived from (`der:key1,key2`), `note` gives the derivation and its
  assumption.
- **Superseded values stay**, with `status` and `superseded_by`. The history
  sections of `results.md` are their prose form.
- **Version.** The arXiv version read is recorded because headline values
  have changed between versions of the same paper.
- **Prose cites the claim.** A number in prose or in a Markdown table keeps
  its flag; the row is found by `section` and `quantity`. Siblings that
  quote the same number cite the owning skill's claim key instead of
  restating a value: one number, one owner.

## 3. Grades

| Grade | Means | Typical locator |
|---|---|---|
| A | read in a table or an equation of the source | `table:`, `eq:` |
| B | read in the body text of the source | `sec:` |
| C | read in the abstract | `abstract` |
| D | taken from a secondary source or a web page | another source's key, `web:` |
| U | unverified note; allowed in local layers only | |

- A derived value takes the lowest grade among its inputs.
- From the present flags: `[src]` becomes C unless the file names a section,
  table or equation, in which case B or A; `[sec]` becomes D; `[der]` becomes
  `kind = derived` with the rule above.
- `verified_by = machine` is allowed for grade C only: a script found the
  value verbatim in the abstract. A and B need a reader.
- A grade is about where the number was read, not about whether the paper is
  right.

## 4. Keys

- **Section keys** exist (phase 2). **Claim keys** are minted when a row is
  written, from data set, quantity and qualifier, lower case with hyphens,
  and never change afterwards.
- A key that disappears is recorded in `references/retired-keys.tsv` with
  what replaced it. Continuous integration compares the keys with the last
  release tag and fails on a key lost without an entry. Claim keys use the
  same registry, with `claims` in its `file` column.
- A release publishes a manifest of added, changed, superseded and retired
  keys. Local layers need it to detect what an update did to them.

## 5. Subtopics

`references/subtopics.tsv`, one row per subtopic of the domain:

| Column | Content |
|---|---|
| `key` | subtopic key, frozen; later the name of its L3 dossier |
| `title` | the subtopic |
| `from` | where it comes from: a review (`sources.tsv` key and section) or a collaboration working group (page and date read) |
| `files` | the L2 sections that cover it, as `<file>#<section key>` |
| `status` | `covered`, `thin`, `missing` |

Selection rule, the same for every domain: take the first- and
second-level sections of two reviews of the last five years, add the working
groups of the collaborations active in the domain, merge duplicates, keep
between six and twelve. Every row records its `from`, so that the list can
be audited and is nobody's personal interest.

## 6. Source rule

Replaces the flat cap. For every subtopic, the bibliography holds at least:

- one foundation paper (the one that fixes the definition or the method);
- one review or method paper;
- the latest result of each collaboration active in the subtopic;
- one critique, where a result is disputed.

This is a floor. A domain may hold more, and nothing verified is removed to
meet a number.

## 7. Checks that follow

The checker of version 2 fails when:

- a claims row has no grade, an unknown `kind`, or a `source` absent from
  `sources.tsv`; a grade A row has no `table:` or `eq:` locator; a key is
  repeated; a `superseded_by` names no row;
- a number in a "What an expert holds in mind" bullet of `SKILL.md` has no
  claims row (headline coverage);
- a subtopic row has no `from`, or names a section that does not exist;
- a subtopic does not meet the source rule.

## 8. What local layers will do with it (phase 5, stated here so that the
formats allow it)

- Three operations, kept apart: **add** a claim the base lacks, **override**
  a base claim by its key, **suppress** a base claim for one's own use.
- An override stores the hash of the base row it was written against. After
  a base update, a changed hash is a conflict to review, not something
  applied silently.
- An answer that uses an override shows both values, each labelled with its
  layer.

## 9. Level 4

Level 4 means reading the source at the claim's `locator`. The package ships
`fetch_abstracts.py`, which covers `abstract` only. Version 2 needs a script
that prints one section, table caption or equation neighbourhood of a paper
from its public HTML rendering, given the `source` and `locator` of a claim.
Where no network is available, level 4 is not done and the answer says so:
it does not fall back to the claims table and call that verification.

## 10. Open points for the maintainer

1. Is a string `value` acceptable, or should central value and errors also
   be split into numeric columns? The draft keeps strings, because the
   package is not a data product.
2. Grade threshold for a headline: should every number in a `SKILL.md`
   bullet be at least B before a release, or is C acceptable with the grade
   shown?
3. The pilot domains, which go first in phase 3: proposed
   `cosmo-galaxy-clustering` and `cosmo-statistics-inference`.
