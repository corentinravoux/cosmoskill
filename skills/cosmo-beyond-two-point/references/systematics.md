# Systematics — statistics beyond the two-point function

Scope: the systematic effects specific to higher-order, void, field-level and simulation-based analyses, with sizes where a paper quantifies them.
Snapshot: 2026-10-13


## 1. Bispectrum and N-point functions
<!-- key: bispectrum-and-n-point-functions -->

### 1.1 Number of mocks versus length of the data vector
<!-- key: number-of-mocks-versus-length-of-the-data-vector -->

Mechanism: the sample covariance of N_b bins from N_m mocks is singular or
badly biased when N_b approaches N_m. Size: with the BOSS mock set the standard
binning held 116 triangles; compression allowed 2734 and cut the credible
intervals on (b1, b2, f, σ8) by 24.8%, 52.8%, 26.4%, 21% [src: abstract] (arXiv:1806.02853), and by 39%, 49%, 29%, 22% with geometrical compression
[src: abstract] (arXiv:1901.00987). Mitigation: compression, analytic covariance,
window-free estimators. Referee check: N_m, N_b, and the Hartlap or Percival
factor applied (those corrections are in `cosmo-statistics-inference`).

Mocks against bins in the main analyses:

| Analysis | Mocks | Bispectrum bins | Correction and caveat |
|---|---|---|---|
| BOSS window-free (arXiv:2112.04515) | 2048 Patchy; 999 with BAO | 62 | Hartlap [src: Sect. III, IV.3] |
| BOSS one-loop (arXiv:2206.08327) | 2048 Patchy | 150 (CMASS), 62 (LOWZ), + 9 for B_2 | Hartlap ≈ 0.91, 0.95; bins widened to that end [src: Sect. 2]. Residual theory systematic on simulations ≤ 0.25 (Nseries) and ≤ 0.33 (Patchy, on S8) of the BOSS error over Ω_m, h, σ8, ω_cdm, ln(10¹⁰A_s), S8; detection floor about 0.15 [src: Table 3, Sect. 5.4] |
| DESI DR1 collaboration (arXiv:2503.09714) | 1000 EZmocks | 150 (189 with P_0,2,4) | Hartlap ≈ 0.8, Sellentin–Heavens. Amplitude rescaled by factors derived for P and assumed valid for B; residual mis-estimate put below about 20% of the DR1 error [src: Sect. 3.4]. χ²/dof ≈ 1.4–1.5 on AltMTL mocks in LRG1 and LRG3, attributed to the model or to an underestimated covariance [src: Sect. 5.2] |
| DESI DR1 TripoSH (arXiv:2610.01836) | 1000 EZmocks with a fast-fibre-assignment emulator | diagonal k_1 = k_2 only | The emulator does not reproduce the realistic (altMTL) assignment, though the variances agree [src: Sect. 4.2, 3.2] |
| DESI DR1 reanalysis (arXiv:2507.13433) | none: Gaussian analytic, with the mask | 49 per chunk | No P–B cross-covariance, no correlation between DR1 full shape and DR2 BAO; validation would need mocks that are high-resolution, numerous and carry fibre collisions [src: Sect. IV.4, VIII] |
| DESI DR1 full shape + DR2 BAO (arXiv:2606.23936) | 100, for the BAO × ShapeFit correlation | compressed parameters | Dropping that block moves σ8 by 0.44σ and h by 0.4σ [src: Sect. 3.4, 4.1] |

Two DESI DR1 P + B results thus rest on covariances built in opposite ways.

Systematic budget of the DESI collaboration analysis, P_0,2,4 + B_0, in
percent of the DR1 1σ statistical error, LRG1 / LRG2 / LRG3 / QSO; a term is
propagated only above 20% [src: Table 4 of arXiv:2503.09714]:

| Source | α_iso | α_AP | fσ_s8 | m+n | σ_s8 |
|---|---|---|---|---|---|
| Modelling (scale cuts and window approximation included) | <20 / <10 / ~20 / ~20 | <20 / ~20 / <20 / <10 | ~20 / ~50 / <20 / ~40 | ~50 / ~50 / ~50 / <20 | <10 / ~90 / ~40 / — |
| Observational (fibre assignment) | <20 / <10 / <20 / ~40 | <20 / <20 / ~50 / ~40 | <20 / <20 / ~60 / ~90 | <10 / ~30 / <10 / <20 | ~30 / ~70 / ~50 / — |
| HOD (mean; maximum over variants below 42) | <10 | <10 | <10 to <20 | <10 to <20 | <20 |
| Fiducial cosmology (mean; maximum up to 77 on m+n) | <10 | <10 | <10 to <20 | <20 to ~30 | ~20 to ~30 |
| Total | <20 / <20 / ~20 / ~45 | <20 / ~20 / ~50 / ~40 | ~20 / ~50 / ~60 / ~103 | ~50 / ~58 / ~50 / ~30 | ~42 / ~116 / ~71 / — |

The systematic term on σ_s8 in LRG2 and on fσ_s8 for the quasars equals the
statistical error; modelling and fibre assignment dominate [src: Sect. 4.4].

### 1.2 Fibre collisions in three-point statistics
<!-- key: fibre-collisions-in-three-point-statistics -->

Mechanism: missing close pairs alter every triangle with a small side. The
independent DESI DR1 reanalysis introduces a stochastic estimator for fibre
collisions specifically to make the bispectrum usable (arXiv:2507.13433). The
collaboration treatment for two-point statistics is in
`cosmo-galaxy-clustering`.

