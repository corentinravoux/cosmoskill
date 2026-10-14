# Open questions — CMB × LSS cross-correlations

Scope: live disagreements with both sides cited, tensions between analyses of the same data, method debates, what the next data decide, forecasts, stale claims, and what was not verified.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` from a named secondary source;
`[der]` derived here. Forecasts are marked **forecast**.

## 1. Is the amplitude of structure low at z < 1 in CMB lensing tomography?
<!-- key: is-the-amplitude-of-structure-low-at-z-1-in-cmb -->

**The numbers.** With the same ACT DR6 and Planck PR4 lensing maps:

| Tracer | Amplitude | Distance from the Planck primary-CMB prediction, as stated by the authors |
|---|---|---|
| unWISE (z ≈ 0.6, 1.1) | S_8 = 0.810 ± 0.015 | "fully consistent" (Farren 2023, arXiv:2309.05659) |
| DESI LRG, HEFT | S_8 = 0.775 +0.019/−0.022 | 1.6–2.2σ; amplitude ≃ 5–7% low (Sailer 2024, arXiv:2407.04607) |
| DESI LRG, HEFT | S_8^× = 0.776 +0.019/−0.021 | 2.1σ, lowest bin largest (Kim 2024, arXiv:2407.04606) |
| DESI Legacy galaxies, linear scales | S_8 = 0.765 ± 0.032 | 1.8σ without the first bin (Qu 2024, arXiv:2410.10808) |
| DESI Legacy LRG, P + B, Planck only | S_8 = 0.769 ± 0.020 | ~2.5σ (Verdiani 2025, arXiv:2510.17796) |
| DESI BGS imaging, + BAO | σ_8 = 0.876 +0.051/−0.067 | aligned with CMB-conditioned ΛCDM (Sailer 2025, arXiv:2503.24385) |
| 2MASS and WISE-based, z ≲ 0.3 | S_8 = 0.79 ± 0.06 | "reasonable agreement" (Rubiola 2025, arXiv:2510.09563) |

All [src].

**Reading A: a mild low-redshift deficit.** The LRG-based results all sit 5–7% below the Planck
prediction, and both arXiv:2407.04606 and arXiv:2410.10808 point to their lowest-redshift bin;
arXiv:2407.04606 writes that this "may motivate further CMB lensing tomography analyses at
z < 0.6 to assess the impact of potential systematics or the consistency of the ΛCDM model". The
bispectrum addition slightly increases the tension (arXiv:2510.17796) [src].

**Reading B: tracer-dependent systematics or a fluctuation.** unWISE, which overlaps the same
redshifts, shows no deficit (arXiv:2309.05659); the tomographic BGS analysis at z ≲ 0.4 does not
either (arXiv:2503.24385); the first DESI Legacy bin is in ~2σ tension with the other two bins of
its own analysis (arXiv:2410.10808) [src]. The LRG analyses share one imaging sample and one pair
of lensing maps, so their agreement is not independent confirmation
(`surveys-and-data.md` §5). Each earlier "low" result moved up by ~1σ when reanalysed
(`results.md` §7.1).

**Context from other probes.** Galaxy-lensing S_8 has itself moved up: KiDS-Legacy
0.815 +0.016/−0.021 and DES Y6 3×2pt 0.789 ± 0.012 [sec: `cosmo-weak-lensing` SKILL.md]. The
statement in arXiv:2407.04607 that its result is "in excellent agreement with galaxy lensing
surveys" referred to the 2024 galaxy-lensing values.

**An external claim.** Sabogal 2025 (arXiv:2505.24465) combines the DESI LRG × CMB lensing
likelihood with BAO and supernovae and reports evidence for dynamical dark energy "exceeding
4σ", including in wCDM, independent of the Planck primary CMB [src]. The measurement papers
quote 1.2–2.2σ from Planck ΛCDM for the same spectra (arXiv:2407.04606, arXiv:2407.04607) [src];
the 4σ belongs to the combination with distance data and inherits the BAO–supernova
preferences discussed in `cosmo-dark-energy-modified-gravity`.

**What decides it.** A lensing × DESI spectroscopic-galaxy analysis with DR2 samples, an
independent imaging tracer at z < 0.6, and SPT-3G or Simons Observatory lensing maps on the same
tracers. None was found in a date-sorted search on 2026-10-09.

## 2. How strong is baryonic feedback, as seen by the kSZ?
<!-- key: how-strong-is-baryonic-feedback-as-seen-by-the -->

**For strong feedback (gas pushed well beyond the virial radius).**
- Stacked kSZ on DESI photometric LRGs at 13σ disfavours IllustrisTNG-like gas (Hadzhiyska 2024,
  arXiv:2407.07152); spectroscopic DR2 LRGs at 18σ favour "feedback efficiencies exceeding those
  in the Battaglia profile" (Qu 2026, arXiv:2604.19744) [src].
- Fiducial simulations are disfavoured at > 3σ (Bigwood 2025, arXiv:2510.15822); kSZ is > 8σ from
  fiducial FLAMINGO, with eROSITA gas fractions twice lower than that simulation (Siegel 2025,
  arXiv:2509.10455) [src].
- Lensing-calibrated gas fractions are ≳ 4σ below TNG300 at fixed radius (Hadzhiyska 2025,
  arXiv:2507.14136); low-mass groups hold 0.21 ± 0.06 of the universal baryon fraction within
  the virial radius (Roper 2025, arXiv:2510.12553) [src].
- Matter power suppression of 10 ± 2% at k = 1 h/Mpc from kSZ + eROSITA (Siegel 2025,
  arXiv:2512.02954); shear × tSZ prefers stronger suppression than mild-feedback simulations at
  2–4σ (Pandey 2025, arXiv:2506.07432) [src].
- Velocity-reconstruction amplitudes of 0.2–0.4 relative to a Battaglia-profile halo model
  (`systematics.md` §8) [src].

**Against, or for caution.**
- DES Y3 + Planck PR4 6×2pt with a gas-fraction prior finds weak feedback, in 2.9–3.3σ tension
  with Illustris and 4.7–5.9σ with OWLS AGN T8.7 (Xu 2025, arXiv:2510.25596) [src].
- A model-independent lensing-to-kSZ ratio on DESI DR2 × ACT DR6 × HSC Y3 finds that the
  *fiducial* FLAMINGO run "most closely tracks" the radial gas fraction, with Illustris-1 and
  TNG300-1 bracketing the data (Liu 2026, arXiv:2609.22466) [src]. This contradicts the > 8σ of
  arXiv:2509.10455 on closely related data.
- The first spectroscopic DESI analysis calls its own preference for strong feedback tentative,
  "with limited statistical significance", because a free amplitude was fitted to each simulated
  profile (Ried Guachalla 2025, arXiv:2503.19870) [src].
- Non-linear velocity terms suppress the stacked signal by 10–20% in a way that mimics missing
  gas when the prediction uses ideal velocities (Ondaro-Mallea 2026, arXiv:2607.23339) [src].
- The gas fractions calibrated on pre-eROSITA X-ray groups (HSC-XXL) prefer 5 ± 4% suppression,
  half the kSZ + eROSITA value (arXiv:2512.02954) [src].
- Stronger feedback that fits the kSZ worsens the agreement with X-ray group gas fractions and is
  "only marginally effective" on the tSZ power spectrum and tSZ × lensing offsets, which probe
  higher masses (McCarthy 2024, arXiv:2410.19905) [src].
- The projected-field measurements concluded that "no baryons are missing on large scales"
  (Kusiak 2021, arXiv:2102.01068) [src]: the question is where the gas is, not whether it exists.

**Implication for S_8.** Using the kSZ profile to inform the baryon model moved DES Y3 cosmic
shear to S_8 = 0.823 +0.019/−0.020 (Bigwood 2024, arXiv:2404.06098) [src]. The weak-lensing side
of this debate, with the X-ray and baryonification literature, is in `cosmo-weak-lensing`.

**What decides it.** One analysis that fits kSZ, lensing and X-ray data of the same haloes with
the stacking velocity estimator reproduced in the simulation, and that reports the result with
and without a free amplitude.

## 3. Does the tSZ prefer a low S_8?
<!-- key: does-the-tsz-prefer-a-low-s8 -->

- Shear + shear × y on DES Y3 with ACT DR6: S_8 = 0.811 +0.015/−0.012, consistent with the
  primary CMB (arXiv:2506.07432) [src].
- The compiled ⟨bP_e⟩(z) fitted with FLAMINGO: S_8 = 0.72 ± 0.03 with strong feedback (Salcido
  2026, arXiv:2605.11083) [src].
- DES shear × Planck tSZ with CIB marginalised at the spectrum level: compatible with FLAMINGO
  only for low S_8, the Planck value "strongly disfavoured", independent of the feedback variant
  (Wayland 2026, arXiv:2609.31774) [src].
- KiDS-1000 × y: amplitude σ_8(Ω_m/0.3)^0.2 low by ~2σ (Tröster 2021, arXiv:2109.04458) [src].

The first uses a halo model with free pressure parameters; the second and third compare with one
simulation suite, in which ⟨bP_e⟩ ∝ S_8³ makes a 10% pressure offset look like a 3% S_8 offset
[der, from the scaling in arXiv:2605.11083]. Whether the discrepancy is cosmology, the pressure
of gas in 10¹³–10¹⁴ M⊙ haloes (reduced according to arXiv:2506.07432), non-thermal pressure
(La Posta 2024, arXiv:2412.12081), or residual CIB and radio emission (`systematics.md` §3) is
open. The same offset appears on the cluster side as the hydrostatic mass bias: see
`cosmo-clusters`.

## 4. High-redshift growth and the Quaia contamination question
<!-- key: high-redshift-growth-and-the-quaia -->

- Quaia × Planck: σ_8 = 0.766 ± 0.034, low value driven by the z ≈ 2.1 bin, with "plausible
  arguments" for foreground contamination of the lensing map beyond z ~ 1.5 (Alonso 2023,
  arXiv:2306.17748); "evidence of contamination" at z ~ 1.7 of undetermined origin (Piccirilli
  2024, arXiv:2402.05761) [src].
- Quaia × ACT DR6 + Planck PR4: no evidence for contamination; σ_8 = 0.802 +0.045/−0.057 (Embil
  Villagra 2025, arXiv:2507.08798) [src].
- DESI DR1 spectroscopic quasars × Planck PR4: σ_8 = 0.929 +0.059/−0.074, 1.5σ *above* Planck (de
  Belsunce 2025, arXiv:2506.22416) [src].
- CatNorth × Planck PR4: S_8 = 0.724 +0.058/−0.054 at z > 1.5, attributed to incompleteness or
  foregrounds (Qin 2026, arXiv:2603.09457) [src].

The quasar results scatter by more than their errors in both directions. The quasar samples
differ in purity and selection function, and the spectroscopic one is high, not low. No
measurement currently indicates a growth anomaly at z > 1.5; the amplitude above z ≈ 2.4 is
fixed to 3.3% by the lensing auto-spectrum minus the cross-correlations (Farren 2024,
arXiv:2409.02109) [src].

## 5. ISW from superstructures
<!-- key: isw-from-superstructures -->

Excess: A_ISW ≈ 5.2 ± 1.6 for DES + BOSS supervoids (Kovács 2018, arXiv:1811.07812), 3.6 ± 2.1
at 0.8 < z < 1.2 and a sign change at z > 1.5 for eBOSS quasar supervoids (Kovács 2021,
arXiv:2107.13038) [src]. No excess: 1.64 ± 0.53 with a matched filter (Nadathur 2016,
arXiv:1608.08638); −0.10 ± 0.69 for DESI Legacy voids, "strongly inconsistent with previous
claims" (Hang 2021, arXiv:2105.11936) [src]. Full cross-correlations give 0.96 ± 0.30 (unWISE;
Krolewski 2021, arXiv:2110.13959) and 1.69 ± 0.61 (Quaia; Ghodsi Yengejeh 2026,
arXiv:2607.22461) [src]. A z < 0.03 analysis reports hot voids and an effect ten times the
expected ISW and Rees–Sciama signal with the opposite sign, which the authors attribute to an
unknown process (Hansen 2025, arXiv:2506.08832) [src]; it has no counterpart in the
cross-spectrum measurements above.

The excess lives in stacks on selected structures and not in the estimators that use the whole
field. Planck 2015 could not exclude an ISW origin for the stacked signal (Planck Collaboration
2015, arXiv:1502.01595) [src]. The w0wa models favoured by DESI do not change the predicted ISW
enough to explain the Quaia value (arXiv:2607.22461) [src].

## 6. Lensing imprint of voids
<!-- key: lensing-imprint-of-voids -->

Earlier work reported void lensing profiles below mock predictions. With DESI Legacy LRG voids
and templates matched in sparseness and photometric-redshift error, A_κ = 1.016 ± 0.054 (Sartori
2026, arXiv:2605.19763, a proceeding summarising a 2025 paper) [src]. The earlier DESI Legacy
superstructure analysis found the mocks high by a factor ~1.3 only for the highest-redshift
density peaks (arXiv:2105.11936) [src]. The discrepancy is now attributed to template
construction.

## 7. Primordial non-Gaussianity from cross-correlations
<!-- key: primordial-non-gaussianity-from-cross -->

| Probe | f_NL (local) | Reference |
|---|---|---|
| DESI Legacy LRG × Planck, κg + gg | 24 +20/−21 | arXiv:2412.10279 |
| Quaia × lensing, p = 1 | −20.5 +19.0/−18.1 | arXiv:2504.20992 |
| DESI DR1 QSO × Planck PR4, p = 1.6 | 2 +28/−34 | arXiv:2512.17865 |
| CIB × Planck lensing | 43 ± 23 | arXiv:2605.03783 |
| kSZ velocity × galaxies, DESI Legacy LRG | −180 +61/−86 | arXiv:2511.15701 |
| kSZ velocity, DESI DR2 | 15.9 +34.6/−34.4 | arXiv:2604.04867 |

All [src]. Open points: the value of p for each tracer; how much of the auto-spectrum can be used
before imaging systematics dominate; and whether the kSZ route delivers its promise. The kSZ
velocity field already has lower noise per mode than the galaxy auto-spectrum at
k < 0.004 Mpc⁻¹ (arXiv:2604.04867) [src]. None of these approaches the CMB bispectrum bound; see
`cosmo-inflation-primordial`.

## 8. Method debates
<!-- key: method-debates -->

- **Linear scale cuts or HEFT.** HEFT to k ≈ 0.6 h/Mpc extracts more signal and adds four nuisance
  parameters per bin; the two approaches agree on the LRG data (arXiv:2407.04607) [src]. The open
  point is the prior on higher-order biases and counterterms, which controls projection effects.
- **Mean or best fit.** `systematics.md` §6.
- **Which kSZ velocities.** Linear reconstruction keeps the interpretation simple; machine-learnt
  or non-linear velocities raise S/N (SNR 14–15 in Gong 2026, arXiv:2609.36355) and require
  simulation-based modelling (arXiv:2607.23339) [src].
- **Profile model or ratio.** GNFW and baryonification fits against the model-independent
  ΔΣ-filter ratio (arXiv:2609.22466) [src].
- **Map-level or spectrum-level component separation** for tSZ cross-correlations
  (arXiv:2609.31774, arXiv:2606.28099) [src].
- **Polarisation-only lensing** as the foreground-free reference: possible at 14σ today
  (Ouellette 2026, arXiv:2606.26223) [src].

## 9. Forecasts
<!-- key: forecasts -->

Each row is a **forecast**, not a measurement.

| Quantity | Forecast | Assumed data | Reference |
|---|---|---|---|
| Stacked kSZ S/N | ~50 | ACT, DESI Y3, Rubin | arXiv:2503.19870 [src] |
| Pairwise kSZ, low z | "roughly a factor of two" better precision | DESI BGS DR2 | Hadzhiyska 2025, arXiv:2510.14135 [src] |
| Force-law index | n = 1 excluded at 10σ | "upcoming surveys" | Gallardo 2026, arXiv:2604.14327 [src] |
| Polarised SZ amplitude, τ_rei | constraints tighter by "roughly a factor of 3" | future CMB and galaxy data | Krywonos 2026, arXiv:2607.16071 [src] |
| Baryon calibration for cosmic shear | framework demonstrated on a simulated LSST Year 1 analysis | kSZ + X-ray + lensing | arXiv:2512.02954 [src] |

Forecasts that assume CMB-S4 need rereading: the project lost DOE and NSF support on 9 July 2025
[sec: `cosmo-cmb` SKILL.md].

## 10. Stale claims and misconceptions
<!-- key: stale-claims-and-misconceptions -->

1. *"CMB lensing tomography finds S_8 low at 2–3σ."* True of the 2021 analyses (arXiv:2105.03421:
   0.784 ± 0.015; arXiv:2111.09898: 0.73 ± 0.03). Both were reanalysed by their own groups and
   moved up by ~1σ for identified reasons (arXiv:2309.05659, arXiv:2407.04607) [src].
2. *"Cross-correlations are free of systematics."* The largest shifts in this field came from the
   lensing normalisation, redshift distributions and priors (`systematics.md` §1, §4, §6).
3. *"The Planck lensing map is contaminated at z > 1.5."* Suggested with Quaia in 2023–2024, not
   confirmed with ACT DR6 (arXiv:2507.08798) [src].
4. *"Supervoids show an ISW signal several times ΛCDM."* Not reproduced with matched mocks or a
   matched filter (arXiv:2105.11936, arXiv:1608.08638) [src].
5. *"The lensing signal of voids is low."* Resolved by template calibration in the DESI Legacy
   analysis (arXiv:2605.19763) [src].
6. *"kSZ measures fσ_8"* or *"kSZ velocities give growth."* No fσ_8 has been published from kSZ;
   the amplitude is degenerate with τ (arXiv:2510.14135, arXiv:2604.04867) [src].
7. *"A kSZ amplitude of 0.3 means 70% of the baryons are missing."* b_v is the ratio to a fiducial
   P_ge that includes the HOD; baryons are recovered at 2–3 virial radii (arXiv:2507.14136) [src].
8. *"DESI × ACT kSZ rules out IllustrisTNG."* The spectroscopic Y1 analysis gives PTE = 0.045 for
   TNG with a free amplitude and calls the preference tentative (arXiv:2503.19870); the stronger
   statements need the lensing-calibrated comparisons (arXiv:2510.15822, arXiv:2509.10455) [src].
9. *"The ISW effect is detected at 5σ."* Only in one five-catalogue tomographic combination
   (arXiv:1710.03238); single-tracer detections are 2.8–3.2σ (arXiv:2110.13959,
   arXiv:2607.22461) [src].
10. *"The moving-lens and patchy-screening effects are undetected."* The moving lens has a first
    reported detection at 3.7–4.8σ (Hotinli 2026, arXiv:2605.18938); screening is still
    undetected once lensing is accounted for (arXiv:2506.17379, arXiv:2608.27458) [src].
11. *"ACT DR6 lensing agrees with Planck, therefore galaxy lensing must be wrong."* The lensing
    auto-spectrum weights z ~ 0.5–5 on mostly linear scales; in 2023 it was 1.7–2.1σ above the
    galaxy-lensing surveys reanalysed uniformly (Madhavacheril 2023, arXiv:2304.05203) [src],
    and the galaxy-lensing values have since risen [sec: `cosmo-weak-lensing` SKILL.md].
12. *Quoting 6×2pt as a lensing-only result.* DES Y3 6×2pt S_8 = 0.792 ± 0.012 includes the CMB
    lensing auto-spectrum; the cross-correlations alone gave 0.736 +0.032/−0.028
    (arXiv:2206.10824, arXiv:2203.12440) [src].

## 11. Disagreement with a sibling skill
<!-- key: disagreement-with-a-sibling-skill -->

`cosmo-peculiar-velocities` stated "b_v ≈ 0.3–0.45" for the kSZ velocity bias when this file was
written; it was corrected on 2026-10-09 to 0.2–0.45, the span of the values below together with
0.45 +0.06/−0.05 from ACT DR5 × DESI-LS (arXiv:2506.21657, quoted in that skill). The DESI
DR2 × ACT DR6 paper it cites gives b_v = 0.229 ± 0.022 (90 GHz) and 0.233 ± 0.020 (150 GHz) for
LRGs in its joint fit (arXiv:2604.04867, table of LRG fits) [src]; the photometric analysis gives
0.33 ± 0.03 (arXiv:2511.15701) and the QML analysis an amplitude A = 0.39 ± 0.04 (arXiv:2506.21684) [src]. The
range read at source this session is therefore 0.23–0.39 for LRG samples. Values for ELGs and
quasars were not read.

## 12. Not verified, and leads without a bibliography row
<!-- key: not-verified-and-leads-without-a-bibliography -->

The bibliography was capped at 100 rows. The following papers were returned by a search tool
with their titles this session but have no row; their identifiers are given bare, and nothing in
this skill relies on them.

- 2401.13033, Coulton et al., ACT search for late-time anisotropic screening with unWISE: null
  result; abstract read (τ̄ < 0.033 arcmin² within a 6′ disk at 95% for the blue sample).
- 2206.07773, Carron et al., CMB lensing from Planck PR4 maps: abstract read (reconstruction
  signal-to-noise raised by almost 20%).
- 1905.00426, Lenz et al., large-scale Planck CIB maps: abstract read (~25% of the sky,
  353–857 GHz).
- 2510.27605, Patki et al., E_G-type statistic from kSZ velocities and CMB lensing: abstract
  read; **forecast** S/N ~ 20–55 for ACT or Simons Observatory with DESI.
- 1810.13424, Münchmeyer et al., f_NL from kSZ tomography: abstract read; **forecast**
  σ(f_NL) ~ 0.5 for CMB-S4 with LSST.
- 2204.13436, Bahr-Kalus et al., ISW with the RACS radio survey: abstract read
  (A_ISW = 0.94 +0.42/−0.41).
- 2209.07395, Carron et al., Planck ISW–lensing likelihood: abstract read.
- 2503.00636 and 1808.07445, Simons Observatory science goals and forecasts: titles only.
- 2609.04133 (moving-lens modelling), 2506.17217 (bias-hardened screening estimators),
  2401.13040 (temperature-inversion screening estimator), 2510.20715 (Iskay2 pairwise pipeline),
  2507.07346 (CLASS_SZ II), 2608.04868 (kSZ × CMB lensing for reionisation), 2609.09144
  (baryonification with X-ray gas fractions), 2512.04209 (DES Y3 revisited): titles only.

Not verified at all:

- The kSZ velocity bias for DESI ELGs and quasars, and the per-tracer f_NL values of
  arXiv:2604.04867 beyond its abstract and LRG table.
- The Sunyaev–Zel'dovich results of Planck 2015 on the tSZ–CIB correlation and the Planck y-map
  papers; the first CIB × CMB lensing detections.
- Whether any DES Y6, Euclid, HSC or KiDS-Legacy × CMB lensing cosmology exists outside arXiv
  listings searched with the terms recorded in this skill's research log.
- Blinding status of the kSZ gas-profile analyses.
- The definition of the tension metric behind each "σ from Planck" quoted in §1, and which Planck
  likelihood each uses.
