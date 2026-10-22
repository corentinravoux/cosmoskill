# Optical selection and projection effects — cosmo-clusters dossier

Scope: how projection effects in optical richness are written into a
cluster analysis (the observed-given-true richness distribution and its
calibration, the selection bias of stacked lensing and clustering as a
boost function, an analytic bias model, a post-processing correction or a
full simulation-based forward model, scale cuts), how each is validated
against SZ cross-matches and spectroscopy, and what each choice was found
to cost. The most detailed projection modelling is DES redMaPPer work;
the HSC CAMIRA, SDSS redMaPPer with HSC lensing, KiDS AMICO, Euclid and
eROSITA cross-match routes are given beside it step by step.
Snapshot: 2026-10-21.
From: Miyatake 2025 review (arXiv:2505.07697), Sects. 3.1 and 5; DES
cluster analyses Y1, Y3 and Y6 strategy (arXiv:2002.11124,
arXiv:2503.13631); KiDS AMICO cosmology paper set (arXiv:2507.14338);
HSC CAMIRA papers (arXiv:1407.4693, arXiv:1701.00818,
arXiv:1904.07524); Euclid Cluster Finder Challenge (arXiv:1906.04707).

Already in L2, not repeated here: the mechanism, the history of the size
estimate (≤ 5% in 2014 to 20–30% in DES Y1), the simulated boosts of
Sunayama 2020 and Wu 2022, the SPT confirmation fractions and the
spectroscopic 16% in `systematics.md#optical-selection-projection-effects-and`;
the DES Y1 budget and the "−2 ± 3% replaced by −20 to −30%" lesson in
`systematics.md#des-y1-redmapper-counts-and-stacked-lensing-des`; the DES
Y3 data vector and the KiDS AMICO priors in the two sections after it;
the S8 values of each optical analysis and the DES Y1 story in
`results.md#the-des-y1-lesson`; the camps of the debate in
`open-questions.md#has-the-optical-selection-problem-been-solved`. The
cluster–galaxy and cluster–cluster statistics themselves are in
`deep/cluster-clustering.md`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Separate the richness noise from the richness–mass relation
<!-- key: step-1-separate-the-richness-noise-from-the -->

The count model is ⟨n(λ^ob, z)⟩ = ∫ dM n(M, z) P(λ^ob | M, z) (Eq. 1),
with n(M, z) the mass function; the observed-richness distribution is
split into a convolution P(λ^ob | M, z) = ∫ dλ^true P(λ^ob | λ^true, z)
P(λ^true | M, z) (Eq. 2), where P(λ^true | M, z) is the intrinsic scatter
and P(λ^ob | λ^true, z) the noise added by the observation [src: Sect. 2,
arXiv:1807.07072]. The reason given is to "disentangle any biases
introduced by the cluster finder and the characteristics of the survey
(e.g. photo-z uncertainty) from the underlying observable–mass relation";
the assumption that λ^ob is independent of mass at fixed λ^true is checked
on mocks [src: same]. The richness perturbation is written λ^ob = λ^true +
Δ^bkg + Δ^prj (Eq. 3): Δ^bkg is photometric and background-subtraction
noise, present even in unstructured fields; Δ^prj is the contribution of
member galaxies of other haloes along the line of sight [src: same].

Notation of the other papers: DES Y6 keeps a lognormal P(λ | M, z) with
σ²_lnλ = σ²_intrinsic + (e^⟨lnλ⟩ − 1)/e^{2⟨lnλ⟩} (Eq. 18), the second term
a Poisson contribution, and mean ln λ0 + A_λ ln(M/M_piv) + B_λ
ln((1 + z)/1.45) (Eq. 19) [src: Sect. II.3.3, arXiv:2503.13631]. KiDS
AMICO writes the intrinsic richness λ* with a lognormal of scatter σ_intr
around α + β log(M/M_piv) + γ log(H(z)/H(z_piv)) + log λ*_piv (Eqs.
20–21) [src: Sect. 5.1, arXiv:2507.14285].

HSC CAMIRA does not separate the two terms: Murata et al. fit a
lognormal P(ln N | M, z) to stacked lensing of 1747 CAMIRA clusters
(N ≥ 15, 0.1 ≤ z ≤ 1.0) and abundances, without informative priors
[src, arXiv:1904.07524], and state that its σ_lnN|M,z "should be
effectively regarded as a total scatter", including intrinsic scatter,
richness errors, halo orientation and projection [src: Sect. 4.1,
same]. Acceptable p-values required terms in ln(1 + z) and [ln(1 +
z)]² in the mean and scatter [src, same]; the middle redshift bin then
has a ⟨M | N⟩ about 20% higher and a slightly smaller scatter, which the
authors ascribe to a non-monotonic redshift dependence of the
projection effect, supported by cluster photo-z errors that are smallest
at 0.4 ≤ z ≤ 0.55 [src: Sects. 6.3 and 7, same]. The scatter is larger
for a Planck than for a WMAP cosmology and rises towards low richness
for Planck only [src, same]. The CAMIRA finder itself (red-sequence
colours from population synthesis, calibrated on spectroscopic galaxies)
was first run on SDSS DR8 and calibrated with CFHTLenS stacked lensing
including miscentring, N = 20 corresponding to M_vir ≈ 10¹⁴ h⁻¹ M_sun
[src, arXiv:1407.4693].

