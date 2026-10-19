# The baryon density from BBN and its use as a prior — cosmo-bbn dossier

Scope: how a light-element baryon density is turned into a prior or a
likelihood term for a BAO or CMB analysis — which abundances, code, rate
treatment and τ_n each analysis uses, how the theory error is added, how
the BBN helium relation enters a CMB fit — and how far each choice moves
ω_b and the abundances predicted from the CMB.
Snapshot: 2026-10-18.
From: Cooke 2024, Sect. 3.1; Grohs & Fuller 2023, Sect. 1; BAO analyses
using BBN priors.

Already in L2, not repeated here: the ω_b values per code and compilation
in `results.md#baryon-density-from-bbn` and
`results.md#code-and-rate-comparisons`; the three abundance compilations in
`surveys-and-data.md#abundance-compilations-in-use`; the η–ω_b conversion
in `physics-and-methods.md#what-bbn-measures`. In L3: full versus
summarised BBN likelihoods, and the loss of the ω_b–N_eff correlation
when D/H is compressed to a Gaussian ω_b prior, in
`deep/nuclear-reaction-rates.md` (sections "Step 6" and "Full likelihood
or summary"); how codes tabulate Y_P in `deep/bbn-codes.md`.

Notation. ω_b = Ω_b h²; η the baryon-to-photon ratio, η₁₀ = 10¹⁰ η;
y_DP = 10⁵ (D/H)_P; Y_P the primordial helium fraction, as a nucleon
fraction 4n_He/n_b unless a paper defines it as a mass fraction (stated
where it matters); τ_n the neutron lifetime; N_eff the effective number
of relativistic species; "theory error" the spread of a predicted
abundance from nuclear-rate and τ_n uncertainties.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the abundances
<!-- key: step-1-choose-the-abundances -->

Analyses read here use: PDG August 2023 values (D/H and Y_P) for the
prior adopted by DESI (Schöneberg 2024, arXiv:2401.15054)
[src: Sects. 3, 5]; PDG 2024 values, 10⁵ D/H = 2.547 ± 0.029 and
Y_P = 0.245 ± 0.003, in ACT DR6 (Calabrese et al. 2025, arXiv:2503.14454)
[src: Sect. VI.2]; Cooke et al. 2018 D/H with Aver et al. 2015 Y_P in the
LINX joint fit (Giovanetti et al. 2024, arXiv:2408.14538)
[src: Sect. VI.2, Eq. 17]. Only D/H and Y_P are used; ACT leaves out ³H,
³He and ⁷Li as "more uncertain in both their determination and their
interpretation" (arXiv:2503.14454) [src: Sect. VI.2].

### Step 2. Predict the abundances with a theory error
<!-- key: step-2-predict-the-abundances-with-a-theory -->

- **Gaussian approximation.** PRIMAT writes
  P(Y_i | ω_b) ≃ N[Ȳ_i(ω_b), σ_i^th(ω_b)] (Eq. 147), the Monte Carlo
  spread over rates and τ_n, and multiplies the individual abundance
  probabilities; only ⁴He and D are used (Pitrou et al. 2018,
  arXiv:1801.08023) [src: Sects. V.5, VI.2].
- **Explicit marginalisation.** PRyMordial samples lognormal rate
  nuisances; without this marginalisation the D/H-based width "would be
  dramatically smaller", dominated by the observational error
  (arXiv:2401.15054) [src: Sect. 3, Fig. 2].
- **Fixed theory error.** For PArthENoPE in the BAO + BBN papers and in
  Schöneberg's runs, "there is no explicit marginalization"; an
  approximate theory error of 6 × 10⁻⁷ on D/H is taken from the
  PArthENoPE rate paper [src: arXiv:2401.15054, Sect. 3].

### Step 3. Infer ω_b
<!-- key: step-3-infer-omegab -->

D/H sets ω_b; Y_P barely moves it. Burns 2026 inverts the PRyMordial
predictions for Cooke D/H and LBT Y_P, using a theory error from which the
ω_b term is removed "because it is the quantity being inferred" and the
ΔN_eff term because it is varied explicitly: the remaining D/H theory
error is 0.027 (PRIMAT rates) and 0.100 (NACRE II rates), in units of
10⁻⁵ (arXiv:2603.22414) [src: Sect. 8]. Results: ω_b = 0.02202 ± 0.00021
(PRIMAT) and 0.02231 ± 0.00056 (NACRE II) at ΔN_eff = 0; 0.02192 ± 0.00026
and 0.02226 ± 0.00056 with ΔN_eff free, since its freedom "is absorbed
almost entirely by Y_P" [src: Sect. 8]. Schöneberg puts flat priors on ω_b
and ΔN_eff and a flat τ_n prior over 876.4–882.4 s, chosen to
encompass the bottle value 877.5 (+0.5/−0.44) s (arXiv:2401.15054)
[src: Sect. 3].

### Step 4. Turn the result into a prior for BAO
<!-- key: step-4-turn-the-result-into-a-prior-for-bao -->

- **The prior in use.** Schöneberg recommends the PRyMordial NACRE II
  value with rates marginalised, ω_b = 0.02218 ± 0.00055 (PDG abundances)
  or 0.02231 ± 0.00055 (Cooke et al. 2018 D/H), because "with relatively
  conservative assumptions about the reaction rate uncertainties it is
  possible to derive a baryon abundance estimate that nicely covers all
  available results in terms of available codes and datasets"; with
  ΔN_eff free, 0.02196 ± 0.00063 or 0.02212 ± 0.00072
  (arXiv:2401.15054) [src: Sect. 5, Eqs. 4–7].
- **How DESI uses it.** DESI DR2, "as in DR1", takes 0.02218 ± 0.00055 in
  ΛCDM and 0.02196 ± 0.00063 when N_eff varies, "in which case there is
  also a covariance between Ω_b h² and N_eff", and uses it only "when we
  require calibrated results that are independent of CMB information"
  (DESI DR2, arXiv:2503.14738) [src: Sect. IV.1, Eqs. 14–15]. With the
  prior the BAO fit samples H₀ and ω_b instead of h r_d [src: Sect. V].
  The role: BAO measure H₀r_d and Ω_m, and with N_eff = 3.044 and
  Σm_ν = 0.06 eV, ω_b breaks the degeneracy [src: Sect. IV.1].
- **Planck's conservative prior.** Planck 2018 converted Cooke et al. D/H
  into ω_b with three pipelines (95%): (a) PArthENoPE with the Adelberger
  et al. empirical d(p,γ)³He rate, 0.02270 ± 0.00075; (b) PArthENoPE with
  the Marcucci et al. ab-initio rate, 0.02198 ± 0.00044; (c) PRIMAT with
  the Iliadis et al. hybrid rate, 0.02189 ± 0.00046; its "conservative BBN
  prior" ω_b = 0.0222 ± 0.0005 (68%) was "set to be compatible with each
  of these three predictions" (arXiv:1807.06209) [src: Sect. 7.6.1,
  Eq. 71].

