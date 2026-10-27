# Classification, redshift fitting, visual inspection and redshift success — cosmo-data-pipelines dossier

Scope: what a template redshift fitter actually fits (templates, redshift
grids, polynomials, priors, confidence flag), how the per-tracer "good
redshift" cut is chosen against a visual-inspection truth table, how VI is
run and merged, how redshift precision, accuracy and error calibration are
measured from repeats, and how redshift failures become catalogue weights;
compared across BOSS, eBOSS, DESI and Euclid.
Snapshot: 2026-10-17.
From: Guy et al. 2023, Sect. IV.12–IV.13; Bolton et al. 2012; DESI and
eBOSS survey-validation groups (copied from `references/subtopics.tsv`).

Already in L2, not repeated here: the family of fitters and after-burners
in one paragraph each
(`physics-and-methods.md#redshift-fitting-classification-and-visual`), the
success, purity and precision table by survey
(`results.md#spectroscopic-redshift-performance`), the catastrophic-failure
and error-calibration systematics
(`systematics.md#redshift-failures-and-catastrophic-redshifts`,
`systematics.md#redshift-error-calibration`), and the fitter debate
(`open-questions.md#redshift-fitters-fast-pca-templates-physical`). The
effect of redshift failures on BAO and RSD fits is in
`cosmo-galaxy-clustering` (systematics, Sect. 6).

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Fit every class on its own redshift grid
<!-- key: step-1-fit-every-class-on-its-own-redshift-grid -->

The common core is a linear least-squares fit of a template basis at each
trial redshift, giving a χ²(z) curve per class; the global minimum sets the
class and redshift.

**BOSS idlspec2d** (Bolton et al. 2012, arXiv:1207.7326) [src: Sect. III.1]:

| Class | Basis | Redshift range and step |
|---|---|---|
| Galaxy | 4 PCA eigenspectra + low-order polynomial | −0.01 < z < 1.0, one pixel (69 km s⁻¹) |
| Quasar | 4 PCA eigenspectra + polynomial | 0.0033 < z < 7.0, four pixels (276 km s⁻¹), refit at one pixel near the 5 best |
| Star | 123 archetype subclasses, one spectrum each | ±1200 km s⁻¹ |
| CV star | 3 eigenspectra | ±1000 km s⁻¹ |

The polynomial absorbs Galactic and intrinsic extinction and residual
spectrophotometric calibration errors, "typically at the 10% level"
[src: arXiv:1207.7326, Sect. III.1]. χ² is compared in reduced form χ²_r so that classes with
different numbers of basis vectors can be ranked; with ~4500 pixels this is
nearly the same as χ² [src: same]. Minima are refined by a quadratic through
the five nearest points (11 for quasars); minima closer than 1000 km s⁻¹ are
merged, because noise produces spurious minima ~200 km s⁻¹ apart
[src: same]. Pixels with sky residuals worse than 3σ of the Poisson model
(BADSKYCHI), sky brighter than flux plus 10σ (BRIGHTSKY), or negative flux
at > 10σ are masked first [src: same].

**DESI Redrock** (Guy et al. 2023, arXiv:2209.14482) [src: Sect. IV.12]:

| Class | Basis | Redshift grid |
|---|---|---|
| GALAXY | 10 PCA eigenvectors from 20,000 desisim spectra (10k ELG, 5k LRG, 5k BGS) built on stellar-population and emission-line models, 0 < z < 1.5 | logarithmic, 0.005 < z < 1.7 |
| QSO | 4 PCA eigenvectors, the SDSS idlspec2d set in that paper | logarithmic, 0.05 < z < 6.0 |
| STAR | 5 eigenvectors per subtype B, A, F, G, K, M, WD; 3 for CVs | linear, −0.002 < z < 0.002 (±600 km s⁻¹) |

Templates are resampled to the data wavelength grid and multiplied by each
spectrum's resolution matrix, so the data are never resampled; χ²(z) is
refined around the three lowest minima per class with a parabola
[src: same]. A χ² penalty is added for negative [O II] flux; no other
physical constraint is imposed [src: Sects. IV.12–IV.13]. For DR1 the QSO
templates were replaced by two eigenspectrum sets
(`results.md#history-what-superseded-what`).

