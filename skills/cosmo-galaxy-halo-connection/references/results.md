# Galaxy–halo connection — results

Scope: measured occupation of haloes by tracer, the stellar-to-halo mass
relation and its scatter, satellite fractions, assembly-bias detections, the
lensing-is-low amplitude and cosmology from clustering plus lensing, with which
values are superseded.
Snapshot: 2026-10-16

Flags: `[src]` read this session in the abstract of the cited paper; `[src:
Sect. n]`, `[src: Table n]` read in the body; `[sec]` from a named secondary
source; `[der]` derived here. Forecasts are labelled.

Every number below is conditional on a cosmology (usually a fixed Planck-like
or WMAP-like one), a halo mass definition and a halo finder; units are as each
paper states them. Compare across rows only after checking those three.

## 1. Occupation of haloes by tracer
<!-- key: occupation-of-haloes-by-tracer -->

| Sample | z | Mean (or typical) halo mass | Satellite fraction | Bias | Model, scales | Reference |
|---|---|---|---|---|---|---|
| SDSS DR7 main, luminosity thresholds | — | M_min rises with L; M_1 ~ 17 M_min over most of the range | rises for redder, fainter galaxies | b(>L) = 1.06 + 0.23 (L/L*)^1.12 | HOD on w_p(r_p), ΛCDM | Zehavi et al. 2011, arXiv:1005.2413 [src] |
| BOSS CMASS, first semester (44 000 galaxies) | 0.4–0.7 | majority central in ~10¹³ M_⊙/h | ~10%, in haloes ~10 times more massive | ~2 | HOD on real- and redshift-space ξ | White et al. 2011, arXiv:1010.4915 [src] |
| eBOSS LRG (> 61 000) | 0.6–0.9 | 2.5 × 10¹³ M_⊙/h | 13 ± 3% | 2.30 ± 0.03 | HOD on small and intermediate scales; σ_log L = 0.19 dex | Zhai et al. 2017, arXiv:1607.05383 [src] |
| eBOSS LRG / ELG / QSO | 0.7–1.1 | 1.9 × 10¹³ / 1.1 × 10¹² / 5 × 10¹² M_⊙/h | — | — | multi-tracer HOD with cross-correlations | Alam et al. 2020, arXiv:1910.05095 [src] |
| DESI One-Percent LRG | 0.4–0.6 | log M_h = 13.40 ± 0.02 | 11 ± 1% | 1.93 (+0.06, −0.04) | AbacusHOD, 0.15 < r < 32 h⁻¹Mpc, Planck 2018 | Yuan et al. 2024, arXiv:2306.06314 [src] |
| DESI One-Percent LRG | 0.6–0.8 | log M_h = 13.24 ± 0.02 | 14 ± 1% | 2.08 ± 0.03 | same | arXiv:2306.06314 [src] |
| DESI One-Percent QSO | 0.8–2.1 | log M_h = 12.65 (+0.09, −0.04) | 3 (+8, −2)% | 2.63 (+0.37, −0.26) | same | arXiv:2306.06314 [src] |
| DESI One-Percent ELG (~270 000) | 0.8–1.6 | log ⟨M_h⟩ ~ 11.9 | — | — | HOD with conformity, down to r_p = 0.04 h⁻¹Mpc | Rocher et al. 2023, arXiv:2306.06319 [src] |
| DESI DR1 QSO × Legacy Surveys DR9 photometric galaxies (PAC) + QSO and LRG auto- and cross-correlations | 0.8–1.0 | Gaussian occupation in halo accretion mass peaking at log(M_acc/h⁻¹M_⊙) = 12.88 ± 0.02, width 0.51 (+0.02, −0.01) | satellite-to-central hosting ratio B = 1.01 ± 0.03: equally likely in centrals and satellites at fixed M_acc | — | N-body + SHMR + stellar-mass incompleteness, 0.1 < r_p < 15 h⁻¹Mpc | Gui et al. 2026, arXiv:2607.21749 [src] |
| DESI DR2 (Y3) LRG multiplets (galaxy pairs to quads) × all LRGs | LRG range | multiplets more biased than single galaxies (more massive haloes) | mock pair fraction ~5% above data, triplets ~1%, quads consistent | — | 25 altmtl mocks with One-Percent HODs fit w_p but under-predict multiplet clustering (r_p w_p averaged over 10–30 Mpc) at a few σ [src: Sect. 6.1]; concentration-based A_c, A_s do not fix it, environment-based B_c = B_s = −0.05 does [src: Sect. 6.2]; α_s from 0.5 to 1.2 and s from −0.3 to 0.3 move multiplets by < 1σ [src: Sect. 6.2] | Wang et al. 2025, arXiv:2511.15354 |

