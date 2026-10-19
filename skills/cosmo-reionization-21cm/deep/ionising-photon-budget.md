# Ionising-photon budget — cosmo-reionization-21cm dossier

Scope: how an ionising-photon budget is built from galaxy data (UV luminosity
function, ξ_ion from Balmer lines or SED fits, f_esc from indirect indicators
or spectral fitting, faint-end cutoff, clumping factor, the ionisation-balance
equation) and checked against τ and the forest emissivity, and how much each
choice moves the end of reionisation.
Snapshot: 2026-10-19.
From: Fan, Bañados & Simcoe 2023 review (arXiv:2212.06907), Sect. 6.1; Gnedin
& Madau 2022 (arXiv:2208.02260), Sects. 2.5 and 5.1; SKA EoR/CD synergies
chapter (arXiv:2606.30947), Sect. 2.1.

Already in L2, not repeated here: the clumping definition of Pawlik et al. and
the Madau, Haardt & Rees criterion (`physics-and-methods.md#ionising-photon-budget`);
the "crisis" and its proposed resolution as headline statements
(`results.md#jwst-early-galaxies-as-a-cosmological-constraint`,
`open-questions.md#which-galaxies-reionised-the-universe`); the sample and f_esc
systematics in one line each (`systematics.md#jwst-abundances-and-the-photon-budget`);
the halo-abundance stress test of JWST galaxies, in the sibling
`cosmo-tensions-anomalies/deep/high-redshift-galaxies.md`.

## How it is done
<!-- key: how-it-is-done -->

Notation, as Muñoz et al. 2024 write it (arXiv:2404.07250, Sect. 2) [src]:
x_HII = 1 − x_HI is the volume-averaged ionised fraction (Q_HII in other
papers); ṅ_ion the comoving density rate of ionising photons reaching the
IGM; n_H = ρ_b (1 − Y_He)/m_H the hydrogen density, Y_He the helium mass
fraction; Φ_UV the UV luminosity function per magnitude; L_UV the luminosity
density at rest 1500 Å; ξ_ion the production rate of ionising photons per
unit L_UV (Hz erg⁻¹); f_esc the fraction escaping into the IGM; C the
clumping factor; α_B the case-B recombination coefficient. "Ṅ_ion" denotes
the rate per galaxy in the galaxy papers and the volume rate in Becker &
Bolton; the meaning is stated at each use.

### Step 1. Write the ionisation balance
<!-- key: step-1-write-the-ionisation-balance -->

The equation every budget paper integrates is
dx_HII/dt = ṅ_ion/n_H − x_HII/t_rec, with t_rec = [C α_B (1 + x_He) n_H]⁻¹
and x_He ≈ Y_He/[4(1 − Y_He)] [src: arXiv:2404.07250, Eqs. 1–2, after Madau
et al. 1999 and Shull et al. 2012]. Written in redshift,
dQ_HII/dz = −[H(z)(1 + z)]⁻¹ (ṅ_ion/⟨n_H⟩ − Q_HII/t̄_rec), integrated from
Q_HII = 0 at z_i = 20 [src: Summerfield et al. 2026, arXiv:2606.14671, Sect.
4.3, Eq. 10].

This is the time-dependent form. The static form (the photon rate needed to
keep the IGM ionised) "should not be used to predict the epoch of
reionization completion because it ignores history-dependent terms"; the
time-dependent form "overestimates the redshift of reionization completion
by δz ~ 1" in a 20 Mpc radiation-hydrodynamic box, and roughly 2 photons per
H atom were needed to reionise it [src: So et al. 2014, arXiv:1311.2152,
abstract]. A mass-weighted variant with a recombination term quadratic in
the ionised fraction and clumping factors fitted to radiative-transfer runs
reproduces the simulated history to < 7% and τ to < 5%, against > 20% for the
widely used models [src: Chen et al. 2020, arXiv:2004.07854, abstract].

