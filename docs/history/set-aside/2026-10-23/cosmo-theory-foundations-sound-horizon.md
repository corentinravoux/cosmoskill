# Set aside from cosmo-theory-foundations/deep/sound-horizon.md

Numbers run of 2026-10-23 (plan of 2026-10-23, steps 1 and 3; owner's rule: no number computed by an agent). The blocks below held agent-computed values: accuracy tables and checks computed with CAMB 2.0.4 at a fiducial point chosen by the agent ([der: CAMB]), and ratios or differences of paper values ([der]). They are copied verbatim from the file as it stood at commit 2b5e381 before removal; line numbers are those of that version.

## Lines 1-9

# Sound horizon r_s, r_d, z_*, z_d, θ_* and θ_MC — cosmo-theory-foundations dossier

Scope: how the two decoupling epochs are defined in the papers and codes
that compute them (and why 1020 and 1060 are both quoted for z_d), how
accurate each sound-horizon formula is against a Boltzmann code across the
parameter range, which assumptions (neutrino splitting, helium, recombination
code, decoupling definition) move r_d at the 0.01–1% level, and how an
analysis calibrates r_d or stays agnostic to it.
Snapshot: 2026-10-18.

## Lines 24-29

Numerical checks flagged [der: CAMB] were run this session with CAMB 2.0.4
(`camb.get_background`, default Recfast recombination, T_CMB = 2.7255 K,
Y_He from the BBN table, 0.2457 at the fiducial point), at H0 = 67.36 km/s/Mpc,
ω_b = 0.02237, ω_c = 0.1200, one massive neutrino of 0.06 eV and N_eff = 3.044
unless stated. They are a derivation with one code version, not a published
accuracy; CLASS could not be run in this session.

## Lines 69-82

| Quantity | Value | Source |
|---|---|---|
| z_drag, Planck 2018 TT,TE,EE+lowE+lensing | 1059.94 ± 0.30 | arXiv:1807.06209, Table 2 [src] |
| z_drag, same, TT+lowE | 1059.39 ± 0.46 | same [src] |
| z_drag, CAMB at the fiducial point | 1059.93 | [der: CAMB] |
| z_*, CAMB at the fiducial point | 1089.91 | [der: CAMB]; Planck 2018 gives 1089.92 ± 0.25 (L2) |
| r_drag, CAMB at the fiducial point | 147.103 Mpc | [der: CAMB]; Planck 2018 147.09 ± 0.26 Mpc |
| r_*/r_drag, CAMB | 0.98192 | [der: CAMB]; the Planck 2018 table values give 144.43/147.09 = 0.98192 [der] |
| r_s/r_d with CLASS, ΛCDM fit to Planck 2018 + DESI DR2 + Pantheon+ | 0.98283 (+0.00025/−0.00027) | arXiv:2510.15835, Sect. III.2 [src] |
| r_s/r_d with CLASS, EDE fit to the same data | 0.98334 (+0.00042/−0.00051) | same [src] |

The CAMB and CLASS ratios differ by 0.09% [der]. A visibility-peak z_*
lies at a different redshift from a τ = 1 z_*, which would produce a
difference of this kind; the cause was not checked (no CLASS run).

## Lines 100-117

Ω_0 h² being the total matter density. Eisenstein & Hu 1998 copy Eq. E2 with
1291 in place of 1345: "we have reduced z_d by a factor of 0.96 from HS (96)
on phenomenological grounds" [src: arXiv:astro-ph/9709112, Sect. 2.1;
1291/1345 = 0.960, der]. At the fiducial point:

| Formula | z | Against CAMB |
|---|---|---|
| Hu–Sugiyama E1, z_* | 1091.9 | +0.18% [der] |
| Hu–Sugiyama Eq. E2, z_d (τ_d = 1 definition) | 1063.4 | +0.33% [der] |
| Eisenstein–Hu Eq. 4, z_d (× 0.96) | 1020.7 | −3.7% [der] |

eBOSS writes that the drag epoch is "around a redshift z = 1020" without
naming its source [src: arXiv:2007.08991, Sect. II.3.1]; the value matches the
Eisenstein–Hu formula at Planck densities [der], whereas DESI's z_d ≈ 1060
(L2) and Planck's 1059.94 are the τ_d = 1 epoch. The Eisenstein–Hu z_d is a
fitting device chosen so that their transfer-function fit works, not the
redshift at which τ_d = 1; this resolves the item left open in
`physics-and-methods.md#not-verified` [der from the three sources above].

## Lines 119-141

### Step 4. Get θ_* and know what θ_MC is
<!-- key: step-4-get-theta-and-know-what-thetamc-is -->

θ_MC is "an approximation to θ_* that is used in CosmoMC and is based on
fitting formulae given in Hu & Sugiyama (1996)" (L2). The z_* fit is
Eq. E1 above; at the fiducial point it is 2.0 redshift units above the
numerical z_* [der]. DESI samples 100θ_MC because it "helps approximate the
degeneracy direction of the CMB parameter space while being faster to
calculate the conversion to H0 and Ω_m"; "any difference between the values
of θ_MC and θ_* only slightly affects the efficiency of the sampling while
having no effect on the accuracy of the likelihood evaluation" [src:
arXiv:2503.14738, Sect. V, footnote 17].

