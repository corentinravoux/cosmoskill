# Damping tail and light relics — cosmo-cmb dossier

Scope: how N_eff and Y_P are extracted from the CMB damping tail and the
acoustic phase, which parameters are held fixed to isolate each effect,
how the free-streaming phase shift is measured separately from the
damping, which BBN table and helium convention each collaboration uses,
and which modelling and foreground choices move N_eff; the N_eff,
Y_P and Σm_ν values themselves are in the reference files.
Snapshot: 2026-10-18.
From: Snowmass CMB white paper, Sect. 2 (light relics and neutrino
physics); SO science goals, Sect. IV.

Already in L2, not repeated here: the N_eff and Σm_ν tables by data set
and the ACT ΔN_eff limits (`results.md#light-relics-and-neutrino-mass`);
the definition of N_eff, the convention for its standard value and the
foundation papers on damping and phase (`physics-and-methods.md#extension-parameters-as-actually-defined`);
the ACT-low versus SPT-standard question and the FIRAS argument
(`open-questions.md#neff-act-low-spt-at-the-standard-value`); the
non-linear lensing and feedback biases (`systematics.md#lensing-related-modelling-of-the-primary-spectra`).
For BBN-side light-relic physics see
`cosmo-bbn/deep/neff-new-physics.md`; for the BAO phase shift and
neutrino-mass physics, `cosmo-neutrinos-dark-matter`.

## How it is done
<!-- key: how-it-is-done -->

Notation. N_eff is defined by ρ_rad = ρ_γ[1 + (7/8)(4/11)^{4/3} N_eff]
(arXiv:2506.20707, Eq. 70). θ_s and θ_d are the angular sizes of the
sound horizon and of the photon diffusion length at recombination;
r_s and r_d the corresponding comoving lengths. Y_P is the primordial
helium abundance, written as a mass fraction (Y_He in CAMB/CLASS, Y_P in
the SPT paper) or as a nucleon number fraction (Y_p in the ACT paper; the
two differ by about 0.001, see Step 4). ε(N_eff) ≡ ρ_ν/ρ_r, the
neutrino fraction of the total radiation density, is the free-streaming
fraction of the radiation (arXiv:2501.13788, Eq. 2.2).

### Step 1. Know what the damping tail actually measures
<!-- key: step-1-know-what-the-damping-tail-actually -->

- With θ_s, the baryon density and z_EQ held fixed, raising N_eff lowers
  high-ℓ power. Hou et al. attribute this almost entirely to extra Silk
  damping, not to the early ISW effect: normalising at ℓ = 400, where ISW
  is negligible, barely reduces the effect [src: arXiv:1104.2333,
  Sect. II.2].
- The mean squared diffusion length is
  r_d² = π² ∫₀^{a*} da/(a³σ_T n_e H) × [R² + (16/15)(1 + R)]/[6(1 + R²)]
  (arXiv:1104.2333, Eq. 1), so r_d ∝ H^{−0.5}, while r_s ∝ 1/H (Eq. 2).
  Keeping θ_s fixed forces D_A ∝ 1/H, so θ_d/θ_s = r_d/r_s ∝ H^{0.5}: the
  data measure the expansion rate before recombination through the ratio
  of two angles, independent of D_A [src: Sect. II.2].
- Fixing θ_d as well, by adjusting Y_P, removes almost all of the N_eff
  signal; what remains is the phase shift [src: Sect. II.2, Fig. 1].
  Y_P acts only through n_e = X_e n_b(1 − Y_P), because helium is neutral
  when hydrogen recombines [src].

Ge, Cyr-Racine and Knox give the general reason. The linear equations
are invariant under √(Gρ_i) → λ√(Gρ_i), σ_T n_e → λσ_T n_e (with
k → λk), arXiv:2210.16335, Eq. 6. Adding light relics breaks this
symmetry in four ways, ordered by impact:

1. change of the photon scattering rate relative to the Hubble rate
   (damping and polarisation generation);
