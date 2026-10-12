# Galaxy-cluster cosmology — physics and methods

Scope: what cluster abundance, clustering, gas fractions and profiles measure, the models and likelihoods in current use, and the public codes.
Snapshot: 2026-10-07

Reviews to start from: Allen, Evrard & Mantz 2011 (arXiv:1103.4829) for the method as a whole and its pre-Planck results; Pratt et al. 2019 (arXiv:1902.10837) for the mass scale, the mass-estimation methods and their biases. No review of cluster cosmology dated after June 2025 was found in a date-sorted title search (2026-10-09).

## 1. What is measured and why it constrains cosmology

The number density of haloes above about 1e14 M_sun falls exponentially with mass, so the abundance of clusters as a function of mass and redshift responds steeply to the amplitude of matter fluctuations and to the matter density. Counts in a survey are

    dN / (dz dΩ dO) = (dV / dz dΩ) ∫ dM  n(M, z)  P(O | M, z)  S(O, z, sky position)

where n(M, z) is the halo mass function, P(O | M, z) the stochastic observable–mass relation and S the selection function. The three ingredients are the three places where an analysis can fail: the mass function is theory, the observable–mass relation is the mass calibration, and the selection is survey-specific.

Four cluster probes are in use.

| Probe | Sensitive to | Limiting ingredient | Where the numbers are |
|---|---|---|---|
| Abundance N(O, z) | σ8 and Ω_m along σ8 Ω_m^α, growth history, Σm_ν, w, modified gravity | absolute mass scale and selection | `results.md` |
| Clustering of clusters | halo bias, hence mass (self-calibration); Ω_m through the shape | sample size, photo-z, RSD modelling | `results.md`, section 7 below |
| Gas-mass fraction of relaxed clusters | distances (f_gas ∝ d^1.5 in the reference cosmology) and Ω_b/Ω_m | gas depletion factor, hydrostatic mass at r2500 | `results.md` |
| Outer profile, splashback, infall region | accretion rate, halo definition, gravity; a test of the selection | optical selection effects, statistical power | section 9 below |

The count degeneracy direction is flatter than the cosmic-shear one. Analyses quote the best-constrained combination with their own exponent: 0.3 with pivot 0.27 (Planck 2013, arXiv:1303.5080), 0.17 (Weighing the Giants, arXiv:1407.4516), 0.2 then 0.25 (SPT, arXiv:1812.01679, arXiv:2401.02075), 0.25 with pivot 0.33 (arXiv:1904.07887) [src]. The standard S8 = σ8 (Ω_m/0.3)^0.5 is usually quoted in addition and has a larger error: 0.029 against 0.016 for the optimal SPT combination [src, arXiv:2401.02075].

## 2. Mass definitions and conventions

- Spherical-overdensity masses: M_Δ = (4π/3) Δ ρ_ref r_Δ³, with ρ_ref the critical density at the cluster redshift (suffix c) or the mean matter density (suffix m). X-ray and SZ work uses M500c; optical and lensing work M200m or M200c; relaxed-cluster f_gas work r2500 (arXiv:1402.6212).
- Tinker et al. 2008 argue that spherical-overdensity masses are more directly linked to cluster observables than friends-of-friends masses (arXiv:0803.2706). Conversion between definitions requires a concentration model; Hu & Kravtsov 2003 give a fitting formula for it (arXiv:astro-ph/0203169).
- Inner profiles are most self-similar when radii are scaled by R200c, outer profiles when scaled by R200m (Diemer & Kravtsov 2014, arXiv:1401.1216). This is the physical reason the two conventions coexist.
- Units: M_sun, M_sun/h, or M_sun/h70 in SPT catalogue papers (arXiv:2311.07512). A factor of h between two quoted mass limits is about 40% for h ≈ 0.7 [der: 1/0.7 = 1.43]. Check before comparing mass thresholds.
- Mass bias: (1 − b) = M_proxy / M_true, where M_proxy comes from a scaling relation calibrated on X-ray hydrostatic masses. A smaller (1 − b) means heavier clusters and a higher σ8 from the same counts. The reference relation matters: with the same lensing data (1 − b) is 0.89 ± 0.04 for a Chandra-calibrated relation and 0.76 ± 0.04 for the XMM one [src, arXiv:2402.04006].
- Hydrostatic bias in simulation papers is often written with the opposite sign, as a negative fractional offset of the hydrostatic mass (arXiv:2409.07849): b_HSE ≈ −0.2 there corresponds to (1 − b) ≈ 0.8 here.

