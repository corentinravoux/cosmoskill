# Next-generation siren forecasts — cosmo-multimessenger dossier

Scope: how a standard-siren forecast for A#, Einstein Telescope, Cosmic
Explorer or LISA is built (network and duty cycle, population and rate,
GW measurement errors, extra distance-error terms, counterpart model,
cosmological inference), what each assumption buys, and how to referee one.
Snapshot: 2026-10-17.
From: Palmese & Mastrogiovanni 2025 review (arXiv:2502.00239), Sect. 4;
Einstein Telescope science case (arXiv:2503.12263), Sect. 2.3.1; LISA
Cosmology Working Group (arXiv:2204.05434), Sects. 2.2–2.3; Zhao et al. 2026
review (arXiv:2605.08595), Sects. 4.1.2 and 4.2.

Already in L2, not repeated here: the table of forecast claims and their
track record in `open-questions.md#forecasts`; planned facilities in
`surveys-and-data.md#planned-detector-upgrades-third-generation-lisa`; the
waveform and calibration requirement `O(ρ⁻²)` for golden dark sirens in
`systematics.md#detector-calibration-and-waveform-systematics`; the
cross-correlation forecasts in `deep/gw-lss-cross-correlation.md`.

## How it is done
<!-- key: how-it-is-done -->

Notation. `d_L` luminosity distance; `Δd_L` or `σ_n` the GW measurement
error on it for event `n`; `ρ` or SNR the network matched-filter
signal-to-noise; `ι` the inclination of the orbital angular momentum to the
line of sight; `ΔΩ_90` the 90% sky area; `R_0` a local merger-rate density
in Gpc⁻³ yr⁻¹; FIM the Fisher information matrix of the waveform
parameters. Network labels are those of the cited papers: `Δ-10km` and
`Δ-15km` for an ET triangle with 10 or 15 km arms, `2L-15km-45°` for two
L-shaped ET detectors with 15 km arms rotated by 45°, CE40 and CE20 for
Cosmic Explorer with 40 and 20 km arms, A# for upgraded LIGO.

### Step 1. Fix the network, the time and the duty cycle
<!-- key: step-1-fix-the-network-the-time-and-the-duty -->

