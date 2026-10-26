# Direct detection of the relic neutrino background — cosmo-neutrinos-dark-matter dossier

Scope: how a direct search for the cosmic neutrino background (CνB) is
set up and analysed: the capture signal on tritium and its rate (Dirac
or Majorana, clustering), the energy-resolution requirement, how the
existing KATRIN overdensity limit was fitted, how a PTOLEMY-type
sensitivity is forecast, which quantum and molecular effects limit
tritium targets, and what the local clustering factor is; the reference
files hold no entry on this subtopic.
Snapshot: 2026-10-19.
From: Di Valentino, Gariazzo & Mena 2024 review (arXiv:2404.19322),
Sect. V.

Already in L2, not repeated here: the indirect evidence for the
background through N_eff and the free-streaming phase shift
(`results.md#measurements-lambdacdm-neff-68-unless-stated`,
`results.md#bao-phase-shift`); the KATRIN neutrino-mass result and its
status (`results.md#laboratory-anchors`,
`surveys-and-data.md#laboratory-neutrino-experiments`). The review
states the motivation: N_eff close to its standard value is "rather
clear indirect evidence" but cannot show that the radiation is
standard-model neutrinos; only a direct detection "would demonstrate
the presence of neutrinos with the expected momentum distribution and
temperature" [src: arXiv:2404.19322 Sect. V].

## How it is done
<!-- key: how-it-is-done -->

Notation: n₀ the number density per degree of freedom (one helicity
state of one mass eigenstate, neutrino or antineutrino) in the absence
of clustering; η (KATRIN) or f_c (theory papers) the local overdensity
n_local/n₀; m_ν the neutrino mass, taken degenerate unless stated;
m_lightest the lightest mass; E₀ or K_end the β-decay endpoint; Δ the
detector energy resolution (full width at half maximum); N_T the number
of tritium nuclei; U_ej the electron-row elements of the mixing matrix;
σ̄ the capture cross section times velocity, averaged.

### Step 1. Signal: neutrino capture on a β emitter
<!-- key: step-1-signal-neutrino-capture-on-a-beta-emitter -->

- **Process and signature.** ν_j + ³H → ³He + e⁻ has no threshold, so
  it works for relic energies; the electron is emitted at
  K_e ≈ K_end + 2m_ν (Eq. 37), a line above the β endpoint
  (Long, Lunardini & Sabancilar 2014, arXiv:1405.7654 Sect. 2.3 [src]).
  The endpoint must include nuclear recoil: neglecting it shifts the
  endpoint by more than the neutrino mass (≈ −0.7 keV for the free
  neutron) [src: footnote 6]. Tritium was chosen in earlier work for
  its rate and low contamination of the signal region (arXiv:2404.19322
  Sect. V.1 [src]).
- **Cross section.** For non-relativistic neutrinos the capture cross
  section times velocity, σ_j v_j ∝ G_F² |V_ud|² |U_ej|² F(Z, E_e) E_e p_e
  (f² + 3g²) (Eq. 44), is the same for both helicities, because the
  helicity factor A(±1/2) → 1; differences between Dirac and Majorana
  come only from how many states are populated (arXiv:1405.7654 Sect.
  2.3 [src]).
- **Rate.** Γ = Σ_j |U_ej|² σ̄ [n_j(ν_hR) + n_j(ν_hL)] N_T (Eq. 53).
  Dirac: Γ^D = σ̄ n₀ N_T (Eq. 54); Majorana: Γ^M = 2σ̄ n₀ N_T (Eq. 55),
  because relic Dirac neutrinos are all left-helical while Majorana
  neutrinos populate both helicities; n₀ ≈ 56 cm⁻³ (Eq. 9) [src: arXiv:1405.7654]. For
  100 g of tritium, Γ^M ≈ 8.12 yr⁻¹ and Γ^D ≈ 4.06 yr⁻¹ (Eq. 57),
  independent of the mass while the neutrinos are non-relativistic
  [src: Sect. 3]. With clustering, helicities mix in bound orbits, but
  the Majorana rate stays twice the Dirac one [src: Sect. 4.2].
- **Per-nucleus rate used by KATRIN.** R_cap = 4.2 × 10⁻²⁵ yr⁻¹ per
  tritium nucleus for Majorana neutrinos, halved for Dirac; KATRIN
  quotes its results for Majorana neutrinos (Aker et al. 2022,
  arXiv:2202.04587 [src: Sect. "Keywords:"]).

### Step 2. Background and resolution
<!-- key: step-2-background-and-resolution -->

