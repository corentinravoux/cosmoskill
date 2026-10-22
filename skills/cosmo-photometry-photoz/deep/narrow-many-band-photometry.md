# Many-band and narrow-band photometry (COSMOS, PAU, ALHAMBRA, J-PAS, J-PLUS, S-PLUS, SPHEREx) — cosmo-photometry-photoz dossier

Scope: how many-band and narrow-band photo-z are produced, from the
narrow-band flux calibration through template sets with emission lines,
band zero-point recalibration, priors and PDF recalibration, and how to
choose between template and machine-learning codes, between calibration
schemes and between configurations when such catalogues serve as a
reference sample. Several survey families do this, each with its own
pipeline: COSMOS (30 bands, then COSMOS2020 and COSMOS2025), PAUS (40
narrow bands), ALHAMBRA (20 medium bands), the Javalambre surveys
(miniJPAS 60 bands, J-PLUS 12 bands), S-PLUS (12 bands) and SPHEREx
(102-band spectrophotometry, forecasts only here).
Snapshot: 2026-10-21.
From: Newman & Gruen 2022 review, Sect. 2.3, 3.2; PAU and COSMOS survey
programmes (copied from `references/subtopics.tsv`).

Already in L2, not repeated here: survey areas, depths and headline
precision of COSMOS2020, COSMOS2025, PAUS, miniJPAS, J-PLUS/S-PLUS and
SPHEREx (`surveys-and-data.md#many-band-and-narrow-band-calibration-fields`);
the precision rows in `results.md#photo-z-performance-of-individual-galaxies`;
catastrophic rates of COSMOS2015 used as truth and the cost of wrong
reference redshifts (`systematics.md#wrong-redshifts-in-the-calibration-sample`);
how DES Y6 perturbs COSMOS2020 and PAUS redshifts inside its SOM error
budget (`results.md#ensemble-n-z-characterisation`); the generic template
codes BPZ, LePhare and EAZY
(`physics-and-methods.md#photometric-redshifts-by-template-fitting`). Survey
calibration of broad-band imaging is in the photometric-calibration dossier.

Symbols. NB, BB: narrow band, broad band. f̃_i, σ_i: observed flux and
error in band i. α_j ≥ 0: amplitude of template j. l_i: global
zero-point factor of band i. k: per-galaxy NB/BB flux scaling. z_b: mode
of p(z). z_s: spectroscopic redshift. Δ_z = (z_b − z_s)/(1 + z_s).
σ_68 = ½(P84 − P16) of Δ_z. σ_NMAD = 1.48 median(|Δz − median Δz|/(1 + z_s)).
Outlier thresholds differ between papers and are given with each number.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Extract and calibrate narrow-band fluxes
<!-- key: step-1-extract-and-calibrate-narrow-band-fluxes -->

- **Forced photometry.** PAUS measures NB fluxes at the positions and
  with the shapes of a deeper broad-band reference catalogue (CFHTLenS,
  KiDS); objects in the wide fields are observed on average three times
  and coadded at catalogue level [src: arXiv:2312.07581, Sect. 2.1]. This
  ties the NB sample to the reference detection and makes the BB/NB
  aperture mismatch a per-galaxy parameter (Step 3).
- **Zero points without NB standards.** No standards exist in the PAU
  system and data are taken in non-photometric conditions, so each
  exposure is calibrated on SDSS stars: stellar templates from the X-shooter
  library (XSL), with Milky Way extinction, are fitted to SDSS broad-band
  photometry, synthetic NB fluxes are computed through the measured PAUCam
  response, and per-star zero points are combined per exposure and filter;
  the zero point absorbs atmospheric extinction and, by construction, the
  colour terms [src: arXiv:2406.06850, Sect. 2.1, 4]. Blue stars are
  preferred because their smoother SEDs are better constrained by five
  broad bands [src: Sect. 2.1].
- **Checks and residuals.** Blue-star and all-star calibrations agree at
  the 2% level, except near 5170 Å (Mg I triplet) and redward of ~6850 Å
  (telluric features); vignetting of the outer central CCDs reaches 8%
  peak to valley and is corrected by a star flat built from star-to-image
  zero-point residuals; calibration from SDSS spectra shows no trend above
  1% with blue stars; repeated stars agree after calibration with errors
  somewhat underestimated; twilight spectrophotometric standards agree up
  to a ~5% offset, not a clean test since extinction was not calibrated
  (King 1985 coefficients assumed) [src: arXiv:2406.06850, Sect. 4].
- **ALHAMBRA (stellar transformation equations).** Transformation
  equations between the ALHAMBRA and SDSS systems are derived from
  primary standards of the HST/STIS Next Generation Spectral Library and
  applied to all stars with good photometry in both; zero points come
  from the mean difference between instrumental and synthetic magnitudes,
  with an internal error of no more than a few hundredths of a magnitude
  per CCD and filter; the NIR bands are tied to 2MASS with uncertainties
  of ~0.03 mag [src: arXiv:1306.4968, Sect. 2.4]. These stellar zero
  points are then refined on galaxies (Step 3).
- **J-PLUS (stellar and white-dwarf loci).** Calibration stars from Gaia
  and 3D dust maps; g, r, i anchored to Pan-STARRS with the CCD-position
  variation; the nine other filters homogenised on the dust-corrected
  instrumental stellar locus in (X − r) against (g − i); absolute colours
  from a joint Bayesian model of eleven colour–colour diagrams against
  the theoretical white-dwarf locus. Errors (numbers table) give 1–2%
  over 1022 deg² with no calibration campaign or atmospheric monitoring;
  the method is to be adapted to J-PAS [src: arXiv:1907.12939]. Like
  PAUS it needs no standards in its own filters; its absolute colour
  scale comes from the white-dwarf locus, not from stellar templates
  fitted to SDSS.
- **COSMOS2020** provides two photometric catalogues of the same images,
  aperture-based (Classic) and profile-fitting (The Farmer); photometry is
  corrected for Galactic extinction with the Schlafly & Finkbeiner map
  (SFD rescaled by 0.86) before any photo-z [src: arXiv:2110.13923,
  Sect. V].

