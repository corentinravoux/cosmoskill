# Results — neutrino mass, light relics and dark-matter properties from cosmological data

Scope: current headline constraints with dataset, model and provenance, then the history of each key number.
Snapshot: 2026-10-16

Flags: `[src]` read in the cited paper this session; `[sec]` taken from a named secondary source; `[der]` derived here, derivation stated.
All Σm_ν upper limits are 95% credible or confidence limits unless stated. "CMB" in DESI papers means Planck PR3 low-ℓ (SimAll, Commander) + PR4 CamSpec high-ℓ + Planck PR4 and ACT DR6 lensing (arXiv:2503.14744).

## 1. Sum of neutrino masses
<!-- key: sum-of-neutrino-masses -->

### 1.1 Laboratory anchors
<!-- key: laboratory-anchors -->

| Quantity | Value | Source | Flag |
|---|---|---|---|
| Minimum Σm_ν, normal ordering (lightest mass zero) | ≥ 0.059 eV | NuFIT 6.0 splittings as used by DESI, arXiv:2503.14744 §4.1; global fit is Esteban et al. 2024, arXiv:2410.05380 | [sec] |
| Minimum Σm_ν, inverted ordering | ≥ 0.10 eV | same | [sec] |
| Mass-ordering preference from oscillations alone | "almost equally good fit for both orderings"; Δχ² = 6.1 for normal ordering only when the Super-Kamiokande atmospheric table is added | arXiv:2410.05380 abstract | [src] |
| Effective electron-antineutrino mass, tritium endpoint | m_ν² = −0.14 (+0.13/−0.15) eV²; m_ν < 0.45 eV (90% CL), 259 days, 36 million electrons | KATRIN, Aker et al. 2024, arXiv:2406.13516 | [src] |
| Σm_ν implied by the KATRIN limit | ≲ 1.3 eV | Qu et al. 2026, arXiv:2607.24742 abstract | [sec] |
| KATRIN status, January 2026 review | "about to reach its target sensitivity of the neutrino mass of less than 300 meV"; next a keV sterile-neutrino search, then KATRIN++ with an atomic tritium source | Drexlin & Weinheimer 2026, arXiv:2601.00248 abstract | [src] |
| JUNO reactor oscillation parameters, 207.2 live days, 8,294 inverse-beta-decay candidates, mean baseline 52.5 km | Δm²_31 = +2.509 (+0.027/−0.025) × 10⁻³ eV² (normal) or −2.482 (+0.025/−0.026) × 10⁻³ eV² (inverted); sin²θ_12 = 0.3036 ± 0.0064; Δm²_21 = (7.388 ± 0.078) × 10⁻⁵ eV² | JUNO Collaboration 2026, arXiv:2609.37895 abstract | [src] |
| Mass ordering from JUNO + long-baseline accelerator Δm²_31 | normal ordering favoured at ≥ 2.1σ (one-sided) for all CP phases; Bayes factor 10.18 | arXiv:2609.37895 abstract | [src] |
| Neutrinoless double beta decay, ¹³⁶Xe, complete KamLAND-Zen data (2.1 ton yr) | T_1/2 > 3.8 × 10²⁶ yr (90% CL); effective Majorana mass m_ββ < 28–122 meV depending on the nuclear matrix element | Abe et al. 2024, arXiv:2406.11438 abstract | [src] |
| Lowest m_ββ in the inverted ordering, the target for next-generation searches | 18 meV | arXiv:2503.14454 §6.1.1 | [sec] |

The three laboratory observables are different combinations of the masses: oscillations give splittings, KATRIN an incoherent sum weighted by electron-flavour mixing, double beta decay a coherent sum that exists only for Majorana neutrinos. None of them is Σm_ν. The KATRIN best-fit m_ν² is itself negative; this is a statistical statement about an endpoint fit, unrelated to the cosmological "negative mass" discussed below.

### 1.2 Cosmological upper limits, ΛCDM + Σm_ν (prior Σm_ν > 0, three degenerate states)
<!-- key: cosmological-upper-limits-lambdacdm-sigmamnu -->

