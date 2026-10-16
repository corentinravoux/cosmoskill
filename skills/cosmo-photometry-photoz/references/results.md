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
| Rubin DP1 (ComCam), eight RAIL codes | 6-band ECDFS | σ_NMAD ~ 0.03 | ~10% | arXiv:2510.07370 [src] |
| COSMOS2020 (30+ bands) | i < 21 / 25 < i < 27 | sub-percent / 5% precision | — | arXiv:2110.13923 [src] |
| COSMOS2025 (JWST + 37 bands) | m_F444W < 28, spectra to z ~ 9 | σ_MAD = 0.012 | — | arXiv:2506.03243 [src] |
| PAUS + broad bands, COSMOS | i_AB < 22.5, best 50% | σ_68/(1+z) = 0.0037 | — | arXiv:1809.04375 [src] |
| PAUS wide fields | i_AB < 23 | σ_68 ≃ 0.019 (0.003–0.02 for z_b ~ 0.1–0.75) | bias < 0.01 | arXiv:2312.07581 [src] |
| KiDS-1000, pop-cosmos | DESI BGS / LRG matches | σ_MAD = 0.03 / 0.05 | 3.2% / 1.0% | arXiv:2602.03930 [src] |
| PAUS 40 narrow bands, Flagship 2 simulation | like the spectroscopic validation sample / complete to i ≲ 23 | σ_NMAD/(1+z) = 0.011 / 0.028 | < 10% | arXiv:2606.25812 [src] |

Rubin DP1 is the first photo-z test on LSST Commissioning Camera data; the
bias and scatter of its machine-learning photo-z meet the LSST Y1
requirement, with degradation at faint magnitudes and z > 1.2
(arXiv:2510.07370) [src].

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
| Euclid clustering redshifts | Flagship 2 mocks | all bins to z_phot ≤ 1.6 within 0.002(1+z) | arXiv:2505.10416 [src] |
| Hierarchical colours + clustering | N-body mocks with prior shifted by 0.05 | residual ≲ 0.003 | arXiv:1910.07127 [src] |
| Forward model (SPS + data model) | GAMA / VVDS data | ≲ 0.003 / ≃ 0.01, no tuning | arXiv:2207.05819 [src] |
| GalSBI-SPS | HSC COSMOS, literature parameters | offset 0.01–0.08 | arXiv:2505.21610 [src] |
| pop-cosmos versus shark | KiDS-1000 bins 1 and 5 | Δz ~ 0.05–0.1 between population models | arXiv:2602.03935 [src] |
| Learned SED prior | controlled mocks | ≲ 0.0007(1+z) | arXiv:2609.26594 [src] |
| Lyα-forest cross-correlation | DESI-5yr × LSST-10yr mocks, z̄ = 2 | σ_z/(1+z̄) = 0.006 (**forecast**) | arXiv:2601.16962 [src] |

Requirements to compare with: LSST DESC SRD δz < 0.001(1+z) at year 10
[sec: arXiv:2206.13633, Sect. 1.2.2]; Euclid weak lensing 0.002(1+z)
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
| Rubin DP1 | eight RAIL codes on real ComCam data | σ_NMAD ~ 0.03, ~10% outliers, ML photo-z within LSST Y1 bias and scatter requirements | arXiv:2510.07370 [src] |

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
| Rubin LSST, WL + LSS, year 10 | mean redshift per bin known to δz < 0.001(1+z); scatter known to δσ_z < 0.003(1+z) | LSST DESC SRD (arXiv:1809.01669) as summarised by Newman & Gruen 2022 [sec: arXiv:2206.13633, Sect. 1.2.2] |
| Rubin LSST, cluster WL masses | δz < 0.001(1+z); δσ_z < 0.005(1+z) | same [sec: arXiv:2206.13633, Sect. 1.2.2] |
| Euclid, ten tomographic bins | σ(⟨z⟩) < 0.002(1+z), or |Δ⟨z⟩| ≤ 0.002(1+z) | arXiv:2208.10503, arXiv:2508.02779 [src] |

The SRD study assumed Gaussian photo-z errors without outliers; higher
moments of n(z) will also matter [sec: arXiv:2206.13633, Sect. 1.2.2].


## Not verified
<!-- key: not-verified -->

- No published Rubin LSST or Euclid DR1 n(z) calibration on wide-survey data
  was found; the Rubin and Euclid numbers above are from commissioning data,
  Q1 or mocks.
- The DESC SRD requirements are quoted through the Newman & Gruen review,
  not read in the SRD.
- Outlier thresholds of the Rubin DP1 and PAUS entries were not read in the
  bodies.
