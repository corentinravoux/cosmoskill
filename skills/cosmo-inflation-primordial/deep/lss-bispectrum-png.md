# Primordial non-Gaussianity from the galaxy bispectrum — cosmo-inflation-primordial dossier

Scope: how f_NL^local, f_NL^equil and f_NL^ortho are obtained from galaxy
power spectra plus bispectra (estimator, binning, PNG terms in the model,
PNG bias parameters and their priors, scale cuts, covariance, validation
on simulations), and how to choose between tree-level and one-loop
bispectra, conservative and simulation-based priors, fixed and free
cosmology. Most EFT power-spectrum-plus-bispectrum f_NL analyses of BOSS
and DESI data read here come from one group (Cabass, Ivanov, Philcox and
co-authors); the independent data analyses are D'Amico et al. (one-loop
bispectrum) and Chen et al. (weighted skew-spectra); the other lines are
power-spectrum-only scale-dependent-bias analyses (eBOSS, DESI) and
simulation studies (Quijote-PNG, field level).
Snapshot: 2026-10-22.
From: Achúcarro et al. 2022 review (arXiv:2203.08128), Sect. 3.2.2 (PNG
from the bispectrum of tracers; map-level inference of PNG).

Already in L2, not repeated here: the result tables (BOSS, DESI DR1, CMB
combination) in `results.md#galaxy-bispectrum`; the prior dependence
940 ± 600 → 260 ± 300 and the simulation-prior DESI + BOSS value in
`systematics.md#d5-bias-parameters-and-scale-cuts-in-bispectrum`; the
b_φ debate for scale-dependent bias in `systematics.md#d1-the-response-bphi`
and `open-questions.md#can-large-scale-structure-overtake-the-cmb-on`; the
BORG field-level forecast in `physics-and-methods.md#galaxy-bispectrum`.
Field-level inference in general is the subject of the
`cosmo-beyond-two-point` dossier `deep/field-level-inference.md`; the EFT
power-spectrum model and its prior conventions are in the
`cosmo-galaxy-clustering` dossier `deep/full-shape-modelling.md`.

## How it is done
<!-- key: how-it-is-done -->

Notation: Φ (or φ) the primordial Bardeen potential, ζ the curvature
perturbation; 𝒯(k) or 𝓜(k) the transfer function from ζ (or φ) to the
linear density, 𝒯 = (P_11/P_ζ)^½; P_11 the linear matter spectrum;
Z_1(k) = b_1 + fμ² and Z_2 the linear and quadratic redshift-space
kernels; b_1, b_2, b_𝒢2, b_Γ3 the Gaussian bias parameters; k_NL the
non-linear scale; P_ℓ and B_ℓ the power-spectrum and bispectrum
multipoles; Q_0 a real-space power-spectrum proxy.

### Step 1. Write the primordial shape
<!-- key: step-1-write-the-primordial-shape -->

The equilateral and orthogonal analyses write
B_ζ = (18/5) f_NL Δ_ζ⁴ 𝒮(k_1, k_2, k_3)/(k_1²k_2²k_3²) (Cabass et al.
2022a, arXiv:2201.07238, Eq. 2), with 𝒮_equil and 𝒮_ortho in Eq. 3
[src]. The orthogonal template used in this line of work is the one with
the physical squeezed-limit suppression 𝒮_ortho ∝ k_1/k_3, "contrasted
with the commonly used approximate template that features an unphysical
enhancement in that limit" (the Planck one) [src: footnote 2]; the 2024
simulation-prior analysis keeps it [src: arXiv:2402.13310, Sect. 4]. A
galaxy f_NL^ortho is therefore not the same template amplitude as the CMB
one unless the template is stated. The amplitudes map to the
effective-field-theory coefficients of single-field inflation (sound speed
c_s, Wilson coefficient c̃_3) through Eq. 5 of arXiv:2201.07238 [src].

### Step 2. Put the PNG terms into the model
<!-- key: step-2-put-the-png-terms-into-the-model -->

Three channels, at first order in f_NL [src: arXiv:2201.07238, Eqs. 8–12;
Chudaykin et al. 2025, arXiv:2512.04266, Sect. 3.3]:

1. **Primordial bispectrum in the initial conditions**:
   f_NL B_111 = 𝒯(k_1)𝒯(k_2)𝒯(k_3) B_ζ (Eq. 8), entering the galaxy
   bispectrum at tree level as f_NL Z_1Z_1Z_1 B_111 (Eq. 12).
