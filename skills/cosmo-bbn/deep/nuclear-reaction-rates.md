# Nuclear reaction rates for BBN — cosmo-bbn dossier

Scope: how a thermonuclear rate for d(p,γ)³He, d(d,n)³He and d(d,p)t is
built from laboratory S-factor data (energy window, dataset selection,
normalisation errors, fitting function, propagation into a BBN code and a
likelihood), and what each of the four current approaches — ab-initio
shapes, Bayesian shapes, polynomials, Gaussian processes — assumes and
costs.
Snapshot: 2026-10-17.
From: Cooke 2024, Sect. 4.1; Grohs & Fuller 2023, Sect. 3; LUNA,
Felsenkeller, n_TOF and Trojan-Horse experiment lists.

Already in L2, not repeated here: which rates dominate each nuclide and the
table of rate evaluations in
`physics-and-methods.md#nuclear-reaction-rates`; the Ω_b h² shifts between
rate sets in `results.md#code-and-rate-comparisons` and
`systematics.md#nuclear-rates`; compressed versus marginalised likelihoods
in `physics-and-methods.md#from-abundances-to-parameters`; the laboratories
in `surveys-and-data.md#nuclear-physics-laboratories`; the d(p,γ)³He
experiment–theory offset in
`open-questions.md#the-d-p-gamma-3he-rate-experiment-versus-ab`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. From cross section to rate
<!-- key: step-1-from-cross-section-to-rate -->

For a non-resonant charged-particle reaction i + j the thermal average is

    ⟨σv⟩(T) = √(8/(π μ_ij)) T^{−3/2} ∫₀^∞ dE E σ(E) e^{−E/T}     (Eq. 3)

and the astrophysical S-factor removes the Coulomb penetrability,

    S(E) ≡ σ(E) E e^{√(E_G/E)},  E_G ≡ 2π² μ_ij (Z_i Z_j α)²     (Eq. 4)

with μ_ij the reduced mass, E the centre-of-mass kinetic energy, Z the
charges, α the fine-structure constant and T in energy units (Pisanti et
al. 2021, arXiv:2011.11537) [src: Sect. 2]. The equivalent form used by
Launders et al. is R(T) = N_A⟨σv⟩ =
√(8/(π μ₁₂)) N_A (k_B T)^{−3/2} ∫ dE e^{−2πη} S(E) e^{−E/k_BT}
(arXiv:2604.16600, Eq. 9) [src: Sect. I.1], where η in the exponent is the
Coulomb (Sommerfeld) parameter, not the baryon-to-photon ratio [der: the
exponent e^{−2πη} plays the role of e^{−√(E_G/E)} in Eq. 4 of
arXiv:2011.11537].

Integration limits matter: Coc et al. found that integrating over the Gamow
window E₀ ± 2ΔE₀ is "not sufficient to reach the high precision needed",
that n ≳ 3 is required, and used n = 4 [src: arXiv:1511.03843, Sect. IV].

### Step 2. Fix the energy window
<!-- key: step-2-fix-the-energy-window -->

| Source | Window | How it was set |
|---|---|---|
| Coc et al. 2015 (PRIMAT) | 0.015 ≤ E ≤ 0.6 MeV for d + d; theory replaced above 2 MeV (d(p,γ)) and 0.6 MeV (d + d) | electron screening below, nuclear-model limits above; Arai et al. theory includes partial waves only to J = 2 and underestimates data above ~1 MeV [src: arXiv:1511.03843, Sects. III, IV] |
| Pisanti et al. 2021 (PArthENoPE) | relevant range ~10–400 keV; D/H sensitive mainly to 20–240 keV, peak ~80 keV | sensitivity function σ(E) = (δD/H / D/H)(S/δS) per 10 keV bin over 10–500 keV (Eq. 12) [src: arXiv:2011.11537, Sects. 2, 3.4] |
| Yeh et al. 2021 | fit 2 keV–2 MeV for d(p,γ)³He | "encompasses the BBN range" [src: arXiv:2011.13874, Sect. II] |
| Launders et al. 2026 | 0.014–0.6 MeV | defined against the current D/H observational precision; GP hyperparameters are constant over the range, so a narrower range strains them less [src: arXiv:2604.16600, Sects. I.2, III.2] |

