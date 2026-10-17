# Full-shape modelling — cosmo-galaxy-clustering dossier

Scope: how a full-shape result is produced from pre-reconstruction
multipoles (one-loop EFT model, bias basis, counterterm and stochastic
priors, marginalisation, combination with post-reconstruction BAO), and how
to choose between full modelling, standard compression and ShapeFit, and
between EFT codes and prior conventions.
Snapshot: 2026-10-16.
From: Ivanov 2022 review (arXiv:2212.08488), Sects. 4–6; DESI DR1
full-shape key paper (arXiv:2411.12021).

Already in L2, not repeated here: the DESI DR1 baseline (code, bias basis,
prior table, k range, emulator, covariance) in
`physics-and-methods.md#theory-models-in-current-analyses`; the community
split on priors, Bayesian versus frequentist and informative priors in the
same section; prior-volume and prior-weight effects with their sizes in
`systematics.md#prior-volume-projection-effects`; the full-shape systematic
budget in `systematics.md#two-budgets-to-keep-apart`; σ8 history in
`open-questions.md#the-amplitude-from-full-shape-was-sigma8-ever`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose what is fitted
<!-- key: step-1-choose-what-is-fitted -->

DESI DR1 distinguishes three routes [src: arXiv:2411.12021, Sect. 4.2]:

| Route | Free parameters of the fit | Cosmology enters |
|---|---|---|
| Standard compression (BOSS, eBOSS) | α_∥, α_⊥ (Eqs. 6–7), fσ8, with a fixed linear template | in a second step, through the compressed values |
| ShapeFit | α_∥, α_⊥, fσ_s8, slope m (and n) | in a second step |
| Full modelling | cosmological parameters; the linear P(k) is recomputed by a Boltzmann code at each step | directly |

In full modelling the catalogue cosmology stays fixed and the AP distortion
is applied to the model with q_∥ = D_H/D_H^fid and q_⊥ = D_M/D_M^fid
(arXiv:2411.12021, Eqs. 2–5); q_∥ and q_⊥ are derived quantities, not
parameters as in the compressions [src: Sect. 4.2.1]. In the compressions
the α's are sometimes applied to the whole template rather than the BAO part
only, because r_d^fid/r_d shifts are small next to D/D^fid shifts at
current precision [src: Sect. 4.2.2].

### Step 2. Build the one-loop model
<!-- key: step-2-build-the-one-loop-model -->

The common structure, as written for the East-coast BOSS analysis, is
P_g,ℓ = P^tree + P^1-loop + P^noise + P^ctr (Ivanov et al. 2020,
arXiv:1909.05277, Eq. 3.1), with the Kaiser tree level (Eq. 3.3) and the
bias expansion δ_g = b_1 δ + (b_2/2) δ² + b_G2 G_2 (Eq. 3.4); b_Γ3 was
fixed to zero because BOSS could not break its degeneracy with other
nuisance parameters [src: Sect. 3.1]. The same paper added a
next-to-leading-order redshift-space counterterm to absorb short-scale
velocity effects instead of a phenomenological fingers-of-God factor [src:
Sect. 3.1].

The four DESI DR1 pipelines differ as follows [src: arXiv:2411.12021,
Sects. 4.3.1–4.3.4]:

| Code | Theory | Bias | Extra terms |
|---|---|---|---|
| velocileptors LPT | one-loop Lagrangian PT, long displacements resummed below k_IR | b_1, b_2, b_s, b_3 (Lagrangian) | 3 counterterms, 3 stochastic |
| velocileptors EPT | Eulerian PT, wiggle/no-wiggle IR resummation; Eulerian biases sampled as reparametrisations of Lagrangian ones so priors centre on zero Lagrangian bias | McDonald–Roy basis | same |
| FOLPSν | one-loop EPT with massive-neutrino kernels; JAX version about 10 times faster | McDonald–Roy or Assassi et al. basis | counterterms, stochastic terms |
| PyBird | one-loop EPT | b_1–b_4 of Perko et al., East- or West-coast parametrisation | 3 counterterms, 3 stochastic |
| EFT-GSM | Gaussian streaming in configuration space, LPT-based | b_1, b_2, b_s² | 2 counterterms; not the full set of non-linearities |

