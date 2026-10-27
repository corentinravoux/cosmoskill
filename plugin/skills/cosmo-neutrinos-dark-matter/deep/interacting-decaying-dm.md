# Interacting and decaying dark matter — cosmo-neutrinos-dark-matter dossier

Scope: how dark matter that scatters with baryons, neutrinos or dark
radiation, or that decays, is put into a Boltzmann code (collision terms,
temperature equations, relative bulk velocity, decay hierarchies and
their approximations), how the linear result is carried to non-linear and
small-scale probes (scale cuts, EFT, half-mode mapping, dedicated
simulations), which priors and sampling choices are made, and what each
choice was found to cost.
Snapshot: 2026-10-19.
From: Snowmass 2021 halo-measurements white paper (Bechtol et al.,
arXiv:2203.07354), Sect. 2.1.4; ACT DR6 extended models
(arXiv:2503.14454), Sects. VI.4.1, VI.5.2.

Already in L2, not repeated here: the limits themselves
(`results.md#interacting-dark-matter-95-upper-limits`,
`results.md#decaying-dark-matter-dark-radiation-and`); the model table
with one line per model (`physics-and-methods.md#what-is-constrained`)
and the two decay models (`physics-and-methods.md#decays`); the
statement that half-mode matching overestimates the dark matter–neutrino
limit (`physics-and-methods.md#half-mode-scale-and-the-kev-conversion`);
Bayesian against profile-likelihood intervals for decays and the S8-prior
dependence of the two-body best fit
(`systematics.md#sub-component-axions-decays-the-x-ray-line`); the scale
dependence of CMB against satellite limits
(`systematics.md#interacting-and-self-interacting-dark-matter`).
Self-interactions inside haloes are in `deep/self-interacting-dm.md`;
neutrino self-interactions and fluid dark radiation in
`cosmo-cmb/deep/damping-tail-light-relics.md`.

## How it is done
<!-- key: how-it-is-done -->

Notation, used throughout: a dot (or a prime in the decay papers) is a
derivative with respect to conformal time τ; a the scale factor; 𝓗 = ȧ/a;
k the comoving wavenumber; δ_X and θ_X the density contrast and velocity
divergence of species X; h and η the synchronous-gauge metric
perturbations, ψ and φ the Newtonian potentials; χ the interacting or
decaying dark-matter species, m_χ its mass, ρ_χ its density, f_χ the
fraction of the dark matter it makes up; m_H the hydrogen mass.

### Step 0. Name the interaction and its parameter
<!-- key: step-0-name-the-interaction-and-its-parameter -->

| Model | Parameter as the analyses write it | Definition | Source |
|---|---|---|---|
| DM–baryon scattering | σ₀, n, m_χ | momentum-transfer cross section σ̄(v) ≡ ∫dc_θ (1 − c_θ) dσ/dc_θ (Eq. 3), taken as σ̄ = σ₀ vⁿ (Eq. 4); n = −1 from a Yukawa potential, −2 for an electric dipole moment, −4 for a millicharge | Dvorkin, Blum & Kamionkowski 2014, arXiv:1311.2937 Sect. II [src] |
| DM–neutrino scattering | u_νχ | u_νχ ≡ (σ_νχ/σ_Th)(m_χ/100 GeV)⁻¹ (Eq. 1), σ_Th the Thomson cross section; chosen "because of the degeneracy between the scattering cross section and dark matter mass in the scattering rate" | Mosbech et al. 2026, arXiv:2607.15020 Sect. 2 [src] |
| DM–dark radiation scattering | {ω_DR, {a_n, α_l}, {b_n, β_l}, {d_n, m_χ, ξ}} | opacity and angular coefficients that fix the linear power spectrum (Eq. 48); the subset {ω_DR, {a_n, α_l}} "is largely responsible" for its broad shape | Cyr-Racine et al. 2016 (ETHOS), arXiv:1512.05344 Sect. IV [src] |
| Decay to dark radiation | f_dcdm (or Ω_dcdm^ini), Γ_dcdm | Γ the decay rate in proper time; CLASS takes the total density of decaying matter plus its radiation either today or "initially", the latter preserving the early evolution until decays begin | Poulin, Serpico & Lesgourgues 2016, arXiv:1606.02073 Sect. 2.1 [src] |
| Two-body decay, one massless and one massive daughter | Γ, ε | ε the fraction of the parent rest-mass energy given to the massless daughter | Franco Abellán et al. 2020, arXiv:2008.09615 abstract [src] |
| Two-body decay, arbitrary daughter masses | Γ, f, ε₁, ε₂ | ε_i ≡ m_χi/m_χ, the daughter-to-parent mass ratios (Eq. 3); ε₁ = 0.99, ε₂ = 0 corresponds to v_kick ≈ 0.01c; observables depend only on the ratios | Lee et al. 2026, arXiv:2607.24910 Sect. II.2, Appendix C [src] |