2. **Non-Gaussian matter loops** in the power spectrum: P_12 (Eq. 9).
3. **Scale-dependent bias.** For local PNG the new bias field is φ itself,
   δ_g ⊃ b_φ f_NL φ(q) + b_δφ f_NL δ(x)φ(q) (arXiv:2512.04266, Eq. 22),
   which adds tree-level power (Eq. 23), loops P_22^fNL, P_13^fNL (Eq. 24)
   and a tree-level bispectrum term B_112^fNL [src: Sect. 3.3]. Its full
   redshift-space form, B_211^fNL, has four groups of terms in b_δφ and b_φ
   (Cabass et al. 2022b, arXiv:2204.01781, Eq. 34), plus a stochastic term
   in b_φ and b_εφ (Eq. 36) that the authors find irrelevant for BOSS
   [src: Sect. 2.4.2]. For equilateral and orthogonal PNG the bias field is
   ψ = (k/k_NL)^Δ φ with Δ = 2, so it acts like a higher-derivative bias and
   one term suffices, δ_g ⊃ b_ψ f_NL (k/k_NL)² φ (arXiv:2512.04266,
   Eqs. 20–21) [src].

Power counting justifies the truncation: with P_11 ∝ k^n, n ≈ −1.7, the
leading non-Gaussian corrections are the NG matter loops and the linear PNG
bias, while O(f_NL²) terms, NG two-loop terms and operators like δ∇²ζ are
subleading for f_NL Δ_ζ ≲ 0.1 and k ≲ 0.17 h Mpc⁻¹ (arXiv:2201.07238,
Eq. 11) [src]; for local PNG "the situation is different: the PNG bias
terms dominate on large scales" [src: footnote 6]. The DESI DR1
reanalysis omits the PNG loop corrections B_221, B_311 to the bispectrum as
next-to-leading order [src: arXiv:2512.04266, Sect. 3.3, footnote 4].

### Step 3. Fix or prior the PNG bias parameters
<!-- key: step-3-fix-or-prior-the-png-bias-parameters -->

| Analysis | Shape | PNG bias treatment | Place read |
|---|---|---|---|
| BOSS P + B (2022a) | equil., ortho. | b_ζ = 1.686 × (18/5)(b_1 − 1) b̃_ζ with b̃_ζ ~ N(1, 5), "motivated by the peak-background split model" | arXiv:2201.07238, main text |
| BOSS P + B (2022b) | local | b_φ = 2δ_c(b_1 − 0.55), b_δφ = 3.85 − 9.49 b_1 + 3.44 b_1² (Eq. 44), fixed; cross-check with universality (Eq. 43) | arXiv:2204.01781, Sect. 2.6 |
| BOSS P + B (D'Amico et al.) | all three | universality-type relations for b_1^fNL, b_2^fNL (Eq. 54), fixed; widened by 60% and 150% as a test | arXiv:2201.11518, App. A |
| DESI DR1 P + B | equil., ortho. | b_ψ ~ N(0, 5²) | arXiv:2512.04266, Sect. 3.3 |
| DESI DR1 P + B | local | b_φ = 2δ_c(b_1 − p) with p = 0.55 (BGS, LRG, "magnitude limited samples"), 1 (ELG2), 1.6 (QSO, QSO-all); b_δφ from Eq. 26 | arXiv:2512.04266, Eqs. 25–26 |

(δ_c = 1.686.) The stated reason for fixing local PNG biases: universality
works for haloes but "rather poorly for galaxies in hydrodynamical
simulations", and marginalising b_φ, b_δφ with broad priors, though the
strict EFT choice, "severely reduces the information content" because of
the near-perfect b_φ–f_NL degeneracy [src: arXiv:2512.04266, Sect. 3.3].
This answers the open item in `results.md#not-verified`: the DESI DR1
f_NL^local = −0.1 ± 7.4 assumes p = 0.55 / 1 / 1.6 by sample.

Other groups on the same choice, power spectrum only:
- **Barreira 2022** (arXiv:2205.05673) [src]: on the BOSS DR12 power
  spectrum, fixed b_φ(b_1) relations change σ(f_NL) by up to an order of
  magnitude, from 16 ± 16 to 230 ± 226 on the same data; marginalising b_φ
  with wide priors "is not conservative" and biases the result through
  projection effects; only f_NL b_φ is measured (≠ 0 at 1.6σ).
- **DESI DR1 collaboration** (Chaussidon et al. 2024, arXiv:2411.17623)
  [src]: universality for LRGs and a recent-merger model for QSOs gives
  −3.6 +9.0/−9.1; universality for QSOs too gives 3.5 +10.7/−7.4.
- **Simulation priors on p.** IllustrisTNG DESI-like quasars give
  p̄ ≃ 1.4 with weak redshift dependence, robust across CAMELS, and
  f_NL = −3.3 ± 9.2 on DESI DR1 (Fondi et al. 2026, arXiv:2602.12357)
  [src]. Field-level HEFT bias on AbacusSummit LRG- and QSO-like samples
  reduces the b_φ uncertainty by 80%, b_∇ being a proxy for concentration
  (Hadzhiyska & Ferraro 2025, arXiv:2501.14873) [src].

### Step 4. Measure P and B without window convolution
<!-- key: step-4-measure-p-and-b-without-window -->

The analyses of Cabass et al. and the DESI DR1 reanalysis use window-free
or quasi-optimal estimators; D'Amico et al. use FKP weights with a
conventional estimator. Cubic window-free estimators give the
unwindowed bispectrum directly, made of a cubic estimator on the data and a
Fisher matrix that deconvolves the bins; minimum variance for weak
non-Gaussianity, with an FKP-based near-optimal form; the Fisher matrix
costs O(100) extra CPU-hours (Philcox 2021, arXiv:2107.06287, abstract)
[src]. The point stated by the BOSS analyses: "we do not need to include
the survey window function in our theoretical model" [src:
arXiv:2204.01781, Sect. 3]. The DESI DR1 reanalysis uses the PolyBin3D
quasi-optimal estimators, which handle integral constraints, wide-angle
effects and fibre collisions, with an approximate mask deconvolution and
analytic subtraction of the constant Poisson shot noise; Gaussian
covariances from the same package include inhomogeneous shot noise and
masking [src: arXiv:2512.04266, Sect. 2.2]. D'Amico et al. used FKP
weights and the Rustico code on a 512³ grid of side 3500 h⁻¹ Mpc,
Poisson shot noise subtracted at estimator level [src: arXiv:2201.11518,
App. B].

