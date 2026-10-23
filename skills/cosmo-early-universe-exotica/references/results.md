# Early-Universe exotica — results

Scope: headline measurements and limits for each exotic ingredient, with the model and data set behind every number, and what superseded what.
Snapshot: 2026-10-16

Flags as in `physics-and-methods.md`.

## 1. Pulsar-timing background: amplitude, spectrum, significance
<!-- key: pulsar-timing-background-amplitude-spectrum -->

Amplitudes are characteristic strain at f = 1 yr⁻¹. "γ = 13/3" (strain index
α = −2/3) is the circular-SMBHB value; a free γ is fitted to the residual
spectrum. Intervals are as each paper states them.

| Array | A at γ = 13/3 | Free spectrum | Significance of HD | Citation | Flag |
|---|---|---|---|---|---|
| NANOGrav 15 yr | 2.4 (+0.7/−0.6) × 10⁻¹⁵ (median, 90%), log-uniform amplitude prior | A = 6.4 (+4.2/−2.7) × 10⁻¹⁵, γ = 3.2 ± 0.6 (5–95%) | BF(HD/CURN) 200–1000; p = 10⁻³ (Bayesian null), 5 × 10⁻⁵ – 1.9 × 10⁻⁴ (optimal statistic) | arXiv:2306.16213 | [src: Sect. I, III] |
| EPTA DR2 (+ InPTA) | (2.5 ± 0.7) × 10⁻¹⁵ (full set and 10.3 yr subset agree) | 10.3 yr spectrum "rather uncertain", in mild tension with the full set | full 24.7 yr: BF 4, FAP 4%; 10.3 yr: BF 60, FAP ~0.1% (≳ 3σ) | arXiv:2306.16214 | [src: abstract] |
| PPTA DR3 | 2.04 (+0.25/−0.22) × 10⁻¹⁵ (68%) | A = 3.1 (+1.3/−0.9) × 10⁻¹⁵, α = −0.45 ± 0.20 | p ≲ 0.02 (~2σ) | arXiv:2306.16215 | [src: abstract] |
| CPTA DR1 | — | log A_c = −14.4 (+1.0/−2.8) for α ∈ [−1.8, 1.5] | 4.6σ at ~14 nHz (discrete-frequency method) | arXiv:2306.16216 | [src: abstract] |
| MPTA 4.5 yr | 4.8 (+0.8/−0.9) × 10⁻¹⁵ | 7.5 (+0.8/−0.9) × 10⁻¹⁵ at α = −0.26 | 3–3.4σ in the most significant noise model, insignificant in others | arXiv:2412.01153 | [src: abstract] |
| InPTA DR2 | < 3.4 × 10⁻¹⁴ (95%) | log₁₀ A_CURN = −13.71 (+1.06/−3.28), γ_CURN unconstrained | none; Savage–Dickey BF 2.5 for CURN | arXiv:2608.02808 | [src: abstract] |
| Five-PTA public combination (121 pulsars) | — | posterior on A and γ consistent with a non-zero amplitude | below 5σ; correlation matches HD | arXiv:2512.08666 | [src: abstract] |

- The NANOGrav amplitude at γ = 13/3 corresponds to an integrated energy
  density Ω_gw = 9.3 (+5.8/−4.0) × 10⁻⁹ in the sensitive band (H0 = 70)
  (arXiv:2306.16213) [src: Sect. I].
- The amplitude posterior of NANOGrav "has essentially no support below
  10⁻¹⁵" (arXiv:2306.16213) [src: Sect. III].
- PPTA: the first half of the data set gives an upper limit in tension with
  the amplitude inferred from the full set (arXiv:2306.16215) [src]. MPTA:
  the HD significance depends on noise assumptions, because a few
  high-precision pulsars close on the sky dominate the statistics
  (arXiv:2412.01153) [src].
- The IPTA comparison finds no significant difference in GWB parameters
  between arrays, agreement within 1σ (arXiv:2309.00693) [src].
- No array has claimed a 5σ detection as of the snapshot; the combined
  five-array analysis remains below 5σ (arXiv:2512.08666) [src].

## 2. Ground-based stochastic-background limits
<!-- key: ground-based-stochastic-background-limits -->

All 95% credible, log-uniform amplitude prior, reference frequency 25 Hz.