Redshift evolution of DESI LRGs (One-Percent survey, w_p + n(z) only):
satellite fraction rises from ≃ 9% at z ≃ 0.5 to ≃ 11% at z ≃ 0.9 and ~15%
above z = 0.95 at low significance; mean halo mass and bias drop above z =
0.95, read as a physically different sample (stellar-mass incompleteness above
log M* = 11.5, faint-W1 red galaxies, post-starbursts); fixed AbacusSummit
snapshots bias mean halo masses of bins whose mean redshift differs from the
snapshot [src: Sect. 6.3 of arXiv:2306.06314]. The σ of the central transition
increases with redshift and M_1 and α decline [src: Sect. 6.3].

Ordering: mean host mass LRG > QSO > ELG in both the eBOSS and the DESI
analyses above, although QSOs have the highest bias because they sit at higher
redshift [der: from the rows of this table].

## 2. Stellar-to-halo mass relation
<!-- key: stellar-to-halo-mass-relation -->

Review-level statements (Wechsler & Tinker 2018, arXiv:1804.03097) [src]:
galaxy formation efficiency peaks near M_h ~ 10¹² M_⊙, where less than 20% of
the available baryons are in stars today; the scatter in stellar mass at fixed
halo mass is below 0.2 dex above that pivot; below it, stellar mass is a steep
function of halo mass.

| Data | z | Quantity | Value | Model | Reference |
|---|---|---|---|---|---|
| COSMOS lensing + clustering + SMF | 0.2–1 | minimum M_h/M* | ~27 at M* = 4.5 × 10¹⁰ M_⊙, M_h = 1.2 × 10¹² M_⊙; low-mass M_h ∝ M*^0.46 | HOD with central scatter | Leauthaud et al. 2012, arXiv:1104.0928 [src] |
| same | 0.88 → 0.37 | pivot stellar mass | (5.75 ± 0.13) → (3.55 ± 0.17) × 10¹⁰ M_⊙, pivot ratio constant ~27 | same | arXiv:1104.0928 [src] |
| Millennium, multi-epoch AM | 0 → 4 | peak star formation efficiency | 23% at z = 0 to 9% at z = 4; peak halo mass 10^11.8 → 10^12.5 M_⊙ | MEAM | Moster et al. 2013, arXiv:1205.5807 [src] |
| SDSS, Bolshoi SHAM | — | scatter at fixed V_peak | 0.20 ± 0.03 dex | SHAM on w_p + conditional SMF | Reddick et al. 2013, arXiv:1207.2160 [src] |
| SDSS DR7 iHOD | — | scatter σ_log M* | 0.22 below 10¹² M_⊙ to 0.18 at 10¹⁴ M_⊙ | iHOD, clustering + lensing | Zu & Mandelbaum 2015, arXiv:1505.02781 [src]; 0.22 (+0.02, −0.01) at 10¹², 0.18 ± 0.01 at 10¹⁴ [sec: arXiv:1804.03097, Sect. 6.2] |
| BOSS z ~ 0.5 clustering | 0.5 | σ_log M* | 0.18, for log M_h = 12.7–13.7 | SHMR on bias vs stellar mass (Tinker et al. 2017) | [sec: arXiv:1804.03097, Sect. 6.2] |
| X-ray clusters | low z | BCG slope, scatter | M*_BCG ∝ M500^(0.35 ± 0.1), ~0.2 dex; total stellar mass ∝ M500^(0.6 ± 0.1), 0.1 dex | direct | Kravtsov et al. 2018, arXiv:1401.7329 [src] |
| COSMOS2020 | 0.2–5.5 | M_h^peak | ~10¹² M_⊙, moving to higher mass at higher z; satellite fraction falls with z | HOD on w(θ) + SMF | Shuntov et al. 2022, arXiv:2203.10895 [src] |
| DES Y3, log M* ~ 9.6–11.5 | — | Behroozi-form parameters | log M_1 = 11.506 (+0.325, −0.404), log ε = −1.632 (+0.306, −0.181), α = −1.638 (+0.108, −0.099), γ = 0.596 (+0.251, −0.210), δ = 3.810 (+2.045, −1.811); satellite fraction ~5–35% | HOD, w(θ) + γ_t | Zacharegkas et al. 2025, arXiv:2506.22367 [src] |
| DESI DR1 BGS, 12 samples, M* down to < 10⁹ M_⊙ | 0.01–0.2 | ⟨M_h(M*)⟩; SHMR slope; scatter | log⟨M_h⟩ = 12.06 + 0.58 log(M*/10¹¹) + (M*/10¹¹)^0.73; slope 0.32 ± 0.06 above Milky-Way mass, 2.08 ± 0.21 for dwarfs; scatter 0.17 ± 0.02 dex (MW) to 0.68 (+0.21, −0.33) dex (LMC-like) | HOD on w_p, ΔΣ and N_sat | Shao et al. 2026, arXiv:2609.04351 [src] |
| DESI Y1 BGS × DECaLS (PAC), to M* = 10^6.4 M_⊙ | low z | SHMR to M_h ≃ 10⁸ h⁻¹M_⊙ | upturn of the SHMR near 10¹⁰ h⁻¹M_⊙ toward low mass; smallest haloes required below 10^8.80 (3σ) and 10^10.24 h⁻¹M_⊙ (5σ) | SHAM on Jiutian | Xu et al. 2026, arXiv:2603.29331 [src] |
| UltraVISTA + VIDEO, 9.3 deg² | 0.25–4 | stellar-to-halo ratio | peaks at M_h ≈ 10¹² M_⊙, maximum at z ~ 1; satellite fraction rising since z ~ 1 | HOD on w(θ) | Stylianou et al. 2026, arXiv:2610.19030 [src] |

