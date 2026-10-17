# Cosmic web — systematics

Scope: what biases a web classification, a filament catalogue, an
environmental trend, an alignment signal, a filament-gas detection or a
reconstruction; size where quantified, mitigation, validation test, and the
paper a referee expects.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Eq. n]`,
`[src: Table n]` body read; `[sec]` named secondary source; `[der]` derived
here.

## 1. Finder dependence
<!-- key: finder-dependence -->

**Mechanism.** Each finder defines a different web (`physics-and-methods.md`
§2). The same simulation gives filament mass fractions from ~10% to ~60% and
void volume fractions from ~40% to ~90% depending on the method (Libeskind et
al. 2018, arXiv:1705.03021) [src: Sect. 5.3].

**Size.** The number of methods agreeing on a halo's environment depends on
halo mass and web type; the maximum possible agreement is 6 methods for knots,
12 for filaments, 9 for sheets and 10 for voids, because not all methods
identify every type [src: Sect. 5.3 of arXiv:1705.03021]. Among NEXUS
variants, density-based ones put more mass in filaments than velocity-based
ones (arXiv:1401.7866) [src: Sect. 5.1]. NEXUS+ mislabels up to 20% of today's
sheet mass as filament at earlier times (arXiv:1401.7866) [src: Sect. 7].

**Mitigation.** Report results for at least two finders of different families,
or calibrate a finder against a reference (DisPerSE calibration guide in
arXiv:2309.08659 [src]; ASTRA thresholds tuned to GAMA volume fractions in
arXiv:2604.01456 [src: Table 2]).

**Validation.** Run the same finder on mocks with the survey's tracer density
and selection.

**Cite.** Libeskind et al. 2018 (arXiv:1705.03021).

## 2. Smoothing scale and threshold
<!-- key: smoothing-scale-and-threshold -->

**Mechanism.** Hessian classifications depend on the smoothing scale and on
the eigenvalue threshold λ_th, whose value has usually been chosen by visual
impression (Olex et al. 2025, arXiv:2412.09531) [src].

**Size.** The T-web reproduces the visual web at λ_th = 0.1, and percolating
voids coexist with connected filaments only for 0.2 < λ_th < 0.4
(arXiv:0809.4135) [src]. Values in use: λ_th = 0.2 on ~1 h⁻¹Mpc cells (T-web)
and 0.44 (V-web) in the finder comparison [src: Sect. 4.4–4.5 of
arXiv:1705.03021]; λ_th = 0 for Cosmicflows V-web catalogues [src: Sect. 2.1
of arXiv:2606.13538]. The halo spin-flip mass changes by more than an order of
magnitude with filament diameter (arXiv:1805.00033) [src]. The mean-colour
dependence on tidal environment can be an artefact of the smoothing scale, and
in redshift space smaller smoothing makes clusters look filamentary
(arXiv:1801.04878) [src: Sect. 4.2].

**Mitigation.** A normalised constant-volume threshold for the V-web, stable
for 0 < z < 2 and most precise at ~3 h⁻¹Mpc (arXiv:2412.09531) [src];
continuous variables (δ, α) instead of classes (arXiv:1801.04878) [src: Sect.
1]; robustness across a range of λ_th (appendix A of arXiv:2606.13538) [src:
Appendix A].

**Cite.** Forero-Romero et al. 2009 (arXiv:0809.4135); Olex et al. 2025
(arXiv:2412.09531).

## 3. Redshift-space distortions, photometric redshifts and sparse sampling
<!-- key: redshift-space-distortions-photometric -->

**Mechanism.** Fingers of God stretch groups along the line of sight into
false filaments; the Kaiser effect flattens structures; photometric redshift
errors scatter galaxies into voids; sparse tracers break filaments.

**Size and mitigation.** Using group centroids as MST nodes removes most
redshift-space distortion in GAMA filament finding [src: Sect. 4.1 of
arXiv:1705.03021]. An 8 h⁻¹Mpc top-hat makes fingers of God negligible for δ₈
but leaves the Kaiser anisotropy, which Alam et al. keep uncorrected [src:
Sect. 3.4 of arXiv:1801.04878]. With J-PAS-like photometric errors, voids
become slightly fewer, larger and less spherical, the main damage being
contamination of void interiors; a quasi-potential field mitigates it
(arXiv:2607.26932) [src]. A probabilistic DisPerSE recovers connectivity from
spectro-photometric data in agreement with 3D mock values (arXiv:2506.15345)
[src]. DisPerSE remains usable for very sparse samples and when half the
points are noise, at persistence ≥ 3σ (arXiv:1009.4014) [src].

**Validation.** Light-cone mocks with the survey's redshift errors run through
the identical finder (arXiv:2506.15345, arXiv:2607.26932) [src].

## 4. Confounding by density and halo mass
<!-- key: confounding-by-density-and-halo-mass -->

**Mechanism.** Halo mass function and local density both vary across the web.
A trend with web class or with distance to a filament at fixed stellar mass
can therefore come from halo mass or local density rather than from the
anisotropic tidal field.

**Size.** In SDSS, filament–field differences in star formation and morphology
at fixed stellar mass disappear once local galaxy density is also matched
(arXiv:2409.09028) [src]. An iHOD mock in which web dependence comes only from
the halo mass function reproduces the main δ₈–α₅ trends of SDSS clustering and
quenching (arXiv:1801.04878) [src]. In TNG, star formation shows the strongest
variation with distance to web features but also the strongest dependence on
local density (arXiv:2109.14623) [src].

**Mitigation.** Use continuous variables orthogonalised against density (α
with the exponent n chosen to null the δ–α correlation, n = 0.55 in SDSS;
arXiv:1801.04878 [src: Sect. 3.4]); match in stellar mass and local density
(arXiv:2409.09028) [src]; exclude galaxies near nodes, since node proximity
drives much of the environmental secondary bias in TNG300 (arXiv:2608.25060)
[src]; separate centrals and satellites (arXiv:2509.18077) [src].

**Validation.** Compare with a halo-mass-only mock (iHOD, SHAM) processed
identically (arXiv:1801.04878) [src].

**Cite.** Alam et al. 2019 (arXiv:1801.04878); O'Kane et al. 2024
(arXiv:2409.09028).

## 5. Alignment measurement systematics
<!-- key: alignment-measurement-systematics -->

**Mechanism.** Spin–filament signals are weak and depend on how spin and
filament are measured: stellar versus gas kinematics, projected versus 3D
spin, finder and its scale, sample selection by mass, morphology and distance
to the spine.

**Size.** The MaNGA hint of mass dependence, in 2–3σ tension with two
simulations when stellar velocities are used, vanishes with Hα velocities
(arXiv:1902.09797) [src]. In the Siena Galaxy Atlas the elliptical signal
reaches ≈ 13σ and the spiral one ≈ 2.8σ, but "these numbers depend on exactly
how the significance is measured" and peak at different distances from the
spine (arXiv:2509.02062) [src]. The flip mass in halo simulations varies by
more than an order of magnitude with filament diameter (arXiv:1805.00033)
[src].

**Mitigation.** Report the alignment as a function of stellar or bulge mass,
morphology and distance to the spine (arXiv:2208.10767, arXiv:2509.02062)
[src]; use 3D spins where possible (arXiv:2104.08275) [src]; compare with a
hydrodynamical simulation processed through the same finder (arXiv:1909.12371)
[src].

**Validation.** Randomised filament orientations; the same statistic on
simulated galaxies; consistency between gas and stellar spin.

**Cite.** Krolewski et al. 2019 (arXiv:1902.09797) for the selection
dependence; Ganeshaiah Veena et al. 2018 (arXiv:1805.00033) for the
filament-scale dependence.

## 6. Filament-gas stacking systematics
<!-- key: filament-gas-stacking-systematics -->

**Mechanism.** The stacked filament signal is small compared with that of the
haloes along and at the ends of the filament. Unmasked haloes, AGN and X-ray
binaries in filament galaxies, halo-model subtraction errors in pair stacks,
the CIB in tSZ maps, and the soft X-ray foreground all add to or mimic the
WHIM.

**Size.** About 40% of the eRASS:4 stacked filament emission is attributed to
unmasked haloes, AGN and X-ray binaries, reducing the WHIM significance from
9σ to 5.4σ (arXiv:2406.00105) [src]. Bound halo gas may contribute up to 20%
of the CMASS pair tSZ residual (arXiv:1709.10378) [src]. CIB contamination
uncertainty reduces the constraining power of the oriented ACT–DES tSZ stacks
(arXiv:2409.04535) [src]. Optical clusters with λ < 20 are deliberately left
unmasked in eRASS:4 because projection makes them unreliable, and are modelled
instead [src: Sect. 2.1 of arXiv:2406.00105].

**Mitigation.** Mask by several catalogues with radii tied to r_500c or the
background level, and mask skeleton critical points (arXiv:2406.00105) [src:
Sect. 2.1, Table 1]; subtract a local background 10–20 Mpc from the spine
(arXiv:2206.00084) [src]; model the halo contribution explicitly
(arXiv:1709.10378, arXiv:1709.05024) [src]; Monte Carlo null tests with random
pair or filament positions (arXiv:1709.05024) [src]; mock maps for profile
stacking (arXiv:2406.00105, appendix "Mock maps for profile stacking
validation") [src: section titles].

**Geometry.** A projected separation underestimates the bridge length when the
axis has a line-of-sight component; for A399–A401 the low inferred density is
"fully explained" this way (arXiv:2107.04611) [src].

**Cite.** Zhang et al. 2024 (arXiv:2406.00105) for contamination modelling; de
Graaff et al. 2019 (arXiv:1709.10378) for halo subtraction.

## 7. Reconstruction systematics
<!-- key: reconstruction-systematics -->

**Mechanism.** A reconstructed field is smoothed, biased and noisy; the web
extracted from it inherits the reconstruction's resolution, galaxy-bias model
and survey boundaries.

**Size.** In CF4++ZOA, only structures recovered in at least 68% of HMC
realisations and away from survey edges are kept: 37 voids and 42 knots; a
density-only classification of the same galaxies puts 23,020 in underdense and
42,313 in overdense regions, against 3041 and 7346 in the dynamically
identified voids and knots [src: Sect. 4 of arXiv:2606.13538]. Galaxy
redshift-space voids need not be matter voids: only three of seven nearby
voids show a clear central matter underdensity from Cosmicflows-3 velocities
(arXiv:2211.16388) [src]. In Lyα tomography, eigenvector recovery requires ≲ 5
h⁻¹Mpc sightline spacing (arXiv:1612.00067, **forecast**) [src].

**Mitigation.** Posterior ensembles rather than single maps (arXiv:1512.02242,
arXiv:2606.13538) [src]; per-object membership probabilities and
classification entropies (arXiv:2604.01456) [src]. Limits of constrained
simulations (constraint scale, bias model) are in `cosmo-simulations-mocks`
systematics §7.

**Cite.** Leclercq et al. 2015 (arXiv:1512.02242); Hollinger & Courtois 2026
(arXiv:2606.13538).

## 8. Referee checklist
<!-- key: referee-checklist -->

1. Finder, tracer, smoothing scale and threshold stated; result shown for a
   second finder or a threshold range.
2. Eigenvalue ordering and tensor normalisation stated for Hessian methods.
3. For environmental trends: matched in stellar mass and in local density or
   halo mass; centrals and satellites separated; node proximity controlled.
4. Redshift-space or photometric-redshift effects tested on mocks run through
   the same pipeline.
5. For alignments: spin tracer (stellar, gas, shape), 2D or 3D, sample
   selection and the significance estimator stated.
6. For filament gas: masking catalogues and radii, background subtraction,
   halo and AGN contamination modelled, null tests with random positions.
7. Gas temperature and density quoted with the profile model (β-model, r_c/r,
   cylinder) and metallicity assumed.
8. Baryon fractions referenced to a stated Ω_b and epoch; "missing" fraction
   defined.
9. Protocluster masses: aperture, descendant-mass definition, forward or
   backward tracking.
10. Reconstructions: posterior ensemble or single map; survey-edge treatment.

## Not verified
<!-- key: not-verified -->

- Systematics budgets in the tSZ filament stacks (CIB, halo-model uncertainty)
  were read only at abstract level, except for eRASS:4 masking.
- No quantitative comparison of filament catalogues from different finders on
  the same galaxy survey was read.
