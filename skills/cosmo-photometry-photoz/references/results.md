# Photometry and photometric redshifts — results

Scope: measured calibration precision, photo-z performance and n(z)
characterisation accuracy of surveys and methods, challenge results, and
which numbers are superseded.
Snapshot: 2026-10-16

Flags: `[src]` read this session in the abstract of the cited paper;
`[src: Sect. n]`, `[src: Table n]` read in the body; `[sec]` from a named
secondary source; `[der]` derived here. Forecasts are labelled.

Metrics used below: σ_NMAD = 1.48 × median(|Δz − median(Δz)| / (1+z)),
Δz = z_phot − z_spec; outlier fraction η above a threshold in |Δz|/(1+z) (0.15 in PHAT and the
Euclid challenge, arXiv:1008.0658, arXiv:2009.12112); bias ⟨Δz⟩. Papers
differ in the threshold and in whether σ is NMAD, σ_68 or RMS; compare only
like with like.

## 1. Photometric calibration achieved
<!-- key: photometric-calibration-achieved -->

| Survey or catalogue | Quantity | Value | Reference |
|---|---|---|---|
| SDSS ubercal | relative calibration, griz / u | ~1% / ~2% over 8500 deg² | arXiv:astro-ph/0703454 [src] |
| Pan-STARRS1 (first 1.5 yr) | relative precision | < 10 mmag in g, r, i; ~10 mmag in z, y | arXiv:1201.2208 [src] |
| DES Y3 FGCM | random error per exposure; uniformity | 5–6 mmag; 7 mmag over 5000 deg² | arXiv:1706.01542 [src] |
| DES Y6 FGCM star catalogue | uniformity; absolute scale | < 1.8 mmag RMS over 17 million stars; ~1% via CALSPEC C26202 | arXiv:2305.01695 [src] |
| J-PLUS DR3, S-PLUS DR4 | zero-point errors found by SCR | up to 15 mmag (stellar locus), 23 mmag (S-PLUS); XP and SCR agree to 1–6 mmag after correction | arXiv:2309.11225, arXiv:2309.11533 [src] |
| BEST standards | precision, passbands | better than 10 mmag, > 200 passbands, > 200 million stars | arXiv:2601.05486 [src] |
| DES chromatic errors | before / after transmission-based correction | up to 2% in some bands / < 0.3% | arXiv:1601.00117 [src] |
| StarDICE grey extinction | most affected exposures, mean absolute error | 0.64 → 0.11 mag; temporal variation 0.025 mag per source | arXiv:2511.00182 [src] |
| CFHTLS T007, passband-variation correction | photo-z bias near z = 0.5 | Δz ~ 0.04 → ~0.02 | arXiv:2310.14716 [src] |
| CALSPEC versus ground BVRI | agreement | better than ~1% for eleven standards | arXiv:1502.01754 [src] |

Relative uniformity (mmag) and absolute scale (~1%) are different numbers:
the DES Y6 catalogue is uniform to < 1.8 mmag RMS but its absolute flux
system is known only to about 1% through CALSPEC (arXiv:2305.01695) [src].
Photo-z and n(z) are sensitive mainly to colour errors and their spatial
pattern, supernova distances to the absolute and inter-band scale
(`cosmo-supernovae`).

## 2. Photo-z performance of individual galaxies
<!-- key: photo-z-performance-of-individual-galaxies -->

