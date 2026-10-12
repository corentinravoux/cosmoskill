# Physics and methods — neutrino mass, light relics and dark-matter properties from structure

Scope: what cosmological data measure about neutrinos, light relics and the particle nature of dark matter; the defining relations, parameterisations, statistical practice and codes in current use.
Snapshot: 2026-10-07

Flags: `[src]` read in the cited paper this session; `[sec]` taken from a named secondary source; `[der]` derived here. Equations without a flag are textbook definitions.

The data side of each probe lives in a sibling skill: CMB spectra, lensing and τ in `cosmo-cmb`; BAO and full shape in `cosmo-galaxy-clustering`; the Lyα forest in `cosmo-lyman-alpha`. This file holds the particle-physics interpretation and the small-scale-structure probes that have no other home.

## 1. Massive neutrinos

### 1.1 Background relations

The relations below are written as in Elbers et al. 2025 (arXiv:2503.14744 §3), the DESI DR2 neutrino paper. The standard review is Lesgourgues & Pastor 2006 (arXiv:astro-ph/0603494).

- Neutrinos decouple at a temperature of about 1 MeV and keep a thermal phase-space distribution.
- A neutrino of mass m_ν becomes non-relativistic at z_nr ≈ 1890 (m_ν / eV) [src]. Any eigenstate lighter than about 0.58 eV is therefore still relativistic at recombination [der: 1090/1890, taking z* ≈ 1090], which is why the primary CMB is nearly blind to Σm_ν in the range now allowed.
- Relativistic limit: ρ_ν = N_eff (7π²/120) T_ν,0⁴ (1+z)⁴. This defines N_eff.
- Non-relativistic limit: Ω_ν h² = Σm_ν / 93.14 eV [src]. The denominator depends on the assumed neutrino temperature and spectral distortions; check it before comparing ω_ν values across codes.
- f_ν ≡ Ω_ν / Ω_m.

Neutrinos count as radiation when the sound horizon r_d is set and as matter when BAO are measured. That mismatch, not free streaming, is what BAO + CMB constrain.

### 1.2 The three channels

| Channel | What is measured | Why it sees Σm_ν | Main degeneracy |
|---|---|---|---|
| Geometry | BAO D_M/r_d, D_H/r_d with CMB θ*, ω_b, ω_cdm | Ω_m = Ω_cb + Ω_ν from BAO; ω_cb from CMB peak heights; the difference is Ω_ν | late-time expansion history (dark energy, curvature); H0 r_d |
| CMB lensing | peak smoothing in TT/TE/EE and the reconstructed C_L^κκ | suppressed growth lowers the lensing amplitude relative to A_s | τ through A_s e^(−2τ); the A_lens excess in some Planck likelihoods |
| Galaxy clustering shape | P(k) and bispectrum multipoles | scale-dependent suppression of the matter power spectrum | bias and counterterm priors; A_s, n_s |

Statements that need care:

- BAO alone do not constrain Σm_ν at all; adding a BBN prior and θ* tightens Ω_m only. The constraint appears when CMB information on ω_b and ω_cdm calibrates r_d and separates Ω_cb from Ω_ν (arXiv:2503.14744 §3.1).
- The small-scale suppression of the linear matter power spectrum is ΔP_m/P_m ≈ −8 f_ν, with the exact coefficient depending on which parameters are held fixed [sec: arXiv:2503.14744 §3.2, which attributes it to Hu, Eisenstein & Tegmark 1997, arXiv:astro-ph/9712057]. The 1997 abstract states that eV-mass neutrinos suppress power "by a factor of two" [src].
- Lensing observables are dimensionless and respond to the matter fraction Ω_m, not the physical density; within ΛCDM the primary CMB alone forces the matter fraction to rise steeply with neutrino mass (Loverde & Weiner 2024, arXiv:2410.00090). Their conclusion is that the geometric channel is at least as constraining as the suppression of structure in current data.
- In the DESI DR2 analysis, adding CMB lensing to DR1 BAO + CMB improves the profile-likelihood width σ by 0.023 eV but also moves the minimum towards positive values by 0.020 eV; adding the DR1 full shape changes σ by only 0.003 eV and lowers the limit mostly through a shift towards negative values (arXiv:2503.14744 §5.1 [src]). An "improved limit" can therefore come from a shift, not from information.
- Other CMB effects of Σm_ν without lensing reconstruction are the integrated Sachs–Wolfe effect, the lensing-induced smoothing of the peaks and the damping tail; the smoothing is the strongest (arXiv:2503.14744 §3.1).

