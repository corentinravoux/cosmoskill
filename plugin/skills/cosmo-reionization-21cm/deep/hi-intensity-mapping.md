# Single-dish HI intensity mapping, from time streams to an amplitude — cosmo-reionization-21cm dossier

Scope: how a single-dish HI intensity-mapping power spectrum is produced step
by step (time-ordered calibration with noise diodes, 1/f noise, map-making,
beam reconvolution or not, choice of the number of removed modes, subset
cross-spectra, jackknife covariance, the fitted model with beam, window and
signal-loss terms, null and injection tests), with the reason each analysis
gives for its choices. The chain followed is MeerKLASS's; each step also gives
what the other single-dish experiments (GBT, Parkes, FAST) and the
interferometric ones (CHIME, MeerKAT in interferometric mode, Tianlai) do in
its place, and the cross-correlation detections with galaxy surveys.
Snapshot: 2026-10-21.
From: Wolz et al. 2026 SKA HI intensity-mapping chapter (arXiv:2607.03259),
Sects. 2–4; Bernal & Kovetz 2022 (arXiv:2206.15377), Sects. 5–6.

Already in L2, not repeated here: the amplitudes and detections
(`results.md#post-reionisation-hi-intensity-mapping`); the CHIME, GBT and
MeerKLASS pipeline rows, including the D(k) loss term and the
transfer-function formula (`physics-and-methods.md#what-the-main-limits-and-detections-did`);
signal loss, mask–gain coupling, the beam ripple and the transfer-function
debate (`systematics.md#post-reionisation-hi-intensity-mapping`,
`open-questions.md#hi-intensity-mapping-first-auto-spectra-and`).

## How it is done
<!-- key: how-it-is-done -->

Notation. T_sky(θ, ν) is the calibrated brightness temperature; a "block" is
one ~1.5 h scan of the field (arXiv:2610.12158, Sect. 2) and a "single cube" one dish in one block; N_fg
the number of removed principal components; Ω_HI b_HI the amplitude of the
auto-spectrum; T̄_HI the mean HI brightness temperature; μ the cosine of the
angle to the line of sight; f the growth rate.

### Step 1. Scan and calibrate each dish's time stream
<!-- key: step-1-scan-and-calibrate-each-dish-s-time -->

- Scan fast at constant elevation. Each of the 64 dishes scans back and forth
  in azimuth at constant elevation, "to help suppress pink noise, airmass,
  and ground spill fluctuations"; two scans per night (rising and setting
  sky) give close-to-orthogonal crossings; a bright compact source is
  tracked before and after each block as bandpass and flux calibrator [src:
  MeerKLASS Collaboration 2026, arXiv:2610.12158, Sect. 2]. In the pilot the
  scan speed was 5 arcmin s⁻¹ in azimuth, 10° in ~100 s, all at elevation
  > 40° [src: Cunnington et al. 2022, arXiv:2206.01579, Sect. 2].
- Two-step calibration with a noise diode (KATcali). First, track the
  calibrator (central and four off-axis pointings) to calibrate the diode
  power, the bandpass and the flux scale; second, use the diode, fired every
  20 s, to calibrate the scan data [src: arXiv:2610.12158, Sect. 2]. The diode
  "removes long-term noise correlation, so-called 1/f noise, due to receiver
  chain gain variations on time scales longer than 20 s"; on shorter scales
  1/f noise is negligible against thermal noise [src: arXiv:2206.01579, Sect.
  2].
- Signal model fitted to each polarisation, channel, dish and scan
  independently: T_model = T_diffuse + T_el + T_diode + T_rec, with T_el the
  elevation-dependent atmosphere and ground spill, T_rec the receiver, and
  T_diffuse = T_Gal + T_CMB (T_CMB = 2.725 K, T_Gal from PySM on the
  reprocessed Haslam 408 MHz map); the correlator output is g(t, ν) T_model
  with the gain a 4th-order polynomial in time — higher orders "produced
  noise-dominated coefficients"; T_cal = T̂_raw/g [src: MeerKLASS
  Collaboration 2024, arXiv:2407.21626, Sect. 2.2, Eqs. 1–4].
- Self-calibration. The Haslam-based sky model is replaced by the Level-6 map
  of the previous loop where that pixel has more than 40 hits, and diode
  samples are no longer up-weighted; five loops, stopped when the residual
  standard deviation converged [src: arXiv:2407.21626, Sect. 2.3, Eq. 6]. The
  reason: the Haslam map's substructure and zero level are limited by 1980s
  instruments, and the faint point sources ignored by the standard
  calibration matter once the noise is low [src: arXiv:2407.21626, Sect.
  2.3].
- RFI is flagged at several levels (raw data, calibrated data, maps) [src:
  arXiv:2610.12158, Sect. 2; arXiv:2206.01579, Sect. 2]. Of 41 deep-field
  blocks, 14 are entirely flagged [src: arXiv:2610.12158, Fig. 2 caption].

Peers for this step:

- GBT (single dish, 680–920 MHz receiver, 700–900 MHz used): passband drifts
  are controlled with a pulsed electronic calibrator averaged per scan, and
  the absolute calibration from radio point sources is accurate to 9%, quoted
  as a separate systematic [src: Switzer et al. 2013, arXiv:1304.3712, Sects.
  2 and 2.2].
