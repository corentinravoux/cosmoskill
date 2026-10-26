# Blinding and internal-consistency tests — cosmo-weak-lensing dossier

Scope: how a lensing collaboration sizes its blinding shifts and why, which
tests it writes down and must pass before each unblinding stage and with
which thresholds, how internal-consistency splits are built and scored
(KiDS three tiers, DES posterior-predictive checks, HSC test tables), and
what was done when a test failed before or after unblinding.
Snapshot: 2026-10-18.
From: Pantos 2026 review (arXiv:2602.12238), Sect. 7.5; KiDS-Legacy
consistency paper (arXiv:2503.19442); DES Y6 posterior-predictive checks
(arXiv:2610.03447).

Already in L2 or a sibling, not repeated here: the blinding level of each
analysis in one line (`physics-and-methods.md#what-each-main-analysis-did`)
and the two lessons drawn by KiDS-Legacy and DES Y6
(`physics-and-methods.md#blinding`); the general table of blinding schemes
across probes (`cosmo-statistics-inference/references/physics-and-methods.md#blinding-strategies`);
how Δ_PPD is computed and why it is not a calibrated p-value
(`cosmo-statistics-inference/deep/tension-metrics.md`); the B-mode PTEs
that gated each unblinding (`systematics.md#psf-modelling-and-leakage`);
the investigation of DES Y6 lens bin 2 as a galaxy–galaxy lensing failure
(`deep/ggl-3x2pt.md`).

Symbols. Θ_ref: reference cosmology and nuisance parameters; ΔΘ: hidden
blinding shift; d̂: measured data vector; B(d̂): blinded vector; dm: added
multiplicative bias; f: shear-catalogue scaling factor; Δ_PPD: fraction of
posterior-predictive realisations less probable than the data (small =
inconsistent); P(A|B): Δ_PPD of subset A predicted from subset B; R:
Bayes ratio; S: suspiciousness; I: information ratio; N_Θ: effective number
of constrained parameters; d: difference of N_Θ between two models; TPD:
translated posterior distribution; N_eff: effective number of sampled
parameters in a χ²/ν.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Freeze the plan and the criteria first
<!-- key: step-1-freeze-the-plan-and-the-criteria-first -->

DES Y6 states the purpose as forcing "a large collaboration to codify the
criteria that will be used to detect internal inconsistencies in their data
and resolve them before knowing the results", and its lens-bin-2 decision
was taken under "a detailed analysis plan, which prevented any post hoc
decisions" (DES Collaboration 2026, arXiv:2601.14559) [src: Sect. IV.8].
HSC Y3 agreed to publish "regardless of the outcome" and not to change the
method after unblinding, and did not compare with Planck, DES or KiDS
before unblinding (Li et al. 2023, arXiv:2304.00702) [src: Sect. II.2].
HSC's 3×2pt criteria are explicit: code available and reviewed part by
part; S8 recovered within 0.5σ on synthetic and mock data vectors; the
internal-consistency table run; goodness of fit quantified for each of the
three blind catalogues (Sugiyama et al. 2023, arXiv:2304.00705) [src: Sect.
IV].

### Step 2. Choose the layers and size the shifts
<!-- key: step-2-choose-the-layers-and-size-the-shifts -->

**Shear-catalogue offsets.**

- *HSC Y3.* Two levels: a user-level dm₁ per analysis team, encrypted with
  the team leads' public keys, so that blinded catalogues cannot be
  compared across the cosmic-shear, Fourier and 3×2pt teams; and a
  collaboration-level dm₂ drawn as one of the triplets (−0.1, −0.05, 0),
  (−0.05, 0, 0.05), (0, 0.05, 0.1), with the true catalogue (dm₂ = 0) at a
  different index in each and the key held by one person outside the
  analyses; m_blind = m_true + dm₁ + dm₂ (arXiv:2304.00702) [src: Sect.
  II.2, Eq. 9]. The spacing 0.05 corresponds to about 0.05 in S8, chosen
  "to cover the S8 tension between weak-lensing and CMB observations"
  [src].
- *KiDS.* Three catalogues generated double-blind; two carry shape changes
  giving up to ±2σ in S8, and the true one is equally likely to give the
  highest, middle or lowest S8. All three were analysed until chains were
  run, the paper written and internally reviewed; only discussion and
  conclusions were written after unblinding (Wright et al. 2025,
  arXiv:2503.19441) [src: Sect. 3.3]. In KiDS-1000 the systematics and
  consistency chains were run for one blind only, then rerun for the true
  one (Asgari et al. 2020, arXiv:2007.15633) [src: App. F].
