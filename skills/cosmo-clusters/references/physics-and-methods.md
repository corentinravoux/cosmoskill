# Galaxy-cluster cosmology — physics and methods

Scope: what cluster abundance, clustering, gas fractions and profiles measure, the models and likelihoods in current use, and the public codes.
Snapshot: 2026-10-14

Reviews to start from: Allen, Evrard & Mantz 2011 (arXiv:1103.4829) for the method as a whole and its pre-Planck results; Pratt et al. 2019 (arXiv:1902.10837) for the mass scale, the mass-estimation methods and their biases; Kravtsov & Borgani 2012 (arXiv:1205.5556) for cluster formation, halo structure, the mass function and clustering as the theoretical foundation, and for where galaxy-formation physics leaves predictions uncertain [src]; Carlstrom, Holder & Reese 2002 (arXiv:astro-ph/0208192) for the SZ effect, whose surface brightness is independent of redshift, making SZ surveys suited to z > 1 [src]. No review of cluster cosmology dated after June 2025 was found in a date-sorted title search (2026-10-09).

## 1. What is measured and why it constrains cosmology
<!-- key: what-is-measured-and-why-it-constrains-cosmology -->

The number density of haloes above about 1e14 M_sun falls exponentially with mass, so the abundance of clusters as a function of mass and redshift responds steeply to the amplitude of matter fluctuations and to the matter density. Counts in a survey are

    dN / (dz dΩ dO) = (dV / dz dΩ) ∫ dM  n(M, z)  P(O | M, z)  S(O, z, sky position)

where n(M, z) is the halo mass function, P(O | M, z) the stochastic observable–mass relation and S the selection function. Haiman, Mohr & Holder 2001 (arXiv:astro-ph/0002336) set out the method for future SZ and X-ray surveys: the total number and redshift distribution of clusters constrain Ω_m and w with only mild w–Ω_m and w–h degeneracies, provided the local abundance is known to a few per cent [src]. The three ingredients are the three places where an analysis can fail: the mass function is theory, the observable–mass relation is the mass calibration, and the selection is survey-specific.

Four cluster probes are in use.

| Probe | Sensitive to | Limiting ingredient | Where the numbers are |
|---|---|---|---|
| Abundance N(O, z) | σ8 and Ω_m along σ8 Ω_m^α, growth history, Σm_ν, w, modified gravity | absolute mass scale and selection | `results.md` |
| Clustering of clusters | halo bias, hence mass (self-calibration); Ω_m through the shape | sample size, photo-z, RSD modelling | `results.md`, section 7 below |
| Gas-mass fraction of relaxed clusters | distances (f_gas ∝ d^1.5 in the reference cosmology) and Ω_b/Ω_m | gas depletion factor, hydrostatic mass at r2500 | `results.md` |
| Outer profile, splashback, infall region | accretion rate, halo definition, gravity; a test of the selection | optical selection effects, statistical power | section 9 below |

The count degeneracy direction is flatter than the cosmic-shear one. Analyses quote the best-constrained combination with their own exponent: 0.3 with pivot 0.27 (Planck 2013, arXiv:1303.5080), 0.17 (Weighing the Giants, arXiv:1407.4516), 0.2 then 0.25 (SPT, arXiv:1812.01679, arXiv:2401.02075), 0.25 with pivot 0.33 (arXiv:1904.07887) [src]. The standard S8 = σ8 (Ω_m/0.3)^0.5 is usually quoted in addition and has a larger error: 0.029 against 0.016 for the optimal SPT combination [src, arXiv:2401.02075].

## 2. Mass definitions and conventions
<!-- key: mass-definitions-and-conventions -->

- Spherical-overdensity masses: M_Δ = (4π/3) Δ ρ_ref r_Δ³, with ρ_ref the critical density at the cluster redshift (suffix c) or the mean matter density (suffix m). X-ray and SZ work uses M500c; optical and lensing work M200m or M200c; relaxed-cluster f_gas work r2500 (arXiv:1402.6212).
- Tinker et al. 2008 argue that spherical-overdensity masses are more directly linked to cluster observables than friends-of-friends masses (arXiv:0803.2706). Conversion between definitions requires a concentration model; Hu & Kravtsov 2003 give a fitting formula for it (arXiv:astro-ph/0203169).
- Inner profiles are most self-similar when radii are scaled by R200c, outer profiles when scaled by R200m (Diemer & Kravtsov 2014, arXiv:1401.1216). This is the physical reason the two conventions coexist.
- Units: M_sun, M_sun/h, or M_sun/h70 in SPT catalogue papers (arXiv:2311.07512). A factor of h between two quoted mass limits is about 40% for h ≈ 0.7 [der: 1/0.7 = 1.43]. Check before comparing mass thresholds.
- Mass bias: (1 − b) = M_proxy / M_true, where M_proxy comes from a scaling relation calibrated on X-ray hydrostatic masses. A smaller (1 − b) means heavier clusters and a higher σ8 from the same counts. The reference relation matters: with the same lensing data (1 − b) is 0.89 ± 0.04 for a Chandra-calibrated relation and 0.76 ± 0.04 for the XMM one [src, arXiv:2402.04006].
- Hydrostatic bias in simulation papers is often written with the opposite sign, as a negative fractional offset of the hydrostatic mass (arXiv:2409.07849): b_HSE ≈ −0.2 there corresponds to (1 − b) ≈ 0.8 here.

