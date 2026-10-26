---
name: cosmo-cmb
description: Use when reviewing, fact-checking or planning text or analysis on CMB anisotropies — TT/TE/EE power spectra, CMB lensing reconstruction, Planck PR3/PR4 likelihoods (Plik, CamSpec, HiLLiPoP, SRoll2), ACT DR6, SPT-3G D1, P-ACT, CMB-SPA, A_L lensing anomaly, optical depth tau, N_eff or neutrino mass from the CMB, B-mode status, foregrounds, beams, Simons Observatory, CMB-S4, LiteBIRD, or when a CMB prior enters a BAO, RSD or peculiar-velocity fit.
---

# CMB anisotropies and lensing — expert reference

Snapshot 2026-10-20. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Acoustic physics, parameter dependence | `references/primary-anisotropies.md` |
| Estimators, likelihoods, codes, conventions | `references/physics-and-methods.md` |
| Instruments, releases, status | `references/surveys-and-data.md` |
| Values and their history | `references/results.md` |
| Systematic sizes, referee list | `references/systematics.md` |
| τ, A_L, CMB–DESI debates; stale claims | `references/open-questions.md` |
| History of measurements; dipole | `references/history-of-measurements.md` |
| Bibliography | `references/sources.tsv` |
| High-ℓ likelihoods, foregrounds, lite | `deep/high-ell-likelihoods.md` |
| Lensing reconstruction, biases, null tests | `deep/lensing-reconstruction.md` |
| Low-ℓ EE and τ likelihoods | `deep/low-ell-polarisation-tau.md` |
| Beams, calibration, polarisation efficiency | `deep/beams-calibration-polarisation.md` |
| N_eff, Y_P, phase shift | `deep/damping-tail-light-relics.md` |
| Map-level cleaning, NILC, ILC bias | `deep/component-separation.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- SPT+ACT matches Planck on H₀ and σ₈; CMB-SPA gives H₀ = 67.19 ± 0.38,
  σ₈ = 0.8137 ± 0.0037 in ΛCDM (arXiv:2506.20707, second version). [src: abstract]
- P-ACT (ACT DR6 + Planck truncated at ℓ < 1000 TT, ℓ < 600 TE/EE;
  H₀ = 67.62 ± 0.50, n_s = 0.9709 ± 0.0038) is not CMB-SPA
  (arXiv:2503.14452) [src: Sect. II, Sect. VIII.3].
- ACT and SPT calibrate on Planck and take τ from Planck low-ℓ
  polarisation; only shape parameters are independent (arXiv:2504.16932).
- τ from Planck reprocessings: 0.051 ± 0.006 (NPIPE, arXiv:2007.04997),
  0.059 ± 0.006 (SRoll2 + high-ℓ, arXiv:1908.09856) [src: abstract],
  0.0580 ± 0.0062 (PR4, arXiv:2309.10034) [src: Sect. 10, table]. CMB + DESI
  without low-ℓ EE prefers 0.090 ± 0.012 (arXiv:2504.16932) [src:
  abstract]; reionisation data side with the low value (arXiv:2601.09644,
  arXiv:2607.26373).
- A_L: 1.180 ± 0.065 is Planck PR3 Plik (arXiv:1807.06209, Eq. 34b). PR4
  gives 1.039 ± 0.052 (HiLLiPoP, arXiv:2309.10034) [src: abstract]; ACT
  DR6 gives 1.007 ± 0.057 (arXiv:2503.14452, Sect. VIII.5); SPT+ACT
  1.016 (+0.048/−0.054). The CMB-SPA peak-smoothing amplitude is still
  1.079 ± 0.038 (arXiv:2506.20707, Sect. VII.2.3).
- A_L rescales peak smoothing only; it is not the reconstruction amplitude
  (arXiv:0803.2309).
- Lensing reconstructions match primary-CMB predictions: ACT DR6
  1.013 ± 0.023 (arXiv:2304.05202), ACT+SPT+Planck 1.025 ± 0.017
  (arXiv:2504.20038), SPT-3G D1 at 2% (arXiv:2608.31136) [src: abstract].
- The CMB–DESI DR2 distance in ΛCDM is 1.6σ (P-ACT, arXiv:2503.14452)
  [src: abstract], 2.8σ (CMB-SPA) or 3.7σ (SPT+ACT) (arXiv:2506.20707,
  Sect. VII.3); name the CMB data set.
- N_eff: ACT DR6 2.60 (+0.21/−0.29) (arXiv:2503.14454, Sect. VI.1.1),
  SPT-3G D1 3.18 (+0.29/−0.33), CMB-SPA 2.82 ± 0.12; standard value 3.044
  (arXiv:2506.20707, Sect. VII.2.4, Eqs. 71 and 73).
- Σm_ν limits from CMB + BAO in ΛCDM move with τ and the lensing data:
  < 0.064 eV (DESI DR2 + CMB, arXiv:2503.14738) [src: abstract],
  < 0.072 eV (arXiv:2608.31136) [src: abstract], < 0.089 eV (P-ACT-LB,
  arXiv:2503.14454 v2, Sect. VI.1.1, Eq. 33); the CMB alone gives
  < 0.26 eV (arXiv:1807.06209, Sect. 7.5.1, Eq. 56b).
- r < 0.036 (BK18, arXiv:2110.00483) [src: abstract] remains the latest
  BICEP/Keck limit.
- CMB-S4 lost DOE and NSF support on 9 July 2025. LiteBIRD was reformed to
  one telescope, 12 bands, launch JFY2036 (arXiv:2607.25285) [src: abstract].
- ACT DR6 and SPT-3G D1 were blinded and both changed after unblinding.
- Check the arXiv version: CMB-SPA H₀ and the ACT Σm_ν limit changed.

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

- Planck likelihood, low-ℓ EE likelihood or τ prior, Planck truncation.
- Temperature-to-polarisation leakage and polarised beams: 1.7σ on Ω_b h²
  in ACT if ignored (arXiv:2503.14452, Sect. III.3.2); SPT's sidelobe
  model lacks direct confirmation (arXiv:2602.06334).
- Polarisation efficiency and calibration to Planck.
- Foreground-template and frequency-split robustness (arXiv:2506.06274).
- Lensing foreground bias and estimator choice (arXiv:2304.05196).
- Non-linear lensing model, Boltzmann accuracy, super-sample lensing,
  aberration (arXiv:2103.05582, arXiv:1401.7992, arXiv:1309.2285).
- Covariance validation; ACT–Planck sky overlap.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting "the Planck value" for H₀, A_L or Ω_K without release and
  likelihood.
- Calling the A_L anomaly "resolved", or quoting the PR3 Plik significance
  as the Planck value.
- Comparing θ_MC, θ* and the CLASS θ_s across tables.
- Comparing σ₈(Ω_m/0.3)^0.25 from CMB lensing (arXiv:2304.05202) [src:
  abstract] with galaxy-lensing S₈.
- Treating ACT, SPT and Planck amplitudes (A_s, σ₈) as independent.
- Citing CMB-S4 or pre-2026 LiteBIRD targets as upcoming.
- Quoting a CMB + DESI neutrino bound as a CMB result.
- Combining CMB and BAO where they disagree at over 3σ (ΛCDM+N_eff).

## Related skills
<!-- key: related-skills -->

- `cosmo-inflation-primordial`: r, n_s, B-mode analyses, birefringence.
- `cosmo-cmb-lss-cross-correlations`: lensing × galaxies, kSZ, tSZ, ISW.
- `cosmo-neutrinos-dark-matter`: Σm_ν, light relics.
- `cosmo-early-universe-exotica`: spectral distortions.
- `cosmo-dark-energy-modified-gravity`, `cosmo-tensions-anomalies`:
  CMB–BAO discrepancy; large-angle anomalies.
- `cosmo-reionization-21cm`: reionisation behind τ.
- `cosmo-distance-ladder-h0`, `cosmo-weak-lensing`: H₀, S₈ comparisons.

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

Sizes, in thousands of tokens: L1 3k; history-of-measurements 4k; open 6k; methods 11k; primary-anisotropies 7k; results 8k; surveys 5k; systematics 11k; deep/beams-calibration-polarisation 9k; deep/component-separation 6k; deep/damping-tail-light-relics 6k; deep/high-ell-likelihoods 8k; deep/lensing-reconstruction 9k; deep/low-ell-polarisation-tau 8k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-cmb`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-cmb/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
