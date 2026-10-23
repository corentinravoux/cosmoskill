# Physics and methods — reionisation, 21 cm, line-intensity mapping

Scope: observables, estimators, models and codes for reionisation, 21 cm and line mapping.
Snapshot: 2026-10-13

Numbers carry [src] (read in the cited paper this session), [sec] (taken from the named
secondary source) or [der] (derived here, derivation stated).

## 1. Reionisation observables
<!-- key: reionisation-observables -->

### 1.1 Thomson optical depth
<!-- key: thomson-optical-depth -->

- Definition (textbook): τ is the line-of-sight integral of n_e σ_T from today to recombination.
  Free electrons after reionisation rescatter the CMB quadrupole and create the low-ℓ EE
  "reionisation bump"; they also damp the primary anisotropies by e^(−2τ), so high-ℓ data
  constrain the product A_s e^(−2τ) and not τ.
- As Planck writes it: τ = n_H(0) c σ_T ∫₀^{z_max} dz x_e(z) (1 + z)² / H(z), with x_e ≡
  n_e^reion/n_H and z_max = 50. Helium is singly ionised with hydrogen, so a complete first
  reionisation has x_e > 1; the second helium ionisation is a fixed smooth step at z = 3.5. The
  bump at ℓ ≲ 30 has an amplitude that "scales like τ²", and its shape carries x_e(z) [src:
  Planck Collaboration 2018, arXiv:1807.06209, Eq. 83 and Sect. 7.8].
- Foundations. Zaldarriaga 1997, arXiv:astro-ph/9608050: reionisation adds large-angle
  polarisation peaks whose position scales as the square root of the reionisation redshift
  and whose amplitude scales with τ [src]. First detection: the WMAP first-year TE excess
  (Kogut et al. 2003, arXiv:astro-ph/0302213; value in section 7 of `results.md`). Midpoint
  parametrisation: appendix of Lewis 2008, arXiv:0804.3865 [src]. Model-independent
  alternative, five principal components of x_e(z): Hu & Holder 2003, arXiv:astro-ph/0303400
  [src].
- The tanh model "is not physically motivated, but makes the optical depth approximately
  independent of the transition width"; Planck fixes the width to Δz = 0.5. In the Planck
  reionisation section a Gunn–Peterson bound is imposed (tanh centre above z = 6.5), which gives
  a floor τ ≳ 0.0430; a free-form "FlexKnot" history with knots at z > 6 can reach τ = 0.0385
  [src: arXiv:1807.06209, Sect. 7.8].
- Consequence used in every 2025–2026 debate: without low-ℓ polarisation, τ is fixed only
  through CMB lensing and BAO, and it is negatively correlated with the matter fraction [src:
  Sailer et al. 2025, arXiv:2504.16932].
- Parametrisations in use. (i) The "instantaneous" tanh transition, the default of Planck
  analyses [src: Planck Collaboration 2016, arXiv:1605.03507]. (ii) Symmetric and asymmetric
  transitions fitted with kSZ information [src: arXiv:1605.03507]. (iii) A Gompertz form
  calibrated on simulations, asymmetric by construction [src: Montero-Camacho & Mao 2026,
  arXiv:2607.26373]. (iv) tanh plus a transient high-redshift "flash" [src: Upadhyay et al.
  2026, arXiv:2609.24989].
- τ maps to a midpoint only inside a parametrisation: τ = 0.059 ± 0.006 gives z_re = 8.14 ± 0.61
  for tanh [src: Pagano et al. 2019, arXiv:1908.09856]; the Planck 2016 models give mean
  redshifts between 7.8 and 8.8 and an ionised fraction below 10% above z ~ 10 [src:
  arXiv:1605.03507].
- Likelihoods for the low-ℓ EE data are not Gaussian and are built from simulations: the
  simulation-based likelihood (SimBaL) of the Planck legacy papers, the maximum-entropy
  "momento" likelihood and a density-estimation scheme give consistent τ on SRoll2 maps [src: de
  Belsunce et al. 2021, arXiv:2103.14378]. Details belong to `cosmo-cmb`.
- How the simulation-based likelihood is built. Planck 2018 "lowE" (SimAll): EE only, ℓ ≤ 29,
  an empirical distribution from 300 end-to-end simulations of HFI noise and residual
  systematics, off-diagonal correlations ignored; low-ℓ TE is excluded for unexplained excess
  variance at ℓ = 5, 18 and 19 [src: arXiv:1807.06209, Sect. 2.2.3]. SRoll2: the 100 × 143 GHz
  EE cross-spectrum over ℓ = 2–29 on a 50% mask; 101 model spectra over τ = [0, 0.1] at fixed
  10⁹ A_s e^(−2τ) = 1.875, 500 signal maps each added to noise and systematics simulations,
  probabilities histogrammed per ℓ and multiplied, neglecting correlations between multipoles
  [src: Pagano et al. 2019, arXiv:1908.09856, Sect. 4, Eq. 2].

### 1.2 Lyman-series absorption in quasar spectra
<!-- key: lyman-series-absorption-in-quasar-spectra -->

- Gunn–Peterson trough. Origin: Gunn & Peterson 1965, doi:10.1086/148444 (title and authors
  confirmed on Crossref; not read). Lyα saturates for a neutral fraction ≳ 0.01%, depending
  on density and temperature [src: Bosman et al. 2022, arXiv:2108.03699, Sect. 1]; hence "the
  existence of the Gunn-Peterson trough by itself does not indicate that the quasar is
  observed prior to the reionization epoch" [src: Becker et al. 2001, arXiv:astro-ph/0108097,
  the first complete trough]. Reference sample of the 2000s: Fan et al. 2006,
  arXiv:astro-ph/0512082. Review: Fan, Bañados & Simcoe 2023, arXiv:2212.06907. Their numbers
  are in section 1.4 of `results.md`.
