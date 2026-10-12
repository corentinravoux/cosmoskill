# Phase 1 log — generalising the package

2026-10-12, branch `phase-1-generalise`. Every passage removed or reworded
because it named one person's machine, tools, notes or voice. Passages are
verbatim except that machine paths are shown with the placeholders of
`../README.md`.
Numbers: see the fingerprint comparison at the end.

## Domain skills (task T4)

### `skills/cosmo-galaxy-clustering/references/results.md`

Why: pointer to a personal data package dropped (owner's decision).

Before:

```
`cosmo-peculiar-velocities`; the machine-readable compilation is in
`<packages>/growth_review`.
```

After:

```
`cosmo-peculiar-velocities`.
```

### `skills/cosmo-lyman-alpha/references/physics-and-methods.md`

Why: reference to one person's package removed.

Before:

```
The author's `lyapower` package fits the Arinyo-i-Prats model to P3D of Nyx boxes; the convergence facts that govern such fits are in §6.
```

After:

```
The convergence facts that govern fits of this model to simulation boxes are in §6.
```

### `skills/cosmo-lyman-alpha/references/physics-and-methods.md`

Why: reference to one person's packages replaced by a neutral statement; the four citations are kept so the bibliography is unchanged.

Before:

```
The author's own packages (`lelantos` for tomography and void finding, `lyavoid` for the void cross-correlation, `lyapower` for P3D fits, `p1desi` for DESI P1D) implement the methods of arXiv:2004.01448, arXiv:2203.11045, arXiv:1506.04519 and arXiv:2306.06311 respectively; general software conventions belong to `cosmo-software-ecosystem`.
```

After:

```
The methods of arXiv:2004.01448 (tomography and void finding), arXiv:2203.11045 (void cross-correlation), arXiv:1506.04519 (P3D model) and arXiv:2306.06311 (DESI P1D) each have a public implementation by their authors; general software conventions belong to `cosmo-software-ecosystem`.
```

### `skills/cosmo-simulations-mocks/references/physics-and-methods.md`

Why: reference to one person's package removed.

Before:

```
It is the model fitted to Nyx boxes in `lyapower`, and the six small-scale parameters that ForestFlow emulates are deviations of this kind.
```

After:

```
The six small-scale parameters that ForestFlow emulates are deviations of this kind.
```

### `skills/cosmo-multimessenger/references/physics-and-methods.md`

Why: private secondary source replaced by the abstract of arXiv:2512.15380, re-read 2026-10-12; 'the biases by its amplitude' was not in the abstract and is reworded to what the abstract states.

Before:

```
- "Peak Sirens": locate the peak of the angular cross-spectrum `C_ℓ(z, D_L)`; H0 is set
  by the position of the peak and the biases by its amplitude [sec: the author's
  tracer-choice report]. First detection on data: de Matos et al. 2025
  (arXiv:2512.15380).
```

After:

```
- "Peak Sirens": find the peak of the 3D angular cross-spectrum `C_ℓ(z, D_L)` between
  galaxy redshifts and siren luminosity distances; H0 follows from the position of the
  peak, and the same measurement bounds the gravitational-wave bias [src]. First
  detection on data: de Matos et al. 2025 (arXiv:2512.15380).
```

### `skills/cosmo-multimessenger/references/physics-and-methods.md`

Why: private report path removed; the class was confirmed in the public repository; the construction detail, read only in a local copy, is demoted.

Before:

```
contains a density data vector for that purpose, `GWDensMesh` in
`flip/data_vector/gw_vectors.py`, built from per-event sky-position kernels (local code
read, 2026-10-10). The tracer-choice argument for that application is in
`<config>/reports/research/2026-10-05_gw-h0-field-tracer-choice/report.md`.
```

After:

```
contains a density data vector for that purpose, `GWDensMesh` in
`flip/data_vector/gw_vectors.py` [src: public flip repository, `main` branch, class
present on 2026-10-12]. How it is built was read in a development copy and is listed
under "Not verified".
```

### `skills/cosmo-multimessenger/references/open-questions.md`

Why: private report removed as a source; the cited bullets below it are kept.

Before:

```
The author's 2026-10-05 report concludes that galaxies are the primary tracer for a
field-level comparison between a siren field in `d_L` and a tracer field in redshift,
with peculiar velocities as a secondary ingredient at the lowest redshifts. The parts
of that argument verified here:
```

After:

```
Which tracer field to compare with a siren field in `d_L` is not settled in the
literature read here. What the cited papers establish:
```

### `skills/cosmo-multimessenger/references/open-questions.md`

Why: reference to the private report removed.

Before:

```
  (arXiv:2512.15380), so an unbiased tracer of the matter field is not required (the
  report's inference, not a statement of that paper).
```

After:

```
  (arXiv:2512.15380). Whether that removes the need for an unbiased tracer of the
  matter field is an inference, not a statement of that paper.
```

### `skills/cosmo-tensions-anomalies/references/physics-and-methods.md`

Why: values quoted from a private compilation removed; the item stays as not verified.

Before:

```
  RACS, LoTSS, CatWISE): the author's 2026-08 compilation lists 0.41–0.46 ×
  10⁻² for radio samples and 0.73 × 10⁻² for CatWISE, not re-read at source
  this session.
```

After:

```
  RACS, LoTSS, CatWISE): not read at source.
```

### `skills/cosmo-software-ecosystem/references/physics-and-methods.md`

Why: environment-bound provenance redefined; private branch names removed.

Before:

```
Provenance of API facts: "installed" means the docstring or signature of the package installed in the author's environment was read this session (camb 2.0.4, pyccl 3.3.6, astropy 8.0.1, healpy 1.19.0, emcee 3.1.6, cosmoprimo 1.0.0). "checkout" means a local clone was read (CLASS v3.2.3, pypower 1.0.0, picca branch `4most_test`, flip branch `mesh_improvements`, EFTCAMB commit of 2026-04-02). "context7" means library documentation fetched through the context7 service on 2026-10-11.
```

After:

```
Provenance of API facts: "installed" means the docstring or signature was read in the released package at the stated version (camb 2.0.4, pyccl 3.3.6, astropy 8.0.1, healpy 1.19.0, emcee 3.1.6, cosmoprimo 1.0.0). "checkout" means the source repository was read at the stated version or commit (CLASS v3.2.3, pypower 1.0.0, EFTCAMB commit of 2026-04-02; picca and flip at a development state, not a release, so their facts should be re-read in the release in use). "context7" means library documentation fetched through the context7 documentation service on 2026-10-11.
```

### `skills/cosmo-software-ecosystem/references/systematics.md`

Why: environment-bound provenance redefined.

Before:

```
Provenance: "installed" is a docstring or signature read in the package installed in the author's environment (camb 2.0.4, pyccl 3.3.6, astropy 8.0.1, healpy 1.19.0, emcee 3.1.6, cosmoprimo 1.0.0); "checkout" is a local clone (CLASS v3.2.3, pypower 1.0.0, picca, flip); "context7" is library documentation fetched on 2026-10-11.
```

After:

```
Provenance: "installed" is a docstring or signature read in the released package at the stated version (camb 2.0.4, pyccl 3.3.6, astropy 8.0.1, healpy 1.19.0, emcee 3.1.6, cosmoprimo 1.0.0); "checkout" is the source repository read at the stated version (CLASS v3.2.3, pypower 1.0.0) or at a development state (picca, flip); "context7" is library documentation fetched on 2026-10-11.
```

### `skills/cosmo-software-ecosystem/references/systematics.md`

Why: statement about a personal package, supported only by private notes, removed.

Before:

```
- **flip and oneuniverse differ on angles.** flip uses radians; the author's `oneuniverse` package stores RA and Dec in degrees [sec: author's project notes].

```

After:

```
(deleted)
```

### `skills/cosmo-software-ecosystem/references/systematics.md`

Why: reference to a personal package and private notes removed; the advice stays.

Before:

```
often use NESTED ordering (the author's `oneuniverse` format does [sec: author's project notes]), whereas
```

After:

```
often use NESTED ordering, whereas
```

### `skills/cosmo-software-ecosystem/references/open-questions.md`

Why: finding about one machine's environment removed.

Before:

```
- Local finding, not a property of the code: in the author's environment the cosmoprimo `class` engine fails to import because `pyclass` was built against NumPy 1.x while NumPy 2.4.6 is installed.

```

After:

```
(deleted)
```

### `skills/cosmo-software-ecosystem/references/surveys-and-data.md`

Why: environment and private branch name removed; the version read is kept.

Before:

```
Version 9.21.0 is the one installed in the author's environment, from a checkout on branch `4most_test`.
```

After:

```
The picca facts in this file were read at version 9.21.0, in a development state of the repository, not a tagged release.
```

## The two peculiar-velocity files moved from the hub (task T2)

Moved with `git mv` to `skills/cosmo-peculiar-velocities/references/`, names kept.
Citations rewritten from Markdown links and bare identifiers to the checked
form `arXiv:<id>`; no value changed.

### `fsigma8-pv-compilation.md`

Why: first person removed.

Before:

```
Every published fσ8 value I could locate from peculiar-velocity data (TF, FP,
```

After:

```
Published fσ8 values from peculiar-velocity data, as located by August 2026 (TF, FP,
```

### `fsigma8-pv-compilation.md`

Why: pointer to a personal data package dropped (owner's decision); history of deleted private files removed.

Before:

```
**The machine-readable data lives only in the package:**
`<packages>/growth_review/growth_review/data/measurements/fsigma8_pv.csv`, with
loaders, the per-row method audit trail and an integrity test suite. The
`fsigma8_pv_data.txt` mirror and its `validate_fsigma8.py` checker that used to
sit beside this file were deleted on 2026-08-14 — two copies of a compilation is
how a compilation goes wrong. This file is discussion only.

```

After:

```
This file is a table for reading and its discussion. It is not a data
product: a compilation meant to be loaded by code belongs in a data package
with its own integrity tests.

```

### `fsigma8-pv-compilation.md`

Why: first person and session narrative removed; the finding is kept.

Before:

```
I said last pass that these empty cells were a gap in this file. **That was
wrong, and the correction was itself the error.** Reading the papers:
```

After:

```
These empty cells are not a gap in this file: the papers give no effective
redshift. Reading them:
```

### `fsigma8-pv-compilation.md`

Why: stale section describing files that no longer exist.

Before:

```
## 6. Machine-readable

The full table lives in **`fsigma8_pv_data.txt`** in this directory — CSV with a
`#` comment header documenting every column, the provenance codes and the
non-independence warnings.

```python
import pandas as pd
d = pd.read_csv("fsigma8_pv_data.txt", comment="#")
d = d[~d.key.str.startswith("DESI_DR1_") | (d.key == "DESI_DR1_consensus")]
```

**35 rows, measurements only** — 32 [src], 3 [der], arXiv identifiers for all.
Simulation-validation studies are deliberately absent from the data file and
live in §2 above. Run `validate_fsigma8.py` after any edit: it checks row count,
column alignment, required fields and controlled vocabularies, and has already
caught two silent corruptions.
```

After:

```
(deleted)
```

### `pv-surveys.md`

Why: pointer to a personal data package dropped (owner's decision).

Before:

```
**Machine-readable form and plotting code**:
`<packages>/growth_review/` — `growth_review/data/measurements/fsigma8_pv.csv`
(18 columns: values, asymmetric errors, separate systematics, σ8 normalisation,
method family, fitting technique, arXiv, provenance) with loaders, the method
audit trail (`growth_review.methods.EVIDENCE`, one source sentence per row) and
figure builders that refuse to plot an uncited point. Discussion companion:
`fsigma8-pv-compilation.md`.
```

After:

```
Discussion companion: `fsigma8-pv-compilation.md`.
```


## Hub (task T3), documents (T5), packaging (T6), checks (T7, T8)

- Hub `SKILL.md`: description and router no longer name the peculiar-velocity
  files; the two paragraphs pointing to them and to a personal data package
  are removed; the four systematics checklists moved unchanged to
  `references/review-checklists.md`; scripts referred to through
  `${CLAUDE_SKILL_DIR}`.
- Hub `references/sources.tsv` created: 25 rows for the identifiers cited in
  `field-state-2026.md`, 23 copied from domain bibliographies, 2 fetched from
  arXiv. The hub is now under the checker.
- `references/suite-conventions.md` rewritten without private tooling.
- `docs/`: the first-build design, plan and test logs moved to
  `docs/history/`, machine paths replaced by placeholders; the agent brief
  made tool-neutral and persona-free.
- `LICENSE` (MIT), `.claude-plugin/plugin.json` at 0.2.0,
  `.claude-plugin/marketplace.json`, root `scripts` symlink removed, README
  rewritten with three install routes and the limits of this version.
- `tools/lint_generic.py`, `tools/check_structure.py`,
  `tools/numeric_fingerprint.py`, `tools/make_arxiv_snapshot.py`, 13 unit
  tests, `.github/workflows/check.yml`.

## Acceptance, as run on 2026-10-12

| Check | Result |
|---|---|
| `tools/lint_generic.py` on the tree | 0 lines |
| lint on its 16 bad fixtures | each flagged (unit test) |
| search for `/home/<name>`, home-relative `Software` or `Documents`, scratch paths, outside `.git` | none |
| `verify_sources.py skills/*/`, arXiv check on, snapshot as cache | 22 skills, 0 problems (hub 25 sources, peculiar velocities 150) |
| checker fails on wrong title, wrong author, uncited row, unlisted citation, bad header, duplicate key, unknown role | yes (unit tests) |
| `tools/check_structure.py` | 0 problems; fails on a broken copy (unit test) |
| unit tests | 13 pass |
| numbers in `skills/`, arXiv identifiers excluded | 49,193 before, 49,156 after; every lost token traced to a logged removal (three kinematic-dipole values quoted from a private compilation, a NumPy version, counts and dates of deleted paragraphs, "150–400 lines") |

Not run:

- `claude plugin validate . --strict`: the `claude` command was not available
  in the session.
- The clean-account test (three install routes, eight questions): needs the
  command-line client, a login and a commit.
- The continuous-integration job on GitHub: needs a push. Its steps were run
  locally, one by one, with the same commands.
