# Interacting dark energy — cosmo-dark-energy-modified-gravity dossier

Scope: how an interacting-dark-energy (IDE) fit is set up (coupling form,
sign convention, perturbation treatment, code, priors, data), why the
same background data that prefer `w0wa` also prefer a coupling, and what
separates the two descriptions; for a reader about to run or referee an
IDE analysis. The worked example is the coupled-fluid / coupled-quintessence
fit of the Zhang group (ePPF, IDECAMB); the fluid route with `w ≃ −1`
(Di Valentino and Nunes group), the geodesic interacting vacuum (Pan, Yang
et al.), pure momentum exchange (dark scattering) and the Planck 2015
collaboration analysis are given beside it, step by step.
Snapshot: 2026-10-22.
From: Li 2026 review (arXiv:2606.21826), Sects. III.1 and III.3.

Already in L2, not repeated here: the one-line claim "interacting dark
energy at 3–5σ" and its reading as one of several absorbers of the same
data mismatch (`systematics.md#combining-data-sets-that-disagree`,
`open-questions.md#does-modified-gravity-explain-the-desi-signal`), and
the table entry for the class in
`physics-and-methods.md#physical-classes-used-in-current-analyses`.

Notation. Subscripts `c` (cold dark matter) and `de` (dark energy); `w` is
the intrinsic equation of state of dark energy; `𝓗 = aH` the conformal
Hubble rate; a prime is a derivative with respect to conformal time; `Q`
the background energy-transfer rate; `δQ` its perturbation; `f` the
momentum-transfer rate. The sign convention differs between papers (see
"Choices"); this dossier follows Li et al. 2026 (arXiv:2601.07361), where
`Q > 0` means transfer from dark matter to dark energy.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Write the coupled conservation equations
<!-- key: step-1-write-the-coupled-conservation-equations -->

Only the total energy-momentum tensor must be conserved, so
`∇_ν T^ν_μ,de = −∇_ν T^ν_μ,c = Q_μ` (arXiv:2601.07361, Eq. 1;
arXiv:2606.21826, Eq. 2). In the background
`rho_de' + 3𝓗(1 + w) rho_de = a Q`, `rho_c' + 3𝓗 rho_c = −a Q`
(arXiv:2601.07361, Eqs. 7–8). A choice of `Q_μ` fixes `Q`, `δQ` and `f`
together [src: same, main text]. Linear perturbations follow Eqs. 9–10
of the same paper, with `Q = Q_de = −Q_c`, `δQ = δQ_de = −δQ_c`,
`f = f_de = −f_c` [src: Sect. I of the supplement].

The background effect can be read through effective equations of state,
`w_de^eff = w − aQ/(3𝓗 rho_de)` and `w_c^eff = aQ/(3𝓗 rho_c)`
(arXiv:2606.21826, Eqs. 9–10): with `w = −1` and `Q ≠ 0` the dark-energy
density is not constant, and the result "may even mimic a time-varying or
phantom-crossing EoS" in a non-interacting analysis [src: Sect. III.1].

### Step 2. Choose the realisation
<!-- key: step-2-choose-the-realisation -->