- Patchy end. A trough ~110 h⁻¹Mpc long with τ_eff ≳ 7 reaching down to z ≃ 5.5 (ULAS
  J0148+0600) showed that the sightline scatter exceeds a uniform background [src: Becker et al.
  2015, arXiv:1407.4850]. Radiative-transfer models in which reionisation ends at z = 5.2–5.3
  with neutral islands reproduce the scatter and such troughs, with 50% of the volume ionised
  at z = 7 [src: Kulkarni et al. 2019, arXiv:1809.06374; Keating et al. 2020, arXiv:1905.12640].
- How the XQR-30 opacity measurement is made: 67 sightlines with S/N > 10 per ≤ 15 km/s pixel;
  τ_eff from the mean of F/F_cont over fixed 50 h⁻¹ cMpc intervals; rest wavelengths above 1185
  Å excluded as proximity zone; continuum predicted from the red side by a PCA; segments with
  damped absorbers, found through their metal lines, removed; bootstrap errors over
  sightlines; maximum-likelihood comparison with the Sherwood and Nyx homogeneous-background
  simulations [src: arXiv:2108.03699, Sects. 2–3 and 5].
- Dark-pixel fraction, origin. Proposed as "a simple, nearly model-independent upper limit" on
  x_HI by Mesinger 2010, arXiv:0910.4161 [src]; first applied by McGreer, Mesinger & Fan 2011,
  arXiv:1101.3314, then McGreer, Mesinger & D'Odorico 2015, arXiv:1411.5375 (limits in section
  1.3 of `results.md`).
- Logic of the dark-pixel fraction: "Any spectral region showing transmission must be highly
  ionized, while dark regions could be ionized or neutral", so the dark fraction is a nearly
  model-independent upper limit on the neutral volume fraction, "modulo choices in binning scale
  and dark pixel definition" [src: Davies et al. 2025, arXiv:2510.25829]. The 2025 analysis bins
  at 3.3 comoving Mpc and uses the negative-pixel method on Lyα, Lyβ and Lyγ [src:
  arXiv:2510.25829].
- Lyβ has a lower optical depth than Lyα and is therefore more sensitive to residual neutral gas
  [src: Zhu et al. 2022, arXiv:2205.04569].
- Dark gaps: contiguous regions where the transmission averaged over 1 h⁻¹Mpc bins falls below
  5%; the statistic F₃₀ is the fraction of sightlines with a gap longer than 30 h⁻¹Mpc [src: Zhu
  et al. 2021, arXiv:2109.06295].
- Effective optical depth τ_eff = −ln⟨F⟩ over a fixed path. Its sightline-to-sightline scatter
  at z > 5.3 is "too strong to be caused by fluctuations in the density field alone" [src:
  Davies et al. 2023, arXiv:2312.08464]. Two model families fit it: residual neutral islands
  from a late end of reionisation, and a fluctuating ionising background with a short, spatially
  varying mean free path [src: arXiv:2312.08464; Zhu et al. 2021, arXiv:2109.06295].
- Inference is by forward modelling. Gaikwad et al. post-process the Sherwood simulations with
  the EX-CITE code to generate photo-ionisation-rate fluctuation models and fit the τ_eff
  distribution for the mean free path, the photo-ionisation rate and the neutral fraction [src:
  Gaikwad et al. 2023, arXiv:2304.02038]. Davies et al. use approximate Bayesian computation on
  the same statistic [src: arXiv:2312.08464].
- Mean free path of ionising photons, direct method: stack quasar spectra below the Lyman limit
  and fit the transmission profile, correcting for the quasar proximity zone [src: Zhu et al.
  2023, arXiv:2308.04614]. Units are proper Mpc.
- Origin and model of the direct method. Stacked-spectrum measurement of the Lyman-limit
  opacity: Prochaska, Worseck & O'Meara 2009, arXiv:0910.0009; extended to z ~ 5 by Worseck et
  al. 2014, arXiv:1402.4154, and to z = 6, with the quasar's own ionising flux modelled, by
  Becker et al. 2021, arXiv:2103.16610 [src]. λ_mfp is the distance over which ionising
  photons are attenuated by 1/e. The proximity effect enters as κ_LL(r) = κ_LL^bg [1 +
  Γ_qso(r)/Γ_bg]^(−ξ), with Γ_qso set by the quasar luminosity through the distance R_eq
  where it equals the background rate; foreground Lyman-series opacity (Lyα to Ly40) is taken
  from the Sherwood simulations; the nominal ξ is 0.67 [src: Zhu et al. 2023,
  arXiv:2308.04614, Sect. III, Eqs. 1–3, and Table 2].

### 1.3 Damping wings
<!-- key: damping-wings -->

- Origin: Miralda-Escudé 1998, arXiv:astro-ph/9708253, predicted the wing redward of Lyα from
  a neutral IGM, noted that a dense absorber associated with the source can hinder the
  measurement, and proposed gamma-ray-burst afterglows as sources [src]. First claims on
  quasars: Mortlock et al. 2011, arXiv:1106.6088 (z = 7.085), and Bañados et al. 2018,
  arXiv:1712.01860 (z = 7.54); limits in section 1.3 of `results.md`.
- A neutral IGM in front of a source imprints Lyα damping-wing absorption redward of the line
  centre. In stacked forest spectra the wing extends more than 1000 km/s beyond a Gunn–Peterson
  trough when x_HI ≳ 0.1 [src: Spina et al. 2024, arXiv:2405.12273]. [src: abstract]
- Quasars. The three difficulties are the stochastic patchy topology, the degeneracy with the
  quasar lifetime, and the unknown intrinsic spectrum near Lyα [src: Davies et al. 2018,
  arXiv:1802.06066]. Current pipelines predict the intrinsic continuum from the red side: a
  covariance-based reconstruction of Lyα and N V from C IV, Si IV and C III] [src: Greig et al.
  2024, arXiv:2404.12585], or a PCA model trained on 15,559 SDSS/BOSS quasars, for which six
  parameters perform best and machine-learning alternatives give no gain [src: Hennawi et al.
  2024, arXiv:2406.12070]. The PCA approach started with 12,764 BOSS quasars at z ~ 2–2.5, 10
  red-side (1280–2900 Å) and 6 blue-side (1180–1280 Å) components and a projection matrix
  between them [src: Davies et al. 2018, arXiv:1801.07679].