### Step 2. Build the template set, with emission lines
<!-- key: step-2-build-the-template-set-with-emission -->

Narrow bands resolve lines: a feature's effect on a band scales with its
equivalent width over the bandwidth, so line modelling matters far more
than for broad bands [src: arXiv:2108.03271, Sect. 4.2]; in COSMOS the
expected line fluxes change medium-band colours by up to 0.4 mag
[src: arXiv:0809.2101, Sect. III.2]. Working configurations:

| Code and data | Continuum | Emission lines | Amplitudes | Place read |
|---|---|---|---|---|
| BCNz2, PAUS 40 NB + COSMOS uBVriz | 35 "runs": ellipticals and red spirals without lines or dust; Sc–SB11 with lines; six BC03 templates (τ = 0.3 Gyr) for missing quiescent galaxies; SB4–SB11 with Calzetti and two bump variants, E(B−V) = 0.05–0.5 in ten steps | two templates with fixed ratios to [O II] (Table 2), [O III] doublet kept separate | non-negative linear combination inside a run; runs combined by summing exp(−χ²_min/2) (Eq. 11) | arXiv:1809.04375, Sect. 4.4–4.5, Table 1 |
| Alarcon et al., PAUS + 26 COSMOS2015 bands (66 bands) | same continuum templates and extinction laws as BCNz2 and COSMOS2015 | line ratios measured from the 66 bands on zCOSMOS-bright: log₁₀ β(O III) = −0.50 ± 0.35, β(Hβ) = −0.56 ± 0.34, β(Hα) = −0.08 ± 0.24 (Eq. 12), median model plus six ±2σ_68 variants per continuum pair; 679 models | two continuum and one line amplitude marginalised (Bayes evidence) with a prior on line strength from the UV–[O II] relation | arXiv:2007.11132, Sect. 3.3, 3.6 |
| LePhare, COSMOS2020 | 19 Polletta ellipticals and spirals (interpolated), 12 BC03 blue star-forming, 2 BC03 exponentially declining; E(B−V) ≤ 0.5 with Calzetti, Prevot and two bump variants; AGN and stellar templates separately | from the UV–[O II] relation and fixed ratios | one template, best amplitude | arXiv:2110.13923, Sect. V.1 |
| EAZY, COSMOS2020 | 17 FSPS templates spanning rest-frame UVJ space at 0 < z < 3 | inside the FSPS templates | non-negative linear combination; template error function and magnitude prior | arXiv:2110.13923, Sect. V.2 |
| LePhare (customised), miniJPAS 60 bands | 50 templates selected from 90,720 CIGALE SPS models (two delayed-exponential populations, BC03, three metallicities, Inoue nebular grid) | inside the templates; LePhare's per-galaxy line adjustment switched off | one template | arXiv:2108.03271, Sect. 3.1, 4.1–4.2 |
| LePhare, COSMOS 30 bands (12 medium) | template library of Sect. III.1 (not read here) | [O II] from the dust-corrected UV luminosity through the Kennicutt SFR relations (Eq. 1), allowed to vary by a factor 2 because the relation scatters by 0.2 dex against VVDS; fixed ratios [O III]/[O II] = 0.36, Hβ/[O II] = 0.61, Hα/[O II] = 1.77, Lyα/[O II] = 2, attenuated with the template | one template | arXiv:0809.2101, Sect. III.2 |
| BPZ2.0, ALHAMBRA 20 medium bands + JHK_s | six PEGASE templates recalibrated on FIREWORKS photometry and spectra, four GRASIL and one starburst (the Fig. 21 caption counts 5 + 5 + 1); Madau IGM | included in the library, with dust | interpolation factor 7 between neighbouring templates; z = 0.001–7, Δz = 0.001 | arXiv:1306.4968, Sect. 4 |
| LePhare, COSMOS2025 (37 bands, JWST) | BC03 with six star-formation histories, two metallicities, 43 ages (0.05–13.5 Gyr); E(B−V) ≤ 1 with Calzetti, Arnouts et al. 2013 and Salim et al. 2018 curves; dust (PAH) emission by energy balance; stellar (with brown dwarfs) and AGN libraries fitted in parallel | Saito et al. 2020 recipe; all line fluxes vary together by a factor 2 | one template | arXiv:2506.03243, Sect. 6.1 |
| LePhare (customised), J-PLUS DR4 12 bands | 30 CIGALE templates selected from 455 candidates with the miniJPAS procedure; Calzetti, E(B−V) = 0, 0.2, 0.4 | inside the templates | one template; galaxy templates only, so p(z) is conditional on the source being a galaxy | arXiv:2607.06662, Sect. 3–3.1 |
| χ² template code, SPHEREx forecast (102 bands + DECaLS, WISE) | the 160 templates (129 Brown et al. 2014, 31 COSMOS) used to make the mock; E(B−V) = 0–1 in steps of 0.05 with Prevot, Calzetti and Allen laws; z = 0–3, Δz = 0.002; flat priors | continuum and lines assessed separately, because the line models of template codes fall short at SPHEREx resolution | one template | arXiv:2312.04636, Sect. V |

