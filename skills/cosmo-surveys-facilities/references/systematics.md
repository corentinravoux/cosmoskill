# Surveys and facilities — facility-level systematics (pointer level)

Scope: instrument and survey-strategy effects that propagate into cosmology, each with its mechanism, a size where a paper read this session quantifies it, the standard mitigation, and the sibling skill that treats it in depth.
Snapshot: 2026-10-07

Flags as in `surveys-and-data.md`: `[src]` read this session in the cited
paper or page; `[sec: GC|WL|CMB|SN|CL]` carried over from the named sibling
skill's `references/surveys-and-data.md`; `[der]` derived here. This file
does not replace the systematics files of the probe skills: it says which
hardware or strategy choice creates the effect and where to read on.

## 1. Spectroscopic surveys
<!-- key: spectroscopic-surveys -->

### 1.1 Fibre collisions and assignment incompleteness
<!-- key: fibre-collisions-and-assignment-incompleteness -->

- **Mechanism.** A fibre system cannot observe every target of a dense
  list. Plates forbid close neighbours; robotic positioners reach only a
  patrol disc; the missed targets are clustered, so the loss is largest
  where the density is highest (Bianchi & Percival 2017, arXiv:1703.02070;
  Lasker et al. 2024, arXiv:2404.03006) [src].
- **Size.** In a DESI Bright Galaxy Survey mock, completeness is above 95%
  in low-density regions and below 10% in the centres of massive clusters
  (Smith et al. 2019, arXiv:1809.07355) [src]. Survey-wide, DESI DR2
  assignment completeness runs from 53.7% (ELG) to 93.6% (QSO)
  (arXiv:2503.14738) [sec: GC].
- **Mitigation.** Pairwise-inverse-probability weights from many reruns of
  the assignment, plus angular upweighting; or removal of small angular
  separations at the model stage (Bianchi et al. 2024, arXiv:2411.12025)
  [src].
- **Validation.** Mocks passed through the real assignment code with the
  real hardware state and observing history (arXiv:2404.03006) [src].
- **Where.** `cosmo-galaxy-clustering` (estimators, θ-cut, window);
  `cosmo-peculiar-velocities` for the effect on low-redshift samples.

### 1.2 Redshift success and its dependence on the instrument
<!-- key: redshift-success-and-its-dependence-on-the -->

- **Mechanism.** The probability of a good redshift depends on exposure
  depth, fibre throughput, position in the focal plane and target
  brightness, so the failures imprint the observing pattern on the sample.
- **Size.** DESI DR2 redshift success is 98.8% for BGS and 99.0% for LRG,
  and 73.9% for ELG and 68.0% for QSO (arXiv:2503.14738) [sec: GC]: the
  correction matters most for the tracers that carry the high-redshift
  measurement.
- **Mitigation.** Exposure times set dynamically to a uniform effective
  depth (Schlafly et al. 2023, arXiv:2306.06309) [src]; redshift-failure
  weights in the catalogues.
- **Where.** `cosmo-galaxy-clustering`.

### 1.3 Redshift accuracy
<!-- key: redshift-accuracy -->

- **Mechanism.** Broad or asymmetric lines (quasars), line misidentification
  and wavelength calibration shift redshifts coherently.
- **Size.** An independent radio check exists: stacking CHIME 21 cm maps on
  eBOSS quasars is sensitive to a redshift bias and finds
  Δv = −66 ± 20 km/s for the quasar catalogue (CHIME Collaboration 2022,
  arXiv:2202.01242) [src].
- **Where.** `cosmo-galaxy-clustering` (quasar redshift errors in BAO and
  RSD), `cosmo-lyman-alpha` (quasar redshifts in the cross-correlation).

### 1.4 Target selection inherited from imaging
<!-- key: target-selection-inherited-from-imaging -->

- **Mechanism.** Spectroscopic targets are selected on imaging, so imaging
  depth, seeing, extinction and stellar density modulate the target density
  (Sect. 2.1). A change of imaging survey inside the footprint is a change
  of selection: the Legacy Surveys switch from Bok/Mayall grz to DECam at
  Dec = 32.375° (legacysurvey.org DR11 description) [src].
- **Mitigation.** Regression or neural-network weights against imaging maps;
  separate treatment of photometric regions. The reference a referee expects
  for the method is Ross et al. 2017 (arXiv:1607.03145) [sec: GC].
- **Where.** `cosmo-galaxy-clustering`; `cosmo-inflation-primordial` for the
  f_NL measurement, which is the most exposed.

### 1.5 Hardware faults as selection effects
<!-- key: hardware-faults-as-selection-effects -->

A spectrograph misalignment stopped WEAVE from 16 September 2024 to July
2025 (ING WHT page) [src]. Interruptions of this kind change the footprint
and the depth pattern a survey finally delivers, and design numbers do not
anticipate them (`open-questions.md`, Sect. 1).

## 2. Imaging surveys
<!-- key: imaging-surveys -->

### 2.1 Depth and seeing variations
<!-- key: depth-and-seeing-variations -->

