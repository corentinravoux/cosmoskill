# Tensions and anomalies — open questions and stale claims

Scope: what the next data will decide, and stale tension claims that still circulate with the paper that corrects each.

Snapshot: 2026-10-07

Flags as in `results.md`: `[src]` read this session in the cited paper; `[sec: X]` taken from the reference files of sibling skill X (abbreviations at the top of `results.md`); `[der]` derived here. "ID in sibling" means the paper is cited with its arXiv ID in that sibling and is not in this skill's `sources.tsv`.

## 1. Live controversies
<!-- key: live-controversies -->

### 1.1 Is the local H0 73 or 70, and is the gap physics?
<!-- key: is-the-local-h0-73-or-70-and-is-the-gap-physics -->

**Side A.** SH0ES (73.18 ± 0.88, arXiv:2509.01667) and the community H0 Distance Network (73.50 ± 0.81, arXiv:2510.23823): removing Cepheids or TRGB has minimal effect; 5.0σ to 7.1σ from every early endpoint [sec: h0].

**Side B.** CCHP (70.39 with total error 1.94, arXiv:2408.06153), consistent with ΛCDM "without the need for the inclusion of additional new physics"; statistical reanalyses of the ladder likelihood that lower H0 by 1 to 2.5 km/s/Mpc (arXiv:2601.22215) [sec: h0].

**Where it sits.** Not in stellar distances (the teams agree at about 0.03 mag) but in the SN Ia calibrator subsample, the SN compilation and the selection model of the hosts; the Milky Way step of the prior argument is settled in favour of SH0ES (arXiv:2603.09880), the extragalactic step is not [sec: h0]. Routes with errors below 2 km/s/Mpc split cleanly (ladder high; CMB, BAO + BBN, inverse ladder low); routes with errors of 3 to 5 (lenses, masers, sirens) are compatible with both [sec: h0]. Detail: `cosmo-distance-ladder-h0` `open-questions.md` §1–§4.

### 1.2 One Ω_m mismatch or five anomalies?
<!-- key: one-omegam-mismatch-or-five-anomalies -->

**The fact.** In ΛCDM, DESI DR2 BAO prefer Ω_m = 0.2975 ± 0.0086 and the CMB 0.3145 to 0.330 depending on the experiment; the discrepancy is 1.6σ to 3.7σ (`results.md` §4).

**Reading A: new late-time physics.** The mismatch is resolved by w0wa at 3.1σ with the CMB and 3.0–3.4σ with supernovae, by every supernova sample after recalibration (arXiv:2601.19424, arXiv:2609.05053, arXiv:2605.27221) [sec: de].

**Reading B: one data inconsistency with several names.** The same mismatch is absorbed by τ ≈ 0.09 (arXiv:2504.16932, arXiv:2504.21813), by a negative effective neutrino mass (arXiv:2407.10965, arXiv:2503.14744), by free lensing amplitudes (arXiv:2511.01967), or by Ω_K > 0 (arXiv:2503.14738) [sec: cmb, nu, inf]. The Bayesian evidence for w0wa with DESI + CMB alone is ln B = −0.57 ± 0.26, and the preference with supernovae traces to a ΛCDM tension between DESI and the supernova sample (arXiv:2511.10631) [sec: stat]. No single data set shows the signal above about 2σ; DESI clustering alone, with the bispectrum, is within 1σ of Λ (arXiv:2606.23936) [sec: de].

**What discriminates.** Each reading predicts something else: a high τ is contradicted by reionisation-history data (arXiv:2601.09644) [sec: cmb]; a lensing excess is contradicted by the reconstructions (arXiv:2608.31136) [sec: cmb]; evolving dark energy predicts a specific shape of D_M/D_H at z > 1 and does not help H0 [sec: de]. The honest statement at the snapshot is that the mismatch is real at 2–3σ, that its interpretation is not fixed, and that the listed extensions must not be counted as separate evidence.

### 1.3 Is there an S8 tension, and between what?
<!-- key: is-there-an-s8-tension-and-between-what -->

**Lensing against the CMB.** Reduced, not gone: KiDS-Legacy 0.73σ, DES Y6 cosmic shear 2.0σ, DES Y6 3×2pt 2.6σ in S8 and 1.8σ in full space (arXiv:2503.19441, arXiv:2602.10065, arXiv:2601.14559) [sec: wl]. A 2026 review of the probes exists (Pantos & Perivolaropoulos 2026, arXiv:2602.12238) [sec: wl].

