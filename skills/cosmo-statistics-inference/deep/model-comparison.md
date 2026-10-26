# Model comparison — cosmo-statistics-inference dossier

Scope: how each model-comparison statistic is computed in practice from chains and nested-sampling
runs (Savage–Dickey from the extended model, DIC from samples, evidence decomposed into fit and
Ockham terms, out-of-sample scoring by held-out data blocks, sequential e-values), how the prior of
the extra parameters is chosen and stress-tested, and what each route gave on the same DESI DR2 data;
the definitions, the DESI Δχ² conversion table and the Lindley-paradox argument are in the
reference files.
Snapshot: 2026-10-19.
From: CosmoVerse White Paper, Sect. 3.1.7.

Prerequisites at L2: definitions of `Δχ²_MAP`, AIC, BIC, DIC, evidence, Bayes factor and the
Savage–Dickey ratio in `physics-and-methods.md#the-statistics-in-use`; the conversion of `Δχ²` to σ
with `k` degrees of freedom in `physics-and-methods.md#the-conversion-desi-uses`; the Lindley
paradox in `physics-and-methods.md#why-evidence-and-chi2-can-disagree`; the DESI DR2 table and the
evidence values in `results.md#model-comparison-evidence-against-delta-chi2-on`; the debate in
`open-questions.md#bayesian-evidence-against-delta-chi2-for`. Nested-sampling settings and the
accuracy of evidence estimators are in `cosmo-software-ecosystem/deep/samplers-frameworks.md`; they
are not repeated here. Equation numbers are those of the paper cited next to them.

Symbols. `M_0` the simpler model nested in `M_1`; `θ` the shared parameters, `η` (or `ω`) the extra
ones, `η_1` (`ω_⋆`) the value at which `M_1` reduces to `M_0`; `Z` the evidence; `ln B` the log
Bayes factor, whose sign convention is stated at each use because papers differ; `D = −2 ln L + C`
the deviance; `p_D` the Bayesian complexity; `π` the prior; `P` the posterior; ELPD the expected
log predictive density.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Decide which question the statistic answers, and fix the alternative in advance
<!-- key: step-1-decide-which-question-the-statistic -->

Karim, Speagle & Hložek 2026 (arXiv:2609.04334) separate three questions [src: Sect. II, Table 1]:

| Statistic | Question | Scoring | Role of the prior width |
|---|---|---|---|
| `Δχ²_MAP` | which model fits best at its best-fitting parameters | in-sample | weak |
| `ln B` | which model better explains the data, averaged over its prior | in-sample | strong |
| ΔELPD | which model better predicts data it has not seen | out-of-sample | weak |

"The three coincide only when the additional parameters are tightly constrained relative to their
priors; neither condition holds for the w0waCDM comparison" [src: Table 1 caption]. Their reading of
the prior: "a functional form of a model with two different assumed priors are treated as two
different models at the level of model comparison", so a Bayes factor computed with a conventional
prior "inherits the convention" [src: Sect. II].

The alternative must be specified before the statistic is computed. In the sequential test of Kim,
Mota & Tamosiunas 2026 (arXiv:2607.28918) the default specification "is our single pre-specified
test (chosen before computing M_t)" [src: Sect. 2], and the paper shows that the answer "depends
strongly on which departures from ΛCDM the test is designed to detect" [src: abstract].

### Step 2. The likelihood-ratio route: find the two maxima, then convert
<!-- key: step-2-the-likelihood-ratio-route-find-the-two -->

- DESI DR2 finds each best fit with `iminuit` started from the MAP of every chain, and defines
  `Δχ²_MAP ≡ −2Δ ln L` as "twice the difference in the negative log posteriors at the maximum
  posterior points for each model", which "accounts for the contribution of any non-uniform priors"
  (arXiv:2503.14738) [src: Sect. V].
- The minimiser itself is a source of noise. Karim et al. (arXiv:2609.04334) find that widening the priors moved
  `Δχ²_MAP` by 0.45, "comparable to the scatter we obtain between minimizer restarts" [src: Sect.
  IV.1]. Run several restarts per model and quote their spread.
