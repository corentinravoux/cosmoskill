# CMB lensing by clusters — cosmo-clusters dossier

Scope: how a cluster mass is measured from the lensing of the CMB (the
estimator, the handling of the cluster's own tSZ, kSZ and dust signals,
the mean field, the profile model that turns a stacked signal into a mean
mass, and the way the result enters a count likelihood), and how to
choose between the quadratic, maximum-likelihood, rotated-stack and
matched-filter forms.
Snapshot: 2026-10-18.
From: Miyatake 2025 review (arXiv:2505.07697), Sect. 4.2; SPT and ACT
CMB-cluster-lensing papers (arXiv:2111.07491, arXiv:2009.07772).

Already in L2, not repeated here: the precision reached by each
measurement and the (1 − b) values in
`physics-and-methods.md#mass-calibration` and
`results.md#planck-sz-clusters-and-the-mass-bias-question`; the CMB-S4
forecast of a 2.5–4.5σ Σm_ν detection with CMB-cluster-lensing
calibration in `open-questions.md#forecasts`; the SPT-3G CMB-lensing
sample sizes in `surveys-and-data.md#lensing-data-sets-used-for-mass-calibration`.
CMB lensing reconstruction over the whole sky (as opposed to around
clusters) is in `cosmo-cmb`; galaxy–CMB-lensing cross-correlations are in
`cosmo-cmb-lss-cross-correlations`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. The signal and its size
<!-- key: step-1-the-signal-and-its-size -->

The lensed CMB is a remapping of the unlensed field, X(n̂) = X̃[n̂ +
α(n̂)], with α the deflection angle; on the arcminute scales of a cluster
the unlensed CMB is smooth because of Silk damping, so to first order
X ≈ X̃ + α · ∇X̃ [src: Sect. 2, Eqs. 1 and 5, arXiv:2305.06326]. The
deflection obeys ∇ · α = −2κ, where the convergence κ = Σ/Σ_cr is the
surface mass density Σ divided by the critical density [src: Eqs. 3–4,
same]. For CMB lensing Σ_cr = (c²/4πG) D_s/(D_l D_ls), with D_s, D_l and
D_ls the angular-diameter distances to the last-scattering surface, to the
cluster, and between them [src: Appendix B, Eq. B2, arXiv:2009.07772].

The cluster reverses the background gradient locally and imprints a dipole
aligned with it. Seljak & Zaldarriaga 2000 (arXiv:astro-ph/9907254) first
described these "step-like wiggles" parallel to the large-scale gradient,
of typical amplitude 10 μK (σ_v / 1400 km/s)², with σ_v the velocity
dispersion, and noted that the effect follows the deflection angle rather
than its derivative, so it weights the outer cluster more than shear does
[src: abstract]. The rms temperature gradient is about 10 μK/arcmin and a
cluster deflects by about 1 arcmin, so the temperature dipole is about
10 μK; the polarisation gradient is about 1 μK/arcmin, so the polarisation
dipole is about 1 μK and needs noise ten times lower to be detected [src:
Sect. 2, arXiv:2305.06326]. The dipole is proportional to the local
gradient, which is why every estimator weights clusters by the gradient
they sit on.

The advantage stated by the papers is reach in redshift: the source is
the last-scattering surface, so the method keeps its sensitivity for
distant clusters, "where galaxy lensing calibration is ineffective due to
the lack of enough resolved background galaxies" [src: abstract,
arXiv:1710.10236]; the ACT measurement targets clusters at mean z = 1.08
(arXiv:2009.07772).

### Step 2. Prepare the maps
<!-- key: step-2-prepare-the-maps -->

Cutouts are taken around each cluster and around random points. Sizes in
use: 60′ × 60′ for the gradient estimate and 10′ × 10′ for the stacked
dipole in SPT-3G [src: Sect. 3.1, arXiv:2404.02153]; 128′ × 128′ with
0.5′ pixels for the ACT quadratic estimator [src: Appendix A,
arXiv:2009.07772]; 256 × 256 pixels (128′ × 128′) for Planck, cut from
larger fields used only to estimate local power spectra, so that
neighbouring clusters and correlated structure contaminate the central
reconstruction less [src: Sect. 4.2, arXiv:1904.07887].

