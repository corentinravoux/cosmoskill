# Results — reionisation, 21 cm, line-intensity mapping

Scope: current headline measurements and the history of the key numbers.
Snapshot: 2026-10-07

## 1. Reionisation history

### 1.1 Thomson optical depth τ

All values are 68% intervals in flat ΛCDM with a tanh (near-instantaneous) reionisation unless stated. The sibling
`cosmo-cmb` holds the likelihood-level discussion; this table records what was read at source for this skill.

| τ | Data and method | Citation | Flag |
|---|---|---|---|
| 0.058 ± 0.012 | Planck TT + low-ℓ HFI polarisation, instantaneous model | Planck Collaboration 2016, arXiv:1605.03507 | [src] |
| 0.055 ± 0.009 | Planck HFI low-ℓ EE only, first HFI-based value | Planck Collaboration 2016, arXiv:1605.02985 | [src] |
| 0.054 ± 0.007 | Planck 2018 legacy (PR3), combined temperature, polarisation and lensing, base ΛCDM | Planck Collaboration 2018, arXiv:1807.06209 | [src] |
| 0.0566 (+0.0053/−0.0062) | SRoll2 HFI maps, large-scale polarisation only | Pagano et al. 2019, arXiv:1908.09856 | [src] |
| 0.059 ± 0.006 | SRoll2 low-ℓ + Planck low-ℓ TT + high-ℓ TTTEEE; z_re = 8.14 ± 0.61 | arXiv:1908.09856 | [src] |
| 0.0627 (+0.0050/−0.0058) | SRoll2 "momento" low-ℓ TTTEEE + CamSpec high-ℓ | de Belsunce et al. 2021, arXiv:2103.14378 | [src] |
| 0.059 ± 0.006 | Planck PR4, tanh model (control fit of a flash-reionisation study) | Upadhyay et al. 2026, arXiv:2609.24989 | [src] |
| 0.061 ± 0.007 | Planck PR4, tanh + flash at high z | arXiv:2609.24989 | [src] |
| < 0.0696 (95%, one-sided) | Planck primary data, slow-roll inflation, standard reionisation | Jhaveri, Hu & Miranda 2026, arXiv:2606.20795 | [src] |
| 0.090 ± 0.012 | DESI BAO + high-ℓ CMB + CMB lensing, **no** low-ℓ polarisation | Sailer et al. 2025, arXiv:2504.16932 | [src] |
| > 0.074 (95%, one-sided) | all CMB except large-angle polarisation + BAO | arXiv:2606.20795 | [src] |
| 0.067 ± 0.011 | CMB without low-ℓ EE + BAO + quasar damping wings + dark pixels, Gompertz reionisation, w0wa | Montero-Camacho & Mao 2026, arXiv:2607.26373 | [src] |
| −0.01 ± 0.14 | polarised SZ bispectrum (Planck, ACT × unWISE, CIB); a non-detection | Krywonos et al. 2026, arXiv:2607.16071 | [src] |

Reading of the table. The Planck legacy value and the later reprocessings of the HFI low-ℓ polarisation lie between
0.054 and 0.063 with σ ≈ 0.006–0.007 [src: rows above]. The sibling `cosmo-cmb` quotes the range 0.051–0.063; its
lower end comes from a PR4 analysis cited there that was not read for this skill. The value 0.090 ± 0.012 is not a
measurement of reionisation: it is what ΛCDM needs to reconcile DESI BAO with the high-ℓ CMB and lensing once the
low-ℓ EE data are dropped, and Sailer et al. put it at "≃ 3–5σ" from the Planck low-ℓ polarisation [src:
arXiv:2504.16932]. Adding reionisation-era astrophysical data in place of the low-ℓ EE likelihood pulls τ back to
0.067 ± 0.011 [src: arXiv:2607.26373].

### 1.2 Attempts to raise τ, and their outcome

| Mechanism | Outcome | Citation | Flag |
|---|---|---|---|
| Primordial-black-hole evaporation at high z | boost of at most Δτ ≃ 0.008 against the Δτ ≃ 0.03 needed | Sierra et al. 2026, arXiv:2608.01919 | [src] |
| Decaying dark matter (χ → e⁺e⁻, 1 GeV) | marginalised τ rises from 0.064 to 0.072; 68% intervals stay below 0.08 for 2 MeV–7 GeV | Wang et al. 2026, arXiv:2609.39923 | [src] |
| "Flash" ionisation at z = 20–25 | total τ unchanged (0.061 ± 0.007); PR4 mildly prefers a flash, PR3 gives only upper limits | arXiv:2609.24989 | [src] |
| Pop III.1 flash centred at z = 20 | a fiducial model reaches τ = 0.087 while evading the most conservative 2σ SPT patchy-kSZ limit | Aggarwal et al. 2026, arXiv:2606.19459 | [src] |
| Low-ℓ power deficit read as an inflationary feature | Planck 95% upper limit rises from 0.0696 to 0.075, and to 0.082 with all CMB + BAO | arXiv:2606.20795 | [src] |
| Prior τ = 0.11 ± 0.006 imposed by hand | Σm_ν = 0.10 (+0.04/−0.05) eV in ΛCDM; a concordance exercise, not a measurement | Sullivan, de Belsunce & Ivanov 2026, arXiv:2606.30903 | [src] |
| Non-monotonic history with a z ≳ 12 component | claimed necessary to fit Planck τ, patchy-kSZ limits and the Lyα endpoint together; relaxes Σm_ν < 0.39 eV (95%) | Wang & Shan 2026, arXiv:2606.27903 | [src] |

### 1.3 Neutral fraction against redshift