## 3. Halo mass function and halo bias

The mass function is written dn/dM = f(σ) (ρ_m / M) d ln σ⁻¹/dM, with σ(M, z) the rms linear fluctuation in a top-hat enclosing M. "Universality" is the statement that f depends on cosmology and redshift only through σ.

| Reference | What it provides | Stated accuracy and limits | Flag |
|---|---|---|---|
| Tinker et al. 2008, arXiv:0803.2706 | f(σ) for spherical-overdensity masses at many Δ, from collisionless flat ΛCDM simulations, z ≲ 2 | ≲ 5% at z = 0 for 1e11 < M < 1e15 M_sun/h; improves earlier fits by 10–20%; **not universal**: the amplitude of the "universal" function falls by 20–50% from z = 0 to 2.5 depending on the mass definition | [src] |
| Tinker et al. 2010, arXiv:1001.3162 | large-scale bias b(ν, Δ), normalised so that the bias of all matter is unity with the 2008 mass function | about 6% scatter; FoF (linking length 0.2) haloes have bias about 10% lower than Δ = 200; the bias function evolves very weakly with redshift; the peak-background split leaves about 20% residuals | [src] |
| Bocquet et al. 2016, arXiv:1502.07357 | hydrodynamical and dark-matter-only fits from Magneticum boxes up to (3818 Mpc)³ | baryons lower masses and hence abundance at fixed mass; the effect vanishes at z ~ 2 and for M200m ≳ 1e14 M_sun; using this DM-only fit instead of Tinker 2008 shifts a Planck-like analysis by Δσ8 ≈ 0.02 | [src] |
| Euclid Collaboration (Castro et al.) 2023, arXiv:2208.02174 | fit calibrated with a Bayesian treatment of numerical systematics, including scale-free simulations to trace non-universality | sub-percent over 9 ΛCDM variants including massive neutrinos; the halo-finder choice is the one effect that "could lead to biased cosmological inference" | [src] |

Practice in current analyses, as far as the abstracts read state it: the KiDS-1000 AMICO analysis marginalises over mass-function uncertainty (arXiv:2507.14285); the SPT analysis adds 2% in quadrature for baryonic effects on the lensing-mass model (arXiv:2310.12213); the ACT f_NL analysis uses a Log–Edgeworth non-Gaussian mass function (arXiv:2602.03917). Which mass function each headline analysis adopts was not read in the paper bodies; see "Not verified".

Mass-function emulators and new prescriptions published between June 2025 and October 2026 were returned by a date-sorted search (titles: "Evolution mapping III: A new recipe for the halo mass function"; "Aletheia: Emulating the halo mass function with evolution mapping"; "CSST Cosmological Emulator II: Generalized Accurate Halo Mass Function Emulation"; "Emulation of the Halo Mass Function with Neural Networks"; "Euclid: Impact of halo mass-conversion model assumptions on galaxy cluster number-count analyses"). They are leads, not read and not cited.

## 4. Observables and observable–mass relations