Other estimators: the FFT multipole estimator of Scoccimarro 2015
(arXiv:1506.02729) measures BOSS bispectrum multipoles ℓ = 0, 2, 4 for all
triangles to k = 0.2 h Mpc⁻¹ in about fifteen minutes on one core, which
makes mock covariances affordable [src]. The skew-spectrum analysis of
BOSS uses FKP estimates with an approximate window convolution, which
errs by up to 5% on the gravitational bispectrum above k = 0.03 h Mpc⁻¹,
6% on the equilateral and 18% on the orthogonal skew-spectra (Chen et
al. 2024, arXiv:2401.13036, Sect. 5) [src]. The Quijote-PNG
quasi-maximum-likelihood estimator compresses P and a modal bispectrum;
the modal expansion converges faster in the numerical derivatives of the
score function than k-binning (Jung et al. 2022, arXiv:2211.07565) [src].
A configuration-space route fits the 2PCF and 3PCF monopoles, calibrated
on halo simulations, with a **forecast** σ(f_NL^local) = 22 for DESI Y1
LRGs (Brown et al. 2024, arXiv:2403.18789) [src].

For the high-z quasars (QSO-all), the DESI DR1 reanalysis applies
redshift weights w_0 = D(b_1 − f/3), w_2 = (2/3)Df, w̃ = b_1 − p with
p = 1.6 (Eq. 2), propagated to window matrix and covariance, and weights
the bispectrum fields to match the power-spectrum effective redshift
[src: Sect. 2.2]. Such redshift weights for the scale-dependent bias come
from the eBOSS quasar analyses: they improved the DR14 error by 15% (40%
if quasars have a lower PNG response) (Castorina et al. 2019,
arXiv:1904.08859) and the DR16 result, f_NL = −12 ± 21, by 37% (Mueller
et al. 2021, arXiv:2106.13725) [src].

### Step 5. Bin, cut and choose statistics
<!-- key: step-5-bin-cut-and-choose-statistics -->

| Analysis | P | B | Bins | Place read |
|---|---|---|---|---|
| BOSS 2022a/b (tree B) | P_0,2,4 for 0.01 ≤ k < 0.17 (2022a) or ≤ 0.25 (2022b); Q_0 to 0.4 (2022a) or 0.25–0.27 (2022b); post-recon α's | monopole, k_i ∈ [0.01, 0.08) | 62 triangles per chunk, 4 chunks | arXiv:2201.07238; arXiv:2204.01781, Sect. 3 |
| BOSS (one-loop B) | P_0, P_2 | monopole, k_max = 0.23 for both | Δk ≈ 0.0108 h Mpc⁻¹ (Δn = 6 k_f), first bin 0.016; all closed triangles; Δn = 12 for orthogonal and joint fits | arXiv:2201.11518, Sect. 4, App. B |
| DESI DR1 (one-loop B) | P_0,2,4, 0.005 ≤ k ≤ 0.2 | B_0, B_2, 0.005 ≤ k ≤ 0.16 (tree-level variant 0.08) | Δk = 0.005 → 0.01 → 0.02; 234 triangles per sample | arXiv:2512.04266, Sect. 2.3 |
| DESI DR1 QSO-all (tree) | P_0, P_2, 0.002–0.1 | B_0, 0.002–0.1 | 98 P bins of 0.001; B bin edges from 0.002 to 0.1 | arXiv:2512.04266, Sect. 2.3 |

(k in h Mpc⁻¹.) Reasons stated:

- **k_min = 0.01** in BOSS removes the first bin to limit stellar
  contamination, radial and atmospheric systematics and integral
  constraints; below it, weight-based and more sophisticated mitigations
  differ by more than the statistical errors [src: arXiv:2204.01781,
  Sect. 3]. D'Amico et al. found k_min = 0.005 reliable on Nseries but used
  0.01 on data for the same reason [src: arXiv:2201.11518, App. B].
- **P k_max for local PNG** was raised to 0.25 because cosmology is fixed
  and the f_NL fit stays unbiased to larger k; "the f_NL^local constraints
  are dominated by the linear LPNG bias and hence are saturated at large
  scales"; Q_0 stops at 0.27 because two-loop terms become comparable to
  PNG contributions above 0.3 [src: arXiv:2204.01781, Sect. 3, footnote 2].
- **B k_max at one loop** is set to avoid theory bias (Step 6 and
  "Choices"); a perturbativity prior instead caps the size of loops in
  D'Amico et al. (next step).

Compressed or alternative statistics: tree-level weighted skew-spectra
with the one-loop P_ℓ on BOSS, cosmology fixed to Planck 2018; two PNG
kernels added to the Legendre ones cut the f_NL^equil and EFT errors by
10–20% [src: arXiv:2401.13036, Sect. 5]. On Quijote-PNG haloes
(k_max = 0.5 h Mpc⁻¹), P plus a suitable marked power spectrum beats P
plus B for f_NL^equil (Jung et al. 2024, arXiv:2403.00490) [src]; a
patch-based CNN summary added to P and B gains 30–45% at
k_max ~ 0.1 h Mpc⁻¹ (Cagliari et al. 2025, arXiv:2510.12715) [src]; BORG
field-level inference on Quijote halo catalogues to k_max ≈ 0.1 h Mpc⁻¹
improves σ(f_NL^local) by ~1.3 over a P + B estimator, marginalising
initial conditions and bias (Andrews et al. 2026, arXiv:2603.20855) [src].
All three are simulation studies, not data results.

### Step 6. Likelihood, priors on the Gaussian nuisances, sampling
<!-- key: step-6-likelihood-priors-on-the-gaussian -->

- **Covariance.** 2048 MultiDark-Patchy mocks per chunk for BOSS, on the
  joint P + B (+ α) vector [src: arXiv:2201.07238; arXiv:2204.01781,
  Sect. 3]. D'Amico et al. apply the Hartlap factor and checked that
  compressing the 40 + 1015 bins per sky cut to 100, 200, ... linear
  combinations maximising the f_NL signal-to-noise gives similar results
  [src: arXiv:2201.11518, App. B]. DESI DR1: analytic Gaussian covariance
  (Step 4).
- **Perturbativity prior** (D'Amico et al.): k_max is chosen so that the
  neglected two-loop signal-to-noise is a fraction X² of the total
  (Eq. 36), with X_P = 1/3 and X_B = 1/2 "in order to obtain unbiased
  results"; a penalty on loop sizes exceeding their expected scaling is
  added to −2 ln L (Eqs. 45–46), normalised so that a global excess costs
  O(1) independently of the number of bins [src: arXiv:2201.11518,
  Sect. 3]. Linear EFT parameters are marginalised analytically; only
  f_NL and b_1, b_2, b_5 per sky cut are sampled; Gaussian priors of
  width 2 or 4 on most EFT parameters (table in App. B) [src: App. B].
- **Cosmology.** Fixed to Planck by D'Amico et al., by the BOSS local
  analysis and by the simulation-prior analysis; varied (ω_cdm, h, A_s,
  with BBN ω_b, Planck n_s and Σm_ν = 0.06 eV fixed) in the BOSS
  equilateral/orthogonal baseline, fixed to Planck priors in its
  "aggressive" variant together with halo-relation quadratic biases [src:
  arXiv:2201.07238; arXiv:2204.01781, Sect. 3; arXiv:2201.11518, App. B;
  arXiv:2402.13310, Sect. 4]. Fixing cosmology "formally corresponds to a
  combination of the CMB power spectra and BOSS" [src: arXiv:2204.01781,
  Sect. 3].

### Step 7. Validate on Gaussian-initial-condition simulations
<!-- key: step-7-validate-on-gaussian-initial-condition -->

Each analysis fits the mean of large-volume simulations with f_NL = 0 using
the covariance of the full simulated volume, so that any offset measures
theory error [src: arXiv:2201.07238; arXiv:2204.01781, Fig. 2;
arXiv:2201.11518, Sect. 4]. D'Amico et al. turn the offset into a bound,
σ_th ≲ |μ_sims| − σ_sims (or σ_sims if negative) (Eq. 50) [src]. Chen et
al. fit the mean of 84 Nseries boxes with the 2048-Patchy covariance
rescaled to the BOSS volume (×2.4) and to the full Nseries volume (×84):
the equilateral bias is about 0.53σ of BOSS, the orthogonal 4.15σ, traced
to the window approximation, so f_NL^ortho was not fitted on data [src:
arXiv:2401.13036, Sect. 5, Table 2]. Results are in "Numbers".

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### What the bispectrum adds, by shape
<!-- key: what-the-bispectrum-adds-by-shape -->