### Step 2. Calibrate the background noise by injection
<!-- key: step-2-calibrate-the-background-noise-by -->

Synthetic clusters of known richness are injected at catalogue level at
10000 random positions in the survey mask, with members drawn from the
self-trained red-sequence model and magnitudes perturbed by the local
depth, over a grid λ_in = 5 to 100 and z_in = 0.1 to 0.3 for SDSS [src:
Sect. 3.1, arXiv:1807.07072]. Δ^bkg is Gaussian N(Δμ, σ); Δ^prj from
uncorrelated structure is a delta plus a one-sided exponential,
P(Δ^prj) = (1 − f^prj) δ_D(Δ^prj) + f^prj τ e^{−τΔ^prj} Θ(Δ^prj) (Eq. 5),
with f^prj the fraction of clusters affected and 1/τ the typical richness
gained; their convolution (Eq. 6) has four parameters fitted per (λ, z)
grid point [src: same]. Injection at random points cannot capture
correlated structure, because clusters live in overdense regions, so this
step only sets the background part [src: Sect. 2, same]. A by-product:
the richness errors quoted in the redMaPPer catalogue underestimate the
true observational uncertainty by about 40–70%, because they assume the
membership probabilities are correct [src: Sect. 3.1, same].

The two calibration routes have a known trade-off, stated by the Euclid
Cluster Finder Challenge: end-to-end simulated data include "realistic
projection effects associated with the spatial correlation between
structures", which injection of simulated clusters into existing data
finds difficult to reproduce, a point "particularly relevant" for
finders based on the galaxy distribution [src: Sect. 1,
arXiv:1906.04707]. HSC CAMIRA uses a hybrid: mock galaxy samples from
the observed COSMOS-field HSC galaxies for the field and CAMIRA members
from the Wide survey for clusters, placed with N-body halo distributions
and keeping masks, matched to input haloes within 1 h⁻¹ Mpc and Δz <
0.1 [src: Sects. 6.1–6.2, arXiv:1701.00818]; the input richness–mass
relation and red fraction are assumptions, on which the scatter and
completeness, but not their qualitative behaviour, depend [src: Sect.
6.1, same]. AMICO in KiDS-DR3 uses mocks derived
directly from the data, preserving photo-z errors, absorption, missing
data and the spatial correlation of galaxies and clusters, "not
rely[ing] on the assumptions" of simulations and semi-analytic models
[src, arXiv:1810.02811]; its KiDS-1000 version is in Step 3.

### Step 3. Calibrate correlated projections in N-body simulations
<!-- key: step-3-calibrate-correlated-projections-in-n -->

Each halo of a light-cone receives a λ^true; the projected contribution
to cluster i is Δ^prj_i = Σ_{j≠i} f^A_ij w(Δz_ij, z_j) λ^true_j (Eq. 4),
with w the redshift kernel (1 at Δz = 0, 0 at large separation) and f^A
the overlap fraction of the two projected areas [src: Sect. 2,
arXiv:1807.07072]. The authors chose not to run the cluster finder on
mock galaxies, because projection depends on the red-sequence width and
its evolution, which mock catalogues do not reproduce; instead the kernel
is calibrated so that random injections in the simulation reproduce the
random injections in the data [src: same]. With clusters at their real
positions a percolation term is added, λ^ob = λ^true + Δ^bkg + Δ^prj +
Δ^prc (Eq. 13), with Δ^prc uniform in [−λ^true, 0] for a fraction f^msk
of masked clusters (Eq. 14); the full distribution is Eq. 15 [src:
Sect. 3.4, same]. 5000 realisations per (λ_in, z_in) are used [src: same].

KiDS AMICO takes a data-driven route instead: SinFoniA mocks built from
the KiDS-1000 galaxies, which keep galaxy and cluster autocorrelations,
the cluster–galaxy cross-correlation, masks and depth variations, are run
through AMICO; the fractional error x = (λ*_ob − λ*_tr)/λ*_tr is Gaussian
with mean μ_x = exp[−λ*_tr (A_μ + B_μ z_tr)] and width σ_x = A_σ
exp(−B_σ λ*_tr) (Eqs. 2–3), giving the mean and width of
P(λ*_ob | λ*_tr, z_tr) in Eqs. 22–23 [src: Sect. 3, arXiv:2507.14285].
The same mocks give purity (detections with a true counterpart over all
detections) and completeness as functions of observed and true richness
and redshift, which enter the counts as 1/P_clu and C_clu (Eq. 18), and
P(z_ob | z_tr) Gaussian with σ = 0.014(1 + z_tr) [src: Sects. 3 and 5.1,
same]. Impurities bias counts high and stacked lensing low [src: Sect. 3,
same].

The cosmology of the simulation matters for correlated structure: the
Euclid challenge mock has Ω_m = 0.25 and σ8 = 0.9, which the authors
expect "to lead to fewer projection effects with other clusters along
the line-of-sight and to increase the overall number of clusters" [src:
Sect. 6.2, arXiv:1906.04707]. Six finders (photometric-redshift
tomography, optimal filtering, hierarchical, wavelet and
friends-of-friends) were run blind on that mock; three reach > 80%
completeness at a mean purity of 80% down to 10¹⁴ M_sun and up to z = 2,
and AMICO (matched filter) and PZWav (adaptive wavelet) were selected
for the Euclid pipeline [src, same].

