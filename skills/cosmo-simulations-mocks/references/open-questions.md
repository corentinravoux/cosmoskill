# Open questions and misconceptions — cosmological simulations and mocks

Scope: live debates, internal tensions between suites, and stale claims with the paper that corrects each.
Snapshot: 2026-10-16

## 1. Live debates
<!-- key: live-debates -->

### 1.1 How strong is baryonic feedback, and which simulation variant is right?
<!-- key: how-strong-is-baryonic-feedback-and-which -->

**For strong feedback.**
- DES Y3 lensing with ACT DR5 kSZ gives a mean feedback scenario more extreme than most hydrodynamical simulations (arXiv:2404.06098).
- DESI Y1 × ACT kSZ disfavours fiducial feedback models at more than 3σ across FLAMINGO, ANTILLES, BAHAMAS, SIMBA and FABLE, in a like-for-like comparison that models halo-mass selection, miscentring and satellites; stronger-AGN variants and SIMBA are within 2σ (arXiv:2510.15822).
- eROSITA gas fractions are 2× lower than the fiducial 1 Gpc FLAMINGO run and the kSZ data are more than 8σ away from it; the variant with the most gas expulsion fits (arXiv:2509.10455).
- Jointly, 10 ± 2% suppression at k = 1 h/Mpc (arXiv:2512.02954).

**Against, or for caution.**
- A model-independent ratio of kSZ to galaxy–galaxy lensing for DESI DR2 galaxies is tracked most closely by fiducial FLAMINGO, with a mild north–south discrepancy in one bin that may indicate residual systematics (arXiv:2609.22466).
- The X-ray sample that the fiducial simulations were calibrated to prefers 5 ± 4% at k = 1 h/Mpc (arXiv:2512.02954).
- The FLAMINGO team notes that its strongest-feedback response is compatible with lensing-plus-external-data analyses and in strong tension with the X-ray gas fractions used for calibration (arXiv:2410.17109). The disagreement is therefore between gas observables as much as between simulations and data.

**What it means for a reader.** "FLAMINGO" or "BAHAMAS" is not one prediction; the variant must be named. A cosmic-shear analysis that marginalises a baryon model with a simulation-based prior inherits the calibration data of that simulation. The lensing-side view of this debate, with the DES 6×2pt result that favours weak feedback, is in `cosmo-weak-lensing` and `cosmo-cmb-lss-cross-correlations`.

### 1.2 Is percent-level gravity-only accuracy still the bottleneck?
<!-- key: is-percent-level-gravity-only-accuracy-still -->

- Codes agree to 1% to k = 10 h/Mpc when tuned (arXiv:2112.09138, arXiv:2605.28581), and emulators reach 1% (arXiv:2010.11288).
- The baryonic response at k = 1 h/Mpc is uncertain between 5% and 10% (arXiv:2512.02954).
- One view: effort should move from gravity-only precision to gas calibration and bracketing hydrodynamical suites (arXiv:1905.06082 already argued for combining probes to constrain baryons).
- The other: the gravity-only reference must stay well below the baryonic uncertainty so that the two do not become degenerate, and it still limits halo statistics (the halo mass function spread between resolutions was reduced to 1% only in 2026, arXiv:2605.28581).

### 1.3 Initial conditions: late 3LPT or early low order?
<!-- key: initial-conditions-late-3lpt-or-early-low-order -->

