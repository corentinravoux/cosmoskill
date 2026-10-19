# Cepheid period–luminosity calibration — cosmo-distance-ladder-h0 dossier

Scope: how Cepheid magnitudes in SN Ia hosts are produced and cleaned before
the global ladder fit (discovery, NIR photometry and background, period and
colour cuts, outlier rejection, metallicity assignment, JWST epochs and
phase), and how the choices of clipping, PL form, period matching, colour
treatment and sample sub-selection move H0, with the tests that validate
each step.
Snapshot: 2026-10-19.
From: Chen & Wang 2026, Sects. 3.1 and 3.4; Verde et al. 2023, Sects. 2.1
and 2.4.2; Freedman & Madore 2023, Sects. 3 and 11; SH0ES programme
(arXiv:2112.04510).

Already in L2: the ladder equations, the design matrix and the covariance
terms (SH0ES Eqs. 1–8), the Wesenheit definition and R, the 2022 sample and
best-fit values in `physics-and-methods.md#formalism-sh0es`; crowding,
metallicity, Gaia and dust systematics with sizes in
`systematics.md#cepheid-crowding-and-blending`,
`systematics.md#cepheid-metallicity-dependence`,
`systematics.md#extinction-law-and-the-wesenheit-colour-term`; the SH0ES
budget in `systematics.md#error-budgets-term-by-term`. Anchors are in
`physics-and-methods.md#geometric-anchors`.

Notation. P: pulsation period in days; m^W_H: NIR Wesenheit magnitude
(F160W, or F150W with JWST, minus R times an optical colour); Z_W: the
metallicity coefficient in mag/dex; [O/H]: oxygen abundance relative to
solar, 12 + log(O/H) = 8.69 for the Sun; bkgd: the change of a Cepheid's
magnitude from adding the mean unresolved background measured with
artificial stars; SD: standard deviation of PL residuals.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Discover and validate Cepheids in the optical
<!-- key: step-1-discover-and-validate-cepheids-in-the -->

Discovery needs ~11–12 epochs in a visual band, with non-redundant
spacings over ~60–100 days, to identify the light curves and measure
periods; image subtraction finds more candidates but they are more blended,
because blends suppress amplitudes and detection [src: arXiv:2112.04510,
Sect. 3.1]. The 2022 sample used ~1050 HST orbits (~150 WFC3-NIR, ~700
optical), all suitable SNe Ia at z < 0.011 (40) plus two beyond [src:
arXiv:2112.04510, Sect. 3.1]. Photometry uses the DAO suite on the
optical frames; NIR positions are transferred from the optical images to
< 0.03 pixel [src: arXiv:2112.04510, Sect. 3.1].

Validation without per-star demands: candidates must have amplitudes of
0.2–1 mag, and the binned composite light curves of ~60,000 measurements
must reproduce the Hertzsprung progression (resonance bump on the
descending branch at P = 5–9 d, symmetric at 9–14 d, on the rising branch
at 14–19 d), which identifies classical fundamental-mode Cepheids [src:
arXiv:2112.04510, Sect. 3.2].

### Step 2. NIR photometry and the background
<!-- key: step-2-nir-photometry-and-the-background -->

- PSF photometry at the optical positions, with an empirical PSF from the
  star P330E and other NIR sources fitted simultaneously [src:
  arXiv:2112.04510, Sect. 3.3].
- Sky annulus 0.24"–0.8" (was 0.96"–1.44"), with a 0.008 mag PSF-wing
  offset measured on bright stars and corrected [src: arXiv:2112.04510,
  Sect. 3.4, item 1].
- 100 artificial stars per Cepheid within 2.4", at the magnitude predicted
  by the period and a trial PL; the recovered offset refines the
  background; the PL is refitted and the cycle repeated to convergence.
  Earlier iterations had "not fully converged" [src: arXiv:2112.04510,
  Sects. 3.3, 3.4 item 2].
- The artificial-star distributions are Gaussian in magnitude out to
  3 sigma; mean minus median is 0.03 sigma per host and 0.01 sigma (4 mmag)
  averaged over hosts, with no trend of skewness with distance — the stated
  justification for Gaussian statistics in magnitude [src:
  arXiv:2112.04510, Sect. 3.3].
- "Associated flux" of unresolved host clusters, ~7 mmag beyond a few Mpc
  (measured in M31), is added to the background [src: arXiv:2112.04510,
  Sect. 3.3].
- New count-rate-nonlinearity calibration of WFC3/NIR, applied between
  anchor Cepheids and the background level of SN-host Cepheids [src:
  arXiv:2112.04510, Sect. 3.4, item 4].
