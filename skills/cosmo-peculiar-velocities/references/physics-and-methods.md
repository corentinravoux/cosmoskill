# Physics and methods — peculiar-velocity estimators and their defining equations

Scope: the observables, estimators, covariance models and likelihoods used in direct
peculiar-velocity cosmology, with the equations as the cited papers write them, their range of
validity, and the public codes. Snapshot: 2026-10-07

Not repeated here: the indicators, the surveys and the four **method families** with the
classification of every published fσ8, which are in
`pv-surveys.md`
(§1–5). This file gives what stands behind each family.

Equations are transcribed from the LaTeX source of the cited paper, read this session, in that
paper's notation: symbols differ between sections.

## 1. The observable: log-distance ratio, and the velocity estimators built on it
<!-- key: the-observable-log-distance-ratio-and-the -->

**What is measured.** A distance indicator gives a distance modulus or a physical size with an error
that is Gaussian in the logarithm of the distance. The natural observable is the log-distance ratio

    η_i = log10[ D(z_obs,i) / D(z_cos,i) ]

with D the comoving radial distance, z_obs the observed and z_cos the cosmological redshift (Ravoux
et al. 2025, arXiv:2501.16852, §3.2) [src]. Johnson et al. 2014 (arXiv:1404.3799) state the reason
it must be used: the intrinsic scatter of the FP and TF relations "is only Gaussian in logarithmic
distance units; wrongly assuming it is Gaussian in linear (velocity) units can bias cosmological
constraints" [src: abstract].

**Redshift composition.** Redshifts multiply, they do not add: (1 + z) = (1 + z̄)(1 + z_p) (Davis &
Scrimgeour 2014, arXiv:1405.0105, their eq. for the total redshift) [src]. The classic approximation
v_p = cz − H0 D "overestimates peculiar velocity by ~100 km/s at z ~ 0.04" [src: abstract]. The
low-redshift expansion of the recession velocity they recommend is

    v(z) = cz/(1+z) · [ 1 + ½(1 − q0) z − ⅙(1 − q0 − 3q0² + j0) z² ]

[src: arXiv:1405.0105, eq. "taylor"].

**Velocity estimators in use.** All of them linearise η → v; they differ in the prefactor.

| Name | Estimator | Source | Flag |
|---|---|---|---|
| naive | v = cz − H0 r_e | criticised in Watkins & Feldman 2015, arXiv:1411.6665, and arXiv:1405.0105 | [src] |
| Watkins–Feldman | v = [c z_mod /(1 + z_mod)] · ln( c z_mod / H0 r_e ), with z_mod = z[1 + ½(1 − q0)z − ⅙(1 − q0 − 3q0² + 1)z²]; error δv = c z_mod δl /(1 + z_mod) | arXiv:1411.6665, eq. "vest" | [src] |
| log-distance (flip) | v_i = ln(10) · D(z_obs,i) H(z_obs,i) /(1 + z_obs,i) · η_i | arXiv:2501.16852, eq. "etatovel" | [src] |
| Hubble-residual (flip) | v_i = −(c ln10 / 5) · J(p_i) · Δμ_i, with J one of four forms: "Watkins" z/(1+z); "low-z" z; "Hubble high-order" (the q0, j0 expansion above divided by 1+z); "full" [ (1+z)c / ((H(z)/h) D(z)) − 1 ]⁻¹ | arXiv:2501.16852, eq. "dmutovel" and Table "velest" | [src] |
| Davis–Scrimgeour | v_DS = c (z − z_l)/(1 + z_l), z_l the redshift solving d_L(z_l) = measured distance | as used by Wang et al. 2026, arXiv:2604.08314, eq. "velocity_hz" | [src] |
| Bayesian, non-linearised | posterior on v from the SN magnitude without assuming local linearity of the magnitude–redshift relation or a fixed cosmology; lower bias at large v_p/cz | Upadhyay, Saini & Sethi 2026, arXiv:2603.06469 | [src] |

