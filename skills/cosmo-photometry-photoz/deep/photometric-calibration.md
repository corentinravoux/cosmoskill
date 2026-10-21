# Global photometric calibration and standards — cosmo-photometry-photoz dossier

Scope: how a survey's relative photometric calibration is set up and
solved (photometric model, calibration-star selection, the fit and its
degeneracies, non-photometric data, chromatic corrections), how its
uniformity is tested against an external reference, and how to choose
between ubercalibration, forward calibration, stellar-colour or Gaia-XP
standards and in-situ throughput metrology, and how a zero-point error
propagates into photo-z and n(z).
Snapshot: 2026-10-21.
From: Scope file; DES, Rubin LSST and Gaia calibration programmes; Newman &
Gruen 2022 review, Sect. 1.1 (copied from `references/subtopics.tsv`).

Already in L2, not repeated here: the headline precision of SDSS ubercal,
Pan-STARRS1, DES Y3 and Y6 FGCM, J-PLUS/S-PLUS recalibrations, BEST and
CALSPEC (`results.md#photometric-calibration-achieved`,
`surveys-and-data.md#standards-and-reference-catalogues`); the one-paragraph
descriptions of ubercal, FGCM, hardware metrology and stellar standards
(`physics-and-methods.md#photometric-calibration`); the size of chromatic
errors and dust-map issues (`systematics.md#chromatic-errors`,
`systematics.md#galactic-extinction`). Calibration of narrow-band data
without standards and band zero-point recalibration inside photo-z codes
are in `deep/narrow-many-band-photometry.md`. Supernova flux calibration
(cross-survey systems, CALSPEC ties for distances) belongs to
`cosmo-supernovae`.

Symbols. m_inst: instrumental magnitude, −2.5 log₁₀ of counts; Z: zero
point, m = m_inst + Z; a, k, x: system throughput term, extinction
coefficient, airmass; f(i, j): flat-field (illumination) term at focal-plane
position i in season j; S_b^obs(λ): observing passband of band b, a
function of focal-plane position, pointing and time; S_b^std(λ): the
chosen standard passband; δ_b^std: the correction from observed to
standard magnitude; E^gray: residual grey (wavelength-independent)
extinction.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Write the photometric model
<!-- key: step-1-write-the-photometric-model -->

Two forms are in use.

- **Phenomenological (ubercal).** −2.5 log₁₀ 𝒦 = a(t) − k(t) x + f(i, j; t)
  (Padmanabhan et al. 2008, arXiv:astro-ph/0703454, Eq. 3), "a crude
  phenomenological model ... completely adequate for our purposes"
  [src: Sect. III.1]. SDSS fits one a-term and flat per CCD (six camera
  columns, five filters separately), a k-term common to columns, flats as
  2048-element vectors because of drift scanning with an amplifier jump
  (Eq. 4), a- and k-terms constant per night, flats constant per "season"
  between camera maintenance (14 seasons, Table 1) [src: Sect. III.1].
  Sky flats are unusable for SDSS because of scattered light [src:
  Sect. III.1]. Pan-STARRS1 writes Z = a_n − k_n x + f_ij + w(F) (Eq. 9):
  nightly a and k (~200 nights per filter), an illumination term for each
  quadrant of 60 CCDs in four seasons, and a quadratic in image FWHM F
  because flux was lost in very sharp or very broad images [src:
  arXiv:1201.2208, Sect. II.3, Table 3].
- **Forward (FGCM).** The passband S_b^obs(λ) of every exposure and CCD is
  built from measured instrument curves (flats, star flats, superstar
  flats, filter and detector response from the in-situ DECal system) and a
  MODTRAN atmosphere, and each magnitude is moved to a standard passband,
  δ_b^std = m_b^std − m_b^obs (Burke et al. 2018, arXiv:1706.01542,
  Eqs. 7–8) [src: Sect. II–III]. Because Eq. 8 needs the source SED, the
  fit uses a first-order SED expansion F_ν(λ) ≈ F_ν(λ_b) + F'_ν(λ_b)(λ − λ_b)
  (Eqs. 9–11), with λ_b the photon-weighted mean wavelength of the
  instrumental passband (Eq. 12) [src: Sect. II]. Free instrumental
  parameters are only the mirror opacity after each washing and its linear
  rate of change (Eq. 19); atmospheric parameters are ozone, precipitable
  water vapour (PWV) with intra-night terms, aerosol optical depth with
  intra-night terms, and the aerosol index (Eq. 26) [src: Sect. III.1.5,
  III.2.4]. Clouds are not modelled; they enter through grey corrections
  [src: Sect. III.3].

