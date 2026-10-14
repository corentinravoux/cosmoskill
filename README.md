# cosmoskill

Skills for [Claude Code](https://claude.com/claude-code) that give it a
working, citable knowledge of observational cosmology: one hub skill and
twenty-one domain skills, each built from the literature, with a bibliography
checked against arXiv.

The package holds general knowledge of the field and links every statement to
its source. It is not a database of verified numbers: when a number matters,
the assistant reads it again in the linked paper.

A skill here is a reference, not a tutorial. It is written for an assistant
helping a cosmology researcher review a manuscript, plan an analysis or check
a claim, and it answers three questions for its domain: what is the current
number and where does it come from, what does a referee check, and which
statements that still circulate are out of date.

Version 0.3.0. Snapshot of the literature: October 2026.

## What is in it

```
cosmoskill/
├── skills/
│   ├── observational-cosmology/   hub: which skill holds what, review rubric,
│   │   ├── references/            conventions, cross-probe digest
│   │   └── scripts/               fetch_paper.py, layers.py, verify_sources.py
│   └── cosmo-<domain>/            21 domain skills, same shape each
│       ├── SKILL.md               when to use, file map, core facts, checklists
│       └── references/
│           ├── physics-and-methods.md
│           ├── surveys-and-data.md
│           ├── results.md
│           ├── systematics.md
│           ├── open-questions.md
│           └── sources.tsv        the bibliography, machine-checked
├── docs/                          specification, roadmap, agent brief, history
├── tools/                         upkeep: section keys, level blocks
├── tests/
└── .claude-plugin/                plugin and marketplace manifests
```

| Skill | Domain | Sources |
|---|---|---|
| `observational-cosmology` | hub and router; conventions; cross-probe digest | 25 |
| `cosmo-cmb` | CMB spectra and lensing, Planck / ACT / SPT, τ, A_L | 91 |
| `cosmo-galaxy-clustering` | BAO, RSD, full shape, DESI DR1/DR2 | 126 |
| `cosmo-lyman-alpha` | Lyα BAO and AP, P1D, tomography, IGM | 172 |
| `cosmo-weak-lensing` | cosmic shear, 3×2pt, S8 | 192 |
| `cosmo-supernovae` | SN Ia Hubble diagram and compilations | 109 |
| `cosmo-distance-ladder-h0` | H0: ladder, masers, time delays, inverse ladder | 103 |
| `cosmo-peculiar-velocities` | velocity surveys and estimators, fσ8 at low redshift, bulk flows | 150 |
| `cosmo-clusters` | cluster counts and mass calibration | 100 |
| `cosmo-cmb-lss-cross-correlations` | CMB lensing × LSS, kSZ, tSZ, ISW | 101 |
| `cosmo-beyond-two-point` | bispectrum, voids, field-level inference, SBI | 120 |
| `cosmo-dark-energy-modified-gravity` | w0wa evidence and critiques, μ–Σ, E_G | 99 |
| `cosmo-neutrinos-dark-matter` | Σmν, N_eff, warm / fuzzy / interacting dark matter | 101 |
| `cosmo-inflation-primordial` | n_s, r, f_NL, curvature, birefringence | 100 |
| `cosmo-tensions-anomalies` | cross-probe synthesis: H0, S8, dipole, CMB anomalies | 100 |
| `cosmo-surveys-facilities` | instruments, releases, dates, status | 102 |
| `cosmo-statistics-inference` | covariance, blinding, priors, tension metrics, SBI | 100 |
| `cosmo-simulations-mocks` | N-body, hydro, fast mocks, emulators, constrained simulations | 100 |
| `cosmo-reionization-21cm` | reionisation history, 21 cm, intensity mapping | 101 |
| `cosmo-multimessenger` | standard sirens, FRBs, lensed transients | 125 |
| `cosmo-software-ecosystem` | codes, their units, defaults and status | 100 |
| `cosmo-theory-foundations` | definitions and formulae with the paper fixing each | 100 |

2,417 bibliography rows and about 400,000 words of reference in total.

## How the content is grounded

Every skill follows one contract, set out in
`skills/observational-cosmology/references/suite-conventions.md` and
`docs/agent-brief.md`:

- Prose cites `arXiv:<id>` or `doi:<doi>`. Every cited identifier has one row
  in the skill's `sources.tsv`, and every row is cited.
- Every number carries a flag: `[src]` read in the cited paper when the file
  was written, `[sec]` taken from a named secondary source, `[der]` derived,
  with the derivation stated.
- `results.md` and `surveys-and-data.md` carry a snapshot date. Superseded
  values stay in a history section, marked as superseded.
- Forecasts are labelled as forecasts.

The checker verifies the first point mechanically. It asks the arXiv API for
every identifier and compares title and first author with the row, and it
reports citations without a row and rows without a citation.

```bash
S=skills/observational-cosmology/scripts
python3 $S/verify_sources.py skills/cosmo-lyman-alpha
python3 $S/verify_sources.py skills/*/                 # all of them
python3 $S/verify_sources.py --offline skills/*/       # no network
python3 $S/fetch_paper.py 2503.14739 --abstract        # read what a paper says
python3 $S/fetch_paper.py 2503.14739 --grep "8.632"    # find a number in its body
```

## Levels

Every skill answers at the depth the question calls for, and says which:

| Level | Read | For |
|---|---|---|
| L1 | the skill's `SKILL.md` | what a domain is, where it stands, what to watch for |
| L2 | one reference file | a value, its source, a referee point |
| L3 | a specialist dossier | how a result is obtained, which method to choose (none written yet) |
| L4 | the cited paper | a number about to enter a manuscript |

The rule is to answer at the lowest level that answers, and to end with a
line such as `[cosmoskill L2 · base · cosmo-cmb/results#optical-depth]`. The
last part is a section key: every section of every file carries one, as a
comment under its heading, and keeps it when the heading is reworded.

## Refining it for your own work

The package is a base layer. You add to it without editing it, in a personal
layer (`~/.cosmoskill/`) or a project layer (`.cosmoskill/` in a project): a
profile saying which domains are yours and which conventions you use, notes
attached to sections of the package by their key, your own papers, and your
own dossiers on the subjects you know in depth. The skills read these layers
and say when an answer draws on them. `docs/layers.md` explains the format.

```bash
L=skills/observational-cosmology/scripts/layers.py
python3 $L init
python3 $L note cosmo-lyman-alpha results#cosmology-from-p1d "quote the mean-flux prior with the value"
python3 $L source cosmo-lyman-alpha <arXiv id> --role method    # row taken from arXiv
python3 $L dossier cosmo-lyman-alpha qmle-window                # template to fill
python3 $L check                                                # after updating the package
```

In a conversation the assistant runs these for you: "note for my Lyα work
that ...", "add this paper to my layer".

## What to trust, and how far

The skills were written by Claude research agents in October 2026, one domain
at a time, under the rule that nothing is written from model memory. Each was
then gated by a coordinating session: the checker rerun, and five to eight
quoted numbers compared with the arXiv abstract. `docs/history/tests/gate-log.md`
records every gate, including the mismatches found and corrected and the
claims that were not checked. Three rounds of testing compared answers given
from memory alone with answers given from the skill files alone
(`docs/history/tests/baseline-grading*.md`).

That leaves limits a user should know:

- The bibliography is verified. The numbers are verified by sample, not
  exhaustively. A number flagged `[src]` was read by an agent in the paper;
  re-read the paper before the number enters a manuscript.
- Many numbers are abstract-level. Values that sit in a paper's body are
  flagged as such in the gate log where they were not re-read.
- Dates and status lines of facilities often rest on official web pages,
  flagged `[sec: web]`.
- Each file lists what its author could not verify under "Not verified".
  Those lists are part of the content.
- The snapshot is October 2026. This field moves monthly.

Limits of this version in particular:

- No specialist dossier (L3) is written yet: below the paper itself, the
  deepest material is the reference files.
- Depth is uneven across domains: 91 to 192 sources, for no principled
  reason. The first version was built for one researcher, and the domains
  nearest to that researcher's work are the deepest.
- Classic references are often missing: the first build searched recent
  work first.
- Domains without a skill: instrument and data pipelines, photometry and
  photometric redshifts, the cosmic web, big-bang nucleosynthesis, the
  galaxy–halo connection, early-universe exotica, machine-learning methods.
- A local layer adds notes, papers and dossiers. It cannot replace a value
  of the package, and nothing in it is promoted to the package.

`docs/specs/` and `docs/plans/` hold the specification and the roadmap that
address these.

## Installing

Three routes. Use one only: two routes at once list every skill twice.

**A. As a plugin, from the marketplace in this repository.** In Claude Code:

```
/plugin marketplace add corentinravoux/cosmoskill
/plugin install cosmoskill@cosmoskill
```

Update later with `claude plugin update cosmoskill@cosmoskill`. Skills are
then named with the plugin prefix: `cosmoskill:cosmo-lyman-alpha`.

**B. As a clone inside the skills directory.**

```bash
git clone https://github.com/corentinravoux/cosmoskill ~/.claude/skills/cosmoskill
```

Update with `git pull`. Names carry the same prefix as in route A.

**C. As linked directories.** Clone anywhere, then link each skill:

```bash
git clone https://github.com/corentinravoux/cosmoskill
for d in cosmoskill/skills/*/; do
    ln -s "$(realpath "$d")" ~/.claude/skills/"$(basename "$d")"
done
```

Update with `git pull`. Names are plain: `cosmo-lyman-alpha`.

The scripts need Python 3.9 or later and nothing outside the standard
library.

## Keeping it current

`skills/observational-cosmology/references/suite-conventions.md` gives the
procedure for refreshing a domain and for adding one. In short: find what
appeared since the snapshot date, read it at source, add the result and move
the superseded value to the history, add the bibliography rows, bump the
date, run the checker. Never refresh from memory.

## Updating

The skills are meant to be refreshed every few months. The cycle is written
out step by step in
`skills/observational-cosmology/references/suite-conventions.md`, and asking
the assistant to update a domain loads it. After editing a skill:

```bash
python3 tools/assign_keys.py     # give new sections their key
python3 tools/sync_blocks.py     # regenerate the level block of each SKILL.md
python3 skills/observational-cosmology/scripts/verify_sources.py skills/cosmo-<domain>
python3 tools/check_keys.py --against <last release tag or commit>
python3 -m unittest discover -s tests
```

## Licence

MIT, for the text and for the scripts. See `LICENSE`.