### Step 2. Write the emissivity as an integral over galaxies
<!-- key: step-2-write-the-emissivity-as-an-integral-over -->

ṅ_ion = ∫ dM_UV Φ_UV(M_UV) L_UV ξ_ion f_esc, every factor allowed to depend on
M_UV, integrated to a cutoff M_UV^cut [src: arXiv:2404.07250, Eq. 3]. The
same integral over a stellar-mass function, with f_esc a function of mass,
SFR and size, is the alternative of Simmonds et al. [src: arXiv:2409.01286,
Sect. 6.1, Eqs. 8–9]. Only the product ξ_ion f_esc enters; the two are "at
face value, fully degenerate", and Balmer lines measure the non-escaping part
ξ_ion (1 − f_esc) [src: arXiv:2404.07250, Sect. 2].

### Step 3. Measure ξ_ion
<!-- key: step-3-measure-xiion -->

Three routes [src: Simmonds et al. 2024, arXiv:2409.01286, Sect. 5.1]:

1. Hα. Correct the flux for dust (an SMC curve, for example), assume case B,
   f_esc = 0 and no dust absorption of Lyman-continuum photons; then
   ṅ_ion = 7.28 × 10¹¹ L(Hα) (s⁻¹, L in erg s⁻¹) and ξ_ion = ṅ_ion/L_UV at
   1500 Å. The paper names its weak points: "a great dependence on the
   chosen attenuation curve", and case B "cannot always be assumed".
2. [O III] λ5007 equivalent width as a measure of the ionisation field, which
   also depends on metallicity and nebular conditions.
3. Full SED fit (Prospector) with f_esc = 0. On 677 emission-line galaxies at
   z ~ 4–9 the line-based and Prospector values agreed tightly, which is why
   the mass-complete analysis uses the SED fit for every galaxy, lines
   detected or not. The output is ξ_ion,0 = ξ_ion (1 − f_esc) (Eq. 3).

Giovinazzo et al. use the equivalent Leitherer & Heckman conversion
L(Hα) = 1.36 × 10⁻¹² N(H⁰) erg s⁻¹, and recover the intrinsic rate as
Ṅ_ion,int = N(H⁰)/(1 − f_esc) [src: arXiv:2607.22834, Sect. 2.3, Eqs. 2–3].
The two coefficients agree to 1% [der: 1/1.36 × 10⁻¹² = 7.35 × 10¹¹ against
7.28 × 10¹¹].

### Step 4. Assign f_esc
<!-- key: step-4-assign-fesc -->

f_esc cannot be measured directly during reionisation because the IGM absorbs
the escaping photons [src: arXiv:2404.07250, Sect. 2]. Prescriptions in use:

- UV slope. f_esc = A_f × 10^(b_f β_UV), A_f = 1.3 × 10⁻⁴, b_f = −1.22, from the
  z ~ 0 LzLCS survey (Chisholm et al. 2022), applied through a β_UV–M_UV
  relation. β_UV is capped at −2.7, "the bluest galaxies where Eq. (5) is
  calibrated". Averaging over a Gaussian scatter σ_β = 0.34 at fixed M_UV
  raises ⟨f_esc⟩ above f_esc(⟨β⟩) by exp[(b_f ln10 σ_β)²/2] ≈ 1.1–1.5. The
  stated physical reason: dust along the line of sight attenuates the FUV
  continuum and the ionising photons together [src: arXiv:2404.07250, Sect.
  2, Eq. 5 and footnote 2].
- Star-formation surface density. f_esc = min[1, 1.6 (Σ_SFR /1000 M_⊙ yr⁻¹
  kpc⁻²)^0.4] (Naidu et al. 2020), with Σ_SFR = (SFR/2)/(π R²) from a
  size–mass relation and the 10 Myr SFR [src: arXiv:2409.01286, Sect. 6.1,
  Eq. 10].
