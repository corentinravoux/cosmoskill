# Weak lensing — systematics

Scope: the canonical systematic effects of cosmic shear and galaxy–galaxy
lensing: mechanism, measured size, mitigation, validation test, and the paper
a referee expects.
Snapshot: 2026-10-12

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here. A flag that names a place, as in
`[src: Table 2]` or `[src: Sect. 5.2.4]`, marks a statement read in the body
of the paper at that place; a bare `[src]` was read in the abstract.

Convention used throughout: the observed shear is modelled as γ_obs = (1 + m)
γ_true + c, with multiplicative bias m and additive bias c;
redshift-distribution errors are summarised per tomographic bin by a shift Δz
of the mean, n_i(z) → n_i(z − Δz_i) (the STEP convention: Heymans et al. 2006,
arXiv:astro-ph/0506112).

## 1. Shear measurement bias (noise, model, selection)
<!-- key: shear-measurement-bias-noise-model-selection -->

**Mechanism.** Ellipticity is a non-linear function of noisy pixels, so its
expectation is biased (noise bias); an assumed galaxy model that does not
match real morphology biases the fit (model bias); any selection that
correlates with the shear (detection, S/N or size cuts) biases the mean
(selection bias).

**Mitigation.** Two families. (a) Calibrate a given estimator on image
simulations: lensfit in CFHTLenS and KiDS (Miller et al. 2013,
arXiv:1210.8201), calibrated with simulations that emulate the data, where
lensfit is found unbiased within a 2 per cent tolerance (Kannawadi et al.
2019, arXiv:1812.03983) [src], and, for KiDS-Legacy, with the multi-band
SKiLLS simulations that calibrate shear and redshift jointly (Li et al. 2023,
arXiv:2210.07163). (b) Self-calibrate on the data by measuring the response of
the estimator to an artificial shear: metacalibration (Huff & Mandelbaum 2017,
arXiv:1702.02600; Sheldon & Huff 2017, arXiv:1702.02601), used for DES Y1
(alongside im3shape; 1σ uncertainties on m of 0.013 and 0.025 respectively)
and Y3 (arXiv:1708.01533, arXiv:2011.03408) [src: abstract], and for DECADE
(arXiv:2502.17674) [src], and metadetection, which also re-runs
detection on the sheared images and so removes shear-dependent detection bias
(Sheldon et al. 2020, arXiv:1911.02505), used for DES Y6 on cell-based coadds
(Yamamoto et al. 2025, arXiv:2501.05665) and planned for Rubin (Sheldon et al.
2023, arXiv:2303.03947). Analytic-response estimators are a third route (Li &
Mandelbaum 2023, arXiv:2208.10522).

**Size.** Metacalibration removes calibration bias to a few tenths of a per
cent on the GREAT3 simulations (arXiv:1702.02600) [src: abstract]. Without a detection
step it leaves a bias of a few per cent at the galaxy densities of current
surveys, growing with density, which metadetection reduces to at most a few
tenths of a per cent (arXiv:1911.02505) [src: abstract]. The DES Y6 metadetection
catalogue has no detectable multiplicative bias: m = (3.4 ± 6.1) × 10⁻³, the
uncertainty being quoted at 3σ (arXiv:2501.05665) [src: abstract]. The Rubin requirement
is at the 0.1% level (arXiv:2303.03947) [src: abstract]. Metacalibration applied to
KiDS-1000 and tested on SKiLLS gives |m| < 0.017 in every tomographic bin with
negligible additive bias, and its calibration is nearly insensitive to galaxy
properties; the cosmology does not move (S8 = 0.789 +0.020/−0.024 against
0.776 with lensfit) (Yoon et al. 2025, arXiv:2510.01122) [src: abstract].

**Multiplicative and additive bias as used in the main analyses.** One row
per analysis; the place read is given in each cell.

| Analysis | m per tomographic bin | How it enters the fit | Additive term |
|---|---|---|---|
| KiDS-1000, lensfit (Asgari et al. 2021, arXiv:2007.15633) | −0.009 ± 0.019, −0.011 ± 0.020, −0.015 ± 0.017, 0.002 ± 0.012, 0.007 ± 0.010 [src: Table 1] | uncertainty absorbed in the covariance, the five bins taken as fully correlated; KV450 had used σ_m = 0.02 in every bin [src: Sect. 4.2.1] | for ξ± only, a constant δ_c with prior 0 ± 2.3 × 10⁻⁴ [src: Table 2] |
| DES Y3, metacalibration (arXiv:2105.13543) | −0.006 ± 0.009, −0.020 ± 0.008, −0.024 ± 0.008, −0.037 ± 0.008; mean shear response ⟨R_γ⟩ from 0.764 to 0.615 and selection response ⟨R_s⟩ from 0.005 to 0.015 from the first to the last bin [src: Tables 1 and 2] | Gaussian priors, sampled, ξ_obs = (1 + m_i)(1 + m_j) ξ [src: Eq. 21] | mean shear ⟨e₁⟩ = 3.2 to 4.1 × 10⁻⁴ per bin, "too large in some redshift bins to be consistent with shape noise and cosmic variance", source unidentified, subtracted per bin and component [src: Table 1, App. A.3] |
| HSC Y3, reGauss calibrated on image simulations (arXiv:2304.00702) | residual Δm_i with prior N(0, 0.01) in each of the four bins, the calibration being "controlled below the 1% level" [src: Sect. IV.4, Table 2] | sampled, ξ → (1 + Δm_i)(1 + Δm_j) ξ [src: Eq. 23] | none subtracted; a four-parameter PSF additive model is sampled (section 3) |
| KiDS-Legacy, lensfit calibrated on SKiLLS (arXiv:2503.19441) | −0.023 ± 0.006, −0.016 ± 0.006, −0.011 ± 0.007, +0.020 ± 0.007, +0.030 ± 0.008, +0.045 ± 0.009 [src: Table 1] | not sampled: an additional covariance term C_mult [src: Sect. 2.6, Eq. 22]; m and δz come from the same simulation realisations and show no cross-covariance [src: Sect. 3.5] | weighted mean ellipticity subtracted per bin, component and hemisphere, 3.4 to 10.3 × 10⁻⁴ in absolute value, of opposite sign in the two hemispheres [src: Table 2] |
| DES Y6, metadetection with image simulations that shear by redshift (arXiv:2602.10065) | −0.0034 ± 0.0058, 0.0065 ± 0.0066, 0.0159 ± 0.0059, 0.0017 ± 0.0122 [src: Sect. II.3, Table 2] | Gaussian priors correlated with the seven redshift-mode parameters through an 11 × 11 covariance [src: Sect. IV.4] | a mean residual shear "beyond cosmic variance and above what was measured in image simulations", of unexplained origin, subtracted per object; worth Δχ² = 0.14 and less than 0.3σ in S8 on a synthetic data vector [src: App. A.3] |

