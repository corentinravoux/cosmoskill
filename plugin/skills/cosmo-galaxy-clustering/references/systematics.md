# Galaxy clustering — systematics

Scope: the canonical systematics of spectroscopic clustering analyses (BAO,
full shape, scale-dependent bias): mechanism, measured size, mitigation,
validation test, and the paper a referee expects. Snapshot: 2026-10-20.

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here. "σ_DR1" is the DESI DR1 statistical
error on the parameter concerned.

## 0. Two budgets to keep apart
<!-- key: two-budgets-to-keep-apart -->

BAO and full shape have different systematics hierarchies. For the BAO scale
the budget is quoted in per cent of α and is dominated by theory and the
galaxy–halo connection; observational effects are not detected. For full
shape the budget is quoted in units of the statistical error and is dominated
by the galaxy–halo connection, priors, imaging and fibre assignment.

**DESI DR1 BAO budget** (DESI Collaboration 2024).
From arXiv:2404.03000, Sect. 5.5 and Table 13 [src]:

| Source | α_iso [%] | α_AP [%] | Comment |
|---|---|---|---|
| Theory and modelling | 0.1 | 0.2 | fitting choices, bias, non-linear shift |
| HOD (configuration space) | 0.2 | 0.2 | one statistically significant detection only |
| Fiducial cosmology | 0.1 | 0.1 | excludes the N_eff template bias |
| N_eff = 3.7 in the template | 0.2 | — | listed separately, not in the total |
| Imaging, spectroscopic, fibre assignment | not detected | not detected | |
| Reconstruction algorithm, covariance | not detected | not detected | |
| **Total adopted** | **0.245** | **0.3** | worst case across tracers, for ξ and P |

Body detail (arXiv:2404.03000) [src: Sect. 5.5, Tables 12–13, Eqs. 17–20]:

| Item | What the paper states |
|---|---|
| Per-space totals before the worst case | ξ: 0.245% (α_iso) and 0.3% (α_AP, LRG/ELG); P(k): α_iso totals of 0.245, 0.18, 0.245 and 0.19 in the tracer columns of Table 13, lower than in ξ where the P(k) HOD term of Table 12 is 0.1, 0.1 and 0.12 (0.2 in its first column) |
| Imaging | largest change 0.3% (ELG1), 0.1% for the rest, tested on data; "not detected" |
| Fiducial D_A(z) | < 0.1%, upper limit set by mock precision |
| How it enters | terms added in quadrature, C_sys = diag(0.245², 0.3²) in (α_iso, α_AP), in per cent, assumed uncorrelated; projected to (α_⊥, α_∥) as 0.265% and 0.316% with correlation +0.478; added to the statistical covariance of each bin |
| Effect on the error | about 5% on the best α_iso; for LRG3+ELG1, +1.5% on α_∥ and +2.2% on α_⊥ |

**DESI DR2 BAO changes** (DESI Collaboration 2025, arXiv:2503.14738;
Andrade et al. 2025, arXiv:2503.14742) [src]: fiducial-cosmology error on
α_AP raised from 0.1% to 0.18% after including an evolving-dark-energy
cosmology in the test; HOD terms made tracer-specific. The systematic term
inflates the total error on α_iso by 1% (BGS) to 9% (LRG3+ELG1) and on α_AP
by 0.1% (QSO) to 2% (LRG3+ELG1); every bin remains statistics-dominated.
Correlating the theory systematics across bins has no significant effect
[src: arXiv:2503.14738, Sect. III.1]. The same section names the
galaxy–halo connection as the term that dominated the DR1 budget. For Lyα,
a theory systematic of 0.3% on α_∥ and α_⊥ is added to the statistical
covariance, degrading the isotropic precision to 0.7% [src:
arXiv:2503.14738, Sect. III.2].

**DESI DR2 BAO budget per tracer** (Andrade et al. 2025), in per cent,
terms added in quadrature, from arXiv:2503.14742 [src: Table 5, Sect. V.2]:

| Tracer | α_iso: theory, HOD, fiducial → total | α_AP: theory, HOD, fiducial → total |
|---|---|---|
| BGS (1D fit) | 0.1, none, 0.1 → 0.141 | — |
| LRG1, LRG2 | 0.1, none, 0.1 → 0.141 | 0.2, 0.19, 0.18 → 0.329 |
| LRG3, LRG3+ELG1 | 0.1, 0.17, 0.1 → 0.221 | 0.2, 0.19, 0.18 → 0.329 |
| ELG1, ELG2 | 0.1, 0.17, 0.1 → 0.221 | 0.2, none, 0.1 → 0.224 |
| QSO | 0.1, 0.17, 0.1 → 0.221 | 0.2, 0.19, 0.18 → 0.329 |

- The text gives the α_AP total as rising "from 0.3% to 0.335%"
  (arXiv:2503.14742) [src: Sect. V.2]; the table prints 0.329 [src: Table 5].
- QSO, newly fitted in 2D, takes the whole LRG3+ELG1 budget for want of a 2D
  HOD test; LRG3 takes the combined-bin budget because its n(z) and bias
  evolve across the bin [src: Sect. V.2].
- Theory terms were not re-evaluated (DR1 precision 0.01–0.1%), nor were
  reconstruction, fibre-assignment and spectroscopic terms; fibre assignment
  is tested only through unbiased recovery on realistic mocks
  (arXiv:2503.14742) [src: Sect. V.2].
- Baseline: systematics uncorrelated across bins. Post-unblinding test with
  theory terms fully or half correlated (covariance ½(0.1%)² on α_iso,
  ½(0.2%)² on α_AP between all bins): negligible shift of the DESI + CMB +
  DESY5 w0wa best fit (arXiv:2503.14742) [src: Sect. VII.1].
- Redshifts are used in the solar-barycentre frame, not the CMB frame; the
  angle-averaged offset in the nearest BGS bin is 0.0002 in z, negligible
  (arXiv:2503.14742) [src: Sect. V.2].

**DESI DR1 full-shape budget** (Adame et al. 2024), in units of σ_DR1.
From arXiv:2411.12021, Sect. 5.8 (total also in its Table 7) [src]:

| Source | Size | Treatment |
|---|---|---|
| Theory (four EFT pipelines, k_max = 0.20 h Mpc⁻¹) | < 0.1, not detected | none |
| Imaging | ≈ 0.2 for ELG, QSO; < 0.1 for BGS, LRG | template + mode-removal correction |
| Spectroscopic | < 0.2 for ELG; < 0.1 otherwise | redshift-failure weights |
| Fibre assignment | ≈ 0.2 | θ-cut and window rotation |
| HOD | ≈ 0.3 | systematic covariance C_HOD |
| Prior-weight effect | ≈ 0.2 | diagonal covariance term |
| Fiducial cosmology | < 0.2 | none |
| Covariance | < 0.2 | rescaling factor |
| **Total** | **≈ 0.46** | contributions ≥ 0.2 added in quadrature |

A contribution counts as a systematic when it exceeds one fifth of the
statistical error [src].

Body detail (arXiv:2411.12021) [src: Sect. 5.8, Table 7, Eqs. 15–17]:

| Item | What the paper states |
|---|---|
| Table 7 row values | HOD ≈ 0.3 (from Findlay et al. Table 2) and prior-weight effect (PWE) ≈ 0.2, listed together as "HOD+PWE"; same budget, ≈ 0.46 σ_DR1, for full modelling and ShapeFit |
| Why ≥ 0.2 | 25 Abacus mocks have one fifth of the DR1 error, so shifts below 0.2 σ_DR1 cannot be detected [src: Sect. 5.4] |
| How it enters | at the data-vector level, not the parameter level, so that it propagates to any cosmological model: window-rotation marginalisation (fibre assignment), HOD+PWE covariance, imaging covariance, added to the rescaled EZmock covariance |
| Check | parameter-level and data-vector-level inclusion give very similar profiles on DR1 mocks [src: Fig. 10] |
| Likelihood | Gaussian; Hartlap and Percival factors (N_params = 7) are smaller than the EZmock rescaling, so no Sellentin–Heavens t-distribution is used |
| FS + BAO | joint EZmock covariance of P_ℓ (2 × 36 k-bins) and the post-reconstruction α's, with the BAO block replaced by the DR1 BAO posterior covariance plus its systematic term |

