# Statistics and inference — failure modes

Scope: the ways a cosmological inference goes wrong for statistical reasons, one subsection each: mechanism, size where a paper quantifies it, standard mitigation, validation test, the paper a referee expects cited.
Snapshot: 2026-10-14

Flags: `[src]` read this session in the cited paper; `[sec]` taken from a named secondary source; `[der]` derived here, derivation stated.

## 1. Noisy covariance from too few mocks
<!-- key: noisy-covariance-from-too-few-mocks -->

**Mechanism.** A covariance estimated from `n_s` mocks is a Wishart random matrix. Its inverse is biased high (errors too small), the bias growing with `n_d/n_s`, and `S` is singular for `n_d > n_s` (Hartlap et al. 2007, arXiv:astro-ph/0608064). Independently, the noise in the precision matrix scatters the best fit by a factor `1 + B (n_d − n_θ)` in variance (Dodelson & Schneider 2013, arXiv:1304.2593), and the width read from the likelihood is biased by yet another factor (Percival et al. 2014, arXiv:1312.4841).

**Size.** See `results.md` §1.1: for 1000 mocks, the error bar of a posterior built on the raw sample covariance must be widened by 10% (100 data points), 24% (200) and 65% (400); of that, the irreducible scatter of the best fit against a perfectly known covariance is 5%, 11% and 29% `[der]`. Percival et al. 2014 quote about 20% for BOSS with 600 mocks [src].

Worked examples in the papers, two readings kept apart. Dodelson & Schneider 2013 (arXiv:1304.2593) give the "fractional increase in variance" of each parameter from the best-fit scatter term: BOSS, 600 mocks, 41 bins, 7%; DLS, 1000, 60, 6%; CFHTLenS, 184, 24, 13% [src: Table 1, Sect. 3.3]. These are variance factors; on the error bar they are about 3.4%, 2.9% and 6.3% `[der: square root]`. Neither includes the Hartlap bias of the precision matrix, which those analyses corrected separately. Hartlap et al. 2007 show that ignoring that bias makes confidence regions too small without moving the maximum-likelihood point (arXiv:astro-ph/0608064) [src: Sect. 3.1]. A statement "N mocks inflate the errors by x%" must say whether x is on the variance or the error bar, and whether the Hartlap term is included.

Non-independent mocks. BOSS DR10 and DR11 drew the north and south caps of joint mocks from overlapping boxes. The correlation coefficient between mock measurements is `r = 2 V_overlap/(V_NGC + V_SGC)`: 0.016, 0.33 and 0.49 for DR9, DR10 and DR11. The covariance noise was modelled by rescaling `A`, `B`, `D` by `(1 + r²)/2`, that is 0.50, 0.55 and 0.62 (Percival et al. 2014, arXiv:1312.4841) [src: Sect. 6.1, Table of areas].

**Mitigation.** In order of preference: (i) the frequentist-matching t-distribution posterior of Percival et al. 2022 (arXiv:2108.10402), or its Gaussian approximation with `S'`; (ii) Hartlap factor on the precision plus the Percival 2014 `m_1` rescaling of the parameter covariance; (iii) the Sellentin–Heavens t-distribution (arXiv:1511.05969), which marginalises over `Σ` but does not include the best-fit scatter term. Reduce `n_d` (compression, §3 of `physics-and-methods.md`), use an analytic or semi-analytic covariance, or denoise (shrinkage, arXiv:0711.2509; RIE, arXiv:2604.13851).

**Validation.** Fit the mocks that were not used for the covariance and compare the scatter of best fits with the mean quoted error; check that `χ²` of the mocks follows the expected distribution (KiDS-1000 revised the effective number of degrees of freedom on this basis, arXiv:2007.01844).

**Traps.** Applying the Hartlap factor alone and calling the covariance "corrected". Applying the Hartlap factor to an analytic covariance (it has no Wishart noise). Applying the corrections when the mocks are not independent (fixed-amplitude or paired simulations, or mocks sharing initial conditions). Using the Gaussian form for a tension statement in the tails, where the t-distribution differs most (arXiv:2108.10402). Denoised covariances can return error bars that are too small in configuration space (arXiv:2604.13851).

**Cite.** arXiv:astro-ph/0608064, arXiv:1304.2593, arXiv:1212.4359, arXiv:1312.4841, arXiv:1511.05969, arXiv:2108.10402.

## 2. Jackknife and internal covariance estimates
<!-- key: jackknife-and-internal-covariance-estimates -->

**Mechanism.** Jackknife regions are not independent realisations: pairs straddle region boundaries, modes larger than a region are not sampled, and the number of regions bounds the rank of the matrix.

**Size.** Bootstrap overestimates the variance of ξ(s) by about 40% on 1–25 Mpc/h; the jackknife is correct on large scales and too large on small scales; an internal 2σ interval can correspond to anything from 1σ to 3σ (Norberg et al. 2009, arXiv:0810.1885) [src]. For cosmic shear the internally estimated uncertainty on the S8-like combination is about 90% of the truth (Friedrich et al. 2016, arXiv:1508.00895) [src].

