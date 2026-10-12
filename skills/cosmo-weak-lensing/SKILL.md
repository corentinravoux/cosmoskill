---
name: cosmo-weak-lensing
description: Use when reviewing, planning or fact-checking cosmic shear, galaxy-galaxy lensing, 3x2pt or 6x2pt work - S8 values and the S8 tension, shear calibration (metacalibration, metadetection, lensfit), PSF, blending, photo-z calibration (SOM, clustering redshifts, shear ratio), intrinsic alignments (NLA, TATT), baryonic feedback, xi+/-, COSEBIs, pseudo-Cl, covariance, blinding; surveys CFHTLenS, KiDS, DES, HSC, DECADE, UNIONS, Euclid, Rubin LSST, Roman.
---

# Weak lensing — expert reference

Snapshot 2026-10-07. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map

| Question | Load |
|---|---|
| Current S8 from survey X, its model, what it superseded | `references/results.md` |
| Is the S8 tension resolved; who disagrees; stale claims | `references/open-questions.md` |
| Size of a systematic; what a referee asks | `references/systematics.md` |
| Estimators, statistics, theory model, covariance, blinding, codes, conventions | `references/physics-and-methods.md` |
| Area, density, release status; Euclid, Rubin, Roman today | `references/surveys-and-data.md` |
| Title, first author, year of a cited paper | `references/sources.tsv` |

## What an expert holds in mind

- KiDS-Legacy cosmic shear: S8 = 0.815 +0.016/−0.021, 0.73σ from Planck; the rise from KiDS-1000 (0.759) is attributed mainly to redshift calibration (arXiv:2503.19441).
- DES Y6 cosmic shear: 0.798 +0.014/−0.015 with NLA, 0.783 +0.019/−0.015 with TATT; 2.0σ and 2.3σ in S8 from Planck + ACT DR6 + SPT-3G (arXiv:2602.10065).
- DES Y6 3×2pt: S8 = 0.789 ± 0.012, 2.6σ in S8 but 1.8σ in the full parameter space (arXiv:2601.14559). The tension is reduced, not gone, and depends on the metric.
- HSC Y3 moves from 0.769 to 0.804 +0.019/−0.018 with DESI clustering redshifts (arXiv:2511.18134); metacalibration on KiDS-1000 changes nothing (arXiv:2510.01122). Redshifts, not shapes, drove the old low values.
- Quoted tensions do not share a CMB reference: KiDS uses Planck alone, DES the tighter, higher three-experiment combination (arXiv:2602.12238).
- IA model choice is worth up to 1σ in S8 (arXiv:2602.10065); the bluest galaxies show no detectable alignment (arXiv:2507.11530).
- Baryonic feedback strength is disputed: kSZ, X-ray, tSZ and the KiDS-Legacy P(k) favour strong suppression (arXiv:2609.09144, arXiv:2509.08365, arXiv:2506.07432); DES Y3 6×2pt favours weak (arXiv:2510.25596).
- External IA and baryon calibration moves DES Y3 to 0.832 +0.013/−0.017 (arXiv:2512.04209).
- Scale cuts saturate: all scales with a free baryon model gain almost nothing (arXiv:2509.03582); LSST year 10 barely beats year 1 without better baryon and redshift priors (arXiv:2602.21863, forecast).
- Mean and MAP of S8 differ through projection effects: 0.790 against 0.801 in DES Y3 + KiDS-1000 (arXiv:2305.17173).
- No Stage-IV cosmic-shear cosmology exists. Euclid DR1 lensing products: mid-2027. Rubin LSST began 30 June 2026; Roman launched 30 August 2026.
- UNIONS-3500: first results non-tomographic, S8 error about ±0.07 (arXiv:2605.13547).

## Systematics a referee checks

1. Redshift calibration: two independent methods, agreement per bin.
2. Shear calibration m per bin, with blending.
3. PSF leakage and B-mode null tests, in more than one statistic.
4. IA model and priors; shift of S8 under the alternative model.
5. Baryons: scale cuts or model, the prior, the residual bias.
6. Covariance construction and goodness of fit.
7. Blinding level and post-unblinding changes.
8. Projection effects on the quoted point estimate.
9. Which CMB data set and which tension metric.
10. Magnification and non-linear bias in galaxy–galaxy lensing.

## Errors that recur

- Quoting "S8 ≈ 0.76, 2–3σ below Planck" as current; that is KiDS-1000 and DES Y3.
- Writing that the tension is "resolved" without the DES Y6 3×2pt figure.
- Citing 0.772 as the DES Y3 cosmic-shear result; it is the optimised-scale variant, the fiducial is 0.759 (arXiv:2105.13543).
- Citing CFHTLenS tomography σ8 = 0.799 as lensing-only; it includes WMAP7, BOSS and an H0 prior (arXiv:1303.1808).
- Treating November 2026 as the Euclid lensing release; it is DR1-Foundation.
- Comparing S8 values with different exponents (0.45, 0.5, 0.58), point estimates or CMB references.

## Related skills

- `cosmo-beyond-two-point`: peaks, PDFs, third-order shear, field-level lensing.
- `cosmo-cmb-lss-cross-correlations`: CMB lensing × galaxies, kSZ, tSZ.
- `cosmo-tensions-anomalies`: S8 across all probes; tension metrics.
- `cosmo-clusters`: cluster lensing masses and cluster S8.
- `cosmo-dark-energy-modified-gravity`: Σ, μ, E_G, w0wa.
- `cosmo-statistics-inference`: covariance corrections, projection effects.
- `cosmo-simulations-mocks`, `cosmo-surveys-facilities`: simulations; instruments.
