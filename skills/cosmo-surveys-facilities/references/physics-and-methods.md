# Surveys and facilities — how a survey is specified and compared

Scope: the quantities used to specify and compare cosmological surveys (etendue, figure of merit, number density and nP, depth, completeness, fibre assignment, cadence), with the reference papers and the conventions that make published numbers non-comparable.
Snapshot: 2026-10-07

Flags as in `surveys-and-data.md`: `[src]` read this session in the cited
paper or page; `[sec: GC|WL|CMB|SN|CL]` carried over from the named sibling
skill's `references/surveys-and-data.md`; `[der]` derived here, with the
assumption stated. Equations given without a flag are textbook definitions.
The estimators, likelihoods and theory models of each probe are in the probe
skills; this file is about the instrument and the survey design.

## 1. Etendue, multiplex and survey speed
<!-- key: etendue-multiplex-and-survey-speed -->

### 1.1 Imaging
<!-- key: imaging -->

The etendue is the product AΩ of collecting area and field of view. At fixed
image quality, sky background and throughput, the time needed to cover a
given area to a given point-source depth scales as 1/(AΩ). The quantity
ignores everything that differs most between ground and space: seeing, sky
brightness, wavelength, detector efficiency and duty cycle.

| Facility | Aperture used | Field | AΩ | Flag |
|---|---|---|---|---|
| Rubin (Simonyi) | 6.5 m effective (8.4 m primary) | 9.6 deg² | 319 m² deg² | inputs [src] arXiv:0805.2366; product [der] |
| ZTF (Palomar 48-inch) | 1.22 m | 47 deg² | 55 m² deg² | inputs [src] arXiv:1902.01932; product [der] |
| DECam on Blanco | 4 m | 2.2° diameter, 3.8 deg² | 48 m² deg² | inputs [src] arXiv:1504.02900; product [der] |
| CSST | 2 m | about 1.1 deg² | 3.5 m² deg² | inputs [src] arXiv:2507.04618; product [der] |
| Roman WFI | 2.4 m | 0.281 deg² | 1.3 m² deg² | inputs [src] arXiv:1902.05569; product [der] |

Assumption for every [der] product: unobstructed circular aperture of the
quoted diameter, A = π(D/2)². For Rubin the paper itself supplies the
effective diameter; with the full 8.4 m the product would be 532 m² deg²,
which is not the number to quote. Euclid VIS (0.54 deg², arXiv:2405.13492)
and NISP (0.57 deg², arXiv:2405.13493) are left out because the telescope
aperture was not read this session.

Three consequences that the table makes visible:

- Rubin's etendue is about six times that of DECam or ZTF [der], which is
  why it can revisit 18,000 deg² about 800 times in ten years
  (arXiv:0805.2366) [src].
- ZTF matches DECam in etendue with a telescope of one tenth the area [der]:
  it buys cadence, not depth. Its design paper states "more than an order of
  magnitude improvement in survey speed" over its predecessor
  (arXiv:1902.01932) [src].
- Space imagers have etendues one to two orders of magnitude below the
  ground surveys [der]. They compete on resolution (0.18″ for VIS
  [src], 0.074″ pixels for CSST [src]), on infrared background, and on
  stability of the point-spread function, none of which enter AΩ.

### 1.2 Multi-object spectroscopy
<!-- key: multi-object-spectroscopy -->

For fibre spectrographs the analogue is collecting area times the number of
fibres, with the fibre density on the sky deciding how many passes a target
class needs.

