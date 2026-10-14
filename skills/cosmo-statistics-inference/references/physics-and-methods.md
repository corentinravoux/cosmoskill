# Statistics and inference — methods, defining formulae, reference papers

Scope: the statistical methods used in cosmological parameter inference, each with its defining formula, its reference paper and a cosmology example.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` taken from a named secondary source; `[der]` derived here, derivation stated.

## 1. Likelihoods and when the Gaussian approximation fails
<!-- key: likelihoods-and-when-the-gaussian-approximation -->

The default in large-scale-structure analyses is a multivariate Gaussian in the compressed statistic `d` (power spectrum, correlation function, multipoles): `−2 ln L = (d − m(θ))^T C^-1 (d − m(θ))` up to a constant, with `C` fixed in parameter space. It is an approximation in three distinct ways.

| Departure from the Gaussian form | What is known | Reference |
|---|---|---|
| The exact distribution of a power-spectrum estimate of a Gaussian field is Wishart (a scaled χ² per multipole), skewed at low multipole | For CMB T and polarisation on a cut sky, the Hamimeche–Lewis approximation "models the non-Gaussian form exactly in the ideal full-sky limit" and is validated at ℓ ≳ 30, where an exact calculation becomes impossible; pixel-based likelihoods are used below | Hamimeche & Lewis 2008, arXiv:0801.0554 [src] |
| A Gaussian likelihood with a parameter-dependent covariance assigns artificial information | Used consistently, it violates the Cramér–Rao bound; "Gaussian likelihoods should always be used with a covariance matrix fixed in parameter space" | Carron 2013, arXiv:1204.4724 [src] |
| The covariance does depend on cosmology | Cosmic-shear covariances vary significantly over Ω_m in [0.2, 0.4], σ8 in [0.6, 1.0], with a non-negligible effect on contour size; remedy by iterating the covariance at the best fit | Eifler, Schneider & Hartlap 2009, arXiv:0810.4254 [src] |
| Size of the effect of ignoring the parameter dependence | For 3×2pt, bias of at most O(10%) of the statistical error even for surveys covering less than 1% of the sky, smaller for larger areas | Kodwani, Alonso & Ferreira 2019, arXiv:1811.11584 [src] |
| Correlation functions on large angular scales are skewed | Non-Gaussian correlations are significant in the CFHTLenS ξ±; the one-point distributions are skewed so that "sound weak lensing data sets are intrinsically likely to lead to a systematically low lensing amplitude being inferred"; the effect grows with angular scale | Sellentin & Heavens 2018, arXiv:1707.04488 [src] |
| Same question for LSST-like areas | No significant bias in the 1D posteriors of Ω_m and σ8 for 100 deg² mocks; the difference shrinks further with area | Lin et al. 2020, arXiv:1905.03779 [src] |
| Pseudo-C_ℓ 3×2pt for a Euclid-like survey | The Gaussian likelihood returns accurate constraints against the exact Wishart on the full sky; the cut-sky likelihood is more non-Gaussian but not enough to matter | Upham, Brown & Whittaker 2021, arXiv:2012.06267 [src] |
| Galaxy power-spectrum multipoles and counts-like statistics | Non-Gaussianity detected in the BOSS `P_ℓ` likelihood, shifting fσ8 by −0.44σ; for the group multiplicity function the Gaussian form underestimates errors, broadening two HOD parameters by 42% and 66% | Hahn et al. 2019, arXiv:1803.06348 [src] |
| The covariance is itself estimated | The likelihood becomes a multivariate t-distribution (§2.1) | Sellentin & Heavens 2016, arXiv:1511.05969 |

Rules of judgment that follow. (i) The Gaussian form is safe when each element of the data vector averages many modes and the covariance is fixed; it fails first for low multipoles, large angular scales, small areas, sparse counts and one-point statistics. (ii) A parameter-dependent covariance is not "more correct" inside a Gaussian likelihood; either keep it fixed (and iterate), or use the exact distribution. (iii) When the likelihood is not known in closed form, the alternative is to learn it from simulations (§12).

## 2. Covariance estimation
<!-- key: covariance-estimation -->

Notation used below, following Percival et al. 2022 (arXiv:2108.10402): `n_s` simulations (mocks), `n_d` data points, `n_θ` fitted parameters, `S` the sample covariance of the mocks, `Σ` the true covariance. `S` is Wishart-distributed with `n_s − 1` degrees of freedom.

### 2.1 Sample covariance from mocks and its corrections
<!-- key: sample-covariance-from-mocks-and-its-corrections -->

| Step | Formula | Reference |
|---|---|---|
| The inverse of `S` is a biased estimate of `Σ^-1`; the bias depends on the ratio of the number of bins to the number of data sets, and `S` is singular when the number of bins exceeds the number of data sets | unbiased precision `Ψ = S^-1 / h`, with `h = (n_s − 1)/(n_s − n_d − 2)` [src: arXiv:2108.10402, where `hS` is called the Hartlap-corrected covariance] | Hartlap, Simon & Schneider 2007, arXiv:astro-ph/0608064 |
| The noise in `Ψ` scatters the best fit: the true parameter covariance is larger than the Fisher one | `V = [1 + B (n_d − n_θ)] F^-1`, `B = (n_s − n_d − 2) / [(n_s − n_d − 1)(n_s − n_d − 4)]` [src: arXiv:1312.4841 eq. for `V`; `B` as written in arXiv:2108.10402] | Dodelson & Schneider 2013, arXiv:1304.2593 (abstract: "a factor of order `1 + N_b/N_s`") |
| The width read from the likelihood is also biased, by a different amount, so the measured parameter covariance must be rescaled | `m_1 = [1 + B (n_d − n_θ)] / [1 + A + B (n_θ + 1)]`, applied to the parameter covariance, its square root to the standard deviation [src]. `A` is defined with `B` in the paper's eq. (AB), not transcribed here. | Percival et al. 2014, arXiv:1312.4841 |
| Marginalising over the unknown `Σ` with an independence-Jeffreys prior turns the Gaussian likelihood into a multivariate t-distribution | posterior `∝ abs(Q)^(-n_s/2)`, `Q = (n_s − 1) S + (x − μ)(x − μ)^T`, equivalently `[1 + χ²/(n_s − 1)]^(-n_s/2)` with `χ² = (x − μ)^T S^-1 (x − μ)` [src: arXiv:2108.10402 §2.1; the second form is `[der]` by the matrix determinant lemma] | Sellentin & Heavens 2016, arXiv:1511.05969 |
| A power-law prior `abs(Σ)^(-(m − n_s + n_d + 1)/2)` chosen so that credible intervals have frequentist coverage | posterior `∝ [1 + χ²/(n_s − 1)]^(-m/2)`, `m = n_θ + 2 + [n_s − 1 + B (n_d − n_θ)] / [1 + B (n_d − n_θ)]`; no Hartlap factor is applied to `S` [src] | Percival, Friedrich, Sellentin & Heavens 2022, arXiv:2108.10402 |
| Gaussian approximation of the previous line | use the inverse of `S' = (n_s − 1)[1 + B (n_d − n_θ)] / (n_s − n_d + n_θ − 1) × S` in `χ²` [src] | arXiv:2108.10402 |

