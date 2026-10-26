# Catalogue-level blinding — cosmo-galaxy-clustering dossier

Scope: how a spectroscopic clustering catalogue is blinded and unblinded in
practice (the equations of the AP-like and RSD-like redshift shifts and of
the f_NL weights, how the hidden parameters and their ranges are chosen,
what is run on blinded data and how reconstruction and full-shape fits
behave on it, how the scheme is validated, which tests gate unblinding and
what may still change afterwards), and how to choose between the variants.
Snapshot: 2026-10-19.
From: DESI 2024 II (arXiv:2411.12020), Sect. 2.4 (copied from
`references/subtopics.tsv`).

Already in L2 or a sibling, not repeated here: the one-paragraph
description of the scheme, the DESI DR1 table of what was blinded and the
post-unblinding fixes (`physics-and-methods.md#blinding`); the referee's
view of what is frozen when (`systematics.md#confirmation-bias`); the
cross-probe table of blinding levels (catalogue, data vector, covariance,
parameter) and the generic requirements of a blinding scheme
(`cosmo-statistics-inference/references/physics-and-methods.md#blinding-strategies`);
lensing-style data-vector blinding and its unblinding criteria
(`cosmo-weak-lensing/deep/blinding-consistency.md`); the DESI DR1 f_NL
model and systematics budget
(`cosmo-inflation-primordial/references/systematics.md#d2b-desi-dr1-lrg-qso-budget-as-read`).

Notation. Ω^ref (Brieden et al.) = Ω_fid (DESI): the fiducial cosmology
used to turn redshifts into distances and to build templates.
Ω^shift (Brieden) = Ω_blind (DESI): the hidden cosmology. Primes denote
blinded quantities. α_∥, α_⊥, α_iso, α_AP as in
`physics-and-methods.md#baryon-acoustic-oscillations-standard-ruler`;
f is the linear growth rate, b the linear bias, Ψ the Lagrangian
displacement estimated by reconstruction, r̂ the line-of-sight unit vector.
This dossier follows the Brieden et al. notation for the shifts and the
DESI notation for the pipeline.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Decide what is blinded and draw the hidden parameters
<!-- key: step-1-decide-what-is-blinded-and-draw-the -->

Brieden et al. 2020 (arXiv:2006.10857) blind only late-time parameters,
ΔΩ = {ΔΩ_m, 0, 0, 0, 0, 0, Δw, Δγ} (Eq. 32), and leave H0 unblinded "as its
value is absorbed into the unit via the factor h" [src: Sect. 3.1]. DESI
DR1 blinds (w0, wa, f_NL) [src: arXiv:2404.07282, Sect. 3.3]. Stated reason
for w0wa rather than also curvature: with DESI alone w0wa and Ω_K are
strongly degenerate, so blinding flat w0waCDM already gives H(z) enough
freedom to mimic a curved model [src: same]; the full-shape paper adds that
other variations (Ω_m, Ω_K) are then "reasonable good fits" to a blind
catalogue in the absence of external data [src: arXiv:2411.12021,
Sect. 2.3].

Constraints on the draw [src: arXiv:2404.07282, Sect. 3.3, Fig. 1, Eq. 14]:

- |α_⊥ − 1| < 0.03 and |α_∥ − 1| < 0.03 over 0.4 < z < 2.1; the allowed
  (w0, wa) region is the white area of their Fig. 1 [src: arXiv:2404.07282,
  Sect. 3.3]. Adding BGS
  (0.1 < z < 0.4) later did not change the region (arXiv:2404.07282, App. A).
- The growth-rate shift is not drawn independently (arXiv:2404.07282): f_blind is set so that
  the RSD boost of the monopole compensates the volume dilation α_iso⁻³ of
  the AP shift,
  f_blind(z) = b_1 { sqrt[ (D²_A,fid H_blind)/(D²_A,blind H_fid)
  (f²_fid/b²_1 + (10/3) f_fid/b_1) + 25/9 ] − 5/3 } (Eq. 14),
  with |f_blind − f_fid| < 10% of f_fid = 0.8.