**Mitigation.** The pair-weighting corrections of Mohammad & Percival 2022 (arXiv:2109.07071), which recover the covariance to the 10% precision of their test; or use the jackknife only to calibrate a model covariance, as RascalC does for the shot-noise rescaling (arXiv:1904.11070).

**Validation.** Compare with mocks on the diagonal and on the leading principal components; vary the number of regions (64 against 125 in arXiv:2109.07071 changes the structure of the matrix, not its amplitude).

**Traps.** A jackknife covariance does not contain super-sample covariance. The Hartlap correction with `n_s` set to the number of jackknife regions assumes independence that the regions do not have.

**Cite.** arXiv:0810.1885, arXiv:1508.00895, arXiv:2109.07071.

## 3. Analytic covariance: missing terms and cosmology dependence
<!-- key: analytic-covariance-missing-terms-and-cosmology -->

**Mechanism.** An analytic covariance is noise-free but only as good as its ingredients: the Gaussian term needs the survey geometry (the `f_sky` approximation fails for complex masks), the connected term needs a trispectrum model, the super-sample term needs the mask's large-scale variance (Takada & Hu 2013, arXiv:1302.6994), and the whole matrix is evaluated at one fiducial cosmology and one set of nuisance parameters.

**Size.** DES Y3: the `f_sky` approximation raises the χ² between maximum-posterior model and data by 3.7% on average (Δχ² ≈ 18.9); not knowing the parameters at which to evaluate the covariance is the dominant effect on parameters, increasing the scatter of the maximum posterior by about 3% for Ω_m and σ8 and 5% for w (Friedrich et al. 2021, arXiv:2012.08568) [src]. DESI 2024: the analytic Fourier-space covariance "does not reproduce the expected measurements" for full shape, while the configuration-space one is adequate for BAO (arXiv:2411.12027) [src]. In the DR1 full-shape paper (arXiv:2411.12021): EZmock and analytic covariances agree on mocks without fibre assignment, but with realistic fibre assignment they differ by ~20% in Fourier space; the RascalC matrix tuned on the data has larger elements than the EZmock one, so EZmocks "underestimat[e] ... the error bars" and every element of the 1000-EZmock covariance is rescaled by a tracer-dependent factor from RascalC over 20 < s < 200 h^-1 Mpc [src: Sect. 5.7]; the Hartlap factor (7 nuisance parameters assumed) and the Percival 2014 factor are applied on top and are "less than the rescaling factor", which is why a Gaussian likelihood is kept rather than the Sellentin–Heavens form [src: Sect. 5.8, Eq. 15]. The mock-realism correction is larger than the finite-mock correction.

**Mitigation.** Iterate the covariance at the best fit; calibrate the non-Gaussian part on the data (RascalC) or on a small mock set; use mocks where observational systematics (fibre assignment, imaging weights) shape the covariance.

**Validation.** Mock-to-analytic comparison of the diagonal, of the χ² distribution of mocks, and of the recovered parameter errors on the same data vector.

**Cite.** arXiv:1302.6994, arXiv:2012.08568, arXiv:2411.12027, arXiv:1904.11070.

## 4. Non-Gaussian likelihood treated as Gaussian
<!-- key: non-gaussian-likelihood-treated-as-gaussian -->

**Mechanism.** Two-point estimators of a Gaussian field follow a Wishart (scaled χ²) distribution, which is skewed when few modes contribute; non-linear evolution, masks and counts-like statistics add further non-Gaussianity. A Gaussian with the right mean and covariance then has the wrong mode and the wrong tails.

**Size.** fσ8 shifts by −0.44σ in the BOSS power-spectrum multipole analysis; for the group multiplicity function, posteriors of two HOD parameters shift by +0.43σ and −0.51σ and broaden by 42% and 66% (Hahn et al. 2019, arXiv:1803.06348) [src]. For CFHTLenS ξ± the skewness of the sampling distribution makes a low lensing amplitude "intrinsically likely" (Sellentin & Heavens 2018, arXiv:1707.04488) [src]. For 100 deg² shear mocks no significant bias on Ω_m and σ8 (Lin et al. 2020, arXiv:1905.03779) [src]; for Stage-IV pseudo-C_ℓ the Gaussian form is sufficient (Upham et al. 2021, arXiv:2012.06267) [src].

**Mitigation.** Exact or approximate non-Gaussian likelihood at low multipoles (Hamimeche & Lewis 2008, arXiv:0801.0554; pixel-based below ℓ ≈ 30); remove or compress the most non-Gaussian data points; Gaussianising transforms; likelihood estimated from mocks (Gaussian mixtures, independent component analysis in arXiv:1803.06348) or neural likelihood estimation (§12 of `physics-and-methods.md`).

**Validation.** Test the one-point distributions and pairwise dependence of the mock data vectors (the diagnostics of arXiv:1707.04488); compare the χ² distribution of mocks with the expected one.