| Item | Size or treatment | Place |
|---|---|---|
| Fibre collisions, reanalysis | Removing triplets with a pair inside θ_cut changes the bispectrum numerator by 10–20% and its normalisation by about 1%; the removed part sums to 4.9σ for the quasars; present on all scales, larger at high k and for equilateral triangles. A direct cut needs triplet counts, hence a stochastic (Girard–Hutchinson) estimator | arXiv:2507.13433 [src: Sect. IV.4, IV.2.3] |
| Fibre collisions, collaboration | No θ-cut, since the fit stops at k = 0.15 (P) and 0.12 h Mpc⁻¹ (B); the residual is the shift between 25 "complete" and 25 AltMTL mocks, the "observational" row of §1.1, up to about 90% of the statistical error on fσ_s8 for quasars | arXiv:2503.09714 [src: Sect. 3.2, 4.2, Table 4] |
| Window, deconvolved in the estimator | Windowed and unwindowed versions give nearly identical constraints | arXiv:2112.04515; arXiv:2507.13433 [src: Sect. VII.3] |
| Window, on the power-spectrum factors of the tree-level monopole only | Restricts the analysis to the monopole; named as a possible source of the m+n offset | arXiv:2206.08327 [src: Eq. 18]; arXiv:2503.09714 [src: Sect. 3.3, 4.1] |
| Window, matrix in the TripoSH basis | A scale-independent monopole residual in LRG1 and LRG2 is left to the shot-noise parameter | arXiv:2610.01836 [src: App. A.2] |
| Imaging systematics | Linear weights suffice for LRGs; a mode-removal correction for quasars shifts posteriors by less than 20% of the DR1 errors; ELGs left out for their imaging dependence | arXiv:2503.09714 [src: Sect. 4.2, Eq. 13] |

### 1.3 Mock realism for the four-point covariance
<!-- key: mock-realism-for-the-four-point-covariance -->

Mechanism: a χ² of the parity-odd 4PCF against mocks is biased if the
parity-even eight-point function of the data differs from that of the mocks.
Size: in BOSS the 8PCF bias term is about 6σ while the genuine parity signal is
0–2.5σ [src: abstract] (arXiv:2407.03397); replacing Patchy by GLAM-Uchuu mocks moves the
significance from > 3.5σ to 1.4σ [src: abstract] (arXiv:2401.09523). In DESI DR1 the auto
analysis gives 4–10σ and the cross-patch analysis gives nothing [src: abstract] (arXiv:2508.09133). Mitigation: cross-correlation between independent patches,
χ²_× and χ²_null, compressed statistics with direct mock covariance
(arXiv:2604.06021). The lesson generalises: a higher-order "detection"
expressed as a χ² against approximate mocks is a statement about the mocks
until shown otherwise.

How the significance moved with the covariance, read in the papers:

| Data, statistic | Noise model | Significance | Place |
|---|---|---|---|
| BOSS, all four chunks, rank test, 1288 bins, 10 radial bins over 20–160 h⁻¹Mpc | 2042 MultiDark-Patchy mocks | > 3.5σ (CMASS-N 2.5σ, CMASS-S 2.2σ, LOWZ-N 2.1σ, LOWZ-S 2.0σ) | arXiv:2401.09523 [src: Table 1] |
| same | 627 GLAM-Uchuu N-body mocks | 1.4σ (CMASS-N 0.0σ, CMASS-S 0.9σ, LOWZ-N 0.9σ, LOWZ-S > 3.2σ) | arXiv:2401.09523 [src: Table 1] |
| same, 250 eigenmodes, analytic T² | Patchy / GLAM-Uchuu | 3.0σ / 2.4σ; with the empirical T² distribution 2.7σ / 2.1σ | arXiv:2401.09523 [src: Sect. II] |
| BOSS CMASS-NGC, χ² with analytic covariance | Patchy | about 7σ, reproduced | arXiv:2407.03397 [src: Sect. 1.2] |
| BOSS, χ²_× between patches | Patchy | 1.8σ (NGC), 1.7σ (SGC); the combined figure depends on which of five well-motivated statistics is chosen | arXiv:2407.03397 [src: Sect. 4.5] |
| DESI DR1 LRG, auto χ² | 25 Abacus AltMTL mocks | 11.4σ (NGC), 7.0σ (SGC); sensitive to the volume correction for box replication | arXiv:2508.09133 [src: Sect. V.2] |
| same | 1000 EZmocks, fast fibre assignment | 6.6σ (NGC), 5.7σ (SGC) | arXiv:2508.09133 [src: Sect. V.2] |
| DESI DR1 LRG, cross χ²_× between 4 + 3 patches | EZmocks | −1.0σ (NGC), −0.8σ (SGC); 6.7σ and 6.1σ would be expected if auto and cross agreed | arXiv:2508.09133 [src: Sect. V.4] |