| Facility | Aperture | Field | Fibres | Fibres per deg² | A × N_fibre [m²] | Flag for inputs |
|---|---|---|---|---|---|---|
| SDSS-V | 2.5 m | — | 500 per site | — | 2.5 × 10³ | [src] arXiv:2507.06989 |
| WEAVE | 4.2 m | 2° diameter, 3.1 deg² | nearly 1000 | about 320 | 1.4 × 10⁴ | [src] arXiv:2212.03981 |
| 4MOST | 4 m class | 4.2 deg² | 2436 | 580 | 3.1 × 10⁴ | [src] arXiv:1903.02464, arXiv:2606.27882 |
| MOONS | 8 m class | 25′ diameter, 0.14 deg² | about 1000 | about 7300 | 5.0 × 10⁴ | [src] arXiv:2009.00628, arXiv:2009.00635 |
| DESI | 4 m | 3.2° diameter, 8.0 deg² | 5020 | 624 | 6.3 × 10⁴ | [sec: GC] arXiv:2205.10939 |
| PFS | 8.2 m | 1.25 deg² | 2386 | 1909 | 1.3 × 10⁵ | [sec: GC] arXiv:2606.14012 |
| Spec-S5 (**design**) | 6 m, two telescopes | — | 13,000 each | — | 3.7 × 10⁵ each | [sec: GC] arXiv:2608.07927 |
| MUST (**design**) | 6.5 m | about 5 deg² | more than 20,000 | 4000 | 6.6 × 10⁵ | [src] arXiv:2605.10102 |
| MSE (**design**, 2025) | 11.5 m | 1.5 deg² | more than 18,000 | 12,000 | 1.9 × 10⁶ | [src] arXiv:2503.15553 |
| WST (**design**) | 12 m class | 3 deg² | 20,000 | 6700 | 2.3 × 10⁶ | [src] arXiv:2403.05398, arXiv:2607.01150 |

The last two columns are [der] with the same unobstructed-aperture
assumption. They ignore throughput, fibre diameter, wavelength coverage,
spectral resolution, reconfiguration time and the fraction of time awarded
to cosmology, so they rank hardware, not surveys. What they show:

- A "Stage-V" facility in the sense used by the MUST and WST papers is one
  to two orders of magnitude above DESI in A × N_fibre [der].
- DESI's fibre density, 624 per deg² [der], equals the density of its LRG
  targets alone (624 per deg², arXiv:2404.03002) [sec: GC]. With BGS Bright
  at 854 per deg² and QSO at 310 per deg² [sec: GC], every tile is
  over-subscribed and completeness is built up by overlapping passes
  (Sect. 5).
- PFS and MOONS trade field for aperture: high fibre density on small
  fields suits deep, dense samples, not 14,000 deg² footprints.

### 1.3 Slitless spectroscopy
<!-- key: slitless-spectroscopy -->

Euclid NISP and the Roman grism take a spectrum of every source in the
field, so there is no multiplex number and no fibre assignment. The
specification is a line-flux limit and a spectral resolution: about
2 × 10⁻¹⁶ erg s⁻¹ cm⁻² at S/N = 3.5 and R ≥ 450 for NISP (arXiv:2405.13493)
[src]. The sample is defined after the fact by the detected line, which
moves the completeness problem from targeting to line identification
(`systematics.md`, Sect. 3). SPHEREx is the limiting case: R = 35–130
spectrophotometry of every pixel (arXiv:2511.02985) [sec: GC], giving
redshifts of low precision for a very large sample.

## 2. Dark Energy Task Force stages and the figure of merit
<!-- key: dark-energy-task-force-stages-and-the-figure-of -->

The staging vocabulary (Stage II, III, IV) and the dark-energy figure of
merit come from the Dark Energy Task Force report (Albrecht et al. 2006,
arXiv:astro-ph/0609591). The figure of merit is the reciprocal of the area
of the error ellipse in the (w0, wa) plane, up to a convention-dependent
constant; the report's abstract, which is all that was read this session,
does not restate the stage definitions or the normalisation. The
conventions in use and their conversion are treated in
`cosmo-dark-energy-modified-gravity` and `cosmo-statistics-inference`.

How the vocabulary is used in the facility papers read this session [src]:

- CSST calls itself "an upcoming Stage-IV sky survey telescope"
  (arXiv:2507.04618).