**Among low-redshift probes.** eRASS1 clusters at 0.86 ± 0.01 against KiDS AMICO clusters at 0.74 ± 0.03 and a tSZ cross-correlation at 0.72 ± 0.03: differences of 3.8σ and 4.4σ [der, `results.md` §2.3]. The cluster values rest on lensing mass calibrations from the shear surveys, and the tSZ value on one simulation suite's gas model (`surveys-and-data.md` §2).

**The astrophysical fork.** Strong baryonic feedback (kSZ, X-ray, tSZ, KiDS P(k)) would raise the S8 inferred from small-scale shear; weak feedback (DES Y3 6×2pt) would not [sec: wl, x]. Recalibrating DES Y3 with external IA and baryon information gives 0.832 (arXiv:2512.04209) [sec: wl].

**Open.** Whether DES Y6's 2.6σ survives a common analysis with KiDS-Legacy; whether eRASS1's high value and its γ = 1.19 ± 0.21 are a feature of the data or of the mass calibration; no Stage-IV lensing result exists [sec: wl, cl].

### 1.4 The number-count dipole: above 5σ or about 3σ?
<!-- key: the-number-count-dipole-above-5sigma-or-about -->

**For an anomaly.** CatWISE quasars at 4.9σ (arXiv:2009.14826) and 5.7σ in a Bayesian analysis (arXiv:2212.07733); radio galaxies and quasars jointly at 5.1σ with no shared objects (arXiv:2206.05624); three radio surveys at 5.4σ with overdispersion modelled (arXiv:2509.16732); a clustering analysis that finds no large-scale power other than the dipole (arXiv:2510.23769); the review of the discovering group concludes that the anomaly "poses a serious challenge to FLRW cosmology" (arXiv:2505.23526) [src].

**Against.** Lognormal mocks with clustering, radial selection and the exact mask give 3.3σ to 3.6σ for the same CatWISE catalogue (arXiv:2511.00822); the theoretical expectation depends on source evolution (arXiv:2111.03616; contested by arXiv:2404.07929); the redshift dipole of DESI DR1 quasars gives 358 (+55/−48) km/s while the count dipole of the same catalogues is enhanced, which its authors attribute to footprint effects (arXiv:2608.30914); the CMB aberration measurement gives 384 ± 78 (stat) ± 115 (syst) km/s (arXiv:1303.5087); kSZ limits exclude a ~370 km/s flow at Gpc scales (arXiv:2605.12499) [src; last item sec: pv].

**Where it sits.** In the null model (what large-scale power a ΛCDM quasar sample has on a masked sky) and in the kinematic expectation (how the sample responds to a boost). Not in the measured dipole amplitude, which independent groups reproduce.

**What decides.** Velocity measurements that do not count sources (redshift dipoles from DESI and later spectroscopic surveys, CMB aberration at higher precision); radio samples of order 10⁶ sources from SKA-era surveys; the joint kinematic + residual fits across catalogues with different count slopes (arXiv:2503.02470) [src].

### 1.5 Large-angle CMB anomalies: evidence or flukes?
<!-- key: large-angle-cmb-anomalies-evidence-or-flukes -->

**For.** Four statistics with little mutual correlation have a joint probability ≤ 3 × 10⁻⁸; the authors conclude "that the anomalies should not be dismissed as flukes within ΛCDM" (Jones et al. 2023, arXiv:2310.12859) [src]. The features persist from WMAP to Planck PR4 (arXiv:2406.11543), and the hemispherical asymmetry extends to ℓ ~ 2000 in PR4 (arXiv:2504.05597) [src].

**Against.** Two of the four statistics do not test statistical anisotropy, and a look-elsewhere correction over the tests published in the literature reduces the joint significance to 2σ–3σ; "the current data is consistent with the ΛCDM model and, in particular, with statistical isotropy" (Guth & Namjoo 2026, arXiv:2602.10178) [src]. The Planck collaboration claims no detection of the corresponding anomalies in polarisation (arXiv:1906.02552) [src].

**What decides.** Only independent modes: large-angle E-mode polarisation at the cosmic-variance limit, and three-dimensional tracers of the same scales. Even then Planck expects that detections above 3σ may remain difficult (arXiv:1906.02552) [src].

