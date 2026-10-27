# Open questions — reionisation, 21 cm, line-intensity mapping

Scope: live controversies, method debates, forecasts and stale claims.
Snapshot: 2026-10-26

Numbers carry [src], [sec] or [der]. Forecasts are labelled.

## 1. Live controversies
<!-- key: live-controversies -->

### 1.1 Is the optical depth 0.06 or 0.09?
<!-- key: is-the-optical-depth-0-06-or-0-09 -->

The case for a high value. ΛCDM fitted to DESI BAO, the high-ℓ CMB and CMB lensing without low-ℓ
polarisation gives τ = 0.090 ± 0.012; τ ~ 0.09 removes the preference for sub-minimal neutrino
mass and lowers the preference for evolving dark energy from ≃ 3σ to ≃ 1.5σ [src: Sailer et al.
2025, arXiv:2504.16932, abstract]. An imposed prior τ = 0.11 ± 0.006 restores concordance with a positive
neutrino mass [src: Sullivan, de Belsunce & Ivanov 2026, arXiv:2606.30903, abstract]. The Planck one-sided 95% upper limit, τ_max = 0.0696 with slow-roll
inflation, rises to 0.075 if the low-ℓ temperature deficit is a physical feature, and to 0.082 with
all CMB+BAO data [src:
Jhaveri, Hu & Miranda 2026, arXiv:2606.20795, abstract].
Two October 2026 proposals raise τ by acting at z ≳ 10: a redshift-localised ionisation burst
from early-collapsing small-scale overdensities is preferred at ~2–2.5σ, with Δτ_burst ~ 0.012
and a total τ ~ 0.073 in both Planck PR3 and PR4 reprocessings [src: Weiner et al. 2026,
arXiv:2610.12552, abstract]; axion-like-particle birefringence that is larger during reionisation
suppresses the EE reionisation signal and makes τ ≃ 0.08–0.10 compatible with Planck low-ℓ EE, BB
and EB [src: Sirletti, Namikawa & Sherwin 2026, arXiv:2610.29764, abstract].

The case against.

- Direct probes. Replacing the low-ℓ EE data by quasar damping wings and dark pixels gives τ =
  0.067 ± 0.011, and a ≳ 2σ preference for dynamical dark energy survives [src: Montero-Camacho
  & Mao 2026, arXiv:2607.26373]. [src: abstract]
- Duration. With the endpoint fixed by the Lyα forest, τ = 0.09 requires a long reionisation, in
  ≈ 2σ tension with the SPT patchy-kSZ limit [src: Cain et al. 2025, arXiv:2505.15899, abstract].
- Exotic early ionisation does not supply the missing Δτ ≃ 0.03: primordial black holes give at
  most 0.008 [src: Sierra et al. 2026, arXiv:2608.01919, abstract]; decaying dark matter gives 0.064 →
  0.072 [src: Wang et al. 2026, arXiv:2609.39923, abstract]; a flash at z = 20–25 leaves the total
  unchanged in Planck PR4 [src: Upadhyay et al. 2026, arXiv:2609.24989, abstract].
