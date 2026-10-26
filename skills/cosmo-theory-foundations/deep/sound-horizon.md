# Sound horizon r_s, r_d, z_*, z_d, θ_* and θ_MC — cosmo-theory-foundations dossier

Scope: how the two decoupling epochs are defined in the papers and codes
that compute them (and why 1020 and 1060 are both quoted for z_d), what
accuracy the authors of each sound-horizon formula state and over which
range, which assumptions (neutrino splitting, helium, recombination code,
decoupling definition) move r_d, and how an analysis calibrates r_d or stays
agnostic to it.
Snapshot: 2026-10-18.
From: Planck 2013 parameter definitions (arXiv:1303.5076, Sect. 2); DESI DR2
BAO (arXiv:2503.14738, Sect. 1); eBOSS cosmology (arXiv:2007.08991, Sect. 2).

Already in L2, not repeated here: the r_s integral, R ≡ 3ρ_b/(4ρ_γ), Planck's
definitions of z_*, z_drag and θ_* (Eqs. 5–7), the Eisenstein–Hu formulae
(arXiv:astro-ph/9709112, Eqs. 2–7, 26), the calibrated fits of Aubourg et al.
(arXiv:1411.1074, Eqs. 16–17) with their stated accuracies, DESI's power law
(arXiv:2503.14738, Eq. 2) and its genealogy, the 1.0275 factor of Planck 2013
(arXiv:1303.5076, Sect. 5.2) (`physics-and-methods.md#sound-horizon-rs-rd-z-zd-and-fitting-formulae`,
`results.md#sound-horizon-fitting-formulae`,
`systematics.md#rd-definition-and-code-dependence`). The BAO fit that uses
r_d is in `cosmo-galaxy-clustering/deep/bao-reconstruction-fitting.md`; the
CMB–BAO comparison in the (Ω_m, h r_d) plane in
`cosmo-tensions-anomalies/deep/cmb-bao-mismatch.md`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Fix what "decoupling" means
<!-- key: step-1-fix-what-decoupling-means -->

Two optical depths define the two epochs, and each code chooses a criterion
on them.

- Photons: Planck defines z_* by τ(η_*) = 1, with τ(η) ≡ ∫_η^η0 τ̇ dη' the
  Thomson optical depth [src: arXiv:1303.5076, Eq. 5; L2].
- Baryons: the baryon Euler equation has the formal solution
  a V_b = ∫_0^η dη' a [τ̇_d Θ_1 + kΨ] e^(−τ_d) [src: Hu & Sugiyama 1996,
  arXiv:astro-ph/9510117, App. C.2, LaTeX source; equation unnumbered in the source read], with
  τ̇_d = τ̇/R; "Drag depth unity τ_d(z_d) = 1 marks the transition between
  the drag and infall epochs", and "for Ω_b h² ≳ 0.03, the drag epoch
  precedes last scattering z_d > z_*" [src: App. C.2]. Θ_1 is the photon
  dipole, Ψ the Newtonian potential, V_b the baryon velocity. Planck Eq. 7
  is the same criterion. Hu & Sugiyama note that an earlier paper of theirs
  defined z_d instead as the epoch when the perturbation joined the growing
  mode, which lowers the redshift "by a factor of 3/5" [src: App. C.2,
  footnote]: the name z_d has carried more than one definition.
- CLASS, as described by users of it: "we define z_* as the redshift at the
  maximum of the photon visibility function, g'(z_*) = 0, and z_d as the
  redshift at which the baryon optical depth κ_b(z) crosses one", with
  κ_b = κ/R [src: Sharma & Lesgourgues 2025, arXiv:2510.15835, Sect. III.2,
  footnote 3]. The z_d criterion is the Planck/CAMB one; the z_* criterion
  (visibility peak) is not Planck's τ = 1.

### Step 2. Compute z_d, then r_d, with a Boltzmann code
<!-- key: step-2-compute-zd-then-rd-with-a-boltzmann-code -->