- Conversion: `k` extra parameters, χ²_k survival function, two-sided Gaussian equivalent (L2). Kim
  et al. (arXiv:2607.28918) restate the DESI case: `Δχ² = 12.5` on `k = 2` gives `p = 0.0019`, 3.1σ two-sided, and
  `sqrt(Δχ²) ≈ 3.5σ` "holds only for k = 1" [src: App. B.1].
- When Wilks' conditions are in doubt, calibrate the tail by Monte Carlo under the null with the
  same Gaussian likelihood. Kim et al. did so for their test statistic with `N = 2 × 10^5` draws and
  found it reproduces Wilks "in this aligned-prior, local-Gaussian regime", a near-equality that is
  "empirical rather than a theorem" [src: App. B.1].

### Step 3. The evidence route: report the fit term and the Ockham term separately
<!-- key: step-3-the-evidence-route-report-the-fit-term -->

Lodha et al. 2025 (DESI extended dark energy, arXiv:2503.14743) compute `ln B` with PolyChord and
the same priors and Boltzmann code as the posterior analysis, with `θ_MC` replaced by `H_0` "to avoid
numerical issues arising from the shooting method", and post-process with `anesthetic` [src: App. A].
They split the log evidence [src: App. A, Eq. 21]:

`log Z = ⟨ln L⟩_P − ⟨ln(P/π)⟩_P`

The first term (arXiv:2503.14743), the posterior average of the log-likelihood, "can be considered the Bayesian
equivalent of χ²"; the second is the Kullback–Leibler divergence from prior to posterior, the
prior-dependent Ockham penalty [src: App. A]. Reporting both shows whether a change of `ln B`
comes from the fit or from the prior: from DR1 to DR2, with Pantheon+, `Δ⟨ln L⟩_P` rose from
3.34 ± 0.17 to 4.53 ± 0.17 while the penalty stayed near 5 (4.87 ± 0.43 to 5.18 ± 0.43)
[src: Table 4]. Their reason for preferring the evidence-side terms to `Δχ²`: the evidence "is
less susceptible to random fluctuations in the data leading to a better fit at a specific point in
parameter space by chance" [src: App. A].

Run settings used in one external evidence analysis (Karim et al., arXiv:2609.04334, PolyChord in Cobaya):
`nlive = 1000`, `nprior = 1500`, `num_repeats = 3 n_dim` (45 and 51 for 15 and 17 sampled
dimensions), precision criterion 0.01; the live-point count "exceeds the usual 25 n_dim guidance
for evidence estimation by a factor of 2.4–2.7"; evidences with `anesthetic` [src: App. A.1]. Nine
CMB nuisance parameters common to both models with identical priors "cancel exactly in the Bayes
factor" [src: App. A.1, Table 3].

### Step 4. The Savage–Dickey route: one chain of the extended model
<!-- key: step-4-the-savage-dickey-route-one-chain-of-the -->

Conditions, as listed by Lin et al. 2025 (arXiv:2506.04339) [src: Sect. 2.2]: (1) the parameters of
`M_1` split into `θ` and `η`; (2) the likelihood of `M_1` reduces to that of `M_0` at `η = η_1`;
(3) the priors on `θ` are identical in both models; (4) the priors on `θ` and `η` are separable.
Then [src: Eq. 6]

`Z_0 / Z_1 = p(η_1 | d, M_1) / p(η_1 | M_1)`,

the normalised marginal posterior of the extra parameters over their prior, at the nested point.
Trotta 2007 (arXiv:astro-ph/0504022) writes the same ratio as Eq. 7 and notes that its derivation
"does not involve any assumption about the posterior distribution, and in particular about its
normality" [src: Sect. 2.2].

Procedure.

1. Sample `M_1` only. The SDDR is computed afterwards from the chain, and a change of prior on `η`
   or a reparameterisation is a reweighting of the same samples (Trotta 2007) [src: Sect. 2.2].
