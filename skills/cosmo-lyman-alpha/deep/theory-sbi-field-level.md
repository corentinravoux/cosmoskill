# Theory-based, simulation-based and field-level inference — cosmo-lyman-alpha dossier

Scope: how a perturbative (EFT) model of the forest is built, calibrated on
hydrodynamical simulations and applied to a P1D data vector; how the field-level
and hybrid EFT forward models are fitted and what they reach; how a
simulation-based (neural posterior) P1D analysis is set up and tested across
galaxy-formation models; and what each route assumes, gains and loses relative
to the emulator likelihoods of `deep/p1d-emulators.md`.
Snapshot: 2026-10-19.
From: Chaves-Montero et al. 2026 review (arXiv:2605.22489), Sects. 0.6.1,
0.6.3, 0.6.4.

Already in L2, not repeated here: the one-paragraph list of EFT, field-level,
hybrid and SBI papers with their headline accuracies
(`physics-and-methods.md#perturbative-models`); the EFT accuracy figures and
the "phenomenological models fail at the field level" warning
(`systematics.md#d2-small-scale-non-linearity-in-full-shape-fits`); the BAO
shift from EFT parameters (`systematics.md#d1-non-linear-bao-broadening-and-shift`);
the EFT σ_8 and Σm_ν results on eBOSS P1D
(`results.md#parameters-in-extended-models`); the method debate for 3D full
shape (`open-questions.md#full-shape-analyses-how-far-down-in-scale`); the
CAMELS cross-model bias in one line
(`systematics.md#simulation-and-emulator-systematics-for-p1d`).

Notation. δ_F = F/F̄ − 1 the flux contrast; δ the matter contrast;
η = ∂_∥v_∥/(aH) the line-of-sight velocity gradient (in linear theory
η = −f μ² δ in Fourier space); b_1 (= b_F = b_δ of L2) and b_η the two
linear biases; f the growth rate; μ = k_∥/k. Sign convention: the EFT papers
write P_tree = (b_1 − b_η f μ²)² P_lin (arXiv:2309.10133, Eq. 3.13), so their
b_η is positive and β = −b_η f / b_1 (stated in arXiv:2604.09407, Sect. 3.2);
the Kaiser convention of L2 writes b_F β_F = b_η f with the opposite sign of
b_η. The field-level papers write δ_F = b_1 δ − b_η η (arXiv:2507.00284,
Eq. 1), which gives the same power spectrum. P_lin is the linear matter power;
k_NL the non-linear scale; k_max the largest wavenumber kept in a fit.

## How it is done
<!-- key: how-it-is-done -->

### Route A — one-loop EFT of the 3D flux power
<!-- key: route-a-one-loop-eft-of-the-3d-flux-power -->

**Step A1. Write the bias expansion.** Because the flux exists only in
redshift space and absorption depends on the tidal field along the line of
sight, the Lyα expansion has only azimuthal symmetry around the line of sight
and admits line-of-sight operators absent for galaxies. At linear order
δ_F = b_1 δ + b_η ẑ^i ẑ^j ∂_i∂_j Φ (arXiv:2309.10133, Eq. 3.11), i.e.
b_1 δ + b_η η (Eq. 3.12). The authors' reason: the non-linear map F = e^(−τ)
"breaks the conservation of tracer number density" and forces line-of-sight
selection terms [src: Sect. 3.2]. To cubic order the deterministic expansion
has 4 selection-free coefficients (b_1, b_2, b_G2, b_Γ3) and 9 selection
coefficients (b_η, b_(KK)∥, b_δη, b_η², b_Π[2]∥, b_δΠ[2]∥, b_ηΠ[2]∥,
b_(KΠ[2])∥, b_Π[3]∥) (Eq. 3.15), with K_ij the traceless tidal tensor and
Π[n]_ij built by convective time derivatives (Eq. 3.16). The redshift-space
mapping then adds pure projection terms whose coefficients are fixed by the
equivalence principle and are not renormalised (Eq. 3.17). The one-loop power
is the usual 22 + 13 structure with selection-dependent kernels K_1, K_2, K_3
(Eqs. 3.18–3.20); K_1 = b_1 − b_η f μ².