In all BOSS chunks but LOWZ-S the GLAM-Uchuu variance exceeds the Patchy
one by a roughly uniform factor, and 41% of the GLAM-Uchuu mocks analysed
with the Patchy noise model show a "detection" at ≥ 3σ [src: Sect. II of
arXiv:2401.09523]. The detection paper itself noted that the mock χ²
histogram is wider than a χ² distribution, that the analytic covariance "may
not be unbiased", that 800 eigenmodes leave about three mocks per degree of
freedom, and that Patchy underestimates power at s ≤ 20 h⁻¹Mpc [src: Sect.
5.1.3, 4.2.2 of arXiv:2206.03625]. The BOSS systematic weights were
validated for two-point functions only [src: Sect. I of arXiv:2401.09523].
In DESI the cross statistic is 2.1 times (NGC) and 30% (SGC) less
constraining than the auto; the Abacus mocks cannot serve for it, as box
replication correlates the patches [src: Sect. V.4 of arXiv:2508.09133].

### 1.4 Range of validity of the perturbative model
<!-- key: range-of-validity-of-the-perturbative-model -->

Tree-level bispectrum fits are restricted to large scales: the BOSS
compression papers used 0.03–0.12 h Mpc⁻¹ [src] (arXiv:1806.02853); the
tree-level EFT monopole was validated to 0.08 h Mpc⁻¹ at z = 0.61 [src]
(arXiv:2110.10161); the DESI collaboration bispectrum uses 0.02–0.12 with a
kernel calibrated on N-body [src: Sect. 3.3 of arXiv:2503.09714]. The one-loop
model reaches higher k at the price of many more nuisance parameters
(arXiv:2206.08327, arXiv:2507.22110). Validation standard: fits to N-body
boxes of volume far above the survey's, such as the PT Challenge suite used in
arXiv:2302.04414 or the 200 h⁻³Gpc³ of AbacusSummit used in arXiv:2610.08908.

### 1.5 Prior-volume (projection) effects
<!-- key: prior-volume-projection-effects -->

With many EFT nuisance parameters the marginal posterior means move away from
the best fit in extended models. The DESI P + B analysis uses ShapeFit
compression explicitly "to mitigate prior volume effects" (arXiv:2606.23936);
arXiv:2610.01836 reports that the w0wa region "remains sensitive to the adopted
prior ranges". The quantified shifts for the power spectrum alone are in
`cosmo-galaxy-clustering`.

Measured on noiseless synthetic data in the independent DESI DR1 reanalysis
(ΛCDM), posterior mean minus input in units of the error,
[src: Table 5 of arXiv:2507.13433]:

| Data | ω_cdm | H_0 | ln(10¹⁰A_s) | Ω_m | σ8 |
|---|---|---|---|---|---|
| P_ℓ | −0.77σ | 0.09σ | 0.56σ | −0.87σ | 0.18σ |
| P_ℓ + B_0 | −0.44σ | 0.24σ | 0.19σ | −0.63σ | 0.14σ |
| P_ℓ + B_0 + BAO | −0.28σ | 0.04σ | 0.07σ | −0.37σ | 0.16σ |

Adding the bispectrum therefore reduces the projection shift; part of a
quoted "shift when adding B" can be this effect and not new information.

## 2. Cosmic voids
<!-- key: cosmic-voids -->

### 2.1 RSD in the void positions (selection bias)
<!-- key: rsd-in-the-void-positions-selection-bias -->

Mechanism: voids found in redshift space are preferentially those elongated or
aligned so that RSD deepen them; the stack is then anisotropic for a reason
that the galaxy-velocity model does not contain. Mitigation: remove RSD from
the galaxy field by velocity reconstruction before void finding, introduced in
arXiv:1904.01030 and used in arXiv:2008.06060 and arXiv:2205.06258; the result
depends on the reconstruction efficiency, studied for Euclid in Radinović et
al. 2023 (arXiv:2302.05302).

Sizes read. Flagship mock: perfect reconstruction gives unbiased fσ8 and ε
in four bins (0.5–0.6% and 8.5–12% per bin); realistic reconstruction and
redshift errors do not degrade this significantly, the largest shift being
about 1σ in the lowest bin [src: Sect. 5.1 of arXiv:2302.05302]. The
RSD-removing reconstruction depends on β = f/b only and is repeated for each
β tested [src: Sect. 3.2]. The deprojection school finds voids in redshift
space and absorbs the selection effect in two nuisance amplitudes, M on the
monopole and Q on the quadrupole term [src: Sect. 3.5, Eq. 44 of
arXiv:2007.07895]; it disputes the need for reconstruction, which adds the
void-centre velocity to the separation and then needs mock calibration, with
only the largest 50% of voids used in arXiv:1904.01030 [src: Sect. 4.3.1].
The two schools were not compared on one catalogue in the papers read.

### 2.2 Response of the void finder to the fiducial cosmology
<!-- key: response-of-the-void-finder-to-the-fiducial -->

Mechanism: analyses assume that void centres transform under the AP distortion
like galaxy positions. A void finder run on an AP-distorted tracer field does
not return the same voids, and the AP signal in the cross-correlation is
reduced. Size: biases in the recovered parameters for all four finders tested
(REVOLVER, VIDE, voxel, Pylians spherical); the abstract gives no number
(arXiv:2407.02699). Consequence: the phrase "free of systematic errors"
attached to the 1% AP measurement of arXiv:1904.01030 predates this effect.
Validation test: stretched simulation boxes.

