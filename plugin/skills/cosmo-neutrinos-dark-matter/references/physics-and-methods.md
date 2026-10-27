# Physics and methods — neutrino mass, light relics and dark-matter properties from structure

Scope: what cosmological data measure about neutrinos, light relics and the particle nature of dark matter; the defining relations, parameterisations, statistical practice and codes in current use.
Snapshot: 2026-10-14

Flags: `[src]` read in the cited paper this session; `[sec]` taken from a named secondary source; `[der]` derived here. Equations without a flag are textbook definitions.

The data side of each probe lives in a sibling skill: CMB spectra, lensing and τ in `cosmo-cmb`; BAO and full shape in `cosmo-galaxy-clustering`; the Lyα forest in `cosmo-lyman-alpha`. This file holds the particle-physics interpretation and the small-scale-structure probes that have no other home.

## 1. Massive neutrinos
<!-- key: massive-neutrinos -->

### 1.1 Background relations
<!-- key: background-relations -->

The relations below are written as in Elbers et al. 2025 (arXiv:2503.14744 Sect. 3), the DESI DR2 neutrino paper. The standard review is Lesgourgues & Pastor 2006 (arXiv:astro-ph/0603494).

- Neutrinos decouple at a temperature of about 1 MeV and keep a thermal phase-space distribution.
- A neutrino of mass m_ν becomes non-relativistic at z_nr ≈ 1890 (m_ν / eV) (arXiv:2503.14744 [src: Sect. III]).
- An eigenstate whose z_nr falls below the redshift of recombination is still relativistic at recombination, which is why the primary CMB is nearly blind to Σm_ν in the range now allowed [der: from the relation above].
- Relativistic limit: ρ_ν = N_eff (7π²/120) T_ν,0⁴ (1+z)⁴. This defines N_eff.
- Non-relativistic limit: Ω_ν h² = Σm_ν / 93.14 eV (Noriega et al. 2022, arXiv:2208.02791 [src: Eq. 5]). The denominator depends on the assumed neutrino temperature and spectral distortions; check it before comparing ω_ν values across codes.
- f_ν ≡ Ω_ν / Ω_m.

Neutrinos count as radiation when the sound horizon r_d is set and as matter when BAO are measured. That mismatch, not free streaming, is what BAO + CMB constrain.

### 1.2 The three channels
<!-- key: the-three-channels -->

| Channel | What is measured | Why it sees Σm_ν | Main degeneracy |
|---|---|---|---|
| Geometry | BAO D_M/r_d, D_H/r_d with CMB θ*, ω_b, ω_cdm | Ω_m = Ω_cb + Ω_ν from BAO; ω_cb from CMB peak heights; the difference is Ω_ν | late-time expansion history (dark energy, curvature); H0 r_d |
| CMB lensing | peak smoothing in TT/TE/EE and the reconstructed C_L^κκ | suppressed growth lowers the lensing amplitude relative to A_s | τ through A_s e^(−2τ); the A_lens excess in some Planck likelihoods |
| Galaxy clustering shape | P(k) and bispectrum multipoles | scale-dependent suppression of the matter power spectrum | bias and counterterm priors; A_s, n_s |

Statements that need care:

- BAO alone do not constrain Σm_ν at all; adding a BBN prior and θ* tightens Ω_m only. The constraint appears when CMB information on ω_b and ω_cdm calibrates r_d and separates Ω_cb from Ω_ν (arXiv:2503.14744 Sect. 3.1).
- The small-scale suppression of the linear matter power spectrum is ΔP_m/P_m ≈ −8 f_ν, with the exact coefficient depending on which parameters are held fixed [sec: arXiv:2503.14744 Sect. 3.2, which attributes it to Hu, Eisenstein & Tegmark 1997, arXiv:astro-ph/9712057]. The 1997 abstract states that eV-mass neutrinos suppress power "by a factor of two" [src].
- Lensing observables are dimensionless and respond to the matter fraction Ω_m, not the physical density; within ΛCDM the primary CMB alone forces the matter fraction to rise steeply with neutrino mass (Loverde & Weiner 2024, arXiv:2410.00090). Their conclusion is that the geometric channel is at least as constraining as the suppression of structure in current data.
- In the DESI DR2 analysis, adding CMB lensing to DR1 BAO + CMB improves the profile-likelihood width σ by 0.023 eV but also moves the minimum towards positive values by 0.020 eV; adding the DR1 full shape changes σ by only 0.003 eV and lowers the limit mostly through a shift towards negative values (arXiv:2503.14744 Sect. 5.1 [src]). An "improved limit" can therefore come from a shift, not from information.
- Other CMB effects of Σm_ν without lensing reconstruction are the integrated Sachs–Wolfe effect, the lensing-induced smoothing of the peaks and the damping tail; the smoothing is the strongest (arXiv:2503.14744 Sect. 3.1).

### 1.3 Parameterisations of the mass spectrum
<!-- key: parameterisations-of-the-mass-spectrum -->

The floors come from the mass splittings. Oscillation was established by the zenith-angle-dependent deficit of atmospheric muon neutrinos in Super-Kamiokande, fitted by two-flavour ν_μ ↔ ν_τ oscillation with sin²2θ > 0.82 and 5 × 10⁻⁴ < Δm² < 6 × 10⁻³ eV² at 90% CL (Super-Kamiokande Collaboration 1998, arXiv:hep-ex/9807003 [src: abstract]); the current splittings are from NuFIT 6.0 (arXiv:2410.05380). The laboratory routes are reviewed for double beta decay by Dolinski 2019 (arXiv:1902.04097 [src]); KATRIN's first run gave m_ν < 1.1 eV (90% CL) from m_ν² = −1.0 (+0.9/−1.1) eV² (Aker 2019, arXiv:1909.06048 [src: abstract]), superseded by the 259-day result (arXiv:2406.13516, abstract).