**Step A2. Add counterterms and stochastic terms.** Higher-derivative terms
(Eq. 3.21) and a stochastic field with
⟨εε⟩ = P_shot + a_0 k²/k_NL² + a_2 k²μ²/k_NL² (Eq. 3.22). In the fitted model
the higher-derivative part is replaced by −2(c_0 + c_2 μ² + c_4 μ⁴) k² P_lin
(Eq. 5.2), "added here as proxy for the two-loop contributions"; the
stochastic terms were negligible for the 3D fit and set to zero [src:
Sect. 5.1]. Reason for keeping the k² terms although the scaling argument
places them at three-loop order: Sherwood is precise enough to detect them and
they "noticeably" improve the fit at k ~ 3 h/Mpc [src: Sect. 3.3].

**Step A3. Compute the loops.** The kernels are decomposed in powers of μ and
integrated with FFTLog; the implementation is a module of CLASS-PT, and "135
one loop integrals are computed in ≈ 1 second on one CPU core" per
cosmology; sampling nuisance parameters needs no recomputation
(arXiv:2405.13208, Supplemental Material) [src].

**Step A4. Calibrate on a hydrodynamical box.** Fit the binned P_3D(k, μ) of
a simulation with a pseudo-χ² that assumes a Gaussian diagonal covariance,
χ² = Σ_i [P_i^data − P^model(k_i, μ_i)]² / [2 (P_i^data)² / N_i], N_i the
number of modes per bin (arXiv:2309.10133, Eq. 5.1; same form in
arXiv:2412.06892, Eq. 13). No noise floor is added, "as our goal here is to fit
the data given its actual precision" [src: arXiv:2309.10133, Sect. 5.1]. Of the
16 nominal parameters (2 linear, 11 non-linear, 3 counterterms), b_Γ3 is set to
zero because it is degenerate with b_G2 at the power-spectrum level; priors are
flat on b_1, b_η ∈ [−2, 2], N(0, 2²) on all quadratic and cubic biases and
N(0, 0.1²) (h⁻¹Mpc)² on c_0,2,4 (Eq. 5.3). Reasons given: naturalness puts the
biases at O(1); the τ → F map multiplies τ-biases by τ_0 ≃ 0.3, so σ = 2 rather
than 10; the counterterm width is twice k_NL⁻² ≈ 0.05 (h⁻¹Mpc)² because
velocities may be more non-linear than densities [src: Sect. 5.1]. Parameters
that enter linearly (P_shot, c_0,2,4, and the four cubic selection biases) are
marginalised analytically; the rest are sampled with MontePython [src:
Sect. 5.1]. ACCEL² uses the same scheme, samples 8 parameters out of 15 (18
with stochastic terms), evaluates the model at the power-weighted mean k and μ
of each bin, and stops at Gelman–Rubin R − 1 < 0.01, about 0.1 CPU-hour
(arXiv:2412.06892, Sect. 4, Table 1) [src].

**Step A5. Choose k_max by posterior stability.** Fits at k_max = 2, 3, 4,
5 h/Mpc on Sherwood at z = 2.8 agree for 2 and 3 and shift "significantly" at
4 and 5, with a worse best-fit χ² beyond 3; 3 h/Mpc is the baseline
(arXiv:2309.10133, Sect. 5.2) [src]. At z = 3.2, with k_NL = 10 h/Mpc, the fit
holds to 5 h/Mpc and the μ⁴ counterterm is detected at almost 20σ, which the
authors read as velocities driving the breakdown and as a case for a
μ-dependent k_max [src: Sect. 5.2]. ACCEL² uses k_max = 2 h/Mpc by default
(arXiv:2412.06892, Table 2 caption) [src].

### Route A′ — from the 3D EFT to P1D
<!-- key: route-a-from-the-3d-eft-to-p1d -->

P1D = (1/2π) ∫_{k_∥}^∞ k P_3D dk (arXiv:2309.10133, Eq. 6.1) integrates over
modes that are not perturbative. The EFT treats it as a loop integral: cut the
integral at k_max (identified with the 3D fit limit) and absorb the cutoff
dependence into a polynomial in k_∥²,
P1D^EFT = (1/2π) ∫_{k_∥}^{k_max} k P_3D dk + C_0 + C_1 k_∥² + C_2 k_∥⁴
(Eq. 6.9); the stochastic terms of Eq. 3.22 have exactly this k_∥ dependence
and renormalise it (Eqs. 6.4–6.7). In 1D the one-loop part scales as (k_∥/k_NL)¹,
like the shot noise, so stochastic terms matter there and not in 3D [src:
Sect. 6, Eq. 6.11]. On
Sherwood at z = 2.8 four counterterms (C_0,2,4,6; C_6 to absorb the
extrapolation of the 3D fit between 2.5 and 3 h/Mpc) give a percent-level
match; the authors flag that four extra parameters "may represent a problem"
for real data and propose simulation priors [src: Sect. 6, Eq. 6.12].