| Data | Ω_GW, α = 0 | Ω_GW, α = 2/3 | Ω_GW, α = 3 | Citation | Flag |
|---|---|---|---|---|---|
| O1–O3 | ≤ 5.8 × 10⁻⁹ (flat, 20–76.6 Hz) | ≤ 3.4 × 10⁻⁹ | ≤ 3.9 × 10⁻¹⁰ | arXiv:2101.12130 | [src: abstract] |
| O1–O4a | ≤ 2.8 × 10⁻⁹ | ≤ 2.0 × 10⁻⁹ (factor 1.7 better) | — | arXiv:2508.20721 | [src: abstract] |
| O1 to April 2025 (new frequency cuts) | ≤ 2.8 × 10⁻⁹ | ≤ 2.0 × 10⁻⁹ (factor 1.4 better than the earlier data recomputed with the new cuts) | — | arXiv:2608.23477 | [src: abstract] |

Integrated bounds on a primordial background (LISA Cosmology WG 2022): A background produced before BBN counts as extra radiation. The bound used is ∫ d ln f Ω_GW h² ≤ 5.6 × 10⁻⁶ (N_eff^upper − 3.046); with the BBN 2σ upper limit N_eff
= 3.41 it gives Ω_GW h² < 2.3 × 10⁻⁶ per logarithmic frequency bin. CMB temperature data give
Ω_GW h² < 1.7 × 10⁻⁶ for adiabatic and < 2.9 × 10⁻⁷ for homogeneous (non-adiabatic) initial
conditions at 95%, valid for f > 10⁻¹⁵ Hz; most sources produce an unperturbed background, so
the homogeneous bound applies (LISA Cosmology WG 2022, arXiv:2204.05434) [src: Sect. 5.1.3]. The
large-scale CMB B-mode limit r < 0.036 corresponds to Ω_GW h² < 1.5 × 10⁻¹⁶ at f = 7.7 × 10⁻¹⁷
Hz [src: Sect. 5.1.3]; the r limit itself belongs to `cosmo-inflation-primordial`. The N_eff
values behind the BBN version of this bound are in `cosmo-bbn`.

The predicted compact-binary background is Ω_CBC(25 Hz) = 0.9 (+1.1/−0.5) ×
10⁻⁹ (90%, GWTC-4 populations; arXiv:2508.20721) and 6.3 (+5.0/−2.2) × 10⁻¹⁰
(90%, GWTC-5.0; arXiv:2608.23477) [src]: the astrophysical foreground sits
within a factor of a few of the current limits, so a cosmological background
at 25 Hz will have to be separated from it.

## 3. Phase transitions and the PTA signal
<!-- key: phase-transitions-and-the-pta-signal -->

| Statement | Value | Model, data | Citation | Flag |
|---|---|---|---|---|
| Bayes factor versus SMBHB alone | pt-bubble 18.1 ± 0.6; pt-sound 3.7 ± 0.1; with SMBHB added: 12.6 ± 0.5 and 6.5 ± 0.3 | NANOGrav 15 yr; SMBHB reference model with astrophysical priors | arXiv:2306.16219 | [src: Sect. V.3] |
| Percolation temperature, pt-bubble | T_* ∈ [0.047, 0.41] GeV (68%), [0.023, 1.75] GeV (95%) | same | arXiv:2306.16219 | [src: Sect. V.3] |
| Percolation temperature, pt-sound | T_* ∈ [4.7, 33] MeV (68%), [2.7, 93] MeV (95%); with SMBHB [4.9, 50] MeV (68%), [0.8, 2 × 10⁶] MeV (95%) | same; the 95% range with SMBHB covers a plateau where SMBHBs explain the signal | arXiv:2306.16219 | [src: Sect. V.3] |
| Secluded dark-sector transition | strongly disfavoured against SMBHBs once BBN and CMB energy-release bounds apply; a dark sector that decays before neutrino decoupling remains viable | NANOGrav common red spectrum published before the 15 yr release (the paper predates it) | Bringmann et al. 2023, arXiv:2306.09411 | [src] |
| EPTA | the measurement "would place tight constraints ... on the level of turbulence developed by first-order phase transitions" | EPTA DR2 + InPTA | arXiv:2306.16227 | [src] |

The T_* intervals shift between templates partly because of the numerical
factors in the peak-frequency definitions; NANOGrav notes that these can be
reabsorbed in T_* (arXiv:2306.16219) [src: Sect. V.3].

## 4. Cosmic strings and defects
<!-- key: cosmic-strings-and-defects -->

