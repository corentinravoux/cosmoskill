# Level test — third L3 test of 2026-10-20, part 3c

Item C of `docs/plans/2026-10-20-plan.md` ("the domains not yet tested"). Four skills:
`cosmo-cosmic-web`, `cosmo-data-pipelines`, `cosmo-early-universe-exotica`,
`cosmo-galaxy-halo-connection`. Thirty-two questions, eight per skill, are in
`docs/tests/levels/l3-questions-3c.md`. Each was answered twice from the skill files only:
an **L2 run** (the skill's `SKILL.md` plus one reference file chosen from the file map) and
an **L3 run** (the same plus at most one dossier of `deep/`, chosen from the file map).
Model memory was not used to fill gaps. This run tests; no skill file was changed. Parts
3a and 3b ran earlier with the same method; other parts run at the same time and write
their own files.

Status: complete; four skills.

## Procedure

1. **Questions first.** Written from the four `subtopics.tsv` files, the file names of
   `deep/` and `references/`, and the one-line skill descriptions of the skill listing,
   before any `SKILL.md` body, reference file or dossier of the four skills was opened.
   Per skill, six questions fall one each on the six dossier subtopics and two on
   subtopics whose `files` column lists no dossier (controls).
2. **Preliminaries read.** The preamble and one skill block of `l3-questions-3a.md`, the
   procedure and the `cosmo-clusters` section of `run-2026-10-20-l3-third-a.md`, plan
   item C. Layer check: no `.cosmoskill/` in the working directory, its parents or the
   home directory; `COSMOSKILL_HOME` unset; layer `base` for every question.
3. **Isolation.** One session answered all questions: each file was read once, and each
   answer was then restricted to the passages of the files assigned to that run. As in
   the earlier runs this is weaker than a fresh session per run; every L2 grade names the
   passage it rests on.
4. **Grading.** (a) Y answers, P partly, N not; (b) locator: Y when the load-bearing
   statements carry paper + section, table or equation. **Tightened rule**: an L2 answer
   graded P counts as an L2 failure.
5. **Pass rule per skill.** The L3 run answers (Y) at least 5 of the 6 dossier questions
   with locators, including at least 3 that the L2 run failed (P or N); each L3 question
   loads at most one dossier. Controls should show no L3 gain; when one gains, the
   dossier that served it is named.
6. **Source checks.** One or two per skill (`fetch_paper.py --grep` or `--section`), of a
   statement an L3 answer used; numbered E1, E2, … within this part.

Abbreviations for reference files: `methods` = `references/physics-and-methods.md`,
`syst` = `references/systematics.md`, `open` = `references/open-questions.md`,
`results` = `references/results.md`, `surveys` = `references/surveys-and-data.md`. Every
run also loaded the skill's `SKILL.md`.

## cosmo-cosmic-web

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| Q1 | methods | `deep/web-classification.md` |
| Q2 | results | `deep/environment.md` |
| Q3 | syst | `deep/spin-alignments.md` |
| Q4 | methods | `deep/filament-gas.md` |
| Q5 | results | `deep/missing-baryons.md` |
| Q6 | results | `deep/protoclusters-superclusters.md` |
| Q7 (control) | results | `deep/web-classification.md` (closest: "T-web threshold and smoothing on galaxy fields") |
| Q8 (control) | methods | `deep/web-classification.md` (closest: "Agreement between finders on the same data", BORG posterior) |

### Answers

**Q1 — Finder families, free parameters, justification on a sparse galaxy sample.**
- L2 (methods §2, SKILL "What an expert holds in mind"): the eleven-row family table with
  input and class rule for T-web (λ_th = 0.2, 4πGρ̄ normalisation), V-web (λ_th = 0.44, H₀),
  MMF/NEXUS+ (seven scales 0.5–4 h⁻¹Mpc, thresholds from virialisation and mass change),
  DisPerSE (persistence in σ), Bisous (radius prior, visit-map 0.05, orientation > 0.7),
  ORIGAMI (shell-crossing, particles only) (arXiv:1705.03021, Sects. 4.1–4.7); conventions
  that differ (eigenvalue order, normalisation, partition against spines); fractions spread
  ~10–60% filament mass (Sect. 5.3); DisPerSE usable on sparse samples at ≥ 3σ
  (arXiv:1009.4014). How a paper should calibrate a threshold for its tracer density, what
  the free parameters of DisPerSE really are, and how finders agree on one galaxy survey
  are absent. **P.**
- L3: tracer choice at constant comoving density or ⟨D_z⟩ normalisation (arXiv:2309.08659,
  Sect. 3.1; arXiv:1710.02676, Sect. 3.2); galaxy against matter skeletons, ~60% of DM
  filaments recovered (arXiv:2307.05240, Sect. 5); FoG treatments before the finder
  (table, Step 2); DisPerSE's two parameters N1 (smoothing cycles) and N2 (persistence),
  N2 as a Poisson significance (arXiv:1009.4015, Eqs. 3–4); calibration of N2 by CPmax–halo
  purity and cluster completeness on mocks at the survey density, S 2σ adopted
  (arXiv:2309.08659, App. B Table 2), 3σ for miniJPAS+DESI (arXiv:2506.15345, Sect. 4.2);
  edge tagging and losses 22–52% (arXiv:2002.01486, Table 3); Bisous visit-map and
  directional-strength thresholds with run-to-run stability (arXiv:2103.06619, Sects. 3,
  4.3); DESI DR1 T-web set-up and its smoothing stability (arXiv:2604.02463, Sects. 3.1–3.2,
  App. A.1); finder agreement by information gain on BORG-SDSS (arXiv:1606.06758, Table 4).
  **Y.**

**Q2 — Web dependence of galaxy properties at fixed density and halo mass; GAMA, SDSS,
DESI conclusions.**
- L2 (results §3.2): the trends per survey — GAMA reddening toward filaments at fixed mass
  (arXiv:1710.02676), GAMA group ages by web class (arXiv:1612.08595), SDSS δ₈–α₅ with the
  iHOD halo-mass-only mock (arXiv:1801.04878), SDSS filament–field difference vanishing at
  fixed local density (arXiv:2409.09028), DESI DR1 red fractions per T-web class with stellar
  mass as primary driver (arXiv:2604.02463); summary "whether a trend remains at fixed halo
  mass and local density is the decisive test". The method — matching tolerances,
  reshuffling, density scale, group halo masses, the null model, the error estimators — is
  reduced to the SKILL checklist line. **P.**
- L3: distance and class definitions (d_fil, d_CP, d_skel; five-class scheme; overlap
  ranking) (arXiv:2109.14623, Sect. 3.1; arXiv:2509.09800, Sect. 2; arXiv:2409.09028,
  Sect. 3.5); tidal anisotropy α_R (arXiv:1706.09906, Eqs. 9–10); four control
  implementations — pairwise matching within 0.1 dex with Σ*₃, binned repeated draws,
  halo-mass weighting, reshuffling in density bins (arXiv:2409.09028, Sect. 4.1;
  arXiv:1710.02676, App. A, Sect. 6; arXiv:1612.08595, Sect. 4.2); the density scale as the
  deciding choice (1 Mpc against 5–8 Mpc; Step 3); group halo masses and the Monte Carlo
  of their calibration (arXiv:1612.08595, Sects. 4.1.1, 4.4.3); the iHOD null model with
  quantile splits (arXiv:1801.04878, Sects. 2.2, 4.1); error estimators per analysis and
  the warning that DESI's binomial errors ignore cosmic variance (Step 6 table). The
  dossier's reading of the GAMA reshuffling result is wrong at source (E2). **Y** (one
  load-bearing statement inverted).

**Q3 — Spin–filament alignment: spin proxy, finder, cosine statistic and null, flip mass,
disagreements.**
- L2 (syst §5, SKILL): mechanism (stellar against gas, 2D against 3D, finder, selection),
  MaNGA hint vanishing with Hα (arXiv:1902.09797), Siena Galaxy Atlas significance depending
  on the estimator (arXiv:2509.02062), flip mass varying with filament diameter
  (arXiv:1805.00033), mitigation and "randomised filament orientations" as validation; flip
  masses 5 × 10¹¹ h⁻¹M☉ and SAMI log M* = 10.4–10.9 (SKILL). How the spin axis is measured,
  the statistic and its null, and how the flip mass is defined are absent. **P.**
- L3: skeleton per analysis (table, Step 1); kinematic PA (FIT_KINEMATIC_PA), thin-disc 3D
  spin with intrinsic flatness p and the sign ambiguity (arXiv:2104.08275, Eqs. 1–4,
  Sect. 2.6), shape proxies, edge-on discs, halo J (arXiv:1805.00033, Eq. 12); assignment and
  FoG treatments (arXiv:1909.12371, Sect. 3.1.1); μ_hf and its 2D reference values
  (arXiv:1805.00033, Eq. 13; arXiv:1902.09797, Sect. III); six randomised nulls and the
  block bootstrap (Step 5 table); M_crit by ⟨cos θ⟩ = 0.5 or median μ = 0.5, SAMI threshold
  scan, PLS primary-parameter analysis (Step 6); reasons for disagreement with sizes: 2D
  signal loss ~40% (App. B of arXiv:1902.09797), stellar against Hα χ², flip against filament
  diameter (Eq. 14), smoothing scaling (arXiv:1201.5794, Eq. 3), mass–redshift trap,
  post-selection significance. **Y.**