| Selection | Detection observable | Mass proxy and calibration | Strength | Characteristic failure |
|---|---|---|---|---|
| X-ray (ROSAT, XMM, eROSITA) | extended soft X-ray emission | L_X, T_X, M_gas, Y_X = M_gas T_X; now weak lensing (arXiv:2402.08458) | large samples, low-scatter follow-up proxies | selection depends on core state and morphology; point sources; selection function built from simulated skies (arXiv:2402.08457) |
| Thermal SZ (Planck, SPT, ACT) | Compton-y decrement through a matched filter; SPT significance ξ, ACT and Planck S/N | Y_SZ or ξ; hydrostatic X-ray (Planck), weak lensing (SPT, ACT) | mass limit that varies slowly with redshift | radio and dust infill, relativistic corrections |
| Optical richness (redMaPPer λ, AMICO λ*) | red-sequence or matched-filter overdensity | stacked weak lensing | lowest mass threshold, largest samples | projection effects correlated with lensing and clustering; miscentring |
| Weak-lensing shear peaks (HSC) | aperture-mass peak height ν | the selection observable is itself the lensing signal | selection "solely depends on gravity" (arXiv:2406.11970) | small samples (129 clusters [src]) |
| Infrared (MaDCoWS) | galaxy overdensity at z ~ 1 | CMB lensing (arXiv:2009.07772) | reaches z > 1 | selection not modelled for cosmology |

The thermal SZ signal measures the line-of-sight integral of electron pressure, y = (σ_T / m_e c²) ∫ P_e dl, and its integral over the cluster measures the total thermal energy of the gas. Self-similar collapse predicts a power law in mass and in E(z). In the Planck parametrisation the self-similar mass slope is quoted as 1.8, and a joint Planck + SPT fit finds α_SZ = 1.49 +0.07/−0.10, about 4σ away [src, arXiv:2112.03606].

X-ray hydrostatic mass: M(<r) = −(k T r / G μ m_p) (d ln ρ_gas/d ln r + d ln T/d ln r). It is biased low by non-thermal pressure and by temperature inhomogeneity, and its absolute scale follows the X-ray temperature calibration (see `systematics.md`).

Scaling relations are modelled as power laws in mass and in E(z) or (1 + z), with lognormal intrinsic scatter and, in multi-observable analyses, correlated scatter between observables. DES Y3 × SPT cross-matching shows that a simple lognormal scatter is inadequate for richness (arXiv:2502.12914).

## 5. Count likelihoods and covariance

- Forward population model. The current standard is a Bayesian hierarchical model in which the survey observable (ξ, X-ray flux or count rate, richness) and the follow-up observables (shear profile, Y_X, velocity dispersion) are drawn from a joint scaling relation with correlated scatter, and the selection is applied to the detection observable. The SPT framework is described in Bocquet et al. 2024 (arXiv:2310.12213) and applied in arXiv:2401.02075; Mantz et al. 2010 (arXiv:0909.3098) is the statistical-methods paper for the X-ray samples.
- Stacked versus individual lensing. SPT uses per-cluster shear profiles inside the population model (arXiv:2310.12213), and the Planck × DES analysis also works with shear profiles (arXiv:2509.02068). Richness-selected analyses (SDSS, DES Y1, KiDS AMICO) stack the lensing signal in bins of richness and redshift (arXiv:1805.00039, arXiv:2507.14285). Stacking is where the optical selection bias enters: the mean lensing profile of a richness-selected stack is not that of a mass-selected sample of the same mean mass.
- Poisson versus Gaussian. Sample variance (the modulation of counts by long-wavelength density modes, proportional to halo bias) is comparable to or larger than shot noise for surveys that reach low masses, and is usually more important than shot noise for constraints on w from z < 1 clusters (Hu & Kravtsov 2003, arXiv:astro-ph/0203169). On 1000 PINOCCHIO catalogues, a Poisson likelihood always underestimates parameter errors for Rubin- or Euclid-like surveys; a Gaussian likelihood with sample covariance is robust over a wide range of binnings, and the Gauss–Poisson compound likelihood brings no gain at higher cost [src] (Payerne et al. 2023, arXiv:2210.11093).
- Counts and clustering of clusters are found to be uncorrelated in Euclid-like mocks, so their likelihoods multiply (arXiv:2510.13509).
- Joint analyses with 3×2pt need the cross-covariance and a common nuisance model: SPT clusters + DES Y3 3×2pt uses 52 astrophysical nuisance parameters [src, arXiv:2412.07765]; the DES Y6 strategy is validated on Cardinal mocks (arXiv:2503.13631).
- Simulation-based inference is entering the field: the XXL analysis with HSC lensing uses DELFI with 12 parameters and reports an extra 3% systematic from neural-network stochasticity [src, arXiv:2602.11989]; the reanalysis of DES Y1 uses a simulation-based forward model of the optical selection (arXiv:2510.25706).

