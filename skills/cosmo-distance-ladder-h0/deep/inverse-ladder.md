# Inverse distance ladder and sound-horizon-free H0 — cosmo-distance-ladder-h0 dossier

Scope: how an inverse-ladder H0 is assembled (BAO set, r_d prior, SN
sample, free M_B, expansion model, likelihood, sampler), how the choice of
expansion model, r_d calibration, BAO subset and SN compilation moves H0 and
M_B, how BAO + BBN and the sound-horizon-free variants (equality scale,
free r_d with CMB lensing, chronometer-calibrated r_d) are set up, and the
tests that show what the result does and does not depend on.
Snapshot: 2026-10-19.
From: Verde et al. 2023, Sect. 3; Chen & Wang 2026, Sect. 1.

Already in L2: the definition, the history (Heavens 2014, Cuesta 2015,
Bernal 2016) and the DESI r_d fitting formula in
`physics-and-methods.md#early-universe-and-inverse-ladder-inference`; the
headline values in `results.md#early-universe-and-inverse-ladder-values`;
the SN-systematic test in
`open-questions.md#theory-status-summary-details-in-sibling-skills`. The
BBN omega_b prior itself (abundances, codes, rates) is in `cosmo-bbn`
(`deep/baryon-density.md`); sound-horizon definitions and formula accuracy
in `cosmo-theory-foundations` (`deep/sound-horizon.md`); why the ladder
enters a model test as an M_B prior in `cosmo-tensions-anomalies`
(`deep/theoretical-resolutions.md`).

Notation. r_d: comoving sound horizon at the baryon-drag epoch; D_M, D_H =
c/H, D_V = [z D_M^2 D_H]^(1/3): transverse, line-of-sight and
volume-averaged BAO distances, measured in units of r_d; M_B (M_0 in some
papers): SN Ia absolute magnitude; q0, j0, s0, l0: deceleration, jerk,
snap and lerk today; omega_b = Omega_b h^2, omega_bc = (Omega_b + Omega_c)
h^2; k_eq: matter–radiation equality wavenumber.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Write the expansion history without a dark-energy model
<!-- key: step-1-write-the-expansion-history-without-a -->

Two families are in use.

**Cosmography.** H(z) as a Taylor series in z to fifth order,
H = H0 [1 + H1 z + H2 z^2 + H3 z^3 + H4 z^4] with H1 = 1 + q0,
H2 = (j0 − q0^2)/2 and higher coefficients in s0, l0 (DES inverse ladder,
Eq. 5); for a flat universe D_L = (c/H0)[z + D1 z^2 + D2 z^3 + D3 z^4 +
D4 z^5], D1 = (1 − q0)/2, D2 = −(1 − q0 − 3 q0^2 + j0)/6 (Eq. 6); then
D_M = D_L/(1 + z) (Eq. 11) and D_H = c/H (Eq. 10) [src: arXiv:2406.05049,
Sects. 2.1, 2.3]. Stated reason: a smooth expansion of the scale factor
with "minimal assumptions about the underlying cosmological model" beyond
homogeneity and isotropy [src: arXiv:2406.05049, Sect. 2.1]. The
curvature term k/a0^2 can replace l0, since the fifth-order term is not
available without flatness [src: arXiv:2602.12822, Sect. 2.3].

**Flexible dark-energy families.** BOSS used "PolyCDM" with a loose
Omega_k = 0 ± 0.1 prior "to suppress high curvature models that are
clearly inconsistent with the CMB", and checked o w0waCDM and LCDM [src:
arXiv:1411.1074, Sect. IV].

Stated reason why the extrapolation is harmless: the SN relative distances
are "precisely measured over a well sampled redshift interval which
includes the BAO redshifts" [src: arXiv:1411.1074, Sect. IV].

### Step 2. Build the two likelihoods
<!-- key: step-2-build-the-two-likelihoods -->

SN term: mu_data = m_b,data − M_B with M_B free (Eq. 7),
mu_theory = 5 log10(D_L / 1 Mpc) + 25 (Eq. 8),
chi^2_SN = D^T C_SN^-1 D (Eq. 9), with the statistical-plus-systematic
covariance of the compilation [src: arXiv:2406.05049, Sect. 2.2]. The
corrected apparent magnitudes are used, not the published moduli, because
the latter carry an assumed H0 and M_B [src: arXiv:2406.05049, Sect. 2.2].

BAO term: chi^2_BAO = Delta^T C_BAO^-1 Delta over the published D_M/r_d,
D_H/r_d and D_V/r_d with their covariance (Eq. 13) [src: arXiv:2406.05049,
Sect. 2.3; arXiv:2602.12822, Eq. 18].