2. change of the free-streaming fraction of the radiation (phase and
   amplitude);
3. change of the fraction of non-relativistic matter that is pressure
   supported;
4. change of recombination rates relative to the Hubble rate.

At N_eff = 4.61 (λ = 1.1) they produce spectral differences of 10–15%,
5–6%, 2–3% and 1–2% respectively [src: Sect. V]. A fixed Σm_ν = 0.06 eV
breaks the symmetry only at a fraction of a percent [src]. SPT uses this
framework to explain why the CMB degeneracy direction lowers Ω_m as N_eff
rises, unlike the BAO-preserving direction [src: arXiv:2506.20707,
Sect. VII.2.4].

### Step 2. Choose the parameter set
<!-- key: step-2-choose-the-parameter-set -->

Standard value N_eff = 3.044 as used in arXiv:2503.14454 (Sect. VI.1.1) and arXiv:2506.20707 (Sect. VII.2.4):

| Model | What varies | What it isolates | Analysis |
|---|---|---|---|
| ΛCDM + N_eff, BBN-consistent Y_P | N_eff; Y_P from a BBN table as a function of (Ω_b h², N_eff) | expansion rate before recombination plus phase | ACT DR6, SPT-3G D1, Planck 2018 |
| ΛCDM + Y_P | Y_P free, N_eff = 3.044 | damping through n_e | ACT, SPT |
| ΛCDM + N_eff + Y_P | both free | phase and residual effects (cause 2–4) once θ_d is free | ACT, SPT |
| ΛCDM + ΔN_eff > 0 | extra species added to 3.044 | limits on new particles by spin and decoupling temperature | ACT |
| ΛCDM + N_eff^δℓ or N_eff^δφ (with or without N_eff) | phase-shift amplitude only | free streaming, independent of damping | Montefalcone et al. 2025 |

ACT reports the ΔN_eff > 0 fit, rather than the tail of the full N_eff
posterior, "we assume the existence of another species in addition to the
three SM neutrinos" [src: arXiv:2503.14454, Sect. VI.1.1, Fig. 20
caption]. The positive-only fit gives ΔN_eff < 0.17 for P-ACT-LB, and
lensing and BAO relax it by moving the N_eff posterior up (< 0.14 for
P-ACT) [src: Eq. 32].

### Step 3. Pick the BBN table and theory settings
<!-- key: step-3-pick-the-bbn-table-and-theory-settings -->

| Analysis | BBN table for Y_P | Neutron lifetime | Other settings | Place |
|---|---|---|---|---|
| Planck 2018 | PArthENoPE 1.1 grid | fixed 880.2 s | Y_P (mass) ≈ 0.2454; PRIMAT higher by ΔY_P ≈ 0.0005, parameters consistent within 0.1σ | [src: arXiv:1807.06209, Sect. 2.1] |
| ACT DR6 | PRIMAT_2021 (CAMB default; tables imported into CLASS) | 879.4 ± 0.6 s | CosmoRec (CAMB) or HyRec (CLASS); HMcode-2020 dark-matter only; lens_potential_accuracy 8, lAccuracyBoost 1.2 | [src: arXiv:2503.14454, Sect. VI.2; App. A, Figs. 47–48] |
| SPT-3G D1 | PArthENoPE tables (CLASS default in the version used) | — | ACT DR6 accuracy settings (L2) | [src: arXiv:2506.20707, Sect. VII.2.4, footnote 41] |

- ACT's stated reason for CosmoRec over RecFast: RecFast's fudge factors
  are tuned to Planck sensitivity, and away from the best fit RecFast
  differs from HyRec or CosmoRec by Δχ² ~ O(100), mostly from TT at
  ℓ ≈ 2000, although no posterior moved [src: arXiv:2503.14454, App. A].
  At the best fit the differences are Δχ² = 0.37 (HyRec) and 0.49
  (CosmoRec) [src].
