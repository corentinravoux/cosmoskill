# Megamasers — cosmo-distance-ladder-h0 dossier

Scope: how a maser-disc distance is fitted from VLBI spot catalogues (data,
warped Keplerian model, error floors, priors, outliers, sampling) and how
the disc distances become an H0 (velocity likelihood, flow model, distance
prior, selection), with the choices that separate the three current
megamaser values, and how the NGC 4258 distance is used and tested by the
ladders downstream. The disc data come from one consortium (MCP and the
NGC 4258 VLBI team); the modelling, the flow corrections and the anchor
tests have independent groups, cited per step.
Snapshot: 2026-10-22.
From: Verde et al. 2023 review (arXiv:2311.13305), Sects. 2.2.5 and 2.4.4;
Freedman & Madore 2023 (arXiv:2309.05618), Sect. 8.2; Megamaser Cosmology
Project (arXiv:2001.09213).

Already in L2, not repeated here: the principle D = r/θ, the six-galaxy
sample and the NGC 4258 history in `physics-and-methods.md#megamasers`
and `physics-and-methods.md#geometric-anchors`; the 2020 and 2026 values
in `results.md#one-step-routes-independent-of-the-ladder-and`; the two
readings of 2026 in `open-questions.md#megamasers-73-9-71-6-or-67`;
budget terms (NGC 4258 statistical and systematic split, velocity noise,
variant spreads) in `systematics.md#error-budgets-term-by-term` and
`systematics.md#megamasers-sirens-chronometers`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Data per maser spot
<!-- key: step-1-data-per-maser-spot -->

Each spot gives four measurements: sky offsets (x, y), Doppler velocity V
and line-of-sight acceleration A [src: arXiv:1908.05625, Sect. II].
Positions and velocities come from VLBI; accelerations from time-varying
Doppler shifts in spectra from the VLBI epochs plus single-dish (GBT) and
VLA monitoring, by a Gaussian decomposition fitted to spectra of several
epochs at once to follow velocity drifts [src: arXiv:1307.6031, Sect. II].
For NGC 4258, 18 VLBI epochs gave ~10,000 data points, binned at
1 km s⁻¹ for fitting [src: same]. Disc spectra show three groups of
features: systemic masers in front of the black hole near the systemic
velocity, and high-velocity masers on the disc midline shifted by several
hundred km s⁻¹ to either side [src: arXiv:2001.09213, Sect. 2, footnote].
Accelerations are measured for only a subset of spots [src:
arXiv:2609.17684, Sect. 3.1].

The NGC 4258 fits of 2013 and 2019 use an averaged data set: spectra of
many epochs reduced to one position, velocity and acceleration per
velocity bin. Van der Boom & Kushnir call this the "single-orbit
assumption" and reject it: a warped disc's near-side "bowl" amplifies
systemic masers over radii of about 3.4–4.1 mas, so one velocity maps to
several positions (ΔX ≈ 50 µas at 425 km s⁻¹ against an averaged error of
≈ 2 µas), and the normalised residuals of the raw positions about the
averaged ones are heavy-tailed, not N(0, 1) [src: arXiv:2601.14374,
Sect. 3.1]. They add that maser lines are a few km s⁻¹ wide, so adjacent
1 km s⁻¹ bins are not independent: the spectra hold fewer than 5
blueshifted, about 10 redshifted and at most 40 systemic masers against
the ~370 independent points implied [src: Sect. 3.2].

### Step 2. The warped Keplerian disc
<!-- key: step-2-the-warped-keplerian-disc -->

As written in the 2026 reanalysis, which reproduces the per-spot
likelihood of the MCP code to a median 5 × 10⁻¹² in log-likelihood [src:
arXiv:2609.17684, Sect. 3.5]:

- Warp: i(r) and Ω(r) expanded to second order about a pivot r_ref near
  the median spot radius, "to decorrelate the warp rates from their
  zero-points" (Eqs. 2–3); i is the inclination (90° edge-on), Ω the
  position angle, r the angular orbital radius in mas [src: Sect. 3.1].
- Sky positions from the disc coordinates (r, φ) and black-hole position
  (x₀, y₀) (Eqs. 4–5); φ = 0 is the near side, systemic features sit near
  φ = 0, π and high-velocity ones near π/2 and 3π/2 [src: same].