### Step 2. Select calibration stars
<!-- key: step-2-select-calibration-stars -->

| Survey | Selection | Place read |
|---|---|---|
| DES Y6 (FGCM) | isolated stars (no neighbour within 2″), S/N > 10 in at least 2 observations in each of griz, PSF fluxes to avoid local-background offsets for faint stars, colours 0.5 < g − i < 3.5 to constrain the atmosphere, down-sampled in dense regions so the χ² is not dominated by the survey edges | arXiv:2305.01695, Sect. I.2 |
| DES Y3 (FGCM) | ~10 million bright isolated stars, typically 8 visits per band at survey end | arXiv:1706.01542, Sect. I |
| Pan-STARRS1 | repeated stars; error floor 0.01 mag "to prevent a few bright stars from dominating the fit" | arXiv:1201.2208, Sect. II.2 |
| SDSS | repeated stars; error floor 0.01 mag in quadrature | arXiv:astro-ph/0703454, Sect. V.1 |
| J-PLUS (SCR) | LAMOST main-sequence stars, 5500 < T_eff < 6500 K, [Fe/H] > −1, LAMOST g-band S/N > 20, band-dependent magnitude-error cuts (0.01–0.03 mag), Gaia BP/RP excess cut; 237,123 to 280,202 stars per band | arXiv:2309.11225, Sect. III.1 |

The FGCM colour range is a design choice: stars spread along the stellar
locus make the χ² sensitive to both the amplitude and the shape of the
passband, so wrong atmospheric parameters show up as wrong chromatic
corrections even within a single exposure [src: arXiv:1706.01542,
Sect. IV.2].

### Step 3. Solve the fit
<!-- key: step-3-solve-the-fit -->

All methods minimise the weighted scatter of repeated measurements of the
same stars, so the absolute zero point cancels:
Σ_o Σ_i (m_o,i − m̄_o)²/σ_o,i² (arXiv:1201.2208, Eq. 4) [src: Sect. II.2];
FGCM writes the same with standard magnitudes and
σ_phot² = σ_inst² + σ₀², σ₀ = 0.003 mag to protect against underestimated
errors of the brightest stars (arXiv:1706.01542, Eqs. 27–29) [src:
Sect. IV.2].

- **Linear ubercal.** With a linear model the problem becomes
  (1 − W) A p = (W − 1) m_inst (Eq. 7), solved by least squares (Eq. 8);
  the normal matrix A′ᵀC⁻¹A′ splits into per-star sums, so A′ (trillions of
  elements for a billion observations) is never built and stars can be
  processed in parallel [src: arXiv:1201.2208, Sect. II.2].
- **Degeneracies.** The overall zero point, the zero point of each
  disconnected region, the flat-field zero point, and an a–k trade-off at
  constant airmass leave null or near-null eigenvectors. SDSS projects out
  every eigenvector that could cause errors above 1%, solves, then adds the
  null space back by minimising a prior χ² (arXiv:astro-ph/0703454,
  Eqs. 28–29); the eigenvalue threshold is chosen so the calibration does
  not depend on it [src: Sect. III.3]. Pan-STARRS1 does the same with an
  SVD [src: arXiv:1201.2208, Sect. II.2]. Nightly k-terms are kept although
  k varies only ~0.05 mag per airmass between nights and the nightly
  airmass spread is ~0.1 (≈ 5 mmag), because the declination extremes
  must be observed at high airmass and a single k would bias large scales
  [src: Sect. II.3].
- **Non-linear FGCM.** The χ² is minimised with bounded L-BFGS-B and
  analytic derivatives; Y3 used 2552 parameters for 133,265,234 degrees of
  freedom and converged in four cycles of 25, 50, 75 and 125 iterations
  [src: arXiv:1706.01542, Sect. IV.2, IV.4]. The star magnitudes are
  functions of the counts and parameters, not free parameters, so the
  statistic is not rigorously a χ² [src: Sect. IV.4].

### Step 4. Separate photometric from non-photometric data
<!-- key: step-4-separate-photometric-from-non -->