- *DES Y6.* η = arctanh e rescaled by 0.9 < f < 1.1 (arXiv:2601.14559)
  [src: Sect. IV.8]. Such a scaling "is approximately equivalent to a
  rescaling of σ8, though only in the linear regime", and no catalogue
  transformation was found that keeps a combined clustering-plus-lensing
  data set valid, which is why DES moved to data-vector blinding (Muir et
  al. 2020, arXiv:1911.05929) [src: Sect. 2.3].

**Data-vector shift.** B(d̂_i) = d̂_i + f_i^(add) with f^(add) = d(Θ_ref +
ΔΘ) − d(Θ_ref) (arXiv:1911.05929) [src: Eq. 7]. A multiplicative factor
d(Θ_ref + ΔΘ)/d(Θ_ref) was rejected because it "would rescale the noise ...
as well as the signal" and behaves unpredictably where d_i ≈ 0 [src:
Sect. 3, footnote 1]. The procedure: Θ_ref "in the middle of the range of
models considered feasible truths"; ΔΘ from a distribution "broader than
the preconceptions causing the confirmation bias", for example Δw four to
five times the forecast error [src: Sect. 3.1]. For DES Y3 3×2pt:
Δσ8 uniform in ±0.12, about the expected 3σ, and Δw in ±0.5, half the flat
prior; other parameters unshifted [src: Sect. 4.4.1]. The acceptance test
on 100 synthetic realisations: the change in best-fit χ² must stay below
30, "within a few percent of the standard deviation" √(2ν) for ν = 430,
i.e. Δχ²/ν = 0.07, against a Y1 unblinding criterion χ²/ν < 1.4; all
realisations passed [src: Sects. 4.4.2, 4.5].

The DESI DR1 × lensing 3×2pt modifies Eq. 7: the nuisance parameters at
both cosmologies are set by minimising the χ² to the data at that
cosmology, which minimises an upper bound on |Δξ| (Porredon et al. 2025,
arXiv:2512.15960) [src: Sect. 3.7, Eqs. 25–26]. Only Ωm and σ8 are blinded
and only galaxy biases optimised, with Ωm,fid = 0.3166, σ8,fid = 0.8120,
ΔΩm uniform in ±0.05 and Δσ8 in ±0.12 [src: Sect. 3.7].

LSST DESC packages the same transformation as Smokescreen, which computes
the shift with the same Firecrown likelihood used for inference and
encrypts the SACC file holding the true vector (Loureiro et al. 2026,
arXiv:2604.18111) [src].

**Parameter level.** HSC hides the y-axis values of data–model plots and
centres every posterior plot at zero (arXiv:2304.00705) [src: Sect. IV];
its internal tests are shown as shifts relative to the fiducial projected
mode (arXiv:2304.00702) [src: Sect. II.2]. DES Y6 runs chains whose
parameter values are not shown and, notably, does "not run chains on the
blinded data vectors" (arXiv:2601.14559) [src: Sect. IV.8].

### Step 3. Pass the stage-by-stage tests (DES Y6 as the worked example)
<!-- key: step-3-pass-the-stage-by-stage-tests-des-y6-as -->

1. Catalogue stage: the null tests of the shape catalogue, e.g. no
   correlation of shear with PSF properties [src: Sect. IV.8].
2. Data-vector stage: the null tests of ξ±, γ_t and w; all measurement and
   model choices are frozen before the data vector is unblinded [src].
3. Parameter stage, under ΛCDM and linear bias [src: App. A.1]:
   - goodness of fit Δ_PPD > 0.01 for ξ± (TATT and NLA), 2×2pt, 3×2pt and
     3×2pt in wCDM (arXiv:2601.14559) [src: App. A.1];
   - seven pairwise consistency checks, P(2×2pt|3×2pt), P(ξ±|3×2pt),
     P(w|2×2pt), P(γ_t|2×2pt), P(w|ξ± + γ_t), P(γ_t|ξ± + w),
     P(ξ±|2×2pt), each Δ_PPD > 0.01, except P(w|ξ± + γ_t), exempted in
     advance because simulations showed prior-volume effects give very
     small values even for self-consistent data (arXiv:2601.14559) [src:
     App. A.1];
   - χ²/ν at the MAP, with χ² = −2 ln P_MAP − 2 Σ ln Δθ_i so that Gaussian
     priors count in the fit [src: Eq. 15], and ν = N_data − N_eff, N_eff
     = N_sampled − Tr(C_P C_π⁻¹) [src: Eq. 16]; the MAP is the best of
     Powell searches started from the 20 highest-posterior samples (arXiv:2601.14559) [src:
     Sect. IV.5];
   - visual check that the nuisance parameters with tight Gaussian priors
     (source and lens n(z) modes, m, magnification α) do not push against
     their priors;
   - then the covariance is recomputed at the still-blind 3×2pt MAP, the
     chains rerun and Δ_PPD rechecked [src: Sect. IV.8].

