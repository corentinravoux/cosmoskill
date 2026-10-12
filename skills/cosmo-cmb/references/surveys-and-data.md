# CMB experiments and data releases

Scope: the experiments and data releases that matter for primary CMB
anisotropies, lensing and B-mode status — instrument, sky, depth, release,
public location, status on the snapshot date and what comes next.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper or official page;
`[sec]` from a named secondary source; `[der]` derived here. Forecasts are
labelled **forecast**.

---

## 1. Past
<!-- key: past -->

### WMAP
<!-- key: wmap -->

Nine-year final release, 2012. The WMAP-only fit and its combinations
remain the Planck-independent large-scale anchor: ACT forms "W-ACT" from
ACT DR6 plus WMAP9, discarding WMAP polarisation at ℓ < 23 and substituting
Planck SRoll2 for τ [src] (Louis et al. 2025, arXiv:2503.14452). The
nine-year parameter paper is Hinshaw et al. 2012 (arXiv:1212.5226), which
reports a detection of tilt at 5σ and r < 0.13 with external data [src].

### Planck
<!-- key: planck -->

ESA satellite, launched 14 May 2009; scanned from 12 August 2009 to
23 October 2013; nine bands from 30 to 857 GHz; all sky [src] (Planck
Collaboration 2018, arXiv:1807.06205).

| Release | Year | Content | Reference | Status |
|---|---|---|---|---|
| 2015 (PR2) | 2015 | Full-mission temperature; LFI low-ℓ polarisation | arXiv:1502.01589 | superseded |
| 2018 (PR3, "legacy") | 2018 | Full use of HFI polarisation; Plik and CamSpec high-ℓ; lowE; lensing 8 ≤ L ≤ 400 | arXiv:1807.06209, arXiv:1907.12875, arXiv:1807.06210 | still the default high-ℓ Planck input of ACT and SPT |
| SRoll2 | 2019 | Reprocessed HFI large-scale polarisation maps and low-ℓ EE likelihood | arXiv:1901.11386, arXiv:1908.09856 | τ input of ACT DR6 |
| PR4 (NPIPE) | 2020 | Joint LFI+HFI reprocessing, slightly more data, 600 end-to-end simulations | arXiv:2007.04997 | basis of CamSpec PR4, HiLLiPoP/LoLLiPoP, PR4 lensing |
| CamSpec PR4 | 2022 | High-ℓ likelihood on NPIPE maps; about 10% tighter than 2018 | Rosenberg et al. 2022, arXiv:2205.10869 | current |
| HiLLiPoP + LoLLiPoP PR4 | 2023 | Up to 75% of sky; 10–20% tighter than 2018 | Tristram et al. 2023, arXiv:2309.10034 | current |
| PR4 lensing | 2022 | S/N almost 20% higher than 2018 | Carron et al. 2022, arXiv:2206.07773 | current |
| CamSpec-NPIPE-lite | 2025 | Nuisance-marginalised PR4 spectra for combination with ground data | Jense et al. 2025, arXiv:2510.09430 | current |

Planck measures five of the six base parameters to better than 1% and 18
acoustic peaks across temperature and polarisation [src] (arXiv:1807.06205).
Going from PR3 to PR4 the extra constraining power comes from polarisation
at all scales and from temperature above ℓ = 1500 [src] (arXiv:2510.09430).

### ACT DR4
<!-- key: act-dr4 -->

ACTPol data from 2013–2016 at 98 and 150 GHz; maps over more than
17,000 deg², the deepest 600 deg² below 10 μK-arcmin; spectra from almost
6000 deg² [src] (Aiola et al. 2020, arXiv:2007.07288). Superseded by DR6.

### SPT-3G 2018
<!-- key: spt-3g-2018 -->

A four-month, partial-focal-plane season on the 1500 deg² field. TT/TE/EE
over 750 ≤ ℓ < 3000 in TT (Balkenhol et al. 2022, arXiv:2212.05642) and a
temperature-only lensing measurement over 50 < L < 2000 (Pan et al. 2023,
arXiv:2308.11608) [src]. Superseded by D1.

### BICEP2 / Keck Array through 2018
<!-- key: bicep2-keck-array-through-2018 -->