- The recommendation from controlled tests is to start late with 3LPT (arXiv:2008.09588), after 2LPT replaced Zel'dovich starts in 2006 (arXiv:astro-ph/0606505).
- FLAMINGO follows it: multi-fluid 3LPT at z = 31, "as late as possible" (arXiv:2306.04024, section 2.4).
- The Euclid Flagship 2 run started at z = 99 with 1LPT (arXiv:2405.13495, section 2.1). Its validation section rests on the code comparisons (1% between codes to k = 10 h/Mpc), on the 10⁹ M_⊙/h requirement and on a comparison of the measured P(k) with EuclidEmulator2 and BACCO, with HALOFIT and HMcode-2020 deviating by up to ±5% at k > 0.1 h/Mpc; it contains no test of the starting redshift or of the LPT order [src: Sect. 2.2 of arXiv:2405.13495].
- What the controlled tests say about such a start: with 1024³ particles in 512 Mpc/h, a Zel'dovich start needs z_i ≳ 200 for percent accuracy on P(k) at z = 0 [src: Sect. 3.1 of arXiv:1503.05920]; with 1024³ in 1 Gpc/h, Zel'dovich starts at z = 49 to 199 are accurate only to about a tenth of the particle Nyquist wavenumber, and the authors estimate a 4% deficit at k about 4 h/Mpc for runs started at z = 200 with the Zel'dovich approximation, among which they count the runs of the first EuclidEmulator, and 1.5% for the BACCO runs started at z = 49 with 2LPT [src: Sect. 5.2.2 of arXiv:2008.09588]. The EuclidEmulator2 training runs also use first-order LPT, at z = 99 [src: Sect. 3.3 of arXiv:2010.11288]. These estimates are made at a mass resolution 80 times coarser than Flagship 2 [der: 8.04 × 10¹⁰ against 10⁹ M_⊙/h] and are not measurements on it; the dependence on resolution goes towards earlier optimal starts at higher resolution [src: Sect. 6 of arXiv:2008.09588]. No paper read here measures the transient of the Flagship 2 run itself.

### 1.4 Is the HOD good enough for Stage-IV small-scale analyses?
<!-- key: is-the-hod-good-enough-for-stage-iv-small-scale -->

- The mass-only HOD fails by 15% against TNG300 (arXiv:1911.02610).
- DESI treats the residual as a measured systematic: 0.19% on α_AP for BAO, a covariance term for the full shape, with shifts often above 20% of the statistical error (arXiv:2404.03008, arXiv:2411.12023).
- For statistics beyond two-point, validation rests on one N-body suite and one occupation family (`cosmo-beyond-two-point`).
- Open: whether extended HODs span the space that hydrodynamical simulations and semi-analytic models occupy, and whether any hydrodynamical simulation is right about assembly bias.

### 1.5 Mock covariance or analytic covariance?
<!-- key: mock-covariance-or-analytic-covariance -->

- DESI DR1 answers differently for two statistics: analytic for the post-reconstruction correlation function, corrected mocks for the power spectrum (arXiv:2411.12027).
- Approximate mocks reproduce parameter errors to 10% (arXiv:1806.09497), which is comparable with, or larger than, the finite-mock corrections.
- That 10% is measured in periodic boxes at z = 1, where a Gaussian covariance with a non-linear spectrum does as well as the mocks [src: Sect. 6 of arXiv:1806.09497]. On the DESI DR1 survey geometry the EZmock covariance gave BAO uncertainties about 10% smaller than a data-tuned analytic covariance and was rescaled by 10 to 40% for the full-shape analysis, while the analytic Fourier-space covariance differed from the mock one by about 10% element by element [src: Sects. 4 and 5 of arXiv:2411.12027]. Neither estimate is a reference for the other; the open question is which one is closer to the truth for a fibre-assigned survey.
- Control-variate estimators that pair each mock with a Zel'dovich realisation were proposed in 2026 to cut the number of mocks needed (title and abstract read, outside the source list).

### 1.6 Is the local Universe underdense in the constrained simulations?
<!-- key: is-the-local-universe-underdense-in-the -->

- SIBELIUS-DARK finds a large-scale underdensity of about 5% within 200 Mpc and an unusually high number of very massive clusters (arXiv:2202.04099).
- Manticore-Local finds no evidence for a large local underdensity (arXiv:2505.10682).
- The two use different inference set-ups; neither abstract reconciles them. The question bears on local-void explanations of the Hubble tension, treated in `cosmo-distance-ladder-h0`.

### 1.7 How should a constrained simulation be validated?
<!-- key: how-should-a-constrained-simulation-be-validated -->

- Internal: posterior-predictive checks against ΛCDM statistics (arXiv:2505.10682, arXiv:2606.10020).
- External: Bayesian evidence against direct distance tracers (arXiv:2502.00121); CMB lensing at 7.4σ and kSZ at 3.5σ (arXiv:2606.10020).
- Object level: matched clusters (arXiv:2505.10682, arXiv:2602.03699).
- Open: there is no agreed benchmark across groups; the velocity comparison of arXiv:2502.00121 is the closest thing to one, and its by-product S8 = 0.793 ± 0.035 disagrees strongly with some peculiar-velocity studies.
- Open: velocity-based forward modelling claims to surpass the standard peculiar-velocity pipeline while stating that systematic biases remain (arXiv:2602.03699).

