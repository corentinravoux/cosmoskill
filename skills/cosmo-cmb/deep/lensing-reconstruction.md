# CMB lensing reconstruction — cosmo-cmb dossier

Scope: how a lensing power spectrum is obtained from CMB maps step by step
(filtering, estimator, mean field, normalisation, N⁰/N¹ and Monte Carlo
corrections, noise immunity, validation), and how to choose between the
estimator variants in use; values already in the reference files are
pointed to, not repeated.
Snapshot: 2026-10-16.
From: Planck 2018 VIII (arXiv:1807.06210); ACT DR6 and SPT-3G D1 lensing
papers (arXiv:2304.05202, arXiv:2608.31136); Simons Observatory science
goals (arXiv:1808.07445), Sect. V.

Already in L2, not repeated here: the estimator definitions and the table of
pipelines as run (`physics-and-methods.md#quadratic-estimators`), the three
lensing amplitudes and their fiducials
(`physics-and-methods.md#three-lensing-amplitudes-that-must-not-be`), the
foreground-bias sizes (`systematics.md#foregrounds-in-lensing-reconstruction`)
and the per-analysis systematic tables
(`systematics.md#act-dr6-lensing-qu-et-al-2023-arxiv-2304-05202`,
`systematics.md#planck-2018-lensing-planck-collaboration-2018`,
`systematics.md#spt-3g-d1-lensing-omori-et-al-2026-arxiv-2608`). The
measured amplitudes are in `results.md#lensing-reconstruction`.

## How it is done
<!-- key: how-it-is-done -->

Notation follows Qu et al. 2023 (ACT DR6, arXiv:2304.05202): `L, M` for
lensing multipoles, `ℓ, m` for CMB multipoles, an overbar for unnormalised
quantities, `R_L` for the response, so that φ̂_LM = R_L⁻¹ φ̄_LM [src:
Sect. V.8.1]. SPT-3G D1 (Omori et al. 2026, arXiv:2608.31136) writes the
same objects with weights `W^α_{ℓ1ℓ2L}` and a tilde for simulation-based
responses [src: Sect. IV.1]. Symbols used throughout: `X, Y ∈ {T, E, B}`
are CMB fields; `(3j)` is the Wigner 3j symbol of (ℓ1 ℓ2 L; m1 m2 −M);
`C^tot_ℓ` is the total (CMB + noise + foreground) spectrum of a filtered
map; `QE(X, Y)` is the estimator applied to maps X and Y; "MV" is the
sum of the pair estimators of Step 2; "PP" is the polarisation-only
estimator.

### Step 1. Filter the CMB maps
<!-- key: step-1-filter-the-cmb-maps -->

- Lensing makes the CMB statistically anisotropic for a fixed φ. ACT
  writes the induced covariance as
  ⟨X_ℓ1m1 Y_ℓ2m2⟩_CMB = Σ_LM (−1)^M (3j) f^XY_ℓ1ℓ2L φ_LM
  (arXiv:2304.05202, Eq. 18), with response functions linear in the CMB
  spectra; lensed spectra are used in them to cancel a higher-order
  correction [src: Sect. V.8.1].
- Two filtered versions of the data enter: Wiener-filtered maps X^WF and
  inverse-variance-filtered maps X̄ [src: arXiv:2304.05202, Sect. V.8.1].
- Planck PR4 (Carron et al. 2022, arXiv:2206.07773) computes the Wiener
  filter jointly for T, E, B,
  X^WF = C^fid 𝒯† [𝒯 C^fid 𝒯† + N]⁻¹ X^dat (Eq. 1). Here 𝒯 maps lensed
  T, E, B harmonic modes onto the observed Stokes maps (5′ beam and HEALPix
  pixel window included), C^fid is the matrix of fiducial lensed spectra
  including C^TE (Eq. 2), N is the pixel noise matrix, taken diagonal,
  and X^dat the observed T, Q, U maps, and conjugate-gradient inversion with
  a convergence criterion weighted to sub-degree scales that makes the
  filtering almost twice as fast [src: Sect. II.3].
- Poorly understood modes are removed by giving them infinite noise in N
  ("deprojection"); PR4 always deprojects the temperature monopole and
  dipole and found consistent results when deprojecting the Commander
  foreground model [src: arXiv:2206.07773, Sect. II.3].
