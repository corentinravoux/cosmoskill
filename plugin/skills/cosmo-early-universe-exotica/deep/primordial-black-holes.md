# Primordial black holes: how a constraint curve is built — cosmo-early-universe-exotica dossier

Scope: how an f_PBH(M) exclusion curve is produced from a microlensing
survey (rate model, halo and disk models, efficiency, Poisson or
timescale likelihood, finite-source and wave-optics corrections) and from
LVK merger data (early-Universe binary rate, suppression factor,
hierarchical likelihood), how monochromatic curves are translated to
extended mass functions and combined, and which assumptions move each
curve.
Snapshot: 2026-10-22.
From: Carr et al. 2026 review, Sects. II–VI; LISA Cosmology WG 2022,
Sect. 10; microlensing surveys (HSC, OGLE, EROS, MACHO) and LVK sub-solar
searches.

Already in L2, not repeated here: the constraint families and the
individual limits in `results.md#primordial-black-holes`; the systematics
table (halo model, clustering, OGLE–MACHO dispute, accretion, withdrawn
white-dwarf and femtolensing limits) in
`systematics.md#primordial-black-hole-constraints`; formation routes and
the asteroid window in `physics-and-methods.md#primordial-black-holes`; the
LVK and OGLE debates in
`open-questions.md#primordial-black-holes-as-dark-matter-and-as`.

## How it is done
<!-- key: how-it-is-done -->

### The common structure
<!-- key: the-common-structure -->

Notation of Carr et al. 2026 (arXiv:2601.06024): f_PBH = Ω_PBH/Ω_DM;
ψ(M) ≡ df_PBH/d ln M, so that ∫ψ d ln M = f_PBH [src: Sect. VI]. A
monochromatic curve has two parameters (M, f_PBH) and bounds the total
f_PBH, not the fraction in a mass interval, so ψ cannot be laid over it
[src: Sect. VI].

Any observable A that each PBH affects independently is linear in ψ:
A[ψ] = A₀ + ∫ d ln M A₁(M) ψ(M) (Eq. 26), with A₀ the value without PBHs
and A₁ a kernel set by the physics and the experiment; the bound
A[ψ] ≤ A_exp (Eq. 25) gives, for a monochromatic function at M_c,
f_PBH(M_c) ≤ (A_exp − A₀)/A₁(M_c) ≡ f_max(M_c) (Eq. 27) [src: Sect. VI].
A published monochromatic curve therefore *is* the kernel, up to
normalisation, and everything below is a way of computing A₁ and A_exp.

### Microlensing, step 1: the rate model
<!-- key: microlensing-step-1-the-rate-model -->

Optical depth (HSC, Niikura et al. 2019, arXiv:1701.02151, Eq. 11):
τ = f_PBH ∫₀^{d_s} dd ρ_DM(d)/M π R_E²(d, M), the probability that a source
lies inside a lens's Einstein radius R_E, i.e. magnification A ≥ 1.34 [src:
Sect. 1.2]. Because R_E² ∝ M, τ does not depend on M; τ ~ 10⁻⁶ towards M31
against ~10⁻⁷ towards the LMC, with the Milky Way and M31 haloes
contributing roughly equally [src: same]. The rate needs a velocity model:
an isotropic Maxwellian with v_c(r) = √(G M_NFW(<r)/r) (Eqs. 12–13), and the
differential rate dΓ of lenses entering the microlensing tube (Eq. 14) [src:
same].

Halo models used:

| Analysis | Milky Way halo | Second halo | Place read |
|---|---|---|---|
| HSC (M31) | NFW, M_vir = 10¹² M☉, ρ_c = 4.88 × 10⁶ M☉ kpc⁻³, r_s = 21.5 kpc | M31 NFW, M_vir = 1.6 × 10¹² M☉, ρ_c = 4.96 × 10⁶ M☉ kpc⁻³, r_s = 25 kpc; d_s = 770 kpc | arXiv:1701.02151, Sect. 1.2 |
| OGLE (LMC, 20 yr) | contracted halo fitted to the Gaia DR2 rotation curve, 0.97 × 10¹² M☉ within 200 kpc; Maxwellian with 1D dispersion V₀(R)/√2 | LMC Hernquist, 1.49 × 10¹¹ M☉, scale 17.1 kpc | arXiv:2403.02386, Methods, sections "Milky Way halo" and "LMC halo" |