- ACT states that the three BBN configurations it tested return the same
  cosmological parameters and differ only in predicted abundances [src:
  Sect. VI.2].

### Step 4. Convert and compare helium consistently
<!-- key: step-4-convert-and-compare-helium-consistently -->

- ACT gives Y_p ≡ n_He/n_b (nucleon fraction), not the mass fraction Y_He
  used inside CMB codes [src: arXiv:2503.14454, Sect. VI.2]. Planck 2018
  gives both: mass fraction ≈ 0.2454, nucleon fraction ≈ 0.2467 for the
  same model [src: arXiv:1807.06209, Sect. 2.1]. SPT's Y_P is the mass
  fraction [src: arXiv:2506.20707, footnote 41].
- ACT treats the astrophysical helium datum as a prior (PDG 2024,
  Y_p = 0.245 ± 0.003, which does not include the EMPRESS value
  0.2370 ± 0.0034, about 2.4σ lower) [src: arXiv:2503.14454, Sect. VI.2].
  SPT compares with Y_P = 0.2453 ± 0.0034 from metal-poor galaxies [src:
  arXiv:2506.20707, Sect. VII.2.4].

### Step 5. Measure the phase shift on its own
<!-- key: step-5-measure-the-phase-shift-on-its-own -->

Montefalcone, Wallisch and Freese build two templates [src:
arXiv:2501.13788, Sects. 2.2–2.3]:

- Spectrum-based (arXiv:2501.13788). The multipole shift relative to N_eff = 3.044 is
  δℓ(N_eff) = A(N_eff) f_ℓ (Eq. 2.4), with
  A(N_eff) = [ε(N_eff) − ε(3.044)]/[ε(1) − ε(3.044)] (Eq. 2.5) and
  f_ℓ = ℓ_∞/[1 + (ℓ/ℓ_⋆)^ξ] (Eq. 2.6), fitted to peak and trough shifts of
  100 CLASS cosmologies with N_eff ∈ [1, 6] at fixed ω_b, a_eq, θ_s and
  θ_d, ISW removed: ℓ_∞ = 11.0 ± 0.6, ℓ_⋆ = 483 ± 53, ξ = −1.69 ± 0.13.
  The template uses TT, TE and EE because polarisation peaks are sharper
  and free of SW and ISW terms [src: Sect. 2.2.1].
- The shift is applied only to the ISW-free part of the undamped
  spectrum, K_ℓ ≡ ℓ(ℓ+1)C_ℓ/2π × exp[a(θ_d ℓ)^κ] (Eq. 2.3), then the
  damping is restored (Eq. 2.8). Writing Δℓ = [A(N_eff^δℓ) − A(N_eff)]f_ℓ
  (Eq. 2.7) prevents double counting the shift already in the CLASS
  spectra [src: Sect. 2.2.2].
- Perturbation-based. The phase is applied to the photon-baryon sources
  inside the line-of-sight integral, k → k + Δφ/r_s in Θ₀ + Ψ, Π, θ_b/k and
  θ_b′/k² (Eq. 2.19), with the ISW source left unshifted [src: Sect. 2.3.2].
- Validation on Planck-like mocks (arXiv:2501.13788): three massless neutrinos, three with
  Σm_ν = 0.06 eV, and two free-streaming plus one fluid species are all
  recovered, and mass does not bias the phase [src: Sect. 2.4].

Why it matters: N_eff in a ΛCDM + N_eff fit counts fluid-like radiation
too, because it is driven by the damping tail; only free-streaming
species shift the phase, so N_eff^δℓ or N_eff^δφ counts free-streaming
species [src: Sect. 2.2.2, footnote 9].

### Step 6. Decide whether CMB and BAO may be combined
<!-- key: step-6-decide-whether-cmb-and-bao-may-be -->

