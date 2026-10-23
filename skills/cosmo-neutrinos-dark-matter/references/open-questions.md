# Open questions — neutrino mass, light relics and dark-matter properties from structure

Scope: the live controversies with both sides cited, tensions between analyses, method debates, what the next data decide, labelled forecasts, and the stale claims that still circulate.
Snapshot: 2026-10-07

Flags: `[src]` read in the cited paper this session; `[sec]` taken from a named secondary source; `[der]` derived here. Forecasts are labelled **forecast**. Numbers without a flag in this file are repeated from `results.md`, where they carry one.

## 1. Neutrino mass
<!-- key: neutrino-mass -->

### 1.1 Is cosmology in tension with the oscillation lower limit?
<!-- key: is-cosmology-in-tension-with-the-oscillation -->

**The claim.** In ΛCDM the data prefer less neutrino mass than oscillations allow. The DESI DR2 BAO + CMB limit is 0.0642 eV, just above the normal-ordering minimum of 0.059 eV; the Feldman–Cousins limit is 0.053 eV, below it; the effective signed mass is −0.101 (+0.047/−0.056) eV, 3σ from the minimum (Elbers et al. 2025, arXiv:2503.14744). Earlier: −160 ± 90 meV with the clustering-only extension on DR1 (Craig et al. 2024, arXiv:2405.00836), 2.8–3.3σ with the consistent extension (Elbers et al. 2024, arXiv:2407.10965), 2.5–5σ across metrics and data (Jiang et al. 2024, arXiv:2407.18047). The most probable value from ACT is also zero (Calabrese et al. 2025, arXiv:2503.14454 §6.1.1 [src]).

**The case that it is not a neutrino statement.**

- The signal is the BAO–CMB mismatch in H0 r_d, re-expressed. A negative effective mass, evolving dark energy and a higher τ each absorb it (arXiv:2503.14744 §5.2; arXiv:2407.10965). DESI itself reads negative values as unidentified systematics or new physics possibly unrelated to neutrinos.
- With two lensing amplitudes free the effective mass is −0.018 (+0.085/−0.089) eV (Cozzumbo et al. 2025, arXiv:2511.01967). [src: abstract]
- With τ near 0.09 the tension disappears (Sailer et al. 2025, arXiv:2504.16932; Jhaveri, Karwal & Hu 2025, arXiv:2504.21813); within DESI's own tests it falls to 1.7σ at τ = 0.074 (`systematics.md` §2).
- Profile-likelihood and Bayesian limits agree, and the limit sits at the edge of what the data can do: "living at the edge" (Naredo-Tuero et al. 2024, arXiv:2407.13831).
- Graham, Green & Meyers 2025 (arXiv:2508.20999) separate two things called negative mass: one describes the expansion history, the other enhanced lensing. They need not have a common origin.

**The case that it is robust.**

- The preference for negative values is present with plik, CamSpec and the PR4 LoLLiPoP–HiLLiPoP likelihoods, weaker with the last (arXiv:2503.14744 §5.2.1 [src]).
- ACT obtains the same limit with WMAP in place of Planck, so the Planck smoothing excess does not set it (arXiv:2503.14454 §6.1.1 [src]).
- Changing the neutrino abundance does not help: the limit moves by at most 0.004 eV, and a lower neutrino temperature makes the tension worse (Figueroa, Sobotka & Erickcek 2026, arXiv:2609.15970 [src]).
- Decaying dark matter relaxes the bound only if lensing and perturbation data are ignored (Montandon et al. 2026, arXiv:2603.03284).
- An external full-shape + bispectrum analysis tightens the limit to 0.049 eV (Ivanov et al. 2026, arXiv:2601.16165).

**Where it stands.** The tension is 3σ at most, in one model (ΛCDM), with one τ. It is the same anomaly as the w0wa preference seen from another parameter, not an independent one; `cosmo-dark-energy-modified-gravity` holds the dark-energy side. Nothing in the data requires a statement about neutrinos beyond "Σm_ν is small in ΛCDM".

### 1.2 Which explanation, if the mismatch is real?
<!-- key: which-explanation-if-the-mismatch-is-real -->

