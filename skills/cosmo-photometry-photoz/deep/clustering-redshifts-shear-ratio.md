# Clustering redshifts and shear-ratio calibration — cosmo-photometry-photoz dossier

Scope: how a clustering-redshift (WZ) measurement is set up in current
analyses (reference slicing, scale range and weighting, estimator,
reference bias, model of the unknown sample's bias, covariance), how the
measured cross-correlations become a constraint on n(z) (shift fits,
Gaussian-process reconstruction, importance sampling of SOM
realisations), and how a shear-ratio likelihood is built; with the
choices DES, KiDS, HSC, Euclid and the DESI cross-survey calibration
made and their stated reasons.
Snapshot: 2026-10-21.
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

- **KiDS-1000.** A single broad radial bin with radial weighting (the
  Schmidt et al. 2013 technique); the earlier KiDS simulation study used
  100 kpc < r < 1 Mpc comoving throughout, and KiDS-1000 explored smaller
  ranges such as 30–300 and 50–500 kpc [src: arXiv:2007.15635,
  Sect. 4.1.1]. KiDS-Legacy later moved to the larger 0.5–1.5 Mpc (above).
- **HSC Y3 (CAMIRA LRG reference).** 0.1–1.0 Mpc, lensing weights
  included in the estimator, the-wizz for the pair counts [src:
  arXiv:2211.16516, Sect. 5.5].
- **HSC PDR3 × DESI DR1/DR2.** W(r) ∝ r^β with β = −1 (after Ménard et
  al. 2014 and Schmidt et al. 2013), fiducial 0.3–3 h⁻¹ Mpc, "more
  conservative" than the 0.1–1 Mpc of the first HSC calibration, with
  1–5 h⁻¹ Mpc as a check; the effective scales are ~0.6 and ~2 h⁻¹ Mpc
  [src: arXiv:2511.18133, Sect. 3.1].
- **DESI DR1 × DES Y3, KiDS-1000, HSC Y1 and Y3.** Reference slices of
  Δz = 0.05 over 0.1 < z < 1.6 with BGS, LRG and ELG; fits at R > 5,
  1.5–10 and 3–20 h⁻¹ Mpc give consistent b_u p_u within the errors
  [src: arXiv:2512.15963, Sect. 4.2, 6.2.2].

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
Sect. 4.2]. DESI DR1 uses w = D_uD_r/D_uR_r − 1 (Eq. 19) with TreeCorr,
because randoms exist for the reference only; each DESI galaxy carries
w_sys × w_IIP (individual inverse-probability fibre weight), which is
appropriate for cross-correlations since only one side of each pair is
subject to fibre collisions, and sources carry their shear weights, so
the result is the lensing-weighted n(z) [src: arXiv:2512.15963,
Sect. 4.2]. KiDS-1000 replaced the-wizz by yet_another_wizz to avoid the
sky pixelisation inherited from STOMP, which gives more realistic errors
at the small angular scales probed at high redshift [src:
arXiv:2007.15635, Sect. 4.1.1]; the-wizz itself separates pair finding
from the redshift estimate, so that a user's sub-sample is processed in
a fraction of the time of rerunning all the correlations [src:
arXiv:1609.09085].

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
[src: arXiv:2510.23565, Sect. IV.2.2]. KiDS-1000 corrects the
reference bias in the same way, and checks the source-bias evolution by
self-consistency (a broad sample against the weighted sum of the
tomographic bins), noting that this check is of limited use because
source bias evolves little across the core of one bin, and that outlier
populations far from that core cannot be corrected, so the method suits
only narrow, unimodal n(z) [src: arXiv:2007.15635, Sect. 4.1.1].
DES Y3 lenses add the unknown sample's own auto-correlation in photo-z
micro-bins of dz = 0.02, whose photo-z scatter integral (Eq. 8) is now
estimated from the clustering redshifts of the micro-bins rather than
from simulations as in DES Y1 [src: arXiv:2012.12826, Sect. 4.2].

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

Three other treatments of the unknown sample's bias:

- **HSC Y3** fits w_LRG−Y3 ∝ φ_nz b_PhotZ b_LRG w_DM (Eq. 7) with one
  free product b = b_LRG b_PhotZ per tomographic bin, and propagates the
  CAMIRA LRG photo-z error by drawing 10 reference catalogues from a
  conditional density trained on spectra and inflating the covariance
  (Eq. 8); w_DM uses CCL halofit at fixed cosmology, since cosmology
  changes its redshift scaling by ~10%, below the ~20% effect of bias
  modelling [src: arXiv:2211.16516, Sect. 5.5].