HSC chose its NFW parameters because they reproduce the observed rotation
curves of both galaxies, and ignored any matter between them [src:
arXiv:1701.02151, Sect. 1.2]. In OGLE's halo the mean timescale is
t_E = 62 d √(M/M☉) [src: arXiv:2403.02386, Methods].

### Microlensing, step 2: the foreground lenses
<!-- key: microlensing-step-2-the-foreground-lenses -->

OGLE models the lenses that are not dark matter: Milky Way thin and thick
disks (two alternative models, with total masses differing by a factor 2.6)
and LMC self-lensing (disk plus bar) [src: arXiv:2403.02386, Methods]. The
expected stellar events are 5.7 (LMC) plus 7.0 or 14.7 (Milky Way disk),
i.e. 12.7 or 20.4 against 13 observed; the heavier disk is still allowed
(Poisson probability 5.6% of 13 or fewer given 20.4) [src: Methods, "Can
all microlensing events…"]. HSC has no stellar-lens model: it
rejects variable candidates that fail the light-curve cuts (χ², asymmetry,
no clear peak, artefacts near bright stars, asteroids) and conservatively
counts its one surviving candidate as real [src: arXiv:1701.02151,
Sect. 3.2, Figs. 15–16; abstract text].

### Microlensing, step 3: detection efficiency and sources
<!-- key: microlensing-step-3-detection-efficiency-and -->

Efficiency ε is computed by injecting simulated events. HSC draws peak
time, impact parameter u_min ∈ [0, 1] and t_FWHM ∈ [0.01, 25,000] s, adds
the measured photometric noise, runs all cuts, and repeats with 10,000
light curves per patch and source flux; a second, image-level injection
with GalSim agrees [src: arXiv:1701.02151, Sect. 4.1]. The recovered fraction
is about 70–60% for m_r = 23–24 and t_FWHM ≈ 0.1–3 h, falling to 30–20%
for m_r = 25–26 [src: abstract text]. Source counts come from peaks in the
best-seeing coadd, per magnitude bin [src: Sect. 4.2]. OGLE restricts
events, efficiency and source counts to I < 22 mag [src:
arXiv:2403.02386, Discussion].

### Microlensing, step 4: the likelihood
<!-- key: microlensing-step-4-the-likelihood -->

- **Counting (HSC).** N_exp = ∫ (dN_event/d ln t_FWHM)(dN_s/dm_r) ε, Poisson;
  with one candidate kept, the 95% bound is P(0) + P(1) ≥ 0.05, i.e.
  N_exp ≤ 4.74 [src: arXiv:1701.02151, abstract text]. About 1000 events
  would be expected for M ~ 10⁻⁹ M☉ PBHs making all the dark matter, hence
  f_PBH ≃ 10⁻³ [src: same].
- **Null hypothesis (OGLE).** All observed events assigned to stars:
  L = e^(−N_exp(f, M)) (Eq. 4), flat prior f ∈ [0, 10], MCMC, 95% upper limit,
  on a grid of 101 masses (10⁻⁶–10⁴ M☉) × 101 values of f (10⁻⁴–10) [src:
  arXiv:2403.02386, Methods].
- **Full timescale likelihood (OGLE).**
  L(f, M) = e^(−N_exp) Π_i [N_s Δt dΓ/dt_E(t_E,i) ε(t_E,i)] (Eq. 1), with
  dΓ/dt_E the sum of f × (Milky Way halo + LMC halo) and the stellar terms
  (Eq. 2) and N_exp from Eq. 3; each event's t_E is averaged over 2 × 10⁵
  posterior samples because some have > 20% errors (Eq. 6) [src:
  arXiv:2403.02386, Methods, section "Full limits on PBHs"]. With one of
  its two Milky Way disk models the best point (log M, log f) = (−1.5,
  −2.55) is preferred over log f = −4 by only Δχ² ≈ 3.7; with the other,
  (−1.8, −2.85) and Δχ² ≈ 1.5; the preference is driven by one 7-day event
  [src: arXiv:2403.02386, Methods, section "Full limits on PBHs"].

### Microlensing, step 5: optics corrections at low mass
<!-- key: microlensing-step-5-optics-corrections-at-low -->

HSC includes the finite source size, assuming a solar radius for all M31
sources because its depth (r ≈ 26) reaches main-sequence or subgiant stars,
and wave optics in the r band (~600 nm) [src: arXiv:1701.02151, Sect. 5].
Finite source dominates; the two together weaken the bound below
~10⁻⁷ M☉ and remove it below ~10⁻¹¹ M☉ [src: Fig. 5 caption, Sect. 5]. The
authors warn that giants among the sources would make the finite-source
effect larger than assumed [src: abstract text].

### LVK mergers, step 1: the rate model
<!-- key: lvk-mergers-step-1-the-rate-model -->

Early-Universe two-body binaries dominate. Andrés-Carcasona et al. 2024
(arXiv:2405.05732, Eq. 12) write
dR/dm₁dm₂ = 1.6 × 10⁶ Gpc⁻³ yr⁻¹ f_PBH^(53/37) (t/t₀)^(−34/37)
(M/M☉)^(−32/37) η^(−34/37) S ψ(m₁)ψ(m₂)/(m₁m₂), with M = m₁ + m₂,
η = m₁m₂/M², and here ψ normalised to unity [src: Sect. III.1]. The
suppression factor S = S₁ S₂(z): S₁ (Eq. 14) removes initial configurations
with a third PBH too close and includes matter perturbations through
σ_M ≃ 0.004; S₂ ≈ min[1, 0.01 χ^(−0.65) e^(−0.03 ln²χ)] with
χ = (t/t₀)^0.44 f_PBH (Eq. 17) accounts for later disruption, valid for
z ≲ 100 [src: same]. A three-body channel (Eq. 18) is added with γ = 1 and
K = 4, "as suggested by numerical simulations"; the most conservative
choice would be γ = 2, K = 1 [src: same]. It dominates above f_PBH ≈ 0.1
and strengthens the edges of the excluded region [src: Sect. IV.1].

Other rate models:

- **LVK sub-solar search** (LVK 2021, arXiv:2109.12197): an equal-mass
  population uniformly distributed in comoving volume, two nearest
  neighbours torqued by the next closest PBH (Eqs. 3–4), Planck cosmology,
  no suppression factor; the authors note that binary disruption by close
  PBHs, clusters and matter inhomogeneities suppress the rate and would
  loosen their bound [src: Sect. III, App. A].
- **Clustered PBHs** (Jedamzik 2020, arXiv:2007.03565): early-Universe
  binaries are taken as negligible (from a companion paper) and the rate is
  computed for mergers inside PBH clusters, with a QCD-epoch mass function
  or one from a peak in the curvature spectrum [src: abstract].

### LVK mergers, step 2: the likelihood
<!-- key: lvk-mergers-step-2-the-likelihood -->

Hierarchical: L({d}|Λ) ∝ e^(−N(Λ)) Π_i ∫ L(d_i|θ) π(θ|Λ) dθ (Eq. 1),
evaluated by reweighting each event's posterior samples (Eq. 2) with at
least 20 effective samples per event (Eq. 3) [src: arXiv:2405.05732,
Sect. II]. N(Λ) = T ∫ p_det π (Eq. 4) uses a semi-analytic detection
probability with SNR threshold 8 (Eqs. 5–6), and injections with
N_eff,inj > 4 N_obs (Eq. 9) [src: same]. The hyperprior is
π = (1 + z)⁻¹ dV_c/dz dR/dm₁dm₂ (Eq. 7) [src: same]. Three readings of the
same catalogue [src: Sects. II, IV]:

1. **All events astrophysical**: L ∝ e^(−N), and the 2σ exclusion is the
   region where N > 3 [src: arXiv:2405.05732, Sect. II]. The abstract's
   bound, f_PBH ≲ 10⁻³ over 1–200 M☉ "in every scenario", is the one quoted
   in L2 [src: arXiv:2405.05732, abstract].
2. **Agnostic**: in each primary-mass band, all events are taken as
   primordial; the combined posterior is the maximum of the individual
   ones — the least restrictive case [src: Sect. II].
3. **Joint PBH + astrophysical fit**: POWER LAW + PEAK for astrophysical
   binaries, log-normal PBHs (σ = 0.6), nested sampling, priors
   f_PBH ~ LogU(10⁻⁵, 1), m_c ~ LogU(0.1, 10³) M☉ (Table 2), using events
   with SNR > 11 and inverse false-alarm rate > 4 yr [src: arXiv:2405.05732,
   Sect. IV.2, Table 2].

Other likelihoods:

- **Mixed with astrophysical channels** (Franciolini et al. 2021,
  arXiv:2105.03349): hierarchical Bayesian inference on GWTC-2 mixing a PBH
  population with common-envelope (CE), globular-cluster (GC),
  nuclear-star-cluster (NSC) and stable-mass-transfer (SMT) channels, with
  free mixing fractions; p_det from the same single-detector semi-analytic
  method with SNR threshold 8; uniform hyperpriors, the accretion cut-off
  redshift capped at 30, above which accretion is negligible [src: SM
  Sect. A.1].
- **Binned mass function** (Chen, Yuan & Huang 2021, arXiv:2108.11740): a
  model-independent binned reconstruction of the PBH mass function from
  GWTC-3 [src: abstract].
- **Non-detection, sub-solar masses** (LVK O3a): no candidate in three
  pipelines (most significant false-alarm rate 0.14 yr⁻¹); ⟨VT⟩ from
  injections with 0.2 < m₁ < 10 M☉, 0.2 < m₂ < 1 M☉, 0.1 < q < 1, in nine
  chirp-mass bins over 0.17–2.39 M☉; a loudest-event 90% limit R₉₀ = 2.3/⟨VT⟩
  per bin, the rate taken constant since only z ≲ 0.12 is reached [src:
  arXiv:2109.12197, Sect. III, Eqs. 1–2]. The pipelines' ⟨VT⟩ agree within
  O(30%) and MBTA is fiducial; calibration (≲ 10% in ⟨VT⟩) is neglected
  [src: same]. The rate limit is equated to the model rate and inverted at
  each mass (App. A).

### Evaporation, in one paragraph
<!-- key: evaporation-in-one-paragraph -->

Hawking temperature T_BH ≈ 10⁴ (M/10⁹ g)⁻¹ GeV (Eq. 21); mass loss
summed over species lighter than T_BH with tabulated greybody
coefficients (Eq. 22); lifetime τ = 0.4 s (M/10⁹ g)³ for non-spinning
holes (Eq. 23); a non-spinning PBH of ≈ 5 × 10¹⁴ g ends its evaporation
today; below 2 × 10¹⁴ g quark and gluon jets fragment, so secondary
emission must be added; near-extremal spins halve the lifetime [src:
arXiv:2601.06024, Sect. III]. The constraint families then follow as in
L2 (BBN 10⁹–10¹³ g, CMB above 10¹³ g, photon background and Voyager to
~10¹⁷ g) [src: Sect. IV.1.1]. One family read at source: Voyager 1, beyond
the heliopause, measures the sub-GeV e± that evaporating PBHs of M ≲ 10¹⁷ g
inject and that the solar field hides from Earth-bound detectors; with a
two-zone diffusion model (K = K₀ β (ℛ/GV)^δ, convection, reacceleration,
halo half-height of a few kpc) PBHs below 10¹⁶ g cannot exceed 0.1% of the
dark matter, less for a log-normal mass function; the limit rests on local
measurements, complementary to cosmological ones (Boudaud & Cirelli 2018,
arXiv:1807.03075) [src: abstract; main text].

### From monochromatic to extended mass functions
<!-- key: from-monochromatic-to-extended-mass-functions -->

From Eqs. 26–27, an extended ψ is allowed if
∫ d ln M ψ(M)/f_max(M) ≤ 1 (Eq. 28); several observables j combine in
quadrature, Σ_j [∫ d ln M ψ/f_max,j]² ≤ 1 (Eq. 29) [src: arXiv:2601.06024,
Sect. VI]. The quadrature rule comes from a χ² sum over independent
observables whose mean coincides with f_PBH = 0 (Carr et al. 2017,
arXiv:1705.05567, App. A, Eqs. 17–20). Combining first into one
monochromatic curve, f_max = (Σ f_max,j⁻²)^(−1/2) (Eq. 21), and then
applying Eq. 28 always overestimates the constraint, by the triangle
inequality (Eq. 22), unless the f_max,j are proportional [src: same].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Halo model
<!-- key: halo-model -->

- **OGLE's test.** Limits scale roughly as 1/τ. Lighter Einasto haloes
  fitted to recent rotation curves give τ ≈ 4.2 × 10⁻⁷ and 4.1 × 10⁻⁷
  towards the LMC centre against 4.4 × 10⁻⁷ for the fiducial; the more
  compact haloes put lenses closer (⟨D_l⟩ = 7.6 and 8.5 kpc against 12.5),
  which raises both θ_E and the relative proper motion, effects that
  "nearly cancel", leaving timescales and rates similar [src:
  arXiv:2403.02386, Methods, section "Discussion"].
- **The critique.** Hawkins 2025 argues that OGLE's halo, built on a
  rotation curve with little data beyond 25 kpc, has v_c ≈ 190 km s⁻¹ at
  50 kpc, "virtually the same" as MACHO's heavy-halo Model S, against
  ≈ 130 km s⁻¹ from Gaia DR3, and that declining rotation curves admit
  haloes consistent with MACHO's τ for a 100% compact-object halo [src:
  arXiv:2509.05400, Sect. 3.6]. He also notes that with so few OGLE events
  the halo choice matters little for the present limit [src: same].