## 6. Mass calibration

| Method | Measures | Precision reached | Main limitation | Key references |
|---|---|---|---|---|
| Weak lensing, per cluster or stacked | projected mass through tangential reduced shear, ΔΣ(R) = Σ_crit γ_t | 5.0% on the richness–mass normalisation in DES Y1 [src, arXiv:1805.00039]; 7% on the ACT normalisation with DES Y3 [src, arXiv:2512.18935]; 8% mass scale in Weighing the Giants [src, arXiv:1407.4516]; 8% mean mass precision in KiDS AMICO [src, arXiv:2507.14285] | model bias of profile fits, source redshifts, miscentring, contamination by members, selection bias of stacks | arXiv:1011.1681, arXiv:1502.01883, arXiv:2310.12213, arXiv:2409.02783 |
| CMB lensing of clusters | mass from the distortion of the CMB gradient behind the cluster; no source redshifts needed | 4.2σ for 677 clusters at mean z = 1.08 [src, arXiv:2009.07772]; 3.1σ for SPT-SZ [src, arXiv:2111.07491]; (1 − b) = 0.71 ± 0.10 for 433 Planck clusters [src, arXiv:1904.07887] | signal-to-noise per cluster; contamination of the estimator by the cluster's own SZ signal | arXiv:2404.02153 |
| X-ray hydrostatic | thermal pressure support | — | hydrostatic bias, temperature calibration | arXiv:1805.00034, arXiv:1509.02162 |
| Dynamical (velocity dispersion) | galaxy kinematics | used by ACT in 2013 with a 15% dynamical-mass bias marginalised [src, arXiv:1301.0816] | velocity bias, interlopers | arXiv:1902.10837 |
| Clustering (self-calibration) | bias, hence mean mass | (1 − b) = 0.62 +0.14/−0.11 from Planck cluster clustering [src, arXiv:2302.14074] | sample size | arXiv:2510.14464 |

Weak-lensing mass is not an unbiased estimator of spherical-overdensity mass. Fitting a spherical NFW profile to the reduced shear of about 1e4 simulated haloes gives a bias of 5–10% and an intrinsic scatter of about 20% for massive clusters and up to about 30% for groups, from triaxiality and from correlated and uncorrelated large-scale structure [src] (Becker & Kravtsov 2011, arXiv:1011.1681). In Euclid-like conditions on N-body haloes the mean bias is −14.6 ± 1.7 % for M200c > 5e13 M_sun at z < 1 [src, arXiv:2409.02783]. Modern analyses therefore calibrate a relation between weak-lensing mass and halo mass on simulations and carry its bias and scatter as nuisance parameters (arXiv:2310.12213, arXiv:2402.08455).

The stacked-lensing model of McClintock et al. 2019 (arXiv:1805.00039) is the reference for richness-selected samples: ⟨M200m | λ, z⟩ = M0 (λ/40)^F ((1 + z)/1.35)^G, with M0 = [3.081 ± 0.075 (stat) ± 0.133 (sys)] × 1e14 M_sun, F = 1.356 ± 0.051 ± 0.008, G = −0.30 ± 0.30 ± 0.06 [src], from 4 × 3 bins at λ ≥ 20 and 0.2 ≤ z ≤ 0.65 and a semi-analytic covariance. It is also the calibration behind the DES Y1 result that failed (see `results.md`), which is why its systematics list matters more than its precision.

## 7. Clustering of clusters