**eBOSS redmonster** (Hutchinson et al. 2016, arXiv:1607.02432) fits
physical archetypes with additive polynomials; the polynomial order was set
empirically: failure rates of 9.5%, 20.9%, 14.2% and 12.9% for constant,
linear, quadratic and cubic terms led to a constant term, because higher
orders absorb real spectral features and lower the Δχ² separation between
templates [src: Sect. III.1].

**Euclid SPE** (Euclid Collaboration 2025, arXiv:2503.15308) works on
slitless spectra that mostly show one line: it computes a redshift PDF
with a prior that divides the PDF by 1000 outside 0.9 < z < 1.8, where Hα
is not observed, so that a lone line is read as Hα rather than [O II]
[src: Sect. 2.2]. Stated reason: at the survey depth [O II] emitters at
z > 2.2 are about 3.5 times fewer than Hα emitters in range, so the prior
raises the net success rate [src: same]. Only pixels from at least three
exposures are kept (the minimum for the sigma-clipped combination), and an
edge-calibration flag restricts Q1 to 0.9 < z < 1.8 [src: Sect. 2.1].

### Step 2. Attach a confidence statistic
<!-- key: step-2-attach-a-confidence-statistic -->

| Fitter | Statistic | Threshold and stated reason | Source |
|---|---|---|---|
| BOSS | Δχ²_r to the next solution > 1000 km s⁻¹ away | ZWARNING set if Δχ²_r < 0.01 absolute or < 0.01 × min χ²_r; 0.01 ≈ Δχ² 45 (naively 6.7σ) for ~4500 d.o.f.; the relative term makes the cut more conservative at high S/N where fits are worse in absolute terms but more discriminating | arXiv:1207.7326 [src: Sect. III.1] |
| BOSS galaxies | Z_NOQSO: same fit excluding QSO templates, absolute cut only | without the prior the code returns unphysical quasar fits for CMASS targets; excluding QSOs imposes the red, extended prior of the galaxy targeting | arXiv:1207.7326 [src: Sect. III.2] |
| eBOSS redmonster | Δχ²/dof, d.o.f. = n_pix − (n_poly + 1) | 0.005, needed for a < 10% failure rate; 0.01 gives 16.3% | arXiv:1607.02432 [src: Sect. III.2] |
| DESI Redrock | DELTACHI2 between the two lowest χ² across all classes; ZWARN bit if < 25 | 25 read as 5σ before systematics | arXiv:2209.14482 [src: Sect. IV.12]; arXiv:2503.14745 [src: Sect. III.1.2] |
| Euclid SPE | spe_z_prob: PDF integral within ±3σ of the peak | values below ~0.99 unreliable; the statistic is "highly non-linear" | arXiv:2503.15308 [src: Sect. 2.3] |

### Step 3. Build a truth table by visual inspection
<!-- key: step-3-build-a-truth-table-by-visual-inspection -->

DESI galaxy VI procedure (Lan et al. 2023, arXiv:2208.08516)
[src: Sect. II]:

1. Each spectrum has at least two inspectors.
2. Each reports redshift, quality 0–4, type (star, galaxy, quasar),
   artefacts and comments.
3. Reports merge automatically if all pairs agree within
   dz_VI = |z_i − z_j|/(1 + z_i) < 0.0033 (990 km s⁻¹, Eq. 1), quality
   within 1, and the same type; final redshift and quality are the means
   [src: arXiv:2208.08516, Sect. II].
4. Otherwise a merger re-inspects.

Quality scale [src: arXiv:2208.08516, Sect. II]: 4 = two or more secure features; 3 = one secure
feature plus continuum or many weak features; 2 = one strong feature of
uncertain identity; 1 = signal without identified features; 0 = no
signal. A robust VI redshift has mean quality ≥ 2.5. VI was run on deep
co-adds (about ten times nominal exposure), and a first campaign of ~17,000
spectra from an early reduction was followed by a second after artefacts
were found [src: Sect. III].

BOSS truth table: 4864 galaxy spectra on eight plates inspected by one
person; impurity defined as a confident pipeline galaxy redshift that VI
confidently places more than Δz = 0.005 away [src: arXiv:1207.7326,
Sect. V.1].

### Step 4. Choose the good-redshift cut on the truth table
<!-- key: step-4-choose-the-good-redshift-cut-on-the -->

Lan et al. define, at main-survey depth (Eqs. 4–5) [src:
arXiv:2208.08516, Sect. IV.2]:

- good-redshift inclusion fraction = N(dz < 0.0033, VI quality ≥ 2.5,
  passes cut) / N(dz < 0.0033, VI quality ≥ 2.5) [src: arXiv:2208.08516, Eq. 4];
- good-redshift purity = N(dz < 0.0033, VI quality ≥ 2.5, passes cut) /
  N(passes cut) [src: arXiv:2208.08516, Eq. 5];

with dz = |z_VI − z_Redrock|/(1 + z_VI) (Eq. 3), Redrock stars excluded.
The cut is the point on the inclusion–purity curve the survey accepts.
The DR1 cuts and stated reasons (DESI 2024 II, arXiv:2411.12020) [src: Sect. 3]:

| Tracer | Cut | Reason given |
|---|---|---|
| BGS | ZWARN = 0, Δχ² > 40 | purity near 100% for bright and faint [src: arXiv:2208.08516, Sect. IV.2] |
| LRG | ZWARN = 0, Δχ² > 15 | inclusion and purity > 99% [src: arXiv:2208.08516, Sect. IV.2] |
| ELG | log₁₀ S_[OII] + 0.2 log₁₀ Δχ² > 0.9, S_[OII] the [O II] doublet S/N | many ELG spectra have only [O II] and no continuum, so low Δχ² but a robust line; a joint cut beats Δχ² alone [src: arXiv:2208.08516, Sect. IV.2] |
| QSO | not rejected by the quasar catalogue: QSO by Redrock, Mg II fit or QuasarNET | only tracer whose success depends on spectral type, which complicates systematics modelling [src: arXiv:2411.12020, Sect. 3] |

For the galaxy tracers the Redrock spectral type does not enter: an LRG
target fitted as QSO or star but passing the cut counts as a success
[src: arXiv:2411.12020, Sect. 3]. The QSO redshift is taken from the first
tile on which the quasar was observed, which changes the success rate by
~0.1% and simplifies its modelling [src: same].

DESI quasar "QSO maker" logic (Alexander et al. 2023, arXiv:2208.08517)
[src: Sect. III.3]: a target is a QSO if any of Redrock, the Mg II
after-burner or QuasarNET says so; Redrock is rerun with only QSO templates
and a top-hat prior of width dz = 0.05 around the QuasarNET redshift when
QuasarNET finds a QSO missed by Mg II, or when the two redshifts disagree by
dz > 0.05. Missed quasars at z < 1 are mostly correct redshifts classified
as galaxies (low-luminosity, Seyfert-like); at z > 1.7 they are mostly
catastrophic failures [src: Sect. V.1].

Euclid's cosmology-like selection: Hα flux > 2 × 10⁻¹⁶ erg s⁻¹ cm⁻², S/N >
3.5, line width < 680 km s⁻¹, plus a spe_z_prob threshold; 80% success at
spe_z_prob ≥ 0.996 with SPE classification alone, 80% at 0.985 and 89% at
0.999 for objects classed as galaxies by both SPE and DESI, over
0.9 < z < 1.6 where both are reliable [src: arXiv:2503.15308, Sect. 6.2].
The design requirement is 45% completeness and 80% purity for Hα S/N > 3.5
and FWHM ≤ 0.5″ [src: Sect. 2.2].

### Step 5. Measure precision, accuracy and error calibration on repeats
<!-- key: step-5-measure-precision-accuracy-and-error -->

- **Precision.** Pairs of independent main-depth spectra of one target:
  dv_ij = c (z_i − z_j)/(1 + z_i); reported MAD × 1.4828/√2, the √2
  because each difference holds two errors (Eq. 8) [src: arXiv:2208.08516,
  Sect. IV.4].
- **Error calibration.** Repeat differences divided by the quadrature sum
  of the quoted errors, histogram fitted by a Gaussian; σ = 1 means
  correct errors. BOSS: 27,170 CMASS and 7503 LOWZ repeats give 1.19 and
  1.34; the larger LOWZ value suggests systematics matter more at high S/N
  [src: arXiv:1207.7326, Sect. V.2]. eBOSS: σ = 0.65, μ = 0.01 on
  extra-deep plates split to normal depth, so errors are to be divided by
  1.54 [src: arXiv:1607.02432, Sect. IV.3].
- **Error distribution.** DESI LRG, ELG and QSO redshift errors are better
  fitted by a Lorentzian than a Gaussian (QSO: or three Gaussians)
  [src: arXiv:2411.12020, Sect. 7.2].
