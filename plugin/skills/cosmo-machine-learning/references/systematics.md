# Machine learning in cosmology — systematics

Scope: the failure modes specific to machine-learning methods in cosmology: simulator dependence, misspecification, out-of-distribution inputs, training-set size, emulator error, overconfidence, reproducibility.
Snapshot: 2026-10-22

Flags: as in `physics-and-methods.md`.

## 1. Simulator dependence
<!-- key: simulator-dependence -->

**Mechanism.** A network trained on one simulator learns that simulator's
mapping from parameters to data, including features that other codes, or
the Universe, do not share: sub-grid feedback, unconverged small-scale halo
properties, galaxy-finder choices. Applied to data from another simulator
it can be biased and overconfident at once.

**Size, where measured.** Most published tests use the CAMELS suites (one
box size, one set of codes); the rows after the CAMELS block below test
other N-body codes, other hydrodynamic runs (Magneticum, EAGLE, BAHAMAS)
and real data.

| Test | Outcome | Reference |
|---|---|---|
| Lyα P1D NPE on CAMELS, train on one sub-grid model, test on the other | ~10% positive bias on σ8, worse precision; multi-domain training removes the bias | Sinigaglia et al. 2026, arXiv:2603.13011 [src: abstract] |
| GNN trained on IllustrisTNG galaxy catalogues, frozen, applied to CAMELS-CROCODILE | fails to recover Ω_m and σ8, overconfident, mainly for simulations with more galaxies than any training one; within the training range Ω_m error 1.5 times the in-distribution value. The network uses galaxy positions and line-of-sight velocities (linking length 2.15 h⁻¹Mpc), the input that earlier tests had found robust | arXiv:2609.23982 [src; inputs from Sect. IV.1] |
| Ω_m from the properties of one galaxy | ~10% precision within one model; "not robust to changes in subgrid physics" | Villaescusa-Navarro et al. 2022, arXiv:2201.02202 [src: abstract] |
| Same, tested on IllustrisTNG, SIMBA, Astrid and Magneticum | good on most galaxies, fails "dramatically" on a small fraction; removing outliers restores accuracy | Echeverri et al. 2023, arXiv:2304.06084 [src] |
| GNN on halo catalogues from Gadget, tested on Abacus, CUBEP³M, Enzo, PKDGrav3, Ramses | Ω_m and σ8 recovered (~6% mean relative error); adding concentration or V_max breaks robustness, probably because codes are not converged on those scales | Shao et al. 2023, arXiv:2209.06843 [src] |
| GNN on galaxy positions and radial velocities, tested on five hydrodynamic codes | Ω_m at ~12%, robust across IllustrisTNG, SIMBA, Astrid, Magneticum, SWIFT-EAGLE and subhalo finders | de Santi et al. 2023, arXiv:2302.14101 [src: abstract] |
| Same with masks, distance errors and selections | precision and accuracy degrade; the model still works on over 90% of catalogues | de Santi et al. 2023, arXiv:2310.15234 [src: abstract] |
| CNN on 2D total-mass maps, train TNG test SIMBA and vice versa | correct Ω_m and σ8 in all four combinations | arXiv:2109.10360 [src: Fig. 2] |
| SimBIG WST, 2000 test simulations with a changed forward model | robust for all parameters except σ8 at k_max = 0.5 h Mpc⁻¹; the data posteriors vary with the flow architecture | Régaldo-Saint Blancard et al. 2024, arXiv:2310.15250 [src: abstract] |
| Same, test sets read in the body | TEST0: 500 mocks, SimBIG forward model on 100 Quijote runs; TEST1: 500 mocks, friends-of-friends finder and a 6-parameter HOD instead of 9; TEST2: 1000 mocks on AbacusSummit with CompaSO at a slightly different cosmology. The distribution of (μ − θ)/σ agrees across sets for Ω_m, Ω_b, h, n_s; σ8 is inferred low on TEST2 and high on TEST1; discarding WST coefficients with j < 2 (k ≳ 0.3 h Mpc⁻¹) restores agreement without changing the other parameters. SBC shows underconfidence on Ω_m and σ8, and the ensemble removes a slight overconfidence of single models on Ω_b, h, n_s | arXiv:2310.15250 [src: Sect. III.1, Fig. 4, 6, 7] |
| Halo GNN, mean relative error by input (trained on Gadget) | Ω_m: 10.1% (positions), 17.4% (V only), 5.6% (positions + V), robust across N-body and hydrodynamic codes; σ8: 11.8% and 5.9% (with mass), robust only for haloes of ≳ 300 particles; Ω_m and σ8 with V, c, V_max: 2.7% and 2.2%, not robust. Not robust to redshift (trained at z = 0) or to a SUBFIND instead of Rockstar finder; robust to higher resolution. Training on many number densities per simulation was "a key ingredient" | arXiv:2209.06843 [src: Sect. IV.1.2, IV.3, Table 2] |
| Galaxy GNN trained on Astrid, positions + v_z, tested on IllustrisTNG, SIMBA, Magneticum, SWIFT-EAGLE, SB28 | in-suite RMSE 0.043, relative error 11.8%, χ² 1.65; across suites RMSE 0.015–0.047, relative error 4.0–13.1%, χ² 0.25–2.38; worst on SB28. Adding stellar mass: in-suite error 9.6%, across suites 10.7–20.7% and χ² up to 14.2. Models trained on IllustrisTNG or SIMBA extrapolated worse than the Astrid one | arXiv:2302.14101 [src: Sect. IV.1, IV.2] |
| Same CROCODILE test, numbers read in the body (201 L50 Sobol runs, SB35-trained GNN of Genel et al., frozen) | Ω_m RMSE 0.035 in distribution → 0.132 ± 0.019 (mean relative error 24%), σ8 0.093 → 0.124 ± 0.007; R² = −0.43 ± 0.43 and −0.21 ± 0.15; mean χ² 30 ± 8 and 25 ± 6 (truncated; 56 and 265 untruncated). 46 runs have more galaxies than any of the 1024 training graphs; without them the Ω_m RMSE is 0.053 but σ8 stays overconfident (χ² 22 ± 6). At fixed cosmology, raising the galaxy count from 5.1 × 10³ to 9.2 × 10³ moves σ8 from 0.74 to 0.89, about 2.5 predicted σ. The 27 fiducial CV runs are recovered and calibrated (χ² 1.1 and 1.4) | arXiv:2609.23982 [src: Sect. IV.2, Fig. 10] |
| Lyα P1D NPE, train IllustrisTNG, test SIMBA, k_max = 3 h Mpc⁻¹ | needs the mean flux rescaled first (the models differ by ~5–15% at z ≳ 3; without it the parameters are "severely biased"); then Ω_m roughly unbiased with larger scatter, σ8 biased high by ~10%, posteriors overconfident in coverage and TARP. Multi-domain training on 475 + 475 runs, tested on 25 + 25, recovers both parameters | arXiv:2603.13011 [src: Sect. IV.2, IV.3] |
| Field-level CNN on matter slices, trained on 1000 Gadget runs, tested on 50 each of Abacus, CUBEP³M, PKDGrav3, Ramses and CAMELS IllustrisTNG | non-AMR codes recovered (R² ~ 1; slightly larger σ8 error on Abacus); Ramses (AMR) above 20% error on Ω_m and σ8 (Ω_m high, σ8 low); tests at twice the resolution biased "in all cases"; the N-body-trained network is biased in σ8 on IllustrisTNG, no worse than on Ramses. A PQMass out-of-distribution test flags Abacus, CUBEP³M and PKDGrav3 although their inference is almost unbiased; smoothing brings the codes into agreement | Bayer et al. 2025, arXiv:2505.13620 [src: Table 1, Sect. III.3; abstract] |
| Cluster masses from X-ray profiles, trained on Magneticum, tested on IllustrisTNG | the network gains 17% on the training data and loses 40% on the test set; scatter augmentation does not help; a domain-adaptation network (DRRN) aligns the latent spaces but stays worse than the Y_X scaling relation | Ntampaka et al. 2025, arXiv:2510.09748 [src: abstract] |
| Halo masses from synthetic HSC-like galaxy images, IllustrisTNG, EAGLE and SIMBA, trained on one and tested on another | without domain adaptation biased and overconfident; MMD adaptation lowers the normalised residual β by 31% on average, up to 57% | Garuda et al. 2026, arXiv:2603.12380 [src: abstract] |
| SIDM cross-section from cluster images, BAHAMAS-SIDM and DARKSKIES | a latent-space clustering flags mock observations unlike either training suite, so their parameter estimates can be discarded | Tregidga et al. 2025, arXiv:2511.09660 [src] |
| SimBIG WST on BOSS, after discarding the coefficients inconsistent across TEST0/1/2 (TEST2 on AbacusSummit with CompaSO) and mapping the observation back into the training support | σ8 histograms consistent across the three test sets; Ω_m = 0.32 ± 0.02, σ8 = 0.80 ± 0.02, 1.4 and 3.1 times tighter than a perturbation-theory P(k) analysis | Pierre et al. 2025, arXiv:2507.03086 [src: Sect. II.2.3, II.2.4, Fig. 2; abstract] |