SPT combines CMB with DESI in an extended model only if the two agree in
(Ω_m, h r_d) within 3σ. For ΛCDM + N_eff, + Y_P and + N_eff + Y_P, the
SPT+ACT and CMB-SPA posteriors fail that rule, so only SPT-3G D1 + DESI
is reported [src: arXiv:2506.20707, Sect. VII.4.2]. The reason is
physical: BAO observables are invariant under the "BAO scaling" (to
< 0.2% in peak positions even at N_eff = 5), while the CMB best fit needs
ρ_m to rise more slowly than ρ_rad, so N_eff moves the CMB along a
degeneracy that BAO crosses [src: Sects. VII.2.4, VII.4.2, footnote 47].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### BBN-consistent Y_P or free Y_P
<!-- key: bbn-consistent-yp-or-free-yp -->

- BBN-consistent: tightest N_eff (ACT 2.60 (+0.21/−0.29); P-ACT
  2.73 ± 0.14; arXiv:2503.14454) [src: Sect. VI.1.1, Eq. 30], at the price of assuming standard BBN between z ~ 10⁹ and
  recombination.
- Free Y_P: N_eff and Y_P anti-correlate at fixed θ_s, because both set
  the damping [src: arXiv:2501.13788, Sect. 2.1; arXiv:2503.14454,
  Sect. VI.2.2]. P-ACT-LB gives Y_p = 0.227 ± 0.014 and
  N_eff = 3.14 ± 0.25, against N_eff = 2.86 ± 0.13 with BBN [src: Eq. 46].
  ACT reads the low Y_p and the low N_eff as the same preference for less
  damping [src]. CMB-SPA gives N_eff = 2.96 (+0.21/−0.24),
  Y_P = 0.233 ± 0.013 [src: arXiv:2506.20707, Table 5].
- A helium prior breaks the degeneracy: P-ACT-LB-He gives
  Y_p = 0.2444 ± 0.0029, N_eff = 2.86 ± 0.14 [src: arXiv:2503.14454,
  Eq. 47].
- With Y_P free, contours still close: Hou et al. attribute this partly to
  the phase shift and partly to the high baryon fraction reached at low
  N_eff and fixed z_EQ, which adds a radiation-driving-like boost in the
  matter era [src: arXiv:1104.2333, Sect. II.3].

### Which BBN code
<!-- key: which-bbn-code -->

- For cosmological parameters the code barely matters: Planck finds
  PArthENoPE and PRIMAT consistent within 0.1σ [src: arXiv:1807.06209,
  Sect. 2.1]; ACT finds identical parameters across its three
  configurations [src: arXiv:2503.14454, Sect. VI.2].
- For predicted abundances it matters. ACT (arXiv:2503.14454), P-ACT-LB, ΛCDM: predicted
  Y_p 0.24727, 0.24707, 0.24691 for PRIMAT_2021, PRIMAT_2024 (τ_n = 878.4 s [src: Sect. VI.2]),
  PRyMordial, the first shift from τ_n and the second from reaction rates;
  predicted D/H × 10⁵ = 2.415, 2.413 and 2.480, with PRIMAT 2–3σ from the
  PDG average and PRyMordial consistent [src: Eqs. 39, 41]. Joint CMB +
  D/H fits are therefore run with PRyMordial only [src: Sect. VI.2.1].

### Damping-tail N_eff or phase-shift N_eff
<!-- key: damping-tail-neff-or-phase-shift-neff -->

- N_eff (damping): sensitive to anything that changes the high-ℓ
  amplitude (foregrounds, beams, calibration, feedback; see below).
- Phase-shift parameter: read from peak and trough positions; adding ACT
  and SPT to Planck sharpens N_eff^δℓ by about 25%, mainly through
  higher multipoles [src: arXiv:2501.13788, Sect. 3.1]. The
  perturbation-based template is preferred by its authors: its central
  value is unchanged between Planck PR3 and PR4, while the spectrum-based
  value moves toward it on PR4; they suggest the PR3 difference may be
  related to the A_L excess [src: Sect. 3.3, footnote 20].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Phase-shift template | ℓ_∞ = 11.0 ± 0.6, ℓ_⋆ = 483 ± 53, ξ = −1.69 ± 0.13 | CLASS, 100 cosmologies | arXiv:2501.13788 | Sect. 2.2.1 |