- UV magnitude. log f_esc = (0.51 ± 0.4) M_UV + 7.3 ± 0.08, from the Vulcan
  simulation (Anderson et al. 2017), and constant 10% or 20% [src:
  arXiv:2409.01286, Sect. 6.1].
- Spectral fit object by object. A picket-fence model: an optically thick
  ISM covers a fraction C_f of the stars and f_esc = 1 − C_f; the model
  spectrum is a linear combination of f_esc = 0 models and f_esc = 1, A_V = 0
  models in the free channels. Raising f_esc steepens β_UV and weakens every
  emission line and the nebular continuum, which is what the fit uses [src:
  Giovinazzo et al. 2025, arXiv:2507.01096, Sect. 3.1]. Settings in the 2026
  budget paper: bagpipes (picket fence in the standard release from v1.3.3),
  non-parametric continuity SFH in seven bins (5–800 Myr), log prior 0.001 <
  f_esc < 1 because "most sources have little-to-no leakage", BPASS v2.2.1
  with an IMF to 300 M_⊙, 0.01 < Z/Z_⊙ < 0.5, Calzetti dust with A_V ≤ 0.5
  "as we were mainly interested in blue sources", no dust on the free
  channels [src: arXiv:2607.22834, Sect. 2.2]. The escaping rate is then the
  integral of the fitted spectrum below 912 Å, Ṅ_ion = ∫ L_ν (hν)⁻¹ dν (Eq.
  4), with the IGM removed (escaping) or with dust removed and f_esc = 1
  (intrinsic) [src: arXiv:2607.22834, Sect. 2.4].
- Learned from simulations. Random forests trained on more than 35,000
  THESAN-ZOOM galaxy realisations at z = 3–16 rank SFR₁₀/SFR₁₀₀ and
  M_gas/M_⋆ as the strongest f_esc indicators and M_UV as the dominant
  predictor of the escaping rate Ṅ_ion,esc; the photometry-only model gives
  log Ṅ_ion,esc = −0.6197 (M_UV + 20) + 0.30 log[(1 + z)/7] + 52.84 for JWST
  galaxies [src: Summerfield et al. 2026, arXiv:2606.14671, abstract, Sect.
  3.3, Eq. 6].

### Step 5. Choose the luminosity function and its faint-end cutoff
<!-- key: step-5-choose-the-luminosity-function-and-its -->

- Muñoz et al.: Bouwens et al. 2021 at z ≤ 9, Donnan et al. 2024 (JWST) at
  z > 9; M_UV^cut is a free parameter, required fainter than −15 by direct
  HST + JWST observations (Atek et al. 2018) [src: arXiv:2404.07250, Sects. 2
  and 3].
- Simmonds et al.: Bouwens et al. 2021, integrated to M_UV = −16, the UV
  completeness of their sample; or the stellar-mass function of Weibel et
  al. 2024 to log M_⋆ = 7.5 [src: arXiv:2409.01286, Sect. 6.1].
- Giovinazzo et al.: GLIMPSE lensing-field luminosity functions at z > 7
  (double power law), Bowler et al. 2020 at z = 5–6, all refitted as double
  power laws to keep the full parameter chains, since "treating their
  uncertainties as independent would overestimate the true uncertainty";
  cutoff −13, "the faintest bin reliably measured at these redshifts"; the
  emissivity function φ(Ṅ_ion,esc) is the luminosity function convolved
  with the measured distribution of ξ_ion f_esc (Eq. 5), sampled 10³ times
  between M_UV = −13 and −23 [src: arXiv:2607.22834, Sect. 4].
- Summerfield et al.: Bouwens et al. 2021 for z = 1.5–8.5 and Whitler et al.
  2025 for z = 8.5–16 in Schechter form, cutoff −13 (the completeness of
  their simulated catalogue, ~9 × 10⁵ M_⊙ in stellar mass) [src:
  arXiv:2606.14671, Sect. 4.1].