The symbol ε means an energy fraction in the first two-body papers and a
mass ratio in the 2026 code paper; convert before comparing.

### Step 1. Background
<!-- key: step-1-background -->

- **Decay.** ρ′_dcdm = −3𝓗ρ_dcdm − aΓρ_dcdm and ρ′_dr = −4𝓗ρ_dr +
  aΓρ_dcdm (arXiv:1606.02073 Eqs. 1–2 [src]).
- **Two-body kinematics.** Each daughter receives momentum p = (m_χ/2)
  [1 − 2(ε₁² + ε₂²) + (ε₁² − ε₂²)²]^(1/2) (arXiv:2607.24910 Eq. 3 [src]);
  daughters are produced continuously, so their phase-space distribution
  is a sum of shells filled at the time of production (Eqs. 4–6). The
  2026 code fills a background momentum grid of 1000 bins, evenly spaced
  in ln q, as each production time is passed, and corrects for the
  momenta between the last filled bin and the current one [src: Sect.
  IV.1].
- **Closure.** The two-body analysis uses a shooting method on the
  budget equation [src: arXiv:2008.09615 Sect. III].

### Step 2. Add the collision terms to the perturbation equations
<!-- key: step-2-add-the-collision-terms-to-the -->

**Scattering with baryons (synchronous gauge, arXiv:1311.2937 Sect.
III.1 [src]).**

θ̇_χ = −𝓗θ_χ + c_χ²k²δ_χ + R_χ(θ_b − θ_χ),
θ̇_b = −𝓗θ_b + c_b²k²δ_b + R_γ(θ_γ − θ_b) + (ρ_χ/ρ_b)R_χ(θ_χ − θ_b),

with the temperatures

Ṫ_χ = −2𝓗T_χ + [2m_χ/(m_χ + m_H)] R′_χ (T_b − T_χ),
Ṫ_b = −2𝓗T_b + [2μ_b/(m_χ + m_H)](ρ_χ/ρ_b) R′_χ (T_χ − T_b) +
(2μ_b/m_e) R_γ (T_γ − T_b) (Eq. 13),

μ_b the mean molecular weight of the baryons and R_γ the Compton term.
The momentum-exchange rate is

R_χ = a c_n ρ_b σ₀ (m_χ + m_H)⁻¹ (T_b/m_H + T_χ/m_χ)^((n+1)/2) 𝓕_He
(Eq. 14), c_n = 2^((n+5)/2) Γ(3 + n/2)/(3√π) (Eq. 10),

which evaluates to c_n ≈ 0.27, 0.33, 0.53, 1, 2.1, 5, 13 for n = −4 to
+2 [src: Sect. II]. R′_χ (Eq. 15) is the thermalisation rate, equal to
R_χ for heavy dark matter. 𝓕_He (Eq. 16) corrects for scattering on
helium; it is ≈ 1 + 0.24(σ_He/σ₀ − 1) for dark matter heavier than
helium, plausible values are 4.6 (coherent) or 1.7 (incoherent), and the
paper sets σ_He = 0, 𝓕_He = 0.76, because 𝓕_He "involves some model
dependence" [src: Sect. III.2]. The dark-matter sound speed is dropped
as unimportant, and the calculation is limited to m_χ > MeV,
non-relativistic below z = 10⁹, with no direct photon coupling [src:
Sect. III.1]. The 2014 analysis modified CAMB; the later ones modify the
thermodynamics and perturbation modules of CLASS (Boddy et al. 2018,
arXiv:1808.00001 Appendix B [src]).