| Probe | Limit on Gμ (95%) | Model | Citation | Flag |
|---|---|---|---|---|
| Planck 2013 power spectrum | < 1.5 × 10⁻⁷ (< 1.3 × 10⁻⁷ with high-ℓ data); f₁₀ < 0.015 | Nambu–Goto | arXiv:1303.5085 | [src: abstract] |
| Planck 2013 power spectrum | < 3.2 × 10⁻⁷; f₁₀ < 0.028 | Abelian-Higgs field theory | arXiv:1303.5085 | [src: abstract] |
| Planck 2013 non-Gaussian searches | < 8.8 × 10⁻⁷ (modal bispectrum) | post-recombination strings | arXiv:1303.5085 | [src] |
| PTA (pre-2014 limits) | ≤ 2.8 × 10⁻⁹ | Blanco-Pillado et al. loop distribution | arXiv:1309.6637 | [src] |
| LVK O3 stochastic + burst | ≲ 4 × 10⁻¹⁵ for one loop model; one to two orders of magnitude better than O2, model-dependent | loop models A, B and an interpolating model | arXiv:2101.12248 | [src] |
| NANOGrav 15 yr fit | stable strings give Bayes factors 0.28–0.38 against SMBHB (0.76–0.89 when added to SMBHB) | stable-c, -k, -m, -n templates | arXiv:2306.16219 | [src: Sect. V.4] |

Superstrings and metastable strings fit the NANOGrav signal; stable
field-theory strings are the only cosmological source that consistently
yields a Bayes factor in favour of SMBHBs (arXiv:2306.16219) [src: Sect.
V.4]. EPTA states that a GW origin of its signal would tightly constrain the
string tension (arXiv:2306.16227) [src].

## 5. Primordial black holes
<!-- key: primordial-black-holes -->

f_PBH = Ω_PBH/Ω_DM, monochromatic mass function unless stated. Constraint families as
summarised by Carr et al. 2026 (arXiv:2601.06024, Sect. IV):

| Family | Mass range and mechanism | Place read |
|---|---|---|
| Evaporation | 10⁹–10¹⁷ g. Non-spinning PBHs lighter than ~10⁹ g evaporate before BBN; BBN constrains 10⁹–10¹³ g; CMB anisotropy damping above 10¹³ g; extragalactic photon background and Voyager e± up to ~10¹⁷ g. Altered by large extra dimensions, memory burden or exotic remnants | [src: Sect. IV.1.1] |
| Microlensing | MACHO, EROS, Kepler, Subaru/HSC and OGLE; claimed to exclude f_PBH > 1% over 10⁻¹⁰–10³ M☉; low-mass end limited by wave optics and finite source size, high-mass end by event duration; extended upwards by supernova lensing and lensing of LVK events | [src: Sect. IV.2.1] |
| Gravitational waves | binaries formed in the early Universe; LVK merger rates and sub-solar searches | Sect. IV.3 title |
| Dynamics | heating and disruption of bound systems | Sect. IV.4 title |
| Accretion | X-ray, radio and CMB (altered ionisation history) | Sect. IV.5 title; Serpico et al. 2020 below |

Individual limits:

| Probe | Mass range | Limit | Data, model | Citation | Flag |
|---|---|---|---|---|---|
| Subaru/HSC M31 microlensing | ~10⁻¹¹–10⁻⁶ M☉ | "most stringent" upper bounds when published; one candidate event | 7 h, 2 min cadence, tens of millions of M31 stars | Niikura et al. 2017, arXiv:1701.02151 | [src] |
| OGLE bulge, 5 yr | 10⁻⁶–10⁻³ M☉ | tightest bound in this range under the null hypothesis; 6 ultrashort events (t_E ≈ 0.1–0.3 d) fit by Earth-mass PBHs at per-cent f_PBH | 2622 events | Niikura et al. 2019, arXiv:1901.07120 | [src] |
| OGLE high-cadence Magellanic Clouds (Oct 2022 – May 2024) | 1.4 × 10⁻⁸ – 0.013 M☉ | f_PBH ≤ 1%; no short events; rules out the PBH origin of the bulge ultrashort events | ~35 million stars | Mróz et al. 2024, arXiv:2410.06251 | [src: abstract] |
| OGLE LMC, 20 yr | 1.8 × 10⁻⁴ – 6.3 M☉; 1.3 × 10⁻⁵ – 860 M☉ | < 1%; < 10% | ~80 million stars, no events with t_E > 1 yr | Mróz et al. 2024, arXiv:2403.02386 | [src: abstract] |
| EROS-2 (+ EROS-1), Magellanic Clouds | 0.6 × 10⁻⁷ – 15 M☉ | excluded as the primary halo component; τ_LMC < 0.36 × 10⁻⁷ (95%), < 8% of the halo at ~0.4 M☉ | 7 × 10⁶ bright stars, 6.7 yr; one candidate where ~39 expected | Tisserand et al. 2006, arXiv:astro-ph/0607207 | [src] |
| LVK O3a sub-solar search | one component 0.2–1.0 M☉, q ≥ 0.1 | f_PBH ≲ 6% (equal-mass isotropic PBHs); merger rate < 220–24200 Gpc⁻³ yr⁻¹ | no candidates; loudest trigger FAR 0.14 yr⁻¹ | LVK 2021, arXiv:2109.12197 | [src: abstract] |
| LVK O3 events, hierarchical | 1–200 M☉ | f_PBH ≲ 10⁻³ in every scenario | early-Universe binaries; several mass functions incl. QCD-epoch critical collapse with non-Gaussianity | Andrés-Carcasona et al. 2024, arXiv:2405.05732 | [src: abstract] |
| CMB, accretion with DM halo | ≳ 20–50 M☉ upward | f_PBH < 3 × 10⁻⁹ around 10⁴ M☉ | Planck 2018 | Serpico et al. 2020, arXiv:2002.10771 | [src] |
| Review summary (microlensing) | 10⁻¹⁰–10³ M☉ | "claimed" exclusion above 1% of the halo | MACHO, EROS, Kepler, HSC, OGLE | Carr et al. 2026, arXiv:2601.06024 | [src: Sect. IV.2.1] |
| Review summary (window) | ~10⁻¹⁷–10⁻¹⁰ M☉ | unconstrained; PBHs could be all the dark matter | — | arXiv:2601.06024 | [src: Sect. V] |

The OGLE LMC paper concludes that PBHs in its mass range "cannot
simultaneously explain a significant fraction of dark matter and
gravitational wave events" (arXiv:2403.02386) [src]; this conclusion is
disputed (open-questions.md §2).

## 6. Scalar-induced gravitational waves
<!-- key: scalar-induced-gravitational-waves -->

| Statement | Value | Citation | Flag |
|---|---|---|---|
| Bayes factor of SIGW versus SMBHB (NANOGrav 15 yr) | sigw-delta 44 ± 2, sigw-gauss 57 ± 3, sigw-box 21 ± 1; with SMBHB added 38 ± 2, 59 ± 3, 23 ± 1 — larger than for inflationary tensors | arXiv:2306.16219 | [src: Sect. V.2] |
| PBH overproduction | disfavours Gaussian SIGW at 2σ and single-field scenarios with non-Gaussianity at 3σ as the explanation of NANOGrav 15 yr; relaxed if non-Gaussianity suppresses PBHs; PTA data do not constrain the PBH abundance | Franciolini et al. 2023, arXiv:2306.17149 | [src] |

These Bayes factors carry the same caveat as all new-physics fits: they
depend on the SMBHB population prior (arXiv:2306.16219) [src].

## 7. Early dark energy
<!-- key: early-dark-energy -->

Axion-like EDE, n = 3 unless stated. The value of f_EDE depends on the data
combination, on the BAO sample and on Bayesian versus profile treatment;
quote all three.