**Mitigation.** Train on several simulators (multi-domain training,
arXiv:2603.13011 [src]); unsupervised domain adaptation by maximum mean
discrepancy, up to 28% better relative error and almost an order of
magnitude better χ² across CAMELS suites (Roncoli et al. 2023,
arXiv:2311.01588 [src: abstract]); restrict inputs to quantities on which codes are
converged (arXiv:2209.06843 [src]); remove the scales that fail the
cross-simulator test (k ≳ 0.3 h Mpc⁻¹ for SimBIG WST, arXiv:2310.15250
[src]); self-supervised pre-training on a cheap simulator then a frozen
encoder (arXiv:2608.26354 [src]); outside CAMELS, MMD adaptation across
IllustrisTNG, EAGLE and SIMBA (arXiv:2603.12380 [src]), smoothing the
field until N-body codes agree (arXiv:2505.13620 [src]), and discarding
simulator-inconsistent summary components before a learned transform of
the observation (arXiv:2507.03086 [src]). Domain adaptation is not always
enough: from Magneticum to IllustrisTNG it stayed worse than a scaling
relation (arXiv:2510.09748 [src]).

**Validation.** Test on a simulator never seen in training, with its own
sub-grid model and finder, and report both bias and calibration there;
test at another resolution too (arXiv:2505.13620 [src: Sect. III.3]). A
field-level out-of-distribution metric can flag a test set whose inference
is nonetheless unbiased, so it is a conservative diagnostic, not a
substitute for the inference test (same, Sect. III.3).
The DES Y3 map-level design does this with Buzzard mocks, built from HOD
galaxy catalogues on a different N-body code, against CosmoGridV1
training mocks generated at the pixel level; Buzzard drives parameter
recovery, posterior predictive checks and the choice of scale cuts
(arXiv:2511.04681) [src: Sect. V.2, VI.1.1, VI.1.3]. Small scales where
linear bias or baryonification break down are removed, following the
standard DES strategy [src: Sect. III.6.1]. The Buzzard test combines
N = 15 mocks into one joint posterior and passes when its MAP lies within
0.5σ of the true (Ω_m, S8, w) in the two-dimensional marginals
[src: Sect. VI.1.1, Eq. 18]. The resulting smoothing scales are a comoving
8 h⁻¹Mpc for lensing (12.5 to 5.4 arcmin from the first to the fourth bin)
and 32 h⁻¹Mpc for clustering (55.3 to 24.2 arcmin) [src: Eq. 10]. Mocks
contaminated one effect at a time (CosmoGridV1 benchmark settings, no
baryonification, NLA amplitude per shell, ±2σ source-galaxy bias) must
shift the Ω_m–S8 posterior by less than 0.3σ from the fiducial MAP, the
DES Y3 criterion, measured on the mean summary of 80 realisations; all
passed [src: Sect. VI.1.2, Eq. 19].
Sibling skills record the data analyses that did this (`cosmo-beyond-two-point`).

