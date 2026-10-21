# Weak lensing — physics and methods

Scope: what cosmic shear and galaxy–galaxy lensing measure, the estimators and
their defining equations, the theory models in current use, covariance,
likelihood and blinding practice, and the public codes.
Snapshot: 2026-10-12

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here. Equations in this file are textbook
definitions (Bartelmann & Schneider 2001, arXiv:astro-ph/9912508; Kilbinger
2015, arXiv:1411.0115; Mandelbaum 2018, arXiv:1710.03235) and carry no flag,
unless an equation number of a named paper follows them: `[src: Eq. 14]`
marks a form read in the body of that paper at that place.

## 1. What is measured
<!-- key: what-is-measured -->

Light from a source at comoving distance χ_s is deflected by the tidal field
of the matter along the line of sight. To first order the image distortion is
described by the convergence κ and the complex shear γ = γ1 + iγ2. For a
source population with normalised redshift distribution n_i(z), the
convergence is a weighted projection of the density contrast δ:

    κ_i(θ) = ∫ dχ q_i(χ) δ(χθ, χ),
    q_i(χ) = (3/2) Ωm (H0/c)² [χ / a(χ)] ∫_χ dχ' n_i(χ') (χ' − χ)/χ'      (flat space)

The observable in cosmic shear is the two-point function of galaxy
ellipticities between tomographic bins i and j. In the Limber approximation

    C_ℓ^{ij} = ∫ dχ q_i(χ) q_j(χ) / χ² · P_m(k = (ℓ + 1/2)/χ, z(χ)).

KiDS-Legacy writes the same projection with the comoving angular diameter
distance f_K in place of χ, P_m,nl evaluated at k = (ℓ + 1/2)/f_K(χ), and the
kernel W_G = (3 H0² Ωm / 2c²) [f_K(χ)/a(χ)] ∫_χ dχ' n_S(χ') f_K(χ' −
χ)/f_K(χ') (arXiv:2503.19441) [src: Eqs. 1–2]; DES Y3 and HSC Y3 write the
flat form above (arXiv:2105.13543 [src: Eq. 14]; arXiv:2304.00702 [src: Eqs.
15–16]). The papers that fixed this framework: the power spectrum of the
image distortion as a projection of the density power spectrum (Kaiser 1992,
doi:10.1086/171151, the reference KiDS-Legacy gives for both the Limber
projection and ξ± [sec: arXiv:2503.19441, Sect. 2.1 and 2.5.1]); its
generalisation to non-flat cosmologies and the growth of the signal with
source redshift (Kaiser 1998, arXiv:astro-ph/9610120) [src]; and tomography,
where auto- and cross-spectra of two or three redshift bins already improve
growth-related parameters by up to an order of magnitude (Hu 1999,
arXiv:astro-ph/9904153) [src]. The Limber and flat-sky approximations have
a negligible effect on parameters at the precision of CFHTLenS (Lemos et al.
2017, arXiv:1704.01054) [src]; KiDS-Legacy notes that Limber is poorer for
the alignment terms, whose kernels are more compact, but sufficient at ℓ ≳ 50
(arXiv:2503.19441) [src: Sect. 2.4].

Because the kernel is broad and proportional to Ωm, and the power spectrum to
σ8², cosmic shear constrains mainly the combination S8 ≡ σ8 (Ωm/0.3)^0.5; the
exponent that best matches the degeneracy direction is survey-dependent:
KiDS-Legacy finds α = 0.58 and quotes Σ8 = σ8(Ωm/0.3)^0.58 alongside S8
(Wright et al. 2025, arXiv:2503.19441) [src].

The measured ellipticity is an estimate of the reduced shear g = γ/(1 − κ),
not of γ; the difference is second order and is modelled explicitly in
third-order analyses (Linke et al. 2026, arXiv:2606.12389) [src].

Galaxy–galaxy lensing measures the mean tangential shear γ_t(θ) of sources
around lens galaxies, or the excess surface density ΔΣ(R) = Σ̄(<R) − Σ(R) =
Σ_crit γ_t when lens redshifts are known. ΔΣ needs a fiducial cosmology to
convert angles and redshifts into R and Σ_crit; γ_t(θ) does not. "3×2pt" is
the joint data vector of cosmic shear, galaxy–galaxy lensing and galaxy
clustering; "6×2pt" adds CMB lensing and its two cross-correlations (DES Y3 ×
SPT/Planck: arXiv:2203.12440, arXiv:2206.10824; DES Y3 × Planck PR4:
arXiv:2510.25596). Foundations: the first detection of galaxy–galaxy lensing,
a mean tangential polarisation of 0.011 ± 0.006 for 3202 lens–source pairs
(Brainerd, Blandford & Smail 1996, arXiv:astro-ph/9503073) [src]; the joint
use of galaxy–galaxy, galaxy–shear and shear–shear correlations between all
redshift bins to constrain dark energy together with the galaxy–halo relation
(Hu & Jain 2004, arXiv:astro-ph/0312395) [src]; a single two-point framework
with nuisance terms for shear errors, magnification, redshift errors,
alignments and theory errors (Bernstein 2009, arXiv:0808.3400) [src]; and
the self-calibration of alignments and galaxy bias, treated as free functions
of scale and redshift, from the same joint data vector (Joachimi & Bridle
2010, arXiv:0911.2454) [src].

## 2. Estimators
<!-- key: estimators -->

Each galaxy has a measured ellipticity ε = ε1 + iε2 and a weight w. Around a
direction joining two galaxies, the tangential and cross components are ε_t =
−Re(ε e^{−2iφ}) and ε_× = −Im(ε e^{−2iφ}). The correlation-function estimator
is

    ξ̂±^{ij}(θ) = Σ_ab w_a w_b [ε_t,a ε_t,b ± ε_×,a ε_×,b] / Σ_ab w_a w_b · 1/[(1 + m_i)(1 + m_j)]

for pairs ab in the angular bin, with the multiplicative calibration applied
to the ensemble, not per galaxy. For a metacalibration catalogue the factor (1
+ m) is replaced by the mean shear response ⟨R⟩ = ⟨R_γ⟩ + ⟨R_S⟩, the sum of
the shear response and the selection response, both measured from artificially
sheared images (Sheldon & Huff 2017, arXiv:1702.02601).

The theory relations are

    ξ±(θ) = (1/2π) ∫ dℓ ℓ J_{0/4}(ℓθ) [C_ℓ^{EE} ± C_ℓ^{BB}],

and the tangential shear around lenses of bin a with sources of bin i is

    γ_t^{ai}(θ) = (1/2π) ∫ dℓ ℓ J_2(ℓθ) C_ℓ^{g_a κ_i},   γ̂_t = Σ w_l w_s ε_t / Σ w_l w_s − (same around random points).

As the papers write the estimator: KiDS-Legacy puts the calibration in the
pair sum of the denominator, Σ_ab w_a w_b (1 + m_a)(1 + m_b), with m from
image simulations (arXiv:2503.19441) [src: Eq. 14]; DES divides by the mean
responses of the two bins, R^i R^j (arXiv:2602.10065) [src: Eq. 3], the
response being ⟨R⟩ = ⟨R_γ⟩ + ⟨R_s⟩ (arXiv:2105.13543) [src: Eq. 4]; HSC
correlates per-object shear estimates that already carry the calibration
(arXiv:2304.00702) [src: Eq. 11]. The Hankel relation above is Eq. 15 of
arXiv:2503.19441.

A lensing-only signal has C^{BB} = 0 to first order, so B modes are a null
test: the ellipticity field splits uniquely into a gradient and a curl part,
and lensing sources only the first (Crittenden et al. 2002,
arXiv:astro-ph/0012336) [src]. In NLA the intrinsic shape field is proportional to the tidal field,
giving

    P_GI(k,z) = −A_IA C1 ρ_crit Ωm / D(z) · [(1+z)/(1+z0)]^η P_m(k,z),   P_II = (same prefactor)² P_m,

with amplitude A_IA and redshift index η (Bridle & King 2007, arXiv:0705.0166;
conventions compared in Lamman et al. 2024, arXiv:2309.08605). The sign and
normalisation conventions of C1 differ between codes; check before comparing
A_IA across papers.

Forms and constants as the analyses write them. KiDS-Legacy: P_δI = −A_IA
(C1 ρ_cr Ωm / D(z)) P_m,nl with C1 ρ_cr ≈ 0.0134, no redshift term
(arXiv:2503.19441) [src: Eq. 6]; its fiducial NLA-M multiplies the amplitude
by f_r (⟨M_h⟩/M_piv)^β per bin, red fraction and mean halo mass, with M_piv =
10^13.5 h⁻¹M⊙ [src: Eq. 11]; NLA-z is linear in ⟨a⟩/a_piv − 1 with a_piv ≈
0.769 [src: Eq. 7]; NLA-k adds the density-weighting term of TATT with one
bias b_src [src: Eq. 9]. DES Y6: a₁(z) = −A₁ C̄₁ ρ_c Ωm/D(z)
[(1+z)/(1+z₀)]^η₁, a₂(z) = 5 A₂ C̄₁ ρ_c Ωm/D²(z) [(1+z)/(1+z₀)]^η₂, a₁δ =
b_TA a₁, with C̄₁ = 5 × 10⁻¹⁴ M⊙ h⁻² Mpc² (as printed; the dimensionally consistent unit
is h⁻² M⊙⁻¹ Mpc³, `deep/intrinsic-alignments.md`) and z₀ = 0.3; NLA is A₂ = η₂ = b_TA
= 0, giving P_GI = a₁ P_m and P_II = a₁² P_m (arXiv:2602.10065) [src: Eqs.
13–15]. HSC Y3 uses the same amplitudes with z₀ = 0.62 and one-loop terms
from FAST-PT (arXiv:2304.00702) [src: Eqs. 19–20]; the DES Y3 + KiDS-1000
joint analysis also takes 0.62 (arXiv:2305.17173) [src: Sect. 2.2]. In TATT
the II term has a B mode, the only one in the DES model (arXiv:2602.10065)
[src: Eq. 10].

## 3. Two-point statistics
<!-- key: two-point-statistics -->

| Statistic | Definition | Properties | Used by | Reference |
|---|---|---|---|---|
| ξ±(θ) | ⟨γ_t γ_t⟩ ± ⟨γ_× γ_×⟩ at separation θ; Hankel transforms of C_ℓ with J0 and J4 | simple, mask-insensitive estimator; mixes E and B modes and all ℓ, ξ− reaches very small scales | DES Y1/Y3/Y6, HSC, KiDS, UNIONS | Schneider et al. 2002, arXiv:astro-ph/0206182 |
| COSEBIs E_n, B_n | integrals of ξ± over a finite [θ_min, θ_max] with weights that separate E and B exactly | clean E/B split, compact data vector, well-defined scale range | KiDS-1000 fiducial; KiDS-Legacy 2+3pt; UNIONS B-mode test | Schneider et al. 2010, arXiv:1002.2136; Asgari et al. 2020, arXiv:1910.05336 |
| Band powers | band-averaged C_ℓ obtained from ξ± with apodised filters | approximately local in ℓ | KiDS-1000 (complementary), KiDS-Legacy | Asgari et al. 2021, arXiv:2007.15633; Joachimi et al. 2021, arXiv:2007.01844 |
| Pseudo-Cℓ | harmonic transform of the masked shear field, corrected by a mode-coupling matrix | natural for theory, needs noise-bias subtraction and mask handling | HSC, UNIONS, KiDS-Legacy cross-check | Hivon et al. 2002, arXiv:astro-ph/0105302; Alonso et al. 2019, arXiv:1809.09603 |

KiDS-Legacy compares the two-point statistics on the same catalogue as part of
its consistency tests (Stölzner et al. 2025, arXiv:2503.19442) [src]. UNIONS
validates B modes with three statistics (pure-mode ξ±^B, COSEBI B_n, C_ℓ^BB)
and finds that scale cuts do not translate between them (Daley et al. 2026,
arXiv:2604.03227) [src].

Definitions as written in KiDS-Legacy (arXiv:2503.19441): COSEBIs are E_n,
B_n = ½ ∫ dθ θ [T_+n(θ) ξ+(θ) ± T_−n(θ) ξ−(θ)] over [θ_min, θ_max], predicted
as E_n = ∫ dℓ ℓ/(2π) C_EE(ℓ) W_n(ℓ) with W_n(ℓ) = ∫ dθ θ T_+n(θ) J0(ℓθ)
[src: Eqs. 16–18]; band powers are C_l = (1/N_l) ∫ dℓ ℓ S_l(ℓ) C(ℓ) with a
top-hat response and N_l = ln(ℓ_up/ℓ_lo), which trace ℓ² C(ℓ) at the
logarithmic centre of the band and give up exact E/B separation for control
of the ℓ range [src: Eqs. 19–21]. HSC Y3 separates E and B in real space,
ξ+^{E/B}(θ) = ½ [ξ+(θ) ± ξ−(θ) ± ∫_θ^∞ dφ/φ ξ−(φ)(4 − 12 θ²/φ²)], with ξ±
measured from 0.2′ to 415′ and extrapolated beyond (arXiv:2304.00702) [src:
Eq. 12], and in harmonic space inverts ⟨C̃_ℓ⟩ = Σ M_ℓℓ' C_ℓ' with the
mode-coupling matrix of the mask (arXiv:2304.00701) [src: Eq. 16]. Earlier
steps: the aperture mass, whose dispersion is the power spectrum under a
narrow kernel (Schneider et al. 1998, arXiv:astro-ph/9708143) [src]; COSEBIs
in tomography, where a small number of modes saturates the information
(Asgari et al. 2012, arXiv:1201.2669) [src]; band-power estimators that are
linear in the binned ξ± and account for the window in real space (Becker &
Rozo 2016, arXiv:1412.3851) [src], the estimator of the DES Y6 B-mode test.
The J0 and J4 filters make ξ+ mix 1 ≲ ℓ ≲ 10⁴ and ξ− reach 10 ≲ ℓ ≲ 10⁵, the
reason KiDS-Legacy keeps ξ± out of its primary analysis (arXiv:2503.19441)
[src: Sect. 2.5.1].

A separate idea is to localise the lensing kernel: the
Bernardeau–Nishimichi–Taruya (BNT) transform builds combinations of
tomographic bins with narrow kernels so that a cut in ℓ becomes a cut in k
(first KiDS application: Gu et al. 2026, arXiv:2607.04384) [src].

## 4. Shape measurement
<!-- key: shape-measurement -->

See `systematics.md` sections 1–3. In brief: moments with PSF correction (KSB;
Kaiser, Squires & Broadhurst 1995, arXiv:astro-ph/9411005), model fitting
calibrated on image simulations (lensfit, arXiv:1210.8201; im3shape in DES SV
and Y1, arXiv:1507.05603 and arXiv:1708.01533; the HSC catalogues,
arXiv:1705.06745 and arXiv:2107.00136), and
self-calibrating estimators (metacalibration, arXiv:1702.02600 and
arXiv:1702.02601; metadetection, arXiv:1911.02505). Community blind challenges
began with STEP (Heymans et al. 2006, arXiv:astro-ph/0506112). The requirement
on PSF model accuracy is set in Paulin-Henriksson et al. 2008
(arXiv:0711.4886).

Foundations of the estimators and of the requirements: the geometry of shear
and ellipticity, optimal weighting and PSF correction with Gaussian-based
basis functions (Bernstein & Jarvis 2002, arXiv:astro-ph/0107431) [src]; the
Bayesian model-fitting method behind lensfit (Miller et al. 2007,
arXiv:0708.2340) [src]; noise bias, of the order of the inverse square of the
signal-to-noise ratio, a per cent at S/N = 10 (Refregier et al. 2012,
arXiv:1203.5050) [src]; the three generic error types, multiplicative and
additive shear errors and redshift-bin centroids, with a multiplicative
error below 1% and centroids to 0.003 for a SNAP-type survey, both scaling as
f_sky^−1/2 (Huterer et al. 2006, arXiv:astro-ph/0506030) [src]; the Stage-IV
allocation, additive A < 1.8 × 10⁻¹² and multiplicative M < 4.0 × 10⁻³
(Massey et al. 2013, arXiv:1210.7690) [src]. The linear model with PSF
leakage, ε_obs = (1 + m)(ε_int + γ) + α ε_PSF + c, is Eq. 24 of
arXiv:2503.19441.

## 5. Theory model of a current analysis
<!-- key: theory-model-of-a-current-analysis -->

| Ingredient | Choices in use | References |
|---|---|---|
| Linear P(k) | CAMB or CLASS (see `cosmo-software-ecosystem`) | — |
| Non-linear P(k) | HALOFIT (Smith et al. 2003, arXiv:astro-ph/0207664; revised by Takahashi et al. 2012, arXiv:1208.2701), HMcode (arXiv:1505.07833, arXiv:2009.01858), emulators (EuclidEmulator2, arXiv:2010.11288). KiDS-Legacy rates HMCode2020 at 2.5%, twice as accurate as Halofit, and recalls that Halofit over-predicts power at low S8 and so biases S8 low [src: Sect. 2.2 of arXiv:2503.19441] | section 5.1 for the choice of each analysis |
| Baryons | scale cuts; HMcode feedback parameter; baryonification emulators; PCA; external gas priors | `systematics.md` section 6 |
| Intrinsic alignments | NLA, TATT, halo-model or mass-dependent variants | `systematics.md` section 5 |
| Projection | Limber; corrections at low ℓ | arXiv:0809.5112, arXiv:1702.05301 |
| Galaxy bias (3×2pt) | linear bias with large-scale cuts, or non-linear bias with smaller cuts | DES Y6: R_min = 6 (4) h⁻¹Mpc for linear (non-linear) bias in γ_t (arXiv:2601.15175) [src]; 9 h⁻¹Mpc for w(θ) with linear bias, 4 with non-linear bias, at "nearly equal final precision" [src: Sect. IV.3 of arXiv:2601.14559] |
| Magnification | one coefficient per lens bin; in DES Y6 each carries a Gaussian prior [src: Table 3 of arXiv:2601.14559] | arXiv:2209.09782, arXiv:2601.14833 |
| Nuisance | m_i, Δz_i or n(z) realisations, IA parameters, bias parameters, baryon parameters | arXiv:2105.13548, arXiv:2601.14859 |

### 5.1 What each main analysis did
<!-- key: what-each-main-analysis-did -->

One row per analysis, read in its method sections. Priors and sizes of each
nuisance term are in `systematics.md`.

| Analysis | Statistic and scales | How the cuts were set | Power spectrum and feedback | Alignments | Covariance | Sampler and point estimate | Blinding |
|---|---|---|---|---|---|---|---|
| KiDS-1000 (arXiv:2007.15633) | COSEBIs, band powers and ξ± compared; 0.5′–300′ and five COSEBI modes [sec: arXiv:2503.19441, Sect. 2.5.2, 5.2.7] | data range | HMCode in its 2016 version, one feedback amplitude [sec: arXiv:2305.17173, Sect. 2.3] | NLA, one amplitude [src: Table 2] | σ_m folded into the covariance, bins fully correlated [src: Sect. 4.2.1] | S8 sampled directly with a flat prior on [0.1, 1.3], because a flat prior on A_s is informative on S8 [src: Sect. 3.2, Table 2] | three shear catalogues [sec: arXiv:2503.19441, Sect. 3.3] |
| DES Y3 cosmic shear (arXiv:2105.13543) | ξ±, 20 angular bins per pair, 227 of 400 points kept (166 in ξ+, 61 in ξ−) [src: Sect. VII.3, VII.6] | OWLS-AGN contamination of a synthetic vector: 3×2pt bias below 0.3σ in two dimensions, Δχ² < 0.5 for shear; a second, "ΛCDM-optimised" set keeps more scales and cuts the S8 error by about 1.5 [src: Sect. VII.3, XII] | CAMB + Halofit, gravity only [src: Sect. VII.3, VII.6] | TATT, five parameters [src: Table 2] | Gaussian part analytic with bin averaging and sky curvature, connected and super-sample parts from CosmoCov (Fang et al. 2020, arXiv:2004.04833), recomputed once at the best fit [src: Sect. III.3 of arXiv:2105.13544] | PolyChord (500 live points) in CosmoSIS, cross-checked with CosmoLike; marginal mean with 34% intervals, MAP from a separate maximiser [src: Sect. VII.6]; 6 cosmological and 19 systematic parameters [src: Sect. XII] | three stages: ellipticities rescaled through \|η\| = 2 arctanh\|e\| → f\|η\|, 0.9 < f < 1.1; data-vector transformation; hidden axes; criterion p > 0.01 [src: Sect. VI.3] |
| HSC Y3 real space (arXiv:2304.00702) | ξ± in 7 + 7 bins, 7.1′–56.6′ and 31.2′–248′, the same for all pairs, 140 points, S/N 26.6 [src: Sect. III.1] | small scales by the baryon modelling error, large scales of ξ+ by B modes [src: Sect. III.1, III.3] | linear spectrum from the BACCO emulator, HMCode 2016 with one feedback amplitude [src: Sect. IV.1.2, V.3.1] | TATT [src: Sect. IV.2] | 1404 ray-traced mocks at one cosmology, Hartlap-corrected [src: Sect. III.2, IV.6] | PolyChord for the result, MultiNest for the tests although its widths are about 10% too small, emcee as a check; 23 parameters [src: Sect. IV.6] | three catalogues with multiplicative offsets 0.05 apart (about 0.05 in S8) plus a per-team offset; no comparison with other results before unblinding; no change of method after it [src: Sect. II.2] |
| HSC Y3 harmonic space (arXiv:2304.00701) | pseudo-Cℓ with NaMaster, field by field, noise bias subtracted analytically, 300 < ℓ < 1800 [src: Sect. III, IV.3] | ℓ_min by the B modes below ℓ = 300 [src: Sect. IV.3] | — | — | the same 1404 mocks [src: Sect. IV.2] | — | — |
| DES Y3 + KiDS-1000 (arXiv:2305.17173) | — | DES "ΛCDM-optimised" cuts and their KiDS equivalent [src: Sect. 2.3] | HMCode2020 with free T_AGN [src: Sect. 2.3] | NLA with redshift power law, separate per survey [src: Sect. 2.2] | — | sampler comparison on DES Y3: PolyChord accurate within a few per cent, MultiNest 12% and 15% too narrow at 68% and 95% [src: App. D]; mean 0.790 and MAP 0.801 both quoted [src] | — |
| KiDS-Legacy (arXiv:2503.19441) | COSEBIs, six modes, 2′–300′ (fiducial) and eight band powers over 100 ≤ ℓ ≤ 1500; ξ± in an appendix only; all from ξ± measured with TreeCorr in 1000 bins [src: Sect. 2.5, 5.1] | 2′ taken from the joint DES + KiDS analysis; modes 7–20 add nothing [src: Sect. 5.2.7, 2.5.2] | CAMB + HMCode2020 through a CosmoPower emulator (at most 0.03σ from direct CAMB), one feedback parameter [src: Sect. 2.2, 5.1, 5.2.1] | NLA-M [src: Sect. 2.4.4] | analytic OneCovariance, C = C_G + C_NG + C_SSC + C_mult with C_G = sample variance + shape noise + mixed term, iterated to convergence in two steps [src: Eqs. 22–23, Sect. 5.2.3] | nautilus in CosmoSIS, Gaussian likelihood; quoted value is the marginal mode with highest-density interval, 0.815 +0.016/−0.021; mean 0.813 ± 0.018; MAP 0.811 +0.022/−0.015, found with Nelder–Mead [src: Sect. 5.1] | three catalogues, of which two are altered by up to ±2σ in S8, kept until after internal review; the paper notes that this scheme "hampered the diagnosis of subtle systematic effects" [src: Sect. 3.3] |
| DES Y6 cosmic shear (arXiv:2602.10065) | ξ± with TreeCorr in 26 bins over 2.5′–1000′, scales above 250′ unused; 267 points (NLA) or 282 (TATT) after cuts, S/N 83 before and 40 or 43 after [src: Sect. III] | bias in the marginal S8 below 0.5σ between gravity-only and BAHAMAS "hi AGN", per alignment model [src: Sect. IV.3] | CAMB + HMCode2020 with Θ_AGN fixed at 7.7 [src: Sect. IV.3] | NLA and TATT in parallel, decided before unblinding [src: Sect. IV.2] | CosmoCov: Gaussian, connected four-point and super-sample terms, recomputed at the 3×2pt MAP [src: Sect. III] | Nautilus (10,000 live points) in CosmoSIS; 19 or 21 parameters; goodness of fit p = 0.06 (NLA), 0.13 (TATT) [src: Sect. III, IV.4] | three stages; null tests first on the blinded vector [src: Sect. III] |
| DES Y6 3×2pt (arXiv:2601.14559) | ξ±, γ_t, w(θ); lens bin 2 dropped [src: Sect. IV.8] | 9 and 6 h⁻¹Mpc for w and γ_t with linear bias, 4 with non-linear bias; for ξ±, Δχ² < 5 against a no-feedback and a stronger-feedback vector, smallest θ_min about 3′ [src: Sect. IV.3] | HMCode2020 for the signal, Halofit in the covariance [src: Sect. IV.2] | TATT, linear galaxy bias in the fiducial run [src: App. D] | CosmoCov, with analytic marginalisation of observing-condition weights and of the point mass [src: Sect. IV.2] | Nautilus; mean with MAP in parentheses, and only parameters free of prior-volume shifts are quoted [src: Sect. IV.4, Table 4] | catalogue (factor 0.9–1.1 on arctanh e), data vector, then chains with hidden values and required Δ_PPD > 0.01; the covariance is recomputed at the still-blind MAP [src: Sect. IV.8] |

An alternative theory route keeps only perturbative scales and uses the
effective field theory of large-scale structure at two loops with lensing
counterterms and a spin-2 EFT for alignments (Chen et al. 2026,
arXiv:2603.28761) [src]. A simulation-based route fits clustering and lensing
to non-linear scales with an HOD on AbacusSummit (Lange et al. 2025,
arXiv:2512.15962) [src].

## 6. Covariance and likelihood
<!-- key: covariance-and-likelihood -->

Stage-III analyses use an analytic covariance with three terms: Gaussian
(including shape noise and the survey geometry), connected non-Gaussian
(trispectrum, from the halo model), and super-sample covariance (Takada & Hu
2013, arXiv:1302.6994). The Gaussian formulae for all second-order shear
measures, tomography included, are in Joachimi, Schneider & Eifler 2008
(arXiv:0708.0387) [src]; the connected term was first computed with the halo
model, where it raises parameter errors by about 15% for a survey to z ~ 1
(Cooray & Hu 2001, arXiv:astro-ph/0012087) [src]. Implementations: CosmoLike (Krause & Eifler 2017,
arXiv:1601.05779), the DES Y3 covariance (Friedrich et al. 2021,
arXiv:2012.08568), KiDS-1000 (arXiv:2007.01844), and OneCovariance for
KiDS-Legacy (Reischke et al. 2024, arXiv:2410.06962). When a covariance is
estimated from a finite number of mocks, the inverse must be debiased (Hartlap
et al. 2007, arXiv:astro-ph/0608064) or the likelihood replaced by the
appropriate t-distribution (Sellentin & Heavens 2016, arXiv:1511.05969); see
`cosmo-statistics-inference`.

The likelihood is Gaussian in the data vector. The covariance is evaluated at
a fiducial cosmology and usually iterated once at the best fit. The choice of
the data vector that enters the Gaussian term is not innocuous: in the
KiDS-Legacy k-cut analysis it moves S8 by about 0.08 (arXiv:2607.04384) [src].

Internal-consistency tests are part of the method: KiDS-Legacy applies three
tiers of metrics to splits by redshift, scale, colour and region
(arXiv:2503.19442) [src]; DES uses posterior-predictive distributions, in Y6
through a fast Gaussian-mixture metric Δ_PPD (Doux et al. 2026,
arXiv:2610.03447) [src].

## 7. Blinding
<!-- key: blinding -->

All Stage-III collaborations blind. KiDS blinds at the shear-catalogue level
(Kuijken et al. 2015, arXiv:1507.00738) [src]. DES developed a transformation
of the summary statistics themselves: the measured two-point functions are
shifted to values consistent with hidden shifted cosmological parameters while
internal consistency, measured by χ², is preserved (Muir et al. 2020,
arXiv:1911.05929) [src]. The KV450, DES Y3, HSC Y3, DES Y6 cosmic-shear and
HSC shear-ratio analyses all state that they were conducted blind
(arXiv:1812.06076, arXiv:2105.13543, arXiv:2304.00702, arXiv:2602.10065,
arXiv:2508.21681) [src]. What each scheme consists of is in the last column
of the table of section 5.1. Two lessons the papers draw: KiDS-Legacy found
that catalogue-level blinding prevents the direct comparison of shapes with
earlier catalogues, which delayed the diagnosis of its B modes
(arXiv:2503.19441) [src: Sect. 3.3]; DES Y6 went through three iterations of
blind inference before dropping a lens bin, under a plan written in advance
(arXiv:2601.14559) [src: Sect. IV.8].

## 8. Codes and pipelines
<!-- key: codes-and-pipelines -->

| Code | Purpose | Reference |
|---|---|---|
| TreeCorr | two- and three-point correlation functions | the paper usually cited is Jarvis et al. 2004, arXiv:astro-ph/0307393, whose subject is the aperture-mass skewness |
| NaMaster | pseudo-Cℓ for any pair of spin-0 or spin-2 fields, with contaminant deprojection and E/B purification | Alonso et al. 2019, arXiv:1809.09603 |
| CosmoSIS | modular parameter-estimation framework connecting CAMB, cosmic-shear modules and samplers | Zuntz et al. 2015, arXiv:1409.3409 |
| CosmoLike | likelihood and covariance for multi-probe analyses | arXiv:1601.05779 |
| CCL | theory predictions for LSST DESC | Chisari et al. 2019, arXiv:1812.05995 |
| OneCovariance | covariance of arbitrary two-point statistics | arXiv:2410.06962 |
| CosmoCov | real-space covariances with the 2D-FFTLog algorithm; used by DES Y3 and Y6 [src: arXiv:2105.13544 Sect. III.3; arXiv:2602.10065 Sect. III] | Fang et al. 2020, arXiv:2004.04833 |
| nautilus | importance nested sampling with neural-network proposals; KiDS-Legacy and DES Y6 [src: arXiv:2503.19441 Sect. 5.1; arXiv:2602.10065 Sect. IV.4] | Lange 2023, arXiv:2306.16923 |
| PolyChord | nested sampling with slice sampling; DES Y3 and HSC Y3. MultiNest reports inconsistent evidences and somewhat narrower intervals [src: arXiv:2202.08233] | Handley et al. 2015, arXiv:1506.00171; Lemos et al. 2023, arXiv:2202.08233 |
| GalSim | image simulation | Rowe et al. 2015, arXiv:1407.7676 |
| ngmix | Bayesian shear measurement; one of the two DES SV pipelines (arXiv:1507.05603) | Sheldon 2014, arXiv:1403.7669 |
| PIFF | PSF modelling in DES Y3 and Y6; default PSF software planned for Rubin weak lensing [src: arXiv:2501.05781] | arXiv:2011.03409, arXiv:2501.05781 |
| HMcode, BCemu, BACCO | non-linear and baryonic power spectra | arXiv:2009.01858, arXiv:2108.08863, arXiv:2011.15018 |

## 9. Conventions that split the community
<!-- key: conventions-that-split-the-community -->

- **Point estimate.** Marginal mean, marginal mode, or maximum a posteriori.
  KiDS-1000 warned that marginal S8 point estimates "are easily misinterpreted
  to be biased low" and proposed an alternative estimator and credible
  interval (arXiv:2007.01844) [src]. In the DES Y3 + KiDS-1000 joint analysis
  the marginal mean is 0.790 and the MAP 0.801, a difference caused by
  skewness and projection effects (arXiv:2305.17173) [src]. State which
  estimate a number is. By survey: KiDS-Legacy quotes the marginal mode with
  its highest-density interval [src: Sect. 5.1 of arXiv:2503.19441]; DES Y3
  and Y6 the marginal mean, with the MAP beside it [src: Sect. VII.6 of
  arXiv:2105.13543; Table 4 of arXiv:2601.14559]. In DES Y6 the cosmic-shear
  mean with TATT is 0.783 and its MAP 0.763; for 3×2pt, 0.789 and 0.793 [src:
  Table 4 of arXiv:2601.14559].
- **S8 exponent.** 0.5 by convention; the best-constrained combination has a
  survey-dependent exponent (0.58 for KiDS-Legacy) [src: arXiv:2503.19441].
- **Tension metric.** One-dimensional S8 difference, full-parameter-space
  shift, or evidence-based; DES Y6 quotes two for the same data (2.6σ and
  1.8σ) (arXiv:2601.14559) [src].
- **Sign of the redshift shift.** DES writes n_i(z) → n_i(z − Δz_i) [src: Eq.
  23 of arXiv:2105.13543], HSC n_i(z) → n_i(z + Δz_i) [src: Eq. 22 of
  arXiv:2304.00702], so a negative HSC shift means a higher true redshift;
  KiDS defines δz as estimated minus true mean [src: Eq. 3 of
  arXiv:2503.19440].
- **Feedback parameter.** HMCode 2016: A_b from 2 to 3.13, the upper end
  being dark matter only [src: Sect. IV.1.2 of arXiv:2304.00702]. HMCode2020:
  log₁₀ T_AGN, with 7.3 close to dark matter only [src: Sect. 5.2.7 of
  arXiv:2503.19441]. The two scales run in opposite directions.
- **Magnification coefficient.** Two definitions differing by a factor 2
  appear in the DES Y6 papers; see `systematics.md` section 7.
- **ΔΣ or γ_t.** ΔΣ embeds a fiducial cosmology and h-dependent units (h M⊙
  pc⁻²); γ_t does not.
- **Ellipticity definition.** |ε| = (a − b)/(a + b) or |e| = (a² − b²)/(a² +
  b²); the responsivity differs by about a factor two.
- **n_eff and σ_ε.** Several definitions of effective source density exist;
  quote the one the survey paper uses.

## Not verified
<!-- key: not-verified -->

- The sampler, the non-linear model and the blinding of the HSC Y3
  harmonic-space analysis (arXiv:2304.00701, Sect. II.2 and V not read), and
  the sampler of KiDS-1000.
- The statistic and covariance of the DES Y3 + KiDS-1000 joint analysis
  (arXiv:2305.17173, Sect. 2.4 to 2.6 not read).
- Methods of DECADE and UNIONS beyond their abstracts.
- Kaiser 1992 (doi:10.1086/171151) is not on arXiv; its content is given
  here as KiDS-Legacy cites it, and its title was confirmed on Crossref.