- Periods are corrected to the rest frame for (1 + z) time dilation [src:
  arXiv:2112.04510, Sect. 3.4, item 6].
- M101 Cepheids with P > 35 d are dropped: the 2006 baseline was too short
  for reliable periods (about 10% of the earlier sample) [src:
  arXiv:2112.04510, Sect. 3.4, item 5].

The 20% background floor that becomes the within-host covariance is
SH0ES Eq. 8 (`systematics.md#cepheid-crowding-and-blending`).

### Step 3. Cut the sample
<!-- key: step-3-cut-the-sample -->

| Cut | Rule | Stated reason | Place read |
|---|---|---|---|
| Period completeness | only periods above each host's detection-completeness limit | avoid a magnitude bias | arXiv:2112.04510, Sect. 3.4 |
| Period range | 5 < P < 120 d, one common slope | host slopes agree within ~2 sigma at −3.27 to −3.30 mag/dex | arXiv:2112.04510, Sect. 4.6 |
| Colour | F814W − F160W within 0.8 mag of the host median | removes blends with sources of different colour (red giants, blue supergiants, clusters); distance- and period-independent, insensitive to reddening | arXiv:2112.04510, Sect. 6.1 |
| Outliers | iteratively remove the single largest residual from the global fit above 3.3 sigma (Chauvenet), until none remain | fully blended yellow supergiants and misidentified objects are expected | arXiv:2112.04510, Sect. 6.1 |

Sizes after cuts [src: arXiv:2112.04510, Table 3]: SN hosts 2680
Cepheids in the field of view, 2173 measured within the colour and period
limits, 2150 after rejection (1.2% rejected), mean period 36.5 d, mean
[O/H] −0.01; NGC 4258 555 / 451 / 443, mean period 14.4 d; LMC 339 fitted
(69 HST, 270 ground), SMC 143, M31 55; 3129 fitted in total.

### Step 4. Assign a metallicity to each Cepheid
<!-- key: step-4-assign-a-metallicity-to-each-cepheid -->

1. Measure radial gradients of the strong-line ratio R23 in H II regions of
   each host (Keck LRIS) and give each Cepheid the value of the linear fit
   at its galactocentric radius [src: arXiv:2112.04510, Sect. 3.5].
2. Convert R23 to 12 + log(O/H) with the mean of nine post-2004
   calibrations (third-order transformations derived from SDSS spectra),
   which lowers the older Z94 scale by 0.28 dex on average and flattens
   gradients slightly [src: arXiv:2112.04510, App. C].
3. Carry the scale uncertainty as a covariance between Cepheids i and j:
   C = Z_W^2 ([O/H]_i,avg − [O/H]_i,PP04)([O/H]_j,avg − [O/H]_j,PP04)
   (SH0ES Eq. 9), iterated so that Z_W matches the global fit; the
   average-minus-PP04 difference is ~0.05 dex, rising to 0.1 dex at
   12 + log(O/H) = 8.8 and 0.15 dex at 9.0 [src: arXiv:2112.04510,
   Sect. 3.5, App. C].
4. Use direct stellar spectroscopy for MW, LMC and SMC Cepheids. The tie
   between the two systems is tested in the MW: 219 Cepheids give
   12 + log(O/H) = 9.303 − 0.056 R_GC (dex/kpc), and PP04 H II regions
   match it to 0.035 ± 0.06 dex [src: arXiv:2112.04510, App. C].

Why PP04 is the comparison system: it is known to match extragalactic
stellar abundances [src: arXiv:2112.04510, Sect. 3.5]. Why the term
barely moves H0: SN-host metallicities span the same range as the anchors,
so the term "does not move the SN hosts with respect to the mean of the
anchors"; dropping it (Fit 29) raises H0 by 0.3 [src: arXiv:2112.04510,
Sect. 6.6]. NGC 4258 hosts and SN hosts share one strong-line scale, so
calibration differences cancel in that comparison [src: arXiv:2112.04510,
App. C].

### Step 5. JWST Cepheids
<!-- key: step-5-jwst-cepheids -->

[src: arXiv:2401.04773, Sects. II, II.1, III.1, III.3]

- Two epochs 15–16 days apart in F090W, F150W, F277W; one short-wavelength
  module on the host, the other on a halo field. JWST wavefront monitoring
  bounds PSF-core changes between epochs below 0.005 mag.
