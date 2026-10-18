# CMB spectral distortions: from energy release to a μ or y limit — cosmo-early-universe-exotica dossier

Scope: how an energy-release history is turned into μ, y and temperature
shift (visibility functions, Green's function), how the FIRAS monopole
limits and the 2022 pixel-level μ map were derived from the data (sky
model, Galactic templates, covariance, masks), how a foreground-marginalised
forecast for a PIXIE-class spectrometer is built, and which choices move
each result.
Snapshot: 2026-10-18.
From: Chluba et al. Voyage 2050 white paper; COBE/FIRAS and its
reanalyses; PIXIE-type and balloon proposals.

Already in L2, not repeated here: the FIRAS, reanalysis and ΛCDM numbers
and the f_NL limit in `results.md#spectral-distortions`; the instruments
and forecast sensitivities in `surveys-and-data.md#absolute-spectrum-cmb-instruments`;
calibration, foregrounds and imager-versus-spectrometer remarks in
`systematics.md#spectral-distortion-measurements`; the physics summary and
CosmoTherm in `physics-and-methods.md#cmb-spectral-distortions`; what a
next instrument decides in
`open-questions.md#spectral-distortions-what-a-next-generation`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. From energy release to distortion parameters
<!-- key: step-1-from-energy-release-to-distortion -->

Notation of Chluba 2025 (arXiv:2502.05188): Q is the heat released,
ρ_γ the photon energy density, x = hν/k_B T₀ = 1.76 [ν/100 GHz]. Any
release first makes a y-type distortion; Compton scattering converts it to
μ if it happens early enough; double Compton (DC) and bremsstrahlung
photon production then thermalise it [src: Sect. 4.5]. At leading order
(Eq. 28) [src]:

- y ≈ ¼ ∫₀^{z_μy} d(Q/ρ_γ)/dz′ dz′,
- μ ≈ 1.401 ∫_{z_μy}^∞ d(Q/ρ_γ)/dz′ J_μ(z′) dz′,
- ΔT/T ≈ ¼ ∫_{z_μy}^∞ d(Q/ρ_γ)/dz′ [1 − J_μ(z′)] dz′,

with z_μy = 5 × 10⁴ the μ–y transition and the distortion visibility
J_μ(z) ≈ e^(−(z/z_μ)^2.5) [src: Sect. 4.5]. The thermalisation redshift is
z_μ = 1.98 × 10⁶ [(1 − Y_p/2)/0.88]^(−2/5) [Ω_b h²/0.022]^(−2/5)
(Chluba & Sunyaev 2012, arXiv:1109.6552, Eq. 38), set by DC; with
bremsstrahlung alone it would be much higher (z_br ≈ 5.27 × 10⁶ in the
2025 review, ~6.2 × 10⁶ in the 2012 paper's footnote), and visibility would
fall more slowly [src: arXiv:2502.05188, Sect. 4.4; arXiv:1109.6552,
Sect. 3.6.1].

Beyond leading order the μ–y transition is gradual and leaves a residual
(non-μ, non-y) distortion carrying the time dependence of the release. The
full answer is the thermalisation Green's function G_th(ν, z_h), computed
once with CosmoTherm by injecting energy at each redshift and evolving to
z = 0, then tabulated: pure y for z_h ≲ 10⁴, pure μ near 3 × 10⁵, a
temperature shift with a residual μ for z_h ≳ few × 10⁶ [src:
arXiv:2502.05188, Sect. 4.6, Fig. 4]. A newer basis of 17 distortion
parameters reproduces it almost exactly without pre-computed tables (as
cited there, Chluba et al. 2023a) [src: same].

### Step 2. From a limit on μ or y to a limit on energy release
<!-- key: step-2-from-a-limit-on-mu-or-y-to-a-limit-on -->

The FIRAS paper uses ΔU/U = 0.71 μ (μ era) and ΔU/U = 4y (after it, before
decoupling) (Fixsen et al. 1996, arXiv:astro-ph/9605054, Sect. 7) [src];
the 2025 review uses Δρ_γ/ρ_γ = μ/1.401 and 4y, which with the FIRAS
limits gives |Δρ_γ/ρ_γ| ≲ 6 × 10⁻⁵ (95%) for release at z ≲ 2 × 10⁶
[src: arXiv:2502.05188, Sect. 4.5 and footnote 15]. The 0.71 and 1/1.401
are the same coefficient [der: 1/1.401 = 0.714].

For a decaying particle of lifetime corresponding to z_X, the visibility-
weighted release is Eq. 39–41 of arXiv:1109.6552: an efficiency integral
J̄(λ_X), λ_X = (1 + z_X)/(1 + z_μ), multiplies the energy release [src:
Sect. 3.6.1]. The older Hu & Silk estimate, which deposits all the energy
at t_X, gives J̄ ≈ e^(−λ_X^(5/2)) and strongly underestimates J̄ for
z_X > z_μ; FIRAS limits on particles with t_X ≲ 6 × 10⁶ s are therefore
"significantly stronger" than that estimate implied [src: same].

### Step 3. The FIRAS monopole fit (1996)
<!-- key: step-3-the-firas-monopole-fit-1996 -->

**Instrument and calibration.** FIRAS is a polarising Michelson
interferometer measuring the difference between a 7° sky patch and an
internal reference blackbody, operated nearly nulled to reduce gain and
drift sensitivity [src: arXiv:astro-ph/9605054, Sect. 2]. Absolute
calibration comes from an external blackbody that fills the sky aperture,
with emissivity > 0.99997 and isothermal to < 1 mK, giving a spectrum
uncertainty of about 10 ppm from the calibrator [src: same]. Each of eight
channels (4 detectors × 2 scan speeds) has a calibration model of about
3000 parameters [src: Sect. 3.4]. The low-frequency spectrum keeps 43
significant elements over 2–21 cm⁻¹ [src: same].

**Fit.** The monopole is fitted linearly,
I₀(ν) = B_ν(T₀) + ΔT ∂B_ν/∂T + G₀ g(ν) + p ∂S_c/∂p (Eq. 3), where g(ν) is
the Galactic residual spectrum with amplitude G₀ and p is either μ or y
[src: Sect. 6]. The distortion shapes are
∂S_μ/∂μ = −(T₀/x) ∂B_ν/∂T (Eq. 5) and
∂S_y/∂y = T₀ [x coth(x/2) − 4] ∂B_ν/∂T (Eq. 7) [src: Sects. 6.2–6.3].
μ and y are "too similar to fit simultaneously"; each is fitted alone
[src: Sect. 6].

**Galactic model.** Either the template g(ν) derived from the all-sky data
or ν²B_ν(T) with free temperature; the latter gives lower χ² at 9 K and is
used for the final table. The authors warn that a 9 K component could be a
Galactic halo, a uniform background with a Galactic-like spectrum, or
variations of dust temperature or emissivity [src: Sect. 6.1]. The
latitude cut is varied to test the Galactic model: changes larger than the
statistical error flag an inadequate model [src: same].

**Results.** With p = 0, the weighted rms residual is 50 ppm of the peak
and χ²/dof = 46/40 [src: Sect. 6.1]. μ = (−1 ± 4) × 10⁻⁵ gives |μ| <
9 × 10⁻⁵ (95%); y = (−1 ± 6) × 10⁻⁶ with an added systematic of 4 × 10⁻⁶
for Galactic-cut and model dependence gives |y| < 15 × 10⁻⁶ (95%) [src:
Sects. 6.2–6.3]. y is more strongly coupled to the Galactic residual than μ
[src: Sect. 6.3].

### Step 4. The pixel-level μ map (2022)
<!-- key: step-4-the-pixel-level-mu-map-2022 -->

Bianchini & Fabbian 2022 (arXiv:2206.02762) refit the FIRAS low-frequency
sky spectra pixel by pixel.

- **Sky model.** I_ν(n̂) = B_ν(T₀) + ΔT(n̂) ∂B_ν/∂T + I_ν^FG + I_ν^SD (Eq. 1),
  T₀ = 2.7255 K; μ enters non-linearly through B_ν(T₀, μ) =
  (2hν³/c²)/(e^(x+μ) − 1) (Eq. 2) [src: Sect. III.1]. The authors' reason:
  in the linearised form (Eq. 3) μ and ΔT both multiply ∂B_ν/∂T and are
  correlated at over 95% according to Fixsen et al.; the non-linear fit
  reduces that degeneracy [src: Sect. III.1, Fig. 3]. y has the shape of
  Eq. 4, with a zero crossing at ≈ 218 GHz against ≈ 125 GHz for μ [src:
  same].
- **Foregrounds** [src: Sect. III.2]: thermal dust as a modified blackbody
  at 353 GHz with T_d = 19.6 K and β_d = 1.6 (Eq. 5); synchrotron power law
  β_s = −3.1 at 23 GHz (Eq. 6); free-free from the Planck Commander
  emission-measure and electron-temperature templates with a Gaunt factor
  (Eqs. 7–9); and the empirical FIRAS Galactic residual. Baseline "A_d +
  β_d": dust amplitude and index free in each pixel (four free parameters
  per pixel with ΔT and μ). CIB and molecular lines are not modelled;
  frequencies above 600 GHz are dropped because the CIB grows there, and
  the free dust index is argued to absorb part of the CIB (through the
  T_d–β_d correlation) and of the CO lines (degenerate with β_d)
  [src: same].
- **Covariance.** Six FIRAS error terms — detector noise (C), bolometer gain
  (JCJ), emissivity gain (PEP), internal-calibrator temperature (PUP,
  U = 180 μK), absolute temperature (PTP, T = 2 mK) and destriper errors
  (β, including map offsets) — assembled in Eqs. 10–12, plus a 0.04² term;
  pixels are treated as uncorrelated, keeping the full frequency–frequency
  structure [src: Sects. III.3–III.4].
- **Inference.** −2 ln L = Δᵀ C⁻¹ Δ per pixel (Eq. 13), emcee with 100
  walkers × 1000 steps, flat priors except β_d ∈ [0, 3]; output a μ map at
  HEALPix N_side = 16 with per-pixel errors [src: Sect. III.4].
- **Monopole.** Inverse-covariance-weighted average of the map over the
  mask; the improved foreground model allows 97% of the sky (FDS mask)
  against 90% (|b| > 5°) in Fixsen et al. [src: Sect. IV.1]. Fiducial mask:
  |⟨μ⟩| ≲ 47 × 10⁻⁶ (95%), ⟨μ⟩ = (−18.2 ± 14.3) × 10⁻⁶ [src: Table 1].
  With the FIRAS foreground model and a similar sky fraction they recover
  ⟨μ⟩ ≲ 90 × 10⁻⁶, consistent with 1996 [src: Sect. IV.1].

### Step 5. A foreground-marginalised forecast
<!-- key: step-5-a-foreground-marginalised-forecast -->

Abitbol et al. 2017 (arXiv:1705.01534) set the template used for
PIXIE-class forecasts [src: Sects. 4–5]:

- **Sky model.** CMB parameters (blackbody shift, y, relativistic tSZ
  temperature kT_eSZ, μ) plus six foregrounds with 12 free parameters:
  thermal dust and CIB as two modified blackbodies (6 parameters),
  synchrotron as a power law with logarithmic curvature (3), free-free (1),
  integrated CO template (1), spinning dust (1). SEDs are taken from Planck
  fluctuation measurements and assumed to describe the monopole [src:
  Sect. 4].
- **Why curvature in synchrotron.** Averaging power laws with different
  indices along the line of sight and in the beam generates curvature, which
  cannot be avoided at PIXIE sensitivity [src: Sect. 4].
- **External information.** A 10% prior on synchrotron amplitude and index,
  standing for Haslam, WMAP, Planck, C-BASS, QUIJOTE or future data [src:
  Sect. 4].
- **Statistics.** Fisher matrix F_ij = Σ ∂ΔI_a/∂p_i C⁻¹_ab ∂ΔI_b/∂p_j
  (Eq. 6) with diagonal noise, and emcee MCMC (≈ 200 walkers) to capture
  non-Gaussian posteriors near threshold and biases from incomplete
  modelling; A_sync > 0 imposed [src: Sect. 5].
- **Results (forecast).** Extended PIXIE detects the average non-relativistic
  and relativistic tSZ at 194σ and 11σ; the ΛCDM μ is not detected;
  |μ| < 3.6 × 10⁻⁷ (95%) with moderate synchrotron information, 9.4 × 10⁻⁸
  with optimistic low-frequency information [src: abstract].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Linear or non-linear μ, and μ with y
<!-- key: linear-or-non-linear-mu-and-mu-with-y -->

The linear template makes μ and ΔT nearly degenerate (> 95%); the
non-linear B_ν(T₀, μ) reduces it [src: arXiv:2206.02762, Sect. III.1].
Fitting μ and y together is not informative with FIRAS: Fixsen et al.
could not do it [src: arXiv:astro-ph/9605054, Sect. 6], and the 2022 fit
finds them anticorrelated by more than 80% on average, with no shift in the
μ × T cross-spectrum [src: arXiv:2206.02762, Sect. IV.3.2]. Quoting a μ
limit obtained with y fixed to zero, and vice versa, is the standard and
should be stated.

### Foreground model and mask
<!-- key: foreground-model-and-mask -->

The 2022 monopole limit depends on the model and on the Galactic mask
(PL90 to PL40) [src: arXiv:2206.02762, Table 1]:

| Model | PL90 | PL80 | PL60 | PL40 |
|---|---|---|---|---|
| A_d + β_d (baseline) | < 47 | < 51 | < 47 | < 53 |
| A_d, fixed β_d | < 74 | < 50 | < 105 | < 179 |

Values are 95% upper limits on |⟨μ⟩| in units of 10⁻⁶ (see "Not verified"
for the unit printed in the table header). With a free dust index the limit
is stable across masks; with the index fixed it degrades on smaller masks.
Fixsen et al. also preferred the ν²B_ν(T) model over the empirical
template on χ² grounds [src: arXiv:astro-ph/9605054, Sect. 6.1].

### Spectrometer or imager
<!-- key: spectrometer-or-imager -->

Planck maps have far lower noise but no absolute zero level: map offsets
are set by HI correlation (LFI) or fixed to a CIB monopole model (HFI), and
FIRAS-based CIB monopoles disagree with the model at 217 and 353 GHz; a
toy model shows that these offset uncertainties inflate the μ error [src:
arXiv:2206.02762, Sect. VI.3]. The earlier Planck μ map (Khatri & Sunyaev,
as cited) is about 60%, 40% and 30% correlated with dust, tSZ and CIB
templates and dominated by CMB leakage, partly because its model has no y
[src: Sect. VI.2]. The authors conclude that Planck-based analyses give
"similar or worse" results once these are included [src: abstract].

### Analytic or numerical visibility
<!-- key: analytic-or-numerical-visibility -->

The leading-order formulas (Step 1) capture the main features; the
Green's function adds the transition-era information [src:
arXiv:2502.05188, Sects. 4.5–4.6]. For decaying particles, the Hu & Silk
visibility underestimates the distortion above z_μ [src: arXiv:1109.6552,
Sect. 3.6.1]. Use tabulated G_th for any limit near z ≈ z_μ or in the μ–y
transition.

