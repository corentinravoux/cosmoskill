# Statistics and inference — methods, defining formulae, reference papers

Scope: the statistical methods used in cosmological parameter inference, each with its defining formula, its reference paper and a cosmology example.
Snapshot: 2026-10-14

Flags: `[src]` read this session in the cited paper; `[sec]` taken from a named secondary source; `[der]` derived here, derivation stated.

Reviews. Trotta 2017, "Bayesian Methods in Cosmology" (arXiv:1701.01467): elementary notions and frequentist intervals; Bayesian parameter inference with priors, the Gaussian linear model and MCMC (Metropolis–Hastings, Gibbs, Hamiltonian Monte Carlo, importance sampling); model selection with the evidence, Occam's razor, p-values, nested sampling, thermodynamic integration, Laplace approximation, Savage–Dickey ratio and information criteria [src: section list]. Also Trotta 2008 (arXiv:0803.4089), Verde 2010 (arXiv:0911.3105) and Heavens 2009 lectures (arXiv:0906.0664), which covers Fisher matrices for survey design and numerical parameter estimation [src: abstracts]; Cranmer, Brehmer & Louppe 2020 (arXiv:1911.01429) for simulation-based inference [src].

## 1. Likelihoods and when the Gaussian approximation fails
<!-- key: likelihoods-and-when-the-gaussian-approximation -->

The default in large-scale-structure analyses is a multivariate Gaussian in the compressed statistic `d` (power spectrum, correlation function, multipoles): `−2 ln L = (d − m(θ))^T C^-1 (d − m(θ))` up to a constant, with `C` fixed in parameter space. It is an approximation in three distinct ways.

| Departure from the Gaussian form | What is known | Reference |
|---|---|---|
| The exact distribution of a power-spectrum estimate of a Gaussian field is Wishart (a scaled χ² per multipole), skewed at low multipole | For CMB T and polarisation on a cut sky, the Hamimeche–Lewis approximation "models the non-Gaussian form exactly in the ideal full-sky limit" and is validated at ℓ ≳ 30, where an exact calculation becomes impossible; pixel-based likelihoods are used below [src]. Full sky, `n` correlated fields: `−2 ln L = (2l+1) {Tr[Ĉ_l C_l^-1] − ln abs(C_l^-1 Ĉ_l) − n} = (2l+1) Σ_i [D_l,ii − ln D_l,ii − 1]`, `D_l` the eigenvalues of `C_l^-1/2 Ĉ_l C_l^-1/2`. Approximation: `g(x) = sign(x − 1) sqrt[2(x − ln x − 1)]` applied to the eigenvalues, `[X_g]_l = vecp(C_fl^1/2 g[C_l^-1/2 Ĉ_l C_l^-1/2] C_fl^1/2)`, and `−2 ln L ≈ Σ_ll' [X_g]_l^T [M_f^-1]_ll' [X_g]_l'` with `M_f` the estimator covariance at a fiducial model, precomputable. Exact on the full sky with isotropic noise "however wrong the fiducial model is"; `C_l`, `Ĉ_l` include noise; assumes `Ĉ_l` positive definite, "which may break down for some estimators at low l" [src: Sect. 3.5] | Hamimeche & Lewis 2008, arXiv:0801.0554 |
| Older single-field approximations, full-sky forms, as summarised by Hamimeche & Lewis | symmetric Gaussian with `Ĉ_l` in the denominator, "poor ... at low l", biases `C_l` low; quadratic with `C_l` in the denominator (often "misleadingly" called Gaussian: no determinant term) biases it high; fiducial-variance Gaussian `[(Ĉ_l − C_l)/C_fl]²`, wrong at each `l` but consistent once summed over a range of `l`; log-normal, correct to second order; the WMAP form `ln L = (1/3) ln L_Q + (2/3) ln L_LN`, correct to third order; the "1/3" forms, nearly correct to fourth order [src: arXiv:0801.0554, Sect. 3.1] | Hamimeche & Lewis 2008, arXiv:0801.0554 |
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
| The inverse of `S` is a biased estimate of `Σ^-1`; the bias depends on the ratio of the number of bins to the number of data sets, and `S` is singular when the number of bins exceeds the number of data sets | unbiased precision `Ψ = S^-1 / h`, with `h = (n_s − 1)/(n_s − n_d − 2)` [src: arXiv:2108.10402, where `hS` is called the Hartlap-corrected covariance]. As the paper writes it: `⟨Ĉ_*^-1⟩ = N/(N − p − 1) Σ^-1` for `p < N − 1`, with `N = n − 1` when the mean is estimated from the `n` realisations, hence the unbiased `Ĉ^-1 = (n − p − 2)/(n − 1) Ĉ_*^-1` for `p < n − 2`, `p` the number of bins [src: Sect. 3.1]. Conditions: Gaussian errors and statistically independent data vectors; the bias steepens the likelihood "but it does not change the maximum-likelihood point" [src: Sect. 3.1]. In a bootstrap test on shear pairs, which violates both conditions, the corrected estimator was "wrong by only ≈ 1%" [src: Sect. 5] | Hartlap, Simon & Schneider 2007, arXiv:astro-ph/0608064 |
| The noise in `Ψ` scatters the best fit: the true parameter covariance is larger than the Fisher one | `⟨p_α p_β⟩_s.o. = B F^-1_αβ (N_b − N_p)`, with `N_p < N_b` the number of fitted parameters [src: Sect. 3, main result], so `V = [1 + B (n_d − n_θ)] F^-1` [src: arXiv:1312.4841 Sect. 2]. With the Gaussian-case values of Taylor et al., `A = 2/[(N_s − N_b − 1)(N_s − N_b − 4)]`, `B = (N_s − N_b − 2)/[(N_s − N_b − 1)(N_s − N_b − 4)]`, "after correcting for the bias in the inverse covariance estimator"; for `N_s >> N_b >> N_p` the variance grows by `(1 + N_b/N_s)` [src: Sect. 3.1]. The extra term "does not alter the shape of the constraints"; a coefficient `B (N_b − N_p) = 0.1` is "equivalent to throwing away 10% of the data set" [src: Sect. 3]. The linear terms can bias the estimate when a parameter-dependent covariance is fixed, or when the covariance is correlated with the data (estimated from the data themselves) [src: Sect. 3] | Dodelson & Schneider 2013, arXiv:1304.2593 |
| The width read from the likelihood is also biased, by a different amount, so the measured parameter covariance must be rescaled | Hartlap step written `Ψ = (1 − D) C^-1`, `D = (n_b + 1)/(n_s − 1)`; `A`, `B` as above [src: Sect. 1, Eq. AB]. Width from integrating the likelihood: `σ̂² = [1 + A + B (n_p + 1)] F^-1`; hence `m_1 = [1 + B (n_b − n_p)] / [1 + A + B (n_p + 1)]`, applied to the parameter covariance, its square root to the standard deviation [src: Sect. 3]. A third factor `m_2` applies when the best-fit scatter is measured on the same mocks that built the covariance (not transcribed) [src: Sect. 7]. Correlated mock sets: `A`, `B`, `D` rescaled by `(1 + r²)/2`, equivalent to `n_s` multiplied by `2/(1 + r²)` [src: Sect. 6.1] | Percival et al. 2014, arXiv:1312.4841 |
| Marginalising over the unknown `Σ` with an independence-Jeffreys prior `π(Σ) ∝ abs(Σ)^(-(p+1)/2)` [src: Eq. 6] turns the Gaussian likelihood into a multivariate t-distribution | `P(X_o given μ, S, N) = c̄_p abs(S)^(-1/2) / [1 + (X_o − μ)^T S^-1 (X_o − μ)/(N − 1)]^(N/2)` [src: Eq. 12], `c̄_p = Γ(N/2) / {[π(N − 1)]^(p/2) Γ((N − p)/2)}`, requiring `N > p` [src: Eq. 13]; `N` simulations, `p` data points. Not the standard frequentist t-distribution: one data vector sets the peak, `N` simulations the covariance; the Wishart form is asymptotically appropriate for non-Gaussian data by the central limit theorem [src: Sect. 2.1] | Sellentin & Heavens 2016, arXiv:1511.05969 |
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

