# cosmoskill

Skills for [Claude Code](https://claude.com/claude-code) and the Claude app that give it a
working, citable knowledge of observational cosmology: one hub skill and
twenty-eight domain skills, each built from the literature, with a bibliography
checked against arXiv.

The package holds general knowledge of the field and links every statement to
its source. It is not a database of verified numbers: when a number matters,
the assistant reads it again in the linked paper.

A skill here is a reference, not a tutorial. It is written for an assistant
helping a cosmology researcher review a manuscript, plan an analysis or check
a claim, and it answers three questions for its domain: what is the current
number and where does it come from, what does a referee check, and which
statements that still circulate are out of date.

Version 1.0.0 (`CHANGELOG.md`). Snapshot of the literature: 26 October 2026
for the results and survey files of every skill; the other reference files
and the dossiers carry their own dates (October 2026).

## What is in it

```
cosmoskill/
├── skills/
│   ├── observational-cosmology/   hub: which skill holds what, review rubric,
│   │   ├── references/            conventions, cross-probe digest
│   │   └── scripts/               fetch_paper.py, verify_sources.py; layers.py,
│   │                              sync_layers.py, promote.py for local layers
│   ├── cosmoskill-refine/         workflow skill: refine the package in a layer
│   └── cosmo-<domain>/            28 domain skills, same shape each
│       ├── SKILL.md               when to use, file map, core facts, checklists
│       └── references/
│           ├── physics-and-methods.md
│           ├── surveys-and-data.md
│           ├── results.md
│           ├── systematics.md
│           ├── open-questions.md
│           ├── sources.tsv        the bibliography, machine-checked
│           └── subtopics.tsv      subtopics and their source
│       └── deep/                  level-3 dossiers, six per domain
├── docs/                          specification, roadmap, agent brief, history
├── tools/                         upkeep: section keys, level blocks, numbers checker,
│                                  refresh status, release manifest
├── tests/
└── .claude-plugin/                plugin and marketplace manifests
```

| Skill | Domain | Sources | Dossiers |
|---|---|---|---|
| `observational-cosmology` | hub and router; conventions; cross-probe digest | 107 |  |
| `cosmo-cmb` | CMB spectra and lensing, Planck / ACT / SPT, τ, A_L | 153 | 6 |
| `cosmo-galaxy-clustering` | BAO, RSD, full shape, DESI DR1/DR2 | 192 | 6 |
| `cosmo-lyman-alpha` | Lyα BAO and AP, P1D, tomography, IGM | 214 | 6 |
| `cosmo-weak-lensing` | cosmic shear, 3×2pt, S8 | 243 | 6 |
| `cosmo-supernovae` | SN Ia Hubble diagram and compilations | 182 | 6 |
| `cosmo-distance-ladder-h0` | H0: ladder, masers, time delays, inverse ladder | 209 | 6 |
| `cosmo-peculiar-velocities` | velocity surveys and estimators, fσ8 at low redshift, bulk flows | 173 | 6 |
| `cosmo-clusters` | cluster counts and mass calibration | 169 | 6 |
| `cosmo-cmb-lss-cross-correlations` | CMB lensing × LSS, kSZ, tSZ, ISW | 215 | 6 |
| `cosmo-beyond-two-point` | bispectrum, voids, field-level inference, SBI | 264 | 6 |
| `cosmo-dark-energy-modified-gravity` | w0wa evidence and critiques, μ–Σ, E_G | 168 | 6 |
| `cosmo-neutrinos-dark-matter` | Σmν, N_eff, warm / fuzzy / interacting dark matter | 199 | 6 |
| `cosmo-inflation-primordial` | n_s, r, f_NL, curvature, birefringence | 164 | 6 |
| `cosmo-tensions-anomalies` | cross-probe synthesis: H0, S8, dipole, CMB anomalies | 228 | 6 |
| `cosmo-surveys-facilities` | instruments, releases, dates, status | 159 | 6 |
| `cosmo-statistics-inference` | covariance, blinding, priors, tension metrics, SBI | 142 | 6 |
| `cosmo-simulations-mocks` | N-body, hydro, fast mocks, emulators, constrained simulations | 264 | 6 |
| `cosmo-reionization-21cm` | reionisation history, 21 cm, intensity mapping | 227 | 6 |
| `cosmo-multimessenger` | standard sirens, FRBs, lensed transients | 179 | 6 |
| `cosmo-software-ecosystem` | codes, their units, defaults and status | 132 | 6 |
| `cosmo-theory-foundations` | definitions and formulae with the paper fixing each | 137 | 6 |
| `cosmo-photometry-photoz` | photometric calibration, photo-z, n(z) calibration | 150 | 6 |
| `cosmo-galaxy-halo-connection` | HOD, SHAM, stellar-to-halo mass, assembly bias, halo model | 162 | 6 |
| `cosmo-data-pipelines` | spectroscopic, imaging and CMB pipelines; masks, randoms, validation | 129 | 6 |
| `cosmo-bbn` | primordial abundances, nuclear rates, BBN codes, Ω_b h² prior | 104 | 6 |
| `cosmo-machine-learning` | emulators, neural compression, SBI, generative models, robustness | 140 | 6 |
| `cosmo-cosmic-web` | web classification, filaments, environment, filament gas, protoclusters | 126 | 6 |
| `cosmo-early-universe-exotica` | PTA background, PBHs, defects, EDE, spectral distortions | 131 | 6 |

5,062 bibliography rows and about 1,370,000 words of reference in total; 168 specialist dossiers (level 3), six in each domain skill.

## How the content is grounded

Every skill follows one contract, set out in
`skills/observational-cosmology/references/suite-conventions.md` and
`docs/agent-brief.md`:

- Prose cites `arXiv:<id>` or `doi:<doi>`. Every cited identifier has one row
  in the skill's `sources.tsv`, and every row is cited.
- Only numbers read in a paper are given (owner, 2026-10-23): every number
  names its paper and the place it was read, `[src: Sect. 4.2]` in the cited
  paper itself, `[sec: <place>]` in a named secondary source. No number is
  computed by an agent; `[der]` marks reasoning in words and carries no
  number. Two exceptions (owner, 2026-10-26): a code fact or a fact from an
  official page carries `[doc: <URL, path or installed package>, <date
  read>]`, and a statement whose numbers are names or notation carries
  `<!-- num: not a value -->`. `tools/check_numbers.py` lists the numbers
  that do not comply, and the `[doc]` facts by read date; a `[doc]` fact
  read more than two years ago fails until it is re-read.
- `results.md` and `surveys-and-data.md` carry a snapshot date. Superseded
  values stay in a history section, marked as superseded.
- Forecasts are labelled as forecasts.

The checker verifies the first point mechanically. It asks the arXiv API for
every identifier and compares title and first author with the row, and it
reports citations without a row and rows without a citation.

```bash
S=skills/observational-cosmology/scripts
python3 $S/verify_sources.py skills/cosmo-cmb
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
| L3 | a dossier of `deep/` (six per domain skill) | how a result is obtained, which method to choose |
| L4 | the cited paper | a number about to enter a manuscript |

The rule is to answer at the lowest level that answers, and to end with a
line such as `[cosmoskill L2 · base · cosmo-cmb/results#optical-depth]`. The
last part is a section key: every section of every file carries one, as a
comment under its heading, and keeps it when the heading is reworded.

## Refining it for your own work

The package is a base layer. You add to it without editing it, in a personal
layer (`~/.cosmoskill/`) or a project layer (`.cosmoskill/` in a project): a
profile saying which domains are yours and which conventions you use, notes
attached to sections of the package by their key, overrides and suppressions
of a section for you alone, your own papers, and your own dossiers on the
subjects you know in depth. The skills read these layers and say when an
answer draws on them; an override is always quoted beside the package's
value. `docs/layers.md` explains the format, `docs/layers-v1.md` specifies it.

```bash
S=skills/observational-cosmology/scripts
python3 $S/layers.py init
python3 $S/layers.py note cosmo-weak-lensing results#the-cmb-reference-values "quote S8 differences against both CMB references"
python3 $S/layers.py override cosmo-cmb results#optical-depth-tau "our baseline is the low-ell reanalysis value"
python3 $S/layers.py source cosmo-supernovae <arXiv id> --role method   # row taken from arXiv
python3 $S/layers.py dossier cosmo-clusters richness-mass-calibration   # template to fill
python3 $S/layers.py resolve cosmo-cmb results#optical-depth-tau        # base and entries, labelled
python3 $S/sync_layers.py                                               # after updating the package
```

`sync_layers.py` reports every entry whose section changed, moved or was
retired since the entry was written, and exits 3 when that entry is an
override. In a conversation the `cosmoskill-refine` skill runs these for
you: "note, for my cluster work, that ...", "add this paper to my layer",
"for me, use this value instead". The package's owner moves an entry into
the package with `promote.py`, which prepares the change in the working
tree and never commits.

## What to trust, and how far

The skills were written by Claude research agents in October 2026, one domain
at a time, under the rule that nothing is written from model memory. Each run
was then gated by a coordinating session: the checkers rerun, and statements
compared with the paper or page they cite. `docs/history/tests/gate-log.md`
records every gate, including the mismatches found and corrected and the
claims that were not checked. Three rounds of testing compared answers given
from memory alone with answers given from the skill files alone
(`docs/history/tests/baseline-grading*.md`).

That leaves limits a user should know:

- The bibliography is verified against arXiv. Every number names its paper
  and the place it was read, and the checker enforces that mechanically;
  whether the value at that place is the one quoted was compared by sample at
  each gate, not exhaustively. Re-read the paper before a number enters a
  manuscript.
- Many places are the abstract; body places (section, table, equation) are
  given where the value sits in the body.
- Code facts and facility dates rest on official pages and installed
  packages, flagged `[doc: <page>, <date read>]`; they are re-read at least
  every two years.
- Each file lists what its author could not verify under "Not verified".
  Those lists are part of the content.
- The snapshot is October 2026. This field moves monthly.

Limits of this version in particular:

- Every domain skill has six specialist dossiers (L3), on the subtopics
  where its reference files answered fewest practitioner questions (two
  rounds of gap audit) (the gap
  audit is recorded per domain in `docs/history/tests/gate-log.md`). The
  other subtopics have no dossier: there the deepest material below the
  paper is the reference files. The pilot test found that a dossier helps
  only where the reference files do not already answer
  (`docs/history/tests/levels/run-2026-10-16-l3-pilot.md`).
- Depth is still uneven: 104 to 264 sources per domain. Every domain now
  cites paper bodies (sections, tables, equations) and its classic
  references, but the share of body-level statements varies.
- Numbers were compared with their papers by sample at each gate
  (`docs/history/tests/gate-log.md`), not exhaustively. A few sampled
  statements could not be located at source and are logged as unconfirmed.
- A local layer adds notes, papers and dossiers, and may override or hide a
  section for its researcher only. It does not change the package: an
  override is quoted beside the package's value, and nothing reaches the
  package unless its owner promotes and commits it.
- Out of scope: searches for dark-matter particles by direct or indirect
  detection and at colliders, and high-energy particle astrophysics (cosmic
  rays, neutrino telescopes). Dark matter is treated through its
  cosmological effects only (`cosmo-neutrinos-dark-matter`); laboratory
  neutrino-mass limits appear where cosmology is compared with them.

`docs/specs/` holds the specification; the release plan is
`docs/plans/2026-10-26-release-1.0.md`. A benchmark with outside questions,
graded by people, is planned for a later release; the level tests in
`docs/history/tests/levels/` are self-tests, not evidence of quality.

## Installing

Four routes: A to C for Claude Code, D for the Claude app. Use one only per
account: two routes at once list every skill twice.

**A. As a plugin, from the marketplace in this repository.** In Claude Code:

```
/plugin marketplace add corentinravoux/cosmoskill
/plugin install cosmoskill@cosmoskill
```

Update later with `claude plugin update cosmoskill@cosmoskill`. Skills are
then named with the plugin prefix: `cosmoskill:cosmo-cmb`.

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

Update with `git pull`. Names are plain: `cosmo-cmb`.

**D. In the Claude app (web, Desktop, Cowork), on a paid plan.** Personnaliser
(Customize) → Plugins → Ajouter (Add) → Ajouter une place de marché (Add
marketplace) → Ajouter à partir d'un référentiel (Add from a repository), enter
`corentinravoux/cosmoskill`, then install `cosmoskill`. Skills need code
execution: Paramètres → Capacités → « Créer et modifier des fichiers »
(Settings → Capabilities → Create and edit files). On a Team or Enterprise
account the owner enables it, under Organization settings → Plugins & skills →
Policy.

What differs in the app:

- **L4.** The app's sandbox cannot reach arXiv by default, so `fetch_paper.py`
  stops at once. Either turn on web search in the chat, and Claude reads
  `arxiv.org/abs/<id>` itself, or have `arxiv.org`, `export.arxiv.org` and
  `ar5iv.labs.arxiv.org` added to the allowed domains, and the script works.
  With neither, the skills answer at L1 to L3 and say when L4 was required.
- **No layers.** The sandbox starts empty in every chat, so personal and
  project layers and `cosmoskill-refine` work in Claude Code only.

Both hosts on one account: Claude Code 2.1.273 and later also loads the
plugins of the Claude account it is signed in with. Use route D or route A,
not both; or keep route A and set `"syncClaudeAiSkills": false` in Claude
Code's settings.

The scripts need Python 3.9 or later and nothing outside the standard
library.

## Keeping it current

`skills/observational-cosmology/references/suite-conventions.md` gives the
procedure for refreshing a domain and for adding one. In short: find what
appeared since the snapshot date, read it at source, add the result and move
the superseded value to the history, add the bibliography rows, bump the
date, run the checker. Never refresh from memory.
`python3 tools/refresh_status.py --due 90` lists what a refresh should cover:
files older than 90 days and `[doc]` facts about to go stale. Contributions
follow `CONTRIBUTING.md`.

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
python3 tools/check_numbers.py --skill cosmo-<domain> --list   # must print nothing
python3 -m unittest discover -s tests
```

At a release, `python3 tools/make_release_manifest.py --from <last release>
--version <new>` writes `releases/<new>.tsv`: the section keys added,
changed, moved or retired, which tells a researcher what `sync_layers.py`
will report on their layer.

## Licence

MIT, for the text and for the scripts. See `LICENSE`.
