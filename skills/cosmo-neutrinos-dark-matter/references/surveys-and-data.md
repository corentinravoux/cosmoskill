# Surveys and data — neutrino mass, light relics and dark-matter properties from structure

Scope: the experiments, samples and data releases behind the constraints in `results.md`, past, current and planned, with what each contributes and where its description lives.
Snapshot: 2026-10-07

Flags: `[src]` read in the cited paper this session; `[sec]` taken from a named secondary source (often a sibling skill, which holds the primary citation); `[der]` derived here. Forecasts are labelled **forecast**.

This domain owns almost no data set of its own. The cosmological inputs are described in `cosmo-cmb`, `cosmo-galaxy-clustering`, `cosmo-lyman-alpha` and `cosmo-supernovae`; this file records which release enters which constraint, and describes in full only the laboratory experiments and the small-scale-structure samples that have no other home.

## 1. What each data set contributes
<!-- key: what-each-data-set-contributes -->

| Constraint | Data that carry it | Data that only break degeneracies | Home of the data description |
|---|---|---|---|
| Σm_ν | BAO distances (Ω_m) + primary CMB (ω_b, ω_cdm, θ*) + CMB lensing (amplitude) | low-ℓ EE (τ), supernovae (dark-energy model), full shape | `cosmo-cmb`, `cosmo-galaxy-clustering` |
| N_eff | CMB damping tail and phase shift; primordial D/H and helium | BAO (pulls N_eff up through H0 r_d) | `cosmo-cmb`; §3.3 here |
| Mass ordering | oscillation splittings + the cosmological Σm_ν posterior | reactor (JUNO) and atmospheric data | §3.1 here |
| Thermal-relic warm dark matter | high-redshift, high-resolution Lyα P1D; Milky Way satellite counts; lensed-quasar flux ratios and arcs; stream density | thermal-history measurements; galaxy–halo models | `cosmo-lyman-alpha`; §3.4–3.6 here |
| Fuzzy dark matter, all of the dark matter | the same small-scale probes, plus dwarf-galaxy kinematics | — | §3.4–3.6 here |
| Ultralight sub-component | CMB spectra and lensing, galaxy full shape | — | `cosmo-cmb`, `cosmo-galaxy-clustering` |
| Dark matter–baryon or –neutrino scattering | CMB, Lyα, satellites, ultraviolet luminosity functions | — | this file |
| Self-interaction | cluster mergers, cluster and group profiles, rotation curves | — | §3.8 here; cluster data in `cosmo-clusters` |
| Decays, dark radiation | CMB + BAO + supernovae + full shape | S8 priors from weak lensing | `cosmo-cmb`, `cosmo-weak-lensing` |

## 2. Past data sets (superseded for these questions, still cited)
<!-- key: past-data-sets-superseded-for-these-questions -->

| Data | Role at the time | What replaced it | Citation | Flag |
|---|---|---|---|---|
| Planck 2018 (PR3) + BOSS-era BAO | Σm_ν < 0.12 eV, N_eff = 2.99 ± 0.17: the last pre-DESI reference | DESI DR1 (2024) and DR2 (2025) BAO; ACT DR6 and SPT-3G D1 at high ℓ | arXiv:1807.06209 | [src: abstract] |
| WMAP + Kim et al. and Croft et al. Lyα spectra | first thermal-relic and sterile-neutrino limits from the forest (0.55 and 2.0 keV) | z > 4 high-resolution samples | arXiv:astro-ph/0501562 | [src] |
| WMAP, Planck, ACT, SPT + WiggleZ | first ultralight-axion fraction limits over 10⁻³² to 10⁻²⁵·⁵ eV | Planck 2018 + BOSS; DESI DR1 full shape; ACT DR6 lensing | arXiv:1410.2896 | [src] |
| SDSS DR14 Lyα P1D (z < 4.5) + XQ-100 | Σm_ν < 0.11 eV with Planck; m_WDM > 5.3 keV | DESI DR1 P1D for the neutrino side (see `cosmo-lyman-alpha`); no DESI warm-dark-matter limit found | arXiv:1911.09073 | [src: abstract] |
| Bullet Cluster 1E 0657-56 | first self-interaction limits from a merger | merger ensembles, relaxed-cluster profiles | arXiv:0704.0261 | [src: abstract] |
| Planck 2015-era CMB | strongly self-interacting neutrino mode | ACT DR6 + Planck: no evidence | arXiv:1902.00534, arXiv:2503.14454 | [src] |