- FAST (single dish, 19 beams, drift scan): all 19 beams show 1/f
  fluctuations of similar structure; a noise-diode, frequency-independent gain
  calibration every 8 s does not change the residual 1/f after SVD
  subtraction; after 30 SVD modes the knee frequency is ~6 × 10⁻⁴ Hz, and the
  1/f noise can bias the HI power spectrum by 10% [src: Hu et al. 2021,
  arXiv:2109.06447, abstract].
- CHIME (cylinder interferometer): the complex gain of each feed is
  calibrated once per sidereal day from the eigendecomposition of the
  N²_feed visibility matrix during the night-time transit of Cygnus A
  (Cassiopeia A, Taurus A or Virgo A otherwise, corrected by a "beam ratio"
  averaged over many nights); the relative spectral flux density of the
  calibrators in the band is known to better than 1% [src: CHIME
  Collaboration 2022, arXiv:2202.01242, Sect. III.1.2]. Common-mode gain
  drifts between daily calibrations are regressed on the outside temperature
  (susceptibility 0.07%/K at 400 MHz to 0.2%/K at 800 MHz), which improves
  the stability from about 0.8% to 0.5% [src: arXiv:2202.01242, Sect.
  III.2.4, Eq. 2]. Bandpass structure that couples with bright sources and
  evades the delay filter is fitted afterwards, source by source, with
  catalogue-based templates (HyFoReS) [src: CHIME Collaboration 2025,
  arXiv:2511.19620, Sect. III.3, Eqs. 20–22].
- MeerKAT in interferometric mode: CASA-based flagging (tfcrop, rflag, a 50
  Jy clip, persistent RFI bands at 933–960 and 1163–1310 MHz) and standard
  delay, bandpass and gain calibration on PKS B1934−638 and PKS J0252−7104
  [src: Paul et al. 2023, arXiv:2301.11943, Sect. II.1].

### Step 2. Make maps
<!-- key: step-2-make-maps -->

- Map-making estimator m̂ = (Aᵀ N⁻¹ A)⁻¹ Aᵀ N⁻¹ d with A the pointing matrix and
  N the time-domain noise covariance, taken diagonal with a per-dish variance;
  the pixel variance n̂ = (Aᵀ N⁻¹ A)⁻¹ gives the inverse-variance weight; 0.25°
  pixels in the pilot [src: arXiv:2206.01579, Sect. 2, Eqs. 1–2]. The 2026
  deep field uses zenith-equal-area pixels of 0.3°, "approximately one-third
  of the beam size", and weights from normalised time-stamp counts, an
  inverse-noise-variance weighting [src: arXiv:2610.12158, Sects. 2 and 2.1].
- The pilot also subtracted the mean signal every 220 s to suppress very slow
  gain drifts, accepting a possible loss of large-angle HI that was assumed
  sub-dominant and not reconstructed [src: arXiv:2206.01579, Sect. 2].
- Noise level by the "ABBA" difference of four neighbouring channels, used
  to characterise the subsets and not in the fit, because subset
  cross-spectra remove the noise bias [src: arXiv:2610.12158, Sect. 2.2].
- Interferometric peers. CHIME builds "deconvolved ringmaps", a map-making
  technique "tailored to CHIME, or effectively any transit radio
  interferometer" of north–south cylinders, by beamforming in the
  north–south direction on the baseline grid (cylinder spacing 22.0 m, feed
  spacing 0.3048 m) [src: arXiv:2202.01242, Sect. IV.3]. MeerKAT in
  interferometric mode makes no map: visibilities are gridded in (u, v),
  delay-transformed per uv pixel with a Blackman–Harris window to limit
  foreground leakage to high k_∥, and k_∥ = 2πτν₂₁H(z)/[c(1 + z)²] [src:
  arXiv:2301.11943, Sect. III.2]. Tianlai's cylinder pathfinder reconstructs
  sky maps from 20 days of drift scans with a drone-measured primary beam,
  which the authors find "significantly enhances reconstruction accuracy over
  previous analytical approximations" [src: Deng et al. 2026,
  arXiv:2604.27465, abstract].

### Step 3. Split the data into independent subsets
<!-- key: step-3-split-the-data-into-independent-subsets -->

Shuffle the block order, then split by block and by dish into four subsets
of comparable hit counts, run the last map-making level on each, and treat
each subset independently in cleaning and power-spectrum estimation. The
reason for shuffling: block-dependent systematics "may remain correlated
between blocks observed under similar conditions"; grouping them would make
the contamination more coherent within a subset [src: arXiv:2610.12158, Sect.
2.1]. In the chess-board split, two pairs share dishes, two share blocks, and
two (A–C, B–D) share neither and are "the most independent".

The other experiments split in time. GBT used four sub-season maps A–D of
similar depth and coverage, determined the foreground modes separately for
each side of a pair, and averaged the six cross-pairs [src: Switzer et al.
2013, arXiv:1304.3712, Sect. 2.3]. CHIME splits its 94 nights into even and
odd subsets and cross-correlates them [src: CHIME Collaboration 2025,
arXiv:2511.19620, Sect. VII.2]. MeerKAT in interferometric mode crosses even
and odd cubes, which "removes the noise bias ... and it is also useful to
minimize the impact of any time-dependent systematics" [src: Paul et al.
2023, arXiv:2301.11943, Sect. III.2].

### Step 4. Decide on beam reconvolution
<!-- key: step-4-decide-on-beam-reconvolution -->

