# Early-Universe exotica — systematics

Scope: the systematics that limit each class of constraint — pulsar-timing noise models, microlensing and PBH modelling, EDE prior-volume effects, FIRAS calibration and foregrounds, energy-deposition modelling — with mitigations and the referee checklist.
Snapshot: 2026-10-16

Flags as in `physics-and-methods.md`.

## 1. Pulsar-timing noise and the Hellings–Downs evidence
<!-- key: pulsar-timing-noise-and-the-hellings-downs -->

| Systematic | Mechanism and size | Mitigation or test | Citation | Flag |
|---|---|---|---|---|
| Intrinsic red noise and white noise per pulsar | NANOGrav characterises each pulsar with three white-noise and two red-noise parameters; the model "does not model all known physical effects explicitly" | single-pulsar noise analyses before the common search | NANOGrav 2023, arXiv:2306.16218 | [src] |
| Dispersion-measure variations | a piecewise-constant time-variable DM model enters the sensitivity; chromatic noise needs multi-band data | simultaneous low-frequency bands (InPTA uGMRT), combinations with InPTA | arXiv:2306.16218; arXiv:2306.16214 | [src] |
| Solar wind | contaminates pulsars at small solar elongation | elongation cuts of 10°, 20°, 30°; InPTA DR2 limit stable | arXiv:2608.02808 | [src] |
| Noise-model choice | the MPTA HD significance moves between 3–3.4σ and insignificant with "slightly different assumptions", because a few precise, close-on-sky pulsars dominate | compare noise models; drop-out tests | arXiv:2412.01153 | [src] |
| Spectral-index sensitivity | γ depends on the data model of a few pulsars, unlike calibrated detection statistics | report A at fixed γ = 13/3 and the free-γ fit | arXiv:2306.16213 | [src: Sect. I] |
| Time-dependent signal strength | PPTA's first-half data limit is in tension with the full-set amplitude; EPTA's 10.3 yr spectrum is in mild tension with the full 24.7 yr | split-data tests | arXiv:2306.16215; arXiv:2306.16214 | [src] |
| Clock and ephemeris errors | monopolar and dipolar correlations; NANOGrav sees a quasi-monochromatic monopole in frequency bin 2 (3.95 nHz) | fit monopole and dipole processes jointly with HD | arXiv:2306.16213 | [src: Fig. 6 caption] |
| Significance calibration | Bayes factors need a null distribution; sky scrambles and phase shifts give p = 10⁻³ against a BF of 200–1000 | quote p-values, not only Bayes factors | arXiv:2306.16213 | [src] |
| Cross-array modelling differences | parameters agree within 1σ; a standardised noise model reduces the tension in pulsar noise parameters | IPTA common noise model | arXiv:2309.00693 | [src] |
| Cosmic variance of HD | intrinsic scatter of the correlation even without noise | compare with the Allen variance | arXiv:2205.05637 | [src] |
| SMBHB prior in model comparison | new-physics Bayes factors 10–100 depend on the SMBHB population prior | quote with the prior; prefer excluded-region statements | arXiv:2306.16219 | [src] |

NANOGrav's minimum noise characteristic strain is 7 × 10⁻¹⁵ at 5 nHz, and
its power-law-integrated sensitivity roughly agrees with the recovered
background amplitude (arXiv:2306.16218) [src].

### 1.1 Theory templates for cosmological backgrounds
<!-- key: theory-templates-for-cosmological-backgrounds -->

| Systematic | Mechanism and size | Mitigation or test | Citation | Flag |
|---|---|---|---|---|
| String loop distribution | the Gμ limit from LVK O3 changes by orders of magnitude between loop models; ≲ 4 × 10⁻¹⁵ holds for one model only | quote the loop model; use the interpolating model as a bracket | arXiv:2101.12248 | [src] |
| Phase-transition peak-frequency factors | numerical factors in the peak frequencies shift T_* between templates and can be reabsorbed in T_* | compare T_* only within one template | arXiv:2306.16219 | [src: Sect. V.3] |
| Template priors | the low-frequency slope prior (a ≥ 1 for pt-bubble, a ≥ 3 for pt-sound) changes how much an added SMBHB term helps the fit | report the prior table with the Bayes factor | arXiv:2306.16219 | [src: Sect. V.3] |
| Effective potential | resummation is required and four-loop infrared divergences remain; non-perturbative input needed | lattice or dimensional-reduction cross-checks | arXiv:2204.05434 | [src: Sect. 6.2] |
| Definition of α | several definitions map differently onto the bag equation of state | state the definition (trace of the energy–momentum tensor in the LISA review) | arXiv:2204.05434 | [src: Sect. 6.2, Eq. 37] |
| SIGW source model | the quadratic source with f_NL may not capture non-Gaussianity; the amplitude can differ significantly | non-perturbative treatment of the curvature field | arXiv:2412.06764 | [src] |
| PBH abundance in SIGW fits | the PBH tail is sensitive to non-Gaussianity; overproduction disfavours Gaussian SIGW at 2σ | include the PBH constraint in the fit | arXiv:2306.17149 | [src] |
| Dark-sector energy | a secluded MeV-scale transition adds dark radiation, constrained by BBN and CMB | include N_eff bounds or a decay before neutrino decoupling | arXiv:2306.09411 | [src] |

