# Intrinsic scatter and dust models — cosmo-supernovae dossier

Scope: how the SN Ia colour and scatter population model of a BBC analysis
is written down, fitted to the data, put into the bias-correction
simulations and turned into a systematic, and how to choose between the
dust-based, spectral-variation and hierarchical treatments.
Snapshot: 2026-10-17.
From: Brout & Riess 2023 review (arXiv:2311.08253), Sects. 0.2–0.6;
DES-SN5YR methods (arXiv:2401.02945), Sects. IV.2.1 and VI.2.1–VI.2.2;
Union3 (arXiv:2311.12098), Sect. IV.3; Unite (arXiv:2609.05053), Sect. 4.3.

Already in L2, not repeated here: the list of scatter models with one line
each in `physics-and-methods.md#intrinsic-scatter-and-dust-models`; the
`sigma_mu` error budget equation and the fitted `alpha`, `beta`, `gamma`,
`sigma_gray` per analysis in
`physics-and-methods.md#the-tripp-relation-as-used-today`; the dust rows of
the DES, DES-Dovekie and Unite budgets in
`systematics.md#des-sn5yr-and-des-dovekie-arxiv-2401-02945` and
`systematics.md#unite-camilleri-et-al-2026-arxiv-2609-05053`; the size
statements and the Fitzpatrick-law implementation bug in
`systematics.md#intrinsic-scatter-and-dust-modelling` and
`systematics.md#milky-way-extinction`; the dust-versus-intrinsic debate on
the mass step in `open-questions.md#is-the-host-step-dust-intrinsic-or-a-symptom-of`.

## How it is done
<!-- key: how-it-is-done -->

Notation follows Brout & Scolnic 2021 (BS21, arXiv:2004.10206): `c_int` is
the intrinsic SALT colour, `E_dust` the host reddening `E(B−V)`, `beta_SN`
the intrinsic colour–luminosity slope, `R_V` the host extinction ratio and
`tau_E` the scale of the reddening distribution. DES-SN5YR writes `beta_int`
for `beta_SN` (arXiv:2401.02945, Sect. IV.2). `beta_SALT2` (or `beta`)
is the single slope fitted in the Tripp relation, which in this framework
is an effective quantity.

### Step 1. Write the colour model
<!-- key: step-1-write-the-colour-model -->

The observed colour is split into an intrinsic part and dust,
`c_obs = c_int + E_dust + epsilon_noise` (BS21, Eq. 9), with
`c_int ~ N(c̄, sigma_c)` (Eq. 10), `E_dust` exponential with
`P(E_dust) = tau_E^-1 exp(−E_dust/tau_E)` for `E_dust > 0` (Eq. 12),
`R_V ~ N(R̄_V, sigma_RV)` with individual values below 0.5 not allowed
(Eq. 13), and `beta_SN ~ N(β̄_SN, sigma_βSN)` drawn per SN (Eq. 14) [src:
Sect. III.3]. The magnitude change is

    Delta m_B = beta_SN c_int + (R_V + 1) E_dust + epsilon_noise   (BS21, Eq. 15)

`R_V + 1 = R_B` because the shift is in the B band [src: Sect. III.3]. The
DES-SN5YR methods paper writes the same correction as
`beta_int c_int + R_V E(B−V)_dust` and states that mean `R_V` values
differing by about 1.25 between high- and low-mass hosts reproduce the
mass step across colours [src: arXiv:2401.02945, Sect. IV.2].

Parameter count, which papers report differently:

- BS21: seven parameters describe one survey (`c̄, sigma_c, β̄_SN,
  sigma_βSN, R̄_V, sigma_RV, tau_E`); a separate `tau_E` for low- and
  high-redshift surveys makes eight, against nine for G10 or C11 with the
  SK16 populations [src: Sect. III.3].
- Dust2Dust, with `R̄_V`, `sigma_RV` and `tau_E` split on host mass and
  `tau_E` also on redshift group: 4 intrinsic-colour and 8 dust parameters
  [src: arXiv:2112.04456, abstract]. Unite calls this "12 free parameters"
  [src: arXiv:2609.05053, Sect. 4.3].
