# BAO reconstruction and fitting — cosmo-galaxy-clustering dossier

Scope: how a BAO distance is obtained from a galaxy catalogue (displacement
solver, convention, smoothing, template, damping priors, 1D or 2D fit,
combination of spaces and methods) and how to choose between the variants;
values already in the reference files are pointed to, not repeated.
Snapshot: 2026-10-16.
From: Huterer 2023 review (arXiv:2212.05003), Sect. 3.1; DESI DR1 BAO key
paper (arXiv:2404.03000) and DR2 BAO working group (arXiv:2503.14742).

Already in L2, not repeated here: the DR1 template (Eqs. 5–16 of
arXiv:2404.03000), its priors and fit ranges, the DR1/DR2 reconstruction
settings per tracer (`physics-and-methods.md#reconstruction`,
`physics-and-methods.md#theory-models-in-current-analyses`), and the BAO
systematic budgets (`systematics.md#two-budgets-to-keep-apart`,
`systematics.md#reconstruction-choices`).

## How it is done
<!-- key: how-it-is-done -->

Notation follows Paillas et al. 2024 (arXiv:2404.03005) for the
reconstruction and Chen et al. 2024 (arXiv:2402.14070) for the model.

### Step 1. Estimate the displacement
<!-- key: step-1-estimate-the-displacement -->

The linear displacement is related to the observed redshift-space galaxy
field through the linearised continuity equation,
∇·Ψ + (f/b) ∇·[(Ψ·r̂) r̂] = −δ_g / b (arXiv:2404.03005, Eq. 3), with r̂ the
local line of sight. Because r̂ varies across a survey, the equation cannot
be solved by one FFT. Three solvers are in use [src: arXiv:2404.03005,
Sect. 2.2; Chen X. et al. 2024, arXiv:2411.19738, Sect. 3]:

| Solver | How it handles the varying line of sight | Where used |
|---|---|---|
| Multigrid (MG) | solves the potential equation (Eq. 4 of arXiv:2404.03005) in configuration space by finite differences and relaxation | BOSS-era codes; DESI cross-check |
| Iterative FFT on the mesh (iFFT) | assumes (Ψ·r̂)r̂ irrotational to start (Eq. 9 of arXiv:2404.03005), then iterates the real-space density estimate, δ_real,n, updating the potential on the grid (Eqs. 10–14) | DESI DR1 and DR2 baseline, 3 iterations; first use in a BAO data analysis [src: Sect. 2.2.1] |
| Iterative FFT on particles (iFFTP) | moves galaxies iteratively to remove RSD | eBOSS [src: arXiv:2404.03005, Sect. 2.2.1] |

The starting approximation alone over-corrects RSD; the iteration recovers
the real-space displacement provided f is known [src: arXiv:2404.03005,
Sect. 2.2.1]. In `pyrecon` the first iteration carries an extra factor
1/(1+β) on the RSD term to speed convergence [src: same].

### Step 2. Prepare the mesh
<!-- key: step-2-prepare-the-mesh -->

DESI paints galaxies and randoms on two grids of 4 h⁻¹ Mpc cells with
triangular-shaped-cloud assignment, pads each side by 20%, smooths with
S = exp[−(kΣ_sm)²/2] (arXiv:2404.03005, Eq. 15), and sets δ = 0 in cells
holding fewer randoms than 75% of the mean [src: Sect. 2.2.2]. The 4 h⁻¹ Mpc
cell agrees with a 2 h⁻¹ Mpc reference within 0.2% (monopole) and 1%
(quadrupole) up to k = 0.4 h Mpc⁻¹; below k = 0.2, a 6 h⁻¹ Mpc cell agrees to
better than 0.1% and 0.5% [src: arXiv:2411.19738, Sect. 5]. DR1 used
4 h⁻¹ Mpc for reconstruction and 6 h⁻¹ Mpc for the post-reconstruction power
spectrum of all tracers [src: same].

The fiducial growth rate is computed as f = σ8^vv / σ8^dd at z_eff with
`cosmoprimo`; the biases are taken from earlier DESI measurements cited
there [src: arXiv:2404.03005, Sect. 2.2.2].

### Step 3. Shift galaxies and randoms, choose a convention
<!-- key: step-3-shift-galaxies-and-randoms-choose-a -->

Galaxies are moved by −RΨ_r, where R multiplies the line-of-sight component
by (1+f). The conventions differ only for the randoms [src: arXiv:2402.14070,
Sect. 4.1]:

- RecIso: randoms shifted by −Ψ_r; linear prediction
  δ_r = (b_1 + (1 − S) f μ²) δ.
- RecSym: randoms shifted by −RΨ_r; linear prediction δ_r = (b_1 + f μ²) δ,
  i.e. linear RSD kept.

The reconstructed field is δ_r = δ_d − δ_s; in configuration space the
Landy–Szalay numerator uses DS and SS in place of DR and RR [src:
arXiv:2404.03005, Sect. 2.2]. The naming and the Zeldovich-level model of
both conventions go back to White 2015 (arXiv:1504.03677), who found that the
quantitative success of the model depends on how RSD are handled in the
reconstruction [src].

### Step 4. Model the post-reconstruction signal
<!-- key: step-4-model-the-post-reconstruction-signal -->

In real space, the post-reconstruction BAO damping is still a single
exponential with
Σ²_rec = (2/3) ∫ dk/(2π²) (1 − S)² P(k) (1 − j_0(k r_d))
(arXiv:2402.14070, Eq. 22), giving
P(k) = b² [P_nw + P_w exp(−k²Σ²_rec/2)] (Eq. 24). The paper states this
result is derived there for the first time, in contrast to earlier
perturbative treatments [src: Sect. 4.2.1]. Shot noise in the field used to
compute the shift adds Σ²_shot ≈ P_shot / (6π^{3/2} b² n̄ R) for R ≪ r_d
(Eq. 25), where P_shot is the dimensionless departure of the galaxy
stochasticity from Poisson (P_shot = 1 for Poisson) [src: Sect. 4.2.1]; for n̄ = 1/(3 × 10³) h³ Mpc⁻³ this is 6 b⁻² R_15⁻¹ P_shot h⁻² Mpc²
[src]. For DESI QSO-like bias and density the shot-noise term pushes the
post-reconstruction damping above the pre-reconstruction value at almost all
smoothing scales, yet reconstruction may still be preferred because it
removes the non-linear shift [src: Sect. 4.2.1, Fig. 5].

In redshift space, RecSym carries over as k²Σ²_rec → K²(μ)Σ²_rec, which
motivates C(k, μ) = (b + fμ²)² exp[−k²(μ²Σ²_∥ + (1 − μ²)Σ²_⊥)/2]
(arXiv:2402.14070, Eq. 26), the same form before and after reconstruction.
RecIso instead gives piecewise damping between displaced and shifted fields
(Σ²_ss and Σ²_ds, Eq. 27). The paper concludes that RecIso has a partly
uncancelled shift, more damping, less signal and more sensitivity to
reconstruction systematics than RecSym [src: Sect. 4.2.2]. A residual
theory error of order (Δf/f)Δα is expected from an imperfect f; the paper
takes a 5% uncertainty on σ8 as conservative [src: Sect. 4.2.2].

The dilation is applied to the observed wavenumbers by
k′ = (α_AP^{1/3}/α_iso)[1 + μ²_obs(1/α²_AP − 1)]^{1/2} k_obs and the
matching μ′ (arXiv:2411.19738, Eqs. 26–27), on the wiggle term only (see L2).

### Step 5. Fit, then validate before unblinding
<!-- key: step-5-fit-then-validate-before-unblinding -->

DESI uses one method for all tracers and fixes all fitting and
reconstruction choices on mocks and blinded data [src: arXiv:2404.03000,
abstract]. DR2 runs a ten-item unblinding checklist; each item passes if the
blinded-data difference falls within the range of 25 Abacus-2 DR2 mocks
[src: arXiv:2503.14742, Sect. VI.2, Table 6]:

1. χ² reasonable and consistent with mocks.
2. Reconstruction settings appropriate (data errors match mocks).
3. Stable when imaging weights are removed entirely.
4. Stable across sky regions and magnitude/mass splits.
5. Data errors within the mock distribution.
6. Pre- and post-reconstruction α consistent.
7. Mock fits unbiased (largest offset 2.46σ, post-reconstruction QSO,
   below the 3σ detection threshold).
8. ξ and P(k) consistent within 0.5σ.
9. Systematic budget fixed from DR1 with stated updates.
10. LRG3 and ELG1 consistent in 0.8 < z < 1.1 (α_iso 0.41σ; α_AP −1.66σ).

