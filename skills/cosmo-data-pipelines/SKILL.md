---
name: cosmo-data-pipelines
description: Use when reviewing, planning or fact-checking how raw data become catalogues and maps - target selection, fibre assignment, altMTL, spectral extraction, sky subtraction, Redrock, redshift success, purity, visual inspection, ISR, brighter-fatter, astrometry, Piff, deblending, SCARLET, co-addition, Balrog, Obiwan, masks, randoms, imaging-systematics weights, CMB time-ordered data, map-making, transfer function, data-release known issues.
---

# Data pipelines — expert reference

Snapshot 2026-10-16. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Targeting/assignment, extraction/sky, redshifts, ISR/astrometry, PSF, deblending/co-addition, CMB maps, masks/randoms/weights, injection, releases | `references/physics-and-methods.md` |
| Survey pipelines, selections, DESI bookkeeping/weights, release content, codes, new pipelines | `references/surveys-and-data.md` |
| Success, purity, residuals, depths/completeness, map noise, supersession | `references/results.md` |
| Systematic sizes; referee checklist | `references/systematics.md` |
| Debates, release tensions, forecasts, stale claims | `references/open-questions.md` |
| Paper title, author, year | `references/sources.tsv` |
| Fitter settings, good-redshift cuts, VI/repeats, failure weights | `deep/redshift-fitting.md` |
| Vetoes, completeness, imaging weights, randoms | `deep/lss-catalogues.md` |
| Injection-run design | `deep/source-injection.md` |
| Spectrograph PSF, flats, sky PCA, standards, cross-talk | `deep/extraction-sky.md` |
| ISR, brighter-fatter kernels, tree rings, CTI | `deep/image-detrending.md` |
| CMB TOD cuts, noise model, filters, nulls | `deep/cmb-mapmaking.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- A success rate means nothing without its denominator, truth table and
  quality cut; DESI purities are against VI of deep co-adds
  (arXiv:2208.08516, arXiv:2208.08517).
- DESI DR1 redshift outliers: ≤ 0.3% for galaxies, 0.7% for quasars at
  z < 2.1, 1.8% above; sky residuals < 1% systematic (arXiv:2503.14745).
- Redrock alone misses quasars: ~86% of VI quasars against ~94% with
  after-burners (arXiv:2208.08517).
- Formal redshift errors are miscalibrated: BOSS low by 1.19–2
  (arXiv:1207.7326), redmonster high by ~54% (arXiv:1607.02432).
- Euclid Q1 gives every H_E < 22.5 source a redshift, but under 10% of
  spectra allow one; 89% success at 0.9 < z < 1.8 needs tuned cuts
  (arXiv:2503.15302, arXiv:2503.15308).
- DESI DR1 flux-calibration variances are underestimated, up to a factor 5
  at S/N ~ 100 per pixel; use zcatalog v1 (arXiv:2503.14745, Sect. II.2).
- In DESI, redshifts feed back into targeting, so the selection function
  depends on the pipeline version used in operations (arXiv:2306.06309).
- Random redshifts drawn from the data null radial modes
  (arXiv:2405.16593).
- Brighter-fatter grows star sizes by up to 2% and must be corrected at
  pixel level (arXiv:1402.0725, arXiv:1501.02802).
- Unrecognised blends are 18.0% of the Rubin DP1 catalogue against HST
  (arXiv:2610.10986); the HSC deblender fails in cluster cores
  (arXiv:1705.06766).
- Injection is now survey-wide: 146 million Balrog injections over DES Y6
  (arXiv:2501.05683, abstract).
- CMB map-maker model error can lose O(1) of large-scale power, invisible
  to simulations without that error (arXiv:2210.02243); ACT DR6 measures
  its transfer function by injection into real data (arXiv:2503.14451).
- Original template subtraction is biased; basic mode projection is not
  (arXiv:1509.08933).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

1. Reduction and code versions; known-issues list.
2. Parent imaging regions and masks of the target selection.
3. Fibre-assignment completeness and correction.
4. Redshift success: definition, truth table, condition dependence.
5. Redshift errors from repeats.
6. Sky residuals on OH lines against the noise model.
7. ISR effects modelled; astrometric and PSF residuals.
8. Deblender, blend fraction, injection test.
9. Vetoes, randoms, weights and survey-property maps.
10. Imaging weights validated on contaminated mocks.
11. CMB: data model, filtering, transfer function on data, null splits.

## Errors that recur
<!-- key: errors-that-recur -->

- Comparing success rates of different surveys without matching the
  denominator (targets, fibres, good-hardware fibres) or quality cut.
- Treating a design area, density or depth as delivered.
- Using Euclid Q1 or DESI v0 catalogues without the release caveats.
- Taking fitter redshift errors at face value.
- Validating a CMB map-maker only on simulations that share its data model.
- Treating weights from one imaging region as valid for another: DES-region
  ELGs in DESI DR2 have a different n(z) (arXiv:2606.18581).
- Building a co-add PSF from stars on the co-add.

## Related skills
<!-- key: related-skills -->

- `cosmo-surveys-facilities`: instruments, release dates, status.
- `cosmo-photometry-photoz`: photometric calibration, dust maps, photo-z,
  n(z) calibration.
- `cosmo-galaxy-clustering`: effect of fibre assignment, imaging weights
  and redshift failures on BAO, RSD, full shape and f_NL.
- `cosmo-weak-lensing`: PSF leakage, ρ statistics, blending in shear.
- `cosmo-cmb`: band powers, MASTER, likelihood ranges, foregrounds.
- `cosmo-lyman-alpha`: quasar spectra for the forest.
- `cosmo-software-ecosystem`: codes as software.
- `cosmo-statistics-inference`: blinding and covariance.

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

Sizes, in thousands of tokens: L1 3k; open 3k; methods 9k; results 4k; surveys 5k; systematics 5k; deep/cmb-mapmaking 8k; deep/extraction-sky 12k; deep/image-detrending 8k; deep/lss-catalogues 7k; deep/redshift-fitting 7k; deep/source-injection 8k.

- L2: when the file map names several files, search them for the term
  before reading, and read only the passage.
- L4 starts from the L2 entry: its citation and flag say where to look. Read
  the paper with
  `python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/fetch_paper.py" <arXiv id>`
  (`--abstract`, `--outline`, `--section`, `--grep`), or with any tool that
  gives the paper. If it cannot be read, say that L4 was required and not
  done.
- Quote a number only with its paper and the place it was read, as the
  skill gives them; the skill holds no number of its own making. A formula
  may be applied to the asker's numbers; label the result as derived.

Local layers: if a directory `.cosmoskill/` exists in the working directory,
in one of its parents, or in the home directory, or if `COSMOSKILL_HOME` is
set, run
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-data-pipelines`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-data-pipelines/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
