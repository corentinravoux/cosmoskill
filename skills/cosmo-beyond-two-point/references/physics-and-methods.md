# Physics and methods — statistics beyond the two-point function

Scope: definitions, estimators, theory models, covariance, blinding and codes for the bispectrum and trispectrum, cosmic voids, density-split and other alternative clustering statistics, higher-order lensing statistics, field-level inference and simulation-based inference.
Snapshot: 2026-10-07

Status lines use three levels: data, blinded or mock-validated; data, not
blind; simulations only. The full status table is `results.md` §0.

## 1. Bispectrum, trispectrum and N-point functions
<!-- key: bispectrum-trispectrum-and-n-point-functions -->

### 1.1 Definitions
<!-- key: definitions -->

The bispectrum is the Fourier-space three-point function,
⟨δ(k1) δ(k2) δ(k3)⟩ = (2π)³ δ_D(k1 + k2 + k3) B(k1, k2, k3); the trispectrum T
is the connected four-point analogue. In redshift space B depends on the
triangle shape and on two angles to the line of sight, and is expanded in
multipoles (monopole, quadrupole, hexadecapole). A Gaussian field has B = 0 and
T = 0; gravity, non-linear galaxy bias and primordial non-Gaussianity all
generate them. The practical value of B is that it separates quantities which
the power spectrum measures only as products: b1, b2, f and σ8 (Gil-Marín et
al. 2014, arXiv:1407.5668), and that it is the large-scale-structure probe of
the non-local (equilateral, orthogonal) shapes of f_NL (Chudaykin, Ivanov &
Philcox 2025, arXiv:2512.04266).

### 1.2 Estimators in use
<!-- key: estimators-in-use -->

| Estimator | What it does | Reference |
|---|---|---|
| Binned-triangle estimator of the bispectrum monopole | Number of triangles limited by the number of mocks | arXiv:1407.5668; Gil-Marín et al. 2016, arXiv:1606.00439 |
| Maximal (Karhunen–Loève) and geometrical compression | Raises the usable triangle count from 116 to 2734 [src] on BOSS CMASS | Gualdi et al. 2018, arXiv:1806.02853; Gualdi et al. 2019, arXiv:1901.00987 |
| Window-free (quasi-optimal, maximum-likelihood) estimators | Deconvolve the survey window in the measurement, so the theory is not window-convolved; extended to ℓ = 2, 4 multipoles | Philcox & Ivanov 2021, arXiv:2112.04515; Ivanov et al. 2023, arXiv:2302.04414 |
| Tripolar spherical harmonic (TripoSH) decomposition | Window convolution becomes a linear transformation of theory multipoles | Guandalin et al. 2026, arXiv:2610.01836 |
| ShapeFit compression of P + B0 | Compress to α_iso, α_AP, fσ_s8, m+n, then infer cosmology; mitigates prior-volume effects | Novell-Masot et al. 2025, arXiv:2503.09714; Novell-Masot et al. 2026, arXiv:2603.19356 |
| Isotropic-basis 4PCF, parity-odd modes | Lowest-order statistic sensitive to scalar parity violation | Hou, Slepian & Cahn 2022, arXiv:2206.03625; Philcox 2022, arXiv:2206.04227 |
| Kurto spectra (composite-field spectra P_2×2, P_3×1) | Compress the parity-odd trispectrum to a low-dimensional vector so that the covariance can come directly from mocks | Gao et al. 2026, arXiv:2604.06021 |

### 1.3 Theory models
<!-- key: theory-models -->

- **Tree-level EFT bispectrum with one-loop power spectrum.** Used for DESI
  DR1 in arXiv:2610.01836; arXiv:2206.08327 describes its own earlier BOSS
  analysis in the same terms. The window-free BOSS analyses are
  arXiv:2112.04515 and arXiv:2302.04414.
- **One-loop EFT bispectrum.** First applied to BOSS by D'Amico et al. 2022
  (arXiv:2206.08327): one-loop for the power spectrum and bispectrum monopole,
  tree level for the bispectrum quadrupole. A systematic power-counting
  derivation and a fast implementation (COBRA) are in Bakx et al. 2025
  (arXiv:2507.22110); the one-loop model is used for the DESI DR1 f_NL
  analysis (arXiv:2512.04266).