Launders et al. note there is "no consensus": Leonard et al. claim data to
~2.75 MeV are needed for the integral to converge beyond T = 2 GK, while
Pisanti et al. find the important range ends at 0.24 MeV
[src: arXiv:2604.16600, Sect. III.2]. Low-energy d + d data are affected by
electron screening, especially d(d,p)t [src: same].

### Step 3. Select datasets
<!-- key: step-3-select-datasets -->

Two axes separate the networks: dataset selection and fitting procedure;
PRIMAT is the most selective, PArthENoPE and PRyM/YOF include roughly the
same number of datasets, not all the same ones (Akharman et al. 2026,
arXiv:2609.12065) [src: Sect. 2.1].

Launders et al.'s rules [src: arXiv:2604.16600, Sect. III.3]:

1. Exclude old (over half a century) datasets that overlap newer, more
   precise ones.
2. Exclude data outside the relevant energy range.
3. Exclude datasets with unknown correlations with other experiments.
4. Otherwise include.
5. If only total errors are given, take the smallest percentage error of the
   set as its normalisation error.

Their fiducial d + d data are five sets (KR87B, KR87M, BR90, GR95, Leo06)
with normalisation errors 6.4%, 8.12%, 1.3%, 3.3% and 1%; their d(p,γ)³He
data are six sets (MA97, SC97, CA02, TI19, LUNA 2020, TU21) [src: Table 3].
Disputed sets and the reasons given:

- **Schulte et al. 1972** (lowest point at 1.96 MeV): used by PArthENoPE
  and PRyM/YOF, excluded by PRIMAT [src: arXiv:2609.12065, Sect. 2.1].
  PRIMAT's reason: not to let extrapolation of the Arai et al. theory to
  high energy bias the fit; Akharman et al.'s reason: inconsistencies or
  systematics at high energy [src: same, footnote 2]. Its sub-percent
  errors were multiplied by 5 by Leonard et al. [src: arXiv:2604.16600,
  Sect. III.2].
- **Tumino et al. 2014 (Trojan Horse)**: normalisation taken from other
  datasets, hence "not independent of the others", and covariances not
  extractable; used by PArthENoPE and PRyM/YOF, excluded by PRIMAT and not
  recommended by Akharman et al. [src: arXiv:2609.12065, Sect. 2.1].
- **PArthENoPE's position**: "if there are no clear indication of large
  systematics in a particular experiment, we don't think it is worth
  neglecting any of available data, even those outside the BBN energy
  range" [src: arXiv:2011.11537, Sect. 3.3].

### Step 4. Fit the S-factor with normalisation errors
<!-- key: step-4-fit-the-s-factor-with-normalisation -->

All approaches give each dataset k a normalisation factor ω_k with prior
width ε_k (the quoted systematic), statistical errors σ_ik per point i.

**Ab-initio shape, fitted scale (PRIMAT; Coc et al. 2015).** The theory
shape F(E) is kept and scaled, because "the energy dependence is
essentially provided by the Coulomb functions, and is therefore more
reliable than the normalization" [src: arXiv:1511.03843, App. A]. Per
dataset, χ²(α_k) = Σ_i [S(E_ik) − α_k F(E_ik)]²/σ_ik² (Eq. 11) gives α̂_k
and σ_α̂;k (Eqs. 12–13); the recommended α is the weighted mean of the α̂_k
(Eq. 17) with σ²_α̂;k → σ²_α̂;k + ε_k² (Eq. 18). With the normalisation
error added, the reduced χ² was close to one, so no √χ² inflation was
applied [src: App. A.3]. Two alternatives were considered: a global fit
with error inflated by √χ² (Cyburt–Fields–Olive form, Eqs. 14–15) and the
D'Agostini joint fit of α and ω_k with MINUIT (Eq. 16) [src: Apps. A.1–A.2].