| Dataset | Σm_ν (95%) | Citation | Flag |
|---|---|---|---|
| Planck 2018 (TT,TE,EE+lowE+lensing+BAO) | < 0.12 eV | Planck Collaboration 2018, arXiv:1807.06209 abstract | [src] |
| DESI DR1 BAO + CMB | < 0.070 eV ("70 meV") | quoted by Craig et al. 2024, arXiv:2405.00836 | [sec] |
| Planck 2018 + ACT lensing + DESI DR1 | < 0.072 eV | quoted by Naredo-Tuero et al. 2024, arXiv:2407.13831 | [sec] |
| DESI DR2 BAO + CMB (baseline, CamSpec) | < 0.0642 eV, σ(Σm_ν) = 0.020 eV | Elbers et al. 2025, arXiv:2503.14744; companion DESI Collaboration 2025, arXiv:2503.14738 | [src] |
| DESI DR2 BAO + CMB (Planck PR4 LoLLiPoP-HiLLiPoP, "L-H") | < 0.0774 eV | arXiv:2503.14744 Table 2 | [src] |
| DESI DR2 BAO + CMB (Planck PR3 plik) | < 0.0691 eV | arXiv:2503.14744 Table 2 | [src] |
| DESI DR2 BAO + CMB + Pantheon+ / Union3 / DESY5 | < 0.0704 / 0.0674 / 0.0744 eV | arXiv:2503.14744 Table 2 | [src] |
| DESI DR2 BAO + CMB, Feldman–Cousins (profile likelihood) | < 0.053 eV; parabola minimum μ0 = −0.036 eV, σ = 0.043 eV | arXiv:2503.14744 Table 3 | [src] |
| DESI DR1 (FS+BAO) + BBN + loose n_s prior, no CMB amplitude | < 0.373 eV (Feldman–Cousins), σ = 0.200 eV | arXiv:2503.14744 Table 3 | [src] |
| P-ACT-LB (ACT DR6 + Planck + lensing + DESI Year-1 BAO), three massive species | < 0.089 eV | Calabrese et al. 2025, arXiv:2503.14454 §6.1.1 of the revised source, Eq. 33; the abstract returned by the arXiv API (re-checked 2026-10-14) still reads 0.082 eV, while the abstract of the HTML rendering reads 0.089 eV | [src] |
| W-ACT-LB (WMAP in place of Planck) | < 0.088 eV | arXiv:2503.14454 §6.1.1 | [src] |
| P-ACT + lensing + BOSS BAO in place of DESI | < 0.13 eV | arXiv:2503.14454 §6.1.1 | [src] |
| P-ACT + lensing + supernovae, no BAO | < 0.23 eV | arXiv:2503.14454 §6.1.1 | [src] |
| Planck + lensing + DESI DR1, as quoted by ACT | < 0.077 eV; ACT attributes it to the DESI DR1 paper, whose own value is 0.072 eV (§8.1), so the two differ in the CMB likelihood or lensing data | arXiv:2503.14454 §6.1.1 | [sec] |
| Planck + Planck and ACT lensing + DESI BAO, standard thermal history (independent analysis) | < 0.0691 eV | Figueroa, Sobotka & Erickcek 2026, arXiv:2609.15970 abstract | [src] |
| Same, neutrino-to-photon temperature ratio free | < 0.0724 eV | arXiv:2609.15970 abstract | [src] |
| SPT-3G D1 lensing + CMB + BAO | < 0.072 eV | Omori et al. 2026, arXiv:2608.31136 abstract | [src] |
| SPT-3G D1 + DESI DR2 BAO; CMB-SPA + DESI DR2 (τ prior 0.051 ± 0.006) | < 0.081 eV; < 0.055 eV; the latter "appears to rule out" normal and inverted orderings at 96.6% and 99.9%, Δχ² = 5.1 (2.3σ) against the normal-ordering minimum | Camphuis et al. 2025, arXiv:2506.20707 Sect. VII.4.6, Eqs. 105–106 | [src] |
| Planck + CMB lensing + DESI DR2 BAO (Qu et al. restatement) | < 0.056 eV | arXiv:2607.24742 abstract | [src] |
| DESI DR1 full shape + bispectrum + cross-correlations + DESI BAO + CMB + SNe (EFT reanalysis, not a DESI Collaboration result) | < 0.049 eV | Ivanov et al. 2026, arXiv:2601.16165 abstract | [src] |
| Planck + DESI BAO (2024 release) + SNe Ia + gamma-ray bursts + cosmic chronometers + galaxy-cluster distances (external analysis; each added background probe tightens the limit through a higher H0) | < 0.043 eV (2σ) | Wang et al. 2024, arXiv:2405.03368 abstract | [src] |
| CMB + DESI + several late-time background probes, no local H0 prior | < 0.05 eV | Jiang et al. 2024, arXiv:2407.18047 abstract | [src] |

Reading rule: the spread 0.049–0.089 eV among the CMB + DESI rows of this table is driven by the Planck high-ℓ likelihood, the lensing data, the BAO release and the supernova sample, not by a change in sensitivity. The Bayesian limit is tighter than its own marginalised error would suggest because the posterior peaks at the prior edge (arXiv:2503.14744 §5).

### 1.3 Dependence on the dark-energy model (DESI DR2 BAO + CMB, arXiv:2503.14744 Table 2, all [src])
<!-- key: dependence-on-the-dark-energy-model-desi-dr2 -->

| Model | Data | Σm_ν (95%) |
|---|---|---|
| wCDM | BAO + CMB | < 0.0851 eV |
| wCDM | + Pantheon+ / Union3 / DESY5 | < 0.0653 / 0.0649 / 0.0586 eV |
| w0waCDM | BAO + CMB | < 0.163 eV |
| w0waCDM | + Pantheon+ / Union3 / DESY5 | < 0.117 / 0.139 / 0.129 eV |
| w0waCDM, Feldman–Cousins | BAO + CMB | < 0.177 eV (μ0 = +0.024 eV, σ = 0.078 eV) |
| w0waCDM, Feldman–Cousins | BAO + CMB + DESY5 | < 0.126 eV (μ0 = −0.007 eV, σ = 0.068 eV) |

Constant-w dark energy tightens the limit with supernovae (w > −1 worsens the BAO–CMB mismatch, which smaller masses compensate); only a time-varying equation of state relaxes it (arXiv:2503.14744 §4.1).

Independent analyses in extended dark-energy models:

| Result | Value | Citation | Flag |
|---|---|---|---|
| (w0, wa) marginalised, also stable under binned and cubic w(a) | Σm_ν < 0.152 eV | Qu et al. 2026, arXiv:2607.24742 | [src] |
| Late-Universe-free route: primary CMB with A_lens marginalised + reconstructed lensing spectrum | Σm_ν < 0.41 eV | arXiv:2607.24742 | [src] |
| w0waCDM, DESI DR1 full shape + bispectrum + BAO + CMB + SNe | Σm_ν < 0.077 eV; stated to be 37% tighter than background data alone | Ivanov et al. 2026, arXiv:2601.16165 | [src] |
| Sign-switching Λ_sCDM, DESI DR2 BAO + CMB + DES-Dovekie SNe | Σm_ν,eff = 0.055 ± 0.050 eV (68%), against −0.075 (+0.039/−0.053) eV in ΛCDM for the same data; transition redshift z† > 2.4 (95%) | Kıbrıs et al. 2026, arXiv:2605.21456 | [src] |

### 1.4 Effective (signed) neutrino mass and the tension with oscillations
<!-- key: effective-signed-neutrino-mass-and-the-tension -->

| Analysis | Data | Result (68%) | Stated tension | Citation | Flag |
|---|---|---|---|---|---|
| Clustering-suppression-only extension to negative values | DESI DR1 BAO + CMB | Σm_ν = −160 ± 90 meV; minimum-mass suppression excluded at 99% | — | Craig et al. 2024, arXiv:2405.00836 | [src] |
| Effective mass consistent in background and perturbations | Planck + ACT + DESI DR1 | Σm_ν,eff = −0.125 (+0.058/−0.070) eV [sec, quoted in arXiv:2503.14744] | 2.8–3.3σ with oscillations | Elbers et al. 2024, arXiv:2407.10965 | [src] for the tension |
| Same parameter | DESI DR2 BAO + CMB | Σm_ν,eff = −0.101 (+0.047/−0.056) eV; σ = 0.053 eV, 2.6 times the baseline Bayesian σ | 3σ with the oscillation lower limit | arXiv:2503.14744 | [src] |
| Same, w0waCDM and mirage dark energy | Planck + ACT + DESI DR1 | Σm_ν,eff = 0.06 (+0.15/−0.10) eV and 0.04 (+0.15/−0.11) eV | none | arXiv:2407.10965 | [src] |
| Effective mass plus two lensing parameters (peak smoothing and lensing-potential amplitude) | Planck, Planck + ACT lensing, DESI | Σm̃_ν = −0.018 (+0.085/−0.089) eV | none | Cozzumbo et al. 2025, arXiv:2511.01967 | [src] |
| Range across dataset combinations and tension metrics | CMB + DESI DR1 + background probes | — | 2.5σ to 5σ | Jiang et al. 2024, arXiv:2407.18047 | [src] |