- **Hybrid EFT + phenomenological model (FolpsD).** An extension of the FOLPS
  code that combines its one-loop EFT power spectrum with a bispectrum model
  mixing EFT and phenomenological ingredients, exploiting small-scale P and
  large-scale B (Bansal et al. 2026, arXiv:2604.08895).
- **Tree-level EFT trispectrum.** Developed and validated on 25 AbacusSummit
  boxes of total volume 200 h⁻³Gpc³ [src] by Tucci & Philcox 2026
  (arXiv:2610.08908), with k_max up to 0.12 h Mpc⁻¹ [src] depending on tracer.
  The abstract states that no full-shape trispectrum analysis yet exists.
- **Simulation-based priors (EFT-SBP).** EFT nuisance parameters receive priors
  learned from HOD simulations; used with P + B in Chen & Ivanov 2025
  (arXiv:2507.00118) and in the DESI + BOSS f_NL combination of
  arXiv:2512.04266. Whether these priors are safe is disputed; see
  `open-questions.md` §1.

### 1.4 Covariance and likelihood
<!-- key: covariance-and-likelihood -->

The bispectrum data vector is long, so the number of mocks sets the binning:
with 2048 MultiDark-Patchy mocks BOSS analyses kept about 116 triangles before
compression (arXiv:1806.02853). DESI DR1 P + B analyses take the cross-covariance
between P, B and post-reconstruction BAO from mocks (Forero-Sánchez et al.
2026, arXiv:2606.23936). For four-point statistics the covariance is the
dominant risk: the parity-odd 4PCF significance depends on which mocks supply
the noise model (see `systematics.md` §1.3).

### 1.5 Status
<!-- key: status-5 -->

Bispectrum (monopole, tree level or one loop): **data, mock-validated**, in
BOSS and DESI DR1, including inside the DESI collaboration. Trispectrum full
shape: **simulations only**. Parity-odd 4PCF: **data, measured, no accepted
detection**.

## 2. Cosmic voids
<!-- key: cosmic-voids -->

Reviews: Pisani et al. 2019 (arXiv:1903.05161); the void chapter of Moresco et
al. 2022 (arXiv:2201.07241).

### 2.1 Void finders
<!-- key: void-finders -->

A void catalogue is defined by its finder; statistics from different finders
are not interchangeable.

| Finder | Principle | Reference |
|---|---|---|
| ZOBOV | Voronoi tessellation density estimate plus watershed; no free parameter, no shape assumption | Neyrinck 2008, arXiv:0712.3049 |
| VIDE | Toolkit built on ZOBOV for surveys and simulations | Sutter et al. 2015, arXiv:1406.1191 |
| REVOLVER, voxel, Pylians3 spherical finder | Three further packages, compared with VIDE in the AP-response study | Radinović et al. 2024, arXiv:2407.02699 |
| VoidFinder, V² | Two algorithms, the second with REVOLVER or VIDE pruning; used for the DESI BGS catalogue | Rincon et al. 2024, arXiv:2411.00148 |
| Spherical-overdensity finder on a Lyα tomographic map | Finder calibrated on hydrodynamical simulations of the intergalactic medium | Krolewski et al. 2018, arXiv:1710.02612 |
| Back-in-time void finder | Dynamical identification after optimal-transport reconstruction | Sartori et al. 2026, arXiv:2601.15378 |

### 2.2 Void size function (VSF)
<!-- key: void-size-function-vsf -->

The VSF is the comoving number density of voids per unit radius. The models in
use descend from the excursion-set model of Sheth & van de Weygaert; current
analyses use its volume-conserving (Vdn) modification, extended with nuisance
parameters tied to the large-scale galaxy bias and calibrated on mocks
(Contarini et al. 2022, arXiv:2205.11525; Contarini et al. 2023,
arXiv:2212.03873). An alternative BOSS DR16 analysis fits the linear
underdensity threshold δ_v and an RSD parameter B directly (Song et al. 2025,
arXiv:2501.07817). Void counts are treated as Poisson distributed; this was
checked on simulations by Thiele et al. 2023 (arXiv:2307.07555).

### 2.3 Void–galaxy cross-correlation: AP and RSD
<!-- key: void-galaxy-cross-correlation-ap-and-rsd -->

The observable is the anisotropic cross-correlation ξ_vg(s, μ) between void
centres and galaxies, compressed to multipoles. Two physical inputs:

- **Geometry.** A stack of voids is spherically symmetric in real space if the
  Universe is statistically isotropic, so its apparent ellipticity under a
  fiducial cosmology measures D_M/D_H (the Alcock–Paczynski test).