The low-mass slope is where analyses disagree most: DESI DR1 BGS finds a steep
SHMR (slope ~2) for dwarfs with large scatter, while the PAC analysis of the
same survey finds an upturn of star formation efficiency in haloes below ~10¹⁰
h⁻¹M_⊙ (arXiv:2609.04351, arXiv:2603.29331) [src]. The two use different
estimators (HOD on w_p + ΔΣ + N_sat vs SHAM on photometric excess counts) and
are not directly comparable without converting definitions.

## 3. Satellites
<!-- key: satellites -->

| Sample | Quantity | Value | Method | Reference |
|---|---|---|---|---|
| BOSS CMASS, 0.48 < z < 0.55 | central velocity dispersion / DM; satellite velocity / DM | 0.22 (+0.03, −0.04); 0.86 (+0.08, −0.03) | HOD on w_p and redshift-space ξ, 0.1–60 h⁻¹Mpc | Guo et al. 2015, arXiv:1407.4811 [src] |
| DESI One-Percent QSO | central velocity bias α_c | 1.54 (+0.17, −0.08): large central velocities, possibly from QSO redshift errors (line shifts), recent mergers, or degeneracy with f_sat | AbacusHOD, w_p then ξ(r_p, π) above 1 h⁻¹Mpc | arXiv:2306.06314 [src: Sect. 7] |
| DESI One-Percent ELG, strict conformity (satellites only with a central) | α; f_sat; f_1h, ⟨M_h⟩ | α = 0.91 (+0.14, −0.11); f_sat five times smaller than without conformity; the one-halo fraction f_1h and mean halo mass barely change, so they are the model-independent quantities to compare across analyses | mHMQ + conformity, GP emulator pipeline | arXiv:2306.06319 [src: Sect. 7.1] |
| DESI One-Percent ELG | satellite velocity dispersion vs DM; fraction outside R_vir | ~30% larger; 0.5% | HOD with conformity | arXiv:2306.06319 [src] |
| DESI DR1 BGS groups (2.2 million galaxies) | satellite HOD slope α | ~0.75 star-forming, ~1.1 quiescent | self-calibrated group finder | Williams et al. 2026, arXiv:2610.20919 [src] |
| DESI DR1 BGS groups | quenched fraction of centrals | depends mostly on halo mass, nearly independent of stellar mass above 10^10.3 M_⊙/h and 10^12.2 M_⊙/h haloes | same | arXiv:2610.20919 [src] |
| SDSS DR7, Basilisk | satellite orbital anisotropy | mildly radial, as for subhaloes in DM-only runs | satellite kinematics, kurtosis included | Mitra et al. 2024, arXiv:2409.03105 [src] |
| SDSS, satellite kinematics | halo mass of red vs blue centrals | red higher at fixed luminosity; no appreciable difference at fixed M* ≲ 10^10.5 h⁻² M_⊙ | kinematics | More et al. 2011, arXiv:1003.3203 [src] |
| KiDS-1000 bright sample | satellite occupation variance | strong preference for sub-Poisson; reduced χ² improves by 0.18 | CSMF + halo model | Dvornik et al. 2023, arXiv:2210.03110 [src] |

