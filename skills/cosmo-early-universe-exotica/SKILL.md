---
name: cosmo-early-universe-exotica
description: Use when reviewing, planning or fact-checking non-standard early-Universe physics — PTA background (NANOGrav, EPTA/InPTA, PPTA, CPTA, MPTA, IPTA), SMBHB or cosmological origin, Hellings–Downs, LVK stochastic limits, phase transitions, cosmic strings, primordial black holes, OGLE or HSC microlensing, scalar-induced GWs, early dark energy, varying α or m_e, modified recombination, μ and y distortions (FIRAS, PIXIE), energy injection, p_ann, primordial magnetic fields, axion-like particles.
---

# Early-Universe exotica — expert reference

Snapshot 2026-10-16. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Ω_GW, HD statistics, phase transitions, strings, PBH formation, SIGW, EDE, recombination, distortions, energy deposition, PMFs, ALPs, codes | `references/physics-and-methods.md` |
| PTA releases, LVK runs, LISA, microlensing surveys, distortion instruments, CMB and γ-ray data | `references/surveys-and-data.md` |
| PTA amplitudes, Ω_GW limits, Gμ, f_PBH, f_EDE, α, m_e, μ, y, p_ann, PMF and ALP bounds, history | `references/results.md` |
| PTA noise, templates, PBH modelling, EDE priors, constants, distortions, injection; referee list | `references/systematics.md` |
| PTA origin, PBH disputes, EDE, distortions, PMF hints, forecasts, stale claims | `references/open-questions.md` |
| PTA pipeline: noise model, priors, HD Bayes factor, optimal statistic, null tests | `deep/sgwb-pta.md` |
| Building an f_PBH(M) curve: microlensing, LVK mergers, extended mass functions | `deep/primordial-black-holes.md` |
| Deriving μ and y limits: visibility, FIRAS fit, μ map, forecasts | `deep/spectral-distortions.md` |
| Title, author, year of a source | `references/sources.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- NANOGrav 15 yr: A = 2.4 (+0.7/−0.6) × 10⁻¹⁵ at γ = 13/3; free fit γ = 3.2 ± 0.6; HD p = 10⁻³ (Bayes-factor null), 5 × 10⁻⁵–1.9 × 10⁻⁴ (frequentist) (arXiv:2306.16213).
- No PTA reaches 5σ: EPTA ≳ 3σ (10.3 yr subset), PPTA ~2σ, MPTA 3–3.4σ depending on noise model, a five-array combination below 5σ (arXiv:2306.16214, arXiv:2306.16215, arXiv:2412.01153, arXiv:2512.08666).
- New-physics Bayes factors of 10–100 depend on the SMBHB prior and "should not be regarded as evidence for new physics"; stable strings alone give factors < 1 (arXiv:2306.16219).
- The PTA amplitude exceeds the local-SMBH prediction (arXiv:2312.06756).
- LVK: Ω_GW(25 Hz) ≤ 2.8 × 10⁻⁹ (flat), ≤ 2.0 × 10⁻⁹ (α = 2/3), against a predicted compact-binary 6.3 × 10⁻¹⁰ (arXiv:2608.23477).
- PBHs: the asteroid window, 10⁻¹⁷–10⁻¹⁰ M☉, is the only unconstrained range (arXiv:2601.06024); LVK O3 gives f_PBH ≲ 10⁻³ over 1–200 M☉ (arXiv:2405.05732); OGLE's < 1% limits are disputed (arXiv:2403.02386, arXiv:2509.05400).
- Gaussian SIGW fits to the PTA signal overproduce PBHs at 2σ (arXiv:2306.17149).
- EDE: ACT DR6 f_EDE < 0.088, no H0 shift, the DR4 hint gone (arXiv:2503.14454); SPT+ACT+Planck < 0.070, with DESI 0.055 (+0.024/−0.047) (arXiv:2507.23355); profile 0.09 ± 0.03 (arXiv:2505.08051).
- Constants at recombination (P-ACT-LB): m_e/m_e,0 = 1.0096 ± 0.0060, α_EM/α_EM,0 = 1.0043 ± 0.0017, both step models with no driving field (arXiv:2503.14454).
- FIRAS: |y| < 15 × 10⁻⁶, |μ| < 9 × 10⁻⁵ (arXiv:astro-ph/9605054); reanalysis |⟨μ⟩| < 47 × 10⁻⁶ (arXiv:2206.02762); ΛCDM predicts μ ≈ 2.3 × 10⁻⁸ (arXiv:1909.01593).
- p_ann < 3.2 × 10⁻²⁸ cm³ s⁻¹ GeV⁻¹ (Planck 2018, on-the-spot; arXiv:1807.06209).
- PMFs: √⟨B²⟩ < 0.69 nG (arXiv:2204.06302), Lyα B < 0.30 nG (arXiv:2501.06299); γ-ray lower bound > 7.1 × 10⁻¹⁶ G, duty-cycle dependent (arXiv:2306.05132); a 1.8–3σ pG hint (arXiv:2503.09599) against ACT clumping b < 0.41.

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

1. PTA noise (red, DM, chromatic, solar wind); split-data stability.
2. HD significance as calibrated p-value, not only Bayes factor.
3. SMBHB prior behind new-physics comparisons.
4. Templates: string loops, phase-transition source, α definition.
5. PBH halo model, mass function, binary channel, accretion.
6. EDE, constants: Bayesian or profile, BAO sample, P-ACT or W-ACT.
7. FIRAS calibration; distortion foregrounds.
8. Energy deposition (on-the-spot or full); PMF clumping model.

## Errors that recur
<!-- key: errors-that-recur -->

- "PTAs detected the background at 5σ"; treating γ as robust.
- Mixing the PTA strain index α with the LVK Ω_GW index α.
- Ω_GW without h or reference frequency.
- The O3 limit 5.8 × 10⁻⁹ cited as current.
- OGLE limits as undisputed; white-dwarf or femtolensing limits as valid.
- "f_EDE < 0.07 rules out EDE", ignoring Bayesian versus profile.
- Quasar Δα/α (z ~ 1) compared with CMB α_EM (z ~ 1100).
- The 1996 FIRAS μ as current; mixing B_1Mpc and √⟨B²⟩.

## Related skills
<!-- key: related-skills -->

- `cosmo-inflation-primordial`: n_s, r, f_NL, isocurvature, features, birefringence.
- `cosmo-tensions-anomalies`: EDE, varying m_e as H0 fixes.
- `cosmo-neutrinos-dark-matter`: fuzzy and particle dark matter, N_eff.
- `cosmo-bbn`: decaying relics, extra radiation.
- `cosmo-multimessenger`: sirens; `cosmo-cmb`: likelihoods.
- `cosmo-reionization-21cm`: dark-ages 21 cm; `cosmo-lyman-alpha`: forest data for PMF limits.
- `cosmo-surveys-facilities`: LISA.

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

Sizes, in thousands of tokens: L1 2k; open 3k; methods 9k; results 8k; surveys 3k; systematics 4k; deep/primordial-black-holes 7k; deep/sgwb-pta 7k; deep/spectral-distortions 6k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-early-universe-exotica`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-early-universe-exotica/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
