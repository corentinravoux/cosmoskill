# Surveys and data — statistics beyond the two-point function

Scope: the data sets, void catalogues, simulation suites and mock challenges on which beyond-two-point analyses have been run or validated.
Snapshot: 2026-10-13


## 1. Spectroscopic samples used for higher-order clustering
<!-- key: spectroscopic-samples-used-for-higher-order -->

Survey descriptions (instrument, footprint, release dates) are in
`cosmo-galaxy-clustering`, file `references/surveys-and-data.md`. The rows
below give only what the beyond-two-point analyses used.

| Data | Sample used | Statistic | Reference |
|---|---|---|---|
| BOSS DR11 CMASS | 690 827 galaxies, 0.43 < z < 0.70, 8 498 deg², V_eff ≈ 6 Gpc³ [src: abstract] | P0, P2 + B0 | arXiv:1407.5668 |
| BOSS DR12 LOWZ, CMASS | 361 762 galaxies at z_eff = 0.32 and 777 202 at z_eff = 0.57 [src: abstract] | P + B0 | arXiv:1606.00439 |
| BOSS DR12 (four data segments) | Window-free P_ℓ, B0, and B2, B4 | P + B multipoles | arXiv:2112.04515, arXiv:2302.04414 |
| BOSS DR12 LOWZ, CMASS | 280 067 LRGs at z̄ = 0.32 and 803 112 at z̄ = 0.57 [src: abstract] | Parity-odd 4PCF | arXiv:2206.03625 |
| DESI DR1 LRG (three bins) and QSO | 0.4 ≤ z ≤ 2.1 [src: abstract of arXiv:2503.09714] | P + B0, ShapeFit | arXiv:2503.09714, arXiv:2603.19356 |
| DESI DR1, six tracers, public catalogues | P_ℓ (ℓ = 0, 2, 4) + B0 | Independent EFT reanalysis | Chudaykin, Ivanov & Philcox 2025, arXiv:2507.13433 |
| DESI DR1 LRG ×3 + QSO | P one loop + B tree level in TripoSH basis | arXiv:2610.01836 |
| DESI DR1 LRG | Parity-odd 4PCF, auto and cross between sky patches | Slepian et al. 2025, arXiv:2508.09133 |
| SDSS DR16 Lyα forest | Parity-odd 4PCF of the forest | Adari & Slosar 2024, arXiv:2405.04660 |

The two BOSS DR12 counts differ between arXiv:1606.00439 and arXiv:2206.03625
because the papers apply different cuts; quote the count with the paper.

Mock sets that matter for the covariance of higher-order statistics:
MultiDark-Patchy (2048 approximate mocks, used by BOSS; arXiv:1712.04970 quotes
the number in its abstract) and GLAM-Uchuu (N-body, 2000³ particles [src: abstract]; Philcox & Ereza
2024, arXiv:2401.09523). The choice between them changes the parity-odd result
(`systematics.md` §1.3).

## 2. Void catalogues and the data behind them
<!-- key: void-catalogues-and-the-data-behind-them -->

| Catalogue | Tracer and volume | Voids | Finder | Reference |
|---|---|---|---|---|
| BOSS DR12 CMASS stacked voids | Radii 30–100 h⁻¹Mpc, 0.43 < z < 0.7; 1000 mocks [src] | not given in abstract | ZOBOV | Mao et al. 2016, arXiv:1602.06306 |
| BOSS DR12 (Hamaus) | Full void sample at mean z = 0.51 [src] | not given in abstract | not given in abstract | arXiv:2007.07895 |
| eBOSS DR14 LRG, QSO | z = 0.703 and 1.53 [src]; QSO catalogue possibly heavily contaminated by Poisson voids | not given in abstract | ZOBOV-based | Hawken et al. 2020, arXiv:1909.04394 |
| eBOSS DR16 LRG+CMASS, ELG, QSO | 0.6 < z < 2.2 [src: abstract] | 2 814, 1 801, 4 347 [src: abstract] | ZOBOV-based | Aubert et al. 2022, arXiv:2007.09013 |
| eBOSS DR16 LRG + CMASS z > 0.6 tail | 0.6 < z < 1.0, z_eff = 0.69 [src] | not given in abstract | reconstruction + watershed | arXiv:2008.06060 |
| SDSS MGS + BOSS + eBOSS LRG | 0.07 < z < 1.0, six redshift bins [src] | not given in abstract | reconstruction + watershed | arXiv:2205.06258 |
| BOSS DR16 non-spherical voids | 0.2 < z < 0.8, two bins [src] | not given in abstract | Voronoi + watershed, ellipticity cut | arXiv:2501.07817 |
| DESIVAST (DESI DR1 BGS, volume limited) | z < 0.24 [src: abstract] | 1 461 (VoidFinder), 420 (V² REVOLVER), 295 (V² VIDE) [src: abstract] | VoidFinder, V² | arXiv:2411.00148 |
| DESI Legacy Survey DR9 LRG (photometric) | ≈ 19 500 deg², ≈ 10 million LRGs, voids at 0.35 < z < 0.95 [src] | not given in abstract | 3D voids with photo-z | arXiv:2412.02761 |
| CLAMATO (Keck/LRIS, COSMOS) | 240 sightlines, 0.16 deg², 2.5 h⁻¹Mpc, 3.15 × 10⁵ h⁻³Mpc³ [src: abstract of arXiv:1710.02612]; DR2: 320 objects, ≈ 0.2 deg², 2.05 < z < 2.55 [src: abstract of arXiv:2109.09660] | void volume fraction 19.5% (data), 18.2% (simulation) [src: abstract of arXiv:1710.02612] | spherical overdensity | arXiv:1710.02612, arXiv:2109.09660 |
| eBOSS Stripe 82 Lyα tomography | 220 deg², 37 quasars deg⁻², 0.94 h⁻³Gpc³, 13 h⁻¹Mpc [src: abstract] | void and protocluster catalogue | finder applied to the Wiener-filtered map | arXiv:2004.01448 |