- Gaussian (disconnected) term plus connected non-Gaussian (trispectrum) term plus super-sample covariance. The effect was first identified as "beat-coupling" by Hamilton, Rimes & Scoccimarro 2006 (arXiv:astro-ph/0511416): products of closely spaced Fourier modes couple through non-linear growth to the beat mode between them, so that the covariance of non-linear power in a survey is "dominated not by small scale structure, but rather by beat-coupling to the largest scales of the survey"; it is absent from an ensemble of periodic boxes [src]. The super-sample term is the response of the power spectrum to a background density mode larger than the survey; it "dominates the covariance of power spectrum estimators for modes much smaller than the survey" for a wide range of volumes (Takada & Hu 2013, arXiv:1302.6994) [src].
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
| Karhunen–Loève (signal-to-noise eigenmodes) | projections on the generalised eigenvectors of signal and noise covariances | Gaussian data, one parameter; an extra singular-value step handles several parameters and unknown fiducial values | Tegmark, Taylor & Heavens 1997, arXiv:astro-ph/9603021 [src]; first applied to galaxy redshift surveys, as the statistically orthogonal modes of a given geometry and selection function, by Vogeley & Szalay 1996, arXiv:astro-ph/9601185 [src] |
| MOPED | `y_m = b_m^t x`, `b_m = [C^-1 μ_,m − Σ_{q<m} (μ_,m^t b_q) b_q] / sqrt[μ_,m C^-1 μ_,m − Σ_{q<m} (μ_,m^t b_q)²]` (for `m = 1` the sums vanish): Gram–Schmidt with `C` as metric; the `y_m` are uncorrelated with unit variance, so `ln L = const − Σ_m (y_m − ⟨y_m⟩)²/2` [src: Sect. 2.1] | the covariance does not depend on the parameters; then the likelihood surface is "on average ... locally identical" to that of the full data [src: Sect. 2.1]; orthonormality "only holds if the fiducial model is correct", iterate if needed [src: Sect. 2.1]; with parameter-dependent noise the errors increase "by a very modest factor" [src] | Heavens, Jimenez & Lahav 2000, arXiv:astro-ph/9911102 |
| Score compression | for a Gaussian likelihood `t = ∇μ_*^T C_*^-1 (d − μ_*) + (1/2)(d − μ_*)^T C_*^-1 ∇C_* C_*^-1 (d − μ_*)`, with `Cov[t, t] = F_*` [src: Eq. 17]; the quasi-maximum-likelihood estimator `θ̂ = θ_* + F_*^-1 [...]` [src: Eq. 18]. The linear term alone is MOPED (∇C = 0), the quadratic term alone the optimal quadratic power-spectrum estimator [src: Sect. 3] | saturates the information inequality in all cases, where Karhunen–Loève is lossy when the covariance depends on the parameters [src: Sect. 3]; conditions: score defined on the support of the likelihood, expectation and derivative interchangeable [src: Sect. 5]. Failure: a many-to-one map `d → t` creates spurious posterior modes; remedy, several expansion points [src: Sect. 5] | Alsing & Wandelt 2018, arXiv:1712.00012 |
| Principal components of the data vector | leading eigenmodes of the data covariance | never exactly; a factor ~5 reduction kept most of the information for shear correlation functions | Lin et al. 2020, arXiv:1905.03779 [src] |
| Physical compression | BAO scaling parameters, `fσ8`, ShapeFit parameters, CMB shift parameters (θ*, ω_b, ω_bc) | only within the model class used to define them | DESI uses the compressed CMB prior (θ*, ω_b, ω_bc) as its minimal early-Universe information (arXiv:2503.14738) [src] |
| Neural compression | a network trained to output parameter estimates or informative summaries | not guaranteed; must be validated | see §12 |