## 2. Primordial-black-hole constraints
<!-- key: primordial-black-hole-constraints -->

| Systematic | Mechanism and size | Mitigation or test | Citation | Flag |
|---|---|---|---|---|
| Milky Way halo model | microlensing limits depend on the assumed dark-matter density profile and velocity dispersion; a relaxation by up to two orders of magnitude has been claimed, contested because the profiles used conflict with the rotation curve | fit halo models to the rotation curve; quote limits for several | Carr et al. 2026, arXiv:2601.06024 | [src: Sect. IV.2.1] |
| Initial clustering | clustered PBHs change microlensing rates, but the clustering needed conflicts with Lyα-forest constraints, so limits are "largely unchanged" in viable models | check the clustering against small-scale structure | arXiv:2601.06024 | [src: Sect. IV.2.1] |
| Event selection, efficiency, passbands, self-lensing | the OGLE–MACHO discrepancy on halo lenses is attributed to these choices by one side, which concludes OGLE puts "no meaningful constraints" on halo PBHs | independent efficiency calculations; blind event selection | Hawkins 2025, arXiv:2509.05400; reply side arXiv:2403.02386 | [src] |
| Wave optics and finite source size | suppress magnification for light lenses; set the low-mass end of optical microlensing near 10⁻¹⁰ M☉ (asteroid window) | X-ray-pulsar sources, shorter wavelengths | arXiv:2601.06024 | [src: Sect. IV.2.1, V] |
| Accretion physics | moves the mass above which CMB accretion limits dominate between ~20 and ~50 M☉ | DM-halo accretion simulations; bracket models | Serpico et al. 2020, arXiv:2002.10771 | [src] |
| Evaporation modelling | memory burden, extra dimensions or exotic remnants modify evaporation bounds | state the evaporation model | arXiv:2601.06024 | [src: Sect. IV.1.1] |
| Withdrawn limits | white-dwarf ignition (fails in hydrodynamic simulations) and γ-ray-burst femtolensing (sources too large) no longer constrain the asteroid window | do not cite as constraints | arXiv:2601.06024 | [src: Sect. V] |
| Mass function and binary channel | LVK limits depend on the early-Universe binary formation and suppression; O3 hierarchical limits are insensitive to non-Gaussianity type and QCD modifications of the mass function | test several mass functions | Andrés-Carcasona et al. 2024, arXiv:2405.05732 | [src] |

## 3. Early dark energy and recombination fits
<!-- key: early-dark-energy-and-recombination-fits -->

| Systematic | Mechanism and size | Mitigation or test | Citation | Flag |
|---|---|---|---|---|
| Prior-volume (projection) effects | parameters z_c, θ_i undefined at f_EDE = 0; marginalisation pulls f_EDE down; profile intervals 0.072 ± 0.036 (Planck + BOSS) and 0.09 ± 0.03 (ACT DR6 + DESI DR2 combination) against Bayesian upper limits | report profile likelihood with the posterior | arXiv:2112.12140; arXiv:2505.08051 | [src] |
| Choice of BAO sample | DESI instead of BOSS BAO loosens the P-ACT-LB bound from < 0.10 to < 0.12 through the shift of best-fit Ω_m | report both BAO samples | arXiv:2503.14454 | [src: Sect. V.1] |
| Planck-likelihood dependence | combining ACT with Planck shifts H0 up; with WMAP much less; NPIPE tightens Planck bounds | quote P-ACT and W-ACT | arXiv:2503.14454 | [src: Sect. V.1] |
| Code and emulator accuracy | emulator neutrino convention: < 0.1 km/s/Mpc in H0; camb–class χ² difference 0.06; class unstable for extreme n = 2 | cross-check with full Boltzmann runs | arXiv:2503.14454 | [src: Sect. V.1] |
| Large-scale-structure data | EDE fits raise power by 10% at k = 1 h/Mpc; the significance with SH0ES drops below 2σ when LSS data are added | include S8 and full-shape data or state their absence | arXiv:2003.07355 | [src] |

### 3.1 Varying constants and modified recombination
<!-- key: varying-constants-and-modified-recombination -->

| Systematic | Mechanism and size | Mitigation or test | Citation | Flag |
|---|---|---|---|---|
| Phenomenological step | constants jump at z = 50 with no driving field; first-principles models with field perturbations and energy density reach different conclusions | state the model; test a dynamical implementation | arXiv:2503.14454 | [src: Sect. V.2] |
| Planck-driven departures | P-ACT m_e/m_e,0 = 0.856 is 2.4σ low, but ACT alone gives 1.02 and W-ACT 0.921 | compare P-ACT with W-ACT and ACT alone | arXiv:2503.14454 | [src: Eqs. 17–18] |
| Geometric degeneracy | a free m_e opens a severe degeneracy broken only by BAO; with Ω_k free the bound on Ω_k weakens by more than a factor of two | always quote the BAO data set; add SNe | arXiv:2503.14454 | [src: Sect. V.2.1–V.2.2] |
| BAO sample in ModRec | DESI and BOSS give different X_e(z) reconstructions through r_d H0 and Ω_m | report both | arXiv:2503.14454 | [src: Sect. V.5] |
| Recombination code | HyRec and CosmoRec treat the constant dependence with similar accuracy | cross-check codes | arXiv:2503.14454 | [src: Sect. V.2] |
| Quasar-absorber calibration | wavelength-calibration errors of earlier spectrographs; ESPRESSO with a laser frequency comb removes them, leaving 0.4 ppm systematic | laser-comb calibration; blinded analysis | arXiv:2112.05819 | [src] |