### Step 4. Model the selection bias of lensing and clustering
<!-- key: step-4-model-the-selection-bias-of-lensing-and -->

The common formalism: if ln λ and ln Σ (Σ the projected density, from
which ΔΣ follows) are bivariate Gaussian at fixed mass with correlation r,
then ⟨ln Σ | ln λ, M⟩ = ⟨ln Σ | M⟩ + r σ_lnΣ (ln λ − ⟨ln λ | M⟩)/σ_lnλ
(Eq. 8); the last term is the selection bias [src: Sect. 2,
arXiv:2203.05416]. In Buzzard the scatter σ_lnΣ peaks near 2 pMpc and
the correlation r near 0.4 pMpc for 5 × 10¹³ and 10¹⁴ h⁻¹ M_sun; Eq. 8
applied halo by halo reproduces the measured bias up to non-Gaussian
residuals [src: Sect. 5, same]. Because ΔΣ(r_p) contains Σ at all r <
r_p, the bias of ΔΣ survives at large radii where that of Σ has vanished
(≳ 20 pMpc) [src: Sect. 4, same]. A cylinder count of depth ±20–60 h⁻¹
Mpc reproduces the redMaPPer bias, which is why counts-in-cylinders mocks
are used as a cheap stand-in for the finder [src: Sect. 6.2, same].

Six ways of carrying this into a likelihood are in use, in order of
appearance; (b′) and (g) are two further routes, from HSC work.

**(a) A multiplicative correction to stacked masses.** DES Y1 corrected
its stacked lensing masses with a simulation calibration of the
"selection effect bias" finalised after unblinding; the earlier ≈ 4%
estimate had combined simulations and analytic arguments [src: Sect. I,
arXiv:2002.11124]. Sizes are in L2.

**(b) An anisotropic boost on the cluster bias.** Σ(R) = Π(R) Σ^iso(R)
and w_p(R) = Π²(R) w_p^iso(R) (Eqs. 14–15), with Π acting on Σ rather
than on ΔΣ so that it stays an effective scale-dependent cluster bias;
Π is linear in R up to a turnover R0 and logarithmic beyond (Eq. 16),
with Π0 and R0 per richness bin and c shared [src: Sect. 2.2,
arXiv:2112.09059]. The squared factor for clustering comes from the
simulation finding that the clustering boost is twice the lensing boost
[src: same]. The DES Y6 strategy paper reports that the Π(R) of the
published papers is a typo for 1 + Π(R) [src: Sect. IV.1.6, footnote,
arXiv:2503.13631]. The SDSS redMaPPer + HSC-Y3 analysis keeps the same
Eqs. (Eqs. 26–28 there) but uses one Π0 and R0 for all richness bins:
with the HSC-Y3 covariance, whose large scales are not shape-noise
dominated, the per-bin model of the earlier SDSS-lensing analysis
(arXiv:2112.09059) did not recover the input
cosmology on a noiseless mock, because the boost amplitude is
degenerate with the clustering and lensing amplitudes [src: Sects. 4.2
and 5.1, arXiv:2309.13025]. With shared parameters, mocks with
projection lengths of 60 and 120 h⁻¹ Mpc, 40% miscentred clusters and
a cluster photo-z scatter of 30 h⁻¹ Mpc were recovered [src: Sect. 5.1,
same], and the blind result is S8 = 0.816 +0.041/−0.039, consistent
with Planck 2018 [src, same], against S8 = 0.718 from the same finder
with SDSS lensing and per-bin boosts (Choices below).

**(b′) A boost on the halo bias of the clustering only (HSC CAMIRA).**
Chiu et al. self-calibrate the CAMIRA richness–mass normalisation from
ξ_cc, ξ_cg (with BOSS CMASS) and ξ_gg, modelling the cluster bias as a
linear combination of the bias without projection and the bias due to
projection, weighted by the probability f that a cluster is a
projection of two haloes (more than two being rare), following Baxter
et al. 2016 [src: Sect. 5.3, arXiv:2005.13564]. The normalisation A_N =
11.9 +3.0/−1.9 at M500 = 10¹⁴ h⁻¹ M_sun, z = 0.6 from all three
functions is consistent with weak-lensing magnification and with shear
+ abundance, with a ≲ 1.9σ preference for a lower value [src, same].

**(c) An empirical scale-dependent ratio (DES Y3 and Y6).** The ratio of
the selected to the original cluster lensing model is b_s1 + b_s2
exp(−θ χ(z̄)/r0); the cluster–galaxy ratio is the same; the cluster
autocorrelation ratio is its square (Eq. 23), b_s1 setting the
large-scale limit, b_s1 + b_s2 the zero-separation amplitude and r0 the
transition [src: Sect. II.3.5, arXiv:2503.13631]. The form was fitted to
HOD-cylinder mocks (cylinder lengths 90, 120, 150 h⁻¹ Mpc gave the same
result) and showed no richness dependence, so one set of parameters is
used for all richness bins [src: Appendix C, same]. A scale-dependent form
was adopted because the scale-independent DES Y1 model, with the lower
scale cuts of the new analysis, biased S8 and Ω_m by 0.45 of the
statistical error [src: Sect. II.3.5, same].