- **HSC × DESI** drops linear bias and assumes only that the
  cross-correlation coefficient r_xy, in w_xy ≈ r_xy √(w_xx w_yy) (Eq. 6),
  does not evolve with redshift inside a tomographic bin, a weaker
  assumption that the agreement of two scale cuts supports down to
  ~0.5 h⁻¹ Mpc [src: arXiv:2511.18133, Sect. 3.1].
- **DESI DR1** fits A_ur with two magnification amplitudes p, q
  (Gaussian priors 4.0 ± 2.0, flat prior on A_ur) (Eqs. 22–23) and
  marginalises a source bias b_u(z) = b₀ + b₁z (Eq. 27) whose Gaussian
  priors, fitted to mocks matched to each survey's magnitudes and
  colours, are widened by a factor 2 [src: arXiv:2512.15963, Sect. 5.2,
  6.2.2]. Magnification becomes non-negligible at z ≳ 1 because of the
  depth of the ELG sample [src: abstract].

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
- HSC Y3: bootstrap resampling as implemented in the-wizz [src:
  arXiv:2211.16516, Sect. 5.5].
- DESI DR1: jackknife over 60 regions; auto- and cross-correlation
  jackknife regions cannot be matched, which matters little because the
  cross-correlation dominates the error budget [src: arXiv:2512.15963,
  Sect. 4.2].

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
4. **Shift of the SOM n(z), single wide-area sample (KiDS-1000).**
   m_θ(z) = A n_SOM(z + δz^CZ) (Eq. 9). If the S/N varies across the
   peak, a template that is too broad (DIR) biases the mean high and one
   too narrow (SOM) biases it low, so the wide-area and deep pencil-beam
   CCs were not combined [src: arXiv:2007.15635, Sect. 4.1.3]. The result:
   no significant bias of the SOM n(z) against the CCs, and a SOM + CC
   calibration with mean-redshift errors of ~0.01–0.02 [src: abstract].
5. **Shift and stretch (DES Y3 lenses).** n(z) = s⁻¹ n_pz((z − z_mean −
   Δz)/s + z_mean) (Eq. 14), used where a shift alone fits badly [src:
   arXiv:2012.12826, Sect. 4.4]; this is the form Euclid later calls the
   SSM (Eq. 72 above). Mean-redshift errors 0.003–0.008, widths 4–9%,
   |Δz| < 0.01 against photo-z in most of eleven bins [src: abstract].
6. **Joint hierarchical posterior (HSC Y3).** A logistic Gaussian-process
   prior on the binned n(z), built from photometry (DNNz) with a
   cosmic-variance term, is combined with the CC likelihood and sampled
   with elliptical slice sampling, marginalising b [src: arXiv:2211.16516,
   Sect. 5.6]. Bin 3 is only partly calibrated and bin 4 not at all,
   since CAMIRA LRGs stop at z < 1.2; a 2–3σ inconsistency near z ≈ 0.2,
   where CAMIRA photo-z are known to be biased, is left for later work;
   conservative priors are recommended [src: Sect. 5.6–5.7].
7. **Splines or SGP on all bins (HSC × DESI).** With ELGs and QSOs the
   four HSC bins are calibrated; relative to Rau et al. the two high bins
   move to higher redshift, Δz₃ = −0.043 (+0.022/−0.020) and
   Δz₄ = −0.050 ± 0.012, shifts considerably smaller than those found by
   the HSC Y3 cosmic-shear analyses [src: arXiv:2511.18133, abstract].
   With these priors HSC Y3 cosmic shear gives S8 = 0.804 (+0.019/−0.018)
   against 0.769 (+0.031/−0.034), an error 1.8 times smaller [src:
   arXiv:2511.18134, abstract].

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

Other shear-ratio set-ups:

