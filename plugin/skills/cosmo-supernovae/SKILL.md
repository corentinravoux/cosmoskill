---
name: cosmo-supernovae
description: Use when reviewing, planning or fact-checking Type Ia supernova cosmology — Hubble diagram, distance modulus, SALT2/SALT3, BayeSN, stretch and colour standardisation, host mass step, BBC/BEAMS bias corrections, photometric classification, UNITY, calibration (Fragilistic, Dovekie), low-redshift anchor, Pantheon+, Union3/3.1, DES-SN5YR, DES-Dovekie, Unite, ZTF SN Ia DR2, DEBASS, Rubin and Roman supernovae, SN sample choice in w0wa fits, lensed SNe, SNe II, siblings.
---

# Type Ia supernova cosmology — expert reference

Snapshot 2026-10-13. Every number names its paper and the place it was
read ([src: <place>] / [sec: <place>]); no number is derived by an agent.
Re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Standardisation, SALT/BayeSN, scatter models, BBC, BEAMS, UNITY, covariance, redshift corrections, calibration chain, blinding, codes | `references/physics-and-methods.md` |
| Surveys, compilations, sample sizes, what is superseded, data locations, Rubin/Roman, SNe II, lensed SNe, siblings | `references/surveys-and-data.md` |
| Current `Omega_m`, `w`, `w0`–`w_a` per sample; history; mass step | `references/results.md` |
| Size, mitigation and test of each systematic; referee checklist | `references/systematics.md` |
| Controversies, method debates, forecasts, stale claims | `references/open-questions.md` |
| How the dust/scatter model is fitted, simulated, propagated; choice | `deep/dust-intrinsic-scatter.md` |
| How SALT is trained, fitted; training-calibration errors; SALT or BayeSN | `deep/light-curve-models.md` |
| How bias-correction simulations and BBC are built, validated; alternatives | `deep/selection-bias-corrections.md` |
| Covariances, `M` marginalisation, significance, unblinding | `deep/covariance-likelihood-blinding.md` |
| Cross-calibration fit, validation | `deep/photometric-calibration.md` |
| Photo-z, classifier calibration, photometric Rubin/Roman Hubble diagrams | `deep/stage-iv-photometric-samples.md` |
| Bibliography | `references/sources.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- An unanchored SN Hubble diagram measures the shape of `d_L(z)` only; `M`
  and `H0` are degenerate. SN-only fits constrain `Omega_m` (LCDM) or a
  `q0`-like combination, never `w_a` (arXiv:2511.07517, arXiv:2609.05053).
- Current samples: **Unite** (2884 SNe, Pantheon+ ∪ DES, arXiv:2609.05053, abstract),
  **DES-Dovekie** (arXiv:2511.07517), **Union3.1** (arXiv:2601.19424).
  DES-SN5YR and Union3 are superseded; Pantheon+ (arXiv:2202.04077) stands
  with revised host masses.
- Flat-LCDM `Omega_m` from SNe alone: 0.310 (+0.012/−0.011) Unite, 0.330 ±
  0.015 DES-Dovekie, 0.344 (+0.026/−0.025) Union3.1 [src: abstract of
  arXiv:2609.05053, arXiv:2511.07517 and arXiv:2601.19424].
- The DESI DR2 significances of 2.8 / 3.8 / 4.2 sigma for Pantheon+ / Union3
  / DESY5 (arXiv:2503.14738) became 3.2 / 3.4 / 3.4 sigma after two fixes
  (arXiv:2601.19424, abstract, which gives all six values); Unite gives 3.3
  sigma with "weak" Bayesian evidence (arXiv:2609.05053, abstract).
  DES-Dovekie is 3.2 sigma in its own paper, with Planck + ACT + SPT as the
  CMB (arXiv:2511.07517, abstract), and 3.4 sigma in the DESI-style
  recomputation.
- The two fixes: Dovekie recalibration plus a colour-law implementation
  error in DES (arXiv:2511.07517), and inconsistent host masses between low
  and high redshift (arXiv:2601.19424, arXiv:2609.05321).
- The compilations share most low-z supernovae; they are not independent.
- The low-z anchor controls the result: cutting all z < 0.1 SNe (687, 24 %
  of Unite) is the only cut that shifts the Unite best fit substantially,
  by ~2 sigma (arXiv:2609.05053, Sect. 9.1). No analysis yet uses a modern
  anchor; DEBASS, ZTF and TITAN are pending (arXiv:2508.10877).
- ZTF SN Ia DR2 is not cosmology-grade by its authors' own statement
  (arXiv:2409.04346, arXiv:2509.04073).
- Calibration and model training are coupled; small zero-point shifts are
  amplified up to sixfold in distance (arXiv:2112.03864, arXiv:2506.05471).
- The residual mass step depends on bias-correction dimensionality, scatter
  model, tracer and stretch linearity: 0.040 ± 0.019 (5D) against 0.066 ±
  0.020 (1D) on the same DES-SN3YR SNe (arXiv:2001.11294, abstract); ~0.17 ±
  0.01 with non-linear stretch on ZTF DR2 (arXiv:2405.20965, abstract). Its
  origin is disputed (arXiv:2004.10206 vs arXiv:2605.06799).
- Bias-corrected distances of the same SN differ between analyses with
  different selection functions (arXiv:2501.06664).
- Unbinned covariances cut the systematic error by ~1.5
  (arXiv:2012.05900, abstract); one-at-a-time budget rows do not add in quadrature.
  Largest terms: redshift bias (Pantheon+), calibration and dust (DES),
  `M_B` and peculiar velocities (Union3).
- Only BBC and UNITY have produced cosmology from data; SBI results are on
  simulations (arXiv:2603.11165).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

Cross-calibration and SALT training on one solution; selection-bias
simulations with their population and scatter models; host step, its tracer
and host-mass consistency across redshift; evolution of `alpha`, `beta`,
`gamma`; contamination and host mismatch; peculiar velocities and the low-z
cut; Milky Way extinction; lensing; anchor heterogeneity; tension metric
before combining probes. Sizes in `references/systematics.md`.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting 4.2 sigma (DESY5) or `Omega_m = 0.352` after November 2025
  (arXiv:2511.07517, abstract).
- Saying Pantheon+ "shows no signal": true of the 2022 release, not after the
  host-mass correction.
- Treating Pantheon+, Union3 and DES as three independent confirmations.
- Reading SN-only `w_a ≈ −8` as a measurement; it is a prior-volume effect.
- Comparing a frequentist `Delta chi2` significance with a Bayes factor, or
  FoM values under different definitions (factor 19.4, arXiv:2311.12098,
  Sect. V.3).
- Comparing object-by-object distance moduli across compilations as a null
  test.
- Using ZTF DR2 light curves for cosmological parameters.
- Citing the "non-accelerating universe" age-bias claim (arXiv:2510.13121)
  without its rebuttals (arXiv:2601.13785, arXiv:2604.16597).
- Mixing `z_hel`, `z_CMB` and `z_HD` in `d_L` (arXiv:1907.12639).

## Related skills
<!-- key: related-skills -->

- `cosmo-distance-ladder-h0`: SN absolute calibration, SH0ES/CCHP, SN II and
  lensed-SN `H0`.
- `cosmo-peculiar-velocities`: SNe as velocity tracers, `f sigma8`.
- `cosmo-dark-energy-modified-gravity`: interpretation of `w0`–`w_a`.
- `cosmo-tensions-anomalies`: cross-probe inconsistency, SN dipoles.
- `cosmo-statistics-inference`: tension metrics, evidence, covariances.
- `cosmo-surveys-facilities`: Rubin, Roman, ZTF instrument facts.

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

Sizes, in thousands of tokens: L1 3k; open 7k; methods 13k; results 7k; surveys 7k; systematics 10k; deep/covariance-likelihood-blinding 8k; deep/dust-intrinsic-scatter 8k; deep/light-curve-models 8k; deep/photometric-calibration 7k; deep/selection-bias-corrections 7k; deep/stage-iv-photometric-samples 6k.

- L2: when the file map names several files, search them for the term
  before reading, and read only the passage.
- L4 starts from the L2 entry: its citation and flag say where to look. Read
  the paper with
  `python3 "${CLAUDE_SKILL_DIR}"/../*observational-cosmology/scripts/fetch_paper.py <arXiv id>`
  (`--abstract`, `--outline`, `--section`, `--grep`). `${CLAUDE_SKILL_DIR}` is
  the folder of this file; if it reaches you unexpanded, write that folder's
  path in its place. If the script cannot run, or reports that arXiv cannot
  be reached, do not run it again: read `https://arxiv.org/abs/<id>` or
  `https://arxiv.org/html/<id>` with a web tool if you have one. If the paper
  cannot be read, say that L4 was required and not done; never give its
  content from memory.
- Quote a number only with its paper and the place it was read, or, for a
  code or facility fact, its `[doc]` page and read date, as the skill gives
  them; the skill holds no number of its own making. A formula
  may be applied to the asker's numbers; label the result as derived.

Local layers: if a directory `.cosmoskill/` exists in the working directory,
in one of its parents, or in the home directory, or if `COSMOSKILL_HOME` is
set, run
`python3 "${CLAUDE_SKILL_DIR}"/../*observational-cosmology/scripts/layers.py cosmo-supernovae`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-supernovae/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