**Q4 — Filament gas in tSZ, X-ray and radio: filament selection, halo removal, δ and T,
limits of the simulation comparison.**
- L2 (methods §6): expected WHIM state in TNG300 (arXiv:2010.15139), four routes, eRASS:4
  filament selection and masking list (arXiv:2406.00105, Sect. 2.1, Table 1), pair-stack
  halo subtraction in one sentence, β-model and r_c/r profiles, APEC temperatures, tSZ +
  lensing, δ_c T_e r_c degeneracy. Radio is absent from methods; the halo-model subtraction,
  covariance, significance definitions and what limits the comparison with simulations are
  not there. **P.**
- L3: stacking geometries with backgrounds (Step 1 table); mask convergence at 3 R₅₀₀ and
  point-source tests (arXiv:1911.09706, App. A; arXiv:2206.00084, Sect. 5); radio wavelet
  source subtraction (arXiv:2101.09331, Sect. 3.2); non-parametric and stretched halo fits
  and why a halo model double counts the two-halo term (arXiv:1709.05024, Sects. 3.2, 4.2;
  arXiv:1709.10378, Sect. 3.2); unresolved emitters 37–40% (arXiv:2406.00105, Table 2,
  Eq. 8); nine covariance methods and the jackknife against independent-pair σ (5.1 → 2.9);
  cylinder and β-model inversions (arXiv:1709.05024, Eqs. 5–11; arXiv:1911.09706, Eqs. 9–21),
  multiphase King model (arXiv:2406.00105, Eqs. 13–21); limits for simulation comparison:
  beam dilution ~15% in BAHAMAS, 1T bias on multiphase gas, background-annulus choice
  moving f_b from 0.127 to 0.086 Ω_b (arXiv:2507.08561, App. B), σ definitions not
  comparable. **Y.**

**Q5 — Baryon census by phase and tracer; FRB DM–z to a baryon fraction; double counting.**
- L2 (results §5.2): census rows — UV absorbers 28/25/18%, shortfall 29 ± 13%
  (arXiv:1112.2706), O VII claim and re-analysis (arXiv:1806.08395; arXiv:2305.01587), FRB
  Ω_b and f_IGM = 0.76, f_X = 0.15 (arXiv:2409.16952), FRB in voids, filament tSZ fractions;
  "missing" depends on reference epoch and what is counted. How the DM–z relation becomes a
  baryon fraction, the host and Milky Way terms and the scatter, and how the absorber census
  is computed are absent. **P.**
- L3: column-density integral and per-ion conversion (arXiv:2305.01587, Eqs. 1–4;
  arXiv:1112.2706, Eq. 1); ionisation and metallicity corrections for O VI, Lyα, BLA, O
  VII/VIII (arXiv:1112.2706, Eqs. 2–9, App. B; arXiv:2507.21719, Sect. 4.2.1); error
  propagation (App. A, Eq. 10); redshift path and dN/dz (arXiv:2610.11203, Eqs. 1–3); ΔC
  statistic, boundary problem and look-elsewhere (arXiv:2305.01587, Sects. 4.3.2, 4.4.1);
  vetoes and double counting — O VI–BLA overlap, O VII/O VIII one phase, CGM veto
  (arXiv:2507.21719, Sects. 3.2.3, 4.2.4); temperature systematic (Table 4). The FRB part is
  not in the dossier (it points to `cosmo-multimessenger/deep/frb-baryon-distribution.md`):
  host and Milky Way DM terms and the cosmic scatter are absent from both runs. **P.**

**Q6 — Protocluster finding at z > 2 and supercluster definitions; descendant mass; purity
and completeness.**
- L2 (results §§6.1–6.2): supercluster definitions (percolation, D8 threshold, Laniakea as
  diverging-flow volume; arXiv:2505.22082, Sect. 2; arXiv:1409.0880), protocluster
  definition and R_e ~ 5–10 cMpc (arXiv:1310.2938), HSC > 76% purity, ODIN, Hyperion, the
  z > 5 aperture fix (arXiv:2605.28930). The overdensity estimators, the mass formulas and
  their calibration, and completeness are absent. **P.**
- L3: descendant definition, R_e and extent, main-halo minority (arXiv:1310.2938, Eq. 4;
  arXiv:1506.08835, Sect. 4); three estimators (aperture counts, cross-validated Gaussian
  kernel, Voronoi Monte Carlo) with reasons (arXiv:1708.09421, Sect. 2.2; arXiv:2406.08645,
  Eq. 1; arXiv:1806.06073, Sect. 3.1); thresholds and random-map contamination (< 0.1% to
  ≈ 20%); purity thresholds per tracer and window (arXiv:1310.2938, Tables 2–4), aperture
  classification (arXiv:1710.02148, Sect. 3.4.1); HSC purity 76% against completeness ~6%;
  five mass routes and the TNG300 correction factors ×3/×2/×1.15 (arXiv:2406.08645,
  Sect. VI.2); three supercluster definitions with the future-collapse table by Ω_m
  (arXiv:1502.04584, Table 1); supercluster mass routes and the ρ_c/ρ_m convention trap. Lyα
  tomography selection rests on a pointer to `cosmo-lyman-alpha`. **Y.**

**Q7 (control, web statistics).** L2 (results §§1–2): fraction definitions on 100³ cells,
per-component ranges across twelve finders (arXiv:1705.03021, Sect. 5.3), NEXUS+ evolution
(arXiv:1401.7866, Sects. 5.1, 6.1, 7), DESI DR1 and EDR volume fractions with methods,
connectivity from peak theory and MDPL2 (arXiv:1803.11477; arXiv:2607.14785), MTNG evolution
(arXiv:2309.08659). **Y.** L3 (`web-classification`): DESI BGS fractions stable with R_s =
6–11 Mpc but not across tracers (arXiv:2604.02463, App. A.1). **Y**, small gain on the
smoothing part.

**Q8 (control, reconstructions).** L2 (methods §7): BORG probabilistic web maps on SDSS
(arXiv:1512.02242), ASTRA ranks, probabilistic DisPerSE, Wiener filter and HMC V-web on
Cosmicflows with the 68% realisation cut (arXiv:2606.13538, Sect. 4), TARDIS and the ≲ 5
h⁻¹Mpc sightline condition (arXiv:1612.00067; arXiv:1903.09049). 2M++ is named only as
`cosmo-simulations-mocks` territory; how reconstruction noise moves the class is given only
as ensemble cuts. **P.** L3 (`web-classification`): classifier information gain on the
BORG-SDSS posterior (arXiv:1606.06758, Table 4). **P**, no gain on 2M++ or noise
propagation.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| Q1 | P | Y | Y | yes |
| Q2 | P | Y | Y | yes |
| Q3 | P | Y | Y | yes |
| Q4 | P | Y | Y | yes |
| Q5 | P | P | Y | partial |
| Q6 | P | Y | Y | yes |
| Q7 (c) | Y | Y | Y | — |
| Q8 (c) | P | P | Y | — |

**Verdict: pass.** L3 answers 5 of 6 with locators; 5 L2 failures answered; one dossier
per question; controls inert (Q7 gains only a stability table, Q8 none). Q5 fails at L3
because `deep/missing-baryons.md` covers the absorption-line census only, while the
subtopic title and the skill description include the FRB census; the FRB conversion lives
in `cosmo-multimessenger`. The Q2 dossier carries an inverted reading of its main GAMA test
(E2).

### Source checks (2 used)

- **E1** `deep/spin-alignments.md`, Numbers and the closing note, used in Q3: Codis et al.
  M_crit "4(±1) × 10¹² M☉ in the text, 5(±1) × 10¹² M☉ in Fig. 3 and Eq. 1", in M☉.
  arXiv:1201.5794, Sect. 2.2: "M^s_crit(z=0) ≃ 4(±1)·10¹² M☉ where M^s_crit is defined as
  the halo mass for which ⟨cos θ⟩ = 0.5"; Sect. 2.3, Eq. 1: "M^s_0 ≃ 5·10¹² M☉"; abstract
  5(±1)·10¹² M☉. Match (units M☉, both values present).
- **E2** `deep/environment.md`, "Matching, weighting or reshuffling", used in Q2: "the
  mass-gradient deviation between the extreme mass bins exceeds 3σ before reshuffling and
  is ~1σ after … So the GAMA colour gradient … does not survive the authors' own
  large-scale density reshuffling at the quoted significance; quote it with that test."
  arXiv:1710.02676, Sect. 6 and Fig. 12 caption: the numbers match (> 3σ before, ~1σ after,
  colour "similarly nearly cancelled"), but the paper reads the reduction the other way:
  "when the large-scale density is used in reshuffling, the signal is reduced …
  suggesting that the measured gradients … are not driven by the density at this scale",
  and density-matched samples still show the gradients, so "beyond the density, large
  scale structures of the cosmic web do impact these galactic properties". The dossier's
  own Step 2 (item 4) says reshuffling destroys the property–distance relation by
  construction, which is why a reduced signal argues against a density origin. **Mismatch**:
  the dossier's conclusion inverts the test. The same paragraph's "With galaxies within 3.5
  Mpc of nodes removed, the reshuffling cancels the mass gradients" refers, per the Fig. 15
  caption, to reshuffling D_skel in bins of D_node, a node test, not the density test.

