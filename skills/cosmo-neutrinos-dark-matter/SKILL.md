---
name: cosmo-neutrinos-dark-matter
description: Use when reviewing, planning or fact-checking cosmological neutrino or dark-matter-property claims — sum of neutrino masses from DESI, ACT, SPT or Planck, negative or effective neutrino mass, mass ordering, tau or A_lens dependence, N_eff, dark radiation, BBN, KATRIN, JUNO, double beta decay; warm, fuzzy, interacting, self-interacting or decaying dark matter limits from Lyα forest, Milky Way satellites, strong lensing, streams, UV luminosity functions, clusters; sterile neutrinos.
---

# Neutrinos, light relics and dark-matter properties — expert reference

Snapshot 2026-10-07. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map

| Question | Load |
|---|---|
| Neutrino channels, effective-mass definitions, statistics, half-mode scale, probes, codes, conventions | `references/physics-and-methods.md` |
| Which release enters which bound, laboratory experiments, small-scale samples, next data | `references/surveys-and-data.md` |
| Σm_ν, N_eff, BBN, WDM, FDM, interacting, SIDM, decay tables; history | `references/results.md` |
| What moves each bound, sizes, tests, referee checklist | `references/systematics.md` |
| Controversies, forecasts, stale claims, not verified | `references/open-questions.md` |
| Bibliography with roles | `references/sources.tsv` |

## What an expert holds in mind

- DESI DR2 BAO + CMB: Σm_ν < 0.0642 eV (95%) in ΛCDM, < 0.163 eV in
  w0waCDM, 0.0691–0.0774 eV with other Planck likelihoods (arXiv:2503.14744).
- One data set, three widths: 0.020 eV (truncated posterior), 0.043 eV
  (profile), 0.053 eV (effective mass). Only the last two measure
  sensitivity (arXiv:2503.14744).
- The effective mass is −0.101 (+0.047/−0.056) eV, 3σ below the oscillation
  minimum (0.059 eV normal, 0.10 eV inverted). The tension vanishes in
  w0waCDM, with free lensing amplitudes, or with τ ≈ 0.09
  (arXiv:2407.10965, arXiv:2511.01967, arXiv:2504.16932).
- The bound is geometric: with BOSS BAO instead of DESI it is 0.13 eV,
  without BAO 0.23 eV. ACT's P-ACT-LB limit is 0.089 eV in the text, 0.082
  in the abstract (arXiv:2503.14454, arXiv:2410.00090).
- τ: doubling its error gives 0.10 eV; removing low-ℓ polarisation gives
  0.19 eV (arXiv:2503.14454).
- Ordering: Bayes factor 10 (DESI), 46.5 or above 460 with other priors
  (arXiv:2407.18047, arXiv:2606.18987). Oscillations alone are undecided
  (arXiv:2410.05380); JUNO favours normal at ≥ 2.1σ (arXiv:2609.37895).
- Laboratory: KATRIN m_ν < 0.45 eV at 90% CL (arXiv:2406.13516);
  KamLAND-Zen m_ββ < 28–122 meV (arXiv:2406.11438). Neither is Σm_ν.
- N_eff: standard 3.044 (arXiv:2008.01074). CMB-only values lie below
  (ACT 2.60, CMB-SPA 2.82 ± 0.12), values with DESI above (3.23 ± 0.18)
  (arXiv:2503.14454, arXiv:2506.20707, arXiv:2503.14744). BBN + CMB: 2.925 ± 0.082 (arXiv:2601.22239).
- Thermal-relic WDM: Lyα 1.9–5.7 keV with the thermal prior
  (arXiv:1912.09397, arXiv:2309.04533); satellites 6.5 keV
  (arXiv:2008.00022); JWST lensing 5.6–7.4 keV with data and subhalo prior
  (arXiv:2511.07765, arXiv:2511.07513).
- Fuzzy dark matter at 10⁻²² eV is excluded as all of the dark matter; Lyα
  limits span 1.9 × 10⁻²¹ to 2 × 10⁻²⁰ eV (arXiv:2606.06969,
  arXiv:2007.12705).
- Self-interaction: below 0.13–0.47 cm²/g on cluster scales
  (arXiv:2012.06611, arXiv:1503.07675); velocity-dependent models survive
  (arXiv:2006.12515).
- Forecasts: Simons Observatory σ(Σm_ν) = 0.03 eV, 0.015 eV with LiteBIRD,
  σ(N_eff) = 0.045 (arXiv:2503.00636); Euclid + Planck 23 meV
  (arXiv:2405.06047). CMB-S4 is cancelled (`cosmo-cmb`).
- Limits below DESI's own are external analyses: 0.049 eV from an EFT
  reanalysis (arXiv:2601.16165), 0.043 eV from Planck + DESI DR1 BAO with
  supernovae, GRBs, chronometers and clusters (arXiv:2405.03368).

## Systematics a referee checks

Model and number of massive states; Planck likelihood, lensing data, BAO
release, supernova sample; τ prior and the limit without low-ℓ EE; a
boundary-free statement next to the Bayesian limit; width change against
shift; CMB–BAO consistency; mass prior for ordering claims; N_eff free-streaming or fluid, Y_P, BBN rates. For dark matter:
production mechanism, half-mode conversion and confidence criterion;
thermal-history family and k_max; LMC analogue, Milky Way mass, disruption;
subhalo-abundance prior and multipoles; shared inputs of combined limits;
velocity of a σ/m limit. Details: `references/systematics.md`.

## Errors that recur

- Quoting 0.064 eV without "ΛCDM".
- Reading σ = 0.020 eV as DESI's sensitivity, or the forecast as met.
- Saying cosmology measured a negative mass, or established the ordering.
- Attributing the bound to growth suppression, or to BAO alone.
- Quoting KATRIN at 95%, or as a limit on Σm_ν.
- Writing N_eff = 3.046 as the current standard value (it is 3.044; 3.046
  is correct only when describing the Planck 2013 or 2018 baseline), or
  mixing N_ν (baseline 3) with N_eff.
- Citing CMB-S4 targets, or Euclid's 4σ, as upcoming.
- A WDM limit without thermal prior, k_max or criterion; 9.7 keV as current.
- Transferring a thermal-relic mass to sterile neutrinos or scattering models.
- A self-interaction limit without velocity; the Bullet Cluster 68% limit
  quoted as 95%.

## Related skills

- `cosmo-cmb`: τ, A_lens, lensing, N_eff data, facility status.
- `cosmo-galaxy-clustering`: DESI BAO and full shape.
- `cosmo-lyman-alpha`: P1D data, thermal state, emulators.
- `cosmo-dark-energy-modified-gravity`, `cosmo-supernovae`: w0wa and the
  supernova samples.
- `cosmo-weak-lensing`, `cosmo-clusters`, `cosmo-distance-ladder-h0`:
  S8, cluster data, BAO + BBN.
- `cosmo-reionization-21cm`, `cosmo-simulations-mocks`: reionisation,
  small-scale simulations.
