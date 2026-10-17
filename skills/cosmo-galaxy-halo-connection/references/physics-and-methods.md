# Galaxy–halo connection — physics and methods

Scope: halo definitions, mass functions, bias and profiles as ingredients; the
halo model; the empirical (HOD, CLF, abundance matching, empirical formation
histories) and physical (semi-analytic, hydrodynamical) models of the
galaxy–halo connection; assembly bias; satellites; lensing with clustering.
Each method with its reference paper. Snapshot: 2026-10-16

Flags: `[src]` read this session in the abstract of the cited paper; `[src:
Sect. n]`, `[src: Eq. n]`, `[src: Table n]` read in the body; `[sec]` from a
named secondary source; `[der]` derived here.

The domain map used throughout is Wechsler & Tinker 2018 (arXiv:1804.03097),
which defines the galaxy–halo connection as "the multi-variate distribution of
galaxy and halo properties that can be derived from observations and
simulations" [src]; the halo-model side follows Asgari, Mead & Heymans 2023
(arXiv:2303.08752). Bias expansions in perturbation theory and the halo-model
equations of the matter spectrum are written out in `cosmo-theory-foundations`
(sections 10–11); how mocks are populated for a survey is in
`cosmo-simulations-mocks` (section 6).

## 1. Halo definitions and finders
<!-- key: halo-definitions-and-finders -->

| Concept | What the sources state | Reference |
|---|---|---|
| Spherical overdensity (SO) | haloes are "generally defined with masses and radii specified by a given overdensity: M_vir = (4π/3) R_vir³ Δ ρ_m", Δ "around 200"; the review uses the Bryan & Norman virial Δ unless stated. Labels: 200m (mean), 200c (critical), 500c (X-ray), vir | [src: Sect. 2.1 of arXiv:1804.03097]; Bryan & Norman 1998, arXiv:astro-ph/9710107 |
| Conversions | SO masses are "much more tightly correlated with each other than with masses based on the number of particles" (FoF); unmatched definitions between hydro and N-body runs give an "observationally significant bias" in abundances | White 2001, arXiv:astro-ph/0011495 [src] |
| Pseudo-evolution | SO mass grows with the falling reference density even for a static profile: "almost the entire mass evolution" of most M200 ~ 10¹² M_⊙ haloes since z = 1, and the low-mass evolution of c(M) | Diemer et al. 2013, arXiv:1207.0816 [src] |
| Outer profiles | most self-similar in units of R200m (inner ones in R200c); steepest slope near R200m, −4 or steeper for fast accretors | Diemer 2014, arXiv:1401.1216 [src] |
| Splashback radius | first apocentre after turnaround: R_sp ≈ 0.8–1 R200m (rapid accretion) to ≈ 1.5 R200m (slow); "not expected to change the qualitative conclusions" of galaxy–halo work; cluster measurements in `cosmo-clusters` | More et al. 2015, arXiv:1504.05591 [src]; [src: Sect. 2.1 of arXiv:1804.03097] |
| Subhaloes | bound peaks orbiting inside a host; "resolving and tracking such objects is critical" | [src: Sect. 2.1 of arXiv:1804.03097] |
| Finder comparison | most finders lose substructure below 30–40 particles (phase-space finders reach 10–20) and near the host centre, but agree "remarkably well" on host properties; finder table in `cosmo-simulations-mocks` section 11 | Knebe et al. 2011, arXiv:1104.0949 [src] |

Rule: an occupation parameter written in terms of halo mass (M_min, M_1) is
meaningful only with the mass definition and finder it was fitted on [der: from
the finder and definition dependence above].

## 2. Halo mass function
<!-- key: halo-mass-function -->

Form. Tinker et al. 2008 write dn/dM = f(σ) (ρ̄_m/M) d ln σ⁻¹/dM [src: Eq. 2 of
arXiv:0803.2706] with f(σ) = A[(σ/b)^(−a) + 1] e^(−c/σ²) [src: Eq. 3], peak
height ν ≡ δ_c/σ(M, z), δ_c ≈ 1.69 [src: Sect. III.1]. Sheth & Tormen 1999
(arXiv:astro-ph/9901122), on spherical-overdensity GIF haloes, define ν ≡
[δ_c(z)/σ(m)]² (note: squared) and fit νf(ν) = A(1 + ν′^(−p)) (ν′/2)^½
e^(−ν′/2)/√π, ν′ = aν, a = 0.707, p = 0.3, A fixed by normalisation;
Press–Schechter is a = 1, p = 0, A = ½ [src: Eqs. 9–10, Sect. 3].

