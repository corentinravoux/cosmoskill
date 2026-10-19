# Halo finding — cosmo-simulations-mocks dossier

Scope: how a halo and subhalo catalogue is made from particles and linked
in time (the FoF seed, the configuration-, phase- and history-space
finders and their parameters, unbinding, merger trees, catalogue cleaning)
and what each choice changes in the mass function, the satellite
population, the clustering and an occupation fit made on the catalogue.
Snapshot: 2026-10-19.
From: Angulo & Hahn 2021 review (arXiv:2112.05165), Sect. 9.4; halo mass
definitions and mass function shared with cosmo-galaxy-halo-connection.

Already in L2, not repeated here: the three families of finders with their
founding papers, the FoF boundary density of 81.62 times the mean for
b = 0.2, the Knebe et al. 2011 summary, the halo mass-function papers and
the requirement of 500 particles per halo for 1% statistics
(`physics-and-methods.md#halo-finding-and-halo-definitions`,
`systematics.md#resolution-and-box-size-effects`). How a concentration is
measured on a catalogue, the choice of centre for a profile and the
conversion between mass definitions are in
`cosmo-galaxy-halo-connection/deep/profiles-concentration.md`; how a
merger-tree catalogue feeds an empirical galaxy model in
`cosmo-galaxy-halo-connection/deep/empirical-sam-hydro.md`.

Symbols used throughout. b: FoF linking length in units of the mean
inter-particle separation ⟨l⟩; Δ: overdensity threshold; M_200c, M_200m,
M_vir: masses inside spheres of 200 times the critical density, 200 times
the mean density, and the Bryan & Norman virial overdensity; V_max: peak of
the circular-velocity curve; M_peak: largest mass along the main-progenitor
branch; N_p: particle number of a halo.

## How it is done

### Step 1. Seed the search with friends-of-friends

Every production finder read here starts from a 3D FoF grouping and
refines it. In the FLAMINGO comparison, HBT-HERONS, SUBFIND and VELOCIraptor
use b = 0.2 and ROCKSTAR its recommended b = 0.28 [src: arXiv:2502.06932,
Sect. 3.1]. The mean separation is computed from the cold-matter density:
⟨l⟩ = [m_dm / ((Ω_cdm + Ω_b) ρ_crit)]^{1/3} in a gravity-only run and
[m_dm / (Ω_cdm ρ_crit)]^{1/3} in a hydrodynamical one, with Ω_cdm excluding
neutrinos [src: Eqs. 1–3]. In hydrodynamical runs HBT-HERONS and SUBFIND
link dark-matter particles only and attach the other species to the nearest
group afterwards, discarding groups below 32 particles; ROCKSTAR links all
species and keeps groups above 10 particles [src: Sect. 3.1].

Why the linking length differs. The ROCKSTAR paper states that b = 0.2 "is
too small, as it does not include all particles out to the virial radius",
and chose b = 0.28 so that virial spheres can be measured "for even the
most ellipsoidal halos"; its modified FoF becomes faster, not slower, as b
grows, because neighbour searches are skipped for particles with more than
16 neighbours [src: arXiv:1110.4372, Sect. III.1]. Values of 0.25–0.35 give
very similar mass functions; smaller values fragment groups, so that at low
particle number one halo can be split in two [src: Sect. IV.5].

CompaSO, run on the fly in AbacusSummit, uses b = 0.25 but only for
particles whose kernel density exceeds Δ_L0,min = 60, with the kernel
W(r) = 1 − r²/b_kernel², b_kernel = 0.4 ⟨l⟩ [src: arXiv:2110.11408,
Sect. 2.2.1, Eq. 1]. The reason given: b = 0.25 alone would percolate near
Δ ≈ 41, and the kernel density has lower variance than the nearest-neighbour
criterion of FoF and imposes a physical smoothing scale [src: Sect. 2.2.1].

### Step 2. Split the group into haloes and subhaloes

The three families differ in the space in which they separate structures.

- **Configuration space (SUBFIND).** The total density is estimated by
  adaptive kernels; density peaks seed candidates that grow by an
  excursion-set algorithm until they reach saddle points; candidates are
  then unbound iteratively, a fraction of particles at a time, until the
  bound number converges or falls below 20 particles [src:
  arXiv:2502.06932, Sect. 3.3].