- **Accuracy.** Against external redshifts (BOSS, DEEP2) for galaxies; for
  quasars, from the radial offset of the peak of small-scale
  cross-correlations with LRG, ELG and the Lyα forest: 30–60 km s⁻¹ at
  0.8 < z < 2.1 [src: arXiv:2411.12020, Sect. 7.2].
- **Catastrophics.** From VI (rates for quasars at 1000 and 3000 km s⁻¹
  thresholds) and from repeats (BOSS: 44 CMASS repeats with |Δz| > 0.005,
  0.16%, mostly superpositions, artefacts and type-II quasars)
  [src: arXiv:2411.12020, Sect. 7.2; arXiv:1207.7326, Sect. V.2].

### Step 6. Turn failures into a weight
<!-- key: step-6-turn-failures-into-a-weight -->

DESI models the success rate G_z against TSNR2, the template S/N squared
of the coadd for that tracer, which uses a fixed template and the estimated
noise and so tracks effective observing time, not the target's brightness
[src: arXiv:2411.12020, Sect. 7.1]. For BGS, LRG and QSO, G_z is an error
function of TSNR2 at fixed fibre flux φ_fib, and

w_zfail(S_ratio, φ_fib) = G_z(∞, φ_fib) / G_z(S_ratio, φ_fib) (Eq. 5),

with S_ratio the TSNR2 value [src: arXiv:2411.12020, Sect. 7.1]. For ELGs, success depends on the
exact redshift because sky lines hide [O II], so a linear relation in
TSNR2_ELG is fitted at each redshift and normalised to mean one
[src: same]. Stated reason for the asymptotic form: it corrects only the
variation with observing depth, not the absolute failure rate; QSOs at low
fibre flux have ~30% success and are up-weighted for the ~10% variation, not
by a factor ~3 [src: same].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### PCA templates, physical archetypes or networks
<!-- key: pca-templates-physical-archetypes-or-networks -->

- **PCA (Redrock).** Fast and flexible, but nothing makes the best fit
  physical, so upstream defects (background, arm-to-arm steps) produce
  false fits [src: arXiv:2209.14482, Sect. IV.13]. The DESI galaxy and
  stellar templates were built for DESI while the QSO templates were
  BOSS's, trained on a few hundred spectra; improving QSO templates first
  degraded galaxy completeness [src: same].
- **Archetype refit** (Anand et al. 2024, arXiv:2405.19288): after the PCA
  scan, the N best redshifts are refitted with one physical archetype
  (α_k > 0) plus Legendre polynomials per camera (Eq. 1), so 1 + 3(d+1)
  coefficients [src: Sect. III.1]. A Gaussian prior σ_a = 0.1 on the
  polynomial coefficients (Eq. 3) stops them absorbing quasar power-law
  slopes, which would misclassify quasars as galaxies, and lowers confident
  fits on sky fibres; the value matches the 0.1–0.5 spread of coefficients
  on 339,712 Y1 sky spectra [src: Sect. III.2]. The archetypes are chosen
  by set cover on s²_red, with one threshold for all galaxy types because
  galaxy spectra have no sharp class boundaries [src: Sect. III.4]. Cost:
  it cannot recover a redshift absent from the PCA short list, and its
  precision is Redrock's [src: Sect. III.1]. Result on Y1 sky fibres:
  6–40% fewer false positives, e.g. 5808 → 4275 under the LRG cut
  (Table 5) [src: Sect. IV.4.1]; the L2 range "5–40%" is the abstract's.
- **Networks.** QuasarNET is used as an after-burner, not a replacement
  [src: arXiv:2209.14482, Sect. IV.12].

### One Δχ² cut or a tracer-specific statistic
<!-- key: one-chi2-cut-or-a-tracer-specific-statistic -->

A single Δχ² fails for emission-line galaxies, whose redshift rests on one
line without continuum; DESI combines line S/N with Δχ² [src:
arXiv:2208.08516, Sect. IV.2]. Euclid, with one line per spectrum, uses a
PDF-peak probability with a line-identity prior [src: arXiv:2503.15308,
Sects. 2.2–2.3]. BOSS used a priori class exclusion (NOQSO) instead of a
tracer-specific statistic [src: arXiv:1207.7326, Sect. III.2].

### Polynomial freedom
<!-- key: polynomial-freedom -->