The Watkins–Feldman estimator is unbiased only if the **true** velocity is small compared with cz;
the estimated one may be several thousand km/s [src: arXiv:1411.6665, text after eq. "vest"]. In the
paper's eq. "vmod" the jerk is set to 1 (the term reads "+1" where arXiv:1405.0105 writes j0) [src].

**Size of the velocity error.** δv ≈ ε H0 r for a fractional distance error ε: σ_n = 0.324 H0 d_z
for 6dFGSv and 0.177 H0 d_z for 2MTF [src: arXiv:1804.05520, eqs. "dcz1", "dcz2"]; mean η error 0.12
(FP) and 0.11 (TF) in DESI DR1 [src: arXiv:2512.03229, §2].

**Distance debiasing.** Exponentiating a Gaussian modulus biases the distance: d_c = 10^(μ/5 − 5) ·
exp(−(κ σ_μ)²/2), κ = ln10/5 [src: arXiv:2604.08314, eq. "corrected_distance"]. Qin 2021
(arXiv:2105.04800) instead Gaussianises the velocities with a power transform tied linearly to the η
error [src: abstract].

## 2. Linear model of the density and velocity power spectra
<!-- key: linear-model-of-the-density-and-velocity-power -->

The model that every likelihood analysis descends from is Koda et al. 2014 (arXiv:1312.1022), who
introduced a redshift-space damping of the velocity field that earlier work had set to 1:

    P^s_gg(k, μ) = (1 + 2 r_g β μ² + β² μ⁴) D_g² b² P_mm(k)
    P^s_gu(k, μ) = i aHf μ (r_g + β μ²) D_g D_u b P_mθ(k) / k
    P^s_uu(k, μ) = (aHf μ / k)² D_u² P_θθ(k)
    D_g(k, μ)²  = [1 + (k μ σ_g)² / 2]⁻¹         (Lorentzian)
    D_u(k)      = sin(k σ_u) / (k σ_u)           (sinc, empirical)

with β = f/b, r_g the galaxy–matter cross-correlation coefficient, and u the line-of-sight velocity
[src: arXiv:1312.1022, eqs. "pgg_zspace", "pgu_zspace", "puu_zspace", "du"].

- σ_u ≈ 13 h⁻¹Mpc at z = 0 "with a small dependence on halo mass"; best fit 13.0 h⁻¹Mpc, with σ_g =
  5.8 h⁻¹Mpc for the density [src: same section].
- Validity: "these equations hold only on large scales, k ≲ 0.2 h Mpc⁻¹"; the sinc formula "applies
  to scales k ≤ 0.2 h Mpc⁻¹" [src].
- The damping is **not** explained by random velocities: "This damping in velocity is much larger
  than that naively expected"; the authors "leave explanations of this strong damping to future
  studies" [src]. D_u is a fit to simulations, not a derived result.
- The velocity has no Kaiser term: "Unlike the density or the momentum, the velocity does not have
  the squashing term" [src].

The fitted amplitude is fσ8 because P_θθ and P_mθ are normalised by the fiducial σ8²; in the flip
decomposition the velocity term has coefficient A_vv = (fσ8)² multiplying (aH)² μ1 μ2 / k² · P_θθ(k)
D_u²(k, σ_u) [src: arXiv:2501.16852, §3.1].

**Beyond the empirical damping.** Chen et al. 2025 (arXiv:2508.00066): 1-loop Lagrangian and
Eulerian EFT for redshift-space pairwise velocity statistics up to the second moment, "with a
consistent set of EFT coefficients" shared with the density; velocities need "a variation on the
usual infrared (IR) resummation procedure"; growth rate recovered on N-body "at better than percent
level precision"; code `velocisaurus` [src]. Dumerchat et al. 2026 (arXiv:2602.03382): HOD emulators
trained on AbacusSummit for the non-linear regime [src].

## 3. Field-level likelihood ("maximum-likelihood fields")
<!-- key: field-level-likelihood-maximum-likelihood-fields -->