| Data | f_EDE | H0 (km/s/Mpc) | Treatment | Citation | Flag |
|---|---|---|---|---|---|
| Planck 2018 alone | < 0.087 (95%) | 68.3 ± 1.0 | Bayesian | as quoted in arXiv:2503.14454 | [sec: ACT DR6, Sect. V.1] |
| ACT DR4 + large-scale Planck TT + Planck lensing + BOSS BAO | 0.091 (+0.020/−0.036) (68%) | 70.9 (+1.0/−2.0) | Bayesian; hint driven by EE at ℓ ~ 500 | as quoted in arXiv:2503.14454 | [sec: ACT DR6, Sect. V.1] |
| ACT DR6 alone | < 0.088 (95%) | 67.5 (+0.9/−1.7) | Bayesian | arXiv:2503.14454 | [src: Eqs. 14–15] |
| P-ACT | < 0.12 (95%) | 69.3 (+0.9/−1.5) | Bayesian | arXiv:2503.14454 | [src: Eqs. 14–15] |
| W-ACT | — | 68.1 (+0.8/−1.6) | Bayesian | arXiv:2503.14454 | [src: Sect. V.1] |
| P-ACT-LB (+ CMB lensing + DESI DR1 BAO) | < 0.12 (95%) | 69.9 (+0.8/−1.5); ΛCDM 68.2 ± 0.4 | Bayesian | arXiv:2503.14454 | [src: Eq. 16] |
| P-ACT-LB with BOSS instead of DESI BAO | < 0.10 (95%) | 69.2 (+0.7/−1.3) | Bayesian | arXiv:2503.14454 | [src: Sect. V.1] |
| SPT-3G D1 alone | < 0.12 (95%) | Hubble tension with SH0ES 2.3σ | Bayesian | Khalife et al. 2025, arXiv:2507.23355 | [src: abstract] |
| SPT + ACT + Planck | < 0.070 (95%) | tension 3.6σ | Bayesian | arXiv:2507.23355 | [src: abstract] |
| SPT + DESI | 0.081 (+0.037/−0.052) (68%) | tension 1.5σ | Bayesian | arXiv:2507.23355 | [src: abstract] |
| SPT + ACT + Planck + DESI | 0.055 (+0.024/−0.047) (68%) | tension 2.6σ | Bayesian | arXiv:2507.23355 | [src: abstract] |
| Planck ℓ < 1000 + ACT DR6 + lensing + Pantheon+ + DESI DR2 | 0.09 ± 0.03 | 71.0 ± 1.1 | profile likelihood | Poulin et al. 2025, arXiv:2505.08051 | [src: abstract] |
| ACT DR6 + DESI DR2 (with varying-m_e study) | < 0.016 | — | Bayesian | Toda et al. 2025, arXiv:2508.09025 | [src] |
| Planck + BOSS full shape | 0.072 ± 0.036 (68%) | — | profile likelihood | Herold et al. 2022, arXiv:2112.12140 | [src: abstract] |

- ACT DR6 finds "no evidence" for EDE; the DR4 hint is not seen in DR6
  (arXiv:2503.14454) [src; src: Sect. V.1].
- SPT-3G attributes the mild preference with DESI to "the discrepancy
  currently present between DESI and CMB experiments" in ΛCDM
  (arXiv:2507.23355) [src].
- Poulin et al. find a residual SH0ES tension of ~2σ, against 3.7σ with
  NPIPE and SDSS BAO; adding SH0ES raises the preference above 5σ,
  Δχ² = −35.4 (arXiv:2505.08051) [src: abstract].
- The Toda et al. bound, f_EDE < 0.016, is far below the others; its prior
  and data choices were not read (see "Not verified").

## 8. Modified recombination and varying constants
<!-- key: modified-recombination-and-varying-constants -->

Constants vary as a step at z = 50 (ACT DR6) unless stated; 68% intervals.

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Δα/α (recombination) | (3.6 ± 3.7) × 10⁻³ | Planck 2013 | Planck int. XXIV, arXiv:1406.7482 | [src: abstract] |
| Δm_e/m_e | (4 ± 11) × 10⁻³ | Planck 2013 | arXiv:1406.7482 | [src] |
| m_e/m_e,0 | 1.0078 ± 0.0067; with SNe 1.0190 ± 0.0055 (H0 = 71.24 ± 0.96) | Planck 2018 + BAO (+ SNe) | Hart et al. 2019, arXiv:1912.03986 | [src: abstract] |
| m_e/m_e,0 | 0.856 (+0.060/−0.073) (P-ACT, 2.4σ below 1, driven by Planck); ACT alone 1.02 (+0.11/−0.15); W-ACT 0.921 ± 0.083; Planck alone 0.880 (+0.068/−0.080) | CMB only | arXiv:2503.14454 | [src: Eqs. 17–18] |
| m_e/m_e,0 | 1.0096 ± 0.0060, H0 = 69.8 ± 1.1 (P-ACT-LB); 1.0063 ± 0.0056, H0 = 69.1 ± 1.0 (P-ACT-LBS) | + lensing + DESI DR1 (+ SNe) | arXiv:2503.14454 | [src: Eq. 19] |
| m_e/m_e,0 | 1.0081 ± 0.0046 | ACT DR6 + DESI DR2 | Toda et al. 2025, arXiv:2508.09025 | [src: Sect. V] |
| m_e with Ω_k | m_e/m_e,0 = 1.022 ± 0.016, Ω_k = −0.0031 ± 0.0037, H0 = 71.0 ± 1.7 (P-ACT-LB); W-ACT-LB 1.014 ± 0.015, 0.0001 ± 0.0042, 70.4 ± 1.7; SNe push back toward ΛCDM | CMB + lensing + BAO | arXiv:2503.14454 | [src: Eqs. 20–21, Fig. 14] |
| m_e with Ω_k (earlier) | H0 = 72.3 (+2.7/−2.8) from CMB + BAO + SNe without local H0 | Planck 2018 + BAO + SNe | Sekiguchi et al. 2020, arXiv:2007.03381 | [src: abstract] |
| α_EM/α_EM,0 | 1.0037 ± 0.0017 (P-ACT); Planck alone 1.0005 ± 0.0025; ACT alone 1.0046 ± 0.0035 | CMB only | arXiv:2503.14454 | [src: Eq. 23] |
| α_EM/α_EM,0 | 1.0043 ± 0.0017 (≈ 2.5σ above 1), H0 = 69.27 ± 0.54 | P-ACT-LB | arXiv:2503.14454 | [src: Eq. 24] |
| Δα/α at z = 1.15 | 1.3 ± 1.3 (stat) ± 0.4 (sys) ppm | ESPRESSO, HE 0515−4414, 16.1 h | Murphy et al. 2021, arXiv:2112.05819 | [src: abstract] |
| X_e(z) reconstruction | consistent with standard recombination; factor-two smaller error at the z ≈ 1467 control point with ACT DR6 | ModRec, Planck-LB and P-ACT-LB | arXiv:2503.14454 | [src: Sect. V.5] |

