# Coordinator gate log

One entry per sub-skill: checker rerun by the coordinator, `SKILL.md` read,
five numbers of the skill compared with the abstract returned by the arXiv MCP
`get_abstract` at gate time.

## cosmo-supernovae — 2026-10-08 — PASS

Checker: `cosmo-supernovae: 109 sources, 0 problem(s) [arXiv-checked]`.
Flags: 265 `[src]`, 9 `[sec]`/`[der]` across the five reference files.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| Unite: 2884 SNe, Ωm = 0.310 (+0.012/−0.011), 3.3σ, weak Bayesian evidence (arXiv:2609.05053) | "2884 likely type Ia supernovae", "Ωm = 0.310^{+0.012}_{−0.011}", "3.3σ (3.1σ)", "only weak preference" | match |
| DES-Dovekie: Ωm = 0.330 ± 0.015, shift −0.022, 4.2σ → 3.2σ (arXiv:2511.07517) | "Ωm = 0.330 ± 0.015 … changes Ωm by −0.022", "3.2σ, reduced from 4.2σ" | match |
| Union3.1: Ωm = 0.344 (+0.026/−0.025), −0.4σ from Union3; 3.4 / 3.4 / 3.2σ for Union3.1 / Dovekie / Pantheon+ (arXiv:2601.19424) | same values, "3.4σ (was 4.2σ before Dovekie) and 3.2σ (was 2.8σ before our correction to Pantheon+)" | match |
| ZTF SN Ia DR2 not cosmology-grade, sensor non-linearity (arXiv:2509.04073) | "pocket-effect … non-linearities in the photometry of a few percent … preventing ZTF SN Ia DR2 to be used for accurate cosmological inference" | match |
| BayeSN on ZTF: host step intrinsic, not dust (arXiv:2605.06799) | "0.103 ± 0.018 mag (5.6σ) step … strong signal of the existence of an intrinsic dependence" | match |

Gaps the agent declared (kept under "Not verified" in the files): Boyd et al.
2025 DA white-dwarf paper (no arXiv ID found), ZTF DR2.5 release paper, SNLS
5-year sample, Rubin SN papers, YSE and TITAN samples, Unite SN-only wCDM and
w0wa central values, Pantheon+ low-z cut, NIR / twins / SUGAR corrections.

Against the RED baseline: the memory-only sheet gave 2.8 / 3.8 / 4.2σ as the
current SN-sample spread and did not know Unite (September 2026) or Union3.1;
it had the Dovekie arXiv ID and Ωm right.

## cosmo-cmb — 2026-10-08 — PASS

Checker: `cosmo-cmb: 91 sources, 0 problem(s) [arXiv-checked]`.
Flags: 308 `[src]` across the five reference files.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| SPT-3G D1 H₀ = 66.66 ± 0.60; CMB-SPA H₀ = 67.19 ± 0.38, σ₈ = 0.8137 ± 0.0037; 2.8σ CMB vs DESI DR2 (arXiv:2506.20707, v2) | same values; v2 is the version served | match |
| SPT sidelobe-depolarisation model not confirmed by the direct beam measurement (arXiv:2602.06334) | "β_pol = 0.89 ± 0.10 … 1.08 ± 0.10 … 0.90 ± 0.22, indicating minimal sidelobe depolarization … differ by an effective 1.3σ" | match |
| LiteBIRD reformed: one telescope, 12 bands, δr < 0.002 (arXiv:2607.25285) | "a single telescope covers 12 frequency bands … δr < 0.002 (68% C.L.)" | match; launch year JFY2036 is not in the abstract, not checked here |
| CMB + DESI without low-ℓ EE prefers τ = 0.090 ± 0.012 (arXiv:2504.16932) | "DESI BAO, high-ℓ CMB and CMB lensing yields τ = 0.090 ± 0.012" | match |
| SPT-3G D1 lensing amplitude at 2 %; Σmν < 0.072 eV with CMB-SPA + DESI DR2 (arXiv:2608.31136) | "consistent with unity at 2% precision", "Σmν < 0.072 eV (95% C.L.)" | match |

Gaps the agent declared: Simons Observatory data-release status (no SO
cosmology result found), NPIPE low-ℓ transfer function, ACT DR6 beam paper,
ACT-alone parameters from ACT's own Table 5, WMAP9 τ and Planck 2013 values,
other B-mode experiments (POLARBEAR, SPIDER, QUBIC, AliCPT), forecast
σ(τ), σ(N_eff), σ(Σmν).

Against the RED baseline: the memory-only sheet gave CMB-SPA H₀ = 67.24 ± 0.35,
the first-version value; the current version reads 67.19 ± 0.38. It did not
know the August 2026 SPT-3G D1 lensing paper or the LiteBIRD reformation.

## cosmo-galaxy-clustering — 2026-10-08 — PASS after one correction

Checker: `cosmo-galaxy-clustering: 125 sources, 0 problem(s) [arXiv-checked]`.
Flags: 309 `[src]` across the five reference files.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| DR1 FS + DR2 BAO: Ωm = 0.3035 ± 0.0085, h = 0.6876 ± 0.0059, σ8 = 0.822 ± 0.034; w0waCDM 1.4σ; abstract misprints w0 = +0.49 (arXiv:2602.18761) | same ΛCDM values; abstract reads "w0 = 0.49 ± 0.25 and wa = −1.52 ± 0.77 … 1.4σ" | match; the sign misprint is real, the table value −0.49 was not re-read at the gate |
| DESI DR1 full shape: Ωm = 0.2962 ± 0.0095, σ8 = 0.842 ± 0.034 (arXiv:2411.12022) | same | match |
| Simulation-based priors: Ωm = 0.2987 ± 0.0066, H0 = 68.80 ± 0.35, σ8 = 0.766 ± 0.015; 2.2σ / 1.4σ (arXiv:2602.18554) | same | match |
| Full-shape posteriors prior-dominated, shifts up to 6.6σ in w0waCDM (arXiv:2508.11811) | "(2.1σ, 4.1σ, 6.5σ, 6.3σ, 6.6σ) shifts between the maximum likelihood estimate and the Bayesian posterior mean" | match |
| DESI DR2 BAO vs CMB "2.3σ, and 2.2σ after the 2026 Lyα AP update" (arXiv:2607.27410) | "slightly reducing their discrepancy from 2.4σ to 2.2σ" | **compressed two papers' numbers into one sequence**; `results.md` had it right, `SKILL.md` and `open-questions.md` corrected by the coordinator |

Gaps the agent declared: DESI DR2 aggregate BAO precision and tracer-specific
HOD systematics, public date of the full DR2 spectra, per-bin BOSS DR12
consensus values, WiggleZ and eBOSS-ELG numbers, Euclid NISP sample numbers,
final Roman survey definition, SPHEREx f_NL forecast, reference papers for
pycorr / pypower / desilike.

Open item for the hub: the 4MOST project site gives first light on 21 October
2025; the hub's `field-state-2026.md` says 18 October. To be settled at
source before the hub is touched.

## cosmo-lyman-alpha — 2026-10-08 — PASS

Checker: `cosmo-lyman-alpha: 172 sources, 0 problem(s) [arXiv-checked]`.
Flags: 426 `[src]` across the five reference files.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| DESI DR2 Lyα BAO: D_H/r_d = 8.632 ± 0.101, D_M/r_d = 38.99 ± 0.53 (stat + sys), z_eff = 2.33 (arXiv:2503.14739) | "8.632 ± 0.098 ± 0.026 and 38.99 ± 0.52 ± 0.12", 0.65 % isotropic, z_eff = 2.33 | match; the combined errors are the quadrature sums (0.1014, 0.534) |
| DESI DR1 P1D cosmology: Δ²★ = 0.379 ± 0.032, n★ = −2.309 ± 0.019 at 0.009 s/km, z = 3; α_s = 0.0014 ± 0.0041; N_eff = 3.02 ± 0.10; gains 1.18 / 1.27 / 1.90 (arXiv:2601.21432) | same values | match |
| Lyα fσ8 fails mock validation and is excluded in DR2; small scales < 10 h⁻¹Mpc marginalised (arXiv:2607.27411) | "mock studies reveal a significant bias in the inferred growth-rate parameter fσ8, leading us to exclude this measurement", "analytic marginalization over small scales (< 10 h⁻¹Mpc)" | match |
| Quasar tomography: 13 h⁻¹Mpc resolution over 220 deg² (arXiv:2004.01448) | "Stripe 82 field (220 deg²) … resolution is 13 h⁻¹Mpc" | match |
| Void–forest RSD: β = 1.21 ± 0.18 (arXiv:2203.11045) | "β = 1.21 ± 0.18", z = 2.49, 8σ | match |
| DESI DR1 P1D measured with FFT and QMLE (arXiv:2505.09493, arXiv:2505.07974) | FFT paper names the QMLE companion; "consistent with each other" | match |

Gaps the agent declared: no DESI DR2 P1D, no DESI P3D / P× on data and no
DESI tomographic map were found; WEAVE-QSO, 4MOST and PFS Lyα status; public
date of the full DESI DR2; DESI DR1 and eBOSS DR16 bias, β and correlation
coefficients; why the 2026 fuzzy-dark-matter limit is ten times weaker than
the 2021 one; the pixel-weight formula and covariance smoothing; reference
papers for Vega and picca.

Against the RED baseline: the memory-only sheet had the DR2 BAO values and
both DR1 P1D arXiv IDs right, but did not know the DR1 P1D cosmology paper
(January 2026) or the DR2 full-shape AP paper (July 2026), and so gave the
BAO-only distance pair as the current best.

## cosmo-weak-lensing — 2026-10-08 — PASS

Checker: `cosmo-weak-lensing: 192 sources, 0 problem(s) [arXiv-checked]`.
Flags: 246 `[src]` across the five reference files.
Method note from the agent: the arXiv MCP was rate-limited, so abstracts and
date-sorted listings were read from arxiv.org directly; no paper body was
read. Every number in this skill is abstract-level.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| DES Y6 cosmic shear: S8 = 0.798 (+0.014/−0.015) NLA, 0.783 (+0.019/−0.015) TATT; 2.0σ and 2.3σ in S8; IA and baryon choices worth up to 1σ (arXiv:2602.10065) | same values; "1.1σ (1.7σ) full space, 2.0σ (2.3σ) in S8"; "up to 1σ" | match |
| DES Y6 3×2pt: S8 = 0.789 ± 0.012; 1.8σ full space, 2.6σ in S8 (arXiv:2601.14559) | same | match |
| HSC Y3 with DESI clustering redshifts: 0.769 → 0.804 (+0.019/−0.018) (arXiv:2511.18134) | "0.804^{0.019}_{−0.018}, compared to previous … 0.769^{+0.031}_{−0.034}" | match |
| DES Y3 with external IA and baryon calibration: S8 = 0.832 (+0.013/−0.017) (arXiv:2512.04209) | same; "shifts by 1.5σ to higher values" | match |
| UNIONS-3500: non-tomographic, S8 error about ±0.07 (arXiv:2605.13547) | "single tomographic bin … S8 = 0.831^{+0.067}_{−0.078}" | match |