Stated reasons. BCNz2 forbids negative amplitudes because they let the
[O III] template fit spurious low fluxes from inter-CCD cross-talk, and
groups SEDs into runs because free dust templates gave too much freedom;
one line template instead of two degraded the photo-z significantly
[src: arXiv:1809.04375, Sect. 4.3.1, 4.4, 4.5]. The public BPZ used for the
design study could not include lines flexibly, which motivated a new code
[src: Sect. 4]. miniJPAS switches off per-galaxy line adjustment because
it admits unphysical solutions; its 50 templates come from 455 grid models
that fit bright (r < 22) spectroscopic galaxies with χ²_r < 1 and a
coefficient of variation of the residuals CV_RMSE < 0.04 (Eq. 6), the
latter because a χ² cut alone favours low-S/N sources; the final set is
chosen by a stochastic search scored on the spectroscopic sample, and
different random starts reach the same score with identical photo-z for
~98% of sources [src: arXiv:2108.03271, Sect. 4.2]. COSMOS2020 drops IRAC
channels 3 and 4 from LePhare because PAH emission at 3.3, 6.2 and 7.7 μm
is hard to model and they are shallow [src: arXiv:2110.13923, Sect. V.1].
COSMOS2025 moves the other way: with NIRCam coverage it replaces the
limited Ilbert et al. 2013 set, chosen earlier to reduce colour–redshift
degeneracies, by a larger BC03 library from which physical parameters
come at the same time, and it models PAH emission because MIRI 7.7 μm
reaches it at z < 0.2; the Salim et al. curve with a 2175 Å bump reduces
systematic model–data differences at fixed redshift relative to the
Prevot curve used before [src: arXiv:2506.03243, Sect. 6.1]. For
SPHEREx, the Brown-only or COSMOS-only subsets do almost as well as the
full 160 templates for σ̂_z/(1+z) < 0.1, but the high-accuracy sample
(< 0.01) is sensitive to template coverage: Brown templates alone give a
5× higher outlier fraction and 10× larger bias [src: arXiv:2312.04636,
Sect. V.1.2].

### Step 3. Fit, with per-galaxy and per-band calibration factors
<!-- key: step-3-fit-with-per-galaxy-and-per-band -->

BCNz2 writes χ²[z, α] = Σ_NB ((f̃_i − l_i k f_i^Model)/σ_i)² +
Σ_BB ((f̃_i − l_i f_i^Model)/σ_i)² (arXiv:1809.04375, Eq. 4), with
f_i^Model = Σ_j f_i^j(z) α_j (Eq. 5) [src: Sect. 4.2]. The p(z) integral
over amplitudes is replaced by exp(−χ²_min(z)/2) (Eqs. 6–7), minimised
with a non-negative algorithm on 0.01 < z < 1.2 in steps of 0.001
[src: Sect. 4.3.1–4.3.2]; the wide-field run extends the grid to z < 2
[src: arXiv:2312.07581, Sect. 3.1]. The scaling k, needed because COSMOS
uses fixed apertures rescaled to total flux while PAUS uses matched
apertures, has the closed form of Eq. 8, updated every tenth minimisation
step [src: arXiv:1809.04375, Sect. 4.2, 4.3.3].

Zero points l_i, four schemes:

| Scheme | Rule | Iterations, sample | Analysis |
|---|---|---|---|
| Spectroscopic, median ratio | l_i = median(f^Model/f^Obs) at fixed z_s (Eq. 9); median against outliers; no train/validation split since one number per band | 20 iterations, k free | BCNz2 COSMOS [src: arXiv:1809.04375, Sect. 4.3.4, 5.2] |
| Iterative, no spectra | same median ratio evaluated at the previous photo-z | 5 iterations; six equal-number i_AB bins; 10% subsample of clean 40-NB objects | PAUS wide [src: arXiv:2312.07581, Sect. 3.2] |
| Likelihood with spectra | maximise Π N(f_g κ_j − T_g,k, κ_j σ_g) over factors κ_j (Eq. 20), iterated with the line-prior calibration | galaxies with χ² > 120 for ~63 degrees of freedom excluded | Alarcon et al. [src: arXiv:2007.11132, Sect. 3.4] |
| Large SPS grid, outside the code | δm(j) = median(m^obs − m^synth) with the best of 90,720 models (Eq. 2), subtracted and repeated; σ(Δm) = √(π/2N) × scatter (Eq. 4) | until new offsets < 0.001 mag (3–4 iterations); ~500 galaxies with r < 22 per pointing, separately for each of the four pointings | miniJPAS [src: arXiv:2108.03271, Sect. 3.2] |
| Spectroscopic, iterative mean offsets | s_f minimising the mean predicted − observed flux at fixed z_s (Ilbert et al. 2006 procedure) | converged after 3 iterations | COSMOS 30 bands [src: arXiv:0809.2101, Sect. III.3] |
| Spectroscopic, median ratio per CCD, with an excess-scatter term | median template/observed flux ratio at z_s, iterated until < 1% in all filters; synthetic F814W as anchor; BPZ also fits a "zeropoint error" (excess scatter over the photometric error) | galaxies with S/N > 10 in all 24 bands | ALHAMBRA [src: arXiv:1306.4968, Sect. 4.2.1] |
| Photo-z of emission-line galaxies used as z_s | same procedure with BPZ photo-z in place of z_s | m_F814W < 23, all 24 filters, Odds ≥ 0.9, χ² ≤ 1, late types (t_b > 7); used for the ~60% of fields without enough spectra | ALHAMBRA [src: arXiv:1306.4968, Sect. 4.2.2] |
| Spectroscopic, median difference | median predicted − observed magnitude, refitted after each correction | converged in 2 iterations; offsets usually < 0.05 mag, smallest in NIRCam, which anchors the fit | COSMOS2025 [src: arXiv:2506.03243, Sect. 6.1] |

COSMOS2020 runs LePhare's spectroscopic offsets iteratively to
convergence, while EAZY also uses galaxies without spectra, to limit the
spectroscopic selection, and sorts residuals by rest-frame wavelength so
that band offsets and template defects separate; it stops after five
iterations when updates fall below 1% [src: arXiv:2110.13923, Sect. V.1–V.2].
The resulting offsets, normalised to K_s, reach +0.145 to +0.213 mag in
IA679 and −0.07 to −0.20 in IRAC ch1–ch2, and differ between Classic and
The Farmer by up to ~0.1 mag in the optical [src: Table 3].