| Forecast | Network | Time, duty cycle | Place read |
|---|---|---|---|
| ET design study (Branchesi et al. 2023, arXiv:2303.15923) | four ET geometries, each with and without the low-frequency (LF) cryogenic instrument | 5 yr (GRB) or 1 yr (kilonova); duty cycle of each configuration included | Sect. 6.4.1 |
| ET science case (arXiv:2503.12263) | `Δ-10km` and `2L-15km-45°` | same catalogues as the design study | Sect. 2.3.1, bright sirens |
| Chen et al. 2024 (arXiv:2402.03120) | HLA (three A#, including LIGO-India), ET, CE4020, CE40ET, CE4020ET; site coordinates in their Table 1 | 1 yr | App. A, Sect. 4 |
| Ferri et al. 2024 (arXiv:2412.00202) | LVK O5; LVK+ET (`Δ-10km`, ET-D); ET+2CE | 3 yr (O5) or 5 yr, 80% duty cycle | Sect. 3.1 |
| De Leo et al. 2026 (arXiv:2607.20413) | ET `Δ-10km` in Sardinia | — | Sect. 3.2 |
| Colombo et al. 2026 (arXiv:2609.12053) | three LIGO (with India), Virgo, KAGRA at O5 sensitivity | 1 yr | Sect. III |
| LISA (arXiv:2204.05434) | LISA, 4 or 10 yr (EMRIs); five-year mission (MBBHs) | — | Sects. 2.2.1, 2.3.2 |

Network geometry matters through localisation: Chen et al. find the
co-located ET triangle poorer than three separated A# detectors at isolating
golden dark sirens, and the two-site CE4020 network unable to localise
well enough for them [src: arXiv:2402.03120, Sect. 4.1]. Cheng & Gair choose
two L-shaped ET detectors over the triangle "as the latter has potentially
highly degenerate localization modes" [src: arXiv:2603.13053, Sect. VII.1.3].

### Step 2. Choose the population and normalise the rate
<!-- key: step-2-choose-the-population-and-normalise-the -->

The rate normalisation is "the parameter that has greatest impact on the
total amount of events" [src: arXiv:2412.00202, Sect. 3.1]. Choices read:

| Forecast | Redshift dependence | Normalisation | Masses | Place read |
|---|---|---|---|---|
| Chen et al. 2024 | Madau–Dickinson `ψ(z) = (1+z)^γ / [1 + ((1+z)/(1+z_p))^κ]` (Eq. 6), `γ = 2.7`, `z_p = 1.9`, `κ = 5.6`, no time delay | `R_0` = 24 (BBH), 45 (NSBH), 320 (BNS) | their App. B.1 | App. B.2 |
| Ferri et al. 2024 | star-formation rate convolved with a log-normal delay, minimum 20 Myr; `dN/dz dt = r(z)/(1+z) dV_c/dz` (Eq. 20) | upper 1σ of GWTC-3 at `z = 0.2`: `r(0.2) = 28 (+14/−9)` (Eq. 21), giving about 41 200 BBH yr⁻¹ to `z ~ 10` | Power Law + Peak from GWTC-3 plus a log-normal 88–1000 M☉ extension; aligned spins only | Sect. 3.1 |
| Colombo et al. 2026 | `∝ (1+z)^2.7` | 200 for all compact binaries | FullPop-4.0 instance, 1–300 M☉; SFHo equation of state, maximum neutron-star mass 2.06 M☉ | Sect. III |
| De Leo et al. 2026 | `R(z) = 1 + 2z` (`z ≤ 1`), `¾(5 − z)` (`1 < z < 5`), 0 beyond (Eq. 6); `P(z) ∝ R(z) 4π d_C² / [H(z)(1+z)]` (Eq. 7) | 20 000 injections in `0.1 < z < 3.5` | 1.4 M☉ for every neutron star | Sect. 3.2 |
| Cheng & Gair 2026 | LVK-consistent model | 20 (BBH), 2 yr → 233 499 detected BBH (2 ET + 1 CE, SNR ≥ 25) | — | Sect. VII.1.3 |

Stated reasons: Chen et al. omit a delay-time distribution because it "is
still uncertain" and the Madau–Dickinson rate alone fits GWTC-3 [src:
arXiv:2402.03120, App. B.2]. Ferri et al. take the upper 1σ rate. The ET
science case warns that, with no BNS candidate in O4 at the time of
writing, the BNS rate of its catalogues "is now toward the upper range,
rather than the mean value" [src: arXiv:2503.12263, Sect. 2.3.1,
footnote 21]. For LISA massive black-hole binaries the event number spans
"a few" to "several tens" per year depending on seeding and delays [src:
arXiv:2204.05434, Sect. 2.2.1].

### Step 3. Compute GW detections and measurement errors
<!-- key: step-3-compute-gw-detections-and-measurement -->

All forecasts read here use Fisher-matrix codes, not full parameter
estimation: GWFISH and GWFAST, which "agree fully" in the ET design study
[src: arXiv:2303.15923, Sect. 6.4.1]; gwbench (arXiv:2402.03120,
Sect. 4.1); GWDALI with 11 parameters (`M_c, η, d_L, ι, θ, φ, ψ, s1z, s2z,
t_c, φ_c`) (arXiv:2412.00202, Eq. 22); GWFish (arXiv:2607.20413,
arXiv:2609.12053) [src]. Detection thresholds are not common: network SNR
> 12 (arXiv:2412.00202, arXiv:2609.12053), > 20, "the most conservative"
ET threshold (arXiv:2607.20413), ≥ 25 (arXiv:2603.13053) [src].

Where the face-on degeneracy breaks the FIM, forecasts do one of three things:

1. **Cut the events.** Ferri et al. invert by SVD with `r_cond = 10⁻¹⁶` and drop
   events with `ι < 5°` or `> 175°` [src: arXiv:2412.00202, Sect. 3.1].
2. **Fix the degenerate parameters and use a scaling law.** For GRB-selected
   events the ET design study fixes the sky position (host identified),
   notes that all its GRBs have `min(ι, 180° − ι) < 5–10°`, and sets
   `Δd_L/d_L = 2/SNR`, "with a factor of two included to be conservative",
   the high-SNR FIM limit when other parameters are fixed [src:
   arXiv:2303.15923, Sect. 6.4.1]. The ET science case states the limits of
   this: near face-on the FIM is ill-conditioned and "the 2/SNR approximation
   is not appropriate anymore", with biases that "can jeopardize the whole
   inference" [src: arXiv:2503.12263, Sect. 2.3.1].
3. **Impose the counterpart's sky position as an exact prior.** Tamanini et
   al. remove the two sky-angle rows and columns of the FIM before inversion
   [src: arXiv:1601.07112, Sect. 7].