- **Competitive spherical overdensity (CompaSO).** The densest particle of
  an L0 group is a nucleus; the L1 radius is where the enclosed density
  falls below Δ_L1; particles inside 0.8 R_L1 cannot seed new nuclei, the
  value of 80% chosen between 70% and 100% because smaller values gouge
  wedges out of large haloes and larger ones deblend close pairs less well;
  a later nucleus takes a particle if its enclosed density with respect to
  the new centre is at least c_Roche = 2 times that of the current
  assignment, a tidal-radius argument for two isothermal spheres; seeding
  stops at the central density of a 35-particle isothermal sphere at
  M_200m; the same procedure inside each L1 halo gives the L2 subhaloes
  [src: arXiv:2110.11408, Sect. 2.2.2]. No unbinding is done (step 3).
- **Phase space (ROCKSTAR).** Inside each FoF group a hierarchy of 6D FoF
  subgroups is built with the metric
  d(p₁, p₂) = (|x₁ − x₂|²/σ_x² + |v₁ − v₂|²/σ_v²)^{1/2}, with σ_x and σ_v the
  position and velocity dispersions of the group, and the linking length
  set so that a fraction f of particles have a neighbour [src:
  arXiv:1110.4372, Sect. III.2, Eq. 1]. f = 0.7: above 0.9 the code is slow
  and finds spurious groups, below 0.5 it misses small substructure; with
  a 20-particle minimum this gives a 10% false-positive rate for
  20-particle groups, falling exponentially with size [src: Sect. III.2].
  Seeds whose positions and velocities agree within 10√2 of their Poisson
  uncertainties are merged; lower thresholds produce a spurious upturn of
  the halo autocorrelation near the force resolution [src: Sect. III.3,
  Eq. 2]. Particles are then given to the nearest seed with the position
  normalised by r_dyn,vir = V_max t_dyn,vir instead of σ_x, which prevents
  host particles in the outskirts from being assigned to a subhalo [src:
  Sect. III.3, Eqs. 3–4].
- **Phase-space peaks (VELOCIraptor).** Particles whose local velocity
  density exceeds a Gaussian background model by a likelihood of 2.5 are
  linked with half the 3D linking length and a velocity criterion, then
  unbound, recursively for groups above 800 particles [src:
  arXiv:2502.06932, Sect. 3.5, Eqs. 8–9].
- **History space (HBT+, HBT-HERONS).** Haloes are tracked as they form.
  The host of a subhalo at the next output is the host of its most-bound
  particle; among progenitors above 2/3 of the most massive, the one with
  the smallest specific kinetic energy relative to the host is the main
  progenitor; after each unbinding the source subhalo passed forward is
  trimmed to at most 3 N_bound particles, to allow re-accretion of stripped
  material [src: arXiv:1708.03646, Sect. 2.2]. Two subhaloes are merged
  when δ_s = Δ_x/σ_x + Δ_v/σ_v < 2, with σ_x, σ_v the dispersions of the 20
  most-bound particles of the host, after which only the most-bound
  particle of the satellite is tracked [src: Sect. 2.4, Eq. 3].

### Step 3. Decide whether to unbind, and how

- HBT+ unbinds iteratively in the frame that minimises the kinetic energy
  (the centre-of-mass frame, with the Hubble flow included), estimating the
  potential from a random 1000-particle subsample, which recovers the bound
  profile to the percent level, and recomputing the most-bound particle
  from the 1000 most bound [src: arXiv:1708.03646, Sect. 2.3, Eqs. 1–2].
- ROCKSTAR does a single pass by default; about 98% of particles assigned
  to centrals are bound at z = 0; haloes with fewer than 50% bound
  particles are not output, and changing that threshold has no
  statistically significant effect until bound fractions below 15% are
  admitted; in mergers of mass ratio 1:3 or closer the potential of the
  combined system is used, because naive unbinding makes merging haloes
  lose mass for several outputs (by a factor of three in another finder)
  [src: arXiv:1110.4372, Sect. III.5.3]. Computing properties with all
  particles raises masses by 1–2% and the one-halo correlation of
  satellites [src: Sect. IV.5]. ROCKSTAR also lets a particle belong to
  several subhaloes (inclusive assignment), unlike the other three finders
  of the FLAMINGO test [src: arXiv:2502.06932, Sect. 3.4].
