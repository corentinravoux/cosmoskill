# H0 from fast radio bursts — cosmo-multimessenger dossier

Scope: how an FRB H0 is built in its three current forms (survey forward
model of `P(z, DM, SNR)`, per-burst `p(DM | z)` of localised bursts, the DM
distribution of unlocalised bursts) and in combination with BAO, with each
model component, prior and completeness cut and the authors' reasons, and
how to choose between them. Route A rests on one code (zDM, ASKAP/CRAFT);
the per-burst and unlocalised routes have several independent groups, each
listed under its step.
Snapshot: 2026-10-22.
From: Glowacki & Lee 2024 review (arXiv:2410.24072), Sect. 5; ASKAP/CRAFT
zDM analyses; the per-burst, unlocalised, dark-siren, neural-network and
simulation-based analyses of other teams.

Already in L2, not repeated here: the DM budget, the Macquart relation and
the `Ω_b h² f_d / h` degeneracy
(`physics-and-methods.md#budget`, `#what-is-degenerate-with-what`); the
likelihood table of Macquart 2020, James 2022 and Connor 2024 and the two
likelihood styles (`physics-and-methods.md#scatter-and-the-likelihood`); the
size of each systematic on the Xu et al. 2025 H0 (Galactic disc, halo, host,
`F`, `f_d`) and the cliff effect
(`systematics.md#fast-radio-bursts-host-and-milky-way-dispersion`); the H0
values and sample sizes (`results.md#h0-from-the-dispersion-measure-redshift-relation`);
the baryon-partition analyses (`deep/frb-baryon-distribution.md`).

## How it is done
<!-- key: how-it-is-done -->

Notation. `DM_EG` (also `DM_E`, `DM_ext`) is the extragalactic DM,
`DM_cosmic` (also `DM_IGM`, `DM_cos`) the intergalactic part, `DM_host` the
rest-frame host term, `μ_host`, `σ_host` the parameters of its log-normal
(median `e^μ_host`), `Δ = DM_cosmic / ⟨DM_cosmic⟩`, `F` (also `f`) the
fluctuation parameter in `σ_Δ = F z^(−1/2)`, `s` the SNR relative to the
survey threshold, `B` the beam sensitivity, `w` the burst width, `E` the
isotropic-equivalent burst energy, `γ` the slope of the energy function,
`E_max` (also `E_*`) its cut-off, `α` the frequency index of the rate,
`n_sfr` (also `n`) the power of the star-formation history followed by the
burst rate. Equations follow James et al. 2022 (arXiv:2208.00819) for the
forward model, Zhang et al. 2026 (arXiv:2610.15536) for the localised
likelihood, Liu et al. 2026 (arXiv:2604.03769) for unlocalised bursts.

### Route A. Survey forward model of `P(z, DM, SNR)` (zDM)
<!-- key: route-a-survey-forward-model-of-p-z-dm-snr-zdm -->

1. **DM components** [src: arXiv:2208.00819, Sect. 2.1, Eq. 1–10]:
   `DM_FRB = DM_EG(z) + DM_local`, `DM_EG = DM_cosmic + DM_host/(1+z)`,
   `DM_local = DM_ISM(l, b) + DM_halo`; NE2001 for the disc, `DM_halo = 50`
   pc cm⁻³, "largely degenerate" with the host model; log-normal host. Planck
   parameters except H0 and `Ω_b`; `Ω_b h² = 0.02242` held fixed, so that
   `⟨DM_cosmic⟩ ∝ 1/H0` (Eq. 10); `Y_He = 0.25`; `f_d(z = 0) = 0.844` with a
   redshift-evolving `f_d(z)`, whose uncertainty is "unimportant" now but
   may become "a limiting systematic in the era of many thousands of
   well-localized FRBs".
2. **Source evolution** [src: Sect. 2.2.1, Eq. 11–13]:

   ```
   Φ(z) = Φ0 / (1+z) × [SFR(z)/SFR(0)]^n_sfr ,
   SFR(z) = 1.0025738 (1+z)^2.7 / [1 + ((1+z)/2.9)^5.6]
   dV/dΩdz = D_H (1+z)² D_A²(z) / E(z) ,  D_H = c/H0
   ```

   `n_sfr = 0` is no evolution, 1 follows star formation, about 2 is
   AGN-like; a higher H0 lowers the rate per comoving volume element.
