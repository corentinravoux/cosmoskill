# Emulator-based summary statistics (density split, kNN, WST, MFs) — cosmo-beyond-two-point dossier

Scope: how a simulation-emulator analysis of a non-perturbative clustering
statistic is built (training-set design over cosmology and HOD, the HOD
parametrisation and its priors, how box simulations are made to look like
the survey, measurement settings of density split, kNN, WST and Minkowski
functionals, network and loss, emulator-error estimate, likelihood), and how
to choose between the designs in use, with what was found when they were
compared on the same data.
Snapshot: 2026-10-18.
From: Beyond-2pt challenge (arXiv:2405.02252), Sects. V.1 (BACCO hybrid
emulator), V.5 (kNN), V.6 (density split) and VI.4 (galaxy–halo connection
models).

Already in L2, not repeated here: definitions and founding papers of each
statistic, the BOSS density-split and Minkowski-functional pipelines in
outline (query points, smoothing, covariance sum, fitted range)
(`physics-and-methods.md#alternative-clustering-statistics-density-split`);
the data values and claimed gains
(`results.md#alternative-clustering-statistics-on-survey-data`); emulator
error, the Nseries residuals, fixed θ_*, survey realism and HOD dependence
as systematics (`systematics.md#emulator-based-small-scale-statistics`); the
debate on whether the gains are real (`open-questions.md#are-the-factor-2-6-gains-real`).
How an emulator is built in general (target transforms, accuracy
requirements) is in `cosmo-machine-learning`, `deep/emulators.md`; HOD
models in general in `cosmo-galaxy-halo-connection`, `deep/hod-clf.md`.

## How it is done
<!-- key: how-it-is-done -->

Notation. 𝒞 is the cosmological parameter set, 𝒢 the galaxy–halo (HOD)
parameter set. HOD symbols, following arXiv:2309.16539: M_cut the minimum
halo mass for a central, σ the width of the central turn-on, M_1 the mass
hosting one satellite, α the satellite power-law index, κM_cut the minimum
mass for a satellite, α_vel,c and α_vel,s the central and satellite velocity
biases (0 and 1 mean no bias), B_cen and B_sat the environment-based
assembly-bias amplitudes, f_ic an incompleteness (downsampling) factor.
C_data, C_emu and C_sim are the sample-variance, emulator-error and
fixed-phase (training-volume) covariance terms. "Q_i" is the i-th density
quintile of the density-split statistic.

### Step 1. Choose the simulation suite and the cosmology grid
<!-- key: step-1-choose-the-simulation-suite-and-the -->

All four BOSS CMASS analyses use the 85 AbacusSummit "emulator" boxes
(c130–c181 plus the derivative grid), each (2 h⁻¹Gpc)³ with 6912³
particles, CompaSO halos at z = 0.5, spanning ω_cdm, ω_b, σ8, n_s,
dn_s/dln k, N_eff, w_0, w_a, with h set by matching θ_* to Planck 2018
[src: arXiv:2309.16539, Sect. 2.2.1, Eq. 6, Table 1]. All emulator boxes
share one phase seed [src: same]. Ranges: ω_cdm [0.103, 0.140], σ8
[0.687, 0.938], n_s [0.901, 1.025], w_0 [−1.27, −0.70], w_a
[−0.628, 0.621] [src: Table 1]. Held-out test cosmologies: c000–c004 and
c013 (density split), c001–c004 (WST, MFs), c001–c004 and c171–c175 (kNN)
[src: arXiv:2309.16539, Sect. 2.3.1; arXiv:2310.16116, Sect. IV.5;
arXiv:2501.01698, Sect. 3.5; arXiv:2405.02252, Sect. V.5.2].

### Step 2. Fix the HOD family and its prior
<!-- key: step-2-fix-the-hod-family-and-its-prior -->