Why the PAUS wide fields dropped spectra: the spectroscopic scheme needs
spectra, inherits their magnitude and redshift selection (the zero points
follow the brightest bin, where most spectra lie), and uses the same
objects to calibrate and to validate [src: arXiv:2312.07581, Sect. 3.2].
Why miniJPAS recalibrates outside the code: with a handful of archetypes,
high-S/N galaxies keep large χ² after convergence, which widens the
spread of per-galaxy offsets; the large SPS grid fits them far better
[src: arXiv:2108.03271, Sect. 3].
Why ALHAMBRA used emission-line galaxies: only ~40% of its fields had
enough spectra, offsets did not correlate with airmass or PSF and so
could not be transferred between fields, and emission-line photo-z were
robust to zero-point changes; corrections derived on late types also
improved early types [src: arXiv:1306.4968, Sect. 4.2.1–4.2.2]. Split
tests (magnitude, aperture, redshift) agree to < 1% except in F954W, so
the offsets are read as real differences between the stellar calibration
and the HST-calibrated template colours [src: Sect. 4.2.1]. The PAUS
wide fields left spectra for another reason, spectroscopic selection.

### Step 4. Priors
<!-- key: step-4-priors -->

BCNz2 builds priors from the ensemble after a first run: weights on runs
(SED, extinction law, E(B−V)) from the fraction of galaxies whose minimum
χ² falls in each run, and an independent redshift prior from the no-prior
n(z) smoothed by a σ_z = 0.003 Gaussian, which "effectively also
incorporates some clustering information from the field"; a joint SED–z
prior was too noisy [src: arXiv:1809.04375, Sect. 5.4]. No luminosity
prior is used [src: Sect. 5.4]. miniJPAS uses LePhare's VVDS prior
P(z, T | m), replaced at i < 20 by a step function (1 at z ≤ 1, 0 above),
admitted to be unrealistic for luminous z > 1 galaxies in J-PAS [src:
arXiv:2108.03271, Sect. 4.1]. COSMOS2020 LePhare uses only M_B ≥ −24
[src: arXiv:2110.13923, Sect. V.1]. Alarcon et al. cap M_I at −26 through
the top-hat continuum prior, from the brightest zCOSMOS galaxy
[src: arXiv:2007.11132, Sect. 3.3]. ALHAMBRA's BPZ2.0 prior p(z, T | m₀)
is derived per spectral type and magnitude from the GOODS-MUSIC, COSMOS
and UDF redshift distributions [src: arXiv:1306.4968, Sect. 4].
J-PLUS DR4 adapts the VVDS prior to its i band and rest-frame g − i
types; the LePhare step function at i < 20, kept for miniJPAS, gave a
high rate of catastrophic outliers in the shallower J-PLUS, so the VVDS
model is extrapolated to brighter magnitudes and, at i < 16.5 where it
turns unphysical, replaced by exp[−2(z/z_max)²] (Eq. 3) with z_max from
absolute-magnitude limits M_i = −25, −23, −21 for early, intermediate and
late types [src: arXiv:2607.06662, Sect. 3.2]. COSMOS2025 and the SPHEREx
forecast use flat priors on all parameters [src: arXiv:2506.03243,
Sect. 6.1; arXiv:2312.04636, Sect. V].

### Step 5. Point estimate, quality flag and PDF recalibration
<!-- key: step-5-point-estimate-quality-flag-and-pdf -->

- **Point estimate.** BCNz2 and DEEPz report the mode [src:
  arXiv:2312.07581, Sect. 3.1; arXiv:2408.16864, Sect. 3.1]; COSMOS2020
  LePhare reports the median of the likelihood marginalised over templates
  [src: arXiv:2110.13923, Sect. V.1], as does COSMOS2025, which also
  gives the minimum-χ² redshift since the two differ for multimodal
  p(z) [src: arXiv:2506.03243, Sect. 6.1]. BPZ2.0 on ALHAMBRA reports the
  mean, z_b = Σ_T ∫ z p(z, T) dz [src: arXiv:1306.4968, Sect. 4], and the
  SPHEREx forecast the first moment, with highest-posterior-density
  intervals because many p(z) are non-Gaussian; where σ_z approaches the
  grid step (0.002) discretisation starts to matter [src:
  arXiv:2312.04636, Sect. V.1.1]. J-PLUS DR4 recomputes mode, mean,
  median and a random draw from the corrected, compressed p(z)
  [src: arXiv:2607.06662, Sect. 3.3].
- **Quality flags.** ODDS = ∫_{z_b−Δz}^{z_b+Δz} p(z) dz (arXiv:1809.04375,
  Eq. 15) and Q_z = χ²/(N_f − 3) × (z^99 − z^1)/ODDS (Eq. 16). Δz was 0.0035
  for ODDS and 0.01 inside Q_z in the COSMOS paper, 0.035 in the wide-field
  paper [src: arXiv:1809.04375, Sect. 5.5; arXiv:2312.07581, Eq. 6]; check
  which value a quoted "50% best" sample used. ALHAMBRA's Odds integrates
  over ±0.0125(1 + z_b) [src: arXiv:1306.4968, Sect. 4], J-PLUS DR4's
  over ±0.03(1 + z_X) [src: arXiv:2607.06662, Sect. 3.3, footnote 1].
  In J-PLUS the LePhare odds are generally well calibrated (outlier rate
  at |Δz| > 0.03 close to 1 − ⟨odds⟩) but overconfident at odds ≳ 0.9,
  while the neural code is realistic at high confidence and slightly
  overconfident at intermediate odds [src: arXiv:2607.06662, Sect. 5.2].
