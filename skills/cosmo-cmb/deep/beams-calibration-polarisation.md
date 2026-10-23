# Beams, calibration and polarisation efficiency — cosmo-cmb dossier

Scope: how a CMB experiment turns planet and point-source observations into
a beam window function with error modes, how it fixes its absolute and
polarisation calibration (dipole for Planck, cross-calibration to Planck
for ACT and SPT), how beam chromaticity and bandpasses enter the
likelihood, and how to choose between carrying beam and calibration errors
in the covariance or as sampled parameters; the leakage sizes and the
nuisance priors are in the reference files.
Snapshot: 2026-10-18.
From: Planck 2018 V, Sect. 3.4; SPT-3G D1 T&E (arXiv:2506.20707), Sect. V.2.1;
SO science goals, Sect. IV.1.4 (beam requirements).

Already in L2, not repeated here: the mechanism and size of
temperature-to-polarisation (T→P) leakage in ACT DR6, SPT-3G D1 and Planck,
and the direct SPT β_pol measurement
(`systematics.md#polarised-beams-and-temperature-to-polarisation`); the
calibration and polarisation-efficiency priors, beam-eigenmode priors and
bandpass-shift priors per analysis
(`systematics.md#nuisance-priors-and-test-sizes-by-analysis`); the
degeneracy of polarisation efficiency with Ω_c h² in ACT EE
(`physics-and-methods.md#what-each-feature-constrains`); the SPT
β_pol discrepancy as an open question
(`open-questions.md#spt-3g-polarised-beams`).

## How it is done
<!-- key: how-it-is-done -->

Notation. B(θ) is the azimuthally averaged ("symmetrised") radial beam
profile, normalised to B(0) = 1; b_ℓ its Legendre transform normalised to
unity at ℓ = 0; the beam window function of the cross-spectrum of maps i
and j is b_ℓ^i b_ℓ^j. Ω is the beam solid angle. "Array-band" is ACT's
term for one detector array at one frequency (e.g. PA5 f090). A
polarisation efficiency p (ACT) or c^PP (Planck) or E_cal (SPT)
multiplies the polarisation map amplitude, so it enters TE once and EE
twice.

### Step 1. Measure the main beam on a compact bright source
<!-- key: step-1-measure-the-main-beam-on-a-compact -->

| Analysis | Source | What is fitted | Place |
|---|---|---|---|
| ACT DR4 (method reused in DR6) | Uranus, central 12′, to about −40 dB of the peak | per-map radial profile in 55 bins of 11″ out to 10′; core fitted with basis functions f_n(θℓ_max) = J_{2n+1}(θℓ_max)/(θℓ_max) (Eq. 9), wings with an α/θ³ term plus a Ruze scattering term | [src: arXiv:2112.12226, Sects. II, IV.2.1–IV.2.6] |
| ACT DR6 | Uranus maps from a custom map-maker that removes the large-scale bias within 12′ of the planet; one joint model per season | profiles consistent between seasons except 2017, before a refocusing at the start of 2018 | [src: arXiv:2503.14451, Sect. II.7] |
| SPT-3G D1 | bright AGN in the field for the core, Saturn for the sidelobes, stitched into one composite real-space map | harmonic decomposition gives B_ℓ^T per band | [src: arXiv:2506.20707, Sect. IV.2.1] |
| Planck HFI | planet transits; spline fits | beam models convolved with the scanning strategy into beam matrices (Step 3) | [src: arXiv:1907.12875, Sect. 3.2.3] |

Stated reasons for the choices:

- ACT averages radial profiles rather than stacking the maps first,
  because averaging profiles gives the full covariance between radial
  bins. That covariance matters because atmospheric noise correlates the
  bins, and it sets the low-ℓ uncertainty of b_ℓ [src: arXiv:2112.12226,
  Sect. IV.2.1].
- ACT fits the core with Bessel functions because a 6 m aperture limits
  the optical response to ℓ ≲ 2πD/λ, so its transform is compact on a
  disk, and the Fourier transforms of the azimuthally symmetric Zernike
  polynomials are J_{2n+1}(θ)/θ (Eqs. 5–9) [src: Sect. IV.2.3].