- **Dynamics.** In linear theory mass conservation gives the mean radial
  outflow v_r(r) = −(1/3) f a H r Δ(r), where Δ(r) is the mean matter density
  contrast inside r. The redshift-space quadrupole therefore measures the
  growth rate, quoted as β = f/b or as fσ8 depending on the analysis.

Two modelling schools exist:

1. **Deprojection, no calibration** (Hamaus et al. 2020, arXiv:2007.07895):
   the real-space profile is inferred from the data by tomographic
   deprojection; the model is linear and has two nuisance parameters;
   optionally calibrated on mocks.
2. **Reconstruction before void finding** (Nadathur et al. 2019,
   arXiv:1904.01030; Nadathur et al. 2020, arXiv:2008.06060; Woodfinden et al.
   2022, arXiv:2205.06258): large-scale RSD are removed from the galaxy field
   with a velocity reconstruction before voids are identified, so that void
   centres carry no RSD-induced selection bias.

Convention trap: arXiv:1904.01030 quotes D_A H/c = 0.4367 at z = 0.57 with D_A
the angular diameter distance, while arXiv:2007.07895 quotes D_A H/c = 0.588 at
z = 0.51 with D_A the *comoving* angular diameter distance. They differ by a
factor (1 + z): 0.4367 × 1.57 = 0.686 [der, assuming the first is the proper
distance]. From 2020 the reconstruction school quotes D_M/D_H.

### 2.4 Void lensing
<!-- key: void-lensing -->

The stacked tangential shear or CMB-lensing convergence around voids measures
the matter profile and hence tests the bias and the mock predictions (Martin
et al. 2025, arXiv:2507.13450; Sartori et al. 2024, arXiv:2412.02761). It has
produced detections and amplitude tests, not cosmological parameters.

### 2.5 Voids in Lyα tomography and the void–forest cross-correlation
<!-- key: voids-in-lyalpha-tomography-and-the-void-forest -->

A tomographic map is a Wiener-filter interpolation of the Lyα flux contrast
between neighbouring sightlines; its resolution is set by the mean transverse
sightline separation. Two regimes exist. Dense galaxy-plus-quasar backgrounds
give about 2–2.5 h⁻¹Mpc over a fraction of a square degree (CLAMATO:
arXiv:1710.02612; Horowitz et al. 2022, arXiv:2109.09660). Quasar-only surveys
give 13 h⁻¹Mpc over 220 deg² at a sightline density of 37 deg⁻² [src]
(arXiv:2004.01448), which also provides a void and protocluster catalogue
from the map.

The void–forest cross-correlation of Ravoux et al. 2022 (arXiv:2203.11045)
correlates void centres from the map with the Lyα flux contrast along the
sightlines. Its quadrupole is fitted with a linear RSD model that includes the
"tomographic effect" of the data lying along parallel lines of sight. The
fitted parameter is the RSD parameter β of the forest around voids. It is not
f/b: the forest β involves the velocity-gradient bias (see
`cosmo-lyman-alpha`), so turning it into a growth-rate measurement requires a
model of that bias. Thesis summary: Ravoux 2022, arXiv:2203.07886.

### 2.6 Voids with simulation-based inference
<!-- key: voids-with-simulation-based-inference -->

Thiele et al. 2023 (arXiv:2307.07555) combine the VSF, the void–galaxy cross
power spectrum and the galaxy power spectrum of BOSS CMASS NGC in an implicit
likelihood analysis with HOD-populated approximate simulations including
particle neutrinos.

### 2.7 Status
<!-- key: status-4 -->

Void–galaxy AP/RSD: **data, mock-validated** (SDSS MGS, BOSS, eBOSS); the
abstracts read this session do not report a blinded analysis, and no DESI
void–galaxy cosmology was found. VSF: **data, with a mock-calibrated model**.
Void lensing: **data, detection level**. Lyα–void: **data, first detection
compared to simulations**, RSD parameter only.

## 3. Alternative clustering statistics: density split, kNN, wavelets, Minkowski functionals, marks
<!-- key: alternative-clustering-statistics-density-split -->

These statistics have no perturbative model on the scales where they gain
information. All data applications so far use **simulation-based emulators**:
N-body boxes at many cosmologies, populated with a halo occupation
distribution (HOD), with the statistic emulated by a neural network over
cosmology and HOD parameters. The cosmological result is therefore conditional
on the simulation suite and on the galaxy–halo model.