3. **Energy function** [src: Sect. 2.2.2, Eq. 14]: cumulative
   `p(E > E_th) = ∫_{E_th}^∞ (E/E_max)^γ exp(−E/E_max) dE` (an upper
   incomplete Gamma, "Schechter"), adopted instead of a hard-cut power law
   because the sharp cut-off produced "numerical artefacts in the analysis of
   H0"; `E_min = 10^30` erg; energies at 1.3 GHz with a 1 GHz effective
   bandwidth; spectral behaviour in the "rate interpretation"
   `Φ(ν) ∝ ν^α`, chosen because it describes the data as well as a spectral
   index and is "computationally much faster".
4. **Widths** [src: Sect. 2.2.3, Eq. 15–16]: intrinsic widths log-normal
   (`log μ_w = 1.70`, `log σ_w = 0.73`, bias-corrected); scattering from
   CHIME at 600 MHz, `log μ_s = 0.7`, `log σ_s = 1.72`, scaled as `ν^(−4)`;
   `w_eff = √(w_int² + w_scat² + w_DM² + w_samp²)`, the last two being DM
   smearing and sampling time.
5. **Rate in `(z, DM)` with beam and width** [src: arXiv:2609.04765, Sect.
   2.3, Eq. 23–29]:

   ```
   R(z, DM | B, w_eff) = P(DM | z) Φ(z) V(z)/(1+z) ∫_{E0(B, w, DM)}^∞ L(E) dE
   R(z, DM) = ∫_0^1 ∫_0^∞ R(z, DM | B, w_eff) Ω(B) P(w_eff) dw_eff dB
   P(N_FRB) = Poisson(⟨N_FRB⟩ = R_FRB Δt)
   ```

   `E0` is the energy at threshold (`s = 1`), `Ω(B)` the solid angle seen at
   beam sensitivity `B`, `Δt` the observing time. The likelihood multiplies
   `P(DM, B, w, s)` for every burst, `P(z | DM, …)` for localised ones, and
   the Poisson term for the number of bursts.
6. **Completeness corrections.** CRAFT/ICS saw 16 bursts with `SNR ≥ 15`
   and only 6 between the threshold of 9 and 15, against 18.4 expected for
   a Euclidean `N(> SNR) ∝ SNR^(−1.5)`; the analysis halves the effective
   observing time to represent the 50% loss [src: arXiv:2208.00819, Sect.
   4.6]. Host completeness: earlier zDM work kept only the part of `(z, DM)`
   where every burst had a confident PATH host, through a maximum `DM_EG` per
   survey (1000 pc cm⁻³ for CRAFT/ICS, so that the `z = 1.016` burst FRB
   20220610A is unused; 183 pc cm⁻³ for a DSA sample, which excluded eight of
   eleven redshifts) [src: arXiv:2609.04765, Sect. 8.1].
7. **Sampling.** H0 on a grid with uniform priors, simulated up to 103 and
   extrapolated by a log-normal fit to 130 km s⁻¹ Mpc⁻¹, every other
   parameter marginalised [src: arXiv:2208.00819, Sect. 5.1].

Other forward models of the selection (no other public `P(z, DM, SNR)` code
was found):

- Sharma et al. 2025 forward-model FRB populations with redshift evolution,
  a luminosity function and a DM selection function, and emulate
  `σ²[DM_cosmic(z)]` with a neural network trained on 5×10⁴ baryonification
  halo-model runs (≤ 4% accurate to `z = 4`); selection alters `p(DM, z)`
  strongly but the conditional `p(DM_exgal | z)` hardly: biases ≲ 0.8σ for
  10² FRBs, possibly > 3σ for 10⁴ depending on the DM search efficiency
  (arXiv:2511.16850) [src: abstract].
- Zhao et al. 2022 normalise their likelihood by `β(H0)`, the integral of
  `p(DM_E | z, H0)` over the hosts below a cut `DM_cutoff = 570` pc cm⁻³,
  after keeping bursts bright enough to avoid the detection threshold
  (arXiv:2212.13433) [src: Sect. III.2, Eq. 11–14] (Route C).

Where H0 comes from in this model [src: arXiv:2208.00819, Sect. 3]:

- the **lower edge** of `P(z, DM)`: the high-DM tail carries host and
  cosmic-web terms, so "the greatest constraining power on H0 is from the
  lower boundary of the contours";
- the **rotation** of the contours with H0, while host parameters "rigidly
  shift and/or widen the contours parallel to DM_EG", so the two are not
  highly degenerate;
