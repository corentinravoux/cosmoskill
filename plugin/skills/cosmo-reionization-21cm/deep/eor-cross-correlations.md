# Cross-correlations of 21 cm during reionisation — cosmo-reionization-21cm dossier

Scope: how a 21 cm cross-correlation during reionisation is estimated and
forecast (with galaxies, with [CII] or CO intensity maps, with the kSZ or
τ fluctuations of the CMB), which Fourier modes survive the wedge and the
galaxy redshift errors, what sets the sign and turnover of the signal, why
squared-field statistics are used, and what the only data attempts found.
Snapshot: 2026-10-19.
From: SKA EoR/CD synergies chapter (arXiv:2606.30947), Sects. 3–4; SKA
EoR/CD overview (arXiv:2606.26435), Sect. 3.

Already in L2, not repeated here: the origin papers of CO × 21 cm and
[CII] × 21 cm (Lidz et al. 2011, Gong et al. 2012) in
`physics-and-methods.md#line-intensity-mapping-in-other-lines`; the wedge and
the delay-spectrum mapping in `physics-and-methods.md#the-foreground-wedge`;
patchy kSZ power and its duration limits in `results.md#patchy-kinetic-sz`;
line–line cross-power error formula and post-reionisation galaxy crosses in
`deep/line-intensity-mapping.md` (Step 8). The post-reionisation HI × galaxy
and HI × Lyα-forest detections are a separate subtopic
(`results.md#post-reionisation-hi-intensity-mapping`); galaxy × kSZ² at low z
is in the sibling `cosmo-cmb-lss-cross-correlations/deep/ksz-gas-profiles.md`.

Status in one line: no cross-correlation of 21 cm with any tracer has been
detected at z > 6. The only data analysis read, MWA × Planck, is consistent
with zero and dominated by 21 cm foregrounds [src: Yoshiura et al. 2018,
arXiv:1803.00756, abstract]. Everything below the "data" items is a
**forecast** framework.

## How it is done
<!-- key: how-it-is-done -->

Notation. δT_b is the 21 cm brightness-temperature fluctuation; δ_g =
n_g/n̄_g − 1 the galaxy overdensity; k_∥ and k_⊥ the line-of-sight and
transverse wavenumbers; σ_z the galaxy redshift error and σ_r = c σ_z/H(z) its
comoving length; m the wedge slope (k_∥ = m k_⊥ at the wedge edge); r(k) =
P_21,g/√(P_21 P_g) the cross-correlation coefficient. Wavenumbers are in Mpc⁻¹
in Gagnon-Hartman et al. and in h Mpc⁻¹ in Sun et al. and Fronenberg & Liu;
each value below keeps the paper's unit.

### Step 1. Decide which tracer and which statistic
<!-- key: step-1-decide-which-tracer-and-which-statistic -->

| Tracer | Statistic | Why it is chosen | Forecast or data | Place read |
|---|---|---|---|---|
| Lyα emitters, Hα/[O III] emitters with spectroscopic or grism redshifts | P_21,g(k_⊥, k_∥) | tracer systematics uncorrelated with 21 cm; "a crucial sanity check for initial 21-cm detection claims" | forecast | arXiv:2502.20447, Sect. 6 |
| Photometric Lyman-break galaxies (σ_z ≳ 0.1) | galaxy × (filtered 21 cm)² | direct cross is suppressed once σ_r × max(k_∥,0, m k_⊥) > 1 | forecast | arXiv:2609.35957, Sect. 2.3 |
| [CII] or CO intensity maps | P_21×[CII] | foregrounds and noise of the two lines are independent | forecast | arXiv:2407.14588, Sect. I; arXiv:2606.30947, Sect. 3.3.4 |
| Patchy kSZ | kSZ² × 21 cm² (bispectrum family) | the kSZ only responds to low-k_∥ modes, which the 21 cm filter removes | forecast | arXiv:2503.09462, abstract and Sect. II.4 |
| CMB temperature (Doppler) | 21 cm × T on degree scales | — | data: consistent with zero | arXiv:1803.00756, abstract |
| τ fluctuations, E modes | 21 cm × τ, 21 cm × E | anti-correlation of ionised and neutral gas | forecast | arXiv:2606.30947, Sect. 3.1.1 |