ACT DR6 calls its m_e and α_EM bounds "the tightest constraints to date" on
these constants at recombination, near the half-percent and per-mille levels,
interpreting the P-ACT departures as statistical fluctuations
(arXiv:2503.14454) [src: Sect. V.2.1, V.2.3]. The overall verdict of the
paper is "no evidence" for varying constants or modified recombination
[src].

## 9. Spectral distortions
<!-- key: spectral-distortions -->

| Quantity | Limit or value | Data | Citation | Flag |
|---|---|---|---|---|
| y | |y| < 15 × 10⁻⁶ (95%) | COBE/FIRAS full data | Fixsen et al. 1996, arXiv:astro-ph/9605054 | [src] |
| μ | |μ| < 9 × 10⁻⁵ (95%) | COBE/FIRAS full data | arXiv:astro-ph/9605054 | [src] |
| T_CMB | 2.728 ± 0.004 K (95%) | COBE/FIRAS | arXiv:astro-ph/9605054 | [src: abstract] |
| μ monopole | |⟨μ⟩| < 47 × 10⁻⁶ (95%), a factor ~2 better than FIRAS | FIRAS reanalysis | Bianchini et al. 2022, arXiv:2206.02762 | [src] |
| f_NL on 10 ≲ k ≲ 5 × 10⁴ | f_NL ≲ 3.6 × 10⁶, n_NL ≲ 1.4 | μT, μE cross-correlation FIRAS × Planck | arXiv:2206.02762 | [src: abstract] |
| ΛCDM μ prediction | (2.3 ± 0.14) × 10⁻⁸ | theory, scale-invariant extrapolation | arXiv:1909.01593 | [src: Sect. 2.1] |

Bianchini et al. also find that earlier μ analyses from Planck, despite
lower noise, give "similar or worse" results once instrumental and
astrophysical uncertainties are accounted for (arXiv:2206.02762) [src].
The FIRAS T_CMB value of 1996 is superseded by later recalibrations, not
read here (see "Not verified").

## 10. Energy injection
<!-- key: energy-injection -->

| Quantity | Limit | Data, assumptions | Citation | Flag |
|---|---|---|---|---|
| p_ann = f_eff ⟨σv⟩/m_χ | < 3.2 × 10⁻²⁸ cm³ s⁻¹ GeV⁻¹ (the bound behind the Planck 2018 mass–cross-section figure) | Planck 2018; on-the-spot; constant f_eff | arXiv:1807.06209 | [src: Sect. 7.9, Fig. 46 caption] |
| s-wave annihilation, Standard Model final states | bounds as a function of mass that "generically exclude" models proposed for the cosmic-ray positron rise | Planck 2015 bound mapped with f_eff | arXiv:1506.03811 | [src] |
| Decay | model-independent bounds via one detectability factor per model | Planck 2015, PCA validated by MCMC | arXiv:1610.06933 | [src] |
| Decaying sub-keV dark matter, ALP–photon coupling | CMB anisotropy bounds extended to arbitrarily low masses | DarkHistory with low-energy electrons | arXiv:2303.07370 | [src] |