## 2. Model misspecification and out-of-distribution data
<!-- key: model-misspecification-and-out-of-distribution -->

**Mechanism.** The observed data lie outside the support of the simulator
used for training. Neural posteriors then extrapolate silently: with
misspecification, naive NPE gives "misleading and erratic posteriors"
(Ward et al. 2022, arXiv:2210.06564) [src], and posterior errors grow with
the distance between the data and the typical set of simulations in the
learned summary space (Schmitt et al. 2023, arXiv:2112.08866) [src].

**Detection.** Maximum mean discrepancy between observed and simulated
summaries in the latent space (arXiv:2112.08866) [src]; goodness-of-fit of
the data under the learned likelihood, e.g. the KiDS-SBI χ² against 500
forward simulations at the MAP, PTE 0.42 (arXiv:2404.15402) [src: Sect. 5.4,
Fig. 13]; before unblinding the DES Y3 hybrid-statistics analysis checked
that the data summaries lie on the manifold of Gower Street mock summaries,
a test that needs no cosmology (Williamson et al. 2026, arXiv:2606.11309)
[src: Sect. 7.2, 7.4, Fig. 7]; Bayesian evidence per smoothing scale with scale-conditioned
flows (arXiv:2508.05744) [src]; a dedicated out-of-distribution task in the
FAIR Universe challenge (arXiv:2604.14451) [src].