Total: chi^2 = chi^2_BAO(r_d, Theta) + chi^2_SN(M_B, Theta) (Eq. 14), with
Theta the expansion parameters; sampled with dynesty, 500 live points,
default stopping [src: arXiv:2406.05049, Sect. 2.4; arXiv:2602.12822,
Eq. 23].

### Step 3. Calibrate r_d
<!-- key: step-3-calibrate-rd -->

| Analysis | r_d input | Stated reason | Place read |
|---|---|---|---|
| BOSS 2015 | 147.49 ± 0.59 Mpc from Planck omega_m, omega_b, standard radiation | CMB enters only through omega_m and omega_b | arXiv:1411.1074, Sect. IV, Table 3 |
| DES SN + DESI DR1 (2024) | Gaussian N(147.46, 0.28) Mpc | from CMB likelihoods with late-ISW, optical depth, CMB lensing and foreground dependence removed | arXiv:2406.05049, Sect. 2.3 |
| DES-Dovekie + DESI DR2 (2026) | same N(147.46, 0.28) | independent of late-time cosmology | arXiv:2602.12822, Sect. 2.1 |

BOSS gives the result in a form that survives a change of r_d:
H0 = (67.3 ± 1.1) × (147.49 Mpc / r_d) (Eq. 23); raising N_eff from 3.046
to 4.0 moves the central value to 69.5 [src: arXiv:1411.1074, Sect. IV,
Eq. 23].

### Step 4. Read off H0 and M_B
<!-- key: step-4-read-off-h0-and-mb -->

H0 is the z → 0 intercept of c ln(1+z)/D_M(z), a quantity that "approach[es]
H0 as z approaches zero, independent of other cosmological parameters"
[src: arXiv:1411.1074, Sect. II.5]. M_B comes out alongside: −19.14 ±
0.042 for a fiducial SALT2 SN in a low-mass host (BOSS, JLA) [src:
arXiv:1411.1074, Sect. IV]; −19.375 (+0.018/−0.017) with DES-SN5YR, against
−19.253 ± 0.027 from Cepheids [src: arXiv:2406.05049, Sect. 3]. M_B values
from different compilations are not interchangeable: each is tied to its
own light-curve standardisation (BOSS defines its fiducial SN explicitly
for that reason) [src: arXiv:1411.1074, Sect. IV].

### Step 5. BAO + BBN in LCDM
<!-- key: step-5-bao-bbn-in-lcdm -->

BAO alone measure Omega_m and H0 r_d; with standard neutrinos (N_eff =
3.044, sum m_nu = 0.06 eV), omega_b fixes r_d through the fitting formula,
so a BBN prior breaks the degeneracy [src: arXiv:2503.14738, Sect. IV.1].
DESI DR2 uses omega_b = 0.02218 ± 0.00055 (LCDM; PRyMordial with
marginalised rates), or 0.02196 ± 0.00063 with N_eff free [src:
arXiv:2503.14738, Eqs. 14, 15]. Result: 68.51 ± 0.58 (Eq. 19), 68.45 ±
0.47 with theta_* (Eq. 20), against 68.53 ± 0.80 in DR1 [src:
arXiv:2503.14738, Sect. VI]. Unlike the inverse ladder this assumes flat
LCDM at low redshift.

### Step 6. Sound-horizon-free variants
<!-- key: step-6-sound-horizon-free-variants -->

**(a) Full shape with the BAO wiggles marginalised (equality scale).** Split
the linear power spectrum into smooth and wiggly parts and rescale only the
wiggles: P_lin(k, q_BAO) = P_smooth(k) + P_wiggly(q_BAO k) (Eq. 3), which
rescales r_d by 1/q_BAO; q_BAO ~ U[0.9, 1.1] [src: arXiv:2411.16677,
Sect. 2, Table 1]. Stated reason for this over an uninformative omega_b
prior: a free omega_b also weakens the k_eq and critical-density
information, while rescaling keeps an informative BBN prior [src:
arXiv:2411.16677, Sect. 2]. k_eq ∝ Omega_cb h (Eq. 2); with
k = 0.02–0.20 h/Mpc the turnover (~0.015 h/Mpc) is not in the data vector,
and the information comes from the broadband shape above k_eq [src:
arXiv:2411.16677, Sect. 4.1]. CMB lensing is added because projection
washes out the wiggles, so it sees k_eq but not r_d [src: arXiv:2411.16677,
Sect. 2]. Omega_m from uncalibrated SNe or Lyα AP breaks the remaining
Omega_m–H0 degeneracy [src: arXiv:2411.16677, Sects. 2, 4.8].

