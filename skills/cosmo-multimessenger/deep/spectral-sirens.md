# Spectral sirens — cosmo-multimessenger dossier

Scope: how a spectral-siren population model is specified (functional form,
priors, rate evolution, redshift evolution of the mass scales, flexible and
non-parametric alternatives), how each choice moves H0 and why, and how
blinded mock data challenges and injection studies are used to test it.
Snapshot: 2026-10-19.
From: Palmese & Mastrogiovanni 2025 (arXiv:2502.00239), Sects. 2.2 (redshift
information from the source mass) and 3.3; Einstein Telescope science case
(arXiv:2503.12263), Sect. 2.3.1 (spectral sirens); Zhao et al. 2026
(arXiv:2605.08595), Sect. 3.2.6.

Already in L2, not repeated here: the principle `m_det = (1 + z) m_src` and
the history of the method (Taylor et al. 2011, Farr et al. 2019, Ezquiaga &
Holz 2022), the features seen in the data and the content of the three LVK
models in words
(`physics-and-methods.md#dark-sirens-spectral-population-method`); the
hierarchical likelihood and the two LVK codes
(`physics-and-methods.md#hierarchical-likelihood-and-selection-function`);
the H0 values of each mass model in GWTC-3, GWTC-4.0 and GWTC-5.0, the
direction of the mis-specification bias, the evolution studies and their
headline results (`systematics.md#population-mass-spectrum-mis-specification`,
`open-questions.md#does-the-black-hole-mass-spectrum-evolve-with`).

## How it is done
<!-- key: how-it-is-done -->

Notation. `m1`, `m2` are the source-frame primary and secondary masses,
`Λ` the population hyperparameters, `𝒫(x | x_min, x_max, α) ∝ x^α` a truncated
power law, `𝒢(x | μ, σ, a, b)` a Gaussian truncated to `[a, b]`, `λ_g` the
fraction of events in Gaussian peaks, `ψ(z)` the merger-rate evolution,
`S_h`, `S_l`, `S_n` high-pass, low-pass and notch filters. The equations
follow Appendix C of the GWTC-4.0 cosmology paper (arXiv:2509.04348), which
Appendix A of the GWTC-5.0 paper (arXiv:2605.27227) cites for the equations;
the GWTC-5.0 priors are those of its Tables 5–8.

### Step 1. Choose the source-frame mass model
<!-- key: step-1-choose-the-source-frame-mass-model -->

The LVK models are mixtures of simple functions [src: arXiv:2509.04348,
App. C, Eq. C1–C20]:

```
Power Law + Peak (PLP):
  p(m1) = (1 − λ_g) 𝒫(m1 | m_min, m_max, −α) + λ_g 𝒢(m1 | μ_g, σ_g, m_min, m_max)   (C7)
  p(m2 | m1) = 𝒫(m2 | m_min, m1, β)                                                 (C8)
  low-mass smoothing: S_h(m | m_min, δ_m) rises from 0 to 1 over (m_min, m_min + δ_m),
  S_h = [f(m − m_min, δ_m) + 1]^(−1),  f(m', δ_m) = exp(δ_m/m' + δ_m/(m' − δ_m))     (C5, C6)
Multi-peak (MLTP): PLP with two Gaussians, fractions λ_g λ_g^low and λ_g (1 − λ_g^low)  (C9)
FullPop-4.0 (all compact binaries):
  p(m1) = (1 − λ_g) ℬ(m1 | m_min, m_max, −α1, α2, b) + two Gaussians as in MLTP        (C10)
  b = (m_break − m_min)/(m_max − m_min),  m_break = ½(m_d^low + m_d^high + δ_d^min − δ_d^max)  (C12, C13)
  notch S_n = 1 − A S_l(m | m_d^high, δ_d^max) S_h(m | m_d^low, δ_d^min),  A ∈ [0, 1]  (C17)
  p(m1, m2) = p_S(m1) p_S(m2) f(m1, m2) / N_S,  f = (m2/m1)^β1 if m2 < m_break, else (m2/m1)^β2  (C19, C20)
FullPop 3 Peaks: FullPop-4.0 with a third Gaussian                                  (2605.27227 Eq. A.1)
```