### 1.5 The optical-depth route
<!-- key: the-optical-depth-route -->

| Result | Value | Citation | Flag |
|---|---|---|---|
| τ preferred by DESI BAO + high-ℓ CMB + CMB lensing in ΛCDM, no low-ℓ EE | 0.090 ± 0.012, 3–5σ from Planck low-ℓ polarisation | Sailer et al. 2025, arXiv:2504.16932 | [src] |
| Same question, independent analysis | τ = 0.091 ± 0.011; neutrino tension at Σm_ν = 0.06 eV removed; w0wa preference below 95% CL | Jhaveri, Karwal & Hu 2025, arXiv:2504.21813 | [src] |
| With τ ≈ 0.09 | w0wa preference falls from about 3σ to 1.4σ (Δχ²_MAP = −3.82) [src: Sect. III.2]; n_s = 0.968 ± 0.004, H0 = 67.94 ± 0.44 km/s/Mpc | arXiv:2504.16932 | [src] |
| DESI DR2 BAO + CMB, τ fixed at 0.067 or 0.074 (about 2σ or 3σ above the baseline 0.054 ± 0.007) | tension of Σm_ν,eff with oscillations remains at 2.3σ or 1.7σ; without large-scale polarisation the tension "could be explained as a ∼2σ statistical fluctuation" | arXiv:2503.14744 §5.2.1 | [src] |
| P-ACT-LB with the SRoll2 error doubled, prior τ = 0.057 ± 0.012 | Σm_ν < 0.10 eV | arXiv:2503.14454 appendix on DESI DR2 and τ | [src] |
| P-ACT-LB without SRoll2 (τ from lensing in the spectra) | Σm_ν < 0.19 eV | same | [src] |
| τ preferred by P-ACT-LB with DESI DR2; τ measured without SRoll2 (P-ACT-LB with DR2 and supernovae) | 0.0643 (+0.0055/−0.0067); 0.081 ± 0.016 | same | [src] |
| Imposed prior τ = 0.11 ± 0.006 | Σm_ν = 0.10 (+0.04/−0.05) eV (68%), presented as a 2σ detection conditional on the prior | Sullivan, de Belsunce & Ivanov 2026, arXiv:2606.30903 | [src] |

The τ values measured from Planck large-scale polarisation, and the evidence from reionisation data, are held in `cosmo-cmb` and `cosmo-reionization-21cm`; the high-τ numbers above are what the neutrino sector would need, not measurements of τ.

### 1.6 Mass ordering from cosmology
<!-- key: mass-ordering-from-cosmology -->

| Statement | Value | Citation | Flag |
|---|---|---|---|
| Posterior probability of normal ordering, ΛCDM, DESI DR2 BAO + CMB + NuFIT 6.0, equal prior odds | P(NO) = 0.91, Bayes factor K = 10 (K = 6 with L-H, K = 8 with plik) | arXiv:2503.14744 §4.3 | [src] |
| Frequentist counterpart | χ²(IO) − χ²(NO) = 4.6 | arXiv:2503.14744 §5.1 | [src] |
| Lightest mass | m_l < 0.023 eV (NO or free ordering), < 0.024 eV (IO) | arXiv:2503.14744 | [src] |
| Σm_ν with oscillation prior | < 0.101 eV (NO), < 0.133 eV (IO) | arXiv:2503.14744 | [src] |
| Earlier Bayes factor, CMB + DESI DR1 + background probes | 46.5 | arXiv:2407.18047 | [src] |
| Alternative prior constructions | K > 460 in ΛCDM, K > 40 in extensions; prior measure changes K by a factor of about 10 | Jimenez et al. 2026, arXiv:2606.18987 | [src] |
| EFT reanalysis | inverted ordering disfavoured at about 3.5σ (ΛCDM) and 2.4σ (w0waCDM) | arXiv:2601.16165 | [src] |

The Bayes factors 10, 46.5 and > 460 use the same class of data. The difference is the prior on the masses and the data combination; see `open-questions.md` §1.4.

## 2. N_eff, light relics and BBN
<!-- key: neff-light-relics-and-bbn -->

### 2.1 Standard-Model value
<!-- key: standard-model-value -->

| Statement | Value | Citation | Flag |
|---|---|---|---|
| N_eff with full collision term, flavour oscillations and QED plasma corrections | 3.0440 | Froustey, Pitrou & Volpe 2020, arXiv:2008.01074 | [src] |
| Finite-temperature QED: O(e²) correction δN_eff ≃ +0.010, O(e³) ≃ −0.001; expected to move 3.044 to 3.043 | — | Bennett et al. 2019, arXiv:1911.04504 | [src] |

The reference value used by DESI, ACT and SPT is 3.044 (arXiv:2503.14744, arXiv:2506.20707). A text quoting 3.046 is using the pre-2020 value, which is the one in Planck 2018 (arXiv:1807.06209 Sect. 7.5.2 [src]). It comes from Mangano 2005 (arXiv:hep-ph/0506164 [src]), who obtained N_eff = 3.046 with three-flavour oscillations in the decoupling calculation.

### 2.2 Measurements (ΛCDM + N_eff, 68% unless stated)
<!-- key: measurements-lambdacdm-neff-68-unless-stated -->