### Step 5. Tie helium to ω_b in the CMB fit
<!-- key: step-5-tie-helium-to-omegab-in-the-cmb-fit -->

Three practices:

| Analysis | BBN table | Y_P definition | Note | Place read |
|---|---|---|---|---|
| Planck 2018 | grid from PArthENoPE 1.1, τ_n = 880.2 s fixed, uncertainties neglected | mass fraction in the fit, nucleon fraction Y_P^BBN quoted | PRIMAT higher by ΔY_P ≈ 0.0005, other parameters "well within 0.1σ" | arXiv:1807.06209, Sect. 2.1 |
| ACT DR6 | PRIMAT 2021 table (CAMB default), imported into CLASS | nucleon fraction in the BBN section | care taken for the N_eff of the table (3.044) against that of the CLASS BBN module (3.046) | arXiv:2503.14454, Sect. III, footnotes 7, 27 |
| SPT-3G D1 | CLASS default tables based on PArthENoPE reloaded | mass fraction | BBN consistency imposed when N_eff varies | arXiv:2506.20707, Sect. VII.2.4, footnote 41 |

ACT states that differences in the helium predicted by recent BBN codes
"have a negligible impact on the CMB primary anisotropy spectra"
(arXiv:2503.14454) [src: Sect. III, footnote 7]; Planck that a beam-like
τ_n ≈ 887 s would shift ΛCDM parameters by at most 0.2σ, for θ_MC
(arXiv:1807.06209) [src: Sect. 7.6.2].

