# B-mode power-spectrum likelihood for r — cosmo-inflation-primordial dossier

Scope: how a ground-based analysis turns Q/U maps into a likelihood for r
— E/B separation on a filtered patch, transfer functions and bandpower
window functions, noise debiasing, the simulation sets and the
conditioning of the bandpower covariance, the Hamimeche–Lewis likelihood
on many auto- and cross-spectra, null tests with their pass criteria and
the validation of the final limit — with the reasons the BICEP/Keck and
SPT-3G papers give for each choice.
Snapshot: 2026-10-19.
From: Achúcarro et al. 2022 review (arXiv:2203.08128), Sect. 2.2.1
(observational progress); SO science goals (arXiv:1808.07445), Sects.
III.2–III.4; BICEP/Keck BK18 (arXiv:2110.00483).

Already in L2 or in other dossiers, not repeated here: the BK18 parameter
list, priors and foreground budget
(`systematics.md#b9-bk18-budget-as-read-in-the-paper-body`), the SPT-3G
foreground model and dust fits
(`systematics.md#b10-spt-3g-2019-2020-bb-budget-as-read`), the 66-spectrum,
nine-bandpower, 499-simulation summary and the χ² = 541.6 goodness of fit
(`physics-and-methods.md#bicep-keck-style-likelihood`), Bayesian against
Feldman–Cousins limits (`physics-and-methods.md#quoting-a-limit`). The SO
pseudo-C_ℓ set-up (NaMaster purification, cross-split debiasing, Gaussian
against Hamimeche–Lewis likelihood at f_sky ≈ 10%) and the foreground
pipelines are in `deep/bmode-foreground-separation.md`; the lensing
template as an extra spectral channel is in `deep/delensing.md`; low-ℓ
satellite-style likelihoods for τ are the `cosmo-cmb` dossier
`deep/low-ell-polarisation-tau.md`.

## How it is done
<!-- key: how-it-is-done -->

Notation: Q, U the Stokes maps; E, B the curl-free and curl components;
C_ℓ^XY a power spectrum, D_ℓ = ℓ(ℓ+1)C_ℓ/2π; a bandpower is a weighted
average of C_ℓ over a multipole bin b; "sign-flip" noise realisations are
data coadds in which subsets enter with random signs so that the sky
cancels; PTE is the probability to exceed.

### Step 1. Separate E and B on the observed patch
<!-- key: step-1-separate-e-and-b-on-the-observed-patch -->

On a partial, filtered sky some modes are both E and B ("ambiguous");
because E is far brighter, their leakage dominates B unless removed.
BICEP/Keck removes them with a purification matrix built from its own
observation matrix (Keck Array and BICEP2 Collaborations 2016,
arXiv:1603.05976):

- A pure B mode b satisfies P^E · b = 0 for all observed E modes (Eq. 11).
  With signal covariances C_E and C_B of the [Q, U] pixels for chosen
  spectra (Eqs. 13–14), approximately pure B modes are the eigenvectors of
  the generalised problem C_B x = λ C_E x with the largest λ, pure E those
  with the smallest (Eq. 15) [src: Sect. III].
- Every linear step of the pipeline (pointing, polynomial filter,
  scan-synchronous subtraction, deprojection of beam systematics,
  apodisation) is encoded in an observation matrix R, and the problem is
  solved for C̃ = Rᵀ C R (Eqs. 16–19) [src: Sects. III, IV].
- Regularisation: σ²I is added to both sides (Eq. 72), with σ² equal to
  1/100 of the mean diagonal of C̃_E and C̃_B; input spectra are a steeply
  red 1/ℓ² for E-only and B-only, so that eigenvalue maps onto multipole;
  the largest quarter of eigenmodes spans pure B (the smallest quarter pure
  E), "adequate for preserving power up to ℓ ∼ 700"; the projector
  Π_B = Σ b_i b_iᵀ is applied to each map (Eqs. 73–74). The 1/ℓ² choice and
  the quarter cut are described as arbitrary [src: Sect. VI.1].
- Stated reason: partial coverage, timestream filtering including
  deprojection, and the map projection plus Fourier estimator all leak E
  into B; without purification "the sample variance of E/B leakage in the
  BICEP2 BB power spectrum is comparable to the uncertainty due to
  instrumental noise" [src: Sect. VII.1].