### 1.6 Is the Cosmicflows-4 bulk flow anomalous?
<!-- key: is-the-cosmicflows-4-bulk-flow-anomalous -->

For: 387 ± 28 km/s at 150 h⁻¹Mpc against an expectation of 139 (arXiv:2302.02028), amplitude confirmed with mock errors (arXiv:2306.11269). Against: a shell analysis with the ΛCDM prediction for the actual sample finds 2.3σ overall and a 3.4σ feature at 120–160 h⁻¹Mpc that falls to 1.6σ without 6dFGS (arXiv:2608.14265); a forward-modelled bulk-flow curve is "fully consistent" with ΛCDM (arXiv:2509.14997) [sec: pv]. Detail: `cosmo-peculiar-velocities` `open-questions.md` §1.

### 1.7 Is the A_L anomaly over?
<!-- key: is-the-al-anomaly-over -->

Yes for ground-based data and PR4 HiLLiPoP (≤ 1σ); not in combinations that keep Planck TT at ℓ > 1000 (CMB-SPA A_2pt = 1.079 ± 0.038, 2.1σ). SPT's position is that the Planck features "may not be cosmological" but that it "cannot make a definitive judgment" (arXiv:2506.20707) [sec: cmb]. The same feature still leaks into Ω_K, Σ0 and the neutrino mass when Planck PR3 is used [sec: cmb, de, inf].

### 1.8 Birefringence: a 4.8σ number nobody claims
<!-- key: birefringence-a-4-8sigma-number-nobody-claims -->

ACT + Planck jointly give β = 0.277° ± 0.057° (arXiv:2608.06480), and its authors claim no detection because the result is conditional on instrumental priors for the polarisation angle [sec: inf]. Decided by absolute angle calibration at the 0.1° level (`cosmo-inflation-primordial`).

### 1.9 JWST: is there anything left for cosmology?
<!-- key: jwst-is-there-anything-left-for-cosmology -->

For a residual problem: three FRESCO galaxies requiring about 50% of baryons in stars (arXiv:2309.02492), now two after one redshift revision (arXiv:2602.03030) [src; the count of two is derived from the two abstracts]. Against: an empirical ΛCDM model reproduces the UV luminosity functions to z = 14 with efficiencies of 2–3% (arXiv:2604.18683) [src]. No measurement at the snapshot requires more baryons than ΛCDM provides. The live questions are astrophysical.

## 2. Theoretical resolutions: status
<!-- key: theoretical-resolutions-status -->

### 2.1 The 2026 systematic comparison
<!-- key: the-2026-systematic-comparison -->

The H0 World Cup (Schöneberg et al. 2026, arXiv:2607.13283, conclusions) [src] compares fourteen models on ACT DR6, SPT-3G D1, Planck, DESI DR2 BAO and Pantheon+, with frequentist and Bayesian tension and model-comparison metrics. In ΛCDM the baseline data give a discrepancy above 5.5σ in M_B.

| Mechanism | Residual tension | Model preference over ΛCDM | Main constraint |
|---|---|---|---|
| Early dark energy and early modified gravity (group E) | about 3σ | strongly favoured | the DES Y6 S8 constraint weakens them, because raising H0 raises S8 |
| Modified recombination (group M), best model | about 4σ | moderate | ACT DR6; lowers Ω_m against late-time data |
| Extra radiation (group R), best model | about 4.5σ | little or none | ACT DR6 damping tail; no longer competitive, unlike in the 2021 comparison |
| Late-time and mixed models (groups L, E + L) | not significantly reduced | none | BAO and uncalibrated supernovae |

Further statements of the same paper [src]: "no model fully resolves the Hubble tension in the full baseline analysis"; without ACT, most models of groups R, M and E reach 3–3.5σ and cold new early dark energy about 2.3σ, so "ACT data are therefore central"; adding CPL dark energy to an early-time model does not help reach the SH0ES calibration (w0, wa shift H0 downward) but models that ease the H0 tension reduce the preference for w0wa; running and running-of-running of the primordial spectrum bring radiation and varying-electron-mass models to 3–3.5σ; BBN constrains groups R, M and E with a dependence on the nuclear-rate code; the models "should be understood primarily as representative of phenomenological mechanisms rather than as complete fundamental theories". The predecessor is the H0 Olympics (Schöneberg et al. 2022, arXiv:2107.10291) [sec: h0].