PWE versus PVE [src: arXiv:2411.12021, Sect. 4.5, 5.2]: the prior-weight
effect is the pull of a mis-centred prior, read from the change of MAP between
flat and baseline priors; the prior-volume effect is the offset of the
marginal mean from the MAP for fixed priors. The PWE across HOD variants is
subdominant except for QSO, and is still counted.

## 1. Non-linear evolution and BAO modelling
<!-- key: non-linear-evolution-and-bao-modelling -->

**Mechanism.** Mode coupling shifts and damps the acoustic feature; galaxy
bias and RSD add anisotropic terms. Before reconstruction the shift of the
BAO scale is below 0.3% (DESI Collaboration 2024, arXiv:2404.03002)
[src: Sect. 2.3].

**Size.** After reconstruction, no more than 0.1% on the isotropic and 0.2%
on the anisotropic distance [src] (Chen et al. 2024, arXiv:2402.14070).
Term by term, σ(α_iso) / σ(α_AP) [src: arXiv:2404.03000, Sect. 5.1,
Table 7]: non-linear mode coupling < 0.1% / < 0.1%; baryon–dark-matter
relative velocity < 0.05% / < 0.05%; broadband modelling < 0.02% / 0.11%;
BAO wiggle extraction and dilating smooth versus wiggle < 0.02% / < 0.09%
each; ξ(s) as Hankel transform of dilated P_ℓ < 0.01% / 0.12%. Only the
broadband (spline versus polynomial) and the ξ-from-P choice are detections,
on the high-precision Abacus control-variate boxes; the 0.1%/0.2% total adds
those two in quadrature and rounds up.

**Mitigation.** Reconstruction (Eisenstein et al. 2007,
arXiv:astro-ph/0604362); a template with separate BAO damping and a smooth
broadband marginalised with a spline basis (arXiv:2402.14070).

**Validation.** Fits to high-precision N-body mocks with varied damping,
broadband and scale-cut choices; comparison of ξ and P fits; DESI DR2 found
the BAO constraints stable to data vector, modelling choices and the
Gaussian-likelihood assumption (arXiv:2503.14742).

**Lyα.** DESI DR2 added a theoretical systematic to Lyα BAO for the first
time: ±0.026 on D_H/r_d and ±0.12 on D_M/r_d [src: abstract] (DESI Collaboration 2025,
arXiv:2503.14739).

## 2. Galaxy–halo connection
<!-- key: galaxy-halo-connection -->

**Mechanism.** The reconstruction and the template assume a bias model; the
true small-scale occupation (satellite fraction, velocity bias, assembly
bias, conformity) can leave residual shifts. In full shape the EFT nuisance
parameters must absorb it.

**Size, BAO.** For LRGs, one 3.3σ detection: 0.19% on α_AP in configuration
space; conservative bounds otherwise [src] (Mena-Fernández et al. 2024,
arXiv:2404.03008). For ELGs, α_iso is recovered within 0.1% and α_AP within
0.3%, with an HOD systematic below 0.17% [src] (Garcia-Quintero et al. 2024,
arXiv:2404.03009). Adopted: 0.2%. Per tracer, P(k) / ξ, α_iso [src:
arXiv:2404.03000, Table 8]: BGS 0.19% / 0.20%; LRG 0.066% / 0.074%; ELG
0.047% / 0.17%; QSO 0.12% / 0.07%; α_AP: LRG 0.094% / 0.187%, ELG 0.089% /
0.11%; most entries are mock-precision limits, not detections.

**Size, full shape.** Shifts across HOD variants are often above 0.2 σ_DR1,
strongest for ELG and QSO, and appear mainly in the growth parameter in the
ShapeFit basis (Findlay et al. 2024, arXiv:2411.12023; arXiv:2411.12021)
[src: arXiv:2411.12021, Sect. 5.2, for the 0.2 σ_DR1].

