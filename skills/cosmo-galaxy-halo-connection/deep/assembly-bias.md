# Assembly bias — cosmo-galaxy-halo-connection dossier

Scope: how galaxy assembly bias is written into an occupation model (choice
and ranking of the secondary property, decorated, re-ranking and
mass-parameter implementations, priors, likelihood), how it is diagnosed
(shuffling, correlated re-ranking, direct HOD splits), and how to choose
between these forms and read their parameters across papers.
Snapshot: 2026-10-21.
From: Wechsler & Tinker 2018, Sect. 5.3–5.4, 6.4, 7.2; Asgari et al. 2023,
Sect. 5.8.

Already in L2, not repeated here: the vocabulary (halo assembly bias, galaxy
assembly bias, conformity) and the halo-level results (Gao, Wechsler,
Villarreal, Mansfield) in
`physics-and-methods.md#assembly-bias-and-secondary-dependencies`; the sizes
of the effect on clustering and lensing, the HSC-Y3 scale-cut diagnostic and
the TNG300 budget of the lensing-is-low excess in
`systematics.md#assembly-bias-and-secondary-dependencies`; the detection
table (SDSS, CMASS, DESI One-Percent, DESI DR1 Q_sat with its method, GAMA ×
KiDS, redMaPPer) in `results.md#assembly-bias-and-conformity-detections`;
the for-and-against debate in
`open-questions.md#is-galaxy-assembly-bias-detected`; the DESI DR1 lensing
model (A_cen, A_sat, η, α_s, blinding) in
`physics-and-methods.md#galaxy-galaxy-lensing-with-clustering`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Pick the secondary property and rank it at fixed mass
<!-- key: step-1-pick-the-secondary-property-and-rank-it -->

Every implementation read here ranks a halo property x within narrow bins
of halo mass, so that the perturbation is a function of the rank, not of x
itself. The definitions differ from paper to paper:

| Property | Definition as written | Analysis | Place read |
|---|---|---|---|
| Concentration | c = r_vir / r_s,Klypin, the velocity-based Klypin scale radius; standardised δ_c = (c − c̄(M))/σ_c(M) | BOSS CMASS, Yuan et al. 2021 | arXiv:2010.04182, Sect. 2.4, Eqs. 4–5 |
| Concentration | c = r_90 / r_25, r_x enclosing x% of the halo mass; rank c^rank ∈ [0, 1] in narrow mass bins, 0.5 = median | AbacusHOD, BOSS and eBOSS | arXiv:2110.11412, Sect. 2.4 |
| Concentration | high or low according to the rank percentile f_split = 0.5 at fixed M_vir | SDSS DR7, Zentner et al. 2019 | arXiv:1606.07817, Sect. 2.2 |
| Concentration | split at the median, decorated HOD | DESI DR1 × DES, KiDS, HSC | arXiv:2512.15962, Sect. III.2, Eq. 8 |
| Environment (tophat) | M_env = summed mass of neighbouring haloes and subhaloes beyond r_vir and within r_max = 5 h⁻¹Mpc; f_env = M_env / M̄_env(M) | Yuan et al. 2021, after Hadzhiyska et al. 2020 | arXiv:2010.04182, Sect. 2.4, Eq. 6 |
| Environment (tophat) | δ = M(r_98 < r < 5 h⁻¹Mpc) / ⟨M(r_98 < r < 5 h⁻¹Mpc)⟩ − 1, ranked as δ^rank | AbacusHOD | arXiv:2110.11412, Eq. 12 |
| Environment (smoothed) | smoothed matter overdensity δ_5 and tidal anisotropy α_5 | SIMBA vs TNG, Yang et al. 2025 | arXiv:2511.01441, abstract, Sect. 3.2 |
| Environment (data) | galaxy overdensity δ_g, rank-ordered into halves | DESI DR1 BGS groups | arXiv:2510.20896 (definition in L2) |
| Environment (smoothed, SAM) | δ_1.25 ranked in narrow mass bins; δ_5 and tidal anisotropy α_0.3,1.25 as alternatives | Xu et al. 2021 | arXiv:2007.05545, Sect. 5.1 |
| Environment (constrained run) | matter overdensity δ_8^m on 8 h⁻¹Mpc, normalised rank in a narrow mass bin, after Wibking et al. | SDSS on ELUCID, Salcedo et al. 2022 | arXiv:2010.04176, Sect. 3.2 |
| Concentration (NFW) | upper or lower 50 percentile in a narrow mass bin | DESI One-Percent BGS, Pearl et al. | arXiv:2309.08675, Sect. II.2.2 |
| Formation time, environment | haloes split by formation time or large-scale environment | EAGLE, Illustris, Artale et al. 2018 | arXiv:1805.06938, abstract |