### Step 6. Add deuterium to a CMB fit, or predict it from the CMB
<!-- key: step-6-add-deuterium-to-a-cmb-fit-or-predict-it -->

- **Planck.** Theory error σ(y_DP) = 0.03, from the claim of Marcucci et
  al. and from PRIMAT, judged to encompass the PArthENoPE–PRIMAT
  difference; added in quadrature to Cooke's 0.030 for a total of 0.042
  (arXiv:1807.06209) [src: Sect. 7.6.1]. Predicted from the Planck ω_b
  (95%): y_DP = 2.587 ± 0.13 (a), 2.455 ± 0.081 (b), 2.439 ± 0.082 (c),
  within 0.8σ, 1.4σ and 1.7σ of Cooke et al. [src: Eq. 72].
- **ACT DR6.** Three BBN configurations: PRIMAT_2021 (τ_n = 879.4 ±
  0.6 s), PRIMAT_2024 (same rates, τ_n = 878.4 ± 0.5 s) and PRyMordial
  (modified NACRE II rates, τ_n = 878.4 ± 0.5 s) (arXiv:2503.14454)
  [src: Sect. VI.2]. From P-ACT-LB (Planck + ACT + lensing + DESI BAO) in
  ΛCDM: y_DP = 2.415 ± 0.019 (0.036), 2.413 ± 0.019 (0.033) and
  2.480 ± 0.020 (0.104), the error in parentheses including the theory
  error [src: Eq. 41]. PRIMAT-based predictions are in "mild tension,
  ranging between 2 and 3σ" with the PDG average; PRyMordial ones are
  consistent "regardless of whether theoretical uncertainties are
  included" [src: Sect. VI.2.1]. ACT therefore combines deuterium "only
  under the assumption of PRyMordial BBN calculations" [src: Sect. VI.2.1].
  Downstream analyses reuse the resulting Gaussian
  10⁵ D/H = 2.547 ± 0.104, observation plus theory (Goldstein & Hill 2026,
  arXiv:2603.13226) [src: Sect. II, Eq. 3].
- **Full joint likelihood.** LINX evaluates
  −2 ln L_BBN = ((Y_P^pred − Y_P^obs)/σ_Y)² + ((D/H^pred − D/H^obs)/σ_D)²
  with Y_P^pred and D/H^pred functions of (ω_b, N_eff, ν_BBN), ν_BBN the
  τ_n and rate nuisances, and ω_b and N_eff shared with the CMB likelihood
  (arXiv:2408.14538) [src: Sect. VI.2, Eq. 17].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Rate family
<!-- key: rate-family -->

- **What it moves.** PRIMAT-family rates give ω_b ≈ 0.0219–0.0220 with
  errors of 0.0002–0.0003; NACRE II-family rates with marginalisation give
  ≈ 0.0222–0.0223 with errors of 0.00055 (arXiv:2603.22414 [src: Sect. 8];
  arXiv:2401.15054 [src: Sect. 5]). The NACRE II constraint is "looser by
  roughly a factor of 2.7" because of the larger D/H rate uncertainty
  [src: arXiv:2603.22414, Sect. 8].
- **Sensitivity to the data set.** Across the three compilations ω_b
  moves by less than 0.3σ with PArthENoPE 3.0 and PRyMordial–NACRE II,
  but by up to 1.4σ with PRyMordial in PRIMAT mode
  (arXiv:2401.15054) [src: Sect. 4.2].