BK18 applies this matrix purification to each frequency map, then
inverse-noise-variance apodises, Fourier transforms and rotates Q/U to E/B
[src: arXiv:2110.00483, main text, "Maps and Power Spectra"]. SPT-3G uses
NaMaster pure-B maps and spectra instead [src: arXiv:2505.02827, Sect. V].

### Step 2. Measure the response: transfer function and window functions
<!-- key: step-2-measure-the-response-transfer-function -->

BICEP/Keck: delta-function input maps in ℓ are passed through R and the
full spectrum pipeline (purification, 2D Fourier transform, E/B
construction, binning) and averaged over N = 100 realisations to give the
bandpower window functions 𝓜^XX_ℓℓ′ (Eq. 76), for XX ∈ {EE→EE, EE→BB,
BB→BB, …}; they include "beam convolution, sky cut, map projection,
polynomial filtering, scan-synchronous signal subtraction, deprojection,
and power spectrum estimation". Filtering moves power from low ℓ into
higher bins, so the measured bin centres differ from the nominal ones
(first bin: nominal 20–55, measured 37–54, centre 46.4) [src:
arXiv:1603.05976, Sect. VII.3.1, Table 2]. The integral of each window is
the suppression factor: beam-dominated at high ℓ, filter-dominated at low
ℓ [src: Sect. VII.3.2]. When maps are apodised differently (BK18 apodises
BICEP3 and the WMAP/Planck maps with the larger BICEP3 inverse-variance
pattern), the suppression of cross- relative to auto-spectra "is
automatically taken into account in the bandpower window function
calculations" [src: arXiv:2110.00483, App. D].

SPT-3G: ⟨Ĉ_ℓ⟩ = F_ℓ B_ℓ² ⟨C_ℓ⟩ (Eq. 2), with ⟨Ĉ_ℓ⟩ the NaMaster spectrum
after mode-coupling correction, F_ℓ the filter transfer function from 100
mock-TOD simulations of ΛCDM (r = 0) plus dust matched to the field, and
B_ℓ the beam from Saturn side lobes stitched to point-source main lobes
[src: arXiv:2505.02827, Sect. V]. Bandpowers are binned with weights w =
(C_ℓ^BB,IGW theory)²/var(C_ℓ^BB) (Eq. 3), so that bins are weighted by the
tensor signal-to-noise, over 32–102, 102–202, …, 402–502 [src: same].

### Step 3. Remove the noise bias
<!-- key: step-3-remove-the-noise-bias -->

Two routes are in use.

- Auto-spectra minus a noise model: BICEP/Keck builds 499 sign-flip noise
  pseudo-simulations (sequences of more than 10⁴ subsets, equal weight in
  both signs, empirically uncorrelated) and subtracts their mean spectrum,
  "very important for the auto-spectra" [src: arXiv:1810.05216, App. H].
- Cross-spectra between data splits only: SPT-3G averages the cross-
  spectra of 24 chronological equal-weight bundles "to eliminate noise
  bias" [src: arXiv:2505.02827, Sect. V]; SO does the same with four splits
  (see `deep/bmode-foreground-separation.md`).

The trade-off is stated in the likelihood paper: an off-diagonal (cross
only) estimator is unbiased whatever the noise and "might therefore be
more robust" than one using auto-spectra, where a noise-model error biases
the estimate immediately; but it is not positive definite and its
distribution differs, so a likelihood built for Wishart-like spectra may
need modification (Hamimeche and Lewis 2008, arXiv:0801.0554, App. C, Eqs.
86–88) [src].

### Step 4. Calibration and leakage terms (SPT-3G)
<!-- key: step-4-calibration-and-leakage-terms-spt-3g -->

SPT-3G calibrates the polarisation amplitude by comparing EE at 302 ≤ ℓ <
602 to the Planck 2018 best-fit ΛCDM spectrum (uncertainties 2.5%, 2.3%,
3.6% at 95, 150, 220 GHz), and subtracts monopole E→B and T→B leakage as
D′_b^BB = D_b^BB + (D_b^EB)²/D_b^EE + (D_b^TB)²/D_b^TT (Eq. 4); in the
lowest bin these terms are below 3 × 10⁻⁴, 6 × 10⁻⁴ and 2 × 10⁻³ μK² for
the three auto-spectra. Higher-order beam leakage is neglected because the
arcminute beam would require pointing offsets of a full beam width to
matter at degree scales [src: arXiv:2505.02827, Sect. V.1]. Before
spectra, the 150 GHz Q maps are cleaned of polarised atmosphere with a
scaled, low-passed 220 GHz map per observation, and observations are
weighted by their ℓ = 50–250 noise: a fivefold improvement in polarised
noise power at ℓ ≈ 30–100, and ℓ_knee from 259 to 182 at 150 GHz [src:
Sect. IV.1, Table 1].