- Adding dark-pixel and damping-wing-like forest limits to the full Planck likelihoods produces no
  significant shift in τ; the forest redistributes the optical depth in redshift [src: Lopez,
  D'Aloisio & Cain 2026, arXiv:2610.28765, abstract].
- A counter-example exists: weakly clustered Pop III.1 sources give τ = 0.087 while passing the
  most conservative 2σ kSZ limit [src: Aggarwal et al. 2026, arXiv:2606.19459, abstract].

Judgement an expert would make: the high τ that would relieve the CMB–BAO mismatch is a
diagnostic of that mismatch, not a reionisation measurement; the astrophysical probes available
today favour lower values, with errors that do not yet exclude it at high significance on their
own, and the comparison is not between independent numbers, since both use the same high-ℓ CMB
and BAO data [der]. The sibling skills `cosmo-cmb`, `cosmo-neutrinos-dark-matter` and
`cosmo-dark-energy-modified-gravity` carry the parameter consequences.

### 1.2 When and how did reionisation end?
<!-- key: when-and-how-did-reionisation-end -->

- Late end. Dark gaps persist to z ≃ 5.3 [src: Zhu et al. 2021, arXiv:2109.06295, abstract]; forward
  models complete reionisation by z ~ 5.2 [src: Gaikwad et al. 2023, arXiv:2304.02038, abstract]; a 500
  cMpc radiation-hydrodynamic simulation ends at z ≈ 5.2 with patches to 4.75 [src: Zier et al.
  2026, arXiv:2605.15310, abstract].
- Neutral islands or background fluctuations. Both fit the opacity distributions [src: Davies et
  al. 2023, arXiv:2312.08464]. Stacked damping wings give x_HI = 0.19 ± 0.07 at z = 5.6 [src:
  Spina et al. 2024, arXiv:2405.12273] and ≥ 0.061 ± 0.039 at z = 5.8 [src: Zhu et al. 2024,
  arXiv:2405.12275], described by their authors as unequivocal and robust evidence of islands.
  The dark-pixel limits (1σ upper limit ⟨x_HI⟩ ≤ 0.030 + 0.048 at z̄ = 5.481 [src:
  abstract]) leave room for an extended
  "soft landing" to z ~ 5.4 [src: Davies et al. 2025, arXiv:2510.25829].
- The mean free path at z = 5.93 depends on the proximity model: 1.53, 0.81 or 0.30 pMpc for an opacity exponent ξ = 0.33, 0.67 or 1.00 [src: Zhu
  et al. 2023, arXiv:2308.04614, Table 2]; an independent stack gives 0.75 (+0.65/−0.45) pMpc [src: Becker
  et al. 2021, arXiv:2103.16610].
- An awkward corollary: the ionising emissivity must fall by a factor 2–3 between z = 6 and 4.8
  [src: Tohfa et al. 2026, arXiv:2602.03923, abstract].
- The photon-budget estimate from JWST spectra ends reionisation at z ~ 5.8, earlier than the
  forest endpoint [src: Giovinazzo et al. 2026, arXiv:2607.22834, abstract].

### 1.3 Rapid or extended? Where is the midpoint?
<!-- key: rapid-or-extended-where-is-the-midpoint -->

| Statement | Value | Citation | Flag |
|---|---|---|---|
| tanh midpoint from τ | z_re = 8.14 ± 0.61 | Pagano et al. 2019, arXiv:1908.09856 | [src: abstract] |
| joint 21 cm limits + Lyman-line x_HI + CMB | z₅₀ = 7.16 (+0.15/−0.12), Δz < 1.8 (95%) | Sims et al. 2025, arXiv:2504.09725 | [src: abstract] |
| mean-free-path emulator | z_re = 6.58 ± 1.2 | arXiv:2602.03923 | [src: abstract] |
| Planck PR4 low-ℓ EE + dark pixels + damping-wing-like limit, FlexKnots | z₅₀ = 7.7 (+0.7/−0.8), Δz₉₀ < 11.4 (95%) | Lopez, D'Aloisio & Cain 2026, arXiv:2610.28765 | [src: abstract] |
| same + Lyα-forest Γ_HI, semi-analytic model (model-dependent) | z₅₀ = 7.4 (+0.2/−0.3), Δz₉₀ = 6.0 (+0.8/−1.0), A_z = 2.4 (+0.3/−0.7) | arXiv:2610.28765 | [src: abstract] |
| JWST galaxy damping wings | x_HI from 0.25 at z ~ 6 to 1.00 at z ~ 9: "a rapid transition around z ∼ 7–8" | Umeda et al. 2025, arXiv:2504.04683 | [src: abstract] |
| JWST Lyα fractions | mass-weighted x_HI = 0.38 (+0.14/−0.38) at z ~ 7 | Kundu et al. 2026, arXiv:2609.40363 | [src: abstract] |
| kSZ | Δ⁵⁰z < 3.8 (SPT-3G), Δz < 4.4 (ACT) | arXiv:2601.20551, arXiv:2506.06274 | [src: abstract] |

The midpoints are not directly comparable: the tanh value is the midpoint of a symmetric model
forced to reproduce τ, while the others come from asymmetric histories tied to a late endpoint.
A late midpoint with a late end and a low τ needs an early, slow start; the absence of a strong
damping wing in a z = 14.44 galaxy is offered as tentative evidence of early local ionisation
[src: Naidu et al. 2025, arXiv:2505.11263, abstract]. The JWST galaxy-based x_HI values have wide
intervals and a documented degeneracy with local absorbers [src: Huberty et al. 2025,
arXiv:2501.13899].

### 1.4 Which galaxies reionised the Universe?
<!-- key: which-galaxies-reionised-the-universe -->

- Too many photons: observed galaxies with JWST ξ_ion and low-z f_esc relations end reionisation
  too early [src: Muñoz et al. 2024, arXiv:2404.07250].
- Resolved by lower ξ_ion in mass-complete samples [src: Simmonds et al. 2024,
  arXiv:2409.01286].
- Reionisation "driven by the few": ~20% of sources give ~87% of the photons; bright galaxies
  dominate at z = 5–6 and faint ones contribute equally above z = 6 [src: arXiv:2607.22834, abstract].
- 21 cm limits combined with other data prefer haloes above ~2.6 × 10⁹ M_⊙ as the dominant
  sources, in a model-dependent analysis [src: arXiv:2504.09725, abstract].

### 1.5 The EDGES profile
<!-- key: the-edges-profile -->

Positions. The EDGES group has published its pipeline and raw data for scrutiny, calls the
question an ongoing debate, and is building evidence-based validation tools [src: Murray et al.
2026, arXiv:2605.16643; Sims et al. 2025, arXiv:2506.20042]. Critics showed non-unique and
unphysical foreground fits [src: Hills et al. 2018, arXiv:1805.01421], a plausible instrumental
origin [src: Bradley et al. 2018, arXiv:1810.09015] and weak Bayesian evidence once calibration
terms are modelled [src: Sims & Pober 2019, arXiv:1910.03165]. SARAS 3 rejects the best-fit
profile with 95.3% confidence, from a radiometer measurement in the 55–85 MHz band, and
concludes that the profile "is not of astrophysical origin" [src: Singh et al. 2021,
arXiv:2112.06778, abstract]. The depth itself depends on the beam correction: 370 mK
without it and up to 670 mK with one simulated beam model, in the original cross-checks
[src: arXiv:1910.03165, Sect. 2.1.3]; in the 2026 open re-processing, choices in the beam
factor move the foreground residuals by "a couple of mK" to just under 20 mK [src:
arXiv:2605.16643, Sect. VIII.3].
Multi-wavelength constraints predict a trough between −201 and
−68 mK, shallower than the 0.5 K of EDGES [src: Dhandha et al. 2025, arXiv:2508.13761].

### 1.6 HI intensity mapping: first auto-spectra and what they say
<!-- key: hi-intensity-mapping-first-auto-spectra-and -->

- CHIME's auto-spectrum disagrees with IllustrisTNG at 3.1–4.0σ on non-linear scales [src: CHIME
  Collaboration 2026, arXiv:2603.25680]. Whether this is HI astrophysics in the simulations or a
  residual of the measurement is open. [src: abstract]