| Explanation | What it predicts | Status | Citation |
|---|---|---|---|
| Evolving dark energy | positive masses recovered: Σm_ν,eff = 0.06 (+0.15/−0.10) eV in w0waCDM; limit relaxes to 0.12–0.16 eV | depends on the supernova sample; see `cosmo-supernovae` | arXiv:2407.10965; arXiv:2503.14744 |
| Higher optical depth | τ ≈ 0.09; with a prior τ = 0.11 ± 0.006, Σm_ν = 0.10 (+0.04/−0.05) eV, a conditional 2σ detection | contradicts Planck low-ℓ EE at 3–5σ and reionisation data [sec: `cosmo-cmb`] | arXiv:2504.16932; Sullivan, de Belsunce & Ivanov 2026, arXiv:2606.30903 |
| Lensing excess | the preference vanishes once lensing amplitudes are free | no excess in the reconstructions, which match the primary-CMB prediction [sec: `cosmo-cmb`] | arXiv:2511.01967 |
| Sign-switching cosmological constant | Σm_ν,eff = 0.055 ± 0.050 eV against −0.075 (+0.039/−0.053) eV in ΛCDM for the same data; transition at z† > 2.4 | one model paper | Kıbrıs et al. 2026, arXiv:2605.21456 |
| New neutrino or dark-sector physics | decays, non-thermal distributions, interacting dark radiation | sterile neutrinos: only the fully thermalised case is strongly disfavoured (Ladeira et al. 2026, arXiv:2606.21518); abundance changes do not help | arXiv:2609.15970; arXiv:2503.14454 |

A fit of an alternative model to the same BAO + CMB data is not new evidence: every row above removes the same Δχ².

### 1.3 Can the neutrino mass be bounded independently of dark energy?
<!-- key: can-the-neutrino-mass-be-bounded-independently -->

Qu et al. 2026 (arXiv:2607.24742) obtain Σm_ν < 0.152 eV with (w0, wa) marginalised, stable under binned and cubic w(a), and Σm_ν < 0.41 eV from the primary CMB with A_lens marginalised plus the lensing reconstruction, without late-time distances. Ivanov et al. (arXiv:2601.16165) reach 0.077 eV in w0waCDM with clustering shape information. The DESI w0waCDM limits are 0.117–0.163 eV. The open point is whether shape and lensing information can restore a limit below the inverted-ordering minimum of 0.10 eV in a general expansion history; at present only the external EFT analysis claims it.

### 1.4 Is the mass ordering decided?
<!-- key: is-the-mass-ordering-decided -->

- **Cosmology says "moderately" to "decisively", depending on the prior.** K = 10 (DESI DR2 + CMB + NuFIT 6.0; 6 with L-H, 8 with plik), Δχ² = 4.6; 46.5 with more data and another prior (arXiv:2407.18047); above 460 in ΛCDM and above 40 in extensions (Jimenez et al. 2026, arXiv:2606.18987), with a stated factor of about 10 from the prior measure alone; 3.5σ (ΛCDM) or 2.4σ (w0waCDM) in the EFT reanalysis (arXiv:2601.16165); "∼98% confidence" from P-ACT-LB (arXiv:2503.14454 [src]).
- **Oscillations alone do not.** NuFIT 6.0 finds both orderings fit almost equally well; Δχ² = 6.1 for normal ordering only with the Super-Kamiokande atmospheric table (Esteban et al. 2024, arXiv:2410.05380).
- **JUNO has started to.** With 207.2 live days and accelerator constraints on Δm²_31, normal ordering is favoured at ≥ 2.1σ, Bayes factor 10.18 (JUNO Collaboration 2026, arXiv:2609.37895 [src: abstract]).
- **The caveats.** The cosmological preference exists only where the upper limit lies between 0.059 and 0.10 eV, which holds in ΛCDM and wCDM and fails in w0waCDM (limits 0.12–0.16 eV). ACT notes that it depends on the use of DESI BAO. A text may say that cosmology in ΛCDM and JUNO point the same way; it may not multiply the two Bayes factors without stating the model assumption.

### 1.5 Bayesian or frequentist?
<!-- key: bayesian-or-frequentist -->

The two agree on the limit (within 0.01 eV in DESI DR2, within about 10% in arXiv:2407.13831) and disagree on what to call the sensitivity (0.020 against 0.043 eV). The live question is presentational: whether collaboration papers should lead with a truncated-posterior limit. For decaying dark matter the two approaches disagree on the intervals themselves (Montandon et al. 2025, arXiv:2505.20193).

