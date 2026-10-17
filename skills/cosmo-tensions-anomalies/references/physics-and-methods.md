# Tensions and anomalies — definitions and how each is computed

Scope: how each tension or anomaly is defined and computed, and the tension metrics.

Snapshot: 2026-10-16

Flags as in `results.md`: `[src]` read this session in the cited paper;
`[sec: X]` taken from the reference files of sibling skill X (abbreviations
listed at the top of `results.md`); `[der]` derived here.

A tension is a statement about two data sets inside one model. An anomaly is
a statement about one data set against the model's sampling distribution.
Both need four things to be reproducible: the two inputs (or the input and
the null), the model, the metric, and the subspace or statistic. Most
disagreements about "how many sigma" in this field are disagreements about
one of these four, not about data.

## 1. Tension metrics
<!-- key: tension-metrics -->

### 1.1 Definitions
<!-- key: definitions -->

Read in Section 3.1 of Schöneberg et al. 2026 (arXiv:2607.13283) [src], which
follows the notation of Raveri & Hu 2019 (arXiv:1806.04649):

| Metric | Definition | What it uses | Weakness |
|---|---|---|---|
| Gaussian tension (Q_DM) | Δ_Gauss = sqrt[(μ_A − μ_B)ᵀ (C_A + C_B)⁻¹ (μ_A − μ_B)] [src: Eq. 16]; for one parameter, abs(μ_A − μ_B) / sqrt(σ_A² + σ_B²) | first two moments of each posterior | "typically fails to capture cases with non-Gaussian posteriors"; assumes independent data |
| Difference of maximum a posteriori (Q_DMAP), the goodness-of-fit loss | Δ_DMAP = sqrt(χ²_min,A+B − χ²_min,A − χ²_min,B) [src: Eq. 17] | best-fit likelihoods only | needs reliable minimisation; no penalty for extra parameters |
| Parameter shift | p(Δθ) = ∫ p_A(θ) p_B(θ − Δθ) dθ; probability that a shift is required = ∫ p(Δθ) dΔθ over the region where p(Δθ) > p(0); Δ_shift = sqrt(2) erf⁻¹ of that probability [src: Eqs. 18–20] | full posteriors | "can be affected by posterior-volume and projection effects that are absent in the likelihood-based metric" |

For Gaussian posteriors the three coincide [src]. The parameter-shift
integral is computed with the `tensiometer` package [src]. A model advances
in that comparison only with −ΔAIC > 10 or ln BF > 3 on the combined fit
with the M_B prior (arXiv:2607.13283) [src: Sect. III.3].

As defined in the body of Lemos et al. 2021 (arXiv:2012.09554) [src: Sect.
4], each with its defining paper:

| Metric | Definition (equation of arXiv:2012.09554) | Defining paper | Behaviour |
|---|---|---|---|
| Bayes (evidence) ratio | R ≡ Z_AB / (Z_A Z_B) (Eq. 5) = P(A\|B)/P(A) (Eq. 8) = ∫ P_A P_B / Π dθ (Eq. 9) | Marshall, Rajguru & Slosar 2006, arXiv:astro-ph/0412535 | global and symmetric; for a flat prior "doubling the prior volume doubles the value of R"; read on the Jeffreys scale (log R < −2.3 strong tension, −1.2 to 1.2 inconclusive, Table 2), whose boundaries "lack obvious interpretation as a statistical significance" |
| Suspiciousness | log S = log R − log I (Eq. 12), log I = D_A + D_B − D_AB with D the Kullback–Leibler divergence (Eqs. 10, 11) | Handley & Lemos 2019, arXiv:1902.04029 | prior-volume independent; for Gaussian posteriors χ²_d-distributed, d the Bayesian model dimensionality (Eq. 13), which gives a tension probability |
| Parameter difference (shift) | P(Δθ) = ∫ P_A(θ) P_B(θ − Δθ) dθ (Eq. 14); Δ = ∫ over P(Δθ) > P(0) (Eq. 15), invariant under reparametrisation; Monte Carlo with a Gaussian KDE | Raveri & Hu 2019, arXiv:1806.04649 [src: Eqs. 37–39]; Monte Carlo form cited to Raveri et al. 2020 (Raveri, Zacharegkas & Hu, arXiv:1912.04880, estimators for correlated data sets [src: abstract]) | for uncorrelated data sets only; normalising-flow estimators for many dimensions agree with the true tension to 0.2σ or better, 0.5σ in difficult cases (Raveri & Doux 2021, arXiv:2105.03324) [src: abstract] |
| Difference in means, update form | Q_DM = Δθ̄ᵀ C⁻¹ Δθ̄ with C = C_p1 + C_p2 for uninformative priors (Eqs. 45, 49 of arXiv:1806.04649); Q_UDM = (θ̂_A+B − θ̂_A)ᵀ (C_A − C_A+B)⁻¹ (θ̂_A+B − θ̂_A) (Eq. 16), χ² with rank(C_A − C_A+B) degrees of freedom, computed over KL modes with 0.2 < λ − 1 < 100 (Eq. 17) | Raveri & Hu 2019, arXiv:1806.04649 [src: Eqs. 49, 50] | for nested or correlated data; in non-update form with uninformative priors equivalent to the index of inconsistency (Lin & Ishak 2017, arXiv:1705.05303) |
| Goodness-of-fit loss | Q_DMAP = 2 ln L_A(θ_pA) + 2 ln L_B(θ_pB) − 2 ln L_A+B(θ_pA+B) (Eq. 19), χ² with ΔN_eff = N_eff^A + N_eff^B − N_eff^A+B degrees of freedom, N_eff = N − tr[C_Π⁻¹ C_p] (Eqs. 20, 21) | Raveri & Hu 2019, arXiv:1806.04649 | needs Gaussianity in data and parameter space |
| Eigentension | compare the two posteriors along the eigenvectors of one experiment's covariance whose prior-to-posterior variance ratio exceeds 10² (for DES Y1: e = σ8 Ω_m^0.57, ratio 2665, Eq. 22), then integrate the KDE of the difference inside the contour through the origin | Park & Rozo 2019, arXiv:1907.05798 | the threshold is ad hoc but fixed a priori on a noiseless data vector |

On simulated DES Y1 data shifted from Planck, the parameter-space metrics,
goodness-of-fit loss and suspiciousness track one another to within about
1σ, while log R stays in "strong agreement" up to an a-priori 1D tension of
about 1σ and turns to "strong tension" only near 4σ (arXiv:2012.09554) [src:
table in Sect. 4.6]. Two calibrations of R exist: by the other metrics on
simulations (arXiv:2012.09554) [src: Sect. 4.1], or against the distribution
of log R over matched simulations with neural ratio estimation (Bevins,
Handley & Gessey-Jones 2024, arXiv:2407.15478) [src: abstract], the method
used for the dipole in arXiv:2607.25703 [src: Sect. 2.3, Eq. 6].

Evidence-based metrics ask whether one parameter set can generate both data
sets; parameter-space metrics ask how significant the difference of the two
posteriors is in the parameters both constrain [sec: stat].

### 1.2 Converting to "sigma"
<!-- key: converting-to-sigma -->

- A probability p is quoted as the two-sided Gaussian equivalent n with
  erfc(n / sqrt 2) = p, unless a paper says otherwise. The CatWISE dipole
  result is one-sided: p = 5 × 10⁻⁷ is "4.9σ for a normal distribution,
  one-sided" (Secrest et al. 2021, arXiv:2009.14826) [src].
- A model-preference significance is not a tension. DESI converts Δχ²_MAP
  between w0waCDM and ΛCDM with two extra degrees of freedom: p = exp(−abs
  Δχ² / 2), so −12.5 gives 3.1σ [sec: stat]; DESI's table states the
  conversion as the significance "given 2 extra free parameters"
  (arXiv:2503.14738) [src: Table 6]. sqrt(abs Δχ²) is the conversion
  for one degree of freedom only.
- A local significance becomes a global one after dividing out the number of
  equivalent tests. For N independent looks p_global ≈ N p_local [sec: stat].
  Section 7 gives the worked case.

### 1.3 Rules that decide most disputes
<!-- key: rules-that-decide-most-disputes -->

1. Name the reference. H0: 4.4σ to 7.1σ for the same local value across four
   early endpoints (`results.md` §1.2). S8: four CMB endpoints from 0.819 to
   0.836 (`results.md` §2.1). CMB against DESI: 1.6σ to 3.7σ across CMB data
   sets (`results.md` §4).
2. Name the subspace. DES Y6 3×2pt against the CMB is 2.6σ projected on S8,
   2.2σ in the S8–Ω_m plane and 1.8σ in the full shared space
   (arXiv:2601.14559) [src: Sect. V.2]. The
   projected number is larger because S8 was chosen as the best-measured,
   most discrepant direction.