DESI DR1 BGS satellite fractions (HOD with measured N_sat): a plateau over
log M* = 9.6–10.6, 20% above an SDSS HOD result but within 1σ, then a drop
from f_sat = 0.4 at log M* = 9.4 to 0.1 at log M* = 8.0, which TNG50 and EAGLE
(roughly constant below 9.6) do not reproduce; group-catalogue fractions are
"significantly lower", because ~30% of the HOD satellites at log M* = 10.0–10.2
sit in haloes below 10^12.5 h⁻¹M_⊙ against ~10% in the DESI groups [src: Sect.
VI.2 of arXiv:2609.04351].

Satellite fractions of LRG, QSO and DES stellar-mass samples are in sections 1
and 2.

## 4. Assembly bias and conformity detections
<!-- key: assembly-bias-and-conformity-detections -->

| Claim | Data | Value | Status | Reference |
|---|---|---|---|---|
| Galaxy assembly bias in clustering | SDSS DR7 w_p, decorated HOD | M_r < −20 and < −20.5 favour strong central assembly bias (high-concentration haloes more likely to host a central); zero excluded "with high significance"; satellite assembly bias significant for M_r < −19; none for M_r < −21 | stated to supersede earlier standard-HOD fits of these data | Zentner et al. 2019, arXiv:1606.07817 [src] |
| Assembly bias in BOSS CMASS | 2D redshift-space 2PCF, extended HOD | χ²/DoF = 1.35; standard 5-parameter HOD "strongly rejected"; 3–5σ preference for positive environment-based assembly bias | model-dependent; also lowers predicted lensing (section 5) | Yuan et al. 2021, arXiv:2010.04182 [src] |
| No assembly bias for DESI One-Percent LRG/QSO/ELG | redshift-space 2PCF, AbacusHOD | "no evidence" at current precision (LRG, QSO); "no significant change" with concentration or environment (ELG) | consistent with zero | arXiv:2306.06314, arXiv:2306.06319 [src]. The LRG AIC comparison prefers the 8-parameter baseline over concentration (A), environment (B) or satellite-profile (s) extensions; with ~10 times fewer galaxies than CMASS (~600 000) the errors are ~3 times larger, so the CMASS signal of Yuan et al. 2021 would be < 1σ [src: Sect. 6.1, Table 1 of arXiv:2306.06314] |
| Direct HOD vs large-scale density | DESI DR1 BGS groups + lensing, 0.05 < z < 0.2 | satellite assembly-bias parameter Q_sat = 0.05 ± 0.14 | consistent with zero, "in tension with many empirical galaxy formation models" | Shao et al. 2025, arXiv:2510.20896 [src]. Method: Yang et al. DESI groups (> 90% complete and pure above 10¹³ h⁻¹M_⊙ at z < 0.5, not colour-biased), binned by abundance-matched mass; N_gal from group–galaxy cross-correlation, M_h from lensing; δ_g counted in a 5–15 h⁻¹Mpc cylindrical shell of ±3000 km/s and rank-ordered; centrals all above 0.4 L*, so only N_sat tests assembly bias; a "galaxy occupation bias" q absorbs miscentring and the ~0.2 dex scatter of M_h^AM [src: main text, δ_g, q and Q_sat paragraphs] |
| Secondary bias of groups | SDSS group catalogue, w_p at fixed mass | b_relative ~ 1.2 (15% reddest centrals) to ~0.8 (bluest); ~1.4 (densest 15% environments) to ~0.7 (least dense) | detection of halo-level secondary bias using groups as halo proxies | Rodriguez et al. 2025, arXiv:2511.19607 [src] |
| Halo assembly bias in clusters | SDSS redMaPPer, 8648 clusters, 0.1 < z < 0.33, split by member separation | equal M200m ≃ 1.9 × 10¹⁴ h⁻¹M_⊙; bias ratio ~1.5; same-bias hypothesis excluded at 2.5σ (lensing) and 4.4σ (clustering) | **disputed**: attributed to projection effects (rows below) | Miyatake et al. 2016, arXiv:1506.06135 [src] |
| Re-analysis of the above | SDSS redMaPPer, projection-robust R̃_mem | lensing bias ratio 1.02 ± 0.14; mock prediction < 1.10, vs 1.24 maximum for a concentration split | consistent with ΛCDM halo assembly bias | Zu et al. 2017, arXiv:1611.00366 [src] |
| Mock re-analyses | Millennium-based mocks | the split produces bias differences even with assembly bias erased, from line-of-sight interlopers; the apparent signal "is not reflected in the three-dimensional distribution of matter" | methodology cannot claim detection | Sunayama et al. 2019, arXiv:1905.07557; Busch et al. 2017, arXiv:1702.01682 [src] |
| Central clustering vs sSFR | SDSS, 10 < log M* < 11.5 | auto-correlations of centrals show "little dependence on sSFR"; quiescent clustering excess mainly from satellites | little net correlation of halo assembly with central sSFR | Kakos et al. 2024, arXiv:2403.01393 [src] |
| Assembly bias in a stellar-mass-selected sample | GAMA w_p × KiDS-1000 ΔΣ, SHAMe | both f_k parameters positive: "strong assembly bias for both central and satellite galaxies" in mocks built from the best fit; small-scale ΔΣ tightens σ, t_merger and β | model-dependent (SHAMe parameterisation) | arXiv:2507.01601 [src: Sect. 5.3] |
| Quiescent vs star-forming at matched halo mass | COSMOS-Web, z = 0–5 | quiescent galaxies more clustered by at least 0.5–1 dex after matching halo mass with UniverseMachine; one-halo conformity to z ≃ 2 | contrasts with the SDSS central result above (different estimator and sample) | Paquereau et al. 2026, arXiv:2606.31978 [src] |
| Galactic conformity, one-halo | SDSS group catalogue | early-type satellite fraction higher around early-type centrals at fixed halo mass, in all masses | foundation of the term | Weinmann et al. 2006, arXiv:astro-ph/0509147 [src] |
| Conformity, large scale | SDSS DR7, z < 0.03 | for centrals below 10¹⁰ M_⊙ conformity extends beyond 4 Mpc; semi-analytic mocks give much weaker effects | two-halo conformity disputed | Kauffmann et al. 2013, arXiv:1209.3306 [src] |
| One-halo conformity in eBOSS | MTHOD, z = 0.7–1.1 | one-halo conformity at more than 3σ; upper limit on two-halo conformity | — | arXiv:1910.05095 [src] |

