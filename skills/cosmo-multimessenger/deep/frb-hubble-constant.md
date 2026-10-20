# H0 from fast radio bursts — cosmo-multimessenger dossier

Scope: how an FRB H0 is built in its three current forms (survey forward
model of `P(z, DM, SNR)`, per-burst `p(DM | z)` of localised bursts, the DM
distribution of unlocalised bursts) and in combination with BAO, with each
model component, prior and completeness cut and the authors' reasons, and
how to choose between them.
Snapshot: 2026-10-19.
From: Glowacki & Lee 2024 review (arXiv:2410.24072), Sect. 5; ASKAP/CRAFT
zDM analyses.

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

### Route D. Break `Ω_b h²` with BAO instead of BBN or the CMB
<!-- key: route-d-break-omegab-h2-with-bao-instead-of-bbn -->

FRBs measure `Ω_b H0 f_d`; DESI BAO measures `D_M/r_d`, `D_H/r_d`, with
`r_d` computed "self-consistently from the sampled physical densities" and
no CMB or BBN prior; `Ω_m`, `Ω_b`, H0, `n_s`, `A_s`, `τ`, `f_d` and the FRB
nuisances are sampled with `Cobaya` to `R − 1 < 0.02` [src:
arXiv:2610.15536, Sect. II.3, Table 1]. FRBs alone give H0 = 75.0
(+20.0/−40.0), DESI DR2 alone 90.0 (+30.0/−40.0); together 71.4 (+2.2/−2.5)
and `Ω_b = 0.0503 (+0.0025/−0.0021)`, `r_d = 142.4 ± 4.8` Mpc, flat ΛCDM, 120
localised bursts [src: Table 2, Table 3].

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
| Example | arXiv:2208.00819 | arXiv:2610.15536, arXiv:2507.18946 |

James et al. show that fixing the nuisance parameters at their best-fit
values gives "a biased and artificially too-precise" H0, which is the cost
of the simpler likelihood when it fixes rather than fits them (L2). The
host-completeness cut is the cost of the forward model's need for a fair
`(z, DM)` sample; the 2026 framework computes `P(x_opt | x_rad)` for each
burst so that the cut can be dropped (its Sect. 8.1, "Overcoming
completeness cuts in zDM") [src: arXiv:2609.04765, Sect. 2.3, 8.1]. Its authors find current host-selection biases
"likely to be small" [src: same].

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

### Gaussian or skewed `P_IGM` for cosmography
<!-- key: gaussian-or-skewed-pigm-for-cosmography -->

With 106 localised bursts at `z ≤ 0.7`, the deceleration parameter in
particular depends "sensitively on both the assumed IGM distribution and the
adopted parameter priors" (arXiv:2606.20471) [src: abstract].

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
- **Quoting a statistical error as total.** The FRB + BAO error shrinks
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
