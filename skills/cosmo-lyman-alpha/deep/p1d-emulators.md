# From P1D to cosmology with emulators — cosmo-lyman-alpha dossier

Scope: how an emulator-based P1D likelihood is built and run (simulation
design, post-processing of the IGM, emulator inputs and training, emulator
error, nuisance structure, compression to linear-power parameters, validation
on mocks), how the LaCE/cup1d, PRIYA and Lyssa/lym1d pipelines differ at each
step and why, and which failure modes their authors report.
Snapshot: 2026-10-16.
From: Chaves-Montero et al. 2026 review (arXiv:2605.22489), Sects. 0.5 and
0.6.2; DESI DR1 P1D cosmology (arXiv:2601.21432), Sects. 3 and 5.

Already in L2, not repeated here: the emulator table with training suites and
accuracies, the two emulation philosophies, the DESI DR1 implementation in
outline and its stated limitations
(`physics-and-methods.md#emulators-and-their-parameterisations`,
`physics-and-methods.md#cosmological-inference-from-p1d`); convergence, UVB and
code-comparison facts (`physics-and-methods.md#convergence-requirements`,
`systematics.md#simulation-and-emulator-systematics-for-p1d`); the contaminant
model of DESI DR1 (`systematics.md#g8-desi-dr1-p1d-cosmology-arxiv-2601-21432`);
the compressed-parameter results and their history, and pivot conventions
(`results.md#compressed-linear-power-parameters-at-k-0-009-s`,
`physics-and-methods.md#conventions-units-and-where-the-community-is`).

Notation: Δ²_p, n_p the amplitude and logarithmic slope of the linear power at
a pivot in comoving units and at the redshift of the data (LaCE); Δ²_★, n_★
the same at k_★ = 0.009 s/km and z_★ = 3; A_Lyα, n_Lyα the same at
k_p = 1 Mpc⁻¹, z_p = 3 (Lyssa); A_P, n_P the primordial amplitude and slope at
0.78 Mpc⁻¹ (PRIYA); F̄ = exp(−τ_eff) the mean transmission; T_0, γ the
temperature–density relation T = T_0 Δ_b^(γ−1); k_F or λ_P the pressure
smoothing scale; LF/HF low and high fidelity.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Design the simulation suite
<!-- key: step-1-design-the-simulation-suite -->

| Item | LaCE / cup1d (DESI DR1) | PRIYA (eBOSS DR14) | Lyssa / lym1d (eBOSS DR14) |
|---|---|---|---|
| Code | MP-Gadget (TreeSPH) | MP-Gadget | Nyx (Eulerian AMR) |
| Training runs | 30, fixed and paired, same phases | LF + HF multi-fidelity: 600 LF and 30 HF spectra per redshift, "ten times the number of simulations" after mean-flux sampling, i.e. 60 LF and 3 HF runs [der]; the 48 LF of `physics-and-methods.md#emulators-and-their-parameterisations` plus the 12 LF added here | 14 Latin hypercube + 4 refinement runs at low Ω_mh², plus a fiducial |
| Box, particles or cells | 67.5 Mpc, 2 × 768³ | — (not read) | 120 Mpc, 4096³ cells; ~3× MP-Gadget resolution |
| Cosmological axes | Δ²_★ ∈ [0.25, 0.45], n_★ ∈ [−2.35, −2.25]; H_0, ω_cdm, ω_b fixed | n_P, A_P, h, Ω_0h² | A_Lyα, n_Lyα, Ω_mh², h; ω_b fixed |
| Astrophysical axes in the runs | H I reionisation midpoint, two thermal-history parameters | He II start/end and quasar index α_q, z_HI, ε_AGN | UVB scaling A_UVB |
| Sampling | Latin hypercube | Latin hypercube, extended by 12 LF runs to cover the 2σ n_P range | Latin hypercube plus refinement |
| Place read | arXiv:2601.21432, Sect. 2.2.1 | arXiv:2309.03943, Sects. 2.1, 2.3 | arXiv:2412.05372, Sect. 2.2; arXiv:2601.21432, Sect. 2.2.2 |