### Step 2. Build the cross-power on the modes both data sets keep
<!-- key: step-2-build-the-cross-power-on-the-modes-both -->

As Gagnon-Hartman, Davies & Mesinger write it [src: arXiv:2502.20447, Sect. 3]:

- Cut the light-cone into chunks of Δν = 6 MHz and compute
  P_21,g(k_⊥, k_∥, z) = ⟨δT_b* δ_g⟩ in cylindrical bins (Eq. 20), "the
  natural basis for interferometers", which also relegates foregrounds to
  one corner of Fourier space.
- Average only over modes that are inside the galaxy footprint (it sets the
  smallest k_⊥), outside the wedge, and above an intrinsic foreground cut.
  The wedge slope is m(z) = sin(θ_FoV) D_c(z) H(z)/[c (1 + z)] (Eq. 21), with
  θ_FoV the angular radius of the beam; three scenarios: fiducial (this
  slope), pessimistic (doubled), optimistic (halved, as a stand-in for
  foreground recovery inside the wedge), with k_∥ ≤ 0.07 Mpc⁻¹ excised
  (fiducial, optimistic) or ≤ 0.175 Mpc⁻¹ (pessimistic) [src: arXiv:2502.20447,
  Sect. 3].
- Galaxy redshift errors are not cut but carried in the noise (Step 3).
- Contaminated modes are treated as unusable and the others as clean. The
  authors note that keeping modes with uncorrelated systematics "might
  still improve the S/N" because such systematics change the variance, not
  the mean; quantifying it needs a forward model of the residuals, left to
  future work.

Sun et al. write the same cuts as a window W_fg = Θ(|k_∥| − k_∥,0) Θ(|k_∥| −
m k_⊥) (Eq. 6) and the redshift error as W_gal = exp(−k_∥² σ_r²/2) (Eq. 7),
with fiducial σ_z = 0.1, k_∥,0 = 0.1 h Mpc⁻¹ and m = 1, fixed in redshift
"given the considerable uncertainty" [src: arXiv:2609.35957, Sect. 2.3].
Zhou et al. use the horizon slope m = H(z) D_c/[c (1 + z)], "around 3" during
reionisation, and an optimistic case where only k_∥ < k_∥,0 is lost [src:
arXiv:2503.09462, Sect. II.4, Eqs. 10–12].

### Step 3. Write the variance
<!-- key: step-3-write-the-variance -->

Per mode, σ²_21,g = ½ [P²_21,g + σ_21 σ_g], with σ²_21 = ½ [P_21/T₀² +
P_21^noise]² and σ²_g = ½ [P_g + P_g^noise]² (Eqs. 22–26); T₀(z) = 26
[(T_S − T_γ)/T_S] (Ω_b h²/0.022) [(0.143/Ω_m h²)(1 + z)/10]^½ normalises the
21 cm field (Eq. 24). The 21 cm noise comes from 21cmSense for HERA-350 or
SKA-Low AA*, 1080 h of drift scans (6 h per night over 180 days), giving
footprints of 990 and 332 deg² for 3σ Gaussian-beam widths of 11.0° and
3.68°. The galaxy noise is P_g^noise = n_gal⁻¹ exp[k_∥² (c σ_z/H)²] (Eq. 27),
shot noise times the redshift-error suppression (Lidz et al. 2009) [src:
arXiv:2502.20447, Sect. 3].

For intensity-map crosses the analytic variance is only a guide: Fronenberg &
Liu build Monte Carlo ensembles over signal, foregrounds (synchrotron,
free–free, point sources for 21 cm; CO interlopers for [CII]) and noise,
pass them through an interferometer and a single-dish model, and read error
covariances, window functions and full distributions from the ensemble
(LIMstat) [src: arXiv:2407.14588, Sects. I–II]. The cumulative S/N is then
SNR_cum = (⟨P̂⟩ᵀ Σ⁻¹ ⟨P̂⟩)^½ with Σ the ensemble covariance of the band powers
(Eq. 24) [src: arXiv:2407.14588, Sect. VII.1].

### Step 4. Model the signal
<!-- key: step-4-model-the-signal -->