- the **redshift reach**: a higher H0 makes a "smaller" universe seen to
  higher `z`, which is "partially degenerate" with `E_max`; in `P(z, SNR)`
  lowering H0 by 10 is "nearly equivalent to lowering `E_max` by 0.1 dex" —
  to the extent that FRB energetics do not evolve, "the analysis is
  effectively a standard candle".

### Route B. Localised bursts, per-burst `p(DM | z)`
<!-- key: route-b-localised-bursts-per-burst-p-dm-z -->

The likelihood of Zhang et al. 2026 [src: arXiv:2610.15536, Sect. II.2,
Eq. 4–10]:

```
⟨DM_IGM(z)⟩ = 3 c Ω_b H0 f_d / (8 π G m_p) ∫_0^z χ_e (1+z') / E(z') dz' ,  χ_e = 7/8 at z < 3
P_IGM(Δ) = A Δ^(−β) exp[−(Δ^(−α) − C0)² / (2 α² σ_IGM²)] ,  α = β = 3 ,  σ_IGM = F z^(−1/2)
P_i = ∫ dDM_halo P_halo ∫ dDM_host P_host P_IGM(Δ_i) / ⟨DM_IGM(z_i)⟩ ,
Δ_i = [DM_E,i − DM_halo − DM_host/(1+z_i)] / ⟨DM_IGM(z_i)⟩ ,  only Δ_i > 0
ln L_FRB = Σ_i ln P_i
```

`A` and `C0` normalise `P_IGM` and set `⟨Δ⟩ = 1`. Choices in that analysis:
halo DM Gaussian 65 ± 15 pc cm⁻³, motivated by estimates of 50–80; `f_d`
flat on [0.84, 0.96] following Connor et al., from `f_d = 1 − f_* − f_cold`
with the stellar fraction allowed to vary by a factor of five; uniform
priors `F` ∈ [0.011, 0.5], `e^μ_host` ∈ [20, 200] pc cm⁻³, `σ_host` ∈
[0.2, 2.0], H0 ∈ [20, 140] [src: Sect. II.2, Table 1].

Peers, by the form taken for `p(DM | z)`:

- **Gaussian.** Hagstotz et al. 2021: `L_i = N(DM_i; DM_LSS(z_i) +
  ⟨DM_host⟩(z_i), σ_i)` with `σ² = σ_MW² + σ_host² + σ_LSS²`; `σ_LSS`
  interpolated linearly from Illustris, about 40 pc cm⁻³ at `z = 0` and 180
  at `z = 1`, scaled with `Ω_b h`; `f_IGM = 0.84`, `Y_He = 0.24`;
  `Ω_m h² = 0.143` and `Ω_b h² = 0.02237` fixed to Planck; 9 bursts give
  62.3 ± 9.1, the 6 gold ones 62.5 ± 10.1 (arXiv:2104.04538) [src: Sect.
  2.1, 3.2, Eq. 9–14].
- **Simulation-calibrated skewed PDF.** Wu et al. 2021 take the Macquart form
  of `P_IGM` with `A`, `C0`, `σ_DM` fitted to IllustrisTNG at each redshift
  (Zhang et al. 2021), a log-normal host with TNG parameters for three host
  types (repeaters like FRB 121102, like FRB 180916, non-repeaters), and a
  Gaussian Milky-Way halo 65 ± 15 pc cm⁻³ (arXiv:2108.00581) [src: Sect. 3,
  Eq. 4–8]. Gao et al. 2024 use the TNG host and IGM distributions for 108
  localised bursts, H0 = 69.40 (+2.14/−1.97) (arXiv:2410.03994) [src:
  abstract].
- **External `Ω_b h²` and `Ω_m` priors instead of fixed values.** Wang et
  al. 2025 take `Ω_b h²` ~ N(0.02233, 0.00036) from the LUNA-based BBN
  value and `Ω_m` ~ N(0.315, 0.007), keep bursts with `DM_obs − DM_MW > 80`
  pc cm⁻³ (86 with NE2001, 88 with YMW16), and tabulate earlier analyses with
  their priors (their Table 2) (arXiv:2501.09260) [src: Sect. II, III].
