# cosmoskill

**Observational-cosmology skills for Claude: they work in Claude Code and in
the Claude app (web, Desktop, Cowork), from this one repository.**

Ask Claude about a measurement, a survey or a method, and the skills give it
the current values, where each comes from, what a referee checks, and which
statements still in circulation are out of date. Every number names the paper
and the place it was read: when it matters, Claude reads the paper again
rather than trusting the skill.

One hub skill and 28 domain skills · 5,062 sources checked against arXiv ·
168 specialist dossiers · literature snapshot 26 October 2026 · version 1.0.3
(`CHANGELOG.md`).

## Install

The same plugin installs in both hosts. Pick one per Claude account (see
[Both hosts on one account](#both-hosts-on-one-account)).

### In the Claude app

Paid plan (Pro, Max, Team, Enterprise).

1. **Customize → Plugins → Add → Add marketplace → Add from a repository**
   (in French: Personnaliser → Plugins → Ajouter → Ajouter une place de marché
   → Ajouter à partir d'un référentiel).
2. Enter `corentinravoux/cosmoskill`, then install **cosmoskill**.
3. Turn on code execution, which skills need: **Settings → Capabilities →
   Create and edit files** (Paramètres → Capacités → « Créer et modifier des
   fichiers »). On a Team or Enterprise account, the owner turns it on under
   Organization settings → Plugins & skills → Policy.
4. To let Claude read the cited papers (level 4, below), turn on **web search**
   in the chat.

### In Claude Code

```
/plugin marketplace add corentinravoux/cosmoskill
/plugin install cosmoskill@cosmoskill
```

Update with `claude plugin update cosmoskill@cosmoskill`.

<details>
<summary>Without the plugin system: link the skills</summary>

Link each skill (skills named `cosmo-cmb`):

```bash
git clone https://github.com/corentinravoux/cosmoskill
for d in cosmoskill/plugin/skills/*/; do
    ln -s "$(realpath "$d")" ~/.claude/skills/"$(basename "$d")"
done
```

Update with `git pull`. Linked before 1.0.3, when the skills were in
`skills/`? The links break on `git pull`: remove them and run the loop again.
</details>

### In other agents (Codex, Gemini CLI, Cursor, Copilot, …)

The skills follow the open [Agent Skills](https://agentskills.io) format and
install with the [skills](https://skills.sh) command:

```
npx skills add corentinravoux/cosmoskill --skill '*'
```

Install all of them: every domain skill calls the hub's scripts in
`observational-cosmology`. Update with `npx skills update`. Layers and
`cosmoskill-refine` need a persistent home directory.

### What each host can do

| | Claude Code | Claude app |
|---|---|---|
| Skills, reference files, dossiers (levels 1–3) | yes | yes |
| Read the cited paper (level 4) | yes, with `fetch_paper.py` | with web search on; or `fetch_paper.py` if `arxiv.org`, `export.arxiv.org` and `ar5iv.labs.arxiv.org` are allowed domains |
| Personal and project layers, `cosmoskill-refine` | yes | no: the app starts each chat with an empty disk |

Without access to papers, the skills still answer from levels 1 to 3, and say
when a question needed level 4.

### What it runs and contacts

The skills are text; the scripts run only when Claude calls them, use the
Python standard library only, and send arXiv identifiers to arXiv, nothing
else. The full list of hosts and cache paths is in
[`plugin/README.md`](plugin/README.md#what-it-runs-and-contacts).

### Both hosts on one account

Claude Code 2.1.273 and later also loads the plugins of the Claude account it
is signed in with. If you install in the app, do not also install in Claude
Code (every skill would load twice), or set `"syncClaudeAiSkills": false` in
Claude Code's settings.

## How it answers

Claude answers at the shallowest level that answers the question, and says
which one it used:

| Level | Claude reads | Enough for |
|---|---|---|
| L1 | the skill's `SKILL.md` | where a domain stands, the headline values, what to watch for |
| L2 | one reference file | another value, its history, a systematic, a referee point |
| L3 | a dossier in `deep/` | how a result is obtained, which method to choose |
| L4 | the cited paper | a number about to go into a manuscript, a proposal or a referee report |

Each answer ends with a line such as
`[cosmoskill L2 · base · cosmo-cmb/results#optical-depth]`, which points to
the section used.

## What is grounded, and how far to trust it

- **Every number carries its source**: `[src: Sect. 4.2]` when read in the
  cited paper, `[sec: …]` when read in a named secondary source, `[doc: page,
  date]` for a code or facility fact. No number is computed by the model.
  `tools/check_numbers.py` enforces this on every file.
- **Every citation is checked**: `verify_sources.py` compares each arXiv
  identifier's title and first author with arXiv, and flags citations without
  a bibliography row and rows never cited.
- **Values were compared with their papers by sample**, not exhaustively
  (`docs/history/tests/gate-log.md`). Re-read the paper before a number goes
  into a manuscript: that is what L4 is for.
- **Each file lists what could not be verified**, under "Not verified".
- **The field moves monthly**; the snapshot is October 2026.
- **Out of scope**: dark-matter particle searches (direct, indirect,
  colliders) and high-energy particle astrophysics.

The skills were written by Claude research agents in October 2026, never from
model memory, and each domain was gated by a second session. The level tests
in `docs/history/tests/levels/` are self-tests, not evidence of quality; a
benchmark with outside questions graded by people is planned.

## Domains

| Skill | Covers | Sources |
|---|---|---|
| `observational-cosmology` | hub: routes to the others; conventions; cross-probe digest | 107 |
| `cosmo-cmb` | CMB spectra and lensing, Planck / ACT / SPT, τ, A_L | 153 |
| `cosmo-galaxy-clustering` | BAO, RSD, full shape, DESI DR1/DR2 | 192 |
| `cosmo-lyman-alpha` | Lyα BAO and AP, P1D, tomography, IGM | 214 |
| `cosmo-weak-lensing` | cosmic shear, 3×2pt, S8 | 243 |
| `cosmo-supernovae` | SN Ia Hubble diagram and compilations | 182 |
| `cosmo-distance-ladder-h0` | H0: ladder, masers, time delays, inverse ladder | 209 |
| `cosmo-peculiar-velocities` | velocity surveys and estimators, fσ8 at low redshift, bulk flows | 173 |
| `cosmo-clusters` | cluster counts and mass calibration | 169 |
| `cosmo-cmb-lss-cross-correlations` | CMB lensing × LSS, kSZ, tSZ, ISW | 215 |
| `cosmo-beyond-two-point` | bispectrum, voids, field-level inference, SBI | 264 |
| `cosmo-dark-energy-modified-gravity` | w0wa evidence and critiques, μ–Σ, E_G | 168 |
| `cosmo-neutrinos-dark-matter` | Σmν, N_eff, warm / fuzzy / interacting dark matter | 199 |
| `cosmo-inflation-primordial` | n_s, r, f_NL, curvature, birefringence | 164 |
| `cosmo-tensions-anomalies` | cross-probe synthesis: H0, S8, dipole, CMB anomalies | 228 |
| `cosmo-surveys-facilities` | instruments, releases, dates, status | 159 |
| `cosmo-statistics-inference` | covariance, blinding, priors, tension metrics, SBI | 142 |
| `cosmo-simulations-mocks` | N-body, hydro, fast mocks, emulators, constrained simulations | 264 |
| `cosmo-reionization-21cm` | reionisation history, 21 cm, intensity mapping | 227 |
| `cosmo-multimessenger` | standard sirens, FRBs, lensed transients | 179 |
| `cosmo-software-ecosystem` | codes, their units, defaults and status | 132 |
| `cosmo-theory-foundations` | definitions and formulae with the paper fixing each | 137 |
| `cosmo-photometry-photoz` | photometric calibration, photo-z, n(z) calibration | 150 |
| `cosmo-galaxy-halo-connection` | HOD, SHAM, stellar-to-halo mass, assembly bias, halo model | 162 |
| `cosmo-data-pipelines` | spectroscopic, imaging and CMB pipelines; masks, randoms, validation | 129 |
| `cosmo-bbn` | primordial abundances, nuclear rates, BBN codes, Ω_b h² prior | 104 |
| `cosmo-machine-learning` | emulators, neural compression, SBI, generative models, robustness | 140 |
| `cosmo-cosmic-web` | web classification, filaments, environment, filament gas, protoclusters | 126 |
| `cosmo-early-universe-exotica` | PTA background, PBHs, defects, EDE, spectral distortions | 131 |

Each domain skill has the same shape: a `SKILL.md`, five reference files
(`physics-and-methods`, `surveys-and-data`, `results`, `systematics`,
`open-questions`), a bibliography `sources.tsv`, and six dossiers in `deep/`.

## Your own layer (Claude Code)

Add your own notes, papers, dossiers, or a different value for one section,
without editing the package. They live in `~/.cosmoskill/` (personal) or
`.cosmoskill/` in a project, and the skills say when an answer uses them.
In a conversation, just ask: "note, for my cluster work, that …", "add this
paper to my layer", "for me, use this value instead"; the `cosmoskill-refine`
skill runs the commands. By hand:

```bash
S=plugin/skills/observational-cosmology/scripts
python3 $S/layers.py init
python3 $S/layers.py note cosmo-weak-lensing results#the-cmb-reference-values "quote S8 differences against both CMB references"
python3 $S/sync_layers.py        # after an update: entries whose section changed
```

Format: `docs/layers.md`; specification: `docs/layers-v1.md`.

## Maintaining

Refresh a domain every few months, never from memory: the procedure is in
`plugin/skills/observational-cosmology/references/suite-conventions.md`, and asking
Claude to update a domain loads it. `python3 tools/refresh_status.py --due 90`
lists what is due. After editing:

```bash
python3 tools/assign_keys.py && python3 tools/sync_blocks.py
python3 plugin/skills/observational-cosmology/scripts/verify_sources.py plugin/skills/cosmo-<domain>
python3 tools/check_keys.py --against <last release>
python3 tools/check_numbers.py --skill cosmo-<domain> --list   # must print nothing
python3 -m pytest -q
```

At a release, `tools/make_release_manifest.py` writes `releases/<version>.tsv`,
the sections added, changed, moved or retired. Contributions follow
`CONTRIBUTING.md`. Scripts need Python 3.9+ and the standard library only.

## Repository layout

The plugin is in `plugin/` (manifest, skills, licence); the rest of the
repository (docs, tests, tools, release manifests) is for maintainers.

## Licence

MIT, for the text and for the scripts. See `LICENSE`.