Read in the body of arXiv:2407.02699. With halos and voids both shifted by
hand, ε is recovered for nine fiducial cosmologies; with voids found in the
distorted halo field the fit is biased for all finders and "strongly favours
values of ε closer to one, regardless of the fiducial cosmology", that is,
towards the fiducial model [src: Sect. 5.1, Fig. 9; no number given]. The
effect sits in the quadrupole of the real-space correlation, exists for
voids found in real or redshift space, and depends on the algorithm.
Mitigations: measure the anisotropic real-space correlation (unbiased,
weaker), or iterate the fiducial cosmology until ε crosses 1 (voxel: fast,
unbiased; ZOBOV: unbiased, slow; spherical: fast, biased). The paper states
that arXiv:2008.06060, arXiv:2007.09013 and arXiv:2205.06258 "correctly
accounted for this bias" through their fiducial-cosmology term, and that a
result with ε near 1 is less affected but not guaranteed free of it
[src: Sect. 6].

Systematic budgets of the main void–galaxy analyses:

| Analysis | Term | Size | Place |
|---|---|---|---|
| SDSS six bins (arXiv:2205.06258), 250 MGS + 250 Patchy mocks at their own Ω_m and at 0.28, 0.34 | Mean offset (subtracted); scatter of offsets (added in quadrature) | fσ8: −0.0113; 0.0161. α_⊥/α_∥: 0.0029; 0.0061. Statistical errors per bin: 0.084 to +0.16/−0.23 and 0.019 to +0.044/−0.052, so the total equals the statistical error to one unit in the last digit | [src: Sect. 4.3, Table 3] |
| SDSS six bins (arXiv:2205.06258) | Largest single offset | fσ8: 0.0464 ± 0.0334 (MGS, Ω_m = 0.28); α_⊥/α_∥: −0.0167 ± 0.0055 (MGS, own cosmology); offsets significant at 2σ in two bins per parameter. The 84 NSERIES N-body mocks show none but are not in the budget (other footprint) | [src: Table 2, Sect. 4.1] |
| eBOSS DR16 LRG (arXiv:2008.06060) | Modelling; fiducial cosmology | Δfσ8 = 0.0144 (3%); Δ(α_⊥/α_∥) = 0.00417 ± 0.00390 (0.42%) from Nseries, the EZmocks giving < 0.00097; 0.8% on α_⊥/α_∥ at Ω_m = 0.350 against 0.286; "small compared to the statistical errors" | [src: Sect. 6.1–6.3] |
| eBOSS DR16 three tracers (arXiv:2007.09013), relative error on β, LRG / ELG / QSO | Binning; FKP weight; estimator; fiducial cosmology; linear RSD model; total | 4.8 / 2.3 / 1.4; 1.4 / 2.3 / 0.7; 2.2 / 3.3 / 1.0; 2.2 each; 9.0 / 8.3 / 39.9; 10.8 / 9.8 / 40.0 %. The quasar β carries a 40% modelling systematic. Finder run 1000 times per catalogue, as random buffer particles change the tessellation | [src: Table 7, Eq. 35, Sect. 3.3.1] |
| same model, re-tested | Offset on β | 0.031, against 0.037 in the original and a statistical error of 0.075 | arXiv:2008.06060 [src: App. A] |
| BOSS deprojection (arXiv:2007.07895) | Fiducial Ω_m 0.307 → 0.247, finder rerun | f/b and Ω_m move by less than their 68% regions | [src: Sect. 4.2.1] |

The SDSS six-bin covariance comes from 1000 mocks with the Percival et al.
(2021) posterior, fixed with cosmology [src: Sect. 3.6 of arXiv:2205.06258].

### 2.3 Tracer versus matter velocity profile
<!-- key: tracer-versus-matter-velocity-profile -->

Mechanism: void centres correlate with the particular realisation of sparse
tracers, so the tracer velocity profile inside voids differs from the matter
one. Size: differences of order 20% in the velocity profile, a few percent in
the Jacobian, and changes in the monopole and quadrupole comparable to the
effect of fσ8 at current statistical precision [src: abstract] (Massara et al. 2022,
arXiv:2206.14120).

### 2.4 Mock calibration
<!-- key: mock-calibration -->

Size: calibrating the BOSS model on survey mocks moves f/b from 0.540 ± 0.091
to 0.347 ± 0.023 [src: abstract]; the authors flag the calibrated result as
dependent on the cosmology and galaxy model of the mocks (arXiv:2007.07895).
Referee check: which numbers are calibration-free.

The calibration both shrinks the error several times and moves the central
value by more than the uncalibrated error [der].

### 2.5 Spurious (Poisson) voids
<!-- key: spurious-poisson-voids -->

Sparse tracers produce voids that are shot-noise fluctuations. The eBOSS DR14
quasar void catalogue "may be heavily contaminated" (arXiv:1909.04394). VSF
analyses apply a cleaning procedure for purity and completeness
(arXiv:2212.03873).

### 2.6 Bias conversion
<!-- key: bias-conversion -->

β from voids becomes fσ8 only with an external linear bias
(arXiv:2007.09013 takes it from the eBOSS consensus papers). Whether the bias
inside voids equals the large-scale linear bias is an assumption; void lensing
gives a direct check, 2.45 ± 0.36 for BOSS voids [src: abstract] (arXiv:2507.13450).

### 2.7 Mask, selection and photo-z
<!-- key: mask-selection-and-photo-z -->

Void catalogues from different selections of the same sky overlap poorly
(arXiv:2411.00148). For photometric voids, the "lensing-is-low" tension in the
CMB-lensing imprint of voids disappeared once mocks matched the sparseness and
redshift-error distribution of the data, calibrated with over one million DESI
spectra [src] (arXiv:2412.02761).

