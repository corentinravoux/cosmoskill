# Physics and methods — peculiar-velocity estimators and their defining equations

Scope: the observables, estimators, covariance models and likelihoods used in direct
peculiar-velocity cosmology, with the equations as the cited papers write them, their range of
validity, and the public codes. Snapshot: 2026-10-22

Indicators and surveys: `surveys-and-data.md` §0–1; published fσ8 by family: `results.md` §0.
Equations are transcribed from the LaTeX source of the cited paper, read this session, in that
paper's notation: symbols differ between sections.

## 0. Method families
<!-- key: method-families -->

The reviews and comparison papers draw the families differently. Their classifications are set
side by side here; none is the field's single one. The fσ8 table of `results.md` §0 is sorted
by the last.

| Classification | Families | Place read |
|---|---|---|
| Dekel 1994 review | analysis of observed peculiar velocities; motions predicted from the galaxy distribution | arXiv:astro-ph/9401022, contents |
| Strauss & Willick 1995 review | velocity surveys alone; velocity surveys combined with redshift surveys (velocity–density comparison) | arXiv:astro-ph/9502079, abstract |
| Turner 2024 review | bulk flows; two-point statistics; velocity field reconstructions; maximum-likelihood estimators, which "model the covariance between the two fields analytically" | arXiv:2411.19484, Sects. 5.1–5.4 |
| DESI DR1 consensus (Turner et al. 2025) | two-point summary statistics, in Fourier space (Park 2000, Howlett 2017c, Qin 2019, 2025) or configuration space (Nusser 2017, Wang 2018, Dupuy 2019, Courtois 2023, Turner 2023, Lyall 2024); maximum-likelihood methods (Johnson 2014, Huterer 2017, Adams & Blake 2020, Lai 2023); reconstruction, the velocity field "inferred from the measured galaxy density field and then directly compared to discrete velocity measurements point-by-point" (Davis 2011, Turnbull 2012, Carrick 2015, Said 2020, Lilow & Nusser 2021, Qin 2023, Boubel 2024, Stiskalek 2025) | arXiv:2512.03230, Sect. 1 |
| Blake & Turner 2024, comparison | two "important classes": the "power-spectrum method" (2-point spectra of velocity and density tracers, fitted) and the "reconstruction-and-scaling method" (a model velocity field compared point by point) | arXiv:2408.05660, abstract |
| Adams & Blake 2020, literature comparison | covariance analyses; multi-tracer approaches; 6dFGS RSD and velocity results; density–velocity comparison approaches, whose fσ8 it calls "velocity-velocity constraints" | arXiv:2004.06399, Sect. 5.2 |
| Velocity Field Olympics (Stiskalek et al. 2025), reconstructions only | by constraint (redshift-space galaxy positions, or direct distance tracers) and by dynamics (BORG, non-linear; linear theory) | arXiv:2502.00121, abstract, Sect. 2.1 |
| This package's compilation (2026-08, folded 2026-10-20) | by what the estimator does to the data before fitting; the fitting technique is a separate axis (table below) | — |

The compilation's families, with "Rows" the rows of the fσ8 table (`results.md` §0); in that
compilation `[src]` meant "traced to the paper" and `[der]` "relabelled or derived, the paper does
not quote fσ8":

| Family | What it does | Depends on | Rows | Here |
|---|---|---|---|---|
| Field-level likelihood-based inference | the likelihood of the observed density and velocity *field values* is written through a model covariance and maximised or sampled; no summary statistic is measured first ("maximum likelihood fields") | the covariance model and its non-linear damping | 6 | §3 |
| Two-point statistics | a correlation function, power or momentum spectrum is *measured*, then fitted | the estimator, its window, the fitting template | 16 | §4 |
| Velocity–density comparison, linear | the velocity field is *predicted* from a redshift-survey density field by **linear theory** — directly, or through a Wiener filter / constrained realisation, still linear dynamics | an external density field, its bias, linear theory | 13 | §5 |
| Velocity–density comparison, particle forward model | the same, with the field evolved from initial conditions by a **gravity solver on a particle field** (LPT, COLA, particle-mesh, N-body), mildly non-linear | the solver, its resolution, the initial-condition prior | **0** | §5 |

