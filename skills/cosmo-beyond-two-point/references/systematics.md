# Systematics — statistics beyond the two-point function

Scope: the systematic effects specific to higher-order, void, field-level and simulation-based analyses, with sizes where a paper quantifies them.
Snapshot: 2026-10-07


## 1. Bispectrum and N-point functions

### 1.1 Number of mocks versus length of the data vector

Mechanism: the sample covariance of N_b bins from N_m mocks is singular or
badly biased when N_b approaches N_m. Size: with the BOSS mock set the standard
binning held 116 triangles; compression allowed 2734 and cut the credible
intervals on (b1, b2, f, σ8) by 24.8%, 52.8%, 26.4%, 21% [src]
(arXiv:1806.02853), and by 39%, 49%, 29%, 22% with geometrical compression
[src] (arXiv:1901.00987). Mitigation: compression, analytic covariance,
window-free estimators. Referee check: N_m, N_b, and the Hartlap or Percival
factor applied (those corrections are in `cosmo-statistics-inference`).

### 1.2 Fibre collisions in three-point statistics

Mechanism: missing close pairs alter every triangle with a small side. The
independent DESI DR1 reanalysis introduces a stochastic estimator for fibre
collisions specifically to make the bispectrum usable (arXiv:2507.13433). The
collaboration treatment for two-point statistics is in
`cosmo-galaxy-clustering`.

### 1.3 Mock realism for the four-point covariance

Mechanism: a χ² of the parity-odd 4PCF against mocks is biased if the
parity-even eight-point function of the data differs from that of the mocks.
Size: in BOSS the 8PCF bias term is about 6σ while the genuine parity signal is
0–2.5σ [src] (arXiv:2407.03397); replacing Patchy by GLAM-Uchuu mocks moves the
significance from > 3.5σ to 1.4σ [src] (arXiv:2401.09523). In DESI DR1 the auto
analysis gives 4–10σ and the cross-patch analysis gives nothing [src]
(arXiv:2508.09133). Mitigation: cross-correlation between independent patches,
χ²_× and χ²_null, compressed statistics with direct mock covariance
(arXiv:2604.06021). The lesson generalises: a higher-order "detection"
expressed as a χ² against approximate mocks is a statement about the mocks
until shown otherwise.

### 1.4 Range of validity of the perturbative model

Tree-level bispectrum fits are restricted to large scales: the BOSS
compression papers used 0.03–0.12 h Mpc⁻¹ [src] (arXiv:1806.02853). The one-loop
model reaches higher k at the price of many more nuisance parameters
(arXiv:2206.08327, arXiv:2507.22110). Validation standard: fits to N-body
boxes of volume far above the survey's, such as the PT Challenge suite used in
arXiv:2302.04414 or the 200 h⁻³Gpc³ of AbacusSummit used in arXiv:2610.08908.

### 1.5 Prior-volume (projection) effects

With many EFT nuisance parameters the marginal posterior means move away from
the best fit in extended models. The DESI P + B analysis uses ShapeFit
compression explicitly "to mitigate prior volume effects" (arXiv:2606.23936);
arXiv:2610.01836 reports that the w0wa region "remains sensitive to the adopted
prior ranges". The quantified shifts for the power spectrum alone are in
`cosmo-galaxy-clustering`.

## 2. Cosmic voids

### 2.1 RSD in the void positions (selection bias)

Mechanism: voids found in redshift space are preferentially those elongated or
aligned so that RSD deepen them; the stack is then anisotropic for a reason
that the galaxy-velocity model does not contain. Mitigation: remove RSD from
the galaxy field by velocity reconstruction before void finding, introduced in
arXiv:1904.01030 and used in arXiv:2008.06060 and arXiv:2205.06258; the result
depends on the reconstruction efficiency, studied for Euclid in Radinović et
al. 2023 (arXiv:2302.05302).

### 2.2 Response of the void finder to the fiducial cosmology