### Step 5. Simulations and the bandpower covariance
<!-- key: step-5-simulations-and-the-bandpower-covariance -->

BICEP/Keck [src: arXiv:1810.05216, App. H; arXiv:2110.00483, main text]:

- 499 lensed- and unlensed-ΛCDM realisations made by resampling timestreams
  from simulated input maps through the full pipeline; the unlensed set
  measures the purity achieved by matrix purification.
- Gaussian power-law dust maps with the observed amplitude, also through
  the pipeline, used where the fluctuations of the real data must be
  matched (spectral-stability tests, the PTE of the data χ²).
- The covariance for any model with signal components of given SEDs is
  assembled from signal×signal, noise×noise and signal×noise simulation
  spectra. Terms with zero expectation (signal–noise, BICEP/Keck noise ×
  WMAP/Planck noise) are set to zero "to reduce the Monte Carlo error …
  given the relatively modest number of realizations", as is covariance
  between bandpowers more than one bin apart, while the covariance between
  auto- and cross-spectra of different bands is kept.

SPT-3G: 100 signal-plus-noise simulations per mask, each a signal
realisation plus a random sign-flip noise realisation; the estimate is
"conditioned" by zeroing off-diagonal elements statistically consistent
with noise [src: arXiv:2505.02827, Sect. V.3].

### Step 6. The Hamimeche–Lewis likelihood
<!-- key: step-6-the-hamimeche-lewis-likelihood -->

For n correlated Gaussian fields on the full sky, with Ĉ_ℓ the n × n
matrix of measured auto- and cross-spectra (noise included) and C_ℓ the
model, −2 ln L = (2ℓ+1){Tr[Ĉ_ℓ C_ℓ⁻¹] − ln|C_ℓ⁻¹Ĉ_ℓ| − n} (arXiv:0801.0554,
Eq. 41) = (2ℓ+1) Σ_i [D_ii − ln D_ii − 1], D the eigenvalues of
C_ℓ^(−1/2) Ĉ_ℓ C_ℓ^(−1/2) (Eq. 43). It is written in quadratic form with
g(x) = sign(x − 1) √(2(x − ln x − 1)) (Eq. 44) and a fiducial model C_f,
giving the cut-sky approximation

−2 ln L ≈ X_gᵀ M_f⁻¹ X_g, [X_g]_ℓ = vecp(C_fℓ^(1/2) g[C_ℓ^(−1/2) Ĉ_ℓ C_ℓ^(−1/2)] C_fℓ^(1/2)) (Eqs. 47–49),

with vecp the vector of distinct matrix elements and M_f the covariance of
those elements for the fiducial model, correlated across ℓ on a cut sky
[src: Sect. III.5]. Why it is used: exact on the full sky "however wrong
the fiducial model is", fast because M_f⁻¹ is precomputed, and it keeps
the non-Gaussian bandpower distribution; it assumes Ĉ_ℓ positive definite,
"which may break down for some estimators at low ℓ"; C_ℓ and Ĉ_ℓ must
include noise, so a zero-noise theory needs an effective noise N_ℓ [src:
same].

As applied: BK18 on 11 auto- and 55 cross-spectra of four BICEP/Keck, two
WMAP and five Planck maps; the other Planck bands are dropped as they "provide a
negligible amount of additional information" [src: arXiv:2110.00483, App.
D]. SPT-3G on its 6 spectra with M_f from its simulations, a fiducial r = 0
spectrum and sign-flip noise (Eqs. 5–6), sampled with Cobaya, uniform
prior r > 0 [src: arXiv:2505.02827, Sect. VI].

When estimated spectra can be negative (cross-spectra, or auto-spectra
after mode deconvolution), an offset O_ℓ is added: X_ℓ = (C_ℓ^fid + O_ℓ)
g((Ĉ_ℓ + O_ℓ)/(C_ℓ + O_ℓ)) with g(x) → sign(x) g(|x|) (Galloni et al.
2026, arXiv:2610.18036, Eqs. 29–30), following a choice made so that 99%
of simulated values are positive [src: Sect. 5.2.1]. In their LiteBIRD
simulations 1.3% (0.85%) of deconvolved spectra at ℓ ≤ 32 were negative,
17% (9%) at ℓ = 2, for two beam windows [src: same].