**Scattering with neutrinos (Newtonian gauge, arXiv:2607.15020 Eqs. 2–3
[src]).** The rate is μ̇ ≡ aσ_νχn_χ = (σ_Th/100 GeV) a u_νχ ρ_χ, and

θ̇_ν = k²ψ + k²(δ_ν/4 − σ_ν) − μ̇(θ_ν − θ_χ),
θ̇_χ = k²ψ − 𝓗θ_χ − (4ρ_ν/3ρ_χ) μ̇(θ_χ − θ_ν).

The factor 4ρ_ν/3ρ_χ is the momentum density ratio of the relativistic
partner. The 2026 simulations treat neutrinos as massless, stating that
masses have "only a minor effect on the final power spectrum" [src:
Sect. 2].

**Scattering with dark radiation (ETHOS, arXiv:1512.05344 Sect. II.1
[src]).** The dark-radiation equations (Eqs. 1–3) carry the opacity
κ̇_DR−DM on the dipole and α_l κ̇_DR−DM + β_l κ̇_DR−DR on the higher
multipoles; the dark-matter Euler equation (Eq. 8) carries κ̇_χ =
(4ρ_DR/3n_χm_χ) κ̇_DR−DM (Eq. 9). α_l (Eq. 6) encodes the angular
dependence of the matrix element, projected on Legendre polynomials
(Eq. 5). The dark-matter temperature obeys dT_χ/dτ = −2𝓗T_χ +
Γ_heat(T_DR − T_χ) (Eq. 11) and enters through c_χ² (Eq. 10). "The
particle physics details ... only enter through the opacity functions
... and through the coefficients α_l and β_l" [src: Sect. II.1].

### Step 3. Treat the relative bulk velocity (baryon scattering only)
<!-- key: step-3-treat-the-relative-bulk-velocity-baryon -->

The drag above is linear only while the dark matter–baryon relative
velocity V_χ is small against the thermal dispersion; the rms relative
velocity exceeds the baryon thermal velocity below z ≈ 10⁴, after which
the drag mixes Fourier modes (arXiv:1311.2937 Sect. III.2, Fig. 1
[src]). Three prescriptions are in use.

1. **Mean field, ΛCDM velocities** (2014): add V_RMS²/3 to the thermal
   term, R_χ → ... (T_b/m_H + T_χ/m_χ + V_RMS²/3)^((n+1)/2) (Eq. 18),
   with V_RMS² = ∫(dk/k) Δ_ξ [(θ_b − θ_c)/k]² (Eq. 17), Δ_ξ ≈ 2.4 × 10⁻⁹.
   The authors call it valid at z > 10⁴, reliable for n ≥ −2 (constrained
   at z ≫ 10⁴ by large-scale structure), and "likely conservative" for
   n ≤ −3, which the CMB constrains at z < 10⁴ [src: arXiv:1311.2937, Sect. III.2].
2. **Self-consistent, k-dependent** (2018 "main"): split the variance at
   each mode k* into V_flow²(k*) from k < k* (Eq. 4), which enters as a
   bulk flow through a confluent hypergeometric ₁F₁, and V_RMS²(k*) from
   k > k* (Eq. 5), which adds to the dispersion:
   R̃_χ = R_χ [1 + V_RMS²/(3v̄_th²)]^((n+1)/2) ₁F₁(−(n+1)/2, 5/2,
   −V_flow²/{2[v̄_th² + V_RMS²/3]}) (Eq. 7). The velocities are computed in
   the interacting cosmology, so the perturbation module is iterated,
   starting from the ΛCDM variance, to 1% convergence; k_max = 5 is
   "sufficient" for V_RMS to reach its high-z plateau; the
   thermodynamics module is inside the loop [src: arXiv:1808.00001 Sect.
   II.2, Appendix B]. A k-independent variant (Eq. 8) uses the
   self-consistent total variance only.