- **No parametric form for `⟨DM_IGM(z)⟩`.** Fortunato et al. 2024 fit
  `⟨DM_IGM(z)⟩` with an artificial neural network, invert its derivative
  for `H(z) ∝ Ω_b h² f_IGM f_e (1+z) (d⟨DM_IGM⟩/dz)^(−1)` and extrapolate
  to `z = 0`; IGM scatter `σ_ΔIGM = 173.8 z^0.4` pc cm⁻³ and
  `σ_local ≈ 30`; 23 bursts give 67.3 ± 6.6 (arXiv:2407.03532) [src: Sect.
  III.1, Eq. 8–12; abstract].

### Route C. Unlocalised bursts, the DM distribution
<!-- key: route-c-unlocalised-bursts-the-dm-distribution -->

Without redshifts the likelihood is the distribution of `DM_obs`, integrated
over the redshift distribution and the selection [src: arXiv:2604.03769,
Sect. II, Eq. 7–15]:

```
P(DM_obs | Θ) ∝ ∫_0^{z_max} P_ext(DM_obs − DM_MW | z) P_z(z) P_det(z) S_DM(DM_obs) dz
P_z ∝ R(z)/(1+z) dV_c/dz ,   R = [SFR(z)/SFR(0)]^n
P_det(z) = ∫_{E_min}^∞ Φ(E) S_F(E / K(z)) dE ,   Φ ∝ (E/E_*)^γ exp(−E/E_*)
K(z) = Δν 4π d_L²(z) / (1+z)^(2+α) ,  Δν = 1 GHz ,  E_min = 10^39 erg
lg S_F = 1.7173 [1 − exp(−2.0348 lg F)] − 1.7173
S_DM = −0.7707 (lg DM_obs)² + 4.5601 lg DM_obs − 5.6291
```

`S_F` and `S_DM` are empirical CHIME Catalog 1 selection functions; `S_DM`
peaks near 1000 pc cm⁻³ because DM smearing removes high-DM bursts and RFI
mitigation removes bright low-DM ones. `DM_ISM` from YMW16, `DM_halo` free,
`f = 10^(−0.75)` fixed (freeing it leaves H0 "essentially unchanged"),
`DM_max = 4000` pc cm⁻³, `z_max = 3` [src: same]. On 2124 CHIME Catalog 2
bursts: H0 = 69 (+17/−15), 22%; breaking the degeneracy between H0, `α`
and `E_*` would give 9% [src: abstract].

Two other treatments of bursts without a host redshift:

- **Pseudo-redshifts.** Gao et al. 2024 draw one redshift per CHIME burst
  from its posterior `L(z_i)` under the TNG host and IGM PDFs at fixed H0,
  discarding draws outside the central 94%, and iterate H0 → z → H0 (they
  find the initial H0 matters "only little"; fitting H0 and all 527
  redshifts jointly was judged too costly); 527 CHIME bursts give H0 =
  68.81 ± 0.68, statistical error only, with systematics stated to dominate
  (arXiv:2410.03994) [src: Sect. 4.1.1, 4.1.2, 4.2.1; abstract]. Liu et al.
  quote 22% from 2124 CHIME Catalog 2 bursts with the CHIME selection
  functions (above).
- **Dark sirens with a galaxy catalogue.** Zhao et al. 2022 sum
  `p(DM′ | z_i, H0)` over the DESI Legacy Imaging galaxies in each
  localisation region, with equal or luminosity weights, constant source
  rate and photo-z errors neglected; 12 ASKAP Fly's Eye bursts (270 to 6811
  candidate hosts each) with a BBN prior give H0 = 80.4 (+24.1/−19.4), 68%
  HDI (arXiv:2212.13433) [src: Sect. II.2, III.2, Table 1; abstract].

### Route D. Break `Ω_b h²` with BAO instead of BBN or the CMB
<!-- key: route-d-break-omegab-h2-with-bao-instead-of-bbn -->

FRBs measure `Ω_b H0 f_d`; DESI BAO measures `D_M/r_d`, `D_H/r_d`, with
`r_d` computed "self-consistently from the sampled physical densities" and
no CMB or BBN prior; `Ω_m`, `Ω_b`, H0, `n_s`, `A_s`, `τ`, `f_d` and the FRB
nuisances are sampled with `Cobaya` to `R − 1 < 0.02` [src:
arXiv:2610.15536, Sect. II.3, Table 1]. FRBs alone give H0 = 75.0
(+20.0/−40.0), DESI DR2 alone 90.0 (+30.0/−40.0); together 71.4 (+2.2/−2.5)
and `Ω_b = 0.0503 (+0.0025/−0.0021)`, `r_d = 142.4 ± 4.8` Mpc, flat ΛCDM, 120
localised bursts [src: Table 2, Table 3]. Wang et al. 2025 combine 92
localised bursts with DESI BAO, Pantheon+ and the CMB for `w0wa`, with
the BBN `Ω_b h²` prior where the CMB is absent (arXiv:2501.09260) [src:
abstract, Sect. II].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Forward model or per-burst likelihood
<!-- key: forward-model-or-per-burst-likelihood -->