| Name | Definition | Used by | Consequence |
|---|---|---|---|
| Degenerate | three states of mass Σm_ν/3, prior Σm_ν > 0 | DESI baseline, ACT, SPT | posterior piles up at zero |
| Degenerate with a floor | same, prior Σm_ν ≥ 0.059 eV (NO) or ≥ 0.10 eV (IO) | DESI DR1 | limit rises to 0.105 / 0.135 eV for DR2 (arXiv:2503.14744) [src: Sect. IV.3] |
| Lightest mass + splittings | NO: Σ = m_1 + √(m_1² + Δm²_21) + √(m_1² + Δm²_31); IO: Σ = m_3 + √(m_3² − Δm²_31) + √(m_3² − Δm²_32) | DESI DR2 with NuFIT 6.0 | 0.101 / 0.133 eV, against 0.105 / 0.135 eV with the floors (arXiv:2503.14744) [src: Sect. IV.3, Eqs. 25–28] |
| Effective signed mass | see §1.4 | Craig et al., Elbers et al., DESI DR2, Cozzumbo et al. | removes the boundary |

All numbers in the fourth column are from arXiv:2503.14744 Sect. 4.3. When Σm_ν is not varied, DESI fixes Σm_ν = 0.06 eV and N_eff = 3.044 (arXiv:2503.14744 Table 2 caption [src]); ACT fixes 0.06 eV "carried by a single massive species" as its baseline and uses three massive species when the mass is varied (arXiv:2503.14454 Sect. 6.1.1 [src]). The oscillation-based prior is strongly non-linear in the heavier masses; a prior linear in all three masses is an alternative that the DESI paper names and that changes Bayes factors (see `open-questions.md` §1.4).

### 1.4 Effective ("negative") neutrino mass: three different parameters
<!-- key: effective-negative-neutrino-mass-three -->

These are not the same quantity and their central values must not be compared directly.

1. **Clustering-only extension** (Craig et al. 2024, arXiv:2405.00836): the suppression of clustering is allowed to become an enhancement. Result on DESI DR1 + CMB: −160 ± 90 meV. [src: abstract]
2. **Consistent extension** (Elbers et al. 2024, arXiv:2407.10965; adopted in arXiv:2503.14744): a negative neutrino contribution to the energy density at late times, implemented in linear perturbation theory so that every effect of Σm_ν extends to negative values; identical to Σm_ν for positive values. Result on DESI DR2 + CMB: −0.101 (+0.047/−0.056) eV (arXiv:2503.14744, Sect. V.2).
3. **Effective mass with lensing nuisance parameters** (Cozzumbo et al. 2025, arXiv:2511.01967): a signed mass varied together with one parameter for peak smoothing and one for the lensing-potential amplitude. Result: −0.018 (+0.085/−0.089) eV. [src: abstract]

How each is implemented, read in the method sections:

| Parameter | Implementation | Data, code | Place |
|---|---|---|---|
| Σm̃_ν (Craig et al.) | modified CAMB: observables computed with physical Σm_ν = 0, and only C_ℓ^κκ rescaled by A_ℓ = C_ℓ^κκ[Σm_ν]/C_ℓ^κκ[0] calibrated on positive masses at fixed H0, ω_m, ω_b; TT/TE/EE lensed with the rescaled spectrum; no neutrino contribution to Ω_m, so slightly weaker than Σm_ν for positive values | Planck 2018 TT/TE/EE, ACT DR6 + Planck lensing, DESI DR1 BAO; Cobaya, R − 1 < 0.01; best fit −160 meV, the oscillation minimum disfavoured at 3σ | arXiv:2405.00836 Sect. 2.2 [src] |
| Σm_ν,eff (Elbers et al., DESI) | sign-reversed neutrino energy in background and Boltzmann hierarchy, Eq. 48 of arXiv:2503.14744 (see §1.7) | DESI DR2 BAO + CMB; CLASS | arXiv:2503.14744 Appendix A [src] |
| Σm̃_ν (Cozzumbo et al.) | every observable X, background and linear, expanded as X = X⁰ + sgn(Σm̃_ν)[X^(|Σm̃_ν|) − X⁰], X⁰ the massless limit, three degenerate states; plus A_lens^φφ (amplitude of the lensing-potential spectrum) and A_lens^TTTEEE (peak smoothing) | Commander low-ℓ TT, SimAll, SRoll2 or LoLLiPoP low-ℓ EE, Plik, CamSpec or HiLLiPoP high-ℓ, P-ACT lensing, DESI DR2; Cobaya + CLASS, R − 1 < 0.03; Σm_ν = 0.06 eV (normal ordering) when not varied | arXiv:2511.01967 Sect. II, Eq. 1 [src] |

The DESI paper states that evidence for negative values is to be read as unidentified systematics or as new physics possibly unrelated to neutrinos, not as negative-mass neutrinos (arXiv:2503.14744 Sect. 5.2). Graham, Green & Meyers 2025 (arXiv:2508.20999) separate two meanings of "negative mass": one describing the change in expansion history, the other describing enhanced lensing.

### 1.5 Statistical practice
<!-- key: statistical-practice -->

- **Bayesian with a positivity prior.** Standard for collaboration limits. The quoted σ(Σm_ν) = 0.020 eV for DESI DR2 + CMB (arXiv:2503.14744, abstract) is a property of the truncated posterior.
- **Profile likelihood with Feldman–Cousins.** The profile in Σm_ν ≥ 0 is close to parabolic; it is extrapolated to a full parabola with minimum μ0 and width σ, and a 95% limit is built with the Feldman–Cousins prescription. DESI DR2 + CMB: μ0 = −0.036 eV, σ = 0.043 eV, limit 0.053 eV (arXiv:2503.14744 Table 3 [src]). The minimisation uses iminuit with 14 free parameters for BAO + CMB and 44 with the full shape.
- **Agreement between the two.** Naredo-Tuero et al. 2024 (arXiv:2407.13831, Sect. III.1) find profile-likelihood and Bayesian limits within about 10%. In DESI DR2 the Feldman–Cousins limit is 0.01 eV lower than the Bayesian one in ΛCDM and 0.01 eV higher in w0waCDM.
- **Three widths for one data set.** 0.020 eV (Bayesian, truncated), 0.043 eV (profile parabola), 0.053 eV (effective-mass posterior) (arXiv:2503.14744, abstract; Sects. V.1, V.2). Only the last two measure sensitivity.
- **Tension metrics.** The tension with oscillations is quoted as 3σ from the effective-mass posterior (arXiv:2503.14744, abstract) and as 2.5–5σ depending on metric and data (Jiang et al. 2024, arXiv:2407.18047, abstract). State the metric.
- **Model comparison for the ordering.** Bayes factor between NO and IO with equal prior odds and a stated mass prior; the frequentist counterpart is Δχ² between the two minimum-mass points.
- **Validation.** The DESI neutrino analysis includes a validation on mocks (arXiv:2503.14744 Sect. 2.8, section title read only).