A systematic counts as detected above 3σ of the test's statistical
precision [src: Sect. VI.2].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Solver: MG, iFFT or iFFTP
<!-- key: solver-mg-ifft-or-ifftp -->

- MG and iFFT (3 iterations) agree within 0.4% in the post-reconstruction
  monopole and quadrupole on BAO scales with RecSym, for ELG, QSO and BGS;
  with RecIso within 1.2% (2% along the line of sight), worst on the largest
  scales [src: arXiv:2411.19738, Sect. 8].
- BAO fits on BGS and ELG show negligible MG–iFFT differences at
  five-year precision [src: Sect. 8].
- iFFTP diverges in realistic geometries because galaxies are moved off the
  boundaries; it does well in periodic boxes, where its propagator is
  slightly better than iFFT. The authors recommend against iFFTP without
  further development [src: abstract; Sect. 7.1].
- Cost: iFFT is consistent with MG at lower computational cost [src:
  arXiv:2404.03005, Sect. 2.2].

### Convention: RecSym or RecIso
<!-- key: convention-recsym-or-reciso -->

| | RecSym | RecIso |
|---|---|---|
| Linear RSD after reconstruction | kept | removed (with an S-dependent residual) |
| Damping form | single exponential (Eq. 26 of arXiv:2402.14070) | piecewise (Eq. 27) |
| Sensitivity to solver errors | smaller [src: arXiv:2411.19738, Sect. 8] | larger |
| Covariance | template independent of R_s | must be recomputed at each R_s [src: arXiv:2605.03446, Sect. 6.1] |
| Used by | DESI DR1/DR2 | SDSS, BOSS, eBOSS [src: arXiv:2402.14070, Sect. 4.1] |

Same-data comparison: on Euclid-like Flagship mocks the two give consistent
BAO within errors, and the Euclid pipeline recommends RecSym during testing
for its lower sensitivity to covariance variations [src: Euclid
Collaboration: Sarpa et al. 2026, arXiv:2605.03446, abstract and Sect. 7].
DESI blinded data were robust to the convention [src: arXiv:2404.03005,
Sect. 5].

### Smoothing scale Σ_sm (R_s)
<!-- key: smoothing-scale-sigmasm-rs -->

- Too large erases linear clustering; too small adds noise and non-linear
  modes; low-density tracers need more smoothing [src: arXiv:2404.03005,
  Sect. 4.2].
- DESI DR1 mock means: going from 15 to 10 h⁻¹ Mpc changes α_iso by at most
  0.0046 (ELG1) and its error by at most 0.0003 for the galaxy tracers; for QSO,
  20 instead of 30 h⁻¹ Mpc gives a larger bias (−1.82σ against −1.17σ) and a
  larger error (0.0039 against 0.0034) [src: arXiv:2404.03005, Table 4].
- Euclid: the continuous-field optimum is R_s ≈ 8.4 h⁻¹ Mpc, but sparse
  catalogues need an empirical check; over R_s ∈ [7, 19] h⁻¹ Mpc no
  significant bias or degradation was found, and large R_s is preferred
  because it allows coarser grids, provided it does not over-smooth the mask
  [src: arXiv:2605.03446, Sects. 6.1, 7].

### Reconstruction inputs (b, f, fiducial cosmology)
<!-- key: reconstruction-inputs-b-f-fiducial-cosmology -->

Sherwin & White 2019 (arXiv:1808.04384) show analytically that wrong
cosmology and bias assumptions shift the peak negligibly but can change the
peak shape at the per-cent level and the quadrupole amplitude at the 5%
level [src]. DESI DR2 tested this on data after unblinding: ELG2 has
b ≈ 1.4 against the 1.2 used, beyond the 10% tolerance the collaboration
accepts; reconstructing with 1.4 moved α_iso by 0.04% and α_AP by 0.3% [src:
arXiv:2503.14742, Sect. VII.2]. eBOSS LRG used b = 2.3,
f = Ω_m^{6/11}(z = 0.7) = 0.815 and 15 h⁻¹ Mpc smoothing [src: Bautista et
al. 2020, arXiv:2007.08993, Sect. 2.3].

### Damping parameters: fixed, free or prior
<!-- key: damping-parameters-fixed-free-or-prior -->

