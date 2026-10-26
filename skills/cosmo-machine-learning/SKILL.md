---
name: cosmo-machine-learning
description: Use when reviewing, planning or fact-checking machine learning in cosmology — neural emulators (CosmoPower, DarkEmulator2), CNN or GNN summaries, IMNN, VMIM, neural posterior, likelihood or ratio estimation, normalising flows, diffusion or flow-matching generative models, NECOLA, baryon painting, CAMELS, Quijote, CosmoGrid, PLAsTiCC, ELAsTiCC, FAIR Universe, SuperNNova, SCONE, anomaly detection, symbolic regression, robustness across simulators, misspecification.
---

# Machine learning in cosmology — expert reference

Snapshot 2026-10-17. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Emulators, compression losses, NPE/NLE/NRE, generative models, solver corrections, classifiers, anomaly detection, symbolic regression | `references/physics-and-methods.md` |
| Training suites (Quijote, CAMELS, CosmoGrid), challenges (PLAsTiCC, ELAsTiCC, Beyond-2pt, FAIR Universe), survey uses, data locations | `references/surveys-and-data.md` |
| Emulator accuracy, neural-summary gains, SBI outcomes, classifier scores, robustness tests, history | `references/results.md` |
| Simulator dependence, misspecification, emulator error, overconfidence, training-set bias, reproducibility, blinding; referee list | `references/systematics.md` |
| Network gains, trust in simulations, interpretability, foundation models, next data, stale claims | `references/open-questions.md` |
| Cited-paper title, author, year | `references/sources.tsv` |
| Emulator design, accuracy requirement, error propagation | `deep/emulators.md` |
| Generative field models: training, validation, prior or posterior use | `deep/generative-models.md` |
| Networks correcting fast solvers; super-resolution; baryon painting | `deep/learned-simulation-corrections.md` |
| Classifier training: augmentation, balance, calibration | `deep/classification.md` |
| Network uncertainties, calibration, seed variance | `deep/uncertainty-reproducibility.md` |
| Saliency tests; symbolic-regression set-up | `deep/interpretability.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Emulator error is a residual against the training code: 99% of
  CosmoPower test non-linear corrections (HMcode) lie within 0.4%
  (arXiv:2106.03846, Sect. 3.2).
- Public non-linear P(k) emulators differ by a few per cent near
  k ~ 1 h/Mpc, with σ8- and w0-dependent trends (arXiv:2605.28596).
- The loss sets the ceiling: MSE summaries reach 81% of the full-field
  FoM, VMIM 100% (arXiv:2407.10877, abstract); on DES Y3
  lensing maps VMIM gave 60% more FoM(Ω_m, S8, w) than the earlier
  MSE-trained CNN (arXiv:2606.11309, abstract, Sect. 8.1).
- CNN gains over the power spectrum on survey S8: 16% (KiDS-1000,
  arXiv:2201.07771, abstract) and 5–24% (HSC Y1, arXiv:2301.01354,
  abstract), not the ≈ 5 times of noiseless maps (arXiv:1802.01212,
  abstract).
- Every benchmarked SBI algorithm can be overconfident; ensembles help
  (arXiv:2110.06581). Never multiply NPE posteriors across data sets
  (arXiv:2605.10719).
- KiDS-SBI: six-flow ensemble, 18 000 realisations, loss converged after
  5000 (arXiv:2404.15402, Sect. 5.4).
- Multi-fidelity field-level SBI: "60 simulations" in the abstract; the body
  needs N ~ 100–120 for reliable widths (arXiv:2606.23346).
- Robustness depends on the input: mass maps transfer between IllustrisTNG
  and SIMBA (arXiv:2109.10360), galaxy properties do not
  (arXiv:2201.02202); a positions-and-velocities GNN fails on a new
  sub-grid model (arXiv:2609.23982).
- Lyα P1D NPE trained on one CAMELS model biases σ8 by ~10% on the other;
  multi-domain training removes it (arXiv:2603.13011, abstract).
- Generative posteriors can match means and marginals yet miss the
  variance-field power by up to ~30% (arXiv:2606.10023, Sects. 5.2, 6.1).
- PLAsTiCC winner: 0.685 on the official weighted metric (arXiv:2012.12392,
  Fig. 7 caption); 0.468 is flat-weight (arXiv:1907.04690, abstract).
- NECOLA corrects COLA to sub-percent at k ≃ 1 h/Mpc from one training
  cosmology (arXiv:2111.02441).
- KiDS-1000 GCNN unblinded only after network–spectrum agreement and
  simulation-setting tests (arXiv:2201.07771).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

1. Training simulator, size, design; data inside its range.
2. Test on an unseen simulator: bias and calibration.
3. Compression loss, architecture, ensemble or single network.
4. Density estimator, stopping rule, simulation count.
5. Emulator test-set percentiles and full-likelihood comparison.
6. Goodness of fit and out-of-distribution check on data.
7. Classifier metric, class weights, unseen classes, calibration.
8. Explicit-likelihood comparison on the same cuts.
9. Code, weights, seeds and hyperparameters public; blinding conditions.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting a noiseless-simulation information gain as a survey gain.
- Treating an emulator's interpolation error as its theory error.
- Calling a network "robust" after one CAMELS-pair test.
- Reading an MSE summary as the data's information content.
- Multiplying NPE posteriors from independent data sets.
- Comparing classifier scores across metrics or class weights.
- Citing the multi-fidelity "60 simulations" (arXiv:2606.23346, abstract) without the body's
  threshold.
- Reporting one network seed or architecture as the result.

## Related skills
<!-- key: related-skills -->

- `cosmo-statistics-inference`: SBI coverage, TARP, simulation count;
  emulator error in likelihoods.
- `cosmo-beyond-two-point`: neural-summary and SBI results on data
  (SimBIG, DES Y3, LiFT); field-level inference.
- `cosmo-simulations-mocks`: simulation suites, gravity-only emulator
  comparison.
- `cosmo-photometry-photoz`: machine-learning photo-z.
- `cosmo-supernovae`: SN Ia photometric classification.
- `cosmo-data-pipelines`: deblending, imaging-systematics and
  spectral-classification networks.
- `cosmo-software-ecosystem`: code versions and maintenance.
- `cosmo-weak-lensing`, `cosmo-lyman-alpha`, `cosmo-reionization-21cm`:
  probe-specific uses.

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

Sizes, in thousands of tokens: L1 3k; open 4k; methods 12k; results 6k; surveys 5k; systematics 9k; deep/classification 8k; deep/emulators 9k; deep/generative-models 10k; deep/interpretability 6k; deep/learned-simulation-corrections 7k; deep/uncertainty-reproducibility 7k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-machine-learning`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-machine-learning/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