- PR4 filters 2 ≤ ℓ ≤ 2048 but uses only 100 ≤ ℓ ≤ 2048 in the estimator
  [src: Sect. II.3]. The ACT DR6 baseline CMB range is 600 < ℓ < 3000, with
  variations down to 2000 or up from 1500 used as null tests [src:
  arXiv:2304.05202, Fig. 19 caption].

### Step 2. Form the quadratic estimator
<!-- key: step-2-form-the-quadratic-estimator -->

- ACT and Planck build an unnormalised spin-1 displacement in real space,
  ₁d̂(n) = −Σ_{s=0,±2} ₋ₛX̄(n)[ð_s X^WF](n) (arXiv:2304.05202, Eq. 19), with
  ð the spin-raising operator and ₛX the spin-s field (Eq. 20). A spin-±1
  transform splits it into a gradient φ̄_LM and a curl Ω̄_LM (Eq. 21) [src:
  Sect. V.8.1].
- SPT writes the harmonic form
  φ̄^α_LM = ((−1)^M/2) Σ (3j) W^{α,φ}_{ℓ1ℓ2L} X̄_ℓ1m1 Ȳ_ℓ2m2
  (arXiv:2608.31136, Eq. 9), with weights built from lensed-gradient
  spectra, evaluated as a map-space product thanks to separability [src:
  Sect. IV.1].
- The temperature-only (s = 0) and polarisation-only (s = ±2) parts are
  summed at field level, not at power-spectrum level. Because of the Wiener
  filter, the s = 0 term already contains part of the TE estimator; for a
  temperature-only estimator the input E must be set to zero [src:
  arXiv:2304.05202, Sect. V.8.1, footnotes 27–28].
- Lensed fiducial spectra in filter and normalisation reduce the N⁽²⁾ bias
  (second order in C^φφ) to sub-percent levels; for TT, ACT uses the
  lensed temperature-gradient spectrum C^{T∇T}, stated reason "to further
  improve the fidelity of the reconstruction" [src: arXiv:2304.05202,
  Sect. V.8.1].

### Step 3. Subtract the mean field
<!-- key: step-3-subtract-the-mean-field -->

- The mean field is the estimator's response to masking and noise
  inhomogeneity. ACT averages 180 noiseless simulations with independent
  CMB and lensing realisations and subtracts it, φ̄ → φ̄ − ⟨φ̄⟩ (Eq. 22);
  noise is left out because the cross-split estimator (Step 6) cancels the
  noise mean field [src: arXiv:2304.05202, Sect. V.8.1, footnote 26].
- PR4 forms two lensing maps whose mean fields come from two
  non-overlapping sets of simulations, and takes their cross-spectrum, so
  that Monte Carlo noise in the mean field does not enter the raw spectrum
  (arXiv:2206.07773, Eqs. 4–5) [src: Sect. II.4]. The number of simulations
  is not given in the section read.

### Step 4. Normalise
<!-- key: step-4-normalise -->

- Analytic normalisation: for the MV combination,
  (R_L^MV)⁻¹ = 1 / Σ_XY R_L^XY (arXiv:2304.05202, Eq. 24), from curved-sky
  expressions [src: Sect. V.8.1].
- Neither masking nor Fourier-space filtering is captured analytically.
  ACT multiplies by ΔA_L^MC,mul = ⟨C_L^φφ⟩ / ⟨C_L^φ̂φ⟩ (Eq. 25), computed
  after binning; Appendix D traces it mainly to the Fourier-space filter
  [src: Sect. V.8.1].
- SPT replaces the analytic response by a simulation response,
  R̃_L^αφ = ⟨C_L(φ^in, φ̄^α) / C_L(φ^in, φ^in)⟩ (arXiv:2608.31136, Eq. 12).
  The correction is about 20% for MV and GMV, dominated by mode loss from
  filtering [src: Sect. IV.1].