Small-aperture refractors at the South Pole observing one deep patch.
BK18 combines BICEP2, Keck Array and BICEP3 through the 2018 season:
Q/U depths of 2.8, 2.8 and 8.8 μK-arcmin at 95, 150 and 220 GHz over about
600 deg² at 95 GHz and about 400 deg² at 150 and 220 GHz [src]
(BICEP/Keck 2021, arXiv:2110.00483). It is still the latest published
BICEP/Keck constraint on r.

## 2. Current
<!-- key: current -->

### ACT DR6 (final ACT cosmology release)
<!-- key: act-dr6-final-act-cosmology-release -->

| Item | Value | Source |
|---|---|---|
| Camera and period | AdvancedACT, 2017–2022 | Naess et al. 2025, arXiv:2503.14451 [src] |
| Bands | 98, 150, 220 GHz (f090, f150, f220) | arXiv:2503.14451 [src] |
| Area mapped | 19,000 deg² | arXiv:2503.14451 [src] |
| Median combined depth | 10 μK-arcmin | arXiv:2503.14451 [src] |
| Polarisation noise | white-noise level three times lower than Planck | arXiv:2503.14452 [src] |
| Area used for spectra | 10,000 deg² | arXiv:2503.14452 [src] |
| Lensing map | 9400 deg², night-time data, 43σ | Qu et al. 2023, arXiv:2304.05202 [src] |
| Papers | maps arXiv:2503.14451; spectra and ΛCDM arXiv:2503.14452; extended models arXiv:2503.14454; foregrounds arXiv:2506.06274; covariance arXiv:2412.07068; lensing arXiv:2304.05202, arXiv:2304.05196 | |
| Public data | NASA LAMBDA, `lambda.gsfc.nasa.gov/product/act/actadv_prod_table.html` | arXiv:2503.14451 [src] |
| Code | PSpipe (spectra), MFLike and ACT-lite (likelihoods) | arXiv:2503.14452, arXiv:2503.14454 [src] |

Night-time data carry about two thirds of the statistical power and are
the only data in the DR6 lensing analysis [src] (arXiv:2304.05202). The
DR6 data end in 2022 [src] (arXiv:2503.14451); DR6 is the last ACT
power-spectrum release.

### SPT-3G
<!-- key: spt-3g -->

10 m telescope at the South Pole, third-generation camera, bands at 95, 150
and 220 GHz.

| Item | Value | Source |
|---|---|---|
| D1 data set | 2019 and 2020 seasons of the Main field | Camphuis et al. 2025, arXiv:2506.20707 [src] |
| Main field | 1500 deg², 4% of the sky | arXiv:2506.20707, arXiv:2608.31136 [src] |
| D1 map depth, I | 5.4, 4.4, 16.2 μK-arcmin at 95, 150, 220 GHz | Quan et al. 2026, arXiv:2603.20163 [src] |
| D1 map depth, Q/U | 8.4, 6.6, 25.8 μK-arcmin | arXiv:2603.20163 [src] |
| Coadded polarisation noise | about 4.9 μK-arcmin | Ge et al. 2024, arXiv:2411.06000 [src] |
| D1 papers | spectra and cosmology arXiv:2506.20707; maps arXiv:2603.20163; secondary anisotropies arXiv:2601.20551; QE lensing arXiv:2608.31136; lensing templates arXiv:2608.06343; polarised beam arXiv:2602.06334 | |
| Earlier D1-era lensing | polarisation-only MUSE analysis | arXiv:2411.06000 |
| Full survey | Main + Summer + Wide fields, about 10,000 deg², 25% of the sky | Vitrier et al. 2025, arXiv:2510.24669 [src] |
| Public data | `pole.uchicago.edu/public/data/camphuis25/`; likelihood data at `github.com/SouthPoleTelescope/spt_candl_data` | arXiv:2506.20707 [src] |
| Code | candl, SPT-lite | arXiv:2401.13433, arXiv:2506.20707 |

The D1 maps are "the deepest to date used for measurements of mid-to-high-ℓ
primary temperature and E-mode polarization" and are public [src]
(arXiv:2603.20163). D1 uses two observing seasons of one field; the
collaboration forecasts that the full 10,000 deg²
data set combined with Planck would improve the figures of merit for early
dark energy and for a varying electron mass by factors above 90 and 190
(**forecast**) and that analysing the fields separately loses under 3% in
ΛCDM parameter precision (**forecast**) [src] (arXiv:2510.24669).

### BICEP3 and BICEP Array
<!-- key: bicep3-and-bicep-array -->

