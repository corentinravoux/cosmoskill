# Machine learning in cosmology — training sets, benchmarks and challenges

Scope: the simulation suites used as training sets, the benchmark suites and data challenges, and the survey applications of machine learning.
Snapshot: 2026-10-17

Flags: as in `physics-and-methods.md`.

## 1. Training-set simulation suites
<!-- key: training-set-simulation-suites -->

Suites designed to train or test machine-learning methods. The physics and
accuracy of the simulations themselves (N-body agreement, baryonic
suppression per suite) are in `cosmo-simulations-mocks`; this table records
what makes each a training set.

| Suite | Content | Design for ML | Reference |
|---|---|---|---|
| Quijote | 44 100 N-body runs, more than 7000 models in {Ω_m, Ω_b, h, n_s, σ8, M_ν, w}; 256³, 512³ or 1024³ particles in 1 h⁻¹Gpc; more than 35 million core hours; about a petabyte released with halo and void catalogues and millions of summary statistics | built for information-content studies (Fisher derivatives) and to "provide enough data to train machine learning algorithms" | Villaescusa-Navarro et al. 2020, arXiv:1909.05273 [src: abstract] |
| CAMELS | 4233 runs of (25 h⁻¹Mpc)³: 2184 (magneto-)hydrodynamic with AREPO (IllustrisTNG model) and GIZMO (SIMBA model), 2049 N-body; Ω_m, σ8 and four feedback parameters | "the largest suite of cosmological (magneto-)hydrodynamic simulations designed to train machine learning algorithms"; the two sub-grid families give significantly different baryon fractions and P(k) suppression, which makes cross-model tests possible | Villaescusa-Navarro et al. 2021, arXiv:2010.00619 [src: abstract] |
| CAMELS Multifield Dataset (CMD) | hundreds of thousands of 2D maps and 3D grids of gas, dark matter and stars from 2000 simulated universes; more than 70 TB | parameter inference posed as a community challenge | Villaescusa-Navarro et al. 2022, arXiv:2109.10915 [src: abstract] |
| CAMELS-CROCODILE | GADGET SPH with the Osaka feedback model, 25 and 50 h⁻¹Mpc boxes, one-parameter, cosmic-variance and Sobol sets over 26 parameters | an independent sub-grid implementation to train and test across galaxy-formation models; its fiducial P(k) suppression is a few per cent against up to ~27% for IllustrisTNG at z = 0 | Nagamine et al. 2026, arXiv:2609.23982 [src: abstract] |
| CAMELS SB35 (as used by BIND) | 1024 paired hydrodynamical and dark-matter-only 50 h⁻¹Mpc runs over 35 parameters | paired runs for learned baryon painting | arXiv:2609.10709 [src: abstract] |
| CosmoGridV1 | PkdGrav3 light-cones; 2500 Sobol grid points in wCDM (Ω_m, σ8, w0, H0, n_s, Ω_b), 7 runs each, 69 particle shells at n_side = 2048 to z = 3.5; 200 fiducial runs with stencil derivatives; 28 benchmark runs with larger boxes and resolution; map-level baryon correction | map-level inference for Stage-III photometric surveys; the benchmark runs test sensitivity to simulation choices | Kacprzak et al. 2023, arXiv:2209.04662 [src: abstract] |
| CAMELS second generation | 1192 IllustrisTNG-model runs in (50 h⁻¹Mpc)³ over 35 cosmological, astrophysical and numerical parameters, eight times the volume of the first generation | MLPs, CNNs, GNNs and Gaussian processes on P(k), maps, galaxy graphs and halo thermodynamics; constraints tighten with volume but more weakly than the square root of the volume | Genel et al. 2026, arXiv:2606.10038 [src: abstract] |
| Gower Street | 791 full-sky PKDGRAV runs with parameters chosen by mixed active learning; more than 3000 DES Y3 mocks | DES Y3 neural-compression SBI | arXiv:2403.02314 [src: abstract] |

## 2. Benchmark suites and data challenges
<!-- key: benchmark-suites-and-data-challenges -->

### 2.1 Time-domain classification challenges
<!-- key: time-domain-classification-challenges -->