## 3. Halo mass function and halo bias
<!-- key: halo-mass-function-and-halo-bias -->

The mass function is written dn/dM = f(σ) (ρ_m / M) d ln σ⁻¹/dM, with σ(M, z) the rms linear fluctuation in a top-hat enclosing M. "Universality" is the statement that f depends on cosmology and redshift only through σ. Jenkins et al. 2001 (arXiv:astro-ph/0005260) found, for a suitable halo definition, a simulated mass function almost independent of epoch, cosmology and initial spectrum in these variables, as Press–Schechter theory predicts, with systematic uncertainty below 10–30% depending on the halo definition [src]. Sheth & Tormen 1999 (arXiv:astro-ph/9901122) showed with the peak-background split that the unconditional mass function suffices to predict large-scale halo bias [src]. The halo density profile used in nearly every lensing model is that of Navarro, Frenk & White 1997 (arXiv:astro-ph/9611107), one shape for all masses, cosmologies and spectra [src].

| Reference | What it provides | Stated accuracy and limits | Flag |
|---|---|---|---|
| Tinker et al. 2008, arXiv:0803.2706 | f(σ) for spherical-overdensity masses at many Δ, from collisionless flat ΛCDM simulations, z ≲ 2 | ≲ 5% at z = 0 for 1e11 < M < 1e15 M_sun/h; improves earlier fits by 10–20%; **not universal**: the amplitude of the "universal" function falls by 20–50% from z = 0 to 2.5 depending on the mass definition | [src] |
| Tinker et al. 2010, arXiv:1001.3162 | large-scale bias b(ν, Δ), normalised so that the bias of all matter is unity with the 2008 mass function | about 6% scatter; FoF (linking length 0.2) haloes have bias about 10% lower than Δ = 200; the bias function evolves very weakly with redshift; the peak-background split leaves about 20% residuals | [src] |
| Bocquet et al. 2016, arXiv:1502.07357 | hydrodynamical and dark-matter-only fits from Magneticum boxes up to (3818 Mpc)³ | baryons lower masses and hence abundance at fixed mass; the effect vanishes at z ~ 2 and for M200m ≳ 1e14 M_sun; using this DM-only fit instead of Tinker 2008 shifts a Planck-like analysis by Δσ8 ≈ 0.02 | [src] |
| Euclid Collaboration (Castro et al.) 2023, arXiv:2208.02174 | fit calibrated with a Bayesian treatment of numerical systematics, including scale-free simulations to trace non-universality | sub-percent over 9 ΛCDM variants including massive neutrinos; the halo-finder choice is the one effect that "could lead to biased cosmological inference" | [src] |

Practice in current analyses, as far as the abstracts read state it: the KiDS-1000 AMICO analysis marginalises over mass-function uncertainty (arXiv:2507.14285); the SPT analysis adds 2% in quadrature for baryonic effects on the lensing-mass model (arXiv:2310.12213); the ACT f_NL analysis uses a Log–Edgeworth non-Gaussian mass function (arXiv:2602.03917).

Read in the bodies, the headline analyses still use Tinker 2008: eRASS1, which finds σ8 lower by 0.02 with Tinker 2010 or Despali 2016 [src: Sect. 7.2, arXiv:2402.08458]; Planck 2015, where Watson et al. 2013 moves the result about 1σ along the degeneracy [src: Appendix A.2, arXiv:1502.01597]; DES Y1, with deviations calibrated on simulations [src: Sect. IV.1, arXiv:2002.11124]; KiDS AMICO, multiplied by a calibrated bias factor with a Gaussian prior [src: Eq. 19, arXiv:2507.14285]. SPT links lensing masses to gravity-only halo masses so that a gravity-only mass function (Tinker 2008 cited) applies, and found no shift when marginalising 3.5% in amplitude and 2% in slope [src: Sect. V.2.1, arXiv:2310.12213; Sect. IV.2.3, arXiv:2401.02075].

Mass-function emulators and new prescriptions published between June 2025 and October 2026 were returned by a date-sorted search (titles: "Evolution mapping III: A new recipe for the halo mass function"; "Aletheia: Emulating the halo mass function with evolution mapping"; "CSST Cosmological Emulator II: Generalized Accurate Halo Mass Function Emulation"; "Emulation of the Halo Mass Function with Neural Networks"; "Euclid: Impact of halo mass-conversion model assumptions on galaxy cluster number-count analyses"). They are leads, not read and not cited.