- PR4 adds a κ-filtering step for Planck's inhomogeneous noise: the sky is
  cut into 64 patches by noise level, and each patch gets an effective
  reconstruction noise N^κ_0,eff and response R^κ_eff, and the QE
  convergence map ĝ^κ is Wiener filtered,
  κ̂^WF = C^κκ_fid [C^κκ_fid + N^κ_0,eff]⁻¹ (R^κ_eff)⁻¹ ĝ^κ
  (arXiv:2206.07773, Eq. 3). The spectrum is rescaled by a scale-dependent
  sky fraction f_A,L = Σ_p f_p (w_L^p)² (Eq. 6), with f_p the area of patch
  p and w_L^p = [C^κκ_L,fid / (C^κκ_L,fid + N^κ,p_0,eff)] R^κ,p_L / R^κ,p_eff
  (Eq. 7). Errors in this patch model are
  absorbed by the multiplicative Monte Carlo correction, because all terms
  scale with 1/f_A,L [src: Sect. II.4]. The paper states the gain is
  limited because isotropic CMB fluctuations, not instrument noise,
  dominate the reconstruction noise [src: Fig. 2 caption].

### Step 5. Estimate the power spectrum and subtract the biases
<!-- key: step-5-estimate-the-power-spectrum-and-subtract -->

- Raw spectrum: Ĉ_L = [w₄(2L+1)]⁻¹ Σ_M φ̂^AB_LM (φ̂^CD_LM)*, where
  w₄ = ∫ d²n M⁴(n)/4π (arXiv:2304.05202, Eq. 26) [src: Sect. V.8.1].
- Realisation-dependent N⁰ (RDN0). ACT's Eq. E1 combines four data ×
  simulation pairings minus two pure-simulation pairings (S, S′). It
  corrects to first order for a mismatch between data and simulation
  two-point functions, and reduces the correlations between lensing band
  powers and with the primary CMB spectra [src: App. E.1]. Here S and S′
  label two independent sets of simulations and C̄^× is the cross-split
  spectrum of Step 6. The pure-simulation part alone is MCN0, the
  Monte Carlo N⁰. SPT's form is
  Eq. 28 of arXiv:2608.31136 [src: Sect. IV.7].
- Number of simulations: ACT uses 480 noiseless pairs; going from 240 to
  480 moved A_lens by 5 × 10⁻⁶ [src: arXiv:2304.05202, App. E.1]. Stated
  reason for noiseless simulations: the cross-split estimator removes the
  noise contribution, and the absence of noise speeds convergence [src:
  App. E.1].
- RDN0 for every covariance simulation would cost N_sim × N_sim
  reconstructions. Both ACT and SPT use a semi-analytic N⁰ for the
  simulations instead,
  N_L^(0),SA = R̃_L⁻² (2L+1)⁻¹ Σ |W|² C^tot_ℓ1 C^tot_ℓ2 (arXiv:2608.31136,
  Eq. 29) [src: Sect. IV.7; arXiv:2304.05202, App. E.1].
- N¹ from simulation pairs that share the lensing map. ACT uses 90 pairs
  (Eq. E2) [src: App. E.2]. SPT uses a second CMB set lensed by the same φ
  (cmb2phi1), Eq. 27 [src: arXiv:2608.31136, Sect. IV.7].
- Additive Monte Carlo term ΔC_L^MC from 480 simulations (Eq. E3 of
  arXiv:2304.05202). It is small, so it is treated as additive [src:
  App. E.3]. The term is the fiducial C^φφ minus the mean of 480
  simulated cross-only spectra after the multiplicative correction, MCN0
  and N¹ are removed.
- SPT subtracts one more term, N_L^MFcorr, measured from input-subtracted
  maps κ̂^res = κ̂ − κ^in, as N^MFcorr = ⟨C_L(κ̂^res, κ̂^res)⟩ − N⁰ − N¹
  (arXiv:2608.31136, Eq. 30). It is 4–7% at L = 2000 across
  estimators, and appears only in lensed simulations [src: Sect. IV.7,
  App. A].
- Higher orders. ACT and PR4 neglect N^(3/2), from the LSS bispectrum and
  post-Born lensing, at their sensitivity [src: arXiv:2304.05202, App. E.2;
  arXiv:2206.07773, Sect. II.4]. Böhm et al. 2016 (arXiv:1605.01392)
  estimate, from two of the largest terms only, a negative bias of order 1%
  of the signal for temperature reconstruction in Stage III and IV
  experiments, which they translate into several standard deviations [src].