- **Background.** The β spectrum (arXiv:1405.7654 Eq. 59) smeared by the
  resolution leaks above the endpoint. Two Gaussian features are
  separable if their separation exceeds the FWHM, Δ = √(8 ln 2) σ ≈
  2.35σ (Eq. 58); since the separation is 2m_ν, the signal exceeds the
  β background for Majorana neutrinos when Δ ≲ 0.7 m_ν [src: Sect. 3,
  Fig. 3, abstract].
- **What that means.** With Δ = 0.15 eV a PTOLEMY-like experiment is
  sensitive only to quasi-degenerate masses, m_ν ≳ 0.1 eV, and sees the
  three peaks as one [src: abstract, Sect. 3]. For m_lightest = 50 meV
  in the normal ordering the capture feature sits within a few tens of
  meV of the β spectrum, so the resolution "needs to be as good as
  20 meV" (Cheipesh, Cheianov & Boyarsky 2021, arXiv:2101.10069 [src]).

### Step 3. Fit a spectrum: the KATRIN overdensity search
<!-- key: step-3-fit-a-spectrum-the-katrin-overdensity -->

KATRIN used its 2019 neutrino-mass data (KNM1 and KNM2) [src:
arXiv:2202.04587]:

1. **Data.** Integral spectra measured with a MAC-E filter, resolution
   ΔE = 2.8 eV at E₀ = 18.57 keV, 117 pixels merged; KNM1 analysed from
   E₀ − 37 eV to E₀ + 49 eV (274 scans, 521.7 h), KNM2 from E₀ − 40 eV to E₀ + 135 eV (361 scans, 743.7 h) [src: arXiv:2202.04587, Sect. "First measurement campaign (KNM1)" and the KNM2 paragraph after it; abstract for 18.57 keV].
2. **Model.** R_calc(qU) = ∫ R_diff(E) f(E − qU) dE + R_bg (Eq. 1),
   f the response function, R_diff = R_β + R_CνB (Eq. 2), R_β with the
   molecular final-state distribution (Eq. 3). The capture term is a
   Gaussian at E₀ + 2m_ν − ⟨E_GS⟩ with amplitude η N_T ε_FSD R_cap T
   (Eq. 4), ε_FSD the ground-state fraction: the 43% of captures that
   leave ³HeT⁺ electronically excited fall below the endpoint and are
   dropped, and ro-vibrational plus Doppler broadening is modelled as a
   0.4 eV Gaussian, checked by simulation [src: arXiv:2202.04587].
3. **Physical region.** Only m_ν² ≥ 0 is allowed, because the capture
   line position is undefined otherwise and an excess near the endpoint
   is "best explained with a positive (physical) neutrino capture
   signal" [src].
4. **Fit and limit.** Free parameters A_s (β normalisation), E₀, m_ν²,
   R_bg and η; systematics by the covariance-matrix approach of the mass
   analysis; a two-dimensional scan over m_ν² ∈ [0, 1] eV² and η, the
   other parameters profiled; 1000 pseudo-experiments for the
   null-hypothesis probability. KNM1 best fit η = (3.7 ± 1.4) × 10¹¹,
   Δχ² = 3.7 against η = 0, probability 2% under the null; KNM2 η =
   (−5.8 ± 5.2) × 10¹⁰, 5%; the KNM2 and combined contours are computed
   relative to the null hypothesis "so as not to benefit from the
   non-physical best fit"; the two campaigns are combined by adding χ²
   surfaces, minimum χ² = 50.7 for 50 degrees of freedom [src: arXiv:2202.04587, Sect. "Combination of individual results" and the KNM1/KNM2 result paragraphs before it].
5. **Result.** η < 9.7 × 10¹⁰ (90%) or 1.1 × 10¹¹ (95%); projected final
   KATRIN sensitivity η < 10¹⁰ (90%) [src: arXiv:2202.04587, abstract]. Earlier
   kinematic experiments gave about 10¹³ [src].

### Step 4. Forecast a dedicated experiment: PTOLEMY
<!-- key: step-4-forecast-a-dedicated-experiment-ptolemy -->

The PTOLEMY collaboration's 2019 sensitivity study (arXiv:1902.05508
[src]):

1. **Binned counts.** β and capture events per bin of width Δ
   (Eqs. 17–18) plus a constant background; Γ_b ≈ 10⁻⁵ Hz in a 15 eV
   window, "1 or 2 per each energy bin per year", is required for
   Δ = 50 meV [src: arXiv:1902.05508, Sect. 4].
2. **Asimov data.** Expected counts with √N errors, no fluctuations
   (Eq. 21); systematic errors deferred until the detector design is
   fixed [src].