| Dataset | N_eff | Citation | Flag |
|---|---|---|---|
| Planck 2018 + BAO | 2.99 ± 0.17 | arXiv:1807.06209 abstract | [src] |
| ACT DR6 alone | 2.60 (+0.21/−0.29) | arXiv:2503.14454 §6.1.1 | [src] |
| P-ACT (ACT DR6 + Planck) | 2.73 ± 0.14 | arXiv:2503.14454 §6.1.1 | [src] |
| ACT DR6 + Planck + lensing + DESI Year-1 BAO (P-ACT-LB) | 2.86 ± 0.13; with external BBN data 2.89 ± 0.11; one-tail N_eff < 3.08 (95%) | arXiv:2503.14454 abstract and §6.1.1 | [src] |
| P-ACT-LB with DESI DR2 in place of DR1 | 2.92 ± 0.12 | arXiv:2503.14454 appendix | [src] |
| P-ACT-LB, N_eff and Σm_ν both free | 2.85 ± 0.25 (95%), Σm_ν < 0.073 eV | arXiv:2503.14454 §6.1.1 | [src] |
| Extra species only (N_eff ≥ 3.044) | ΔN_eff < 0.32 (ACT), < 0.14 (P-ACT), < 0.17 (P-ACT-LB), 95% | arXiv:2503.14454 §6.1.1 | [src] |
| SPT-3G D1 alone | 3.18 (+0.29/−0.33) | Camphuis et al. 2025, arXiv:2506.20707 Table 5 (HTML v2) | [src] |
| SPT + ACT | 2.78 ± 0.17 | same | [src] |
| CMB-SPA (SPT + Planck + ACT) | 2.82 ± 0.12 | same | [src] |
| SPT-3G D1 + DESI | 3.53 ± 0.23 | same | [src] |
| DESI DR2 BAO + CMB (Planck CamSpec + lensing) | 3.23 ± 0.18 (68%); 3.23 (+0.35/−0.34) (95%) | arXiv:2503.14744 | [src] |
| DESI DR2 BAO + CMB, Σm_ν free | 3.16 ± 0.17, Σm_ν < 0.0741 eV; correlation ρ = 0.18 | arXiv:2503.14744 | [src] |
| DESI DR2 BAO + CMB + DESY5, w0waCDM | 3.01 ± 0.19 | arXiv:2503.14744 Table 2 | [src] |
| Self-interacting dark radiation | N_idr < 0.134 (95%) | arXiv:2503.14454 abstract | [src] |
| Self-interacting dark radiation with running and running-of-running free; Planck + ACT DR6 + DESI DR2 + uncalibrated Pantheon+ | ΔN_eff < 0.58 (95%); < 0.68 with dark-radiation–matter decoupling | Garny, Niedermann & Sloth 2026, arXiv:2604.26541 | [src] |

Every CMB-only value is within 2σ of 3.044 (arXiv:2506.20707 [src]). CMB-only values sit below 3.044 and values with DESI BAO sit above it: BAO prefer larger H0 r_d and smaller Ω_m, which N_eff absorbs (arXiv:2503.14744 §4.2). `cosmo-cmb` warns that in ΛCDM + N_eff the CMB and BAO disagree at more than 3σ for some CMB combinations, so the combined number should not be quoted without that caveat.

### 2.3 BAO phase shift
<!-- key: bao-phase-shift -->

| Statement | Value | Citation | Flag |
|---|---|---|---|
| Phase-shift amplitude β_φ > 0, DESI DR1 BAO, combined tracers | 1.6σ | Whitford et al., as reported in arXiv:2503.14744 §4.2 | [sec] |
| Same with DESI DR2 BAO | 2.6σ | arXiv:2503.14744 §4.2 | [src] |

The phase shift is produced by free-streaming radiation travelling faster than the plasma sound speed and cannot be mimicked by other standard parameters for adiabatic initial conditions (Bashinsky & Seljak 2003, arXiv:astro-ph/0310198). It is the only N_eff signature in BAO that does not pass through the expansion rate; on its own it gives no useful N_eff constraint yet (arXiv:2503.14744).

### 2.4 BBN
<!-- key: bbn -->

| Quantity | Value | Citation | Flag |
|---|---|---|---|
| Primordial deuterium | (D/H)_P = (2.527 ± 0.030) × 10⁻⁵, seven systems | Cooke, Pettini & Steidel 2017, arXiv:1710.11129 | [src] |
| Predicted helium mass fraction, standard BBN | Y_P = 0.24709 ± 0.00017 (PRIMAT) | Pitrou et al. 2018, arXiv:1801.08023 | [src] |
| Measured primordial helium, LBT Y_p Project | Y_p = 0.2458 ± 0.0013, stated to be the most precise to date | Yeh et al. 2026, arXiv:2601.22239 | [src] |
| Baryon density, Y_p + D/H + BBN + CMB, N_ν = 3 | η = (6.120 ± 0.038) × 10⁻¹⁰, Ω_b h² = 0.02236 ± 0.00014 | arXiv:2601.22239 | [src] |
| N_ν, BBN + CMB | 2.925 ± 0.082; ΔN_ν ≤ 0.125 (95%, for N_ν ≥ 3) | arXiv:2601.22239 | [src] |
| N_ν, BBN + CMB, earlier | 2.898 ± 0.141; N_ν < 3.180 (2σ) | Yeh et al. 2022, arXiv:2207.13133 | [src] |
| Change between epochs | −0.708 < N_ν^CMB − N_ν^BBN < 0.328 | arXiv:2207.13133 | [src] |
| Baryon density from light elements with nuclear rates marginalised (PRyMordial) | Ω_b h² = 0.02218 ± 0.00055 (ΛCDM); 0.02196 ± 0.00063 (+N_eff) | Schöneberg 2024, arXiv:2401.15054 | [src] |
| ΔN_eff from light elements alone | −0.14 ± 0.21 | arXiv:2401.15054 | [src] |

The BBN baryon density depends on the deuterium-burning rates: ab-initio theoretical rates favour lower Ω_b h², experimentally determined rates higher (arXiv:2401.15054). A "BBN prior" in a BAO analysis therefore names a code and a rate set, not a single number; `cosmo-distance-ladder-h0` holds the BAO + BBN H0 results.

## 3. Warm dark matter (thermal-relic mass, 95% lower limits unless stated)
<!-- key: warm-dark-matter-thermal-relic-mass-95-lower -->

All limits are for a thermal relic making up all of the dark matter. A limit on another candidate (sterile neutrino, non-thermal production) needs a model-specific translation of the cutoff scale and is not obtained by quoting the same number.

### 3.1 Lyman-α forest
<!-- key: lyman-alpha-forest -->