The DESIVAST paper reports "significant differences in the void volume overlap"
with an SDSS catalogue of the same region, attributed to galaxy selection and
masks (arXiv:2411.00148): a void catalogue is a property of the survey as much
as of the sky.

Planned. Euclid spectroscopic survey: 15 000 deg², 0.9 < z < 1.8, tens of
thousands of voids expected [src: abstract] (arXiv:2205.11525). Future tomography
surveys are covered in `cosmo-lyman-alpha`.

Not found in searches this session: a DESI DR1 or DR2 void–galaxy AP/RSD
cosmology paper. Treat its existence as unverified.

## 3. Simulation suites and mock challenges behind emulator-based statistics
<!-- key: simulation-suites-and-mock-challenges-behind -->

| Suite or challenge | Content | Used for | Reference |
|---|---|---|---|
| Quijote | 44 100 N-body simulations, more than 7 000 cosmologies in {Ω_m, Ω_b, h, n_s, σ8, M_ν, w}, 1 h⁻¹Gpc boxes, 256³–1024³ particles; a petabyte of public products [src: abstract] | Fisher information content; training of SimBIG | arXiv:1909.05273 |
| AbacusSummit | N-body suite used for the DSC, WST, MF and kNN emulators; 25 boxes totalling 200 h⁻³Gpc³ used for the trispectrum test [src: abstract of arXiv:2610.08908, for the latter] | Emulators with HOD galaxies | as used in arXiv:2309.16539, arXiv:2310.16116, arXiv:2501.01698, arXiv:2610.08908 |
| SimBIG forward model | Quijote N-body + flexible halo occupation + BOSS CMASS survey realism (angular mask, fibre collisions); 20 000 training catalogues, 2 000 test simulations in the WST analysis [src: abstract of arXiv:2310.15250] | Simulation-based inference on BOSS CMASS | arXiv:2211.00660, arXiv:2310.15250 |
| Beyond-2pt challenge | Parameter-masked HOD mocks: real space, redshift space, light cone at 0.8 < z < 1.3; public | Blind validation of eight pipelines | arXiv:2405.02252, Sects. I–II |

The reference paper for AbacusSummit itself was not fetched this session; it
is cited here only through the analyses that use it.

All survey-data applications of DSC, WST and MFs read this session use one
sample: BOSS DR12 CMASS in a narrow range: 0.45 < z < 0.6 for DSC (arXiv:2309.16541, Sect. 2.1), 0.46 < z < 0.57 for WST (arXiv:2310.16116, abstract), 0.45 < z < 0.58 for MFs (arXiv:2501.01698, abstract). No application to DESI data was found.

Reference papers of the suites (abstracts read 2026-10-13). AbacusSummit:
139 boxes of 2 h⁻¹Gpc at particle mass 2 × 10⁹ h⁻¹M_⊙ over 97 cosmologies,
plus 1883 boxes of 500 h⁻¹Mpc for covariances [src: abstract] (Maksimova et al. 2021,
arXiv:2110.11398). CosmoGridV1: 2500 wCDM grid points with 7 PKDGRAV3
simulations each, 200 at the fiducial cosmology, with a shell-based baryon
correction [src: abstract] (Kacprzak et al. 2022, arXiv:2209.04662). PT Challenge:
blinded BOSS-like mocks of a hundred times the BOSS volume [src: abstract] (Nishimichi
et al. 2020, arXiv:2003.08277).

