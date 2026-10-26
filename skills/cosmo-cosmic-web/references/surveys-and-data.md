# Cosmic web — surveys and data

Scope: the galaxy surveys, filament and void catalogues, reconstructions,
X-ray, SZ, radio and FRB data sets, protocluster samples and simulations used
to study the cosmic web, past, current and planned.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Eq. n]`,
`[src: Table n]` body read; `[sec]` named secondary source; `[der]` derived
here.

## 1. Galaxy surveys and filament catalogues
<!-- key: galaxy-surveys-and-filament-catalogues -->

| Data set | What | Size, depth | Status | Citation | Flag |
|---|---|---|---|---|---|
| SDSS Bisous filament catalogue | public filament spines, radius ~0.5 h⁻¹Mpc | longest 60 h⁻¹Mpc | public | Tempel et al. 2014, arXiv:1308.2533 | [src: abstract] |
| GAMA large-scale structure catalogue | filaments, tendrils, isolated void galaxies from an adapted MST | 45,542 galaxies and 6,000 groups at z ≤ 0.213; 643 filaments | published | Alpaslan et al. 2014, arXiv:1311.1211 | [src: abstract] |
| CAVITY (Calar Alto Void Integral-field Treasury surveY) | integral-field spectroscopy of void galaxies, PMAS/PPAK V500, 3745–7500 Å at 6 Å FWHM | DR1 (2024, arXiv:2410.08265); DR2: 200 data cubes in 15 voids at 0.005 ≤ z ≤ 0.050 | DR2 public, cavity.caha.es | Bidaran et al. 2026, arXiv:2609.24726 | [src: abstract] |

Integral-field and imaging samples used against these skeletons: SAMI
galaxies assigned to DisPerSE filaments reconstructed on GAMA fields
(arXiv:1909.12371) [src]; MaNGA galaxies against SDSS skeletons from DisPerSE
(arXiv:2104.08275) and from the Cosmic Web Reconstruction algorithm
(arXiv:1902.09797) [src]; the Siena Galaxy Atlas, 32,517 discs and 18,955
ellipticals within 2 Mpc of SDSS DR12 Bisous spines at z ≤ 0.2
(arXiv:2509.02062) [src: abstract]. Environmental studies use GAMA at
0.03 ≤ z ≤ 0.25 with DisPerSE (arXiv:1710.02676) [src: abstract], SDSS DR8 with
23,441 mass-complete galaxies (arXiv:2409.09028) [src: abstract], SDSS DR18
(arXiv:2507.18614) [src] and COSMOS2020 to z = 4 (arXiv:2610.07710) [src: abstract].

## 2. Reconstructions of the local and survey-scale web
<!-- key: reconstructions-of-the-local-and-survey-scale -->

| Data set | What | Facts | Citation | Flag |
|---|---|---|---|---|
| DESI EDR cosmic-web environment catalogue | per-object void/sheet/filament/knot probabilities for BGS, LRG, ELG, QSO | 20 EDR rosettes, ~175 deg², 100 realisations per tracer and zone; "first public cosmic-web environment catalog built on any DESI data release" | Zapata-Zuluaga et al. 2026, arXiv:2604.01456 | [src: abstract] |
| DESI DR1 T-web environments | colour versus web class for BGS (0.15 ≤ z < 0.55), LRG (0.6 ≤ z < 0.9), ELG (0.6 ≤ z < 1.6) | T-web on a 256³ grid in an 800 Mpc cube | Ullah et al. 2026, arXiv:2604.02463 | [src: abstract] |
| CF4++ZOA V-web catalogue | 37 voids (effective radii 13–38 h⁻¹Mpc) and 42 knots (10⁴ to 3.3 × 10⁵ h⁻³Mpc³) to z = 0.1; 3041 CF4++ galaxies in the voids and 7346 in the knots | Cosmicflows-4 with zone-of-avoidance extension, HMC ensemble | Hollinger & Courtois 2026, arXiv:2606.13538 | [src]; [src: Sect. 4] for galaxy counts |
| Cosmicflows-2 Wiener-filter velocity field | local flow dominated by the Shapley attractor and a single "dipole repeller" at 16,000 ± 4,500 km/s; Local Group moves at 631 ± 20 km/s with respect to the CMB | Cosmicflows-2 | Hoffman et al. 2017, arXiv:1702.02483 | [src: abstract] |
| Laniakea | supercluster boundary from diverging flows | Cosmicflows | arXiv:1409.0880 | [src] |
| BORG reconstructions of SDSS | probabilistic web maps | SDSS main sample | arXiv:1512.02242 | [src] |
| miniJPAS + DESI | local filaments around galaxies, 0.2 < z < 0.8 | spectro-photometric | arXiv:2506.15345 | [src: abstract] |
| COSMOS2020 | MMF on galaxy density maps, 0.4 < z < 4 | photometric, mass-complete | arXiv:2610.07710 | [src: abstract] |

The peculiar-velocity data behind Cosmicflows and the bulk-flow results are in
`cosmo-peculiar-velocities`; the constrained resimulations built on them are
in `cosmo-simulations-mocks`.

## 3. Lyα-forest maps used for the web
<!-- key: lyalpha-forest-maps-used-for-the-web -->

CLAMATO (Keck/LRIS, COSMOS, 2.05 < z < 2.55; arXiv:2109.09660, abstract),
LATIS (Magellan/IMACS, maps over 1.65 deg² at z = 2.2–2.8;
arXiv:2510.08815, abstract) and the eBOSS Stripe 82 wide-field map are documented, with their
sample sizes and resolutions, in `cosmo-lyman-alpha` (surveys-and-data §5).
For the web as an object, two points matter here. First, deep-field maps at ≲
5 h⁻¹Mpc sightline spacing are the regime in which the tidal-tensor
eigenvectors are recovered well enough for web classification and alignment
studies (arXiv:1612.00067, **forecast**) [src]. Second, constrained
reconstruction of initial conditions from the forest (TARDIS) classifies the z
~ 2.5 web and follows galaxies to their z = 0 environments (arXiv:1903.09049)
[src]; the CLAMATO DR2 release provides such a forward-modelled dark-matter
field ("the first 3D maps of the detailed cosmic web at 2.05 < z < 2.55",
title of arXiv:2109.09660) [src: title].

## 4. Gas in filaments: X-ray, SZ, radio and FRB data
<!-- key: gas-in-filaments-x-ray-sz-radio-and-frb-data -->

| Data set | Role | Facts | Citation | Flag |
|---|---|---|---|---|
| Planck Compton-y and CMB-lensing maps | first pair and filament tSZ stacks | used for 260,000 LRG pairs, 1,002,334 CMASS pairs, 24,544 filaments | arXiv:1709.05024, arXiv:1709.10378, arXiv:1911.09706 | [src: abstract of each] |
| ACT DR6 + Planck y; MUSTANG-2 | oriented supercluster stacks; resolved A399–A401 bridge at 1.65′ | ~3 times the significance of the proof of concept for extended gas | arXiv:2409.04535, arXiv:2107.04611 | [src: abstract of each] |
| ROSAT all-sky survey | first stacked X-ray filament detection | 15,165 filaments | arXiv:2011.05343 | [src: abstract] |
| eROSITA eFEDS | stacked X-ray in a small deep field | 463 filaments | arXiv:2206.00084 | [src: abstract] |
| eROSITA eRASS:4 (scans of 12 Dec 2019 to 19 Dec 2021; eSASS pipeline 020; telescope modules 1–4 and 6 only, avoiding the light leak in 5 and 7) | stacked X-ray of WHIM | ~3200 deg² SDSS overlap reduced to 2275 deg² after foreground cuts | arXiv:2406.00105 | [src: Sect. 2] |
| SDSS LOWZ+CMASS DisPerSE filament catalogue (Malavasi et al.) | filament positions for most stacks | 63,391 filaments at 3σ persistence | as used in arXiv:2406.00105 | [sec: Zhang et al. 2024, Sect. 2] |
| LOFAR; LoTSS DR2 | radio ridges; rotation measures | 140 MHz for the A399–A401 ridge (arXiv:1906.07584); 144 MHz for the LoTSS DR2 rotation measures (arXiv:2202.04607) | arXiv:1906.07584, arXiv:2202.04607 | [src: abstract of each] |
| Dedicated eROSITA + ASKAP/EMU + DECam field | A3391/95 | 15 deg² | arXiv:2012.08491 | [src: abstract] |

**FRB samples.** The first FRB baryon census used published arcsecond
localisations plus four new hosts at z = 0.118, 0.291, 0.378 and 0.522
(arXiv:2005.13161) [src: abstract]. The void stack uses 3455 CHIME/FRB
sightlines on 1288 SDSS BOSS voids (arXiv:2605.01994) [src: abstract]. FRB
instruments and the DM–redshift relation as a cosmological probe are in
`cosmo-multimessenger`.

The 2024 partition adds DSA-110 bursts: the array (1.28–1.53 GHz at Owens
Valley, 48 core and 15 outrigger antennas in its commissioning period from
January 2022 to March 2024) discovered 60 new FRBs, 39 with spectroscopic host
redshifts, appended to 30 previously localised sources (arXiv:2409.16952)
[src: main text, the paragraph that introduces DSA-110 and the one after it;
the HTML rendering has no headings].

**UV and X-ray absorption.** HST/COS spectra of ten quasar sightlines near
cluster pairs at z < 1 measure broad Lyα and O VI incidence in putative
inter-cluster filaments (arXiv:2610.11203) [src: abstract]; XMM-Newton grating spectra
of 1ES 1553+113 are the data behind the O VII claim and its re-analysis
(arXiv:1806.08395, arXiv:2305.01587) [src].

## 5. Protocluster samples
<!-- key: protocluster-samples -->

| Survey | Selection | Scale | Citation | Flag |
|---|---|---|---|---|
| HSC-SSP (GOLDRUSH) | g-dropout overdensities > 4σ at z ~ 3.8; U-dropouts at z ~ 3 | 121 deg², 179 candidates (S16A) | arXiv:1708.09421; arXiv:2610.01816 | [src: abstract of each] |
| ODIN + DESI | narrowband Lyα emitters at z ≈ 2.4, 3.1 with DESI spectroscopy | ≈ 14 deg² (COSMOS, XMM-LSS), six confirmed | arXiv:2603.09739 | [src: abstract] |
| VUDS | spectroscopic Voronoi density at z ~ 2.45 | COSMOS | arXiv:1806.06073 | [src: abstract] |
| MUSE deep fields (MUDF, MXDF) | LAE overdensities and diffuse Lyα, 3 ≲ z ≲ 5 | 41 overdensities | arXiv:2609.20938 | [src: abstract] |
| JWST protocluster candidates at 5 < z < 9 | literature compilation | — | arXiv:2605.28930 | [src] |

## 6. Simulations used as references
<!-- key: simulations-used-as-references -->

| Simulation | Used here for | Citation | Flag |
|---|---|---|---|
| Gadget-2 dark-matter-only simulation, 200 h⁻¹Mpc box with 512³ particles, gridded on 100³ cells of (2 h⁻¹Mpc)³ (finder comparison) | mass and volume fractions of twelve finders | arXiv:1705.03021 | [src: Sect. 3] for the box; [src: Sect. 5.3] for the grid |
| P-Millennium | halo spin flip with NEXUS | arXiv:1805.00033 | [src] |
| Horizon 4π; Horizon-AGN | halo spin flip; galaxy colour gradients and spin transition | arXiv:1201.5794; arXiv:1710.02676; arXiv:1909.12371 | [src] |
| IllustrisTNG (TNG50, TNG300), Illustris, Magneticum, MillenniumTNG | filament populations, gas phases, galaxy bias, low-mass filament galaxies, filament evolution | arXiv:2003.09697; arXiv:2010.15139; arXiv:2608.25060; arXiv:2605.23457; arXiv:2309.08659 | [src] |
| SIMBA | star formation vs filament distance, z = 3–0 | arXiv:2509.18077 | [src] |
| MDPL2 (1 h⁻¹Gpc)³ | gigaparsec DisPerSE catalogue, connectivity | arXiv:2607.14785 | [src] |
| FLAMINGO | voids with photometric redshifts (J-PAS mocks) | arXiv:2607.26932 | [src] |


## 7. Planned and next
<!-- key: planned-and-next -->

- eROSITA: stacking of all-sky survey scans beyond eRASS:4 is the route to
  WHIM detections on more filaments; the eRASS:4 analysis already reaches 9σ
  total (arXiv:2406.00105) [src].
- FRB surveys named as expanding the void-baryon measurement by orders of
  magnitude: CHORD, DSA, SKA, with galaxy surveys DESI, LSST, Euclid, PFS,
  SPHEREx, Roman (arXiv:2605.01994) [src].
- Subaru PFS: > 10,000 coeval galaxies would constrain galaxy–web alignments
  at z ~ 2.5 to Δ⟨cos θ⟩ ~ 0.03 (arXiv:1612.00067, **forecast**) [src: abstract].
- J-PAS: watershed voids on a quasi-potential survive J-PAS-like photometric
  errors (arXiv:2607.26932) [src].
- Facility schedules are in `cosmo-surveys-facilities`.

## 8. Public data and access
<!-- key: public-data-and-access -->

| Product | Access as stated in the paper read | Citation | Flag |
|---|---|---|---|
| CAVITY DR2 | 200 IFS cubes and master catalogues at cavity.caha.es/data/dr2/ | arXiv:2609.24726 | [src: abstract] |
| DESI EDR web-environment catalogue | "all data products and the open-source pipeline are publicly available" | arXiv:2604.01456 | [src] |
| SDSS Bisous filaments | "a public catalogue of filaments" | arXiv:1308.2533 | [src] |
| Laniakea | accompanying movie at irfu.cea.fr/laniakea | arXiv:1409.0880 | [src] |
| Gigaparsec MDPL2 filament catalogue | produced; release not stated in the abstract | arXiv:2607.14785 | [src] |
| eRASS:4 source catalogue used for masking | proprietary at the time of the analysis | arXiv:2406.00105 | [src: Sect. 2.1] |

Order of the sections above follows the brief: past catalogues (SDSS, GAMA)
first, current releases (DESI EDR and DR1, eRASS:4, CAVITY DR2) next, and
planned programmes in §7. Instrument and release-date facts beyond those
quoted here belong to `cosmo-surveys-facilities`.

## Not verified
<!-- key: not-verified -->

- The arXiv identifier of the Malavasi et al. SDSS LOWZ+CMASS DisPerSE
  filament catalogue was not looked up; it enters only as cited by
  arXiv:2406.00105.
- No DESI DR1 or DR2 filament catalogue paper beyond the EDR environment
  catalogue and the DR1 T-web quenching study was found.
- Public URLs of the filament catalogues (SDSS Bisous, GAMA, DESI EDR) were
  not opened.