## 4. Observables and observable–mass relations
<!-- key: observables-and-observable-mass-relations -->

| Selection | Detection observable | Mass proxy and calibration | Strength | Characteristic failure |
|---|---|---|---|---|
| X-ray (ROSAT, XMM, eROSITA) | extended soft X-ray emission | L_X, T_X, M_gas, Y_X = M_gas T_X; now weak lensing (arXiv:2402.08458) | large samples, low-scatter follow-up proxies | selection depends on core state and morphology; point sources; selection function built from simulated skies (arXiv:2402.08457) |
| Thermal SZ (Planck, SPT, ACT) | Compton-y decrement through a matched filter; SPT significance ξ, ACT and Planck S/N | Y_SZ or ξ; hydrostatic X-ray (Planck), weak lensing (SPT, ACT) | mass limit that varies slowly with redshift | radio and dust infill, relativistic corrections |
| Optical richness (redMaPPer λ, AMICO λ*) | red-sequence or matched-filter overdensity | stacked weak lensing | lowest mass threshold, largest samples | projection effects correlated with lensing and clustering; miscentring |
| Weak-lensing shear peaks (HSC) | aperture-mass peak height ν | the selection observable is itself the lensing signal | selection "solely depends on gravity" (arXiv:2406.11970) | small samples (129 clusters [src]) |
| Infrared (MaDCoWS) | galaxy overdensity at z ~ 1 | CMB lensing (arXiv:2009.07772) | reaches z > 1 | selection not modelled for cosmology |

The thermal SZ signal measures the line-of-sight integral of electron pressure, y = (σ_T / m_e c²) ∫ P_e dl, and its integral over the cluster measures the total thermal energy of the gas. Self-similar collapse predicts a power law in mass and in E(z). In the Planck parametrisation the self-similar mass slope is quoted as 1.8, and a joint Planck + SPT fit finds α_SZ = 1.49 +0.07/−0.10, about 4σ away [src, arXiv:2112.03606].

The SZ template and Y–M relation used by Planck come from Arnaud et al. 2010 (arXiv:0910.1234): the universal pressure profile from 33 REXCESS clusters, with low dispersion beyond 0.2 R500, a residual mass dependence of slope about 0.12, and the Y_SZ–M500 relation derived from it [src]. Planck 2015 detects with this profile as matched-filter template [src: Sect. 2, arXiv:1502.01597].

X-ray hydrostatic mass: M(<r) = −(k T r / G μ m_p) (d ln ρ_gas/d ln r + d ln T/d ln r). It is biased low by non-thermal pressure and by temperature inhomogeneity, and its absolute scale follows the X-ray temperature calibration (see `systematics.md`). The simulation reference is Nagai, Vikhlinin & Kravtsov 2007 (arXiv:astro-ph/0609247): mock Chandra analyses recover gas mass to < 6%, while the hydrostatic mass is biased low by about 5–20% through the virial region [src].

X-ray mass proxies and the L_X–M relation. Y_X = M_gas T_X was introduced as a low-scatter proxy on simulated clusters (Kravtsov, Vikhlinin & Nagai 2006, arXiv:astro-ph/0603205) [src]. The Chandra Cluster Cosmology Project calibrated M–T_X, M–M_gas and M–Y_X on relaxed low-z clusters and gave the first evolving L_X–M relation from a complete sample with Malmquist-bias corrections (Vikhlinin et al. 2009, arXiv:0805.2207) [src]. REXCESS found L_X–T and L_X–Y_X slopes significantly steeper than self-similar (Pratt et al. 2009, arXiv:0809.3784) [src].

Optical richness. redMaPPer (Rykoff et al. 2014, arXiv:1303.3562) self-trains the red-sequence model, assigns P(z) and centring probabilities, and gave about 25000 SDSS DR8 clusters at 0.08 < z < 0.55 with σ_z ≈ 0.006 at z ~ 0.1 rising to 0.02 at z ~ 0.5; its paper put the incidence of projection effects at ≤ 5% [src], an estimate later work raised (see `systematics.md`, section 8).

Scaling relations are modelled as power laws in mass and in E(z) or (1 + z), with lognormal intrinsic scatter and, in multi-observable analyses, correlated scatter between observables. The multivariate form with intrinsic covariance between X-ray and SZ signals was studied in the Millennium Gas Simulations by Stanek et al. 2010 (arXiv:0910.1599) [src]. For SPT clusters with DES redMaPPer richness, ⟨ln λ | M500⟩ ∝ B_λ ln M500 + C_λ ln E(z) gave B_λ = 1.14 +0.21/−0.18 from 25 clusters (Saro et al. 2015, arXiv:1506.07814) [src]. DES Y3 × SPT cross-matching shows that a simple lognormal scatter is inadequate for richness (arXiv:2502.12914).

