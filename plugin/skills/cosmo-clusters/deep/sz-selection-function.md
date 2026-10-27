# SZ selection function — cosmo-clusters dossier

Scope: how a tSZ cluster sample is detected and how its selection is
written into the count likelihood (matched filter, choice of observable,
optimisation bias, the significance–mass link, completeness, purity and
optical confirmation), and how to choose between the SPT, ACT and Planck
conventions.
Snapshot: 2026-10-17.
From: Miyatake 2025 review (arXiv:2505.07697), Sects. 3.3–3.4; SPT, ACT
and Planck catalogue papers (arXiv:2311.07512, arXiv:2507.21459,
arXiv:1502.01598).

Already in L2, not repeated here: contamination sizes (dust, radio,
relativistic corrections, CIB, purity) in
`systematics.md#sz-selection-astrophysical-contamination`; the Planck
Y–M relation and its priors in
`systematics.md#planck-2015-sz-counts-planck-collaboration-2015`; the SPT
priors, sample and purity in
`systematics.md#spt-clusters-with-des-y3-and-hst-lensing`; the binned
and unbinned Poisson likelihoods in
`physics-and-methods.md#count-likelihoods-and-covariance`; the general
observable table in
`physics-and-methods.md#observables-and-observable-mass-relations`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Filter the maps
<!-- key: step-1-filter-the-maps -->

All three experiments detect clusters with a multi-frequency matched
filter. ACT writes it as ψ(k_x, k_y, ν_i) = A Σ_j N⁻¹_ij(k_x, k_y)
f_SZ(ν_j) S(k_x, k_y, ν_j), with N the noise covariance between the
frequency maps, S the beam-convolved signal template, f_SZ = x (e^x + 1)/
(e^x − 1) − 4 the non-relativistic tSZ spectrum (x = hν/k_B T_CMB), and A
a normalisation such that the filter returns the central Comptonization
(arXiv:2009.11043, Eqs. 1–2) [src: Sect. II.2]. The filter is 2D in
Fourier space because the scan pattern makes the noise anisotropic; the
template is axisymmetric [src: same].

| Choice | SPT (SPTpol 500d) | ACT (DR5, DR6) | Planck (MMF3, SZiFi) |
|---|---|---|---|
| Template | projected β profile ΔT = ΔT_0 (1 + θ²/θ_c²)^−(3β−1)/2 with β = 1 (arXiv:2311.07512, Eq. 1) | Universal Pressure Profile of Arnaud et al. 2010 (arXiv:0910.1234) convolved with the beam | Arnaud et al. 2010 profile |
| Scales searched | 12 core radii θ_c from 0.25′ to 3′ [src: arXiv:2311.07512, Sect. 3] | 16 filters, M500c ∈ {1, 2, 4, 8} × 1e14 M_sun × z ∈ {0.2, 0.4, 0.8, 1.2} [src: arXiv:2009.11043, Sect. II.2; same in DR6, arXiv:2507.21459, Sect. 2.2.2] | θ500 from 1 to 35 arcmin (see L2) |
| Noise covariance | not stated in the section read | estimated from the maps themselves, which are CMB-dominated on large scales and white-noise-dominated on small scales [src: arXiv:2009.11043, Sect. II.2] | from the data covariance in the official catalogues; iterative in SZiFi [src: arXiv:2408.06189, Sect. 3.3.5] |
| Map handling | point sources > 6 mJy at 150 GHz masked; massive SPT-SZ clusters at ξ ≥ 6 masked in a first pass, then added back [src: arXiv:2311.07512, Sect. 3] | 280 tiles of ≈ 10° × 5° with their own filters in DR5 [src: arXiv:2009.11043, Sect. II.2] | HEALPix tiles [src: arXiv:2408.06189, Sect. 3.3.1] |

The SPT reason for masking massive clusters first: at SPTpol depth the
Fourier filtering creates spurious candidates around massive clusters along
the scan direction [src: arXiv:2311.07512, Sect. 3].

### Step 2. Estimate the noise without the clusters
<!-- key: step-2-estimate-the-noise-without-the-clusters -->

