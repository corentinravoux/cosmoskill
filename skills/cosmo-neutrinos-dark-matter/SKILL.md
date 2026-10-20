---
name: cosmo-neutrinos-dark-matter
description: Use when reviewing, planning or fact-checking cosmological neutrino or dark-matter-property claims — sum of neutrino masses from DESI, ACT, SPT or Planck, negative or effective neutrino mass, mass ordering, tau or A_lens dependence, N_eff, dark radiation, BBN, KATRIN, JUNO, double beta decay; warm, fuzzy, interacting, self-interacting or decaying dark matter limits from Lyα forest, Milky Way satellites, strong lensing, streams, UV luminosity functions, clusters; sterile neutrinos; relic neutrino background, PTOLEMY.
---

# Neutrinos, light relics and dark-matter properties — expert reference

Snapshot 2026-10-14. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Bound by bound: model, prior, data, codes; effective masses; N_eff; M_hm-to-keV | `references/physics-and-methods.md` |
| Releases, laboratory experiments, small-scale samples, next data | `references/surveys-and-data.md` |
| Σm_ν, N_eff, BBN, WDM, FDM, interacting, SIDM, decay tables; history | `references/results.md` |
| Budgets, what moves each bound, referee checklist | `references/systematics.md` |
| Controversies, forecasts, stale claims, not verified | `references/open-questions.md` |
| Full-shape Σm_ν: method, tests | `deep/neutrino-mass-full-shape.md` |
| Lensing substructure: forward model | `deep/strong-lensing-substructure.md` |
| σ/m: method, critiques | `deep/self-interacting-dm.md` |
| DM interactions, decays: method | `deep/interacting-decaying-dm.md` |
| Fuzzy, axion DM: method | `deep/fuzzy-ultralight-dm.md` |
| Relic-neutrino detection | `deep/relic-neutrino-background.md` |
| Sources | `references/sources.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- DESI DR2 BAO + CMB: Σm_ν < 0.0642 eV (95%, ΛCDM), < 0.163 eV
  (w0waCDM), 0.0691–0.0774 eV with other Planck likelihoods (arXiv:2503.14744).
- Three widths, one data set: 0.020 eV (truncated posterior), 0.043 eV
  (profile), 0.053 eV (effective mass); only the last two measure
  sensitivity (arXiv:2503.14744).
- Effective mass −0.101 (+0.047/−0.056) eV, 3σ below the oscillation
  minimum (0.059 eV normal, 0.10 eV inverted); none in w0waCDM,
  with free lensing amplitudes or τ ≈ 0.09
  (arXiv:2407.10965, arXiv:2511.01967, arXiv:2504.16932).
- Geometric bound: 0.13 eV with BOSS instead of DESI BAO,
  0.23 eV without BAO; ACT P-ACT-LB 0.089 eV (abstract: 0.082)
  (arXiv:2503.14454, arXiv:2410.00090).
- τ: error doubled 0.10 eV; low-ℓ polarisation removed
  0.19 eV (arXiv:2503.14454).
- Ordering: Bayes factor 10 (DESI); 46.5 or > 460, other priors
  (arXiv:2407.18047, arXiv:2606.18987); oscillations alone undecided
  (arXiv:2410.05380); JUNO: normal at ≥ 2.1σ (arXiv:2609.37895).
- Laboratory: KATRIN m_ν < 0.45 eV, 90% CL (arXiv:2406.13516);
  KamLAND-Zen m_ββ < 28–122 meV (arXiv:2406.11438). Neither is Σm_ν.
- N_eff: standard 3.044 (arXiv:2008.01074). CMB-only below
  (ACT 2.60, CMB-SPA 2.82 ± 0.12), with DESI above (3.23 ± 0.18)
  (arXiv:2503.14454, arXiv:2506.20707, arXiv:2503.14744). BBN + CMB: 2.925 ± 0.082 (arXiv:2601.22239).
- Thermal-relic WDM: Lyα 1.9–5.7 keV by thermal prior
  (arXiv:1912.09397, arXiv:2309.04533); satellites 6.5 keV
  (arXiv:2008.00022); JWST lensing 5.6–7.4 keV (Bayes factor 10:1) by data and subhalo
  prior (arXiv:2511.07765, arXiv:2511.07513); M_hm-to-keV slopes differ
  (−10/3, −3.564).
- Fuzzy DM at 10⁻²² eV excluded as all DM; Lyα 1.9 × 10⁻²¹ to 2 × 10⁻²⁰ eV (arXiv:2606.06969,
  arXiv:2007.12705).
- Self-interaction: < 0.13–0.47 cm²/g in clusters (arXiv:2012.06611,
  arXiv:1503.07675); velocity-dependent models survive (arXiv:2006.12515).
- Forecasts: SO σ(Σm_ν) = 0.03 eV, 0.015 eV + LiteBIRD, σ(N_eff) =
  0.045 (arXiv:2503.00636); Euclid + Planck 23 meV (arXiv:2405.06047).
  CMB-S4 cancelled.
- Tighter: CMB-SPA + DESI DR2 < 0.055 eV
  (arXiv:2506.20707); EFT reanalysis 0.049 eV
  (arXiv:2601.16165); 0.043 eV, many background probes
  (arXiv:2405.03368).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

Massive states; Planck likelihood, lensing, BAO release, SN sample; τ
prior, limit without low-ℓ EE; boundary-free limit beside the
Bayesian; width change versus shift; CMB–BAO consistency; ordering
prior; N_eff free-streaming or fluid, Y_P, BBN rates. DM:
production, half-mode conversion, confidence criterion; thermal history
and k_max; LMC analogue, Milky Way mass, disruption; subhalo prior and
multipoles; shared inputs of combined limits; σ/m velocity.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting 0.064 eV without "ΛCDM".
- σ = 0.020 eV read as DESI's sensitivity; the forecast as met.
- Claiming cosmology measured negative mass or settled the ordering.
- Attributing the bound to growth suppression or BAO alone.
- KATRIN quoted at 95%, or as a limit on Σm_ν.
- N_eff = 3.046 as current (3.044; 3.046 is the Planck 2013/2018
  value); N_ν (baseline 3) mixed with N_eff.
- Citing CMB-S4 targets, or Euclid's 4σ, as upcoming.
- A WDM limit without thermal prior, k_max, criterion; 9.7 keV as current.
- A thermal-relic mass transferred to sterile neutrinos or scattering.
- A σ/m limit without velocity; Bullet Cluster 68% limit as 95%.

## Related skills
<!-- key: related-skills -->

- `cosmo-cmb`: τ, A_lens, lensing, N_eff. `cosmo-galaxy-clustering`:
  BAO, full shape. `cosmo-lyman-alpha`: P1D, thermal state, emulators.
- `cosmo-dark-energy-modified-gravity`, `cosmo-supernovae`: w0wa, SN samples.
- `cosmo-weak-lensing`, `cosmo-clusters`, `cosmo-distance-ladder-h0`: S8,
  cluster data, BAO + BBN.
- `cosmo-reionization-21cm`, `cosmo-simulations-mocks`: reionisation,
  small-scale simulations.

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

Sizes, in thousands of tokens: L1 3k; open 8k; methods 12k; results 12k; surveys 7k; systematics 14k; deep/fuzzy-ultralight-dm 7k; deep/interacting-decaying-dm 8k; deep/neutrino-mass-full-shape 8k; deep/relic-neutrino-background 6k; deep/self-interacting-dm 7k; deep/strong-lensing-substructure 8k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-neutrinos-dark-matter`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-neutrinos-dark-matter/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