- Sign. An IGM colder than the CMB gives a positive galaxy–21 cm
  correlation; in the post-heating regime (saturated spin temperature) it is
  negative [src: arXiv:2606.30947, Sect. 3.2.2]. The large-scale sign change
  happens "when both ionization fluctuations dominate over 21 cm spin
  temperature fluctuations and when the average spin temperature exceeds"
  the CMB temperature; the transition redshift is insensitive to the
  galaxy tracer, depends on the heating history, and is scale dependent
  [src: Moriwaki, Beane & Lidz 2024, arXiv:2404.08266, abstract].
- Shape. The strongest anti-correlation is at scales below a few cMpc,
  where ionised regions around emitters are cold spots; r(k) tends to zero
  on large scales [src: arXiv:2606.30947, Sect. 3.2.1]. For emitters the
  small-scale amplitude scales with the mean neutral fraction and the
  spin-temperature-weighted overdensity of neutral regions; the size
  distribution of ionised regions sets the shape and inversion point; the
  amplitude falls if lower-mass galaxies drive reionisation [src:
  arXiv:2606.30947, Sect. 3.2.2, summarising Hutter et al.].
- Simulation. 21cmFASTv4 light-cones of 1 Gpc with galaxies assigned Lyα
  luminosities from the empirical relations of Mason et al. 2018 and other
  lines from Gong et al. 2017; six realisations per magnitude cut [src:
  arXiv:2502.20447, Sects. 4 and 6]. For intensity-map forecasts, correlated
  Gaussian fields can stand in: T_[CII](k) = f(k) T_21(k) e^(−iφ(k)), f =
  √(P_[CII]/P_21), with a random phase of width σ(k) tuned to the desired r(k)
  (Eqs. 4–5); these fields carry no physical non-Gaussianity [src:
  arXiv:2407.14588, Sect. III].

### Step 5. Square the filtered field when the overlap is gone
<!-- key: step-5-square-the-filtered-field-when-the -->

Cross-correlating a long-wavelength field (photometric galaxies, kSZ) with a
21 cm field that lost its low-k_∥ modes gives almost nothing. Squaring the
filtered 21 cm field 𝒯 couples pairs of surviving short modes into a long
mode of 𝒜 = 𝒯², so ⟨δ_gal 𝒜⟩ = W_gal ∫ d³q W_21(q) W_21(k − q) B_gTT (Eqs.
9–11), a projection of the galaxy–21 cm–21 cm bispectrum; in the T_S ≫ T_CMB
limit it is positive early in reionisation and negative late [src: Sun et al.
2026, arXiv:2609.35957, Sect. 2.3, Fig. 1 caption].