Costs and cautions. (i) Compression is optimal at the fiducial point only; far from it information is lost, never invented, so the result is conservative but can be biased if the fiducial model is poor: iterate. (ii) The compression needs a covariance and derivatives; if the covariance is noisy, the compressed statistic is noisy but the number of mocks needed scales with the compressed dimension (Percival et al. 2022, arXiv:2108.10402, have an appendix on compressing the data in this context). (iii) Compressed data hide model misfit: a goodness-of-fit test on `n` numbers for `n` parameters has no degrees of freedom left; keep a test on the uncompressed vector. (iv) A physical compression carries its model: a compressed CMB prior excludes lensing and late-time information by construction, which is why DESI + compressed CMB gives 2.4σ where DESI + full CMB gives 3.1σ for w0wa (arXiv:2503.14738) [src]. (v) Finite compression can degrade an explicit-likelihood analysis while leaving a learned likelihood nearly unaffected (arXiv:2607.17942) [src].

## 4. Blinding strategies
<!-- key: blinding-strategies -->

The purpose of blinding is "to hide an experiment's critical results ... until all decisions affecting its analysis have been finalised" (Muir et al. 2020, arXiv:1911.05929) [src]. The practice comes from nuclear and particle physics, reviewed by Klein & Roodman 2005 (doi:10.1146/annurev.nucl.55.090704.151521): a blind analysis prevents experimenters "from knowing the answer until the analysis is complete", with "at least circumstantial evidence" that bias affected past measurements [src]. The schemes differ by the level at which the data are altered.

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
| Metropolis–Hastings MCMC | random-walk proposals from a learned covariance, with fast and slow parameter blocks | no | no | Metropolis et al. 1953 (doi:10.1063/1.1699114) [src: abstract]; first cosmological MCMC code CosmoMC, Lewis & Bridle 2002 (arXiv:astro-ph/0205436) [src]; fast–slow decorrelation and "dragging", Lewis 2013 (arXiv:1304.4473) [src]. Cobaya (Torrado & Lewis 2021, arXiv:2005.05290): parameters "grouped in blocks according to their dependencies and optimally sorted" by cost, caching of intermediate results, sub-millisecond overhead [src]. DESI DR2 cosmology chains (arXiv:2503.14738). |
| Nested sampling | live points climbing iso-likelihood shells; the evidence is the primary output, the posterior a by-product | yes | no | Skilling 2006 (doi:10.1214/06-BA127): sampling "within a hard constraint on likelihood value", the evidence with "an estimate of numerical uncertainty" [src: abstract]. With the prior mass `X(λ) = ∫_{L > λ} p(θ) dθ`, `Z = ∫_0^1 L(X) dX ≈ Σ_i L(X_i) W_i`, `W_i = (X_{i−1} − X_{i+1})/2` (as written in Trotta 2017, arXiv:1701.01467) [src: Sect. 4.3.1]. MultiNest, Feroz, Hobson & Bridges 2009 (arXiv:0809.3437): multimodal ellipsoidal nested sampling with an evidence error estimate [src]. PolyChord (Handley, Hobson & Lasenby 2015, arXiv:1506.00171): slice sampling inside the hard likelihood constraint, exploits a hierarchy of parameter speeds [src]. DES Y3 choice (Lemos et al. 2023, arXiv:2202.08233). MultiNest is the ellipsoidal variant discussed in the same paper. |
| Importance nested sampling with a learned proposal | neural-network regression builds the proposal; all likelihood calls are used | yes | no | nautilus (Lange 2023, arXiv:2306.16923): efficiency "substantially higher than that of all other samplers, often by more than an order of magnitude" on its benchmarks [src]. |
| Hamiltonian Monte Carlo, NUTS | trajectories following the gradient of the log posterior; NUTS chooses the path length automatically and adapts the step size by dual averaging | no | yes | Neal 2011 review (arXiv:1206.1901): fictitious momenta give distant Metropolis proposals; volume preservation avoids a Jacobian "even when the dynamics is approximated by discretizing time" [src]. Hoffman & Gelman 2014 (arXiv:1111.4246) [src]. Requires a differentiable likelihood, hence emulators or auto-differentiable codes (§11). Used for field-level inference, where the dimension is 10^5 to 10^7 (see `cosmo-beyond-two-point`). |
| Affine-invariant ensemble sampler | walkers proposing along each other's positions; 1 or 2 tuning parameters against ~N² for a Metropolis proposal | no | no | `emcee`, Foreman-Mackey et al. 2013 (arXiv:1202.3665) [src] |
| GPU nested sampling with neural emulators | vectorised likelihood on a GPU | yes | no | Lovick et al. 2025 (arXiv:2509.13307): Bayes factors for a 39-dimensional ΛCDM against w0wa shear analysis "in just 2 days on a single A100 GPU" [src]. |

