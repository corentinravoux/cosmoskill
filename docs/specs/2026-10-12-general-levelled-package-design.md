# cosmoskill 2 — a general, levelled, refinable package: design

Date: 2026-10-12. Status: design agreed in conversation in its direction;
this document is the written form for review. Nothing described here is built.

## 1. Where the package stands

`cosmoskill` holds one hub skill and 21 domain skills of observational
cosmology, 2,382 cited works, built in October 2026 by research agents under
a "nothing from memory" contract (`docs/design.md`, `docs/agent-brief.md`,
`docs/tests/gate-log.md`). It was built for one person on one machine. Known
limits, all measured or logged:

- 40 skill files carry machine paths or references to the author's tools,
  notes and packages.
- Depth is uneven: 91 to 192 sources per domain, the deepest being the
  first builder's fields, because agents were told so.
- A flat cap of 100 sources cut verified content in several domains.
- Numbers are verified by sample. Many are abstract-level.
- Classic references are often missing: agents searched 2025–2026 first.
- Domains absent: instrument and data pipeline, photometry and photo-z,
  cosmic web, BBN, galaxy–halo connection, early-universe exotica,
  machine-learning methods.
- Every question in a domain gets the same material, whatever its depth.

## 2. New aims (author, October 2026)

1. **General.** Useful to any cosmology researcher. No tailoring to one
   person's bibliography, papers or tools.
2. **Levelled.** The package answers at the depth the question calls for.
3. **Refinable.** A researcher takes the general base and refines it for
   their own research, without forking the base and without losing the
   ability to update it.

## 3. Non-goals

- Not a textbook and not a course. The reader is a researcher.
- No machine-readable data compilations in the base (they belong to data
  packages with their own tests; the base may cite them as external
  resources).
- No private or collaboration-internal knowledge in the base, ever.
- No answer-writing for manuscripts; the package informs, the researcher
  writes.

## 4. Levels

| Level | Content | Typical cost | Reader's situation |
|---|---|---|---|
| L1 Orient | the 10–15 facts and traps of a domain | 1–2k tokens | outside the field, or a first pass |
| L2 Reference | dated tables, systematics, open questions | 7–17k per file | checking a claim, a value, a referee point |
| L3 Specialist | one dossier per subtopic: derivations, body-level numbers, method variants, reading list | 5–15k per dossier | working inside the field |
| L4 Source | the cited paper's section, fetched on demand | paper-dependent | a number entering a manuscript; two files disagreeing |

Rules, held by the hub and repeated in one fixed block in every skill:

- Choose the level from the question; start at the lowest that can answer;
  escalate when it cannot.
- L4 is mandatory before a number is endorsed for a manuscript.
- Every answer states the level it was given at and the layer it came from
  (section 5).
- L1 and L2 exist today (`SKILL.md`, the five reference files). L3 is new.
  L4 exists as tooling only (`verify_sources.py`, `fetch_abstracts.py`).

L3 subtopics are taken from a neutral source: the section structure of the
domain's recent reviews and the working-group structure of its
collaborations, never from one researcher's interests. L3 depth is even
across domains by rule, not by taste.

## 5. Layers: base, personal, project

Three layers with the same file contract:

| Layer | Location | Owner | Updated by |
|---|---|---|---|
| base | the installed package | the maintainers | package update; changes by contribution |
| personal | `~/.cosmoskill/` | one researcher | that researcher, with the refine workflow |
| project | `<project>/.cosmoskill/` | one project (a paper, a proposal) | its authors |

Resolution order: project, then personal, then base. Layers **add** by
default. A layer overrides a base entry only by naming its key and giving a
reason; the base file is never edited in place.

```
~/.cosmoskill/
├── profile.md               field(s), default level per domain, unit and
│                            fiducial conventions, collaborations, own papers
├── <skill>/
│   ├── notes.md             refinements, keyed by the base section they attach to
│   ├── deep/<subtopic>.md   personal L3 dossiers
│   ├── claims.tsv           added or overriding claims, base schema
│   └── sources.tsv          added sources, base schema, same checker
└── private/                 never promoted, never shared
```