`ℬ` is a broken power law joined at `b` (Eq. C14), `m_d^low`, `m_d^high` the
edges of the neutron-star–black-hole dip, `A` its depth (`A = 1` an empty
gap), `p_S` the mass density multiplied by the three filters (Eq. C18). The
notch makes the gap depth data-driven: "the data can determine whether the
rate goes to zero within the gap or if the gap is partially or totally
filled" [src: arXiv:2605.27227, App. A]. With the pairing function the
marginal mass distributions differ from the marginals of the joint density
[src: arXiv:2509.04348, App. C]. In the three-peak model the peak fractions
get Beta(1, 2) and Beta(1, 1) priors, equivalent to a symmetric Dirichlet,
"to have an equal prior weight on each peak" [src: arXiv:2605.27227, App. A,
Table 7].

### Step 2. Set the priors on the population
<!-- key: step-2-set-the-priors-on-the-population -->

GWTC-5.0 priors (U uniform, LU log-uniform) [src: arXiv:2605.27227, Tables
5–8]:

| Model | Parameter | Prior |
|---|---|---|
| MLTP | `α`; `β` | U(1.5, 12); U(−4, 12) |
| MLTP | `m_min`; `m_max`; `δ_m` | U(2, 10); U(50, 200); U(10⁻³, 10) M☉ |
| MLTP | `μ_g^low`, `μ_g^high`; `σ_g^low`; `σ_g^high` | U(5, 100); U(0.4, 10); U(0.4, 15) M☉ |
| FullPop-4.0 | `α1`, `α2`, `β1`, `β2` | U(−4, 12) |
| FullPop-4.0 | `m_min`; `m_max` | U(0.4, 1.4); U(50, 200) M☉ |
| FullPop-4.0 | `δ_m^min`; `δ_m^max` | LU(10⁻², 1); LU(10⁻³, 10) M☉ |
| FullPop-4.0 | `μ_g^low`, `μ_g^high`; `σ_g^low`; `σ_g^high` | U(5, 150); U(0.4, 10); U(0.4, 15) M☉ |
| FullPop-4.0 | `m_d^low`; `m_d^high`; `δ_d`; `A` | U(1.5, 3); U(5, 9); LU(0.01, 2); U(0, 1) |
| FullPop 3 Peaks | `μ_g^(1,2,3)`; `σ_g^(1)`; `σ_g^(2,3)` | U(5, 150); U(0.4, 10); U(0.4, 15) M☉ |
| Rate | `γ`; `κ`; `z_p` | U(0, 12); U(0, 6); U(0, 4) |

The rendering of the GWTC-4.0 paper read here has narrower widths for the
same models: `σ_g^low` U(0.4, 5) and `σ_g^high` U(0.4, 10) in MLTP and
FullPop-4.0, `δ_m^max` LU(10⁻³, 1) in FullPop-4.0, and `μ_g` U(20, 50) in PLP
[src: arXiv:2509.04348, Tables 3–5]. The GWTC-5.0 text states nonetheless "We
do not change our priors from previous studies" and that "significantly
extending the prior range of the population parameters could alter the
reconstructed mass spectra", a possibility it does not consider [src:
arXiv:2605.27227, Sect. V.2]. Which version of each table is final was not
checked; compare the tables of the versions you cite.

### Step 3. Choose the rate evolution
<!-- key: step-3-choose-the-rate-evolution -->

```
ψ(z | γ, κ, z_p) = [1 + (1 + z_p)^(−γ−κ)] (1 + z)^γ / {1 + [(1 + z)/(1 + z_p)]^(γ+κ)}   (A.2)
```

[src: arXiv:2605.27227, App. A, Eq. A.2.] The reason given for a
Madau–Dickinson form rather than the plain `(1 + z)^γ` of population papers:
"when varying the cosmology, a GW event at given distance can be associated
with a redshift which is significantly higher than the one corresponding to
the fiducial cosmology", and Eq. A.2 makes the rate decay after `z_p`; wide
priors on `γ` and `κ` stand in for a convolution with delay times [src:
same]. The second blinded challenge injects the delay-time convolution
explicitly [src: arXiv:2604.26273, Sect. III, Eq. 1–3]:

```
R(z) = R0 ∫_z^∞ P_t(t_d) R_SFR(z_f) (dt/dz_f) dz_f / ∫_0^∞ P_t(t_d) R_SFR(z_f) (dt/dz_f) dz_f
P_t(t_d) ∝ t_d^(−d)  for t_d^min < t_d < t_d^max
```

### Step 4. Decide whether the mass scales may evolve
<!-- key: step-4-decide-whether-the-mass-scales-may-evolve -->

Two parametrisations are in use.

- **Linear.** Every mass parameter `x(z) = x0 + z ε_x` (blinded challenges,
  arXiv:2412.14244 Sect. III.2; arXiv:2604.26273 Sect. III) [src].
- **Sigmoid.** For a hyperparameter `φ` (arXiv:2605.20112, following
  its ref. [33]) [src: Sect. II.1, Eq. 3–5]:

  ```
  φ(z) = φ0 + (φ∞ − φ0) S((z − z_φ)/Δz_φ),   S(x) = ½ [1 + tanh x]
  λ(z) = [1 − S((z − z_λ)/Δz_λ)] λ0 + S((z − z_λ)/Δz_λ) λ∞      (weights stay on the simplex)
  ```

  applied to `α1, α2, m_b, μ1, σ1, μ2, σ2` of a broken power law with two
  peaks. Only the primary-mass features evolve, because they are "the most
  robustly identified structure"; `m_min` and `m_max` stay fixed because edge
  parameters "are constrained only by the subset of events close to those
  edges" and are sensitive to Monte Carlo variance [src: Sect. II.1]. Priors:
  `Δφ = φ∞ − φ0` zero-mean normal, `z_φ` uniform on [0.05, 1.5], `Δz_φ` in
  [0.05, 2] sampled in log, Dirichlet weights, and logistic transforms of
  bounded variables "improving Hamiltonian Monte Carlo geometry" [src: Sect.
  II.2]. Total 45 hyperparameters: 2 cosmological (`H0`, `Ω_m`), 3 rate, 15
  mass, 21 shape evolution, 4 weight evolution [src: Sect. II.1].

GWTC-5.0 does not evolve the spectrum; it argues that "cosmological effects
imprint a coherent and predictable modulation on the mass spectrum observed
across different redshifts", which appropriate modelling should separate
from astrophysical evolution, and recommends data-driven approaches for the
future [src: arXiv:2605.27227, Sect. V.2].

### Step 5. Or drop the parametric form
<!-- key: step-5-or-drop-the-parametric-form -->

- **Gaussian process** (Farah et al., arXiv:2404.02210): the hyperparameters
  are the rate at each posterior sample's and each found injection's source
  mass; the Gaussian process is the prior on them, its kernel parameters
  ("hyper-hyper-parameters") fitted with the rest; cosmological priors
  uniform, H0 on U(30, 120). At the edges, where data are absent but the
  detectors are sensitive, it learns a low rate; where neither data nor
  sensitivity exist (below about 5 and above about 100 M☉) it reverts to
  the prior, which "is uninformative for the `H0` constraint" [src: Sect.
  II.3]. On 1000 simulated O5-like events: 5.8% on H0 with the other
  cosmological parameters fixed, 6.4% on `H(z = 0.9)` [src: abstract].
  **forecast**.
- **B-splines** with adaptive knots (arXiv:2601.03347): three peaks near 10,
  18 and 33 M☉ in 137 GWTC-4.0 BBH, Bayes factors up to 226 over parametric
  models, 12–21% tighter H0, best 57.8 (+21.9/−20.6) [src: abstract].
- **B-splines in `log m`** with fixed knots (arXiv:2604.14290): H0 by number
  of splines and spacing, below [src: Sect. IV].
- **Power laws only** (arXiv:2603.06792): linear combinations of truncated
  power laws give H0 = 53.3 (+14.0/−10.8) at 68% on GWTC-4.0 [src: abstract].

### Step 6. Validate on blinded mocks
<!-- key: step-6-validate-on-blinded-mocks -->

The blinded challenges separate a simulation team and an analysis team under
a coordinator; ten injection sets per threshold are drawn by at least three
members with population and cosmology from uniform ranges, one is chosen at
random, and its parameters stay hidden until the analysis ends
(arXiv:2412.14244) [src: Sect. II]. Settings and outcomes:

| Challenge | Truth | Data | Analysis model | Outcome | Place read |
|---|---|---|---|---|---|
| MDC-I vanilla | PLP, no evolution, H0 = 67.8 | O1–O4 noise, 3 yr, SNR > 10, 286 events, 10⁶ injections | PLP, `icarogw` | H0 = 62.08 (+28.07/−21.15); `α`, `m_min`, `σ_g`, `γ` within 2σ | arXiv:2412.14244, Sect. II, V.1 |
| MDC-I redshift-dependent | PLP with `μ_g = 40.9 + 2.84 z`, `σ_g = 7.63 + 2.70 z`, a high H0 by design | O4 noise, 1 yr, SNR > 12, 80 events, up to `z = 1.7` | PLP without evolution | true H0 outside about the 90% interval; `μ_g`, `σ_g` agree with the truth at each `z` within about 68% | arXiv:2412.14244, Sect. III.2, V.2 |
| MDC-II | linear evolution of all mass parameters plus a delay-time rate | O4 noise, `bilby` with IMRPhenomPv2, spins zero | PLP without evolution, 14 hyperparameters, H0 U(10, 250), `Ω_m` U(0.1, 0.9) | evolution of 40–50% over `z ∈ [0, 1]` biases H0 by about 60% | arXiv:2604.26273, Sect. III, IV.2, V.1 |

The SNR threshold of the evolving case was raised to 12 "to make sure that
the contamination from noise fluctuation is not significant", so that the
systematic is seen over the statistical error [src: arXiv:2412.14244, Sect.
II]. In both MDC-I runs `μ_g` and `σ_g` are the parameters most correlated
with H0, negatively: "higher values of `μ_g` suggest a more massive BBH
population, leading to lower inferred redshifts and a lower `H0`" [src: Sect.
V.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Number and form of features
<!-- key: number-and-form-of-features -->

| Choice | H0 (68%) | Data | Place read |
|---|---|---|---|
| LVK multi-peak, spectral only (reference for the comparisons below) | 77.1 (+40.8/−26.3) | GWTC-4.0 | arXiv:2605.20112, Sect. III.3, quoting arXiv:2509.04348 |
| `log m` splines, 10 / 12 / 14 / 16 knots | 64.20 (+18.75/−13.36) / 62.66 (+16.22/−11.24) / 68.40 (+17.57/−12.47) / 50.26 (+16.30/−8.00) | GWTC-4.0 | arXiv:2604.14290, Sect. IV |
| uniform-knot splines, 10 / 12 | 81.19 (+28.41/−18.39) / 75.93 (+21.13/−15.43) | GWTC-4.0 | same |
| 18 and 20 `log m` splines | about 180 | GWTC-4.0 | same |
| 10 M☉ subpopulation only (24 events, median `m1 < 13` M☉), 4 splines / single power law | 58.60 (+26.92/−20.85) / 48.35 (+28.66/−17.16) | GWTC-4.0 | arXiv:2604.14290, Sect. V |

Shifts relative to the LVK multi-peak result collected by Agapito et al.
[src: arXiv:2605.20112, Table 2]: B-splines 0.05–0.7σ (4–25 km s⁻¹ Mpc⁻¹);
third peak near 60 M☉ about 0.04σ (about 2); sharper features 0.3–0.8σ
(12–26); splines and subpopulations below 0.1 to 0.8σ (a few to 25), with the
most extreme spline runs up to about 2.5σ. What the extra freedom buys and
costs, in the authors' words: with too many spline degrees of freedom "the
additional degrees of freedom introduced by cosmological parameters are
effectively used to compress the population reconstruction, clustering
events into a small number of sharp peaks" [src: arXiv:2604.14290, Sect. IV];
"Determining the appropriate amount of allowed variability ... remains an
open problem" [src: arXiv:2605.20112, Sect. III.3]. Which features carry the
weight: a sharper high-mass cut-off moves H0 towards about 70, a sharper
10 M☉ peak tightens it; the high-mass regime is "particularly problematic"
because few events populate it [src: arXiv:2604.14290, Sect. IV].

### BBH-only or full population
<!-- key: bbh-only-or-full-population -->