### 5.2 Convergence criteria actually used
<!-- key: convergence-criteria-actually-used -->

- DESI DR2 (arXiv:2503.14738, §5) [src]: Metropolis–Hastings in Cobaya with CAMB; convergence when the Gelman–Rubin statistic satisfies `R − 1 < 0.01`, "or that the chains have an effective sample size of ≳ 10^3, whichever is longer"; summaries with `getdist`; mean and standard deviation for symmetric posteriors, the 68% minimal credible interval otherwise; limits at 68% except Σm_ν at 95%; best fit with `iminuit` started from the MAP of each chain.
- The `R − 1` of cosmology codes (Lewis 2013, arXiv:1304.4473, CosmoMC, and the DESI and ACT chains through Cobaya) is a "generalized Gelman-Rubin statistic": the between-chain covariance of the chain means `C_x̄ = Σ_i (x̄_i − x̄)(x̄_i − x̄)^T/(n − 1)`, orthonormalised by the Cholesky factor of the mean within-chain covariance `C_x = L L^T`, and `R − 1 ≡ max(D_i)` over the eigenvalues of `L^-1 C_x̄ L^-T`, the largest variance of any orthonormalised parameter mean in units of the posterior variance; "typically chains are run to obtain `R − 1 ≲ 0.1`", and `R − 1 ~ 0.02` "works well for many purposes" [src: Sect. IV.1]. It tests the means; for intervals the statistic must be generalised to the between-chain variance of the confidence limits [src: Sect. IV.1].
- The diagnostic comes from Gelman & Rubin 1992 (doi:10.1214/ss/1177011136), who recommend several independent sequences from overdispersed starts [src: abstract].
- The statistics literature defines split-`R̂ = sqrt(var⁺/W)` with `var⁺ = (N − 1) W/N + B/N`, `B` and `W` the between- and within-chain variances over `M` half-chains of `N` draws (Vehtari et al. 2021, arXiv:1903.08008) [src: Eqs. 1–4]. Recommended practice: rank-normalised, folded `R̂ < 1.01`, "much tighter than the one recommended by Gelman and Rubin (1992)" (1.1); at least four chains; rank-normalised bulk and tail effective sample size above 400 [src: Sect. 2]. A cosmology `R − 1 < 0.01` is roughly `R̂ < 1.005`, not `R̂ < 1.01` `[der: for one parameter and large N, Lewis's D ≈ B/(N W) ≈ R̂² − 1 ≈ 2(R̂ − 1); ignores the eigenvalue maximum and chain splitting]`.
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

The formulas as the papers write them:

- Profile likelihood-ratio statistic `t_μ^LR(x) = −2 log[L_x(μ, ν̂̂)/L_x(μ̂, ν̂)]`, `ν̂̂` the conditional maximum-likelihood nuisance values at fixed `μ`: "frequentist statistics [handle nuisance parameters] by optimization instead" (Herold et al. 2024, arXiv:2408.07700) [src: Eq. 6]. Wilks: in the limit of a large data set `t` is χ²-distributed, and non-central χ² for `μ` away from the truth [src: Sect. III.5]. Wald's relation `t = (μ̂ − μ)²/σ_μ²`, with `σ_μ` often estimated on the Asimov data set [src: Eq. 7]. Only when all three hold, independently of the nuisance parameters, does the Neyman construction reduce to the graphical one, "just considering the iso-contours of the profile likelihood"; the prerequisites "are often not checked in detail" [src: Sect. III.5].
- With a boundary `μ ≥ 0`, the denominator is taken at the best physical value: `t = −2 log[L(μ, ν̂̂)/L(0, ν̂̂_0)]` if `μ̂ < 0`, Eq. 6 otherwise [src: Eq. 8]. Then `t = μ²/σ² − 2μμ̂/σ²` for `μ̂ < 0`, linear instead of parabolic [src: Eq. 10]; at `μ = 0` the distribution is a "half-χ²" with half the mass at zero. For a Gaussian with `σ = 1` and an observed `t_obs = 0.25` (their Fig. 1), the cut-offs become ~0.6 instead of 1 (68%) and ~2.9 instead of 4 (95%): "the correction from the boundary leads to tighter constraints" than a naive graphical reading [src: Sect. III.6].
- Feldman & Cousins ordering: values of `x` enter the acceptance region at fixed `μ` in decreasing order of `R(x) = P(x given μ)/P(x given μ_best)`, `μ_best = max(0, x)`, so that `R = exp(−(x − μ)²/2)` for `x ≥ 0` and `exp(xμ − μ²/2)` for `x < 0`; `[x_1, x_2]` with `R(x_1) = R(x_2)` and `∫ P(x given μ) dx = α` (arXiv:physics/9711021) [src: Sect. 4.2]. Consequences: the interval turns into an upper limit below `x = 1.28` at 90% CL; the 90% upper limit at `x = 0` is 1.64, the standard 95% one, the price of repairing flip-flopping; for large negative `x` limits fall as `1/abs(x)`, so measurements unlikely for every physical `μ` need "particular caution" [src: Sect. 4.2].

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
| Akaike criterion | `AIC ≡ −2 ln L_max + 2k` [src: Trotta 2017, arXiv:1701.01467, Sect. 4.3.5] | no | yes, penalised | quick ranking |
| Bayesian information criterion | `BIC ≡ −2 ln L_max + k ln N`, from a Gaussian approximation of the evidence at large `N`; harsher than AIC for `N > 7` [src: same] | no (asymptotic) | yes, penalised | quick ranking |
| Deviance information criterion | `DIC = D(θ̄) + 2 p_D`, `D = −2 ln L`, `p_D = <D> − D(θ̄)` (textbook); written `DIC ≡ −2 D_KL + 2 C_b`, `C_b` the effective number of parameters, in arXiv:1701.01467 [src: Sect. 4.3.5]. AIC and BIC "penalize extra parameters regardless of whether they are constrained by the data", unlike the evidence [src: same] | weakly, through the posterior | yes, penalised | DESI, KiDS |
| Bayesian evidence | `Z = ∫ L(θ) π(θ) dθ` | yes, linearly in the prior volume of the extra parameters | yes | nested sampling analyses |
| Bayes factor | `B = Z_1 / Z_0`; for nested models with separable priors `p(θ_0, θ_1 given M_1) = p(θ_1 given M_1) p(θ_0 given M_0)`, the Savage–Dickey ratio `B_01 = p(θ_1 given d, M_1)/p(θ_1 given M_1)` at `θ_1 = 0` [src: arXiv:1701.01467, Sect. 4.3.4] | yes | yes | "ln B" |
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

The probability-to-σ step is written `N_σ ≡ sqrt(2) Erf^-1(PTE)` in Lemos et al. 2021 (arXiv:2012.09554) [src: Eq. 4] and `n_σ = sqrt(2) erf^-1(Δ)` in DES Y6 (arXiv:2601.14559); in both the argument is the probability mass inside the contour, so it is a two-sided equivalent `[der: erf(n/sqrt 2) is the Gaussian mass within ±nσ]`.

Conditions for the conversion to hold: nested models, the simpler model in the interior of the larger one's parameter space, Gaussian asymptotics, no parameter that becomes unidentified under the null. `sqrt(Δχ²)` is the significance only for one extra parameter; applying it to w0wa would turn 3.1σ into 3.5σ `[der]`.

### 8.3 Why evidence and Δχ² can disagree
<!-- key: why-evidence-and-chi2-can-disagree -->

For a nested model with extra parameters whose prior width is much larger than the posterior width, the Bayes factor carries an Ockham factor of order (posterior width)/(prior width) per extra parameter. A `Δχ²` significance has no such factor. With the same data the two can therefore differ in sign: this is the Lindley paradox, and it is the situation of w0wa in 2025–2026 (`results.md` §4). Efstathiou 2008 (arXiv:0802.3185) made the argument with dark energy as the example: the evidence rests on "subjective judgements concerning the choice of model and priors", and for nested problems "Bayesian parameter estimation can be more informative than computing Bayesian Evidence for poorly motivated physical models" [src].