### 1.6 What will decide
<!-- key: what-will-decide -->

| Question | Deciding data | When | Flag |
|---|---|---|---|
| Is the BAO–CMB mismatch growing? | DESI full-survey BAO | 2027 | [sec: `cosmo-galaxy-clustering`] |
| Is τ ≈ 0.055? | ground-based large-scale polarisation; LiteBIRD | LiteBIRD not before Japanese fiscal year 2036 | [sec: `cosmo-cmb`] |
| Is there excess lensing? | SPT-3G full survey, Simons Observatory | SO full instrument from 2028, survey to 2034 | arXiv:2503.00636 [src] |
| Minimum mass at 2σ | SO + large-scale structure: σ(Σm_ν) = 0.03 eV (**forecast**, statistical only) | by 2034 | arXiv:2503.00636 [src] |
| Minimum mass at about 4σ | SO + LiteBIRD: σ = 0.015 eV (**forecast**) | after LiteBIRD | arXiv:2503.00636 [src] |
| Independent large-scale-structure measurement | Euclid: σ = 56 meV alone, 23 meV with Planck (**forecast**); degrades by up to a factor of two in w0waCDM | DR1 mid-2027 [sec: `cosmo-galaxy-clustering`] | Euclid Collaboration 2024, arXiv:2405.06047 [src] |
| Ordering | JUNO with more exposure | — | arXiv:2609.37895 |
| Absolute mass in the laboratory | KATRIN to below 0.3 eV, then KATRIN++ | not competitive with 0.06 eV | Drexlin & Weinheimer 2026, arXiv:2601.00248 [src] |
| Majorana mass | KamLAND-Zen at 28–122 meV; target 18 meV | next generation | Abe et al. 2024, arXiv:2406.11438; arXiv:2503.14454 [src] |

If KATRIN or a double-beta experiment measured a mass above the cosmological limit, the conflict would be with ΛCDM plus stable thermal neutrinos, not with cosmological data as such: the bounds assume long-lived neutrinos with a Fermi–Dirac distribution (arXiv:2503.14454 §6.1.1 [src]).

## 2. N_eff and light relics
<!-- key: neff-and-light-relics -->

- **Low or high?** CMB-only values lie below 3.044 (ACT 2.60 +0.21/−0.29, P-ACT 2.73 ± 0.14, CMB-SPA 2.82 ± 0.12), values with DESI BAO lie above (3.23 ± 0.18 with Planck, 3.53 ± 0.23 with SPT-3G D1) (arXiv:2503.14454; Camphuis et al. 2025, arXiv:2506.20707; arXiv:2503.14744). All CMB-only values are within 2σ of 3.044. The upward pull is the same BAO–CMB mismatch as in §1.
- **Is the ACT damping-tail preference real?** ACT prefers less damping than the Planck best fit; SPT-3G D1 alone gives 3.18 (+0.29/−0.33). Late photon heating cannot produce a low N_eff without violating FIRAS (`systematics.md` §9). SPT-3G wide fields and SO decide [sec: `cosmo-cmb`].
- **What BBN adds.** N_ν = 2.925 ± 0.082 from the LBT helium measurement with D/H and the CMB (Yeh et al. 2026, arXiv:2601.22239), also below 3 by about 1σ; light elements alone give ΔN_eff = −0.14 ± 0.21 with rates marginalised (Schöneberg 2024, arXiv:2401.15054). Whether the rate uncertainty or the helium systematics dominate the BBN side is not settled between those two treatments.
- **How much dark radiation is allowed?** ΔN_eff < 0.17 (P-ACT-LB, free-streaming) and N_idr < 0.134 (fluid), but < 0.58 if the primordial spectrum is not a pure power law (Garny, Niedermann & Sloth 2026, arXiv:2604.26541). ACT DR6 closes most of the room that stepped and interacting dark-radiation models used to raise H0 (Cvetko, Joseph & Marques-Tavares 2025, arXiv:2512.19633); the strongly self-interacting neutrino mode of Kreisch, Cyr-Racine & Doré 2019 (arXiv:1902.00534) finds no support in ACT DR6 + Planck.
- **Phase shift.** 2.6σ evidence for β_φ > 0 in DESI DR2 BAO, up from 1.6σ in DR1 (arXiv:2503.14744). It is the model-independent signature of free streaming (Bashinsky & Seljak 2003, arXiv:astro-ph/0310198), not yet a constraint on N_eff.
- **Forecasts.** σ(N_eff) = 0.045 for the enhanced SO LAT (**forecast**, arXiv:2503.00636 [src]); ΔN_eff < 0.144 (95%) for Euclid + Planck (**forecast**, arXiv:2405.06047 [src]). The thresholds they are measured against: the minimum contribution of one additional thermalised species is 0.027 for a scalar and 0.095 for a spin-3/2 fermion (arXiv:2503.14454 §6.1.1 [src]). The SO forecast does not reach the scalar threshold at 2σ [der: 2 × 0.045 = 0.09 > 0.027].