- MUST is presented as "the first Stage-V spectroscopic facility currently
  under construction" (arXiv:2605.10102); the Snowmass road map speaks of
  "DESI, DESI-II, Stage-5" (arXiv:2209.03585).
- The CHIME analysis-method paper quotes its forecast as a figure-of-merit
  gain: a medium-sized cylinder telescope "improves the DETF Figure of Merit
  by around 70% over Planck and Stage II experiments" (**forecast**; Shaw et
  al. 2015, arXiv:1401.2095).

Rules for comparing figures of merit:

1. A figure of merit is a property of a survey plus its priors plus its
   external data. The Euclid **forecast** of a (w0, wa) figure of merit above
   400 is for all primary probes combined (arXiv:2510.09153) [sec: WL]; a
   single-probe number from another paper is not comparable.
2. Check whether curvature and neutrino mass are free. Font-Ribera et al.
   2014 (arXiv:1308.4164) [src] show that BAO-only dark-energy constraints
   are "substantially degraded" once neutrino mass is free and that broadband
   power and lensing recover the loss.
3. Systematics floors are usually absent from the Fisher forecasts behind a
   figure of merit; the same paper says of itself that it does "not try to
   be especially innovative ... in careful treatments of potential systematic
   errors" [src].
4. A design figure of merit describes a survey that may not be executed as
   designed (Sect. 4 of `results.md`).

## 3. Number density, nP and effective volume
<!-- key: number-density-np-and-effective-volume -->

For a tracer of mean density n̄ and power spectrum P(k), the shot-noise to
sample-variance balance is set by n̄P. The Feldman–Kaiser–Peacock weight
w = 1/(1 + n̄P) minimises the variance of the power-spectrum estimate for
Gaussian fluctuations (Feldman et al. 1994, arXiv:astro-ph/9304022), and the
corresponding effective volume is

    V_eff(k) = ∫ [ n̄(r) P(k) / (1 + n̄(r) P(k)) ]² d³r .

Reading rules:

- n̄P ≈ 1 at the scale of interest is the usual design target; far above it
  the survey is sample-variance limited and extra fibres are better spent on
  area or redshift range; far below it the survey is shot-noise limited.
- n̄P must be quoted with the k and the P at which it is evaluated (BAO
  scale, with or without the bias and redshift-space boost).
- Distance errors from BAO follow a fitting formula in the survey volume,
  n̄P and a non-linear damping scale (Seo & Eisenstein 2007,
  arXiv:astro-ph/0701079) [src]; it is the standard quick forecast and it
  isolates the acoustic feature, excluding broadband information.
- Consistent Fisher projections for BOSS, eBOSS, HETDEX, DESI, Euclid and
  WFIRST are tabulated in arXiv:1308.4164 [src]; they are **forecasts** made
  in 2013 and the surveys were executed differently.

Worked example from the DESI papers. The Survey Validation paper projected
BAO precisions of 0.28% at z < 1.1, 0.39% at 1.1 < z < 1.9 and 0.46% at
1.9 < z < 3.5 for the full 14,000 deg² programme (**forecast**;
arXiv:2306.06307) [src]. The road-map paper states that DESI captures "a
significant fraction of the available linear modes up to z = 1.2"
(arXiv:2209.03585) [src]: beyond that redshift the gain comes from density
and redshift reach, which is the case made for DESI-II and the Stage-V
facilities.

Multi-tracer and intensity-mapping surveys change the accounting. A 21 cm
intensity map has no discrete-object shot noise in the galaxy-survey sense;
its noise is thermal and its limit is foreground removal (Sect. 8).

## 4. Imaging depth, effective source density and photometric redshifts
<!-- key: imaging-depth-effective-source-density-and -->

### 4.1 Depth is quoted in incompatible ways
<!-- key: depth-is-quoted-in-incompatible-ways -->

