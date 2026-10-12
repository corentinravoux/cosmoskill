---
name: cosmo-supernovae
description: Use when reviewing, planning or fact-checking Type Ia supernova cosmology — Hubble diagram, distance modulus, SALT2/SALT3, BayeSN, stretch and colour standardisation, host mass step, BBC/BEAMS bias corrections, photometric classification, UNITY, calibration (Fragilistic, Dovekie), low-redshift anchor, Pantheon+, Union3/3.1, DES-SN5YR, DES-Dovekie, Unite, ZTF SN Ia DR2, DEBASS, Rubin and Roman supernovae, SN sample choice in w0wa fits, lensed SNe, SNe II, siblings.
---

# Type Ia supernova cosmology — expert reference

Snapshot 2026-10-07. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map

| Question | Load |
|---|---|
| Standardisation, SALT/BayeSN, scatter models, BBC, BEAMS, UNITY, covariance, redshift corrections, calibration chain, blinding, codes | `references/physics-and-methods.md` |
| Surveys, compilations, sample sizes, what is superseded, data locations, Rubin/Roman, SNe II, lensed SNe, siblings | `references/surveys-and-data.md` |
| Current `Omega_m`, `w`, `w0`–`w_a` per sample; history; mass-step history | `references/results.md` |
| Size, mitigation and test of each systematic; referee checklist | `references/systematics.md` |
| Controversies, method debates, forecasts, stale claims | `references/open-questions.md` |
| Bibliography | `references/sources.tsv` |

## What an expert holds in mind

- An unanchored SN Hubble diagram measures the shape of `d_L(z)` only; `M`
  and `H0` are degenerate. SN-only fits constrain `Omega_m` (LCDM) or a
  `q0`-like combination, never `w_a` (arXiv:2511.07517, arXiv:2609.05053).
- Current samples: **Unite** (2884 SNe, Pantheon+ ∪ DES, arXiv:2609.05053),
  **DES-Dovekie** (arXiv:2511.07517), **Union3.1** (arXiv:2601.19424).
  DES-SN5YR and Union3 are superseded; Pantheon+ (arXiv:2202.04077) stands
  with revised host masses.
- Flat-LCDM `Omega_m` from SNe alone: 0.310 (+0.012/−0.011) Unite, 0.330 ±
  0.015 DES-Dovekie, 0.344 (+0.026/−0.025) Union3.1 [src].
- The DESI DR2 significances of 2.8 / 3.8 / 4.2 sigma for Pantheon+ / Union3
  / DESY5 (arXiv:2503.14738) became 3.2 / 3.4 / 3.4 sigma after two fixes
  (arXiv:2601.19424); Unite gives 3.3 sigma with "weak" Bayesian evidence.
  DES-Dovekie is 3.2 sigma in its own paper, with Planck + ACT + SPT as the
  CMB (arXiv:2511.07517), and 3.4 sigma in the DESI-style recomputation.
- The two fixes: Dovekie recalibration plus a colour-law implementation
  error in DES (arXiv:2511.07517), and inconsistent host masses between low
  and high redshift (arXiv:2601.19424, arXiv:2609.05321).
- The compilations share most low-z supernovae; they are not independent.
- The low-z anchor controls the dark-energy result: cutting z < 0.1 moves
  Unite by ~2 sigma. No analysis yet uses a modern anchor; DEBASS, ZTF and
  TITAN are pending (arXiv:2508.10877).
- ZTF SN Ia DR2 is not cosmology-grade by its authors' own statement
  (arXiv:2409.04346, arXiv:2509.04073).
- Calibration and model training are coupled; small zero-point shifts are
  amplified up to sixfold in distance (arXiv:2112.03864, arXiv:2506.05471).
- The residual mass step runs from 0 to 0.17 mag depending on bias-correction
  dimensionality, scatter model, tracer and stretch linearity; its origin is
  disputed (arXiv:2004.10206 vs arXiv:2605.06799).
- Bias-corrected distances of the same SN differ between analyses with
  different selection functions (arXiv:2501.06664).
- Unbinned covariances cut the systematic error by ~1.5
  (arXiv:2012.05900); one-at-a-time budget rows do not add in quadrature.
- Only BBC and UNITY have produced cosmology from data; SBI results are on
  simulations (arXiv:2603.11165).

## Systematics a referee checks

Cross-calibration and SALT training on one solution; selection-bias
simulations with their population and scatter models; host step, its tracer
and host-mass consistency across redshift; evolution of `alpha`, `beta`,
`gamma`; contamination and host mismatch; peculiar velocities and the low-z
cut; Milky Way extinction; lensing; anchor heterogeneity; tension metric
before combining probes. Sizes in `references/systematics.md`.

## Errors that recur

- Quoting 4.2 sigma (DESY5) or `Omega_m = 0.352` after November 2025.
- Saying Pantheon+ "shows no signal": true of the 2022 release, not after the
  host-mass correction.
- Treating Pantheon+, Union3 and DES as three independent confirmations.
- Reading SN-only `w_a ≈ −8` as a measurement; it is a prior-volume effect.
- Comparing a frequentist `Delta chi2` significance with a Bayes factor, or
  FoM values under different definitions (factor 19.4).
- Comparing object-by-object distance moduli across compilations as a null
  test.
- Using ZTF DR2 light curves for cosmological parameters.
- Citing the "non-accelerating universe" age-bias claim (arXiv:2510.13121)
  without its rebuttals (arXiv:2601.13785, arXiv:2604.16597).
- Mixing `z_hel`, `z_CMB` and `z_HD` in `d_L` (arXiv:1907.12639).

## Related skills

- `cosmo-distance-ladder-h0`: SN absolute calibration, SH0ES/CCHP, SN II and
  lensed-SN `H0`.
- `cosmo-peculiar-velocities`: SNe as velocity tracers, `f sigma8`.
- `cosmo-dark-energy-modified-gravity`: interpretation of `w0`–`w_a`.
- `cosmo-tensions-anomalies`: cross-probe inconsistency, SN dipoles.
- `cosmo-statistics-inference`: tension metrics, evidence, covariances.
- `cosmo-surveys-facilities`: Rubin, Roman, ZTF instrument facts.