- Stated reason for 3% and 10%: "roughly based on the precision of such
  measurements before DESI DR1" [src: Sect. 3.3]. Brieden et al. advise
  that the shift "should probably not exceed deviations of 3σ" of the
  forecast sensitivity, because large shifts break the approximations
  (fixed covariance, reference template) [src: arXiv:2006.10857, Sect. 6].
- f_NL^blind ∈ [−15, 15] for data [src: arXiv:2404.03000, Sect. 2.3;
  arXiv:2411.17623, Sect. 3.1.3]; the method paper studied [−50, 50] and
  expected a narrower data range because σ(f_NL) ≈ 15 was forecast for DR1
  [src: arXiv:2406.00191, Sect. 2.3.3].
- Draw: 1000 random (w0, wa) pairs inside the allowed region; one is picked
  for all tracers; "even the 'blinding team' did not have access" to it
  [src: arXiv:2404.07282, Sect. 3.3]. The values are stored in files read
  by every catalogue version so the blind stays fixed across versions
  [src: arXiv:2404.03000, Sect. 2.3].

### Step 2. AP-like shift (blinds the expansion history)
<!-- key: step-2-ap-like-shift-blinds-the-expansion -->

Each observed redshift is converted to a comoving distance with the hidden
cosmology and back to a redshift with the fiducial one:
z_i → D_M(z_i, Ω^shift) = D_M(z'_i, Ω^ref) → z'_i (Eq. 34), and
Δ^AP z_i = z'_i − z_i (Eq. 35) [src: arXiv:2006.10857, Sect. 3.2]. The
shift depends only on redshift, so angular positions, and hence
fibre-collision corrections and angular systematics, are untouched
[src: Sect. 3.1]. Since r_d is unchanged (Eq. 39), the expected effect is

α'_⊥/α_⊥ = D_M^ref(z_*)/D_M^shift(z_*),  α'_∥/α_∥ = H^shift(z_*)/H^ref(z_*)
(Eq. 41),

valid whether the effective redshift z_* moves or not [src: Sect. 3.2].
DESI writes the same transformation as its Eq. 10 [src:
arXiv:2404.07282, Sect. 3.2].

Redshift cuts after the shift [src: arXiv:2006.10857, Sects. 3.2, 4.3]:
"shifted redshift cuts" keep the same objects and move z_* by Δz(z_*)
(Eq. 36); "fixed redshift cuts" keep the same z limits and leave
z'_* ≃ z_* (Eq. 37) only when the cuts sit where n(z) is close to its mean.
In BOSS mocks about 5% of galaxies left and 5% entered each bin and z_*
agreed within 0.1%, but the authors warn this does not generalise; they
recommend shifted cuts "whenever possible" [src: Sect. 4.3].

### Step 3. RSD-like shift (blinds the growth rate)
<!-- key: step-3-rsd-like-shift-blinds-the-growth-rate -->

On the AP-shifted catalogue, run a reconstruction with fiducial b^ref,
f^ref and smoothing R_sm to estimate Ψ, then remove the fiducial RSD
displacement and add one with the hidden growth rate:

r' = r − f^ref (Ψ·r̂) r̂ + f^shift (Ψ·r̂) r̂ (Eq. 42),

and convert r' back to z' with the fiducial cosmology [src:
arXiv:2006.10857, Sect. 3.3; DESI Eq. 11 in arXiv:2404.07282, Sect. 3.2].
The shift differs per galaxy because Ψ depends on the local density. The
expected recovered growth rate is f' = f + f^shift − f^ref (Eq. 43), i.e.
fσ8' = fσ8 + (f^shift − f^ref) σ8^ref (Eq. 48) [src: Sects. 3.3, 4.4].
σ8 itself cannot be blinded, because only radial positions move [src:
Sect. 4.4, footnote 9]. For several redshift bins the authors recommend a
coherent parametrisation of f(z) across bins rather than independent
shifts [src: Sect. 3.3].

Smoothing choice (arXiv:2006.10857) [src: Sect. 4.4]: R_sm = 15 h⁻¹ Mpc left an RSD bump at
0.05 < k < 0.20 h Mpc⁻¹; 5 h⁻¹ Mpc gave a negative reconstructed
quadrupole (non-linear velocities over-predict linear RSD); 10 h⁻¹ Mpc was
adopted for LOWZ and CMASS, and a sub-optimal choice "does not affect the
recovered parameter values" [src: Sect. 6].

### Step 4. f_NL weights (blinds the scale-dependent bias)
<!-- key: step-4-fnl-weights-blinds-the-scale-dependent -->

Redshift shifts cannot imitate a 1/k² bias, so a weight is multiplied into
the catalogue [src: arXiv:2406.00191, Sect. 2.2.1]:

w^d_blind(x) = 1 + w_blind(x) (Eq. 6),
w_blind(k) = [b_Φ f_NL^blind / (b α(k))] δ̂^r(k) ≡ a(k) δ̂^r(k) (Eq. 7),

with δ̂^r an estimate of the real-space density, b_Φ the PNG bias response
and α(k) the transfer from the primordial potential to density, both at
the effective redshift (`cosmo-inflation-primordial/references/physics-and-methods.md#scale-dependent-bias-large-scale-structure`
for their definitions). δ̂^r is built by painting data and randoms (CIC),
smoothing with S_1 = exp(−k²σ_1²/2) (Eq. 8), estimating RSD displacements
with pyrecon's iterative FFT for a fiducial b and f, moving the galaxies
back, repainting, dividing by b and smoothing with S_2 (σ_2); σ_1 = σ_2 =
30 h⁻¹ Mpc (arXiv:2406.00191) [src: Sect. 2.2.2]. Stated reason: only large scales are needed,
and S_2 keeps the weights away from BAO and RSD scales [src: same]. The
blinded spectrum is (Eq. 11) the original plus 2a(k) X̃ + a(k)² Ỹ, with X̃
and Ỹ (Eqs. 12–13) carrying a shot-noise term; a corrective factor a'/a in
[0, 1], fixed at a pivot k_p (4 × 10⁻³ h Mpc⁻¹ for f_NL^blind > 0), removes
the shot-noise bias [src: Sects. 2.3.1–2.3.3].

DESI DR1 specifics [src: arXiv:2411.17623, Sect. 3.1.3, Eq. 9]:
f_NL^obs = f_NL^loc + f_NL^blind; the weights were generated with b_Φ for
p = 1 in every sample, so for QSOs analysed with p = 1.6 the apparent blind
value is larger in absolute value; the weights are multiplied into the
completeness weights "preventing anyone from breaking the blinding since
the large-scale modes of the power spectrum cannot be recovered without
correcting for completeness". The full-shape paper states the merger is
with the imaging weights [src: arXiv:2411.12021, Sect. 2.3, footnote 2];
the two papers name different host weights.

### Step 5. Apply all three together, never partially
<!-- key: step-5-apply-all-three-together-never-partially -->

BAO, RSD and f_NL blinds "are always simultaneously applied on the
catalogues, and we never partially blind (or unblind)" [src:
arXiv:2411.12021, Sect. 2.3]. The same blind catalogue served DR1 BAO,
full shape and f_NL, so f_NL and RSD stayed blind after BAO was unblinded
[src: arXiv:2404.07282, Sect. 3.3]. DR2 reused the DR1 pipeline
[src: arXiv:2503.14742, Sect. II.4].