- Naming: the hand-tuned BS21 values are "BS21" (Pantheon+ used them); the
  fitted values are "P23" in Unite and DES-Dovekie and "P21" in DES-SN5YR
  [src: arXiv:2609.05053, Sect. 4.3 and its footnote].

### Step 2. Model the stretch population separately
<!-- key: step-2-model-the-stretch-population-separately -->

The stretch distribution and its host-mass dependence are taken from the
method of Popovic et al. 2021 and excluded from the dust fit, "as the BS21
model does not propose a relationship between `x1` and host-galaxy mass"
[src: arXiv:2112.04456, Sect. IV.3; arXiv:2401.02945, Sect. IV.2].

### Step 3. Fit the population parameters to the data
<!-- key: step-3-fit-the-population-parameters-to-the-data -->

BS21 matched simulations to data with four pseudo-χ² terms in bins of
colour: the colour histogram (Eq. 4), the Hubble-residual RMS (Eq. 5), the
mean Hubble residual (Eq. 6) and the fitted `beta_SALT2` (Eq. 7), summed in
Eq. 8; 100 data-sized SNANA realisations per model; a coarse grid followed
by gradient descent on 1D perturbations, because large simulations are
"prohibitive for out-of-the-box minimizers and Monte Carlo samplers" [src:
Sect. II.4]. The values were tuned this way, not sampled [src:
arXiv:2609.05053, Sect. 4.3].

Dust2Dust (Popovic et al. 2023, arXiv:2112.04456) replaces this by an
MCMC [src: Sect. IV.3]:

1. One large reference simulation with "bounding" distributions: a flat-top
   asymmetric Gaussian for each Gaussian parameter (Eq. 19), an exponential
   for `tau_E`; selection effects included.
2. At each step, events are kept with probability `p/p_ref` (Eqs. 17–18),
   so the selected sample follows the proposed parameters without a new
   simulation. The reason given: simulating anew at each step is too slow;
   the bounding functions gain about `1.3^4 ≈ 4` in efficiency over flat
   ones [src].
3. The kept sample is downsized to 5000 SNe to limit fluctuations; if it
   cannot be, the step gets log-likelihood −∞ [src].
4. The M11 (SALT2mu) fit is run on data and on the weighted simulation;
   `L = −χ²_Tot/2` (Eq. 21) is sampled with emcee [src].

`χ²_Tot` has seven terms (Eq. 20, Table 3): colour histogram; mean residual
versus colour and residual scatter versus colour, each split into low- and
high-mass hosts; `beta_SALT2`; `sigma_int` [src: Sect. IV.3]. The colour
metrics use 6 bins from `c = −0.2` to `0.25`, which hold more than 99 % of
the sample; scatter is the robust `sigma_r = 1.48 median(|X|)` (Eq. 12)
with error `sigma_r/sqrt(2N)` (Eq. 14) [src: Sect. IV.1]. What each metric
constrains: `R̄_V` sets the slope of residual versus colour; `sigma_RV` the
relation for the reddest SNe and the scatter versus colour; the `beta_SN`
distribution the fitted `beta_SALT2` and the scatter floor [src: Sect. IV.1].

The residuals in the fit are computed **without** bias corrections ("BBC0D")
"as bias corrections are estimated making strong assumptions on SN
colour/dust distribution" [src: arXiv:2401.02945, Sect. IV.2].

Chains for Pantheon+: 24 walkers, 18 900 steps after 100 burn-in, acceptance
15 %, autocorrelation time 100, "near the computation limits"; posteriors
uni-modal but not Gaussian; the chain means are the fiducial values [src:
arXiv:2112.04456, Sect. V.1]. Walker bounds [src: Table 4]: `c̄` [−0.3,
−0.04], `sigma_c` [0.01, 0.2], `R̄_V` [0.8, 4], `sigma_RV` [0.25, 4],
`tau_E` [0.05, 0.2], `β̄_SN` [1.0, 3.0], `sigma_βSN` [0, 1].

### Step 4. Put the model in the bias-correction simulation
<!-- key: step-4-put-the-model-in-the-bias-correction -->

The fitted model generates the SALT3 parameters of the BBC simulations
(arXiv:2401.02945, Sect. IV.2). Three settings follow from it:

- **No simulated step.** The DES baseline simulates no mass or colour step
  (`gamma = 0` in the simulation) but fits `gamma` on the data; a residual
  for `c < 0` SNe "not captured by simulations" is "captured by fitting for
  `gamma`" [src: Sect. IV.2]. BS21 had predicted that, done properly, no
  residual `gamma` would remain, and recommended not correcting for an
  observed `gamma` [src: arXiv:2004.10206, Sect. VI.2]; the DES fit finds
  it at > 5σ (see L2).
- **Error model.** `sigma_mu^2 = f(z, c, M*) sigma_S3fit^2 + sigma_floor^2(z,
  c, M*) + sigma_z^2 + sigma_vpec^2 + sigma_lens^2` (DES, Eq. 8), with
  `sigma_floor^2 = sigma_scat^2(z, c, M*) + sigma_gray^2` (Eq. 9); `f` and
  `sigma_scat` come from the bias-correction simulations so that the reduced
  χ² is about one in each `{z, c, M*}` cell; if `f < 1`, `sigma_floor` is set
  to 0 "to avoid negative covariances" [src: Sect. III.5]. The additive
  floor replaced the scale-only scheme of DES-SN3YR because with the BS21
  model `f` could be "much larger than unity, leading to pathologically
  large distance uncertainties"; both are unbiased on simulations [src].
- **Test of the model.** `sigma_gray`, global and fitted in BBC, "is
  expected to be zero if the scatter model used in the simulations is
  accurate"; this testability is the stated reason for the nominal choice
  over a constant floor, both recovering the input cosmology on 25
  simulations [src: Sects. III.5, VI.2.2].

### Step 5. Choose variants and test them against the data
<!-- key: step-5-choose-variants-and-test-them-against -->

DES-SN5YR carries as systematics three parameter sets drawn from the
Dust2Dust chains, the original BS21 values, the fit split on host `u−r`
colour, and the age model W22 [src: arXiv:2401.02945, Sect. VI.2.1]. Each
variant is scored by

    chi2_S = sum_i (mu_obs,S^i − mu_best-fit,S(z_i))^2 / sigma_mu,Nominal^2   (DES, Eq. 13)

with the nominal errors held fixed "to ensure that changes ... are not
driven by inflated/reduced uncertainties", over SNe with `P_Ia > 0.5`;
the scatter of `Delta chi2_S` is measured on 25 simulations of the nominal
model [src: Sect. VII.1]. All dust variants have `Delta chi2_S` between 0
and +15, within that scatter; G10 has `Delta chi2_S = 102` and is dropped,
C11 likewise [src: Sect. VII.1.1]. A variant that is disfavoured enters the
budget with small weight: in DES-Dovekie the `u−r` split gives the largest
shift, `delta w = 0.029`, but no contribution to the uncertainty, "likely
indicating that this particular systematic does not well-match the data"
[src: arXiv:2511.07517, Sect. 9.2.1].

### Step 6. Propagate the parameter uncertainty
<!-- key: step-6-propagate-the-parameter-uncertainty -->

Dust2Dust compares two ways [src: arXiv:2112.04456, Sect. V.3]:

1. Forward: 400 data-sized simulations with parameters drawn from the chains
   and 400 with the best fit, each through SALT2 fitting, BBC4D and `wfit`
   with a CMB prior; `sigma_w,sys = sqrt(STDEV(w_syst+stat)^2 −
   STDEV(w_stat)^2)` (Eq. 22) gives 0.014 ± 0.001.
2. Covariance: a nominal bias-correction simulation plus three at
   `Delta chi2 ≈ 10` from the best fit, in the covariance matrix: 0.011 on
   `w` and 0.145 km/s/Mpc on `H0` (Eqs. 23–24, Table 7).

The authors call the forward value an upper bound because the covariance
route was binned for consistency and an unbinned matrix can self-correct
[src]. These body numbers come from the HTML rendering, which is an earlier
arXiv version: its own abstract gives an "upper threshold" of 0.014(1) on
w. The current arXiv abstract gives `sigma_w = 0.005` and 0.145 km/s/Mpc
on H0 [src: abstract]; the current version's body was not read, so the
revised method behind 0.005 is under "Not verified". L2 quotes the current
abstract.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Dust-based or spectral-variation scatter
<!-- key: dust-based-or-spectral-variation-scatter -->

