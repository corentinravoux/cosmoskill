# CMB primary anisotropies — physics and parameter dependence

Scope: how the primary temperature and E-mode spectra arise (initial
conditions, acoustic driving, baryon loading, radiation driving, diffusion
damping, polarisation generation, projection, reionisation), which parameter
combination each feature fixes, and what the spectra alone cannot constrain.
Estimators, likelihoods and current values are in `physics-and-methods.md`
and `results.md`; definitions of r_s, r_d, θ* and z* in
`cosmo-theory-foundations`.
Snapshot: 2026-10-20

Provenance flags: `[src: <place>]` read this session in the body of the
cited paper at that place; `[src]` its abstract; `[der]` derived here.
Years attached to author names are arXiv submission years. Equations are
given as the cited paper writes them, in its notation (Θ = ΔT/T, conformal
time η, Newtonian-gauge potentials Ψ = δg_tt/2 and Φ = δg_ij/(2a²δ_ij)).

## 1. The observable and its sampling limit
<!-- key: sampling-limit -->

The temperature field Θ(n̂) = ΔT/T is expanded in spherical harmonics and,
if Gaussian, is fully characterised by C_ℓ; the plotted quantity
Δ_T² ≡ ℓ(ℓ+1)C_ℓ T²/2π is the power per logarithmic interval in wavenumber
for ℓ ≫ 1, and ℓ ~ 10² corresponds to degree scales (Hu & Dodelson 2001,
arXiv:astro-ph/0110414) [src: Sect. 2.2, Eqs. 1–3].

- **Cosmic variance.** One sky gives 2ℓ+1 samples per multipole, hence
  ΔC_ℓ = √(2/(2ℓ+1)) C_ℓ; averaging over bands Δℓ ≈ ℓ gives about 1% at
  ℓ = 100 and 0.1% at ℓ = 1000 (arXiv:astro-ph/0110414) [src: Sect. 2.2, Eq. 4].
- **Noise and sky cut.** Gaussian noise of known spectrum enters by
  replacing C_ℓ with signal plus noise in that formula; masking to a
  fraction f_sky inflates errors by f_sky^(−1/2) ("sample variance")
  [src: Sect. 2.2].
- **Monopole and dipole.** A cosmological monopole or dipole cannot be
  separated from our local value or from our peculiar motion; yet the
  spatial variation of the monopole and dipole at recombination is what
  projects into the anisotropies seen today ("free streaming" of power to
  higher ℓ) [src: Sect. 2.2].
- **Polarisation.** E and B are linear, non-local combinations of Q and U.
  Parity invariance makes the B×Θ and B×E correlations vanish; EE is about a
  factor of ten below TT, its oscillations are out of phase with but
  correlated to the temperature ones, and density perturbations produce no
  B modes at first order [src: Sect. 2.3, Eq. 5].

The measured monopole temperature and the dipole amplitude are in
`physics-and-methods.md` §1; the spectrum of the monopole and its
distortions belong to `cosmo-early-universe-exotica`.

## 2. Initial conditions and the Sachs–Wolfe plateau
<!-- key: initial-conditions -->

- **Superhorizon origin.** The degree scale of the acoustic peaks is also
  the particle horizon at recombination, so the perturbations must have been
  laid down while those scales were far outside the horizon, with
  correlations at the 10⁻⁵ level [src: Hu & Dodelson 2001, arXiv:astro-ph/0110414, Sect. 3.2].
- **Temperature from a time shift.** The Newtonian potential is a time
  shift δt/t = Ψ, so Θ = −δa/a = −(2/3)(1 + p/ρ)⁻¹ δt/t: −Ψ/2 in radiation
  domination and −2Ψ/3 in matter domination [src: Sect. 3.2, Eq. 13].
- **Observed temperature.** After recombination photons climb out of the
  potential, so the observed fluctuation is the effective temperature
  Θ + Ψ. Its large-scale limit is the Sachs–Wolfe result Ψ/3: overdense
  regions are cold spots [src: Sect. 3.3, Eq. 15]. Modes larger than the
  sound horizon at recombination (ks ≪ 1) are frozen at their initial
  values, which is why the COBE-scale anisotropies measure the initial
  conditions directly [src: Sect. 3.1].