**Mitigation.** A systematic covariance added to the data covariance
(arXiv:2411.12023). Alternatively, priors informed by the HOD (Zhang et al.
2025, arXiv:2504.10407) or by field-level simulations (Chudaykin et al. 2026,
arXiv:2602.18554); these trade a nuisance-parameter problem for a
model-dependence problem.

**Validation.** Refit AbacusSummit boxes populated with a family of HODs
tuned to early data (Yuan et al. 2022, arXiv:2110.11412, for the HOD
framework).

**Not studied in DESI DR1** [src] (arXiv:2411.12021): intrinsic alignments
with the tidal field, baryon–dark-matter relative velocities, line-of-sight
selection biases.

## 3. Fiducial cosmology
<!-- key: fiducial-cosmology -->

**Mechanism.** The catalogue is built with fiducial distances, the
reconstruction with a fiducial growth rate and bias, and compressed analyses
use a fiducial template. BAO are insensitive to this at leading order unless
the fiducial is far from the truth.

**Size.** BAO: 0.1% in DR1 (Pérez-Fernández et al. 2024, arXiv:2406.06085)
[src: abstract]; α_AP raised to 0.18% in DR2 (arXiv:2503.14742)
[src: Table 5]. Full modelling: maximum
shift 0.22 σ_DR1 in ΛCDM and 0.12σ with supernova mock data in w0waCDM;
ShapeFit compressed parameters below 0.45 σ_DR1, the slope m being the most
affected (Gsponer et al. 2025, arXiv:2509.08057) [src: abstract].

**Validation.** Rerun mocks with the four secondary AbacusSummit cosmologies
(low Ω_m, thawing dark energy, high N_eff, low σ8), iterating grid, template
and reconstruction cosmology consistently (arXiv:2406.06085). In DR1
[src: arXiv:2404.03000, Sect. 5.4, Tables 10–11]: the thawing case (c002)
offsets distances by about 4.7–7.5% and r_d by 6.8%, and AP by up to 2.9%;
a shift counts when above 3σ of the 25-mock dispersion; c003 (N_eff = 3.70)
gives about 0.2% in α_iso, a BAO phase shift from N_eff that is left out of
the budget; the adopted term is 0.1% on α_iso and α_AP.

**Referee point.** A w0waCDM result should be shown stable when the fiducial
cosmology is itself a w0wa cosmology; DESI added that test in DR2 and in the
full-shape systematics paper.

## 4. Fibre assignment and fibre collisions
<!-- key: fibre-assignment-and-fibre-collisions -->

**Mechanism.** A fibre positioner cannot serve two close targets in one pass.
In SDSS the limit is a 62″ collision radius (Mohammad et al. 2020,
arXiv:2007.09005) [src: abstract]. In DESI each robotic positioner has a finite patrol
radius, and target classes have different priorities, so incompleteness is
correlated with density and with the number of overlapping tiles; the
clustering amplitude is suppressed in a scale-dependent way (Bianchi et al.
2024, arXiv:2411.12025).

**Size.** DESI assignment completeness in DR1: BGS 61.6%, LRG 69.2%, ELG 35%,
QSO 87.6% (arXiv:2404.03002) [src: Sect. 2.2, sample paragraphs]; in DR2:
BGS 75.5%, LRG 82.6%, ELG 53.7%, QSO 93.6% (arXiv:2503.14738)
[src: Table 2]. On BAO the effect is not detected: the
mean shift between complete and fibre-assigned mocks is
Δα_iso = 0.00149 ± 0.00077, just under 2σ, flagged for a closer look in
future analyses (arXiv:2404.03000) [src: Sect. 5.3]. On full shape about
0.2 σ_DR1 [src] (arXiv:2411.12021).

**Mitigation.**