A relation fitted in log space must be converted to a linear mean before it
enters Eq. 3: ⟨Ṅ_ion,esc⟩ = 10^(½ ln10 σ²) Ṅ_ion,esc, with σ = 0.725 dex
taken from the simulated scatter [src: arXiv:2606.14671, Sect. 4.1, Eq. 8].
For σ = 0.725 the factor is 4.0 [der: 10^(0.5 × 2.303 × 0.526)].

### Step 6. Choose the sinks
<!-- key: step-6-choose-the-sinks -->

| Choice | Value | Reason given | Place read |
|---|---|---|---|
| Constant C | C = 3, α_B at T = 2 × 10⁴ K | "for simplicity and comparison with past literature"; nearly identical to the Shull et al. 2012 C(z) fit; simulations give C ≈ 2–5 | arXiv:2404.07250, Sect. 2 |
| Fitted C(z) | C = 9.25 − 7.21 log₁₀(1 + z) | calibrated on radiation-hydrodynamic runs (Finlator 2009, Chen 2020), as in Madau 2024 and Wu 2025 | arXiv:2606.14671, Sect. 4.3 |
| Bracket | C = 1, 3, 10 | uniform IGM up to many recombinations | arXiv:2409.01286, Sect. 6.1 |
| Observational C | C ≈ 12 at z = 5–6 (C ~ 10–15 over z = 2–6; ~17 at z = 6 with large error) | photoionisation equilibrium with the measured Γ_HI and λ_mfp | arXiv:2406.18186, Sect. III.2 |
| Physically defined IGM | C ~ 3 at z = 6 | IGM defined by the transmission of ionising photons; robust to resolution, box and definition | arXiv:2511.09364, abstract |

The observational estimate equates photoionisations and recombinations,
n_γ c/λ_mfp = C α_HII χ_e (1 − x_HI)² n_H², so C = n_γ c /[λ_mfp α_HII χ_e
(1 − x_HI)² n_H²], with n_γ the ionising-photon density, χ_e ≈ 1.08 for
singly ionised helium and α_HII the case-B value at 10⁴ K [src: Davies,
Bosman & Furlanetto 2024, arXiv:2406.18186, Sect. II, Eqs. 5, 12–13]. All
three variants derived there scale as C ∝ Γ_HI/λ_mfp; the authors adopt the
third "as it appears to have the fewest explicit assumptions". At C ≈ 12
galaxies must produce about 3 photons per baryon to finish by z ~ 6, about
twice the C = 3 requirement [src: arXiv:2406.18186, abstract]. The IGM
clumping factor of a simulation cannot be computed to better than ~20%
because the over-ionised proximity zones around galaxies make the IGM
boundary ambiguous [src: Kaurov & Gnedin 2015, arXiv:1412.5607, abstract].

### Step 7. Confront the result with the IGM
<!-- key: step-7-confront-the-result-with-the-igm -->

- τ. τ_CMB = ∫ dℓ n_e σ_T over proper distance with the proper electron
  density, He I ionised with H and He II at z = 4; Muñoz et al. use only τ as
  the constraint and check x_HI(z) afterwards [src: arXiv:2404.07250, Sect.
  3, Eq. 7 and footnote 3].
- Forest emissivity, the independent route at z ≲ 5. Γ_HI is obtained by
  matching τ_eff from simulated spectra, 1000 sightlines per output, to the
  observed τ_eff at the measured temperature, for a chosen slope γ of the
  temperature–density relation (τ ∝ (1 + z)⁶ (Ω_b h²)² T^−0.7 H⁻¹ Γ⁻¹ Δ^β,
  β = 2 − 0.7(γ − 1)); γ = 1.4 is fiducial with 1.2 and 1.6 as bounds [src:
  Becker & Bolton 2013, arXiv:1307.2259, Sect. 4.1, Eq. 2]. The emissivity
  follows from Γ through the cosmological radiative-transfer integral J(ν₀,
  z₀) = (1/4π) ∫ dz (dl/dz) (1 + z₀)³/(1 + z)³ ε(ν, z) e^−τ_eff (Eq. 3), with
  the opacity from a power-law column-density distribution fitted jointly to
  λ₉₁₂ and the Lyman-limit-system counts (Eq. 5; A = 0.93, β_N = 1.33, β_z =
  1.92) [src: arXiv:1307.2259, Sect. 5.1]. At z = 4.75 the result is 2 to 14
  ionising photons per atom per Gyr [src: arXiv:1307.2259, Sect. 7.3]. After
  reionisation the volume emissivity flattens at log(Ṅ_ion/s⁻¹ Mpc⁻³) ~ 50.8
  at z ≲ 5–6 [src: arXiv:2409.01286, Sect. 6.1].
