# Observational-cosmology skill suite — implementation plan

Design: `design.md`. Agent instructions: `agent-brief.md`. Live status: the
claude-mem work-state list `cosmo-skill-suite`.

## Steps

| # | Step | Gate |
|---|---|---|
| 0 | Design, agent brief, `verify_sources.py` (tested on a fixture with good, wrong, orphan and uncited rows) | checker flags all four defect kinds |
| 1 | RED baseline: `tests/questions.md` answered from memory, no tools, no skill → `tests/baseline.md` | failures documented |
| 2 | Wave N: one background research agent per domain, each following `agent-brief.md` | agent reports checker exit 0 |
| 3 | Coordinator gate per domain: rerun the checker; read `SKILL.md`; spot-check five numbers of `results.md` against `get_abstract` | all pass, or the file is corrected |
| 4 | GREEN: the baseline questions answered from the skill files only → `tests/green-waveN.md` | every answer correct and located |
| 5 | Hub: router table in `observational-cosmology/SKILL.md`, `references/suite-conventions.md`; `install.sh` lines; run `install.sh` | skills listed in a fresh session |
| 6 | arXiv topic watch per domain | `list_watches` shows them |
| 7 | Next wave: back to step 2 | |

Commits are left to the author.

## Domain scopes

### Wave 1

| Skill | Scope |
|---|---|
| `cosmo-cmb` | Primary anisotropies TT/TE/EE and what they constrain (θ*, ωb, ωc, ns, As e^-2τ, τ); CMB lensing reconstruction and its power spectrum; polarisation B-modes at the level of status (detail belongs to `cosmo-inflation-primordial`); foregrounds and component separation; beams, calibration, transfer functions; likelihoods (Planck PR3/PR4: Plik, CamSpec, HiLLiPoP/LoLLiPoP, SRoll2; ACT DR4/DR6; SPT-3G 2018, D1 and later); the combined ground+space constraints; the lensing-amplitude A_L anomaly and its fate; τ and its tension with DESI-era fits; N_eff and Σmν from CMB alone; facilities: Planck, ACT, SPT-3G, BICEP/Keck, Simons Observatory, CMB-S4 cancellation, LiteBIRD; secondary anisotropies only as pointers (tSZ, kSZ, ISW belong to cross-correlation and cluster skills). |
| `cosmo-galaxy-clustering` | Spectroscopic galaxy and quasar clustering: BAO (isotropic and anisotropic, reconstruction, D_M/r_d, D_H/r_d, D_V/r_d), RSD and fσ8, the Alcock–Paczynski effect, full-shape / EFTofLSS and ShapeFit analyses, primordial non-Gaussianity from scale-dependent bias (status only), two-point estimators (Landy–Szalay, FKP/Yamamoto multipoles, window function, wide-angle and integral-constraint corrections), covariance from mocks vs analytic, blinding, imaging and spectroscopic systematics, fibre collisions and PIP weights, HOD and bias models at the level needed for analysis. Surveys: 2dFGRS, 6dFGS, WiggleZ, SDSS/BOSS/eBOSS, DESI (EDR, DR1, DR2, any DR3 material), Euclid spectroscopic, PFS, 4MOST, Roman, SPHEREx. The DESI DR1 and DR2 BAO and full-shape results and their cosmological interpretation (the dark-energy interpretation itself belongs to `cosmo-dark-energy-modified-gravity`). |
| `cosmo-lyman-alpha` | The Lyα forest as a cosmological probe: flux transmission, the fluctuating Gunn–Peterson approximation, continuum fitting and the delta field (picca), the 1D flux power spectrum P1D (FFT and QMLE estimators, resolution, noise, side-band metals, DLA/BAL masking), the 3D correlations and Lyα BAO (auto and quasar cross-correlation, distortion matrix, metals, HCD modelling, Vega), Lyα full shape and AP, the 3D power spectrum P3D and P× estimators, Lyα tomography (CLAMATO, LATIS, PFS, DESI-based maps) and Lyα–void cross-correlation, IGM thermal state (T0, γ, pressure smoothing, UV background, reionisation relics), hydrodynamical simulations and emulators (Nyx, Gadget/MP-Gadget, Sherwood, ACCEL², LaCE, PRIYA, ForestFlow), cosmological constraints from P1D (ns running, Σmν, warm and fuzzy dark matter — the particle-physics interpretation is shared with `cosmo-neutrinos-dark-matter`), high-resolution samples (HIRES, UVES, XQ-100, KODIAQ, SQUAD) vs survey samples (BOSS, eBOSS, DESI EDR/DR1/DR2), future (DESI-II, WEAVE-QSO, 4MOST, PFS, MUST, Spec-S5). |
| `cosmo-weak-lensing` | Cosmic shear and galaxy–galaxy lensing: shear estimators and calibration (metacalibration, metadetection, image simulations), PSF modelling, blending, photometric-redshift calibration (SOM, clustering redshifts, direct calibration, shear ratio), intrinsic alignments (NLA, TATT, halo models), baryonic feedback and its mitigation (scale cuts, HMCode, baryonification, kSZ/X-ray-informed priors), 3×2pt and 6×2pt analyses, statistics (ξ±, COSEBIs, band powers, pseudo-Cℓ), covariance, blinding, S8 and its history, the resolution or persistence of the S8 tension. Surveys: CFHTLenS, KiDS (KiDS-1000, Legacy), DES (Y1, Y3, Y6), HSC (Y1, Y3), DECADE, UNIONS, Euclid (Q1, DR1 status), Rubin LSST (status), Roman. Higher-order lensing statistics as pointers to `cosmo-beyond-two-point`; CMB lensing cross-correlation as pointers to `cosmo-cmb-lss-cross-correlations`. |
| `cosmo-supernovae` | Type Ia supernova cosmology: standardisation (stretch, colour, host-mass step, SALT2/SALT3, BayeSN, dust-based models), photometric calibration and cross-survey calibration (Fragilistic, Dovekie and successors), selection bias and BBC/BEAMS, photometric classification, hierarchical Bayesian frameworks (UNITY, Steve, BAHAMAS), host-galaxy and environment dependence, intrinsic scatter models, the Hubble diagram and its covariance, low-redshift anchor samples and their role in the dark-energy result, peculiar-velocity corrections of SN redshifts (the use of SNe as velocity tracers belongs to `cosmo-peculiar-velocities`). Compilations: JLA, Pantheon, Pantheon+, Union3/3.1, DES-SN5YR and its 2025–2026 recalibration, ZTF SN Ia DR2 and DR2.5, and the status of Rubin, Roman, and any Union or DES update. Also briefly: SNe II, strongly lensed SNe, and SN siblings as cross-checks. |
| `cosmo-distance-ladder-h0` | The Hubble constant: the local distance ladder (geometric anchors — Gaia parallaxes, LMC DEBs, NGC 4258 maser; Cepheids, TRGB, JAGB, Miras, SBF; SN Ia calibration), SH0ES and CCHP results including JWST, crowding and metallicity debates, the Local Distance Network; ladder-independent routes (megamasers, time-delay cosmography TDCOSMO/H0LiCOW, standard sirens at summary level, Tully–Fisher and SBF Hubble-flow calibrations, cosmic chronometers); the inverse distance ladder (BAO + r_d, BBN + BAO) and the CMB value; how the tension significance is computed and what it depends on; local-void and peculiar-velocity explanations; the status of theoretical resolutions (early dark energy, r_d-modifying models) at summary level with pointers to `cosmo-tensions-anomalies` and `cosmo-dark-energy-modified-gravity`. |

