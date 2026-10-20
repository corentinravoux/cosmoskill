# Galaxy–halo connection — open questions

Scope: live controversies with both sides cited, method debates, what coming
data will decide, and the misconceptions and stale claims that still circulate.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]` body read; `[sec]`
named secondary source; `[der]` derived here. Forecasts are labelled.

## 1. Lensing is low: cosmology or galaxy–halo modelling?
<!-- key: lensing-is-low-cosmology-or-galaxy-halo -->

**The claim.** Clustering-trained models predict a lensing signal around BOSS
CMASS 20–40% above the measurement at Planck 2015 cosmology (arXiv:1611.08606)
[src]; for LOWZ the mismatch is ~35%, independent of halo mass (10^13.3–10^13.9
h⁻¹M_⊙) and radial scale (0.1–60 h⁻¹Mpc), which the authors argue "places
important constraints on the degree to which astrophysical processes (baryonic
effects, assembly bias) can fully explain the effect" (arXiv:2011.02377) [src].
With DES Y3, HSC Y1 and KiDS-1000 the lensing/clustering ratio is A = 0.79 ±
0.03 and 0.84 ± 0.05 at Planck but consistent with 1 at S8 = 0.76
(arXiv:2202.07440) [src].

**Galaxy–halo side.**

- Halo-mass-dependent satellite selection removes the discrepancy below 1
  h⁻¹Mpc, though not above (arXiv:2010.01143) [src].
- In TNG300 the ~30% excess is reproduced by ignoring assembly bias, satellite
  segregation and baryons together (arXiv:2211.01744) [src].
- Extended SHAM fits BOSS clustering and lensing at Planck and at low S8,
  differing mainly in the assembly-bias level, ~20% vs ~10% (arXiv:2305.09637)
  [src].
- Abundance matching calibrated with PAC cross-correlations reproduces CMASS
  lensing with S8 = 0.8294 ± 0.0110 (HSC) (arXiv:2502.09404) [src].
- UNIONS lensing finds no significant effect for CMASS and stresses that large
  scales, not only small ones, decide it (arXiv:2606.23651) [src]: the Planck
  HOD over-predicts ΔΣ by only ~7% after shear-bias correction, yet its joint
  fits sit at S8 = 0.743, set by the large-scale GGL [src: Sect. 7.1; Sect. 7.2,
  Table 3; Sect. 7.3].

**Cosmology side.** Lower S8 reconciles the measurements (arXiv:1611.08606,
arXiv:2202.07440) [src]; but above 5.25 h⁻¹Mpc the Planck and Lensing
predictions differ by at most ~2σ, so "no compelling evidence" exists on
linear scales and the inconsistency is driven by small scales, where the
f_conc treatment of baryons misses the scale dependence of kSZ-based
estimates [src: Sect. 8 of arXiv:2202.07440]; dynamical dark energy of the DESI kind lowers GGL
relative to clustering by up to 7% through distances (arXiv:2508.05746) [src].

**Where it stands.** Recent simulation-based fits with assembly bias give S8 =
0.797 (+0.023, −0.024) (DESI DR1 × DES + KiDS) and 0.791 (+0.020, −0.021) (×
HSC) at CMB-fixed other parameters (arXiv:2512.15962) [src]; KiDS-1000
halo-model S8 = 0.773 (+0.028, −0.030) (arXiv:2210.03110) [src]; GAMA × KiDS
SHAMe S8 = 0.793, 1.7σ from Planck (arXiv:2507.01601) [src]; satellite
kinematics S8 = 0.81 ± 0.05 with "no indication of S8 tension"
(arXiv:2512.14889) [src]; HSC-Y3 × SDSS halo-model 3×2pt S8 = 0.763
(+0.040, −0.036) (arXiv:2304.00704) [src]; UNIONS × CMASS joint HOD +
cosmology fits S8 = 0.743 (arXiv:2606.23651) [src: Sects. 7.2–7.3]. The central
values span 0.74–0.81 [der: range of the values just listed; corrected
2026-10-16 from "0.79–0.81", which omitted KiDS-1000 and the HSC-Y3 and
UNIONS fits], between and below the low lensing cosmology (0.76) and Planck
(0.83) used by Amon et al. The effect is therefore no longer one number:
its size depends on the galaxy–halo model, the scales and the source survey
(KiDS small-scale LOWZ lensing is "much lower" than HSC and DES in
arXiv:2502.09404) [src].

## 2. Is galaxy assembly bias detected?
<!-- key: is-galaxy-assembly-bias-detected -->

| For | Against or null |
|---|---|
| SDSS DR7 clustering favours strong central assembly bias for M_r < −20 and −20.5 (arXiv:1606.07817) [src] | DESI One-Percent LRG, QSO and ELG fits find no evidence (arXiv:2306.06314, arXiv:2306.06319) [src] |
| BOSS CMASS redshift-space 2PCF prefers positive environment-based assembly bias at 3–5σ and rejects the standard HOD (arXiv:2010.04182) [src] | DESI DR1 BGS direct HOD vs density: Q_sat = 0.05 ± 0.14, "in tension with many empirical galaxy formation models" (arXiv:2510.20896) [src] |
| GAMA × KiDS-1000 SHAMe finds strong central and satellite assembly bias (arXiv:2507.01601) [src: Sect. 5.3]; DESI DR2 LRG multiplets are fitted only with environment-based secondary bias (arXiv:2511.15354) [src: Sect. 6.2] | HSC-Y3 × SDSS: S8 unchanged between (2, 3) and (8, 12) h⁻¹Mpc cuts, no assembly-bias signature (arXiv:2304.00704) [src: Sect. VI.2] |
| Hydrodynamical simulations predict it for DESI-like tracers (arXiv:2202.12911) [src] | Basilisk is designed to be insensitive to it rather than to measure it (arXiv:2409.03105) [src] |

Part of the split is statistical: the DESI One-Percent LRG sample is ~10
times smaller than CMASS, which would reduce the CMASS assembly-bias signal
to < 1σ (arXiv:2306.06314) [src: Sect. 6.1].
The halo-level signal is detected with groups split by central colour or local
overdensity (b_relative 0.7–1.4, arXiv:2511.19607) [src]; the galaxy-level
signal remains sample- and estimator-dependent. Detections from redshift-space
clustering are degenerate with velocity bias and satellite profile, which the
null DESI fits also free [der: from the parameter sets listed in
`physics-and-methods.md` section 11].

**Clusters: settled against the original claim.** The redMaPPer 1.5 bias ratio
with 4.4σ in clustering (arXiv:1506.06135) [src] is attributed to projection
effects: 1.02 ± 0.14 with a projection-robust estimator (arXiv:1611.00366),
signal present in mocks with assembly bias erased (arXiv:1905.07557), "not
reflected in the three-dimensional distribution of matter" (arXiv:1702.01682)
[src]. The 1.24 ± 0.02 ceiling is the bias ratio of mock clusters split by
3D dark-matter concentration (auto-correlations above 10 h⁻¹Mpc, matched to
the redMaPPer number density); a membership-distance split retains ~60% less,
1.10 ± 0.02, itself an upper limit; the earlier measurements exceeded 1.24 by
1.5σ and 3.4σ [src: Sect. 1, Sect. 4 of arXiv:1611.00366].

## 3. Conformity and whether halo mass alone sets quenching
<!-- key: conformity-and-whether-halo-mass-alone-sets -->

- One-halo conformity is established since Weinmann et al. 2006
  (arXiv:astro-ph/0509147) [src] and detected at > 3σ in eBOSS
  (arXiv:1910.05095) [src].
- Two-halo (large-scale) conformity: SDSS signal beyond 4 Mpc for low-mass
  centrals that SAM mocks do not reproduce (arXiv:1209.3306) [src], against
  only an upper limit in eBOSS (arXiv:1910.05095) [src].
- At z ~ 0, SDSS centrals cluster almost independently of sSFR, and a
  halo-mass-only V_peak model reproduces both auto- and cross-correlations
  (arXiv:2403.01393) [src]; DESI BGS groups find the quenched fraction of
  centrals set mostly by halo mass (arXiv:2610.20919) [src]. COSMOS-Web instead
  finds quiescent galaxies more clustered by 0.5–1 dex at matched halo mass to
  z = 5, with environmental quenching of low-mass galaxies (arXiv:2606.31978)
  [src]; UniverseMachine finds galaxy assembly correlated "strongly" with halo
  assembly (arXiv:1806.07893) [src]. The disagreement involves different
  redshifts, mass ranges and halo-mass matching; it is open.

## 4. The SHMR at the ends
<!-- key: the-shmr-at-the-ends -->

- Low mass. DESI DR1 BGS finds a slope steepening to 2.08 ± 0.21 for dwarfs and
  scatter rising to 0.68 dex (arXiv:2609.04351) [src]; the PAC analysis of DESI
  finds an upturn of star formation efficiency below ~10¹⁰ h⁻¹M_⊙
  (arXiv:2603.29331) [src]. Whether the two are compatible once mass
  definitions and estimators are matched has not been shown in the papers read.
- High mass. Stellar masses of BCGs from standard photometry are low by factors
  ~2–4, steepening the high-mass SHMR (arXiv:1401.7329) [src]; the review asks
  that studies based on the earlier relation "be re-evaluated" [src: Sect.
  6.5.1 of arXiv:1804.03097].
- Redshift evolution of the peak halo mass: rising to higher z in COSMOS2020
  and multi-epoch abundance matching (arXiv:2203.10895, arXiv:1205.5807) [src];
  UltraVISTA + VIDEO find the stellar-to-halo ratio maximal at z ~ 1
  (arXiv:2610.19030) [src].

## 5. Method debates
<!-- key: method-debates -->

- **Analytic halo model vs simulation-based forward modelling.** The analytic
  model needs non-linear halo bias, exclusion and residual-RSD corrections to
  reach 5–10% (arXiv:1206.6890, arXiv:2011.08858) [src]; a fully numerical
  mock-based test of the standard ΛCDM + halo model on SDSS DR7 fits each
  statistic separately but not w_p, group multiplicity and number density
  together, with a 2.3σ tension for luminous galaxies (Sinha et al. 2018,
  arXiv:1708.04892) [src]. Simulation-based models handle exclusion and halo
  assembly bias automatically but are limited by simulation resolution and
  volume (arXiv:2512.15962) [src: Sect. III.5].
- **Free parameters vs theoretical error.** Freeing assembly-bias and
  phase-space parameters (arXiv:2512.15962) versus a broad error budget
  spanning zero effect (arXiv:2202.07440) [src: Sect. 4]. The first can absorb
  cosmology if the parameters are degenerate with S8; the second inflates
  errors [der].
- **Which halo property.** V_peak with 0.20 dex scatter fits SDSS where other
  proxies fail on satellite fractions (arXiv:1207.2160) [src]; interpolating
  toward peak mass tunes assembly bias (arXiv:1510.05651) [src]; the amplitude
  and sign of assembly bias depend on the halo definition itself
  (arXiv:1705.04327) [src].
- **Physical models.** SAMs applied without recalibration to a common
  simulation scatter far more than earlier comparisons suggested
  (arXiv:1505.04607) [src]; hydrodynamical suites reproduce clustering after
  calibration but with degenerate feedback (arXiv:2309.17075) [src].
- **Small-scale lensing and baryons.** Scale cuts versus explicit baryon
  models: Mahony et al. find the all-scale S8 1.26σ higher than with cuts,
  "against naive expectations" of feedback suppression (arXiv:2507.01601)
  [src]; Amon et al. bracket baryons with f_conc = 0.61–0.84 (arXiv:2202.07440)
  [src: Sect. 4.1].

## 6. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

- DESI BGS groups and lensing at larger volume will test the Q_sat ≈ 0 result
  against empirical models (arXiv:2510.20896) [src].
- Deeper lensing overlaps on DESI lenses decide whether the residual
  large-scale lensing deficit above 1 h⁻¹Mpc (arXiv:2010.01143) [src] persists;
  UNIONS shows large scales already carry the test (arXiv:2606.23651) [src].
- No quantitative forecast for galaxy–halo constraints from Euclid, Rubin LSST
  or DESI DR2 was read; any forecast number must be found and labelled
  **forecast** before use.

## 7. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

| Claim still seen | Correction |
|---|---|
| "Lensing is low proves low S8." | Galaxy–halo models with assembly bias, satellite segregation or selection reproduce the signal at Planck cosmology (arXiv:2211.01744, arXiv:2305.09637, arXiv:2502.09404) [src]; current joint fits give S8 ≈ 0.74–0.81, depending on model, scales and source survey (section 1). |
| "Halo assembly bias was detected in SDSS clusters (Miyatake et al. 2016)." | Projection effects explain the split (arXiv:1611.00366, arXiv:1905.07557, arXiv:1702.01682) [src]. |
| "The halo mass function is universal." | Not at the 5% level; amplitude changes by 20–50% to z = 2.5 (arXiv:0803.2706) [src]; universality depends on the mass definition (arXiv:1507.05627, arXiv:2512.05847) [src]. |
| "Satellites are Poisson." | Sub-Poisson preferred in KiDS-1000 (arXiv:2210.03110) [src]; the central condition alone breaks Poisson statistics [src: Sect. 4.1 of arXiv:2303.08752]. |
| "NFW concentration relations are interchangeable." | Calibrations differ by 16–23% (arXiv:0804.2486) [src]; baryons alter c(M) (arXiv:2610.03544) [src]. |
| "A halo's mass grows as M_vir(z) says." | Much of the apparent growth since z = 1 is pseudo-evolution (arXiv:1207.0816) [src]. |
| "Quiescent galaxies cluster more because their haloes are older." | At z ~ 0 the excess is mainly from satellites; centrals cluster alike (arXiv:2403.01393) [src]. |
| "Stellar mass is the scatter-free tracer of halo mass." | Scatter ~0.2 dex above 10¹² M_⊙ (arXiv:1804.03097) [src], rising to ~0.7 dex for dwarfs (arXiv:2609.04351) [src]. |

## Not verified
<!-- key: not-verified -->

- (Closed 2026-10-16: the 1.24 split definition was read in Zu et al. 2017,
  Sect. 4.)
- Searched 2026-10-16: HSC Y3 × SDSS halo-model cosmology exists
  (arXiv:2304.00704, `results.md` section 5) but is not framed as a
  lensing-is-low test; no DESI DR2 lensing-is-low analysis was found.