If the tSZ signal of the detections stays in the maps used to estimate N,
two things happen: N is overestimated, so fewer and less significant
detections are made, and a negative "covariance bias" appears in q_obs and
ŷ_0 because the signal is in the covariance estimated from the same data,
analogous to the ILC bias [src: arXiv:2408.06189, Sect. 3.3.5]. SZiFi
masks every candidate above q_mask = 4 within 3 θ̂500 and re-estimates the
covariance once; one iteration removes both effects [src: same]. ACT DR6
does the same with a multi-pass run of its finder (Nemo): bright point
sources (S/N > 50, then S/N > 5) are found and subtracted, clusters are
detected at q > 3, subtracted with their best template, and the final run
detects q̃ > 4; further passes add no candidates [src: arXiv:2507.21459,
Sect. 2.2.2]. The official Planck catalogues took the noise covariance
equal to the data covariance [src: arXiv:2408.06189, Sect. 3.3.5].

### Step 3. Define the selection observable
<!-- key: step-3-define-the-selection-observable -->

- **SPT**: ξ is "the maximum detection significance across the 12 matched
  filter scales" [src: arXiv:2311.07512, Sect. 3, footnote 5].
- **ACT**: two quantities are kept. SNR is maximised over filter scales;
  SNR_2.4 (written q̃ in DR6) is measured at a fixed reference scale
  θ500c = 2.4′, which corresponds to M500c = 2 × 1e14 M_sun at z = 0.4
  [src: arXiv:2009.11043, Sects. II.2–II.3]. The reason given: a fixed
  scale avoids inter-filter noise bias, where local noise (a CMB cold spot
  near a candidate) changes the signal and size estimated at the best
  scale; maximisation over position still leaves a positive bias of ≈ 7%
  at SNR_2.4 = 4 [src: Sect. II.3]. DR6 also reports positions from the
  2.4′ map "for the purposes of minimizing optimization bias and
  calculating the correction for this consistently" [src:
  arXiv:2507.21459, Sect. 2.2.2].
- **Planck**: the signal-to-noise q of the MMF3 detection, with
  q_cat = 6 for the cosmology sample (see L2).

### Step 4. Link the observable to mass
<!-- key: step-4-link-the-observable-to-mass -->

Three forms are in use.

**SPT** (arXiv:2310.12213, Sect. VI):

    P(ξ | ζ) = N( sqrt(ζ² + 3), 1 )                                   (Eq. 40)
    ⟨ln ζ⟩ = ln A_SZ + B_SZ ln(M200c / 3e14 M_sun/h) + C_SZ ln(E(z)/E(0.6))   (Eq. 41, arXiv:2310.12213)

ζ is the "unbiased significance", the significance at the true position and
scale; the "+3" accounts for maximisation over three free parameters (R.A.,
Dec., filter scale) with unit noise in the rescaled maps [src: Sect. VI].
Intrinsic scatter is lognormal in ζ with width σ_lnζ. The depth of each
field enters as A_SZ,field = γ_field A_SZ (Eq. 42), and C_SZ is shifted per
survey: −0.09 for SPTpol ECS and +0.26 for SPTpol 500d relative to SPT-SZ
(Eq. 43) [src]. The relation fails for ξ < √3; below ζ_min = 1, estimated
from simulations, maximisation bias is not applied, and ζ_min = 2 changes
the parameters little [src: arXiv:2401.02075, Sect. IV.2.5]. In the
cosmology fit ζ, M_WL and richness share one multivariate lognormal with
correlated scatter (arXiv:2310.12213, Eqs. 46–47).