| Data | m_WDM | Thermal-history assumption, k_max | Citation | Flag |
|---|---|---|---|---|
| Kim et al. and Croft et al. spectra + WMAP | > 0.55 keV (thermal), > 2.0 keV (sterile neutrino), 2σ | — | Viel et al. 2005, arXiv:astro-ph/0501562 | [src] |
| 25 quasars at z > 4, HIRES + MIKE | > 3.3 keV (2σ) | several physically motivated thermal histories | Viel et al. 2013, arXiv:1306.2314 | [src] |
| Same spectra, wider range of thermal histories | no limit: warm and cold models fit the cutoff equally well | — | Garzilli, Boyarsky & Ruchayskiy 2015, arXiv:1510.07006 | [src] |
| XQ-100 alone / HIRES+MIKE alone / combined | > 1.4 / 4.1 / 5.3 keV (2σ) | T(z) a power law in redshift | Iršič et al. 2017, arXiv:1702.01764 | [src] |
| XQ-100 + HIRES/MIKE, temperature jumps up to 5000 K allowed | > 3.5 keV (2σ) | non-smooth T(z) | arXiv:1702.01764 | [src] |
| SDSS DR14 (z < 4.5) + XQ-100 | > 5.3 keV | — | Palanque-Delabrouille et al. 2019, arXiv:1911.09073 | [src] |
| High-resolution spectra, coldest reionisation histories allowed by data | > 1.9 keV | cold histories; limit set by position of the flux-power maximum | Garzilli et al. 2019, arXiv:1912.09397 | [src] |
| Boera et al. 2019 spectra, 4.0 ≲ z ≲ 5.2, 1080 Cholla simulations | > 3.1 keV; peak likelihood at 4.5 keV | wide range of thermal histories | Villasenor et al. 2022, arXiv:2209.14220 | [src] |
| HIRES + UVES, z = 4.2–5.0 | > 5.7 keV | k_max = 0.2 s/km, inhomogeneous reionisation included | Iršič et al. 2023, arXiv:2309.04533 | [src] |
| Same, restricted to earlier scales and priors | > 4.1 keV | k_max < 0.1 s/km | arXiv:2309.04533 | [src] |

The range 1.9–5.7 keV matches what `cosmo-lyman-alpha` quotes; that skill holds the data and emulator side.

### 3.2 Milky Way satellites, strong lensing, stellar streams, and combinations
<!-- key: milky-way-satellites-strong-lensing-stellar -->

| Probe | m_WDM | Notes | Citation | Flag |
|---|---|---|---|---|
| Milky Way satellites, DES + Pan-STARRS1 | > 6.5 keV (free-streaming length ≲ 10 h⁻¹ kpc) | marginalised over galaxy–halo connection, Milky Way mass, disk disruption | Nadler et al. 2020, arXiv:2008.00022 | [src] |
| Milky Way + M31 satellites (DES, PS1, PAndAS) | > 6.20 keV (95%); > 5.75 keV (20:1 posterior ratio) | not a collaboration analysis | Liu, Gong & Liao 2025, arXiv:2512.01361 | [src] |
| 8 quadruply imaged quasars, flux ratios | > 5.2 keV (m_hm < 10^7.8 M⊙) | — | Gilman et al. 2019, arXiv:1908.06983 | [src] |
| 31 lensed quasars, JWST MIRI flux ratios | > 5.6 keV (m_hm < 10^7.8 M⊙, Galacticus subhalo prior) or > 6.4 keV (m_hm < 10^7.6 M⊙, N-body prior), Bayes factor 10:1 | — | Keeley et al. 2025, arXiv:2511.07765 | [src] |
| 28 quads, JWST, flux ratios + extended arcs | > 6.5 keV (m_hm < 10^7.4 M⊙, Galacticus) or > 7.4 keV (m_hm < 10^7.2 M⊙, N-body), Bayes factor 10:1; free-streaming length < 7.0 or < 6.0 kpc | 0.4 dex gain from the arcs | Gilman et al. 2025, arXiv:2511.07513; Gilman et al. 2026, arXiv:2606.05277 | [src] |
| GD-1 and Pal 5 streams | > 3.6 keV streams alone; > 6.2 keV with dwarf satellite counts | — | Banik et al. 2019, arXiv:1911.02663 | [src] |
| Lensing (extended sources) + Lyα + Milky Way satellites | > 6.048 keV (λ_hm < 0.089 Mpc/h, M_hm < 3 × 10⁷ M⊙/h); a likelihood-ratio 1/20 criterion gives 2.552 keV | — | Enzi et al. 2020, arXiv:2010.13802 | [src] |
| Lensing flux ratios + Milky Way satellites, joint | > 9.7 keV (M_hm < 10^7.0 M⊙); 7.4 keV disfavoured 20:1 | stated 30% gain over each probe alone | Nadler et al. 2021, arXiv:2101.07810 | [src] |
| Galaxy ultraviolet luminosity functions, JWST z = 9–14.5 with HST z = 4–8 | ≥ 3.2 keV | marginalised over star-formation-efficiency parameters | Liu, Shan & Zhang 2024, arXiv:2404.13596 | [src] |

Two JWST lensing numbers circulate (5.6/6.4 keV and 6.5/7.4 keV). They come from the same survey: the first uses flux ratios only, the second adds the lensed arcs. Each has two values because the subhalo-abundance prior differs.

### 3.3 Sterile-neutrino dark matter and the 3.5 keV line
<!-- key: sterile-neutrino-dark-matter-and-the-3-5-kev -->

| Statement | Citation | Flag |
|---|---|---|
| Unidentified line at E = (3.55–3.57) ± 0.03 keV in a stack of 73 clusters; if all dark matter is a 7.1 keV sterile neutrino, sin²(2θ) = 7 × 10⁻¹¹ | Bulbul et al. 2014, arXiv:1402.2301 | [src] |
| No line in more than 30 Ms of XMM-Newton blank-sky data; decaying-dark-matter origin stated to be excluded | Dessert, Rodd & Safdi 2018, arXiv:1812.06976 | [src] |
| Rebuttals: the limit relaxes by a factor of about 20 (Abazajian 2020, arXiv:2004.06170) or by more than an order of magnitude (Boyarsky et al. 2020, arXiv:2004.06601) under different background modelling; the original authors replied and maintained the exclusion (reply read this session, not listed in `sources.tsv`) | — | [src] |
| Structure-formation side: the 7.1 keV sterile neutrino is ruled out for lepton asymmetries L6 > 10 | arXiv:2010.13802 | [src] |

