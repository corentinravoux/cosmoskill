# Data pipelines — surveys and data products

Scope: which pipeline each survey runs, what its releases contain at catalogue
and map level, and where the products live. Instrument facts and release
dates are in `cosmo-surveys-facilities`.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Table n]`
body read; `[sec]` named secondary source; `[der]` derived here.

## 1. Spectroscopic surveys
<!-- key: spectroscopic-surveys -->

**Target selections.**

| Survey, tracer | Selection | Target density | Source |
|---|---|---|---|
| BOSS CMASS and LOWZ | colour cuts on SDSS imaging; code MKSAMPLE released | — | Reid et al. 2015, arXiv:1509.06529 [src] |
| eBOSS LRG | SDSS + WISE colours, z < 19.95, 19.9 < i < 21.8 | ~50 deg⁻² | Prakash et al. 2015, arXiv:1508.04478 [src: abstract] |
| eBOSS QSO (CORE) | XDQSOz likelihood + mid-IR–optical cut, g < 22 or r < 22; PTF variability for z > 2.1 | ~70 deg⁻² at 0.9 < z < 2.2 and ~7 deg⁻² at z > 2.1 expected | Myers et al. 2015, arXiv:1508.04472 [src: abstract] |
| eBOSS ELG | g−r vs r−z box + g cut on DECaLS | 200 (NGC), 240 (SGC) deg⁻² | Raichoor et al. 2017, arXiv:1704.00338 [src: abstract] |
| DESI BGS | r < 19.5 (Bright), 19.5 < r < 20.175 colour-selected (Faint) | — | Hahn et al. 2022, arXiv:2208.08512 [src: abstract] |
| DESI LRG | g, r, z, W1 from Legacy Surveys | 605 deg⁻²; n = 5×10⁻⁴ h³ Mpc⁻³ at 0.4 < z < 0.8 | Zhou et al. 2022, arXiv:2208.08515 [src: abstract] |
| DESI ELG | g cut + (g−r) vs (r−z) box, two disjoint subsamples | ~1940 and ~460 deg⁻² | Raichoor et al. 2022, arXiv:2208.08513 [src: abstract] |
| DESI QSO | random forest on g, r, z, W1, W2, 16.5 < r < 23 | 310 deg⁻² | Chaussidon et al. 2022, arXiv:2208.08511 [src: abstract] |
| 4MOST CRS BG, LRG | from Legacy Surveys DR10.1 | 5.4 million redshifts over ~5700 deg² planned | Bandi et al. 2025, arXiv:2510.02449 [src: abstract] |

The trend is from colour boxes to likelihood and machine-learning selections
(XDQSOz in eBOSS, a random forest for DESI quasars) and from SDSS imaging to
the Legacy Surveys, which now serve as the parent imaging for both DESI and
4MOST CRS (arXiv:2510.02449) [src].

**Survey operations as part of the pipeline (DESI).** Afternoon planning,
automatic field selection during the night, real-time completeness from the
exposure-time calculator, morning reduction and redshifting, and update of the
target list (Schlafly et al. 2023, arXiv:2306.06309) [src]. Each tile is
designed on the fly and redesigned at NERSC the next morning, to prove the
assignment can be reproduced [src: arXiv:2306.06309, Sect. V.9]. Depth is
counted in effective time, the exposure that would reach the goal
uncertainty in nominal conditions (1.1″ seeing, r-band sky of 21.07 mag
arcsec⁻², photometric, zenith, no dust): 1000 s for the dark programme, 180 s
for the bright one; extinction lengthens the real exposure
[src: arXiv:2306.06309, Sect. V.2]. Spectroscopic results feed back into
targeting: quasar targets start at priority 3400 with 4 observations planned;
Redrock z ≥ 2.1, or a definite QuasarNET high-z classification, marks a Lyα
quasar for re-observation, while low-z quasars have their remaining count
reduced by three [src: arXiv:2306.06309, Sect. VI.3.3]. The feedback loop
means the selection function depends on the pipeline version used during
operations.

**DESI targeting bookkeeping.** The DESI pipeline `desitarget`
defines a unique TARGETID, the targeting bitmasks, the survey phases
(commissioning, survey validation, main) and the "supporting" classes:
standard stars, blank-sky locations and random catalogues that mimic the
angular selection function (Myers et al. 2023, arXiv:2208.08518) [src]. Its
random points take RELEASE and BRICKID from the Legacy Surveys bricks and
carry a MOCK bit, so they never collide with a real TARGETID
[src: arXiv:2208.08518, Sect. III.1.3]. Where the northern (BASS + MzLS) and
southern (DECaLS) imaging overlap, a "resolve" step keeps the northern
imaging only north of the Galactic plane and at Dec ≥ 32.375°, so every
area has one imaging source [src: arXiv:2208.08518, Sect. IV.1.3]. Blank-sky
fibres come from pixel-level erosion of the detection maps, at 18,000
locations per deg² for the main survey [src: arXiv:2208.08518,
Sect. IV.4.1].

**DESI DR1 LSS catalogue weights** (Ross et al. 2025, arXiv:2405.16593).

| Weight | Corrects | Definition |
|---|---|---|
| w_comp | fibre-assignment incompleteness | 1/f_TLID in DR1; tile-level completeness f_tile folded into the randoms [src: arXiv:2405.16593, Sect. 7.2] |
| w_sys | imaging-induced density variations | regression on survey-property maps (Sect. 5.2 of the paper; methods below) |
| w_zfail | redshift failures that vary with conditions and fibre | Sect. 5.3 of the paper |
| w_FKP | optimal weighting for P(k) | w_FKP = 1/(1 + n(z, N_tile) P₀), with n depending on redshift and number of overlapping tiles, because completeness tracks N_tile [src: arXiv:2405.16593, Sect. 7.3, Eq. 6] |

## 2. Imaging surveys
<!-- key: imaging-surveys -->

**Pipelines.** The HSC pipeline, built on the LSST prototype stack, has
four stages: CCD processing, joint calibration, co-addition and
co-add processing (Bosch et al. 2018, arXiv:1705.06766) [src: Sects. 3–4];
DES runs nightly processing for image-quality decisions and twice-yearly
reprocessing with a refined pipeline before co-addition (Morganson et al.
2018, arXiv:1801.03177) [src]; KiDS uses Astro-WISE for the co-added ugri
images and a separate THELI reduction of the r band for the lensing
catalogue (Kuijken et al. 2019, arXiv:1902.11265) [src]. The Rubin data
management system was designed as a general open-source stack for
optical and infrared surveys and is the basis of the HSC pipeline (Jurić
et al. 2017, arXiv:1512.07914) [src].

**PSF models by survey.**

| Pipeline | Star selection | Model and interpolation | Source |
|---|---|---|---|
| HSC | k-means on second-moment sizes, four clusters, objects brighter than 12,500 counts (i ≈ 22.3); 20% kept for cross-validation; ~72 stars per CCD | PSFEx used as a library, polynomial in position per CCD | Bosch et al. 2018, arXiv:1705.06766 [src: Sect. 4.3] |
| DES Y3 | — | Piff, model varying over the full field of view | Jarvis et al. 2021, arXiv:2011.03409 [src] |
| DES Y6 | Gaia and infrared photometry to purify stars | Piff with colour-dependent PSF, the first in a lensing analysis; fourth-moment diagnostics; g band now usable (excluded in Y3) | Schutt et al. 2025, arXiv:2501.05781 [src] |
| Rubin DP1 | — | Piff, second-order (pipeline default) and fourth-order (final DP1) polynomial interpolation; both underestimate PSF size, the fourth-order less | arXiv:2603.23786 [src: Sect. V.2] |

**Photometry.** HSC measures PSF, fixed-aperture, Kron, CModel and
PSF-matched aperture photometry, plus centroids, shapes, star–galaxy class
and blendedness [src: arXiv:1705.06766, Sect. 4.9 outline]. Calibration of
those fluxes is in `cosmo-photometry-photoz`.

## 3. CMB experiments
<!-- key: cmb-experiments -->

**Planck.** HFI 2018 fits bandpass-mismatch coefficients per detector inside
the map-making and builds frequency maps from single detectors adjusted to
a common bandpass; the Solar dipole is the calibrator (Planck 2018 III,
arXiv:1807.06207) [src]. LFI 2018 improved calibration and ADC
non-linearity corrections (Planck 2018 II, arXiv:1807.06206) [src]. NPIPE
processes LFI and HFI jointly and ships 600 end-to-end simulations with full
time-domain processing, plus the raw and processed TOD and the software
(Planck Collaboration 2020, arXiv:2007.04997) [src].

**ACT DR6** (arXiv:2503.14451). The noise model is built from the data, which
contains the sky; so a first map is subtracted before the noise model is
rebuilt. Three passes: 300 CG steps with 4× downsampling for the first two,
30 CG steps without downsampling for the last; the second and third passes
also subtract the polarised sidelobes [src: arXiv:2503.14451, Sect. III.4].
For DR6, TOD filtering was dropped to keep low ℓ, ground pickup being removed
in map space; the transfer function is measured by injecting a simulated
sky into the real data, TF(ℓ) = crossspec(map(d + P sim) − map(d), sim) /
powspec(sim) [src: arXiv:2503.14451, Sect. V.2, Eq. 13].

## 4. What each release contains
<!-- key: what-each-release-contains -->

Release dates, instruments and status are in `cosmo-surveys-facilities`;
this table keeps catalogue- and map-level content.

| Release | Content relevant to pipelines | Source |
|---|---|---|
| SDSS DR16 (eBOSS) | DR16Q: 750,414 quasars, VI for 320,161 spectra; LSS catalogues: 343,708 quasars at 0.8 < z < 2.2 over 4808 deg², 174,816 eBOSS LRGs combined with BOSS into 377,458 over 9493 deg² | arXiv:2007.09001, arXiv:2007.09000 [src] |
| SDSS DR17 | last SDSS-IV release; eBOSS main sample was complete in DR16 | arXiv:2112.02026 [src] |
| BOSS DR12 | target selection and LSS catalogues with randoms; MKSAMPLE code | arXiv:1509.06529 [src] |
| DESI EDR | Survey Validation spectra: 466,447 MWS, 428,758 BGS, 227,318 LRG, 437,664 ELG, 76,079 QSO targets, plus 137,148 secondary; LSS catalogues; intermediate products | arXiv:2306.06308 [src] |
| DESI DR1 | first 13 months of the main survey plus SV reprocessed: 18.7M confident redshifts (13.1M galaxies, 1.6M quasars, 4M stars); spectra, redshift catalogues, LSS catalogues, VACs | arXiv:2503.14745 [src] |
| DES DR2 | ~5000 deg² grizY; 691M objects in 10,169 co-add tiles from 76,217 exposures; median PSF FWHM g 1.11″ to z 0.83″; uniformity < 3 mmag vs Gaia; astrometric precision ~27 mas; S/N = 10 depth i = 23.8 | arXiv:2101.05765 [src] |
| DES Y3 Gold | ~390M objects; maps of footprint, masks, depth, conditions, foregrounds | arXiv:2011.03407 [src] |
| DES Y6 Gold | 669M objects; i ≈ 23.4 at S/N ~10; uniformity < 2 mmag; star–galaxy efficiency 98.6%, contamination 0.8% at 17.5 < i < 22.5; 448M galaxies after cuts; survey-property maps | Bechtol et al. 2025, arXiv:2501.05739 [src] |
| HSC-SSP PDR3 | 670 deg² at full depth (~26 mag, 5σ), 1470 deg² including partial; small-scale sky subtraction before detection cut false detections | Aihara et al. 2022, arXiv:2108.13045 [src] |
| KiDS DR4 | 1006 deg² of ugri tiles with weight maps, masks, nine-band forced photometry with VIKING, photo-z | arXiv:1902.11265 [src] |
| KiDS DR5 | 1347 deg², i band re-observed (+0.4 mag); 126,085 sources with spectroscopic and photometric redshifts for calibration | arXiv:2503.19439 [src] |
| Legacy Surveys | g, r, z over a ~14,000 deg² design footprint plus WISE forced photometry; Tractor catalogue; software released with data | arXiv:1804.08657 [src] |
| Euclid Q1 | 63.1 deg² at wide-survey depth; ~30M objects; ~3M validated red-grism spectra; early pipeline versions; masks | arXiv:2503.15302, arXiv:2503.15307 [src] |
| Rubin DP1 | 1792 LSSTComCam exposures over 48 nights; ~15 deg² in seven fields; images, co-adds, difference images, catalogues, survey-property maps; ~2.3M objects; ~3.5 TB on the Rubin Science Platform | arXiv:2603.23786 [src] |
| Planck NPIPE | frequency maps, raw and processed TOD, software, 600 end-to-end simulations | arXiv:2007.04997 [src] |
| ACT DR6 | maps at 98, 150, 220 GHz over 19,000 deg², null-test splits, depth-1 maps, matched-filtered and ILC maps; on LAMBDA | arXiv:2503.14451 [src] |
| SPT-3G D1 | Main-field maps at 95, 150, 220 GHz from 2019–2020 over 4% of the sky, public | arXiv:2603.20163 [src] |

## 5. Public pipeline software
<!-- key: public-pipeline-software -->

Versions, maintenance and installation are in `cosmo-software-ecosystem`.

| Stage | Codes (reference) |
|---|---|
| Targeting, fibre assignment, LSS catalogues | desitarget (arXiv:2208.08518); altMTL realisations (arXiv:2404.03006); DESI LSS pipeline (arXiv:2405.16593); MKSAMPLE (arXiv:1509.06529); mangle (arXiv:0711.4352) |
| Spectroscopic reduction and redshifts | DESI spectroscopic pipeline and Redrock (arXiv:2209.14482); redmonster (arXiv:1607.02432); autoz (arXiv:1404.2626); QuasarNET (arXiv:1808.09955); Euclid SIR and SPE (arXiv:2503.15307, arXiv:2503.15308) |
| Imaging reduction | LSST Science Pipelines (arXiv:1512.07914, arXiv:2603.23786); HSC pipeline (arXiv:1705.06766); DESDM (arXiv:1801.03177); Astro-WISE and THELI (arXiv:1902.11265); Euclid VIS (arXiv:2503.15303) |
| Detection, deblending, photometry | SExtractor (doi:10.1051/aas:1996164); SCARLET (arXiv:1802.10157); Tractor (arXiv:1804.08657); DeepDISC (arXiv:2610.10986); BLISS (arXiv:2601.03422) |
| PSF | Piff (arXiv:2011.03409, arXiv:2501.05781); PSFEx as used in HSC (arXiv:1705.06766) |
| Imaging-systematics weights | SYSNet (arXiv:1907.11355) |
| Source injection | Balrog (arXiv:1507.08336, arXiv:2012.12825, arXiv:2501.05683); Obiwan (arXiv:2007.08992) |
| CMB map-making | Madam (arXiv:astro-ph/0412517); SRoll2 (arXiv:1901.11386); NPIPE (arXiv:2007.04997); MAPPRAISER (arXiv:2405.10239); POMME in FURAX (arXiv:2606.31720) |

## 6. Pipelines being built for the next data
<!-- key: pipelines-being-built-for-the-next-data -->

- **Rubin LSST.** Designed (**forecast**) to image ~18,000 deg² about 800 times, with
  ~15 TB per night, a real-time alert stream and eleven data releases over
  ten years (Jurić et al. 2017, arXiv:1512.07914) [src]. DP1 is the first
  test of the full science pipelines on sky; global astrometric calibration
  brought only modest gains there because of the short baseline and small
  ComCam distortions, and is expected to matter more for LSSTCam
  [src: arXiv:2603.23786, Sect. V.3]. Piff is the planned default PSF code
  (arXiv:2501.05781) [src].
- **Euclid.** Q1 used early versions of every processing function, with
  improvements planned for DR1 and later releases, and the reliability of
  automated NISP redshifts is the stated main challenge, harder when DR1
  deepens the extracted sample [src: arXiv:2503.15302, Sect. 9].
- **4MOST CRS.** Bright galaxies, LRGs, ELGs and quasars, about 8 million
  objects over 0.15 < z < 3.5 in the design (**forecast**; Richard et al. 2019,
  arXiv:1903.02474) [src]; target catalogues validated on Legacy Surveys
  DR10.1 for 5.4 million redshifts over ~5700 deg² (arXiv:2510.02449) [src].
- **PFS.** 2400 fibres over 380–1260 nm; the cosmology survey targets ELGs at
  0.8 < z < 2.4 in the design (**forecast**; Takada et al. 2014, arXiv:1206.0737) [src],
  in the regime of more targets than fibres (arXiv:1912.06583) [src].
- **DESI second phase.** Lyman-break galaxies at z ~ 2–4.5 with
  network-based decontamination (arXiv:2608.10080) [src].
- **Simons Observatory.** An automated scheduler turns scan strategies into
  observing scripts and a workflow system runs daily reduction on site (Guan
  et al. 2024, arXiv:2406.10905) [src]; for the small-aperture telescopes, a
  transfer-function method for power spectra from filtered maps recovers
  unbiased parameters, including r, on simulated first-year data
  (Hervías-Caimapo et al. 2025, arXiv:2502.00946) [src].

## Not verified
<!-- key: not-verified -->

- Current Legacy Surveys release area (DR10, DR11) not read here; see `cosmo-surveys-facilities`.
- SDSS-V, WEAVE and MOONS reduction pipelines not read.
- Euclid DR1 content and date: not in this skill.