3. **Fit.** Linear priors A_β ∈ [0, 2], ln N_b ∈ [−1, 3], ΔE_end ∈ [−1, 1]
   eV, m_lightest ∈ [0, 1] eV with fixed oscillation splittings, and a
   capture normalisation A_CNB ∈ [0, 5] with fiducial value 1; a
   detection is claimed when the credible interval of A_CNB excludes
   zero; a Savage–Dickey model comparison gave "slightly more
   pessimistic results" [src].
4. **Outcome.** Configurations with less than 100 g of tritium "are not
   suitable" for a CνB search; clustering, Majorana nature or
   non-standard interactions help only if the resolution separates the
   signal from the β background [src: Sect. 6]. The review summarises
   the target as about 100 g, Δ of about 0.1 eV, about 5 events per
   year, and a 3σ observation in a year for masses above 0.2 eV in the
   first simulations (arXiv:2404.19322 Sect. V.1 [src]).

### Step 5. Predict the local overdensity
<!-- key: step-5-predict-the-local-overdensity -->

- **Method.** Neutrinos with a Fermi–Dirac distribution at T_ν,0 ≈ 1.95 K
  are followed through the gravitational potential of Milky Way-like
  haloes with Hamilton's equations (Eq. 1), rewritten with velocity
  instead of momentum and a time variable s(z) (Eq. 2) so that one run
  serves all masses; 27 haloes of M₂₀₀ = (0.6–2.0) × 10¹² M⊙ from a
  25 Mpc box, 80 000 neutrinos per halo spanning 0.01–400 T_ν,0 in
  momentum, and healpix maps (N_side = 8) for anisotropies (Zimmer,
  Correa & Ando 2023, arXiv:2306.16444 Sects. 2–3 [src]).
- **Result.** Clustering factors of 1 + 𝒪(10⁻³) to 1 + 𝒪(1) for 0.01–
  0.3 eV, from about 1.0005 at 0.01 eV to about 3 at 0.3 eV, the spread
  set mainly by halo mass; the analytic NFW approach agrees in
  normalisation and slope when the same halo parameters are used [src:
  abstract, Sect. 4.1]. KATRIN quotes 1.2 to 20 for m_ν < 0.6 eV from
  earlier work [src: arXiv:2202.04587]. The 2014 phenomenology paper
  quotes "a few tens of per cent" at m_ν ~ 0.1 eV, comparable to the
  statistical error of a few years of PTOLEMY data [src:
  arXiv:1405.7654 Sect. 4.2].
- **Bounds on η from other arguments.** The Pauli principle disfavours
  η ≫ 1 at small masses but allows η ≲ 125 at m_ν ≈ 0.8 eV; cosmology
  "strongly favours" 0.2 ≲ η ≲ 3.5 (Bauer & Shergold 2022,
  arXiv:2207.12413 abstract [src]). Cosmic rays scattering on relic
  neutrinos give η ≲ 10¹³ locally for m_ν ~ 0.1 eV (Císcar-Monsalvatje,
  Herrera & Shoemaker 2024, arXiv:2402.00985 abstract [src]).

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Molecular, atomic or bound tritium
<!-- key: molecular-atomic-or-bound-tritium -->

| Target | Limitation stated | Source |
|---|---|---|
| Molecular gas (KATRIN) | the final-state ground-state distribution extends the endpoint by ⟨E_GS⟩ ≈ 1.7 eV, an "irreducible background" for m_ν < 0.85 eV; the β tail exceeds the capture signal by about seven orders of magnitude at η = 1; η limits "well below 1 · 10⁶" for m_ν < 0.85 eV seem unlikely, "making the actual detection of CνB with molecular tritium virtually impossible" | arXiv:2202.04587 [src: Sect. "Keywords:"] |
| Gas generally | KATRIN "falls short of the required sample activity by six orders of magnitude" | arXiv:2101.10069 [src] |
| Tritium on graphene (PTOLEMY) | zero-point motion of the bound nucleus broadens the electron energy by ΔE ≈ (ħc/λ_el) γ (Eq. 5), γ = [Q² m_e/(m_nucl³ c⁴)]^(1/4) (Eq. 6); ΔE ≈ 0.60–0.75 eV for chemisorption and 0.22–0.33 eV for physisorption across ab initio potentials (Table 1); ΔE ∝ κ^(1/4) in the binding stiffness κ, so an order-of-magnitude gain needs κ four orders smaller; tritium (γ ≈ 3 × 10⁴) "lies deep inside the region where the observation of the CνB peak is impossible"; heavier emitters are listed as alternatives | arXiv:2101.10069 [src] |
| Same, collaboration analysis | the spread for one tritium atom on flat graphene is "at least an order of magnitude larger than the energy resolution expected"; if ³He⁺ ends in the continuum the capture peak is hidden, if bound the rate is exponentially suppressed; proposed mitigations: hydrogen-passivated carbon nanotubes (sliding along the axis) and a magnetic field against dimerisation | PTOLEMY Collaboration (Apponi et al.) 2022, arXiv:2203.11228 Sect. V [src] |