## 4. Fuzzy / ultralight dark matter
<!-- key: fuzzy-ultralight-dark-matter -->

### 4.1 All of the dark matter (lower limits on the boson mass)
<!-- key: all-of-the-dark-matter-lower-limits-on-the -->

| Probe | Limit | Citation | Flag |
|---|---|---|---|
| Lyα, XQ-100 + HIRES/MIKE | > 20 × 10⁻²² eV (2σ) allowing temperature jumps; > 37.5 × 10⁻²² eV for a power-law thermal history | Iršič et al. 2017, arXiv:1703.04683 | [src] |
| Lyα, emulator of hydrodynamical simulations | > 2 × 10⁻²⁰ eV (95%) | Rogers & Peiris 2020, arXiv:2007.12705 | [src] |
| Lyα P1D at z = 4.2, 4.6, 5.0, neural-network emulator | > 1.9 × 10⁻²¹ eV (95%) | Liu, Gong & Zhou 2026, arXiv:2606.06969 | [src] |
| Milky Way satellites (DES + PS1) | > 2.9 × 10⁻²¹ eV (95%) | arXiv:2008.00022 | [src] |
| Milky Way + M31 satellites | > 1.74 × 10⁻²⁰ eV (95%) | arXiv:2512.01361 | [src] |
| Stellar streams (GD-1, Pal 5) | > 1.4 × 10⁻²¹ eV; > 2.2 × 10⁻²¹ eV with satellite counts | arXiv:1911.02663 | [src] |
| Sizes and stellar kinematics of Segue 1 and Segue 2 (dynamical heating by granules) | > 3 × 10⁻¹⁹ eV (99%) | Dalal & Kravtsov 2022, arXiv:2203.05750 | [src] |
| Stellar kinematics of Leo II, wavefunction reconstruction | > 2.2 × 10⁻²¹ eV (95%), independent of cosmology and production mechanism | Zimmermann et al. 2024, arXiv:2405.20374 | [src] |
| One VLBI lensed arc at < 5 mas resolution | m ≤ 4.4 × 10⁻²¹ eV excluded at 20:1 posterior odds; vector case > 1.4 × 10⁻²¹ eV | Powell et al. 2023, arXiv:2302.10941 | [src] |
| Warm-wave dark matter with a subhorizon field spectrum peaked at k* | m > 6 × 10⁻¹⁸ eV (k*/10⁴ Mpc⁻¹) for k* > 10⁴ Mpc⁻¹ | Nadler et al. 2026, arXiv:2605.15371 | [src] |

The Lyα lower limits differ by an order of magnitude (1.9 × 10⁻²¹ to 2 × 10⁻²⁰ eV) across analyses of comparable high-redshift data; the 2026 paper marginalises over intergalactic-medium parameters with its own emulator and is the weakest of the three.

### 4.2 Sub-component (upper limits on the axion fraction or density)
<!-- key: sub-component-upper-limits-on-the-axion -->

| Mass range | Limit (95%) | Data | Citation | Flag |
|---|---|---|---|---|
| 10⁻³² ≤ m ≤ 10⁻²⁵·⁵ eV | Ω_a/Ω_d < 0.05, Ω_a h² < 0.006 | WMAP, Planck, ACT, SPT, WiggleZ | Hložek et al. 2014, arXiv:1410.2896 | [src] |
| m ≤ 10⁻²⁶ eV; 10⁻³⁰ ≤ m ≤ 10⁻²⁸ eV | < 10% of the dark matter; < 1% | Planck 2018 + BOSS power spectrum and bispectrum | Rogers et al. 2023, arXiv:2301.08361 | [src] |
| m ≈ 10⁻²⁹ eV | as low as 0.3% of the total matter density | DESI DR1 full shape + Planck + ACT | Verdiani et al. 2026, arXiv:2607.11876 | [src] |
| m = 10⁻²⁶ eV; 10⁻²⁵ eV | < 1.5%; < 9% of the dark matter | Planck, ACT and SPT-3G CMB lensing, non-linear axion model | Laguë et al. 2026, arXiv:2606.06410 | [src] |
| log10(m/eV) = −23, −22, −21 | f_FDM < 0.07, 0.12, 0.65 | Lyα P1D, z = 4.2–5.0 | arXiv:2606.06969 | [src] |

Hints that did not survive combination: BOSS alone preferred axions at 2.7σ for m = 10⁻²⁶ eV (arXiv:2301.08361); the DESI luminous red galaxy sample shows a mild preference at the same mass that vanishes with CMB data (arXiv:2607.11876); ACT lensing shows a 2.1σ preference at 10⁻²⁴·⁵ eV driven by a few data points (arXiv:2606.06410).

## 5. Interacting dark matter (95% upper limits)
<!-- key: interacting-dark-matter-95-upper-limits -->

| Interaction | Limit | Data | Citation | Flag |
|---|---|---|---|---|
| Dark matter–proton, velocity-independent, spin-independent | σ < 5.3 × 10⁻²⁷ cm² (1 keV), 3.0 × 10⁻²⁶ cm² (1 MeV), 1.7 × 10⁻²⁵ cm² (1 GeV), 1.6 × 10⁻²³ cm² (1 TeV) | Planck temperature, polarisation and lensing | Gluscevic & Boddy 2017, arXiv:1712.07133 | [src] |
| Dark matter–baryon, velocity-independent | σ < 2 × 10⁻²⁹ cm² (10 keV), 6 × 10⁻²⁷ cm² (10 GeV); scaling m^1/4 below 1 GeV and m above | Milky Way satellite population | Nadler et al. 2019, arXiv:1904.10000 | [src] |
| Dark matter–proton, velocity-independent | σ0 < 8.8 × 10⁻²⁹ cm² for a 100 MeV particle | Milky Way satellites, DES + PS1 | arXiv:2008.00022 | [src] |
| Dark matter–proton, σ = σ0 (v/c)ⁿ, 1 MeV particle | σ0 < 1.1 × 10⁻²⁵ cm² (n = 2), 2.1 × 10⁻²² cm² (n = 4); for n = 0 within an order of magnitude of the Lyα and satellite limits | HST ultraviolet luminosity functions, z ≈ 4–10, blank and lensed fields, + Planck + Pantheon | Lazare et al. 2025, arXiv:2510.10757 | [src] |
| Dark matter–neutrino | u_νχ ≤ 1.5 × 10⁻⁸; stated to exclude earlier hints of non-zero interaction | high-resolution Lyα forest, dedicated hydrodynamical simulations | Mosbech et al. 2026, arXiv:2607.15020 | [src] |
| Dark matter–dark radiation | ETHOS-4 model excluded at the inferred 95 percentiles | lensing + Lyα + satellites | arXiv:2010.13802 | [src] |
| Collisionless dark matter, only a small axion-like fraction allowed | consistent | ACT DR6 + Planck | arXiv:2503.14454 | [src] |