**Related trap.** Letting the covariance vary with parameters inside a Gaussian likelihood adds artificial information (Carron 2013, arXiv:1204.4724); the measured effect of keeping it fixed is at most O(10%) of the statistical error (Kodwani et al. 2019, arXiv:1811.11584) [src].

**Cite.** arXiv:0801.0554, arXiv:1204.4724, arXiv:1707.04488, arXiv:1803.06348, arXiv:2012.06267.

## 5. Projection (prior-volume) effects
<!-- key: projection-prior-volume-effects -->

**Mechanism.** Marginalising over weakly constrained nuisance parameters weights each value of the parameter of interest by the volume of nuisance space compatible with it (`physics-and-methods.md` §6.1). The marginal mean moves away from the best fit without any change in goodness of fit.

**Size.** Up to 1σ and 2σ in BOSS EFT fits depending on the prior family (arXiv:2208.05929); up to 1.6σ in eBOSS (arXiv:2309.04468); 2.1σ to 6.6σ in DESI DR1 full shape + BAO under w0waCDM, below 1σ in ΛCDM (arXiv:2508.11811); 0.011 in S8 for DES Y3 + KiDS-1000 (0.790 against 0.801, arXiv:2305.17173) [src for all]. It grows with model freedom and shrinks with data volume or with an external data set that breaks the degeneracy: CMB (arXiv:2208.05929), supernovae (arXiv:2508.11811).

**Mitigation.** Quote MAP and mean; informative priors from HOD mocks (arXiv:2409.12937, arXiv:2402.13310); reparameterisation or Jeffreys prior (arXiv:2509.09562, arXiv:2607.02498); Mpc units for nuisance priors (arXiv:2610.08751); profile likelihood as cross-check (arXiv:2309.04468).

**Collaboration practice.** DES Y6 agreed before unblinding to run a noiseless data vector at the MAP through the data pipeline, and that "parameters showing prior-volume effects larger than 1σ ... should be presented with caveats and would not be highlighted as key results"; the measured pulls are below 0.5σ for the fiducial ΛCDM analysis and reach 0.83σ in S8 for wCDM with non-linear bias (arXiv:2601.14559) [src]. Both DES Y6 and KiDS-Legacy show the MAP with a projected joint highest-posterior-density interval next to the marginal (arXiv:2601.14559, arXiv:2503.19441). DESI DR1 full shape (arXiv:2411.12021) separates a prior weight effect (MAP pulled by the location and width of a prior) from the prior volume effect (mean against MAP), reports the MAP with every marginal constraint, and sets its nuisance priors on the mean of 25 Abacus DR1 mocks and noiseless data: counterterm priors of 50% of the linear signal at `k_max = 0.20 h/Mpc` (width 12.5 h^-2 Mpc²), with 20% giving the same constraints and 500% or flat priors "much stronger" projection; with 25 times the DR1 volume both effects nearly vanish; the hexadecapole was dropped because its poorly constrained nuisance parameters add projection; w0waCDM is considered only with external data for the same reason [src: Sects. 4.5–4.5.2].

**Validation.** Noiseless synthetic data vector at known cosmology through the full pipeline, for every model that is fitted, not only ΛCDM. The test must be repeated for each data combination because the effect depends on what breaks the degeneracies.

**Traps.** Reading a shift of the posterior mean as a preference of the data. Comparing the mean of one analysis with the best fit of another. Validating priors in ΛCDM and then fitting w0waCDM. Declaring a tension between a full-shape posterior and Planck that disappears in the profile likelihood (arXiv:2309.04468; arXiv:2208.05929 argue on this basis that the BOSS σ8 is not in tension with Planck).

**Cite.** arXiv:2208.05929, arXiv:2309.04468, arXiv:2508.11811, arXiv:2007.01844, arXiv:2203.16285.

## 6. Parameter boundaries and one-sided limits
<!-- key: parameter-boundaries-and-one-sided-limits -->

**Mechanism.** When the likelihood peaks at or beyond a physical boundary (Σm_ν ≥ 0, r ≥ 0, a fraction in [0, 1]), a Bayesian posterior truncated at the boundary gives an upper limit that tightens as the peak moves further into the unphysical region; the width of the truncated posterior is not the sensitivity of the experiment. On the frequentist side, the graphical `Δχ²` reading loses coverage near a boundary, and choosing between a limit and an interval after seeing the data ("flip-flopping") also breaks coverage (Feldman & Cousins 1998, arXiv:physics/9711021).

**Size.** DESI DR2 BAO + CMB in ΛCDM: Bayesian Σm_ν < 0.0642 eV with a marginalised σ of 0.020 eV, Feldman–Cousins limit 0.053 eV, both below the oscillation minimum (arXiv:2503.14744) [src]. Planck 2013: CMB-only profile minimum "well within the unphysical negative-mass region" (arXiv:1311.1657) [src].