- **PDF recalibration.** BCNz2 adds a uniform outlier term,
  p_corr = (1 − κ) p + κ p_outlier (Eq. 18), κ = 0.13, because scattered
  light and uncorrected cross-talk violate the Gaussian error model
  [src: arXiv:1809.04375, Sect. 5.6]. The wide fields use the Bordoloi et
  al. remapping p_corr(z) = p(z) N_PIT(ζ(z)) (Eq. 14), valid for the full
  sample only if the spectroscopic sample is representative; before it the
  PIT peaked at the edges, i.e. p(z) too narrow [src: arXiv:2312.07581,
  Sect. 4.4]. miniJPAS convolves p(z) with a Lorentzian kernel (γ = 1.18,
  Eq. 7) and raises it to the power 1/α with α = 0.54, both fitted on the
  whole sample with highest-probability-density intervals; before
  correction faint galaxies were under-confident and r < 19 ones
  over-confident [src: arXiv:2108.03271, Sect. 4.3]. J-PLUS DR4 applies
  the same two operations, with α and γ optimised on its spectroscopic
  training sample, then stores each p(z) as the redshifts of fixed CDF
  quantiles (ColdPress) because full-resolution PDFs for 79 million
  sources are prohibitive [src: arXiv:2607.06662, Sect. 3.3]. The SPHEREx
  and 7DS forecast finds template p(z) relatively well calibrated but
  with confidence intervals generally too narrow, most for bright
  galaxies (**forecast**, mock data) [src: arXiv:2512.24537]. COSMOS2020 multiplies
  flux errors by 2 so that 68% of i < 22.5 spectra fall inside the 1σ
  interval; fainter objects stay underestimated, possibly a spectroscopic
  selection effect, and are not corrected [src: arXiv:2110.13923,
  Sect. V.3]. It also adds 0.02 mag (optical), 0.05 mag (JHK_s, ch1,
  narrow bands) and 0.1 mag (ch2) in quadrature before fitting
  [src: Sect. V.1].

### Step 6. Faint end: combine with broad-band photo-z
<!-- key: step-6-faint-end-combine-with-broad-band-photo-z -->

Beyond i_AB ≈ 22.5 the NB noise is sky-dominated and NB S/N falls to
~1–3, while BB S/N stays roughly flat; NB+BB then does no better than BB
alone [src: arXiv:2312.07581, Sect. 3.4]. The wide-field catalogue
therefore averages the BCNz (NB+BB) and BPZ (BB-only, from the survey
teams) estimates with inverse-variance weights w = 1/σ_68²(i_AB) (Eq. 11),
which also removes artificial n(z) peaks at z_b ~ 0.7–0.8 [src:
Sect. 3.4, 4.2]. The design study already found that at 22.5 < i < 23.7
narrow bands improve the bias but not the precision [src:
arXiv:1402.3220, Sect. 6].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Template or machine learning on the same narrow-band data
<!-- key: template-or-machine-learning-on-the-same-narrow -->

On the PAUS wide fields, DEEPz (autoencoder plus a ten-Gaussian mixture
density network, pre-trained on simulations, trained with on-the-fly
coadds that include each exposure with probability 0.8) and BCNz2 perform
alike to i ≈ 20 and z ≈ 0.3; beyond, DEEPz is better, by up to
0.02(1 + z_s) in σ_68 at i = 23 (W1, W3) [src: arXiv:2408.16864, Sect. 3.1,
4.3]. On the bright G09 sample BCNz2 is better in every case, and adding
COSMOS galaxies to the DEEPz training narrows but does not close the gap;
DEEPz gains with training-set size and number of broad bands [src:
Sect. 4.3]. Pre-training on simulations halves the faint-source scatter
[src: Sect. 3.1]. The errors of the two codes correlate linearly, as
expected from shared photometry [src: Sect. 4.3]. DEEPz precision depends
on which spectroscopic survey dominates the training set (VIPERS against
GAMA_SDSS at equal size, 1760 galaxies each) [src: Sect. 4.2]. The design
study reported that some training codes ran into difficulties with
O(50) filters [src: arXiv:1402.3220, Sect. 1].

Other surveys, other answers on their own data:

- **S-PLUS DR1 (5 broad + 7 narrow bands, with unWISE).** On the same
  test sample (nDet_auto ≥ 8), a Bayesian network with a mixture-density
  output reaches σ_NMAD = 0.0234, bias −0.0010 and 0.64% outliers against
  0.0308, −0.0058 and 2.76% for the survey's template code BPZ2; GPz
  sits between (0.0316, −0.0018, 0.72%) [src: arXiv:2110.13901, Table 4].
  The authors summarise this as 24% lower scatter, 82% lower bias and
  77% lower outlier fraction, and note that only the deep-learning
  methods picked up the "redshift window of opportunity" at
  0.26 ≤ z_s ≤ 0.32, where [O III] and Hα fall in J0660 and J0861
  [src: Sect. 4.3]. The authors adopt the full feature set (magnitudes,
  colours and morphology), stating that all three codes perform better
  with it, although in their Table 3 colours plus morphology give a
  slightly lower σ_NMAD for each code (e.g. 0.02338 against 0.02343 for
  the MDN) [src: Sect. 4.2, Table 3].
- **J-PLUS DR4 (12 bands, r < 22).** On 50,325 spectroscopic galaxies
  with z_s < 1 (the LePhare search range), the neural pipeline LeMoNNADE
  beats LePhare in precision, σ_NMAD and outlier rate at all magnitudes,
  the gap widening at the faint end; LePhare's photo-z are biased high at
  low z and low at high z, which the authors attribute to the prior
  favouring z ~ 0.4–0.5 for faint sources [src: arXiv:2607.06662,
  Sect. 5.2]. Adding WISE lowers quasar catastrophic outliers from ~40%
  to ~23% [src: abstract].
- **SPHEREx mocks (102 bands, forecast).** A probabilistic autoencoder
  with an explicit forward model beats template fitting in source
  recovery, outliers and posterior calibration, with prior-dependent
  trade-offs in redshift performance; template outliers sit on shallow
  likelihoods where the discrete grid gives "artificially confident but
  incorrect" redshifts; an SBI variant matches it at ~200× the
  throughput [src: arXiv:2603.24668]. On SPHEREx + 7DS mocks six codes
  all reach σ_NMAD ≲ 0.005 at 13 < i < 18 [src: arXiv:2512.24537].

The PAUS comparison above (template better on the bright G09 sample,
network better at the faint end) and the S-PLUS and J-PLUS ones (network
better throughout) were made on different depths, band sets and
training samples; none of these papers compares across surveys.