| Practice | Who | What it costs |
|---|---|---|
| Fixed to fits of N-body mock means | eBOSS LRG (Nseries means, held fixed for single realisations) [src: arXiv:2007.08993, Sect. 3.1] | biased α if the values are wrong [src: arXiv:2402.14070, Sect. 7.8] |
| Gaussian priors of 1 (Σ_⊥) and 2 h⁻¹ Mpc (Σ_∥, Σ_s), about 20% of expected values | DESI [src: arXiv:2402.14070, Sect. 7.8] | small extra error |
| Free | — | bias and weak constraints on noisy data [src: same] |

Critique: fitting with cosmological and damping parameters fixed at
fiducial values underestimates distance errors by nearly a factor of 2 in a
purely geometric framework (Anselmi et al. 2019, arXiv:1811.12312) [src].

### DESI DR1 methodology against (e)BOSS
<!-- key: desi-dr1-methodology-against-e-boss -->

Chen et al. 2024 list eight changes [src: arXiv:2402.14070, Sect. 7.8]:
RecSym instead of RecIso; cubic-spline broadband (14 free parameters in
P(k), 6 in ξ for ℓ = 0, 2) instead of polynomials, because it has "better
theoretical motivation" and is "less arbitrary in its choice of free
parameters" (validated in their Sect. 7.1); theory-motivated damping
priors instead of fixed values; FoG on the smooth part only; template
de-wiggled following Wallisch (2018, as cited) instead of Eisenstein–Hu or
Kirkby et al.; dilation of the wiggles only; flat priors on b and β;
ξ computed strictly as the Hankel transform of the P(k) model instead of
applying dilation and bias in configuration space. The last choice alone
gives 0.12% in α_AP between the two methods [src]. Following these
practices, modelling choices contribute at most 0.05% (α_iso) and 0.12%
(α_AP) [src].

The eBOSS LRG template, for comparison, is
P(k, μ) = b²[1 + β(1 − S(k))μ²]² / (1 + k²μ²Σ²_s/2) × [P_no peak +
P_peak e^{−k²Σ²_nl(μ)/2}] (arXiv:2007.08993, Eq. 4), with a Lorentzian FoG,
a peak/no-peak split by polynomial replacement of ξ_lin over the peak
region, and fits over 30 < r < 180 h⁻¹ Mpc [src: Sect. 3.1]. The Euclid DR1
pipeline uses a quadratic configuration-space broadband
A_ℓ,0 + A_ℓ,1 s_ref/s + A_ℓ,2 s²_ref/s² with s_ref = 80 h⁻¹ Mpc
(arXiv:2605.03446, Eq. 46) and an Eisenstein–Hu no-wiggle spectrum [src:
Sect. 4.2]. Three active pipelines therefore use three broadband and
de-wiggling choices.

### 1D or 2D fit
<!-- key: 1d-or-2d-fit -->

DR2 criteria [src: arXiv:2503.14742, App. B.1]: signal-to-noise high enough
for a stable 2D fit; a Gaussian α_AP posterior; an α_iso–α_AP correlation
matching mocks and theory; the χ² distribution against mocks. With them DR2
moved ELG1 and QSO to 2D and kept BGS in 1D (see L2).

### Configuration or Fourier space, and combining them
<!-- key: configuration-or-fourier-space-and-combining -->

- DESI: ξ is the fiducial space, P(k) a parallel analysis; on DR2 data the
  two agree, the largest difference being BGS, within 1σ [src:
  arXiv:2503.14742, App. A].
- eBOSS combined BAO from ξ and P, and BAO with RSD, into consensus values
  by C_c = (Σ_m Σ_n C⁻¹_mn)⁻¹ and x_c = C_c Σ_m (Σ_n C⁻¹_nm) x_m
  (arXiv:2007.08993, Eqs. 38–39), taking off-diagonal blocks from 1000
  EZmocks rescaled to the data (Eqs. 41–42), and combining at most two
  methods at a time to limit noise [src: Sect. 3.4].

### Sampler
<!-- key: sampler -->

Across emcee, dynesty, zeus and nautilus no systematic difference is seen,
but posterior means of single realisations differ by up to 0.1% (α_iso) and
0.5% (α_AP); nautilus was fastest and gives the evidence, and became the
Barry default [src: arXiv:2402.14070, Sect. 7.7]. The Euclid pipeline uses
an emulator (Bora.jl) with NUTS, more than 500 times faster than standard
MCMC [src: arXiv:2605.03446, abstract].

### Template fit or linear point
<!-- key: template-fit-or-linear-point -->