### 1.3 Parameterisations of the mass spectrum

| Name | Definition | Used by | Consequence |
|---|---|---|---|
| Degenerate | three states of mass Σm_ν/3, prior Σm_ν > 0 | DESI baseline, ACT, SPT | posterior piles up at zero |
| Degenerate with a floor | same, prior Σm_ν ≥ 0.059 eV (NO) or ≥ 0.10 eV (IO) | DESI DR1 | limit rises to 0.105 / 0.135 eV for DR2 [src] |
| Lightest mass + splittings | NO: Σ = m_1 + √(m_1² + Δm²_21) + √(m_1² + Δm²_31); IO: Σ = m_3 + √(m_3² − Δm²_31) + √(m_3² − Δm²_32) | DESI DR2 with NuFIT 6.0 | 0.101 / 0.133 eV; within 0.004 eV of the floor approximation [src] |
| Effective signed mass | see §1.4 | Craig et al., Elbers et al., DESI DR2, Cozzumbo et al. | removes the boundary |

All numbers in the fourth column are from arXiv:2503.14744 §4.3. When Σm_ν is not varied, DESI fixes Σm_ν = 0.06 eV and N_eff = 3.044 (arXiv:2503.14744 Table 2 caption [src]); ACT fixes 0.06 eV "carried by a single massive species" as its baseline and uses three massive species when the mass is varied (arXiv:2503.14454 §6.1.1 [src]). The oscillation-based prior is strongly non-linear in the heavier masses; a prior linear in all three masses is an alternative that the DESI paper names and that changes Bayes factors (see `open-questions.md` §1.4).

### 1.4 Effective ("negative") neutrino mass: three different parameters

These are not the same quantity and their central values must not be compared directly.

1. **Clustering-only extension** (Craig et al. 2024, arXiv:2405.00836): the suppression of clustering is allowed to become an enhancement. Result on DESI DR1 + CMB: −160 ± 90 meV.
2. **Consistent extension** (Elbers et al. 2024, arXiv:2407.10965; adopted in arXiv:2503.14744): a negative neutrino contribution to the energy density at late times, implemented in linear perturbation theory so that every effect of Σm_ν extends to negative values; identical to Σm_ν for positive values. Result on DESI DR2 + CMB: −0.101 (+0.047/−0.056) eV.
3. **Effective mass with lensing nuisance parameters** (Cozzumbo et al. 2025, arXiv:2511.01967): a signed mass varied together with one parameter for peak smoothing and one for the lensing-potential amplitude. Result: −0.018 (+0.085/−0.089) eV.

The DESI paper states that evidence for negative values is to be read as unidentified systematics or as new physics possibly unrelated to neutrinos, not as negative-mass neutrinos (arXiv:2503.14744 §5.2). Graham, Green & Meyers 2025 (arXiv:2508.20999) separate two meanings of "negative mass": one describing the change in expansion history, the other describing enhanced lensing.

### 1.5 Statistical practice

- **Bayesian with a positivity prior.** Standard for collaboration limits. The quoted σ(Σm_ν) = 0.020 eV for DESI DR2 + CMB is a property of the truncated posterior.
- **Profile likelihood with Feldman–Cousins.** The profile in Σm_ν ≥ 0 is close to parabolic; it is extrapolated to a full parabola with minimum μ0 and width σ, and a 95% limit is built with the Feldman–Cousins prescription. DESI DR2 + CMB: μ0 = −0.036 eV, σ = 0.043 eV, limit 0.053 eV (arXiv:2503.14744 Table 3 [src]). The minimisation uses iminuit with 14 free parameters for BAO + CMB and 44 with the full shape.
- **Agreement between the two.** Naredo-Tuero et al. 2024 (arXiv:2407.13831) find profile-likelihood and Bayesian limits within about 10%. In DESI DR2 the Feldman–Cousins limit is 0.01 eV lower than the Bayesian one in ΛCDM and 0.01 eV higher in w0waCDM.
- **Three widths for one data set.** 0.020 eV (Bayesian, truncated), 0.043 eV (profile parabola), 0.053 eV (effective-mass posterior). Only the last two measure sensitivity.
- **Tension metrics.** The tension with oscillations is quoted as 3σ from the effective-mass posterior (arXiv:2503.14744) and as 2.5–5σ depending on metric and data (Jiang et al. 2024, arXiv:2407.18047). State the metric.
- **Model comparison for the ordering.** Bayes factor between NO and IO with equal prior odds and a stated mass prior; the frequentist counterpart is Δχ² between the two minimum-mass points.
- **Validation.** The DESI neutrino analysis includes a validation on mocks (arXiv:2503.14744 §2.8, section title read only).