Mechanism: analyses assume that void centres transform under the AP distortion
like galaxy positions. A void finder run on an AP-distorted tracer field does
not return the same voids, and the AP signal in the cross-correlation is
reduced. Size: biases in the recovered parameters for all four finders tested
(REVOLVER, VIDE, voxel, Pylians spherical); the abstract gives no number
(arXiv:2407.02699). Consequence: the phrase "free of systematic errors"
attached to the 1% AP measurement of arXiv:1904.01030 predates this effect.
Validation test: stretched simulation boxes.

### 2.3 Tracer versus matter velocity profile

Mechanism: void centres correlate with the particular realisation of sparse
tracers, so the tracer velocity profile inside voids differs from the matter
one. Size: differences of order 20% in the velocity profile, a few percent in
the Jacobian, and changes in the monopole and quadrupole comparable to the
effect of fσ8 at current statistical precision [src] (Massara et al. 2022,
arXiv:2206.14120).

### 2.4 Mock calibration

Size: calibrating the BOSS model on survey mocks moves f/b from 0.540 ± 0.091
to 0.347 ± 0.023 [src], a factor four in precision and a shift of 2.1 times
the uncalibrated error [der: (0.540 − 0.347)/0.091]; the
authors flag the calibrated result as dependent on the cosmology and galaxy
model of the mocks (arXiv:2007.07895). Referee check: which numbers are
calibration-free.

### 2.5 Spurious (Poisson) voids

Sparse tracers produce voids that are shot-noise fluctuations. The eBOSS DR14
quasar void catalogue "may be heavily contaminated" (arXiv:1909.04394). VSF
analyses apply a cleaning procedure for purity and completeness
(arXiv:2212.03873).

### 2.6 Bias conversion

β from voids becomes fσ8 only with an external linear bias
(arXiv:2007.09013 takes it from the eBOSS consensus papers). Whether the bias
inside voids equals the large-scale linear bias is an assumption; void lensing
gives a direct check, 2.45 ± 0.36 for BOSS voids [src] (arXiv:2507.13450).

### 2.7 Mask, selection and photo-z

Void catalogues from different selections of the same sky overlap poorly
(arXiv:2411.00148). For photometric voids, the "lensing-is-low" tension in the
CMB-lensing imprint of voids disappeared once mocks matched the sparseness and
redshift-error distribution of the data, calibrated with over one million DESI
spectra [src] (arXiv:2412.02761).

### 2.8 Lyα tomography specifics

The map resolution equals the mean sightline separation, so voids smaller than
that are not resolved; the finder threshold is calibrated on simulations and
checked through the void volume fraction (19.5% in data, 18.2% in simulation
[src], arXiv:1710.02612); the cross-correlation model must include the
sampling of the field along parallel sightlines (arXiv:2203.11045). Continuum
fitting, DLAs and metals propagate into the map; those are described in
`cosmo-lyman-alpha`.

## 3. Emulator-based small-scale statistics

### 3.1 Galaxy–halo connection

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
regime" (arXiv:2405.02252, §6.4 title).

### 3.2 Emulator error

An emulator has its own error, which must enter the covariance. In the
Beyond-2pt challenge an underestimated emulation uncertainty on the
hexadecapole biased one submission and was found only after unmasking, on a
volume larger than earlier tests (arXiv:2405.02252). Referee check: emulator
error budget per data-vector element, and a recovery test at a volume well
above the survey's (84 times in arXiv:2309.16541).

### 3.3 Parameter-space restrictions of the simulation suite

AbacusSummit-based emulators fix the angular sound-horizon scale θ_*, whereas
Quijote-based ones do not; EFT teams had to rerun with the same prior to be
comparable (arXiv:2405.02252). Analyses built on these suites derive H0 from a
fixed θ_* (stated in arXiv:2204.13717). Quoted errors on h or ω_cdm from such
analyses carry CMB information.

### 3.4 Model misspecification in neural posterior estimation