- Velocity: V_kep = C_v √[(M_BH/M_⊙)/((r/mas)(D_A/Mpc))], C_v ≈ 0.94 km s⁻¹
  (Eq. 6), and V_i = c[(1 + V_rec/c)(1 + z_D)(1 + z_g) − 1] (Eq. 7), with
  relativistic Doppler including the transverse term (Eqs. 8–11) and
  Schwarzschild gravitational redshift (Eq. 12) [src: same].
- Acceleration: a_los = C_a M_BH cos φ sin i / (r² D_A²),
  C_a = 1.872 × 10⁻⁴ km s⁻¹ yr⁻¹ (Eq. 13) [src: same].

Why accelerations matter: velocities constrain only M_BH/D_A, the
accelerations constrain M_BH/D_A² and break the mass–distance degeneracy
"only partially"; the fit therefore samples η = log[(M_BH/M_⊙)/(D_A/Mpc)]
(Eq. 1) [src: Sect. 3.1]. In an edge-on disc spots at φ and π − φ share
position and velocity but have opposite accelerations; with accelerations
for only some spots the per-spot φ stays bimodal and is marginalised
[src: same, Fig. 2].

The disc likelihood depends only on D_A, so the per-galaxy fit makes no
assumption on H0; a fiducial cosmology only sets the bounds of the uniform
D_A prior [src: Sect. 3.1].

### Step 3. Error floors as parameters
<!-- key: step-3-error-floors-as-parameters -->

Since 2019 the error floors on positions, systemic and high-velocity
velocities and accelerations are free parameters, added in quadrature to
the data errors, which requires keeping the 1/σ prefactor of the Gaussian
in the likelihood; mock discs with known noise recovered it [src:
arXiv:1908.05625, Sect. II]. The reason: the relative weighting of
heterogeneous data affects the fitted parameters, and fixed floors left a
freedom that could bias them [src: same]. Effects: for NGC 4258 the
position floors fell from (10, 20) µas assumed to about (2, 4) µas
measured, halving the statistical distance error [src: same]; for the MCP
galaxies the earlier fixed floors were generally "too conservative"
(UGC 3789 acceleration floor 0.34 ± 0.06 against 0.57 km s⁻¹ yr⁻¹ fixed
before) [src: arXiv:2001.09213, Sect. 2.1]. MCP priors on the floors:
truncated Gaussians 10 ± 5 µas (positions), 2 ± 1 km s⁻¹ (velocities),
0.3 ± 0.15 km s⁻¹ yr⁻¹ (accelerations) [src: Sect. 2]; the 2026
reanalysis uses the same centres and widths with explicit truncation
bounds [src: arXiv:2609.17684, Table 2].

Independent refit of the averaged NGC 4258 data [src: arXiv:2601.14374,
Sect. 2.5]: with the 2013 fixed floors 7.277 ± 0.166 Mpc against the
published 7.596 ± 0.167 (≈ 1.3σ) at χ²_ν ≈ 0.4, so those floors look
"overly conservative"; with the 2019 fitted floors held fixed 7.551 ±
0.072 Mpc but χ²_ν ≈ 1.4 (495 dof, chance probability ≈ 9 × 10⁻⁹); with
free floors 7.547 ± 0.079 Mpc and χ²_ν ≈ 1.2, consistent with Reid et
al. 2019. The authors warn that χ²_ν is not a valid goodness of fit once
floors are fitted, and that the fitted high-velocity velocity floor
exceeds the bin width while the systemic one is below it, which "hint[s]"
at residual systematics [src: Sect. 2.5.3].

### Step 4. Priors and sampling
<!-- key: step-4-priors-and-sampling -->

| Parameter | Prior (2026 reanalysis) [src: arXiv:2609.17684, Table 2] |
|---|---|
| D_A | uniform at stage 1; reweighted to uniform in volume (∝ D²) at stage 2 |
| log M_BH | U(4, 10) (via η) |
| i₀ | sine prior on (65°, 115°) |
| linear warp rates | U(−30, 30) deg mas⁻¹ |
| quadratic warps (optional) | N(0, 90) deg mas⁻² |
| eccentricity components (optional) | N(0, 0.025) each |
| ΔV_sys | N(0, 300) km s⁻¹ |
| per-spot r_i, φ_i | flat r > 0; φ uniform on the side fixed by the spot class |