FullPop models add the neutron-star mass scales and the gap; GWTC-5.0 keeps
FullPop-4.0 as fiducial although FullPop 3 Peaks is slightly preferred, "so
our results remain comparable" with GWTC-4.0 [src: arXiv:2605.27227, Sect.
V.2]. The subpopulation route goes the other way: 24 low-mass events give
40% on H0 against 44% for the full LVK BBH population, and their rate slope
`γ = 11.63 (+7.19/−4.74)` differs from the full-sample `γ = 3.73
(+0.66/−0.60)` (free cosmology), which suggests that "uniform BBH properties
across the full population may be oversimplified" [src: arXiv:2604.14290,
Sect. V]. The cut at 13 M☉ "may be affected by event misclassification"
[src: same].

### Spins modelled or not
<!-- key: spins-modelled-or-not -->

On the multi-peak model, modelling spins widens the H0 error by 8.8%
(Gaussian spin model) or 5.3% (Transition model), and the Transition model
is preferred at `log10 B = 3.16 ± 0.10` [src: arXiv:2605.27227, Sect. V.2;
priors in Tables 9–10]. Agapito et al. checked that a Gaussian spin model has
"no impact" on their result [src: arXiv:2605.20112, Sect. II.1, footnote 2].

### Evolving or not
<!-- key: evolving-or-not -->

On GWTC-4.0 with free `H0` and `Ω_m` (median, 68%; 90% in parentheses)
[src: arXiv:2605.20112, Table 1]:

| Model | H0 | Shift |
|---|---|---|
| Non-evolving broken power law + 2 peaks | 64.8 (+21.1/−18.1) (+37.2/−28.2) | — |
| Evolving | 56.4 (+23.2/−17.1) (+42.6/−26.2) | −0.30σ, 8.42 |
| Evolving, tight priors on `α1`, `α2` | 57.2 (+22.9/−16.5) | −0.27σ |
| Evolving, tight priors on `μ1`, `σ1` | 57.3 (+21.0/−16.0) | −0.28σ |
| Evolving, tight priors on `μ2`, `σ2` | 65.8 (+20.2/−18.4) | +0.04σ |
| Evolving, tight priors on all | 66.9 (+20.0/−16.9) | +0.08σ |

The shift is defined as the difference of medians over the quadrature sum of
the mean 68% half-widths. Fixing the high-mass peak removes it, fixing the
low-mass peak does not [src: Sect. III.3]. A KL-divergence test between
`p(m1 | z)` at `z = 0.2` and `z = 1` finds 94% of realisations compatible
with no evolution [src: same]. In injections from a non-evolving population
(150 O4-like events) the evolving model reproduces the low shift; with 1000
O5-like events the trend partly reverses to higher H0, as the 35 M☉ feature
becomes "constrained directly by the data, rather than by the prior" [src:
Sect. III.4]. The authors read this as evidence that the shift is
"compatible with overflexibility, not as evidence that the real data are
stationary" [src: same].

### Parametric or non-parametric
<!-- key: parametric-or-non-parametric -->

An incorrect parametric model produces "a systematic bias in cosmological
inference, not an increase in statistical uncertainty": on 50 mocks drawn
from PLP, PLP recovers H0 symmetrically, a broken power law favours higher
H0; "it is not possible in practice to know which direction an incorrect
parametric model will bias `H0`" (arXiv:2404.02210) [src: App. D]. The
flexible models pay with prior-dominated edges (Gaussian process) or with
the compression failure mode (splines, above).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Hyperparameters, sigmoid-evolving model | 45 | GWTC-4.0 | arXiv:2605.20112 | Sect. II.1 |
| Hyperparameters, MDC analyses | 14 | mocks | arXiv:2604.26273 | Sect. IV.2 |
| H0 prior | U(10, 200) (LVK GWTC-5.0, physics file); U(30, 120) (Gaussian process mocks); U(10, 250) (MDC) | — | arXiv:2404.02210; arXiv:2604.26273 | Sect. II.3; Table 2 |
| Evolution transition range | `z_φ ∈ [0.05, 1.5]`, `Δz_φ ∈ [0.05, 2]` | GWTC-4.0 | arXiv:2605.20112 | Sect. II.2 |
| Spin-model widening of the H0 error | 8.8% (Gaussian), 5.3% (Transition) | GWTC-5.0 MLTP | arXiv:2605.27227 | Sect. V.2 |
| Injected evolution, MDC-I | `μ_g = 40.9 + 2.84 z`, `σ_g = 7.63 + 2.70 z` M☉ | mocks | arXiv:2412.14244 | Sect. V.2 |
| Evolution that biases H0 by about 60% | 40–50% over `z ∈ [0, 1]` | mocks | arXiv:2604.26273 | Sect. V.1 |
| Statistical precision needed for the tension | about 2% (about 5σ on an 8% discrepancy); mass-spectrum systematics well below it | argument | arXiv:2604.26273 | Sect. V.1, footnote 1 |
| Subpopulation precision | 40% (24 events) against 44% (full BBH, LVK) | GWTC-4.0 | arXiv:2604.14290 | Sect. V |

