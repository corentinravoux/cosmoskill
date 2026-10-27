# Galactic foreground component separation for r — cosmo-inflation-primordial dossier

Scope: how a B-mode analysis removes polarised dust and synchrotron before
fitting r (cross-spectrum parametric, blind needlet ILC, map-based
parametric), what each pipeline fits and assumes, how foreground residuals
are carried into the r likelihood, and what was found when the pipelines
were run on the same simulations.
Snapshot: 2026-10-17.
From: Achúcarro et al. 2022 review (arXiv:2203.08128), Sect. 2.2.1
(measurement challenges); SO science goals (arXiv:1808.07445), Sects. II.4.4
and III.4.3 (foreground complexity); LiteBIRD 2022 (arXiv:2202.02773),
Sect. 5.2 (foreground cleaning).

Already in L2, not repeated here: the BK18 eight-parameter model, its
priors and its foreground budget (`systematics.md#b9-bk18-budget-as-read-in-the-paper-body`);
the SO bias on r from dust complexity and the d10/s5 findings
of Liu et al. (`systematics.md#b1-polarised-galactic-dust`); synchrotron in
BK18 (`systematics.md#b2-synchrotron`); beam chromaticity
(`systematics.md#b5-beam-chromaticity-and-bandpass`); the six-SAT forecast
table (`systematics.md#b11-so-six-sat-forecast-how-sigma-r-moves`); the
moment expansion as a concept (`physics-and-methods.md#component-separation-for-the-next-generation`).

## How it is done
<!-- key: how-it-is-done -->

The three families below are the ones the Simons Observatory (SO) runs side
by side on its Small Aperture Telescope (SAT) data, and the ones LiteBIRD
names [src: arXiv:2302.04276, Sect. 2; arXiv:2202.02773, Sect. 5.2.3].
Notation: ν a frequency channel, ℓ a multipole, D_ℓ = ℓ(ℓ+1)C_ℓ/2π,
A_lens the amplitude of the lensing B-mode spectrum relative to ΛCDM
(A_lens < 1 after delensing), f_sky the effective sky fraction.

### Step 1. Measure B-mode spectra on a cut sky
<!-- key: step-1-measure-b-mode-spectra-on-a-cut-sky -->

All three SO pipelines estimate spectra with the pseudo-C_ℓ method of
NaMaster and use B-mode purification, because a mask creates "ambiguous"
modes contaminated by full-sky E modes that must be removed at map level
[src: arXiv:2302.04276, Sect. 2.1]. The SO set-up: the SAT hits map
apodised with a C1 kernel of 10°, f_sky ≈ 10%, bandpowers of Δℓ = 10, and
30 ≤ ℓ ≤ 300 kept. The reasons given: larger scales are expected to be
contaminated by atmospheric noise and filtering on real data, smaller ones
carry no primordial signal [src: same].

Noise bias is removed by cross-correlating data splits rather than by
subtracting a noise model: S = 4 splits, averaging the S(S−1)/2
unequal-split pairs, giving N(N+1)/2 noise-debiased spectra for the N
channels. The stated reason is that a noise model accurate enough may not
exist on real data; a wrong noise model then only inflates σ(r) through
the covariance, while the cross-split estimate keeps r unbiased [src:
arXiv:2302.04276, Sect. 2.1].

### Step 2a. Cross-spectrum parametric fit ("pipeline A", BBPower)
<!-- key: step-2a-cross-spectrum-parametric-fit-pipeline -->

The data vector is the set of all cross-frequency spectra C_ℓ^{νν′}, as in
BICEP/Keck; the likelihood compares it with the map-level sky model
propagated to spectra [src: arXiv:2302.04276, Sect. 2.1]. Fiducial model:
foreground angular spectra D_ℓ = A_c (ℓ/ℓ_0)^{α_c}, ℓ_0 = 80, c = d (dust)
or s (synchrotron); dust SED a modified black body with index β_d and
temperature fixed to 20 K; synchrotron a power law of index β_s; a
dust–synchrotron correlation ε_ds. With r and A_lens, nine free parameters
{A_lens, r, A_d, α_d, β_d, A_s, α_s, β_s, ε_ds} (Eq. 1) [src: same].