### 2.8 Lyα tomography specifics
<!-- key: lyalpha-tomography-specifics -->

The map resolution equals the mean sightline separation, so voids smaller than
that are not resolved; the finder threshold is calibrated on simulations and
checked through the void volume fraction (19.5% in data, 18.2% in simulation
[src: abstract], arXiv:1710.02612); the cross-correlation model must include the
sampling of the field along parallel sightlines (arXiv:2203.11045). Continuum
fitting, DLAs and metals propagate into the map; those are described in
`cosmo-lyman-alpha`.

## 3. Emulator-based small-scale statistics
<!-- key: emulator-based-small-scale-statistics -->

### 3.1 Galaxy–halo connection
<!-- key: galaxy-halo-connection -->

Mechanism: the cosmological dependence of a statistic at 1–30 h⁻¹Mpc is
entangled with how galaxies occupy halos. An emulator built on one HOD family
marginalises only within that family. Evidence that the family matters: the
SimBIG WST posterior on σ8 is not robust to a change of forward model at
k_max = 0.5 h Mpc⁻¹ (arXiv:2310.15250); standard HOD mocks underpredict DESI
multiplet clustering (arXiv:2511.15354); the DESI σ8 with simulation-based
priors is pulled down "driven by the quasar HOD assumptions" (Chudaykin, Ivanov
& Philcox 2026, arXiv:2602.18554). Mitigation: extended HODs with assembly
bias, recovery tests on mocks built with a different galaxy model
(arXiv:2501.01698, arXiv:2211.00660). The Beyond-2pt paper lists this as the
main obstacle to "correct cosmology constraints from the highly nonlinear
regime" (arXiv:2405.02252, §6.4 title). The non-HOD test of arXiv:2501.01698
is one Uchuu box populated by subhalo abundance matching (other N-body code,
Rockstar halos): ω_cdm, σ8 and n_s are recovered by the 2PCF, the MFs and
both, without assembly bias in the model; shown as contours, no offset
quoted [src: Sect. 4.3].

### 3.2 Emulator error
<!-- key: emulator-error -->

An emulator has its own error, which must enter the covariance. In the
Beyond-2pt challenge an underestimated emulation uncertainty on the
hexadecapole biased one submission and was found only after unmasking, on a
volume larger than earlier tests (arXiv:2405.02252). Referee check: emulator
error budget per data-vector element, and a recovery test at a volume well
above the survey's (84 times in arXiv:2309.16541, abstract).

Sizes in the BOSS density-split analysis (arXiv:2309.16541). The emulator,
trained on periodic boxes at one redshift, is applied to a survey with a
footprint, a radial selection and fibre collisions; the residual on the mean
of 84 Nseries mocks (120 h⁻³Gpc³ covariance) is Δω_cdm = 0.00015 ± 0.0018,
Δσ8 = 0.0129 ± 0.018, Δn_s = 0.0080 +0.020/−0.019, Δfσ8 = 0.0066 ± 0.011
(2σ), none significant; the 2σ scatter of the 84 best fits over √84 is added
in quadrature [src: Sect. 4.4.3]. Below about 20 h⁻¹Mpc the emulator error
dominates the monopoles, so those scales add little [src: Sect. 4.4.2].

The test is limited by the number of N-body mocks: a residual in σ8 of the
size measured, a sizeable fraction of the data error, cannot be excluded
[der].

### 3.3 Parameter-space restrictions of the simulation suite
<!-- key: parameter-space-restrictions-of-the-simulation -->

AbacusSummit-based emulators fix the angular sound-horizon scale θ_*, whereas
Quijote-based ones do not; EFT teams had to rerun with the same prior to be
comparable (arXiv:2405.02252). Analyses built on these suites derive H0 from a
fixed θ_* (stated in arXiv:2204.13717). Quoted errors on h or ω_cdm from such
analyses carry CMB information.

### 3.4 Model misspecification in neural posterior estimation
<!-- key: model-misspecification-in-neural-posterior -->

The SimBIG WST analysis reports that the inferred posterior varies
significantly across normalising-flow architectures, interpreted as model
misspecification (arXiv:2310.15250). Validation: simulation-based calibration
(coverage) and out-of-distribution test sets (arXiv:2211.00660).

### 3.5 Survey realism
<!-- key: survey-realism -->

Masks, veto masks, radial and angular selection, fibre collisions and
systematic weights alter non-two-point statistics in ways without analytic
corrections; they must be forward-modelled in every training mock
(arXiv:2211.00660, arXiv:2501.01698). Minkowski functionals on masked fields
need an unbiased boundary treatment (arXiv:2110.06109); the same paper reports
a low-significance north–south difference in LOWZ, a_0 = −0.080 ± 0.040
against 0.032 ± 0.024 [src: abstract], which may be a data systematic.

### 3.6 Fisher forecasts from periodic boxes
<!-- key: fisher-forecasts-from-periodic-boxes -->

Quijote Fisher gains refer to the matter or halo field in a 1 h⁻¹Gpc periodic
box. For tracers at BOSS-like density the marked power spectrum does not beat
P + B (arXiv:2411.14377). Never quote a matter-field Fisher gain as the
expected gain on a survey.

## 4. Higher-order weak lensing
<!-- key: higher-order-weak-lensing -->

Shear calibration, PSF and photometric redshifts are treated in
`cosmo-weak-lensing`. Specific to higher-order statistics:

### 4.1 Baryonic feedback
<!-- key: baryonic-feedback -->