There, almost every analysis maximises a likelihood, so "maximum likelihood" is a fitting
detail; the fitting technique is forward likelihood (Boruah 2020, Stahl 2021), forward model
(Boubel 2024), hierarchical Bayes (Stiskalek 2026, Ma+2012), MCMC or χ². The families fail
differently: on the covariance model; on the estimator and template; on the external density
field and linear theory.

Where the classifications place one analysis differently:

- **"Maximum likelihood" as a family or a technique.** Turner 2024 and the DESI DR1 consensus
  make it a family (above); the compilation makes it a technique. Turner (2024) Table 1 groups
  Howlett+2017 with the maximum-likelihood analyses, though it measures and fits the velocity
  power spectrum (its abstract finds the Watkins & Feldman estimator "suitable for measuring the
  velocity power spectrum") [src: arXiv:1706.05130, abstract]. Per Lai+2023, "In the development
  of the maximum likelihood fields method, Adams & Blake (2017) were the first to simultaneously
  model..."; Lai+2023 (arXiv:2209.04166) and the DESI analysis (arXiv:2512.03229) name the method
  in their own abstracts.
- **Forward-modelled indicator likelihoods** (Said 2020, Boubel 2024, Stiskalek 2025): the DESI
  consensus lists them under reconstruction; the compilation under linear velocity–density
  comparison, the forward model being the fitting technique.
- **Courtois et al. 2023 (Cosmicflows-4)**: a configuration-space correlation function in the
  DESI consensus, and its abstract gives its fσ8 "using the pairwise correlation of radial
  peculiar velocities" [src: arXiv:2211.16390, abstract]; a Hamiltonian Monte Carlo
  reconstruction that samples the growth rate in the Velocity Field Olympics [src:
  arXiv:2502.00121, Sect. 2.1.5].
- **Bulk flows** are a family in Turner 2024; the other rows classify growth-rate estimators and
  leave them out (§6).

## 1. The observable: log-distance ratio, and the velocity estimators built on it
<!-- key: the-observable-log-distance-ratio-and-the -->

**What is measured.** A distance indicator gives a distance modulus or a physical size with an error
that is Gaussian in the logarithm of the distance. The natural observable is the log-distance ratio

    η_i = log10[ D(z_obs,i) / D(z_cos,i) ]

with D the comoving radial distance, z_obs the observed and z_cos the cosmological redshift (notation
of arXiv:2501.16852, §3.2) [src]. Johnson et al. 2014 (arXiv:1404.3799) state the reason
it must be used: the intrinsic scatter of the FP and TF relations "is only Gaussian in logarithmic
distance units; wrongly assuming it is Gaussian in linear (velocity) units can bias cosmological
constraints" [src: abstract]. The DESI DR1 form, η ≡ log10[D(z_obs)/D(z_H)] = α v_p with
α(z_obs) = (1 + z_obs) / [ln(10) D(z_obs) H(z_obs)], follows Johnson et al. 2014 and Adams & Blake
2017 (derivation in their App. B); FP velocity errors are log-normal because the magnitude offsets
from the plane are Gaussian (Springob et al. 2014, App. A) [src: arXiv:2512.03230, eqs. 18–20,
Sect. 3.2.1].

**Where the indicators come from.** Faber & Jackson 1976 (doi:10.1086/154215): velocity dispersion
correlates with absolute magnitude, ellipticals are "close to being a one-parameter family" [src:
abstract]. Dressler et al. 1987 (doi:10.1086/164947): 97 ellipticals in six clusters lie on a plane
L ∝ σ^{8/3} Σe^{−3/5}; the D_n–σ relation gives distances with rms ≲ 25 % per galaxy, ≲ 10 % per rich
cluster [src: abstract]. Djorgovski & Davis 1987 (doi:10.1086/164948) name the "fundamental plane"
and propose it as an improved distance indicator [src: abstract]. The TF relation is Tully & Fisher
1977 (A&A 54, 661; no DOI or arXiv record found), cited here through Turner 2024 [sec:
arXiv:2411.19484, Sect. 3.1, which quotes 0.35–0.40 mag TF scatter and ~0.1 dex FP scatter, both
~20 % in distance]. Nusser & Davis 1994 (arXiv:astro-ph/9407100) fit the **inverse** TF relation
with a parametrised velocity field: free of Malmquist bias without multi-streaming, if no selection
is made on the circular velocities [src: abstract].

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
| log-distance (arXiv:2501.16852) | v_i = ln(10) · D(z_obs,i) H(z_obs,i) /(1 + z_obs,i) · η_i | arXiv:2501.16852, eq. "etatovel" | [src] |
| Hubble-residual (arXiv:2501.16852) | v_i = −(c ln10 / 5) · J(p_i) · Δμ_i, with J one of four forms: "Watkins" z/(1+z); "low-z" z; "Hubble high-order" (the q0, j0 expansion above divided by 1+z); "full" [ (1+z)c / ((H(z)/h) D(z)) − 1 ]⁻¹ | arXiv:2501.16852, eq. "dmutovel" and Table "velest" | [src] |
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

The redshift-space terms descend from Kaiser 1987 (doi:10.1093/mnras/227.1.1): peculiar velocities
give the large-scale power spectrum "a quadrupole anisotropy, providing a way to estimate Ω" [src:
abstract]. The model that every likelihood analysis descends from is Koda et al. 2014 (arXiv:1312.1022), who
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

The fitted amplitude is fσ8 because P_θθ and P_mθ are normalised by the fiducial σ8²; in the
decomposition of arXiv:2501.16852 the velocity term has coefficient A_vv = (fσ8)² multiplying (aH)² μ1 μ2 / k² · P_θθ(k)
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
density–velocity cross-covariance); Adams & Blake 2020 (arXiv:2004.06399, RSD in the density term),
all on 6dFGS; then Lai et al. 2023 (arXiv:2209.04166, wide-angle effect and zero-point calibration)
[src: abstracts]. Earlier roots: Jaffe & Kaiser 1994 (arXiv:astro-ph/9408046), a likelihood of
velocity data for a P(k) parametrised by (σ8, Γ), applied to Lauer & Postman clusters and to SNe Ia;
Abate et al. 2008 (arXiv:0802.1935), the full velocity covariance averaged in grid cells, which
"reduces the number of data points and smooths out nonlinearities", with < 3 % bias on σ8 for a
6dFGSv-like survey [src: abstracts]. Johnson et al. 2014 grid with the Abate et al. scheme [src:
arXiv:1404.3799, Sect. 3.5].