- **Mechanism.** The limiting magnitude varies with exposure number, seeing,
  sky brightness and extinction; the galaxy density and the redshift
  distribution of a flux-limited sample follow.
- **Mitigation at the facility level.** Dynamic exposure times to equalise
  depth (Dey et al. 2019, arXiv:1804.08657) [src]; survey-property maps
  released with the data.
- **Size.** Archival, heterogeneous imaging can still be used for shear:
  the DECADE catalogues are built from community DECam data
  (arXiv:2509.03582) [sec: WL].
- **Where.** `cosmo-galaxy-clustering` (imaging-systematics weights),
  `cosmo-weak-lensing` (variable depth in n(z) and shear).

### 2.2 Photometric calibration
<!-- key: photometric-calibration -->

- **Mechanism.** Zero-point errors that vary over the sky create spurious
  large-scale clustering and bias colours, photometric redshifts and
  supernova distances.
- **Size.** About 1% relative calibration in griz for SDSS after
  ubercalibration (Padmanabhan et al. 2008, arXiv:astro-ph/0703454); 7 mmag
  uniformity over the DES footprint with the forward global calibration,
  and under 5 mmag chromatic uncertainty for main-sequence stars (Burke et
  al. 2018, arXiv:1706.01542); better than 3 mmag against Gaia in DES DR2
  (arXiv:2101.05765); 7–12 mmag for Pan-STARRS1 (Chambers et al. 2016,
  arXiv:1612.05560) [src].
- **Why it matters most for supernovae.** A Stage-IV supernova analysis is
  sensitive to zero-point shifts at the 5 mmag level (**forecast**)
  [sec: SN]; the
  cross-calibration of surveys (Fragilistic, Dovekie) is a facility-level
  product.
- **Where.** `cosmo-supernovae` (calibration), `cosmo-weak-lensing`
  (photo-z), `cosmo-galaxy-clustering` (target selection).

### 2.3 Point-spread function
<!-- key: point-spread-function -->

- **Mechanism.** PSF model errors leak into galaxy shapes; a broad band
  makes the PSF depend on the galaxy spectrum.
- **Facility facts.** Euclid VIS uses one broad band covering r, i and z
  (arXiv:2405.13492) [src]; UNIONS supplies the ground-based colours needed
  "for the calibration of the wavelength dependence of the Euclid
  point-spread function" in the north (Gwyn et al. 2025, arXiv:2503.13783)
  [src]. UNIONS and CFHTLenS share a camera and the same detector-scale
  additive pattern in B modes [sec: WL].
- **Where.** `cosmo-weak-lensing`.

### 2.4 Blending
<!-- key: blending -->

Deeper ground-based imaging loses sources to blending: the LSST **forecast**
of the effective source density falls from about 37 to about 31 arcmin⁻²
when seriously blended galaxies are rejected (Chang et al. 2013,
arXiv:1305.0793) [src]. Blending also biases photometric redshifts and
cluster lensing. Where: `cosmo-weak-lensing`, `cosmo-clusters`.

## 3. Slitless spectroscopy and spectrophotometry
<!-- key: slitless-spectroscopy-and-spectrophotometry -->

- **Mechanism.** Every source is dispersed, so spectra overlap, and a
  redshift often rests on a single emission line. Line misidentification
  produces interlopers at a wrong redshift; contamination depends on the
  dispersion direction, hence on the dither and roll pattern.
- **Facility facts.** Euclid NISP: R ≥ 450, wavelength calibration required
  to better than 5 Å, relative spectrophotometry to better than 0.7%
  (arXiv:2405.13493) [src]; four dithered frames per wide-survey pointing
  (Scaramella et al. 2022, arXiv:2108.01201) [src].
- **Status.** No Euclid clustering measurement on data exists; the BAO
  pipeline has been validated on mocks [sec: GC].
- **SPHEREx.** R = 35–130 spectrophotometry in 6.2″ pixels [sec: GC]:
  redshift precision and star–galaxy separation set the usable sample for
  the f_NL measurement.
- **Where.** `cosmo-galaxy-clustering` (interlopers, purity and
  completeness), `cosmo-inflation-primordial` (f_NL requirements).

## 4. CMB experiments
<!-- key: cmb-experiments -->

- **Beams.** The beam window multiplies every power spectrum; its
  uncertainty and its polarised sidelobes limit the damping tail and
  temperature-to-polarisation leakage. Resolution is also the lever on
  parameter precision at fixed sensitivity (Knox 1995,
  arXiv:astro-ph/9504054) [src].
- **Scan strategy and atmosphere.** Ground-based maps lose the largest
  angular scales to atmospheric and ground-synchronous signals; the remedy
  is fast polarisation modulation and a satellite for the reionisation
  bump. Day-time data are harder to use: the ACT DR6 lensing analysis uses
  night-time data only [sec: CMB].
- **Frequency coverage.** Foreground separation sets the band list; the
  LiteBIRD reformation cut the bands from 15 to 12 and relaxed the
  sensitivity requirement [sec: CMB].
