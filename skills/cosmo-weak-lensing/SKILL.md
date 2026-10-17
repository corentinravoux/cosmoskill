---
name: cosmo-weak-lensing
description: Use when reviewing, planning or fact-checking cosmic shear, galaxy-galaxy lensing, 3x2pt or 6x2pt work - S8 values and the S8 tension, shear calibration (metacalibration, metadetection, lensfit), PSF, blending, photo-z calibration (SOM, clustering redshifts, shear ratio), intrinsic alignments (NLA, TATT), baryonic feedback, xi+/-, COSEBIs, pseudo-Cl, covariance, blinding; surveys CFHTLenS, KiDS, DES, HSC, DECADE, UNIONS, Euclid, Rubin LSST, Roman.
---

# Weak lensing — expert reference

Snapshot 2026-10-12. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Current S8 from survey X, its model, what it superseded | `references/results.md` |
| Is the S8 tension resolved; who disagrees; stale claims | `references/open-questions.md` |
| Size of a systematic; what a referee asks | `references/systematics.md` |
| Estimators, statistics, theory model, covariance, blinding, codes, conventions | `references/physics-and-methods.md` |
| Area, density, release status; Euclid, Rubin, Roman today | `references/surveys-and-data.md` |
| Title, first author, year of a cited paper | `references/sources.tsv` |
| Making m and its prior: metacalibration, metadetection, image simulations | `deep/shear-calibration.md` |
| Choosing an IA model; building its priors | `deep/intrinsic-alignments.md` |
| Setting baryon scale cuts or a feedback model; emulators | `deep/baryonic-feedback.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- KiDS-Legacy cosmic shear: S8 = 0.815 +0.016/−0.021 (marginal mode), 0.73σ from Planck in Σ8, 0.74–0.76σ in S8; the rise from KiDS-1000 (0.759) is attributed mainly to redshift calibration (arXiv:2503.19441).
- DES Y6 cosmic shear: 0.798 +0.014/−0.015 with NLA, 0.783 +0.019/−0.015 with TATT; 2.0σ and 2.3σ in S8 from Planck + ACT DR6 + SPT-3G (arXiv:2602.10065).
- DES Y6 3×2pt: S8 = 0.789 ± 0.012, 2.6σ in S8 but 1.8σ in the full parameter space (arXiv:2601.14559). Reduced, not gone; metric-dependent.
- HSC Y3 moves from 0.769 to 0.804 +0.019/−0.018 with DESI clustering redshifts (arXiv:2511.18134); metacalibration on KiDS-1000 changes nothing (arXiv:2510.01122). Redshifts, not shapes, drove the old lows.
- CMB references differ: KiDS Planck alone (0.834 ± 0.016), DES Planck + ACT + SPT (0.836 +0.012/−0.013), same centre, tighter; against Planck 2018 alone the DES Y6 3×2pt full-parameter difference is 1.0σ (arXiv:2601.14559, arXiv:2602.12238).
- IA model choice: 0.6σ in S8 between NLA and TATT, about 1σ in the S8–Ωm plane across variants (arXiv:2602.10065); the bluest galaxies show no detectable alignment (arXiv:2507.11530).
- Baryonic feedback strength is disputed: kSZ, X-ray, tSZ and the KiDS-Legacy P(k) favour strong suppression (arXiv:2609.09144, arXiv:2509.08365, arXiv:2506.07432); DES Y3 6×2pt favours weak (arXiv:2510.25596).
- External IA and baryon calibration moves DES Y3 to 0.832 +0.013/−0.017 (arXiv:2512.04209).
- Scale cuts saturate: all scales plus a free baryon model gain almost nothing (arXiv:2509.03582); LSST year 10 barely beats year 1 without better baryon and redshift priors (arXiv:2602.21863, forecast).
- Mean and MAP of S8 differ through projection effects: 0.790 vs 0.801 in DES Y3 + KiDS-1000 (arXiv:2305.17173).
- No Stage-IV cosmic-shear cosmology exists. Euclid DR1 lensing products: mid-2027. Rubin LSST began 30 June 2026; Roman launched 30 August 2026.
- UNIONS-3500: first results non-tomographic, S8 error about ±0.07 (arXiv:2605.13547).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

1. Redshift calibration: two independent methods, agreement per bin.
2. Shear calibration m per bin, with blending.
3. PSF leakage; B-mode null tests in more than one statistic.
4. IA model and priors; shift of S8 under the alternative.
5. Baryons: cuts or model, prior, residual bias.
6. Covariance construction; goodness of fit.
7. Blinding level and post-unblinding changes.
8. Projection effects on the point estimate.
9. CMB data set and tension metric.
10. Magnification and non-linear bias in galaxy–galaxy lensing.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting "S8 ≈ 0.76, 2–3σ below Planck" as current; that is KiDS-1000 and DES Y3.
- Writing that the tension is "resolved" without the DES Y6 3×2pt figure.
- Citing 0.772 as the DES Y3 cosmic-shear result; it is the optimised-scale variant, the fiducial is 0.759 (arXiv:2105.13543).
- Citing CFHTLenS tomography σ8 = 0.799 as lensing-only; it includes WMAP7, BOSS, an H0 prior (arXiv:1303.1808).
- Treating November 2026 as the Euclid lensing release; it is DR1-Foundation.
- Comparing S8 values with different exponents (0.45, 0.5, 0.58), point estimates or CMB references.

## Related skills
<!-- key: related-skills -->

- `cosmo-beyond-two-point`: peaks, PDFs, third-order shear, field-level lensing.
- `cosmo-cmb-lss-cross-correlations`: CMB lensing × galaxies, kSZ, tSZ.
- `cosmo-tensions-anomalies`: S8 across all probes; tension metrics.
- `cosmo-clusters`: cluster lensing masses and cluster S8.
- `cosmo-dark-energy-modified-gravity`: Σ, μ, E_G, w0wa.
- `cosmo-statistics-inference`: covariance corrections, projection effects.
- `cosmo-simulations-mocks`, `cosmo-surveys-facilities`: simulations; instruments.

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

Sizes, in thousands of tokens: L1 2k; open 5k; methods 9k; results 7k; surveys 6k; systematics 14k; deep/baryonic-feedback 6k; deep/intrinsic-alignments 6k; deep/shear-calibration 8k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-weak-lensing`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-weak-lensing/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