| Calibration | What it established | Reference |
|---|---|---|
| Press–Schechter extended to ellipsoidal collapse | ellipsoidal collapse with a mass-dependent threshold δ_ec(m) reduces the excess of low-mass objects of the spherical model and improves mass function and bias | Sheth et al. 2001, arXiv:astro-ph/9907024 [src] |
| Hubble Volume and other runs | near-universal f in suitable variables; systematic uncertainty 10–30% depending on the halo definition; Press–Schechter overestimates typical and underestimates massive haloes | Jenkins et al. 2001, arXiv:astro-ph/0005260 [src] |
| SO haloes, 10¹¹–10¹⁵ M_⊙/h, z ≲ 2 | calibration to ≲ 5%; not universal at that accuracy; the amplitude of the "universal" function falls by ~20–50% from z = 0 to 2.5 | Tinker et al. 2008, arXiv:0803.2706 [src] |
| Virial definition | the virial-definition HMF is "nearly universal" in ν across redshift and cosmology, other overdensities are not; fits to a few per cent for many definitions | Despali et al. 2016, arXiv:1507.05627 [src] |
| Magneticum hydro vs DM-only | baryons lower cluster masses and so their abundance; the effect vanishes at z ~ 2 and M200m ≳ 10¹⁴ M_⊙; a Planck-like sample shifts by Δσ8 ≃ 0.02 relative to Tinker 2008 | Bocquet et al. 2016, arXiv:1502.07357 [src] |
| Aemulus emulator, M200m, flat wCDM | better than 1% precision over much of the space; non-universality confirmed | McClintock et al. 2019, arXiv:1804.05866 [src] |
| Dark Emulator, 101 wCDM models, z = 0–1.48 | HMF, halo–matter and halo–halo correlations; for CMASS-like haloes halo–matter < 2% and halo auto-correlation < 4% error | Nishimichi et al. 2019, arXiv:1811.09504 [src] |
| Euclid calibration, ΛCDM and massive neutrinos | sub-per-cent accuracy over 9 ΛCDM variants; the halo finder is the one calibration systematic that "could lead to biased cosmological inference" | Euclid Collaboration: Castro et al. 2023, arXiv:2208.02174 [src] |
| Uchuu, 6.5 < log M200m < 16, 0 < z < 20 | GPS+ model within 10–20%; Sheth–Tormen deviates by 70–80% at high z; Bryan–Norman masses less universal than M200m | Fernández-García et al. 2025, arXiv:2512.05847 [src] |
| VVV + large volumes, 10⁻⁶–10¹⁵·⁵ M_⊙, z = 30–0 | fitting formula after Reed et al. with ~2–3% deviations at z < 2 and ~7% at z ≳ 5 | Zheng et al. 2026, arXiv:2607.05505 [src] |
| Aletheia, evolution mapping | Gaussian-process emulator in σ12 and shape parameters; per-cent level, applicable to dynamical dark energy | Fiorilli et al. 2026, arXiv:2609.10665 [src] |

How the HMF enters cluster counts, and the mass calibration that dominates
them, belongs to `cosmo-clusters`.

## 3. Halo bias
<!-- key: halo-bias -->

- Mo 1996 (arXiv:astro-ph/9512127) extend Press–Schechter with spherical
  collapse into an analytic bias function and find the halo autocorrelation
  proportional to that of mass "over a wide range in R, even including scales
  where both functions are significantly greater than unity" [src].
- Peak-background split. Sheth 1999 (arXiv:astro-ph/9901122): "knowledge of the
  unconditional mass function alone is sufficient to provide an accurate
  estimate of the large scale bias factor" [src]; with the fit above, b_Eul =
  1 + (aν − 1)/δ_c + (2p/δ_c)/[1 + (aν)^p]: massive haloes slightly less, small
  ones more biased than Mo & White [src: Eq. 12, Sect. 3].
- Numerical calibration. Tinker et al. 2010 (arXiv:1001.3162): ~6% scatter
  about the fit; normalised so that all matter has unit bias with the Tinker
  2008 mass function; rare haloes are more biased than the Sheth–Mo–Tormen
  ellipsoidal model predicts; FoF (b = 0.2) bias is ~10% below Δ = 200; the
  bias function "evolves very weakly with redshift, if at all"; the
  peak-background split leaves ~20% residuals at high and low mass [src].
  Fit: b(ν) = 1 − A ν^a/(ν^a + δ_c^a) + B ν^b + C ν^c, ν = δ_c/σ, normalised by
  ∫ b f dν = 1 [src: Eqs. 6–7]; for 200 ≤ Δ ≤ 3200 (y = log₁₀Δ): A = 1 +
  0.24y e^(−(4/y)⁴), a = 0.44y − 0.88, B = 0.183, b = 1.5, C = 0.019 + 0.107y +
  0.19 e^(−(4/y)⁴), c = 2.4 [src: Table 2].
- Non-linear (scale-dependent) halo bias in the 1-halo/2-halo transition is an
  ingredient of halo-model extensions (section 5).
- Secondary bias. At fixed mass, halo clustering depends on formation time,
  concentration and other properties (section 9).

## 4. Density profiles and concentration
<!-- key: density-profiles-and-concentration -->

- NFW. Equilibrium profiles "have the same shape, independent of halo mass, of
  initial density fluctuation spectrum, and of the values of the cosmological
  parameters"; low-mass haloes are denser, reflecting earlier collapse
  (Navarro, Frenk & White 1997, arXiv:astro-ph/9611107) [src]. ρ(r)/ρ_crit =
  δ_c/[(r/r_s)(1 + r/r_s)²] [src: Eq. 1]; with c = r_200/r_s (r_200 at 200
  ρ_crit), δ_c = (200/3) c³/[ln(1 + c) − c/(1 + c)], one free parameter at fixed
  M_200, c falling with mass [src: Sect. 3.2]. Truncation: `cosmo-theory-foundations` §11.