| Realisation | Definition | Extra parameters | Where read |
|---|---|---|---|
| Coupled fluid (CF), `Q ∝ rho_de` | `Q = beta H0 rho_de`, constant `w` | `w`, `beta` | arXiv:2601.07361, Eq. 6 |
| CF, other kernels in use | `Q = beta H rho_c`, `beta H rho_de` (Eq. 5) or `beta H0 rho_c`, `beta H0 rho_de` (Eq. 6) | 1–2 | arXiv:2606.21826, Sect. III.1 |
| Interacting vacuum | CF with `w = −1` fixed | `beta` | arXiv:2606.21826, Sect. III.1 |
| Coupled quintessence (CQ) | Lagrangian with dark-matter mass `m(phi) ∝ exp(−beta sqrt(kappa) phi)`, `kappa = 8 pi G`; `Q_μ = −beta rho_c sqrt(kappa) ∂_μ phi`, background `Q = beta rho_c sqrt(kappa) phi'/a` (Eqs. 4, 11–12); potential `U = U_0 (sqrt(kappa) phi)^{−alpha}` (Eq. 5) | `alpha`, `beta` | arXiv:2601.07361 |
| Running coupling | `Q(a) = 3 beta(a) H0 rho_0`, `rho_0 = rho_de0 + rho_c0`, `beta(a) = beta_0 a + beta_e (1 − a)` (Eq. 11) | `beta_0`, `beta_e` | arXiv:2606.21826, Sect. III.1 |
| Binned coupling | interacting vacuum with `beta(z)` in 20 bins and a Gaussian smoothness prior | 20, about 3 effective | Li and Zhang 2025, arXiv:2506.18477 [src: abstract] |
| Fluid, `Q = xi 𝓗 rho_DE`, `w ≃ −1` | `Q` enters the dark-matter equation with `+` sign (Eqs. 2–3), `xi < 0` means transfer from dark matter to dark energy; `w` not sampled | `xi` | Silva et al. 2025, arXiv:2503.23225, Sects. II.1, III; Giarè et al. 2024, arXiv:2404.15232, model section |
| Geodesic interacting vacuum, `Q ∝ H rho_dm` | `w = −1`, `rho_dm ∝ a^(−3+delta_0)`, hence `Q = −delta_0 H rho_dm` (Eq. 5) | `delta_0` | Pan et al. 2025, arXiv:2504.00994, Sect. II |
| Transfer potential in trace-free Einstein gravity | `w = −1`, energy-momentum transfer potential proportional to `rho_c` | `epsilon` | Zhai et al. 2025, arXiv:2503.15659 [src: abstract] |
| Coupled quintessence, Planck 2015 | `m(phi) = m_0 exp(−beta phi)`, `V = V_0 phi^(−alpha)`, `w ≈ −2/(alpha + 2)`, `G_eff = G(1 + 2 beta²)` for dark matter (Eqs. 54–57) | `alpha`, `beta` | Planck 2015 XIV, arXiv:1502.01590, Sect. 5.3.4 |
| Dark scattering (pure momentum exchange) | no energy transfer, background unchanged; friction `A(a) = [1 + w(a)] (H0²/H) 3 xi Omega_DE/(8 pi G)` in the Euler equation (Eqs. 5–6), `xi > 0` in bn/GeV, with CPL `w(a)` | `xi` (or `A_ds = (1 + w) xi`), `w0`, `wa` | Tsedrik and Bose 2025, arXiv:2512.17684, Sect. 2 |

The Planck 2015 coupled quintessence is the same Lagrangian model as the CQ
row above (exponential mass coupling, inverse-power-law potential): Planck
fixes `V_0` by an iterative routine valid for `alpha ≥ 0.03` (about
`w = −0.99`) and notes that `w` is "not an independent parameter", being
degenerate with the flatness of the potential [src: arXiv:1502.01590,
Sect. 5.3.4].

Why `H` or `H0` in the kernel: an energy-transfer rate needs an inverse
time; `H` keeps the background equations analytically tractable, while the
view that a local interaction should not know the global expansion rate
leads to `H0` as a fixed scale only. Both "remain phenomenological
parametrizations rather than unique consequences of an underlying
microscopic theory" [src: arXiv:2606.21826, Sect. III.1]. The CQ model is
the original coupled quintessence of Amendola 2000 (arXiv:astro-ph/9908023),
conformally equivalent to Brans–Dicke with a power-law potential, which then
gave `|beta| ≤ 0.1` [src: abstract]; Li et al. note the same equivalence,
via a Weyl rescaling, to modified-gravity models such as `f(R)` [src:
arXiv:2601.07361, main text].

### Step 3. Make the perturbations stable
<!-- key: step-3-make-the-perturbations-stable -->

- **The instability.** A constant-`w` dark-energy fluid with a simple
  coupling to dark matter has an early-time instability: the curvature
  perturbation "blows up on super-Hubble scales", even with adiabatic
  initial conditions and "regardless of how weak the coupling is"
  (Valiviita, Majerotto and Maartens 2008, arXiv:0804.0232) [src:
  abstract].
- **The doom factor.** Gavela et al. 2009 (arXiv:0901.1611) isolate the term
  that drives it, `d ≡ Q/[3𝓗 rho_de (1 + w)]` (Eq. 13); a positive `d`
  acts as anti-damping, and `d > 1` with a positive density coefficient
  gives runaway growth [src: Sect. 2.4]. For their `Q ∝ rho_de` model
  `d = xi/[3(1 + w)]` (Eq. 40); for `Q ∝ rho_dm`, `d = xi rho_dm/[3(1 + w)
  rho_de]` (Eq. 56), large at early times "even for tiny values of xi"
  because `rho_dm/rho_de` is large then [src: Sect. 4.2]. This is why
  `Q ∝ rho_de` kernels dominate the fluid literature.
- **The ePPF fix.** Li, Zhang and Zhang 2014 (arXiv:1404.5220) replace the
  dark-energy pressure-perturbation condition on large scales by a relation
  between the momentum density of dark energy and that of the other
  components, then match large- and small-scale evolution; the instability
  is removed for "all the interacting dark energy models" [src: abstract].
  IDECAMB (Li and Zhang 2023, arXiv:2306.01593) implements CQ and CF in CAMB
  through five free mapping functions, with a model-independent PPF
  treatment of CF [src: abstract]. In arXiv:2601.07361 the mapping is
  `δQ = C_1 δ_de + C_2 δ_c + C_3 θ_de`, `f_k = −Q θ + D_1 θ_de + D_2 θ_c`
  (Eqs. 2–3), with `C_1 = Q/(1 + w)`, `C_2 = D_1 = Q`,
  `C_3 = a^2 U_phi Q/(−phi')`, `D_2 = 0` for CQ, and `C_1 = D_2 = Q`,
  `C_2 = C_3 = D_1 = 0` for CF [src: main text]. CQ has a rest-frame dark
  energy sound speed of 1; CF needs none under ePPF [src: Sect. I].