Points of interpretation, all from arXiv:2108.10402 [src]:

- The Hartlap factor makes the precision unbiased over repeated draws of `S`; it does not make the parameter credible interval correct. The Sellentin–Heavens posterior has covariance `hS` around the data, the same as the Hartlap-corrected Gaussian, but heavier tails; a Hartlap-corrected Gaussian has "tail probabilities that are lower than the t-distribution, and may be in considerable error when datasets in tension are discussed and compared".
- The Sellentin–Heavens likelihood does not contain the Dodelson–Schneider term. Percival et al. 2022 note that the proposal of Friedrich & Eifler (cited there as Friedrich18, not fetched here) is to multiply the Sellentin–Heavens covariance by `1 + B (n_d − n_θ)`, and that this is close to their `S'` when `n_θ` is small.
- The mean over draws of `S` of the inverse Gaussian Fisher matrix is `(n_s − n_d + n_θ − 1)/(n_s − 1) × F_Σ^-1`: before any correction, the naive error is too small by that factor.

Requirements on the number of mocks (Taylor, Joachimi & Kitching 2013, arXiv:1212.4359) [src]: the fractional error on a parameter variance equals the fractional variance of the precision matrix; for a 5% error on a parameter error and `N_D << 100` data points, at least 200 realisations are needed; for `N_D >> 100`, `N_S > N_D` is required, with a fractional accuracy better than `sqrt(2/N_D)` on the covariance.

### 2.2 Internal estimates: jackknife and bootstrap
<!-- key: internal-estimates-jackknife-and-bootstrap -->

- Norberg et al. 2009 (arXiv:0810.1885) compared jackknife and bootstrap with external Monte-Carlo errors on N-body simulations: the standard bootstrap overestimates the variance of ξ(s) by about 40% on all scales probed; the jackknife returns the correct variance on large scales and overestimates it on small scales; a 2σ interval from an internal estimator "could correspond in practice to anything from 1-sigma to 3-sigma" [src].
- Friedrich et al. 2016 (arXiv:1508.00895), for cosmic shear with log-normal simulations: the volume inside constant-likelihood contours in Ω_m–σ8 from internally estimated covariances is on average ≳ 85% of the true one, and the uncertainty on Σ8 ~ σ8 Ω_m^0.5 is about 90% of the true uncertainty (a forecast for the 5-year DES survey) [src].
- Mohammad & Percival 2022 (arXiv:2109.07071) derive correction terms for delete-one jackknife and bootstrap of the two-point correlation function; tested on 1000 Quijote boxes of 1 (Gpc/h)³, the corrected estimators recover the amplitude and principal components to about 10%, the precision of the test [src].

### 2.3 Analytic and semi-analytic covariances
<!-- key: analytic-and-semi-analytic-covariances -->

- Gaussian (disconnected) term plus connected non-Gaussian (trispectrum) term plus super-sample covariance. The super-sample term is the response of the power spectrum to a background density mode larger than the survey; it "dominates the covariance of power spectrum estimators for modes much smaller than the survey" for a wide range of volumes (Takada & Hu 2013, arXiv:1302.6994) [src].
- RascalC (Philcox et al. 2019, arXiv:1904.11070): configuration-space two-point covariance for arbitrary geometry, with non-Gaussianity approximated by a rescaling of the shot noise calibrated on the jackknife of the data; finely binned matrices in fewer than 100 CPU-hours [src]. It is the fiducial covariance of the DESI 2024 BAO analysis (Forero-Sánchez et al. 2024, arXiv:2411.12027) [src].
- DES Y3 3×2pt uses an analytic halo-model covariance validated in Friedrich et al. 2021 (arXiv:2012.08568); KiDS-1000 validated its analytic covariance against more than 20000 mocks (Joachimi et al. 2021, arXiv:2007.01844) [src].
- 2026 work: analytic Gaussian covariance of the cosmic-shear correlation function (Nagura et al. 2026, arXiv:2605.16186); the linear-construction covariance for Euclid cluster clustering, up to 20 times faster than the sample covariance (Lindholm et al. 2026, arXiv:2603.10735) [src, abstracts].

### 2.4 Shrinkage and denoising
<!-- key: shrinkage-and-denoising -->

- Linear shrinkage combines the empirical covariance with a model target to minimise the mean squared error (Pope & Szapudi 2008, arXiv:0711.2509) [src].
- Non-linear shrinkage (NERCOME) and the Rotational Invariant Estimator were benchmarked for clustering in Farina et al. 2026 (arXiv:2604.13851): both reduce the stochastic shifts of the best fit due to the Dodelson–Schneider effect, but the uncertainties they return are probe-dependent; in configuration space both can give constraints that are too tight, with a bias growing with the data-vector size [src].

## 3. Data compression
<!-- key: data-compression -->

Compression reduces the data vector before the likelihood is evaluated. It matters for two reasons: the mock-count corrections of §2 scale with the length of the data vector, and density estimators in simulation-based inference work in low dimension.

| Method | Compressed statistic | Lossless when | Reference |
|---|---|---|---|
| Karhunen–Loève (signal-to-noise eigenmodes) | projections on the generalised eigenvectors of signal and noise covariances | Gaussian data, one parameter; an extra singular-value step handles several parameters and unknown fiducial values | Tegmark, Taylor & Heavens 1997, arXiv:astro-ph/9603021 [src] |
| MOPED | `M` linear combinations of the data for `M` parameters (weight vectors given in the paper) | the noise covariance does not depend on the parameters; then "the Fisher information matrices are identical"; with parameter-dependent noise the errors increase "by a very modest factor" | Heavens, Jimenez & Lahav 2000, arXiv:astro-ph/9911102 [src] |
| Score compression | the gradient of the log-likelihood with respect to the parameters at a fiducial point, `t = ∇_θ ln L`, giving `n` summaries for `n` parameters | preserves the Fisher information; generalises linear compression and quadratic estimators, and the non-Gaussian case under regularity conditions | Alsing & Wandelt 2018, arXiv:1712.00012 [src] |
| Principal components of the data vector | leading eigenmodes of the data covariance | never exactly; a factor ~5 reduction kept most of the information for shear correlation functions | Lin et al. 2020, arXiv:1905.03779 [src] |
| Physical compression | BAO scaling parameters, `fσ8`, ShapeFit parameters, CMB shift parameters (θ*, ω_b, ω_bc) | only within the model class used to define them | DESI uses the compressed CMB prior (θ*, ω_b, ω_bc) as its minimal early-Universe information (arXiv:2503.14738) [src] |
| Neural compression | a network trained to output parameter estimates or informative summaries | not guaranteed; must be validated | see §12 |

Costs and cautions. (i) Compression is optimal at the fiducial point only; far from it information is lost, never invented, so the result is conservative but can be biased if the fiducial model is poor: iterate. (ii) The compression needs a covariance and derivatives; if the covariance is noisy, the compressed statistic is noisy but the number of mocks needed scales with the compressed dimension (Percival et al. 2022, arXiv:2108.10402, have an appendix on compressing the data in this context). (iii) Compressed data hide model misfit: a goodness-of-fit test on `n` numbers for `n` parameters has no degrees of freedom left; keep a test on the uncompressed vector. (iv) A physical compression carries its model: a compressed CMB prior excludes lensing and late-time information by construction, which is why DESI + compressed CMB gives 2.4σ where DESI + full CMB gives 3.1σ for w0wa (arXiv:2503.14738) [src]. (v) Finite compression can degrade an explicit-likelihood analysis while leaving a learned likelihood nearly unaffected (arXiv:2607.17942) [src].