Why concentration: it correlates with formation history, earlier-forming
haloes being more concentrated at fixed mass [src: arXiv:2010.04182, Sect.
2.4]. Why environment: it was found to be a necessary tracer of secondary
bias both in simulations and in CMASS data [src: arXiv:2110.11412, Sect.
2.4]. Why r_max = 5 h⁻¹Mpc: "large enough to capture the immediate vicinity
of the halo without extending deep into the 2-halo regime" [src:
arXiv:2010.04182, Sect. 2.4], and the value recommended by Hadzhiyska et al.
2020 as best at capturing the secondary-bias signature in hydrodynamical
simulations [src: arXiv:2110.11412, Sect. 7.1]. Why the large-scale
density: the bias shift is Δb_g = ρ_cc σ(b|M)/√⟨N_gal⟩, so the best
variable has |ρ_cc| → 1 with halo bias, i.e. the overdensity itself
(arXiv:2010.04176, Eq. 6) [src: Sect. 3.2]. Why ranks: less sensitive to
the exact definition and scale of the environment [src: arXiv:2007.05545,
Sect. 5.1; arXiv:2010.04176, Sect. 3.2].

### Step 2. Choose how the occupation responds to the rank
<!-- key: step-2-choose-how-the-occupation-responds-to -->

Four implementations are in use. Notation: ⟨N_c|M⟩ and ⟨N_s|M⟩ are the
mass-only (baseline) mean central and satellite occupations.

**(a) Decorated HOD, mean-conserving (Hearin et al. 2016).** The decorated
distribution P_dec(N|M, x) must reproduce the marginal moments of the
standard one, ⟨N^k|M⟩_dec = ⟨N^k|M⟩_std (arXiv:1512.03050, Eq. 15); with the
decoration function δN^k(M, x) ≡ ⟨N^k|M, x⟩_dec − ⟨N^k|M⟩_std (Eq. 16) this
reads ∫ δN^k P(x|M) dx = 0 for every k (Eq. 17). For centrals, a
nearest-integer distribution makes all moments equal the first, so
conserving k = 1 conserves everything (Eq. 18) [src: Sect. 4.1.2]. For
satellites, Poisson statistics both before and after decoration cannot
conserve the HOD (Eq. 19); the paper lists three ways out and in its
two-population model keeps both distributions Poisson, accepting that the
second moment is not conserved, following subhalo occupation statistics
(Mao et al. 2015, as cited) [src: Sects. 4.1.3, 4.2]. In the two-population
version, a fraction P_1 of haloes with the highest x gets δN_1, the rest
δN_2 with P_1 δN_1 + P_2 δN_2 = 0 (Eq. 26). Positivity and N_c ≤ 1 bound
the decoration (Eqs. 27–30); 𝒜_bias ∈ [−1, 1] is the fraction of the
maximum allowed strength, positive meaning more galaxies in haloes above
the median x [src: Sect. 4.2.1]. For f_split = 0.5 this becomes
δN_cen = A_cen min[⟨N_cen|M⟩, 1 − ⟨N_cen|M⟩], δN_sat = A_sat ⟨N_sat|M⟩
(Zentner et al. 2019, arXiv:1606.07817, Eq. 5) [src]; DESI DR1 writes the
same central rule as its Eq. 8 (arXiv:2512.15962) [src]. Central-satellite
pairs: ⟨N_c N_s|M, x⟩ = ⟨N_c|M, x⟩⟨N_s|M, x⟩ at fixed x (Eq. 23), which
still induces a central–satellite correlation after marginalising over x
(Eq. 24) [src: arXiv:1512.03050, Sect. 4.1.4].

**(b) Pseudo-mass re-ranking, density-conserving (Yuan et al. 2018, 2021).**
Haloes are ranked by log₁₀M_pseudo = log₁₀M + A δ_c + A_e f_env
(arXiv:2010.04182, Eqs. 5, 7), and the list of mass-only expected numbers
is mapped bijectively onto the re-ranked haloes. This swaps galaxies
between haloes and preserves the total number density, but not ⟨N|M⟩,
unlike the Halotools decorated HOD [src: Sect. 2.4]. A is formally
unbounded; the authors "expect A to be between −1 and 1". One A and one A_e
act on centrals and satellites together, a simplification the authors chose
"for model simplicity and to limit the number of necessary parameters"
[src: Sect. 2.4].

