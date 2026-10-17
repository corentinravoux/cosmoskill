# Photometry and photometric redshifts — surveys and data

Scope: photometric standards and reference catalogues, imaging surveys and
their photo-z products, many-band calibration fields, and the spectroscopic
samples used to train and calibrate photo-z.
Snapshot: 2026-10-16

Flags: `[src]` read this session in the abstract of the cited paper;
`[src: Sect. n]` read in the body; `[sec]` from a named secondary source.
Facility facts (aperture, field of view, survey dates) are kept in
`cosmo-surveys-facilities`; this file holds what matters for photometry and
redshifts.

## 1. Standards and reference catalogues
<!-- key: standards-and-reference-catalogues -->

| Resource | Content | Reference |
|---|---|---|
| HST CALSPEC | STIS (0.17–1.0 μm) and WFC3 IR grism (0.8–1.7 μm) spectrophotometry of white dwarfs and stars; the absolute scale of most optical surveys | arXiv:1502.01754, arXiv:1903.11985, arXiv:1403.6861 [src] |
| Gaia DR3 XP spectra and GSPC | flux-calibrated 330–1050 nm spectra for ~220 million sources; synthetic photometry in common systems | arXiv:2206.06215 [src] |
| DES Y6 FGCM catalogue | grizY for 17 million stars, 16 < i < 21, 5000 deg², 1.8 mmag uniformity | arXiv:2305.01695 [src] |
| BEST | > 200 million standards in > 200 passbands, all sky | arXiv:2601.05486 [src] |
| DESI stellar reddening maps | E(g−r), E(r−z) from 2.6 million stars, high Galactic latitude | arXiv:2409.05140 [src] |
| CSFD | SFD with CIB/LSS removed | arXiv:2306.03926 [src] |

What each standard has shown:

- **HST CALSPEC.** The absolute flux scale of most surveys is tied to HST
  STIS spectrophotometry of white-dwarf and stellar standards. Synthetic
  photometry from STIS agrees with ground-based B, V, R, I photometry of
  eleven CALSPEC stars to better than about 1% (Bohlin & Landolt 2015,
  arXiv:1502.01754) [src]; WFC3 IR grism spectra extend the scale to 1.7 μm at
  about 1% (Bohlin & Deustua 2019, arXiv:1903.11985) [src]. Sirius and Vega
  monochromatic fluxes at 5557.5 Å are given to 0.5% formal uncertainty
  (Bohlin 2014, arXiv:1403.6861) [src].
- **Gaia XP synthetic photometry.** Gaia DR3 provides flux-calibrated
  low-resolution spectra for about 220 million sources over 330–1050 nm, from
  which synthetic photometry can be computed for any passband inside that
  range; existing high-quality photometry is reproduced to a few percent, and
  to millimag after standardisation against external photometry (Gaia
  Collaboration, Montegriffo et al. 2022, arXiv:2206.06215) [src].
- **Stellar colour regression (SCR).** Spectroscopic stellar parameters
  (LAMOST) predict intrinsic colours, giving standards per star. Applied to
  J-PLUS and S-PLUS it exposed position-dependent zero-point errors of up to
  15 mmag (stellar-locus method) and 23 mmag (S-PLUS DR4), and errors of up to
  10 mmag in uncorrected Gaia XP synthetic photometry; with corrected XP
  spectra the two routes agree to 1–6 mmag (Xiao et al. 2023,
  arXiv:2309.11225, arXiv:2309.11533) [src]. The BEST database extends this to
  more than 200 million standards in over 200 passbands at better than 10
  mmag (Xiao et al. 2026, arXiv:2601.05486) [src].
- **Temperature scale.** The infrared flux method applied to over 6000 FGK
  stars finds the SDSS r band well standardised, offsets of a few hundredths
  of a magnitude in i and z, a small one in g, and a u-band offset that
  depends on whether the red leak of the filter is included (Zhou et al.
  2026, arXiv:2606.11587) [src].

In practice a modern survey calibration uses all three layers: internal
relative calibration from repeated stars (ubercal or FGCM), an external
check of its spatial pattern against Gaia XP or SCR standards, and an
absolute tie to CALSPEC (arXiv:2305.01695, arXiv:2309.11533) [src].

## 2. Imaging surveys and their photo-z products
<!-- key: imaging-surveys-and-their-photo-z-products -->