The value in every current BAO analysis comes from a Boltzmann code. DESI
DR2: "Theory models are computed using interfaces to CAMB", with Cobaya
sampling [src: arXiv:2503.14738, Sect. V]; its power-law Eq. 2 is a
statement of scaling, not what the chains use. Values to check a pipeline
against:

| Quantity | Value | Source |
|---|---|---|
| z_drag, Planck 2018 TT,TE,EE+lowE+lensing | 1059.94 ± 0.30 | arXiv:1807.06209, Table 2 [src] |
| z_drag, Planck 2018 TT+lowE | 1059.39 ± 0.46 | arXiv:1807.06209, Table 2 [src] |
| z_*, Planck 2018 TT,TE,EE+lowE+lensing | 1089.92 ± 0.25 | arXiv:1807.06209, Table 2 [src] |
| r_*, same | 144.43 ± 0.26 Mpc | arXiv:1807.06209, Table 2 [src] |
| r_drag, same | 147.09 ± 0.26 Mpc | arXiv:1807.06209, Table 2 [src] |
| r_s/r_d with CLASS, ΛCDM fit to Planck 2018 + DESI DR2 + Pantheon+ | 0.98283 (+0.00025/−0.00027) | arXiv:2510.15835, Sect. III.2 [src] |
| r_s/r_d with CLASS, EDE fit to the same data | 0.98334 (+0.00042/−0.00051) | arXiv:2510.15835, Sect. III.2 [src] |

Sharma & Lesgourgues take z_* at the peak of the visibility function
(Step 1), Planck at τ = 1, so their CLASS ratio and a ratio formed from the
Planck table are not the same quantity [der]. The size of that difference
was not read in a paper.

### Step 3. Read 1020 and 1060 as two definitions, not two cosmologies
<!-- key: step-3-read-1020-and-1060-as-two-definitions -->

The fitting formulae for the epochs are those of Hu & Sugiyama 1996,
App. E, "designed to be valid at the percent level" for
0.0025 ≲ Ω_b h² ≲ 0.25 and 0.025 ≲ Ω_0 h² ≲ 0.64, with T_0 = 2.726 K and
Y_p ≈ 0.23 fixed [src: arXiv:astro-ph/9510117, App. E]:

z_* = 1048 [1 + 0.00124 (Ω_b h²)^(−0.738)] [1 + g_1 (Ω_0 h²)^(g_2)],
g_1 = 0.0783 (Ω_b h²)^(−0.238) [1 + 39.5 (Ω_b h²)^(0.763)]^(−1),
g_2 = 0.560 [1 + 21.1 (Ω_b h²)^(1.81)]^(−1)  [src: arXiv:astro-ph/9510117, App. E, first equation, E1 by order];

z_d = 1345 (Ω_0 h²)^(0.251) / [1 + 0.659 (Ω_0 h²)^(0.828)] × [1 + b_1 (Ω_b h²)^(b_2)],
b_1 = 0.313 (Ω_0 h²)^(−0.419) [1 + 0.607 (Ω_0 h²)^(0.674)],
b_2 = 0.238 (Ω_0 h²)^(0.223)  [src: arXiv:astro-ph/9510117, App. E; Eisenstein & Hu 1998 cite it as "Eqn. … E2", Sect. 2.1],

Ω_0 h² being the total matter density. Eisenstein & Hu 1998 copy Eq. E2 of Hu & Sugiyama 1996
(arXiv:astro-ph/9510117) with 1291 in place of 1345: "we have reduced z_d by a factor of 0.96 from HS (96)
on phenomenological grounds" [src: arXiv:astro-ph/9709112, Sect. 2.1].