- **A code's D/H normalisation.** PRIMAT gives ω_b = 0.02190 ± 0.00025
  from BBN alone; a code predicting 10⁵ D/H ≃ 2.61 instead of 2.46 at
  Planck parameters would give 0.02271 ± 0.00025, "exactly the same
  central value" as PArthENoPE in Consiglio et al. (arXiv:1801.08023)
  [src: Sect. VI.2].

### Conservative prior or pipeline-specific prior
<!-- key: conservative-prior-or-pipeline-specific-prior -->

- **Assumes.** A conservative prior assumes no rate family can be
  preferred; a pipeline prior assumes its rates and theory error.
- **Buys.** Schöneberg's prior "encompass[es] both the theoretical
  ab-initio calculations and the experimental rates" for d(d,n)³He and
  d(d,p)t, useful "if one wants to remain agnostic"
  (arXiv:2401.15054) [src: Sects. 3, 5]; Planck's 0.0222 ± 0.0005 was
  built the same way from three pipelines (arXiv:1807.06209)
  [src: Sect. 7.6.1].
- **Costs.** Errors 2–2.7 times larger than a PRIMAT-family prior
  (0.00055 against 0.00021–0.00026) [der: from arXiv:2603.22414, Sect. 8].
  In BAO + BBN, ω_b calibrates r_d, so the H₀ error inherits this choice;
  DESI DR2 gets H₀ = 68.51 ± 0.58 km s⁻¹ Mpc⁻¹ with the conservative prior
  (arXiv:2503.14738) [src: Sect. VI, Eq. 19].

### Neutron lifetime
<!-- key: neutron-lifetime -->

Schöneberg finds no strong correlation of τ_n with ω_b; fixing
τ_n = 879.4 s gives a "very similar" result (arXiv:2401.15054)
[src: Sect. 3, footnote 6]. In ACT's helium predictions, moving τ_n from
879.4 to 878.4 s lowers Y_P by 0.0002 (0.24727 → 0.24707), while the
PRIMAT-to-PRyMordial rate change lowers it by a further 0.00016, both
within the codes' theory errors (arXiv:2503.14454) [src: Sect. VI.2.1,
Eq. 39]. For deuterium "the neutron lifetime value has a negligible
impact" [src: Sect. VI.2.1].

### Which helium value
<!-- key: which-helium-value -->

ω_b is "largely insensitive to the assumed Helium abundance, as long as
it remains within a range compatible with the standard BBN codes"; the
EMPRESS value would give a much lower ω_b, which Schöneberg attributes to
"the breakdown of the compatibility with standard rates and assumptions"
(arXiv:2401.15054) [src: Sect. 5].

### Deuterium in a CMB fit, or not
<!-- key: deuterium-in-a-cmb-fit-or-not -->

- **ACT.** Adds D/H with PRyMordial only; N_eff = 2.87 ± 0.13 with D,
  2.89 ± 0.11 with D and He (PDG), and 2.93 ± 0.21 from BBN alone; the
  N_eff error barely changes with D "as the theoretical error on
  deuterium dominates" (arXiv:2503.14454) [src: Sect. VI.2.1, Eqs.
  43–44].
- **SPT-3G D1.** Uses BBN only through the Y_P(ω_b, N_eff) tables and
  compares with Y_P = 0.2453 ± 0.0034 from metal-poor galaxies, without a
  deuterium term (arXiv:2506.20707) [src: Sect. VII.2.4].
- **Planck.** Uses Planck + D with σ(y_DP) = 0.042 to fit a d(p,γ)³He
  rescaling A₂ (Eq. 73): A₂ = 1.080 ± 0.061 (TT,TE,EE + lowE + D), "half-way"
  between experiment and the Marcucci theory rate (A₂^th = 1.16)
  (arXiv:1807.06209) [src: Sect. 7.6.1, Eq. 74b].

### Full joint likelihood or a prior
<!-- key: full-joint-likelihood-or-a-prior -->