- CompaSO does not unbind, for speed and because a single particle's
  energy is not conserved in an evolving system, so binding "is not a
  guarantee of long-term membership"; unbinding treats each halo as
  isolated, discards host particles from any halo, and ignores the
  potential of mass outside the boundary [src: arXiv:2110.11408,
  Sect. 3.3]. On a 296 Mpc/h test box, standard unbinding removes 6.5% of
  particles in small haloes and 4% in massive ones; adding the potential of
  the NFW mass beyond r_vir, φ_extra = −(G M_vir / r_vir) f(c) with
  f(c) = [ln(1 + c)(c⁻¹ + 1) − 1]⁻¹, brings this to 3.5% and 0% [src:
  Sect. 3.3, Eqs. 4–5].

### Step 4. Measure halo properties consistently

Masses, centres and V_max depend on the finder's choices even when the
member particles agree. The FLAMINGO comparison therefore computes every
property with one external tool, SOAP, from each finder's membership and
centres, imposes exclusive assignment on ROCKSTAR, and keeps only subhaloes
above 100 dark-matter particles [src: arXiv:2502.06932, Sect. 5]. CompaSO
stores four centres (L1 nucleus, L1 centre of mass, largest-L2 nucleus,
largest-L2 centre of mass) and recommends the largest-L2 centre of mass,
which peaks within about 10⁻² Mpc/h, the softening scale, of a shrinking-
sphere centre r_i = (1 − 0.05)^i r₀ [src: arXiv:2110.11408, Sect. 4.4,
Eq. 12].

### Step 5. Build merger trees

The merger-tree comparison of ten codes on common catalogues found that
"all algorithms produced distinct results" and asks of a useful code that
it match haloes by particle IDs, skip at least one output to recover
subhaloes temporarily lost in mergers, and cope with large temporary mass
fluctuations [src: arXiv:1307.3577, abstract]. Two production schemes:

- **AbacusSummit.** Using a 10% particle subsample, each L1 halo at output
  i is compared with haloes within r_max = 4 Mpc/h at outputs i − 1 and
  i − 2; a candidate donating at least f_thresh = 0.5 of its particles is a
  progenitor; the main progenitor is the one contributing the largest
  kernel-density-weighted fraction; tracking i − 2 as well lets the tree
  switch back to the correct branch after a fly-by; a halo that is the main
  progenitor without being a progenitor is flagged IsPotentialSplit, which
  happens in about 2% of 150-particle haloes and 0.001% of
  15,000-particle ones [src: arXiv:2110.11409, Sect. 2.4]. A 296 Mpc/h box
  with 186 outputs (Δ ln a ≈ 0.007) showed that 33 outputs, the AbacusSummit
  cadence, give the same formation redshifts down to 50 particles [src:
  Sect. 3].
- **Consistent-trees.** Halo positions and velocities at one output are
  evolved gravitationally to the adjacent output and compared with the
  catalogue; links with a deviation metric above d_break = 3.2 (1–2% of
  particle-based links in Bolshoi), links to a progenitor that is not the
  most massive (2–3%), and links with mass ratios beyond 0.5 dex in M_vir or
  0.15 dex in V_max (2% at z = 0 for ROCKSTAR) are broken and re-matched
  within d_match = 15; missing haloes are inserted as "phantoms" [src:
  arXiv:1110.4370, Sect. V.3]. Tracks with more than 25% phantoms, tracked
  for fewer than 5 outputs, or subhaloes never outside their host and
  tracked for fewer than 10 outputs, are removed; the authors call these
  defaults "fairly lax" for the 180 outputs of Bolshoi [src: Sect. V.4].

### Step 6. Clean the catalogue before populating it

A finder decides at each output whether a satellite that has passed
through a host is a separate halo. An HOD then assigns galaxies by the
present mass of the stripped remnant: two galaxies before the encounter can
become one after it [src: arXiv:2110.11408, Sect. 3.1]. The AbacusSummit
cleaning traverses the main-progenitor branch, flags a halo whose peak mass
exceeds its present mass by more than κ = 2, adds its mass to the halo it
was part of at the epoch of the peak, and keeps the two merged at all later
outputs [src: arXiv:2110.11409, Sect. 4.2]. It removes about 1–5% of
objects, mostly low-mass haloes on the edges of massive ones [src: Sect.
4.2], and those removed have preferentially positive radial velocities
1–3 Mpc/h from cluster centres, the signature of objects that have passed
through the host [src: Fig. 11 caption].