| Data, method | Sample | σ (definition) | Outliers | Reference |
|---|---|---|---|---|
| HDF, BPZ | 108 spectra, z < 6 | rms Δz/(1+z) = 0.08 | none reported | arXiv:astro-ph/9811189 [src] |
| SDSS DR1, ANNz | 0 < z < 0.7 | rms 0.023 (in z) | — | arXiv:astro-ph/0311058 [src] |
| CFHTLS Deep, LePhare + VVDS | i < 24 | σ_Δz/(1+z) = 0.037 | η = 3.7% | arXiv:astro-ph/0603217 [src] |
| CFHTLS Deep | 17.5 < i < 22.5 / 22.5 < i < 24 | 0.029 / 0.043 | 1.7% / 5.4% | arXiv:astro-ph/0603217 [src] |
| Deep K-selected fields, EAZY | CDF-S and others | 0.034 in Δz/(1+z) | — | arXiv:0807.1533 [src] |
| SDSS main sample, CNN on images | z < 0.4 | σ_MAD < 0.01; < 0.007 at S/N > 100 | — | arXiv:1806.06607 [src] |
| HSC-SSP DR1 grizy | i < 25 / i < 24, 0.2 ≲ z_phot ≲ 1.5 | σ(Δz/(1+z_phot)) ~ 0.05 / ~0.04 | ~15% / ~8% | arXiv:1704.05988 [src] |
| Rubin DP1 (ComCam), eight RAIL codes | 6-band ECDFS, test set like the training set | σ_NMAD of the mode = 0.028 (FlexZBoost) to 0.055 (GPz) | η(|Δz| > 0.15) = 11.7–20.4% | arXiv:2510.07370 [src: Table 2, Sect. 3.4] |
| COSMOS2020 (30+ bands) | i < 21 / 25 < i < 27 | sub-percent / 5% precision | — | arXiv:2110.13923 [src] |
| COSMOS2025 (JWST + 37 bands) | m_F444W < 28, spectra to z ~ 9 | σ_MAD = 0.012 | — | arXiv:2506.03243 [src] |
| PAUS + broad bands, COSMOS | i_AB < 22.5, best 50% | σ_68/(1+z) = 0.0037 | — | arXiv:1809.04375 [src] |
| PAUS wide fields | i_AB < 23 | σ_68 ≃ 0.019 (0.003–0.02 for z_b ~ 0.1–0.75) | bias < 0.01 | arXiv:2312.07581 [src] |
| KiDS-1000, pop-cosmos | DESI BGS / LRG matches | σ_MAD = 0.03 / 0.05 | 3.2% / 1.0% | arXiv:2602.03930 [src] |
| PAUS 40 narrow bands, Flagship 2 simulation | like the spectroscopic validation sample / complete to i ≲ 23 | σ_NMAD/(1+z) = 0.011 / 0.028 | < 10% | arXiv:2606.25812 [src] |

Rubin DP1 is the first photo-z test on LSST Commissioning Camera data; the
bias and scatter of its machine-learning photo-z meet the LSST Y1
requirement, with degradation at faint magnitudes and z > 1.2
(arXiv:2510.07370) [src]. In the body, the Y1 per-galaxy requirements used
are |bias| < 0.005 and σ < 0.1; the machine-learning codes have mean Δz
between −0.0035 and 0.0025, the template codes BPZ and LePhare −0.018 and
−0.014, and the bias as a function of redshift exceeds the Y1 requirement on
the mean [src: Sect. 4.2, Table 2]. Template codes put some 1.5 < z < 3
galaxies at z < 0.5, a Lyman–Balmer break confusion; in a four-band field
whose colours differ from the ECDFS training set, machine-learning n(z)
inherit the training-set redshift distribution [src: Sect. 4.2, 4.4].
Assigning five equipopulated bins from the mode is right for 59–78% of
galaxies [src: Table 2].

Adding bands. Infrared bands help mainly at high redshift: for DES Y6 Gold, adding WISE
W1 and W2 to DNF improves scatter, bias and outlier fraction, adding VHS at
the available depth gives no further gain at z < 1.5, and infrared data with
S/N < 10 add nothing (Puebla et al. 2026, arXiv:2607.07771) [src]. Euclid
near-infrared photometry improves Rubin DP1 photo-z at z > 1.2 (Zhang et al.
2025, arXiv:2510.07370) [src].

## 3. Ensemble n(z) characterisation
<!-- key: ensemble-n-z-characterisation -->

Uncertainty on the mean redshift of a tomographic bin, σ⟨z⟩ or |Δ⟨z⟩|,
by method. "Mocks" means a simulated test; "data" a calibration actually
used. The per-analysis priors and their S8 consequences are in
`cosmo-weak-lensing`.