### 1.8 Which dynamics inside field-level inference?
<!-- key: which-dynamics-inside-field-level-inference -->

- LPT (arXiv:1203.3639), particle mesh (arXiv:1806.11117), COLA with posterior resimulation (arXiv:2304.09193), tiled sCOLA (arXiv:2003.04925), differentiable particle mesh with BullFrog steps (arXiv:2510.05206, arXiv:2409.19049), and neural field-level emulators (outside the source list) are all in use.
- The trade is accuracy per gradient evaluation against memory; the adjoint formulation of DISCO-DJ removes the dependence of memory on the number of steps (arXiv:2510.05206).
- Open: at what scale the choice of solver changes the inferred initial conditions rather than only the resimulated haloes.

### 1.9 Lyα simulations: which missing physics matters most?
<!-- key: lyalpha-simulations-which-missing-physics -->

- Candidates with quantified effects: AGN feedback (2% on σ_8, arXiv:2002.02822), patchy hydrogen and helium reionisation (arXiv:2207.13098, arXiv:2306.05471), the mean-flux degeneracy (arXiv:2412.05372), splicing (10%, arXiv:1406.6361), SPH density estimation (arXiv:2207.05023).
- Emulators trained on suites with different physics give different amplitudes from the same data; the sibling `cosmo-lyman-alpha` records σ_8 = 0.733 and 0.841 from one eBOSS data vector.
- Open: whether P3D emulation from 30 boxes (arXiv:2409.05682) is sufficient for a joint small- and large-scale analysis, and how to validate it on scales no hydrodynamical box contains.


### 1.10 Can a baryonified gravity-only run replace survey-volume hydrodynamics?
<!-- key: can-a-baryonified-gravity-only-run-replace -->

- For: the 2025 baryonification reproduces the P(k) suppression of FLAMINGO and TNG variants to 2% up to k = 5 h/Mpc, assigns gas pressure and temperature to particles, and compares well with a hydrodynamical run at map level by visual inspection (arXiv:2507.07892).
- Against: the same paper states that further work is needed to quantify the accuracy at the level of observables; the method reproduces whatever profiles it is calibrated on and does not predict them.
- The alternative is survey-volume hydrodynamics with on-the-fly light-cones: FLAMINGO at 2.8 Gpc and MillenniumTNG at 740 Mpc (arXiv:2306.04024, arXiv:2210.10060), at a cost that allows a dozen variants, not a parameter scan.

### 1.11 Are small-box training suites safe for machine-learning inference?
<!-- key: are-small-box-training-suites-safe-for-machine -->

- CAMELS spans cosmology and feedback with 25 Mpc/h boxes and two sub-grid families that give "significantly different" baryon fractions and baryonic effects on P(k); its authors read this as a need to marginalise over baryonic effects (arXiv:2010.00619).
- Quijote spans seven parameters at fixed, coarse resolution (arXiv:1909.05273).
- Open: whether a network trained on one sub-grid family is robust on another, and whether information measured on the matter field of such boxes survives in galaxies. The data-side evidence is in `cosmo-beyond-two-point`.

## 2. What the next data and simulations will decide
<!-- key: what-the-next-data-and-simulations-will-decide -->

- **Feedback strength.** DESI DR2 × ACT DR6 gas measurements are already in (arXiv:2609.22466); the resolution of the kSZ-versus-X-ray difference needs the next generation of simulations calibrated on eROSITA-era gas fractions, which the FLAMINGO and observational papers both call for (arXiv:2410.17109, arXiv:2509.10455).
- **Stage-IV lensing.** A simulated LSST Year 1 analysis shows that multi-wavelength gas calibration can recover the small-scale power of cosmic shear (arXiv:2512.02954, **forecast**).
- **Emulator coverage.** Dark Quest II is extending the design to massive neutrinos and clustering dark energy (arXiv:2605.28581); whether w0wa cosmologies near the DESI-preferred region are inside existing emulator boxes should be checked case by case.
- **DESI full-survey analyses** (expected 2027 according to `cosmo-galaxy-clustering`) will need larger mock sets than DR1; the DR2 reference mocks and 2LPT Lyα mocks are the first pieces (arXiv:2607.27412).
- **Euclid DR1** will be the first test of the Flagship-based validation chain on data (arXiv:2405.13495).
- **Constrained simulations at survey depth.** Manticore-Deep covers the SDSS and BOSS volumes (arXiv:2606.10020); DESI-density data would lower the constraint scale. No forecast was read.
- **Exascale gravity-only runs.** Frontier-E (two trillion particles) is served through OpenCosmo (arXiv:2607.16059); its science papers were not read.