### 1.6 Free-streaming signatures that are independent of the expansion rate
<!-- key: free-streaming-signatures-that-are-independent -->

- **Phase shift.** Free-streaming radiation travels faster than the sound speed of the plasma and shifts the phase of the acoustic oscillations; for adiabatic initial conditions no other standard parameter produces this (Bashinsky & Seljak 2003, arXiv:astro-ph/0310198). In BAO it is parameterised by an amplitude β_φ, equal to 1 for N_eff = 3.044 and 0 for no free-streaming species (arXiv:2503.14744 Sect. 4.2).
- **Self-interacting neutrinos.** Delaying the onset of free streaming removes the phase shift; other parameters can compensate in the CMB (Kreisch, Cyr-Racine & Doré 2019, arXiv:1902.00534), which is why a phase-shift detection is model-dependent.

### 1.7 How the main analyses obtain the bound
<!-- key: how-the-main-analyses-obtain-the-bound -->

Read in the method sections this session of arXiv:2503.14744 (DESI DR2), arXiv:2503.14454 (ACT DR6), arXiv:2506.20707 (SPT-3G D1) and arXiv:1807.06209 (Planck 2018), one column each, at the place given in each cell. "Fixed" is the value used when Σm_ν is not varied.

| Item | DESI DR2 (arXiv:2503.14744) | ACT DR6 (arXiv:2503.14454) | SPT-3G D1 (Camphuis et al. 2025, arXiv:2506.20707) | Planck 2018 (arXiv:1807.06209) |
|---|---|---|---|---|
| Mass model when varied | three degenerate states, Σm_ν = 3m_ν [src: Sect. IV.3] | "three massive neutrino species" [src: Sect. VI.1.1, Eq. 33] | "arbitrary, positive Σm_ν"; number of massive states not stated in that section [src: Sect. VII.4.6] | three degenerate species, Fermi–Dirac, zero chemical potential; splittings neglected [src: Sect. 7.5.1] |
| Fixed | Σm_ν = 0.06 eV, N_eff = 3.044 [src: Table 1] | 0.06 eV in a single massive species [src: Sect. VI.1.1] | one massive neutrino, m_ν = 0.06 eV [src: Sect. V.5] | normal hierarchy at the minimal 0.06 eV [src: Sect. 7.5.1] |
| Prior | U[0, 5] eV on Σm_ν; U[0.05, 10] on N_eff; w0waCDM with w0 + wa < 0 [src: Table 1] | Σm_ν > 0 | Σm_ν > 0 | Σm_ν > 0 |
| τ | Planck PR3 low-ℓ SimAll EE + Commander TT [src: Sect. II.3] | Planck SRoll2 low-ℓ EE, often compressed to τ = 0.0566 ± 0.0058 [src: Sect. II.1] | Gaussian prior τ ~ N(0.051, 0.006) [src: Sect. VII.1] | Planck lowE |
| High-ℓ CMB | PR4 CamSpec (ℓ > 30); alternatives PR3 plik, PR4 LoLLiPoP–HiLLiPoP [src: Sect. II.3] | ACT DR6 + Planck cut to ℓ < 1000 in TT and ℓ < 600 in TE/EE ("P-ACT"), or WMAP ("W-ACT") [src: Sect. II.1] | SPT-3G D1; CMB-SPA adds ACT and Planck with Planck removed at ℓ > 1000 [src: Sect. VII.4.6] | Plik; CamSpec as alternative |
| Lensing, BAO | Planck PR4 + ACT DR6 lensing; DESI DR2 BAO | Planck + ACT lensing; DESI Year-1 BAO ("LB") | SPT-3G lensing; DESI DR2 BAO [src: abstract, Sect. VII.3] | Planck 2018 lensing; BOSS-era BAO |
| Codes | Cobaya (Metropolis–Hastings), CAMB, CLASS for the effective mass, getdist [src: Sect. II.6] | Cobaya with CAMB, CLASS or CosmoPower; CosmoRec or HyRec; HMcode 2020 dark-matter only; PRIMAT helium [src: Sect. III] | CAMB, CLASS, HyRec, CosmoPower and OLÉ emulators; ACT DR6 accuracy settings [src: Sect. V.5] | — |
| Limit, 95% | < 0.0642 eV, BAO + CMB [src: Eq. 15] | < 0.089 eV P-ACT-LB, < 0.088 eV W-ACT-LB [src: Eq. 33] | < 0.081 eV SPT-3G D1 + DESI; < 0.055 eV CMB-SPA + DESI [src: Eqs. 105–106] | < 0.24 eV TT,TE,EE+lowE+lensing [src: Eq. 57b] |

Points that the table does not carry:

- **DESI's other parameterisations.** For the ordering it varies the lightest mass m_l with prior U[0, 5] eV and the NuFIT 6.0 splittings, and a binary ordering variable 𝓜 with prior U[−1, 1] and equal prior odds [src: arXiv:2503.14744, Table 1; Sect. IV.3, Eqs. 20–21]. DESI notes that this prior is "highly non-linear" in the heavier masses. Floors of 0.059 and 0.10 eV on the degenerate model give 95% limits of 0.105 and 0.135 eV, against 0.101 and 0.133 eV with the splittings [src: Eqs. 25–28].
- **DESI's effective mass.** The neutrino energy ε = √(p² + a²m²) in the background and Boltzmann equations is replaced by ε_eff = sgn(m_ν,eff) √(p² + a²m²_ν,eff) [src: arXiv:2503.14744, Appendix A, Eq. 48]. To keep N_eff = 3.044 the massless-species number N_ur is set to 0.00441 for positive and 6.08627 for negative masses [src: Appendix A]. Runs with this parameter use CLASS [src: Sect. II.6].
- **DESI's external priors** for runs without full CMB: ω_b = 0.02218 ± 0.00055 from BBN; n_s = 0.9649 ± 0.0042, or ten times that width ("n_s,10"); and multivariate Gaussian priors on (θ*, ω_b, ω_cdm) or (θ*, n_s) compressed from the baseline CMB with the effective mass free [src: arXiv:2503.14744, Sect. II.7].
- **DESI full shape.** P(k) monopole and quadrupole of DR1 in six bins (BGS, LRG1–3, ELG1, QSO), 0.02 < k < 0.20 h/Mpc, seven EFT nuisance parameters per tracer with physically motivated priors, covariance from 1000 EZmocks [src: arXiv:2503.14744, Sect. II.2]. A run in which Σm_ν enters the background only gives a much weaker limit, so the full-shape limit uses the scale-dependent free-streaming effect; marginalising a fudge factor X_rsd on θ = X_rsd f δ leaves the limit almost unchanged, so it does not come from the amplitude [src: Sect. VI, Eqs. 39–40]. With CMB priors on θ* and n_s only (no CMB ω_b or ω_cdm), DESI DR1 (FS + BAO) + BBN gives < 0.193 eV; this limit is not free-streaming-only: geometry and shape each contribute about half of its observed information [src: Sect. VI, Eq. 42]. Details in `deep/neutrino-mass-full-shape.md`.
- **SPT and the BAO consistency gate.** SPT does not combine data sets whose Ω_m–h r_d constraints differ by more than 3σ: it reports no SPT+ACT + DESI neutrino limit. CMB-SPA + DESI "appears to rule out" the normal and inverted orderings at 96.6% and 99.9%; moving Σm_ν to zero lowers χ² by 5.1 relative to the normal-ordering minimum, 2.3σ for one parameter [src: arXiv:2506.20707, Sect. VII.4.6]. CMB alone: < 0.77 eV (SPT-3G D1), < 0.58 eV (SPT+ACT), < 0.19 eV (CMB-SPA), against < 0.25 eV for Planck [src: Eqs. 102–104].
- **Planck 2018, which channel.** For m_ν ≪ 1 eV the primary-spectrum effect is a distance change degenerate with H0, so Planck constrains low masses through lensing; the lowE τ tightens A_s through C_ℓ ∝ A_s e^(−2τ) and so the mass [src: arXiv:1807.06209, Sect. 7.5.1]. Planck lensing + BAO + θ_MC alone gives < 0.60 eV, "almost independent of lensing effects in the CMB spectra" [src: Eq. 59]; TT+lowE+BAO without lensing gives < 0.16 eV [src: Eq. 60a].
- **Older parameterisation work.** DESI cites limits on the lightest mass of 0.086 eV (BOSS DR12 + Planck 2015 + Pantheon + BBN) and 0.040 eV (Planck 2018 + BOSS DR12 + MGS + 6dFGS) from the analyses that introduced the m_l parameterisation [sec: arXiv:2503.14744 Sect. IV.3; primary papers not fetched].

## 2. N_eff and light relics
<!-- key: neff-and-light-relics -->

- Standard-Model value: 3.044 (Froustey, Pitrou & Volpe 2020, arXiv:2008.01074 gives 3.0440; QED corrections in Bennett et al. 2019, arXiv:1911.04504). The earlier 3.046 comes from momentum-dependent kinetic equations with three-flavour oscillations, which change the energy-density result little but raise the effect on primordial ⁴He by about 20% (Mangano 2005, arXiv:hep-ph/0506164 [src]).
- What the CMB measures: the expansion rate before recombination through the damping tail relative to the acoustic scale, and the phase shift. The first is degenerate with the primordial helium fraction (arXiv:astro-ph/0310198); analyses either impose BBN consistency for Y_P or free it.
- **Free-streaming versus fluid radiation.** N_eff in tables is free-streaming radiation. Self-interacting (fluid) dark radiation produces no phase shift and is constrained separately as N_idr (arXiv:2503.14454: N_idr < 0.134).
- **Model dependence of ΔN_eff limits.** The ACT limit assumes a power-law primordial spectrum; freeing the running and its running relaxes the limit on self-interacting dark radiation to ΔN_eff < 0.58 (Garny, Niedermann & Sloth 2026, arXiv:2604.26541). [src: abstract]
- **Stepped or decoupling dark radiation.** Wess–Zumino dark radiation changes its energy density when a mediator becomes non-relativistic; ACT DR6 closes most of the parameter space in which it raised H0 (Cvetko, Joseph & Marques-Tavares 2025, arXiv:2512.19633).
- **BBN.** Light-element abundances measure the expansion rate at about one second through N_ν and the baryon density through D/H. The helium prediction depends mainly on the weak rates and the neutron lifetime; the baryon density inferred from D/H depends on the deuterium-burning rates (Pitrou et al. 2018, arXiv:1801.08023; Schöneberg 2024, arXiv:2401.15054). BBN and the CMB probe the radiation density at different epochs, so a difference between them is itself a constraint (Yeh et al. 2022, arXiv:2207.13133).
- Convention: BBN papers quote N_ν with baseline 3; CMB papers quote N_eff with baseline 3.044. The stated difference is N_eff − 3 = 0.044 (arXiv:2207.13133, abstract).

### How N_eff is constrained in the main analyses
<!-- key: how-neff-is-constrained-in-the-main-analyses -->