Clusters are highly biased tracers: measured biases run from 2.95 ± 0.21 to 4.34 ± 0.62 for eRASS1 luminosity-limited samples [src, arXiv:2402.08460] and 5.30 ± 0.24 for SPT-3G clusters at 0.25 < z < 1.1 [src, arXiv:2610.08947]. On large scales P_cc(k) = b² P_m(k); since b(M) is predicted (section 3), the clustering amplitude measures the mean mass without any lensing or hydrostatic assumption.

Statistics in use: projected correlation function with a halo-occupation model (eRASS1, arXiv:2402.08460); redshift-space two-point function over 10–150 Mpc/h (Planck clusters, arXiv:2302.14074); angular correlation function and angular power spectrum of photometric clusters (AMICO KiDS-DR3, arXiv:2310.12224); cluster auto-correlation with an analytic covariance (SPT-3G, arXiv:2610.08947); cluster–galaxy and cluster–shear cross-correlations inside a multiprobe data vector (DES Y1 and Y3, arXiv:2010.01138, arXiv:2503.13632).

What clustering adds, according to forecasts that differ in size: in Euclid-like mocks adding clustering raises the figure of merit by more than 300% [src, arXiv:2510.13509, **forecast**]; for future SZ samples of 33000 to 140000 clusters with current mass–observable priors, σ(w) improves by factors of 1.023 ± 0.007 to 1.079 ± 0.011 and σ(Ω_m) by 1.068 to 1.145, and the gain on w "largely vanishes" when the mass–observable priors are tightened by a factor of two [src, arXiv:2510.14464, **forecast**]. The two are not in contradiction: clustering helps in proportion to how poorly the mass–observable relation is known otherwise.

The non-Gaussian mass function is constrained with the same count data: f_NL = 55 ± 125 from ACT DR6 [src, arXiv:2602.03917]. The method belongs to `cosmo-inflation-primordial`.

## 8. Gas-mass fraction

For the hottest, dynamically relaxed clusters the ratio of X-ray gas mass to total mass in a shell around r2500 is expected to be nearly constant in mass and redshift. The measured f_gas depends on the assumed distances roughly as d^1.5, so requiring a constant true f_gas constrains the expansion history, and its normalisation gives Ω_b/Ω_m once the gas depletion factor is taken from simulations (arXiv:0706.0033, arXiv:1402.6212). Sample selection is by morphology (the SPA criteria: 57 of 361 clusters pass [src, arXiv:1502.06020]); the hydrostatic mass at r2500 agrees with lensing, ratio 0.96 ± 9% (stat) ± 9% (sys) [src, arXiv:1509.02162]. This is a distance probe, independent of the mass function and of the count selection function.

## 9. Splashback radius and outer profiles

- Definition. The splashback radius is the apocentre of the first orbit of accreted matter; it appears as the radius where the logarithmic slope of the density profile is steepest. Diemer & Kravtsov 2014 (arXiv:1401.1216) show that profiles depart from NFW and Einasto forms beyond 0.5 R200m, that the steepest slope lies near R200m and reaches −4 or steeper for high peak height or accretion rate, and give a fitting formula accurate to better than 10% for r < 9 R_vir, 0 < z < 6 and M_vir > 1.7e10 M_sun/h [src].
- First detection and the puzzle. More et al. 2016 (arXiv:1601.06063) detect the feature in the projected density of SDSS photometric galaxies around redMaPPer clusters and report a 6.6σ halo assembly-bias signal [src]; the measured splashback radii are smaller, and the assembly-bias signal stronger, than N-body expectations.
- Selection test. With SZ-selected clusters (SPT-SZ and ACTPol) correlated with DES Y3 galaxies, the splashback radius is consistent with simulations, while redMaPPer clusters give a radius about 2σ smaller [src] (Shin et al. 2019, arXiv:1811.06081). The discrepancy points to optical selection, the same mechanism as in the DES Y1 lensing failure. Blue galaxies show no splashback feature, consistent with first infall.
- Current state. For 9049 AMICO KiDS-1000 clusters at 0.1 < z < 0.8, stacked reduced shear and the cluster–galaxy correlation function over 0.4–5 Mpc/h give consistent splashback radii that agree with ΛCDM predictions, with 14% and 10% precision per stack [src] (Lesci et al. 2026, arXiv:2602.07114).
- Profiles as a cosmological probe. The mean lensing profile of the infall region of clusters, compared with a simulation suite, gives Ω_m = 0.34 ± 0.06 and σ8 = 0.77 ± 0.04 with a preliminary UNIONS catalogue [src, arXiv:2501.09147].

