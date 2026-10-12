---
name: cosmo-distance-ladder-h0
description: Use when reviewing, planning or fact-checking Hubble-constant work — distance ladder, Cepheids, TRGB, JAGB, Miras, SBF, Tully-Fisher, Fundamental Plane, anchors (Gaia parallaxes, LMC/SMC eclipsing binaries, NGC 4258), SH0ES, CCHP, H0DN, megamasers, time-delay cosmography (H0LiCOW, TDCOSMO), lensed SNe, standard sirens, cosmic chronometers, inverse distance ladder, BAO+BBN, sound horizon, M_B prior, Hubble tension significance, local void, early dark energy.
---

# Distance ladder and H0 — expert reference

Snapshot 2026-10-07. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map

| Question | Load |
|---|---|
| Formalism, anchors, indicators, masers, time delays, inverse ladder, priors, selection, blinding | `references/physics-and-methods.md` |
| Programmes, samples, release dates | `references/surveys-and-data.md` |
| H0 by route, tension table, reanalyses, history | `references/results.md` |
| Each systematic; referee checklist | `references/systematics.md` |
| Controversies, forecasts, stale claims | `references/open-questions.md` |
| Bibliography | `references/sources.tsv` |

## What an expert holds in mind

- The ladder measures the SN Ia `M_B`; H0 follows from the SN Hubble-diagram
  intercept, so the ladder–CMB mismatch is insensitive to the late expansion
  history (arXiv:2103.08723, arXiv:2607.29562).
- Local values [src]: SH0ES 73.17 ± 0.86 (HST, four anchors,
  arXiv:2404.08038) and 73.18 ± 0.88 (plus JWST Cepheids and TRGB,
  arXiv:2509.01667); H0DN 73.50 ± 0.81 (arXiv:2510.23823).
  73.04 ± 1.04 (arXiv:2112.04510) is the last HST-only baseline.
- CCHP: 70.39 ± 1.22 (stat) ± 1.33 (sys) ± 0.70 (sigma_SN) [src], total 1.94
  [der] (arXiv:2408.06153).
- SH0ES and CCHP stellar distances agree at about 0.03 mag; the H0 gap sits
  in the SN calibrator subsample and SN compilation (arXiv:2408.11770,
  arXiv:2503.11769). The complete 35-calibrator TRGB sample gives 72.1 to
  73.3 ± 1.8 (arXiv:2504.08921).
- Both JWST ladders rest on NGC 4258 alone (arXiv:1908.05625) and share SN
  hosts.
- Early side, flat LCDM [src]: 67.4 ± 0.5 Planck 2018 (arXiv:1807.06209);
  66.66 ± 0.60 SPT-3G D1 and 67.19 ± 0.38 SPT + ACT + Planck
  (arXiv:2506.20707); 68.51 ± 0.58 DESI DR2 BAO + BBN, no CMB
  (arXiv:2503.14738).
- The tension is 4.4 to 7.1 sigma for the latest SH0ES and H0DN values,
  depending on the early endpoint [der]; name both endpoints.
- Time delays: 73.3 (+1.7/−1.8) assumed mass profiles (arXiv:1907.04869);
  with the mass-sheet degeneracy free, 71.6 (+3.9/−3.3) (arXiv:2506.03023).
- Megamasers: 73.9 ± 3.0 had no flow correction (arXiv:2001.09213); 2026
  reanalyses give 66.9 to 68.8 (arXiv:2608.06247) or 71.6 ± 3.7
  (arXiv:2609.17684).
- DESI DR1 FP + TF, 73.7 ± 0.06 ± 1.1, borrows the SH0ES/Pantheon+ zero
  point (arXiv:2512.03232).
- Volume priors give 70.6 ± 1.0 (arXiv:2601.22215); with selection modelled
  the Milky Way calibration is recovered within 0.5 sigma (arXiv:2603.09880);
  extragalactic selection stays open (arXiv:2607.22425).
- A late-time fix needs a step in `M_B` at z ~ 0.01 or broken distance
  duality (arXiv:2602.06293); SPT + ACT + Planck give f_EDE < 0.070 at 95%
  (arXiv:2507.23355).
- Gaia DR4 is planned for 2 December 2026; current values use EDR3/DR3.

## Systematics a referee checks

H0 from each anchor alone; Gaia parallax offset; Cepheid metallicity and
dust law; host selection and its place in the likelihood; SN compilation,
redshift cut and velocity model; calibrator sample size; distances compared
rather than H0 values; TRGB and JAGB statistic and zero point; for lenses,
free mass-sheet degeneracy, kinematics, Omega_m prior; for masers and
two-rung ladders, the velocity reconstruction. The gap to close is 0.176 ±
0.035 mag (arXiv:2112.04510).

## Errors that recur

- Offering Cepheid crowding as an explanation: HST − JWST is −0.01 ± 0.03
  mag, rejected at 8.2 sigma (arXiv:2401.04773).
- "The TRGB gives 69.8": the 2021 CCHP value (arXiv:2106.15656); no CATS
  variant falls below 71.6 (arXiv:2304.06693).
- "4.4 sigma" or "5 sigma" unqualified: the 2019 and 2022 figures against
  Planck 2018 (arXiv:1903.07603).
- "Planck is the outlier": SPT-3G alone and BAO + BBN are also low.
- Using the SH0ES H0 as a Gaussian prior: it double counts low-z SNe and
  fixes q0; use the `M_B` calibration (arXiv:2103.08723).
- A local void as the fix: direct distances limit it to under 70 Mpc
  (arXiv:2506.10518, arXiv:1901.08681).

## Related skills

- `cosmo-supernovae`: light-curve models, calibration, host corrections.
- `cosmo-peculiar-velocities`: flow reconstructions, DESI PV.
- `cosmo-cmb`, `cosmo-galaxy-clustering`: CMB and BAO inputs.
- `cosmo-tensions-anomalies`, `cosmo-dark-energy-modified-gravity`: models.
- `cosmo-multimessenger`: standard sirens.