| Quantity | Value | Source |
|---|---|---|
| 100(θ_MC − θ_*), Planck 2018 chain means | −0.00018 | L2 [der] |
| 100(θ_MC − θ_*), CAMB, fiducial point | −0.00022 | [der: CAMB, `cosmomc_theta()` against `thetastar`] |
| same, over ω_b = 0.0210–0.0238, ω_c = 0.105–0.135 | −0.00038 to −0.00005, driven by ω_b | [der: CAMB] |
| Planck error on 100θ_* | 0.00031 | L2 |

The offset is therefore 0.2 to 1.2 times the Planck error across that box
[der]: a prior written on θ_* must be applied to θ_*, and the offset is not
a constant that can be subtracted once.

## Lines 152-158

| Route | What enters | Where used |
|---|---|---|
| Full CMB likelihood | r_d computed by the Boltzmann code at each sample | DESI DR2 with CMB [src: arXiv:2503.14738, Sect. V] |
| Compressed early-Universe prior | Gaussian on (θ_*, ω_b, ω_bc) = (0.01041, 0.02223, 0.14208) with covariance 10⁻⁹ × [[0.006621, 0.12444, −1.1929], [0.12444, 21.344, −94.001], [−1.1929, −94.001, 1488.4]] | DESI DR2 [src: Eqs. 35–36, App. A]; σ = 2.6 × 10⁻⁶, 1.5 × 10⁻⁴, 1.2 × 10⁻³ [der] |
| BBN prior on ω_b | r_d from ω_b and the BAO-fitted Ω_m h² | DESI DR2 (L2) |
| Uncalibrated, Method I | ratios that cancel r_s and r_d | arXiv:2510.15835, Eqs. 10–14 [src] |
| Uncalibrated, Method II | r_s free (flat prior), r_d = r_s/(r_s/r_d)_CLASS | arXiv:2510.15835, Sect. III.2 [src] |

## Lines 185-211

### Boltzmann value or a formula
<!-- key: boltzmann-value-or-a-formula -->

Accuracy against CAMB 2.0.4 on a 5 × 5 grid ω_b ∈ {0.0210, 0.0218, 0.02237,
0.0230, 0.0238}, ω_c ∈ {0.105, 0.112, 0.120, 0.128, 0.135}, N_eff = 3.044,
one 0.06 eV state [der: CAMB]:

| Formula | At the fiducial point | Over the grid | Why |
|---|---|---|---|
| DESI DR2 Eq. 2 (power law) | +0.079% | −0.15% to +0.41% | the CAMB slope d ln r_d/d ln ω_bc at fixed ω_b is −0.255, against −0.23 in Eq. 2; the other slopes agree (−0.129 against −0.13 for ω_b at fixed ω_bc; −0.104 against −0.1 for N_eff) |
| Aubourg Eq. 16 | −0.027% | −0.028% to +0.058% | calibrated for N_eff = 3.046; run here at 3.044 |
| Eisenstein–Hu Eq. 6 with its own z_d | +2.59% | — | the Planck 2013 factor was 1.0275 at the 2013 fiducial model (L2) |
| Eisenstein–Hu short form Eq. 26 | +1.86% | — | stated "∼2%" (L2) |

With N_eff free (ω_b, ω_c fixed at the fiducial values) [der: CAMB]:

| N_eff | CAMB r_drag (Mpc) | DESI Eq. 2 | Aubourg Eq. 17 |
|---|---|---|---|
| 2.5 | 149.93 | +0.14% | −0.14% (outside its stated 3 < N_eff < 5) |
| 3.044 | 147.10 | +0.08% | −0.03% |
| 3.5 | 144.87 | +0.21% | +0.02% |
| 4.0 | 142.55 | +0.49% | +0.04% |

What this buys: DESI DR2 measures h r_d to 0.7% (L2), so Eq. 2 is adequate
for illustration near the Planck point and inadequate as a substitute for
the Boltzmann value in an extended model or far from it; the Aubourg fits
stay below 0.06% in the box above.

## Lines 213-225

### One massive state or three degenerate
<!-- key: one-massive-state-or-three-degenerate -->

At fixed ω_cb, changing Σm_ν from 0 to 0.5 eV moves r_drag by −0.26% with
one massive state and −0.105% with three degenerate states; at 1.0 eV by
−0.80% and −0.38% [der: CAMB, N_eff = 3.046]. Aubourg et al. quote −0.26%
(0.5 eV) and −0.92% (1.0 eV) [src: arXiv:1411.1074, Sect. II.2]. Their
Eq. 16 reproduces CAMB to −0.012% at 0.5 eV with one massive state and is
off by −0.17% with three degenerate states [der: CAMB]. The fit therefore
encodes the single-massive-state convention; DESI DR2 varies Σm_ν with
"three degenerate mass eigenstates" [src: arXiv:2503.14738, Sect. V], so a
re-analysis that uses Eq. 16 with degenerate masses carries an error that
reaches 0.17% at 0.5 eV [der].

