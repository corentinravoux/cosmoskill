# Tensions and anomalies — data sets entering each and what they share

Scope: which data sets enter each tension and what is shared between them.

Snapshot: 2026-10-07

Flags as in `results.md`: `[src]` read this session in the cited paper;
`[sec: X]` taken from the reference files of sibling skill X; `[der]`
derived here. Instrument facts, release dates and access points live in
`cosmo-surveys-facilities`; sample definitions live in the probe skills.
This file answers one question per tension: are the inputs independent?

## 1. H0

| Input | Enters | Shared with | Flag |
|---|---|---|---|
| NGC 4258 maser distance | SH0ES, CCHP, H0DN, SBF zero point | the single anchor of both JWST ladders | [sec: h0] |
| Gaia EDR3/DR3 parallaxes of Milky Way Cepheids | SH0ES, H0DN | Gaia DR4 is planned for 2 December 2026; no current value uses it | [sec: h0] |
| LMC and SMC detached eclipsing binaries | SH0ES, H0DN | — | [sec: h0] |
| SN Ia calibrator hosts (55 in SH0ES 2025; 24 in CCHP) | SH0ES, CCHP, H0DN | the CCHP hosts are a subset of the nearby calibrators; the H0 gap between the two teams sits in the calibrator subsample and the SN compilation | [sec: h0] |
| Pantheon+ Hubble-flow supernovae, 0.023 < z < 0.15 | SH0ES, H0DN, the DESI DR1 peculiar-velocity H0 | also the low-redshift anchor of the w0wa fits (Section 4) | [sec: h0, de] |
| Planck PR3/PR4 | early endpoint; calibration and τ for ACT and SPT | every CMB-based endpoint | [sec: cmb] |
| ACT DR6, SPT-3G D1 | early endpoint | shape parameters independent of Planck; amplitude and τ not | [sec: cmb] |
| DESI DR2 BAO + BBN baryon density | early endpoint with no CMB anisotropies | BAO also enter the inverse ladder and every r_d-free H0 | [sec: h0] |
| Time-delay lenses (8 in TDCOSMO-2025) | one-step local value | Ω_m prior from supernovae | [sec: h0] |

Independence, in one sentence each.

- SH0ES, CCHP and H0DN are not three measurements: same anchor for JWST,
  overlapping hosts and Hubble-flow supernovae [sec: h0].
- The DESI DR1 Fundamental Plane + Tully–Fisher value (73.7) inherits the
  SH0ES/Pantheon+ zero point [sec: h0, pv].
- Planck, ACT and SPT share calibration and the τ prior; BAO + BBN is the
  early-side route that shares nothing with them except the standard
  pre-recombination physics that sets r_d [sec: cmb, h0].
- Megamasers and lenses are independent of the ladder but have errors of 3
  to 5 km/s/Mpc and central values that have moved with modelling choices
  [sec: h0].

## 2. S8

| Probe | Data | Shared ingredients | Flag |
|---|---|---|---|
| KiDS-Legacy cosmic shear | KiDS DR5, 1347 deg² | redshift calibration method changed from KiDS-1000 | [sec: wl] |
| DES Y6 cosmic shear and 3×2pt | ≈ 5000 deg², ≈ 140 million sources | same shear catalogue in both; CMB reference Planck 2018 + ACT DR6 + SPT-3G DR1 | [sec: wl] |
| HSC Y3 | 416 deg² | redshift distributions recalibrated with DESI clustering | [sec: wl] |
| unWISE × CMB lensing | ACT DR6 + Planck lensing maps | the lensing maps of the primary-CMB experiments | [sec: x] |
| DESI LRG × CMB lensing | same lensing maps; photometric DESI LRG sample | the several LRG papers use one galaxy sample | [sec: x] |
| tSZ × galaxies | Planck y map × SDSS, BOSS, eBOSS, DES, DESI tracers | one y map; the gas model of one simulation suite | [sec: x] |
| eRASS1 clusters | 5259 X-ray clusters over 12791 deg², western Galactic hemisphere; lensing from DES Y3, KiDS-1000 and HSC | lensing mass calibration from the shear surveys above | [sec: cl] |
| SPT clusters | 1005 SZ clusters, DES and HST lensing | DES shear | [sec: cl] |
| Planck PSZ2 clusters | 439-cluster cosmology sample, DES shear, Chandra | DES shear; Planck SZ map | [sec: cl] |
| KiDS-1000 AMICO clusters | about 8000 optical clusters, 839 deg² | KiDS-1000 shear and redshifts, the pre-Legacy calibration | [sec: cl] |

What is shared.