- PIP weights with angular up-weighting (Bianchi & Percival 2017,
  arXiv:1703.02070): unbiased down to about 0.1 h⁻¹ Mpc in eBOSS [src]
  (arXiv:2007.09005) and recover the true clustering in all DESI cases
  tested, including the first power spectrum measured with PIP weights on
  real data [src] (arXiv:2411.12025). Body detail [src: arXiv:2411.12025,
  Sects. 5.2, 7, 8]: completeness weights correct large and intermediate
  scales but not pairwise effects; the angular pair counts are suppressed
  below about 0.02°, by up to about 80% for SGC ELGs. DR1 PIP used 128
  alternative assignments (data and one altMTL mock; 256 fast-assignment
  realisations per mock). Angular upweighting a_DD = DD_full / DD_full,PIP
  is applied below θ_max = 0.2° (ξ) or 0.25° (P), and a new weight w_NTMP
  handles the many zero-probability galaxies of one-pass regions and
  priority conflicts. Fast fibre assignment gives fewer zero-probability
  pairs and a weaker collision window than altMTL, and is one suspected
  reason why the EZmock covariance has about 10% less power than it should.
- θ-cut: remove pairs below 0.05° and include the cut in the window, plus a
  rotation of data vector and window that removes sensitivity to high-k
  theory [src] (Pinon et al. 2024, arXiv:2406.04804). Validated on DESI DR1
  ELG mocks at 1.1 < z < 1.6 only; the rotation of data vector, window and
  covariance leaves the likelihood unchanged and lets the window be truncated
  at theory k_t < 0.2 h Mpc⁻¹ [src: arXiv:2406.04804, Sect. 6]. This is what the DESI
  DR1 cosmology fits use. Full-shape test [src: arXiv:2411.12021, Sect. 5.4,
  Figs. 7–8]: on 25 complete Abacus mocks the θ-cut changes nothing; complete
  versus altmtl mocks with the θ-cut scatter up to 2/5 σ_DR1 per bin, with σ8
  over-estimated in every bin, but the joint fit stays mostly within 1/5
  σ_DR1. Sect. 5.4 concludes "we do not report any residual systematic
  contribution", yet Table 7 lists ≈ 0.2 for fibre assignment and counts it
  in the 0.46 total; in the data-vector budget it enters only through the
  window-rotation marginalisation [src: Sect. 5.8].
- On BAO scales, nearest-neighbour up-weighting was adequate for eBOSS at
  s > 20 h⁻¹ Mpc (arXiv:2007.09005) [src: abstract].

**Validation.** Mocks with the real fibre-assignment code run on alternative
target ledgers ("altmtl") against "complete" mocks.

**Open point.** DESI stated that PIP weights were impractical for DR1 fits
because of the large single-pass area and expected them to be usable for DR2
[src] (arXiv:2411.12021).

## 5. Imaging systematics (target-density variations)
<!-- key: imaging-systematics-target-density-variations -->

**Mechanism.** Target density depends on depth, seeing, Galactic extinction
and stellar density of the imaging used for selection. The spurious power is
at large scales and mostly angular.

**Size.** The weights change the ELG clustering by Δχ² > 1000, yet the BAO
parameters move by at most 0.27σ (QSO α_iso), typically below 0.2σ, with no
coherent direction [src] (arXiv:2404.03000, Sect. 5.3). In full shape the
residual is about 0.2 σ_DR1 for ELG and QSO [src] (arXiv:2411.12021).