The 2022 analysis includes the authors of the 2021 objection, and both
leave the remaining spread from thermal motion and electronic
excitations to future work [src: arXiv:2203.11228 Sect. V].

### Dirac or Majorana, and what A_CNB measures
<!-- key: dirac-or-majorana-and-what-acnb-measures -->

A fitted capture normalisation mixes the Dirac/Majorana factor of two,
clustering and non-standard interactions; the PTOLEMY study names this
degeneracy and does not attempt to separate them [src: arXiv:1902.05508
Sect. 4]. KATRIN's limit is stated for Majorana neutrinos; a Dirac
reading doubles it [der: R_cap halved, arXiv:2202.04587].

### Ordering
<!-- key: ordering -->

At small masses, detection is easier in the inverted ordering, because
m₁ and m₂ are larger and their peaks lie further above the endpoint
[src: arXiv:1902.05508 Sect. 6]. For direct-detection proposals in
general, observing the background "without a significant overdensity"
needs m_ν ≳ 50 meV, otherwise η ≳ 3 × 10⁵ [src: arXiv:2207.12413
abstract].

### Flux or wind
<!-- key: flux-or-wind -->

Measuring the dipole of the flux from the motion through the CνB frame
needs an exposure at least 10⁵ times that for detecting the flux, and
for non-relativistic Majorana neutrinos the signal is further suppressed
by a factor of order (m_ν/T_ν)² (Long, Uwabo-Niibo & Yamaguchi 2026,
arXiv:2607.05221 abstract [src]). The review notes that annual
modulation can help when the resolution is insufficient, but the
required number of events is "still far from any proposed realization"
[src: arXiv:2404.19322 Sect. V.1, footnote 3].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Number density per degree of freedom | n₀ ≈ 56 cm⁻³ | theory | arXiv:1405.7654 | Eq. 9 |
| Relic temperature today | T_ν,0 ≈ 1.95 K; mean energy ~0.5 meV (review) | theory | arXiv:2306.16444; arXiv:2404.19322 | Sect. 2; Sect. V |
| Capture rate, 100 g ³H, unclustered | 8.12 yr⁻¹ (Majorana), 4.06 yr⁻¹ (Dirac) | PTOLEMY-like | arXiv:1405.7654 | Eq. 57 |
| Per-nucleus rate | 4.2 × 10⁻²⁵ yr⁻¹ (Majorana) | KATRIN | arXiv:2202.04587 | after Eq. 4 |
| Resolution criterion | Δ ≲ 0.7 m_ν (Majorana) | PTOLEMY-like | arXiv:1405.7654 | Fig. 3, abstract |
| PTOLEMY design resolution in the 2014 study | 0.15 eV | — | arXiv:1405.7654 | Sect. 3 |
| Background requirement | Γ_b ≈ 10⁻⁵ Hz in 15 eV, for Δ = 50 meV | PTOLEMY forecast | arXiv:1902.05508 | Sect. 4 |
| Prototype voltage control | resolution better than 500 meV needs a few ppm; achieved 0.2 ppm per 1 kV board, ≲ 50 mV over 10 kV | PTOLEMY prototype | Ammendola et al. 2025, arXiv:2512.19437 | abstract |
| KATRIN spectrometer resolution | 2.8 eV at 18.57 keV | KATRIN 2019 | arXiv:2202.04587 | Sect. "Experimental setup"; abstract for 18.57 keV |
| KATRIN overdensity limit | η < 9.7 × 10¹⁰ (90%), 1.1 × 10¹¹ (95%); final sensitivity < 10¹⁰ (90%) | KNM1 + KNM2 | arXiv:2202.04587 | abstract |
| Molecular endpoint extension | ⟨E_GS⟩ ≈ 1.7 eV; irreducible below m_ν = 0.85 eV | KATRIN | arXiv:2202.04587 | Sect. "Relic neutrino analysis" |
| Zero-point broadening on graphene | 0.60–0.75 eV (chemisorption), 0.22–0.33 eV (physisorption) | tritium on graphene | arXiv:2101.10069 | Table 1 |
| Clustering factor | ~1.0005 (0.01 eV) to ~3 (0.3 eV) | 27 simulated haloes | arXiv:2306.16444 | Sect. 4.1 |
| Overdensity favoured by cosmology | 0.2 ≲ η ≲ 3.5 | compilation | arXiv:2207.12413 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Recoil left out of the endpoint.** The shift exceeds the neutrino
  mass (arXiv:1405.7654 footnote 6). Test: compute K_end with recoil.