Sampling: MCP disc fits used Hamiltonian Monte Carlo in PyMC3, matching
the earlier Metropolis–Hastings code with better convergence [src:
arXiv:2001.09213, Sect. 2]. The 2026 reanalysis first locates the global
mode by differential evolution with the per-spot (r, φ) marginalised
numerically (14 disc parameters), then samples with NUTS for the disc
parameters inside a Metropolis-within-Gibbs scheme plus a "reflection
move" between the two φ modes of each high-velocity spot; mode-finding
from random starts is called "the central difficulty" [src:
arXiv:2609.17684, Sect. 3.5]. Van der Boom & Kushnir also marginalise
(r, φ) numerically per maser and sample the global parameters with
dynesty (14 free parameters); they trace the 1.3σ gap to the 2013 value
to the φ degeneracy of the high-velocity masers, and recover 7.58 ± 0.21
Mpc when each maser is instead set at its likelihood-maximising (r, φ),
which they suspect mimics the 2013 sampler [src: arXiv:2601.14374,
Sect. 2.5.1].

### Step 5. Outlier rejection
<!-- key: step-5-outlier-rejection -->

MCP: a blinded, iterative removal of outlying spots at about 3σ [src:
arXiv:2609.17684, Sect. 2.1]. 2026: at the MAP disc parameters each spot
is scored by its largest normalised residual averaged over its conditional
(r, φ) posterior, spots above 2.5σ are removed, and the loop repeats until
stable (at most four rounds); 2σ or 3σ thresholds leave distances
unchanged [src: Sect. 3.3]. The two procedures clip 31 and 32 spots of
686, only 8 in common, with negligible effect on distances [src:
Sect. 2.1].

### Step 6. From distances to H0
<!-- key: step-6-from-distances-to-h0 -->

MCP 2020 [src: arXiv:2001.09213, Sect. 3]: the black hole is assumed to
share the galaxy's distance and redshift (its relative motion is ≪ 1 km s⁻¹
expected, at most a few tens measured). The model distance is the flat-ΛCDM
angular-diameter distance with Ω_m = 0.315; L = L_D L_v, with L_D the
product of the disc posteriors and L_v a velocity term; flat priors;
dynesty. Four velocity treatments:

| Treatment | Velocity term | H0 | Place read |
|---|---|---|---|
| Inflated errors | σ_pec = 250 km s⁻¹ in quadrature, "the upper end" of 150–250 | 73.9 ± 3.0, χ²_ν = 0.6 (ν = 5) | Sect. 3.1 |
| Global distribution | Sivia "conservative" error law, σ_pec fitted: 141 (+185/−80) km s⁻¹ | 74.4 (+3.9/−3.4) | Sect. 3.2 |
| Group velocities | Tully 2015 groups, 150 km s⁻¹ | 73.3 (+2.8/−2.7) | Sect. 3.3 |
| Flow models | 2M++ (Carrick 2015) / CF3 / M2000, 150 km s⁻¹ | 71.8 ± 2.9 / 71.8 (+2.7/−2.6) / 76.9 ± 2.9 | Sect. 3.4 |

The M2000 outlier comes from Great Attractor infall applied to three hosts
behind it, which adds 300–600 km s⁻¹ to their recession velocities [src:
Sect. 3.4].

Other treatments of the same six MCP distances:

- Boruah, Hudson & Lavaux 2021: a volumetric distance prior and
  marginalisation of the peculiar-velocity correction along each line of
  sight, with the 2M++ reconstruction or a kernel-smoothed Tully–Fisher
  field (SuperTF; 6dF not usable, all six hosts are northern); H0 = 69
  (+2.9/−2.8) with 2M++ [src: arXiv:2010.01119, abstract, Sect. 6.3].
  A uniform instead of volumetric prior biases distances low and H0 high,
  by ~1 km/s/Mpc here [src: Sect. 6.3, Table 3].