- **Reading.** The two statements concern different quantities: OGLE tests
  how τ moves for its alternative haloes; Hawkins disputes the velocity
  normalisation at the LMC distance. A referee should ask for the limit
  under a halo matching the Gaia DR3 v_c at the LMC distance, which
  arXiv:2509.05400 (Sect. 3.6) takes as 50 kpc.

### Null hypothesis or timescale likelihood
<!-- key: null-hypothesis-or-timescale-likelihood -->

Ignoring timescales (Eq. 4) and using them (Eq. 1) agree for
M ≲ 10⁻⁴ M☉ and M ≳ 10 M☉, where no stellar lens mimics a PBH event; in
between, the full likelihood is weaker by up to Δlog f = 0.59 dex (factor
3.9) at log M = −0.6; the two disk models differ by at most 0.18 dex
(log M = −0.1) [src: arXiv:2403.02386, Methods, "Full limits"].

### Event selection and efficiency
<!-- key: event-selection-and-efficiency -->

Hawkins argues that OGLE's weak constraint on points in the bump and its
strong goodness-of-fit cut, in one passband and crowded fields, reject real
events; if ε is not lowered accordingly, N_exp is overestimated and the
limit is too strong [src: arXiv:2509.05400, Sects. 3.3–3.4]. He proposes
the overlap between surveys observing the same field at the same time as
an independent check of ε [src: Sect. 3.4]. OGLE's own robustness test:
limiting magnitudes I < 21.5 and I < 21 change the limits by at most 0.10
and 0.20 dex [src: arXiv:2403.02386, Discussion].