| | Survey forward model | Per-burst `p(DM | z)` |
|---|---|---|
| Uses | localised and unlocalised bursts, SNR, beam, widths, Poisson count | localised bursts only |
| Extra parameters | `n_sfr`, `γ`, `E_max`, `α`, width and scattering laws | none beyond the DM terms |
| Selection | modelled (DM smearing, beam, threshold, completeness) | not modelled |
| Cost | larger H0 error, compute (grid in H0) | relies on a fair redshift sample |
| Example | arXiv:2208.00819 | arXiv:2610.15536, arXiv:2507.18946, arXiv:2104.04538, arXiv:2108.00581, arXiv:2501.09260 |

James et al. show that fixing the nuisance parameters at their best-fit
values gives "a biased and artificially too-precise" H0, which is the cost
of the simpler likelihood when it fixes rather than fits them (L2). The
host-completeness cut is the cost of the forward model's need for a fair
`(z, DM)` sample; the 2026 framework computes `P(x_opt | x_rad)` for each
burst so that the cut can be dropped (its Sect. 8.1, "Overcoming
completeness cuts in zDM") [src: arXiv:2609.04765, Sect. 2.3, 8.1]. Its authors find current host-selection biases
"likely to be small" [src: same]. From outside zDM, Sharma et al. find the
conditional `p(DM_exgal | z)` biased by ≲ 0.8σ for 10² FRBs and by
possibly > 3σ for 10⁴, so that explicit selection modelling "will be
essential" for the next samples (arXiv:2511.16850) [src: abstract].

### Prior on `F`: narrow or loose
<!-- key: prior-on-f-narrow-or-loose -->

This choice decides the answer. With 125 localised bursts and a loose prior
`F ∈ [0.01, 10]` Jia et al. obtain `F = 3.89 (+1.54/−0.82)` and H0 = 45.74
(+2.74/−3.81), with `Ω_b h² = 0.02237` and `f_IGM = 0.83` fixed; with the
narrow priors of Macquart et al. (`F ∈ [0.011, 0.5]`, `e^μ ∈ [20, 200]`,
`σ_host ∈ [0.2, 2.0]`) `F` piles at 0.45 against its upper bound and H0 =
63.29 (+2.81/−3.77) [src: arXiv:2510.09463, Sect. III.1, Eq. 16–21]. The
evidence prefers the loose prior (`ln B = −6.68`, `ΔAIC = ΔBIC = 13.43`
for the narrow one) [src: Eq. 22]. Their remedy is a shifted log-normal for
the host, `P_host ∝ exp{−[log(DM_host − ℓ) − μ]² / (2σ²)} / (DM_host − ℓ)` for
`DM_host > ℓ` (Eq. 23); `ℓ > 0` moves DM from the IGM to the host and raises
H0; a universal constant `ℓ` "does not work well" because it must stay below
the smallest `(1 + z_i) DM_E,i`; the redshift-dependent variants are
preferred by `ln B` up to 74.28 [src: Sect. III.2, Table 5]. The Zhang et
al. baseline uses the narrow `F` prior (Table 1 above). Liu et al. fix `F`
(Route C). Three analyses, three treatments of the same parameter.

### Analytic or simulated `P_IGM`, `f_d` free or fixed
<!-- key: analytic-or-simulated-pigm-fd-free-or-fixed -->

Zhang et al. vary one ingredient at a time [src: arXiv:2610.15536, Table 3,
Sect. III.3]:

| Variation (FRB + DESI DR2) | H0 |
|---|---|
| Baseline (NE2001, halo 65 ± 15, Macquart `P_IGM`, `f_d` free) | 71.4 (+2.2/−2.5) |
| YMW16 disc | 71.6 (+2.2/−2.4) |
| NE2025 disc | 72.0 ± 2.4 |
| YT2020 halo | 71.7 ± 2.3 |
| Huang25 halo | 70.2 ± 2.1 |
| `f_d = 0.94` fixed | 70.2 (+1.8/−2.0) |
| IllustrisTNG `P_IGM` and `P_host` | 69.9 ± 1.5 |
| IllustrisTNG and `f_d = 0.94` | 68.8 ± 1.0 |

Galactic models move H0 by at most about 0.5σ; the extragalactic DM model
both tightens the error and moves H0 towards the CMB value, "identifying
extragalactic DM modeling as the dominant systematic uncertainty" [src:
abstract, Sect. III.3]. This is the same conclusion as the Xu et al. shifts
in L2, reached on a different sample and with BAO in place of a BBN prior.