## 3. Current data sets
<!-- key: current-data-sets -->

### 3.1 Laboratory neutrino experiments
<!-- key: laboratory-neutrino-experiments -->

| Experiment / fit | What it measures | Current statement | Citation | Flag |
|---|---|---|---|---|
| NuFIT 6.0 global oscillation fit | mass splittings, mixing angles, ordering | lower limits Σm_ν ≥ 0.059 eV (normal), ≥ 0.10 eV (inverted) as used by DESI; orderings fit almost equally well without the Super-Kamiokande atmospheric table, Δχ² = 6.1 for normal ordering with it | Esteban et al. 2024, arXiv:2410.05380; arXiv:2503.14744 §4.1 | [src] abstract; minimum sums [sec] |
| KATRIN, first five campaigns | endpoint of the tritium β spectrum; the effective electron-antineutrino mass | m_ν < 0.45 eV (90% CL) from 259 measurement days and 36 million electrons; m_ν² = −0.14 (+0.13/−0.15) eV² | Aker et al. 2024, arXiv:2406.13516 | [src: abstract] |

| KATRIN, status in the January 2026 review | — | "about to reach its target sensitivity of the neutrino mass of less than 300 meV"; the experiment then turns to a keV sterile-neutrino search and later to KATRIN++ (quantum read-out, atomic tritium source) | Drexlin & Weinheimer 2026, arXiv:2601.00248 | [src: abstract] |
| JUNO | reactor antineutrinos at a mean baseline of 52.5 km | 207.2 live days, 8,294 inverse-beta-decay candidates; Δm²_31 to about 1%, sin²θ_12 to 2.1%, Δm²_21 to 1.1%; with long-baseline accelerator constraints, normal ordering at ≥ 2.1σ (one-sided), Bayes factor 10.18 | JUNO Collaboration 2026, arXiv:2609.37895 | [src: abstract] |
| KamLAND-Zen 800, complete data set | neutrinoless double beta decay of ¹³⁶Xe, 745 kg of enriched xenon, 2.1 ton yr | T_1/2 > 3.8 × 10²⁶ yr (90% CL); m_ββ < 28–122 meV | Abe et al. 2024, arXiv:2406.11438 | [src: abstract] |

Reading notes.

- The oscillation minimum sums move with the splittings by far less than the cosmological error; JUNO's 1% measurement of Δm²_31 changes nothing in the 0.059 and 0.10 eV floors at the precision at which cosmology uses them [der: √(2.5 × 10⁻³ eV²) ≈ 0.050 eV, and a 1% change in Δm² moves it by 0.5%].
- The ordering evidence from the laboratory is now of the same size as the one cosmology claims: a JUNO-based Bayes factor of 10.18 [src] against the DESI DR2 + CMB + NuFIT factor of 10 (`results.md` §1.6). They are independent in data and can be multiplied only if the cosmological model assumption (ΛCDM) is accepted.
- KATRIN quotes 90% CL, cosmology 95%. KATRIN's target sensitivity, below 0.3 eV on the effective electron-neutrino mass, corresponds to Σm_ν of roughly 0.9 eV for nearly degenerate masses [der: three times the per-state mass], more than ten times the cosmological limit. A laboratory confirmation of a cosmological Σm_ν near 0.06 eV is therefore not within reach of the running experiment.
- The double-beta-decay limit applies only if neutrinos are Majorana particles, and its mass range reflects nuclear matrix elements. ACT states that KamLAND-Zen excludes almost all of the inverted-ordering band and gives 18 meV as the lowest inverted-ordering m_ββ, the target for next-generation searches (arXiv:2503.14454 §6.1.1 [src]).
- No KATRIN mass result later than the 259-day analysis, and no published LEGEND-200 limit, was read this session (see "Not verified").