### Source size and optics
<!-- key: source-size-and-optics -->

The HSC curve below ~10⁻⁷ M☉ depends on the source-radius assumption; the
wave-optics correction matters less than finite source size [src:
arXiv:1701.02151, Sect. 5]. This is the physics that sets the upper edge
of the asteroid window (L2).

### LVK: what the events are taken to be
<!-- key: lvk-what-the-events-are-taken-to-be -->

Allowing any fraction of events to be primordial weakens the bounds
relative to the all-astrophysical case [src: arXiv:2405.05732,
Sect. IV.2]. In the joint fit the astrophysical base rate drops from
log₁₀ R₀ = −0.16(13) (astrophysical only) to −0.48(13), meaning the fit
prefers some PBH sub-population [src: same]. The joint fit gives a
stronger sub-solar constraint than the agnostic one, which the authors
attribute to insufficient resolution of the scan [src: same].

Other readings of the same catalogues, as their authors state them:

- The PBH fraction "depends significantly on the set of assumed
  astrophysical models": PBHs are favoured against GC and NSC channels, but
  a dominant SMT channel "drastically reduces the need for PBHs", except
  for the rate of mass-gap events such as GW190521; without GW190521 the
  evidence for CE+GC+SMT and CE+GC+SMT+PBH becomes comparable; SMT would
  need a fraction 0.34 ± 0.22 [src: arXiv:2105.03349, abstract and
  Discussion].
