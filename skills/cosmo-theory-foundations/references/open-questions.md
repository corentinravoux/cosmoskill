# Theory foundations — where the community is split on a convention or a model, and misconceptions

Snapshot: 2026-10-26

## 1. h⁻¹Mpc units and σ8 versus σ12
<!-- key: h-1mpc-units-and-sigma8-versus-sigma12 -->

**The proposal.** Sánchez 2020, arXiv:2002.07829, proposes "to abandon the traditional h⁻¹Mpc units in the analysis of new surveys" and to replace σ8 by σ12, the linear rms fluctuation in spheres of 12 Mpc [src: abstract]. His own demonstration (ΛCDM, the same wide priors for all three data sets) [src: Sect. IV]:

| Combination | Planck | DES 3×2pt | BOSS |
|---|---|---|---|
| S12 = σ12 (ω_m/0.14)^0.4 | 0.815 ± 0.013 | 0.798 ± 0.043 | 0.716 ± 0.047 |

In (ω_m, σ12) "the constraints inferred from DES and Planck are in excellent agreement", while "BOSS data prefer lower values of σ12". The data are the 2018–2019 releases; the numbers are an illustration of the effect of the convention, not current constraints.

**The other side.** The same paper states that "using h⁻¹Mpc or Mpc units yields identical cosmological constraints": the units carry no information, and a full-modelling fit that varies h is unaffected. What is affected is (i) any compressed quantity quoted as σ8 or fσ8 from a fit with fixed template, and (ii) any comparison of σ8 between experiments with different h posteriors. The community has not adopted σ12: every collaboration result gathered in the sibling skills (`cosmo-weak-lensing`, `cosmo-galaxy-clustering`, `cosmo-cmb`) is still quoted as σ8 or S8, and the survey table in `surveys-and-data.md` records what each one does.

**Rule of judgment.** Comparing two S8 or σ8 values is safe when both come from chains that sample h (the comparison is then between posteriors of the same derived parameter). It is unsafe when one of them is a template-fit fσ8 at fixed h, or when the h posteriors are very different in width (lensing-only against CMB).


**2026 evidence for fσ12.** The Euclid Collaboration's study of simulated catalogues in non-standard cosmologies (Euclid Collaboration 2026, arXiv:2603.13148) reports that "across a wide range of models, the linear growth rate multiplied by the matter density within spheres of radius 12 Mpc, fs12, exhibits a notable robustness to the choice of cosmological template", extended to "scenarios with markedly distinct gravitational or dark energy dynamics"; it also warns that most of the scatter in inferred parameters appears already with the correct template, and that deviations are "often … much larger than error bars" [src, abstract]. So Euclid's template-fit work is moving to σ12 while DESI defines σ_s8 through r_d^fid: two different repairs of the same problem, and a compilation will have to carry both.

## 2. EFTofLSS priors, bias bases and projection effects
<!-- key: eftoflss-priors-bias-bases-and-projection -->

**The debate.** One-loop EFT fits carry seven to ten nuisance parameters per tracer (in the DESI DR1 baseline: b1, b2, b_s, with b3 fixed, three counterterms and three stochastic terms; Adame et al. 2024, arXiv:2411.12021). Several are weakly constrained, so the marginal posteriors of cosmological parameters depend on the nuisance priors and on the parameter basis in which those priors are flat or Gaussian.