eBOSS writes that the drag epoch is "around a redshift z = 1020" without
naming its source [src: arXiv:2007.08991, Sect. II.3.1]; DESI DR2 writes
z_d ≈ 1060 [src: arXiv:2503.14738, Sect. I], and Planck 2018 gives
z_drag = 1059.94 ± 0.30 [src: arXiv:1807.06209, Table 2], the τ_d = 1 epoch.

The Eisenstein–Hu z_d is a fitting device, rescaled from the Hu–Sugiyama fit
on phenomenological grounds so that their transfer-function fit works, not
the redshift at which τ_d = 1. That the eBOSS value is the Eisenstein–Hu one
is an inference from the sources above, not a statement of eBOSS; no paper
evaluating the two fits at Planck densities was read [der].

### Step 4. Get θ_* and know what θ_MC is
<!-- key: step-4-get-theta-and-know-what-thetamc-is -->

θ_MC is "an approximation to θ_* that is used in CosmoMC and is based on
fitting formulae given in Hu & Sugiyama (1996)" (L2). The z_* fit is
Eq. E1 above. DESI samples 100θ_MC because it "helps approximate the
degeneracy direction of the CMB parameter space while being faster to
calculate the conversion to H0 and Ω_m"; "any difference between the values
of θ_MC and θ_* only slightly affects the efficiency of the sampling while
having no effect on the accuracy of the likelihood evaluation" [src:
arXiv:2503.14738, Sect. V, footnote 17].

| Quantity | Value | Source |
|---|---|---|
| 100θ_MC, Planck 2018 TT,TE,EE+lowE+lensing | 1.04092 ± 0.00031 | arXiv:1807.06209, Table 2 [src] |
| 100θ_*, same | 1.04110 ± 0.00031 | arXiv:1807.06209, Table 2 [src] |

The two are different parameters with different posteriors: a prior written
on θ_* must be applied to θ_* [der]. How their difference varies across a
prior box was not read in a paper.

What the CMB actually fixes in r_d, from Planck 2018 [src: arXiv:1807.06209,
Sect. 3.1, Eqs. 8–9, TT,TE,EE+lowE, ΛCDM]: "a tight 0.04%-precision relation"
(r_drag h/Mpc)(Ω_m/0.3)^0.4 = 101.056 ± 0.036, and, because r_drag "depends
primarily on the matter, baryon, and radiation densities", a 0.05% constraint
Ω_m^0.3 h (Ω_b h²)^(−0.16) = 0.87498 ± 0.00052.

### Step 5. Calibrate r_d, or do not
<!-- key: step-5-calibrate-rd-or-do-not -->

| Route | What enters | Where used |
|---|---|---|
| Full CMB likelihood | r_d computed by the Boltzmann code at each sample | DESI DR2 with CMB [src: arXiv:2503.14738, Sect. V] |
| Compressed early-Universe prior | Gaussian on (θ_*, ω_b, ω_bc) = (0.01041, 0.02223, 0.14208) with covariance 10⁻⁹ × [[0.006621, 0.12444, −1.1929], [0.12444, 21.344, −94.001], [−1.1929, −94.001, 1488.4]] | DESI DR2 [src: arXiv:2503.14738, Eqs. 35–36, App. A] |
| BBN prior on ω_b | r_d from ω_b and the BAO-fitted Ω_m h² | DESI DR2 (L2) |
| Uncalibrated, Method I | ratios that cancel r_s and r_d | arXiv:2510.15835, Eqs. 10–14 [src] |
| Uncalibrated, Method II | r_s free (flat prior), r_d = r_s/(r_s/r_d)_CLASS | arXiv:2510.15835, Sect. III.2 [src] |

DESI states that the compressed prior gives w0wa posteriors "remarkably
similar" to the full CMB, "indicating that most of the information added by
the CMB in this scenario comes from the anchoring constraint it provides on
Ω_m" [src: App. A].