- Barua, Ramakrishnan & Desai 2025: frequentist profile likelihood over
  the six velocity nuisance parameters gives 73.5 (+3.0/−2.9), within 0.2σ
  of the MCP Bayesian 73.9 ± 3.0, with consistent intervals [src:
  arXiv:2502.11998, abstract].

2026 hierarchical form [src: arXiv:2609.17684, Sect. 3.4, Eq. 24]: each
galaxy's distance posterior (kernel density, flat prior) is reweighted by
D²; the redshift likelihood is a Gaussian of width σ_pec about
cz_pred with 1 + z_pred = (1 + z_cosmo)(1 + V_pec/c) (Eqs. 21–22);
V_pec = β V_recon(n̂, D) + n̂·V_ext (Eq. 23); a selection probability S
per galaxy and a normalisation Z(Λ)^(−N_gal). Baseline: Manticore-Local
with β = 1 fixed (non-linear field at fixed cosmology), averaged over
posterior realisations; linear 2M++ variant with β ~ N(0.43, 0.02); V_ext
prior calibrated on Cosmicflows-4 Tully–Fisher, 111 ± 15 km s⁻¹ (Manticore)
or 201 ± 16 km s⁻¹ (linear); σ_pec Maxwell prior with mean 250 km s⁻¹;
NUTS in BlackJAX [src: same]. The two-stage result was checked against a
full joint fit on test cases [src: same, footnote]. NGC 4258 is left out
of the H0 sample: it carries little H0 information and anchors the ladder
[src: Sect. 4.4].

Selection: the parent sample is flux-limited, and the MCP pipeline (AGN
selection, GBT detection, triple-peaked spectrum, VLBI and monitoring,
suitability for the disc model) cannot be reconstructed from published
information, so a soft threshold on redshift is used,
S(cz) = Φ[(cz_lim − cz)/cz_width] (Eq. 25), normalised by Z(Λ) integrated
over volume (Eq. 26); because cz_pred depends on H0, the selection does
not cancel [src: Sect. 3.4].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Velocity noise or velocity field
<!-- key: velocity-noise-or-velocity-field -->

- **Noise only (MCP baseline).** Assumes uncorrelated Gaussian peculiar
  velocities; buys model independence. The critique: it neither removes
  coherent motions nor captures non-Gaussian infall tails, and with six
  objects each velocity matters [src: arXiv:2608.06247, Sect. 2].
- **Flow field.** All three 2026 analyses agree that a reconstruction
  lowers H0 relative to the 2020 baseline (L2). The Manticore velocities of
  the three farthest hosts are larger than the linear 2M++ ones (e.g.
  NGC 5765b: 607 ± 53 against 124 km s⁻¹; NGC 6323: 694 ± 88 against
  414), all positive, and the three lie in one coherent outflow; with all
  velocities positive, uncorrected redshifts bias H0 high [src:
  arXiv:2608.06247, Table 1, Sect. 2].
- **Noise level with a field.** Watkins & Feldman fit one parameter, H0,
  with σ_i² = σ_d,i² + (σ_v/c · dd_m/dz)² (their Eq. 3), and show that
  σ_v moves H0 because a common velocity error down-weights the precise
  objects such as NGC 4258; this dependence "was not explored" by the MCP
  [src: arXiv:2608.06247, Sect. 3]. They reproduce the MCP 2M++ value
  (71.5 ± 2.6 with σ_v = 150 km s⁻¹) as a check and average the likelihood
  over the 80 Manticore realisations rather than averaging velocities,
  because the six velocities of one realisation are correlated [src:
  same].

### Where the field is read
<!-- key: where-the-field-is-read -->

The 2026 reanalysis reimplements the Watkins & Feldman model and recovers
their table to 0.07 km/s/Mpc; without the field their model gives 73.4, so
their velocity treatment lowers H0 by 4.6 [src: arXiv:2609.17684,
Sect. 5.1]. It attributes the gap to its own fiducial (2.7 km/s/Mpc on the
same distances and field) to the lookup radius: the field was read at
0.681 D_A in h⁻¹ Mpc, i.e. at the angular-diameter distance converted with
the box h = 0.681, whereas the box radial coordinate is set by observed
redshifts and should be read at r = hD (comoving) with the sampled h; for
NGC 5765b, which carries 55% of the H0 Fisher information there, this
raises the assigned velocity by ~400 km s⁻¹ [src: same]. Stepwise: five
galaxies and σ_v = 250 km s⁻¹ give 69.4; comoving instead of angular
distance +0.5; sampled h instead of 0.681 +1.5 (remaining steps not read)
[src: same]. Watkins & Feldman's own stated reason for D_A is not given in
the part read; the reanalysis suggests it is the distance the maser
geometry delivers [src: same]. This is one group's diagnosis of the
other; no reply was found in this run.