Polynomials absorb calibration errors but also real features; redmonster
found the constant term best [src: arXiv:1607.02432, Sect. III.1]; the
archetype refit allows polynomials per camera but regularises them [src:
arXiv:2405.19288, Sect. III.2]; BOSS allowed a low-order polynomial for
~10% calibration errors [src: arXiv:1207.7326, Sect. III.1].

### Sky fibres as a false-positive test
<!-- key: sky-fibres-as-a-false-positive-test -->

redmonster used the ~10% of plate fibres on blank sky as a proxy for
catastrophic failures in the low-S/N limit: a factor seven fewer confident
sky redshifts than spectro1d at a given threshold [src:
arXiv:1607.02432, Sect. III.2]. DESI inspects sky-fibre redshifts in daily
quality assessment [src: arXiv:2405.19288, Sect. IV.4.1].

### Why VI earns its cost
<!-- key: why-vi-earns-its-cost -->

VI found that 1–2% of BGS spectra in an early reduction had a spurious
z-band flux excess from neighbouring fibres on bright stars, mimicking a
4000 Å break; modelling it cut BGS catastrophic failures by a factor three.
It also found ~0.5% of spectra hit by an unmasked CCD region near 8000 Å
[src: arXiv:2208.08516, Sect. V].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Redrock GALAXY basis | 10 eigenvectors from 20,000 simulated spectra | DESI | arXiv:2209.14482 | Sect. IV.12 |
| ZWARN Δχ² flag | < 25 | DESI | arXiv:2209.14482 | Sect. IV.12 |
| BOSS Δχ²_r threshold | 0.01 (≈ Δχ² 45) | BOSS DR9 | arXiv:1207.7326 | Sect. III.1 |
| redmonster threshold | Δχ²/dof 0.005 | eBOSS LRG | arXiv:1607.02432 | Sect. III.2 |
| VI merge tolerance | dz < 0.0033 (990 km s⁻¹), quality within 1 | DESI SV | arXiv:2208.08516 | Sect. II, Eq. 1 |
| Robust VI redshift | mean quality ≥ 2.5 | DESI SV | arXiv:2208.08516 | Sect. II |
| Redshift recovery rate at main depth | BGS bright 98.1 ± 0.3%, faint 99.4 ± 0.3%, LRG 98.9 ± 0.2%, ELG LOP 93.8 ± 0.2%, ELG VLO 97.5 ± 0.3% | DESI SV | arXiv:2208.08516 | Sect. IV.1 |
| Inclusion / purity after cut | BGS bright 97.2% / 100%; LRG 99.2% / 99.6%; ELG LOP 94.3% / 99.6% | DESI SV | arXiv:2208.08516 | Table 3 |
| Precision (MAD) | BGS 9.2 km s⁻¹, LRG 36.7, ELG LOP 6.8 | DESI SV | arXiv:2208.08516 | Table 3 |
| DR1 success, observed targets | BGS 98.9%, LRG 99.1%, ELG 72.7%, QSO 66.8% | DESI DR1 | arXiv:2411.12020 | Table 2 |
| QSO VI recovery | standard 85.5 ± 0.5%, modified 93.6 ± 0.4% | DESI SV main selection | arXiv:2208.08517 | Table 8 |
| QSO purity (dz = 0.0033 / 0.010) | standard 94.0% / 98.6%; modified 93.3% / 99.0% | DESI SV | arXiv:2208.08517 | Table 9 |
| QSO precision, NMAD | 57 km s⁻¹ overall; ~20 at z ~ 0.8 to ~125 at z ~ 1.8 | DESI SV repeats | arXiv:2411.12020 | Sect. 7.2 |
| QSO catastrophics (> 3000 / > 1000 km s⁻¹) | 0.7% / 4.5% at z < 2.1; 1.8% / 12.2% at z > 2.1 | DESI SV (old templates) | arXiv:2411.12020 | Sect. 7.2 |
| ELG catastrophics | 0.27% with Δv beyond ±1000 km s⁻¹ | DESI DR1 | arXiv:2411.12020 | Sect. 7.2 |
| LRG vs BOSS | 0.3% differ by > 0.002; mean offset 4 km s⁻¹ | DESI DR1 | arXiv:2411.12020 | Sect. 7.2 |
| BOSS error scaling | 1.19 (CMASS), 1.34 (LOWZ) | BOSS DR9 | arXiv:1207.7326 | Sect. V.2 |
| eBOSS error scaling | 0.65 | eBOSS LRG | arXiv:1607.02432 | Sect. IV.3 |
| BOSS CMASS impurity | ~0.2% (truth table); 0.16% (repeats) | BOSS DR9 | arXiv:1207.7326 | Sects. V.1–V.2 |
| Euclid Q1 processed spectra | 3.8M of 5.1M H_E ≤ 22.5 objects; ~100,000 expected Hα redshifts in range | Euclid Q1 | arXiv:2503.15308 | Sect. 2.1 |
| Archetype prior σ_a | 0.1 | DESI Y1 | arXiv:2405.19288 | Sect. III.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Calibration steps read as spectral breaks.** Fibre cross-talk or arm
  steps mimic a 4000 Å break or a line. Test: VI of deep co-adds, sky-fibre
  redshifts [src: arXiv:2208.08516, Sect. V; arXiv:2405.19288,
  Sect. IV.4.1].