**(c) Analytic modulation of the mass parameters (Xu et al.; AbacusHOD).**
The origin, fitted to a SAM: log M_min = log M_min⁰ + B_cen(δ_1.25^rank −
0.5), log M_1 = log M_1⁰ + B_sat(δ_1.25^rank − 0.5); negative B lowers the
mass scales in dense regions; |B| is the range in dex; modulating σ_log M
alone could not reproduce the central signal of the SAM (arXiv:2007.05545,
Eqs. 7–8) [src: Sect. 5.1]. Salcedo et al. use the same form on δ̃_8^m with
𝒬_cen, 𝒬_sat, positive 𝒬_cen meaning dense haloes are less likely to host
centrals (arXiv:2010.04176, Eqs. 7–8) [src: Sect. 3.2]. AbacusHOD's version
shifts the two mass scales of the baseline HOD:
log₁₀M_cut^mod = log₁₀M_cut + A_cent(c^rank − 0.5) + B_cent(δ^rank − 0.5) and
log₁₀M_1^mod = log₁₀M_1 + A_sat(c^rank − 0.5) + B_sat(δ^rank − 0.5)
(arXiv:2110.11412, Eqs. 10–11). Reason: galaxy-swap schemes conserve the
number density "but tend to be computationally expensive"; the analytic mix
is cheaper [src: Sect. 2.4]. Because ⟨N⟩ is non-linear in log M_cut and log
M_1, symmetric shifts of ±(rank − 0.5) do not conserve ⟨N|M⟩ exactly [der:
from Eqs. 10–11 and the erf/power-law baseline]; the fit to the number
density absorbs the difference.

**(d) Density-dependent onset slopes (Yang et al. 2025).** From SIMBA and
TNG, a six-parameter HOD N_c = 1/[1 + (M/M_1)^(−μ)], N_s = N_c (M/M_2)^γ /
[1 + (M/M_3)^(−ν)] (arXiv:2511.01441, Eq. 7), with the δ_5 dependence put in
the slopes, μ = μ_tot − C_δ (r_δ − 0.5) and likewise for ν (Eq. 8).
Reason: the HODs of the δ_5 quartiles differ "almost entirely in the
rapidity of onset" of centrals and satellites; high-mass haloes are nearly
independent of environment [src: Sect. 6, abstract]. Fitted relations: M_2
/ M_1 close to 10, M_3 / M_2 close to 0.4, γ close to 1; C_δ(μ) ~ 2 C_δ(ν);
the authors suggest marginalising over C_δ "of order unity" [src: Sect. 6].

The direct DESI measurement uses the form of (c) for satellites: log
M_1(δ_g) = log M_1* + Q_sat(δ̃_g − 0.5), with δ̃_g set to 0.25 and 0.75 for
the low- and high-density halves and α fixed to 1 (arXiv:2510.20896, Eq.
9) [src]. The BGS One-Percent fit writes the central decoration as δN_cen =
A_cen(0.5 − |0.5 − ⟨N_cen⟩_std|) (arXiv:2309.08675, Eq. 7) [src], equal to
the min form of (a) [der: 0.5 − |0.5 − x| = min(x, 1 − x)].

### Step 3. Fit
<!-- key: step-3-fit -->

The SDSS DR7 decorated-HOD analysis is the reference set-up for w_p
[src: arXiv:1606.07817, Sect. 2.3]:

- Data: w_p in eleven logarithmic bins from 0.17 to 16.9 h⁻¹Mpc with the
  published covariance, plus the number density. Two larger-separation
  points were dropped because they "add considerably to the computational
  expense but alter our results insignificantly".
- Likelihood: χ² = Δw_p,i [C⁻¹]_ij Δw_p,j + (n_g^mock − n_g^meas)²/σ_n²
  (Eq. 6), σ_n Poisson for both measured and predicted densities.
- Sampler: emcee; ~3–10 × 10⁶ samples to converge.
- Priors, all uniform (Table 1): log M_min [9, 14], σ_log M [0.01, 1.5],
  log M_0 [9, 14], log M_1 [10.7, 15], α [0, 2], A_cen and A_sat [−1, 1]
  with "strict boundaries". Only log M_0 and σ_log M priors matter to the
  posterior; log M_0 is often very poorly constrained by clustering.