### Generality flags

- `deep/web-classification.md` is DisPerSE-centred: of 93 citations, 67 are to DisPerSE
  analyses (arXiv:2002.01486, arXiv:2309.08659, arXiv:1710.02676, arXiv:2508.15915,
  arXiv:2506.15345, arXiv:2307.05240, arXiv:1009.4015); Bisous (7), T-web (12) and the BORG
  comparison (3) are the alternatives, and NEXUS/MMF on galaxy data is not mentioned.
- `deep/missing-baryons.md` rests on four papers (60 of 65 citations): one FUV census
  (arXiv:1112.2706) and an X-ray series (arXiv:2305.01587, arXiv:2507.21719, "Paper I" of
  which was not read); the O VII detection claim (arXiv:1806.08395) was read at abstract
  only, so the side that claims detection is represented by its critics.
- `deep/spin-alignments.md`, `deep/filament-gas.md`, `deep/environment.md` and
  `deep/protoclusters-superclusters.md` spread their citations over SAMI, MaNGA, SDSS and
  simulations; Planck, ACT, ROSAT, eROSITA and radio; GAMA, SDSS, TNG and DESI; HSC, ODIN,
  VUDS, TNG and supercluster catalogues. No flag.

## cosmo-data-pipelines

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| P1 | methods | `deep/extraction-sky.md` |
| P2 | methods | `deep/redshift-fitting.md` |
| P3 | methods | `deep/image-detrending.md` |
| P4 | methods | `deep/cmb-mapmaking.md` |
| P5 | methods | `deep/lss-catalogues.md` |
| P6 | results | `deep/source-injection.md` |
| P7 (control) | methods | `deep/image-detrending.md` (closest: brighter-fatter and the PSF-star flux ceiling) |
| P8 (control) | methods | `deep/source-injection.md` (closest: Step 5, matching and blend flags) |

### Answers

**P1 — Extraction (boxcar, optimal, spectro-perfectionism), flux calibration and sky
subtraction in DESI, BOSS/eBOSS, 4MOST/WEAVE; residuals reaching the Lyα forest or
emission-line redshifts.**
- L2 (methods §3): DESI order of operations (arXiv:2209.14482, Sect. IV), optimal
  extraction exact only for separable PSFs (Horne 1986), spectro-perfectionism and the
  resolution matrix (arXiv:0911.2689), fit R·M not M (Sect. IV.5.7); three sky families
  with the DESI sky-fit equation (Eq. 14), PCA (arXiv:1007.0648), beam switching
  (arXiv:1609.06142), NMF and LAMOST variants; standard-star flux calibration in one
  sentence; ε_λ noise term. BOSS/eBOSS extraction, sky and flux calibration are absent,
  4MOST/WEAVE are listed under "Not verified", and which residuals reach the forest or the
  line redshifts is reduced to "matters for the redshift fitter's Δχ²". **P.**
- L3: pixel variance from a model image, not the data, and why (arXiv:2209.14482,
  Sect. IV.2.9, Eq. 2); Gauss–Hermite PSF with tails left out on purpose and the δF/F
  stability criterion tied to the ELG false-identification requirement (Sects. IV.3.1–IV.3.3,
  Eqs. 3–4); the extraction algebra C⁻¹ = QQ, R = s⁻¹Q and the few-percent difference
  with row-wise optimal extraction (arXiv:0911.2689, Sects. II–III, Eqs. 8–15); fibre
  flat, one lamp at a time, 2% radial residual (Sects. IV.6.2–IV.6.3); per-fibre α_k
  replaced in DR1 by a positioner throughput model, PCA of Δλ and ΔLSF, variance Eq. 16
  (Sects. IV.7.2–IV.7.4); standard-star cuts, model grid, aperture-loss Eq. 18
  (Sects. IV.8–IV.9.3); cross-talk 0.1–0.2% rising to 1.5% at 9800 Å (Sect. IV.10);
  co-addition Eq. 20 (Sect. IV.11); the sky-correction variants table with AAOmega PCA and
  the nod-and-shuffle 2√2 cost (arXiv:1007.0648, Sect. 2.3, App. B.2); BOSS quasar
  design-wavelength miscalibration, +19% at 3600 Å, −24% at 10,000 Å, and the
  offset-standard fix (arXiv:1506.04790, Sect. III.3, Eq. 13, Table 2); residuals
  reaching science: DR1 P1D noise power 2.8% low (arXiv:2505.09493, Sect. 4.2), unmasked
  cosmic rays and sky residuals as false ELG lines, the 6% blue-end step. BOSS
  extraction and sky model and the 4MOST, PFS, WEAVE pipelines remain under "Not
  verified". **Y** (DESI-centred; see flags).

**P2 — Template fitters and after-burners; redshift success and catastrophic failures;
dependence on tracer and depth.**
- L2 (methods §4): χ² scan over linear template combinations; BOSS PCA templates with
  VI and repeats (arXiv:1207.7326); redmonster archetypes (arXiv:1607.02432); Redrock
  outputs and DELTACHI2 = 25 as 5σ (arXiv:2503.14745, Sect. III.1.2); PCA false fits
  (arXiv:2209.14482, Sect. IV.13); archetype refit; GAMA autoz; QuasarNET and the Mg II
  after-burner in one sentence; Euclid SPE quality cuts; definitions of success and
  purity to match. How the after-burners combine with Redrock, how the good-redshift cut
  is chosen, the VI protocol and the failure rates per tracer are absent from methods
  (the rates are in `results.md`). **P.**
- L3: per-class bases and redshift grids for BOSS and Redrock (arXiv:1207.7326,
  Sect. III.1; arXiv:2209.14482, Sect. IV.12), redmonster polynomial order from failure
  rates (arXiv:1607.02432, Sect. III.1), Euclid line-identity prior (arXiv:2503.15308,
  Sect. 2.2); the confidence-statistic table with thresholds and reasons (BOSS Δχ²_r
  0.01 with a relative term, Z_NOQSO, redmonster 0.005, Redrock 25, spe_z_prob); the
  DESI VI protocol, merge tolerance and quality scale (arXiv:2208.08516, Sect. II,
  Eq. 1); inclusion and purity definitions (Eqs. 3–5) and the DR1 per-tracer cuts with
  reasons, including the ELG [O II] S/N–Δχ² cut (arXiv:2411.12020, Sect. 3); the QSO
  maker logic and where missed quasars fall (arXiv:2208.08517, Sects. III.3, V.1);
  precision and error calibration on repeats (Eq. 8; BOSS 1.19/1.34, eBOSS 0.65); success
  per tracer at main depth and in DR1 (BGS 98.9%, LRG 99.1%, ELG 72.7%, QSO 66.8%;
  Table 2), QSO catastrophics by redshift and threshold; the TSNR2 failure weight
  (Sect. 7.1, Eq. 5). Mg II and QuasarNET thresholds are listed as not read. **Y.**

**P3 — ISR steps and sensor effects in DES, HSC, Rubin; brighter-fatter derivation and
validation; astrometry against Gaia.**
- L2 (methods §5): Rubin DP1 ISR order (arXiv:2603.23786, Sect. IV.2.1); brighter-fatter
  physics and the DECam reverse charge shift fitted to flat-field correlations
  (arXiv:1402.0725; arXiv:1501.02802); DP1 anomalies named; DECam astrometric model and
  Gaia interpolation to 7 mas, 3–6 mas solution (arXiv:1703.01679); Rubin gbdes against
  Gaia DR3 with proper motion and parallax. DES and HSC ISR steps, fringing, tree rings,
  edge distortions and how a brighter-fatter kernel is derived and validated are absent.
  **P.**
- L3: calibration-product table HSC / DES / Euclid VIS with stated reasons
  (arXiv:1705.06766, Sect. 4.1; arXiv:1801.03177, Sects. III.1–III.3; arXiv:2503.15303,
  Sects. 3.4–3.10), Rubin twilight flats (arXiv:2603.23786, Sect. II.3), DES order and
  mask rules (Sect. III.2); fringe frames (HSC) and PCA sky templates (DES); area
  coefficients, sum rule, covariance and PTC equations, and the non-linearity bias on a_00
  (arXiv:2301.03274, Eqs. 1–7); five kernel variants (DES imposed ratios, curl-free HSC and
  Rubin, Euclid Poisson kernel, electrostatic model, PTC-linearising kernel) and their
  validation on the δT/T ≤ 10⁻³ requirement (arXiv:2301.03274, Sect. 6.1; arXiv:2312.03115,
  Sect. VI); tree rings ~1% and edge distortions ~10% as pixel-size variations with
  templates (arXiv:1403.6127, Sect. IV); CTI and trap pumping (arXiv:2503.15303, Sect. 3.8,
  Eq. 1). Astrometry rests on the L2 passage; the dossier lists astrometry beyond L2 as not
  read. **Y.**

**P4 — Maximum-likelihood, destriping and filter-and-bin map-makers; TOD filtering and
flagging; transfer function; large-scale cost.**
- L2 (methods §8): d = Pm + n and the GLS solution, early CG stopping biases
  (arXiv:2503.14451, Sect. V.2); the families table (Madam destriping, Gibbs destriping,
  SRoll2 templates, ACT DR6 ML with cut-sample and model-error degrees of freedom,
  SPT-3G filter and bin with simulated transfer function, POLARBEAR filtering, HWP
  marginalisation). Flagging and cuts, the noise model, how the transfer function is
  measured and the large-scale cost (Naess & Louis) are not in methods; the ACT
  transfer function is a pointer to `surveys-and-data.md`. **P.**