What these priors cost. DES Y3: dropping the shear-calibration correction and
its uncertainty altogether biases S8 low by 0.5σ, and an extra 1% bias fully
correlated between bins changes nothing (arXiv:2105.13543) [src: Sect. XI];
the Y3 calibration applied to the Y1 data vector raises the Y1 S8 [src: Sect.
IX.5]. DES Y6: fixing m changes σ(S8) only from 0.015 to 0.014 (NLA) and from
0.017 to 0.016 (TATT) (arXiv:2602.10065) [src: Sect. VI.3]. KiDS-1000: free m
per bin, correlated or not, and setting σ_m to zero all leave Σ8 within the
0.1σ scatter between chains (arXiv:2007.15633) [src: Sect. 4.2.1, 4.2.3].

The requirements on m, c and the bin centroids, and the size of noise bias,
are in `physics-and-methods.md` section 4.

**Validation.** Image simulations with known shear; mean shear and tangential
shear around random points and stars; shear as a function of galaxy and
observing properties; cross-pipeline comparison on the same data.

**Referee expects:** arXiv:1702.02601 and arXiv:1911.02505 for the method; the
survey's own shape-catalogue and image-simulation papers for m and its
uncertainty.

## 2. Blending
<!-- key: blending -->

**Mechanism.** Overlapping galaxies are detected as one object or contaminate
each other's light. When the blended galaxies are at different redshifts the
shear response is a mixture, so blending couples the shear calibration to the
redshift distribution: m becomes redshift-dependent and the effective n(z)
changes.

**Size.** In the DES Y3 image simulations blending-related effects are the
dominant contribution to a mean multiplicative bias of about −2% (MacCrann et
al. 2022, arXiv:2012.08567) [src: abstract], and the blending corrections shift the DES
Y3 best-fit S8 by 0.5σ without a substantial increase in uncertainty (Amon et
al. 2022, arXiv:2105.13543) [src: abstract].

**Sizes in the main analyses.**

| Analysis | What was read |
|---|---|
| DES Y3 (arXiv:2105.13543) | effective distribution n_γ(z) = [1 + F(z)] n_obs(z) + G(z), F for redshift-dependent multiplicative effects, G for the response to light sheared at another redshift [src: Eq. 22]; redshift-dependent blending is the dominant contributor to the shear calibration, "in some regimes by factors of several" [src: Sect. IV]; the redshift-mixing part alone is subdominant for the cosmology [src: Sect. XI] |
| DES Y6 (arXiv:2602.10065) | blending shifts the mean redshifts by Δz = −0.013, −0.021, −0.002, −0.034, "relatively large compared to DES Y3" (more blending, fainter samples, their weights in the redshift calibration) [src: Sect. II.3]; ignoring the redshift-dependent part has "little impact on overall cosmology" [src: Sect. VII.2.2] |
| KiDS-Legacy (arXiv:2503.19441) | SKiLLS includes a redshift-dependent shear, of negligible importance for m and the redshift bias at that sensitivity [src: Sect. 3.5] |
| HSC Y3 (arXiv:2304.00702) | the bias from blends at different redshifts is stated to be small [src: Sect. IV.4] |

**Mitigation and referee reference.** DES Y3 calibrates shear and redshift
biases jointly with image simulations (arXiv:2012.08567); KiDS-Legacy does the
equivalent with SKiLLS (arXiv:2210.07163); DES Y6 uses metadetection plus
full-survey synthetic source injection with Balrog, which shows percent-level
accuracy of the measured object properties (Anbajagane et al. 2025,
arXiv:2501.05683) [src]. Earlier quantifications: ambiguous blends (Dawson et
al. 2016, arXiv:1406.1506), impact on deep surveys (Nourbakhsh et al. 2022,
arXiv:2112.07659).

## 3. PSF modelling and leakage
<!-- key: psf-modelling-and-leakage -->

**Mechanism.** The PSF both circularises (multiplicative) and imprints its
ellipticity (additive) on galaxy shapes; errors in PSF size and ellipticity
models propagate into m and c (Paulin-Henriksson et al. 2008,
arXiv:0711.4886).

**Mitigation.** Empirical PSF models interpolated from stars, with diagnostics
from the correlation functions of PSF residuals (the ρ statistics; Rowe 2010,
arXiv:0904.3056). DES Y3 and Y6 use PIFF (Jarvis et al. 2021,
arXiv:2011.03409; Schutt et al. 2025, arXiv:2501.05781).

**Size.** HSC Y1: fractional PSF size residuals of about 0.003 (requirement
0.004) and ρ1 < 3×10⁻⁷ at 0.5° (requirement 4×10⁻⁷), "narrowly" meeting
requirements (Mandelbaum et al. 2018, arXiv:1705.06745) [src: abstract]. KiDS-1000
verifies that its PSF model induces less than a 0.1σ change in S8 (Giblin et
al. 2021, arXiv:2007.01845) [src: abstract]. DES Y6 improved PIFF with Gaia and infrared
photometry to purify the star sample (arXiv:2501.05781) [src]. For Rubin,
simulations put the additive PSF-error contribution well below 30% of the
cosmic-shear uncertainty (Hébert et al. 2026, arXiv:2608.21688) [src: abstract].

**Leakage coefficients and null tests in the main analyses.**