## 5. Count likelihoods and covariance
<!-- key: count-likelihoods-and-covariance -->

- Forward population model. The current standard is a Bayesian hierarchical model in which the survey observable (ξ, X-ray flux or count rate, richness) and the follow-up observables (shear profile, Y_X, velocity dispersion) are drawn from a joint scaling relation with correlated scatter, and the selection is applied to the detection observable. The SPT framework is described in Bocquet et al. 2024 (arXiv:2310.12213) and applied in arXiv:2401.02075; Mantz et al. 2010 (arXiv:0909.3098) is the statistical-methods paper for the X-ray samples.
- The count likelihood as the papers write it.
  - Binned Poisson (Planck 2015): ln L = Σ_ij [N_ij ln N̄_ij − N̄_ij − ln N_ij!] over 10 bins of Δz = 0.1 and 5 bins of Δlog q = 0.25, with N̄_ij = (dN/dz dq) Δz Δq; bins treated as uncorrelated [src: Sect. 5.1, Eqs. 15–16, arXiv:1502.01597]. The mean signal follows Ȳ500 ∝ [(1 − b) M500]^α E^β(z) with lognormal scatter σ_lnY [src: Eqs. 7, 9].
  - Unbinned Poisson (SPT): from P(k | μ) = μ^k e^−μ / k! in bins holding at most one cluster, ln L = Σ_i ln(dμ/dx)|_x_i − ∫ (dμ/dx) dx, the sum running over clusters [src: Sect. VII.2.1, Eqs. 48–50, arXiv:2310.12213]. The cosmology fit adds a "mass calibration likelihood" P(λ_i, g_t,i | λ_i > λ_min(z), ξ_i, z_i, p) per cluster, conditional on the selection observables, so lensing data do not enter the counts term twice [src: Sect. III.2, Eq. 11, arXiv:2401.02075].
  - eRASS1 writes the same unbinned form with a selection P(I | Ĉ_R, ẑ, Ĥ) times a richness cut Θ(λ̂ > 3), then splits it into a counts term, a total-number term, and conditional richness and shear terms [src: Sect. 4.1, Eqs. 1, 2, 6, arXiv:2402.08458]; the differential counts integrate the redshift error, selection function, count-rate error, mass function, comoving volume and lognormal count-rate–mass relation over true mass, count rate and redshift [src: Eq. 8].
  - Poisson × Gaussian super-sample term (KiDS AMICO): the count likelihood is a convolution of Poisson distributions with the Gaussian distribution of background modes δ_b per redshift bin, following Lima & Hu 2004 and Lacasa & Grain 2019 [src: Sect. 5.4, arXiv:2507.14285]. The expected counts in bins of observed richness and redshift divide by purity and integrate the mass function, its bias factor, completeness, the lognormal richness–mass relation and the observed-given-true richness and redshift distributions [src: Eq. 18].
- Stacked versus individual lensing. SPT uses per-cluster shear profiles inside the population model (arXiv:2310.12213), and the Planck × DES analysis also works with shear profiles (arXiv:2509.02068). Richness-selected analyses (SDSS, DES Y1, KiDS AMICO) stack the lensing signal in bins of richness and redshift (arXiv:1805.00039, arXiv:2507.14285). Stacking is where the optical selection bias enters: the mean lensing profile of a richness-selected stack is not that of a mass-selected sample of the same mean mass.
- Poisson versus Gaussian. Sample variance (the modulation of counts by long-wavelength density modes, proportional to halo bias) is comparable to or larger than shot noise for surveys that reach low masses, and is usually more important than shot noise for constraints on w from z < 1 clusters (Hu & Kravtsov 2003, arXiv:astro-ph/0203169). On 1000 PINOCCHIO catalogues, a Poisson likelihood always underestimates parameter errors for Rubin- or Euclid-like surveys; a Gaussian likelihood with sample covariance is robust over a wide range of binnings, and the Gauss–Poisson compound likelihood brings no gain at higher cost [src] (Payerne et al. 2023, arXiv:2210.11093).
- Counts and clustering of clusters are found to be uncorrelated in Euclid-like mocks, so their likelihoods multiply (arXiv:2510.13509).
- Joint analyses with 3×2pt need the cross-covariance and a common nuisance model: SPT clusters + DES Y3 3×2pt uses 52 astrophysical nuisance parameters [src, arXiv:2412.07765]; the DES Y6 strategy is validated on Cardinal mocks (arXiv:2503.13631).
- Simulation-based inference is entering the field: the XXL analysis with HSC lensing uses DELFI with 12 parameters and reports an extra 3% systematic from neural-network stochasticity [src, arXiv:2602.11989]; the reanalysis of DES Y1 uses a simulation-based forward model of the optical selection (arXiv:2510.25706).