## 4. Blinding strategies
<!-- key: blinding-strategies -->

The purpose of blinding is "to hide an experiment's critical results ... until all decisions affecting its analysis have been finalised" (Muir et al. 2020, arXiv:1911.05929) [src]. The schemes differ by the level at which the data are altered.

| Level | How it works | Strength | Weakness | Reference and user |
|---|---|---|---|---|
| Catalogue, clustering | shift galaxy redshifts along the line of sight by (1) a geometric shift mimicking the Alcock–Paczynski effect and (2) a perturbative shift akin to redshift-space distortions | one scheme for every summary statistic; angular positions and angular systematics untouched; "almost impossible to accidentally unblind" | must be validated for each observable; does not blind statistics insensitive to the shifted quantities | Brieden et al. 2020, arXiv:2006.10857 [src]; DESI DR1 and DR2 |
| Catalogue, f_NL | weights that imitate a scale-dependent bias | blinds primordial non-Gaussianity together with BAO and RSD | — | Andrade et al. 2024, arXiv:2404.07282 [src] |
| Catalogue, Lyα forest | geometric shift of each forest in wavelength after the continuum fit, with consistent shifts of quasar redshifts | moves the BAO peak as for a ~5% change in matter content without changing posterior shapes | metals and Lyβ are mixed with Lyα, visible mainly in the 1D correlation | Perez-Sanchez et al. 2026, arXiv:2607.07875 [src] |
| Summary statistic (data vector) | add to the measured two-point functions the difference between model vectors at a hidden and a reference cosmology | preserves internal consistency and `χ²`, so that cross-probe checks remain possible | relies on the model used to compute the shift | Muir et al. 2020, arXiv:1911.05929 [src]; DES Y3 and Y6; LSST DESC through the Smokescreen package, which encrypts the true vector (Loureiro et al. 2026, arXiv:2604.18111) [src] |
| Covariance | hide a bias in the covariance matrix that moves the posterior peak in a chosen direction; deblinding is a reweighting of the posterior | the blinder controls where the blinded posterior peaks | assumes Gaussian data | Sellentin 2020, arXiv:1910.08533 [src] |
| Catalogue, shear | several copies of the shape catalogue with altered ellipticities or calibration, only one true | simple | not verified here for the current KiDS and HSC releases | see `cosmo-weak-lensing` |
| Parameter level | offsets added to plotted axes and printed numbers | cheap | easy to undo; does not protect the data vector | generic |

DESI validated its scheme "on mocks, as well as on data by applying a second blinding layer", and found that "the BAO and RSD analysis choices do not need any modification before and after unblinding" (arXiv:2404.07282) [src].

What a blinding scheme must satisfy, as stated across these papers: the shift is large compared with the statistical error; null and consistency tests keep their power on blinded data; the analysis pipeline behaves the same on blinded and unblinded data; accidental unblinding is hard; and the list of tests to pass before unblinding is written in advance.

## 5. Samplers and convergence
<!-- key: samplers-and-convergence -->

### 5.1 The families
<!-- key: the-families -->

| Family | Principle | Gives the evidence | Needs gradients | Reference and cosmology use |
|---|---|---|---|---|
| Metropolis–Hastings MCMC | random-walk proposals from a learned covariance, with fast and slow parameter blocks | no | no | Cobaya (Torrado & Lewis 2021, arXiv:2005.05290): parameters "grouped in blocks according to their dependencies and optimally sorted" by cost, caching of intermediate results, sub-millisecond overhead [src]. DESI DR2 cosmology chains (arXiv:2503.14738). |
| Nested sampling | live points climbing iso-likelihood shells; the evidence is the primary output, the posterior a by-product | yes | no | PolyChord (Handley, Hobson & Lasenby 2015, arXiv:1506.00171): slice sampling inside the hard likelihood constraint, exploits a hierarchy of parameter speeds [src]. DES Y3 choice (Lemos et al. 2023, arXiv:2202.08233). MultiNest is the ellipsoidal variant discussed in the same paper. |
| Importance nested sampling with a learned proposal | neural-network regression builds the proposal; all likelihood calls are used | yes | no | nautilus (Lange 2023, arXiv:2306.16923): efficiency "substantially higher than that of all other samplers, often by more than an order of magnitude" on its benchmarks [src]. |
| Hamiltonian Monte Carlo, NUTS | trajectories following the gradient of the log posterior; NUTS chooses the path length automatically and adapts the step size by dual averaging | no | yes | Hoffman & Gelman 2014 (arXiv:1111.4246) [src]. Requires a differentiable likelihood, hence emulators or auto-differentiable codes (§11). Used for field-level inference, where the dimension is 10^5 to 10^7 (see `cosmo-beyond-two-point`). |
| GPU nested sampling with neural emulators | vectorised likelihood on a GPU | yes | no | Lovick et al. 2025 (arXiv:2509.13307): Bayes factors for a 39-dimensional ΛCDM against w0wa shear analysis "in just 2 days on a single A100 GPU" [src]. |

### 5.2 Convergence criteria actually used
<!-- key: convergence-criteria-actually-used -->

- DESI DR2 (arXiv:2503.14738, §5) [src]: Metropolis–Hastings in Cobaya with CAMB; convergence when the Gelman–Rubin statistic satisfies `R − 1 < 0.01`, "or that the chains have an effective sample size of ≳ 10^3, whichever is longer"; summaries with `getdist`; mean and standard deviation for symmetric posteriors, the 68% minimal credible interval otherwise; limits at 68% except Σm_ν at 95%; best fit with `iminuit` started from the MAP of each chain.
- The classical `R̂` has known flaws: it "will fail to correctly diagnose convergence failures when the chain has a heavy tail or when the variance varies across the chains"; the rank-normalised, folded `R̂` with quantile-based efficiency measures and rank plots is the recommended replacement (Vehtari et al. 2021, arXiv:1903.08008) [src].
- For nested sampling the controls are the number of live points, the stopping tolerance and, in PolyChord, the number of slice-sampling repeats; arXiv:2202.08233 recommends separate settings for test runs and final chains.

### 5.3 What the comparisons found
<!-- key: what-the-comparisons-found -->

Lemos et al. 2023 (arXiv:2202.08233), with the full DES Y1 likelihood and a fast approximate one [src]: MultiNest "reports inconsistent estimates of the Bayesian evidence and somewhat narrower parameter credible intervals" than PolyChord; PolyChord agrees with Metropolis–Hastings; PolyChord "provides a good balance of speed and robustness". The DES Y3 + KiDS-1000 joint analysis lists samplers among the analysis choices it had to reconcile (arXiv:2305.17173).

Finding the best fit is a separate problem from sampling. The MAP of a chain is a noisy estimate in 20 or more dimensions; DESI polishes it with `iminuit` (arXiv:2503.14738), the profile-likelihood codes use simulated annealing (arXiv:2401.14225).

## 6. Priors and projection effects
<!-- key: priors-and-projection-effects -->