Volume-averaged ⟨x_HI⟩ unless noted. Limits from dark pixels are model-independent upper limits; damping-wing and
Lyα-visibility values depend on a reionisation-topology model and on the assumed intrinsic spectrum.

| z | ⟨x_HI⟩ | Probe and sample | Citation | Flag |
|---|---|---|---|---|
| 5.481 | ≤ 0.030 + 0.048 (1σ upper limit) | dark pixels, Lyβ + Lyγ, 34 XQR-30 quasars | Davies et al. 2025, arXiv:2510.25829 | [src] |
| 5.654 | ≤ 0.095 + 0.037 | same | arXiv:2510.25829 | [src] |
| 5.831 | ≤ 0.191 + 0.056 | same | arXiv:2510.25829 | [src] |
| 6.043 | ≤ 0.199 + 0.087 | same | arXiv:2510.25829 | [src] |
| 5.55, 5.75, 5.95 | ≤ 0.05, 0.17, 0.29 | Lyβ dark-gap lengths, 42 quasars | Zhu et al. 2022, arXiv:2205.04569 | [src] |
| 5.6 | 0.19 ± 0.07 (1σ), (+0.11/−0.16 at 2σ) | stacked damping wing next to Gunn–Peterson troughs | Spina et al. 2024, arXiv:2405.12273 | [src] |
| 5.9 | < 0.44 | same | arXiv:2405.12273 | [src] |
| 5.8 | ≥ 0.061 ± 0.039 | stacked damping wing at edges of Lyβ dark gaps | Zhu et al. 2024, arXiv:2405.12275 | [src] |
| 5.8, 5.95, 6.05, 6.55 | < 0.21, 0.20, 0.21, 0.18 (68%) | quasar damping wings, 23 of 42 XQR-30 quasars | Greig et al. 2024, arXiv:2404.12585 | [src] |
| 6.15 | 0.20 (+0.14/−0.12) | same | arXiv:2404.12585 | [src] |
| 6.35 | 0.29 (+0.14/−0.13) | same | arXiv:2404.12585 | [src] |
| 7.09 | 0.48 ± 0.26 | damping wing, ULAS J1120+0641, marginalised over quasar lifetime 10³–10⁸ yr | Davies et al. 2018, arXiv:1802.06066 | [src] |
| 7.54 | 0.60 (+0.20/−0.23) | damping wing, ULAS J1342+0928 | arXiv:1802.06066 | [src] |
| 7.12 → 9.91 | 0.53 (+0.18/−0.47) → 0.92 (+0.08/−0.10) | galaxy damping wings, 27 JWST/NIRSpec galaxies, 4 stacks | Umeda et al. 2023, arXiv:2306.00487 | [src] |
| ~5, 6, 7, 9, 10 | 0.00 (+0.12/−0.00), 0.25 (+0.10/−0.20), 0.65 (+0.27/−0.35), 1.00 (+0.00/−0.20), 1.00 (+0.00/−0.40) | 581 JWST/NIRSpec galaxies, Gunn–Peterson + damping wing | Umeda et al. 2025, arXiv:2504.04683 | [src] |
| ~7, 8, 11 | 0.38 (+0.14/−0.38), 0.57 (+0.23/−0.57), 0.93 (+0.05/−0.17) (mass-weighted; EW > 25 Å) | JWST Lyα-emitter fractions against THESAN and a semi-analytic model | Kundu, Lidz & Sun 2026, arXiv:2609.40363 | [src] |
| ~7, 8, 11 | 0.52 (+0.09/−0.21), 0.68 (+0.12/−0.39), 0.89 (+0.11/−0.15) (EW > 10 Å) | same | arXiv:2609.40363 | [src] |
| 5.2, 5.8, 6.7, 7.7, 9.8 | ceilings 0.36, 0.76, 0.74, 0.84, 1.0 | upper envelope of Lyα escape, 250 DIVER galaxies | Zhu et al. 2026, arXiv:2608.19311 | [src] |

### 1.4 End of reionisation from the Lyα forest

- Long dark gaps: the fraction of sightlines with a gap longer than 30 h⁻¹Mpc is F₃₀ ≃ 0.9, 0.6 and 0.15 at z = 6.0,
  5.8 and 5.6, and the last long gap persists to z ≃ 5.3 (55 quasars) [src: Zhu et al. 2021, arXiv:2109.06295].
- Forward-modelled τ_eff distributions in 12 bins over 4.85 < z < 6.05 are "consistent with a model in which
  reionization completes by z ∼ 5.2"; between z ∼ 5 and z ∼ 6 the mean free path falls by a factor ∼ 6 and the neutral
  fraction rises by ∼ 10⁴ [src: Gaikwad et al. 2023, arXiv:2304.02038].
- Direct Lyman-continuum mean free path from stacked quasar spectra: λ_mfp = 9.33 (+2.06/−1.80), 5.40 (+1.47/−1.40),
  3.31 (+2.74/−1.34) and 0.81 (+0.73/−0.48) proper Mpc at z = 5.08, 5.31, 5.65 and 5.93 [src: Zhu et al. 2023,
  arXiv:2308.04614]. A re-analysis with radiative-transfer simulations and explicit proximity-zone modelling gives
  1.49 (+0.47/−0.52) pMpc at z = 6 and finds the environment and patchiness biases minimal [src: Satyavolu et al.
  2023, arXiv:2311.06344].
- An emulator of the mean free path trained on 2 h⁻¹Mpc radiative-transfer boxes gives a reionisation midpoint z_re =
  6.58 ± 1.2 and "10% neutral still at z < 5.8 (6.3) at 1 (2)σ", with an ionising emissivity falling by a factor 2–3
  between z = 6 and 4.8 [src: Tohfa et al. 2026, arXiv:2602.03923].