## Choices and what they cost

### Which family of finder

| Finder | Separates by | Unbinding | Cost on one FLAMINGO output | Main stated weakness |
|---|---|---|---|---|
| SUBFIND | density peaks and saddle points | iterative | O(10³) CPU-h | blending of massive subhaloes near the host centre |
| VELOCIraptor | phase-space density peaks | iterative | O(10³) CPU-h | miscentring of some massive centrals |
| ROCKSTAR | 6D FoF hierarchy | single pass, inclusive membership | O(10) CPU-h | low central bound masses, mass function 10% off |
| HBT-HERONS / HBT+ | history (tracking bound particles) | iterative, subsampled | O(10) CPU-h | needs outputs in time; cadence not tuned in FLAMINGO |
| CompaSO | competitive SO on a kernel-density FoF | none, cleaning by trees | on the fly | over-splitting at large mass |

Costs and weaknesses [src: arXiv:2502.06932, Sects. 3.3–3.5, 4.2.1 and 5;
arXiv:1708.03646, Sect. 3.4.1; arXiv:2110.11408, Sect. 4.1]. The FLAMINGO
authors note that SUBFIND and VELOCIraptor "require a comparable investment
to running the simulation itself", while HBT-HERONS and ROCKSTAR cost a
negligible fraction of the O(10⁶) CPU-h L1_m9 run [src: arXiv:2502.06932,
Sect. 5], and conclude that HBT-HERONS is their preferred finder for its
low cost, self-consistent merger trees and robust identification [src:
abstract]. The comparison is made by the HBT-HERONS developers on their own
simulations; no independent test of that ranking was read.

What was found when the families were run on the same particles:

- **Field haloes.** In FLAMINGO gravity-only runs the M_200c mass functions
  of HBT-HERONS and SUBFIND agree to much better than 1%, since both use
  the same FoF groups; VELOCIraptor is up to 3% low at high mass because
  some massive centrals are centred on a satellite, with M_200c sometimes
  lower by an order of magnitude; ROCKSTAR agrees within 1% above
  4 × 10¹⁴ M_⊙ and departs by about 10% at lower masses [src:
  arXiv:2502.06932, Sect. 4.2.1].
- **Bound masses.** Bound-mass functions differ by up to 75% at the high
  mass end, "even when using the maximum circular velocity as a mass
  proxy"; the number of well-resolved subhaloes differs by up to 20% near
  R_200c and increasingly towards host centres; most finders do not improve
  with resolution and do worse in hydrodynamical than gravity-only runs
  [src: abstract].
- **Clustering.** In bins of V_max, finders agree beyond 1–10 Mpc apart
  from a small ROCKSTAR offset, explained by its lower central bound masses:
  a V_max cut then selects more massive haloes; below about 2 Mpc, where the
  one-halo term dominates, the correlation functions differ significantly,
  SUBFIND being increasingly suppressed at small separations [src: Sect.
  4.4].
- **SUBFIND against HBT+.** On the same runs the final subhalo mass function
  of HBT+ is about 10% above SUBFIND at low mass, and at high mass the
  difference corresponds to a factor 2–3 in subhalo mass or an order of
  magnitude in abundance, attributed to configuration-space "blending" when
  a subhalo overlaps the host centre [src: arXiv:1708.03646, Sect. 3.4.1].
  The SUBFIND peak-mass function, built with the dtree code, is instead
  higher, because switches of the main branch overestimate M_peak and
  broken links create extra branches; disrupted peak-mass functions differ
  by up to a factor 2 [src: Sects. 3.4.1 and 3.5].
- **CompaSO against ROCKSTAR** on AbacusSummit at z = 0.5: CompaSO has up
  to about 10% more haloes near 10¹¹ M_⊙/h and about 50% fewer near
  10¹⁵ M_⊙/h; the differences are halved by cleaning; agreement is within
  25% over 10¹¹–10¹⁴ M_⊙/h; in V_max the two functions agree within about 5%
  everywhere, so "the two halo algorithms find the same objects for the
  most part" and the mass difference is a matter of boundaries and
  definitions [src: arXiv:2110.11408, Sect. 4.1].