### Joint NB+BB fit, multiplied PDFs, or NB alone
<!-- key: joint-nb-bb-fit-multiplied-pdfs-or-nb-alone -->

Without broad bands BCNz2 confused [O III] with Hα, producing outliers at
Δ_z ≈ ±0.15, mostly scattered low; multiplying separate NB and BB p(z)
(Eq. 14) helps, but the joint fit is better because it constrains one SED
for both systems [src: arXiv:1809.04375, Sect. 5.3].

### Fixed literature line ratios or measured ones
<!-- key: fixed-literature-line-ratios-or-measured-ones -->

Measured ratios and a marginalised line amplitude give σ_68(Δ_z) ≈ 0.003
at i ≈ 18 and 0.009 at i ≈ 23, 3× and 1.66× tighter than COSMOS2015, with
|median Δ_z| ≤ 0.001 at all redshifts and magnitudes considered [src:
arXiv:2007.11132, abstract]. With literature ratios the iterative
zero-point step produced a large colour trend that lifted short-wavelength
fluxes and biased photo-z low [src: Sect. 5]. Residuals by template class
show elliptical models lacking near-infrared flux, so a recalibration
dominated by starbursts can harm ellipticals [src: Sect. 5]. The baseline
these refine: in COSMOS with 30 bands, adding UV-predicted lines with
fixed ratios improved σ_Δz/(1+z_s) from ~0.02 to 0.007, a factor 2.5,
"especially when the medium bands are used" [src: arXiv:0809.2101,
Sect. IV.3].

### Spectroscopic or iterative zero points
<!-- key: spectroscopic-or-iterative-zero-points -->

On W3 the two give the same σ_68 at all i_AB, and five iterations suffice
[src: arXiv:2312.07581, Sect. 4.1]. The iterative scheme frees the
validation sample and allows magnitude-dependent zero points. On miniJPAS
the redshift-split test (offsets from galaxies above and below the
median z agree within their uncertainties) addresses the band–template
degeneracy; a uniqueness test applies random common shifts of ±0.2 mag
per band and expects the recalibration to return them, Δm(j) − Δm*(j) ≈
x(j) (Eq. 5) [src: arXiv:2108.03271, Sect. 3.3]. On ALHAMBRA,
zero points from emission-line photo-z were always slightly worse than
spectroscopic ones and always much better than stellar ones [src:
arXiv:1306.4968, Sect. 4.2.2]. Whatever the scheme, skipping it costs
most: in COSMOS without band offsets, stripes with biases > 0.1 appear
(z_s ~ 0.8 placed at ~0.7), reduced below 0.05 with them [src:
arXiv:0809.2101, Sect. IV.3].

### Ensemble priors
<!-- key: ensemble-priors -->

Gains are small with 40 narrow bands: 10³ σ_68/(1+z) goes from 8.5 to 8.3
(full sample) and 3.9 to 3.7 (best 50%) with SED and redshift priors
[src: arXiv:1809.04375, Table 3].

### Aperture or profile-fitting photometry
<!-- key: aperture-or-profile-fitting-photometry -->

Classic and The Farmer give similar photo-z with the same code; Classic is
slightly better at i < 22.5, The Farmer fainter, and its smaller flux
errors make the faint-end underestimation of photo-z errors stronger
[src: arXiv:2110.13923, Sect. V.3].

### Quality cuts
<!-- key: quality-cuts -->