The moment extension adds the leading effect of spatially varying spectral
indices. Expanding the SED to second order in δβ (the deviation of the
index from its mean) splits each cross-spectrum into 0×0, 0×1, 1×1 and 0×2
terms (Azzoni et al. 2021, arXiv:2011.11575, Eqs. 10–14). Three
assumptions reduce it to two extra spectra per component: no correlation
between components in the higher-order terms; Gaussian fields, which
cancels the 0×1 term; amplitudes uncorrelated with index fluctuations. The
authors state each is known to be wrong at some level and treat the
neglected correlations as higher order [src: arXiv:2011.11575, Sect. 2.2].
What remains (Eqs. 15–18):

- C_ℓ^{νν′}|_{0×0}: the usual dust, synchrotron and cross terms with mean
  SEDs S̄_ν^c;
- C_ℓ^{νν′}|_{1×1} = Σ_c ∂_β S̄_ν^c ∂_β S̄_ν′^c Σ_{ℓ1ℓ2} [(2ℓ1+1)(2ℓ2+1)/4π]
  (Wigner 3j)² C_{ℓ1}^{cc} C_{ℓ2}^{β_c}: the amplitude spectrum convolved
  with the spectrum of the index map;
- C_ℓ^{νν′}|_{0×2} = Σ_c ½ [S̄_ν^c ∂²_β S̄_ν′^c + (ν↔ν′)] C_ℓ^{cc} σ²_{β_c},
  with σ²_{β_c} = Σ_ℓ (2ℓ+1)/4π C_ℓ^{β_c} (Eq. 19).

The index spectrum is a power law C_ℓ^{β_c} = B_c (ℓ/ℓ_0)^{γ_c} (Eq. 21),
so the moment model has 13 parameters (Eq. 23): the nine above plus B_d,
γ_d, B_s, γ_s [src: arXiv:2011.11575, Sect. 2.2]. SO's six-SAT forecast
uses exactly this "minimal" expansion, with the four extra parameters, and
labels its two cases "no FG decorr." and "with FG decorr." [src:
arXiv:2512.15833, Sect. 3.1].

Priors of the SO pipeline-A runs (TH top-hat centre ± half-width; G Gaussian centre ± σ) [src: arXiv:2302.04276, Table 2]:

| Parameter | Prior | Parameter | Prior |
|---|---|---|---|
| A_lens | TH 1.0 ± 1.0 | A_s | TH 2.0 ± 2.0 |
| r | TH 0.0 ± 0.1 | α_s | TH −1.0 ± 1.0 |
| A_d | TH 25 ± 25 | β_s | G −3.0 ± 0.3 |
| α_d | TH 0.0 ± 0.5 | ε_ds | TH 0.0 ± 1.0 |
| β_d | G 1.54 ± 0.11 | B_s, γ_s | TH 0 ± 10; −4 ± 2 |
| | | B_d, γ_d | TH 5 ± 5; −4 ± 2 |

The r prior extends to negative values on purpose: negative r can come
from volume effects of the priors on the other parameters, and an open
prior lets one see them. On real data it is to be replaced by r > 0 only
after checking that the other priors do not bias r [src: arXiv:2302.04276,
Sect. 2.1].

Likelihood: Gaussian in the bandpowers. The authors checked that the
Hamimeche–Lewis form gives the same constraints and give the reason it
holds: each bandpower averages N_modes ≃ Δℓ f_sky (2ℓ+1) > 61 modes, which
"would not hold any longer for the smaller BICEP/Keck-like patch sizes"
[src: arXiv:2302.04276, Sect. 2.1]. Sampling with emcee [src: same].

### Step 2b. Blind needlet ILC ("pipeline B")
<!-- key: step-2b-blind-needlet-ilc-pipeline-b -->