### Step 4. Score internal-consistency splits (KiDS-Legacy three tiers)
<!-- key: step-4-score-internal-consistency-splits-kids -->

Each split is fitted twice: a fiducial model with one parameter set, and a
split model with duplicated cosmological and flat-prior parameters;
nuisance parameters with informative priors are shared, "since the
posterior distribution of the nuisance parameters is entirely driven by
the prior", except in the colour split, which gets separate δz and A_IA
(Stölzner et al. 2025, arXiv:2503.19442) [src: Sect. 3.2, Table 1]. The
subsets stay linked through the joint covariance [src: Sect. 4].

- **Tier 1, evidence.** log₁₀R = log₁₀Z_fid − log₁₀Z_split [src: Eq. 4];
  for correlated subsets Z_split ≠ Z_A Z_B and must come from the joint
  posterior. Because R depends on the prior, and duplication doubles the
  prior volume, the paper prefers the suspiciousness ln S = ln R − ln I
  [src: Eq. 6], converted with d = N_Θ^split − N_Θ^fid into p_t = ∫_{d−2 ln
  S}^∞ χ²_d(x) dx and N_σ = √2 erf⁻¹(1 − p_t) [src: Eqs. 7, 9–10]. N_Θ is
  estimated by χ² minimisation on mock data vectors, because common
  dimensionality estimators are biased; the Bayesian model dimensionality
  N_Θ/2 = ⟨ln L²⟩ − ⟨ln L⟩² is computed for comparison [src: Sect. 3.2.1,
  Eq. 8].
- **Tier 2, parameter shift.** Δθ = θ₁ − θ₂ per sample in the constrained
  subspace; V = ∫_{P(Δθ)<P(0)} P(Δθ) dΔθ from a kernel density estimate,
  m = √2 erf⁻¹(1 − V), equivalent to the Monte Carlo exact parameter shift
  of DES [src: Eqs. 11–14].
- **Tier 3, data space.** The TPD maps posterior samples to model vectors;
  data of subset A are simulated conditional on subset B with μ_A^sim =
  t_A(θ_B) + C_AB C_BB⁻¹ [d_B − t_B(θ_B)], C_A^sim = C_AA − C_AB C_BB⁻¹ C_BA
  [src: Eqs. 16–17]; p(A|B) is the fraction of samples with χ²[d_A^sim]
  > χ²[d_A] [src: Eqs. 18–19]; threshold p > 0.01 (arXiv:2503.19442) [src: Sect. 4.1.1].
  Because TPD p-values "can result in p-values that are biased low" when
  the two posteriors sit far apart, the paper reads them as conservative
  and calibrates only a split that fails [src: Sect. 3.2.3].

Splits used: each redshift bin against the rest, auto- against
cross-correlations, scales, north against south, red against blue (at
T_B = 3.0, about a third red, and T_B = 1.9, about 16% red), and joint
vectors of different statistics (arXiv:2503.19442) [src: Sects. 3.2, 4.2.2]. Red–blue
cross-correlations are left out of the data vector, because their mixed
signal "cannot be easily modelled", but enter through the covariance [src:
Sect. 4.2.2].

HSC Y3 3×2pt runs a pre-unblinding table of about thirty variants: 2×2pt
and cosmic shear alone, each lens sample removed, each nuisance fixed (Δz,
m, magnification, PSF, IA = 0 or 5), R_max = 30 h⁻¹Mpc, each of the six
fields alone, three photo-z codes for the source selection
(arXiv:2304.00705) [src: Table 2].

### Step 5. After unblinding
<!-- key: step-5-after-unblinding -->

State what changed. KiDS-1000: the δ_c definition was allowed to take both
signs and the ξ± chains rerun, with changes at the level of chain-to-chain
variation; the covariance iterated at the best fit moved S8 by less than
0.1σ (arXiv:2007.15633) [src: App. F]. DES Y6: the covariance was updated
to include HMCode2020 baryons and IA, with "no significant shifts"; lens
bin 2 was restored for a check (arXiv:2601.14559) [src: App. A.3, A.5].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