Reasons given. LaCE varies only the small-scale amplitude and slope because
"P1D measurements are only weakly sensitive to other cosmological parameters"
(arXiv:2601.21432) [src: Sect. 2.2.1]. Lyssa uses Ω_mh² as a design axis
because the dependence of P1D on Ω_m and H_0 enters mainly through the
velocity-to-comoving conversion H(z)/(1+z) ≈ √(Ω_mh²(1+z)) at z > 2, so it
avoids "artificial parameter dependencies" (arXiv:2412.05372, Eq. 4) [src:
Sect. 2.2]. Both run without massive neutrinos and treat Σm_ν by remapping
the amplitude (Lyssa) or by the compression (LaCE) [src: same; and
arXiv:2011.15127, Sect. 2.1].

### Step 2. Post-process the IGM state
<!-- key: step-2-post-process-the-igm-state -->

The mean flux and, for Nyx, the temperature are varied after the run, which
multiplies the training set cheaply.

- PRIYA: τ_eff(z) = τ_0 (τ^Kim(z)/τ^Kim(3))^dτ_0 τ^Kim(z), with
  τ^Kim = 0.0023(1+z)^3.65 (arXiv:2309.03943, Eqs. 2–3); 10 mean-flux values
  per snapshot, rescaling τ by 0.66–1.3, so that τ_eff(z = 3) spans
  0.238–0.47 [src: Sect. 2.1]. The freedom exists because F̄ is degenerate
  with the UVB amplitude [src: footnote in Sect. 2.1].
- Lyssa: gimlet rescales gas temperature and τ_eff; a main design of 4 thermal
  samples per simulation (3800 K < T_0 < 27800 K, 1.0 < γ < 1.9,
  |F̄ − exp(−0.0025(1+z)^3.7)| < 0.15) and an auxiliary design of 15 per
  base-suite point, 297 training points per redshift in all
  (arXiv:2412.05372) [src: Sects. 2.2, 2.3].
- LaCE: P1D extracted from snapshots between z = 2 and 4.5 every Δz = 0.25,
  768² skewers per axis at 0.05 Mpc (arXiv:2601.21432) [src: Sect. 2.2.1];
  the GP is trained on 2000 points split in two overlapping F̄ bins of 1000
  [src: Sect. 3.2].

### Step 3. Choose what the emulator takes as input
<!-- key: step-3-choose-what-the-emulator-takes-as-input -->

| Pipeline | Inputs | Redshift handling |
|---|---|---|
| LaCE / lace-mpg | Δ²_p, n_p at k_p = 0.7 Mpc⁻¹; F̄, σ_T, γ, k_F | redshift is not an input: one emulator for all z |
| PRIYA | 9 simulation parameters + τ_0, dτ_0 | one multi-fidelity GP per redshift |
| Lyssa / lym1d | A_Lyα, n_Lyα, Ω_mh², h, T_0(z), γ(z), F̄(z), λ_P(z) (8) | one GP per redshift, predicting all k bins |

Place read: arXiv:2601.21432, Sect. 3.1; arXiv:2309.03943, Sects. 2.1, 2.3;
arXiv:2412.05372, Sect. 2.3.

LaCE's reasons for linear-power inputs (arXiv:2011.15127) [src: Sect. 1]:
the effects of ΛCDM parameters on the forest "are strongly degenerate with
one another", degeneracies "can be artificially broken by interpolation
errors", and fewer dimensions place simulations more efficiently; and one
emulator can then serve extended models (Σm_ν, curvature, running) whose
small-scale linear power is described by an amplitude and slope. Supporting
facts: at fixed ω_m, H(z = 2) differs by 1.2% between h = 0.67 and 0.74 and by
0.5% at z = 4; Planck-chain samples with free Σm_ν or Ω_k, once amplitude and
slope are matched at 0.7 Mpc⁻¹, agree to within 1% over the BOSS-sensitive
scales [src: Sect. 2.1, Fig. 1]. Dropping redshift as input was tested by
removing all z = 3 training points: z = 3 predictions stayed sub-percent
[src: Sect. 4.2]. σ_T is used instead of T_0, with a (1+z)/H(z) factor that
keeps internal units comoving (arXiv:2601.21432) [src: Sect. 3.1].