**(d) A forward analytical model.** The projected richness is written as
a line-of-sight integral over haloes weighted by a kernel w_z and overlap
f_A (Eqs. 3–4); the density of projected haloes uses a scale-dependent
optical cluster bias b_λob (Eq. 5), taken as a sigmoid between a
small-scale value b⁰ and a large-scale value b^∞ (Eq. 6) with k =
2.5/θ_λ and θ0 = θ_λ/2 fixed from mocks, b^∞ = b_eff (1 + 0.13 δ^prj)
(Eq. 7) with δ^prj the excess richness boost over a mass-matched random
sample, and b⁰ obtained by inverting the richness equation (Eq. 8) [src:
Sect. II.1, arXiv:2604.05833]. For λ^ob = 20 at z = 0.5 the mean bias is
2.1 times that of a mass-matched random sample at R = 0 and 5% higher on
large scales; the distortion persists to R ≈ 10 h⁻¹ Mpc; a double
power-law fitting function (Appendix C) is provided because the nested
integrals are expensive inside a sampler [src: Sects. II.1 and V, same].

**(e) A simulation-calibrated post-processing correction (Euclid).**
CosmoPostProcess paints galaxies on simulated haloes, assigns a
probabilistic richness λ = Σ P_mem/[(1 − f_bkg) C(m, z)] (Eqs. 6–7) in
the style of the Euclid richness estimator, applies miscentring and
baryonification, and measures the ratio of richness-selected to
mass-selected stacked profiles [src: Sect. 4.3.1, arXiv:2605.02723]. The
bias peaks at 20–40% near R ≈ 1 h⁻¹ Mpc, the two-halo term dominating
beyond 0.5 h⁻¹ Mpc; NFW fits give b_mass = ⟨M_fit/M_true⟩ = 1.22 for
projection only and 0.86 with miscentring and baryons, and the pure
selection term b_sel = M_fit(rich)/M_fit(mass-selected) averages 1.17
over 16 (z, λ) bins (Eqs. 15–16) [src: Sects. 5.1 and 5.6, same]. Because
the correction depends on cosmology (Step 5 of "Choices"), the plan is an
emulator over the PICCOLO cosmologies rather than recomputation inside
the likelihood [src: Sect. 5.4, same].

**(f) A full simulation-based forward model.** Salcedo et al. populate
N-body haloes with an HOD, weight galaxies along the line of sight by the
Costanzi et al. projection kernel with σ_z measured on DES Y1 (so the
depth is cosmology-independent), count N_cyl within R_λ = (N_cyl/100)^0.2
h⁻¹ physical Mpc, percolate by ranking haloes in mass down to 10¹¹ h⁻¹
M_sun, and map N_cyl to λ by abundance matching to the observed counts
(Eq. 5); each halo receives a centred and a miscentred richness, and
lensing is computed from the simulation with a baryonic model and
emulated over cosmology [src: Sects. III.2, IV.1, IV.3,
arXiv:2510.25706]. Here the selection bias is not modelled; it is present
in the mocks by construction.

**(g) A different mass proxy.** Huang et al. compare halo-mass tracers
at 0.2 < z < 0.5 with HSC galaxy–galaxy lensing: the outer stellar mass
M*[50,100] performs comparably to redMaPPer and CAMIRA richness above
log M_vir/M_sun = 14.0, and in N-body simulations haloes selected by it
have lensing profiles consistent with no projection or miscentring,
while richness-selected clusters show an excess at R ~ 1 Mpc "which may
suggest a more significant impact from selection biases" [src,
arXiv:2109.02646].

### Step 5. Choose scales
<!-- key: step-5-choose-scales -->

Scale cuts are the cheapest protection. KiDS AMICO fits stacked shear in
0.4–3.5 h⁻¹ Mpc: the inner cut reduces member contamination, the outer
cut reduces the dependence on correlated matter and "the impact of
possible anisotropic boosts"; multiplying the two-halo term by 1.2 to
mimic the simulated bias left the posteriors unchanged, and the authors
name the outer limit as "a key difference" from DES Y1, whose calibration
modelled lensing to 30 Mpc [src: Sects. 4.3 and 6.3, arXiv:2507.14285].
DES Y6 uses cluster lensing above 2 h⁻¹ Mpc, cluster clustering above
16 h⁻¹ Mpc and cluster–galaxy and galaxy clustering above 8 h⁻¹ Mpc, and
transforms γ_c into a localised Σ "more resilient to unknown small-scale
physics" [src: Sect. III.0.5, arXiv:2503.13631]. These two strategies are
opposite: KiDS discards large scales, DES discards small ones and models
the large-scale boost with clustering data to constrain it.

### Step 6. Validate against non-optical data
<!-- key: step-6-validate-against-non-optical-data -->

**SZ follow-up.** For each redMaPPer cluster the likelihood of its SPT
significance ξ given richness and redshift is Eq. 14, and of a
non-detection below the threshold Eq. 15; an extra non-detected fraction
π_cont (unvirialised red overdensities) enters as Eqs. 16–17 [src:
Sect. 3.2, arXiv:2502.12914]. Models compared: lognormal scatter,
contamination, mass-dependent scatter, the simulation-calibrated
projection model, and the projection model with a free amplitude
(α0), richness trend and redshift trend of τ (Eq. 19) [src: Table 1 and
Sect. 3.3, same]. Projection models are "for the most part, strongly
favored" over lognormal scatter, which the authors read as skewness that
neither contamination nor mass-dependent lognormal scatter can absorb;
the best model is the fully extended one, with a redshift trend in the
number of unassociated members that departs from the simulation, but its
preference over the plain projection model runs from "strong" to
"insignificant" depending on the complexity penalty [src: Sect. 4.2,
same]. The simulated fraction of unassociated members falls from about
30% at low richness to below 10% at high richness and is larger at high
redshift [src: Sect. 4.3.3, same].