The Galactic disc model is not always small: Wang et al. 2025 obtain
H0 = 69.04 (+2.30/−2.07) with NE2001 and 75.61 (+2.23/−2.07) with YMW16,
and trace the difference to a few low-latitude bursts (two with much lower
YMW16 `DM_MW`, about 12 with higher) (arXiv:2501.09260) [src: abstract,
Sect. III]; Zhang et al. find 71.4 against 71.6 (table above), with a BAO
calibration and 120 bursts.

The form of `p(DM_cosmic | z)` itself, from ray tracing through
IllustrisTNG (Konietzka et al. 2025, arXiv:2507.07090): sparse snapshot
sampling in earlier TNG studies misestimates the standard deviation and
higher moments by over 50% [src: abstract]; of six forms, only a modified
normal with power-law tail, `α ≈ 1`, `β ≈ 3.3` (`p_np,31`), fits all
redshifts 0.1–5, while the Macquart `α = β = 3` form and the log-normal
"should be avoided" (the log-normal overestimates the low-DM side and
misses the tail) [src: Sect. IV.2, Eq. 44, Fig. 14]; boxes below 35 h⁻¹Mpc
or baryonic masses below 5×10⁸ h⁻¹M☉ distort the DM by more than 8% [src:
abstract].

### Gaussian or skewed `P_IGM` for cosmography
<!-- key: gaussian-or-skewed-pigm-for-cosmography -->

With 106 localised bursts at `z ≤ 0.7`, the deceleration parameter in
particular depends "sensitively on both the assumed IGM distribution and the
adopted parameter priors" (arXiv:2606.20471) [src: abstract]. The Gaussian
case is the likelihood of Hagstotz et al. (Route B); Konietzka et al. find
the simulated PDF right-skewed and leptokurtic at all `z` (above).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| `Ω_b h²` fixed | 0.02242 (D/H alternative 0.02233 ± 0.00036) | zDM 2022 | arXiv:2208.00819 | Sect. 2.1 |
| `f_d(z = 0)` | 0.844 | zDM 2022 | arXiv:2208.00819 | Sect. 2.1 |
| `f_d` prior | U(0.84, 0.96) | FRB + BAO | arXiv:2610.15536 | Sect. II.2 |
| Scattering at 600 MHz | `log μ_s = 0.7`, `log σ_s = 1.72` (Table 1 lists 1.9) | zDM 2022 | arXiv:2208.00819 | Sect. 2.2.3, Table 1 |
| Widths and scattering, 2026 defaults | `(μ_w, σ_w) = (0, 0.42)`, `(μ_τ, σ_τ) = (0.305, 0.75)`, log10, 600 MHz | zDM 2026 | arXiv:2609.04765 | Sect. 2.3 |
| `n_sfr`, H0 fiducial | 0.73, 67.66 | zDM 2022 | arXiv:2208.00819 | Table 1 |
| `E_min` | 10³⁰ erg (zDM); 10³⁹ erg (unlocalised) | — | arXiv:2208.00819; arXiv:2604.03769 | Sect. 2.2.2; Sect. II |
| CRAFT/ICS low-SNR loss | 6 seen against 18.4 expected; observing time halved | zDM 2022 | arXiv:2208.00819 | Sect. 4.6 |
| CRACO assumed sensitivity | about 4.4 times CRAFT/ICS, 288 MHz | **forecast** | arXiv:2208.00819 | Sect. 3 |
| Host-complete `DM_EG` cuts | 1000 (CRAFT/ICS), 1395 (MeerKAT), 183 (DSA sample) pc cm⁻³ | zDM | arXiv:2609.04765 | Sect. 8.1 |
| Halo DM | 50 fixed (zDM 2022); 65 ± 15 Gaussian (FRB + BAO); free (unlocalised) | — | arXiv:2208.00819; arXiv:2610.15536; arXiv:2604.03769 | Sect. 2.1; II.2; II |
| H0 statistical precision with 500 localised bursts | about 1% (TNG `P_IGM`, `f_d` fixed) | **forecast** | arXiv:2610.15536 | Sect. III.3 |
| H0 statistical precision with about 500 localised bursts | about 1% | **forecast** | arXiv:2410.03994 | abstract |
| LSS scatter of DM | `σ_LSS` ≈ 40 (`z = 0`) to 180 (`z = 1`) pc cm⁻³, Gaussian | per-burst 2021 | arXiv:2104.04538 | Sect. 2.1 |
| IGM scatter of DM | `σ_ΔIGM = 173.8 z^0.4` pc cm⁻³ | ANN 2024 | arXiv:2407.03532 | Sect. III.1, Eq. 11 |
| Shape of `p(DM_cosmic | z)` | modified normal, `α ≈ 1`, `β ≈ 3.3` (±0.5 with binning) | TNG ray tracing | arXiv:2507.07090 | Sect. IV.2 |
| H0, NE2001 against YMW16 disc | 69.04 (+2.30/−2.07) against 75.61 (+2.23/−2.07), 86 and 88 bursts | per-burst 2025 | arXiv:2501.09260 | abstract, Sect. III |
| H0, localised (TNG PDFs) | 69.40 (+2.14/−1.97), 108 bursts | per-burst 2024 | arXiv:2410.03994 | abstract |
| H0, CHIME pseudo-redshifts | 68.81 ± 0.68 (statistical only), 527 bursts | unlocalised 2024 | arXiv:2410.03994 | abstract |
| H0, dark sirens | 80.4 (+24.1/−19.4), 12 ASKAP FE bursts + BBN | unlocalised 2022 | arXiv:2212.13433 | abstract |
| H0, ANN reconstruction | 67.3 ± 6.6, 23 bursts | ANN 2024 | arXiv:2407.03532 | abstract |
| Selection bias on conditional `p(DM | z)` | ≲ 0.8σ (10² FRBs); may exceed 3σ (10⁴) | simulation, **forecast** | arXiv:2511.16850 | abstract |