- **Equilateral and orthogonal.** The bispectrum drives the constraint:
  BOSS power spectrum alone gives f_NL^equil = −640 ± 1200, f_NL^ortho =
  2400 ± 1600 [src: arXiv:2201.07238]; in DESI DR1 the power spectrum alone
  is about an order of magnitude weaker than with the tree-level
  bispectrum [src: arXiv:2512.04266, Sect. 4.2].
- **Local.** The power spectrum's scale-dependent bias dominates; adding
  the bispectrum tightens BOSS by about 20% (9 +33/−35 → −33 ± 28), by
  about 30% if universality is assumed, and breaks part of the
  degeneracy with the non-Gaussian bias [src: arXiv:2204.01781, Sect. 5,
  Eqs. 46–49]; on DESI QSO-all by about 15% (−2 +11/−10 → −3 ± 9) [src:
  arXiv:2512.04266, Sect. 4.1]. With k_min = 0.05 instead of 0.01 the BOSS
  local error grows by a factor of four [src: arXiv:2204.01781, Eq. 47].
- **The same split in simulations.** On Quijote-PNG haloes, local PNG is
  best measured by the power-spectrum scale-dependent bias with sample
  variance cancellation and small scales add little; equilateral and
  orthogonal information is mostly in the bispectrum, raised up to ×4 by
  small scales, but f_NL^equil stays degenerate with σ8 and the bias model
  (Coulton et al. 2022, arXiv:2206.15450) [src]. The local signal
  saturates at k ~ 0.2 h Mpc⁻¹; **forecast** Δf_NL = 45 (local), 570
  (equil.), 110 (ortho.) for 1 (h⁻¹ Gpc)³ at z = 1 with k_max = 0.5
  [src: arXiv:2211.07565].

### Tree level or one loop for B
<!-- key: tree-level-or-one-loop-for-b -->

- **Gain.** DESI DR1: one-loop B improves equil./ortho. by about 12% and
  26% over tree level, less than simulations suggested, which the authors
  attribute to many poorly constrained one-loop parameters and the small
  k_max [src: arXiv:2512.04266, Sect. 4.2]. BOSS with one-loop B and a
  perturbativity prior reaches 207 ± 292 (equil.) at k_max = 0.23 with
  cosmology fixed [src: arXiv:2201.11518, Sect. 4].
- **Theory bias.** On PT-Challenge simulations (566 h⁻³ Gpc³) the one-loop
  B is unbiased up to k_max ≈ 0.15 h Mpc⁻¹; beyond, f_NL^equil shifts by
  more than 2σ, reaching Δf_NL^equil ≈ 400 at k_max = 0.17; a smaller
  shift at 0.20 "is not a sign of the reduction of the systematic error"
  (Bakx et al. 2025, arXiv:2507.22110, Sect. 5.3) [src]. The DESI DR1
  reanalysis quotes a bias "as large as Δf_NL^equil ≈ 500 for
  k_max ≥ 0.17" from a cited simulation study and chose k_max^B = 0.16
  accordingly [src: arXiv:2512.04266, Sect. 2.3]; which paper that is was
  not read (see "Not verified").
- **Tree level is not bias-free either.** On the same simulations the
  tree-level monopole at k_max^B = 0.08 gives f_NL^equil = 316 ± 67 for a
  true value of 0; the authors judge a 0.5σ theory error tolerable at
  BOSS precision but warn that it may matter once simulation-based priors
  shrink the errors [src: arXiv:2507.22110, Sect. 5.3]. On Nseries (about
  40 times the BOSS volume) the BOSS tree-level pipeline gave
  f_NL^equil = 240 ± 130, f_NL^ortho = −6 +52/−54, read as a theory error
  Δf_NL^equil ≲ 100, less than 0.2σ of BOSS [src: arXiv:2201.07238].

### Conservative or simulation-based priors (equilateral, orthogonal)
<!-- key: conservative-or-simulation-based-priors -->

The simulation-based prior (SBP) is built from 10,500 HOD mocks on
AbacusSummit 500 h⁻¹ Mpc boxes at z = 0.5 with BOSS-like bias (≈ 2) and
n̄ ≤ 3.6 × 10⁻⁴ h³ Mpc⁻³, HOD parameters drawn uniformly (Eq. 2) including
assembly-bias parameters B_cen, B_sat; EFT parameters are measured at field
level (cosmic-variance cancellation) and a normalising flow models their
density [src: arXiv:2402.13310, abstract, Sect. 2.1]. Only b_2 and b_𝒢2
matter for this PNG analysis, so real-space mocks suffice; the mapping is
for BOSS-like galaxies and "will have to be calibrated anew" for other
samples such as DESI ELGs; cosmology is fixed to Planck 2018 in the mocks
[src: Sect. 2.1]. Result on BOSS: bias posterior volume reduced by an
order of magnitude, f_NL^equil = 320 ± 300 and f_NL^ortho = 100 ± 130,
about 40% tighter, "equivalent to doubling the survey volume" [src:
abstract]. In DESI DR1 with one-loop B the SBP gain is marginal; with the
tree-level QSO-all sample about 12% on f_NL^equil, but the central value
moves (670 ± 440 → −100 ± 390) [src: arXiv:2512.04266, Sect. 4.2].