- DOLPHOT with its NIRCam module; Cepheids matched to the HST optical
  lists within 0.7 SW pixel (0.02"), typically 0.01".
- Quality: DOLPHOT chi^2 below 1.4 per degree of freedom, allowed to rise
  linearly to 1.7 with log P because bright long-period Cepheids expose PSF
  imperfections (removes ~7%); colour 0.3 < F090W − F150W < 1.15, i.e.
  0.5 < V − I < 1.7 (removes ~5%, mostly blends with red giants); the range
  is shifted redward for a host with E(V − I) = 0.21.
- 200 artificial stars bracketing the Cepheid magnitudes; mean crowding
  corrections 0.04, 0.07, 0.09 mag in F090W, F150W, F277W, about seven
  times smaller than HST F160W.
- Wesenheit systems: baseline F150W − 0.41 (F555W − F814W), keeping the
  HST optical colour; JWST-only F150W − 0.72 (F090W − F150W) and F277W −
  0.30 (F090W − F150W); R from Fitzpatrick with R_V = 3.3.
- PL slope fixed at −3.25 (JWST mean −3.21 ± 0.03, HST −3.26 ± 0.05),
  0.05 mag/dex propagated, with −3.20 and −3.30 as variants.
- Phase: the magnitudes "are phase corrected" (their Table 2 note); the
  epoch-to-epoch difference, compared with template light curves,
  constrains the phase (their Fig. 5).

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Outlier rejection
<!-- key: outlier-rejection -->

Fits 2–9 of SH0ES 2022 test global rejection (all objects above threshold
at once), rejection per host PL, 3 sigma or 5 sigma thresholds, and none;
their median H0 is 0.2 higher than the baseline; global rejection is within
0.15 and is used for most variants for speed [src: arXiv:2112.04510,
Sect. 6.1]. With few or no rejections (Fits 6, 7, 9) chi^2/dof exceeds
1.07, which for this number of degrees of freedom is a 3 sigma excess, and
the fits are judged "not good" [src: arXiv:2112.04510, Sect. 6.1].
JWST: without clipping SD rises from 0.178 to 0.218 mag and chi^2_nu from
1.0 to 1.7, while JWST − HST moves from −0.011 to 0.017 mag [src:
arXiv:2401.04773, Table 4].

### Single slope, broken slope or matched periods
<!-- key: single-slope-broken-slope-or-matched-periods -->

SH0ES: mean slopes below and above 10 d are −3.33 ± 0.02 and −3.21 ± 0.06
(1.8 sigma), the LMC and M31 change in opposite directions, and formal slope
errors are underestimated by 10% (35% in the LMC) because of uneven period
sampling; a single slope is kept with the break as a variant [src:
arXiv:2112.04510, Sect. 4.6].

A 2024 reanalysis (Högås & Mörtsell) finds host Cepheids with
log P ≳ 0.9 give lower H0 than shorter-period ones, and shorter host
periods, closer to the anchors' (mean 36.5 d in hosts against 13.3 d in
the Magellanic Clouds [src: arXiv:2112.04510, Table 3]), give lower H0
[src: arXiv:2412.07840, Sect. VI.1]. Two remedies, each with its cost
[src: arXiv:2412.07840, Sects. VI.2, VI.3]:

| Remedy | Result | Cost |
|---|---|---|
| Resample anchors and hosts, without replacement, to the product of their period histograms, 10^4 times | Delta H0 = −0.49 (−0.20 to −0.63 for 3 to 12 bins); 72.18 ± 1.76 | ~700 Cepheids kept of ~3200; error 1.41 plus 1.05 from resampling |
| Two breaks fitted at log P = 0.465 (+0.015/−0.354) and 0.909 (+0.020/−0.009) | Delta chi^2 = 28, p = 0.0004 by simulation; Delta AIC = −20 but Delta BIC = +5; Delta H0 = −0.32; 72.35 ± 0.91 | slopes −3.257, −3.347, −3.236 mag/dex; bimodal first break; mode at 71.62 |

Both include the authors' Milky Way recalibration; the total shift from
the four-anchor SH0ES value is −0.82 for the broken PL [src:
arXiv:2412.07840, Sect. VI.3]. Their reference is the four-anchor SH0ES
value, 73.17 ± 0.86, from ~3200 Cepheids [src: arXiv:2412.07840,
abstract].

### Universal colour term or per-host colour–luminosity relations
<!-- key: universal-colour-term-or-per-host-colour -->