For the kSZ: filter the CMB with F(ℓ) = C_ℓ^kSZ,reion/(C_ℓ^TT + C_ℓ^kSZ,reion
+ C_ℓ^kSZ,late + N_ℓ) times the beam (Eqs. 8–9), N_ℓ from a harmonic ILC of
residual CIB, radio sources, tSZ and noise; filter the 21 cm field with the
foreground cut and a Wiener filter P_21/(P_21 + P_noise) (Eq. 13); square both
and cross them [src: Zhou et al. 2025, arXiv:2503.09462, Sect. II.4]. The
S/N per redshift chunk is (S/N)² = f_sky Σ_ℓ (2ℓ + 1) C_ℓ² /[C_ℓ^{T²T²,f}
C_ℓ^{21²21²,f} + C_ℓ²] (Eq. 19), with the CMB² term in the Gaussian
approximation (Eq. 20) but the 21 cm² term from noisy mocks, because the
Gaussian approximation overestimates it by 10–100 (HERA) or 1–10 (SKA1-Low)
[src: arXiv:2503.09462, Sect. IV and footnote 4]. Why squaring: a direct
kSZ × 21 cm cross is small because ionised regions move towards and away
from the observer with equal probability, and line-of-sight-integrated maps
cancel homogeneous against patchy contributions [src: arXiv:2606.30947,
Sect. 3.1.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Galaxy redshift precision against area
<!-- key: galaxy-redshift-precision-against-area -->

| Survey type | σ_z (δz) assumed | Footprint considered | Outcome with SKA-Low AA*, fiducial wedge | Place read |
|---|---|---|---|---|
| Narrow band (Subaru HSC, SILVERRUSH: 16 deg², m_AB = 26) | 5 × 10⁻² | 10–20 deg² | no detection, even to m_AB < 30, except with optimistic foregrounds | arXiv:2502.20447, Sect. 5.1, Tables 2–3 |
| Grism (Roman HLS, z > 7.2) | 10⁻² | one AA* beam inside 500 deg² of overlap | 8σ per beam; √47 × 8 = 54.8σ for 47 beams; ~13σ with HERA-350 | arXiv:2502.20447, Sects. 5.1 and 6 |
| Grism (JWST NIRCam, Hα/[O III], FRESCO 62 arcmin²) | 10⁻² | 0–350 arcmin² | no detection; ten times the area gives ~3σ with AA4 | arXiv:2502.20447, Sect. 6 |
| Slit (VLT MOONS, MOONRISE 1.2 deg²) | 10⁻³ | 0–4 deg² | ~3σ; ELT MOSAIC ~4σ in ~500 h over 1–3 deg², 5σ in 1000 h | arXiv:2502.20447, Sect. 5.1 |

The narrow-band result "contradicts some previous claims (e.g., Sobacchi et
al. 2016; Hutter et al. 2018), which treated the redshift uncertainties in
the LAE sample more simplistically" [src: arXiv:2502.20447, Sect. 5.1]. The
synergies chapter, summarising earlier forecasts, still writes that
narrow-band surveys reach S/N > 1 over several k bins for 10 deg² and need
> 10 deg² for significant detections, while slit and slitless surveys reach
S/N > 3 with fields of several 100 arcmin² to 1 deg² [src: arXiv:2606.30947,
Sect. 3.2.1]. The two statements differ in the treatment of σ_z; the more
recent forecast is the one that propagates it through Eq. 27. The floor of δz
~ 0.001 is set by peculiar velocities and the Lyα offset from systemic [src:
arXiv:2502.20447, Sect. 3, footnote 3]. More pointings beat more depth per
unit time [src: arXiv:2502.20447, Sect. 5.1]. A slit-spectroscopic Lyα survey
to m_AB^α ≤ 26 at z ~ 7 needs photometric candidates to M_UV ≤ −20 for ≥ 95%
completeness [src: arXiv:2502.20447, Sect. 4].

### Direct cross or squared field
<!-- key: direct-cross-or-squared-field -->

The squared statistic opens photometric samples (σ_z ~ 0.1–0.3): for 10 deg²,
1000 h of SKA-Low with 15 MHz bandwidth and a Roman HLWAS sample to m_AB = 27,
the LBG–21 cm² cross is "detectable at high significance across much of the
EoR" (**forecast**) [src: arXiv:2609.35957, abstract]. Its cost is that it
measures a projected bispectrum, whose amplitude depends on the available
triangle configurations [src: arXiv:2609.35957, Sect. 2.3]. For the kSZ, the
kSZ² × 21 cm² signal peaks at x_HII ≈ 0.1–0.2, changes sign, reaches a minimum
near x_HII ~ 0.5 and vanishes at the end, in three models; S/N ≳ 5 is
possible with SKA1-Low and CMB-S4 (**forecast**) [src: arXiv:2503.09462,
abstract]. With HERA the 21 cm² variance rises at lower z because fixed ℓ maps
onto larger k_⊥ where baseline counts are low; the largest S/N is near z₀ ~ 9
at intermediate chunk widths, a trade-off between variance (falls with wider
chunks) and signal (also falls) [src: arXiv:2503.09462, Sect. IV].

### Wedge avoidance or recovery
<!-- key: wedge-avoidance-or-recovery -->

Foreground scenarios change the S/N by "factors of few"; recovering wedge
modes helps SKA-Low far more than HERA, whose wedge modes carry high noise —
"Foreground-avoidance was indeed a design choice for HERA" [src:
arXiv:2502.20447, Sects. 3 and 6]. For HERA × CCAT-prime with wedge
avoidance, the usable region is k_∥ > 0.29 and k_⊥ < 0.29 h Mpc⁻¹ in five k
bins; z = 6 is noise-limited and z = 7–8 limited by a CO(2–1) interloper;
the limited Fourier overlap limits the cumulative S/N [src: arXiv:2407.14588,
Sect. VII.1 and Fig. 8 caption].

### Galaxy cross or intensity-map cross
<!-- key: galaxy-cross-or-intensity-map-cross -->