| Statistic | Definition | Model in use | Reference |
|---|---|---|---|
| Density-split clustering (DSC) | Rank random query points by the smoothed local galaxy density, split into quantiles, and measure the quantile–galaxy cross-correlation and quantile auto-correlation multipoles | SUNBIRD neural emulator on AbacusSummit HOD mocks, sub-percent accuracy down to 1 h⁻¹Mpc [src] | Cuesta-Lazaro et al. 2023, arXiv:2309.16539; Paillas et al. 2023, arXiv:2309.16541 |
| k-nearest-neighbour CDFs (kNN) | Empirical cumulative distribution of distances from volume-filling random points to the k-th nearest data point; sensitive to all connected N-point functions; contains counts-in-cells and the void probability function | AbacusSummit emulator (in the Beyond-2pt challenge) | Banerjee & Abel 2021, arXiv:2007.13342; Banerjee & Abel 2021, arXiv:2102.01184 |
| Wavelet scattering transform (WST) | Moduli of successive wavelet convolutions of the density field, spatially averaged; a fixed-kernel analogue of a convolutional network | AbacusSummit HOD emulator, or SimBIG forward model | Valogiannis & Dvorkin 2022, arXiv:2204.13717; Valogiannis, Yuan & Dvorkin 2024, arXiv:2310.16116; Régaldo-Saint Blancard et al. 2024, arXiv:2310.15250 |
| Minkowski functionals (MFs) | Volume, surface area, mean curvature and Euler characteristic of excursion sets of the smoothed field as functions of threshold | Hermite expansion on large scales (perturbatively non-Gaussian regime); neural emulator on AbacusSummit HOD mocks for the full information | Appleby et al. 2022, arXiv:2110.06109; Liu et al. 2025, arXiv:2501.01698 |
| Marked power spectrum | Power spectrum of the field weighted by a function ("mark") of the local density; up-weighting low density enhances neutrino sensitivity | One-loop perturbation theory; non-perturbative at z = 0 for small smoothing scales | Massara et al. 2021, arXiv:2001.11024; Philcox, Massara & Spergel 2020, arXiv:2006.10055 |
| Galaxy multiplets | Small groups of nearby galaxies treated as objects and cross-correlated with the galaxy field | Comparison with AbacusSummit HOD mocks | Wang et al. 2025, arXiv:2511.15354 |
| Compressed Lyα forest bispectrum | Three-point statistic of the 3D forest, compressed | proposed estimator; see `cosmo-lyman-alpha` for the forest itself | de Belsunce, Sullivan & McDonald 2025, arXiv:2510.23597 |

Information-content studies use the Quijote suite: 44 100 N-body simulations
over more than 7 000 cosmologies in boxes of 1 h⁻¹Gpc [src]
(Villaescusa-Navarro et al. 2020, arXiv:1909.05273). A Fisher forecast from
Quijote is an upper bound for matter or halos in a periodic box; it is not a
survey forecast.

Covariance: from mocks at fixed cosmology (for example 1 500 mocks for DSC in
the Beyond-2pt challenge), with an emulator-error term added (table in
arXiv:2405.02252, Krause et al. 2024).

Status. DSC, WST, MFs: **data (BOSS CMASS only), mock-validated, emulator-
and HOD-dependent**. kNN, marked power spectrum: **simulations and mock
challenge only**; no cosmological constraint from survey data was found this
session. Multiplets: **data (DESI DR2 LRG), used for the galaxy–halo
connection, not cosmology**.

## 4. Higher-order weak-lensing statistics
<!-- key: higher-order-weak-lensing-statistics -->

Two-point lensing (ξ±, COSEBIs, pseudo-Cℓ, shear and redshift calibration) is
in `cosmo-weak-lensing`. This section covers what is added on top.

### 4.1 Statistics
<!-- key: statistics -->