- Einasto-type. The logarithmic slope decreases monotonically inward with no
  convergence to an inner power law; cusps as steep as r^(−1.5) are
  inconsistent with most simulations (Navarro et al. 2004,
  arXiv:astro-ph/0311231) [src]. Einasto describes stacked profiles better than
  NFW, though both agree well at cluster scales at low z (Child et al. 2018,
  arXiv:1804.10199) [src].
- Concentration–mass relations:

| Relation | Content | Reference |
|---|---|---|
| Bullock et al. 2001 | c_v ∝ 1/(1+z) at fixed mass; scatter in log c_v ~ 0.18; denser environments give more concentrated haloes | arXiv:astro-ph/9908159 [src] |
| Duffy et al. 2008 | power law for 10¹¹–10¹⁵ M_⊙/h, z < 2, in WMAP5; z = 0 concentrations 23% (10¹¹) to 16% (10¹⁴ M_⊙/h) below Millennium values; "much lower" than X-ray inferences [src]. Form c = A(M/M_pivot)^B (1+z)^C, M_pivot = 2 × 10¹² h⁻¹M_⊙ [src: Eq. 4]; NFW, full sample, z = 0–2: (A, B, C) = (5.71, −0.084, −0.47) for 200c, (7.85, −0.081, −0.71) for vir, (10.14, −0.081, −1.01) for 200m; [src: Table 1]; relaxed haloes have A higher by ~18% [der: ratio of the Table 1 rows] | arXiv:0804.2486 |
| Ludlow et al. 2016 | c(M, z) of CDM monotonic; WDM non-monotonic; collapsed mass history predicts both | arXiv:1601.02624 [src] |
| Child et al. 2018 | in M/M*: power law below M/M* ~ 500–1000, then constant c_0 ~ 3; relaxed fraction falls to ~0.5 | arXiv:1804.10199 [src] |
| Diemer 2019 | analytic model from pseudo-evolution plus ν, n_eff and α_eff; 5% accuracy against scale-free and ΛCDM simulations; in Colossus | arXiv:1809.07326 [src] |
| CAMELS, 28 parameters | baryonic imprints on c_vir–M_vir over 10¹¹–10¹⁴·⁵ M_⊙/h, z = 0–3, from 2048 TNG-model runs | Delgado 2026, arXiv:2610.03544 [src] |

Concentration taken from one relation (often Duffy et al. 2008 with its slopes
fixed) is an assumption of most halo-model fits of lensing; the cluster
analyses that do so are listed in `cosmo-clusters`.

## 5. The halo model and its limits
<!-- key: the-halo-model-and-its-limits -->

Foundations. Seljak 2000 (arXiv:astro-ph/0001493) writes the power spectrum as
"a sum of two contributions, one from correlations between the halos and one
from correlations within the same halo", and predicts a scale-dependent,
non-monotonic galaxy bias; galaxy–galaxy lensing "cannot be interpreted simply
as an average halo profile of a typical galaxy, because different halo masses
dominate at different scales" [src]. Ma 2000 (arXiv:astro-ph/0003343) build the
same model from profiles, mass functions and halo correlations and extend it to
the bispectrum [src]; Peacock 2000 (arXiv:astro-ph/0005010) add the occupation
number, one galaxy at the centre and satellites tracing the mass, "a recipe for
non-local bias" [src]. Review: Cooray 2002 (arXiv:astro-ph/0206508); current
pedagogical review: Asgari, Mead & Heymans 2023 (arXiv:2303.08752).

The two-halo matter term is P^2h_mm(k) = P^lin_mm(k) [ (1/ρ̄) ∫ M Û_m(M, k)
b(M) n(M) dM ]² [src: Eq. 35 of arXiv:2303.08752]; the one-halo and two-halo
terms of a general pair of fields are its Eqs. 13 and 18. The galaxy terms need
⟨N_c N_s⟩ and ⟨N_s(N_s − 1)⟩ (Eqs. 26–27), so the occupation statistics, not
only the mean, enter (section 6).

Known limits, as the review lists them [src: Sect. 5 of arXiv:2303.08752]:

| Limit | Mechanism | Remedy in the literature |
|---|---|---|
| Large-scale one-halo term | Û(M, k → 0) is constant, so P^1h ∝ k⁰ while P^2h ∝ k^(n_s): the one-halo term dominates again at k ~ 10⁻⁴ h/Mpc. Correct as shot noise for a discrete tracer, wrong for matter, which must fall faster than k⁴ by mass and momentum conservation [src: Sect. 5.4] | compensation kernels enforcing k² (Mohammed & Seljak; Seljak & Vlah), Lagrangian formulations, a halo-fluctuation field with a general bias expansion |
| Transition region | linear halo bias under-predicts power between the two regimes | beyond-linear halo bias: a corrective two-halo term measured in N-body that "can boost power in the two-halo term by a factor of ~2 at scales k ~ 0.7 h/Mpc" and "almost completely" removes the under-prediction (Mead 2021, arXiv:2011.08858) [src] |
| Halo exclusion | finite radii force the halo correlation to zero below r_h,1 + r_h,2; its form depends on the halo definition [src: Sect. 5.6] | automatic if P_hh or β^nl is calibrated on simulations (Dark Emulator, Mead & Verde); otherwise modified integration limits, which bias the predicted number density and must be corrected by hand. Originals: Zehavi et al. 2004 (arXiv:astro-ph/0301280) keep in the two-halo term only haloes with R_vir ≤ r/2 and use b²(M, r) = [1 + 0.2 ξ_m(r)]^(−0.5) b²_lin(M), with residuals of ~10–20% [src: Sect. III, App. A]; Tinker et al. 2005 (arXiv:astro-ph/0411777) show that the r/2 cut under-counts two-halo pairs by > 50% at 1 h⁻¹Mpc, spherical exclusion (R_vir1 + R_vir2 ≤ r) by ~25%, ellipsoidal exclusion (axis ratios 0.9, 0.8) by ~10%, and use an n̄′_g-matched shortcut; the original SMT bias over-predicts galaxy bias by ~15% at r ≳ 10 h⁻¹Mpc [src: App. B, Eqs. B10–B13] |
| Scatter in concentration | σ_ln c ~ 0.3; the mean profile is used where ⟨Û²⟩ appears; realistic scatter boosts matter power by a few per cent at k ≳ 10 h/Mpc [src: Sect. 5.8] | an extra integral over p(c) if spatially uncorrelated; spatially correlated scatter is assembly bias |
| Accuracy of the full model | the CLF + halo-model framework with scale-dependent halo bias and exclusion reproduces 3D galaxy–galaxy and galaxy–matter correlations to better than 10% (mostly 5%); ignoring either effect gives errors "that easily exceed 40 percent on scales of ~1 h⁻¹Mpc"; residual redshift-space distortions in w_p exceed 20% at r_p ≳ 10 h⁻¹Mpc if ignored and are corrected to ~2% with a modified Kaiser formula | van den Bosch et al. 2013, arXiv:1206.6890 [src] |

Halofit and HMcode are fits inspired by the halo model, not evaluations of its
integrals; they live in `cosmo-theory-foundations` and
`cosmo-simulations-mocks`. The halo-model treatment of baryonic feedback on the
matter spectrum is in `cosmo-weak-lensing` and `cosmo-simulations-mocks`.

## 6. Halo occupation distribution and conditional luminosity function
<!-- key: halo-occupation-distribution-and-conditional -->

**HOD.** Berlind 2002 (arXiv:astro-ph/0109001) define the bias of a population
by P(N|M) plus the spatial and velocity distributions of galaxies within
haloes; different statistics respond to different combinations of its
parameters, and cosmological and HOD parameters are argued to have
non-degenerate effects [src]. In dissipationless simulations ⟨N⟩(M) of
subhaloes has "a step, a shoulder, and a power law high-mass tail"; it is
Poisson at high mass but sub-Poisson for ⟨N⟩ < 4; ⟨N_s⟩ ∝ M^b with b ~ 1
(Kravtsov et al. 2004, arXiv:astro-ph/0308519) [src]. Zheng et al. 2005
(arXiv:astro-ph/0408564) find the central–satellite split in an SPH simulation
and a semi-analytic model, with M_1 ≈ 14 M_min (SPH) or 18 M_min (SA), and a
conditional galaxy mass function that is not Schechter because of the central
"bump" [src].

The five-parameter form, as the Asgari review writes it [src: Eqs. 51–52 of
arXiv:2303.08752]:

- ⟨N_c(M)⟩ = ½ [1 + erf( log₁₀(M/M_min) / σ_log₁₀M )]
- ⟨N_s(M)⟩ = Θ(M − M_0) [(M − M_0)/M_1]^α

with Bernoulli centrals and, usually, Poisson satellites; the three-parameter
Zehavi et al. 2004 form is the limit σ_log M = 0, M_0 = 0 [src: Sect. 4.1]. The
"central condition" (no satellite without a central) is incompatible with
Bernoulli centrals plus Poisson satellites; the usual fix modifies the
satellite distribution, so that the ⟨N_s⟩ of Eq. 52 is no longer the true mean
and a covariance Cov(N_c, N_s) = λ(1 − p) appears [src: Sect. 4.1 and its
occupation-statistics table, arXiv:2303.08752].

**Tracer-specific forms.** Red, luminous samples are mostly centrals; blue or
emission-line samples need a central occupation that falls at high mass [src:
Sect. 4.1 of arXiv:2303.08752]. For eBOSS ELGs the baseline shape fitted to a
semi-analytic model has "a decaying occupation of central ELGs at high halo
masses"; w_p captures most of the effect of the satellite distribution and
profile, ξ_2 most of the velocity effects, and the mean HOD shape is
subdominant (Avila et al. 2020, arXiv:2007.09012) [src]. The DESI One-Percent
ELG analysis compares four central forms with a Bernoulli draw: Gaussian in log
M (GHOD), log-normal (LNHOD), Gaussian below M_c with a power law (M/M_c)^γ
above (SFHOD), and a Gaussian multiplied by [1 + erf(γ(log₁₀M − log₁₀M_c)/(√2
σ_M))], the "modified High Mass Quenched" model derived from the HMQ model with
the quenching factor sent to infinity (mHMQ) [src: Sect. 3.1, Eqs. 2–5 of
arXiv:2306.06319]. The fitted extensions (conformity, galaxies beyond R_vir,
velocity bias) are in `results.md` sections 1 and 3.