FGCM computes per-star residuals E^gray (Eq. 30), averages them per CCD
(Eq. 31, statistical error ~1–2 mmag, enough to resolve structure above the
~0.2° CCD size) and per exposure (EXP^gray, VAR^gray; Eqs. 33–34), and
removes occulted exposures after each cycle with a cut set on the
non-occulted side of the EXP^gray distribution; 2–3% of candidate
exposures are removed per cycle, halving the bias each time, ending at a
Gaussian peak μ ≈ 0.5 mmag and width σ ≈ 5 mmag [src: arXiv:1706.01542,
Sect. IV.3–IV.4]. About 80% of exposures are photometric in Y3 and in Y6
[src: Sect. III.3; arXiv:2305.01695, Sect. I.2]. Cutting too tightly
biases the star magnitudes in the opposite sense to thin cloud left in the
sample, which is why a final grey correction per CCD and exposure is
applied rather than relying on the cut [src: arXiv:1706.01542,
Sect. IV.4]. Non-photometric exposures are then tied to the star network to
get zero points and chromatic terms for every CCD and exposure with
enough overlap [src: arXiv:2305.01695, Sect. I.2].

### Step 5. Apply chromatic corrections
<!-- key: step-5-apply-chromatic-corrections -->

Integrated corrections for 50,000 random exposure–CCD pairs of Y3 range
from 1–2 mmag (blue stars in i, z) to 40–50 mmag (red stars in g); the
linearised correction cuts the residual by factors of 2–10, to an RMS of
~2 mmag, ~5 mmag for g − i ≈ 3 stars in g [src: arXiv:1706.01542,
Sect. V.4]. The linear form is used in the fit because the full integral at
every χ² evaluation is too slow [src: Sect. V.4]. FGCM delivers passbands
for nearly all exposures on calibratable nights, so corrections can be
computed for known or hypothetical SEDs, including galaxies, not only from
measured colours [src: Sect. IV.3].

### Step 6. Test uniformity against an external reference
<!-- key: step-6-test-uniformity-against-an-external -->

| Survey | Reference | Procedure | Result | Place read |
|---|---|---|---|---|
| DES Y3 | Gaia DR1 G | fit a weighted combination of DES g, r, i passbands to the Gaia G response; stars with 0.5 < g − i < 1.5; mean difference per HEALPix NSIDE = 256 pixel | Gaussian σ = 6.6 mmag; structure from both surveys | arXiv:1706.01542, Sect. V.3 |
| DES Y6 | Gaia DR3 G | G synthesised from griz, 0.5 < g − i < 1.5, G < 20, per NSIDE = 128 pixel (≈ 0.21 deg²) | RMS 1.8 mmag; main features follow Gaia scans, not DES pointings; offsets up to 1% at the Galactic-bulge edge (~5% of the area), origin unresolved | arXiv:2305.01695, Sect. II |
| Pan-STARRS1 | SDSS stars (m < 18) transformed to PS1 | per-exposure zero point from SDSS against the internal one, solved without SDSS | agreement 7 mmag (r) to 13 mmag (y); maps show SDSS 3° scan stripes and PS1 rectangles | arXiv:1201.2208, Sect. III.2 |
| J-PLUS DR3 | SCR (LAMOST + Gaia) and corrected Gaia XP synthetic photometry (XPSP) | per-tile second-order polynomial star flat fitted to model − observed magnitudes | SCR vs stellar locus σ = 2.4–3.9 mmag (griz), 6.5–15.2 (blue), 3.2–3.9 (red); SCR vs corrected XPSP ~1 mmag (griz), 3–5 (blue) | arXiv:2309.11225, Sect. III, IV.3, IV.5 |
| SDSS | internal | χ = (m − ⟨m⟩)/σ unit-Gaussian at the faint end; residuals about the flat vector ~0.5% | — | arXiv:astro-ph/0703454, Sect. V.1 |

The SDSS paper also maps the eigenmodes of the curvature matrix onto the
sky: no simple large-scale mode apart from the exact zero point survives,
showing a well-connected survey, and typical modes are stripes along the
scan direction because camera columns are calibrated separately; the
unfitted dk/dt produced a coherent tilt across the survey in simulations
[src: arXiv:astro-ph/0703454, Sect. V.2]. Pixel size matters when
comparing uniformity numbers: Y3 used NSIDE 256, Y6 NSIDE 128.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Phenomenological or forward model
<!-- key: phenomenological-or-forward-model -->