The Planck figure also shows the AMS proton excess and Fermi Galactic-centre
regions computed for annihilation into b b̄ (arXiv:1807.06209) [src: Fig. 46
caption]; whether the CMB excludes them is read on that figure, not here.

## 11. Primordial magnetic fields
<!-- key: primordial-magnetic-fields -->

| Quantity | Limit or value | Data, model | Citation | Flag |
|---|---|---|---|---|
| B_1Mpc, non-helical | < 4.4 nG (95%) | Planck 2015 power spectra | arXiv:1502.01594 | [src] |
| B_1Mpc, maximally helical | < 5.6 nG | Planck 2015 | arXiv:1502.01594 | [src] |
| B_1Mpc, nearly scale-invariant | < 2.0 nG; < 0.9 nG with the ionisation-history effect | Planck 2015 | arXiv:1502.01594 | [src: abstract] |
| B_1Mpc from non-Gaussianity | < 2.8 nG (passive-tensor bispectrum); < 4.5 nG (preferred directions); < 3 nG (compensated scalar) | Planck 2015 | arXiv:1502.01594 | [src: abstract] |
| √⟨B²⟩, ionisation history | < 0.69 nG (Planck 2018), < 0.72 nG (SRoll2 low-ℓ EE), marginalised over n_B (95%) | ambipolar diffusion + MHD turbulence | Paoletti et al. 2022, arXiv:2204.06302 | [src: abstract] |
| Clumping variance b | < 0.41 (P-ACT), < 0.44 (P-ACT-LB) (95%); no evidence of clumping | three-zone M1 model | arXiv:2503.14454 | [src: Eq. 27, Fig. 15] |
| PMF strength from recombination fits | preference for 5–10 pG today, ~1.8σ (Planck + DESI) to ~3σ (+ SH0ES-calibrated SNe) | non-helical, Batchelor spectrum; MHD-informed recombination | Jedamzik et al. 2025, arXiv:2503.09599 | [src: abstract] |
| Lyα forest | B < 0.30 nG for n_B = −2.9 (k_peak > 30 Mpc⁻¹, 3σ, conservative noise model); a hint of extra power fitted by B ~ 0.2 nG at k_peak ~ 20 Mpc⁻¹ | hydrodynamic simulations, > 250 000 flux models | Pavičević et al. 2025, arXiv:2501.06299 | [src] |
| IGMF lower bound | B ≥ 3 × 10⁻¹⁶ G | Fermi, TeV blazars | Neronov et al. 2010, arXiv:1006.3504 | [src] |
| IGMF lower bound | B > 7.1 × 10⁻¹⁶ G for 1 Mpc coherence and a 10 yr duty cycle; > 1.8 × 10⁻¹⁴ G (10⁴ yr), > 3.9 × 10⁻¹⁴ G (10⁷ yr) | Fermi-LAT + H.E.S.S. | H.E.S.S. & Fermi-LAT 2023, arXiv:2306.05132 | [src: abstract] |

The gap between the γ-ray lower bounds (~10⁻¹⁶–10⁻¹⁴ G) and the CMB and
Lyα upper bounds (~0.1–1 nG) is the window in which a primordial field
would have to lie [der: comparison of the rows above, same comoving
normalisation assumed, which the papers do not all share].

## 12. Axion-like particles
<!-- key: axion-like-particles -->

| Quantity | Limit | Data | Citation | Flag |
|---|---|---|---|---|
| Ω_ax/(Ω_ax + Ω_c), m_ax = 10⁻²⁶ eV | < 0.070 (Planck), < 0.052 (P-ACT) (95%) | primary CMB | arXiv:2503.14454 | [src: Eq. 51] |
| same, m_ax = 10⁻²⁷ eV | ≈ 4.5% for both Planck and P-ACT (95%) | primary CMB | arXiv:2503.14454 | [src: Sect. VI.3] |

Part of the improvement comes from the degeneracy between the axion density
and n_s (arXiv:2503.14454) [src: Sect. VI.3]. ACT DR6 summarises: "only a
small fraction allowed as axion-like particles" [src].

## 13. History of key numbers
<!-- key: history-of-key-numbers -->