The ILC assumes only d_ν = a_ν s + n_ν (Eq. 2), with a_ν the CMB black body
(a vector of ones in thermodynamic units) and n_ν everything else, and forms
s̃ = wᵀ d with w = aᵀĈ⁻¹/(aᵀĈ⁻¹a) (Eqs. 3–4), Ĉ the frequency–frequency
covariance of the data per pixel [src: arXiv:2302.04276, Sect. 2.2]. In
the needlet version the weights are computed separately in harmonic windows
h_i(ℓ) with Σ_i h_i² = 1 (Eq. 5). SO uses five windows with ℓ_peak = {0,
100, 200, 350, 500}; all maps are brought to the 93 GHz beam (30′ FWHM);
the 27 GHz channel is dropped from the third window and 27 and 39 GHz from
the last two because of their resolution; the covariance is averaged over
pixel domains of 185°, 72°, 44°, 31° and 39° FWHM, chosen so that each
window holds at least 2500 modes and the ILC bias stays below 0.2% [src:
same]. The cleaned map's B spectrum is noise-debiased with noise-only
simulations passed through the same weights, and only r and A_lens are fitted
(r prior from −0.013 upward, A_lens in [0, 2]), Gaussian likelihood,
30 < ℓ ≤ 300 [src: same].

Semi-blind extensions add nulling constraints. Constrained moment ILC
(cMILC) minimises wᵀCw subject to wᵀA_CMB = 1 and wᵀA_α = 0 for selected
foreground moments α (Mustafa et al. 2026, arXiv:2603.11026, Eq. 7),
giving w = eᵀ(AᵀC⁻¹A)⁻¹AᵀC⁻¹ (Eq. 8), with the SED expanded around pivot
indices as in Eq. 6. Each extra constraint removes a degree of freedom from
the variance minimisation and raises the reconstruction noise [src:
arXiv:2603.11026, Sect. 2.2].

### Step 2c. Map-based parametric fit ("pipeline C", fgbuster)
<!-- key: step-2c-map-based-parametric-fit-pipeline-c -->

Data model d = Â(β) s + n (Eq. 6), with Â the mixing matrix set by spectral
indices β. Step 1 maximises the spectral likelihood (Stompor et al. 2009;
arXiv:2302.04276, Eq. 7) on maps smoothed to a common 100′ beam, with a
diagonal noise covariance from 500 noise simulations; step 2 recovers the
components by generalised least squares, s̃ = (ÃᵀN̂⁻¹Ã)⁻¹ÃᵀN̂⁻¹d ≡ Ŵd
(Eq. 8), on the unsmoothed maps; the effective beam B_ℓ^eff = ŴB_ℓ must be
corrected to get an unbiased spectrum [src: arXiv:2302.04276, Sect. 2.3].
The cosmological fit uses C_ℓ = C_ℓ^prim(r) + C_ℓ^lens(A_lens) + Ñ_ℓ (Eq. 10)
in −2 ln L = Σ_ℓ (2ℓ+1) f_sky [C̃_ℓ/C_ℓ + ln C_ℓ] (Eq. 11), an approximation
that ignores mode coupling from the footprint [src: same].

LiteBIRD's baseline is the same family, with spectral parameters fitted on
HEALPix pixels whose resolution depends on Galactic latitude: in the three
least contaminated 20%-of-sky regions (from the Planck GAL20/40/60 masks)
β_d at N_side = 64 everywhere, T_d at N_side = 8, 4, 0 and β_s at 4, 2, 2
from low to high latitude (Table 15). β_d is kept at the maximum
resolution "since LiteBIRD turns out to be particularly sensitive to this
parameter". On f_sky = 49% this is 24,545 non-linear parameters plus 144,534
Q/U amplitudes, against a data vector of about 10⁶ [src:
arXiv:2202.02773, Sect. 5.2.3].

### Step 3. Carry the residuals into the r likelihood
<!-- key: step-3-carry-the-residuals-into-the-r-likelihood -->

Three ways are in use:

1. **Model them in the spectra** (moment parameters in pipeline A; Step 2a).
2. **Marginalise a dust template.** Pipeline C computes the BB spectrum of
   its own recovered dust map, C̃_ℓ^dust, and adds A_dust C̃_ℓ^dust to the
   model (arXiv:2302.04276, Eq. 12); only dust is included "as it turns out
   to be the largest contamination" [src: Sect. 2.3].