## What goes wrong
<!-- key: what-goes-wrong -->

- **The evolving model fitted to a stationary truth shifts H0.** Shown on
  injections (above); the sign may change with sensitivity (arXiv:2605.20112)
  [src: Sect. III.4]. Test: run the evolving and non-evolving models on
  injections from both, at the catalogue's sensitivity.
- **Unmodelled evolution biases H0 beyond the interval.** MDC-I and MDC-II
  (Step 6). The diagnostic used in MDC-I: compare the reconstructed
  `p(m1)` in three redshift bins (`z < 0.65`, `0.65–1.05`, `≥ 1.05`, chosen
  for similar numbers of events) with the model evaluated at the bin centres
  [src: arXiv:2412.14244, Sect. V.2].
- **Flexibility compresses the population.** Many splines with free
  cosmology give H0 near 180 (Choices). Test: compare the reconstructed
  spectrum at free and at fixed cosmology; a spectrum that sharpens when H0 is
  freed is a warning [src: arXiv:2604.14290, Sect. IV].
- **Edge parameters drive the answer.** H0 is sensitive "primarily through
  features at the population boundaries" (arXiv:2604.14290) [src: abstract];
  two lowest-mass events created multimodality in `m_min`, handled by
  truncating its prior at 7 M☉ [src: Sect. V]. Test: drop the extreme events
  and refit.
- **Priors on the peaks change the model ranking.** Narrowing the peak
  priors raises the Bayes factor between two GWTC-4.0 models from
  `log10 B = 0.30` to 2.3 (`systematics.md`); prior widths differ between
  the two LVK papers read here (Step 2). Test: refit with the other paper's
  priors.
- **Confirmation bias.** The MDC injected a high H0 deliberately to check
  for it and found it did not drive the inference [src: arXiv:2412.14244,
  Sect. III.2]. LVK H0 analyses are not blinded (L2).

## Reading list
<!-- key: reading-list -->

- Method, models and priors: LVK GWTC-4.0 cosmology, arXiv:2509.04348, App.
  C — equations of PLP, MLTP, FullPop-4.0.
- Method, current priors: LVK GWTC-5.0 cosmology, arXiv:2605.27227, App. A
  and Sect. V.2.
- Method, evolution: Agapito et al. 2026, arXiv:2605.20112 — sigmoid
  evolution, injections, comparison of systematics.
- Method, non-parametric: Farah et al. 2024, arXiv:2404.02210 — Gaussian
  process mass model; App. D on parametric bias.
- Application, flexible: Gennari et al. 2026, arXiv:2604.14290 — splines,
  compression failure, subpopulation.
- Application, flexible: Tagliazucchi et al. 2026, arXiv:2601.03347;
  Bertheas et al. 2026, arXiv:2603.06792.
- Validation: blinded challenges, arXiv:2412.14244 and arXiv:2604.26273.
- Foundation: Ezquiaga & Holz 2022, arXiv:2202.08240 (L2).

## Not verified
<!-- key: not-verified -->

- Which arXiv version carries the GWTC-4.0 prior tables quoted in Step 2.
- The PowerLaw–Dip–Break papers that FullPop-4.0 extends, and the evolution
  form of its ref. [33] (Lalleman et al. 2025), seen only as references in
  arXiv:2605.20112.
- The number of events and injected parameter values of MDC-II (its Table 1
  was not read).
- The ET science case and Zhao et al. sections named in "From".
- The Bayes factors of Table 2 of arXiv:2605.27227.