### Forecast assumptions
<!-- key: forecast-assumptions -->

Varying foreground amplitudes by up to a factor 5 barely changes the
forecast; spectral indices and temperatures can move by ≈ 20% without
spoiling it [src: arXiv:1705.01534, Sect. 7.1]. Dropping synchrotron
curvature improves the μ significance by about a factor 2, and removing the
CIB improves all CMB parameters by about 5, both judged unrealistic by the
authors [src: same]. Spinning dust costs < 20% with the synchrotron prior
and less than a factor 2 without it [src: same]. Low-frequency
(ν ≲ 15–30 GHz) synchrotron information at the 1% level is the main lever
for μ [src: Sect. 4]. The forecast assumes sky-averaged SEDs; averaging
spatially varying SEDs does not give the same SED, which a moment
expansion would handle [src: Sect. 4].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| μ coefficient | μ ≈ 1.401 Δρ_γ/ρ_γ (ΔU/U = 0.71 μ) | theory; FIRAS | arXiv:2502.05188; arXiv:astro-ph/9605054 | Eq. 28; Sect. 7 |
| y coefficient | y ≈ ¼ Δρ_γ/ρ_γ | theory | arXiv:2502.05188 | Eq. 28 |
| μ–y transition | z_μy = 5 × 10⁴ | theory | arXiv:2502.05188 | Sect. 4.5 |
| Thermalisation redshift | z_μ = 1.98 × 10⁶ (Y_p, Ω_b h² scaling) | theory | arXiv:1109.6552 | Eq. 38 |
| Energy-release limit | |Δρ_γ/ρ_γ| ≲ 6 × 10⁻⁵ (95%), z ≲ 2 × 10⁶ | FIRAS | arXiv:2502.05188 | Sect. 4.5 |
| Calibrator emissivity | > 0.99997; ~10 ppm spectrum error | FIRAS | arXiv:astro-ph/9605054 | Sect. 2 |
| Spectral elements | 43 over 2–21 cm⁻¹ | FIRAS | arXiv:astro-ph/9605054 | Sect. 3.4 |
| Residual rms | 50 ppm of peak; χ²/dof = 46/40 | FIRAS | arXiv:astro-ph/9605054 | Sect. 6.1 |
| μ fit | (−1 ± 4) × 10⁻⁵ | FIRAS | arXiv:astro-ph/9605054 | Sect. 6.2 |
| y fit | (−1 ± 6) × 10⁻⁶ + 4 × 10⁻⁶ systematic | FIRAS | arXiv:astro-ph/9605054 | Sect. 6.3 |
| Dust model | T_d = 19.6 K, β_d = 1.6 at 353 GHz; β_d ∈ [0, 3] when free | FIRAS reanalysis | arXiv:2206.02762 | Sects. III.2, III.4 |
| Calibration errors | U = 180 μK; T = 2 mK | FIRAS reanalysis | arXiv:2206.02762 | Sect. III.3 |
| Map resolution | N_side = 16 | FIRAS reanalysis | arXiv:2206.02762 | Sect. III.4 |
| Sky fraction | 97% (FDS mask) vs 90% (F96) | FIRAS reanalysis | arXiv:2206.02762 | Sect. IV.1 |
| μ monopole (fiducial mask) | (−18.2 ± 14.3) × 10⁻⁶; < 47 × 10⁻⁶ (95%) | FIRAS reanalysis | arXiv:2206.02762 | Table 1 |
| μ–y anticorrelation | > 80% | FIRAS reanalysis | arXiv:2206.02762 | Sect. IV.3.2 |
| Foreground parameters | 12 | PIXIE forecast | arXiv:1705.01534 | Sect. 4 |
| Synchrotron prior | 10% on amplitude and index | PIXIE forecast | arXiv:1705.01534 | Sect. 4 |
| μ forecast | < 3.6 × 10⁻⁷; < 9.4 × 10⁻⁸ optimistic (95%) | PIXIE forecast | arXiv:1705.01534 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Galactic residual read as a distortion.** y couples more strongly to the
  Galactic residual; a 9 K component may be dust variations [src:
  arXiv:astro-ph/9605054, Sects. 6.1, 6.3]. Test: vary the latitude cut and
  the Galactic model; add the spread as a systematic, as FIRAS did for y.