**Mitigation.** Weights from a regression of density on imaging maps: linear
for BGS and LRG, neural network (SYSNet) for ELG, random forest for QSO in DR1
[src] (arXiv:2411.12021, Sect. 5.5). Non-linear regressions remove real
modes, so DESI adds a mode-removal correction measured on mocks and a
polynomial template with amplitude s_p, marginalised with a Gaussian prior of
width 0.2 [src]. The effective model is theory + s_p Poly[(X_w − X_nw)^data
− (X_w − X_nw)^mock] + Poly[(X_w − X_nw)^mock], with Poly = c₋₅k⁻⁵ +
c₋₃k⁻³ + c₋₂k⁻² for P(k); in the baseline the mode-removal term is added to
the measured spectrum and (s_p X_poly)(s_p X_poly)ᵀ with s_p = 0.2 to the
covariance, which is analytic marginalisation over s_p. For ELG and QSO the
correction contributes up to 1/4 of the DR1 statistical error; for BGS and
LRG nothing beyond linear weights is detected [src: arXiv:2411.12021,
Sect. 5.5, Eq. 14]. For DR2 the QSO weights were switched from random forest to
linear regression [src] (arXiv:2503.14738). The low-k cut of the full-shape
fit, k_min = 0.02 h Mpc⁻¹, is set by how far the imaging correction is
trusted [src] (arXiv:2411.12021, Sect. 4.7). Forward modelling of the
selection with image simulations combined with neural-network regression is
explored for ELGs in Rosado-Marín et al. 2024, arXiv:2411.12024. That paper
[src: arXiv:2411.12024, Sects. 8.3, 9]: the ELG density depends mainly on
E(B−V), galactic depth and seeing; SYSNet weights are the DR1 ELG baseline;
Obiwan image simulations reproduce the trends qualitatively but not
statistically, so they are not used as the correction; depth-dependent N(z)
variations at 0.6 < z < 0.8 are the main reason the DR1 LSS catalogues keep
ELGs at 0.8 < z < 1.6 only; radial weights are negligible above z = 0.8.
Residual test: mitigation schemes compared by χ² of the multipoles, and BAO
fits with and without the fiducial weights for every tracer; the
unweighted-minus-weighted ξ_ℓ residuals show no BAO-like feature, even for
ELGs, the most contaminated tracer (plotted divided by 30 in Fig. 17).

**Validation.** Null tests of density versus each map after weighting;
contaminated and uncontaminated mocks through the same regression; weighted
versus unweighted BAO.

**For f_NL this is the limiting systematic.** Over-correction removes the
signal, under-correction mimics it. DESI DR1 modelled the angular integral
constraint induced by the weights as a window correction and improved the
radial integral constraint model [src] (Chaussidon et al. 2024,
arXiv:2411.17623). An earlier eBOSS analysis concluded that the modest gain
from optimal weights points to remaining unknown systematics in the data
[src] (Cagliari et al. 2024, arXiv:2309.15814).

**Reference for the SDSS era.** Ross et al. 2017, arXiv:1607.03145:
simulated systematic trends impart no bias on BAO and have a minor effect on
its uncertainty [src]. BOSS and eBOSS weights, budgets and the Euclid plan,
side by side: `boss-eboss-euclid.md`, Sects. 1–7.

## 6. Spectroscopic systematics
<!-- key: spectroscopic-systematics -->

**Mechanism.** The redshift success rate varies with observing conditions and
fibre; catastrophic redshifts displace a small fraction of objects radially;
redshift errors smear the line-of-sight clustering.

**Size.** Success-rate fluctuations of up to 3% with effective spectroscopic
signal-to-noise for LRG, BGS, QSO (Krolewski et al. 2024,
arXiv:2405.17208) [src: abstract]. For ELGs, 0.26% catastrophic redshifts in
DR1 and a redshift uncertainty of 8.5 km/s; the effect on RSD parameters is
below 0.2σ (Yu et al. 2024, arXiv:2405.16657) [src: abstract]. DR2 redshift
success: BGS 98.8%, LRG 99.0%, ELG 73.9%, QSO 68.0% (arXiv:2503.14738)
[src: Table 2]. eBOSS for comparison: 98% success for LRGs with under 1%
catastrophic failures; 95% and 2% for quasars (Ross et al. 2020,
arXiv:2007.09000) [src: abstract].

**Mitigation.** Redshift-failure weights and removal of badly performing
fibres.

**Validation.** Repeat observations for the error distribution; injection of
catastrophics in mocks.

**Space-based slitless surveys.** For Euclid the equivalent problems are the
angular modulation of the detection probability and line interlopers; the
mitigation is a random catalogue built from a detection model as a function
of emission-line signal-to-noise (Euclid Collaboration: Monaco et al. 2025,
arXiv:2511.20856).