**Planck** (arXiv:1502.01597, Sects. 3.1–3.3): the mean signal-to-noise
q̄_m ≡ Ȳ500(M500, z) / σ_f[θ̄500(M500, z), l, b] (Eq. 3), where σ_f is the
filter noise, which depends on sky position (l, b) and on cluster size.
Observed q is drawn from P[q | q̄_m] = ∫ d ln q_m P[q | q_m] P[ln q_m | q̄_m]
(Eq. 10), the second factor being lognormal intrinsic scatter of width
σ_lnY (Eq. 11). The detection probability above q_cat is
χ̂ = ∫_{q_cat}^∞ dq P[q | q̄_m] (Eq. 5). With pure Gaussian noise
P[q | q_m] is a unit Gaussian and the selection function is the "ERF
completeness" χ = ½ [1 − erf((q_cat − q_m)/√2)] (Eq. 14) [src].

**ACT** (arXiv:2507.21459, Sect. 2.5): ỹ_0 = 10^A_0 E(z)² (M500c /
M_pivot)^(1+B_0) Q(θ500c) f_rel(M500c, z) (Eq. 4), with B_0 = 0.08,
M_pivot = 3 × 1e14 M_sun, Q the filter-mismatch function (the size
difference between a cluster and the 2.4′ reference filter, one Q per
tile), f_rel the relativistic correction and σ_int = 0.2 lognormal
intrinsic scatter [src]. Completeness on a (M500c, z) grid is an
area-weighted sum over noise patches i of an ERF in q̃_i = ỹ_0 / δỹ_0i,
integrated over the lognormal scatter (Eqs. 6–8), with ỹ_0 first corrected
for optimisation bias, ỹ_0^corr = ỹ_0 (1 + q̃^−p) (Eq. 10), p = 2.1 from
30 end-to-end simulations [src: Sect. 2.6, Appendix B].

### Step 5. Purity and optical confirmation
<!-- key: step-5-purity-and-optical-confirmation -->

- **Purity from simulations with tSZ.** SPT now estimates false detections
  on simulated skies that contain tSZ from halo light-cones: candidates are
  matched to the most massive unmatched halo within 2′, random sightlines
  give the chance-association probability f_R(M), and the true-association
  fraction p(M, ξ_min) = (N_obs − N_cand f_R)/(N_cand (1 − f_R)) is
  integrated down in mass [src: arXiv:2311.07512, Sect. 6.4]. The reason:
  tSZ-free simulations overestimate the number of false candidates by a
  factor ≈ 1.4 at ξ_min = 4, because foregrounds and the tSZ field are not
  Gaussian [src: same]. ACT DR5 still used signal-free simulations (CMB +
  CIB + white noise), which the authors call "slightly optimistic" for the
  false-positive rate but a reasonable match to optical confirmation [src:
  arXiv:2009.11043, Sect. II.2].
- **Optical confirmation as part of the selection.** SPT runs MCMF on each
  candidate and on random positions, and confirms a candidate when its
  richness exceeds λ_min(z), set so that the chance-association probability
  gives > 98% purity at every redshift; DES is used to z ≈ 1.1, WISE beyond
  [src: arXiv:2310.12213, Sect. II.1]. The threshold of 98% was chosen
  "such that the remaining level of contamination is within the shot noise
  of the total sample size" [src: footnote 3]. The selection modelled in
  the likelihood is then ξ > 5, z > 0.25 outside DES (110 clusters, Eq. 1),
  and ξ > 4.25 / 4.5 / 5 (500d / SZ / ECS), λ > λ_min(z), z > 0.25 inside
  DES (895 clusters, Eq. 2) [src]. The different ξ cuts keep purity about
  constant across surveys of different depth, since a fixed number of noise
  peaks above a ξ cut is spread over more real clusters in a deeper field
  [src: Sect. II.1, footnote 4].
- **Why z > 0.25.** Map filtering against atmosphere and the primary CMB
  makes the SPT selection evolve strongly at low redshift [src:
  arXiv:2310.12213, Sect. II.1].

### Step 6. Validate the selection
<!-- key: step-6-validate-the-selection -->

- Planck: the ERF completeness is compared with Monte Carlo injection of
  simulated clusters into the maps, including profile-shape variations,
  and with an external truth table (MCXC clusters at z < 0.2, which ROSAT
  should all contain, and SPT clusters); results are "consistent with
  Gaussian noise" [src: arXiv:1502.01597, Sect. 3.3].