- Reionisation history. Summerfield et al. compare Q_HII(z) with CMB,
  damping-wing, Lyα-emission and dark-pixel constraints and find completion
  at z_f = 5.5 ± 0.2 (simulation relation) and 5.6 ± 0.3 (JWST relation), with
  Q_HII(z = 8) ≤ 0.2; AGN are neglected [src: arXiv:2606.14671, Sect. 4.3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Which ξ_ion sample
<!-- key: which-xiion-sample -->

An emission-line-selected sample "could bias the sample towards strong line
emitters (and thus high ξ_ion) at fixed UV magnitude"; with ξ_ion fixed at
10^25.5 Hz erg⁻¹ (the lowest mean of a sample without line selection) the
budget still needs a cutoff at M_UV ≈ −14 or brighter [src: arXiv:2404.07250,
Sect. 4]. The tension Muñoz et al. find comes from the JWST relation log ξ_ion
≈ 25.8 + 0.11(M_UV + 17) + 0.05(z − 7), capped at M_UV = −16.5, against the
pre-JWST 25.2; with it, reionisation would start by z ~ 12, end by z ~ 8 and
give τ ≈ 0.08, against τ ≈ 0.055 for the pre-JWST model [src: arXiv:2404.07250,
Sect. 2, Eq. 4]. A stellar-mass-complete sample "leads to a milder ξ_ion
evolution with M_UV", which reduces the weight of faint galaxies; since its
ξ_ion,0 carries the factor (1 − f_esc), the resulting Ṅ_ion are lower limits,
by < 0.1 dex for the sample's mean f_esc ~ 3% [src: arXiv:2409.01286, Sect.
6.1]. A spectroscopic sample with confident redshifts may in turn favour
strong line emitters [src: arXiv:2607.22834, Sect. 6].

### Hα or the SED integral
<!-- key: halpha-or-the-sed-integral -->

Hα counts the photons that do not escape; the SED integral counts those that
do. Compared on the intrinsic rate, Hα is lower by a median 0.05 dex; the
paper attributes this to the Leitherer & Heckman models (IMF to 100 M_⊙, no
binaries) against BPASS (to 300 M_⊙, binaries), and the high outliers to
broad Hα, possibly AGN or little red dots, which no AGN template fits [src:
arXiv:2607.22834, Sect. 2.5]. A conversion coefficient is therefore tied to
the population-synthesis model it came from.

### Which f_esc prescription
<!-- key: which-fesc-prescription -->

- Constant f_esc makes the history depend strongly on the faint-end cutoff;
  with the simulation-calibrated Ṅ_ion,esc–M_UV relation, moving the cutoff
  by ± 3 mag about −13 shifts the end of reionisation by < 0.1 in z. Budgets
  with constant f_esc and a bright cutoff "should be interpreted as lower
  limits" [src: arXiv:2606.14671, Sect. 4.5].
- The β_UV relation needs "little to no extrapolation" to overproduce
  photons; reaching τ with a cutoff at −11 needs ⟨f_esc⟩ ≈ 3%, which the LzLCS
  relation would only give for β_UV ≈ −1.93, redder than observed at z > 5
  [src: arXiv:2404.07250, Sect. 4]. Two ways out named there: a lower f_esc at
  fixed β at high z (more neutral gas, less dust per gas), or an
  anti-correlation of f_esc with ξ_ion.
