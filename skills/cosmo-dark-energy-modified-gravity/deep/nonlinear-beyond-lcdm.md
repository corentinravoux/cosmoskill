# Non-linear predictions beyond ΛCDM — cosmo-dark-energy-modified-gravity dossier

Scope: how predictions for dark-energy and modified-gravity models are
carried from linear theory to the mildly and fully non-linear scales that
clustering and lensing analyses use (perturbation-theory kernels,
power-spectrum ratios, halo-model reaction, emulators, N-body methods,
theory-error terms, lensing magnification), and what each approximation
costs in bias or constraining power.
Snapshot: 2026-10-17.
From: Euclid 2025 review (arXiv:2512.09748), Sects. 6–8; DESI DR1
modified-gravity key paper (arXiv:2411.12026), Sect. 2.3 and App. A.

Already in L2, not repeated here: what DESI DR1 (EdS kernels checked against
fkpt), DES Y3 (Halofit ratio, "linear" scale cuts keeping 256 of 462 points;
arXiv:2207.05766, Sect. II.4, Table 1),
KiDS-1000 (ReACT on HMcode, cosmic shear only) and DESI DR1 `f(R)` (fkpt,
`k_max = 0.17 h/Mpc`, screening neglected) did, in
`physics-and-methods.md#what-the-main-modified-gravity-analyses-did`; the
statement that weak-lensing gravity tests are limited by non-linear modelling
in `systematics.md#modified-gravity-non-linear-scales-bias-and`; ReACT in
`physics-and-methods.md#codes`.

Notation. `P(k, z)` is the non-linear matter power spectrum; `P_L` the
linear one; `k` in `h/Mpc` unless stated; `ell` a multipole; `|f_R0|` the
Hu–Sawicki background field today; nDGP the normal branch of the
Dvali–Gabadadze–Porrati model; EdS means Einstein–de Sitter perturbation
kernels; "screening" is the non-linear suppression of a fifth force.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Decide which regime the probe needs
<!-- key: step-1-decide-which-regime-the-probe-needs -->

| Probe | Scales | Prediction route | Place read |
|---|---|---|---|
| Spectroscopic clustering multipoles | quasi-linear, `k ≲ 0.2–0.3` | one-loop perturbation theory (EFTofLSS or TNS) with modified kernels | arXiv:2512.09748, Sect. 6.1 |
| Weak lensing, photometric clustering, galaxy–galaxy lensing | to `k ~ 10` | the ratio `Xi = P/P_ΛCDM` from a fitting formula, an emulator or the halo-model reaction, multiplied by a ΛCDM emulator | arXiv:2512.09748, Sect. 6.2 |
| Anything beyond the validity of the above | fully non-linear | N-body codes modified for the model | arXiv:2512.09748, Sect. 8 |

Perturbation theory "is not applicable" at the wavenumbers that photometric
probes reach [src: arXiv:2512.09748, Sect. 6.2].

### Step 2. Spectroscopic clustering: choose the kernels
<!-- key: step-2-spectroscopic-clustering-choose-the -->

Both EFTofLSS and TNS need density and velocity kernels to third order. In
ΛCDM the analytic EdS forms are an excellent approximation and allow FFT
methods; beyond ΛCDM the exact kernels must be solved numerically, which is
"largely unfeasible" inside a parameter inference [src: arXiv:2512.09748,
Sect. 6.1]. Euclid tested four approximations against N-body halo `P_0`,
`P_2` at `z = 1`, using the minimum reduced χ² as a function of `k_max`
with nuisance parameters fitted and cosmology fixed: kernel approximation,
bias model, massive-neutrino treatment, IR resummation; three codes (PBJ,
PyBird, MG-Copter, the last exact but slowest) [src: same; Euclid
Collaboration: Bose et al. 2024, arXiv:2311.13529, abstract].

Results [src: arXiv:2512.09748, Sects. 6.1.1–6.1.3]:

- **Scale-independent models** (`w0wa`, nDGP, dark scattering): negligible
  degradation from EdS kernels within current constraints; standard
  Eulerian bias and wiggle/no-wiggle resummation perform as in ΛCDM;
  screening in the nDGP kernels can be neglected at percent level. Against a
  mock with a Euclid volume, EdS without screening gives `chi2_red ≈ 1` for
  `k_max ≤ 0.3`; ignoring massive neutrinos when the mock has
  `Σm_nu = 0.16 eV` does the same, in ΛCDM and `w0wa`.
- **Hu–Sawicki `f(R)`**: EdS and no-screening break down for dark-matter
  multipoles. A "ΛCDM-screened approximation", FFT-compatible, matches the
  exact kernels to 1% for all multipoles including `P_4` down to
  `k = 0.25` at `z = 1`. For halo multipoles, however, all approximations
  give `chi2_red` comparable to the exact kernels up to `k_max = 0.3`.
- **General**: Eulerian bias and the local Lagrangian relation do not
  degrade fits; TNS fits slightly better than EFTofLSS; both reach
  `chi2_red ≈ 1` for `0.19 ≤ k_max ≤ 0.21` in ΛCDM and beyond.

The authors' reading of the same result: a single redshift bin with `P_0`,
`P_2` carries little information on screening or neutrino mass, so
multiple bins, higher multipoles, the bispectrum and lensing will be needed
[src: arXiv:2311.13529, abstract; arXiv:2512.09748, Sect. 6.1.1].

### Step 3. Photometric probes: predict the ratio Xi
<!-- key: step-3-photometric-probes-predict-the-ratio-xi -->

The quantity modelled is `Xi(k, z) = P(k, z)/P_ΛCDM(k, z)`
(arXiv:2512.09748, Eq. 53). The authors' reasons [src: Sect. 6.2]: for
models with a ΛCDM background (`f(R)`, nDGP) it isolates the structure-
formation effect; `P_ΛCDM` can come from emulators calibrated on
high-resolution simulations; modified-gravity simulations are expensive and
the ratio cancels cosmic variance and much of the resolution error, so
cheaper simulations suffice. Then `P_f(R) = Xi × P_ΛCDM`, the cosmology
dependence entering mainly through `P_ΛCDM` [src: arXiv:2409.03524, Sect.
5.2].

Available predictions for Hu–Sawicki `f(R)` [src: arXiv:2512.09748, Sect. 6.2.1]:

| Prediction | Basis | Cosmology dependence | Validity stated |
|---|---|---|---|
| Fitting formula (Winther et al. 2019) | ELEPHANT/ECOSMOG simulations, tested on DUSTGRAIN/MG-Gadget | none, with separate corrections for `sigma8`, `Omega_m,0` | used in Euclid Fisher forecasts |
| FORGE | 50 MG-Arepo runs in `f_R0`, `Omega_m,0`, `sigma8`, `h`; GP emulation | emulates the ratio to halofit; the ΛCDM/halofit correction exists only at the reference cosmology | — |
| mgemu | COLA with approximate screening; `Omega_m,0 h^2`, `sigma8`, `n_s`, `log10 f_R0` | yes | `k < 1` |
| e-MANTIS | ECOSMOG; `f_R0`, `Omega_m,0`, `sigma8`; GP emulation | yes | agreement with the fitting formula better than 3% at `k < 10`, with mgemu 1% at `k < 1`, with FORGE 1% (3%) for `|f_R0| = 10^-6` (`10^-5`) at `k < 10`, all at `z = 0` |
| ReACT (halo-model reaction) | halo model plus spherical collapse | yes, through the pseudo spectrum | 4% to `k = 3` for `|f_R0| ≤ 10^-5` with massive neutrinos; 2% without |

### Step 4. The halo-model reaction in detail
<!-- key: step-4-the-halo-model-reaction-in-detail -->