## 5. Clustering plus lensing: lensing is low, and cosmology
<!-- key: clustering-plus-lensing-lensing-is-low-and -->

**The discrepancy.**

| Data | Statement | Value | Reference |
|---|---|---|---|
| BOSS CMASS × CFHTLenS + CS82, r < 10 h⁻¹Mpc | predicted ΔΣ from clustering-trained mocks exceeds the measurement | 20–40% too high at Planck 2015 | Leauthaud et al. 2017, arXiv:1611.08606 [src] |
| BOSS LOWZ, M_halo ~ 10^13.3–10^13.9 h⁻¹M_⊙, r = 0.1–60 h⁻¹Mpc | amplitude mismatch, independent of halo mass and radial scale | ~35% at Planck CMB cosmology | Lange et al. 2021, arXiv:2011.02377 [src] |
| BOSS × DES Y3, HSC Y1, KiDS-1000, 0.15 < R < 60 h⁻¹Mpc, Dark Emulator | lensing/clustering scaling A at Planck (S8 = 0.83) | A = 0.79 ± 0.03 (DES+KiDS), 0.84 ± 0.05 (HSC) | Amon et al. 2023, arXiv:2202.07440 [src] |
| same, at "Lensing" cosmology (S8 = 0.76) | A | 0.91 ± 0.04 (DES+KiDS), 0.97 ± 0.06 (HSC); both cosmologies acceptable for R > 5.25 h⁻¹Mpc | arXiv:2202.07440 [src] |
| BOSS LOWZ + CMASS, HOD with halo-mass-dependent selection | small-scale lensing | discrepancy below 1 h⁻¹Mpc "fully resolved"; above 1 h⁻¹Mpc lensing still below prediction | Zu 2021, arXiv:2010.01143 [src] |
| TNG300 mock of BOSS-like galaxies | origin | ~30% over-prediction reproduced by ignoring assembly bias, satellite segregation and baryons | Chaves-Montero et al. 2023, arXiv:2211.01744 [src] |
| BOSS, z = 0.31–0.43, SHAMe on Planck and low-S8 simulations | joint fit | "excellent agreement" in both; assembly bias ~20% (Planck) vs ~10% (low S8) | Contreras et al. 2023, arXiv:2305.09637 [src] |
| BOSS CMASS, AM from PAC with DESI photometry | S8 per source survey | 0.8294 ± 0.0110 (HSC), 0.8073 ± 0.0372 (DES), 0.8189 ± 0.0440 (KiDS); KiDS small-scale LOWZ lensing "much lower" | Luo et al. 2025, arXiv:2502.09404 [src] |
| BOSS CMASS × UNIONS, ~2650 deg² overlap | lensing-is-low | no significant effect; best joint fits with slightly lower amplitude than Planck; large scales matter | Campbell et al. 2026, arXiv:2606.23651 [src] |
| same, clustering-only HOD at Planck 2018 | predicted ΔΣ / measured | ~13% high with the response-calibrated shear, ~7% after the ~6% multiplicative-bias correction [src: Sect. 7.1]; joint HOD + cosmology fits give S8 = 0.743 with or without a baryon-correction model, because large-scale GGL forbids a higher S8; kSZ-calibrated strong feedback under-predicts small-scale GGL further [src: Sect. 7.3]; mean host mass log(M̄_h/h⁻¹M_⊙) = 13.351 (M_200m), 13.330 in the Rockstar definition [src: Sect. 7.4] | arXiv:2606.23651 |
| same, after theoretical corrections for baryons and assembly bias (small scales, DES+KiDS) | A | 0.75 ± 0.04 (Planck), 0.89 ± 0.04 (Lensing cosmology); the corrections lower A further and "cannot resolve" A ≠ 1; full-scale Planck values correspond to a ~3–7σ finding of A ≠ 1 | arXiv:2202.07440 [src: Sect. 7.2] |
| DESI-motivated w0wa vs ΛCDM | GGL relative to clustering | reduced by up to 7%, through distances in the lensing kernel | Heydenreich et al. 2025, arXiv:2508.05746 [src] |