3. **Marginalise a pipeline-specific residual template.** For NILC and
   cMILC, foreground maps from generalised NILC (GNILC) are propagated
   through the ILC weights, the noise-residual spectrum is subtracted, and
   the resulting C_ℓ^FTres enters as a_temp C_ℓ^FTres with a_temp uniform in
   (−50, 50) (arXiv:2603.11026, Eq. 16) [src: Sect. 5.1]. The authors
   contrast it with option 2: the parametric template depends on the
   accuracy of the foreground model, theirs targets the residuals of the
   pipeline actually used [src: Sect. 5.2].

LiteBIRD splits residuals into "systematic" (noiseless, they bias r) and
"statistical" (from noisy spectral-index estimates, they set σ(r)), and
estimates σ(r = 0) = 1/√F with F = −⟨∂² ln L/∂r²⟩ (Eq. 35), where
−2 ln L = f_sky [tr C⁻¹D + ln det C] and C contains lensing, noise and
statistical residuals averaged over 1000 foreground + noise realisations
[src: arXiv:2202.02773, Sects. 5.2.3–5.2.4]. The statistical residuals
dominate its budget [src: Sect. 5.2.4].

### Step 4. Covariance
<!-- key: step-4-covariance -->

SO builds the bandpower covariance from 500 simulations with Gaussian
foregrounds, because the realistic foreground templates are single
realisations; it ignores correlations between multipole windows. Pass
criterion: the empirical distribution of χ²_min matches the expected one,
also on the non-Gaussian foreground simulations [src: arXiv:2302.04276,
Sect. 2.1 and App. A]. For d10s5 the fiducial model gives
χ²_min = 601 ± 41 for 558 degrees of freedom (PTE 0.10), which confirms the
covariance but also shows that χ² cannot flag the foreground bias (see
"What goes wrong") [src: Sect. 4.4].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Same simulations, three pipelines
<!-- key: same-simulations-three-pipelines -->

SO ran all three on 500 simulations of 27–280 GHz SAT maps with r = 0,
A_lens = 1, four foreground skies and four noise cases [src:
arXiv:2302.04276, Sects. 3.3, 4.2, Table 4]. The skies: Gaussian
foregrounds; PySM d0s0 (Planck/WMAP templates, uniform SEDs, β_d = 1.54,
T_d = 20 K, β_s = −3); d1s1 (spatially varying SEDs); dmsm (β_d and T_d
templates smoothed to 2°, synchrotron index fluctuations multiplied by 1.6
and small-scale structure added following S-PASS) [src: Sect. 3.3].

10³ × (r ± σ(r)), goal white noise with optimistic 1/f (arXiv:2302.04276) [src: Table 4]:

| Sky | A (C_ℓ fiducial) | A + moments | B (NILC) | C (map parametric) | C + dust marg. |
|---|---|---|---|---|---|
| d0s0 | −0.4 ± 2.1 | −0.5 ± 2.7 | −0.1 ± 2.1 | 0.5 ± 2.3 | −1.7 ± 3.5 |
| d1s1 | 1.8 ± 2.1 | −0.2 ± 2.8 | 2.1 ± 2.1 | 2.6 ± 2.3 | 0.0 ± 3.3 |
| dmsm | 3.9 ± 2.1 | 0.3 ± 2.7 | 3.8 ± 2.1 | 5.3 ± 2.4 | 0.2 ± 3.0 |
| d10s5 (100 sims) | 19.2 ± 1.9 | 2.7 ± 2.8 | 15.8 ± 1.9 | 22.0 ± 2.6 | −1.5 ± 5.1 |

(d10s5 from Sect. 4.4, Eq. 15.) Readings stated by the authors:

- The nominal pipelines have comparable σ(r), 2.1–3.6 × 10⁻³ across noise
  models; d1s1 gives about 1σ bias, dmsm up to about 2σ, d10s5 10, 8 and 8σ
  for A, B and C [src: arXiv:2302.04276, Sects. 4.2, 4.4].
- Both extensions bring the bias below 1σ in every case. A + moments costs
  about 25% in σ(r) on average (45% on d10s5); C + dust marginalisation
  costs more (σ(r) 3.0–5.9 × 10⁻³; 95% on d10s5). "This makes A + moments
  the unbiased method with the lowest statistical error" [src:
  arXiv:2302.04276, Sects. 4.2, 4.4].