- GW190521 fits a PBH reading naturally, while the light events (GW190814,
  GW190425, GW200105, GW200115) are "quite unlikely" to be binary PBHs,
  because the PBH rates are much smaller than LVK's [src: arXiv:2108.11740,
  abstract].
- In the opposite direction, QCD-epoch PBHs making all the dark matter and
  merging in clusters reproduce the heavy-BH rates and GW190814, and
  explain why no light–light merger has been seen; the authors call the
  match "tantalizing" [src: arXiv:2007.03565, abstract]. This rests on
  early binaries being negligible, the opposite of the two-body dominance
  assumed by arXiv:2405.05732 (Step 1).
- Below 1 M☉, the LVK non-detection gives f_PBH ≲ 6% for equal-mass binaries
  of 0.2–1.0 M☉, under the unsuppressed rate [src: arXiv:2109.12197, Sect.
  III].

### LVK: mass-function shape
<!-- key: lvk-mass-function-shape -->

Critical-collapse mass functions with three non-Gaussianity models
(non-linear δ–ζ relation only, quasi-inflection point, curvaton), at
f_PBH ≃ 10⁻³, give "nearly identical" limits close to the monochromatic
one; the QCD-induced enhancement near 1 M☉ has no noticeable effect [src:
arXiv:2405.05732, Sect. IV.1]. The sub-solar tail, from the three-body
channel, is more sensitive to the width than the super-solar part [src:
same]. For mass functions spanning several decades the merger-rate formula
is less reliable, since it assumes PBHs of similar mass [src: same].