- **Phase coherence as a test.** Causal mechanisms that create curvature
  only inside the horizon add a phase φ(k) to the oscillation, which can
  wash out the peaks (defect models) or shift them (many isocurvature
  models). Independently of D*, the peak-position ratios
  ℓ₁ : ℓ₂ : ℓ₃ ~ 1 : 2 : 3 measure the phase (φ = 0), and the peak spacing
  ℓ_n − ℓ_(n−1) = ℓ_A measures the angular-diameter distance. The observed
  coherent peaks with φ = 0 are a non-trivial test of the inflationary
  paradigm [src: Sect. 3.2]. Current limits on isocurvature and on the
  primordial spectrum are in `cosmo-inflation-primordial`.

## 3. Acoustic oscillations
<!-- key: acoustic-oscillations -->

The photon–baryon fluid before recombination obeys, in Fourier space and
conformal time, a forced oscillator. The steps below follow Hu & Dodelson
2001 (arXiv:astro-ph/0110414); the original analytic treatment is Hu &
Sugiyama 1994 and 1995 (arXiv:astro-ph/9407093, arXiv:astro-ph/9510117).

| Ingredient | Equation as written | Consequence | Place read |
|---|---|---|---|
| Ideal fluid | Θ̈ + c_s²k²Θ = 0, c_s = 1/√3 | Θ(η*) = Θ(0) cos(ks*), s = ∫c_s dη the sound horizon; peaks at k_n = nπ/s* | Sect. 3.1, Eqs. 9–10 |
| Projection | ℓ_n ≈ n ℓ_a, ℓ_a ≡ π D*/s* | in a flat matter-dominated model η*/η₀ ≈ 1/30, ℓ₁ ≈ 200 | Sect. 3.1, Eq. 11 |
| Gravity | Θ̈ + c_s²k²Θ = −(k²/3)Ψ − Φ̈ | Θ + Ψ oscillates about zero; oscillations arise from infall even if Θ(0) = 0 | Sect. 3.3, Eq. 14 |
| Baryon loading | R = (p_b + ρ_b)/(p_γ + ρ_γ) ≈ 30 Ω_b h² (z/10³)⁻¹; c_s = 1/√(3(1+R)) | zero point shifts to Θ = −(1+R)Ψ, amplitude grows; odd (compressional) peaks enhanced; amplitude decays as (1+R)^(−1/4) | Sect. 3.4, Eqs. 16–17 |
| Radiation driving | ρ_m/ρ_r ≈ 24 Ω_m h² (z/10³)⁻¹ | potentials decay in radiation domination and drive the oscillation; amplitude rises by a factor 4–5 across k_eq | Sect. 3.5 |
| Diffusion damping | damping factor of order e^(−k²η/τ̇); k_d ~ √(τ̇/η) | k_d s* ≈ 10: strong suppression beyond the third peak | Sect. 3.6, Eq. 20 |

Points to hold:

- **Peaks are compressions and rarefactions, not "Doppler peaks".** The
  first peak is the mode caught in its first compression at recombination,
  the second the mode that completed one compression and rarefaction
  [src: Sect. 3.3]. The fluid velocity is of the same order as the effective
  temperature but out of phase; its Doppler contribution projects through
  j′_ℓ, which has no strong peak at kD* = ℓ, so it cannot produce strong
  peaks [src: Sect. 3.8].
- **Baryons alternate the peak heights.** Since the observed temperature is
  still Θ + Ψ, the zero-point shift enhances only the compressional phase:
  the first, third, fifth peaks in the working model [src: Sect. 3.4].
- **Radiation driving erases the alternation.** By eliminating the
  potentials, radiation driving also removes the odd–even modulation; a high
  third peak therefore indicates that cold dark matter exists and dominates
  the energy density at recombination [src: Sect. 3.5]. Any radiation whose
  density perturbations stop growing near horizon crossing contributes to
  the driving [src: Sect. 3.5]; the light-relic signatures (damping and
  phase shift) are in `deep/damping-tail-light-relics.md`.