## 3. Warm dark matter
<!-- key: warm-dark-matter -->

### 3.1 How strong is the Lyα limit?
<!-- key: how-strong-is-the-lyalpha-limit -->

- **Strong side.** > 5.7 keV with thermal history and inhomogeneous reionisation marginalised (Iršič et al. 2023, arXiv:2309.04533); > 5.3 keV from earlier samples (Iršič et al. 2017, arXiv:1702.01764; Palanque-Delabrouille et al. 2019, arXiv:1911.09073).
- **Cautious side.** > 3.1 keV, with the likelihood peaking at 4.5 keV, from a 1080-simulation grid of heating histories (Villasenor et al. 2022, arXiv:2209.14220); > 1.9 keV if the coldest histories are allowed (Garzilli et al. 2019, arXiv:1912.09397); no limit at all in the 2015 reanalysis with unconstrained histories (Garzilli, Boyarsky & Ruchayskiy 2015, arXiv:1510.07006).
- **Reading.** The disagreement is about priors on the intergalactic medium, not about data. `cosmo-lyman-alpha` holds the thermal-state measurements that the strong side uses to narrow the prior.

### 3.2 Which number is "the" limit?
<!-- key: which-number-is-the-limit -->

Each probe now reports 6–7 keV: satellites 6.5 keV (Nadler et al. 2020, arXiv:2008.00022), lensing 5.6–7.4 keV depending on data and subhalo prior (Keeley et al. 2025, arXiv:2511.07765; Gilman et al. 2025, arXiv:2511.07513), Lyα 5.7 keV. The often-quoted 9.7 keV (Nadler et al. 2021, arXiv:2101.07810) is a 2021 combination that predates the JWST sample. Satellites, streams and lensing share the subhalo mass function and its tidal evolution (`systematics.md` §16); the N-body and semi-analytic predictions for the inner subhalo abundance differ by about 50% (arXiv:2511.07513 §4.3 [src]). A defensible summary is "thermal relics below about 5–6 keV are excluded by three probes with partly shared theory, and below about 2 keV even for the coldest thermal histories considered in the 2019 analysis".

### 3.3 Is warm dark matter still motivated?
<!-- key: is-warm-dark-matter-still-motivated -->

The original motivation was the small-scale "crisis" of cold dark matter (Bode, Ostriker & Turok 2000, arXiv:astro-ph/0010389; Viel et al. 2013, arXiv:1306.2314, whose title states it). This session did not research whether masses above 6 keV still affect any of the small-scale puzzles; that belongs to `cosmo-simulations-mocks` and is listed under "Not verified".

### 3.4 Sterile neutrinos and the 3.5 keV line
<!-- key: sterile-neutrinos-and-the-3-5-kev-line -->

The line was reported in a stack of 73 clusters (Bulbul et al. 2014, arXiv:1402.2301); a blank-sky analysis claimed to exclude the decaying-dark-matter origin (Dessert, Rodd & Safdi 2018, arXiv:1812.06976); two comments argue the limit is weaker by a factor of 20 or more (Abazajian 2020, arXiv:2004.06170; Boyarsky et al. 2020, arXiv:2004.06601), and the original authors maintained their result. Structure formation excludes the 7.1 keV candidate only for some lepton asymmetries (Enzi et al. 2020, arXiv:2010.13802). KATRIN will search for keV sterile neutrinos in the laboratory after its mass programme (arXiv:2601.00248 [src]). The status of the line in recent X-ray microcalorimeter data was not researched.

## 4. Fuzzy and ultralight dark matter
<!-- key: fuzzy-and-ultralight-dark-matter -->