- ACT forces the wings to fall as 1/θ³ because the Airy pattern of a
  circular aperture has an envelope ∝ 1/sin³θ beyond about 2′ (Eqs.
  10–12), confirmed by the geometric theory of diffraction (Eq. 13); the
  noise prevents separating the far wings from the background without
  such an assumption [src: Sect. IV.2.4].
- SPT stitches two sources because AGN are too faint for the sidelobes
  and planets saturate some detectors in the core [src: arXiv:2506.20707,
  Sect. IV.2.1].
- With only 6 to 51 profile measurements per covariance, ACT shrinks the
  sample covariance S toward its diagonal T, C = λ*T + (1 − λ*)S (Eq. 2),
  with λ* = Σ_{i≠j} Var(S_ij)/Σ_{i≠j} S_ij² (Eq. 4); λ* ranged from 0.24
  to 1. Stated reason: the plain sample covariance was often too noisy to
  invert [src: arXiv:2112.12226, Sect. IV.2.2].

### Step 2. Transform to harmonic space and apply small corrections
<!-- key: step-2-transform-to-harmonic-space-and-apply -->

b_ℓ = (2π/Ω) ∫ B(θ) P_ℓ(cos θ) d(cos θ) (arXiv:2112.12226, Eq. 21), with
the model extrapolated beyond the fit radius to capture the low-ℓ part and
the solid angle outside it [src: Sect. IV.3]. ACT then divides out, in
order (arXiv:2112.12226) [src: Sect. IV.4]:

| Correction | Size for ℓ < 10,000 | Place |
|---|---|---|
| Pixel window of the planet map | ≲ 0.1% | [src: Sect. IV.4] |
| Radial-binning transfer function, from simulated planet maps | ≲ 1% | [src: Sect. IV.4] |
| Uranus disk, deconvolved with 2J₁(ℓr)/(ℓr) | ≲ 0.1% | [src: Sect. IV.4] |
| Spectral (colour) correction from a Rayleigh–Jeans source to the CMB, B′(ℓ) = B(ℓν_RJ/ν_CMB) | ≲ 1.5% | [src: Sect. IV.4] |

In DR6 the colour correction is no longer a single rescaling: the
frequency dependence of the beam is inferred from a physical-optics model
whose parameters are fitted so that the model, weighted by the Uranus SED
and integrated over the passband, matches the observed Uranus profile;
beams for the CMB and for other sky components are then derived from it
[src: arXiv:2503.14451, Sect. II.7]. Per-season beams are linearly
transformed into per-split beams with weights set by each season's
statistical contribution to each split [src: Sect. II.7].

### Step 3. From instantaneous to effective map beam
<!-- key: step-3-from-instantaneous-to-effective-map-beam -->

The beam in a coadded map is broader than the planet beam because of
pointing errors, alignment and changes over a season.

- ACT models the effective beam as B_ℓ^eff = B_ℓ exp[−ℓ(ℓ+1)V/2]
  (arXiv:2112.12226, Eq. 22), with V the "pointing jitter" variance in
  square radians. V is fitted on high-pass-filtered cut-outs of point
  sources with S/N ≥ 10 matched to known catalogues, about 20 sources in
  the small deep regions to 520 in the largest; the mean V and its
  intrinsic scatter σ_V are inferred from all sources with the likelihood
  of Eq. 23 [src: Sect. IV.5]. The method was validated by injecting
  simulated sources with known V into real data [src].
- Negative V is allowed, because V absorbs all beam-altering effects, not
  only pointing (arXiv:2112.12226) [src: Sect. IV.5]. The 98 GHz jitter of PA3 is much larger
  than at 150 GHz (e.g. 190.9 ± 7.0 against 6.6 ± 5.8 arcsec² in Deep56),
  which the authors read as seasonal beam change rather than pointing
  [src: Table 3, Sect. IV.5].
- DR6: average jitter 0.15′ ± 0.04′, about 30% worse than DR4, attributed
  to the wider (60° peak-to-peak) azimuth scans; it adds 2% to the
  effective FWHM and is part of the beam model [src: arXiv:2503.14451,
  Sect. II.6]. DR6 also found pointing differences up to 0.5′ between the
  two ends of 90° azimuth scans and added a time-dependent azimuth slope
  to the pointing model [src].