| Method, survey | Setting | σ⟨z⟩ or bias of the mean | Reference |
|---|---|---|---|
| Stage-III methods, idealised (review compilation) | earlier / latest methods | 0.004–0.05 / 0.001–0.006 | arXiv:2206.13633 [src: Sect. 2.3] |
| KiDS SOM direct calibration | mocks | σ ≤ 0.006 per bin; maximal bias 0.013 ± 0.006 (≤ 0.025 at 97.5%) | arXiv:1909.09632 [src] |
| DES SOMPZ (Y3-like) | idealised simulation | σ_Δz = 0.007 per bin | arXiv:1901.05005 [src] |
| DES Y3 SOMPZ + WZ + SR | data | σ⟨z⟩ ~ 0.01 per bin | arXiv:2012.08566 [src] |
| DES Y3 clustering redshifts | simulations | RMS ~ 0.014 | arXiv:2012.08569 [src] |
| DES Y6 SOMPZ + WZ | data, bins at 0.414, 0.538, 0.846, 1.157 | 0.012, 0.008, 0.009, 0.024 | arXiv:2510.23566 [src] |
| DES Y6 MagLim++ lenses, SOMPZ + WZ | data | 1–2% of the mean, 20–30% below Y3 | arXiv:2509.07964 [src] |
| KiDS clustering redshifts | MICE mocks | |Δz| < 0.006 (truth as model); up to ~0.04 (colour n(z) as model) | arXiv:2007.01846 [src] |
| DESI unified calibration of DES, HSC, KiDS | data | σ_z̄ ~ 0.01 or better | arXiv:2510.25419 [src] |
| Euclid SOM | DR3-like mocks | 8 of 10 bins within 0.002(1+z) with photo-z binning; ≤ 6 with C3R2-like calibration | arXiv:2508.02779 [src] |
| Euclid clustering redshifts | Flagship 2 mocks | all bins to z_phot ≤ 1.6 within 0.002(1+z) with the shifted-stretched model; slightly outside in bins 1, 3, 7 with the conservative Gaussian-process model, inside again for doubled patches | arXiv:2505.10416 [src: Sect. 5] |
| Hierarchical colours + clustering | N-body mocks with prior shifted by 0.05 | residual ≲ 0.003 | arXiv:1910.07127 [src] |
| Forward model (SPS + data model) | GAMA / VVDS data | ≲ 0.003 / ≃ 0.01, no tuning | arXiv:2207.05819 [src] |
| GalSBI-SPS | HSC COSMOS, literature parameters | offset 0.01–0.08 | arXiv:2505.21610 [src] |
| pop-cosmos versus shark | KiDS-1000 bins 1 and 5 | Δz ~ 0.05–0.1 between population models | arXiv:2602.03935 [src] |
| Learned SED prior | controlled mocks | ≲ 0.0007(1+z) | arXiv:2609.26594 [src] |
| Lyα-forest cross-correlation | DESI-5yr × LSST-10yr mocks, z̄ = 2 | σ_z/(1+z̄) = 0.006 (**forecast**) | arXiv:2601.16962 [src] |

**Error budgets read in the papers.**

- *DES Y3 sources (Myles et al. 2021, arXiv:2012.08566).* Shot noise and
  sample variance 0.006, 0.005, 0.004, 0.006; redshift-sample choice 0.003,
  0.004, 0.006, 0.006; deep-field photometric calibration 0.010, 0.005,
  0.002, 0.002; Balrog transfer < 0.001; SOMPZ method 0.003 [src: Table 2].
  The prior used in cosmology, after WZ and blending, has σ⟨z⟩ = 0.018,
  0.015, 0.011, 0.017; sample variance in the deep fields is the largest
  term overall, the redshift sample leads in bin 3 [src: Table 2, Sect. 5.6].
- *DES Y6 sources (Yin et al. 2025, arXiv:2510.23566).* Method: a 32 × 32
  wide SOM on griz fluxes (not colours, noise-dominated at low S/N) is
  linked to a 64 × 64 deep SOM on ugrizJHKs through Balrog injections,
  p(z|b) = Σ p(z|c,b) p(c|ĉ) p(ĉ|b), with wide cells binned by the mode of
  their n(z) [src: Sect. 4.1, Eqs. 5–8; Sect. 4.2]; COSMOS2020 and PAUS
  redshifts are perturbed by their median offset and scatter from spectra
  per magnitude–redshift cell [src: Sect. 5.1, Eqs. 9–11]; blending enters
  as n → (1+F_i(z)) n, fitted on image simulations, whose integral gives the
  shear bias m_i [src: Sect. 7.1, Eqs. 27–29]. σ⟨z⟩ per bin
  grows as each term is added: shot noise alone 0.003, 0.002, 0.001, 0.003;
  with sample variance 0.008, 0.005, 0.004, 0.009; with deep-field
  zero-point uncertainty 0.010, 0.008, 0.006, 0.010; with the
  calibration-sample (redshift) uncertainty 0.012, 0.011, 0.012, 0.028
  [src: Table 2]. Adding WZ lowers these to 0.009, 0.008, 0.008, 0.025 and
  raises every bin mean by 0.007–0.013; the blending correction then lowers
  the four means by 0.013, 0.021, 0.002 and 0.034 [src: Table 2]. The
  calibration-sample term dominates because the source limit moved from
  i = 23.5 (Y3) to 24.7 and spectra are only 19% of the calibration sample
  in the highest bin against 48% in the first [src: Sect. 5.1]. On simulated
  data vectors, mean shifts Δz and seven-mode sampling give S8 constraints
  differing by 0.004σ (cosmic shear) and 0.039σ (3×2pt), and WZ tightens
  S8 by 10% and 7% [src: Sect. 8.2].