Pivot choice in comoving units for training: "the P1D k-binning is uniform in
comoving coordinates across different cosmologies, which facilitates emulator
training"; predictions are converted to velocity units at inference [src:
same].

### Step 4. Train, and keep box noise out of the training set
<!-- key: step-4-train-and-keep-box-noise-out-of-the -->

- **lace-mpg.** Small boxes give spurious large-scale fluctuations that a
  naive emulator would learn, so it emulates five coefficients a_i of a smooth
  model, P1D^smooth = exp[g(k/k_max, a)] P1D^base(k, F̄),
  g(x, a) = Σ_{i=0}^{4} a_i / (1 + e^(2^(i−1) x)) (arXiv:2601.21432,
  Eqs. 3–4), where the base is ForestFlow evaluated on the central
  simulation and interpolated in F̄; for a = 0 it reduces to the Kaiser-like
  large-scale limit [src: Sect. 3.2]. Fits run to k_∥ = 4.25 Mpc⁻¹ with
  Nelder–Mead; the GP uses an anisotropic Matérn-1/2 kernel [src: same].
  Between mpg-central and mpg-seed the raw P1D differs by up to 2.5%, the
  smooth fits by about ten times less [src: same, Fig. 3].
- **PRIYA.** P_F^HF = ρ_z P_F^LF + δ(k, θ | z) with ρ_z constant and δ a GP
  (arXiv:2309.03943, Eq. 5); a k-dependent ρ "was harder to train and did not
  significantly improve the accuracy" [src: Sect. 2.3].
- **Lyssa.** Matérn-5/2 kernel with one length scale per input, optimised per
  k and z bin; typical length scales 3–20 times the simulated range
  (arXiv:2412.05372) [src: Sect. 2.3].

### Step 5. Put emulator error in the likelihood
<!-- key: step-5-put-emulator-error-in-the-likelihood -->

| Pipeline | Error term | How estimated | Reason given | Place read |
|---|---|---|---|---|
| cup1d | full emulator covariance, strongly correlated in k and z | residuals of 30 leave-one-out emulators on all k of the 11 snapshots, interpolated to DESI k and z; smoothing errors (≈ 5× smaller) and cosmic variance (≈ 10× smaller) omitted | captures training-set sparsity | arXiv:2601.21432, App. A |
| PRIYA | K = K_BOSS + σ_GP σ_GPᵀ + σ_CV σ_CVᵀ, σ_GP omitted in the baseline | σ_CV² = mean squared leave-one-out error over LF runs (Eq. 7) | varying h moves Fourier modes between bins and mimics new phases; σ_GP "can sometimes unphysically drive the chain away from the edges of parameter space" | arXiv:2309.03943, Sect. 3.3, Eqs. 6–7 |
| Lyssa | eBOSS covariance only | — | — | arXiv:2412.05372, Sect. 2.4 |

The DESI robustness check of its covariance: 30 covariances from 29 of the 30
leave-one-out tests scatter by a few percent (arXiv:2601.21432) [src: App. A].
PRIYA's σ_CV matters only at k < 2.5 × 10⁻³ s/km and 2.8 < z < 3.4, near the
~20 Mpc/h size and epoch of its He II reionisation bubbles; doubling it or
setting it to 0.02 left the posteriors "almost unchanged" (arXiv:2309.03943)
[src: Sect. 3.3].

### Step 6. Set up the nuisance structure and fit
<!-- key: step-6-set-up-the-nuisance-structure-and-fit -->

**cup1d (DESI DR1)** [src: arXiv:2601.21432, Sects. 5.1–5.2, Table 4]:

1. Fit each redshift alone first (Planck cosmology fixed, Nelder–Mead) to
   check the model is flexible enough. IGM parameters are fitted as
   deviations from mpg-central, with flat priors over the simulated range,
   "making it easier to define meaningful parameter ranges".
2. Joint fit: vary A_s ∈ [1.0, 3.4] × 10⁻⁹ and n_s ∈ [0.7, 1.3] with H_0 and
   densities fixed to Planck, and rescale (Δ²_★, n_★) from Planck without a
   Boltzmann call, since the Universe is effectively Einstein–de Sitter at
   these redshifts.