- L3: ACT three-level data selection with thresholds (arXiv:2503.14451, App. A,
  Tables 2–3, 13) and Planck's ring-block χ² test (arXiv:1807.06207, Sect. 2.1.3);
  time-domain calibration and preparation in ACT, Planck HFI and SPT (Sects. II.3–III.1;
  Sect. 2.1.2; arXiv:2603.20163, Sects. III.2.4, VI.1); noise models (ACT Eq. 2 and the
  multipass reason; SPT PSD weight Eq. 8; HFI 1/f from glitch tails, Sect. 5.8);
  nearest-neighbour against bilinear pointing (Eqs. 6–7; arXiv:2210.02243, Sect. 2.2.3);
  cut-sample and model-error degrees of freedom (Sects. III.3.3–III.3.4, Eqs. 8–9);
  SPT high-pass ℓ_x,c = 300 chosen from four runs, source masking and filtering
  artefacts, anti-alias filter (arXiv:2603.20163, Sects. III.2.1–III.2.3); empirical
  transfer function in SRoll (Sect. 5.11.1); the comparison table of the three families;
  the toy in which ML, observation-matrix filter-and-bin and destriper all lose 2/3 of a
  long mode with nearest-neighbour pointing (arXiv:2210.02243, Sects. 2.1.5–2.1.6); ACT
  low-ℓ TT cut from a few-percent flat field (Sect. II.4.1); null splits and the SPT
  decision rule (Sect. VII.1.4). The ACT injection transfer function itself is a pointer
  to L2. **Y.**

**P5 — Clustering catalogue: masks, randoms, completeness, redshift-failure and imaging
weights in DESI, eBOSS, DES; tests against residual systematics and signal removal.**
- L2 (methods §9): randoms as an unclustered draw of the selection (arXiv:2405.16593);
  mangle; DESI vetoes ZWARN_MTL and TSNR2 (Sect. 4.2); shuffled random redshifts and the
  radial integral constraint (Sect. 7.2); Euclid visibility mask; Balrog randoms; weights
  multiplied, FKP; eBOSS χ²/dof 776/10 → 6/8 (arXiv:2007.09000); the method-family table
  with its caveats (arXiv:1509.08933; arXiv:1907.11355; arXiv:2105.13540). Completeness
  definitions, the regression maps per tracer, the null-test pass rule and the
  signal-removal test are absent; the DESI weight definitions are a pointer. **P.**
- L3: potential assignments (arXiv:2411.12020, Sects. 2.1, 5.1); veto table with areas
  and reasons (Sects. 4.1–4.3.2, Table 5); f_TLID and f_tile, θ-cut, PIP from 128 altMTL
  realisations and why it is not the baseline (Sects. 5.2–5.3, Eqs. 2–3); TSNR2 failure
  weight (Sect. 7.1, Eq. 5) against eBOSS per-plate S_i model (arXiv:2007.09000,
  Sect. 5.3, Eqs. 5–6); maps and methods per tracer, with ΔEBV kept for validation because
  of CIB (Sects. 6.1–6.4); null test against 25 uncontaminated altMTL mocks with a pass
  rule fixed while blinded (Sect. 6); random redshifts per photometric region and the
  normalisation (Sect. 8.1); w_tot and FKP refactoring (Sect. 8.2, Eqs. 6–9); eBOSS close-
  pair weight and linear regression with residual χ² (Eqs. 2, 13, Table 5); DES Y3 PCA map
  basis, ISD with T_1D = 2 chosen on mocks, false-correction bias ≤ 20% σ, method spread
  in the covariance (arXiv:2105.13540, Sects. 4.2, 5.3.1, 7.1, 8.4, Eqs. 7–10, 20–23);
  Euclid detection-model randoms (arXiv:2511.20856, Sect. 3.3, Eq. 22). **Y.**

**P6 — Balrog and Obiwan: injection mechanics, injected population, measured quantities,
limits.**
- L2 (results §5b; SKILL): programme table (Balrog SV, Y3 from Deep Field models on 20%,
  Y6 146 million, Obiwan eBOSS ELG, Rubin DP1 with DC2), what each measured (randoms,
  density fluctuations within 1%, colour calibration, percent-level properties, clustering
  validation). How sources are rendered and where they enter, the truth selection, the
  pattern and matching, the products (n(z) transfer function, magnification) and the limits
  are absent. **P.**
- L3: where injection enters the DESDM chain and what it cannot test (arXiv:2012.12825,
  Sect. II.1.1; arXiv:1705.01599, Sect. 3.3); truth catalogue from bdf fits of deep fields
  with cuts and reasons (Sects. III.1, III.4) and the Y6 changes (arXiv:2501.05683,
  Sects. 3.1, 3.4); GalSim rendering (Sects. II.2.4–II.2.5); lattice against random
  patterns per programme with reasons; two-step matching and the Y6 1.5″ flag
  (Sect. III.5; arXiv:2501.05683, Sect. 3.4); the validation ladder and the 3 mmag floor
  (Sect. II.3); products: SOM transfer function for photo-z (Eq. 3), magnification
  coefficient (Eq. 8), depth, Obiwan weight map (arXiv:2007.08992, Sect. 5.3), radial
  selection (arXiv:2411.12024, Eqs. 9–13), null tests; single-epoch against co-add,
  emulated against production, Obiwan with Tractor models and the de-biased LRG shapes
  (arXiv:2405.16299, Sect. 5.1); limits: Obiwan failures for DESI ELG and LRG with χ²
  values and the hybrid (arXiv:2411.12024, Sects. 5.2, 7.1–7.2), upstream PSF and
  background errors invisible. **Y.**

**P7 (control, PSF modelling).** L2 (methods §6): pipeline steps, review of contributors
and validation metrics (arXiv:2306.07996), Piff for Rubin (arXiv:2501.05781), HSC co-add PSF
from input models and its failure where the number of inputs changes (arXiv:1705.06766,
Sect. 3.3.1); ρ statistics and shear propagation are a pointer to `cosmo-weak-lensing`;
PSFEx is unread; chromatic effects and the HSC and Euclid models are not described. **P.**
L3 (`image-detrending`): brighter-fatter as a PSF-size bias, the δT/T requirement and the
cap on PSF-star flux (arXiv:2301.03274, Sect. 6.1; arXiv:2312.03115, Sect. VI). **P**,
small gain on one sensor input to the PSF.

**P8 (control, deblending and co-addition).** L2 (methods §7): matched-filter against
weighted and PSF-homogenised co-addition and the proper co-add (arXiv:1512.06872;
arXiv:1512.06879), production weighted co-adds (arXiv:1705.06766, Sect. 3.3); deblender
table (SDSS-heritage, SCARLET, Tractor, DeepDISC, BLISS) with HSC mitigations
(Sect. 4.8.3); blending biases measured by the BTK benchmark (arXiv:2607.28475) and
unrecognised blends against HST (SKILL, arXiv:2610.10986). **Y.** L3 (`source-injection`):
match rules and ambiguous-blend fractions as part of an injection run (arXiv:2012.12825,
Sect. III.5). **Y**, no gain needed.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| P1 | P | Y | Y | yes |
| P2 | P | Y | Y | yes |
| P3 | P | Y | Y | yes |
| P4 | P | Y | Y | yes |
| P5 | P | Y | Y | yes |
| P6 | P | Y | Y | yes |
| P7 (c) | P | P | Y | — |
| P8 (c) | Y | Y | Y | — |

**Verdict: pass.** L3 answers 6 of 6 with locators; 6 L2 failures answered; one dossier
per question; controls inert (P7 gains one sensor input, P8 none). `physics-and-methods.md`
names each method family with its foundation paper but holds no settings, thresholds or
pass rules; every dossier states its L2 overlap and adds the procedure. The surveys a
question names are covered unevenly: 4MOST, WEAVE, PFS and the BOSS extraction and sky
model are "Not verified" in both L2 and L3 (P1).

### Source checks (2 used)

- **E3** `deep/redshift-fitting.md`, Step 4 table, used in P2: ELG cut "log₁₀ S_[OII] +
  0.2 log₁₀ Δχ² > 0.9" and "DR1 success, observed targets … ELG 72.7%". arXiv:2411.12020,
  Sect. 3 (ELG): "spectroscopic success: log10(S[OII]) + 0.2 log10(Δχ²) > 0.9, where
  S[OII] is the signal-to-noise ratio of the [OII] emission line doublet … 72.7% of ELG
  observations yield a successful redshift"; BGS "98.9% of observed BGS_BRIGHT targets".
  Match.
- **E4** `deep/lss-catalogues.md`, Step 6, used in P5: pass rule "the total χ²_null over
  all tested maps below that of at least one of the 25 mocks, and each map's χ²_null below
  at least two mocks … the maps and methods were never changed after unblinding".
  arXiv:2411.12020, Sect. 6: "When blinded, we classified the null tests as passed if the
  sum of the χ²_null for the data across all tested maps was less than that from at least
  one of the 25 mocks and each of the individual maps tested had a χ²_null less than at
  least two of the 25 mocks … fixed based on tests on the blinded data and never changed
  on the unblinded data". Match. The same section's footnote 14 says the Poisson errors
  were erroneously divided by the pre-refactoring mean completeness weight, making them
  underestimated but consistently for data and mocks; the dossier's "known to be only
  approximately right" does not mention it (omission, not an error).