### Step 4. Add the non-instrumental distance errors
<!-- key: step-4-add-the-non-instrumental-distance-errors -->

The template is the per-event variance of Tamanini et al. 2016
(arXiv:1601.07112, Eq. 12):

```
F_ij = Σ_n [σ_n² + σ_lens²(z_n) + σ_v²(z_n)]⁻¹ (∂d_L/∂θ_i)(∂d_L/∂θ_j) |_fid
σ_lens(z) = d_L(z) × 0.066 [(1 − (1+z)^−0.25)/0.25]^1.8                (Eq. 16)
σ_v(z)   = d_L(z) [1 + c(1+z)/(H(z) d_L(z))] √⟨v²⟩/c ,  √⟨v²⟩ = 500 km/s (Eq. 17)
```

Caveat: Mpetha et al. 2024 (arXiv:2402.19476, Sect. IV.3) note that the σ_lens
expression of Tamanini et al. 2016 lacks a factor 1/2, because the original
fit is for σ(ln d_L²) = 2σ(d_L)/d_L; including it "would improve results in
numerous forecasting papers" [src]. See `deep/gw-lensing.md`.

`σ_n` adds, for photometric redshifts, `(∂d_L/∂z) Δz` with
`Δz ≈ 0.03(1+z)` [src: Sect. 7]. In their optimistic scenario `σ_lens` is
halved, assuming de-lensing by mapping the line of sight and the
non-Gaussianity of the convergence PDF [src: same]. The ET design study
instead adds `Δd_L/d_L = 0.05 z` for lensing in quadrature [src:
arXiv:2303.15923, Sect. 6.4.1]. For LISA massive black-hole binaries at
`z ≈ 2–4`, weak lensing, not the LISA error, dominates the distance error,
"up to 5–10%" [src: arXiv:2204.05434, Sect. 2.3.2]. De Leo et al. carry no
lensing term (no paragraph of the paper mentions lensing) [src:
arXiv:2607.20413, grep of the rendering].

### Step 5. Model the counterpart
<!-- key: step-5-model-the-counterpart -->

| Forecast | Counterpart and instrument | Rule | Place read |
|---|---|---|---|
| ET design study (arXiv:2303.15923), ET+VRO | kilonova, Rubin | follow up all events with `ΔΩ_90 < 40` deg² in its sky, `g` and `i` on the first two nights, 600 s per pointing; pointings = `ΔΩ`/FoV + 1; 60 s overhead per night; 2600 h of Rubin time per year | Table 10, Sect. 4.3 |
| ET design study (arXiv:2303.15923), ET+THESEUS | short-GRB prompt emission | short-GRB model normalised to observations; 75 joint detections in 5 yr for 2L-20km | Sect. 6.4.1 |
| Chen et al. 2024 (arXiv:2402.03120) | kilonova, LSST | `z ≤ 0.5`, `ΔΩ ≤ 100` deg² (≤ 10 pointings), 30 s single exposure, peak brighter than the band limit, then 40% kept for coverage and duty cycles; highest detected `z = 0.28` | Sect. 4.2 |
| Colombo et al. 2026 (arXiv:2609.12053) | kilonova; GRB prompt | `m_g,lim = 26` (about 180 s with Rubin); GBM fluence `3 × 10⁻⁷` erg cm⁻² (×10 better as a variant) | End Matter, Sect. VI.1.2 |
| De Leo et al. 2026 | GRB afterglow, Rubin | equivalent to `ι < 18°` | Sect. 3.2 |
| LISA (arXiv:2204.05434), massive black-hole binaries | radio (SKA) localisation, then ELT redshift | about 10–25 bright sirens in five years; about four useful per year | Sects. 2.2.1, 2.3.2 |

Reasons and caveats stated: kilonova emission is close to isotropic, so the
selected events are not near face-on and the FIM is better conditioned
[src: arXiv:2303.15923, Sect. 6.4.1]; the 40% factor stands for "sky
coverage, systematic biases as well as duty-cycles" [src: arXiv:2402.03120,
Sect. 4.2]; the APR4 equation of state, chosen by Chen et al., makes compact
stars that eject less mass and lowers kilonova numbers [src: same]; the
threshold model of Colombo et al. ignores localisation and survey strategy,
which "may alter the absolute detection rates by a factor of order ∼2", and
the day–night cycle and single hemisphere reduce bright-siren rates "by at
least a factor of two" [src: arXiv:2609.12053, VI.1.2, Sect. III].