Mechanism: feedback changes halo profiles, hence peaks, PDF tails and
small-scale skewness, not only the power spectrum. Size: up to 1σ bias in S8
for peaks, minima, PDF and scattering transform at 2′ smoothing with the
strongest feedback in IllustrisTNG and BAHAMAS mocks, for HSC Y1 depth; in the
HSC Y1 data the shift between including and excluding small scales is ≤ 0.5σ
[src: abstract] (Grandón et al. 2024, arXiv:2403.03807). DES Y3 persistent homology
reports biases under 0.3σ in the Ω_m–S8 plane [src: abstract] (arXiv:2506.13439).
Mitigation: scale cuts; a baryon correction model validated on several
hydrodynamical simulations (arXiv:2606.12389). The sibling skill records that
the strength of feedback is itself disputed; a robustness test is only as good
as the feedback models it spans.

Sizes read in bodies. KiDS-Legacy, ⟨M_ap³⟩ alone: omitting feedback biases
Ω_m low by 1σ, S8 by less [src: Sect. 5.4 of arXiv:2606.12389]. DES Y3
hybrid SBI: training simulations are dark matter only; 118 CosmoGridV1 mocks
with a baryon correction model must shift the result by less than 0.3σ in
the Ω_m–S8 plane and in w, which is passed with ℓ ≤ 1024 [src: Sect. 7.2,
5.4.2 of arXiv:2606.11309]: one baryon model at one cosmology.

### 4.2 Source clustering and reduced shear
<!-- key: source-clustering-and-reduced-shear -->

Source galaxies cluster with the lensing structure, which modulates noise and
signal at third order. Forward-modelled in the DES Y3 SBI analyses
(arXiv:2405.10881, arXiv:2403.02314) and corrected analytically in KiDS-Legacy
together with reduced shear (arXiv:2606.12389).

Read in the KiDS-Legacy body (arXiv:2606.12389): the correction is a factor per data point,
the ratio of simulated data vectors with and without the effect, not a
formula [src: Sect. 2.6]. For ⟨M_ap³⟩ alone, neglecting reduced shear moves
S8 up by 0.54σ, source clustering by 0.13σ, and a source bias of 0.7 or 1.3
by less than 0.1σ [src: Sect. 5.4].

### 4.3 Intrinsic alignments at third order
<!-- key: intrinsic-alignments-at-third-order -->

The IA model must be specified beyond two-point. KiDS-Legacy uses a model with
redshift and mass dependence (arXiv:2606.12389); HSC Y3 2+3-point detects no
significant IA (arXiv:2508.14019); DES SBI forward-models IA in the mocks
(arXiv:2405.10881). In KiDS-Legacy, four IA treatments (none, NLA, NLA-z,
NLA-M) give Ω_m and S8 within 1σ of each other for ⟨M_ap³⟩ alone; dropping IA
altogether lowers both [src: Sect. 5.4 of arXiv:2606.12389]. At low
redshift the third-order signal is dominated by IA, not lensing, so one
aperture radius is kept there [src: Sect. 5.2].

### 4.4 Simulation suite fidelity and coverage
<!-- key: simulation-suite-fidelity-and-coverage -->

An SBI posterior is only calibrated within the support and physics of the
training simulations. Tests: coverage (arXiv:2606.11309); consistency between
statistics, p > 0.1 for all combinations in DES Y3 (arXiv:2405.10881, abstract).
Non-Gaussian shape noise and mask must be in the mocks (arXiv:2403.02314).

A documented failure and repair (arXiv:2606.11309). Coverage is tested with
TARP in the joint (Ω_m, S8, w) space [src: Sect. 7.1]. After unblinding, a
software bug was found to have hidden overconfidence and bias, mainly in the
Ω_m–w plane, the density estimators conditioning poorly on cosmology. A
regularisation term was added to the compression and the ensemble enlarged
from 4 to 8 flows; the 2D posteriors moved by less than 0.3σ [src: Sect.
7.5]. Pre-unblinding checks worth copying: the compressed data must fall
inside the cloud of compressed simulations, and each density estimator must
converge on the data with its mean hidden [src: Sect. 7.4].

Conventional third-order likelihood: KiDS-Legacy has 1944 mock realisations,
which caps the data vector at 291 entries (126 COSEBIs); ⟨M_ap³⟩ is cut down
accordingly (equilateral apertures, one scale at low redshift, merged bins)
and the sample covariance is rescaled to the measured signal [src: Sect.
4.4, 5.2, Eqs. 28–32 of arXiv:2606.12389].

### 4.5 Prior bounds
<!-- key: prior-bounds -->

The DES Y3 SBI wCDM analyses impose −1 < w < −1/3 (arXiv:2403.02314, Sect. 4.2): the
quoted "w < −0.80" (abstract) is a one-sided limit against a prior edge, not a
measurement of w, and cannot be compared with w0 = −1.39 ± 0.31 from the 2+3
point analysis (arXiv:2508.14018, abstract), which allows w < −1.

### 4.6 Redshift calibration inherited from the two-point analysis
<!-- key: redshift-calibration-inherited-from-the-two -->

A higher-order statistic uses the same n(z). ⟨M_ap³⟩ can self-calibrate the
mean-redshift nuisance of the highest DES bin with little loss
(arXiv:2508.14018), but it cannot repair a calibration that is wrong in a way
the nuisance model does not span.