| Analysis | Choice | Reason given | Place read |
|---|---|---|---|
| MeerKLASS pilot 2022 | weighted Gaussian reconvolution to γ θ_FWHM(ν_min) with γ = 1.2 (1.82°), kernel K = exp{−Δθ²/[2(γσ²_max − σ²(ν))]}, weights reconvolved to stay inverse variances (Eqs. 16–18); GBT used γ = 1.4 | simulations show Gaussian resmoothing does not help blind cleaning even for a Gaussian beam, but on real data it "homogenise[s] some of the systematic contributions from e.g. residual RFI or polarisation leakage"; smaller γ because the MeerKAT beam is already large | arXiv:2206.01579, Sect. 4.1 |
| MeerKLASS deep field 2024 | reconvolution kept | "slightly improves the foreground clean"; the smoothing makes pixel spectra smoother by suppressing systematics, not necessarily by homogenising resolution | arXiv:2407.21626, App. B.1 |
| MeerKLASS auto-spectrum 2026 | no reconvolution | recent work finds it "detrimental": it changes the cube in a frequency-dependent way and increases mode mixing between foreground and signal in the linear decomposition PCA assumes | arXiv:2610.12158, Sect. 11.6 |

The beam then enters the model only as a Gaussian transverse damping at the
median frequency (Step 7), which neglects its frequency dependence, side
lobes and asymmetry [src: arXiv:2610.12158, Sect. 11.6].

GBT's reason for its γ = 1.4 was polarisation: the leakage beam "mixes ~10% of
polarization to intensity", is antisymmetric about the boresight and slightly
broader than the primary beam, and Faraday rotation adds spectral structure;
convolving to 1.4 times the 700 MHz beam mitigates this and the
frequency-dependent Stokes I beam, at the cost of halving the number of
independent resolution elements, viable because GBT has "roughly twice the
resolution needed" for linear scales [src: Switzer et al. 2013,
arXiv:1304.3712, Sect. 2.2]. The interferometric
MeerKAT analysis enters the beam through the power-squared beam area
Ω_ps = ∫ A²(l, m) dl dm from the eidos beam model [src: Paul et al. 2023,
arXiv:2301.11943, Sect. III.2, Eq. 2].

### Step 5. Remove foregrounds and choose N_fg
<!-- key: step-5-remove-foregrounds-and-choose-nfg -->

- PCA on the weighted frequency covariance C = (w ∘ X)(w ∘ X)ᵀ/(n_θ − 1),
  eigen-decomposed, with the first N_fg eigenvectors as mixing matrix A and
  X_clean = X − A Aᵀ X; the weights are constant in frequency "to avoid
  increasing the rank" of the data [src: arXiv:2407.21626, Sect. 4.3, Eqs.
  27–31]. N_fg = 10 in that analysis.
- Multiscale PCA (2026): starlet wavelet split of each subset into large and
  small angular scales, PCA on each with its own N_fg,L and N_fg,S, sum of the
  two cleaned cubes (Eqs. 6–7). The stated reason: systematics break the
  spectral smoothness of foregrounds, and separating scales eases the split
  between the smooth astrophysical regime and the corrupted one; each subset
  is cleaned separately because different systematics act in each [src:
  arXiv:2610.12158, Sect. 3].
- Choice of N_fg. Clean on a grid of (N_fg,L, N_fg,S) per subset, fit each
  subset cross-spectrum with the amplitude only and β = 0 (no loss term, "to
  avoid being prone to over-cleaning and large reconstruction from the β
  correction"), and keep the set that maximises S/N with χ²_red inside its 68%
  range; one set per subset across all its cross-spectra; the lowest N_fg
  when several are equivalent; then free β and check that amplitudes and χ²
  do not move [src: arXiv:2610.12158, Sect. 8]. Adopted values: N_fg,L = 11,
  11, 10, 8 and N_fg,S = 11, 10, 9, 10 for the four subsets [src:
  arXiv:2610.12158, Table 3]. Low-S/N combinations can give χ²_red ≲ 1 with an
  amplitude near zero; the fitted amplitude is used to reject them.
- First check of the cleaning: the frequency–frequency correlation matrix of
  each cleaned cube, expected diagonal beyond 2–3 MHz (~10 channels); off-
  diagonal terms below 15%, 2.5% on average [src: arXiv:2610.12158, Sect. 3].

Peers for this step:

- GBT, SVD of a cross-covariance. The noise-inverse-weighted cross-variance
  C_AB = (W_A ∘ M_A)(W_B ∘ M_B)ᵀ/N_θ of two sub-season maps is decomposed by
  SVD, its left and right vectors cleaning A and B; the weights are made
  separable, "so rank-1, so that it does not increase the map rank" [src:
  Switzer et al. 2013, arXiv:1304.3712, Sect. 2.1]. The limit is "not from the
  number of degrees of freedom along the line of sight, but ... the number of
  independent angular resolution elements", with the rule of thumb T ~ [(1 −
  N_m/N_ν)(1 − N_m/N_res)]² for the signal transfer; the fields had ~70 and ~30
  resolution elements [src: arXiv:1304.3712, Sect. 2.1].
- GBT, choice of the mode number. The optimum "coincides with the most
  stringent upper bound from the auto-power spectrum": the wide field shows a
  minimum from 20 to 30 modes and 30 are removed; the deep field's minimum is
  at 15 but 10 are removed, "conservatively", because the optimum concerns
  an ensemble of surveys and one survey may scatter low [src:
  arXiv:1304.3712, Sect. 2.1]. MeerKLASS instead maximises the S/N of the
  cross-spectrum fit under a χ² condition (above).