| Analysis | HOD parameters | Stated reason | Place |
|---|---|---|---|
| Density split (SUNBIRD) | 9: M_cut, M_1, σ, α, κ, α_vel,c, α_vel,s, B_cen, B_sat; B shifts log M_cut and log M_1 by B(δ_m − 0.5), δ_m the matter density in a 5 h⁻¹Mpc top-hat around the halo excluding the halo (Eq. 9) | environment traces the halo properties that control occupation in hydro and SAM models; velocity bias is observed for CMASS centrals; DSC is meant to constrain environment effects | arXiv:2309.16539, Sect. 2.2.2, Eqs. 7–10 |
| WST | 7: the five vanilla parameters and two velocity biases; no assembly bias | assembly bias acts on smaller scales than those used; checked on a UniverseMachine mock; acknowledged as a potential systematic | arXiv:2310.16116, Sect. IV.2 |
| MFs | 7: as WST | — (same family as WST) | arXiv:2501.01698, Sect. 3.2, Table 1 |
| kNN (Beyond-2pt) | 10: five vanilla, f_ic, two velocity biases, assembly bias against concentration or environment, a baryonic modulation s | model selected among three by goodness of fit, evidence and cross-prediction between RD-kNN, DD-kNN and the 2PCF | arXiv:2405.02252, Sect. V.5.2, V.5.4 |

Training ranges (DSC): log M_cut [12.4, 13.3], log M_1 [13.2, 14.4], log σ
[−3, 0], α [0.7, 1.5], κ [0, 1.5], α_vel,c [0, 0.5], α_vel,s [0.7, 1.3],
B_cen [−0.5, 0.5], B_sat [−1, 1] [src: arXiv:2309.16539, Table 1]. WST and
MFs use wider κ [0, 8], α_vel,s [0, 1.5], log M_1 [13, 15] [src:
arXiv:2310.16116, Table 1; arXiv:2501.01698, Table 1]. kNN priors:
log M_cut U[12.0, 14.5], log M_1 U[13, 15], log σ U[−3.5, 1.5], κ U[0, 2],
α_vel,s U[0.2, 1.8], B_cent, B_sat U[−1, 1] [src: arXiv:2405.02252,
Eq. 28].

Density matching. Mocks denser than the target are randomly downsampled
(f_ic); mocks below it are discarded: 151 474 of 229 500 WST mocks kept at
n̄ = 2.9 × 10⁻⁴ h³Mpc⁻³; about 18% of 53 125 MF variations discarded at
2.4 × 10⁻⁴ [src: arXiv:2310.16116, Sect. IV.5; arXiv:2501.01698, Sect. 3.5].
Discarding imposes a non-uniform prior on the HOD (and cosmology); the MF
analysis emulates n̄(θ) and imposes it as a hard prior (Eq. 23) [src:
arXiv:2501.01698, Sect. 3.6.1].

### Step 3. Make the box look like the survey
<!-- key: step-3-make-the-box-look-like-the-survey -->

Three solutions are in use, in increasing realism.

1. **Periodic box with AP only (density split).** Galaxies are moved to
   redshift space along three axes, and positions and box sides are scaled
   by q_⊥ and q_∥ of each simulation against the fiducial cosmology, giving
   non-cubic periodic boxes; grid cell and smoothing are kept fixed in the
   distorted box to mimic the observational choice [src: arXiv:2309.16539,
   Sect. 2.2.3, 2.2.4]. Footprint, radial selection and fibre collisions are
   *not* modelled; their effect is tested on 84 Nseries cut-sky mocks (L2).
2. **Cut-sky mocks from the box (WST).** Because the WST "is sensitive to
   the survey geometry through the successive wavelet convolutions" and no
   window model exists, each cube is downsampled to constant n̄, cut to the
   CMASS NGC and SGC footprints over 0.4613 < z < 0.5692 with radial RSD,
   converted back with the fiducial cosmology (AP), and turned into an FKP
   field with 50 × randoms [src: arXiv:2310.16116, Sect. IV.3, IV.4.1,
   Eqs. 13–16]. The data carry fibre-collision, redshift-failure and
   systematic weights; the mocks carry none [src: same].