**Principle.** The data vector S (gridded galaxy overdensities and log-distance ratios or
velocities) is taken as Gaussian with zero mean and covariance C(Θ) = C_field(Θ) + C_obs; the
likelihood is maximised or sampled, and no summary statistic is measured. Origin: Johnson et al.
2014 (arXiv:1404.3799, velocity only, fσ8(k)); Adams & Blake 2017 (arXiv:1706.05205, first
density–velocity cross-covariance); Adams & Blake 2020 (arXiv:2004.06399, RSD in the density term)
[src: abstracts].

**Covariance from the power spectrum.** For two fields a, b at positions r1, r2,

    C_ab(r1, r2) = (2π)⁻³ ∫ d³k  P_ab(k, μ1, μ2) e^{i k·r}

with μ1, μ2 the cosines to the two lines of sight. The flip framework (arXiv:2501.16852, §2.2)
writes any model as

    P_ab(k, μ1, μ2) = Σ_n A_ab,n  B_ab,n(k, μ1, μ2)  P_ab,n(k)
    C_ab            = Σ_n A_ab,n  C_ab,n
    C_ab,n          = Σ_{ℓ,ℓ1,ℓ2} N^{ℓ1 ℓ2}_{ab,n,ℓ}(φ, α) · H_ℓ[ P_ab,n(k) M^{ℓ1 ℓ2}_{ab,n}(k) ](r)
    M^{ℓ1 ℓ2}(k)    = ¼ ∫∫ dμ1 dμ2  B(k, μ1, μ2) L_ℓ1(μ1) L_ℓ2(μ2)
    H_ℓ[f](r)       = i^ℓ ∫ k² dk / (2π²)  j_ℓ(kr) f(k)

[src: eqs. "Pwflip", "sum_cov", "cov_flip_wa", "mlldef"]. The A_n are the fitted parameters, so each
C_ab,n is computed once; the angular terms N and M are integrated analytically (sympy), the Hankel
transform by FFTLog; α is the angle between the two lines of sight and φ the angle between the
separation vector and the reference direction [src].

**The velocity–velocity term in closed form** (wide-angle, linear, one term):

    C_vv(r1, r2) = (aH fσ8)² / (2π²) ∫ dk  P_θθ(k) D_u²(k, σ_u)
                   × [ j0(kr) cos α / 3 − j2(kr) (3 cos 2φ + cos α) / 6 ]

"the mathematical equivalency is only valid when the line-of-sight reference is the bisector" [src:
arXiv:2501.16852, §3.1].

**Named covariance models** (as flip labels them) [src: arXiv:2501.16852, §3.1]:

| Label | Paper | Content | Limitation stated |
|---|---|---|---|
| AB17 | arXiv:1706.05205 | gg, gv, vv; density **without** RSD; wide-angle | no RSD in the density |
| AB20 | arXiv:2004.06399 | RSD in gg and gv | plane-parallel: "breaks for large-area surveys at low redshift" |
| C23 | Carreres et al. 2023, arXiv:2303.01198 | vv only, the wide-angle vv of AB17 | velocity only |
| L22 | Lai, Howlett & Davis 2023, arXiv:2209.04166 | wide-angle with RSD; Finger-of-God exp[−(kμσ_g)²/2] Taylor-expanded to order p = 4 so that σ_g stays a linear parameter | needs kμσ_g ≪ 1, "typically k < 0.1 h Mpc⁻¹"; a separate nuisance amplitude for 0.2 < k < 1.0 h Mpc⁻¹ |
| RC25 | arXiv:2501.16852 | wide-angle with RSD and no Taylor expansion | σ_g cannot be a linear coefficient: covariances are pre-computed on a σ_g grid and interpolated |

**Likelihood with the zero-point marginalised.** Lai et al. 2023 (arXiv:2209.04166) marginalise
analytically over an additive offset in η with Gaussian prior width σ_y; as used on DESI DR1
(arXiv:2512.03229, eq. 32):

    P(S|m) = [ (2π)^n |C(m)| ]^{-1/2} (N_x σ_y)⁻¹ exp{ −½ [ Sᵀ C⁻¹ S − N_y²/N_x² ] }
    N_x = sqrt( xᵀ C⁻¹ x + 1/σ_y² ),   N_y = Sᵀ C⁻¹ x