### Wave 2

| Skill | Scope |
|---|---|
| `cosmo-peculiar-velocities` | Direct peculiar velocities: distance indicators (TF, FP, SN Ia, SBF), log-distance ratio, estimators (velocity two-point, momentum power spectrum, maximum likelihood / field-level, density–velocity comparison, reconstruction), bulk flow and its estimators, fσ8 at z<0.1, tests of gravity and scale-dependent growth, velocity–density cross-correlation, zero-point and Malmquist systematics, non-linear damping models; surveys (Cosmicflows-4, 6dFGSv, SDSS-PV, 2MTF, WALLABY, DESI PV DR1 and later, ZTF SN Ia, Rubin, 4MOST Hemisphere Survey); forecasts (labelled). **Builds on the hub's existing `references/pv-surveys.md` and `references/fsigma8-pv-compilation.md`: read them first, do not duplicate them, point to them, and add what they lack.** The machine-readable compilation stays in `<packages>/growth_review`. |
| `cosmo-clusters` | Galaxy-cluster cosmology: detection (X-ray, SZ, optical richness), mass calibration (weak lensing, hydrostatic bias, CMB lensing), the halo mass function and its calibration, selection functions, cluster counts and clustering, gas-mass fractions, results from eROSITA eRASS1, SPT, ACT, Planck SZ, DES redMaPPer (and the Y1 projection-effect lesson), HSC, KiDS, Euclid Q1; the cluster S8 history; splashback and the cluster profile as probes. |
| `cosmo-cmb-lss-cross-correlations` | CMB lensing × galaxies and quasars (unWISE, DESI LRG, DESI Legacy, Quaia), tomographic growth constraints, kSZ (pairwise, projected-field, velocity-reconstruction stacking; ACT × DESI results and the baryon-feedback implication), tSZ × LSS, ISW, CIB, moving-lens and other secondary effects at status level; the role of cross-correlations in systematics control. |
| `cosmo-beyond-two-point` | Bispectrum and trispectrum, cosmic voids (void finders, void size function, void–galaxy cross-correlation and AP/RSD, Lyα–void cross-correlation), density-split statistics, k-nearest-neighbour, wavelet scattering, Minkowski functionals, marked statistics, peak counts and one-point PDFs in lensing, field-level inference (BORG and successors, differentiable forward models), simulation-based inference with learned summaries (SimBIG, and DESI/BOSS applications); validation challenges (Beyond-2pt challenge); what has delivered robust constraints on data vs on mocks only. |
| `cosmo-dark-energy-modified-gravity` | Dark-energy phenomenology (w, w0wa/CPL, binned and non-parametric reconstructions, thawing/quintessence, phantom crossing), the DESI DR1/DR2 evidence for dynamical dark energy and every published critique (SN sample dependence, low-z anchor, priors, parameterisation, physical vs effective models), modified-gravity parameterisations (μ, Σ, η; growth index γ; EFT of dark energy α-basis; Horndeski after GW170817), screening and its tests, the E_G statistic, results from DES, KiDS, DESI full-shape, Planck/ACT; model-comparison practice. |
| `cosmo-neutrinos-dark-matter` | Cosmological neutrino mass (physics of the signal, current bounds by dataset and model, the tension with oscillation lower limits, "negative neutrino mass", dependence on τ and on dark-energy model), N_eff and light relics, BBN consistency; dark-matter properties from structure: warm, fuzzy/ultralight, interacting and self-interacting dark matter, limits from Lyα forest, Milky-Way satellites, strong lensing, stellar streams, UV luminosity functions; decaying dark matter and dark radiation at status level. |

