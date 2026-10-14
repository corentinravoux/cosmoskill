---
name: cosmo-simulations-mocks
description: Use when reviewing, planning or fact-checking simulations and mocks behind a cosmological analysis — N-body codes and their agreement, initial conditions, AbacusSummit, Uchuu, Quijote, Euclid Flagship, hydrodynamical suites (IllustrisTNG, FLAMINGO, CAMELS, Nyx, PRIYA), baryonic suppression of P(k), COLA, FastPM, EZmocks, GLASS, HOD, SHAM, assembly bias, light-cones, emulators, constrained simulations, BORG, Manticore, digital twins, neutrino or modified-gravity simulations.
---

# Cosmological simulations and mocks — expert reference

Snapshot 2026-10-13. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Methods and founding papers: N-body, initial conditions, halo finders, sub-grid, Lyα hydrodynamics, COLA/FastPM, HOD, light-cones, emulators, constrained simulations; suite set-ups | `references/physics-and-methods.md` |
| Suite tables (code, box, resolution, cosmologies, access); survey mock sets; constrained projects | `references/surveys-and-data.md` |
| Code agreement, emulator and fast-method accuracy, baryonic suppression per suite, mock counts, history | `references/results.md` |
| Where a simulation stops being trustworthy; referee checklist | `references/systematics.md` |
| Debates, Stage-IV requirements, misconceptions | `references/open-questions.md` |
| Bibliography with roles | `references/sources.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- N-body codes agree on P(k) to 1% at k ≤ 1 h/Mpc and, at z ≤ 1, 3% at k ≤ 10 at standard settings (arXiv:1503.05920); 1% to k = 10 needs tuned settings (arXiv:2112.09138, arXiv:2605.28581).
- 1% on P(k) needs L ≥ 0.5 Gpc/h and m_p ≤ 10⁹ M_⊙/h (arXiv:1503.05920); 1% on halo statistics needs 500 particles per halo (arXiv:1804.05865).
- Zel'dovich starts at z = 49 lose 2–8% of non-linear power (arXiv:astro-ph/0606505); advice is late-start 3LPT (arXiv:2008.09588), as in FLAMINGO at z = 31 (arXiv:2306.04024). Flagship 2 (3600 Mpc/h, 16,000³) used 1LPT at z = 99 (arXiv:2405.13495).
- Baryons remove power: 10% at k = 1 h/Mpc in OWLS-AGN (arXiv:1104.1174), up to 20% in IllustrisTNG (arXiv:1707.03397). The group baryon fraction drives it (arXiv:1906.00968) without fixing it (arXiv:2410.17109).
- Data give 10 ± 2% at k = 1 h/Mpc from kSZ and eROSITA, 5 ± 4% from older X-ray data (arXiv:2512.02954). Fiducial FLAMINGO is more than 8σ from one analysis, tracks another (arXiv:2509.10455, arXiv:2609.22466).
- Emulator accuracies are interpolation errors: EuclidEmulator2 1% to k = 10 h/Mpc, z ≤ 3 (arXiv:2010.11288); Mira-Titan, BACCO 2–3% (arXiv:2207.12345, arXiv:2004.06245).
- COLA with 40 steps: P(k) to 1% at k ≲ 1 h/Mpc, halo mass function to 5% (arXiv:1509.04685). Twenty steps do not give converged cluster masses (arXiv:2304.09193).
- Approximate-mock covariances: parameter errors within 10% of N-body ones (arXiv:1806.09497).
- DESI DR1: 1000 EZmocks per Galactic cap, tuned to AbacusSummit HOD mocks; BAO covariance analytic, full-shape from mocks rescaled by 10–40% (arXiv:2411.12027). DESI-PV: 675 mocks (arXiv:2512.03228).
- A mass-only HOD misses 15% of TNG300 clustering (arXiv:1911.02610); HOD choice shifts DESI full-shape parameters by more than 20% of the statistical error (arXiv:2411.12023).
- Lyα: 20 kpc/h cells and L > 40 Mpc/h for 1%; splicing good to 10% (arXiv:1406.6361). Nyx and SPH agree to 1% with tessellated density (arXiv:2207.05023). AGN feedback moves σ_8 by 2% (arXiv:2002.02822).
- Fixed-and-paired boxes cannot provide a covariance (arXiv:1603.05253, arXiv:1811.02111).
- Constrained simulations are posterior ensembles valid above the constraint scale: 4 Mpc/h over (4 Gpc/h)³ in Manticore-Deep (arXiv:2606.10020). SIBELIUS-DARK finds a 5% local underdensity, Manticore-Local none (arXiv:2202.04099, arXiv:2505.10682).
- Neutrino implementations agree below 1% (arXiv:2211.12457); modified-gravity codes to 1% on the ratio to ΛCDM (arXiv:1506.06384).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

Particle mass and box against the statistic; LPT order, starting redshift;
convergence for the statistic used; fast-mock steps and mesh factor;
hydrodynamical variant and calibration data; baryon prior; emulator range,
error; occupation model tested against another; mock count, calibration and
replication; Lyα resolution, mean flux, splicing; constraint scale, ensemble
size. Details: `references/systematics.md`.

## Errors that recur
<!-- key: errors-that-recur -->

- "Codes agree to 1%" without the k range and settings.
- Naming FLAMINGO or BAHAMAS without the variant in a feedback claim.
- Reading a P(k) suppression from a 25 Mpc/h CAMELS box.
- Citing a 1% emulator as a 1% theory error.
- Treating COLA, FastPM or EZmocks as N-body on small scales.
- Attributing DESI BAO errors to mock covariances.
- Calling agreement of data with data-calibrated mocks a validation.
- Assuming Lyα BAO mocks are hydrodynamical.
- Quoting one constrained run as an observation.
- Comparing k_max in Mpc⁻¹, h/Mpc and s/km unconverted.

## Related skills
<!-- key: related-skills -->

- `cosmo-lyman-alpha`: forest analyses, their mocks.
- `cosmo-weak-lensing`, `cosmo-cmb-lss-cross-correlations`: baryons in S8; kSZ, tSZ.
- `cosmo-galaxy-clustering`: DESI covariance, HOD systematics.
- `cosmo-beyond-two-point`: simulation-based and field-level inference.
- `cosmo-statistics-inference`: mock-count corrections, emulator error.
- `cosmo-peculiar-velocities`: velocity reconstructions.
- `cosmo-neutrinos-dark-matter`, `cosmo-dark-energy-modified-gravity`, `cosmo-software-ecosystem`, `observational-cosmology`.

<!-- cosmoskill:block:start — generated by tools/sync_blocks.py, do not edit by hand -->
## Levels and layers
<!-- key: levels-and-layers -->

Answer at the lowest level that answers the question, then stop.

| Level | Read | Holds |
|---|---|---|
| L1 | this file only | the headline values, the state of the domain, the list a referee checks, the errors that recur |
| L2 | one file of `references/` | what this file does not hold: other values, their history, the size of each systematic, methods, releases |
| L3 | one dossier of `deep/` | none in this skill yet: say so and answer at L2 |
| L4 | the cited paper itself | what L1 to L3 quote; required before a number goes into a manuscript, a proposal or a referee report, and when two statements of the skills disagree |

Sizes, in thousands of tokens: L1 3k; open 6k; methods 28k; results 8k; surveys 8k; systematics 15k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-simulations-mocks`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-simulations-mocks/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