3. Compare the quantity that is measured. The ladder measures the SN Ia
   absolute magnitude M_B, not H0; the H0 World Cup quotes the ΛCDM
   discrepancy as "above 5.5σ in the supernova calibration parameter M_B" for
   CMB + BAO + SN because M_B "consistently incorporates the calibration
   information while accounting for the small Ω_m tension emerging between
   CMB, DESI BAO, and uncalibrated supernova data" (arXiv:2607.13283,
   conclusions) [src]. See also Efstathiou 2021 (arXiv:2103.08723) [sec: h0].
4. Do not use R, S or the convolution form on correlated data. ACT and SPT
   are calibrated on Planck and take τ from it; supernova compilations share
   their low-redshift objects; DESI DR1 and DR2 overlap [sec: cmb, de, stat].
5. Fix metric, subspace and reference before unblinding. DES Y6 uses
   n_σ ≡ sqrt(2) erf⁻¹(Δ) < 3, with Δ the parameter-shift probability
   estimated with normalising flows in tensiometer, as its criterion for
   combining data sets (arXiv:2601.14559) [src: Sect. IV.6, Eqs. 17–19].
6. A posterior mean is not a best fit. In extended models the two differ
   through prior-volume effects, which is why a Bayesian limit and a profile
   likelihood can disagree on the same data (early dark energy, Section 11).

## 2. H0 tension
<!-- key: h0-tension -->

Definition. The difference between H0 from a calibrated local distance scale
and H0 inferred in flat ΛCDM from data that fix the sound horizon r_d (CMB
anisotropies, or BAO with a BBN baryon density).

How the local side is built [sec: h0]: geometric anchors (Gaia parallaxes,
detached eclipsing binaries in the Magellanic Clouds, the NGC 4258 maser)
calibrate stellar standard candles (Cepheids, TRGB, JAGB, Miras), which
calibrate M_B of SNe Ia in common hosts; H0 follows from the intercept of
the SN Hubble diagram at 0.023 < z < 0.15 with q0 fixed. The tension
expressed in the measured quantity is 0.176 ± 0.035 mag in 5 log H0 for SH0ES
2022 against Planck (arXiv:2112.04510) [sec: h0].

How the early side is built [sec: cmb, h0]: the CMB fixes the angular
acoustic scale θ_* to 0.02% and, through the physical densities, r_d (147.00
± 0.24 Mpc for CMB-SPA, arXiv:2506.20707); H0 follows from the distance to
last scattering in the assumed late-time model. BAO measure D/r_d, so BAO +
BBN gives H0 without CMB anisotropies (arXiv:2503.14738).

Consequences of the construction.

- The early value is a ΛCDM inference; the tension is a statement that
  ΛCDM, the local calibration and the early data cannot all be right.
- BAO constrain the product H0 r_d and uncalibrated supernovae the shape
  E(z). A model that keeps r_d must change the shape, and the shape is
  measured (Section 11).
- The significance is computed as a Gaussian difference by every
  collaboration; the tables of `results.md` §1.2 follow that convention.

## 3. S8 tension
<!-- key: s8-tension -->

Definition. S8 ≡ σ8 (Ω_m / 0.3)^0.5 is the combination best constrained by
cosmic shear. The tension is the difference between S8 from a low-redshift
probe and S8 predicted in flat ΛCDM from the primary CMB.

How each side is computed [sec: wl, x, cl].

- Cosmic shear and 3×2pt: two-point statistics of galaxy shapes and
  positions, with nuisance parameters for shear calibration, redshift
  distributions, intrinsic alignments and baryonic feedback. The quoted
  point estimate (mean, mode or MAP) differs between surveys, and the mean
  and MAP of one posterior can differ by more than half an error bar.
- CMB-lensing tomography: cross-spectra of a lensing map with galaxies; the
  best-measured combination has an exponent near 0.25 to 0.4, not 0.5.
- Clusters: counts above a mass-proxy threshold with a lensing mass
  calibration; the best-measured combination has an exponent of 0.2 to 0.3.
- tSZ cross-correlations: the bias-weighted electron pressure ⟨b P_e⟩(z),
  which scales as S8^ε(z) with ε ≈ 3 over 0.1 ≤ z ≤ 1 in the FLAMINGO
  simulations and is boosted by feedback (Salcido et al. 2026,
  arXiv:2605.11083) [src], and is therefore sensitive to S8 and to the gas
  model in the same measurement.