**Robust inference.** RNPE models the discrepancy between simulations and
data explicitly (arXiv:2210.06564) [src]; a regularised loss penalises
summaries that increase the data–model mismatch (Huang et al. 2023,
arXiv:2305.15871) [src]. Compression of CMB maps into NILC cross-spectra
chosen to be robust to foreground misspecification gave unbiased r on the
PySM d12 model from training on a semi-analytic model (arXiv:2512.16869)
[src].

**Misspecification measured in a survey pipeline.** KiDS-SBI trained a
second likelihood on 18 000 simulations of an "isotropic" model without
variable depth or additive and PSF shear biases, and crossed data and
likelihood models (arXiv:2404.15402) [src: Sect. 7.2]:

| Effect or test | Size stated |
|---|---|
| Variable depth, two-point signal | up to 1%, about 0.2σ of additional non-cosmological signal |
| Variable depth, two-point uncertainty | ≲ 20% (quoting Joachimi et al. 2021) |
| Additive and PSF shear biases, pseudo-C_ℓ | per-cent level, up to ~0.3σ, below 0.1σ at most scales |
| Same mock analysed with both learned likelihoods | S8 marginal shifts by ~0.7σ; anisotropic model ~5% narrower |
| Effects neglected but present in the data, over noise realisations | S8 biased by up to ~1σ |
| Gaussian likelihood with fixed covariance against the SBI likelihood | S8 interval ~11% (noiseless) and ~10% (noisy) narrower, and more biased with noise |

The last row comes from the cosmology dependence of the cosmic variance,
mostly through S8, which a fixed-covariance Gaussian likelihood ignores
[src: Sect. 8]. The paper's point is that a systematic must be judged by
its effect on the likelihood, not only on the signal-to-noise
[src: Sect. 7.2].

**Explicit likelihoods can be worse calibrated.** In the same CAMELS Lyα
setting a Gaussian likelihood with a Ledoit–Wolf-regularised covariance
from 27 cosmic-variance runs and an RBF-interpolated P1D was "severely
overconfident"; calibration needed the covariance scaled by λ = 2.8, and
the calibrated MCMC was ~12% and ~40% less precise than SBI on Ω_m and σ8
(arXiv:2603.13011) [src: Sect. II.6 for the 27 runs, Sect. IV.4].

The comparison measures the cost of
a poorly estimated covariance, not an advantage of SBI on the same
information [der].

**Baryons as a misspecification test.** The DES Y3 map analyses train on
dark-matter-only simulations and test with baryon-corrected CosmoGridV1
mocks. The C_ℓ × CNN analysis averaged the compressed statistics of 100
CosmoGridV1 runs, an independent PKDGRAV3 suite, and found shifts below
0.3σ in the S8–Ω_m plane and in the mean of w for baryons and for a
source-galaxy bias of 0.5 or 1.5 instead of 1 (arXiv:2403.02314)
[src: Sect. 7.3.1]; the hybrid-statistics analysis uses 118 seed-matched pairs at one
cosmology and requires a shift below 0.3σ in the Ω_m–S8 plane and in w
(arXiv:2606.11309) [src: Sect. 7.2]; the clustering + lensing design found
the baryon effect negligible at its scale cuts and marginalises over it
anyway (arXiv:2511.04681) [src: Sect. VI.1.2]. No cosmology collaboration has adopted a general robust-SBI method
in a headline analysis; see `cosmo-statistics-inference` §4 of its
open-questions file for the statistics side.