- **μ absorbed by the temperature.** With linear templates μ and ΔT are
  > 95% correlated [src: arXiv:2206.02762, Sect. III.1]. Test: non-linear μ
  in the fit; report the μ–ΔT correlation.
- **Foreground model too rigid.** Fixed β_d degrades with mask choice
  [src: arXiv:2206.02762, Table 1]. Test: monopole across masks for each
  model.
- **Unmodelled CIB and lines.** Neither is in the 2022 model; frequencies
  above 600 GHz are cut [src: arXiv:2206.02762, Sect. III.2]. Test:
  frequency cuts; template deprojection (their Sect. IV.3.3).
- **Imager zero levels.** Map offsets tied to CIB monopole models [src:
  arXiv:2206.02762, Sect. VI.3]. Test: propagate offset uncertainties.
- **Wrong visibility for short lifetimes.** Instantaneous-release estimates
  underestimate J̄ above z_μ [src: arXiv:1109.6552, Sect. 3.6.1]. Test:
  Green's function from CosmoTherm.
- **Forecast without SED curvature or averaging.** Two-parameter synchrotron
  inflates μ significance by about 2 [src: arXiv:1705.01534, Sect. 7.1].
  Test: curved synchrotron and moment expansion.
- **Sampler failure in high dimension.** emcee converges "extremely slowly"
  with 14–16 parameters [src: arXiv:1705.01534, Sect. 5]. Test: compare
  with Fisher where Gaussian; use another sampler.