- DESI's own mitigation is to sample bias with σ8 attached, {(1+b1)σ8, b2σ8², b_sσ8²}, because "this parameterisation represents better the signal in the data and hence reduces volume effects", to drop the hexadecapole, and to take only full modelling to the cosmology paper since "projection effects can impact how the compressed parameters of the ShapeFit method are interpreted" [src, arXiv:2411.12021 Sect. 4.7].
- Bonici et al. 2026 (arXiv:2607.02498) reanalyse the DESI DR1 multipoles: with baseline priors, DESI + BBN + n_s constraint shows "multi-σ projection in the Hubble parameter H0 and dark energy equation of state parameters w0 and wa"; a Jeffreys prior over all EFT coefficients "recenters these posteriors to enclose the maximum a posteriori estimate within the 68% credible regions"; a hybrid Jeffreys + Gaussian configuration is their preferred choice, and the result agrees with HOD-informed priors and with frequentist profile likelihoods "in both central values and degeneracy directions in the w0–wa plane" [src, abstract].
- The size of the effect in extended models (best fit against posterior mean) and the simulation-based-prior results are tabulated in `cosmo-galaxy-clustering`; the statistical side (profile likelihood, prior-volume effects) in `cosmo-statistics-inference`.

**The two early BOSS analyses already showed the dependence.** With n_s and Ω_b/Ω_c fixed, D'Amico et al. 2020 (arXiv:1909.05271) found ln(10¹⁰A_s) = 2.72 ± 0.13, Ω_m = 0.309 ± 0.010, H0 = 68.5 ± 2.2; with a BBN prior on ω_b, fixed tilt and neutrino masses varied in a tight range, Ivanov, Simonović & Zaldarriaga 2020 (arXiv:1909.05277) found H0 = 67.9 ± 1.1, Ω_m = 0.295 ± 0.010, σ8 = 0.721 ± 0.043 [src: abstract of each]. Same data, same theory order, different priors and codes; the low σ8 of that generation is treated as superseded in `cosmo-galaxy-clustering`.

**Bias bases.** The second-order non-local term can be written with s_ij s_ji or equivalently with θ − δ (McDonald & Roy 2009, arXiv:0902.0991), with the Galileon operators of Assassi et al. 2014 (arXiv:1402.5916), or with a Lagrangian shear bias b_s (velocileptors). The numerical values of "b2" and "the tidal bias" are not comparable between papers without the conversion, which this session did not read at source (see "Not verified" in `physics-and-methods.md`).

**Where the frontier is.** Higher-point functions in the EFT (territory of `cosmo-beyond-two-point`), hybrid N-body + bias expansions, and differentiable one-loop codes (Kobayashi & Akitsu 2026, arXiv:2610.08023: relative numerical error of order 0.01% at k ≲ 1 h/Mpc against brute-force integration, a statement about the integrals, not about the validity of one-loop theory) [src, abstract]. Ivanov 2026 (arXiv:2607.28314) is the current pedagogical entry point: counterterms, renormalisation, IR resummation and its relation to the equivalence principle, bias, redshift-space stochasticity, Lagrangian perturbation theory.


**A unit-based explanation, October 2026.** Pezzotta et al. 2026 (arXiv:2610.08751) argue that the prior-volume effects "are largely driven by imposing priors on the model parameters defined in Mpc/h units, thereby introducing a spurious correlation with the Hubble parameter h", and that priors in Mpc reduce the shifts on Stage-IV synthetic data "from several standard deviations to well within 1σ", with a performance "comparable to that of alternative mitigation strategies, such as the adoption of invariant priors or the reparametrisation of nuisance parameters"; within the reparametrisation route, "using σ12 in place of the commonly adopted σ8 … improves the performance" [src, abstract; synthetic data, so a **forecast**-type result]. This ties the projection-effect debate to the unit debate of section 1; it has not been applied to DESI data in the papers read here.