- Spectral fitting gives f_esc per object and makes the distribution of
  ξ_ion f_esc bimodal (a main cloud of weak leakers and a second cloud of
  strong leakers), with no M_UV dependence; sources with f_esc > 10%, about
  20% of the sample, give about 87% of the photons [src: arXiv:2607.22834,
  Sects. 4 and 5.1]. Its cost: SFH–f_esc degeneracy and population-synthesis
  assumptions (below).
- Random forests give Ṅ_ion,esc with less scatter than f_esc, which the
  authors read as "Ṅ_ion,esc may therefore be a more reliable quantity for
  reionization modelling"; they cannot predict log f_esc > −0.5, a limit of
  averaging trees [src: arXiv:2606.14671, Sect. 3.3].

### Which luminosity-function form
<!-- key: which-luminosity-function-form -->

Giovinazzo et al. refit every luminosity function as a double power law,
because Schechter fits underestimate bright galaxies at high z [src:
arXiv:2607.22834, Sect. 4]. Summerfield et al. compared Schechter and double
power-law forms and a stellar-mass function in an appendix and kept Schechter
as "most suitable for this work" [src: arXiv:2606.14671, Sect. 4.1]. A
flattening faint end (Finkelstein & Bagley 2022) does not remove the Muñoz
tension, because it needs no extrapolation beyond M_UV ≈ −15, where faint-end
uncertainties change abundances by ~30% [src: arXiv:2404.07250, Sect. 4].

### Which clumping factor
<!-- key: which-clumping-factor -->

C = 3 against C ≈ 12 is a factor two in the photons needed [src:
arXiv:2406.18186, abstract], but C = 20 still overproduces reionisation by
more than 3σ in τ once JWST ξ_ion is used, and such numbers of recombinations
"are not standard in ΛCDM cosmologies" [src: arXiv:2404.07250, Sect. 4]. The
observational C assumes local photoionisation equilibrium, which fails at
z ≲ 4 where the mean free path is long; this is the likely cause of its upturn
at z < 3 [src: arXiv:2406.18186, Sect. III.2]. The simulation-based value
depends on how the IGM is defined; a transmission-based definition gives C ~ 3
at z = 6, within a factor two of overdensity-threshold definitions [src:
arXiv:2511.09364, abstract].

### How the four routes compare
<!-- key: how-the-four-routes-compare -->