### 3.2 CMB and large-scale structure inputs (described in sibling skills)
<!-- key: cmb-and-large-scale-structure-inputs-described -->

| Input | Release used in the neutrino and light-relic constraints | Note for this domain | Citation | Flag |
|---|---|---|---|---|
| Planck | PR3 low-ℓ (SimAll, Commander) + PR4 CamSpec high-ℓ is the DESI baseline; PR4 LoLLiPoP–HiLLiPoP and PR3 plik are the alternatives | the choice moves the DR2 limit between 0.0642, 0.0774 and 0.0691 eV | arXiv:2503.14744 Table 2 | [src] |
| CMB lensing | Planck PR4 + ACT DR6 reconstructions in the DESI baseline; SPT-3G D1 quadratic-estimator reconstruction since 2026 | carries the amplitude information | arXiv:2503.14744; Omori et al. 2026, arXiv:2608.31136 | [src] |
| ACT DR6 | spectra + extended-model paper | N_eff, interacting dark radiation, neutrino self-interaction, axion-like fraction | Calabrese et al. 2025, arXiv:2503.14454 | [src] |
| SPT-3G D1 | 2019–2020 observations of the Main field | N_eff alone and in CMB-SPA | Camphuis et al. 2025, arXiv:2506.20707 | [src] |
| DESI DR1 | BAO (2024) and full shape | Σm_ν < 0.072 eV with CMB; the full shape enters the DR2 neutrino paper because no DR2 full shape exists | arXiv:2404.03002, arXiv:2503.14744 | [src] |
| DESI DR2 | BAO (March 2025) | current collaboration limits | arXiv:2503.14738, arXiv:2503.14744 | [src] |
| Supernovae | Pantheon+, Union3, DESY5 in the DESI paper; DES-Dovekie in later work | select the dark-energy model, and through it the neutrino limit | arXiv:2503.14744; Kıbrıs et al. 2026, arXiv:2605.21456 | [src] |
| DESI DR1 Lyα P1D | compressed linear-power amplitude and slope at z = 3 | does not significantly tighten Σm_ν; N_eff = 3.02 ± 0.10 with CMB + BAO | Chaves-Montero et al. 2026, arXiv:2601.21432 | [src: abstract] |

ACT and SPT are calibrated on Planck and take τ from Planck low-ℓ polarisation, so their neutrino limits are not independent of Planck in amplitude [sec: `cosmo-cmb`]. DESI completed its planned survey in April 2026, and results from the full data set are expected in 2027 [sec: `cosmo-galaxy-clustering`].

### 3.3 Primordial abundances
<!-- key: primordial-abundances -->

| Data | Content | Citation | Flag |
|---|---|---|---|
| Primordial deuterium | seven quasar absorption systems, (D/H)_P = (2.527 ± 0.030) × 10⁻⁵ | Cooke, Pettini & Steidel 2017, arXiv:1710.11129 | [src: abstract] |
| LBT Y_p Project | new primordial helium determination, Y_p = 0.2458 ± 0.0013 | Yeh et al. 2026, arXiv:2601.22239 | [src: abstract] |
| Rate compilations and codes | PRIMAT (weak-rate corrections); PRyMordial (rates marginalised) | Pitrou et al. 2018, arXiv:1801.08023; Schöneberg 2024, arXiv:2401.15054 | [src] |

### 3.4 Lyman-α forest samples used for dark-matter limits
<!-- key: lyman-alpha-forest-samples-used-for-dark-matter -->