| Survey | Photometry | Photo-z product and status | Reference |
|---|---|---|---|
| DESI Legacy Imaging Surveys | DECaLS, BASS, MzLS: ~14,000 deg² in g, r, z plus WISE 3.4–22 μm; source shapes and fluxes from probabilistic inference | catalogues and software public, two releases per year planned | Dey et al. 2019, arXiv:1804.08657 [src] |
| Legacy Surveys DR8, all-sky photo-z | as above, ~19,400 deg² | sparse Gaussian processes with Gaussian-mixture partitioning and cost-sensitive weights against training-set bias; ≳ 9 × 10⁸ galaxies, 0 < z ≲ 7; less biased at z > 1 than earlier estimates | Duncan 2022, arXiv:2203.01949 [src] |
| HSC-SSP DR1 / DR2 | grizy | several codes compared and calibrated; σ(Δz/(1+z)) ~ 0.05 and ~15% outliers to i = 25 at 0.2 ≲ z_phot ≲ 1.5, ~0.04 and ~8% at i < 24; some codes mis-estimate PDF widths; point estimates and full PDFs public | Tanaka et al. 2018, arXiv:1704.05988; Nishizawa et al. 2020, arXiv:2003.01511 [src] |
| DES Y6 MagLim++ lens sample | grizY with deep fields and Balrog injections | SOMPZ with noise-weighted metric, O(10⁸) n(z) realisations importance-sampled with clustering redshifts; mean-z uncertainty 1–2%, 20–30% below Y3; compressed to orthogonal modes | Giannini et al. 2025, arXiv:2509.07964 [src] |
| KiDS DR5 (KiDS-Legacy) | 1347 deg² of lensing imaging plus 27 deg² over spectroscopic fields; VST ugri (i observed twice) and VISTA ZYJHKs, 5σ limits from r = 25.07 to Ks = 22.02 | photo-z cuts z_B define six equipopulated bins over 0.1 < z_B ≤ 2.0, 41 million sources, n_eff = 8.8 arcmin⁻²; n(z) from per-bin SOMs with gold weights, checked by clustering redshifts | Wright et al. 2025, arXiv:2503.19440 [src: Sect. 2, Tables 1, 3] |
| DES Y6 Gold | 5000 deg² grizY | DNF reference photo-z; WISE-enhanced release | arXiv:2607.07771 [src] |
| Rubin LSST DP1 | ComCam ugrizy in ECDFS, griz elsewhere | eight RAIL codes run; σ_NMAD ~ 0.03 | arXiv:2510.07370 [src] |
| Euclid Q1 | VIS + NISP with ground-based photometry | PHZ pipeline: star/galaxy/QSO classification, photo-z and physical properties; precision compatible with requirements, but a bias correction is needed for cosmology; QSO separation from photometry insufficient | Euclid Collaboration: Tucci et al. 2025, arXiv:2503.15306 [src] |
| HSC-CLAUDS | multi-field u to y | CNN redshifts with domain adaptation for ~4 million sources at i < 25 | arXiv:2512.11700 [src] |

## 3. Many-band and narrow-band calibration fields
<!-- key: many-band-and-narrow-band-calibration-fields -->