## 6. Mass calibration
<!-- key: mass-calibration -->

| Method | Measures | Precision reached | Main limitation | Key references |
|---|---|---|---|---|
| Weak lensing, per cluster or stacked | projected mass through tangential reduced shear, ΔΣ(R) = Σ_crit γ_t | 5.0% on the richness–mass normalisation in DES Y1 [src, arXiv:1805.00039]; 7% on the ACT normalisation with DES Y3 [src, arXiv:2512.18935]; 8% mass scale in Weighing the Giants [src, arXiv:1407.4516]; 8% mean mass precision in KiDS AMICO [src, arXiv:2507.14285] | model bias of profile fits, source redshifts, miscentring, contamination by members, selection bias of stacks | arXiv:1011.1681, arXiv:1502.01883, arXiv:2310.12213, arXiv:2409.02783 |
| CMB lensing of clusters | mass from the distortion of the CMB gradient behind the cluster; no source redshifts needed | 4.2σ for 677 clusters at mean z = 1.08 [src, arXiv:2009.07772]; 3.1σ for SPT-SZ [src, arXiv:2111.07491]; (1 − b) = 0.71 ± 0.10 for 433 Planck clusters [src, arXiv:1904.07887] | signal-to-noise per cluster; contamination of the estimator by the cluster's own SZ signal | arXiv:2404.02153 |
| X-ray hydrostatic | thermal pressure support | — | hydrostatic bias, temperature calibration | arXiv:1805.00034, arXiv:1509.02162 |
| Dynamical (velocity dispersion) | galaxy kinematics | used by ACT in 2013 with a 15% dynamical-mass bias marginalised [src, arXiv:1301.0816] | velocity bias, interlopers | arXiv:1902.10837 |
| Clustering (self-calibration) | bias, hence mean mass | (1 − b) = 0.62 +0.14/−0.11 from Planck cluster clustering [src, arXiv:2302.14074] | sample size | arXiv:2510.14464 |

Weak-lensing mass is not an unbiased estimator of spherical-overdensity mass. Fitting a spherical NFW profile to the reduced shear of about 1e4 simulated haloes gives a bias of 5–10% and an intrinsic scatter of about 20% for massive clusters and up to about 30% for groups, from triaxiality and from correlated and uncorrelated large-scale structure [src] (Becker & Kravtsov 2011, arXiv:1011.1681). In Euclid-like conditions on N-body haloes the mean bias is −14.6 ± 1.7 % for M200c > 5e13 M_sun at z < 1 [src, arXiv:2409.02783]. Modern analyses therefore calibrate a relation between weak-lensing mass and halo mass on simulations and carry its bias and scatter as nuisance parameters (arXiv:2310.12213, arXiv:2402.08455). The method paper is Grandis et al. 2021 (arXiv:2103.16212): shear libraries from hydrodynamical projected-mass maps, with shear bias and noise, photo-z, miscentring, member contamination, morphology and line-of-sight structure, are fitted with a one-parameter model; matching to gravity-only twins measures the hydrodynamical effect; about 1000 realisations of the systematics give the prior on the M_WL–M relation [src]. eRASS1, SPT and HSC all use it (`systematics.md`, section 13).

Stacked lensing of optical clusters began with SDSS: Johnston et al. 2007 (arXiv:0709.1159) inverted the shear around about 130000 groups and clusters into mean 3D profiles in bins of richness and luminosity, modelled the profile as central galaxy + halo + neighbouring haloes with miscentring, and measured the mass at fixed richness to 13% [src].

The stacked-lensing model of McClintock et al. 2019 (arXiv:1805.00039) is the reference for richness-selected samples: ⟨M200m | λ, z⟩ = M0 (λ/40)^F ((1 + z)/1.35)^G, with M0 = [3.081 ± 0.075 (stat) ± 0.133 (sys)] × 1e14 M_sun, F = 1.356 ± 0.051 ± 0.008, G = −0.30 ± 0.30 ± 0.06 [src], from 4 × 3 bins at λ ≥ 20 and 0.2 ≤ z ≤ 0.65 and a semi-analytic covariance. It is also the calibration behind the DES Y1 result that failed (see `results.md`), which is why its systematics list matters more than its precision.

## 7. Clustering of clusters
<!-- key: clustering-of-clusters -->