- **What G10 and C11 are.** Both are perturbations of the SALT spectral
  model that average to zero [src: arXiv:1209.2482, Sect. III.2]. G10: a
  coherent term `sigma_COH = 0.09` mag plus independent broadband scatter of
  about 0.07, 0.03, 0.02, 0.03, 0.06 mag at U, B, V, R, I, from the SALT2
  training residuals, turned into a wavelength function with nodes every
  800 Å. C11: a UBVRI covariance from SNfactory spectra, extended to an ad
  hoc U′ band at 2500 Å with 0.59 mag, interpolated and multiplied by 1.3
  [src: Sect. III.2, Table 4]. The achromatic fraction is given as about 75 %
  for G10 and 25 % for C11 by Dust2Dust [src: arXiv:2112.04456, Sect. V.1],
  and as 70 % achromatic and 25 % chromatic for G10, 70 % chromatic for C11,
  by DES-SN5YR [src: arXiv:2401.02945, Sect. VI.2.1].
- **What the data say.** With SK16 populations both reproduce the colour
  histogram (χ²_c 9.0 and 9.5 in 12 bins) but not the scatter versus colour
  (χ²_RMS 35 for C11, 68 for G10) nor, for C11, the mean residual (χ²_Δμ
  about 29, against about 12 for G10) [src: arXiv:2004.10206, Sect. III.2].
  Dust2Dust reaches a total χ² about two times smaller than BS21 and nearly
  five times smaller than G10 and C11 [src: arXiv:2112.04456, Sect. V.1].
  G10 and C11 assume a single colour slope; Dust2Dust finds
  `sigma_βSN > 0` at more than 3σ [src].
- **What the choice costs.** If the truth is BS20 and the bias correction
  uses G10 or C11, `w` is biased by −0.025 or −0.040 on simulations; on data
  the shifts are −0.033 and −0.041 [src: arXiv:2004.10206, Sect. V, Table 3],
  largest at `z < 0.1` and `z > 0.8`, up to about 0.05 mag in distance [src].
  These comparisons used 1D bias corrections without a host split, because
  BBC5D cannot correct for two colour slopes (`beta_SN` and `R_V`) [src:
  Sects. V, VI.2].

### Hand-tuned, MCMC-fitted or SBI-fitted parameters
<!-- key: hand-tuned-mcmc-fitted-or-sbi-fitted-parameters -->

| Parameter | BS21 (Table 1) | P21(M*) in DES-SN5YR (Table 3) |
|---|---|---|
| `c̄` / `sigma_c` | −0.084 ± 0.004 / 0.042 ± 0.002 | −0.07 / 0.053 |
| `β̄_SN` / `sigma_βSN` | 1.98 ± 0.18 / 0.35 ± 0.20 | 2.07 / 0.22 |
| `R̄_V`, `sigma_RV`, high-mass | 1.50 ± 0.25, 1.3 ± 0.2 | 1.66, 0.95 |
| `R̄_V`, `sigma_RV`, low-mass | 2.75 ± 0.35, 1.3 ± 0.2 | 3.25, 0.93 |
| `tau_E` high / low mass, low-z | 0.19 ± 0.08 / 0.01 (+0.05/−0.01) | 0.11 / 0.14 |
| `tau_E` high / low mass, high-z or DES | 0.15 ± 0.02 / 0.12 ± 0.02 | 0.15 / 0.12 |

BS21 prints `β̄_SN − 1 = 0.98` [src: arXiv:2004.10206, Table 1];
the DES values are from arXiv:2401.02945, Table 3 [src]. The `u−r` fit
(red/blue hosts split at `u−r = 1`) gives `R_V` 1.5 and 3.05 [src: Table 3].
Dust2Dust on Pantheon+ finds `c̄ = −0.077 ± 0.006`, `sigma_c = 0.058 ±
0.005`, `β̄_SN = 2.064 ± 0.174` with an uncertainty on `sigma_βSN` about
four times smaller than BS21, all four `tau_E` between 0.08 and 0.11, and
`R̄_V` differing between mass bins at 2.8σ [src: arXiv:2112.04456,
Sects. V.1–V.2].

