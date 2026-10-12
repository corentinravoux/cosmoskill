---
name: cosmo-cmb
description: Use when reviewing, fact-checking or planning text or analysis on CMB anisotropies — TT/TE/EE power spectra, CMB lensing reconstruction, Planck PR3/PR4 likelihoods (Plik, CamSpec, HiLLiPoP, SRoll2), ACT DR6, SPT-3G D1, P-ACT, CMB-SPA, A_L lensing anomaly, optical depth tau, N_eff or neutrino mass from the CMB, B-mode status, foregrounds, beams, Simons Observatory, CMB-S4, LiteBIRD, or when a CMB prior enters a BAO, RSD or peculiar-velocity fit.
---

# CMB anisotropies and lensing — expert reference

Snapshot 2026-10-07. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map

| Question | Load |
|---|---|
| What a feature constrains, estimators, likelihoods, codes, conventions | `references/physics-and-methods.md` |
| Instruments, releases, data locations, status, what comes next | `references/surveys-and-data.md` |
| Current parameter values, lensing, τ, N_eff, Σm_ν, history of each number | `references/results.md` |
| Beams, leakage, calibration, foregrounds, τ systematics, referee checklist | `references/systematics.md` |
| τ debate, A_L fate, CMB–DESI discrepancy, forecasts, stale claims | `references/open-questions.md` |
| Bibliography with roles | `references/sources.tsv` |

## What an expert holds in mind

- SPT+ACT now matches Planck on H₀ and σ₈; CMB-SPA gives H₀ = 67.19 ± 0.38,
  σ₈ = 0.8137 ± 0.0037 in ΛCDM (arXiv:2506.20707, second version).
- P-ACT (ACT DR6 + Planck truncated at ℓ < 1000 TT, ℓ < 600 TE/EE;
  H₀ = 67.62 ± 0.50, n_s = 0.9709 ± 0.0038) is not CMB-SPA
  (arXiv:2503.14452).
- ACT and SPT are calibrated on Planck and take τ from Planck low-ℓ
  polarisation; only shape parameters are independent (arXiv:2504.16932).
- τ from Planck reprocessings lies in 0.051–0.063 with σ ≈ 0.006
  (arXiv:2007.04997, arXiv:1908.09856, arXiv:2309.10034). CMB + DESI
  without low-ℓ EE prefers 0.090 ± 0.012 (arXiv:2504.16932); reionisation
  data side with the low value (arXiv:2601.09644, arXiv:2607.26373).
- A_L: 1.180 ± 0.065 is Planck PR3 Plik (arXiv:1807.06209). PR4 gives
  1.039 ± 0.052 (HiLLiPoP, arXiv:2309.10034); ACT DR6 gives 1.007 ± 0.057;
  SPT+ACT 1.016 (+0.048/−0.054). The CMB-SPA peak-smoothing amplitude is
  still 1.079 ± 0.038.
- A_L rescales peak smoothing only; it is not the reconstruction amplitude
  (arXiv:0803.2309).
- Lensing reconstructions match the primary-CMB prediction: ACT DR6
  1.013 ± 0.023 (arXiv:2304.05202), ACT+SPT+Planck 1.025 ± 0.017
  (arXiv:2504.20038), SPT-3G D1 at 2% (arXiv:2608.31136).
- The CMB–DESI DR2 distance in ΛCDM is 1.6σ (P-ACT), 2.8σ (CMB-SPA) or
  3.7σ (SPT+ACT); name the CMB data set (arXiv:2503.14452,
  arXiv:2506.20707, arXiv:2503.14738).
- N_eff: ACT DR6 2.60 (+0.21/−0.29), SPT-3G D1 3.18 (+0.29/−0.33), CMB-SPA
  2.82 ± 0.12; standard value 3.044 (arXiv:2503.14454, arXiv:2506.20707).
- Σm_ν limits of 0.064–0.089 eV are CMB + BAO in ΛCDM and move with τ and
  the lensing data (arXiv:2503.14744, arXiv:2608.31136); the CMB alone
  gives < 0.26 eV (arXiv:1807.06209).
- r < 0.036 (BK18, arXiv:2110.00483) is still the latest BICEP/Keck limit.
- CMB-S4 lost DOE and NSF support on 9 July 2025. LiteBIRD was reformed to
  one telescope, 12 bands, launch JFY2036 (arXiv:2607.25285).
- ACT DR6 and SPT-3G D1 were blinded and both changed after unblinding.
- Check the arXiv version: CMB-SPA H₀ and the ACT Σm_ν limit both changed.

## Systematics a referee checks

- Planck likelihood, low-ℓ EE likelihood or τ prior, Planck truncation.
- Temperature-to-polarisation leakage and polarised beams: 1.7σ on Ω_b h²
  in ACT if ignored; SPT's sidelobe model is not confirmed by a direct
  measurement (arXiv:2602.06334).
- Polarisation efficiency and calibration to Planck.
- Foreground-template and frequency-split robustness (arXiv:2506.06274).
- Lensing foreground bias and estimator choice (arXiv:2304.05196).
- Non-linear lensing model, Boltzmann accuracy, super-sample lensing,
  aberration (arXiv:2103.05582, arXiv:1401.7992, arXiv:1309.2285).
- Covariance validation; ACT–Planck sky overlap.

## Errors that recur

- Quoting "the Planck value" for H₀, A_L or Ω_K without release and
  likelihood.
- Calling the A_L anomaly either "2.8σ" or "resolved".
- Comparing θ_MC, θ* and the CLASS θ_s across tables.
- Comparing σ₈(Ω_m/0.3)^0.25 from CMB lensing with galaxy-lensing S₈.
- Treating ACT, SPT and Planck amplitudes (A_s, σ₈) as independent.
- Citing CMB-S4 or pre-2026 LiteBIRD targets as upcoming.
- Quoting a CMB + DESI neutrino bound as a CMB result.
- Combining CMB and BAO where they disagree at over 3σ (ΛCDM+N_eff).

## Related skills

- `cosmo-inflation-primordial`: r, n_s, B-mode analyses, birefringence.
- `cosmo-cmb-lss-cross-correlations`: lensing × galaxies, kSZ, tSZ, ISW.
- `cosmo-neutrinos-dark-matter`: Σm_ν and light-relic models.
- `cosmo-dark-energy-modified-gravity`, `cosmo-tensions-anomalies`:
  implications of the CMB–BAO discrepancy; large-angle anomalies.
- `cosmo-reionization-21cm`: reionisation history behind τ.
- `cosmo-distance-ladder-h0`, `cosmo-weak-lensing`: H₀ and S₈ comparisons.