**Bayesian shape (Gómez Iñesta, Iliadis & Coc 2017).** Lognormal likelihood
for each S_i given f_n f_s S_th (Eqs. 2a–2c), with f_s an overall scale
under a truncated N(0, 100²) prior (Eq. 3) and f_n;k a per-dataset
normalisation under a lognormal prior of median 1 and width set by the
quoted systematic (Eq. 4); a robust-regression switch flags points with
over-optimistic errors and down-weights them [src: arXiv:1710.01647,
Sects. II.1–II.3]. Lognormal is chosen because S-factors are products of
measured quantities and cannot be negative [src: Sect. II.1].

**Polynomial (PArthENoPE; Pisanti et al. 2021).**

    χ²(a_l, ω_k) = Σ_{i_k} (S_th(E_ik, a_l) − ω_k S_ik)²/(ω_k² σ_ik²)
                   + Σ_k (ω_k − 1)²/ε_k²                           (Eq. 8)

with S_th a polynomial in E; the errors are rescaled by ω_k to avoid the
d'Agostini bias ⟨ω⟩ = 1/[1 + (n − 1)ε] of the plain covariance form
(Eqs. 5–7); the degree is raised until the reduced χ² stabilises, "typically
... 2-th or 3-th degree" [src: arXiv:2011.11537, Sect. 2]. When only total
errors exist, ε_k = max(σ_tot/S) [src: same]. Yeh et al. fit d(p,γ)³He with
a third-order polynomial, statistical and systematic errors in quadrature,
and an energy-independent discrepancy error that keeps χ²/dof ≤ 1
[src: arXiv:2011.13874, Sect. II].

**Gaussian process (Launders et al. 2026).** Joint Gaussian prior on S at
data and prediction energies (Eq. 7), with Σ holding total errors on the
diagonal and within-experiment normalisation correlations off-diagonal;
posterior mean and covariance by conditioning (Eq. 8); zero prior mean;
hyperparameters by cross-validation giving each dataset equal weight, so
that the most precise sets (BR90, Leo06) do not dominate; d(p,γ)³He fitted
in ln S because it rises nearly two orders of magnitude [src:
arXiv:2604.16600, Sects. I.1, III.1]. A small-ν Matérn component makes the
samples jagged; thermal averaging smooths them [src: Sect. III.1].

### Step 5. Turn the fit into a rate with an uncertainty
<!-- key: step-5-turn-the-fit-into-a-rate-with-an -->

- **Lognormal rate (PRIMAT).** N_A⟨σv⟩^k = exp(μ_k(T) + p_k σ_k(T)) with
  p_k ~ N(0, 1), exp(μ_k) the recommended rate and exp(σ_k) the factor
  uncertainty f.u. = √(rate_high/rate_low) ≈ 1 + Δα/α (Eqs. 3–5); abundance
  median and 68% interval from Monte Carlo quantiles [src:
  arXiv:1511.03843, Sect. IV]. These are 1σ limits, unlike NACRE and
  NACRE II [src: same].
- **One amplitude nuisance per reaction in the code.** In LINX each of the
  12 key reactions has an N(0, 1) amplitude parameter, plus τ_n sampled
  from 879.4 ± 0.6 s: 13 nuisance parameters [src: arXiv:2609.12065,
  Sect. 2.1]. "In both approaches [PArthENoPE and PRIMAT], uncertainties in
  D/H are parametrized by rescaling each relevant rate by a single
  parameter" [src: arXiv:2604.16600, Sect. I].