| Statistic | Definition | Modelling | Data applications read this session |
|---|---|---|---|
| Third-order aperture mass ⟨M_ap³⟩ | Skewness of the shear field filtered with a compensated aperture; a compression of the shear three-point function | Conventional likelihood; joint covariance from simulated shear maps | DES Y3 (Gomes et al. 2025, arXiv:2508.14018); HSC Y3 (Sugiyama, Gomes & Jain 2025, arXiv:2508.14019); KiDS-Legacy (Linke et al. 2026, arXiv:2606.12389) |
| Moments of the convergence map | Second and third moments of smoothed mass maps | Validated on simulations; simulation-based inference in the 2024 analysis | DES Y3 (Gatti et al. 2022, arXiv:2110.10141; validation in Gatti et al. 2020, arXiv:1911.05568) |
| Peak (and minimum) counts | Number of local maxima (minima) of the aperture-mass or convergence signal-to-noise map as a function of height | N-body simulations | KiDS-450 (Martinet et al. 2018, arXiv:1709.07678); HSC Y1 tomographic peaks (Liu et al. 2023, arXiv:2210.07853); DES Y3 (Jeffrey et al. 2025, arXiv:2403.02314) |
| One-point PDF | Histogram of the smoothed convergence | Simulations | HSC Y1 (Novaes et al. 2025, arXiv:2409.01301) |
| Minkowski functionals | Area, perimeter and genus of excursion sets of the convergence map | Simulations | HSC Y1 (Armijo et al. 2025, arXiv:2410.00401; arXiv:2409.01301) |
| Scattering transform, wavelet phase harmonics | Moduli of iterated wavelet convolutions; phase couplings between scales | Simulations | HSC Y1 (Cheng et al. 2025, arXiv:2404.16085); DES Y3 (Gatti et al. 2024, arXiv:2310.17557; Gatti et al. 2025, arXiv:2405.10881) |
| Persistent homology (Betti numbers) | Birth and death of connected components and holes across thresholds, on the sphere | Simulations | DES Y3 (Prat et al. 2025, arXiv:2506.13439) |
| Map-level neural compression | A convolutional network compresses the tomographic maps to a few numbers | Simulations | KiDS-450 and KiDS-1000 (Fluri et al. 2019, arXiv:1906.03156; Fluri et al. 2022, arXiv:2201.07771); HSC Y1 (Lu, Haiman & Li 2023, arXiv:2301.01354); DES Y3 (arXiv:2403.02314; Williamson et al. 2026, arXiv:2606.11309) |
| Peak steepness | Profile slope of lensing peaks, sensitive to halo profiles and feedback | Simulations | HSC Y1 (Li et al. 2026, arXiv:2608.24591) |

### 4.2 Inference practice
<!-- key: inference-practice -->

The ⟨M_ap³⟩ analyses use a conventional likelihood. The other statistics take
their model from simulations, as an emulator or, in the DES Y3 2024–2026
series and the HSC Y1 combined analysis (arXiv:2409.01301), by
**simulation-based inference**: a suite of N-body lensing
simulations spanning cosmology is turned into mock surveys with the mask,
shape noise, shear calibration, photometric-redshift uncertainty, intrinsic
alignments and source clustering applied; the statistic is compressed by a
neural network; and a neural density estimator gives the likelihood or
posterior. The DES Y3 implementation rests on the Gower Street suite, 791
full-sky PKDGRAV simulations from which more than 3 000 mock DES data sets are
built [src] (arXiv:2403.02314). Validation is by coverage tests and by
contaminating the test vector with baryonic feedback (arXiv:2606.11309,
arXiv:2506.13439).

The DES Y3 "hybrid" analysis compresses the maps to seven summaries, combining
the power spectrum with neural summaries built to add information beyond it
(arXiv:2606.11309).

### 4.3 Status
<!-- key: status-3 -->

Higher-order lensing is the most mature beyond-two-point family on data:
**survey data, collaboration analyses, systematics forward-modelled, validated
by coverage and feedback tests**, for DES Y3, KiDS-Legacy and HSC. Blinding
status is not stated in the abstracts read; check each paper. A combined
lensing-plus-clustering map-level pipeline exists as an analysis design for
DES Y3 (Thomsen et al. 2025, arXiv:2511.04681); its cosmological result was
not found.

## 5. Field-level inference
<!-- key: field-level-inference -->

### 5.1 Three things called "field-level"
<!-- key: three-things-called-field-level -->

The term covers three different methods. A text that does not say which one
it means cannot be checked.

1. **Forward-model inference with sampled initial conditions.** The joint
   posterior P(θ, δ_ini | d) ∝ L(d | F[δ_ini, θ]) P(δ_ini | θ) P(θ) is sampled,
   where F is a structure-formation model plus bias, selection and noise, and
   δ_ini has as many dimensions as the grid (10⁶ or more). Hamiltonian Monte
   Carlo is the standard sampler. This is the only form that accesses all
   non-Gaussian information on the scales modelled.