**Cosmology from clustering plus lensing (model, scales and fixed parameters
of each row in its second column).**

| Data | Model, scales | S8 or equivalent | Reference |
|---|---|---|---|
| SDSS DR7 (3 samples, z̄ = 0.11, 0.28, 0.40) | large scales only, flat ΛCDM, n_s and h fixed | σ8 (Ω_m/0.25)^0.57 = 0.80 ± 0.05 | Mandelbaum et al. 2013, arXiv:1207.1120 [src] |
| SDSS abundance + clustering + lensing | CLF + halo model, flat ΛCDM, WMAP7 priors on n_s, h, Ω_b | Ω_m = 0.278 (+0.023, −0.026), σ8 = 0.763 (+0.064, −0.049) (95% CL); non-Poisson satellites give σ8 = 0.744 | Cacciato et al. 2013, arXiv:1207.0503 [src] |
| HSC-Y1 × SDSS, 0.15 < z < 0.7, blinded | Dark Emulator + HOD, ΔΣ from R ≃ 3, w_p from 2 h⁻¹Mpc, flat ΛCDM | S8 = 0.795 (+0.049, −0.042); σ8(Ω_m/0.3)^0.17 = 0.745 (+0.039, −0.031) | Miyatake et al. 2022, arXiv:2111.02419 [src] |
| KiDS-1000 bright + faint samples | CSMF + halo model with non-linear bias, exclusion, baryons, flat ΛCDM | S8 = 0.773 (+0.028, −0.030), Ω_m = 0.290 (+0.021, −0.017) | Dvornik et al. 2023, arXiv:2210.03110 [src] |
| same, checks | 17-parameter model; r_p > 5 h⁻¹Mpc goodness of fit p = 0.19 (no tension with the all-scale fit), but a large-scale-only chain does not converge; Poisson satellites give S8 = 0.951 (rejected) | — | arXiv:2210.03110 [src: Sect. 4.2, 4.4] |
| GAMA × KiDS-1000, stellar-mass selected | SHAMe; fiducial excludes GGL below r_p = 1.4 h⁻¹Mpc | S8 = 0.793 (+0.025, −0.024), 1.7σ from Planck; all-scale S8 1.26σ higher | Mahony et al. 2025, arXiv:2507.01601 [src] |
| DESI DR1 BGS + LRG × DES, KiDS | AbacusSummit HOD with assembly bias; clustering to 0.4, lensing to 2.5 h⁻¹Mpc; other parameters at CMB values | S8 = 0.797 (+0.023, −0.024), Ω_m = 0.292 ± 0.011 | Lange et al. 2025, arXiv:2512.15962 [src] |
| DESI DR1 BGS + LRG × HSC | same, with HSC's preferred photo-z offset | S8 = 0.791 (+0.020, −0.021), Ω_m = 0.300 ± 0.009 | arXiv:2512.15962 [src] |
| HSC-Y3 × SDSS DR11, 3×2pt (ξ±, ΔΣ, w_p), 416 deg², blinded | Dark Emulator + HOD, w_p from 2 and ΔΣ from 3 h⁻¹Mpc, flat prior U(−1, 1) on the source photo-z shift, flat ΛCDM | S8 = 0.763 (+0.040, −0.036); S8′ = σ8(Ω_m/0.3)^0.22 = 0.721 ± 0.028; ~2.5σ from Planck in S8 | Miyatake et al. 2023, arXiv:2304.00704 [src] |
| same, scale-cut test | (4, 6) and (8, 12) h⁻¹Mpc cuts | parameters "almost unchanged" with (8, 12); ΔS8 between (2, 3) and (8, 12) cuts has p ≈ 50% under no assembly bias, while the assembly-bias mocks sit in the tail | arXiv:2304.00704 [src: Sect. VI.2] |
| HSC-Y3 × SDSS, 4 tomographic source bins, ΔΣ from 2 to 70 h⁻¹Mpc | point-mass correction (not an occupation model), flat ΛCDM | S8 = 0.780 (+0.029, −0.030); wCDM 0.756 (+0.038, −0.036) | Zhang et al. 2025, arXiv:2507.01386 [src] |
| DESI DR1 full-shape P(k) + BAO + BBN | perturbative EFT with HOD-informed priors on nuisance parameters, ΛCDM | Ω_m = 0.2994 ± 0.0090, σ8 = 0.836 (+0.024, −0.027): ~4% and 23% tighter than Gaussian priors; projection shifts in w0wa removed | Zhang et al. 2025, arXiv:2504.10407 [src] |
| DESI BGS + LRG × DES Y3, harmonic space | Lagrangian EFT / hybrid EFT bias, IA marginalised (perturbative, not an occupation model) | S8 = 0.850 (+0.042, −0.050) | Chen et al. 2024, arXiv:2407.04795 [src] |
| SDSS DR7, satellite kinematics + luminosity function | Basilisk with baryonification | Ω_m = 0.324 ± 0.012, σ8 = 0.775 ± 0.063, S8 = 0.81 ± 0.05; σ8(Ω_m/0.3)² = 0.91 ± 0.05 | Mitra et al. 2025, arXiv:2512.14889 [src] |