How a skill finds the layers: a fixed "Local layers" block at the end of
every `SKILL.md` tells the assistant to run one command,
`scripts/layers.py <skill>`, which prints the layer files that exist for that
skill and the profile's settings for it. No harness feature is assumed beyond
a skill being able to ask for a command to be run. Whether the harness offers
something better (dynamic context in a skill file, a plugin data directory, a
per-project skill directory with precedence) is a fact to verify in the
Claude Code documentation before the mechanism is fixed.

Workflows shipped with the package, as one skill `cosmoskill-refine`:

- **profile**: create or edit `profile.md`.
- **add**: a paper, a claim, a note — read at source, checked by the same
  checker, written to the personal or project layer.
- **deepen**: write a personal L3 dossier on a subtopic.
- **correct**: record a disagreement with a base entry, with its source.
- **sync**: after a base update, report personal entries the base now
  covers, contradicts or has superseded.
- **promote**: turn public-literature entries of a personal layer into a
  contribution to the base. Entries under `private/` and entries without a
  public source cannot be promoted.

This is also where one researcher's own bibliography belongs: in their
personal layer, not in the base.

## 6. Contract, version 2

Changes to the per-skill contract that the levels and layers need:

- **Stable keys.** Every section that a layer may attach to, and every
  claim, has a key that survives edits.
- **Claims table.** `references/claims.tsv`, one row per quoted number:
  key, quantity, value, uncertainty, model, data set, source id, location in
  the source (abstract, section, table, equation), verification grade, date
  read, status (current, superseded by key).
- **Verification grade**, visible to the reader: A re-read in a table or
  equation of the source; B read in the body; C read in the abstract;
  D secondary source or web page; U unverified note (personal layers only).
- **Sources.** Same `sources.tsv`; the flat cap is replaced by a budget per
  subtopic; a "foundations" role is filled by rule for every domain.
- **Levels on disk.** `SKILL.md` (L1), `references/*.md` (L2),
  `deep/<subtopic>.md` (L3), `references/claims.tsv` and `sources.tsv`
  (the hooks for L4).
- **No machine-specific content.** Relative links only; no absolute paths;
  no reference to one person's tools except as cited public software.

Tooling grows with the contract: the checker validates keys, the claims
table and grades; a second script resolves layers; a third reports what a
base update does to a personal layer.

## 7. Distribution and trust

- Installable by anyone: plugin manifest and marketplace entry, and the plain
  directory-link route, both documented and tested on a clean account.
- A licence for the text and one for the scripts (to be chosen by the author).
- Continuous checking on the public repository: the checker on every push.
- Versioned releases with a snapshot date and a changelog of superseded
  values.
- A contribution guide and an error-report template: an error in a number is
  reported with the source that contradicts it.
- A refresh procedure that needs no private tooling.

## 8. Phases

Each phase is its own specification, plan and implementation cycle. Order:

1. **Generalise what exists.** No new research. Remove personal and
   machine-specific content; fold the hub's two peculiar-velocity files into
   the domain skill; installable by anyone; checker in continuous
   integration; licence. Acceptance: fresh clone on a clean account, every
   skill loads, checker passes, no personal string left.
2. **Level router and layers v0.** Level rules in the hub, the fixed block
   in every skill, a level map per skill; `profile.md` and `notes.md` only,
   with `layers.py`. Acceptance: question sets written from several
   sub-fields' points of view land on the right level at the expected cost;
   a note in a personal layer is found and labelled.
3. **Contract version 2 and even L2.** Keys, claims table, grades; uniform
   source rule; foundations pass; body-level re-read of headline numbers;
   per-subtopic budgets. Acceptance: every headline number has a claims row
   with a grade; source counts per domain within a set band.