## 4. Lensing data sets used for higher-order statistics
<!-- key: lensing-data-sets-used-for-higher-order -->

Survey descriptions are in `cosmo-weak-lensing`. Used here:

| Data | What was used | Reference |
|---|---|---|
| KiDS-450 | Shear peaks from aperture-mass maps; first CNN map analysis | arXiv:1709.07678, arXiv:1906.03156 |
| KiDS-1000 | Graph-convolutional network on maps, wCDM, CosmoGrid simulations | arXiv:2201.07771 |
| KiDS-Legacy | COSEBIs at 2′–300′ plus ⟨M_ap³⟩ at 4′–32′ [src: abstract] | arXiv:2606.12389 |
| HSC Y1 | Tomographic peaks over ≈ 58 deg² [src: abstract of arXiv:2210.07853]; 19 sub-fields of 3 × 3 deg² for the CNN [src: abstract of arXiv:2301.01354]; PDF, peaks, minima, MFs, scattering transform | arXiv:2210.07853, arXiv:2301.01354, arXiv:2409.01301, arXiv:2404.16085, arXiv:2410.00401 |
| HSC Y3 | ξ± plus ⟨M_ap³⟩ | arXiv:2508.14019 |
| DES Y3 | 4 139 deg² effective area [src: abstract of arXiv:2110.10141]; moments; ξ± plus ⟨M_ap³⟩ in four source bins; SBI with peaks, CNN, scattering transform, wavelet phase harmonics, persistent homology, hybrid statistics | arXiv:2110.10141, arXiv:2508.14018, arXiv:2403.02314, arXiv:2405.10881, arXiv:2506.13439, arXiv:2606.11309 |
| Gower Street simulations | 791 full-sky PKDGRAV runs, over 3 000 DES Y3 mocks [src: abstract] | arXiv:2403.02314 |

Next: the DES team states the intention to apply the hybrid SBI analysis to
DES Y6 (arXiv:2606.11309). No higher-order lensing cosmology from DES Y6,
Euclid or Rubin was found this session.

## 5. Data used in field-level and simulation-based inference
<!-- key: data-used-in-field-level-and-simulation-based -->

| Data | Use | Reference |
|---|---|---|
| 2M++ galaxy compilation | BORG particle-mesh reconstruction of the nearby Universe; Manticore-Local constrained simulations | arXiv:1806.11117, arXiv:2505.10682 |
| SDSS-III/BOSS | BORG density reconstruction with foreground-template marginalisation | arXiv:1909.06396 |
| Quaia quasars (G < 20.0 and G < 20.5) | BORG reconstruction over (10 h⁻¹Gpc)³ at 39.1 h⁻¹Mpc resolution [src: abstract] | arXiv:2602.02363 |
| BOSS CMASS subsample (≈ 10% of the BOSS volume; arXiv:2310.15243, abstract) | SimBIG: P_ℓ, B0, CNN, WST, marked P | arXiv:2310.15243, arXiv:2310.15246, arXiv:2310.15256, arXiv:2404.04228 |
| DESI DR1 LRG (LRG1, LRG2, LRG3) | Neural field-level BAO reconstruction (LiFT) | arXiv:2609.14862 |
| Simulated ZTF 6-year SNe Ia + DESI DR3 BGS | Gaussian field-level fσ8 **forecast** with flip | Ravoux et al. 2026, arXiv:2609.34508 |
| Quijote halo catalogues | Field-level f_NL^loc test | arXiv:2603.20855 |
| Simulated halos, 8 (h⁻¹Gpc)³, rest frame | LEFTfield σ8 test | arXiv:2403.03220 |

Public products: Manticore-Local posterior realisations and the Quaia
reconstruction maps are described as data products in their papers; locations
were not checked this session.

## 6. Validation by mock challenge
<!-- key: validation-by-mock-challenge -->

### 6.1 The Beyond-2pt challenge
<!-- key: the-beyond-2pt-challenge -->