Redshift-space set-up (BOSS CMASS): ξ(r_p, π) from 0.169 to 30 h⁻¹Mpc
transverse and 0 to 30 h⁻¹Mpc along the line of sight, with a re-run on
doubled scales (0.338–60 h⁻¹Mpc in 8 log bins, 0–60 in 6 linear bins)
[src: arXiv:2010.04182, Sect. 6.3]. AbacusHOD adds parameters one at a time
and then samples with dynesty to compute evidences [src: arXiv:2110.11412,
Sect. 5.4]. DESI DR1 frees A_cen and A_sat over the maximum range allowed
by the model, [−1, 1] [src: arXiv:2512.15962, Sect. III.2, Table 1].
Count statistics: SDSS DR7 (Wang et al. 2022) and DESI BGS (Pearl et al.)
fit n_gal, w_p and counts-in-cylinders P(N_CiC) with a concentration-
decorated HOD [src: arXiv:2204.05332, abstract; arXiv:2309.08675, Sect.
II.3]. Salcedo et al. fit w_p of quintiles in galaxy counts on 8 h⁻¹Mpc
cross the full sample, p(N_8^g) and n_g on the constrained ELUCID
reconstruction of the SDSS volume [src: arXiv:2010.04176, abstract,
Sect. 6 headings].

### Step 4. Diagnose with shuffling
<!-- key: step-4-diagnose-with-shuffling -->

The shuffling test (Croton et al. 2007) removes every dependence of
occupation on halo properties other than mass. As run on SIMBA and TNG
[src: arXiv:2511.01441, Sect. 3.1]:

1. Bin haloes in log mass, width 0.1 dex (modest changes in width do not
   matter).
2. Move the galaxy content of each halo to a random halo of the same bin;
   centrals keep their offset from the halo's most-bound particle,
   satellites their offset from the central.
3. Measure w_p (10 log bins, 0.1–20 h⁻¹Mpc, π_max = 30 h⁻¹Mpc) and form
   w_p / w_p,shuffled − 1, averaged over ten shufflings.
4. Errors: jackknife over 5 × 5 sub-boxes in the X–Y plane, plus the
   scatter between shufflings.
5. Control: randomly rotating each halo's content changes clustering by ≲
   1%, so halo-orientation alignments, which shuffling destroys, do not
   produce the signal.

Hadzhiyska et al. 2020 shuffle in 5% mass bins and average the
bijective-over-shuffled ratio over 1 < r < 20 h⁻¹Mpc [src:
arXiv:1911.02610, Sect. 3.1]. To find which property carries the signal,
they re-order occupations within each mass bin by a secondary property with
an adjustable correlation r, drawn from a bivariate Gaussian of correlation
r and mapped to ranks (six steps in their Sect. 4.2); further shuffling
within bins of mass and environment shows how much of the excess the
environment explains (their Sect. 4.3, Conclusions) [src]. In a SAM, Xu et
al. shuffle centrals in 0.1 dex bins below log M_h = 14.6 (0.2 and 0.6 dex
above), move satellites with their central, place a moved central at the
former occupant or the most-bound particle, and use 10 shuffles for the
error [src: arXiv:2007.05545, Sect. 3.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Concentration, environment or both
<!-- key: concentration-environment-or-both -->

- **CMASS, redshift-space.** Added one at a time to the baseline +
  velocity-bias model, (A_cent, A_sat) improves χ² by 6.1, (B_cent, B_sat)
  by 18.2, the satellite profile parameter s by 7.1; other extensions are
  insignificant. Baseline + velocity bias + B reaches χ² = 42; adding s
  gives χ² = 33 for 32 degrees of freedom; the 1D marginals of B_cent and
  B_sat show no detection but the 2D posterior strongly prefers non-zero
  values; central concentration assembly bias is at 2σ [src:
  arXiv:2110.11412, Sect. 5.4, Figs. 6–7].
- **Hydrodynamical runs.** Among eight properties tested in TNG300, the
  environment correlates most strongly with occupation; matching the
  hydro clustering needs r = 0.2 for f_env against r = 0.45 for velocity
  anisotropy β and for σ²R_halfmass [src: arXiv:1911.02610, Sect. 4.2,
  Conclusions]. In SIMBA and TNG most assembly bias is attributed to δ_5,
  and tidal anisotropy contributes negligibly [src: arXiv:2511.01441,
  abstract].
- **Semi-analytic model.** Halo age or concentration carry only 20–30% of
  the signal; the smoothed matter density or the tidal anisotropy "can
  account for the full level" (definition matters) [src: arXiv:2007.05545,
  abstract]. On tidal anisotropy this differs from the SIMBA/TNG result
  above.