Before IR resummation PyBird, FOLPSν and velocileptors are essentially
equivalent; the resummation schemes differ at two-loop order [src:
Sect. 4.3.3]. Further differences [src: Maus et al. 2024,
arXiv:2404.07272, Sect. 3.6]: LPT counterterms multiply k²P_Zel, the others
k²P_lin (a two-loop difference); PyBird has an extra isotropic stochastic
term ∝ k²/k_M².

### Step 3. Set the nuisance priors
<!-- key: step-3-set-the-nuisance-priors -->

DESI ties counterterm prior widths to the linear signal: the 1σ
counterterm contribution may be a fraction X of P_lin at k_max, giving
|α_0|, |α_2| ≤ X/k²_max (arXiv:2411.12021, App. E, Eqs. 46–48), hence
α_0,2 width 12.5 h⁻² Mpc² for X = 0.5 and k_max = 0.20 (Eq. 49) [src].
The two BOSS-era conventions, as compared by Simon et al. 2023
(arXiv:2208.05929, Sect. II.1) [src]:

| | West coast (PyBird) | East coast (CLASS-PT) |
|---|---|---|
| Rationale | region physically allowed by the EFT | coevolution model and simulations |
| b_1 | flat [0, 4] | b̃_1 flat [0, 4] |
| Non-linear bias | c_2 = (b_2 + b_4)/√2 flat [−4, 4]; b_3 ~ N(0, 2); c_4 = 0 | b̃_2, b_G2 ~ N(0, 1); b_Γ3 ~ N(23/42 (b_1 − 1), 1) |
| Counterterms | c_ct, 2c_r,1 ~ N(0, 2), with k_M = 0.7, k_R = 0.35 h Mpc⁻¹ | c_0 ~ N(0, 30), c_2 ~ N(30, 30), c_4 ~ N(0, 30) [h⁻² Mpc²]; c̃ ~ N(500, 500) h⁻⁴ Mpc⁴ |
| Stochastic | c_e,0, c_e,2 ~ N(0, 2); c_e,1 = 0 | c_e,0,1,2 ~ N(0, 2) |
| EFT parameters per sky cut (ℓ = 0, 2) | 9 | 11 |

The bases map by b_2 = b̃_1 + (7/2) b_G2, b_3 = b̃_1 + 15 b_G2 + 6 b_Γ3,
b_4 = b̃_2/2 − (7/2) b_G2 (arXiv:2208.05929, Eq. 1).

### Step 4. Marginalise the linear nuisance parameters
<!-- key: step-4-marginalise-the-linear-nuisance -->