- **Subhalo comparison on one Milky-Way halo** (Aquarius, five
  resolutions): all finders agree on the presence and position of
  substructure and on V_max; properties set by particles near the subhalo
  edge agree at the 20% level; mass and V_max are recovered reliably above
  100 particles [src: arXiv:1203.3695, abstract].

### Mass or V_max as the halo variable

The CompaSO comparison finds V_max more robust than mass across finders
(within about 5% of ROCKSTAR, arXiv:2110.11408, Sect. 4.1); the FLAMINGO comparison finds bound-mass functions 75% apart
even in V_max at high mass and uses V_max for clustering as "less
sensitive" than bound mass [src: arXiv:2502.06932, abstract and Sect.
4.4]. Abundance matching on V_peak and an HOD on M_200m therefore inherit
different finder systematics. One check in the other direction: the
15% assembly-bias deficit of TNG300 survives a change of finder to
ROCKSTAR (`cosmo-galaxy-halo-connection/deep/assembly-bias.md`).

### Cleaning or not, and how hard

The AbacusSummit cleaning parameter κ was tested at 1.2, 2.0 and 20: κ = 2
reduces the high-mass difference with ROCKSTAR from 50% to 25%, κ = 1.2 is
indistinguishable from it, and κ = 20 barely changes the default catalogue
[src: arXiv:2110.11409, Sect. 4.3]. The unprocessed catalogue shows "a
strong excess of low-mass haloes in the outskirts of galaxy clusters", a
peak in the cross-correlation near 1 Mpc/h that cleaning removes [src:
Sect. 4.3, Fig. 10 caption]. Consistent-trees changes the ROCKSTAR mass
function on Bolshoi by about 0.5% at z < 1, added phantoms and deleted
haloes nearly cancelling; the authors read this as the raw catalogue being
self-consistent at better than 1% at z = 0, a statement of precision, not
accuracy [src: arXiv:1110.4370, Sect. VI.4].

### What the cleaning does to an occupation fit

The one measured case read: a seven-parameter HOD (five mass-only
parameters and two velocity-bias parameters) fitted with AbacusHOD to the
BOSS CMASS DR12 ξ(r_p, π) at 0.46 < z < 0.6, on the AbacusSummit
Base_c000_ph000 box with and without cleaning [src: arXiv:2110.11409,
Sect. 4.7, Eqs. 1–4]. The cleaned catalogue is preferred by about 14
e-folds in both Bayesian evidence (log Z = −62 against −76) and best-fit
likelihood; M₁ falls and α rises, i.e. more satellites, because re-merged
fringe haloes turn their centrals into satellites; the satellite velocity
bias α_s moves back towards 1; residuals shrink at r_p ≈ 3–10 Mpc/h, where
the uncleaned mocks over-cluster [src: Sect. 4.7, Table 2 discussion]. The
occupation parameters of a fit are therefore tied to the catalogue
processing, not only to the finder.

### Tracking finders and orphans

Phase-space finders lose subhaloes inside hosts: in Bolshoi, ROCKSTAR shows
a radial incompleteness scale for merger ratios below 1:30 in
10¹³·⁵–10¹⁴ M_⊙ hosts, defined where the satellite density slope becomes
shallower than −1.5, the observed slope being −1.7 to −1.5 [src:
arXiv:1110.4372, Sect. V]. The same section notes that matching
small-scale clustering often needs "orphan" galaxies without a subhalo.
The particle-tracking finder Symfind follows subhaloes to much lower
masses than ROCKSTAR with consistent-trees, finding 15–40% more subhaloes
within R_vir and 35–120% more within R_vir/4 at fixed peak mass, with more
found at higher resolution; it resolves mass loss for n_peak ≳ 4 × 10³
particles but V_max only for n_peak ≳ 3 × 10⁴, and states that ROCKSTAR
"converges to false solutions" for the subhalo mass function, radial
distribution and disruption masses [src: arXiv:2308.10926, abstract]. The
trade is between modelling orphans analytically on a phase-space catalogue
and tracking particles, which needs the particle data at every output.

