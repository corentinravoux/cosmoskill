---
name: cosmo-peculiar-velocities
description: Use when reviewing, planning or fact-checking direct peculiar-velocity cosmology — log-distance ratio, Tully-Fisher, Fundamental Plane or SN Ia velocities, low-redshift fσ8, maximum-likelihood fields, flip, momentum power spectrum, velocity correlation functions, velocity–density comparison (2M++, β), bulk flow and its estimators, zero-point or Malmquist bias, σ_u damping, kSZ velocities, growth index; DESI PV DR1, Cosmicflows-4, 6dFGSv, SDSS PV, WALLABY, ZTF, 4HS, Rubin.
---

# Peculiar velocities — expert reference

Snapshot 2026-10-14. Every number names its paper and the place it was read
([src: <place>] / [sec: <place>]); no number is derived by an agent (numbers
re-read on 2026-10-23). Re-verify against the cited paper before a number
enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Method families, equations, conventions | `references/physics-and-methods.md` |
| Indicators, surveys, DR1 cut flow, codes | `references/surveys-and-data.md` |
| fσ8 table, provenance, results, bulk flows, kSZ, gravity | `references/results.md` |
| Systematics, sizes, referee checklist | `references/systematics.md` |
| Controversies, forecasts, stale claims | `references/open-questions.md` |
| Momentum P(k), ψ1/ψ2: weights, model | `deep/two-point-statistics.md` |
| Field-level cells, covariance, numerics | `deep/field-level-likelihood.md` |
| Velocity–density likelihood, σ8 linearisation, errors | `deep/velocity-density-comparison.md` |
| FP/TF fits, η posteriors, selection | `deep/distance-indicators.md` |
| Bulk-flow weights, window, χ², mocks | `deep/bulk-flows.md` |
| SN residuals, covariance, cuts | `deep/supernova-velocities.md` |
| Bibliography | `references/sources.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- DESI DR1 PV consensus: fσ8(z = 0.07) = 0.4497 ± 0.0548 (arXiv:2512.03230,
  abstract), from three estimators (0.391, 0.440, 0.483; abstracts of
  arXiv:2512.03230, arXiv:2512.03231, arXiv:2512.03229), correlated at only
  27.3 % to 38.8 % on 675 mocks (arXiv:2512.03228, Sect. 9) and called
  consistent within 1σ by their own papers.
- That measurement is FP: 73 686 FP against 2 929 TF velocities; TF at z > 0.05
  was discarded for an unexplained excess correlation (arXiv:2512.03230,
  Sect. 2.2.2).
- The field-level fit fixes σ_u = 16 h⁻¹Mpc (±0.018 on fσ8) and inflates its
  Hessian errors ×1.64 to the mock scatter (arXiv:2512.03229, abstract, Sects.
  4.4.2 and 5). σ_u is ≈ 13 h⁻¹Mpc from N-body (arXiv:1312.1022, Sect. 2.3.1),
  6.75 on 2MTF data and "within [19,23]" on SDSS PV mocks (both as quoted in
  arXiv:2303.01198, Sect. 5.1).
- The sinc damping D_u is an empirical fit valid to k ≤ 0.2 h Mpc⁻¹
  (arXiv:1312.1022, Sect. 2.3.1); EFT and emulator replacements exist (arXiv:2508.00066,
  arXiv:2602.03382).
- Errors are Gaussian in η, not in v (arXiv:1404.3799); the DESI momentum
  spectrum still converts η to v first (arXiv:2512.03231). v = cz − H0 d is
  ~100 km/s wrong at z ~ 0.04 (arXiv:1405.0105, abstract).
- Zero-point: DESI DR1 η_zp = 0.139 ± 0.007, tied to SH0ES/Pantheon+ SNe through
  groups; fully correlated across the sample (arXiv:2512.03232, Sect. V.5).
- FP is most exposed to the Malmquist treatment: S8 shifts by 0.08 (SDSS FP)
  and 0.15 (6dF FP) against a ~0.03 statistical error (arXiv:2509.20235,
  Sect. 5); TF + SN give S8 = 0.798 ± 0.035 (same, abstract).
- TF and FP residuals correlate with environment; velocities are unreliable
  below ~10 h⁻¹Mpc (arXiv:2602.23033, abstract; arXiv:2512.03226).
- CF4 bulk flow: 387 ± 28 km/s at 150 h⁻¹Mpc (arXiv:2302.02028, Table 1); with
  mock errors the probability is 0.11 % (arXiv:2306.11269, abstract); a shell
  analysis finds dipole and joint deviations of 2.29σ and 2.36σ overall and a
  window-dependent 3.40σ feature (arXiv:2608.14265, abstract).
- A bulk flow needs its estimator, window and depth; MV weights carry a ΛCDM
  prior on the velocity correlations (arXiv:1508.03860).
- No fσ8 from ZTF data; only simulations — 19 % alone, 10 % with DESI DR3
  BGS (arXiv:2303.01198, arXiv:2609.34508; abstract of each). No DESI DR2 PV
  paper.
- kSZ gives τ × v; the amplitude b_v depends on the tracer and profile (0.33 ±
  0.03 for DESI-LS LRGs × ACT DR6, arXiv:2511.15701, abstract), so it
  constrains f_NL, not fσ8 (arXiv:2604.04867).
- γ_L = 0.580 ± 0.110 from DESI DR1 PV + full shape (arXiv:2512.03231, abstract).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

Zero-point anchor and marginalisation; Malmquist treatment and its alternative;
split by indicator; σ_u value, prior, induced error; scale cuts; wide-angle
modelling; mock realism and box size; σ8 convention and z_eff; for flows,
window, depth, mock-calibrated errors; shared galaxies. Details: the referee
list at the end of `references/systematics.md`.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting the CF4 flow as "4.8σ" (as in arXiv:2311.17988, abstract) without the
  mock-calibrated value.
- Comparing bulk flows of different windows or depths, or with residual
  ("external") flows from velocity–density fits.
- Calling the DESI DR1 H0 = 73.7 (arXiv:2512.03232, abstract) independent: it is
  a calibration transfer.
- Treating the three DESI DR1 estimators, or CF4 and its constituent surveys, as
  independent data.
- Mixing β = f/b, β* = Ω_m^0.55/b* (arXiv:1504.04627, abstract) and Ω_m^γ/b, or
  σ_u (h⁻¹Mpc) with σ_v (km/s).
- Citing Taipan-based or volume-Fisher forecasts as expected performance;
  presenting a simulated fσ8 (TITAN, ZTF) as a measurement.
- Citing FP-based low S8 (arXiv:2007.04993) as growth suppression.
- Reading the CF4++ clustering fσ8 (arXiv:2605.00450) as a velocity statistic.

## Related skills
<!-- key: related-skills -->

- `observational-cosmology` — hub.
- `cosmo-galaxy-clustering` — RSD, full shape, estimators.
- `cosmo-supernovae` — SN samples, nuisance velocities.
- `cosmo-distance-ladder-h0` — TF/FP/SBF rungs, sirens.
- `cosmo-cmb-lss-cross-correlations` — kSZ.
- `cosmo-beyond-two-point` — field-level inference as a method; here, its velocity-field likelihood only.
- `cosmo-dark-energy-modified-gravity` — γ, μ–Σ, E_G.
- `cosmo-tensions-anomalies`, `cosmo-simulations-mocks` — dipoles; mocks.

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

Sizes, in thousands of tokens: L1 3k; open 7k; methods 13k; results 16k; surveys 7k; systematics 12k; deep/bulk-flows 7k; deep/distance-indicators 9k; deep/field-level-likelihood 9k; deep/supernova-velocities 7k; deep/two-point-statistics 6k; deep/velocity-density-comparison 11k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-peculiar-velocities`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-peculiar-velocities/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
