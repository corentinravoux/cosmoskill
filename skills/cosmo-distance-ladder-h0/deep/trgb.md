# Tip of the red giant branch — cosmo-distance-ladder-h0 dossier

Scope: how a TRGB distance is measured from a colour–magnitude diagram
(field selection, colour band, smoothing, edge detection or luminosity-
function fitting, tip uncertainty, colour standardisation, zero-point
transfer) and how to choose between the CCHP, EDD and CATS procedures that
give different tips from the same images.
Snapshot: 2026-10-17.
From: Chen & Wang 2026 review (arXiv:2606.26831), Sect. 4.1; Verde et al.
2023 review (arXiv:2311.13305), Sects. 2.2.1 and 2.4.3; Freedman & Madore
2023 (arXiv:2309.05618), Sect. 4; CCHP programme (arXiv:2408.06153).

Already in L2, not repeated here: the TRGB physics, the founding papers and
the zero points per filter in `physics-and-methods.md#primary-stellar-indicators`;
the zero-point budgets (CCHP F115W, CATS, F090W) in
`systematics.md#error-budgets-term-by-term`; tip detection, zero points and
reach in `systematics.md#trgb-specific-effects`; the H0 values in
`results.md#local-distance-ladder-three-rung-geometry-stars`; calibrator
sample selection in `systematics.md#choice-and-size-of-the-calibrator-sample`
and `open-questions.md#is-the-local-ladder-value-73-or-70`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Select the field
<!-- key: step-1-select-the-field -->

The tip is an old, low-mass population feature, so blue star-forming
regions must be masked; the "ultimate goal" is agreed, the details are
debated [src: arXiv:2503.11769, Sect. III.3]. Three prescriptions:

| Group | Rule | Stated reason | Place read |
|---|---|---|---|
| CCHP (JWST F115W) | start from the LEDA D25 or SGA-2020 D26 isophote, then dilate or shrink the ellipse while inspecting the CMD, aiming at negligible blue stars, no excess of intermediate-age AGB stars, a clear tip and a slope near expectation; shape fixed; parameters locked while blinded | "the quality of a TRGB measurement is self-evident": power, uni-modality and width of the tip are the best indicator of a good selection | arXiv:2503.11769, Sect. III.3 |
| EDD-style (JWST F090W, NGC 4258) | stars outside the D25 isophote only; same cut applied to artificial stars | isophotal radii are available from all-sky surveys and scale with galaxy size; HI maps used for a previous cut are not available for most SN hosts | arXiv:2401.04776, Sect. IV.1 |
| CATS (HST F814W) | mask regions where the density of blue stars (F606W − F814W < 0.3) exceeds 10% of the frame peak, per 16 arcsec², with a floor of 4 | an automated, frame-specific rule fixed in advance on the GHOSTS sample | arXiv:2304.06693, Sect. II.1.1 |

Sizes: CATS clips 5–20% of SN fields and 20–40% of NGC 4258 fields, with
~10,000 and ~5,000 stars respectively [src: arXiv:2304.06693,
Sect. II.1.1]. Outside D25 in NGC 4258, 23,268 sources pass the cuts, and
blue stars are fewer than 1 in 28 within ± 0.5 mag of the tip [src:
arXiv:2401.04776, Sect. IV.1].

### Step 2. Select a colour band
<!-- key: step-2-select-a-colour-band -->

CATS selects a diagonal CMD band of width 1.0 mag whose centre and slope
(−7 to −5 in F814W against F606W − F814W) maximise the stars in the band
[src: arXiv:2304.06693, Sect. II.1.2]. The F090W calibration uses
F090W − F150W = 1.30–1.75 mag to drop yellow supergiants; 0.5–2.5 mag gives
nearly the same tip [src: arXiv:2401.04776, Sects. IV.3, IV.4, Table 2].

### Step 3. Locate the edge
<!-- key: step-3-locate-the-edge -->