3. IGM parameters at four nodes z = 2.20, 2.73, 3.38, 4.20, linearly
   interpolated (six nodes tested: "excellent agreement"); metal and HCD
   parameters at two nodes (one power law in z); one resolution parameter per
   redshift bin. Total 53 free parameters: 2 cosmology, 16 IGM, 24 metal and
   HCD, 11 resolution. The "16 metal and 8 HCD parameters" of
   `physics-and-methods.md#cosmological-inference-from-p1d` are those 24: 8
   metal and 4 HCD parameters, each at two nodes; the HCD normalisation is
   fixed to zero because it is "strongly degenerate with the parameters
   scaling the mean flux".
4. Sampling: emcee, 11,648 chains of 3000 steps, 1500 burn-in, thinning 20,
   about one node hour per run.

**PRIYA** [src: arXiv:2309.03943, Sects. 3.1, 3.4]: Gaussian likelihood
summed over z = 2.2–4.6 with log det K; Cobaya Metropolis to R − 1 < 0.01;
strong Gaussian prior on ε_AGN (μ = 0.05, σ = 0.005) and a weak one on h
(μ = 0.70, σ = 0.015) "to avoid the inference straying into areas near the
edge of parameter volume"; DLA template reduced from four to two parameters
(α_lls for 1.6 × 10¹⁷–10²⁰ cm⁻², α_dla for 10²¹–10²²·⁵ cm⁻²) because the data
could not separate four; one Si III amplitude. The IGM temperature at mean
density can be added as a second likelihood.

**Lyssa** [src: arXiv:2412.05372, Sects. 2.3–2.4]: thermal parameters as
broken power laws with pivot z_p = 3 for T_0(z) and λ_P(z) and power laws for
γ(z) and τ_eff(z) (Eq. 6), chosen "to better compare with previous fits of
eBOSS data"; MontePython sampling.

### Step 7. Compress and validate the compression
<!-- key: step-7-compress-and-validate-the-compression -->

The DESI chains return (Δ²_★, n_★) at each step. Appendix B of
arXiv:2601.21432 tests the compression by matching (Δ²_★, n_★) between
cosmologies and comparing the linear P1D of Eq. 20 [src: App. B]:

- Varying h at fixed physical densities: residuals < 1.0% in P_lin and < 0.3%
  in linear P1D before matching, halved after matching.
- Σm_ν = 0.3 eV at fixed ω_m: residual approaching 0.7% after matching,
  "which explains the small shift" seen in that robustness variation.
- ω_cdm varied by up to 10σ around Planck: matching reduces residuals by
  more than an order of magnitude but extremes stay above 1%; matching also
  the curvature α_★ = d²log P_lin/d log k² at the pivot (Eq. 21) reduces them
  further. α_★ is not used because the MP-Gadget suite varies only A_s and
  n_s, so α_★ is the same in every training simulation; lace-lyssa includes it
  because Lyssa spans ω_cdm [src: App. C].

Pivot: k_★ = 0.009 s/km is kept for continuity; the decorrelation pivot for
DR1 is 0.019 s/km (r = −0.0011), where Δ̃²_★ = 0.600 (+0.049/−0.052) and
ñ_★ = −2.446 ± 0.019, with amplitude S/N 11.8 against 11.7, a negligible gain
[src: App. F]. Conversion between conventions (arXiv:2412.05372, Eqs. 2–3):
Δ²_★ ≈ A_Lyα (k_★³/2π²)(H(z)/(1+z))(k_★/k_Lyα)^n_Lyα and n_★ ≈ n_Lyα, with
k_★ converted to comoving units [src: Sect. 2.2].

### Step 8. Validate on mocks from other codes
<!-- key: step-8-validate-on-mocks-from-other-codes -->

DESI built smoothed, contaminant-free mocks from mpg-central, mpg-seed,
lyssa-central and Sherwood, gave them the DR1 covariance and fitted them with
the full contaminant model. All four return compressed parameters consistent
with truth, so limited MP-Gadget resolution and SPH-versus-grid differences
"do not bias the inferred cosmological constraints beyond the 1σ level"; the
fitted metal and HCD parameters are consistent with zero, yet IGM, metal, HCD
and resolution parameters may absorb modelling errors and are reported as
nuisances (arXiv:2601.21432) [src: Sect. 5.3]. PRIYA recovered all inputs
within 1σ on an HF output, and on an LF run with a different seed recovered
n_P, A_P and τ_0, dτ_0, but not h (arXiv:2309.03943) [src: Sect. 3.5].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Linear-power inputs or cosmological-parameter inputs
<!-- key: linear-power-inputs-or-cosmological-parameter -->