The SimBIG WST analysis reports that the inferred posterior varies
significantly across normalising-flow architectures, interpreted as model
misspecification (arXiv:2310.15250). Validation: simulation-based calibration
(coverage) and out-of-distribution test sets (arXiv:2211.00660).

### 3.5 Survey realism

Masks, veto masks, radial and angular selection, fibre collisions and
systematic weights alter non-two-point statistics in ways without analytic
corrections; they must be forward-modelled in every training mock
(arXiv:2211.00660, arXiv:2501.01698). Minkowski functionals on masked fields
need an unbiased boundary treatment (arXiv:2110.06109); the same paper reports
a low-significance north–south difference in LOWZ, a_0 = −0.080 ± 0.040
against 0.032 ± 0.024 [src], which may be a data systematic.

### 3.6 Fisher forecasts from periodic boxes

Quijote Fisher gains refer to the matter or halo field in a 1 h⁻¹Gpc periodic
box. For tracers at BOSS-like density the marked power spectrum does not beat
P + B (arXiv:2411.14377). Never quote a matter-field Fisher gain as the
expected gain on a survey.

## 4. Higher-order weak lensing

Shear calibration, PSF and photometric redshifts are treated in
`cosmo-weak-lensing`. Specific to higher-order statistics:

### 4.1 Baryonic feedback

Mechanism: feedback changes halo profiles, hence peaks, PDF tails and
small-scale skewness, not only the power spectrum. Size: up to 1σ bias in S8
for peaks, minima, PDF and scattering transform at 2′ smoothing with the
strongest feedback in IllustrisTNG and BAHAMAS mocks, for HSC Y1 depth; in the
HSC Y1 data the shift between including and excluding small scales is ≤ 0.5σ
[src] (Grandón et al. 2024, arXiv:2403.03807). DES Y3 persistent homology
reports biases under 0.3σ in the Ω_m–S8 plane [src] (arXiv:2506.13439).
Mitigation: scale cuts; a baryon correction model validated on several
hydrodynamical simulations (arXiv:2606.12389). The sibling skill records that
the strength of feedback is itself disputed; a robustness test is only as good
as the feedback models it spans.

### 4.2 Source clustering and reduced shear

Source galaxies cluster with the lensing structure, which modulates noise and
signal at third order. Forward-modelled in the DES Y3 SBI analyses
(arXiv:2405.10881, arXiv:2403.02314) and corrected analytically in KiDS-Legacy
together with reduced shear (arXiv:2606.12389).

### 4.3 Intrinsic alignments at third order

The IA model must be specified beyond two-point. KiDS-Legacy uses a model with
redshift and mass dependence (arXiv:2606.12389); HSC Y3 2+3-point detects no
significant IA (arXiv:2508.14019); DES SBI forward-models IA in the mocks
(arXiv:2405.10881).

### 4.4 Simulation suite fidelity and coverage

An SBI posterior is only calibrated within the support and physics of the
training simulations. Tests: coverage (arXiv:2606.11309); consistency between
statistics, p > 0.1 for all combinations in DES Y3 (arXiv:2405.10881).
Non-Gaussian shape noise and mask must be in the mocks (arXiv:2403.02314).

### 4.5 Prior bounds

The DES Y3 SBI wCDM analyses impose −1 < w < −1/3 (arXiv:2403.02314): the
quoted "w < −0.80" is a one-sided limit against a prior edge, not a
measurement of w, and cannot be compared with w0 = −1.39 ± 0.31 from the 2+3
point analysis (arXiv:2508.14018), which allows w < −1.

### 4.6 Redshift calibration inherited from the two-point analysis

A higher-order statistic uses the same n(z). ⟨M_ap³⟩ can self-calibrate the
mean-redshift nuisance of the highest DES bin with little loss
(arXiv:2508.14018), but it cannot repair a calibration that is wrong in a way
the nuisance model does not span.

## 5. Field-level inference

### 5.1 Likelihood (noise model) misspecification