### Extended mass functions in general
<!-- key: extended-mass-functions-in-general -->

Constraints usually become more stringent for extended functions than for
monochromatic ones [src: arXiv:1705.05567, abstract]; the asteroid window
closes for log-normal widths σ ≳ 2.5, while the narrow critical-collapse
function (γ = 0.36) changes the limits only mildly [src: arXiv:2601.06024,
Sect. VI]. The linear-kernel method fails for constraints that depend on
several PBHs at once — mergers, Poisson clustering at f_PBH ~ 1, Lyα,
dynamical heating, mass segregation in dwarf galaxies — and accretion can
evolve ψ, so the review treats its ψ as effective mass functions [src:
same].

### Merger-rate conventions
<!-- key: merger-rate-conventions -->

The review writes the rate with f_PBH^(−21/37) (arXiv:2601.06024,
Eq. 33) [src]; the LVK O3 PBH paper writes it with f_PBH^(53/37)
(arXiv:2405.05732, Eq. 12) [src].

The two exponents describe the same rate: in the review ψ is normalised
to f_PBH, so ψ(m₁)ψ(m₂) carries f_PBH squared, while the other paper
normalises ψ to one [der: from the normalisations stated in
arXiv:2601.06024, Sect. VI and arXiv:2405.05732, Sect. III.1]. The
LVK O3 PBH paper warns that different conventions are in use (its
footnote 3) [src: arXiv:2405.05732, footnote 3].