| Item | What the paper writes | Place |
|---|---|---|
| Definition | ρ_rad = N_eff (7/8)(4/11)^(4/3) ρ_γ (Planck Eq. 62; SPT Eq. 70 writes ρ_rad = ρ_γ[1 + (7/8)(4/11)^(4/3) N_eff]); ACT writes N_eff ≡ (8/7)(11/4)^(4/3) ρ_ν/ρ_γ | arXiv:1807.06209 Sect. 7.5.2; arXiv:2506.20707 Sect. VII.2.4; arXiv:2503.14454 Sect. VI.1.1 [src] |
| Where in the spectrum | the damping tail (high ℓ) of TT/TE/EE, because N_eff changes the expansion rate before recombination and so the diffusion-damping time, and because free-streaming radiation damps perturbation growth; the latter also shifts the phase of the acoustic peaks | arXiv:2503.14454 Sect. VI.1.1 [src] |
| Mass while N_eff varies | ACT and SPT keep 0.06 eV in one massive state; DESI fixes Σm_ν = 0.06 eV, prior U[0.05, 10] on N_eff | arXiv:2503.14454 Sect. VI.1.1; arXiv:2506.20707 Sect. V.5; arXiv:2503.14744 Table 1 [src] |
| Helium | varied with N_eff or by BBN consistency; with Y_P free as well, CMB-SPA gives N_eff = 2.96 (+0.21/−0.24) and Y_P = 0.233 ± 0.013, against 2.82 ± 0.12 with BBN Y_P | arXiv:2506.20707 Table 5 [src] |
| One-sided extra species | ACT fits a positive ΔN_eff above 3.044 and maps it to spin and decoupling temperature; P-ACT-LB excludes spin-0 and spin-1/2 relics decoupling below about 200 MeV and spin-3/2 below about 1 GeV (95%) | arXiv:2503.14454 Sect. VI.1.1, Eq. 32 [src] |
| Relic contribution | ΔN_eff = g [43/(4 g_s)]^(4/3) × (4/7 for a boson, 1/2 for a fermion), g_s the entropy degrees of freedom at decoupling | arXiv:1807.06209 Eq. 63 [src] |
| BAO phase shift | φ(k) = β_φ(N_eff) f(k) with a template f(k); β_φ = 1 for N_eff = 3.044, 0 for no free-streaming species | arXiv:2503.14744 Sect. IV.2 [src] |
| BBN code in CMB fits | ACT uses a PRIMAT helium table (N_eff = 3.044) and corrects for the 3.046 assumed in the CLASS BBN module | arXiv:2503.14454 Sect. III [src] |

Planck 2018 still writes the standard value as N_eff ≈ 3.046 and attributes it to incomplete decoupling at electron–positron annihilation, citing Gnedin & Gnedin 1998, Mangano et al. 2005 and de Salas & Pastor 2016 [sec: arXiv:1807.06209 Sect. 7.5.2].

## 3. Dark-matter properties from small-scale structure
<!-- key: dark-matter-properties-from-small-scale -->

### 3.1 What is constrained
<!-- key: what-is-constrained -->

All of the models below are tested through one of two effects: a cutoff in the linear matter power spectrum (fewer low-mass haloes), or a change in the internal structure of haloes.

| Model | Parameter | Linear-theory effect | Halo-scale effect |
|---|---|---|---|
| Warm (thermal relic) | m_WDM in keV | free-streaming cutoff | fewer subhaloes, lower concentrations (Bode, Ostriker & Turok 2000, arXiv:astro-ph/0010389) |
| Fuzzy / ultralight | boson mass in eV | cutoff from the de Broglie scale, about 1 kpc at 10⁻²² eV; proposed by Hu 2000 (arXiv:astro-ph/0003365 [src: abstract]: wave properties give halo cores and "sharply" suppress small-scale linear power) | soliton core, interference granules; haloes below about 10⁷ (m/10⁻²² eV)^(−3/2) M⊙ do not form (Hui et al. 2016, arXiv:1610.08297 [src]); review of wave dark matter below about 30 eV: Hui 2021, arXiv:2101.11735 [src] |
| Ultralight sub-component | Ω_a or fraction, mass | scale-dependent suppression of growth | — |
| Scattering with baryons | σ0, index n in σ ∝ vⁿ, mass | collisional damping: momentum transfer between dark matter and baryons changes the CMB and the matter power spectrum (Chen 2002, arXiv:astro-ph/0202496); constraints for −4 ≤ n ≤ 2 from Planck and SDSS Lyα, the forest dominating for n > −3 (Dvorkin 2014, arXiv:1311.2937) [src] | — |
| Scattering with neutrinos or dark radiation | u_νχ; ETHOS parameters | damping and dark acoustic oscillations (Cyr-Racine et al. 2015, arXiv:1512.05344) | — |
| Self-interacting | σ/m at a stated velocity | none for elastic scattering | cores, then gravothermal core collapse; offsets in mergers (Spergel & Steinhardt 1999, arXiv:astro-ph/9909386) |
| Decaying | lifetime, fraction, kick velocity | late-time loss of matter or of small-scale power; decays to relativistic particles affect mainly the low-ℓ CMB, and the lifetime correlates with r and Ω_k (Audren 2014, arXiv:1407.2418 [src]) | — |

### 3.2 Half-mode scale and the keV conversion
<!-- key: half-mode-scale-and-the-kev-conversion -->

Limits are derived on the half-mode mass M_hm (or wavelength λ_hm) and then converted to a thermal-relic mass. Pairs read this session:

| M_hm | m_WDM | Source | Flag |
|---|---|---|---|
| 10^7.8 M⊙ | 5.2 keV | Gilman et al. 2019, arXiv:1908.06983 | [src: abstract] |
| 10^7.8 M⊙ | 5.6 keV | Keeley et al. 2025, arXiv:2511.07765 | [src: abstract] |
| 10^7.6 M⊙ | 6.4 keV | arXiv:2511.07765 | [src: abstract] |
| 10^7.4 M⊙ | 6.5 keV | Gilman et al. 2025, arXiv:2511.07513 | [src: abstract] |
| 10^7.4 M⊙ | 7.4 keV | Nadler et al. 2021, arXiv:2101.07810 | [src: abstract] |
| 10^7.2 M⊙ | 7.4 keV | arXiv:2511.07513 | [src: abstract] |
| 10^7.0 M⊙ | 9.7 keV | arXiv:2101.07810 | [src: abstract] |
| 3 × 10⁷ M⊙/h (λ_hm = 0.089 Mpc/h) | 6.048 keV | Enzi et al. 2020, arXiv:2010.13802 | [src: abstract] |

The same half-mode mass maps to different keV values in different papers (10^7.8 M⊙ gives 5.2 or 5.6 keV, arXiv:1908.06983 and arXiv:2511.07765; 10^7.4 M⊙ gives 6.5 or 7.4 keV, arXiv:2511.07513 and arXiv:2101.07810; all abstract). The conversion depends on the adopted transfer-function fit, cosmology and unit convention (M⊙ or M⊙/h). Compare limits in M_hm, or re-derive the mass with one relation.

**The relations as the papers write them.** The cutoff parameter α_cutoff used by the stream analysis below is attributed there to Schneider 2012 (arXiv:1112.0330, whose abstract describes WDM halo mass functions, concentrations and bias from N-body simulations and the halo model [src]; the attribution is [sec: arXiv:1911.02663 Sect. 3.1]).

| Step | Relation | Source |
|---|---|---|
| Transfer function | T(k) = [P_WDM(k)/P_CDM(k)]^(1/2) at fixed cosmological parameters | Viel et al. 2005, arXiv:astro-ph/0501562 Sect. 2; Gilman et al. 2025, arXiv:2511.07513 Eq. 17; Liu, Gong & Liao 2025, arXiv:2512.01361 Eq. 1 [src] |
| Thermal-relic fit, 2005 | T(k) = [1 + (αk)^(2ν)]^(−5/ν), ν = 1.12 (best fit for k < 5 h/Mpc), α = 0.049 (m_x/1 keV)^(−1.11) (Ω_x/0.25)^(0.11) (h/0.7)^(1.22) h⁻¹ Mpc, from CMBFAST or CAMB runs; form taken from Bode et al. 2000 | arXiv:astro-ph/0501562 Sect. 2 [src] |
| Same form in a Lyα analysis | T ≈ [1 + (αk)^(2μ)]^(−5/μ), μ = 1.12, α = 70 ckpc (m_WDM/1 keV)^(−1.11); the simulations sample 1/m_WDM on a grid 0, 1/4, 1/3, 1/2 keV⁻¹ | Iršič et al. 2023, arXiv:2309.04533 Sect. IV.1, Table 1 [src] |
| Updated thermal-relic fit | T² = [1 + (α k)^(2ν)]^(−10/ν), ν = 1.049, α = 0.0437 (m/1 keV)^(−1.188) (ω_WDM/0.12)^(0.2463) (h/0.6736)^(2.012) h⁻¹ Mpc | arXiv:2512.01361 Eqs. 9–10, citing a later transfer-function calculation [src] |
| Half-mode scale | T(k_hm) = 1/2, i.e. T² = 0.25; for T = (1 + (αk)^β)^(−γ), k_hm = α⁻¹ (2^(1/γ) − 1)^(1/β) | arXiv:2512.01361 Eq. 2; arXiv:2511.07513 Sect. IV.2 [src] |
| Half-mode mass | M_hm = (4π/3) Ω_m ρ_crit (π/k_hm)³, ρ_crit at z = 0 | arXiv:2512.01361 Eq. 3; arXiv:2511.07513 Sect. IV.2 [src] |
| keV conversion, JWST arcs + flux ratios | m_hm = 4.0 × 10⁸ (m_therm/3 keV)^(−3.564) M⊙, from the Vogel & Abazajian transfer function | arXiv:2511.07513 Eq. 18 [src] |
| keV conversion, JWST flux ratios | m_hm = 5 × 10⁸ (m_therm/3 keV)^(−10/3) M⊙ | Keeley et al. 2025, arXiv:2511.07765 Eq. 10 [src] |
| keV conversion, Milky Way + M31 satellites | M_hm = 4.3 × 10⁸ (m_WDM/3 keV)^(−3.564) M⊙ | arXiv:2512.01361 Eq. 11 [src] |
| Streams (GD-1, Pal 5) | M_hm = (4π Ω_m ρ_crit/3)(λ_hm/2)³, λ_hm = 2π α_cutoff (2^(ν/5) − 1)^(−1/(2ν)), ν = 1.12, α_cutoff = 0.047 (m_WDM/keV)^(−1.11) (Ω_c/0.2589)^(0.11) (h/0.6774)^(1.22) h⁻¹ Mpc; subhalo function (1 + γ M_hm/M)^(−β) × CDM, γ = 2.7, β = 0.99 (Aquarius fit); prior log10 M_hm/M⊙ uniform on [4.8, 10], "approximately 1 to 50 keV" | Banik et al. 2019, arXiv:1911.02663 Sects. 3.1, 4.1 [src] |
| Halo and subhalo suppression | dN_WDM = dN_CDM × f(m_hm/m), f(x) = (1 + a x^b)^c, a = 1.95, b = 0.8, c = −1.0; concentration c_WDM = c_CDM f with a = 60, b = 1, c = −0.17 | arXiv:2511.07513 Eqs. 19–22 [src] |
| Subhalo suppression for satellites | f = [1 + (α M_hm/M)^β]^(−γ), M the peak virial mass; WDM (α, β, γ) = (2.5, 0.9, 1.0), fuzzy (5.5, 2.5, 0.3), fitted to zoom-in simulations with modified initial conditions | arXiv:2512.01361 Eqs. 8, 12 [src] |
| Fuzzy dark matter | T² = [sin(x^m)/(x^m (1 + B x^(6−m)))]², m = 5/2, x = A k/k_J, k_J = 9 Mpc⁻¹ m_22^(1/2), A = 2.22 m_22^(1/25 − ln(m_22)/1000), B = 0.16 m_22^(−1/20); M_hm = 4.5 × 10¹⁰ M⊙ m_22^(−1.41), m_22 = m/10⁻²² eV | arXiv:2512.01361 Eqs. 5–7 [src] |
| Thermal relic to sterile neutrino | m_sterile = 4.43 keV (m_thermal/1 keV)^(4/3) (0.25 × 0.7²/ω_x)^(1/3), for sterile neutrinos produced by oscillations with the active-neutrino phase-space shape scaled by a factor χ, matching ω_x and m_x/T_x | arXiv:astro-ph/0501562 Sect. 2 [src] |
| Lyα sensitivity | linear P_WDM/P_CDM ∼ m^20 k^(−20) for k ≫ 14 (m/1 keV) Mpc⁻¹; in the simulations the flux-power suppression at 4.2 < z < 5.0 and 0.01 < k < 0.2 s/km scales approximately as 1 − 0.1 ((1+z)/5)⁴ (k/0.1)^(3/4) (m/4 keV)^(−1) for m > 3 keV | arXiv:2309.04533 Sect. IV.3 [src] |

