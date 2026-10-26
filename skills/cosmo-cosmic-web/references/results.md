# Cosmic web — results

Scope: headline measurements on the cosmic web — mass and volume fractions per
component, filament and node statistics, environmental dependence of haloes
and galaxies, spin alignments, filament gas detections and the baryon census,
protoclusters — with what superseded what.
Snapshot: 2026-10-26

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Eq. n]`,
`[src: Table n]` body read; `[sec]` named secondary source; `[der]` derived
here.

## 1. Mass and volume fractions per web component
<!-- key: mass-and-volume-fractions-per-web-component -->

A mass or volume fraction is a property of a finder, a tracer and a smoothing
scale, not of the Universe. The comparison of twelve finders on one
dark-matter simulation (Libeskind et al. 2018, arXiv:1705.03021) defines mass
fraction as the particles in all cells of one type over all particles, and
volume fraction as the cells of one type over all cells, on 100³ cells of (2
h⁻¹Mpc)³ [src: Sect. 5.3].

| Component | Range across finders (z = 0, dark matter) | Grouping of methods | Citation | Flag |
|---|---|---|---|---|
| Knots | most methods: < ~1% of the volume, 10–20% of the mass; ORIGAMI (no knot/halo distinction): nearly half the mass in ~7% of the volume | mass and volume fractions follow a tight linear proportionality across methods | arXiv:1705.03021 | [src: Sect. 5.3] |
| Filaments | volume from virtually nothing (MSWA) to more than a third (SpineWeb, ~35%); mass from ~10% (MSWA) to ~60% (DisPerSE, SpineWeb; DisPerSE volume ~25%); Bisous, CLASSIC, V-web, MMF-2: ~5% of the volume, ~30% of the mass | weaker linear trend, larger spread | arXiv:1705.03021 | [src: Sect. 5.3] |
| Sheets | mass ~30% ± 5% for most methods (ORIGAMI and MMF-2 lower); volume from < ~10% (MSWA) to > 40% (T-web) | tight in mass, loose in volume | arXiv:1705.03021 | [src: Sect. 5.3] |
| Voids | volume in three groups: ~40% (DisPerSE, SpineWeb, T-web), ~70% (NEXUS+, ORIGAMI, V-web, MMF-2, CLASSIC), ~90% (MSWA); mass 10–15% for the first group, ~15% (NEXUS+) to ≳ 50% (MMF-2) for the second | void and filament mass fractions anti-correlate across methods | arXiv:1705.03021 | [src: Sect. 5.3] |
| NEXUS+ alone | nodes: significant mass, negligible volume; filaments: half the mass in a relatively small volume; walls: mean density 1 + δ ~ 1; voids: by far the largest volume, ~15% of the mass | the five NEXUS variants agree approximately; density-based variants put more mass in filaments than velocity-based ones | Cautun et al. 2014, arXiv:1401.7866 | [src: Sect. 5.1] |
| Haloes per environment (NEXUS+) | < 10% of haloes above 10¹² h⁻¹M☉ in sheets, < 20% of 10¹¹ h⁻¹M☉ haloes in walls, at most 5% of haloes ≥ 10¹¹ h⁻¹M☉ in voids | most galaxies of redshift surveys are in filaments and nodes | arXiv:1401.7866 | [src: Sect. 5.1] |
| SDSS galaxies (Bisous, ~0.5 h⁻¹Mpc radius) | filaments hold 35–40% of the total galaxy luminosity in roughly 5–8% of the volume | agrees with N-body simulations | Tempel et al. 2014, arXiv:1308.2533 | [src] |

Observational volume fractions per web class, each with its own method:

| Data | Volume fractions | Method | Citation | Flag |
|---|---|---|---|---|
| DESI DR1 BGS, LRG, ELG | sheets ~45–48%, filaments ~37–40%, voids ~6–16%, knots ~4–6% | T-web, 256³ grid in an 800 Mpc cube | Ullah et al. 2026, arXiv:2604.02463 | [src: abstract] |
| DESI EDR BGS | void volume fraction ~59%, by construction equal to GAMA at 4 h⁻¹Mpc smoothing; the uncalibrated ASTRA void threshold gave only ~2.5% | ASTRA rank thresholds | Zapata-Zuluaga et al. 2026, arXiv:2604.01456 | [src: Sect. "The rank parameter r"] |

The DESI DR1 and DESI EDR void fractions above differ through the method
and the threshold, not the data: the EDR thresholds were recalibrated to
GAMA, while the uncalibrated ASTRA threshold gave a much smaller fraction
[der: comparison of the two rows].

Earlier literature quoted void volume fractions from ~10% (Hahn et al. 2007;
Forero-Romero et al. 2009) to ~90% (MMF, phase-space), for the same reason
(arXiv:1401.7866) [src: Sect. 5.1]; Table 3 of that paper compiles them.

## 2. Filaments, nodes and walls: statistics and evolution
<!-- key: filaments-nodes-and-walls-statistics-and -->

| Quantity | Value | Data or simulation | Citation | Flag |
|---|---|---|---|---|
| Evolution of mass fractions (NEXUS+) | nodes hold significant mass only after z = 1 and 10% today; filament mass rises to z ~ 0.5 then decreases slightly as nodes accrete it; filament volume falls by a factor 2 from z = 2 to today; walls hold ~20% less mass and volume than at early times | dark-matter simulations | arXiv:1401.7866 | [src: Sect. 6.1] |
| Mass transport | less than 40% of the z = 2 wall mass is still in walls today, most having flowed into filaments; about half the z = 2 void mass has streamed into sheets and filaments; up to 20% of today's sheet mass was tagged filament earlier (a finder artefact) | same | arXiv:1401.7866 | [src: Sect. 7] |
| Filament mass–length relation | median M_f ∝ L^2.2 at z = 0 | same | arXiv:1401.7866 | [src: Fig. 55 caption] |
| Longest filaments | > 100 h⁻¹Mpc, nearly straight, bridging massive clusters (simulation); up to 60 h⁻¹Mpc in SDSS (Bisous); up to 200 h⁻¹Mpc in GAMA (MST, 643 filaments, average 8 groups each); GAMA "tendrils" ~10 h⁻¹Mpc with ~6 galaxies | finder-dependent | arXiv:1401.7866; arXiv:1308.2533; arXiv:1311.1211 | [src: abstract] |
| Connectivity of Gaussian random fields | nodes connected on average to exactly κ = 4 neighbours in 2D and ~6.1 in 3D; local number of filaments 3 (2D) and 4 (3D); κ rises with peak height and scales as 10/3 times the log of halo mass; mean connectivity decreases with redshift and scale in a cosmology-dependent way | peak theory, persistent skeleton | Codis, Pogosyan & Pichon 2018, arXiv:1803.11477 | [src: abstract] |
| Connectivity–mass relation in N-body haloes | power law from group to cluster scale for 22,900 haloes with M200c = 10¹²–10¹⁵·⁵ h⁻¹M☉; stated as the first N-body confirmation of the predicted scaling across three decades | MDPL2, (1 h⁻¹Gpc)³, 92 million haloes, multi-block DisPerSE | Singh et al. 2026, arXiv:2607.14785 | [src: abstract] |
| Connectivity evolution | node connectivity globally decreases from early to late times; comoving filament length functions and overdensity profiles almost unchanged over the last ~12.25 Gyr; short filaments contract, long ones extend; ~5σ density difference between shortest and longest | MillenniumTNG galaxies, z = 0–4 | Galárraga-Espinosa et al. 2024, arXiv:2309.08659 | [src: abstract] |
| Cluster connectivity in a photometric survey | connectivity increases with cluster mass at all redshifts up to z < 1; at fixed mass, clusters with a higher fraction of red (elliptical) galaxies are more strongly connected; radial red and elliptical fractions hint at pre-processing in filaments; consistent with Euclid Q1 | DES Y3 photometry, 2D DisPerSE in tomographic slices of 220 Mpc comoving thickness at ~0.1 galaxies Mpc⁻², public cluster catalogues | Gouin et al. 2026, arXiv:2610.31800 | [src: abstract] |
| Two filament populations | short (L_f < 9 Mpc) filaments are puffier, denser and attached to massive nodes; long (L_f > 20 Mpc) thinner and less dense; galaxy-density excess > 5σ out to 27 Mpc from the spine | Illustris-TNG, Illustris, Magneticum, DisPerSE | Galárraga-Espinosa et al. 2020, arXiv:2003.09697 | [src: abstract] |
| Filament radius | slope of the stacked galaxy profile is minimal at ~1 Mpc from the spine at z = 0, in simulations and data; radius falls quickly from z = 4 to 1, then rises slightly | hydrodynamical simulations and observations | Wang et al. 2024, arXiv:2402.11678 | [src] |
| Galaxy bias in filaments | object-by-object large-scale bias up to ~4 times the halo-mass expectation in node outskirts; mean bias 1.4 for short filaments falling to −0.5 for the longest, at fixed halo mass and colour; normalised bias ~0.85 near saddle points to ~1.06 near nodes along long filaments | TNG300, DisPerSE | Soto-Suárez et al. 2026, arXiv:2608.25060 | [src: abstract] |
| Sub-filaments | sub-filaments inside larger filaments have radial phase-space profiles distinct from their parents | hierarchical reconstruction in simulations | Dhawalikar et al. 2026, arXiv:2608.25840 | [src] |

## 3. Environmental dependence of haloes and galaxies
<!-- key: environmental-dependence-of-haloes-and-galaxies -->

### 3.1 Void galaxies
<!-- key: void-galaxies -->

| Result | Value | Sample | Citation | Flag |
|---|---|---|---|---|
| Star-formation histories | void galaxies have had, on average, slower SFHs than galaxies in filaments, walls and clusters; both "short-timescale" and "long-timescale" SFH types evolve slower in voids | CAVITY parent sample (SDSS spectra) | Domínguez-Gómez et al. 2023, arXiv:2306.16818 | [src] |
| Mass–size relation | early-type void galaxies 10–20% smaller than counterparts in denser environments, with a shallower slope at high mass; ~140,000 galaxies, 10^8.5–10^11 M☉ | CAVITY parent sample + SDSS DR16 images | Pérez et al. 2025, arXiv:2501.07345 | [src: abstract] |
| High-mass size deficit | at fixed stellar mass, redshift and colour, void galaxies with M* > 10¹¹ h⁻¹M☉ are 11 ± 3% more compact; deficit deepens toward the emptiest interiors and vanishes at typical density; reproduced by TNG300 | SDSS DR7 NSA, VoidFinder, z ≤ 0.114 | Curtis et al. 2026, arXiv:2609.19253 | [src: abstract] |
| Void galaxies in photometric-survey mocks | lower stellar masses, bluer colours and enhanced star formation relative to equal-mass galaxies in dense regions, preserved with J-PAS-like redshift errors | FLAMINGO mocks, z = 0.3 | arXiv:2607.26932 | [src: abstract] |

### 3.2 Haloes and galaxies in filaments, sheets and nodes
<!-- key: haloes-and-galaxies-in-filaments-sheets-and -->

| Result | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Halo formation time by web class | below M*, haloes of given mass are older in clusters and younger in voids; no dependence at higher mass; low-mass cluster haloes less spherical and with higher median spin | N-body, Hessian classification | Hahn et al. 2007, arXiv:astro-ph/0610280 | [src] |
| Halo assembly bias by web class, observed | low-mass GAMA groups in knots are older than equal-mass groups in voids; the trend reverses at high mass | GAMA, tidal-tensor classes | Tojeiro et al. 2017, arXiv:1612.08595 | [src] |
| Mass and colour gradients toward the skeleton | more massive and passive galaxies lie closer to filaments and walls; red fraction rises toward nodes and toward filaments regardless of node distance; star-forming galaxies redden at fixed mass near filaments; Horizon-AGN reproduces the trends | GAMA, DisPerSE | Kraljic et al. 2018, arXiv:1710.02676 | [src] |
| Clustering and quenching vs δ₈ and α₅ | quenching primarily a function of δ₈, with a subtle dependence on α₅ at fixed δ₈; an iHOD mock whose web dependence comes only from the halo mass function reproduces the main trends, so any direct effect of the tidal field on scales > 5 h⁻¹Mpc "must be extremely weak" | SDSS | Alam et al. 2019, arXiv:1801.04878 | [src] |
| Filament effect reduces to local density | SDSS filament galaxies less star-forming and more early-type than field galaxies at fixed stellar mass; the difference vanishes when local galaxy density is also matched; cluster interiors still differ | 23,441 SDSS DR8 galaxies with M* > 10^9.91 M☉ | O'Kane et al. 2024, arXiv:2409.09028 | [src: abstract] |
| Quenched fraction by T-web class | highest in clusters, intermediate in filaments, lowest in sheets; flattening above log M* ~ 10.6; at log M* ≳ 11.5 quenched and bulge fractions rise in clusters and fall in sheets | SDSS DR18, mass-matched | Nandi & Pandey 2025, arXiv:2507.18614 | [src: abstract] |
| Star formation vs filament distance over time | z ≳ 2: enhanced SFR and gas accretion close to filaments; z = 0: V-shaped sSFR trend with minimum at ~0.25 cMpc and an upturn near cores, mostly satellites | SIMBA, DisPerSE | Jego et al. 2025, arXiv:2509.18077 | [src: abstract] |
| Low-mass filament galaxies | integrated properties and quenched fractions similar to the field at fixed stellar and halo mass, outside groups; smaller, more asymmetric cold-gas discs; "cosmic web stripping" for late infallers | TNG50, 10⁸–10¹⁰ M☉ | Zakharova et al. 2026, arXiv:2605.23457 | [src: abstract] |
| Which property feels the web most | star formation varies most with distance to web features but also tracks local density most; spin direction varies least but is most independent of local density | IllustrisTNG, DisPerSE | Malavasi et al. 2022, arXiv:2109.14623 | [src] |
| DESI DR1 colours by T-web class | stellar mass drives the primary quenching trend; LRG red fractions at z ≈ 0.66 range from 58.37 ± 3.15% (sheets) to 65.90 ± 0.45% (knots) and converge to ~68–70% by z ≈ 0.88 | BGS, LRG, ELG | Ullah et al. 2026, arXiv:2604.02463 | [src: abstract] |
| Evolution with redshift | z < 1: stellar mass up to ~0.35 dex higher in clusters than field, SFR suppressed by ~0.1 dex in clusters; 1 < z < 2: largely independent of environment; z > 2: mild increase of SFR (~+0.1 dex) and sSFR (~+0.13 dex) from field to clusters | COSMOS2020, MMF on galaxy density maps, 0.4 < z < 4 | Taamoli et al. 2026, arXiv:2610.07710 | [src: abstract] |
| Causal test | splicing a Milky-Way-mass halo next to a large filament leaves its mass and virial radius unchanged, but changes spin and shape orientation relative to the filament by up to 80% around the mean | zoom simulations with fixed initial patch | Storck et al. 2024, arXiv:2409.13010 | [src: abstract] |

The summary of this table: at fixed stellar mass, environmental trends along
the web are detected in every survey; whether a trend remains at fixed halo
mass and local density is the decisive test, and the SDSS analyses that apply
it (arXiv:1801.04878, arXiv:2409.09028) find little or nothing left. See
`open-questions.md` §2.

## 4. Spin and shape alignments
<!-- key: spin-and-shape-alignments -->

| Result | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Halo spin flip, first large measurement | spins of haloes above a critical mass ~5 × 10¹² (units as printed in the abstract, M☉) perpendicular to the closest filament and aligned with the intermediate tidal axis; below it, aligned with the filament; critical mass scales as (1 + z)^−2.5 | Horizon 4π, 43 million haloes | Codis et al. 2012, arXiv:1201.5794 | [src] |
| Halo spin flip with NEXUS | flip at an average mass of 5 × 10¹¹ h⁻¹M☉, rising with filament diameter by more than an order of magnitude from thinnest to thickest filaments; inner halo flips at a several times smaller mass; major axes and velocities strongly aligned with filaments | P-Millennium | Ganeshaiah Veena et al. 2018, arXiv:1805.00033 | [src: abstract] |
| SDSS spirals and ellipticals | spiral spins align with the host Bisous filament, more strongly in the outer parts; minor axes of ellipticals preferentially perpendicular; weak correlation with sheets | SDSS | Tempel & Libeskind 2013, arXiv:1308.2816 | [src] |
| Siena Galaxy Atlas + SDSS DR12 Bisous filaments | ellipticals perpendicular at up to ≈ 13σ; spirals weakly aligned at ≈ 2.8σ; significance depends on how it is measured; maximum within 0.5–1 Mpc (spirals) and 0.2–0.5 Mpc (ellipticals) of the spine | 32,517 discs and 18,955 ellipticals within 2 Mpc of a spine, z ≤ 0.2 | Muralichandran et al. 2025, arXiv:2509.02062 | [src: abstract] |
| SAMI stellar kinematics | first mass-dependent spin–filament transition from IFS at > 2σ: low-mass aligned, high-mass orthogonal; transition stellar mass between log M* = 10.4 and 10.9; DisPerSE filaments on GAMA; reproduced by Horizon-AGN, not by dark-matter-only + semi-analytic models | SAMI | Welker et al. 2020, arXiv:1909.12371 | [src: abstract] |
| SAMI bulge dependence | bulge mass M_bulge = M* × (B/T) is the primary correlate of the flip; S0s preferentially perpendicular | SAMI + GAMA filaments | Barsanti et al. 2022, arXiv:2208.10767 | [src] |
| MaNGA, first analysis | no evidence for alignment; hints of mass dependence in 2–3σ tension with MassiveBlack-II and Illustris, which vanish with Hα instead of stellar velocities | MaNGA + SDSS filaments (Cosmic Web Reconstruction) | Krolewski et al. 2019, arXiv:1902.09797 | [src] |
| MaNGA, 3D spins | late-type spirals parallel to the closest filament, dominated by low-mass spirals; S0s preferentially perpendicular; signal weak but statistically significant | MaNGA + SDSS DisPerSE | Kraljic et al. 2021, arXiv:2104.08275 | [src] |
| Galaxy spin vs filament spin | low-mass spirals (log M* ≲ 10) anti-parallel to the spin of their filament, enhanced in dynamically cold filaments; no trend at high mass | MaNGA; filament spin from redshift asymmetry across spines | Wang et al. 2025, arXiv:2506.22794 | [src: abstract] |

## 5. Gas in filaments and the baryon census
<!-- key: gas-in-filaments-and-the-baryon-census -->

### 5.1 Filament gas detections
<!-- key: filament-gas-detections -->

| Detection | Significance | Inferred gas | Data and method | Citation | Flag |
|---|---|---|---|---|---|
| tSZ between SDSS DR12 LRG pairs (~260,000 pairs, 6–10 h⁻¹Mpc tangential, < 6 h⁻¹Mpc radial) | 5.3σ, Δy = (1.31 ± 0.25) × 10⁻⁸ | δ_c (T_e/10⁷ K)(r_c/0.5 h⁻¹Mpc) = 2.7 ± 0.5; BAHAMAS gives (0.84 ± 0.24) × 10⁻⁸ | Planck y, pair stacking with halo subtraction | Tanimura et al. 2019, arXiv:1709.05024 | [src: abstract] |
| tSZ between 1,002,334 CMASS pairs | 2.9σ, y = (0.6 ± 0.2) × 10⁻⁸ for a 10.5 h⁻¹Mpc stacked filament | ρ_b = (5.5 ± 2.9) ρ̄_b, T = (2.7 ± 1.7) × 10⁶ K with lensing; 11 ± 7% of all baryons, 28 ± 12% on the longer baseline; bound halo gas ≤ 20% of the signal | Planck y + lensing | de Graaff et al. 2019, arXiv:1709.10378 | [src: abstract] |
| tSZ along 24,544 SDSS filaments of 30–100 Mpc | 4.4σ tSZ; 8.1σ CMB lensing | central overdensity 19.0 (+27.3/−12.1), T = (1.2 ± 0.4) × 10⁶ K, baryon fraction (0.080 +0.116/−0.051) Ω_b | Planck y and κ, groups above ~3 × 10¹³ M☉ excluded | Tanimura et al. 2020, arXiv:1911.09706 | [src: abstract] |
| X-ray along 15,165 SDSS filaments (0.2 < z < 0.6, 30–100 Mpc) | 4.2σ in 0.56–1.21 keV | T = 0.9 (+1.0/−0.6) keV, central overdensity ~30 | ROSAT stacking | Tanimura et al. 2020, arXiv:2011.05343 | [src: abstract] |
| X-ray along 463 filaments in eFEDS | 3.8σ; null probability ~0.0017 | T = 1.0 (+0.3/−0.2) keV, central overdensity 21 ± 5 | eROSITA eFEDS, 0.4–2.3 keV | Tanimura et al. 2022, arXiv:2206.00084 | [src: abstract] |
| X-ray along 7817 SDSS filaments | 9σ total, 5.4σ attributed to WHIM after ~40% contamination by unmasked haloes, AGN and X-ray binaries | log(T/K) = 6.84 ± 0.07 (single-temperature fit), log Δ_b = 1.88 ± 0.18 for 0.2 Z☉ | eRASS:4, imaging + spectral stacking, 0.3–1.2 keV | Zhang et al. 2024, arXiv:2406.00105 | [src: abstract] |
| Oriented tSZ around DES Y3 clusters in superclusters, 2.5–40 Mpc | dipole and quadrupole at 8–10σ, m = 4 at up to 6σ | prefers higher average pressure in extended structures; CIB contamination limits it | ACT DR6 y × DES Y3 | Lokken et al. 2024, arXiv:2409.04535 | [src: abstract] |
| kSZ oriented on 2D filaments around DESI BGS, z ≈ 0.3 | 7.2σ monopole, 4σ quadrupole (first kSZ gas–web alignment) | slightly larger and more extended than TNG300-1 and Illustris | ACT × DESI Legacy imaging | Hadzhiyska et al. 2024, arXiv:2412.03631 | [src: abstract] |
| A399–A401 bridge, tSZ | two-cluster-only model excluded at > 5σ | filament mass (3.3 ± 0.7) × 10¹⁴ M☉ (~8% of the system), width ~1.9 Mpc, n = (0.88 ± 0.24) × 10⁻⁴ cm⁻³ with Suzaku T | ACT + Planck, MUSTANG-2 | Hincks et al. 2022, arXiv:2107.04611 | [src: abstract] |
| A399–A401 bridge, radio | ridge of 140 MHz emission between the clusters: relativistic electrons and magnetic field in the filament | LOFAR | Govoni et al. 2019, arXiv:1906.07584 | [src: abstract] |
| A3391/95 system | 15 Mpc projected continuous warm-hot emission filament; bridge between the clusters with hints of warm gas | dedicated eROSITA + ASKAP/EMU + DECam over 15 deg² | Reiprich et al. 2021, arXiv:2012.08491 | [src: abstract] |
| Abell 2744 | hot (10⁷ K) gas filaments coherent over 8 Mpc; 5–10% of filament mass in baryonic gas | XMM-Newton with point sources removed, plus lensing | Eckert et al. 2015, arXiv:1512.00454 | [src: abstract] |
| Magnetic field in filaments | if the whole 144 MHz residual RM is from filaments: RRM_0,f = 0.71 ± 0.07 rad m⁻², B_f = 32 ± 3 nG | LoTSS DR2 RM catalogue vs NVSS at 1.4 GHz | Carretti et al. 2022, arXiv:2202.04607 | [src: abstract] |
| Magnetic field in one X-ray-detected filament (A3667–A3651, > 13 Mpc projected) | residual RM dispersion 6.9 ± 3.6 rad m⁻² (marginal), coherent median residual RM 6.3 ± 1.3 rad m⁻² | B = 0.1–3.5 μG at 95% confidence, preferred 0.2–0.3 μG depending on coherence scale; stated as the first Faraday-rotation constraint in an individual X-ray-detected inter-cluster filament; structured Galactic foreground RM is a major uncertainty | POSSUM RM grid, 54 background polarised sources, electron-density priors from eROSITA X-ray | Stuardi et al. 2026, arXiv:2608.28758 | [src: abstract] |
| A3266 and its north-western group | X-ray filament at 3.6σ over a 3D length L_R200–R200 = 1.1 (+0.5/−0.1) Mpc | T = 1.2 (+0.3/−0.2) keV, Z = 0.07 (+0.09/−0.05) Z☉, n_e = 8 (+1/−2) × 10⁻⁵ cm⁻³ for a simple geometry; hotter and denser than pristine WHIM, consistent with gas processed in the cluster environment | eROSITA all-sky survey imaging and spectra, NED member galaxies, SLOW constrained simulation | Dietl et al. 2026, arXiv:2607.28140 | [src: abstract] |

The X-ray stacks see the hot, dense end of the WHIM: the eRASS:4 authors state
that the broadband emission "traces the high end of the temperature and
density values" of the WHIM population (arXiv:2406.00105) [src].

### 5.2 The baryon census
<!-- key: the-baryon-census -->

| Census | Result | Method | Citation | Flag |
|---|---|---|---|---|
| UV absorber census, low z | photoionised Lyα forest 28 ± 11%, O VI/BLA-traced WHIM 25 ± 8%, collapsed phase (galaxies, groups, clusters, CGM) 18 ± 4%; shortfall 29 ± 13% | HST H I, O VI and broad Lyα absorbers with ionisation and metallicity corrections | Shull, Smith & Danforth 2012, arXiv:1112.2706 | [src: abstract] |
| O VII absorbers toward 1ES 1553+113 | two O VII absorbers in regions of ×4 galaxy overdensity; "the missing baryons have been found" | XMM-Newton high-S/N X-ray spectrum | Nicastro et al. 2018, arXiv:1806.08395 | [src: abstract] |
| Re-analysis of the same quasar | one possible O VII at z = 0.1877 at 2.6σ with an O VI prior; stacking finds no further X-ray WHIM; the two earlier lines re-examined; hot WHIM Ω_WHIM,X/Ω_b = 44 ± 22% with large systematic uncertainties | XMM-Newton | Spence et al. 2023, arXiv:2305.01587 | [src: abstract] |
| FRB census, first | Ω_b = 0.051 (+0.021/−0.025) h₇₀⁻¹ (95% confidence), consistent with CMB and BBN | localized FRBs including four new hosts at z = 0.118–0.522 | Macquart et al. 2020, arXiv:2005.13161 | [src: abstract] |
| FRB census and partition | Ω_b h₇₀ = 0.051 ± 0.006; f_IGM = 0.76 (+0.10/−0.11); f_X (baryons in intersected haloes) = 0.15 (+0.11/−0.10) | 39 new DSA-110 FRBs with spectroscopic hosts (9 unique to the paper, three near or beyond z = 1) plus 30 earlier localisations; IGM defined as gas outside virialised haloes | Connor et al. 2024, arXiv:2409.16952 | [src: abstract] for Ω_b and f_IGM; [src: Results] for f_X and sample |
| FRB DM in voids | DM deficit toward void centres at 3.2σ; uniform-void electron contrast δ_e,v = −0.58 ± 0.30 (~60% baryon underdensity); with tSZ stacks T_e ≲ (1.1 ± 0.7) × 10⁶ K | 3455 CHIME/FRB sightlines on 1288 SDSS BOSS voids, 0.2 < z < 0.7 | Sharma et al. 2026, arXiv:2605.01994 | [src: abstract] |
| WHIM tracers between cluster pairs | excess incidence of broad Lyα absorbers and O VI about twice that of narrow Lyα; covering fractions ~1.7 and 1.8 times the random field | HST/COS, ten QSO sightlines near cluster pairs, z < 1, Δv = ±1000 km/s, Δd < 3 Mpc | Martínez-Acosta et al. 2026, arXiv:2610.11203 | [src: abstract] |
| Filament gas fraction from stacks | 11 ± 7% of all baryons (28 ± 12% on the longer baseline) from CMASS pair tSZ; (0.080 +0.116/−0.051) Ω_b from filament tSZ | see §5.1 | arXiv:1709.10378; arXiv:1911.09706 | [src: abstract] |

Quoted shortfalls depend on the reference epoch and on what is counted as
"observed": 30–40% (arXiv:1806.08395), "a factor of two" (arXiv:1512.00454),
"~10%" of baryons in galaxies and clusters (arXiv:1709.10378) [src: abstract of each]. The FRB
dispersion measure counts every ionised baryon along the line of sight and is
the only census independent of gas phase (arXiv:2005.13161) [src]; the use of
the DM–redshift relation for H₀ and Ω_b as cosmology is in
`cosmo-multimessenger`.

## 6. Protoclusters and superclusters
<!-- key: protoclusters-and-superclusters -->

### 6.1 Superclusters
<!-- key: superclusters -->

Supercluster catalogues are defined either by friends-of-friends percolation
of groups and clusters with a linking length chosen before percolation, or by
thresholding a luminosity-density field smoothed at 8 h⁻¹Mpc (D8) (M. Einasto
2025 review, arXiv:2505.22082) [src: Sect. 2]. At threshold D_t ≈ 5,
superclusters fill about 1% of the volume; the percolation functions of
superclusters are similar in ΛCDM and SDSS, those of voids very different
[src: Sect. 2].

| Structure | Facts | Data | Citation | Flag |
|---|---|---|---|---|
| Laniakea | supercluster defined dynamically as the volume inside the surface of diverging peculiar-velocity flows around us | Cosmicflows peculiar-velocity catalogue | Tully et al. 2014, arXiv:1409.0880 | [src] |
| BOSS Great Wall, z ≈ 0.47 | two walls of 186 and 173 h⁻¹Mpc diameter and two superclusters of 64 and 91 h⁻¹Mpc; 830 galaxies; total mass ≈ 2 × 10¹⁷ h⁻¹M☉ | BOSS, luminosity density smoothed at 8 h⁻¹Mpc, 0.43 < z < 0.71 | Lietzen et al. 2016, arXiv:1602.08498 | [src] |
| Hyperion proto-supercluster, z ≈ 2.45 | ~60 × 60 × 150 cMpc³, total mass ~4.8 × 10¹⁵ M☉, at least 7 density peaks of 0.1–2.7 × 10¹⁴ M☉ connected by filaments, predicted to virialise by z ~ 0.8–1.6 | VUDS + zCOSMOS-Deep + photo-z, 3D Voronoi density | Cucciati et al. 2018, arXiv:1806.06073 | [src] |

How the BOSS Great Wall appears in a constrained reconstruction of the
SDSS and BOSS volumes is recorded in `cosmo-simulations-mocks`.

### 6.2 Protoclusters
<!-- key: protoclusters -->

**Definition.** Protoclusters are the progenitor regions of present-day
clusters (M > 10¹⁴ h⁻¹M☉); in the Millennium simulations they can be
identified to at least z ~ 5 if galaxy overdensities are measured on effective
radii R_e ~ 5–10 cMpc (Chiang, Overzier & Gebhardt 2013, arXiv:1310.2938)
[src: abstract]. The review of the field is Overzier 2016 (arXiv:1610.05201) [src].

| Result | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Systematic search at z ~ 3.8 | 216 overdense regions (> 4σ), 179 unique candidates over 121 deg²; > 76% predicted to become haloes ≥ 10¹⁴ M☉; correlation length 35.0 h⁻¹Mpc | HSC-SSP S16A g-dropouts | Toshikawa et al. 2018, arXiv:1708.09421 | [src: abstract] |
| Spectroscopic follow-up at z ~ 3 | three HSC U-dropout candidates confirmed (> 4σ on the sky, > 98.4% in redshift); individually diverse star formation and Lyα equivalent widths, average consistent with the field | HSC-SSP + spectroscopy | Toshikawa et al. 2026, arXiv:2610.01816 | [src: abstract] |
| ODIN + DESI | six protoclusters confirmed at z ≈ 2.4 and 3.1 over ≈ 14 deg²; one overlaps a LATIS tomographic field; a 1.2 × 10¹¹ M☉ quiescent galaxy at z ≈ 3.12; protocluster LAEs brighter with a deficit of faint emitters | ODIN narrowband Lyα + DESI spectroscopy, COSMOS and XMM-LSS | Ortiz et al. 2026, arXiv:2603.09739 | [src: abstract] |
| "Too many protoclusters" at z > 5 | apparent excess of Coma-like progenitors (~2 and 300 times, 2.3σ and 4σ) removed by comparing like with like: observed halo masses summed over ≳ 50 R_vir apertures vs simulated virial masses, and forward rather than backward tracking; 64% of candidates likely proto-groups (M200c < 10¹⁴ M☉), none likely Coma-like | JWST literature candidates vs TNG-Cluster and TNG300 | Witten et al. 2026, arXiv:2605.28930 | [src: abstract] |
| Lyα filaments in SSA22, z = 3.1 | Lyα emission from multiple filaments extending more than 1 Mpc between active galaxies | SSA22 protocluster | Umehata et al. 2019, arXiv:1910.01324 | [src: abstract] |
| Cosmic-web Lyα emission vs overdensity, 3 ≲ z ≲ 5 | 41 LAE overdensities (δ ≈ 2–10); non-detections mostly at δ < 2; maximum intrinsic SB ≈ 2 × 10⁻¹⁹ erg s⁻¹ cm⁻² arcsec⁻² at δ ≳ 3.5; emitting fraction of filament area 0.20–0.25 | MUSE Ultra Deep and Extremely Deep Fields | Tornotti et al. 2026, arXiv:2609.20938 | [src: abstract] |
| Galaxies in SSA22 web filaments | 18 dusty star-forming galaxies in Lyα-traced filaments of the core; median r₃₁ = 0.66 (+0.05/−0.04), as in the field; lower-mass members show excess gas fractions and depletion times | ALMA, JWST, JVLA | Umehata et al. 2026, arXiv:2609.06679 | [src: abstract] |

Lyα-tomography-selected protoclusters (CLAMATO, LATIS "Antu") and the tracer
discrepancies between forest and galaxy selections are recorded in
`cosmo-lyman-alpha` (results §7, open questions §9).

## 7. History of key numbers
<!-- key: history-of-key-numbers -->

| Quantity | Earlier | Later | Citation | Flag |
|---|---|---|---|---|
| Halo spin-flip mass | ~5 × 10¹² (Horizon 4π, critical mass scaling as (1 + z)^−2.5) | 5 × 10¹¹ h⁻¹M☉ on average with NEXUS, varying by more than ten with filament diameter | arXiv:1201.5794; arXiv:1805.00033 | [src: abstract] |
| Observed spin–filament transition | no evidence (MaNGA 2019, stellar spins) | SAMI transition at log M* = 10.4–10.9 (> 2σ); MaNGA 3D spins: spirals parallel, S0s perpendicular | arXiv:1902.09797; arXiv:1909.12371; arXiv:2104.08275 | [src: abstract] |
| Stacked tSZ from filaments | 5.3σ LRG pairs; 2.9σ CMASS pairs (2017) | 4.4σ along 30–100 Mpc filaments (2019); 8–10σ oriented multipoles with ACT DR6 (2024) | arXiv:1709.05024; arXiv:1709.10378; arXiv:1911.09706; arXiv:2409.04535 | [src: abstract] |
| Stacked X-ray from filaments | 4.2σ ROSAT (2020); 3.8σ eFEDS (2022) | 9σ total, 5.4σ WHIM, eRASS:4 (2024) | arXiv:2011.05343; arXiv:2206.00084; arXiv:2406.00105 | [src: abstract] |
| FRB Ω_b | 0.051 (+0.021/−0.025) h₇₀⁻¹ at 95% (2020) | Ω_b h₇₀ = 0.051 ± 0.006 with f_IGM = 0.76 (2024) | arXiv:2005.13161; arXiv:2409.16952 | [src: abstract] |
| UV census shortfall | 29 ± 13% missing (2012) | FRB census accounts for the total, partition statistical (2024) | arXiv:1112.2706; arXiv:2409.16952 | [src: abstract] |
| CAVITY releases | DR1 (2024) | DR2, 200 data cubes in 15 voids (2026) | arXiv:2410.08265; arXiv:2609.24726 | [src: abstract] |
| Connectivity–mass scaling | predicted from peak theory (2018) | confirmed across three decades of halo mass in MDPL2 (2026) | arXiv:1803.11477; arXiv:2607.14785 | [src] |

## Not verified
<!-- key: not-verified -->

- The units of the Codis et al. 2012 critical mass (arXiv:1201.5794,
  printed as "5 10^12" in the abstract) were not checked in the body here;
  `deep/spin-alignments.md` reads them in the body.
- No DESI DR1 or DR2 filament-gas stack (tSZ, kSZ or X-ray on DESI filaments)
  was found beyond the photometric BGS kSZ study.
- The SAMI and MaNGA alignment amplitudes (mean cos θ per mass bin) were not
  read from the bodies.
- The per-method table of mass and volume fractions in Libeskind et al. 2018
  was not read; the values above come from its text.