- Amplitudes at low redshift: 10³ Ω_HI b_HI r = 0.86 ± 0.10 ± 0.12 in cross-correlation with WiggleZ
  (0.400 < z < 0.459)
  [src: Cunnington et al. 2022, arXiv:2206.01579, abstract] and 10³ Ω_HI b_HI = 1.271 (+1.080/−0.598) in
  auto-correlation [src: MeerKLASS Collaboration 2026, arXiv:2610.12158, abstract].
- Method debate: correct the foreground-cleaning signal loss with a transfer function [src:
  Cunnington et al. 2023, arXiv:2302.07034] or marginalise it in the likelihood [src:
  arXiv:2610.12158]. The argument for the second: cleaning also mixes modes, and a transfer
  function, "numerically equivalent to a renormalisation of the power spectrum estimator",
  can then bias the correlations between k bins on large scales [src: arXiv:2610.12158, Sect.
  11.4]. CHIME takes a third route and applies its stored filter to the simulations [src:
  arXiv:2511.19620, Sect. III.2.3].
- Single-dish against interferometric designs for BAO-scale work: single-dish reaches the large
  scales but has a coarse beam; interferometers lose low k_∥ to foreground filtering. No BAO
  measurement from intensity mapping was found in the searches run.

### 1.7 21 cm limits: avoidance, subtraction and statistics
<!-- key: 21-cm-limits-avoidance-subtraction-and -->

- Statistical foreground separation gains sensitivity (a factor ≳ 3 in simulations) but can
  suppress signal [src: Mertens et al. 2017, arXiv:1711.10834; Ceccotti et al. 2025,
  arXiv:2504.18534].