Because the JWST papers and the satellite papers convert half-mode masses to keV with different relations (table above), part of the keV spread between them can come from the conversion rather than from the data [der: from the relations in the table above].

The pairs of Nadler et al. 2021 (10^7.4 M⊙ ↔ 7.4 keV, 10^7.0 M⊙ ↔ 9.7 keV) come from the 5 × 10⁸ (m/3 keV)^(−10/3) M⊙ relation, which that paper takes from Nadler et al. 2020 (arXiv:2101.07810 Sect. 2.4 [src]); the same section gives the subhalo suppression as [1 + (α M_hm/M)^β]^γ with (α, β, γ) = (2.7, 1.0, −0.99) in the 2020 satellite analysis and (1, 1, −1.3) in the 2019 lensing analysis [src]. The 2020 satellite, 2021 joint and 2025 flux-ratio limits use the −10/3 relation, the 2025 arcs and Milky Way + M31 papers the −3.564 one (table above); the relation behind the 2019 pair (10^7.8 M⊙ ↔ 5.2 keV) was not read. Liu, Gong & Liao caution that comparing different non-cold models through M_hm "can be an oversimplification and may introduce significant biases" (arXiv:2512.01361 Sect. II.1 [src]).

**Confidence criterion.** The JWST flux-ratio limits are 5.6 and 6.4 keV as 10:1 Bayes-factor bounds, and 7.9 and 9.7 keV at 95% confidence for the same data and priors; the authors note that limits from different probes "are not directly comparable" because their prior ranges differ (arXiv:2511.07765 Sects. VIII.1, IX [src]).

A thermal-relic limit does not transfer to other models by matching the half-mode scale: for dark matter–neutrino scattering this mapping overestimates the constraint relative to dedicated simulations (Mosbech et al. 2026, arXiv:2607.15020). For ultralight fields produced with a field power spectrum peaked at a subhorizon wavenumber k*, the field free-streams like warm dark matter and the mass limit scales with k* (Nadler et al. 2026, arXiv:2605.15371).

### 3.3 The probes
<!-- key: the-probes -->

| Probe | Observable | Scales | What must be modelled |
|---|---|---|---|
| Lyα forest P1D at z ≳ 4 | flux power to k_max = 0.1–0.2 s/km (arXiv:2309.04533, abstract; arXiv:2007.12705, footnote 4) | cutoff in the 1D flux power | thermal history, reionisation, peculiar-velocity smearing; data and emulators in `cosmo-lyman-alpha` |
| Milky Way satellites | luminosity function with survey selection | haloes hosting the faintest galaxies | galaxy–halo connection, Milky Way mass, subhalo disruption by the disk (Nadler et al. 2020, arXiv:2008.00022) |
| Strong lensing, flux ratios | relative magnifications of quad images | haloes down to 10⁶ M⊙ in the lens and along the line of sight | macromodel including m = 1, 3, 4 multipoles, source size, tidal stripping, globular clusters, subhalo-abundance prior (arXiv:2511.07765, abstract) |
| Strong lensing, extended arcs | surface-brightness perturbations | individual subhaloes; granules for fuzzy dark matter | source reconstruction, smooth-lens model (Powell et al. 2023, arXiv:2302.10941) |
| Stellar streams | density variations along GD-1, Pal 5 | subhaloes below the dwarf-galaxy scale | slope and normalisation of the subhalo mass function, tidal disruption in the inner Galaxy (Banik et al. 2019, arXiv:1911.02663) |
| Ultraviolet luminosity functions | faint-end abundance at z = 4–8 (HST) and 9–14.5 (JWST), arXiv:2404.13596 abstract | delayed formation of low-mass haloes | star-formation efficiency, magnitude–halo-mass scatter (Liu, Shan & Zhang 2024, arXiv:2404.13596) |
| Dwarf-galaxy kinematics | sizes and velocity dispersions | granule heating; core structure | soliton–halo relation, other heating sources (Dalal & Kravtsov 2022, arXiv:2203.05750) |
| Cluster mergers and profiles | dark matter–galaxy offsets; central densities | σ/m at relative velocities of order 1000 km/s (arXiv:1605.04307, Sect. 1) | how centroids are measured, gas stripping, adiabatic contraction (Robertson, Massey & Eke 2016, arXiv:1605.04307) |
| CMB and galaxy power spectra | TT/TE/EE, lensing, P(k) | sub-component axions, scattering, decays | non-linear model for the non-cold component (Rogers et al. 2023, arXiv:2301.08361) |

### 3.4 Self-interactions
<!-- key: self-interactions -->