- *KiDS-Legacy (Wright et al. 2025, arXiv:2503.19440).* One 51 × 51 SOM
  per tomographic bin (KiDS-1000: one 101 × 101 SOM) on all colours of the
  ten-band photometry; gold weights averaged over many SOM trainings replace
  the gold class, whose per-source flags proved stochastic; bin biases
  δz = μ̂_z − μ_z come from SKiLLS mocks [src: Sect. 4.1–4.2, Eq. 3]. SOM biases from
  SKiLLS, as median shifts, are −0.002, 0.015, 0.006, 0.005, −0.005 and
  −0.056 in the six bins, each ±0.010–0.011 after an error floor; the
  clustering-redshift shift fits D_z are 0.000 ± 0.007, 0.028 ± 0.006,
  0.021 ± 0.006, 0.035 ± 0.010, −0.018 ± 0.028 and −0.145 ± 0.091, and
  their difference from the SOM bias is consistent with zero except in bin
  four (~2σ) [src: Table 8, Sect. 7.2.2]. Bin six is poorly constrained
  because DESI stops at z ≈ 1.6 [src: Sect. 7.2.1]. The mean bias of bin
  one (−0.026) differs from its median because of a small high-z outlier
  population [src: Table 8, Sect. 7.2.2].
- *HSC Y3 (Rau et al. 2023, arXiv:2211.16516).* The n(z) prior is a
  logistic Gaussian process (lognormal counts per redshift bin, cross-bin
  correlations) carrying the COSMOS2015 cosmic variance; the lensing
  analysis varies only the mean of the MAP n(z) [src: Sect. 5.4, Eq. 6;
  Sect. 5.7]. Bin means from DNNz
  photometry alone are 0.463, 0.766, 1.084, 1.330 with statistical σ of
  only 0.003–0.005; adding LRG cross-correlations (bins 1–3) moves bin 1 to
  0.452 with a Bayesian surprise of 3.84, against 0.10 and 0.28 in bins 2
  and 3, read as unaccounted systematics in bin 1 [src: Table 1,
  Sect. 5.7]. The adopted totals, 0.024, 0.022, 0.031 and 0.034, add the
  DNNz–DEMPz difference linearly to the joint error, a conservative bound
  from Eq. 11 [src: Table 1, Sect. 5.7]. The HSC Y1 errors were 0.0285,
  0.014, 0.0383, 0.0376 [src: Table 1].
- *DESI unified calibration (Lange et al. 2025, arXiv:2510.25419).* DESI
  COSMOS–XMM spectra, supplemented by COSMOS2020 photo-z, give bin means
  whose shot-noise errors are 0.003–0.010, with a cosmic-variance column
  (σ_CV/b) of 0.004–0.012; the differences from the published means are
  −0.014 to +0.017 for DES Y3, −0.015 to +0.014 for HSC Y1, and up to
  +0.036 (bin 1) and +0.038 (bin 4) for KiDS-1000 [src: Table 1]. Against
  DES Y3 without its blending and WZ steps, the differences fall to −0.010,
  −0.007, +0.008, −0.004 [src: Sect. V.1].

Requirements to compare with: LSST DESC SRD δz < 0.001(1+z) at year 10
for lensing sources, 0.002(1+z) as the year-1 goal (arXiv:1809.01669)
[src: Sect. 5.2]; Euclid weak lensing 0.002(1+z)
(arXiv:2208.10503) [src]; Euclid DR1 photometric clustering 0.004(1+z) for
80% of the w0wa 3×2pt power (arXiv:2604.00805) [src]. These are **forecast**
requirements.