### Step 6. Turn distances into cosmology
<!-- key: step-6-turn-distances-into-cosmology -->

- **Fisher on `d_L(z)`.** `Γ_ij = Σ_k σ_DL⁻² (∂D_L/∂θ_i)(∂D_L/∂θ_j)_k`
  (arXiv:2402.03120, Eq. 4), with Gaussian priors added on the diagonal
  (Eq. 5), `σ(H0) = 10`, `σ(Ω_m) = 0.5`; the priors keep the unconstrained Ω_m
  from producing unphysical errors that "adversely affect the errors in H0"
  [src: Sect. 4.1].
- **Scattered mock data, then MCMC.** The ET design study computes `d_L` at
  the counterpart redshift in the fiducial cosmology (H0 = 67.66, Ω_M = 0.31)
  and scatters it by `Δd_L` "to simulate the realistic setting of an
  experiment" [src: arXiv:2303.15923, Sect. 6.4.1]. De Leo et al. fit with
  Cobaya, flat priors H0 ∈ [20, 100] and Ω_m ∈ [0.1, 0.9], a diagonal
  covariance that "neglects possible correlated systematic uncertainties, such
  as a common detector-calibration error", and `r_d` free on [100, 200] Mpc
  when BAO are added [src: arXiv:2607.20413, Sect. 4].
- **Realisations.** Tamanini et al. simulate 118 five-year catalogues per
  formation scenario because the population scatter is large [src:
  arXiv:1601.07112, Sect. 7]; Chen et al. draw 1000 realisations of the few
  `z < 0.1` events and quote the median with a 99% band; a realisation
  without a golden siren returns the prior [src: arXiv:2402.03120,
  Sect. 4.1]. Golden dark sirens are defined as `z < 0.1` and
  `ΔΩ < 0.04` deg², where one `L*` galaxy is expected [src: same].
- **Figure of merit.** `FoM = det(F)^{1/2N}` for `N` parameters (Tamanini et
  al., Eq. 18); not the DETF definition, which uses 2σ errors [src:
  arXiv:1601.07112, Sect. 7].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### ET geometry and the low-frequency instrument
<!-- key: et-geometry-and-the-low-frequency-instrument -->

Same BNS sample, same EM signal, duty cycles included [src:
arXiv:2303.15923, Sect. 6.4.1, Tables 28–29]: `Δ-15km` and `2L-15km-45°` give
similar H0 and improve on `Δ-10km` by a factor 1.3–1.6. For ET+VRO, losing
the LF instrument leaves 6% (`Δ-10km`) or 11% (`2L-15km`) of the joint
detections, and the H0 constraint is more than seven times weaker. The
authors state that these numbers compare geometries and "should not be
understood as forecasts for the overall capability of ET" [src: same].

### Kilonova or GRB counterparts
<!-- key: kilonova-or-grb-counterparts -->

ET+VRO gives the best H0 because its events are more numerous and at low
redshift, but its estimate "strongly depend[s] on the BNS merger rate
normalization", uncertain by an order of magnitude; the THESEUS estimate is
"very solid and conservative", prompt emission only, with afterglows by XGIS
and SXI raising detections by about 3 [src: arXiv:2303.15923, Sect. 6.4.1].
GRB-selected events are face-on, which is exactly where the FIM fails
(Step 3) [src: arXiv:2503.12263, Sect. 2.3.1].

### Bright or golden dark sirens
<!-- key: bright-or-golden-dark-sirens -->

In one year, bright-siren H0 equals or beats golden dark sirens for every
network; the gap is largest for HLA (localisation too coarse for unique
hosts) and CE4020 (two detectors). CE4020 detects 131 bright sirens against
196 for HLA yet constrains H0 better through higher SNR. CE4020ET has at
least one golden dark siren in every realisation and almost always better
than 2% [src: arXiv:2402.03120, Sects. 4.1–4.2].

### Low or high redshift
<!-- key: low-or-high-redshift -->

With bright sirens alone, the H0 variance is smallest in the lowest bin
(`z ≈ 0.23`) and the cumulative error "largely saturates by `z_max ≃ 1`";
the reasons given are the growing Ω_m sensitivity of `d_L` and the growing
distance error [src: arXiv:2607.20413, Sect. 5.1]. Note their catalogue
excludes `z < 0.1` [src: Sect. 3.2]. LISA massive-binary sirens at
`z ≈ 2–4` give "few percent" on H0 in ΛCDM and matter more for tests beyond
H0 [src: arXiv:2204.05434, Sect. 2.3.2].