A galaxy survey gives positions with a known redshift error and a shot-noise
floor; a [CII] map carries its own foregrounds (CO interlopers) and transfer
function, so both sides need modelling. The motive for either is the same:
independent foregrounds and noise. The caveat is the same: residual
foregrounds "will increase the uncertainty" of the cross-power [src:
arXiv:2606.30947, Sect. 3.3.4]. The light-cone effect can change the [CII] ×
21 cm amplitude by ≈ 20% or more at k ≤ 0.1 Mpc⁻¹ [src: arXiv:2606.30947, Sect.
3.3.4, summarising Murmu et al. 2021].

### Stacking or a power spectrum
<!-- key: stacking-or-a-power-spectrum -->

Stacking 21 cm images around galaxies measures the mean profile of ionised
regions; without foregrounds 30 galaxies give 5σ at z ~ 9, with foregrounds
100 of the brightest galaxies in one SKA1-Low field give 1.4σ; partial
foreground removal reduces the number needed. Differencing the mean signal on
1–5 arcmin between fields with and without emitters (10 fields, 1000 h) can
separate an IGM 10% neutral from one 50% neutral (**forecasts**) [src:
arXiv:2606.30947, Sect. 4.1.2, summarising Davies et al. 2021 and Hutter et
al. 2017].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Chunk width for cylindrical cross-power | Δν = 6 MHz | 21cmFASTv4 forecast | arXiv:2502.20447 | Sect. 3 |
| Intrinsic foreground cut | k_∥ ≤ 0.07 Mpc⁻¹ (fiducial), ≤ 0.175 Mpc⁻¹ (pessimistic) | same | arXiv:2502.20447 | Sect. 3 |
| 21 cm integration and footprints | 1080 h; SKA-Low AA* 332 deg², HERA-350 990 deg² | same | arXiv:2502.20447 | Sect. 3, footnote 4 |
| Redshift errors assumed | narrow band 5%, grism 1%, slit 0.1% | same | arXiv:2502.20447 | Sect. 4 |
| LBG–21 cm² fiducial cuts | σ_z = 0.1, k_∥,0 = 0.1 h Mpc⁻¹, m = 1 | LIMFAST | arXiv:2609.35957 | Sect. 2.3 |
| Horizon wedge slope during the EoR | m ≈ 3 | kSZ² × 21 cm² | arXiv:2503.09462 | Sect. II.4 |
| Gaussian overestimate of the 21 cm² variance | × 10–100 (HERA), × 1–10 (SKA1-Low) | same | arXiv:2503.09462 | Sect. IV, footnote 4 |
| Foreground removal needed for 21 cm × LAE (MWA) | ≥ 99% of point sources and 80% of diffuse emission for k < 0.5 h Mpc⁻¹; 80 times the MWA-128 sensitivity at small scales | MWA + HSC/PFS simulation | arXiv:1709.04168 | abstract |
| MWA × Planck data | consistent with zero; polynomial foreground fit lowers the error tenfold; detection needs > 99.95% foreground removal, 2000 h and f_sky = 0.5 | MWA Phase I | arXiv:1803.00756 | abstract |
| 21 cm × E-mode cross | S/N of one only for SKA-Low fields of 1000 h covering 2% of the sky, before foregrounds | review | arXiv:2606.30947 | Sect. 3.1.1 |
| 21 cm × τ cross | cumulative S/N 11.5 for SKA × SO over ≥ 10% of the sky, noise- and cosmic-variance-limited | review, quoting Roy et al. 2020 | arXiv:2606.30947 | Sect. 3.1.1 |
| Galaxy-informed stacking | 5σ with 30 galaxies without foregrounds; 1.4σ with 100 with foregrounds (z ~ 9) | review, quoting Davies et al. 2021 | arXiv:2606.30947 | Sect. 4.1.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- Foregrounds do not bias a cross-spectrum on average but dominate its
  variance. In MWA simulations they dominate the cross-power error "even in
  the so-called EoR window" [src: arXiv:1709.04168, abstract]; in MWA ×
  Planck data the error is foreground dominated, and the variance shows
  "unexpected systematics error at small scales" [src: arXiv:1803.00756,
  abstract]. Checks made there: dependence on ionospheric activity, on the
  group of pointings and on frequency [src: arXiv:1803.00756, abstract].