Stjörnumál (Popovic et al. 2026, arXiv:2607.28725) keeps the Dust2Dust
importance sampling but replaces the χ² by neural posterior estimation on
the catalogue `{c, m_B, x1, z, errors, mu, M*, mu_RES}` [src: Sects. 4,
4.1]. Its stated reasons: Dust2Dust's "long convergence time and inability
to compare models in a statistically-principled way" [src: Sect. 1]. What
changes:

- Model comparison by Bayes factor: two-population ("Banana Split") models
  are disfavoured at log10 BF = 1.90 and 3.4 on DES-SN5YR; single-`R_V` is
  the worst model on the Dust2Dust metrics (χ²/ν about 65) [src: Sect. 8.1].
- Lower `R_V` limit 1.2, following BayeSN, against the "less-realistic"
  `R_V > 0.4` of Dust2Dust [src: Sect. 1]; with that truncation the
  expected `R_V` is 2.21 (high mass) and 3.08 (low mass),
  `Delta E(R_V) = 0.8`, and `gamma = 0` corresponds to `Delta E(R_V) = 0.6`
  [src: Sect. 8.2, Eq. 19].
- Distances move little between models: `d mu/dz < 0.025` on a simulation
  50 times the DES-SN5YR size [src: Sect. 8.3].
- Limits stated: `alpha` and `beta` are fixed (0.145, 3.1) when computing
  `mu_RES` and cannot be resampled; `beta_int` and `gamma` depend strongly
  on the assumed cosmology, and `beta_int` and `R_V` shift beyond 1σ for
  `Delta beta_SALT = 0.2` [src: Sects. 4, 7.3].

### Host tracer: stellar mass, colour or age
<!-- key: host-tracer-stellar-mass-colour-or-age -->

- DES-SN5YR repeats the Dust2Dust fit split on rest-frame `u−r` (Table 3)
  after reproducing the steeper `x1`–`u−r` correlation, and then measures a
  colour step `gamma_u−r` instead of a mass step [src: arXiv:2401.02945,
  Sects. IV.2.1, VI.2.1].
- W22 drives `R_V` from a galaxy evolution model: a Gaussian split on host
  mass (BS21), the same split on mass-weighted galaxy age, or a mean `R_V`
  linear in progenitor age with a width that also varies (Eqs. 14–16); its
  baseline uses `alpha_sim = 0.15`, `β̄ = 1.98`, `sigma_β = 0.35` [src:
  arXiv:2207.05583, Sects. 3.2.4–3.2.5, 3.5]. DES-Dovekie carries it as the
  "W22" variant with a colour step [src: arXiv:2511.07517, Sect. 7.2].
- Host mass is kept nominal because it is "the host property most robust to
  limited photometric information", while "not necessarily the most
  accurate tracer" [src: arXiv:2511.07517, Sect. 7.2].

### Population model in simulations (BBC) or latent colours (UNITY)
<!-- key: population-model-in-simulations-bbc-or-latent -->

UNITY1.5 does not simulate a dust population. Each SN has two latent
colours, `c_B^true` from a Gaussian and `c_R^true` from an exponential, with
separate slopes, described as "very similar in detail to a broken-linear
relation" [src: arXiv:2311.12098, Sect. IV.1.1]. The authors reject the
naive split of SNe at a colour cut because Eddington bias causes "large
biases in both the slopes and intercepts on either side of the cut" [src].
Unexplained dispersion is per dataset, shared between `m_B`, `x1`, `c` by
global simplex fractions scaled by `{1, 0.14^−2, 3^−2}` (Eq. 9) rather than
`{1, alpha^−2, beta^−2}`, because the latter would cancel `alpha` and `beta`
and put all the dispersion in `m_B` [src: Sect. IV.3]. SALT3 model
uncertainties, several hundredths of a magnitude in distance, are treated as
measurement errors, not as unexplained dispersion [src: Sect. IV.3,
Fig. 6 caption].

### Weight of blue against red SNe
<!-- key: weight-of-blue-against-red-sne -->