Method I of Sharma & Lesgourgues (arXiv:2510.15835) defines
R_M(z_i) ≡ 100 (r_s/r_d) D_M(z_i)/D_M(z_*) [src: Eq. 10] and
R_H(z_i) ≡ D_M(z_i)/D_H(z_i) [src: Eq. 11], fitted to
100θ_s/θ_s(z_i) and Δz(z_i)/θ_s(z_i) [src: Eq. 12], with θ_s(z_i) the BAO
angle and Δz(z_i) the radial BAO interval in redshift; for an isotropic
point R_V ≡ 100 (r_s/r_d) D_V(z_i)/D_M(z_*) [src: Eq. 13]. The residual
dependence is on r_s/r_d only, "very close to 0.983" even in extended models:
models that shift the whole recombination history (primordial magnetic
fields, varying constants) "change both z_* and z_d in such a way that r_s/r_d
is not significantly affected", and EDE-type models "do not affect z_* and
z_d, but shift both r_s and r_d" [src: Sect. III.2]. Only models in which
"photons or baryons experience non-standard interactions or non-thermal
distortions that shift their respective decoupling times by a different
amount" break this [src: same]. The two methods "are expected to be
equivalent up to prior volume effects", and gave "nearly identical results"
[src: Sect. III.2, App. A].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Boltzmann value or a formula
<!-- key: boltzmann-value-or-a-formula -->

The accuracies the authors state, each against their own numerical
reference:

| Formula | Stated accuracy | Range | Source | Place read |
|---|---|---|---|---|
| Aubourg et al. Eq. 16 | "accurate to 0.021%" | N_eff = 3.046, Σm_ν < 0.6 eV, ω_b and ω_cb within 3σ of Planck | arXiv:1411.1074 | Sect. II.2 |
| Aubourg et al. Eq. 17 (free N_eff) | "accurate to 0.119%" | 0 < Σm_ν < 0.6 eV, 3 < N_eff < 5 | arXiv:1411.1074 | Sect. II.2 |
| Eisenstein–Hu Eq. 26 (short form) | "∼2%" on the sound horizon | Ω_b h² ≳ 0.0125, 0.025 ≲ Ω_0 h² ≲ 0.5 | arXiv:astro-ph/9709112 | Sect. 4.1 |
| Eisenstein–Hu Eq. 6 with its own z_d | CosmoMC multiplied the numerical r_s(z_drag) by 1.0275 "to match the Eisenstein-Hu approximation in the fiducial model" | Planck 2013 fiducial model | arXiv:1303.5076 | Sect. 5.2 |
| DESI DR2 Eq. 2 (power law) | none stated; with CMB ω_b and ω_bc it gives "a 0.2% determination of r_d", a precision | N_eff = 3.04 | arXiv:2503.14738 | Sect. I |

Aubourg et al. add that "increasing N_eff by unity decreases r_d by about
3.2%" [src: arXiv:1411.1074, Sect. II.2]. DESI DR2 BAO alone give
h r_d = (101.54 ± 0.73) Mpc [src: arXiv:2503.14738, Eq. 17].

What this buys: a formula with a stated accuracy well below the BAO error on
h r_d serves for illustration inside its stated range; a formula with no
stated accuracy, or one used outside its range, is no substitute for the
Boltzmann value in an extended model [der].

### One massive state or three degenerate
<!-- key: one-massive-state-or-three-degenerate -->

Aubourg et al.: "a 0.5 (1.0) eV neutrino mass changes r_d by −0.26%
(−0.92%) for fixed ω_cb" [src: arXiv:1411.1074, Sect. II.2]. DESI DR2 varies
Σm_ν with "three degenerate mass eigenstates" [src: arXiv:2503.14738,
Sect. V].

The passage of Aubourg et al. read does not say how the neutrino mass is
split among states in the calibration of Eq. 16; a re-analysis that uses it
with degenerate masses should check it against the Boltzmann code with the
neutrino setting of the chain [der].

### Recombination physics and helium
<!-- key: recombination-physics-and-helium -->