- Planck: because of the scanning strategy, a beam matrix
  W_ℓ^{XY,X′Y′} relates observed and sky spectra,
  C_ℓ^XY = Σ W_ℓ^{XY,X′Y′} C_ℓ^{sky,X′Y′} (arXiv:1907.12875, Eq. 21). Its
  diagonal is the "effective beam" that corrects the data vector; its
  off-diagonal terms are leakage, corrected in the model vector. The
  effective beam of a cross-spectrum is not the geometric mean of the two
  auto-spectrum beams, and it depends on the mask; in 2018 the matrices
  were computed for the actual likelihood masks (QuickPol, Hivon et al.
  2016, arXiv:1608.08833), a correction of < 0.7% (EE), < 0.5% (TE) and
  < 0.2% (TT) at ℓ = 2000 in 143×143 [src: Sect. 3.2.3].

### Step 4. Build the beam error modes
<!-- key: step-4-build-the-beam-error-modes -->

- ACT DR4: covariance of b_ℓ from the Legendre transforms of samples of
  the radial-model posterior plus the jitter uncertainty; the matrix
  (ℓ = 0 to 30,000) is stored as its 10 largest singular modes, plus 3
  modes for variations of the surface roughness (20 and 30 μm) and of the
  offset-fit range (3.5′–5′, 5′–7′, 7′–10′): 13 modes in all, added to the
  data covariance [src: arXiv:2112.12226, Sect. IV.6]. The offset-fit
  ranges are what raise the low-ℓ beam error; DR3 had instead doubled the
  formal errors [src].
- SPT-3G D1: a beam covariance from varying the AGN and Saturn
  observations in the stitched beam and the analysis choices (stitching
  radius among them), spanning all frequencies and TT/TE/EE; nine
  eigenmodes kept (eigenvalues below 1% of the largest discarded), each
  amplitude sampled with a standard-normal prior,
  𝔹^Δ·C = (1 + Σ β_i B_i^{Δ,μ})(1 + Σ β_i B_i^{Δ,ν}) C^{μν} (Eq. 43)
  [src: arXiv:2506.20707, Sect. V.2.1]. Temperature-beam uncertainty is at
  most 0.2% of the beam at ℓ = 3000 [src: Sect. IV.2.1].
- Planck 2018 ignores beam-determination uncertainty entirely. Stated
  reason: in 2015 the analytically marginalised beam-error contribution to
  the covariance had become effectively negligible [src: arXiv:1907.12875,
  Sect. 3.3.5].

### Step 5. Calibrate the temperature amplitude
<!-- key: step-5-calibrate-the-temperature-amplitude -->

| Analysis | Procedure | Place |
|---|---|---|
| Planck HFI | orbital dipole as absolute calibrator; gain precision better than 3 × 10⁻⁴ for the CMB channels (as quoted from the HFI processing paper); 100 and 217 GHz inter-calibrated to 143×143 by minimising χ²(c_ν^TT) of Eq. 42 on dust-cleaned maps, cross-checked with SMICA over 30 < ℓ_min < 100 and 400 < ℓ_max < 600 | [src: arXiv:1907.12875, Sects. 3.3.4–3.3.5, Eqs. 42–43] |
| ACT DR6 | Uranus gives a first calibration good to 1–4% (scatter of the gain–loading relation, point source versus beam-filling CMB); final per-array-band factor against Planck temperature maps on the common sky by three estimators (Eq. 15): ⟨C^{A×A}/C^{A×P}⟩, ⟨C^{A×A}/C^{P×P}⟩^½, ⟨C^{A×P}/C^{P×P}⟩, averaged over ℓ_min ≤ ℓ ≤ 2000 | [src: arXiv:2503.14451, Sect. II.4.2; arXiv:2503.14452, Sect. V.3] |
| SPT-3G D1 | 150 GHz maps cross-correlated with Planck PR3 143 GHz inside the Main-field mask, ℓ = 800–1200 for gain and 400–1300 for polarisation efficiency; the Planck map is mock-observed through the SPT filtering; 95 and 220 GHz then calibrated internally to the recalibrated 150 GHz map | [src: arXiv:2506.20707, Sect. III.4] |