with x = 1 for a log-distance entry and 0 for a density entry, and σ_y = 0.005 for DESI DR1 [src:
arXiv:2512.03229, §3.3]. Johnson et al. 2014 introduced the analytic marginalisation over zero-point
errors and a matrix "hyper-parameter" scheme to combine correlated velocity surveys [src:
arXiv:1404.3799, abstract].

**Practice on DESI DR1** (arXiv:2512.03229) [src: body, §2–5]:

- Configuration: 20 h⁻¹Mpc grid; σ_u = 16 h⁻¹Mpc with density + velocity and 10 h⁻¹Mpc with velocity
  only, set on mocks; "the gridding kernel and the RSD damping are degenerate" [src: §3–4, figure
  captions].
- σ_u is fixed (not sampled): the systematic from fixing it is estimated by finite difference,
  ∂fσ8/∂σ_u · δσ_u = 0.018, "around 30 % of the statistical uncertainty"; sampling it would need
  covariances pre-computed on a σ_u grid, and "fixing σ_u already requires around ~140 GB of
  memory".
- Cells with δ_g > 10 are removed as ones "that our quasi-linear theory cannot accurately model" (41
  of 2 023 cells, about 2 %, in the configuration of its appendix), and a 4σ cut on η removes
  outliers.
- The likelihood is "a combination of a Gaussian and a non-Gaussian part, arising from marginalising
  over the zero-point", which makes the posterior of small samples asymmetric.
- The algorithm was rewritten in JAX for the DR1 sample size [src: abstract].

**Cost.** The covariance is dense and N × N: DESI DR1 needed a gridded density field and a fixed
σ_u. The DESI BGS × ZTF simulation study (Ravoux et al. 2026, arXiv:2609.34508) applies "a
wide-angle likelihood-based field-level inference" while "varying the different density and velocity
field configurations" [src: abstract].

## 4. Two-point statistics measured and then fitted
<!-- key: two-point-statistics-measured-and-then-fitted -->

### 4a. Momentum power spectrum
<!-- key: momentum-power-spectrum -->

The radial momentum field is the density-weighted velocity, ρ(r) = [1 + δ_g(r)] v(r); its power
spectrum is the velocity power spectrum plus three higher-order terms, ⟨uu⟩ + ⟨uδu⟩ + ⟨δuu⟩ + ⟨δuδu⟩
(Howlett 2019, arXiv:1906.02875, eq. "mom") [src]. It is used because it needs no volume weighting
of a sparsely sampled velocity field. Estimator:

    F^p(r)        = w(r) n_g(r) u(r) / A
    P̂^p_ℓ(k)     = |F^p_ℓ(k)|² − N^p_ℓ(k)
    N^p_ℓ(k)      = ∫ d³r  w²(r) n̄(r) ⟨v²(r)⟩ L_ℓ(k̂·r̂),   ⟨v²⟩ = (1/N) Σ u²

[src: arXiv:1906.02875, eqs. "momfield", "shot-noise" and following]. The shot noise contains the
**measured** velocity variance, i.e. the measurement errors: it is the dominant term for TF/FP
samples. Linear limit:

    P^p_L(k, μ) ≈ μ² f² (aH)² k⁻² P_L(k)
    P^p_{L,0} = f²(aH)² P_L / (3k²),   P^p_{L,2} = 2 f²(aH)² P_L / (3k²)

[src: arXiv:1906.02875]; the Gaussian covariance has the FKP form with P^p + ⟨v²⟩/n̄ in place of P +
1/n̄ [src: eq. "covgauss"]. Applications: Qin, Howlett & Staveley-Smith 2019 (arXiv:1906.02874, 2MTF
+ 6dFGSv); Qin et al. 2024 (arXiv:2411.09571, adds the density–momentum **cross** spectrum on SDSS
PV); Qin et al. 2025 (arXiv:2512.03231, DESI DR1, generalised to density and momentum from distinct
surveys) [src: titles and abstracts].