## 10. Blinding practice

| Analysis | Blinding as stated | Citation |
|---|---|---|
| SDSS redMaPPer | blind analysis | arXiv:1810.09456 |
| DES Y1 clusters | blind, with changes after unblinding | arXiv:2002.11124 |
| SDSS redMaPPer + HSC Y3 | blind | arXiv:2309.13025 |
| HSC shear-selected | blind | arXiv:2406.11970 |
| KiDS-1000 AMICO | blinded through the sample completeness (selection function) | arXiv:2507.14285, arXiv:2507.14338 |

The DES Y1 case shows the limit of blinding: an analysis can be blind, pass its internal tests and still be wrong, because blinding protects against tuning and not against a missing term in the model. Blinding strategies of the eROSITA, SPT and Planck analyses were not read this session.

## 11. Public codes, catalogues and pipelines

| Item | Purpose | Reference | Flag |
|---|---|---|---|
| redMaPPer | red-sequence cluster finder (richness λ) | used in arXiv:1810.09456, arXiv:2002.11124; reference paper not fetched | [sec] |
| eROMaPPer | optical identification of eROSITA candidates on Legacy Survey imaging | arXiv:2402.08453 | [src] |
| AMICO, PZWav | cluster finders used for KiDS and for Euclid Q1 | arXiv:2507.14338, arXiv:2503.19196 | [src] |
| MCMF | optical confirmation of SZ candidates | used in arXiv:2401.02075 | [sec] |
| SZiFi | tSZ cluster finder with CIB deprojection, public on GitHub (inigozubeldia/szifi) | arXiv:2408.06189 | [src] |
| ACT DR6 detection software, noise maps and masks | public with the catalogue | arXiv:2507.21459 | [src] |
| tSZ cluster forecast products (binned counts, Fisher matrices) | public on GitHub (sriniraghunathan/tSZ_cluster_forecasts) | arXiv:2107.10250 | [src] |
| CosmoPostProcess | simulation-calibrated correction of lensing selection bias for richness-selected clusters | arXiv:2605.02723 | [src] |
| PINOCCHIO | fast halo catalogues for covariance and likelihood tests | used in arXiv:2210.11093 | [sec] |

## 12. Where the community is split

- Reference mass scale: hydrostatic XMM (Planck), hydrostatic Chandra, or lensing only. The same counts give the same cosmology under any of them, but (1 − b) values are not comparable across references (arXiv:2402.04006).
- Stacked lensing in richness bins against per-cluster lensing in a population model.
- Poisson against Gaussian count likelihoods (section 5).
- Whether optical richness can be calibrated by lensing alone at low richness, or needs a multi-wavelength anchor (arXiv:2010.13800, arXiv:2101.04984).
- Constant against mass- and redshift-dependent mass bias (arXiv:2509.02068, arXiv:2512.18935).

## Not verified

- Which mass function (Tinker 2008, Bocquet 2016, an emulator) each of eRASS1, SPT 2024, DES Y3 and KiDS AMICO adopts: not read in the paper bodies.
- Reference papers of redMaPPer, MCMF, AMICO, PINOCCHIO and of general-purpose halo-model libraries: not fetched, so no identifier is given.
- The foundational papers of the analytic mass function (Press and Schechter, Sheth and Tormen, Jenkins and collaborators) and of the SZ effect were not fetched and are not cited.
- The universal pressure profile and the paper that calibrates the Planck Y–M relation were not fetched.
- Blinding schemes of the eRASS1, SPT and Planck cluster analyses.