ReACT (Cataneo et al. 2019, arXiv:1812.05594) defines a "pseudo" ΛCDM
cosmology whose initial conditions are adjusted so that its linear spectrum
equals the target's at the output redshift,
`P_L^pseudo(k, z_f) = P_L^real(k, z_f)` (Eq. 51), and models the reaction
`R(k, z) ≡ P^real/P^pseudo` (Eq. 52) as
`R = {[(1 − E) e^{−k/k_*} + E] P_L^real + P_1h^real}/{P_L^real + P_1h^pseudo}`
(Eq. 53), with `E(z) = P_1h^real(k→0)/P_1h^pseudo(k→0)` (Eq. 54) and `k_*`
from perturbation theory; `R → 1` on linear scales and
`≈ P_1h^real/P_1h^pseudo` on small scales; intermediate scales
`0.1 ≲ k ≲ 1` are controlled by the mass-function ratio [src: Sect. 3.3].
The reason for the pseudo cosmology: matching linear spectra makes the mass
functions similar, so the reaction avoids the usual halo-model errors in
the transition region [src: same]. Accuracy: within 1% for `k ≲ 1` in all
cases studied, provided accurate mass-function ratios from simulations;
without them `≲ 3%` [src: Sect. 6]. The reaction is used only above
`k = 0.01` because of the constant one-halo tail at low `k` [src: Sect.
3.3, footnote]. For dark energy, the reaction applied to a ΛCDM emulator
reproduced the emulator's own `w ≠ −1` output, showing that ΛCDM emulators
can be extended analytically [src: Sect. 6].

For phenomenological μ–Σ forecasts Euclid uses ReACT and brackets
screening by two limits: unscreened (US), modifications on all non-linear
scales, and super-screened (SS), the spectrum returning to GR "as quickly
as possible" from linear to non-linear scales [src: arXiv:2512.09748, Sect.
4.1.1].

### Step 5. Set the scale cuts
<!-- key: step-5-set-the-scale-cuts -->

Euclid forecast settings [src: arXiv:2512.09748, Sect. 2.2]:

| Setting | Weak lensing | Photometric clustering and GGL | Spectroscopic |
|---|---|---|---|
| Optimistic | `10 ≤ ell ≤ 5000` | `10 ≤ ell ≤ 3000` | `0.001 ≤ k ≤ 0.30` |
| Pessimistic | `ell ≤ 1500` | `ell ≤ 750`, plus `z < 0.9` when all probes are combined | `k ≤ 0.25` |
| Quasi-linear | — | — | `k ≤ 0.15` |

For μ–Σ, conservative cuts of `k_max = 0.25 Mpc^-1` (3×2pt) and
`0.1 Mpc^-1` (spectroscopic) give relative errors on `mu_0` and `Sigma_0`
of 278% and 35% (SS) or 169% and 22% (US) from 3×2pt alone, and 24% and 3%
(SS) or 23% and 3% (US) for 3×2pt + spectroscopic (**forecast**) [src:
arXiv:2512.09748, Sect. 4.2.1]. More optimistic cuts bring both to about 1% "however, such
an improvement requires ensuring that the modelling of nonlinear scales can
reach a high level of accuracy" (**forecast**) [src: same]. ReACT's
accuracy rules out the optimistic weak-lensing cut (`ell_max = 5000`); it
can be applied only at `ell_max = 1500` [src: Sect. 6.2.1].

### Step 6. Add a theory-error term when predictions disagree
<!-- key: step-6-add-a-theory-error-term-when-predictions -->

Euclid propagates a relative error `alpha(k, z)` on `P` (Eq. 36) to an
angular-spectrum error `E_ij^XY(ell)` (Eq. 35), shifts the model covariance
by `epsilon_ell L^{1/2} E(ell)` with one nuisance `epsilon_ell ~ N(0, 1)` per
multipole and `L = ell_max − ell_min + 1` (Eq. 37), adds `Σ epsilon_ell^2`
to the χ² (Eq. 38) and minimises over the `epsilon_ell` (Eq. 39), after
Audren et al. 2013; errors are taken as uncorrelated in `ell`, "the most
conservative approach" [src: arXiv:2409.03524, Sect. 6.1]. The `L^{1/2}`
normalisation makes a 1σ theory error at every `ell` raise χ² by one [src:
same].

### Step 7. Fully non-linear: modified N-body
<!-- key: step-7-fully-non-linear-modified-n-body -->