- **An order of magnitude between Lyα analyses.** > 2 × 10⁻²⁰ eV (Rogers & Peiris 2020, arXiv:2007.12705), > 2–3.75 × 10⁻²¹ eV (Iršič et al. 2017, arXiv:1703.04683), > 1.9 × 10⁻²¹ eV (Liu, Gong & Zhou 2026, arXiv:2606.06969). The most recent is the weakest.
- **Dwarf heating against everything else.** > 3 × 10⁻¹⁹ eV from the sizes and dispersions of Segue 1 and 2 (Dalal & Kravtsov 2022, arXiv:2203.05750) is one to two orders of magnitude above the other limits; the cosmology-independent Leo II limit is 2.2 × 10⁻²¹ eV (Zimmermann et al. 2024, arXiv:2405.20374). Whether the granule-heating argument holds for realistic dwarf histories is the open point.
- **Does the canonical window survive?** The 10⁻²² eV mass at which fuzzy dark matter was proposed to matter for galaxies (Hui et al. 2016, arXiv:1610.08297) is excluded as all of the dark matter by every limit above. A sub-component is allowed: f < 0.07, 0.12, 0.65 at 10⁻²³, 10⁻²², 10⁻²¹ eV (arXiv:2606.06969).
- **Production dependence.** If the field has a subhorizon spectrum peaked at k*, it free-streams like warm dark matter and the limit becomes m > 6 × 10⁻¹⁸ eV (k*/10⁴ Mpc⁻¹) (Nadler et al. 2026, arXiv:2605.15371): the fuzzy limits above are limits on one production scenario.
- **Hints at lower mass.** 2.7σ in BOSS at 10⁻²⁶ eV (Rogers et al. 2023, arXiv:2301.08361), a mild DESI preference that vanishes with the CMB (Verdiani et al. 2026, arXiv:2607.11876), 2.1σ in ACT lensing at 10⁻²⁴·⁵ eV (Laguë et al. 2026, arXiv:2606.06410). None is confirmed by a second data set; limits are below 1% of the dark matter at 10⁻³⁰–10⁻²⁸ eV and reach 0.3% of the matter density at 10⁻²⁹ eV. The original CMB + clustering limits are in Hložek et al. 2014 (arXiv:1410.2896).

## 5. Self-interacting dark matter
<!-- key: self-interacting-dark-matter -->

- **Constant cross section.** The value of order 1 cm²/g proposed for dwarf cores (Spergel & Steinhardt 1999, arXiv:astro-ph/9909386) is excluded on cluster scales: < 0.47 cm²/g from 72 mergers (Harvey et al. 2015, arXiv:1503.07675), < 0.35 cm²/g from relaxed clusters (Sagunski et al. 2020, arXiv:2006.12515), < 0.13 cm²/g from cluster strong lensing (Andrade et al. 2020, arXiv:2012.06611).
- **Velocity dependence.** About 2 cm²/g on galaxy scales falling to 0.1 cm²/g in clusters fits dwarfs to clusters (Kaplinghat, Tulin & Yu 2015, arXiv:1508.03339); groups give 0.5 ± 0.2 cm²/g (arXiv:2006.12515). This is a consistent picture, not a detection: the galaxy-scale value rests on Jeans modelling with baryons.
- **Core collapse.** With gravothermal collapse included, rotation curves admit a second solution near 100 cm²/g with a velocity scale of about 60 km/s (Jia et al. 2026, arXiv:2601.17118). Whether dense dwarfs and lensing perturbers are core-collapsed haloes is the active question of the field; reviews: Tulin & Yu 2017 (arXiv:1705.02358), Adhikari et al. 2022 (arXiv:2207.10638).
- **The Bullet Cluster number.** σ/m < 1.25 cm²/g is a 68% limit (Randall et al. 2007, arXiv:0704.0261), and resimulation shows the offset method was overinterpreted (Robertson, Massey & Eke 2016, arXiv:1605.04307).

## 6. Interacting and decaying dark matter
<!-- key: interacting-and-decaying-dark-matter -->

