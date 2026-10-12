---
name: cosmo-peculiar-velocities
description: Use when reviewing, planning or fact-checking direct peculiar-velocity cosmology — log-distance ratio, Tully-Fisher, Fundamental Plane or SN Ia velocities, fσ8 at z<0.1, maximum-likelihood fields, flip, momentum power spectrum, velocity correlation functions, velocity–density comparison (2M++, β), bulk flow and its estimators, zero-point or Malmquist bias, σ_u damping, kSZ velocities, growth index; DESI PV DR1, Cosmicflows-4, 6dFGSv, SDSS PV, WALLABY, ZTF, 4HS, Rubin.
---

# Peculiar velocities — expert reference

Snapshot 2026-10-07. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

Read first: `references/pv-surveys.md` (indicators, surveys, method families,
the fσ8 table) and `references/fsigma8-pv-compilation.md` (the discussion of
each value and its provenance).

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Distance indicators, each survey, Cosmicflows-4 composition, method families, the fσ8 table row by row, systematics by indicator | `references/pv-surveys.md` |
| Discussion and provenance of each fσ8 value, discrepancies found at source, σ8 conventions | `references/fsigma8-pv-compilation.md` |
| Estimator equations: η and velocity estimators, Koda model, field-level covariance (flip), momentum P(k), ψ1/ψ2, bulk-flow MLE/MV, conventions | `references/physics-and-methods.md` |
| Sample counts per release, DESI DR1 cut flow, CF4++, ZTF/WALLABY/4HS status, public data and codes | `references/surveys-and-data.md` |
| DESI DR1 non-fσ8 output and consensus construction, 2025–2026 results, bulk-flow record, kSZ velocities, gravity tests, history | `references/results.md` |
| Size of each systematic, mitigation, referee checklist | `references/systematics.md` |
| Controversies with both sides, forecasts (labelled), stale claims | `references/open-questions.md` |
| Bibliography | `references/sources.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- DESI DR1 PV consensus: fσ8(z = 0.07) = 0.4497 ± 0.0548, from three estimators
  (0.391, 0.440, 0.483) correlated at only 27–39 % on 675 mocks; the largest
  pairwise difference is 1.1σ in mock units (arXiv:2512.03228, arXiv:2512.03230).
- That measurement is FP: 73 686 FP against 2 929 TF velocities; TF at z > 0.05
  was discarded for an unexplained excess correlation (arXiv:2512.03230).
- The field-level fit fixes σ_u; the cost is ±0.018 on fσ8, ~30 % of the
  statistical error (arXiv:2512.03229). σ_u ranges from 6.75 to 19–23 h⁻¹Mpc
  across analyses, 13 from N-body (arXiv:1312.1022, arXiv:2303.01198).
- The sinc damping D_u is an empirical fit valid to k ≤ 0.2 h Mpc⁻¹
  (arXiv:1312.1022); EFT and emulator replacements exist (arXiv:2508.00066,
  arXiv:2602.03382).
- Fit in log-distance, never in velocity; v = cz − H0 d is ~100 km/s wrong at
  z ~ 0.04 (arXiv:1404.3799, arXiv:1405.0105).
- Zero-point: DESI DR1 η_zp = 0.139 ± 0.007, tied to SH0ES/Pantheon+ SNe through
  groups; fully correlated across the sample (arXiv:2512.03232).
- FP is the indicator most exposed to the Malmquist treatment: S8 shifts of
  0.08–0.15 against a 0.03 error; TF + SN give S8 = 0.798 ± 0.035
  (arXiv:2509.20235).
- TF and FP residuals correlate with environment; velocities are unreliable
  below ~10 h⁻¹Mpc (arXiv:2602.23033, arXiv:2512.03226).
- CF4 bulk flow: 387 ± 28 km/s at 150 h⁻¹Mpc (arXiv:2302.02028); with mock
  errors the probability is 0.11 % (arXiv:2306.11269); a shell analysis finds
  2.3σ overall and a window-dependent 3.4σ feature (arXiv:2608.14265).
- A bulk flow needs its estimator, window and depth; MV weights carry a ΛCDM
  prior on the velocity correlations (arXiv:1508.03860).
- No fσ8 from ZTF data exists; only simulations — 19 % alone, 10 % with DESI DR3
  BGS (arXiv:2303.01198, arXiv:2609.34508). No DESI DR2 PV paper either.
- kSZ gives τ × v; b_v ≈ 0.2–0.45, so it constrains f_NL, not fσ8
  (arXiv:2604.04867, arXiv:2511.15701).
- γ_L = 0.580 ± 0.110 from DESI DR1 PV + full shape (arXiv:2512.03231).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

Zero-point anchor and marginalisation; Malmquist treatment and its alternative;
split by indicator; σ_u value, prior, induced error; scale cuts; wide-angle
modelling; mock realism and box size; σ8 convention and z_eff; for flows,
window, depth, mock-calibrated errors; shared galaxies. Details:
`references/systematics.md` §10.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting the CF4 flow as "4.8σ" without the mock-calibrated value.
- Comparing bulk flows of different windows or depths, or with residual
  ("external") flows from velocity–density fits.
- Calling the DESI DR1 H0 = 73.7 independent: it is a calibration transfer.
- Treating the three DESI DR1 estimators, or CF4 and its constituent surveys, as
  independent data.
- Mixing β = f/b, β* = Ω_m^0.55/b* and Ω_m^γ/b, or σ_u (h⁻¹Mpc) with σ_v (km/s).
- Citing Taipan-based or volume-Fisher forecasts as expected performance;
  presenting a simulated fσ8 (TITAN, ZTF) as a measurement.
- Citing FP-based low S8 (arXiv:2007.04993) as growth suppression.
- Reading the CF4++ clustering fσ8 (arXiv:2605.00450) as a velocity statistic.

## Related skills
<!-- key: related-skills -->

- `observational-cosmology` — hub: cross-probe digest, conventions, which skill holds what.
- `cosmo-galaxy-clustering` — RSD fσ8, full shape, estimators, blinding.
- `cosmo-supernovae` — SN samples, standardisation, velocities as nuisance.
- `cosmo-distance-ladder-h0` — TF/FP/SBF as H0 rungs, local void, sirens.
- `cosmo-cmb-lss-cross-correlations` — kSZ gas physics and CMB side.
- `cosmo-dark-energy-modified-gravity` — γ, μ–Σ, E_G beyond the velocity data.
- `cosmo-tensions-anomalies`, `cosmo-simulations-mocks` — dipole anomalies;
  constrained simulations and mocks.

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

Sizes, in thousands of tokens: L1 3k; fsigma8-pv-compilation 5k; open 6k; methods 8k; pv-surveys 7k; results 9k; surveys 4k; systematics 6k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-peculiar-velocities`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-peculiar-velocities/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