### Fixing or freeing the PNG bias (local)
<!-- key: fixing-or-freeing-the-png-bias-local -->

D'Amico et al.: widening the b^fNL priors by 60% moves BOSS from 52 ± 34
to 64 +30/−60 and raises the error by about 32% with the bispectrum, about
60% with the power spectrum alone; at 150% the posterior becomes a
hyperbola because only b^fNL f_NL is bounded. For equilateral and
orthogonal shapes setting these biases to zero leaves results "practically
unchanged" [src: arXiv:2201.11518, App. A]. Cabass et al.: universality
instead of the simulation fit gives −50 ± 40 instead of −33 ± 28, because
universality underpredicts b_φ by about 30% at b_1 ≈ 2 [src:
arXiv:2204.01781, Sect. 5]. In the power-spectrum-only case a flat prior
b^fNL f_NL > 0.01 was needed because the limit → 0 has infinite prior
volume [src: arXiv:2201.11518, App. A, footnote 16].

### Same data, different pipelines (BOSS)
<!-- key: same-data-different-pipelines-boss -->

Equilateral: 940 ± 600 (tree B, cosmology varied) against 207 ± 292
(one-loop B, cosmology fixed); local: −33 ± 28 against 52 ± 34, a shift
of 2.5 to 3 times either quoted error [der: (52 + 33)/34 ≈ 2.5 and
(52 + 33)/28 ≈ 3.0, ignoring the correlation between two analyses of the
same data] [src: arXiv:2201.07238; arXiv:2204.01781, Eq. 48; arXiv:2201.11518,
Eqs. 51–53]. The analyses differ in loop order, k ranges, PNG bias
relations (b_φ with p = 0.55 against universality) and priors, so the
difference cannot be assigned to one choice from what was read.