Design, from §2 of arXiv:2405.02252. HOD galaxy mocks on N-body simulations in
flat ΛCDM, without observational systematics, at three levels: real-space
snapshot (10 realisations, z = 1), redshift-space snapshot (10 realisations,
z = 1), and one light-cone mock (0.8 < z < 1.3, simple footprint) whose
effective volume is similar to the BOSS DR12 LRG sample [src: Sect. II]. Cosmology and
HOD were hidden ("parameter masking"); teams froze scale cuts and priors,
submitted posteriors, and the organisers then unmasked the fractional distance
to the truth.

Participants and their ingredients [src, Table 1 of arXiv:2405.02252]:

| Method | Mocks analysed | Gravity model | Tracer model | Covariance |
|---|---|---|---|---|
| BACCO P (hybrid-EFT emulator) | all | N-body | hybrid EFT | analytic + emulator |
| Density split | redshift space | N-body | HOD | 1 500 mocks + emulator |
| EFT field-level Bayesian inference (LEFTfield) | real space | perturbative | EFT | analytic |
| EFT P + B | all | perturbative | EFT | analytic |
| kNN | redshift space | N-body | HOD | jackknife + emulator |
| SBI P + B | redshift space | N-body | HOD | not applicable |
| Void–galaxy correlation function | light cone | perturbative | linear bias | jackknife |
| Void size function | light cone | perturbative | linear bias | analytic |

What the challenge does and does not establish, in the paper's own terms:

- On the redshift-space mocks all teams recovered the input Ω_m–σ8 within
  their 1σ region. Results are the mean of 10 realisations with the covariance
  of one (2 h⁻¹Gpc)³ box, so that a ≥ 1σ shift from cosmic variance has
  probability 0.16% [src: arXiv:2405.02252, Sect. II]; a bias would indicate model misspecification.
- It does **not** establish that reported uncertainties are correct, "
  particularly relevant for small-scale analyses and simulation-based methods,
  based on empirical galaxy–halo connection parameterizations and priors", and
  it is not a ranking of methods: priors differ between all analyses.
- Field-level inference took part only on the real-space mock, with all
  cosmological parameters except σ8 fixed to the truth.
- On the light cone, both void methods and EFT P + B recovered Ω_m within 95%
  CL (arXiv:2405.02252, Sect. II.2); the paper reports recovery of σ8 only for the EFT pipeline. The VSF analysis used
  informative priors (three times the Planck 2018 width) on h, ω_b and n_s,
  and the truth lay outside that prior.
- After unmasking, the BACCO team traced a parameter bias to an
  underestimated emulation uncertainty of the hexadecapole, unnoticed on
  smaller volumes.
- The mocks are HOD-based. Methods that assume an HOD were therefore tested
  on their own model family.

### 6.2 Other validation standards
<!-- key: other-validation-standards -->

- **SimBIG mock challenge.** 1 500 test simulations built with a different
  N-body code, halo finder and occupation model from the training set; for the
  power spectrum to k_max = 0.5 h Mpc⁻¹ the Ω_m and σ8 posteriors are unbiased
  but conservative (Hahn et al. 2023, arXiv:2211.00660, abstract).
- **PT Challenge and large-volume N-body tests** for EFT pipelines (used in
  arXiv:2302.04414; 200 h⁻³Gpc³ in arXiv:2610.08908, abstract).
- **Recovery tests at inflated volume** for emulators: the DSC pipeline
  recovers unbiased parameters in a volume 84 times that of CMASS [src: abstract] (arXiv:2309.16541).
- **External mocks with a non-HOD galaxy model**, used by the MF analysis
  (arXiv:2501.01698).

## 7. Status today and what comes next
<!-- key: status-today-and-what-comes-next -->

| Item | Status at the snapshot | Source |
|---|---|---|
| DESI bispectrum | DR1 only; three pipelines published between March 2025 and October 2026 | arXiv:2503.09714, arXiv:2507.13433, arXiv:2610.01836 |
| DESI voids | DR1 BGS void catalogue (DESIVAST) published; no void–galaxy cosmology found | arXiv:2411.00148 |
| DESI field-level | Neural BAO reconstruction of DR1 LRGs by an external group | arXiv:2609.14862 |
| DES higher-order lensing | Y3 complete in several statistics; Y6 announced | arXiv:2606.11309 |
| KiDS | Legacy 2+3-point published June 2026 | arXiv:2606.12389 |
| Euclid voids | **Forecasts** only, for the 15 000 deg² spectroscopic survey | arXiv:2205.11525, arXiv:2302.05302 (both abstract) |
| DESI survey and Euclid DR1 dates | DESI completed its planned survey in April 2026, full-survey results expected in 2027; Euclid DR1 clustering products mid-2027 | [sec] `cosmo-galaxy-clustering` SKILL.md, not re-checked |