Assumptions read in the bodies. DES Y3: one Δz_i and one m_i per bin, with
(1 + m)³ on the three-point function; NLA (amplitude, redshift slope) at
both orders, where the fiducial two-point analysis used TATT; covariance
from 796 CosmoGridV1 mocks [src: Sect. III.4, II.2, Eqs. 13–17 of
arXiv:2508.14018]. HSC Y3: Gaussian priors of about 2% on Δz in the two
low-redshift bins, flat between −1 and 1 in the two high-redshift ones
[src: Sect. IV.2.2 of arXiv:2508.14019].

## 5. Field-level inference
<!-- key: field-level-inference -->

### 5.1 Likelihood (noise model) misspecification
<!-- key: likelihood-noise-model-misspecification -->

Mechanism: the field-level likelihood needs the full distribution of the
residual between model and data at every mode, not only its power spectrum.
Size: fitting data with non-Gaussian noise using a Gaussian field-level
likelihood gives "significant biases" in the cosmological parameters; the
authors call the correct likelihood "the primary challenge" for smaller
scales (arXiv:2509.09673). Summary-statistic analyses are less exposed because
the central limit theorem Gaussianises band powers.

The tests, read in the body of arXiv:2509.09673. Poisson noise added to a *linear* Gaussian
signal leaves the Gaussian field-level likelihood unbiased at k_max = 0.12
h Mpc⁻¹, since only power-spectrum information is used; with the non-linear
signal b_1(δ_1 + G_2) it is biased, while P + B with the noise bispectrum
B_ε = 1/n̄² is not [src: Sect. VII.1, Eqs. 55–58; contours, no number].
On N-body halos the authors' Gaussian-likelihood pipeline "fails to
converge", the noise amplitude decreasing without limit [src: Sect. VII.3].
Their runs: eight NUTS chains, at least 10³ effective samples [src: Sect.
III.2.3].

### 5.2 Forward-model accuracy and resolution
<!-- key: forward-model-accuracy-and-resolution -->

BORG moved from second-order LPT, valid above about 6 h⁻¹Mpc
(arXiv:1203.3639), to particle-mesh (arXiv:1806.11117). For f_NL the
constraint improves with resolution and was tested against the choice of
structure-formation model (arXiv:2603.20855). Validation: posterior predictive
tests of the power spectrum, bispectrum, Gaussianity of the initial conditions
and the halo mass function (arXiv:2505.10682).

### 5.3 Survey systematics inside the forward model
<!-- key: survey-systematics-inside-the-forward-model -->

Foreground contamination, selection and masks must be modelled at the field
level, since there is no later stage at which to apply weights. The BOSS
analysis marginalises over known and unknown foreground templates and returns
maps of residual systematics (arXiv:1909.06396); the Quaia analysis imposes
conservative sky cuts (arXiv:2602.02363). The external check used by both is
the cross-correlation with Planck CMB lensing.

### 5.4 Sampler performance
<!-- key: sampler-performance -->

The redshift-space information study states that realising the gains "will
require substantial developments on the modeling of observations and
observational systematics as well as on the numerical inference techniques"
(arXiv:2609.16719). No convergence diagnostics were read this session; ask for
effective sample sizes of the cosmological parameters and of the largest-scale
modes.

Read on 2026-10-13. BORG on 2M++: burn-in is tested from a field ten times
too low in amplitude; power spectrum and one-point distribution reach their
targets after about 4000 transitions; no effective sample size in the
sections read [src: Sect. 4.3 of arXiv:1806.11117]. LEFTfield
(arXiv:2403.03220): effective sample size of the amplitude α of 200 and 100
at k_max = 0.10 and 0.12 h Mpc⁻¹ for one halo sample, 180 and 60 for the
other [src: Table 1, App. B.3]; chains from different initialisations agree;
two cross-check chains reached about 21 and 13 effective samples [src: App.
A.2, A.4]. The factors 3.5–5.2 thus compare error bars estimated from
60–200 independent samples on the field-level side. The P + B posterior is
trained in sequential rounds that narrow the prior, then checked by
simulation-based calibration and against the number of simulations; adding
non-Gaussian stochastic terms to P + B changes little [src: App. A.3, B.4,
B.5].

### 5.5 Baryons and intrinsic alignments in field-level lensing
<!-- key: baryons-and-intrinsic-alignments-in-field-level -->

Included in BORG-WL through an enthalpy-gradient-descent model and TATT; the
paper illustrates the bias from a misspecified baryon model on synthetic data
(arXiv:2304.04785).

### 5.6 Neural field-level methods
<!-- key: neural-field-level-methods -->

The answer depends on the training simulations. The LiFT validation set
differs from the training set in gravity solver, halo finder, HOD, cosmology
and fibre-assignment history, and includes mocks analysed with a distorted
distance–redshift relation (arXiv:2609.14862). Referee check: was the network
tested on a cosmology and a galaxy model it never saw, and is the BAO shift
unbiased there.

### 5.7 Gaussian field-level likelihood
<!-- key: gaussian-field-level-likelihood -->

The systematic is the covariance model: its wavenumber integration range, its
validity in separation, wide-angle terms and the zero-point calibration
(arXiv:2209.04166, arXiv:2501.16852). Details and
the damping-parameter issue are in `cosmo-peculiar-velocities`.

## 6. Simulation-based inference
<!-- key: simulation-based-inference -->

