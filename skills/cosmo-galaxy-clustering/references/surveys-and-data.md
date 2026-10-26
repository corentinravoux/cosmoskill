# Galaxy clustering — surveys and data

Scope: the spectroscopic redshift surveys used for BAO, RSD and full-shape
cosmology: instrument, area, samples, releases, public data, status, next
steps. Past, current, planned. Snapshot: 2026-10-26.

Flags: `[src]` read this session in the cited paper or on the named official
page; `[sec]` from a named secondary source; `[der]` derived here. Facility
detail beyond what clustering analyses need belongs to
`cosmo-surveys-facilities`.

## 1. Past surveys
<!-- key: past-surveys -->

### 1.1 2dF Galaxy Redshift Survey (2dFGRS)
<!-- key: 2df-galaxy-redshift-survey-2dfgrs -->

- Instrument: 2dF multi-fibre spectrograph on the Anglo-Australian Telescope,
  400 objects at once over a 2° diameter field [src: abstract] (Colless et al. 2001,
  arXiv:astro-ph/0106498).
- Design: about 250,000 galaxies to b_J = 19.45, 2000 deg², median depth
  z = 0.11 (arXiv:astro-ph/0106498) [src: abstract].
- Final clustering sample: 221,414 galaxies (Cole et al. 2005,
  arXiv:astro-ph/0501174) [src: abstract].
- Result that matters: evidence for baryon oscillations in P(k),
  Ω_m h = 0.168 ± 0.016, Ω_b/Ω_m = 0.185 ± 0.046 [src: abstract]
  (arXiv:astro-ph/0501174).

### 1.2 6dF Galaxy Survey (6dFGS)
<!-- key: 6df-galaxy-survey-6dfgs -->

- Southern sky at |b| > 10°; 125,071 galaxies in the final catalogue, median
  redshift 0.053 (Jones et al. 2009, arXiv:0903.5451) [src: abstract].
- BAO at z_eff = 0.106: D_V = 456 ± 27 Mpc, H0 = 67 ± 3.2 km/s/Mpc with the
  WMAP-7 sound horizon [src: abstract] (Beutler et al. 2011, arXiv:1106.3366).
- It is the lowest-redshift BAO point of the pre-DESI compilations; the
  lowest DESI bin is BGS at z_eff = 0.295 [src: Sect. III.1] (arXiv:2503.14738).

### 1.3 WiggleZ
<!-- key: wigglez -->

- Redshift range 0.2 < z < 1. Reconstructed BAO distances at
  z = 0.44, 0.60, 0.73 with 4.8%, 4.5% and 3.4% precision (Kazin et al.
  2014, arXiv:1401.0358) [src: abstract].
- Sample size and area were not read this session.

### 1.4 SDSS-I/II
<!-- key: sdss-i-ii -->

- LRG sample of the first BAO detection: 46,748 galaxies, 3816 deg²,
  0.16 < z < 0.47, 0.72 h⁻³ Gpc³ [src: abstract] (Eisenstein et al. 2005,
  arXiv:astro-ph/0501171).
- DR7 Main Galaxy Sample for BAO: z < 0.2, 6813 deg², bias about 1.5, 1000
  mocks [src: abstract] (Ross et al. 2015, arXiv:1409.3242).

### 1.5 BOSS (SDSS-III)
<!-- key: boss-sdss-iii -->

- Final DR12 clustering sample: 1.2 million massive galaxies, effective area
  9329 deg², volume 18.7 Gpc³, 0.2 < z < 0.75, analysed in three overlapping
  slices at z_eff = 0.38, 0.51, 0.61 (Alam et al. 2017, arXiv:1607.03155)
  [src: abstract; 0.2 < z < 0.75 from Sect. 2.2].
- Samples named LOWZ and CMASS in the catalogue papers; the consensus
  analysis combines them.
- Observational systematics and selection function: Ross et al. 2017,
  arXiv:1607.03145.
- Public: SDSS DR12 large-scale-structure catalogues. BOSS remains the
  standard test-bed for new estimators and EFT pipelines.

### 1.6 eBOSS (SDSS-IV)
<!-- key: eboss-sdss-iv -->

Final DR16 catalogues (Ross et al. 2020, arXiv:2007.09000; Mohammad et
al. 2020, arXiv:2007.09005). LRG and QSO rows from the abstract of the first,
ELG row from the abstract of arXiv:2007.09005 [src: abstract of each]:

| Tracer | z range | N | Area [deg²] |
|---|---|---|---|
| LRG (eBOSS only) | 0.6–1.0 | 174,816 | 4,242 |
| LRG (eBOSS + BOSS CMASS) | 0.6–1.0 | 377,458 | 9,493 |
| ELG | 0.6–1.1 | 173,736 | 1,170 |
| QSO | 0.8–2.2 | 343,708 | 4,808 |

The SDSS cosmology compilation uses eight BAO samples and six fσ8
measurements from SDSS, SDSS-II, BOSS and eBOSS, including Lyα [src] (Alam et
al. 2021, arXiv:2007.08991). The DESI DR2 paper states that its bins now have
far larger effective volume than the SDSS counterparts and no longer forms
mixed DESI + SDSS compilations [src] (DESI Collaboration 2025,
arXiv:2503.14738).

## 2. Current surveys
<!-- key: current-surveys -->

### 2.1 DESI
<!-- key: desi -->

**Instrument** [src: abstract] (DESI Collaboration 2022, arXiv:2205.10939): 4 m Mayall
telescope, Kitt Peak; 3.2° diameter prime-focus corrector; 5020 robotic fibre
positioners in ten petals; ten three-arm spectrographs covering 360–980 nm at
resolution 2000–5000. Survey start: May 2021.

**Design** (DESI Collaboration 2016, arXiv:1611.00036): four target classes
selected from imaging, BGS, LRG, ELG, QSO, with QSO at z > 2.1 used for the
Lyα forest (2.1 < z < 3.5); more than 30 million redshifts planned
[src: Sect. 1]. Targets come from
the DESI Legacy Imaging Surveys DR9 (DECaLS, BASS, MzLS) (DESI
Collaboration 2024, arXiv:2404.03002) [src: Sect. 2.2].

**Target densities and priorities** (arXiv:2404.03002) [src: Sect. 2.2,
sample paragraphs]: BGS Bright 854 deg⁻²; LRG 624 deg⁻²; QSO 310 deg⁻²,
highest priority; ELG lowest priority, with a random 10% at LRG priority. Bright-time and dark-time programmes are
separate.

**Releases.**