### Applying Route A to data: the eBOSS DR14 P1D
<!-- key: applying-route-a-to-data-the-eboss-dr14-p1d -->

As done in arXiv:2405.13208 (v2 LaTeX source read; letter plus Supplemental
Material) [src throughout]:

1. **Data cut.** SDSS DR14 P1D restricted to 3.4 ≤ z ≤ 4.2 (6 bins). Lower
   bins dropped because they need "an accurate calibration of the bias
   parameters that is not possible with publicly available simulations"; the
   two highest dropped to avoid inhomogeneous reionisation. The public
   covariance with its diagonal systematic terms is used.
2. **Model.** One-loop 3D EFT (11 non-linear biases) integrated to
   k_max = 3 h/Mpc, plus C_0 + C_2 k_∥² (13 parameters per bin before priors).
   Si III oscillation as a multiplicative factor
   κ = 1 + 2a cos(v k_∥) + a², a = f_SiIII/(1 − F̄_fid), f_SiIII = 8.7 × 10⁻³,
   v = 2π/0.0028 km/s, F̄_fid = exp(−0.0025(1+z)^3.7); thermal broadening as
   exp(−(k_∥/k_s)²) with k_s = 0.11 s/km. Results stated insensitive to these
   choices.
3. **Priors (the decisive step).** A Fisher study at z = 3.2 shows σ_8 is
   lost "almost entirely" if non-linear biases vary, and that even with only
   (σ_8, b_1, b_η) free the error goes from 0.1% (unmarginalised) to 3%. So
   b_1, b_η are free per redshift bin (12 parameters; per-bin preferred over
   smooth evolution on χ²) and every non-linear bias follows a linear relation
   b_O = A_O b_1 + B_O fitted to Sherwood P_3D at z = 2, 2.4, 2.8, 3.2
   (Supplemental Table; e.g. A, B = −0.32, −0.52 for δ²; 4.4, 0.063 for δη),
   with flat errors of 1 imposed on cubic biases "to be conservative and
   avoid overfitting". Reason for priors as functions of b_1: such relations
   "are more robust than the bias parameter values themselves".
4. **Recalibration of C_n.** Sherwood P1D does not match SDSS; mean-flux
   renormalisation removes most of the difference; the remainder is absorbed
   by recalibrating C_0(b_1), C_2(b_1) on synthetic P1D from the LaCE neural
   emulator varying only two thermal parameters (reduced χ² 1.2–1.4 per
   redshift). The other LaCE parameters were not tuned "to avoid double
   counting of information".
5. **Validation and result.** On LaCE mocks σ_8 is recovered to 0.3%, ≈ 15%
   of the statistical error. Data: σ_8 = 0.841 ± 0.017, χ² = 170 for 197
   degrees of freedom, with all other parameters fixed to a Planck-like
   cosmology. With b_O(b_1) scatter marginalised ("conservative"):
   σ_8 = 0.69 (0.75) ± 0.05 for the mean (best fit), "subject to significant
   prior effects"; Σm_ν < 0.08 eV (Planck + BOSS DR12 BAO) becomes < 0.15 eV.
   Freeing n_s gives a σ_8–n_s correlation of −0.99 at one redshift.

### Route A″ — analytic compression of the EFT nuisance space for DESI P1D
<!-- key: route-a-analytic-compression-of-the-eft -->

arXiv:2604.09407 replaces "fix the non-linear biases to b_O(b_1)" by a
controlled relaxation [src: Sects. 3–4]:

1. Fit all 15 P_3D biases on ACCEL² (baseline) and Sherwood (alternative) at
   five snapshots with iminuit, priors N(0, 4) on the ten one-loop biases and
   N(0, 1) on the three counterterms (rescaled by 10 h⁻¹Mpc), none on
   b_1, b_η; errors from 200 jittered Monte Carlo fits (Sect. 3.1, Table 1).
   b_O(z) follows A_O[(1+z)/4]^γ_O; for b_1, A = −0.179 ± 0.002 and
   γ = 3.25 ± 0.08, offered as data priors. The two simulations agree on
   b_O(b_1) within errors "with a minor indication of a systematic
   difference".
2. Integrate P_3D^EFT to k_max = 3 h/Mpc, chosen so that k³P_lin/2π² ≲ 1, and
   fit the residual P1D with C_0, C_2, C_4, each a quadratic in b_1. The
   non-stochastic EFT part is > 70% of ACCEL² P1D at the lowest k, ~40% at
   2 h/Mpc and 0 at 3 h/Mpc (z = 2.6) (Sect. 3.1.1).