### Step 6. Run the analysis on the blinded catalogue
<!-- key: step-6-run-the-analysis-on-the-blinded-catalogue -->

- Everything that defines the measurement is built on blinded data: LSS
  catalogue iterations (six over 13 months for DR1), imaging and fibre
  corrections, priors, scale range and the imaging-weight nuisance
  parameter [src: arXiv:2411.12021, Sect. 6].
- Reconstruction on blinded data uses the same fiducial (b, f) as on
  unblinded data. On BOSS CMASS, reconstructing the blinded catalogue with
  f = 0.784 or with the blind target f = 0.695 was compared [src:
  arXiv:2006.10857, Fig. 16]; using the same f in both cases has "very
  small" impact [src: Sect. 4.5.1].
- Full shape: only ShapeFit may be run blind; full-modelling fits "would
  inform us about the cosmological interpretation" [src: arXiv:2411.12021,
  Sect. 6]. Stated reasons for ShapeFit at this stage: same information as
  full modelling for many models, no assumed cosmology, each compressed
  parameter tied to a range of scales (so systematics are easier to spot),
  and no prior-volume shifts [src: same].
- f_NL: imaging-weight validation is done on blinded large-scale monopoles
  split by photometric region and redshift. The blind is insensitive to
  shot noise and hence identical across sub-samples, so spurious excess
  power can be sought even though the window and integral constraints
  differ per sub-sample [src: arXiv:2411.17623, Sect. 5.3.1]. This is how
  the LRG k_min was raised from 0.003 to 0.006 h Mpc⁻¹ [src: same].