- ACT uses three estimators because they "would not have to agree if the
  ACT or Planck data were affected by additive systematic effects"; PA5
  and PA6 agree between them at 0.3%, PA4 scatters more within its errors
  [src: arXiv:2503.14452, Sect. V.3].
- ACT doubles the measured calibration error to define the prior, and
  carries the Planck dipole uncertainty as a separate parameter cal_dipole
  [src: Sect. VI.1.5].
- SPT normalises its temperature beam at ℓ = 800 "to decorrelate the beam
  shape from the Planck based calibration" [src: arXiv:2506.20707,
  Sect. IV.2.1]. ACT DR4 instead normalises the beam at θ = 0 and treats
  calibration separately, because the calibration is done over a range of
  ℓ (600 < ℓ < 1800 in DR4), not at a single "effective" multipole as in
  DR3 [src: arXiv:2112.12226, Sect. IV.6].
- SPT states that the cross-calibration uses about 4% of the Planck map
  and so does not compromise blindness to Planck in the cosmological
  analysis [src: arXiv:2506.20707, Sect. III.4].

The calibrated model spectra in ACT DR6 are D^th_{TT}/(cal²_dipole c_X c_W),
D^th_{TE}/(cal²_dipole c_X c_W p_W) and D^th_{EE}/(cal²_dipole c_X c_W p_X p_W)
for array-bands X and W [src: arXiv:2503.14452, Sect. VI.1.5].

### Step 6. Fix or fit the polarisation efficiency
<!-- key: step-6-fix-or-fit-the-polarisation-efficiency -->

No experiment has an independent absolute measurement precise enough, so
all three tie it to the CMB itself.

- Planck 2018. Ground-measured efficiencies (about 83–96% per detector,
  statistical error about 0.3%) are in the map-making. Relative
  corrections at 353 GHz from polarised dust came out about five times the
  ground error. For 100–217 GHz the absolute factor c_ν^PP is fitted by
  matching C_ℓ^{EE,ν×ν} to the EE spectrum predicted by the TT-only ΛCDM
  best fit (Eq. 44), over 200 ≤ ℓ ≤ 1000 [src: arXiv:1907.12875,
  Sect. 3.3.4]. Stated reasons: EE is too noisy for an EE-to-EE
  inter-calibration, and only a fit to a model gives the absolute
  temperature-to-polarisation ratio; ℓ < 200 is cut for Galactic
  residuals and ℓ > 1000 for low S/N [src]. The authors acknowledge that
  this pushes polarisation parameters toward temperature, and check that
  marginalising the absolute T-to-P calibration leaves parameters
  unchanged [src].
- The TE-based check of arXiv:1907.12875, Eq. 46, gives c_100^TE = 1.04 ± 0.02,
  c_143^TE = 1.00 ± 0.02, c_217^TE = 1.02 ± 0.02 (Eq. 47), about 1σ from
  the EE values at 100 and 217 GHz and more at 143 GHz [src]. End-to-end
  simulations show no such difference; correlated noise, a residual
  transfer function and leakage-template errors (too small by about a
  factor 5) were ruled out [src]. Plik's baseline keeps the map-based
  model; the spectrum-based alternative is tested with CamSpec [src].
- ACT DR6 first rescales each spectrum with an efficiency fitted to a
  fiducial ΛCDM EE, so that null tests are amplitude-independent, then
  frees one efficiency per array-band in the likelihood with a flat ±10%
  prior, sampled with each cosmological model [src: arXiv:2503.14452,
  Sect. V.3]. The released maps are divided by efficiencies of 0.907 to
  0.972 (Table 8 of the maps paper) [src: arXiv:2503.14451, Sect. III.10].
- SPT-3G D1 fits the external efficiency jointly with cosmology under a
  flat prior, and uses the Planck-based prior only for TE-only or EE-only
  results, where some parameters are fully degenerate with it [src:
  arXiv:2506.20707, Sect. V.2.1].

### Step 7. Model polarised beams and beam chromaticity
<!-- key: step-7-model-polarised-beams-and-beam -->