Roman launch (30 August 2026) and the Rubin survey start (30 June 2026) are
sourced in `surveys-and-data.md` to the NASA mission page and to
arXiv:2603.23786; not re-fetched at the gate.

Gaps the agent declared: Planck S8 with its error and the exact
Planck + ACT + SPT S8 that DES Y6 uses; per-bin shear bias m for DES Y3, HSC
Y3 and KiDS-Legacy; ρ-statistic amplitudes; each survey's fiducial Boltzmann
code, non-linear prescription and scale ranges; public location of the UNIONS
and KiDS-Legacy shear catalogues; Rubin DR1 date.

Open items for the hub (`field-state-2026.md`), reported by the agent and to
be settled at source before the hub is edited: HSC Y3 recalibrated is
0.804 (+0.019/−0.018), not 0.805 ± 0.018 (confirmed at this gate); DES Y3
3×2pt is 0.776 ± 0.017, and 0.772 is the optimised-scale cosmic-shear
variant, fiducial 0.759 (not re-read at the gate); "S8 has converged" is too
strong while DES Y6 3×2pt sits 2.6σ from the CMB in S8.

Against the RED baseline: the memory-only sheet had DES Y6 3×2pt and
KiDS-Legacy right, including the 1.8σ / 2.6σ attribution it doubted.

## cosmo-distance-ladder-h0 — 2026-10-08 — PASS after three corrections

Built in two runs: research and six files by the first agent (cut by the
session limit), `SKILL.md` and checker by a second agent from the checkpoint
files, with no new research.
Checker: `cosmo-distance-ladder-h0: 103 sources, 0 problem(s) [arXiv-checked]`.

| Claim in the skill | Source | |
|---|---|---|
| SH0ES with JWST Cepheids and TRGB: 73.18 ± 0.88 (arXiv:2509.01667) | abstract: "55 SNe Ia and gives H0 = 73.18 ± 0.88"; 73.49 ± 0.93 without TRGB | match |
| H0DN baseline 73.50 ± 0.81, 7.1σ from flat ΛCDM (arXiv:2510.23823) | abstract: same | match |
| Megamasers: 71.6 ± 3.7 (stat), five MCP galaxies, Manticore (arXiv:2609.17684) | abstract: "For five of the six … H0 = 71.6 ± 3.7 … statistical" | match |
| Megamasers: low H0, in tension with the ladder (arXiv:2608.06247) | abstract gives no number ("consistent with the CMB … tension … at greater than 2σ"); the 66.9–68.8 range is flagged as read in the body, not re-read at the gate | consistent |
| DESI DR1 FP + TF: 73.7 ± 0.06 ± 1.1, calibrated to SH0ES/Pantheon+ (arXiv:2512.03232) | abstract: same | match |

Corrections by the coordinator:
1. `results.md` said H0DN baseline Hubble-flow tracers were "SN Ia + SBF";
   `physics-and-methods.md` added masers. The vote table of arXiv:2510.23823
   Sect. 2.1.3 puts "Masers in Hubble flow" in the baseline (19 of 32 votes).
   `results.md` corrected.
2. `results.md` said the two megamaser reanalyses read "the same six
   galaxies"; one uses six, the other five. Corrected.
3. `open-questions.md` quoted the DESI 2.8–4.2σ range without saying it has
   been revised; now points to `cosmo-supernovae`.

Gaps the agents declared: SH0ES 2022 b_W, Z_W, M_B^0 and Wesenheit R; a
cosmic-chronometer H0; the CCHP TRGB zero point and its revised-calibration
H0; M_B prior values; H0 anisotropy claims; JWST programme IDs; data URLs.

## Wave 1 repair pass after GREEN — 2026-10-08

One agent closed the gaps listed in `baseline-grading.md` from primary
sources. Checker rerun by the coordinator on the six skills: all exit 0
(cmb 91, galaxy-clustering 126, lyman-alpha 172, weak-lensing 192,
supernovae 109, distance-ladder-h0 103 sources).

| Item | Added | Source as reported by the agent |
|---|---|---|
| DESI P1D ranges | EDR FFT 0.145 ≤ k ≤ 2 Å⁻¹, z = 2.2–3.8; EDR QMLE z = 2.0–3.8, k end points derived from the binning; DR1 FFT 0.0468–2.0 Å⁻¹, to z = 4.2; DR1 QMLE z = 2.0–4.6 with end bins removed | paper bodies of arXiv:2306.06311, 2306.06316, 2505.09493, 2505.07974 |
| Lyα systematics | "Applies to" tag on 22 subsections; referee checklist split into 3D and P1D | file content |
| ACT DR6 alone | H0 = 66.11 ± 0.79, n_s = 0.9666 ± 0.0077 | Table 5 of arXiv:2503.14452, read in the PDF |
| CCHP | 70.39 is TRGB alone; JWST-only TRGB and JAGB values added; no later CCHP Cepheid or combined H0 found | abstract of arXiv:2408.06153 |
| SH0ES 73.18 | anchors stated; NGC 4258-only 72.85 ± 1.30 | body of arXiv:2509.01667 |
| Euclid releases | ERO 23 May 2024; Q1 19 March 2025; Q2 24 June 2026; planned DR1-Foundation 12 Nov 2026, DR1 mid-2027, Q3 2028, DR2 June 2029 | ESA pages |
| DESI w0wa with SNe | 2.8–4.2σ marked "as published", revised 3.2 / 3.4 / 3.4σ | abstract of arXiv:2601.19424 |
| DES-SN5YR total | 1829 | Sect. 2.1 of arXiv:2401.02929 |

None of these additions was re-read by the coordinator. The ACT-alone values
agree with the memory-only baseline sheet.

Open: the DR1 QMLE paper's redshift range implies bins up to z = 4.4, the DR1
cosmology paper quotes 4.2. Flagged in `cosmo-lyman-alpha/references/results.md`
as unresolved; the author of the suite co-authored these papers and can settle it.

## cosmo-dark-energy-modified-gravity — 2026-10-08 — PASS

Checker: `cosmo-dark-energy-modified-gravity: 97 sources, 0 problem(s) [arXiv-checked]`.
Flags: 391 `[src]` across the five reference files.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| DES Y6 all probes + DESI DR2 + CMB: 3.0σ (arXiv:2605.27221) | "w0 = −0.82 ± 0.05, wa = −0.63 (+0.21/−0.18), with a 3.0σ deviation"; 2.6σ without SN | match |
| Phantom crossing: 3.2 % of non-crossing mocks imitate it (arXiv:2506.15091) | "in 3.2% of cases, CPL with phantom crossing not only fits better, but exceeds the real-data χ² improvement" | match |
| μ0 = 0.05 ± 0.22, Σ0 = 0.008 ± 0.045; Planck PR3 Σ0 tension a likelihood artefact (arXiv:2411.12026) | same values; "goes away when using LoLLiPoP+HiLLiPoP likelihoods" | match |
| E_G = 0.36 (+0.06/−0.05) against 0.401 in GR at z = 0.555 (arXiv:2401.12971) | same | match |
| Hu–Sawicki f_R0 < 1.4 × 10⁻⁸ from galaxy morphology (arXiv:2009.08743) | same | match |
| Pantheon+ with DR2: 2.8σ but ln B = −0.66 ± 0.44 (arXiv:2503.14743) | the Bayes factor is not in the abstract | not checked at the gate |

Gaps the agent declared: DESI growth index γ; numerical Planck 2018 μ0 and
Σ0; full w0, wa prior ranges; equations of the thawing, emergent and mirage
classes; Vainshtein and nDGP bounds; which Horndeski models survive
GW170817; early dark energy; no DES Y6 or KiDS-Legacy μ–Σ paper found.

Cross-skill nuance reported and applied: DES-Dovekie is 3.2σ in its own paper
(Planck + ACT + SPT as the CMB) and 3.4σ in the recomputation of
arXiv:2601.19424; `cosmo-supernovae/SKILL.md` now says both.

## cosmo-peculiar-velocities — 2026-10-08 — PASS

Checker: `cosmo-peculiar-velocities: 140 sources, 0 problem(s) [arXiv-checked]`.
Flags: 222 `[src]` across the five reference files. The skill points to the
hub's `pv-surveys.md` and `fsigma8-pv-compilation.md` for the survey
descriptions and the historical fσ8 table and does not copy them; the agent
did not re-read the hub rows.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| DESI DR1 PV: three estimators 0.391, 0.440, 0.483; consensus fσ8(z = 0.07) = 0.4497 ± 0.0548; 675 mocks (arXiv:2512.03230, 2512.03231, 2512.03229, 2512.03228) | 0.391 (+0.080/−0.081); 0.440 (+0.080/−0.096); 0.483 (+0.080/−0.043) stat ± 0.018 sys; consensus 0.4497 ± 0.0548; "675 available mock realizations" | match |
| Field-level σ_u systematic ±0.018; 415 523 redshifts, 76 616 velocities (arXiv:2512.03229) | same | match |
| γ_L = 0.580 ± 0.110 from DR1 PV + full shape | "γ_L = 0.580 (+0.110/−0.110)" (arXiv:2512.03230) | match |
| CF4 shell analysis: 2.3σ overall, window-dependent 3.4σ feature (arXiv:2608.14265) | "dipole and joint deviations of 2.29σ and 2.36σ … 120–160 h⁻¹Mpc … 3.40σ … depends strongly on the survey window" | match |
| TF + SN: S8 = 0.798 ± 0.035; FP unstable under the Malmquist treatment (arXiv:2509.20235) | same; "fundamental plane constraints are instead unstable under the inhomogeneous Malmquist bias treatment" | match |
| ZTF: simulations only, 10 % with DESI DR3 BGS (arXiv:2609.34508) | "σ_fσ8 = (+0.047/−0.048) corresponding to a 10 % error", simulation | match |