The cluster's own thermal SZ signal is larger than the lensing signal,
"in many cases ... by about an order of magnitude", and must be removed or
made harmless; the kinetic SZ has the CMB spectrum and cannot be removed
by frequency combination [src: Sect. 4.1.2, arXiv:1904.07887]. The five
treatments in use are compared under "Choices" below. The Planck version
is a constrained internal linear combination of the six frequency fields,
with weights w chosen so that wᵀa = 1 (unit response to the CMB, spectrum
a) and wᵀb = 0 (zero response to the tSZ, spectrum b), minimising the
output variance given the inter-frequency covariance R of the residuals
[src: Eqs. 3–4, same].

### Step 3. Estimate the lensing signal
<!-- key: step-3-estimate-the-lensing-signal -->

Four estimator families are in use; notation follows each paper.

**Quadratic estimator with a band-limited gradient (Planck, ACT,
SPTpol).** Planck writes the TT estimator as κ̂(L) = −N(L) (2/L²) ∫
d²x/(2π) e^{−iL·x} ∇ · [F₁(x) ∇F₂(x)], where F₁ is the inverse-variance-
filtered map (filter 1/C_l^{T̂T̂}) and F₂ the Wiener-filtered map
(C_l^{T̃T̃}/C_l^{T̂T̂} for l ≤ l_f, zero above), N(L) the normalisation,
C^{T̃T̃} the lensed CMB spectrum and C^{T̂T̂} the total spectrum of the
field [src: Sect. 4.2, Eqs. 5–9, arXiv:1904.07887]. The cut l_f = 2000
keeps the estimator unbiased near clusters, "where second and higher
orders of κ become important"; the lensed spectrum is used because it
gives approximately the correct response averaged over other lensing
modes [src: same]. ACT uses the same structure, the divergence of the
product of a low-pass gradient map (ℓ_G = 2000, "to mitigate bias in
massive clusters as well as to reduce contamination from foregrounds")
and a high-resolution map (ℓ ≤ 6000), drops ℓ < 200 because of the cutout
size, and keeps 200 < L < 5000 in the output, a filter then propagated
into the model [src: Appendix A, Eq. A1, arXiv:2009.07772]. The
reconstruction noise of the Planck estimator is N_κ(L) = C_L^κκ + N⁽⁰⁾(L)
+ N⁽¹⁾(L): uncorrelated large-scale structure, Gaussian CMB and noise
fluctuations, and the N⁽¹⁾ term [src: Eq. 13, arXiv:1904.07887].

**Minimum-variance quadratic estimator on a joint ground + space map.**
Huchet & Melin build one ILC map per cluster from three SPT-SZ and six
Planck frequency maps, with the anisotropic SPT transfer function inside
the response vectors, apply the flat-sky Hu–Okamoto estimator (Eqs.
11–14) and match-filter the potential with an NFW template [src: Sects.
3.1 and 3.5, arXiv:2402.18346]. Additive spurious signal is removed by
running the pipeline on ten random sets of 468 positions and subtracting
their mean ("on − ⟨off⟩₁₀"), which inflates the error by √(1 + 1/10)
[src: Sect. 3.1, same].

**Rotated-stack dipole estimator (SPTpol polarisation, SPT-3G
temperature).** Introduced for Q/U maps in arXiv:1907.08605 and extended
to temperature in arXiv:2305.06326 [src: abstracts]. The SPT-3G steps
[src: Sect. 3.1, arXiv:2404.02153]:
1. On a tSZ-nulled ILC map (95, 150, 220 GHz), Wiener-filter the 60′
   cutout with W_ℓ = C_ℓ/(C_ℓ + N_ℓ) for ℓ ≤ 2000 and zero above
   (Eq. 1), with N_ℓ from half-difference maps, and take the median
   gradient direction in the central 6′ × 6′.
2. Cut 10′ × 10′ stamps from the unfiltered map, rotate them along the
   gradient, weight by w = w_n w_g (inverse noise variance times gradient
   magnitude), subtract each stamp's mean, and stack.
3. Subtract the stack at random points: s = s_c − s_r (Eq. 2), with
   N_rand = 10 N_clus drawn from the survey randoms so that they avoid
   masked regions; larger random sets did not change the result.
4. Estimate the cluster tSZ (and CIB and other cluster-correlated
   emission) as the mean of 25 stacks of randomly rotated cluster stamps
   and subtract it (Eqs. 16–17 of arXiv:2305.06326).
5. Compare with model stacks built the same way from noiseless lensed
   simulations in mass bins from 0 to 4 × 10¹⁴ M_sun (step 0.1 × 10¹⁴),
   adding white noise and Gaussian foregrounds to the models only when
   estimating the gradient direction, because otherwise the better
   gradient estimate of the models "will cause a bias towards lower
   masses" [src: Sect. 3.2, same].
6. Likelihood −2 ln L = Σ (s − m) Ĉ⁻¹ (s − m)ᵀ over pixels (Eq. 3), with
   a jackknife covariance from N_jk = 0.9 N_clus subsamples (Eq. 4),
   chosen because it captures all noise sources; for sub-samples of about
   a third of the clusters the full-sample covariance is multiplied by 3
   rather than re-estimated [src: Sect. 3.3, same].

**Maximum-likelihood fit of lensed templates (SPT-SZ 2015, forecasts).**
−2 ln L(d | Σ_lens) = ln |Σ_lens| + dᵀ Σ_lens⁻¹ d, with d the pixel values
of the T or Q/U stamp and Σ_lens the pixel–pixel covariance of the lensed
CMB plus noise and foregrounds for a given mass; clusters are combined by
a weighted sum of their log-likelihoods [src: Sect. 2.1, Eqs. 4–5,
arXiv:1705.00411]. The box is 10′ × 10′; doubling its area changes the
S/N by ≤ 1% [src: same]. The first SPT detection used this approach on
513 SZ-selected clusters (3.1σ) [src: abstract, arXiv:1412.7521].

A fifth form, direct inversion of the background gradient with a matched
filter, was proposed for low-noise data: it beats the quadratic estimator
by up to about 50% for a cluster at z = 2 at 1 μK-arcmin and "approaches
the performance of maximum likelihood methods, at a fraction of the
computational cost" [src: abstract, arXiv:1710.10236].

### Step 4. Subtract the mean field
<!-- key: step-4-subtract-the-mean-field -->

Masks, tapering windows, anisotropic beams and inhomogeneous noise make
the quadratic estimator see lensing where there is none. ACT estimates
this mean field from about 300 times as many random positions as
clusters; it is roughly constant with radius and amounts to 20% of the
measurement in the first radial bin, 50% in the second, and more than the
measurement beyond [src: Appendix A, arXiv:2009.07772]. Planck estimates
local mean fields in 10 ecliptic-latitude bands (north and south bands
paired), from 16384 random fields per band inside the 60% Galactic mask,
because the Planck scan strategy makes noise and beam vary with ecliptic
latitude [src: Sect. 4.2, arXiv:1904.07887]. The random-point stack of
the rotated estimator (Step 3, point 3) plays the same role.

### Step 5. Turn the signal into a mass
<!-- key: step-5-turn-the-signal-into-a-mass -->

**Stacked profile with a halo model (ACT, SPT-3G).** ACT fits the
azimuthally averaged κ̂ profile in five bins within 8′ of the centre with
κ = κ_1h + κ_2h (Eq. B1): an NFW one-halo term in M500c with a
concentration–mass relation, and a two-halo term from the halo bias
b(m, z) times the linear matter spectrum, projected to Σ_2h and converted
with an extra (1 + z)² for comoving coordinates (Eqs. B3–B6); both are
passed through the reconstruction filter [src: Appendix B,
arXiv:2009.07772]. The population is integrated over the observed
redshift distribution, the mass function, a lognormal richness–mass
relation of scatter 0.5 and a selection Θ(λ − 20) over 0.7 < z < 1.8
(Eqs. B7–B12), with the richness normalisation β the only free
parameter; the quoted quantity is the population-weighted mean mass
(Eq. B9) because it "directly quantifies the amplitude of the lensing
signal" while β depends on the assumed selection and scatter [src: same].
The steps of the fit show what each term does: a single NFW at z = 1.1
gives ⟨M500c⟩ = (2.1 ± 0.5) × 10¹⁴ M_sun, adding the two-halo term
(1.7 ± 0.4) × 10¹⁴, the full population model (1.7 ± 0.4) × 10¹⁴ [src:
same]. The covariance is the weighted scatter of individual profiles
(Eq. 1) [src: Sect. III, same].

SPT-3G models κ_tot = κ_1h + κ_2h with miscentring applied in Fourier
space, κ̃_1h(ℓ) = κ_1h(ℓ)[(1 − f_mis) + f_mis exp(−σ_s² ℓ²/2)] (Eq. 5),
f_mis = 0.22 ± 0.11, σ_s = σ_R/D_A(z), σ_R = c_mis R_λ with R_λ = (λ/100)^0.2
h⁻¹ Mpc and ln c_mis = −1.13 ± 0.22; simulations include tSZ and kSZ
from the Agora suite, CIB and radio power, the 150 GHz beam, the measured
noise, and a 2D transfer function F = exp[−(ℓ₁/ℓ_x)⁶] exp[−(ℓ_x/ℓ₂)⁶]
with ℓ₁ = 300 and ℓ₂ = 13000 for the time-stream filtering [src:
Sect. 3.4, arXiv:2404.02153]. Detection significance is quoted as
S/N = √(2[ln L(M_fit) − ln L(M = 0)]) [src: same; Eq. 22,
arXiv:2305.06326].

**Per-cluster matched filter and a signal-to-noise observable
(Planck).** Each reconstructed κ field is filtered with an NFW template
κ_t of angular scale θ_s set by the catalogue SZ mass, giving κ̂₀ (Eq. 22)
with variance σ²_κ₀ (Eq. 23); the mass estimate M̂500 = M_fid κ̂₀/κ₀^fid
(Eq. 25) is biased at linear order by any mismatch between template and
true profile, whereas p_obs = κ̂₀/σ_κ₀ (Eq. 27) is biased only at second
order, so p_obs is the observable [src: Sects. 4.3.2–4.3.3,
arXiv:1904.07887]. In their test for a 5 × 10¹⁴ M_sun cluster at z = 0.2,
⟨p_obs⟩ varies from 0.2136 to 0.2159 for template masses from 0.1 to
1.0 × 10¹⁵ M_sun, while ⟨M̂500⟩ runs from 0.36 to 0.58 × 10¹⁵ M_sun [src:
Table 1, same]. A typical 1′ miscentring (from the 2.4′ 95% positional
uncertainty of the Planck catalogue) biases p_obs low by about 3% [src:
Sect. 4.3.3, same].

### Step 6. Enter the count likelihood
<!-- key: step-6-enter-the-count-likelihood -->

**Joint hierarchical model (Planck).** The SZ signal-to-noise q and the
lensing p are drawn from a bivariate lognormal around their mean
relations, with scatters σ_SZ and σ_CMBlens and correlation r_CMBlens−SZ
(Eq. 45); the parameters are 1 − b_SZ, 1 − b_CMBlens, the two scatters,
r, and the Y–M normalisation and slopes (Eq. 52) [src: Sects. 6.1.2 and
6.4.1, arXiv:1904.07887]. The CMB-lensing bias parameter absorbs the
residual second-order biases of the filter [src: Sect. 4.3.3, same]. The
correlation is allowed because both SZ and lensing integrate along the
line of sight, so triaxiality moves them together [src: Sect. 5, same].

**Why not a mass ratio.** The simple estimator 1/(1 − b) = ⟨M_lens/M_Yz⟩
(Eq. 33) needs unbiased lensing masses, SZ masses that are unbiased at
fixed true mass, and negligible SZ scatter. Selection on SZ
signal-to-noise makes the catalogue SZ masses scatter high near the
threshold, so the ratio estimator overestimates 1 − b, and matched-filter
mass biases propagate straight into it; this is the authors' explanation
of why the Planck 2015 CMB-lensing value, 1/(1 − b) = 0.99 ± 0.19,
differs from their 1.41 ± 0.20 [src: Sects. 5 and 8, Table 6, same].

**Mean-mass prior (SPT-SZ).** Chaubal et al. take the stacked
M200 = (5.1 ± 2.1) × 10¹⁴ M_sun of the SPT-SZ CMB-lensing measurement as a
prior on the model mean mass of the sample (Eq. 5), because the
individual signal is "too weak to justify the computational complexity" of
a per-cluster term; they convert to M500 = (3.49 ± 0.74) × 10¹⁴ M_sun with
c = 3 at z = 0.7, and estimate a 2% error from converting the mean rather
than each cluster [src: Sects. II.4 and III, arXiv:2111.07491]. The
lensing systematics are taken as uncorrelated with the other follow-up
data [src: Sect. III, same].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Treatment of the cluster's own tSZ
<!-- key: treatment-of-the-cluster-s-own-tsz -->

| Treatment | What it assumes | Cost | Used by |
|---|---|---|---|
| tSZ-free ILC of the whole map | known tSZ spectrum, accurate inter-band calibration | 90/150 GHz combination lowers S/N by "nearly a factor of three" (larger beam, more noise); a 1% relative calibration error leaves a −6.3 ± 0.7% mass bias [src: Sect. 4.6.1, arXiv:1705.00411] | SPT-SZ 2015 (via arXiv:2111.07491, Sect. II.4); Planck CILC (arXiv:1904.07887); Planck + SPT ILC (arXiv:2402.18346) |
| tSZ-free map for the gradient leg only | contamination must appear in both legs to bias the quadratic estimator | small-scale leg keeps full sensitivity; tSZ still adds variance there | SPTpol temperature (arXiv:1810.10998, abstract); ACT, which also subtracts best-fit tSZ of about 4000 detected clusters from the high-resolution leg, cutting the errors of the first three bins by ≈ 10% [src: Appendix A, arXiv:2009.07772] |
| random-rotation stack | tSZ rotationally invariant on average | removes tSZ, CIB and member emission together; the tSZ-nulled alternative "approximately doubles the mass uncertainty" in SPT-3G [src: Sect. 4.3.1, arXiv:2404.02153]; in simulations the mitigation step costs a factor ≈ 2 in mass error against a foreground-free baseline, ≈ 2.5 with 0.5′ positional errors added [src: Sect. 5.3.2, arXiv:2305.06326] | SPT-3G, Levy et al. forecasts |
| tSZ in the pixel covariance | tSZ profile known | percent-level mis-modelling gives ≈ 6% bias, while current tSZ modelling errors are "more than an order of magnitude larger" [src: Sect. 4.6.2, arXiv:1705.00411] | proposed only |
| polarisation | foregrounds largely unpolarised | needs about ten times lower noise; 4.8σ from about 18000 DES clusters at λ ≥ 10 in SPTpol [src: abstract, arXiv:1907.08605] | SPTpol |

A null band near 217 GHz is not a way out: dusty member galaxies rise
steeply with frequency, and the estimated tSZ–CIB signal at 220 GHz is
nearly three quarters of the 150 GHz tSZ signal [src: Sect. 4.6.1,
arXiv:1705.00411].

### Treatment of the kSZ
<!-- key: treatment-of-the-ksz -->

The kSZ sign follows each cluster's line-of-sight velocity. In a rotated
stack it averages out and only increases the mass uncertainty, by a
factor 1.2 in simulations [src: Sect. 5.3.2, arXiv:2305.06326]. In a
pixel-likelihood fit that omits it from the covariance it biases the mass
low by 41% (32% with an analytic model), vanishes when the covariance is
built from the same simulations, and returns as −7.5 ± 0.4% for a 20%
error in the kSZ model [src: Sect. 4.5, arXiv:1705.00411]. In the
Planck + SPT quadratic-estimator analysis a 300 km/s velocity dispersion
shifts M_CMBlens/M_SZ by −0.060 ± 0.015, and the result is corrected for
it [src: Sect. 6.1, arXiv:2402.18346]. So the kSZ is harmless for a
stack and a correctable bias for per-cluster quadratic or likelihood
estimators.

### Estimator
<!-- key: estimator -->

| Estimator | Buys | Costs | Comparison on the same simulations |
|---|---|---|---|
| quadratic (band-limited gradient) | analytic normalisation and noise (N⁽⁰⁾, N⁽¹⁾); public tools | linear in κ, suboptimal at low noise; needs mean-field subtraction | Planck: "very close to the optimal" at Planck noise, citing arXiv:1705.00411 [src: Sect. 4.2, arXiv:1904.07887] |
| maximum likelihood | optimal; uses Q/U directly without E/B loss | pixel covariance per mass; kSZ and tSZ must sit in the covariance | outperforms the quadratic estimator by a factor of two at low temperature noise [src: abstract, arXiv:1705.00411] |
| rotated stack | simple; kSZ-immune; tSZ removable by rotations | gradient-direction noise must be forward-modelled | same mass error as the MLE over 0.1–7 μK-arcmin; the quadratic estimator matches both for ΔT ≥ 3 μK-arcmin and is two times worse at 0.1 μK-arcmin [src: Sect. 5.2, Fig. 3, arXiv:2305.06326] |
| gradient inversion | near-MLE at low cost | not yet applied to data in the papers read | up to ≈ 50% better than the quadratic estimator at z = 2, 1 μK-arcmin [src: abstract, arXiv:1710.10236] |

### Mass observable and its entry into the counts
<!-- key: mass-observable-and-its-entry-into-the-counts -->

- Mean mass of a stack, fitted with a population model: robust for
  optical samples, but a single number per bin; used as a prior on the
  model mean (SPT-SZ) or to calibrate a richness–mass normalisation
  (SPTpol, SPT-3G).
- Per-cluster signal-to-noise in a hierarchical model with correlated
  scatter (Planck): keeps the selection on SZ explicit and avoids the
  ratio-estimator bias, at the cost of a prior on the lensing-observable
  bias and scatter from N-body simulations (see "Numbers").
- Combining data sets of different resolution: Planck + SPT-SZ reaches
  4.8σ against 3.9σ (SPT-SZ only) and 3.7σ (Planck only), using both the
  two ranges of scales and the lensing-induced correlation between them
  [src: abstract, arXiv:2402.18346].

### Weight in a current counts analysis
<!-- key: weight-in-a-current-counts-analysis -->

In SPT-SZ counts with Planck spectra, moving the SZ normalisation A_SZ
from 4.4 to 5.5 changes the optical weak-lensing log-likelihood by −5.8
and the CMB-cluster-lensing one by −0.38, 15 times less; the CMB-lensing
term therefore did not change S8 [src: Sect. IV.1, arXiv:2111.07491].
Its forecast value lies in the redshift lever arm: for SPT-3G, adding
CMB-cluster lensing alone reduces the 7-parameter wCDM volume by a factor
2.8 and σ(σ8) from 0.039 to 0.016 (**forecast**) [src: Sect. V, Table 3,
same].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Gradient band limit | ℓ ≤ 2000 | Planck, ACT, SPT-3G | arXiv:1904.07887; arXiv:2009.07772; arXiv:2404.02153 | Sect. 4.2; App. A; Eq. 1 |
| High-resolution leg; output band | ℓ ≤ 6000; 200 < L < 5000 | ACT × MaDCoWS | arXiv:2009.07772 | App. A |
| Mean field | 20% (bin 1), 50% (bin 2), > 100% beyond | ACT | arXiv:2009.07772 | App. A |
| Randoms | 10 N_clus (stack); ≈ 300 N_clus (mean field); 16384 per band | SPT-3G; ACT; Planck | as listed | Sect. 3.1; App. A; Sect. 4.2 |
| Fit range | 5 bins within 8′ | ACT | arXiv:2009.07772 | App. B |
| Miscentring prior | f_mis = 0.22 ± 0.11; ln c_mis = −1.13 ± 0.22 | SPT-3G × DES Y3 | arXiv:2404.02153 | Sect. 3.4 |
| Lensing-observable priors | 1 − b_CMBlens 0.93 ± 0.05; σ_CMBlens 0.20 ± 0.05; r 0.83 ± 0.10 | Planck MMF3 | arXiv:1904.07887 | Table 3 |
| Posteriors | 1 − b_CMBlens 0.92 ± 0.05; σ_CMBlens 0.21 ± 0.04; r 0.80 +0.06/−0.09; ⟨p_obs⟩ = 0.234 ± 0.052 (4.5σ) | same | same | Table 5; Sect. 8 |
| Stacked masses, DES Y3 redMaPPer | M200m = 1.66 ± 0.13 ± 0.03, 1.97 ± 0.18 ± 0.05, 2.11 ± 0.20 ± 0.05 (× 10¹⁴ M_sun; flux-, volume-, volume&redshift-limited) | SPT-3G 2019–20 | arXiv:2404.02153 | Sect. 4.2 |
| Systematic budget | miscentring 1.7%, beam 1.7%, residual foregrounds 1.3%, filtering 0.9%; total 2.4% (0.25σ) | same | same | Table 2 |
| Modelling budget on M_CMBlens/M_SZ | total ± 0.026 (14% of the 0.190 statistical error); profile truncation +0.017/−0.019; kSZ bias −0.060 corrected | Planck + SPT-SZ, 468 clusters | arXiv:2402.18346 | Table 5 |
| Ratio | M_CMBlens/M_SZ = 0.98 ± 0.19 ± 0.03 | same | same | abstract |
| SPTpol temperature | M200m = 1.62 +0.32/−0.25 ± 0.04 (volume-limited, 1741) and 1.28 +0.14/−0.18 ± 0.03 (flux-limited, 4003), × 10¹⁴ M_sun; systematics dominated by centroids | SPTpol × DES Y3 | arXiv:1810.10998 | abstract |
| Forecast mass precision | SPT-3G Main T 7.1%, T + Pol 6.4%, Main + Extended T + Pol 5.7% (**forecast**) | SPT-3G × DES | arXiv:2404.02153 | Table 3 |
| Forecast mass precision | 6.6% (SPT-3G, 7000 clusters), 4.1% (SO, 25000), 3.9% (SO + FYST), 1.8% (CMB-S4, 100000) (**forecast**) | rotated stack, temperature | arXiv:2305.06326 | Sect. 6.2 |
| Forecast mass precision | 3–6% for SPT-3G, AdvACT, Simons Array with 10000 clusters; < 1% for CMB-S4 with 100000 (**forecast**) | MLE | arXiv:1705.00411 | abstract |

The three forecasts differ because they assume different estimators,
foreground treatments and sample sizes; the 1.8% of arXiv:2305.06326
includes tSZ mitigation, the < 1% of arXiv:1705.00411 does not include
the foreground biases of its own Table 1.

## What goes wrong
<!-- key: what-goes-wrong -->

| Failure | How it shows | Test that catches it | Source |
|---|---|---|---|
| tSZ leakage into the stack | mass biased low; model–data PTE ≈ 0 because the stack is dominated by the mean tSZ | compare with a tSZ-nulled map (SPT-3G: consistent); rotation stacks; foreground-free versus foreground simulations (1.3% shift) | arXiv:2305.06326, Sect. 5.3.2; arXiv:2404.02153, Sect. 4.3.1 |
| Imperfect tSZ frequency cleaning | −6.3 ± 0.7% for 1% relative calibration error | calibration and bandpass checks; relativistic tSZ in the spectrum (−0.012 on the ratio when omitted) | arXiv:1705.00411, Sect. 4.6.1; arXiv:2402.18346, Sect. 6.6 |
| Dust in the gradient map | spurious correlated signal in both legs | stack the gradient map at all cluster positions (ACT: no residual over 1676 clusters) | arXiv:2009.07772, App. A |
| Dusty members, fitting approach | −4.5 ± 1.7% in temperature, −1.3 ± 1.2% in polarisation | multi-frequency checks | arXiv:1705.00411, Table 1 |
| Spurious lensing from masks, noise, beams | non-zero signal at random points | mean field from randoms; curl null test (ACT PTE 0.05) | arXiv:2009.07772, App. A |
| Miscentring | mass low; −7.5% (T) for typical SZ offsets without correction; −0.05 ± 0.01 at 0.5′, −0.01 ± 0.01 after shifting the models | forward-model offsets in the templates; vary priors (SPT-3G +1.7%) | arXiv:1705.00411, Table 1; arXiv:2305.06326, Sect. 5.3.1; arXiv:2404.02153, Sect. 4.3.2 |
| Correlated haloes along the line of sight | mass high by 2.5 ± 0.3% (T) and 6.3 ± 1.1% (Q/U) | fit a two-halo term | arXiv:1705.00411, Sect. 4.1 |
| Wrong profile shape | −2.4% to +3.1% (T) for Einasto, modified NFW, substructure (Table 1; the text of Sect. 4.2 says −2.5% to 3.8%); concentration ± 20% moves ACT mass ± 10% | vary truncation radius and c–M relation | arXiv:1705.00411, Table 1; arXiv:2009.07772, App. B |
| Template-scale mismatch in a matched filter | linear bias in M̂ | use the signal-to-noise p_obs | arXiv:1904.07887, Sect. 4.3.3 |
| SZ selection in a ratio estimator | 1 − b biased high | hierarchical model with correlated scatter | arXiv:1904.07887, Sect. 5 |
| Transfer function and beam | 0.9% (ℓ₁ = 300 ± 20) and 1.7% | vary filter edge; beam realisations from its covariance | arXiv:2404.02153, Sects. 4.3.3–4.3.4 |
| Contaminated optical sample | low-mass projected groups lower the stacked mass as they do for galaxy lensing | SZ or X-ray cross-match; flux-limited stack ≈ 20% below volume-limited | arXiv:2404.02153, Sects. 4.2 and 4.3.5 |

Validation suites as stated: SPT-3G runs 25 mock sets of 5500 clusters,
each with its own jackknife covariance, plus 25 model sets per mass bin
[src: Sect. 3.4, arXiv:2404.02153]; Planck
validates its likelihood on simulated catalogues (Sect. 7 of
arXiv:1904.07887, not read in detail).

## Reading list
<!-- key: reading-list -->

- Foundation: Seljak & Zaldarriaga 2000 (arXiv:astro-ph/9907254), for the
  dipole and why it traces the outer cluster.
- Method, estimator comparison and systematics table: Raghunathan et al.
  2017 (arXiv:1705.00411), Table 1 is the reference list of biases.
- Method, small-scale lenses: Horowitz et al. 2019 (arXiv:1710.10236),
  for gradient inversion and the limits of the quadratic estimator.
- Method, foreground-immune stack: Levy et al. 2023 (arXiv:2305.06326),
  Eqs. 13–17 and the kSZ and tSZ tests.
- Application, likelihood: Zubeldia & Challinor 2019 (arXiv:1904.07887),
  Sects. 4–6, for the signal-to-noise observable, the hierarchical model
  and the critique of the ratio estimator.
- Application, high redshift: Madhavacheril et al. 2020
  (arXiv:2009.07772), Appendices A–B, for the quadratic estimator with a
  tSZ-free gradient and the population model of a stacked profile.
- Application, current precision: Ansarinejad et al. 2024
  (arXiv:2404.02153), Sects. 3–4, for the full SPT-3G pipeline and budget.
- Application, data combination: Huchet & Melin 2024 (arXiv:2402.18346),
  for ground + space ILC and the kSZ correction.
- Application, counts: Chaubal et al. 2022 (arXiv:2111.07491), Sects. III
  and V, for the mean-mass prior and SPT-3G and CMB-S4 forecasts.
- First detections: Baxter et al. 2015 (arXiv:1412.7521), MLE on 513 SPT
  clusters; Raghunathan et al. 2019 (arXiv:1907.08605), polarisation only.

## Not verified
<!-- key: not-verified -->

- Hu, DeDeo & Vale 2007 and Lewis & King 2006, the quadratic and
  likelihood foundations cited by every paper above, and Melin & Bartlett
  2015, the matched-filter approach behind the Planck 2015 CMB-lensing
  calibration: not read.
- The N-body study that set the Planck priors on the lensing-observable
  bias and scatter is cited as "in prep." in arXiv:1904.07887 and was not
  located.
- The SPT-3G richness–mass normalisation result (Sect. 4.4 of
  arXiv:2404.02153) and the redshift trend of its stacked mass (Sect.
  4.5): not read.
- The cleaned-gradient method paper cited by ACT for its tSZ-deprojected
  gradient: not read, so not cited.
- No CMB-cluster-lensing mass calibration posted after June 2025 was
  found in two date-sorted searches (2026-10-18); in particular none from
  ACT DR6, SPT-3G five-year data or Simons Observatory.