## 2b. Accuracy requirements for Stage-IV surveys, as stated in the sources
<!-- key: accuracy-requirements-for-stage-iv-surveys-as -->

These are the published statements against which a simulation is judged; they are requirements, not achievements.

| Requirement | Statement | Reference |
|---|---|---|
| Matter power spectrum | 1% or better for 0.1 < k < 10 h/Mpc | arXiv:1104.1174 |
| Matter power spectrum | 1% over a range including very non-linear scales; needs L ≥ 0.5 Gpc/h, m_p ≤ 10⁹ M_⊙/h, more than a trillion particles for survey volumes | arXiv:1503.05920 |
| Baryonic effects | galaxy formation alters two-point observables beyond the statistical uncertainty of upcoming experiments at separations under 10 Mpc | arXiv:1905.06082 |
| Halo clustering for DESI | 2.1 × 10⁹ M_⊙/h particles sufficient for s > 20 Mpc/h in redshift space | arXiv:2112.09138 |
| Euclid galaxy mock | resolve 10¹¹ M_⊙/h haloes over a volume comparable to the survey: 3600 Mpc/h and m_p = 10⁹ M_⊙/h | arXiv:2405.13495 |
| Lyα flux statistics | 20 kpc/h cells and L > 40 Mpc/h for 1% | arXiv:1406.6361 |
| Covariance | no box replication for the DESI DR1 mocks: (6 Gpc/h)³ boxes | arXiv:2411.12027 |
| Emulator | 1% over eight parameters to k = 10 h/Mpc, z ≤ 3, reached by EuclidEmulator2 against gravity-only runs | arXiv:2010.11288 |

What is achieved against these: the gravity-only requirement is met by tuned codes and by one emulator; the baryonic part is not, by a wide margin (section 1.1); the Lyα requirement is met in boxes of about 100 Mpc/h and not in survey volumes; the Euclid mock meets its size requirement with a single realisation.

## 3. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