BS21 finds an RMS of about 0.1 mag for blue, "dust-free" colours against
about 0.18 for red, a blue SN being about three times more constraining,
with smaller bias corrections and `gamma` consistent with zero; they suggest
weighing this in survey strategy [src: arXiv:2004.10206, Sect. VI.2]. No
current analysis restricts its sample to blue SNe.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| BS21 parameters per survey | 7, 8 with two `tau_E` | BS21 | arXiv:2004.10206 | Sect. III.3 |
| Dust2Dust parameters | 4 intrinsic + 8 dust | Pantheon+ | arXiv:2112.04456 | abstract |
| Colour bins of the fit | 6, `c` from −0.2 to 0.25 | Dust2Dust | arXiv:2112.04456 | Sect. IV.1 |
| Weighted simulation size | 5000 SNe per step | Dust2Dust | arXiv:2112.04456 | Sect. IV.3 |
| Chain | 24 walkers, 18 900 steps, acceptance 15 %, τ_auto 100 | Pantheon+ | arXiv:2112.04456 | Sect. V.1 |
| Fit quality | χ²_Tot 129 on data; 42–105 (mean 70) on 16 simulations | Pantheon+ | arXiv:2112.04456 | Sect. V.1 |
| Parameter recovery | 12 consistent; low-mass `sigma_RV` biased 2.9σ; errors underestimated, within 15 % | 16 simulations | arXiv:2112.04456 | Sect. V.1 |
| `sigma_w` from parameter uncertainty | 0.014 ± 0.001 (forward), 0.011 (covariance); abstract 0.005 | Pantheon+ | arXiv:2112.04456 | Sect. V.3, Table 7, abstract |
| `sigma_H0` from parameter uncertainty | 0.145 km/s/Mpc | Pantheon+ | arXiv:2112.04456 | Table 7 |
| Mean-`R_V` difference reproducing the step | about 1.25 | DES-SN5YR | arXiv:2401.02945 | Sect. IV.2 |
| `Delta chi2_S` of dust variants | 0 to +15; G10 +102 | DES-SN5YR | arXiv:2401.02945 | Sect. VII.1.1 |
| `w` bias, wrong scatter model in bias correction | −0.025 (G10), −0.040 (C11) on sims; −0.033, −0.041 on data | 1445 SNe | arXiv:2004.10206 | Table 3 |
| Distance difference between colour models | up to ~0.05 mag at z < 0.1 and z > 0.8 | compiled sample | arXiv:2004.10206 | Sect. V |
| RMS blue vs red | ~0.1 vs ~0.18 mag | compiled sample | arXiv:2004.10206 | Sect. VI.2 |
| G10 broadband scatter | 0.07, 0.03, 0.02, 0.03, 0.06 mag (UBVRI) + 0.09 coherent | SNLS/SDSS sims | arXiv:1209.2482 | Sect. III.2 |
| UNITY dispersion scaling | `{1, 0.14^−2, 3^−2}` | Union3 | arXiv:2311.12098 | Eq. 9 |
| Expected `R_V`, truncated at 1.2 | 2.21 (high mass), 3.08 (low mass) | DES-SN5YR, SBI | arXiv:2607.28725 | Sect. 8.2 |
| Distance change across population models | `d mu/dz < 0.025` | DES-SN5YR, SBI | arXiv:2607.28725 | Sect. 8.3 |
| `sigma_int` nominal vs no mass step | 0.055 vs 0.089 | DES-SN5YR, SBI | arXiv:2607.28725 | Sect. 8.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Parameter sets that do not match their source.** The DES-SN5YR "BS20"
  column (arXiv:2401.02945, Table 3) lists `R_V = 1.25` for high-mass hosts
  and `tau_E = 0.10` for low-z low-mass hosts, where BS21 Table 1 has
  1.50 ± 0.25 and 0.01 (+0.05/−0.01) [src: both tables]. DES-Dovekie states
  that this variant had "adjusted parameters (specifically the `tau`
  parameters do not match BS21) ... though the provenance of these changes
  has been lost" and keeps it [src: arXiv:2511.07517, Sect. 7.2]. Test:
  compare any variant table with the original paper before citing a
  "BS21" result.
- **Swapped labels in prose.** The comparison text of Dust2Dust attributes
  `R̄_V` of 1.5 to low-mass and about 3.0 to high-mass hosts in BS21 [src:
  arXiv:2112.04456, Sect. V.2], the reverse of BS21 Table 1 and of the DES
  table, where high-mass hosts have the lower `R_V`. Read values from the
  tables.