- The MWA "Gaussian component" limit assumes the cosmological signal is Gaussian and the leakage
  is not [src: Trott et al. 2025, arXiv:2508.04164]; a referee will ask how well that premise
  holds for a patchy reionisation signal, and what a signal-injection test returns.
- Deepest limits come from different k: 0.076 (LOFAR; arXiv:2503.05576, abstract), 0.18 (MWA; arXiv:2508.04164, abstract), 0.34 (HERA; arXiv:2210.04912, abstract) h/Mpc. A model is
  needed to compare them.
- Sizes of the two risks differ greatly in the record: an avoidance pipeline corrects a total of
  5.5% (z = 10.4) and 7.2% (z = 7.9) of power for loss [src: arXiv:2210.04912, Table 2], while the one
  retracted limit had loss "underestimated by a factor of > 1000" under empirical covariance
  weighting [src: Cheng et al. 2018, arXiv:1810.05175, Sect. V]. Injection into the real data,
  as LOFAR does with 100 signals per redshift [src: arXiv:2503.05576, Sect. 5.3], is the test
  to ask for.

### 1.8 JWST abundances and ΛCDM
<!-- key: jwst-abundances-and-lambdacdm -->

No analysis read here finds a violation of the halo baryon limit by spectroscopically confirmed
objects; models inside ΛCDM reproduce the luminosity functions to z = 14–17 with higher
efficiency or burstiness [src: Prada et al. 2026, arXiv:2604.18683, abstract; Lagos et al. 2026,
arXiv:2609.03537, abstract]. The open question is astrophysical: why star formation is so efficient or
bursty at z > 10. `cosmo-tensions-anomalies` tracks this as a tension.

## 2. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

| Question | Deciding data | Expectation | Citation | Flag |
|---|---|---|---|---|
| EDGES profile | deeper NenuFAR and HERA Phase II Cosmic Dawn limits; a second global-signal instrument | NenuFAR needs an order of magnitude more depth to test EDGES-compatible fluctuation models | Munshi et al. 2025, arXiv:2507.10533 | [src] |
| Cosmic Dawn power spectrum | — | predicted 8.7 mK² ≲ Δ²₂₁(z = 15) ≲ 197 mK² at 95% CI in the k bin where HERA limits are strongest (k ≈ 0.35 h/Mpc) [src: arXiv:2508.13761, Sect. 3.2]; best NenuFAR 2σ limit Δ²₂₁ < 4.6 × 10⁵ mK² at z = 20.3, k = 0.038 h/cMpc [src: arXiv:2507.10533, abstract] | arXiv:2508.13761; arXiv:2507.10533 | [src: Sect. 3.2; abstract] |
| EoR power spectrum | full HERA Phase II seasons | only two weeks with 180 antennas analysed so far; mutual coupling must be modelled | HERA Collaboration 2025, arXiv:2511.21289 | [src: Sect. I] |
| τ independent of Planck | large-angle polarisation from space; 21 cm clustering | 21 cm τ competitive only with a clean wedge and ~5 years of data (**forecast**) | Sailer, Chen & White 2022, arXiv:2205.11504 | [src] |
| τ from polarised SZ | future CMB × galaxy data | a factor ~3 tighter than today's −0.01 ± 0.14 (**forecast**) | Krywonos et al. 2026, arXiv:2607.16071 | [src: abstract] |
| Duration | kSZ with better tSZ–CIB separation | — | Chaubal et al. 2026, arXiv:2601.20551 | [src] |
| x_HI at z > 6 with small errors | larger quasar samples with the new continuum methods | a single spectrum cannot do it; samples are needed | Hennawi et al. 2024, arXiv:2406.12070 | [src] |
| HI BAO | CHORD (2028), SKA-Mid wide survey | SKA-Mid Wide Band 1 Survey: 20,000 deg², z = 0.35–3, 10,000 h on sky (**forecast** survey definition) | arXiv:2607.09374; Wolz et al. 2026, arXiv:2607.03259 | [src: Sect. 2.1 of arXiv:2607.03259] |
| CO power spectrum | COMAP five-year data | S/N 9–17 (**forecast** made in 2021) | Cleary et al. 2021, arXiv:2111.05927 | [src: abstract] |
| [CII] at z > 5 | CCAT Deep Spectroscopic Survey | shot-noise regime first (**forecast**) | Dev et al. 2026, arXiv:2607.20404 | [src] |

