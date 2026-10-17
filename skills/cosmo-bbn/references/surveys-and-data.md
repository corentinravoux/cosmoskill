# BBN — observations, experiments and data

Scope: the observational programmes that measure primordial D/H, Y_P, ³He
and ⁷Li; the laboratory facilities that measure the nuclear rates and the
neutron lifetime; public codes and rate compilations; what is expected next.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Table n]`
body read; `[sec]` named secondary source; `[der]` derived here.

## 1. Deuterium: quasar absorption-line programmes
<!-- key: deuterium-quasar-absorption-line-programmes -->

| Programme | Instrument | What it delivered | Citation | Flag |
|---|---|---|---|---|
| Precision sample (Cooke, Pettini, Steidel and collaborators) | Keck/HIRES, VLT/UVES | seven systems analysed homogeneously, one percent (D/H)_P | arXiv:1710.11129 | [src] |
| Ioffe / Balashev group with Murphy, Ledoux, Noterdaeme | VLT/UVES, Keck/HIRES | J1332+0052 sub-DLA at z = 3.42; eight-system mean | arXiv:2401.12797 | [src] |
| ESPRESSO fundamental-physics programme (Guarneri, Pasquini, Molaro, Murphy and others) | VLT/ESPRESSO | PKS1937−101 at z ≈ 3.572 | arXiv:2402.05586 | [src] |
| Swinburne / Webb group (Zavarygin, Webb, Riemer-Sørensen, Dumont) | Keck/HIRES | Q1009+2956 re-analysis; 13-system compilation | arXiv:1706.09512, arXiv:1801.04704 | [src] |

The method dates from Adams (1976), who proposed measuring D and H Lyman
lines in high-redshift clouds against a background source; the first
near-pristine systems needed Keck-class telescopes more than two decades
later (Cooke 2024 review, arXiv:2409.06015) [sec: Cooke 2024, Sect. 3.1;
the 1976 paper was not read]. The fitting codes in use are ALIS
(Cooke et al.) and VPFIT (Webb group) [src: arXiv:1710.11129, Sect. III;
arXiv:1910.02913].

Each new system weighs heavily because so few exist: only seven absorbers
had been "consistently measured" by 2024 (arXiv:2409.06015)
[src: Sect. 3.1], and PRIMAT's authors note that D/H "rests on" the Cooke
et al. measurements (arXiv:2011.11320) [src: Discussion]. Thousands of DLAs
are known from large surveys, but most background quasars are too faint for
precision follow-up with current telescopes (arXiv:2011.11320)
[src: Discussion].

## 2. Helium-4: metal-poor H II region programmes
<!-- key: helium-4-metal-poor-h-ii-region-programmes -->

| Programme | Instrument | Sample | Citation | Flag |
|---|---|---|---|---|
| LBT Y_p Project (Skillman, Pogge, Aver, Olive and collaborators); papers I–V in January 2026 | LBT MODS optical + LUCI near-IR (He I 10830) simultaneously | 54 metal-poor H II regions observed uniformly; 41 qualifying; 15 low-metallicity high-S/N | Skillman et al. 2026, arXiv:2601.22232; Weller et al. 2026, arXiv:2601.22237; Aver et al. 2026, arXiv:2601.22238; Yeh et al. 2026, arXiv:2601.22239 | [src] for IV and V; titles only for I and III |
| EMPRESS (Ouchi and collaborators) | Subaru near-IR + existing optical | extremely metal-poor galaxies (0.01–0.1 Z_⊙); 29 galaxies incl. 14 EMPGs in XV | Matsumoto et al. 2022, arXiv:2203.09617; Yanagisawa et al. 2025, arXiv:2506.24050 | [src] |
| Izotov–Thuan–Guseva (HeBCD) | optical + near-IR | 45 H II regions, 28 kept | arXiv:1408.6953 | [src] |
| PHLEK (Hsyu, Cooke, Prochaska, Bolte) | Keck NIRSPEC, NIRES | 16 galaxies, 12 + log(O/H) = 7.13–8.00 | arXiv:2005.12290 | [src] |
| Ioffe group (Kurichin, Kislitsyn, Ivanchik) | SDSS spectra | 100 H II regions | arXiv:2101.09127; metallicity method arXiv:2201.06431 | [src]; [src: title only for 2201.06431] |
| Peimbert group (Valerdi, Peimbert, Peimbert) | VLT/FORS1 | 7 H II regions in 3 galaxies; NGC 346 in the SMC | arXiv:2105.12260; arXiv:1904.01594 | [src]; [src: title only for 1904.01594] |
| Intergalactic absorption (Cooke & Fumagalli) | quasar absorption | one near-pristine cloud at z = 1.724 | arXiv:1810.06561 | [src] |

The method: He and H recombination lines of metal-poor H II regions, with
a model for temperature, density, optical depth, underlying stellar
absorption and collisional excitation, followed either by a regression of y
on O/H to zero metallicity or, with enough very metal-poor targets, by a
weighted average (arXiv:2601.22238) [src]. Adding He I 10830 breaks the
density–temperature degeneracy and reduced the error on Y_P by over 50%
(Aver, Olive & Skillman 2015, arXiv:1503.08146) [src].

## 3. Helium-3
<!-- key: helium-3 -->

| Route | Instrument | What it gives | Citation | Flag |
|---|---|---|---|---|
| ³He⁺ 8.7 GHz hyperfine line in Galactic H II regions (Bania, Balser, Rood) | Green Bank Telescope | ³He/H across the disk; the "³He plateau" and its gradient | Balser & Bania 2018, arXiv:1810.09422; planetary nebulae, Bania & Balser 2021, arXiv:2012.11707 | [src]; [src: snippet for 2012.11707] |
| Metastable He I* absorption, ³He/⁴He isotope shift (Cooke and collaborators) | VLT/CRIRES+ | ³He/⁴He in Orion and two Milky Way sightlines; primordial ratio via chemical-evolution models | arXiv:2203.11256; arXiv:2605.00122 | [src] |
| Strategy for ³He I emission in metal-poor H II regions | extremely large telescopes | model-independent primordial ³He/⁴He | Cooke 2015, arXiv:1510.02801; arXiv:2605.00122 | [src] |

## 4. Lithium-7: halo stars and other environments
<!-- key: lithium-7-halo-stars-and-other-environments -->

| Route | Data | Citation | Flag |
|---|---|---|---|
| Li I 6708 Å in metal-poor halo dwarfs and subgiants (Spite plateau) | literature compilation of ~200 stars, 5500 < T_eff < 6700 K, −6 < [Fe/H] < −1.5 | Norris et al. 2023, arXiv:2303.11497 | [src] |
| Large surveys | GALAH, > 100 000 field stars, −3 ≲ [Fe/H] ≲ +0.5 | Gao et al. 2020, arXiv:2006.05173 | [src] |
| Globular clusters (stars of one birth composition in several evolutionary phases) | 15 years of work summarised | Korn 2021, arXiv:2111.00913 | [src] |
| Stars of an accreted system | ω Cen, 91 stars, VLT FLAMES-GIRAFFE | Monaco et al. 2010, arXiv:1008.1817 | [src] |
| Interstellar gas | SMC, ⁷Li I absorption | Howk et al. 2012, arXiv:1207.3081 | [src] |

## 5. Nuclear-physics laboratories
<!-- key: nuclear-physics-laboratories -->

| Facility | Type | BBN reactions | Result or status | Citation | Flag |
|---|---|---|---|---|---|
| LUNA, Gran Sasso | deep-underground accelerator | d(p,γ)³He at BBN energies | setup systematic error < 3%; rate published 2020 with order-3% error | Mossa et al. 2020a, arXiv:2005.00002; Mossa et al. 2020b, doi:10.1038/s41586-020-2878-4; Pisanti et al. 2021, arXiv:2011.11537 | [src]; [sec: arXiv:2011.11537 for the 3%] |
| Felsenkeller, Dresden | shallow-underground (45 m rock), 5 MV Pelletron | measurements for solar fusion and BBN ongoing; open user facility (ChETEC-INFRA) | Masha et al. 2025, arXiv:2510.05651 | [src] |
| n_TOF EAR2, CERN | spallation neutron time-of-flight | ⁷Be(n,α)⁴He, 10 meV–10 keV; ⁷Be(n,p)⁷Li, thermal to ~325 keV | both point to a minor role in the lithium problem | Barbagallo et al. 2016, arXiv:1606.09420; Damone et al. 2018, arXiv:1803.05701 | [src] |
| TUNL (Leonard et al.) | accelerator | d(d,p)t, d(d,n)³He at 110–650 keV | ~2% ± 1% scale error; both rates ~7% above NACRE | Leonard et al. 2006, arXiv:nucl-ex/0601035 | [src] |
| Trojan Horse Method groups (Catania and collaborators) | indirect, quasi-free breakup | d(d,p)t and others | d(d,p)t S_bare(0) = 56.7 ± 2.0 keV b, U_e = 13.2 ± 4.3 eV; THM rate set run in PRIMAT | Li et al. 2015, arXiv:1503.08672; Spartà et al. 2025, arXiv:2512.24358 | [src] |

The n_TOF ⁷Be(n,α) energy dependence shows that the cross sections used in
BBN codes were inadequate, but the reaction plays a minor role and leaves the
lithium problem unsolved (arXiv:1606.09420) [src]; ⁷Be(n,p) is higher than
evaluations at low energy but consistent with the time-reversed
⁷Li(p,n)⁷Be in the BBN window (arXiv:1803.05701) [src].

## 6. Neutron-lifetime experiments
<!-- key: neutron-lifetime-experiments -->

| Experiment | Method | Latest value read | Citation | Flag |
|---|---|---|---|---|
| UCNτ, LANSCE | bottle: magneto-gravitational trap, in situ detection; ~38 × 10⁶ UCN counted (2017–2018), three blinded analyses | τ_n = 877.75 ± 0.28 (stat) +0.22/−0.16 (syst) s | Gonzalez et al. 2021, arXiv:2106.10375 | [src] |
| PNPI gravitational trap and others (Serebrov group) | bottle, material walls | storage results of the last 20 years "in good agreement" | Serebrov et al. 2020, arXiv:2011.13272 | [src] |
| NIST beam (BL1) | beam: proton counting, ⁶Li fluence monitor | 2005 result updated to τ_n = 887.7 ± 1.2 (stat) ± 1.9 (syst) s after a five-fold better fluence-monitor efficiency | Yue et al. 2013, arXiv:1309.2623 | [src] |
| J-PARC pulsed cold beam | beam: electrons counted in a ³He-loaded TPC, distinct systematics | τ_n = 877.2 ± 1.7 (stat) +4.0/−3.6 (sys) s; consistent with bottles, 2.3σ from the proton-counting beam average | Fuwa et al. 2024, arXiv:2412.19519; first result Hirota et al. 2020, arXiv:2007.11293 | [src] |
| τSPECT, PSI | bottle: fully magnetic trap | simulation framework validated on data; no lifetime value yet | Auler et al. 2025, arXiv:2503.15239 | [src] |

Averages: beam 888.0(2.0) s against trapped UCN 879.4(6) s, an
8.6(2.1) s or ~4σ difference (Czarnecki, Marciano & Sirlin 2018,
arXiv:1802.01804) [src].

## 7. Codes and rate compilations
<!-- key: codes-and-rate-compilations -->

| Code | Public at | Status | Reference | Flag |
|---|---|---|---|---|
| PArthENoPE | parthenope.na.infn.it | v3.0 ("Revolutions", 2021) with revised d(p,γ), d(d,n), d(d,p) and new GUI; v2.0 replaced NAG with ODEPACK | arXiv:2103.05027; arXiv:1712.04378; arXiv:0705.0290 | [src] |
| PRIMAT | distributed with the paper (Mathematica) | 2018 release; 2021 upgrade with LUNA d(p,γ) and updated network | arXiv:1801.08023; arXiv:2011.11320 | [src] |
| AlterBBN | public C code | v2 without closed external libraries | arXiv:1106.1363; arXiv:1806.11095 | [src] |
| PRyMordial | GitHub | Python, optional Julia; extended by users to grand-unified and varying-constant scenarios | arXiv:2307.07061; Dreyer & Martins 2026, arXiv:2604.04870 | [src]; [src: snippet for 2604.04870] |
| LINX | public (JAX) | differentiable | arXiv:2408.14538 | [src] |
| bbn-sensitivity-atlas | GitHub | sensitivities to 14 parameters and 63 rates, with two rate compilations | arXiv:2603.22414 | [src] |
| BBN-simple | — | pedagogical code | Meador-Woodruff & Huterer 2024, arXiv:2412.07893 | [src: title only] |

Rate compilations and evaluations used by the codes are listed in
`physics-and-methods.md` §3.

### Abundance compilations in use
<!-- key: abundance-compilations-in-use -->

Three combinations of D/H and Y_P are common in cosmological analyses and
overlap strongly (Schöneberg 2024, arXiv:2401.15054) [src: Sect. 3,
Table 1]:

| Name | 10⁵ D/H | Y_P | Used by |
|---|---|---|---|
| "BAO+BBN papers" | 2.527 ± 0.030 (Cooke 2018) | 0.2449 ± 0.0040 (Aver 2015) | earlier BAO + BBN analyses |
| PDG August 2023 | 2.547 ± 0.029 | 0.2450 ± 0.0030 | PDG recommendation at the time |
| Yeh et al. 2022 | 2.550 ± 0.030 | 0.2448 ± 0.0033 (Aver 2021) | basis of the PDG Ω_b h² |

Since January 2026 the LBT Y_P = 0.2458 ± 0.0013 (arXiv:2601.22238) [src]
is available and is used by Yeh et al. 2026, Goldstein & Hill 2026,
Akharman et al. 2026 and Burns 2026 (arXiv:2601.22239, arXiv:2603.13226,
arXiv:2609.12065, arXiv:2603.22414) [src]. EMPRESS values are usually
treated as an alternative or an outlier (arXiv:2401.15054) [src: Sect. 4.3].

### CMB and BAO data combined with BBN
<!-- key: cmb-and-bao-data-combined-with-bbn -->

The joint analyses read here combine BBN with Planck (with or without
large-scale polarisation), ACT DR6, SPT-3G D1 and DESI DR2 BAO
(arXiv:2603.13226, arXiv:2609.12065, arXiv:2604.16600) [src]. The CMB data
themselves are described in `cosmo-cmb` and the BAO data in
`cosmo-galaxy-clustering`.

## 8. Next data
<!-- key: next-data -->

| What | Expected | Citation | Flag |
|---|---|---|---|
| D/H from 30 m-class telescopes | statistics improved by a factor ≳ 100; lower-redshift systems with less Lyα-forest blending (**forecast**) | Cooke 2024, arXiv:2409.06015 | [src: Sect. 4.2] |
| ELT HIRES D/H | 0.3% precision with a five-fold sample, if blue coverage suffices (**forecast**) | Pitrou et al. 2021, arXiv:2011.11320 | [src: Discussion] |
| Bright quasar searches for new D/H targets | QUBRICS identified 55 new z > 2.5 quasars | named in arXiv:2011.11320 | [sec: arXiv:2011.11320, Discussion] |
| CMB Stage-4 | Ω_b h² more precise than BBN; Y_P to ~2% (**forecast**) | arXiv:2409.06015 | [src: Sect. 4.2] |
| Simons Observatory | needed to shrink the ΔN_eff term of the Y_P theory error | Burns 2026, arXiv:2603.22414 | [src] |
| ³He in gamma-ray-burst sightlines and in metal-poor H II regions | needs extremely large telescopes (**forecast**) | arXiv:2409.06015 [src: Sect. 4.2]; arXiv:1510.02801 [src] | |
| Neutron lifetime | J-PARC electron-counting beam improving; τSPECT magnetic trap commissioning | arXiv:2412.19519; arXiv:2503.15239 | [src] |
| Nuclear rates | d(d,n)³He, d(d,p)t at 0.1–0.6 MeV; Felsenkeller BBN programme ongoing | arXiv:2604.16600; arXiv:2510.05651 | [src] |

## Not verified
<!-- key: not-verified -->

- The LUNA d(p,γ)³He result (doi:10.1038/s41586-020-2878-4) was confirmed by
  title on Crossref; its rate and Ω_b h² were not read.
- No n_TOF or LUNA programme pages were read for current schedules.
- Release dates of the LBT Y_p Project papers II (not found) and of future
  EMPRESS papers.
- Interstellar Li in other galaxies after the SMC: not searched.
