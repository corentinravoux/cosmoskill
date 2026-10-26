---
name: cosmo-lyman-alpha
description: Use when reviewing, planning or fact-checking Lyman-alpha forest work — Lyα BAO and Alcock-Paczynski at high redshift, full shape, 1D flux power spectrum P1D (FFT, QMLE), P3D and P-cross, picca deltas, continuum fitting, distortion matrix, DLA/BAL/metal contamination, Vega fits, Lyα tomography, IGM thermal state, Nyx/PRIYA/LaCE/ForestFlow emulators, warm or fuzzy dark matter and neutrino limits from the forest, BOSS/eBOSS/DESI DR1/DR2 Lyα results.
---

# Lyman-alpha forest — expert reference

Snapshot 2026-10-14. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Delta field, estimators (ξ, P1D, P3D, P×), fit model, AP, emulators, codes, units | `references/physics-and-methods.md` |
| Samples, releases, simulations, mocks, public products, future | `references/surveys-and-data.md` |
| Values, fit details, history, superseded results | `references/results.md` |
| Systematics: size, mitigation, validation; referee checklist | `references/systematics.md` |
| Tensions, method debates, forecasts, stale claims | `references/open-questions.md` |
| Bibliography, roles | `references/sources.tsv` |
| Continuum fit, distortion matrix: procedure, alternatives | `deep/continuum-distortion.md` |
| P1D estimation (FFT, QMLE): corrections, validation | `deep/p1d-estimation.md` |
| Emulator-based P1D inference: construction, validation | `deep/p1d-emulators.md` |
| EFT, field-level, SBI inference: calibration, priors | `deep/theory-sbi-field-level.md` |
| Tomographic maps, voids, protoclusters: method, validation | `deep/tomography-voids.md` |
| Lyα mocks: construction, tuning, contaminants; AP blinding | `deep/validation-mocks-blinding.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Current BAO: DESI DR2, D_H/r_d = 8.632 ± 0.101, D_M/r_d = 38.99 ± 0.53 (stat + sys), ρ = −0.431, z_eff = 2.33 (arXiv:2503.14739) [src: Sect. VI.2, Eq. 14].
- Best distances, DR2 full shape: D_M/D_H = 4.572 ± 0.046, D_H/r_d = 8.600 ± 0.066, D_M/r_d = 39.32 ± 0.33, ρ = +0.225 (arXiv:2607.27410) [src: Sect. V.3, Eqs. 25–26]; agree with Planck ΛCDM, ~2σ from CMB + BAO w0waCDM.
- Non-linear BAO-shift systematic: 0.3% per direction (BAO paper, arXiv:2503.14739) [src: Sect. VI.1], revised to 0.15% isotropic and 0.8% peak AP (full shape, arXiv:2607.27410) [src: Sect. 5.2]; studies disagree on its sign (arXiv:2412.06892, arXiv:2503.13442).
- Forest fσ8 fails mock validation; excluded in DR1 and DR2 (arXiv:2509.15308, arXiv:2607.27411). β is b_η f / b_δ, not f/b.
- The continuum fit removes the mean and slope of δ per forest and absorbs F̄(z); models are distorted with the distortion matrix (arXiv:1702.00176, arXiv:2506.15262). It leaks r_∥ < 10 h⁻¹Mpc into all scales: percent-level AP bias unless marginalised (arXiv:2607.27410) [src: Sect. 3.3].
- DESI DR1 P1D cosmology: Δ²_★ = 0.379 ± 0.032, n_★ = −2.309 ± 0.019 at 0.009 s/km, z = 3, from 62,807 spectra with S/N > 3, consistent with Planck (arXiv:2601.21432) [src: abstract; Sect. 2.1 for the sample].
- DR1 slope error is 3× eBOSS: LLS, Si II–Si II and emulator errors now marginalised.
- Running: eBOSS-era α_s = −0.010 ± 0.004 (arXiv:1911.09073); DESI DR1 + CMB + BAO: 0.0014 ± 0.0041 (arXiv:2601.21432) [src: abstract of each paper]. "5σ" tension claims use eBOSS likelihoods (arXiv:2311.16377, arXiv:2511.01612).
- One eBOSS data vector gave σ_8 = 0.733 (PRIYA, arXiv:2309.03943) and 0.841 (EFT, arXiv:2405.13208) [src: abstract]; amplitude degenerate with mean flux (arXiv:2412.05372).
- WDM limits depend on thermal-history priors and k_max: > 1.9 keV (95%) when cold histories are allowed (arXiv:1912.09397), > 5.7 keV (95%) from HIRES + UVES at z = 4.2–5.0 (arXiv:2309.04533) [src: abstract of each paper].
- DESI P1D: FFT and QMLE measured; cosmology uses QMLE (arXiv:2505.09493, arXiv:2505.07974).
- Tomography regimes: with galaxies, 2.5 h⁻¹Mpc (CLAMATO, arXiv:1710.02894) and 4 h⁻¹ cMpc over 1.65 deg² (LATIS, arXiv:2510.08815); with quasars, 13 h⁻¹Mpc over 220 deg² (arXiv:2004.01448) [src: abstract of each paper].

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

Continuum distortion and its small-scale leakage; mean-flux prior; DLA finder purity and residual HCD/LLS model; metals; BAL masking; resolution and noise; quasar redshift errors; correlated sky-subtraction noise; BAO shift term; UV fluctuations and reionisation relics; covariance; emulator error and thermal priors; mock realism; blinding. Sizes and mitigations: `references/systematics.md`.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting DESI DR1 (2% on H, arXiv:2404.03001) as the latest Lyα BAO, or a 2.5σ Lyα BAO tension with ΛCDM (BOSS DR11, arXiv:1404.1801; 1.5σ at eBOSS DR16, arXiv:2007.08995) [src: abstract of each paper].
- Quoting a Lyα fσ8, or converting β to f as for galaxies.
- Comparing compressed P1D parameters across papers without checking pivot units (s/km versus Mpc⁻¹) and definitions: (Δ²_★, n_★), (A_Lyα, n_Lyα), (A_P, n_P) differ.
- Quoting a WDM or FDM limit without its thermal-history assumption and k_max.
- Claiming the forest alone constrains Σm_ν (alone ~1 eV); DESI DR1 P1D moves CMB + BAO from 55.1 to 53.7 meV (arXiv:2601.21432) [src: Sect. 7, table].
- Mixing D_A with D_M, or the DR2 BAO-only and full-shape distance pairs (opposite-sign correlations).
- Confusing DESI P1D sample sizes: >300,000 quasars measured (arXiv:2505.07974) [src: abstract], 62,807 used for cosmology (arXiv:2601.21432) [src: Sect. 2.1].
- Treating b_α, β_α from BAO fits as measurements (nuisance parameters).

## Related skills
<!-- key: related-skills -->

- `cosmo-galaxy-clustering`: galaxy and quasar BAO, combined DESI cosmology.
- `cosmo-dark-energy-modified-gravity`: the w0wa interpretation.
- `cosmo-neutrinos-dark-matter`: particle interpretation of Σm_ν, N_eff, WDM, FDM.
- `cosmo-reionization-21cm`: reionisation history, τ.
- `cosmo-beyond-two-point`: voids, field-level inference.
- `cosmo-simulations-mocks`, `cosmo-software-ecosystem`, `cosmo-surveys-facilities`: simulations, codes, facilities.

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

Sizes, in thousands of tokens: L1 3k; open 8k; methods 15k; results 14k; surveys 7k; systematics 16k; deep/continuum-distortion 7k; deep/p1d-emulators 8k; deep/p1d-estimation 11k; deep/theory-sbi-field-level 9k; deep/tomography-voids 10k; deep/validation-mocks-blinding 7k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-lyman-alpha`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-lyman-alpha/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