2. Estimate the normalised marginal density at `η_1`: a normalised histogram for one or two extra
   parameters, a normalising flow beyond a few dimensions, because "beyond even a few dimensions
   normalizing a histogram becomes computationally challenging" (Lin et al.) [src: Sects. 2.3–2.4].
3. Error bar: bootstrap. Lin et al. resample the marginal posterior samples with replacement and
   retrain a flow (or rebuild the histogram) for each set, quoting the mean and standard deviation
   [src: Sect. 2.5]; Trotta 2007 splits the chain into `R = 5` subsets [src: App. C]. Neither error
   includes "a possible systematic under-exploration of the likelihood's tails" [src: Trotta 2007,
   App. C].
4. Check the regime of validity: the nested point must lie where the chain has samples (Step 6).

Analytic guide. For a Gaussian prior of width `Δω` centred on `ω_⋆` and a Gaussian likelihood of
mean `μ̂` and width `σ̂`, with `λ = |μ̂ − ω_⋆|/σ̂` and `β = σ̂/Δω` [src: Trotta 2007, Eq. 8]:

`ln B_01 = (1/2) ln(1 + β^-2) − λ²/[2(1 + β²)]`, and for informative data `ln B_01 ≈ I − λ²/2`
with `I = −ln β` [src: Eq. 9].

Evidence against the simpler model grows as `λ²`; evidence for it only as `I` (arXiv:astro-ph/0504022); "for strong odds
against the simpler model (λ ≫ 1) the prior choice becomes irrelevant unless I ≫ λ", which is the
Lindley regime [src: Sect. 2.2]. For moderately informative data (`I ≈ 1–2` in base 10) the measured
mean must lie about 4σ from `ω_⋆` "to robustly disfavor the simpler model" [src: Sect. 3.3].

### Step 5. DIC from samples
<!-- key: step-5-dic-from-samples -->

As written by Liddle 2007 (arXiv:astro-ph/0701113) [src: Sect. 2.3, Eqs. 5–7] and adopted by DESI
(Lodha et al., arXiv:2503.14743, Eqs. 19–20) [src: Sect. VI.4]:

`p_D = mean[χ²(θ)] − χ²(θ̄)`, `DIC ≡ D(θ̄) + 2 p_D = mean[D(θ)] + p_D`,

means over the posterior. `p_D → 1` for a parameter well inside its prior and `→ 0` for an
unconstrained one, so `p_D` counts constrained parameters [src: Liddle, Sect. 2.3].

Computation: average `χ²` over the (weighted) samples; one extra likelihood call at the posterior
mean, or, with someone else's chains, "the sample closest to that mean value" (Liddle) [src: Sect.
2.3]. Weighted nested-sampling samples work as well [src: same]. When chains of two experiments
are combined by density estimation, DESI computes `⟨χ²⟩` as the sum of the two experiments' means,
each over its weighted `CombineHarvesterFlow` chain (arXiv:2503.14738) [src: Sect. V].

Scale used by DESI for nested models: a decrease of at least 2 needed for a "not insignificant"
improvement, up to 5 "positive", up to 10 "strong", beyond "decisive"; for non-nested classes "there
is no absolute scale" and each is compared with ΛCDM only (arXiv:2503.14743) [src: Sect. VI.4].

Two choices inside the DIC. (i) The point estimate: mean or maximum likelihood; the choice "affects
the possible reparametrization dependence of the statistic", and the mean is "a poor choice if the
likelihood has distinct strong peaks" [src: Liddle, Sect. 2.3]. (ii) Asymptotics: the DIC tends to
the AIC for large data sets and is "dimensionally inconsistent", sharing support among models even
with infinite data, while the evidence and the BIC are consistent [src: Liddle, Sect. 2.5].

### Step 6. Stress-test the prior of the extra parameters
<!-- key: step-6-stress-test-the-prior-of-the-extra -->