| N_eff^δℓ, ΛCDM + N_eff^δℓ | 2.87 (+0.54/−0.73) P18 TT; 2.67 (+0.39/−0.43) P18 TTTEEE; 2.87 (+0.31/−0.35) P18 + ACT + SPT | Planck PR3 Plik ± ground data | arXiv:2501.13788 | Table 2 |
| N_eff^δℓ = 0 excluded | Δχ² = 24, 52, 97: about 7σ, 10σ, 14σ | same three combinations | arXiv:2501.13788 | Sect. 3.1, footnote 18 |
| N_eff^δφ, Planck PR4 | 2.33 (+0.28/−0.33) CamSpec; 2.34 (+0.28/−0.33) HiLLiPoP | PR4 alone, N_eff fixed | arXiv:2501.13788 | Table 4 |
| Two free-streaming + one fluid species | excluded at > 2.5σ | P18 + ACT + SPT | arXiv:2501.13788 | Sect. 3.1 |
| Phase-shift error, **forecast** | 4.3% (SO), 2.5% (CMB-S4) | Fisher | arXiv:2501.13788 | abstract |
| Spectral differences at N_eff = 4.61 by cause 1–4 | 10–15%, 5–6%, 2–3%, 1–2% | theory | arXiv:2210.16335 | Sect. V |
| H₀ with N_eff free | 67.00 ± 0.91 | P-ACT-LB | arXiv:2503.14454 | Sect. VI.1.1 |
| Photon-energy increase for the P-ACT (P-ACT-LB) central N_eff | 12% (6%); μ = 0.16 or y = 0.03 (0.09, 0.02) | ACT DR6 | arXiv:2503.14454 | Sect. VI.1.1 |
| FIRAS-allowed ΔN_eff from μ or y era injection | about −0.0002 | ACT DR6 | arXiv:2503.14454 | Sect. VI.1.1, footnote 25 |
| N_eff, BBN only (D + He, PRyMordial) | 2.93 ± 0.21 | PDG abundances | arXiv:2503.14454 | Sect. VI.2.1 |
| N_eff, Y_P from SPT-3G D1 alone, both free | 2.98 (+0.40/−0.64), 0.269 (+0.040/−0.030) | SPT-3G D1 | arXiv:2506.20707 | Table 5 |
| N_eff, SPT-3G D1 + DESI | 3.53 ± 0.23 (2.1σ above 3.044) | ΛCDM + N_eff | arXiv:2506.20707 | Eq. 86 |
| N_eff from SPT lensed EE + φφ vs MUSE unlensed EE + φφ | 3.36 (+0.77/−0.88) vs 2.70 (+0.70/−0.91) | SPT-3G D1 | arXiv:2506.20707 | Sect. VII.2.4, footnote 40 |
| Planck τ_n uncertainty → σ(Y_P^BBN) | 1.0 s → 3.0 × 10⁻⁴; 0.8 s → 2.4 × 10⁻⁴ | PArthENoPE, PRIMAT | arXiv:1807.06209 | Sect. 7.6.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