### 6.1 Sensitivity to the simulation ingredients
<!-- key: sensitivity-to-the-simulation-ingredients -->

For a DESI-LRG-like density, with P_ℓ and B0: inference is insensitive to
replacing N-body by particle-mesh gravity; changing the halo finder from
friends-of-friends to Rockstar can bias σ8 from the bispectrum; training on a
complex HOD works on simpler data, but training on a simple HOD fails on data
from a more complex one (Modi et al. 2023, arXiv:2309.15071).

Detail from the body of arXiv:2309.15071 (no shift quoted as a number). Gravity: residuals and
coverage agree between N-body and particle-mesh training (friends-of-friends
halos, 10-parameter HOD) [src: Sect. 5.1]. Halo finder: Ω_m and the
power-spectrum σ8 are unbiased, but with the bispectrum a model trained on
friends-of-friends halos "consistently under-predicts σ8" on Rockstar data,
and the reverse biases it high [src: Sect. 5.2]. Galaxy model: a
5-parameter training set on 10-parameter data fails, the power spectrum
sometimes, the bispectrum "almost always", "aggravated as the summary
statistics used become more informative" [src: Sect. 5.3]. The SimBIG test
sets change several ingredients at once and sit at one cosmology, so they
do not isolate the halo-finder effect [src: Sect. 5.2].

### 6.2 Robustness is statistic-dependent
<!-- key: robustness-is-statistic-dependent -->

Within one forward model (SimBIG), the bispectrum and CNN analyses pass the
changed-forward-model test (arXiv:2310.15243, arXiv:2310.15256) while the WST
fails for σ8 at small scales (arXiv:2310.15250). Passing for one statistic
says nothing about another.

| Statistic | What the test showed | Place |
|---|---|---|
| Wavelet scattering | On TEST2 (AbacusSummit, CompaSO) σ8 posteriors lie "almost always below" the truth; removing scales j < 2 (k ≳ 0.3 h Mpc⁻¹) restores consistency. On data the cut moves σ8 from 0.84 ± 0.03 to 0.75 ± 0.05 and Ω_m from 0.28 ± 0.04 to 0.25 ± 0.03 (SimBIG P_ℓ: σ8 = 0.81 ± 0.07): three times the quoted σ8 error | arXiv:2310.15250 [src: Sect. III.1, Table 2] |
| CNN | Dropout and ℓ2 penalties were raised "through trial-and-error" until TEST1 and TEST2 were passed; a third, untouched set "would be ideal" but was unaffordable. Robustness is shown on the sets it was tuned on | arXiv:2310.15256 [src: Sect. III.1, II.3] |
| Bispectrum | Coverage on 2000 held-out simulations: ranks near uniform, slight ∩ shape for Ω_m and σ8 (posteriors slightly too broad) | arXiv:2310.15243 [src: Sect. III.4] |
| All | The three test sets sit at fixed cosmologies, so a rank test on them is distorted by the prior; posterior means and widths are compared between sets instead. Every set, in or out of distribution, is an HOD population of dark-matter halos | arXiv:2211.00660 [src: Sect. IV, V] |

### 6.3 Coverage is not accuracy
<!-- key: coverage-is-not-accuracy -->

Simulation-based calibration tests the posterior against the training
distribution. It cannot detect that the data lie outside it. The Beyond-2pt
paper makes the same point about its own challenge (arXiv:2405.02252).

### 6.4 Small volumes
<!-- key: small-volumes -->

The SimBIG results use about 10% of BOSS (arXiv:2310.15243, abstract). The Beyond-2pt SBI entry was trained
on (1 h⁻¹Gpc)³ boxes against (2 h⁻¹Gpc)³ for the others and trimmed the largest
scales, which widened its Ω_m posterior (arXiv:2405.02252). Scaling the number
and volume of simulations to DESI is the stated bottleneck (arXiv:2309.15071).

## 7. What a referee checks in a beyond-two-point results section
<!-- key: what-a-referee-checks-in-a-beyond-two-point -->

1. Which data, which release, what fraction of the survey (SimBIG: 10% of
   BOSS, arXiv:2310.15243, abstract; emulator analyses: CMASS at 0.45–0.6 only, arXiv:2309.16541, Sect. 2.1).
2. The baseline of every quoted gain, and whether that baseline is optimal.
3. Covariance: number of mocks against data-vector length; approximate or
   N-body mocks; whether a different mock set changes the significance.
4. Galaxy–halo model: HOD family, assembly bias, test on a non-HOD mock.
5. Emulator or network error in the covariance; recovery test at a volume
   above the survey's.
6. Simulation-suite restrictions that carry external information (fixed θ_*,
   prior edges such as −1 < w < −1/3).
7. Coverage test *and* out-of-distribution test for any neural posterior;
   stability across architectures.
8. For voids: finder, reconstruction before finding, AP response of the
   finder, calibration-free or mock-calibrated, source of the bias used to
   turn β into fσ8.
9. For lensing: baryon test with more than one feedback model, source
   clustering, IA at third order, which redshift calibration.
10. For field-level work: which of the three meanings; noise model; what is
    sampled; whether cosmology is varied; effective sample size.
11. For tomography voids: map resolution against void size, finder threshold
    calibration, sampling of the field along sightlines.
12. Blinding: of the data, or only of a mock challenge.
13. Posterior mean against best fit in extended models (prior-volume effects).
14. Whether a "detection" survives a cross-correlation between independent
    sky patches.