- Polarised sidelobes (ACT DR4). Compact lobes near 15′ (PA1, PA2) or
  30–40′ (PA3) from the beam centre, polarised perpendicular to the
  radius, holding 1.2%, 3.4% and 0.15% of the main-beam solid angle;
  stable in time and attributed to diffraction by the metal-mesh filters.
  They are modelled as shifted, polarised copies of the main beam fitted
  on stacked Saturn maps and deprojected from the time-ordered data before
  map-making; the residual is carried as a leakage term [src:
  arXiv:2112.12226, Sect. V.2]. The leakage factor γ_ℓ never exceeds
  0.0035 at 150 GHz and 0.038 at 98 GHz; at ℓ ≈ 1000–3000 it is a 1–4%
  effect on TE and 0–0.4% on EE (Eqs. 26a–b) [src: Sect. V.3].
- Polarised beam shape (SPT-3G D1).
  B_ℓ^{P;μ} = (B_ℓ^{main;μ} + β_pol^μ B_ℓ^{sidelobe;μ})/(same at ℓ = 800)
  (Eq. 18), with the main beam computed from the optics and the sidelobe
  term defined as B^T − B^main (Eq. 19) [src: arXiv:2506.20707,
  Sect. IV.2.3]. Stated reason: no polarised source in the field is bright
  enough to map the polarised beam, and sidelobes from scattering and
  panel gaps need not be polarised like the main beam [src: App. B.2].
- Quadrupolar leakage (SPT, arXiv:2506.20707). Leakage beams are Hermite expansions around
  a Gaussian (Eq. 122), fitted on 25 coadds built from 418 bright-source
  thumbnails; the spin-2 amplitude is
  ε₂ = (a_{2,0}^{T→Q} − a_{0,2}^{T→Q} + a_{1,1}^{T→U})/2 (Eq. 124), propagated
  to band powers by Eq. 14 [src: App. B.1, Sect. IV.2.2].
- Beam chromaticity. With a passband τ_ν, the CMB beam is
  b_ℓ^CMB = (1/𝒦) ∫ dν τ_ν 𝓕_ν b_{ℓ,ν}, 𝒦 = ∫ dν τ_ν 𝓕_ν, where 𝓕_ν is the
  thermodynamic-to-surface-brightness conversion (Giardiello et al. 2024,
  arXiv:2411.10124, Eqs. 3, 5). A foreground with SED f_ν then enters each
  channel through f̂_ℓ = ∫ dν r_{ℓ,ν} f_ν with
  r_{ℓ,ν} = τ_ν 𝓕_ν b_{ℓ,ν}/∫ τ 𝓕 b (Eqs. 10–11): an ℓ-dependent effective
  frequency. The CMB term is unaffected if its beam is right; only the
  foreground terms change [src: Sect. II].
- ACT DR6 implements this in MFLike with chromatic beam windows in the
  normalised passband (Eqs. 30–31), and does not propagate bandpass shifts
  into the chromatic beams, judging that a second-order effect [src:
  arXiv:2503.14452, Sect. VI.1.4]. The passbands were measured with a
  Fourier-transform spectrometer at 15–20 pointings per optics tube; their
  errors are well approximated by uniform shifts [src].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Beam errors in the covariance, or as sampled parameters
<!-- key: beam-errors-in-the-covariance-or-as-sampled -->

- Covariance (ACT, Planck 2013–2015 analytically marginalised): no extra
  dimensions in the chain. ACT DR6 adds a beam term
  ∝ D_ℓ D_ℓ′ ⟨δB δB/BB⟩ from Uranus to the covariance
  (`physics-and-methods.md#covariance-and-likelihood`).
- Parameters (SPT D1, nine eigenmodes): residual beam errors can be
  fitted and checked against zero. SPT reports all nine amplitudes
  compatible with zero, also after widening the priors by a factor 10
  [src: arXiv:2506.20707, Sect. V.2.1]. The cost, priors ×100 wider,
  shifts n_s by < 0.5σ (`systematics.md#spt-3g-d1-t-e-camphuis-et-al-2025-arxiv-2506`).
- Ignore (Planck 2018): justified by the 2015 finding of a negligible
  contribution [src: arXiv:1907.12875, Sect. 3.3.5].

### Polarisation efficiency: fixed from TT, or free
<!-- key: polarisation-efficiency-fixed-from-tt-or-free -->