### Step 7. Null tests before unblinding
<!-- key: step-7-null-tests-before-unblinding -->

BICEP/Keck jackknives: 14 data splits chosen so that the halves may carry
different systematics; split maps are differenced, and χ² and χ (sum of
deviations) of the bandpowers against signal+noise simulations are formed
for EE, BB and EB, for the lowest five and nine bandpowers (ℓ < 200 and
< 300), band by band and year by year: 504 tests at 95 GHz and 1008 at
220/230 GHz in BK18 [src: arXiv:2110.00483, App. B]. PTEs are computed
against the 499 simulations because the statistics do not follow their
nominal distributions; an excess in the edge bins of the PTE histogram
would indicate a noise-debias or fluctuation problem. With more tests than
simulations, a few PTEs of 0 or 1 are expected (2 for BICEP3, 3 for Keck
220/230 GHz). Failures led to cuts made before the non-jackknife spectra
were examined: the November 2016 Keck data (season-split failure) and
BICEP3 focal-plane tile 1 (tile jackknife; suspected reflections) [src:
same].

SPT-3G null tests: five splits (chronological, sun up/down, moon up/down,
azimuth, scan direction); each null spectrum is compared with 100 sign-flip
expectation spectra. Pass criteria, stated in advance: (1) the table of
PTEs consistent with uniform, KS p > 0.05; (2) every PTE > 0.05/N_tests =
0.0008; (3) Fisher-combined PTE per test row > 0.05/N_rows = 0.01. Results:
KS p = 0.61, all PTEs > 0.0008, row PTEs 0.18–0.86 [src: arXiv:2505.02827,
Sect. V.2, Table 2].

### Step 8. Validate the limit on simulations
<!-- key: step-8-validate-the-limit-on-simulations -->