**Spectroscopy.** DESI spectra of redMaPPer members show a projected
fraction more than twice as large at low richness as at high, and an
increase of up to 25% from z ~ 0.1 to z ~ 0.2 [src: abstract,
arXiv:2506.06249].

**X-ray cross-matches.** In the eRASS1 identification with redMaPPer
on the Legacy Surveys (eROMaPPer), 3% of clusters have overlapping
structures in projection and get a secondary redshift, 95 optical
detections were judged by eye to be in projection to the X-ray source,
and the i band rejected low-richness clusters with high contamination
probability, "for which the i-band might help to identify random
line-of-sight projections" (numbers in the table) [src: Sects. 4.1.1,
4.2.1 and 4.2.2, arXiv:2402.08453]. The paper quotes SDSS reshuffling
tests (purity ≳ 95%) as showing that redMaPPer clusters "are not
significantly affected by projection effects" [sec: Sect. 3.1,
arXiv:2402.08453, citing Rykoff et al. 2014], a test of detection
purity rather than of the richness boost. eFEDS candidates are
confirmed with MCMF and CAMIRA [src, arXiv:2106.14519]; S-PLUS matches
PZWav to eRASS1 at purities of 80–95%, stricter purity lowering
completeness mostly for low-luminosity systems, with more groups
recovered than by redMaPPer [src, arXiv:2607.02706].

**Weak-lensing selection.** Of 129 HSC-Y3 shear peaks (ν > 4.7), 126
have optical counterparts, the rest being line-of-sight projections or
offsets to low-mass haloes [src: Sect. 2.2, arXiv:2608.02755]; fCAMIRA
ranks all red-sequence counterparts along the line of sight by their
lensing contribution f_lens, and the ≈ 8% redshift outliers against a
positional match are "primarily attributed to projection effects" [src:
abstract and Sect. 4.2, same].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### How much of the richness noise model matters
<!-- key: how-much-of-the-richness-noise-model-matters -->

On a simulated SDSS-like counts + mean-mass data vector, Costanzi et al.
compared four models: the full Eq. 15 recovers the input; a model
calibrated only from random injections (no correlated structure) gives a
≈ 1σ cosmology bias, compensated by a steeper and higher richness–mass
relation; dropping percolation alone is harmless; Gaussian noise only
(the practice before 2019) biases the richness–mass relation and
disfavours the input cosmology at more than 2σ, with a fitted σ_intr ≈
0.5 against an input of 0.25 [src: Sect. 4, arXiv:1807.07072]. The
authors conclude the model is "necessary for Stage III dark energy
experiments, but not for stage II" [src: same]. Perturbing the
calibration (richness–mass parameters by 1σ, the kernel percentile, four
cosmologies outside the 95% region) left the recovered parameters
unchanged [src: same].

### How large the lensing mass bias is, by finder and galaxy model
<!-- key: how-large-the-lensing-mass-bias-is-by-finder -->

Fitting NFW mass and concentration to mock stacked ΔΣ with the DES Y1
covariance over 0.2–30 Mpc (11 bins), split at 3 Mpc: a counts-in-
cylinders mock on MiniUchuu gives ≈ 25% (small scales), ≈ 50% (large
scales), ≈ 25% (all), nearly independent of richness; redMaPPer on
Cardinal gives 20–40%, 20–80% and 20–50%, largest at z ≥ 0.5 and λ ≈ 20
[src: Sect. IV, arXiv:2510.00753]. The two simulations have similar σ8
(0.8159 and 0.82), so the authors attribute the difference to the
galaxy–halo connection and the cluster finder; for comparison the
SPT lensing systematics are 5–10%, at most 16% at z ≈ 1 [src: Sects. IV
and V, same]. Euclid's b_sel = 1.17 is at the low end of this range
[src: Sect. 5.6, arXiv:2605.02723].

Two readings follow. A small-scale-only fit is not bias-free: the
MiniUchuu small-scale bias equals the all-scale one, and Wu et al. find
the Σ bias peaking near 1 pMpc and, for high richness, 10–15% in the 3D
density at small radii [src: Sect. 4, arXiv:2203.05416]. The KiDS AMICO
test, which boosted only the two-halo term by 1.2, therefore does not
probe the one-halo part of the effect [der: comparison of the tests in
arXiv:2507.14285 Sect. 6.3 and arXiv:2510.00753 Sect. IV].

### The six model families compared
<!-- key: the-six-model-families-compared -->