- What the XQR-30 damping-wing analysis did: the intrinsic Lyα + N V profile is drawn from a
  covariance matrix of emission-line parameters (three Gaussian components for the blend)
  conditioned on the red side; the wing is fitted on 1218–1230 Å against synthetic wings from
  reionisation simulations at each sampled neutral fraction, with absorption features masked;
  quasars with nearby damped absorbers or broad absorption lines are excluded (23 of 42 kept)
  [src: arXiv:2404.12585, Sects. 2.2 and 3.3–3.4, Table 1].
- Galaxies. JWST/NIRSpec prism spectra of UV-bright galaxies show a softening of the break at
  rest 1216 Å with redshift, fitted with an ionised bubble of radius R_b in an IGM of neutral
  fraction x_HI [src: Umeda et al. 2023, arXiv:2306.00487]. Local damped absorption in the
  galaxy or its circumgalactic gas is degenerate with the IGM wing at prism resolution (section
  3 of `systematics.md`).

### 1.4 Lyα emission from galaxies
<!-- key: lyalpha-emission-from-galaxies -->

- Observable: the fraction X_Lyα of UV-selected galaxies with Lyα equivalent width above a
  threshold (25 Å or 10 Å in arXiv:2609.40363), or the Lyα luminosity function. Both fall when
  the surrounding IGM is neutral.
- Origin. Lyα luminosity functions at z = 5.7 and 6.5 compared as a reionisation test, with
  no strong suppression found [src: Malhotra & Rhoads 2004, arXiv:astro-ph/0407408]. The "Lyα
  fraction" among continuum-selected dropouts, calibrated over 3 < z < 6 on more than 600
  spectra, with a tentative drop at z ~ 7 [src: Stark et al. 2010, arXiv:1003.5244]. The
  Bayesian framework in use today: reionisation simulations, empirical line profiles (velocity
  offset against UV luminosity) and the full equivalent-width distribution, upper limits
  included [src: Mason et al. 2018, arXiv:1709.05356].
- The inference needs the intrinsic (post-reionisation) equivalent-width distribution as a
  baseline, taken at z ~ 5–6 [src: Prieto-Lyon et al. 2025, arXiv:2509.18302], and a
  reionisation simulation for the transmission, for example THESAN [src: Kundu et al. 2026,
  arXiv:2609.40363].

### 1.5 Kinetic SZ
<!-- key: kinetic-sz -->

- Origin. Doppler scattering off ionised patches as an arcminute anisotropy that gives "the
  typical size of the ionized region and the duration of the reionization process": Gruzinov
  & Hu 1998, arXiv:astro-ph/9803188; analytic spectrum peaking at the angular scale of the
  ionised regions: Knox, Scoccimarro & Dodelson 1998, arXiv:astro-ph/9805012 [src]. Scalings
  used to read a duration, D_3000 ∝ ⟨z⟩ and ∝ Δz^0.47 with patchy power of 0.6–2.8 μK²:
  Battaglia et al. 2013, arXiv:1211.2832 [src]. First data limit: Zahn et al. 2012,
  arXiv:1111.6386 (section 5 of `systematics.md`). Four-point statistic separating kSZ from
  lensing and foregrounds: Smith & Ferraro 2017, arXiv:1607.01769 [src].
- The small-scale CMB temperature spectrum contains kSZ power from the late-time ionised
  Universe ("homogeneous") and from ionised bubbles during reionisation ("patchy"). Only the
  sum, D_3000^kSZ, is measured; the patchy part, and hence the duration, follows after
  subtracting an assumed late-time template [src: Chaubal et al. 2026, arXiv:2601.20551;
  Beringue et al. 2025, arXiv:2506.06274].
- Duration is defined differently in each paper: Δ⁵⁰z from x_e = 25% to 75% and Δ⁹⁰z from 5% to
  95% in SPT-3G D1 [src: arXiv:2601.20551].
- The kSZ trispectrum (a quadratic estimator on two temperature maps that reconstructs the
  large-scale velocity modulation of the small-scale kSZ) is contaminated by CMB lensing and
  foregrounds, which must be simulated and subtracted [src: Raghunathan et al. 2024,
  arXiv:2403.02337].

### 1.6 Ionising-photon budget
<!-- key: ionising-photon-budget -->

- Bookkeeping (textbook): the ionising emissivity is the UV luminosity density times the
  ionising efficiency ξ_ion times the escape fraction f_esc, balanced against recombinations set
  by a clumping factor.
- Origin. The criterion that hydrogen in a clumpy universe is reionised "when the number of
  photons emitted above 1 ryd in one recombination time equals the mean number of hydrogen
  atoms", with the filling factor of H II regions as the variable, is Madau, Haardt & Rees
  1999, arXiv:astro-ph/9809058 [src]. The clumping factor is C = ⟨ρ_b²⟩/⟨ρ_b⟩² over the
  recombining gas; photo-heating lowers it strongly, so that the z = 6 galaxy population can
  keep the IGM ionised if f_esc > 0.2 [src: Pawlik, Schaye & van Scherpenzeel 2009,
  arXiv:0807.3963]. The pre-JWST reference budget matched τ = 0.066 ± 0.012 with galaxies and a
  history confined to 6 ≲ z ≲ 10 [src: Robertson et al. 2015, arXiv:1502.02024].