- The angular average is not the ensemble average. Cross-correlation
  "correlates away" foregrounds only if different sky patches have
  independent foregrounds; for 6 × 6 deg² patches combined incoherently, the
  residual foreground scatter at k = 0.16 and 0.36 h Mpc⁻¹ follows 1/√N, so
  the approximation holds in that test [src: arXiv:2407.14588, Sect. IX.1].
- Non-Gaussian errors. Binning the 3D P(k⃗) into the spherical P(k) sums non-independent,
  non-identically distributed variables, so the central limit theorem need
  not apply; some Gaussianisation occurs with residual non-trivial tails
  [src: arXiv:2407.14588, Sect. IX.2].
- Correlated band powers. Substantial correlations between all k bins appear
  in the HERA × CCAT-prime forecasts, against the rule of thumb that bins
  spaced by more than 2π/L are independent; use the full covariance, above all
  at low S/N [src: arXiv:2407.14588, Sect. IX.4]. Window functions are broad
  and skewed; a band power does not measure power at its bin centre [src:
  arXiv:2407.14588, Sect. VII.1].
- Separate simulation of components. Varying signal, foreground and noise
  one at a time and adding the variances in quadrature reproduces the full
  Monte Carlo outside the wedge, but not at low k where foregrounds matter
  [src: arXiv:2407.14588, Sect. IX.3].
- Interlopers on the line side. For HERA × CCAT-prime, CO(2–1) limits the z =
  7 and 8 cross [src: arXiv:2407.14588, Fig. 8 caption].
- Redshift errors treated loosely. They decide whether narrow-band samples
  can be used at all (see the table above) [src: arXiv:2502.20447, Sect. 5.1].
- Sign confusion. A positive cross can mean a cold IGM or an early stage of
  reionisation; the sign alone does not give x_HI without the heating history
  [src: arXiv:2404.08266, abstract; arXiv:2609.35957, Sect. 2.3].

## Reading list
<!-- key: reading-list -->

- Review: SKA EoR/CD synergies chapter, arXiv:2606.30947 — map of all
  cross-correlation and stacking options with their forecasts (Sects. 3–4).
- Method: Gagnon-Hartman, Davies & Mesinger 2025, arXiv:2502.20447 —
  cylindrical cross-power, wedge scenarios, redshift-error noise, survey
  benchmarks.
- Method: Sun et al. 2026, arXiv:2609.35957 — galaxy × 21 cm² for
  photometric samples.
- Method: Zhou et al. 2025, arXiv:2503.09462 — kSZ² × 21 cm², filters and
  S/N with mock-based variance.
- Method and critique: Fronenberg & Liu 2024, arXiv:2407.14588 — end-to-end
  Monte Carlo of 21 cm × [CII] errors; what the analytic forecasts get wrong.
- Theory: Moriwaki, Beane & Lidz 2024, arXiv:2404.08266 — what sets the
  sign change of the large-scale cross-power.
- Data: Yoshiura et al. 2018, arXiv:1803.00756 — MWA × Planck, the only data
  analysis found.
- Systematics: Yoshiura et al. 2017, arXiv:1709.04168 — foreground removal
  needed for 21 cm × LAE.
- Foundation: Lidz et al. 2011, arXiv:1104.4800 — CO × 21 cm at reionisation
  redshifts.

## Not verified
<!-- key: not-verified -->

- The papers summarised by the synergies chapter (Sobacchi et al. 2016,
  Hutter et al. 2017, 2018, 2023, Kubota et al. 2018, 2020, Heneka &
  Mesinger 2020, Davies et al. 2021, Roy et al. 2020, Tashiro et al. 2010,
  Karoumpis et al. 2022, 2024, Murmu et al. 2021) were not read; their
  numbers above are as the chapter quotes them. Sobacchi et al. 2016
  (arXiv:1602.04837) was seen in search results only.
- The S/N values of the HERA × CCAT-prime forecast (Table 4 of
  arXiv:2407.14588) were not read.
- La Plante et al. 2020 (21 cm–kSZ–kSZ bispectrum, arXiv:2005.07206) and the
  2025–2026 kSZ² × 21 cm² follow-ups (arXiv:2512.05588, arXiv:2610.03527)
  were seen in search results only.
- The body of arXiv:1803.00756 was not read: which MWA fields, which Planck
  map, and the ℓ range are not recorded.
- No cross-correlation search with LOFAR, HERA or NenuFAR data at z > 6 was
  found by the searches run.