| Quantity | Earlier value | Superseded by | Why | Citation | Flag |
|---|---|---|---|---|---|
| Isotropic LVK limit, flat spectrum | Ω_GW ≤ 5.8 × 10⁻⁹ (O1–O3) | ≤ 2.8 × 10⁻⁹ (O1–O4a; confirmed with data to April 2025) | more data; new frequency-domain cuts | arXiv:2101.12130 → arXiv:2508.20721, arXiv:2608.23477 | [src] |
| PTA strain amplitude at f = 1 yr⁻¹, γ = 13/3 | 1.92 × 10⁻¹⁵ and 2.95 × 10⁻¹⁵, common-process values quoted in the 2022 LISA review | NANOGrav 15 yr 2.4 (+0.7/−0.6) × 10⁻¹⁵ with HD correlations | first HD evidence | arXiv:2204.05434 [src: Sect. 5.1.3] → arXiv:2306.16213 | [src] |
| PTA string tension (pre-2014 PTA data) | Gμ ≤ 2.8 × 10⁻⁹ | PTA signal fitted by metastable or superstrings; stable strings disfavoured | detection of a common signal | arXiv:1309.6637 → arXiv:2306.16219 | [src] |
| Planck string tension | Gμ < 1.3–1.5 × 10⁻⁷ (Nambu–Goto) | still the CMB reference; LVK and PTA bounds are model-dependent and far tighter | — | arXiv:1303.5085 | [src: abstract] |
| f_EDE hint | 0.091 (+0.020/−0.036), ACT DR4 combination | ACT DR6 < 0.088 (ACT), < 0.12 (P-ACT-LB) | DR6 polarisation | arXiv:2503.14454 | [src: Sect. V.1] |
| Δα/α at recombination | (3.6 ± 3.7) × 10⁻³ (Planck 2013) | α_EM/α_EM,0 = 1.0037 ± 0.0017 (P-ACT) | ACT DR6 damping tail | arXiv:1406.7482 → arXiv:2503.14454 | [src; src: Eq. 23] |
| m_e/m_e,0 | 1.0078 ± 0.0067 (Planck 2018 + BAO) | 1.0096 ± 0.0060 (P-ACT-LB) | ACT DR6 + DESI | arXiv:1912.03986 → arXiv:2503.14454 | [src; src: Eq. 19] |
| μ monopole | < 9 × 10⁻⁵ (FIRAS 1996) | < 47 × 10⁻⁶ (FIRAS reanalysis) | reanalysis with a μ map | arXiv:astro-ph/9605054 → arXiv:2206.02762 | [src] |
| PMF amplitude | B_1Mpc < 0.9 nG with ionisation (Planck 2015) | √⟨B²⟩ < 0.69 nG (Planck 2018); Lyα B < 0.30 nG (n_B = −2.9) | better polarisation; Lyα small scales | arXiv:1502.01594 → arXiv:2204.06302, arXiv:2501.06299 | [src] |
| IGMF lower bound | B ≥ 3 × 10⁻¹⁶ G | B > 7.1 × 10⁻¹⁶ G (1 Mpc, 10 yr duty cycle) | combined Fermi-LAT + H.E.S.S. | arXiv:1006.3504 → arXiv:2306.05132 | [src] |
| Planetary-mass PBHs | per-cent f_PBH fits the OGLE ultrashort events | ≤ 1% for 1.4 × 10⁻⁸ – 0.013 M☉ | high-cadence Magellanic Cloud survey | arXiv:1901.07120 → arXiv:2410.06251 | [src] |
| Stellar-mass PBHs from LVK | PBH dark matter consistent with GW150914 rates (2016) | f_PBH ≲ 10⁻³ over 1–200 M☉ (O3) | population analyses | arXiv:1603.00464, arXiv:1603.08338 → arXiv:2405.05732 | [src] |

The PIXIE quoted in older papers (2011) was a B-mode polarimeter; the 2024
design is a spectrum and polarisation mission with different sensitivities
(arXiv:1105.2044; arXiv:2405.20403) [src].

<!-- key: history-of-key-numbers -->

## Not verified
<!-- key: not-verified -->

- The selection, priors and data of the f_EDE < 0.016 bound of
  arXiv:2508.09025, which disagrees with all other EDE bounds here.
- Planck PR4 (NPIPE) EDE and varying-constant bounds.
- SPT-3G D1 bounds on varying constants and modified recombination (the
  combined SPT + ACT + Planck paper was not read here).
- Updated FIRAS temperature calibrations after 1996.
- Domain-wall and inflationary-tensor parameters fitted by NANOGrav.
- The full ACT DR6 PMF comparison with Planck + SPT (cut in the section
  read).
<!-- key: not-verified -->