## Reading list
<!-- key: reading-list -->

- Foundation and data: Fixsen et al. 1996, arXiv:astro-ph/9605054 —
  instrument, calibration, monopole fit and Galactic model.
- Method: Chluba & Sunyaev 2012, arXiv:1109.6552 — thermalisation, z_μ,
  visibility, decaying-particle efficiency.
- Review: Chluba 2025, arXiv:2502.05188 — leading-order formulas, Green's
  function, energy-release limits.
- Application: Bianchini & Fabbian 2022, arXiv:2206.02762 — pixel-level μ
  map, covariance, foreground models; critique of Planck-based μ maps.
- Forecast method: Abitbol et al. 2017, arXiv:1705.01534 — foreground model
  and Fisher/MCMC forecasting for PIXIE.
- Review: Chluba et al. 2019, arXiv:1909.01593 — ΛCDM targets and
  next-generation sensitivities (in L2).

## Not verified
<!-- key: not-verified -->

- Table 1 of arXiv:2206.02762 prints "[×10⁻⁵]" in the header of its model
  rows while the caption and abstract give 10⁻⁶; the values are reported here
  in 10⁻⁶, consistent with the abstract's 47 × 10⁻⁶.
- The Planck μ map of Khatri & Sunyaev (as cited in arXiv:2206.02762) and
  the Wright et al. 1994 interpretation cited by Fixsen et al. were not read;
  no identifiers recorded.
- The 17-parameter distortion basis (Chluba et al. 2023a, as cited) and the
  Hu & Silk 1993 estimates were not read.
- PIXIE 2024 (arXiv:2405.20403) and FOSSIL foreground budgets were not read
  in the bodies.
