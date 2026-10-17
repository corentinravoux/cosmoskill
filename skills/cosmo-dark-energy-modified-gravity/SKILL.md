---
name: cosmo-dark-energy-modified-gravity
description: Use when reviewing, planning or fact-checking dark-energy or modified-gravity claims — w, w0wa/CPL, pivot, figure of merit, thawing quintessence, phantom crossing, DESI DR1/DR2 evidence for dynamical dark energy and its critiques (SN sample, low-z anchor, priors, tau, negative neutrino mass), mu-Sigma-eta, growth index gamma, EFT of dark energy, Horndeski after GW170817, f(R), screening, E_G, Bayes factor versus Delta chi2 or DIC.
---

# Dark energy and modified gravity — expert reference

Snapshot 2026-10-14. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| CPL, pivot, models, μ–Σ–η, γ, EFT, screening, `E_G`, statistics, codes | `references/physics-and-methods.md` |
| What each data set contributes, releases, next data | `references/surveys-and-data.md` |
| `w0`–`wa`, Bayes factors, μ0, Σ0, `f_R0`, `E_G`, history | `references/results.md` |
| What can fake the signal, sizes, tests, referee checklist | `references/systematics.md` |
| Critiques and replies, MG debates, stale claims | `references/open-questions.md` |
| Bibliography with roles | `references/sources.tsv` |
| Reconstructing w(z) | `deep/wz-reconstruction.md` |
| Interacting dark energy fits | `deep/interacting-dark-energy.md` |
| Non-linear scales beyond ΛCDM | `deep/nonlinear-beyond-lcdm.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- DESI DR2 BAO prefers `w0wa` at 1.7σ alone, 3.1σ with CMB, and 2.8 / 3.8 /
  4.2σ with Pantheon+ / Union3 / DESY5 (arXiv:2503.14738). The last three
  are superseded.
- After the supernova revisions: 3.2–3.4σ for every sample
  (arXiv:2511.07517, arXiv:2601.19424); Unite 3.3σ, "weak" Bayesian evidence
  (arXiv:2609.05053); DES Y6 + DESI + CMB 3.0σ (arXiv:2605.27221).
- No single data set shows it: DESI clustering without CMB gives 1.4σ; the
  bispectrum weakens it (arXiv:2602.18761, arXiv:2606.23936).
- The preference is a slope, not an offset: `w_p = −0.954 ± 0.024` at
  `z_p = 0.31` (arXiv:2503.14738, arXiv:2404.08056).
- Statistics can disagree in sign: Pantheon+ with DR2 gives 2.8σ but
  `ln B = −0.66 ± 0.44` (arXiv:2503.14743).
- Compressed CMB priors give 2.4σ, primary CMB 2.7σ, lensing 3.1σ
  (arXiv:2503.14738). A `tau = 0.09` prior leaves 1.4σ (arXiv:2504.16932).
- The BAO + CMB tension lies in directions that violate the null energy
  condition (arXiv:2412.13894). Thawing models beat Λ only with supernovae
  and lose to CPL (arXiv:2503.14743, arXiv:2512.20832).
- Phantom crossing is preferred within CPL, not established: 3.2% of
  non-crossing mocks imitate it (arXiv:2506.15091).
- Negative neutrino mass, interacting dark energy and non-minimal coupling
  absorb the same data mismatch as `w0wa` (arXiv:2407.10965,
  arXiv:2601.07361, arXiv:2503.19898).
- Perturbations agree with general relativity: `mu0 = 0.05 ± 0.22`,
  `Sigma0 = 0.008 ± 0.045`; the Planck PR3 Σ0 tension is a likelihood
  artefact (arXiv:2411.12026).
- GW170817: `abs(c_g/c − 1) ≤ 5 × 10^-16`; only conformally coupled
  Horndeski terms survive (arXiv:1710.05901, arXiv:1710.05877).
- Hu–Sawicki `f_R0 < 1.4 × 10^-8` from galaxies (arXiv:2009.08743);
  10^-5-level from DESI clustering (arXiv:2604.26915).
- `E_G` at z = 0.555, GR value 0.401: 0.36 (+0.06/−0.05) with Planck
  lensing (arXiv:2401.12971), 0.31 (+0.06/−0.05) with ACT DR6, 0.34 ± 0.05
  with both (arXiv:2405.12795). The low 2015 value is superseded.
- `w0waCDM` lowers `H0` (arXiv:2503.14738).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

Supernova sample and calibration version; a fit without the `z < 0.1`
anchor; shared supernovae between compilations; CMB experiment, likelihood,
lensing and τ; which BAO bins carry the signal; MAP against posterior mean
for full-shape fits; prior edges on `w0`, `wa`; a non-crossing model fit;
data-set consistency under ΛCDM before combining; for μ–Σ the convention,
background, scale cuts and CMB lensing likelihood; stability priors in EFT
fits; the source of `Omega_m` in `E_G`.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting 4.2σ, or "DESI alone", for evolving dark energy.
- Presenting a `Delta chi2` significance as Bayesian evidence, or the reverse.
- Reading the CPL best fit as proof of `w < −1` at high redshift.
- Saying the data favour quintessence.
- Counting three supernova compilations as independent confirmations.
- Quoting a `w0wa` significance without naming the CMB data set.
- Treating a 3σ fit of an alternative model to the same data as new evidence.
- Mixing `mu0`, `Sigma0` conventions (GR at 0 or 1) or `Delta DIC` signs.
- Citing the Planck PR3 Σ0 anomaly, or the low 2015 `E_G`, as current.
- Quoting the cosmological `f(R)` bound as the strongest one.
- Citing a DESI DR2 full-shape or modified-gravity result: none exists.

## Related skills
<!-- key: related-skills -->

- `cosmo-supernovae`: calibration, low-z anchor, sample definitions.
- `cosmo-galaxy-clustering`, `cosmo-lyman-alpha`: BAO and full shape.
- `cosmo-cmb`: τ, `A_L`, lensing, P-ACT versus CMB-SPA.
- `cosmo-weak-lensing`, `cosmo-cmb-lss-cross-correlations`: `S8`, 3×2pt, Σ, `E_G`.
- `cosmo-peculiar-velocities`: low-redshift `f sigma8`.
- `cosmo-neutrinos-dark-matter`, `cosmo-tensions-anomalies`,
  `cosmo-distance-ladder-h0`: neutrino mass, early dark energy, `H0`.
- `cosmo-statistics-inference`, `cosmo-theory-foundations`: evidence and
  tension metrics; scalar–tensor theory.

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

Sizes, in thousands of tokens: L1 2k; open 8k; methods 11k; results 10k; surveys 4k; systematics 10k; deep/interacting-dark-energy 6k; deep/nonlinear-beyond-lcdm 7k; deep/wz-reconstruction 8k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-dark-energy-modified-gravity`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-dark-energy-modified-gravity/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
