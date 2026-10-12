---
name: cosmo-lyman-alpha
description: Use when reviewing, planning or fact-checking Lyman-alpha forest work — Lyα BAO and Alcock-Paczynski at z~2.3, full shape, 1D flux power spectrum P1D (FFT, QMLE), P3D and P-cross, picca deltas, continuum fitting, distortion matrix, DLA/BAL/metal contamination, Vega fits, Lyα tomography and void cross-correlation, IGM thermal state, Nyx/PRIYA/LaCE/ForestFlow emulators, warm or fuzzy dark matter and neutrino limits from the forest, BOSS/eBOSS/DESI DR1/DR2 Lyα results.
---

# Lyman-alpha forest — expert reference

Snapshot 2026-10-07. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map

| Question | Load |
|---|---|
| Delta field, estimators (ξ, P1D, P3D, P×), fit model, AP, emulators, codes, units | `references/physics-and-methods.md` |
| Samples, releases, simulations, mocks, public products, future | `references/surveys-and-data.md` |
| Current values, fit details, history, what is superseded | `references/results.md` |
| Each systematic: size, mitigation, validation; referee checklist | `references/systematics.md` |
| Tensions, method debates, forecasts, stale claims | `references/open-questions.md` |
| Bibliography with roles | `references/sources.tsv` |

## What an expert holds in mind

- Current BAO: DESI DR2, D_H/r_d = 8.632 ± 0.101, D_M/r_d = 38.99 ± 0.53 (stat + sys), ρ = −0.431, z_eff = 2.33 (arXiv:2503.14739).
- Current best distances come from the DR2 full shape: D_M/D_H = 4.572 ± 0.046, D_H/r_d = 8.600 ± 0.066, D_M/r_d = 39.32 ± 0.33, ρ = +0.225 (arXiv:2607.27410). They agree with Planck ΛCDM and sit about 2σ from the CMB + BAO w0waCDM prediction.
- The Lyα BAO carries a theory systematic for the non-linear shift: 0.3% per direction in the BAO paper, revised to 0.15% (isotropic) and 0.8% (peak AP) in the full-shape paper. Studies disagree on the sign (arXiv:2412.06892, arXiv:2503.13442).
- fσ8 from the forest fails mock validation and is excluded in DR1 and DR2 (arXiv:2509.15308, arXiv:2607.27411). β is b_η f / b_δ, not f/b.
- The continuum fit removes the mean and slope of δ per forest and absorbs F̄(z); models are distorted with the distortion matrix (arXiv:1702.00176, arXiv:2506.15262). The distortion leaks r_∥ < 10 h⁻¹Mpc into all scales and biases AP at the percent level unless marginalised (arXiv:2607.27410).
- DESI DR1 P1D cosmology: Δ²_★ = 0.379 ± 0.032, n_★ = −2.309 ± 0.019 at 0.009 s/km, z = 3, from 62,807 spectra with S/N > 3, consistent with Planck (arXiv:2601.21432).
- The DR1 slope error is three times the eBOSS one: LLS, Si II–Si II and emulator errors are now marginalised.
- Running: eBOSS-era α_s = −0.010 ± 0.004 (arXiv:1911.09073); DESI DR1 + CMB + BAO gives 0.0014 ± 0.0041. The "5σ" tension claims use eBOSS likelihoods (arXiv:2311.16377, arXiv:2511.01612).
- One eBOSS data vector gave σ_8 = 0.733 (PRIYA, arXiv:2309.03943) and 0.841 (EFT, arXiv:2405.13208); the amplitude is degenerate with the mean flux (arXiv:2412.05372).
- WDM limits run from 1.9 to 5.7 keV with thermal-history priors and k_max (arXiv:1912.09397, arXiv:2309.04533).
- DESI measures P1D with both FFT and QMLE; cosmology uses QMLE (arXiv:2505.09493, arXiv:2505.07974).
- Tomography has two regimes: 2–4 h⁻¹Mpc over ≲ 2 deg² with galaxies (CLAMATO, LATIS), 13 h⁻¹Mpc over 220 deg² with quasars (arXiv:2004.01448); void–forest RSD: β = 1.21 ± 0.18 (arXiv:2203.11045).

## Systematics a referee checks

Continuum distortion and its small-scale leakage; mean-flux prior; DLA finder purity and residual HCD/LLS model; metals; BAL masking; resolution and noise; quasar redshift errors; correlated sky-subtraction noise; BAO shift term; UV fluctuations and reionisation relics; covariance; emulator error and thermal priors; mock realism; blinding. Sizes and mitigations: `references/systematics.md`.

## Errors that recur

- Quoting DESI DR1 (2% on H) as the latest Lyα BAO, or a 2.5σ Lyα BAO tension with ΛCDM (BOSS DR11; 1.5σ at eBOSS DR16).
- Quoting a Lyα fσ8, or converting β to f as for galaxies.
- Comparing compressed P1D parameters across papers without checking pivot units (s/km versus Mpc⁻¹) and definitions: (Δ²_★, n_★), (A_Lyα, n_Lyα), (A_P, n_P) differ.
- Quoting a WDM or FDM limit without its thermal-history assumption and k_max.
- Stating that the forest alone constrains Σm_ν: alone about 1 eV; DESI DR1 P1D moves CMB + BAO from 55.1 to 53.7 meV.
- Mixing D_A with D_M, or the DR2 BAO-only and full-shape distance pairs (opposite-sign correlations).
- Confusing the DESI P1D sample sizes: more than 300,000 quasars measured, 62,807 used for cosmology.
- Treating b_α and β_α from BAO fits as measurements; they are nuisance parameters.

## Related skills

- `cosmo-galaxy-clustering`: galaxy and quasar BAO, combined DESI cosmology.
- `cosmo-dark-energy-modified-gravity`: the w0wa interpretation.
- `cosmo-neutrinos-dark-matter`: particle interpretation of Σm_ν, N_eff, WDM, FDM.
- `cosmo-reionization-21cm`: reionisation history, τ.
- `cosmo-beyond-two-point`: voids, field-level inference.
- `cosmo-simulations-mocks`, `cosmo-software-ecosystem`, `cosmo-surveys-facilities`: simulations, codes, facilities.