- **Molecular final states.** Treating molecular tritium as atomic hides
  the 1.7 eV extension of the endpoint and the 43% of captures lost
  below it (arXiv:2202.04587, Sect. "Keywords:"). Test: include the final-state
  distribution in both β and capture spectra.
- **Unphysical best fits.** A negative η or m_ν² best fit can make a
  limit look tighter; KATRIN builds contours relative to the null
  hypothesis and restricts m_ν² ≥ 0 (arXiv:2202.04587).
- **Look-elsewhere and fluctuations.** A 2% null-hypothesis probability
  for KNM1 was not taken as evidence; pseudo-experiments set the
  probability (arXiv:2202.04587).
- **Asimov forecasts without systematics.** The PTOLEMY sensitivity has
  no detector systematics yet (arXiv:1902.05508 Sect. 4); a forecast
  quoted from it should say so.
- **Ignoring the bound-state physics.** A forecast that assumes an
  atomic-tritium line on a solid substrate omits the zero-point spread
  (arXiv:2101.10069; arXiv:2203.11228).
- **Reading A_CNB as a single property.** It combines the
  Dirac/Majorana factor, clustering and interactions
  (arXiv:1902.05508).
- **Over-optimistic clustering.** For neutrino masses between 0.01 and 0.3 eV the clustering factor ranges from 1 + O(10⁻³) to 1 + O(1) (arXiv:2306.16444, abstract; about 1.0005 at 0.01 eV, Sect. 4.1); an assumed large η needs a source.

## Reading list
<!-- key: reading-list -->

- Review: Di Valentino, Gariazzo & Mena 2024, arXiv:2404.19322 Sect. V —
  the methods (capture, Stodolsky effect, coherent scattering, ion
  beams) and the motivation.
- Foundation of the rate: Long, Lunardini & Sabancilar 2014,
  arXiv:1405.7654 — kinematics, Dirac/Majorana factor, resolution
  criterion.
- Data analysis: KATRIN (Aker et al.) 2022, arXiv:2202.04587 — the only
  limit from a running experiment; fit, physical region, molecular
  effects.
- Forecast: PTOLEMY Collaboration 2019, arXiv:1902.05508 — Bayesian
  sensitivity method and requirements.
- Critique: Cheipesh, Cheianov & Boyarsky 2021, arXiv:2101.10069 —
  zero-point broadening of bound tritium.
- Response: PTOLEMY Collaboration 2022, arXiv:2203.11228 — quantified
  spread, nanotubes.
- Clustering: Zimmer, Correa & Ando 2023, arXiv:2306.16444 — simulated
  local overdensity and anisotropies.
- Limits: Bauer & Shergold 2022, arXiv:2207.12413 (abstract) — Pauli,
  cosmology and experiment on η.
- Indirect: Císcar-Monsalvatje, Herrera & Shoemaker 2024,
  arXiv:2402.00985 (abstract) — cosmic-ray boosted relic neutrinos.
- Beyond the flux: Long, Uwabo-Niibo & Yamaguchi 2026, arXiv:2607.05221
  (abstract) — the CνB wind.

## Not verified
<!-- key: not-verified -->

- The PTOLEMY detection-significance curves (Fig. 5 of
  arXiv:1902.05508) were not read as numbers; only the qualitative
  conclusions are quoted.
- The values of σ̄, and the Fermi-function and form-factor inputs behind
  Eq. 57 of arXiv:1405.7654, were not checked individually.
- The quantitative spread computed in arXiv:2203.11228 Sects. II–IV and
  the electronic-excitation analysis it cites (its ref. [60]) were not
  read.
- Alternative detection methods named in the review (Stodolsky effect,
  coherent scattering on macroscopic targets, capture on accelerated
  ion beams) and later proposals found in a search (matter
  interferometers, sub-meV threshold detectors) were not researched.
- No KATRIN overdensity result from data later than 2019 was found in
  the search run on 2026-10-19; absence is not established.
- The neutrino-temperature distortions from late entropy injection,
  which change n₀, were seen only in titles of 2026 papers.