- The alternative reading, strong ionising-background fluctuations with a short and spatially varying mean free path
  and no explicit residual neutral islands, also describes the XQR-30 τ_eff distributions [src: Davies et al. 2023,
  arXiv:2312.08464]. The stacked damping-wing detections (table above) are the evidence quoted against it.
- An ionising-photon budget built from 1428 JWST/NIRSpec spectra at 5 < z < 10 gives reionisation ending at z ∼ 5.8,
  with about 20% of sources (those with f_esc > 10%) producing about 87% of the ionising photons [src: Giovinazzo et
  al. 2026, arXiv:2607.22834].
- The Lumina radiation-hydrodynamic simulation (500 cMpc box, 2 × 6000³ elements) predicts a late, stellar-driven
  reionisation with the median sub-volume ionised by z ≈ 5.2 and residual neutral patches to z ≈ 4.75, with τ in
  agreement with Planck [src: Zier et al. 2026, arXiv:2605.15310].

### 1.5 Patchy kinetic SZ

The kSZ power at ℓ = 3000 is the sum of a late-time (homogeneous) part and a reionisation (patchy) part; the duration
limit depends on the template assumed for the first. Definitions of "duration" differ between papers and must be
quoted.

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| D_3000^kSZ | 3.0 ± 1.0 μK² (first ≥ 3σ kSZ power) | SPT-SZ 2540 deg² + SPTpol 500 deg² | Reichardt et al. 2020, arXiv:2002.06197 | [src] |
| Δz_re | 1.0 (+1.6/−0.7); < 4.1 at 95% | same, with the tSZ bispectrum prior | arXiv:2002.06197 | [src] |
| D_3000^kSZ | 1.75 ± 0.86 μK² (free angular shapes) | SPT-3G D1, 1646 deg², two years, 95/150/220 GHz | Chaubal et al. 2026, arXiv:2601.20551 | [src] |
| Δ⁵⁰z_re (x_e 25%→75%) | < 3.8 at 95% (semi-analytic model) | same | arXiv:2601.20551 | [src] |
| Δ⁹⁰z_re (x_e 5%→95%) | < 6.1 at 95% (AMBER simulations) | same | arXiv:2601.20551 | [src] |
| Δz_rei | < 4.4 ("conservative"; minimal low-z kSZ, midpoint from τ) | ACT DR6 multi-frequency spectra | Beringue et al. 2025, arXiv:2506.06274 | [src] |
| Δz_re,50 | < 4.5 at 95% (Gunn–Peterson prior) | kSZ trispectrum, SPT + Herschel-SPIRE, 100 deg² | Raghunathan et al. 2024, arXiv:2403.02337 | [src] |
| Δz (symmetric model) | < 2.8 | Planck + ACT/SPT kSZ amplitude | arXiv:1605.03507 | [src] |

The SPT trispectrum rejects zero at 10.3σ, but the signal is dominated by CMB lensing and foregrounds and no kSZ-only
excess is detected [src: arXiv:2403.02337]. The SPT-3G D1 paper states that its SZ powers depend on the modelling of
the tSZ–CIB correlation, so the fall from 3.0 ± 1.0 to 1.75 ± 0.86 μK² is not a like-for-like update [src:
arXiv:2601.20551]. With the end of reionisation pinned by the Lyα forest, τ becomes a probe of duration, and τ = 0.09
is then in ≈ 2σ tension with the SPT patchy-kSZ limits [src: Cain et al. 2025, arXiv:2505.15899]. Patchy screening and
polarised SZ are covered in `cosmo-cmb-lss-cross-correlations`.

### 1.6 Lyα emitters as a reionisation probe

- JWST/NIRISS slitless (PASSAGE): four emitters at 7.5 ≤ z ≤ 9.5 in four pointings; the luminosity function drops by a
  factor ≲ 10 relative to post-reionisation, less than pre-JWST expectations, and the emitters are inferred to sit in
  ionised bubbles ⪆ 2 physical Mpc [src: Runnholm et al. 2025, arXiv:2502.19174].
- The z ∼ 5–6 baseline needed to interpret z > 6 visibility: 45 ± 5% of M_UV = −19.5 galaxies have EW > 25 Å (236
  galaxies, 62 detections, MMT/Binospec), with a median velocity offset of 258 km/s; the observed profiles are broader
  than the z ∼ 2 templates used before JWST, which raises the predicted transmission through a neutral IGM [src:
  Prieto-Lyon et al. 2025, arXiv:2509.18302].
- Neutral fractions inferred from the JWST emitter fractions are in the table of section 1.3 (arXiv:2609.40363,
  arXiv:2608.19311).

## 2. 21 cm global signal