### Generality flags

- `deep/extraction-sky.md` rests on one pipeline: of 65 explicit citations, 47 are DESI
  papers (arXiv:2209.14482 alone 36, plus most of the 41 bare section locators), with BOSS
  only through its quasar flux-calibration fix (arXiv:1506.04790, 6) and AAOmega PCA
  (arXiv:1007.0648, 5); BOSS idlspec2d extraction, and 4MOST, PFS, WEAVE and SDSS-V
  pipelines, are under "Not verified". The dossier's scope line says so.
- `deep/lss-catalogues.md` follows DESI DR1 (arXiv:2411.12020, 33 of 61) with eBOSS (10)
  and DES Y3 (9) compared step by step; KiDS, HSC and UNIONS lens catalogues are not read.
  Acceptable for the question; noted.
- `deep/redshift-fitting.md`, `deep/image-detrending.md`, `deep/cmb-mapmaking.md` (ACT 31,
  SPT 19, Planck 10 of 68) and `deep/source-injection.md` (Balrog, Obiwan, SynPipe, Rubin)
  spread their citations over several programmes. No flag.

## cosmo-early-universe-exotica

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| E1 | syst | `deep/sgwb-pta.md` |
| E2 | methods | `deep/phase-transitions.md` |
| E3 | results | `deep/cosmic-defects.md` |
| E4 | syst | `deep/primordial-black-holes.md` |
| E5 | methods | `deep/scalar-induced-gw.md` |
| E6 | methods | `deep/spectral-distortions.md` |
| E7 (control) | methods | `deep/sgwb-pta.md` (closest: "Red-noise priors"; no dossier mentions EDE) |
| E8 (control) | methods | `deep/spectral-distortions.md` (closest: Step 2, energy release of decaying particles) |

### Answers

**E1 — PTA evidence: CURN, HD, Bayes factors and frequentist statistics, per-pulsar noise;
array differences; SMBHB against cosmological origin.**
- L2 (syst §1; SKILL): systematics table — white and red noise per pulsar
  (arXiv:2306.16218), DM variations and InPTA, solar wind, MPTA noise-model dependence
  (arXiv:2412.01153), γ fragility, split-data tension (arXiv:2306.16215; arXiv:2306.16214),
  monopole in bin 2, null distribution by sky scrambles and phase shifts against BF
  200–1000 (arXiv:2306.16213), IPTA comparison (arXiv:2309.00693), Allen cosmic variance,
  SMBHB prior behind Bayes factors 10–100 (arXiv:2306.16219); significances per array in
  the SKILL. The likelihood, the optimal statistic, the frequency and prior choices and how
  each array models its noise are absent. **P.**
- L3: timing model and why parallax and proper motion are fitted (arXiv:2306.16213,
  Sect. II); EFAC, EQUAD, ECORR and EPTA's choice to drop ECORR (arXiv:2306.16214,
  Sect. 2); the Gaussian-process likelihood and the IRN/CURN/HD covariance with the HD
  function (Eqs. 1–8); frequency bins per array and why (Sect. II; Sect. 4.1;
  arXiv:2309.00693, Sect. III.1); priors and R̂ < 1.01 (Table 1, App. B); four Bayes-factor
  tools (Eq. B1, product space, reweighting); the optimal statistic and why its S/N is not
  a σ level (Sect. IV, Eqs. 9–11); phase shifts and sky scrambles with the match
  criterion (App. F, Eq. F1) and their saturation (arXiv:2305.04464); per-array noise
  recipes (DMX against DMGP, EPTA model selection, PPTA caps and band noise) and the DMGP
  shift of γ (Sect. V.1); PPTA prior construction and its effect on the CURN Bayes factor
  (arXiv:2306.16215, Sects. II.1.1, III.1); EPTA full
  against recent data and BayesEphem 60 → 17 (Sects. 4.3, 4.4.2, 6); spurious CURN
  detections (arXiv:2207.12237); LVK cross-correlation estimator (arXiv:2101.12130,
  Eqs. 2–7). CPTA and MPTA likelihoods are under "Not verified"; the SMBHB-against-
  cosmological test rests on the L2 prior statement and the K-ratio pointer. **Y.**

**E2 — Phase-transition GW spectrum from (α, β/H, v_w, T); sources and templates;
template uncertainty for PTA and LISA.**
- L2 (methods §2): sources and history (arXiv:astro-ph/9310044; arXiv:1304.2433); the
  four parameters with α and β definitions (arXiv:2204.05434, Sect. 6.2, Eqs. 37, 39);
  effective-potential theory error; template papers (arXiv:1512.06239; arXiv:1910.13125;
  arXiv:2403.03723) and NANOGrav pt-bubble and pt-sound with slope priors
  (arXiv:2306.16219, Sect. V.3); dark-radiation bound (arXiv:2306.09411). No amplitude or
  peak formula, no efficiency, no suppression factor, and no size for the template
  uncertainty. **P.**
- L3: α definitions (bag, α_θ, α_e) and why (arXiv:1910.13125, Eqs. 9–13, Sect. 2.2); κ_s
  fit and the 0.6 bulk-fluid factor (arXiv:2306.16219, Sect. V.3; arXiv:2403.03723,
  Sect. 2.2.1); H_*R_* from β (Eq. 11); source choice, runaway walls, turbulence neglected
  or fitted (EPTA, arXiv:2306.16227, Sect. 4.3.1); the three amplitude prescriptions with
  the redshift factor and the lifetime suppression Υ (Eqs. 33–36; Eqs. 19–32; Eq. 10);
  peak frequencies and shapes (Eqs. 37–39; Eqs. 30–31; Eqs. 8–9); NANOGrav, EPTA, Bringmann
  and LISA SGWBinner fits with priors and foregrounds (Table 3; Sect. 4.3.2; Sect. 4,
  Eq. 15; Sect. 3.3); template uncertainty sized: K² differs by 0.36 between the κ
  normalisations [der], suppression conventions differ by order-unity factors near
  H_*τ_sh ~ 1, T_* moves between templates through 0.58 against 1.58 and the slope prior,
  daisy-resummation scale dependence of two to three orders of magnitude in the peak
  amplitude (arXiv:2009.10080, abstract). **Y.**

**E3 — Gμ limits from CMB, LVK stochastic and burst, PTA; loop models and string types;
why limits differ by orders of magnitude.**
- L2 (results §4): Planck Nambu–Goto < 1.5 × 10⁻⁷ and Abelian–Higgs < 3.2 × 10⁻⁷
  (arXiv:1303.5085); pre-2014 PTA ≤ 2.8 × 10⁻⁹ with the BOS distribution
  (arXiv:1309.6637); LVK O3 ≲ 4 × 10⁻¹⁵ for one loop model, models A, B and interpolating
  (arXiv:2101.12248); NANOGrav stable-string Bayes factors 0.28–0.38, superstrings and
  metastable strings fitting (arXiv:2306.16219, Sect. V.4). How each limit is derived,
  what the loop models are and why the numbers spread are absent; the spread is stated in
  the systematics file, not loaded. **P.**
- L3: VOS loop density with calibration constants (arXiv:2306.16219, Eqs. 43–45); models A
  (BOS), B (LRS), C-1, C-2 written out (arXiv:2610.02590, Eqs. S-49 to S-54) and why
  simulations differ on small loops (arXiv:2306.16227, Sect. 4.2.1); harmonic P_k
  templates and the burst waveforms with beaming (arXiv:2306.16219, Eq. 41;
  arXiv:2101.12248, Eqs. 1–4, 8); the two Ω_GW sums (Eqs. 40, 42; Eq. 10); metastable
  E-factor and √κ prior, superstrings by 1/P (Eqs. 46–52); searches: LVK stochastic and
  burst set-ups, PTA K-ratio and HPD limits, multi-band joint likelihood, Planck f₁₀ fit
  (arXiv:2101.12248, Sects. III, V; arXiv:2610.02590, Eqs. 7–11; arXiv:1303.5085,
  Sect. 3); the spread: LVK model A Gμ ≳ 9.6 × 10⁻⁹–10⁻⁶ against B, C ≳ 2–7 × 10⁻¹⁵,
  harmonic against burst 25–31% on the rising branch, N_c and N_k dependence, Nambu–Goto
  against field-theory loops (f_NG < 0.1, arXiv:2103.16248, abstract), segments
  contested (arXiv:2507.12386). **Y.**

**E4 — PBH limits from microlensing, LVK mergers and sub-solar searches, CMB accretion;
assumptions; the claimed OGLE excess.**
- L2 (syst §2): halo model, clustering, event selection and efficiency with the
  OGLE–MACHO dispute (arXiv:2509.05400 against arXiv:2403.02386), wave optics and finite
  source, accretion moving the CMB threshold between 20 and 50 M☉ (arXiv:2002.10771),
  evaporation models, withdrawn limits, LVK mass function and binary channel
  (arXiv:2405.05732). Each assumption is named; how a limit is derived from the data is
  absent. **P.**