Goodness of fit of the DESI DR1 analysis: χ² = 48.5 for 54 points (DES/KiDS)
and 55.1 for 72 points (HSC); with numerically estimated effective galaxy
degrees of freedom 14.0 and 20.3, p = 0.12 and 0.28, one AbacusSummit cosmology
fitting all lens samples [src: Sect. IV.1 of arXiv:2512.15962]. One S8, Ω_m
for all samples costs Δχ² = 7.0 for 4 (DES/KiDS, p = 0.14) and 3.7 for 6
fewer degrees of freedom (HSC, p = 0.72); the results sit 1.5σ (DES+KiDS) and
1.8σ (HSC) below Planck 2018 in S8; without the HSC photo-z offsets S8 =
0.841 ± 0.020 (a ~2.5σ shift, Δχ² = +7.1), so photo-z calibration would add
~0.019 to σ(S8) [src: Sect. IV.2]. With 8 and 6 h⁻¹Mpc cuts and point-mass
marginalisation the same DESI × lensing data give S8 ≈ 0.65–0.71 with ~0.09
errors (Porredon et al. 2026, as quoted) [sec: Sect. IV.2 of
arXiv:2512.15962]: the non-linear scales carry most of the information.

These S8 values are not directly comparable: they fix different parameters, use
different scale cuts and define S8 with exponent 0.5 except where written. The
Chen et al. analysis is perturbative and belongs with the 2×2-point results of
`cosmo-weak-lensing`; it is listed because its title answers the lensing-is-low
question for DESI lenses.