### 6.1 What a projection effect is
<!-- key: what-a-projection-effect-is -->

For parameters of interest `θ` and nuisance parameters `ν`, the marginal posterior is `P(θ) ∝ ∫ L(θ, ν) π(θ, ν) dν`, while the profile likelihood is `L_p(θ) = max_ν L(θ, ν)`. In the Laplace approximation around the conditional maximum `ν̂(θ)`,

`P(θ) ∝ L(θ, ν̂(θ)) π(θ, ν̂(θ)) × det[H_νν(θ)]^(-1/2)`,

where `H_νν` is the Hessian of `−ln(L π)` in the nuisance directions `[der: standard Laplace approximation; this is the framework used by Hadzhiyska et al. 2023, arXiv:2301.11895, to relate analytic marginalisation, volume effects and the profile likelihood]`. The last factor is the "prior volume" or "projection" term: where the data constrain `ν` weakly for some values of `θ`, those values gain posterior weight although they do not fit better. The marginal mean and the maximum a posteriori (MAP) point then separate, and neither is wrong: they answer different questions.

Synonyms in the literature: projection effect, prior-volume effect, marginalisation bias, volume effect.

### 6.2 Where it appears
<!-- key: where-it-appears -->

| Setting | Mechanism | Reference |
|---|---|---|
| EFTofLSS full-shape fits | Many weakly constrained bias and counterterm parameters, degenerate with amplitude; results depend on the "West-coast" (PyBird) or "East-coast" (CLASS-PT) prior | Simon et al. 2023, arXiv:2208.05929; Carrilho, Moretti & Pourtsidou 2023, arXiv:2207.14784 |
| Same, in extended models (w0waCDM) | The extra background parameters open degeneracies that the nuisance volume fills | Morawetz et al. 2025, arXiv:2508.11811 |
| Priors on nuisance parameters set in Mpc/h units | They introduce "a spurious correlation with the Hubble parameter h" | Pezzotta et al. 2026, arXiv:2610.08751 |
| Models with a parameter that switches a sector off (early dark energy fraction, an interaction cross-section, an interacting fraction) | When the amplitude goes to zero the other parameters of the sector are unconstrained, so the posterior favours that region | Herold, Ferreira & Komatsu 2022, arXiv:2112.12140; Straight et al. 2026, arXiv:2603.25731 |
| Cosmic shear, S8 | Skewed marginal and projection in a high-dimensional space; the marginal mean lies below the MAP | Joachimi et al. 2021, arXiv:2007.01844; DES & KiDS 2023, arXiv:2305.17173 |

### 6.3 Diagnostics and mitigations in use
<!-- key: diagnostics-and-mitigations-in-use -->

- Report the MAP (or best fit) next to the marginal mean and interval. KiDS-1000 proposed an alternative point estimate and credible interval because the standard S8 estimate from the marginal "is easily misinterpreted to be biased low" (arXiv:2007.01844) [src].
- Fit a noiseless synthetic data vector at a known cosmology with the full pipeline and priors; the offset of the marginal from the input is the projection effect of that setup.
- Profile distributions estimated directly from existing chains, as a fast test (Gómez-Valent 2022, arXiv:2203.16285).
- Widen the nuisance priors: in BOSS, doubling the widths improved the agreement between best fits of the two prior choices from ~1σ to ~0.5σ (arXiv:2208.05929) [src].
- Informative, physically motivated priors on EFT parameters from HOD mocks (Zhang et al. 2024, arXiv:2409.12937; Ivanov et al. 2024, arXiv:2402.13310).
- Reparameterisation: absorb the amplitude parameters into the nuisance parameters (Tsedrik, Carrilho & Moretti 2025, arXiv:2509.09562); non-linear orthogonalisation or a Jeffreys prior over the EFT coefficients (Bonici et al. 2026, arXiv:2607.02498); nuisance parameters defined in Mpc units, and σ12 in place of σ8 (arXiv:2610.08751).
- Analytic (Laplace) marginalisation of nuisance parameters, which reproduces the volume effect at lower cost (arXiv:2301.11895).
- A frequentist profile likelihood as a prior-independent cross-check (§7).

The Jeffreys prior is `π(θ) ∝ sqrt(det F(θ))` with `F` the Fisher matrix; it is invariant under reparameterisation, which is why it removes the volume factor that a flat prior in an arbitrary parameterisation introduces (textbook definition; its use for EFT coefficients is in arXiv:2607.02498).

## 7. Profile likelihoods and frequentist intervals
<!-- key: profile-likelihoods-and-frequentist-intervals -->

### 7.1 Construction
<!-- key: construction -->

The profile likelihood of a parameter `θ` is `L_p(θ) = max_ν L(θ, ν)`, with all other parameters re-optimised at each fixed `θ`. The "graphical" interval is read from `Δχ²(θ) = −2 ln[L_p(θ)/L_max]`: `Δχ² = 1` for 68.3% and `3.84` for 95% in one dimension. This reading rests on Wilks' theorem, that is on the asymptotic limit of a large data set, a Gaussian estimator and a true value away from any boundary (Herold, Ferreira & Heinrich 2024, arXiv:2408.07700). It contains no prior and is invariant under reparameterisation.

Feldman & Cousins 1998 (arXiv:physics/9711021) give a confidence-belt construction that unifies upper limits and two-sided intervals, avoids unphysical intervals for a Gaussian measurement with a bounded physical region, and removes the loss of coverage that occurs when the choice between a limit and an interval is made after seeing the data [src]. In cosmology it is the standard tool for the neutrino mass, where the best fit sits at or beyond `Σm_ν = 0`.

### 7.2 When the graphical construction can be trusted
<!-- key: when-the-graphical-construction-can-be-trusted -->

Herold et al. 2024 (arXiv:2408.07700) tested the assumptions with Planck 2018 `Plik_lite` data [src]:

| Model | Finding | Recommended construction |
|---|---|---|
| ΛCDM | the profile likelihood gives correct coverage | graphical `Δχ²` |
| ΛCDM + Σm_ν | consistent with a Gaussian near a boundary | boundary-corrected or Feldman–Cousins |
| w0CDM | "indication of a violation of the assumptions" | full Neyman construction with simulations |

Barua et al. 2025 (arXiv:2508.10633) compare Wilks-based intervals, likelihood integration and Feldman–Cousins on non-Gaussian problems: agreement within 10% near the Gaussian regime, larger discrepancies outside it, and intervals that are too narrow when parameters are held fixed in the mock fits of the Feldman–Cousins construction [src].

### 7.3 Use in cosmology
<!-- key: use-in-cosmology -->

- Planck intermediate results XVI (arXiv:1311.1657): profile likelihoods of the 2013 likelihood with Minuit; "excellent" agreement with the Bayesian results in ΛCDM; for the neutrino mass the profile of the CMB-only combination has its minimum "well within the unphysical negative-mass region", regularised by adding CMB lensing [src].
- Early dark energy: the profile likelihood removed the volume effect of the MCMC analysis (arXiv:2112.12140; Herold & Ferreira 2023, arXiv:2210.16296).
- Tensor-to-scalar ratio: Campeti & Komatsu 2022 (arXiv:2205.05617).
- EFT full shape of BOSS, eBOSS and DESI DR1: Holm et al. 2023 (arXiv:2309.04468); Morawetz et al. 2025 (arXiv:2508.11811).
- Neutrino mass with DESI: Naredo-Tuero et al. 2024 (arXiv:2407.13831); DESI DR2 quotes a Feldman–Cousins limit next to the Bayesian one (Elbers et al. 2025, arXiv:2503.14744). The physics is in `cosmo-neutrinos-dark-matter`.