- L3: linear-kernel structure f_max = (A_exp − A₀)/A₁ (arXiv:2601.06024, Sect. VI,
  Eqs. 25–27); optical depth and rate with the HSC and OGLE halo models
  (arXiv:1701.02151, Sect. 1.2, Eqs. 11–14; arXiv:2403.02386, Methods); stellar
  foreground lenses (12.7 or 20.4 expected, 13 seen); efficiency by injection; HSC Poisson
  bound N_exp ≤ 4.74 and OGLE null and full timescale likelihoods (Eqs. 1–6) with their
  difference ≤ 0.59 dex; finite-source and wave-optics corrections (Sect. 5); LVK merger
  rate with suppression factors and the three-body channel (arXiv:2405.05732, Eqs. 12–18),
  hierarchical likelihood and three readings of the catalogue (Eqs. 1–9, Sect. IV.2);
  extended mass functions and the quadrature rule (arXiv:1705.05567, App. A); OGLE halo
  against the Hawkins critique (v_c 190 against 130 km s⁻¹, Sect. 3.6) and the efficiency
  dispute (Sects. 3.3–3.4), with a referee reading; OGLE's best point resting on one 7-day
  event (Δχ² ≈ 3.7). CMB accretion rests on the L2 line only (the dossier scope leaves it
  out), and the bulge ultrashort events of arXiv:1901.07120 are in `results.md`, not in
  the files loaded. **Y.**

**E5 — SIGW spectrum from an enhanced curvature spectrum: kernel, gauge,
non-Gaussianity, equation of state; PBH overproduction; which choices decide viability.**
- L2 (methods §5): second-order sourcing (arXiv:gr-qc/0612013), analytic kernel
  (arXiv:1804.08577), single-field departure needed, three NANOGrav templates
  (arXiv:2306.16219, Sect. V.2), PBH link and the 2σ overproduction (arXiv:2306.17149),
  f_NL expansion inadequate (arXiv:2412.06764). No kernel formula, no PBH-abundance
  method, no equation-of-state treatment. **P.**
- L3: templates including BPL and EPTA power law (Eqs. 29–31; arXiv:2306.17149, Eq. 1;
  arXiv:2306.16227, Eqs. 25–26); the kernel and the δ-function closed form
  (arXiv:2306.16219, Eqs. 27–28; arXiv:2306.16227, Eq. 27); transfer to today and the three
  prefactor conventions (Eq. 26; arXiv:2306.17149, Eqs. 3–5; arXiv:2306.16227, Eqs. 29–30);
  fits and priors (Table 3; Sect. 4.4); Press–Schechter f_PBH (App. C.2, Eqs. C4–C9)
  against compaction-function thresholds (arXiv:2306.17149, Eqs. 9, 14–17, S3–S6) and why
  they disagree on the same data; three non-Gaussian maps and their opposite effects on
  PBHs (Eqs. 10–13), the Iovino 𝒜⁴ factor (arXiv:2412.06764, Eqs. 8–18); QCD equation of
  state in the infrared tail (arXiv:2306.17136, Eqs. 2–3, Table 1); K-ratio exclusions as
  prior-robust (Eq. A5). Gauge choice is not discussed in either file. **Y.**

**E6 — μ and y from FIRAS and its reanalyses; distortion of an injection history;
limits of PIXIE-type and balloon forecasts.**
- L2 (methods §8): y and μ origin, CosmoTherm (arXiv:1109.6552), ΛCDM μ ≈ 2.3 × 10⁻⁸ and
  the window (arXiv:1909.01593, Sect. 2.1), μ anisotropies (arXiv:2206.02762). FIRAS
  calibration, the foreground model, the monopole fit and how a forecast is built are
  absent. **P.**
- L3: leading-order μ, y, ΔT/T integrals with J_μ and z_μ (arXiv:2502.05188, Eq. 28;
  arXiv:1109.6552, Eq. 38) and the Green's function (Sect. 4.6); limit-to-energy
  conversion and the decaying-particle efficiency (arXiv:astro-ph/9605054, Sect. 7;
  arXiv:1109.6552, Eqs. 39–41); FIRAS instrument, external calibrator, linear monopole fit
  (Eqs. 3, 5, 7), Galactic model and latitude-cut test, |μ| < 9 × 10⁻⁵, |y| < 15 × 10⁻⁶
  with a 4 × 10⁻⁶ systematic (Sects. 2, 3.4, 6.1–6.3); the 2022 pixel fit with non-linear
  μ, foregrounds, six-term covariance and mask comparison (arXiv:2206.02762, Sects.
  III.1–IV.1, Eqs. 1–13); PIXIE forecast with 12 foreground parameters, synchrotron
  curvature and prior, Fisher and MCMC, and its sensitivity to assumptions
  (arXiv:1705.01534, Sects. 4–5, 7.1). Balloon proposals are not covered. **Y.** The
  dossier's locator for the mask-by-model table is wrong (source check E6).

**E7 (control, early dark energy).** L2 (methods §6; SKILL): potential, n = 3 baseline,
f_EDE, z_c, θ_i definitions and ACT DR6 priors (arXiv:2503.14454, Sect. V.1, Eqs. 10–12);
signatures and degeneracies; prior-volume effects and the profile result 0.072 ± 0.036
(arXiv:2112.12140); ACT DR6 < 0.088 with the DR4 hint gone, SPT + ACT + Planck < 0.070,
profile 0.09 ± 0.03 (SKILL, arXiv:2507.23355; arXiv:2505.08051). **Y.** L3
(`sgwb-pta`): nothing on EDE. **Y**, no gain.

**E8 (control, energy injection).** L2 (methods §9): p_ann ≡ f_eff⟨σv⟩/m_χ, ExoClass with
on-the-spot and constant f_eff (arXiv:1807.06209, Sect. 7.9, Eq. 86), f_eff tables per
injected species and energy mapping to s-wave models (arXiv:1506.03811), principal
components for decays (arXiv:1610.06933), DarkHistory with backreaction
(arXiv:1904.09296); p_ann < 3.2 × 10⁻²⁸ (SKILL). **Y.** L3 (`spectral-distortions`):
pre-recombination release only. **Y**, no gain.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| E1 | P | Y | Y | yes |
| E2 | P | Y | Y | yes |
| E3 | P | Y | Y | yes |
| E4 | P | Y | Y | yes |
| E5 | P | Y | Y | yes |
| E6 | P | Y | Y | yes |
| E7 (c) | Y | Y | Y | — |
| E8 (c) | Y | Y | Y | — |

**Verdict: pass.** L3 answers 6 of 6 with locators; 6 L2 failures answered; one dossier
per question; controls inert. The reference files name each method and its systematic
but give no formula or likelihood; every dossier supplies them. Gaps that remain at L3:
CPTA and MPTA noise modelling (E1), CMB accretion limits on PBHs (E4, L2 only), gauge
choice for SIGWs (E5), balloon forecasts (E6).

### Source checks (2 used)

Source-check numbers continue the part's sequence; they are not the question ids
E1–E8 of this skill.

- **E5** `deep/cosmic-defects.md`, "Loop distribution", used in E3: "LVK O3 stochastic
  exclusions: model A Gμ ≳ (9.6 × 10⁻⁹ – 10⁻⁶), B ≳ (4.0–6.3) × 10⁻¹⁵, C-1 ≳
  (2.1–4.5) × 10⁻¹⁵, C-2 ≳ (4.2–7.0) × 10⁻¹⁵". arXiv:2101.12248, Sect. V: "For model A, we
  rule out the range Gμ ≳ (9.6 × 10⁻⁹ − 10⁻⁶). For model B … (4.0−6.3) × 10⁻¹⁵. For model
  C-1 … (2.1−4.5) × 10⁻¹⁵, aside from a small region where N_k ≳ 180 … C-2 …
  (4.2−7.0) × 10⁻¹⁵"; bursts tighter only for C-1 with N_k > 70. Match; the C-1 exception
  for N_k ≳ 180 is not carried.
- **E6** `deep/spectral-distortions.md`, "Foreground model and mask" and "Not verified",
  used in E6: the model-by-mask table (A_d + β_d < 47, 51, 47, 53; fixed β_d < 74, 50,
  105, 179) is cited as "arXiv:2206.02762, Table 1", and the "Not verified" note says
  "Table 1 … prints [×10⁻⁵] in the header of its model rows while the caption … give
  10⁻⁶". arXiv:2206.02762, Sect. IV.1: Table 1 (masks FDS, PL90–PL40) is the monopole
  statistics table, header [×10⁻⁶], fiducial PL90 ⟨μ⟩ = −18.2 ± 14.3, < 47 — matching
  the dossier's Step 4 numbers. The model-by-mask table is **Table 2** ("μ distortion
  monopole upper limits for different choices of foreground separation methods and
  Galactic masks"), whose header prints [×10⁻⁵] and which has a last column σ_syst (2.5
  for A_d + β_d, 48 for fixed β_d, 34 for the FIRAS residual) that the paper takes as the
  systematic uncertainty. Values match; **locator mismatch** (Table 2, not Table 1) in
  two places and in the "Not verified" note, and the σ_syst column and the
  FIRAS-residual row are omitted.

### Generality flags