**Covariance from the power spectrum.** For two fields a, b at positions r1, r2,

    C_ab(r1, r2) = (2π)⁻³ ∫ d³k  P_ab(k, μ1, μ2) e^{i k·r}

with μ1, μ2 the cosines to the two lines of sight. One general decomposition, implemented in the flip code (arXiv:2501.16852, §2.2), writes any model as

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

**Named covariance models** (labels of arXiv:2501.16852) [src: arXiv:2501.16852, §3.1]:

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
- Cells with δ_g > 10 are removed as ones "that our quasi-linear theory cannot accurately model" (6
  of ~6 000 cells on the 20 h⁻¹Mpc grid; the 41 of 2 023 cells, about 2 %, is the δ_g > 2 cut of the
  30 h⁻¹Mpc variant) [src: App. B], and a 4σ cut on η removes outliers.
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
of a sparsely sampled velocity field. The statistic was introduced by Park 2000
(arXiv:astro-ph/0012066: momentum field "equal to the velocity field in the linear regime", radial
part with ~1/3 of the total power, applied to Mark III) and measured on SFI by Park & Park 2005
(arXiv:astro-ph/0509740: β_S = 0.49 +0.08/−0.05 over 0.026 ≲ k ≲ 0.157 h Mpc⁻¹) [src: abstracts];
Howlett 2019 revisits these "two key references" [src: arXiv:1906.02875, Sect. 1]. Estimator:

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