2. **Gaussian field-level likelihood.** The observed field values (velocities,
   densities) are the data vector of a multivariate Gaussian whose covariance
   is computed from a model power spectrum; no initial conditions are sampled.
   It is optimal for a Gaussian field and uses two-point information only;
   nuisance parameters of the field are fitted with the cosmology. This is
   what `flip` implements, with wide-angle covariance models; the paper
   presents it as the foundation for a non-linear extension (Ravoux et al.
   2025, arXiv:2501.16852). See `cosmo-peculiar-velocities`.
3. **Neural field-level methods.** A network takes the gridded field and
   returns either compressed summaries for simulation-based inference (SimBIG,
   Lemos et al. 2024, arXiv:2310.15256) or a reconstructed linear field (LiFT,
   Parker et al. 2026, arXiv:2609.14862). The information extracted is whatever
   the network learned from the training simulations.

### 5.2 Forward-model families
<!-- key: forward-model-families -->

| Family | Gravity model | Tracer model | Applied to | Reference |
|---|---|---|---|---|
| BORG | second-order Lagrangian perturbation theory | galaxy bias, survey mask and selection function | SDSS DR7-like mocks; valid above about 6 h⁻¹Mpc [src] | Jasche & Wandelt 2013, arXiv:1203.3639 |
| BORG with particle mesh | particle-mesh N-body inside the sampler | hierarchical bias and selection parameters, block sampling + HMC | 2M++ | Jasche & Lavaux 2019, arXiv:1806.11117 |
| BORG on deep surveys | physical structure-formation model (LPT for Quaia) with light-cone effects and RSD | bias, selection and foreground corrections | SDSS-III/BOSS; Quaia quasars | Lavaux, Jasche & Leclercq 2019, arXiv:1909.06396; Andrews et al. 2026, arXiv:2602.02363 |
| Manticore-Local | non-linear gravity solver, physics-informed priors | refined bias model | 2M++; yields a posterior ensemble of constrained simulations ("digital twin") | McAlpine et al. 2025, arXiv:2505.10682 |
| LEFTfield | Lagrangian EFT forward model | EFT bias expansion with noise parameters | simulated halos; Beyond-2pt real-space mock | Nguyen et al. 2024, arXiv:2403.03220 |
| Perturbative forward model, Gaussian likelihood | perturbation theory | EFT bias, Gaussian noise with constant power | mock data from the same model | Akitsu et al. 2025, arXiv:2509.09673; Spezzati, Marinucci & Simonović 2025, arXiv:2507.05378 |
| BORG-WL | gravity model of the BORG-WL framework | TATT or NLA alignments, enthalpy-gradient-descent baryons | synthetic shear data only | Porqueres et al. 2023, arXiv:2304.04785 |
| BORG for f_NL^loc | structure-formation model and resolution varied as tests | bias + initial conditions + f_NL sampled jointly | Quijote halo catalogues, k_max ≈ 0.1 h Mpc⁻¹ | Andrews et al. 2026, arXiv:2603.20855 |

### 5.3 What the outputs are
<!-- key: what-the-outputs-are -->

The BORG runs on data read here deliver **fields** (initial conditions,
density, velocity, with posterior uncertainty) and quote no cosmological
parameter. EFT-type runs vary σ8 or A, ω_cdm, H0 and deliver **parameter
posteriors**, so far on simulations.

### 5.4 Status
<!-- key: status-2 -->

Forward-model inference: **reconstructions from survey data (2M++, BOSS,
Quaia); cosmological parameters from simulations only**; no parameter
constraint from survey data was found this session. Neural field-level:
**survey data** (BOSS CMASS subsample, DESI DR1 LRG BAO), validated on mocks
with changed forward models, outside collaboration pipelines. Gaussian
field-level likelihood: **survey data, collaboration result** for fσ8 from
DESI DR1 peculiar velocities (`cosmo-peculiar-velocities`).

## 6. Simulation-based inference with learned summaries
<!-- key: simulation-based-inference-with-learned -->

### 6.1 Method
<!-- key: method -->

Simulation-based (implicit-likelihood, likelihood-free) inference replaces the
analytic likelihood by a neural density estimator, usually a normalising flow,
trained on pairs of parameters and simulated data vectors. The data vector is
a set of summary statistics, optionally compressed by a second network, or the
output of a convolutional network applied to the field. Three checks are
standard: simulation-based calibration (posterior coverage on held-out
simulations), a test set built with a *different* forward model, and
stability under changes of the density-estimator architecture
(arXiv:2211.00660, arXiv:2310.15250).