**Extensions in current use.** Velocity bias of centrals and satellites,
satellite-profile modulation, incompleteness, and secondary-property
("decorated") occupation; the DESI LRG and QSO fits of the One-Percent survey
use AbacusSummit templates via AbacusHOD and fit 0.15 < r < 32 h⁻¹Mpc in
redshift space (Yuan et al. 2024, arXiv:2306.06314) [src]. A multi-tracer HOD
(MTHOD) fits eBOSS LRG, ELG and QSO jointly with their cross-correlations (Alam
et al. 2020, arXiv:1910.05095) [src]. The DESI and Flagship implementations
used for mocks are in `cosmo-simulations-mocks` section 6.

**CLF.** Yang et al. 2003 (arXiv:astro-ph/0207019) introduce the conditional
luminosity function Φ(L|M) dL, the number of galaxies with luminosity in [L, L
+ dL] in a halo of mass M, constrained by the luminosity function and
luminosity-dependent clustering [src]. Integrated above a threshold it gives an
HOD, and it carries the luminosity function as data; Cacciato et al. 2009
(arXiv:0807.4932) show that a CLF fitted to clustering in a (Ω_m, σ8) = (0.3,
0.9) cosmology over-predicts the SDSS lensing signal, while (0.238, 0.734) fits
it [src], which is the origin of the clustering + lensing method of section 11.
Zu & Mandelbaum 2015 (arXiv:1505.02781) generalise the HOD to stellar mass with
incompleteness ("iHOD"), using ~80% more galaxies than threshold HODs [src].

## 7. Abundance matching and the stellar-to-halo mass relation
<!-- key: abundance-matching-and-the-stellar-to-halo-mass -->

**Principle.** Vale 2004 (arXiv:astro-ph/0402500) replace linearity between
light and mass with monotonicity between galaxy luminosity and halo or subhalo
mass; their halo/subhalo mass–luminosity relation is a double power law tending
to L ∝ M⁴ at low mass and L ∝ M^0.28 at high mass [src]. Conroy et al. 2006
(arXiv:astro-ph/0512234) match luminosity to V_max, taken at accretion for
subhaloes (V_max,acc), and reproduce SDSS and DEEP2 clustering for 0.1 < r_p <
10 h⁻¹Mpc and Lyman-break galaxies at z ~ 3–5 [src]. Abundance matching
"assumes that every dark matter halo or subhalo above a specific mass threshold
hosts one galaxy" (Behroozi et al. 2010, arXiv:1001.0015) [src].

**Choice of halo property and scatter.** Reddick et al. 2013 (arXiv:1207.2160),
on Bolshoi with SDSS clustering and the conditional stellar mass function of
groups, rule out several proxies because their satellite fractions disagree
with the data and favour the peak circular velocity with 0.20 ± 0.03 dex
scatter in stellar mass at fixed V_peak [src]. Lehmann et al. 2017
(arXiv:1510.05651) interpolate between peak mass and peak V_max, which sets the
concentration dependence and therefore the assembly bias of an
abundance-matched catalogue, and show that SDSS clustering and satellite
fractions constrain this together with the scatter [src].

**Parametric SHMR fits (abundance matching or HOD with a stellar-mass
function).** Moster et al. 2010 (arXiv:0903.4682) fit a parameterised
stellar-to-halo relation to the stellar mass function and find clustering adds
no strong constraint [src]. Behroozi et al. 2010 (arXiv:1001.0015) give the
uncertainty budget (`systematics.md` sections 4–5) [src].. Multi-epoch
abundance matching (Moster et al. 2013, arXiv:1205.5807) follows satellites
from their accretion time [src]. Behroozi et al. 2013 (arXiv:1207.6105) extend
the relation to star formation histories from z = 0 to 8 [src].

**Joint lensing + clustering + abundance.** Leauthaud et al. 2012
(arXiv:1104.0928), COSMOS z = 0.2–1, is the first joint analysis of the three,
"carefully accounting for sample variance and for scatter between stellar and
halo mass" [src]. The DES Y3 analysis fits log M*(M_h) = log(ε M_1) +
f[log(M_h/M_1)] − f(0), f(x) ≡ −log(10^(αx) + 1) + δ [log(1 + exp(x))]^γ / [1 +
exp(10^(−x))], from ~100 kpc to ~100 Mpc (Zacharegkas et al. 2025,
arXiv:2506.22367) [src].

Results by survey are in `results.md` section 2.

## 8. Empirical, semi-analytic and hydrodynamical models
<!-- key: empirical-semi-analytic-and-hydrodynamical -->

The review orders approaches from fewest to most physical assumptions: HOD/CLF
and abundance matching, empirical models of formation histories, semi-analytic
models, hydrodynamical simulations, and stresses their complementarity [src:
Sect. 2.2–2.4 of arXiv:1804.03097].

**Empirical models of galaxy formation histories.** These assign star formation
(not stellar mass) to haloes along merger trees and fit many observables at
once.

