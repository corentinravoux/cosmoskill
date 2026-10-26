---
name: cosmo-statistics-inference
description: Use when reviewing, planning or fact-checking the statistical side of a cosmological analysis — likelihood, covariance from mocks, jackknife or analytic (Hartlap, Percival, Sellentin–Heavens), data compression, blinding, MCMC, nested sampling, NUTS, convergence, priors and projection or prior-volume effects, profile likelihood, Feldman–Cousins, Bayes factor, AIC/BIC/DIC, Δχ² to σ, tension metrics, Fisher forecasts, emulator error, simulation-based inference coverage, look-elsewhere effect.
---

# Statistics and inference in cosmology — expert reference

Snapshot 2026-10-14. Every number names its paper and the place it was read ([src: <place>] / [sec: <place>]); no number is derived by an agent.
Re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Methods, formulae, codes | `references/physics-and-methods.md` |
| Collaboration practice; priors | `references/surveys-and-data.md` |
| Correction sizes, projection shifts, Δχ² against evidence, metrics | `references/results.md` |
| Failure modes; referee checklist | `references/systematics.md` |
| Debates, misconceptions, not verified | `references/open-questions.md` |
| Bibliography with roles | `references/sources.tsv` |
| Building, correcting, validating a covariance; χ² goodness of fit | `deep/covariance-estimation.md` |
| Computing a profile likelihood | `deep/profile-likelihoods.md` |
| Computing and choosing a tension metric | `deep/tension-metrics.md` |
| Computing and choosing a model-comparison statistic | `deep/model-comparison.md` |
| Testing or replacing a Gaussian likelihood | `deep/likelihood-form.md` |
| Validating a pipeline on synthetic data | `deep/pipeline-validation.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Hartlap fixes the precision bias only; best-fit scatter needs a second factor (arXiv:1304.2593), the likelihood width a third (arXiv:1312.4841), or a matching-prior t-posterior (arXiv:2108.10402). Name variance or error bar: BOSS "7%" (600 mocks, 41 bins) is variance (arXiv:1304.2593, Sect. III.3 table).
- A Gaussian likelihood takes a covariance fixed in parameter space (arXiv:1204.4724); likelihood non-Gaussianity moved BOSS fσ8 by −0.44σ (arXiv:1803.06348, abstract).
- Posterior mean and best fit separate in extended models: 6.6σ in wa for DESI DR1 full shape in w0waCDM (arXiv:2508.11811, abstract); up to 1σ or 2σ in BOSS, by EFT prior (arXiv:2208.05929, abstract).
- DES Y6 pre-registered its projection test, with pulls below 0.5σ in ΛCDM (arXiv:2601.14559, App. B); KiDS-Legacy reports mean, mode and MAP side by side (arXiv:2503.19441).
- Profile likelihoods are prior-free, not assumption-free: Wilks holds for ΛCDM; Σm_ν needs a boundary-corrected or Feldman–Cousins belt; w0 is doubtful (arXiv:2408.07700).
- DESI's σ is `Δχ²_MAP` with 2 dof: −12.5 gives 3.1σ, `Δ(DIC) = −8.7` (arXiv:2503.14738, Table 6). The same data give `ln B = −0.57 ± 0.26` (arXiv:2511.10631, abstract).
- The Bayes ratio scales with prior volume; parameter differences, suspiciousness and eigentension agree (arXiv:2012.09554, arXiv:1902.04029).
- A tension needs metric, subspace and reference: DES Y6 against the CMB is 1.8σ full-space, 2.6σ in S8 (arXiv:2601.14559); CMB against DESI DR2 is 1.6σ for ACT, 2.8σ for SPT (arXiv:2503.14452, arXiv:2506.20707; abstract of each).
- MultiNest gave narrower intervals and inconsistent evidences on DES Y1 (arXiv:2202.08233); DES Y6 and KiDS-Legacy use Nautilus (arXiv:2306.16923). Cosmology's `R − 1 < 0.01` tests chain means (arXiv:1304.4473), unlike `R̂` (arXiv:1903.08008).
- Simulation-based inference inflates variance at least as much as a mock covariance (arXiv:2412.02311); passing coverage is not validation (arXiv:2605.00980).
- Emulator accuracies (0.4%, arXiv:2106.03846; 1% dark-matter-only, arXiv:2010.11288; abstract of each) are interpolation errors; such error can miscalibrate a Gaussian likelihood (arXiv:2607.17942).
- Fisher forecasts underestimate w0–wa errors from geometrical probes by 30%–70% (arXiv:1205.3984, abstract).
- Blinding levels: catalogue (DESI, arXiv:2404.07282), data vector (DES, arXiv:1911.05929), three catalogues (KiDS); ACT DR6 and DES Y6 publish criteria and deviations (arXiv:2503.14452).
- The trial factor equals the prior-to-posterior volume ratio (arXiv:2007.13821).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

Covariance source, mocks against data-vector length, correction;
likelihood form; prior edges; mean, mode or MAP, projection per
model; boundary treatment; sampler, convergence, best-fit
search; `Δχ²` with its degrees of freedom; Bayes factor with priors; tension
metric, subspace and reference fixed in advance; independence of combined
data; emulator range and error; coverage plus a fixed-parameter
test; blinding level and post-unblinding changes:
`references/systematics.md` Sect. 17.

## Errors that recur
<!-- key: errors-that-recur -->

- "Hartlap-corrected" as the full treatment of mock noise; a variance factor quoted as an error-bar factor.
- `sqrt(Δχ²)` quoted as σ for two extra parameters.
- A `Δχ²` significance described as Bayesian evidence, or the reverse.
- "The tension is nσ" without metric and reference; quadrature sums for correlated data.
- An extended-model full-shape posterior mean read as the preferred value.
- A truncated-posterior width near a boundary read as sensitivity.
- A coverage plot or Fisher forecast offered as error-bar validation.
- Supernova compilations, or two releases of one survey, counted as independent.
- Citing a 1% emulator as a 1% theory error.

## Related skills
<!-- key: related-skills -->

- `cosmo-galaxy-clustering`: DESI full-shape priors, covariance, blinding.
- `cosmo-dark-energy-modified-gravity`: w0wa significances, critiques.
- `cosmo-weak-lensing`: S8, shear blinding, HSC.
- `cosmo-beyond-two-point`: simulation-based, field-level analyses.
- `cosmo-neutrinos-dark-matter`: Σm_ν boundary.
- `cosmo-tensions-anomalies`: cross-probe tensions, CMB anomalies.
- `cosmo-cmb`, `cosmo-supernovae`: Planck likelihoods; hierarchical models.
- `cosmo-simulations-mocks`, `cosmo-software-ecosystem`: mocks; codes.

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

Sizes, in thousands of tokens: L1 3k; open 9k; methods 23k; results 10k; surveys 8k; systematics 13k; deep/covariance-estimation 9k; deep/likelihood-form 7k; deep/model-comparison 9k; deep/pipeline-validation 7k; deep/profile-likelihoods 8k; deep/tension-metrics 7k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-statistics-inference`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-statistics-inference/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