### 6.2 SimBIG
<!-- key: simbig -->

SimBIG forward-models the BOSS CMASS sample from Quijote N-body simulations
and a flexible halo occupation model with survey geometry and fibre collisions
(arXiv:2211.00660). The published analyses use a CMASS subsample that spans
about 10% of the full BOSS volume [src] (Hahn et al.
2024, arXiv:2310.15246), to k_max = 0.5 h Mpc⁻¹. Statistics analysed: power
spectrum multipoles, bispectrum monopole (Hahn et al. 2024, arXiv:2310.15243),
CNN field-level summary (arXiv:2310.15256), wavelet scattering transform
(arXiv:2310.15250), marked power spectrum (Massara et al. 2024,
arXiv:2404.04228).

### 6.3 Status
<!-- key: status -->

**Survey data (BOSS CMASS subsample), mock challenge with changed forward
models passed for some statistics and failed for others; no collaboration
blinding.**

## 7. Blinding, codes and conventions
<!-- key: blinding-codes-and-conventions -->

### 7.1 Blinding and validation practice
<!-- key: blinding-and-validation-practice -->

- Parameter-masked mock challenge: Beyond-2pt (arXiv:2405.02252), described in
  `surveys-and-data.md` §6. It blinds the *truth of a mock*, not survey data.
- Blind tests on data stated in the abstracts read: the BOSS parity-odd 4PCF
  rank test (arXiv:2206.04227). For every other data result in this skill the
  abstract does not state whether the data analysis was blinded; the
  collaboration analyses (DESI bispectrum, DES Y3 and KiDS-Legacy lensing)
  are expected to follow the survey blinding schemes described in
  `cosmo-galaxy-clustering` and `cosmo-weak-lensing`; this was not checked
  per paper.
- Changed-forward-model test sets: SimBIG (arXiv:2211.00660), LiFT
  (arXiv:2609.14862), MFs with non-HOD mocks (arXiv:2501.01698).
- Large-volume recovery tests: 84 times the CMASS volume for density split
  (arXiv:2309.16541); 200 h⁻³Gpc³ for the trispectrum (arXiv:2610.08908).

### 7.2 Codes and public products named in the papers read
<!-- key: codes-and-public-products-named-in-the-papers -->

| Code or product | Purpose | Reference |
|---|---|---|
| flip | Gaussian field-level likelihood for velocity and density fields, Fisher forecasts | arXiv:2501.16852 |
| BORG | Bayesian reconstruction of initial conditions | arXiv:1203.3639, arXiv:1806.11117 |
| LEFTfield | Lagrangian EFT forward model for field-level inference | arXiv:2403.03220 |
| FolpsD, COBRA | Fast P + B models for DESI | arXiv:2604.08895, arXiv:2507.22110 |
| SUNBIRD | Density-split emulator, public on GitHub [src] | arXiv:2309.16539 |
| ZOBOV, VIDE, VoidFinder, V², REVOLVER | Void finders | arXiv:0712.3049, arXiv:1406.1191, arXiv:2411.00148, arXiv:2407.02699 |
| TopoS2 | Persistent homology on the sphere | arXiv:2506.13439 |
| Quijote, Gower Street, SimBIG mocks, Beyond-2pt mocks | Simulation suites and challenge data | arXiv:1909.05273, arXiv:2403.02314, arXiv:2211.00660, arXiv:2405.02252 |

### 7.3 Conventions that cause errors
<!-- key: conventions-that-cause-errors -->

- **D_A H/c against D_M/D_H** in void papers: proper or comoving D_A (§2.3).
- **β** means f/b for galaxies around voids, and the forest RSD parameter in
  the void–forest correlation; neither is fσ8.
- **S8** is σ8 (Ω_m/0.3)^0.5 in every lensing paper cited here; always state
  ΛCDM or wCDM with the value.
- **k_max** is in h Mpc⁻¹. The perturbative bispectrum, trispectrum and
  field-level analyses read here stop at 0.10–0.12; SimBIG quotes 0.5;
  emulators quote 1 h⁻¹Mpc in configuration space.
- **"Field-level"** has three meanings (§5.1).
- **"Gain"** must name its baseline: the same pipeline's two-point analysis,
  a perturbative analysis, or a Fisher forecast.