| Model | What is parameterised | Constrained by | Selected findings | Reference |
|---|---|---|---|---|
| Age distribution matching | at fixed luminosity, colour monotonic in z_starve, a halo-assembly redshift | SDSS M_r < −19 statistics | halo and galaxy assembly "are indeed correlated" | Hearin et al. 2013, arXiv:1304.5557 [src] |
| EMERGE | SFR from halo growth rate times an instantaneous baryon conversion efficiency; delayed-then-rapid satellite quenching; tidal disruption | data out to high z, model selection statistics | at fixed halo mass passive galaxies have higher stellar mass; intracluster mass up to 8 times the central | Moster et al. 2018, arXiv:1705.05373 [src] |
| UniverseMachine | SFR from potential-well depth, assembly history and redshift | SMFs, SFRs, quenched fractions, UV luminosity functions, IRX-UV, auto- and cross-correlations by star-formation class, environmental quenching, 0 < z < 10 | galaxy assembly correlates strongly with halo assembly; massive quenched galaxies sit in more massive haloes than star-forming ones at fixed stellar mass; Planck cosmologies give up to 0.3 dex lower SHMR at early times | Behroozi et al. 2019, arXiv:1806.07893 [src] |

**Semi-analytic models (SAMs).** Review: Somerville et al. 2015
(arXiv:1412.2712), which finds models converged on cosmological accretion,
stellar winds most efficient at low mass, black-hole feedback at high mass, and
merging and environment, all "phenomenological implementations" tuned to
observations [src]. Examples: the Munich model recalibrated to Planck
(Henriques et al. 2015, arXiv:1410.0365) [src]; GALFORM with a top-heavy
starburst IMF (Lacey et al. 2016, arXiv:1509.08473) [src]; Shark, open source
and modular, which finds SAM halo baryon fractions much higher than EAGLE's
(Lagos et al. 2018, arXiv:1807.11180) [src]. The nIFTy comparison ran 12 SAMs
and 2 HOD models on one simulation and one set of merger trees without
recalibration: stellar mass functions, sSFR, stellar-to-halo ratios and orphan
abundances scatter widely, "much larger than seen in previous comparison
studies" (Knebe et al. 2015, arXiv:1505.04607) [src].

**Hydrodynamical simulations.** Review: Crain et al. 2023 (arXiv:2309.17075):
current suites "broadly reproduce the observed spatial clustering of galaxies"
once subgrid feedback is calibrated; similar galaxy populations emerge from
dissimilar feedback, with different gas flows, so circumgalactic-gas data are
the discriminant [src]. Applied to survey tracers: DESI-like LRG and ELG
selections in IllustrisTNG follow their baseline HODs but deviate in satellite
distribution, velocity bias and secondary biases, with concentration- and
environment-based assembly bias and a 10–15% shuffling excess in LRG clustering
of modest significance (Yuan et al. 2022, arXiv:2202.12911) [src]. Simulation
codes and suites are in `cosmo-simulations-mocks` section 3.

## 9. Assembly bias and secondary dependencies
<!-- key: assembly-bias-and-secondary-dependencies -->

Vocabulary: *halo assembly bias* (halo clustering at fixed mass depends on
another property), *galaxy assembly bias* (galaxy content depends on it),
*conformity* (correlated properties of centrals and satellites, or of
neighbouring haloes). The review keeps these distinct [src: Sect. 5.3–5.4 and
7.2 of arXiv:1804.03097].

| Result | Content | Reference |
|---|---|---|
| Halo assembly bias, formation time | below ~10¹³ M_⊙/h clustering depends strongly on formation time; at 10¹¹ M_⊙/h the oldest 10% are > 5 times more correlated than the youngest 10% | Gao et al. 2005, arXiv:astro-ph/0506510 [src] |
| Concentration | b(c, M\|z) = b(M\|z) b(c\|M/M*), sign change at M*: concentrated haloes cluster more below M*, less above | Wechsler et al. 2006, arXiv:astro-ph/0512416 [src] |
| Halo definition | amplitude and sense depend on Δ; Δ ~ 20m–40m removes most concentration dependence below 10¹² h⁻¹M_⊙; no definition removes all forms | Villarreal et al. 2017, arXiv:1705.04327 [src] |
| Causes at low mass | splashback subhaloes give two thirds; the rest from ≲ 10% of haloes in dense regions slowed by tidal fields and fast ambient matter (web view: `cosmo-cosmic-web`) | Mansfield et al. 2019, arXiv:1902.00030 [src] |
| Galaxy assembly bias, shuffling | ±10% in two-point correlations of a SAM on Millennium; fixing formation redshift or concentration as well does not remove it | Croton et al. 2007, arXiv:astro-ph/0605636 [src] |
| Mass-only HOD on biased mocks | inferred HOD significantly wrong; sizes in `systematics.md` section 7 | Zentner et al. 2014, arXiv:1311.1818 [src] |
| Decorated HOD | "minimally expand the parameter space and maximize the independence between traditional and novel HOD parameters" | Hearin et al. 2016, arXiv:1512.03050 [src] |
| Environment-based terms | concentration alone "cannot capture the full galaxy assembly bias effect"; concentration- and environment-based HOD terms; both kinds present for DESI-like tracers in TNG | Yuan et al. 2021, arXiv:2010.04182; arXiv:2202.12911 [src] |