Clusters are highly biased tracers: measured biases run from 2.95 ± 0.21 to 4.34 ± 0.62 for eRASS1 luminosity-limited samples [src, arXiv:2402.08460] and 5.30 ± 0.24 for SPT-3G clusters at 0.25 < z < 1.1 [src, arXiv:2610.08947]. On large scales P_cc(k) = b² P_m(k); since b(M) is predicted (section 3), the clustering amplitude measures the mean mass without any lensing or hydrostatic assumption. This is self-calibration: Majumdar & Mohr 2004 (arXiv:astro-ph/0305341) showed that adding the cluster power spectrum and 100 direct masses to the redshift distribution improves w by roughly a factor of 4 for X-ray and SZ surveys [src, **forecast**]; Lima & Hu 2004 (arXiv:astro-ph/0401559) used the excess variance of counts in cells, reaching σ(w) = 0.06 for a deep 4000 deg² survey with an unknown power-law evolution of the mass–observable relation [src, **forecast**].

Statistics in use: projected correlation function with a halo-occupation model (eRASS1, arXiv:2402.08460); redshift-space two-point function over 10–150 Mpc/h (Planck clusters, arXiv:2302.14074); angular correlation function and angular power spectrum of photometric clusters (AMICO KiDS-DR3, arXiv:2310.12224); cluster auto-correlation with an analytic covariance (SPT-3G, arXiv:2610.08947); cluster–galaxy and cluster–shear cross-correlations inside a multiprobe data vector (DES Y1 and Y3, arXiv:2010.01138, arXiv:2503.13632).

What clustering adds, according to forecasts that differ in size: in Euclid-like mocks adding clustering raises the figure of merit by more than 300% [src, arXiv:2510.13509, **forecast**]; for future SZ samples of 33000 to 140000 clusters with current mass–observable priors, σ(w) improves by factors of 1.023 ± 0.007 to 1.079 ± 0.011 and σ(Ω_m) by 1.068 to 1.145, and the gain on w "largely vanishes" when the mass–observable priors are tightened by a factor of two [src, arXiv:2510.14464, **forecast**]. The two are not in contradiction: clustering helps in proportion to how poorly the mass–observable relation is known otherwise.

The non-Gaussian mass function is constrained with the same count data: f_NL = 55 ± 125 from ACT DR6 [src, arXiv:2602.03917]. The method belongs to `cosmo-inflation-primordial`.

## 8. Gas-mass fraction
<!-- key: gas-mass-fraction -->

For the hottest, dynamically relaxed clusters the ratio of X-ray gas mass to total mass in a shell around r2500 is expected to be nearly constant in mass and redshift. The measured f_gas depends on the assumed distances roughly as d^1.5, so requiring a constant true f_gas constrains the expansion history (the method proposed by Sasaki 1996, arXiv:astro-ph/9611033, from the baryon fraction against redshift [src]), and its normalisation gives Ω_b/Ω_m once the gas depletion factor is taken from simulations (arXiv:0706.0033, arXiv:1402.6212). Sample selection is by morphology (the SPA criteria: 57 of 361 clusters pass [src, arXiv:1502.06020]); the hydrostatic mass at r2500 agrees with lensing, ratio 0.96 ± 9% (stat) ± 9% (sys) [src, arXiv:1509.02162]. This is a distance probe, independent of the mass function and of the count selection function.

## 9. Splashback radius and outer profiles
<!-- key: splashback-radius-and-outer-profiles -->

- Definition. The splashback radius is the apocentre of the first orbit of accreted matter; it appears as the radius where the logarithmic slope of the density profile is steepest. Diemer & Kravtsov 2014 (arXiv:1401.1216) show that profiles depart from NFW and Einasto forms beyond 0.5 R200m, that the steepest slope lies near R200m and reaches −4 or steeper for high peak height or accretion rate, and give a fitting formula accurate to better than 10% for r < 9 R_vir, 0 < z < 6 and M_vir > 1.7e10 M_sun/h [src]. Adhikari, Dalal & Chamberlain 2014 (arXiv:1409.4482) predict the splashback location from spherical collapse with no free parameter, set by accretion rate and redshift [src]. More, Diemer & Kravtsov 2015 (arXiv:1504.05591) propose R_sp as the physical halo boundary: about 0.8–1 R200m for rapidly accreting haloes and about 1.5 R200m for slowly accreting ones [src].
- First detection and the puzzle. More et al. 2016 (arXiv:1601.06063) detect the feature in the projected density of SDSS photometric galaxies around redMaPPer clusters and report a 6.6σ halo assembly-bias signal [src]; the measured splashback radii are smaller, and the assembly-bias signal stronger, than N-body expectations.
- Selection test. With SZ-selected clusters (SPT-SZ and ACTPol) correlated with DES Y3 galaxies, the splashback radius is consistent with simulations, while redMaPPer clusters give a radius about 2σ smaller [src] (Shin et al. 2019, arXiv:1811.06081). The discrepancy points to optical selection, the same mechanism as in the DES Y1 lensing failure. Blue galaxies show no splashback feature, consistent with first infall.
- Current state. For 9049 AMICO KiDS-1000 clusters at 0.1 < z < 0.8, stacked reduced shear and the cluster–galaxy correlation function over 0.4–5 Mpc/h give consistent splashback radii that agree with ΛCDM predictions, with 14% and 10% precision per stack [src] (Lesci et al. 2026, arXiv:2602.07114).
- Profiles as a cosmological probe. The mean lensing profile of the infall region of clusters, compared with a simulation suite, gives Ω_m = 0.34 ± 0.06 and σ8 = 0.77 ± 0.04 with a preliminary UNIONS catalogue [src, arXiv:2501.09147].