### Wave 3

| Skill | Scope |
|---|---|
| `cosmo-inflation-primordial` | Primordial power spectrum (ns, running, features), tensor-to-scalar ratio from BICEP/Keck, Planck, SPT, SO and LiteBIRD prospects, the ACT DR6 ns shift and its consequence for inflation models, primordial non-Gaussianity (local, equilateral, orthogonal; CMB bispectrum limits; LSS scale-dependent bias limits from eBOSS and DESI; SPHEREx forecast), isocurvature, spatial curvature, primordial features searches, cosmic birefringence. |
| `cosmo-tensions-anomalies` | H0 and S8 tensions as a cross-probe synthesis (pointers to the dedicated skills for detail), tension metrics (parameter-difference, suspiciousness, evidence ratio, goodness-of-fit loss) and their pitfalls, the cosmic dipole (radio and quasar number counts, SN dipole, bulk flows), large-angle CMB anomalies, A_L, the DESI–CMB–SN three-way inconsistency within ΛCDM, the τ question, JWST high-redshift galaxy abundance, cosmic-birefringence hint; for each: current significance, datasets, and the mundane explanations on the table. |
| `cosmo-surveys-facilities` | A facility-by-facility reference: instrument, site, aperture, field of view, multiplex or sensitivity, sky area, wavelength coverage, target classes and densities, survey strategy, data-release history with dates and public access points, status today, next milestone. Spectroscopic (SDSS-I–V, DESI and DESI-II, PFS, 4MOST, WEAVE, MOONS, Euclid NISP, Roman, SPHEREx, MUST, Spec-S5, WST, MSE), imaging (DES, KiDS, HSC, DESI Legacy Surveys, UNIONS, Rubin LSST, Euclid VIS, Roman, CSST), CMB (Planck, ACT, SPT, BICEP/Keck, SO, LiteBIRD, CMB-S4 fate), time domain (ZTF, ATLAS, YSE, Rubin), radio (CHIME, MeerKAT, ASKAP, SKA, HIRAX, DSA-2000), X-ray (eROSITA), GW (LVK, ET, CE, LISA). |
| `cosmo-statistics-inference` | Likelihoods and when the Gaussian approximation fails, covariance estimation (mocks, jackknife, analytic; Hartlap and Percival corrections, Sellentin–Heavens), data compression, blinding strategies, samplers (MCMC, nested sampling, HMC/NUTS) and convergence, priors and projection effects, frequentist profile likelihoods vs Bayesian posteriors, model comparison (evidence, information criteria, Δχ² to σ conversion), tension metrics, Fisher forecasts and their limits, emulators and their error budgets, simulation-based inference and its validation (coverage tests), combining probes and correlated datasets, look-elsewhere effect. Each with the reference paper and a concrete cosmology example. |
| `cosmo-simulations-mocks` | N-body codes and their agreement (Gadget, AbacusSummit, Uchuu, Quijote, Euclid Flagship), hydrodynamical suites (IllustrisTNG, EAGLE, FLAMINGO, MillenniumTNG, CAMELS, Nyx, Sherwood, ACCEL²), approximate methods and fast mocks (COLA, FastPM, EZmocks, lognormal, GLASS), galaxy–halo connection (HOD, SHAM, assembly bias), light-cones and survey realism, constrained simulations and reconstructions of the local Universe, emulators (Aemulus, EuclidEmulator, CosmicEmu, BACCO), neutrino and modified-gravity simulations, convergence and accuracy requirements for Stage-IV surveys, baryonic feedback calibration. |