BK18 runs the full CosmoMC analysis on 200 lensed-ΛCDM + dust + noise
simulations: 60% of the r curves peak at zero and 11% have a lower
zero-to-peak likelihood ratio than the data; the zero-to-peak CDF is
compared with the ansatz ½[1 − f(−2 ln L₀/L_peak)], f the one-degree χ²
CDF. A faster check runs maximum-likelihood searches with non-physical
values (negative r) allowed, on simulations of the model being refitted,
and checks that inputs are recovered in the mean (a small bias on A_d is
formally detectable); the scatter gives σ(r) = 0.009. The collaboration
prefers this σ(r) as the measure of constraining power "since it is
independent of the particular noise fluctuation that is present in the
real data" [src: arXiv:2110.00483, App. E.3]. A synoptic diagnostic of
mode loss: f_sky(ℓ) = (1/(2ℓΔℓ)) (√2 N̄_b/σ(N_b))², the observed number of
B-mode degrees of freedom over the full-sky number, which turns down at
low ℓ from filtering and purification [src: main text, Fig. 3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### E/B separation
<!-- key: e-b-separation -->

| Method | Handles | Cost | Measured on the same simulations |
|---|---|---|---|
| Fourier E/B on apodised maps ("normal") | nothing beyond apodisation | leakage variance | noiseless r = 0 sims: r < 0.17 (95%) from leakage alone |
| Smith-type pure estimator | apodisation leakage | ignores spatial filtering | r < 0.074 |
| BK matrix purification | every linear filter in R | building and diagonalising R; loss of ambiguous low-ℓ modes | r < 8.3 × 10⁻⁵; leaked power about three orders of magnitude lower |

[src: arXiv:1603.05976, Sect. VII.2, 200 noiseless unlensed-ΛCDM
simulations]. Because the mean leakage is debiased, only its variance
matters, which is why the comparison is quoted as a limit on r [src:
same]. An approximate observation matrix from a subset of observations is
acceptable "as long as it is representative of the full scan strategy",
because purification only needs leakage below the noise [src: same].
NaMaster pure-B (SPT-3G, SO) is the pseudo-C_ℓ alternative; no paper read
here compares it with matrix purification on identical data.

### Auto-spectra with a noise model, or cross-spectra only
<!-- key: auto-spectra-with-a-noise-model-or-cross -->

BICEP/Keck keeps auto-spectra and debiases them with sign-flip noise;
SPT-3G and SO use only split cross-spectra. The first keeps all modes but
puts the noise model in the mean; the second is unbiased for any noise and
pays with spectra that can be negative and a non-Wishart distribution
[src: arXiv:0801.0554, App. C]. BK18 notes a preliminary downward bias on
r of 2 × 10⁻³ from "imperfections in our noise bias estimates as they
interact with leakage deprojection filtering" (`systematics.md#b9-bk18-budget-as-read-in-the-paper-body`)
[src: arXiv:2110.00483, App. F.2].

### Likelihood approximation
<!-- key: likelihood-approximation -->

- Hamimeche–Lewis: BK, SPT-3G; exact on the full sky, fiducial-dependent
  only on the cut sky [src: arXiv:0801.0554, Sect. III.5].
- Gaussian in bandpowers: SO checked that HL gives the same result when
  each bandpower averages more than 61 modes, and states this "would not
  hold" for BK-sized patches (`deep/bmode-foreground-separation.md`).
- Pixel-based at the largest scales: for LiteBIRD-like simulations
  (20,000 end-to-end, MC-NILC cleaning), the offset-HL 68% upper bound on r
  is 19–29% larger than the pixel-based benchmark over ℓ ≤ 128 (13.5–26.6%
  on the pixel-likelihood range); offset-HL bias is compatible with zero,
  while the pixel benchmark retains a MAP(r) of 0.07–0.12 δr from its
  finite real-space covariance. The pixel likelihood needs more than about
  12,000 simulations to meet the authors' criteria, the harmonic one a few
  hundred with the Sellentin–Heavens correction, without which "the
  harmonic bound is spuriously tight" [src: arXiv:2610.18036, Sect. 8].
  Their recommendations: Sellentin–Heavens correction, ℓ_max of the
  absolute range ≥ 40, signal-to-noise binning at small scales, and a
  Gaussian 640′ beam window [src: same].

### Covariance size and conditioning
<!-- key: covariance-size-and-conditioning -->

BICEP/Keck uses 499 realisations and removes terms with zero expectation
and correlations beyond adjacent bins; SPT-3G uses 100 and zeroes
off-diagonals consistent with noise [src: arXiv:1810.05216, App. H;
arXiv:2505.02827, Sect. V.3]. Neither paper read here applies a Hartlap
or Sellentin–Heavens correction; the LiteBIRD study finds that omitting the
latter makes the bound too tight [src: arXiv:2610.18036, Sect. 8]. The
covariance-correction formulae are in `cosmo-statistics-inference`.

### Patch and bins
<!-- key: patch-and-bins -->

BK18: 9 bandpowers over 20 < ℓ < 330 of nominal width 35; SPT-3G: 5 bins
over 32–502, wider, signal-to-noise weighted [src: arXiv:1603.05976, Table
2; arXiv:2505.02827, Sect. V]. SPT-3G's lowest usable multipoles are set
by its ℓ_knee (L2, `systematics.md#b6-low-frequency-noise-and-filtering`).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Purification regulariser | σ² = 1/100 of mean diagonal | BICEP2 | arXiv:1603.05976 | Sect. VI.1 |
| Pure-B subspace | largest 1/4 of eigenmodes; power kept to ℓ ≈ 700 | BICEP2 | arXiv:1603.05976 | Sect. VI.1 |
| Window-function realisations | N = 100 | BICEP2 | arXiv:1603.05976 | Sect. VII.3.1 |
| BB bins | 20–55, 55–90, …, 300–335 (nominal) | BICEP2 / BK | arXiv:1603.05976 | Table 2 |
| Simulations | 499 sign-flip noise; 499 lensed and unlensed ΛCDM | BK15, BK18 | arXiv:1810.05216 | App. H |
| Jackknife tests | 14 splits; 504 (95 GHz) and 1008 (220/230 GHz) tests | BK18 | arXiv:2110.00483 | App. B |
| Likelihood validation | 200 sims; 60% peak at r = 0; 11% beat the data's zero-to-peak ratio | BK18 | arXiv:2110.00483 | App. E.3 |
| Bundles; TF simulations; covariance simulations | 24; 100; 100 | SPT-3G | arXiv:2505.02827 | Sects. V, V.3 |
| Polarisation calibration | 2.5%, 2.3%, 3.6% (95, 150, 220 GHz) from EE at 302–602 | SPT-3G | arXiv:2505.02827 | Sect. V.1 |
| Null-test thresholds | KS p > 0.05; PTE > 0.0008; row PTE > 0.01 | SPT-3G | arXiv:2505.02827 | Sect. V.2 |
| HL vs pixel likelihood | 68% bound 19–29% larger (ℓ ≤ 128) | LiteBIRD-like sims | arXiv:2610.18036 | Sect. 8 |
| Simulations needed | pixel > 12,000; harmonic: a few hundred with SH correction | LiteBIRD-like sims | arXiv:2610.18036 | Sect. 8 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **E→B leakage from filtering.** Leakage variance comparable to the noise
  in BICEP2 without purification [src: arXiv:1603.05976, Sect. VII.1].
  Test: unlensed-ΛCDM simulations through the pipeline, BB measured;
  EE→BB window functions [src: arXiv:1810.05216, App. H;
  arXiv:1603.05976, Sect. VII.3.1].
- **Bin centres taken as nominal.** Filtering shifts the effective
  multipoles (first BICEP2 bin: nominal centre 37.5, measured 46.4) [src:
  arXiv:1603.05976, Table 2]; use the window functions, not the bin edges,
  when refitting public bandpowers.
- **Noise-model error in auto-spectra.** Shows up as an excess of jackknife
  PTEs in the edge bins [src: arXiv:2110.00483, App. B]; cross-spectra
  avoid it [src: arXiv:0801.0554, App. C].
- **Negative estimated spectra in HL.** g is undefined; use an offset form
  [src: arXiv:2610.18036, Sect. 5.2.1].
- **Too few simulations for the covariance.** Spuriously tight bound
  without the Sellentin–Heavens correction [src: arXiv:2610.18036, Sect.
  8]; zeroing known-zero terms is the BK remedy [src: arXiv:1810.05216,
  App. H].
- **Null tests judged one by one.** With hundreds of tests, PTEs of 0 or 1
  occur by chance; judge the histogram and multiplicity-corrected
  thresholds [src: arXiv:2110.00483, App. B; arXiv:2505.02827, Sect. V.2].
- **Data cuts after unblinding.** BICEP/Keck states that its cuts were
  made before the non-jackknife spectra were examined [src:
  arXiv:2110.00483, App. B]; a referee asks the same of any new analysis.
- **Quoting the data's r curve as the sensitivity.** BK prefers σ(r) from
  simulations, independent of the noise fluctuation in the data [src:
  arXiv:2110.00483, App. E.3].
- **Polarised atmosphere at ℓ ≲ 200.** The largest large-scale noise source
  for SPT-3G; tested by the Q-map excess and handled by 220 GHz
  subtraction [src: arXiv:2505.02827, Sect. IV.1].

## Reading list
<!-- key: reading-list -->

- Foundation: Hamimeche and Lewis 2008, arXiv:0801.0554 — the likelihood
  (Eqs. 41–50) and the cross-spectrum trade-off (App. C).
- Method: Keck Array and BICEP2 Collaborations 2016, arXiv:1603.05976 —
  observation matrix, purification (Eqs. 11–19, 72–74), window functions
  (Eq. 76).
- Application: BICEP2/Keck 2018 (BK15), arXiv:1810.05216 — simulation sets
  and covariance construction (App. H).
- Application: BICEP/Keck 2021 (BK18), arXiv:2110.00483 — jackknives (App.
  B), apodisation and spectra (App. D), likelihood validation (App. E.3).
- Application: Zebrowski et al. 2025, arXiv:2505.02827 — an independent
  NaMaster + HL pipeline with explicit null-test criteria (Sects. V–VI).
- Critique: Galloni et al. 2026, arXiv:2610.18036 — HL against a
  pixel-based likelihood, negative spectra, simulation counts.

## Not verified
<!-- key: not-verified -->

- How BICEP/Keck turns the r posterior into its 95% limit and whether it
  blinds; the BKP paper (arXiv:1502.00612) where the multi-spectrum
  likelihood was introduced was not read for this.
- "Appendix B of Ref. [28]" cited by BK18 for covariance details; the
  Smith pure-B estimator, Mangilli et al. 2015 (offset HL), Sayre et al.
  (leakage subtraction) and Dutcher et al. (SPT null-test criteria): cited
  inside the papers read, not read.
- The BICEP/Keck polarisation-angle and absolute-calibration procedure.