- ACT DR6: 30 end-to-end simulated skies (Tinker 2008 haloes, Arnaud
  profiles, CMB, anisotropic white noise scaled up by 1.16 to match the
  real ỹ_0 noise, 1/f atmospheric noise) are run through Nemo; the forward
  prediction gives 5766 clusters at q̃ > 5 in the Legacy footprint against
  5732 detected on average, within 1% [src: arXiv:2507.21459, Appendix B].
- SZiFi: on synthetic Planck-like maps, the iterative iMMF6 catalogue has
  785 clusters; the prediction is 818 ± 29 (1.14σ) with the optimisation
  bias and 688 ± 26 (−3.73σ) without it. Without iterative noise
  estimation the catalogue has 719 clusters against 780 ± 28 and 654 ± 25
  [src: arXiv:2408.06189, Sect. 9.2].
- Against another selection: forced photometry of ACT DR6 maps at eRASS1
  positions (see "What goes wrong").

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Correct the optimisation bias or not
<!-- key: correct-the-optimisation-bias-or-not -->

- **What it is.** The optimal signal-to-noise q_opt is obtained by
  maximising over noisy data, so it is biased high and non-Gaussian even
  for a perfect template, no foregrounds and Gaussian noise [src:
  Zubeldia et al. 2021, arXiv:2106.03718, abstract]. The mean is written
  q̄_obs = [q̄² + f]^{1/2} with f the number of maximised parameters, f = 3
  for two sky coordinates and θ500 (arXiv:2408.06189, Eq. 9) [src: Sect.
  9.2]. In mock observations q_opt is a unit-variance Gaussian for
  q ≥ 6, f_eff ≈ 3 for q̄_t > 6 and f_eff grows at lower signal-to-noise
  [src: arXiv:2106.03718, abstract and Sect. 3.2.3].
- **Who corrects it.** SPT through Eq. 40 since its early analyses; ACT
  DR6 through Eq. 10 above; Planck 2015 set f = 0 [src: arXiv:2408.06189,
  Sect. 9.2].
- **What it costs to ignore.** For Planck at q ≥ 6 the change in counts is
  below the Poisson error in every bin; for a Simons Observatory-like
  survey it exceeds the Poisson error in the lowest bins, especially with
  q_th = 5 [src: arXiv:2106.03718, Sect. 3.4.2]. A free tSZ–mass relation
  can absorb part of the bias, but not all, because it is not a power law
  [src: same, footnote 3].
- **SPT and ACT forms differ.** SPT shifts the mean of ξ (Eq. 40); ACT
  multiplies ỹ_0 by 1 + q̃^−2.1, with the bias reaching 1.03 at q̃_FP ≈ 5,
  and sets the correction to 1 more than 3 below the q̃ cut where Eq. 10
  diverges [src: arXiv:2507.21459, Appendix B].

### Optimal or fixed filter scale
<!-- key: optimal-or-fixed-filter-scale -->

The optimal observable (SPT ξ, ACT SNR, Planck q) carries extra
maximisation over size and is affected by inter-filter noise; the fixed
2.4′ observable avoids the latter at the cost of a filter-mismatch function
Q that depends on the assumed profile and on mass and redshift [src:
arXiv:2009.11043, Sect. II.3]. In Planck the dependence on cluster size
enters through σ_f[θ̄500(M, z)] in Eq. 3 [src: arXiv:1502.01597, Sect.
3.1].

### Analytic or injected completeness
<!-- key: analytic-or-injected-completeness -->

Planck chose MMF3 rather than the intersection of three detection methods
because the ERF model needs well-defined noise σ_f, which the intersection
catalogue lacks [src: arXiv:1502.01597, Sect. 3.3]. The Monte Carlo and
ERF completeness differ by ≈ 2.5% in modelled counts per redshift bin, 9%
at most, and the cosmology moves by < 0.5σ in Ω_m and σ8 (with 1 − b fixed
at 0.8 for the test); the ERF was kept "for simplicity" [src: Sect. 3.3,
Appendix A.1]. ACT DR6 also uses a semi-analytic ERF sum, validated on
end-to-end simulations [src: arXiv:2507.21459, Sect. 2.6].

