---
name: cosmo-galaxy-halo-connection
description: Use when reviewing, planning or fact-checking how galaxies occupy dark-matter haloes - HOD per tracer (LRG, ELG, QSO, BGS), decorated HOD, SHAM, CLF, stellar-to-halo mass relation and scatter, UniverseMachine, semi-analytic models, assembly bias, conformity, satellite fractions and kinematics, velocity bias, group catalogues, galaxy-galaxy lensing with clustering, "lensing is low", halo mass definitions, splashback, mass function, halo bias, concentration, halo model.
---

# Galaxy–halo connection — expert reference

Snapshot 2026-10-16. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Halo ingredients, halo model, HOD/CLF/SHAM, empirical/physical models, assembly bias, satellites, joint-fit practice, codes | `references/physics-and-methods.md` |
| Samples, group and lensing catalogues, simulations, what constrains what | `references/surveys-and-data.md` |
| HOD values, SHMR, satellites, assembly-bias detections, lensing-is-low, joint-fit S8, history | `references/results.md` |
| Size of a systematic; referee checklist | `references/systematics.md` |
| Lensing-is-low, assembly-bias detection, conformity, SHMR ends, method debates, stale claims | `references/open-questions.md` |
| HOD/CLF fitting: engine, priors, covariance, sampler | `deep/hod-clf.md` |
| SHAM/SHMR: proxy, scatter, orphans, nuisances | `deep/abundance-matching-shmr.md` |
| Assembly-bias forms, environment, shuffling | `deep/assembly-bias.md` |
| Groups, satellite kinematics, velocity bias | `deep/satellites.md` |
| Empirical-model fits, SAM tuning, hydro HODs | `deep/empirical-sam-hydro.md` |
| Concentration measurement, conversion, f_conc | `deep/profiles-concentration.md` |
| Cited paper's title, first author, year | `references/sources.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Formation efficiency peaks near M_h ~ 10¹² M_⊙ with < 20% of baryons in
  stars; M* scatter at fixed M_h is < 0.2 dex above it (arXiv:1804.03097,
  abstract).
- An occupation parameter needs its mass definition, finder and cosmology;
  FoF halo bias is ~10% below Δ = 200 (arXiv:1001.3162, abstract).
- The HMF is not universal at its ≲ 5% calibration accuracy; amplitude falls
  ≈ 20–50% from z = 0 to 2.5 (arXiv:0803.2706, abstract).
- DESI One-Percent LRGs: f_sat = 11 ± 1% and log M_h = 13.40 at
  0.4 < z < 0.6, 14 ± 1% and 13.24 at 0.6 < z < 0.8; QSOs log M_h = 12.65
  (arXiv:2306.06314, abstract); ELGs ~11.9, with conformity
  (arXiv:2306.06319, abstract).
- Assembly bias is predicted (> 5× at 10¹¹ h⁻¹M_⊙, arXiv:astro-ph/0506510,
  abstract)
  but galaxy-level detections split: yes in SDSS and CMASS
  (arXiv:1606.07817, arXiv:2010.04182), Q_sat = 0.05 ± 0.14 in DESI DR1
  (arXiv:2510.20896, abstract).
- The redMaPPer halo assembly-bias detection (arXiv:1506.06135) reflects
  projection effects: ratio 1.02 ± 0.14 (arXiv:1611.00366, abstract).
- Lensing is low: 20–40% at Planck for CMASS (arXiv:1611.08606, abstract);
  A = 0.79 ± 0.03 at Planck, consistent with 1 at S8 = 0.76
  (arXiv:2202.07440, abstract).
- Galaxy–halo explanations: assembly bias, satellite segregation, baryons
  (arXiv:2211.01744), SHAMe (arXiv:2305.09637); UNIONS sees no significant
  effect (arXiv:2606.23651).
- Joint clustering + lensing fits give S8: DESI DR1 0.797
  (arXiv:2512.15962, abstract), KiDS-1000 0.773 (arXiv:2210.03110,
  abstract), HSC-Y3 0.763 (arXiv:2304.00704, abstract), UNIONS 0.743
  (arXiv:2606.23651, Sect. 7.2), satellite kinematics 0.81 ± 0.05
  (arXiv:2512.14889, abstract).
- BOSS centrals move at 0.22 and satellites at 0.86 of the dark-matter
  velocity dispersion (arXiv:1407.4811, abstract).
- Dwarf SHMR in DESI DR1 BGS: slope 2.08 ± 0.21, scatter up to 0.68 dex
  (arXiv:2609.04351, abstract).
- BCG stellar masses from standard photometry are low by ~2–4
  (arXiv:1401.7329).
- The analytic halo model needs non-linear bias and exclusion: ignoring them
  costs > 40% at ~1 h⁻¹Mpc (arXiv:1206.6890, abstract).
- Satellite assumptions are cosmology-level: DM-tracing or subhalo-like
  profiles put satellite kinematics ~2σ and ~5σ from Planck
  (arXiv:2512.14889, Sect. 5.2); Poisson satellites move KiDS-1000 S8 from
  0.773 to 0.951 (arXiv:2210.03110, abstract and Sect. 4.4).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

1. Halo definition, finder, simulation resolution.
2. Fixed cosmology during HOD or SHMR fits.
3. Central form, satellite statistics, central condition.
4. Assembly bias: modelled, bracketed or argued away.
5. Satellite profile and velocity bias.
6. Stellar-mass systematics and measurement scatter.
7. Lens selection, completeness versus z.
8. Lensing: n(z), shear, boost, baryons, scale cuts.
9. Residual RSD in w_p; exclusion in analytic models.
10. Covariance, Hartlap factor, blinding.

## Errors that recur
<!-- key: errors-that-recur -->

- Comparing M_min or M_1 across different Δ, finders or cosmologies.
- Calling "lensing is low" evidence for low S8 without its galaxy–halo
  model.
- Citing Miyatake et al. 2016 as a halo assembly-bias detection.
- Treating satellites as Poisson and the central condition as harmless.
- Reading M_vir growth as accretion (pseudo-evolution, arXiv:1207.0816).
- Comparing S8 values with different fixed parameters, scale cuts or
  exponents.
- Plugging ν = δ_c/σ into Sheth–Tormen, which is written in ν = (δ_c/σ)²
  (arXiv:astro-ph/9901122).
- Using the quiescent clustering excess as central assembly bias: at z ~ 0
  it is mainly satellites (arXiv:2403.01393).

## Related skills
<!-- key: related-skills -->

- `cosmo-simulations-mocks`: populating, validating survey mocks; finders.
- `cosmo-theory-foundations`: perturbative bias expansions, halo-model
  equations.
- `cosmo-clusters`: cluster mass calibration and splashback.
- `cosmo-weak-lensing`: shear and n(z) calibration, 3×2pt, hybrid EFT.
- `cosmo-galaxy-clustering`, `cosmo-beyond-two-point`: emulator cosmology
  from small-scale clustering.
- `cosmo-cosmic-web`: environment and web dependence.
- `cosmo-surveys-facilities`: release dates, instruments.

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

Sizes, in thousands of tokens: L1 3k; open 4k; methods 12k; results 8k; surveys 4k; systematics 6k; deep/abundance-matching-shmr 7k; deep/assembly-bias 9k; deep/empirical-sam-hydro 10k; deep/hod-clf 9k; deep/profiles-concentration 6k; deep/satellites 9k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-galaxy-halo-connection`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-galaxy-halo-connection/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