**Mitigation.** Report a boundary-free statement next to the limit: a Feldman–Cousins interval, the profile extrapolated across the boundary, or an effective parameter allowed to go negative (arXiv:2503.14744). State the expected limit (sensitivity) for the true value at the boundary.

**Validation.** Coverage test with simulated data at several true values near the boundary; check of the Wilks assumptions as in arXiv:2408.07700, which finds the neutrino-mass case "consistent with a Gaussian near a boundary".

**Traps.** Quoting the truncated-posterior σ as the sensitivity. Comparing a 95% Bayesian limit of one experiment with a 90% CL frequentist limit of another. In Feldman–Cousins mock fits, fixing parameters that were free in the data fit underestimates the interval (arXiv:2508.10633).

**Cite.** arXiv:physics/9711021, arXiv:1311.1657, arXiv:2408.07700, arXiv:2503.14744. Physics in `cosmo-neutrinos-dark-matter`.

## 7. Informative priors and prior-dependent evidence
<!-- key: informative-priors-and-prior-dependent-evidence -->

**Mechanism.** The evidence is the likelihood averaged over the prior, so it scales inversely with the prior volume of any parameter the data constrain. The Bayes ratio used as a tension metric scales the other way: "doubling the prior volume doubles the value of R" (Lemos et al. 2021, arXiv:2012.09554) [src]. A flat prior chosen "wide enough not to matter" for parameter estimation always matters for the evidence.

**Size.** For DESI DR2 BAO + Planck, the `w0`, `wa` prior turns a 3.1σ preference in `Δχ²` into `ln B = −0.57 ± 0.26` (Ong et al. 2025, arXiv:2511.10631) [src]. Two Gaussians 3σ apart go from `R << 1` to `R > 1` when the flat prior widens from [−10, 10] to [−200, 200] (arXiv:2012.09554) [src].

**Mitigation.** State the prior ranges of the extra parameters with every Bayes factor; show the Bayes factor for a second, physically motivated prior; use prior-insensitive companions (suspiciousness for tension, arXiv:1902.04029; `Δχ²`, information criteria or an out-of-sample score for model comparison, arXiv:2609.04334).

**Validation.** Recompute the evidence with the prior width halved and doubled; the change of `ln B` should be the logarithm of the volume ratio if the posterior is inside the prior.

**Other prior traps.** Posteriors cut off by the prior: for DESI BAO alone "the posteriors in this poorly constrained case are cut off by the priors, so the marginalized means and limits quoted above are prior-dependent" (arXiv:2503.14738) [src]. A flat prior in one parameterisation is informative in another (flat in `ln 10^10 A_s` against flat in σ8; flat in Σm_ν against flat in the lightest mass). Priors on derived parameters induced by flat priors on sampled ones.

**Cite.** arXiv:0803.4089, arXiv:0802.3185, arXiv:1902.04029, arXiv:2012.09554.

## 8. Delta chi2 converted to sigma outside its range of validity
<!-- key: delta-chi2-converted-to-sigma-outside-its-range -->

**Mechanism.** The conversion of a `Δχ²` between nested models into "nσ" uses Wilks' theorem: under the simpler model, `Δχ²` follows a χ² distribution with as many degrees of freedom as extra parameters. It requires Gaussian asymptotics, the null model inside the parameter space of the alternative, and no parameter that is unidentified under the null.

**Where it fails.** (i) Boundaries: a prior edge such as `wa > −3` or `w0 < 1` that the fit reaches; DESI notes that the DESI + compressed-CMB posterior "is still bounded by the `wa > −3` prior at the lower end" (arXiv:2503.14738) [src]. (ii) Non-Gaussian likelihoods: the profile-likelihood test of Herold et al. 2024 (arXiv:2408.07700) finds "indication of a violation of the assumptions" already for w0CDM with Planck [src]. (iii) Wrong number of degrees of freedom: `sqrt(Δχ²)` is correct for one extra parameter only. (iv) A posteriori model choice: the model was proposed after seeing the data, or is the best of several tried (§15). (v) The `Δχ²` is dominated by a conflict between two data sets rather than by a coherent signal (arXiv:2511.10631).

**Size.** For two extra parameters, 3σ needs `Δχ² = 11.83`, not 9; quoting `sqrt(12.5) = 3.5σ` for DESI + CMB instead of 3.1σ would be an error of 0.4σ `[der]`.