Unlike the correlation-function and field-level analyses, the DESI DR1 power spectra convert η to a
velocity first, v = c z_mod ln10 η / (1 + z_mod) with the Watkins–Feldman z_mod, and take ⟨v²⟩ =
(ln10 c z σ_η / (1 + z))² + 300² km² s⁻² in the shot noise; p ≡ (1 + δ)v (eq. 2) is preferred
because velocities are only sampled where galaxies are [src: arXiv:2512.03231, eqs. 2, 57–59,
Sect. 3.1, App. A].

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

[src: arXiv:2604.08314, eqs. "psipar", "psiperp" and following]. The DESI DR1 correlation-function
paper prints the two kernels the other way round, j0 − 2j1/(kr) under Ψ⊥ and j1/(kr) under Ψ∥
[src: arXiv:2512.03230, Sect. 3.1.1, Eqs. 8–9]; check which assignment a code follows before
comparing (`deep/two-point-statistics.md`). The measured ψ1, ψ2 are
survey-geometry-dependent mixtures, ψ1(r) = A(r) Ψ∥ + [1 − A(r)] Ψ⊥ and ψ2(r) = B(r) Ψ∥ + [1 − B(r)]
Ψ⊥ [src: Turner et al. 2025, arXiv:2512.03230, §3], so **the model must be built with the survey's
own A(r), B(r)**; two surveys' ψ1 are not comparable.

DESI DR1 writes them directly in η (arXiv:2512.03230, eqs. 23–25) [src: Sect. 3.2.3]:
ψ̂1 = Σ W_a W_b η_a η_b cos θ_ab / Σ W_a W_b cos² θ_ab and ψ̂2 = Σ W_a W_b η_a η_b cos θ_a cos θ_b
/ Σ W_a W_b cos θ_a cos θ_b cos θ_ab over data–data pairs, rescaled to velocity units by α_vv(r) =
Σ W_a W_b / Σ W_a W_b α_a α_b; 6 h⁻¹Mpc bins over 0–150 h⁻¹Mpc (pycorr, crosscorr).

DESI DR1 configuration (arXiv:2512.03230) [src: body]: five statistics ψ1, ψ2, ξ⁰_gg, ξ²_gg, ξ¹_gu
in 6 h⁻¹Mpc bins; fit range 24–120 h⁻¹Mpc (16 bins each, 80 × 80 covariance from all 675 mocks);
model from density and momentum power spectra at 1-loop Eulerian perturbation theory. The lower
bound is a compromise: 12 h⁻¹Mpc is "strictly closest to the fiducial cosmology" on mocks but "leads
to a poor goodness-of-fit". Earlier applications: Turner, Blake & Ruggeri 2023 (arXiv:2207.03707,
6dFGS) [src: title].

A **linear template biases this family low** (Tonegawa et al. 2024, arXiv:2309.14457; 5.2 % on HR4
mocks [sec: 2026-08 compilation, `results.md` §0]; non-linear and density–velocity terms shift fσ8
by ~10 % for a next-generation volume with r_min = 20 h⁻¹Mpc [src: abstract]), and finite mock volumes suppress large-scale velocity
correlations (`systematics.md` §8).

### 4c. Supernova magnitude covariance
<!-- key: supernova-magnitude-covariance -->