### Lower significance threshold with optical confirmation
<!-- key: lower-significance-threshold-with-optical -->

Going below ξ = 5 with MCMF confirmation raised the SPT z < 1 sample from
654 to 869 clusters. S8^opt was unchanged; B_SZ, C_SZ and Ω_m moved up.
Using the covariance of a subset (difference of covariances) the Ω_m shift
is 0.9σ, against 0.5σ from adding variances, and mock pairs give similar
shifts [src: arXiv:2401.02075, Sect. IV.2.6]. The full sample against
ξ > 5, 0.25 < z < 1 differs by 1.2σ; the authors find no significant
internal tension [src: same].

### Which mass scale the catalogue masses carry
<!-- key: which-mass-scale-the-catalogue-masses-carry -->

ACT DR6 changed its normalisation to 10^A_0 = 3.0 × 1e-5, ≈ 60% of the
Arnaud et al. value 4.95 × 1e-5 used by earlier ACT and by Planck, to agree
with stacked lensing of ACT DR5 (1 − b = 0.65 ± 0.05, Robertson et al.
2024, arXiv:2304.10219) [src: arXiv:2507.21459, Sect. 2.5]. The 90%
completeness limit at z = 0.5 for q̃ > 5 is therefore M500c > 5.3 × 1e14
M_sun on the new scale and 3.0 × 1e14 M_sun on the A10 scale (DR5:
3.8 × 1e14 M_sun on the A10 scale) [src: Sect. 2.6]. Catalogue masses are
Eddington-corrected posteriors with a Tinker 2008 prior at σ8 = 0.80;
"uncorrected" masses are given for comparison with PSZ2 [src: Sect. 2.5].
A completeness limit is meaningful only with its mass scale.

### Frequency channels and CIB deprojection
<!-- key: frequency-channels-and-cib-deprojection -->

SZiFi builds ten iterative filters from six, five or four HFI channels,
with or without spectral deprojection of a CIB SED and of its first
moment in β or β_T, because the CIB rises with frequency and its SED
varies between clusters and with redshift [src: arXiv:2408.06189, Sect.
3.2, Table 1]. Two earlier studies disagree on the size of the
cluster-correlated CIB effect on Planck: about 10% fewer detections at
0.4 < z < 0.8 and negligible cosmology shifts (Melin et al. 2018), against
a more significant impact on Websky synthetic maps (Zubeldia et al.
2023b), as summarised there [src: Sect. 3.2]. SPTpol 500d gives the 95 and
150 GHz channels close to equal weight because the tSZ signal is 1.6 times
brighter at 95 GHz in CMB temperature units [src: arXiv:2311.07512,
Sect. 3].

### Redshift evolution tied to depth
<!-- key: redshift-evolution-tied-to-depth -->