SH0ES fixes R in all hosts and warns that varying R between galaxies
without first subtracting the intrinsic colour turns the
colour–luminosity relation of the instability strip (slope ~0.6) into a
spurious luminosity change of the candle [src: arXiv:2112.04510, Sect. 3.4
and its footnote]. A data-driven alternative fits a colour–luminosity
relation per host and anchor on the 2016 data: 73.2 ± 1.3 with Wesenheit
magnitudes, 73.9 ± 1.8 with an extinction law per galaxy, but then the
single-anchor values range from 68.1 ± 3.5 to 76.7 ± 2.0 and the Milky Way
anchor is 2.1 to 3.1 sigma from NGC 4258 and the LMC [src:
arXiv:2105.11461, abstract].

### Sub-selecting "uncrowded" Cepheids
<!-- key: sub-selecting-uncrowded-cepheids -->

The CCHP proposed selecting the Cepheids that look least crowded at JWST
resolution, for NGC 7250 [src: arXiv:2401.04773, Sect. III.3]. Splitting
the SH0ES JWST sample at the median DOLPHOT crowding parameter gives SD
0.165 against 0.201 mag but only 0.015 ± 0.053 mag difference in distance;
SH0ES argues that selecting on appearance admits superposed blends that
look isolated, so any sub-selection must also be applied to the
artificial stars [src: arXiv:2401.04773, Sect. III.3, Table 4].

### Photometry package in disc fields
<!-- key: photometry-package-in-disc-fields -->

CCHP reports that in the disc fields where Cepheids live, DAOPHOT and
DOLPHOT give "significant photometric differences that require further
investigation", absent in TRGB halo fields, and defers its JWST Cepheid
H0 [src: arXiv:2408.06153, App. B]. SH0ES validates its PSF photometry
against aperture photometry to sigma ≈ 0.02 mag [src: arXiv:2112.04510,
Sect. 3.3]. No CCHP Cepheid H0 was found (see
`open-questions.md#is-the-local-ladder-value-73-or-70`).

### Phase information on JWST
<!-- key: phase-information-on-jwst -->

One epoch gives SD = 0.224 mag; two phase-corrected epochs 0.178 mag plus
~100 single-epoch Cepheids, worth a 70% larger sample; with perfect
photometry, one random phase gives ~0.15 mag, two ~0.11 and two
phase-corrected ~0.075 mag [src: arXiv:2401.04773, Sect. III.3]. Dropping
the phase correction changes JWST − HST by 0.004 mag [der: −0.007 against
−0.011] [src: arXiv:2401.04773, Table 4].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Optical discovery cadence | 11–12 epochs over 60–100 d | SH0ES HST | arXiv:2112.04510 | Sect. 3.1 |
| Artificial stars | 100 per Cepheid within 2.4" (HST); 200 bracketing the Cepheid magnitudes (JWST) | SH0ES | arXiv:2112.04510; arXiv:2401.04773 | Sect. 3.3, Fig. 7; Sect. II.1 |
| Background floor as covariance | 0.03–0.06 mag within a host | SH0ES | arXiv:2112.04510 | Sect. 3.4 |
| Inner vs outer NGC 4258 | backgrounds differ by 0.45 mag, intercepts by 0.01 mag (sigma ≈ 0.05) | SH0ES | arXiv:2112.04510 | Sect. 3.3, Fig. 8 |
| Fit residuals against background | 0.010 ± 0.014 mag per mag | SH0ES | arXiv:2112.04510 | Sect. 3.3 |
| Amplitude test of background | < 0.03 mag | SH0ES (cited) | arXiv:2112.04510 | Sect. 3.3 |
| Change of F160W photometry vs 2016 | 63% of Cepheids fainter | SH0ES | arXiv:2112.04510 | Sect. 3.4 |
| Rejected outliers | 1.2% at 3.3 sigma | SH0ES | arXiv:2112.04510 | Sect. 6.1, Table 3 |
| LMC PL slope | −3.284 ± 0.017 mag/dex | SH0ES | arXiv:2112.04510 | Sect. 4.6 |
| Metallicity scale offset (avg − PP04) | ~0.05 dex | SH0ES | arXiv:2112.04510 | Sect. 3.5 |
| Mean [O/H]: SN hosts, NGC 4258, LMC, SMC | −0.01, −0.10, −0.29, −0.72 | SH0ES | arXiv:2112.04510 | Table 3 |
| JWST baseline sample | 938 Cepheids, SD 0.178, JWST − HST −0.011 ± 0.032 mag | SH0ES JWST | arXiv:2401.04773 | Table 4 |
| JWST P > 15 d only | 870 Cepheids, −0.020 ± 0.043 mag | SH0ES JWST | arXiv:2401.04773 | Table 4 |
| JWST without / doubled metallicity term | −0.005 / −0.016 mag | SH0ES JWST | arXiv:2401.04773 | Table 4 |
| CCHP M_B against mu, 42 SH0ES calibrators | slope 0.082 ± 0.023 (3 sigma) | CCHP on SH0ES data | arXiv:2408.06153 | App. B |
| Share of SH0ES hosts beyond 20 Mpc | 60% | CCHP | arXiv:2408.06153 | App. B |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Blends with stars of another colour.** Show up as colour outliers;
  caught by the 0.8 mag colour window (HST) or the F090W − F150W window
  (JWST) [src: arXiv:2112.04510, Sect. 6.1; arXiv:2401.04773, Sect. II].
