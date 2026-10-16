# Photometry and photometric redshifts — systematics

Scope: the systematic errors of photometric calibration, photo-z estimation
and n(z) characterisation: mechanism, measured size, mitigation, validation,
and the paper a referee expects.
Snapshot: 2026-10-16

Flags: `[src]` read this session in the abstract of the cited paper;
`[src: Sect. n]`, `[src: Table n]` read in the body; `[sec]` from a named
secondary source; `[der]` derived here.

The size of redshift-distribution errors in each lensing analysis, and the
priors adopted on them, are in `cosmo-weak-lensing`
(`references/systematics.md`, section "Redshift distributions"). This file
covers the mechanisms upstream of those priors.

## 1. Zero-point and flat-field errors
<!-- key: zero-point-and-flat-field-errors -->

**Mechanism.** Errors in per-exposure zero points and in the large-scale
flat field imprint spatial patterns on magnitudes and therefore on colours,
photo-z and target densities. Sky flats alone can be wrong by up to 0.13 mag
peak to valley (arXiv:1111.2058) [src].
**Size after calibration.** About 1% for SDSS ubercal, dominated by
unmodelled atmosphere (arXiv:astro-ph/0703454) [src]; 7 mmag uniformity for
DES Y3 and below 1.8 mmag RMS for the DES Y6 star catalogue
(arXiv:1706.01542, arXiv:2305.01695) [src].
**Validation.** Independent standards: stellar colour regression and
corrected Gaia XP synthetic photometry found position-dependent errors of up
to 15–23 mmag in survey releases that had passed their internal checks
(arXiv:2309.11225, arXiv:2309.11533) [src].
**Referee expects:** Padmanabhan et al. 2008, Burke et al. 2018, and an
external check against Gaia XP or another survey.

## 2. Chromatic errors
<!-- key: chromatic-errors -->

**Mechanism.** The effective passband changes with airmass, water vapour,
aerosols and focal-plane position, so a colour-independent zero point leaves
an error that depends on the source SED and, for galaxies, on redshift.
**Size.** Up to 2% in some DES bands before correction, below 0.3% after
(arXiv:1601.00117) [src]; filter-edge shifts of several nanometres across the
LSSTCam focal plane (arXiv:2606.31822) [src].
Off-axis sources in several cameras have their redshifts overestimated
because interference filters shift with angle of incidence; knowing the mean
wavelength of each passband per observation is almost sufficient to
correct it, because that mean is independent of the source SED; in Phosphoros
on CFHTLS T007 the bias around z = 0.5 falls from Δz ~ 0.04 to ~ 0.02
(Euclid Collaboration: Paltani et al. 2024, arXiv:2310.14716) [src].
**Mitigation.** Forward modelling of passbands per exposure with chromatic
corrections (FGCM, arXiv:1706.01542) [src]; in situ throughput metrology
(arXiv:astro-ph/0604285, arXiv:2606.31822) [src].

## 3. Galactic extinction
<!-- key: galactic-extinction -->

**Mechanism.** Errors in E(B−V) or in R_b shift colours coherently over the
sky; infrared-emission maps also contain the cosmic infrared background, so
the correction is correlated with the extragalactic structure being
measured.
**Size.** SFD normalisation 14% too high (arXiv:1012.4804) [src]; DESI
stellar reddening differs from SFD by up to 80 mmag in E(B−V)
(arXiv:2409.05140) [src]; extragalactic imprints at the millimagnitude level
in nine of ten maps tested (arXiv:1808.03294) [src].
**Mitigation.** Recalibrated coefficients (arXiv:1012.4804), CIB-cleaned maps
(CSFD, arXiv:2306.03926), stellar reddening maps (arXiv:2409.05140) [src];
compare clustering results under two maps.
**Validation.** Cross-correlate the map with spectroscopic tracers in
redshift slices (the clustering-redshift test of arXiv:1808.03294) [src].

## 4. Unrepresentative training and calibration samples
<!-- key: unrepresentative-training-and-calibration -->

**Mechanism.** See physics-and-methods §5.2: volume effects, photometric
pre-selection, redshift-dependent success rates, and confident wrong
redshifts, especially from blends (arXiv:2605.06790) [src: Sect. 2.0.6].
**Size.** In simulated DES Y1 direct calibration, colour cuts not available
to the lensing galaxies bias the weighted mean redshift by Δz ~ 0.015, and
keeping only high-confidence spectroscopic redshifts biases the mean by Δz =
0.005–0.05, of either sign; this is why DES Y1 did not use direct calibration
(Hartley et al. 2020, arXiv:2003.10454) [src]. For cluster lensing,
spectroscopic selection biases empirical p(z) by more than 10%, reducible to
5% by lensing weighting, while shape-catalogue selection gives ≤ 2% (Gruen &
Brimioulle 2017, arXiv:1610.01160) [src]. Incompleteness inside SOM cells
alters n(z) in the DESI recalibration of KiDS-1000 (arXiv:2512.15964) [src].
Photometric noise in the calibration field creates an apparent dependence of
redshift on magnitude at fixed colour (arXiv:2309.13109) [src].
**Mitigation.** Targeted spectroscopy of empty colour cells (C3R2,
arXiv:2106.11367) [src]; restricting to represented cells (KiDS gold,
arXiv:1909.09632) [src]; deep-to-wide noise transfer (arXiv:2601.02005)
[src]; independent clustering redshifts.
**Validation.** KL divergence, Wasserstein distance and PIT histograms are
the most sensitive diagnostics of training-set damage (arXiv:2601.10797)
[src].