- On the simpler skies the extensions show a small negative bias (≈ 0.1σ
  for A + moments, < 0.5σ for C + dust), attributed to prior-dominated extra
  parameters weakly degenerate with r [src: arXiv:2302.04276, Sect. 4.2].
- The channel weights agree between pipelines: 93 and 145 GHz positive,
  280 GHz negative in all three [src: arXiv:2302.04276, Sect. 4.3].

### Parametric or blind
<!-- key: parametric-or-blind -->

- **Parametric** is efficient when the SED model is close to the sky and
  degrades strongly when it is not; **minimum-variance** methods assume no
  model and are less sensitive to where the complexity comes from. With
  line-of-sight ("3D") dust complexity added, parametric residuals grew by
  O(10) and NILC residuals by O(1) in LiteBIRD-like simulations; the most
  damaging dust model was not the same for the two methods (Vacher et al.
  2025, arXiv:2411.11649, Sect. 4.4) [src]. The proxies of complexity that
  predict parametric residuals (decorrelation, E/B ratio) do not predict
  NILC ones, which track the power added by moments away from 353 GHz
  [src: same].
- **Blind alone is not enough** on ground-based patches: on SO-like
  simulations NILC and cMILC still leave r ≈ 1 × 10⁻³ (d1s1) and ≈ 10⁻²
  (d10s5); NILC also biases A_lens [src: arXiv:2603.11026, Sect. 4.2].
  Adding the residual template removes the bias at a cost in σ(r)
  (arXiv:2603.11026) [src: Sect. 5.2, Table 2]:

| 10³ (r ± σ(r)), baseline-optimistic noise | d1s1 | d10s5 |
|---|---|---|
| NILC | 1.2 ± 2.7 | 12.9 ± 3.1 |
| NILC + template | 0.1 ± 3.1 | 0.5 ± 8.4 |
| cMILC | 1.4 ± 3.1 | 10.7 ± 4.0 |
| cMILC + template | 0.6 ± 4.2 | 0.6 ± 8.8 |

  Fixing A_lens = 1 tightens σ(r) (NILC + template on d10s5: 8.4 → 6.5 ×
  10⁻³) but loads any residual systematic onto r alone [src:
  arXiv:2603.11026, Sect. 5.2, Table 3].

### Moments or decorrelation parameter
<!-- key: moments-or-decorrelation-parameter -->

On public BK15 data the minimal moment model reproduces the published r
posterior when its extra parameters are switched off, finds no evidence for
spectral-index variation when they are on, shifts r slightly down and
widens it by about 24%. A constant decorrelation parameter (the BK
approach) is equivalent to a non-perturbative moment expansion only for
scale-independent index variations; it gives a similar shift and a
slightly narrower posterior [src: arXiv:2011.11575, Sect. 4.5; App. A].
On PySM-type skies with low index variation, the moment model corrected a
bias of more than 1σ: r = 0.0029 ± 0.0023 → 0.0005 ± 0.0028, with β_d's
posterior width up by about 30% [src: Sect. 4.3].

### Spatial resolution of the fitted indices (map-based)
<!-- key: spatial-resolution-of-the-fitted-indices-map -->

LiteBIRD picks N_side per parameter and latitude "to balance between the
statistical uncertainties sourced by the number of free parameters, and the
need for a flexible enough model" [src: arXiv:2202.02773, Sect. 5.2.3].
Its mask for the residual spectra is cut where residuals are highest, with
the threshold chosen so that the bias on r is low while f_sky stays large;
the authors note this exact procedure "will not be applicable to real data
sets" [src: Sect. 5.2.4].

### Delensing interacts with cleaning
<!-- key: delensing-interacts-with-cleaning -->

On d1s1 with SO baseline noise, 50% delensing (A_lens = 0.5) reduced σ(r) by
25–30% for pipelines A and B, 10–20% for A + moments and 0–33% for
C + dust marginalisation [src: arXiv:2302.04276, Sect. 4.2, Table 5].