| Survey | Quoted depth | Convention | Source |
|---|---|---|---|
| DES DR2 | g 24.7, r 24.4, i 23.8, z 23.1, Y 21.7 | S/N = 10, 1.95″ diameter aperture, coadd | arXiv:2101.05765 [src] |
| UNIONS | u 23.7, g 24.5, r 24.2, i 23.8, z 23.3 | 10σ point source, 2″ aperture | arXiv:2503.13783 [src] |
| HSC-SSP Wide | r ≈ 26 | 5σ point source | arXiv:1704.05858 [src] |
| Pan-STARRS1 3π | g 23.3, r 23.2, i 23.1, z 22.3, y 21.4 | 5σ point source, stack | arXiv:1612.05560 [src] |
| Rubin | r ≈ 24.5 single visit, r ≈ 27.5 coadd | 5σ point source, **design** | arXiv:0805.2366 [src] |
| Euclid VIS | m_AB > 24.5 | S/N > 10, extended source, single broad band | arXiv:2405.13492 [src] |
| Euclid reference survey | 26.2 visible, 24.5 near-infrared | 5σ point source, pre-launch **design** | arXiv:2108.01201 [src] |
| CSST | g ≈ 26 | 5σ point source, **design** | arXiv:2507.04618 [src] |

A 5σ point-source limit and a 10σ extended-source limit in the same data
differ by more than a magnitude. The two Euclid rows describe the same
instrument: 26.2 and "> 24.5" are not in conflict. Never rank surveys by
depth without converting to one convention.

### 4.2 Effective source density
<!-- key: effective-source-density -->

For weak lensing the survey power is set by area, shape noise and the
effective number density n_eff of sources (Chang et al. 2013,
arXiv:1305.0793). That paper's **forecast** for LSST is n_eff ≈ 37 arcmin⁻²
before blending and masking and ≈ 31 arcmin⁻² after rejecting seriously
blended galaxies [src]. Delivered Stage-III values run from about 4.6 to 20
arcmin⁻² (DECADE 4.59, UNIONS 4.96, DES Y3 5.59, KiDS-1000 6.17, DES Y6
8.22, HSC Y3 19.9) [sec: WL]. Each survey uses its own n_eff definition, so
the column is indicative; `cosmo-weak-lensing` gives the definitions.

### 4.3 Uniformity and calibration as specifications
<!-- key: uniformity-and-calibration-as-specifications -->

- Relative photometric calibration from overlaps ("ubercalibration"): about
  1% in griz over 8500 deg² for SDSS (Padmanabhan et al. 2008,
  arXiv:astro-ph/0703454) [src].
- Forward global calibration with atmosphere and instrument models: 7 mmag
  uniformity over the 5000 deg² DES footprint, with chromatic corrections
  needed to go below a percent (Burke et al. 2018, arXiv:1706.01542) [src];
  DES DR2 reports better than 3 mmag uniformity against Gaia
  (arXiv:2101.05765) [src].
- Pan-STARRS1: 7–12 mmag systematic floor depending on band
  (arXiv:1612.05560) [src].
- Uniform depth by design: the Legacy Surveys adjust exposure times
  dynamically (arXiv:1804.08657) [src]; DESI and PFS do the same for
  spectroscopy with an "effective exposure time" (arXiv:2306.06309;
  arXiv:2606.14012) [src].

Photometric-redshift requirements (for example |Δ⟨z⟩| ≤ 0.002(1+z) per bin
for Euclid) belong to `cosmo-weak-lensing`.

## 5. Completeness and fibre assignment
<!-- key: completeness-and-fibre-assignment -->

Three completeness factors multiply, and papers do not always say which one
they quote: the fraction of the parent target list given a fibre
(assignment completeness), the fraction of observed targets with a good
redshift (redshift success), and the fraction of the footprint observed to
nominal depth. DESI DR2 values per tracer show the range: assignment
completeness 75.5% (BGS), 82.6% (LRG), 53.7% (ELG), 93.6% (QSO); redshift
success 98.8%, 99.0%, 73.9%, 68.0% (arXiv:2503.14738) [sec: GC].