- Covariance: DR2 pipelines were fixed while blind and rerun on unblinded
  measurements, because calibrating the covariance needs the true
  clustering [src: arXiv:2503.14742, Sects. II.4, IV.4].

### Step 7. Validate the blinding itself
<!-- key: step-7-validate-the-blinding-itself -->

Metric [src: arXiv:2404.07282, Sect. 4.4, Eqs. 24–27]: rescale each
measured α by α^rescaling (Eq. 25: D_V and D_M/D_H ratios of blind to
fiducial cosmology), then divide by the unblinded measurement on the same
mock, Γ_α = (α^measured/α^rescaling)/α^measured_baseline (Eq. 26), which
cancels sample variance; Γ̃_m (Eq. 27) uses differences for m. Γ = 1
(Γ̃ = 0) means no residual.

Mock test (arXiv:2404.07282) [src: Sects. 5.1–5.2]: 25 AbacusSummit DR1-like mocks (200 h⁻³
Gpc³) for the multipoles; one mock blinded 8 × 2 times (8 (w0, wa) pairs ×
f_NL = ±20) for fits. Pass criterion is qualitative: Γ near unity and
reduced χ² within the 1σ–2σ spread of the 16 cases (about 80% within 1σ).
Data test [src: Sect. 6]: a second blind with a (w0, wa) pair at the edge
of the allowed region and f_NL = 20 was applied on top of the blinded data
("double-blinded"); six BAO analysis variants (1D, pre-recon, P(k),
polynomial broadband, flat damping priors) agreed with the baseline on
both layers, and the double-blinded posteriors differ from a simple
posterior shift of the fiducial-blinded ones, showing catalogue blinding
is "more complex" than posterior blinding [src: Sects. 6.1.1–6.1.2].

### Step 8. Unblind on a written checklist, with a written list of allowed changes
<!-- key: step-8-unblind-on-a-written-checklist-with-a -->

Pass rule shared by DR1 BAO, DR1 full shape and DR2 BAO: a test passes if
the difference seen in the blinded data lies within the full range spanned
by 25 Abacus-2 mocks [src: arXiv:2404.03000, Table 14; arXiv:2411.12021,
Table 8; arXiv:2503.14742, Table 6]. A systematic counts as detected above
3σ of the test's statistical precision [src: arXiv:2503.14742, Sect. VI.2].
The systematic budget is fixed before unblinding, with the stated aim of
preventing the tendency "to attribute a higher level of systematic
uncertainty to outcomes that are unexpected" [src: arXiv:2404.03000,
Sect. 6].

DR2 column from arXiv:2503.14742, Table 6 [src]; the other columns as listed under the table:

| Checklist item | DR1 BAO | DR1 FS (ShapeFit) | DR2 BAO |
|---|---|---|---|
| χ² acceptable | yes | yes | yes, and consistent with mocks |
| pre- vs post-reconstruction α | yes | ShapeFit α vs post-recon BAO | yes |
| NGC+SGC vs NGC; North vs South | yes; clustering level | yes; clustering level | data splits incl. magnitude/mass |
| ξ vs P(k) | yes | yes | within 0.5σ |
| different fiducial cosmologies | yes | — | budget item #9 |
| error bars vs mocks | yes | — | yes |
| LRG vs ELG at 0.8 < z < 1.1 | yes | — | Δα_iso 0.41σ, Δα_AP −1.66σ |
| reconstruction settings; imaging robustness; mock bias | — | — | yes; stable without imaging weights; largest 2.46σ (QSO post-recon) |

[src: arXiv:2404.03000, Table 14; arXiv:2411.12021, Table 8 and Sect. 6;
arXiv:2503.14742, Table 6]

Allowed after unblinding, decided beforehand:

- DR1 BAO: covariance calibration and choice (EZmocks were not ready); a
  rerun with another N_eff template if the cosmology fit preferred one;
  catalogue fixes for errors found in checks unrelated to BAO fitting; HOD
  systematics for QSO and BGS [src: arXiv:2404.03000, Sect. 6].
- DR1 full shape: covariance update; ShapeFit template cosmology update
  (so that α ≈ 1, m ≈ 0); HOD systematics for BGS and QSO; the method for
  adding systematics at the k-bin level was developed after unblinding
  "because of its novelty" [src: arXiv:2411.12021, Sect. 6].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

**Catalogue, data-vector or posterior blinding.** Catalogue blinding blinds
every statistic at once, including the bispectrum [src: arXiv:2411.12021,
Sect. 2.3], at the price of validating the shift for each observable and
of a shift that is not exactly a cosmological model: DESI notes the blind
background and growth are not linked by f = Ω_m^0.55 [src: same]. The
double-blind test shows it is not equivalent to shifting posteriors [src:
arXiv:2404.07282, Sect. 6.1.2]. Data-vector blinding is the lensing
choice (`cosmo-weak-lensing/deep/blinding-consistency.md`).

**Shift size.** Larger shifts hide more but degrade predictability; a 50%
shift in f degraded only the accuracy of the error-bar criterion [src:
arXiv:2006.10857, Sect. 6]. DESI used 3% in α and 10% in f [src:
arXiv:2404.07282, Sect. 3.3]; the bispectrum validation used Δf = −0.068
(about 3σ of its recovered error) and Δα = −0.013 (1–2σ) [src:
arXiv:2407.12931, Sect. 5].

**Fixed or shifted redshift cuts.** Shifted cuts give a predictable z_*
(Eq. 36); fixed cuts rely on n(z) near its mean at the edges (Eq. 37)
[src: arXiv:2006.10857, Sects. 3.2, 4.3].

**Reconstruction inputs on blind data.** Same (b, f, R_sm) as for
unblinded data. Using reconstruction inputs far from the truth can bias
post-reconstruction BAO, but the blinded mocks agreed with expectation;
only CMASS post-recon showed "a small trend towards smaller errors after
blinding", attributed possibly to a sub-optimal bias [src: Sect. 4.5.1].

**Template cosmology.** Fits of blinded Patchy means with Ref, Low-Ω_m
(0.286) and High-Ω_m (0.35) templates all recover the expected ratios,
e.g. at z = 0.60 α'_∥/α_∥ expected 0.9502, recovered 0.951 ± 0.002 (Ref),
0.949 ± 0.002, 0.956 ± 0.002 [src: arXiv:2006.10857, App. B, Table 6].

**b_Φ assumed in the f_NL weights.** One p for all tracers keeps the blind
coherent across samples for split tests; the cost is that the apparent
blind value depends on the p used in the fit [src: arXiv:2411.17623,
Sect. 3.1.3].