The two scattering widths for the same CHIME result (1.72 in the text, 1.9 in
Table 1 of arXiv:2208.00819) are both as printed; which one was run was not
established.

## What goes wrong
<!-- key: what-goes-wrong -->

- **A narrow prior on `F` sets H0.** `F` piles against the upper bound 0.5
  of the Macquart priors and cannot be constrained "from the right hand
  side"; with larger `F` H0 falls to about 46 [src: arXiv:2510.09463, Sect.
  III.1]. Test: report the `F` posterior and H0 with the prior widened; a
  posterior on a prior edge is a warning.
- **The host log-normal is the wrong shape.** The shifted log-normal is
  preferred by large evidence ratios and restores agreement with Planck and
  SH0ES (above). Test: refit with a second host form.
- **H0 and the energy function trade off.** Lower `E_max` mimics higher H0
  in the redshift reach and SNR distribution [src: arXiv:2208.00819, Sect.
  3]; in the unlocalised analysis H0, `α` and `E_*` are degenerate enough
  that breaking them would take the error from 22% to 9% [src:
  arXiv:2604.03769, abstract]. Test: show the joint posterior of H0 with
  `E_max` and `α`.
- **Missing low-SNR bursts.** An unexplained deficit of bursts just above
  threshold in CRAFT/ICS [src: arXiv:2208.00819, Sect. 4.6]; corrected
  through observing time, tested in its App. A.1.
- **Host-completeness and reporting bias.** Requiring confident hosts biases
  towards low-redshift, bright hosts, and samples published only with
  confident hosts do not allow the completeness to be estimated; cuts are
  safe only on radio properties, with `P(x_opt | x_rad)` modelled
  accordingly (e.g. a Galactic-latitude cut) [src: arXiv:2609.04765, Sect.
  8.3].
- **One low-DM burst drives a survey.** In zDM 2022, FRB 20190102 (DM 322.2
  at `z = 0.378`) pulls one survey to higher H0 through the cliff effect; a
  single localised burst of one survey gives as much information as 26 or
  28 unlocalised bursts of two others [src: arXiv:2208.00819, Sect. 5.1].
  Test: per-survey and leave-one-out posteriors (its Fig. 7).