| Family | Assumes | Buys | Costs | Used by |
|---|---|---|---|---|
| (a) mass correction factor | the simulation's galaxies and finder are right | simple | DES Y1: correction finalised after unblinding, cosmology still discrepant | arXiv:2002.11124 |
| (b) Π(R) boost | boost is a scale-dependent bias, clustering = boost² | lensing + clustering constrain it jointly | validated on 56 mocks yet S8 = 0.718 on SDSS; lensing at Planck cosmology "significantly underpredicts cluster masses" [src: Sect. 6, arXiv:2112.09059] | SDSS + SDSS lensing, SDSS + HSC Y3 |
| (c) b_s1 + b_s2 exp ratio | richness-independent, same for lensing and cluster–galaxy | three parameters, works with small scale cuts | needs w_cc and w_cg to constrain it; residual systematics < 0.3σ in Y6 mocks [src: Sect. IV.1.8, arXiv:2503.13631] | DES Y3, Y6 |
| (d) forward analytical model | P(λ^ob \| λ^true) and kernel known; no miscentring or orientation | links the bias to cosmology and survey depth | nested integrals; large-scale b^∞ not tested across cosmologies [src: Sect. V, arXiv:2604.05833] | proposed for DES |
| (e) post-processing correction | simulated galaxies and richness estimator are realistic | full one- and two-halo shape with baryons and miscentring | cosmology dependence needs an emulator; HOD-dependent at a few per cent | Euclid DR1 plan |
| (f) simulation-based forward model | HOD + cylinder kernel describe the finder | no separate bias model | emulator over cosmology; insensitive to ± 25% in depth and concentration, extra satellite scatter 0.2, percolation threshold at DES Y1 precision [src: Appendix A, arXiv:2510.25706] | DES Y1 reanalysis |

The Park et al. post-unblinding tests are the most instructive failure:
dropping the lowest richness bin moved nothing; removing clustering moved
S8 up towards other probes; lensing-only and clustering-only fits needed
boost amplitudes of 60–70%, which the authors judge not genuine given
expected values around 20% [src: Sect. 5.1, arXiv:2112.09059]. Their
model passed a blind mock challenge, so the failure points to a
difference between mocks and data, for which they name shear-specific
effects such as unmodelled intrinsic alignments or member confusion
[src: Sect. 6, same].

### Validation route
<!-- key: validation-route -->

SZ cross-matches calibrate projection only where SZ detects clusters
(the SPT-SZ × DES Y1 confirmations of L2 are at λ > 40) and cannot test photometric-redshift finders such as
AMICO, PZWav or WaZP, for which "no study of projection effects has been
carried out"; the authors expect them to be "equally, if not more
strongly, affected" because their line-of-sight kernel is wider than the
red sequence [src: Sect. 5.3, arXiv:2502.12914]. Spectroscopy reaches low
richness but only at low redshift (arXiv:2506.06249). AMICO and PZWav
rely instead on data-driven mocks and the Euclid challenge (Steps 2–3);
the KiDS-DR3 AMICO counts and lensing gave S8 = 0.78 ± 0.04 [src,
arXiv:2012.12273]. CAMIRA is tested against XXL and XMM-LSS X-ray
properties and centres [src, arXiv:1701.00818].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Injection grid | λ_in = 5–100 (10 values), z_in = 0.1–0.3 (5 values), 10000 positions each | SDSS redMaPPer | arXiv:1807.07072 | Sect. 3.1 |
| Underestimate of catalogue richness errors | 40–70% | SDSS redMaPPer | arXiv:1807.07072 | Sect. 3.1 |
| Correlated-structure boost of Δ^prj | × 2–4 for λ^true = 20–100; f^prj → 1 for λ^true ≳ 40 | SDSS mocks | arXiv:1807.07072 | Sect. 3.4 |
| Percolation | 5% of λ^true = 20 haloes lose > 50%; ± 15% percolation radius → ± 2% abundance | same | same | Sect. 3.4 |
| AMICO richness error | A_μ = 0.198 ± 0.005, B_μ = −0.179 ± 0.007, A_σ = 0.320 ± 0.008, B_σ = 0.011 ± 0.001; σ_x up to 35% above Poisson | KiDS-1000 | arXiv:2507.14285 | Sect. 3, Eqs. 2–3 |
| AMICO redshift error | σ = 0.014(1 + z) | KiDS-1000 | arXiv:2507.14285 | Sect. 5.1 |
| Lensing fit range | 0.4–3.5 h⁻¹ Mpc, 6 bins | KiDS-1000 AMICO | arXiv:2507.14285 | Sect. 4.3 |
| Scale cuts | γ_c > 2, w_cg and w_gg > 8, w_cc > 16 h⁻¹ Mpc; 20 log bins 2.5–250′ | DES Y6 strategy | arXiv:2503.13631 | Sect. III.0.5 |
| Bias of a scale-independent selection model | 0.45σ on S8, Ω_m | DES Y6 mocks | arXiv:2503.13631 | Sect. II.3.5 |
| ΔΣ selection bias | 20–60% at large r_p; Σ bias 10–20%, peak ≈ 1 pMpc | Buzzard redMaPPer | arXiv:2203.05416 | Sect. 4 |
| Lensing mass bias | 25% (MiniUchuu cylinders); 20–50% (Cardinal redMaPPer); large-scale 50% and 20–80% | DES Y1-like covariance | arXiv:2510.00753 | Sect. IV |
| Euclid selection bias | peak 20–40% at ≈ 1 h⁻¹ Mpc; b_sel = 1.17; lower-Ω_m cosmology lowers the peak by up to ≈ 9%; 2σ HOD changes: a few per cent | Euclid-like, PICCOLO | arXiv:2605.02723 | Sects. 5.1, 5.4–5.6 |
| Optical cluster bias, λ^ob = 20, z = 0.5 | 2.1 × random-selected at R = 0; + 5% at large R | DES Y3-like mock | arXiv:2604.05833 | Sect. II.1 |
| Unassociated members (simulation calibration) | ≈ 30% at low λ to < 10% at high λ | DES Y3 redMaPPer | arXiv:2502.12914 | Sect. 4.3.3 |
| Best-constrained combination | σ8 (Ω_m/0.3)^0.36 | DES Y1 forward model | arXiv:2510.25706 | Sect. VII.2, Eq. 34 |
| CAMIRA HSC catalogue | 1921 clusters, 0.1 < z < 1.1, N > 15 (≈ M200m ≳ 10¹⁴ h⁻¹ M_sun), ≈ 232 deg²; photo-z bias < 0.005, scatter < 0.01 | HSC S16A | arXiv:1701.00818 | abstract |
| CAMIRA completeness and purity | > 0.9 for massive clusters; 90 mocks, ≈ 144 deg² | HSC S16A | arXiv:1701.00818 | abstract; Sect. 6.2 |
| CAMIRA mass–richness | 1747 clusters; lensing S/N = 19 at 0.7 ≤ z ≤ 1.0; ⟨M \| N⟩ ≈ 20% higher in the middle z bin | HSC Y1 | arXiv:1904.07524 | abstract; Sect. 7 |
| CAMIRA clustering normalisation | A_N = 11.9 +3.0/−1.9 (ξ_cc + ξ_cg + ξ_gg), 21% error | HSC × BOSS CMASS | arXiv:2005.13564 | abstract |
| Boost mock tests | d_proj = 60, 120 h⁻¹ Mpc; 40% miscentred; σ_ph = 30 h⁻¹ Mpc: recovered | SDSS redMaPPer + HSC-Y3 | arXiv:2309.13025 | Sect. 5.1 |
| S8, shared boost | 0.816 +0.041/−0.039 | SDSS redMaPPer + HSC-Y3 | arXiv:2309.13025 | abstract |
| AMICO KiDS-DR3 | 7988 candidates, S/N > 3.5, purity ≈ 95%; 3652 with λ* ≥ 20 give S8 = 0.78 ± 0.04 | KiDS-DR3 | arXiv:1810.02811; arXiv:2012.12273 | abstracts |
| Euclid finder challenge | 6 finders; 3 with > 80% completeness at 80% purity to 10¹⁴ M_sun, z = 2; mock Ω_m = 0.25, σ8 = 0.9 | Euclid-like mock | arXiv:1906.04707 | abstract; Sect. 6.2 |
| eRASS1 optical projections | 332 (3%) overlapping in projection; 95 X-ray/optical projections; 446 rejected with i band, P_cont = 49% | eRASS1 × LS | arXiv:2402.08453 | Sects. 4.1.1, 4.2.1, 4.2.2 |
| eFEDS confirmation | 477 of 542; contamination 6 ± 3% (confirmed), 17 ± 3% (all) | eFEDS × HSC, LS | arXiv:2106.14519 | abstract |
| Shear-selected counterparts | purity ≳ 98% (126/129); ≈ 8% redshift outliers > 0.15 from projection | HSC-Y3 | arXiv:2608.02755 | Sect. 2.2; abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