3. **Aggressive**: ignore the bulk velocity. Shown "for illustration
   only", as a floor on what an exact treatment could gain [src: Sect.
   IV.2].

### Step 4. Write the decay perturbations
<!-- key: step-4-write-the-decay-perturbations -->

- **Decay to dark radiation.** The decay term in the Boltzmann equation
  (Eq. 3) is not gauge invariant: "such a simple form of the decay rate
  is only valid in the gauge comoving with the decaying DM", a point the
  authors say an earlier bound overlooked; they therefore work in the
  synchronous gauge comoving with all the dark matter, valid for
  adiabatic initial conditions, where δ′_dcdm = −h′/2 and θ_dcdm = 0
  (Eqs. 12–13), and transform to the Newtonian gauge (Eqs. 14–17,
  Table 1) [src: arXiv:1606.02073 Sect. 2.2]. The dark radiation is
  followed through the integrated, Legendre-expanded distribution F_dr
  normalised by r_dr ≡ ρ̄_dr a⁴/ρ_cr,0 (Eqs. 18–21), which removes the
  time dependence from the background distribution [src].
- **Massive (warm) daughter.** The integration over momenta is not
  analytic, and following the full time- and momentum-dependent
  distribution "requires solving 𝒪(10⁸) linear differential equations";
  the 2020 analysis therefore switches to a viscous-fluid description of
  the daughter (first three multipoles) on sub-Hubble scales, kτ > 25,
  with 300 momentum bins, validated against 10⁴ bins and l_max = 17
  [src: arXiv:2008.09615 Sect. II, Appendix A].
- **Integral equations.** CLASSIER-DDM replaces the hierarchy by time
  integrals over metric sources along unperturbed geodesics, "requiring
  neither a Boltzmann hierarchy nor any fluid approximation"; a hundred
  perturbation momentum bins give 𝒪(0.1%) accuracy in P(k) to k ≈ 3
  Mpc⁻¹, with runtimes of about a minute [src: arXiv:2607.24910
  abstract, Sect. I].

### Step 5. Carry the linear result to the data
<!-- key: step-5-carry-the-linear-result-to-the-data -->

| Route | What is done | Stated reason | Source |
|---|---|---|---|
| Linear scales only | decay to radiation: limit to k ≲ 0.4–0.5 h/Mpc and use σ8 Ω_m^α from weak lensing rather than the full CFHT P(k) | halofit and the only N-body runs (all dark matter decaying, small boxes) disagree; "a safe bet" where all results agree | arXiv:1606.02073 Sect. 4.2.1 [src] |
| One-loop EFT of galaxy clustering | PyBird on the DCDM linear spectrum; BOSS fitted to k_max = 0.2 h/Mpc, EFT computed to k_nl = 0.7 h/Mpc; checked that the daughter free-streaming wavenumber k_fs exceeds k_max over most of the favoured region | "corrections should also be minor"; "an improved EFT treatment including the effect of the massive decay product would be necessary" to reach k_nl | Simon et al. 2022, arXiv:2203.07440 Sect. III, Appendix B [src] |
| Half-mode mapping to WDM simulations | compute T(k) = (P_collisional/P_CDM)^(1/2) in modified CLASS, match the half-mode scale to a thermal WDM transfer function, apply the WDM subhalo suppression as a survival probability per subhalo, fit the satellite luminosity function with a Poisson likelihood, flat prior on log M_hm, then map P(M_hm) to P(σ₀ | m_χ) | the suppression is "remarkably similar to that in WDM" and late-time interactions are expected to be small | Nadler et al. 2019, arXiv:1904.10000 Sect. III [src] |
| Dedicated hydrodynamical simulations | 48 P-Gadget3 runs (four u_νχ values chosen to cut off near 1.5, 2, 3, 4 keV WDM × 12 thermal histories), 2 × 1024³ particles in (20 Mpc/h)³, initial conditions from modified CLASS at z = 99; CDM runs reused; neural-network emulator (three layers of 60), error < 1.5%; Cobaya MCMC on the Boera et al. P1D at z = 4.2, 4.6, 5.0 to k_max = 0.2 s/km | to test the mapping rather than assume it | arXiv:2607.15020 Sects. 2–4 [src] |
| Halo mass function for decays | spherical collapse tracking decay mass loss: δ_c(M₀) between two plateaus (daughters retained or escaping), transition mass M₁ ∝ v_k³ Γ̃^(−1/2) t_ta where the kick equals the orbital velocity; validated on N-body at z = 0 and ≈ 1 | an efficient route to halo-mass-function probes | Montandon et al. 2026, arXiv:2607.19244 abstract [src] |