The CMB limits and the satellite limits on the same cross section differ by orders of magnitude because the satellites probe smaller scales (arXiv:1904.10000). Mapping a warm-dark-matter mass limit onto an interacting model through the half-mode scale overestimates the constraint for dark matter–neutrino scattering (arXiv:2607.15020).

## 6. Self-interacting dark matter (cross section per unit mass)
<!-- key: self-interacting-dark-matter-cross-section-per -->

| System, relative velocity | Result | Citation | Flag |
|---|---|---|---|
| Bullet Cluster 1E 0657-56, offset method | σ/m < 1.25 cm²/g (68%) | Randall et al. 2007, arXiv:0704.0261 | [src] |
| Bullet Cluster, mass-to-light ratio argument | σ/m < 0.7 cm²/g | arXiv:0704.0261 | [src] |
| Bullet Cluster re-simulated | constraint depends more on how positions are measured than on initial conditions; earlier tight limits overstated | Robertson, Massey & Eke 2016, arXiv:1605.04307 | [src] |
| 72 cluster collisions, dark matter–star offset 5.8 ± 8.2 kpc | σ/m < 0.47 cm²/g (95%) | Harvey et al. 2015, arXiv:1503.07675 | [src] |
| Relaxed groups, Jeans analysis | σ/m = 0.5 ± 0.2 cm²/g | Sagunski et al. 2020, arXiv:2006.12515 | [src] |
| Relaxed clusters, Jeans analysis | σ/m = 0.19 ± 0.09 cm²/g; < 0.35 cm²/g (95%) | arXiv:2006.12515 | [src] |
| 8 clusters, strong lensing, mean relative velocity 1458 (+80/−81) km/s | σ/m = 0.082 (+0.027/−0.021) cm²/g; < 0.13 cm²/g (95%) | Andrade et al. 2020, arXiv:2012.06611 | [src] |
| Dwarfs to clusters, combined fit | about 2 cm²/g on galaxy scales falling to about 0.1 cm²/g on cluster scales | Kaplinghat, Tulin & Yu 2015, arXiv:1508.03339 | [src] |
| SPARC rotation curves, isothermal Jeans model with core collapse | L-shaped degeneracy: σ0 ≈ 2 cm²/g with ω ≳ 500 km/s, or σ0 ≈ 100 cm²/g with ω ≈ 60 km/s; best fit under the core-growth reading σ0 ≃ 5 cm²/g, ω ≃ 250 km/s; about 1/6 of galaxies admit both a core-growth and a core-collapse solution | Jia et al. 2026, arXiv:2601.17118 | [src] |

Reading rule: a velocity-independent cross section of order 1 cm²/g, the value originally invoked for dwarf cores, is disfavoured by groups and clusters; a cross section that falls with velocity is not (arXiv:2006.12515). A self-interaction limit is meaningless without the velocity at which it applies. Reviews: Tulin & Yu 2017, arXiv:1705.02358; Adhikari et al. 2022, arXiv:2207.10638.

## 7. Decaying dark matter, dark radiation and neutrino interactions (status level)
<!-- key: decaying-dark-matter-dark-radiation-and -->

| Model | Result | Data | Citation | Flag |
|---|---|---|---|---|
| Fraction f of dark matter decaying to dark radiation | at most 3.8% decayed between recombination and today (95%); f Γ < 6.3 × 10⁻³ Gyr⁻¹ for long lifetimes | CMB only (2016) | Poulin, Serpico & Lesgourgues 2016, arXiv:1606.02073 | [src] |
| Same model | f_dcdm ≲ 0.022 for lifetimes shorter than the age of the Universe; τ/f_dcdm ≳ 250 Gyr in the long-lived regime | Planck + Pantheon + BOSS (EFT full shape) | Simon et al. 2022, arXiv:2203.07440 | [src] |
| Decay to dark radiation + warm daughter (two-body) | best fit with an S8 prior: τ = 120 Gyr, v_kick/c ≃ 1.2% | same + KiDS-1000 S8 prior | arXiv:2203.07440 | [src] |
| Two-body decay, profile likelihood | half-life 6.93 (+7.88/−2.85) Gyr, kick 1250 (+1450/−1000) km/s at 68% CL; differs strongly from Bayesian intervals (volume effect) | Planck + SDSS BAO | Montandon et al. 2025, arXiv:2505.20193 | [src] |
| Decaying dark matter as a way to relax Σm_ν | background data alone allow Σm_ν of order 1 eV; full Planck likelihood with lensing restores Σm_ν ≲ 0.079 eV | BAO + SNe + CMB | Montandon et al. 2026, arXiv:2603.03284 | [src] |
| Self-interacting neutrinos, strongly interacting mode (2019) | H0 = 72.3 ± 1.4, σ8 = 0.786 ± 0.020, N_eff = 4.02 ± 0.29 | Planck 2015-era data | Kreisch, Cyr-Racine & Doré 2019, arXiv:1902.00534 | [src] |
| Neutrino self-interactions, 2025 | no evidence | ACT DR6 + Planck | arXiv:2503.14454 | [src] |
| Wess–Zumino (stepped) dark radiation; atomic dark matter with coupled dark radiation | ACT DR6 closes most of the parameter space that had allowed higher H0 | ACT DR6 | Cvetko, Joseph & Marques-Tavares 2025, arXiv:2512.19633 | [src] |
| Light sterile neutrino, fully thermalised | strongly disfavoured without a local H0 prior; partially populated (Dodelson–Widrow-like or cooler) cases remain viable | Planck + DESI DR2 BAO + SNe | Ladeira et al. 2026, arXiv:2606.21518 | [src] |

## 8. History of the key numbers
<!-- key: history-of-the-key-numbers -->