| Analysis | PSF contamination model and coefficients | Propagated effect | B-mode test |
|---|---|---|---|
| DES Y3 (arXiv:2105.13543) | δε = α ε_model + β (ε_* − ε_model) + η ε_* (T_* − T_model)/T_* [src: Eq. 34]; α = 0.010 ± 0.005, −0.001 ± 0.005, −0.004 ± 0.005, 0.014 ± 0.006; β = 0.6 to 2.5; η = −4.6 to 4.2 with errors near 2.7, fitted to the ρ statistics per bin [src: Table 4] | at most 30% of the signal, on the small scales of a few bin pairs; the 2σ limits leave Ωm and σ8 unchanged [src: App. A.1] | non-tomographic: p = 0.06 (pseudo-Cℓ) and 0.87 (COSEBIs); tomographic pseudo-Cℓ with NaMaster, 8 ≤ ℓ ≤ 2048, covariance from 10,000 Gaussian simulations [src: App. A.2] |
| HSC Y3 (arXiv:2304.00702, arXiv:2304.00701) | γ_sys = α⁽²⁾ e_psf + β⁽²⁾ Δe_psf + α⁽⁴⁾ M_psf⁽⁴⁾ + β⁽⁴⁾ ΔM_psf⁽⁴⁾, second- and fourth-moment leakage and model error, sampled in the fit with unit Gaussian priors on decorrelated combinations [src: Eq. 24, Table 2 of arXiv:2304.00702] | without the PSF model S8 rises by about 0.15σ and Ωm by 0.3σ [src: Sect. V.4.1] | ξ+ B modes are significant at large scales in the high-redshift bins, which sets the upper cut at 56.6′; after cuts p ≈ 0.1–0.2 (the text gives 0.143 and 0.237, the caption of Fig. 5 0.1143 and 0.1237) [src: Sect. III.3]. In harmonic space B modes exceed zero below ℓ = 300, about the field of view, which sets ℓ_min; within 300 < ℓ < 1800, p = 0.50 for BB and 0.95 for EB; about 20 deg² with very good seeing and large fourth-moment PSF residuals were removed after a significant detection [src: Sect. IV.3 of arXiv:2304.00701] |
| KiDS-Legacy (arXiv:2503.19441) | ε_obs = (1 + m)(ε_int + γ) + α ε_PSF + c [src: Eq. 24]; after shape recalibration the largest residual is α₂ ≈ 0.01, three orders of magnitude below the value before; focal-plane pattern \|c/σ_ε\| ≤ 1% [src: Sect. 3.5] | total Paulin-Henriksson term δξ+^sys below 10% of the ξ+ uncertainty in every bin [src: Sect. 4.1]; ξ^sys = ⟨ε_obs ε_PSF⟩²/⟨ε_PSF ε_PSF⟩ below the same level for all but 5 of 189 points [src: Sect. 4.2, Eq. 27]. No ρ statistics are evaluated, because no requirement relative to the noise exists for them [src: Sect. 4.1, footnote 7] | COSEBI B_n: p = 0.04 (six modes) and 0.09 (twenty), threshold 0.01; the first blinded sample failed and 46.6 deg² with large astrometric scatter between exposures were removed [src: Sect. 4.3, App. E]; with scales down to 0.5′ the test fails again [src: Sect. 5.2.7] |
| DES Y6 (arXiv:2602.10065) | eight parameters, second and fourth moments [src: Eq. 23]; α = 0.028 ± 0.013, 0.003 ± 0.014, 0.000 ± 0.015, 0.016 ± 0.017; the fourth-moment model-error coefficient β⁽⁴⁾ = 2.6 to 3.1 (errors 0.5 to 0.7) is the only one detected in every bin [src: Table 5] | best-fit contamination, and contamination with all parameters raised by 3σ, both shift S8 by less than the 0.3σ requirement [src: App. A.1] | band-power estimator built from ξ± (Becker & Rozo 2016, arXiv:1412.3851), 20 band powers, 0.25–250′, covariance from mocks: null within 3σ in every bin pair [src: App. A.2] |

**Validation.** ρ statistics and their propagation into ξ±; star–galaxy
cross-correlation; B modes. UNIONS traced initial B-mode failures to galaxy
size cuts and stellar halo masking, and an oscillatory COSEBI B-mode pattern
to a repeating additive shear bias at the CCD scale, the same detector-level
effect seen in CFHTLenS; after cuts all three E/B statistics pass, minimum PTE
= 0.18 (Daley et al. 2026, arXiv:2604.03227) [src: abstract].

## 4. Redshift distributions
<!-- key: redshift-distributions -->

**Mechanism.** The lensing kernel depends on the source n(z); an error in the
mean redshift of a bin maps almost directly into the shear amplitude and hence
S8.

**Mitigation, three independent routes plus one cross-check.**
1. *Colour-space reweighting with self-organising maps (SOM).* Map the
   many-band colour space, populate it with spectroscopic or many-band
   photometric redshifts, and reweight to the wide sample (Masters et al.
   2015, arXiv:1509.03318; KiDS: Wright et al. 2020, arXiv:1909.09632; DES
   SOMPZ: Buchs et al. 2019, arXiv:1901.05005; Myles et al. 2021,
   arXiv:2012.08566). The earlier form is direct reweighting of a
   spectroscopic sample (Lima et al. 2008, arXiv:0801.3822).
2. *Clustering redshifts.* Cross-correlate the photometric sample with
   spectroscopic tracers in thin redshift slices (Newman 2008,
   arXiv:0805.1409; Ménard et al. 2013, arXiv:1303.4722; DES Y3: Gatti et al.
   2022, arXiv:2012.08569; KiDS: van den Busch et al. 2020, arXiv:2007.01846).
3. *Shear ratios.* The ratio of tangential shear around the same lenses for
   two source bins is geometric (Jain & Taylor 2003, arXiv:astro-ph/0306046;
   DES Y3: Sánchez et al. 2022, arXiv:2105.13542).
4. *Self-calibration in the cosmological fit.* HSC Y3 applies "a conservative,
   wide, flat prior on the photometric redshift errors on the last two
   tomographic bins" and lets the relative shear amplitudes across bins
   calibrate them (Li et al. 2023, arXiv:2304.00702) [src]; the HSC Y3 3×2pt
   analysis then finds hints that the true mean redshift at z ≳ 0.75 is higher
   than the photo-z estimate (Miyatake et al. 2023, arXiv:2304.00704) [src: abstract].

**Size, earlier analyses.** KiDS-1000: SOM-reweighted spectroscopic
calibration in five bins over 0.1 < z_B ≤ 1.2, residual mean-redshift biases ≲
0.01 with uncertainties ~0.01, and ~0.01–0.02 for the clustering-redshift
recalibration (Hildebrandt et al. 2021, arXiv:2007.15635) [src: abstract]; on mocks the
SOM method has a maximal bias Δ⟨z⟩ = 0.013 ± 0.006 (arXiv:1909.09632) [src: abstract].
DES Y3: combined σ⟨z⟩ ~ 0.01 per bin (arXiv:2012.08566) [src: abstract]; clustering
redshifts recover the bin means to an RMS of ~0.014 in simulations
(arXiv:2012.08569) [src: abstract]; shear ratios tighten the source-redshift priors by
up to 38% in some bins and the cosmic-shear S8 constraint by up to 31% (10%
for 3×2pt) (arXiv:2105.13542) [src: abstract].