By class of model [src: arXiv:2512.09748, Sect. 8]:

- **Smooth dark energy, `w(a)`**: only `H(z)` changes, entering the growth
  equation `δ̈_m + 2H δ̇_m = 4 pi G_N (rho_m δ_m + rho_DE δ_DE)` (Eq. 57)
  with `δ_DE = 0`; a tabulated `H(z)` from a Boltzmann code is enough (Sect.
  8.1).
- **Low sound speed or coupled dark energy**: dark-energy perturbations
  source the potential; a coupling adds a fifth force
  `v̇ = −c^2 ∇Phi − c^2 beta(phi) ∇δphi` (Eq. 58), with `δphi ≈ 2 beta_i Phi_i`
  for a dark-matter-only coupling (Eq. 59), implemented by rescaling forces
  per particle species, plus a time-varying particle mass and a "friction"
  term `beta(phi) phi̇ v` (Eq. 60); dark scattering adds a momentum-exchange
  drag (Eq. 61) (Sect. 8.2).
- **Screened models**: a non-linear field equation
  `□phi = S(phi, ∇phi, ∇∇phi, rho_m)` (Eq. 62), with field redefinitions for
  `f(R)` and operator splitting for Vainshtein models (DGP, cubic and
  quartic Galileons); approximate screening factors or linearised equations
  as cheaper alternatives (Sect. 8.3).
- **Quasi-static approximation**: time derivatives of the scalar
  perturbation dropped, valid inside the scalar's sound horizon; adopted by
  most codes, with non-static codes available (Sect. 8.4).

Code agreement: for `f(R)`, DGP and symmetron runs from the same initial
conditions, the fractional deviation of `P(k)` from ΛCDM agrees "to better
than 1% up to k ~ 5–10 h/Mpc", and the quasi-static limit is "a very good
approximation" even for the symmetron, where non-static effects should be
largest (Winther et al. 2015, arXiv:1506.06384) [src: abstract]. The Euclid
code comparison reports "a high degree of agreement" among codes across
models (arXiv:2409.03522) [src: abstract].

### Step 8. Model lensing magnification in number counts
<!-- key: step-8-model-lensing-magnification-in-number -->

With local count slope `(5/2) s(z, F_lim) ≡ −∂log10 N(z, F > F_lim)/∂log10 F_lim`
(arXiv:2512.09748, Eq. 54), photometric clustering spectra gain
`(5 s_j − 2) C^Gκ + (5 s_i − 2) C^κG + (5 s_i − 2)(5 s_j − 2) C^κκ` (Eq. 55)
and galaxy–galaxy lensing gains `(5 s_i − 2) C^κL` (Eq. 56) [src: Sect. 7.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### EdS kernels or exact kernels
<!-- key: eds-kernels-or-exact-kernels -->

For scale-independent modifications EdS kernels cost nothing measurable up
to `k_max = 0.3` at Euclid volume; for `f(R)` they fail for dark matter
but not, at current precision, for halo multipoles [src:
arXiv:2512.09748, Sects. 6.1.1–6.1.2]. DESI DR1's check against fkpt (L2)
is the same test on its data. Cost of the exact route: slow, numerically
fragile kernels (MG-Copter) [src: Sect. 6.1].

### Emulator, fitting formula or reaction
<!-- key: emulator-fitting-formula-or-reaction -->

- **Same data, different predictions.** Synthetic weak-lensing data from
  FORGE at `log10 |f_R0| = −5.301`, fitted by the others: 1D bias in
  `log10 |f_R0|` of 0.273 (fitting formula) and 0.602 (e-MANTIS) in the
  optimistic setting; 0.441, 0.518 and 3.11 (ReACT) in the pessimistic
  setting, with a 1D bias in `h` of 0.988 and 0.812 for the fitting formula
  and e-MANTIS [src: arXiv:2409.03524, Sect. 4.2.2, Tables 8–9]. The 1D
  bias is `B_1D = (mu − mu_FORGE)/sigma_FORGE` (Eq. 30). The authors call
  the choice of FORGE as truth "disadvantageous" to ReACT, so the estimate
  is conservative; with e-MANTIS as truth, ReACT's mean is closer but the
  bias remains at the 3σ level because e-MANTIS errors are smaller [src:
  same].
- **Why they differ.** Against an MG-Arepo training node, FORGE and
  e-MANTIS agree within 1% to `k = 3`, the fitting formula and ReACT within
  1% to `k = 1`; the FORGE departure on the earlier comparison runs is
  attributed to emulation error and to its halofit calibration [src:
  arXiv:2409.03524, Sect. 4.1.1]. The fitting formula lacks cosmology
  dependence in `Xi`, which shows up as a bias in `h` [src: Sect. 4.2.2].
- **Summary statement of the review.** "A few percent difference in the
  nonlinear matter power spectrum prescription can bias the inference of the
  model parameter, `f_R0`, at the 2σ-level" (**forecast**) [src:
  arXiv:2512.09748, Sect. 6.2.1].