- Lensing mass calibration of every current cluster sample comes from DES,
  KiDS or HSC shear. A redshift-calibration error in a shear survey
  propagates to the cluster S8 calibrated on it. The KiDS AMICO result
  (0.74) uses KiDS-1000, whose cosmic-shear S8 rose by 0.056 with the
  Legacy recalibration [sec: wl, cl; the inference that the cluster value
  would follow is not tested in any paper read].
- CMB-lensing cross-correlations use the lensing maps of the experiments
  that define the CMB endpoint; they are tests of structure growth between
  z ≈ 0.3 and 2, not independent of the CMB lensing amplitude.
- The CMB endpoint is shared by all, and it moved (0.834 to 0.819 from
  Planck PR3 to PR4) [sec: cmb].
- Baryonic feedback enters cosmic shear at small scales and the tSZ and
  kSZ measurements directly; the feedback strength is itself disputed
  between probes [sec: wl, x].

## 3. CMB data combinations

Definitions as used by the collaborations [sec: cmb].

| Name | Content |
|---|---|
| Planck PR3 (Plik) | 2018 likelihoods; A_L = 1.180 ± 0.065 |
| Planck PR4 (HiLLiPoP + LoLLiPoP, or CamSpec) | NPIPE maps; reduced A_L |
| ACT DR6 | TT/TE/EE with Planck SRoll2 low-ℓ EE for τ |
| SPT-3G D1 | TT/TE/EE on the 2019–2020 main field + SPT lensing + τ prior |
| P-ACT | ACT DR6 + Planck cut at ℓ < 1000 (TT) and ℓ < 600 (TE, EE) + low-ℓ |
| CMB-SPA | SPT-3G D1 + ACT DR6 + Planck, with lensing |
| "CMB" in DESI papers | Planck with CamSpec rather than Plik, with ACT lensing added [sec: inf] |

What is shared: τ (Planck low-ℓ EE in every combination); absolute
calibration (ACT and SPT calibrate on Planck); sky (ACT overlaps Planck).
What is independent: the shape of the damping tail and of the polarisation
spectra, hence θ_*, Ω_b h², Ω_c h², n_s and N_eff. The A_L excess lives in
Planck TT at ℓ ≈ 1100–2000 and is absent from ACT and SPT; P-ACT removes
most of that range, CMB-SPA keeps it. The CMB–DESI discrepancy is smallest
for P-ACT (1.6σ) and largest for SPT + ACT (3.7σ) [sec: cmb].

## 4. BAO, SN and the w0wa preference

| Input | Content | Shared ingredients | Flag |
|---|---|---|---|
| DESI DR2 BAO | more than 14 million objects (DR1: over 6 million in seven redshift bins over 0.1 < z < 4.2), including the Lyα forest at z_eff = 2.33 | DR1 is a subset; SDSS BAO overlap in sky and redshift | [sec: de] |
| CMB | Section 3 | compressed priors (θ_*, ω_b, ω_bc) give 2.4σ, the full CMB 3.1σ; lensing adds the difference | [sec: de] |
| Pantheon+ | 2022 compilation, host masses corrected in 2026 | low-redshift sample shared with the others | [sec: de] |
| Union3 → Union3.1 | UNITY framework | shares most low-redshift supernovae with Pantheon+ | [sec: de] |
| DES-SN5YR → DES-Dovekie | DES photometric sample + external low-z; recalibrated November 2025 | external low-redshift sample | [sec: de] |
| Unite | 2884 SNe, Pantheon+ ∪ DES | one combined sample | [sec: de] |

The three supernova compilations are not independent confirmations: they
share the low-redshift anchor, and cutting z < 0.1 from Unite moves its
result by about 2σ [sec: de]. No dark-energy analysis at the snapshot uses a
modern, homogeneous low-redshift sample (ZTF, DEBASS and TITAN are pending;
`cosmo-supernovae`). The same Pantheon+ low-redshift supernovae set the
Hubble-flow intercept of the SH0ES ladder: one sample carries both the H0
intercept and the low-redshift end of the w0wa fits.

## 5. Cosmic dipole catalogues

All rows [src], from the abstracts read on 2026-10-10 (`results.md` §7).

| Catalogue | Band | Sample used | Used in |
|---|---|---|---|
| CatWISE2020 quasars | mid-infrared, 3.4 and 4.6 μm, WISE cryogenic to reactivation phases | 1.36 million (2021 selection); 1.6 million in the 2025 clustering analysis | arXiv:2009.14826, arXiv:2212.07733, arXiv:2511.00822, arXiv:2510.23769, arXiv:2607.25703 |
| NVSS | radio, NRAO VLA Sky Survey | radio galaxies; no objects shared with the WISE quasars | arXiv:2206.05624, arXiv:2503.02470, arXiv:2509.16732 |
| RACS-low | radio, Rapid ASKAP Continuum Survey | — | arXiv:2503.02470, arXiv:2509.16732 |
| LoTSS-DR2 | radio, low frequency, "the deepest wide-area survey" | — | arXiv:2509.16732 |
| TGSS-ADR1, WENSS, SUMSS | radio, a decade of frequencies with NVSS | amplitudes increase with decreasing frequency in a common-mask analysis | arXiv:2010.08366 |
| DESI DR1 BGS, LRG, ELG, QSO | spectroscopic, 0.1 < z < 2.1 | redshift dipole; 1,000 EZmocks | arXiv:2608.30914 |
| Pantheon+SH0ES supernovae | optical, low redshift | luminosity-distance multipoles | arXiv:2403.17741 |
| Planck 2013 temperature maps | CMB | aberration and modulation | arXiv:1303.5087 |