**f_NL blinding and full-shape parameters.** With f_NL^blind ∈ {−15, 0,
15} on 25 LRG Abacus mocks, q_∥, q_⊥ and f/f_fid are unaffected; m shifts,
below the statistical error, because the blind changes the large-scale
slope [src: arXiv:2406.00191, App. C]. The DR1 mock validation saw the
same offset in m between f_NL = ±20 and a very mild f_NL dependence of
f/f_fid through its correlation with m [src: arXiv:2404.07282,
Sect. 5.2.2]. On unblinded DR1 data, ShapeFit m moved by about 1σ for some
tracers, read as the f_NL blind's effect [src: arXiv:2411.12021,
Sect. 6.1].

**Mock calibration while blind.** HOD mocks can be tuned to the blinded
data; Brieden et al. suggest shifting mock galaxies "back" at unblinding
[src: arXiv:2006.10857, Sect. 6]. DESI DR1 mocks were calibrated to the
One-Percent survey instead, a stated limitation [src: arXiv:2404.03000,
Sect. 6].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Allowed α_∥, α_⊥ shift | < 3% over 0.4 < z < 2.1 | DESI DR1 | arXiv:2404.07282 | Sect. 3.3, Fig. 1 |
| Allowed f shift | < 10% of f_fid = 0.8 | DESI DR1 | arXiv:2404.07282 | Sect. 3.3, Eq. 14 |
| f_NL^blind range | [−15, 15] | DESI DR1 | arXiv:2404.03000; arXiv:2411.17623 | Sect. 2.3; Sect. 3.1.3 |
| Candidate (w0, wa) list | 1000 pairs, one drawn | DESI DR1 | arXiv:2404.07282 | Sect. 3.3 |
| Validation blinds | 8 (w0, wa) × f_NL = ±20 on one mock | DESI DR1 | arXiv:2404.07282 | Sect. 5.1 |
| Γ_αiso, Γ_αAP, LRG 0.8–1.1 post-recon ξ | 1.000–1.012 (σ ≈ 0.013); 0.986–1.011 (σ ≈ 0.035–0.041) | DESI DR1 mock | arXiv:2404.07282 | Table 3 |
| RSD-blind smoothing | R_sm = 10 h⁻¹ Mpc (15 and 5 rejected) | BOSS mocks | arXiv:2006.10857 | Sect. 4.4 |
| f_NL-blind smoothing | σ_1 = σ_2 = 30 h⁻¹ Mpc | DESI DR1 | arXiv:2406.00191 | Sect. 2.2.2 |
| Scale above which the f_NL blind is negligible | k ≈ 0.06 h Mpc⁻¹ | DESI mocks | arXiv:2406.00191 | Sect. 3.4 |
| Blind shift sizes, BOSS mocks | ~10% on Ω_m and w (≈ 1σ of LOWZ+CMASS BAO) | BOSS | arXiv:2006.10857 | Sect. 4.1 |
| Galaxies crossing a fixed z cut | ≈ 5% out, ≈ 5% in; z_* within 0.1% | BOSS mocks | arXiv:2006.10857 | Sect. 4.3 |
| Unblinding pass rule | within full range of 25 Abacus-2 mocks | DESI DR1, DR2 | arXiv:2404.03000; arXiv:2503.14742 | Table 14; Table 6 |
| Detection threshold | 3σ of test precision | DESI DR2 | arXiv:2503.14742 | Sect. VI.2 |
| Post-unblinding catalogue fix | largest −0.7σ (α_AP, LRG1), others < 0.5σ | DESI DR1 | arXiv:2404.03000 | Sect. 2.3 |
| Post-unblinding code fix | < 0.3σ, most < 0.1σ | DESI DR1 | arXiv:2404.03000 | Sect. 6 |
| Unblinded vs blinded f/f_fid | 2–2.5σ for ELG and QSO, as expected from the blind | DESI DR1 FS | arXiv:2411.12021 | Sect. 6.1 |
| DR1 full-shape unblinding date | 12 June 2024 | DESI DR1 | arXiv:2411.12021 | Sect. 6 |
| RSD-blinding cost | 5–7 min on a dual-core CPU per BOSS sample | BOSS | arXiv:2006.10857 | Sect. 6 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Accidental unblinding by omitting a weight.** Countered by merging the
  f_NL weight into a weight without which large scales are visibly wrong
  [src: arXiv:2411.17623, Sect. 3.1.3; arXiv:2411.12021, Sect. 2.3].