- **EAGLE and Illustris.** At fixed low halo mass, haloes in dense regions
  and early-formed haloes more often host a central; early-formed haloes
  host fewer satellites; "in agreement with previous findings from
  semi-analytical models" [src: arXiv:1805.06938, abstract].
- **What DESI DR1 did.** Concentration only, stating that other secondary
  properties such as overdensity are advocated and "further tests are
  needed" [src: arXiv:2512.15962, Sect. III.2].
- **What each one moves.** Concentration terms matter mostly below r_p = 1
  h⁻¹Mpc (one-halo pairs); environment terms lower w_p most near r_p ~ 3
  h⁻¹Mpc, the scale at which the environment is defined [src:
  arXiv:2110.11412, Sect. 2.4, Fig. 1].

### Conserve ⟨N|M⟩, conserve n̄, or neither
<!-- key: conserve-n-m-conserve-n-or-neither -->

- **Mean-conserving (decorated HOD).** The baseline parameters keep their
  meaning: averaged over haloes of fixed mass, the decorated model has the
  same HOD as the standard model with the same five parameters [src:
  arXiv:1606.07817, Sect. 2.2]. Cost: hard bounds on 𝒜 that depend on the
  baseline (Eqs. 27–30 of arXiv:1512.03050) and, for satellites, a choice
  between conserving the second moment and keeping Poisson statistics [src:
  Sect. 4.1.3].
- **Density-conserving re-ranking.** Multiple secondary properties in one
  pseudo-mass, total n̄ fixed; ⟨N|M⟩ is not conserved [src:
  arXiv:2010.04182, Sect. 2.4], so the fitted M_cut, M_1 and α are not those
  of a mass-only model. In AbacusHOD fits, adding environment terms lowers
  M_cut, M_1 and α, moving centrals and satellites to lower-mass haloes
  [src: arXiv:2110.11412, Sect. 5.4].
- **Analytic modulation.** Cheapest, separate central and satellite terms;
  the sign convention is reversed relative to Yuan et al. 2021 (see "What
  goes wrong").

### Separate central and satellite terms
<!-- key: separate-central-and-satellite-terms -->

The unified A and A_e of Yuan et al. 2021 were a simplification; AbacusHOD
finds the satellite environment term stronger than the central one, "the
need for separate secondary bias prescriptions" [src: arXiv:2110.11412,
Sect. 5.4]. In the decorated HOD the two terms act on different mass
ranges: central assembly bias only where 0 < ⟨N_c⟩ < 1, satellite assembly
bias wherever ⟨N_s⟩ > 0; with 𝒜_sat = 1 low-concentration haloes host no
satellites at all [src: arXiv:1512.03050, Sect. 4.2.1].

### Baseline HOD and mass range
<!-- key: baseline-hod-and-mass-range -->

The large-scale reach of central assembly bias grows with σ_log M, because
a wider transition widens the mass range where 0 < ⟨N_c|M⟩ < 1; centrals
are typically 70–90% of a sample [src: arXiv:1512.03050, Sect. 5.3]. In
SIMBA and TNG the occupation varies with δ_5 only near the turn-on masses
of centrals and satellites [src: arXiv:2511.01441, abstract, Sect. 6]. A
data constraint is therefore specific to the mass range probed: the DESI
direct test covers galaxies above 0.4 L* in haloes with log M_h > 12.9, and
the authors leave open that strong assembly bias may be a lower-mass
phenomenon [src: arXiv:2510.20896, Conclusions].

### Environment definition
<!-- key: environment-definition -->

- Tophat r_max: in CMASS, best χ² at r_max = 4 h⁻¹Mpc and largest A_e at 6
  h⁻¹Mpc; Gaussian smoothing prefers 2 h⁻¹Mpc; the same r_max preference
  survives doubling the scales of the data vector [src: arXiv:2010.04182,
  Sect. 6.3].
- With AbacusSummit and CompaSO haloes, varying r_max, or using r_max = 5
  r_98, gives no improvement, and a grid-based environment (1024³ grid, 3
  h⁻¹Mpc Gaussian) gives no improvement over the no-environment HOD; the
  authors recommend the enclosed neighbour mass and stress "the high
  sensitivity of the fit to the details of the HOD model" [src:
  arXiv:2110.11412, Sect. 7.1].

### Which statistic
<!-- key: which-statistic -->