- **Sky area versus depth.** Sect. 7 of `physics-and-methods.md`.
- **Where.** `cosmo-cmb` (beams, transfer functions, calibration,
  foregrounds), `cosmo-inflation-primordial` (B-mode systematics),
  `cosmo-cmb-lss-cross-correlations` (masks and overlap with galaxy
  surveys).

## 5. Time-domain surveys
<!-- key: time-domain-surveys -->

- **Detector effects in photometry.** ZTF light curves carry a
  flux-dependent PSF distortion (the "pocket effect") that produces
  non-linearities of a few percent and affects every ZTF light-curve
  release; scene-modelling photometry changes colours by 10 mmag and the
  absolute calibration by 90 mmag relative to forced photometry (Lacroix et
  al. 2025, arXiv:2509.04073) [sec: SN]. This is why the ZTF SN Ia DR2
  (arXiv:2409.04346) is not a cosmology sample [sec: SN].
- **Cross-survey calibration.** ATLAS photometry showed initial offsets of
  about 40 mmag against DES stars, reduced to an estimated 5–10 mmag
  [sec: SN].
- **Cadence and selection.** Detection efficiency depends on cadence,
  filter sequence and depth, and the spectroscopic follow-up adds its own
  selection. For Rubin the choice of footprint, filter pairing and cadence
  regularity changes the cosmological return (Lochner et al. 2022,
  arXiv:2104.05676) [src].
- **Where.** `cosmo-supernovae`; `cosmo-peculiar-velocities` for SN Ia
  velocities; `cosmo-distance-ladder-h0` for the calibrator samples.

## 6. Radio
<!-- key: radio -->

- **Foregrounds and beam chromaticity.** Galactic and extragalactic
  foregrounds exceed the 21 cm signal by orders of magnitude; a
  frequency-dependent beam mixes their smooth spectra into the line-of-sight
  modes of the signal. For a cylinder telescope, simulations require the
  per-feed beam width to 0.1% and gains to 1% within a minute (Shaw et al.
  2015, arXiv:1401.2095) [src].
- **Mechanical tolerances.** For HIRAX, the first 28 dishes have surface
  deviations within requirements, while feed placement "satisfies all
  accuracy criteria but fails precision limits" (Studer et al. 2026,
  arXiv:2607.26972) [src]: redundancy, on which the calibration relies, is
  a manufacturing specification.
- **Polarisation leakage and total-power stability.** Treated by projection
  onto temperature modes in the m-mode analysis (arXiv:1401.2095) [src];
  single-dish mapping needs gain stability on the scan timescale, which
  MeerKLASS reports as achieved (Cunnington et al. 2026, arXiv:2606.25955)
  [src].
- **Where.** `cosmo-reionization-21cm` (foreground methods, signal loss),
  `cosmo-cmb-lss-cross-correlations` for cross-correlations with optical
  surveys.

## 7. X-ray and gravitational waves
<!-- key: x-ray-and-gravitational-waves -->

- **eROSITA.** Cluster cosmology depends on a selection function built from
  simulated skies and on optical confirmation with Legacy Survey imaging
  [sec: CL]; only half the sky is released by the German consortium
  (arXiv:2401.17274) [src]. Where: `cosmo-clusters`.
- **Gravitational-wave detectors.** Strain calibration enters the luminosity
  distance directly, and the detection threshold defines the selection
  function of a siren sample. Where: `cosmo-multimessenger`.

## 8. Referee checklist for a facility description
<!-- key: referee-checklist-for-a-facility-description -->

1. Is each number a design value or a delivered value, and from which
   release? (Area, number of objects, depth, number of passes.)
2. Is the depth convention stated (S/N, aperture, point or extended source)?
3. Which completeness is quoted: assignment, redshift success, or area?
4. Is the fibre-assignment correction named (PIP, angular upweighting,
   θ-cut) and validated on mocks run through the real assignment?
5. Are the imaging releases used for targeting named (for example Legacy
   Surveys DR9 for DESI, DR10.1 for 4MOST CRS [sec: GC]) and the
   north/south photometric boundary handled?
6. For photometric samples: the calibration method and its uniformity
   figure; for supernovae, the cross-calibration reference.
7. For slitless samples: purity and completeness from simulations with the
   actual dither pattern.
8. For CMB maps: beam, transfer function, sky fraction after masking, and
   the depth in the units used elsewhere in the text.
9. For radio intensity maps: the beam-knowledge requirement and how signal
   loss in foreground removal was measured.
10. Is every "will" attached to a date that has not already passed or
    slipped (`open-questions.md`, Sect. 4)?

## Not verified
<!-- key: not-verified -->

- SDSS and BOSS fibre-collision angular scales; DESI positioner patrol
  radius.
- Size of the north/south photometric offset in the Legacy Surveys and how
  DESI DR2 treats it.
- Euclid NISP delivered purity and completeness; the 2026 SPHEREx papers on
  detector artefacts and star–galaxy separation were seen as search results
  only and are not cited.
- CMB beam and transfer-function numbers: none is quoted here; see
  `cosmo-cmb`.
- eROSITA and gravitational-wave calibration uncertainties.