- **Selection functions taken from another catalogue.** The unlocalised
  analysis uses CHIME Catalog 1 empirical `S_F` and `S_DM` for Catalog 2
  bursts; whether the functional forms of `P_cos` and `P_host` matter for
  unlocalised bursts is "beyond the scope" of that work [src:
  arXiv:2604.03769, Sect. II].
- **One Galactic model.** NE2001 against YMW16 moves H0 by 6.6 [der: 75.61
  − 69.04] in Wang et al. (a few low-latitude bursts) and by 0.2 in Zhang et
  al. (arXiv:2501.09260; arXiv:2610.15536). Test: refit with both models
  and with a Galactic-latitude cut.
- **A log-normal or `α = β = 3` cosmic PDF.** Both misfit the ray-traced TNG
  distribution (arXiv:2507.07090, Sect. IV.2). Test: refit with the
  modified-normal `p_np,31` or a simulated PDF.
- **Quoting a statistical error as total.** Gao et al. state that their
  ±0.68 from 527 CHIME pseudo-redshifts is statistical only and that
  systematics dominate (arXiv:2410.03994, abstract, Sect. 5.2). The FRB + BAO error shrinks
  from 2.4 to 1.0 when `P_IGM` and `f_d` are fixed to a simulation, with a
  shift of 2.6 [der: 71.4 − 68.8] (Table 3 above). The quoted error is
  conditional on the DM model.

## Reading list
<!-- key: reading-list -->

- Method, forward model: James et al. 2022, arXiv:2208.00819, Sects. 2–3,
  4.6, 5.1 — zDM components and where H0 comes from.
- Method, host uncertainty: James et al. 2026, arXiv:2609.04765, Sects. 2.3
  and 8 — rate equation, completeness cuts, reporting bias.
- Method, unlocalised: Liu et al. 2026, arXiv:2604.03769, Sect. II — DM
  distribution with CHIME selection functions.
- Application, BAO route: Zhang et al. 2026, arXiv:2610.15536 — localised
  likelihood, priors, DM-model variations.
- Critique, priors: Jia et al. 2025, arXiv:2510.09463 — the `F` prior and
  generalised host distributions.
- Critique, PDF form: Lemos et al. 2026, arXiv:2606.20471 (abstract).
- Foundation: Macquart et al. 2020, arXiv:2005.13161 (L2).
- Systematics sizes: Xu et al. 2025, arXiv:2507.18946 (L2).
- Peer, Gaussian per-burst likelihood: Hagstotz et al. 2021,
  arXiv:2104.04538, Sects. 2.1, 3.2.
- Peer, TNG-calibrated PDFs: Wu et al. 2021, arXiv:2108.00581, Sect. 3;
  Gao et al. 2024, arXiv:2410.03994 (also CHIME pseudo-redshifts, Sects.
  4–5).
- Peer, priors and Galactic model: Wang et al. 2025, arXiv:2501.09260,
  Sects. II–III and Table 2 (a compilation of H0 values with their priors).
- Peer, unlocalised with galaxy catalogue: Zhao et al. 2022,
  arXiv:2212.13433, Sect. III.2.
- Peer, data-driven `⟨DM_IGM(z)⟩`: Fortunato et al. 2024, arXiv:2407.03532,
  Sect. III.1.
- Simulation, cosmic PDF: Konietzka et al. 2025, arXiv:2507.07090, Sect.
  IV.2.
- Simulation, selection effects outside zDM: Sharma et al. 2025,
  arXiv:2511.16850 (abstract).

## Not verified
<!-- key: not-verified -->

- Table 1 of arXiv:2208.00819 beyond its first nine rows (energy-function
  and host fiducial values).
- The updated zDM analyses cited in arXiv:2609.04765 (Hoffmann et al. 2025,
  Sharma et al. 2026, James et al. 2026b), and the PATH paper; quoted only as
  cited there.
- The H0 result of arXiv:2604.03769 under freed `F` (stated unchanged, value
  not read) and its Sect. III.
- The redshift-dependent host variants of arXiv:2510.09463 (Sect. III.3) and
  their H0 values.
- Glowacki & Lee 2024, Sect. 5, named in "From".
- Localised samples from CHIME/FRB Outriggers and MeerTRAP as separate H0
  analyses: none found by title search this run; the 2025–2026 per-burst
  analyses above pool bursts from several instruments.
