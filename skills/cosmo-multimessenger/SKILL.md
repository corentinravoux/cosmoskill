---
name: cosmo-multimessenger
description: Use when reviewing, planning or fact-checking multi-messenger cosmology — standard sirens (bright, dark, spectral), GW170817 H0, peculiar velocity or inclination of a siren host, galaxy-catalogue completeness (GLADE+), LVK GWTC-3/4/5 H0, modified GW propagation, siren–galaxy cross-correlation, Einstein Telescope or LISA siren forecasts, fast radio bursts (dispersion measure–redshift relation, baryon fraction, H0), lensed supernovae (Refsdal, H0pe, Encore).
---

# Multi-messenger cosmology — expert reference

Snapshot 2026-10-26. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Siren likelihoods, host velocities, catalogue/spectral methods, Macquart relation, codes, conventions | `references/physics-and-methods.md` |
| Runs and catalogues (O1–O4, IR1), galaxy catalogues, FRB samples, lensed transients | `references/surveys-and-data.md` |
| H0 tables (GW170817, LVK, external, FRB, lensed SNe), `Xi_0`, baryon census, history | `references/results.md` |
| Size of each systematic; referee checklist | `references/systematics.md` |
| Controversies, forecasts (labelled), stale claims | `references/open-questions.md` |
| Bibliography | `references/sources.tsv` |
| Siren–galaxy cross-correlation H0: build, tests | `deep/gw-lss-cross-correlation.md` |
| ET, CE, A#, LISA siren forecasts; error budgets | `deep/next-generation-siren-forecasts.md` |
| FRB baryon split IGM/haloes; DM–galaxy stacking | `deep/frb-baryon-distribution.md` |
| GW lensing: `σ_WL`, lensed-pair searches, lensed-siren H0 | `deep/gw-lensing.md` |
| Spectral-siren mass models, priors, evolution, mock challenges | `deep/spectral-sirens.md` |
| FRB H0: zDM forward model, `F` prior, unlocalised bursts, BAO | `deep/frb-hubble-constant.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- GW170817 is still the only bright siren; GWTC-5.0 adds no neutron-star source
  (arXiv:2605.27226).
- LVK value: H0 = 71.7 (+9.4/−7.5), GWTC-5.0, 236 sources, mass spectrum + DES Y6
  catalogue + GW170817 (arXiv:2605.27227) [src: abstract]; compatible with
  both tension endpoints.
- Mass-spectrum features, not galaxies, drive it (arXiv:2605.27227 [src: Sect. IV.1],
  arXiv:2111.03604).
- GW170817 alone: 70.0 (+12.0/−8.0) (arXiv:1710.05835). Jet-informed values differ
  by more than their errors: 68.9 (arXiv:1806.10596), 75.46 (arXiv:2305.19914), 65.5 ± 4.4
  (arXiv:2605.11437) [src: abstract of each].
- NGC 4993 velocity: 310 ± 150 km/s (LVC, arXiv:1710.05835 [src: Methods]) or 373,
  σ ≈ 130 (BORG, arXiv:1909.08627 [src: Sect. 6.1]); 200 km/s moves H0 by about 4
  (arXiv:1909.09609 [src: abstract]); catalogues disagree beyond errors
  (arXiv:1909.00587); DESI data give 70.9 or 73.4 (arXiv:2512.08818 [src: abstract]).
- Velocity covariance can double the H0 error within 50 Mpc (arXiv:2509.03101)
  [src: abstract].
- GLADE+ is complete to 47 Mpc (arXiv:2110.06184) [src: abstract]; completion and host
  weighting bias H0 (arXiv:2310.08991, arXiv:2405.14818).
- Unmodelled mass-spectrum evolution: up to 3σ with 2000 events
  (arXiv:2312.11627), 1.5σ in a blinded challenge (arXiv:2412.14244) [src: abstract of each]; not seen
  at current sensitivity (arXiv:2605.20112).
- Dark-siren H0 is extrapolated from z ≈ 0.44 under a background model
  (arXiv:2511.11795) [src: abstract].
- Cross-correlation: first detection at 5.9σ, H0 = 67 (+18/−15)
  (arXiv:2512.15380) [src: abstract].
- GWTC-5.0: 390 candidates (arXiv:2605.27225), 267 in population (arXiv:2605.27226),
  236 in cosmology (arXiv:2605.27227) [src: abstract of each]. O4 ended 18 November
  2025; IR1 targets a mid-January 2027 start; O5 undated [doc: https://www.aei.mpg.de/gwastronomy, 2026-10-26]
  (`references/surveys-and-data.md` Sect. 1.1).
- FRBs: DM ∝ Ω_b h² f_d / h. Ω_b h70 = 0.051 ± 0.006, f_IGM = 0.76
  (arXiv:2409.16952). H0 = 62.3 ± 9.1 (arXiv:2104.04538), 85.3 (+9.4/−8.1)
  (arXiv:2305.07022); 71.28 (+1.90/−2.08) is statistical only (arXiv:2507.18946)
  [src: abstract of each]:
  host model, Galactic halo and scatter parameter each move it by about 3σ.
  With DESI DR2 BAO in place of a BBN prior, 71.4 (+2.2/−2.5) from 120 localised
  bursts (arXiv:2610.15536) [src: abstract].
- Lensed supernovae [src: abstract of each]: Refsdal 64.8 (eight models) or 66.6 (two
  best models) (arXiv:2305.06367), 65.0 with the cluster mass parametrisation held fixed
  (arXiv:2610.12595), H0pe 75.7
  (arXiv:2403.18902), Encore 66.9 (arXiv:2509.12301), SN 2025wny 70.8
  (arXiv:2608.28427).
- The 2017 forecast of 2% in five years (arXiv:1712.06531) assumed counterparts
  that never came.

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

Bright: recession velocity (galaxy or group), velocity model and zero
point, covariance between hosts, viewing-angle source and jet model, distance
and H0 priors (arXiv:2606.30504), MAP or median. Dark: population fixed or
inferred, second mass-model family, evolution, spectral-only result shown,
catalogue completeness, completion, weighting band, photo-z, selection
injections, pipeline, Ω_m prior. FRB: Ω_b h² prior, f_d, Galactic and host DM,
p(DM|z) form, selection. Lensed: lens models and weights, mass sheet, blinding,
microlensing. Details:
`references/systematics.md` §9.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting 70 (+12/−8) (arXiv:1710.05835), or the fixed-population GWTC-3 value
  68 (+8/−6) (arXiv:2111.03604), as the siren H0 [src: abstract of each].
- Presenting one jet-informed GW170817 value as "the" result.
- Calling dark sirens free of astrophysics or a cosmological model.
- Assuming the catalogue covers the detection horizon.
- Averaging host velocity errors as 1/√N for nearby sirens.
- Giving "267" (the population sample, arXiv:2605.27226 [src: abstract]) as the size
  of GWTC-5.0, or a date for O5.
- Using BBH–AGN flare associations (arXiv:2607.03672, arXiv:2009.14199) as
  established bright sirens.
- Calling an FRB H0 independent of early-universe priors, or quoting its
  statistical error as total.
- Mixing f_IGM and f_d (0.59, arXiv:2402.00505; 0.76, arXiv:2409.16952; more than
  90%, arXiv:2506.03536; [src: abstract of each]).

## Related skills
<!-- key: related-skills -->

- `cosmo-distance-ladder-h0`: tension endpoints, TDCOSMO and lensed quasars.
- `cosmo-peculiar-velocities`: velocity reconstructions, flip, bulk flows.
- `cosmo-surveys-facilities`: detectors and radio facilities.
- `cosmo-statistics-inference`: hierarchical selection effects, priors.
- `cosmo-supernovae`: standardisation of lensed SNe Ia.
- `cosmo-dark-energy-modified-gravity`: theory behind `Xi_0`.
- `cosmo-cmb-lss-cross-correlations`, `cosmo-weak-lensing`,
  `cosmo-simulations-mocks`: kSZ, baryonic feedback.
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

Sizes, in thousands of tokens: L1 3k; open 7k; methods 12k; results 8k; surveys 5k; systematics 14k; deep/frb-baryon-distribution 7k; deep/frb-hubble-constant 8k; deep/gw-lensing 8k; deep/gw-lss-cross-correlation 8k; deep/next-generation-siren-forecasts 7k; deep/spectral-sirens 7k.

- L2: when the file map names several files, search them for the term
  before reading, and read only the passage.
- L4 starts from the L2 entry: its citation and flag say where to look. Read
  the paper with
  `python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/fetch_paper.py" <arXiv id>`
  (`--abstract`, `--outline`, `--section`, `--grep`), or with any tool that
  gives the paper. If it cannot be read, say that L4 was required and not
  done.
- Quote a number only with its paper and the place it was read, or, for a
  code or facility fact, its `[doc]` page and read date, as the skill gives
  them; the skill holds no number of its own making. A formula
  may be applied to the asker's numbers; label the result as derived.

Local layers: if a directory `.cosmoskill/` exists in the working directory,
in one of its parents, or in the home directory, or if `COSMOSKILL_HOME` is
set, run
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-multimessenger`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-multimessenger/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