## 4. Spectral-distortion measurements
<!-- key: spectral-distortion-measurements -->

- **Absolute calibration.** FIRAS measures the difference between the sky
  and a blackbody, so the limits are set by the calibrator; PIXIE compares
  the sky with an external blackbody target and aims at sub-percent absolute
  calibration (arXiv:astro-ph/9605054; arXiv:2405.20403) [src].
- **Foregrounds.** Galactic and extragalactic emission dominate the
  monopole; the Voyage 2050 sensitivities are quoted "in the presence of
  foregrounds", with PIXIE σ(μ) ≃ 3 × 10⁻⁸ — comparable to the ΛCDM signal,
  which is why Super-PIXIE-class sensitivity is needed for a μ detection
  (arXiv:1909.01593) [src: Sect. 1.2]. The FIRAS μ-map constraints are
  "robust against galactic and extragalactic foreground contaminations"
  (arXiv:2206.02762) [src].
- **Imager versus spectrometer.** μ anisotropies from Planck maps carry
  instrumental and foreground uncertainties that cancel their lower noise
  (arXiv:2206.02762) [src].
- **Low frequencies.** Free–free absorption after z ≲ 10³ alters the shape
  of primordial distortions at very low frequencies, which a template must
  include (arXiv:1109.6552) [src].

## 5. Energy-injection and magnetic-field limits
<!-- key: energy-injection-and-magnetic-field-limits -->

- **Deposition efficiency.** Planck uses the on-the-spot approximation and a
  constant f_eff (arXiv:1807.06209) [src: Sect. 7.9]; model limits need the
  f_eff(E) tables of arXiv:1506.03811 [src], and backreaction and the
  low-energy cascade need DarkHistory (arXiv:1904.09296; arXiv:2303.07370)
  [src].
- **Clumping model.** The three-zone model neglects Lyα photon mixing;
  constraints are to be read "in the context of this model"
  (arXiv:2503.14454) [src: Sect. V.3]; MHD-informed recombination changes
  the inference (arXiv:2503.09599) [src].
- **Low-ℓ polarisation likelihood.** SRoll2 low-ℓ EE allows larger PMF
  amplitudes than the Planck 2018 baseline, especially for positive n_B:
  √⟨B²⟩ < 0.72 against < 0.69 nG (arXiv:2204.06302) [src].
- **Lyα noise model.** The PMF hint in the forest disappears with
  conservative noise modelling (arXiv:2501.06299) [src].
- **Blazar duty cycle.** The IGMF lower bound rises from 7.1 × 10⁻¹⁶ G (10
  yr) to 3.9 × 10⁻¹⁴ G (10⁷ yr) (arXiv:2306.05132) [src].

## 6. Referee checklist
<!-- key: referee-checklist -->

1. PTA: array, data release, number of pulsars and span; A at γ = 13/3 and
   the free fit; HD significance as a calibrated p-value, not only a Bayes
   factor.
2. PTA new physics: SMBHB prior used in any Bayes factor; whether the claim
   is a fit or an exclusion region independent of the signal's origin.
3. Ω_GW: h convention, reference frequency, spectral index and prior
   (log-uniform or uniform) for any LVK limit.
4. Strings: loop-distribution model, stable or metastable or superstring.
5. Phase transitions: definition of α, template (collisions, sound waves,
   turbulence), N_eff/BBN bound on a dark sector.
6. PBHs: mass function, halo model, binary formation channel, and whether
   the OGLE limits are used with their dispute noted.
7. EDE: n, priors on f_EDE, z_c, θ_i; Bayesian or profile; BAO sample; with
   or without SH0ES; LSS data included.
8. Varying constants: step redshift, which constant, BAO and SNe included;
   phenomenological model stated as such.
9. Distortions: FIRAS limit used (1996 or the 2022 reanalysis), confidence
   level, foreground model of any forecast.
10. Energy injection: on-the-spot or full deposition; f_eff source.
11. PMFs: B_1Mpc versus √⟨B²⟩, n_B, helicity, clumping model.

## Not verified
<!-- key: not-verified -->

- The size of the EPTA and PPTA noise-model differences in the IPTA
  comparison (individual pulsar tables) was not read.
- No independent critique of the PTA noise models outside the collaborations
  and the five-array reanalysis was read this session.
- The PIXIE and FOSSIL foreground budgets behind their forecasts were not
  read in the bodies.
- The OGLE reply to Hawkins 2025, if any, was not searched.