3. **Remapped box with veto masks (MFs).** The box is remapped to a
   1.414 × 2.828 × 2.0 cuboid (volume-preserving), placed to contain both
   caps over 0.45 < z < 0.58, cut with all DR12 veto masks, regions of
   completeness below 0.9 removed, and downsampled to constant
   n̄ = 2.4 × 10⁻⁴; three rotations are averaged [src: arXiv:2501.01698,
   Sect. 3.3]. Reason: forward-model what cannot be corrected, so that
   data–mock differences come from cosmology and HOD only [src: same].

### Step 4. Measure the statistic
<!-- key: step-4-measure-the-statistic -->

| Statistic | Settings | Data-vector size | Place |
|---|---|---|---|
| Density split | grid 5 h⁻¹Mpc, Gaussian R_s = 10 h⁻¹Mpc, N_query = 5 N_gal, 5 quintiles; Q_2 dropped because the quintile CCFs sum to zero up to shot noise; ℓ = 0, 2; 241 μ bins; s bins of 1 (0–4), 3 (4–30), 5 h⁻¹Mpc (30–150) | 648 with the 2PCF | arXiv:2309.16539, Sect. 2.2.4, 2.3.2; arXiv:2309.16541, Sect. 2.2.2 |
| WST | box 2700 h⁻¹Mpc, NGRID = 270, TSC, Gaussian σ = 0.8 cell (8 h⁻¹Mpc), J = 4 scales, L = 4 orientations, q = 0.8, modified KYMATIO for masked fields; about 60 s per mock on a GPU | 76 coefficients | arXiv:2310.16116, Sect. IV.4.1 |
| kNN (RD and DD) | k = 1–9; 8 log bins in r_p from 0.63 to 63 h⁻¹Mpc, 5 in r_π from 0.5 to 32 h⁻¹Mpc; bins with CDF < 0.05 or > 0.95 removed to Gaussianise; DD cut at r_p > 5 h⁻¹Mpc | 114 (RD), 144 (DD) | arXiv:2405.02252, Sect. V.5.1, V.5.4 |
| MFs | four functionals of the excursion sets, smoothing ≥ 15 h⁻¹Mpc (L2) | — | arXiv:2501.01698 |

The kNN binning is designed for non-linear and quasi-linear scales and is
"not sensitive to large-scale features such as the BAO by design"; the k
range is "fairly arbitrary" [src: arXiv:2405.02252, Sect. V.5.1].

### Step 5. Train the emulator
<!-- key: step-5-train-the-emulator -->

| Analysis | Training set | Network and loss | Place |
|---|---|---|---|
| Density split | 85 cosmologies × 100 HODs (Latin hypercube of 8500), 80/20 train/validation by cosmology | fully connected, SiLU, Gaussian negative log-likelihood (mean and σ_pred), AdamW, batch 256, dropout, learning rate ÷10 on plateau to 10⁻⁶, Optuna over 200 trials; separate networks for 2PCF, DS ACF, DS CCF | arXiv:2309.16539, Sect. 2.2.3, 2.3.1, Eq. 13 |
| WST | 85 × 2700 HODs, 151 474 kept, each cut twice (NGC, SGC) | 3 layers × 300, GELU, Adam, MSE weighted by the diagonal of the CMASS covariance | arXiv:2310.16116, Sect. IV.5 |
| MFs | 500 HODs per cosmology (42 500) plus 125 × 85; 32 812 train, 8197 validation, 2512 test | 4 × 512, SiLU, AdamW, batch 64, rate 10⁻³ halved after 30 stagnant epochs; inputs and outputs standardised; Optuna found no improvement | arXiv:2501.01698, Sect. 3.2, 3.5 |
| kNN | MCMC in HOD space against the target at each cosmology, 20 000 evaluations per box, samples with log L > −9000 kept | 5 × 500, RReLU, Adam, MSE weighted by covariance diagonal | arXiv:2405.02252, Sect. V.5.2 |