The pipelines with extra foreground freedom gain less, so a delensing gain
quoted for a fiducial pipeline does not carry over to a debiased one [der:
reading of the table above].
Delensing itself is in `deep/delensing.md`.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| SO SAT multipole range, binning | 30 ≤ ℓ ≤ 300, Δℓ = 10 | SO pipelines | arXiv:2302.04276 | Sect. 2.1 |
| SO SAT f_sky, apodisation | ≈ 10%, C1 kernel 10° | SO | arXiv:2302.04276 | Sect. 2.1 |
| Data splits | 4, giving 6 pairs, 21 spectra for 6 channels | SO A | arXiv:2302.04276 | Sect. 2.1 |
| Modes per bandpower | > 61 (justifies Gaussian likelihood) | SO A | arXiv:2302.04276 | Sect. 2.1 |
| Fiducial / moment parameters | 9 / 13 | SO A; minimal moments | arXiv:2302.04276; arXiv:2011.11575 | Eq. 1; Eq. 23 |
| NILC windows, minimum modes, ILC bias | 5; ≥ 2500 per window; < 0.2% | SO B | arXiv:2302.04276 | Sect. 2.2 |
| Common beam | 30′ (NILC); 100′ (spectral likelihood, C) | SO B, C | arXiv:2302.04276 | Sects. 2.2, 2.3 |
| Simulations for covariance and noise bias | 500 (Gaussian foregrounds) | SO A, B, C | arXiv:2302.04276 | Sects. 2.1–2.3 |
| Nominal σ(r) range | 2.1–3.6 × 10⁻³ (no delensing) | SO, three pipelines | arXiv:2302.04276 | Sect. 4.2 |
| Bias, nominal pipelines, d10s5 | 10σ (A), 8σ (B), 8σ (C) | SO | arXiv:2302.04276 | Sect. 4.4 |
| σ(r) cost of debiasing on d10s5 | +45% (A + moments), +95% (C + dust) | SO | arXiv:2302.04276 | Sect. 4.4 |
| Model odds, fiducial vs moments, d10s5 | 10⁻²⁶ to 10⁻²; 99/100 sims below 1% | SO A (AIC) | arXiv:2302.04276 | Sect. 4.4 |
| PySM dust/sync amplitudes in the SAT patch | A_BB^d = 28 μK² (353 GHz), A_BB^s = 1.6 μK² (23 GHz), ℓ = 80 | SO sims | arXiv:2302.04276 | Sect. 3.3 |
| LiteBIRD free parameters in comp. sep. | 24,545 non-linear + 144,534 amplitudes | LiteBIRD 2022 | arXiv:2202.02773 | Sect. 5.2.3 |
| LiteBIRD foreground bias and σ(r) | r_FG = (3.3 ± 6.2) × 10⁻⁴; σ(r = 0.01) = 0.0013 | LiteBIRD 2022, d1s1 (**forecast**) | arXiv:2202.02773 | Sect. 5.2.4 |
| Reionisation vs recombination bump | σ(r = 0.01) = 0.0036 (ℓ < 20), 0.0014 (ℓ > 20) | LiteBIRD 2022 (**forecast**) | arXiv:2202.02773 | Sect. 5.2.4 |
| PySM d1 SED spread on 49.5% of sky | β_d = 1.534 ± 0.028, T_d = 22.23 ± 1.56 K, β_s = −2.993 ± 0.046 | LiteBIRD sims | arXiv:2202.02773 | Sect. 5.2.1 |
| Residual-template prior | a_temp uniform in (−50, 50) | NILC/cMILC | arXiv:2603.11026 | Sect. 5.1 |

The LiteBIRD 2022 numbers are for the pre-reformation three-telescope
design with 22 channels [src: arXiv:2202.02773, Sect. 5.2.3]; the 2026
design has one telescope and 12 bands (`surveys-and-data.md#planned`).

## What goes wrong
<!-- key: what-goes-wrong -->

- **Bias invisible to goodness of fit.** On dmsm the nominal pipelines are
  biased by about 2σ and simple model-selection metrics give no significant
  evidence that a richer model is needed; on d10s5 χ² still has PTE 0.10,
  while AIC odds computed on the same seed do flag it [src:
  arXiv:2302.04276, Sect. 4.4]. Test the authors recommend: choose the
  pipeline complexity so that r is unbiased on every foreground model
  consistent with current data, use that as fiducial, and compare less
  conservative pipelines to it by goodness of fit, with robustness tests
  for foreground signatures [src: same].