## 3. Emulator error
<!-- key: emulator-error -->

**Mechanism.** The emulator returns t̂(θ) = t(θ) + ε(θ); ε is small inside
the training design and uncontrolled outside it. For simulation-trained
emulators ε also contains the simulation's own resolution and shot-noise
error at high k (arXiv:2605.28596) [src].

**Size.** 0.1% (linear) and 0.4% (non-linear correction) at the 99th
percentile for CosmoPower on Boltzmann-code output (arXiv:2106.03846)
[src: Sect. 3.2]; sub-percent to k ≃ 10 h Mpc⁻¹ for DarkEmulator2
(arXiv:2605.28596) [src]. These are residuals against the training code.

Error budgets against held-out simulations or codes, read in the bodies:

| Emulator | Held-out test | Error stated |
|---|---|---|
| PyBird-Emu (one-loop EFTofLSS P_ℓ) | 5000 linear spectra drawn from the COMET parameter space, errors in units of a Stage-IV σ (V_eff = 50 Gpc³, n̄ = 5 × 10⁻⁴ h³ Mpc⁻³) | 95% of residuals below 0.1σ for all multipoles to k_max = 0.2 h Mpc⁻¹; about 0.5σ to 0.3 h Mpc⁻¹ (arXiv:2507.20990) [src: Sect. 2.2, App. B] |
| Same, end to end | PT-challenge mocks, 566 (h⁻¹Gpc)³ | posteriors of PyBird-Emu and PyBird differ by < 0.06% of the parameter values, ~0.3% for σ8 in the wedge fit to 0.3 h Mpc⁻¹ (arXiv:2507.20990) [src: Sect. 4.1, Fig. 4] |
| GokuNEmu (T2N-MusE) | leave-one-out on 21 high-fidelity (1000 h⁻¹Mpc, 3000³) and 564 low-fidelity (250 h⁻¹Mpc, 750³) Goku-W runs, 10 parameters, 6 redshifts × 64 k | mean error more than five times and worst case about eight times lower than the Gaussian process, whose worst case the authors compute at 8.81%; the 2-step architecture alone gains about three (arXiv:2507.07184) [src: Sect. II.1, IV, Table 1] |
| DarkEmulator2 | 30 independent test cosmologies; mean absolute percentage error per cosmology, averaged over the test set | adding the linear P(k) as input lowers the mean error at z = 0 by about 5.8% (relative) and removes BAO-scale oscillations; errors larger at the edge of the prior volume; unphysical high-k features when the resolution input exceeds N_p^{1/3} = 3100; usable to z ≃ 4 only qualitatively (arXiv:2605.28596) [src: Eq. 13–14, Sect. 4.1, App. D] |

Two lessons recur: the error grows towards the edges of the training
design, where sampling is sparse (arXiv:2605.28596 [src: Sect. 4.1]), and
an emulator error quoted per k must be translated into σ of the target
survey before it means anything (arXiv:2507.20990 [src: Sect. 2.2]).

**Mitigation.** Split the target into a well-known part and a learned
correction (P_L × P_NL-corr, arXiv:2106.03846 [src: Sect. 3.2]); feed physical
auxiliary inputs such as the linear P(k) (arXiv:2605.28596, arXiv:2507.20990)
[src]; propagate the validation-set error into the likelihood
(arXiv:2205.11587) [src].

**Validation.** Full-likelihood posterior comparison against the exact code
on mock data with the survey covariance (arXiv:2106.03846 [src: Sect. 3.2];
arXiv:2603.16003 [src]); tests at cosmologies outside the training set
(arXiv:2507.20990) [src].