The skew-spectrum analysis finds f_NL^equil = −34 +296/−334 and states it
consistent within 1σ with 260 ± 300 and 245 ± 293 of its Refs. [10] and
[12]; it describes [12] as one-loop P_0, P_2 and B_0 with FKP and fixed
Planck cosmology (an error 7.5% different from its own with only a tree
bispectrum) and [10] as window-free P + B_0 in the "aggressive" model
(errors within 5%) [src: arXiv:2401.13036, Sect. 5]. Widening its EFT
priors fivefold gives similar f_NL^equil [src: same].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Theory-error bound from Nseries | Δf_NL^equil ≲ 100 (< 0.2σ BOSS) | BOSS tree B | arXiv:2201.07238 | main text |
| Nseries mean, one-loop B | equil. 162 ± 64, ortho. −32 ± 20, local 3 ± 4 | BOSS one-loop | arXiv:2201.11518 | Eqs. 47–49 |
| Theory-error bounds, one-loop B | ≲ 0.34σ (equil.), 0.16σ (ortho.), 0.12σ (local) of BOSS | BOSS one-loop | arXiv:2201.11518 | Sect. 4 |
| Nseries mean, local P + B | −4.9 ± 5.0 | BOSS tree B | arXiv:2204.01781 | Fig. 2 |
| One-loop B unbiased to | k_max ≈ 0.15 h Mpc⁻¹; Δf_NL^equil ≈ 400 at 0.17 | PT-Challenge | arXiv:2507.22110 | Sect. 5.3 |
| Tree-level B bias | f_NL^equil = 316 ± 67 at k_max^B = 0.08 (truth 0) | PT-Challenge | arXiv:2507.22110 | Sect. 5.3 |
| Perturbativity tolerances | X_P = 1/3, X_B = 1/2 | BOSS one-loop | arXiv:2201.11518 | Sect. 3 |
| Nuisance count | 14 (13 Gaussian bias/counterterms + b_ζ) | BOSS tree B | arXiv:2201.07238 | main text |
| BOSS volume and size | ≈ 1.2 × 10⁶ galaxies, 6 (h⁻¹ Gpc)³, z_eff = 0.38, 0.61 | BOSS DR12 | arXiv:2204.01781 | Sect. 3 |
| Modes used | ≈ 0.5 × 10⁶ to k_max ≈ 0.23 (V_eff ≈ 2.4 h⁻³ Gpc³) | BOSS one-loop | arXiv:2201.11518 | Sect. 4 |
| Patchy mocks | 2048 per chunk | BOSS | arXiv:2201.07238; arXiv:2201.11518 | main text; App. B |
| SBP mocks | 10,500 HOD catalogues, 500 h⁻¹ Mpc boxes, z = 0.5 | BOSS SBP | arXiv:2402.13310 | Sect. 2.1 |
| PNG bias prior (non-local) | b_ψ ~ N(0, 5²); BOSS: b̃_ζ ~ N(1, 5) | DESI DR1; BOSS | arXiv:2512.04266; arXiv:2201.07238 | Sect. 3.3; main text |
| k_NL in the ψ field | 0.45 h Mpc⁻¹ | DESI DR1 | arXiv:2512.04266 | Sect. 3.3 |
| One-loop vs tree B gain | ≈ 12% (equil.), ≈ 26% (ortho.) | DESI DR1 | arXiv:2512.04266 | Sect. 4.2 |
| Bispectrum gain, local | ≈ 20% (BOSS, sim. b_φ), ≈ 30% (universality), ≈ 15% (DESI QSO-all) | BOSS; DESI DR1 | arXiv:2204.01781; arXiv:2512.04266 | Sect. 5; Sect. 4.1 |
| DESI DR1 galaxies only, local | 6 ± 13 (LRG alone 6 +14/−13; collaboration 2 +15/−14 for p = 0.55) | DESI DR1 reanalysis | arXiv:2512.04266 | Sect. 4.1 |
| DESI DR1 P only, local | −3.6 +9.0/−9.1 (QSO merger model); 3.5 +10.7/−7.4 (universality) | DESI DR1 LRG + QSO | arXiv:2411.17623 | abstract |
| DESI DR1 with TNG prior on p | p̄ ≃ 1.4; f_NL = −3.3 ± 9.2 | DESI DR1 QSO | arXiv:2602.12357 | abstract |
| BOSS P only, b_φ relation spread | 16 ± 16 to 230 ± 226 | BOSS DR12 | arXiv:2205.05673 | abstract |
| eBOSS QSO, local | −51 < f_NL < 21 (95%, DR14); −12 ± 21 (DR16) | eBOSS | arXiv:1904.08859; arXiv:2106.13725 | abstracts |
| Skew-spectra BOSS, equil. | −34 +296/−334 (cosmology fixed) | BOSS DR12 | arXiv:2401.13036 | Sect. 5, Eq. 5.1 |
| Skew-spectra Nseries bias | 0.53σ (equil.), 4.15σ (ortho.) of BOSS | Nseries | arXiv:2401.13036 | Sect. 5, Table 2 |
| Field level vs P + B (sims) | σ(f_NL^local) ~1.3 times smaller, k_max ≈ 0.1 | Quijote, BORG | arXiv:2603.20855 | abstract |
| HEFT b_φ prior | b_φ uncertainty −80% (galaxy samples) | AbacusSummit | arXiv:2501.14873 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **k_max beyond the model.** Shows up as f_NL^equil drifting with k_max,
  possibly non-monotonically. Test: k_max scan on simulations whose volume
  far exceeds the survey's, with the covariance of that volume [src:
  arXiv:2507.22110, Sect. 5.3; arXiv:2201.11518, Sect. 4].
- **Theory error hidden by wide priors, exposed by tight ones.** A tree-level
  bias acceptable at BOSS precision may not be once simulation-based priors
  are applied [src: arXiv:2507.22110, Sect. 5.3]. Test: rerun the
  simulation validation with the informative priors switched on.
- **Prior mapping outside its calibration.** SBPs are calibrated for one
  galaxy type, one redshift and one cosmology [src: arXiv:2402.13310,
  Sect. 2.1]. Local PNG has the same issue for b_φ: wide priors are not a
  safe fallback, since they bias f_NL through projection [src:
  arXiv:2205.05673]; simulation priors on p are calibrated on one
  hydrodynamical model (TNG, checked against CAMELS) [src:
  arXiv:2602.12357]. Test: compare conservative and SBP results; a large shift of
  the central value, as in DESI QSO-all (670 → −100), deserves a reason
  [src: arXiv:2512.04266, Sect. 4.2].
- **Local f_NL with b_φ fixed.** Results move with the assumed relation
  (BOSS: −33 ± 28 against −50 ± 40 [src: arXiv:2204.01781, Sect. 5]; power
  spectrum alone, an order of magnitude in σ [src: arXiv:2205.05673]). Test:
  report the result for a second relation, or fit b_φ f_NL and b_δφ f_NL
  directly, as Cabass et al. do in their Sect. 6 [src: Sect. 2.6].