## 4. Challenge results
<!-- key: challenge-results -->

| Challenge | Set-up | Main finding | Reference |
|---|---|---|---|
| PHAT0 / PHAT1 | simulations / GOODS multi-band data | scatter differs by up to 2× between codes even in the idealised PHAT0; on PHAT1 scatter 4–8% in Δz/(1+z), outliers > 7.5% (|Δz|/(1+z) > 0.15), > 4.5% after cleaning; empirical codes less biased than template codes; few codes gain from mid-IR | Hildebrandt et al. 2010, arXiv:1008.0658 [src] |
| CANDELS | eleven participants, U to mid-IR deep photometry | no code or template set is significantly better; the best use a training sample for zero points, template adjustment or extra errors; quoted 68% intervals too small; all codes significantly biased (bias < scatter); combining codes lowers scatter and outliers | Dahlen et al. 2013, arXiv:1308.5353 [src] |
| LSST DESC (DC1) | twelve PDF codes, perfect template library and representative training set | systematic biases and over/under-broad PDFs in many codes; CDE loss proposed | Schmidt et al. 2020, arXiv:2001.03621 [src] |
| Euclid photo-z challenge | thirteen codes on emulated Euclid photometry of COSMOS, 0.2 < z < 2.6, blind validation | participants' rejection flags remove strong outliers (> 0.15(1+z)); all methods give reliable point estimates, several machine-learning methods do not give useful PDFs | Euclid Collaboration: Desprez et al. 2020, arXiv:2009.12112 [src] |
| Rubin DP1 | eight RAIL codes on real ComCam data | σ_NMAD 0.028–0.055, outliers 12–20%, ML photo-z within LSST Y1 bias and scatter requirements | arXiv:2510.07370 [src: Table 2] |

**Euclid challenge in numbers (arXiv:2009.12112).** σ is the NMAD of
(z_spec − z_phot)/(1+z_spec) and η the fraction with |Δz| > 0.15
[src: Sect. 4.1]. On the 12,463 reliable spectra without rejection, σ runs
from 0.046 (Le Phare, Adaboost) to 0.078 (GPz) and η from 9.2% (Adaboost)
to 28.3% (frankenz, whose missing estimates count as outliers)
[src: Table 4]. In the Euclid selection (0.2 < z_phot < 2.6, USE = 1),
METAPHOR reaches σ = 0.036 and η = 2.7% but keeps 7865 sources, while
ANNz keeps 12,012 at σ = 0.048, η = 10.1% [src: Table 5]. Weighted to the
colour space of the full shear sample (Lima et al. weights), η rises to
13–33% for most codes, and METAPHOR (3.1%) and DNF (9.3%) keep their
precision only by rejecting about two-thirds and three-quarters of the
weighted sample [src: Table 6, Sect. 4.1]. Template codes in identical
configuration give near-identical results; differences among them come
from the configuration and the point-estimate definition (median versus
mode of the PDF) [src: Sect. 4.1]. Rejection flags buy precision at the
cost of completeness [src: Sect. 4.1].

With representative training data, most methods in these challenges still
miss LSST Y1 characterisation requirements; real-data errors are larger
(Newman & Gruen 2022, arXiv:2206.13633) [src: Sect. 2.3].


## 5. History: what superseded what
<!-- key: history-what-superseded-what -->