- SPT bins 30 ≤ L ≤ 3000 into 17 bands (3 logarithmic between 30 and 100,
  14 between 100 and 3000) with weights w_L^b = 1/σ²(Ĉ_L^κκ) [src:
  arXiv:2608.31136, Sect. IV.7, Eq. 31].

### Step 6. Make the spectrum immune to noise modelling (optional)
<!-- key: step-6-make-the-spectrum-immune-to-noise -->

- Stated reason: the standard QE spectrum stays sensitive to the noise
  simulations even with RDN0, and ACT's atmospheric and instrumental noise
  is hard to simulate [src: arXiv:2304.05202, Sect. V.8.3].
- ACT reconstructs from pairs of data splits i, j with independent noise,
  φ̂^(ij) = ½[QE(X^i, Y^j) + QE(X^j, Y^i)] (arXiv:2304.05202, Eq. 30). The
  spectrum keeps only terms in which all four splits differ,
  C^× = (1/4!) Σ_{i≠j≠k≠l} Ĉ(φ̂^(ij), φ̂^(kl)) (Eq. 33), and is evaluated
  quickly through the auxiliary estimators of Eqs. 34–37 [src:
  Sect. V.8.3].
- The baseline map uses φ̂ = (1/6) Σ_{i<j} φ̂^(ij) (Eq. 38) [src].
- The estimator comes from Madhavacheril et al. 2020 (arXiv:2011.02475).
  It needs at least four splits with independent noise, makes the spectrum
  insensitive to the noise model, loses "no substantial" signal-to-noise
  "in many practical situations", and scales as O(m²) in the number of
  splits rather than O(m⁴) [src].

### Step 7. Validate before unblinding
<!-- key: step-7-validate-before-unblinding -->

ACT (arXiv:2304.05202):

- Every null test is χ² = d_nullᵀ ℂ⁻¹ d_null (Eq. 41), with ℂ from 792
  simulations run through the same analysis, so correlations between the
  differenced data sets are kept. There are 10 degrees of freedom in the
  baseline range and 13 in the extended range [src: Sect. VI.2].
- The PTE distributions are uniform by a Kolmogorov–Smirnov test (10% in
  the baseline range, 74% in the extended range) [src: Sect. VI.6].
- The tests are grouped by category (noise, scales, frequency,
  foregrounds, isotropy, instrument). The sum and the worst χ² in each
  group are compared with their simulated distributions at 2σ. Only the
  worst-χ² statistics of the noise-only and instrument groups slightly
  exceed it; the paper argues why these are not concerning [src:
  Sect. VI.6].

SPT-3G D1 (arXiv:2608.31136):

- Simulation mean: over 498 realisations, the mean of the TT, PP and GMV
  spectra must lie within 0.3σ of the input in every bin. Most bins agree
  to better than 0.1σ, a few reach about 0.15σ. The criterion is set at
  band-power level because a parameter-level threshold would depend on
  model and priors [src: Sect. V.1].
- Unlensed simulations: 50 realisations with no deflection, debiased by N⁰
  only, must give a mean spectrum with PTE > 0.05 against zero. The
  results are 0.06 (TT), 0.22 (PP), 0.16 (GMV) [src: Sect. V.2].
- Curl: a non-zero curl spectrum appears in data and simulations alike.
  It is attributed to map-making and filtering, and the simulation mean is
  subtracted. The residual curl gives PTE 0.88, 0.61, 0.20 for TT, PP, GMV
  [src: Sect. V.3.1].
- Against MUSE, on 100 matched simulations: band-power differences give
  χ² = 19.8 for 15 degrees of freedom (PTE 0.18). At parameter level,
  A_recon has PTE 0.89 (PP) and 0.97 (GMV), and σ₈Ω_m^0.25 has PTE 0.43
  and 0.45 [src: Sect. VI.3.3, Eqs. 46–47].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Combining T, E and B: HO02, SQE or GMV
<!-- key: combining-t-e-and-b-ho02-sqe-or-gmv -->

Maniyar et al. 2021 (arXiv:2101.12193) compare four quadratic estimators
on the same noise models:

| Estimator | Construction | Noise relative to the others | Used by |
|---|---|---|---|
| HO02 (Hu & Okamoto) | optimal single-pair weights (Eqs. 11–12), then optimal linear combination w_α = Σ_β(N⁻¹)_αβ / Σ_βγ(N⁻¹)_βγ (Eq. 33) | not the global minimum [src: Sect. VII] | — |
| OH03 (Okamoto & Hu) | separable, slightly suboptimal TE | below HO02 by about 0.08% at small scales for CMB-S4-like, above it by < 0.5% at large scales [src: Sect. VI.2] | — |
| SQE | C^TE set to 0 in the inverse filter; one λ_SQE(L) for all pairs (Eqs. 60–61), λ_SQE(L) being the common normalisation | noisier than HO02 by about 1–8% and than GMV by about 9–12% for sensitive experiments [src: Sect. VII] | Planck 2018 and earlier SPT [src: Sect. V]; ACT DR6 [src: arXiv:2304.05202, footnote 29] |
| GMV | joint inverse filtering of T, E, B with C^TE kept, all pairs at once (stated reason for the SPT baseline: the sum of pair estimators "does not yield the lensing estimator with the lowest possible variance" [src: arXiv:2608.31136, Sect. IV.2]) | lowest; vs SQE about 3% (L ≲ 500) to 6% (L ~ 2000) for Planck-like, about 11–12% for SO- and S4-like [src: Sect. VI.2] | Planck PR4 [src: arXiv:2206.07773, Eq. 1]; SPT-3G D1 baseline [src: arXiv:2608.31136, Sect. IV.2] |

- The GMV is the weak-signal first step of likelihood-based estimators
  [src: arXiv:2101.12193, Sect. VII].
- For CMB-S4-like noise, the GMV gain over HO02 comes from the TT–TE–EE
  block rather than from better EB filtering, and is largest at L ≲ 200
  [src: Sect. VI.2].
- Cost: SQE keeps configuration-space separability and is cheaper on a cut
  sky [src: Sect. V].
- The SPT GMV filter is
  C_ℓ⁻¹ = [[C^EE/D, −C^TE/D, 0], [−C^TE/D, C^TT/D, 0], [0, 0, 1/C^BB]] with
  D_ℓ = C^TT C^EE − (C^TE)² (arXiv:2608.31136, Eq. 15). Here C_ℓ includes
  signal, noise and foreground residuals [src: Sect. IV.2].

### Foreground mitigation in the temperature leg
<!-- key: foreground-mitigation-in-the-temperature-leg -->

| Variant | How it works | Cost and caveat | Who |
|---|---|---|---|
| Profile (bias) hardening | reconstructs a source field with a chosen profile and removes the estimator's linear response to it (arXiv:2304.05202, Eqs. 27–28; arXiv:2608.31136, Eqs. 17–22) | a tSZ-profile hardening also cuts point-source bias by about a factor 5 [src: arXiv:2304.05202, Sect. V.8.2]; in the GMV it acts only on T̄ in the TT weight, not on T entering Ē through C^TE [src: arXiv:2608.31136, Sect. IV.4] | ACT DR6 baseline (reason stated: robustness to extragalactic foregrounds, Sect. V.8); SPT-3G D1 check, profile (C_ℓ^tSZ)^γ from Agora (γ a chosen exponent, normalisation arbitrary), chosen because stacking on clusters and sources gave a cleaner map [src: Sect. IV.4] |
| tSZ deprojection in one leg ("tSZdpj") | tSZ-nulled map in one leg, minimum-variance map in the other | avoids the noise of deprojecting both legs [src: arXiv:2608.31136, Sect. IV.3] | SPT-3G D1 check |
| Cross-ILC ("xILC") | tSZ-deprojected map in one leg, CIB-deprojected in the other | suppresses both tSZ and CIB [src: Sect. IV.3] | SPT-3G D1 check |
| Polarisation only | no temperature | larger noise | SPT MUSE (arXiv:2411.06000) |
| Point-source trispectrum correction | measure the shot-noise trispectrum S₄ with a source estimator, subtract its template, add a rank-one covariance term | PR4: 10¹³ Ŝ₄ = 3.0 ± 0.8 μK⁴, about 30% above PR3; correction up to a quarter of a band-power error in the last conservative bins; covariance change at most 0.3% [src: arXiv:2206.07773, Sect. II.6, Eqs. 11–13] | Planck PR4 |