- GBT × eBOSS, FastICA. Idealised simulations need N_IC ≥ 4; on
  systematics-dominated data more components also remove non-Gaussian and
  anisotropic systematics, at the risk of HI loss, which a transfer function
  from 100 injected lognormal mocks corrects [src: Wolz et al. 2021,
  arXiv:2102.04946, Sect. 3.2].
- FAST: SVD subtraction of 20 modes lowers the 1/f knee frequency in a 10 MHz
  band to 1.8 × 10⁻³ Hz; the residual 1/f is then uncorrelated in frequency
  [src: Hu et al. 2021, arXiv:2109.06447, abstract].
- CHIME, filtering in delay. Point sources are 10³–10⁵ times the signal; each
  map pixel is high-pass filtered along frequency with a DAYENU filter built
  from the covariance C_mn = ε⁻¹ sinc[2πτ_cut(ν_m − ν_n)] + δ_mn, pseudo-
  inverted with the 47.2% of masked channels zeroed, its weights propagated
  [src: CHIME Collaboration 2022, arXiv:2202.01242, Sect. IV.5, Eqs. 52–56].
  The delay cut is chosen empirically: the "aggressive" cut is the lowest
  delay where P_data/P_noise < 3; four cuts 25–100 ns below it were pushed
  through the pipeline on data and on a simulated signal, and the cut minus
  75 ns gave the highest S/N [src: arXiv:2202.01242, Sect. IV.5, Fig. 9].
  The 2025 auto-spectrum filters each 9.94 s integration before time
  averaging (L2) and adds HyFoReS for residual bandpass leakage [src:
  arXiv:2511.19620, Sects. III.2.3 and III.3].
- Tianlai: multiscale PCA in wavelet domains on the sphere (mPCA-UWTS), with
  foregrounds about five orders of magnitude above the signal; MeerKLASS's
  mPCA is the flat-cube analogue [src: Deng et al. 2026, arXiv:2604.27465,
  abstract].
- MeerKAT interferometric, avoidance not removal. Foregrounds are left in the
  wedge; low-level broadband RFI or mutual coupling that shows as peaks
  outside the wedge, concentrated near zero fringe rate, is flagged per
  antenna pair and per 15-min scan at 5σ above thermal noise (BLF), or on the
  gridded uv–τ cube (UVDF) [src: Paul et al. 2023, arXiv:2301.11943, Sects.
  IV.2–IV.3]. BLF gives 3.2σ and 3.5σ at z ≈ 0.32 and 0.44; UVDF raises them
  to 5.9σ and 9.18σ [src: arXiv:2301.11943, abstract].

### Step 6. Estimate cross-spectra and their covariance
<!-- key: step-6-estimate-cross-spectra-and-their -->

- Cross-spectra between subsets, never auto-spectra of a subset, enter the
  detection [src: arXiv:2610.12158, Sects. 5 and 2.2].
- Jackknife covariance: 224 contiguous sub-cubes in R.A., Dec. and frequency,
  delete-one replicas with the mask also applied to window and weights;
  Σ = [(N_jack − 1)/(N_jack − n_k − 2)] [(N_jack − 1)/N_jack] Σ_J (P̂^J − ⟨P̂⟩)(P̂^J
  − ⟨P̂⟩)ᵀ, the first factor the Hartlap correction, the second for the
  non-independence of replicas (Eq. 12) [src: arXiv:2610.12158, Sect. 6].
- Gaussian comparison: Σ_G = (P̂_ii P̂_jj + P̂_ij P̂_ji)/N_k (Eq. 13). The jackknife
  errors are larger at all scales; built instead from the model signal plus
  ABBA noise, the Gaussian errors are much tighter at large scales, which
  shows that the measured auto-spectra carry excess power from residual
  contaminants; the jackknife is kept because it captures that budget and
  the bin correlations (≈ 30% between the second and third k bins, ≈ 10% for
  other neighbours) [src: arXiv:2610.12158, Sect. 6].

Peers for this step:

- GBT estimator: the optimal quadratic estimator of Liu & Tegmark 2011 on
  weighted, cleaned sub-season maps, cross-pairs only, binned in (k_⊥, k_∥),
  with the weighted mean of each frequency slice removed [src: Switzer et al.
  2013, arXiv:1304.3712, Sect. 2.3].
- GBT × eBOSS covariance: from the cross-correlation of the cleaned GBT data
  with 100 WiggleZ random catalogues, which includes cosmic variance and noise;
  at small k the analytic error from the measured auto-spectra is larger than
  the covariance-based one, and both converge at small scales; FastICA adds no
  significant correlation between k modes in the injected lognormals [src:
  Wolz et al. 2021, arXiv:2102.04946, App. B].
- CHIME stacking: the noise covariance of the stack is the sample covariance
  of stacks on 10 000 mock catalogues drawn without replacement from the eBOSS
  random catalogues, because the propagated radiometric noise misses residual
  foregrounds, RFI and the frequency coupling of the filter, which shows as a
  sinc-like covariance between frequency offsets [src: CHIME Collaboration
  2022, arXiv:2202.01242, Sect. IV.8, Fig. 12].