Operating at the South Pole. The next release will use data through 2024
and is forecast to reach σ(r) ≈ 0.005 including delensing; the long-term
goal is σ(r) ≈ 0.001 by 2034 (**forecast**) [src] (Vergès et al. 2026,
arXiv:2606.13942). Delensing will use SPT-3G lensing templates (Nakato et
al. 2026, arXiv:2608.06343).

### CLASS
<!-- key: class -->

Large-angular-scale polarimeter array in the Atacama using a
variable-delay polarisation modulator. The 90 GHz data through 2024
(115 detector-years) reach 78 μK-arcmin in polarisation,
comparable to Planck at 100 and 143 GHz, and give the first ground-based
τ estimate in cross-correlation with Planck [src] (Li et al. 2025,
arXiv:2501.11904).

### Simons Observatory (SO)
<!-- key: simons-observatory-so -->

Cerro Toco, Atacama, 5200 m [src] (Harrington et al. 2026,
arXiv:2609.26938).

| Item | Status | Source |
|---|---|---|
| Design | three 0.5 m small-aperture telescopes (SATs) and one 6 m large-aperture telescope (LAT); 27, 39, 93, 145, 225, 280 GHz; 60,000 bolometers | SO Collaboration 2018, arXiv:1808.07445 [src] |
| Mid-frequency SATs | commissioning observations began late 2023; about 9400 biased detectors each; combined NET 2.4 μK√s at 90 GHz and 3.2 μK√s at 150 GHz, better than the baseline target | arXiv:2609.26938 [src] |
| LAT | first celestial image (Mars) on 22 February 2025 | Simons Foundation press release of 17 March 2025 [src] |
| SAT expansion | six SATs by 2027, 48,160 detectors at 93 and 145 GHz, survey to 2035 | SO Collaboration 2025, arXiv:2512.15833 [src] |
| LAT upgrade | complete by 2028: doubled mapping speed with 30,000 new detectors; survey of about 60% of the sky | SO Collaboration 2025, arXiv:2503.00636 [src] |

No SO cosmological power spectrum, lensing map or public data release was
found in the searches of 2026-10-07; the 2026 SO papers found are
instrument and commissioning papers.

## 3. Planned, and cancelled
<!-- key: planned-and-cancelled -->

### CMB-S4 — cancelled
<!-- key: cmb-s4-cancelled -->

On 9 July 2025 DOE and NSF informed the project that they "have jointly
decided that they can no longer support the CMB-S4 Project"; the project is
carrying out an orderly shutdown and documenting its designs [src]
(cmb-s4.org, read 2026-10-07). The science case is in the CMB-S4 Science
Book (Abazajian et al. 2016, arXiv:1610.02743). Any text that lists CMB-S4
targets as upcoming measurements is stale.

### What replaces it in practice
<!-- key: what-replaces-it-in-practice -->

| Project | Plan | Target | Source |
|---|---|---|---|
| SPT-3G+ | New receiver on SPT, installation planned early 2029; 24,080 detectors at 90 and 150 GHz; six-year survey overlapping the BICEP field to 0.5 μK-arcmin | with BICEP Array as the "South Pole Observatory": σ(r) = 0.001 (**forecast**) | Natoli et al. 2026, arXiv:2608.20236 [src] |
| BICEP Array | additional receivers; BA4 at 90/150 GHz scheduled for deployment in the 2026–27 austral summer | σ(r) ≈ 0.001 by 2034 (**forecast**) | arXiv:2606.13942 [src]; BA4 schedule from 2026 BICEP Array instrument papers [sec] |
| SO, expanded SATs | six SATs, survey to 2035 | σ(r) = 1.2 × 10⁻³, or 7 × 10⁻⁴ for optimistic foregrounds and noise, assuming 70% delensing (**forecast**) | arXiv:2512.15833 [src] |
| SO, original | three SATs, five years | σ(r) = 0.003 (**forecast**) | arXiv:1808.07445 [src] |
| SO enhanced LAT | 60% of sky, ten times Planck's map depth | light relics, neutrino mass with LSS, 30,000 clusters (**forecast**) | arXiv:2503.00636 [src] |

### LiteBIRD
<!-- key: litebird -->

JAXA-led satellite for large-scale B modes.

