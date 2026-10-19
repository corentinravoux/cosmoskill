# Clustering redshifts and shear-ratio calibration — cosmo-photometry-photoz dossier

Scope: how a clustering-redshift (WZ) measurement is set up in current
analyses (reference slicing, scale range and weighting, estimator,
reference bias, model of the unknown sample's bias, covariance), how the
measured cross-correlations become a constraint on n(z) (shift fits,
Gaussian-process reconstruction, importance sampling of SOM
realisations), and how a shear-ratio likelihood is built; with the
choices DES, KiDS and Euclid made and their stated reasons.
Snapshot: 2026-10-19.
From: Newman & Gruen 2022 review, Sect. 3.3, 4.2.6; DES and KiDS redshift
working groups (copied from `references/subtopics.tsv`).

Already in L2, not repeated here: the principle and Newman's error
scaling, Ménard's all-scale and cell-by-cell variants, the results table
of KiDS, DES Y3/Y6 and Euclid mocks
(`physics-and-methods.md#clustering-redshifts`); the shear-ratio idea and
DES Y3 gains (`physics-and-methods.md#shear-ratios`); the systematics
budget (magnification, bias evolution, small scales, reference coverage)
and the KiDS-Legacy and DES Y6 bin-by-bin numbers
(`systematics.md#clustering-redshift-systematics`,
`results.md#ensemble-n-z-characterisation`); whether WZ is good enough
for Stage IV (`open-questions.md#are-clustering-redshifts-good-enough-for-stage`).
The DES Y6 shear-ratio configuration and its consistency results, and how
n(z) uncertainties enter the 3×2pt likelihood, are in `cosmo-weak-lensing`
(`deep/ggl-3x2pt.md`, `references/systematics.md`). Fibre-collision
weights of the reference sample belong to `cosmo-galaxy-clustering`.

Symbols. u: the unknown (photometric) sample or tomographic bin; r_i: the
i-th thin redshift slice of the spectroscopic reference sample;
w_ur, w_rr: scale-averaged angular cross- and auto-correlation
amplitudes; b_u, b_r: linear galaxy biases; α_u, α_r: magnification
coefficients; w_m(z): projected matter correlation with the same scale
weighting; r_p: transverse comoving (or physical, as each paper states)
separation; W(θ) or W(r_p): scale weight; n_u(z): normalised redshift
distribution of u; D_z or δz: shift of a model n(z); s: stretch. Notation
follows the DES Y6 paper (d'Assignies et al. 2025, arXiv:2510.23565)
unless a step names another paper; KiDS and Euclid write s for the
spectroscopic sample and p for the photometric one.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Slice the reference sample and fix the scales
<!-- key: step-1-slice-the-reference-sample-and-fix-the -->

- **DES Y6.** Ten logarithmic angular bins spanning r_p = 1.5–5 Mpc,
  combined with W(θ) = θ⁻¹/Σ Δθ_i θ_i⁻¹, pair counts with TreeCorr
  [src: arXiv:2510.23565, Sect. II.2.1]. The lower bound "is a compromise
  between measurement precision and modeling accuracy, while the upper
  bound is fixed by the need to maintain statistical independence from
  the cosmological w(θ) measurements" [src: Sect. IV.2.2]. Reference
  slices of Δz = 0.05 [src: Fig. 8 caption].
- **Euclid (Flagship 2).** Scanning 0.05–10 Mpc on five 1000 deg²
  patches, the S/N peaks near 1 Mpc in the low-z bin and near 2 Mpc in the
  others while χ² stays roughly flat; 1.5–5 Mpc is "nearly optimal" in
  S/N, avoids the one-halo regime and the cosmology scales [src:
  arXiv:2505.10416, Sect. 4.4]. Among W ∝ r_p^γ with γ ∈ {−1, 0, 1},
  inverse-scale weighting applied to the correlation functions (not to the
  per-scale n(z)) gives the lowest RMS and highest S/N, because scales
  near 1.5 Mpc have more signal and less deviation than those near 5 Mpc
  [src: Sect. 4.5]. With logarithmic binning the effective weight is
  W_eff ∝ r_p^(γ+2) [src: Sect. 4.2]. Optimal slicing 0.04 ≤ Δz ≤ 0.06,
  Δz = 0.05 adopted: narrow slices are more sensitive to bin-edge
  modelling, magnification and RSD, wide ones flatten the shape and break
  the constant-bias assumption within a slice [src: Sect. 4.6].
- **KiDS-Legacy.** One bin of transverse physical separation 0.5 < r ≤ 1.5
  Mpc, 32 linear redshift bins over 0.05 ≤ z < 1.6 (1.4 on MICE2)
  [src: arXiv:2503.19440, Sect. 5.2]. On MICE2, excluding r < 0.5 Mpc gave
  the least biased shifts and 1.5 Mpc as upper limit kept good S/N
  [src: Sect. 6.2.2]. These scales are larger than in earlier KiDS work
  [src: Sect. 5.2, footnote 11].

Euclid notes that earlier choices (KiDS, HSC, DES) were driven by small
reference samples and set at the S/N peak, and that larger scales would
need a more complex covariance, "never implemented in practice" [src:
arXiv:2505.10416, Sect. 4.4].

### Step 2. Measure the correlations
<!-- key: step-2-measure-the-correlations -->

DES uses the Davis–Peebles estimator, Σ Δθ W (D_xD_y − R_xD_y)/R_xD_y
(Eq. 19), when no random catalogue exists for the unknown sample (sources),
and Landy–Szalay, Σ Δθ W (D_x − R_x)(D_y − R_y)/R_xR_y (Eq. 20), when it
does (MagLim lenses) [src: arXiv:2510.23565, Sect. II.2.1, IV.1]. LS has
smaller bias and variance; DP is more exposed to mask shapes and edges
[src: Sect. IV.1]. KiDS (yet_another_wizz 2.6.0) uses LS for all
auto-correlations and DP for cross-correlations with the random catalogue
of the spectroscopic sample, "since most of the spectroscopic surveys
provide well-established random catalogues"; regions are defined by
k-means on sky coordinates and pairs are counted across region boundaries
[src: arXiv:2503.19440, Sect. 5.1]. Euclid compared weighting the ratio of
pair counts with weighting the pair counts themselves: no difference in
uncertainties, so the simpler first form was kept [src: arXiv:2505.10416,
Sect. 4.2].

### Step 3. Calibrate the reference bias
<!-- key: step-3-calibrate-the-reference-bias -->

From the reference auto-correlation in each slice,
b_r,i = [w_r,i r,i / ∫ dz n_r,i² w_m]^½ (arXiv:2510.23565, Eq. 6), with no
bias evolution inside a narrow slice and no magnification [src: Sect.
II.1.1]. KiDS writes the bias-corrected estimate
n_p(z) = w_sp / [Δz² w_ss w_pp]^½ = N_CC/√w_pp (Eq. 4) and corrects only
the reference term w_ss, measured in the same redshift and separation bins
as the cross-correlation; the source-sample bias evolution is left
uncorrected, mitigated by tomographic binning and shown small in earlier
work [src: arXiv:2503.19440, Sect. 5.2]. DES checks that b_r from 1.5–5
Mpc and 5–15 Mpc agree, so neither scale-dependent bias nor fibre
collisions matter at the fiducial range, while 0.1–1.5 Mpc biases differ;
BOSS/eBOSS bias jumps near z = 0.2 and 0.7 follow selection changes
[src: arXiv:2510.23565, Sect. IV.2.2].

### Step 4. Model the cross-correlation and its errors
<!-- key: step-4-model-the-cross-correlation-and-its -->

DES Y6 writes the unknown distribution on sawtooth (triangle) basis
functions, n_u(z) = Σ_j f_u^j K_j(z) (Eqs. 7–8), chosen because they are
continuous and vanish at z → 0, and models

  ŵ_ur_i = Σ_j f_u^j [b_u,j A_j,r_i (1 + S_ur_i) + α_u,j b_r_i D_ij
  + b_u,j α_r_i D_ji]  (arXiv:2510.23565, Eq. 17),

with A_ji = b_r_i ∫ dz K_j n_r_i w_m (Eq. 10), D the magnification
kernels, and a systematic function S = Σ_{k≤M} s_uk √(2k+1)/0.85 L_k(z̃)
on z̃ ∈ [−0.85, 0.85] (Eq. 18) [src: Sect. II.1.1, II.1.3]. Because A is
not diagonal, correlations at the edges of the reference slices are
modelled, replacing the one-bin (Limber) approximation [src: Sect. IV.1].
w_m uses CCL's non-linear halofit power spectrum with linear bias, judged
adequate down to 1.5 Mpc [src: Sect. II.1.1].

The order M and the prior widths come from Cardinal mocks run twice: a
"no systematics" case (true per-slice biases, idealised bins, LS) that
must recover the truth, and an "all systematics" case with the data's
ignorance; the ratio w/ŵ in the second case is fitted with Legendre
polynomials [src: Sect. IV.1]. Order 2 for MagLim bin 1, order 1 for
MagLim bins 2–6 and all four source bins [src: Sect. IV.1.1–IV.1.2]. The
priors are Gaussian centred at zero with σ equal to the best-fit Cardinal
amplitude, because the team trusts Cardinal for the size of the
systematics but not for their exact form; centring on the Cardinal best
fit was the rejected alternative [src: Sect. IV.1.1].

Euclid instead corrects the unknown sample's bias directly, comparing six
methods: M0 none, M1 reference only, M2 one bias per tomographic bin, M3
bias measured in photometric bins of Δz_photo = 0.1 then fitted by a
polynomial in z, M4 the same with 0.02, M5 truth [src: arXiv:2505.10416,
Sect. 3.3.1]. With both biases measured in the same slices,
n_p(z_i) = w_sp / [Δz √(w_ss w_pp)] (Eq. 49), valid also at next order in
the bias expansion [src: Sect. 3.3.1].

### Step 5. Estimate the covariance
<!-- key: step-5-estimate-the-covariance -->

- DES Y6: jackknife over 100 sub-regions of the BOSS overlap (~8 deg²,
  much larger than the ~2 Mpc correlation scale); covariances between
  different reference slices are set to zero, verified on data, on
  Cardinal and numerically; the resulting block-diagonal matrix (one
  N_u × N_u block per reference slice) is inverted without Hartlap
  correction, because zeroing suppresses the patch noise, and the
  diagonal of the inverse agrees with a Hartlap-corrected noisy one [src:
  arXiv:2510.23565, Sect. II.2.2].
- Euclid: jackknife over 200 regions with about a dozen data points, so
  Hartlap or Percival corrections are percent-level and neglected (Eq. 64)
  [src: arXiv:2505.10416, Sect. 3.4.2].
- KiDS-Legacy: spatial jackknife on k-means regions (bootstrap before);
  checked against halo-model analytic covariances, but the jackknife was
  kept because of the non-linear regime, HOD uncertainties and non-Limber
  connected terms [src: arXiv:2503.19440, Sect. 5.1].

### Step 6. Turn w into an n(z) constraint
<!-- key: step-6-turn-w-into-an-n-z-constraint -->

Three routes in current use:

1. **Shift fit of a model n(z) (KiDS).** n_model(z) = A n(z − D_z) (Eq. 5)
   with the SOM n(z) as template, a free amplitude A (the points are not
   normalised because of bias and systematics) and an extra error term
   s = [Δn_CC² + f²(1+z)²]^½ (Eq. 6) marginalised over f, because the data
   show scatter beyond their errors, worst in bins 5–6 at high z [src:
   arXiv:2503.19440, Sect. 5.4]. Five reference samples are measured
   separately and combined by inverse variance; BOSS, GAMA and 2dFLenS
   dominate below z ≈ 0.7, DESI above, VIPERS contributes little [src:
   Sect. 5.2]. MICE2 errors were inflated and values perturbed to match
   the data's lower S/N, a difference left unexplained [src: Sect. 5.3].
2. **Model-independent reconstruction (Euclid).** Shifted-stretched model
   n_model(z | s, δz) = s⁻¹ n((z − ⟨z⟩ − δz)/s + ⟨z⟩) (Eq. 72), whose δz
   and s are directly the mean and width errors, or a suppressed Gaussian
   process: GP draws (Matérn 3/2, length l = Δz/2), multiplied by
   S(x) = 1 − (1 − x)^k with k = 0.3 where the smoothed S/N falls below a
   threshold, renormalised, moments taken over the draws (Eqs. 75–77)
   [src: arXiv:2505.10416, Sect. 3.5.4–3.5.5]. The SSM with the true n(z)
   as template "may be overestimated" relative to real use with a SOM
   template, which is why the SGP is also run [src: Sect. 3.5.4, 4.6].
3. **Likelihood of SOM realisations (DES Y6).** With Gaussian
   likelihood, Gaussian priors on α_r, α_u and s_uk, and flat priors on
   b_u (Eqs. 21–22), the integral over (α, s) is analytic; b_u is profiled
   by Newton iterations with automatic differentiation (Eqs. 23–24) [src:
   arXiv:2510.23565, Sect. II.3]. About 10⁸ SOMPZ realisations are drawn,
   each kept with probability β p(w | n_i)/max p, β set so ~3000 survive;
   the survivors are compressed to a few modes and a density estimator
   gives the prior used in cosmology (Eq. 25) [src: Sect. II.4]. Lens bins
   are importance-sampled independently; source bins are concatenated to
   keep their cross-bin correlations, and the raw SOM realisations were
   too noisy for importance sampling to work, so components that do not
   affect the observables are projected out first [src: Sect. II.4].

### Step 7. Build a shear-ratio likelihood (DES Y3)
<!-- key: step-7-build-a-shear-ratio-likelihood-des-y3 -->

For one lens bin, γ_t^(l,s_i)/γ_t^(l,s_j) ≃ Σ⁻¹_crit,eff^(l,s_i) /
Σ⁻¹_crit,eff^(l,s_j) (Eqs. 3–5), exact only for an infinitely narrow lens
bin; DES Y3 instead models the ratios with the full 3×2pt tangential-shear
model, including magnification, intrinsic alignments and shear bias
(Sánchez et al. 2022, arXiv:2105.13542) [src: Sect. III.1]. Choices and
reasons:

- Three lowest lens bins, because they hold most of the S/N and the
  highest bins are dominated by magnification; for each lens bin, ratios
  of source bins 1, 2, 3 over bin 4, the highest-S/N measurement in the
  denominator to minimise noise bias: nine ratios [src: Sect. IV.1.1].
- Scales 2–6 h⁻¹ Mpc, the lower limit to stay out of the one-halo regime
  where TATT is not valid; the two nearly geometric ratios (l₁, s₃, s₄) and
  (l₂, s₃, s₄) use all scales from 2.5′ [src: Sect. IV.1.2, Table 2].
  Large-scale ratios (> 8 h⁻¹ Mpc to 250′) only validate [src: Sect.
  IV.1.2].
- Each ratio is a minimum-variance average over scales,
  r = σ_r² Dᵀ C_r⁻¹ r(θ) with C_r = J C_γ Jᵀ (Eqs. 24–27); scale-dependent
  ratios did not improve results [src: Sect. IV.1.3]. The 9 × 9 covariance
  comes from 10⁵ Gaussian realisations of the γ_t data vector drawn from
  the theory covariance [src: Sect. IV.1.4].
- Free parameters: one Δz per source and lens bin (widths too for
  MagLim), m per source bin, linear lens bias, five TATT parameters;
  magnification coefficients fixed [src: Sect. III.2.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

| Choice | Option A | Option B | What decides | Source |
|---|---|---|---|---|
| Scale range | 0.5–1.5 Mpc (KiDS-Legacy) | 1.5–5 Mpc (DES Y6, Euclid) | bias of shifts on mocks vs one-halo avoidance and independence from cosmology scales | arXiv:2503.19440, Sect. 6.2.2; arXiv:2510.23565, Sect. IV.2.2; arXiv:2505.10416, Sect. 4.4 |
| Unknown-sample bias | left uncorrected (KiDS) | systematic function with mock-set priors (DES); measured in Δz_photo = 0.1 bins, polynomial (Euclid M3) | Euclid: M1 suffices at low z, both biases needed at high z, M3 ≈ M5 and better than M4 | arXiv:2505.10416, Sect. 4.8.2 |
| Output | shift D_z of the SOM template (KiDS) | SSM/SGP moments (Euclid); importance weights on SOM realisations (DES Y6) | SSM inherits template shape; SGP gives weaker but realistic errors; importance sampling keeps SOM shape freedom | arXiv:2505.10416, Sect. 4.6; arXiv:2510.23565, Sect. II.4 |
| Estimator | DP (one random catalogue) | LS (both) | availability of randoms for the photometric sample | arXiv:2510.23565, Sect. II.2.1 |
| Systematics prior | centred on mock best fit | centred on zero, width = mock amplitude | how far the mock is trusted | arXiv:2510.23565, Sect. IV.1.1 |
| Covariance | jackknife | analytic halo model | non-linear regime, HOD and non-Limber uncertainty favour jackknife | arXiv:2503.19440, Sect. 5.1 |

Compared on the same mock: on MICE2, fitting KiDS CCs with the true n(z)
gives ⟨D_z⟩ within 0.01 of zero (except bin six) with scatter 0.005 in
bins 1–4, but fitting them with the SOM n(z) gives ⟨D_z⟩ = 0.014, 0.060,
0.056, 0.015, −0.016, −0.085: the shift absorbs the SOM–truth shape
difference [src: arXiv:2503.19440, Table 7 of the HTML rendering,
Sect. 6.2.2]. On real DES Y6 data, Fid (1.5–5 Mpc) and LS (5–15 Mpc) n(z)
agree within the systematic-function freedom; SS (0.1–1.5 Mpc) n(z)
differ by much more than their small errors [src: arXiv:2510.23565,
Sect. IV.2.2, App. D].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Scale range, weight | 1.5–5 Mpc, 10 log bins, W ∝ θ⁻¹ | DES Y6 | arXiv:2510.23565 | Sect. II.2.1 |
| Reference slicing | Δz = 0.05 | DES Y6; Euclid | arXiv:2510.23565; arXiv:2505.10416 | Fig. 8; Sect. 4.6 |
| Jackknife regions | 100 (~8 deg²) / 200 | DES Y6 / Euclid | arXiv:2510.23565; arXiv:2505.10416 | Sect. II.2.2; Sect. 3.4.2 |
| Systematic-function order | M = 2 (MagLim bin 1), 1 elsewhere | DES Y6 | arXiv:2510.23565 | Sect. IV.1.1–IV.1.2 |
| SOM realisations, survivors | ~10⁸ → ~3000 | DES Y6 | arXiv:2510.23565 | Sect. II.4 |
| Overlap area for WZ | 700 deg² BOSS–eBOSS | DES Y6 | arXiv:2510.23565 | Sect. IV.1 |
| Cosmology dependence of √w_m(z) | ~1% across DES Y3, KiDS-Legacy, Planck 2018 | DES Y6 | arXiv:2510.23565 | Sect. IV.1 |
| KiDS scales and bins | 0.5 < r ≤ 1.5 Mpc; 32 bins, 0.05 ≤ z < 1.6 | KiDS-Legacy | arXiv:2503.19440 | Sect. 5.2 |
| KiDS intrinsic-scatter amplitude f (data) | 0.06–0.10 per bin | KiDS-Legacy | arXiv:2503.19440 | Table 7 (HTML) |
| KiDS χ²/dof of shift fits (data) | 1.44, 1.04, 1.11, 1.03, 1.04, 1.14 | KiDS-Legacy | arXiv:2503.19440 | Table 7 (HTML) |
| MICE2 scatter of D_z^true | 0.005 (bins 1–4), 0.017, 0.044 (bins 5, 6) | KiDS-Legacy | arXiv:2503.19440 | Sect. 6.2.2 |
| Euclid slicing optimum | 0.04 ≤ Δz ≤ 0.06 | Flagship 2 | arXiv:2505.10416 | Sect. 4.6 |
| SGP settings | Matérn 3/2, l = Δz/2, k = 0.3 | Flagship 2 | arXiv:2505.10416 | Sect. 3.5.5 |
| Shear-ratio set | 3 lens bins × 3 ratios over source bin 4; 2–6 h⁻¹ Mpc | DES Y3 | arXiv:2105.13542 | Sect. IV.1.1–IV.1.2 |
| Shear-ratio covariance | 10⁵ realisations | DES Y3 | arXiv:2105.13542 | Sect. IV.1.4 |
| SR data vs 3×2pt best fit | χ²/ndf 11.3/9 (redMaGiC), 18.8/9, p = 0.03 (MagLim; threshold 0.01) | DES Y3 | arXiv:2105.13542 | Fig. 4 caption |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Bias evolution of the unknown sample** is the dominant WZ systematic
  in DES Y6 Cardinal mocks; a wider luminosity range in MagLim bin 1 needs
  a higher-order systematic function [src: arXiv:2510.23565,
  Sect. IV.1, IV.1.1]. Test: run the mock with and without true per-slice
  biases and fit w/ŵ.
- **Small scales.** Linear bias with non-linear P(k) holds visually down to
  r_p ≈ 1 Mpc, but SS-range biases and n(z) depart from Fid and LS [src:
  arXiv:2510.23565, Sect. IV.2.2]. Test: compare b_r and n(z) across
  three scale ranges.
- **Fibre collisions** lower auto-correlation biases at small separation;
  DES found no significant effect at 1.5–5 Mpc, also because BOSS/eBOSS
  and DESI references, with different collision properties, agree [src:
  arXiv:2510.23565, Sect. IV.1, IV.2.2, App. C]. KiDS could not include
  DESI pair weights in its estimator [src: arXiv:2503.19440, Sect. 5.3].
- **Excess scatter** in the measured CCs beyond their errors, worst in
  the high-z bins; absorbed by the f(1+z) term [src: arXiv:2503.19440,
  Sect. 5.4]. Organised random catalogues are named as a future fix
  [src: Sect. 5.4].
- **Mocks cleaner than data.** MICE2 CCs had much lower noise than the
  data, possibly from selection, small-scale clustering amplitude, uniform
  mock depth or fibre collisions; the mock noise was inflated by hand
  [src: arXiv:2503.19440, Sect. 5.3].
- **Template-shape leakage into D_z** (MICE2 SOM-template shifts up to
  0.06 in bin 2 against ≤ 0.005 with the true template) [src:
  arXiv:2503.19440, Table 7 of the HTML rendering].
- **Noisy realisations break importance sampling**: project out modes
  that do not affect the observables before weighting [src:
  arXiv:2510.23565, Sect. II.4].
- **Too little reference area to see small effects**: the "full-u-bin"
  edge systematic seen on 1000 deg² Euclid × DESI mocks was not detectable
  with 700 deg² [src: arXiv:2510.23565, Sect. IV.1].
- **Shear ratios with lens–source overlap** depend on IA and
  magnification; restrict to scales where TATT holds and check against
  large-scale ratios [src: arXiv:2105.13542, Sect. IV.1.2]. The MagLim
  ratio fit (p = 0.03) passed the 0.01 threshold set in advance [src:
  Fig. 4 caption].

## Reading list
<!-- key: reading-list -->

- Foundation: Newman 2008, arXiv:0805.1409 — the estimator and error
  scaling (summary in `physics-and-methods.md#clustering-redshifts`).
- Method: Ménard et al. 2013, arXiv:1303.4722 — all scales and
  photometric-space voxels.
- Application: d'Assignies et al. 2025, arXiv:2510.23565 — the most
  complete current recipe: basis-function model, systematic function from
  mocks, block-diagonal jackknife, profile likelihood, importance sampling.
- Method: d'Assignies et al. 2025, arXiv:2505.10416 — how scales,
  weights, slicing and bias-correction method were optimised on mocks;
  SSM versus SGP.
- Application: Wright et al. 2025, arXiv:2503.19440, Sect. 5–6 — KiDS
  choices, reference-only bias correction, shift fits with excess scatter.
- Method: Gatti et al. 2022, arXiv:2012.08569 — DES Y3 WZ with the
  systematic function the Y6 method extends.
- Critique: van den Busch et al. 2020, arXiv:2007.01846 — how the n(z)
  model used in the fit drives the bias (summary in L2).
- Method: Sánchez et al. 2022, arXiv:2105.13542 — shear-ratio
  construction, scale cuts, covariance by realisations.

## Not verified
<!-- key: not-verified -->

- The DES Y3 WZ method sections (arXiv:2012.08569) and the van den Busch
  et al. bias-mitigation equations were not re-read this session; only
  the L2 summaries are used for them.
- Bernstein et al. 2025 (mode compression and density estimators used
  after importance sampling) and Gatti & Vielzeuf et al. 2018 were cited
  by the DES Y6 paper but not read.
- The KiDS-Legacy shift fits are read in Table 7 of the HTML rendering;
  `systematics.md#clustering-redshift-systematics` cites the same values
  as Table 8, probably a version difference; the values agree. The
  Fig. 8 caption of the same paper quotes f = 0.14 ± 0.04 for the data
  in bin six, against 0.07 ± 0.04 in Table 7; the difference is left
  unresolved.
- A date-restricted search for 2025–2026 clustering-redshift papers was
  rate-limited this session; papers after the DES Y6, KiDS-Legacy and
  Euclid ones already in L2 may be missing.