The same signal written as a covariance of SN magnitude residuals: Hui & Greene 2006
(arXiv:astro-ph/0512159; ignoring it underestimates a low-z anchor's zero-point error "by about a
factor of 2"); first detection, σ8 = 0.79 ± 0.22, by Gordon, Land & Slosar 2007 (arXiv:0705.1718);
standard Hubble-diagram treatment in Davis et al. 2011 (arXiv:1012.2912); growth fits in Huterer et
al. 2017 (arXiv:1611.09862) and Crisman et al. 2026 (arXiv:2604.06361) [src: abstracts and titles].
SNe Ia as velocity tracers go back to Riess, Press & Kirshner 1994 (arXiv:astro-ph/9412017): 13
SNe at an effective 7 000 km/s, ~5 % distances, Local Group motion 600 ± 350 km/s consistent with
the CMB dipole [src: abstract]. Its role as a *nuisance* in SN cosmology belongs to `cosmo-supernovae`.

## 5. Velocity–density comparison and forward models
<!-- key: velocity-density-comparison-and-forward-models -->

**Linear comparison.** The velocity field is predicted from a redshift-survey density field by
linear theory and scaled by β = f/b; with σ8 of the galaxies measured in the same field this gives
fσ8 normalised to the **linear** σ8. Reference analyses: Pike & Hudson 2005
(arXiv:astro-ph/0511012), Carrick et al. 2015 (arXiv:1504.04627, 2M++: β* = 0.431 ± 0.021 → Ω_m^0.55
σ8,lin = 0.401 ± 0.024), Boruah, Hudson & Lavaux 2020 (arXiv:1912.09383), Said et al. 2020
(arXiv:2007.04993: β = 0.341 ± 0.024 from 15 894 FP galaxies), Stahl et al. 2021 (arXiv:2105.05185),
Lilow & Nusser 2021 (arXiv:2102.07291), Boubel et al. 2024 (arXiv:2301.12648) [src: abstracts].
Classical formalism, including Malmquist bias: Strauss & Willick 1995 (arXiv:astro-ph/9502079);
review of that era: Dekel 1994 (arXiv:astro-ph/9401022, sections on measuring velocities, predicted
motions from the galaxy distribution, and Ω) [src: abstract]. The reverse route, the 3D velocity
and mass fields reconstructed from radial velocities alone under a no-vorticity assumption, is POTENT:
Bertschinger & Dekel 1989 (doi:10.1086/185348) and the method paper Dekel, Bertschinger & Faber 1990
(doi:10.1086/169418), which smooths with a tensor window and explores Malmquist bias with Monte Carlo
simulations [src: abstracts]. **Calibration of the method on mocks.** Hollinger & Hudson 2024 (arXiv:2312.03904) and Dixon et al.
2026 (arXiv:2606.14962); numbers in `systematics.md` §6.

**Forward-modelling the distance indicator.** VIRBIUS (Lavaux 2016, arXiv:1512.04534) samples true
distances, the 3D velocity field and calibration parameters jointly, handling selection and
miscalibration [src: abstract]. Stiskalek 2025 (arXiv:2509.20235) and Stiskalek, Desmond & Lavaux
2025 (arXiv:2509.14997) calibrate each indicator jointly with a linear-theory reconstruction and
marginalise over distances ("jointly calibrates each distance indicator and a *linear theory*
reconstruction") [src: abstracts]; Boubel 2024, Boruah 2020 and Stahl 2021 likewise forward-model
the TF relation, Malmquist bias or standardisation against the 2M++ linear-theory prediction. In
all of these the velocity field is linear: "forward model" does not imply non-linear dynamics; nor
do constrained realisations, a Wiener filter in spherical Fourier–Bessel space (Lilow & Nusser 2021)
[src: arXiv:2102.07291, abstract].

**Forward-modelling the field.** Graziani et al. 2019 (arXiv:1901.01818: hierarchical Bayesian
forward model of CF3 that "assumes the ΛCDM model within the linear regime"); Boruah, Lavaux &
Hudson 2022 (arXiv:2111.15535: "a forward-modelled velocity field reconstruction algorithm",
forward-modelling the distance data and inhomogeneous Malmquist bias); Valade et al. 2026
(arXiv:2602.03699, Hamlet-PM: "The dynamics are integrated with a particle-mesh gravity solver, thus
probing the mildly non-linear regime", on CF4 to z < 0.05, 100 constrained 512³ runs in 500 h⁻¹Mpc
boxes — the clearest particle-evolving analysis); Nusser 2026 (arXiv:2606.08593, Zel'dovich MAP
reconstruction of 2MRS with an unbinned Poisson likelihood, tested on CF4 groups); BORG (Jasche &
Lavaux 2019, arXiv:1806.11117) and Manticore-Local (McAlpine et al. 2025, arXiv:2505.10682: BORG
with a nonlinear gravitational solver on 2M++, Bayesian evidence comparisons) on the density side
[src: abstracts, titles]. None quotes fσ8: **no published fσ8 comes from a particle-evolving forward
model** (`open-questions.md` §9). The quotations and this check (2026-08-14) were folded on
2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the paper" and
`[der]` "relabelled or derived, the paper does not quote fσ8".

**Machine-learned reconstruction.** Gong & Bean 2026 (arXiv:2606.05047): a gradient-boosted tree and
a Transformer trained on AbacusSummit to predict the residual between true and linear-theory
velocity; used for kSZ stacking (§7) [src].

## 6. Bulk-flow estimators
<!-- key: bulk-flow-estimators -->

**Origin.** Lynden-Bell et al. 1988 (doi:10.1086/166066): the motions of 400 ellipticals are fitted
better by infall onto a "great attractor" at 4 350 ± 350 km/s than by a bulk motion, which was
itself better than pure Hubble flow in the CMB frame; streaming at the Sun 570 ± 60 km/s [src:
abstract]. Flow models and bulk flows have been compared since.

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
depth, typically shallow. [src: Sect. 1]

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

The kinematic Sunyaev–Zel'dovich effect gives **τ × v**, never v alone. Its three estimators —
pairwise kSZ, velocity-weighted stacking, kSZ velocity reconstruction — and their degeneracies (τ̄,
the stacking velocity, the velocity bias b_v) are tabulated with the 2025–2026 measurements in
`results.md` §4. With b_v ≈ 0.3–0.45 (arXiv:2506.21657, arXiv:2511.15701) the *amplitude*, hence
fσ8, is not measurable by kSZ alone; kSZ velocities constrain shapes (f_NL, the force-law index) and
gas physics, which belong with the CMB side to `cosmo-cmb-lss-cross-correlations`.

## 8. Covariance, mocks, consensus, blinding practice and codes
<!-- key: covariance-mocks-consensus-blinding-practice -->

- **Field-level**: the covariance *is* the model; it is analytic, dense, N × N, and recomputed (or
  interpolated) for every non-linear parameter. Errors come from the posterior, and are checked
  against mock scatter: on DESI DR1 FP mocks the mean posterior error (0.064) matches the scatter of
  best fits (0.063) [src: arXiv:2512.03229, §4], but with density + velocity the mean error (0.036)
  is below the scatter (0.059), and the data error was inflated by 1.64 [src: arXiv:2512.03229,
  Table 1, Sect. 4.4.2].
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
- **What each main analysis did** (priors and systematic terms in `systematics.md` §9b; none
  describes a blinding step):

| Analysis | Data | Scales | Model, nuisances | Covariance, likelihood |
|---|---|---|---|---|
| DESI DR1 field-level, arXiv:2512.03229 | 415 523 BGS z + 76 616 η, 0.01 < z < 0.1 | 20 h⁻¹Mpc grid, δ_g ≤ 10 | linear + RSD, wide-angle; fσ8, bσ8, b_add σ8, σ_v, σ_g; σ_u = 16 fixed | analytic; zero-point marginalised (eq. 32); error × 1.64 from mocks [src: Sect. 4.1, 4.4.2] |
| DESI DR1 correlation functions, arXiv:2512.03230 | same, 76 615 η | 24–120 h⁻¹Mpc, 6 h⁻¹Mpc bins | 1-loop; fσ8, b1σ8, b2σ8, σ²_vT, σ²_vS | 675 mocks, Hartlap, emcee [src: Sect. 3.3] |
| DESI DR1 power spectra, arXiv:2512.03231 | same | P^δ, P^δp to k = 0.3; P^p to 0.1 h Mpc⁻¹ | 1-loop, the same five parameters | 675 mocks, Sellentin–Heavens (eq. 54) [src: Sect. 5.1, 6.1] |
| SDSS PV field-level, arXiv:2209.04166 | 34 059 FP, 7 016 deg², z < 0.1 | k_max = 0.15, δ_g ≤ 20; 30 h⁻¹Mpc grid on mocks without Taylor expansion | as DESI, σ_u = 22 fixed | analytic, zero-point marginalised [src: Sect. 2.1, 4.1.2, Fig. 11] |
| SDSS PV power spectra, arXiv:2411.09571 | same | not read | 1-loop; fσ8, b1σ8, b2σ8, b3nlσ8, σ²_v | 2 048 mocks, Box–Cox, Sellentin–Heavens [src: Sect. V.1] |
| 6dFGSv field-level, arXiv:1404.3799 | 8 896 FP, cz < 16 120 km/s | gridded (Abate et al. 2008) | velocity only; zero-point marginalised (eq. 32) | analytic [src: Sect. 2.1, 3.5, 3.6] |
| 6dFGS RSD + PV, arXiv:2004.06399 | 6dFGS redshifts + 6dFGSv | k_max fixed (systematic term) | + α_b for redshift-dependent bias | analytic; fixed-parameter systematics by finite difference [src: Sect. 5.1.1] |

- **Codes**: `flip`, `velocisaurus`, Galaxy_Power_Spectrum, Gacomb, VIRBIUS, Iskay2, with references
  in `surveys-and-data.md` §7.

## 9. Conventions, units and where the community is split
<!-- key: conventions-units-and-where-the-community-is -->

- **Three different "β"**: β ≡ f/b (arXiv:1312.1022, arXiv:1706.05205); β* ≡ Ω_m^0.55 / b* with b*
  the bias of an L* galaxy (arXiv:1504.04627); β ≡ Ω_m^γ / b (arXiv:2007.04993). Converting any of
  them to fσ8 needs σ8 of the galaxy field, and the second and third assume a growth index.
- **Two different velocity-dispersion nuisances**: σ_u in h⁻¹Mpc is the scale of the sinc damping
  (§2); σ* (or σ_v) in km/s is an additive 1D dispersion on each velocity, ~300 km/s in the Kaiser
  estimator (§6) and a free "residual velocity scatter" in forward models (arXiv:2509.20235). They
  are not interchangeable and some analyses carry both.
- **σ8 normalisation and effective redshift**: see `results.md` §0a–0b. DESI DR1 defines z_eff as the
  mean redshift of all density and velocity galaxies [src: arXiv:2512.03230].
- **Bulk-flow window and depth**: Gaussian (arXiv:0809.4041), top-hat (arXiv:1808.07772), or the
  survey's own weights (MLE). "Depth" is a radius R for the first two and an error-weighted mean
  distance for the third.
- **Distance scale**: velocities from catalogued distances need the H0 of that catalogue (75.0 for
  CF4, arXiv:2512.03168); working in η with distances in h⁻¹Mpc removes the dependence.
- **Splits**: two-point compression with mock covariances (Qin, Turner et al.) against a field
  likelihood with a model covariance (Johnson, Adams, Lai, Ravoux et al.) — DESI runs both;
  empirical damping against EFT or emulators (§2); the density as data in the fit against a fixed
  external reconstruction, with opposite exposure to sample variance and to bias modelling.

## Not verified in this file
<!-- key: not-verified-in-this-file -->

- Tully & Fisher 1977 (A&A 54, 661): no DOI or arXiv record found and abstract not read; cited only
  through Turner 2024.
- The scale range of the SDSS PV power-spectrum fit (arXiv:2411.09571) and the k_max of the 6dFGS
  joint fit (arXiv:2004.06399).
- Malmquist 1920 and the earliest inhomogeneous-Malmquist treatments: no identifier found this pass.
- §0 and the forward-model passages of §5: folded from the 2026-08 compilation, not re-read (except
  the abstracts of arXiv:1706.05130 and arXiv:2102.07291, read 2026-10-20).