Hardware sets the pattern of what is missed:

- Plates with drilled holes (SDSS, BOSS, eBOSS): a minimum separation between
  neighbouring fibres, the "close-pair issue" (Bianchi & Percival 2017,
  arXiv:1703.02070) [src].
- Robotic positioners with a finite patrol radius (DESI): each fibre reaches
  only a small disc, so the constraint is the number of targets per patrol
  area (Lasker et al. 2024, arXiv:2404.03006) [src].
- Tilting spines (4MOST): 2436 spines positioned to about 0.27″ RMS on sky
  after six months of operation (arXiv:2606.27882) [src].

Because missed targets are clustered, assignment incompleteness suppresses
the measured clustering in a scale-dependent way. In a DESI BGS mock the
completeness is above 95% in low-density regions and below 10% in the
centres of massive clusters (Smith et al. 2019, arXiv:1809.07355) [src].
The correction now standard is pairwise-inverse-probability (PIP)
weighting: rerun the assignment many times, estimate for each pair the
probability of being observed, and upweight (arXiv:1703.02070) [src]. It is
unbiased only if every pair has a non-zero probability of being observed,
which is why DESI randomly promotes a fraction of low-priority targets
(arXiv:1809.07355) [src]. DESI implements it with alternate merged target
ledgers (arXiv:2404.03006) [src]; for DR1, PIP weights with angular
upweighting recover the true clustering in both Fourier and configuration
space, a fast emulator of fibre assignment supplies the covariance mocks,
and a model-stage alternative removes small angular separations ("θ-cut")
(Bianchi et al. 2024, arXiv:2411.12025) [src]. Analysis detail:
`cosmo-galaxy-clustering`.

Survey scheduling is part of the specification. DESI plans each night in
the afternoon, selects fields automatically, judges completeness in real
time and updates the target list the next morning, over 15,000 fields
(arXiv:2306.06309) [src]. PFS allocates "fibre hours" and co-observes
several programmes in one exposure (arXiv:2606.14012) [src].

## 6. Cadence and time-domain strategy
<!-- key: cadence-and-time-domain-strategy -->

| Survey | Cadence as specified | Source |
|---|---|---|
| ATLAS | whole visible sky every two days | arXiv:1802.00879 [src] |
| ZTF | 47 deg² per exposure, 8 s readout | arXiv:1902.01932 [src] |
| YSE | about 750 deg² every three days in griz (2020) | arXiv:2010.09724 [src] |
| Rubin | pairs of 15 s exposures, two visits per pointing per night; 10,000 deg² in one filter in three nights (**design**) | arXiv:0805.2366 [src] |
| Roman HLTDS | filter subsets every five days | [sec: SN] |
| Euclid | step-and-stare, four dithered frames per wide-survey pointing | arXiv:2108.01201 [src] |
| SPHEREx | four all-sky passes in two years | [sec: GC] |
| eROSITA | one all-sky pass every six months | arXiv:2010.03477 [src] |
| CHIME | drift scan, three quarters of the sky every day | arXiv:2201.07869 [src] |

For a supernova survey the specification is the joint distribution of
filter, depth and revisit time, plus the low-redshift anchor it will be
combined with (`cosmo-supernovae`). For Rubin, the cosmological return was
evaluated on more than 100 simulated strategies; the footprint, whether the
repeat visits of a night are taken in different filters, and the regularity
of the cadence each change it "profoundly" (Lochner et al. 2022,
arXiv:2104.05676) [src]. A cadence quoted from a design paper is a
requirement, not what the scheduler delivered.

## 7. CMB sensitivity: map depth, resolution and sky fraction
<!-- key: cmb-sensitivity-map-depth-resolution-and-sky -->