**Counterterms as physics or as nuisance.** Ivanov, Simonović & Zaldarriaga relate the quadrupole counterterm to a velocity dispersion but stress that "the true amplitude (and even the sign) of the counterterms cannot be predicted" (arXiv:1909.05277). Chen & Aviles 2026 (arXiv:2609.35757) ask whether fingers of God can be resummed into a damping function and answer "potentially, but at the cost of significantly expanding the operator basis and promoting free coefficients to free functions" [src, abstract]. Informative priors on these terms, from simulations or HOD models, are therefore a modelling assumption about small-scale velocities, not a derivation. A first measurement of where the counterterms come from: relating the effective stress tensor to individual haloes in N-body simulations, Hebbar, de S. Nascimento & Banerjee 2026 (arXiv:2610.19001) find that haloes above 10^12 M_⊙/h account for "∼95%, ∼85%, and ∼70%" of the background pressure, effective sound speed and shear viscosity, "depending on the EFT cutoff scale", dominated by cluster-scale haloes of 10^14–10^15 M_⊙/h, and present this as a route to "physics-informed priors" [src: abstract]. That concerns the dark-matter counterterms; it does not yet fix the galaxy or redshift-space ones.

## 3. Compressed versus full-modelling parameters
<!-- key: compressed-versus-full-modelling-parameters -->

Three routes from a measured P_ℓ(k) to cosmology coexist, and they do not return the same parameter (DESI DR1 full shape, Adame et al. 2024, arXiv:2411.12021, Sect. 4.2):

| Route | What is fitted | Fiducial cosmology enters through |
|---|---|---|
| Standard compression (BOSS, eBOSS) | α_∥, α_⊥, fσ8 per redshift bin | distances, the template shape, the one-loop terms, and the 8 h⁻¹Mpc radius |
| ShapeFit (Brieden, Gil-Marín & Verde 2021, arXiv:2106.07641) | α_∥, α_⊥, f (quoted as fσ_s8), slope m | the same, with an approximate correction of the one-loop terms |
| Full modelling | the cosmological parameters themselves | distances only (corrected by q_∥, q_⊥) |

ShapeFit's own claim is that one extra effective parameter captures "the same amount of information as the full modelling approach, but in a model-independent way" [src, abstract of arXiv:2106.07641]; the DESI comparison of velocileptors, PyBird and FOLPSν found that the theories "give consistent constraints in both the forward-modeling and ShapeFit compressed fitting approaches" on AbacusSummit mocks (Maus et al. 2024, arXiv:2404.07272, abstract).

What remains open is interpretation, not agreement. A compressed fσ8 is model-independent only to first order: "at higher-order corrections, this is no longer exact" (arXiv:2411.12021). An fσ_s8 is not an fσ8 until rescaled by q_iso; a compilation plot that mixes BOSS/eBOSS fσ8, DESI fσ_s8 and peculiar-velocity fσ8 (the last obtained at z < 0.1 with a different treatment of the amplitude, see `cosmo-peculiar-velocities`) mixes three definitions. Brieden et al. 2022 (arXiv:2204.11868) is the model-agnostic reanalysis of BOSS + eBOSS with this compression: h = 0.6816 ± 0.0067, Ω_m = 0.3001 ± 0.0057, σ8 = 0.858 ± 0.036 in flat ΛCDM with a BBN prior and Lyα BAO [src, abstract]. That σ8 is higher than the 0.721 ± 0.043 obtained from BOSS with an EFT full-modelling fit by Ivanov, Simonović & Zaldarriaga (2020, arXiv:1909.05277, abstract) [src]: same survey family, different route and priors (section 2).

## 4. Non-linear prescriptions and baryons
<!-- key: non-linear-prescriptions-and-baryons -->

The two Stage-III lensing collaborations did not use the same non-linear matter spectrum, and the choice moves S8.

- DES Y3: halofit (Takahashi et al. 2012, arXiv:1208.2701) with the Bird et al. 2012 (arXiv:1109.4416) neutrino correction, gravity only, baryons removed by scale cuts (Krause et al. 2021, arXiv:2105.13548).
- KiDS-Legacy: HMCode2020 (Mead et al. 2021, arXiv:2009.01858) with a free feedback parameter (Wright et al. 2025, arXiv:2503.19441).
- KiDS-Legacy's own statement of the consequence: halofit "tends to overestimate power for lower values of S8, resulting in an underestimated S8 value", and HMCode2020 gives "a slightly higher S8" than HMCode2015 [src, arXiv:2503.19441 Sect. 2.2].