Caveat stated by the practitioners themselves: the profile likelihood of BOSS "prefers extreme values of the EFT parameters" (arXiv:2309.04468) [src]. A best fit can sit where the nuisance parameters are unphysical; the prior that causes the projection effect is also what excludes that region.

### 7.4 Codes
<!-- key: codes -->

PROSPECT (Holm et al. 2023, arXiv:2312.02972; works with cobaya and MontePython), Procoli (Karwal et al. 2024, arXiv:2401.14225; simulated annealing, MontePython and CLASS), pinc (released with arXiv:2408.07700). The numerical difficulty is the optimiser: Boltzmann-code noise makes gradient minimisers unreliable, which is why simulated annealing and many restarts are used.

## 8. Model comparison
<!-- key: model-comparison -->

### 8.1 The statistics in use
<!-- key: the-statistics-in-use -->

| Statistic | Definition (textbook) | Depends on the prior | In-sample | Typical use |
|---|---|---|---|---|
| `Δχ²_MAP` | twice the difference of the negative log posterior (or likelihood) at the two best fits | no (apart from non-uniform priors at the MAP) | yes | DESI w0wa significance |
| Significance from `Δχ²` | p-value of a χ² with `k` degrees of freedom, `k` the number of extra parameters (Wilks' theorem for nested models), converted to a two-sided Gaussian `nσ` | no | yes | "3.1σ" |
| Akaike criterion | `AIC = −2 ln L_max + 2k` | no | yes, penalised | quick ranking |
| Bayesian information criterion | `BIC = −2 ln L_max + k ln N` | no (asymptotic) | yes, penalised | quick ranking |
| Deviance information criterion | `DIC = D(θ̄) + 2 p_D`, `D = −2 ln L`, `p_D = <D> − D(θ̄)` | weakly, through the posterior | yes, penalised | DESI, KiDS |
| Bayesian evidence | `Z = ∫ L(θ) π(θ) dθ` | yes, linearly in the prior volume of the extra parameters | yes | nested sampling analyses |
| Bayes factor | `B = Z_1 / Z_0`; for nested models with separable priors the Savage–Dickey ratio `B_01 = P(θ_extra = θ_0 given d, M_1) / π(θ_extra = θ_0)` | yes | yes | "ln B" |
| Expected log predictive density | score of held-out data under the posterior, by cross-validation | weakly | no (out-of-sample) | Karim, Speagle & Hložek 2026, arXiv:2609.04334 |

The reference review for the Bayesian side is Trotta 2008 (arXiv:0803.4089), which covers the evidence, the effective model complexity and their computation.

### 8.2 The conversion DESI uses
<!-- key: the-conversion-desi-uses -->

DESI DR2 (DESI Collaboration 2025, arXiv:2503.14738) finds the best fit with `iminuit` started from the MAP of each chain, defines `Δχ²_MAP` as "twice the difference in the negative log posteriors at the maximum posterior points for each model", and converts it to "the corresponding (frequentist) significance levels given 2 extra free parameters" [src]. The conversion is `p = exp(−Δχ²/2)` for two degrees of freedom, then the two-sided Gaussian equivalent `[der]`; it reproduces the published column (`Δχ² = −12.5` gives 3.10σ, `−21.0` gives 4.19σ; full table in `results.md` §4).

Thresholds `[der, from the χ² survival function]`:

| nσ (two-sided) | p | Δχ², 1 dof | 2 dof | 3 dof | 4 dof |
|---|---|---|---|---|---|
| 1 | 0.317 | 1.00 | 2.30 | 3.53 | 4.72 |
| 2 | 0.0455 | 4.00 | 6.18 | 8.02 | 9.72 |
| 3 | 2.70e-3 | 9.00 | 11.83 | 14.16 | 16.25 |
| 4 | 6.33e-5 | 16.00 | 19.33 | 22.06 | 24.50 |
| 5 | 5.73e-7 | 25.00 | 28.74 | 31.81 | 34.56 |

Conditions for the conversion to hold: nested models, the simpler model in the interior of the larger one's parameter space, Gaussian asymptotics, no parameter that becomes unidentified under the null. `sqrt(Δχ²)` is the significance only for one extra parameter; applying it to w0wa would turn 3.1σ into 3.5σ `[der]`.

### 8.3 Why evidence and Δχ² can disagree
<!-- key: why-evidence-and-chi2-can-disagree -->

For a nested model with extra parameters whose prior width is much larger than the posterior width, the Bayes factor carries an Ockham factor of order (posterior width)/(prior width) per extra parameter. A `Δχ²` significance has no such factor. With the same data the two can therefore differ in sign: this is the Lindley paradox, and it is the situation of w0wa in 2025–2026 (`results.md` §4). Efstathiou 2008 (arXiv:0802.3185) made the argument with dark energy as the example: the evidence rests on "subjective judgements concerning the choice of model and priors", and for nested problems "Bayesian parameter estimation can be more informative than computing Bayesian Evidence for poorly motivated physical models" [src].

The Jeffreys scale as used by DES for `log R`: above 2.3 strong, 1.2 to 2.3 substantial, −1.2 to 1.2 inconclusive, and symmetrically for tension (Lemos et al. 2021, arXiv:2012.09554, table 1) [src]. The same paper notes that "the boundaries in Jeffreys' scale are arbitrary, and they lack obvious interpretation as a statistical significance". DESI's rule of thumb for the information criterion: `Δ(DIC) < −5` "strong", `< −10` "decisive" (arXiv:2503.14738) [src].

## 9. Tension metrics
<!-- key: tension-metrics -->

Tension metrics answer one of two questions (Lemos et al. 2021, arXiv:2012.09554) [src]. Evidence-based methods ask whether the model can generate the data of both experiments with one set of parameters. Parameter-space methods ask how significant the difference between the two posteriors is, in the parameters both experiments constrain. All formulae below were read in §4 of that paper.

| Metric | Definition | Property | Reference |
|---|---|---|---|
| 1D difference | `(x_A − x_B) / sqrt(σ_A² + σ_B²)` | valid for one Gaussian parameter and independent data; ignores the other dimensions | textbook |
| Bayes ratio | `R = Z_AB / (Z_A Z_B) = ∫ P_A P_B / Π dθ` | proportional to the prior volume for a flat prior: "doubling the prior volume doubles the value of R"; read on the Jeffreys scale | used in DES Y1; critique in Handley & Lemos 2019, arXiv:1902.04029 |
| Information ratio | `log I = D_A + D_B − D_AB`, with `D = ∫ P log(P/Π) dθ` the Kullback–Leibler divergence | carries the prior dependence | arXiv:1902.04029 |
| Suspiciousness | `log S = log R − log I` | prior-volume independent; for Gaussian posteriors it is `χ²_d`-distributed (the exact combination is given in arXiv:1902.04029), which gives a tension probability `p_T` | arXiv:1902.04029 |
| Bayesian model dimensionality | `d = 2 ∫ P (log(P/Π) − D)² dθ` | the number of parameters the data constrain; equals 1 for a 1D Gaussian | arXiv:1902.04029 |
| Parameter difference | `P(Δθ) = ∫ P_A(θ) P_B(θ − Δθ) dθ`, `Δ = ∫_{P(Δθ) > P(0)} P(Δθ) dΔθ` | invariant under reparameterisation; needs density estimation in many dimensions (KDE, or normalising flows) | Raveri & Hu 2019, arXiv:1806.04649; Raveri & Doux 2021, arXiv:2105.03324 |
| Update difference in mean | `Q_UDM = (θ̂^{A+B} − θ̂^A)^T (C^A − C^{A+B})^-1 (θ̂^{A+B} − θ̂^A)` | χ² with `rank(C^A − C^{A+B})` degrees of freedom for Gaussian posteriors; usable when A and B are correlated, since it compares A with A+B; Karhunen–Loève modes kept for `0.2 < λ − 1 < 100` | arXiv:1806.04649 |
| Goodness-of-fit loss | change of best-fit χ² when the data sets are fitted jointly rather than separately | defined in §4.5 of arXiv:2012.09554, not transcribed here | arXiv:1806.04649 |
| Eigentension | difference restricted to the well-measured eigenmodes of one experiment | defined in §4.6 of arXiv:2012.09554, not transcribed here | arXiv:2012.09554 |
| Posterior predictive distribution | probability of data subset B given the posterior from subset A, with a p-value or the fraction `Δ_PPD` of the predictive density below the observed data | works on correlated probes and on the data vector rather than on parameters | Doux et al. 2021, arXiv:2011.03410; Doux et al. 2026, arXiv:2610.03447 |

Codes: `tensiometer` (parameter differences, `Q_UDM`), `anesthetic` (suspiciousness and dimensionality from nested-sampling chains), both named in arXiv:2012.09554 [src]; `unimpeded` (Ong, Yallup & Handley 2026, arXiv:2603.05472).

Three rules. (i) A tension in one projected parameter and a tension in the full shared parameter space are different numbers, and the second can be smaller: DES Y6 3×2pt against the CMB is 2.6σ projected on S8 and 1.8σ in the full space (DES Collaboration 2026, arXiv:2601.14559) [src]. (ii) Metrics that assume independent data (`R`, `S`, parameter differences as a convolution) cannot be applied to correlated data sets; use the update form or a posterior predictive test. (iii) The metric and the reference data set are part of the result: a "2σ tension" without both is not reproducible.

## 10. Fisher forecasts
<!-- key: fisher-forecasts -->

The Fisher information matrix is `F_αβ = E[(∂ ln L/∂θ_α)(∂ ln L/∂θ_β)]`; by the Cramér–Rao theorem its inverse is a lower bound on the covariance of unbiased estimators (as recalled in arXiv:2108.10402) [src]. For Gaussian data with mean `μ(θ)` and covariance `C`,

`F_αβ = (∂μ/∂θ_α)^T C^-1 (∂μ/∂θ_β) + (1/2) Tr[C^-1 (∂C/∂θ_α) C^-1 (∂C/∂θ_β)]`

(textbook form; the reference for its use in cosmology is Tegmark, Taylor & Heavens 1997, arXiv:astro-ph/9603021). The second term is the information in the covariance; for two-point statistics treated with a Gaussian likelihood it must be dropped (§1, Carron 2013). The marginalised 1σ forecast on `θ_α` is `sqrt((F^-1)_αα)`; the dark-energy figure of merit is proportional to `1/sqrt(det)` of the marginalised `w0`–`wa` block.

What a Fisher forecast assumes: a Gaussian posterior in the chosen parameters, a fiducial model that is the truth, exact derivatives, a known covariance, and no systematic outside the parameter list. It is a statement about the curvature at one point.

Where it fails, with the documented sizes:

- Non-Gaussian posteriors. Wolz et al. 2012 (arXiv:1205.3984) compare Fisher forecasts with MCMC for Stage-III and Stage-IV dark-energy surveys: for purely geometrical probes the Fisher matrix "underestimates the marginalized errors ... between 30%-70%", because it "can not reproduce the highly non-elliptical shape of the likelihood", especially when marginalising over `wa`; for probes including structure growth such as weak lensing the contours agree and the errors change at the 5% level [src]. Higher-order expansions (DALI, Sellentin, Quartin & Amendola 2014, named here without further detail) recover curved contours.
- Numerical derivatives. The Euclid forecast validation (Euclid Collaboration, Blanchard et al. 2020, arXiv:1910.09273) had to "compare and improve different numerical implementations" before independent codes agreed to within the required precision, and found that the results "depend on the specific cosmological model and remaining freedom in each setup" (flat or non-flat, non-linear cuts) [src].
- Boundaries and priors. A parameter at a physical boundary (Σm_ν) or a nuisance parameter with an informative prior is not described by a curvature.
- Projection effects (§6) are invisible to a Fisher matrix by construction: it has no volume term.
- Optimistic systematics. A forecast is conditional on its scale cuts and nuisance model; the "optimistic" and "pessimistic" settings of arXiv:1910.09273 are both conditional forecasts, not bounds.

Legitimate uses: survey design and relative comparisons, the choice of compression (§3), identification of well-measured modes before unblinding (the Karhunen–Loève modes of the tension metrics, §9), and fast marginalisation over linear nuisance parameters. A Fisher bias formula (first-order shift of the best fit from a systematic in the data vector) is the standard tool for setting requirements; it shares all the assumptions above.

## 11. Emulators
<!-- key: emulators -->

An emulator is a fast surrogate for an expensive theory prediction, trained on a design of exact evaluations. Two kinds must be kept apart.

| Kind | Replaces | Error is set by | Examples and stated accuracy |
|---|---|---|---|
| Emulator of a Boltzmann code or of a perturbative model | CAMB or CLASS spectra, EFT loop integrals | the interpolation (network or Gaussian process) only; the training data are exact and cheap, so the error can be made negligible | CosmoPower (Spurio Mancini et al. 2022, arXiv:2106.03846): matter power spectrum error below 0.4% for k in [10^-5, 10] Mpc^-1 and z in [0, 5]; CMB spectra within the 5σ region around the Planck best fit with error ≲ 10% of the Simons Observatory shot noise; speed-up up to O(10^4); posteriors recovered "with differences ... smaller than sampling noise" [src]. Effort for the EFTofLSS (Bonici et al. 2025, named here without further detail). |
| Emulator of N-body or hydrodynamic simulations | the non-linear matter power spectrum, halo statistics, galaxy clustering with an HOD, Lyα flux statistics | the interpolation plus the accuracy, resolution, volume and physics of the training simulations | EuclidEmulator2 (Euclid Collaboration, Knabenhans et al. 2021, arXiv:2010.11288): non-linear correction accurate to 1% or better for 0.01 ≤ k ≤ 10 h/Mpc and z ≤ 3 against dark-matter-only simulations, in the eight-parameter w0waCDM + Σm_ν space, from over 250 simulations of 3000³ particles in 1 (Gpc/h)³ boxes with paired-and-fixed initial conditions; blind test against the Flagship v2.0 simulation [src]. |

Error budget of an emulator-based likelihood, in the order a referee asks for it: (1) interpolation error, measured by leave-one-out or a held-out test set, as a function of scale, redshift and position in parameter space; (2) error of the training simulations themselves (resolution, box size, the "dark-matter-only" caveat: baryonic effects are not in a gravity-only emulator); (3) the boundary of the training design, where errors grow and beyond which the emulator must not be evaluated; (4) how the error enters the likelihood.

Three ways to propagate it: add an emulator covariance to the data covariance; marginalise over the approximation error using the errors the network reports in validation (Grandón & Sellentin 2022, arXiv:2205.11587, a Bayesian propagation that de-biases "even for strongly biased neural nets") [src]; or show that the error is negligible by rerunning the final chain with the exact code.

Differentiable emulators make gradient-based samplers and Fisher matrices by automatic differentiation available (§5, §10). Probe-specific emulators and their error budgets are in the probe skills: Lyα flux statistics in `cosmo-lyman-alpha`, small-scale clustering in `cosmo-galaxy-clustering` and `cosmo-beyond-two-point`, baryonic feedback in `cosmo-weak-lensing`.

## 12. Simulation-based inference
<!-- key: simulation-based-inference -->

### 12.1 What is learned
<!-- key: what-is-learned -->

Simulation-based inference (also called likelihood-free or implicit inference) replaces the analytic likelihood by a density learned from pairs (θ, d) drawn from the prior and the simulator. Three targets are in use: the likelihood `p(d given θ)` (neural likelihood estimation, then sampled with an ordinary sampler), the posterior `p(θ given d)` (neural posterior estimation, amortised over data), and the likelihood-to-evidence ratio (neural ratio estimation). The data are first compressed to a few summaries, by score compression (§3), a neural network, or hand-built statistics.

Reference for cosmology: Alsing et al. 2019 (arXiv:1903.00007), density-estimation likelihood-free inference with neural density estimators and active learning, public code `pydelfi`; "for typical problems high-fidelity posterior inference can be achieved with just O(10^3) simulations or fewer" [src].

What the simulator must contain is everything the likelihood would have contained: the signal model, noise, mask, selection, and every systematic with its prior. KiDS-SBI (von Wietersheim-Kramsta et al. 2024, arXiv:2404.15402) forward-models galaxy positions and shapes with shear and redshift calibration uncertainties, variable depth and point-spread-function anisotropy, on 18 000 realisations, with sequential neural likelihood estimation [src].

### 12.2 Validation tests
<!-- key: validation-tests -->

| Test | What it checks | Limitation | Reference |
|---|---|---|---|
| Simulation-based calibration | over many simulated data sets, the rank of the true parameter among posterior samples is uniform | one-dimensional marginals; needs posterior samples for each simulation | Talts et al. 2018, arXiv:1804.06788 |
| Expected coverage | the true value falls inside the α credible region a fraction α of the time, averaged over the prior | an average over the prior, not a statement at fixed θ | Hermans et al. 2022, arXiv:2110.06581 |
| TARP (tests of accuracy with random points) | coverage of regions defined around random reference points, from samples only; shown to be "necessary and sufficient" for an accurate posterior estimator | still averaged over the prior predictive distribution | Lemos et al. 2023, arXiv:2302.03026 |
| Comparison with a likelihood analysis on a statistic whose likelihood is known | posterior mean, variance and higher moments | available only for simple statistics | KiDS-SBI, arXiv:2404.15402; Alokda, Porciani & Eggemeier 2026, arXiv:2605.00980 |
| Goodness of fit, out-of-distribution test | whether the observed summaries lie inside the support of the simulated ones | does not validate the posterior shape | arXiv:2404.15402 (a probability-to-exceed for the forward model) |

### 12.3 Known limits
<!-- key: known-limits -->

- Overconfidence. Hermans et al. 2022 (arXiv:2110.06581): all benchmarked algorithms (neural posterior, ratio and likelihood estimation, sequential variants, approximate Bayesian computation) "can yield overconfident posterior approximations"; ensembles of surrogates mitigate the issue [src].
- Finite simulation budget. Homer, Friedrich & Gruen 2024 (arXiv:2412.02311): on a Gaussian linear model, simulation-based inference "suffers an inflation of posterior variance that is equal or greater than the analytical result in covariance estimation for Gaussian likelihoods for the same number of simulations"; "the assumption that SBI requires a smaller number of simulations than covariance estimation for a Gaussian likelihood analysis is inaccurate" [src].
- Coverage is necessary, not sufficient in practice. Alokda et al. 2026 (arXiv:2605.00980): for f_NL from halo fields over 1000 realisations, posteriors that pass coverage tests can be underconfident and differ from the likelihood-based ones in kurtosis, that is in the tails [src].
- Model misspecification. A posterior is only valid for data the simulator could have produced. The standard symptom is observed summaries outside the training distribution; `cosmo-beyond-two-point` documents the SimBIG wavelet case and the restrictions of each simulation suite.
- Prior edges. Training simulations drawn in a hard-edged uniform box give a density estimator that is least accurate near the boundary, which is where an upper or lower limit is read (the simulation suites and their boxes are in `cosmo-simulations-mocks`).

### 12.4 Explicit and implicit likelihoods are not rivals
<!-- key: explicit-and-implicit-likelihoods-are-not-rivals -->

Vinciguerra, Martinet & Gatti 2026 (arXiv:2607.17942) compare a Gaussian likelihood built from an emulator and a covariance with a learned likelihood on Euclid-like Gaussian mocks: the explicit route "becomes strongly miscalibrated under emulation inaccuracies or likelihood non-Gaussianity", the learned one stays calibrated, and the disagreement "largely vanishes once addressed" [src]. The calibration diagnostics developed for simulation-based inference apply equally to a classical likelihood pipeline, and few classical pipelines have been subjected to them.

## 13. Combining probes and correlated datasets
<!-- key: combining-probes-and-correlated-datasets -->

For independent data sets the joint likelihood is the product of the likelihoods. The work is in establishing independence, or in building the cross-covariance when it fails.

| Situation | Correct treatment | Example |
|---|---|---|
| Disjoint sky, disjoint redshift, no shared calibration | multiply likelihoods | BAO in separate redshift bins of different tracers, to good approximation |
| Same survey, several two-point functions | one data vector with a full covariance including cross terms | 3×2pt (arXiv:2012.08568 for DES Y3) |
| Same galaxies, two statistics | joint covariance from mocks, or an analytic cross-covariance | pre-reconstruction power spectrum and post-reconstruction BAO: an analytic approximation exists and the cross-covariance is "sufficiently small that even approximate treatments are adequate" (Maus et al. 2026, arXiv:2602.12343) [src] |
| Overlapping footprints of two surveys | joint mocks or a cross-covariance; never multiply | DES Y3 with KiDS-1000, done as a joint-survey analysis with a common pipeline (arXiv:2305.17173) |
| Two releases of one survey, or two surveys sharing volume | use one, or a combined measurement with the stated correlation | DESI DR1 and DR2; DESI and SDSS bins (the quoted SDSS–DESI difference depends on an assumed correlation, see `cosmo-galaxy-clustering`) |
| Compilations sharing objects or calibrators | they are not independent confirmations | the supernova compilations (see `cosmo-supernovae`) |
| Shared external prior | apply it once | BBN prior on ω_b, a τ prior, a CMB prior used in two of the combined likelihoods |
| CMB lensing with CMB primary, or with galaxy surveys on the same sky | lensing-induced covariance and sky overlap need to be assessed | see `cosmo-cmb`, `cosmo-cmb-lss-cross-correlations` |

Before combining: test consistency in the model in which the combination will be interpreted (§9). A combined posterior of two data sets in tension is narrow and centred where neither is; an extended model that relieves the tension is then preferred for that reason alone (arXiv:2511.10631).

Technical routes for combining posteriors without re-running everything: importance reweighting of one chain by the other likelihood (only when the second posterior lies within the bulk of the first), and density-estimation of each posterior followed by multiplication (the weighted `CombineHarvesterFlow` chains used by DESI for the DES Y3 3×2pt combination, arXiv:2503.14738) [src]. Both assume independence.

Nuisance parameters when surveys are combined: common parameters (intrinsic alignments, baryonic feedback) should be shared only if the samples are comparable; the DES Y3 + KiDS-1000 analysis had to reconcile intrinsic-alignment models, baryon mitigation, priors, samplers and non-linear power-spectrum models before combining (arXiv:2305.17173) [src].

## 14. Look-elsewhere effect
<!-- key: look-elsewhere-effect -->

When a signal is searched for over a range (a mass, a scale, a frequency, a redshift bin, a set of models or data cuts), the probability of a fluctuation of given local significance somewhere in the range exceeds the local p-value. The trial factor is "the ratio between the probability of observing the excess at some fixed mass point, to the probability of observing it anywhere in the range" (Gross & Vitells 2010, arXiv:1005.1891) [src].

- For `N` independent trials the Šidák correction is `p_global = 1 − (1 − p_local)^N`, approximately `N p_local` (Bonferroni) for small p (textbook).
- For a continuous search, Gross & Vitells give "a simple and fast procedure for estimating the trial factor, based on earlier results by Davies"; asymptotically "the trial factor grows linearly with the (fixed mass) significance" [src].
- Bayer & Seljak 2020 (arXiv:2007.13821) relate the trial factor to the prior-to-posterior volume ratio through the Laplace approximation of the Bayes factor, which gives "a continuous generalization of the Bonferroni and Sidak corrections" and accounts for extra degrees of freedom, "generalizing Wilks' theorem" [src]. The Ockham factor of the evidence and the frequentist trial factor are thus the same quantity seen from two sides.

In cosmology the effect rarely appears as a scan over one parameter; it appears as analysis freedom. Typical forms: an oscillation frequency or feature scale in the primordial spectrum (`cosmo-inflation-primordial`); the choice of one redshift bin, one tracer or one multipole range as "the" anomaly (CMB large-angle anomalies, `cosmo-tensions-anomalies`); the choice among several external data sets (three supernova compilations giving 2.8σ, 3.8σ and 4.2σ with the same BAO and CMB, arXiv:2503.14738); the choice of parameterisation of `w(z)`; the choice of projection for a tension (§9); the choice of statistic after seeing which one shows a signal. The honest global significance requires either pre-registration (blinding with frozen choices) or a simulation of the whole search under the null.

## 15. Public codes
<!-- key: public-codes -->

Only codes whose reference paper, or a paper naming them, was read this session. The wider ecosystem (CosmoSIS, MontePython, CAMB, CLASS, Firecrown) is in `cosmo-software-ecosystem`.

| Code | Purpose | Reference | Used by |
|---|---|---|---|
| Cobaya | sampling framework, Metropolis–Hastings with speed blocking, maximisation, importance reweighting | Torrado & Lewis 2021, arXiv:2005.05290 | DESI DR2 (arXiv:2503.14738), ACT DR6 (arXiv:2503.14452) |
| PolyChord | slice-sampling nested sampling, evidences | Handley et al. 2015, arXiv:1506.00171 | DES Y3 (arXiv:2202.08233); evidence grids (arXiv:2603.05472) |
| Nautilus | importance nested sampling with neural proposals | Lange 2023, arXiv:2306.16923 | DES Y6 (arXiv:2601.14559), KiDS-Legacy (arXiv:2503.19441) |
| `iminuit`, Powell, Nelder–Mead | best-fit search after sampling | named in arXiv:2503.14738, arXiv:2601.14559, arXiv:2503.19441 | DESI, DES, KiDS respectively |
| PROSPECT, Procoli, pinc | profile likelihoods | arXiv:2312.02972, arXiv:2401.14225, arXiv:2408.07700 | external analyses |
| `tensiometer` | parameter-difference tension, normalising-flow posterior densities | arXiv:1806.04649, arXiv:2105.03324 | DES |
| `anesthetic`, `unimpeded` | nested-sampling post-processing, suspiciousness; public evidence grid | named in arXiv:2012.09554; arXiv:2603.05472 | external analyses |
| RascalC | semi-analytic two-point covariance | arXiv:1904.11070 | DESI BAO |
| CosmoCov, OneCovariance | analytic 3×2pt and shear covariances | named in arXiv:2601.14559 and arXiv:2503.19441 | DES, KiDS |
| CosmoPower | neural emulators of Boltzmann-code spectra | arXiv:2106.03846 | KiDS-Legacy |
| EuclidEmulator2 | non-linear matter power spectrum | arXiv:2010.11288 | Euclid preparation |
| `pydelfi` | density-estimation likelihood-free inference | arXiv:1903.00007 | early simulation-based analyses |
| Smokescreen | data-vector blinding with encryption | arXiv:2604.18111 | LSST DESC |
| `getdist` | chain summaries and plots | named in arXiv:2503.14738 | most analyses |

## Not verified
<!-- key: not-verified -->

- The constant `A` in the Percival 2014 `m_1` factor, and the original Hartlap 2007 notation, were not transcribed from their papers; the Hartlap factor is quoted as written in arXiv:2108.10402.
- The Friedrich & Eifler precision-matrix proposal is described only as summarised in arXiv:2108.10402.
- The goodness-of-fit-loss and eigentension definitions (arXiv:2012.09554, §4.5 and §4.6) and the exact χ² combination of the suspiciousness were not transcribed.
- Foundational references not fetched and therefore not cited: Metropolis–Hastings, Gelman & Rubin 1992, Skilling's nested sampling, MultiNest, emcee, Wilks 1938, Jeffreys' scale, the deviance information criterion, Akaike and Schwarz criteria, the Savage–Dickey ratio, the DETF figure of merit, DALI, approximate Bayesian computation, the Kullback–Leibler divergence. Their definitions above are textbook statements.
- HMC and NUTS in a specific cosmological two-point analysis: no survey analysis using them as the production sampler was read; the statements concern the algorithm and its requirements.
- Shear-catalogue blinding of HSC, and the Planck likelihood architecture, are left to `cosmo-weak-lensing` and `cosmo-cmb`.
- The upcrossing formula of Gross & Vitells and the Laplace-approximation trial factor of Bayer & Seljak are described from their abstracts; the formulae were not transcribed.