- Fixed from the TT best fit (Planck Plik baseline): uses the T–P
  agreement and risks pulling polarisation parameters toward TT; the
  authors found the TT/TE/EE agreement decreased rather than increased
  after these corrections [src: arXiv:1907.12875, Sect. 3.3.4].
- Free with a broad prior (ACT uniform 0.9–1.1, arXiv:2503.14452, Table 4;
  SPT U(0.8, 1.2), arXiv:2506.20707, Table 9): model-independent
  amplitude, at a cost for EE-only constraints, which ACT quantifies as a
  doubling of σ(Ω_c h²) and σ(H₀) (L2). ACT reports that freeing the Planck
  efficiency does not broaden the P-ACT EE posteriors
  (`systematics.md#act-dr6-power-spectra-louis-et-al-2025-arxiv`).

### Polarised beam equal to the temperature beam, or one free fraction
<!-- key: polarised-beam-equal-to-the-temperature-beam-or -->

- Equal (pre-unblinding SPT, ACT, Planck with GRASP check): simplest; the
  Planck GRASP simulations put the effect of imperfect co-polarisation at
  < 0.3% in polarised amplitude and < 0.4′ in effective FWHM, absorbed by
  the efficiency correction [src: arXiv:1907.12875, Sect. 3.3.5].
- One β_pol per band (SPT D1): preferred by Δχ² = 30.8 in a
  cosmology-independent lite reconstruction (χ² 1198.64 against 1229.46,
  ΔAIC = 24.8), with 22.7 of the improvement below ℓ = 1000 [src:
  arXiv:2506.20707, App. B.2]. The EE 150×150 versus 95×150 difference
  test went from PTE 0.004 to 51% [src].
- The direct point-source measurement uses the same one-parameter model,
  written B_pol = (1 − β_pol)B_main + β_pol B_full (arXiv:2602.06334,
  Eq. 3), and draws about 45% (95 and 220 GHz) and 30% (150 GHz) of its
  precision from ℓ < 3000, the rest mostly from 3000 ≲ ℓ ≲ 10,000
  [src: Sects. 4.2 and 4.3], while the spectra constrain β_pol at
  ℓ ≲ 3000 [src: Sect. 5.2]. The authors list a scale-dependent
  polarised beam as one possible reconciliation; their ℓ-restricted fits
  find no significant scale dependence (weakest p = 0.08 before
  look-elsewhere) [src: Sect. 5.2].

### Chromatic or achromatic beams
<!-- key: chromatic-or-achromatic-beams -->

- For passbands of fractional width Δν/ν ≈ 0.2 in an SO-LAT-like setup,
  neglecting chromaticity shifts extragalactic foreground parameters by
  more than 2σ and N_eff and H₀ by up to 0.3σ (α = 2, the
  diffraction-limited scaling), with no change of errors; for a
  cosmic-variance-limited survey the cosmological shifts reach several σ
  (**forecast**) [src: arXiv:2411.10124, Sect. III].