**(b) BAO with r_d as a free parameter plus an Omega_m h^2 constraint.**
CAMB is modified so that r_d is a primary parameter in the BAO likelihood
only; CMB lensing (and optionally DES 3×2pt) constrains Omega_m h^2 through
k_eq, and theta_* is added as a transverse BAO point at z = 1100 [src:
arXiv:2509.16202, Sects. II.1, III.2]. Stated reason over full shape: all
three BAO observables are used at each redshift, so H0 depends less on an
SN Omega_m [src: arXiv:2509.16202, Sect. II.1].

**(c) Chronometer-calibrated ladders.** Gaussian-process reconstructions of
H(z) from cosmic chronometers calibrate M_B against SNe and r_d against BAO
on a grid in (M_B, Omega_k, r_d); H0 then follows from the Hubble-flow SNe
with M_B, in the SH0ES form with q0 free or fixed [src: arXiv:2511.19332,
Sects. 3.1–3.2.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Expansion model and its order
<!-- key: expansion-model-and-its-order -->

DES-SN5YR + DESI DR1 BAO, same r_d prior [src: arXiv:2406.05049, Table 1]:

| Model | H0 | M_B | Delta AIC (vs 4th order) |
|---|---|---|---|
| flat LCDM | 67.67 (+0.69/−0.68) | −19.394 | 6.1 |
| 3rd order | 70.03 (+0.66/−0.65) | −19.344 | 89.9 |
| 4th order (baseline) | 67.19 (+0.66/−0.64) | −19.375 | 0.0 |
| 5th order | 67.26 (+0.73/−0.71) | −19.381 | 2.3 |

The third order fits DES-SN5YR alone but not the higher-redshift BAO
(Delta chi^2 = 81), so the too-short series raises H0 by 2.8 [der: 70.03
− 67.19] [src: arXiv:2406.05049, Sect. 3]. With DES-Dovekie + DESI DR2: 66.54 ± 0.70
(4th), 66.82 ± 0.74 (5th, weakly preferred, Delta AIC = 2.1), 66.59 ± 0.69
with curvature free [src: arXiv:2602.12822, Table 1]. BOSS: PolyCDM 67.3 ±
1.1, o w0waCDM 67.1 ± 1.1, LCDM "nearly unchanged" [src: arXiv:1411.1074,
Sect. IV, Table 3]. Choose the order by an information criterion on the
joint data, and report the next order as a variant.

### Which BAO observable
<!-- key: which-bao-observable -->

Splitting DESI DR2: D_M-only measurements give 67.16 (+0.85/−0.80),
D_H-only 71.2 (+2.0/−1.9) [src: arXiv:2602.12822, Sect. 4.1]. Splitting by
redshift, DESI + BBN at z < 1.1 and at z > 1.1 are each more than 3 sigma
from SH0ES [src: arXiv:2503.14738, Fig. 9 caption]. Anisotropic (3D)
against angular (2D) BAO in the chronometer ladder: 68.83 against 69.85
(+3.19/−3.58), the angular data favouring higher H(z) as in earlier work
[src: arXiv:2511.19332, Sect. 4.1, Table 2].

### Which SN compilation
<!-- key: which-sn-compilation -->

On the DESI DR2 inverse ladder: DES-Dovekie 66.82 ± 0.74, Pantheon+ 66.35
(+0.81/−0.86), Union 66.15 ± 0.86 [src: arXiv:2602.12822, Sect. 4.1]. BOSS:
Union 2.1 for JLA leaves H0 unchanged and inflates the error by ~30% [src:
arXiv:1411.1074, Sect. IV]. The compilation matters more where the
Hubble-flow SNe set the result: the chronometer ladder gives 68.83 with the
DES-SN5YR Hubble flow and 72.12 ± 2.97 with Pantheon+, because Hubble-flow
SNe common to both are fainter in DES-SN5YR [src: arXiv:2511.19332,
Sect. 4.1].

### How r_d is calibrated
<!-- key: how-rd-is-calibrated -->

- CMB-calibrated r_d: its 0.4% error is "already small"; shrinking it ten
  times leaves the H0 error unchanged, while shrinking the SN or the BAO
  errors halves it — the two add roughly linearly [src: arXiv:1411.1074,
  Sect. IV]. WMAP9 in place of Planck: 66.9 ± 1.2 [src: arXiv:1411.1074,
  Sect. IV].
- BBN-calibrated r_d (LCDM): 68.51 ± 0.58 [src: arXiv:2503.14738, Eq. 19].
- Free r_d with k_eq from full shape: 71.2 ± 4.1 (DESI DR1 galaxies alone);
  70.1 (+2.7/−3.3) with CMB lensing; 69.6 (+2.4/−2.6) adding Lyα AP; 66.1
  to 67.6 adding SN Omega_m [src: arXiv:2411.16677, Table 2]. q_BAO =
  0.995 (+0.021/−0.022), consistent with 1 within 1.8 to 2.0 sigma [src:
  arXiv:2411.16677, Sect. 5].
- Free r_d with BAO + theta_* + CMB lensing: 70.5 ± 2.0; + DES Y3 70.3 ±
  1.7; + A_s prior 70.40 ± 0.98; + Pantheon+ 70.03 ± 0.97; pre-DESI BAO
  68.7 ± 1.7 [src: arXiv:2509.16202, Sect. IV.1]. Precision is limited by
  Omega_m h^2, hence the A_s prior N(3.04, 0.02), chosen to contain A_s in
  modified-recombination and early-dark-energy fits [src: arXiv:2509.16202,
  Sects. III.2, IV.1].
- Chronometer-calibrated r_d: 144.00 (+5.08/−4.88) Mpc and H0 = 68.83
  (+3.03/−3.07) [src: arXiv:2511.19332, Table 2].

### Prior-volume effects in the r_d-free full shape
<!-- key: prior-volume-effects-in-the-rd-free-full-shape -->

Opening q_BAO enlarges the nuisance space; on mocks without a Jeffreys
prior H0 shifts by ~2 sigma, corrected "almost entirely" with it; the
counterterms and stochastic terms are profiled at each point [src:
arXiv:2411.16677, Sect. 4.4]. Priors: H0 U[20, 100], omega_b BBN, n_s
N(0.9649, 0.042) (ten times the Planck width), N(0.96, 0.02) with CMB
lensing; sum m_nu fixed at 0.06 eV [src: arXiv:2411.16677, Sect. 4.4,
Table 1]. See `cosmo-statistics-inference` for projection effects in
general.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| r_d prior | N(147.46, 0.28) Mpc | DES + DESI inverse ladders | arXiv:2406.05049; arXiv:2602.12822 | Sects. 2.3; 2.1 |
| r_d prior | 147.49 ± 0.59 Mpc | BOSS | arXiv:1411.1074 | Table 3 |
| DES-SN5YR sample | 1829 SNe (1635 DES at 0.10–1.13 + 194 low-z) | DES + DESI DR1 | arXiv:2406.05049 | Sect. 2.2 |
| DESI DR1 BAO input | 12 measurements, 7 bins, 0.1 < z < 4.2 | DES + DESI DR1 | arXiv:2406.05049 | Sect. 2.3 |
| q0, j0, s0 (4th order) | −0.342 ± 0.013; 0.255; −0.494 | DES + DESI DR1 | arXiv:2406.05049 | Table 1 |
| q0 (5th order), spread over SN systematics | −0.48; ≤ 0.01 | DES-Dovekie + DESI DR2 | arXiv:2602.12822 | Sect. 4.2 |
| H0 spread over all DES-Dovekie SN systematics | 0.1 | DESI DR2 inverse ladder | arXiv:2602.12822 | Sect. 4.2 |
| Low-z (z ≤ 0.1) magnitude step tested | −0.05 to −0.35 mag in 0.05 steps; −0.30 gives 70.96 (+0.55/−0.54) | DES-Dovekie + DESI DR2 | arXiv:2602.12822 | Sects. 3.2, 4.2 |
| Linear d mu/dz tested | p = 0.20 gives 71.08, strongly disfavoured | same | arXiv:2602.12822 | Sect. 4.2 |
| Delta AIC of a −0.05 mag low-z step; of −0.30 | 20; 4000 | same | arXiv:2602.12822 | Sect. 4.2 |
| Omega_M (flat LCDM, SN only) after a −0.30 mag step | 0.134, 13 sigma from 0.330 ± 0.015 | same | arXiv:2602.12822 | Sect. 4.2 |
| Tension of DES + DESI DR1 inverse ladder with SH0ES 2022 | ~4.6 sigma | DES + DESI DR1 | arXiv:2406.05049 | Sect. 3 |
| DESI + CMB in LCDM | H0 = 68.17 ± 0.28, Omega_m = 0.3027 ± 0.0036 | DESI DR2 | arXiv:2503.14738 | Sect. VI table |
| Full-shape data vector | k = 0.02–0.20 h/Mpc, ell = 0, 2, dk = 0.005 | DESI DR1 | arXiv:2411.16677 | Sect. 4.1 |
| Chronometer ladder with SH0ES M_B on DES-SN5YR Hubble flow | 70.84 ± 1.16 | CCH + DESY5 | arXiv:2511.19332 | Sect. 4.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Truncated cosmography.** A third-order series fits SNe alone but fails
  once BAO at z > 1 are added and raises H0 by 2.8 [der]; test: Delta AIC and
  Delta chi^2 between orders on the joint data [src: arXiv:2406.05049,
  Sect. 3].
- **Calling it independent of the CMB.** It "does depend on the drag scale
  r_d calibrated from the CMB so it is not an entirely independent
  measurement" [src: arXiv:2406.05049, Sect. 3]; what is removed is the
  late-time model. Report H0 × (r_d/147.49) or the r_d used [src:
  arXiv:1411.1074, Eq. 23].
- **Expecting SN systematics to move it.** The BAO set the absolute scale
  at high z; SN systematics move H0 by 0.1 and q0 by 0.01, and a
  low-z step large enough to give 71 is ten times any listed SN
  systematic [src: arXiv:2602.12822, Sect. 4.2].
- **Distance duality.** The method converts D_L to D_M with
  D_M = D_L/(1 + z), valid "in any metric theory of gravity"; BOSS tested a
  free modification of D_L [src: arXiv:1411.1074, Sect. IV]. A late-time
  fix that breaks it is a different hypothesis
  (`open-questions.md#theory-status-summary-details-in-sibling-skills`).
- **Mixed M_B.** Comparing an inverse-ladder M_B with a Cepheid M_B from a
  different compilation mixes standardisations; compare within one
  compilation [src: arXiv:1411.1074, Sect. IV; arXiv:2406.05049, Sect. 3].
- **Projection effects in r_d-free fits.** ~2 sigma shifts in H0 on mocks
  without a Jeffreys prior [src: arXiv:2411.16677, Sect. 4.4]; test with
  mocks and profile likelihoods.
- **Omega_m h^2 from lensing degenerate with A_s and sum m_nu.** H0 moves
  with the A_s prior and correlates positively with sum m_nu [src:
  arXiv:2509.16202, Sects. II.4, IV.1]; report the neutrino and A_s
  assumptions.
- **Reconstruction bias of Gaussian processes.** A zero prior mean biases
  the reconstructed H(z); quantified on mocks as at most 0.3 sigma on M_B
  [src: arXiv:2511.19332, Sects. 3.2, 4.1].
- **BAO–CMB inconsistency in LCDM.** DESI BAO and the CMB differ by 2.3
  sigma in (Omega_m, r_d h), and DESI + BBN overlaps the CMB posterior at
  the same level [src: arXiv:2503.14738, Sect. VI]; a combined
  "early" endpoint inherits it (`cosmo-tensions-anomalies`,
  `deep/cmb-bao-mismatch.md`).

## Reading list
<!-- key: reading-list -->

- Aubourg et al. 2015, arXiv:1411.1074 (foundation of current practice):
  Sect. IV for the construction, Eq. 23, and the error-budget tests by
  covariance rescaling.
- Cuesta et al. 2015, arXiv:1411.1094 (foundation): the two anchors, H0 at
  z = 0 or r_d at high z (abstract read for L2).
- Camilleri et al. 2024, arXiv:2406.05049 (method and application):
  cosmography Eqs. 5–14, r_d prior, order selection.
- Popovic & Sullivan 2026, arXiv:2602.12822 (test): SN systematics, low-z
  steps, D_M against D_H, compilation swap.
- DESI Collaboration 2025, arXiv:2503.14738 (application): BBN prior,
  Eqs. 14–20, redshift split.
- Zaborowski et al. 2025, arXiv:2411.16677 (method): q_BAO rescaling,
  priors, Jeffreys prior.
- García Escudero et al. 2025, arXiv:2509.16202 (method): r_d as a free
  parameter with CMB lensing; the A_s prior.
- Favale et al. 2025, arXiv:2511.19332 (alternative): chronometer-
  calibrated M_B and r_d; compilation dependence of the Hubble flow.

## Not verified
<!-- key: not-verified -->

- The paper that derives the N(147.46, 0.28) Mpc r_d prior (cited as Lemos
  & Lewis 2023 in arXiv:2406.05049) was not read. [src: Sect. 2.3]
- The PolyCDM parametrisation itself (Sect. II.1 of arXiv:1411.1074) and
  BOSS's distance-duality test result were not read.
- The DES-Dovekie systematics tables (Tables 6 and 7 of the DES-Dovekie
  paper) behind the 0.1 spread were read only through arXiv:2602.12822.
- An inverse ladder with DESI DR2 and Union3 or with Gaussian-process
  expansion instead of cosmography (other than the chronometer ladder).