3. Per redshift bin, build the Fisher matrix of P1D in the 15-dimensional
   bias space, project out the direction m of the fiducial b_O(b_1) relation
   (F* = Π F Π, Π = I − vvᵀ/|v|², v = F m), and keep the leading eigenvectors
   q_n of F*: λ_1/λ_0 = 3.4%, λ_2/λ_0 = 0.2%; three vectors reconstruct F to
   10⁻⁵ relative Frobenius distance (Sect. 3.2).
4. Linearise in the q_n amplitudes and in C_n and marginalise them
   analytically: φ_MAP = Σ_MAP β_MAP, Σ_MAP⁻¹ = KᵀC⁻¹K + S⁻¹, and
   ln L_marg = −½(χ² + ln det Σ_MAP⁻¹) (Eqs. 8–13); the authors prefer this to
   the equivalent covariance update C + KSKᵀ because it avoids re-inverting a
   large matrix at each step (Sect. 4.1).

Stated limits of this route: like any emulator it depends on its training
simulations through b_O(b_1), and "it cannot eliminate the degeneracy between
the forest bias and the amplitude of the linear matter power spectrum"; the
fiducial b_O(b_1) direction responds almost like ln(10¹⁰A_s) (Sects. 3.2–3.3)
[src]. The forecast it yields is in `open-questions.md#forecasts-all-labelled`.

### Route B — EFT forward model at the field level
<!-- key: route-b-eft-forward-model-at-the-field-level -->

arXiv:2507.00284 and arXiv:2606.26234 [src: body of the first, read in LaTeX;
abstract and Sects. IV, VII of the second]:

1. Take the initial linear field δ_1 of the simulation to be modelled
   (Sherwood 160 h⁻¹Mpc, 2048³, z = 2.8, grid 1024² × 2048 along the line of
   sight; AbacusSummit boxes with an FGPA-painted forest in the second paper).
2. Build the operators to second order (δ_1, the shifted η combination
   δ_Z − (3/7) f μ² G̃_2, δ_1², G_2, δη, η², (KK)∥), orthogonalise them by
   Gram–Schmidt, and shift them by Zel'dovich displacements for IR
   resummation; Π[2]∥ is dropped as fully degenerate (2507.00284, the
   transfer-function model equation and its footnotes). With k-dependent transfer functions this
   second-order set reproduces the one-loop power and tree-level bispectrum.
3. Fit each transfer function β_i(k, μ) as the cross-spectrum with the truth
   divided by the operator auto-spectrum (written out for β_1), i.e. the
   choice that minimises the error power P_err = ⟨|δ_F^truth − δ_F^model|²⟩.
4. Judge the model by P_err and the cross-correlation coefficient
   (P_err = P_truth (1 − r_cc²)). EFT predicts P_err = n_0 (1 + α_1 k² +
   α_2 μ²k²) as k → 0.

Reason for working at the field level: matching a realisation requires all
amplitudes and phases to be right, "a more stringent accuracy test than
comparing summary statistics" [src: 2507.00284, Introduction]. A model built as
(P_F/P_lin)^(1/2) δ_1 matches the power spectrum by construction but fails at
the field level beyond 0.04 h/Mpc [src: 2507.00284, Results].

### Route B′ — hybrid EFT (HEFT)
<!-- key: route-b-hybrid-eft-heft -->

arXiv:2512.13681 [src: Sects. 2.1, 2.3, 5]: the same Lagrangian bias
expansion (with δ³ and a ∇²δ term) is attached as weights to the particles
of an N-body simulation and advected with the simulation's non-linear
displacements, 1 + δ_F^(s)(x) = ∫ d³q F(q) δ^D(x − q − Ψ^(s)(q)) (Eqs. 1, 4),
instead of Zel'dovich displacements. Transfer functions come from the
least-squares solution β̂ = M⁻¹A over k_min < k < k_max, μ_min < μ < μ_max
(Eqs. 7–10), with Δμ = 0.1, Δk = 0.005 h/Mpc, against the AbacusSummit FGPA
forest at z = 2.5. The authors propose an emulator of operator-template
spectra on fixed-phase AbacusSummit cosmologies (Eqs. 13–14).

### Route C — simulation-based inference on P1D
<!-- key: route-c-simulation-based-inference-on-p1d -->

arXiv:2603.13011, the first full SBI on P1D [src: Sects. II, III, IV]:

1. **Training set.** CAMELS LH suites: 1000 IllustrisTNG (AREPO) and 1000
   SIMBA (GIZMO) runs, 25 h⁻¹Mpc boxes with 256³ dark-matter and 256³ gas
   elements, Latin hypercube in Ω_m ∈ [0.1, 0.5], σ_8 ∈ [0.6, 1.0] and four
   feedback amplitudes; skewers at eight redshifts 2.00–3.49. No variation of
   thermal or reionisation history (Sect. II).
2. **Parameters.** Ω_m and σ_8, not (Δ²_★, n_★), because the suite varies
   only those two and the network does not need a minimal basis; the
   Einstein–de Sitter argument for the compression "may no longer hold" with
   dynamical dark energy (Sect. II.3).
3. **Scale and redshift cuts.** k_max = 3 h/Mpc and z < 3.5, because CAMELS
   resolution is below that of current emulator training sets and resolution
   corrections are still ~10% to 3 h/Mpc in this range (Sect. II.7).
4. **Estimator.** Neural posterior estimation with a masked autoregressive
   flow (10 transforms, 100 hidden units, batch 64, Adam with learning rate
   5 × 10⁻⁴, early stopping after 20 epochs) via sbi/LtU-ILI; input is the
   concatenated P1D at the eight redshifts; 950 training (90/10 split for
   validation) and 50 test simulations (Sect. III).
5. **Calibration tests.** Univariate coverage and TARP; mean flux of each
   model rescaled before mixing models, because a 5–15% mean-flux difference
   between TNG and SIMBA at z ≳ 3 is degenerate with cosmology (Sect. IV.2).

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### One-loop or minimal (tree-level) EFT
<!-- key: one-loop-or-minimal-tree-level-eft -->

The one-loop auto-power model has 19 free parameters (2 linear, 11 non-linear,
3 counterterms, 3 stochastic) (arXiv:2608.21226, Sect. 3.1) [src]. A
tree-level model with the leading counterterms and stochastic terms fits
Sherwood and Sherwood–Relics auto-spectra to k_max = 3 h/Mpc and the
flux × matter cross-spectrum to 2 h/Mpc [src: abstract, Sect. 5]. The cost is
degeneracy: P_shot, the counterterms and the linear biases are strongly
correlated, an unconstrained P_shot runs negative at higher redshift and drags
the other parameters, and "increasing the number of nuisance parameters is not
automatically conservative if the data do not constrain them independently"
[src: Sect. 5]. The tree-level paper is the closest thing to an independent
test of the EFT calibration route; its author list does not overlap with
those of the one-loop papers.

### Deterministic b_O(b_1) relations or marginalised scatter
<!-- key: deterministic-bo-b1-relations-or-marginalised -->

The eBOSS EFT result depends on this choice by a factor 3 in σ_8 error
(0.017 → 0.05) and moves the central value from 0.841 to 0.69 (mean)
(arXiv:2405.13208) [src]. Evidence on the assumption: ACCEL² and Sherwood
share one linear b_O(b_1) relation within errors (arXiv:2604.09407,
Sect. 3.1) [src]; the tree-level study finds that correlations with b_F "show
some scatter, indicating that one single parameter is not enough to determine
the model parameters", and that resolution and, less, box size shift the
inferred biases and counterterms, much reduced by splicing (arXiv:2608.21226,
abstract and Sect. 5) [src]. Reionisation history moves mainly the linear
biases (same) [src]. The compression route of arXiv:2604.09407 is the
intermediate option: keep b_O(b_1) as the backbone and marginalise the two or
three best-measured orthogonal departures.

### Which simulation calibrates the priors
<!-- key: which-simulation-calibrates-the-priors -->

Sherwood (160 h⁻¹Mpc, homogeneous UVB, optically thin, ionisation
equilibrium; arXiv:2309.10133, Sect. 5.1) [src] was the only public P_3D set
for the first EFT papers; ACCEL² (Nyx) is the baseline of the compression
paper; their b_O(b_1) agree within errors (arXiv:2604.09407) [src]. Stochastic
counterterms agree less well between the two ("not ideal", Fig. 4 caption)
and must be relaxed for data [src: Sect. 3.1.1].

### EFT, field-level EFT, HEFT or the phenomenological P_3D model
<!-- key: eft-field-level-eft-heft-or-the -->