- In ACT DR6 data, neglecting it shifts foreground parameters by up to 1σ;
  it was added after unblinding [src: arXiv:2503.14452, Sect. VI.1.4;
  App. B as in L2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Uranus profile depth | about −40 dB of peak, 55 bins of 11″ to 10′ | ACT DR4 | arXiv:2112.12226 | Sect. IV.2.1 |
| Shrinkage intensity λ* | 0.24–1 | ACT DR4 | arXiv:2112.12226 | Sect. IV.2.2 |
| Primary surface rms used in the Ruze term | 20 μm (30 μm tested as an error mode) | ACT DR4 | arXiv:2112.12226 | Sects. IV.2.5–IV.6 |
| Beam error modes kept | 10 statistical + 3 systematic | ACT DR4 | arXiv:2112.12226 | Sect. IV.6 |
| Effective-beam solid angle, PA2 150 GHz S15 Deep56 | 190.3 ± 4.8 nsr | ACT DR4 | arXiv:2112.12226 | Table 4 |
| Solid angle for synchrotron, dust or tSZ SEDs versus CMB | differs by 0.3–5.3% | ACT DR4 | arXiv:2112.12226 | Sect. IV.5, App. C |
| DR6 pointing jitter | 0.15′ ± 0.04′ (+2% on FWHM) | ACT DR6 | arXiv:2503.14451 | Sect. II.6 |
| DR6 effective FWHM | printed as 1.42/2.07/1.01′ at f090/f150/f220 (the first two appear transposed in the text) | ACT DR6 | arXiv:2503.14451 | Sect. II.7 |
| Intensity-beam power leaking into E / B, near sidelobes excluded | about 0.01% / 0.002% | ACT DR6 | arXiv:2503.14451 | Sect. II.7 |
| Uranus calibration accuracy (before Planck) | 1–4% by band; Planck calibrates Uranus to 1% | ACT DR6 | arXiv:2503.14451 | Sect. II.4.2 |
| Calibration factors to Planck (release) | 0.9702–1.0435 by array-band; statistical errors 0.0008–0.0015 (PA5, PA6), 0.006–0.028 (PA4 f220) | ACT DR6 | arXiv:2503.14452 | Table 8 |
| Polarisation-efficiency corrections in released maps | 0.9074–0.9715 | ACT DR6 | arXiv:2503.14451 | Table 8 |
| Bandpass uncertainty | about 1 GHz; up to 3.6 GHz (PA4 f220) | ACT DR6 | arXiv:2503.14452 | Sect. VI.1.4 |
| ACT–Planck EE comparison PTEs | 7–90% (PR3), 42–78% (NPIPE); TE versus NPIPE 100 GHz 1–9% | ACT DR6 | arXiv:2503.14452 | Table 2 |
| SPT cross-calibration ranges | gain ℓ = 800–1200; polarisation efficiency 400–1300 | SPT-3G D1 | arXiv:2506.20707 | Sect. III.4 |
| SPT temperature-beam uncertainty | ≤ 0.2% at ℓ = 3000 | SPT-3G D1 | arXiv:2506.20707 | Sect. IV.2.1 |
| Beam eigenmodes sampled | 9 (eigenvalue cut 1% of largest) | SPT-3G D1 | arXiv:2506.20707 | Sect. V.2.1 |
| Point sources for β_pol | 100 (46 Main, 54 Summer fields), > 200 mJy at 95 GHz in Main; 91 detectably polarised, mostly 1–3% | SPT-3G | arXiv:2602.06334 | Sect. 2.3 |
| Prior that the direct measurement offers | δβ_pol ≈ 0.1 at 95 and 150 GHz | SPT-3G | arXiv:2602.06334 | Sect. 5.2 |
| Planck ground efficiencies, statistical error | about 0.3% (100, 143), 0.2% (217) | Planck 2018 | arXiv:1907.12875 | Sect. 3.3.4 |
| Planck effective-beam mask correction, 143×143 at ℓ = 2000 | < 0.7% EE, < 0.5% TE, < 0.2% TT | Planck 2018 | arXiv:1907.12875 | Sect. 3.2.3 |
| Planck TE leakage correction | Δχ² ≈ 37 over 762 binned TE degrees of freedom; six free template amplitudes within 1.5σ, Δχ² = 6 | Planck 2018 | arXiv:1907.12875 | Sect. 3.3.5 |
| Planck TT→TE leakage-template error, 143×143 | < 0.1 μK² in D_ℓ near ℓ ≈ 200, about 0.1% of TE | Planck 2018 | arXiv:1907.12875 | Sect. 3.3.5 |

## What goes wrong
<!-- key: what-goes-wrong -->

| Failure | How it shows | Test that catches it | Place |
|---|---|---|---|
| Map-maker bias around the planet ("bowling", scan stripe) | wings washed out, b_ℓ wrong at low ℓ | custom planet map-maker; offset fit α/θ³ + β subtracted per profile | [src: arXiv:2503.14451, Sect. II.7; arXiv:2112.12226, Sect. IV.2.1] |
| Planet beam sharper than the map beam | small-scale power over-corrected | jitter fit on catalogue point sources in the science maps; injection test | [src: arXiv:2112.12226, Sect. IV.5] |
| Wrong colour correction | foreground parameters biased; beam solid angle off by up to 5% for non-CMB SEDs | chromatic beams in the likelihood | [src: arXiv:2112.12226, App. C; arXiv:2411.10124] |
| Additive systematic mistaken for gain | calibration estimators disagree | three ACT×Planck ratio estimators (Eq. 15) | [src: arXiv:2503.14452, Sect. V.3] |
| Polarised beam ≠ temperature beam | EE frequency-difference failures at ℓ < 1200 | cross-frequency difference tests; cosmology-free lite reconstruction | [src: arXiv:2506.20707, App. B.2] |
| Quadrupolar leakage from detector ellipticity | TE/EE differences fail above ℓ = 3000; TE–TT parameter disagreement | stacked Q/U at bright sources; difference tests | [src: arXiv:2506.20707, App. B.1] |
| Efficiency fitted from TT drags EE toward TT | apparent T–P agreement too good | TE-based versus EE-based efficiency (Planck: 143 GHz disagreement unexplained) | [src: arXiv:1907.12875, Sect. 3.3.4] |
| Daytime mirror deformation | multi-lobed beams | eigenmode "badness" β > 4% cut, removing 30–34% of daytime data | [src: arXiv:2503.14451, App. D] |
| Flat-field error | low-ℓ power loss | ACT attributes its TT ℓ < 600–1000 cut mainly to a flat field accurate to a few percent | [src: arXiv:2503.14451, Sect. II.4.1] |

Two lessons the papers draw themselves:

- SPT: the quadrupolar leakage was coherent across frequencies at large
  scales, which is why inter-frequency tests missed it except in the
  already excluded ℓ = 3000–4000 range; this "underscores a limitation of
  our blinding procedure" [src: arXiv:2506.20707, App. B.1].
- ACT DR4: the main-beam leakage correction was added after unblinding,
  when TE residuals prompted a search; it reduced residuals without moving
  cosmology, and leakage-amplitude scalings fitted to data were consistent
  with unity [src: arXiv:2112.12226, Sect. V.3].

## Reading list
<!-- key: reading-list -->

- Foundation: Hivon et al. 2016, arXiv:1608.08833 — QuickPol, the effective
  beam matrix and T→P leakage from scanning strategy and detector
  mismatch; read for why cross-spectrum beams depend on the mask.
- Method: Lungu et al. 2021, arXiv:2112.12226 — the complete ground-based
  beam pipeline (radial profiles, shrinkage covariance, Bessel core,
  1/θ³ wings, jitter, error modes, polarised sidelobes).
- Method: Giardiello et al. 2024, arXiv:2411.10124 — the chromatic-beam
  formalism and its forecast cost.
- Application: Naess et al. 2025, arXiv:2503.14451, Sects. II.4–II.7 — ACT
  DR6 flat field, Uranus calibration, pointing, beam colour correction,
  daytime beam.
- Application: Louis et al. 2025, arXiv:2503.14452, Sects. V.3, VI.1.4–VI.1.5
  — calibration to Planck and the calibrated data model.
- Application: Camphuis et al. 2025, arXiv:2506.20707, Sects. III.4, IV.2,
  V.2.1, App. B — SPT calibration, stitched beams, eigenmode sampling,
  β_pol and quadrupolar leakage.
- Application: Planck Collaboration 2019, arXiv:1907.12875, Sects. 3.2.3,
  3.3.4–3.3.5 — beam matrices, model-based efficiencies, the 143 GHz TE/EE
  efficiency puzzle.
- Critique: de Haan et al. 2026, arXiv:2602.06334 — direct β_pol from point
  sources, and the three readings of its 1.3σ difference with the spectra
  [src: abstract].

## Not verified
<!-- key: not-verified -->

- The ACT DR6 beam paper (cited as Duivenvoorden et al., "in prep" in
  arXiv:2503.14452) was not found on arXiv in the search of 2026-10-18;
  DR6 beam statements come from the maps and power-spectrum papers.
- The SPT-3G beam paper ("H26" in arXiv:2602.06334) and the SPT-3G D1 maps
  paper's calibration appendix were not read; the SPT beam covariance
  construction is as summarised in arXiv:2506.20707.
- The Planck HFI processing paper that gives the 3 × 10⁻⁴ gain precision
  was not read; the number is quoted from arXiv:1907.12875 [sec: section
  "Beams and beam-leakage uncertainty", citing its Table 7].
- Hardware polarisation-angle calibrators (wire grids, Tau A, drones) are
  in `cosmo-inflation-primordial` (birefringence) and not repeated here.