### Sirens alone or with external priors
<!-- key: sirens-alone-or-with-external-priors -->

ET with a Planck 2018 prior: GW+GRB goes from 5.7% (`Δ-10km`) and 4% (2L)
to 1.1% for both, "clearly dominated by the Planck prior"; GW+KN from 0.9% and
0.6% to 0.7% and 0.4% [src: arXiv:2503.12263, Sect. 2.3.1]. A forecast that
includes CMB, BAO or SN priors is not a siren-only forecast.

### LISA source classes
<!-- key: lisa-source-classes -->

[src: arXiv:2204.05434, Sect. 2.3.2] Stellar-origin BBHs cross-matched with
simulated catalogues (SNR > 8, `z < 0.1`, `Δd_L/d_L < 20%`): from 7 events and
7% to 259 events and 1% across configurations and rates. EMRIs (SNR > 100,
`z ≤ 0.7`): 3.6%, 2.5%, 1.6% in 4 yr and 2.6%, 1.5%, 1.1% in 10 yr for
pessimistic, fiducial, optimistic populations (about 5, 30, 70 useful
events in 10 yr). Massive binaries with counterparts: few percent. A
combined analysis of the three classes had not been done.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Lensing error | `0.066 [(1 − (1+z)^−0.25)/0.25]^1.8 d_L`; halved with de-lensing | LISA forecasts | arXiv:1601.07112 | Eq. 16 |
| Lensing error, alternative | `0.05 z d_L` | ET design study | arXiv:2303.15923 | Sect. 6.4.1 |
| Peculiar-velocity error | Eq. 17 with 500 km/s | LISA forecasts | arXiv:1601.07112 | Eq. 17 |
| Distance error scaling | `2/SNR`, sky fixed | ET GW+GRB | arXiv:2303.15923 | Sect. 6.4.1 |
| ET H0, GW+GRB, 5 yr | 5.7% (`Δ-10km`), 3.5% (`Δ-15km`), 4.0% (2L-15), 2.9% (2L-20); **forecast** | ET+THESEUS | arXiv:2303.15923 | Table 28 |
| ET H0, GW+KN, 1 yr | 0.9%, 0.7%, 0.6%, 0.4% (same order); HF only 6.5%, 5.7%, 6.6%, 3.1%; **forecast** | ET+VRO | arXiv:2303.15923 | Table 29 |
| Rubin time budget | 2600 h yr⁻¹; 600 s per pointing | ET+VRO | arXiv:2303.15923 | Table 10 caption |
| Local rates assumed | BBH 24, NSBH 45, BNS 320 Gpc⁻³ yr⁻¹ | XG networks | arXiv:2402.03120 | App. B.2 |
| Events within `z = 0.1` | about 10 BBH, 20 NSBH, 120 BNS per year | same | arXiv:2402.03120 | Sect. 4.1 |
| O5 yearly detections | 3 BNS, 8 NSBH, 2324 BBH; kilonova for all 3 BNS and 5 NSBH; **forecast** | LVK-India O5, SNR > 12 | arXiv:2609.12053 | Sect. III |
| Detected BBH, cross-correlation forecast | 377 (O5), 54 991 (LVK+ET), 73 260 (ET+2CE) | Ferri | arXiv:2412.00202 | Sect. 3.1 |
| LISA massive-binary sirens | 10–25 in 5 yr; about 4 useful per year, `z` peak 2–4 | LISA | arXiv:2204.05434 | Sects. 2.2.1, 2.3.2 |
| LISA localisation | 0.4 deg² to `z ≈ 3` for 10⁵–10⁶ M☉, at merger; `d_L` better than 10% at `z < 3` | LISA | arXiv:2204.05434 | Sect. 2.2.1 |
| Photometric redshift error | `0.03(1+z)` | LISA (ELT hosts) | arXiv:1601.07112 | Sect. 7 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Fisher matrix at low SNR or for weakly constrained parameters.** It "can be
  a poor predictor" for many-parameter waveforms at modest SNR and when
  priors are ignored; the paper gives recipes for singular matrices, priors
  and the SNR at which FIM results can be believed [src: Vallisneri 2008,
  arXiv:gr-qc/0703086, abstract]. On real events GWFAST reproduces SNRs and
  error magnitudes but is optimistic for GW200208_130117 (network SNR 10.8),
  "for such a value of the SNR, the FIM approach is not guaranteed to work"
  [src: arXiv:2207.06910, Sect. VI]. Test: compare with full parameter
  estimation on a subset; report the threshold SNR.