The instruments, resolutions and reduction are described in `cosmo-lyman-alpha`. Only high-resolution spectra at z ≳ 4 reach the wavenumbers where a keV-scale cutoff appears.

| Sample | Redshift, scales | Used for | Citation | Flag |
|---|---|---|---|---|
| Keck/HIRES + Magellan/MIKE | 25 quasars at z > 4 | m_WDM > 3.3 keV; reanalysed with wider thermal histories | Viel et al. 2013, arXiv:1306.2314; Garzilli, Boyarsky & Ruchayskiy 2015, arXiv:1510.07006 | [src] |
| XQ-100 (X-shooter) + HIRES/MIKE | intermediate and small scales | m_WDM > 5.3 keV; fuzzy dark matter > 20–37.5 × 10⁻²² eV | Iršič et al. 2017, arXiv:1702.01764, arXiv:1703.04683 | [src] |
| Boera et al. 2019 spectra | 4.0 ≲ z ≲ 5.2 | m_WDM > 3.1 keV with the 1080-simulation Cholla grid | Villasenor et al. 2022, arXiv:2209.14220 | [src: abstract] |
| HIRES + UVES | z = 4.2–5.0, k_max = 0.2 s/km | m_WDM > 5.7 keV | Iršič et al. 2023, arXiv:2309.04533 | [src: abstract] |
| High-resolution P1D at z = 4.2, 4.6, 5.0 | — | pure and mixed fuzzy dark matter; dark matter–neutrino scattering | Liu, Gong & Zhou 2026, arXiv:2606.06969; Mosbech et al. 2026, arXiv:2607.15020 | [src] |
| SDSS DR14 + XQ-100 | z < 4.5 | m_WDM > 5.3 keV; Σm_ν with Planck | arXiv:1911.09073 | [src: abstract] |

No DESI Collaboration warm- or fuzzy-dark-matter limit from the DR1 or DR2 P1D was found (see `results.md`, "Not verified").

### 3.5 Milky Way and Local Group
<!-- key: milky-way-and-local-group -->

| Sample | Content | Used for | Citation | Flag |
|---|---|---|---|---|
| DES + Pan-STARRS1 satellite census | Milky Way satellite luminosity function with survey selection functions | m_WDM > 6.5 keV; fuzzy dark matter > 2.9 × 10⁻²¹ eV; dark matter–proton scattering | Nadler et al. 2020, arXiv:2008.00022 | [src: abstract] |
| Milky Way satellite population, earlier analysis | — | first dark matter–baryon scattering limits from satellites | Nadler et al. 2019, arXiv:1904.10000 | [src] |
| DES + PS1 + PAndAS | Milky Way and M31 satellites together | m_WDM > 6.20 keV; fuzzy dark matter > 1.74 × 10⁻²⁰ eV | Liu, Gong & Liao 2025, arXiv:2512.01361 | [src: abstract] |
| GD-1 and Pal 5 stellar streams | density variations along two cold streams | m_WDM > 3.6 keV alone, 6.2 keV with satellite counts | Banik et al. 2019, arXiv:1911.02663 | [src: abstract] |
| Segue 1 and Segue 2 | sizes and stellar velocity dispersions of two ultra-faint dwarfs | fuzzy dark matter > 3 × 10⁻¹⁹ eV | Dalal & Kravtsov 2022, arXiv:2203.05750 | [src] |
| Leo II | stellar kinematics | fuzzy dark matter > 2.2 × 10⁻²¹ eV | Zimmermann et al. 2024, arXiv:2405.20374 | [src] |

### 3.6 Strong lensing
<!-- key: strong-lensing -->