Not checked at the gate, body-level claims: the 27–39 % estimator
correlations and the 1.1σ spread in mock units (flagged [der] by the agent);
73 686 FP against 2 929 TF velocities and the discarded TF at z > 0.05;
BGS + TF 0.261 against BGS + FP 0.440.

Gaps the agent declared: bulk-flow amplitudes of Peery 2018 and Duangchan
2025; 4HS sample numbers and Taipan status; ZTF DR2.5 and any WALLABY public
release; the label of the ±4.86 term in the DESI EDR FP H0.

For the author: the agent reads the DESI DR1 estimator spread as 1.1σ given
the measured correlations, and suggests the hub file's "honest scale of
method systematics" wording be tempered. The hub PV files were not edited.

## cosmo-neutrinos-dark-matter — 2026-10-09 — PASS

Built in two runs: research, `results.md` and `physics-and-methods.md` by the
first agent (cut by the session limit); the three other reference files and
`SKILL.md` by a second agent with a 30-call research budget (26 used).
Checker: `cosmo-neutrinos-dark-matter: 100 sources, 0 problem(s) [arXiv-checked]`.
Flags: 341 `[src]` across the five reference files.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| DESI DR2 BAO + CMB: Σmν < 0.0642 eV (95 %), σ = 0.020 eV; Feldman–Cousins 0.053 eV; N_eff = 3.23 (arXiv:2503.14744) | same; N_eff = 3.23 (+0.35/−0.34) at 95 % | match; the skill's ±0.18 is the 68 % equivalent, not printed in the abstract |
| JUNO: normal ordering at ≥ 2.1σ, Bayes factor 10.18, 207 days (arXiv:2609.37895) | "207.2 live days … at least 2.1σ … Bayes factor of 10.18" | match |
| KATRIN: m_ν < 0.45 eV at 90 % CL, 259 days (arXiv:2406.13516) | same | match |
| Tightest limit 0.049 eV is an external reanalysis (arXiv:2601.16165) | "M_ν < 0.049 eV (ΛCDM) and M_ν < 0.077 eV (w0waCDM) at 95 % CL", Ivanov et al. | match |
| BBN + CMB: N_ν = 2.925 ± 0.082 (arXiv:2601.22239) | same | match |
| Simons Observatory forecast σ(Σmν) = 0.03 eV, σ(N_eff) = 0.045 (arXiv:2503.00636) | numbers not in the abstract | not checked at the gate |

Gaps the agents declared: KATRIN final data set, LEGEND-200, Project 8;
Rubin, DESI-II and Spec-S5 forecasts; primordial-helium and stellar-stream
systematics; the 3.5 keV line in microcalorimeter data.

Cross-skill notes from the agent: the ACT P-ACT-LB limit reads 0.082 eV in
the arXiv abstract and 0.089 eV in the revised body (Sect. 6.1.1); `cosmo-cmb`
and this skill both quote 0.089 with that note. The hub digest cites
arXiv:2507.16589 (Σmν = 0.098 eV, 2.7σ in w0waCDM), which neither agent read.

## cosmo-clusters — 2026-10-09 — PASS, with a loss to note

Built in two runs (first agent cut at 23 research calls; second resumed from
the checkpoint files, 31 more calls).
Checker: `cosmo-clusters: 100 sources, 0 problem(s) [arXiv-checked]`.
Flags: 259 `[src]` across the five reference files.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| eRASS1: 5259 clusters, S8 = 0.86 ± 0.01 (arXiv:2402.08458) | same; Ωm = 0.29 (+0.01/−0.02), σ8 = 0.88 ± 0.02 | match |
| SPT: S8 = 0.795 ± 0.029; σ8(Ωm/0.3)^0.25 = 0.805 ± 0.016 (arXiv:2401.02075) | same; 1.1σ from Planck 2018 | match |
| KiDS AMICO: S8 = 0.74 ± 0.03 (arXiv:2507.14285) | same; Ωm = 0.22 ± 0.02, σ8 = 0.86 ± 0.03 | match |
| Planck PSZ2 + DES shear: S8 = 0.791 (arXiv:2509.02068) | "0.791 (+0.023/−0.021)", (1 − b) = 0.844 (+0.055/−0.062) | match |
| DES Y1 clusters: S8 = 0.65 ± 0.04, attributed to lensing-signal modelling (arXiv:2002.11124) | same; "discrepancy resides in our modeling of the weak lensing signal" | match |
| DES Y3 clusters: S8 = 0.864 ± 0.035 (arXiv:2503.13632) | same | match |

Loss: to stay under the 100-source cap introduced on 2026-10-09 the second
agent removed 15 rows the first agent had verified, with their table lines
(Liu2024sc, Migkas2024, Tarrio2026, Klein2024, Zelmer2025, Zelmer2026,
Mazoun2024, Vogt2025, Okabe2025, Chiu2026, Shirasaki2024, Mantz2010IV,
Kleinebreil2024, Garrel2022, Gianfagna2023). The files' "Not verified"
sections name them. The brief now says the caps stop additions and never
justify deleting verified content.

Gaps the agents declared: which mass function each headline analysis adopts;
reference papers for Press–Schechter, Sheth–Tormen, the SZ effect, the
universal pressure profile, redMaPPer; eROSITA beyond eRASS1; Simons
Observatory clusters; CMB-lensing mass calibration after June 2025; blinding
in the eRASS1, SPT and Planck analyses.

## cosmo-cmb-lss-cross-correlations — 2026-10-09 — PASS

Checker: `cosmo-cmb-lss-cross-correlations: 100 sources, 0 problem(s) [arXiv-checked]`.
One run, about 52 of 70 research calls.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| unWISE × ACT DR6 + Planck: S8 = 0.810 ± 0.015, consistent with the primary CMB (arXiv:2309.05659) | same; 0.813 ± 0.021 with ACT alone | match |
| DESI LRG × Planck PR4 and ACT DR6: amplitude 5–7 % below the primary-CMB prediction at about 2σ (arXiv:2407.04607) | "≃ 5–7 % lower … modest (∼2σ)"; S8 = 0.765 ± 0.023 with Planck alone; the combined 0.775 is past the part of the abstract read | consistent |
| kSZ velocity reconstruction, DESI DR2 × ACT DR6: 17.0σ LRG, 20.8σ cumulative; f_NL = 15.9 (+34.6/−34.4) (arXiv:2604.04867) | same | match; b_v = 0.23 ± 0.02 is a body value, not checked |
| Lensing/kSZ ratio: fiducial FLAMINGO tracks the gas distribution best (arXiv:2609.22466) | "the fiducial FLAMINGO run most closely tracks the observed radial gas distribution in both samples" | match |
| tSZ cross-correlations with FLAMINGO: S8 = 0.72 ± 0.03, strong feedback (arXiv:2605.11083) | same | match |
| Moving lens: first detection, 4.8σ (arXiv:2605.18938) | "b_ML = 1.24 ± 0.26 (4.8σ)" | match |

Cross-skill correction: `cosmo-peculiar-velocities/SKILL.md` gave
b_v ≈ 0.3–0.45 while citing the DESI DR2 paper, whose LRG values the
cross-correlation agent read as 0.229 ± 0.022 and 0.233 ± 0.020. The range now
reads 0.2–0.45.

Gaps the agent declared: Planck y-map and tSZ–CIB papers; first CIB × lensing
detections; kSZ velocity bias for DESI ELGs and quasars; release dates and
public locations of most maps; blinding status of the kSZ gas-profile
analyses; about 15 leads listed with bare IDs in `open-questions.md` §12; no
DES Y6, Euclid or DESI DR2 × CMB lensing cosmology found.

## cosmo-beyond-two-point — 2026-10-09 — PASS

Checker: `cosmo-beyond-two-point: 120 sources, 0 problem(s) [arXiv-checked]`.
One run, 48 of 70 research calls. The 100-source cap was passed (120): the
agent reached it before field-level inference and simulation-based inference
and, as the corrected brief says, added what those subtopics needed and
deleted nothing.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| DESI DR1 bispectrum: σ8 up 1.1σ, errors −26 %; w0wa 2.8σ with CMB, 3.1σ with CMB and DES-Dovekie (arXiv:2606.23936) | same; 1.6σ with DES-Dovekie alone | match |
| Parity-odd 4PCF in DESI DR1: 4–10σ in auto, nothing cross-patch (arXiv:2508.09133) | "4–10σ depending on details … cross … no detection … in significant tension" | match |
| SDSS void–galaxy AP/RSD: Ωm = 0.337 (+0.026/−0.029) (arXiv:2205.06258) | same | match |
| BOSS voids: f/b 0.540 ± 0.091, 0.347 ± 0.023 after mock calibration (arXiv:2007.07895) | same | match |
| DES Y3 map-level SBI: S8 = 0.808 ± 0.017 in wCDM (arXiv:2606.11309) | same; Ωm = 0.325 ± 0.024 | match |
| Beyond-2pt challenge: HOD mocks, masked parameters, does not validate error bars (arXiv:2405.02252) | mock challenge with masked parameters confirmed; the error-bar statement is past the part of the abstract read | consistent |

Gaps the agent declared: any DESI void–galaxy AP/RSD cosmology; kNN on survey
data; SBI or initial-condition-sampling cosmology from DESI clustering; older
DES / KiDS / HSC peak, PDF and third-order papers; void ISW; per-paper
blinding status.

## Wave 2 test and repair — 2026-10-09

GREEN on `questions-wave2.md`: 11 of 12 fully answered, 1 partial. Conflicts
and gaps, and what was done about each: `baseline-grading-wave2.md`. Checker
after the repairs: all six wave-2 skills exit 0.

## cosmo-inflation-primordial — 2026-10-09 — PASS

Built in two runs (first agent cut at 27 research calls; second resumed from
the checkpoint, 26 more).
Checker: `cosmo-inflation-primordial: 100 sources, 0 problem(s) [arXiv-checked]`.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| Birefringence, ACT + Planck jointly: β = 0.277° ± 0.057°, 4.8σ, no detection claimed (arXiv:2608.06480) | same; 3.5σ with dust mitigation; "unresolved systematics … must be understood before we can draw strong cosmological conclusions" | match |
| Planck PR4 f_NL: local −0.1 ± 5.0, equilateral 6 ± 46, orthogonal −8 ± 21 (arXiv:2504.00884) | same | match |
| BK18: r_0.05 < 0.036 at 95 % (arXiv:2110.00483) | same | match |
| DESI DR1 features: a hint at fixed Planck cosmology that vanishes when cosmology varies (arXiv:2610.10530) | A_lin < 0.033, A_log < 0.035 marginalised; tighter at fixed Planck 2018 cosmology "but in this case we also find a …" (abstract cut there) | consistent |
| SO with six SATs: σ(r) = 1.2 × 10⁻³, forecast (arXiv:2512.15833) | same, with ℓ_knee = 50 and 70 % delensing | match |
| DESI DR1 f_NL = −3.6 (+9.0/−9.1), 1 631 716 LRGs and 1 189 129 quasars (arXiv:2411.17623) | same | match |