- JWST values of ξ_ion with low-redshift f_esc calibrations overproduce photons [src: Muñoz et
  al. 2024, arXiv:2404.07250]; later mass-complete samples lower ξ_ion [src: Simmonds et al.
  2024, arXiv:2409.01286]; spectral fitting of f_esc object by object gives an end at z ~ 5.8
  [src: Giovinazzo et al. 2026, arXiv:2607.22834].

## 2. The 21 cm signal
<!-- key: the-21-cm-signal -->

Equations in this section are quoted from the review of Liu & Shaw 2019, arXiv:1907.08211,
section 2.1 [sec for the numbers].

- Spin temperature: n₁/n₀ = 3 exp(−h ν₂₁ / k_B T_s), with ν₂₁ ≈ 1420.406 MHz.
- Brightness temperature against the CMB: T_b = [1 − exp(−τ_HI)] (T_s − T_γ)/(1 + z), with 1 + z
  = ν₂₁/ν.
- Optical depth: τ_HI = (3 ħ c³ A₁₀ / 16 k_B ν₂₁²) x_HI n_H / [(1 + z)(dv_∥/dr_∥) T_s], with A₁₀
  = 2.85 × 10⁻¹⁵ s⁻¹. It is ≲ 4% everywhere of interest, so T_b ∝ x_HI n_H (1 − T_γ/T_s) / [(1 +
  z)² (dv_∥/dr_∥)].
- As Pritchard & Loeb 2012, arXiv:1109.6012, write them [src: Sect. 2.1, Eqs. 3–8]: n₁/n₀ =
  (g₁/g₀) exp(−T⋆/T_S), g₁/g₀ = 3, T⋆ = 0.068 K; τ_ν = ∫ ds [1 − exp(−E₁₀/k_B T_S)] σ₀ φ(ν) n₀,
  n₀ = n_H/4, σ₀ ≡ 3c²A₁₀/8πν²; δT_b = (T_S − T_R)(1 − e^(−τ_ν))/(1 + z) ≈ 27 x_HI (1 + δ_b)
  (Ω_b h²/0.023) [(0.15/Ω_m h²)(1 + z)/10]^(1/2) [(T_S − T_R)/T_S] mK, times a line-of-sight
  velocity-gradient factor; T_S⁻¹ = (T_γ⁻¹ + x_α T_α⁻¹ + x_c T_K⁻¹)/(1 + x_α + x_c), with x_α
  and x_c the Lyα (Wouthuysen–Field) and collisional couplings and T_α the Lyα colour
  temperature. The rendering read prints the gradient factor as ∂_r v_r/[(1 + z)H(z)], in the
  numerator; arXiv:1907.08211 above has dv_∥/dr_∥ in the denominator. Check before use.
- For T_s ≫ T_γ the signal no longer depends on T_s. This is the regime of post-reionisation
  intensity mapping and of late reionisation with a heated IGM.
- Origins. Lyα coupling of the spin temperature to the gas (Wouthuysen–Field effect):
  Wouthuysen 1952, doi:10.1086/106661, and Field 1958, doi:10.1109/JRPROC.1958.286741 (both
  confirmed on Crossref; not read). Its strength at high redshift, reduced by up to ~2 by
  cascades ending in two-photon decay, with fitting formulae for T_k ≥ 2 K: Hirata 2006,
  arXiv:astro-ph/0507102 [src]. 21 cm tomography of a preheated IGM seen as a patchwork of
  emission: Madau, Meiksin & Rees 1997, arXiv:astro-ph/9608010 [src]. Power-spectrum formalism
  in angle and frequency: Zaldarriaga, Furlanetto & Hernquist 2004, arXiv:astro-ph/0311514
  [src]. Reviews: Furlanetto, Oh & Briggs 2006, arXiv:astro-ph/0608032; arXiv:1109.6012.
- Global signal, origin. A sharp step in the sky spectrum at 70–240 MHz for reionisation at 5
  < z < 20, detectable in principle with a small telescope because the signal fills the sky:
  Shaver et al. 1999, arXiv:astro-ph/9901320 [src]. The first observational result was an
  EDGES all-sky spectrum over 100–200 MHz (6 < z < 13) excluding a reionisation faster than
  Δz < 0.06 at 95% [src: Bowman & Rogers 2010, arXiv:1209.1117].
- Two observables: the global (sky-averaged) spectrum T̄_b(ν), and the fluctuations, summarised
  by the dimensionless power spectrum Δ²₂₁(k) = k³ P(k)/2π² in mK².
- Frequency coverage: 47–234 MHz corresponds to z = 5.1–29.3 [src: HERA Collaboration 2025,
  arXiv:2511.21289]. [src: Sect. I]
- Sequence of epochs. Lyα photons from the first stars couple T_s to the cold gas and produce
  absorption; X-ray heating then raises the gas above the CMB temperature; reionisation removes
  the signal. EDGES read its profile edges as the onset of Lyα coupling by 180 Myr and heating
  less than 100 Myr later [src: Bowman et al. 2018, arXiv:1810.05912]. [src: abstract]
- The EDGES depth requires one of three things: gas colder than adiabatic cooling allows (for
  example dark-matter–baryon scattering), a radio background in excess of the CMB at high
  redshift, or an unmodelled systematic [src: arXiv:2511.21289, introduction; arXiv:1810.05912].
- Limits are interpreted through a galaxy-formation model. Parameters that current limits touch:
  the X-ray luminosity per star-formation rate (heating), the radio efficiency of early
  galaxies, and the minimum halo mass [src: HERA Collaboration 2022, arXiv:2210.04912; Dhandha
  et al. 2025, arXiv:2508.13761; Sims et al. 2025, arXiv:2504.09725].
- A perturbative, symmetries-based bias expansion of the 21 cm field exists for large scales and
  is the basis of **forecasts** of τ from 21 cm data [src: Sailer, Chen & White 2022,
  arXiv:2205.11504].

## 3. Post-reionisation HI intensity mapping
<!-- key: post-reionisation-hi-intensity-mapping -->