- Plot the result in the `(I, λ)` plane: "a different choice of prior will amount to a horizontal
  shift of the points", as long as the posterior is likelihood-dominated, so the prior change needed
  to reverse a conclusion can be read off without resampling (Trotta 2007) [src: Sect. 3.3]. His
  example: for `n_s` from WMAP3 a prior two orders of magnitude wider would reverse the conclusion,
  "however physically unmotivated" [src: Sect. 3.3].
- DESI's version of the same test: with DESI DR2 BAO + CMB + DESY5, reversing the ranking would need
  the prior "expanded by a factor of more than 10 times for both w parameters, leading to a greater
  than 100 times expansion in prior volume", which they judge "unphysical and unreasonable"
  (arXiv:2503.14743) [src: App. A].
- Direct measurement: Karim et al. (arXiv:2609.04334) widen every prior (Table 3: `(w_0, w_a)` area 1.096 against 15.5,
  shared parameters also widened) on identical data; `ln B` moves from −0.92 to +2.36 (their sign:
  positive favours ΛCDM) on posteriors that are "indistinguishable" [src: Sect. IV.1; Table 3 in
  App. A.1].
- The measured shift of `ln B` is larger than the logarithm of the `(w_0, w_a)` area ratio alone
  `[der: from the two areas above]`; the shared parameters cancel between models, so the difference
  is not explained by the text read and is left unresolved (evidence errors for these two rows not
  read).
- Posterior-informed priors are not legitimate for an evidence. Karim et al. run their baseline
  with priors spanning at least 5σ of each marginal, legitimate for ELPD, but "not a defensible a
  priori prior for an evidence calculation" [src: Apps. A.1, A.3].
- A physically motivated alternative is a different model, not a different prior on the same one:
  in the sequential test a thawing-quintessence specification "rejects more strongly than any
  agnostic choice" (arXiv:2607.28918) [src: abstract].

### Step 7. Out-of-sample scoring by held-out blocks
<!-- key: step-7-out-of-sample-scoring-by-held-out-blocks -->

Karim et al. 2026 (arXiv:2609.04334) [src: Sects. II.1, III, App. A]:

1. Partition the data into withheld `y_i` and seen `y_−i`, and compute
   `p(y_i | y_−i) = ∫ p(y_i | y_−i, θ) p(θ | y_−i) dθ` [src: Eq. 1]; the conditional likelihood
   term handles correlated data, and the posterior from seen data "is what makes log predictive
   density much less sensitive to assumed priors compared to ln B" [src: Sect. II.1].
2. Choose blocks by redshift, not single points (arXiv:2609.04334): each DESI BAO tracer bin is one block (`K = 7`
   blocks, 13 observables); supernovae sorted by `z_cmb` into contiguous equal-count blocks (30 of
   53 for Pantheon+, 31 of 59 for DES-Y5, 35 of 52 for DES-Dovekie; Union3 already binned, `K = 22`)
   [src: Sect. III]. A joint hold-out removes a BAO block with all supernovae in the same redshift
   group [src: Sect. III].
3. Never withhold a block that is not local in the tested direction: the CMB "is part of y_seen at
   every step", because it "constrains the late-time expansion only through a global geometric
   degeneracy" [src: Sect. III].
4. Estimate each held-out term from the full chain by Pareto-smoothed importance sampling (PSIS),
   with `arviz`, after converting weighted chains to equal weights with `anesthetic` [src: Sect. II.1,
   App. A.1].
5. Check the Pareto shape `k̂` of every block. In the `z < 0.1` supernova cell `k̂ = 0.75` for
   DES-Dovekie, "at or beyond its reliability threshold"; the block must then be removed and the chain
   rerun [src: Sect. IV.3].
6. Read ΔELPD as a log odds: a joint hold-out `ΔELPD = −0.46` means odds `e^0.46 ≈ 1.58:1` for
   w0waCDM [src: Sect. IV]; decompose by block to localise the preference.

