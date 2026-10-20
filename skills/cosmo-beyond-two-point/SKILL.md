---
name: cosmo-beyond-two-point
description: Use when reviewing, planning or fact-checking statistics beyond the two-point function — galaxy bispectrum, trispectrum, parity-odd 4PCF, cosmic voids (finders, void size function, void–galaxy AP/RSD, void lensing), density-split, kNN, wavelet scattering, Minkowski functionals, marked spectra, lensing peaks, PDF or third-order shear, field-level inference (BORG, LEFTfield, Gaussian field likelihoods), simulation-based inference (SimBIG), Beyond-2pt challenge, data-versus-mocks status.
---

# Beyond two-point statistics — expert reference

Snapshot 2026-10-13. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Data or mocks only (§0 status table); current values; history | `references/results.md` |
| Definitions, estimators, models, meanings of "field-level", codes, conventions | `references/physics-and-methods.md` |
| Samples, void catalogues, simulation suites, the Beyond-2pt challenge | `references/surveys-and-data.md` |
| Size of a systematic; referee checklist | `references/systematics.md` |
| Controversies, forecasts, stale claims, what was not verified | `references/open-questions.md` |
| Bibliography with roles | `references/sources.tsv` |
| How a void size function fit is built | `deep/void-finding-size-function.md` |
| How a field-level sampler is set up and checked | `deep/field-level-inference.md` |
| How an SBI analysis is built and checked | `deep/simulation-based-inference.md` |
| How a void–galaxy or void–forest RSD and AP fit is built | `deep/void-galaxy-rsd-ap.md` |
| How a void shear or CMB-lensing stack is measured and fitted | `deep/void-lensing-cmb.md` |
| How a density-split, kNN, WST or MF emulator analysis is built | `deep/emulator-summary-statistics.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- The DESI bispectrum is DR1 only. It tightens the amplitude, raises σ8 by 1.1σ and weakens the w0wa preference: 2.8σ with CMB, 3.1σ with CMB and DES-Dovekie (arXiv:2606.23936).
- The gain from B0 depends on the pipeline and the baseline: 4–10% (arXiv:2610.01836), about 10% (arXiv:2507.13433), 20–26% (arXiv:2603.19356, arXiv:2606.23936); the 26% is not at fixed power-spectrum data vector.
- Parity-odd 4PCF: 7.1σ in BOSS against Patchy mocks (arXiv:2206.03625), 1.4σ with N-body mocks (arXiv:2401.09523); in DESI DR1 the auto analysis gives 4–10σ and the cross-patch analysis nothing (arXiv:2508.09133). No detection.
- Void–galaxy AP/RSD has no DESI result; the reference is SDSS, Ω_m = 0.337 +0.026/−0.029 (arXiv:2205.06258). Finder response to AP and velocity-profile mismatch were quantified afterwards (arXiv:2407.02699, arXiv:2206.14120); the SDSS budgets cover the first through their fiducial-cosmology term.
- Mock calibration moves the BOSS void f/b from 0.540 ± 0.091 to 0.347 ± 0.023 (arXiv:2007.07895).
- Density split, wavelet scattering and Minkowski functionals on data all use BOSS CMASS, AbacusSummit and an HOD: σ8 = 0.792 ± 0.034 and 0.783 ± 0.026 (arXiv:2309.16541, arXiv:2501.01698). Their agreement is not independent confirmation.
- The Beyond-2pt challenge tested the bias of the mean on HOD mocks without systematics; it states that it does not validate error bars (arXiv:2405.02252).
- Third-order shear: KiDS-Legacy S8 = 0.806 +0.025/−0.023 (arXiv:2606.12389), DES Y3 0.780 ± 0.015 (arXiv:2508.14018), HSC Y3 0.736 ± 0.020 (arXiv:2508.14019). The gain is in Ω_m.
- DES Y3 map-level SBI: S8 = 0.808 ± 0.017 in wCDM, almost three times the two-point figure of merit (arXiv:2606.11309).
- "Field-level" means sampled initial conditions, a Gaussian likelihood on the field (from peculiar-velocity analyses, arXiv:1706.05205; implemented in flip, arXiv:2501.16852), or a neural network. Only the last two were found to have produced parameters from data.
- BORG on 2M++ (arXiv:1806.11117, arXiv:2505.10682), BOSS (arXiv:1909.06396) and Quaia (arXiv:2602.02363) delivers fields.
- Field-level gain over P + B: factor 3.5–5.2 on simulated halos (arXiv:2403.03220) against equivalence with an analytic likelihood (arXiv:2507.05378, arXiv:2509.09673).
- SimBIG uses about 10% of BOSS; its bispectrum result is robust, its wavelet result is not (arXiv:2310.15243, arXiv:2310.15250).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

Mock count against data-vector length and mock fidelity; galaxy–halo model
and a non-HOD test; emulator error; simulation-suite restrictions (fixed θ_*,
prior edges); coverage and out-of-distribution tests; void finder,
reconstruction and calibration; baryons, source clustering and IA at third
order; field-level noise model; baseline of every quoted gain; blinding of
data against blinding of a mock. Details: `references/systematics.md` §7.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting a Quijote Fisher gain for the matter field as a survey forecast; the marked spectrum fell from above 2× to 1.2× on data (arXiv:2001.11024, arXiv:2404.04228).
- Comparing D_A H/c between void papers: proper in arXiv:1904.01030, comoving in arXiv:2007.07895.
- Reading "w < −0.80" from DES Y3 SBI as a measurement; the prior is −1 < w < −1/3 (arXiv:2403.02314).
- Mixing ΛCDM and wCDM S8 values from lensing SBI papers.
- Citing the HSC Y3 2+3-point 3.2σ tension without the later redshift recalibration.
- Calling a BORG reconstruction a cosmological constraint.

## Related skills
<!-- key: related-skills -->

- `cosmo-galaxy-clustering`: two-point full shape, BAO, f_NL from scale-dependent bias.
- `cosmo-lyman-alpha`: tomography, forest systematics.
- `cosmo-weak-lensing`: two-point shear, calibration, S8 history.
- `cosmo-peculiar-velocities`: field likelihoods on velocity data, fσ8 at low redshift.
- `cosmo-inflation-primordial`: f_NL and parity models.
- `cosmo-statistics-inference`, `cosmo-simulations-mocks`, `observational-cosmology`: covariance corrections, simulation suites, hub.

<!-- cosmoskill:block:start — generated by tools/sync_blocks.py, do not edit by hand -->
## Levels and layers
<!-- key: levels-and-layers -->

Answer at the lowest level that answers the question, then stop.

| Level | Read | Holds |
|---|---|---|
| L1 | this file only | the headline values, the state of the domain, the list a referee checks, the errors that recur |
| L2 | one file of `references/` | what this file does not hold: other values, their history, the size of each systematic, methods, releases |
| L3 | one dossier of `deep/` | how a result is obtained and how to choose a method |
| L4 | the cited paper itself | what L1 to L3 quote; required before a number goes into a manuscript, a proposal or a referee report, and when two statements of the skills disagree |

Sizes, in thousands of tokens: L1 3k; open 6k; methods 19k; results 9k; surveys 4k; systematics 12k; deep/emulator-summary-statistics 6k; deep/field-level-inference 7k; deep/simulation-based-inference 6k; deep/void-finding-size-function 8k; deep/void-galaxy-rsd-ap 8k; deep/void-lensing-cmb 6k.

- L2: when the file map names several files, search them for the term
  before reading, and read only the passage.
- L4 starts from the L2 entry: its citation and flag say where to look. Read
  the paper with
  `python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/fetch_paper.py" <arXiv id>`
  (`--abstract`, `--outline`, `--section`, `--grep`), or with any tool that
  gives the paper. If it cannot be read, say that L4 was required and not
  done.
- A formula of the skill may be applied to the asker's numbers; label the
  result as derived.

Local layers: if a directory `.cosmoskill/` exists in the working directory,
in one of its parents, or in the home directory, or if `COSMOSKILL_HOME` is
set, run
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-beyond-two-point`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-beyond-two-point/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