Cutting on Q_z or ODDS to the best 50% gives σ_68 ≈ 0.004(1+z) at
i < 22.5 [src: arXiv:1809.04375, Sect. 5.5]; a prior χ² cut followed by
ODDS beats ODDS alone at fixed removed fraction [src: Sect. 5.5]. Such cuts
select on data quality, SED and method together, and an ODDS cut has
reproduced SDSS scanning stripes [src: Sect. 5.5]; removing large fractions
can bias clustering [src: arXiv:1402.3220, Sect. 6].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| NB filter set | 40 bands, 4500–8500 Å, 100 Å spacing, 130 Å FWHM as built (design 125 Å) | PAUS | arXiv:2312.07581; arXiv:1402.3220 | Sect. 2.1; Sect. 6 |
| Design target | σ_z/(1+z) = 0.0035 for 50% at i < 22.5; ≤ 0.05 at 22.5 < i < 23.7 | PAUS simulations | arXiv:1402.3220 | Sect. 1, 6 |
| NB calibration consistency | 2% (blue vs all stars); vignetting 8% peak to valley; standards offset ~5% | PAUS | arXiv:2406.06850 | Sect. 4 |
| BCNz2 grid | 0.01 < z < 1.2, Δz = 0.001 (COSMOS); z < 2 (wide) | PAUS | arXiv:1809.04375; arXiv:2312.07581 | Sect. 4.3.2; Sect. 3.1 |
| Zero-point iterations | 20 (spec-z); 5 (iterative, six i bins, 10% subsample) | PAUS | arXiv:1809.04375; arXiv:2312.07581 | Sect. 5.2; Sect. 3.2 |
| PDF outlier fraction κ | 0.13 | PAUS COSMOS | arXiv:1809.04375 | Sect. 5.6 |
| σ_68/(1+z), outliers | 0.0037 for best 50% at i < 22.5; 18% outliers (|Δ_z| > 0.02) for the full sample | PAUS COSMOS | arXiv:1809.04375 | Sect. 5.1 |
| Wide-field σ_68 | 0.019 (BCNz), 0.020 (BCNzw); 1,241,047 objects over 40.99 deg² after mask; outliers defined |Δ_z| > 0.1 | PAUS wide | arXiv:2312.07581 | Table 3, Eq. 9 |
| 66-band photo-z | σ_68 ≈ 0.003 (i ≈ 18), 0.009 (i ≈ 23); |median Δ_z| ≤ 0.001 | PAUS + COSMOS2015 | arXiv:2007.11132 | abstract |
| Line models | 679 models; β medians Eq. 12 | PAUS + COSMOS2015 | arXiv:2007.11132 | Sect. 3.3 |
| COSMOS2020 precision | σ_NMAD ~ 0.01(1+z) at i < 22.5; < 0.025(1+z) at i < 25; outliers |Δz| > 0.15(1+z) | COSMOS2020 | arXiv:2110.13923 | Sect. V.3 |
| COSMOS2020 error floors | 0.02 / 0.05 / 0.1 mag; flux errors ×2 | COSMOS2020 LePhare | arXiv:2110.13923 | Sect. V.1, V.3 |
| miniJPAS recalibration | 90,720 models; ~500 galaxies per pointing; < 0.001 mag after 3–4 iterations | miniJPAS | arXiv:2108.03271 | Sect. 3.1–3.2 |
| miniJPAS templates | 455 candidates → 50; same photo-z for ~98% across runs | miniJPAS | arXiv:2108.03271 | Sect. 4.2 |
| miniJPAS PDF correction | γ = 1.18, α = 0.54; z step 0.002 to z = 1.5 | miniJPAS | arXiv:2108.03271 | Sect. 4.1, 4.3 |
| DEEPz vs BCNz2 | equal to i ≈ 20, z ≈ 0.3; DEEPz better by up to 0.02(1+z_s) at i = 23; BCNz2 better on bright G09 | PAUS wide | arXiv:2408.16864 | Sect. 4.3 |
| Ensemble priors | 10³ σ_68/(1+z): 8.5 → 8.3 (100%), 3.9 → 3.7 (50%) | PAUS COSMOS | arXiv:1809.04375 | Table 3 |
| COSMOS 30-band precision | σ_Δz/(1+z_s) = 0.007 at i < 22.5; 0.012 at i < 24, z < 1.25; 0.06 at i ~ 24 to z ~ 2; 4148 spectra | COSMOS (LePhare) | arXiv:0809.2101 | abstract |
| Effect of lines, offsets | lines: ~0.02 → 0.007; offsets: biases > 0.1 → < 0.05; 3 iterations | COSMOS 30 bands | arXiv:0809.2101 | Sect. III.3, IV.3 |
| COSMOS2025 precision | σ_MAD = 0.012 at m_F444W < 28, ≲ 0.03 in all magnitude, colour and type bins; ~2× better than COSMOS2020 at 26 AB; offsets < 0.05 mag after 2 iterations | COSMOS2025 | arXiv:2506.03243 | abstract; Sect. 6.1 |
| ALHAMBRA precision | σ_NMAD = 0.0106, η(|Δz|/(1+z_s) > 0.2) ≈ 2.7% at F814W < 22.5; 0.0134, 4.0% at < 24.5; ~7200 spectra | ALHAMBRA (BPZ2.0) | arXiv:1306.4968 | Sect. 4.1 |
| ALHAMBRA calibration | stellar ZP a few 0.01 mag; NIR ~0.03 mag; galaxy ZP iterated to < 1%; split tests < 1% | ALHAMBRA | arXiv:1306.4968 | Sect. 2.4, 4.2.1 |
| J-PLUS calibration | ~19 mmag (u, J0378, J0395), ~11 (J0410, J0430), ~8 (others); 1022 deg² | J-PLUS | arXiv:1907.12939 | abstract |
| J-PLUS DR4 catalogue | 79.2 million sources to r = 22; LePhare z grid 0–1, Δz = 0.005; QSO outliers ~40% → ~23% with WISE | J-PLUS DR4 | arXiv:2607.06662 | abstract; Sect. 3 |
| S-PLUS template vs ML | σ_NMAD 0.0308 (BPZ2), 0.0316 (GPz), 0.0249 (DN), 0.0234 (MDN); outliers 2.76%, 0.72%, 0.64%, 0.64% | S-PLUS DR1, 16 < r < 21 | arXiv:2110.13901 | Table 4 |
| SPHEREx (**forecast**) | 19 million galaxies with σ_z < 0.003(1+z), 445 million < 0.1(1+z), 810 million < 0.2(1+z), 3 × 10⁴ deg² | COSMOS2020 + GAMA mocks | arXiv:2312.04636 | abstract, Sect. V.1.1 |
| SPHEREx + 7DS (**forecast**) | σ_NMAD ≲ 0.005, bias ≲ 0.005, failures ≲ 0.005 at 13 < i < 18, all six codes | GAMA + COSMOS mocks | arXiv:2512.24537 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Line confusion.** [O III]/Hα swaps at Δ_z ≈ ±0.15 when broad bands are
  missing or a single line template is used [src: arXiv:1809.04375,
  Sect. 4.5, 5.3]. Test: outlier histogram at ±0.15 against a spectroscopic
  subsample; run with and without the separate [O III] template.
- **Zero points absorbing template errors.** Biased mean model colours
  make the iteration create colour trends and redshift biases [src:
  arXiv:2007.11132, Sect. 5]. Tests: split the recalibration sample at the
  median redshift and compare offsets; inject random band offsets and
  check that they are returned (Eq. 5) [src: arXiv:2108.03271, Sect. 3.3]; inspect residuals
  against rest-frame wavelength and template class [src:
  arXiv:2110.13923, Sect. V.2; arXiv:2007.11132, Sect. 5].
- **Spectroscopic selection in the calibration.** Spec-z zero points
  follow the bright bin; PDF remappings and error rescalings tuned on
  spectra assume representativeness [src: arXiv:2312.07581, Sect. 3.2,
  4.4; arXiv:2110.13923, Sect. V.3]. Test: iterative calibration without
  spectra and per-magnitude zero points.
- **Photometric outliers.** Scattered light and cross-talk produce PIT
  spikes and catastrophic outliers that a Gaussian likelihood cannot
  absorb [src: arXiv:1809.04375, Sect. 5.6]; some 66-band outliers trace to
  unflagged photometry, and fitting individual exposures is proposed
  [src: arXiv:2007.11132, Sect. 5].
- **Telluric and stellar features in NB zero points.** Calibration errors
  cluster near 5170 Å and redward of ~6850 Å [src: arXiv:2406.06850,
  Sect. 4]. Test: compare blue-star-only and all-star zero points per
  filter.