## 10. Blinding practice
<!-- key: blinding-practice -->

| Analysis | Blinding as stated | Citation |
|---|---|---|
| SDSS redMaPPer | blind analysis | arXiv:1810.09456 |
| DES Y1 clusters | blind, with changes after unblinding | arXiv:2002.11124 |
| SDSS redMaPPer + HSC Y3 | blind | arXiv:2309.13025 |
| HSC shear-selected | blind | arXiv:2406.11970 |
| KiDS-1000 AMICO | blinded through the sample completeness (selection function) | arXiv:2507.14285, arXiv:2507.14338 |
| eRASS1 | four of six selection functions, shuffled by an external blinder, analysed in parallel [src: Sect. 5.2] | arXiv:2402.08458 |
| SPT 2024 | constant random offsets on parameters; HST-39 excluded from the blind phase [src: Sect. IV.1] | arXiv:2401.02075 |
| DES Y3 clusters | parameter-level shifts only, the 3×2pt data being already unblinded [src: Sect. IV.1] | arXiv:2503.13632 |

The DES Y1 case shows the limit of blinding: an analysis can be blind, pass its internal tests and still be wrong, because blinding protects against tuning and not against a missing term in the model. The selection-effect correction that changed the DES Y1 mass scale by 20–30% was adopted after unblinding [src: Sect. III.3, arXiv:2002.11124]. The blinding of the Planck cluster analyses was not read this session.

## 11. Public codes, catalogues and pipelines
<!-- key: public-codes-catalogues-and-pipelines -->

| Item | Purpose | Reference | Flag |
|---|---|---|---|
| redMaPPer | red-sequence cluster finder (richness λ) | Rykoff et al. 2014, arXiv:1303.3562; used in arXiv:1810.09456, arXiv:2002.11124 | [src] |
| eROMaPPer | optical identification of eROSITA candidates on Legacy Survey imaging | arXiv:2402.08453 | [src] |
| AMICO, PZWav | cluster finders used for KiDS and for Euclid Q1 | arXiv:2507.14338, arXiv:2503.19196 | [src] |
| MCMF | optical confirmation of SZ candidates | used in arXiv:2401.02075 | [sec] |
| SZiFi | tSZ cluster finder with CIB deprojection, public on GitHub (inigozubeldia/szifi) | arXiv:2408.06189 | [src] |
| ACT DR6 detection software, noise maps and masks | public with the catalogue | arXiv:2507.21459 | [src] |
| tSZ cluster forecast products (binned counts, Fisher matrices) | public on GitHub (sriniraghunathan/tSZ_cluster_forecasts) | arXiv:2107.10250 | [src] |
| CosmoPostProcess | simulation-calibrated correction of lensing selection bias for richness-selected clusters | arXiv:2605.02723 | [src] |
| PINOCCHIO | fast halo catalogues for covariance and likelihood tests | used in arXiv:2210.11093 | [sec] |

## 12. Where the community is split
<!-- key: where-the-community-is-split -->

- Reference mass scale: hydrostatic XMM (Planck), hydrostatic Chandra, or lensing only. The same counts give the same cosmology under any of them, but (1 − b) values are not comparable across references (arXiv:2402.04006).
- Stacked lensing in richness bins against per-cluster lensing in a population model.
- Poisson against Gaussian count likelihoods (section 5).
- Whether optical richness can be calibrated by lensing alone at low richness, or needs a multi-wavelength anchor (arXiv:2010.13800, arXiv:2101.04984).
- Constant against mass- and redshift-dependent mass bias (arXiv:2509.02068, arXiv:2512.18935).

## 13. What the main analyses did
<!-- key: what-the-main-analyses-did -->

Read in the paper bodies; the systematics budget of each is in `systematics.md`, section 13.