Detection strategies: (i) fit decorated or extended HODs to clustering; (ii)
split haloes or groups at fixed mass by a secondary property and compare
large-scale bias from clustering and lensing; (iii) measure the HOD directly as
a function of large-scale density with groups plus lensing; (iv) conformity
statistics. Results and their critiques are in `results.md` section 4 and
`open-questions.md`.

## 10. Satellite fractions and kinematics
<!-- key: satellite-fractions-and-kinematics -->

**Central/satellite classification.** Group finders assign galaxies to haloes
and label centrals and satellites: the halo-based finder of Yang et al. 2007
(arXiv:0707.4640) iterates mass-to-light ratios to set group size and velocity
dispersion in redshift space [src]; the Self-Calibrated Group Finder calibrates
its parameters on the clustering of the sample itself (arXiv:2610.20919) [src].
Catalogue facts are in `surveys-and-data.md` section 3.

**Satellite fraction** is constrained by the one-halo term of clustering, by
group catalogues and by satellite counts, and is degenerate with the scatter of
the central relation; Reddick et al. 2013 rule out abundance-matching proxies
by their satellite fractions (arXiv:1207.2160) [src].

**Satellite kinematics.** Satellites trace the potential of the central's halo:
kinematics, group catalogues, lensing and abundance matching give mass
relations agreeing "typically within a factor of two" (More et al. 2011,
arXiv:1003.3203) [src]. Basilisk, a Bayesian hierarchical forward model of
satellite kinematics and abundance, models interlopers, adds the kurtosis of
the line-of-sight velocities, breaks the mass–anisotropy degeneracy and is
stated to be "insensitive to halo assembly bias" (Mitra et al. 2024,
arXiv:2409.03105) [src].

**Velocity bias and radial distribution.** BOSS CMASS redshift-space clustering
requires centrals moving relative to the halo core and satellites slower than
the dark matter (Guo et al. 2015, arXiv:1407.4811) [src]; values are in
`results.md` section 3. Satellites are usually placed on the host's NFW profile
with a free concentration; the Basilisk S8 analysis stresses "the importance of
correctly modeling the satellite radial profile in any analysis involving
small-scale information" (arXiv:2512.14889) [src]. Orphan satellites are a
modelling choice that varies widely between SAMs (arXiv:1505.04607) [src].

## 11. Galaxy–galaxy lensing with clustering
<!-- key: galaxy-galaxy-lensing-with-clustering -->

**Observables.** Projected clustering w_p(r_p) of a lens sample and its excess
surface density ΔΣ(R) measured with background sources. On large scales w_p ∝
b² and ΔΣ ∝ b r_cc, so the ratio constrains the matter clustering amplitude; on
small scales both are set by the occupation (one-halo term) [der: from the
linear-bias limit of the halo model, section 5].

**Two strategies.**

1. Large scales only, with a cross-correlation coefficient close to unity
   outside a few virial radii: Mandelbaum et al. 2013 (arXiv:1207.1120) remove
   scales below 2 (lensing) and 4 h⁻¹Mpc (clustering), detect scale-dependent
   bias for the luminous samples, and find σ8 (Ω_m/0.25)^0.57 = 0.80 ± 0.05
   with statistical and systematic errors comparable [src]. Its perturbative
   version (hybrid EFT) is in `cosmo-weak-lensing`.
2. All scales with a galaxy–halo model:

| Framework | Data | Reference |
|---|---|---|
| CLF + analytic halo model | SDSS | arXiv:1206.6890; Cacciato et al. 2013, arXiv:1207.0503 [src] |
| Emulated halo statistics (Dark Emulator) + HOD | HSC-Y1 × SDSS | Miyatake et al. 2022, arXiv:2111.02419 [src] |
| Conditional stellar mass function + simulation-calibrated halo model with non-linear bias, exclusion, baryons | KiDS-1000 | Dvornik et al. 2023, arXiv:2210.03110 [src] |
| Simulation-based HOD with assembly bias (AbacusSummit) | DESI DR1 × DES, KiDS, HSC | Lange et al. 2025, arXiv:2512.15962 [src] |
| Extended SHAM (SHAMe): V_peak–M* scatter σ, orphan lifetime t_merger, two assembly-bias parameters f_k,c+s and f_k,c−s, and β [src: Sect. 2.1, Eq. 1]; emulated, gravity-only ΔΣ; recovers TNG300 cosmology within 1σ with or without ΔΣ below 1.4 h⁻¹Mpc [src: Sect. 4] | GAMA × KiDS-1000 | Mahony et al. 2025, arXiv:2507.01601 |
| Satellite kinematics + luminosity function (Basilisk) | SDSS DR7 | arXiv:2512.14889 [src] |

**"Lensing is low".** Clustering-trained models of BOSS CMASS predict lensing
20–40% above the CFHTLenS + CS82 measurement on r < 10 h⁻¹Mpc (Leauthaud et al.
2017, arXiv:1611.08606) [src]. Resolutions divide into cosmology (lower S8) and
galaxy–halo modelling (assembly bias, satellite segregation, selection,
baryons): numbers in `results.md` section 5, the debate in `open-questions.md`
section 1.

**Analysis practice in current joint fits** (read in the method sections):