- **Dark matter–neutrino scattering.** Earlier hints of a non-zero interaction are stated to be excluded by dedicated Lyα simulations, u_νχ ≤ 1.5 × 10⁻⁸ (Mosbech et al. 2026, arXiv:2607.15020).
- **Dark matter–baryon scattering.** CMB limits (Gluscevic & Boddy 2017, arXiv:1712.07133) are superseded on small scales by satellites (Nadler et al. 2019, arXiv:1904.10000; arXiv:2008.00022) and complemented by luminosity functions for velocity-dependent models (Lazare et al. 2025, arXiv:2510.10757).
- **Dark matter–dark radiation.** The ETHOS-4 benchmark (framework: Cyr-Racine et al. 2015, arXiv:1512.05344) is excluded by the joint lensing + Lyα + satellite analysis (arXiv:2010.13802).
- **Decays and S8.** Decay to dark radiation is limited to a few percent of the dark matter (Poulin, Serpico & Lesgourgues 2016, arXiv:1606.02073; Simon et al. 2022, arXiv:2203.07440). The two-body decay proposed to lower S8 is preferred only with an S8 prior, and its intervals depend on the statistical method (arXiv:2505.20193). Whether an S8 tension remains to be explained is a question for `cosmo-weak-lensing`.

## 7. Method debates
<!-- key: method-debates -->

- **Limits or effective parameters.** Whether to publish a signed effective mass at all, given that three inequivalent definitions exist (`physics-and-methods.md` §1.4).
- **Priors on masses.** Linear in Σm_ν, linear in the lightest mass, or logarithmic: the ordering Bayes factor changes by a factor of about 10 (arXiv:2606.18987).
- **Thermal-relic language.** Whether small-scale limits should be published as M_hm or as a transfer-function parameterisation, and only then translated (arXiv:2607.15020 shows the translation fail for one model).
- **Subhalo abundance.** Semi-analytic or N-body priors for lensing (arXiv:2511.07513), and how many LMC-analogue hosts a satellite analysis needs (arXiv:2008.00022).
- **Collaboration or external.** External reanalyses of public DESI data now quote the tightest neutrino numbers (arXiv:2601.16165); they use different priors and extra statistics and are not interchangeable with the collaboration values.

## 8. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