**Reference a referee expects.** arXiv:2106.03846 for the method;
arXiv:2205.11587 for propagation; the sibling `cosmo-statistics-inference`
for the budget in the likelihood.

## 4. Overconfident posteriors and training-set size
<!-- key: overconfident-posteriors-and-training-set-size -->

**Mechanism.** A neural density estimator trained on a finite simulation
bank can be overconfident; every algorithm in the Hermans et al. benchmark
(SNPE, NRE, SNL, ABC variants) produced overconfident approximations in
some setting (arXiv:2110.06581) [src]. The benchmark used budgets of 2¹⁰ to
2¹⁷ simulations and up to three parameters; overconfidence was most
prominent for sequential (non-amortised) methods at small budgets, a large
budget did not guarantee conservative posteriors, ABC with the identity
as a sufficient statistic was not conservative either, and ensembles of
five amortised estimators always raised the coverage but could still be
overconfident, while bagging did not reliably help [src: Sect. 3.3, 3.4].
A coverage analysis of a sequential method needs the whole pipeline
rerun per observation (300 here), which the authors call computationally
prohibitive; they recommend amortised methods for sensitive applications
[src: Sect. 3.4]. With limited simulation budgets "the
inferred posteriors can easily be quite wrong", and Thiele 2026 calls the
limited simulation budget the critical problem for cosmology
(arXiv:2605.10719) [src: Sect. 5; abstract]. A further trap: NPE posteriors
must not be multiplied for i.i.d. data sets, because each already contains
the prior, and imperfect learning of a box prior then amplifies the error
(arXiv:2605.10719) [src: Sect. 2.7, Fig. 5].

**Mitigation.** Ensembles of estimators (arXiv:2110.06581 [src];
KiDS-SBI stacks six flows, arXiv:2404.15402 [src: Sect. 5.4]; deep
ensembles in general ML, Lakshminarayanan et al. 2017, arXiv:1612.01474
[src]); balanced NRE, which is more conservative at small budgets with the
same Bayes-optimal solution (Delaunoy et al. 2022, arXiv:2208.13624) [src];
post hoc coverage calibration at the population level (arXiv:2608.23534)
[src]; multi-fidelity training or analytic treatment of large scales
(arXiv:2605.10719) [src: Sect. 5]; conformal prediction for classifiers,
with anomaly-stratified Mondrian conformal prediction giving uniform
conditional coverage where vanilla Mondrian under-covers (Sasli et al.
2026, arXiv:2607.08044) [src].

**Validation.** Coverage, TARP and fixed-θ tests are the business of
`cosmo-statistics-inference` (its results.md §8 and open-questions.md §4).
What the survey analyses ran:

| Analysis | Coverage test | Outcome |
|---|---|---|
| KiDS-SBI | TARP on S8 and Ω_m only, 500 new Latin-hypercube simulations, 1000 posterior samples each, bootstrapped 100 times; repeated with A_IA varied | slightly underconfident, within 1σ of ideal (arXiv:2404.15402) [src: Sect. 7.1, Fig. 14] |
| DES Y3 lensing + clustering design | HPD and TARP in the full ten-dimensional space, 1000 held-out CosmoGridV1 mocks; HPD found the more sensitive | "accurate calibration" (arXiv:2511.04681) [src: Sect. VI.2, Fig. 10] |
| DES Y3 hybrid statistics | TARP in (Ω_m, S8, w) with a truncated-Gaussian fit to the active-learning simulation prior, leaving out the test simulation | after unblinding a software bug was found: TARP in fact showed overconfidence and bias in the Ω_m–w plane, traced to MAFs conditioning poorly on cosmology (arXiv:2606.11309) [src: Sect. 7.1, 7.5] |

The DES Y3 hybrid fix added a VICReg term to the final compression and
grew the flow ensemble from 4 to 8, with conditioning networks of 200
instead of 70–80 units; all 2D marginals moved by less than 0.3σ
[src: Sect. 7.5]. The same analysis trains on −1.05 < w < −0.3 and applies
the hard w prior afterwards, to avoid artefacts of a training set with a
hard boundary [src: Sect. 6.3].
Hold some diagnostics out of hyperparameter tuning, so as not to overfit on
them (arXiv:2605.10719) [src: Sect. 2.7].