Ubercal fits a few terms per night and season and is linear; its SDSS
precision was limited by unmodelled atmospheric variation (L2:
`physics-and-methods.md#relative-calibration-from-repeated-stars`). FGCM
fits physical atmospheric parameters and delivers per-exposure passbands
and chromatic corrections, at the cost of a non-linear fit and dependence
on instrument measurements (DECal) and on the atmosphere model [src:
arXiv:1706.01542, Sect. III, IV]. For Y6 the GPS water-vapour constraint
used in Y3 was dropped, and aperture (PSF-wing) effects and a linear
chromatic mirror degradation between recoatings were added [src:
arXiv:2305.01695, Sect. I.2; arXiv:1706.01542, Sect. IV.5.3]. The Y6
uniformity is attributed to DECam stability and a simple strategy of
equal 90 s exposures [src: arXiv:2305.01695, Sect. II].

### Internal network or external standards
<!-- key: internal-network-or-external-standards -->

SCR predicts each star's intrinsic colours from LAMOST T_eff and [Fe/H],
C₀ = C − R E(G_BP − G_RP) (arXiv:2309.11225, Eq. 1), giving
m_SCR = G_BP,RP − C₀^mod(T_eff, [Fe/H]) − R E(G_BP − G_RP) (Eq. 2); reddening
comes from the star-pair method rather than SFD because of SFD's
low-latitude limits and spatially dependent errors [src: Sect. III.1].
XPSP integrates corrected Gaia XP spectra through the passband (Eq. 3),
extrapolated linearly below 336 nm for the u band [src: Sect. III.2]. SCR
covers 91% of J-PLUS tiles (the LAMOST footprint), XPSP all; the final
zero point uses SCR inside and XPSP outside [src: Sect. III.2].
Uncorrected XP spectra agreed with SCR only to 1–2 mmag (griz) and 4–9
mmag (blue), with magnitude-, colour- and extinction-dependent errors;
the correction halves the disagreement [src: Sect. IV.4–IV.5]. Residual
extinction dependence in the blue bands traces spatial variation of the
extinction law at E(G_BP − G_RP) > 0.12 [src: Sect. IV.4]. The stellar-locus
method's errors were partly inherited from PS1 systematics (J-PLUS and PS1
r agree to better than 2 mmag in their systematic pattern) and partly
metallicity dependent [src: Sect. IV.3].

### Uniformity is not the absolute scale
<!-- key: uniformity-is-not-the-absolute-scale -->

FGCM and ubercal fix relative calibration only; the absolute zero point is
an exact degeneracy fixed by a prior or an external tie [src:
arXiv:astro-ph/0703454, Sect. III.3; arXiv:1201.2208, Sect. III.2]. The
DES absolute tie is in L2.

### Laboratory curves or in-situ metrology
<!-- key: laboratory-curves-or-in-situ-metrology -->

Rubin's Collimated Beam Projector (CBP) requirements: 300–1100 nm, output
bandwidth below 1 nm, collimated beam pivoting about its pupil, all
LSSTCam CCDs illuminated in one pointing, stability over ten years [src:
arXiv:2606.31822, Sect. 2.2]. First results: percent-level differences
between CBP-measured and tabulated relative detector QE over 400–860 nm,
"insufficient for the per-mil precision" FGCM needs; near-infrared fringing
above 800 nm exceeds 5%; CBP transmission and a vignetting model are the
outstanding ingredients [src: Sect. 4, 6]. The angle-of-incidence blue
shift of filter edges has only an initial measurement [src: Sect. 6].

## How a zero-point error propagates
<!-- key: how-a-zero-point-error-propagates -->

- **Template photo-z.** Zero-point errors "may create discontinuities not
  reproduced by the templates"; on CFHTLS D1 they left a systematic offset
  at z_s < 0.5 [src: arXiv:astro-ph/0603217, Sects. 3.3, 4.1]. Offsets
  fitted on 468 bright spec-z galaxies stay below 0.1 mag (mean 0.042);
  with template optimisation they remove the trends (σ = 0.037), and the
  catastrophic fraction falls by 2.3 over the three steps, the prior
  included, not by the offsets alone [src: Table 1, Sect. 5.1].
- **Lensing n(z).** DES Y3 perturbs deep-field magnitudes by their
  zero-point errors (u 0.0548, griz 0.0039, JHK_s 0.0054 mag) and reruns
  SOMPZ: the spread peaks where the 4000 Å break crosses a filter, and the
  ⟨z⟩ term is 0.010, 0.005, 0.002, 0.002 (bins 1–4; all terms 0.012,
  0.008, 0.006, 0.009), u-dominated at low z [src: arXiv:2012.08566,
  Sect. 5.3, Fig. 15, Table 2]. DES Y6 (u 0.055 mag) finds it largest in
  bin 1 and rising again in bin 4, as a fixed magnitude error maps to a
  larger redshift error at high z [src: arXiv:2510.23566, Sect. 5.2].