The linear point (mean of peak and dip positions of ξ_0) is fitted with a
centred quintic polynomial, ξ_0(s) = Σ a_i((s − s_0)/σ)^i,
s_0 = 93 h⁻¹ Mpc, σ = 15 h⁻¹ Mpc, over 70–115 h⁻¹ Mpc in 4 h⁻¹ Mpc bins
(Uberoi et al. 2026, arXiv:2601.05967, Eq. 12, Sect. 3.2). On DESI:
pre-reconstruction it differs from template α_iso by up to 1%, with a
residual offset even after the standard 1.005 correction; post-reconstruction
it is 15–60% more precise but still shifted by up to 0.5% in mocks; with a
damping correction it agrees with template BAO in DR1 and DR2, at the price
of the model independence that motivated it and up to 4% larger errors; no
linear point was found in pre-reconstruction DR1 BGS [src: Sect. 6;
abstract]. The authors keep it as a cross-check, not for inference [src].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| iFFT iterations | 3 | DESI DR1 | arXiv:2404.03005 | Sect. 2.2.1 |
| Mesh cell (reconstruction) | 4 h⁻¹ Mpc, 20% padding | DESI DR1 | arXiv:2404.03005 | Sect. 2.2.2 |
| Empty-cell threshold | < 75% of mean randoms per cell → δ = 0 | DESI DR1 | arXiv:2404.03005 | Sect. 2.2.2 |
| MG vs iFFT post-recon P_ℓ | < 0.4% (RecSym); < 1.2% (RecIso) | DESI mocks | arXiv:2411.19738 | Sect. 8 |
| Gain from reconstruction on α_iso error | 23–47% on blinded data, all tracers but QSO | DESI DR1 | arXiv:2404.03005 | Sect. 5 |
| α_iso–α_AP correlation | −0.12, −0.09, −0.03 (LRG1–3); −0.31 (ELG2); α_∥–α_⊥ about −0.45 | DESI DR1 blinded | arXiv:2404.03005 | Sect. 4.6 |
| Pre-recon α bias (mock means) | up to 0.5% α_⊥, 1.0% α_∥; post-recon < 0.2% | eBOSS LRG | arXiv:2007.08993 | Sect. 4.1 |
| Post-recon EZmock biases | up to 0.13% α_⊥, 0.18% α_∥ | eBOSS LRG | arXiv:2007.08993 | Sect. 4.1, Table 5 |
| eBOSS LRG data errors | ≈ 1.9% α_⊥, 2.6% α_∥ | eBOSS LRG | arXiv:2007.08993 | Sect. 4.1 |
| k_max effect on P(k) BAO errors | up to 50% worse at 0.2; about 10% better at 0.4 h Mpc⁻¹ | DESI mocks | arXiv:2402.14070 | Sect. 7.3 |
| s_min bias threshold | 0.1% in α_iso for s_min < 28 h⁻¹ Mpc | DESI mocks | arXiv:2402.14070 | Sect. 7.3 |
| Modelling-choice systematic | ≤ 0.05% α_iso, ≤ 0.12% α_AP | DESI | arXiv:2402.14070 | Sect. 7.8 |
| Damping priors | σ = 1 (Σ_⊥), 2 (Σ_∥, Σ_s) h⁻¹ Mpc | DESI | arXiv:2402.14070 | Sect. 7.8 |
| Bias tolerance for reconstruction | 10% | DESI DR2 | arXiv:2503.14742 | Sect. VII.2 |
| Detection threshold | 3σ of the test's precision | DESI DR2 | arXiv:2503.14742 | Sect. VI.2 |
| Mock-scatter check | 1–3 mocks outside 2σ (1 expected), 5–10 outside 1σ (8 expected), 25 mocks | DESI DR2 | arXiv:2503.14742 | Sect. VI.4.2 |
| RascalC BAO error accuracy | better than 5% (from DR1 studies) | DESI DR2 | arXiv:2503.14742 | Sect. VI.4.2 |
| Euclid continuous-field optimum R_s | ≈ 8.4 h⁻¹ Mpc | Euclid mocks | arXiv:2605.03446 | Sect. 6.1 |
| Euclid covariance mocks | 8 per snapshot (semi-analytic BeXiCov+WinCov); error bias from ≈ 20% to < 5% | Euclid mocks | arXiv:2605.03446 | Sect. 7 |
| Linear point fit | n = 5, 70–115 h⁻¹ Mpc, Δs = 4 h⁻¹ Mpc | DESI DR1/DR2 | arXiv:2601.05967 | Sect. 3.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Solver diverges at survey edges.** iFFTP displacements differ most from
  MG at redshift boundaries and along the line of sight [src:
  arXiv:2411.19738, Sect. 8]. Test: compare displacements with an MG
  solution in a middle redshift slice and at the boundaries.