| Analysis | Sample and threshold | Mass calibration | Mass function | Priors of note | Blinding |
|---|---|---|---|---|---|
| eRASS1 (arXiv:2402.08458) | 11141 candidates at extent likelihood > 6; 12791 deg² overlap with LS DR10-South; 6562 optically identified of 7077 candidates there [src: Sect. 2.1]; integrals over 0 < z < 0.9, 5e12–5e15 M_sun [src: Sect. 4.1] | DES Y3, KiDS-1000, HSC shear profiles per cluster; M_WL–M relation from TNG300 snapshots at z = 0.24–0.95 [src: Sect. 6.2] | Tinker 2008 [src: Sect. 7.2] | H0 N(67.77, 0.6), flat or distance-ladder H0 checked [src: Sect. 4.6] | six selection functions sent to an external blinder, four analysed in parallel; no change after unblinding [src: Sect. 5.2] |
| SPT (arXiv:2401.02075) | 1005 clusters, ξ > 5, z > 0.25, ≳ 95% pure; DES richness over 73% of the area [src: Sect. II.1] | DES Y3 shear profiles + HST-39; M_WL–M_halo from Magneticum, TNG difference as baryonic error [src: Sect. V.2.1, arXiv:2310.12213] | gravity-only (Tinker 2008 cited) | h N(0.70, 0.05²); Planck Ω_b h², n_s [src: Table 1] | random parameter offsets; HST-39 kept out of the blind phase because already published; no change after unblinding [src: Sects. IV.1, IV.3] |
| Planck 2015 (arXiv:1502.01597) | 439 MMF3 clusters, S/N > 6 | prior on 1 − b: CCCP baseline, WtG and CMB lensing alternatives [src: Table 2] | Tinker 2008 [src: Appendix A.2] | Y–M slope α = 1.79 ± 0.08 [src: Table 1] | not stated in the sections read |
| Planck × DES (arXiv:2509.02068) | 439 PSZ2 clusters, 93 with DES Y3 shear [src: Sect. 2.3] | per-cluster DES shear profiles, Chandra-calibrated Y–M relation [src: Sects. 3.3, 4.2.3] | Tinker 2008 [src: Sect. 5.1] | (1 − b) flat; BBN Ω_b h²; BOSS DR12 BAO [src: Sect. 6.1] | not read |
| Planck + ACT (arXiv:2403.19542) | 439 Planck MMF3 + 59 ACT clusters [src: Sect. 2.2] | CCCP + MENeaCS or CMB-lensing 1 − b priors [src: Sect. 3.1] | not read | not read | not read |
| DES Y1 (arXiv:2002.11124) | redMaPPer counts in richness and redshift bins | stacked DES Y1 lensing (arXiv:1805.00039), corrected after unblinding for selection effects | Tinker [src: Sect. IV.1] | σ_intr prior the one exception to pre-unblinding finalisation [src: Appendix B] | random displacement of chains; staged unblinding with SDSS first [src: Appendix B] |
| DES Y3 (arXiv:2503.13632) | 16491 clusters, 0.2 < z < 0.65, λ ≥ 20 in 4 richness bins [src: Sect. III.1] | cluster lensing γ_c inside a 2pt data vector with w_cc, w_cg, w_gg | not read | IA, photo-z, shear priors of 3×2pt; prior-volume bias < 0.3σ [src: Sect. III.2] | parameter-level shifts only [src: Sect. IV.1] |
| KiDS-1000 AMICO (arXiv:2507.14285) | S/N > 3.5, 0.1 ≤ z ≤ 0.8, 839 deg² effective [src: Sect. 2.1] | stacked KiDS-1000 shear in richness and redshift bins, Gaussian likelihood with bootstrap + systematic covariance [src: Eqs. 40–44] | Tinker 2008 × bias factor [src: Eq. 19] | h N(0.7, 0.03); Ω_b, n_s Planck with 5σ widths [src: Sect. 5.4] | completeness blinded [src: Appendix B] |
| HSC shear-selected (arXiv:2406.11970) | aperture-mass peaks; selection by injection | simulation-calibrated M_WL–M–z relation as Gaussian priors [src: Sect. 4.5] | not read | constant-bias alternative A_WL N(0.99, 0.05²) [src: Sect. 4.5.2] | three blinded shape catalogues [src: Sect. 4.7] |

## Not verified
<!-- key: not-verified -->

- Which mass function DES Y3 and the HSC shear-selected analysis adopt: not found in the sections read (eRASS1, SPT, Planck 2015, DES Y1 and KiDS AMICO are now answered in section 3).
- Reference papers of MCMF, AMICO, PINOCCHIO and of general-purpose halo-model libraries: not fetched, so no identifier is given.
- Press & Schechter 1974 ("Formation of Galaxies and Clusters of Galaxies by Self-Similar Gravitational Condensation"), Kaiser 1986 ("Evolution and clustering of rich clusters") and White, Efstathiou & Frenk 1993 ("The amplitude of mass fluctuations in the Universe"), each confirmed on Crossref, and Sunyaev & Zeldovich 1972: no abstract could be read (publisher, ADS and Semantic Scholar refused or elided it), so they are not cited.
- Blinding scheme of the Planck cluster analyses.