What this buys and costs: ePPF lets the sampler explore the whole
`(w, beta)` plane, including regions a fluid treatment would exclude
(see "What goes wrong"). The Gavela et al. stability condition is a property
of the fluid model; with ePPF it no longer acts as a prior.

Other treatments in use, one line each:

- **Fluid with `w = −1 + epsilon` and a fixed flow direction.** Giarè et al.
  regularise the early-time super-horizon instability by `w = −1 + epsilon`,
  `epsilon ≃ 10⁻⁴`, and require `xi < 0` (dark matter to dark energy)
  [src: arXiv:2404.15232, model section, footnote 2]; Silva et al. implement
  the same kernel in CLASS with MontePython and a flat prior
  `xi ∈ [−1, 0]` (`[−1.5, 1.5]` for the sign-switching variant) [src:
  arXiv:2503.23225, Sect. III, Table 1]. These papers share Gavela's
  convention, in which `xi < 0` with `w > −1` gives `d = xi/[3(1 + w)] < 0`
  [der: Eq. 40 of arXiv:0901.1611], so here the stability condition does
  act as a prior.
- **Geodesic dark matter, unperturbed vacuum.** Pan et al. take
  `Q^μ ∥ u^μ_c` (energy exchange without momentum transfer), so dark matter
  stays geodesic, the vacuum is homogeneous (`delta_de = theta_de = 0`), and
  only the dark-matter continuity equation gains a term in `delta_0`
  (synchronous gauge, CDM frame, Eqs. 9–10); the prior on `delta_0` is
  two-sided, `[−1, 1]` [src: arXiv:2504.00994, Sect. II, Table 1].
- **Scalar field solved directly.** Planck 2015 integrates the Klein–Gordon
  equation with the dark-matter source term, `phi'' + 2𝓗 phi' + a² dV/dphi =
  a² beta rho_c` (Eq. 56), each component treated as a fluid [src:
  arXiv:1502.01590, Sect. 5.3.4].
- **Momentum exchange only.** In dark scattering the growing mode requires
  the friction to vanish early, `w0 + wa < −1/2`; linear growth agrees with a
  modified CLASS within 1–2% over the prior range, and non-linear scales use
  the halo-model reaction (ReACT) with a CosmoPower emulator
  [src: arXiv:2512.17684, Sect. 2].

### Step 4. Sample with the CMB computed consistently
<!-- key: step-4-sample-with-the-cmb-computed-consistently -->

Li et al. 2026 sample `H0` instead of `theta_*`, because the usual
Hu–Sugiyama fitting formula for `z_*` (their Eqs. 13–14) may be invalid
when the interaction modifies density scalings and recombination; `theta_*`
is derived from the visibility-function maximum (Eq. 15) [src:
arXiv:2601.07361, Sect. II]. Codes: IDECAMB with Cobaya [src: main text].

Priors (flat) [src: arXiv:2601.07361, Table 3]:

| Model | Parameter | Prior |
|---|---|---|
| CPL | `w0`; `wa` | [−3, 1]; [−3, 2] |
| CQ | `alpha`; `beta` | [0, 1.4]; [0, 0.15] |
| CF | `w`; `beta` | [−3, 1]; [−5, 1] |

The CQ priors are one-sided: `alpha > 0` is imposed "to ensure a physically
viable quintessence behavior" [src: main text], and `beta ≥ 0` by the prior
range. The ΛCDM limit (`alpha = beta = 0`) therefore sits on the corner of
the prior box.

Data in the 2026 baseline: Planck 2018 low-ℓ (Commander, SimAll), CamSpec
TT to ℓ < 1000 and TE/EE to ℓ < 600, ACT DR6 and SPT-3G "lite"
likelihoods, joint Planck + ACT + SPT lensing, DESI DR2 BAO, and one of
Pantheon+, DESY5 or DES-Dovekie [src: arXiv:2601.07361, Sect. II].