4. **L3 pilot.** Two domains of different kind, one probe and one method.
   Acceptance: specialist question set answered from the dossiers; a
   researcher of that field finds no textbook-level filler.
5. **Layers v1 and the refine workflows.** Structured personal and project
   layers; add, deepen, correct, sync, promote. Acceptance: a refinement
   survives a base update; a conflict is reported; a private entry cannot be
   promoted.
6. **Coverage.** The missing domains; L3 for the remaining domains.
7. **Release.** Version 1.0 of the general package: changelog, contribution
   guide, refresh procedure, announcement material.

Layers come in two steps on purpose. The free-text step (phase 2) needs no
schema and gives personal refinement early. The structured step (phase 5)
depends on the keys and the claims table of phase 3: an overlay cannot attach
to entries that have no stable name.

## 9. Constraints carried over

- Nothing from model memory; every number read at source; provenance visible.
- One research agent at a time; hard budgets in each brief; checkpoint to
  disk; after a cut, a fresh agent resumes from the files. Before relaunching,
  check that no agent is alive in the directory.
- Caps stop additions; they never delete verified content.
- No commit or push without the author's request.

## 10. Decisions

Taken by the maintainer on 2026-10-12:

- Licence: MIT, for the text and for the scripts.
- Name: `cosmoskill`, kept for the general release.
- The pointer to an external fσ8 data package is dropped; the base stays
  general.

Open:

- Pilot domains for L3. Proposed: `cosmo-galaxy-clustering` (probe) and
  `cosmo-statistics-inference` (method).

## 11. Revisions proposed by the planning pass (2026-10-12, for review)

The planner checked the Claude Code documentation and the repository. Its
roadmap is `docs/plans/2026-10-12-cosmoskill2-roadmap.md`. It proposes these
changes to the sections above; none is applied to them yet.

1. **Section 1, correction.** Content tied to one person or machine sits in
   20 skill files (37 lines), not 40: most "the author" matches mean a
   paper's authors. The software skill's provenance vocabulary ("installed",
   "checkout") is environment-bound and needs redefining.
2. **Section 5, layers are data, not skills.** The harness gives no
   "project, then personal, then base" precedence between skills of the same
   name, and plugin skills are namespaced (`cosmoskill:cosmo-cmb`). The
   resolver script stays the mechanism.
3. **Section 5, no load-time command in domain skills.** A skill file can
   inject command output when it loads, but a failing or unapproved command
   aborts the skill. The "Local layers" block stays an instruction,
   conditional on a layer directory existing.
4. **Sections 5 and 6, paths.** `SKILL.md` refers to its own directory with
   `${CLAUDE_SKILL_DIR}`; scripts stay under the hub skill, the one place
   reachable under every install route; the root `scripts` symlink goes.
5. **Section 5, location.** Personal layer at `$COSMOSKILL_HOME`, default
   `~/.cosmoskill`; not the plugin data directory, which is deleted on
   uninstall.
6. **Section 7, three install routes** (marketplace plugin, clone into the
   skills directory, per-skill links), one at a time; names differ between
   routes. A `version` in the manifest pins users until it changes.
7. **Section 4, routing.** The listing drops descriptions beyond a budget, so
   descriptions cannot be the only router; the hub carries the level rules.
   `SKILL.md` plus the fixed block must stay under 5,000 tokens.
8. **Section 8, section keys move to phase 2.** A free-text note attached to
   a heading would be orphaned when keys arrive in phase 3.
9. **Section 8, subtopic lists belong to phase 3**, and the L3 pilot domains
   go first inside phase 3, so phase 4 does not wait for the other 19.
10. **Section 8, phase 6 splits**: 6a the missing domains, before release
    1.0; 6b L3 for all remaining domains, after it.
11. **Section 6, underspecified**: claims schema (asymmetric errors, limits,
    units, arXiv version read, who verified), mapping from flags to grades,
    who mints keys and how a rename is recorded, how an override is shown,
    how a conflict is detected after a base update, and a public tool for L4
    beyond abstracts.