In SPTpol 500d simulations C_SZ is higher by 0.26 than in SPT-SZ and ECS
fields (a 7σ shift in the simulations), from lower noise, which helps
high-z clusters more because of the fixed primary-CMB noise at low ℓ, and
from the larger 95 GHz weight, which helps low-z clusters [src:
arXiv:2311.07512, Sect. 6.2]. Single-frequency runs move C_SZ by −0.2
(95 GHz only) and +0.2 (150 GHz only) [src: same]. The depth factor is
γ = 2.23 for 500d, i.e. ≈ 1.8 times higher significance than SPT-SZ
[src: same].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| ξ–ζ relation | P(ξ\|ζ) = N(√(ζ²+3), 1) | SPT | arXiv:2310.12213 | Eq. 40 |
| ζ_min | 1 (2 tested) | SPT | arXiv:2401.02075 | Sect. IV.2.5 |
| SZ relation fit | ln A_SZ = 0.72 ± 0.09, B_SZ = 1.69 ± 0.06, C_SZ = 0.50 ± 0.27, σ_lnζ = 0.20 ± 0.05 (M200c, pivot 3e14 M_sun/h) | SPT clusters + lensing | arXiv:2401.02075 | Table 3 |
| ξ cuts | 4.25 / 4.5 / 5 (500d / SZ / ECS) with λ > λ_min(z); 5 outside DES | SPT | arXiv:2310.12213 | Eqs. 1–2 |
| Confirmed-sample purity target | > 98% | SPT MCMF | arXiv:2310.12213 | Sect. II.1 |
| False detections, tSZ-free vs tSZ sims | overestimated × 1.4 at ξ_min = 4 | SPTpol 500d | arXiv:2311.07512 | Sect. 6.4 |
| Purity of confirmed sample | 93% (sims), 95% (empirical), quoted ≈ 94% | SPTpol 500d | arXiv:2311.07512 | Sect. 6.4 |
| SPTpol depth factor | γ = 2.23; ΔC_SZ = 0.26 | SPTpol 500d | arXiv:2311.07512 | Sect. 6.2 |
| Reference filter | 2.4′ ↔ M500c = 2e14 M_sun at z = 0.4 | ACT | arXiv:2009.11043 | Sect. II.3 |
| Residual position bias | ≈ 7% at SNR_2.4 = 4 | ACT DR5 | arXiv:2009.11043 | Sect. II.3 |
| False positives | 2471 / 75 / 2 above SNR_2.4 = 4 / 5 / 6; fraction 0.34 at 4, 0.03 at 5 | ACT DR5 | arXiv:2009.11043 | Sect. II.2 |
| Intrinsic scatter | σ_int = 0.2 in ỹ_0 | ACT | arXiv:2507.21459 | Sect. 2.5 |
| Optimisation-bias model | C = 1 + q̃_FP^−p, p = 2.1; 1.03 at q̃_FP ≈ 5 | ACT DR6 | arXiv:2507.21459 | App. B, Eq. 10 |
| Completeness validation | 5732 detected vs 5766 predicted, q̃ > 5 | ACT DR6 sims | arXiv:2507.21459 | App. B |
| 90% mass limit, z = 0.5, q̃ > 5 | 5.3e14 M_sun (new scale); 3.0e14 M_sun (A10 scale) | ACT DR6 | arXiv:2507.21459 | Sect. 2.6 |
| Normalisation | 10^A_0 = 3.0e-5 (was 4.95e-5) | ACT DR6 | arXiv:2507.21459 | Sect. 2.5 |
| ERF vs injection completeness | ≈ 2.5% per z bin (max 9%) in counts; < 0.5σ | Planck 2015 | arXiv:1502.01597 | Sect. 3.3, App. A.1 |
| Optimisation-bias count test | 785 observed; 818 ± 29 with, 688 ± 26 without correction | SZiFi validation | arXiv:2408.06189 | Sect. 9.2 |
| Gaussianity of q_opt | unit-variance Gaussian for q ≥ 6 | mock MF observations | arXiv:2106.03718 | abstract, Sect. 3.2.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Optimisation bias left out.** Shows up as too few predicted clusters at
  low signal-to-noise, spread over a broad redshift range (−3.7σ in the
  SZiFi validation) [src: arXiv:2408.06189, Sect. 9.2]. Test: forced
  photometry at the true positions of simulated clusters against blind
  values, as ACT DR6 does [src: arXiv:2507.21459, Appendix B].
- **Noise covariance contaminated by the clusters.** Lower significance and
  a negative bias in q and ŷ_0; in the validation, non-iterative counts
  fall about 1σ below prediction [src: arXiv:2408.06189, Sects. 3.3.5,
  9.2]. Test: re-run with clusters masked from the covariance.
- **Finder settings.** In ACT DR5 the segmentation threshold equal to the
  catalogue cut made the catalogue incomplete at the cut, and a minimum of
  two pixels instead of one made it purer than expected at q ≈ 4; both were
  fixed in DR6 [src: arXiv:2507.21459, Sect. 2.2.2]. Test: reproduce the
  candidate list with an independent run near the threshold.