**Mitigation and validation.** Calibrate the `Δχ²` distribution on mocks generated under the null model with the full pipeline (the only route when Wilks' conditions are in doubt); quote `Δχ²`, the number of extra parameters and the p-value explicitly; add an information criterion and, with its prior, a Bayes factor.

**Cite.** arXiv:2503.14738 for the practice, arXiv:2408.07700 for the conditions.

## 9. Tension metric chosen after the fact, or misapplied to correlated data
<!-- key: tension-metric-chosen-after-the-fact-or -->

**Mechanism.** There are many metrics and many reference data sets; choosing among them after seeing the result selects the largest or the smallest figure. Separately, most metrics assume independent data sets and Gaussian posteriors.

**Size.** On the same posteriors, DES Y6 3×2pt against the CMB is 1.8σ in the full parameter space and 2.6σ projected on S8 (arXiv:2601.14559) [src]. Choosing the most discrepant or the most concordant LSS combination against Planck 2015 gave 2.55σ or 0.76σ (Charnock et al. 2017, arXiv:1703.05959) [src]. The Bayes ratio can change sign with the prior width (arXiv:2012.09554) [src]. Non-Gaussian estimators are accurate to 0.2σ in general and 0.5σ in difficult cases (arXiv:2105.03324) [src], which bounds how many digits a tension deserves.

**Mitigation.** Fix the metric, the parameter subspace and the reference data set before unblinding; the DES suite of arXiv:2012.09554 was assembled before the Year 3 data for that purpose ("a toolset for robustly testing tensions in the DES Year 3 data and beyond"). Report a full-space metric and the projected one. For correlated data use the update form `Q_UDM` (arXiv:1806.04649) or a posterior predictive test (arXiv:2011.03410, arXiv:2610.03447).

**Validation.** Inject a known shift in synthetic data and check that the metric responds as expected, as done in arXiv:2012.09554 and arXiv:2610.03447.

**Known failure of posterior predictive tests** (Doux et al. 2026, arXiv:2610.03447) [src]: internal tensions that nuisance parameters can absorb become harder to detect, and "poorly constrained directions in parameter space can induce projection effects in PPDs for disjoint sets of observables, producing reports of tension even for consistent data".

**Traps.** Adding the errors in quadrature for data sets that share sky, calibration or a prior. Using the Hartlap-corrected Gaussian in the tails (§1). Combining data sets in a model in which they are in tension and then reading the combined posterior as evidence for an extension that relieves it (arXiv:2511.10631).

**Cite.** arXiv:1806.04649, arXiv:1902.04029, arXiv:2012.09554, arXiv:2105.03324.

## 10. Unconverged or biased sampling
<!-- key: unconverged-or-biased-sampling -->

**Mechanism.** A chain that has not mixed, a nested-sampling run with too few live points or too short slice chains, or a proposal that misses a mode, gives intervals that are too narrow and an evidence that is wrong, without any error message.

**Size.** On the DES Y1 likelihood, MultiNest returned "inconsistent estimates of the Bayesian evidence and somewhat narrower parameter credible intervals" than PolyChord (Lemos et al. 2023, arXiv:2202.08233) [src]. The classical `R̂` fails for heavy tails or chains of unequal variance (Vehtari et al. 2021, arXiv:1903.08008) [src].

**Mitigation.** Several independent chains from dispersed starts; `R − 1 < 0.01` and an effective sample size of order 10^3 (the DESI criterion, arXiv:2503.14738); rank-normalised `R̂` and tail effective sample size when limits are quoted; for evidences, repeat the run and quote the scatter, and cross-check with a second algorithm; for tails beyond 2σ, more samples than for the 68% interval.

**Validation.** Run the sampler on a fast surrogate likelihood with a known answer, as arXiv:2202.08233 did; compare two samplers on the final likelihood.

**Traps.** Reading the best `χ²` from the chain instead of running a minimiser. Importance-reweighting a chain towards a posterior that lies in its tail. Quoting a Bayes factor error from a single nested-sampling run. Gradient-based samplers on a likelihood whose emulator has noisy derivatives.

**Cite.** arXiv:2202.08233, arXiv:1903.08008, arXiv:1111.4246.

## 11. Emulator error and extrapolation
<!-- key: emulator-error-and-extrapolation -->

**Mechanism.** The emulator prediction differs from the exact calculation by an interpolation error that varies with scale, redshift and position in parameter space, and grows towards the edge of the training design. If the error is not in the likelihood, it biases parameters; if the sampler leaves the design, the prediction is an extrapolation. For simulation emulators the training simulations add their own error.

**Size.** Stated interpolation accuracies: below 0.4% for a Boltzmann-code emulator (arXiv:2106.03846), 1% for a non-linear N-body emulator to k = 10 h/Mpc (arXiv:2010.11288) [src]. KiDS-Legacy's retrained CosmoPower emulator of CAMB + HMCode2020 (450 000 training, 50 000 test spectra, Latin hypercube over a seven-parameter box that defines its validity, k from 10^-5 to 20 h/Mpc) has a maximal error below 0.1% for 68% of test samples; for comparison the paper places HMCode2020 itself at the ~2.5% accuracy level of simulation emulators, so the emulator error is small against the model error, not only against the data (arXiv:2503.19441) [src: Appendix A, Sect. 2.2]. On Euclid-like mocks an explicit Gaussian likelihood became "strongly miscalibrated under emulation inaccuracies" (Vinciguerra et al. 2026, arXiv:2607.17942) [src]: an error that looks small per data point is coherent across the data vector.

**Mitigation.** Emulator covariance added to the data covariance, with its correlations; Bayesian propagation of the validation errors (Grandón & Sellentin 2022, arXiv:2205.11587); priors no wider than the training design; a final chain, or an importance-reweighting, with the exact code.

**Validation.** Held-out test set reported as a function of k, z and parameters, not as one number; a posterior comparison against the exact code on the real data vector (as arXiv:2106.03846 does for KiDS and Planck); a blind test on an independent simulation (the Flagship test of arXiv:2010.11288).

**Traps.** Quoting the median error where the 99th percentile matters. Using an emulator trained in ΛCDM for an extended model, or outside its neutrino-mass or `w0`–`wa` range. Treating the accuracy against dark-matter-only simulations as the accuracy of the model. Posteriors that pile up against the edge of the training box.

**Cite.** arXiv:2106.03846, arXiv:2010.11288, arXiv:2205.11587.

## 12. Simulation-based inference: overconfidence and model misspecification
<!-- key: simulation-based-inference-overconfidence-and -->

**Mechanism.** The learned density is an approximation trained on a finite set of simulations from an imperfect simulator. Three separate failures: the density estimator is wrong although the simulator is right (too few simulations, poor training); the estimator is right on average but wrong at the parameter value of interest; the simulator cannot produce the observed data (misspecification).

**Size.** All benchmarked algorithms can be overconfident (Hermans et al. 2022, arXiv:2110.06581) [src]. The variance inflation from a finite simulation budget is at least the Dodelson–Schneider one (Homer et al. 2024, arXiv:2412.02311) [src]. Posteriors can pass coverage and still be underconfident with wrong tails (Alokda et al. 2026, arXiv:2605.00980) [src]. In the body of that paper, 1000 halo realisations at `f_NL = 0`: the conditional coverage at fixed truth is 0.58 to 0.62 at 68% and 0.91 to 0.96 at 95% for ratio estimation, against 0.70 to 0.73 and 0.97 to 0.99 for the likelihood analysis [src: Table 2]; the joint P + B constraint is tighter than both single-statistic ones in 84.3% of realisations for the likelihood analysis and in only 6.7% for ratio estimation, a failure "not captured by coverage-based diagnostics" [src: Sect. 4.3.2]. Coverage at fixed parameter need not equal the nominal level even for an exact posterior; it does under probability-matching priors, Bernstein–von Mises asymptotics, or approximately Gaussian posteriors [src: Sect. 4.2.2]. Hermans et al. 2022 found non-conservative estimators for every algorithm on at least one benchmark, for budgets up to 2^17 simulations [src: Sects. 3.3–3.4]. In KiDS-SBI, omitting variable depth and PSF anisotropy from the simulator biases S8 by about 5% (arXiv:2404.15402) [src].

**Mitigation.** Ensembles of density estimators; more simulations than the covariance-based intuition suggests; simulators that include every observational systematic with its prior; summaries restricted to those that are stable across simulators; training designs padded beyond the prior box.

**Validation, in the order a referee should ask.** (1) Coverage on held-out simulations (simulation-based calibration, arXiv:1804.06788; TARP, arXiv:2302.03026). (2) A test at fixed parameter values near the result, since coverage is a prior average (arXiv:2605.00980). (3) Comparison with a likelihood analysis on a statistic for which the likelihood is known (arXiv:2404.15402). (4) Out-of-distribution and goodness-of-fit tests of the observed summaries. (5) Robustness of the result to a second simulator or galaxy–halo model. (6) Number of simulations against the dimension of the summary vector.

**Traps.** A coverage plot presented as full validation. A limit that sits at the edge of the training prior read as a measurement (the `w` example in `cosmo-beyond-two-point`). Gains quoted against a two-point analysis that used a different likelihood, different scales or a different covariance.

**Cite.** arXiv:1903.00007, arXiv:1804.06788, arXiv:2110.06581, arXiv:2302.03026, arXiv:2412.02311.

## 13. Fisher forecasts beyond their validity
<!-- key: fisher-forecasts-beyond-their-validity -->

**Mechanism.** The Fisher matrix is the curvature of the log-likelihood at the fiducial point. It returns ellipses whatever the true posterior looks like, has no prior-volume term, and inherits every instability of the numerical derivatives.

**Size.** Marginalised errors on `w0`, `wa` from geometrical probes underestimated by 30%–70% against MCMC; 5% level for weak lensing (Wolz et al. 2012, arXiv:1205.3984) [src]. Independent Euclid forecast codes agreed only after a dedicated comparison and correction campaign (arXiv:1910.09273) [src].

**Mitigation.** Validate the forecast against a sampled posterior on a synthetic data vector for at least the extended model of interest; check derivative stability against step size; use a higher-order expansion or sample when the degeneracy is curved; state the nuisance model, priors and scale cuts with every forecast number.

**Validation.** Two independent codes on the same specification (the method of arXiv:1910.09273).

**Traps.** Comparing a Fisher forecast with an achieved posterior and calling the difference "underperformance": projection effects and non-Gaussian degeneracies are absent from the forecast. Quoting a Fisher gain for a new statistic computed on the matter field as a survey forecast (the examples are in `cosmo-beyond-two-point`). Using a Gaussian-likelihood Fisher matrix with the covariance-derivative term for two-point statistics (Carron 2013, arXiv:1204.4724). Labelling a forecast as a constraint.

**Cite.** arXiv:astro-ph/9603021, arXiv:1205.3984, arXiv:1910.09273.

## 14. Double counting and neglected cross-covariance when combining probes
<!-- key: double-counting-and-neglected-cross-covariance -->

**Mechanism.** Multiplying likelihoods assumes independence. Shared sky area, shared galaxies, shared calibrators, a shared prior, or two releases of the same survey violate it; the combined error is then too small and any tension between the two is misjudged.

**Size.** Case-dependent. For pre-reconstruction full shape with post-reconstruction BAO of the same galaxies, the cross-covariance is small enough that an analytic approximation leaves parameter constraints "virtually unchanged" (Maus et al. 2026, arXiv:2602.12343) [src]: here the correlation is real but weak. For 3×2pt the cross terms between probes are a leading part of the covariance and cannot be dropped (arXiv:2012.08568). For overlapping lensing surveys a joint analysis was required (arXiv:2305.17173).

**Mitigation.** Joint covariance from common mocks or an analytic cross term; a single application of each external prior; one release per survey; for compilations, a list of shared objects. Consistency under the combining model before combination (§9).

**Validation.** Fit the mocks jointly and compare the scatter of best fits with the quoted joint error; drop one data set at a time and check that shifts are within the expectation for nested data (the update form of the parameter difference, arXiv:1806.04649).

**Traps.** Counting DR1 and DR2 of DESI, or DESI and SDSS bins at the same redshift, as independent. Counting several supernova compilations as independent confirmations. Importance-reweighting or multiplying posteriors of data sets that share nuisance parameters. Combining data sets that are discrepant in ΛCDM and reading the resulting preference for an extension as a detection (arXiv:2511.10631).

**Cite.** arXiv:2012.08568, arXiv:2305.17173, arXiv:2602.12343.

## 15. Look-elsewhere effect and a posteriori statistics
<!-- key: look-elsewhere-effect-and-a-posteriori -->

**Mechanism.** A local significance is computed as if the test had been specified before the data were seen. When the feature, the bin, the model, the data combination or the statistic was chosen because it showed something, the probability of an equally striking result somewhere in the space of choices is larger by the trial factor (Gross & Vitells 2010, arXiv:1005.1891).

**Size.** For `N` independent looks, `p_global ≈ N p_local`: a 3σ local excess (p = 2.7e-3) among 20 independent looks has a global p of about 5%, that is 1.9σ `[der]`. Bayer & Seljak 2020 (arXiv:2007.13821) show that the trial factor is the prior-to-posterior volume ratio of the searched parameter [src], so a narrow feature searched over a wide range pays a large factor. In practice the documented cosmological cases are spreads between equally defensible choices (`results.md` §11).

**Mitigation.** Blinding with frozen analysis choices; a single pre-declared headline combination, with the others labelled as variations; simulation of the full search under the null (the mock-based calibration of the phantom-crossing preference and of the parity-odd signal, described in the sibling skills, are examples); for model scans, the global p-value or a Bayes factor with a stated prior on the searched parameter.

**Validation.** Ask how many models, cuts and data combinations were tried, and whether the reported one was fixed before unblinding.

**Traps.** "The preference grows to 4.2σ with data set X" when three data sets were tried. A new model fitted to the same data that showed the anomaly, reported with a fresh `Δχ²`. An a posteriori statistic built to maximise a feature seen in the data (the usual objection to CMB large-angle anomalies; see `cosmo-tensions-anomalies`).

**Cite.** arXiv:1005.1891, arXiv:2007.13821.

## 16. Unblinding leaks and post-unblinding changes
<!-- key: unblinding-leaks-and-post-unblinding-changes -->

**Mechanism.** Confirmation bias acts through analysis choices made while seeing the result: scale cuts, priors, which systematic test to add, when to stop looking for errors. Blinding removes the result from view; it fails when the blinding can be undone, when it is lifted before the choices are frozen, or when choices change afterwards.

**Leak routes.** Statistics that the scheme does not alter (a catalogue-level Alcock–Paczynski shift leaves angular clustering unchanged by design, arXiv:2006.10857); comparison of blinded and unblinded intermediate products; a blinding shift smaller than the statistical error; for the Lyα forest, contaminant lines that respond differently to the shift (arXiv:2607.07875); extended-model fits run before the baseline is unblinded.

**Mitigation.** A scheme validated on mocks and on the data themselves with a second blinding layer (arXiv:2404.07282); encryption of the true data vector (arXiv:2604.18111); a written unblinding checklist; a section in the paper listing every change made after unblinding and its effect on the result.

**Validation.** The analysis choices tuned on blinded data must be shown to be unchanged after unblinding (arXiv:2404.07282), and the internal-consistency statistics must be preserved by the blinding transformation (arXiv:1911.05929).

**Size of a catalogue-level shift.** DESI DR1 drew the blind (w0, wa) so that `abs(α_⊥ − 1)` and `abs(α_∥ − 1)` stay below 3% over 0.4 < z < 2.1, with f changed by at most 10% of 0.8 and f_NL = ±20, "roughly based on the precision of such measurements before DESI DR1"; one pair among 1000 random ones was used for all tracers, unknown even to the blinding team (arXiv:2404.07282) [src: Sect. 3.3]. On 16 blinded Abacus catalogues the residual of the expected shift, `Γ_α_iso`, stayed within 0.8% of unity for an error of about 1.3% per case [src: Table 3].

**Documented cases.** DES Y6: at the last blinding stage several posterior predictive tests failed and one lens-bin redshift parameter pushed against its prior; the bin was dropped under a pre-written plan, after "three iterations of blind inference" (arXiv:2601.14559) [src]. ACT DR6: a pre-unblinding requirement (parameter recovery on a realistic non-Gaussian simulation) was not met, with 3σ shifts traced to foreground complexity in the simulation; the plan was amended in writing, with a 0.5σ threshold for adding foreground parameters, and the test was passed after unblinding (arXiv:2503.14452) [src]. KiDS-Legacy: the three-catalogue scheme "effectively hampered the diagnosis of subtle systematic effects", because comparing shape catalogues with earlier releases would unblind (arXiv:2503.19441) [src]. Blinding has a cost, and the honest papers state it.

**Traps for a referee.** "Blinded" can mean the catalogue, the data vector, the parameters, or only the comparison with external data: ask which. A blind test on a mock (a challenge) is not a blind analysis of data (see `cosmo-beyond-two-point`). Re-analyses of public data cannot be blind to the published result.

**Cite.** arXiv:1911.05929, arXiv:2006.10857, arXiv:2404.07282, arXiv:1910.08533.

## 17. What a referee checks in a results section
<!-- key: what-a-referee-checks-in-a-results-section -->

Covariance and likelihood

1. Source of the covariance (mocks, jackknife, analytic, hybrid); number of mocks against the length of the data vector; which correction was applied, and whether it covers both the bias of the precision and the scatter of the best fit (§1).
2. For an analytic covariance: geometry treatment, non-Gaussian and super-sample terms, the cosmology at which it was evaluated, whether it was iterated (§3).
3. Likelihood form, and a test of it on mocks where few modes or counts enter (§4).
4. Goodness of fit with the effective number of degrees of freedom stated.

Priors and point estimates

5. Prior ranges of every sampled parameter; which posteriors touch a prior edge.
6. Mean, MAP or mode: which is quoted, and the size of the projection effect measured on a synthetic data vector in each model fitted (§5).
7. For a limit: the confidence or credible level, the treatment of the boundary, and the expected sensitivity (§6).

Sampling

8. Sampler, settings, convergence criterion; how the best fit was found (§10).
9. For an evidence: repeated runs, a second algorithm, and the prior volume (§7).

Significance and comparison

10. For "nσ" from a `Δχ²`: the value, the number of extra parameters, and whether Wilks' conditions hold (§8).
11. For a Bayes factor: priors on the extra parameters, and the companion `Δχ²` (§7).
12. For a tension: the metric, the parameter subspace, the reference data set, and whether these were fixed before unblinding (§9).
13. Number of models, cuts and data combinations tried (§15).

Combination

14. Independence of the combined data sets, or the cross-covariance; priors applied once; consistency under the model used for the combination (§14).

Surrogates and simulations

15. Emulator accuracy as a function of scale and parameters, the training range against the prior range, and how the error enters the likelihood (§11).
16. For simulation-based inference: coverage, a fixed-parameter test, an out-of-distribution test, the number of simulations, and a second simulator (§12).
17. A forecast labelled as such, with its nuisance model and scale cuts (§13).

Blinding

18. Level of blinding, the unblinding criteria, and the list of post-unblinding changes with their effect (§16).

## Not verified
<!-- key: not-verified -->

- Non-independent mocks: only the overlapping-box case of BOSS (arXiv:1312.4841, Sect. 6.1) was read; no paper on fixed-amplitude, paired or shared-initial-condition mocks and the Hartlap and Dodelson–Schneider corrections was read.
- The statement in §2 that a jackknife covariance lacks super-sample covariance is the standard argument and was not read in a cited paper this session.
- No documented case of an accidental unblinding in a survey analysis was collected.
- The size of the bias from gradient-based sampling with a noisy emulator (§10, traps) is not quantified here.
- The prior-reparameterisation examples in §7 (flat in `ln A_s` against σ8, flat in Σm_ν against the lightest mass) are generic illustrations without a paper read for their size; the neutrino case is treated in `cosmo-neutrinos-dark-matter`.