### Theory error or tighter cuts
<!-- key: theory-error-or-tighter-cuts -->

Theory errors "can mitigate biases, but come at the cost of significantly
worse constraints"; better emulators reduce the cost [src:
arXiv:2512.09748, Sect. 6.2.1]. For ReACT the error term alone did not
remove the bias; a fiducial-cosmology correction
`Xi_ReACT-FORGE = Xi_ReACT (Xi_FORGE/Xi_ReACT)_fiducial` (Eq. 42) was also
needed, after which the input was recovered; with e-MANTIS as truth the
error term reduced biases by both widening errors and moving the means
[src: arXiv:2409.03524, Sect. 6.3]. The alternative is the pessimistic cut,
which avoids the baryon-induced bias "at the expense of weaker
constraints" [src: abstract].

### Baryons and modified gravity together
<!-- key: baryons-and-modified-gravity-together -->

Baryonic feedback changes the lensing spectrum at `ell > 100` in a way
similar to `f(R)` [src: arXiv:2409.03524, Sect. 5.2]. With BCemu
baryons in the optimistic setting, the 1σ error on `log10 |f_R0|` grows
from 0.088 to 0.281 (e-MANTIS as data and model), still within the prior;
with FORGE as data, the prediction difference is absorbed by the baryon
parameter `log10 M_c` and `h`, and the 95.5% limit `log10 |f_R0| < −5.477`
excludes the input −5.301; the profile likelihood gives a best fit −5.765
against a marginal mean −6.087 and `Δχ² = 2.657` at the input value,
showing part of the shift is a prior-volume effect [src: same]. The
pessimistic setting with ΛCDM synthetic data gives a "prior-independent"
`log10 |f_R0| < −5.6` (**forecast**) [src: abstract].

### Screening bracket for μ–Σ
<!-- key: screening-bracket-for-mu-sigma -->

US and SS bracket an unknown screening behaviour. With conservative cuts
the two give similar combined errors (24% and 23% on `mu_0`; 3% and 3% on
`Sigma_0`) but very different 3×2pt-only errors (278% and 169% on `mu_0`)
(**forecast**) [src: arXiv:2512.09748, Sect. 4.2.1]. A μ–Σ analysis using
non-linear scales should state which limit it assumes; the DES Y3 Halofit
ratio of L2 corresponds to neither and is applied only with linear cuts.

### Magnification: model it, fix it, or ignore it
<!-- key: magnification-model-it-fix-it-or-ignore-it -->

- Photometric clustering alone: including magnification reduces the `w0`,
  `wa` errors by about 30% (slope known), 15% (slope free) or 20% (10%
  prior on the slope) (**forecast**) [src: arXiv:2512.09748, Sect. 7.1.1].
- Neglecting it biases `w0`, `wa` by about 1σ (photometric clustering) and
  2–5σ (clustering + lensing + GGL); the large values are "not
  quantitatively trusted" because they come from a first-order expansion,
  but the authors call modelling it "imperative" (**forecast**) [src: Sect.
  7.1.2].
