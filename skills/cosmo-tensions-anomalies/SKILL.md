---
name: cosmo-tensions-anomalies
description: Use when reviewing, planning or fact-checking a claim of cosmological tension or anomaly across probes — Hubble tension size and its endpoints, S8 tension, A_L lensing anomaly, optical depth tau, CMB versus DESI BAO discrepancy, w0wa preference, negative neutrino mass, cosmic dipole (radio, quasar, CatWISE, Ellis-Baldwin), bulk flow, large-angle CMB anomalies, cold spot, JWST too-massive galaxies, early dark energy, tension metrics, look-elsewhere, "n sigma" statements.
---

# Cosmological tensions and anomalies — expert reference

Snapshot 2026-10-20. Flags: [src] read in the paper; [sec] from the probe
skill holding the source; [der] derived.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Size of a tension today, its endpoints, what moved it | `references/results.md` |
| Definitions, tension metrics, theory classes | `references/physics-and-methods.md` |
| Shared inputs; next data | `references/surveys-and-data.md` |
| Mundane explanations, metric pitfalls, checklist | `references/systematics.md` |
| Live disputes, H0 models, stale claims | `references/open-questions.md` |
| Homogeneity scale, inhomogeneous models, local void | `references/cosmological-principle.md` |
| Dipole significance: cuts, estimator, mocks | `deep/cosmic-dipoles.md` |
| CMB–DESI distance: metric, inputs, extensions | `deep/cmb-bao-mismatch.md` |
| Anomaly p-values, look-elsewhere, polarisation tests | `deep/anomaly-significance.md` |
| Asymmetry, Cold Spot, alignments | `deep/large-angle-cmb-anomalies.md` |
| JWST abundance test; age problem | `deep/high-redshift-galaxies.md` |
| Judging an H0 model on all data (M_B prior, BBN) | `deep/theoretical-resolutions.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- H0: SH0ES 73.18 ± 0.88, "~6σ" above ΛCDM + CMB (arXiv:2509.01667); H0DN 73.50 ± 0.81, 7.1σ from Planck + SPT + ACT and 5.0σ from BBN + DESI BAO (arXiv:2510.23823); CCHP 70.39 ± 1.22 (stat) ± 1.33 (sys) ± 0.70 (σ_SN), "consistent with" ΛCDM (arXiv:2408.06153) [src: abstract of each].
- Early side beyond Planck: SPT-3G D1 66.66 ± 0.60, CMB-SPA 67.19 ± 0.38 (arXiv:2506.20707) [src: abstract], DESI DR2 BAO + BBN 68.51 ± 0.58 (arXiv:2503.14738) [src: Eq. 19].
- Lensing S8 vs CMB: KiDS-Legacy 0.76σ in S8 and 0.73σ in Σ8 from Planck alone (arXiv:2503.19441) [src: abstract; Sect. 7]; DES Y6 3×2pt 2.6σ in S8, 1.8σ full space from Planck + ACT + SPT (arXiv:2601.14559) [src: abstract], 1.0σ full space from Planck 2018 alone [src: Sect. V.2]. CMB S8 spans 0.819 (PR4, arXiv:2309.10034 [src: Eq. 17]) to 0.836 (arXiv:2601.14559 [src: Table 4]).
- Low-z amplitudes disagree more among themselves than with the CMB: eRASS1 0.86 ± 0.01, KiDS clusters 0.74 ± 0.03, tSZ 0.72 ± 0.03 (arXiv:2402.08458, arXiv:2507.14285, arXiv:2605.11083) [src: abstract of each].
- CMB against DESI DR2 in ΛCDM: 1.6σ (P-ACT, arXiv:2503.14452 [src: abstract]) to 3.7σ (SPT + ACT, arXiv:2506.20707 [src: Sect. VII.3]). Higher τ, w0wa, negative neutrino mass and Ω_K > 0 each absorb this one mismatch (arXiv:2504.16932, arXiv:2407.10965).
- w0wa: 1.7σ DESI alone; with CMB 3.1σ (2.7σ without CMB lensing, 2.4σ compressed priors) (arXiv:2503.14738) [src: Table 6]; 1.4σ with τ = 0.09 (arXiv:2504.16932) [src: Sect. III.2]; 3.0σ with DES Y6 (arXiv:2605.27221) and 3.4σ with Union3.1 (arXiv:2601.19424) after the supernova recalibrations; 4.2σ superseded [src: abstract of each]. Evidence for DESI + CMB mildly favours Λ (arXiv:2511.10631).
- A_L = 1.180 ± 0.065 is Planck PR3 (arXiv:1807.06209) [src: Sect. 2.2.1]; PR4 HiLLiPoP gives 1.039 ± 0.052 (arXiv:2309.10034) [src: abstract] and ACT DR6 1.007 ± 0.057 (arXiv:2503.14452) [src: Sect. VIII.5]; CMB-SPA A_2pt = 1.079 ± 0.038, yet 1.6σ from ΛCDM in the (A_2pt, A_recon) plane (arXiv:2506.20707) [src: Sect. VII.2.3].
- Number-count dipole: 4.9σ (arXiv:2009.14826) to 5.7σ (arXiv:2212.07733) for CatWISE, 5.4σ for three radio surveys (arXiv:2509.16732), but 3.63σ (no clustering dipole), 3.44σ (random) or 3.27σ (aligned) with clustering-aware mocks (arXiv:2511.00822); the DESI redshift dipole gives 357.95 (+55.05/−48.47) km/s (arXiv:2608.30914) [src: abstract of each].
- CMB large-angle anomalies are a posteriori: a joint ≤ 3 × 10⁻⁸ becomes 3σ (about 16 tests) or 2σ (about 50) after look-elsewhere correction; none confirmed in polarisation (arXiv:2310.12859, arXiv:2602.10178, arXiv:1906.02552) [src: abstract of each].
- CF4 bulk flow: probability 0.00021% (arXiv:2302.02028 [src: Table 1]) → 0.11% with mock errors (arXiv:2306.11269) → 2.29σ full-range dipole in a shell analysis (arXiv:2608.14265) [src: abstract of each].
- JWST: no spectroscopic sample needs more baryons than ΛCDM supplies (arXiv:2309.02492, arXiv:2604.18683).
- No model resolves H0: early dark energy leaves about 3σ and raises S8; radiation models fail on ACT DR6; late-time models gain ≲ 2% (arXiv:2607.13283, arXiv:2607.21244).
- Every "nσ" needs two named inputs, a model, a metric and a subspace.

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

- Release, likelihood, CMB combination per input.
- Independence: shared anchor, supernovae, τ prior, calibration, shear catalogue, mocks.
- Projected parameter or full space; point estimate; S8 exponent.
- Anomaly null models: clustering, mask, selection, statistics tried.
- ΛCDM consistency before combining data in an extension.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting an H0 or w0wa significance ("4.4σ", "5σ", "4.2σ") without date and endpoint (arXiv:2411.13621, arXiv:2112.04510, arXiv:2503.14738) [src: abstract of each].
- Listing A_L, Ω_K, negative neutrino mass, τ and w0wa as separate anomalies.
- "S8 from lensing is low" from pre-2025 values, or "the S8 tension is resolved".
- Counting SH0ES, CCHP and H0DN, three supernova samples, or five CatWISE papers as independent.
- Calling a Δχ² preference Bayesian evidence.
- "The dipole violates the cosmological principle at 5σ" without the mock-based reassessment.
- "Evolving dark energy helps H0": it lowers it.
- Citing CosmoVerse (arXiv:2504.01669) for current values: it predates most 2025–2026 results.

## Related skills
<!-- key: related-skills -->

- Sourced numbers, per-probe detail: `cosmo-distance-ladder-h0`, `cosmo-weak-lensing`, `cosmo-cmb`, `cosmo-dark-energy-modified-gravity`, `cosmo-clusters`, `cosmo-cmb-lss-cross-correlations`, `cosmo-galaxy-clustering`, `cosmo-supernovae`, `cosmo-peculiar-velocities`.
- `cosmo-neutrinos-dark-matter`, `cosmo-inflation-primordial`, `cosmo-beyond-two-point`: neutrino mass; curvature, birefringence; parity.
- `cosmo-statistics-inference`: theory of tension metrics.
- `cosmo-reionization-21cm`, `cosmo-simulations-mocks`: τ astrophysics, JWST; constrained simulations.

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

Sizes, in thousands of tokens: L1 3k; cosmological-principle 6k; open 8k; methods 9k; results 18k; surveys 6k; systematics 11k; deep/anomaly-significance 7k; deep/cmb-bao-mismatch 8k; deep/cosmic-dipoles 8k; deep/high-redshift-galaxies 8k; deep/large-angle-cmb-anomalies 8k; deep/theoretical-resolutions 10k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-tensions-anomalies`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-tensions-anomalies/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