Conventions that break comparisons: the exponent; the point estimate; the
CMB reference (Planck PR3, PR4, P-ACT, or the three-experiment combination);
projected against full-space metric; ΛCDM against wCDM chains.

## 4. CMB internal: A_L, tau, CMB-BAO discrepancy
<!-- key: cmb-internal-al-tau-cmb-bao-discrepancy -->

A_L. A phenomenological factor that rescales the lensing potential power
used to smooth the acoustic peaks of the TT, TE and EE spectra; A_L = 1 is
ΛCDM. It does not rescale the lensing reconstruction (four-point)
measurement, which is why a smoothing excess with a normal reconstruction
amplitude cannot be real lensing [sec: cmb; Motloch & Hu 2019,
arXiv:1912.06601]. SPT splits it into A_2pt (smoothing) and A_recon
(reconstruction) (arXiv:2506.20707) [sec: cmb]. The anomaly is A_L > 1 in a
ΛCDM + A_L fit to spectra.

τ. The Thomson optical depth to reionisation, measured from large-scale E-mode
polarisation; every analysis that includes CMB data takes it from Planck
low-ℓ EE, and ACT and SPT import it as a prior [sec: cmb]. The high-ℓ spectra
constrain the combination A_s e^(−2τ) (tabulated as such by SPT,
arXiv:2506.20707), so τ is degenerate with A_s and hence with the lensing
amplitude.

CMB–BAO discrepancy. Computed in ΛCDM in the plane of the two parameters BAO
measure, Ω_m and h r_d: DESI uses the Gaussian difference χ² = (p_A −
p_B)ᵀ(Cov_A + Cov_B)⁻¹(p_A − p_B) of the two posteriors, converted through
its probability to exceed (arXiv:2503.14738) [src: Eq. 18]; SPT quotes the
same two-parameter difference "accounting for the correlations between the
two parameters" as a one-dimensional Gaussian fluctuation (arXiv:2506.20707)
[src: Sect. VII.3]. Its size depends on the CMB data set because the experiments
differ in Ω_m.

Why one mismatch has several names. The CMB-inferred τ is anti-correlated
with the matter fraction, so dropping the low-ℓ EE data lets τ rise and
absorbs the discrepancy (arXiv:2504.16932) [sec: cmb]; the neutrino-mass
tension "largely arises from the CMB lensing constraints on the calibration
of the sound horizon" and relies on the same τ measurement (arXiv:2504.21813)
[sec: de]; with DESI the CMB prefers A_lens > 1, which SPT calls "a
rephrasing of the marginal agreement of the two probes in ΛCDM"
(arXiv:2506.20707) [sec: cmb]; Ω_K > 0 and w0wa change the geometry instead
[sec: inf, de]. Five parameters respond to one mismatch.

## 5. Dynamical dark energy preference and negative neutrino mass
<!-- key: dynamical-dark-energy-preference-and-negative -->

w0wa. w(a) = w0 + wa (1 − a). The preference is the improvement of the
best-fit χ² over ΛCDM, converted to σ with two degrees of freedom, with
ΔDIC as a companion and ln B from nested sampling as the Bayesian statistic
[sec: de, stat]. The three answer different questions: for DESI DR2 + CMB
they read 3.1σ, ΔDIC = −8.7 (arXiv:2503.14738) [src: Table 6] and ln B =
−0.57 ± 0.26 (arXiv:2511.10631) [src: Table 1]. The
preference is carried by a slope: at the pivot redshift the equation of
state is within about 2σ of −1 [sec: de].

Effective neutrino mass. The physical Σm_ν ≥ 0 is replaced by a signed
parameter whose negative values extrapolate the effect of mass on the
expansion history and on lensing; three inequivalent definitions are in use
[sec: nu]. The "tension with oscillations" is the distance of that
parameter from the minimum allowed by oscillation data (0.059 eV, normal
ordering). The width of a posterior truncated at zero is not a sensitivity
[sec: nu].

## 6. Cosmic dipole
<!-- key: cosmic-dipole -->