| Claim that circulates | What the sources say | Reference |
|---|---|---|
| "N-body codes agree to 1%." | To k = 1 h/Mpc at standard settings, 3% to k = 10; 1% to k = 10 only with tuned accuracy parameters. | arXiv:1503.05920, arXiv:2112.09138, arXiv:2605.28581 |
| "Baryons add small-scale power through cooling." | They remove power for 0.3 < k < 10s of h/Mpc; cooling dominates only above k about 70 h/Mpc. | arXiv:1104.1174 |
| "The group gas fraction fixes the baryonic suppression." | It predicts P_hydro/P_DMO to about 0.01 at k ≤ 1–2 h/Mpc; the shape differs between thermal and jet feedback at fixed gas fraction, BAHAMAS and FLAMINGO differ at nearly equal gas fractions, and a one-parameter model built on one suite does not reproduce another. | arXiv:1906.00968, arXiv:2306.04024, arXiv:2410.17109 |
| "Responses from 100 Mpc boxes (EAGLE, Illustris, SIMBA, Horizon-AGN) are as good as any." | The response converges to 1% only above (200 Mpc)³; smaller boxes probably overestimate it at k < 4 h/Mpc. | arXiv:2410.17109 |
| "Zel'dovich initial conditions are fine if the start is early enough." | Even from z = 199 they are accurate only to an eighth of the particle Nyquist wavenumber at z = 0, at the resolution tested. | arXiv:2008.09588 |
| "Friends-of-friends haloes enclose 180 times the mean density." | The boundary is at 81.62 times the mean for b = 0.2 and the enclosed overdensity depends on concentration. | arXiv:1103.0005 |
| "Hydrodynamical simulations predict the suppression." | They are calibrated; the suppression follows the group gas fraction they were tuned to, and suites differ by a factor of two. | arXiv:1906.00968, arXiv:2512.02954 |
| "FLAMINGO is ruled out by kSZ" / "FLAMINGO fits the kSZ". | The fiducial variant is more than 8σ from one kSZ and X-ray analysis and tracks another kSZ-to-lensing measurement; strong-feedback variants fit the first. | arXiv:2509.10455, arXiv:2609.22466 |
| "CAMELS gives the baryonic effect on P(k)." | Its first-generation boxes are 25 Mpc/h, the second generation's 50 Mpc/h (1,192 runs; arXiv:2606.10038); the response converges only above (200 Mpc)³. CAMELS is a training set. | arXiv:2010.00619, arXiv:2410.17109, arXiv:2606.10038 |
| "The emulator is accurate to 1%, so theory error is 1%." | 1% is interpolation error against gravity-only runs; add the code-to-code and baryonic terms. | arXiv:2010.11288; `cosmo-statistics-inference` |
| "Fixed-and-paired simulations give better covariances." | They suppress variance; they cannot estimate it. Three-point variance is not even reduced. | arXiv:1603.05253, arXiv:1811.02111 |
| "Start the simulation as early as possible." | Early starts amplify discreteness errors; start late with 3LPT. | arXiv:2008.09588 |
| "COLA or FastPM mocks are N-body simulations." | They are accurate for large-scale fields and halo abundance at stated settings, not for halo interiors. | arXiv:1509.04685, arXiv:2304.09193 |
| "DESI BAO errors come from 1000 mocks." | The BAO covariance is analytic, validated on mocks; the full-shape covariance is a corrected mock covariance. | arXiv:2411.12027 |
| "Mocks agree with the data, so the pipeline is validated." | Effective-bias mocks are fitted to the data or to HOD mocks fitted to the data. | arXiv:2007.08997, arXiv:2411.12027 |
| "Lyα BAO mocks are hydrodynamical." | They are Gaussian, lognormal or 2LPT skewers with an absorption recipe. | arXiv:1912.02763, arXiv:2607.27412 |
| "Splicing boxes is exact." | 10% on P1D in the Nyx test. | arXiv:1406.6361 |
| "SPH and grid codes agree for the forest." | To 1%, provided the SPH density is tessellated. | arXiv:2207.05023 |
| "The HOD is assumption-free because it is fitted." | The mass-only form misses 15% of the clustering in TNG300. | arXiv:1911.02610 |
| "A constrained simulation reproduces the local Universe." | Above the constraint scale and as an ensemble; below it, the structure is a prior draw. | arXiv:1510.04900, arXiv:2505.10682 |
| "Field-level reconstructions measure cosmology." | They assume it; they deliver fields. | arXiv:1806.11117; `cosmo-beyond-two-point` |
| "The local volume is known to be underdense from constrained simulations." | 5% in one project, no large underdensity in another. | arXiv:2202.04099, arXiv:2505.10682 |
| "Modified-gravity simulations are accurate to 1%." | The ratio to ΛCDM is, for three models, between codes. | arXiv:1506.06384 |
| "Quijote can be used for small-scale galaxy mocks." | At most 1024³ particles in 1 Gpc/h; it is designed for information content and machine-learning training. | arXiv:1909.05273 |
| "HalfDome resolves emission-line-galaxy hosts." | Minimum halo mass about 6 × 10¹² M_⊙/h; valid to k about 1 h/Mpc. | arXiv:2407.17462 |

## Not verified
<!-- key: not-verified -->

- The DES 6×2pt preference for weak feedback is quoted from the sibling skills, not from the paper.
- Whether SIBELIUS-DARK and Manticore-Local start from related inferences: not read.
- Amon & Efstathiou's proposal that a stronger non-linear suppression reconciles lensing with Planck was read in abstract and lies outside the source list.
- Forecasts for simulation needs of Stage-V surveys: not researched.
- GPU and differentiable code releases of 2026, neural field-level emulators, generative light-cone models: titles seen, not read.
- Ray-tracing and intrinsic-alignment modelling in simulations: not researched. Halo finders are now in `physics-and-methods.md` §11, from abstracts.
- The size of the 1LPT transient in the Flagship 2 run itself: section 2.2 of arXiv:2405.13495 was read and contains no such test.
- Whether the DESI w0wa-preferred region lies inside the parameter boxes of EuclidEmulator2, Mira-Titan IV and BACCO was not checked against their tables.