- CHIME auto-spectrum: delay spectra by a matched-filter, inverse-covariance
  transform whose forward operator R = W G H F includes the mask and the
  foreground filter, to keep compact k_∥ windows [src: CHIME Collaboration
  2025, arXiv:2511.19620, Sect. V.1, Eqs. 50–54]; noise covariance from 1000
  Monte Carlo noise realisations passed through the even × odd estimator,
  off-diagonal correlations ≲ 15% [src: arXiv:2511.19620, Sect. V.4, Eq. 73].
  Stated limits: ≲ 10% errors in single k_y bins, rebinning correlations not
  modelled, a frequency-independent sky-noise template; the realisations match
  the jackknife-measured noise to ≲ 10% [src: arXiv:2511.19620, Sect. V.4,
  "Limitations"].

Three practices side by side: MeerKLASS keeps a data jackknife because a
Gaussian or model-based covariance misses residual contaminants (above);
CHIME's auto-spectrum builds its covariance from noise simulations and checks
it against a jackknife; the cross-correlation analyses (GBT × WiggleZ/eBOSS,
CHIME stacks) stack or cross the real map on random catalogues, which CHIME
adopts because the residual foregrounds and RFI are in the map.

### Step 7. Fit the model
<!-- key: step-7-fit-the-model -->

- Theory: P^th = T̄²_HI (b_HI + f μ²)² P_m(k), with T̄_HI = 180 h Ω_HI (1 + z)²/
  [H(z)/H₀] mK ≡ Ω_HI A_HI (Eqs. 14–15); with matter-only RSD it becomes
  A²_HI (Ω_HI b_HI)² (1 + f μ²)² P_m (Eq. 17), so with cosmology fixed only Ω_HI
  b_HI is free. No non-linear bias, clustering or fingers of God "given the
  signal-to-noise ratio" [src: arXiv:2610.12158, Sect. 7].
- Beam: B_beam = exp[−½ (1 − μ²) k² R_b²], R_b = d_c(z_eff) θ_FWHM/√(8 ln 2),
  θ_FWHM = c/(ν_med D_dish), D_dish = 13.5 m (Eqs. 18–19); it damps 70% at k ≳
  0.15 h Mpc⁻¹ [src: arXiv:2610.12158, Sects. 7.1 and 11.6].
- Observed spectrum: P_ij^obs = Q_ij ⊛ {D_ij(k) [B² P^th + P_TN,i δ_ij]}, with B
  the product of beam, pixel and channel windows, D = (k/h Mpc⁻¹)^β applied to
  the whole spectrum including noise and not squared, because it acts on the
  power spectrum rather than on the field, and Q_ij the normalised product of
  the subsets' Fourier-space windows (Eqs. 26–28); β is subset-pair dependent
  [src: arXiv:2610.12158, Sects. 7.3 and 7.5].

Peers for this step. Where MeerKLASS models the loss with D(k), GBT corrected
it by a Monte Carlo transfer function, T(k_i) from signal simulations
injected before cleaning, squared "because cleaning is applied to both sides
of the quadratic estimator", with 300 simulations "sufficient" (Eq. 1), and a
separate beam transfer function from Gaussian simulations at the common
resolution [src: Switzer et al. 2013, arXiv:1304.3712, Sect. 2.3]. CHIME
applies the stored filter to its simulations, so the loss sits in the model
(L2). In cross-correlation with galaxies, the amplitude is
Ω_HI b_HI r, r the HI–galaxy correlation coefficient, at an effective k:
GBT × WiggleZ [0.43 ± 0.07 (stat) ± 0.04 (sys)] × 10⁻³ over 0.6 < z < 1 and
~41 deg² [src: Masui et al. 2012, arXiv:1208.0331, abstract]; with the later
GBT maps on 100 deg², at k_eff = 0.31 h Mpc⁻¹ and z ≃ 0.8, 0.58 ± 0.09 ±
0.05 (WiggleZ), 0.40 ± 0.09 ± 0.04 (eBOSS ELG) and 0.35 ± 0.08 ± 0.03 (eBOSS
LRG), × 10⁻³ [src: Wolz et al. 2021, arXiv:2102.04946, abstract]. Parkes ×
2dF (0.057 < z < 0.098, ~1300 deg²) detects the cross at 5.18σ, but at k ~
1.5 h Mpc⁻¹ the cross-power is more than six times below the ALFALFA-based
expectation (14.8σ), red galaxies correlating much more weakly than blue
ones [src: Anderson et al. 2018, arXiv:1710.00424, abstract]. Since r "is
dependent on the HI content of the optical galaxy sample", the three
GBT amplitudes are not one quantity [src: arXiv:2102.04946, abstract].

### Step 8. Validate
<!-- key: step-8-validate -->

| Test | Procedure | Pass criterion as stated | Place read |
|---|---|---|---|
| Null by shuffling | shuffle one cleaned subset in frequency or in pixels, cross with an unshuffled one, 200 times; χ² of data and of each null against Σ + Σ_null (Eqs. 31–32) | fraction of nulls exceeding χ²_data; none of 200 did, so p < 5 × 10⁻³, in both directions | arXiv:2610.12158, Sect. 10.2 |
| Signal injection | inject mock HI before cleaning, form T(k) from 200 mocks, compare P̂/T with the fitted model with D(k) (Eqs. 42–43) | χ²_inj = 9.74 (p = 0.37) and 8.25 (p = 0.51) for the two most independent pairs | arXiv:2610.12158, Sect. 10.7 |
| Beam-ripple k range removed | 8 k bins with k_min = 0.113, k_∥,min = 0.1, k_⊥,min = 0.045 h Mpc⁻¹ | consistent amplitudes, S/N almost halved | arXiv:2610.12158, Sect. 11.6 |
| Others listed in the paper | splitting strategy, patchwork tests, leakage between components, cross-correlation with non-cosmological frequencies, radial spectra, N_fg stability, galaxy cross-correlation | — (not read) | arXiv:2610.12158, Sect. 10 outline |