## 5. Photo-z selection and shear
<!-- key: photo-z-selection-and-shear -->

Tomographic bins selected on photo-z correlate with shear; propagating shear
responses through the selection (AnaCal) keeps the induced multiplicative
bias within |m| < 3 × 10⁻³ in all five bins for a template and a
machine-learning photo-z on LSST Y10-like blended simulations (Li et al.
2026, arXiv:2610.00999) [src].

## 6. Wrong redshifts in the calibration sample
<!-- key: wrong-redshifts-in-the-calibration-sample -->

**Mechanism.** Training and direct-calibration methods assume every
reference redshift is right. Low-S/N spectra can match a template at a false
redshift (noise near sky lines, a single line misidentified) (Newman &
Gruen 2022, arXiv:2206.13633) [src: Sect. 4.2.2].
**Size.** Repeat observations give failure rates of 0.75% (Q = 3) and 0.15%
(Q = 4) in DEEP2, where ~17% of secure redshifts are Q = 3, and about 1% and
0.2% in zCOSMOS-bright, where Q = 3 is ~58% of the secure set; many-band
photo-z used as truth (COSMOS2015) have catastrophic rates from ~0.6% for
quiescent galaxies at i ~ 22.5 to > 10% for star-forming galaxies at i ~ 24.5
[src: Sect. 4.2.2]. A toy model in which a fraction f_inc of redshifts is
off by Δ shifts the mean by δ⟨z⟩ = f_inc Δ and inflates the width by
δσ ≈ f_inc Δ²/(2σ) [src: Sect. 4.2.2]. For σ = 0.1 and one Δ = 0.5(1+z)
error per thousand, the mean moves by 0.0005(1+z) but σ by 0.0024(1+z),
in tension with the requirement δσ < 0.003(1+z) (the review quotes the mean
requirement as δ⟨z⟩ < 0.002(1+z) here); f_inc must be ≲ 10⁻³, an order of
magnitude below current deep samples [src: Sect. 4.2.2].
**Mitigation.** Use only Q = 4-like redshifts; repeat observations; model
outliers in the n(z) likelihood; cross-check with clustering redshifts,
which do not use the reference redshifts of the target galaxies.

## 7. Sample variance of calibration fields
<!-- key: sample-variance-of-calibration-fields -->

**Mechanism.** At fixed photometry the redshift distribution is broad, and in
a small field it is modulated by the large-scale structure along the line of
sight. NG22 split the error into three terms: variation of the density
n̂_ij of galaxies per colour cell in the field, variation of the true mean
redshift per cell (σ^z_CV,ij), and shot noise σ^z_ij/√N_ij
[src: arXiv:2206.13633, Sect. 4.2.3]. When the wide survey measures fewer
bands than the calibration field, an extra term from the field's
n̂_ij appears, so sample variance hits few-band surveys hardest
[src: Sect. 4.2.3]. A fully sampled deep survey with broad bins
is limited by the cosmic-variance term, so sparse sampling over more area is
preferred [src: Sect. 4.2.3].
**Size.** Cosmic variance is visible between 0.8 deg² CFHTLS Deep fields
(arXiv:astro-ph/0603217) [src]; in GalSBI forward models sample variance
dominates the mean-redshift error for samples brighter than 24 mag
(arXiv:2606.23783) [src]; HSC Y3 includes the cosmic variance of its
calibration fields in the n(z) posterior (arXiv:2211.16516) [src].
**Mitigation.** Deep-field SOM intermediary over several fields
(arXiv:1901.05005) [src]; many-band wide coverage (PAUS, arXiv:2312.07581)
[src]; clustering redshifts over the full footprint.

## 8. Blending
<!-- key: blending -->