The quoted accuracies are of different kinds and should not be compared as if they were one number: revised halofit, 5% at k ≤ 1 h/Mpc and 10% at 1–10 h/Mpc against its own 16 WMAP-like simulations (arXiv:1208.2701, abstract); HMcode-2015, ≃5% at k ≤ 10 h/Mpc, z ≤ 2 (arXiv:1505.07833, abstract); HMcode-2020, RMS 2.5% at k < 10 h/Mpc, z < 2 with worst cases up to 16% (arXiv:2009.01858, abstract). Each is a fit error against a simulation set of limited cosmological range, not an error against the truth; the emulator and N-body floor is in `cosmo-simulations-mocks`, and the disputed strength of baryonic feedback, which dominates at k ≳ 1 h/Mpc, in `cosmo-weak-lensing`.

The halo model itself remains a calibrated description, not a derivation. Its ingredients carry their own errors: the mass function is known to ≲5% at z = 0 and is not universal (its amplitude falls 20–50% from z = 0 to 2.5, Tinker et al. 2008, arXiv:0803.2706); the bias fit has ~6% scatter and depends on the halo definition at the 10% level (Tinker et al. 2010, arXiv:1001.3162); the transition between the one- and two-halo terms is the long-standing weak point, for which a model with haloes defined by orbiting particles reports ≈2% accuracy on the halo–mass correlation over 0.1–50 h⁻¹Mpc (Salazar et al. 2024, arXiv:2406.04054) [src: abstract of each].

## 5. Neutrino treatment
<!-- key: neutrino-treatment -->

Analyses that are combined routinely do not treat neutrinos alike (each read at source, `surveys-and-data.md`):

| Choice | Who | Source and place |
|---|---|---|
| One massive state of 0.06 eV, two massless, N_eff = 3.046 | Planck 2013 and 2018 | arXiv:1303.5076, Sect. 2.1.1; arXiv:1807.06209, Sect. 2.1 |
| 0.06 eV in one massive state | ACT DR6; DESI DR2 when Σm_ν is fixed | arXiv:2503.14452, Sect. 7.1; arXiv:2503.14738, Sect. V |
| Three degenerate states | DESI DR2 when Σm_ν is varied | arXiv:2503.14738, Sect. V |
| Σm_ν fixed to 0.06 eV | KiDS-Legacy | arXiv:2503.19441, Sects. 2.2 and 5.1 |
| Σm_ν varied in the baseline | DES Y3 | arXiv:2105.13549, Sect. IV.2 and Table 1 |
| N_eff = 3.044 | DESI DR1 full shape and DR2 | arXiv:2411.12021, Sect. 4.7; arXiv:2503.14738, Sect. IV.1 |

- **Does it matter?** For r_d, no paper giving the effect of 3.044 against 3.046 was read. For S8 the choice between fixing and marginalising Σm_ν moves the marginal posterior: the DES Y3 modelling paper shows (Ω_m, S8) posteriors from noiseless synthetic data "assuming massless neutrinos" and "marginalizing over neutrino mass", with different offsets from the input (Krause et al. 2021, arXiv:2105.13548, Fig. 2 caption) [src]. A comparison of a KiDS S8 (fixed mass) with a DES S8 (marginalised mass) contains this difference; it is a prior effect, not a physical disagreement.
- **Which field.** Simulations settle that bias and the mass function are universal in the cb field (arXiv:1311.1212; arXiv:1311.0866). What is not uniform is the reported amplitude: Planck's σ8 is total matter, DESI's "excluding neutrinos" (arXiv:2411.12021). No paper read here converts between the two explicitly.
- **Growth.** With massive neutrinos the growth rate is scale-dependent at the 0.3–2% level (arXiv:1708.01154), so "f(z)" and a single growth index are approximations; the definition of fσ8 through velocity–density correlations (arXiv:1807.06209, Eq. 27) survives, the product f × σ8 does not.
- **Geometry against growth.** Ge et al. 2026 (arXiv:2610.20977) split Σm_ν "at the Boltzmann-code level": one parameter "sets H(z) for distance computation", the other "sets H(z) for perturbation evolution", both extended to negative values; the difference of the two "is a null test of the ΛCDM model, passed by current data at 0.4σ level" (Planck, ACT and SPT lensing, DESI BAO) [src: abstract]. A neutrino-mass result quoted from such a fit is a different parameter from the single Σm_ν of the rows above.
- The bounds on Σm_ν, the effective (negative) mass and the role of τ are in `cosmo-neutrinos-dark-matter`.