- **HSC Y3 (Rana et al.).** Spectroscopic lenses from GAMA, SDSS and
  DESI in fifteen narrow bins; sources in bins 2–4 behind z_l < 0.4
  lenses and bins 3–4 behind z_l < 0.55; five logarithmic θ bins from
  0.17′ to 137.5′ [src: arXiv:2508.21681, Sect. III]. The ratio is
  modelled through Σ⁻¹_crit,eff^(i,j) / Σ⁻¹_crit,eff^(i,k) (Eqs. 10–11), in
  which ΔΣ cancels [src: Sect. IV.1]. Gaussian Δz priors from Rau et al.
  on bins 1–2, uniform on bins 3–4, Δm priors of σ = 0.01, four PSF
  parameters [src: Sect. V]. Covariance from 300 random rotations of
  source shapes, added to the measured signal rather than used alone to
  avoid noise in the denominator; Hartlap-corrected total S/N 203; no
  significant correlation with cosmic shear, so the two are combined
  [src: Sect. VIII.1]. Blinded [src: abstract].
- **KiDS, DES and HSC around BOSS (Emas et al.)** with a Bayesian
  estimator to reduce the ratio bias [src: arXiv:2403.07313]; the
  DESI-DR1 3×2pt validation fits new ratios with the cosmic-shear model
  [src: arXiv:2510.05539].
- **DES Y1 lensing ratios** with galaxy, SPT and Planck lensing, a
  geometric test of cosmology rather than a redshift calibration [src:
  arXiv:1810.02212].

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
| Reference sample | one photometric LRG sample with modelled photo-z errors, z < 1.2 (HSC Y3) | DESI BGS, LRG, ELG, QSO (HSC × DESI; DESI DR1 cross-survey) | redshift reach (bins 3–4) and photo-z error of the reference | arXiv:2211.16516, Sect. 5.6; arXiv:2511.18133, abstract |
| Bias assumption | linear bias per slice | constant cross-correlation coefficient within a bin | how far to small scales one may go | arXiv:2511.18133, Sect. 3.1 |
| Combination with photometry | template shift or importance weights (KiDS, DES) | joint hierarchical posterior (HSC Y3) | whether the CC likelihood and the photometric prior enter one inference | arXiv:2211.16516, Sect. 5.6 |

Compared on the same mock: on MICE2, fitting KiDS CCs with the true n(z)
gives ⟨D_z⟩ within 0.01 of zero (except bin six) with scatter 0.005 in
bins 1–4, but fitting them with the SOM n(z) gives ⟨D_z⟩ = 0.014, 0.060,
0.056, 0.015, −0.016, −0.085: the shift absorbs the SOM–truth shape
difference [src: arXiv:2503.19440, Table 7 of the HTML rendering,
Sect. 6.2.2]. On real DES Y6 data, Fid (1.5–5 Mpc) and LS (5–15 Mpc) n(z)
agree within the systematic-function freedom; SS (0.1–1.5 Mpc) n(z)
differ by much more than their small errors [src: arXiv:2510.23565,
Sect. IV.2.2, App. D].