The Jeffreys scale as used by DES for `log R`: above 2.3 strong, 1.2 to 2.3 substantial, −1.2 to 1.2 inconclusive, and symmetrically for tension (Lemos et al. 2021, arXiv:2012.09554, table 1) [src]. The same paper notes that "the boundaries in Jeffreys' scale are arbitrary, and they lack obvious interpretation as a statistical significance". DESI's rule of thumb for the information criterion: `Δ(DIC) < −5` "strong", `< −10` "decisive" (arXiv:2503.14738) [src].

## 9. Tension metrics
<!-- key: tension-metrics -->

Tension metrics answer one of two questions (Lemos et al. 2021, arXiv:2012.09554) [src]. Evidence-based methods ask whether the model can generate the data of both experiments with one set of parameters. Parameter-space methods ask how significant the difference between the two posteriors is, in the parameters both experiments constrain. All formulae below were read in §4 of that paper; equation numbers are those of arXiv:2012.09554 unless another paper is named. Probabilities are converted with `N_σ ≡ sqrt(2) Erf^-1(PTE)` [src: Eq. 4], "only a convenient proxy" that "does not assume Gaussianity per se" [src: Sect. 3.1].

| Metric | Definition | Property | Reference |
|---|---|---|---|
| 1D difference | `(x_A − x_B) / sqrt(σ_A² + σ_B²)` | valid for one Gaussian parameter and independent data; ignores the other dimensions | textbook |
| Bayes ratio | `R = Z_AB / (Z_A Z_B) = ∫ P_A P_B / Π dθ` | proportional to the prior volume for a flat prior: "doubling the prior volume doubles the value of R"; read on the Jeffreys scale | used in DES Y1; critique in Handley & Lemos 2019, arXiv:1902.04029 |
| Information ratio | `log I = D_A + D_B − D_AB` [src: Eq. 10], with `D = ∫ P log(P/Π) dθ` the Kullback–Leibler divergence [src: Eq. 11] | carries the prior dependence | arXiv:1902.04029 |
| Suspiciousness | `log S = log R − log I` [src: Eq. 12] | prior-volume independent, "the version of R that corresponds to the smallest priors that do not significantly alter the posterior"; for Gaussian posteriors "it follows a `χ²_d` distribution", `d` the dimensions constrained by both data sets, giving `p_T` as its p-value; Box–Cox Gaussianisation preserves `S` [src: Sect. 4.2] | arXiv:1902.04029 |
| Bayesian model dimensionality | `d = 2 ∫ P (log(P/Π) − D)²` [src: Eq. 13] | the number of parameters the data constrain; equals 1 for a 1D Gaussian; unlike the Bayesian model complexity it needs no mean or MAP point [src: Sect. 4.2] | arXiv:1902.04029 |
| Parameter difference | `P(Δθ) = ∫_{V_p} P_A(θ) P_B(θ − Δθ) dθ` for uncorrelated data sets [src: Eq. 14], `Δ = ∫_{P(Δθ) > P(0)} P(Δθ) dΔθ` [src: Eq. 15] | invariant under reparameterisation; Monte Carlo over the `N_A N_B` sample pairs with a Gaussian KDE at Silverman's bandwidth, binomial error [src: Sect. 4.3]; normalising flows in high dimension | Raveri & Hu 2019, arXiv:1806.04649; Raveri & Doux 2021, arXiv:2105.03324 |
| Update difference in mean | `Q_UDM = (θ̂^{A+B} − θ̂^A)^T (C^A − C^{A+B})^-1 (θ̂^{A+B} − θ̂^A)` | χ² with `rank(C^A − C^{A+B})` degrees of freedom for Gaussian posteriors; usable when A and B are correlated, since it compares A with A+B; Karhunen–Loève modes kept for `0.2 < λ − 1 < 100` | arXiv:1806.04649 |
| Goodness-of-fit loss | `Q_DMAP = 2 ln L_A(θ_pA) + 2 ln L_B(θ_pB) − 2 ln L_A+B(θ_pA+B)`, likelihoods at each MAP [src: Eq. 19] | χ² with `ΔN_eff = N_eff^A + N_eff^B − N_eff^A+B` degrees of freedom [src: Eq. 20], `N_eff = N − tr[C_Π^-1 C_p]` [src: Eq. 21], when likelihoods and posteriors are Gaussian; requires Gaussianity "in both data space and parameter space" [src: Sect. 4.5] | arXiv:1806.04649 |
| Eigentension | eigenvectors of one experiment's parameter covariance whose prior-to-posterior variance ratio exceeds 10², fixed a priori on a noiseless data vector; both chains projected on them, KDE of the difference, mass inside the contour through zero [src: Sect. 4.6]. For DES Y1 one mode, `σ8 Ω_m^0.57`, variance ratio 2665 [src: Eq. 22] | 1.28 × 10^7 Monte Carlo draws reach 5.4σ [src: Sect. 4.6] | arXiv:2012.09554 (method of Park & Rozo 2019, not read) |
| Posterior predictive distribution | probability of data subset B given the posterior from subset A, with a p-value or the fraction `Δ_PPD` of the predictive density below the observed data | works on correlated probes and on the data vector rather than on parameters | Doux et al. 2021, arXiv:2011.03410; Doux et al. 2026, arXiv:2610.03447 |