Mechanism: the field-level likelihood needs the full distribution of the
residual between model and data at every mode, not only its power spectrum.
Size: fitting data with non-Gaussian noise using a Gaussian field-level
likelihood gives "significant biases" in the cosmological parameters; the
authors call the correct likelihood "the primary challenge" for smaller
scales (arXiv:2509.09673). Summary-statistic analyses are less exposed because
the central limit theorem Gaussianises band powers.

### 5.2 Forward-model accuracy and resolution

BORG moved from second-order LPT, valid above about 6 h⁻¹Mpc
(arXiv:1203.3639), to particle-mesh (arXiv:1806.11117). For f_NL the
constraint improves with resolution and was tested against the choice of
structure-formation model (arXiv:2603.20855). Validation: posterior predictive
tests of the power spectrum, bispectrum, Gaussianity of the initial conditions
and the halo mass function (arXiv:2505.10682).

### 5.3 Survey systematics inside the forward model

Foreground contamination, selection and masks must be modelled at the field
level, since there is no later stage at which to apply weights. The BOSS
analysis marginalises over known and unknown foreground templates and returns
maps of residual systematics (arXiv:1909.06396); the Quaia analysis imposes
conservative sky cuts (arXiv:2602.02363). The external check used by both is
the cross-correlation with Planck CMB lensing.

### 5.4 Sampler performance

The redshift-space information study states that realising the gains "will
require substantial developments on the modeling of observations and
observational systematics as well as on the numerical inference techniques"
(arXiv:2609.16719). No convergence diagnostics were read this session; ask for
effective sample sizes of the cosmological parameters and of the largest-scale
modes.

### 5.5 Baryons and intrinsic alignments in field-level lensing

Included in BORG-WL through an enthalpy-gradient-descent model and TATT; the
paper illustrates the bias from a misspecified baryon model on synthetic data
(arXiv:2304.04785).

### 5.6 Neural field-level methods

The answer depends on the training simulations. The LiFT validation set
differs from the training set in gravity solver, halo finder, HOD, cosmology
and fibre-assignment history, and includes mocks analysed with a distorted
distance–redshift relation (arXiv:2609.14862). Referee check: was the network
tested on a cosmology and a galaxy model it never saw, and is the BAO shift
unbiased there.

### 5.7 Gaussian field-level likelihood

The systematic is the covariance model: its wavenumber integration range, its
validity in separation, and wide-angle terms (arXiv:2501.16852). Details and
the damping-parameter issue are in `cosmo-peculiar-velocities`.

## 6. Simulation-based inference

### 6.1 Sensitivity to the simulation ingredients

For a DESI-LRG-like density, with P_ℓ and B0: inference is insensitive to
replacing N-body by particle-mesh gravity; changing the halo finder from
friends-of-friends to Rockstar can bias σ8 from the bispectrum; training on a
complex HOD works on simpler data, but training on a simple HOD fails on data
from a more complex one (Modi et al. 2023, arXiv:2309.15071).

### 6.2 Robustness is statistic-dependent

Within one forward model (SimBIG), the bispectrum and CNN analyses pass the
changed-forward-model test (arXiv:2310.15243, arXiv:2310.15256) while the WST
fails for σ8 at small scales (arXiv:2310.15250). Passing for one statistic
says nothing about another.

### 6.3 Coverage is not accuracy

Simulation-based calibration tests the posterior against the training
distribution. It cannot detect that the data lie outside it. The Beyond-2pt
paper makes the same point about its own challenge (arXiv:2405.02252).

### 6.4 Small volumes

The SimBIG results use about 10% of BOSS. The Beyond-2pt SBI entry was trained
on (1 h⁻¹Gpc)³ boxes against (2 h⁻¹Gpc)³ for the others and trimmed the largest
scales, which widened its Ω_m posterior (arXiv:2405.02252). Scaling the number
and volume of simulations to DESI is the stated bottleneck (arXiv:2309.15071).

## 7. What a referee checks in a beyond-two-point results section

1. Which data, which release, what fraction of the survey (SimBIG: 10% of
   BOSS; emulator analyses: CMASS at 0.45–0.6 only).
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