DESI DR1 configuration (arXiv:2512.03231) [src: conclusions]: data vector [P^δ_0, P^δ_2, P^p_0,
P^δp_1]; free parameters [fσ8, b1σ8, b2σ8, σ²_vT, σ²_vS]; models validated on mocks to k_max = 0.3 h
Mpc⁻¹ for that set (0.25 when P^p_2 and a momentum bias are added); window convolution through a
matrix built from randoms on a 140³ grid in a 700 h⁻¹Mpc box; **the momentum spectrum is fitted only
to k ≤ 0.1 h Mpc⁻¹** because "the systematic bias of FP data enhances the measured momentum power
spectrum at k > 0.1 h Mpc⁻¹".

The *velocity* (not momentum) power spectrum was estimated directly by Howlett et al. 2017
(arXiv:1706.05130, 2MTF) [src: title].

### 4b. Velocity and momentum correlation functions
<!-- key: velocity-and-momentum-correlation-functions -->

The statistics go back to Gorski 1988 (doi:10.1086/185255) and Gorski et al. 1989
(doi:10.1086/167771). The pair estimators of the parallel and perpendicular velocity correlations
are

    Ψ̂∥(r) = [ Σw g² · Σw f u1u2 − Σw fg · Σw g u1u2 ] / [ Σw f² · Σw g² − (Σw fg)² ]
    Ψ̂⊥(r) = [ Σw f² · Σw g u1u2 − Σw fg · Σw f u1u2 ] / [ Σw f² · Σw g² − (Σw fg)² ]

with f, g the geometric factors of each pair, and their linear predictions

    Ψ∥(r) = (f H0)²/(2π²) ∫ dk P(k) [ j0(kr) − 2 j1(kr)/(kr) ]
    Ψ⊥(r) = (f H0)²/(2π²) ∫ dk P(k)   j1(kr)/(kr)

[src: arXiv:2604.08314, eqs. "psipar", "psiperp" and following]. The measured ψ1, ψ2 are
survey-geometry-dependent mixtures, ψ1(r) = A(r) Ψ∥ + [1 − A(r)] Ψ⊥ and ψ2(r) = B(r) Ψ∥ + [1 − B(r)]
Ψ⊥ [src: Turner et al. 2025, arXiv:2512.03230, §3], so **the model must be built with the survey's
own A(r), B(r)**; two surveys' ψ1 are not comparable.

DESI DR1 configuration (arXiv:2512.03230) [src: body]: five statistics ψ1, ψ2, ξ⁰_gg, ξ²_gg, ξ¹_gu
in 6 h⁻¹Mpc bins; fit range 24–120 h⁻¹Mpc (16 bins each, 80 × 80 covariance from all 675 mocks);
model from density and momentum power spectra at 1-loop Eulerian perturbation theory. The lower
bound is a compromise: 12 h⁻¹Mpc is "strictly closest to the fiducial cosmology" on mocks but "leads
to a poor goodness-of-fit". Earlier applications: Turner, Blake & Ruggeri 2023 (arXiv:2207.03707,
6dFGS) [src: title].

A **linear template biases this family low** (Tonegawa et al. 2024, arXiv:2309.14457; 5.2 % on HR4
mocks per `fsigma8-pv-compilation.md` [sec]), and finite mock volumes suppress large-scale velocity
correlations (`systematics.md` §8).

### 4c. Supernova magnitude covariance
<!-- key: supernova-magnitude-covariance -->