- **Inversion choices.** GWFAST offers Cholesky (default), SVD, regularised SVD
  and LU; dropping small singular values "might result in underestimating the
  uncertainty" of the affected parameters [src: arXiv:2207.06910, Sect. IV.1].
  Test: report the condition number and the inversion method.
- **Face-on counterparts.** Ill-conditioned FIM and invalid `2/SNR` (Step 3).
  Test: an inclination prior or selection-aware treatment; the ET science case
  points to a dedicated method [src: arXiv:2503.12263, Sect. 2.3.1].
- **Rate optimism.** BNS rates toward the upper range after O4 [src:
  arXiv:2503.12263, Sect. 2.3.1]; the kilonova route scales with that rate
  [src: arXiv:2303.15923, Sect. 6.4.1]. Test: rerun at the lower bound.
- **Idealised counterpart search.** Threshold models without sky localisation
  or strategy overestimate by a factor of about 2 or more [src:
  arXiv:2609.12053, Sect. III, VI.1.2]. Test: a time-budgeted follow-up as in
  arXiv:2303.15923, Table 10.
- **Missing correlated errors.** A diagonal distance covariance omits a common
  calibration error [src: arXiv:2607.20413, Sect. 4]; see
  `systematics.md#detector-calibration-and-waveform-systematics` for its size.
- **Missing lensing term, or lensing selection.** Some forecasts omit lensing
  (De Leo et al., above). For high-redshift sources, magnification selection
  shifts the mean magnification from 1 and introduces "an irreducible
  (multiplicative) bias on the distance reconstruction, independent of the
  sample size" [src: arXiv:2204.05434, Sect. 3.2.1].
- **One catalogue realisation.** Population scatter between realisations is
  large for rare sources; 118 catalogues (arXiv:1601.07112) or 1000
  realisations (arXiv:2402.03120) were needed [src]. Colombo et al. warn that
  their single realisation should carry population uncertainties [src:
  arXiv:2609.12053, Sect. III].
- **Bright and dark sirens split without selection.** Removing bright events
  from the dark sample without modelling EM selection biases the low-mass
  spectrum [src: arXiv:2609.12053, VI.1.2]; see L2
  `physics-and-methods.md#hierarchical-likelihood-and-selection-function`.

## Reading list
<!-- key: reading-list -->

- Method: Tamanini et al. 2016, arXiv:1601.07112 — the per-event error budget
  (instrument, lensing, peculiar velocity, photo-z) and catalogue averaging.
- Critique: Vallisneri 2008, arXiv:gr-qc/0703086 — when a Fisher forecast of GW
  parameter errors can be trusted.
- Code: Iacovelli et al. 2022, arXiv:2207.06910 — GWFAST, inversion options and
  comparison with real events. Dupletsa et al. 2023, arXiv:2205.02499 — GWFISH.
- Application: Branchesi et al. 2023, arXiv:2303.15923, Sect. 6.4.1 — ET
  geometries, kilonova and GRB counterparts, time-budgeted Rubin follow-up.
- Review: ET science case, arXiv:2503.12263, Sect. 2.3.1 — updated numbers and
  the limits of `2/SNR`.
- Application: Chen et al. 2024, arXiv:2402.03120 — XG networks, golden dark
  against bright sirens, population assumptions.
- Application: De Leo et al. 2026, arXiv:2607.20413 — where bright-siren
  information on H0 saturates in redshift.
- Application: Colombo et al. 2026, arXiv:2609.12053 — O5 counts and EM
  thresholds in a joint bright–dark population model.
- Review: LISA Cosmology Working Group, arXiv:2204.05434, Sects. 2.2–2.3 —
  source classes, counterpart strategy, lensing as the high-z floor.

## Not verified
<!-- key: not-verified -->

- The method cited in the ET science case for overcoming FIM limits with
  GRB-selected events (its ref. 1170) was not identified: the HTML rendering
  of arXiv:2503.12263 stops before the reference list. [src: Sect. "Bright sirens."]
- The origin of the `σ_lens` fitting formula (ref. 87 of arXiv:1601.07112) and
  of `σ_v` (ref. 93) were not read.
- The GWFISH paper (arXiv:2205.02499) was not read beyond its title as listed
  in arXiv:2607.20413.
- The 90-event and 20-event figures of arXiv:2607.20413 quoted in L2 were not
  re-read here (only its Sect. 5.1).
- Cosmic Explorer, Einstein Telescope and LISA project milestones (as in L2).