- **Unphysical template combinations at low S/N.** BOSS CMASS fitted as
  quasars; PCA fits of sky spectra with high Δχ² [src: arXiv:1207.7326,
  Sect. III.2; arXiv:2405.19288, Sect. III.2]. Test: refit without the
  suspect class or with physical archetypes and compare.
- **Line confusion.** Broad [O III] taken as Hα in type-II quasars (BOSS);
  [O II] taken as Hα in Euclid [src: arXiv:1207.7326, Sect. V.2;
  arXiv:2503.15308, Sect. 2.2]. Test: repeats with |Δz| > 0.005; external
  redshifts.
- **Quasars missed by templates.** Red, low-luminosity quasars classified
  as galaxies [src: arXiv:2208.08517, Sect. V.1]. Test: after-burner
  union scored on VI.
- **Thresholds that drift with S/N.** An absolute Δχ² cut is looser at high
  S/N where template mismatch dominates; BOSS added a relative cut for this
  [src: arXiv:1207.7326, Sect. III.1].
- **Formal errors taken at face value.** Off by 1.19–1.34 (BOSS) and 0.65
  (eBOSS) [src: arXiv:1207.7326, abstract, Sect. V.2; arXiv:1607.02432, Sect. IV.3].
  Test: repeat-difference histogram scaled by quoted errors.
- **Success depending on conditions.** Up-weighting the absolute failure
  rate over-corrects; DESI weights only the TSNR2 dependence at fixed fibre
  flux, and for ELGs the redshift-dependent sky-line effect
  [src: arXiv:2411.12020, Sect. 7.1]. Test: weighted density flat against
  TSNR2 in fibre-flux bins.
- **Type-dependent success (QSO).** Mixing classifiers makes the
  failure model depend on class decisions [src: arXiv:2411.12020, Sect. 3].

## Reading list
<!-- key: reading-list -->

- Foundation: Bolton et al. 2012, arXiv:1207.7326 — χ² scan, Δχ²_r with a
  relative term, NOQSO, truth table and repeat calibration.
- Method: Guy et al. 2023, arXiv:2209.14482, Sects. IV.12–IV.13 — Redrock
  templates, grids, warning flags, limitations.
- Method: Hutchinson et al. 2016, arXiv:1607.02432 — how to set polynomial
  order and Δχ² threshold; sky fibres as a false-positive test.
- Validation: Lan et al. 2023, arXiv:2208.08516 — VI protocol, quality
  scale, inclusion and purity definitions, precision from repeats.
- Validation: Alexander et al. 2023, arXiv:2208.08517 — quasar VI and the
  after-burner combination.
- Application: DESI 2024 II, arXiv:2411.12020, Sects. 3, 7 — DR1 cuts,
  redshift-failure weights, precision and accuracy summary.
- Alternative: Anand et al. 2024, arXiv:2405.19288 — archetype refit with
  regularised polynomials.
- Slitless: Euclid Collaboration 2025, arXiv:2503.15308 — line-identity
  prior, PDF probability, success against DESI.

## Not verified
<!-- key: not-verified -->

- Redrock reference paper (in preparation per DESI DR1) not read.
- DESI DR2 cuts or weight changes: no DR2 catalogue paper read.
- QuasarNET and Mg II after-burner thresholds (Chaussidon et al. 2023,
  Fig. 9 flowchart) not read.
- GAMA autoz figure-of-merit calibration beyond the L2 summary not read.