### 8.1 Σm_ν upper limit, ΛCDM, 95%
<!-- key: sigmamnu-upper-limit-lambdacdm-95 -->

| Year | Data | Limit | Citation | Flag | Status |
|---|---|---|---|---|---|
| 2018 | Planck 2018 + BAO | < 0.12 eV | arXiv:1807.06209 | [src] | superseded as the headline; still the last limit that predates DESI |
| 2019 | SDSS DR14 Lyα + Planck, with running free | < 0.11 eV; < 0.09 eV with CMB lensing and BAO | arXiv:1911.09073 | [src] | superseded; relies on the eBOSS-era P1D likelihood, see `cosmo-lyman-alpha` |
| 2024 | DESI DR1 BAO + CMB | < 0.072 eV (prior Σm_ν > 0); < 0.113 eV (prior Σm_ν > 0.059 eV) | DESI Collaboration 2024, arXiv:2404.03002 | [src] | superseded by DR2 |
| 2025 | ACT DR6 + Planck + lensing + DESI DR1 | < 0.089 eV (0.082 eV in the abstract) | arXiv:2503.14454 | [src] | current for ACT; uses DR1 BAO |
| 2025 | DESI DR2 BAO + CMB | < 0.0642 eV | arXiv:2503.14744 | [src] | current DESI Collaboration value |
| 2026 | DESI DR1 Lyα P1D added to CMB + BAO | "do not significantly tighten the limits" | Chaves-Montero et al. 2026, arXiv:2601.21432 abstract | [src] | `cosmo-lyman-alpha` gives the shift as 55.1 → 53.7 meV [sec, sibling skill] |
| 2026 | SPT-3G D1 lensing + CMB + BAO | < 0.072 eV | arXiv:2608.31136 | [src] | current for SPT |

The limit fell by a factor of about two between 2018 and 2025 while the effective-mass posterior width stayed near 0.05 eV (σ = 0.053 eV, arXiv:2503.14744). The tightening is mostly a shift of the preferred value towards and below zero, not a gain in sensitivity. Forecasts made before the data anticipated about 0.02 eV precision for DESI with Planck (Font-Ribera et al. 2013, arXiv:1308.4164, **forecast**); the Bayesian σ = 0.020 eV matches that number only because the prior boundary truncates the posterior.

### 8.2 N_eff
<!-- key: neff -->

| Year | Data | Value | Citation | Flag |
|---|---|---|---|---|
| 2018 | Planck 2018 + BAO | 2.99 ± 0.17 | arXiv:1807.06209 | [src] |
| 2022 | BBN + CMB | 2.898 ± 0.141 | arXiv:2207.13133 | [src] |
| 2025 | P-ACT-LB | 2.86 ± 0.13 | arXiv:2503.14454 | [src] |
| 2025 | CMB-SPA | 2.82 ± 0.12 | arXiv:2506.20707 | [src] |
| 2025 | DESI DR2 BAO + Planck + lensing | 3.23 ± 0.18 | arXiv:2503.14744 | [src] |
| 2026 | LBT Y_p + D/H + CMB | 2.925 ± 0.082 | arXiv:2601.22239 | [src] |
| 2026 | DESI DR1 Lyα P1D + CMB + BAO | 3.02 ± 0.10 | arXiv:2601.21432 abstract | [src] |

### 8.3 Thermal-relic warm dark matter mass, Lyα forest
<!-- key: thermal-relic-warm-dark-matter-mass-lyalpha -->

2005: 0.55 keV (arXiv:astro-ph/0501562) → 2013: 3.3 keV (arXiv:1306.2314) → 2017: 5.3 keV, or 3.5 keV with a non-smooth thermal history (arXiv:1702.01764) → 2019: 1.9 keV for the coldest allowed histories (arXiv:1912.09397) → 2022: 3.1 keV (arXiv:2209.14220) → 2023: 5.7 keV, or 4.1 keV at k_max < 0.1 s/km (arXiv:2309.04533). All [src]. The sequence is not monotonic: the lower values are deliberate relaxations of the thermal-history prior, not older data.

### 8.4 Thermal-relic warm dark matter mass, strong-lensing flux ratios
<!-- key: thermal-relic-warm-dark-matter-mass-strong -->

2019: 5.2 keV, 8 lenses (arXiv:1908.06983) → 2025: 5.6 or 6.4 keV, 31 lenses with JWST (arXiv:2511.07765) → 2025–2026: 6.5 or 7.4 keV, 28 quads with arcs (arXiv:2511.07513, arXiv:2606.05277). All [src]. The 2021 joint lensing + satellites value of 9.7 keV (arXiv:2101.07810) used the 2019 lensing posterior and has not been redone with the JWST sample in any paper found this session.

### 8.5 Self-interaction cross section on cluster scales
<!-- key: self-interaction-cross-section-on-cluster-scales -->

2007: < 1.25 cm²/g at 68%, Bullet Cluster (arXiv:0704.0261) → 2015: < 0.47 cm²/g, 72 mergers (arXiv:1503.07675) → 2020: < 0.35 cm²/g, relaxed clusters (arXiv:2006.12515) → 2020: < 0.13 cm²/g, cluster strong lensing (arXiv:2012.06611). All [src]. The methods differ (merger offsets, Jeans modelling, lensing profiles), so the sequence is not a single improving measurement.

## Not verified
<!-- key: not-verified -->

- The first JUNO oscillation paper (59 days of data) was seen only through citing abstracts; its arXiv ID was not retrieved. The 207-day paper in §1.1 supersedes it.
- LEGEND-200 first results on ⁷⁶Ge exist as 2025 conference proceedings found in a search; they were not read and no number is quoted.
- No KATRIN neutrino-mass result later than the 259-day analysis was found in an arXiv title search from June 2025; whether the final-data-set result has appeared elsewhere was not checked.
- The hub file `observational-cosmology/references/field-state-2026.md` quotes a 2.7σ positive Σm_ν in w0waCDM from a joint analysis with DES data; that paper was not read here and is not cited.
- No DESI Collaboration warm- or fuzzy-dark-matter limit from the DR1 or DR2 P1D was found in the searches run this session; absence of a result is not established.
- The Σm_ν limit from the eBOSS final cosmology paper was not found in its abstract and is omitted.
- Project 8 and KATRIN++ sensitivities are quoted only from secondary abstracts.