| Challenge | Organisers, dates | Data | Outcome | Reference |
|---|---|---|---|---|
| PLAsTiCC | Kaggle, 28 September – 17 December 2018; 1094 teams; winners in February 2019 | simulated LSST light curves of 18 transient and variable models (released after the challenge), LSST Operations Simulator cadence, SNANA fluxes; small, bright, non-representative training set; test set of 3.5 million objects; an unseen "Other" class in the test set | top three: boosted trees with GP augmentation (Boone), and two ensembles of trees and neural networks | Kessler et al. 2019, arXiv:1903.11756 [src: abstract]; Hložek et al. 2020, arXiv:2012.12392 [src: Sect. 3.2] |
| ELAsTiCC (Extended LSST Astronomical Time-Series Classification Challenge) | organisers not read here; used by the Fink broker and by LSST DESC papers | about 0.5 million events used for ORACLE training; 19 classes including SN sub-types, AGN, variable stars, microlensing and kilonovae | ORACLE macro-averaged top-level precision 0.96 after 1 day, > 0.99 after 64 days, 0.83 for the 19-way task at 1024 days; Fink CATS ≥ 93% precision for all classes but "long" (~83%) | arXiv:2501.01496 [src: abstract]; arXiv:2404.08798 [src: abstract] |
| ELAsTiCC-based SN Ia cosmology simulation | LSST DESC | ~6000 photometrically classified SNe Ia with host photo-z in ~50 deg² of Deep Drilling Fields plus a spectroscopic low-z sample; SCONE + BBC | w0wa figure of merit about 150 against 54 for DES 5-year; "small but significant biases" over 25 samples (**forecast**) | Mitra et al. 2025, arXiv:2512.06319 [src: abstract] |
| Strong Gravitational Lens Finding Challenge | open challenge | 100 000 candidate images | several methods find more than half the lenses above thresholds with zero false positives, better than human inspection | arXiv:1802.03609 [src: abstract] |

### 2.2 Image tasks with survey data
<!-- key: image-tasks-with-survey-data -->

| Task | Data | Outcome | Reference |
|---|---|---|---|
| Giant arcs in clusters with Mask R-CNN (ARTEMIDE) | trained and validated on over 4500 simulated images (mock sources injected in Euclidised HST images of 10 lensing clusters), tested on 500 simulations and Euclid Q1 | precision 76%, recall 58% on the test set; 66% of visually confirmed Q1 arcs above the training area threshold recovered; false positives and faint arcs remain the limitation | Euclid Collaboration 2025, arXiv:2511.03064 [src: abstract] |
| Active anomaly search in Euclid images | 10 000 images, hybrid of Protege and PineForest | 799 unusual objects, including 29 strong-lens systems and candidates (9 absent from the published Q1 lens catalogues searched) and 202 ring galaxies | arXiv:2609.36096 [src: abstract] |

### 2.3 Cosmological-inference challenges
<!-- key: cosmological-inference-challenges -->

| Challenge | Data | What it tests | Reference |
|---|---|---|---|
| Beyond-2pt mock data challenge (first round) | parameter-masked mock galaxy catalogues in real space, redshift space and on a light cone, from the Aspen 2022 programme | unbiased recovery of masked ΛCDM parameters by density split, kNN, BACCO emulator, voids, LEFTfield, P + B with EFT and with SBI; data public, open to new entries | Beyond-2pt Collaboration 2024, arXiv:2405.02252 [src] |
| FAIR Universe Weak Lensing ML Uncertainty Challenge | HSC-Y3-like convergence maps (WIDE12H subfield, second tomographic bin, 2 arcmin pixels) from 101 flat-ΛCDM models in (Ω_m, S8); 256 noiseless maps of 1424 × 176 pixels per model; baryons through an HMcode transfer function (T_AGN in [7.2, 8.5], f0 in [0, 0.0265]); photo-z shift Δz with σ = 0.022; shape noise for n_g = 30 arcmin⁻² added in training | Phase 1: parameters and uncertainties with a limited training set; Phase 2: out-of-distribution detection | Dai et al. 2026, arXiv:2604.14451 [src: Sect. 2, Table 1] |
| CAMELS Multifield Dataset | as above | parameter inference from multi-field maps | arXiv:2109.10915 [src] |