Codes: `tensiometer` (parameter differences, `Q_UDM`), `anesthetic` (suspiciousness and dimensionality from nested-sampling chains), both named in arXiv:2012.09554 [src]; `unimpeded` (Ong, Yallup & Handley 2026, arXiv:2603.05472).

Three rules. (i) A tension in one projected parameter and a tension in the full shared parameter space are different numbers, and the second can be smaller: DES Y6 3×2pt against the CMB is 2.6σ projected on S8 and 1.8σ in the full space (DES Collaboration 2026, arXiv:2601.14559) [src]. (ii) Metrics that assume independent data (`R`, `S`, parameter differences as a convolution) cannot be applied to correlated data sets; use the update form or a posterior predictive test. (iii) The metric and the reference data set are part of the result: a "2σ tension" without both is not reproducible.

## 10. Fisher forecasts
<!-- key: fisher-forecasts -->

The Fisher information matrix is `F_αβ = E[(∂ ln L/∂θ_α)(∂ ln L/∂θ_β)]`; by the Cramér–Rao theorem its inverse is a lower bound on the covariance of unbiased estimators (as recalled in arXiv:2108.10402) [src]. For Gaussian data with mean `μ(θ)` and covariance `C`,

`F_αβ = (∂μ/∂θ_α)^T C^-1 (∂μ/∂θ_β) + (1/2) Tr[C^-1 (∂C/∂θ_α) C^-1 (∂C/∂θ_β)]`

(written so in Alsing & Wandelt 2018, arXiv:1712.00012 [src: Eq. 16]; the reference for its use in cosmology is Tegmark, Taylor & Heavens 1997, arXiv:astro-ph/9603021). The second term is the information in the covariance; for two-point statistics treated with a Gaussian likelihood it must be dropped (§1, Carron 2013). The marginalised 1σ forecast on `θ_α` is `sqrt((F^-1)_αα)`; the dark-energy figure of merit is proportional to `1/sqrt(det)` of the marginalised `w0`–`wa` block.

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

Foundations: conditional density estimation of the posterior without an ε-ball, Papamakarios & Murray 2016 (arXiv:1605.06376) [src]; for cosmology, score compression to one number per parameter followed by density estimation, Alsing, Wandelt & Feeney 2018 (arXiv:1801.01497) [src]; review, arXiv:1911.01429. Reference for cosmology: Alsing et al. 2019 (arXiv:1903.00007), density-estimation likelihood-free inference with neural density estimators and active learning, public code `pydelfi`; "for typical problems high-fidelity posterior inference can be achieved with just O(10^3) simulations or fewer" [src].

What the simulator must contain is everything the likelihood would have contained: the signal model, noise, mask, selection, and every systematic with its prior. KiDS-SBI (von Wietersheim-Kramsta et al. 2024, arXiv:2404.15402) forward-models galaxy positions and shapes with shear and redshift calibration uncertainties, variable depth and point-spread-function anisotropy, on 18 000 realisations, with sequential neural likelihood estimation [src].

### 12.2 Validation tests
<!-- key: validation-tests -->

| Test | What it checks | Limitation | Reference |
|---|---|---|---|
| Simulation-based calibration | for `θ̃ ~ π(θ)`, `ỹ ~ π(y given θ̃)` and `L` posterior draws given `ỹ`, the rank of `f(θ̃)` among the `f(θ_l)` is uniform over the integers [0, L], for any joint distribution [src: Theorem 1]; histogram with a 99% band from Binomial(N, 1/(L+1)), `N/B ≈ 20` replications per bin; spikes at the edges flag autocorrelated draws, so MCMC draws must be thinned [src: Sects. 4.1–4.2] | one-dimensional quantities `f`, one histogram each; needs posterior samples for each simulation | Talts et al. 2018, arXiv:1804.06788 |
| Expected coverage | `E_p(θ,x)[1(θ ∈ Θ_p̂(θ given x)(1 − α))]`, `Θ` the highest-posterior-density region [src: Eq. 2], estimated by the fraction of `n` joint draws whose true `θ*_i` falls inside [src: Eq. 5]; equal to the expected frequentist coverage `E_p(θ) E_p(x given θ)` [src: Eq. 3]; "conservative" when it is at least the credibility level [src: Def. 2.2] | an average over the prior, "no guarantee on the quality of a single posterior approximation"; a posterior equal to the prior passes, so pair it with the expected information gain [src: Sect. 2.2]; for non-amortised methods each coverage point needs a full retraining (300 observables in the benchmark) [src: Sects. 3.3–3.4] | Hermans et al. 2022, arXiv:2110.06581 |
| TARP (tests of accuracy with random points) | coverage of regions defined around random reference points, from samples only; shown to be "necessary and sufficient" for an accurate posterior estimator | still averaged over the prior predictive distribution | Lemos et al. 2023, arXiv:2302.03026 |
| Comparison with a likelihood analysis on a statistic whose likelihood is known | posterior mean, variance and higher moments | available only for simple statistics | KiDS-SBI, arXiv:2404.15402; Alokda, Porciani & Eggemeier 2026, arXiv:2605.00980 |
| Goodness of fit, out-of-distribution test | whether the observed summaries lie inside the support of the simulated ones | does not validate the posterior shape | arXiv:2404.15402 (a probability-to-exceed for the forward model) |