| Statement | Value | Citation | Flag |
|---|---|---|---|
| EDGES low-band claimed detection | flattened absorption profile centred at 78 MHz, FWHM 19 MHz, amplitude 0.5 K, "more than a factor of two greater than the largest predictions" | Bowman et al. 2018, arXiv:1810.05912 | [src] |
| EDGES timing inference | stars had produced a Lyα background by 180 Myr after the Big Bang; gas heated above the radiation temperature less than 100 Myr later | arXiv:1810.05912 | [src] |
| SARAS 3 non-confirmation | radiometer spectrum in 55–85 MHz; the EDGES best-fitting profile "is rejected with 95.3% confidence" and is "not of astrophysical origin" | Singh et al. 2021, arXiv:2112.06778 | [src] |
| Foreground-model critique | the EDGES fit implies unphysical foreground parameters and is not unique | Hills et al. 2018, arXiv:1805.01421 | [src] |
| Ground-plane resonance alternative | 2-term foreground + three cavity-mode resonances: rms residual 20.8 mK (11 parameters) against 24.5 mK (9 parameters) for the EDGES 5-term foreground + flattened Gaussian | Bradley et al. 2018, arXiv:1810.09015 | [src] |
| Bayesian re-analysis with calibration systematics | models with a noise model and calibration-error terms are decisively preferred; those with a signal favour an amplitude A < 209 mK; no strong evidence for a signal over no signal | Sims & Pober 2019, arXiv:1910.03165 | [src] |
| SARAS 3 astrophysics | disfavours (68%) radio-luminous galaxies in haloes of 4.4 × 10⁵–1.1 × 10⁷ M_⊙ at z = 20, star-formation efficiency > 5%, and a synchrotron radio background exceeding the CMB by ≳ 6% at 1.42 GHz | Bevins et al. 2022, arXiv:2212.00464 | [src] |
| Prediction from multi-wavelength data | absorption trough depth −201 mK ≲ T_21,min ≲ −68 mK at z_min ≈ 10–16; Δ²₂₁(z = 15, k = 0.35 h/Mpc) between 8.7 and 197 mK² (HST + JWST UVLFs, X-ray and radio backgrounds, SARAS 3, HERA; model-dependent) | Dhandha et al. 2025, arXiv:2508.13761 | [src] |

Status on the snapshot date. No independent experiment has confirmed the EDGES profile; SARAS 3 is the only published
measurement that tests it directly, and it rejects it [src: arXiv:2112.06778]. The EDGES collaboration published its
full calibration and analysis pipeline as open source, together with the raw data of earlier papers, in May 2026 and
describes the question as an "ongoing debate" [src: Murray et al. 2026, arXiv:2605.16643]. A Bayesian framework from
the EDGES group (beam-factor chromaticity correction with null-test validation, "BaNTER") is demonstrated on
simulations only [src: Sims et al. 2025, arXiv:2506.20042]. No new sky measurement from REACH, MIST, PRIZM, LEDA or
EDGES-3 was returned by the date-sorted search of 2026-10-10.

## 3. 21 cm power-spectrum upper limits at z > 6

All entries are 2σ (95%) **upper limits** on Δ²₂₁(k); no interferometer has detected the cosmological 21 cm power
spectrum at z > 6. Limits are quoted as the papers quote them, either as Δ² in mK² or as (Δ)² with Δ in mK.

| Instrument | z | Limit | k [h Mpc⁻¹] | Integration | Citation | Flag |
|---|---|---|---|---|---|---|
| HERA Phase I | 7.9 | Δ² ≤ 457 mK² (≈ (21.4 mK)² [der: square root]) | 0.34 | 94 nights | HERA Collaboration 2022, arXiv:2210.04912 | [src] |
| HERA Phase I | 10.4 | Δ² ≤ 3496 mK² | 0.36 | 94 nights | arXiv:2210.04912 | [src] |
| HERA Phase I (first) | 7.9 | (30.76 mK)² | 0.192 | 18 nights, ~36 h | HERA Collaboration 2021, arXiv:2108.02263 | [src] |
| HERA Phase I (first) | 10.4 | (95.74 mK)² | 0.256 | same | arXiv:2108.02263 | [src] |
| HERA Phase II (first) | 7.05 | 1.78 × 10³ mK² | 0.70 | two weeks | HERA Collaboration 2025, arXiv:2511.21289 | [src] |
| HERA Phase II (first) | 16.78 | 1.13 × 10⁶ mK² | 0.55 | two weeks | arXiv:2511.21289 | [src] |
| LOFAR (NCP) | 10.1 | (68.7 mK)² | 0.076 | 10 nights [src: arXiv:2505.00373] | Mertens et al. 2025, arXiv:2503.05576 | [src] |
| LOFAR (NCP) | 9.1 | (54.3 mK)² | 0.076 | same | arXiv:2503.05576 | [src] |
| LOFAR (NCP) | 8.3 | (65.5 mK)² | 0.083 | same | arXiv:2503.05576 | [src] |
| LOFAR (3C196) | 9.16 | (146.61 mK)² | 0.078 | one 6-hour night | Ceccotti et al. 2025, arXiv:2504.18534 | [src] |
| MWA (EoR0) | 6.5 | (30.2 mK)² | 0.18 | 268 h | Nunhokee et al. 2025, arXiv:2505.09097 | [src] |
| MWA (EoR0) | 6.8 | (31.2 mK)² | 0.18 | 268 h | arXiv:2505.09097 | [src] |
| MWA (EoR0) | 7.0 | (39.1 mK)² | 0.21 | 268 h | arXiv:2505.09097 | [src] |
| MWA, Gaussian component | 6.5 | (23.0 mK)² EW; (21.7 mK)² = 470 mK² NS | 0.18 | 268 h | Trott et al. 2025, arXiv:2508.04164 | [src] |
| NenuFAR | 20.3 | 4.6 × 10⁵ mK² | 0.038 | 26.1 h | Munshi et al. 2025, arXiv:2507.10533 | [src] |
| NenuFAR | 17.0 | 5.0 × 10⁶ mK² | 0.041 | 23.6 h | arXiv:2507.10533 | [src] |
| PAPER-64 (re-analysis) | 7.48–10.87 | (300), (380), (200), (280), (1900), (1500) mK squared at z = 7.48, 8.13, 8.37, 8.68, 9.93, 10.87 | — | — | Kolopanis et al. 2019, arXiv:1909.02085 | [src] |