A shuffle in one direction kills radial or angular systematics but not both,
so passing both argues against either [src: arXiv:2610.12158, Sect. 10.2].

Peers for this step. CHIME's auto-spectrum null: each of the even and odd
subsets is halved and differenced, and the cross-spectrum of the two
differenced sets, in which a constant sky cancels and noise stays
independent, is consistent with the noise covariance [src: CHIME
Collaboration 2025, arXiv:2511.19620, Sect. VII.2, Fig. 15]. The stacking
analysis checks consistency between polarisations, between even and odd
days, beam-calibration errors and linearity [src: CHIME Collaboration 2022,
arXiv:2202.01242, Sect. VII, outline]. The interferometric MeerKAT analysis
runs foreground-scatter, signal-extraction, jackknife and null tests [src:
Paul et al. 2023, arXiv:2301.11943, Sect. V, outline; criteria not read].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Diode calibration, filtering or a joint Bayesian solution
<!-- key: diode-calibration-filtering-or-a-joint-bayesian -->

Fast scanning covers the scales of interest before gains drift; internal
references (diodes) correct drifts; time-domain filtering helps when drifts
are correlated in frequency [src: arXiv:2607.03259, Sect. 2.4]. In MeerKAT
pilot data the time-correlated component is 10–20 times the white noise at k =
0.04 Mpc⁻¹; it is partly correlated across channels, so an SVD removes 1/f
noise together with foregrounds, at the cost of 40% of the HI power at k = 0.04
Mpc⁻¹ for a 3-mode clean; map-making with the full noise covariance, 1/f
included, reduces the excess power by up to 30% against unweighted binning
[src: Irfan et al. 2023, arXiv:2302.02683, abstract]. A Gibbs-sampled joint
calibration and map-making, with noise tied to the system temperature through
the radiometer equation and a 1/f model free of spurious periodic
correlations, is demonstrated on MeerKLASS-like simulations only [src: Zhang et
al. 2025, arXiv:2509.10992, abstract].

### Standard or self-calibration
<!-- key: standard-or-self-calibration -->

Self-calibration replaces an external sky model by the data's own map and
lowers the residuals over five loops [src: arXiv:2407.21626, Sect. 2.3, Fig. 2
caption]. It adds iterations through the full pipeline; the papers read do
not quantify any signal absorbed into the gains; the SKA chapter names that
risk ("part of the signal to be erroneously absorbed into the calibration
solutions") for sky-model-based interferometric calibration [src:
arXiv:2607.03259, Sect. 2.4].

### PCA or multiscale PCA
<!-- key: pca-or-multiscale-pca -->

PCA with one N_fg per cube is the 2022–2024 practice; mPCA adds a second
parameter per scale and per subset, and is chosen because systematics couple
with foregrounds differently at large and small angular scales [src:
arXiv:2407.21626, Sect. 4.3; arXiv:2610.12158, Sect. 3]. Both remove signal;
the 2026 analysis models the loss, the 2022–2024 ones corrected it with a
transfer function (L2).

### Jackknife or Gaussian or mock covariance
<!-- key: jackknife-or-gaussian-or-mock-covariance -->

Jackknife covariance is data-driven and includes residual systematics; it is
"suitable for quantifying the detection significance" and for constraints
within the observed volume [src: arXiv:2610.12158, Sect. 6]. The Gaussian
form with measured auto-spectra already absorbs excess power and is close to
the jackknife on the diagonal; with model auto-spectra it underestimates the
errors at large scales [src: arXiv:2610.12158, Sect. 6].

### Remove in frequency covariance or filter in delay
<!-- key: remove-in-frequency-covariance-or-filter-in-delay -->

Blind decompositions (PCA, SVD, FastICA, mPCA) learn the foreground modes
from the data, remove signal on all scales and need a transfer function or a
loss model; their efficacy is limited by the number of angular resolution
elements (Step 5) [src: arXiv:1304.3712, Sects. 2.1 and 2.3]. CHIME's delay
filter fixes the removed region (τ < τ_cut) in advance and is applied to the
simulations as well, but couples all channels, which shows as a sinc-shaped
frequency covariance (Step 6) [src: arXiv:2202.01242, Sects. IV.5 and IV.8].
Avoidance, in the interferometric MeerKAT analysis, keeps only modes outside
the wedge and flags what contaminates them (Step 5) [src: arXiv:2301.11943,
Sect. IV.2].

### Auto-spectrum or cross-correlation with galaxies
<!-- key: auto-spectrum-or-cross-correlation-with-galaxies -->

The first detections were cross-correlations with galaxies (GBT × WiggleZ
and eBOSS, Parkes × 2dF, MeerKAT × WiggleZ, CHIME stacks on eBOSS), whose
amplitude carries r, the HI–galaxy correlation coefficient (Step 7) [src:
arXiv:1208.0331; arXiv:2102.04946; arXiv:1710.00424; arXiv:2206.01579;
arXiv:2202.01242, abstracts]; Parkes × 2dF finds a strong small-scale
decrement, read as weak HI clustering, a small r, or both [src:
arXiv:1710.00424, abstract]. The interferometric MeerKAT paper states the
contrast: "So far, detections have only been achieved through
cross-correlations with galaxy surveys" [src: arXiv:2301.11943, abstract].
An auto-spectrum constrains Ω_HI b_HI without r (Step 7).