Planck 2018: the atomic-physics and radiative-transfer effects omitted by
earlier recombination calculations "can lead to significant biases to
several cosmological parameters", but "at the present level of precision
these can be reliably incorporated within the advanced recombination codes
CosmoRec … and HyRec …, as well as the recfast code …, modified using
corrections calculated with the more precise codes" [src: arXiv:1807.06209,
Sect. 7.7]. No r_d difference between these codes was read. No paper giving
the response of r_d to the helium fraction Y_He was read; codes that fix
Y_He instead of taking it from BBN differ by that response.

### Which z_* definition
<!-- key: which-z-definition -->

τ = 1 (Planck, CAMB) or visibility peak (CLASS as described in
arXiv:2510.15835). The r_* difference this implies was not read in a
paper.

### Calibrated or agnostic
<!-- key: calibrated-or-agnostic -->

A calibrated r_d inherits "standard pre-recombination physics" (L2). The
agnostic methods replace it by a free scale; the cost is the residual
assumption r_s/r_d ≈ 0.983, whose uncertainty in ΛCDM and EDE fits is
"at least two orders of magnitude smaller" (ΛCDM) or "at least 30 times
smaller" (EDE) than the current errors on the ratios [src: arXiv:2510.15835,
Sect. III.2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| z_drag | 1059.94 ± 0.30 | Planck 2018 TT,TE,EE+lowE+lensing | arXiv:1807.06209 | Table 2 |
| r_drag h (Ω_m/0.3)^0.4 | 101.056 ± 0.036 Mpc | Planck 2018 TT,TE,EE+lowE | arXiv:1807.06209 | Eq. 8 |
| Ω_m^0.3 h (Ω_b h²)^(−0.16) | 0.87498 ± 0.00052 | same | arXiv:1807.06209 | Eq. 9 |
| HS96 z_d coefficient; EH98 | 1345; 1291 (× 0.96) | — | arXiv:astro-ph/9510117; arXiv:astro-ph/9709112 | Eq. E2; Sect. 2.1 |
| HS96 fit validity | percent level, 0.0025 ≲ ω_b ≲ 0.25, 0.025 ≲ ω_m ≲ 0.64 | — | arXiv:astro-ph/9510117 | App. E |
| r_s/r_d (CLASS) | 0.98283; 0.98334 in EDE | Planck 2018 + DESI DR2 + Pantheon+ | arXiv:2510.15835 | Sect. III.2 |
| z_*; r_*; r_drag | 1089.92 ± 0.25; 144.43 ± 0.26 Mpc; 147.09 ± 0.26 Mpc | Planck 2018 TT,TE,EE+lowE+lensing | arXiv:1807.06209 | Table 2 |
| 100θ_MC; 100θ_* | 1.04092 ± 0.00031; 1.04110 ± 0.00031 | same | arXiv:1807.06209 | Table 2 |
| Aubourg Eq. 16; Eq. 17 | accurate to 0.021%; to 0.119% | ranges in the text | arXiv:1411.1074 | Sect. II.2 |
| r_d response | −0.26% (0.5 eV), −0.92% (1.0 eV) at fixed ω_cb; about −3.2% per unit N_eff | — | arXiv:1411.1074 | Sect. II.2 |
| Eisenstein–Hu Eq. 26 | ∼2% | Ω_b h² ≳ 0.0125, 0.025 ≲ Ω_0 h² ≲ 0.5 | arXiv:astro-ph/9709112 | Sect. 4.1 |
| Compressed CMB prior means | θ_* = 0.01041, ω_b = 0.02223, ω_bc = 0.14208 | CamSpec-based | arXiv:2503.14738 | Eq. 35 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Eisenstein–Hu z_d quoted as the drag redshift.** Shows up as z_d ≈ 1020
  (arXiv:2007.08991, Sect. II.3.1) next to a Boltzmann r_d. Test: recompute
  with τ_d = 1; the Planck value is 1059.94 (arXiv:1807.06209, Table 2).
