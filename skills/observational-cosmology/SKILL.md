---
name: observational-cosmology
description: Use when reviewing, planning, or fact-checking observational-cosmology content that spans several probes or whose probe is not yet clear — a manuscript chapter, a proposal, a tensions overview — and for notation and unit conventions, cross-probe field state, to find which cosmo-* skill covers a topic, or to update the cosmo-* skills from the recent literature.
---

# Observational cosmology working knowledge

## Which skill holds what
<!-- key: which-skill-holds-what -->

This skill is the hub of a suite. Each domain below is its own skill with
dated results, provenance flags and a bibliography checked against arXiv.
For a question inside one domain, load that skill and follow its file map;
its numbers supersede the digest in this hub.

| Topic | Skill |
|---|---|
| CMB spectra, lensing reconstruction, Planck / ACT / SPT likelihoods, τ, A_L, N_eff from the CMB | `cosmo-cmb` |
| Galaxy and quasar BAO, RSD, full shape, f_NL from clustering, estimators, DESI DR1/DR2 | `cosmo-galaxy-clustering` |
| Lyα BAO and AP, P1D, P3D, tomography, IGM, forest limits on dark matter | `cosmo-lyman-alpha` |
| Cosmic shear, 3×2pt, S8, shear and photo-z calibration, IA, baryons | `cosmo-weak-lensing` |
| SN Ia Hubble diagram, standardisation, calibration, compilations | `cosmo-supernovae` |
| H0: distance ladder, SH0ES / CCHP / H0DN, masers, time delays, inverse ladder | `cosmo-distance-ladder-h0` |
| Peculiar-velocity estimators and their equations, bulk flows, kSZ velocities, zero-point and Malmquist systematics, DESI DR1 PV and 2025–2026 results, forecasts; survey descriptions and the fσ8 table | `cosmo-peculiar-velocities` |
| Cluster counts, mass calibration and hydrostatic bias, selection, projection effects, cluster S8, gas fractions, splashback; eROSITA, SPT, ACT, Planck SZ, DES, KiDS | `cosmo-clusters` |
| CMB lensing × galaxies and quasars, lensing tomography, kSZ and gas profiles, tSZ × LSS, ISW, CIB, moving lens | `cosmo-cmb-lss-cross-correlations` |
| Bispectrum, parity-odd 4PCF, voids, density split, wavelets, lensing peaks and third-order shear, field-level inference, simulation-based inference | `cosmo-beyond-two-point` |
| n_s and running, tensor-to-scalar ratio and B modes, primordial non-Gaussianity, isocurvature, curvature, primordial features, cosmic birefringence | `cosmo-inflation-primordial` |
| Likelihoods, covariance corrections, blinding, samplers, priors and projection effects, profile likelihoods, Bayes factor against Δχ², tension metrics, Fisher limits, emulator error, SBI validation | `cosmo-statistics-inference` |
| N-body and hydrodynamical suites, fast mocks (COLA, FastPM, EZmocks), HOD and assembly bias, emulators, baryonic suppression of P(k), constrained simulations, accuracy requirements | `cosmo-simulations-mocks` |
| Facility facts: instrument, area, multiplex, release history and dates, status, next milestone, for spectroscopic, imaging, CMB, time-domain, radio, X-ray and gravitational-wave facilities | `cosmo-surveys-facilities` |
| Cross-probe synthesis: H0 and S8 tensions by endpoint and metric, CMB–BAO mismatch, cosmic dipole, large-angle CMB anomalies, JWST abundance, status of proposed resolutions | `cosmo-tensions-anomalies` |
| Reionisation history (τ, x_HI, mean free path, kSZ), 21 cm global signal and power-spectrum limits, HI and line intensity mapping, JWST early galaxies | `cosmo-reionization-21cm` |
| Standard sirens (bright, dark, spectral), host peculiar velocity, catalogue completeness, GW × LSS, fast radio bursts, lensed transients | `cosmo-multimessenger` |
| Definitions and formulae with the paper that fixes each convention: distances, r_d, σ8 and σ12, growth index, multipoles, Kaiser and streaming models, EFT ingredients, bias bases, Limber, neutrinos; which convention each survey adopts | `cosmo-theory-foundations` |
| Codes: Boltzmann solvers and forks, theory façades, samplers, perturbation-theory codes, estimators, Lyα and lensing tools, field-level codes; default units and settings, code agreement, maintenance status | `cosmo-software-ecosystem` |
| Σm_ν bounds and their model dependence, negative effective mass, mass ordering, N_eff, BBN, laboratory limits; warm, fuzzy, interacting, self-interacting, decaying dark matter | `cosmo-neutrinos-dark-matter` |
| w, w0wa, the DESI dark-energy evidence and its critiques, μ–Σ, growth index, EFT of dark energy, f(R), screening, E_G | `cosmo-dark-energy-modified-gravity` |
| Photometric calibration and standards, dust maps, photo-z by templates and machine learning, n(z) calibration (SOM, clustering redshifts, forward models), p(z) storage, spectroscopic training samples, requirements | `cosmo-photometry-photoz` |
| Galaxy–halo connection: HOD, SHAM, CLF, stellar-to-halo mass relation, assembly bias, satellite kinematics, "lensing is low", halo definitions, mass function, halo bias and concentration, halo model | `cosmo-galaxy-halo-connection` |
| Data pipelines: target selection, fibre assignment, spectral extraction, sky subtraction, redshift fitting and success rates, imaging pipelines (PSF, deblending, co-addition, injection), CMB map-making and transfer functions, masks and randoms, data-release validation | `cosmo-data-pipelines` |
| Big-bang nucleosynthesis: primordial D, ⁴He, ³He, ⁷Li and their measurement, nuclear rates (d(p,γ)³He), neutron lifetime, BBN codes and their agreement, Ω_b h² from BBN as a prior, lithium problem, N_eff and new physics from BBN | `cosmo-bbn` |
| Machine learning as a method: emulators and their error budgets, neural compression, field-level networks, neural posterior/likelihood/ratio estimation, generative models, learned simulation corrections, transient and spectral classification, anomaly detection, benchmark suites, robustness to the training simulator | `cosmo-machine-learning` |
| Cosmic web as an object: T-web/V-web/NEXUS/DisPerSE classification, filaments, walls, nodes, voids as structures, environment dependence of galaxies, spin and shape alignments, filament gas and missing baryons (X-ray, tSZ, FRBs), protoclusters, web reconstructions | `cosmo-cosmic-web` |
| Early-Universe physics beyond the standard history: PTA and LVK stochastic backgrounds, primordial black holes, cosmic strings and defects, phase transitions, early dark energy and modified recombination (physics and limits), varying constants, primordial magnetic fields, axion-like particles, CMB spectral distortions, dark-ages energy injection | `cosmo-early-universe-exotica` |