- Origin. BAO in the 21 cm brightness by three-dimensional intensity mapping, without
  resolving galaxies: Chang et al. 2008, arXiv:0709.3672 [src]. First detection: a stack of
  GBT maps on DEEP2 galaxies [src: Chang et al. 2010, arXiv:1007.3709]. The early detections
  are listed in section 3 of `surveys-and-data.md`.
- After reionisation the residual neutral hydrogen (x_HI ~ 2%) sits in self-shielded gas inside
  haloes of ~10¹⁰–10¹³ M_⊙ and is seen in emission [sec: arXiv:1907.08211, section 2.4].
- Abundance targets quoted by the same review: Ω_HI ~ (3.9 ± 0.6) × 10⁻⁴ at z < 0.06 from
  ALFALFA, and Ω_HI = 9.8 (+2.0/−1.8) × 10⁻⁴ at z = 4.9 from damped Lyα systems [sec:
  arXiv:1907.08211, section 2.4].
- Intensity mapping does not resolve galaxies: each voxel integrates the emission of many
  sources, and the angular resolution is matched to the cosmological scale of interest [sec:
  arXiv:1907.08211]. The MeerKAT beam at L-band corresponds to ~30 Mpc comoving [sec: Cunnington
  et al. 2026, arXiv:2606.25955, section 3].
- What an amplitude measures. The mean brightness temperature scales with Ω_HI, so a cross-power
  with galaxies constrains Ω_HI b_HI r [src: Masui et al. 2012, arXiv:1208.0331], and an
  auto-power constrains Ω_HI b_HI [src: MeerKLASS Collaboration 2026, arXiv:2610.12158]. CHIME
  quotes A_HI ≡ 10³ Ω_HI (b_HI + ⟨fμ²⟩) with ⟨fμ²⟩ = 0.552 for stacking [src: CHIME
  Collaboration 2022, arXiv:2202.01242] and A²_HI ≡ 10⁶ Ω²_HI (b²_HI + ⟨fμ²⟩)² for the
  auto-spectrum [src: CHIME Collaboration 2026, arXiv:2603.25680]. These are different
  combinations; they are not interchangeable.