### 1.6 Free-streaming signatures that are independent of the expansion rate

- **Phase shift.** Free-streaming radiation travels faster than the sound speed of the plasma and shifts the phase of the acoustic oscillations; for adiabatic initial conditions no other standard parameter produces this (Bashinsky & Seljak 2003, arXiv:astro-ph/0310198). In BAO it is parameterised by an amplitude β_φ, equal to 1 for N_eff = 3.044 and 0 for no free-streaming species (arXiv:2503.14744 §4.2).
- **Self-interacting neutrinos.** Delaying the onset of free streaming removes the phase shift; other parameters can compensate in the CMB (Kreisch, Cyr-Racine & Doré 2019, arXiv:1902.00534), which is why a phase-shift detection is model-dependent.

## 2. N_eff and light relics

- Standard-Model value: 3.044 (Froustey, Pitrou & Volpe 2020, arXiv:2008.01074 gives 3.0440; QED corrections in Bennett et al. 2019, arXiv:1911.04504).
- What the CMB measures: the expansion rate before recombination through the damping tail relative to the acoustic scale, and the phase shift. The first is degenerate with the primordial helium fraction (arXiv:astro-ph/0310198); analyses either impose BBN consistency for Y_P or free it.
- **Free-streaming versus fluid radiation.** N_eff in tables is free-streaming radiation. Self-interacting (fluid) dark radiation produces no phase shift and is constrained separately as N_idr (arXiv:2503.14454: N_idr < 0.134).
- **Model dependence of ΔN_eff limits.** The ACT limit assumes a power-law primordial spectrum; freeing the running and its running relaxes the limit on self-interacting dark radiation to ΔN_eff < 0.58 (Garny, Niedermann & Sloth 2026, arXiv:2604.26541).
- **Stepped or decoupling dark radiation.** Wess–Zumino dark radiation changes its energy density when a mediator becomes non-relativistic; ACT DR6 closes most of the parameter space in which it raised H0 (Cvetko, Joseph & Marques-Tavares 2025, arXiv:2512.19633).
- **BBN.** Light-element abundances measure the expansion rate at about one second through N_ν and the baryon density through D/H. The helium prediction depends mainly on the weak rates and the neutron lifetime; the baryon density inferred from D/H depends on the deuterium-burning rates (Pitrou et al. 2018, arXiv:1801.08023; Schöneberg 2024, arXiv:2401.15054). BBN and the CMB probe the radiation density at different epochs, so a difference between them is itself a constraint (Yeh et al. 2022, arXiv:2207.13133).
- Convention: BBN papers quote N_ν with baseline 3; CMB papers quote N_eff with baseline 3.044. The stated difference is N_eff − 3 = 0.044 (arXiv:2207.13133).

## 3. Dark-matter properties from small-scale structure

### 3.1 What is constrained

All of the models below are tested through one of two effects: a cutoff in the linear matter power spectrum (fewer low-mass haloes), or a change in the internal structure of haloes.

| Model | Parameter | Linear-theory effect | Halo-scale effect |
|---|---|---|---|
| Warm (thermal relic) | m_WDM in keV | free-streaming cutoff | fewer subhaloes, lower concentrations (Bode, Ostriker & Turok 2000, arXiv:astro-ph/0010389) |
| Fuzzy / ultralight | boson mass in eV | cutoff from the de Broglie scale, about 1 kpc at 10⁻²² eV | soliton core, interference granules; haloes below about 10⁷ (m/10⁻²² eV)^(−3/2) M⊙ do not form (Hui et al. 2016, arXiv:1610.08297 [src]) |
| Ultralight sub-component | Ω_a or fraction, mass | scale-dependent suppression of growth | — |
| Scattering with baryons | σ0, index n in σ ∝ vⁿ, mass | collisional damping | — |
| Scattering with neutrinos or dark radiation | u_νχ; ETHOS parameters | damping and dark acoustic oscillations (Cyr-Racine et al. 2015, arXiv:1512.05344) | — |
| Self-interacting | σ/m at a stated velocity | none for elastic scattering | cores, then gravothermal core collapse; offsets in mergers (Spergel & Steinhardt 1999, arXiv:astro-ph/9909386) |
| Decaying | lifetime, fraction, kick velocity | late-time loss of matter or of small-scale power | — |