Not checked at the gate: Ω_K = +0.0023 ± 0.0011 for DESI DR2 + CMB
(arXiv:2503.14738, body).

Gaps the agents declared: pre-reformation LiteBIRD δr and launch date at
source; Simons Observatory status beyond forecasts; BK24; ACT
correlated-isocurvature limits; Planck feature limits per template; f_NL
convention conversion; other B-mode experiments (AliCPT, CLASS, POLARBEAR);
twelve identified papers left out by the 100-row cap.

## cosmo-statistics-inference — 2026-10-09 — PASS

Checker: `cosmo-statistics-inference: 100 sources, 0 problem(s) [arXiv-checked]`.
One run, 50 of 70 research calls (an earlier attempt was stopped with the
session before writing anything).

| Claim in the skill | arXiv abstract | |
|---|---|---|
| DESI DR2 + Planck: 3.1σ by Δχ² but ln B = −0.57 ± 0.26 (arXiv:2511.10631) | "Bayesian evidence modestly favours ΛCDM (ln B = −0.57 ± 0.26), in contrast to the collaboration's 3.1σ" | match |
| Profile likelihood: Wilks holds for ΛCDM, Feldman–Cousins needed for Σmν, doubtful for w0 (arXiv:2408.07700) | "correct coverage" for ΛCDM; "boundary-corrected or Feldman-Cousins" for Σmν; "indication of a violation of the assumptions" for w0CDM | match |
| SBI inflates variance at least as much as a mock covariance (arXiv:2412.02311) | "neither methods circumvent the issues of covariance es[timation]" (abstract cut) | consistent |
| Passing coverage is not validation (arXiv:2605.00980) | title "Coverage is not enough"; coverage "probe[s] calibration only in an averaged sense" | match |
| MultiNest: narrower intervals, inconsistent evidences on the DES Y1 likelihood (arXiv:2202.08233) | "inconsistent estimates of the Bayesian evidence and somewhat narrower parameter credible intervals than … PolyChord" | match |
| Fisher underestimates w0–wa errors from geometrical probes by 30–70 % (arXiv:1205.3984) | same | match |

Cross-skill notes from the agent, checked by the coordinator:
- "0.053 eV" in `cosmo-neutrinos-dark-matter`: its `results.md` carries both
  the Feldman–Cousins 95 % limit < 0.053 eV (Table 3) and an effective-mass
  width σ = 0.053 eV, each sourced to arXiv:2503.14744. The abstract gives only
  the first. No edit; the coincidence is worth knowing.
- `ln B = −0.66 ± 0.44` in the dark-energy skill is a body value of
  arXiv:2503.14743, not checked at any gate.

Gaps the agent declared: HSC Y3 practice; SPT-3G D1 likelihood, covariance
and sampler; Planck 2018 / PR4 likelihood papers; any Euclid
inference-pipeline paper; twelve 2025–2026 leads listed by title only.

Tooling: `scripts/fetch_abstracts.py` added to the hub (prints first author,
title and abstract for arXiv IDs), replacing a scratch script lost at the
session restart.

## cosmo-simulations-mocks — 2026-10-09 — PASS

Checker: `cosmo-simulations-mocks: 100 sources, 0 problem(s) [arXiv-checked]`.
One run, 32 of 70 research calls.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| N-body codes agree on P(k) to 1 % at k ≤ 1 h/Mpc and 3 % at k ≤ 10 at standard settings (arXiv:1503.05920) | same, for Ramses, Pkdgrav3 and Gadget3 | match |
| COLA with 40 steps: P(k) within 1 % at k ≲ 1 h/Mpc, halo mass function within 5 % (arXiv:1509.04685) | same; halo bias within 2 % for k ≲ 0.7 h/Mpc | match |
| Baryonic suppression from data: 10 ± 2 % at k = 1 h/Mpc (kSZ + eROSITA), 5 ± 4 % (HSC-XXL) (arXiv:2512.02954) | same | match |
| Manticore-Local on 2M++: no large local underdensity (arXiv:2505.10682) | "we find no evidence for a large local underdensity" | match |
| Manticore-Deep: (4 h⁻¹Gpc)³ at about 4 Mpc/h (arXiv:2606.10020) | same, to z ≈ 0.7, five redshift surveys | match |
| Flagship 2: four trillion particles, light-cone to z = 3 (arXiv:2405.13495) | "four trillion particles … 16 billion haloes … up to redshift z = 3" | match; 1LPT at z = 99 is a body value, not checked |

Cross-skill correction: `cosmo-beyond-two-point/SKILL.md` cited
arXiv:2505.10682 in a list for "BORG on 2M++, BOSS and Quaia" with no BOSS
paper in it. The line now attaches each ID to its data set and cites the BOSS
reconstruction (arXiv:1909.06396).

Gaps the agent declared: DES and Euclid covariance-mock counts; number of
CoLoRe-2LPT realisations; code names and box sizes of about ten suites whose
abstracts omit them (Millennium, Uchuu, Quijote, EAGLE, BAHAMAS, TNG boxes);
halo finders; ray-tracing accuracy; about 25 papers read in abstract but left
without ID by the 100-source cap (ELUCID, HESTIA, L-PICOLA, CARPool,
DarkEmulator2 among them).

## cosmo-surveys-facilities — 2026-10-09 — PASS, dates web-sourced

Checker: `cosmo-surveys-facilities: 100 sources, 0 problem(s) [arXiv-checked]`.
One run, 63 of 70 research calls. Built first from the sourced facility facts
of five sibling skills, then from overview papers and official pages. Forty
statements carry the flag `[sec: web]` (official page or web-search summary):
release dates and status lines are of that kind and were not re-fetched at
the gate.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| eROSITA DR2: catalogues from the first three all-sky surveys, German half (arXiv:2607.27772) | "first three completed eROSITA all-sky surveys (eRASS:3), covering the western Galactic hemisphere"; 1 911 744 point-like and 63 796 extended sources | match |
| MUST is under construction, 6.5 m, Stage V (arXiv:2605.10102) | "first Stage-V spectroscopic facility currently under construction … 6.5-meter … over 20,000 targets … ∼5 deg²" | match |
| Spec-S5 is a design: two 4 m telescopes upgraded to 6 m, 13 000 spectra each (arXiv:2608.07927) | same | match |
| Roman surveys are the community-defined ones (arXiv:2505.10574) | ROTAC report on the three Core Community Surveys | match |
| SDSS-V has no clustering programme (arXiv:2507.06989) | overview describes Milky Way, black-hole and local-volume mapping; no cosmological clustering survey named in the part read | consistent |

Dates settled at source by the agent: 4MOST first light 18 October 2025
(ESO); Euclid DR2 June 2029 on the ESA timeline, against March 2029 on the
IPAC page; Roman launch 30 August 2026 (NASA page).
Left unresolved in the files: Simons Observatory LAT first light (22 February
or April 2025); KiDS-Legacy calibration fields (23 or 27 deg²).

Gaps the agent declared: start of the 4MOST and WEAVE main surveys; DESI DR2
spectra release date; Rubin DR1 date; Roman tier areas; current SKAO
schedule; why eROSITA stopped early; LVK O5 date.

## cosmo-tensions-anomalies — 2026-10-10 — PASS; six sibling discrepancies examined

Checker: `cosmo-tensions-anomalies: 100 sources, 0 problem(s) [arXiv-checked]`.
Synthesis skill: 67 of its 100 sources are rows copied from sibling
bibliographies, 33 are new (cosmic dipole, large-angle CMB anomalies, JWST
abundance, H0 resolutions); 39 of 50 research calls.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| CatWISE dipole 3.3–3.6σ with clustering-aware mocks (arXiv:2511.00822) | "3.63σ in the absence of a clustering dipole, and 3.44σ with a randomly oriented clustering dipole" (abstract cut before the aligned case) | match on two of three values |
| DESI DR1 redshift dipole gives 358 km/s, matching the CMB velocity (arXiv:2608.30914) | "QSO sample implies a peculiar velocity of v = 357.9 …" | match |
| Joint CMB-anomaly p ≤ 3 × 10⁻⁸ becomes 2–3σ after look-elsewhere correction (arXiv:2602.10178) | "if the four tests with the smallest p-values are cherry-picked from 10 independent tests … only 3σ" | match |
| No model resolves H0; fourteen contenders compared (arXiv:2607.13283) | "fourteen representative solutions … four broad mechanisms"; conclusion past the part read | consistent |
| JWST: no spectroscopic sample needs more baryons than ΛCDM supplies (arXiv:2604.18683) | UV statistics at 7 ≤ z ≤ 14 "naturally reproduced within the standard ΛCDM framework … 2–3 percent of baryons converted into stars by z = 10–12" | match |

Sibling discrepancies reported by the agent, and the coordinator's reading:

| Quantity | Values | Reading | Action |
|---|---|---|---|
| ln B, DESI DR2 + CMB + DES-SN5YR | 4.88 ± 0.44 (dark-energy skill) vs +3.32 ± 0.27 (statistics skill) | two papers, two priors: DESI's own (arXiv:2503.14743) and an independent analysis (arXiv:2511.10631) | note added to the dark-energy skill; not comparable row by row |
| ln B with DES-Dovekie | odds about 5:1 vs −0.30 ± 0.19 | same: the Dovekie paper's own odds (arXiv:2511.07517) against the independent analysis | covered by the same note |
| Planck PR3 S8 | 0.834 ± 0.016 (CMB skill) vs 0.831 (weak-lensing skill) | published value against a value derived from the abstract's central σ8 and Ωm | weak-lensing skill now points to the published value |
| ACT Σmν 0.082 / 0.089 | abstract against revised body | already documented in both skills | none |
| Planck + SPT + ACT H0 | 67.24 ± 0.35 (H0 skill) vs 67.19 ± 0.38 (CMB skill) | first and second arXiv version; the H0 skill carries the first as the value adopted by H0DN | none |
| Ω_K, Planck + BAO | 0.001 ± 0.002 vs 0.0007 ± 0.0019 | abstract rounding against the body value of the same paper | none |