- **Damping physics** (arXiv:astro-ph/0110414). Shear viscosity (photon quadrupole, coefficient
  A_v = 16/15) and heat conduction (A_h = R²/(1+R)) add a damping term; the
  damping length is the geometric mean of horizon and mean free path, the
  random walk of photons from hot to cold regions (Silk damping)
  [src: Sect. 3.6, Eq. 20]. More matter means more damping at fixed ℓ but
  slightly less at fixed peak number; under the Saha approximation the
  damping length scales roughly as (Ω_b h²)^(−1/4) [src: Sect. 3.6].
- **Recombination must be integrated numerically.** The mean free path
  grows rapidly through recombination, so damping and polarisation require
  numerical integration [src: Sect. 3.6–3.7]. The recombination codes used
  by current Boltzmann solvers are listed in `physics-and-methods.md` §9.

## 4. Polarisation generation
<!-- key: polarisation-generation -->

- **Only a quadrupole polarises.** Thomson scattering of an isotropic
  incident field leaves the outgoing radiation unpolarised; only a
  quadrupole anisotropy of the incident radiation produces net linear
  polarisation [src: Hu & Dodelson 2001, Sect. 3.7].
- **The "Catch-22".** The quadrupole is generated by photon motion only
  where the Universe is optically thin across the scale, and scattering
  that polarises also suppresses its quadrupole source; the quadrupole is
  of order k v_γ/τ̇, so polarisation is smaller than temperature by a factor
  of order k/τ̇ at recombination. The polarised fraction rises with ℓ to a
  maximum of about ten per cent before damping removes the dipole source
  [src: Sect. 3.7].
- **Phases.** Because v_γ is π/2 out of phase with the monopole, the EE
  peaks are out of phase with the TT peaks, and C_ℓ^ΘE oscillates at twice
  the acoustic frequency [src: Sect. 3.7].
- **E only from scalars.** In linear theory a scalar mode has one direction,
  k, and so produces only E. The acoustic polarisation peaks are therefore
  in EE alone, which separates them cleanly from gravitational waves and
  lensing, and they are a prediction of the temperature peaks that tests the
  initial conditions and the ionisation history [src: Sect. 3.7].
- The all-sky E/B formalisms are Zaldarriaga & Seljak 1996
  (arXiv:astro-ph/9609170) and Kamionkowski et al. 1996
  (arXiv:astro-ph/9611125); see `physics-and-methods.md` §1. B modes from
  tensors and their status belong to `cosmo-inflation-primordial`.

## 5. Projection: the line-of-sight source
<!-- key: projection-line-of-sight -->

Hu & Dodelson write the projected source for each multipole as
[src: Sect. 3.8, Eq. 22]

    a_ℓ(k) = [Θ + Ψ](η*) j_ℓ(kD*) + v_b(k, η*) j′_ℓ(kD*)
             + ∫_η*^η₀ dη (Ψ̇ − Φ̇) j_ℓ(kD),

and C_ℓ = (2/π) ∫ (dk/k) k³ a_ℓ²(k) [src: Eq. 23]. The three terms are the
effective temperature (Sachs–Wolfe plus acoustic), the Doppler term, and the
integrated Sachs–Wolfe (ISW) term.

- **j_ℓ peaks at kD* ≈ ℓ**, so the k–ℓ mapping is only approximate: a plane
  wave contributes to a range of ℓ [src: Sect. 3.8].
- **Early ISW.** Residual radiation after decoupling makes the potentials
  decay just after recombination. Because this happens quickly, the term
  adds in phase with the monopole; it lowers ℓ₁ as the matter-to-radiation
  ratio at recombination decreases [src: Sect. 3.8].
- **Late ISW.** Potential decay at the onset of dark-energy or curvature
  domination lasts about a Hubble time, so photons cross many crests and
  troughs and only modes with k ⊥ n̂ survive; the effect is suppressed by a
  factor of order ℓ and appears only at the lowest multipoles, where cosmic
  variance limits its detection [src: Sect. 4.2.1]. Its detection through
  correlation with tracers belongs to `cosmo-cmb-lss-cross-correlations`.
- **Codes.** The line-of-sight integration (a geometric term times a source
  term) is the basis of CMBFAST (Seljak & Zaldarriaga 1996,
  arXiv:astro-ph/9603033) and its successors; in curved geometry j_ℓ is
  replaced by ultraspherical Bessel functions [src: Hu & Dodelson 2001,
  Sect. 3.8].