| Analysis | ξ_ion | f_esc | LF and cutoff | C | Outcome | Place read |
|---|---|---|---|---|---|---|
| Muñoz et al. 2024 | JWST relation (Eq. 4) | β_UV relation, capped | Bouwens 2021 + Donnan 2024; free cutoff ≤ −15 | 3 | no overlap of τ, f_esc and cutoff constraints | arXiv:2404.07250, Sect. 3 |
| Simmonds et al. 2024 | Prospector, mass-complete, star-forming | constant 10–20%, M_UV, β, Σ_SFR | Bouwens 2021 to −16; mass function to 10^7.5 M_⊙ | 1, 3, 10 | consistent with the literature; the β relation matches the forest shape | arXiv:2409.01286, Sect. 6.1 |
| Giovinazzo et al. 2026 | SED integral | picket-fence fit per object | GLIMPSE DPL to −13 | — | end at z ~ 5.8 (L2); strong leakers dominate | arXiv:2607.22834, Sects. 4–5 |
| Summerfield et al. 2026 | (enters through Ṅ_ion,esc) | random forest on THESAN-ZOOM | Bouwens 2021 + Whitler 2025 to −13 | C(z) fit | z_f = 5.5–5.6, no crisis | arXiv:2606.14671, Sect. 4.3 |

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Pre-JWST ξ_ion | log ξ_ion = 25.2 Hz erg⁻¹, f_esc = 20%, cutoff ≈ −13: τ ≈ 0.055, end z ~ 6 | Robertson 2013 model as used by Muñoz | arXiv:2404.07250 | Sect. 2 |
| Pre-JWST overlap | f_esc ≈ 15–30% for cutoffs fainter than −15 | Muñoz et al. | arXiv:2404.07250 | Sect. 3 |
| Cutoff that removes the tension | M_UV^cut = −17 with f_esc = 15%; or −11 with 3% | Muñoz et al. | arXiv:2404.07250 | Sect. 4, Fig. 3 caption |
| H α conversion | ṅ_ion = 7.28 × 10¹¹ L(Hα) | case B, f_esc = 0 | arXiv:2409.01286 | Sect. 5.1 |
| Leitherer & Heckman conversion | L(Hα) = 1.36 × 10⁻¹² N(H⁰) erg s⁻¹ | — | arXiv:2607.22834 | Sect. 2.3, Eq. 2 |
| Hα vs SED intrinsic rate | median offset 0.05 dex (Hα lower) | NIRSpec prism | arXiv:2607.22834 | Sect. 2.5 |
| f_esc distribution | approximately exponential, mean 10% | NIRSpec prism | arXiv:2607.22834 | Sect. 2.3 |
| f_esc recovery | robust for high f_esc at all S/N; at S/N = 3 all inputs < 30% are consistent with 0; Bayes factor > 100 as the confidence threshold | injection on bagpipes models through the JWST ETC, S/N 3, 5, 10, 20 | arXiv:2507.01096 | Sect. 4 |
| Lognormal mean correction | σ = 0.725 dex → factor 4.0 [der] | THESAN-ZOOM | arXiv:2606.14671 | Sect. 4.1, Eq. 8 |
| Clumping fit | C = 9.25 − 7.21 log₁₀(1 + z) | Madau 2024 / Wu 2025 model | arXiv:2606.14671 | Sect. 4.3 |
| Observational C | ≈ 12 (z = 5–6); ≈ 3 photons per baryon | Γ_HI and λ_mfp | arXiv:2406.18186 | Sect. III.2; abstract |
| Forest Γ_HI error budget | statistical ± 0.04–0.07 dex; γ = 1.2–1.6 gives ± 0.06–0.09 dex | z = 2.4–4.75 | arXiv:1307.2259 | Table 1 |
| Local-source approximation | underestimates the emissivity by up to a factor 2 at z ~ 2 | — | arXiv:1307.2259 | Sect. 5.1 |
| Emissivity at z = 4.75 | 2–14 photons per atom per Gyr | forest | arXiv:1307.2259 | Sect. 7.3 |
| Spectral index of the sources | α from 2 to 3: ε₉₁₂ +0.11–0.13 dex, Ṅ_ion −0.05–0.07 dex | forest | arXiv:1307.2259 | Sect. 5.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- Degeneracy of ξ_ion and f_esc. Only the product enters; a Balmer-line ξ_ion
  assumes f_esc = 0 and is therefore biased low by (1 − f_esc), which is
  negligible for weak leakers and not for strong ones [src: arXiv:2409.01286,
  Sect. 5.1; arXiv:2607.22834, Sect. 2.3]. Test: state which of ξ_ion,0 or
  ξ_ion enters.
- SFH mimicking leakage. A recently quenched galaxy (star formation within
  100 Myr, O stars gone, B stars present) has a steep β_UV and weak Balmer
  lines, as a leaker does. The fit marginalises the SFH jointly with f_esc,
  and none of the high-confidence leakers shows a Balmer break; the authors
  still call for fits of objects with directly measured f_esc [src:
  arXiv:2507.01096, Sect. 7.2; arXiv:2607.22834, Sect. 6].
