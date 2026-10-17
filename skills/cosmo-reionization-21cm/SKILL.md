---
name: cosmo-reionization-21cm
description: Use when reviewing, planning or fact-checking reionisation or 21 cm work — reionisation history, optical depth tau, Gunn-Peterson troughs, dark pixels, Lyα damping wings, Lyα emitter fractions, patchy kSZ, neutral fraction x_HI, EDGES and SARAS global signal, 21 cm power-spectrum limits (HERA, LOFAR, MWA, NenuFAR), foreground wedge, HI intensity mapping (CHIME, MeerKAT, Tianlai, HIRAX, CHORD, SKA), line-intensity mapping (CO, [CII], COMAP, SPHEREx), JWST early galaxies.
---

# Reionisation, 21 cm and line-intensity mapping — expert reference

Snapshot 2026-10-13. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| τ, x_HI(z), kSZ, 21 cm limits, HI and line-intensity results, JWST; history of each number | `references/results.md` |
| Observables, 21 cm equations, wedge, estimators, codes, conventions | `references/physics-and-methods.md` |
| Experiments, data sets, status, what comes next | `references/surveys-and-data.md` |
| Signal loss, calibration, continuum, local absorbers; referee checklist | `references/systematics.md` |
| τ = 0.06 or 0.09, late reionisation, EDGES, forecasts, stale claims | `references/open-questions.md` |
| How a 21 cm limit becomes an astrophysical constraint: likelihood, models, priors, emulators, samplers | `deep/eor-inference-modelling.md` |
| How x_HI is inferred from Lyα equivalent widths: measurement, baseline, transmission model, likelihood | `deep/lya-emitters.md` |
| How a CO, [CII] or Hα map becomes a limit on L(M_h) or ρ_H2: estimators, stacking, VID, interlopers, nulls | `deep/line-intensity-mapping.md` |
| Bibliography with roles | `references/sources.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Planck low-ℓ polarisation gives τ = 0.051–0.063, σ ≈ 0.005–0.009 (arXiv:1807.06209, arXiv:1908.09856, arXiv:2103.14378; lowest, 0.051 ± 0.006 from NPIPE, arXiv:2007.04997, in `cosmo-cmb`). The value 0.090 ± 0.012 is CMB + DESI without low-ℓ EE, not a measurement (arXiv:2504.16932).
- Reionisation probes in place of low-ℓ EE give τ = 0.067 ± 0.011 (arXiv:2607.26373). τ = 0.09 sits ≈ 2σ from SPT patchy-kSZ limits (arXiv:2505.15899); exotic ionisation adds ≤ 0.008 (arXiv:2608.01919).
- Reionisation ends late: dark gaps persist to z ≃ 5.3 (arXiv:2109.06295); x_HI = 0.19 ± 0.07 at z = 5.6 (arXiv:2405.12273). Background fluctuations remain an alternative (arXiv:2312.08464).
- The mean free path falls from 9.33 to 0.81 proper Mpc over z = 5.08–5.93 (arXiv:2308.04614).
- At z ~ 7 every probe gives x_HI ≈ 0.4–0.65 with errors of 0.2–0.4 (arXiv:1802.06066, arXiv:2504.04683, arXiv:2609.40363).
- kSZ: SPT-3G D1 finds D_3000 = 1.75 ± 0.86 μK² and Δz(25–75%) < 3.8 (arXiv:2601.20551); ACT gives Δz < 4.4 (arXiv:2506.06274). "Δz = 1.0" is superseded (arXiv:2002.06197).
- EDGES (78 MHz, 0.5 K; arXiv:1810.05912) is unconfirmed; SARAS 3 rejects its profile at 95.3% (arXiv:2112.06778); its depth moves from 370 to 670 mK with the beam correction (arXiv:1910.03165). EDGES data are public since 2026 (arXiv:2605.16643).
- No 21 cm power spectrum is detected at z > 6. Deepest 2σ limits: HERA Phase I 457 mK² (z = 7.9, k = 0.34 h/Mpc; arXiv:2210.04912), MWA (23.0 mK)² east–west and (21.7 mK)² = 470 mK² north–south (z = 6.5; arXiv:2508.04164), LOFAR (54.3 mK)² (z = 9.1; arXiv:2503.05576), NenuFAR 4.6 × 10⁵ mK² (z = 20.3; arXiv:2507.10533). HERA Phase II is limited by mutual coupling (arXiv:2511.21289).
- HI intensity mapping has auto-spectra: CHIME, 12.5σ at z ~ 1 (arXiv:2511.19620); MeerKLASS, S/N 6.2 at z = 0.42 (arXiv:2610.12158). No BAO.
- An amplitude is Ω_HI b_HI r (cross), Ω_HI b_HI (auto) or CHIME's A_HI, never Ω_HI (arXiv:1208.0331, arXiv:2202.01242).
- No other line is detected on clustering scales: COMAP sets limits (arXiv:2406.07511); COPSS and mmIME see CO shot noise (arXiv:1605.03971, arXiv:2008.08087); mean CO (7σ) and [CII] (3σ) backgrounds come from tomographic cross-correlation (arXiv:2602.02658).
- JWST: the baryon-limit argument used photometric candidates (arXiv:2208.01611); ΛCDM models fit luminosity functions to z = 14 (arXiv:2604.18683). The photon-budget excess (arXiv:2404.07250) shrinks with mass-complete samples (arXiv:2409.01286).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

- τ: low-ℓ likelihood, reionisation parametrisation, measured or prior.
- x_HI: weighting, topology model, limit or measurement; continuum and lifetime; local absorbers (arXiv:2501.13899).
- 21 cm limits: confidence level, k, z; signal-loss test (arXiv:1810.05175); sky-model calibration (arXiv:1603.00607).
- Global signal: foreground-model uniqueness, beam chromaticity (arXiv:1805.01421).
- Intensity mapping: transfer function (arXiv:2302.07034); null tests between subsets.
- kSZ: late-time template, tSZ–CIB model, definition of Δz.

## Errors that recur
<!-- key: errors-that-recur -->

- Writing that EDGES detected cosmic dawn, or that HERA detected heating.
- Quoting τ ≈ 0.09 as measured, or "reionisation ended at z = 6".
- Ranking 21 cm limits taken at different k, or mixing mK² with (mK)².
- Citing PAPER-64 limits from before the 2019 re-analysis (arXiv:1909.02085).
- Reading a dark trough as a neutral-fraction measurement (arXiv:2510.25829).
- Stating that 21 cm has only cross-correlation detections.
- Reading "blind" foreground cleaning as analysis blinding.
- Comparing the tanh midpoint (z ≈ 8.1) with model-based midpoints (z ≈ 7.2; arXiv:2504.09725).

## Related skills
<!-- key: related-skills -->

- `cosmo-cmb`: low-ℓ likelihoods, τ in parameter fits.
- `cosmo-lyman-alpha`: forest at z < 5, thermal history.
- `cosmo-cmb-lss-cross-correlations`: late-time kSZ, patchy screening.
- `cosmo-tensions-anomalies`, `cosmo-neutrinos-dark-matter`, `cosmo-dark-energy-modified-gravity`: consequences of τ.
- `cosmo-surveys-facilities`, `cosmo-simulations-mocks`: facility facts; simulation suites.

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

Sizes, in thousands of tokens: L1 3k; open 5k; methods 13k; results 13k; surveys 5k; systematics 11k; deep/eor-inference-modelling 8k; deep/line-intensity-mapping 8k; deep/lya-emitters 6k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-reionization-21cm`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-reionization-21cm/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