| Choice | Buys | Costs | Who |
|---|---|---|---|
| Catalogue-level multiple catalogues | blinds every downstream statistic, including ones not foreseen; no reanalysis after unblinding (arXiv:2304.00705) [src: Sect. IV] | three full analyses; KiDS-Legacy: comparison of shapes with earlier catalogues becomes an unblinding risk, which "hampered the diagnosis of subtle systematic effects" (arXiv:2503.19441) [src: Sect. 3.3] | KiDS, HSC |
| Catalogue scaling of e | one catalogue | ≈ σ8 shift only in the linear regime; cannot blind clustering (arXiv:1911.05929) [src: Sect. 2.3] | DES (first layer) |
| Additive data-vector shift | preserves χ² and cross-probe consistency checks | relies on the model; can push nuisance posteriors to prior edges (2 of the large-truth-shift realisations), a false alarm for a standard validation check; Δχ² grows when both blinding and truth shifts are large (arXiv:1911.05929) [src: Sect. 4.5] | DES Y3, Y6; DESI DR1 3×2pt; LSST DESC |
| Nuisance re-optimised at each cosmology | smaller ‖Δξ‖ bound | extra fits (arXiv:2512.15960) [src: Sect. 3.7] | DESI DR1 3×2pt |
| Parameter-level hiding only | cheap | data vector unprotected | HSC (as an extra layer) |
| PPD metric (Δ_PPD > 0.01; arXiv:2601.14559 [src: Sect. IV.8, App. A.1]) | works for correlated subsets, no parameter duplication | sensitive to covariance amplitude; some pairs dominated by prior volume | DES |
| Three tiers (evidence, parameter shift, TPD) | three views; TPD conservative | parameter duplication; N_Θ needs mocks; Bayes ratio prior-dependent | KiDS-Legacy |

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Catalogue m offsets | triplets of dm₂ spaced 0.05 (≈ 0.05 in S8) plus a per-team dm₁ | HSC Y3 | arXiv:2304.00702 | Sect. II.2, Eq. 9 |
| Catalogue S8 offsets | up to ±2σ, true catalogue at random position | KiDS-Legacy | arXiv:2503.19441 | Sect. 3.3 |
| Shape scaling | 0.9 < f < 1.1 on arctanh e | DES Y6 | arXiv:2601.14559 | Sect. IV.8 |
| Data-vector shift range | Δσ8 ± 0.12 (≈ 3σ), Δw ± 0.5 | DES Y3 3×2pt design | arXiv:1911.05929 | Sect. 4.4.1 |
| Blinding Δχ² tolerance | 30 for ν = 430 (Δχ²/ν = 0.07) | DES Y3 3×2pt design | arXiv:1911.05929 | Sect. 4.4.2 |
| Data-vector shift range | ΔΩm ± 0.05, Δσ8 ± 0.12 | DESI DR1 3×2pt | arXiv:2512.15960 | Sect. 3.7 |
| Unblinding threshold | Δ_PPD > 0.01 (goodness of fit and pairwise) | DES Y6 | arXiv:2601.14559 | Sect. IV.8, App. A.1 |
| First-attempt Δ_PPD, all data | 3×2pt 0.006; P(γ_t ∣ ξ± + w) 0.000; P(ξ± ∣ 2×2pt) 0.004 | DES Y6 | arXiv:2601.14559 | Table 7 |
| Δ_PPD without lens bin 2 | 3×2pt 0.059; P(γ_t ∣ ξ± + w) 0.053; P(ξ± ∣ 2×2pt) 0.049 | DES Y6 | arXiv:2601.14559 | Table 7 |
| MAP χ²/ν | 3×2pt 737.0/644.9 (p = 0.007) → 654.3/588.4 (p = 0.031) | DES Y6 | arXiv:2601.14559 | Table 8 |
| Non-linear-bias exception | P(γ_t ∣ w + ξ) stays below 1% after removing bin 2 (0.004) | DES Y6 | arXiv:2601.14559 | App. A.1, Table 7 |
| Internal-consistency threshold | p > 0.01 (TPD) | KiDS-Legacy | arXiv:2503.19442 | Sect. 4.1.1 |
| Redshift-bin splits | N_σ ≤ 1.39 in tiers 1–2 (suspiciousness 1.16σ for bin 2, 1.39σ for bin 4); all TPD p > 0.01 | KiDS-Legacy | arXiv:2503.19442 | Sects. 4.1.1, 6 |
| Pipeline recovery criterion | S8 within 0.5σ on mocks | HSC Y3 3×2pt | arXiv:2304.00705 | Sect. IV |
| Post-unblinding covariance iteration | < 0.1σ on S8 | KiDS-1000 | arXiv:2007.15633 | App. F |

## What goes wrong
<!-- key: what-goes-wrong -->