- **Shot-noise-dominated tracer.** Reconstruction may not improve the error
  (DESI DR1 QSO on blinded data). DESI fixed reconstructed QSO as fiducial
  before unblinding, regardless of its efficiency on data [src:
  arXiv:2404.03000, Sect. 6; arXiv:2404.03005, Sect. 5]. Test: per-mock
  distribution of pre/post errors.
- **Wrong bias in reconstruction.** Shape and quadrupole errors rather than
  peak shifts [src: arXiv:1808.04384]. Test: rerun with the bias measured
  after unblinding, as DR2 did for ELG2 [src: arXiv:2503.14742, Sect. VII.2].
- **Damping fixed at wrong values or left free on noisy data.** Biased α or
  non-Gaussian posteriors [src: arXiv:2402.14070, Sect. 7.8]. Test: priors
  from Zeldovich expectations; compare fixed, prior and free.
- **Scale range too narrow in ξ.** With s_max < 130 h⁻¹ Mpc the quadrupole
  model absorbs BAO information unless scales on both sides constrain the
  broadband (≈ 0.15% in α_AP) [src: arXiv:2402.14070, Sect. 7.3].
- **Non-Gaussian posteriors in weak bins.** The reason DESI fits weak
  samples in 1D [src: arXiv:2503.14742, App. B.1]. DR1 found Gaussian
  posteriors after reconstruction; formal normality tests reject Gaussianity
  as chains grow, so DESI judged it visually [src: arXiv:2404.03005,
  Sect. 4.6].
- **Mock noise read as bias.** An excess near k = 0.29 h Mpc⁻¹ in the mock
  mean produced apparent >0.1% shifts for some k_max; no trend with scale
  identified it as noise [src: arXiv:2402.14070, Sect. 7.3].
- **Choosing settings on unblinded data.** DESI decided the QSO treatment,
  reconstruction scheme and smoothing before unblinding [src:
  arXiv:2404.03000, Sect. 6]; changes after unblinding are listed in
  `physics-and-methods.md#blinding`.

## Reading list
<!-- key: reading-list -->

- Foundation: White 2015, arXiv:1504.03677 — Zeldovich model of
  reconstruction; RecSym/RecIso.
- Method: Chen et al. 2024, arXiv:2402.14070 — post-reconstruction damping
  derivation, best practices, list of changes from (e)BOSS.
- Method: Paillas et al. 2024, arXiv:2404.03005 — iFFT algorithm as
  implemented, mesh settings, smoothing-scale tests.
- Method: Chen X. et al. 2024, arXiv:2411.19738 — MG, iFFT, iFFTP compared
  on DESI mocks; optimal grid and randoms.
- Application: Andrade et al. 2025, arXiv:2503.14742 — DR2 unblinding
  checklist, 1D/2D criteria, post-unblinding tests.
- Application: Bautista et al. 2020, arXiv:2007.08993 — eBOSS RecIso
  template, fixed damping, consensus combination.
- Application: Euclid Collaboration: Sarpa et al. 2026, arXiv:2605.03446 —
  RecSym against RecIso and smoothing on Euclid mocks.
- Test: Sherwin & White 2019, arXiv:1808.04384 — wrong reconstruction
  assumptions.
- Critique: Anselmi et al. 2019, arXiv:1811.12312 — fixed-parameter fits
  underestimate errors; purely geometric alternatives.
- Critique: Uberoi et al. 2026, arXiv:2601.05967 — linear point on DESI data.

## Not verified
<!-- key: not-verified -->

- The derivation of the RecSym/RecIso propagators in White 2015 (abstract
  only read).
- The solutions to wrong-assumption biases proposed by Sherwin & White 2019
  (abstract only).
- The DR2 mock-recovery table (Table 7 of arXiv:2503.14742, cited in
  Sect. VII.2 but not read).
- The Wallisch (2018) and Kirkby et al. (2013) de-wiggling methods: named in
  arXiv:2402.14070 and arXiv:2007.08993, not read; no identifier recorded.
