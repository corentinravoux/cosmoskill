# Cosmic web — open questions

Scope: live controversies, method debates, what the next data will decide,
forecasts (labelled), and stale claims about the cosmic web with the paper
that corrects each.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Eq. n]`,
`[src: Table n]` body read; `[sec]` named secondary source; `[der]` derived
here.

## 1. Are the missing baryons found?
<!-- key: are-the-missing-baryons-found -->

**Side A: yes, in total.** Localized FRBs measure Ω_b h₇₀ = 0.051 ± 0.006 at
low redshift, with f_IGM = 0.76 (+0.10/−0.11), "agreeing with the baryon-rich
cosmic web scenario" (Connor et al. 2024, arXiv:2409.16952) [src: abstract]. Two O VII
absorbers in overdense regions led Nicastro et al. (2018, arXiv:1806.08395) to
conclude that the missing baryons "have been found" [src: abstract].

**Side B: not where, and not in which phase.** A re-analysis of the same
quasar finds one possible O VII line at 2.6σ, no stacked signal and large
systematic uncertainties on temperature and abundances; it calls for a larger
sample of X-ray sources (Spence et al. 2023, arXiv:2305.01587) [src:
abstract]. The X-ray stacks see only the hot, dense end of the WHIM
(arXiv:2406.00105) [src], and the tSZ stacks give filament gas fractions with
errors of order the value: (0.080 +0.116/−0.051) Ω_b along SDSS filaments
(arXiv:1911.09706) [src: abstract], and 11 ± 7% of all baryons (28 ± 12% on
the longer baseline) between CMASS pairs (arXiv:1709.10378) [src: abstract].
The FRB
census itself partitions IGM and haloes only statistically, through their
different redshift dependence (arXiv:2409.16952) [src: Results].

**What decides it.** A spatially resolved partition: FRB sightlines stacked on
web structures (voids already at 3.2σ, arXiv:2605.01994) [src: abstract], X-ray
absorption spectroscopy of many sightlines, and kSZ, which as a linear probe
of density is the most sensitive SZ route to the WHIM (arXiv:2412.03631)
[src].

## 2. Does the web affect galaxies beyond halo mass?
<!-- key: does-the-web-affect-galaxies-beyond-halo-mass -->

**Side A: yes, through anisotropic tides and accretion geometry.** In GAMA,
star-forming galaxies redden at fixed mass toward filaments, regardless of
node distance, interpreted as anisotropic assembly bias (arXiv:1710.02676)
[src]. In GAMA groups, halo age depends on web class at fixed mass
(arXiv:1612.08595) [src]. In TNG50, low-mass filament galaxies have smaller,
asymmetric gas discs at fixed stellar and halo mass, and late infallers
undergo "cosmic web stripping" (arXiv:2605.23457) [src]. Splicing experiments
show that filament proximity leaves halo mass unchanged but changes spin
orientation by up to 80% (arXiv:2409.13010) [src: abstract].

**Side B: mostly not, once density and halo mass are controlled.** In SDSS, a
halo-mass-only mock reproduces clustering and quenching trends in δ₈ and α₅,
so any direct effect of tides on > 5 h⁻¹Mpc scales "must be extremely weak"
(arXiv:1801.04878) [src]; filament–field differences vanish at fixed local
density (arXiv:2409.09028) [src]; in TNG, integrated properties of low-mass
filament galaxies match the field (arXiv:2605.23457) [src].

**Reconciliation in progress.** The effect may live in resolved gas and
kinematics rather than in integrated star formation (arXiv:2605.23457) [src],
and in halo properties that track α rather than b₁ (arXiv:1903.02007) [src].
The decisive test is a resolved-gas or spin measurement at fixed halo mass and
local density. Assembly-bias detections in clustering are in
`cosmo-galaxy-halo-connection`.

## 3. The spin-alignment transition
<!-- key: the-spin-alignment-transition -->

- The transition mass differs by an order of magnitude between halo-finder
  set-ups: ~5 × 10¹² (arXiv:1201.5794) versus 5 × 10¹¹ h⁻¹M☉
  (arXiv:1805.00033), the latter depending on filament diameter [src:
  abstract of each].
- In stars, the transition is detected with SAMI at log M* = 10.4–10.9
  (arXiv:1909.12371) [src: abstract] and tied to bulge mass
  (arXiv:2208.10767) [src], while
  the first MaNGA study found no alignment with stellar spins and a dependence
  on whether stellar or Hα kinematics are used (arXiv:1902.09797) [src]. The
  stellar transition is present in Illustris but not in MassiveBlack-II, so it
  depends on feedback and subgrid physics (arXiv:1902.09797) [src].
- New observable: galaxy spin anti-parallel to filament spin for low-mass
  spirals (arXiv:2506.22794) [src]; independent confirmation of filament
  rotation was not looked for.
- Forecast: at z ~ 2.5, IGM tomography with > 10,000 galaxies (PFS) reaches
  Δ⟨cos θ⟩ ~ 0.03 (arXiv:1612.00067, **forecast**) [src: abstract].

## 4. Which finder, which web?
<!-- key: which-finder-which-web -->

There is no agreed definition of a filament. Across twelve finders the
filament mass fraction spans from ~10% (MSWA) to ~60% (DisPerSE), and void
volume fractions fall in three groups at ~40%, ~70% and ~90%
(arXiv:1705.03021) [src: Sect. 5.3]. Observational catalogues of the DESI era
give void volume fractions of ~6–16% across DR1 tracers with the T-web
(arXiv:2604.02463) [src: abstract] and ~59% for EDR BGS with ASTRA thresholds
tuned to GAMA (arXiv:2604.01456) [src: Sect. "The rank parameter r"]. Directions of progress:
physically motivated thresholds (arXiv:2412.09531) [src], probabilistic
per-object classes (arXiv:2604.01456) [src], filament populations separated by
length (arXiv:2003.09697) [src], and hierarchies of sub-filaments
(arXiv:2608.25840) [src]. Machine-learned classifiers and generative models of
web environments (for example arXiv:2609.09950, diffusion-model attention maps
compared with T-web classes [src]) belong to `cosmo-machine-learning`.

## 5. Protoclusters: tracer discrepancies and abundance
<!-- key: protoclusters-tracer-discrepancies-and-abundance -->

**Abundance at z > 5.** JWST candidates looked two to 300 times too numerous
for ΛCDM (2.3σ to 4σ); Witten et al. (2026, arXiv:2605.28930) remove the
tension by matching aperture definitions of halo mass and using forward
tracking, and conclude that 64% of the candidates are proto-groups [src: abstract]. A
claim of too many protoclusters should state the aperture of the mass estimate
and the descendant-mass criterion.

**Purity of photometric candidates.** More than 76% of HSC z ~ 3.8 candidates
are predicted to become ≥ 10¹⁴ M☉ haloes once projection is modelled
(arXiv:1708.09421) [src: abstract]; spectroscopy of three z ~ 3 candidates
confirmed all three but found individual diversity (arXiv:2610.01816) [src:
abstract].

**Galaxy versus gas selection.** Forest-selected and galaxy-selected
protoclusters do not always coincide (summarised in `cosmo-lyman-alpha`, open
questions §9); ODIN now overlaps one LATIS field directly (arXiv:2603.09739)
[src], the setting where that question can be tested.

## 6. What next data will decide
<!-- key: what-next-data-will-decide -->

| Question | Data | Expected | Citation | Flag |
|---|---|---|---|---|
| WHIM detection on more filaments, temperature distribution | eROSITA all-sky stacks beyond eRASS:4 | the 9σ eRASS:4 total sets the baseline | arXiv:2406.00105 | [src] |
| Baryons in voids and filaments | CHORD, DSA, SKA FRBs × DESI, LSST, Euclid, PFS, SPHEREx, Roman | samples "by orders of magnitude" larger, tomographic baryon mapping | arXiv:2605.01994 | [src], **forecast** |
| Galaxy–web alignments at z ~ 2.5 | PFS galaxies + IGM tomography | Δ⟨cos θ⟩ ~ 0.03 | arXiv:1612.00067 | [src: abstract], **forecast** |
| Web in photometric surveys | J-PAS | dynamically dominant voids recoverable | arXiv:2607.26932 | [src] |
| Filament connectivity as cosmology | large-volume skeletons | mean connectivity decreases with redshift in a cosmology-dependent way | arXiv:1803.11477; arXiv:2309.08659 | [src] |

## 7. Stale claims and misconceptions
<!-- key: stale-claims-and-misconceptions -->

| Claim | Correction | Citation |
|---|---|---|
| "Filaments contain X% of the mass" as a property of the Universe | the value ranges from ~10% to ~60% across finders on one simulation | arXiv:1705.03021 [src: Sect. 5.3] |
| "The missing baryons have been found" in X-ray absorption | re-analysis of the two O VII lines: z = 0.3551 has a look-elsewhere-corrected p ≈ 0.46, very likely a fluctuation; z = 0.4339 stays above 99.9% but the blazar likely sits in a group at z ≈ 0.433, so the line may be intrinsic or intra-group and its WHIM identification is tentative [src: Sect. 4.4.1–4.4.2]; one new possible line at 2.6σ, large systematics | arXiv:1806.08395 vs arXiv:2305.01587 [src] |
| "X-ray stacks measure the WHIM" | they trace its hot, dense end, and ~40% of the stacked emission is unmasked haloes, AGN and X-ray binaries | arXiv:2406.00105 [src: abstract] |
| "Galaxies in filaments are redder because of the filament" | the difference vanishes at fixed local density in SDSS | arXiv:2409.09028 [src] |
| "Spins align with filaments" without qualification | parallel at low mass, perpendicular at high mass, with a method- and selection-dependent transition | arXiv:1805.00033; arXiv:1902.09797 [src] |
| "JWST finds too many protoclusters for ΛCDM" | aperture and tracking inconsistencies; 64% of candidates likely proto-groups | arXiv:2605.28930 [src: abstract] |
| "A void in the galaxy distribution is empty of matter" | only three of seven nearby voids show a central matter underdensity dynamically | arXiv:2211.16388 [src] |
| "Overdensities alone drive the Local Group motion" | the local flow is dominated by a single attractor (Shapley) and a single, previously unidentified repeller | arXiv:1702.02483 [src] |

## 8. Do simulations get filament gas right?
<!-- key: do-simulations-get-filament-gas-right -->

Three recent stacks lean the same way, each mildly. The eRASS:4 WHIM
temperature, log(T/K) = 6.84 ± 0.07, is "marginally higher" than in
simulations, possibly because a single-temperature model is fitted to a
multi-temperature spectrum (arXiv:2406.00105) [src: abstract]. The kSZ signal oriented
on DESI BGS filaments is "comparable but slightly larger and more extended"
than in TNG300-1 and Illustris, read by the authors as excess accretion and
feedback through filaments (arXiv:2412.03631) [src]. The oriented ACT DR6
tSZ stacks prefer the model with higher average pressure in extended
structures, with the CIB as the main caveat (arXiv:2409.04535) [src]. None
of these is a tension at a stated significance; together they make the
filament-gas budget a test of feedback models, which connects to the
baryonic-suppression debate in `cosmo-cmb-lss-cross-correlations` and
`cosmo-weak-lensing`.

## 9. Void galaxies: environment or selection?
<!-- key: void-galaxies-environment-or-selection -->

The CAVITY results (slower star-formation histories, smaller early-type
galaxies; arXiv:2306.16818, arXiv:2501.07345) [src] compare void galaxies
with galaxies in denser large-scale environments. The SDSS DR7 size deficit
of massive void galaxies is "a steep function of the underdensity contrast",
deepening toward void interiors and vanishing at typical density, which the
authors take to mean that "strict density control and sample selection are
imperative" (arXiv:2609.19253) [src]. A void-galaxy claim therefore needs
the void finder, the local density contrast of each galaxy and a matched
control sample; comparisons between CAVITY (its own void catalogue) and
VoidFinder-based SDSS samples are not like for like.

## 10. Lyα emission from the web
<!-- key: lyalpha-emission-from-the-web -->

Diffuse Lyα emission maps filaments directly: filaments extending more than
one megaparsec in the SSA22 protocluster at z = 3.1 (arXiv:1910.01324) [src:
abstract] and, at 3 ≲ z ≲ 5, a trend of surface brightness with LAE
overdensity in the MUSE deep fields, with an emitting area fraction of
0.20–0.25 inside filaments (arXiv:2609.20938) [src: abstract]. The emission is
powered by local ionising sources in overdense regions (arXiv:1910.01324)
[src], so it traces the dense spines and the brightest environments, not the
average filament; the MUSE authors forecast oriented stacking in larger,
shallower samples (arXiv:2609.20938) [src].

## Not verified
<!-- key: not-verified -->

- Whether the filament spin used in arXiv:2506.22794 has been independently
  confirmed was not searched.
- The cosmological constraining power claimed for connectivity and filament
  statistics (arXiv:1803.11477, arXiv:2309.08659) was not quantified in any
  paper read; cosmology from voids and density-split statistics is in
  `cosmo-beyond-two-point`.