- `deep/sgwb-pta.md` is NANOGrav-centred: arXiv:2306.16213 carries 35 of 86 explicit
  citations and most bare locators; EPTA (14), the IPTA comparison (9) and PPTA are the
  alternatives, and CPTA and MPTA, which the question and the skill description name,
  are not read in their bodies.
- `deep/scalar-induced-gw.md` and `deep/phase-transitions.md` take their PTA fits from
  NANOGrav 15 yr new physics (arXiv:2306.16219, 26 and 21 citations) with EPTA and one
  independent group (arXiv:2306.17149) as the comparison; fits by PPTA, CPTA, MPTA and
  IPTA were not searched (both "Not verified" lists say so).
- `deep/primordial-black-holes.md`: the LVK part rests on one analysis
  (arXiv:2405.05732, 14 citations); microlensing on HSC and OGLE with EROS and MACHO only
  in L2; CMB accretion is outside its scope.
- `deep/spectral-distortions.md` rests on FIRAS data (the only measurement), with one
  reanalysis and one forecast paper; inherent to the field. `deep/cosmic-defects.md`
  spreads over NANOGrav, LVK, EPTA, Planck and a multi-band analysis. No flag.

## cosmo-galaxy-halo-connection

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| J1 | methods | `deep/profiles-concentration.md` |
| J2 | methods | `deep/hod-clf.md` |
| J3 | methods | `deep/abundance-matching-shmr.md` |
| J4 | methods | `deep/empirical-sam-hydro.md` |
| J5 | methods | `deep/assembly-bias.md` |
| J6 | methods | `deep/satellites.md` |
| J7 (control) | methods | `deep/assembly-bias.md` (closest: "Consequence for lensing") |
| J8 (control) | methods | `deep/profiles-concentration.md` (closest: Step 6, conversion between mass definitions) |

### Answers

**J1 — c(M) relations (Duffy, Diemer–Kravtsov or Diemer–Joyce, Ludlow, Child): definition,
fitting, halo sample; use in halo-model and lensing fits; baryons in hydro runs.**
- L2 (methods §4, §5 limits table): NFW and Einasto (arXiv:astro-ph/9611107;
  arXiv:astro-ph/0311231); the relation table — Bullock, Duffy with its Table 1
  coefficients per definition and the relaxed offset, Ludlow, Child in M/M*, Diemer 2019 at
  5%, CAMELS (arXiv:0804.2486; arXiv:1601.02624; arXiv:1804.10199; arXiv:1809.07326;
  arXiv:2610.03544); σ_ln c ~ 0.3 in the halo model (arXiv:2303.08752, Sect. 5.8); Duffy
  with fixed slopes as the usual lensing assumption. Fitting methods, samples and
  conversions are absent; baryons are one CAMELS line. **P.**
- L3: particle minima and their reasons per analysis and the resolution bound c_max
  (arXiv:1402.7073, Sect. 2.4; arXiv:1804.10199, App. B.6; arXiv:1809.07326, Sect. II.2);
  relaxation cuts and what they do (x_off, ρ_rms; Diemer & Joyce keep all haloes and
  why); centring effect < 5% to 20%; bins, radial ranges and fits per analysis, with
  Einasto α fixed and why (Step 3 table); enclosed-mass, peak and V_max estimators and
  their spread; per-bin 2% systematic and scatter 0.11 against 0.16 dex; NFW conversion
  accuracy between definitions up to ν ≈ 2.5 (App. B); NFW against Einasto ~15%, V_max up to
  15% higher; Planck against WMAP5 ~20% (Eqs. 8–9); inter-model differences up to 20%
  (Sect. IV.2); three ways c(M) enters lensing fits — KiDS f_h, f_s (arXiv:2210.03110,
  Eq. 15, Sect. 4.3), Dark Emulator satellites only with the Diemer–Kravtsov relation
  (arXiv:1811.09504, App. G), f_conc bracket (arXiv:2202.07440, Sect. 4.1) — and the
  off-centring kernel. Baryons in hydrodynamical runs are covered only through the free
  normalisation and the f_conc bracket; the hydro papers are under "Not verified".
  **Y.**

**J2 — HOD forms per tracer; fitting to w_p and n with emulators or direct population;
HOD against CLF.**
- L2 (methods §6, §11 practice table): five-parameter form and the central condition
  (arXiv:2303.08752, Eqs. 51–52, Sect. 4.1); eBOSS ELG decaying central (arXiv:2007.09012);
  four DESI ELG central forms (arXiv:2306.06319, Eqs. 2–5); AbacusHOD fits of LRG and QSO
  over 0.15–32 h⁻¹Mpc (arXiv:2306.06314); MTHOD; CLF and its integration to an HOD
  (arXiv:astro-ph/0207019; arXiv:0807.4932); the One-Percent likelihood and covariance.
  Emulators against direct population, priors, the density term and the samplers are
  absent; BGS is not covered. **P.**
- L3: notation map between Zheng-type, SDSS and Aemulus forms and the QSO satellite term
  (arXiv:2306.06314, Eqs. 4–8; arXiv:1005.2413, Eq. 7; arXiv:1804.05867, Eq. 7); the
  nine-parameter CLF (arXiv:1207.0503, Eqs. 3–10) and why an HOD needs fewer priors
  (arXiv:1005.2413, Sect. II.3); seven prediction engines in a table with cost per call
  (arXiv:2110.11412, Sect. 4.4) and tabulation (arXiv:2306.06314, App. A); statistics and
  binning per analysis and why ξ(r_p, π); three number-density treatments; three
  covariance constructions including the model covariance (arXiv:2306.06319, Eq. 11);
  samplers and convergence; prior tables and what priors do (App. B); w_p degeneracies
  (arXiv:2110.11412, Sect. 5.2); GP surrogate against AbacusHOD on the same ELG data
  (arXiv:2306.06319, Sect. 7.3); Aemulus emulator error 0.9% (Sect. III). BGS is not
  covered here either. **Y.**

**J3 — SHAM set-up (property, scatter, incompleteness, orphans); SHMRs from abundance
matching, lensing (HSC, DES, COSMOS) and clustering compared, high-mass slope and
scatter.**
- L2 (methods §7): Vale & Ostriker, Conroy V_max,acc, Behroozi definition; Reddick v_peak
  with 0.20 dex (arXiv:1207.2160); Lehmann interpolation (arXiv:1510.05651); Moster,
  Behroozi, multi-epoch; COSMOS joint analysis (arXiv:1104.0928); DES Y3 SHMR formula
  (arXiv:2506.22367); results by survey are a pointer to `results.md`. **P.**
- L3: rank-order assignment (arXiv:1705.06347, Eq. 2); eight proxies and their effect on
  satellites (arXiv:1207.2160, Sect. III.2); v_α at the epoch of peak mass
  (arXiv:1510.05651, Eqs. 1–3); SMF nuisance model (arXiv:1001.0015, Eq. 1); three scatter
  implementations and why deconvolution is not used for errors (Eq. 17, Sect. III.4.2);
  satellite rules, disruption cuts and SHAMe orphans (arXiv:2012.06596, Eqs. 1–2);
  assembly bias through the proxy or the scatter; fits; v_peak against M_peak, the
  satellite deficit, EAGLE and TNG tests; Behroozi high-mass form (Eq. 21, δ = 0.5–0.6,
  γ = 1.3–1.7) and the stellar-mass systematic ~0.25 dex; scatter 0.20 and 0.17 dex from
  SDSS clustering. The comparison the question asks for — SHMR normalisation, high-mass
  slope and scatter from HSC, DES and COSMOS lensing against abundance matching and
  clustering — is not in the dossier, which points to `results.md#stellar-to-halo-mass-relation`.
  **P.**

**J4 — UniverseMachine, EMERGE, SAMs (Galacticus, SAGE, L-Galaxies), hydro (TNG, EAGLE,
FLAMINGO): calibration, predictions, when each is right for mocks or HOD tests.**
- L2 (methods §8): empirical-model table (age matching, EMERGE, UniverseMachine), SAM
  review, Munich, GALFORM, Shark, nIFTy scatter without recalibration (arXiv:1505.04607),
  Crain review, TNG DESI-like HODs (arXiv:2202.12911). What each is fitted with, at what
  cost, and when to choose which are absent; Galacticus, SAGE, EAGLE and FLAMINGO are
  not named. **P.**
- L3: halo layers (arXiv:1806.07893, Sect. 2.1; arXiv:1705.05373, Sect. 2.1;
  arXiv:1505.04607, Sect. 2); UniverseMachine SFR parameterisation and assembly by rank
  (Eqs. 2–18) and EMERGE efficiency and satellite quenching (Eqs. 5, 13, 15) with the data
  chosen per parameter group; orphan treatments (App. B.2, Eqs. 32–36); forward-modelled
  observational errors (Sect. 3.5, Eqs. 25–29); likelihoods, samplers and costs (400 000
  CPU hours; App. F); EMERGE model selection by Bayes factors (App. A.3); Shark tuning
  targets and the SMF choice propagating to a factor 1.4–8.5 at 10¹⁵ M_⊙
  (arXiv:1807.11180, Sect. 5.2); TNG300 DESI-like tracer extraction in five steps
  (arXiv:2202.12911, Sects. 2–3); diffsky transfer as a misspecification test
  (arXiv:2512.15962, Sect. III.4); "Choices and what they cost" for the three families;
  orphan excess against satellite lensing (arXiv:2312.04847, Sect. 5); hydro velocity bias
  and Poisson tests. Hydro rests on TNG300 only; Galacticus, SAGE and L-Galaxies are
  covered only as nIFTy participants without names; EAGLE and FLAMINGO are absent.
  **Y.**