## 3. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

| Claim still seen | Status | Correcting paper |
|---|---|---|
| "EDGES detected the cosmic-dawn 21 cm signal." | Unconfirmed; the only independent test rejects the profile at 95.3%. | arXiv:2112.06778, abstract |
| "EDGES requires dark-matter cooling of the gas." | One of three options; an instrumental origin fits the data as well. | arXiv:1810.09015, arXiv:1910.03165 |
| "Reionisation was complete at z = 6." | Dark gaps persist to z ≃ 5.3 (arXiv:2109.06295, abstract); x_HI = 0.19 ± 0.07 at z = 5.6 is claimed (arXiv:2405.12273, abstract). | arXiv:2109.06295, arXiv:2405.12273 |
| "The Gunn–Peterson trough measures the neutral fraction." | A dark trough gives only an upper limit on the neutral volume; a measurement needs the damping wing. | arXiv:2510.25829 |
| "τ ≈ 0.09 has been measured." | It is the value ΛCDM needs when low-ℓ EE is discarded (arXiv:2504.16932, abstract); Planck 2018 gives 0.054 ± 0.007 (arXiv:1807.06209, abstract) and the SRoll2 reprocessing 0.059 ± 0.006 (arXiv:1908.09856, abstract). | arXiv:2504.16932, arXiv:1807.06209, arXiv:1908.09856, arXiv:2103.14378 |
| "The PAPER-64 limit is the deepest 21 cm limit." | Withdrawn for signal loss; superseded by the 2019 re-analysis and by HERA, LOFAR, MWA. | arXiv:1810.05175, arXiv:1909.02085 |
| "HERA detected IGM heating." | HERA sets upper limits that exclude an unheated IGM; nothing is detected. | arXiv:2210.04912 |
| "21 cm cosmology has only cross-correlation detections." | CHIME detected the auto-spectrum at 12.5σ (November 2025); MeerKLASS at S/N 6.2 (October 2026). | arXiv:2511.19620, arXiv:2610.12158, abstracts (abstract of each) |
| "21 cm intensity mapping measures Ω_HI." | It measures Ω_HI b_HI (auto) or Ω_HI b_HI r (cross), or CHIME's A_HI. | arXiv:1208.0331, arXiv:2202.01242 |
| "kSZ measures the duration of reionisation, Δz ≈ 1." | That was SPT 2020 with a tSZ-bispectrum prior; SPT-3G D1 finds lower kSZ power and quotes limits only. | arXiv:2002.06197, arXiv:2601.20551 |
| "COMAP detected CO at z ~ 3." | Upper limits; the spectrum is consistent with zero. | arXiv:2406.07511 |
| "JWST galaxies are too massive for ΛCDM." | The 2022 statement concerned photometric candidates at the edge of the limit; later models fit the data in ΛCDM. | arXiv:2208.01611, arXiv:2604.18683 |
| "JWST damping wings give precise x_HI(z)." | Local absorbers are degenerate with the IGM wing at prism resolution. | arXiv:2501.13899 |
| "MeerKLASS analyses are blinded." | "Blind" there means blind component separation. | arXiv:2302.07034 |

## Not verified
<!-- key: not-verified -->

- One 2026 paper that `cosmo-cmb` cites for reionisation data siding against a high τ
  (identifier 2601.09644 in its bibliography) was not read in this session and is not in this
  bibliography.
- The Planck 2015 τ value is known here only as quoted by arXiv:1502.02024 (0.066 ± 0.012);
  the WMAP nine-year value was not read. [src: abstract]
- Frequency coverage of the full EDGES profile against the SARAS 3 band: only the SARAS band
  and the EDGES centre and width were read; whether SARAS 3 covers the whole EDGES band was not
  read in either paper and is an inference [der].
- Forecasts for kSZ with Simons Observatory and SPT-3G, and for SKA-Low reionisation power
  spectra, were seen in search results but not recorded.
- Lyα intensity mapping (BOSS/eBOSS/DESI cross-correlations, HETDEX) was not found by the
  searches run.
- Helium reionisation is outside the searches run; see `cosmo-lyman-alpha` for the thermal
  history.