**Mechanism and size.** For more than half of Rubin-detected galaxies,
neighbours contribute at least 1% of the flux in their pixels; blending
accounts for roughly 20% of persistent outliers in deep many-band
photometry, and in 1–5% of faint spectroscopic targets a blended emitter
sets the spectroscopic redshift; in DEEP2 at z > 1, more than 5% of targets
have several HST counterparts within 0.75 arcsec (arXiv:2206.13633)
[src: Sect. 4.2.5]. In lensing, a sheared faint blend at z₁ inside a
dominant galaxy at z₀ changes the effective n(z) of the bin; for DES Y3 the
effective mean redshift moves by 0.003 < |δz| < 0.012 [src: Sect. 4.2.5].
**Mitigation.** Image simulations that model blends jointly with shear;
space-based imaging of calibration fields; shear responses propagated
through photo-z selection (arXiv:2610.00999) [src]. Spectral confusion plays
the same role for SPHEREx deep fields (arXiv:2510.01410) [src].

## 9. Clustering-redshift systematics
<!-- key: clustering-redshift-systematics -->

**Mechanism.** w_ps ∝ b_p b_s n_p(z); the bias evolution of the photometric
sample, lensing magnification, and non-linear small-scale clustering all
mimic or distort n(z) (arXiv:2206.13633) [src: Sect. 4.2.6].
- *Magnification.* For a luminosity-function slope of −1, typical of faint
  galaxies, the photometric sample is not magnified; the dominant term is
  magnification of luminous spectroscopic objects by foreground photometric
  galaxies [src: Sect. 4.2.6]. It must be modelled at Stage-IV precision.
- *Small scales.* S/N peaks at small separations, but the 1-halo regime
  forces a minimum separation of 1.5 Mpc in the Euclid pipeline
  (arXiv:2505.10416) [src]; DES Y6 uses 1.5–5 Mpc (arXiv:2510.23565) [src].
- *Bias evolution.* Mitigated by autocorrelations and self-consistency at
  |Δz| < 0.006 on KiDS mocks, but the result depends on the n(z) model:
  replacing the truth by a colour-based n(z) raises biases to |Δz| ~ 0.04
  (arXiv:2007.01846) [src].
- *Reference coverage.* DES Y6 WZ loses power above z ~ 1.1
  (arXiv:2510.23565) [src]; HSC Y3 cross-correlations stop at z = 1.2
  (arXiv:2211.16516) [src].
**Validation.** Agreement with SOM n(z) per bin (DES Y6 within 0.1σ in
cosmology, arXiv:2510.23566; KiDS-Legacy within 2σ per bin,
arXiv:2503.19440) [src].

## 10. Template and population-model mismatch
<!-- key: template-and-population-model-mismatch -->

Template sets that miss real SEDs bias template photo-z; starbursts were 18%
of the CFHTLS spectroscopic sample and 54% of its catastrophic errors
(arXiv:astro-ph/0603217) [src]. Most codes quote 68% intervals that are too
small and are all significantly biased (CANDELS, arXiv:1308.5353) [src].
Forward models carry the same risk at the population level: GalSBI-SPS with
literature parameters has mean-n(z) offsets of 0.01–0.08 before fitting
(arXiv:2505.21610) [src]; the Euclid Q1 pipeline still needs a bias
correction for cosmology (arXiv:2503.15306) [src].

## 11. Photo-z errors in photometric clustering
<!-- key: photo-z-errors-in-photometric-clustering -->

Lens samples need n(z) as much as sources do: in Euclid DR1 the mean of the
clustering-sample n(z) must be known to 0.004(1+z) (arXiv:2604.00805) [src];
spatially varying n(z) biases w(θ) by up to ~10% at small scales in the
highest bin and can shift σ8 by 1.7σ in an LSST-like set-up
(arXiv:2609.15542) [src]. In photometric BAO, typical photo-z uncertainties
shift the measured BAO scale and must be corrected (Saulder et al. 2025,
arXiv:2501.10759) [src].

## Referee checklist
<!-- key: referee-checklist -->

A results section that uses photometric redshifts or calibrated photometry
should state:

1. The photometric calibration: method (ubercal, FGCM, external standards),
   its measured uniformity, and an external check (Gaia XP or SCR).
2. The extinction map and coefficients, and the effect of switching map
   (SFD, CSFD, stellar reddening) on the clustering result.
3. Whether filter curves vary with focal-plane position or time, and how
   that is handled.
4. The photo-z method, its training or template set, and its implicit or
   explicit prior.
5. The calibration sample: depth, completeness, redshift-quality cut,
   number of fields, and the treatment of unrepresented colour cells.
6. Two independent n(z) calibrations (colour-based and clustering-based),
   compared per bin.
7. The n(z) uncertainty model (mean shifts, modes, or an ensemble) and its
   width compared with the survey requirement.
8. Sample variance of calibration fields and its inclusion in the error.
9. Blending: its effect on n(z) and on shear selection.
10. For clustering redshifts: scales used, bias-evolution and magnification
    treatment, redshift coverage of the reference sample.
11. For PDFs: which object is stored (posterior, likelihood, frequentist),
    the storage format, and the PIT or CDE-loss calibration.


## Not verified
<!-- key: not-verified -->