Parameters that enter the model linearly are marginalised analytically:
log L = ½ F_1,i F⁻¹_2,ij F_1,j + F_0 − ½ ln|det F_2|, with F_2 built from
the derivatives of the windowed model with respect to those parameters
(PyBird form, Lai et al. 2024, arXiv:2404.07283, Eqs. 16–18, following
D'Amico et al. 2020). In PyBird all nuisance parameters except b_1, b_2 and
b_4 are marginalised this way, and the analytic and full likelihoods give
the same cosmology on the mean of the LRG mocks [src: Sect. 3.1.1]. The
inverse covariance in that expression already carries the Hartlap and
Percival factors [src: same].

### Step 5. For compressions, interpret
<!-- key: step-5-for-compressions-interpret -->

ShapeFit's cosmological step treats the compressed posterior as Gaussian:
log L = −½ (q − q_mean) C⁻¹ (q − q_mean)ᵀ (arXiv:2404.07283, Eq. 24). For
each proposed cosmology, r_d, D_M, H and the no-wiggle transfer function
are computed, and m = d/dln k [(T^NW)²/(s³ (T^NW,fid)²)] at k_p (Eq. 25),
with s = r_d/r_d^ref [src: Sect. 3.3]. The original paper defines the
amplitude through A_sp = s⁻³ P^lin_no-wiggle(k_p/s) (Brieden et al. 2021,
arXiv:2106.07641, Eq. 31) and recommends f A_sp^{1/2} over fσ_s8 for
inference (Eq. 32); n maps to n_s − n_s^ref (Eq. 33); m is computed with
n_s held at the reference value so that n_s moves n only (Eq. 34) [src:
Sect. 3.4]. Replacing the Gaussian by an interpolated chain posterior gave
consistent constraints in PyBird tests [src: arXiv:2404.07283, Sect. 3.3].

### Step 6. Add post-reconstruction BAO
<!-- key: step-6-add-post-reconstruction-bao -->

Three ways exist [src: arXiv:2411.12021, Sect. 4.4]:

1. Summary-statistic level: pre-reconstruction P_ℓ with
   post-reconstruction ξ_ℓ and their joint covariance (Chen et al. 2022,
   BOSS).
2. Pre-reconstruction P_ℓ bins plus the post-reconstruction α's
   (Philcox & Ivanov 2022, BOSS).
3. Compressed with compressed: ShapeFit parameters plus α's.

A comparison on eBOSS LRG found 5–10% differences in error bars between the
three, as cited there [src]. DESI DR1 uses option 2 for full modelling and
option 3 for ShapeFit [src]. For DR1 full shape with DR2 BAO, Forero-Sánchez
et al. 2026 (arXiv:2602.18761) use option 3 because the DR2 × DR1
cross-covariance then has only 8 coefficients, estimable from 100 EZmocks;
the full-modelling equivalent needs N_BAO × N_P(k) terms and at least ten
times more realisations [src: Sect. 3.4]. Their adopted covariance takes
the diagonal blocks from the data posteriors and only the cross block from
mocks, rescaled by the data variances (Eqs. 16–17) [src].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Full modelling or ShapeFit
<!-- key: full-modelling-or-shapefit -->

- **Same data, same code.** PyBird on DESI-like mocks: best-fit shifts of
  about 0.5σ (ΛCDM), ≤ 0.7σ (wCDM) and ≤ 0.5σ (oCDM) between the two,
  "small compared to the statistical error", origin not identified [src:
  arXiv:2404.07283, Sect. 8].
- **What ShapeFit gives.** Model-independent compressed variables that
  separate early- from late-time information, full-modelling constraining
  power once interpreted, and about 30 times faster inference [src:
  arXiv:2106.07641, Sect. 7]. With modern emulators speed is secondary; the
  argument made in 2026 is that the compressed space regularises the fit
  and removes the prior-volume effects that dominate DESI-only full
  modelling [src: arXiv:2602.18761, Sect. 3.2].
- **What it misses.** Information in the BAO amplitude, left out on purpose
  because it is processed by late-time effects and matters only without a
  CMB or BBN ω_b prior [src: arXiv:2106.07641, Sect. 7]. Without a BBN prior,
  ShapeFit constrains only r_d h from BAO and h weakens; full modelling gets
  a weak ω_b from the wiggle amplitude [src: arXiv:2404.07283, Sect. 3.3].
- **Two readings of the same DESI DR1 posteriors.** The DR1 key paper
  rejects ShapeFit for its cosmological inference because projection
  effects offset the derived cosmology, mainly through α_AP and m in the
  weaker bins, and because of residual template dependence [src:
  arXiv:2411.12021, Sect. 5]. The 2026 DR1 FS + DR2 BAO paper finds the
  ShapeFit posteriors close to Gaussian, approximate and true MAP
  coinciding, and w0waCDM results unchanged between MAP and mean [src:
  arXiv:2602.18761, App. A]. A reader should report which centre (MAP or
  mean) of the compressed posterior entered the second step.
- **Template versus direct in BOSS.** With the same LPT model and priors,
  the template fit gives higher fσ8 for two reasons: the AP warping ε is
  free in the template fit but tied to Ω_m (and so to the shape) in ΛCDM,
  and nuisance parameters degenerate with shape parameters produce a
  prior-volume offset [src: Maus et al. 2023, arXiv:2302.07430, Sect. 5].
  With tight priors on the other ΛCDM parameters and on (α̃, ε) the two
  become identical [src].

### Bias parametrisation
<!-- key: bias-parametrisation -->

- **Minimal against maximal freedom.** Maximal: all four biases free with
  wide priors. Minimal ("coevolution"): b_s^L = b_3^L = 0, which in the EPT
  bases means b_2^E = b_2^L + (8/21) b_1^L, b_s^E = −(2/7)(b_1^E − 1),
  b_3^E = b_1^E − 1 (velocileptors; arXiv:2404.07272, Eq. 15) or
  b_s² = −(4/7)(b_1^E − 1), b_3nl = (32/315)(b_1^E − 1) (FOLPSν; Eq. 16)
  [src: Sect. 3.5]. Cosmology agrees between codes in both cases [src:
  Sect. 6].
- **Cost of coevolution.** Assuming b_s co-evolves with b_1 adds
  information on A_s and ω_cdm (full modelling) or on fσ_s8 and m
  (ShapeFit); DESI DR1 therefore kept b_s free and fixed b_3 = 0, since b_3
  is degenerate with the counterterms and barely moves ΛCDM posteriors
  [src: arXiv:2411.12021, Sect. 4.7].
- **b_3 and m.** In PyBird, a free b_3 is degenerate with m and produces a
  tail in the QSO m posterior; a Gaussian b_3 prior removes it without bias
  [src: arXiv:2404.07272, Sect. 6]. Fixing b_2 and b_3 by the local
  Lagrangian relation ("BOSS MinF") tightens m and slightly reduces
  systematic error [src: arXiv:2404.07283, Sects. 5.3, 8].
- **Bias scaled by σ8.** DESI samples (1 + b_1)σ8, b_2σ8², b_sσ8² because
  this matches the signal better and reduces volume effects [src:
  arXiv:2411.12021, Sect. 4.7].

### West-coast or East-coast priors
<!-- key: west-coast-or-east-coast-priors -->

On BOSS, prior-volume effects move the posterior mean from the MAP by up to
about 1σ (West coast) and 2σ (East coast); the prior weight moves the MAP
between the two by ≲ 1σ, with min χ² differing by Δχ² ≈ 9. Doubling the
prior ranges brings the MAPs to ≲ 0.4σ and Δχ² = 0.4, but raises the
projection effect by up to about 33%. With one common prescription the two
pipelines agree to better than 0.2σ [src: arXiv:2208.05929, Sect. VI].
Remedies listed there: profile likelihoods, larger data volume, adding the
CMB [src].

### Code and IR resummation
<!-- key: code-and-ir-resummation -->

velocileptors, FOLPSν and PyBird agree up to k_max ≈ 0.25 h Mpc⁻¹ at the
precision of 8 (h⁻¹ Gpc)³ boxes; on noiseless data generated by one model
and fitted by another, significant deviations appear only at k_max ≳ 0.26,
attributed to the limits of one-loop theory rather than to the codes [src:
arXiv:2404.07272, Sect. 6]. For scale: DESI bin volumes are about 2, 3, 5
(BGS, LRG1, LRG2), 10, 20 and 60 (h⁻¹ Gpc)³ for the larger bins; the bins
overlap, so they do not add up to the ~70 (h⁻¹ Gpc)³ quoted as the total
volume to z = 2.1 [src: same]. Differences among codes in DR1 parameters of interest
were below 0.1% [src: arXiv:2411.12021, Sect. 5.1]. The choice of k_IR in
velocileptors matters only at unphysical volumes (200 h⁻³ Gpc³) [src:
arXiv:2404.07272, Sect. 3.6].

### Scale cut and multipoles
<!-- key: scale-cut-and-multipoles -->

| Analysis | k_max [h Mpc⁻¹] | Multipoles | How validated | Place read |
|---|---|---|---|---|
| BOSS, East coast | 0.25 | 0, 2 | mocks; residual model error plus projection ≤ 1σ per 1D marginal | arXiv:1909.05277, Sects. 2, 3.2 |
| BOSS, West coast | 0.23 | 0, 2 | theory error σ_sys from the distance of the truth to the 68% region on Challenge boxes about 16 times the BOSS volume | arXiv:1909.05271, Sects. 3.5, 4.1–4.2 |
| PyBird DESI tests | 0.20 | 0, 2 (4 optional) | single-box covariance ≈ DESI Y5 volume; beyond 0.20 little gain, slightly more bias | arXiv:2404.07283, Sect. 8 |
| DESI DR1 baseline | 0.20 | 0, 2 | see L2 | arXiv:2411.12021 |

The hexadecapole does not help ΛCDM but notably improves wCDM and oCDM and
reduces systematic bias in the PyBird tests, which recommend it for
extended models [src: arXiv:2404.07283, Sect. 8]; DESI DR1 dropped it for
prior-weight reasons (see L2). The West-coast analysis set c_4 and the
monopole stochastic term to zero and c_r,2 = 0 when the hexadecapole is not
fitted [src: arXiv:1909.05271, Sect. 3.5].

### Measurement choices, same data
<!-- key: measurement-choices-same-data -->

On BOSS, with the model fixed [src: arXiv:2208.05929, Sects. IV.3, VI]:
FKP against quadratic power-spectrum estimator up to 0.6σ on all
cosmological parameters; Fourier against configuration space 0.3–0.5σ on
σ8, S8, n_s; LOWZ/CMASS against z1/z3 split ≲ 0.3σ; the two public
post-reconstruction BAO measurements in Fourier space 0.9σ on h; integral
constraints and shot-noise subtraction ≲ 0.2σ.

### De-wiggling for m
<!-- key: de-wiggling-for-m -->

Different de-wiggling methods differ by 1–2% in the smooth spectrum, and
the derivative amplifies this to differences of up to 50% in m; this does
not bias cosmology as long as data and theory pipelines compute m the same
way [src: Ghaemi et al. 2025, arXiv:2504.10578, Sect. 5]. Recommended
systematic: σ_m,syst = 0.023|m| + 0.001 (conservative; Eq. 9), or
0.011|m| + 0.001 with the procedure of their Sect. 3.4; models that change
the baryonic suppression, such as early dark energy, need extra care [src].
Lai et al. found three de-wiggling algorithms consistent in ΛCDM, wCDM and
oCDM [src: arXiv:2404.07283, Sect. 3.3].

### n_s and ω_b
<!-- key: ns-and-omegab -->

The East-coast BOSS baseline fixed n_s = 0.9649 because BOSS cannot measure
it, and kept a neutrino mass free in (0.06, 0.18) eV because it is
degenerate with the amplitude [src: arXiv:1909.05277, Sect. 3.3]. The
West-coast BOSS analysis fixed Ω_b/Ω_c and n_s to Planck [src:
arXiv:1909.05271, Sect. 4.2]. DESI DR1 put a Gaussian prior on n_s (see L2).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Counterterm prior rule | 1σ term = X P_lin at k_max; X = 0.5 → 12.5 h⁻² Mpc² | DESI DR1 | arXiv:2411.12021 | App. E, Eq. 49 |
| FM vs ShapeFit best-fit shift | ≈ 0.5σ ΛCDM, ≤ 0.7σ wCDM, ≤ 0.5σ oCDM | PyBird, DESI mocks | arXiv:2404.07283 | Sect. 8 |
| Inter-code agreement | to k_max ≈ 0.25 at 8 (h⁻¹ Gpc)³; deviations at ≳ 0.26 | velocileptors, FOLPSν, PyBird | arXiv:2404.07272 | Sect. 6 |
| WC vs EC MAP shift | ≲ 1σ, Δχ² ≈ 9; ≲ 0.4σ, Δχ² = 0.4 with doubled priors | BOSS | arXiv:2208.05929 | Sect. VI |
| Same-prescription agreement | < 0.2σ | BOSS | arXiv:2208.05929 | Sect. VI |
| EFT parameters per sky cut | 9 (WC), 11 (EC) for ℓ = 0, 2 | BOSS | arXiv:2208.05929 | Sect. II.1 |
| ShapeFit pivot and shape | k_p ≈ 0.03 h Mpc⁻¹, a = 0.6 | DESI | arXiv:2602.18761 | Eq. 8 |
| ShapeFit cross-covariance | 8 coefficients from 100 EZmocks | DESI DR1 FS × DR2 BAO | arXiv:2602.18761 | Sect. 3.4 |
| Pre/post-recon combination methods | 5–10% difference in error bars (as cited) | eBOSS LRG | arXiv:2411.12021 | Sect. 4.4 |
| σ_m,syst | 0.023|m| + 0.001 | ShapeFit | arXiv:2504.10578 | Eq. 9 |
| m spread across de-wiggling | up to 50%; 1.1% or 2.3% with matched or filtered derivative | ShapeFit | arXiv:2504.10578 | Sect. 5 |
| ShapeFit speed | ≈ 30 times faster than FM (pre-emulator) | BOSS | arXiv:2106.07641 | Sect. 7 |
| BOSS EC k_max | 0.25 h Mpc⁻¹, 50 k-bins per multipole, Δk = 0.005 | BOSS DR12 | arXiv:1909.05277 | Sect. 3.2 |
| BOSS WC loop fraction | one-loop ≈ 15% of monopole at k = 0.23 (Challenge A) | BOSS mocks | arXiv:1909.05271 | Sect. 4.1 |
| FOLPSν JAX speed-up | ≈ 10 | DESI | arXiv:2411.12021 | Sect. 4.3.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Prior pull read as a measurement.** Test: compare MAP and mean, rerun
  with doubled prior widths, and fit noiseless synthetic data with the data
  covariance (`systematics.md#prior-volume-projection-effects`; Simon et al.
  for the doubling test, arXiv:2208.05929, Sect. VI).
- **Compressed posterior non-Gaussian in weak bins.** Shows up as offsets in
  α_AP and m after interpretation [src: arXiv:2411.12021, Sect. 5]. Test:
  interpolated-posterior likelihood against the Gaussian approximation, as
  in arXiv:2404.07283, Sect. 3.3.
- **Inconsistent m pipelines.** Data and theory computing m with different
  de-wiggling or derivatives; up to 50% in m [src: arXiv:2504.10578,
  Sect. 5]. Test: null tests where m ≈ 0 is expected (their Sect. 4.1).
- **Free b_3 with ShapeFit.** Tail in m for QSO [src: arXiv:2404.07272,
  Sect. 6]. Test: run with a Gaussian b_3 prior.
- **Bias conventions mixed across codes.** One code's basis cannot always be
  mapped to another's by a transformation of parameters, so equal-looking
  priors are not equal [src: arXiv:2404.07272, Sect. 3.5]. Test: compare in
  minimal and maximal freedom.
- **k_max beyond one loop.** Codes diverge above ≈ 0.26 h Mpc⁻¹ at large
  volume [src: arXiv:2404.07272, Sect. 6]. Test: k_max scan on mocks with a
  covariance of the full survey volume, not a single box only.
- **Validation on large volumes only.** Prior effects were found late in
  BOSS because pipelines were validated on large simulations; one-sky
  synthetic data with the BOSS covariance show them [src: arXiv:2208.05929,
  Sect. VI].
- **Measurement version.** Two public BOSS post-reconstruction BAO
  measurements differ by 0.9σ on h; the authors warn against using them
  until clarified [src: arXiv:2208.05929, Sect. VI].
- **Template cosmology far from truth.** Residual template dependence of
  ShapeFit, mitigated by iterating on reference cosmologies not disfavoured
  by the data [src: arXiv:2411.12021, Sect. 5].

## Reading list
<!-- key: reading-list -->

- Review: Ivanov 2022, arXiv:2212.08488 — EFT of LSS, IR resummation, bias
  and RSD in the EFT.
- Foundation/method: Brieden et al. 2021, arXiv:2106.07641 — ShapeFit
  definitions and interpretation recipe.
- Application: Ivanov et al. 2020, arXiv:1909.05277 — East-coast model,
  parameters and priors for BOSS.
- Application: D'Amico et al. 2020, arXiv:1909.05271 — West-coast analysis,
  theory-systematic procedure.
- Application: Adame et al. 2024, arXiv:2411.12021 — DESI DR1 routes, codes,
  counterterm priors, FS+BAO combination.
- Method: Maus et al. 2024, arXiv:2404.07272 — three EFT codes compared,
  minimal and maximal freedom.
- Method: Lai et al. 2024, arXiv:2404.07283 — ShapeFit against full
  modelling with PyBird; analytic marginalisation; k_max and hexadecapole.
- Application: Forero-Sánchez et al. 2026, arXiv:2602.18761 — ShapeFit with
  DR2 BAO; compressed cross-covariance.
- Critique: Simon et al. 2023, arXiv:2208.05929 — prior conventions and
  measurement choices on BOSS.
- Critique: Maus et al. 2023, arXiv:2302.07430 — why template fits gave
  higher fσ8 in BOSS.
- Critique: Ghaemi et al. 2025, arXiv:2504.10578 — de-wiggling systematics
  of m.

## Not verified
<!-- key: not-verified -->

- The eBOSS comparison of combination methods (Gil-Marín 2022), the PyBird
  DESI implementation (Lai et al. 2025), velocileptors DESI tests (Maus et
  al. 2025a) and EFT-GSM (Ramirez-Solano et al. 2025): named in
  arXiv:2411.12021, not read; no identifier recorded.
- Chen et al. 2022 and Philcox & Ivanov 2022 combination methods: cited
  through arXiv:2411.12021, Sect. 4.4, bodies not read here.
- The theory-systematic values σ_sys per parameter in arXiv:1909.05271
  (Fig. 7, not readable as text).