## 6. Reionisation in the primary spectra
<!-- key: reionisation-primary -->

- **Peak suppression.** Rescattering after reionisation suppresses the
  acoustic peaks by the fraction of photons rescattered, approximately the
  optical depth; scales near the horizon at reionisation are not suppressed.
  Except at the lowest, cosmic-variance-limited multipoles the effect mimics
  a change of normalisation [src: Hu & Dodelson 2001, Sect. 4.3.1]. This is
  the origin of the A_s e^(−2τ) degeneracy in `physics-and-methods.md` §2.
- **Large-angle E bump.** Rescattered radiation is polarised by the
  quadrupole present at the horizon scale at reionisation, producing a bump
  in EE at ℓ ~ few with amplitude of order tenths of μK; cancellation along
  the line of sight suppresses it sharply at higher ℓ in linear theory
  [src: Sect. 4.3.2]. Its position scales with the square root of the
  reionisation redshift and its amplitude is proportional to τ (Zaldarriaga
  1996, arXiv:astro-ph/9608050) [src].
- **Doppler from reionisation** is strongly suppressed by the same
  cancellation and negligible below ℓ ~ 10² unless the optical depth
  approaches unity [src: Hu & Dodelson 2001, arXiv:astro-ph/0110414, Sect. 4.3.3].
- Measurement of τ: `deep/low-ell-polarisation-tau.md`; reionisation
  history: `cosmo-reionization-21cm`; patchy kSZ:
  `cosmo-cmb-lss-cross-correlations`.

## 7. Parameter sensitivity of the peaks
<!-- key: parameter-sensitivity -->

Hu & Dodelson reduce the acoustic phenomenology to four observables plus
the initial conditions [src: Sect. 3.9]: the angular sound horizon
ℓ_a ≡ πD*/s*, the angular scale of the horizon at equality
ℓ_eq ≡ k_eq D*, the angular damping scale ℓ_d ≡ k_d D*, and the
baryon–photon momentum ratio R*. ℓ_a sets the spacing, ℓ_eq and ℓ_d compete
for the amplitudes (radiation driving against damping), R* with ℓ_eq sets
the odd–even modulation, and the initial conditions set the phase and the
tilt.

Their linear response, for the 2001 working model (Ω_tot = 1,
Ω_Λ = 2/3, Ω_b h² = 0.02, Ω_m h² = 0.16, n = 1), as written in arXiv:astro-ph/0110414 [src: Eq. 24]:

| Observable | Ω_m h² | Ω_b h² | Ω_Λ | Ω_tot |
|---|---|---|---|---|
| Δℓ_a/ℓ_a | −0.24 | +0.07 | −0.17 | −1.1 |
| Δℓ_eq/ℓ_eq | +0.5 | — | −0.17 | −1.1 |
| Δℓ_d/ℓ_d | −0.21 | +0.20 | −0.17 | −1.1 |
| ΔR*/R* | — | 1.0 | — | — |

Coefficients multiply fractional changes of each parameter. In that model
ℓ_a = 301, ℓ₁ = 0.73 ℓ_a, ℓ_eq = 149, ℓ_d = 1332, R* = 0.57 (arXiv:astro-ph/0110414) [src: Sect. 3.9];
the 2001 data values quoted beside them are superseded and not repeated.

What follows from it [src: Sect. 3.9]:

- **No single scale is a standard ruler** even in the working model: ℓ_a
  depends strongly on Ω_m h² (hence on H₀). Measuring ℓ_eq breaks that
  dependence, and R* breaks the weaker baryon dependence; ℓ_d is a
  consistency check of recombination and of the energy content at that
  epoch.
- **Geometric degeneracy.** Ω_tot and Ω_Λ enter only through D*, which
  leaves a weak but perfect angular-diameter-distance degeneracy; dark
  energy cannot be isolated from the peaks alone, and the CMB evidence for
  it needs external information. The current treatment, with lensing and
  BAO breaking the degeneracy, is in `physics-and-methods.md` §2.
- **What the peaks fix.** Precise peaks determine Ω_b h², Ω_m h², D* and n;
  more generally ℓ_a, ℓ_eq, ℓ_d and R*, which extends the result to models
  that break the working-model assumptions.