| Failure | How it shows | Test or fix | Place |
|---|---|---|---|
| tSZ spectral shape fixed when the data prefer a tilt | N_eff and Ω_c h² shift by 0.5σ in P-ACT ΛCDM + N_eff when α_tSZ is fixed to 0; 0.3σ for ACT alone | marginalise α_tSZ (2.2–2.7σ from 0 in ΛCDM + N_eff) | [src: arXiv:2506.06274, Sect. IV.3] |
| Other foreground-template choices | ΛCDM + N_eff parameters move < 0.5σ in all ACT tests; no alternative fits better | template and extension tests | [src: arXiv:2506.06274, abstract, Sect. IV.2] |
| Achromatic beams in the likelihood | N_eff biased by up to 0.3σ for an SO-like LAT (**forecast**) | chromatic beam windows | [src: arXiv:2411.10124, Sect. III] |
| Outdated recombination code | Δχ² ~ O(100) away from the best fit, TT near ℓ ≈ 2000 | HyRec or CosmoRec | [src: arXiv:2503.14454, App. A] |
| Mixing helium conventions | spurious 0.001 offsets between "Y_P" values | state nucleon or mass fraction | [src: arXiv:1807.06209, Sect. 2.1] |
| Combining CMB and BAO along the N_eff degeneracy | joint N_eff dragged by BAO; SPT+ACT and CMB-SPA fail the 3σ rule | consistency test before combining | [src: arXiv:2506.20707, Sect. VII.4.2] |
| Reading a low N_eff from damping as "fewer free-streaming species" | damping counts fluid and free-streaming radiation alike | phase-shift parameter | [src: arXiv:2501.13788, Sect. 2.2.2] |
| A subset fluctuation read as physics | ACT N_eff per spectrum and frequency compared with the expected subset scatter; total dominated by ACT TT and TE | subset tests with nested-shift bands | [src: arXiv:2503.14454, Sect. VI.1.1, Fig. 21] |

ACT's own reading of the robustness test: the result is "stable across
probes, frequencies, and combinations with Planck", and N_eff "is often
used as a proxy parameter to explore the sensitivity of small-scale CMB
data to physics that impacts the damping tail" [src: arXiv:2503.14454,
Sect. VI.1.1]. A shift in N_eff is therefore first a statement about the
damping tail, and only second about relics.

## Reading list
<!-- key: reading-list -->

- Foundation: Hou et al. 2011, arXiv:1104.2333 — why N_eff is a damping
  measurement: the expansion rate sets the ratio of the diffusion scale to
  the sound horizon [src: abstract]; the role of Y_P and of the baryon
  fraction.
- Foundation: Baumann et al. 2015, arXiv:1508.06342 — the phase shift as
  a robust signature of free streaming.
- Method: Ge, Cyr-Racine & Knox 2022, arXiv:2210.16335 — scaling
  symmetry and the four causes that make light relics observable; read
  before interpreting a degeneracy direction.
- Method: Montefalcone, Wallisch & Freese 2025, arXiv:2501.13788 — two
  phase-shift templates, mock validation, PR3 versus PR4.
- Application: Calabrese et al. 2025, arXiv:2503.14454, Sects. VI.1–VI.2
  and App. A — ACT N_eff, ΔN_eff, Y_p, BBN codes and theory settings.
- Application: Camphuis et al. 2025, arXiv:2506.20707, Sects. VII.2.4 and
  VII.4.2 — SPT N_eff and Y_P, rate-ratio interpretation, CMB–BAO
  combination rule.
- Application: Planck Collaboration 2018, arXiv:1807.06209, Sects. 2.1
  and 7.6 — PArthENoPE baseline, helium conventions, BBN error budget.
- Critique and robustness: Beringue et al. 2025, arXiv:2506.06274,
  Sects. IV.2–IV.3 — foreground-model dependence of ΛCDM + N_eff,
  including the α_tSZ shift.

## Not verified
<!-- key: not-verified -->

- The body of Baumann et al. 2015 (arXiv:1508.06342) was not read, only
  its abstract (a phase shift needs modes faster than the plasma sound
  speed: free-streaming radiation or isocurvature). It is cited for its
  role, not for a number.
- Which ACT and SPT data releases enter "P18 + ACT + SPT" in
  arXiv:2501.13788 was not found in the text read; they predate ACT DR6
  and SPT-3G D1.
- No phase-shift analysis of ACT DR6 or SPT-3G D1 data was found in the
  search of 2026-10-18 beyond the theory-oriented works listed.
- The Snowmass white paper section named in "From" was not re-read for
  this dossier.