The 100 HODs per cosmology of SUNBIRD were "a compromise between reducing
the emulator error and increasing the computational cost" [src:
arXiv:2309.16539, Sect. 2.2.3]. The kNN design concentrates training near
the maximum-likelihood region to improve precision there [src:
arXiv:2405.02252, Sect. V.5.2].

### Step 6. Estimate the emulator error and build the covariance
<!-- key: step-6-estimate-the-emulator-error-and-build -->

The network's own σ_pred was over-confident: test-set z-scores have a
variance about 15% above unity, so it is ignored and C_emu is taken as the
covariance of emulator-minus-simulation residuals over 600 test mocks,
which drops its parameter dependence [src: arXiv:2309.16539, Sect. 2.3.2,
3.1.2, Eq. 15]. C_sim is estimated from 1643 small (500 h⁻¹Mpc) boxes at
c000 with a CMASS-like HOD, rescaled by 1/64 to (2 h⁻¹Gpc)³; it is "almost
negligible" for CMASS but not for DESI [src: Eq. 16]. On data C_data comes
from 2048 Patchy mocks; C_data and C_sim get the Percival et al. factor
𝒫 = (N_s − 1)[1 + B(N_d − N_θ)]/(N_s − N_d + N_θ − 1) (arXiv:2309.16541,
Eqs. 15–20). The kNN analysis uses a jackknife over 125 cubes of
(400 h⁻¹Mpc)³ in each of 10 realisations (condition numbers 10⁷ and
4 × 10⁷) plus a hold-out emulator covariance [src: arXiv:2405.02252,
Sect. V.5.3].

### Step 7. Sample and validate
<!-- key: step-7-sample-and-validate -->

Gaussian likelihood (each paper has a Gaussianity appendix, not read
here), dynesty, uniform priors except a BBN prior ω_b = 0.02268 ±
0.00038 [src: arXiv:2309.16541, Eq. 21]. Validation ladder: held-out
AbacusSummit cosmologies; a non-HOD mock (Uchuu with SHAM ranked on a mix of
v_max and v_vir, including assembly bias, for density split; Uchuu with
UniverseMachine for WST) [src: arXiv:2309.16539, Sect. 3.2.4;
arXiv:2310.16116, Sect. V.2.2]; Nseries cut-sky mocks (L2).

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### How much HOD freedom
<!-- key: how-much-hod-freedom -->

Fixing assembly or velocity bias moves σ8 down in the BOSS density-split
fit, through correlations with α, α_vel,s and B_sat; the data prefer
negative B (galaxies in denser environments) [src: arXiv:2309.16541,
Sect. 4.4.4]. In the challenge the same omission moved σ8 and n_s down
within 1σ, and the extensions were kept to be robust to such effects in
the mocks [src: arXiv:2405.02252, Sect. V.6.4]. Freeing assembly bias also
costs precision: the MF paper attributes part of DSC's wider errors to the
extra B degeneracies [src: arXiv:2501.01698, Sect. 6.1]. For kNN, DD
statistics below r_p = 5 h⁻¹Mpc failed the robustness tests for all three
HOD models after unmasking, "subject to either error miscalibration or
model misspecification, even within the HOD framework" [src:
arXiv:2405.02252, Sect. VI.4, VI.4.1].

### Emulator error in or out
<!-- key: emulator-error-in-or-out -->