Notes on the table.

- The limits are at different k and cannot be ranked by the number alone. In Δ² the deepest quoted values are HERA
  Phase I at z = 7.9 (457 mK²) and the MWA Gaussian-component limit at z = 6.5 (470 mK²), at k = 0.34 and 0.18 h/Mpc
  respectively [src: arXiv:2210.04912, arXiv:2508.04164].
- LOFAR 2025 is a reprocessing of comparable data to the earlier LOFAR limits with a 2 to 4-fold improvement; the
  residual excess is attributed to distant-source foregrounds, beam-model errors and low-level RFI [src:
  arXiv:2503.05576].
- HERA Phase II covers 50–250 MHz (abstract; 47–234 MHz in the paper's introduction) and reports eight bands over 5.6 ≤ z ≤ 24.4; mutual coupling "has become our
  dominant systematic" and costs the modes k = 0.35–0.55 relative to Phase I [src: arXiv:2511.21289].
- The NenuFAR limit at z = 20.3 is more than an order of magnitude deeper than earlier Cosmic Dawn limits and starts
  to exclude only models stronger than the EDGES profile; an order of magnitude more is needed to test
  EDGES-compatible signals [src: arXiv:2507.10533].
- The 2015 PAPER-64 limit was withdrawn: the original pipeline suffered signal loss, and the 2019 re-analysis
  "supersede[s] all previous PAPER results" [src: Cheng et al. 2018, arXiv:1810.05175; arXiv:1909.02085].

What the limits exclude.

- HERA Phase I: the IGM was heated above the adiabatic-cooling limit by z = 10.4, ruling out "cold reionization"; the
  99% credible interval excludes the local L_X/SFR relation and requires heating by evolved low-metallicity stars [src:
  arXiv:2210.04912]. A 2026 re-interpretation with the 21cmEMUv3 emulator excludes L_X/SFR below 10^39.2 erg s⁻¹ M_⊙⁻¹
  yr at 95% [src: Breitman et al. 2026, arXiv:2606.00219].
- MWA: "first evidence of heated intergalactic medium at redshifts z = 6.5 to 7.0" [src: arXiv:2505.09097].
- Joint analysis of Planck and SPT, Lyman-line neutral fractions and HERA, LOFAR, MWA limits: midpoint z₅₀ = 7.16
  (+0.15/−0.12), duration Δz_re < 1.8 (95%), minimum halo mass ≳ 2.6 × 10⁹ M_⊙ ((1+z)/10)^(1/2); the authors caution
  that the inference is model-dependent [src: Sims et al. 2025, arXiv:2504.09725].

## 4. Post-reionisation HI intensity mapping

The measured quantity is a clustering amplitude, never Ω_HI alone: cross-correlations give Ω_HI b_HI r (r is the
HI–galaxy correlation coefficient), auto-spectra give Ω_HI b_HI or an amplitude that includes redshift-space
distortions. No BAO, growth-rate or dark-energy measurement from 21 cm intensity mapping exists on the snapshot date.

| Measurement | Value | z | Scales | Data | Citation | Flag |
|---|---|---|---|---|---|---|
| Cross-correlation, GBT × WiggleZ | Ω_HI b_HI r = [0.43 ± 0.07 (stat) ± 0.04 (sys)] × 10⁻³ | 0.6–1 (~0.8) | — | ~41 deg², 190 h | Masui et al. 2012, arXiv:1208.0331 | [src] |
| Cross-correlation, GBT × WiggleZ | [0.58 ± 0.09 ± 0.05] × 10⁻³ | ≃ 0.8 | k_eff = 0.31 h/Mpc | 100 deg² | Wolz et al. 2021, arXiv:2102.04946 | [src] |
| Cross-correlation, GBT × eBOSS ELG | [0.40 ± 0.09 ± 0.04] × 10⁻³ | ≃ 0.8 | 0.31 | same | arXiv:2102.04946 | [src] |
| Cross-correlation, GBT × eBOSS LRG | [0.35 ± 0.08 ± 0.03] × 10⁻³ | ≃ 0.8 | 0.31 | same | arXiv:2102.04946 | [src] |
| Cross-correlation, MeerKAT × WiggleZ | [0.86 ± 0.10 (stat) ± 0.12 (sys)] × 10⁻³, 7.7σ | 0.400–0.459 | k_eff ~ 0.13 | 10.5 h pilot, single-dish mode | Cunnington et al. 2022, arXiv:2206.01579 | [src] |
| Stacking, CHIME × eBOSS | 7.1σ (LRG), 5.7σ (ELG), 11.1σ (QSO); A_HI ≡ 10³ Ω_HI (b_HI + ⟨fμ²⟩) = 1.51 (+3.60/−0.97) at z = 0.84, 6.76 (+9.04/−3.79) at 0.96, 1.68 (+1.10/−0.67) at 1.20 | 0.78–1.43 | non-linear | 102 nights | CHIME Collaboration 2022, arXiv:2202.01242 | [src] |
| Cross-correlation, CHIME × eBOSS Lyα forest | 9σ | mean 2.3 (1.8–2.5) | k_∥ ≳ 0.13 Mpc⁻¹ kept | 88 days, 400–500 MHz | CHIME Collaboration 2023, arXiv:2309.04404 | [src] |
| **Auto-power spectrum, CHIME** | 12.5σ; sub-bands 8.7σ (z ~ 1.08) and 9.2σ (z ~ 1.24) | 1.01–1.34 | 0.4 < k < 1.5 h/Mpc | 94 nights, 608.2–707.8 MHz | CHIME Collaboration 2025, arXiv:2511.19620 | [src] |
| **Auto-power spectrum, MeerKLASS** (from internal cross-spectra of independent subsets) | S/N 6.2; 10³ Ω_HI b_HI = 1.271 (+1.080/−0.598) | 0.42 | 0.095 < k < 0.245 h/Mpc | ~236 deg², 2021 campaign, 971.2–1023.6 MHz | MeerKLASS Collaboration 2026, arXiv:2610.12158 | [src] |

Notes.

- CHIME's auto-spectrum is the first detection of the cosmological 21 cm signal in auto-correlation at z ~ 1 and does
  not rely on an external galaxy survey [src: arXiv:2511.19620]. It lies on non-linear scales (0.4 < k < 1.5
  h/Mpc); it is an astrophysical measurement, not yet a BAO measurement.
- Interpretation of the CHIME auto-spectrum: the amplitude parameter is A²_HI ≡ 10⁶ Ω²_HI (b²_HI + ⟨fμ²⟩)², and the
  measurement disagrees with IllustrisTNG at 3.1σ (TNG100) and 4.0σ (TNG300), attributed to non-linear redshift-space
  clustering of HI in the simulations and not to the total HI abundance [src: CHIME Collaboration 2026,
  arXiv:2603.25680]. The value of A_HI is not in the abstract and is not reproduced here.
- The CHIME stacking analysis is also sensitive to the tracer redshift bias and finds Δv = −66 ± 20 km/s for the eBOSS
  quasars [src: arXiv:2202.01242].
- The MeerKLASS auto-spectrum was posted on 2026-10-08. The subset auto-spectra still show excess power from
  unresolved systematics; the detection uses cross-spectra between observationally independent subsets and
  marginalises the signal loss of the foreground cleaning [src: arXiv:2610.12158].
- MeerKAT in interferometric mode (DEEP2, MIGHTEE) has yielded a "tentative detection as well as upper limits" on
  small-scale HI clustering [src: Mazumder et al. 2026, arXiv:2606.24730].
- Tianlai cylinder pathfinder: 20 days of drift scans at 714.4–781.7 MHz (z ≈ 0.82–0.99), a drone-measured beam,
  wavelet-domain PCA foreground removal and the first spherical Fourier–Bessel power-spectrum analysis of 21 cm data;
  no detection is claimed in the abstract [src: Deng et al. 2026, arXiv:2604.27465].

## 5. Line-intensity mapping (CO, [CII], Lyα)

State of the field in one sentence: outside the 21 cm line, no three-dimensional line-intensity power spectrum has
been detected; a 2026 methods paper states that "other lines that reveal large-scale structure or astrophysical
processes remain undetected" [src: Kramer et al. 2026, arXiv:2603.13218]. The detections that exist are of the mean
background by tomographic cross-correlation of broadband maps.

| Quantity | Value | Line, z | Data | Citation | Flag |
|---|---|---|---|---|---|
| P_CO(k) | −2.7 ± 1.7 × 10⁴ μK² Mpc³ over k = 0.051–0.62 Mpc⁻¹ | CO(1–0), z = 2.4–3.4 | COMAP Pathfinder, first 13 months | Cleary et al. 2021, arXiv:2111.05927 | [src] |
| ⟨Tb⟩² | < 49 μK² | same | same | arXiv:2111.05927 | [src] |
| k P_CO(k) | < 2400–4900 μK² Mpc² (95%) in each of the six deepest bins, 0.09 < k < 0.73 Mpc⁻¹ | CO(1–0), z = 2.4–3.4 | COMAP Season 2 (two seasons), feed-group pseudo cross-spectrum | Stutzer et al. 2024, arXiv:2406.07511 | [src] |
| Consistency with zero | probability-to-exceed ≈ 34%; 2.7σ excess in the most sensitive bin; 312 difference-map null tests pass | same | same | arXiv:2406.07511 | [src] |
| Stack on quasars | no detection; L′_CO < 10.0 × 10¹⁰ K km s⁻¹ pc² (95%) in an ~18 cMpc box; ~3σ tension with the brightest models | CO(1–0), z ~ 3 | COMAP Season 2 × eBOSS/DESI quasars | Dunne et al. 2025, arXiv:2510.23568 | [src] |
| Mean CO background | detected at 7σ across the rotational ladder | 0 < z < 4.2 | tomographic clustering of diffuse broadband intensity with reference galaxies | Chiang 2026, arXiv:2602.02658 | [src] |
| Mean [CII] background | detected at 3σ | 0 < z < 4.2 | same | arXiv:2602.02658 | [src] |
| Ω_H2 from CO(1–0) | "about twice that resolved in galaxy surveys"; global depletion time ~ 1 Gyr | — | same | arXiv:2602.02658 | [src] |

Notes.

- COMAP Season 2 is about an order of magnitude more sensitive than Early Science in its six deepest bins and is the
  strongest direct constraint on the 3D CO(1–0) power spectrum [src: arXiv:2406.07511]. The Early Science forecast was
  a detection after five years at S/N 9–17, and S/N 19 for the CO–galaxy cross-spectrum (**forecast**) [src:
  arXiv:2111.05927].
- [CII] at reionisation redshifts: TIME has commissioning data on a Galactic field only (2021–2022 run, Sgr A) and no
  extragalactic result [src: Yang et al. 2025, arXiv:2511.09473]. CCAT/FYST EoR-Spec results are simulations: the
  filter-and-bin pipeline keeps > 80% of the power at k ≳ 0.5 Mpc⁻¹ and < 20% at k ≲ 0.1 Mpc⁻¹, so only the shot-noise
  regime is recoverable with the first pipeline (**forecast**) [src: Dev et al. 2026, arXiv:2607.20404].
- JWST-era burstiness of star formation multiplies the LIM shot noise by a line-dependent boost B_λ: at z ~ 6, B_Hα ≃
  7 and B ~ 2.5–3.5 for [CII], CO and UV. This helps auto-spectrum detection and hurts BAO-type applications [src:
  Kovetz et al. 2026, arXiv:2605.13967].
- SPHEREx: launched 11 March 2025; 102 bands over 0.75–5.0 μm; two deep fields near the ecliptic poles are the
  intensity-mapping fields. No intensity-mapping result was found on the snapshot date [src: Bock et al. 2025,
  arXiv:2511.02985].

## 6. JWST early galaxies as a cosmological constraint

The cosmological question is narrow: does any observed abundance exceed what the ΛCDM halo mass function and the
cosmic baryon fraction allow? The sibling `cosmo-tensions-anomalies` treats it as a tension; the entries below are
what was read at source here.

| Statement | Content | Citation | Flag |
|---|---|---|---|
| The baryon-budget test | the halo mass function sets an absolute upper limit on n(> M_⋆, z) and ρ_⋆(> M_⋆, z); the most massive early JWST **candidates** at z ~ 7–10 "lie at the very edge of these limits" | Boylan-Kolchin 2022, arXiv:2208.01611 | [src] |
| ΛCDM + empirical galaxy model at 7 ≤ z ≤ 14 | UniverseMachine on the Uchuu simulation matches the UV luminosity functions over five magnitudes; star-formation efficiency rises with z at fixed halo mass, reaching 2–3% of baryons by z = 10–12; earlier claims of insufficient stellar mass at z = 8 are attributed to AGN contamination, dust and missing MIRI data | Prada et al. 2026, arXiv:2604.18683 | [src] |
| Semi-analytic model tuned at z = 0 | the Shark model reproduces the UV luminosity function up to z = 17 without changing baryon physics, through starbursts triggered by disk instabilities | Lagos et al. 2026, arXiv:2609.03537 | [src] |
| Highest spectroscopic redshift read here | MoM-z14, z_spec = 14.44 ± 0.02, M_UV = −20.2, 280 Myr after the Big Bang; number density of bright z ~ 14–15 sources 182 (+329/−105) times pre-JWST consensus models (from ~350 arcmin²) | Naidu et al. 2025, arXiv:2505.11263 | [src] |
| Photon-budget "crisis" | observed galaxies (M_UV < −15), with JWST ξ_ion and low-z-calibrated f_esc taken at face value, would end reionisation too early, in tension with the CMB and the Lyα forest | Muñoz et al. 2024, arXiv:2404.07250 | [src] |
| Its proposed resolution | a stellar-mass-complete JADES sample of 15,721 galaxies at 3 ≤ z ≤ 9 finds a much milder evolution of ξ_ion; galaxies with −20 < M_UV < −16 and a reasonable f_esc reionise the Universe without exceeding the budget | Simmonds et al. 2024, arXiv:2409.01286 | [src] |

Reading. The factor of ~180 for MoM-z14 is against pre-JWST galaxy-formation models, not against the ΛCDM halo
abundance; both 2026 models above reproduce the z > 10 luminosity functions inside ΛCDM by raising star-formation
efficiency or burstiness. The photon-budget problem is a tension between galaxy observables and the reionisation
history (τ, section 1.1; the Lyα endpoint, section 1.4), not with cosmological parameters. The absence of a strong
damping wing in MoM-z14 is reported as tentative evidence of local ionisation at a redshift where models predict a
neutral IGM [src: arXiv:2505.11263].

## 7. History of the key numbers

### τ

| Year | Value | What changed | Citation | Flag |
|---|---|---|---|---|
| 2016 | 0.055 ± 0.009 (EE only); 0.058 ± 0.012 (with TT) | first use of HFI low-ℓ polarisation; "reducing significantly the central value and uncertainty" relative to earlier data | arXiv:1605.02985, arXiv:1605.03507 | [src] |
| 2018 | 0.054 ± 0.007 | Planck legacy release | arXiv:1807.06209 | [src] |
| 2019 | 0.0566 (+0.0053/−0.0062); 0.059 ± 0.006 with TT and high-ℓ | SRoll2 map-making removes the dipole-distortion residual; uncertainty down ~40% | arXiv:1908.09856 | [src] |
| 2021 | 0.0627 (+0.0050/−0.0058) | joint low-ℓ temperature–polarisation likelihood on SRoll2 maps, CamSpec high-ℓ | arXiv:2103.14378 | [src] |
| 2025 | 0.090 ± 0.012 **without** low-ℓ EE | DESI BAO enters; not a polarisation measurement | arXiv:2504.16932 | [src] |
| 2026 | 0.067 ± 0.011 without low-ℓ EE but with reionisation probes | astrophysical data replace the EE likelihood | arXiv:2607.26373 | [src] |

None of the pre-2025 values is superseded in the sense of being wrong; they are successive treatments of the same
Planck HFI data. The value to quote depends on the likelihood named.

### Duration of reionisation from kSZ

| Year | Value | Citation | Flag |
|---|---|---|---|
| 2016 | Δz < 2.8 (symmetric model, Planck + ACT/SPT kSZ amplitude) | arXiv:1605.03507 | [src] |
| 2020 | Δz = 1.0 (+1.6/−0.7), < 4.1 (95%); D_3000^kSZ = 3.0 ± 1.0 μK² | arXiv:2002.06197 | [src] |
| 2024 | Δz_re,50 < 4.5 (95%), trispectrum | arXiv:2403.02337 | [src] |
| 2025 | Δz_rei < 4.4 (ACT DR6, conservative) | arXiv:2506.06274 | [src] |
| 2026 | Δ⁵⁰z < 3.8, Δ⁹⁰z < 6.1 (95%); D_3000^kSZ = 1.75 ± 0.86 μK² | arXiv:2601.20551 | [src] |

The 2020 central value Δz = 1.0 should no longer be quoted as a measurement: the kSZ power it rested on has moved down
and the current SPT statement is an upper limit.

### Neutral fraction near z = 7

| Year | ⟨x_HI⟩ | Probe | Citation | Flag |
|---|---|---|---|---|
| 2018 | 0.48 ± 0.26 (z = 7.09) | one quasar damping wing | arXiv:1802.06066 | [src] |
| 2023 | 0.53 (+0.18/−0.47) (z = 7.12) | JWST galaxy stack | arXiv:2306.00487 | [src] |
| 2025 | 0.65 (+0.27/−0.35) (z ~ 7) | 581 JWST galaxies | arXiv:2504.04683 | [src] |
| 2026 | 0.38 (+0.14/−0.38) or 0.52 (+0.09/−0.21) (z ~ 7) | JWST Lyα fractions, two EW thresholds | arXiv:2609.40363 | [src] |

All four agree within their errors; the errors have not shrunk in eight years.

### 21 cm power-spectrum limits

| Year | Milestone | Citation | Flag |
|---|---|---|---|
| 2018–2019 | PAPER-64 limits withdrawn and replaced: (200 mK)² at z = 8.37 is the best of the re-analysis | arXiv:1810.05175, arXiv:1909.02085 | [src] |
| 2021 | HERA Phase I, 18 nights: (30.76 mK)² at z = 7.9, an order of magnitude deeper than before at that redshift | arXiv:2108.02263 | [src] |
| 2022 | HERA Phase I, 94 nights: 457 mK² at z = 7.9, a factor 2.1 better at that redshift (2.6 at z = 10.4) | arXiv:2210.04912 | [src] |
| 2025 | LOFAR reprocessing: 2 to 4 times deeper than its previous limits; MWA: (30.2 mK)² then (23.0 mK)² at z = 6.5; NenuFAR: first deep Cosmic Dawn limits; HERA Phase II: first limits over z = 5.6–24.4 | arXiv:2503.05576, arXiv:2505.09097, arXiv:2508.04164, arXiv:2507.10533, arXiv:2511.21289 | [src] |

The first HERA Phase II limit at z = 7.05 (1.78 × 10³ mK² at k = 0.70) is shallower than the Phase I limit at z = 7.9
(457 mK² at k = 0.34): Phase II so far uses two weeks of data and loses low-k modes to mutual coupling [src:
arXiv:2511.21289].

### HI intensity mapping

| Year | Milestone | Citation | Flag |
|---|---|---|---|
| 2012 | GBT × WiggleZ cross-correlation at z ~ 0.8 | arXiv:1208.0331 | [src] |
| 2021 | GBT × eBOSS and WiggleZ, three galaxy samples | arXiv:2102.04946 | [src] |
| 2022 | first interferometric detection (CHIME stacking); first multi-dish single-dish-mode detection (MeerKAT × WiggleZ, 7.7σ) | arXiv:2202.01242, arXiv:2206.01579 | [src] |
| 2023 | highest-redshift detection, z = 2.3 (CHIME × Lyα forest, 9σ) | arXiv:2309.04404 | [src] |
| 2025 | first auto-power detection at z ~ 1 (CHIME, 12.5σ) | arXiv:2511.19620 | [src] |
| 2026 | auto-spectrum on cosmological scales at z = 0.42 (MeerKLASS, S/N 6.2) | arXiv:2610.12158 | [src] |

### Other lines

COMAP: ⟨Tb⟩² < 49 μK² in 2021 [src: arXiv:2111.05927]; in 2024 a spectrum about ten times more sensitive, still
consistent with zero [src: arXiv:2406.07511]. The mean CO and [CII] backgrounds were first detected in 2026 by
tomographic cross-correlation, not by a line-intensity-mapping instrument [src: arXiv:2602.02658].

## Not verified

- The Planck PR4 τ values of the original PR4 likelihood papers (two entries of the `cosmo-cmb` bibliography) were not
  read here; the PR4 row of section 1.1 is the tanh control fit of arXiv:2609.24989.
- The XQR-30 mean-flux measurement that first placed the end of reionisation at z ≈ 5.3 (Bosman et al. 2022), the
  earlier mean-free-path measurement (Becker et al. 2021) and the late-reionisation model papers (Kulkarni et al.
  2019, Keating et al. 2020) are expected references that were not fetched; the z ≈ 5.3 statement here rests on
  arXiv:2109.06295, arXiv:2405.12273 and arXiv:2304.02038.
- The earlier LOFAR (2020) and MWA (2020) limits that the 2025 papers improve on were not read.
- The value of A_HI from the CHIME auto-spectrum is in the body of arXiv:2603.25680 and was not read.
- The MeerKAT interferometric auto-power detection (Paul et al. 2023) is known here only through arXiv:2606.25955.
- Pre-JWST Lyα-emitter-fraction inferences of x_HI at z ~ 7–8 were not fetched.
- No result was found for: EDGES high-band or EDGES-3, REACH, MIST, PRIZM, LEDA sky measurements after 2022; CONCERTO,
  mmIME, COPSS; Lyα intensity mapping; SPHEREx intensity mapping.