How the suite is built, checked and updated, with the update cycle step by
step: `references/suite-conventions.md`. Design documents and test logs are in the
`docs/` directory of the package repository.

## Hub files
<!-- key: hub-files -->

- `references/field-state-2026.md`: cross-probe digest and facility timeline.
  Each domain skill supersedes it for its own domain.
- `references/conventions.md`: notation, units, estimator definitions to pin
  down.
- `references/review-checklists.md`: four worked systematics checklists for
  reviewing a results section. Every domain skill carries its own list under
  "Systematics a referee checks".
- `${CLAUDE_SKILL_DIR}/scripts/verify_sources.py <skill directory>`: checks
  every cited arXiv identifier of a skill against arXiv.
- `${CLAUDE_SKILL_DIR}/scripts/fetch_paper.py <arXiv id>`: reads a cited
  paper: `--abstract`, `--outline`, `--section <title>`, `--grep <text>`.
- `${CLAUDE_SKILL_DIR}/scripts/layers.py <skill>`: prints a researcher's
  personal and project notes, papers and dossiers for a skill. To record
  something for the researcher, when asked: `layers.py note <skill>
  <file>#<key> <text>`, `layers.py source <skill> <arXiv id> --role <role>`,
  `layers.py dossier <skill> <name>`; add `--project` for one project only.

## Choosing the level
<!-- key: choosing-the-level -->

Every skill of the suite answers at four depths. Start at the lowest that
can answer, and go deeper only when it cannot.

| Level | Read | It holds |
|---|---|---|
| L1 | the domain's `SKILL.md`, nothing else | headline values, where the domain stands, the list a referee checks, the errors that recur |
| L2 | one reference file, chosen from the file map | every other value, the history of a number, the size of each systematic, methods, releases |
| L3 | a dossier of `deep/` | how a result is derived and how to choose between methods. Every domain skill has six, listed in its file map; a subtopic without one is answered at L2, saying so |
| L4 | the cited paper, at the place the number is given | the source itself |

- **The lowest level that answers.** A value that is in the `SKILL.md` is an
  L1 answer. An L1 answer does not open a reference file "to be safe".
- **Levels stack.** L4 starts from the L2 entry, whose citation and flag say
  where to look: `[src]` was read in the paper, `[sec]` came second-hand,
  `[der]` was derived. Flags are in the reference files; the `SKILL.md`
  bullets carry citations only.
- **L4 is mandatory** before endorsing a number for a manuscript, a proposal
  or a referee report. Read the paper with
  `${CLAUDE_SKILL_DIR}/scripts/fetch_paper.py <arXiv id>` (abstract, outline,
  one section, or the paragraphs containing a term), or with any tool that
  gives the paper. If it cannot be read, say that L4 was required and not
  done; a skill file is never the verification.
- **Applying a formula.** With no dossier, a derivation is answered at L2
  with the formula and its source. Working it out for the asker's numbers is
  allowed and is labelled as derived.
- **Which skill, when two fit.** The size or status of a tension across
  probes: `cosmo-tensions-anomalies`. A date, a release or the status of an
  instrument: `cosmo-surveys-facilities`. One probe's value or method: that
  probe's skill. A statistical or coding question: the method skill, not the
  probe that raised it.
- **State the level.** End the answer with the line each skill gives:
  `[cosmoskill L<level> · <layer> · <skill>/<file>#<key>]`.

## How to use this in review
<!-- key: how-to-use-this-in-review -->

1. **Date-check every claim.** Results move fast; a "latest" statement written in
   2025 is often stale. Cross-check numbers against the reference file, and if
   the number matters, verify against arXiv/ADS before endorsing it.
2. **Never invent numbers.** Central values, error bars, significances and paper
   numbers must come from a fetched source or the author. If unverified, say so.
3. **Check the probe-specific systematics list** when reviewing a results
   section — each domain skill gives the set a referee will look for.
4. **Check consistency of conventions** — h-factors, σ₈ vs S₈ vs fσ₈, redshift
   frame (heliocentric/CMB), RA/Dec units, k in h/Mpc vs 1/Mpc, ξ(r) vs P(k)
   Fourier convention. Silent convention drift between chapters is the most
   common real error in a multi-topic manuscript.

## Reviewing prose
<!-- key: reviewing-prose -->

`references/review-rubric.md` holds the rubric for reviewing cosmology prose:
red flags, conceptual slips that recur, how to avoid false positives, and how
to calibrate a finding to the section it sits in. Load it when the task is a
review.

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

Sizes, in thousands of tokens: L1 4k; conventions 1k; field-state-2026 2k; review-checklists 1k; review-rubric 1k; suite-conventions 2k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" observational-cosmology`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · observational-cosmology/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