| Item | 2022 design | After the 2024–2026 reformation |
|---|---|---|
| Telescopes | three | one cross-Dragone reflector, 500 mm aperture, cooled to about 5 K |
| Bands | 15 between 34 and 448 GHz | 12, centres 40–402 GHz, optical coverage 34–448 GHz |
| Sensitivity goal | total 2.2 μK-arcmin; 0.5° resolution at 100 GHz | δr < 0.002 (68%) total, including foreground residuals, systematics and margin |
| Survey | 3 years at L2 | 3 years, Lissajous orbit at L2 |
| Launch | "late 2020s" | JFY2036 |
| Source | LiteBIRD Collaboration 2022, arXiv:2202.02773 [src] | LiteBIRD Collaboration 2026, arXiv:2607.25285 [src]; launch date and reviews from the ISAS/JAXA mission page, read 2026-10-07 [src] |

Milestones from the ISAS/JAXA page [src]: October 2024, KEK relinquished
its technological contribution and a one-year study of reformation plans
began; 25 September 2025, the reformation plan was evaluated and the team
was told to continue toward a mission definition review; 26 June 2026,
Mission Definition Review #2 was held, and the page headline states that
LiteBIRD passed it and advanced to Phase A. The δr < 0.001 target that
appears in older texts is the earlier design goal [sec] (stated as
"δr ∼ 0.001" in a 2025 LiteBIRD simulation-release abstract seen in the
search results); the reformed requirement is δr < 0.002.

## 4. Where the data are
<!-- key: where-the-data-are -->

| Product | Location | Verified |
|---|---|---|
| ACT DR6 maps and derived products | LAMBDA (URL above) | [src] arXiv:2503.14451 |
| SPT-3G D1 band powers and likelihood | pole.uchicago.edu (URL above), spt_candl_data on GitHub | [src] arXiv:2506.20707 |
| SPT, ACT likelihoods in differentiable form | candl, `github.com/Lbalkenhol/candl` | [src] arXiv:2401.13433 |
| SRoll2 maps | `sroll20.ias.u-psud.fr` | [src] arXiv:1901.11386 |
| CosmoPower emulators trained for SPT accuracy | cosmopower GitHub repository, `trained_models/SPT_high_accuracy` | [src] arXiv:2506.20707 |

## 5. Timeline in one view
<!-- key: timeline-in-one-view -->

| Date | Event | Source |
|---|---|---|
| 2018-07 | Planck legacy release | arXiv:1807.06209 |
| 2020-07 | Planck PR4 (NPIPE); ACT DR4 | arXiv:2007.04997, arXiv:2007.07288 |
| 2021-10 | BK18, r < 0.036 | arXiv:2110.00483 |
| 2023-04 | ACT DR6 lensing | arXiv:2304.05202 |
| 2024-04-18 | ACT DR6 parameters unblinded | arXiv:2503.14452 |
| 2024-09-09 | SPT-3G D1 unblinded | arXiv:2506.20707 |
| 2025-02-22 | SO LAT first image | Simons Foundation |
| 2025-03-18 | ACT DR6 spectra, parameters and extended models on arXiv, same day as DESI DR2 | arXiv:2503.14452, arXiv:2503.14738 |
| 2025-06-25 | SPT-3G D1 spectra and CMB-SPA | arXiv:2506.20707 |
| 2025-07-09 | CMB-S4 support withdrawn | cmb-s4.org |
| 2026-03 | SPT-3G D1 maps public | arXiv:2603.20163 |
| 2026-06-26 | LiteBIRD Mission Definition Review #2 | ISAS/JAXA |
| 2026-08-31 | SPT-3G D1 quadratic-estimator lensing | arXiv:2608.31136 |

## Not verified
<!-- key: not-verified -->

- The Planck Legacy Archive URL and the exact content of each Planck public
  release were not checked this session.
- The end date of ACT observations is given as 2022 on the basis of the
  DR6 data period (2017–2022); the decommissioning date was not read, and
  the statement that DR6 is the last ACT power-spectrum release rests on
  the collaboration's description of DR6, not on an explicit sentence read
  this session.
- CLASS band list and sky fraction were seen only in search snippets of
  other CLASS papers and are not quoted.
- The names and areas of the individual SPT-3G Summer and Wide fields and
  the number of Main-field seasons already taken were not tabulated from a
  cited source here.
- A first Simons Observatory data release was described as targeted for
  autumn 2026 in a conference talk found by web search; no official
  release page was read, and no release is asserted.
- Other operating or planned experiments (POLARBEAR/Simons Array, SPIDER,
  QUBIC, AliCPT, GroundBIRD, Taurus, PICO, CMB-HD) were not researched.