- **Purity estimated without tSZ in the simulations.** Purity too low at
  low ξ by a factor up to 1.4 in false detections [src: arXiv:2311.07512,
  Sect. 6.4]. Test: compare two tSZ normalisations (power-spectrum matched
  and count matched); they agree within 1σ at ξ > 4.5 [src: same].
- **Radio sources inside clusters.** Forced photometry of ACT DR6 at 428
  eRASS1 positions with M500c > 5e14 M_sun and z > 0.2 gives q̃ > 5 for
  92%; 32 have q̃ < 5, and 14 of them 3 < q̃ < 5. MACS J0242.5−2132, with a
  65 mJy source at 90 GHz in its BCG, is recovered at q̃ = 4.8 with 22% of
  its eRASS1 mass [src: arXiv:2507.21459, Sect. 5.2]. The authors name
  radio AGN as most likely, with X-ray–SZ miscentring as a possible part
  [src: same]. The ACT completeness calculation itself does not include
  sources correlated with clusters [src: Sect. 2.6].
- **Low-redshift filtering.** Strong evolution of the SPT selection below
  z = 0.25, hence the cut [src: arXiv:2310.12213, Sect. II.1].
- **Masses on different scales.** Comparing ACT DR6 masses (new A_0) with
  DR5, Planck PSZ2 (A10 scale, no Eddington correction) or SPT (M200c in
  the cosmology fit, arXiv:2401.02075, Sect. V.2.1) without conversion.
- **Subset tests read with added variances.** For a sub-sample the
  parameter-difference covariance is the difference of the covariances;
  adding variances understates a shift (0.5σ against 0.9σ in SPT) [src:
  arXiv:2401.02075, Sect. IV.2.6].

## Reading list
<!-- key: reading-list -->

- Review: Miyatake 2025, arXiv:2505.07697 — Sect. 3.3 and Eq. 11 for the
  place of the selection in the count model.
- Foundation: Arnaud et al. 2010, arXiv:0910.1234 — the pressure profile
  used as filter template by ACT and Planck.
- Method: Planck 2015 XXIV, arXiv:1502.01597 — Sects. 3.1–3.3: q̄_m, the
  ERF completeness, Monte Carlo and external validation.
- Method: Hilton et al. 2021, arXiv:2009.11043 — Sects. II.2–II.4: the
  fixed-scale observable, Q function, mock completeness.
- Method: Bleem et al. 2024, arXiv:2311.07512 — Sects. 3, 6.2, 6.4: SPT
  filtering, depth factors, purity with tSZ simulations.
- Application: Bocquet et al. 2024, arXiv:2310.12213 and arXiv:2401.02075 —
  ξ–ζ relation, optical confirmation inside the selection, robustness
  tests of the cuts.
- Application: ACT DR6 catalogue, arXiv:2507.21459 — multi-pass filtering,
  optimisation-bias model, end-to-end validation, eRASS1 forced photometry.
- Critique: Zubeldia et al. 2021, arXiv:2106.03718 — why q_opt is biased
  and non-Gaussian, and when it matters.
- Critique and method: Zubeldia et al. 2024, arXiv:2408.06189 — iterative
  noise covariance, CIB deprojection, count validation with and without
  the bias correction.

## Not verified
<!-- key: not-verified -->

- Vanderlinde et al. 2010, cited for the first discussion of the
  optimisation bias and the ξ–ζ form, and Melin et al. 2006, cited for the
  multi-frequency matched filter: not read, no identifier recorded.
- Zubeldia et al. 2023a (iterative noise estimation) and 2023b (CIB
  deprojection with spectrally constrained filters), and Melin et al. 2018
  on dust in Planck clusters: known here only through arXiv:2408.06189,
  Sect. 3.2–3.3.5; bodies not read.
- The Planck PSZ2 Monte Carlo completeness procedure (arXiv:1502.01598)
  and the SPT-3G five-year selection (arXiv:2607.01175): not read this
  session.
- The cluster counts per experiment in Table 1 of arXiv:2106.03718 (the
  table was cut in the rendering).
- The cosmocnc likelihood code for SZ counts: found by title only, not read.