- **Clustering n(z) and density.** For DES Y6 MagLim++ the term is largest
  in bin 6 on ⟨z⟩ and σ₆₈ and moderate in bin 2 (g–r transition, z ~ 0.4)
  [src: arXiv:2509.07964, Sect. IV.2]. A varying calibration field breaks
  the isotropy of the observed density and couples multipoles
  [src: arXiv:1211.1015, Sect. II.2, Eq. 17]; sizes in
  `deep/chromatic-extinction.md#how-an-error-propagates`. Wide-field
  residuals enter clustering through imaging weights (`cosmo-data-pipelines`).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| FGCM error floor σ₀ | 0.003 mag | DES Y3 | arXiv:1706.01542 | Eq. 28 |
| FGCM fit size | 2552 parameters, 133,265,234 d.o.f., 4 cycles | DES Y3 | arXiv:1706.01542 | Sect. IV.4 |
| Exposure rejection per cycle | 2–3%; final EXP^gray μ ≈ 0.5, σ ≈ 5 mmag | DES Y3 | arXiv:1706.01542 | Sect. IV.4 |
| Photometric fraction | ~80% of exposures | DES Y3, Y6 | arXiv:1706.01542; arXiv:2305.01695 | Sect. III.3; Sect. I.2 |
| CCD grey statistical error | ~1–2 mmag | DES Y3 | arXiv:1706.01542 | Sect. IV.3 |
| Chromatic correction size | 1–2 to 40–50 mmag; linear residual ~2 mmag (~5 for g − i ≈ 3 in g) | DES Y3 | arXiv:1706.01542 | Sect. V.4 |
| Uniformity vs Gaia | 6.6 mmag (DR1, NSIDE 256); 1.8 mmag (DR3, NSIDE 128); up to 1% near the bulge | DES Y3; Y6 | arXiv:1706.01542; arXiv:2305.01695 | Sect. V.3; Sect. II |
| Y6 star selection | S/N > 10 in ≥ 2 visits per griz band; 0.5 < g − i < 3.5; no neighbour within 2″ | DES Y6 | arXiv:2305.01695 | Sect. I.2 |
| PS1 model | ~200 a, ~200 k, 4 × 60 × 4 flat, 2 FWHM parameters per filter; error floor 0.01 mag | Pan-STARRS1 | arXiv:1201.2208 | Table 3, Sect. II.2 |
| PS1 vs SDSS zero points | 7 (r) to 13 (y) mmag | Pan-STARRS1 | arXiv:1201.2208 | Sect. III.2 |
| Nightly k variation | ~0.05 mag per airmass; ~5 mmag if ignored | Pan-STARRS1 | arXiv:1201.2208 | Sect. II.3 |
| SDSS eigenmode cut | modes able to cause > 1% errors projected out | SDSS | arXiv:astro-ph/0703454 | Sect. III.3 |
| SDSS flat residuals | ~0.5% about the flat vector | SDSS | arXiv:astro-ph/0703454 | Sect. V.1 |
| SCR vs corrected XPSP | 0.9–1.6 mmag (g, r, i, z and red NB), 4.4–5.4 (u, J0378, J0395) | J-PLUS DR3 | arXiv:2309.11225 | Sect. IV.5 |
| CBP requirements | 300–1100 nm, < 1 nm bandwidth, full focal plane per pointing | Rubin | arXiv:2606.31822 | Sect. 2.2 |
| QE and fringing | percent-level QE offsets vs laboratory; fringing > 5% above 800 nm | Rubin LSSTCam | arXiv:2606.31822 | Sect. 6 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Survey-strategy imprint.** Calibration errors correlate in time and
  are printed on the sky by the tiling: ~2° structures in DECam data
  where few visits exist, scan-direction stripes in SDSS, scan patterns
  in PS1 and Gaia maps [src: arXiv:1706.01542, Sect. V.3;
  arXiv:astro-ph/0703454, Sect. V.2; arXiv:1201.2208, Sect. III.2]. Test:
  map residuals against an external reference in HEALPix pixels and
  look for the pattern of each survey.
- **Disconnected or weakly connected regions.** Their relative zero points
  are unconstrained [src: arXiv:astro-ph/0703454, Sect. III.3]. Test:
  eigenmode analysis of the curvature matrix, projected on the sky.