### 2.2 Early dark energy: where the limits come from
<!-- key: early-dark-energy-where-the-limits-come-from -->

- Bayesian limits: f_EDE < 0.12 (SPT alone) and < 0.070 (SPT + ACT + Planck) at 95%, residual tension 3.6σ; with DESI, f_EDE = 0.055 (+0.024/−0.047) and 2.6σ, "driven by the CMB–DESI discrepancy in ΛCDM" (Khalife et al. 2025, arXiv:2507.23355) [sec: h0].
- Profile likelihood: f_EDE = 0.09 ± 0.03 and H0 = 71.0 ± 1.1 with ACT DR6 + DESI DR2, residual tension about 2σ, with prior-volume effects in the Bayesian limits (Poulin et al. 2025, arXiv:2505.08051) [sec: h0]. Model class reviewed in Poulin, Smith & Karwal 2023 (arXiv:2302.09032) [sec: h0].
- ACT DR6 finds no evidence for early dark energy, extra radiation, varying constants or modified recombination (Calabrese et al. 2025, arXiv:2503.14454) [sec: h0].
- The two faces of the same data: part of the room for early dark energy with DESI comes from the Ω_m mismatch of Section 1.2, not from the ladder.
- Side effects: higher S8 (arXiv:2607.13283) [src]; a structural limit on any model that only shrinks r_d (arXiv:2010.04158) [sec: h0].

### 2.3 Modified recombination
<!-- key: modified-recombination -->

A data-driven m_e(z) history resolves the tension with Planck + ACT and no longer does once DESI DR2 BAO are added, because "raising H0 by modifying recombination generically lowers Ω_m" (Lee & Zhou 2026, arXiv:2606.06495) [src]. SPT + ACT + Planck + DESI show mild preferences for modified recombination or a varying electron mass in a non-flat universe (arXiv:2506.20707) [sec: h0]; in the World Cup the varying-electron-mass model with curvature becomes competitive only with a neutrino-mass prior or the S8 constraint [src].

### 2.4 Late-time models
<!-- key: late-time-models -->

Three independent arguments say no: the ladder constrains M_B, not H0 (arXiv:2103.08723, arXiv:2607.29562); fitting SH0ES, DESI BAO and supernovae together needs a step in M_B at z ~ 0.01 or broken distance duality (arXiv:2602.06293) [sec: h0]; the shape of E(z) from unanchored supernovae and BAO allows ≲ 2% of the ≳ 8% needed, also when early-time physics is added (arXiv:2607.21244) [src]. The DESI w0wa preference lowers H0 [sec: de]. A local void is limited to under 70 Mpc (arXiv:2506.10518) [sec: h0].

### 2.5 What a viable resolution must pass
<!-- key: what-a-viable-resolution-must-pass -->

θ_* at 0.02%; the ACT DR6 and SPT-3G damping tail; DESI BAO in Ω_m and h r_d; the shape of uncalibrated supernovae; BBN abundances; S8 from lensing; an r_d-free H0 (69.0 ± 2.5 from energy densities, arXiv:2511.23432 [src], and the equality-scale values of 66.7 to 67.9 held in `cosmo-distance-ladder-h0`). At the snapshot no published model passes all of them and reaches 73.

## 3. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

| Question | Deciding data | When | Flag |
|---|---|---|---|
| Is the Milky Way anchor right? | Gaia DR4 parallaxes | planned 2 December 2026 | [sec: h0] |
| Is the CCHP–SH0ES gap a calibrator-sample fluctuation? | more JWST hosts with all indicators; a second JWST anchor | ongoing | [sec: h0] |
| Does the Ω_m mismatch grow? | DESI full-survey BAO and full shape | 2027 | [sec: `cosmo-galaxy-clustering`] |
| Is the w0wa preference tied to the low-redshift supernova anchor? | ZTF, DEBASS, TITAN samples in a cosmology analysis | pending | [sec: `cosmo-supernovae`] |
| Is τ ≈ 0.055 or ≈ 0.09? | an independent cosmic-variance-limited low-ℓ EE measurement (LiteBIRD, launch JFY2036); CLASS in the meantime | 2036 or later | [sec: cmb] |
| Does peak smoothing agree with ΛCDM without Planck TT? | further ACT, SPT-3G and Simons Observatory spectra | no dated release held | [sec: cmb] |
| Is S8 from lensing 0.79 or 0.82? | Euclid DR1 lensing | mid-2027, tentative | [sec: wl] |
| Do cluster values converge? | counts cosmology from ACT DR6 (10040 clusters) and SPT-3G (7190 clusters), none published | open | [sec: cl] |
| Is the count dipole kinematic? | redshift dipoles from spectroscopic surveys; radio samples of order 10⁶ sources | DESI later releases; SKA | [src: arXiv:2608.30914, arXiv:2607.25703] |
| Is the 120–160 h⁻¹Mpc flow feature a 6dFGS artefact? | 4HS Fundamental Plane; DESI PV | after 4MOST operations start | [sec: pv] |
| Are the CMB anomalies in polarisation? | large-angle E modes at the cosmic-variance limit | LiteBIRD era | [src: arXiv:1906.02552] |
| Is β real? | absolute polarisation-angle calibration at 0.1° | Simons Observatory, LiteBIRD | [sec: inf] |
| Is any z > 7 galaxy above the baryon limit? | multi-line spectroscopy and MIRI photometry of the massive candidates | ongoing | [src: arXiv:2602.03030] |