Simulations of the FAIR Universe set combine MP-Gadget for 0 < z < 0.45
(320 h⁻¹Mpc, 960³) and FastPM for 0.45 < z < 2.72 (704 and 1536 h⁻¹Mpc)
[src: Table 1, arXiv:2604.14451]: the challenge itself mixes simulators.

## 3. Survey applications
<!-- key: survey-applications -->

Where machine learning enters a survey analysis, and which collaboration
documents it. Cosmological values belong to the probe skills.

| Survey | ML component | Status | Reference |
|---|---|---|---|
| LSST DESC | white paper: AI/ML across photo-z, transient classification, lensing inference and simulations; priorities are Bayesian inference at scale, physics-informed methods, validation frameworks and active learning; foundation models and LLM agents only "coupled with rigorous evaluation and governance" | planning | LSST DESC 2026, arXiv:2601.14235 [src] |
| DES Y3 | lensing-map SBI with CNN compression (Gower Street) | data result, wCDM | arXiv:2403.02314 [src] |
| DES Y3 | weak lensing + clustering maps, graph CNNs on the full footprint trained on over one million CosmoGridV1 mocks, normalising-flow likelihood in ten parameters, validated on Buzzard; 2–3 times higher Ω_m–S8 figure of merit than its two-point baseline (**forecast**) | analysis design; data analysis announced | Thomsen et al. 2025, arXiv:2511.04681 [src] |
| KiDS-1000 | GCNN map-level analysis on CosmoGrid; SBI of pseudo-C_ℓ | data results | arXiv:2201.07771 [src]; arXiv:2404.15402 [src] |
| HSC Y1 | CNN on 19 sub-fields of 3 × 3 deg² in four bins | data result | arXiv:2301.01354 [src: abstract] |
| KiDS-Legacy | multi-fidelity field-level SBI | mock analysis | arXiv:2606.23346 [src] |
| DES 5-year SNe | SuperNNova classification in BEAMS; NPE population model | data results; see `cosmo-supernovae` | arXiv:2607.28725 [src] |
| DESI | neural BAO reconstruction of DR1 LRGs by an external group; outlier detection in EDR BGS | see `cosmo-beyond-two-point`; arXiv:2307.07664 [src] | — |
| Rubin alert brokers | Fink classifiers and anomaly detection; ORACLE | operating on ZTF; tested on ELAsTiCC | arXiv:2404.08798 [src]; arXiv:2603.29511 [src]; arXiv:2501.01496 [src] |

## 4. Reviews by probe
<!-- key: reviews-by-probe -->

| Probe or method | Review | Reference |
|---|---|---|
| Deep learning for galaxy surveys (all probes) | a Dawes review | Huertas-Company & Lanusse 2022, arXiv:2210.01813 |
| Machine learning in cosmology, community plan | Snowmass 2021 white paper | Dvorkin et al. 2022, arXiv:2203.08056 |
| Simulation-based inference | general review; pedagogical chapter | arXiv:1911.01429; Thiele 2026, arXiv:2605.10719 |
| Weak lensing | estimators, limits of traditional analyses, ML remedies | Shirasaki 2026, arXiv:2605.12877 [src] |
| Lyman-α forest | absorber characterisation, continuum reconstruction, emulators of hydrodynamics, SBI, field-level and 3D reconstruction | Chaves-Montero 2026, arXiv:2605.22489 [src] |
| LSST DESC programme | AI/ML across probes; priorities and risks | arXiv:2601.14235 |

Photometric-redshift machine learning has its own reviews and challenges,
listed in `cosmo-photometry-photoz`. The 2026 chapters by Thiele and
Chaves-Montero belong to one series titled "Machine Learning Techniques for
Astrophysics and Cosmology" (titles of arXiv:2605.10719 and
arXiv:2605.22489) [src].

## 5. Public code and data locations
<!-- key: public-code-and-data-locations -->

Locations as stated in the abstracts read; versions and maintenance belong
to `cosmo-software-ecosystem`.

