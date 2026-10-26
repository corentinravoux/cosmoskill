---
name: cosmo-galaxy-clustering
description: Use when reviewing, planning or fact-checking spectroscopic galaxy or quasar clustering — BAO (D_M/r_d, D_H/r_d, D_V/r_d, reconstruction), RSD and fσ8, Alcock–Paczynski, full-shape, EFTofLSS or ShapeFit fits, f_NL from scale-dependent bias, Landy–Szalay or FKP/Yamamoto estimators, window functions, covariance, blinding, fibre collisions, PIP weights, imaging systematics, HOD — for 2dFGRS, 6dFGS, WiggleZ, BOSS, eBOSS, DESI DR1/DR2, Euclid, PFS, 4MOST, Roman, SPHEREx.
---

# Spectroscopic galaxy clustering — expert reference

Snapshot 2026-10-20. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Definitions, estimators, EFT/ShapeFit models, covariance, blinding, codes, conventions | `references/physics-and-methods.md` |
| Instruments, samples, releases, public data, status | `references/surveys-and-data.md` |
| BAO tables, ΛCDM and full-shape parameters, fσ8, f_NL, history | `references/results.md` |
| Systematic budgets, mitigations, referee checklist | `references/systematics.md` |
| Controversies, method debates, next data, stale claims | `references/open-questions.md` |
| RSD model history; BOSS and eBOSS models, mock challenges | `references/rsd-modelling.md` |
| BOSS, eBOSS values and budgets; Euclid spectroscopic plan | `references/boss-eboss-euclid.md` |
| Bibliography with roles | `references/sources.tsv` |
| BAO reconstruction: solver, convention, damping, 1D/2D | `deep/bao-reconstruction-fitting.md` |
| Full modelling or ShapeFit; EFT codes, bias bases, priors, FS+BAO | `deep/full-shape-modelling.md` |
| Window matrix, wide-angle terms, integral constraints, normalisation | `deep/estimators-window.md` |
| altMTL, FFA, PIP/IIP, angular up-weighting, θ-cut | `deep/fibre-assignment.md` |
| Bad fibres, residual trends, χ²_sys, catastrophics, z errors, interlopers | `deep/spectroscopic-systematics.md` |
| Blinding shifts, f_NL weights, unblinding checklists | `deep/blinding.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Latest DESI BAO: DR2 (arXiv:2503.14738); full shape: still DR1
  (arXiv:2411.12021); "DR1 FS + DR2 BAO" papers mix releases
  (arXiv:2602.18761).
- BAO measure D/r_d, not H0. DR2 + BBN gives H0 = 68.51 ± 0.58; DR2 alone
  gives Ω_m = 0.2975 ± 0.0086 (arXiv:2503.14738) [src: Table 5].
- DESI DR2 BAO versus CMB in ΛCDM: 2.3σ (arXiv:2503.14738). The 2026 Lyα
  AP paper: 2.4σ before, 2.2σ after (arXiv:2607.27410). [src: abstract of each]
- The w0wa preference is 1.7σ for DESI BAO alone, 3.1σ with CMB
  [src: Table 6], 2.8–4.2σ with supernovae, by sample [src: abstract]
  (arXiv:2503.14738); with the recalibrated samples it is 3.2σ (Pantheon+),
  3.4σ (Union3.1) and 3.4σ (DES-Dovekie) (arXiv:2601.19424) [src: abstract].
- DESI clustering beyond BAO has not strengthened it: 1.4σ for DR1 FS + DR2
  BAO without CMB (arXiv:2602.18761) [src: abstract]; the bispectrum weakens
  it (arXiv:2606.23936).
- DESI BAO errors are statistics-dominated: systematics add at most 9% to
  the α_iso error (arXiv:2503.14738) [src: Sect. III.1]; DR1 budget 0.245%
  (α_iso) and 0.3% (α_AP) (arXiv:2404.03000) [src: Sect. 5.5, Table 13].
- Full-shape posteriors in extended models are prior-dominated: best fit and
  posterior mean differ by up to 6.6σ in w0waCDM (arXiv:2508.11811)
  [src: abstract]; ask for the MAP.
- σ8 from full shape: BOSS EFT gave 0.721 ± 0.043 (arXiv:1909.05277) and
  0.692 (+0.035/−0.041) (arXiv:2112.04515); DESI DR1 gives 0.842 ± 0.034
  (arXiv:2411.12022). Simulation-based priors return 0.766 ± 0.015
  (arXiv:2602.18554). [src: abstract of each]
- DESI DR1 "fσ8" points are fσ_s8 under r_d = r_d^fid, for display only
  (arXiv:2411.12021).
- f_NL from scale-dependent bias constrains f_NL·b_φ: DESI DR1 gives
  −3.6 (+9.0/−9.1) or 3.5 (+10.7/−7.4) by quasar assumption
  (arXiv:2411.17623); Planck has −0.9 ± 5.1 (arXiv:1905.05697).
  [src: abstract of each]
- The SDSS–DESI difference at z ≈ 0.7 fell from 3σ (DR1) to about 2.6σ
  (DR2), under an assumed correlation (arXiv:2503.14738) [src: Sect. III.3.2].
- BOSS DR12 fσ8: 0.497, 0.458, 0.436 at z = 0.38, 0.51, 0.61, systematic
  0.024, 0.015, 0.009 (arXiv:1607.03155) [src: Table 7]; eBOSS LRG
  systematics exceeded half σ_stat (arXiv:2007.08993).
- DESI finished its planned survey in April 2026, full-survey results
  due 2027. Euclid DR1 clustering products: mid-2027.

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

Theory and BAO modelling (0.1%/0.2%, arXiv:2402.14070, abstract); galaxy–halo
connection (arXiv:2404.03008, arXiv:2411.12023); fiducial cosmology
(arXiv:2406.06085); fibre assignment (arXiv:2406.04804,
arXiv:2411.12025); imaging weights and integral constraints
(arXiv:1904.08851); spectroscopic success (arXiv:2405.17208); covariance
(arXiv:astro-ph/0608064, arXiv:2411.12027); nuisance
priors; blinding (arXiv:2404.07282). Details:
`references/systematics.md`.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting "DESI prefers evolving dark energy at 4σ" without CMB and
  supernova sample.
- Comparing D_V/r_d with older r_s/D_V or D_A values unconverted.
- Treating DR1 and DR2 BAO, or DESI and SDSS bins, as independent.
- Citing a DESI DR2 full-shape or fσ8 result: none exists.
- w0 = 0.49 in the abstract of arXiv:2602.18761 is −0.49 in its table.
- Taking the DR1 BAO count (5.7 million, arXiv:2404.03000) for the
  full-shape one (4.7 million, arXiv:2411.12021) [src: abstract of each].
- Calling BOSS-era low σ8 a current full-shape result.
- Giving an f_NL limit without its b_φ assumption.

## Related skills
<!-- key: related-skills -->

- `cosmo-lyman-alpha`: Lyα BAO, AP and P1D.
- `cosmo-dark-energy-modified-gravity`: w0wa, μ–Σ.
- `cosmo-peculiar-velocities`: low-redshift fσ8 from peculiar velocities.
- `cosmo-beyond-two-point`: bispectrum, voids, field-level inference.
- `cosmo-inflation-primordial`: f_NL.
- `cosmo-neutrinos-dark-matter`, `cosmo-cmb`, `cosmo-distance-ladder-h0`,
  `cosmo-supernovae`: external data.
- `cosmo-statistics-inference`, `cosmo-simulations-mocks`,
  `cosmo-software-ecosystem`, `cosmo-surveys-facilities`,
  `cosmo-theory-foundations`: shared methods.
- `observational-cosmology`: hub.

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

Sizes, in thousands of tokens: L1 3k; boss-eboss-euclid 6k; open 5k; methods 9k; results 8k; rsd-modelling 6k; surveys 6k; systematics 9k; deep/bao-reconstruction-fitting 7k; deep/blinding 7k; deep/estimators-window 6k; deep/fibre-assignment 7k; deep/full-shape-modelling 7k; deep/spectroscopic-systematics 5k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-galaxy-clustering`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-galaxy-clustering/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