Outside the suite: the author's dipole report
(`reports/research/2026-08-19_kinematic-dipole-compilation/`) attributes
arXiv:2010.08366 to Secrest in its CSV. The arXiv record is Siewert et al.,
"The Cosmic Radio Dipole: Estimators and Frequency Dependence"; Secrest et
al. is arXiv:2009.14826. Not edited.

Gaps the agent declared: defining formulas and Planck p-values for S_1/2, the
low quadrupole and the dipole-modulation amplitude; per-catalogue kinematic
dipole expectations; bodies of the CosmoVerse paper and four 2026 reviews;
per-model tables of the H0 comparison.

## cosmo-reionization-21cm — 2026-10-10 — PASS

Checker: `cosmo-reionization-21cm: 100 sources, 0 problem(s) [arXiv-checked]`.
One run, 41 of 70 research calls.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| CHIME 21 cm auto-spectrum, 12.5σ at z ~ 1 (arXiv:2511.19620) | "first detection … in auto-correlation at z ~ 1 … 12.5 sigma", 0.4 < k < 1.5 h/Mpc | match |
| MeerKLASS auto-spectrum at z = 0.42 (arXiv:2610.12158, posted 2026-10-08) | "direct measurement of the 21-cm signal … at redshift z = 0.42 … 0.095 < k < 0.245 h/Mpc … approximately 236 deg²"; S/N past the part read | consistent |
| HERA Phase II first limits (arXiv:2511.21289) | 2σ limits in eight bands, 5.6 ≤ z ≤ 24.4; tightest Cosmic Dawn limit 1.13 × 10⁶ mK²; the mutual-coupling statement is past the part read | consistent |
| SPT-3G D1 secondary anisotropies (arXiv:2601.20551) | the abstract read gives the tSZ power; the kSZ value 1.75 ± 0.86 μK² is past the part read | not checked |

Cross-skill correction: `cosmo-surveys-facilities/SKILL.md` said 21 cm
cosmology rests on cross-correlation detections. The CHIME auto-spectrum
exists (confirmed above); the line now says so and points here.

The agent could not verify the lower end 0.051 of the τ range that
`cosmo-cmb` quotes (it read 0.054–0.063).

Gaps the agent declared: Lyα intensity mapping; SPHEREx, CONCERTO, mmIME,
COPSS results; REACH, MIST, PRIZM, EDGES-3 sky results; SKA array-assembly
dates; hardware facts for CHIME, MeerKAT, LOFAR, MWA; Bosman 2022, Becker
2021, Pritchard & Loeb 2012 and the wedge papers left out by the source cap.

## cosmo-multimessenger — 2026-10-10 — PASS

Checker: `cosmo-multimessenger: 125 sources, 0 problem(s) [arXiv-checked]`.
One run. The agent reports about 23 research calls for 125 sources (batched
abstract fetches) and passed the 100-source cap without deleting anything.
Because that ratio is low, eight claims were checked instead of five.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| LVK GWTC-5.0: H0 = 71.7 (+9.4/−7.5), 236 sources, mass spectrum + DES Y6 catalogue + GW170817 (arXiv:2605.27227) | same | match |
| GLADE+ complete to 47 Mpc (arXiv:2110.06184) | "complete up to luminosity distance d_L = 47 (+4/−2) Mpc" in B-band luminosity | match |
| GW170817 with the afterglow: 75.46 (arXiv:2305.19914) | "75.46 (+5.34/−5.39)" | match |
| Velocity correction framework for NGC 4993 (arXiv:1909.08627) | abstract gives H0 = 68.3 (+4.6/−4.5); the velocity 373 km/s is a body value | consistent, velocity not checked |
| DESI observations of the NGC 4993 group and H0 (arXiv:2512.08818) | paper confirmed, 39 group galaxies; the two H0 values are past the part read | consistent |
| Velocity covariance in siren H0 (arXiv:2509.03101) | paper confirmed; the factor of two is past the part read | consistent |
| Blinded mock challenge for the mass-spectrum method (arXiv:2412.14244) | paper confirmed; the 1.5σ figure is past the part read | consistent |
| 2026 VLBI reanalysis of GW170817 (arXiv:2605.11437) | paper confirmed; 65.5 ± 4.4 is past the part read | consistent |

Cross-skill correction: `cosmo-surveys-facilities` said "GWTC-5.0 has 267
mergers". 267 is the population-analysis sample; the cosmology analysis uses
236 sources. Line corrected.

Gaps the agent declared: GWTC-5.0 spectral-only and catalogue-only H0;
lensed gravitational waves, lensed FRBs, SN Zwicky / iPTF16geu; O1–O3a dates;
ET / CE / LISA milestones; CHIME outriggers; journal-version values where
they differ from the arXiv abstract.

## cosmo-theory-foundations — 2026-10-11 — PASS after a collision and one correction

Incident: two agents wrote this directory at the same time for about thirty
minutes. The first, launched on 2026-10-10, was suspended with the session
and resumed with it; the coordinator, reading its day-old progress file as a
dead run, launched a second. The second noticed foreign writes, stopped
without touching `SKILL.md` or pruning the bibliography, and left a hand-off
note. The first merged and deduplicated both contributions and finished.
Rule added to the coordinator's procedure: check the agent list before
relaunching after a restart.

Checker: `cosmo-theory-foundations: 100 sources, 0 problem(s) [arXiv-checked]`.
After the merge: no duplicated section heading in `physics-and-methods.md`
(346 lines), no duplicated bibliography key.

| Claim in the skill | arXiv abstract | |
|---|---|---|
| Limber error is O(1/ℓ²) and needs (ℓ + 1/2) (arXiv:0809.5112) | "the error in ordinary Limber approximation is O(1/ℓ²) … using ℓ instead of (ℓ+1/2) … spoils the accuracy" | match |
| HMcode-2020: 2.5 % RMS (arXiv:2009.01858) | "RMS error of 2.5 per cent … k < 10 h/Mpc … z < 2" | match |
| σ8's radius moves with h; σ12 removes this (arXiv:2002.07829) | "σ8 … does not correctly capture the impact of h on the amplitude of density fluctuations" | match |
| Growth-index formula "good to 0.05–0.5 %" (arXiv:astro-ph/0507263) | "fitting formula for linear perturbation growth accurate to 0.05–0.2 %" | **mismatch**; corrected to 0.05–0.2 % in `SKILL.md` and `systematics.md` |
| Inverse distance ladder, standard pre-recombination physics (arXiv:1411.1074) | "H0 = 67.3 ± 1.1 … assumes standard pre-recombination physics"; the 0.021 % fit accuracy is a body value | consistent |
| Revised halofit accuracy 5–10 % (arXiv:1208.2701) | accuracy figure past the part read | not checked |

Body-level claims not checked at the gate: DESI DR1 full-shape σ8 "excluding
neutrinos" (arXiv:2411.12021, footnote 3); the three Planck 2018 r_drag
values; z_d ≈ 1020 (eBOSS) against ≈ 1060 (DESI); the printed slips reported
in arXiv:1909.05277 and arXiv:astro-ph/0603494.

Cross-skill correction: `cosmo-neutrinos-dark-matter` listed "writing
N_eff = 3.046" as an error without qualification. It is the value in the
Planck 2013 and 2018 baselines; the bullet now says so.

Gaps the agents declared: accuracy of DESI's power-law r_d formula; DES Y6
modelling; ACT N_eff and non-linear choices; the full Challinor–Lewis
expression; mass-function and NFW formulae; BBKS and Carroll–Press–Turner;
PyBird bias conversion.

## cosmo-software-ecosystem — 2026-10-12 — PASS

Checker: `cosmo-software-ecosystem: 100 sources, 0 problem(s) [arXiv-checked]`.
One run, 56 of 70 research calls. Besides papers, the agent read library
documentation through the context7 MCP server, repository pages, and the
docstrings of the packages installed in the author's environment (camb 2.0.4,
pyccl 3.3.6, astropy 8.0.1, healpy 1.19.0, emcee 3.1.6, cosmoprimo 1.0.0) and
of local checkouts (CLASS v3.2.3, pypower 1.0.0, picca, flip). Nothing was
installed or modified. Files carry Snapshot 2026-10-11.

| Claim in the skill | Source | |
|---|---|---|
| CAMB v2 exists, a substantial update for high-precision surveys (arXiv:2607.14854) | abstract: "substantial update to CAMB … new treatment of the hyperspherical Bessel functions … updated integrators, a recalibrated fast recombination model" | match; the 1.5 % TT figure and the timing against CLASS are past the part read |
| EFTCAMB is superseded by H-EFTCAMB (arXiv:2603.01662) | abstract: "the official successor to EFTCAMB … Cobaya-Integrated, Python-Wrapped" | match |
| flip: k in h/Mpc, distances in Mpc/h, RA and Dec in radians, velocities in km/s; engines classy, cosmoprimo, pyccl | agrees with the author's project notes; flagged in the file as read in the flip checkout documentation; the per-engine unit conversion is declared not read | consistent |

Gaps the agent declared: flip's per-engine unit conversion; the k unit of
cosmoprimo spectra (derived, flagged); defaults of desilike, pycorr,
Corrfunc, Triumvirate, nbodykit, Vega, LaCE, MontePython, CosmoSIS; CLASS
later than 3.2.3; the BORG repository; no estimator cross-check paper found.

Reported, outside the suite, not fixed: in the author's environment the
`class` engine of cosmoprimo fails to import (pyclass built against NumPy
1.x, NumPy 2.4.6 installed).

All twenty-one planned sub-skills are now built, gated and installed.

## Waves 3 and 4 test and repair — 2026-10-12

GREEN on `questions-wave34.md`: 14 of 14 answered. Five conflicts repaired and
one ambiguous statement in `cosmo-statistics-inference` rewritten (mock-count
cost: variance factor against error-bar widening). Detail:
`baseline-grading-wave34.md`.

Suite total at this date: hub + 21 sub-skills.

## Packaging — 2026-10-12

The hub, the 21 sub-skills and these documents were moved from
`<config>/` (`claude/skills/`,
`reports/research/2026-10-07_cosmo-skill-suite/`) to `<repo>/`
(`skills/`, `docs/`). Paths in the operational files (agent brief, design,
conventions, hub `SKILL.md`, the peculiar-velocity pointers to the hub) were
rewritten; the test logs above keep the paths of the time they were written.

`claude_config/install.sh` now links every `cosmoskill/skills/*/` that holds a
`SKILL.md`: 44 links replaced (22 skills × 2 Claude homes), 0 broken,
`install.sh --check` reports 77 linked, 0 needing attention.