Counts-in-cylinders: SDSS DR7 gives significant positive central
assembly bias for M_r < −20.0 and −19.5, none for −21.0, and at most a
marginal negative satellite term [src: arXiv:2204.05332, abstract]; on
DESI BGS the CiC-free fit gives "very little information about assembly
bias" [src: arXiv:2309.08675, Fig. 6 caption]. On w_p alone, Vakili &
Hahn find modest central assembly bias in M_r < −20.5 to −19.5, none in
the brightest samples, no satellite dependence, and information criteria
favouring the mass-only HOD in most cases [src: arXiv:1610.01991,
abstract].

Decorated parameters are "in many instances poorly constrained" by SDSS
DR7 w_p alone [src: arXiv:1606.07817, Sect. 2.2]. Fitting ξ(r_p, π) to mocks
with the CMASS jackknife covariance recovers A and A_e within their 1σ
errors, and most other parameters within 1σ, except κ (satellite cut-off)
at ~2σ [src: arXiv:2010.04182, Sect. 6.1].

### Constrained or random simulation
<!-- key: constrained-or-random-simulation -->

On mocks, cosmic variance between a constrained and a non-constrained
simulation can bias the fit into "an erroneous detection" of assembly
bias; the ELUCID reconstruction of the SDSS volume removes that
degeneracy and gives 𝒬_cen = −0.09 ± 0.05, 𝒬_sat = 0.09 ± 0.10 above
M_⋆ = 10^10.2 h⁻²M_⊙, "no evidence for a significant (> 2σ)" assembly bias
[src: arXiv:2010.04176, abstract].

### Consequence for cosmology
<!-- key: consequence-for-cosmology -->

Extending the HOD (halo shape, incompleteness, baryons, central position
bias) in Aemulus fits of BOSS w_p, ξ_0 and ξ_2 does not significantly
change the growth rate, with weak to mild evidence for some extensions
[src: arXiv:2409.19399, abstract].

### Consequence for lensing
<!-- key: consequence-for-lensing -->

Assembly-bias fits to ξ(r_p, π) move galaxies to lower-mass haloes and lower
the predicted CMASS lensing by ~10–20%, bringing it to about 1σ from the
data; a joint w_p + ΔΣ fit with concentration assembly bias only had left a
10–20% w_p misfit and reduced the lensing discrepancy by only ~10% [src:
arXiv:2010.04182, Sect. 5.3; arXiv:2110.11412, Sect. 7.2].

### What galaxy-formation models predict
<!-- key: what-galaxy-formation-models-predict -->