**J5 — Galaxy against halo assembly bias; decorated HOD and secondary-property SHAM;
which detections survive projection and selection tests; cosmological bias if ignored.**
- L2 (methods §9; SKILL): vocabulary, halo-level results (Gao, Wechsler, Villarreal,
  Mansfield), shuffling (arXiv:astro-ph/0605636), Zentner mass-only HOD wrong (sizes in
  `systematics.md`), decorated HOD (arXiv:1512.03050), environment terms (arXiv:2010.04182),
  four detection strategies; SKILL: SDSS and CMASS detections, DESI DR1 Q_sat = 0.05 ±
  0.14, redMaPPer ratio 1.02 ± 0.14 from projection (arXiv:1611.00366). The
  implementations and their differences, and any size of the cosmological bias, are
  absent. **P.**
- L3: secondary properties and how each analysis ranks them (arXiv:2010.04182, Eqs. 4–6;
  arXiv:2110.11412, Sect. 2.4, Eq. 12; arXiv:1606.07817, Sect. 2.2); four implementations —
  mean-conserving decorated HOD (arXiv:1512.03050, Eqs. 15–30; arXiv:1606.07817, Eq. 5),
  pseudo-mass re-ranking, analytic mass-parameter modulation (arXiv:2110.11412,
  Eqs. 10–11), density-dependent slopes (arXiv:2511.01441, Eqs. 7–8); fit set-ups; the
  shuffling diagnostic in five steps with a rotation control and correlated re-ranking
  (arXiv:1911.02610, Sects. 3.1, 4.2); which property carries the signal (Δχ² by
  extension, Sect. 5.4; r = 0.2 for f_env); sign conventions; the DESI direct test and its
  mass range (arXiv:2510.20896, Eq. 9, Conclusions); consequence for lensing, predicted
  CMASS ΔΣ lowered by 10–20% (arXiv:2010.04182, Sect. 5.3; arXiv:2110.11412, Sect. 7.2);
  model predictions 15 ± 1% (TNG300) and SIMBA against TNG. Projection tests rest on the
  SKILL's redMaPPer line; the bias on cosmological parameters is given only as the
  lensing-prediction shift. **Y.**

**J6 — Satellite fractions and velocity bias: group catalogues, satellite kinematics,
small-scale RSD; group-finder purity and completeness; velocity bias in RSD fits.**
- L2 (methods §10): Yang finder and the self-calibrated finder in one sentence each
  (arXiv:0707.4640; arXiv:2610.20919); f_sat constraints and its degeneracy with scatter;
  More et al. factor-of-two agreement (arXiv:1003.3203); Basilisk (arXiv:2409.03105); CMASS
  velocity bias requirement (arXiv:1407.4811); satellite profile importance
  (arXiv:2512.14889). Purity and completeness and their propagation, and how velocity
  bias is parameterised and measured, are absent. **P.**
- L3: Yang finder in five steps with the B = 10 threshold tuned on f_c(1 − f_i)
  (arXiv:0707.4640, Sects. III.1–III.5, Eqs. 3–11); the self-calibrated finder's ten
  parameters and calibration on w_p and L_sat (arXiv:2610.20919, Sects. IV.1–IV.2,
  Eqs. 2–14); isolation cones (arXiv:1003.3203, Eq. 3; arXiv:2409.03105, Eq. 1); fibre
  collisions per analysis and lost-galaxy redshifts (App. A.2–A.3); stacked dispersions
  with satellite and host weighting (Eqs. 4–5) against the Basilisk forward model with
  interlopers, splashback and β (Sects. 4.2.4–4.2.5); fracturing, fusing and central
  inversion and their effect on f_sat and conformity across three finders
  (arXiv:1505.04798, Sects. 3.1, 4.3, 4.6, 6); purity and completeness numbers (SDSS DR4
  mock; DESI satellites 82.3% and 81.2% against SV3); α_c and α_s defined and tabulated
  (arXiv:1407.4811, Eqs. 10–11, Sect. 2.2.2), which statistics constrain them and why w_p
  matters (Sect. 3.2). **Y.**

**J7 (control, lensing is low).** L2 (methods §11; SKILL): definition from clustering-
trained CMASS models predicting lensing 20–40% high on r < 10 h⁻¹Mpc (arXiv:1611.08606);
the two strategies; explanations listed; the practice table with models, scales and
blinding for DESI DR1, HSC-Y1, BOSS × DES/HSC/KiDS and DESI One-Percent; SKILL: A = 0.79 ±
0.03 at Planck (arXiv:2202.07440), assembly bias, satellite segregation and baryons
(arXiv:2211.01744), UNIONS no significant effect, joint-fit S8 per survey. **Y.** L3
(`assembly-bias`): assembly-bias fits lower predicted CMASS ΔΣ by 10–20% (arXiv:2010.04182,
Sect. 5.3). **Y**, small gain on one explanation.

**J8 (control, mass function and bias).** L2 (methods §§2–3): Tinker 2008 and Sheth–Tormen
forms, the calibration table (Jenkins, Despali, Bocquet, Aemulus, Dark Emulator, Euclid,
Uchuu), FoF bias 10% below Δ = 200 and the Tinker 2010 bias fit with its Table 2; the
propagation into cluster counts is a pointer to `cosmo-clusters`, and into galaxy-bias
priors absent. **P.** L3 (`profiles-concentration`): concentration conversion between
definitions, not the mass function. **P**, no gain.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| J1 | P | Y | Y | yes |
| J2 | P | Y | Y | yes |
| J3 | P | P | Y | partial |
| J4 | P | Y | Y | yes |
| J5 | P | Y | Y | yes |
| J6 | P | Y | Y | yes |
| J7 (c) | Y | Y | Y | — |
| J8 (c) | P | P | Y | — |

**Verdict: pass.** L3 answers 5 of 6 with locators; 5 L2 failures answered; one dossier
per question; controls inert (J7 gains one explanation's size, J8 none). J3 fails at L3:
`deep/abundance-matching-shmr.md` covers how a SHAM or SHMR fit is built but leaves the
cross-method comparison of SHMRs (lensing against abundance matching and clustering, slope
and scatter at high mass) to `results.md`. Thin spots at L3: baryonic profile changes in
hydro runs (J1), BGS HODs (J2), named SAMs and EAGLE or FLAMINGO (J4), projection tests of
assembly-bias detections (J5, SKILL line only).

### Source checks (2 used)

- **E7** `deep/hod-clf.md`, Step 6, used in J2: the SDSS DR7 acceptance rule "written
  exp[−(χ²_new − χ²_old)]", with the dossier's [der] remark that it lacks the factor ½ of a
  likelihood ∝ exp(−χ²/2). arXiv:1005.2413, Sect. II.3: "The probability to accept the new
  set of HOD parameters is taken to be 1 if χ²_new ≤ χ²_old and exp[−(χ²_new − χ²_old)] if
  χ²_new > χ²_old … The length of the chain … is typically 10,000". Match on the quoted
  rule; the paper itself does not comment on the factor, so the remark stays the
  dossier's own inference, correctly flagged [der] and hedged ("should check which was
  used").
- **E8** `deep/satellites.md`, Numbers, used in J6: "satellites purity 82.3%, completeness
  81.2%; centrals 94.1%, 94.5% (against SV3, not mocks)". arXiv:2610.20919, App. A.3,
  Fig. 15 caption: "The overall satellite purity and completeness for HNN is 82.3% and
  81.2% respectively. The overall purity and completeness of centrals is 94.1% and 94.5%.
  Note that this comparison is to our SV3 'Truth' catalog, not a mock catalog, and so the
  true purity and completeness would include … general group finding systematics as shown
  in Paper I, which lowers these numbers somewhat." Match, caveat carried.

### Generality flags

- `deep/hod-clf.md` rests mostly on DESI One-Percent and AbacusHOD: arXiv:2306.06314,
  arXiv:2306.06319 and arXiv:2110.11412 carry 54 of 94 citations; SDSS DR7 (14), Aemulus
  (6), HSC × SDSS (7) and the SDSS CLF are the alternatives. No BGS HOD and no non-DESI
  simulation-based HOD framework (beyond Aemulus) is described.
- `deep/assembly-bias.md`: about half of 89 citations are to one group's papers
  (arXiv:2110.11412, arXiv:2010.04182, arXiv:1911.02610), with the decorated HOD
  (arXiv:1512.03050, arXiv:1606.07817) and SIMBA/TNG (arXiv:2511.01441) as the
  alternatives; balanced in method, CMASS-heavy in data.
- `deep/empirical-sam-hydro.md`: the hydro part rests on one simulation (TNG300,
  arXiv:2202.12911); EAGLE appears only in the SHAM dossier and FLAMINGO nowhere; SAMs
  are Shark and nIFTy, the Munich calibration paper is unread.
- `deep/profiles-concentration.md`, `deep/abundance-matching-shmr.md` and
  `deep/satellites.md` spread their citations over several groups and simulations. No
  flag.