- **A fitting formula used outside its stated range.** DESI Eq. 2 states no
  accuracy; Aubourg Eq. 16 states its accuracy only for N_eff = 3.046,
  Σm_ν < 0.6 eV and ω_b, ω_cb within 3σ of Planck (arXiv:1411.1074,
  Sect. II.2). Test: compare with the Boltzmann r_drag at the best fit and at
  the prior edges.
- **Aubourg Eq. 16 with degenerate neutrinos.** The neutrino splitting of its
  calibration is not stated in the passage read. Test: compute r_drag with the
  neutrino setting of the chain.
- **θ_MC treated as θ_*.** Planck 2018 gives 100θ_MC = 1.04092 ± 0.00031 and
  100θ_* = 1.04110 ± 0.00031 (arXiv:1807.06209, Table 2). Test: report which
  one the prior is on; DESI uses θ_* in its compressed prior
  (arXiv:2503.14738, Eq. 35).
- **r_*/r_d assumed universal across codes.** The CLASS-based ratio
  (arXiv:2510.15835, Sect. III.2) uses the visibility-peak z_*, Planck the
  τ = 1 one. Test: take the ratio from the code and the definition of the
  analysis.
- **Calibration hidden in a "model-independent" H0.** BAO + BBN or BAO + θ_*
  inherit the pre-recombination assumption; Method I or II of
  arXiv:2510.15835 removes it at the cost of the r_s/r_d assumption.

## Reading list
<!-- key: reading-list -->

- Hu & Sugiyama 1996, arXiv:astro-ph/9510117 (foundation): App. C.2 for the
  drag optical depth and its τ_d = 1 definition; App. E for the z_* and z_d
  fits behind θ_MC and Eisenstein–Hu.
- Eisenstein & Hu 1998, arXiv:astro-ph/9709112 (foundation): Sect. 2.1 for the
  0.96 rescaling of z_d and the analytic s.
- Planck Collaboration 2018, arXiv:1807.06209 (results): Table 2 for z_drag,
  r_drag, r_*; Eqs. 8–9 for what the CMB fixes; Sect. 7.7 on recombination
  codes.
- Aubourg et al. 2015, arXiv:1411.1074 (method): Sect. II.2, the calibrated
  fits and their neutrino and N_eff responses.
- DESI Collaboration 2025, arXiv:2503.14738 (results): Sect. V for the code
  and neutrino settings, footnote 17 on θ_MC, App. A for the compressed prior.
- Sharma & Lesgourgues 2025, arXiv:2510.15835 (method): Sect. III.2 for
  CLASS's epoch definitions, r_s/r_d and the two uncalibrated likelihoods.
- eBOSS Collaboration 2021, arXiv:2007.08991 (results): Sect. II.3.1, where
  the 1020 is written.

## Not verified
<!-- key: not-verified -->

- The r_d and r_* given by CLASS and by CAMB for the same input, and the size
  of the τ = 1 against visibility-peak z_* difference: not read in a paper.
- Differences in r_d between CosmoRec, HyRec and Recfast: Planck 2018 says
  they agree "at the present level of precision" but gives no r_d number.
- The accuracy of DESI DR2 Eq. 2 against a Boltzmann code, and the neutrino
  splitting behind the calibration of Aubourg Eq. 16: not stated in the
  passages read.
- The response of r_d to Y_He: not read in a paper. The CAMB accuracy tables
  that stood here before 2026-10-23 were agent computations and are set aside
  in `docs/history/set-aside/2026-10-23/cosmo-theory-foundations-sound-horizon.md`.
- The CosmoMC/CAMB implementation of θ_MC was not read in source (the
  compiled routine is not shipped as text); the Hu–Sugiyama attribution is
  Planck's and DESI's.
- r_d in models with non-standard recombination (varying m_e, EDE) beyond the
  r_s/r_d statement of arXiv:2510.15835.