- Spectroscopic 2PCF: shifts below 0.5σ for all `w0waCDM` parameters,
  0.1σ for `w0`, `wa`, but up to 1σ on the growth parameter in the highest
  redshift bin, unacceptable for a gravity test; precomputing magnification
  at a fixed CMB cosmology reduces the shift to 0.13σ (`w0waCDM`) and 0.1σ
  (**forecast**) [src: arXiv:2512.09748, Sects. 7.2.2–7.2.3].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Context | Source | Place read |
|---|---|---|---|---|
| EdS/no-screening validity, scale-independent models | `chi2_red ≈ 1` to `k_max = 0.3` | Euclid-volume mock, `z = 1`, `P_0`, `P_2` | arXiv:2512.09748 | Sect. 6.1.1 |
| `chi2_red ≈ 1` range, TNS and EFTofLSS | `0.19 ≤ k_max ≤ 0.21` | N-body halo multipoles | arXiv:2512.09748 | Sect. 6.1.3 |
| ΛCDM-screened approximation | within 1% of exact kernels to `k = 0.25`, `z = 1` | `f(R)` dark-matter multipoles | arXiv:2512.09748 | Sect. 6.1.2 |
| ReACT accuracy | 1% for `k ≲ 1` (with mass-function ratios), `≲ 3%` without | `f(R)`, DGP, dark energy | arXiv:1812.05594 | Sect. 6 |
| ReACT accuracy | 4% to `k = 3` (massive neutrinos), 2% without, `|f_R0| ≤ 10^-5` | `f(R)` | arXiv:2512.09748 | Sect. 6.2.1 |
| mgemu range | `k < 1` | `f(R)` | arXiv:2512.09748 | Sect. 6.2.1 |
| N-body code agreement | better than 1% to `k ~ 5–10` | `f(R)`, DGP, symmetron | arXiv:1506.06384 | abstract |
| Nonlinear-model bias in `log10 |f_R0|` | 0.27–0.60σ (emulators, formula); 3.11σ (ReACT, pessimistic) | Euclid WL, FORGE truth | arXiv:2409.03524 | Tables 8–9 |
| `log10 |f_R0|` error with baryons | 0.088 → 0.281 | Euclid WL optimistic, e-MANTIS | arXiv:2409.03524 | Sect. 5.2 |
| Forecast limit | `log10 |f_R0| < −5.6`, pessimistic WL, ΛCDM data (**forecast**) | Euclid | arXiv:2409.03524 | abstract |
| μ–Σ relative errors, conservative cuts | `mu_0` 24% (SS), 23% (US); `Sigma_0` 3% (**forecast**) | Euclid 3×2pt + spectroscopic | arXiv:2512.09748 | Sect. 4.2.1 |
| Magnification neglect | ≈ 1σ (GCph), 2–5σ (GCph + WL + GGL) on `w0`, `wa` (**forecast**) | Euclid photometric | arXiv:2512.09748 | Sect. 7.1.2 |
| Magnification precomputed | shift 0.13σ (`w0waCDM`) | Euclid spectroscopic | arXiv:2512.09748 | Sect. 7.2.3 |
| ReACT low-`k` limit | used only for `k > 0.01` | halo-model tail | arXiv:1812.05594 | Sect. 3.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **A ΛCDM non-linear recipe applied to a modified model.** The common
  shortcut of applying a ΛCDM halofit ratio to a modified linear spectrum is
  what DES Y3 used only together with linear scale cuts (L2). For
  interacting dark energy, N-body runs show scale-dependent departures that
  ΛCDM-calibrated prescriptions miss (arXiv:2606.11368, abstract, see
  `deep/interacting-dark-energy.md`). Test: compare with a model-specific
  `Xi` or restrict to scales where linear and non-linear predictions differ
  by `Δχ² < 1` (the DES procedure in L2).
- **Emulator outside its training space.** FORGE spans a narrow `|f_R0|`
  prior and caused problems when used as the fitted model with baryons; its
  ΛCDM correction exists only at the reference cosmology [src:
  arXiv:2409.03524, Sect. 4.2.2; arXiv:2512.09748, Sect. 6.2.1]. Test:
  check the training ranges and the cosmology dependence of every factor.