### Step 6. Sample
<!-- key: step-6-sample -->

- **Baryon scattering, CMB.** Planck 2015 TT, TE, EE (Plik lite) plus
  SMICA lensing; MontePython with MultiNest, checked against
  Metropolis–Hastings (R − 1 < 0.01); m_χ and f_χ fixed in most runs
  with seven free parameters and broad flat priors; when f_χ or m_χ is
  free, log-flat priors on it and on σ₀ "to sample the parameter space
  effectively" [src: arXiv:1808.00001 Sect. IV.1]. Excluding high-ℓ
  polarisation degrades the limits "by only a few percent" [src:
  footnote 6, citing earlier work].
- **Two-body decay.** −4 ≤ log₁₀ ε ≤ log₁₀ 0.5, −4 ≤ log₁₀(Γ/Gyr⁻¹) ≤ 1,
  0 ≤ Ω_dcdm^ini ≤ 1; log priors chosen "to ease comparison with earlier
  work" and called "more agnostic"; tension quantified with Q_DMAP
  (√Δχ² of the fit with and without the S8 point) and the evidence with
  MultiNest [src: arXiv:2008.09615 Sect. III, Appendix D].
- **Neutrino scattering, Lyα.** Uniform prior u_νχ ∈ [0, 2.4] × 10⁻⁷,
  matched to the simulated range "to avoid any extrapolation"; γ and
  τ_eff uniform over the simulated range; two thermal priors on (u₀, T₀),
  u₀ the cumulative heat injected per proton: a Gaussian prior on the
  CMB optical depth mapped onto (u₀, T₀) at z = 5.0, or Gaussian T₀
  priors per bin from independent temperature measurements [src:
  arXiv:2607.15020 Sect. 5].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Bulk-velocity prescription
<!-- key: bulk-velocity-prescription -->

- With all the dark matter interacting, the self-consistent prescription
  gives limits close to the ΛCDM-velocity one, because at the limit the
  interaction barely changes the velocity variance; ignoring the bulk
  velocity gives limits stronger by "more than an order of magnitude"
  for n = −4 [src: arXiv:1808.00001 Sect. IV.2].
- Reproducing the earlier prescription, the 2018 authors obtain limits a
  factor of about 1.8 weaker for n = −4 and 1.4 stronger for n = −2 than
  the earlier papers with the same likelihoods [src: arXiv:1808.00001, footnote 8]. An
  n = −4 or −2 limit therefore carries a prescription and code version.
- For an interacting sub-component the ΛCDM-velocity prescription
  "overestimates the relative bulk velocity and thus overly suppresses
  the interaction rate", so the self-consistent one is required [src:
  Sect. II.2].
- The 2014 mean-field rate (Eq. 18) against the thermal-only rate
  (Eq. 14) makes "a significant difference" only for n ≤ −3 [src:
  arXiv:1311.2937 Sect. III.2].

### Interacting fraction
<!-- key: interacting-fraction -->

For n = −4 at 1 MeV, the σ₀ limit scales roughly with f_χ for
f_χ ≳ 2%; below that the interacting part becomes tightly coupled, the
effect on the spectra saturates and the Planck limit disappears for
f_χ ≲ 0.4%, consistent with ≲ 0.6% from the helium constraint [src:
arXiv:1808.00001 Sect. IV.2]. A full-dark-matter limit is not a
sub-component limit scaled by 1/f_χ.

### Half-mode mapping against dedicated simulations
<!-- key: half-mode-mapping-against-dedicated-simulations -->