**One-dimensional edge detection (CCHP lineage).** Lee et al. (1993)
convolved the I-band luminosity function with a Sobel filter [−2, 0, +2]
[src: arXiv:1907.05922, Sect. III.3]. CCHP smooths the luminosity
function with GLOESS (Gaussian-windowed locally weighted smoothing),
chosen because it suppresses noise-induced edges in sparse bins, applies a
[−1, 0, +1] kernel, steps through smoothing scales "to ensure that the
peak … was not over-broadened", and weights the filter response inversely
by the Poisson noise of adjacent bins [src: same]. Edges were measured
independently by several team members and compared only at the end [src:
same].

**Two-dimensional edge detection (CCHP, JWST F115W).** In the near
infrared the tip slopes with colour, so the CMD is kept as a smoothed Hess
diagram; the vertical gradient is divided by the horizontal gradient,
because the steep blue edge of the dense RGB could otherwise overpower the
tip, and this works since the F115W tip slope is ≤ −1 mag mag⁻¹; an
ellipse fitted to the strongest contour defines the tip, its angle being a
nuisance parameter [src: arXiv:2503.11769, Sect. IV.1.2].

**CATS.** GLOESS smoothing with σ = 0.1 mag, Sobel filter with Poisson
weighting, and every edge above 60% of the strongest peak retained as a
candidate tip; each tip receives a contrast ratio R, the number of stars
0.5 mag below over those 0.5 mag above the tip [src: arXiv:2304.06693,
Sects. II.1.3–II.1.4]. Foreground extinction is subtracted; internal
extinction estimates are ≲ 0.02 mag [src: same].

**Luminosity-function fitting (EDD lineage).** A broken power law (RGB
below, AGB above the tip) fitted to the stars, by maximum likelihood
(TRGBTOOL), by non-linear least squares on a binned luminosity function, or
by a maximum-likelihood tool without artificial stars [src:
arXiv:2401.04776, Sect. IV.4]. Artificial stars enter the first two to
model incompleteness and photometric errors [src: same].

### Step 4. Assign the tip uncertainty
<!-- key: step-4-assign-the-tip-uncertainty -->

| Method | Rule | Place read |
|---|---|---|
| CCHP HST | quadrature of photometric, edge-detection, AGB-contamination (from artificial-star tests) and metallicity (± 0.01 mag) terms; minimum ± 0.04 mag even when the formal error is ± 0.02 | arXiv:1907.05922, Sect. III.6.1 |
| CCHP F115W | half-width of the tip ellipse perpendicular to the tip, divided by the contrast (stars below/above the ellipse axis): b = 0.10 mag with 40 below and 20 above gives 0.05 mag | arXiv:2503.11769, Sect. IV.1.2 |
| CATS | empirical model of Wu et al. 2022: σ² = {[2e^{1.5(3−R)}/(e^{1.5(3−R)} + 1)] (N₊,₁.₀ − 100)^(−0.1)}² + 0.04², with N₊,₁.₀ the stars within 1 mag below the tip; tips with R < 2 rejected | arXiv:2304.06693, Eq. 2 |
| F090W edge detection | 1,000 bootstrap resamplings | arXiv:2401.04776, Sect. IV.3 |

The CCHP F115W rule gives 0.029 mag for the high-contrast NGC 4258 halo
field, 0.066 mag for NGC 5643 (contrast 1.2) and 0.093 mag for NGC 2442,
the largest [src: arXiv:2503.11769, App. C.3].

### Step 5. Standardise
<!-- key: step-5-standardise -->

- **I band.** CCHP: metal-poor halo tips show negligible slope; the edge
  detector triggers on the bluer, brighter stars; correcting for the slope
  "as in" earlier work did not change precision or accuracy [src:
  arXiv:1907.05922, Sect. III.6.1].
- **Contrast (CATS).** m^{R=4} = m − 0.021 (R − 4) (arXiv:2304.06693,
  Eq. 1), with the slope combined from GHOSTS (−0.023 ± 0.0046) and 11
  NGC 4258 fields (−0.015 ± 0.008); R = 4 is near the SN-host median and
  drops out of H0 if used on both rungs [src: Sect. III.1]. Stated reason:
  whether astrophysical or a measurement effect (asymmetric populations
  push stars to the bright side of the break), the tip must be
  standardised between rungs to avoid a bias when the mean R differs
  between NGC 4258 and the hosts [src: same].