### Real-space or redshift-space evaluation
<!-- key: real-space-or-redshift-space-evaluation -->

Boruah et al. (2021, arXiv:2010.01119; numbers as described in the
reanalysis) used the MCP distances with the linear field and obtained 70.1 ± 2.9 (uniform distance
prior) or 69.0 (+2.9/−2.8) (uniform in volume). Their shift from 73.9
splits into ~2 from applying the field at all, ~0.6 from a prior flat in
distance instead of the MCP flat prior on latent recession velocity, and
~1 from querying the field at the sampled distance (real space) rather
than at the observed redshift (MCP); every real-space evaluation lies
~1.2 below the redshift-space one [src: arXiv:2609.17684, Sect. 5.1].

### Distance prior and stage-1 prior
<!-- key: distance-prior-and-stage-1-prior -->

The MCP population stage puts a flat prior on each latent recession
velocity, which carries a Jacobian ≈ H0 per galaxy relative to a prior
flat in distance; its stage-1 disc chains use a prior log-flat in D_A, so
the distance "likelihood" is weighted by 1/D_A [src: arXiv:2609.17684,
Sect. 3.5]. The reanalysis uses flat-in-D_A at stage 1 and D² at stage 2,
and states that a uniform-in-volume prior "particularly requires" a
selection term, since without it five draws would sit at larger distances
than observed [src: Sects. 3.5, 5.1]. Dropping the selection term moves its
H0 by −2.2 (L2).

### Linear or quadratic warp, eccentric or circular orbits
<!-- key: linear-or-quadratic-warp-eccentric-or-circular -->

For the five Hubble-flow discs, the eccentric variant returns e consistent
with zero and leaves distances and H0 unchanged, so e = 0 is fixed [src:
arXiv:2609.17684, Sect. 3.1, footnote]. For NGC 4258 the linear warp is
"decisively disfavoured": D_A = 7.416 ± 0.056 (linear), 7.512 ± 0.058
(quadratic), 7.558 ± 0.073 Mpc (quadratic + eccentric, e = 0.0041 ±
0.0009), against 7.576 ± 0.082 ± 0.076 from Reid et al. 2019, whose
e = 0.007 ± 0.001 lies 2.1σ higher [src: Sect. 4.4]. Reid et al. 2019 fit
eccentric orbits and a second-order warp, so these enter its statistical
error; the only remaining systematic is unmodelled spiral structure,
± 0.076 Mpc [src: arXiv:1908.05625, Sect. II].

### Spiral structure in NGC 4258
<!-- key: spiral-structure-in-ngc-4258 -->

A persistent slope of systemic-maser accelerations with impact parameter
and periodic structure in high-velocity positions suggest spiral arms
[src: arXiv:1307.6031, Sect. V.2.1]. A simulated arm of 15% of the disc
mass limit shifted the recovered distance by 3.6%, with tell-tale shifts
of x₀ by ~0.2 mas, systemic velocity by ~40 km s⁻¹ and e by ~0.08; the
fitted systemic velocity (474.3 ± 0.5 km s⁻¹, against 472 ± 4 from Hα) and
e = 0.006 exclude an effect that large, so 1% was adopted [src: same].
Van der Boom & Kushnir show that the averaging alone can also bias the
distance and raise χ²_ν above 1 on synthetic data, an effect of the same
kind as the 1% spiral-structure term [src: arXiv:2601.14374, Sect. 3.1].

### Averaged bins or tracked maser components
<!-- key: averaged-bins-or-tracked-maser-components -->