## 5. Non-representative training sets for classifiers
<!-- key: non-representative-training-sets-for-classifiers -->

**Mechanism.** Spectroscopically confirmed training sets are brighter and at
lower redshift than the photometric samples to be classified. PLAsTiCC was
built around this: a small, pristine training set against a 3.5-million
object test set with larger uncertainties (arXiv:2012.12392)
[src: Sect. 3.2].

**Size.** SCONE reaches 99.73% in distribution, and its authors report that
out-of-distribution performance "does not fully match" (arXiv:2106.04370)
[src]. Trained on the spectroscopic subset and tested on the full
photometric sample, SCONE falls to 80.61 ± 1.75% accuracy, 81.86 ± 2.22%
purity, 80.06 ± 1.31% efficiency and AUC 0.855, against 98.84% accuracy on
its own validation set; restricted to class-balanced low-redshift test
subsets it reaches 83% (z < 0.4) and 87% (z < 0.3), because the
spectroscopic set is skewed to low redshift (arXiv:2106.04370)
[src: Sect. III.1.2, Table 5]. A first real case: Superphot+, trained on
ZTF g and r light curves of spectroscopically confirmed SNe and applied to
Rubin DP1 LSSTComCam photometry with redshift-matched bands, returned
uncalibrated, implausible class fractions (four SNe IIn of eleven) and
flagged all but one light curve as anomalous relative to ZTF; the authors
treated all eleven only as likely SNe (arXiv:2507.22864)
[src: Sect. IV.2, Table 4]. SuperNNova finds that common algorithms are poorly calibrated and
overconfident out of distribution (arXiv:1901.06384) [src]. In SN Ia
cosmology the resulting contamination is a small part of the systematic
budget; the numbers are in `cosmo-supernovae`. The DESC ELAsTiCC study
trains SCONE and computes bias corrections on a separate simulation of
millions of events, which "is still needed" when real data replace the
simulated ones (arXiv:2512.06319) [src: Sect. II, Sample Sizes]; it quotes
purity and accuracy above 98% for SuperNNova and SCONE as used in DES-SN5YR
[src: Sect. I]. Its SCONE was trained on a simulation of about 50 000 SNe Ia and
50 000 non-Ia after selection and reached 98% training and validation
accuracy [src: Sect. III.3]. Averaged over 25 realisations the wCDM fits
keep a w bias of ~0.01–0.03 at ~3–8σ significance (stat only) and slightly
smaller at ~2–6σ with systematics, depending on the Hubble-diagram
binning, for σ_w ≈ 0.02
[src: Sect. IV.1, Table 7]. The bias disappears when all true non-Ia are
removed, that is with a perfect classifier; three code fixes did not
remove it [src: Sect. IV.4].

**Mitigation.** Augmentation of the training set in redshift and noise
(the PLAsTiCC winner, arXiv:1907.04690 [src]; degrading low-z light curves
to mimic high z, arXiv:2012.12392 [src: Sect. 3.2]); spectroscopic
follow-up of many well-observed intermediate-redshift transients rather
than a representative sample (arXiv:1907.04690) [src]; Bayesian networks
for calibrated probabilities (arXiv:1901.06384) [src]; an explicit unseen
class and anomaly scores (arXiv:2012.12392 [src: Sect. 5];
arXiv:2607.08044 [src]).

**Validation.** Report the metric with its class weights; test with an
unseen class; measure calibration, not only accuracy.

## 6. Reproducibility practice
<!-- key: reproducibility-practice -->

**Mechanism.** A neural result depends on architecture, loss, random seed,
hyperparameters and training-set draw, none of which a reader can see in a
posterior plot. Two documented cases: SimBIG WST posteriors on BOSS "vary
significantly across different normalizing flow architectures"
(arXiv:2310.15250) [src]; one CNN can be less informative than the power
spectrum while an ensemble is not (arXiv:2610.19891) [src]. The loss
function alone moves the attainable figure of merit from 81% to 100%
(arXiv:2407.10877) [src: abstract].