- **Large-scale systematics in the first k bin.** Test: raise k_min and
  compare; BOSS analyses cut at 0.01 h Mpc⁻¹ for that reason [src:
  arXiv:2204.01781, Sect. 3]. The DESI DR1 reanalysis added BGS and ELG2
  after comparing weighted and unweighted spectra and the low-k power
  spectrum, and gives an LRG-only result as a test [src:
  arXiv:2512.04266, Sect. 2.1].
  The power-spectrum analyses test several contamination-removal methods
  on EZ mocks, among them a neural-network cleaning (eBOSS DR16,
  arXiv:2106.13725), and add an angular integral constraint to the window
  for the photometric dependence of target selection, validated blind
  (DESI DR1, arXiv:2411.17623) [src].
- **Approximate window convolution.** A few-percent window error was
  enough for a 4.15σ orthogonal bias in the skew-spectrum analysis [src:
  arXiv:2401.13036, Sect. 5]. Test: the Nseries fit at full volume.
- **Template mismatch with the CMB.** The physical orthogonal template
  differs from Planck's in the squeezed limit [src: arXiv:2201.07238,
  footnote 2]. Test: state the template before combining with Planck.
- **Unknown data systematics.** D'Amico et al. warn that their analyses
  assume the public BOSS catalogues are free of unknown systematics and
  undetected foregrounds [src: arXiv:2201.11518, Sect. 4].
- **Goodness of fit.** D'Amico et al. report a p-value of about 4% for
  their best fit [src: arXiv:2201.11518, Sect. 4]; quote it with the
  result.

## Reading list
<!-- key: reading-list -->

- Review: Achúcarro et al. 2022, arXiv:2203.08128, Sect. 3.2.2 — where the
  bispectrum and map-level methods stand among PNG probes.
- Method: Philcox 2021, arXiv:2107.06287 — window-free cubic bispectrum
  estimator.
- Application: Cabass et al. 2022a, arXiv:2201.07238 — equilateral and
  orthogonal model (Eqs. 8–12), power counting, PNG bias prior, Nseries
  test.
- Application: Cabass et al. 2022b, arXiv:2204.01781 — local PNG terms in
  the bispectrum (Eq. 34), b_φ and b_δφ choices, k_min test.
- Application: D'Amico et al. 2022, arXiv:2201.11518 — one-loop B,
  perturbativity prior, theory-error rule (Eq. 50), PNG bias widening test.
- Method: Ivanov et al. 2024, arXiv:2402.13310 — simulation-based priors
  from HOD mocks and normalising flows.
- Application: Chudaykin, Ivanov and Philcox 2025, arXiv:2512.04266 —
  DESI DR1 P + B, PolyBin3D, per-sample p, tree vs one-loop gain.
- Critique: Bakx et al. 2025, arXiv:2507.22110 — where the one-loop and
  tree-level bispectrum bias f_NL^equil.
- Application (other groups): Chen, Chakraborty & Dvorkin 2024,
  arXiv:2401.13036 — weighted skew-spectra on BOSS, Nseries bias.
  Chaussidon et al. 2024, arXiv:2411.17623; Mueller et al. 2021,
  arXiv:2106.13725; Castorina et al. 2019, arXiv:1904.08859 — DESI and
  eBOSS scale-dependent bias, redshift weights.
- Critique: Barreira 2022, arXiv:2205.05673 — b_φ uncertainty on BOSS.
  Priors: Fondi et al. 2026, arXiv:2602.12357; Hadzhiyska & Ferraro 2025,
  arXiv:2501.14873.
- Method: Scoccimarro 2015, arXiv:1506.02729 (FFT bispectrum multipoles);
  Brown et al. 2024, arXiv:2403.18789 (2PCF + 3PCF).
- Simulation studies: Coulton et al. 2022, arXiv:2206.15450; Jung et al.
  2022, arXiv:2211.07565 and 2024, arXiv:2403.00490 (Quijote-PNG);
  Cagliari et al. 2025, arXiv:2510.12715; Andrews et al. 2026,
  arXiv:2603.20855 (BORG field level).

## Not verified
<!-- key: not-verified -->

- The simulation study cited by arXiv:2512.04266 for Δf_NL^equil ≈ 500 at
  k_max ≥ 0.17 h Mpc⁻¹ (its reference list was not readable); the PT-
  Challenge value read here is ≈ 400 at 0.17 (arXiv:2507.22110).
- Cabass et al. 2022b, Sect. 6 (direct fits of b_φ f_NL and b_δφ f_NL): not
  read beyond its announcement.
- The full PNG-bias prior table and the result tables of arXiv:2512.04266
  (Table 1) and the Gaussian-nuisance priors of arXiv:2201.07238.
- Map-level (field-level) inference of PNG on data: no analysis read here;
  see `cosmo-beyond-two-point`.
- The cosmological-collider BOSS analysis (Cabass et al. 2024): title
  seen in a search, not read.
- The reference list of arXiv:2401.13036: which papers its Refs. [10] and
  [12] are, and why its 245 ± 293 for [12] differs from the 207 ± 292 read
  in arXiv:2201.11518.