A CMB survey is specified by map depth (μK-arcmin, in temperature or in
Q/U), beam width, sky fraction and frequency coverage. With white noise of
weight w per solid angle and a Gaussian beam of width σ_b, the noise power
is N_ℓ = w⁻¹ exp(ℓ² σ_b²) and the error on a band power is

    ΔC_ℓ = sqrt( 2 / ((2ℓ + 1) f_sky) ) (C_ℓ + N_ℓ) .

Knox 1995 (arXiv:astro-ph/9504054) [src] drew the design conclusion that
still holds: for fixed detector sensitivity and observing time "a smaller
beam provides significantly more information than a larger beam", and the
uncertainties on n_s and r scale roughly with the beam size.

Depths of the current maps, to fix orders of magnitude [sec: CMB]: ACT DR6
has a median of 10 μK-arcmin over 19,000 deg²; SPT-3G D1 reaches 4.4
μK-arcmin in intensity at 150 GHz over 1500 deg²; BK18 reaches 2.8
μK-arcmin in Q/U at 95 and 150 GHz over about 400–600 deg². Depth and area
trade at fixed detector-years; the sample-variance term favours area for
lensing and damping-tail science and depth on a small clean patch for
primordial B modes. Hence the split into large-aperture telescopes (6 m and
10 m) and small-aperture refractors (0.5 m class) at the Simons Observatory
and the South Pole [sec: CMB]. Likelihood-level detail: `cosmo-cmb`.

## 8. Radio and gravitational-wave figures of merit
<!-- key: radio-and-gravitational-wave-figures-of-merit -->

**21 cm intensity mapping.** Two architectures are in use. Compact
interferometers with redundant baselines (CHIME, CHORD, HIRAX) measure
Fourier modes directly; arrays of dishes used in auto-correlation
("single-dish" mode: MeerKLASS, SKA-Mid) reach the largest angular scales
over thousands of square degrees (arXiv:2606.25955) [src]. The specification
that matters is not thermal sensitivity but the calibration accuracy needed
to separate foregrounds brighter than the signal by orders of magnitude. For
a CHIME-like cylinder analysed with the m-mode formalism, unbiased power
spectra require each feed's beam width known to 0.1% and amplifier gains
known to 1% within each minute, and foreground cleaning leaves only
k_∥ < 0.02 h/Mpc inaccessible (**forecast** on simulations;
arXiv:1401.2095) [src]. Treatment: `cosmo-reionization-21cm`.

**HI galaxy and continuum surveys.** Specified like optical surveys:
sensitivity per channel and resolution (WALLABY: about 1.6 mJy per beam per
4 km/s channel at about 30″, arXiv:2002.07311 [src]) or continuum rms
(DSA-2000 **design**: 500 nJy per beam, arXiv:1907.07648 [src]).

**Gravitational-wave detectors.** The quantities to quote are the number of
candidates above a stated threshold and the localisation, not a depth. The
catalogue grew from 90 candidates (GWTC-3.0) to 218 (GWTC-4.0, threshold
p_astro ≥ 0.5; arXiv:2508.18082) [src], with 267 mergers in the GWTC-5.0
population analysis (arXiv:2605.27226) [src]. For cosmology what counts is
the number of events with a redshift, by counterpart or statistically
(`cosmo-multimessenger`).

## Not verified
<!-- key: not-verified -->

- The DETF stage definitions and the exact normalisation of the DETF figure
  of merit (only the abstract of arXiv:astro-ph/0609591 was read).
- Telescope obstruction and throughput for every entry of the etendue and
  multiplex tables; the Euclid and HSC apertures and the HSC field of view
  were not read, so both are absent from Table 1.1.
- The SDSS fibre-collision angular scales (plate hardware limits) and the
  DESI patrol radius in millimetres or arcseconds.
- The third n_eff value of arXiv:1305.0793 (after masking), cut off in the
  abstract text retrieved.
- Rubin's delivered cadence since 30 June 2026, and the adopted baseline
  survey strategy version.