What is shared and what is not.

- NVSS radio galaxies and WISE quasars are "systematically independent and
  have no shared objects" (arXiv:2206.05624) [src]; this is the strongest
  point of the anomaly.
- All CatWISE analyses use one catalogue with a "known trend of the quasar
  number counts with ecliptic latitude" (arXiv:2510.23769) [src]. The five CatWISE papers of the table are five analyses of one data
  set.
- RACS is in "high discordance" with both CatWISE and NVSS in a Bayesian
  tension analysis, which its authors read as "a possible systematic
  difference in the RACS catalogue itself" (Land-Strykowski, Lewis & Murphy
  2025, abstract read this session; not in `sources.tsv`).
- Whether the radio amplitude depends on frequency is itself disputed:
  increasing with decreasing frequency in arXiv:2010.08366, "no evidence for
  any frequency dependence" in arXiv:2206.05624 [src].
- The DESI redshift dipole and the DESI number-count dipole come from the
  same catalogues and disagree; the authors attribute the count excess to
  footprint incompleteness (arXiv:2608.30914) [src].

## 6. Large-angle CMB maps

| Data | Use | Flag |
|---|---|---|
| WMAP temperature maps | the same large-angle features, "observed … both by WMAP and by Planck"; an independent instrument for the same sky | arXiv:1510.07929 [src] |
| Planck PR3 (2018), four component-separated maps: Commander, NILC, SEVEM, SMICA | reference analysis of isotropy and statistics in temperature and, for the first time, polarisation | arXiv:1906.02552 [src] |
| Planck PR4 (NPIPE) with end-to-end simulations | reanalyses of lack of power, hemispherical asymmetry, alignments | arXiv:2312.09989, arXiv:2406.11543, arXiv:2504.05597 [src] |
| Planck lensing map | test of the supervoid explanation of the Cold Spot | arXiv:2211.16139 [src] |

There is one temperature sky. WMAP and Planck agree on it, which excludes
instrument-specific artefacts and nothing else. All temperature analyses
are reanalyses of the same realisation with different masks, component
separations and statistics; their p-values are not independent, and the
spread between component-separation methods is a measure of the systematic
(the lower-tail probability of the lack of power is quoted as "≤" a value
"depending on the component separation method", arXiv:2312.09989) [src].
In polarisation the p-values vary between the four maps, which the collaboration reads as possibly "an
incomplete understanding of the noise properties of the data"
(arXiv:1906.02552, conclusions) [src].

## 7. JWST high-redshift samples

| Sample | Type | Flag |
|---|---|---|
| JWST early release NIRCam imaging: six candidates at 7.4 < z < 9.1 | photometric redshifts and SED masses | arXiv:2207.12446 [src] |
| FRESCO: 36 dust-obscured galaxies at z_spec = 5–9 | NIRCam slitless grism redshifts; a single dispersion angle with a single emission feature is the failure mode identified in arXiv:2602.03030 | arXiv:2309.02492 [src] |
| NIRSpec IFU + ALMA follow-up of S1 | multi-line redshift; revises one FRESCO object from z = 5.58 to 3.2439 | arXiv:2602.03030 [src] |
| Spectroscopically confirmed JWST and HST galaxies at 7 ≤ z ≤ 14, compiled for comparison with UniverseMachine on Uchuu | UV luminosity functions, M_*–SFR and M_*–M_UV relations | arXiv:2604.18683 [src] |

What is shared: the SED-fitting assumptions behind every stellar mass, and, for slitless samples, the contamination mode demonstrated by S1. JWST survey descriptions are not held in this suite; see `cosmo-reionization-21cm` for the reionisation side.

## 8. Shared ingredients across tensions