- **Misidentified variables.** Caught statistically by the Hertzsprung
  progression in binned light curves [src: arXiv:2112.04510, Sect. 3.2].
- **Incompleteness at short periods.** Bright-biased PL intercepts; cut at
  each host's completeness period [src: arXiv:2112.04510, Sect. 3.4].
- **Aliased long periods.** Short monitoring baselines give wrong periods
  above ~1.2 times the baseline; drop them (M101 P > 35 d) [src:
  arXiv:2112.04510, Sect. 3.4].
- **Background misestimate.** Tests: inner vs outer fields of one galaxy;
  regression of fit residuals on background; NIR amplitudes against MW
  Cepheids; aperture photometry; JWST against HST for the same stars
  [src: arXiv:2112.04510, Sect. 3.3; arXiv:2401.04773, Table 4].
- **Unconverged artificial-star iterations.** Trial PL and corrections
  must be iterated to convergence; the 2016 reduction had not converged
  in some hosts [src: arXiv:2112.04510, Sect. 3.4].
- **Distance-dependent bias.** Test: M_B against host distance (CCHP finds
  a 3 sigma slope on HST data) and JWST − HST against distance (SH0ES finds
  none over 19 hosts, `systematics.md#cepheid-crowding-and-blending`)
  [src: arXiv:2408.06153, App. B].
- **Anchor–host period mismatch.** Test: H0 in host-period bins, matched
  resampling, broken PL with a simulated null [src: arXiv:2412.07840,
  Sect. VI].
- **Per-host extinction laws without intrinsic colours.** Spreads single-
  anchor H0 values; check the anchors' mutual consistency [src:
  arXiv:2105.11461, abstract; arXiv:2112.04510, Sect. 3.4].
- **Too few rejections.** chi^2/dof above 1.07 flags an unacceptable fit
  at this sample size [src: arXiv:2112.04510, Sect. 6.1].

## Reading list
<!-- key: reading-list -->

- Riess et al. 2022, arXiv:2112.04510 (method and application): Sects. 3.1
  to 3.5, 4.6, 6.1, 6.6 and App. C for every step above; no HTML
  rendering, read through the LaTeX source.
- Riess et al. 2024, arXiv:2401.04773 (method, JWST): quality cuts,
  crowding corrections, Wesenheit systems, phase, Table 4 variants.
- Riess et al. 2025, arXiv:2509.01667 (test): 19 JWST hosts, background-
  free host (summarised in L2).
- Breuval et al. 2024, arXiv:2404.08038 (method): SMC anchor and the
  metallicity coefficient on [Fe/H] and [O/H] (summarised in L2).
- Freedman et al. 2024, arXiv:2408.06153 (critique): App. B on photometry
  packages, M_B–distance trend, host distances.
- Mörtsell et al. 2021, arXiv:2105.11461 (critique): per-host
  colour–luminosity relations.
- Högås & Mörtsell 2024, arXiv:2412.07840 (critique): period dependence,
  matched resampling, broken PL.
- Madore & Freedman 2026, arXiv:2602.13397 and Breuval et al. 2025,
  arXiv:2507.15936 (debate): Milky Way calibration and metallicity
  (summarised in L2).

## Not verified
<!-- key: not-verified -->

- The optical discovery pipeline and its selection cuts (Yuan et al.,
  cited as Y22b in arXiv:2112.04510) and the period-completeness limit per
  host.
- How SH0ES phase-corrects random-phase HST F160W epochs; Sect. 3.4 only
  says observations are taken "at known Cepheid phases".
- SH0ES Appendix D on the use and misuse of Wesenheit magnitudes, and the
  body of arXiv:2105.11461 (abstract only).
- The Milky Way recalibration of arXiv:2412.07840 (their Sect. V) and the
  value of their Eq. 24, which the quoted shifts imply is 72.67 [der].
- The CCHP JWST Cepheid analysis of NGC 7250 (cited in arXiv:2408.06153).