Linear-power inputs (LaCE) buy fewer dimensions, redshift-independent
emulation and reuse for smooth extensions; they cost validity for models with
"sharp features in the small-scale matter power spectrum" (WDM, ultra-light
axions) and for models with a non-standard baryon–velocity relation such as
modified gravity (arXiv:2011.15127) [src: Sect. 6]. Cosmological inputs
(PRIYA, Lyssa) keep h and Ω_mh² explicit; PRIYA found that h carries "zero
cosmological information" and relabelled it v_scale, since it only maps
simulation bins to velocity and is degenerate with the initial seed
(arXiv:2309.03943) [src: Sect. 3.5].

### Box volume, resolution and phases
<!-- key: box-volume-resolution-and-phases -->

Fixed-and-paired 67.5 Mpc boxes (MP-Gadget) against 120 Mpc single-phase
boxes (Lyssa): cosmic variance in smooth-model fits is below 2% for MP-Gadget
but up to 10% raw and 2.5% after smoothing for Lyssa, roughly ten times
larger; lace-lyssa leave-one-out accuracy is better than 2% at 1σ against
twice that precision for lace-mpg (arXiv:2601.21432) [src: App. C]. DESI kept
lace-mpg for three stated reasons: lace-lyssa's error is dominated by cosmic
variance not captured by leave-one-out; Lyssa used one transfer function for
baryons and dark matter, which suppresses P1D by up to 5% at high z and small
scales, corrected from a single simulation; and the resolution advantage of
Lyssa did not matter, because lace-mpg recovers a Lyssa mock within 1σ [src:
same]. The cost on the MP-Gadget side: limited resolution could underestimate
P1D by ~10% at the smallest DESI scales at z = 3 [src: Sect. 2.2.1]. On DESI
data the two emulators agree at ≃ 0.5σ, with a 70% larger Δ²_★ error for
lace-lyssa [src: Sect. 6.1.2].

### Single or multi-fidelity
<!-- key: single-or-multi-fidelity -->

PRIYA combines cheap LF and expensive HF runs through ρ_z and a GP
correction; leave-one-out errors were 0.2% (LF) and 1% (HF), the latter
"likely a significant over-estimate" since it removes a third of the HF data
(arXiv:2309.03943) [src: Sect. 2.3].

### Emulator error: include, omit, or estimate how
<!-- key: emulator-error-include-omit-or-estimate-how -->

DESI includes a leave-one-out covariance; it costs 30% (Δ²_★) and 19% (n_★)
precision (`physics-and-methods.md#cosmological-inference-from-p1d`). PRIYA
omits the GP's own error because it penalises fits near the parameter edges
where, with few simulations, "there is not enough information present for the
GP to learn" that the model is accurate; including it mostly shifts weakly
measured parameters (Ω_Mh², z_HI) and leaves cosmology unchanged
(arXiv:2309.03943) [src: Sect. 3.5, App. A].

### Latin hypercube or adaptive refinement
<!-- key: latin-hypercube-or-adaptive-refinement -->

With 16 Nyx runs and a separate 9-run test hypercube, emulation was unbiased
with ~0.2–0.4% scatter and end-to-end fits on eBOSS-like errors were unbiased;
for DESI-like errors "even the small emulation errors can affect the
posterior, leading e.g. to erroneously bimodal distributions". Adding runs
throughout the hypercube "did not provide noticeable improvement"; one local
refinement step removed the bimodality "without a noticeable increase in
computing cost" (arXiv:2012.04008) [src: Sects. 4.4, 5]. The Lyssa suite's
four refinement runs at low Ω_mh² follow this route (arXiv:2412.05372) [src:
Sect. 2.2].

### Mean flux free or with an external prior
<!-- key: mean-flux-free-or-with-an-external-prior -->