| Sample | Content | Used for | Citation | Flag |
|---|---|---|---|---|
| 8 quadruply imaged quasars | flux ratios | m_WDM > 5.2 keV | Gilman et al. 2019, arXiv:1908.06983 | [src] |
| JWST Lensed Quasar Dark Matter Survey | 31 lensed quasars, MIRI flux ratios | m_WDM > 5.6 or 6.4 keV | Keeley et al. 2025, arXiv:2511.07765 | [src: abstract] |
| Same survey, 28 quads | flux ratios + extended lensed arcs | m_WDM > 6.5 or 7.4 keV; free-streaming length < 7.0 or 6.0 kpc | Gilman et al. 2025, arXiv:2511.07513; Gilman et al. 2026, arXiv:2606.05277 | [src] |
| One VLBI lensed radio jet | arc resolved at < 5 mas | fuzzy dark matter ≤ 4.4 × 10⁻²¹ eV excluded | Powell et al. 2023, arXiv:2302.10941 | [src] |
| Extended-source lenses | joint with Lyα and satellites | m_WDM > 6.048 keV | Enzi et al. 2020, arXiv:2010.13802 | [src: abstract] |

### 3.7 High-redshift galaxies
<!-- key: high-redshift-galaxies -->

| Sample | Used for | Citation | Flag |
|---|---|---|---|
| JWST ultraviolet luminosity functions, z = 9–14.5, with HST at z = 4–8 | m_WDM ≥ 3.2 keV | Liu, Shan & Zhang 2024, arXiv:2404.13596 | [src: abstract] |
| HST ultraviolet luminosity functions, z ≈ 4–10, blank and lensed fields | dark matter–proton scattering with σ ∝ vⁿ | Lazare et al. 2025, arXiv:2510.10757 | [src] |

### 3.8 Clusters, groups and galaxies (self-interaction)
<!-- key: clusters-groups-and-galaxies-self-interaction -->

| Sample | Method | Citation | Flag |
|---|---|---|---|
| Bullet Cluster | offset between galaxies and lensing mass; mass-to-light ratio | Randall et al. 2007, arXiv:0704.0261; critique Robertson, Massey & Eke 2016, arXiv:1605.04307 | [src] |
| 72 cluster collisions | ensemble dark matter–star offset, 5.8 ± 8.2 kpc | Harvey et al. 2015, arXiv:1503.07675 | [src: abstract] |
| Relaxed groups and clusters | Jeans analysis of central profiles | Sagunski et al. 2020, arXiv:2006.12515 | [src] |
| 8 clusters | strong-lensing central densities, mean relative velocity 1458 km/s | Andrade et al. 2020, arXiv:2012.06611 | [src: abstract] |
| SPARC rotation curves | isothermal Jeans model with core collapse | Jia et al. 2026, arXiv:2601.17118 | [src] |

### 3.9 X-ray line searches (sterile-neutrino decay)
<!-- key: x-ray-line-searches-sterile-neutrino-decay -->

| Sample | Result | Citation | Flag |
|---|---|---|---|
| Stack of 73 galaxy clusters | unidentified line at 3.55–3.57 keV | Bulbul et al. 2014, arXiv:1402.2301 | [src: abstract] |
| More than 30 Ms of XMM-Newton blank-sky exposure | no line; the limit is disputed by two technical comments | Dessert, Rodd & Safdi 2018, arXiv:1812.06976; arXiv:2004.06170; arXiv:2004.06601 | [src] |

## 4. Simulation suites behind the limits
<!-- key: simulation-suites-behind-the-limits -->

| Suite | Size and content | Used in | Flag |
|---|---|---|---|
| Cholla thermal-history × warm-dark-matter grid | 1080 hydrodynamical simulations | arXiv:2209.14220 | [src: abstract] |
| Emulator of hydrodynamical simulations for ultralight axions | emulator over axion mass and intergalactic-medium parameters | Rogers & Peiris 2020, arXiv:2007.12705 | [src] |
| Neural-network P1D emulator for pure and mixed fuzzy dark matter | z = 4.2, 4.6, 5.0 | arXiv:2606.06969 | [src: abstract] |
| Dedicated hydrodynamical simulations with dark matter–neutrino scattering | replaces the half-mode mapping | arXiv:2607.15020 | [src] |
| Semi-analytic and N-body subhalo populations | two alternative subhalo-abundance priors (Galacticus, N-body) in the JWST lensing analyses | arXiv:2511.07765, arXiv:2511.07513 | [src] |
| ETHOS | mapping from dark-sector parameters to linear power and self-interaction | Cyr-Racine et al. 2015, arXiv:1512.05344 | [src] |