## 6. Relativistic effects: detectability
<!-- key: relativistic-effects-detectability -->

- The complete linear expression for the observed number counts exists in three independent derivations that agree: Yoo, Fitzpatrick & Zaldarriaga 2009 (arXiv:0907.0707), Bonvin & Durrer 2011 (arXiv:1105.5280) and Challinor & Lewis 2011 (arXiv:1105.5292). What is open is whether any term beyond density, RSD and magnification is detectable, and with which estimator.
- Odd multipoles are already detected in BOSS DR12, but as a wide-angle and window effect of the end-point line of sight, not as a relativistic signal (Beutler, Castorina & Zhang 2019, arXiv:1810.05051).
- For f_NL the terms are not optional. A Fisher analysis for a SPHEREx-like survey reaching σ(f_NL) ~ 1 finds that "neglecting the relativistic and wide-angle contributions shifts the recovered f_NL by an amount of order its own uncertainty" (Lukens & Jeong 2026, arXiv:2608.18334, **forecast**) [src, abstract].
- Estimators are still being rewritten: the Yamamoto estimator is optimal only in the plane-parallel limit; the optimal wide-angle estimator is a two-ℓ generalisation whose exact window function is a finite sum computable with FFTs, with "order-unity improvements in the signal-to-noise ratio of ultra-large-scale power spectrum measurements" (Sailer et al. 2026, arXiv:2607.05513) [src, abstract].
- A practical threshold from a full-sky calculation of density, velocity and ellipticity correlations: wide-angle corrections "become non-negligible for opening angles Θ ≳ 30°" (Mikura et al. 2026, arXiv:2608.19039) [src, abstract]. The peculiar-velocity case, where the samples are nearby and the angles large, is in `cosmo-peculiar-velocities`.

## 7. Which ruler: the sound horizon or the equality scale
<!-- key: which-ruler-the-sound-horizon-or-the-equality -->

BAO anchor distances to r_d, which is fixed by pre-recombination physics; the broadband turnover of P(k) is fixed by matter–radiation equality. Brieden, Gil-Marín & Verde 2023 (arXiv:2212.04522) measure H0 both ways from BOSS + eBOSS with a BBN prior, in ΛCDM [src, abstract]:

| Route | Anchor | H0 (km/s/Mpc) |
|---|---|---|
| BAO + BBN | sound horizon | 67.42 +0.88/−0.94 |
| shape + BBN | equality scale | 70.1 ± 2.1 |

They call these "the tightest sound-horizon free H0 constraints from LSS data to date" and conclude that an extension of ΛCDM meant to solve the Hubble tension "needs to modify consistently not only the sound horizon scale physics, but also the matter-radiation equality scale". For this skill the point is definitional: the ShapeFit slope m and an EFT full-shape fit carry equality-scale information, a BAO fit does not, and a quoted "H0 from LSS" must say which ruler it used. Status of the Hubble tension: `cosmo-distance-ladder-h0`, `cosmo-tensions-anomalies`.

## 8. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