- Two observing modes. Single-dish (each dish's auto-correlation, scanned over a wide area)
  reaches the largest scales: MeerKLASS, and the planned SKA-Mid survey [src: arXiv:2606.25955].
  Interferometers with compact redundant arrays (CHIME, Tianlai, HIRAX, CHORD) measure smaller
  transverse scales and lose low k_∥ to the foreground filter [src: arXiv:2202.01242; The CHORD
  Collaboration 2026, arXiv:2607.09374].
- BAO analysis planned for SKA: a template fit of the HI power-spectrum multipoles in α_iso and
  α_AP with a Gaussian beam term and broadband splines, as in DESI; no density-field
  reconstruction is assumed because it "has not been tested in the presence of foregrounds"
  [src: Wolz et al. 2026, arXiv:2607.03259, section 4.1].
- The sibling `cosmo-galaxy-clustering` covers BAO template and full-shape practice for
  galaxies, from which this template is adapted.

## 4. Line-intensity mapping in other lines
<!-- key: line-intensity-mapping-in-other-lines -->

- Review of record: Bernal & Kovetz 2022, arXiv:2206.15377 (target lines, modelling, statistics,
  synergies). Earlier status report, with the instrument landscape: Kovetz et al. 2017,
  arXiv:1709.09066.
- Origins. Redshifted CO and [CII] lines as a clustered signal in CMB bands, separable by
  observing at different spectral resolutions: Righi, Hernández-Monteagudo & Sunyaev 2008,
  arXiv:0805.2174 [src]. CO intensity mapping at reionisation redshifts and its cross-spectrum
  with 21 cm, less sensitive to foregrounds than either auto-spectrum: Lidz et al. 2011,
  arXiv:1104.4800 [src]. [CII] intensity mapping, with the CO interloper problem and the
  [CII] × 21 cm cross-power: Gong et al. 2012, arXiv:1107.3553 [src].
- Measurements before COMAP (COPSS, mmIME, Planck × SDSS for [CII]) are in section 4 of
  `surveys-and-data.md`.
- Model of the power spectrum (textbook form used by COMAP): a clustering term proportional to
  ⟨Tb⟩² P_m(k), with ⟨Tb⟩ the mean line temperature times bias, plus a scale-independent
  shot-noise term. COMAP quotes its constraint as ⟨Tb⟩² [src: Cleary et al. 2021,
  arXiv:2111.05927].
- Shot noise depends on the scatter of line luminosity at fixed halo mass. JWST-era burstiness
  raises it by a line-dependent factor (B_Hα ≃ 7; 2.5–3.5 for [CII], CO, UV at z ~ 6) [src:
  Kovetz et al. 2026, arXiv:2605.13967]. [src: abstract]
- Interlopers: one observed frequency contains several lines from different redshifts. For [CII]
  at reionisation redshifts the interlopers are lower-redshift CO lines, and the first CCAT
  measurement is expected to be of the combined [CII] + CO power (**forecast**) [src: Dev et al.
  2026, arXiv:2607.20404]. Interlopers are masked, modelled, or removed by cross-correlation.
- Estimators beyond the auto-power: stacking on an external catalogue, the conditional voxel
  intensity distribution, and the cross-power; simulations for a [CII] pathfinder give
  comparable significance for the three and the best constraints from their combination [src:
  Kramer et al. 2026, arXiv:2603.13218].
- Tomographic clustering redshifts applied to broadband diffuse maps give the mean line
  background without a spectrometer [src: Chiang 2026, arXiv:2602.02658].

## 5. Estimators, covariance and likelihood practice
<!-- key: estimators-covariance-and-likelihood-practice -->

### 5.1 The foreground wedge
<!-- key: the-foreground-wedge -->

- Foregrounds are spectrally smooth and should occupy the lowest k_∥ modes. An interferometer
  baseline of fixed length probes a k_⊥ that scales with frequency, so the Fourier transform
  along frequency mixes foreground power to higher k_∥ ("mode mixing") [sec: arXiv:1907.08211,
  section 12.1.5].
- For flat-spectrum unclustered sources the leaked power follows the squared primary beam
  evaluated at (k_∥/k_⊥)(c/H₀)(1 + z)/E(z); lines of constant contamination are k_∥ ∝ k_⊥ [sec:
  arXiv:1907.08211, eq. for P̂(k) in section 12.1.5].
- Wedge boundary [der: set the beam argument equal to D_c θ₀, with θ₀ the angle at which the
  beam reaches zero]: k_∥ = k_⊥ H₀ D_c E(z) θ₀ / [c (1 + z)]. With θ₀ at the horizon this is the
  "horizon line"; the region above it is the "EoR window".
- Delay-spectrum mapping as HERA writes it: Ṽ(τ) = ∫ V(ν) e^(2πiντ) dν; P̂(k_⊥, k_∥) =
  (X²Y/Ω_pp B) Ṽ₁(u, τ) Ṽ₂*(u, τ); k_∥ = 2πτ/X and k_⊥ = (2π/Y)(b/λ), with X = c (1 + z)²
  ν₂₁⁻¹ H(z)⁻¹, Y = D(z) the transverse comoving distance, Ω_pp the sky integral of the squared
  primary beam and B the bandwidth; Δ²(k) = P(k) k³/2π² in mK². Treating a delay mode as a
  k_∥ mode is the "delay approximation", valid for short baselines [src: HERA Collaboration
  2021, arXiv:2108.02263, Eqs. 22–26]. The horizon wedge is the light travel time along the
  baseline, τ_wedge = |b|/c [src: HERA Collaboration 2022, arXiv:2210.04912, Eq. 8]. Combining
  the two gives k_∥ = k_⊥ D(z) H(z) / [c (1 + z)] [der: Eq. 8 inserted in Eqs. 24–25 with λ =
  c (1 + z)/ν₂₁], the horizon line of the bullet above.
- Origins. Three-dimensional power spectrum from an interferometric data cube, with its
  symmetries separating smooth foregrounds: Morales & Hewitt 2004, arXiv:astro-ph/0312437,
  and Zaldarriaga, Furlanetto & Hernquist 2004, arXiv:astro-ph/0311514 [src]. The wedge first
  appeared in simulations of bright-source subtraction errors, at k_⊥ ≳ 0.05 Mpc⁻¹, with
  requirements of 0.1 arcsec in source position and 0.05% in gain amplitude [src: Datta,
  Bowman & Carilli 2010, arXiv:1005.4071]; it was explained as mode mixing, with the forecast
  of an "EoR window", by Morales et al. 2012, arXiv:1202.3830 [src]. Per-baseline delay
  transform, confining smooth foregrounds within the maximum geometric delay and relying on
  "spectrally- and spatially-smooth instrumental responses": Parsons et al. 2012,
  arXiv:1204.4749 [src]. Covariant errors in the window: Liu, Parsons & Trott 2014,
  arXiv:1404.2596 [src].
- Foreground avoidance restricts the analysis to the window; foreground subtraction or
  statistical separation tries to recover modes inside the wedge, as the LOFAR Gaussian-process
  approach does [sec: arXiv:1907.08211, section 12.1.5; src: Mertens et al. 2017,
  arXiv:1711.10834].

### 5.2 Foreground removal
<!-- key: foreground-removal -->

| Method | Used by | Property to check | Citation |
|---|---|---|---|
| Delay filtering and avoidance | HERA, CHIME | which k_∥ are lost; leakage from mutual coupling and reflections | arXiv:2210.04912, arXiv:2309.04404 |
| Gaussian process regression | LOFAR | recovers k = 0.07–0.3 h/cMpc in simulations and gains a factor ≳ 3 over avoidance; needs foreground coherence ≳ 3 MHz [src: abstract] | Mertens et al. 2017, arXiv:1711.10834 |
| Machine-learned GPR covariance | LOFAR 2025 | signal suppression; a bias correction was needed on the 3C196 field [src] | arXiv:2503.05576, Ceccotti et al. 2025, arXiv:2504.18534 |
| Blind source separation (PCA, FastICA) + transfer function | GBT, MeerKLASS | signal loss on all scales, corrected by mock injection [src] | Wolz et al. 2021, arXiv:2102.04946; Cunnington et al. 2023, arXiv:2302.07034 |
| Wavelet-domain PCA | Tianlai | first use with spherical Fourier–Bessel power spectrum [src] | Deng et al. 2026, arXiv:2604.27465 |
| Polynomial or physical foreground + signal model | global-signal experiments | uniqueness of the fit; number of terms [src] | Hills et al. 2018, arXiv:1805.01421 |

### 5.3 Reporting conventions
<!-- key: reporting-conventions -->

- Upper limits on Δ² are 2σ and are quoted with the k and z of the most constraining bin. Papers
  add whether the remaining bins are consistent with thermal noise.
- Cross-spectra between independent data splits remove the noise bias: nights or baselines in
  interferometers, "feed groups" in COMAP [src: Stutzer et al. 2024, arXiv:2406.07511], scan-
  and dish-wise subsets in MeerKLASS [src: arXiv:2610.12158].
- Validation practice read in the papers: end-to-end pipeline simulations and statistical tests
  (HERA, arXiv:2210.04912), signal injection (LOFAR, arXiv:2503.05576), 312 difference-map null
  tests (COMAP, arXiv:2406.07511), null and robustness tests on subset cross-spectra (MeerKLASS,
  arXiv:2610.12158).
- Global-signal claims are assessed by Bayesian evidence between data models with and without a
  signal and with and without systematic terms [src: Sims & Pober 2019, arXiv:1910.03165], and
  more recently by null-test evidence ratios [src: Sims et al. 2025, arXiv:2506.20042].
- Blinding. None of the abstracts read for this skill reports a blinded analysis. In MeerKLASS
  papers "blind" refers to blind component separation, which is a foreground-removal technique
  and not analysis blinding [src: arXiv:2610.12158; arXiv:2302.07034].
- Neutral-fraction inferences are Bayesian comparisons with reionisation simulations; the quoted
  intervals are posterior medians with 68% intervals and are bounded by 0 and 1, so error bars
  are strongly asymmetric near the bounds.

### 5.4 What the main limits and detections did
<!-- key: what-the-main-limits-and-detections-did -->

| Analysis | Calibration and foreground strategy | Bands, scales, estimator | Signal loss and how a result is quoted | Place read |
|---|---|---|---|---|
| HERA Phase I | redundant-baseline calibration (χ² over redundant groups, no sky model), absolute calibration of three degeneracies on GLEAM-calibrated visibilities, gain smoothing on 6 h and 10 MHz; crosstalk subtracted near zero fringe rate; **avoidance** with a buffer beyond the horizon of 200 ns (2021) then 300 ns (2022; k = 0.15 and 0.17 h Mpc⁻¹) | z = 10.4 and 7.9; delay spectra from cross-products of visibilities with independent noise (no noise bias), averaged incoherently over baseline pairs and LST fields | loss budgeted per step and corrected (section 6 of `systematics.md`); limit = measured Δ² + 2σ, negative bandpowers set to zero | arXiv:2210.04912, Sects. III.1, III.3.3; arXiv:2108.02263, Sects. IV.1, IV.4 |
| LOFAR 2025 | direction-independent, then direction-dependent calibration with spectrally smooth gains and sky-model subtraction; baselines < 250 λ excluded from the latter; residual foregrounds ("approximately three orders of magnitude brighter than the 21-cm signal") removed by Gaussian-process regression, d = f_fg + f_21 + n, K = K_fg + K_21 + K_n, with a 21 cm kernel learned from GRIZZLY simulations (**subtraction**) | z ≈ 10.1, 9.1, 8.3; seven logarithmic bins over k = 0.06–0.5 h cMpc⁻¹; noise bias from time-differenced visibilities subtracted | injection test; limit = 95% bound of spectra drawn from the regression posterior; positive residuals, only partly correlated between nights, not read as signal | arXiv:2503.05576, Sects. 3.7, 4.4, 5.1 |
| MWA 2025 | Hyperdrive calibration; ionospheric offsets corrected for the 1,000 brightest sources, 7,000 more subtracted at catalogue positions; no statistical subtraction (**direct subtraction, then avoidance**) | three overlapping 15.36 MHz bands (z = 7.0, 6.8, 6.5), ~9 MHz effective after a Blackman–Harris taper; CHIPS; window 0.015 < k_⊥ < 0.06, k_∥ > 0.11 and k_∥ > 2 k_⊥ + 0.08 h Mpc⁻¹ | end-to-end simulation fixes a normalisation correction; second pipeline (FHD/εppsilon) on 335 observations; 2σ | arXiv:2505.09097, Sects. III.3, III.5, V |
| PAPER-64 (2015, retracted) | empirical inverse-covariance weighting with fringe-rate filtering | z = 8.4, 0.15 < k < 0.5 h Mpc⁻¹, 135 days | loss underestimated; arXiv abstract now states the limits "have been retracted"; the re-analysis uses an estimator "that is not lossy" | arXiv:1502.06016; arXiv:1810.05175, Sect. V |
| CHIME 2025 auto-spectrum | new RFI masks; DAYENU foreground filter on each 9.94 s integration of north–south beamformed visibilities, before time averaging; foregrounds confined below ≈ 200 ns (**filtering**) | 94 nights, 608.2–707.8 MHz; delay spectrum; A²_HI ≡ 10⁶ Ω²_HI (b_HI + ⟨fμ²⟩)², ⟨fμ²⟩ = 0.761 | the stored filter is applied to the simulations, so loss is in the model; significance = Δχ² = χ²_null − χ²_best-fit against 1000 noise realisations, fitted with an F distribution | arXiv:2511.19620, Sects. III.2.3, VI.2.3, VI.3 |
| MeerKLASS 2022 cross-power | PCA on the frequency covariance of the maps, first N_fg = 30 modes removed (**blind subtraction**) | 199 channels, 973.2–1014.6 MHz; cross-power with WiggleZ | transfer function T(k) = ⟨P(M_c, M_g)/P(M_HI, M_g)⟩ from 100 lognormal mocks injected into the data, M_c = [M_HI + X_obs]_PCA − [X_obs]_PCA | arXiv:2206.01579, Sects. 4.2–4.3, Eqs. 19–20 |
| MeerKLASS 2026 auto-power | multiscale PCA: wavelet split into large and small angular scales, cleaned separately, per data subset (**blind subtraction**) | cross-spectra between subsets split by observing block and by dish; jackknife covariance | loss modelled, not corrected: D(k) = (k / h Mpc⁻¹)^β, β a nuisance parameter; S/N 7.3 for the data vector against zero, 6.2 for the model fit (the abstract value) | arXiv:2610.12158, Sects. 3, 7.3, 11.1 |
| COMAP Season 2 | low-level filtering of the time streams; feed-group pseudo-cross-spectrum, P = P_CO + P_noise + P_syst with the last two removed by crossing feed groups | CO(1–0), z = 2.4–3.4 | P_CO = C_k/T(k), T = T_f T_b T_p T_ν (filter from simulations; beam, pixel, channel analytic); 95% limits per k bin with a positivity prior; a 2.7σ excess at 0.12 < k < 0.18 Mpc⁻¹ is still quoted as a limit | arXiv:2406.07511, Sects. 2.1, 4, 5.4, Eqs. 2, 18–20 |

All rows [src]. Notes.

- The LOFAR mode-mixing coherence scales fitted by the regression are 2.5–8 MHz at z = 8.3 and
  9.1 [src: arXiv:2503.05576, Sect. 3.7]. Earlier limits of the same instruments, both 2σ:
  LOFAR (73 mK)² at k = 0.075 h cMpc⁻¹, z ≈ 9.1, 141 h [src: Mertens et al. 2020,
  arXiv:2002.07196]; MWA (43 mK)² at k = 0.14 h Mpc⁻¹, z = 6.5, 110 h [src: Trott et al. 2020,
  arXiv:2002.02575].
- CHIME filters before averaging because frequency-dependent RFI masks couple to day-to-day
  gain changes of ~1% and leak smooth foregrounds to high delay. Validation: imaginary part,
  even against odd days, Stokes Q, right-ascension and declination halves, baseline
  selections, sub-bands, source-mask flux cuts, agreement with the stacking amplitude [src:
  arXiv:2511.19620, Sects. III.2.3 and VII]. The earlier stacking analysis masked 47.2% of the
  band and filtered each map pixel along frequency against foregrounds 10³–10⁵ times the
  signal [src: CHIME Collaboration 2022, arXiv:2202.01242, Sect. IV.5].
- COMAP: CO(2–1) from z = 6–8 is a ~10% interloper; the sensitivity gain is a factor eight
  over COMAP Early Science and ten over COPSS [src: arXiv:2406.07511, Sects. 2.1 and 5.4].

## 6. Codes and simulations
<!-- key: codes-and-simulations -->

| Code or suite | Role | Reference | Flag |
|---|---|---|---|
| Excursion-set model and semi-numerical method | ionised regions tied to large-scale density fluctuations, with sizes from the excursion-set formalism; then applied directly to linear density and velocity fields with first-order Lagrangian perturbation theory and tested against N-body simulations with radiative transfer | Furlanetto, Zaldarriaga & Hernquist 2004, arXiv:astro-ph/0403697; Mesinger & Furlanetto 2007, arXiv:0704.0946 | [src] |
| 21cmFAST | semi-numerical 3D realisations of density, ionisation, velocity and spin temperature; agrees with a hydrodynamic simulation to tens of percent in the power spectrum on scales ≳ 1 Mpc | Mesinger, Furlanetto & Cen 2010, arXiv:1003.3878 | [src] |
| 21cmEMUv3 | emulator of 21cmFASTv3 summaries (cylindrical and spherical power spectra, global signal, x_HI, T_s, UV luminosity functions, τ) over σ₈ and ten astrophysical parameters; sub-percent median accuracy; public | Breitman et al. 2026, arXiv:2606.00219 | [src] |
| GRIZZLY | 21 cm power-spectrum model used for the LOFAR interpretation | Ghara et al. 2025, arXiv:2505.00373 | [src] |
| EDGES analysis package | open-source end-to-end calibration, analysis and simulation package for global-signal experiments; raw EDGES data released with it | Murray et al. 2026, arXiv:2605.16643 | [src] |
| EX-CITE on Sherwood | post-processing for ionising-background fluctuations in Lyα forest modelling | arXiv:2304.02038 | [src] |
| THESAN, CoDa-III, Aton | radiation-hydrodynamic or radiative-transfer reionisation simulations used as comparison in Lyα and Lyα-emitter work | named in arXiv:2304.02038 and arXiv:2609.40363 | [sec] |
| Lumina | 500 cMpc radiation-hydrodynamic box (AREPO, IllustrisTNG model, GPU M1 transport), through HI and He II reionisation to z = 3 | Zier et al. 2026, arXiv:2605.15310 | [src: abstract] |
| AMBER, Agora | reionisation and microwave-sky simulations behind the SPT kSZ duration limits and the trispectrum foreground estimate | named in arXiv:2601.20551 and arXiv:2403.02337 | [sec] |
| UniverseMachine on Uchuu; Shark | empirical and semi-analytic galaxy models compared with JWST luminosity functions | Prada et al. 2026, arXiv:2604.18683; Lagos et al. 2026, arXiv:2609.03537 | [src] |

The sibling `cosmo-simulations-mocks` covers the simulation suites themselves;
`cosmo-software-ecosystem` covers general inference tooling.

## 7. Conventions and traps specific to the domain
<!-- key: conventions-and-traps-specific-to-the-domain -->

- Δ² is quoted either in mK² (HERA: 457 mK²) or as a squared temperature (LOFAR: (68.7 mK)²).
  Square or take the root before comparing.
- Wavenumbers are in h Mpc⁻¹ for 21 cm experiments and in Mpc⁻¹ for COMAP and for CHIME's k_∥
  cut.
- Neutral fractions are volume-weighted in most quasar work and mass-weighted in some galaxy
  work (for example arXiv:2609.40363); the two differ during patchy reionisation.
- Mean free paths are in proper Mpc; dark-gap lengths and bin sizes in comoving h⁻¹Mpc.
- "Duration of reionisation" has at least three definitions (section 1.5).
- "Detection" in intensity mapping can mean a cross-correlation, a stack, or an auto-spectrum;
  these constrain different parameter combinations.

## Not verified
<!-- key: not-verified -->

- The orientation of the velocity-gradient factor in Eq. 7 of arXiv:1109.6012 (numerator in
  the rendering read, denominator in arXiv:1907.08211) was not checked against the journal
  version.
- Gunn & Peterson 1965, Wouthuysen 1952 and Field 1958 are cited by DOI after a Crossref check
  of title, author and year; none has an abstract online and none was read. The Gunn–Peterson
  optical-depth formula itself is not given here.
- The foundational wedge papers (arXiv:1005.4071, arXiv:1202.3830, arXiv:1204.4749,
  arXiv:1404.2596) were read as abstracts only; the wedge equations here come from HERA papers
  and from arXiv:1907.08211.
- The review of Furlanetto, Oh & Briggs 2006 was read as an abstract only.
