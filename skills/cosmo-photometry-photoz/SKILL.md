---
name: cosmo-photometry-photoz
description: Use when reviewing, planning or fact-checking photometric calibration or photometric redshifts - ubercal, FGCM, CALSPEC, Gaia XP standards, chromatic corrections, dust maps (SFD, CSFD), template fitting (BPZ, LePhare, EAZY), machine-learning photo-z, p(z) storage, n(z) calibration (SOM, clustering redshifts, shear ratio, forward models), spectroscopic training samples (C3R2, DESI-Deep), photo-z challenges, LSST and Euclid requirements, COSMOS, PAUS, SPHEREx.
---

# Photometry and photometric redshifts — expert reference

Snapshot 2026-10-16. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Methods: calibration, templates, ML, hierarchical models, SOM, clustering redshifts, PDFs, codes | `references/physics-and-methods.md` |
| Standards, survey photo-z products, many-band fields, training spectra, what comes next | `references/surveys-and-data.md` |
| Calibration precision, photo-z scatter, n(z) accuracy, challenges, requirements, history | `references/results.md` |
| Size of a systematic; referee checklist | `references/systematics.md` |
| Debates, stale claims, what Rubin, Euclid, DESI and SPHEREx will decide | `references/open-questions.md` |
| Building and validating a forward-model or hierarchical n(z) | `deep/population-forward-models.md` |
| Narrow-band photo-z: line templates, zero points, PDF fixes; template fitting in general | `deep/narrow-many-band-photometry.md` |
| Running ubercal or FGCM; uniformity tests; XP or SCR standards | `deep/photometric-calibration.md` |
| Setting up and validating a training-based (ML) photo-z | `deep/machine-learning-photoz.md` |
| Passband extinction coefficients; dust-map choice and its cost | `deep/chromatic-extinction.md` |
| Clustering redshifts (WZ) and their combination with SOM n(z) | `deep/clustering-redshifts-shear-ratio.md` |
| Title, first author, year of a cited paper | `references/sources.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Cosmology needs **characterisation** of n(z), not per-galaxy precision; the
  LSST DESC requirement on the source-bin mean is δz < 0.001(1+z) at year
  10, 0.002(1+z) as the year-1 goal (arXiv:1809.01669, Sect. 5.2), Euclid's
  0.002(1+z) (arXiv:2208.10503).
- DES Y6 FGCM stars are uniform to < 1.8 mmag RMS, but the absolute scale is
  known only to ~1% through CALSPEC (arXiv:2305.01695).
- Gaia XP and stellar colour regression exposed 15–23 mmag zero-point
  errors in released surveys (arXiv:2309.11225, arXiv:2309.11533).
- Chromatic errors reach 2% before correction, < 0.3% after
  (arXiv:1601.00117); angle-dependent filter shifts bias off-axis photo-z
  high (arXiv:2310.14716).
- SFD is 14% too high in normalisation (arXiv:1012.4804) and nine of ten
  dust maps carry extragalactic structure (arXiv:1808.03294); DESI stellar
  reddening differs from SFD by up to 80 mmag (arXiv:2409.05140).
- Stacked posteriors are a biased n(z); posteriors under implicit priors
  cannot be used for inference (arXiv:2007.12178).
- DES Y6 source σ⟨z⟩ = 0.012, 0.008, 0.009, 0.024, dominated by missing
  faint spectra (arXiv:2510.23566).
- One wrong spectroscopic redshift per thousand already strains LSST's
  width tolerance; current Q = 3 failure rates are 0.75–1%
  (arXiv:2206.13633, Sect. 4.2.2).
- Spectroscopic selection biases direct calibration by Δz = 0.005–0.05
  (arXiv:2003.10454).
- Two population models change KiDS-1000 edge-bin means by Δz ~ 0.05–0.1
  (arXiv:2602.03935): forward modelling moves the risk to the prior.
- DESI calibrates DES, HSC and KiDS together to σ_z̄ ~ 0.01, disagreeing with
  the KiDS-1000 means (arXiv:2510.25419).
- Euclid mocks: binning on SOM-cell spec-z meets the requirement in no bin,
  on photo-z in eight of ten (arXiv:2508.02779).
- Several machine-learning codes give good point estimates but useless PDFs
  (arXiv:2009.12112).
- Rubin DP1: σ_NMAD 0.028–0.055, 12–20% outliers (arXiv:2510.07370); Euclid Q1
  photo-z still need a bias correction (arXiv:2503.15306).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

1. Calibration uniformity with an external check; absolute tie stated.
2. Dust map and coefficients; result under a second map.
3. Passband variation across the focal plane and in time.
4. Training set or templates, and the prior they imply.
5. Calibration-sample completeness, redshift-quality cut, number of fields.
6. Two independent n(z) calibrations compared per bin.
7. n(z) uncertainty model (shifts, modes, ensembles).
8. Blending in photometry, spectra and shear selection.
9. Clustering redshifts: scales, bias evolution, magnification.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting photo-z scatter σ_z where the requirement concerns the mean of n(z).
- Comparing σ_NMAD, σ_68 and RMS, or outlier rates with different thresholds
  and depths, as if equivalent.
- Writing "1% calibration" for relative uniformity, which is now mmag.
- Using SFD E(B−V) without the recalibrated coefficients.
- Treating COSMOS many-band photo-z as truth: outliers exceed 10% for faint
  star-forming galaxies in COSMOS2015 (arXiv:2206.13633, Sect. 4.2.2).
- Citing one LSST number without its context: the SRD mean-z requirement
  is 0.001(1+z) for year-10 lensing, 0.002(1+z) for year 1, 0.003(1+z) for
  year-10 clustering (arXiv:1809.01669, Sect. 5.1–5.2).
- Summing per-galaxy posteriors to get n(z).

## Related skills
<!-- key: related-skills -->

- `cosmo-weak-lensing`: each survey's n(z) priors and their effect on S8.
- `cosmo-galaxy-clustering`: spectroscopic samples used as references.
- `cosmo-supernovae`: supernova photometric calibration.
- `cosmo-clusters`: photometric cluster redshifts.
- `cosmo-data-pipelines`: imaging pipelines, masks, systematics weights.
- `cosmo-machine-learning`: ML methods beyond photo-z.
- `cosmo-surveys-facilities`: release dates and instrument facts.

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

Sizes, in thousands of tokens: L1 3k; open 4k; methods 10k; results 6k; surveys 5k; systematics 5k; deep/chromatic-extinction 7k; deep/clustering-redshifts-shear-ratio 7k; deep/machine-learning-photoz 8k; deep/narrow-many-band-photometry 8k; deep/photometric-calibration 7k; deep/population-forward-models 9k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-photometry-photoz`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-photometry-photoz/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