| Survey | Bands | Role | Reference |
|---|---|---|---|
| COSMOS2020 | ~2 deg²; 1.7 million sources, ~966,000 with all broad bands; aperture and profile-fitting (The Farmer) photometry, two photo-z codes | sub-percent photo-z at i < 21, 5% at 25 < i < 27; same precision as COSMOS2015 almost one magnitude deeper; the reference truth for many SOM and forward-model calibrations | Weaver et al. 2022, arXiv:2110.13923 [src] |
| COSMOS2025 (COSMOS-Web) | JWST NIRCam (4 bands) + MIRI over ~0.54 deg², 37 bands 0.3–8 μm, > 700,000 galaxies | σ_MAD = 0.012 at m_F444W < 28 against spectra to z ~ 9; ~2× better than COSMOS2020 at 26 AB; PDFs released | Shuntov et al. 2025, arXiv:2506.03243 [src] |
| PAUS design | 40 narrow bands of 12.5 nm FWHM, 450–850 nm, on the WHT | design goal σ(z)/(1+z) ~ 0.0035 to i_AB < 22.5–23.0 (simulations) | Martí et al. 2014, arXiv:1402.3220 [src] |
| PAUS COSMOS | as above + broad bands | σ_68/(1+z) = 0.0037 to i_AB < 22.5 for the best 50% (BCNz2, zCOSMOS DR3); ~0.001 for a bright high-quality selection driven by emission lines | Eriksen et al. 2019, arXiv:1809.04375 [src] |
| PAUS wide fields | ~50 deg², ~1.8 million objects to i_AB < 23, overlapping CFHTLenS W1, W3 and KiDS/GAMA G09 | σ_68 ≃ 0.019 for all galaxies, bias < 0.01; zero-point calibration independent of spectroscopic samples | Navarro-Gironés et al. 2023, arXiv:2312.07581 [src] |
| miniJPAS (J-PAS demonstration) | ~1 deg² of AEGIS in 60 bands, 54 narrow and 6 broad over 3800–9100 Å | template photo-z (jphotoz pipeline) with odds parameter: 64% of r < 23 galaxies within |Δz| < 0.03, 87% at odds > 0.61; mode carries a systematic offset Δz_sys = (1.4 ± 0.1) × 10⁻³, which also tilts the PIT and is removed by shifting the PDFs | Hernán-Caballero et al. 2021, arXiv:2108.03271 [src: Sect. 4.1, 6.2] |
| J-PLUS, S-PLUS | 12 broad and medium bands (J-PLUS) | recalibrated with Gaia XP and SCR to 1–6 mmag agreement; illustrate how medium-band surveys depend on external standards | arXiv:2309.11225, arXiv:2309.11533 [src] |
| PAUS | 40 optical narrow bands | σ_NMAD/(1+z) = 0.011 for a validation-like mock sample; joint with Euclid forecast to reach 0.011 and < 4% outliers to i < 23.5 for a deeper survey (**forecast**) | arXiv:2606.25812 [src] |

SPHEREx (NASA Medium-Class Explorer, all-sky 0.75–5 μm low-resolution
spectral survey) is the space analogue. Simulations based on COSMOS2020 SEDs
forecast 19 million galaxies with σ_z < 0.003(1+z), 445 million with σ_z <
0.1(1+z) and 810 million with σ_z < 0.2(1+z) over 30,000 deg² (**forecast**;
Feder et al. 2023, arXiv:2312.04636) [src]. Spectral confusion from faint
untargeted galaxies (0.8–3.8 μJy, 1σ) is negligible at full-sky depth but
significant in the deep fields, where it biases redshifts slightly high
(Huai et al. 2025, arXiv:2510.01410) [src].

## 4. Spectroscopic training and calibration samples
<!-- key: spectroscopic-training-and-calibration-samples -->

Spectroscopy cannot replace photometry for lensing-depth samples: Newman &
Gruen 2022 (arXiv:2206.13633) estimate that spectra of the LSST gold sample (4 billion galaxies, i < 25.3)
at DEEP2 signal-to-noise would take nearly 16,000 years of integration with a
5000-fibre spectrograph on a 10 m telescope, and that 10–25% of faint targets
fail to give a secure redshift at that depth [src: Sect. 1.1].


| Sample | Depth and size | Note | Reference |
|---|---|---|---|
| VVDS (as used for CFHTLS) | 3241 redshifts, 0 < z < 5 | the calibration set of the CFHTLS Deep photo-z | arXiv:astro-ph/0603217 [src] |
| C3R2 (Keck, GTC, VLT) | targeted to i ~ 24.5 in under-sampled SOM cells; DR1 1283 redshifts; 5130 by DR3 | raises spectroscopic coverage of Euclid colour space (0.2 < z_phot < 2.6) from 51% to 91% | Masters et al. 2017, arXiv:1704.06665; Euclid Collaboration: Stanford et al. 2021, arXiv:2106.11367 [src] |
| DESI DC3R2 (secondary targets) | 230k galaxies with KiDS-VIKING ugriZYJHKs | with ELG, LRG, BGS, spans 56% of the colour space visible to Euclid and LSST; KiDS-VIKING noise creates an apparent magnitude dependence of z at fixed colour | McCullough et al. 2024, arXiv:2309.13109 [src] |
| DESI in COSMOS and XMM/VVDS | > 256k high-quality redshifts | three times earlier compilations in these fields | arXiv:2512.15964 [src] |
| DESI-Deep pilot | to m_i ≤ 24.5 | DESI on the 4 m Mayall reaches redshift success comparable to 10 m-class telescopes in only ~2× longer integration (not the ~8× of aperture scaling), with ~30× the multiplex; S/N background-limited up to ~7 h; proposed "DESI-Deep" survey for LSST training | Dey et al. 2026, arXiv:2604.06143 [src] |

