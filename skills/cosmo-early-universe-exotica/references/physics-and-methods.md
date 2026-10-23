# Early-Universe exotica — physics and methods

Scope: the physics behind each non-standard early-Universe ingredient (gravitational-wave backgrounds,
phase transitions, defects, primordial black holes, early dark energy, modified recombination, varying
constants, spectral distortions, energy injection, primordial magnetic fields, axion-like particles), the
observables, the models used in current analyses and the public codes. Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Eq. n]`, `[src: Table n]` body read;
`[sec]` named secondary source; `[der]` derived here.

## 1. Stochastic gravitational-wave background
<!-- key: stochastic-gravitational-wave-background -->

A stochastic gravitational-wave background (SGWB) is characterised by its energy density per logarithmic
frequency in units of the critical density, Ω_GW(f) = (1/ρ_c) dρ_GW/d ln f, or equivalently by the
characteristic strain h_c(f). The textbook relation is Ω_GW(f) = (2π²/3H0²) f² h_c(f)², so an Ω_GW quoted
without h (or H0) is ambiguous by h². Pulsar-timing arrays (PTAs) fit h_c = A (f / 1 yr⁻¹)^α; the
timing-residual power spectral density then scales as f^(−γ) with γ = 3 − 2α. A population of circular
supermassive black-hole binaries (SMBHBs) evolving by gravitational radiation alone gives α = −2/3, γ =
13/3 (Phinney 2001, arXiv:astro-ph/0108028, which relates the background to the comoving energy emitted by
the sources [src]); NANOGrav states its fiducial model as f^(−2/3) in characteristic strain and f^(−13/3)
in timing residuals (arXiv:2306.16213) [src: Sect. I].

### 1.1 The PTA signature and its statistics
<!-- key: the-pta-signature-and-its-statistics -->

- **Hellings–Downs (HD) correlation.** An isotropic, unpolarised background produces a quadrupolar
  correlation of timing residuals as a function of the angle between two pulsars (Hellings & Downs 1983,
  doi:10.1086/183954). Monopolar correlations point to clock errors, dipolar ones to ephemeris errors;
  only the HD pattern identifies gravitational waves.
- **CURN versus HD.** The common uncorrelated red noise (CURN) model has the same spectrum in every pulsar
  but no inter-pulsar correlation. A Bayes factor of HD over CURN measures the evidence for the
  correlation itself; a Bayes factor of CURN over pulsar noise alone measures only the common spectrum.
  NANOGrav 15 yr reports both: > 10¹⁴ for a power-law background over independent pulsar noise, and
  200–1000 for HD over CURN, depending on spectral modelling (arXiv:2306.16213) [src: abstract].
- **Calibrating the significance.** NANOGrav builds the null distribution of the HD Bayes factor by
  removing inter-pulsar correlations (phase shifts, sky scrambles), giving p = 10⁻³ (about 3σ); the
  frequentist optimal statistic gives p = 5 × 10⁻⁵ to 1.9 × 10⁻⁴ (3.5–4σ) (arXiv:2306.16213) [src]. PPTA
  validates its correlations by randomising pulsar positions on the sky (arXiv:2306.16215) [src].
- **Cosmic variance of HD.** Even with noise-free data the measured correlation at fixed angle scatters
  around the HD curve. Allen 2022 (arXiv:2205.05637) derives the variance for discrete point sources and
  splits it into cosmic variance and pulsar variance; measuring it informs on the nature of the sources
  [src].
- **Frequency bins.** PTA frequencies are f_i = i/T with T the data span; for NANOGrav 15 yr, T = 16.03
  yr, excess power appears in bins 1–8 and HD power in bins 1–5 and 8 (arXiv:2306.16213) [src: Fig. 6
  caption]. The low bins carry most of the information on γ, so a fitted γ is fragile.
- **Spectral-index fragility.** NANOGrav warns that "the estimation of γ is very sensitive to minor
  details in the data model of a few pulsars", unlike the calibrated detection statistics
  (arXiv:2306.16213) [src: Sect. I].

### 1.2 Ground-based interferometers
<!-- key: ground-based-interferometers -->

LIGO–Virgo–KAGRA (LVK) cross-correlate detector pairs; the optimal cross-correlation method and its
sensitivity are set out in Allen & Romano 1999 (arXiv:gr-qc/9710117) [src]. Limits are quoted on Ω_GW at a
reference 25 Hz for power laws Ω_GW ∝ f^α with α = 0 (scale-invariant, typical of cosmological sources),
2/3 (compact binaries) and 3, each with a log-uniform prior on the amplitude (arXiv:2101.12130) [src].
Note the clash of notation: α is the strain index in PTA papers and the Ω_GW index in LVK papers.

### 1.3 Integrated bounds on a primordial background
<!-- key: integrated-bounds-on-a-primordial-background -->

A background produced before BBN counts as extra radiation, so BBN and CMB bounds on N_eff cap its
integrated energy density; the CMB bound depends on adiabatic or homogeneous initial conditions
(arXiv:2204.05434) [src: Sect. 5.1.3]. Values in `results.md` §2.

## 2. First-order phase transitions
<!-- key: first-order-phase-transitions -->

A first-order phase transition (FOPT) proceeds by nucleation of bubbles of the true vacuum. Gravitational
waves come from three sources: bubble-wall collisions, sound waves in the plasma and magnetohydrodynamic
turbulence. The first estimates (Kamionkowski et al. 1994, arXiv:astro-ph/9310044) treated collisions and
Kolmogorov turbulence and found the minimal-Standard-Model electroweak transition far too weak, Ω ~ 10⁻²²
at ~4 mHz [src]. The first 3D simulations including the fluid showed that compression waves keep sourcing
GWs long after the bubbles have merged, so for a wide range of models "the main source ... is the sound
the bubbles make" (Hindmarsh et al. 2014, arXiv:1304.2433) [src].

**The four parameters** (LISA Cosmology WG 2022, arXiv:2204.05434) [src: Sect. 6.2]:

- T_* — the plasma temperature at percolation, when about one third of the comoving volume has converted;
  for moderately strong transitions T_* ≈ T_n, the nucleation temperature at which the critical action S_c
  ≈ 140.
- α — the energy released as a fraction of the radiation energy, α = Δθ/ρ_rad with Δθ = ΔV(T) − (T/4)
  ∂ΔV/∂T [src: Eq. 37]. Several definitions coexist; they map differently onto the bag equation of state.
- β/H_* = T_* d(S_3/T)/dT at T_* — the inverse duration [src: Eq. 39]; the amplitude falls and the peak
  frequency rises with β/H_*.
- v_w — the bubble-wall velocity, which with α fixes the efficiency of conversion into bulk fluid motion.

The effective potential needs resummation of infrared-sensitive bosonic modes and has true infrared
divergences at four loops, so non-perturbative calculations matter [src: Sect. 6.2]; the predicted
spectrum carries this theory error.

**Templates and pipelines.** The eLISA study (Caprini et al. 2016, arXiv:1512.06239) set the
model-independent sensitivity to collisions, turbulence and sound waves [src]; its update (Caprini et al.
2020, arXiv:1910.13125) rests on sound-wave simulations, clarifies "common misconceptions" and introduces
the PTPlot web tool [src]. The 2024 LISA pipeline (arXiv:2403.03723) builds a template databank for the
three sources and forecasts ~10% reconstruction of the parameters in part of the space, accounting for
Galactic and extragalactic foregrounds — a **forecast** [src].

**At nanohertz frequencies.** A transition at T_* ~ MeV–GeV lands in the PTA band. NANOGrav fits two
templates, pt-bubble (collisions; low-frequency index allowed down to a = 1) and pt-sound (sound waves; a
≥ 3), with priors listed in its Table 3 (arXiv:2306.16219) [src: Sect. V.3]. Energy released in a secluded
dark sector at MeV temperatures counts as dark radiation, so BBN and CMB bounds on N_eff apply (Bringmann
et al. 2023, arXiv:2306.09411) [src].

## 3. Cosmic strings and other defects
<!-- key: cosmic-strings-and-other-defects -->

Topological defects form when a symmetry breaks and the vacuum manifold has non-trivial topology (Kibble
1976, doi:10.1088/0305-4470/9/8/029). Strings are characterised by their tension in units of Newton's
constant, Gμ (Gμ/c²).

- **CMB.** Strings source active, incoherent perturbations. Planck added the string power spectrum to ΛCDM
  with an amplitude f₁₀ at ℓ = 10 and modelled both Nambu–Goto and Abelian-Higgs field-theory strings,
  "spanning the range of theoretical uncertainty" (Planck 2013 XXV, arXiv:1303.5085) [src].
- **Gravitational waves from loops.** Loops oscillate at f = 2k/ℓ for harmonic k; NANOGrav writes
  Ω_GW^cs(f) = (8π/3H0²)(Gμ)² Σ_k P_k I_k(f), summed to k_max = 10⁵ (arXiv:2306.16219) [src: Eq. 40]. The
  loop number density is the dominant modelling uncertainty; the loop distribution calibrated on
  Nambu–Goto simulations is given by Blanco-Pillado et al. 2014 (arXiv:1309.6637) [src]. LVK tests two
  loop-distribution models and an interpolating third one, with cusps, kinks and kink–kink collisions
  (arXiv:2101.12248) [src].
- **Flavours.** Stable field-theory strings, metastable strings (which decay by monopole–antimonopole
  nucleation, so their low-frequency spectrum is suppressed) and cosmic superstrings (reduced
  intercommutation probability) are fitted separately; priors are log₁₀ Gμ ∈ [−14, −6] for stable strings
  and superstrings and [−14, −1.5] for metastable strings (arXiv:2306.16219) [src: Sect. V.4]. Metastable
  strings tied to B−L breaking predict a large signal in the LVK band over a sizable part of the parameter
  space that fits PTA data (Buchmüller et al. 2020, arXiv:2009.10649) [src].
- **Domain walls** are the other defect fitted to PTA data (arXiv:2306.16219) [src].

## 4. Primordial black holes
<!-- key: primordial-black-holes -->

Black holes may form in the early Universe from the collapse of large overdensities (Carr & Hawking 1974,
doi:10.1093/mnras/168.2.399), and those light enough evaporate by Hawking radiation (Hawking 1974,
doi:10.1038/248030a0). The abundance is quoted as f_PBH = Ω_PBH/Ω_DM, for a monochromatic mass function
unless stated; the Carr et al. 2026 review (arXiv:2601.06024) also maps the constraints onto extended mass
functions [src: Sect. VI title].

**Formation.** The standard route is critical collapse of curvature fluctuations, affected by the QCD
transition and by non-Gaussianity; other routes are phase transitions, topological defects and
non-inflationary scenarios (arXiv:2601.06024) [src: Sect. II outline]. The LISA review treats the
threshold for collapse and its dependence on the thermal history (arXiv:2204.05434) [src: Sect. 10.2
outline].

**Constraint families**: evaporation, microlensing, gravitational waves, dynamics and accretion
(arXiv:2601.06024, Sect. IV); the summary table is in `results.md` §5.

**The asteroid-mass window**, ~10⁻¹⁷ to 10⁻¹⁰ M☉, "remains the only unconstrained region": too heavy to
evaporate, too light for optical microlensing. White-dwarf ignition limits were eliminated by hydrodynamic
simulations, femtolensing of γ-ray bursts fails because the sources are too large, and neutron-star
capture limits depend on the uncertain dark-matter density of globular clusters; X-ray-pulsar microlensing
and Solar System ephemerides are proposed tests (arXiv:2601.06024) [src: Sect. V].

**PBH binaries and LVK.** Binaries formed in galactic haloes (arXiv:1603.00464) or in the early Universe
(arXiv:1603.08338) predict different merger rates; see `open-questions.md` §2.

**Accretion and the CMB.** Massive PBHs accrete and inject energy that alters recombination. With a
dominant non-PBH dark-matter component, a dark matter halo forms around each PBH and changes the bound;
the CMB then dominates other limits above 20–50 M☉, the threshold depending on accretion physics (Serpico
et al. 2020, arXiv:2002.10771) [src].

## 5. Scalar-induced gravitational waves
<!-- key: scalar-induced-gravitational-waves -->

At second order in perturbation theory, scalar curvature perturbations source tensor modes during
radiation domination; future detectors can thus constrain the primordial spectrum on scales far below
those of the CMB and large-scale structure (Ananda et al. 2006, arXiv:gr-qc/0612013) [src]. The kernel of
the induced spectrum is universal and has been integrated analytically, which makes the remaining
numerical integrals easy (Kohri et al. 2018, arXiv:1804.08577) [src]; enhancement can also come from early
matter-dominated stages [src].

- **Why it matters.** The CMB fixes A_s ≈ 2.10 × 10⁻⁹ at 0.05 Mpc⁻¹; a slightly red spectrum extrapolated
  to small scales predicts no observable SIGW, so a PTA-level SIGW requires a departure from single-field
  slow-roll, for example an inflection point in the potential (NANOGrav, arXiv:2306.16219) [src: Sect.
  V.2]. PBH formation in single-field models is itself debated [src: Sect. V.2].
- **Templates.** NANOGrav fits a δ-function, a Gaussian and a box-shaped curvature spectrum (sigw-delta,
  sigw-gauss, sigw-box) (arXiv:2306.16219) [src: Sect. V.2].
- **The PBH link.** Large enough curvature perturbations also form PBHs, so a SIGW interpretation must not
  overproduce them; the PBH abundance is exponentially sensitive to the tail of the curvature
  distribution, hence to non-Gaussianity (Franciolini et al. 2023, arXiv:2306.17149) [src]. The quadratic
  source model with f_NL may not capture non-Gaussianity adequately, and the GW amplitude can then differ
  "significantly" (Iovino et al. 2024, arXiv:2412.06764) [src].
- f_NL measured on CMB and LSS scales belongs to `cosmo-inflation-primordial`; the small-scale
  non-Gaussianity here is not constrained by those measurements.

## 6. Early dark energy
<!-- key: early-dark-energy -->

Early dark energy (EDE) is a component that behaves like a cosmological constant at early times (z ≳ 3000)
and then dilutes like radiation or faster, which reduces the sound horizon at decoupling and raises the
CMB-inferred H0 (Poulin et al. 2019, arXiv:1811.04083) [src]. Whether it resolves the Hubble tension is
judged in `cosmo-tensions-anomalies`; this section holds the physics and the constraints.

**The axion-like model used by ACT, SPT and most analyses** (ACT DR6, Calabrese et al. 2025,
arXiv:2503.14454) [src: Sect. V.1]:

- Potential V(φ) = m² f² (1 − cos(φ/f))ⁿ [src: Eq. 10]. n = 1 is excluded because the field would add to
  dark matter at late times; n ≥ 2 is viable; n = 3 is the baseline of the literature.
- Phenomenological parameters: f_EDE = 8πG ρ_EDE(z_c)/(3H²(z_c)), the maximum fractional contribution,
  reached at the critical redshift z_c; and θ_i = φ_i/f, the initial displacement [src: Eqs. 11–12]. The
  field is frozen by Hubble friction until H ~ m near z_c.
- Priors in ACT DR6: f_EDE ∈ [0.001, 0.5], log₁₀ z_c ∈ [3.0, 4.3], θ_i ∈ [0.1, 3.1], uniform [src: Sect.
  V.1].
- Signatures: for z_c ~ z_eq, features at ℓ ~ 400–800 and broader imprints at smaller scales; partly
  absorbed by Ω_c h² and n_s, so high-resolution polarisation breaks the degeneracies [src: Sect. V.1].
  f_EDE correlates positively with H0, Ω_c h² and S8 [src: Fig. 12 caption].
- Codes and their accuracy: `systematics.md` §3 and §12 below.

**Why EDE raises S8.** An EDE fit to CMB and SH0ES gives scale-dependent changes in the matter power
spectrum, including 10% more power at k = 1 h/Mpc, which aggravates tension with large-scale structure
(Hill et al. 2020, arXiv:2003.07355) [src].

**Bayesian versus frequentist.** f_EDE = 0 makes z_c and θ_i undefined, so marginalised posteriors carry
prior-volume effects. A grid and profile likelihood on Planck and BOSS full shape found the allowed f_EDE
"strongly depends on the particular choice of the other parameters", and gave f_EDE = 0.072 ± 0.036 (68%)
free of volume effects (Herold et al. 2022, arXiv:2112.12140) [src]. The model class and its theoretical
issues (a second coincidence problem, S8, BOSS EFT full shape) are reviewed by Poulin et al. 2023
(arXiv:2302.09032) [src].

## 7. Modified recombination and varying constants
<!-- key: modified-recombination-and-varying-constants -->

**Physics.** Recombination depends on the fine-structure constant α_EM and the electron mass m_e at z ~
10³. The dominant effects are the Thomson cross section, σ_T ∝ α_EM² m_e⁻², and the hydrogen energy
levels, E ∝ α_EM² m_e; larger values recombine earlier and move the acoustic and damping scales (ACT DR6,
arXiv:2503.14454) [src: Sect. V.2]. Earlier recombination can raise the CMB-inferred H0 while keeping the
CMB fit, and a time-varying m_e in a curved ΛCDM model was the first concrete example (Sekiguchi et al.
2021, arXiv:2007.03381) [src].

**Standard phenomenological set-up** (arXiv:2503.14454) [src: Sect. V.2]:

- The constant takes a free value before an instantaneous step at z = 50 and the laboratory value after;
  recombination physics through HyRec in class (CosmoRec is "similarly accurate").
- Flat priors m_e/m_e,0 ∈ [0.3, 1.7], α_EM/α_EM,0 ∈ [0.6, 1.4], Ω_k ∈ [−0.6, 0.6] when curvature is free
  [src: Sect. V.2.1–V.2.3].
- The model "is not physical": no field drives the variation. A first-principles implementation, with
  perturbations and energy density of the driving field, can reach "rather different conclusions" [src:
  Sect. V.2].
- BAO break the strong geometric degeneracy that a free m_e opens in the primary CMB [src: Sect. V.2.1];
  m_e with Ω_k preserves both the acoustic and the damping scales, which is why that pair moves H0 most
  [src: Sect. V.2.2].

**Model-independent recombination (ModRec).** Departures ΔX_e(z) of the free-electron fraction are fitted
at seven control points between z = 533 and 1600, joined by a cubic spline bounded by 0 ≤ X_e ≤ X_e^max,
with reionisation and helium recombination unchanged; it captures primordial magnetic fields, varying m_e
and dark-matter annihilation as special cases; BAO are essential, and the choice of DESI or BOSS changes
the reconstruction through r_d H0 and Ω_m (arXiv:2503.14454) [src: Sect. V.5]. A data-driven m_e(z) built
to raise H0 resolves the tension with Planck + ACT but not once DESI DR2 BAO are added, because "raising
H0 by modifying recombination generically lowers Ω_m" (Lee et al. 2026, arXiv:2606.06495) [src].

**Local and intermediate-redshift α.** Quasar absorbers measure Δα/α at z ~ 1–2 (ESPRESSO data in
`surveys-and-data.md` §6). A CMB bound (z ~ 1100) and an absorber bound (z ~ 1) test different epochs and
must not be compared as one number.

## 8. CMB spectral distortions
<!-- key: cmb-spectral-distortions -->

Energy released into the photon–baryon plasma after thermalisation becomes inefficient leaves a departure
from a blackbody. The Compton y-distortion of hot electrons (Zeldovich & Sunyaev 1969,
doi:10.1007/BF00661821, on the interaction of matter and radiation in a hot universe) is produced late; at
earlier times Compton scattering establishes a Bose–Einstein spectrum with chemical potential μ. The
thermalisation problem — double Compton, bremsstrahlung and recombination — is solved with CosmoTherm
(Chluba et al. 2011, arXiv:1109.6552), which computes the distortions from annihilating dark matter,
decaying relics, dissipation of acoustic waves and quasi-instantaneous heating; the adiabatic cooling of
electrons alone gives a negative μ-type distortion of ΔI/I ~ 10⁻⁸ in the GHz band [src]. Distortions probe
the thermal history at z ≲ 2 × 10⁶ (Cyr et al. 2026, arXiv:2609.16194) [src]. Recent reviews: Chluba 2025
(arXiv:2502.05188) [src] and Cyr et al. 2026 [src].

**What ΛCDM predicts.** If near scale invariance holds to small scales, the dissipation of acoustic modes
gives μ ≃ (2.3 ± 0.14) × 10⁻⁸, with the window W_μ(k) dominated by k ≃ 10²–10⁴ Mpc⁻¹; no detection above μ
= 2 × 10⁻⁸ would immediately rule out enhanced small-scale power at k ≃ 10–10⁴ Mpc⁻¹, and a non-detection
at the ΛCDM level would "immediately require new physics" (Chluba et al. 2019 Voyage 2050 white paper,
arXiv:1909.01593) [src: Sect. 2.1]. Distortions therefore link to the primordial spectrum
(`cosmo-inflation-primordial`) and to PBH formation, which needs enhanced small-scale power (§4).

**Anisotropic distortions.** A μ map correlated with CMB temperature and polarisation constrains
primordial non-Gaussianity on 10 ≲ k ≲ 5 × 10⁴ (Bianchini et al. 2022, arXiv:2206.02762) [src].

## 9. Energy injection during recombination and the dark ages
<!-- key: energy-injection-during-recombination-and-the -->

Energy injected after recombination by decaying or annihilating particles, evaporating or accreting PBHs,
or other exotic sources heats and ionises the gas, broadens the last-scattering surface and damps the CMB
anisotropies; energy carried away by 100 keV – 1 TeV photons appears instead in the X-ray and γ-ray
backgrounds (Chen et al. 2003, arXiv:astro-ph/0310473) [src: abstract].

- **Annihilation parameter.** Planck constrains p_ann ≡ f_eff ⟨σv⟩/m_χ (Planck 2018 VI, arXiv:1807.06209)
  [src: Eq. 86], computed with the ExoClass branch of class v2.6.3 and HyRec, the on-the-spot
  approximation and a constant f(z) = f_eff, because the anisotropies are weakly sensitive to the redshift
  dependence of the deposited fraction [src: Sect. 7.9].
- **From p_ann to a model.** f_eff values for photons and e⁺e⁻ injected at keV–TeV energies, weighted by
  the spectrum of annihilation products, map the Planck bound onto any s-wave model (Slatyer 2016,
  arXiv:1506.03811) [src]. For decays, a principal-component analysis shows the CMB imprint is
  approximately one number per model, also for lifetimes shorter than the age of the Universe (Slatyer et
  al. 2017, arXiv:1610.06933) [src].
- **Beyond on-the-spot.** DarkHistory solves the free-electron fraction and gas temperature together with
  the cooling cascade of the injected particles, including backreaction (Liu et al. 2019,
  arXiv:1904.09296) [src]. Its extension computes the post-recombination spectral distortion of exotic
  injections, which has a high-energy feature unique to high-energy particles and may be detectable by
  PIXIE-class experiments (**forecast**), and recasts decay bounds on axion-like-particle couplings to
  photons (Liu et al. 2023, arXiv:2303.07370) [src].
- Energy released before recombination is constrained instead by distortions (§8) and by BBN (`cosmo-bbn`,
  which holds the decaying-relic limits for lifetimes 0.01 s – 10¹² s). The 21 cm signal of the dark ages
  as a probe of this heating belongs to `cosmo-reionization-21cm`.

## 10. Primordial magnetic fields
<!-- key: primordial-magnetic-fields -->

Magnetic fields in galaxies and clusters are amplified seeds; whether the seeds are primordial (inflation,
phase transitions) or astrophysical is open. The review of generation, evolution and observational tests
is Durrer et al. 2013 (arXiv:1303.7121) [src].

**CMB channels** (Planck 2015 XIX, arXiv:1502.01594) [src]: the impact on the anisotropy spectra
(compensated and passive modes), Faraday rotation of polarisation, the ionisation history (dissipation by
ambipolar diffusion and decaying MHD turbulence after recombination, Paoletti et al. 2022,
arXiv:2204.06302 [src]), magnetically induced non-Gaussianity and broken statistical isotropy. Amplitudes
are quoted as B_1Mpc, the comoving field smoothed on 1 Mpc, or as √⟨B²⟩, with a spectral index n_B (n_B =
−2.9 is "nearly scale-invariant"); helicity changes the limits.

**Baryon clumping at recombination.** Blue-tilted PMFs with kpc correlation lengths drive small-scale
baryon inhomogeneities after photon decoupling, which accelerate recombination through the quadratic
source term and shrink the sound horizon. Two counteracting effects change Silk damping (faster hydrogen
recombination suppresses it, earlier helium recombination enhances it), the first being empirically
dominant, so the damping tail is the probe (ACT DR6, arXiv:2503.14454) [src: Sect. V.3]. The standard
parametrisation is a three-zone model, scenario "M1" (f₂ = 1/3, Δ₁ = 0.1, Δ₂ = 1), leaving one parameter,
the clumping variance b with 1 + b = Σ f_i Δ_i² [src: Eq. 26]; it neglects Lyα photon mixing [src: Sect.
V.3]. The proposal that PMF clumping relieves the H0 and S8 tensions is Jedamzik et al. 2020
(arXiv:2004.09487) [src]; recombination computed with full MHD simulations and Lyα radiative transfer
replaces the toy model in Jedamzik et al. 2025 (arXiv:2503.09599) [src]. Faraday-rotation effects are not
used in the ACT analysis and are expected to be weaker [src: Sect. V.3].

**Lower bounds from γ rays.** TeV photons from blazars pair-produce on the extragalactic background light;
the pairs inverse-Compton scatter into a GeV cascade, which an intergalactic field deflects out of the
line of sight. The non-observation of the cascade gives a lower bound, which improves as λ_B^(−1/2) for
correlation lengths below a megaparsec (Neronov et al. 2010, arXiv:1006.3504) [src]; the bound depends on
the assumed blazar duty cycle (H.E.S.S. + Fermi-LAT, arXiv:2306.05132) [src].

**Small-scale structure.** PMFs add power to the linear matter spectrum at a scale parametrised by k_peak,
to which the Lyα-forest flux power is very sensitive (Pavičević et al. 2025, arXiv:2501.06299) [src].

## 11. Axion-like particles
<!-- key: axion-like-particles -->

Axion physics in cosmology is reviewed by Marsh 2016 (arXiv:1510.07633), from the QCD axion and string
axiverse through misalignment production, perturbations and Jeans scale, CMB and LSS, to non-gravitational
couplings (dark radiation, birefringence, conversion in magnetic fields) [src]. The boundary of this
skill: ultralight axions as all or most of the dark matter (fuzzy dark matter, Lyα and satellite limits)
belong to `cosmo-neutrinos-dark-matter`; cosmic birefringence to `cosmo-inflation-primordial`; axion-like
EDE is §6 here.

- **Ultralight sub-component.** For 10⁻²⁸ < m_ax/eV < 10⁻²⁴ the field is frozen ("dark-energy-like") until
  m_ax ≃ 3H, then oscillates and redshifts as matter; structure is smoothed below a Jeans scale λ_J ∝
  m_ax^(−1/2). ACT DR6 models it with axionCAMB, a mixed-dark-matter halo model for small scales, and the
  axionEmu emulator built on CosmoPower (arXiv:2503.14454) [src: Sect. VI.3, Eqs. 48–50].
- **Thermal axions as dark radiation.** Any light species once in equilibrium with the Standard Model
  leaves ΔN_eff ≥ a minimum set by its decoupling temperature, so sub-percent N_eff measurements reach
  axion couplings to all Standard Model fields, in many cases orders of magnitude beyond laboratory and
  astrophysical bounds — a **forecast** for future CMB experiments (Baumann et al. 2016, arXiv:1604.08614)
  [src]. Measured N_eff values belong to `cosmo-neutrinos-dark-matter` and `cosmo-bbn`.
- **Photon–ALP conversion.** In intergalactic magnetic fields photons convert to ALPs; for n_e ≲ 10⁻⁹ cm⁻³
  this distorts the CMB spectrum too much to explain supernova dimming (Mirizzi et al. 2005,
  arXiv:astro-ph/0506078) [src]. Decaying light ALPs inject energy and are bounded by CMB anisotropies
  through the ALP–photon coupling (arXiv:2303.07370) [src].

## 12. Public codes
<!-- key: public-codes -->

| Code | Purpose | Reference | Flag |
|---|---|---|---|
| PTArcade | wrapper of ENTERPRISE and ceffyl for stochastic or deterministic new-physics signals in PTA data | Mitridate et al. 2023, arXiv:2306.16377 | [src] |
| PTPlot | web tool for LISA phase-transition detection prospects | arXiv:1910.13125 | [src] |
| class EDE (from class_ede), CosmoPower EDE emulators, camb (n = 2) | early dark energy | arXiv:2503.14454 | [src: Sect. V.1] |
| HyRec, CosmoRec | recombination with varying constants | arXiv:2503.14454 | [src: Sect. V.2] |
| class ModRec | model-independent X_e(z) | arXiv:2503.14454 | [src: Sect. V.5] |
| axionCAMB, axionEmu | ultralight axion sub-component | arXiv:2503.14454 | [src: Sect. VI.3] |
| ExoClass (class branch) | energy injection, p_ann | arXiv:1807.06209 | [src: Sect. 7.9] |
| DarkHistory | ionisation and thermal history with exotic injection, backreaction | arXiv:1904.09296 | [src] |
| CosmoTherm | thermalisation and spectral distortions | arXiv:1109.6552 | [src] |

General Boltzmann codes and samplers: `cosmo-software-ecosystem`.

## Not verified
<!-- key: not-verified -->

- The relation Ω_GW(f) = (2π²/3H0²) f² h_c² and γ = 3 − 2α are textbook relations, not re-read in a paper
  this session.
- The definition of the loop models "A, B" in arXiv:2101.12248 and the meaning of NANOGrav's
  stable-c/-k/-m/-n templates were not read.
- The ACT DR6 n = 2 EDE results (Appendix E) and Planck NPIPE EDE bounds were not read.
- Domain-wall template parameters and results in arXiv:2306.16219 were not read.