Peers: Silva et al. sample `100 theta_s` in CLASS, with Planck 2018 Plik
TT/TE/EE, low-ℓ SimAll, Planck lensing, DESI DR2 and one of Pantheon+,
Pantheon+ with SH0ES calibration, Union3 or DESY5 [src: arXiv:2503.23225,
Sect. III]; Pan et al. sample `100 theta_MC` with Planck 2018, DESI DR2,
cosmic chronometers and Pantheon+, Union3 or DESY5 [src: arXiv:2504.00994,
Table 1, abstract]; Tsedrik and Bose fit DES Y3 3×2pt with DESI DR2 BAO,
DESY5 and Planck [src: arXiv:2512.17684, abstract]. Silva et al. combine
only data sets not in tension with CMB + DESI DR2 for the sign-switching
model; DESY5 reaches 4.64σ there and is left out [src: arXiv:2503.23225,
Sect. IV.2].

### Step 5. Report coupling, fit and model comparison
<!-- key: step-5-report-coupling-fit-and-model-comparison -->

Marginalised constraints, a profile likelihood of `beta` (to separate
likelihood from prior-volume effects), and `Delta chi2_MAP` split into CMB,
BAO and SN pieces with `Delta DIC` against ΛCDM and CPL [src:
arXiv:2601.07361, main text, Table 2, Fig. 2]. With CMB + DESI + DES-Dovekie
the profile of `beta` has a well-defined minimum away from zero for both
models, approximately parabolic, "comparable" to the marginalised
significance [src: main text].

Peers report differently. Planck 2015 found the CQ coupling 2.5σ (TT) to
2.8σ (with polarisation) from zero for Planck + BSH, yet "the goodness of
fit does not improve"; it points to the `beta`–`alpha` degeneracy, under
which marginalising over `alpha` gives more weight to larger `beta`, as a
possible prior dependence [src: arXiv:1502.01590, Sect. 5.3.4]. Pan et al.
report `Delta chi2_min`, AIC and Bayesian evidence together: the first
mildly favours the interaction for most data sets, the others favour ΛCDM
[src: arXiv:2504.00994, abstract]. Silva et al. give `Delta chi2_min` and
`Delta AIC` per data combination [src: arXiv:2503.23225, Table 2].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Sign conventions
<!-- key: sign-conventions -->

| Paper | Equation for dark matter | Positive coupling means |
|---|---|---|
| Li et al. 2026; Li 2026 review | `rho_c' + 3𝓗 rho_c = −aQ` | transfer from dark matter to dark energy |
| Gavela et al. 2009 | `rho_dm' + 3𝓗 rho_dm = xi 𝓗 rho_de` (Eq. 29) | transfer from dark energy to dark matter |
| Silva et al. 2025; Giarè et al. 2024 | `rho_DM' + 3𝓗 rho_DM = Q`, `Q = xi 𝓗 rho_DE` (Eq. 2) | `xi > 0`: dark energy to dark matter (`xi < 0` imposed: the reverse) |
| Pan et al. 2025 | `rhȯ_dm + 3H rho_dm = −Q`, `Q = −delta_0 H rho_dm` (Eqs. 4–5) | `delta_0 > 0`: dark matter dilutes more slowly, `a^(−3+delta_0)` |
| Planck 2015 XIV | `rho_c' = −3𝓗 rho_c − beta rho_c phi'` (Eq. 55) | larger positive `beta`: more transfer from dark matter to dark energy |

So `beta > 0` in one paper and `xi > 0` in the other mean opposite
directions of flow. Gavela et al. give `w_de^eff = w + xi/3` (Eq. 32) and
note that phantom behaviour then requires `w < −1 − xi/3` [src: Sect.
3.1]. Before comparing a coupling value, a sign or a stability statement
across papers, rewrite both in one convention.

### Coupled fluid or coupled quintessence
<!-- key: coupled-fluid-or-coupled-quintessence -->

The two realisations fit the same data by opposite routes [src:
arXiv:2601.07361, main text]:

- **CQ.** `beta > 0` at more than 5σ in the marginalised constraint (with
  the prior `beta ≥ 0`); dark matter dilutes faster than in ΛCDM, dark
  energy is enhanced at `0.5 ≲ z ≲ 2`, and the background "partially
  mimics" CPL while the field's own equation of state stays quintessence-like
  at all redshifts. CQ needs no phantom crossing.
- **CF.** `beta < 0` and `w < −1`: energy flows from dark energy to dark
  matter, dark matter dilutes more slowly, and `Omega_m` is high today
  (0.613 ± 0.062 with the `f sigma8` data; arXiv:2601.07361, Supp.
  Sect. III.4), compensated in the distances by a strongly phantom `w`; growth is
  strongly suppressed (low `sigma8`, `S8`). The authors call this "an
  extreme corner of the IDE parameter space".