Compared across surveys with one reference: DESI DR1 clustering
redshifts agree with the SOM-calibrated n(z) of DES Y3, KiDS-1000 and
HSC within uncertainties in every tomographic bin [src:
arXiv:2512.15963, abstract]. Compared within HSC: the photometric and
CAMIRA-CC posterior means agree in the first three bins with mild tension
in the first [src: arXiv:2211.16516, Sect. 5.7]; the shear-ratio Δz₂–Δz₄
agree with the cosmic-shear self-calibration, with a mild Δz₃–Δz₄ shift
that disappears with DESI-DR1 lenses only, attributed to the
heterogeneous lens depth [src: arXiv:2508.21681, abstract]; the DESI
clustering shifts are smaller than the cosmic-shear ones [src:
arXiv:2511.18133, abstract]. Shear ratios add to cosmic shear less than
an accurate photo-z prior on the mean source redshift does, and their
S8 gain (up to 34%) shrinks when combined with full 3×2pt [src:
arXiv:2403.07313, abstract].

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
| KiDS-1000 scales; SOM + CC error | 100 kpc–1 Mpc (earlier), 30–300 and 50–500 kpc explored; ⟨z⟩ errors ~0.01–0.02 | KiDS-1000 | arXiv:2007.15635 | Sect. 4.1.1; abstract |
| DES Y3 lens WZ | ⟨z⟩ errors 0.003–0.008, width 4–9%; micro-bins dz = 0.02 | DES Y3 redMaGiC, MagLim | arXiv:2012.12826 | abstract; Sect. 4.2 |
| HSC Y3 WZ | 0.1–1.0 Mpc; 10 CAMIRA error-model catalogues; LRG z < 1.2 (no bin-4 CC) | HSC Y3 | arXiv:2211.16516 | Sect. 5.5–5.6 |
| HSC × DESI | 0.3–3 h⁻¹ Mpc, W ∝ r⁻¹; Δz₃ = −0.043, Δz₄ = −0.050 ± 0.012 vs Rau et al. | HSC PDR3, DESI DR1/DR2 | arXiv:2511.18133 | Sect. 3.1; abstract |
| HSC Y3 S8 with DESI WZ priors | 0.804 (+0.019/−0.018) vs 0.769 (+0.031/−0.034) | HSC Y3 cosmic shear | arXiv:2511.18134 | abstract |
| DESI DR1 cross-survey WZ | Δz = 0.05, 0.1 < z < 1.6; 60 jackknife regions; magnification priors 4.0 ± 2.0 | DES Y3, KiDS-1000, HSC Y1/Y3 | arXiv:2512.15963 | Sect. 4.2, 5.2 |
| HSC Y3 shear ratios | S/N 59, 75, 62 (bins 2–4), total 203; 300 rotations; S8 = 0.773 ± 0.031 with cosmic shear | HSC Y3 | arXiv:2508.21681 | abstract; Sect. VIII.1 |
| Shear ratio with cosmic shear | S8 improved up to 34% (KiDS, DES, HSC × BOSS) | three surveys | arXiv:2403.07313 | abstract |
| DES Y1 lensing ratio amplitude | A = 1.1 ± 0.1 relative to ΛCDM | DES Y1 + SPT + Planck | arXiv:1810.02212 | abstract |

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
- **A photometric reference with its own photo-z errors** (CAMIRA LRGs)
  leaves residual bias where those errors are known to be biased (the
  z ≈ 0.2 tension) and cannot reach the highest bins [src:
  arXiv:2211.16516, Sect. 5.6]. Test: draw the reference from its error
  model several times and compare with a spectroscopic reference.
- **Template shape under varying S/N.** A shift fit to a too-broad or
  too-narrow template biases the mean when S/N changes across the peak
  [src: arXiv:2007.15635, Sect. 4.1.3]. Test: the toy model of its
  App. A, or fit shift and stretch.
- **Heterogeneous lens depth in shear ratios** shifts the Δz₃–Δz₄ plane
  [src: arXiv:2508.21681, abstract]. Test: repeat with a single
  homogeneous lens sample.

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
- Method: Hildebrandt et al. 2020, arXiv:2007.15635, Sect. 4 — KiDS-1000
  CC with yet_another_wizz, SOM template shifts and the S/N argument.
- Method: Cawthon et al. 2020, arXiv:2012.12826 — DES Y3 lens WZ, bias
  correction from micro-bins, shift and stretch.
- Code: Morrison et al. 2016, arXiv:1609.09085 — the-wizz.
- Application: Rau et al. 2022, arXiv:2211.16516, Sect. 5.5–5.7 — HSC Y3
  joint hierarchical posterior with a photometric LRG reference.
- Application: Choppin de Janvry et al. 2025, arXiv:2511.18133 and
  arXiv:2511.18134 — HSC with DESI references, constant
  cross-correlation coefficient, effect on S8.
- Application: Ruggeri et al. 2025, arXiv:2512.15963 — one DESI
  reference for DES, KiDS and HSC, magnification and bias marginalised.
- Method: Rana et al. 2025, arXiv:2508.21681 — HSC Y3 shear-ratio
  calibration of Δz; Emas et al. 2024, arXiv:2403.07313 and 2025,
  arXiv:2510.05539 — shear ratios across KiDS, DES, HSC with BOSS and
  DESI; Prat et al. 2018, arXiv:1810.02212 — lensing ratios with CMB
  lensing.

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
- A search on 2026-10-21 found the 2025 HSC × DESI and DESI DR1
  cross-survey papers now included; no search restricted to 2026 was run,
  so later papers may be missing.
- Emas et al. 2024 and 2025 (arXiv:2403.07313, arXiv:2510.05539) and
  Prat et al. (arXiv:1810.02212) were read in their abstracts only; the
  form of the Bayesian ratio estimator was not read. The scale cuts of
  the HSC Y3 shear-ratio analysis beyond the measured θ range were not
  read.
- The KiDS-1000 list of explored scales is cut in the rendering read
  ("30–300 kpc, 50–500 kpc and 5…"); the remaining range was not read.