No forecast number is given in this table: the forecasts held by the siblings are for single probes and are labelled there.

## 4. Stale claims and their corrections
<!-- key: stale-claims-and-their-corrections -->

| Claim still in circulation | Why it is stale or wrong | Correcting paper | Flag |
|---|---|---|---|
| "The Hubble tension is 4.4σ" or "5σ", unqualified | 2019 and 2022 figures against Planck 2018; the range is now 4.4σ to 7.1σ for SH0ES and H0DN depending on the endpoint | arXiv:2112.04510; arXiv:2510.23823 | [sec: h0] |
| "JWST resolved the Hubble tension" | CCHP's 70.39 has a total error of 1.94 and uses a calibrator subsample; SH0ES with JWST gets 73.18 ± 0.88 | arXiv:2408.06153; arXiv:2509.01667 | [sec: h0] |
| "Planck is the outlier" | SPT-3G alone gives 66.66 ± 0.60; BAO + BBN gives 68.51 ± 0.58 | arXiv:2506.20707; arXiv:2503.14738 | [sec: h0] |
| "Lensing time delays confirm 73 at 2.4%" | with the mass-sheet degeneracy free: 71.6 (+3.9/−3.3) | arXiv:2506.03023 | [sec: h0] |
| "Evolving dark energy relieves the H0 tension" | w0waCDM lowers H0; the ladder mismatch is in M_B | arXiv:2503.14738; arXiv:2607.29562 | [sec: de, h0] |
| "A late-time transition can raise H0" | needs a step in M_B at z ~ 0.01; the E(z) shape allows ≲ 2% | arXiv:2602.06293; arXiv:2607.21244 | [sec: h0; src] |
| "We live in a void that explains it" | void smaller than 70 Mpc; no step in the SN Hubble diagram | arXiv:2506.10518; arXiv:1901.08681 | [sec: h0] |
| "Early dark energy is ruled out" or "solves the tension" | best-performing class, residual about 3σ, penalised by S8; limits depend on Bayesian or profile treatment | arXiv:2607.13283; arXiv:2507.23355; arXiv:2505.08051 | [src; sec: h0] |
| "Extra radiation (N_eff) can ease the tension" | no longer competitive once ACT DR6 is included | arXiv:2607.13283 | [src] |
| "S8 ≈ 0.76, 2–3σ below Planck" | KiDS-1000 and DES Y3 values; KiDS-Legacy is 0.815, DES Y6 0.789–0.798 | arXiv:2503.19441; arXiv:2601.14559 | [sec: wl] |
| "The S8 tension is resolved" | DES Y6 3×2pt is 2.6σ low in S8; cluster and tSZ values span 0.72 to 0.86 | arXiv:2601.14559; `results.md` §2 | [sec: wl] |
| "Clusters prefer low σ8" | eRASS1 0.86 ± 0.01, SPT 0.795 ± 0.029, KiDS 0.74 ± 0.03: name the sample | arXiv:2402.08458; arXiv:2401.02075; arXiv:2507.14285 | [sec: cl] |
| "CMB-lensing tomography gives S8 ≈ 0.73–0.78" | superseded: unWISE 0.810 ± 0.015, DESI LRG 0.775 (+0.019/−0.022) | arXiv:2309.05659; arXiv:2407.04607 | [sec: x] |
| "Planck prefers A_L > 1 at 2.8σ" or "the A_L anomaly is resolved" | PR3 Plik 1.180 ± 0.065; PR4 HiLLiPoP 1.039 ± 0.052; ground data 1.0; CMB-SPA still 2σ | arXiv:2309.10034; arXiv:2506.20707 | [sec: cmb] |
| "Planck shows a closed universe" | the A_L feature; PR4 gives −0.012 ± 0.010; with BAO consistent with flat | arXiv:2002.06892; arXiv:2309.10034 | [sec: cmb, inf] |
| "DESI found evolving dark energy at 4.2σ" | superseded by the supernova recalibration: 3.0σ to 3.4σ; DESI BAO alone 1.7σ | arXiv:2511.07517; arXiv:2601.19424 | [sec: de] |
| "Three supernova samples independently confirm it" | they share the low-redshift anchor | arXiv:2609.05053 | [sec: de] |
| "Cosmology measured a negative neutrino mass" | an effective parameter; 3σ in ΛCDM only; absent in w0waCDM or with free lensing amplitudes | arXiv:2407.10965; arXiv:2511.01967 | [sec: nu] |
| "The quasar dipole violates the cosmological principle at 5σ" | 3.3σ to 3.6σ with clustering-aware mocks; velocity from the DESI redshift dipole agrees with the CMB | arXiv:2511.00822; arXiv:2608.30914 | [src] |
| "The dipole excess is a mask or radio-systematics artefact" | the mask makes it worse; overdispersion is modelled; two populations without shared objects agree | arXiv:2212.07733; arXiv:2509.16732; arXiv:2206.05624 | [src] |
| "The CMB anomalies exclude isotropy at 5σ" | 2σ to 3σ after a look-elsewhere correction | arXiv:2602.10178 | [src] |
| "The Cold Spot is the imprint of a supervoid" | disfavoured by the lensing signal, odds 1:13 to 1:20 | arXiv:2211.16139 | [src] |
| "Cosmicflows-4 shows a 5σ bulk flow" | probability 0.11% with mock errors; 2.3σ full range | arXiv:2306.11269; arXiv:2608.14265 | [sec: pv] |
| "Parity violation detected at 7σ in BOSS" | against Patchy mocks; 0–2.5σ with 8PCF-free statistics; null in the DESI cross-patch analysis | arXiv:2407.03397; arXiv:2508.09133 | [sec: b2p] |
| "Cosmic birefringence is detected" | 4.8σ conditional on angle priors; authors claim no detection | arXiv:2608.06480 | [sec: inf] |
| "JWST galaxies are too massive for ΛCDM" | photometric candidates of 2022; the spectroscopic sample shows no tension; one extreme object was a z = 3.24 interloper | arXiv:2309.02492; arXiv:2602.03030 | [src] |
| "The CosmoVerse white paper gives the current status" | submitted April 2025: it predates SPT-3G D1, DES Y6, H0DN, the supernova recalibrations and the 2026 dipole and anomaly papers; use it as a map of models and probes | Di Valentino et al. 2025, arXiv:2504.01669 | [sec: wl; date src] |

## Not verified
<!-- key: not-verified -->

- Reviews of 2026 seen in a title search and not read: "The Hubble tension: A decade review" (Cai & Wang, cited in `cosmo-distance-ladder-h0`), "Hubble tension: a short review of theoretical explanations", "A Review on Resolving the Hubble Tension via Late-Universe Physics", "Dark Energy in the DESI Era: A Brief Review". Their contents are not represented here.
- The body of the CosmoVerse white paper (arXiv:2504.01669) was not read this session; only its submission date and title were confirmed.
- Whether a successor to the CosmoVerse white paper has been issued: none was found in a date-sorted title search (from 2025-04-01) on 2026-10-10; the search matched title words only.
- The H0 World Cup tables (per-model residual tensions and Bayes factors): only the conclusions and the metrics section were read; the per-group figures above are the rounded values of the conclusions.
- Claims of redshift-dependent ("running") H0, of anisotropic acceleration from supernovae, and of a decelerating universe after age corrections: seen in searches (2024–2026 preprints by one group) and not assessed; the rebuttals of the age-bias claim are cited in `cosmo-supernovae`.
- A number-count dipole from Euclid, Rubin or SPHEREx data: none found.