- **Stability, rewritten** [der: Li's CF has `+aQ` in the dark-energy
  equation, Gavela's `−xi 𝓗 rho_de`, so `xi 𝓗` corresponds to `−beta H0
  a`; the CF best fit `beta < 0`, `w < −1` then gives `xi > 0` and
  `d = xi/[3(1 + w)] < 0`]: the preferred CF corner lies on the side that
  the doom-factor criterion of arXiv:0901.1611 calls free of the early
  instability, in a model whose perturbations are in any case computed
  with ePPF. Gavela et al. themselves explored only `w > −1`, `xi < 0`
  [src: arXiv:0901.1611, Sect. 3.5].

### Constant, running or binned coupling
<!-- key: constant-running-or-binned-coupling -->

As summarised by the review [src: arXiv:2606.21826, Sect. III.1]: support
for a coupling depends on the kernel, being mainly associated with
`Q ∝ rho_de` (an interacting-vacuum `Q = beta H0 rho_de` reached about 3σ
with Planck, DESI DR1 and DESY5); a running coupling with DESI DR2, DESY5
and Planck changes sign from positive at early times to negative at late
times, reaching 4.1σ in one variant; letting `w` evolve as well "reduced"
the significance of excluding `w = −1` once interaction is included. The
binned interacting-vacuum reconstruction also changes sign, with about 2σ
from zero at high redshift and a supernova-dependent low-redshift
behaviour; CMB + DESI DR2 + DESY5 gives `Delta chi2_MAP = −17.76` and
`ln B = 5.98 ± 0.69`, with about three effective extra degrees of freedom
from a PCA [src: arXiv:2506.18477, abstract]. The primary papers behind the
first three statements were not read here.

Constant couplings with `w` fixed near −1, read in other groups' papers:

- Planck 2018 + DESI DR1, `Q = xi 𝓗 rho_DE`: `xi = −0.32 (+0.18/−0.14)`,
  `H0 = 70.8 (+1.4/−1.7)`; the model gives lower `Omega_m` and higher
  `sigma8`, "which may not be fully consistent" with large-scale-structure
  data [src: arXiv:2404.15232, abstract].
- Same kernel with DESI DR2: the significance falls; DR2 moves `Omega_m`
  up with about half the error, and since more negative `xi` means less
  dark matter, the higher `Omega_m` drives `xi` towards zero [src:
  arXiv:2503.23225, Sect. IV.1]. Adding Pantheon+, Union3 or DESY5 gives
  only lower bounds on `xi`, the tightest with DESY5 [src: same, Table 2].
- Geodesic interacting vacuum, `Q ∝ H rho_dm`: a preference "at slightly
  more than 1σ however still within 2σ", "no strong evidence" [src:
  arXiv:2504.00994, abstract].
- Trace-free Einstein gravity, `Q ∝ rho_c`: `epsilon ~ 10⁻⁴`; CMB and SN
  alone do not favour it, DESI 2024 BAO adds a 1σ preference for transfer
  from dark matter to dark energy, driven by the low-redshift BAO points
  that favour a lower `Omega_m` [src: arXiv:2503.15659, abstract].

The two pictures as the papers give them: with a free `w` and ePPF, Li et
al. find the CQ coupling away from zero with Pantheon+, DESY5 and
DES-Dovekie alike [src: arXiv:2601.07361, Table 1]; with `w ≃ −1` and the fixed sign,
Silva et al. find DESY5 pulls the coupling to its tightest bound near zero
[src: arXiv:2503.23225, Table 2]. The models differ (free or fixed `w`,
kernel, perturbation scheme, prior range); neither paper compares the two.

### Why IDE and w0wa cannot be separated by distances
<!-- key: why-ide-and-w0wa-cannot-be-separated-by -->

Gravity sees only the total energy-momentum tensor, so `Omega_m` "cannot
be measured" without assumptions on the dark sector and IDE "is always
equivalent to a family of non-interacting models" (Kunz 2007,
arXiv:astro-ph/0702615) [src: abstract]. Explicitly, a non-interacting
dark energy `w̄_x(a)` and an interacting vacuum give the same `H(z)` if
`ρ̃_c = ρ̄_c + ρ̄_x (1 + w̄_x)` and `ρ̃_x = −w̄_x ρ̄_x` (von Marttens et al.
2019, arXiv:1911.02618, Eqs. 29–30); the present-day density parameters
then differ between the two descriptions [src: Sect. 3.1]. In perturbations
the degeneracy holds only for specified dark-energy pressure perturbations
(sound speed) and anisotropic stress, so a choice of sound speed breaks it
[src: abstract]. With a luminal sound speed in both, constraints on
`Omega_m0` and `sigma8` are "considerably weakened" for interacting vacuum,
which "can change the significance of tensions" [src: abstract].
Gavela et al. give the background mapping for their model,
`w̃(z) ≃ w(1 + xi z)` at small `z` (Eq. 39), with a divergence of the
reconstructed `w̃` at `z ~ 1–10` for positive `xi` [src: Sect. 3.2].

Consequence for reading a result: a coupling "detected" from BAO + CMB +
SN is the same distance information as the `w0wa` preference, re-expressed;
it becomes a distinct claim only through perturbations (growth, lensing,
ISW), which is also the authors' own conclusion: future perturbation probes
are "essential for differentiating between these two scenarios" [src:
arXiv:2601.07361, Conclusion].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Data | Source | Place read |
|---|---|---|---|---|
| CQ `beta`; `alpha` | 0.0527 ± 0.0087; 0.46 ± 0.18 | CMB + DESI DR2 + DES-Dovekie | arXiv:2601.07361 | Table 1 |
| CQ `beta` (other SN) | 0.0517 (+0.0092/−0.0078) Pantheon+; 0.0561 (+0.0094/−0.0068) DESY5 | CMB + DESI DR2 + SN | arXiv:2601.07361 | Table 1 |
| CF `beta`; `w` | −2.59 (+0.76/−0.62); −1.52 (+0.16/−0.13) | CMB + DESI DR2 + DES-Dovekie | arXiv:2601.07361 | Table 1 |
| CF `beta`; `w`, no SN | −2.37 (+0.82/−0.93); −1.45 (+0.13/−0.15) | CMB + DESI DR2 | arXiv:2601.07361 | Table 1 |
| Total `Delta chi2_MAP` vs ΛCDM, DES-Dovekie | CPL −14.13; CQ −13.66; CF −15.64 | CMB + DESI DR2 + DES-Dovekie | arXiv:2601.07361 | Table 2 |
| `Delta DIC`, DES-Dovekie | CPL −12.22; CQ −11.31; CF −12.89 | same | arXiv:2601.07361 | Table 2 |
| Split of CF `Delta chi2_MAP` | CMB −6.82, BAO −3.59, SN −5.23 | same | arXiv:2601.07361 | Table 2 |
| CMB + DESI only | CPL −12.48 (`Delta DIC` −11.39); CQ −7.14 (−6.52); CF −12.91 (−8.08) | CMB + DESI DR2 | arXiv:2601.07361 | Table 2 |
| CF `Omega_m`, `sigma8`, `S8` with `f sigma8` | 0.613 ± 0.062; 0.480 (+0.026/−0.040); 0.682 (+0.011/−0.016) | CMB + DESI + DES-Dovekie + 20 `f sigma8` points | arXiv:2601.07361 | Supp. Sect. III.4 |
| `chi2` of the 20 `f sigma8` points | ΛCDM 9.03, CPL 9.02, CQ 9.55, CF 10.03 | same | arXiv:2601.07361 | Supp. Sect. III.4 |
| CF with `f sigma8`, overall | `Delta chi2 = −15.77`, `Delta DIC = −11.24` | same | arXiv:2601.07361 | Supp. Sect. III.4 |
| CQ `Omega_m`, `S8`, `H0` | 0.2986 ± 0.0051; 0.8253 ± 0.0095; 68.01 ± 0.54 | CMB without lensing + DESI + DES-Dovekie | arXiv:2601.07361 | Table 6 |
| Binned interacting vacuum | `Delta chi2_MAP = −17.76`, `ln B = 5.98 ± 0.69`, ≈ 3 effective d.o.f. | CMB + DESI DR2 + DESY5 | arXiv:2506.18477 | abstract |
| Coupled quintessence, early bound | `abs(beta) ≤ 0.1` | data of 1999 | arXiv:astro-ph/9908023 | abstract |
| Planck CQ `beta` | < 0.066 (95%) TT + lowP; 0.037 (+0.018/−0.015) + BSH; 0.036 (+0.016/−0.013) TT,TE,EE + lowP + BSH | Planck 2015 + BAO, SN, `H0` | arXiv:1502.01590 | Table 9 |
| Planck CQ `alpha`, `H0` | 0.29 (+0.077/−0.26); 67.47 (+0.88/−0.79) | Planck TT + lowP + BSH | arXiv:1502.01590 | Table 9 |
| Fluid `xi`, `w ≃ −1` | −0.32 (+0.18/−0.14), `H0 = 70.8 (+1.4/−1.7)` | Planck 2018 + DESI DR1 | arXiv:2404.15232 | abstract |
| Fluid `xi`, `w ≃ −1` | −0.132 (+0.087/−0.064), `Delta chi2_min = +1.1`, `Delta AIC = +3.1` | Planck 2018 + DESI DR2 | arXiv:2503.23225 | Table 2 |
| Same, with SN | `xi > −0.0538` (Pantheon+), `> −0.0220` (DESY5), `> −0.0630` (Union3); `Delta chi2_min` +1.38, +2.32, +0.5 | Planck 2018 + DESI DR2 + SN | arXiv:2503.23225 | Table 2 |
| Same, with SH0ES-calibrated Pantheon+ | −0.116 (+0.060/−0.050), `H0 = 69.61 ± 0.44`, `Delta chi2_min = −2.20` | Planck 2018 + DESI DR2 + PPS | arXiv:2503.23225 | Table 2, Sect. IV.1 |
| Geodesic vacuum `delta_0` | −0.00059 ± 0.00034 (CMB + DESI); −0.00044 (+0.00034/−0.00033) (+ DESY5); inner of the two printed intervals | Planck 2018 + DESI DR2 (+ SN) | arXiv:2504.00994 | results table, Sect. III |
| Dark scattering `A_ds`; `w0`, `wa` | 9.8 (+2.8/−9.5) bn/GeV; −0.79 (+0.05/−0.06), −0.56 (+0.24/−0.15) (CPL alone: −0.76 ± 0.06, −0.77 (+0.23/−0.20)) | DES Y3 3×2pt + DESI DR2 + DESY5 + Planck | arXiv:2512.17684 | abstract |
| FoM gain from DES Y3 on (`w0`, `wa`) | ~12% CPL, ~25% dark scattering | same vs DESI + SN + CMB | arXiv:2512.17684 | abstract |

Reading the table [der]: the IDE Δχ² values are close to the CPL ones with
the same number of extra parameters (two). The
"3–5σ" of the abstract refers to the departure of the marginalised
parameters from the non-interacting limit, not to a `Delta chi2`
conversion [src: arXiv:2601.07361, main text].

## What goes wrong
<!-- key: what-goes-wrong -->

- **Fluid instability mistaken for a constraint.** Without a stable
  perturbation scheme, constant-`w` fluids with `Q ∝ rho_c` blow up at early
  times for any coupling [src: arXiv:0804.0232, abstract]; an analysis that
  restricts the prior to the stable region imposes a theoretical prior that
  shapes the posterior. Test: state whether perturbations use ePPF (or an
  equivalent), and whether the prior was cut by the doom-factor sign.
  Examples of such cuts in use: `xi < 0` with `w = −1 + 10⁻⁴`
  [src: arXiv:2404.15232, footnote 2]; `xi ∈ [−1, 0]` [src:
  arXiv:2503.23225, Table 1].
- **Sign mixed between papers.** See "Sign conventions". Test: rewrite both
  continuity equations before comparing.
- **One-sided priors and corner limits.** In CQ, `beta ≥ 0` and `alpha > 0`
  put the ΛCDM limit at a prior corner [src: arXiv:2601.07361, Table 3];
  a marginalised "σ from zero" is then not a two-sided test. The profile
  likelihood of `beta` is the check the authors ran [src: Fig. 2]; report
  `Delta chi2` against ΛCDM as well.
- **Fitting formulae outside their model.** The Hu–Sugiyama `z_*` and any
  `theta_*` sampling assume standard density scalings [src:
  arXiv:2601.07361, Sect. II]. Test: derive `theta_*` from the visibility
  function.
- **An extreme corner preferred.** CF's `Omega_m ≈ 0.6` with `S8 ≈ 0.68`
  fits CMB + BAO + SN, and current `f sigma8` data do not exclude it, but
  CF fits those growth points worst of the four models [src:
  arXiv:2601.07361, Supp. Sect. III.4]. Test: weak lensing and full-shape
  clustering; the authors note that using them consistently needs IDE
  non-linear modelling, bias, baryons and intrinsic alignments, "which we
  leave for future work" [src: same].
- **ΛCDM-calibrated non-linear prescriptions.** N-body simulations of
  `Q = xi 𝓗 rho_x` (with the dark-matter Euler equation unchanged and an
  effective time-dependent particle mass) show scale-dependent departures
  that ΛCDM-calibrated prescriptions do not capture (Zhai et al. 2026,
  arXiv:2606.11368) [src: abstract]. Test: do not combine IDE with
  non-linear weak-lensing scales modelled by a ΛCDM halofit or HMcode.
  Tools that do model the non-linear regime: ReACT for dark scattering
  [src: arXiv:2512.17684, Sect. 2]; the Euclid preparation suite includes
  CiDER coupled-quintessence runs with c-GADGET (`beta` = 0.03, 0.05, 0.08,
  background fixed to ΛCDM, suppressed growth) [src: arXiv:2409.03523,
  Sect. 3.7].
- **A marginal peak without a better fit.** Planck 2015 found a 2.5–2.8σ
  CQ coupling with no improvement in overall χ² and suspects the
  `beta`–`alpha` degeneracy under marginalisation [src: arXiv:1502.01590,
  Sect. 5.3.4]; the same corner structure as the Li et al. priors above.
  Test: profile likelihood and `Delta chi2` beside the marginal interval.
- **Different statistics, different verdicts.** In one paper the same fits
  are mildly favoured by `Delta chi2_min` and disfavoured by AIC and the
  Bayesian evidence [src: arXiv:2504.00994, abstract]. Test: report all
  three with the number of added parameters.
- **Background degeneracy read as detection.** Kunz's argument and the
  explicit mapping of arXiv:1911.02618 (above) mean that a coupling and a
  `w(z)` are two names for the same `H(z)`. Evidence that a coupling rather
  than an evolving `w` is present has to come from perturbations [src:
  arXiv:astro-ph/0702615; arXiv:2601.07361, Conclusion].
- **Robustness to the supernova recalibration, read both ways.** The IDE
  authors stress that the coupling "persists under the DES-Dovekie
  recalibration, which significantly weakens the evidence for dynamical DE"
  [src: arXiv:2601.07361, abstract]. In their own Table 2, CPL with
  DES-Dovekie still has total Δχ² = −14.13, within 0.5 and 1.5 of CQ and CF
  [src: Table 2]: the data mismatch that both models absorb is still there,
  and neither model absorbs it much better.
- **Supernova-sample dependence.** In the binned reconstruction the
  low-redshift sign of `beta(z)` depends on the supernova sample [src:
  arXiv:2506.18477, abstract], as the `w0wa` preference does in L2.

## Reading list
<!-- key: reading-list -->

- Foundation: Amendola 2000, arXiv:astro-ph/9908023 — coupled quintessence.
- Foundation/critique: Kunz 2007, arXiv:astro-ph/0702615 — the dark
  degeneracy; why `Omega_m` and the coupling are not separately measurable.
- Method: Valiviita et al. 2008, arXiv:0804.0232 — the large-scale
  instability of coupled fluids.
- Method: Gavela et al. 2009, arXiv:0901.1611 — the doom factor (Eq. 13),
  `Q ∝ rho_de` versus `Q ∝ rho_dm`, background mapping to `w̃(z)` (Eq. 38).
- Method: Li, Zhang and Zhang 2014, arXiv:1404.5220 — ePPF.
- Code: Li and Zhang 2023, arXiv:2306.01593 — IDECAMB.
- Method: von Marttens et al. 2019, arXiv:1911.02618 — explicit IDE ↔
  dynamical-DE mapping (Eqs. 27–30).
- Review: Li 2026, arXiv:2606.21826, Sect. III — IDE results after DESI.
- Application: Li et al. 2026, arXiv:2601.07361 — CQ and CF with DESI DR2,
  three CMB experiments and DES-Dovekie; priors, fit split, growth test.
- Application: Li and Zhang 2025, arXiv:2506.18477 — binned
  interacting-vacuum coupling.
- Critique: Zhai et al. 2026, arXiv:2606.11368 — non-linear structure in
  IDE is not captured by ΛCDM-calibrated prescriptions.
- Collaboration: Planck 2015 XIV, arXiv:1502.01590, Sect. 5.3.4 — coupled
  quintessence with Planck, BAO, SN, `H0`, WL and RSD; prior-dependence caveat.
- Collaboration (simulations): Euclid preparation LXIII, arXiv:2409.03523 —
  CiDER coupled-quintessence N-body runs.
- Application (fluid, `w ≃ −1`): Giarè et al. 2024, arXiv:2404.15232
  (DESI DR1); Silva et al. 2025, arXiv:2503.23225 (DESI DR2, CLASS).
- Application (geodesic vacuum, `Q ∝ H rho_dm`): Pan et al. 2025,
  arXiv:2504.00994 — `Delta chi2`, AIC and evidence side by side.
- Application (trace-free gravity, `Q ∝ rho_c`): Zhai et al. 2025,
  arXiv:2503.15659.
- Application (momentum exchange): Tsedrik and Bose 2025, arXiv:2512.17684
  — dark scattering with DES Y3 3×2pt, ReACT.

## Not verified
<!-- key: not-verified -->

- The primary papers for the DESI DR1 interacting-vacuum comparison, the
  running-coupling 4.1σ result, the CPL + interaction DR2 analysis and the
  sign-switching models: read only as summarised in arXiv:2606.21826,
  Sect. III.1; no identifiers recorded.
- Supplementary parts of arXiv:2601.07361 on the per-redshift BAO and SN
  residuals (Sect. III.2) and the full Table 6 rows for CF beyond `Omega_m`.
- The review of Wang et al. on dark-sector interactions (cited as [63] in
  arXiv:2601.07361): not read.
- Collaboration IDE analyses: Planck 2015 (above) is the one read. No DESI,
  DES, ACT or SPT collaboration fit of an IDE model was found in the
  searches of 2026-10-17 and 2026-10-22; Euclid has simulations only.
- The tables of arXiv:2504.00994 and arXiv:2503.23225 were read without
  their captions' confidence-level conventions beyond what is stated above;
  the value of `w` used by Silva et al. is not stated in the sections read.