The same signal written as a covariance of SN magnitude residuals: Hui & Greene 2006
(arXiv:astro-ph/0512159; ignoring it underestimates a low-z anchor's zero-point error "by about a
factor of 2"); first detection, σ8 = 0.79 ± 0.22, by Gordon, Land & Slosar 2007 (arXiv:0705.1718);
standard Hubble-diagram treatment in Davis et al. 2011 (arXiv:1012.2912); growth fits in Huterer et
al. 2017 (arXiv:1611.09862) and Crisman et al. 2026 (arXiv:2604.06361) [src: abstracts and titles].
Its role as a *nuisance* in SN cosmology belongs to `cosmo-supernovae`.

## 5. Velocity–density comparison and forward models
<!-- key: velocity-density-comparison-and-forward-models -->

**Linear comparison.** The velocity field is predicted from a redshift-survey density field by
linear theory and scaled by β = f/b; with σ8 of the galaxies measured in the same field this gives
fσ8 normalised to the **linear** σ8. Reference analyses: Pike & Hudson 2005
(arXiv:astro-ph/0511012), Carrick et al. 2015 (arXiv:1504.04627, 2M++: β* = 0.431 ± 0.021 → Ω_m^0.55
σ8,lin = 0.401 ± 0.024), Boruah, Hudson & Lavaux 2020 (arXiv:1912.09383), Said et al. 2020
(arXiv:2007.04993: β = 0.341 ± 0.024 from 15 894 FP galaxies), Stahl et al. 2021 (arXiv:2105.05185),
Lilow & Nusser 2021 (arXiv:2102.07291), Boubel et al. 2024 (arXiv:2301.12648) [src: abstracts].
Classical formalism, including Malmquist bias: Strauss & Willick 1995 (arXiv:astro-ph/9502079).

**Calibration of the method on mocks.** Hollinger & Hudson 2024 (arXiv:2312.03904) and Dixon et al.
2026 (arXiv:2606.14962); numbers in `systematics.md` §6.

**Forward-modelling the distance indicator.** VIRBIUS (Lavaux 2016, arXiv:1512.04534) samples true
distances, the 3D velocity field and calibration parameters jointly, handling selection and
miscalibration [src: abstract]. Stiskalek 2025 (arXiv:2509.20235) and Stiskalek, Desmond & Lavaux
2025 (arXiv:2509.14997) calibrate each indicator jointly with a linear-theory reconstruction and
marginalise over distances [src: abstracts]. In all of these the velocity field is still linear.

**Forward-modelling the field.** Graziani et al. 2019 (arXiv:1901.01818, CF3, linear); Boruah,
Lavaux & Hudson 2022 (arXiv:2111.15535, inhomogeneous Malmquist corrections); Valade et al. 2026
(arXiv:2602.03699, Hamlet-PM: particle-mesh dynamics on CF4 to z < 0.05, 100 constrained 512³ runs
in 500 h⁻¹Mpc boxes); Nusser 2026 (arXiv:2606.08593, Zel'dovich MAP reconstruction of 2MRS with an
unbinned Poisson likelihood, tested on CF4 groups); BORG (Jasche & Lavaux 2019, arXiv:1806.11117)
and Manticore-Local (McAlpine et al. 2025, arXiv:2505.10682) on the density side [src: abstracts,
titles]. None quotes fσ8 (`pv-surveys.md` §5).

**Machine-learned reconstruction.** Gong & Bean 2026 (arXiv:2606.05047): a gradient-boosted tree and
a Transformer trained on AbacusSummit to predict the residual between true and linear-theory
velocity; used for kSZ stacking (§7) [src].

## 6. Bulk-flow estimators
<!-- key: bulk-flow-estimators -->

**Two definitions that coincide only for a uniform field** (Nusser 2016, arXiv:1508.03860) [src:
abstract]: the volume average of the 3D velocity,

    U_i = (1/V) ∫_V v_i d³r,

and the dipole of the radial component with a radial weight. Nusser 2014 (arXiv:1405.6271) showed
that the maximum-likelihood estimator, which assumes a constant velocity in the volume, is
"inconsistent with the definition of the bulk flow as the average of the peculiar velocity field"
even for ideal data [src: abstract]. For an irrotational field the exact relation is

    U_i = (R²/V) ∫_V  s(r) r̂_i / r²  d³r,     s = v·r̂

i.e. an r⁻² weighting of radial velocities (Peery, Watkins & Feldman 2018, arXiv:1808.07772, eq.
"rad") [src].

**Kaiser maximum-likelihood estimator** (Kaiser 1988, doi:10.1093/mnras/231.2.149):

    L(B, σ*) = Π_n [2π(σ_n² + σ*²)]^{-1/2} exp{ −(v_n − B·r̂_n)² / [2(σ_n² + σ*²)] }
    B_i = Σ_n w_{n,i} v_n,   w_{n,i} = Σ_j A⁻¹_ij r̂_{n,j} / (σ_n² + σ*²),
    A_ij = Σ_n r̂_{n,i} r̂_{n,j} / (σ_n² + σ*²)

with σ* the 1D non-linear dispersion, "usually assumed to be ~300 km/s" [src: as written in
arXiv:1804.05520, §3]. Its window is whatever the survey gives; its depth is the error-weighted
depth, typically shallow.

**ηMLE** (Qin et al. 2018, arXiv:1804.05520): the same likelihood written in the observable,

    P(η | B) = Π_i [2π(ε_i² + ε*,i²)]^{-1/2} exp{ −(η̃_i(B) − η_i)² / [2(ε_i² + ε*,i²)] }
    ε*,i = (1 + z_i) σ* / [ ln(10) H(z_i) d_z,i ]

"preserves the Gaussian nature of the measurement errors and … does not require any assumption on
the unknown magnitude of a galaxy's velocity compared to its redshift"; no analytic maximum, so it
is sampled [src: eqs. "pvpi" and following].

**Minimum-variance (MV) estimator** (Watkins, Feldman & Hudson 2009, arXiv:0809.4041; Feldman,
Watkins & Hudson 2010, arXiv:0911.5516): choose weights so that u_i = Σ_n w_{i,n} S_n minimises
⟨(U_i − u_i)²⟩, where U_i is the moment of an *ideal* survey with the chosen window. With the
constraints Σ_n w_{i,n} r̂_{n,j} = δ_ij (a uniform flow is recovered) and Σ_n w_{i,n} cz_n = 0
(independence of H0),

    w_{i,n} = Σ_m G⁻¹_nm [ ⟨S_m U_i⟩ − ½ Σ_j λ_ij r̂_{m,j} − ½ β_i cz_m ],
    G_nm = ⟨S_n S_m⟩

[src: arXiv:1808.07772, eqs. "up", "Hconstraint", "w"]. G and ⟨S U⟩ are computed from a **fiducial
power spectrum** — the method "require[s] a prior expressed in terms of the radial velocity
correlation function" (arXiv:1508.03860) [src] — so the MV estimate carries a ΛCDM prior on the
velocity correlations, which is what Duangchan et al. 2025 (arXiv:2507.22236) remove with a forward
model "assuming only a flat Universe" [src: abstract].

**Wiener filter / constrained realisations** (Hoffman, Courtois & Tully 2015, arXiv:1503.05422):
top-hat flow from a Wiener-filtered 3D field, "determined by the tension between the observational
data and the assumed prior model" and data-dominated only where cosmic variance exceeds the variance
of the constrained realisations (to R ~ 200 h⁻¹Mpc in Cosmicflows-2) [src]. ACE (Nusser & Davis
2011, arXiv:1101.1650) is a related all-space constrained estimate.

**Estimator performance on mocks** (arXiv:2306.11269): unbiased, precision tied to survey geometry,
analytic errors "typically underestimated" [src]. The record is in `results.md` §3.

## 7. kSZ velocities, at the level relevant here
<!-- key: ksz-velocities-at-the-level-relevant-here -->

The kinematic Sunyaev–Zel'dovich effect measures the electron momentum along the line of sight: it
gives **τ × v**, never v alone. Three estimators are in use — pairwise kSZ, velocity-weighted
stacking, and kSZ velocity reconstruction (kSZ tomography) — each with its own degeneracy (mean
optical depth τ̄, accuracy of the stacking velocity, velocity bias b_v). They are tabulated with the
2025–2026 measurements in `results.md` §4. The point to retain: b_v is measured at ≈ 0.3–0.45
(arXiv:2506.21657, arXiv:2511.15701), so the *amplitude* of the velocity field, hence fσ8, is not
measurable by kSZ alone; kSZ velocities constrain shapes (f_NL, the force-law index) and gas
physics. Gas physics and the CMB side belong to `cosmo-cmb-lss-cross-correlations`.

## 8. Covariance, mocks, consensus, blinding practice and codes
<!-- key: covariance-mocks-consensus-blinding-practice -->

- **Field-level**: the covariance *is* the model; it is analytic, dense, N × N, and recomputed (or
  interpolated) for every non-linear parameter. Errors come from the posterior, and are checked
  against mock scatter: on DESI DR1 FP mocks the mean posterior error (0.064) matches the scatter of
  best fits (0.063) [src: arXiv:2512.03229, §4].
- **Two-point**: covariance from mocks (675 for DESI DR1, 2 048 for SDSS PV, 100 with a Hartlap
  factor in arXiv:2604.08314), or the Gaussian analytic form for the momentum spectrum (§4a).
- **Mocks** must reproduce the density sample, each distance indicator with its scatter and
  selection, and the survey mask. The DESI DR1 set reproduces "the Bright Galaxy Survey number
  density and clustering at low redshift (z < 0.1) and the DESI PV samples of Fundamental plane and
  Tully-Fisher distances", plus SN Ia mocks; its fiducial value is f σ8 = 0.636 × 0.726 = 0.462,
  evaluated at z = 0.2 [src: arXiv:2512.03228, abstract and §9]. Mocks did **not** reproduce the TF
  excess correlation at z > 0.05 (`systematics.md` §4).
- **Consensus** across estimators: the BOSS method of combining correlated Gaussian posteriors with
  a mock-estimated correlation matrix; details and the DESI DR1 correlations (27–39 %) in
  `results.md` §1.
- **Blinding**: no blinding procedure is described in the DESI DR1 peculiar-velocity papers — the
  word does not occur in the LaTeX sources of arXiv:2512.03226 to arXiv:2512.03232 [src: text search
  of the sources, this session]. Sample cuts made after seeing the statistic (TF at z > 0.05, the k
  ≤ 0.1 momentum cut, the FP group correction) are documented as such. For the blinding standards of
  DESI clustering analyses see `cosmo-galaxy-clustering`.
- **Codes**: `flip`, `velocisaurus`, Galaxy_Power_Spectrum, Gacomb, VIRBIUS, Iskay2, with references
  in `surveys-and-data.md` §7.

## 9. Conventions, units and where the community is split
<!-- key: conventions-units-and-where-the-community-is -->

- **flip units**: RA/Dec in radians, comoving distances in h⁻¹Mpc, velocities in km/s, k in h Mpc⁻¹
  (workspace `CLAUDE.md` §5); reference paper arXiv:2501.16852.
- **Three different "β"**: β ≡ f/b (arXiv:1312.1022, arXiv:1706.05205); β* ≡ Ω_m^0.55 / b* with b*
  the bias of an L* galaxy (arXiv:1504.04627); β ≡ Ω_m^γ / b (arXiv:2007.04993). Converting any of
  them to fσ8 needs σ8 of the galaxy field, and the second and third assume a growth index.
- **Two different velocity-dispersion nuisances**: σ_u in h⁻¹Mpc is the scale of the sinc damping
  (§2); σ* (or σ_v) in km/s is an additive 1D dispersion on each velocity, ~300 km/s in the Kaiser
  estimator (§6) and a free "residual velocity scatter" in forward models (arXiv:2509.20235). They
  are not interchangeable and some analyses carry both.
- **σ8 normalisation and effective redshift**: see `pv-surveys.md` and `fsigma8-pv-compilation.md`. DESI DR1 defines z_eff as the mean
  redshift of all density and velocity galaxies [src: arXiv:2512.03230].
- **Bulk-flow window and depth**: Gaussian (arXiv:0809.4041), top-hat (arXiv:1808.07772), or the
  survey's own weights (MLE). "Depth" is a radius R for the first two and an error-weighted mean
  distance for the third.
- **Distance scale**: velocities from catalogued distances need the H0 of that catalogue (75.0 for
  CF4, arXiv:2512.03168); working in η with distances in h⁻¹Mpc removes the dependence.
- **Splits**: two-point compression with mock covariances (Qin, Turner et al.) against a field
  likelihood with a model covariance (Johnson, Adams, Lai, Ravoux et al.) — DESI runs both;
  empirical damping against EFT or emulators (§2); the density as data in the fit against a fixed
  external reconstruction, with opposite exposure to sample variance and to bias modelling.