The dedicated-simulation limit u_νχ ≤ 1.5 × 10⁻⁸ maps to 5.1 keV (±5%
matching of the linear P(k)), 5.15 keV (half-mode, P/P_ΛCDM = 0.25) or
5.35 keV (δA criterion), while a dedicated WDM analysis of the same data
and pipeline gives m_WDM > 5.86 keV: "all three methods would lead to an
overestimation of the constraining power" [src: arXiv:2607.15020 Sect.
6]. The satellite DM–neutrino limit that the authors call comparable
was obtained by matching suppression scales to WDM simulations [src:
Sect. 6]. The dark acoustic oscillations of the linear input are
"completely washed out" in the flux power [src: Sect. 5].

### Hierarchy, fluid or integral equations for a warm daughter
<!-- key: hierarchy-fluid-or-integral-equations-for-a -->

| Method | Accuracy stated | Cost stated | Source |
|---|---|---|---|
| Full hierarchy, 10⁴ bins, l_max = 17 | reference | 𝒪(10⁸) equations for realistic analyses | arXiv:2008.09615 Sect. II, Appendix A [src] |
| Fluid on sub-Hubble scales (kτ > 25), 300 bins | CMB TT/EE well below 1%; P(k) a few percent, 2–3% at the smallest scales; S8 0.767 against 0.762 (0.65%) | used for the MCMC | arXiv:2008.09615 Sect. II, Appendix A [src] |
| Same fluid approximation, checked in 2026 | "percent-level deviations ... particularly on small scales"; does not capture the oscillations from daughter free streaming | — | arXiv:2607.24910 Appendix C [src] |
| Integral equations (CLASSIER-DDM) | sub-0.1% convergence in P(k) and C_L^φφ after a modest number of iterations | about 1 min per evaluation | arXiv:2607.24910 abstract [src] |

The 2020 authors judged the fluid error safe against the 1.8% S8 error
of the weak-lensing data of the time [src: arXiv:2008.09615 Appendix A];
the 2026 check matters at the precision of later surveys.

### Linear or log priors on decay parameters
<!-- key: linear-or-log-priors-on-decay-parameters -->

With linear priors over the original range one "would (wrongly) deduce
an upper limit only", while a restricted linear range or the log prior
finds ε and Γ non-zero at 2σ; moving the lower edge of the ε prior from
10⁻⁴ to 10⁻⁶ changes the 2D log-prior contours mildly and the 1D
posteriors little, and leaves Q_DMAP unchanged because it uses best fits
[src: arXiv:2008.09615 Appendix D].

### Thermal prior in the Lyα analysis
<!-- key: thermal-prior-in-the-lyalpha-analysis -->

