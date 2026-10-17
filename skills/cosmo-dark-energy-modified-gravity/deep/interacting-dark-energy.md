# Interacting dark energy — cosmo-dark-energy-modified-gravity dossier

Scope: how an interacting-dark-energy (IDE) fit is set up (coupling form,
sign convention, perturbation treatment, code, priors, data), why the
same background data that prefer `w0wa` also prefer a coupling, and what
separates the two descriptions; for a reader about to run or referee an
IDE analysis.
Snapshot: 2026-10-17.
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

### Step 5. Report coupling, fit and model comparison
<!-- key: step-5-report-coupling-fit-and-model-comparison -->

Marginalised constraints, a profile likelihood of `beta` (to separate
likelihood from prior-volume effects), and `Delta chi2_MAP` split into CMB,
BAO and SN pieces with `Delta DIC` against ΛCDM and CPL [src:
arXiv:2601.07361, main text, Table 2, Fig. 2]. With CMB + DESI + DES-Dovekie
the profile of `beta` has a well-defined minimum away from zero for both
models, approximately parabolic, "comparable" to the marginalised
significance [src: main text].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Sign conventions
<!-- key: sign-conventions -->

| Paper | Equation for dark matter | Positive coupling means |
|---|---|---|
| Li et al. 2026; Li 2026 review | `rho_c' + 3𝓗 rho_c = −aQ` | transfer from dark matter to dark energy |
| Gavela et al. 2009 | `rho_dm' + 3𝓗 rho_dm = xi 𝓗 rho_de` (Eq. 29) | transfer from dark energy to dark matter |

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
  matter, dark matter dilutes more slowly, and `Omega_m` reaches about 0.6
  today, compensated in the distances by a strongly phantom `w`; growth is
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

Reading the table: the IDE Δχ² values sit within about 2 of CPL with the
same number of extra parameters (two); the extra fit of CF over CPL is 1.5
in total χ² for DES-Dovekie [der: −15.64 − (−14.13), Table 2]. The
"3–5σ" of the abstract refers to the departure of the marginalised
parameters from the non-interacting limit, not to a `Delta chi2`
conversion [src: arXiv:2601.07361, main text]; converted with two degrees
of freedom as DESI does, a total Δχ² of −13.7 to −15.6 is a 3.3–3.6σ
preference [der: Wilks with 2 d.o.f.; L2 conversion convention in
`physics-and-methods.md#model-comparison-practice`], close to the CPL value
for the same data.

## What goes wrong
<!-- key: what-goes-wrong -->

- **Fluid instability mistaken for a constraint.** Without a stable
  perturbation scheme, constant-`w` fluids with `Q ∝ rho_c` blow up at early
  times for any coupling [src: arXiv:0804.0232, abstract]; an analysis that
  restricts the prior to the stable region imposes a theoretical prior that
  shapes the posterior. Test: state whether perturbations use ePPF (or an
  equivalent), and whether the prior was cut by the doom-factor sign.
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
- Whether any collaboration (DESI, DES, ACT, SPT) has published an IDE
  analysis: none was found in the searches made for this dossier.