## Lines 227-248

### Recombination physics and helium
<!-- key: recombination-physics-and-helium -->

Planck 2018: the atomic-physics and radiative-transfer effects omitted by
earlier recombination calculations "can lead to significant biases to
several cosmological parameters", but "at the present level of precision
these can be reliably incorporated within the advanced recombination codes
CosmoRec … and HyRec …, as well as the recfast code …, modified using
corrections calculated with the more precise codes" [src: arXiv:1807.06209,
Sect. 7.7]. No r_d difference between these codes was read. The helium
fraction does move r_d slightly: Y_He from 0.235 to 0.255 changes r_drag
from 147.134 to 147.074 Mpc (−0.041%), z_drag from 1059.58 to 1060.25 and
r_* by −0.049% [der: CAMB]. Codes that fix Y_He instead of taking it from
BBN differ by that order.

### Which z_* definition
<!-- key: which-z-definition -->

τ = 1 (Planck, CAMB) or visibility peak (CLASS as described in
arXiv:2510.15835). The r_* difference this implies was not measured here;
the 0.09% gap between the CAMB and CLASS r_*/r_d ratios above is the only
indication, with different data combinations behind the two numbers.

## Lines 260-277

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
| r_*/r_drag (CAMB) | 0.98192 | fiducial point | this session | [der: CAMB] |
| DESI Eq. 2 against CAMB | +0.08% (pivot), up to +0.41% (ω_c = 0.135), +0.49% (N_eff = 4) | — | this session | [der: CAMB] |
| Aubourg Eq. 16 against CAMB | ≤ 0.06% on the grid; −0.17% at 0.5 eV with 3 degenerate states | — | this session | [der: CAMB] |
| d ln r_d / d ln ω_bc (fixed ω_b); / d ln ω_b (fixed ω_bc); / d ln N_eff | −0.255; −0.129; −0.104 | fiducial point | this session | [der: CAMB] |
| Δr_drag for ΔY_He = +0.02 | −0.041% | fiducial point | this session | [der: CAMB] |
| 100(θ_MC − θ_*) | −0.00022 (fiducial); −0.00005 to −0.00038 over ω_b 0.021–0.024 | — | this session | [der: CAMB] |
| Compressed CMB prior means | θ_* = 0.01041, ω_b = 0.02223, ω_bc = 0.14208 | CamSpec-based | arXiv:2503.14738 | Eq. 35 |

## Lines 279-299

## What goes wrong
<!-- key: what-goes-wrong -->

- **Eisenstein–Hu z_d quoted as the drag redshift.** Shows up as z_d ≈ 1020
  next to a Boltzmann r_d. Test: recompute with τ_d = 1; the Planck value is
  1059.94.
- **A fitting formula used outside its pivot.** DESI Eq. 2 drifts to 0.4–0.5%
  at the edge of a wide prior box or at N_eff = 4. Test: compare with the
  Boltzmann r_drag at the best fit and at the prior edges.
- **Aubourg Eq. 16 with degenerate neutrinos.** Shows up as a 0.1–0.2%
  r_d offset growing with Σm_ν. Test: compute r_drag with the neutrino
  setting of the chain.
- **θ_MC treated as θ_*.** A prior on one applied to the other is off by
  0.2–1.2σ of Planck, depending on ω_b. Test: report which one the prior is
  on; DESI uses θ_* in its compressed prior (Eq. 35).
- **r_*/r_d assumed universal across codes.** CAMB 0.9819 against CLASS-based
  0.9828. Matters for uncalibrated ratios only at the 0.1% level, below
  current BAO errors.
- **Calibration hidden in a "model-independent" H0.** BAO + BBN or BAO + θ_*
  inherit the pre-recombination assumption; Method I or II of
  arXiv:2510.15835 removes it at the cost of the r_s/r_d assumption.

## Lines 321-337

## Not verified
<!-- key: not-verified -->

- The r_d and r_* given by CLASS for the same input as the CAMB runs above,
  and the size of the τ = 1 against visibility-peak z_* difference: CLASS
  (pyclass) could not be imported in this session.
- Differences in r_d between CosmoRec, HyRec and Recfast: Planck 2018 says
  they agree "at the present level of precision" but gives no r_d number;
  CosmoRec and HyRec were not compiled into the CAMB used here.
- Why Aubourg et al.'s −0.92% at 1.0 eV differs from the −0.80% that CAMB
  2.0.4 gives with one massive state (the 0.5 eV value agrees): CAMB version
  or neutrino-treatment differences were not investigated.
- The CosmoMC/CAMB implementation of θ_MC was not read in source (the
  compiled routine is not shipped as text); the Hu–Sugiyama attribution is
  Planck's and DESI's.
- r_d in models with non-standard recombination (varying m_e, EDE) beyond the
  r_s/r_d statement of arXiv:2510.15835.