| Release | Public date | Content | Flag |
|---|---|---|---|
| EDR (Survey Validation) | 13 June 2023 | 1.8 million unique targets, Survey Validation observations December 2020 through June 2021 | [doc: https://data.desi.lbl.gov/doc/releases/, 2026-10-26] [doc: https://data.desi.lbl.gov/doc/releases/edr/, 2026-10-26] |
| DR1 | 2025-03-19 | 18.7 million new spectra, main survey May 2021 – June 2022, plus a reprocessing of the Survey Validation data of the EDR | [doc: https://data.desi.lbl.gov/doc/releases/, 2026-10-26]; count also in arXiv:2503.14745 [src: abstract] |
| DR2 cosmology products | 6 October 2025 | cosmology chains (MCMC) and best-fit values; the full DR2 "in some months" | [doc: https://www.desi.lbl.gov/2025/10/06/desi-dr2-cosmology-chains-and-data-products-released/, 2026-10-26] |
| DR2 spectra and catalogues | not public at snapshot | first three years | see "Not verified" |

EDR per target class: 428,758 BGS, 227,318 LRG, 437,664 ELG, 76,079 QSO,
466,447 Milky Way Survey objects with good spectra (DESI Collaboration
2023, arXiv:2306.06308) [src: abstract]. DR1: 13.1 million galaxies, 1.6
million quasars, 4 million stars (DESI Collaboration 2025, arXiv:2503.14745)
[src: abstract].

Public locations [src]: `data.desi.lbl.gov/public/edr`,
`data.desi.lbl.gov/public/dr1`, and for DR2 cosmology
`data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/`.

**DR1 clustering data** (arXiv:2404.03002) [src: Sect. 2.2]: main-survey observations
from 14 May 2021 to 14 June 2022; 2744 dark and 2275 bright tiles; about
7500 deg², just over half of the expected final 14,200 deg²; the final survey
was planned at 9929 dark and 5676 bright tiles. Catalogue construction: Ross
et al. 2025, arXiv:2405.16593; sample definitions and two-point pipeline:
DESI Collaboration 2024, arXiv:2411.12020.

**Clustering samples, DR1 versus DR2.** DR1 counts from arXiv:2404.03002
(Sect. 2.2 sample paragraphs; BGS and QSO also in its Table 1); DR2 columns
from arXiv:2503.14738, Table 2, except the QSO count, which is the BAO bin of
its Table 3. From arXiv:2404.03002 and arXiv:2503.14738 [src: Sect. 2.2, Tables 1, 2 and 3]:

| Tracer | z range | N (DR1 BAO) | N (DR2 BAO) | DR2 area [deg²] | DR2 assignment completeness | DR2 z success |
|---|---|---|---|---|---|---|
| BGS | 0.1–0.4 | 300,017 | 1,188,526 | 12,355 | 75.5% | 98.8% |
| LRG | 0.4–1.1 | 2,138,600 | 4,468,483 | 10,031 | 82.6% | 99.0% |
| ELG | 0.8–1.6 | 2,432,022 | 6,534,844 | 10,352 | 53.7% | 73.9% |
| QSO (tracer) | 0.8–2.1 (BAO) | 856,652 | 1,461,588 | 11,181 | 93.6% | 68.0% |

The DR2 QSO row of the catalogue table counts 2,062,839 good redshifts over
0.8 < z < 3.5; the 1,461,588 is the 0.8 < z < 2.1 BAO bin (arXiv:2503.14738)
[src: Tables 2 and 3].

Changes from DR1 to DR2 (arXiv:2503.14738, Sect. II.1) [src]:

- ELG sample larger by a factor 2.7, LRG 2.1, QSO 1.7; area larger by
  between 54% (QSO) and 75% (LRG and ELG) (arXiv:2503.14738) [src: Sect. II.1].
  The DR1 and DR2 effective volumes per bin are in the tables of
  `results.md`, Sects. 1.1–1.2.
- BGS: nearly 4× the DR1 BAO sample. Half of the gain is area and
  completeness; the rest comes from relaxing the absolute-magnitude cut from
  M_r < −21.5 to M_r < −21.35, with a new definition of M_r without k- or
  e-corrections (arXiv:2503.14738) [src: Sect. II.1].
- DESI DR2 holds more than 9.1 million BGS redshifts at 0.1 < z < 0.4; the
  BAO analysis uses 1,188,526 of them (Table 2). Using all would add about
  20% of effective volume (arXiv:2503.14738) [src: Sect. II.1].
- Lyα: over 820,000 forest spectra and over 1.2 million quasar positions,
  about twice DR1 [src: abstract] (DESI Collaboration 2025, arXiv:2503.14739).

**Mocks.** AbacusSummit N-body (Maksimova et al. 2021, arXiv:2110.11398) with
HODs fitted to early data for validation; EZmocks for covariance (Chuang et
al. 2015, arXiv:1409.1124).

**Status** [doc:
https://www.desi.lbl.gov/2026/04/15/desi-reaches-mapping-milestone-surpassing-expectations/,
2026-10-26] (DESI announcement of 15 April 2026): the planned five-year survey
is complete, its observations finished "ahead of schedule", with more than 47
million galaxies and quasars against a goal of 34 million, and 20 million
stars of the Milky Way. Observations continue through 2028 and extend the
footprint from 14,000 to 17,000 deg². The first dark-energy results from the
full five-year survey are expected in 2027; the analyses so far use the first
three years of data.

**Published cosmology by release.**

| Release | BAO | Full shape | f_NL |
|---|---|---|---|
| DR1 | April 2024 (arXiv:2404.03000, arXiv:2404.03002) | November 2024 (Adame et al. 2024, arXiv:2411.12021; DESI Collaboration 2024, arXiv:2411.12022) | November 2024 (Chaussidon et al. 2024, arXiv:2411.17623) |
| DR2 | March 2025 (arXiv:2503.14738, arXiv:2503.14739) | Lyα AP only, July 2026 (DESI Collaboration 2026, arXiv:2607.27410); no galaxy full-shape key paper found | none found |

### 2.2 Euclid (spectroscopic survey)
<!-- key: euclid-spectroscopic-survey -->

- Mission: optical imaging plus near-infrared imaging and slitless
  spectroscopy over about 14,000 deg² (Euclid Collaboration: Mellier et
  al. 2025, arXiv:2405.13491) [src: abstract].
Public releases to date, complete list as of 2026-10-26 (ESA Euclid data page
[doc: https://www.cosmos.esa.int/web/euclid/data, 2026-10-26]; ESA Euclid
timeline [doc: https://www.cosmos.esa.int/web/euclid/timeline, 2026-10-26]):
(i) Early Release Observations (ERO) data release, 23 May 2024; (ii) Quick
Data Release 1 (Q1), 19 March 2025; (iii) Quick Data Release 2 (Q2), 24 June
2026. No other public release is listed. None of the three is a cosmology
release.
- Q1 content: 63.1 deg² of the Euclid Deep Fields at wide-survey depth, about
  30 million objects, processed with early pipelines [src: abstract] (Euclid
  Collaboration: Aussel et al. 2025, arXiv:2503.15302).
Q2 content: the Euclid Galactic Bulge Survey, 4.8 deg² over nine adjoining
fields, calibrated VIS images with astrometry and photometry catalogues for 60
million stars; the page lists no galaxy-clustering or lensing product (Euclid
Consortium Q2 page [doc: https://www.euclid-ec.org/science/q2/, 2026-10-26]).
Announced next releases (ESA Euclid timeline [doc:
https://www.cosmos.esa.int/web/euclid/timeline, 2026-10-26]; the page states
that "data release dates are tentative and will have to be confirmed"):
DR1-Foundation 12 November 2026; DR1 mid-2027; Quick Data Release 3 (Q3) 2028;
DR2 June 2029; Quick Data Release 4 (Q4) 2030; DR3 October 2031. The IPAC
timeline [doc: https://euclid.caltech.edu/page/data-release-timeline,
2026-10-26] gives DR1 Foundation 12 November 2026, DR1 complete mid-2027, DR2
March 2029 and DR3 October 2031; the ESA page is the reference.
DR1: about 1900 deg² (about 1400 south, 500 north), observed 14 February 2024
to 21 May 2025, released in two stages: DR1-Foundation (raw data and
calibrated images, catalogues, spectra) in November 2026, on 12 November by
the IPAC page, and the complete DR1 with the higher-level products for galaxy
clustering and weak lensing in mid-2027 (ESA Euclid DR1 timeline page, update
of 15 June 2026 [doc: https://www.cosmos.esa.int/web/euclid/dr1-timeline,
2026-10-26]; IPAC Euclid DR1 page for the split, the observation dates and the
day [doc: https://euclid.caltech.edu/page/euclid-dr1, 2026-10-26]).
- The BAO pipeline was validated end to end on mocks for 0.9 ≤ z ≤ 1.8
  (Euclid Collaboration: Sarpa et al. 2026, arXiv:2605.03446). [src: abstract]
- No Euclid spectroscopic clustering measurement on data was found as of the
  snapshot.

### 2.3 Subaru Prime Focus Spectrograph (PFS)
<!-- key: subaru-prime-focus-spectrograph-pfs -->

- 8.2 m Subaru; 1.25 deg² field; 2386 science fibres; offered to the
  community since March 2025, with queue observing and "fibre hours" as the
  allocation unit [src: abstract] (Tanaka et al. 2026, arXiv:2606.14012).
- Cosmology programme as designed (**forecast**): emission-line galaxies over
  0.8 < z < 2.4 in 9.3 (Gpc/h)³; distances to 3% in each of six redshift bins
  from BAO; growth to 6% from RSD; 300 nights assumed [src: abstract] (Takada et al.
  2014, arXiv:1206.0737).
- No PFS clustering result was found as of the snapshot.

### 2.4 4MOST
<!-- key: 4most -->

VISTA, a 4-m-class telescope at Paranal; spectra of about 2400 objects at once
(ESO: "more than 2400 fibres") over a hexagonal 4.2 deg² field; Verification,
Commissioning and Survey Validation phases in 2026, full science operations
expected from Q2 2026; an initial five-year Public Survey of at least 25
million objects over at least 15 000 deg² (4MOST project site [doc:
https://www.4most.eu/cms/, 2026-10-26]). First light was obtained on 18
October 2025 (ESO announcement sciann17735, published 22 October 2025 [doc:
https://www.eso.org/sci/publications/announcements/sciann17735.html,
2026-10-26]). The project site gives 21 October; quote ESO's date.
- Cosmology Redshift Survey (CRS): 5.4 million redshifts over about 5700 deg²
  from bright galaxies, LRGs and quasars, selected from Legacy Survey DR10.1
  imaging [src: abstract] (Bandi et al. 2025, arXiv:2510.02449). **Planned**, not yet
  observed at the time of that paper.

### 2.5 SPHEREx
<!-- key: spherex -->

- Launched 11 March 2025; all-sky spectral survey in 102 bands from 0.75 to
  5.0 μm at resolving power 35–130 in 6.2″ pixels; four all-sky passes over
  two years (Bock et al. 2025, arXiv:2511.02985) [src: abstract].
- Cosmology goal: a low-resolution all-sky redshift survey to constrain
  inflationary non-Gaussianity [src]. Spectral images are released rapidly;
  no redshift catalogue or clustering result was found as of the snapshot.

### 2.6 Nancy Grace Roman Space Telescope
<!-- key: nancy-grace-roman-space-telescope -->

Launched 30 August 2026 on a Falcon Heavy, towards L2, for a three-month
commissioning; first images expected by early 2027 (NASA release [doc:
https://www.nasa.gov/news-release/nasas-dark-universe-seeking-nancy-grace-roman-space-telescope-launches/,
2026-10-26]). In the science commissioning phase since 22 October 2026 (NASA
Roman blog [doc:
https://science.nasa.gov/blogs/roman/2026/10/22/nasas-roman-space-telescope-enters-final-commissioning-phase/,
2026-10-26]).
- Reference High Latitude Spectroscopic Survey (**forecast**, 2021 reference
  design): 2000 deg² with the near-IR grism (1.0–1.93 μm, R = 435–865), about
  10 million Hα redshifts at z = 1–2 and 2 million [O III] redshifts at
  z = 2–3, in about 0.6 years of observing [src: abstract] (Wang et al. 2022,
  arXiv:2110.01829). The survey as finally defined (High Latitude Wide Area
  Survey) was not read this session.

## 3. Planned
<!-- key: planned -->

- **DESI extension** (through 2028; footprint in Sect. 2.1).
- **Spec-S5**: two 4 m telescopes upgraded to 6 m wide-field facilities, each
  with 13,000 fibres; more than a tenfold gain in spectroscopic capability;
  concept and overview stage [src: abstract] (Poppett et al. 2026, arXiv:2608.07927).
- **Euclid DR1 clustering products**: mid-2027; DR2 June 2029 and DR3 October
  2031, tentative (Sect. 2.2).
- **DESI final-survey BAO**: 2027 (Sect. 2.1).

## 4. Timeline
<!-- key: timeline -->

| Date | Event | Flag |
|---|---|---|
| 2005 | First BAO detections (SDSS LRG, 2dFGRS) | [src] |
| 2017 | BOSS DR12 consensus | [src] |
| 2020–2021 | eBOSS DR16 final results | [src] |
| May 2021 | DESI main survey starts | [src] |
| June 2023 | DESI EDR | [src] |
| April 2024 | DESI DR1 BAO | [src] |
| May 2024 | Euclid ERO data release (2024-05-23) | [src] |
| November 2024 | DESI DR1 full shape, f_NL | [src] |
| March 2025 | DESI DR1 public; DESI DR2 BAO; Euclid Q1 (2025-03-19); PFS operations; SPHEREx launch | [src] |
| October 2025 | DESI DR2 cosmology products public; 4MOST first light | [src] |
| April 2026 | DESI planned survey complete | [src] |
| June 2026 | Euclid Q2 (2026-06-24; Galactic Bulge Survey, not cosmology) | [src] |
| July 2026 | DESI DR2 Lyα AP | [src] |
| August 2026 | Roman launch | [src] |
| 2026-11-12 | Euclid DR1-Foundation (planned) | [src] |
| 2027 | DESI full-survey results; Euclid complete DR1 (planned, mid-2027) | [src] |
| June 2029; October 2031 | Euclid DR2; Euclid DR3 (planned, tentative) | [src] |

## 5. Practical notes on using the data
<!-- key: practical-notes-on-using-the-data -->

- DESI BAO likelihoods are distributed as means and covariances of
  (D_M/r_d, D_H/r_d) or D_V/r_d per bin; DR1 and DR2 must not be combined as
  independent.
- The DESI DR1 full-shape likelihood exists in two forms: the collaboration's
  full-modelling data vectors with systematic covariance, and the ShapeFit
  compressed vectors with Gaussian covariances given in the appendix of
  arXiv:2411.12021. The Gaussian approximation is weakest where projection
  effects are strong (BGS α_AP is prior-dominated [src]).
- DR1 LSS catalogues, two-point measurements and covariances are released
  with DR1 [src] (arXiv:2411.12020).
- Independent groups reanalyse the public DR1 catalogues with their own
  estimators (Chudaykin et al. 2025, arXiv:2507.13433); their data vectors
  are not the collaboration's.

## Not verified
<!-- key: not-verified -->

- Public release date of the full DESI DR2 spectra and catalogues. The DESI
  announcement of 6 October 2025 says "in some months"; a web-search summary
  attributed "by early 2027" to a 2025 Milky Way Survey paper, not read here.
- The total redshift goal of the DESI extension (a web-search summary gave a
  figure that was not found on the pages fetched).
- WiggleZ sample size and area; BOSS LOWZ/CMASS individual numbers.
- Euclid launch date, NISP wavelength range, and expected numbers of
  spectroscopic redshifts in DR1.
- PFS cosmology survey area and observing progress; 4MOST start of full
  science operations (the site states an expected date, not an achieved one).
- The Roman survey definition after the 2025 community process.
- SPHEREx completion date of the first all-sky pass.