Lyssa on eBOSS: with an external τ_eff prior (from a measurement anchored on
high-resolution data and a different continuum method) the A_Lyα tension
"completely disappears (+0.3σ)", although z ≥ 2.6 alone still shows +1.2σ; the
authors therefore "caution against strong interpretations of the baseline 3.8σ
tension" (arXiv:2412.05372) [src: Sect. 5.3.1]. They also note a large
A_Lyα–T_0 anti-correlation and decline high-resolution IGM priors for fear of
correlated methodological systematics [src: same]. DESI DR1 uses no
informative IGM priors because unbiased IGM recovery by cup1d was not
validated (`physics-and-methods.md#cosmological-inference-from-p1d`). On the
central mock, the baseline errors on Δ²_★ and n_★ are 1.5 and 1.7 times those
of a fit that frees only cosmology and the IGM (contaminants fixed to truth),
and 4.6 and 1.8 times those of a cosmology-only fit (arXiv:2601.21432) [src:
Sect. 5.3]: informative IGM priors would pay most on the amplitude.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Training runs, box | 30 fixed-and-paired, 67.5 Mpc, 2 × 768³ | lace-mpg | arXiv:2601.21432 | Sect. 2.2.1 |
| Snapshot spacing, skewers | Δz = 0.25 (z = 2–4.5); 768² per axis at 0.05 Mpc | lace-mpg | arXiv:2601.21432 | Sect. 2.2.1 |
| Smooth-model k range | to 4.25 Mpc⁻¹ | lace-mpg | arXiv:2601.21432 | Sect. 3.2 |
| Leave-one-out accuracy | better than 1% (30 tests) | lace-mpg | arXiv:2601.21432 | Sect. 3.3 |
| Leave-one-out accuracy | better than 2% at 1σ (14 tests) | lace-lyssa | arXiv:2601.21432 | App. C |
| Free parameters | 53 (2 + 16 + 24 + 11) | DESI DR1 | arXiv:2601.21432 | Sect. 5.2 |
| χ², single-z fits combined | 636 for 494 dof (p = 1.6 × 10⁻⁵); 577 (p = 0.58%) with 5% error inflation | DESI DR1 | arXiv:2601.21432 | Sect. 5.1 |
| χ², joint fit | 655, p = 22% (187 → 53 parameters) | DESI DR1 | arXiv:2601.21432 | Sect. 5.2 |
| Poor single-z fits | z = 3.0, 3.6, 4.0: p = 0.65%, 0.33%, 0.77% | DESI DR1 | arXiv:2601.21432 | Sect. 5.1 |
| Δχ² removing a contaminant (z = 2.2) | Si II–Si III 10.7, HCD 21.2, Si II–Si II 29.0, Lyα–Si II 46.5, Lyα–Si III 632.5; all 735.1 | DESI DR1 | arXiv:2601.21432 | Sect. 5.1 |
| Error inflation, baseline vs fixed contaminants / vs cosmology only | ×1.5/×1.7; ×4.6/×1.8 on Δ²_★/n_★ | mpg-central mock | arXiv:2601.21432 | Sect. 5.3 |
| Decorrelation pivot | 0.019 s/km | DESI DR1 | arXiv:2601.21432 | App. F |
| Mean-flux sampling | 10 values; τ × 0.66–1.3 | PRIYA | arXiv:2309.03943 | Sect. 2.1 |
| LF / HF leave-one-out | 0.2% / 1% | PRIYA | arXiv:2309.03943 | Sect. 2.3 |
| eBOSS k range emulated | 0.001–0.02 s/km, 35 bins of 5.42 × 10⁻⁴ s/km; z = 2.2–4.6 | PRIYA | arXiv:2309.03943 | Sect. 3.1 |
| Low-z DLA parameter | α_DLA(z < 2.6) = −0.0134 ± 0.0074; n_P → 0.916 ± 0.014; internal tension reduced by 1/3 | PRIYA | arXiv:2309.03943 | Sect. 5.1 |
| Training points per z | 297 | Lyssa | arXiv:2412.05372 | Sect. 2.3 |
| Lyssa pivot | k_p = 1 Mpc⁻¹, z_p = 3 | Lyssa | arXiv:2412.05372 | Sect. 2.2 |
| Converged box and cell (Nyx, DESI-like 1%) | 120 Mpc, ~30 kpc, ~4000³ cells; ~2 million CPU-h | Walther 2021 | arXiv:2012.04008 | Sect. 5 |
| Cost of one hydro run (LaCE era) | ~10⁵ CPU hours; ≲ 100 runs per analysis | LaCE | arXiv:2011.15127 | Sect. 1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Emulator learns box noise.** Large-scale fluctuations of small boxes enter
  the training set; mitigated by smooth-model coefficients and
  fixed-and-paired phases; test with a different-seed simulation
  (arXiv:2601.21432) [src: Sect. 3.2, App. C].