- **Prior-volume shifts from extra nuisance parameters.** Negative r biases
  of 0.1–0.5σ on simple skies [src: arXiv:2302.04276, Sect. 4.2]. Test:
  open the r prior to negative values during validation, as SO does [src:
  Sect. 2.1].
- **ILC bias from small pixel domains.** Test: domain sizes with enough modes
  (≥ 2500 per window for < 0.2% bias in SO) [src: arXiv:2302.04276,
  Sect. 2.2].
- **Inhomogeneous noise in NILC.** A positive bias on Gaussian foregrounds
  traced to the pixel covariance used for the weights; absent for
  homogeneous noise; SO reruns those cases on a more homogeneous mask
  [src: arXiv:2302.04276, Sect. 4.2].
- **Effective beam of the cleaned map not corrected** (map-based) — biased
  spectrum [src: arXiv:2302.04276, Sect. 2.3].
- **Template mismatch.** GNILC templates are poor in synchrotron-dominated
  channels and show spectral bumps there; with cMILC weights the template
  amplitude is off by a near-constant factor, which a free a_temp absorbs at
  the price of a wider posterior [src: arXiv:2603.11026, Sects. 5.1–5.2].
- **Validation on too simple skies.** Results change by an order of
  magnitude between d1s1 and d10s5 (table above), and dust models with
  line-of-sight complexity built to stay compatible with Planck spectra
  raise parametric residuals by O(10) [src: arXiv:2411.11649, Sect. 4.4].
- **Gaussian likelihood on small patches.** Justified at f_sky ≈ 10% by the
  mode count; stated not to hold for BICEP/Keck-size patches [src:
  arXiv:2302.04276, Sect. 2.1].

## Reading list
<!-- key: reading-list -->

- Review: Achúcarro et al. 2022, arXiv:2203.08128 — where component
  separation sits among the B-mode measurement challenges.
- Foundation: Chluba et al. 2017, arXiv:1701.00274 — moment expansion of
  foreground SEDs.
- Method: Azzoni et al. 2021, arXiv:2011.11575 — the minimal power-spectrum
  moment model (Eqs. 15–23), its assumptions and its test on BK15.
- Method and comparison: Wolz et al. 2023, arXiv:2302.04276 — the three SO
  pipelines on common simulations; read Table 4 and Sect. 4.4.
- Application: Simons Observatory 2025, arXiv:2512.15833 — the six-SAT
  forecast built on the minimal moment model.
- Application: LiteBIRD Collaboration 2022, arXiv:2202.02773, Sect. 5.2 —
  multi-resolution map-based fit, residual split, Fisher σ(r).
- Method: Mustafa et al. 2026, arXiv:2603.11026 — cMILC and a pipeline-
  specific residual template for blind cleaning.
- Critique: Vacher et al. 2025, arXiv:2411.11649 — line-of-sight dust
  complexity and why parametric and blind methods fail differently.
- Critique: Liu et al. 2025, arXiv:2508.00073 — dust complexity bias for SO
  (in L2).

## Not verified
<!-- key: not-verified -->

- BICEP/Keck's own reasons for the decorrelation treatment beyond what L2
  records from BK18 App. E; the BK15 paper was not read.
- The HTML of arXiv:2302.04276, Sect. 2.1, cuts the sentence introducing
  the moment model; the 13-parameter form is taken from arXiv:2011.11575.
- Harmonic-space likelihood validation for LiteBIRD (Galloni et al. 2026,
  arXiv:2610.18036): abstract read only; it reports that the offset
  Hamimeche–Lewis likelihood gives a 68% upper bound on r 19–29% larger
  than a pixel-based benchmark over ℓ ≤ 128, depending on the beam window
  function [src: abstract].
- Component-separation choices for the reformed LiteBIRD (arXiv:2607.25285
  names component separation among ground-segment tasks only).
- Mangilli et al. 2021 and other moment-expansion variants: named in
  arXiv:2512.15833, not read.
