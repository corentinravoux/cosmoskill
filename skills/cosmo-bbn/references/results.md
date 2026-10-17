# BBN — results

Scope: current primordial abundances, BBN predictions, the baryon density
from BBN and its comparison with the CMB, N_eff and new-physics limits from
BBN alone and with the CMB, with the history of the key numbers.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Eq. n]`,
`[src: Table n]` body read; `[sec]` named secondary source; `[der]` derived here.

## 1. Primordial deuterium
<!-- key: primordial-deuterium -->

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| (D/H)_P, precision sample | log₁₀(D/H)_P = −4.5974 ± 0.0052; 10⁵ (D/H)_P = 2.527 ± 0.030 | seven homogeneously analysed absorbers (Keck/HIRES, VLT/UVES) | Cooke, Pettini & Steidel 2018, arXiv:1710.11129 | [src: Sect. V.1, Eq. 9–10] |
| (D/H)_P, all prior measurements plus J1332+0052 | (2.533 ± 0.024) × 10⁻⁵; 5% more precise than before; ~2.2σ moderate tension with the Standard-Model expectation | eight-system compilation | Kislitsyn et al. 2024, arXiv:2401.12797 | [src] |
| J1332+0052 sub-DLA, z_abs = 3.42 | log(D I/H I) = −4.622 ± 0.014 (0.008 dex statistical, 0.012 dex systematic); [O/H] = −1.71 ± 0.02; log N(H I) = 19.304 ± 0.004 | VLT/UVES + Keck/HIRES | arXiv:2401.12797 | [src] |
| Q1243+307, z_abs = 2.52564 | log₁₀(D/H) = −4.622 ± 0.015 from eight D I lines; [O/H] = −2.769 ± 0.028 | Keck/HIRES archival + new | arXiv:1710.11129 | [src] |
| PKS1937−101, z ≈ 3.572 | (2.638 ± 0.128) × 10⁻⁵ ESPRESSO alone; (2.608 ± 0.102) × 10⁻⁵ with UVES | VLT/ESPRESSO | Guarneri et al. 2024, arXiv:2402.05586 | [src] |
| Q1009+2956, z_abs = 2.504 | D/H = 2.48 (+0.41/−0.35) × 10⁻⁵ (17% error despite S/N 147) | Keck | Zavarygin et al. 2018, arXiv:1706.09512 | [src] |
| (D/H)_p, 13 "reliable" literature values (least trimmed squares on 15) | (2.545 ± 0.025) × 10⁻⁵, giving Ω_b h² = 0.02174 ± 0.00025 | literature compilation | arXiv:1706.09512; arXiv:1801.04704 | [src] |

The seven systems of the precision sample are statistically consistent with
one another although they span different amounts of stellar processing; chemical-evolution
models give D/H unchanged from primordial below about 1% of solar
metallicity (Cooke 2024 review, arXiv:2409.06015) [src: Sect. 3.1].

**Standard-BBN predictions at the CMB baryon density.** Yeh, Olive & Fields
(2021, arXiv:2011.13874) predicted (D/H) = (2.51 ± 0.11) × 10⁻⁵ with the
LUNA d(p,γ)³He data included, against (2.57 ± 0.13) × 10⁻⁵ with older rates
[src]. Launders, Giovanetti & Liu (2026, arXiv:2604.16600), fitting the
three deuterium-burning reactions with Gaussian-process regression, predict
10⁵ D/H = 2.442 ± 0.040 at the Planck baryon density, 1.70σ below Cooke et
al., and 1.98σ with the combined Planck + ACT DR6 + SPT-3G D1 baryon density
[src]. The predicted error is larger than the observational one in every
analysis read here: the observations are no longer the limiting factor.

## 2. Primordial helium-4
<!-- key: primordial-helium-4 -->

Y_P is the primordial ⁴He mass fraction; y_P = n(He)/n(H) by number.

| Group, sample | Y_P | Method | Citation | Flag |
|---|---|---|---|---|
| LBT Y_p Project IV: 15 low-metallicity (O/H < 4 × 10⁻⁵) high-S/N targets of 54 observed | 0.2458 ± 0.0013 (0.5%) | weighted average; no regression | Aver et al. 2026, arXiv:2601.22238 | [src] |
| LBT Y_p Project IV, same 41-target qualifying set | 0.2451 ± 0.0022 (weighted least squares, S = 1.70); 0.2466 ± 0.0025 (linmix, intrinsic scatter 0.00262 ± 0.00048) | regression on y vs O/H | arXiv:2601.22238 | [src: Sect. VII.3, Eqs. 5–6] |
| EMPRESS XV: 29 Subaru NIR galaxies incl. 14 EMPGs, plus 58 literature | 0.2402 ± 0.0040; implies N_eff = 2.54 (+0.20/−0.25) | photoionisation modelling with He I 10830 | Yanagisawa et al. 2025, arXiv:2506.24050 | [src] |
| EMPRESS VIII: 8 EMPGs + 51 metal-poor galaxies | 0.2370 (+0.0034/−0.0033) | regression | Matsumoto et al. 2022, arXiv:2203.09617 | [src] |
| Ioffe group (Kurichin et al.): 100 SDSS H II regions + HeBCD | 0.2462 ± 0.0022; with PDG D/H, N_eff = 2.95 ± 0.16 | regression to zero metallicity | Kurichin et al. 2021, arXiv:2101.09127 | [src] |
| Valerdi, Peimbert & Peimbert: 7 H II regions (VLT/FORS1) | 0.2448 ± 0.0033 for ΔY/ΔZ_O = 3.3 ± 0.7 | t² formalism, Helio14 | Valerdi et al. 2021, arXiv:2105.12260 | [src] |
| PHLEK survey (Hsyu, Cooke et al.): 16 Keck NIR galaxies + SDSS + literature | y_P = 0.0805 ± 0.0017, Y_P = 0.2436 ± 0.0040; with Cooke D/H, Ω_b h² = 0.0215 ± 0.0005, N_eff = 2.85 ± 0.28 | linear fit with intrinsic scatter | Hsyu et al. 2020, arXiv:2005.12290 | [src] |
| Aver, Olive & Skillman 2015 (HeBCD + He I 10830) | 0.2449 ± 0.0040 | regression | arXiv:1503.08146 | [src] |
| Izotov, Thuan & Guseva 2014: 28 of 45 H II regions | 0.2551 ± 0.0022; with D/H, N_eff = 3.58 ± 0.25 | regression, He I 10830 | arXiv:1408.6953 | [src] |
| Intergalactic absorber at z_abs = 1.724 (Cooke & Fumagalli) | Y = 0.250 (+0.033/−0.025) | He I absorption against a quasar | arXiv:1810.06561 | [src] |

**Prediction.** Standard BBN at the Planck baryon density gives
Y_P = 0.24709 ± 0.00017 with PRIMAT (arXiv:1801.08023) [src]; the LBT team
quotes 0.2467 ± 0.0002 from its own code (arXiv:2601.22238) [src]. The
spread of measured values (0.2370 to 0.2551) is much larger than any quoted
error and is set by method and sample, not by statistics.

## 3. Helium-3
<!-- key: helium-3 -->

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| ³He/⁴He, Orion Nebula (θ² Ori A) | (1.77 ± 0.13) × 10⁻⁴, first direct measure outside the Local Interstellar Cloud | VLT/CRIRES+ metastable He I* absorption | Cooke et al. 2022, arXiv:2203.11256 | [src] |
| (³He/⁴He)_P inferred with chemical evolution (2022) | (1.043 ± 0.089) × 10⁻⁴ (model error excluded), ~2σ from Standard Model (1.257 ± 0.017) × 10⁻⁴ | Orion + protosolar | arXiv:2203.11256 | [src] |
| (³He/H)_P empirical limit | < (1.09 ± 0.18) × 10⁻⁵ | Galactic D/H, He/H, ³He/⁴He | arXiv:2203.11256 | [src] |
| (³He/⁴He)_P inferred (2026) | (1.15 +0.24/−0.21) × 10⁻⁴, consistent with Standard Model + CMB | two new Milky Way He I* absorbers + Orion at ≲ 4% | Cooke et al. 2026, arXiv:2605.00122 | [src] |
| Galactic ³He/H gradient | (−0.116 ± 0.022) × 10⁻⁵ as a function of Galactocentric radius (units as in the paper); little variation overall, the "³He plateau" | GBT ³He⁺ 8.7 GHz in five H II regions | Balser & Bania 2018, arXiv:1810.09422 | [src] |
| N_eff from D/H + pre-solar ³He/⁴He | 3.01 (+0.95/−0.76), 95% | meteoritic ratio assumed primordial | Cooke 2015, arXiv:1510.02801 | [src] |

The H II-region plateau, against high ³He/H in some planetary nebulae, is the
"³He problem"; thermohaline mixing in stellar models suppresses net ³He
production and predicts the small negative gradient observed
(arXiv:1810.09422) [src]. A further ~4 measurements of ³He/⁴He within
~3 kpc would give the primordial ratio to ~30% (**forecast**, Johnson,
Weller & Cooke 2025, arXiv:2510.08689) [src].

## 4. Lithium-7
<!-- key: lithium-7 -->

| Quantity | Value | Citation | Flag |
|---|---|---|---|
| ⁷Li/H observed (Spite plateau, as adopted by PRIMAT from Sbordone et al. 2010) | (1.58 +0.35/−0.28) × 10⁻¹⁰ | Pitrou et al. 2021, arXiv:2011.11320 | [src: Table 2] |
| ⁷Li/H predicted, PRIMAT 2021 at 100 Ω_b h² = 2.242 ± 0.014 (Planck 2018 CMB + BAO), τ_n = 879.4(6) s | (5.464 ± 0.220) × 10⁻¹⁰ | arXiv:2011.11320 | [src: Table 2] |
| ⁷Li/H predicted, PRIMAT 2018 at 100 Ω_b h² = 2.2250 ± 0.016 | (5.627 ± 0.259) × 10⁻¹⁰ | arXiv:2011.11320 | [src: Table 2] |
| ⁷Li/H scaling, Fields–Olive–Yeh | 4.937 × 10⁻¹⁰ at η₁₀ = 6.115, ∝ η^2.117 | Yeh et al. 2023, arXiv:2303.04140 | [src: Eq. 16] |
| Size of the discrepancy | factor 3–4, 4–5σ (WMAP era) | Fields 2012, arXiv:1203.3551 | [src] |
| Plateau level after the "meltdown" | A(Li) ≈ 2.3 reached by [Fe/H] ≈ −3.0 | Norris et al. 2023, arXiv:2303.11497 | [src] |
| ω Centauri main-sequence and subgiant stars (91 stars) | A(Li) = 2.19 ± 0.14 | Monaco et al. 2010, arXiv:1008.1817 | [src] |
| GALAH warm dwarfs (> 100 000 stars) | cool group on the plateau ~0.4 dex below BBN; warm group at −1.0 < [Fe/H] < −0.5 forms an elevated plateau "largely consistent" with BBN | Gao et al. 2020, arXiv:2006.05173 | [src] |
| Globular-cluster diffusion correction | birth-cloud Li of plateau stars ~0.3 dex higher, leaving ~0.15 dex nominal offset | Korn 2021, arXiv:2111.00913 | [src] |
| Interstellar ⁷Li, Small Magellanic Cloud (¼ solar metallicity) | nearly equal to the BBN prediction | Howk et al. 2012, arXiv:1207.3081 | [src] |

The ratio of the PRIMAT 2021 prediction to the adopted observation is 3.5
[der: 5.464/1.58]. Fields et al. (2020) conclude that the problem "remains,
and indeed is more acute given the very tight D/H observational
constraints"; new ⁷Be(n,p) data increase the uncertainty slightly without
changing the problem (arXiv:1912.01132) [src].

## 5. Baryon density from BBN
<!-- key: baryon-density-from-bbn -->

All rows assume standard BBN with N_ν = 3 unless stated.

| Ω_b h² (or 100 Ω_b h²) | Inputs | Rate treatment | Citation | Flag |
|---|---|---|---|---|
| 100 Ω_b h² = 2.166 ± 0.015 (D/H) ± 0.011 (BBN); η₁₀ = 5.931 ± 0.051 | Cooke 2018 D/H | Marcucci et al. ab-initio d(p,γ) | arXiv:1710.11129 | [src: Sect. V.2, Eqs. 11–12] |
| 100 Ω_b h² = 2.235 ± 0.016 ± 0.033 | Cooke 2018 D/H | Adelberger et al. empirical d(p,γ) | arXiv:1710.11129 | [src: Eq. 14] |
| 0.02218 ± 0.00055 (ΛCDM); 0.02196 ± 0.00063 (+N_eff) | PDG 2023 D/H and Y_P | PRyMordial, rates marginalised | Schöneberg 2024, arXiv:2401.15054 | [src] |
| 0.02236 ± 0.00034 | Cooke D/H + Aver 2015 Y_P | PArthENoPE v3.0 (LUNA) | arXiv:2401.15054 | [src: Sect. 4.1] |
| 0.02195 ± 0.00021 | same | PRIMAT rates in PRyMordial | arXiv:2401.15054 | [src: Sect. 4.1] |
| 0.0215 ± 0.0005 (with N_eff free) | PHLEK Y_P + Cooke D/H | — | Hsyu et al. 2020, arXiv:2005.12290 | [src] |
| 0.02174 ± 0.00025 | 13-system D/H compilation | — | Zavarygin et al. 2018, arXiv:1706.09512 | [src] |
| 0.02236 ± 0.00014; η = (6.120 ± 0.038) × 10⁻¹⁰ | LBT Y_p + D/H + BBN + CMB | Fields–Olive–Yeh | Yeh et al. 2026, arXiv:2601.22239 | [src] |
| 0.02229 ± 0.00016 with N_ν free | same | same | arXiv:2601.22239 | [src] |

**CMB comparison.** PRIMAT 2021 compares with 100 Ω_b h² = 2.242 ± 0.014
(Planck 2018 CMB + BAO) and predicts D/H = (2.439 ± 0.037) × 10⁻⁵ against
the observed 2.527 ± 0.030 (arXiv:2011.11320) [src: Table 2], the
≃1.8σ tension of its abstract [src]. The CMB baryon density itself, for
Planck, ACT DR6, SPT-3G and their combinations, is held in `cosmo-cmb`.
Light-element Ω_b h² and CMB Ω_b h² agree or disagree at the 1–2σ level
depending on the rate set: data-driven rates (PArthENoPE, Fields–Olive–Yeh)
give agreement, ab-initio or Gaussian-process rates give D/H predictions
1.7–2σ below observation (arXiv:2011.13874, arXiv:2011.11537,
arXiv:2011.11320, arXiv:2604.16600) [src].

**Use as a prior.** BAO analyses calibrate r_d with a BBN prior on ω_b; the
value in common use is the PRyMordial 0.02218 ± 0.00055. Akharman et al.
(2026) note that the DESI DR2 analysis takes its prior from one reaction
network and that SPT avoids the deuterium-based ω_b altogether
(arXiv:2609.12065) [src: Sect. 1]. The BAO + BBN H0 values and how BAO uses
the prior are held in `cosmo-galaxy-clustering` and
`cosmo-distance-ladder-h0`; with BBN nuisance parameters marginalised,
Akharman et al. find h = 0.6833 (+0.0048/−0.0053) from DESI DR2 BAO + BBN
in ΛCDM (arXiv:2609.12065) [src].

## 6. N_eff and new physics
<!-- key: neff-and-new-physics -->

BBN papers quote N_ν (baseline 3); CMB papers quote N_eff (baseline 3.044)
(arXiv:2207.13133) [src]. The synthesis of all N_eff bounds is in
`cosmo-neutrinos-dark-matter`; the rows below are those in which BBN data
enter.

| N_ν or N_eff | Data | Citation | Flag |
|---|---|---|---|
| ΔN_eff = −0.14 ± 0.21 | light elements alone, rates marginalised | Schöneberg 2024, arXiv:2401.15054 | [src] |
| N_eff = 3.41 ± 0.45 (95%) | Cooke D/H + Planck 2015 | arXiv:1710.11129 | [src: Eq. 16] |
| N_eff = 2.95 ± 0.16 | Kurichin Y_P + PDG D/H | arXiv:2101.09127 | [src] |
| N_eff = 2.85 ± 0.28 | PHLEK Y_P + Cooke D/H | arXiv:2005.12290 | [src] |
| N_eff = 2.54 (+0.20/−0.25) | EMPRESS XV Y_P | arXiv:2506.24050 | [src] |
| N_eff = 3.58 ± 0.25 | Izotov 2014 Y_P + D/H | arXiv:1408.6953 | [src] |
| N_ν = 2.86 ± 0.15 | BBN with CMB baryon density, lithium set aside, 2020 | Fields et al. 2020, arXiv:1912.01132 | [src] |
| N_ν = 2.880 ± 0.144 | BBN + Planck with LUNA rate | Yeh et al. 2021, arXiv:2011.13874 | [src] |
| N_ν = 2.898 ± 0.141; N_ν < 3.180 (2σ); −0.708 < N_ν^CMB − N_ν^BBN < 0.328 | BBN + CMB, 2022 | Yeh et al. 2022, arXiv:2207.13133 | [src] |
| N_ν = 2.925 ± 0.082; ΔN_ν ≤ 0.125 (95%, N_ν ≥ 3) | LBT Y_p + D/H + CMB | Yeh et al. 2026, arXiv:2601.22239 | [src] |
| N_eff = 2.990 ± 0.070; ΔN_eff < 0.107 (95%) | LBT Y_p + D/H + Planck + ACT + SPT + DESI BAO, no large-scale Planck polarisation | Goldstein & Hill 2026, arXiv:2603.13226 | [src] |
| N_eff = 2.974 (+0.098/−0.099) (BAO + BBN); 3.065 (+0.078/−0.076) (BAO + BBN + CMB) | DESI DR2 + Planck, BBN nuisances marginalised | Akharman et al. 2026, arXiv:2609.12065 | [src] |

Akharman et al. stress that N_eff from the joint analysis depends on the
reaction network, which the Yeh 2026 and Goldstein & Hill 2026 analyses do
not vary (arXiv:2609.12065) [src: Sect. 1].

**Other new physics.**

| Scenario | Limit or result | Citation | Flag |
|---|---|---|---|
| MeV-scale thermal relics | m_χ > 0.4 MeV (BBN, 2σ); electrophilic and neutrinophilic m_χ > 3.7 MeV (BBN + CMB) | Sabti et al. 2020, arXiv:1910.01649; addendum arXiv:2107.11232 | [src] |
| Electron-neutrino lepton asymmetry | ξ_νe = 0.043 ± 0.015 (no dark radiation), 0.046 ± 0.021 (free), driven by EMPRESS Y_P | Escudero et al. 2022, arXiv:2208.03201 | [src] |
| Lepton asymmetry from EMPRESS alone | ξ_e = 0.05 (+0.03/−0.02) (VIII); 0.05 (+0.02/−0.03) (XV) | arXiv:2203.09617; arXiv:2506.24050 | [src] |
| Expansion rate during D burning | ΔH/H = 0.087 (+0.036/−0.037) at T_D ≃ 0.03 MeV in an EDE cosmology; extra radiation does not reconcile Ω_b h² | Poulin et al. 2026, arXiv:2607.20635 | [src] |
| Long-lived decaying particles | hadronic and electromagnetic constraints for 0.01 s < τ < 10¹² s | Kawasaki, Kohri & Moroi 2005, arXiv:astro-ph/0408426; Jedamzik 2006, arXiv:hep-ph/0604251; update Bianco et al. 2026, arXiv:2605.26824 | [src] |
| Negative ΔN_eff | the usual N_eff fit is inconsistent for ΔN_eff < 0 unless neutrino-induced rates are adjusted | Ganguly, Jung & Yun 2025, arXiv:2507.23354 | [src] |
| Sensitivity atlas | 14 parameters and 63 rates in PRyMordial; with ΔN_eff free it dominates the Y_P theory error | Burns 2026, arXiv:2603.22414 | [src] |

Reviews of BBN as a probe of new physics: Pospelov & Pradler 2010
(arXiv:1011.1054) and Bertulani, Hall & Santoyo 2022 (arXiv:2210.04071)
[src: title and abstract read for 1011.1054; title only for 2210.04071].

## 7. Code and rate comparisons
<!-- key: code-and-rate-comparisons -->

Same data (Cooke et al. 2018 D/H and Aver et al. 2015 Y_P), ΛCDM, Ω_b h²
from light elements only (Schöneberg 2024, arXiv:2401.15054)
[src: Sect. 4.1, Table 1]:

| Code and rate set | Ω_b h² | Shift |
|---|---|---|
| PArthENoPE v2.0 (pre-LUNA d(p,γ)) | 0.02271 ± 0.00038 | — |
| PArthENoPE v3.0 (LUNA d(p,γ)) | 0.02236 ± 0.00034 | −0.9σ from v2.0 |
| PRyMordial, PRIMAT (ab-initio) rates | 0.02195 ± 0.00021 | ~1.0σ below v3.0, error ~40% smaller |
| PRyMordial, data-driven with marginalisation over rate errors | 0.02231 ± 0.00055 | covers all three |

With the PDG August 2023 abundances (10⁵ D/H = 2.547 ± 0.029,
Y_P = 0.2450 ± 0.0030) and rates marginalised, Ω_b h² = 0.02218 ± 0.00055
(ΛCDM) and 0.02196 ± 0.00063 (ΛCDM + N_eff), with ΔN_eff = −0.14 ± 0.21
from light elements alone (arXiv:2401.15054) [src; abundances from
Sect. 3, Table 1]. These reproduce the published PRIMAT and PArthENoPE
results (arXiv:2401.15054) [src: Sect. 4.1, footnote 8].

The three abundance compilations in use overlap strongly: "BAO+BBN papers"
(Cooke 2018 D/H, Aver 2015 Y_P = 0.2449 ± 0.0040), PDG August 2023, and
Yeh et al. 2022 (10⁵ D/H = 2.550 ± 0.030, Aver 2021 Y_P = 0.2448 ± 0.0033)
(arXiv:2401.15054) [src: Table 1].

Pitrou et al. (2021, arXiv:2011.11320) report a ≃1.8σ tension between the
baryon density from light elements and that from CMB + BAO with PRIMAT
rates [src]; Pisanti et al. (2021, arXiv:2011.11537) find D/H after LUNA
"in excellent agreement" with Planck [src]; Yeh, Olive & Fields (2021,
arXiv:2011.13874) find consistency with their data-driven rates [src]. The
split follows the rate treatment, not the code as software.

## 8. History: what superseded what
<!-- key: history-what-superseded-what -->

| Quantity | Earlier | Later | Citation | Flag |
|---|---|---|---|---|
| (D/H)_P | Cooke et al. earlier six-system mean | seven systems, 2.527 ± 0.030 (2018) | arXiv:1710.11129 | [src: Sect. V.1] |
| (D/H)_P | 2.527 ± 0.030 | eight systems, 2.533 ± 0.024 (2024) | arXiv:2401.12797 | [src] |
| Y_P from the HeBCD sample with He I 10830 | 0.2551 ± 0.0022 (Izotov et al. 2014) | 0.2449 ± 0.0040 (Aver et al. 2015, re-analysis of the Izotov, Thuan & Stasinska 2007 data with the 2014 He I 10830 observations) | arXiv:1408.6953; arXiv:1503.08146 | [src] |
| Y_P (LBT team) | 0.2449 ± 0.0040 (2015) | 0.2458 ± 0.0013 (2026, new LBT data) | arXiv:1503.08146; arXiv:2601.22238 | [src] |
| Y_P (EMPRESS) | 0.2370 (+0.0034/−0.0033) (2022) | 0.2402 ± 0.0040 (2025) | arXiv:2203.09617; arXiv:2506.24050 | [src] |
| d(p,γ)³He | Adelberger empirical or Marcucci ab-initio | LUNA 2020 | arXiv:1710.11129; doi:10.1038/s41586-020-2878-4 | [src: Sect. V.2] |
| PArthENoPE Ω_b h² | 0.02271 ± 0.00038 (v2.0) | 0.02236 ± 0.00034 (v3.0) | arXiv:2401.15054 | [src: Sect. 4.1] |
| N_ν, BBN + CMB | 2.86 ± 0.15 (2020); 2.880 ± 0.144 (2021) | 2.898 ± 0.141 (2022); 2.925 ± 0.082 (2026) | arXiv:1912.01132; arXiv:2011.13874; arXiv:2207.13133; arXiv:2601.22239 | [src] |
| N_eff with BBN + CMB + BAO | — | 2.990 ± 0.070 (2026) | arXiv:2603.13226 | [src] |
| NIST beam τ_n | 886.3 ± 1.2 ± 3.2 s (2005) | 887.7 ± 1.2 ± 1.9 s (2013) | arXiv:1309.2623 | [src] |
| J-PARC beam τ_n | first result (2020) | 877.2 ± 1.7 (+4.0/−3.6) s, five-fold better (2024) | arXiv:2007.11293; arXiv:2412.19519 | [src] |
| Y_P prediction | 0.24709 ± 0.00017 (PRIMAT 2018) | 0.24721 ± 0.00014 (PRIMAT 2021, CMB + BAO baryon density) | arXiv:1801.08023; arXiv:2011.11320 | [src: Table 2] |
| PDG concordance η | 4.7–6.5 × 10⁻¹⁰, N_ν = 3.24 ± 1.2 (95%) (2006) | 5.7–6.7 × 10⁻¹⁰, N_ν = 3.28 ± 0.28 (2014) | arXiv:astro-ph/0601514; arXiv:1412.1408 | [src] |

The "six-system mean" of the first row is stated as the previous estimate in
arXiv:1710.11129 [src: Sect. V.1]; its value was not read.

## Not verified
<!-- key: not-verified -->

- The 2024 PDG recommended D/H and Y_P are known here only as
  10⁵ D/H = 2.547 ± 0.029 and Y_P = 0.2450 ± 0.0030 through
  arXiv:2401.15054 (Table 1) [sec].
- The LUNA d(p,γ)³He Ω_b h² (doi:10.1038/s41586-020-2878-4) not read.
- The Sbordone et al. 2010 lithium plateau paper not read; its value enters
  via arXiv:2011.11320 Table 2.
- No ⁶Li results were collected.
