---
name: cosmo-statistics-inference
description: Use when reviewing, planning or fact-checking the statistical side of a cosmological analysis — likelihood, covariance from mocks, jackknife or analytic (Hartlap, Percival, Sellentin–Heavens), data compression, blinding, MCMC, nested sampling, NUTS, convergence, priors and projection or prior-volume effects, profile likelihood, Feldman–Cousins, Bayes factor, AIC/BIC/DIC, Δχ² to σ, tension metrics, Fisher forecasts, emulator error, simulation-based inference coverage, look-elsewhere effect.
---

# Statistics and inference in cosmology — expert reference

Snapshot 2026-10-07. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map

| Question | Load |
|---|---|
| A method, its formula, its reference paper, codes | `references/physics-and-methods.md` |
| How DESI, DES, KiDS, ACT, SPT, Planck, Euclid do it; priors side by side | `references/surveys-and-data.md` |
| Sizes of corrections, documented shifts, Δχ² against evidence, metric differences | `references/results.md` |
| Failure modes, one per section; referee checklist | `references/systematics.md` |
| Method debates, misconceptions table, not verified | `references/open-questions.md` |
| Bibliography with roles | `references/sources.tsv` |

## What an expert holds in mind

- The Hartlap factor fixes the precision bias only; best-fit scatter needs a second factor. With 1000 mocks and 10 parameters, the best-fit scatter grows by 5% in error bar for 100 data points and 29% for 400 (Dodelson–Schneider variance factors 1.10, 1.65); a posterior built on the raw sample covariance must be widened by 10% and 65%, Hartlap term included (arXiv:2108.10402, arXiv:1304.2593).
- A Gaussian likelihood takes a covariance fixed in parameter space (arXiv:1204.4724); likelihood non-Gaussianity moved BOSS fσ8 by −0.44σ (arXiv:1803.06348).
- Posterior mean and best fit separate in extended models: up to 6.6σ for DESI DR1 full shape in w0waCDM (arXiv:2508.11811); 1σ to 2σ in BOSS depending on the EFT prior (arXiv:2208.05929).
- DES Y6 pre-registered its projection test, with pulls below 0.5σ in ΛCDM (arXiv:2601.14559); KiDS-Legacy reports mean, mode and MAP side by side (arXiv:2503.19441).
- Profile likelihoods are prior-free, not assumption-free: Wilks holds for ΛCDM, needs Feldman–Cousins for Σm_ν, is doubtful for w0 (arXiv:2408.07700).
- DESI's σ is `Δχ²_MAP` with 2 degrees of freedom: −12.5 gives 3.1σ, `Δ(DIC) = −8.7` (arXiv:2503.14738). The same data give `ln B = −0.57 ± 0.26` (arXiv:2511.10631).
- The Bayes ratio scales with prior volume; parameter differences, suspiciousness and eigentension agree (arXiv:2012.09554, arXiv:1902.04029).
- A tension needs metric, subspace and reference: DES Y6 against the CMB is 1.8σ full-space, 2.6σ in S8 (arXiv:2601.14559); CMB against DESI DR2 is 1.6σ for ACT, 2.8σ for SPT (arXiv:2503.14452, arXiv:2506.20707).
- MultiNest gave narrower intervals and inconsistent evidences on the DES Y1 likelihood (arXiv:2202.08233); DES Y6 and KiDS-Legacy use Nautilus (arXiv:2306.16923).
- Simulation-based inference inflates variance at least as much as a mock covariance (arXiv:2412.02311); passing coverage is not validation (arXiv:2605.00980).
- Emulator accuracies (0.4%, arXiv:2106.03846; 1% dark-matter-only, arXiv:2010.11288) are interpolation errors; emulator error can miscalibrate a Gaussian likelihood (arXiv:2607.17942).
- Fisher forecasts underestimate w0–wa errors from geometrical probes by 30%–70% (arXiv:1205.3984).
- Blinding levels differ: catalogue (DESI, arXiv:2404.07282), data vector (DES, arXiv:1911.05929), three catalogues (KiDS). ACT DR6 and DES Y6 publish criteria and deviations (arXiv:2503.14452).
- The trial factor equals the prior-to-posterior volume ratio (arXiv:2007.13821).

## Systematics a referee checks

Covariance source, mock count against data-vector length, which correction;
likelihood form; prior ranges and posteriors at prior edges; mean, mode or
MAP, with the projection effect measured on synthetic data in each model;
boundary treatment of limits; sampler, convergence, best-fit search; `Δχ²`
with its degrees of freedom; Bayes factor with its priors; tension metric,
subspace and reference fixed in advance; independence of combined data;
emulator range and error propagation; coverage plus a fixed-parameter test;
blinding level and post-unblinding changes. Details:
`references/systematics.md` §17.

## Errors that recur

- "Hartlap-corrected" presented as the full treatment of mock noise.
- `sqrt(Δχ²)` quoted as σ for two extra parameters.
- A `Δχ²` significance described as Bayesian evidence, or the reverse.
- "The tension is nσ" without metric and reference; adding errors in quadrature for correlated data.
- The posterior mean of an extended-model full-shape fit read as the preferred value.
- A truncated-posterior width near a boundary read as sensitivity.
- A coverage plot, or a Fisher forecast, offered as validation of an error bar.
- Counting supernova compilations, or two releases of one survey, as independent.
- Citing a 1% emulator as a 1% theory error.

## Related skills

- `cosmo-galaxy-clustering`: DESI full-shape priors, covariance, blinding.
- `cosmo-dark-energy-modified-gravity`: w0wa significances and critiques.
- `cosmo-weak-lensing`: S8 values, shear blinding, HSC.
- `cosmo-beyond-two-point`: simulation-based and field-level analyses.
- `cosmo-neutrinos-dark-matter`: boundary effects for Σm_ν.
- `cosmo-tensions-anomalies`: cross-probe tension values, CMB anomalies.
- `cosmo-cmb`, `cosmo-supernovae`: Planck likelihoods; hierarchical models.
- `cosmo-simulations-mocks`, `cosmo-software-ecosystem`: mocks; codes.
- `observational-cosmology`: hub.