### 3.2 Half-mode scale and the keV conversion

Limits are derived on the half-mode mass M_hm (or wavelength λ_hm) and then converted to a thermal-relic mass. Pairs read this session:

| M_hm | m_WDM | Source | Flag |
|---|---|---|---|
| 10^7.8 M⊙ | 5.2 keV | Gilman et al. 2019, arXiv:1908.06983 | [src] |
| 10^7.8 M⊙ | 5.6 keV | Keeley et al. 2025, arXiv:2511.07765 | [src] |
| 10^7.6 M⊙ | 6.4 keV | arXiv:2511.07765 | [src] |
| 10^7.4 M⊙ | 6.5 keV | Gilman et al. 2025, arXiv:2511.07513 | [src] |
| 10^7.4 M⊙ | 7.4 keV | Nadler et al. 2021, arXiv:2101.07810 | [src] |
| 10^7.2 M⊙ | 7.4 keV | arXiv:2511.07513 | [src] |
| 10^7.0 M⊙ | 9.7 keV | arXiv:2101.07810 | [src] |
| 3 × 10⁷ M⊙/h (λ_hm = 0.089 Mpc/h) | 6.048 keV | Enzi et al. 2020, arXiv:2010.13802 | [src] |

The same half-mode mass maps to different keV values in different papers (10^7.8 M⊙ gives 5.2 or 5.6 keV; 10^7.4 M⊙ gives 6.5 or 7.4 keV). The conversion depends on the adopted transfer-function fit, cosmology and unit convention (M⊙ or M⊙/h). Compare limits in M_hm, or re-derive the mass with one relation.

A thermal-relic limit does not transfer to other models by matching the half-mode scale: for dark matter–neutrino scattering this mapping overestimates the constraint relative to dedicated simulations (Mosbech et al. 2026, arXiv:2607.15020). For ultralight fields produced with a field power spectrum peaked at a subhorizon wavenumber k*, the field free-streams like warm dark matter and the mass limit scales with k* (Nadler et al. 2026, arXiv:2605.15371).

### 3.3 The probes

| Probe | Observable | Scales | What must be modelled |
|---|---|---|---|
| Lyα forest P1D at z ≳ 4 | flux power to k ≈ 0.1–0.2 s/km | cutoff in the 1D flux power | thermal history, reionisation, peculiar-velocity smearing; data and emulators in `cosmo-lyman-alpha` |
| Milky Way satellites | luminosity function with survey selection | haloes hosting the faintest galaxies | galaxy–halo connection, Milky Way mass, subhalo disruption by the disk (Nadler et al. 2020, arXiv:2008.00022) |
| Strong lensing, flux ratios | relative magnifications of quad images | haloes down to 10⁶ M⊙ in the lens and along the line of sight | macromodel including m = 1, 3, 4 multipoles, source size, tidal stripping, globular clusters, subhalo-abundance prior (arXiv:2511.07765) |
| Strong lensing, extended arcs | surface-brightness perturbations | individual subhaloes; granules for fuzzy dark matter | source reconstruction, smooth-lens model (Powell et al. 2023, arXiv:2302.10941) |
| Stellar streams | density variations along GD-1, Pal 5 | subhaloes below the dwarf-galaxy scale | slope and normalisation of the subhalo mass function, tidal disruption in the inner Galaxy (Banik et al. 2019, arXiv:1911.02663) |
| Ultraviolet luminosity functions | faint-end abundance at z ≈ 4–14 | delayed formation of low-mass haloes | star-formation efficiency, magnitude–halo-mass scatter (Liu, Shan & Zhang 2024, arXiv:2404.13596) |
| Dwarf-galaxy kinematics | sizes and velocity dispersions | granule heating; core structure | soliton–halo relation, other heating sources (Dalal & Kravtsov 2022, arXiv:2203.05750) |
| Cluster mergers and profiles | dark matter–galaxy offsets; central densities | σ/m at relative velocities above 1000 km/s | how centroids are measured, gas stripping, adiabatic contraction (Robertson, Massey & Eke 2016, arXiv:1605.04307) |
| CMB and galaxy power spectra | TT/TE/EE, lensing, P(k) | sub-component axions, scattering, decays | non-linear model for the non-cold component (Rogers et al. 2023, arXiv:2301.08361) |

### 3.4 Self-interactions