Shuffling gives ~5% at z = 2 in both SIMBA and TNG, then ~10% at z = 0 in
TNG and nearly zero in SIMBA [src: arXiv:2511.01441, abstract]; the TNG300
shuffled deficit at 1–20 h⁻¹Mpc is 15 ± 1%, not removed by changing the
finder to ROCKSTAR; M_200m minimises it among the mass proxies tried (M_200m, M_200c, V_peak) without removing it
[src: arXiv:1911.02610, Sect. 3.1, Conclusions]. A semi-analytic mock at the
DESI density gives Q_sat = −0.25 (as cited by the DESI paper) against the
measured 0.05 ± 0.14 [src: arXiv:2510.20896, Conclusions]. Conformity: in
the SAG model on MDPL2, for centrals in 10^11.6–10^11.8 h⁻¹M_⊙ haloes split
by sSFR and age, the level of conformity correlates with the level of
assembly bias, and removing centrals near massive haloes lowers both [src:
arXiv:2505.03880, abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Decorated-HOD bounds | 𝒜_cen, 𝒜_sat ∈ [−1, 1], hard | SDSS DR7 | arXiv:1606.07817 | Table 1 |
| HOD priors (uniform) | log M_min [9, 14], σ_log M [0.01, 1.5], log M_0 [9, 14], log M_1 [10.7, 15], α [0, 2] | SDSS DR7 | arXiv:1606.07817 | Table 1 |
| w_p data vector | 11 log bins, 0.17–16.9 h⁻¹Mpc | SDSS DR7 | arXiv:1606.07817 | Sect. 2.3 |
| Chain length | ~3–10 × 10⁶ samples (emcee) | SDSS DR7 | arXiv:1606.07817 | Sect. 2.3 |
| Environment radius | r_max = 5 h⁻¹Mpc beyond r_vir (or r_98) | CMASS, AbacusHOD | arXiv:2010.04182; arXiv:2110.11412 | Eqs. 6, 12 |
| Preferred r_max | χ² minimum 4, A_e maximum 6 h⁻¹Mpc; Gaussian 2 h⁻¹Mpc | CMASS | arXiv:2010.04182 | Sect. 6.3 |
| Δχ² by extension | A pair −6.1, B pair −18.2, s −7.1 | CMASS ξ(r_p, π) | arXiv:2110.11412 | Sect. 5.4 |
| Best fit | χ² = 33 for 32 d.o.f. (baseline + velocity bias + B + s) | CMASS | arXiv:2110.11412 | Sect. 5.4 |
| Central concentration assembly bias | 2σ | CMASS | arXiv:2110.11412 | Fig. 7 caption |
| Lensing change | predicted ΔΣ lowered by ~10–20% | CMASS | arXiv:2110.11412 | Sect. 7.2 |
| Shuffled deficit | 15 ± 1% over 1–20 h⁻¹Mpc | TNG300-1, 5% mass bins | arXiv:1911.02610 | Sect. 3.1 |
| Correlation needed | r = 0.2 (f_env), 0.45 (β, σ²R_halfmass) | TNG300-1-Dark | arXiv:1911.02610 | Sect. 4.2 |
| Shuffling assembly bias | ~5% at z = 2; ~10% (TNG), ~0 (SIMBA) at z = 0 | stellar-mass samples | arXiv:2511.01441 | abstract |
| Orientation control | ≲ 1% | SIMBA, TNG | arXiv:2511.01441 | Sect. 3.1 |
| Density-slope coupling | C_δ(μ) ~ 2 C_δ(ν); C_δ of order unity | SIMBA, TNG | arXiv:2511.01441 | Sect. 6 |
| Direct satellite test | Q_sat = 0.05 ± 0.14; −0.01 ± 0.14 with a 5% M_h bias for dense haloes | DESI DR1 BGS, log M_h > 12.9 | arXiv:2510.20896 | Q_sat paragraph |
| Recovery on mocks | A, A_e within 1σ; κ ~2σ off | CMASS-like mocks | arXiv:2010.04182 | Sect. 6.1 |
| Constrained-run bound | 𝒬_cen = −0.09 ± 0.05, 𝒬_sat = 0.09 ± 0.10 | SDSS on ELUCID, M_⋆ > 10^10.2 h⁻²M_⊙ | arXiv:2010.04176 | abstract |
| Central assembly bias with CiC | positive at 99.9% (M_r < −20.0), 99.5% (< −20.5); 94.8% at −21.0, z ~ 0.25 | DESI One-Percent BGS | arXiv:2309.08675 | abstract |
| Share of the signal from age or concentration | 20–30% | SAM, shuffling | arXiv:2007.05545 | abstract |
| Shuffle mass bins | 0.1 dex below log M_h = 14.6, then 0.2 and 0.6 dex; 10 shuffles | SAM | arXiv:2007.05545 | Sect. 3.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Sign conventions.** In the decorated HOD and in Yuan et al. 2021 a
  positive parameter puts more galaxies in haloes with high x; in AbacusHOD
  a positive A or B puts fewer galaxies there; AbacusHOD's negative B_cent,
  B_sat correspond to Yuan et al.'s positive A_e [src: arXiv:2110.11412,
  Sects. 2.4, 5.4]. A positive Q_sat means fewer satellites in dense
  environments [src: arXiv:2510.20896, Eq. 9], as does a positive 𝒬_cen
  in Salcedo et al. [src: arXiv:2010.04176, Sect. 3.2]; a negative B_cen of
  Xu et al. lowers M_min in dense regions, the AbacusHOD sense [src:
  arXiv:2007.05545, Sect. 5.1]. Test: before comparing
  values, write down which way each paper's parameter moves galaxies.
- **Amplitudes compared across definitions.** A_e is degenerate with the
  amplitude of f_env and is not comparable between the tophat and Gaussian
  definitions [src: arXiv:2010.04182, Sect. 6.3]; 𝒜 is a fraction of a
  baseline-dependent maximum [src: arXiv:1512.03050, Sect. 4.2.1]. Compare
  the induced clustering change or the shuffling ratio instead.
- **Posterior at a hard prior edge.** 𝒜 cannot exceed ±1; an
  unconstrained σ_log M or log M_0 changes the mass range where central
  assembly bias can act [src: arXiv:1606.07817, Sect. 2.3;
  arXiv:1512.03050, Sect. 5.3]. Test: report the 1D posteriors with the
  prior range and rerun with σ_log M fixed.
- **Degeneracy with the satellite profile.** The satellite concentration
  term weakens once s is free [src: arXiv:2110.11412, Fig. 7 caption]; the
  environment terms do not change [src: Sect. 5.4]. Test: free s and
  velocity bias together with the secondary terms.