The general simulation landscape is in `cosmo-simulations-mocks`; the Lyα emulators (LaCE, PRIYA, Sherwood-Relics) are in `cosmo-lyman-alpha`.

## 5. What comes next
<!-- key: what-comes-next -->

| Facility or data set | What it adds for this domain | Status and date | Source | Flag |
|---|---|---|---|---|
| DESI full survey | BAO with the complete data; the first DR2-or-later full shape | planned survey completed April 2026; results expected in 2027 | `cosmo-galaxy-clustering` | [sec] |
| Simons Observatory, enhanced Large Aperture Telescope | lensing amplitude and damping tail: σ(Σm_ν) = 0.03 eV, or 0.015 eV with LiteBIRD; σ(N_eff) = 0.045 (**forecast**, statistical errors only) | full instrument expected to begin observations in 2028; survey ends 2034, 2.6 μK-arcmin over about 61% of the sky; no cosmology release yet [sec: `cosmo-cmb`] | SO Collaboration 2025, arXiv:2503.00636 §4 | [src] |
| SPT-3G full survey | more sky for the lensing and N_eff measurements | Main, Summer and Wide fields, about 10,000 deg² | `cosmo-cmb` | [sec] |
| LiteBIRD | cosmic-variance-limited low-ℓ EE, the direct measurement of τ | reformed to one telescope; launch in Japanese fiscal year 2036 | `cosmo-cmb` | [sec] |
| CMB-S4 | was the light-relic and neutrino-mass experiment of the 2030s | lost DOE and NSF support on 9 July 2025; shutting down | `cosmo-cmb` | [sec] |
| Euclid | 3×2pt and spectroscopic clustering: σ(Σm_ν) = 56 meV alone, 23 meV with Planck (at least 2.6σ evidence for non-zero mass); 4σ only with LiteBIRD and CMB Stage-IV; ΔN_eff < 0.144 (95%) with Planck, < 0.063 with future CMB; sensitivity to Σm_ν degrades by at most a factor of two in w0waCDM (**forecast**) | first cosmology release (DR1) planned for mid-2027 [sec: `cosmo-galaxy-clustering`] | Euclid Collaboration 2024, arXiv:2405.06047 | [src: abstract] |
| Rubin LSST | fainter and more complete Milky Way satellite census, more streams, more lensed quasars | survey began 30 June 2026 [sec: hub `field-state-2026.md`]; no dark-matter forecast was read here | — | [sec] |
| JWST Lensed Quasar Dark Matter Survey | the 31-lens flux-ratio sample and the 28-quad arc analysis are published | joint re-analysis with Milky Way satellites not found | arXiv:2511.07765, arXiv:2511.07513 | [src] |
| KATRIN complete data set; KATRIN++ | sensitivity below 0.3 eV; later an atomic-tritium source with quantum read-out | data set nearly complete at the January 2026 review | arXiv:2601.00248 | [src] |
| JUNO | mass ordering from reactor data alone with more exposure | 207 live days analysed | arXiv:2609.37895 | [src] |
| Next-generation double beta decay | m_ββ down to the 18 meV floor of the inverted ordering | proposed (nEXO) or running first phase (LEGEND-200); not researched | arXiv:2503.14454 for the target | [sec] |
| Reionisation-relic method for the forest | DESI-like Lyα data to m_WDM > 5.0 keV, 7.1 keV with SKA (**forecast**) | proposal paper, 2026 | `cosmo-lyman-alpha` | [sec] |