- **Function samples (GP).** 60 000 joint draws of the three GP rates (and
  overall scalings of the others) at fixed ω_b give the D/H mean and
  standard deviation; 100 000 when ω_b is marginalised; the other nine
  reactions from PRIMAT (switching to PArthENoPE moves D/H by ≲ 0.17%)
  [src: arXiv:2604.16600, Sects. I.1, I.3].

### Step 6. Put the rates into the likelihood
<!-- key: step-6-put-the-rates-into-the-likelihood -->

The full BBN likelihood used with LINX is

    ln L_BBN = −½ [ ((Y_P^BBN − Y_P^obs)/σ_Y)² + ((D/H − D/H^obs)/σ_D)² ]   (Eq. 2)

with the rate nuisances sampled alongside cosmology; Y_P^BBN ≡ 4n_He/n_B
is distinguished from the CMB helium mass fraction [src: arXiv:2609.12065,
Sect. 2.1]. The summarised alternative replaces the rate nuisances by a
fixed theory error σ̂_D^th from 4000 draws of the 12 nuisances at
(ω_b, N_eff) = (0.02237, 3.044), added in quadrature to σ_D^obs; τ_n is
still sampled [src: Sect. 3.2.3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Fitting function
<!-- key: fitting-function -->

- **Rigid theory shape.** Stable when datasets are dropped: for d(d,n)³He,
  PArthENoPE's polynomial changes strongly when high-energy data are
  excluded, while the theory-shaped PRIMAT fit does not [src:
  arXiv:2011.11537, Sect. 3.3]. Cost: relies on the theory being right in
  shape; the shape is "relatively inflexible" [src: arXiv:2609.12065,
  Sect. 2.1].
- **Polynomials.** Model-independent [src: arXiv:2011.13874, abstract].
  Cost, in Monte Carlo mocks with the real energies and errors: D/H bias
  (mean (pred − true)/σ_pred, Eq. 11) of 0.71–1.33 for degree-2 (d(d,p)t)
  and degree-4 (d(d,n)³He) polynomials against 0.32–0.50 for GPs;
  degree-2 d(d,p)t fits run high below 0.1 MeV and low above, even for a
  smooth truth; KL divergences ~5 (10) times and KS statistics ~2 (3) times
  larger than GPs for the theory (smoothed-GP) truth [src:
  arXiv:2604.16600, Sect. II].
- **Gaussian processes.** In the same mocks, truth inside 1σ in 66–69% and
  inside 2σ in ~95% of realisations, mean ≲ 0.5σ above truth; must
  extrapolate above ~0.3 MeV where d + d data end [src: arXiv:2604.16600,
  Sect. I.2]. Cost: non-parametric rates are not yet folded into a full
  cosmological inference [src: Sect. I.3].

### Penalty term per dataset or per point
<!-- key: penalty-term-per-dataset-or-per-point -->

Launders et al. state that the PArthENoPE network includes N_k penalty
terms per dataset, i.e. χ² of their Eq. 30, and that this is no longer a
maximum a posteriori estimate; in a single-experiment toy it gives
σ_ω² ≈ ε²/N (Eq. 34), so datasets with many points (75 for TU14, 50 for
RG85 against 6 for Leo06) get their normalisation errors underestimated
[src: arXiv:2604.16600, Supplement III.2]. Their own Eq. 13 has one penalty
per dataset, which equals the printed Eq. 8 of Pisanti et al.; Launders et
al. thank the PArthENoPE author for pointing out "a typo in Eq. (8)" of
their ref. [11] [src: arXiv:2604.16600, Sect. II, footnote 3]. A reader
should therefore not take the printed Eq. 8 as the code's χ² without
checking.

### Dataset selection, same fitting method
<!-- key: dataset-selection-same-fitting-method -->

Refitting PArthENoPE's polynomials with only PRIMAT's datasets reproduces
the PRIMAT d(d,p)t rate closely, "showing that the main source of
difference ... is due to the data selection criterium"; for d(d,n)³He the
fitting function matters more [src: arXiv:2011.11537, Sect. 3.3].

### Resulting D/H, same code, same ω_b
<!-- key: resulting-d-h-same-code-same-omegab -->

With LINX at the Planck ω_b [src: arXiv:2604.16600, Table 2]:

| Network | 10⁵ D/H | Against 2.527 ± 0.030 |
|---|---|---|
| Gaussian process | 2.442 ± 0.040 | 1.70σ |
| PRIMAT | 2.444 ± 0.037 | 1.74σ |
| PArthENoPE | 2.512 ± 0.042 | 0.29σ |
| PRyM/YOF | 2.520 ± 0.104 | 0.06σ |

PRyM/YOF uses LUNA for d(p,γ)³He and NACRE II for d + d; its agreement
is "largely a byproduct of the large uncertainty" [src: Sect. II,
Table 2]. LINX's "key_YOF" network does not include the later Yeh et al.
2022 polynomial fits for d(d,n)³He and d(d,p)t [src: arXiv:2609.12065,
Sect. 2.1, footnote 3]. Akharman et al. adopt PRIMAT as fiducial because of
the GP validation [src: Sect. 2.1].

### Full likelihood or summary
<!-- key: full-likelihood-or-summary -->

A Gaussian ω_b prior from D/H loses the ω_b–N_eff correlation and reverses
the ordering of N_eff across networks; the fixed-theory-error D/H summary
reproduces the full posterior approximately, with a ~15% of σ difference in
the upper N_eff bound for PRyM/YOF [src: arXiv:2609.12065, Sect. 3.2.3].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| D/H sensitivity to d + d rates | ΔD/H/D/H = −0.54 Δ⟨σv⟩_ddn/⟨σv⟩ − 0.46 Δ⟨σv⟩_ddp/⟨σv⟩; < 2% precision needed | PRIMAT rates | arXiv:1511.03843 | Sect. III, Eq. 2 |
| Gamow-window integration | n ≳ 3 needed, n = 4 used | Coc 2015 | arXiv:1511.03843 | Sect. IV |
| D/H error per rate (1σ, one at a time) | 10⁵σ_D: dpγ 0.027 (58.5%), ddn 0.018 (26.9%), ddp 0.013 (14.2%), pnγ 0.002 (0.3%) | PArthENoPE 2021 | arXiv:2011.11537 | Table 1 |
| Same before LUNA | dpγ 0.062 (87.0%), ddn 0.020, ddp 0.013 | PArthENoPE earlier | arXiv:2011.11537 | Table 1 |
| D/H sensitivity window | 20–240 keV, peak ~80 keV | PArthENoPE | arXiv:2011.11537 | Sect. 3.4 |
| Normalisation errors, d + d sets | 6.4%, 8.12%, 1.3%, 3.3%, 1% | KR87B, KR87M, BR90, GR95, Leo06 | arXiv:2604.16600 | Table 3 |
| Turkat 2021 d(p,γ) | 8% and 5% per target plus a shared 12% | GP fit | arXiv:2604.16600 | Table 3 |
| Polynomial degree | 2–3 (PArthENoPE general); 2 (ddp), 4 (ddn) | PArthENoPE | arXiv:2011.11537; arXiv:2604.16600 | Sect. 2; Sect. II |
| D/H bias in mocks | 0.32–0.50 (GP) vs 0.71–1.33 (polynomial) | Launders 2026 | arXiv:2604.16600 | Sect. II |
| GP coverage | 66–69% within 1σ, ~95% within 2σ | Launders 2026 | arXiv:2604.16600 | Sect. I.2 |
| Nuisance parameters in LINX | 12 rate amplitudes N(0, 1) + τ_n = 879.4 ± 0.6 s | Akharman 2026 | arXiv:2609.12065 | Sect. 2.1 |
| d(p,γ)³He nuisance shift in BAO + BBN + CMB | nearly 1σ (PRIMAT), > 0.5σ (PArthENoPE) | Akharman 2026 | arXiv:2609.12065 | Sect. 3.2.1 |
| Draws for summarised theory error | 4000 at (0.02237, 3.044) | Akharman 2026 | arXiv:2609.12065 | Sect. 3.2.3 |
| Scale-factor prior | f_s ~ N(0, 100²) truncated at 0; f_n lognormal, median 1 | Gómez Iñesta 2017 | arXiv:1710.01647 | Eqs. 3–4 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Many-point datasets dominating.** Shows as ω_k pinned near 1 for large
  sets [src: arXiv:2604.16600, Supplement III.2]. Test: refit with one
  penalty per dataset and compare ω_k distributions on mocks.
- **Data outside the window steering the fit.** Shows as a d(d,n)³He rate
  that moves when high-energy sets are dropped [src: arXiv:2011.11537,
  Sect. 3.3]. Test: refit with and without the out-of-window sets.
- **Non-independent datasets.** Trojan-Horse data normalised to other
  datasets double-count them [src: arXiv:2609.12065, Sect. 2.1]. Test:
  exclude, or include only with the cross-covariance.
- **Underestimated normalisation errors.** Shows as χ²_ν ≫ 1 across sets;
  PRIMAT found χ²_ν ≈ 1 once ε_k was added [src: arXiv:1511.03843,
  App. A.3]; Gómez Iñesta et al. down-weight outliers instead
  [src: arXiv:1710.01647, Sect. II.3].
- **Electron screening in low-energy data.** Biases d(d,p)t most [src:
  arXiv:2604.16600, Sect. III.2]. Test: a low-energy cut (15 keV in PRIMAT
  and the GP analysis).
- **Fit method bias not checked.** Test: inject a known S_true with the
  real energies and errors (their Eq. 10), refit, and measure bias and
  coverage of D/H (Eq. 11) [src: arXiv:2604.16600, Sect. I.2].
- **Rate tension read as cosmology.** Posterior shifts of the d(p,γ)³He
  nuisance in joint fits show the abundance data constrain the rate more
  than the laboratory does in ΛCDM [src: arXiv:2609.12065, Sect. 3.2.1].
  Report nuisance posteriors against their priors.
- **Narrow integration window.** E₀ ± 2ΔE₀ is too narrow at this precision
  [src: arXiv:1511.03843, Sect. IV].

## Reading list
<!-- key: reading-list -->

- Foundation: Coc et al. 2015, arXiv:1511.03843 — theory-shaped S-factors,
  normalisation options, lognormal rates.
- Method: Gómez Iñesta, Iliadis & Coc 2017, arXiv:1710.01647 — Bayesian
  S-factor fits with normalisation priors and robust regression.
- Method/application: Pisanti et al. 2021, arXiv:2011.11537 — polynomial
  χ² with normalisation factors, sensitivity window, error budget.
- Application: Yeh, Olive & Fields 2021, arXiv:2011.13874 — polynomial
  d(p,γ)³He with discrepancy error.
- Method/critique: Launders, Giovanetti & Liu 2026, arXiv:2604.16600 —
  Gaussian processes, dataset rules, mock validation of all methods.
- Application: Akharman et al. 2026, arXiv:2609.12065 — networks compared,
  dataset recommendations, nuisance posteriors, full versus summarised
  likelihood.

## Not verified
<!-- key: not-verified -->

- The PArthENoPE code's actual χ² (one penalty per dataset as printed in
  arXiv:2011.11537, Eq. 8, or N_k penalties as stated in
  arXiv:2604.16600): the code was not inspected.
- The Arai et al. 2011 four-nucleon calculation, NACRE II and the Tumino
  et al. 2014 Trojan-Horse data: cited through the papers above, not read.
- The temperature dependence of the PRyMordial rate nuisances: not read in
  arXiv:2307.07061 for this dossier.
- The ω_b column of arXiv:2604.16600, Table 1 was not copied; check it at
  source before use.