| Analysis | Galaxy model and its freedom | Scales | Covariance, likelihood | Blinding | Reference |
|---|---|---|---|---|---|
| DESI DR1 BGS + LRG × DES, KiDS, HSC | AbacusSummit haloes; Zheng-type HOD with an LRG colour-incompleteness factor f_Γ [src: Eqs. 6–7]; decorated-HOD central and satellite assembly-bias parameters A_cen, A_sat ∈ [−1, 1] split at the median concentration [src: Eqs. 8–9]; satellite spatial bias η = c_sat/c and velocity bias α_s; flat ranges in its Table 1 | clustering to 0.4, lensing to 2.5 h⁻¹Mpc | predictions tabulated with TabCorr 1.1.2 | data-vector masking: ΔΣ multiplied by an unknown A_lens drawn uniformly in [0.85, 1.15] before unmasking; mass resolution judged insufficient for BGS1 during the masked phase [src: Sect. III.5] | arXiv:2512.15962 [src: Sect. III.2, Table 1] |
| same | stated shortcomings: baryons neglected (Illustris-level suppression moves S8 and Ω_m by < 0.3σ), smooth satellite profiles neglect subhaloes (under-predicts small-scale lensing), assembly bias only through concentration | — | — | — | arXiv:2512.15962 [src: Sect. III.2] |
| HSC-Y1 × SDSS | Dark Emulator + HOD with nuisance parameters; off-centring and incompleteness as extended models | (2, 3) h⁻¹Mpc for (w_p, ΔΣ), larger than virial radii of massive haloes; (4, 6) and (8, 12) as tests | — | two tiers: three shape catalogues of which one is true, and no data–model or external comparisons, centred posteriors; publication committed before unblinding | arXiv:2111.02419 [src: Sect. IV.3, Sect. V] |
| BOSS × DES Y3, HSC Y1, KiDS-1000 | Dark Emulator HOD; theoretical error budget for baryons (concentration normalisation f_conc = 0.84 fiducial, uncertainty from 0.84 vs 0.61) and for assembly bias (difference between a vanilla HOD and a 10-parameter AbacusHOD with velocity bias and environment-based secondary bias), each wide enough to include zero effect | 0.15 < R < 60 h⁻¹Mpc and R > 5.25 h⁻¹Mpc | — | — | arXiv:2202.07440 [src: Sect. 4.1–4.2] |
| DESI One-Percent LRG and QSO | AbacusHOD baseline plus extensions | 0.15 < r < 32 h⁻¹Mpc in ξ(r_p, π) | Gaussian χ² plus a half-normal number-density term with σ_n = 0.1 n_data [src: Eqs. 10–12]; covariance from 1800 AbacusSummit 500 h⁻¹Mpc boxes, rescaled to jackknife diagonals; Hartlap correction ~6% | — | arXiv:2306.06314 [src: Sect. 5] |

Two practices differ across groups: the theoretical-error approach (Amon et
al.) widens the error budget instead of freeing the model, while the
simulation-based approach (Lange et al.; Yuan et al.) frees assembly-bias and
phase-space parameters and fits them. Both leave baryonic effects mostly to
scale cuts.

## 12. Codes
<!-- key: codes -->

| Code | Purpose | Reference |
|---|---|---|
| Colossus | cosmology, peak height, bias, mass function, SO radii and masses, profiles, concentration, splashback; > 40 fitting functions | Diemer 2018, arXiv:1712.04512 [src] |
| Halotools | open-source package for the galaxy–halo connection; decorated HODs | Hearin et al. 2016, arXiv:1512.03050 [src] |
| AbacusHOD | forward-models clustering by populating AbacusSummit; used for DESI One-Percent HODs | arXiv:2306.06314 [src] |
| TabCorr | tabulated halo correlation functions convolved with an HOD; version 1.1.2 in the DESI DR1 lensing analysis | arXiv:2512.15962 [src: Sect. III.2] |
| Dark Emulator | emulated HMF, halo–matter and halo–halo correlations over wCDM; HOD at equation level | Nishimichi et al. 2019, arXiv:1811.09504 [src] |
| BNL | beyond-linear halo bias in the halo model | Mead 2021, arXiv:2011.08858 [src] |
| hmfc | HMF fitting formula from 10⁻⁶ to 10¹⁵·⁵ M_⊙ | Zheng et al. 2026, arXiv:2607.05505 [src] |
| Aletheia | HMF emulator with evolution mapping | Fiorilli et al. 2026, arXiv:2609.10665 [src] |
| UniverseMachine | empirical model; public data release DR1 | Behroozi et al. 2019, arXiv:1806.07893 [src] |
| Shark | open-source modular SAM (C++11, OpenMP) | Lagos et al. 2018, arXiv:1807.11180 [src] |
| Basilisk | Bayesian hierarchical satellite-kinematics forward model | Mitra et al. 2024, arXiv:2409.03105 [src] |

## Not verified
<!-- key: not-verified -->

- Zheng et al. 2007 satellite profiles were not read in the original paper.
  (The Zehavi 2004 and Tinker 2005 exclusion schemes, the Sheth–Tormen mass
  function and bias, NFW and the Duffy and Tinker 2010 fits were read in their
  bodies on 2026-10-16.)
- Searched 2026-10-16: HSC-Y3 results are in `results.md` §5; no DES Y6 or
  KiDS-Legacy occupation-model analysis was found (DES Y6 cuts at 4–6 h⁻¹Mpc).