Kinematic expectation. An observer moving with velocity v = βc relative to
the frame in which distant sources are isotropic sees a dipole in the number
counts of a flux-limited sample, through aberration and Doppler boosting.
For sources with spectra S ∝ ν^(−α) and integral counts N(> S) ∝ S^(−x) the
amplitude is D_kin = [2 + x(1 + α)] β (Ellis & Baldwin 1984,
doi:10.1093/mnras/206.2.377; as written in Eq. 1 of arXiv:2009.14826 [src]). With the CMB dipole read as kinematic, β =
0.00123 (v = 369 km/s; arXiv:1303.5087) [src]. Because x and α are
properties of the sample, each catalogue has its own D_kin, and the test is
the ratio D_obs / D_kin together with the direction.

What the test assumes. (i) The CMB dipole is entirely kinematic. (ii) The
sources are distant enough that their own clustering dipole is small. (iii)
x and α measured at the flux limit describe the response of the whole
sample to a boost. Assumption (iii) is the subject of the theory critique:
if the spectral index and magnification bias evolve with redshift, the
standard expression may be inaccurate (Dalang & Bonvin 2022,
arXiv:2111.03616) [src]; the reply is that the Ellis–Baldwin test "is in
fact robust to such effects" (von Hausegger 2024, arXiv:2404.07929) [src].

Estimators in use [src, abstracts of the papers in `results.md` §7].

| Estimator | Used by | Remark |
|---|---|---|
| Linear and quadratic estimators on a masked sky | arXiv:2010.08366 | a linear estimator on a masked sky has a general bias in direction; a quadratic estimator recovers the direction to better than one degree and the amplitude to better than 10⁻³ for 10⁷ simulated sources (Siewert et al. 2021, arXiv:2010.08366) |
| Bayesian evidence comparison of hypotheses for the same counts | arXiv:2212.07733 | the Galactic mask leaks dipole power to higher multipoles |
| Negative-binomial likelihood | arXiv:2509.16732 | multi-component radio sources overdisperse the counts |
| Joint kinematic + residual model across catalogues | arXiv:2503.02470 | uses the different D_kin of each catalogue to separate the two |
| Simulation-based (neural ratio) tension | arXiv:2607.25703 | forward models selection effects such as Eddington bias |
| Mock-based null distribution with clustering and mode coupling | arXiv:2511.00822 | lowers the significance; fitting higher multipoles trades bias for variance |

Other dipoles that measure the same velocity.

- CMB aberration and modulation of the small-scale anisotropies, a
  measurement of β independent of the temperature dipole (arXiv:1303.5087).
- The redshift dipole: the Doppler modulation of observed redshifts in a
  spectroscopic survey, less sensitive to imaging systematics than counts
  (Wu & Xia 2026, arXiv:2608.30914) [src].
- The luminosity-distance dipole of supernovae at low redshift, which
  measures the observer's velocity relative to the supernova sample and is
  degenerate with the bulk flow of that sample (Sorrenti, Durrer & Kunz
  2024, arXiv:2403.17741) [src].
- The kSZ bulk-flow limit at Gpc scales (arXiv:2605.12499) [sec: pv].

In ΛCDM these dipoles should be aligned but need not have equal amplitudes,
because the intrinsic velocity of a source sample falls with its redshift
(the argument of Yoo, Magi & Huterer 2025, read in abstract this session;
not in `sources.tsv`).

## 7. Large-angle CMB anomalies
<!-- key: large-angle-cmb-anomalies -->

Each anomaly is a summary statistic of the temperature map whose observed
value lies in the tail of its distribution over isotropic Gaussian ΛCDM
simulations. The statistics named in the papers read this session [src]:

| Anomaly | Statistic as named | Source |
|---|---|---|
| Lack of large-angle correlation | S_1/2 ≡ ∫_{−1}^{1/2} [C(θ)]² d(cos θ), separations 60°–180°, masked sky, pseudo-C_ℓ to ℓ = 40; small because the ℓ = 2–5 contributions cancel those of higher ℓ, not because low-ℓ power is low (only C_2 is) [src: Eq. 7, 8] | arXiv:2310.12859 |
| Odd-parity preference | R^TT ≡ D_+(ℓ_max)/D_−(ℓ_max), with D_± the mean of ℓ(ℓ+1)C_ℓ/2π over even or odd ℓ; ℓ_max = 27, unmasked N_side = 64 sky [src: Eq. 9, 10] | arXiv:2310.12859 |
| Hemispherical variance asymmetry | σ²_16 ≡ mean of (T − T̄)² over the masked northern-ecliptic pixels of an N_side = 16 map; Planck 2013 found p ∼ 0.1% north, ∼ 45% south [src: Eq. 11] | arXiv:2310.12859 |
| Quadrupole–octopole alignment | S_QO ≡ (1/3) Σ |w^(2;1,2) · w^(3;i,j)|, with w the cross products of multipole vectors [src: Eq. 12, 13] | arXiv:2310.12859 |
| Hemispherical power asymmetry, dipolar modulation | variance-asymmetry estimators and ℓ to ℓ ± 1 mode coupling; angular clustering of local bandpower directions | arXiv:1906.02552; arXiv:2504.05597 |
| Lack of power | lower-tail probability of the low-ℓ variance, in temperature alone or jointly with polarisation | arXiv:2312.09989 |
| Cold Spot | "an unexpected cold ~10° region with p-value ≲ 0.01 in standard ΛCDM" | arXiv:2211.16139 |