- **A few-percent prediction difference read as a gravity signal.** Biases
  of 2–3σ in `f_R0` arise from differences between prescriptions [src:
  arXiv:2409.03524, Sect. 4.2.2]. Test: fit synthetic data made with one
  prescription using another, as Euclid does; include a theory-error term.
- **Baryons absorbing modified gravity, or the reverse.** Degenerate above
  `ell = 100` [src: arXiv:2409.03524, Sect. 5.2]. Test: profile likelihood
  next to the marginal; pessimistic cuts as a cross-check.
- **Screening ignored in the regime that needs it.** Single-bin `P_0`, `P_2`
  barely see screening [src: arXiv:2512.09748, Sect. 6.1.2], but weak
  lensing at high `ell` does; the US/SS spread is the size of the
  ignorance [src: Sect. 4.2.1]. Test: run both limits.
- **Quasi-static approximation outside the sound horizon.** Valid only
  inside the scalar's sound horizon [src: arXiv:2512.09748, Sect. 8.4]; the
  2015 comparison found it very good for the models tested [src:
  arXiv:1506.06384, abstract]. For other models, state the check.
- **Magnification left out of photometric counts.** Biases `w0`, `wa` by
  1–5σ in Euclid forecasts [src: arXiv:2512.09748, Sect. 7.1.2]; for
  spectroscopic growth up to 1σ at high redshift [src: Sect. 7.2.2]. Test:
  include it with a measured count slope, or precompute it.
- **Validation on simulation volumes smaller than the survey.** The Euclid
  kernel tests used Gaussian covariances for the simulation volume,
  "typically lower than the volume Euclid will probe", and repeated the key
  test with Euclid-volume mocks [src: arXiv:2512.09748, Sect. 6.1].

## Reading list
<!-- key: reading-list -->

- Review: Euclid Collaboration 2025, arXiv:2512.09748, Sects. 6–8 — kernel
  approximations, `Xi` predictions, theory errors, magnification, N-body
  methods.
- Method: Cataneo et al. 2019, arXiv:1812.05594 — halo-model reaction,
  pseudo cosmology (Eqs. 51–54).
- Code: Bose et al. 2020, arXiv:2005.12184 — ReACT (in L2).
- Method/validation: Winther et al. 2015, arXiv:1506.06384 — modified-gravity
  N-body code comparison and the quasi-static test.
- Method: Euclid Collaboration: Bose et al. 2024, arXiv:2311.13529 — EdS and
  screening approximations in spectroscopic clustering.
- Method: Euclid Collaboration: Adamek et al. 2024, arXiv:2409.03522 —
  numerical methods and code comparison beyond ΛCDM.
- Critique/application: Euclid Collaboration: Koyama et al. 2024,
  arXiv:2409.03524 — prescription-to-prescription biases, baryons, theory
  error (Eqs. 30, 35–42).
- Application: Ishak et al. 2024, arXiv:2411.12026 — EdS kernels checked
  against fkpt for DESI DR1 (in L2).
- Critique: Zhai et al. 2026, arXiv:2606.11368 — IDE non-linear structure
  versus ΛCDM-calibrated prescriptions.

## Not verified
<!-- key: not-verified -->

- The ReACT validation papers for phenomenological μ–Σ models (Srinivasan
  et al. 2021, 2024), the `w0wa` and nDGP validations (Bose et al. 2021,
  2023; Carrilho et al. 2022), the Winther et al. 2019 fitting formula, and
  the FORGE, mgemu and e-MANTIS papers: cited in arXiv:2512.09748, not read;
  no identifiers recorded.
- The results paper of the Euclid simulation suite (Euclid Collaboration:
  Rácz et al., cited in arXiv:2512.09748, Sect. 8): not read.
- Non-linear prescriptions used by any analysis of real data for `w0wa`
  beyond what L2 records (e.g. HMcode settings in DESI DR2 combinations
  with 3×2pt) were not read here.
- Audren et al. 2013, the origin of the theory-error recipe: cited in
  arXiv:2409.03524, not read.
