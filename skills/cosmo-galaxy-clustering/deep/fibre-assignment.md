# Fibre assignment: alternative realisations, inverse-probability weights and their validation — cosmo-galaxy-clustering dossier

Scope: how the alternative fibre-assignment realisations behind PIP weights
are generated (altMTL on data and mocks, the fast emulator FFA for
covariance mocks), how individual and pairwise inverse-probability weights,
angular up-weighting and the zero-probability correction are computed,
how each mitigation is validated, and how to choose between completeness
weights, θ-cut and PIP for a given analysis.
Snapshot: 2026-10-19.
From: DESI 2024 II (arXiv:2411.12020), Sect. 5 (copied from
`references/subtopics.tsv`).

Already in L2 or a sibling, not repeated here: the mechanism, DR1/DR2
completeness per tracer, the BAO and full-shape sizes and the θ-cut
full-shape test (`systematics.md#fibre-assignment-and-fibre-collisions`);
the SDSS-era history of collision corrections
(`physics-and-methods.md#fibre-assignment-weights`); the DESI f_TLID and
f_tile completeness weights, the eBOSS close-pair weight and DESI's stated
reasons for not using PIP as DR1 baseline
(`cosmo-data-pipelines/deep/lss-catalogues.md`, Step 3 and "Close-pair
weights or PIP"); the θ-cut window and its rotation
(`deep/estimators-window.md`, Step 6 and "Hard θ-cut or apodised cut");
the open question of PIP in DR2 full shape
(`open-questions.md#fibre-assignment-at-small-scales`).

Notation. K: number of alternative realisations (replicas); c_i: number of
replicas in which galaxy i is assigned (its "recurrence"); c_ij: number in
which both i and j are assigned; N_bits: length of the bitwise weight
(N_bits = K in DESI). IIP: individual inverse probability; PIP: pairwise
inverse probability. n_tile: number of tiles that could reach a target.
DD, DR, RR: data–data, data–random, random–random pair counts.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Generate alternative assignments that follow the real survey history
<!-- key: step-1-generate-alternative-assignments-that -->

The only random input to DESI fibre assignment is the SUBPRIORITY of each
target (uniform in [0, 1]), which resolves conflicts between targets of
equal PRIORITY; rerunning `fiberassign` with new SUBPRIORITY values
samples the assignment probability [src: arXiv:2411.12025, Sect. 3.1;
arXiv:2404.03006, Sect. 4.2]. Because DESI updates its merged target
ledgers (MTLs) between passes, and a successful observation lowers a
target's priority, one changed assignment changes all later ones. The
alternative-MTL (altMTL) pipeline therefore replays the survey
[src: arXiv:2404.03006, Sects. 4.2–4.4]:

1. Truncate the MTLs to their initial entries and replace SUBPRIORITY with
   new random numbers seeded by HEALPix pixel, realisation number and a
   user seed (the SV3 run omitted the pixel from the seed) [src: Sect. 4.3].
2. Re-draw the random promotions: 20% of BGS_FAINT to the higher-priority
   class, and in the main survey 10% of ELGs to ELG_HIP [src: same].
3. Process tiles date by date in survey order, with the same sky fibres,
   standards, secondary targets and hardware state as the real run
   [src: Sect. 4.4].
4. Give each alternative target the observation outcome of whichever
   target the same fibre observed in reality, so positioner failures and
   bad-hardware flags enter automatically. The outcome can come from
   another target class; the fraction of observations whose primary target
   information changes is 6.7% (SV3) and 13.0% (Y1) of dark-time
   observations [src: Sect. 4.4]. For quasars, whose redshift sets the
   number of further visits, this is "not exactly correct"; a "twin fibre"
   scheme and, for the final sample, substitution of final QSO redshifts
   are planned [src: same].
5. Separate the assignment and MTL-update steps so that reprocessed tiles
   (changed redshift outcomes) can be replayed [src: same].

Validation of the pipeline: with randomisation switched off, one
realisation reproduces SV3 and Y1 exactly; the promotions are
statistically equivalent [src: Sect. 4.6].

Number of realisations [src: Sect. 4.3, Table 4, Figs. 3–4]: 128 for data
and 256 for SV3 mocks, chosen from the convergence of the zero-probability
fraction. After 128 realisations the zero-probability fraction is 0 to
3 × 10⁻³ % in SV3 but 0.17% to 0.28% in Y1 (ELG 0.17%, BGS_BRIGHT 0.21%,
LRG 0.22%, QSO 0.28%), and the Y1 trend shows it would be "prohibitive"
to remove them by more realisations. DR1 used K = 128 replicas plus the
real one, for data and for one Abacus mock only (mock 11), because
`fiberassign` is expensive [src: arXiv:2411.12025, Sect. 7].

For comparison, eBOSS used 1860 runs of its tiling code for the DR16 data
(the first being the real one) and 310 per mock; collisions in groups of
more than two targets are resolved by an optimisation, not randomly,
which creates zero-probability pairs near the collision scale [src:
arXiv:2007.09005, Sect. 4.4].

### Step 2. For covariance mocks, emulate assignment instead (FFA)
<!-- key: step-2-for-covariance-mocks-emulate-assignment -->

Running altMTL on 1000 covariance mocks is impossible, so DESI built a
shallow emulator ("fast fibre assignment", FFA) [src: arXiv:2411.12025,
Sect. 3.2]:

- Inputs: all potential targets with their n_tile. A friends-of-friends
  group finder on angular separation, linking angle θ_LL, isolates groups
  of assignment-entangled galaxies; for each galaxy the close-friend count
  n_CFC is the number of companions within θ_LL.
- Kernel: F(n_CFC, n_tile) = fraction assigned among targets with those
  values, learnt from a reference run of `fiberassign` (trained on the real
  data for DR1).
- Sampling: each galaxy is drawn assigned in N_bit replicas with
  probability F (N_bit should be at least O(100)).
- Anticorrelation: within each FOF group, bits are permuted to maximise
  the anticorrelation of assigned pairs while conserving each galaxy's
  count; a fraction f_anti of bits is then swapped at random to tune it.
  A tilt β_tilt of F along n_CFC was used only for BGS, whose pre-assignment
  mocks are less dense than the data.
- DR1 settings: θ_LL = 0.02°, f_anti = 0.1; one tracer at a time; K = 256
  replicas for each of 25 Abacus mocks; IIP weights w = (c + 1)/(K + 1)
  as written in Sect. 3.2 [src: Sects. 3.2, 7].

Stated reason for a shallow model rather than a neural network: few,
interpretable parameters and less sensitivity to a small training set
[src: Sect. 3.2].

### Step 3. Turn the realisations into weights
<!-- key: step-3-turn-the-realisations-into-weights -->

Bitwise weights [src: arXiv:1703.02070, Sect. 6.3, Eq. 14]: store for each
galaxy the binary array of its selections, w^(b); the pair weight is

w_mn = N_bits / popcnt[w^(b)_m AND w^(b)_n] (Eq. 14),

so storage scales with N_gal, not N_gal². In practice the IIP weight
w_n = N_bits/Σ_i s_i^(n) is evaluated first and Eq. 14 is applied only when
both IIP weights exceed 1; DR pairs need only IIP weights, so PIP is
slower only when DD dominates the cost [src: same, footnote 6].

DESI DR1 refinement [src: arXiv:2411.12025, Sect. 5.2, Eqs. 8–11]:

- Efficient estimator of 1/p, w^eff = (K + 1)/(c + 1) (Eq. 8), with K the
  number of replicas excluding the true realisation; adopted because it
  converges fastest with K, which matters with limited computing.
- Expected pair weight under independent selection,
  g_K(c_i, c_j) = Σ_{c_ij} [(K + 1)/(c_ij + 1)] P_K(c_ij | c_i, c_j)
  (Eq. 10), with the hypergeometric P_K of Eq. 9.
- Pair weight w^PIP_ij = w^eff_i w^eff_j w^eff_ij / g_K(c_i, c_j) (Eq. 11):
  two individual factors and one purely pairwise factor. Stated reason for
  putting g_K in the pair count rather than in the normalisation (the
  earlier recipe): it removes residual scale-dependent effects from the
  clustering of low-probability objects. g_K needs only K(K + 1)/2
  evaluations.
- IIP weights are w^IIP = w^eff unless otherwise stated.

Fourier space, hybrid IIP–PIP [src: Sect. 5.2, Eqs. 6–7]: P_ℓ^PIP =
P_ℓ^IIP plus a pair sum over A_ij j_ℓ(k s_ij) L_ℓ(ŝ_ij·η̂_ij) (Eq. 6),
A_ij = w^PIP_ij − w^IIP_i w^IIP_j (Eq. 7), restricted to pairs below
θ_max. This is exact if an angle θ_ind exists above which assignments are
independent.

### Step 4. Restore zero-probability pairs and galaxies
<!-- key: step-4-restore-zero-probability-pairs-and -->

PIP is unbiased only for pairs with non-zero probability [src:
arXiv:1703.02070, Sect. 6.1]. Two corrections:

- **Angular up-weighting** [src: arXiv:1703.02070, Eq. 13;
  arXiv:2411.12025, Sect. 5.2.1, Eqs. 12–13]: multiply DD by
  a_DD(θ) = DD_ref/DD_dep. The original recipe takes the parent sample
  restricted to the clustering redshift range as reference, and the
  observed sample as depleted. DESI DR1 uses DD^full (all targets, no
  redshift cut) over DD^full_PIP (PIP-weighted assigned targets, with or
  without a good redshift), so the factor measures pairs lost to
  assignment alone, unaffected by photometric-redshift scatter or
  redshift failures. Counts are normalised to total pairs so that ξ and P
  normalisations are untouched. In Fourier space
  A_ij = a_DD(θ_ij) w^PIP_ij − w^IIP_i w^IIP_j (Eq. 13), the first
  application of angular up-weighting to P(k); the DR correction was
  negligible. The assumption: the unobserved pairs cluster like observed
  pairs at the same angle [src: Sect. 5.2.1]. eBOSS applies up-weighting
  to DD and DR (its Eqs. 8–9) and warns that tile overlaps correlated with
  target density can violate that assumption [src: arXiv:2007.09005,
  Sect. 4.3].
- **w_NTMP** [src: arXiv:2411.12025, Sect. 5.2.2]: in DR1 about 2.5 × 10⁵
  NGC ELG targets have zero probability; they trace the completeness
  pattern (hence n_tile) and bias angular counts by about 1% on large
  scales. f_NTMP(n_tile) = Σ w_IIP over assigned galaxies of the full
  sample with that n_tile, divided by the number of full-sample galaxies
  with that n_tile; 1 − f_NTMP estimates the zero-probability fraction. It
  is applied as a random weight f_NTMP (or galaxy weight 1/f_NTMP).
  Stated reasons: Σ w_IIP rather than a count also absorbs unidentified
  effects; on the randoms the larger density lowers noise; it lets PIP be
  used in Fourier space without up-weighting at large θ.
  (w_comp, f_tile) and (w_IIP, f_NTMP) play analogous roles [src: same].

Settings used in DR1 measurements [src: Sect. 7]: up-weighting below
θ_max = 0.2° for ξ and PIP plus up-weighting below 0.25° for P(k); "thanks
to w_NTMP weights" the choice does not affect results as long as θ_max
exceeds the collision window.

### Step 5. Or cut the small angles (θ-cut)
<!-- key: step-5-or-cut-the-small-angles-theta-cut -->

Requirements stated for a θ-cut [src: arXiv:2411.12025, Sect. 6.1]: θ_cut
small enough to lose little information; an unbiased individual-weight
correction above it; tractable in estimator and model. θ_cut = 0.05° is
the DESI positioner patrol diameter, the angle below which incompleteness
affects the pair counts of all samples; positioner-body collisions act at
about 0.01° [src: arXiv:2406.04804, Sect. 2.3]. At z = 1, 0.05° is about
3 h⁻¹ Mpc transverse, against the ≳ 30 h⁻¹ Mpc (k ≲ 0.2 h Mpc⁻¹) used in
full shape [src: arXiv:2411.12025, Sect. 6.1]. In P(k) the cut is Eq. 6
with A_ij = −w_i w_j, applied to randoms too; its effect is purely
geometric and goes into the window (Eq. 14) [src: same]. The rotated
window is in `deep/estimators-window.md`.

### Step 6. Validate on mocks with the real assignment
<!-- key: step-6-validate-on-mocks-with-the-real -->

Reference: the "complete" sample (all potential targets of a class) of
the same mock [src: arXiv:2411.12025, Sect. 7]. DR1 test setup: Abacus
mock 11, NGC only (SGC compatible, noisier); ξ in linear 4 h⁻¹ Mpc bins
and logarithmic bins below 20 h⁻¹ Mpc; P(k) on a 1024³ mesh, CIC with
interlacing, Δk = 0.005 h Mpc⁻¹; no FKP weights, to isolate fibre effects;
small-scale ξ errors from 7 FFA mocks with PIP + up-weighting, fitted by a
power law, called "a convenient method for normalizing and visualizing"
rather than true confidence intervals [src: same]. Four schemes compared:
completeness (fiducial), IIP, PIP, PIP + angular up-weighting.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

| Scheme | Assumes | Buys | Costs | Used by |
|---|---|---|---|---|
| Completeness weights (f_TLID, f_tile) | targets competing for a fibre are equivalent | cheap, available for 1000 mocks | biased for close pairs | DESI DR1 and DR2 BAO, alone; DR1 full shape with θ-cut |
| IIP | θ_ind exists | unbiased above θ_ind | not below θ_ind | building block |
| PIP | every pair has p > 0 | unbiased where p > 0 | K realisations; zero-probability pairs remain | eBOSS (1860 runs); DESI SV3 and DR1 small-scale studies |
| PIP + angular up-weighting (+ w_NTMP) | missing pairs cluster like observed ones at equal θ | most accurate in every DR1 case tested, ξ and P | needs full target sample and bitweights; one altMTL mock only | DESI DR1 characterisation; proposed for later releases |
| θ-cut + window | individual weights unbiased above 0.05° | robust to how assignment is simulated in mocks | discards < 0.05° pairs; non-compact window to rotate | DESI DR1 full shape |

[src: arXiv:2411.12025, Sects. 5–8; arXiv:2406.04804, Sect. 2.3;
arXiv:2007.09005, Sects. 4.4, 7]

Outcome of the comparison [src: arXiv:2411.12025, Sect. 8]: "PIP weights
with angular upweighting deliver the most accurate estimates of the 'true'
clustering, in all scenarios considered, both in configuration and Fourier
space, and for all types of tracers"; the companion paper shows the θ-cut
reaches similar performance with completeness weights. The θ-cut makes the
analysis "robust to the forward modelling of the fiber assignment in mock
catalogs" [src: arXiv:2406.04804, Sect. 2.3], which is its main argument
when mocks and data differ.

**Reconstruction.** For BAO the θ-cut is "less effective, due to the
transfer of small-scale incompleteness to larger scale" through the
displacement field; DR1 BAO used completeness weights alone because no
further correction was needed [src: arXiv:2411.12025, Sect. 8]. In DR2
fibre assignment was not re-evaluated; the test is unbiased BAO recovery
on realistic mocks [src: arXiv:2503.14742, Sect. V.2].

**altMTL or FFA mocks.** altMTL are realistic and passed all tests against
the data, but cost limits them to a handful [src: arXiv:2411.12025,
Sect. 8]. FFA reproduces the angular completeness and n(z) of altMTL (total
assigned 2.44 versus 2.41 million ELGs, 2.15 versus 2.16 million LRGs,
0.86 million QSOs in both; assigned fractions 0.20, 0.56, 0.58) [src:
Sect. 4.2, Table 2], but has fewer zero-probability pairs and a weaker
collision window [src: Sect. 8]; altMTL weights show a shorter high-weight
tail and more weights equal to one, most visibly for ELGs [src:
Sect. 4.2]. FFA is how the DR1 full-shape P(k) covariance was obtained, and
is one suspected cause of its roughly 10% missing power [src: Sect. 8;
size in `systematics.md#covariance`].

**Number of realisations.** More replicas reduce zero-probability objects
but cannot remove them in DESI-like multi-pass tiling with priority
conflicts (0.17–0.28% after 128 in Y1) [src: arXiv:2404.03006, Table 4];
the efficient estimator and g_K (Eqs. 8–11) are the DESI answer to finite
K [src: arXiv:2411.12025, Sect. 5.2].

**Reference sample for up-weighting.** Using the full target sample
without redshift cut, rather than the parent restricted in redshift,
isolates the assignment loss from photometric and redshift-failure effects
[src: arXiv:2411.12025, Sect. 5.2.1].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| altMTL realisations | 128 (data), 256 (SV3 mocks) | DESI | arXiv:2404.03006 | Sect. 4.3 |
| Zero-probability objects after 128 | Y1: BGS_BRIGHT 0.21%, LRG 0.22%, ELG 0.17%, QSO 0.28%; SV3: ≤ 3 × 10⁻³ % | DESI | arXiv:2404.03006 | Table 4 |
| Observations whose target information changes in replay | 6.7% (SV3), 13.0% (Y1) of dark time | DESI | arXiv:2404.03006 | Sect. 4.4 |
| altMTL replicas in DR1 tests | K = 128 + real; data and Abacus mock 11 | DESI DR1 | arXiv:2411.12025 | Sect. 7 |
| FFA replicas | K = 256 for each of 25 Abacus mocks | DESI DR1 | arXiv:2411.12025 | Sect. 7 |
| FFA parameters | θ_LL = 0.02°, f_anti = 0.1, β_tilt for BGS only | DESI DR1 | arXiv:2411.12025 | Sect. 3.2 |
| Zero-probability ELG targets, NGC | ≈ 2.5 × 10⁵; ≈ 1% bias on angular counts | DESI DR1 | arXiv:2411.12025 | Sect. 5.2.2 |
| Up-weighting range | θ < 0.2° (ξ); θ < 0.25° (P) | DESI DR1 | arXiv:2411.12025 | Sect. 7 |
| θ-cut | 0.05° (patrol diameter); positioner collisions ≈ 0.01° | DESI DR1 | arXiv:2406.04804 | Sect. 2.3 |
| 0.05° at z = 1 | ≈ 3 h⁻¹ Mpc transverse | DESI DR1 | arXiv:2411.12025 | Sect. 6.1 |
| eBOSS tiling runs | 1860 (DR16 data), 310 per mock | eBOSS DR16 | arXiv:2007.09005 | Sect. 4.4 |
| eBOSS tiling run time | ≈ 1–2 h per realisation before parallelisation | eBOSS | arXiv:2007.09005 | Sect. 4.4 |
| Suggested N_bits | ~10³, split into ~10 integer sub-weights | method | arXiv:1703.02070 | Sect. 6.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Zero-probability pairs mistaken for PIP failure.** PIP alone leaves a
  small-scale deficit wherever single-pass areas or priority conflicts
  make pairs unobservable; it appears in DR1 data, altMTL mocks and, less,
  FFA mocks [src: arXiv:2411.12025, Sect. 5.2.1]. Test: PIP versus PIP +
  up-weighting against the complete mock.
- **Zero-probability galaxies tracing n_tile.** Uncorrected, a percent-level
  large-scale error in two-point measurements [src: Sect. 5.2.2]. Test:
  angular pair counts of assigned (IIP-weighted) over full sample as a
  function of n_tile; correction w_NTMP.
- **Double counting of completeness.** With PIP, the IIP part must be
  divided out of the catalogue WEIGHT (w'_galaxies = w_galaxies/w_IIP)
  before applying bitweights, and the randoms must carry f_NTMP [src:
  Sect. 7]; with PIP the randoms must not also carry f_tile
  (`cosmo-data-pipelines/deep/lss-catalogues.md`).
- **Up-weighting assumption broken by tiling design.** In eBOSS, tile
  overlaps correlate with target density, which can bias the DR16
  small-scale measurement in a way no available method corrects [src:
  arXiv:2007.09005, Sect. 4.3]; averaged over 100 EZmocks a bias near the
  collision scale in w_p appeared, spread to ~10 h⁻¹ Mpc in multipoles
  for PIP alone and removed by adding up-weighting [src: Sect. 7].
- **Replayed outcomes from the wrong target class.** Mapping real fibre
  outcomes onto alternative targets is approximate for QSOs, whose
  redshift decides further visits [src: arXiv:2404.03006, Sect. 4.4].
- **Covariance mocks with a softer collision window.** FFA under-produces
  zero-probability pairs; one suspected reason for the DR1 P(k) covariance
  deficit [src: arXiv:2411.12025, Sect. 8].
- **θ-cut with reconstruction.** Small-scale incompleteness is propagated
  to large scales by the displacement field [src: Sect. 8].

## Reading list
<!-- key: reading-list -->

- Foundation: Bianchi & Percival 2017, arXiv:1703.02070 — PIP, bitwise
  weights (Eq. 14), angular up-weighting (Eq. 13), small-scale conditions.
- Method, data: Lasker et al. 2024, arXiv:2404.03006 — how altMTL
  replays the DESI survey; realisation counts and zero-probability
  fractions.
- Method and validation: Bianchi et al. 2024, arXiv:2411.12025 — FFA,
  efficient PIP estimator with g_K, full-sample up-weighting, w_NTMP and
  the four-way comparison.
- Alternative: Pinon et al. 2024, arXiv:2406.04804 — choice of the 0.05°
  θ-cut and its window.
- Application: Mohammad et al. 2020, arXiv:2007.09005 — eBOSS PIP +
  angular up-weighting, its limits from tiling design.
- Application: Andrade et al. 2025, arXiv:2503.14742 — how DR2 BAO
  treated fibre assignment (mock recovery only).

## Not verified
<!-- key: not-verified -->

- The convergence study of the efficient estimator (the paper cited as
  ref. [16] in arXiv:2411.12025) was not read; Eq. 8 and its stated
  property are taken from arXiv:2411.12025.
- The FFA IIP formula is written as (c + 1)/(K + 1) in Sect. 3.2 of
  arXiv:2411.12025 and as (K + 1)/(c + 1) in Eq. 8; the first is read as a
  typesetting inversion, not checked against code.
- Quantitative residuals per scheme in Figs. 11–14 of arXiv:2411.12025
  (only text and the L2 numbers read).
- Whether DESI DR2 full-shape or small-scale analyses adopted PIP +
  up-weighting.