- **Edges of the training space.** Accuracy degrades away from training
  points; GP error then pushes chains away from edges (PRIYA), and priors on
  h or F̄ are used to stay inside (arXiv:2309.03943 [src: Sects. 3.4–3.5];
  arXiv:2412.05372 [src: Sect. 5.3.1]).
- **Mean-flux degeneracy.** The amplitude can be driven low by F̄ near its
  prior edge; compare with and without an external τ_eff prior
  (arXiv:2412.05372) [src: Sect. 5.3.1].
- **Spurious bimodality.** Small emulation errors at DESI precision; fix by
  local refinement (arXiv:2012.04008) [src: Sect. 5].
- **Compression outside its range.** Large ω_cdm shifts or sharp cut-offs
  break (Δ²_★, n_★); check linear-P1D residuals after matching, or add α_★
  (arXiv:2601.21432 [src: App. B]; arXiv:2011.15127 [src: Sect. 6]).
- **Initial-condition transfer functions.** One shared transfer function for
  baryons and dark matter costs up to 5% in P1D (arXiv:2601.21432) [src:
  App. C].
- **Data–model χ² excess.** Specific redshifts fit poorly without k-dependent
  residual structure; DESI inflates statistical errors by 5% and notes a
  possible systematic at z = 3 found in the estimator validation
  (arXiv:2601.21432) [src: Sect. 5.1].
- **Nuisances absorb physics.** Mocks free of contaminants still pass, but
  fitted IGM and contaminant parameters may lack physical meaning (same,
  Sect. 5.3); PRIYA's low-z tension may come from data systematics (z = 2.2
  measurements disagree between SDSS, DESI EDR and KODIAQ), stronger AGN
  feedback, DLAs, metals, or LLS-dependent quasar selection
  (arXiv:2309.03943) [src: Sect. 5.1].

## Reading list
<!-- key: reading-list -->

- Foundation: Pedersen et al. 2021, arXiv:2011.15127 — why emulate in
  linear-power parameters, and the redshift-independent emulator.
- Method: Walther et al. 2021, arXiv:2012.04008 — convergence for DESI,
  Latin hypercube against adaptive refinement, end-to-end mock fits.
- Application: Fernandez et al. 2024, arXiv:2309.03943 — PRIYA likelihood:
  multi-fidelity GP, mean-flux post-processing, σ_CV from h, priors.
- Application: Walther et al. 2025, arXiv:2412.05372 — Lyssa emulator,
  parameter design, mean-flux prior and the amplitude tension.
- Application: Chaves-Montero et al. 2026, arXiv:2601.21432 — cup1d with
  lace-mpg: smooth-model emulation, emulator covariance, nuisance nodes,
  compression tests, cross-code mocks.
- Simulation suite: Bird et al. 2023, arXiv:2306.05471 — the PRIYA runs.

## Not verified
<!-- key: not-verified -->

- The PRIYA LF/HF box sizes and particle loads (Table 1 of arXiv:2309.03943
  and arXiv:2306.05471 not read).
- The neural-network LaCE emulator (arXiv:2305.19064) and ForestFlow
  (arXiv:2409.05682) training details beyond L2.
- Pedersen et al. 2023, cited by arXiv:2601.21432 for the rescaling of
  compressed parameters and for tests on extended models (not identified or
  read).
- Simulation-based and EFT alternatives to emulator likelihoods
  (subtopic `theory-sbi-field-level`, status thin).