### Single-dish or interferometer for SKA
<!-- key: single-dish-or-interferometer-for-ska -->

Interferometers correlate out 1/f noise but need per-antenna gains; SKA arrays
will need sky-based calibration with large, iteratively built sky models,
since existing catalogues are not complete enough [src: arXiv:2607.03259,
Sect. 2.4]. Single-dish SKA-Mid must deal with a heterogeneous array of
MeerKAT, MeerKAT+ and SKA-Mid dishes with different beams, "yet to be explored
in practice" [src: arXiv:2607.03259, Sect. 2.5].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Diode cadence | every 20 s | MeerKLASS | arXiv:2206.01579; arXiv:2610.12158 | Sect. 2 |
| Gain model | 4th-order polynomial in time | MeerKLASS deep field | arXiv:2407.21626 | Sect. 2.2 |
| Self-calibration | 5 loops; sky model where > 40 hits | MeerKLASS deep field | arXiv:2407.21626 | Sect. 2.3 |
| Channels kept | 252 of 4096 (δν = 0.209 MHz), 971.2–1023.6 MHz, z = 0.388–0.463, z_eff = 0.42 | MeerKLASS 2026 | arXiv:2610.12158 | Sect. 2 |
| Field | 330° < R.A. < 360°, −36° < Dec. < −25.6°, ≈ 236 deg², 133 × 73 pixels; ~30% of pixels trimmed | MeerKLASS 2026 | arXiv:2610.12158 | Sect. 2, Fig. 1 caption |
| Pilot | 10.5 h, 7 blocks over 6 nights, ~200 deg², 199 channels at 973.2–1014.6 MHz (32 more removed) | MeerKLASS 2022 | arXiv:2206.01579 | Sect. 2 |
| Reconvolution | γ = 1.2, common FWHM 1.82° (GBT: γ = 1.4) | MeerKLASS 2022 | arXiv:2206.01579 | Sect. 4.1 |
| N_fg | 10 (PCA, 2024); 8–11 per scale and subset (mPCA, 2026) | MeerKLASS | arXiv:2407.21626; arXiv:2610.12158 | Sect. 4.3; Table 3 |
| Cleaned-cube frequency correlations | < 15% off-diagonal, 2.5% mean | MeerKLASS 2026 | arXiv:2610.12158 | Sect. 3 |
| Jackknife sub-cubes | 224 | MeerKLASS 2026 | arXiv:2610.12158 | Sect. 6 |
| 1/f vs white noise | 10–20 times at k = 0.04 Mpc⁻¹ | MeerKAT pilot | arXiv:2302.02683 | abstract |
| SVD 1/f + foreground clean | 40% HI power lost at k = 0.04 Mpc⁻¹ for 3 modes | simulation | arXiv:2302.02683 | abstract |
| Null tests | 200 shuffles per direction; p < 5 × 10⁻³ | MeerKLASS 2026 | arXiv:2610.12158 | Sect. 10.2 |
| Injection | 200 mocks; χ²_inj p = 0.37 and 0.51 | MeerKLASS 2026 | arXiv:2610.12158 | Sect. 10.7 |
| Absolute calibration | 9% (point sources) | GBT 2013 | arXiv:1304.3712 | Sect. 2 |
| Polarisation leakage | ~10% of polarisation into intensity | GBT | arXiv:1304.3712 | Sect. 2.2 |
| Modes removed | 30 (wide), 10 (deep; optimum 15) | GBT auto 2013 | arXiv:1304.3712 | Sect. 2.1 |
| Transfer-function simulations | 300 | GBT auto 2013 | arXiv:1304.3712 | Sect. 2.3 |
| Thermal gain susceptibility | 0.07%/K (400 MHz) to 0.2%/K (800 MHz); stability 0.8% → 0.5% | CHIME | arXiv:2202.01242 | Sect. III.2.4 |
| Band masked before the delay filter | 47.2% | CHIME stack | arXiv:2202.01242 | Sect. IV.5 |
| Delay cut | aggressive cut (P_data/P_noise < 3) minus 75 ns | CHIME stack | arXiv:2202.01242 | Sect. IV.5 |
| Stack noise covariance | 10 000 random mock catalogues | CHIME stack | arXiv:2202.01242 | Sect. IV.8 |
| Auto noise covariance | 1000 realisations; off-diagonal ≲ 15% | CHIME auto | arXiv:2511.19620 | Sect. V.4 |
| FAST 1/f knee | 1.8 × 10⁻³ Hz after 20 SVD modes; ~6 × 10⁻⁴ Hz after 30; 10% bias on P(k) | FAST pilot | arXiv:2109.06447 | abstract |
| Ω_HI b_HI r | 0.43 ± 0.07 ± 0.04 × 10⁻³ (WiggleZ, 2013); 0.58 ± 0.09 ± 0.05, 0.40 ± 0.09 ± 0.04, 0.35 ± 0.08 ± 0.03 × 10⁻³ (WiggleZ, ELG, LRG; k_eff = 0.31 h Mpc⁻¹) | GBT cross | arXiv:1208.0331; arXiv:2102.04946 | abstract of each |
| Parkes × 2dF | 5.18σ; > 6× below expectation at k ~ 1.5 h Mpc⁻¹ (14.8σ) | Parkes | arXiv:1710.00424 | abstract |
| Interferometric auto detection | 3.2σ, 3.5σ (BLF); 5.9σ, 9.18σ (UVDF) at z ≈ 0.32, 0.44 | MeerKAT interferometric | arXiv:2301.11943 | abstract |
| Stacking systematic | ν_sys = 17.90 (+6.53/−4.27) MHz, A_sys = 0.50 ± 0.33 (prior-limited) | MeerKLASS × GAMA stack | arXiv:2504.03908 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- Gain non-linearity near a transmitter. "Zebra stripes": a time-dependent
  gain non-linearity as dishes scan past a bright out-of-band transmitter on
  the horizon, giving large ripples in the maps [src: arXiv:2607.03259, Sect.
  2.5].