- Sailer et al. 2020 (arXiv:2007.04325) find in simulations that all
  extragalactic temperature foregrounds can be approximated by sources
  with identical profiles. For an SO-like experiment, hardening allows a
  higher ℓ_max and about 50% more statistical power than the standard QE
  (**forecast**) [src].
- SPT stacks lensing maps on clusters, infrared sources and radio sources
  just below the masking threshold to compare the residuals of each
  variant. The baseline GMV shows an oscillatory ring around clusters,
  induced by cluster temperature signal and filtering [src:
  arXiv:2608.31136, Sect. IV.5, Fig. 4 caption].

### Noise bias: simulations or cross-splits
<!-- key: noise-bias-simulations-or-cross-splits -->

- RDN0 with noise simulations, as in Planck PR4 and SPT [src:
  arXiv:2206.07773, Sect. II.4; arXiv:2608.31136, Sect. IV.7], relies on
  the noise simulations for the bias.
- The ACT cross-split estimator needs no noise simulation for the mean
  field or N⁰. Noise simulations remain necessary for the covariance [src:
  arXiv:2304.05202, Sect. V.8.3; L2]. It requires at least four
  independent-noise splits [src: arXiv:2011.02475].
- ACT gives as the motivation the sensitivity of the standard QE to noise
  modelling, which persists despite RDN0 [src: arXiv:2304.05202,
  Sect. V.8.3, App. F].

### Quadratic estimator or MUSE
<!-- key: quadratic-estimator-or-muse -->

- MUSE (Ge et al. 2024, arXiv:2411.06000) marginalises the unlensed CMB f
  and φ in the joint posterior 𝒫(f, φ, θ | d) (Eqs. 1–2). The marginal mean
  solves s^MAP(θ, d) = ⟨s^MAP(θ, d′)⟩ over simulations (Eq. 4), and the
  covariance is Σ⁻¹ = H†J⁻¹H + Σ_prior⁻¹ (Eqs. 7–9) [src: Sect. III.1].
  Here θ holds about a hundred band-power and systematics parameters,
  s^MAP_i is the gradient of the joint log posterior with respect to θ_i at
  the maximum a posteriori (f, φ), J is the covariance of s^MAP over
  simulations and H its derivative with respect to θ [src: Eqs. 5–9].
- The result is asymptotically unbiased for any latent space. The loss of
  optimality is bounded below 10% of the statistical error for a
  comparable lensing analysis [src: Sect. III.1, citing Millea & Seljak].
- Unlike a QE, MUSE uses moments of all orders (EE, EB, BB, EEE, …) [src].
- Assumption: the simulation model must represent the data accurately
  [src].
- Same-data comparison with the QE: consistent at band-power and parameter
  level on SPT-3G D1 polarisation (Step 7) [src: arXiv:2608.31136,
  Sect. VI.3.3].
- Planck's 2018 iterative MAP alternative and its forecast gain are in L2
  (`physics-and-methods.md#quadratic-estimators`).

### Polarisation or temperature dominance
<!-- key: polarisation-or-temperature-dominance -->

- Hu & Okamoto 2002 (arXiv:astro-ph/0111606) find that polarisation starts
  to help at about 40 μK-arcmin with a 7′ beam, that it surpasses
  temperature at about 26 μK-arcmin and 4′, and that EB can give a
  high-signal-to-noise mass map to L ~ 1000 [src].
- SPT-3G D1 is polarisation-dominated at L ≲ 600 (L2). For ACT DR6 the
  temperature-only foreground bias is larger than the MV one (L2,
  `systematics.md#act-dr6-lensing-qu-et-al-2023-arxiv-2304-05202`), so the
  weight of temperature in the estimator sets how much the foreground
  treatment matters.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Mean-field simulations | 180 noiseless | ACT DR6 | arXiv:2304.05202 | Sect. V.8.1 |