### Wave 4

| Skill | Scope |
|---|---|
| `cosmo-reionization-21cm` | Reionisation history (τ, Gunn–Peterson troughs, Lyα damping wings, LAE fractions, kSZ), the 21 cm global signal (EDGES and the SARAS non-confirmation) and power-spectrum limits (HERA, LOFAR, MWA), post-reionisation HI intensity mapping (CHIME detection, MeerKAT, Tianlai, HIRAX, SKA), line-intensity mapping (CO, [CII], Lyα; COMAP, SPHEREx), JWST constraints on early galaxies as they bear on cosmology, foreground mitigation. |
| `cosmo-multimessenger` | Standard sirens (bright: GW170817; dark: catalogue and spectral methods; LVK O1–O4 H0 constraints), systematics (selection, population, galaxy-catalogue completeness, peculiar velocity of the host), third-generation and LISA forecasts (labelled); fast radio bursts as baryon and H0 probes (dispersion-measure–redshift relation); strong-lensing time delays as a pointer to `cosmo-distance-ladder-h0`; lensed transients; GW × LSS cross-correlation. |
| `cosmo-software-ecosystem` | The codes an analyst meets: Boltzmann solvers (CAMB, CLASS, and their modified-gravity forks EFTCAMB, hi_class, MGCAMB), wrappers and theory façades (cosmoprimo, pyccl, astropy.cosmology), samplers and frameworks (Cobaya, MontePython, CosmoSIS, desilike, emcee, dynesty, PolyChord, nautilus, NumPyro/BlackJAX), perturbation-theory codes (velocileptors, CLASS-PT, PyBird, FOLPS, FAST-PT), estimators (pypower, pycorr, nbodykit, TreeCorr, NaMaster, Corrfunc, Triumvirate), Lyα (picca, Vega, LaCE, lym1d), lensing (healpy, lenstools), field-level and differentiable (flip, BORG, pmwd, JaxPM, jax-cosmo, DISCO-DJ), emulators (CosmoPower, capse), mocks (see sibling). For each: what it computes, reference paper, repository, conventions and units that trap users, maintenance status. **Use the context7 MCP tools for current API facts in addition to the reference papers.** |
| `cosmo-theory-foundations` | The theory an observer must hold exactly: FLRW distances and their conventions, the parameter basis and derived parameters, r_d and r_s definitions and fitting formulae, linear growth and its approximations, transfer functions, σ8 and its definition, Fourier and multipole conventions, redshift-space distortions (Kaiser, fingers of God, streaming models), perturbation theory and EFTofLSS (counterterms, IR resummation, bias expansions), the halo model, galaxy bias (linear, non-local, assembly), Limber approximation and angular power spectra, relativistic and wide-angle effects, massive-neutrino treatment, unit and h conventions. Each formula with the paper that defines the convention. |

## Final step — package as `<repo>/` (requested 2026-10-09)

**Done on 2026-10-12**; see the last entry of `tests/gate-log.md`. The steps
below are kept as the record of what was asked and planned.

Author's instruction: "At the end, reorganize this effort in a claude code
skill package in here: <repo>. put all the cosmo
skills organized in here and link that to claude config so that you can use it
all the time if needed."

To do once the last wave is gated, not before (agents write to the current
paths until then):

1. Create `<repo>/` as its own git repository, laid out as a
   Claude Code skill package: `skills/<name>/` for the hub
   `observational-cosmology` and every `cosmo-*` skill, the checker under
   `scripts/`, the design, plan, agent brief and test logs under `docs/`, a
   `README.md`, and a plugin manifest so it can also be installed as a plugin.
2. Move the skills out of `claude_config/claude/skills/` (move, not copy: one
   home for each skill).
3. Link it into the Claude configuration through `claude_config/install.sh`,
   so both accounts (`~/.claude`, `the second Claude home`) load the skills in every
   session under their present names; other skills refer to
   `observational-cosmology` by name and must keep working.
4. Update every absolute path that points to the old location: the checker
   path in `agent-brief.md` and `suite-conventions.md`, the design and plan
   paths in the hub `SKILL.md`, the memory note, `claude_config/README.md`.
5. Verify in a fresh session that all skills are listed, rerun the checker on
   every skill from the new location, and leave the commit to the author.