- Beam chromaticity. Ripples of the beam width with frequency, linked to
  standing waves between the dish panels and the feed, convolve smooth ground
  pickup and synchrotron into frequency structure that PCA cannot isolate;
  ground pickup is handled by constant elevation [src: arXiv:2607.03259, Sect.
  2.5]. In the stacked spectrum it appears as an oscillation matching
  diffraction from the secondary reflector [src: Chen et al. 2025,
  arXiv:2504.03908, abstract]. The 2026 auto-spectrum sees no ripple peak in
  its radial spectra near k_ν ≈ 0.05 MHz⁻¹, which the authors attribute,
  speculatively, to cross-correlating subsets cleaned independently, since
  standing waves are dish- and elevation-dependent [src: arXiv:2610.12158,
  Sect. 11.6].
- Plane-parallel projection. A beam purely transverse to the local line of
  sight leaks into radial modes once projected onto one global line of sight;
  a frequency-dependent beam couples transverse and radial modes [src:
  arXiv:2610.12158, Sect. 11.6].
- Correlated systematics inside a subset. Avoided by shuffling blocks before
  splitting (Step 3) [src: arXiv:2610.12158, Sect. 2.1].
- Over- or under-cleaning. Too high an N_fg increases loss, too low leaves
  residuals [src: arXiv:2407.21626, Sect. 4.3]; past the "cleaning sweet spot"
  the cross-spectrum amplitude falls towards zero [src: arXiv:2610.12158, Sect.
  8].
- Signal loss outside the cleaning. Bandpass calibration may also remove
  signal; "investigations are ongoing" [src: arXiv:2610.12158, Sect. 7.3,
  footnote 5]. Mean subtraction every 220 s in the pilot removed large-angle
  power that was not reconstructed [src: arXiv:2206.01579, Sect. 2].
- Covariance scope. The jackknife covariances are "suitable for quantifying
  the detection significance of our measurements and for constraining
  physical quantities within the observed volume"; the paper then lists
  uncertainties they do not include, a list cut off in the rendering read
  [src: arXiv:2610.12158, Sect. 6, final paragraph].

## Reading list
<!-- key: reading-list -->

- Method, review: Wolz et al. 2026, arXiv:2607.03259 (SKA HI surveys,
  calibration, SKA systematics).
- MeerKLASS single dish: MeerKLASS Collaboration 2024, arXiv:2407.21626
  (diode model, self-calibration, weighted PCA); 2026, arXiv:2610.12158
  (subsets, mPCA, N_fg, jackknife, loss model, validation); Cunnington et al.
  2022, arXiv:2206.01579 (pilot, reconvolution); Cunnington et al. 2023,
  arXiv:2302.07034 (transfer function); Irfan et al. 2023, arXiv:2302.02683
  (1/f); Chen et al. 2025, arXiv:2504.03908 (beam ripple); Zhang et al. 2025,
  arXiv:2509.10992 (joint Bayesian calibration).
- Other single dishes: Switzer et al. 2013, arXiv:1304.3712 (GBT auto:
  sub-season crosses, SVD, transfer function); Hu et al. 2021,
  arXiv:2109.06447 (FAST 1/f).
- Detections in cross-correlation: Masui et al. 2012, arXiv:1208.0331 (GBT ×
  WiggleZ); Wolz et al. 2021, arXiv:2102.04946 (GBT × eBOSS, FastICA);
  Anderson et al. 2018, arXiv:1710.00424 (Parkes × 2dF).
- Interferometers: CHIME Collaboration 2022, arXiv:2202.01242 (calibration,
  ringmaps, DAYENU, stack covariance) and 2025, arXiv:2511.19620 (auto,
  HyFoReS, noise Monte Carlo); Paul et al. 2023, arXiv:2301.11943 (MeerKAT
  interferometric, avoidance, flagging); Deng et al. 2026, arXiv:2604.27465
  (Tianlai, drone beam, wavelet PCA).

## Not verified
<!-- key: not-verified -->

- Wang et al. 2021 (the KATcali calibration paper) is described here through
  the 2022, 2024 and 2026 MeerKLASS papers; its identifier was not retrieved
  and its body not read.
- Matshawule et al. 2021, Spinelli et al. 2022 and Carucci et al. 2025 (the
  reconvolution and mPCA studies cited by arXiv:2610.12158) were not read.
- Sects. 10.1 and 10.3–10.11 of arXiv:2610.12158 (splitting, patchwork,
  leakage, radial and N_fg-stability tests) were not read; their pass criteria
  are not recorded.
- HIRAX and CHORD have no power-spectrum analysis read; their hardware
  status is in L2 (`surveys-and-data.md`). Tianlai was read in its abstract
  only. The CHIME primary-beam deconvolution and beam calibration (Sects.
  IV.3.3, IV.4 of arXiv:2202.01242) were not read.
- FAST HI intensity-mapping power spectra (beyond the 1/f study) were not
  searched for this run.