| Quantity | Older value | Superseded by | Why |
|---|---|---|---|
| SDSS relative calibration | ~1% (ubercal, arXiv:astro-ph/0703454) | zero points re-anchored to AB through the IRFM temperature scale: r well standardised, offsets of a few hundredths in i and z, filter-curve-dependent u offset (arXiv:2606.11587) [src] | absolute AB tie, not relative uniformity |
| DES calibration uniformity | 7 mmag (Y3 FGCM, arXiv:1706.01542) | < 1.8 mmag RMS (Y6 catalogue, arXiv:2305.01695) [src] | more epochs, refined FGCM |
| Survey standards | stellar locus; Landolt fields | Gaia XP + SCR, BEST (arXiv:2309.11225, arXiv:2601.05486) [src] | stellar locus errors up to 15 mmag |
| Galactic reddening | SFD (arXiv:astro-ph/9710327) | SFD with its 14% recalibration and new R_b tables (arXiv:1012.4804), CSFD (arXiv:2306.03926), DESI stellar maps (arXiv:2409.05140) [src] | normalisation, CIB contamination |
| COSMOS reference photo-z | COSMOS2015 | COSMOS2020 (same precision ~1 mag deeper, arXiv:2110.13923); COSMOS2025 (~2× better at 26 AB, arXiv:2506.03243) [src] | deeper imaging, JWST |
| Euclid colour-space coverage by spectra | 51% (Masters et al. 2015) | 91% (C3R2 DR3, arXiv:2106.11367) [src] | targeted spectroscopy |
| DES lensing source calibration | Y3, σ⟨z⟩ ~ 0.01 (arXiv:2012.08566) | Y6, 0.008–0.024 with NIR in SOMPZ (arXiv:2510.23566) [src] | deeper, fainter bins; dominant term is missing faint spectra |
| Stacked p(z) as n(z) | common in Stage III | hierarchical / forward inference (arXiv:2007.12178, arXiv:1602.05960) [src] | stacking is biased |

## 6. Requirements
<!-- key: requirements -->

All are **forecast**-derived: they follow from requiring that n(z) errors
not dominate the statistical error of the survey.

| Survey | Requirement | Source |
|---|---|---|
| Rubin LSST, WL (3×2pt sources), year 10 / year-1 goal | mean redshift per bin known to δz < 0.001(1+z) / 0.002(1+z); scatter known to δσ_z < 0.003(1+z) / 0.006(1+z) | LSST DESC SRD, requirements WL1, WL2 (arXiv:1809.01669) [src: Sect. 5.2]; also summarised in arXiv:2206.13633, Sect. 1.2.2 [sec] |
| Rubin LSST, LSS (photometric clustering), year 10 / year-1 goal | δz < 0.003(1+z) / 0.005(1+z); δσ_z < 0.03(1+z) / 0.1(1+z) | SRD requirements LSS1, LSS2 [src: Sect. 5.1] |
| Rubin LSST, cluster WL masses, year 10 / year-1 goal | δz < 0.001(1+z) / 0.008(1+z); δσ_z < 0.005(1+z) / 0.02(1+z) | SRD requirements CL1, CL2 [src: Sect. 5.3]; same values for year 10 in arXiv:2206.13633 [sec] |
| Euclid, ten tomographic bins | σ(⟨z⟩) < 0.002(1+z), or |Δ⟨z⟩| ≤ 0.002(1+z); the width σ_n of each bin to 10%, σ(σ_n) ≤ 0.1 σ_n | arXiv:2208.10503, arXiv:2508.02779 [src]; width criterion arXiv:2505.10416 [src: Sect. 3.5.1, Eqs. 67–68] |

The SRD study assumed Gaussian photo-z errors without outliers; higher
moments of n(z) will also matter [sec: arXiv:2206.13633, Sect. 1.2.2].
In the SRD itself, each mean-redshift requirement was derived by shifting
the means of all bins coherently (tighter than single-bin shifts, looser
than a dark-energy-like pattern), and the scatter requirement by broadening
the photo-z scatter in the data vector while keeping it fixed in the model;
the mean and the scatter each receive 0.7/√7 ≈ 0.25 of the calibratable
systematic budget of the WL analysis (arXiv:1809.01669) [src: Sect. 5.1–5.3,
App. J2.3]. The SRD names full N(z) calibration, including outliers, as the
task of its PZCalibrate pipeline [src: Sect. 6]. The Rubin DP1 paper tests
per-galaxy photo-z against |bias| < 0.005 and σ < 0.1, the values of the
year-1 LSS goals (arXiv:2510.07370) [src: Sect. 4.2].


## Not verified
<!-- key: not-verified -->

- No published Rubin LSST or Euclid DR1 n(z) calibration on wide-survey data
  was found; the Rubin and Euclid numbers above are from commissioning data,
  Q1 or mocks.
- The DESC SRD requirements, formerly quoted through the Newman & Gruen
  review, were read in the SRD body this session (§6 above).
- The outlier threshold of the PAUS entries was not read in the bodies
  (Rubin DP1: |Δz| > 0.15, read in Sect. 3.4 of arXiv:2510.07370).