**Practice that the literature now treats as standard.** Release code,
weights and training data: CosmoPower, CONNECT, Avocado, SCONE, ORACLE,
DASH, BIND, Astronomaly and the challenge data sets all state public
releases (arXiv:2106.03846, arXiv:2205.15726, arXiv:1907.04690,
arXiv:2106.04370, arXiv:2501.01496, arXiv:1903.02557, arXiv:2609.10709,
arXiv:2010.11202, arXiv:2405.02252) [src]. Use shared pipelines with
built-in coverage diagnostics and benchmarking, such as LtU-ILI (Ho et al.
2024, arXiv:2402.05137) [src]. Compare methods on a common data set
(Beyond-2pt, FAIR Universe; arXiv:2405.02252, arXiv:2604.14451) [src]. Tune
hyperparameters with k-fold cross-validation (arXiv:2605.10719)
[src: Sect. 2.7]. The DESC white paper asks for validation frameworks and
"reproducible integration within scientific pipelines"
(arXiv:2601.14235) [src].

**Blinding.** The KiDS-1000 GCNN analysis gives the clearest ML
protocol read here: observed shears entered only through noise footprints
until two conditions held, agreement between the power-spectrum and the
network analyses on mocks and robustness to the CosmoGrid benchmark
simulations (particle count 2048³, box 2250 h⁻¹Mpc, 500 time steps); after
unblinding one inference hyperparameter (the GPABC smoothing scale, 0.4 to
0.2) was changed in an additional run, tightening S8 by ~11%, and reported
as such (arXiv:2201.07771) [src: Sect. III, IV.1.3, VI]. The same analysis
trained three networks of the fiducial architecture and three "benchmark
networks" with changed batch size, depth or no graph convolutions, to test
hyperparameter robustness [src: Sect. IV.6]. The DES Y3 map-level design
works from the blinded DES Y3 catalogues (arXiv:2511.04681) [src: Sect. I].
KiDS-SBI fixed its forward model and all validation tests before any
measurement on the data; its first unblinded run gave an anomalously low
S8, traced to an inconsistency between the measurement code applied to the
simulations and to the data, and the data were re-measured and run
through the unchanged pipeline (arXiv:2404.15402) [src: Sect. 9.1]. The
DES Y3 C_ℓ × CNN analysis departed from the standard DES blinding because
active learning needed interim posteriors, which were kept inside the code;
networks were frozen after a run on a simulation, the compressed data were
checked to lie in the convex hull of the simulated ones, and the data
posterior was first seen shifted by a hidden offset to compare its figure
of merit with simulations (arXiv:2403.02314) [src: Sect. 7.5]. The
DES Y3 hybrid-statistics analysis trained and validated everything on
simulations, then ran two blind checks on the data: the data summaries
lie on the mock manifold, and every flow of the ensemble converges, with
the chains mean-subtracted and shifted to (Ω_m, S8) = (0.3, 0.8)
(arXiv:2606.11309) [src: Sect. 7.4]; the two post-unblinding changes are
reported with their < 0.3σ effect [src: Sect. 7.5, App. B].

## 7. What a referee checks
<!-- key: what-a-referee-checks -->

1. Training set: which simulator, how many simulations, parameter design
   and priors; whether the data lie inside the training range.
2. A test on a simulator not used in training, with bias and calibration
   reported there (`systematics.md` §1).
3. Loss function and architecture of any compression network; whether the
   summary is a posterior mean (MSE) or trained for sufficiency (VMIM,
   IMNN); ensemble or single network.
4. Density estimator, ensemble size, stopping rule, number of
   simulations; for NPE, no multiplication of posteriors.
5. Emulator: test-set error percentiles, full-likelihood comparison with
   the exact code, behaviour at the edge of the training box, error
   propagated or not.
6. Goodness of fit of the data under the learned model, and an
   out-of-distribution check.
7. Coverage and calibration tests, and their limits (sibling
   `cosmo-statistics-inference`).
8. Classifiers: metric and class weights, unseen classes, calibration,
   representativeness of the training set.
9. Comparison with an explicit-likelihood analysis on the same data and
   scale cuts.
10. Code, weights and training data public; seeds and hyperparameters
    stated.

## 8. Not verified
<!-- key: not-verified -->