Instead of averaged bins, van der Boom & Kushnir track individual maser
components across epochs, which needs spatially resolved epochs, so most
epochs are dropped. Their distances span about 6.7 to 8.1 Mpc depending
on how components are selected; "visually and statistically robust fits
can differ by several standard deviations", because the present cadence
cannot follow intrinsically variable masers, and high-cadence monitoring
is needed for this method to give an anchor [src: arXiv:2601.14374,
abstract]. They do not propose a replacement distance. The 2026 MCP-data
reanalysis keeps the averaged per-spot catalogues and refits NGC 4258 to
7.558 ± 0.073 Mpc with an eccentric quadratic warp (above) [src:
arXiv:2609.17684, Sect. 4.4].

## Downstream: NGC 4258 as a ladder anchor
<!-- key: downstream-ngc-4258-as-a-ladder-anchor -->

How each ladder uses the maser distance is in L2
(`results.md#one-step-routes-independent-of-the-ladder-and`); what tests
it:

- **Cepheids, SH0ES.** 669 HST Cepheids in NGC 4258 give a Wesenheit PL
  zero point consistent with the LMC calibration to 0.032 ± 0.044 mag,
  after a metallicity term of −0.20 ± 0.05 mag dex⁻¹ [src:
  arXiv:2203.06681, abstract].
- **Cepheids, critique.** On the earlier (R16) photometry, the LMC DEB
  distance with SH0ES Cepheids places NGC 4258 at 6.98 Mpc against the
  maser 7.58 Mpc, Δμ = 0.177 ± 0.051 mag (≈ 3.5σ, metallicity ignored);
  NGC 4258 alone as anchor gives H0 = 72.0 ± 1.9 (no priors) or 70.3 ±
  1.8 (slope prior), the LMC alone 76.5 ± 1.7 or 74.8 ± 1.6 [src:
  arXiv:2007.10716, Sects. 3.1, 4.1]. The same paper notes that Miras
  give μ_N4258 − μ_LMC = 10.95 ± 0.06, against 10.92 ± 0.04 from DEB +
  maser, which tests his first explanation (an error in the geometric
  distances) and passes it; the abstract proposes instead a 0.1–0.15 mag
  bias in the SH0ES Cepheid PL intercepts and calls an independent
  NGC 4258 distance "particularly critical" [src: Sect. 3.1, abstract].
  With Gaia EDR3 parallaxes added the anchor tension grows: the
  parallaxes and the LMC pull H0 up, the maser anchor down, so the
  three-anchor fits are "statistically inconsistent" [src:
  arXiv:2103.08723, Sect. 3]. The SH0ES Cepheid zero-point agreement
  above uses the later photometry of 669 Cepheids.
- **TRGB, CCHP.** Halo fields give F814W₀ = 25.347 ± 0.014 (stat) ±
  0.042 (sys); with the maser distance M_F814W^TRGB = −4.050 ± 0.028 ±
  0.048 mag, within 1% of the LMC DEB calibration [src: arXiv:2008.04181,
  abstract].