- **Too few draws for the systematic.** Unite reports that independent work
  "suggested that the three sets of dust parameters used as systematic
  variations may not accurately capture the range of systematic
  uncertainty"; it tests ±1σ and ±2σ shifts of the most influential
  parameters and finds only a data–simulation mismatch in the RMS for
  `c > 0.2`, meaning the errors there may be overestimated [src:
  arXiv:2609.05053, App. B].
- **Model not good enough for the data.** Data χ²_Tot = 129 against a
  simulation mean of 70: the authors conclude that "improvements to the
  model, notably `sigma_r`, are likely needed" [src: arXiv:2112.04456,
  Sect. V.1]. Test: run the fit on data-sized simulations of the best fit
  and compare the χ² distribution.
- **Uncorrected distances used to estimate `Delta w`.** Comparing distances
  without bias corrections assumes selection effects cancel between
  variants; a calibration test gave `Delta w = 0.10` that way against 0.02
  end to end [src: arXiv:2607.28725, Sect. 8.3 and footnote].
- **Population fit tied to a cosmology and to `alpha`, `beta`.** SBI fits
  show `beta_int` and `gamma` depend strongly on the simulated `w` and on
  the `beta_SALT` used for `mu_RES` [src: arXiv:2607.28725, Sect. 7.3].
  Test: refit with the simulator cosmology and `beta` shifted.
- **Residual `gamma` read as physics.** The baseline simulation has no step,
  so the fitted `gamma` absorbs whatever the dust model misses for blue SNe
  [src: arXiv:2401.02945, Sect. IV.2]; its value depends on the population
  model (see `results.md#the-host-mass-step`).
- **SALT trained with one colour component.** BS21 asks that the dust model
  be "integrated into the SALT2 training, which currently only accounts for
  one component of the observed SN Ia color" [src: arXiv:2004.10206,
  Sect. VI.2]. No BBC analysis read here has done this; joint training is
  the BayeSN route (see `deep/light-curve-models.md`).
- **Errors inflated by a scale factor.** With a dust model the scale-only
  error scheme gives pathologically large errors [src: arXiv:2401.02945,
  Sect. III.5]; check which scheme an analysis used before comparing its
  `sigma_int`.

## Reading list
<!-- key: reading-list -->

- Review: Brout & Riess 2023, arXiv:2311.08253 — why colour-dependent
  scatter points to dust and why it matters for `w` and not for `H0`.
- Foundation: Brout & Scolnic 2021, arXiv:2004.10206 — the model (Eqs.
  9–15), the four metrics and the cost of the wrong scatter model.
- Method: Popovic et al. 2023, arXiv:2112.04456 — Dust2Dust likelihood,
  reweighting, propagation to `w` and `H0`.
- Method: Kessler et al. 2013, arXiv:1209.2482 — how G10 and C11 are built
  as spectral perturbations.
- Application: Vincenzi et al. 2024, arXiv:2401.02945 — parameters,
  variants, error model and the `chi2_S` test.
- Application: Popovic et al. 2025, arXiv:2511.07517 — variants carried in
  DES-Dovekie and the lost-provenance warning.
- Alternative: Rubin et al. 2023, arXiv:2311.12098 — latent colours and
  per-dataset dispersion in UNITY.
- Alternative: Wiseman et al. 2022, arXiv:2207.05583 — age-driven `R_V`.
- Critique: Popovic et al. 2026, arXiv:2607.28725 — SBI successor, model
  comparison, cosmology dependence of the fit.
- Validation: Camilleri et al. 2026, arXiv:2609.05053 — App. B tests of the
  P23 model.

## Not verified
<!-- key: not-verified -->

- Dust2Dust Table 5 (fitted P23 values with errors) is not readable as text;
  only the values quoted in its Sect. V.2 prose are given.
- Guy et al. 2010 (G10) and Chotard et al. 2011 (C11) originals, Popovic et
  al. 2021 stretch populations (cited through arXiv:2401.02945), Amanullah
  et al. 2010 blue/red `beta` (cited through arXiv:2311.12098), and the
  announced Carreres et al. hierarchical dust model: not read.
- The body of the current version of arXiv:2112.04456, whose abstract gives
  `sigma_w = 0.005` (the HTML rendering read is an earlier version giving
  0.014): how the revised value was obtained.