- **Mass-constant amplitude.** If the dependence lives near turn-on masses
  (arXiv:2511.01441, Sect. 6), a mass-independent A misdescribes it.
  Test: fit the density dependence of the slopes, or split samples by
  luminosity.
- **Wrong property, small signal.** A concentration-only model can return
  A ≈ 0 while environment terms are needed (DESI DR2 multiplets in L2;
  arXiv:2110.11412, Sect. 5.4). Test: run concentration and environment
  terms separately and jointly.
- **Shuffling noise read as signal.** Single shuffles are noisy. Test:
  average ten shuffles, add the shuffle scatter to the jackknife variance,
  and run the rotation control [src: arXiv:2511.01441, Sect. 3.1]; check a
  pure-HOD N-body box gives no deficit, as on 27 Abacus sub-boxes [src:
  arXiv:1911.02610, Conclusions].
- **Cosmic variance read as assembly bias.** Fitting a non-constrained
  simulation to a small volume can produce a spurious detection [src:
  arXiv:2010.04176, abstract]. Test: repeat on a constrained run or
  several boxes.
- **Box variance and finder.** The TNG300 deficit was checked against box
  size and the halo finder (FoF, ROCKSTAR) [src: arXiv:1911.02610,
  Conclusions]. Test: repeat the shuffle on a second finder.

## Reading list
<!-- key: reading-list -->

- Foundation: Hearin et al. 2016, arXiv:1512.03050 — HOD conservation,
  decoration functions, bounds on 𝒜, dependence on σ_log M and on the
  secondary property.
- Application: Zentner et al. 2019, arXiv:1606.07817 — decorated-HOD fit of
  SDSS w_p with priors, likelihood and sampler written out.
- Method: Yuan et al. 2021, arXiv:2010.04182 — pseudo-mass re-ranking,
  environment definition and its r_max scan, mock recovery tests.
- Method: Yuan et al. 2021 (AbacusHOD), arXiv:2110.11412 — AbacusHOD analytic
  modulation, sign convention, extension-by-extension Δχ², environment
  definitions.
- Diagnostic: Hadzhiyska et al. 2020, arXiv:1911.02610 — shuffling in a
  hydro run, correlated re-ranking, ranking of eight secondary properties.
- Critique: Yang et al. 2025, arXiv:2511.01441 — SIMBA and TNG disagree at
  z = 0; density dependence confined to turn-on masses; C_δ slope model.
- Application: Shao et al. 2025, arXiv:2510.20896 — model-light direct
  satellite test against environment.
- Method: Xu et al. 2021, arXiv:2007.05545 — SAM dissection of secondary
  properties; origin of the analytic B_cen, B_sat modulation.
- Application: Salcedo et al. 2022, arXiv:2010.04176 — 𝒬_cen, 𝒬_sat on a
  constrained simulation of the SDSS volume.
- Application: Wang et al. 2022, arXiv:2204.05332; Pearl et al. 2024,
  arXiv:2309.08675 — counts-in-cylinders detections in SDSS DR7 and DESI
  BGS.
- Application: Vakili & Hahn 2019, arXiv:1610.01991 — w_p bound with model
  selection.
- Prediction: Artale et al. 2018, arXiv:1805.06938 (EAGLE, Illustris);
  Lacerna et al. 2025, arXiv:2505.03880 (conformity and assembly bias in
  SAG).
- Cosmology impact: Zhai & Percival 2024, arXiv:2409.19399.
- Application: Lange et al. 2025, arXiv:2512.15962 — decorated HOD in a
  cosmological lensing + clustering fit, and its stated limits.

## Not verified
<!-- key: not-verified -->

- Yuan et al. 2018 (implementation of the re-ranking), Walsh & Tinker 2019
  and Mao et al. 2015 are cited in the papers read; not read, no
  identifiers recorded. Xu et al. 2020 is now read (arXiv:2007.05545).
- The SDSS indirect constraint Q_sat = 0.09 ± 0.10 quoted by the DESI
  direct paper (its reference 32) equals the value in Salcedo et al.
  (arXiv:2010.04176, abstract); that reference 32 is this paper was not
  checked.
- Artale et al. 2018, Wang et al. 2022, Vakili & Hahn 2019, Zhai & Percival
  2024 and Lacerna et al. 2025: abstracts only.
- Hadzhiyska et al. 2021 (arXiv:2108.00006, TNG vs Santa-Cruz SAM): abstract
  only; the quantitative differences in occupancy response were not read.
- The definitions of δ_5 and α_5 (smoothing kernel) in arXiv:2511.01441,
  Sect. 3.2, were not read.