From the new location: `verify_sources.py skills/cosmo-*` exits 0 on all 21
skills with the arXiv check on (2,382 sources). The session's skill listing
shows all 22 skills under their plain names.

Nothing was committed in either repository.

## Deepening passes — from 2026-10-12

One research agent per skill, under `docs/agent-brief-deepen.md`: paper
bodies read for systematics and methods, classic references added. Gate per
skill: upkeep tools and checker rerun by the coordinator, then statements
carrying a body-level place compared with the paper.

| Skill | Date | Sources | Body-level places | Gate |
|---|---|---|---|---|
| `cosmo-weak-lensing` | 2026-10-12 | 192 → 224 (13 foundation added) | 0 → 229 | checker 0 problems, keys 0 problems, 35 tests pass. 10 statements compared, 10 match: KiDS-Legacy shear biases and redshift shifts (arXiv:2503.19441, Table 1, printed in units of 10⁻²), its feedback limit 7.71 (8.01) (Sect. 6), DES Y3 m and Δz priors (arXiv:2105.13543, prior table), HSC Y3 scale cuts (arXiv:2304.00702), DES Y6 PSF α (arXiv:2602.10065, App. A), DES Y6 magnification coefficients (arXiv:2601.14833), NLA–TATT 0.6σ (arXiv:2602.10065, Sect. VI.1), DES Y6 against Planck 2018 only 1.0σ (arXiv:2601.14559, Sect. VIII). One bullet of `SKILL.md` qualified by the coordinator: the 1.0σ is the full-parameter difference. Three bullets corrected by the agent (IA model shift, CMB reference of DES, KiDS-Legacy significance). Not read: bodies of DECADE, UNIONS and the DES Y6 redshift papers; arXiv:2511.18134 read in an earlier version only. |
| `cosmo-multimessenger` | 2026-10-13 (run cut once by the usage limit, resumed from its checkpoint) | 125 → 134 (foundation 6 → 13) | 5 → 135 | checker 0 problems, keys 0 problems, 35 tests pass. 11 statements compared, 11 match: GWTC-5.0 H0 (arXiv:2605.27227, abstract), the 1/H0 prior of the GW170817 measurement (arXiv:1710.05835), FRB host-model shift above 3σ, outlier shifts and the F values (arXiv:2507.18946, Sect. IV.1 and IV.4), F = 0.32 and the Galactic-disc selection (arXiv:2208.00819, App. A.2), F range (arXiv:2005.13161), mass-sheet limit from magnifications (arXiv:2403.18902, Sect. X.3), free-λ H0 of the quasar sample (arXiv:2506.03023), millilensing 29% against 10% (arXiv:2509.12301, Sect. V.2), delay shifts of SN 2025wny (arXiv:2608.28427, Sect. VI.1). One reference-file correction by the agent: the prior of the 2017 measurement is flat in log H0, not flat. Not read: arXiv:1805.11579 (no rendering), the text of Refsdal 1964, the current-version tables of arXiv:2602.04766 and arXiv:2507.18946. |
| `cosmo-simulations-mocks` | 2026-10-13 | 100 → 214 (foundation 0 → 52; before 2010: 2 → 64) | 0 → 89 | checker 0 problems (109 added arXiv rows compared with arXiv), keys 0 problems, 35 tests pass. The 5 rows with a DOI only compared with Crossref: author, title and year match. 9 statements compared, 9 match: EZmocks and PATCHY accuracies (arXiv:1409.1124, arXiv:1307.3285, abstracts), baryon effect without AGN feedback (arXiv:astro-ph/0512426), code agreement 1% to k = 1 and 3% to k = 10 at z ≤ 1 only (arXiv:1503.05920, abstract and Sect. 2.3), AbacusSummit step count (arXiv:2110.11398, Sect. II.5), FLAMINGO response (arXiv:2410.17109), DESI DR1 mock covariance rescaled by 10 to 40% (arXiv:2411.12027, Sect. 4). Three bullets of `SKILL.md` corrected by the agent: the 3% agreement holds at z ≤ 1; group baryon fraction drives the suppression without fixing it; full-shape covariance from rescaled mocks. Not read: abstracts of four papers cited by DOI (described from a review, flagged `[sec]`), bodies of Crocce 2006, COLA and FastPM, per-suite suppression at k = 1 h/Mpc, DESI DR2 mocks. |
| `cosmo-reionization-21cm` | 2026-10-13 | 101 → 167 (foundation 1 → 32, method 5 → 17; before 2010: 0 → 26) | 6 → 104 | checker 0 problems, keys 0 problems, 35 tests pass. The 3 rows with a DOI only (Gunn & Peterson 1965, Wouthuysen 1952, Field 1958) compared with Crossref: match. 9 statements compared, 9 match: Planck 2018 lowE optical depth and the limit on τ(15,30) (arXiv:1807.06209, Eqs. 2 and 85a), continuum share of the damping-wing error (arXiv:2406.12070, Sect. 5.7), HERA dynamic range (arXiv:2108.02263, abstract), HERA crosstalk filter (arXiv:2210.04912, Eq. 3), 100 mocks in the MeerKAT transfer function (arXiv:2206.01579, Sect. 4.3), EDGES depth of 370 to 670 mK with the beam correction (arXiv:1910.03165, Sect. 2.1.3), CO shot power (arXiv:2008.08087, abstract). Three bullets of `SKILL.md` corrected by the agent: uncertainty of the Planck optical depth is 0.005 to 0.009, not 0.006; CO is detected as shot noise, not on clustering scales; EDGES depth depends on the beam correction. Not read: bodies of Bowman 2018, Hills 2018 and Singh 2021; the three 1952 to 1965 papers have no abstract online; the SPT-3G D1 body read is the first version. |
| `cosmo-beyond-two-point` | 2026-10-13 (run cut by the usage limit after 40 of 60 research calls, all written to the files; finished by the coordinator) | 120 → 218 (foundation 1 → 49, method 20 → 44) | 0 → 141 | checker 0 problems, keys 0 problems, 35 tests pass. The 2 rows with a DOI only (Duane 1987, Alcock 1979) compared with Crossref: match; the first DOI is written with its parentheses percent-encoded, because the citation pattern stops at a parenthesis. 10 statements compared, 10 match: 1000 EZmocks and the omission of ELGs in the DESI DR1 bispectrum (arXiv:2503.09714, Sect. 2), SDSS void systematic offsets (arXiv:2205.06258, Table in Sect. 4.1), SimBIG test-set statement (arXiv:2310.15256, Sect. II.3), parity-odd significances (arXiv:2206.03625, arXiv:2508.09133, abstracts), field-level gain 3.5 (5.2) (arXiv:2403.03220), gain on σ8 at fixed power spectrum (arXiv:2610.01836, Sect. 6.2), DESI P+B shifts and their baseline (arXiv:2606.23936, abstract and Sect. 3.2), the finder-response paper's statement on the SDSS budgets (arXiv:2407.02699, Sect. 6). Two bullets of `SKILL.md` corrected by the coordinator from what the run had read: the 26% gain is not at fixed power-spectrum data vector; the SDSS void budgets cover the finder response through their fiducial-cosmology term. `physics-and-methods.md` (668 lines) and `systematics.md` (625) exceed the target length; nothing was cut. |
| `cosmo-cmb-lss-cross-correlations` | 2026-10-13 | 101 → 171 (foundation 4 → 39, method 3 → 22, review 0 → 5) | 0 → 65 | checker 0 problems, keys 0 problems, 35 tests pass. The 6 rows with a DOI only (Limber 1953, Sunyaev & Zel'dovich 1970 and 1980, Sachs & Wolfe 1967, Rees & Sciama 1968, Birkinshaw & Gull 1983) compared with Crossref: match. 5 statements compared, 5 match: scale cuts of the ACT DR6 × DESI Legacy analysis and its 0.19σ modelling test (arXiv:2410.10808, Sect. III.1), velocity bias of DESI DR2 LRGs, ELGs and quasars (arXiv:2604.04867, Sects. IV.2 and V.3). No bullet of `SKILL.md` contradicted. Cross-skill correction by the coordinator: `cosmo-peculiar-velocities` gave b_v ≈ 0.2–0.45; the ELG value is 0.10–0.15, so the range is now 0.1–0.45 by tracer. Not read: tSZ–CIB correlation coefficient, a miscentring size, the expected ISW signal-to-noise, bodies of the classic papers; arXiv:2309.05659 has no HTML rendering and was read as LaTeX. |
| `cosmo-distance-ladder-h0` | 2026-10-13 | 103 → 139 (foundation 4 → 24, method 5 → 16) | 0 → 129 | checker 0 problems, keys 0 problems, 35 tests pass. The 10 rows with a DOI only compared with Crossref: match. 7 statements compared, 7 match: SH0ES 2022 variant dispersion 0.3 km/s/Mpc, baseline 0.2 below the median, full error 1.04 km/s/Mpc or 1.4% (arXiv:2112.04510, Sect. 6.14, read as LaTeX: no HTML rendering), first-rung error 0.65% to 0.60% with the SMC and the metallicity slopes −0.234 ± 0.052 on [Fe/H] and −0.190 ± 0.047 on [O/H] (arXiv:2404.08038, abstract and Sect. V), supernova part of the H0 error 0.7 and 0.29 km/s/Mpc (arXiv:2202.04077, Sect. IV.5), CCHP TRGB budget 2.6%, 1.9%, 1% (arXiv:2408.06153, Sect. XIII.3). No bullet of `SKILL.md` contradicted. Not compared: the cells of Table 7 of arXiv:2112.04510. Not read: arXiv:1903.08096 (no HTML, no source); Leavitt & Pickering 1912 and Tully & Fisher 1977 have no DOI and are named in prose only; arXiv:2408.11770 body and abstract differ, abstract kept. |
| `cosmo-supernovae` | 2026-10-14 | 109 → 159 (foundation 3 → 22) | 0 → 105 | checker 0 problems, keys 0 problems, 35 tests pass. The 4 rows with a DOI only (Refsdal 1964, Cardelli 1989, Kirshner 1974, Pippin 2020) compared with Crossref: match. 6 statements compared, 6 match: DES-Dovekie sample of 1623 DES and 197 low-redshift SNe (arXiv:2511.07517, Sect. 6.1), Union3.1 with UNITY1.7 and Ω_m = 0.344 +0.026/−0.025 (arXiv:2601.19424, abstract and Sect. I.3), sign of the host term in Pantheon+ Eq. 1 and its footnote on the bias term (arXiv:2202.04077, Sect. II.1), redshift bias as the largest Pantheon+ term, 0.011 on w (same paper, Table 4), progenitor-age shift (arXiv:2604.16597). No bullet of `SKILL.md` contradicted; one added on the largest budget terms. Three reference-file corrections by the agent (UNITY version, largest Pantheon+ term, DES-Dovekie sample). Not read: Tripp 1998 (no arXiv version, no DOI); Union3.1 gives no budget of its own. |
| `cosmo-clusters` | 2026-10-14 | 100 → 122 (foundation 4 → 15, review 2 → 4, method 17 → 24) | 0 → 125 | checker 0 problems, keys 0 problems, 35 tests pass. No row with a DOI only added. 5 statements compared, 5 match: Planck 2015 count likelihood binning (arXiv:1502.01597, Sect. 5.1), weak-lensing bias uncertainties from TNG (arXiv:2310.12213, Eq. 39), mass-function uncertainty test (arXiv:2401.02075, Sect. IV.2.3), eRASS1 scatter prior (arXiv:2402.08458, Sect. 4.6), Rayleigh-plus-Gamma miscentring model (arXiv:2402.08455, Eq. 26). No bullet of `SKILL.md` contradicted. Not read: abstracts of Press & Schechter 1974, Kaiser 1986, White, Efstathiou & Frenk 1993, Sunyaev & Zel'dovich 1972 (not cited); cells of SPT Table 4 and DES Y3 Table 2; mass function of DES Y3 and HSC; Planck blinding. |
| `cosmo-cmb` | 2026-10-14 | 91 → 114 (23 classic papers) | 0 → 97 | checker 0 problems, keys 0 problems, 35 tests pass. No row with a DOI only added. 6 statements compared, 6 match: CamSpec PR4 A_L = 1.095 ± 0.056 and Ω_K = −0.025 +0.013/−0.010 (arXiv:2205.10869, Sect. 6 table), ACT DR6 lensing calibration shift 0.00432 (0.18σ) (arXiv:2304.05202, Sect. VII.2), lensing foreground bias −0.18σ and −0.04σ (MV), −0.31σ and −0.06σ (TT) (arXiv:2304.05196, Sect. V.1), ACT DR6 tSZ–CIB prior 0 ≤ ξ ≤ 0.2 (arXiv:2503.14452, Sect. VII.2), Plik calibration prior 1 ± 0.0025 (arXiv:1907.12875, Eq. 39). No bullet of `SKILL.md` contradicted. Not read: Silk 1968 (no abstract online, not cited), the ACT DR6 beam paper, the NPIPE low-ℓ transfer function; Planck N¹ tests and the ACT aberration correction left out at the length cap. |
| `cosmo-galaxy-clustering` | 2026-10-14 | 126 → 146 (11 foundation, 7 method, 2 review added) | 0 → 38 flags, several covering whole budget tables | checker 0 problems, keys 0 problems, 35 tests pass. The 2 rows with a DOI only (Peebles & Yu 1970, Sunyaev & Zel'dovich 1970) compared with Crossref: match. 5 statements compared, 5 match: DESI DR1 BAO systematic totals 0.245 and 0.3 per cent and their (α_⊥, α_∥) projection with correlation 0.478 (arXiv:2404.03000, Sect. 5.5, Eq. 20), DR2 BAO systematic table, 0.221 and 0.329 per cent (arXiv:2503.14742, Sect. V.2), DR1 full-shape total systematic 0.46 σ of the DR1 error (arXiv:2411.12021, Sect. 5.8). No bullet of `SKILL.md` contradicted. Not read: per-tracer HOD shifts of the full shape (arXiv:2411.12023, Table 2), the DR2 mock-recovery table; DR1 BAO estimator details read but not written, the methods file being at the cap. |
| `cosmo-lyman-alpha` | 2026-10-14 | 172 → 196 (24 foundation and method papers) | 1 → 87 | checker 0 problems, keys 0 problems, 35 tests pass. The DOI-only row added (Kaiser 1987) is already confirmed in `cosmo-galaxy-clustering`. 5 statements compared, 4 match: DESI DR2 BAO validation against σ/3 (arXiv:2503.14739, Sect. V.2), DR1 BAO covariance validation 0.96 ± 0.05 and 0.99 ± 0.06 (arXiv:2404.03001, Sect. 6.2.2), continuum-bias table 6.768 − 0.699x at z = 2.2 (arXiv:2505.07974, App. B), DR2 full-shape minimum scales 30 and 40 h⁻¹Mpc with small-scale marginalisation in the undistorted model, leakage from r_∥ < 10 h⁻¹Mpc (arXiv:2607.27410, Sects. III.3 and IV.1). The fifth, the mock β_Lyα sequence 1.628 → 1.553 → 1.464 attributed to Table 4 of arXiv:2404.03001, was not found in the HTML rendering; not confirmed. Three reference-file corrections by the agent, confirmed: the DR2 full shape marginalises below r_min = 30 (auto) and 40 (cross) h⁻¹Mpc, not below 10; its non-linear parameters are fixed to ForestFlow values, not given priors. Not read: per-redshift P1D budgets (figures only), DR2 BAO blinding, the cross-correlation damping equation. |
| `cosmo-peculiar-velocities` | 2026-10-14 (two earlier starts stopped before any research: one stalled, one hit the usage limit) | 150 → 164 (14 rows, 1976–2008) | about 33 → 108 | checker 0 problems, keys 0 problems, 35 tests pass. The 4 new rows with a DOI only (Faber & Jackson 1976, Lynden-Bell 1988, Bertschinger & Dekel 1989, Dekel 1990) compared with Crossref: match. 5 statements compared, 5 match: 6dFGS systematic dominated by α_b, 6.06 × 10⁻², against 1.09 × 10⁻³ for σ_u (arXiv:2004.06399, Sect. 5.1.1, Table 5), DESI DR1 field-level fit with σ_u = 16 h⁻¹Mpc on 675 mocks, mean error 0.036 against scatter 0.066 before cuts and 0.059 after, errors rescaled by their ratio following Sugiyama et al. (arXiv:2512.03229, Sects. 4.4.2 and 5; the factor 1.64 is the ratio, derived), η converted to velocity in the DESI momentum spectrum (arXiv:2512.03231, Sect. 2.1.2). Two bullets of `SKILL.md` corrected by the agent (errors Gaussian in η, the momentum spectrum still converts η to v; σ_u fixed at 16 with errors rescaled); one reference-file correction (the 6dFGS systematic comes from α_b, not σ_u). Not read: Tully & Fisher 1977 abstract (no DOI or arXiv record), a 2025 bulk-flow amplitude, the SDSS PV power-spectrum scale range, three budgets. |
| `cosmo-dark-energy-modified-gravity` | 2026-10-14 | 99 → 126 (18 foundation, 3 review, 5 method or code, 1 critique) | 0 → about 129 | checker 0 problems, keys 0 problems, 35 tests pass after the coordinator regenerated one stale level block. The 3 rows with a DOI only (Ratra & Peebles 1988, Wetterich 1988, Horndeski 1974) compared with Crossref: match; the Wetterich DOI is written percent-encoded. 5 statements compared, 5 match: the w0wa preference 3.1σ, 2.7σ without CMB lensing, 2.4σ with compressed CMB priors (arXiv:2503.14738, Sect. IX), τ = 0.09 prior leaving Δχ²_MAP = −3.82, 1.4σ (arXiv:2504.16932, Sect. III.2), 118 Foundation SNe common to Pantheon+ and DES5Y with offset −0.051 ± 0.007 mag (arXiv:2408.07175, Sect. 3) and their place in the DES5Y split (arXiv:2411.11685, Sect. 4.2). One bullet of `SKILL.md` corrected by the agent: the significances per CMB treatment, and 1.4σ (not ≃1.5σ) with τ = 0.09. Not read: bodies of arXiv:2502.04212 and arXiv:2504.21813; which named Horndeski models survive GW170817; the classic papers cited by DOI beyond their metadata. |
| `cosmo-neutrinos-dark-matter` | 2026-10-14 | 101 → 114 (7 foundation, 3 review, 2 method, 1 data) | 0 → 92, plus about 30 table rows with their place | checker 0 problems, keys 0 problems, 35 tests pass. No row with a DOI only added. 4 statements compared, 4 match: SPT CMB-SPA + DESI bound Σm_ν < 0.055 eV (arXiv:2506.20707, Eq. 106), DESI BAO + CMB (CamSpec) < 0.0642 eV (arXiv:2503.14738, Sect. VIII), the half-mode-mass conversion slope −3.564 (arXiv:2511.07513, Sect. IV.2), the 9.7 keV joint lensing and satellite bound (arXiv:2101.07810, abstract). Two bullets of `SKILL.md` corrected by the agent: SPT's own collaboration bound is below DESI's; the JWST lensing keV values are Bayes-factor bounds and the conversion slope differs between papers. The agent also shortened `SKILL.md` to about 690 words; the diff shows rewording only, no fact removed. Not read: two M_hm-to-keV relations, the source of DESI's fixed-mass state count, an alternative subhalo suppression, prior tests of the JWST lensing limits. |
| `cosmo-inflation-primordial` | 2026-10-14 | 100 → 132 (31 foundation, method or review) | 0 → 107 | checker 0 problems, keys 0 problems, 35 tests pass. The 12 rows with a DOI only (inflation papers of 1980–1992, Carroll 1990) compared with Crossref: match; contents not read. 4 statements compared, 4 match: BK18 fixes n_t = 0 in the likelihood and estimates a point-source bias on r of 1–3 × 10⁻³ (arXiv:2110.00483, likelihood paragraph and App. F.2), the SO six-SAT forecast σ(r) = 1.4 × 10⁻³ for pessimistic 1/f noise, A_lens = 0.5 and foreground decorrelation, 1.2 × 10⁻³ with A_lens = 0.3 (arXiv:2512.15833, Sect. 3.2 table). One bullet of `SKILL.md` qualified by the agent (the SO forecast and its delensing), two sizes added to the referee list; one reference-file correction (BK18 fixes n_t = 0, it does not use the consistency relation). Not read: arXiv:2504.00884 (no HTML), values inside ACT DR6 Tables 5 and 9 and the Planck PR4 birefringence table, BICEP/Keck blinding. |
| `cosmo-statistics-inference` | 2026-10-14 (a first start hit the usage limit before any research) | 100 → 118 (foundation 11 → 20, review 2 → 6) | 0 → 104 | checker 0 problems, keys 0 problems, 35 tests pass. No row with a DOI only added (Wilks 1938 and Duane 1987 not cited, no abstract). 3 statements compared, 3 match: rank-normalised R̂ < 1.01 against the 1.1 of 1992 (arXiv:1903.08008, Sect. 2), the cosmology R − 1 measures the variance of chain means (arXiv:1304.4473, Sect. IV.1), the profile-likelihood review's validity analysis (arXiv:2408.07700). One derived statement checked for its flag: R − 1 < 0.01 is about R̂ < 1.005, marked `[der]` with its derivation and assumptions. Three bullets of `SKILL.md` sharpened by the agent (boundary-corrected or Feldman–Cousins belt; variance against error-bar factor kept explicit; R − 1 is not R̂); the body was compressed to 700 words, the diff shows rewording only. Not read: the Percival 2014 m_2 factor, the eigentension paper, the Friedrich & Eifler paper, DESI DR2 covariance practice. |
| `cosmo-surveys-facilities` | 2026-10-14 (prompt adapted: facility specifications from instrument and survey-design papers) | 102 → 110 (DESI design, KiDS overview, Euclid Red Book, Planck mission, ACT and SPT-3G receivers, Advanced LIGO and Virgo) | 0 → 72 | checker 0 problems, keys 0 problems, 35 tests pass. No row with a DOI only added. 3 statements compared, 3 match: CHIME first light 7 September 2017 and cosmology data from 7 October 2018 (arXiv:2201.07869, Sect. IV.1), Roman wide-area tiers 2400, 2700 and 19.2 deg² with their depths (arXiv:2505.10574, Sect. II). One `[sec: web]` flag replaced by a paper, several secondary flags replaced by body reads. No bullet of `SKILL.md` contradicted; one recurring error added (gravitational-wave candidate counts without their threshold). Not read: bodies of the 4MOST overview, the 2019 Roman paper and GWTC-4.0 (no rendering, LaTeX download failed), LiteBIRD beam widths, why eROSITA stopped early. |
| `cosmo-software-ecosystem` | 2026-10-14 (prompt adapted: code comparisons, defaults, units) | 100 → 107 (line-of-sight integration, Ma & Bertschinger, FFTLog, MASTER, Skilling, Goodman & Weare, Neal) | 0 → 85 | checker 0 problems, keys 0 problems, 35 tests pass. The 2 rows with a DOI only (Skilling 2006, Goodman & Weare 2010) compared with Crossref: match. 3 statements compared, 3 match: the SO-like accuracy likelihood (arXiv:2607.14854, App. C), the NaMaster curved-sky validation with N_dof = 681 (arXiv:1809.09603, Sect. 4.2), MultiNest Ω_m intervals about 10% smaller than PolyChord's (arXiv:2202.08233, Sect. 4.4). The bullet the agent sharpened said "Ω_m and σ8 widths about 10 % too narrow"; the paper gives about 10% for Ω_m and "to a lesser extent" for S8: corrected by the coordinator. One reference-file correction by the agent: the CAMB citation place is App. B, read in an earlier version. Not read: the Landy & Szalay abstract (no row added), the DISCO-DJ II body, the sampler-settings table of Lemos et al. 2022, bodies of eight further codes. |
| `cosmo-theory-foundations` | 2026-10-15 (first run cut after 12 of 55 calls, resumed run cut by the weekly limit during its final upkeep step; upkeep, gate and checkpoint removal finished by the coordinator on 2026-10-16) | 100 → 104 (Pezzotta 2025, Schöneberg 2022, Calabrese 2025, Alam 2017) | lines naming an equation, section, table or appendix: 153 → 214 (equation numbers re-read in the HTML rendering for Hogg, Planck 2013, Aubourg, DESI DR2, Linder, Eisenstein & Hu, Hamilton, Ivanov, Asgari, LoVerde, Krause, Lesgourgues & Pastor, Reid & White) | checker 0 problems, keys 0 problems, 35 tests pass; one stale level block regenerated. 6 statements compared, 6 match: DESI DR2 r_d power law (arXiv:2503.14738, Eq. 2), Aubourg calibrated r_d "accurate to 0.021%" (arXiv:1411.1074, Eq. 16, Sect. II.2), c₂² ≈ 2.5 σ_v² for b₁ = 2, f = 0.75 (arXiv:1909.05277, Eq. 3.8), DES Y3 prior 10³Ω_ν h² ∈ (0.60, 6.44) (arXiv:2105.13549, Table 1), ACT DR6 HyRec/CosmoRec instead of Recfast (arXiv:2503.14454, Sect. III), growth index γ = 0.55 + 0.05[1 + w(z=1)] and its accuracy (arXiv:astro-ph/0507263, Sect. V.1, Eq. 17). One `SKILL.md` bullet corrected by the agent (growth-index accuracy). Recorded slip: (b₁ + fμ)² in Eq. A.1 of arXiv:1909.05277. Not verified: σ8 of cold matter against total matter (no number found in arXiv:1311.0866); accuracy of the DESI power-law r_d against a Boltzmann code (not stated in arXiv:2209.14330 or arXiv:2212.04522). |
| `cosmo-tensions-anomalies` | 2026-10-16 (last of the 21; prompt adapted: reconcile with the deepened sibling skills first, then read the tension measurements) | 100 → 106 (foundation: Marshall 2006, Park & Rozo 2019, Lin & Ishak 2017; method: Raveri 2020, Raveri & Doux 2021, Bevins 2024; Raveri & Hu and Handley & Lemos re-roled foundation) | 0 → 127 | checker 0 problems, keys 0 problems, 35 tests pass; 30 of 60 research calls. 5 statements compared, 5 match: KiDS-Legacy Hellinger distance 0.76σ in S8 (arXiv:2503.19441, Sect. 7), DES Y6 3×2pt 1.8σ full space from SPT+ACT+Planck and 1.0σ from Planck 2018 (arXiv:2601.14559, Sect. V.2), CMB-SPA A_2pt = 1.079 ± 0.038 and 1.6σ in the (A_2pt, A_recon) plane (arXiv:2506.20707, Sect. VII.2.3), DESI DR2 w0wa 2.4σ with compressed CMB priors (arXiv:2503.14738, Sect. VII.1), 1.4σ with τ = 0.09 (arXiv:2504.16932, Sect. III.2). Three `SKILL.md` bullets corrected by the agent (S8 metric and endpoints, w0wa significances, A_L). Sibling discrepancies reported by the agent and fixed by the coordinator after reading at source: KiDS-Legacy 0.73σ now labelled Σ8 with 0.76σ in S8 in `cosmo-weak-lensing` (`results.md`, `open-questions.md`), `cosmo-statistics-inference` `results.md` (metric now read) and hub `field-state-2026.md`; "about 1.5σ" → 1.4σ in `cosmo-neutrinos-dark-matter` (`results.md`, `systematics.md`). One reported discrepancy not acted on: `cosmo-cmb` "σ ≈ 0.006" refers to the Planck reprocessings (SRoll2, NPIPE, PR4), whose errors are 0.0053–0.0062; Planck 2018 lowE alone gives 0.0086 (arXiv:1807.06209, Eq. 2), a different data set. Not read: SH0ES 2022 body, the bodies of the SPT and PSZ2 cluster papers, two further papers. |

## New domains — from 2026-10-16

One build agent per domain, under `docs/agent-brief.md` and the scope row of
`docs/scopes-new-domains.md`, in the order set there. Gate per skill: upkeep
tools and checker rerun by the coordinator, no edit outside the skill's
directory, statements compared with the papers, then the hub router row and
`install.sh` by the coordinator.

| Skill | Date | Sources | Body-level places | Gate |
|---|---|---|---|---|
| `cosmo-photometry-photoz` | 2026-10-16 | 110 (33 method, 22 results, 17 data, 12 foundation, 10 systematics, 8 code, 5 forecast, 3 review); 11 subtopics from Newman & Gruen 2022 (arXiv:2206.13633) and Tortorelli & Grün 2026 (arXiv:2605.06790) | 41 | checker 0 problems, keys 0 problems, 35 tests pass; about 50 of 90 research calls; no file changed outside the skill. 6 statements compared, 6 match: DES Y6 FGCM uniformity < 1.8 mmag and absolute scale ~1% via CALSPEC C26202 (arXiv:2305.01695), 14% recalibration of SFD (arXiv:1012.4804), DESI stellar reddening up to 80 mmag from SFD (arXiv:2409.05140), Euclid SOM binning on cell spec-z meets the requirement in 0 of 10 bins, on photo-z in 8 of 10 (arXiv:2508.02779), pop-cosmos against shark Δz ~ 0.05–0.1 in the edge bins of KiDS-1000 (arXiv:2602.03935), DES Y6 σ⟨z⟩ = 0.012, 0.008, 0.009, 0.024 dominated by missing faint spectra (arXiv:2510.23566). Thin: p(z) storage; LSST DESC requirements read through the review only. Not read: KiDS DR5 photometry paper, J-PAS, Roman and CSST photo-z plans. Hub router row added; linked by `install.sh`. |
| `cosmo-galaxy-halo-connection` | 2026-10-16 | 117; 10 subtopics from Asgari et al. 2023 and Wechsler & Tinker 2018 (no second review within five years found) | 66 | checker 0 problems, keys 0 problems, 35 tests pass; about 50 of 90 research calls; no file changed outside the skill. 8 statements compared with the abstracts, 8 match: Tinker 2008 mass function calibrated to ≲ 5%, amplitude down 20–50% to z = 2.5 (arXiv:0803.2706); redMaPPer bias ratio 1.02 ± 0.14 after the projection-robust split (arXiv:1611.00366); A = 0.79 ± 0.03 at Planck with DES+KiDS (arXiv:2202.07440); UNIONS no significant "lensing is low" for CMASS (arXiv:2606.23651); DESI DR1 S8 = 0.797 (+0.023/−0.024) with DES+KiDS lensing (arXiv:2512.15962); Q_sat = 0.05 ± 0.14 (arXiv:2510.20896); CMASS velocity bias 0.22 (centrals) and 0.86 (satellites) (arXiv:1407.4811); dwarf SHMR slope 2.08 ± 0.21, scatter 0.68 (+0.21/−0.33) dex at LMC-like scales (arXiv:2609.04351). Not read: DESI DR2, Euclid, Rubin, HSC Y3, DES Y6 galaxy–halo results; Sheth–Tormen, NFW and exclusion prescriptions quoted through the Asgari review. Hub router row added; linked by `install.sh`. |