Two forecasts need a correction before they are quoted. The Euclid 4σ figure assumes CMB Stage-IV, which is cancelled; the figure that survives is 23 meV with Planck, or what a Simons Observatory combination would give, which that paper does not state. The DESI + Planck forecast of about 0.02 eV (Font-Ribera et al. 2013, arXiv:1308.4164, **forecast**) has nominally been met by the Bayesian error, but the errors that measure sensitivity are 0.043–0.053 eV (`results.md` §8.1). ACT gives 0.02–0.03 eV as the precision that future CMB and BAO data can reach (**forecast**, arXiv:2503.14454 §6.1.1 [src]).

With σ(Σm_ν) = 0.03 eV, the normal-ordering minimum of 0.059 eV is a 2σ signal, and with 0.015 eV a 4σ signal [der: 0.059/0.03 and 0.059/0.015]. In this forecast a detection of the minimum mass at 3σ or more therefore needs LiteBIRD, the instrument designed to measure τ from large-scale polarisation [sec: `cosmo-cmb`]; the neutrino-mass programme and the τ debate cannot be separated (`systematics.md` §2).

## 6. Timeline of the releases that moved these numbers
<!-- key: timeline-of-the-releases-that-moved-these -->

| Date | Event | Effect | Source |
|---|---|---|---|
| 2018 | Planck 2018 parameters | Σm_ν < 0.12 eV; N_eff = 2.99 ± 0.17 | arXiv:1807.06209 [src: abstract] |
| April–May 2024 | DESI DR1 BAO | Σm_ν < 0.072 eV; first "negative mass" analyses | arXiv:2404.03002, arXiv:2405.00836 [src] |
| June 2024 | KATRIN 259 days; KamLAND-Zen complete data | m_ν < 0.45 eV; m_ββ < 28–122 meV | arXiv:2406.13516, arXiv:2406.11438 [src] |
| October 2024 | NuFIT 6.0 | ordering undecided by oscillations alone | arXiv:2410.05380 [src] |
| March 2025 | DESI DR2 BAO; ACT DR6 | Σm_ν < 0.0642 eV; 3σ tension of the effective mass; N_eff = 2.86 ± 0.13 | arXiv:2503.14744, arXiv:2503.14454 [src] |
| June 2025 | SPT-3G D1 | N_eff = 2.82 ± 0.12 for CMB-SPA | arXiv:2506.20707 [src] |
| 9 July 2025 | CMB-S4 support withdrawn | the planned σ(N_eff) and σ(Σm_ν) programme ends | `cosmo-cmb` [sec] |
| November 2025 | JWST lensed-quasar papers III and IV | m_WDM > 5.6–7.4 keV | arXiv:2511.07765, arXiv:2511.07513 [src] |
| January 2026 | LBT Y_p Project; DESI DR1 P1D cosmology | N_ν = 2.925 ± 0.082; no gain on Σm_ν from the forest | arXiv:2601.22239, arXiv:2601.21432 [src] |
| April 2026 | DESI planned survey complete | — | `cosmo-galaxy-clustering` [sec] |
| August 2026 | SPT-3G D1 lensing | Σm_ν < 0.072 eV | arXiv:2608.31136 [src] |
| September 2026 | JUNO 207-day analysis | normal ordering at ≥ 2.1σ from the laboratory | arXiv:2609.37895 [src] |

The months are the arXiv submission months of the cited papers.

## Not verified
<!-- key: not-verified -->

- Sample sizes, survey areas and satellite counts of the DES + Pan-STARRS1 census were not read this session.
- No public-data location was read for any of the small-scale dark-matter samples.
- The KATRIN final data set, Project 8, LEGEND-200, CUORE and nEXO were not researched beyond what is quoted in §3.1; their numbers are not given.
- Rubin, Roman and Euclid forecasts for satellite counts, streams or lensed-quasar samples were not read.
- The Simons Observatory forecast assumptions (which large-scale-structure data enter the 0.03 eV figure) were read only in the paper's summary section.