Dropping C_emu and C_sim more than doubles the BOSS DSC precision without
moving the means, but biases the fit to the Nseries mean at more than 3σ
down to 1 h⁻¹Mpc [src: arXiv:2309.16541, Sect. 4.4.4]. In the challenge the
largest effect of dropping it is on n_s [src: arXiv:2405.02252, Sect.
V.6.4]. A test-set C_emu computed over the whole prior may overestimate
errors near the best fit (the DSC team's stated caveat), which is what the
kNN high-likelihood training addresses [src: arXiv:2405.02252, Sect. V.6.4,
V.5.2].

### Number of HOD draws
<!-- key: number-of-hod-draws -->

100 (DSC), 500 (MFs), 2700 (WST) per cosmology; the MF paper finds a
"considerable improvement" in constraining power if the emulator error is
reduced, and suggests WST's tighter errors partly come from its larger
training set and its smaller smoothing scale (about 8 against
15 h⁻¹Mpc) [src: arXiv:2501.01698, Sect. 3.2, 6.1].

### Small scales
<!-- key: small-scales -->

In density split, scales from 30 down to 1 h⁻¹Mpc add little: the
correlation functions do not see clustering below R_s = 10 h⁻¹Mpc beyond the
smoothed density PDF, and emulator and training errors dominate there [src:
arXiv:2405.02252, Sect. VI.4, V.6.4]. On BOSS data the DSC-only σ8 is
0.768 +0.037/−0.043, below the 2PCF-only value; using only Q_0 and Q_4
costs 9% on ω_cdm, since most information sits in the extreme quintiles;
monopole only costs 18%, 13% and 18% on ω_cdm, σ8 and fσ8 [src:
arXiv:2309.16541, Sect. 4.4.4].

### Same data, different statistics
<!-- key: same-data-different-statistics -->

On BOSS CMASS with AbacusSummit emulators [src: arXiv:2501.01698, Table 5]:

| Statistic + 2PCF | ω_cdm | σ8 | n_s | h | fσ8 |
|---|---|---|---|---|---|
| MFs | 0.1172 +0.0020/−0.0023 | 0.783 ± 0.026 | 0.966 +0.019/−0.015 | 0.6889 +0.0075/−0.0065 | 0.453 ± 0.016 |
| Density split | 0.1201 ± 0.0022 | 0.792 ± 0.034 | 0.970 ± 0.018 | 0.6793 ± 0.0070 | 0.462 ± 0.020 |
| WST | 0.1241 ± 0.0011 | 0.795 ± 0.019 | 0.924 ± 0.01 | 0.669 ± 0.0049 | 0.469 ± 0.012 |

MFs and WST + 2PCF differ by 2.9σ in ω_cdm, 2.1σ in n_s and 2.3σ in h; the authors
"can't give a straightforward explanation" [src: arXiv:2501.01698,
Sect. 6.1]. The pipelines differ in HOD prior ranges, survey forward model
(Step 3), smoothing scale and training-set size, so the comparison does not
isolate the statistic. L2 notes that agreement in σ8 is not independent
confirmation; the disagreement in ω_cdm, n_s and h shows that the shared
ingredients do not force agreement either.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Emulator-error z-score variance | ≈ 1.15 (σ_pred over-confident) | DSC | arXiv:2309.16539 | Sect. 3.1.2 |
| C_emu test mocks; C_sim boxes | 600; 1643 × (500 h⁻¹Mpc)³, scaled by 1/64 | DSC | arXiv:2309.16539 | Eqs. 15–16 |
| Target densities | 3.5 × 10⁻⁴ (DSC), 2.9 × 10⁻⁴ (WST), 2.4 × 10⁻⁴ h³Mpc⁻³ (MFs) | CMASS | arXiv:2309.16539; arXiv:2310.16116; arXiv:2501.01698 | Sect. 2.2.3; IV.3; 3.3 |
| Fit quality on CMASS | χ²/dof = 1.66 (2PCF + DSC, 635 dof), 1.06 (2PCF) | DSC | arXiv:2309.16541 | Table 2 |
| Nseries vs CMASS monopole | χ² = 30 for 23 dof, about 2σ | DSC | arXiv:2309.16541 | Sect. 4.4.1 |
| Uniform ω_b prior | means move < 0.2σ, ω_cdm precision −15% | DSC | arXiv:2309.16541 | Sect. 4.4.4 |
| N_eff free | ω_cdm error × 2.4 | DSC | arXiv:2309.16541 | Sect. 4.4.4 |
| WST coefficients | 76 (J = 4, L = 4, q = 0.8) | WST | arXiv:2310.16116 | Sect. IV.4.1 |
| kNN data vector | 114 RD, 144 DD bins; jackknife 125 × (400 h⁻¹Mpc)³ | Beyond-2pt | arXiv:2405.02252 | Sect. V.5.1, V.5.3 |
| MF remap cuboid | 1.414 × 2.828 × 2.0 (box units), three rotations | MFs | arXiv:2501.01698 | Sect. 3.3 |
| MF vs WST + 2PCF | 2.9σ (ω_cdm), 2.1σ (n_s), 2.3σ (h) | CMASS | arXiv:2501.01698 | Sect. 6.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Emulator uncertainty taken from the network.** Over-confident by about
  15% in variance; use test-set residuals [src: arXiv:2309.16539, Sect.
  3.1.2].
- **Emulator error left out.** More than 3σ bias on a large-volume mock
  [src: arXiv:2309.16541, Sect. 4.4.4]; the challenge's BACCO hexadecapole
  case is in L2.
- **Data not described by any model in the family.** CMASS fits have lower
  Bayesian evidence than every one of 84 Nseries mocks, even with
  s_min = 50 h⁻¹Mpc, which the authors read as possible residual systematics
  in the CMASS catalogue not removed by the weights [src: arXiv:2309.16541,
  Sect. 4.4.1]. Test: evidence or χ² of the data against the distribution
  over mocks.
- **Density cut as a hidden prior.** Discarding low-density HOD draws
  reshapes the HOD prior; model it explicitly [src: arXiv:2501.01698,
  Sect. 3.6.1].
- **Box-trained statistic applied to a survey.** Geometry-sensitive
  statistics need cut-sky training mocks (WST, MFs); for density split the
  Nseries test is the only check (L2). Mocks carry no fibre-collision or
  systematic weights while data do (WST) [src: arXiv:2310.16116, Sect.
  IV.4.1].
- **HOD mocks validating HOD models.** The challenge mocks were HOD-based,
  which "gives HOD-based modeling approaches an inherent advantage"; future
  suites should be consistent with data and built on assumptions different
  from those of the tested models [src: arXiv:2405.02252, Sect. VI.4.1].
- **AP information absent from the test.** The challenge redshift-space
  mocks had no AP distortion, which density split exploits efficiently, so
  its relative gain was not tested there [src: arXiv:2405.02252,
  Sect. V.6.4, VI.4].
- **Smoothing and quantile choices** were inherited from CMASS and not
  re-tuned for other samples [src: arXiv:2405.02252, Sect. V.6.4].

## Reading list
<!-- key: reading-list -->

- Method: Cuesta-Lazaro et al. 2023, arXiv:2309.16539 — SUNBIRD: HOD with
  environment bias, training design, emulator loss, C_emu and C_sim.
- Application: Paillas et al. 2023, arXiv:2309.16541 — BOSS DSC: fit
  quality, Nseries evidence test, robustness table.
- Application: Valogiannis, Yuan & Dvorkin 2024, arXiv:2310.16116 — WST
  configuration and cut-sky forward model.
- Application: Liu et al. 2025, arXiv:2501.01698 — MFs with remapped,
  vetoed mocks; density-cut prior; comparison table with DSC and WST.
- Method and critique: Beyond-2pt challenge, arXiv:2405.02252 — Sects.
  V.5–V.6 (kNN and DSC set-ups), VI.4 (non-linear scales, HOD-mock caveat,
  design of future suites).
- Foundation: Banerjee & Abel 2021, arXiv:2007.13342 — kNN-CDF definition.
- Foundation: Maksimova et al. 2021, arXiv:2110.11398 — AbacusSummit.

## Not verified
<!-- key: not-verified -->

- The kNN supporting papers cited as Yuan et al. in arXiv:2405.02252
  (methodology, HOD selection, Gaussianity) and the small-scale 2PCF
  hybrid-MCMC emulator compared in arXiv:2501.01698: not read, identifiers
  not recorded.
- The BACCO hybrid-EFT emulator set-up (arXiv:2405.02252, Sect. V.1): not
  read in this run.
- No DESI application of density split, kNN, WST or MFs to cosmology was
  found in a date-sorted search from 2025-06-01.