| Resource | Location stated | Reference |
|---|---|---|
| CosmoPower | github.com/alessiospuriomancini/cosmopower | arXiv:2106.03846 [src] |
| CONNECT | github.com/AarhusCosmology | arXiv:2205.15726 [src] |
| pydelfi | github.com/justinalsing/pydelfi | arXiv:1903.00007 [src] |
| LtU-ILI | github.com/maho3/ltu-ili | arXiv:2402.05137 [src] |
| Stjörnumál (SN Ia population SBI) | github.com/bap37/Stjornumal | arXiv:2607.28725 [src] |
| SCONE | github.com/helenqu/scone | arXiv:2106.04370 [src] |
| SuperNNova | github.com/supernnova/SuperNNova | arXiv:1901.06384 [src] |
| ORACLE | github.com/uiucsn/ELAsTiCC-Classification | arXiv:2501.01496 [src] |
| DASH | pip install astrodash; astrodash.readthedocs.io | arXiv:1903.02557 [src] |
| Astronomaly | github.com/MichelleLochner/astronomaly | arXiv:2010.11202 [src] |
| ARTEMIDE | github.com/LBasz/ARTEMIDE (announced) | arXiv:2511.03064 [src] |
| PLAsTiCC model libraries | Zenodo record 2612896 (as printed in the abstract) | arXiv:1903.11756 [src] |
| CosmoGridV1 | www.cosmogrid.ai | arXiv:2209.04662 [src] |
| CAMELS Multifield Dataset | camels-multifield-dataset.readthedocs.io | arXiv:2109.10915 [src] |
| CAMELS second generation | camels.readthedocs.io | arXiv:2606.10038 [src] |
| BIND models and generated haloes | released (location not read) | arXiv:2609.10709 [src] |
| Beyond-2pt challenge data | public, open to new submissions | arXiv:2405.02252 [src] |

## 6. Timeline: past, current, planned
<!-- key: timeline-past-current-planned -->

**Past (training sets and challenges that set the practice).**
- 2009: the Coyote Universe emulates P(k) from 37 models
  (arXiv:0902.0429) [src: abstract].
- 2018: PLAsTiCC on Kaggle, 28 September – 17 December, 1094 teams
  (arXiv:1903.11756) [src: abstract]; the lens-finding challenge on 100 000
  candidates (arXiv:1802.03609) [src: abstract].
- 2019: Quijote, 44 100 N-body runs (arXiv:1909.05273) [src: Sect. II].
- 2020–2021: CAMELS, 4233 runs (arXiv:2010.00619) [src: abstract]; CMD, 70 TB
  (arXiv:2109.10915) [src: abstract].
- 2022: CosmoGridV1 and the KiDS-1000 GCNN analysis (arXiv:2209.04662,
  arXiv:2201.07771) [src].

**Current.**
- 2024: Beyond-2pt first-round results (arXiv:2405.02252) [src];
  KiDS-SBI (arXiv:2404.15402) [src]; DES Y3 neural-compression SBI on
  Gower Street (arXiv:2403.02314) [src].
- 2025: ELAsTiCC-trained classifiers (arXiv:2501.01496) [src]; DES Y3
  map-level lensing + clustering design (arXiv:2511.04681) [src]; Fink
  anomaly detection in operation on ZTF since 25 January 2023
  (arXiv:2603.29511) [src: abstract].
- 2026: FAIR Universe Weak Lensing ML Uncertainty Challenge in two phases
  (arXiv:2604.14451) [src]; CAMELS second generation and
  CAMELS-CROCODILE (arXiv:2606.10038, arXiv:2609.23982) [src]; LSST DESC
  AI/ML white paper (arXiv:2601.14235) [src].

**Planned or announced.**
- DES Y3 map-level weak lensing + clustering on data (announced in
  arXiv:2511.04681) [src].
- Application of DESC ML classifiers and anomaly detection to the Rubin
  alert stream (arXiv:2404.08798) [src].

## 7. Not verified
<!-- key: not-verified -->

- Dates and organisation of ELAsTiCC itself (no ELAsTiCC description paper
  was read; facts come from papers that used it). An INSPIRE search
  (2026-10-17) found eight ELAsTiCC-using papers and no description paper.
- FAIR Universe challenge timeline and the organisers' results paper
  (announced for NeurIPS 2026, arXiv:2604.09621, Sect. 4 [src]); the winning
  entry is in `results.md` §5.
- Release status of the DES Y3 map-level clustering + lensing data
  analysis after its design paper: no data paper found by a date-sorted
  arXiv search from November 2025 (2026-10-16); the lensing-only DES Y3
  hybrid-statistics analysis appeared (arXiv:2606.11309) [src].