A posteriori status. The Planck collaboration reports p-values for these
tests as null-hypothesis tests and does not combine them (arXiv:1906.02552)
[src]. Three structural facts set their weight:

1. The Planck 2015 release "essentially corresponded to the limit of our
   ability to probe CMB anomalies with temperature fluctuations alone";
   large-angle polarisation enables "largely independent tests"
   (arXiv:1906.02552, conclusions) [src].
2. The statistics were chosen after seeing the data, and several measure
   the same mode couplings (arXiv:1906.02552, conclusions) [src].
3. The joint probability of four of them, ≤ 3 × 10⁻⁸ (arXiv:2310.12859),
   becomes 3σ if the four smallest p-values were picked from about 16
   tests and 2σ from about 50 (Guth & Namjoo 2026, arXiv:2602.10178) [src].

How the look-elsewhere correction of arXiv:2602.10178 works: assume N
independent tests, select the four smallest p-values, and ask how often
their product is as small as observed; under the null each p-value is
uniform, so the density of the product follows in closed form [src: Sect.
II, Eqs. 1–11]; then raise N to account for the measured correlation among
the four (10 and 27 independent tests become 16 and 50). The paper lists 17
anomaly tests published in the literature, several with free parameters,
and argues that unreported null tests make 16 to 50 plausible [src: Sect.
IV, V].

## 8. Bulk flow
<!-- key: bulk-flow -->

The bulk flow is the volume average of the peculiar velocity field inside a
window; it is estimated from radial peculiar velocities (log-distance
ratios) with a maximum-likelihood or minimum-variance weighting that targets
an ideal window, and compared with the ΛCDM rms expected for that window
through a χ² with three degrees of freedom [sec: pv]. The amplitude, the
window, the depth and the error model are all part of the result.
Definitions, estimators and their equations are in
`cosmo-peculiar-velocities` `physics-and-methods.md` §6. A bulk flow at
150–200 h⁻¹Mpc is not the same test as the number-count dipole at Gpc
scales; they are related only if one posits a single coherent flow.

## 9. JWST high-redshift abundance
<!-- key: jwst-high-redshift-abundance -->

The argument of Boylan-Kolchin 2023 (arXiv:2208.01611) [src: Sect. 2]: the stellar
mass of a galaxy is limited by the baryons of its halo, M_* = ε f_b M_halo
with f_b = Ω_b/Ω_m = 0.156 (Planck 2018) and ε ≤ 1 the fraction converted into
stars; with the Sheth–Tormen mass function this gives n_gal(> M_*) ≤
n_halo(> M_*/f_b) and ρ_*(> M_*) ≤ f_b ρ_m(> M_*/f_b) [src: Eqs. 1–5]. The halo mass function therefore gives an upper limit on the
cumulative number density n(> M_*, z) and stellar mass density ρ_*(> M_*,
z). A measured density above the ε = 1 curve contradicts ΛCDM; one below
it constrains ε.

What enters the observed side: photometric or spectroscopic redshift; the
stellar mass from an SED fit, for which arXiv:2604.18683 names AGN
contamination, dust attenuation and the lack of JWST/MIRI constraints as the
systematic uncertainties [src]; the survey volume. Each can move a galaxy across the bound, which is why
the result depends on spectroscopy (`results.md` §10, `systematics.md` §8).
The same data constrain the UV luminosity function, where the comparison is
with a model of star-formation efficiency rather than with a hard bound
(Prada et al. 2026, arXiv:2604.18683) [src].

## 10. Curvature, birefringence, parity-odd 4PCF
<!-- key: curvature-birefringence-parity-odd-4pcf -->