- **Near-infrared colour (CCHP F115W).** M_IR ≃ constant + β(colour)
  (arXiv:2503.11769, Eq. 5), justified because the metallicity effect on
  the tip (0.3 mag in F115W) is much larger than the age effect (0.09 mag)
  in isochrone studies, and becomes more stable for ages above about
  4–6 Gyr [src: Sect. II.3]. The slope is fitted with external HST
  distances (SH0ES-22 Cepheids and CCHP TRGB averaged; masers for NGC 4258)
  but the intercept is discarded, so that JWST distances are not pegged to
  HST ones; residuals show no trend with colour [src: Sects. IV.2.3,
  VII.2.2]. Homogenised F356W/F444W scale: β = −0.863 ± 0.206 mag mag⁻¹,
  colour offset 0.042 ± 0.03 mag, the offset attributed to CO absorption
  near 5 µm [src: Sect. IV.2.3]. Distances are μ_i = m_i + β(c_i − c₀) − M
  (L2).

### Step 6. Transfer the zero point
<!-- key: step-6-transfer-the-zero-point -->

The zero point is the tip measured in NGC 4258 fields with the maser
modulus 29.397 [src: arXiv:2503.11769, Table 4]. In F115W the NGC 4258 tip
is redder than the host fiducial, so the colour slope error enters the
zero point (0.020–0.036 mag) (L2). In F090W the NIRCam zero-point and
DOLPHOT set-up terms (0.02, 0.03 mag) cancel when hosts are reduced the
same way and are left out of the total [src: arXiv:2401.04776, Table 3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Edge detection or luminosity-function fitting; artificial stars
<!-- key: edge-detection-or-luminosity-function-fitting -->

On one NGC 4258 data set the four baseline methods split into 25.04 and
25.07 mag, not by method family but by whether artificial stars are used;
the authors suggest that methods without them trigger on up-scattered tip
stars (photometric error 0.04 mag near the tip), while warning that this
may over-read the result [src: arXiv:2401.04776, Sect. IV.5, Table 2].
Method differences of ~0.04 mag on the same data are "common", and matter
most for NGC 4258, which calibrates many hosts [src: same].

### Smoothing scale and Poisson weighting
<!-- key: smoothing-scale-and-poisson-weighting -->

Unweighted Sobel: no change for σ_S = 0.04–0.12 mag; above 0.12 the tip
blends with a fainter edge [src: arXiv:2401.04776, Sect. IV.3, Fig. 6].
Poisson-weighted Sobel: the tip brightens steadily for σ_S > 0.06 mag with
no apparent cause, as also seen in simulated and LMC luminosity functions;
the authors therefore avoid weighted detectors and recommend testing the
smoothing scale [src: same]. CCHP keeps Poisson weighting and steps the
smoothing scale to avoid over-broadening [src: arXiv:1907.05922,
Sect. III.3]. CATS fixes σ = 0.1 mag and varies it in its variant set
[src: arXiv:2304.06693, Sects. II.1.3, IV].

### Several peaks: choose, average or standardise
<!-- key: several-peaks-choose-average-or-standardise -->

Without contrast weighting, the choice of tip among several peaks moves
H0 by 3.6 in the table (highest edge response 71.7 ± 2.6; highest R 74.1 ±
2.7; average of peaks 75.3 ± 2.5) [src: arXiv:2304.06693, Table 4], and
"by up to 5" in the authors' text [src: Sect. V.2]. CATS
argues that an algorithm fixed a priori is needed because case-by-case
choices can use knowledge of the SN brightness, so a low SN–TRGB dispersion
without one may be "unrealistic" [src: Sect. V.2]. CCHP replies that
several real tips more than 1 mag apart in one host are unphysical, since
the intrinsic tip dispersion should not exceed 0.1 mag; they signal a
failed colour or spatial selection [src: arXiv:2503.11769, App. D.4].

### Contrast standardisation: correction or artefact
<!-- key: contrast-standardisation-correction-or-artefact -->

- **For.** The mean R differs between NGC 4258 fields (weighted 7.2) and
  SN hosts (5.2); ΔR ≈ 2 times 0.021 is 0.042 mag, about 1.6 in H0 [src:
  arXiv:2304.06693, Sect. IV.2]. Selecting the highest-contrast,
  brightest NGC 4258 fields without the same selection in hosts would bias
  H0 [src: Sect. V.2].
- **Against.** R is the ratio of RGB to AGB stars, a population proxy, not
  a contrast; the first derivative of the luminosity function already
  measures contrast; without artificial-star tests, incompleteness that
  differs across the boundary inflates R for brighter edges, more so in
  shallower SN-host data, biasing distances short and H0 high [src:
  arXiv:2503.11769, App. D.2].

### Fixed-fraction or inspected spatial clipping
<!-- key: fixed-fraction-or-inspected-spatial-clipping -->

CCHP: a fixed fraction of the frame's blue-star peak cannot suit galaxies
at different distances and inclinations; in the Antennae (NGC 4038/9),
pointed at star-forming tidal debris, the strictest CATS clip (5%) still
leaves young stars [src: arXiv:2503.11769, App. D.1]. CATS: tips fixed
without an a priori algorithm risk selection with knowledge of the answer
[src: arXiv:2304.06693, Sect. V.2]. The F090W calibration found its tip
insensitive to the spatial cut (outer chips only: 25.05 against 25.04)
[src: arXiv:2401.04776, Sect. IV.3], but LF fits moved by 0.01–0.02 mag
with the cruder cut, "cause for close examination" in lower-S/N data
[src: Sect. IV.4].

### Hosts without a usable tip
<!-- key: hosts-without-a-usable-tip -->

CATS finds no tip with R > 2 within 1 mag of expectation in NGC 5584,
NGC 1309, NGC 3370 and NGC 3021, imaged on their discs for Cepheids, and
drops them; an earlier analysis with other photometry (DAOPHOT) had
measured tips there, and the difference could not be traced because that
catalogue is not public [src: arXiv:2304.06693, Sect. III.1].

### NGC 4258 tip by group
<!-- key: ngc-4258-tip-by-group -->

Corrected for foreground extinction: CATS 25.389 at the mean host R (simple
field mean 25.371 ± 0.041); CCHP 25.347 ± 0.015 from the outer part of one
field; EDD 25.402 ± 0.025 from two other fields with a colour correction of
about −0.02 mag. These give H0 differences of +1.6 (CCHP) and −0.3 (EDD)
relative to CATS [src: arXiv:2304.06693, Sect. V.2]. The calibration field
and its contrast are therefore an analysis choice worth ~1.6 in H0.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| CATS fixed parameters | clip 10% of blue-star peak; band width 1.0 mag; GLOESS σ 0.1 mag; peak threshold 60% | CATS | arXiv:2304.06693 | Sects. II.1.1–II.1.4 |
| Contrast slope | −0.021 ± 0.004 mag per unit R | CATS | arXiv:2304.06693 | Sect. III.1 |
| Mean R, NGC 4258 / hosts | 7.2 / 5.2 (weighted) | CATS | arXiv:2304.06693 | Sect. IV.2 |
| Tip-selection spread without R | 71.7 to 75.3 | CATS | arXiv:2304.06693 | Table 4 |
| Error floor | 0.04 mag | CCHP HST; CATS model | arXiv:1907.05922; arXiv:2304.06693 | Sect. III.6.1; Eq. 2 |
| Six edge-detector variants | agree to ~0.01 mag in IC 1613; ± 0.04 in NGC 1365 (as cited) | CCHP | arXiv:1907.05922 | Sect. III.3 |
| F115W colour slope | −0.863 ± 0.206 mag mag⁻¹; offset 0.042 ± 0.03 mag | CCHP JWST | arXiv:2503.11769 | Sect. IV.2.3 |
| F115W zero point (homogenised) | M = −5.208 at c = 1.549, total 0.036 mag before the maser term | CCHP JWST | arXiv:2503.11769 | Table 4 |
| F115W tip errors | 0.029 to 0.093 mag | CCHP JWST | arXiv:2503.11769 | App. C.3 |
| F090W tip by method | 25.04–25.07 (D > D25); 25.05–25.09 (outer chips) | NGC 4258 | arXiv:2401.04776 | Table 2 |
| F090W smoothing stability | σ_S = 0.04–0.12 mag (unweighted) | NGC 4258 | arXiv:2401.04776 | Sect. IV.3 |
| Stars within 1 mag below tip, F090W | ~3,200 | NGC 4258 | arXiv:2401.04776 | Sect. IV.3 |
| Metallicity vs age effect on F115W tip | 0.3 vs 0.09 mag (isochrones, as cited) | CCHP JWST | arXiv:2503.11769 | Sect. II.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **AGB or supergiant edge taken for the tip.** Shows up as several edges
  or a tip far from expectation. Test: colour band excluding supergiants
  [src: arXiv:2401.04776, Sect. IV.3]; tighter spatial selection [src:
  arXiv:2503.11769, App. D.4].
- **Weighted detector drifting with smoothing.** Test: scan σ_S with and
  without Poisson weighting [src: arXiv:2401.04776, Sect. IV.3].
- **Incompleteness not modelled.** Artificial stars must share the
  spatial selection of the real stars [src: arXiv:2401.04776,
  Sect. IV.1]; methods without them may sit ~0.03 mag bright [src:
  Sect. IV.5].
- **Calibration field unlike host fields.** Different contrast or
  population between NGC 4258 fields and hosts; test: tip against R or
  colour across fields, and compare the field choices of each group [src:
  arXiv:2304.06693, Sect. V.2]. The NGC 4258 fields scatter by 0.071 mag
  before and 0.030 after colour correction in F115W (L2).
- **Circular colour calibration.** Test: residuals of the new distances
  against the external ones as a function of colour [src:
  arXiv:2503.11769, Sect. VII.2.2].
- **Analyst choice informed by SN brightness.** Test: an algorithm fixed
  in advance [src: arXiv:2304.06693, Sect. V.2], or blinding of
  selection, slope and tip detection as in CCHP JWST [src:
  arXiv:2503.11769, Sect. III.3] (blinding in L2).
- **Disc-dominated pointings.** Cepheid-oriented pointings leave little
  halo area; some hosts give no usable tip [src: arXiv:2304.06693,
  Sect. III.1]; programmes targeting TRGB fields from the outset would
  reduce tip errors [src: arXiv:2503.11769, App. C.3].

## Reading list
<!-- key: reading-list -->

- Foundation: Lee, Freedman & Madore 1993, doi:10.1086/173334 — the Sobel
  edge detector.
- Method/application: Freedman et al. 2019, arXiv:1907.05922 — CCHP
  GLOESS + weighted Sobel, error terms.
- Method: Anand et al. 2024, arXiv:2401.04776 — four methods on one data
  set; smoothing and artificial-star tests; F090W zero point.
- Method/application: Hoyt et al. 2025, arXiv:2503.11769 — 2D edge
  detection, colour standardisation, critique of CATS.
- Method/critique: Scolnic et al. 2023, arXiv:2304.06693 — unsupervised
  algorithm, contrast standardisation, NGC 4258 field comparison.
- Application: Li et al. 2025, arXiv:2504.08921 — complete calibrator
  sample (L2).
- Application: Cruz Reyes et al. 2026, arXiv:2602.15421 — Gaia-only
  calibration (L2).

## Not verified
<!-- key: not-verified -->

- Hatt et al. 2017 (GLOESS and Poisson weighting), Wu et al. 2022 (CATS
  optimisation on GHOSTS, origin of Eq. 2), Makarov et al. 2006 and the
  modified TRGBTOOL: cited through the papers above, not read; no
  identifier recorded.
- The earlier TRGB measurements in NGC 5584, NGC 1309, NGC 3370 and
  NGC 3021 (reference [31] of arXiv:2304.06693) were not identified.
- The CCHP blinding protocol details beyond Sect. III.3 of
  arXiv:2503.11769, and Appendix C.1–C.2 (2D fit details), not read.
- Any CATS reply to the 2025 CCHP critique was not searched.