### 12.3 Known limits
<!-- key: known-limits -->

- Overconfidence. Hermans et al. 2022 (arXiv:2110.06581): all benchmarked algorithms (neural posterior, ratio and likelihood estimation, sequential variants, approximate Bayesian computation) "can yield overconfident posterior approximations"; ensembles of surrogates mitigate the issue [src]. In the body: budgets from 2^10 to 2^17 simulations, problems with up to 3 parameters [src: Sect. 3.3]; every method is non-conservative on at least one problem, most often non-amortised methods at small budgets, and "a large simulation budget does not guarantee" conservativeness; ensembles of five raise coverage but can still be non-conservative; approximate Bayesian computation with a sufficient statistic is not conservative either [src: Sect. 3.4]. A coverage-calibrated fix is to replace the α region by the level that has the desired expected coverage [src: Sect. 3.4].
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
- For a continuous search, Gross & Vitells give "a simple and fast procedure for estimating the trial factor, based on earlier results by Davies"; asymptotically "the trial factor grows linearly with the (fixed mass) significance" [src]. The formulas: for a parameter `θ` that does not exist under the null, with `q(θ)` χ²-distributed with `s` degrees of freedom at fixed `θ`, `P(q(θ̂) > c) ≤ P(χ²_s > c) + ⟨N(c)⟩`, `N(c)` the number of upcrossings of level `c` [src: Eq. 1]; `⟨N(c_0)⟩` is counted at a low reference level in a few background-only simulations and scaled as `(c/c_0)^((s−1)/2) e^(−(c−c_0)/2)` [src: Eq. 3], best at `c_0 = s − 1`. For `c >> s`, `P ≈ P(χ²_s > c) + 𝒩 P(χ²_(s+1) > c)`, `𝒩` the effective number of independent search regions [src: Eqs. 5–6], and the trial factor is `≈ 1 + sqrt(π/2) 𝒩 Z_fix` for `s = 1` [src: Eq. 12]. Conditions: Wilks holds at fixed `θ`; the bound becomes an equality only for `⟨N(c)⟩ << 1` [src: Sect. 2].
- Bayer & Seljak 2020 (arXiv:2007.13821) relate the trial factor to the prior-to-posterior volume ratio through the Laplace approximation of the Bayes factor, which gives "a continuous generalization of the Bonferroni and Sidak corrections" and accounts for extra degrees of freedom, "generalizing Wilks' theorem" [src]. In the body, for one signal amplitude and a `t`-tailed test: global p-value `N t e^(−q̂_L/2)/sqrt(2π q̂_L)` [src: Eq. 3.2], the test statistic `q_S = q_L − 2 ln N + ln(2π q_L) − 2 ln t` with global p-value `→ e^(−q̂_S/2)` [src: Eqs. 3.3–3.4], and the trial factor `N = V_>1,prior / V̂_>1,posterior`, the prior-to-posterior volume of the non-amplitude parameters, with no trial factor from the amplitude [src: Eqs. 3.7–3.8]. The Ockham factor of the evidence and the frequentist trial factor are thus the same quantity seen from two sides.

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

- The Percival 2014 factor `m_2` (best-fit scatter measured on the mocks that built the covariance) was not transcribed. (The constant `A` and the original Hartlap 2007 notation are now in §2.1.)
- The Friedrich & Eifler precision-matrix proposal is described only as summarised in arXiv:2108.10402.
- The Park & Rozo eigentension paper and the Handley & Lemos derivation of the suspiciousness χ² were not read; §9 quotes them as summarised in arXiv:2012.09554.
- Foundational references not cited: Wilks 1938 (DOI confirmed on Crossref, no abstract available) and Duane et al. 1987 on hybrid Monte Carlo (same); Jeffreys' scale, the original DIC, Akaike and Schwarz papers, the DETF figure of merit, DALI, approximate Bayesian computation, the Kullback–Leibler divergence. AIC, BIC, DIC and Savage–Dickey are quoted from the Trotta 2017 review.
- HMC and NUTS in a specific cosmological two-point analysis: no survey analysis using them as the production sampler was read; the statements concern the algorithm and its requirements.
- Shear-catalogue blinding of HSC, and the Planck likelihood architecture, are left to `cosmo-weak-lensing` and `cosmo-cmb`.