| Model | Reach on simulations | Place read |
|---|---|---|
| Linear + transfer function, field level | fails beyond ~0.04 h/Mpc (Sherwood); ~0.1 h/Mpc at 5% (Abacus) | arXiv:2507.00284, Results; arXiv:2606.26234, Sect. IV.1 |
| Cubic EFT forward model, field level | P_3D within 5% to k ≈ 0.6 h/Mpc (Sherwood z = 2.8); 0.8 h/Mpc (Abacus); 1% (5%) to 0.3 (1.0) h/Mpc for 3D and 1D over z = 2.0–3.2 | arXiv:2507.00284; arXiv:2606.26234, abstract and Sect. IV.1 |
| HEFT (N-body displacements) | 5% (1%) to k ≲ 1 (0.3) h/Mpc, AbacusSummit FGPA forest | arXiv:2512.13681, Sect. 5 |
| One-loop EFT, power spectrum | sub-percent to 3 h/Mpc at z = 2.8 (Sherwood) | arXiv:2309.10133, Sect. 5.2 |

The HEFT paper converts its gain (k_max 0.8 → 1.0 h/Mpc) into "an increase of
the observed volume by a factor of two" and "up to ~40%" smaller errors, an
estimate from cumulative S/N, not a demonstrated parameter fit [src:
arXiv:2512.13681, Sect. 5]. Both field-level papers note that the DESI full
shape works at r ≥ 25 h⁻¹Mpc, k ≈ 0.13 h/Mpc, where their models are
sub-percent [src: arXiv:2512.13681, Sect. 5; arXiv:2606.26234, Sect. IV.1
footnote]. The empirical P_3D model used by DESI is validated on mocks at the
two-point level (`systematics.md#g7-desi-dr2-lyalpha-full-shape-arxiv-2607-27411`);
a field-level failure and an unbiased two-point fit are compatible.

### Emulator, EFT or SBI for P1D
<!-- key: emulator-eft-or-sbi-for-p1d -->

- **EFT** recomputes the prediction at any parameter point, so extended
  models need no new simulations; that is the authors' main argument, with
  ~1 s per cosmology (arXiv:2405.13208) [src]. It has been used for PBH limits
  from MIKE/HIRES P1D at z = 4.2–5.4 "down to scales of 100 kpc"
  (arXiv:2508.04767, abstract) [src]. Its costs: most nuisance directions are
  invisible to a 1D data vector (β cannot be constrained by DESI P1D;
  arXiv:2604.09407, Sect. 3.2) [src], so the result rests on simulation priors,
  and the b_1–A_s degeneracy stays.
- **SBI** needs ~10³ full simulations per galaxy-formation model and inherits
  their resolution; in return it needs no explicit likelihood and no
  Gaussian covariance. Against an explicit-likelihood fit on the same 950
  CAMELS nodes (RBF interpolation, Ledoit–Wolf-shrunk covariance from 27
  fixed-cosmology runs, rescaled by r² per step), the uncalibrated explicit
  posteriors were "severely overconfident" and needed a heuristic factor
  λ = 2.8 on the covariance; after it, SBI was ~4.7 (Ω_m) and ~6 (σ_8) times
  more accurate in residuals and 12% and 40% more precise (arXiv:2603.13011,
  Sect. IV.4) [src]: comparing SBI with an uncalibrated explicit likelihood
  would exaggerate the gain. The test is internal to a 25 h⁻¹Mpc suite with
  no thermal-history freedom.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Nominal one-loop P_3D parameters | 2 linear + 11 non-linear + 3 counterterms (+ 3 stochastic) | EFT on Sherwood | arXiv:2309.10133; arXiv:2608.21226 | Sect. 5.1; Sect. 3.1 |