- **Stage-IV precision removes the slack.** Approximations that were harmless at Stage III are not: Limber, neglected RSD in angular clustering and a poorer non-linear spectrum each bias Roman and Rubin 3×2pt by 1σ or more (arXiv:2606.23781, **forecast**); priors in Mpc/h shift full-shape posteriors by several σ on Stage-IV synthetic data (arXiv:2610.08751, **forecast** setting); relativistic and wide-angle terms shift f_NL by about 1σ for SPHEREx (arXiv:2608.18334, **forecast**).
- **Amplitude parameter.** Euclid's preparation papers work with fσ12 (arXiv:2603.13148) and a σ12-based emulator exists (arXiv:2511.13826); DESI uses σ_s8. Whether the first Stage-IV cosmology releases quote σ8, σ12 or both will decide if compilations need a conversion layer. The release calendar is in `cosmo-surveys-facilities` and `cosmo-galaxy-clustering`.
- **Compression.** eBOSS already judged that its compression "might not be the best approach for future surveys including DESI and Euclid" (arXiv:2007.08991); DESI took full modelling to its cosmology paper. If full-survey DESI and Euclid results are published only as full-modelling posteriors, model-independent fσ8-type points will stop being produced, and growth compilations will end at the DR1-era points.
- **Halo-model and non-linear theory.** HMcode-2020's 2.5% (arXiv:2009.01858, abstract) and the emulators' ~1% (`cosmo-simulations-mocks`) are above what Stage-IV shear needs on k ~ 1 h/Mpc; baryonic feedback is the limiting uncertainty (`cosmo-weak-lensing`).

## 9. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

Each line gives the claim, then what the source read this session says.