- **Too few airmasses or one global k.** a–k degeneracy, large-scale
  errors at the declination limits [src: arXiv:astro-ph/0703454,
  Sect. III.3; arXiv:1201.2208, Sect. II.3].
- **Thin cloud in the photometric set.** An asymmetric tail of EXP^gray;
  iterate the selection, then apply grey corrections [src:
  arXiv:1706.01542, Sect. IV.3–IV.4].
- **Bright stars dominating.** Underestimated bright-star errors; add an
  error floor (0.003 mag FGCM, 0.01 mag PS1 and SDSS) and check that χ is
  unit-Gaussian at the faint end [src: arXiv:1706.01542, Eq. 28;
  arXiv:1201.2208, Sect. II.2; arXiv:astro-ph/0703454, Sect. V.1].
- **Reference with its own systematics.** Uncorrected Gaia XP spectra
  carry magnitude-, colour- and extinction-dependent errors; stellar-locus
  calibrations inherit PS1 patterns and metallicity trends [src:
  arXiv:2309.11225, Sect. IV.3–IV.4]. Test: compare two independent
  external routes (SCR and corrected XPSP) per band.
- **Extinction-law variation.** Residual zero-point correlations with R_V
  in high-extinction tiles (E(G_BP − G_RP) > 0.12) [src: arXiv:2309.11225,
  Sect. IV.4]. Test: residuals against E and R_V per tile.
- **Unresolved edge offsets.** DES Y6 shows up to 1% at the bulge edge
  without an identified cause (DES, Gaia, reddening or background) [src:
  arXiv:2305.01695, Sect. II]. Mask or flag such regions for
  colour-sensitive work.
- **Laboratory response curves.** Percent-level QE differences and
  fringing make tabulated curves inadequate for per-mil forward
  calibration [src: arXiv:2606.31822, Sect. 6]. Test: in-situ
  monochromatic measurements, filter-in and filter-out.
- **Chromatic residuals for extreme colours.** Linearised corrections
  leave ~5 mmag for very red stars in g [src: arXiv:1706.01542,
  Sect. V.4]. Use the delivered passbands with explicit SEDs where
  colours are extreme [src: Sect. IV.3].

## Reading list
<!-- key: reading-list -->

- Foundation: Padmanabhan et al. 2008, arXiv:astro-ph/0703454 — the
  ubercal model, degeneracies and eigenmode treatment, error-mode maps.
- Method: Schlafly et al. 2012, arXiv:1201.2208 — scalable linear solution,
  FWHM term, nightly k, external check against SDSS.
- Method: Burke et al. 2018, arXiv:1706.01542 — FGCM: standard passbands,
  linearised chromatic corrections, cycle-wise selection, grey corrections,
  Gaia uniformity test.
- Application: Rykoff et al. 2023, arXiv:2305.01695 — DES Y6 star
  selection, changes since Y3, 1.8 mmag Gaia DR3 test.
- Method/critique: Xiao et al. 2023, arXiv:2309.11225 — SCR and corrected
  Gaia XP standards; errors of the stellar-locus method and of uncorrected
  XP spectra.
- Method: Amouroux et al. 2026, arXiv:2606.31822 — Rubin in-situ throughput
  requirements and first results.
- Foundation: Stubbs & Tonry 2006, arXiv:astro-ph/0604285 — the case for
  in-situ throughput metrology (summarised in L2).

## Not verified
<!-- key: not-verified -->

- The DES Y3 Gold calibration update cited by arXiv:2305.01695 ("Abbott et
  al. 2021"), where the FGCM improvements are described in detail: not read;
  no identifier recorded.
- FGCM Appendix D (exact selection thresholds for calibration exposures
  and calibratable nights) and the PWV and aerosol functional forms
  (Eqs. 21–25 of arXiv:1706.01542): not read.
- Rubin LSST's production calibration (FGCM on LSSTCam data) and any
  published uniformity number for Rubin data: no paper found in the search
  of 2025–2026 work.
- The Gaia XP correction paper used by arXiv:2309.11225 and the BEST
  standards body (arXiv:2601.05486): not read for this dossier.
- Outlier rates as a function of a wide-field zero-point error, for
  template or machine-learning photo-z: no paper read here isolates them
  (arXiv:astro-ph/0603217 reports the combined effect of offsets, templates
  and prior). KiDS-Legacy zero-point propagation into n(z): no passage
  found in arXiv:2503.19440 by term search; not read further.