| Bias priors in calibration fits | N(0, 2²); c_n ~ N(0, 0.1²) (h⁻¹Mpc)²; b_1, b_η flat in [−2, 2] | Sherwood z = 2.8 | arXiv:2309.10133 | Eq. 5.3 |
| Baseline k_max, 3D | 3 h/Mpc (z = 2.8), 5 h/Mpc (z = 3.2) | Sherwood | arXiv:2309.10133 | Sect. 5.2 |
| Fit quality | χ² = 188 for 161 points, 15 parameters | Sherwood z = 2.8 | arXiv:2309.10133 | Sect. 5.2 |
| Linear biases at z = 2.8 | b_1 = −0.2167 (+0.0093/−0.0096), b_η = 0.325 ± 0.023 | Sherwood | arXiv:2309.10133 | Table 1 |
| Model beyond k_max | within 10% at 3.5 h/Mpc, 20% at 5 h/Mpc | Sherwood | arXiv:2309.10133 | Sect. 5.2 |
| P1D counterterms (z = 2.8) | 0.085 + 1.8 × 10⁻³ k² + 3.1 × 10⁻⁴ k⁴ − 4.2 × 10⁻⁵ k⁶ (h⁻¹Mpc units) | Sherwood | arXiv:2309.10133 | Eq. 6.12 |
| ACCEL² default fit | k_max = 2 h/Mpc, 203 data points, χ²_ν = 1.19–1.31 (z = 2.0–3.0) | ACCEL² | arXiv:2412.06892 | Table 2 |
| ACCEL² b_1 | −0.0805 ± 0.0033 (z = 2.0), −0.1521 ± 0.0065 (2.6), −0.2108 (+0.0098/−0.0087) (3.0) | ACCEL², no stochastic terms | arXiv:2412.06892 | Table 2 |
| b_1(z) power law | A = −0.179 ± 0.002, γ = 3.25 ± 0.08, in A[(1+z)/4]^γ | ACCEL² | arXiv:2604.09407 | Sect. 3.1 |
| EFT P1D data cut (eBOSS) | 3.4 ≤ z ≤ 4.2, 6 bins, 12 free parameters | SDSS DR14 | arXiv:2405.13208 | Data, Analysis details |
| Loop cost | 135 integrals in ≈ 1 s on one core | CLASS-PT module | arXiv:2405.13208 | Supplemental |
| Mock recovery of σ_8 | 0.3%, ≈ 15% of σ | LaCE mocks, 3.2 ≤ z ≤ 4.2 | arXiv:2405.13208 | Results |
| Compression spectrum | λ_1/λ_0 = 3.4%, λ_2/λ_0 = 0.2%; 3 vectors → 10⁻⁵ | DESI DR1 P1D bins, z = 3.0 | arXiv:2604.09407 | Sect. 3.2 |
| Lyα "shot noise" n_0 | ≈ 0.18 (h⁻¹Mpc)³; α_1 ≈ −0.25, α_2 ≈ 0.51 (h⁻¹Mpc)² | field-level fit, Sherwood z = 2.8 | arXiv:2507.00284 | Model error section |
| Onset of P_err scale dependence | k ≈ 0.4–0.6 h/Mpc | Sherwood and Abacus | arXiv:2606.26234 | Sect. IV.3 |
| BAO on EFT mock at z = 2.33 | α_∥ = 1.011 ± 0.018, α_⊥ = 1.0021 (+0.0060/−0.0080), k_max = 0.5 h/Mpc | field-level EFT mocks | arXiv:2606.26234 | Sect. VII.2.2, Eq. 65 |
| CAMELS training set | 2 × 1000 runs, 25 h⁻¹Mpc, 256³ + 256³, z = 2.00–3.49 (8 snapshots) | SBI | arXiv:2603.13011 | Sect. II |
| Cross-model bias | σ_8 high by ~10%, posteriors overconfident (train TNG, test SIMBA) | SBI | arXiv:2603.13011 | Sect. IV.2 |

The DESI DR1 P1D upper limit, 0.0318 s/km at z = 3
(`results.md#the-one-dimensional-flux-power-spectrum`), is about 3.6 h/Mpc
[der: k[h/Mpc] = k[s/km] × H(z)/((1+z) h), with H(3)/(4h) ≈ 113 km/s per
h⁻¹Mpc for flat Ω_m = 0.31]. The highest P1D bins therefore lie beyond the
3 h/Mpc integration cut of the 3D EFT, which is why the 1D stochastic
counterterms carry the small-scale signal.

## What goes wrong
<!-- key: what-goes-wrong -->

- **k_max chosen by χ² alone.** Posteriors drift before χ² degrades; the
  test is stability of all bias posteriors under k_max variation
  (arXiv:2309.10133, Sect. 5.2) [src]. The breakdown is along the line of
  sight: transverse modes fit to 4 h/Mpc at z = 2.8 [src: same].
- **Gaussian diagonal covariance in calibration fits.** The authors state the
  interpretation is "contingent upon our covariance matrix assumptions"
  (arXiv:2309.10133, Sect. 5.1); the compression paper finds χ² ≈ 36 for 303
  degrees of freedom with a 5% noise floor, i.e. the floor overestimates
  simulation errors (arXiv:2604.09407, Sect. 3.1) [src]. Prior widths
  extracted from such fits inherit this.
- **Degenerate parameters fixed by hand.** b_Γ3 = 0 (degenerate with b_G2)
  is "without loss of generality" only because the two enter as
  2b_Γ3 + 5b_G2 (arXiv:2405.13208, Supplemental) [src]; a field-level fit
  does measure b_Γ3 (arXiv:2606.26234, Table 7) [src].