| Claim that circulates | Correction | Source |
|---|---|---|
| "γ = 0.55 is the prediction of general relativity" | it is the ΛCDM value; γ = 0.55 + 0.05[1 + w(z=1)] | arXiv:astro-ph/0507263, Eq. 17 |
| "f = Ω_m^0.6" | pre-2005 convention; "a needless 6% error in β" against Ω_m^0.55 (arXiv:astro-ph/0701317, Sect. III) | arXiv:astro-ph/9708102; arXiv:astro-ph/0507263; arXiv:astro-ph/0701317 |
| "BAO measure H0" | BAO alone measure Ω_m and h r_d; H0 needs r_d from BBN or the CMB and standard pre-recombination physics | arXiv:2503.14738 |
| "The sound horizon is 147 Mpc" (for the CMB) | r_drag = 147.09 Mpc, r_* = 144.43 Mpc (arXiv:1807.06209, Table 2); the Eisenstein–Hu value is higher by the factor 1.0275 (arXiv:1303.5076, Sect. 5.2) | arXiv:1807.06209; arXiv:1303.5076 |
| "θ_MC is the acoustic angle" | "an approximation to θ_*"; 100θ_MC = 1.04092 ± 0.00031 against 100θ_* = 1.04110 ± 0.00031 (arXiv:1807.06209, Table 2) | arXiv:1303.5076; arXiv:1807.06209 |
| "σ8 is the fluctuation at 8 Mpc" | 8 h⁻¹Mpc, a radius in Mpc that depends on h; σ12 uses spheres of 12 Mpc (arXiv:2002.07829, abstract) | arXiv:1303.5076; arXiv:2002.07829 |
| "σ8 means the same thing in Planck and DESI" | total matter against "excluding neutrinos" | arXiv:1303.5076; arXiv:2411.12021 |
| "fσ8 is model-independent" | exact only at first order; depends on the fixed h and template; DESI's quantity is fσ_s8 | arXiv:2002.07829; arXiv:2411.12021 |
| "Working in h⁻¹Mpc loses or adds information" | constraints are identical if h is carried through; what changes is σ8, fixed-template fits, and priors | arXiv:2002.07829; arXiv:2610.08751 |
| "Ω_k > 0 is a closed universe" | open, in the Hogg and DESI sign convention (sinh branch) | arXiv:astro-ph/9905116; arXiv:2503.14738 |
| "D_H is c/H0" in a BAO table | D_H(z) = c/H(z) | arXiv:2503.14738; arXiv:1411.1074 |
| "Limber is safe above ℓ of a few tens" | true for shear; for tomographic clustering it biases Stage-IV analyses, and ℓ + 1/2 is required | arXiv:0809.5112; arXiv:1911.11947; arXiv:2606.23781 |
| "Eisenstein–Hu gives the BAO wiggles" | 10% accuracy (abstract), "order unity residuals" in the oscillation phase at small scales (Sect. 3.3) | arXiv:astro-ph/9709112 |
| "halofit is accurate at the per-cent level" | 5% to k = 1 h/Mpc, 10% to 10 h/Mpc (arXiv:1208.2701, abstract); biases S8 low (arXiv:2503.19441, Sect. 2.2) | arXiv:1208.2701; arXiv:2503.19441 |
| "The fingers-of-God σ is the galaxy velocity dispersion" | a pairwise dispersion, √2 larger; and the damping form is phenomenological | arXiv:astro-ph/9708102; arXiv:2609.35757 |
| "EFT counterterms are measurable small-scale physics" | "the true amplitude (and even the sign) … cannot be predicted" | arXiv:1909.05277 |
| "One-loop EFT is valid to k = 0.3 h/Mpc" | stated for real space and BOSS volume (arXiv:1909.05277, Sect. 3.1); DESI fits to 0.20 h/Mpc in redshift space (arXiv:2411.12021, Sect. 4.7) | arXiv:1909.05277; arXiv:2411.12021 |
| "Bias parameters can be compared across papers" | tidal bias differs by a factor 2 and b1 by 1 between bases | arXiv:2404.07272 |
| "Halo bias depends on mass only" | at fixed mass the oldest 10% of 10^11 M_⊙/h haloes are over 5 times more correlated than the youngest | arXiv:astro-ph/0506510, abstract |
| "Neutrinos suppress P(k) by 8 f_ν" | only on small linear scales, at fixed ω_m, for f_ν < 0.07 | arXiv:astro-ph/0603494, Sect. 4.5.6 |
| "Projection effects are a bias in the data" | a property of marginal posteriors under given priors; the MAP is unaffected | arXiv:2105.13548; arXiv:2607.02498 |
| "A measured dipole of P(k) is a relativistic signal" | the end-point line of sight generates odd multipoles through wide-angle and window terms | arXiv:1810.05051 |
| "N_eff = 3.046 is simply wrong" | 3.044 is the current standard (`cosmo-neutrinos-dark-matter`), but Planck 2013 and 2018 chains were run with 3.046: describing them requires that number | arXiv:1303.5076, abstract; arXiv:1807.06209, abstract |

Stale values to recognise: the S12 numbers of Sánchez 2020 (2018–2019 data); r_d = 147.49 ± 0.59 Mpc (Planck 2013, arXiv:1411.1074, Sect. II.2); the low σ8 of the first BOSS EFT fits (arXiv:1909.05277), superseded as described in `cosmo-galaxy-clustering`; β values with exponent 0.6 (arXiv:astro-ph/9708102).

## Not verified
<!-- key: not-verified -->

- Whether any collaboration has adopted σ12 for a data release: none of the analyses read does; a systematic search was not made.
- The size of the DES Y3 S8 shift between fixed and marginalised Σm_ν: only the figure caption was read, not the numbers. The prior itself is now read: flat 10³ Ω_ν h² ∈ (0.60, 6.44) (arXiv:2105.13549, Table 1) [src]; `surveys-and-data.md` section 6.
- Whether the Pezzotta et al. Mpc-prior result holds on DESI data: the paper uses synthetic data, and no application to data was found.
- Independent confirmations of the Brieden et al. equality-scale H0 with DESI data: found among recent titles by the second pass of this build but not read, and not cited here.
- Community positions on bias-basis standardisation (a common basis for DESI, Euclid and Rubin codes): no paper proposing one was read.