The quantity is the cross section per unit mass σ/m in cm²/g at a characteristic relative velocity, which rises from dwarfs to clusters. Reviews: Tulin & Yu 2017 (arXiv:1705.02358), Adhikari et al. 2022 (arXiv:2207.10638). Velocity-dependent models are written with a normalisation σ0 and a velocity scale ω (as in Jia et al. 2026, arXiv:2601.17118). Haloes first form an isothermal core and can later undergo gravothermal core collapse, so one rotation curve can admit a core-growth and a core-collapse solution.

### 3.5 Decays

Two models are in use (Simon et al. 2022, arXiv:2203.07440): a fraction f of the dark matter decaying to dark radiation with lifetime τ, constrained mainly by the CMB; and all of the dark matter decaying to dark radiation plus a massive warm daughter, with a fraction ε of the rest-mass energy going to radiation, proposed as a way to lower S8. The Boltzmann hierarchy for the first is derived in Poulin, Serpico & Lesgourgues 2016 (arXiv:1606.02073).

## 4. Codes named in the analyses read this session

| Code | Use | Reference | Flag |
|---|---|---|---|
| CLASS, non-cold relics module | massive neutrinos, warm dark matter and arbitrary phase-space distributions in a Boltzmann code | Lesgourgues & Tram 2011, arXiv:1104.2935 | [src] |
| PRIMAT | BBN network with weak-rate corrections | arXiv:1801.08023 | [src] |
| PRyMordial | BBN with marginalisation over nuclear rates | named in arXiv:2401.15054; reference paper not fetched | [sec] |
| Cholla | GPU hydrodynamics for the 1080-simulation warm-dark-matter grid | used in arXiv:2209.14220; reference not fetched | [sec] |
| Galacticus | semi-analytic subhalo populations for lensing and satellite analyses | used in arXiv:2101.07810, arXiv:2511.07513; reference not fetched | [sec] |
| GALLUMI with CLASS DMeff | ultraviolet luminosity functions with interacting dark matter | used in arXiv:2510.10757; references not fetched | [sec] |
| ETHOS | mapping of dark-sector microphysics to linear-power and self-interaction parameters | arXiv:1512.05344 | [src] |
| iminuit | profile likelihoods | used in arXiv:2503.14744 | [sec] |

`cosmo-software-ecosystem` holds the general Boltzmann (CAMB), sampler (Cobaya) and emulator (EuclidEmulator2) references, and the fuzzy-dark-matter simulation codes; they are not repeated here.

## 5. Conventions and where the community is split

- **Limit level.** Neutrino-mass limits are 95%; KATRIN quotes 90% CL; lensing papers quote Bayes-factor 10:1 or posterior-odds 20:1 bounds next to 95% limits. Liu, Gong & Liao 2025 (arXiv:2512.01361) give both: 6.20 keV at 95% and 5.75 keV at 20:1.
- **Units.** Σm_ν in eV or meV; warm-dark-matter mass in keV for a thermal relic; fuzzy-dark-matter mass in eV; Lyα wavenumbers in s/km; σ/m in cm²/g; dark matter–proton cross sections in cm².
- **Thermal relic versus sterile neutrino.** The same data give 0.55 keV for a thermal relic and 2.0 keV for a sterile neutrino (Viel et al. 2005, arXiv:astro-ph/0501562). State the production mechanism.
- **Bayesian versus frequentist.** Split on neutrino mass (§1.5) and on decaying dark matter, where the two give strongly different 68% regions (Montandon et al. 2025, arXiv:2505.20193).
- **Collaboration result versus external reanalysis.** The tightest Σm_ν numbers (0.049 eV in ΛCDM, 0.077 eV in w0waCDM) come from an external EFT reanalysis of DESI DR1 with bispectrum and cross-correlations (Ivanov et al. 2026, arXiv:2601.16165), not from the DESI Collaboration.
- **Blinding.** The CMB and BAO inputs are blinded by their collaborations (see `cosmo-cmb`, `cosmo-galaxy-clustering`). No blinding statement was read this session for any of the small-scale dark-matter analyses listed in §3.3.

## Not verified

- The numerical form of the warm-dark-matter transfer function and of the half-mode-mass to keV relation was not read at source; only the paired values in §3.2 were.
- The fuzzy-dark-matter Jeans scale formula was not read at source.
- Whether the DESI baseline puts the fixed 0.06 eV in one massive state or in three degenerate states was not re-read this session (ACT: one state, §1.3).
- References for PRyMordial, Cholla, Galacticus, GALLUMI and CLASS DMeff were not fetched.