## 7. Window, integral constraints and wide-angle terms
<!-- key: window-integral-constraints-and-wide-angle-terms -->

**Mechanism.** See `physics-and-methods.md` Sect. 2.3. Errors here act at
low k: wrong normalisation, missing radial integral constraint when
redshifts of randoms are drawn from the data, missing wide-angle terms in
the window.

**Mitigation.** Window-matrix formalism with wide-angle terms (Beutler &
McDonald 2021, arXiv:2106.06324; Beutler et al. 2019, arXiv:1810.05051);
integral-constraint corrections (de Mattia & Ruhlmann-Kleider 2019,
arXiv:1904.08851).

**Validation.** Mocks with the survey geometry and with redshifts of randoms
assigned as in the data; odd multipoles as a null test of the wide-angle
model.

**Relevance.** Negligible for BAO; small for RSD; decisive for f_NL.

## 8. Covariance
<!-- key: covariance -->

**Mechanism.** Approximate mocks miss part of the variance; a finite number
of mocks biases the inverse covariance; analytic covariances miss
non-Gaussian and observational terms.

**Size.** In DESI DR1 the EZmock covariance with fast fibre assignment
underestimates the errors: about 20% mismatch with the analytic covariance in
Fourier space once realistic fibre assignment is included, and a higher χ²
on data with EZmock than with RascalC covariances [src] (arXiv:2411.12021,
Sect. 5.7). For the 2PCF, analytic and mock errors on the BAO parameters
agree within 8% [src] (Rashkovetskyi et al. 2024, arXiv:2404.03007).

**Mitigation.** Tracer-dependent rescaling of the mock covariance, calibrated
on the data-tuned RascalC covariance in configuration space over
20 < s < 200 h⁻¹ Mpc [src] (arXiv:2411.12021); the factors 1/χ²_red are
1.39 (BGS), 1.15 (LRG1, LRG2), 1.22 (LRG3), 1.29 (ELG2), 1.11 (QSO)
[src: arXiv:2411.12021, Table 3, Sect. 5.7]. On mocks without fibre
assignment EZmock and analytic covariances agree in both spaces; with altmtl
assignment the Fourier-space mismatch is about 20% [src: Sect. 5.7]. Hartlap and Percival
corrections (Hartlap et al. 2007, arXiv:astro-ph/0608064; Percival et al.
2014, arXiv:1312.4841).

**Validation.** Mock versus analytic comparison per tracer (Forero-Sánchez et
al. 2024, arXiv:2411.12027); χ² distribution of mock fits.

## 9. Prior-volume (projection) effects
<!-- key: prior-volume-projection-effects -->

**Mechanism.** Marginalising over poorly constrained EFT parameters shifts
the marginal posterior away from the best fit. It is a property of the
inference, not of the data, but it changes quoted parameters.

**Size.** BOSS: posterior mean versus best fit up to 1σ or 2σ depending on
the prior set [src] (Simon et al. 2023, arXiv:2208.05929); frequentist
intervals up to 1.9 times wider (Holm et al. 2023, arXiv:2309.04468)
[src: abstract]. DESI DR1 in w0waCDM: shifts of 2.1σ, 4.1σ, 6.5σ, 6.3σ and
6.6σ in σ8, H0, Ω_m, w0 and wa between maximum likelihood and posterior mean
for full shape + BBN + n_s prior, without supernovae (Morawetz et al. 2025,
arXiv:2508.11811) [src: abstract; Sect. 4.2 for the parameter order].

**Mitigation.** Scaling bias parameters with σ8, dropping the hexadecapole
(DESI DR1 baseline); HOD-informed priors (arXiv:2504.10407); ShapeFit
compression (Forero-Sánchez et al. 2026, arXiv:2602.18761); profile
likelihoods alongside posteriors.