| Failure | How it shows | Test that catches it | Source |
|---|---|---|---|
| Lognormal-only richness scatter | fitted scatter doubled; cosmology off by > 2σ in mocks | fit Eq. 15 or an SZ cross-match model comparison | arXiv:1807.07072, Sect. 4; arXiv:2502.12914, Sect. 4.2 |
| Projection calibrated at random points only | ≈ 1σ bias absorbed by the richness–mass slope | calibrate with clusters at their simulated positions | arXiv:1807.07072, Sect. 4 |
| Scale-independent selection model with small scale cuts | 0.45σ shift in S8 and Ω_m | mock analysis with a contaminated data vector | arXiv:2503.13631, Sect. II.3.5 |
| Π(R) implemented without the "1 +" | boost model wrong at all radii | check the convention against the original papers | arXiv:2503.13631, Sect. IV.1.6 |
| Model passes mocks, fails on data | low Ω_m and S8; lensing-only at Planck cosmology underpredicts masses | drop sectors of the data vector; split lensing at 8 h⁻¹ Mpc | arXiv:2112.09059, Sect. 5.1 |
| Galaxy model and finder dependence | 25% versus 20–50% mass bias for two simulations | run the calibration on more than one mock and finder | arXiv:2510.00753, Sect. IV |
| Cosmology dependence of the correction | up to ≈ 9% on the bias peak between two Ω_m | emulate the correction over cosmology | arXiv:2605.02723, Sect. 5.4 |
| Redshift trend absent in simulations | unmatched fraction versus redshift misfit | free redshift trend of τ (Eq. 19) | arXiv:2502.12914, Sects. 3.3, 4.2 |
| Miscentring correlated with projection | not modelled in the 2019 calibration | none stated; flagged as future work | arXiv:1807.07072, Sect. 2 |
| Selection correction decided after unblinding | large post-unblinding change | fix the correction and its prior before unblinding | arXiv:2002.11124, Sect. I |
| Per-bin boosts with a sample-variance-dominated lensing covariance | input cosmology not recovered on a noiseless mock | share the boost parameters across richness bins | arXiv:2309.13025, Sect. 5.1 |
| Redshift-dependent projection | non-monotonic ⟨M \| N⟩ and scatter with z | free ln(1 + z) and [ln(1 + z)]² terms; compare with cluster photo-z errors | arXiv:1904.07524, Sects. 6.3, 7 |
| Mock cosmology with low Ω_m or high σ8 | fewer projections than in the data | run calibration mocks at the current cosmology | arXiv:1906.04707, Sect. 6.2 |
| Wrong counterpart along the line of sight | wrong redshift (≈ 8% of shear peaks; 3% of eRASS1) | rank counterparts by lensing contribution; secondary redshifts; visual inspection | arXiv:2608.02755, abstract; arXiv:2402.08453, Sect. 4.2.1 |