| Claim still seen | Correction | Source |
|---|---|---|
| "Cosmology gives Σm_ν < 0.12 eV" | Planck 2018 + BAO; superseded by 0.064–0.089 eV with DESI, in ΛCDM | arXiv:1807.06209; arXiv:2503.14744 |
| "DESI finds Σm_ν < 0.064 eV" with no model | 0.163 eV in w0waCDM with the same data; 0.117–0.139 eV with supernovae | arXiv:2503.14744 |
| "ACT DR6 gives Σm_ν < 0.082 eV" | the abstract value; the revised text gives < 0.089 eV | arXiv:2503.14454 §6.1.1 [src] |
| "DESI measures σ(Σm_ν) = 0.02 eV" | a truncated-posterior width; the sensitivity is 0.043–0.053 eV | arXiv:2503.14744 |
| "Cosmology has measured a negative neutrino mass" | an effective parameter with three definitions; 3σ at most, absent in w0waCDM or with free lensing amplitudes | arXiv:2407.10965; arXiv:2511.01967 |
| "The limit comes from the suppression of structure growth" | in current data the geometric channel is at least as constraining | Loverde & Weiner 2024, arXiv:2410.00090 |
| "BAO constrain the neutrino mass" | BAO alone do not; they constrain Ω_m | arXiv:2503.14744 §3.1 |
| "The Lyα forest tightens the neutrino limit" | DESI DR1 P1D does not significantly tighten it | Chaves-Montero et al. 2026, arXiv:2601.21432 |
| "Cosmology has established the normal ordering" | K from 10 to above 460 with the prior; valid in ΛCDM only | arXiv:2606.18987; arXiv:2503.14744 |
| "Oscillation data alone establish the normal ordering" | NuFIT 6.0: almost equal without the Super-Kamiokande table; JUNO-based ≥ 2.1σ | arXiv:2410.05380; arXiv:2609.37895 |
| A KATRIN limit quoted at 95%, or read as a limit on Σm_ν | < 0.45 eV at 90% CL (259 days) on the effective electron-neutrino mass; Σm_ν ≲ 1.3 eV follows only for nearly degenerate masses | Aker et al. 2024, arXiv:2406.13516 |
| "N_eff = 3.046 in the Standard Model" | 3.044 | Froustey, Pitrou & Volpe 2020, arXiv:2008.01074; Bennett et al. 2019, arXiv:1911.04504 |
| "CMB-S4 will measure N_eff and detect the neutrino mass in the 2030s" | CMB-S4 lost its agency support in July 2025; SO forecasts 0.045 and 0.03 eV | [sec: `cosmo-cmb`]; arXiv:2503.00636 |
| "Euclid will detect the neutrino mass at 4σ" | only with LiteBIRD and CMB Stage-IV; 2.6σ with Planck (**forecast**) | arXiv:2405.06047 |
| "DESI + Planck reach 0.02 eV as forecast" | forecast of Font-Ribera et al. 2013; met only by the truncated error | arXiv:1308.4164 |
| "Lyα gives m_WDM > 5.3 keV" without conditions | 1.9–5.7 keV with the thermal-history prior and k_max | arXiv:1912.09397; arXiv:2309.04533 |
| "Warm dark matter lighter than 9.7 keV is excluded" | a 2021 combination; individual current probes give 5.6–7.4 keV | arXiv:2101.07810; arXiv:2511.07513 |
| "A 6 keV thermal-relic limit excludes a 6 keV sterile neutrino" | the mapping depends on production; the same data gave 0.55 and 2.0 keV | Viel et al. 2005, arXiv:astro-ph/0501562 |
| "Fuzzy dark matter of 10⁻²² eV solves small-scale problems" | excluded as all of the dark matter by Lyα, satellites, streams, lensing and dwarfs | arXiv:2007.12705; arXiv:2008.00022; Banik et al. 2019, arXiv:1911.02663; Powell et al. 2023, arXiv:2302.10941 |
| "The Bullet Cluster requires σ/m < 1 cm²/g" quoted as a 95% limit | 1.25 cm²/g at 68%; method criticised | arXiv:0704.0261; arXiv:1605.04307 |
| "Self-interacting neutrinos solve the Hubble tension" | no evidence in ACT DR6 + Planck | arXiv:2503.14454 |
| "The 3.5 keV line is excluded" or "is dark matter" | both contested; the exclusion depends on background modelling | arXiv:1812.06976; arXiv:2004.06601 |
| "Joint lensing + satellite limit" quoted as current | not redone with the JWST lenses | Gilman et al. 2019, arXiv:1908.06983; Gilman et al. 2026, arXiv:2606.05277 |

Supporting references for rows above: the standard review of neutrino cosmology is Lesgourgues & Pastor 2006 (arXiv:astro-ph/0603494); the suppression argument goes back to Hu, Eisenstein & Tegmark 1997 (arXiv:astro-ph/9712057); the Boltzmann treatment of non-cold relics is Lesgourgues & Tram 2011 (arXiv:1104.2935). The mirror statement on the dark-energy side is in the DESI DR2 BAO paper (arXiv:2503.14738) and, for DR1, arXiv:2404.03002. SPT-3G D1 lensing gives the same limit as DESI DR1 did, 0.072 eV (Omori et al. 2026, arXiv:2608.31136). Primordial deuterium: Cooke, Pettini & Steidel 2017 (arXiv:1710.11129); helium prediction: Pitrou et al. 2018 (arXiv:1801.08023); epoch comparison: Yeh et al. 2022 (arXiv:2207.13133). Stream + Milky Way + M31 satellite limits: Liu, Gong & Liao 2025 (arXiv:2512.01361); ultraviolet luminosity function limit: Liu, Shan & Zhang 2024 (arXiv:2404.13596).

## 9. Not verified
<!-- key: not-verified -->

- Whether a KATRIN result from the complete data set, or a published LEGEND-200 limit, exists at the snapshot.
- The 2.7σ positive Σm_ν in w0waCDM reported in the hub file from a joint DESI + CMB + DES analysis was not read here.
- Whether thermal relics above 6 keV still alter any small-scale structure observable.
- The status of the 3.5 keV line in microcalorimeter data.
- Forecasts for Rubin satellite counts, stream samples and lensed-quasar samples.
- DESI-II, Spec-S5, PFS and 4MOST forecasts for Σm_ν.
- Project 8 and next-generation double-beta sensitivities.
- No date-sorted search for N_eff, fuzzy dark matter or self-interacting dark matter was repeated on resume; the first pass covered them to mid-2026.