| RDN0 simulation pairs | 480 (240 sufficient; ΔA_lens = 5 × 10⁻⁶) | ACT DR6 | arXiv:2304.05202 | App. E.1 |
| N¹ simulation pairs | 90 + 90 | ACT DR6 | arXiv:2304.05202 | App. E.2 |
| Covariance and null-test simulations | 792 | ACT DR6 | arXiv:2304.05202 | Sect. VI.2 |
| Null-test degrees of freedom | 10 (baseline), 13 (extended) | ACT DR6 | arXiv:2304.05202 | Sect. VI.2 |
| KS test on all null PTEs | 10% (baseline), 74% (extended) | ACT DR6 | arXiv:2304.05202 | Sect. VI.6 |
| Data splits | 4 in the cross estimator (Eqs. 31–38) | ACT DR6 | arXiv:2304.05202 | Sect. V.8.3 |
| Simulation response correction | about 20% (MV, GMV), from filtering | SPT-3G D1 | arXiv:2608.31136 | Sect. IV.1 |
| N^MFcorr at L = 2000 | 4–7% | SPT-3G D1 | arXiv:2608.31136 | Sect. IV.7 |
| Band powers | 17 bins, 30 ≤ L ≤ 3000 | SPT-3G D1 | arXiv:2608.31136 | Sect. IV.7 |
| Simulation-mean criterion | < 0.3σ per bin, 498 realisations | SPT-3G D1 | arXiv:2608.31136 | Sect. V.1 |
| Unlensed-simulation PTE | 0.06, 0.22, 0.16 (TT, PP, GMV); requirement > 0.05 | SPT-3G D1 | arXiv:2608.31136 | Sect. V.2 |
| Curl PTE after simulation-mean subtraction | 0.88, 0.61, 0.20 | SPT-3G D1 | arXiv:2608.31136 | Sect. V.3.1 |
| QE vs MUSE band powers | χ² = 19.8 / 15, PTE 0.18 | SPT-3G D1 | arXiv:2608.31136 | Sect. VI.3.3 |
| CMB multipoles used | 100 ≤ ℓ ≤ 2048 (filtered from 2) | Planck PR4 | arXiv:2206.07773 | Sect. II.3 |
| κ-filter patches | 64; noise averaged over 8 ≤ L ≤ 100 | Planck PR4 | arXiv:2206.07773 | Sect. II.4 |
| Shot-noise trispectrum amplitude S₄ | 10¹³ Ŝ₄ = 3.0 ± 0.8 μK⁴ | Planck PR4 | arXiv:2206.07773 | Sect. II.6, Eq. 11 |
| PR4 amplitude, conservative range 8 ≤ L ≤ 400 | A = 1.00 ± 0.024, χ² = 8.5 / 9 (2018: 1.01 ± 0.026); L2 quotes 1.004 ± 0.024 from the abstract; Eq. 18 rounds to two decimals | Planck PR4 | arXiv:2206.07773 | Sect. III.1, Eq. 18 |
| GMV vs SQE noise | 3% (L ≲ 500) to 6% (L ~ 2000), Planck-like; 11–12%, SO/S4-like (**forecast**) | — | arXiv:2101.12193 | Sect. VI.2 |
| N^(3/2) estimate | about −1% of the signal, temperature, Stage III/IV (**forecast**) | — | arXiv:1605.01392 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Noise mis-modelling biases N⁰.** It shows up as failures in noise-only
  split-difference tests. The cure is the cross-split estimator, or RDN0
  with tested noise simulations [src: arXiv:2304.05202, Sect. V.8.3,
  App. F].
- **Array-frequency map nulls fail while the lensing spectrum is fine.**
  These nulls lack signal variance, so their errors are much smaller, and
  they carry no N⁰ subtraction: a failure can reflect differing CMB spectra
  between the maps rather than a lensing error [src: arXiv:2304.05202,
  Sect. VI.6]. Test: band-power-level array differences, which include
  signal covariance and are more sensitive to multiplicative biases [src].
- **Mask and filter break the analytic normalisation.** Visible as a
  multiplicative offset in simulation input–output cross-spectra. The
  correction is about 20% for SPT-3G D1 [src: arXiv:2608.31136, Sect. IV.1]
  and is computed after binning in ACT [src: arXiv:2304.05202,
  Sect. V.8.1]. Test: simulation-mean recovery within 0.3σ per bin [src:
  arXiv:2608.31136, Sect. V.1].