- Extrapolation in M_UV. Giovinazzo et al. apply a ξ_ion f_esc distribution
  measured brighter than M_UV = −18 down to −13, which they name as possibly
  "the biggest caveat"; GLIMPSE is one lensed pointing and subject to cosmic
  variance [src: arXiv:2607.22834, Sects. 4 and 6].
- Log-space fits used as linear means. Without the lognormal factor of Step 5
  the emissivity is biased low; the history moves significantly with the
  assumed scatter [src: arXiv:2606.14671, Sects. 4.1 and 4.5].
- Calibration extrapolated beyond its range. The β_UV relation is calibrated
  to β = −2.7 and is implicitly extrapolated in z and M_UV [src:
  arXiv:2404.07250, Sect. 2]. JWST β_UV of galaxies fainter than M_UV = −16
  is now being measured in lensing fields [src: Jecmen et al. 2026,
  arXiv:2601.19995, abstract].
- Wrong balance equation. The static criterion predicts the wrong completion
  epoch; the volume-filling form biases τ by > 20% in a simulation test [src:
  arXiv:1311.2152; arXiv:2004.07854, abstracts].
- AGN left out. The simulation-calibrated budget neglects them [src:
  arXiv:2606.14671, Sect. 4.3]; broad-line objects distort Hα-based ξ_ion
  [src: arXiv:2607.22834, Sect. 2.5].

Checks the papers apply: the predicted τ against Planck, x_HI(z) against
damping-wing, dark-pixel and Lyα data not used in the fit, and the post-
reionisation emissivity against the forest value [src: arXiv:2404.07250,
Sect. 3; arXiv:2606.14671, Sect. 4.3; arXiv:2409.01286, Sect. 6.1]. Muñoz et
al. note that a bright cutoff makes reionisation faster and a low f_esc makes
it slower, so x_HI(z) and 21 cm bubble clustering can separate solutions
that give the same τ [src: arXiv:2404.07250, Sect. 4].

## Reading list
<!-- key: reading-list -->

- Foundation: Madau, Haardt & Rees 1999, arXiv:astro-ph/9809058 — the
  balance equation and the clumping criterion.
- Method: Becker & Bolton 2013, arXiv:1307.2259 — Γ_HI from τ_eff and the
  emissivity with cosmological radiative transfer; the error budget.
- Method: Davies, Bosman & Furlanetto 2024, arXiv:2406.18186 — clumping
  factor from Γ_HI and λ_mfp.
- Critique: So et al. 2014, arXiv:1311.2152 — when the static and
  time-dependent balance equations fail.
- Application: Muñoz et al. 2024, arXiv:2404.07250 — the budget with JWST
  ξ_ion and β-based f_esc; the "possible outs".
- Application: Simmonds et al. 2024, arXiv:2409.01286 — ξ_ion of a
  mass-complete sample; several f_esc prescriptions side by side.
- Method: Giovinazzo et al. 2025, arXiv:2507.01096 — picket-fence f_esc
  fit and its recovery test.
- Application: Giovinazzo et al. 2026, arXiv:2607.22834 — the emissivity
  function from per-object escaping rates.
- Critique: Summerfield et al. 2026, arXiv:2606.14671 — learned indicators,
  cutoff and scatter sensitivity of the history.

## Not verified
<!-- key: not-verified -->

- Chisholm et al. 2022 (LzLCS β–f_esc relation), Naidu et al. 2020, Anderson
  et al. 2017, Atek et al. 2024 and the GLIMPSE luminosity-function papers
  are used through the papers above; their bodies and identifiers were not
  read.
- Kaurov & Gnedin 2015, So et al. 2014, Chen et al. 2020 and Oku & Cen 2025
  were read as abstracts only.
- The Γ_HI measurements at z > 5 (Davies et al., cited by arXiv:2406.18186)
  and the emissivity curves of Gaikwad et al. 2023 were not read here.
- The AGN contribution to the budget was not researched.
- The redshift of completion in Giovinazzo et al. (z ~ 5.8) is taken from
  L2; its section 5.2 was not read.