The quantity is the cross section per unit mass σ/m in cm²/g at a characteristic relative velocity, which rises from dwarfs to clusters. Reviews: Tulin & Yu 2017 (arXiv:1705.02358), Adhikari et al. 2022 (arXiv:2207.10638). Velocity-dependent models are written with a normalisation σ0 and a velocity scale ω (as in Jia et al. 2026, arXiv:2601.17118). Haloes first form an isothermal core and can later undergo gravothermal core collapse, so one rotation curve can admit a core-growth and a core-collapse solution.

### 3.5 Decays
<!-- key: decays -->

Two models are in use (Simon et al. 2022, arXiv:2203.07440): a fraction f of the dark matter decaying to dark radiation with lifetime τ, constrained mainly by the CMB; and all of the dark matter decaying to dark radiation plus a massive warm daughter, with a fraction ε of the rest-mass energy going to radiation, proposed as a way to lower S8. The Boltzmann hierarchy for the first is derived in Poulin, Serpico & Lesgourgues 2016 (arXiv:1606.02073).

## 4. Codes named in the analyses read this session
<!-- key: codes-named-in-the-analyses-read-this-session -->

| Code | Use | Reference | Flag |
|---|---|---|---|
| CLASS, non-cold relics module | massive neutrinos, warm dark matter and arbitrary phase-space distributions in a Boltzmann code | Lesgourgues & Tram 2011, arXiv:1104.2935 | [src] |
| PRIMAT | BBN network with weak-rate corrections | arXiv:1801.08023 | [src] |
| PRyMordial | BBN with marginalisation over nuclear rates | named in arXiv:2401.15054; reference paper not fetched | [sec] |
| Cholla | GPU hydrodynamics for the 1080-simulation warm-dark-matter grid | used in arXiv:2209.14220, abstract; reference not fetched | [sec] |
| Galacticus | semi-analytic subhalo populations for lensing and satellite analyses | used in arXiv:2101.07810, arXiv:2511.07513; reference not fetched | [sec] |
| GALLUMI with CLASS DMeff | ultraviolet luminosity functions with interacting dark matter | used in arXiv:2510.10757; references not fetched | [sec] |
| ETHOS | mapping of dark-sector microphysics to linear-power and self-interaction parameters | arXiv:1512.05344 | [src] |
| iminuit | profile likelihoods | used in arXiv:2503.14744 | [sec] |

`cosmo-software-ecosystem` holds the general Boltzmann (CAMB), sampler (Cobaya) and emulator (EuclidEmulator2) references, and the fuzzy-dark-matter simulation codes; they are not repeated here.

## 5. Conventions and where the community is split
<!-- key: conventions-and-where-the-community-is-split -->

- **Limit level.** Neutrino-mass limits are 95%; KATRIN quotes 90% CL; lensing papers quote Bayes-factor 10:1 or posterior-odds 20:1 bounds next to 95% limits. Liu, Gong & Liao 2025 (arXiv:2512.01361, abstract) give both: 6.20 keV at 95% and 5.75 keV at 20:1.
- **Units.** Σm_ν in eV or meV; warm-dark-matter mass in keV for a thermal relic; fuzzy-dark-matter mass in eV; Lyα wavenumbers in s/km; σ/m in cm²/g; dark matter–proton cross sections in cm².
- **Thermal relic versus sterile neutrino.** The same data give 550 eV for a thermal relic and 2.0 keV for a sterile neutrino (Viel et al. 2005, arXiv:astro-ph/0501562, abstract). State the production mechanism. Non-resonant production by oscillations with active neutrinos (Dodelson 1994, arXiv:hep-ph/9303287, abstract: sterile neutrinos "can be either hot, warm, or cold", and 0.1–1.0 keV gives warm dark matter) differs from lepton-asymmetry-driven resonant production, which gives a colder, non-thermal spectrum (Shi 1999, arXiv:astro-ph/9810076) [src]. Review of production mechanisms and limits: Boyarsky 2019, arXiv:1807.07938 [src].
- **Bayesian versus frequentist.** Split on neutrino mass (§1.5) and on decaying dark matter, where the two give strongly different 68% regions (Montandon et al. 2025, arXiv:2505.20193). [src: abstract]
- **Collaboration result versus external reanalysis.** The tightest Σm_ν numbers (0.049 eV in ΛCDM, 0.077 eV in w0waCDM) come from an external EFT reanalysis of DESI DR1 with bispectrum and cross-correlations (Ivanov et al. 2026, arXiv:2601.16165), not from the DESI Collaboration. Not every limit below DESI's own is external: SPT's CMB-SPA + DESI DR2 gives < 0.055 eV (Camphuis et al. 2025, arXiv:2506.20707 Eq. 106 [src]), with Planck removed above ℓ = 1000.
- **Blinding.** The CMB and BAO inputs are blinded by their collaborations (see `cosmo-cmb`, `cosmo-galaxy-clustering`). No blinding statement was read this session for any of the small-scale dark-matter analyses listed in §3.3.

## Not verified
<!-- key: not-verified -->

- The half-mode to keV relation of Gilman et al. 2019 was not read, only its pair 10^7.8 M⊙ ↔ 5.2 keV (arXiv:1908.06983, abstract); that of Enzi et al. 2020 was not read either. The others are in the half-mode subsection above.
- The fuzzy-dark-matter Jeans scale was read only as it enters the transfer-function fit of arXiv:2512.01361 (k_J = 9 Mpc⁻¹ m_22^(1/2)); its derivation and the paper of reference [65] there were not read.
- Number of massive states in DESI's fixed-mass baseline runs: not stated in the sections read; for the effective-mass runs the massless-species value N_ur = 0.00441 is "the standard CLASS value" (arXiv:2503.14744 Appendix A).
- References for PRyMordial, Cholla, Galacticus, GALLUMI and CLASS DMeff were not fetched.
- (2026-10-24.) The statement that the floor approximation reproduces DESI's ordering limits "within 0.004 eV" was an agent's difference of the limits of arXiv:2503.14744, Eqs. 25–28; the paper does not state it. The two pairs of limits are now given side by side.