- **A test fails at the last blind stage.** DES Y6 saw several Δ_PPD below
  0.01 and a lens n(z) mode against its prior; after three iterations of
  blind inference and a review of most of the pipeline it removed the bin
  under the pre-written plan; restoring it after unblinding changed Ωm and
  σ8 by 0.4σ and S8 negligibly (arXiv:2601.14559) [src: Sect. IV.8, App.
  A.5]. The lesson the paper draws is procedural: the plan made the
  decision non-post-hoc.
- **The metric reacts to the covariance, not the data.** "A few percent
  change" in covariance amplitude moves Δ_PPD from 10⁻³ to 10⁻² [src:
  arXiv:2601.14559, App. A.3]. Test: recompute at the blind MAP and with
  the missing terms.
- **Prior volume fakes inconsistency.** P(w|ξ± + γ_t) gives tiny Δ_PPD on
  self-consistent simulations; DES exempts it in advance and marks such
  entries "–" [src: arXiv:2601.14559, App. A.1, Table 7]. KiDS shares
  informatively-constrained nuisances across split halves for the same
  reason [src: arXiv:2503.19442, Sect. 3.2].
- **Blinding triggers a false alarm.** Data-vector blinding with a large
  truth offset pushed galaxy-bias posteriors into hard prior bounds;
  suggested remedies: one member checks whether the collision is due to
  the shift, or several shifts at different Θ_ref [src: arXiv:1911.05929,
  Sect. 4.5].
- **Blinding hides a localised systematic.** KiDS-Legacy could not compare
  shapes with earlier catalogues; its first blinded sample failed the
  COSEBI B-mode test and an area with astrometric scatter was removed
  (`systematics.md#psf-modelling-and-leakage`) [src: arXiv:2503.19441,
  Sect. 3.3].
- **Bayes ratio read on Jeffreys' scale.** "Lacks a clear motivation and
  there is no consensus on when to report tension", and inflates with the
  duplicated prior volume; use suspiciousness with a mock-calibrated d
  [src: arXiv:2503.19442, Sect. 3.2.1].
- **TPD p-values biased low** for splits whose posteriors sit far apart;
  calibrate with simulations when a split fails [src: arXiv:2503.19442,
  Sect. 3.2.3].
- **Comparing with external results while blind.** Forbidden in HSC Y3
  (arXiv:2304.00702) [src: Sect. II.2]; DES Y6 adds that blinding matters
  most "when previous results have shown marginal evidence for failure of
  the ΛCDM model" (arXiv:2601.14559) [src: Sect. IV.8].

## Reading list
<!-- key: reading-list -->

- Method: Muir et al. 2020, arXiv:1911.05929 — the additive data-vector
  transformation, how to size ΔΘ, the Δχ² acceptance test.
- Method: Stölzner et al. 2025, arXiv:2503.19442 — three tiers of
  consistency metrics with split models and their equations.
- Method: Doux et al. 2026, arXiv:2610.03447 — the Gaussian-mixture Δ_PPD
  used by DES Y6 (see the statistics sibling).
- Application: DES Collaboration 2026, arXiv:2601.14559 — three blinding
  stages, the full unblinding test list (App. A, Tables 7–8).
- Application: Li et al. 2023, arXiv:2304.00702 — two-level catalogue
  blinding with encrypted offsets.
- Application: Sugiyama et al. 2023, arXiv:2304.00705 — unblinding
  criteria and a pre-unblinding table of variants.
- Application: Wright et al. 2025, arXiv:2503.19441 — catalogue blinding
  across three KiDS catalogues and its cost.
- Application: Porredon et al. 2025, arXiv:2512.15960 — a modified
  data-vector blinding with re-optimised nuisances.
- Code: Loureiro et al. 2026, arXiv:2604.18111 — Smokescreen, data-vector
  blinding with encryption for LSST DESC.
- Critique and practice: Asgari et al. 2020, arXiv:2007.15633 (App. F) and
  Heymans et al. 2020, arXiv:2007.15632 (App. H) — what changed after
  unblinding, and redundancy and code review from pixels to parameters.

## Not verified
<!-- key: not-verified -->

- Kuijken et al. 2015 (arXiv:1507.00738), the origin of the KiDS scheme,
  and the exact way the KiDS ±2σ shape changes are generated: not read
  this session.
- The DES Y6 catalogue and data-vector null-test papers (cited as [151],
  [41], [61], [146] in arXiv:2601.14559) and their pass criteria.
- The DES Y3 unblinding criteria beyond the p-value threshold recorded in L2, and
  the redMaGiC/MagLim switch of DES Y3 in relation to unblinding.
- Whether UNIONS-3500 and DECADE blinded and how.