The rate grows as (1 + z)^(51/37) in matter domination, unlike the
astrophysical rate that falls above z ≈ 3 [src: arXiv:2601.06024,
Sect. VII.2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Optical depth, all-PBH halo | ~10⁻⁶ (M31); 4.4 × 10⁻⁷ (LMC centre, fiducial) | HSC; OGLE | arXiv:1701.02151; arXiv:2403.02386 | Sect. 1.2; Methods section "Discussion" |
| Poisson 95% bound, one candidate | N_exp ≤ 4.74 | HSC | arXiv:1701.02151 | abstract text |
| HSC cadence, sensitivity | 2 min, 7 h; 4 min ≲ t_FWHM ≲ 3 h | HSC | arXiv:1701.02151 | Sect. 4.1 |
| HSC efficiency | 70–60% (m_r 23–24), 30–20% (m_r 25–26) | HSC | arXiv:1701.02151 | abstract text |
| Mean halo timescale | t_E = 62 d √(M/M☉) | OGLE | arXiv:2403.02386 | Methods section "Milky Way halo" |
| Expected stellar events | 12.7 or 20.4 (observed 13) | OGLE LMC | arXiv:2403.02386 | Methods section "Can all microlensing events detected by OGLE be explained by non-dark-matter objects?" |
| Full vs null likelihood | ≤ 0.59 dex weaker (log M = −0.6) | OGLE LMC | arXiv:2403.02386 | Methods section "Full limits on PBHs" |
| Disk-model effect | ≤ 0.18 dex (at log M = −0.1) | OGLE LMC | arXiv:2403.02386 | Methods section "Full limits on PBHs" |
| Limiting-magnitude effect | ≤ 0.10 dex (I 21.5), ≤ 0.20 dex (I 21) | OGLE LMC | arXiv:2403.02386 | Methods section "Discussion" |
| v_c at 50 kpc | 190 (OGLE model) vs 130 km s⁻¹ (Gaia DR3) | critique | arXiv:2509.05400 | Sect. 3.6 |
| Merger-rate normalisation | 1.6 × 10⁶ Gpc⁻³ yr⁻¹ | LVK O3 PBH | arXiv:2405.05732 | Eq. 12 |
| σ_M | ≃ 0.004 | LVK O3 PBH | arXiv:2405.05732 | Eq. 14 |
| Three-body parameters | γ = 1, K = 4 (conservative γ = 2, K = 1) | LVK O3 PBH | arXiv:2405.05732 | Sect. III.1 |
| Exclusion criterion (no PBH events) | N > 3 (2σ) | LVK O3 PBH | arXiv:2405.05732 | Sect. II |
| Detection threshold | SNR_c = 8; joint fit SNR > 11, IFAR > 4 yr | LVK O3 PBH | arXiv:2405.05732 | Sects. II, IV.2 |
| Sub-solar limit | f_PBH ≲ 6% (equal mass, 0.2–1.0 M☉, unsuppressed rate) | LVK O3a SSM | arXiv:2109.12197 | Sect. III |
| SSM rate limit | R₉₀ = 2.3/⟨VT⟩; 9 chirp-mass bins, 0.17–2.39 M☉; pipelines within O(30%) | LVK O3a SSM | arXiv:2109.12197 | Sect. III |
| SMT fraction needed | 0.34 ± 0.22 | GWTC-2 mixed channels | arXiv:2105.03349 | abstract |
| Voyager e± limit | f_PBH < 0.1% for M < 10¹⁶ g | Voyager 1 | arXiv:1807.03075 | abstract |
| Evaporating today | M ≈ 5 × 10¹⁴ g (non-spinning) | review | arXiv:2601.06024 | Sect. III |
| Window closure | log-normal σ ≳ 2.5 | review | arXiv:2601.06024 | Sect. VI |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Laying ψ over a monochromatic curve.** The two are different
  quantities [src: arXiv:2601.06024, Sect. VI]. Test: apply Eq. 28 per
  observable and Eq. 29 for combinations.
- **Combining before converting.** A single combined monochromatic curve
  overstates the extended-function constraint [src: arXiv:1705.05567,
  App. A, Eq. 22]. Test: keep each observable's f_max,j separate.
- **Applying the linear method where it fails.** Merger, clustering,
  Lyα and dynamical limits are not linear in ψ [src: arXiv:2601.06024,
  Sect. VI]. Test: recompute those limits for the specific ψ.
- **Halo normalisation.** A heavy halo at the LMC distance strengthens the
  limit [src: arXiv:2509.05400, Sect. 3.6]; OGLE's alternative haloes move
  τ by ≲ 7% [src: arXiv:2403.02386, Discussion; der: 4.1/4.4]. Test: limit
  under a halo matching the outer rotation curve.
- **Efficiency not matched to the cuts.** Shows up as fewer events than
  predicted by known stars [src: arXiv:2509.05400, Sects. 3.3–3.4]. Test:
  image-level injections (HSC did both, arXiv:1701.02151, Sect. 4.1) and
  overlap with another survey.
- **One short event driving a "detection".** OGLE's best point rests on a
  7-day event; without it log f = −4 is disfavoured by < 1.5 in Δχ² [src:
  arXiv:2403.02386, Methods section "Full limits on PBHs"]. Test: drop-one-event.
- **Source radius.** Giants among the sources make finite-source suppression
  larger [src: arXiv:1701.02151, abstract text]. Test: source-size
  distribution from the luminosity function.
- **Merger-rate convention.** A factor f_PBH² hidden in ψ. Test: check the
  normalisation of ψ against the power of f_PBH.
- **Binary disruption mis-modelled at large f_PBH.** S₂ is valid only for
  z ≲ 100 and the three-body channel matters above f_PBH ≈ 0.1 [src:
  arXiv:2405.05732, Sects. III.1, IV.1].
- **High-velocity PBHs.** A large recoil velocity for all PBHs would shift
  OGLE's limits to higher masses [src: arXiv:2403.02386, Methods].

## Reading list
<!-- key: reading-list -->

- Review: Carr et al. 2026, arXiv:2601.06024 — constraint families,
  evaporation, extended mass functions (Sect. VI), merger rate (Sect. VII.2).
- Method: Carr et al. 2017, arXiv:1705.05567 — linear kernel, quadrature
  combination, extended mass functions.
- Application: Niikura et al. 2019, arXiv:1701.02151 — full microlensing
  pipeline from rate to Poisson bound, finite source and wave optics.
- Application: Mróz et al. 2024, arXiv:2403.02386 — halo, disk and LMC
  models; null and timescale likelihoods; robustness tests.
- Application: Andrés-Carcasona et al. 2024, arXiv:2405.05732 — merger
  rate with suppression, hierarchical likelihood, three readings of LVK
  data.
- Application: LVK 2021, arXiv:2109.12197 — sub-solar search, ⟨VT⟩ and
  loudest-event limit, unsuppressed PBH rate (Sect. III, App. A).
- Application: Franciolini et al. 2021, arXiv:2105.03349 — PBHs mixed with
  astrophysical channels in a hierarchical fit.
- Application: Chen, Yuan & Huang 2021, arXiv:2108.11740 — binned mass
  function from GWTC-3 (abstract).
- Critique: Jedamzik 2020, arXiv:2007.03565 — cluster mergers as evidence
  for PBH dark matter (abstract).
- Application: Boudaud & Cirelli 2018, arXiv:1807.03075 — Voyager 1 e±
  evaporation limit.
- Critique: Hawkins 2025, arXiv:2509.05400 — passbands, selection,
  efficiency, self-lensing, halo models in the OGLE analysis.

## Not verified
<!-- key: not-verified -->

- The Einstein-radius and timescale formulae (HSC Eqs. 1–7) and the full
  rate integral after Eq. 14 were not read beyond what is cited.
- OGLE's detection efficiency and event sample come from a companion paper
  (Mróz et al. 2024b, as cited by both sides), not read.
- No OGLE reply to arXiv:2509.05400 was searched.
- The derivation of S₁ and S₂ (Raidal et al. and Hütsi et al., as cited
  in arXiv:2405.05732) was not read; no identifiers recorded.
- Evaporation constraints were read only in the review summary, except
  Voyager (arXiv:1807.03075, abstract and propagation text); the BBN, CMB
  and photon-background analyses were not.
- The LVK O3b and O4 sub-solar searches, the companion paper of
  arXiv:2007.03565 and the bodies of arXiv:2108.11740 and arXiv:2007.03565
  were not read. The Lyα, dynamical-heating and dwarf-galaxy limits named
  in "Extended mass functions in general" are known only through the
  review.