### Step 8. Repeated looks across data releases
<!-- key: step-8-repeated-looks-across-data-releases -->

A significance quoted at DR1, then at DR2, is a test run twice. Kim et al. 2026 (arXiv:2607.28918)
build an e-value, a non-negative statistic with `E[E | H_0] ≤ 1`, so that rejecting at `E ≥ 1/α`
controls the type-I error at `α` by Markov's inequality, and e-values from independent data multiply
[src: Sect. 2]. The mixture e-value [src: Eq. 2]

`E_mix = ∫ [L(data | θ)/L(data | H_0)] π(θ) dθ`

"is exactly the Bayes factor with prior π" (arXiv:2607.28918), valid because `π` is proper and fixed before the data
[src: Sect. 2]. A maximised likelihood ratio is not an e-value: `E_H0[exp(Δχ²(k)/2)]` diverges for a
χ²_k variable [src: App. A, Remark 2, Eq. 11]. Default specification: flat on a 30 × 30 grid in
`[−1.5, −0.5] × [−2, 1]` for `(w_0, w_a)` [src: Sect. 2]. No σ is quoted, because an e-value "has no
canonical null distribution": at `E = 33.97` the distribution-free bound gives 2.18σ and the
Monte Carlo tail 3.69σ [src: App. B.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

| Route | Needs | Prior dependence | Cost | Fails when |
|---|---|---|---|---|
| `Δχ²_MAP` + Wilks | two optimisations | none (except non-flat priors at the MAP) | low; minimiser restarts | boundaries, non-Gaussian likelihood, post hoc model (L2) |
| Nested-sampling evidence | one run per model | linear in prior volume | high | prior conventional; noisy runs (sampler dossier) |
| Savage–Dickey | one chain of `M_1` | same as evidence | negligible after sampling | nested point beyond about 3σ in the tail |
| DIC | chains of both models | weak | negligible | multimodal or "singular" posteriors |
| ΔELPD by blocks | one chain per model, PSIS | weak | low; reruns when `k̂` is large | blocks not local; correlated blocks without the conditional term |
| e-value | proper specification fixed in advance | through the specification | low | specification chosen after seeing the data |

Head-to-head results.

- **Evidence estimators on one posterior** (Lin et al. 2025, arXiv:2506.04339; `ln B` positive for
  ΛCDM, mock truth ΛCDM). Simulated DES Y1 3×2pt, wCDM: nested sampling 2.23 ± 0.45, learned
  harmonic mean 2.15 ± 0.01, SDDR histogram 2.14 ± 0.02, SDDR flow 2.13 ± 0.02 [src: Table 3].
  Stage-IV shear, 39 against 37 parameters, w0waCDM: nested sampling 0.78 ± 0.71, learned harmonic
  mean 1.53 ± 0.07, SDDR 1.75 ± 0.06 with either estimator [src: Table 4]. The SDDR saves the
  sampling of the nested model, "approximately halving the computational cost" [src: Sect. 3.2].
- **SDDR accuracy against the exact answer** (Trotta 2007, arXiv:astro-ph/0504022, Gaussian benchmark in D = 5, 10, 20):
  "extremely well for λ ≤ 2", less accurate at λ = 3, "very unpractical" beyond; fewer than 10^5
  samples suffice for λ < 3, and the error grows "only mildly" from D = 5 to 20 [src: App. C, Fig. 5].
- **DIC against Δχ² on DESI DR2** (arXiv:2503.14743, Table 3): `ΔDIC (Δχ²)` = −6.8 (−10.7), −13.5
  (−17.4), −17.2 (−21.0) for w0wa with Pantheon+, Union3, DESY5; a one-parameter calibrated thawing
  model gives +0.4 (−1.6), −0.6 (−2.5), −5.8 (−7.1) [src: Table 3]. The mirage class matches w0wa
  (−9.1 to −18.7) [src: same].
- **Two evidence analyses, same DESI priors, DR2 BAO + CMB + SNe** (sign: positive favours w0wa).
  Lodha et al. (arXiv:2503.14743; CMB as in the DESI paper): −0.66 ± 0.44, 3.03 ± 0.44, 4.88 ± 0.44 for Pantheon+,
  Union3, DESY5 [src: App. A, Table 4]. Ong et al. 2025 (arXiv:2511.10631; Planck 2018 CamSpec, PolyChord in Cobaya,
  `w_0 ∈ [−3, 1]`, `w_a ∈ [−3, 2]`): −1.70 ± 0.26, +1.37 ± 0.27, +3.32 ± 0.27 [src: Sect. II,
  Table 1]. For every compilation the two disagree by more than their quoted errors; the CMB
  likelihood and the `θ_MC → H_0` substitution differ, and no paper read reconciles them.
- **Three statistics, one prior change** (Karim et al., arXiv:2609.04334, Pantheon+ + DESI + Planck, identical data):
  `ln B` shifts from +2.36 to −0.92 (wide to narrow priors), `Δχ²_MAP` moves by 0.45, ΔELPD by 0.01, 0.03 and 0.02 (BAO hold-out, SN hold-out,
  joint) [src: Sect. IV.1].
- **Where the preference sits.** ELPD: the LRG2 block (z = 0.706) scores between −1.21 and −1.99
  depending on the supernova sample, the supernovae at the same redshift between +0.92 and −0.19, and
  removing LRG2 alone brings the total to between +0.27 and −0.04 [src: arXiv:2609.04334, Sect.
  IV.2]. e-value: `M_DR2 = 33.97` for the aligned specification, 0.49 without LRG2, and no survival
  of a correction for any of the seven bins producing the excess [src: arXiv:2607.28918, abstract].
  The in-sample evidence analysis attributes the preference to a DESI–DES-SN5YR conflict instead
  (L2, `results.md#the-same-data-under-the-bayesian-evidence`); the disagreement is open.

When to use which. A nested extension with a physically fixed prior range: evidence, cross-checked
by SDDR from the same chain. A phenomenological extension without a natural prior (CPL): `Δχ²_MAP`
with `k` and a Monte Carlo check of the tail, plus a Bayes factor shown for at least two priors, plus
an out-of-sample score to localise the driver. Non-nested model classes: DIC or ΔELPD, ranked against
a common reference, with no absolute scale. A claim updated release after release: an e-value with
its specification stated.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Scatter of `Δχ²_MAP` between minimiser restarts | ≈ 0.45 | DESI DR2 + Planck + Pantheon+ | arXiv:2609.04334 | Sect. IV.1 |
| PolyChord settings for evidences | `nlive = 1000`, `nprior = 1500`, `num_repeats = 3 n_dim`, precision 0.01 | external w0wa analysis | arXiv:2609.04334 | App. A.1 |
| Live-point guidance for evidences | 25 n_dim | as quoted | arXiv:2609.04334 | App. A.1 |
| SDDR valid range (Gaussian benchmark) | λ ≲ 3, < 10^5 samples | toy, D = 5–20 | arXiv:astro-ph/0504022 | App. C |
| Distance needed to disfavour the simpler model, `I ≈ 1–2` | λ ≳ 4 | Gaussian guide | arXiv:astro-ph/0504022 | Sect. 3.3 |
| DIC scale for nested models | 2 / 5 / 10 | DESI DR2 | arXiv:2503.14743 | Sect. VI.4 |
| Prior expansion needed to reverse `ln B` (DR2 + CMB + DESY5) | > 10 per `w` parameter, > 100 in volume | DESI DR2 | arXiv:2503.14743 | App. A |
| Ockham penalty `Δ⟨ln(P/π)⟩_P`, DR2 + CMB + SNe | 5.18, 4.75, 4.54 (± 0.43) | DESI DR2 | arXiv:2503.14743 | Table 4 |
| Fit term `Δ⟨ln L⟩_P`, same | 4.53, 7.78, 9.42 (± 0.16–0.17) | DESI DR2 | arXiv:2503.14743 | Table 4 |
| `ln B` (positive for w0wa), DR2 + CMB + Pantheon+ / Union3 / DESY5 | −0.66 / 3.03 / 4.88 (± 0.44) | DESI DR2 | arXiv:2503.14743 | Table 4 |
| Same with Planck CamSpec | −1.70 / +1.37 / +3.32 (± 0.26–0.27) | external | arXiv:2511.10631 | Table 1 |
| `ln B` change from wide to narrow priors, identical data | +2.36 → −0.92 (positive for ΛCDM) | external | arXiv:2609.04334 | Sect. IV.1 |
| `(w_0, w_a)` prior area, baseline and wide (with `w_0 + w_a < 0`) | 1.096 and 15.5 | external | arXiv:2609.04334 | Table 3 |
| Joint hold-out ΔELPD, DESI + Planck + Pantheon+ | −0.46 (odds 1.58:1 for w0wa) | external | arXiv:2609.04334 | Sect. IV |
| Pareto `k̂` at `z < 0.1`, DES-Dovekie | 0.75 | external | arXiv:2609.04334 | Sect. IV.3 |
| e-value, DR1 → DR2, aligned specification; without LRG2 | 33.97; 0.49 | external | arXiv:2607.28918 | abstract |
| e-value threshold for 5% | 20 | external | arXiv:2607.28918 | abstract |
| Bayes factor to p-value bound | `B ≤ −1/(e p ln p)` for `p ≤ 1/e` | external | arXiv:2511.10631 | Eq. 1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **A `Δχ²` read from the chain.** The best sample of an MCMC is not the maximum; DESI polishes with
  `iminuit` from every chain's MAP (arXiv:2503.14738) [src: Sect. V]. Test: restart the minimiser
  and quote the spread; a spread comparable to 0.5 (arXiv:2609.04334) [src: Sect. IV.1] matters for
  differences of a few units.
- **SDDR in the tail.** If ΛCDM sits 3σ or more from the extended-model posterior, the chain does not
  sample `η_1` and the histogram or flow value there is an extrapolation; the bootstrap error does not
  see it (arXiv:astro-ph/0504022) [src: App. C]. Test: count samples near `η_1`; compare with a direct
  nested-sampling evidence; Trotta suggests sampling "at a higher temperature" [src: App. C].
- **SDDR with non-separable or different priors.** If the prior on the shared parameters differs
  between the two runs, or depends on `η`, conditions (3)–(4) fail (arXiv:2506.04339) [src: Sect.
  2.2]. Typical cosmology case: a derived-parameter prior or a hard cut such as `w_0 + w_a < 0` that
  couples `η` to other parameters; the cut is on `η` alone and keeps separability, a cut involving
  `θ` does not `[der: from condition 4]`.
- **DIC on a singular or multimodal posterior.** When the maximum-likelihood point, the MAP and the
  posterior mean disagree, "it is unclear why the posterior mean (what DIC uses) should be the fixed
  point" (arXiv:2609.04334) [src: Sect. II.1]; the mean is a poor choice for distinct peaks
  (arXiv:astro-ph/0701113) [src: Sect. 2.3]. Test: recompute `D(θ̄)` at the MAP instead of the mean;
  a large change flags the problem.
- **`ΔDIC` read on an absolute scale for non-nested models.** DESI says there is none
  (arXiv:2503.14743) [src: Sect. VI.4].
- **A Bayes factor under a posterior-informed prior.** It is not an a priori evidence
  (arXiv:2609.04334) [src: App. A.3]. Test: state where the prior ranges came from.
- **Prior change confused with model change.** Two priors on the same functional form are two
  models (arXiv:2609.04334) [src: Sect. II]; quote `ln B` for each with its ranges.
- **Bayes factor converted to σ without saying how.** Ong et al. use the bound `B ≤ −1/(e p ln p)`
  and quote the result as an upper bound on the significance, computed only when `ln B > 0`
  (arXiv:2511.10631) [src: Sect. II, Table 1]; Kim et al. refuse any conversion of their e-value
  because two defensible conversions give 2.18σ and 3.69σ (arXiv:2607.28918) [src: App. B.1].
- **PSIS beyond its range.** A large Pareto `k̂` makes the held-out score biased; rerun without the
  block (arXiv:2609.04334) [src: Sect. IV.3]. The large `k̂` is itself a finding: "the remaining data
  predict this block poorly" [src: same].
- **Re-testing the same claim at each release.** A fresh Wilks σ at every release ignores the earlier
  looks (arXiv:2607.28918) [src: abstract]. Test: an anytime-valid e-value with a fixed
  specification, or a trial-factor argument (L2, `physics-and-methods.md#look-elsewhere-effect`).
- **A global number hiding one data point.** In-sample statistics "cannot localize the source of model
  preference" (arXiv:2609.04334) [src: Sect. I]; a leave-one-block-out score or e-value does, and on
  DESI DR2 both point to one BAO bin [src: Sect. IV.2; arXiv:2607.28918, abstract].

## Reading list
<!-- key: reading-list -->

- Foundation: Trotta 2007, arXiv:astro-ph/0504022 — the SDDR, its Gaussian form, the `(I, λ)` plane
  for prior sensitivity and its benchmark limits (Sects. 2.2, 3.3, App. C).
- Foundation: Liddle 2007, arXiv:astro-ph/0701113 — AIC, BIC and DIC side by side, computing DIC
  from samples, dimensional consistency (Sects. 2.2–2.5).
- Review: Trotta 2008, arXiv:0803.4089 — evidence, model complexity and their computation (L2).
- Method: Lin et al. 2025, arXiv:2506.04339 — SDDR with normalising flows, bootstrap errors and a
  comparison with nested sampling and the learned harmonic mean on DES Y1 and Stage-IV mocks.
- Method: Karim, Speagle & Hložek 2026, arXiv:2609.04334 — ELPD by held-out redshift blocks with
  PSIS, prior-sensitivity test of three statistics on identical data.
- Method: Kim, Mota & Tamosiunas 2026, arXiv:2607.28918 — e-values valid across data releases,
  why a maximised `Δχ²` is not one, and why no σ is quoted.
- Application: Lodha et al. 2025, arXiv:2503.14743 — DESI DR2 evidences with the fit/Ockham split,
  DIC for nested and non-nested dark-energy classes, the prior-expansion argument.
- Application: DESI Collaboration 2025, arXiv:2503.14738 — `Δχ²_MAP` from minimiser restarts, DIC
  with combined chains (Sect. V).
- Critique: Ong, Yallup & Handley 2025, arXiv:2511.10631 — the same data under the evidence, and the
  Bayes-factor-to-σ bound.
- Critique: Efstathiou 2008, arXiv:0802.3185 — limits of the evidence for poorly motivated nested
  models (L2).

## Not verified
<!-- key: not-verified -->

- The individual rows of Table 2 of arXiv:2609.04334 (ΔELPD per supernova sample and hold-out type)
  did not render; only the values quoted in its text are used.
- The original DIC paper (Spiegelhalter et al. 2002), the PSIS paper (Vehtari et al.,
  cited by arXiv:2609.04334) and the general non-factorised Gaussian ELPD estimator cited there as [4]
  were not read; the `k̂` reliability threshold is quoted only as arXiv:2609.04334 states it.
- The source of DESI's DIC scale (reference [183] of arXiv:2503.14743) was not read.
- The reason for the difference in `ln B` between arXiv:2503.14743 and arXiv:2511.10631 with
  the same priors was not established; nor the gap between the measured `ln B` shift and the
  logarithm of the prior-area ratio in arXiv:2609.04334.
- The e-value paper's per-bin and thawing-specification values beyond its abstract, and its DR3
  forecast (Sect. 4.4), were not read.
- Bayesian model averaging and the learned harmonic mean method paper were not read.