- **Faint-end S/N.** NB information vanishes at i ≳ 22.5; NB+BB precision
  claims should be quoted per magnitude bin and against BB-only
  [src: arXiv:2312.07581, Sect. 3.4].
- **PDF width.** Uncorrected template p(z) were too narrow (PAUS wide),
  mixed under- and over-confident with magnitude (miniJPAS), and too
  narrow at i > 22.5 even after error scaling (COSMOS2020) [src:
  arXiv:2312.07581, Sect. 4.4; arXiv:2108.03271, Sect. 4.3;
  arXiv:2110.13923, Sect. V.3]. Test: PIT and QQ, or HPD coverage, per
  magnitude bin.
- **Mixed metrics.** Outlier thresholds are 0.02 (PAUS COSMOS, DEEPz),
  0.1 (PAUS wide, 66-band) and 0.15(1+z) (COSMOS2020); ODDS windows differ
  by a factor of ten between PAUS papers [src: arXiv:1809.04375, Eq. 13;
  arXiv:2312.07581, Eq. 9; arXiv:2408.16864, Fig. 6 caption;
  arXiv:2110.13923, Sect. V.3]. ALHAMBRA uses |Δz|/(1+z_s) > 0.2 and
  > 5σ_NMAD (Eqs. 12–13) [src: arXiv:1306.4968, Sect. 4.1]; J-PLUS DR4
  |Δz| > 0.15 and f₁ = fraction with |Δz| < 0.01 [src: arXiv:2607.06662,
  Sect. 5.2]; the SPHEREx forecast 3σ outliers relative to each source's
  own reported error [src: arXiv:2312.04636, Sect. V.1.1].
- **Prior tuned for a deeper survey** (J-PLUS, Step 4 and the J-PLUS
  comparison above). Test: photo-z against z_s per magnitude bin with and
  without the prior.
- **Faint end of a mock SPHEREx sample.** At 20.5 < W1 < 21.5, where the
  long-wavelength SPHEREx bands carry little information, recovered
  redshifts are biased low, and quiescent galaxies drive a mild negative
  bias in the low-accuracy bins [src: arXiv:2312.04636, Sect. V.1.1].
- **Using a many-band catalogue as truth.** The 1σ errors of COSMOS2020
  are underestimated beyond i = 22.5 [src: arXiv:2110.13923, Sect. V.3];
  propagate them as in the DES Y6 scheme summarised in L2 rather than
  treating the catalogue as spectroscopic.

## Reading list
<!-- key: reading-list -->

- Foundation: Martí et al. 2014, arXiv:1402.3220 — PAUS filter design and
  why narrow bands help bias more than precision at the faint end.
- Method: Eriksen et al. 2019, arXiv:1809.04375 — BCNz2: line templates,
  NB/BB scaling, zero points, priors, quality flags, PDF outlier term.
- Method: Castander et al. 2024, arXiv:2406.06850 — calibrating a
  narrow-band system with no standards.
- Application: Navarro-Gironés et al. 2023, arXiv:2312.07581 — iterative
  zero points without spectra; PDF remapping; BB weighting at the faint end.
- Method: Alarcon et al. 2020, arXiv:2007.11132 — measured line ratios
  and Bayesian marginalisation over amplitudes on 66 bands.
- Application: Weaver et al. 2022, arXiv:2110.13923 — COSMOS2020 LePhare
  and EAZY configurations, offsets, error rescaling.
- Method: Hernán-Caballero et al. 2021, arXiv:2108.03271 — recalibration
  with a large SPS grid, data-driven template selection, PDF contrast
  correction.
- Critique/comparison: Daza-Perilla et al. 2024, arXiv:2408.16864 — deep
  learning against template fitting on the same PAUS data.
- Foundation: Ilbert et al. 2008, arXiv:0809.2101 — COSMOS 30-band
  LePhare: UV-predicted emission lines and iterative band offsets, the
  template set-up later configurations inherit.
- Data/method: Molino et al. 2013, arXiv:1306.4968 — ALHAMBRA: BPZ2.0,
  zero points from emission-line photo-z. Shuntov et al. 2025,
  arXiv:2506.03243, Sect. 6 — COSMOS2025 LePhare set-up.
- Method: López-Sanjuan et al. 2019, arXiv:1907.12939 — stellar and
  white-dwarf loci calibration. Application: Hernán-Caballero et al. 2026,
  arXiv:2607.06662 — J-PLUS DR4, LePhare against a neural pipeline.
- Comparison: Lima et al. 2021, arXiv:2110.13901 — S-PLUS, machine
  learning against BPZ2 on 12 bands.
- Forecast: Feder et al. 2023, arXiv:2312.04636 (SPHEREx mocks, template
  recovery); arXiv:2603.24668 (autoencoder, SBI); arXiv:2512.24537 (+ 7DS).

## Not verified
<!-- key: not-verified -->

- The PAUS narrow-band image photometry paper (Serrano et al. 2022), and
  the PAUS Gaussian-process (Delight) and multi-task photo-z papers: found
  by search, not read; identifiers not recorded here.
- The original DEEPz paper (Eriksen et al. 2020) and the miniJPAS
  template-optimisation paper in preparation: named, not read.
- SPHEREx: only pre-launch forecasts on mocks were read (arXiv:2312.04636,
  arXiv:2603.24668, arXiv:2512.24537); no photo-z paper on SPHEREx survey
  data was found in a date-restricted search on 2026-10-21. The hybrid
  continuum-plus-line estimator announced in arXiv:2312.04636 (Sect. V)
  was not read.
- The S-PLUS template-fitting precision study (Molino et al. 2019) and
  the J-PLUS Gaia XP recalibration papers were found by search, not read.
- The outcome of the miniJPAS random-shift test (arXiv:2108.03271,
  Sect. 3.3, after Eq. 5) was not read; the dossier states only its design
  and the redshift-split result.