## Numbers

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| FoF linking length | 0.2 (HBT-HERONS, SUBFIND, VELOCIraptor); 0.28 (ROCKSTAR) | FLAMINGO comparison | arXiv:2502.06932 | Sect. 3.1 |
| ROCKSTAR b tested | 0.25–0.35 give similar mass functions; 0.2 misses virial outskirts | Consuelo | arXiv:1110.4372 | Sects. III.1, IV.5 |
| ROCKSTAR refinement fraction f | 0.7; f = 0.9 gives 4% false 30-particle haloes | Consuelo | arXiv:1110.4372 | Sects. III.2, IV.5 |
| ROCKSTAR bound threshold | 0.5; no significant effect until < 0.15 | — | arXiv:1110.4372 | Sect. III.5.3 |
| ROCKSTAR major-merger potential ratio | 0.3 (1:3); < 1% on mass function | — | arXiv:1110.4372 | Sect. III.5.3, Table 2 |
| CompaSO parameters | b = 0.25, Δ_L0,min = 60, b_kernel = 0.4 ⟨l⟩, R_elig = 0.8 R_L1, c_Roche = 2, N_min = 35 | AbacusSummit | arXiv:2110.11408 | Sects. 2.2.1–2.2.2 |
| CompaSO potential splits at z = 0.5 | 12.8% overall; 10.5% at 10¹¹·⁵, 0.42% at 10¹⁴·⁵ M_⊙/h | AbacusSummit | arXiv:2110.11408 | Table 2 |
| AbacusSummit tree matching | r_max = 4 Mpc/h, f_thresh = 0.5, 10% subsample, 33 outputs | AbacusSummit | arXiv:2110.11409 | Sects. 2.4, 3 |
| Cleaning parameter | κ = 2 (1.2 equivalent; 20 ineffective); 1–5% of objects merged | AbacusSummit | arXiv:2110.11409 | Sects. 4.2–4.3 |
| HOD fit, cleaned against raw | Δ log Z ≈ 14 (−62 against −76) | CMASS ξ(r_p, π) | arXiv:2110.11409 | Sect. 4.7 |
| Consistent-trees thresholds | d_break = 3.2, d_match = 15, 0.5 dex M_vir, 0.15 dex V_max, f_phant = 25%, t_tracked = 5, t_tracked,subs = 10 | Bolshoi | arXiv:1110.4370 | Sects. V.3–V.4 |
| HBT+ merging criterion | δ_s < 2 (20 most-bound particles) | — | arXiv:1708.03646 | Sect. 2.4, Eq. 3 |
| HBT+ source size; potential subsample | 3 N_bound; 1000 particles | — | arXiv:1708.03646 | Sects. 2.2–2.3 |
| Finder spread, M_200c mass function | ≪ 1% (HBT-HERONS/SUBFIND), 3% (VELOCIraptor), 10% (ROCKSTAR) | FLAMINGO DMO, z = 0 | arXiv:2502.06932 | Sect. 4.2.1 |
| Finder spread, bound mass; satellites near R_200c | up to 75%; up to 20% | FLAMINGO | arXiv:2502.06932 | abstract |
| Minimum for reliable subhalo mass and V_max | 100 particles | Aquarius | arXiv:1203.3695 | abstract |
| Symfind resolution limits | mass loss n_peak ≳ 4 × 10³; V_max n_peak ≳ 3 × 10⁴ | Symphony | arXiv:2308.10926 | abstract |
| FLAMINGO output cadence | 79 outputs, ⟨Δ ln a⟩ = 0.015 | FLAMINGO | arXiv:2502.06932 | Sect. 2 |

## What goes wrong

- **Fringe haloes in SO and FoF catalogues.** Low-mass haloes carved out of
  the edges of massive ones, or remnants of fly-throughs, show up as a peak
  near 1 Mpc/h in the cross-correlation of low- and high-mass haloes and as
  excess clustering at r_p ≈ 3–10 Mpc/h of HOD mocks; the test is the
  halo–halo cross-correlation by mass bin and the peak-to-present mass
  ratio along the tree (arXiv:2110.11409, Sects. 4.3 and 4.7). A ratio of
  r_halo/r_vmax atypical for the mass also flags them (arXiv:2110.11408,
  Sect. 3.2, Fig. 3).