**Validation.** Noiseless synthetic data vectors fitted with the baseline
priors; MAP shown with every marginal posterior. DESI DR1 chose its priors
on the mean of 25 Abacus DR1 mocks [src: arXiv:2411.12021, Sect. 4.5.1,
Fig. 2]: counterterm widths of 20% and 50% of the linear signal at k_max
give similar results, 500% and flat priors give a much larger PVE, and with
the covariance rescaled to 25 times the DR1 volume both PVE and PWE nearly
vanish. Noiseless w0waCDM synthetic data with DR1 covariance isolate the
PVE alone [src: Sect. 4.5.2]. Reporting rule: marginal means and MAP are
both given [src: Sect. 4.5].

## 10. Reconstruction choices
<!-- key: reconstruction-choices -->

Smoothing scale, RSD treatment, bias and growth-rate inputs, and algorithm.
DESI finds the BAO constraints robust to all of them (Paillas et al. 2024,
arXiv:2404.03005) and carries no reconstruction term in its budget [src]
(arXiv:2404.03000). The errors from a wrong bias or fiducial cosmology in the
reconstruction are counted inside the HOD and fiducial-cosmology terms, not
separately [src: arXiv:2404.03000, Sect. 5.5].

## 11. Cross-release and cross-survey correlations
<!-- key: cross-release-and-cross-survey-correlations -->

Overlapping samples are correlated. DESI estimates the correlation between
power-spectrum estimates from overlapping samples with an effective-volume
formula: C ≈ 0.57 between DR2 LRG2 and eBOSS LRG, 0.21 for DR1
(arXiv:2503.14738) [src: Sect. III.3.2]; C = sqrt(N_DR1/N_DR2) between
releases for galaxies and C = 0.61 for Lyα [src: Sect. III.3.1 and its
footnote 12]. QSO versus ELG in 1.1 < z < 1.6 has C < 0.1 and is
ignored (arXiv:2404.03002) [src: Sect. 2.3.2]. Combining DR1 full shape with DR2 BAO
requires a joint mock covariance (arXiv:2602.18761).

## 12. Confirmation bias
<!-- key: confirmation-bias -->

Mitigated by catalogue-level blinding (Andrade et al. 2024,
arXiv:2404.07282); see `physics-and-methods.md` Sect. 5. A referee checks
which choices were frozen before unblinding and which tests were finalised
after: DESI notes, for example, that its fibre-assignment BAO test was
finalised after unblinding [src] (arXiv:2404.03000).

## 13. What a referee checks in a results section
<!-- key: what-a-referee-checks-in-a-results-section -->

1. Is the measurement stated as D/r_d (or α), with z_eff and its definition,
   and is the fiducial cosmology given?
2. Pre- or post-reconstruction? Which algorithm and convention?
3. Scale cuts (s_min, k_min, k_max), multipoles used, and who chose them
   when (before unblinding?).
4. Covariance: source, number of mocks, Hartlap/Percival factors, any
   rescaling, and its validation.
5. Systematic budget table with a stated threshold, and whether it is added
   at parameter or data-vector level.
6. Mock-recovery test at the statistical precision of the stacked mocks.
7. Fibre-assignment treatment (PIP, θ-cut, nearest neighbour) and the scales
   it is valid on.
8. Imaging weights: method, maps, null tests, and for f_NL the integral
   constraints.
9. For full shape: priors on nuisance parameters, MAP next to posterior
   means, sensitivity to prior width, and results with and without the BAO
   cross-covariance.
10. For f_NL: the b_φ assumption, stated next to the number.
11. Consistency across data splits (NGC/SGC, redshift bins, tracers) and
    between ξ and P.
12. Correlation with earlier releases or overlapping surveys when a shift is
    quoted in σ.
13. For any extended-model claim: which CMB likelihood, which supernova
    sample, which BBN prior.

## Not verified
<!-- key: not-verified -->

- The size of the wide-angle correction for BGS. (DR1 smoothing scales are
  now in `physics-and-methods.md` Sect. 2.5.)
- Redshift-error modelling for DESI quasars.
- Per-tracer full-shape HOD shifts (Table 2 of arXiv:2411.12023, not read)
  and the DR2 BAO mock-recovery table (Table VI of arXiv:2503.14742).