Null and consistency tests stated in the papers read: cross-shear and
tangential shear around 50 times as many randoms consistent with zero,
χ²_red = 0.6 for g× (KiDS AMICO) [src: Appendix A, arXiv:2507.14285];
consistency of halo-run and finder-run data vectors in Cardinal (DES Y6)
[src: Sect. III.0.5, arXiv:2503.13631]; Σ8 consistent across richness,
redshift and scale splits at 2 h⁻¹ Mpc (DES Y1 forward model) [src:
Sect. VII.2, arXiv:2510.25706]. The DES Y6 pass criterion is that no
tested systematic biases the constraints by more than 0.3 of the
statistical uncertainty [src: Sect. IV.1.8, arXiv:2503.13631].

## Reading list
<!-- key: reading-list -->

- Foundation of the richness noise model: Costanzi et al. 2019
  (arXiv:1807.07072), Sects. 2–4, Eqs. 3–6 and 13–15.
- Formalism of the lensing selection bias: Wu et al. 2022
  (arXiv:2203.05416), Eq. 8 and Sects. 4–6; mitigation list in Sect. 7.2.
- Boost model and its failure on data: Park et al. 2021
  (arXiv:2112.09059), Sects. 2.2, 5 and 6.
- Current DES model and validation criteria: To et al. 2025
  (arXiv:2503.13631), Sects. II.3.3, II.3.5, III.0.5, IV.1 and Appendix C.
- Analytic forward model: Costanzi et al. 2026 (arXiv:2604.05833),
  Sect. II and Appendix C.
- Euclid correction: Euclid Collaboration 2026 (arXiv:2605.02723),
  Sects. 4.3 and 5.
- Simulation-based forward model: Salcedo et al. 2025 (arXiv:2510.25706),
  Sects. III–IV and Appendix A.
- Size of the mass bias by finder: Nde et al. 2025 (arXiv:2510.00753).
- Data-driven alternative and scale-cut strategy: Lesci et al. 2025
  (arXiv:2507.14285), Sects. 3, 4.3, 5.1 and 6.3.
- Critique from SZ data: Grandis et al. 2025 (arXiv:2502.12914),
  Sects. 3–5.
- HSC CAMIRA: Oguri 2014 (arXiv:1407.4693); Oguri et al. 2018
  (arXiv:1701.00818), Sect. 6; Murata et al. 2019 (arXiv:1904.07524),
  Sects. 4.1, 6.3; Chiu et al. 2020 (arXiv:2005.13564), Sect. 5.3.
- Shared boost with HSC-Y3 lensing: Sunayama et al. 2024
  (arXiv:2309.13025), Sects. 4.2, 5.1. Proxy with reduced projection:
  Huang et al. 2021 (arXiv:2109.02646).
- KiDS AMICO DR3: Maturi et al. 2019 (arXiv:1810.02811); Lesci et al.
  2022 (arXiv:2012.12273). Euclid finder challenge: Adam et al. 2019
  (arXiv:1906.04707), Sects. 1, 6.2.
- Cross-matches: eRASS1, Kluge et al. 2024 (arXiv:2402.08453), Sects.
  4, 7; eFEDS, Klein et al. 2022 (arXiv:2106.14519); S-PLUS, Doubrawa
  et al. 2026 (arXiv:2607.02706); HSC shear-selected, Chiu et al. 2026
  (arXiv:2608.02755).

## Not verified
<!-- key: not-verified -->

- The calibration of the redshift kernel width σ_z(z) (Sect. 3.2 of
  arXiv:1807.07072) and its validation (Sect. 3.3): not read.
- Eqs. 3–4 of arXiv:2510.25706, the galaxy weights of the cylinder count,
  did not render.
- The fitted values of b_s1, b_s2, r0 in the DES Y3 cosmology analysis
  (arXiv:2503.13632, Table 2 did not render in an earlier session).
- The SinFoniA mock method itself (Maturi et al.), known here only as
  described in arXiv:2507.14285.
- The body of the DESI spectroscopic study (arXiv:2506.06249): not read.
  The HSC shear-selected optical confirmation (arXiv:2608.02755) is now
  read in Sects. 2.2 and 4.2.
- CAMIRA has no dedicated P(λ^ob | λ^true) calibration in the papers
  read; the value of the projection probability f in arXiv:2005.13564
  and the body of the AMICO KiDS-DR3 selection paper (arXiv:1810.02811)
  were not read. Projection studies for the Euclid AMICO and PZWav
  samples (beyond the challenge) and for the final DES WaZP catalogue
  (title only): not read.