- **Non-zero curl.** SPT-3G D1 sees curl power in data and simulations
  alike and subtracts the simulation mean. Stated reason: the data and
  simulation curl spectra agree and the gradient simulation-mean test
  passes, so the curl is read as a known offset of map-making and
  filtering [src: Sect. V.3.1]. A curl excess in data relative
  to simulations would point to an unmodelled systematic [src:
  arXiv:2608.31136, Sect. V.3.1]. Planck 2018 restricted its likelihood
  range because of a curl-test issue at high L (L2).
- **Mean-field Monte Carlo noise.** Use independent simulation subsets for
  the mean fields of the two legs [src: arXiv:2206.07773, Sect. II.4].
- **A bias correlated with the mean field at high L.** SPT-3G D1 needed an
  extra 4–7% term at L = 2000 [src: arXiv:2608.31136, Sect. IV.7, App. A].
  Test: the power spectrum of input-subtracted reconstructions in lensed
  simulations.
- **Foreground residuals around clusters.** Stack the lensing map on
  clusters and sources below the masking threshold, for each estimator
  variant [src: arXiv:2608.31136, Sect. IV.5]. Compare variants with
  different foreground immunity at band-power level (L2).
- **Un-subtracted point-source trispectrum.** Planck PR4 detects it at
  3–4σ with the S₂ estimator [src: arXiv:2206.07773, Sect. II.6].
- **Non-Gaussian lenses ignored.** The N^(3/2) bias, of order −1% for
  temperature-based reconstruction at Stage III/IV depth, is estimated from
  two terms only [src: arXiv:1605.01392]. ACT and PR4 call it negligible at
  their sensitivity [src: arXiv:2304.05202, App. E.2; arXiv:2206.07773,
  Sect. II.4].
- **Data-processing changes move individual band powers.** Running the
  2018 pipeline on NPIPE maps instead of 2018 maps shifts some peak bins by
  amounts comparable to their errors. In a crude paired-noise model the
  lowest peak bin is 3.1σ low (MV) [src: arXiv:2206.07773, Sect. III.1].

## Reading list
<!-- key: reading-list -->

- Foundation: Hu & Okamoto 2002, arXiv:astro-ph/0111606: the
  minimum-variance quadratic estimators and when polarisation takes over.
- Method: Maniyar et al. 2021, arXiv:2101.12193: HO02, OH03, SQE and GMV
  compared, with explicit weights and noise.
- Method: Madhavacheril et al. 2020, arXiv:2011.02475: the cross-split
  estimator, immune to noise modelling.
- Method: Sailer et al. 2020, arXiv:2007.04325: foreground hardening and
  its noise cost (forecast).
- Application: Qu et al. 2023, arXiv:2304.05202: the full ACT DR6 pipeline,
  bias formulae (App. E) and null-test statistics.
- Application: Carron et al. 2022, arXiv:2206.07773: GMV Wiener filtering,
  κ-filtering and the point-source correction on Planck PR4.
- Application: Omori et al. 2026, arXiv:2608.31136: SPT-3G D1 GMV and
  hardening variants, validation thresholds, comparison with MUSE.
- Method: Ge et al. 2024, arXiv:2411.06000: MUSE as run on data.
- Critique: Böhm et al. 2016, arXiv:1605.01392: the bias from the LSS
  bispectrum that quadratic pipelines neglect.

## Not verified
<!-- key: not-verified -->

- The Hu & Okamoto 2002 estimator equations: abstract only. The weights
  quoted here are read in Maniyar et al. 2021.
- The details of Madhavacheril et al. 2020, Sailer et al. 2020 and Böhm et
  al. 2016: abstracts only, read through INSPIRE.
- The SPT-3G D1 C⁻¹ filter and linear-combination maps (Sects. II.4–II.6
  of arXiv:2608.31136): not read.
- The ACT App. D explanation of the multiplicative correction and App. F
  noise tests: cited by the main text, not read.
- The Planck 2018 lensing body (arXiv:1807.06210): not re-read this
  session; statements about it come from L2.