## 6. What superseded what
<!-- key: what-superseded-what -->

| Quantity | Earlier value or method | Current | Why |
|---|---|---|---|
| HMF fit | Press–Schechter; Sheth–Tormen; Jenkins 2001 "universal" | Tinker 2008 (≲ 5%), then emulators at ~1% (arXiv:1804.05866) and Euclid's sub-per-cent calibration (arXiv:2208.02174) [src] | non-universality and definition dependence |
| SDSS decorated-HOD fits | standard HOD fits to DR7 w_p | Zentner et al. 2019 state that their inferences "supersede previously-published results even in the case of a standard HOD analysis" (arXiv:1606.07817) [src] | improved analysis of the same data |
| Cluster halo assembly bias | bias ratio ~1.5 (arXiv:1506.06135) | 1.02 ± 0.14 (arXiv:1611.00366) [src] | projection effects |
| Lensing-is-low amplitude | 20–40% (arXiv:1611.08606) | A = 0.79–0.84 at Planck with three lensing surveys (arXiv:2202.07440); no significant effect with UNIONS (arXiv:2606.23651) [src] | more lensing data, broader models |
| First DESI HODs | eBOSS LRG/ELG/QSO HODs (arXiv:1607.05383, arXiv:1910.05095) | DESI One-Percent (arXiv:2306.06314, arXiv:2306.06319), then DESI DR1 BGS groups and SHMR (arXiv:2610.20919, arXiv:2609.04351) [src] | new survey |
| High-mass SHMR | abundance matching on standard SDSS photometry | relations from improved photometry, BCG masses higher by ~2–4 (arXiv:1401.7329) [src] | sky subtraction and outer profiles |
| SDSS clustering + lensing S8 | σ8 = 0.763 at WMAP7 priors (arXiv:1207.0503) | simulation-based DESI DR1 S8 ≈ 0.79–0.80 (arXiv:2512.15962) [src] | different parameterisation: compare only after converting |


## Not verified
<!-- key: not-verified -->

- Velocity-bias and satellite-fraction values of the DESI DR1 BGS and LRG
  samples in the full-scale analysis (arXiv:2512.15962) were not read in its
  results tables.
- Searched 2026-10-16: the only DESI DR2 galaxy–halo result found is the
  multiplet test (arXiv:2511.15354); no DR2 HOD fit was found. No Euclid Q1,
  KiDS-Legacy or Rubin DP1 HOD or SHMR paper was found; DES Y6 lensing keeps R
  ≥ 4–6 h⁻¹Mpc and fits no occupation model (arXiv:2601.15175) [src: Sect.
  III, Scale cuts].
- The year-1 HSC and DES lens-sample definitions behind the S8 values were read
  in abstracts only.