- **Miscentring.** A massive central centred on a satellite returns an
  M_200c too low, sometimes by an order of magnitude; bijective matching of
  centrals between two finders and the offset distribution catch it
  (arXiv:2502.06932, Sect. 4.2.1 and App. C). Comparing the stored centre
  with a shrinking-sphere centre is the CompaSO test (arXiv:2110.11408,
  Sect. 4.4).
- **Blending of massive subhaloes.** Configuration-space finders underweight
  massive subhaloes near the host centre; the symptom is a deficit of
  massive subhaloes in the inner radial distribution relative to a
  phase-space or tracking finder (arXiv:1708.03646, Sect. 3.4.1).
- **Premature subhalo loss.** Phase-space finders lose satellites inside
  hosts at a radius that depends on mass ratio; the test is the logarithmic
  slope of the satellite number density against the observed −1.5 to −1.7
  (arXiv:1110.4372, Sect. V), or a particle-tracking comparison
  (arXiv:2308.10926).
- **Merger-tree switching.** Main-branch switches during major mergers
  inflate M_peak, and broken links add branches; the peak-mass function
  split into surviving and disrupted parts, and the length of the main
  progenitor branch, are the diagnostics (arXiv:1708.03646, Sect. 3.5;
  arXiv:2110.11409, Sect. 4.4).
- **Finder settings changed between runs.** Mass functions at low particle
  number move with b and f; a mock and its convergence run must use the
  same finder and settings (arXiv:1110.4372, Sect. IV.5).
- **Baryons.** Finders developed on gravity-only runs fail more often in
  hydrodynamical ones; linking only dark matter or all species changes the
  result, and including black holes in ROCKSTAR linking produced
  structures over 10 Mpc long (arXiv:2502.06932, Sects. 3.4 and 5).

## Reading list

- Review: Angulo & Hahn 2021, arXiv:2112.05165, Sect. 9.4 — the families
  of finders and the mass-definition problem.
- Method: Behroozi et al. 2011, arXiv:1110.4372 — ROCKSTAR, with a
  parameter-by-parameter test of its defaults (Sect. IV.5).
- Method: Hadzhiyska et al. 2021, arXiv:2110.11408 — CompaSO, the case
  against unbinding, centre choices.
- Method: Bose et al. 2021, arXiv:2110.11409 — AbacusSummit trees, the
  cleaning step and its effect on a CMASS HOD fit.
- Method: Behroozi et al. 2011, arXiv:1110.4370 — consistent-trees,
  gravitational checks between outputs.
- Method: Han et al. 2017, arXiv:1708.03646 — HBT+ tracking, unbinding,
  merging; comparison with SUBFIND.
- Critique: Forouhar Moreno et al. 2025, arXiv:2502.06932 — four finders on
  FLAMINGO with a common property calculator.
- Critique: Mansfield et al. 2023, arXiv:2308.10926 — subhalo durability
  and false convergence of a phase-space finder.
- Comparison: Knebe et al. 2011, arXiv:1104.0949 (in L2); Onions et al.
  2012, arXiv:1203.3695 — field-halo and subhalo comparison projects.
- Comparison: Srisawat et al. 2013, arXiv:1307.3577 — ten merger-tree codes
  and the three properties a tree code needs.

## Not verified

- The bodies of the Srisawat et al. 2013, Onions et al. 2012 and Symfind
  papers: abstracts only.
- The Euclid Flagship 2 ROCKSTAR settings: the FLAMINGO comparison states
  that a single unbinding pass reflects the choice made in the Flagship
  simulations; the Flagship paper's own settings were not read here.
- The DESI DR2 Uchuu abundance-matching mocks and their finder and
  orphan treatment: not read.
- Effect of the finder on a cosmological parameter, as opposed to an HOD
  fit or a clustering statistic: no paper read here measures it. The
  SBI test of training on one finder and testing on another is in
  `cosmo-beyond-two-point/deep/simulation-based-inference.md`.
- AHF, Ntropy, VOBOZ, ORIGAMI and the other finders of the 2011 comparison:
  named in its code list only.
- A 2025 continuous-wavelet subhalo finder and the SOAP property
  calculator used by the FLAMINGO comparison: titles and abstract snippets
  seen in the date-sorted search, not read; search by these descriptions
  before citing.