**Size, final analyses.** DES Y6: σ⟨z⟩ = 0.012, 0.008, 0.009, 0.024 for bins
centred at 0.414, 0.538, 0.846, 1.157; the dominant term is the lack of faint
representative spectra; SOMPZ and clustering redshifts agree, and give
cosmological constraints within 0.1σ of each other (Yin et al. 2025,
arXiv:2510.23566) [src]. Adding clustering redshifts (BOSS and eBOSS
references, 1.5–5 Mpc scales) improves the DES Y6 S8 constraint by about 10%
(d'Assignies et al. 2025, arXiv:2510.23565) [src]. KiDS-Legacy: SOM and
cross-correlation estimates agree on simulations and to better than 2σ in
every bin on data (Wright et al. 2025, arXiv:2503.19440) [src]. HSC Y3:
replacing the original calibration by DESI clustering redshifts moves S8 from
0.769 to 0.804 and shrinks the error by a factor 1.8 (arXiv:2511.18134) [src].
DESI-based unified calibration reaches σ_z̄ ~ 0.01 or better for DES, HSC and
KiDS (Lange et al. 2025, arXiv:2510.25419) [src]; applied to KiDS-1000 it
finds mean shifts averaging −0.028 and shows that spectroscopic incompleteness
within SOM cells can alter n(z) (Blanco et al. 2025, arXiv:2512.15964) [src: abstract].

**Redshift nuisance parameters of the main analyses.**

| Analysis | Bins (mean z) | Parametrisation and prior | What the fit and the cross-checks say |
|---|---|---|---|
| KiDS-1000 (arXiv:2007.15633) | five, 0.1 < z_B ≤ 1.2 | one shift per bin with correlated Gaussian priors; Δz = z_est − z_true = 0.000 ± 0.0106, 0.002 ± 0.0113, 0.013 ± 0.0118, 0.011 ± 0.0087, −0.006 ± 0.0097 from MICE2 mocks [src: Table 1, Table 2] | fixing the shifts, widening the priors or adopting the clustering-redshift shifts has "a negligible impact" on Σ8 [src: Sect. 4.2.2] |
| DES Y3 (arXiv:2105.13543) | four: 0.336, 0.521, 0.742, 0.964 [src: Table 1] | n_i(z) → n_i(z − Δz_i) [src: Eq. 23], zero-mean Gaussian priors of width 0.018, 0.015, 0.011, 0.017 [src: Table 2] | fixing shear and redshift priors gives "no significant improvement" in S8: not limited by observational systematics [src: Sect. XII] |
| HSC Y3 (arXiv:2304.00702) | four over 0.3–1.5 | n_i(z) → n_i(z + Δz_i), the opposite sign [src: Eq. 22]; N(0, 0.024), N(0, 0.022) for bins 1–2, flat on [−1, 1] for bins 3–4 because the CAMIRA-LRG cross-correlation stops at z = 1.2 [src: Sect. IV.3, Table 2] | posterior Δz₃ = −0.115, Δz₄ = −0.192 (true redshifts higher), unlikely in 50 noisy mocks; the Gaussian priors N(0, 0.031) and N(0, 0.034) instead move S8 by about 2σ; the flat priors are "a large part of the reason" Y3 does not improve on Y1 [src: Sect. V.4.2]. Harmonic space: Δz₃ = −0.076 +0.056/−0.059, Δz₄ = −0.157 +0.094/−0.111 [src: Sect. VI.2.5 of arXiv:2304.00701] |
| HSC Y3 recalibrated (arXiv:2511.18134) | same bins | DESI-calibrated n(z) with N(0, 0.008), N(0, 0.009), N(0, 0.020), N(0, 0.012) [src: Table 1 of the ar5iv rendering, an earlier version than the current abstract] | the new Δz₃,₄ lie "1–2 sigma away" from the HSC Y3 self-calibrated posterior [src: Sect. 4] |
| KiDS-Legacy (arXiv:2503.19441) | six: 0.335, 0.477, 0.587, 0.789, 0.940, 1.224 [src: Table 1] | SKiLLS biases applied to the N(z): δz = −0.026, +0.014, −0.002, +0.008, −0.011, −0.054, each with two uncertainties, 0.001–0.004 and 0.010 [src: Table 1]; correlated Gaussian prior [src: Table 3, Fig. 3]. The calibration paper lists the uncertainties as 0.010–0.011 "after applying the error floor" (arXiv:2503.19440) [src: Table 8] | clustering shifts fitted on the data: 0.000 ± 0.007, 0.028 ± 0.006, 0.021 ± 0.006, 0.035 ± 0.010, −0.018 ± 0.028, −0.145 ± 0.091; they agree with the median SOM bias in every bin but the fourth, about 2σ (arXiv:2503.19440) [src: Table 8, Sect. 7.2.2]. With the clustering N(z) Σ8 moves by 0.01σ and its error grows by 23% (COSEBIs) or 29% (band powers); calibrating on MICE2 instead of SKiLLS raises Σ8 by up to 1.25σ through a coherent shift of at most 0.016 in bins 3–6, a variant the paper holds inferior since MICE2 stops near z = 1.4 [src: Sect. 5.2.6]; removing one bin moves Σ8 by at most 0.24σ, against up to 1.8σ in KiDS-1000 [src: Sect. 5.2.8] |
| DES Y6 (arXiv:2602.10065) | four: 0.414, 0.538, 0.846, 1.157 | no mean shifts: seven mode amplitudes with unit Gaussian priors carry the n(z) shape and the correlations between bins [src: Table 2, Sect. IV.4] | fixing them tightens S8 by a factor 1.2 (σ = 0.015 → 0.012 NLA, 0.017 → 0.014 TATT) [src: Sect. VI.3]; one Δz per bin instead: "no noticeable impact"; without clustering redshifts: consistent; shear ratios (two highest source bins, lowest lens bin, below 6 Mpc/h): within about 0.3σ, S8 tighter by 1% (NLA) or 10% (TATT); a 3σ-wide flat prior on the modes: about 0.4σ in the (S8, Ωm) plane [src: Sect. VII.2.1] |

In the DES Y6 3×2pt analysis the redshift calibration of sources and lenses
is the largest parametrised systematic, where in Y3 it was negligible
(arXiv:2601.14559) [src: App. D]; one n(z) mode of lens bin 2 pushed against
its prior, several posterior-predictive tests failed at the last blinding
stage, and all data of that lens bin were dropped, the cause not being found
[src: Sect. IV.8].

Schmidt et al. 2013 (arXiv:1303.0292) show on simulations that clustering
redshifts can use non-linear scales for narrow bins, the difficulty being to
separate n(z) from an evolving galaxy bias [src].

**Referee expects:** two independent methods with a quantitative comparison;
the treatment of spectroscopic incompleteness; how n(z) uncertainty is
propagated (mean shifts, or an ensemble of n(z) realisations as in DES Y3/Y6).
Review: Newman & Gruen 2022, arXiv:2206.13633.

## 5. Intrinsic alignments
<!-- key: intrinsic-alignments -->

**Mechanism.** Galaxy shapes align with the tidal field, adding
intrinsic–intrinsic (II) and gravitational–intrinsic (GI) terms to the shear
correlation (Hirata & Seljak 2004, arXiv:astro-ph/0406275). The II term was
predicted first: analytically, from alignment of halo shape or spin with the
tidal field, which gives long-range ellipticity correlations (Catelan et al.
2001, arXiv:astro-ph/0005470) [src], and in N-body haloes, at about 10⁻⁴ on
0.1–10′ for a survey of median redshift 1, below the lensing signal there
but possibly dominant in shallow wide surveys (Heavens et al. 2000,
arXiv:astro-ph/0005269) [src: abstract]. A lensing-only field is curl-free whereas spin
alignments are not, which is the origin of the B-mode null test (Crittenden
et al. 2002, arXiv:astro-ph/0012336) [src].

**Models.** NLA: linear alignment with the non-linear matter power spectrum,
one amplitude plus an optional redshift power law (Bridle & King 2007,
arXiv:0705.0166). TATT: tidal alignment plus tidal torquing plus density
weighting from perturbation theory (Blazek et al. 2019, arXiv:1708.09247).
Halo models with a satellite term (Schneider & Bridle 2010, arXiv:0903.3870,
where centrals follow the large-scale potential and satellites point at the
halo centre [src]; Fortuna et al. 2021, arXiv:2003.02700). The luminosity and
redshift scalings used as priors come from luminous red galaxies: amplitude ∝
L^b with b = 1.1 +0.3/−0.2 and an extra (1+z)^n with n = −0.3 ± 0.8 (Joachimi
et al. 2011, arXiv:1008.3491) [src: abstract].
Reviews: Joachimi et al. 2015, arXiv:1504.05456; Troxel & Ishak 2015,
arXiv:1407.6990; Lamman et al. 2024, arXiv:2309.08605; Chisari 2025,
arXiv:2510.15738.

**Why the model matters.** With alignments included, two or more times as many
tomographic bins are needed to recover 80 per cent of the information
(arXiv:0705.0166) [src: abstract]. The quadratic and cross terms of TATT can be
order-unity corrections to the alignment signal at k ~ 0.1 h/Mpc, and in an
LSST-like **forecast** NLA cannot absorb them even with a free redshift
dependence (arXiv:1708.09247) [src: abstract]. The halo-model study finds that the model
refinements it tests give negligible biases for Stage-III surveys, but that
for Stage IV at least one additional parameter for the redshift dependence is
essential (arXiv:2003.02700) [src, **forecast**].

**Size.** The NLA/TATT choice moves the DES Y6 cosmic-shear S8 from 0.798 to
0.783 and the precision from 1.8% to 2.5% (arXiv:2602.10065) [src: abstract]. In UNIONS
the S8–A_IA degeneracy, with A_IA drawn from a direct-measurement prior, is
one of the largest uncertainties (arXiv:2605.13543) [src: abstract].

**Model, prior and posterior in the main analyses.** Model equations are in
`physics-and-methods.md` section 5.

| Analysis | Model and prior | Posterior | S8 under an alternative model |
|---|---|---|---|
| KiDS-1000 (arXiv:2007.15633) | NLA, one amplitude, flat on [−6, 6] [src: Table 2] | A_IA and S8 are the only constrained physical parameters; band powers prefer an amplitude higher by 0.53 than COSEBIs and ξ±, a difference met in about 5% of noise realisations [src: App. A] | a free redshift index η_IA ∈ [−5, 5] leaves the upper edge of Σ8 in place and widens the interval [src: Sect. 4.2.4] |
| DES Y3 (arXiv:2105.13543, arXiv:2105.13544) | TATT, five parameters: a₁, a₂, η₁, η₂ flat on [−5, 5], b_TA on [0, 2] [src: Table 2 of arXiv:2105.13543] | a₁ = −0.47 +0.30/−0.52, a₂ = 1.02 +1.61/−0.55, with a₁ = a₂ = 0 inside the 1σ contour and a hint of a sign-flipped second mode; NLA: a₁ = −0.09 +0.20/−0.13; GI + II is "a few percent" of the signal [src: Sect. VI.3.1 of arXiv:2105.13544] | the model without alignments has the highest evidence, "weakly preferred" on the Jeffreys scale [src: Sect. VI.3.2 of arXiv:2105.13544] |
| DES Y3 + KiDS-1000 (arXiv:2305.17173) | NLA with a redshift power law, pivot 0.62, separate parameters per survey [src: Sect. 2.2] | separately A_IA = 0.32 +0.43/−0.37 (DES) and 0.65 +0.88/−0.54 (KiDS); jointly −0.02 +0.58/−0.29 and 1.04 +0.54/−0.52, 1.47σ apart: the parameter "may ... be absorbing more than" alignments [src: Sect. 3.3] | shared parameters: S8 up by 0.1σ [src: Sect. 3.3] |
| HSC Y3 (arXiv:2304.00702) | TATT, A₁, A₂, η₁, η₂ flat on [−6, 6], b_TA on [0, 2], pivot 0.62 [src: Sect. IV.2, Table 2] | A₁ detected at 1.1σ (TATT) and 2.1σ (NLA): "we do not find a significant detection" [src: Sect. V.3.2]; with the DESI n(z), A₁ = 0.44 +0.36/−0.33 (arXiv:2511.18134) [src: Table 1 of the ar5iv rendering] | NLA or no alignment: no significant change in S8, under 0.5σ in Ωm and σ8 [src: Sect. V.3.2] |
| KiDS-Legacy (arXiv:2503.19441) | "NLA-M": only the red fraction of each bin aligns, with a power law of mean halo mass; Gaussian prior from direct early-type measurements, A_IA = 5.74 ± 0.29, β = 0.44 ± 0.03, correlation −0.59 [src: Sect. 2.4.4] | alignments are "around 10 percent" of the signal [src: Sect. 2.4]; the amplitudes of the NLA and NLA-k variants are consistent with zero [src: Sect. 5.2.4] | NLA, NLA-z, NLA-k: Σ8 moves by at most 0.17σ (band powers) and 0.54σ (COSEBIs); NLA-M is about 5% tighter than NLA and 12–13% tighter than NLA-z thanks to its prior [src: Sect. 5.2.4] |
| DES Y6 (arXiv:2602.10065) | NLA and TATT both fiducial; A₁ ∈ [−1, 3], A₂ ∈ [−3, 3] flat, η₁, η₂ Gaussian around 0, b_TA fixed to 1, pivot 0.3 [src: Table 2] | A₁ ~ 0.5 at low redshift, consistent with zero at high redshift, a small amplitude that the paper relates to a faint sample with a high blue fraction [src: Sect. VIII.1] | the two fiducial posteriors differ by 0.6σ; Z_NLA/Z_TATT = 16.9 ± 0.2, "strong", a ratio that changes by a factor 2 if the A₂ and η₂ priors are scaled by √2 [src: Sect. VII.3.1]. Fifteen variants span S8 = 0.773 +0.023/−0.018 (TATT, linear redshift evolution) to 0.802 ± 0.014 (tidal alignment with b_TA = 1); no alignment at all gives 0.792 ± 0.013 [src: Table 4]. Fixing the parameters would tighten S8 by 1.1 (NLA) or 1.3 (TATT) [src: Sect. VI.3] |
| DES Y3 blue sample (arXiv:2512.04209) | star-forming galaxies only; per bin a Gaussian prior centred on zero with the width of direct measurements [src: Sect. III.2] | — | with the DES scale cuts, S8 = 0.803 +0.016/−0.022 against 0.777 +0.035/−0.024 for TATT on the same sample: a factor 1.7 in precision [src: Table 1, Sect. IV] |

KiDS-1000 states that its known modelling systematics bias S8 by no more than
0.1σ, "with the caveat that no conclusive validation data exist for models of
intrinsic galaxy alignments" (Joachimi et al. 2021, arXiv:2007.01844) [src: abstract].
Type dependence was seen from the start: CFHTLenS found a significant
alignment signal for early-type galaxies and none for late types (Heymans et
al. 2013, arXiv:1303.1808) [src].

**Direct measurements.** DES Y3 redMaGiC, eBOSS LRG and BOSS CMASS: alignments
detected at 5σ–22σ on 6 < r_p < 70 h⁻¹Mpc; eBOSS emission-line galaxies give a
null result, A1 = 0.07 +0.32/−0.42 in NLA (Samuroff et al. 2023,
arXiv:2212.11319) [src: abstract]; DESI DR1 with DES, HSC, KiDS and SDSS shapes, over 2
million galaxies: the bluest galaxies are consistent with zero alignment, red
galaxies align more strongly with luminosity, and luminosity and colour
explain the signal at 0 < z < 1.5 without an explicit redshift dependence
(Siegel et al. 2025, arXiv:2507.11530) [src: abstract].

**Mitigation in practice.** Marginalise a model; inform it with direct
measurements (KiDS-Legacy, arXiv:2503.19441); or select a low-alignment blue
sample (arXiv:2512.04209).

## 6. Baryonic feedback
<!-- key: baryonic-feedback -->

**Mechanism.** AGN and stellar feedback move gas out of haloes and suppress
the matter power spectrum. The OWLS AGN simulation predicted a decrease
relative to dark-matter-only, at z = 0, of 1% at k ≈ 0.3 h/Mpc, 10% at k ≈ 1
h/Mpc and 30% at k ≈ 10 h/Mpc, so that baryons "cannot be ignored" for k > 0.3
h/Mpc (van Daalen et al. 2011, arXiv:1104.1174) [src: abstract]; simulation library: van
Daalen et al. 2020, arXiv:1906.00968. In shear, the baryonic correction model
predicts a 15–25% suppression of the shear power spectrum beyond ℓ ~ 100–600
and 10–25% effects on ξ+ below 5 arcmin and on ξ− below 50 arcmin (Schneider
et al. 2019, arXiv:1810.08629) [src: abstract]. Most of the effect on the scales of
cosmic shear comes from group-mass haloes, M ~ 10¹³–10¹⁴ M⊙ (Salcido et al.
2023, arXiv:2305.09710) [src: abstract].

**Mitigation.** (a) Scale cuts validated on synthetic data: DES Y3 reports no
bias above 0.3σ in the S8–Ωm plane from theory-model uncertainty (Secco et al.
2022, arXiv:2105.13544; strategy in Krause et al. 2021, arXiv:2105.13548; Y6
in arXiv:2601.14859) [src: abstract of arXiv:2105.13544]. (b) Halo-model parametrisation: HMcode (Mead et
al. 2015, arXiv:1505.07833); HMcode-2020 has a six-parameter feedback model
and a single-parameter variant, matches the hydrodynamical power-spectrum
response to better than 1% for z < 1 and k < 20 h/Mpc, and ships with CAMB
(Mead et al. 2021, arXiv:2009.01858) [src: abstract]. (c) Baryonification of N-body
simulations and its emulators (Schneider & Teyssier 2015, arXiv:1510.06034;
Schneider et al. 2019, arXiv:1810.08629; Giri & Schneider 2021,
arXiv:2108.08863; Aricò et al. 2021, arXiv:2011.15018). (d) Principal
components of simulation suites (Huang et al. 2019, arXiv:1809.01146). (e)
Simulation-based fitting functions tied to halo baryon fractions (Salcido et
al. 2023, arXiv:2305.09710). (f) Nulling of small physical scales with the BNT
transform (arXiv:2607.04384). (g) External priors from X-ray gas fractions,
tSZ and kSZ (arXiv:2512.04209, arXiv:2506.07432, arXiv:2609.09144; kSZ
evidence: Bigwood et al. 2024, arXiv:2404.06098; Hadzhiyska et al. 2024,
arXiv:2407.07152; Ried Guachalla et al. 2025, arXiv:2503.19870).

**Earlier lensing-only constraints.** DES Y3 small scales with
baryonification: best-fit suppression ~5% at k = 1 h/Mpc and ~15% at k = 5
h/Mpc, M_c > 10^13.2 h⁻¹M⊙ at 95% (Chen et al. 2023, arXiv:2206.08591) [src: abstract];
DES Y3 with the BACCO emulator: log M_c = 14.38 +0.60/−0.56 and S8 = 0.799
+0.023/−0.015, 0.9σ from Planck and 1.4σ above the official DES Y3 value
because of modelling choices (Aricò et al. 2023, arXiv:2303.05537) [src: abstract].
X-ray gas fractions through the baryonic emulator imply a suppression
exceeding 1% at k = 0.1–0.4 h/Mpc and peaking at 20–28% near k = 7 h/Mpc
(arXiv:2108.08863) [src: abstract].

**External gas probes.** DES Y3 lensing + ACT DR5 kSZ constrain a mean
feedback scenario "more extreme than the predictions from most hydrodynamical
simulations" (arXiv:2404.06098) [src]. Stacked kSZ on DESI imaging galaxies is
detected at 13σ and disfavours low-feedback models of the IllustrisTNG kind
(arXiv:2407.07152) [src: abstract]. kSZ around DESI Y1 LRGs gives a tentative preference
for stronger feedback (Illustris z = 0.5, PTE = 0.37, against IllustrisTNG z =
0.8, PTE = 0.045) (arXiv:2503.19870) [src: abstract]. Detail belongs to
`cosmo-cmb-lss-cross-correlations`.

**Size.** See `results.md` section 1.5. Current scale cuts leave about 0.3σ
residual bias in (S8, Ωm) for a 13,000 deg² Stage-III data set
(arXiv:2509.03582) [src].

**Treatment and size in the main analyses.**

| Analysis | Feedback model and prior | Scale-cut rule | Size found |
|---|---|---|---|
| KiDS-1000 (arXiv:2007.15633) | HMCode amplitude A_bary flat on [2, 3.13], 3.13 being no feedback [src: Table 2, Sect. 4.2.4] | none beyond the data range, 0.5′–300′ (as recalled in arXiv:2503.19441) [sec: Sect. 5.2.7] | fixing A_bary = 3.13 matters most for ξ±, which reach the smallest scales [src: Sect. 4.2.4] |
| DES Y3 (arXiv:2105.13543, arXiv:2105.13544) | none: gravity-only Halofit | data vectors contaminated with the OWLS-AGN (and EAGLE) ratio P_hydro/P_DMO; cuts such that the 3×2pt bias is below 0.3σ in the Ωm–S8 plane and Δχ² < 0.5 for cosmic shear, which keeps 166 + 61 = 227 of 400 points [src: Sect. VII.3, Eq. 20 of arXiv:2105.13543] | a halo model with two free feedback parameters shifts S8 by 0.5σ, read as a projection effect since both stay unconstrained and χ² goes from 237.7 to 236.8 [src: Sect. VII.1 of arXiv:2105.13544]; the "optimised" cuts cut the S8 error by about 1.5, and fixed alignments plus all scales by 1.8 [src: Sect. XII of arXiv:2105.13543] |
| DES Y3 + KiDS-1000 (arXiv:2305.17173) | HMCode2020, free T_AGN | the DES "ΛCDM-optimised" cuts and equivalent ones for KiDS, predicted bias below 0.14σ in two dimensions [src: Sect. 2.3] | dark-matter-only with the same cuts lowers S8 by 0.4σ, to 0.784 +0.016/−0.015; the amplitude is unconstrained [src: Sect. 3.4]. HMCode 2016 → 2020 moves KiDS-1000 by 0.19σ [src: Sect. 2.3, footnote 13] |
| HSC Y3 (arXiv:2304.00702) | HMCode 2016, A_b flat on [2, 3.13] with η_b = 0.98 − 0.12 A_b [src: Sect. IV.1.2, Eq. 17] | fixed cuts for all bin pairs, 7.1′ for ξ+ and 31.2′ for ξ− [src: Sect. III.1] | CAMB, HMCode2020 with Θ_AGN ∈ [7.3, 8.3] or dark matter only: all under 0.5σ [src: Sect. V.3.1]; with the DESI n(z), A_b = 2.075 +0.243/−0.128, against the edge of the prior farthest from the dark-matter-only value (arXiv:2511.18134) [src: Table 1 of the ar5iv rendering] |
| KiDS-Legacy (arXiv:2503.19441) | HMCode2020, log₁₀(T_AGN/K) flat on [7.3, 8.3] [src: Table 3] | COSEBIs over 2′–300′ [src: Sect. 5.1] | prior-dominated; ≤ 7.71 (8.01) at 68% (95%) with the cosmology fixed to Planck: "little evidence ... for significant amplitudes of baryon feedback" [src: Sect. 6]; scales down to 0.5′ lower S8 by 0.1σ, against 0.8σ in KiDS-1000 and 0.3σ after its shape recalibration [src: Sect. 5.2.7] |
| DES Y6 (arXiv:2602.10065) | HMCode2020 fixed at Θ_AGN = 7.7 | bias in the marginal S8 below 0.5σ between a gravity-only spectrum and the BAHAMAS "hi AGN" run, both on EuclidEmulator2: 178 + 89 points with NLA, 183 + 99 with TATT, of 400 [src: Sect. IV.3] | an Illustris-like suppression would bias S8 low by 0.7σ, the stated worst case [src: Sect. IV.3]; free Θ_AGN ∈ [7.2, 9.0]: S8 = 0.807 +0.017/−0.019; free A_mod ∈ [0.5, 1.5] in P_m = P_L + A_mod (P_NL − P_L): 0.806 +0.021/−0.025 [src: Sect. VII.3.2, Eq. 20]; EuclidEmulator2 or BACCO in place of HMCode2020: 0.03σ and 0.08σ [src: Sect. IV.3]; a perfect model down to 2.5′ would shrink σ(S8) from 0.015 to 0.009 (NLA) or 0.017 to 0.012 (TATT), and 0.006 with all nuisance parameters fixed [src: Sect. VI.3] |
| DES Y3 blue sample (arXiv:2512.04209) | BCEmu baryonification with correlated priors from eROSITA gas fractions and ACT kSZ profiles, masses from galaxy–galaxy lensing, 10% systematic allowances on each [src: Sect. III.1] | none, 400 points | suppression known to 4.3% at k = 1 h/Mpc; stronger than FLAMINGO by 2.2σ, BAHAMAS 1.5σ, MTNG740 3.1σ, FABLE 2.9σ, SIMBA 0.8σ at k = 2 h/Mpc; the calibrated priors add a factor 1.2 in S8 precision, 0.820 +0.016/−0.025 → 0.832 +0.013/−0.017 [src: Sect. IV, Table 1] |

First statements of the problem: baryonic cooling changes the power spectrum
near k ~ 10 h/Mpc and the convergence spectrum at the per cent level at
multipoles of several thousand (White 2004, arXiv:astro-ph/0405593) [src];
with the OWLS AGN run a dark-matter-only model biases w0 by about 40%, and a
halo model with simple modifications brings the bias down to the statistical
error of a Euclid-like mission (Semboloni et al. 2011, arXiv:1105.1075)
[src]. HMCode2020 is calibrated on BAHAMAS (arXiv:2503.19441) [src: Sect.
2.3], simulations whose stellar and AGN feedback were calibrated to the
galaxy stellar mass function and to the hot-gas fractions of groups and
clusters (McCarthy et al. 2017, arXiv:1603.02702) [src].

**The "non-linear solution".** Amon & Efstathiou 2022 (arXiv:2206.11794)
fitted a one-parameter suppression of the non-linear spectrum to KiDS-1000 and
argued that lensing and Planck ΛCDM are reconciled if the suppression is
stronger than assumed [src]. Preston et al. 2023 (arXiv:2305.09827) found that
the suppression DES Y3 requires is weaker than for KiDS but still more extreme
than recent simulations, and must reach k ~ 0.2 h/Mpc [src: abstract]. The FLAMINGO
simulations (Schaye et al. 2023, arXiv:2306.04024) answered that across their
feedback variations "baryonic effects are not sufficiently large to remove the
S8 tension" (McCarthy et al. 2023, arXiv:2309.07959) [src]. With the 2025–2026
S8 values the amount of suppression that would be "required" is smaller than
these papers assumed; none of the three has been redone on KiDS-Legacy or DES
Y6 as far as the searches of this session show.

## 7. Other effects a complete analysis treats
<!-- key: other-effects-a-complete-analysis-treats -->

| Effect | Standard treatment | Reference |
|---|---|---|
| Magnification of the lens sample | magnification coefficients per lens bin from Balrog source injection, with Gaussian priors. DES Y6 MagLim++ coefficients, bins 1 to 6, are 3.16 ± 0.08, 2.76 ± 0.21, 4.09 ± 0.15, 4.42 ± 0.16, 4.90 ± 0.29, 4.83 ± 0.25; neglecting magnification shifts the 2×2pt S8 by 1.37σ and Ωm by −0.84σ (−0.61σ and −0.71σ with cosmic shear included) [src: abstract of arXiv:2601.14833]. The 3×2pt prior table lists the six coefficients as α = 1.58 ± 0.04, 1.38 ± 0.11, 2.04 ± 0.08, 2.21 ± 0.08, 2.45 ± 0.14, 2.42 ± 0.13 (arXiv:2601.14559) [src: Table 3]. Magnification accounts for under 1% of the 3×2pt S8 width [src: App. D of arXiv:2601.14559] | Elvin-Poole et al. 2023, arXiv:2209.09782; DES Y6: Legnani et al. 2026, arXiv:2601.14833 |
| Non-linear galaxy bias and point-mass term in γ_t | scale cuts, or analytic marginalisation of an enclosed-mass term | Prat et al. 2022, arXiv:2105.13541 |
| Source clustering, reduced shear | modelled explicitly once third-order statistics are used | arXiv:2606.12389 |
| Limber approximation | extended Limber or exact projection at low ℓ | LoVerde & Afshordi 2008, arXiv:0809.5112; Kilbinger et al. 2017, arXiv:1702.05301 |
| Covariance errors | analytic halo-model covariance with super-sample term, validated on mocks. DES Y3: the f_sky approximation for finite area is the largest effect, raising χ² by 3.7% (Δχ² ≈ 18.9) and the scatter of best-fit Ωm, σ8 by about 3% [src: arXiv:2012.08568]. KiDS-Legacy: OneCovariance is accurate at the per cent level; ignoring the survey geometry misestimates cosmic-variance terms by about 10% [src: arXiv:2410.06962]; against GLASS mocks the analytic covariance agrees within 10% at large separations and 5% below 0.5°, and keeping only the Gaussian term shrinks the Σ8 error by 12% (band powers) to 19% (COSEBIs) with no shift; iterating the covariance at the best fit converges in two steps [src: Sect. 2.6, 5.2.2, 5.2.3 of arXiv:2503.19441]. DES Y6: the signal uses HMCode2020 but the covariance Halofit, at most 2.5% on individual elements [src: Sect. IV.2 of arXiv:2601.14559]. HSC Y3: 1404 ray-traced mocks at one (WMAP9) cosmology, mock signal rescaled by its ratio 0.81 to theory, Hartlap factor about 0.9 for 140 points [src: Sect. III.2, IV.6 of arXiv:2304.00702]. Sampler: MultiNest underestimates the 68% and 95% widths of S8 by 12% and 15% (arXiv:2305.17173) [src: App. D] | arXiv:2012.08568, arXiv:2410.06962; non-Gaussian term: Cooray & Hu 2001, arXiv:astro-ph/0012087, about 15% on parameter errors for a survey to z ~ 1 [src]; samplers: Lemos et al. 2023, arXiv:2202.08233 |
| Cross-survey galaxy–galaxy lensing amplitude | blind comparison of ΔΣ around the same BOSS lenses from different shear catalogues: systematics above 15% (25%) excluded at 68% (95%) at z < 0.54; a 3–4σ correlation of amplitude with survey depth for z_L > 0.43 [src: abstract of arXiv:2111.13805]. With DESI DR1 lenses a trend with source redshift appears and vanishes once the HSC redshift shifts favoured by its cosmology analysis are applied [src: arXiv:2506.21677] | Leauthaud et al. 2022, arXiv:2111.13805; Heydenreich et al. 2025, arXiv:2506.21677 |
| Spatially varying depth | lens-sample weights and masks; variable-depth n(z) | Rodríguez-Monroy et al. 2025, arXiv:2509.07943 |

The magnification coefficients of arXiv:2601.14833 and the α values of the
3×2pt prior table of arXiv:2601.14559 are not on the same scale; check the
definition in each paper before comparing them [der: from the two lists].

**Which term limits S8.**

| Analysis | Budget as the paper states it |
|---|---|
| KiDS-1000 (arXiv:2007.15633) | observational systematics, separately or jointly, have a small impact [src: Sect. 4.2.3] |
| DES Y3 (arXiv:2105.13543) | fixing shear and redshift priors gains nothing; fixing the alignment parameters and using all scales gains a factor 1.8 [src: Sect. XII] |
| KiDS-Legacy (arXiv:2503.19441) | fixing alignment, redshift and shear nuisance parameters tightens Σ8 by 10% (COSEBIs) or 20% (band powers) and moves it by 0.28σ or 0.14σ: "statistics-limited" [src: Sect. 5.2.5] |
| DES Y6 cosmic shear (arXiv:2602.10065) | gain in σ(S8) with one ingredient made perfect: shear calibration a minimal change (σ = 0.015 to 0.014 for NLA, 0.017 to 0.016 for TATT), redshifts 1.2, alignments 1.1 (NLA) or 1.3 (TATT), scale cuts 1.6 (NLA) or 1.4 (TATT), all together 2.3–2.6 [src: Sect. VI.3] |
| DES Y6 3×2pt (arXiv:2601.14559) | cuts and point-mass marginalisation lower the signal-to-noise from 302 to 95; among parametrised effects redshifts weigh about 14%, alignments 3%, magnification under 1% [src: App. D] |

## 8. What a referee checks in a lensing results section
<!-- key: what-a-referee-checks-in-a-lensing-results -->

1. Which CMB data set the "tension" is measured against, and with which metric
   (S8 difference, full-parameter shift, PPD). References: arXiv:2602.12238
   for the CMB reference that each survey uses, arXiv:2601.14559 for two
   metrics quoted on the same data (2.6σ and 1.8σ) [src: abstract].
2. The IA model, its priors, and how much S8 moves under the alternative.
3. The baryon treatment: scale cuts (and the simulation that set them) or a
   model (and its prior), and the residual bias.
4. Two independent redshift calibrations and their agreement per bin; how the
   uncertainty is propagated.
5. Shear calibration m per bin with its uncertainty, including the
   blending-induced redshift dependence.
6. PSF leakage (ρ statistics or equivalent) and B-mode null tests with PTEs,
   in more than one statistic.
7. Covariance: analytic or mocks, super-sample and non-Gaussian terms,
   survey-geometry treatment, and the goodness of fit.
8. Blinding: at which level (catalogue, data vector, parameters) and what
   changed after unblinding. References: Muir et al. 2020, arXiv:1911.05929
   (data-vector level, DES); Kuijken et al. 2015, arXiv:1507.00738
   (shear-catalogue level, KiDS).
9. Prior-volume and projection effects on marginal S8 (mean vs MAP),
   especially with TATT or wide Δz priors. References: arXiv:2305.17173
   (DES Y3 + KiDS-1000: mean 0.790, MAP 0.801) [src: abstract]; arXiv:2007.01844 (KiDS-1000
   warning on marginal point estimates).
10. Internal consistency splits: redshift bins, scales, colour, sky region,
    statistic.

## Not verified
<!-- key: not-verified -->

- ρ-statistic curves of each survey (only the leakage coefficients fitted to
  them were read; KiDS-Legacy does not compute them), and the per-bin PSF
  coefficients that HSC Y3 samples.
- The scale-dependent additive term that the subtracted mean shear of DES Y3
  and Y6 may leave: both papers say its origin is unknown.
- Body-level sizes for DECADE, UNIONS and the DES Y6 redshift papers
  (arXiv:2509.03582, arXiv:2605.13547, arXiv:2510.23566): abstracts only.
- arXiv:2511.18134 was read in the ar5iv rendering, an earlier version
  (abstract: S8 = 0.805 ± 0.018) than the current one (0.804 +0.019/−0.018);
  the values quoted from its Table 1 may have changed.