- **Curvature.** D = R sin(d/R) in a closed universe (sinh for open): a
  given comoving scale at fixed distance subtends a larger angle in a closed
  universe than in a flat one, so the acoustic peaks move to lower ℓ; in a
  flat dark-energy model the shift of ℓ₁ is small next to that of curvature
  [src: Sect. 3.1, Eq. 12 and Fig. 2].

## 8. The spectra read with Planck
<!-- key: spectra-read-with-planck -->

Planck 2018 I (Planck Collaboration 2018, arXiv:1807.06205) restates the
same physics for the measured spectra [src: Sect. 3.2]:

- **Three regions of TT.** Above the Hubble scale at last scattering
  (low ℓ) a nearly scale-invariant plateau that images the initial
  conditions; at degree scales the near-harmonic series of peaks of the
  oscillating baryon–photon fluid; below the geometric mean of Hubble scale
  and mean free path, erasure by photon diffusion. The diffusion scale is
  the mean free path times the square root of the number of scatterings.
  Polarisation shows the same behaviour without the low-ℓ plateau and with
  sharper peaks, sourced mainly by the quadrupole at last scattering.
- **θ* from the extrema.** θ* is set by the positions of peaks and troughs,
  not their amplitudes, so it is stable and weakly model dependent; θ*
  from TT matches θ* from EE and TE, which limits the non-adiabatic fraction
  of the perturbations. r* = ∫c_s dt = ∫dη/√(3(1 + 3ρ_b/4ρ_γ)).
- **The Ω_m–h degeneracy and how it is broken.** With ω_b fixed to better
  than 1% by the relative peak heights, θ* constrains
  Ω_m h³ = 0.09633 ± 0.00029 (68%, Planck 2018; arXiv:1807.06205) [src:
  Sect. 3.2, Eq. 6]. The orthogonal
  direction is fixed by Ω_m h² through the damping scale and through the
  share of the potentials set by cold dark matter rather than by the
  baryon–photon fluid, which changes the relative peak heights.
- **Tilt.** With the amplitude fixed at k₀ = 0.05 Mpc⁻¹, which projects
  near ℓ = 500, raising n_s adds power at ℓ > 500 and removes it below; over
  three decades in wavenumber Planck finds n_s ≠ 1 at more than 8σ
  (arXiv:1807.06205) [src: Sect. 3.2].
- **Reionisation.** Scattering suppresses power below the Hubble scale at
  reionisation (ℓ > 10) by e^(−2τ) and generates large-angle polarisation
  with C_ℓ^EE ∝ τ²; Planck limits the reionisation redshift to < 9 (95%)
  (arXiv:1807.06205) [src: Sect. 3.2].
- **Lensing** changes the primordial spectra slightly, invisibly by eye but
  included in the model; its treatment is in `physics-and-methods.md` §3.

The TT, TE and EE spectra are mutually consistent within ΛCDM: any pair
predicts the third within the conditional errors, notably at low and
intermediate ℓ where Planck is cosmic-variance limited [src: Sect. 4.1,
Fig. 17]. That the sky is linearly polarised follows from the anisotropies
and Thomson scattering, and Planck 2018 I points to Hu & White 1997 for a
pedagogical review [src: Sect. 4.1]. That primer explains how the
polarisation pattern is read off the quadrupole moments, which correspond
to the scalar (compressional), vector (vortical) and tensor (gravitational
wave) modes, and the E/B parity distinction [src] (Hu & White 1997,
arXiv:astro-ph/9706147).

## 9. Which assumptions the primary spectra test
<!-- key: assumptions-tested -->

Planck 2018 I lists eight assumptions of ΛCDM (A1–A8: universality of
physics, GR, statistical homogeneity, a hot dense past, five constituents,
small curvature, Gaussian adiabatic nearly scale-invariant initial
fluctuations, trivial topology) and states which the CMB tests
(arXiv:1807.06205) [src: Sects. 3.1 and 3.3]:

| Assumption | CMB evidence as stated | Place |
|---|---|---|
| Same physics everywhere | ω_b from acoustic physics before 400 000 yr agrees with ω_b from BBN in the first three minutes | Sect. 3.3, Fig. 16 |
| GR at last scattering | η_slip = 1.004 ± 0.007 (68%) for a scale-independent ratio of the two metric potentials, Planck alone | Sect. 3.3, Eq. 7 |
| Hot dense past | blackbody spectrum; acoustic wiggles require an ionised plasma dense enough to oscillate without excessive dissipation | Sect. 3.3 |
| Primordial, adiabatic, superhorizon fluctuations | regular peaks and the relative phases of T and E imply "primordial" and "apparently acausal" perturbations, all in the growing mode by z ≃ 1100, with no evidence of active sources (strings, textures) | Sect. 3.3 |
| Trivial topology | no cubic toroidal or slab topology detected, with a scale below the diameter of the last-scattering surface | Sect. 3.3 |

The base model fixes the radiation content to photons at T = 2.7260 K and
neutrinos with N_eff = 3.046 and a single massive eigenstate of 0.06 eV,
with Y_P from standard BBN (arXiv:1807.06205) [src: Sect. 3.2]; extensions that free these are
in `physics-and-methods.md` §7.
Given the assumptions, the high-redshift ionisation history is computed to
high accuracy, so only the constituents and the low-redshift ionisation
history need to be specified; the small amplitude of the fluctuations makes
the calculation linear perturbation theory in a Boltzmann code
[src: Planck 2018 I, Sect. 3.1].

## 10. What the primary spectra do not constrain
<!-- key: what-spectra-do-not-constrain -->

- **A_s and τ separately** at ℓ > 10: only A_s e^(−2τ) is measured there;
  τ needs the large-angle E bump (§6; Planck 2018 I, arXiv:1807.06205,
  Sect. 3.2).
- **Curvature and dark energy from the unlensed peaks**: the geometric
  degeneracy (§7). WMAP alone could not break it, and parameters moved to
  the Planck-preferred values once BAO were added [src: Planck 2018 I,
  Sect. 4.1]. Lensing and BAO break it (`physics-and-methods.md` §2).
- **The intrinsic dipole.** A cosmological dipole of order 10⁻⁵ is expected
  but unobservable beneath the kinematic one [src: Planck 2018 I,
  Sect. 5.1]. Of the four second-order effects of our motion
  (frequency-dependent quadrupole, dipolar modulation, monopole shift,
  aberration), the first two do not depend on the origin of the dipole, the
  third is unobservable, and aberration is degenerate with an L = 1 lensing
  mode; the boost interpretation is compelling but not definitive
  [src: Sect. 5.1]. Aberration with an asymmetric Galactic mask biases θ* by
  less than 0.1σ in Planck [src: Sect. 5.1] (Jeong et al. 2013,
  arXiv:1309.2285).
- **Many parameters at once, from few directions.** For adiabatic CDM
  models with power-law scalar and tensor spectra, most of the variance of
  the parameter estimates sits in two or three principal components; an
  exact likelihood shows that the Fisher-matrix approach can significantly
  overestimate the errors; and small correlated errors in the spectrum
  below cosmic variance (foregrounds, scanning) can bias the parameters
  significantly [src] (Efstathiou & Bond 1998, arXiv:astro-ph/9807103).
- **Late-time physics at low ℓ**: the late ISW is confined to the lowest
  multipoles and cosmic-variance limited (§5); the large-angle anomalies are
  in `cosmo-tensions-anomalies`.
- **The lowest multipoles drive parameters when the lever arm is short.**
  With ℓ < 800 only, the deficit of power at ℓ ≲ 30 raises n_s, lowers
  A_s e^(−2τ) and ω_m, raises ω_b and pulls H₀ higher at fixed acoustic
  scale; this is how Planck Int. LI explained part of the WMAP–Planck
  parameter difference [src: Planck 2018 I, Sect. 4.1] (Planck
  Collaboration 2016, arXiv:1608.02487).

## Not verified
<!-- key: not-verified -->

- The modern (Planck-era) numerical values of ℓ_a, ℓ_eq, ℓ_d and R* were not
  read in a current paper; the coefficients of the table above are those of
  a 2001 model and should be recomputed before use [der: they are linear
  responses about a different fiducial].