| Ingredient | Tensions it enters | Consequence |
|---|---|---|
| Planck low-ℓ EE (τ) | CMB–BAO discrepancy, w0wa, neutrino mass, n_s, S8 reference through A_s | a "single-point failure" in the words of arXiv:2504.16932 [sec: cmb]; τ ≈ 0.09 would reduce the w0wa preference to about 1.5σ and remove the neutrino tension |
| Planck high-ℓ TT smoothing | A_L, Ω_K < 0, Σ0 in modified-gravity fits, part of the neutrino-mass preference | one feature, four parameters [sec: cmb, inf, de] |
| Ω_m mismatch between DESI BAO (0.2975 ± 0.0086) and the CMB (0.3175 ± 0.0055 for CMB-SPA) | CMB–BAO discrepancy, w0wa, negative neutrino mass, Ω_K > 0, the rise of n_s in CMB + BAO fits, the limit on modified-recombination models | one mismatch read in six ways [sec: cmb, de, nu, inf; arXiv:2606.06495 src] |
| Low-redshift supernovae (z < 0.1) | H0 intercept, w0wa, supernova dipole | the same objects anchor the ladder and tilt the dark-energy fit [sec: h0, de] |
| Shear-survey redshift calibration | cosmic-shear S8, cluster S8, 3×2pt | the 2025 recalibrations moved cosmic shear by 0.04–0.06 [sec: wl] |
| Baryonic feedback model | cosmic-shear S8, tSZ S8, kSZ, cluster gas | disputed strength [sec: wl, x] |
| CMB dipole read as kinematic | number-count dipole, supernova dipole, bulk-flow frame, every redshift converted to the CMB frame | the frame assumption behind all low-redshift distances |
| Peculiar-velocity reconstruction of the local volume (2M++, Manticore) | megamaser H0, two-rung ladders, local-void tests, zero-point dipoles | the same reconstructions adjudicate several local claims [sec: h0, pv] |
| Mock catalogues | bulk-flow errors, parity-odd 4PCF, dipole null distribution, CMB anomalies | each claimed significance fell when mocks were made more realistic (`results.md` §12) |

The table is the main reason not to count anomalies: the list in
`results.md` §0 has fifteen rows and perhaps six independent facts (the
ladder calibration, the Ω_m mismatch, the Planck TT smoothing feature, the
low-redshift amplitude spread, the quasar and radio count dipole, the CMB
temperature sky at ℓ < 30).

## 9. Next data

Dates are those held by the siblings [sec]; none is a forecast of a result.

| Data | Bears on | When | Source |
|---|---|---|---|
| Gaia DR4 | parallax zero point of the Milky Way anchor | planned 2 December 2026 | `cosmo-distance-ladder-h0` |
| DESI full-survey BAO and full shape (survey completed April 2026) | Ω_m mismatch, w0wa, neutrino mass | results expected in 2027 | `cosmo-galaxy-clustering` |
| Euclid DR1 (lensing and clustering products) | S8 with an independent Stage-IV shear survey | mid-2027, tentative; DR1-Foundation on 12 November 2026 is not the lensing release | `cosmo-surveys-facilities`, `cosmo-weak-lensing` |
| Rubin LSST (survey began 30 June 2026) | S8; a homogeneous supernova sample | DR1 will use the first year of data | `cosmo-surveys-facilities` |
| Simons Observatory | peak smoothing and lensing at Planck-level precision without Planck TT [inference from the data combinations of Section 3, not a statement of the collaboration] | no public data at the snapshot | `cosmo-surveys-facilities` |
| LiteBIRD (one telescope, launch JFY2036) | cosmic-variance-limited τ; large-angle E modes; birefringence | 2036 or later | `cosmo-cmb` |
| CLASS (ground, 90 GHz) | independent τ, currently ± 0.018 | ongoing | `cosmo-cmb` |
| SKA radio continuum surveys | the count dipole with O(10⁶) radio sources | no date held | arXiv:2607.25703 abstract names SKA, LSST and Euclid as the next stage [src] |
| 4MOST Hemisphere Survey (Fundamental Plane), DESI PV later releases | bulk flow at 120–160 h⁻¹Mpc without 6dFGS; local void | after 4MOST science operations start | `cosmo-peculiar-velocities` |
| ZTF, DEBASS, TITAN low-redshift supernovae | the z < 0.1 anchor of w0wa and of the ladder intercept | pending | `cosmo-supernovae` |

CMB-S4 was cancelled on 9 July 2025 [sec: cmb]; forecasts that rely on it
(τ-independent neutrino mass, hemispherical variance in polarisation) no
longer describe a planned experiment.

## Not verified

- Sample sizes and flux cuts of NVSS, RACS-low and LoTSS-DR2 as used in the
  dipole papers (not in the abstracts read).
- The sky fraction, mask and number of sources of the 2025–2026 WISE AGN
  reselection (a 2026 paper titled "Dipole Anisotropy in Newly Sampled AGN
  Population: Still in Tension with CMB Dipole" was seen in a search and not
  read).
- Whether any analysis has propagated the KiDS-Legacy redshift
  recalibration to the KiDS AMICO cluster result.
- JWST survey areas and depths.