The τ_CMB-based prior gives u_νχ < 1.5 × 10⁻⁸, the Gaussian-T₀ prior
< 2.03 × 10⁻⁸ (95%); the first pushes T₀ at z = 4.2 and 4.6 to the lower
edge of its prior through the u₀–T₀ anticorrelation [src:
arXiv:2607.15020 Sect. 5]. Matching the massless-neutrino spectrum to a
Σm_ν = 0.06 eV one gives an estimated ≤ 2.0 × 10⁻⁸ [src: Sect. 6].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Transition of relative velocity above thermal | z ≈ 10⁴ | DM–baryon | arXiv:1311.2937 | Sect. II, Fig. 1 |
| ΛCDM relative-velocity variance | ⟨V_cb²⟩ ≈ 10⁻⁸ (c = 1) at z > 10³, then ∝ (1 + z)² | DM–baryon | arXiv:1808.00001 | Sect. II.2 |
| Iteration convergence; k_max for velocities | 1%; 5 | DM–baryon, CLASS | arXiv:1808.00001 | Appendix B |
| Recombination switch | full T_b evolution from z ≈ 10⁴ instead of z ≈ 850 | DM–baryon | arXiv:1808.00001 | Appendix B |
| Planck 2015 σ₀ (95%), 1 MeV | 1.7 × 10⁻⁴¹ cm² (n = −4), 2.3 × 10⁻³³ cm² (n = −2); flat in m_χ below 10 MeV | DM–proton | arXiv:1808.00001 | Table 1 |
| CMB-S4-like forecast, 1 MeV | 5.8 × 10⁻⁴² and 1.0 × 10⁻³³ cm² (**forecast**; experiment cancelled, see `surveys-and-data.md#what-comes-next`) | DM–proton | arXiv:1808.00001 | Sect. IV.2 |
| Fraction below which Planck limits vanish | f_χ ≲ 0.4% | n = −4 | arXiv:1808.00001 | Sect. IV.2 |
| Satellite half-mode limit behind the DM–baryon limits | M_hm < 3.1 × 10⁸ M⊙, k_hm > 36 h/Mpc (95%) | DM–baryon | arXiv:1904.10000 | Sect. III |
| WDM-equivalent mass | m_WDM = 2.32 (Ω_m/0.25)^0.4 (h/0.7)^0.8 (M_hm/10⁹ M⊙)^(−0.3) keV (Eq. 8) | conversion | arXiv:1904.10000 | Sect. IV |
| Lyα simulation grid | 4 u_νχ × 12 thermal histories = 48; 5000 sightlines per box | DM–ν | arXiv:2607.15020 | Sect. 3 |
| u_νχ prior; limits | [0, 2.4] × 10⁻⁷; < 1.5 × 10⁻⁸ (τ prior), < 2.03 × 10⁻⁸ (T₀ prior) | DM–ν | arXiv:2607.15020 | Sect. 5 |
| Earlier preferred u_νχ | ~5 × 10⁻⁶ (Lyα), 2–4 × 10⁻⁵ or 2 × 10⁻⁶–10⁻⁴ (CMB + BAO), ~2 × 10⁻⁴ (with DES Y3) | DM–ν | arXiv:2607.15020, quoting others | Sect. 6 |
| Two-body S8 best fit | Γ⁻¹ ≈ 55 Gyr, ε ≈ 0.7%; degeneracy Γ⁻¹ ≈ 55 (ε/0.007)^1.4 Gyr | DCDM → WDM + DR, with S8 prior | arXiv:2008.09615 | Sect. III |
| Effect of the S8 prior | Q_DMAP 2.7σ (ΛCDM) → 1.3σ; Δln B = −0.81; no preference without the prior | same | arXiv:2008.09615 | Sect. III |
| Non-linear cut, decay to radiation | k ≲ 0.4–0.5 h/Mpc | DCDM → DR | arXiv:1606.02073 | Sect. 4.2.1 |
| EFT ranges | k_max = 0.2 h/Mpc (BOSS fit), k_nl = 0.7 h/Mpc | DCDM | arXiv:2203.07440 | Appendix B |

The 1.7 × 10⁻⁴¹ cm² and 2.3 × 10⁻³³ cm² values (arXiv:1808.00001, Table 1) are velocity-dependent
coefficients with v in units of c; they are not comparable with the
velocity-independent limits in `results.md`.

## What goes wrong
<!-- key: what-goes-wrong -->

- **Recombination-code glitch.** Generalising the linearised T_b ≈ T_γ
  approximation that Recfast and HyRec use above z ≈ 850 to include
  DM–proton heat exchange "can lead to significant numerical glitches"
  that "artificially enhance" the effect on the CMB. Test: solve the
  full T_b equation from z ≈ 10⁴ and compare both recombination codes
  (arXiv:1808.00001 Appendix B [src]).
- **Ignoring mode coupling.** A limit computed with the bulk velocity
  switched off is too strong by more than ten for n = −4. Test: state
  the prescription; compare with the self-consistent one (Sect. IV.2).
- **Sub-component with ΛCDM velocities.** Too-weak coupling, hence wrong
  limits at small f_χ (Sect. II.2).
- **Gauge of the decay term.** The simple decay term is valid only in
  the gauge comoving with the decaying matter (arXiv:1606.02073 Sect.
  2.2). Test: derive in that gauge, then transform.
- **Truncation and fluid artefacts.** A truncated hierarchy can produce
  numerical artefacts if l_max is too low; the fluid approximation
  misses free-streaming oscillations (arXiv:2607.24910 Sect. I,
  Appendix C [src]). Test: one high-precision run (l_max = 100,
  N_q = 1000 was used) at the best fit.