- **Simulation–data mismatch absorbed by counterterms.** The Sherwood P1D
  does not match SDSS even after mean-flux renormalisation; the C_n
  recalibration on LaCE mocks moves C_0 from −0.17 b_1 − 0.0148 to
  −0.17 b_1 − 0.2053 h⁻¹Mpc (arXiv:2405.13208, Supplemental) [src], so the
  EFT likelihood is calibrated partly by an emulator.
- **Negative shot noise.** Free P_shot drifts negative, especially at high
  z, and shifts counterterms and biases (arXiv:2608.21226, Sect. 5) [src].
  The field-level table also returns negative P_shot (arXiv:2606.26234,
  Table 7) [src]. Check: refit with P_shot = 0 (the tree-level paper's
  Sect. 4.3) and compare.
- **Resolution-dependent priors.** Biases and counterterms depend on
  simulation resolution, less after splicing (arXiv:2608.21226, Sect. 5) [src].
- **Stochasticity beyond the gradient expansion.** P_err flattens near
  0.6 h/Mpc, where the power-law expansion of the noise breaks
  (arXiv:2507.00284) [src]; HEFT is the proposed remedy (arXiv:2512.13681)
  [src].
- **Truth built on FGPA.** HEFT and the Abacus tests use an FGPA forest
  painted on N-body particles as truth; the authors note the templates "use a
  simple FGPA prescription" (arXiv:2512.13681, Sect. 5) [src]. Agreement with
  such mocks tests the bias expansion, not the gas physics.
- **SBI out of distribution.** Training on one feedback model and testing on
  another gives ~10% σ_8 bias and overconfident posteriors; mean-flux
  mismatch alone biases the result severely; multi-domain training on TNG +
  SIMBA restores coverage (arXiv:2603.13011, Sects. IV.2–IV.3, App. E) [src].
  Pass criterion used: univariate coverage and TARP consistent with the
  diagonal [src: Sect. IV].

## Reading list
<!-- key: reading-list -->

- Foundation: Ivanov 2024, arXiv:2309.10133 — the line-of-sight bias
  expansion, counterterms, the P1D renormalisation (Sect. 6), k_max choice.
- Calibration: de Belsunce et al. 2025, arXiv:2412.06892 — EFT parameters
  per redshift from ACCEL², analytic marginalisation set-up.
- Application: Ivanov et al. 2025, arXiv:2405.13208 — first EFT fit to P1D
  data; read the Supplemental Material for the b_O(b_1) table and C_n
  recalibration.
- Method: Karaçaylı et al. 2026, arXiv:2604.09407 — b_O(b_1) backbone plus
  compressed, analytically marginalised departures for DESI P1D.
- Method: de Belsunce et al. 2025, arXiv:2507.00284, and 2026,
  arXiv:2606.26234 — field-level forward model, P_err, mocks for DESI and
  DESI-II.
- Method: de Belsunce et al. 2025, arXiv:2512.13681 — hybrid EFT with N-body
  displacements, template emulator design.
- Critique and test: Autieri et al. 2026, arXiv:2608.21226 — minimal EFT on
  Sherwood(-Relics): degeneracies, resolution and reionisation dependence,
  scatter in b_O(b_F).
- Method: Sinigaglia et al. 2026, arXiv:2603.13011 — first SBI on P1D,
  cross-simulator generalisation, explicit-likelihood comparison.
- Application: Ivanov & Trifinopoulos 2025, arXiv:2508.04767 — EFT P1D used
  for an extended model at z = 4.2–5.4.
- Review: Chaves-Montero 2026, arXiv:2605.22489, Sect. 0.6 — the four routes
  side by side.

## Not verified
<!-- key: not-verified -->

- The DESI P1D collaboration's own assessment of EFT likelihoods (not found
  in the passages of arXiv:2601.21432 read for L2).
- SBI on Voigt-profile distributions, neural compressions of spectra and
  CNN field-level IGM inference: known here only through the review
  (arXiv:2605.22489, Sects. 0.6.3–0.6.4); the primary papers were not
  identified or read.
- The compressed 3D bispectrum and Lyα × halo EFT papers (not read).
- Results of arXiv:2608.21226 beyond its abstract, Sect. 3.1 and conclusions
  (the numerical tables of its Appendices were not read).
- ACCEL² EFT parameters at z = 3.6 and 4.0 (table cut in the passage read).