The spectroscopic needs were set out in a community white paper: large
allocations on kilo-object spectrographs for training and calibration, or,
as the alternative route for calibration, cross-correlation with the bright
samples of a BAO survey such as DESI (Newman et al. 2013,
arXiv:1309.5384) [src]. DESI now plays both roles: targeted faint
spectroscopy (DC3R2, DESI-Deep) and clustering reference (§8 of
physics-and-methods).

## 5. What is expected next
<!-- key: what-is-expected-next -->

Dates and facility parameters are kept in `cosmo-surveys-facilities`; what
matters here:

- **Rubin LSST.** Photo-z production runs through RAIL (arXiv:2505.02928)
  [src]; the commissioning-camera test reached σ_NMAD ~ 0.03 on DP1
  (arXiv:2510.07370) [src]; system throughput is being mapped in situ by the
  Collimated Beam Projector (arXiv:2606.31822) [src].
- **Euclid.** The PHZ pipeline runs on Q1 and needs a bias correction for
  cosmology (arXiv:2503.15306) [src]; SOM and clustering calibrations are
  validated on Flagship mocks (arXiv:2508.02779, arXiv:2505.10416) [src];
  C3R2 supplies targeted spectra (arXiv:2106.11367) [src].
- **DESI.** Deep spectroscopy for LSST training (DESI-Deep, arXiv:2604.06143)
  [src], secondary-target calibration (DC3R2, arXiv:2309.13109) [src], and
  wide clustering references including the Lyα forest at 2 < z < 3
  (arXiv:2601.16962, **forecast**) [src].
- **SPHEREx.** All-sky 0.75–5 μm spectrophotometry, with deep-field confusion
  as the known systematic (arXiv:2312.04636, arXiv:2510.01410) [src].
- **COSMOS-Web.** COSMOS2025 is the new deep reference catalogue with PDFs
  (arXiv:2506.03243) [src].
- **Roman.** On HST/CANDELS imaging (F606W, F814W, F125W, F160W) used as a
  Roman proxy, LePhare with default RAIL settings is worse than every
  machine-learning method; a semi-supervised CNN (PITA) on pixels cuts bias
  by 34%, σ_NMAD by 14% and outliers by 17% against a photometry-only
  network to m_F160W < 25; faint-source photo-z will stay label-limited
  (**forecast**; Khederlarian et al. 2026, arXiv:2602.10207)
  [src: Sect. II.1, IV.1.2].
- **CSST.** The 2 m China Space Station Telescope plans a ~17,500 deg²
  NUV-to-NIR survey with its Survey Camera; its Multi-Channel Imager adds
  medium bands for deep fields. On COSMOS-based mocks, LePhare on MCI + SC
  photometry gives σ_z ~ 0.015 and ~1.5% catastrophic outliers, against a
  stated goal of σ ≃ 0.02 (**forecast**; Cao et al. 2021,
  arXiv:2110.07088) [src: Sect. 1, 4]. The paper's launch date ("around
  2024") is outdated; see `cosmo-surveys-facilities`.


## Not verified
<!-- key: not-verified -->

- KiDS DR5 (KiDS-Legacy) photometric data-release paper was not read; the
  DR5 imaging facts above come from Table 1 and Sect. 2 of the
  redshift-calibration paper (arXiv:2503.19440).
- The J-PAS survey itself (beyond the miniJPAS photo-z catalogue,
  arXiv:2108.03271), and the S-PLUS and J-PLUS photo-z releases, were not
  read beyond the calibration papers.
- Roman and CSST photo-z plans were read only in one simulation paper each
  (arXiv:2602.10207, arXiv:2110.07088); the official Roman High Latitude
  Survey and CSST survey-definition papers were not read.
- Public data locations (archives, URLs) of the catalogues above were not
  checked beyond what the abstracts state (HSC: the release site named in
  arXiv:1704.05988; COSMOS2020: ESO, IRSA and CDS per arXiv:2110.13923).