Sharing ω_b and N_eff between a full Planck likelihood and LINX gave
100 ω_b = 2.223 ± 0.018 and N_eff = 3.08 ± 0.13 in about 8 500 CPU-hours
of nested sampling; a gradient-based run with an emulator and the Planck
"Lite" likelihood reproduced 2.226 (+0.019/−0.021) and 3.08 (+0.13/−0.14)
in about 24 CPU-hours, though the emulator could not take Y_P^pred as
input and CMB nuisances were not sampled (arXiv:2408.14538)
[src: Sect. VI.2, Eqs. 18–19]. A single likelihood and gradient
evaluation took ~2 s [src: Sect. VI.2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Recommended BBN prior | ω_b = 0.02218 ± 0.00055 (PDG 2023); 0.02231 ± 0.00055 (Cooke D/H) | PRyMordial NACRE II, rates marginalised | arXiv:2401.15054 | Sect. 5, Eqs. 4–5 |
| Same with ΔN_eff free | 0.02196 ± 0.00063; 0.02212 ± 0.00072 | same | arXiv:2401.15054 | Eqs. 6–7 |
| τ_n prior in that fit | flat 876.4–882.4 s | same | arXiv:2401.15054 | Sect. 3 |
| PArthENoPE fixed D/H theory error | 6 × 10⁻⁷ | BAO + BBN papers | arXiv:2401.15054 | Sect. 3 |
| Data-set sensitivity of ω_b | < 0.3σ (PArthENoPE 3.0, NACRE II); up to 1.4σ (PRIMAT mode) | three compilations | arXiv:2401.15054 | Sect. 4.2 |
| ω_b from D/H + Y_P, ΔN_eff = 0 | 0.02202 ± 0.00021 (PRIMAT); 0.02231 ± 0.00056 (NACRE II) | PRyMordial, LBT Y_P | arXiv:2603.22414 | Sect. 8 |
| D/H theory error without ω_b term | 0.027 (PRIMAT); 0.100 (NACRE II), × 10⁻⁵ | same | arXiv:2603.22414 | Sect. 8 |
| Planck conservative prior | 0.0222 ± 0.0005 (68%) | three pipelines, Cooke D/H | arXiv:1807.06209 | Sect. 7.6.1 |
| Planck pipelines (95%) | 0.02270 ± 0.00075; 0.02198 ± 0.00044; 0.02189 ± 0.00046 | (a), (b), (c) | arXiv:1807.06209 | Eq. 71 |
| Planck D/H theory error | σ(y_DP) = 0.03; total with observation 0.042 | Planck + D fits | arXiv:1807.06209 | Sect. 7.6.1 |
| τ_n error to Y_P error | 1.0 s → 3.0 × 10⁻⁴ (PArthENoPE); 0.8 s → 2.4 × 10⁻⁴ (PRIMAT) | Planck | arXiv:1807.06209 | Sect. 7.6.1 |
| y_DP predicted from P-ACT-LB, ΛCDM | 2.415 ± 0.036; 2.413 ± 0.033; 2.480 ± 0.104 (total errors) | PRIMAT_2021, PRIMAT_2024, PRyMordial | arXiv:2503.14454 | Eq. 41 |
| Same, ΛCDM + N_eff | 2.384 ± 0.042; 2.383 ± 0.040; 2.455 ± 0.099 | same | arXiv:2503.14454 | Eq. 42 |
| Y_P predicted, ΛCDM | 0.24727 ± 0.000131; 0.24707 ± 0.000118; 0.24691 ± 0.000153 | same | arXiv:2503.14454 | Eq. 39 |
| D/H Gaussian used in CMB + BBN fits | 2.547 ± 0.104 (× 10⁻⁵) | ACT DR6 practice | arXiv:2603.13226 | Eq. 3 |
| DESI DR2 + BBN | H₀ = 68.51 ± 0.58; with θ_* 68.45 ± 0.47 km s⁻¹ Mpc⁻¹ | conservative prior | arXiv:2503.14738 | Eqs. 19–20 |
| Joint CMB + BBN, LINX | 100 ω_b = 2.223 ± 0.018, N_eff = 3.08 ± 0.13 (full Planck); 2.226, 3.08 (emulator, Planck Lite) | Cooke D/H, Aver 2015 Y_P | arXiv:2408.14538 | Eqs. 18–19 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **A prior without provenance.** "BBN prior" with no code, rate family,
  abundances or theory-error treatment cannot be compared: the same D/H
  gives 0.0219–0.0227 depending on pipeline (arXiv:1807.06209)
  [src: Eq. 71]. Test: quote the four items with the prior.
- **ΛCDM prior in an N_eff fit.** DESI switches to 0.02196 ± 0.00063 and
  notes the ω_b–N_eff covariance when N_eff varies (arXiv:2503.14738)
  [src: Sect. IV.1]; a one-dimensional prior drops that covariance,
  which `deep/nuclear-reaction-rates.md` quantifies.
- **BBN prior on top of the CMB.** DESI uses it only for results
  "independent of CMB information" (arXiv:2503.14738) [src: Sect. IV.1];
  adding it to a CMB fit counts ω_b information the CMB already
  dominates and couples two determinations whose comparison is a test.
- **Deuterium from a code in tension.** ACT found PRIMAT-based D/H 2–3σ
  from observation and therefore used PRyMordial for its D term
  (arXiv:2503.14454) [src: Sect. VI.2.1]; a joint fit with a tensioned
  pair pulls N_eff or ω_b. Test: run both rate families, as ACT and
  Schöneberg do, and quote the spread.
- **Table settings.** A BBN table computed at N_eff = 3.044 used in a code
  assuming 3.046, or a nucleon-fraction Y_P read as a mass fraction
  (arXiv:2503.14454 [src: Sect. III, footnote 7]; arXiv:2506.20707
  [src: footnote 41]). Test: print the table's N_eff, τ_n and Y_P
  definition.
- **Validation used in the papers.** Schöneberg shows the ω_b of every
  code and compilation side by side (arXiv:2401.15054) [src: Sect. 4.2,
  Fig. 4] and checks that his runs reproduce the published PRIMAT and
  PArthENoPE results (`results.md#code-and-rate-comparisons`); LINX reproduces the full
  joint posterior with its fast pipeline (arXiv:2408.14538)
  [src: Sect. VI.2].

## Reading list
<!-- key: reading-list -->

- Schöneberg 2024, arXiv:2401.15054 (method): the prior DESI uses, how it
  was built, its sensitivity to code and data.
- Planck 2018, arXiv:1807.06209, Sect. 7.6 (application): three
  pipelines, conservative prior, D/H theory error, A₂ test.
- DESI DR2, arXiv:2503.14738, Sect. IV.1 (application): how a BAO
  analysis applies the prior, with and without N_eff.
- Calabrese et al. 2025 (ACT DR6), arXiv:2503.14454, Sect. VI.2
  (application): Y_P and D/H predicted per BBN configuration; why
  deuterium is combined with one code only.
- Camphuis et al. 2025 (SPT-3G D1), arXiv:2506.20707, Sect. VII.2.4
  (application): helium-only BBN consistency.
- Pitrou et al. 2018, arXiv:1801.08023 (foundation): Gaussian
  approximation of the BBN likelihood and the D/H normalisation effect.
- Burns 2026, arXiv:2603.22414 (method): ω_b from abundances with the
  correct theory error, per rate compilation.
- Giovanetti et al. 2024, arXiv:2408.14538 (method): a joint CMB + BBN
  likelihood with shared parameters.
- Cooke et al. 2018, arXiv:1710.11129 (foundation): D/H to η to ω_b with
  separate observational and BBN errors.

## Not verified
<!-- key: not-verified -->

- ACT DR6's own derivation of the 0.104 total D/H error (the PRyMordial
  theory error combined with the PDG observational error) is inferred
  from its Fig. 29 caption and from arXiv:2603.13226; the PDG 2024 review
  itself was not read.
- The DESI DR1 BAO paper's use of the same prior is stated by DESI DR2
  ("as in DR1"), not read in DR1.
- The earlier full LINX + Planck analysis ("Paper II" of
  arXiv:2408.14538) was not identified or read.
- The PArthENoPE rate paper that sets the 6 × 10⁻⁷ D/H theory error is
  named by arXiv:2401.15054 and not read here.