- **Blue supergiants.** The flux-weighted gravity–luminosity relation
  gives m − M = 29.38 ± 0.12, in agreement with the maser distance [src:
  arXiv:2411.07974, abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| MCP disc distances | UGC 3789 51.5 (+4.5/−4.0); NGC 6264 132.1 (+21/−17); NGC 6323 109.4 (+34/−23); NGC 5765b 112.2 (+5.4/−5.1); CGCG 074-064 87.6 (+7.9/−7.2); NGC 4258 7.58 ± 0.11 Mpc | MCP 2020 | arXiv:2001.09213 | Table of Sect. 2 |
| CMB-frame velocities (optical convention) | 3319.9, 10192.6, 7801.5, 8525.7, 7172.2, 679.3 km s⁻¹ (same order) | MCP 2020 | arXiv:2001.09213 | Table of Sect. 2 |
| Velocity measurement errors | 1–2 km s⁻¹ typical | MCP 2020 | arXiv:2001.09213 | Sect. 3 |
| Ω_m effect on D(z) | ≲ 1% for 0 ≤ Ω_m ≤ 0.5 | MCP 2020 | arXiv:2001.09213 | Sect. 3 |
| NGC 4258 error floors (fitted) | σ_x 1.6 ± 0.5 µas, σ_y 4.1 ± 0.5 µas, σ_v,hv 2.25 ± 0.31 km s⁻¹, σ_a 0.46 ± 0.04 km s⁻¹ yr⁻¹ | Reid 2019 | arXiv:1908.05625 | Table 2 |
| NGC 4258 disc | M_BH = 3.98 ± 0.04 × 10⁷ M_⊙; i = 87.05 ± 0.09° at r = 6.1 mas; e = 0.007 ± 0.001 | Reid 2019 | arXiv:1908.05625 | Table 2 |
| NGC 4258 fit quality | χ²_ν = 1.2 for 483 dof (1.4 in 2013) | Reid 2019 | arXiv:1908.05625 | Sect. II |
| Spots per galaxy (updated-all, 2026) | 686 in five tables; NGC 5765b 212 published, 43 removed by MCP | 2026 reanalysis | arXiv:2609.17684 | Sect. 2.1 |
| NGC 6264 acceleration errors | inflated by a median factor 3 in the MCP update | 2026 reanalysis | arXiv:2609.17684 | Sect. 2.1 |
| Outlier threshold | ~3σ (MCP); 2.5σ averaged over (r, φ) (2026) | — | arXiv:2609.17684 | Sects. 2.1, 3.3 |
| V_ext prior | 111 ± 15 km s⁻¹ (Manticore), 201 ± 16 km s⁻¹ (linear) | 2026 reanalysis | arXiv:2609.17684 | Sect. 3.4 |
| β for linear 2M++ | N(0.43, 0.02) | 2026 reanalysis | arXiv:2609.17684 | Sect. 3.4 |
| Field lookup shift, NGC 5765b | ~400 km s⁻¹ | reanalysis of arXiv:2608.06247 | arXiv:2609.17684 | Sect. 5.1 |
| Manticore realisations | 80 | arXiv:2608.06247 | arXiv:2608.06247 | Sect. 3 |
| NGC 4258 distance, independent refit of averaged data | 7.277 ± 0.166 (2013 floors); 7.551 ± 0.072 (2019 floors fixed); 7.547 ± 0.079 Mpc (floors free) | van der Boom & Kushnir 2026 | arXiv:2601.14374 | Sect. 2.5 |
| NGC 4258 distance, tracked components | ~6.7 to 8.1 Mpc across selections | van der Boom & Kushnir 2026 | arXiv:2601.14374 | abstract |
| MCP H0, profile likelihood | 73.5 (+3.0/−2.9) | Barua et al. 2025 | arXiv:2502.11998 | abstract |
| MCP distances, 2M++ LOS marginalisation, volumetric prior | 69 (+2.9/−2.8) | Boruah et al. 2021 | arXiv:2010.01119 | abstract |
| NGC 4258 from LMC DEB + R16 Cepheids | 6.98 Mpc; Δμ = 0.177 ± 0.051 mag against the maser | Efstathiou 2020 | arXiv:2007.10716 | Sect. 3.1 |
| H0, NGC 4258 sole anchor (R16 Cepheids) | 72.0 ± 1.9 (no priors); 70.3 ± 1.8 (slope prior) | Efstathiou 2020 | arXiv:2007.10716 | Sect. 4.1 |
| TRGB zero point from the maser distance | M_F814W = −4.050 ± 0.028 (stat) ± 0.048 (sys) | CCHP, Jang et al. 2020 | arXiv:2008.04181 | abstract |
| Cepheid PL zero point, NGC 4258 vs LMC | 0.032 ± 0.044 mag | SH0ES, Yuan et al. 2022 | arXiv:2203.06681 | abstract |
| FGLR (blue supergiant) modulus | 29.38 ± 0.12 | Kudritzki et al. 2024 | arXiv:2411.07974 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Fixed error floors.** Bias the relative weights of positions,
  velocities and accelerations; fit them as parameters, keeping the 1/σ
  prefactor [src: arXiv:1908.05625, Sect. II].
- **Trapped in one φ mode or a local disc mode.** Test: global search
  before sampling and moves between reflected φ solutions [src:
  arXiv:2609.17684, Sect. 3.5].
- **Spot catalogue version.** The MCP 2026 erratum replaced accelerations
  (NGC 6264) and positions (NGC 6323); published against updated tables
  move H0 by 1.8 to 2.1 (L2) [src: arXiv:2609.17684, Sect. 2.1]. Test: run
  original and updated tables through the same model.
- **Distance prior without selection.** A D² prior needs a selection
  term; Test: compare redshift- and distance-threshold selections [src:
  Sects. 3.4, 5.1].
- **Velocity field read in the wrong coordinate.** Comoving distance in
  h⁻¹ Mpc at the sampled h; test: recover the published velocities by
  interpolation along each line of sight, as the reanalysis did [src:
  Sect. 5.1].
- **Single-σ_v sensitivity.** Test: scan σ_v, or fit it [src:
  arXiv:2608.06247, Sect. 3; arXiv:2001.09213, Sect. 3.2].
- **Leverage of one host.** Leave-one-out jackknife (MCP Table of
  Sect. 3); NGC 5765b dominates in the one-parameter fit [src:
  arXiv:2001.09213, Sect. 3.1; arXiv:2609.17684, Sect. 5.1].
- **Unmodelled disc structure.** Look for shifts in x₀, systemic velocity
  against an independent value, and eccentricity [src: arXiv:1307.6031,
  Sect. V.2.1].
- **Averaged bins treated as independent spots.** Adjacent velocity bins
  share one line; test: fit tracked components or synthetic averaged data
  [src: arXiv:2601.14374, Sects. 3.1–3.2].
- **χ²_ν read as fit quality with fitted floors.** Not χ²-distributed;
  test on mock discs instead [src: arXiv:2601.14374, Sect. 2.5.3].

## Reading list
<!-- key: reading-list -->

- Foundation: Herrnstein et al. 1999, arXiv:astro-ph/9907013 — the
  geometric method on NGC 4258.
- Method: Humphreys et al. 2013, arXiv:1307.6031 — data, accelerations,
  disc model, spiral-structure systematic.
- Method: Reid et al. 2019, arXiv:1908.05625 — error floors as parameters;
  current anchor distance.
- Application: Pesce et al. 2020, arXiv:2001.09213 — four velocity
  treatments and the 73.9 baseline.
- Application/critique: Watkins & Feldman 2026, arXiv:2608.06247 —
  Manticore correction, σ_v dependence.
- Application/critique: Stiskalek & Desmond 2026, arXiv:2609.17684 —
  spot-level refit, priors, selection, diagnosis of the other analyses.
- Data: McAlpine et al. 2025, arXiv:2505.10682 — Manticore-Local field.
- Independent NGC 4258 modelling: van der Boom & Kushnir 2026,
  arXiv:2601.14374 — single-orbit critique, refits, component tracking.
- Other flow and statistics treatments: Boruah et al. 2021,
  arXiv:2010.01119 (Sect. 6.3); Barua et al. 2025, arXiv:2502.11998.
- Anchor tests: Efstathiou 2020, arXiv:2007.10716 (Sects. 3–4); Yuan et
  al. 2022, arXiv:2203.06681; Jang et al. 2020, arXiv:2008.04181;
  Kudritzki et al. 2024, arXiv:2411.07974.

## Not verified
<!-- key: not-verified -->

- The MCP erratum (Pesce et al. 2026): described through
  arXiv:2609.17684, not read; no identifier recorded. Boruah et al. 2021
  (arXiv:2010.01119) read at abstract and Sect. 6.3 only; its Table 3
  values and its uniform-prior 70.1 are as quoted by arXiv:2609.17684.
- Van der Boom & Kushnir 2026: Sect. 4 results and the cadence study
  (Sect. 5) not read beyond the abstract; no reply by the NGC 4258 team
  found.
- SH0ES 2022 anchor-by-anchor H0 (arXiv:2112.04510): no HTML; not read
  here.
- The last steps of the reanalysis's reconciliation with arXiv:2608.06247
  (text cut off after the h-conversion step), and any reply by its
  authors.
- Individual MCP galaxy papers (Reid 2013, Kuo 2013, 2015, Gao 2016/2017,
  Pesce 2020a): cited through arXiv:2001.09213 and arXiv:2609.17684.
- The acceleration-fitting paper of NGC 4258 (Humphreys et al., Paper II):
  cited through arXiv:1307.6031.