- **Partial unblinding.** Running full modelling on blinded data reveals
  the cosmology; DESI allows only ShapeFit while blind [src:
  arXiv:2411.12021, Sect. 6].
- **Effective-redshift drift.** With fixed cuts and steep n(z) edges, z_*
  moves and the expected α' ratio is read at the wrong redshift [src:
  arXiv:2006.10857, Sect. 4.3]. Test: compare z_* before and after
  blinding.
- **Blind and imaging correction interfering.** On FastPM QSO mocks with
  realistic contamination, the blind f_NL^blind = 10 was recovered with
  exact inverse weights; with untuned regressis weights it was 1.4σ off
  [src: arXiv:2406.00191, Sect. 4.3].
- **Blinded bias differs from the unblinded one.** In DESI DR1 f_NL, b_1
  was lower in the blinded catalogue than in the unblinded one, more than
  the blinding method predicts; the cause is unknown, and blinded f_NL
  errors were correspondingly larger [src: arXiv:2411.17623, Sect. 6.1].
  The method paper predicts a smaller effective bias from the S_2 damping
  [src: arXiv:2406.00191, Sect. 3.4].
- **Errors found after unblinding.** DR1 found a random-weight error and a
  model-implementation discrepancy after unblinding; both fixes were within
  rules written in advance [src: arXiv:2404.03000, Sects. 2.3, 6]. Test for
  a referee: are the post-unblinding changes on the pre-agreed list?
- **Bispectrum multipoles beyond the monopole.** No adequate window model
  exists, so AP-blinding validation covers {P_0, P_2, B_0} only; with B_0
  alone f and σ8 stay degenerate and only fσ8 tests the RSD blind [src:
  arXiv:2407.12931, Sect. 5]. Full-modelling bispectrum fits need their own
  validation [src: same].

## Reading list
<!-- key: reading-list -->

- Method: Brieden et al. 2020, arXiv:2006.10857 — the AP and RSD shift
  equations, cut conventions, smoothing choice and BOSS worked example.
- Method: Chaussidon et al. 2024, arXiv:2406.00191 — the f_NL weights,
  shot-noise correction and their interplay with imaging weights.
- Validation: Andrade et al. 2024, arXiv:2404.07282 — DESI ranges, Eq. 14,
  the Γ metric and the double-blind test.
- Application: DESI Collaboration 2024, arXiv:2404.03000 (Sects. 2.3, 6) —
  BAO unblinding checklist and allowed post-unblinding changes.
- Application: Adame et al. 2024, arXiv:2411.12021 (Sects. 2.3, 6) — first
  blinded full-shape analysis; ShapeFit-only rule.
- Application: Chaussidon et al. 2024, arXiv:2411.17623 (Sects. 3.1.3,
  5.3) — validating imaging weights on blinded large scales.
- Application: Andrade et al. 2025, arXiv:2503.14742 (Sect. VI.2) — DR2
  ten-item checklist.
- Test: Novell-Masot et al. 2024, arXiv:2407.12931 — the scheme on the
  bispectrum and its limits.

## Not verified
<!-- key: not-verified -->

- The list of requirements i)–vi) of Brieden et al. Sect. 6 (only parts
  read) and their Table 2 shift values.
- DESI DR1 Sect. 2.4 of arXiv:2411.12020 was not read; the implementation
  details here come from the BAO, full-shape, f_NL and validation papers.
- The DR2 blinding seed or ranges (only "DR1 pipeline" reused was read).
- Blinding plans of Euclid, PFS or 4MOST spectroscopic clustering: not
  searched in depth; none found in the search run.