- **Prior that hides or creates a detection.** Linear priors over a wide
  range can turn a 2σ preference into an upper limit; a log prior
  depends on its lower edge (arXiv:2008.09615 Appendix D).
- **Preference that comes from one prior.** The two-body model fits S8
  only when the S8 prior is included (arXiv:2008.09615 Sect. III);
  `systematics.md#sub-component-axions-decays-the-x-ray-line` has the
  profile-likelihood counterpart.
- **Degeneracies to report.** σ₀ with n_s (positive), weakly with A_s,
  τ, Ω_χh² and h (arXiv:1808.00001 Sect. IV.2); Γ with ε
  (arXiv:2008.09615); decay with Σm_ν, lifted by current data
  (arXiv:1606.02073 Sect. 3.3 [src]).
- **Extrapolating an emulator.** Avoided by matching the prior to the
  simulated range (arXiv:2607.15020 Sect. 5).
- **Applying halofit to decays.** It gives more small-scale power than
  ΛCDM where the only simulations give less (arXiv:1606.02073 Sect.
  4.2.1). Test: scale cut, or the EFT with a free-streaming check.
- **Validation used in the Lyα analysis.** Reproduce the CDM-limit
  result of the WDM pipeline with each prior; the limit is stated to
  hold "even under our weakest assumptions for the astrophysical
  parameters or when removing the smallest-scale bins" (arXiv:2607.15020
  Sects. 5–6 [src]).

## Reading list
<!-- key: reading-list -->

- Foundation, baryons: Dvorkin, Blum & Kamionkowski 2014,
  arXiv:1311.2937 — drag force, c_n, R_χ, helium, Boltzmann equations.
- Method, baryons: Boddy et al. 2018, arXiv:1808.00001 — relative bulk
  velocity prescriptions, iteration in CLASS, sub-component limits.
- Foundation, dark radiation: Cyr-Racine et al. 2016, arXiv:1512.05344 —
  ETHOS opacities and angular coefficients.
- Application, neutrinos: Mosbech et al. 2026, arXiv:2607.15020 —
  dedicated Lyα simulations, priors, test of WDM mappings.
- Method, small scales: Nadler et al. 2019, arXiv:1904.10000 — half-mode
  mapping onto satellite counts.
- Foundation, decays: Poulin, Serpico & Lesgourgues 2016,
  arXiv:1606.02073 — gauge-correct equations, scale cut.
- Method, warm daughter: Franco Abellán et al. 2020, arXiv:2008.09615 — fluid
  approximation, priors, S8 test.
- Method, non-linear: Simon et al. 2022, arXiv:2203.07440 — EFT of
  galaxy clustering for decaying models.
- Code and critique: Lee et al. 2026, arXiv:2607.24910 — integral
  equations, test of the fluid approximation.
- Halo mass function: Montandon et al. 2026, arXiv:2607.19244 (abstract).

## Not verified
<!-- key: not-verified -->

- The Gluscevic & Boddy 2017 (arXiv:1712.07133) and earlier n = 0
  implementations: no body rendering available; the limits are in L2.
- The ACT DR6 sections named in "From" (VI.4.1, VI.5.2) were not read
  for this dossier.
- Mosbech et al. quote the Planck optical depth as τ = 0.054 ± 0.0007
  (Sect. 5); Planck 2018 gives τ = 0.0544 ± 0.0073 (arXiv:1807.06209,
  Sect. 3), an error ten times larger. The paper does not comment on it;
  whether its τ prior used the printed width was not checked.
- The numerical value of 𝓕_He used by the 2018 and 2026 analyses was
  not read; the 2014 value is 0.76 (arXiv:1311.2937, Sect. III.2).
- The dark-radiation hierarchy equations for ℓ ≥ 2 of arXiv:1606.02073
  (after Eq. 21) were not read.
- The constraints paper that uses CLASSIER-DDM (companion of
  arXiv:2607.24910) was not identified.
- The Montandon et al. 2026 halo-mass-function framework was read at
  abstract level only.