- Curvature: Ω_K = 1 − Ω_tot, so Ω_K < 0 is closed. From the CMB alone it is
  measured through lensing smoothing and the geometric degeneracy, which
  ties it to A_L; with BAO it is measured geometrically, which ties it to
  the CMB–BAO mismatch and to the dark-energy model [sec: inf].
- Isotropic birefringence: a rotation β of the polarisation plane, which
  produces C_ℓ^EB = ½ sin(4β) (C_ℓ^EE − C_ℓ^BB); it is degenerate with a
  miscalibration of the detector polarisation angle unless that angle is
  known independently or foreground EB is used as a calibrator [sec: inf].
- Parity-odd four-point function: the parity-odd modes of the galaxy
  four-point correlation function; the detection statistic is a χ² against a
  mock covariance, which is biased if the parity-even eight-point function of the
  data differs from that of the mocks [sec: b2p].

Details in `cosmo-inflation-primordial` and `cosmo-beyond-two-point`.

## 11. Theoretical resolutions of the H0 tension
<!-- key: theoretical-resolutions-of-the-h0-tension -->

Classification, following the H0 World Cup (arXiv:2607.13283) [src]:

| Group | Mechanism | Examples tested there |
|---|---|---|
| E | early, non-radiative energy injection before recombination, or early modified gravity; reduces r_d | axion-like early dark energy, cold new early dark energy, early modified gravity |
| M | modified recombination | varying effective electron mass, four-parameter recombination history |
| R | additional radiation before recombination | free-streaming, self-interacting, Wess–Zumino dark radiation |
| L | late-time modification of the expansion history at fixed r_d | sign-switching cosmological constant, dark matter–dark energy interaction |
| E + L | both | thawing gravity |

Why early-time models. BAO fix H0 r_d; raising H0 by the required 8% at
fixed θ_* needs a smaller r_d or a change of the late-time distance integral.

The no-go arguments against late-time models.

- Calibration argument: the ladder constrains M_B, and any smooth change of
  H(z) at z > 0.02 is bounded by BAO and uncalibrated supernovae (Efstathiou
  2021, arXiv:2103.08723; Efstathiou 2026, arXiv:2607.29562) [sec: h0]. A
  model that fits SH0ES, DESI BAO and supernovae needs a step in M_B at z ~
  0.01 or a violation of distance duality (Bansal & Huterer 2026,
  arXiv:2602.06293) [sec: h0].
- Normalisation wall and shape wall: at fixed r_d and θ_s, δH0/H0 ≃ δI/I
  with I = ∫ dz/E(z); a non-parametric reconstruction of E(z) from
  unanchored Pantheon+ supernovae and DESI DR2 BAO allows a fractional
  increase of H0 of ≲ 2%, against ≳ 8% required, and the limit holds also
  when early-time physics is added (Sabogal et al. 2026, arXiv:2607.21244)
  [src].

The limits on early-time models.

- Reducing r_d alone conflicts with BAO or with weak lensing (Jedamzik,
  Pogosian & Zhao 2021, arXiv:2010.04158) [sec: h0].
- Raising H0 by modifying recombination "generically lowers Ω_m", which is
  inconsistent with late-time data: a perturbative m_e(z) history resolves
  the tension with Planck + ACT and no longer does once DESI DR2 BAO are
  added (Lee & Zhou 2026, arXiv:2606.06495) [src].
- H0 can be measured without r_d: calibrating the total energy density
  with the photon density, the BBN baryon-to-photon ratio and the
  baryon-to-matter ratio from clustering gives 69.0 ± 2.5 from DESI DR1 +
  θ_* + BBN, "robust to pre-recombination modifications such as Early Dark
  Energy" (Krolewski et al. 2025, arXiv:2511.23432) [src]. At that precision
  it does not discriminate.

Results of the model comparisons are in `open-questions.md` §2.

## Not verified
<!-- key: not-verified -->

- The amplitude of the dipolar modulation was not read (the definitions of
  S_1/2, R^TT, σ²_16 and S_QO are now in §7, from the body of
  arXiv:2310.12859).
- The values of x and α and the resulting D_kin for NVSS, RACS and LoTSS:
  not read at source. For CatWISE, the mean spectral index is 1.26 and the
  expected amplitude ∼0.007 (arXiv:2009.14826) [src: Sect. II, IV].
- The Thomson-scattering physics behind A_L as originally defined (the
  defining paper is cited in `cosmo-cmb`, not here).
