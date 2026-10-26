# HOD and CLF fitting — cosmo-galaxy-halo-connection dossier

Scope: how an occupation model is fitted to clustering (which prediction
engine: analytic halo model, direct population of a simulation, tabulation
or emulator; which statistic and binning; how the number density enters;
priors; covariance; sampler and convergence), how the CLF variant is
parametrised, and what each choice was found to cost when two were run on
the same data.
Snapshot: 2026-10-21.
From: Wechsler & Tinker 2018, Sect. 2.2.3; Asgari et al. 2023, Sect. 4.1;
DESI, eBOSS and SDSS clustering working groups.

Already in L2, not repeated here: the history of the HOD and the five-
parameter and tracer-specific forms (ELG central shapes, MTHOD) in
`physics-and-methods.md#halo-occupation-distribution-and-conditional`; the
DESI One-Percent LRG/QSO likelihood (Gaussian χ² plus half-normal density
term, 1800-box covariance, Hartlap ~6%) in
`physics-and-methods.md#galaxy-galaxy-lensing-with-clustering`; the occupation
statistics and the central condition in
`systematics.md#occupation-statistics-and-the-central-condition`; fitted
values per tracer in `results.md#occupation-of-haloes-by-tracer`. HOD fits on
fast-mock haloes for covariance mocks are in `cosmo-simulations-mocks`
(`deep/fast-mocks.md`); exclusion and non-linear halo bias in analytic models
in `physics-and-methods.md#the-halo-model-and-its-limits`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Fix the parameterisation and what it is written in
<!-- key: step-1-fix-the-parameterisation-and-what-it-is -->

Notation differs. The DESI and AbacusHOD form for LRGs and QSOs (Zheng et
al. 2007 as cited) is n̄_cent = (f_ic/2) erfc[log₁₀(M_cut/M)/(√2 σ)],
n̄_sat = [(M − κM_cut)/M_1]^α n̄_cent (arXiv:2306.06314, Eqs. 4–5): M_cut is
the minimum mass for a central, σ the width of the transition, M_1 the mass
with typically one satellite, α the slope, κM_cut the satellite cut-off,
f_ic ∈ (0, 1] an incompleteness down-sampling [src: Sect. 4.1]. For QSOs
the n̄_cent factor is dropped from the satellite term because "there is no
evidence that the existence of satellite QSOs are strongly associated with
central QSOs" [src: Eq. 6]. The SDSS DR7 form multiplies the central step
into the satellite term with an independent cut-off M_0 and normalisation
M_1′; M_min is the mass where ⟨N_cen⟩ = 0.5 and M_1 (≠ M_1′) the mass where
⟨N_sat⟩ = 1 (Zehavi et al. 2011, arXiv:1005.2413, Eq. 7) [src: Sect. II.3].
Aemulus writes the satellites as (M/M_sat)^α exp(−M_cut/M) N_cen
(arXiv:1804.05867, Eq. 7) [src]. DES Y3 writes ⟨N_c⟩ = (f_cen/2)[1 +
erf((log M_h − log M_min)/σ_log M)] and ⟨N_s⟩ = ⟨N_c⟩(M_h/M_1)^α with no
cut-off; f_cen, for redMaGiC only, multiplies centrals and satellites and
is fully degenerate with M_1 (arXiv:2106.08438, Eqs. 1–2) [src: Sect. 2.1].
The DESI BGS One-Percent fit (Pearl et al.) uses the SDSS form with log M_0
reparametrised as Q_0 ∈ [0, 1] between log M_min and log M_1
(arXiv:2309.08675, Eqs. 1–3) [src: Sect. II.2.2]. Read which mass is
called M_1 before comparing.

Phase-space parameters in current use [src: arXiv:2306.06314, Sect. 4.1,
Eqs. 7–8]: central line-of-sight velocity v_cent,z = v_L2,z + α_vel,c
δv(σ_LoS), α_vel,c ≥ 0 because its sign is unobservable; satellite velocity
v_sat,z = v_L2,z + α_vel,s (v_p,z − v_L2,z), α_vel,s = 1 meaning satellites
track their particles. Aemulus uses η_con = c_sat/c_halo, η_vs and η_vc
(velocity-dispersion ratios) [src: arXiv:1804.05867, Sect. II.3]. The
DESI One-Percent baseline is the five vanilla parameters plus f_ic, α_vel,c
and α_vel,s: eight in all [src: arXiv:2306.06314, Sect. 4.1].

**CLF variant.** Φ(L|M) = Φ_c + Φ_s (arXiv:1207.0503, Eq. 3), centrals
log-normal in L with constant scatter σ_c (Eq. 4), satellites a modified
Schechter function falling as exp[−(L/L*_s)²] (Eq. 5); L_c(M) = L_0
(M/M_1)^γ1 / [1 + M/M_1]^(γ1−γ2) (Eq. 6); L*_s = 0.562 L_c (Eq. 7); constant
faint-end slope α_s (Eq. 8); log φ*_s = b_0 + b_1 log M_12 + b_2 (log
M_12)² (Eq. 9). Nine parameters (Eq. 10). The authors state that these forms
have no physical motivation; they describe the SDSS group-catalogue CLF
[src: Sect. 3.2]. An HOD follows from the CLF by integrating over
luminosity; the CLF "typically requires stronger prior assumptions", while a
five-parameter HOD is already flexible enough for luminosity-threshold
samples [src: arXiv:1005.2413, Sect. II.3]. KiDS-1000 uses the stellar-mass
version (CSMF, after Yang et al. 2008): the same central and satellite
shapes in M_⋆, M*_s = 0.56 M*_c, log φ*_s = b_0 + b_1 log m_13 (no quadratic
term), σ_c and α_s independent of halo mass, and a mass-dependent Poisson
parameter 𝒫(M) = ⟨N_s(N_s − 1)⟩/⟨N_s⟩² for the satellite–satellite term
(arXiv:2210.03110, Eqs. 16–25) [src: Sect. 2.2]. Halotools (Hearin et al.
2017, arXiv:1606.04106) implements HOD, CLF, abundance matching and
assembly-bias variants as interchangeable components populating a halo
catalogue, with mock clustering, lensing and group statistics [src:
abstract]; the DESI BGS fit runs on it.

### Step 2. Choose the prediction engine
<!-- key: step-2-choose-the-prediction-engine -->

| Engine | What is computed per likelihood call | Analysis | Place read |
|---|---|---|---|
| Analytic halo model | w_p from HMF, bias, NFW with c(M) = 11 (M/M_nl)^(−0.13)/(1+z), M_nl = 2.26 × 10¹² h⁻¹M_⊙; Tinker et al. n̄′_g-matched exclusion, accurate to 10% or better | SDSS DR7 | arXiv:1005.2413, Sect. II.3 |
| Analytic halo model + CLF | Φ(L), w_p and ΔΣ; model accurate to 10% (mostly 5%) for 3D statistics, so no modelling error is put in the likelihood | SDSS, Cacciato et al. 2013 | arXiv:1207.0503, Sect. 4 |
| Emulated halo statistics + HOD at equation level | Dark Emulator HMF, halo–matter and halo–halo terms, integrated over a five-parameter HOD | HSC-Y1 × SDSS | arXiv:2111.02419, Sect. IV.1, App. C |
| Direct population of a simulation | populate halos and particles, apply RSD, count pairs (Corrfunc) | DESI One-Percent, AbacusHOD | arXiv:2306.06314, Sect. 4.3; arXiv:2110.11412, Sect. 4 |
| Tabulation | pre-computed halo–halo, halo–particle, particle–particle w_p per mass-bin pair, weighted by the HOD (Eqs. 14–16) | DESI One-Percent, mass-only HOD on w_p + n_z | arXiv:2306.06314, App. A |
| GP surrogate of χ² | 20 mocks per point, mean χ² and its error fed to a Gaussian process, refined iteratively | DESI One-Percent ELG | arXiv:2306.06319, Sect. 5.1 |
| GP emulator of the statistic over cosmology + HOD | 15 inputs; trained on 2000 HOD designs over N-body cosmologies | Aemulus | arXiv:1804.05867, Sect. III |
| Same, applied | ξ_0, ξ_2, w_p at 0.1–60 h⁻¹Mpc with a halo-velocity scaling γ_f | Aemulus V, BOSS | arXiv:2203.08999, abstract |
| Analytic halo model + CSMF | SMF, ΔΣ and w_p with non-linear halo bias β^NL from an emulator, updated from the median walker position rather than at each step | KiDS-1000 | arXiv:2210.03110, Sects. 2.2, 3.6 |
| Halo model for γ_t | HOD + halo model, with satellite stripping, point mass, magnification and IA terms, to ~100 kpc | DES Y3 redMaGiC, MagLim | arXiv:2106.08438, abstract, Sect. 3 headings, Sect. 6 |
| Pretabulation (galtab) | Halotools HOD on SMDPL (400 h⁻¹Mpc); CiC predicted from placeholder galaxies, Monte Carlo or analytic mode, GPU-portable | DESI One-Percent BGS | arXiv:2309.08675, Sects. II.3, III.4–III.6 |

Direct population runs fast enough to sample with: on one 32-core node,
populating a downsampled AbacusSummit box at CMASS density takes 0.17 s and
ξ(r_p, π) 0.18 s, just under 0.4 s per call; halos are downsampled from 3.99
× 10⁸ to 6.18 × 10⁶ and particles from 3.15 × 10⁸ to 1.77 × 10⁷ with
mass-dependent filters (arXiv:2110.11412, Eq. 13) [src: Sect. 4.4].
Tabulation gives the mean prediction rather than one noisy realisation,
"which further reduces the bias of HOD fitting", but each extra dependence
(velocity or assembly bias) adds a tabulation dimension, so DESI used it
only for the mass-only model on w_p [src: arXiv:2306.06314, App. A].

### Step 3. Choose the statistic and binning
<!-- key: step-3-choose-the-statistic-and-binning -->

| Analysis | Statistic | Binning | Place read |
|---|---|---|---|
| SDSS DR7 | w_p, π_max = 60 h⁻¹Mpc (40 for low-z samples), 0.2 dex r_p bins, 2 h⁻¹Mpc π bins | residual RSD not modelled | arXiv:1005.2413, Sect. II.2 |
| SDSS decorated HOD | w_p, 11 bins 0.17–16.9 h⁻¹Mpc | — | arXiv:1606.07817, Sect. 2.3 |
| DESI One-Percent LRG/QSO | ξ(r_p, π) primary, w_p alongside | 14 log r_p bins 0.15–32 h⁻¹Mpc; π 0–32 in 4 h⁻¹Mpc bins; w_p with π_max = 32 | arXiv:2306.06314, Sect. 2.2 |
| DESI One-Percent ELG | w_p, ξ_0, ξ_2 | w_p: 17 log bins 0.04–32 h⁻¹Mpc, π ± 40; multipoles: 27 log bins 0.17–32 h⁻¹Mpc | arXiv:2306.06319, Sect. 2.1 |
| AbacusHOD CMASS | w_p, then ξ(r_p, π) | ξ: 8 log r_p bins 0.169–30, 6 linear π bins 0–30 h⁻¹Mpc | arXiv:2110.11412, Sect. 4.4 |
| HSC-Y1 × SDSS | w_p and ΔΣ, no n̄_g | w_p 16 bins 2–30, ΔΣ 9 bins 3–30 h⁻¹Mpc; 75 points for three samples | arXiv:2111.02419, Sect. IV.2 |
| DESI One-Percent BGS | n_gal, w_p, counts-in-cylinders P(N_CiC) | w_p: 12 log bins 0.158–39.81 h⁻¹Mpc, π_max = 40; cylinders R = 2, half-length 10 h⁻¹Mpc; 28 N_CiC bins | arXiv:2309.08675, Sects. II.3, II.3.1 |
| DES Y3 | γ_t per lens–source bin pair, plus n̄_g for redMaGiC | 30 angular bins per pair, down to ~100 kpc | arXiv:2106.08438, Sects. 5.2, 6 |
| KiDS-1000 | SMF, ΔΣ, w_p jointly | full covariance with cross-terms | arXiv:2210.03110, Sect. 3.6 |

Why ξ(r_p, π): its r_p dependence traces the one- to two-halo transition
and its π dependence the velocities and fingers of God; w_p is "strictly
less informative" but easy to visualise, easy to get a covariance for and
free of velocity modelling [src: arXiv:2306.06314, Sect. 2.2]. Why DESI
stopped at 32 h⁻¹Mpc: to capture the one-halo regime and the transition
"while limiting our exposure to large scale modes due to the small
footprint" [src: same]. Why SDSS dropped two large-r_p points: they add
cost but change results insignificantly [src: arXiv:1606.07817, Sect. 2.3].
Why counts-in-cylinders: 2 h⁻¹Mpc cylinders mainly count intra-halo
neighbours, so they probe satellite occupation and assembly bias; w_p could
be replaced by ξ_0 and ξ_2 "at the expense of additional degrees of
freedom" [src: arXiv:2309.08675, Sect. II.3].

### Step 4. Put in the number density
<!-- key: step-4-put-in-the-number-density -->

Three treatments:

1. Gaussian term: (n_g − n_g*)²/σ²_ng with a 5% uncertainty (arXiv:1005.2413,
   Eq. 8) [src]; Poisson σ_n in the decorated-HOD fit (arXiv:1606.07817,
   Eq. 6) [src].
2. One-sided term with incompleteness: penalty only when the mock is
   below the data; otherwise f_ic = n_data/n_mock down-samples the mock at
   no cost (arXiv:2306.06314, Eq. 11; arXiv:2110.11412, Eq. 18). It "allows
   for incompleteness in the observed galaxy sample while penalising HOD
   models that produce insufficient galaxy number density" [src]. Values:
   σ_n = 0.1 n_data (DESI); n_data = 3.0 × 10⁻⁴ and σ_n = 4.0 × 10⁻⁵ h³Mpc⁻³,
   "rather lenient" (AbacusHOD CMASS) [src].
3. Fixed density by construction: the ELG pipeline rescales A_c and A_s by
   a common factor so that every mock has 10⁻³ h³Mpc⁻³; their ratio sets the
   satellite fraction and the clustering does not depend on the common
   factor; M_1 is fixed to 10¹³ h⁻¹M_⊙ because it is degenerate with A_s
   and α [src: arXiv:2306.06319, Sect. 3.3].

4. Density as one entry of the data vector: DES Y3 appends n̄_g to the
   redMaGiC γ_t vector with its variance on the diagonal, which "effectively
   serves as a prior", and leaves it out for MagLim [src: arXiv:2106.08438,
   Sect. 6]; the BGS fit puts n_gal (inverse-probability weighted) inside
   the jackknife covariance with w_p and CiC [src: arXiv:2309.08675, Sects.
   II.3, II.3.1].

HSC-Y1 × SDSS uses no abundance term at all [src: arXiv:2111.02419, Sect.
IV.2]; KiDS-1000 fits the stellar mass function itself [src:
arXiv:2210.03110, Sect. 3.6].

### Step 5. Build the covariance
<!-- key: step-5-build-the-covariance -->

- **Jackknife.** SDSS DR7: 144 regions of ~55 deg². Jackknife and external
  estimates agree on large scales; jackknife somewhat overestimates errors
  at r_p ≲ 2 h⁻¹Mpc (Norberg et al., as cited); mocks would include cosmic
  variance at the survey scale, but a new mock set per sample was
  impractical; fits with diagonal errors only are shown as a check [src:
  arXiv:1005.2413, Sect. II.2].
- **Mock correlation, data diagonal.** DESI One-Percent: a 128-region
  jackknife of ξ(r_p, π) was "noisy and close to singular", so (i) a
  baseline HOD is fitted with jackknife diagonals only; (ii) its best fit
  populates the 1800 AbacusSummit 500 h⁻¹Mpc boxes; (iii) the mock
  correlation matrix is kept and rescaled with the jackknife diagonals
  [src: arXiv:2306.06314, Sect. 5]. Small scales are shot-noise dominated
  and nearly independent; QSO matrices are essentially diagonal [src:
  same]. The ELG analysis does the same with K-means jackknife regions
  [src: arXiv:2306.06319, Sect. 5.2].
- **Model covariance added.** The ELG GP pipeline adds C_model: a fixed
  correlation matrix from 1000 realisations at a reference HOD, scaled by
  the quadrature sum of the stochastic variance of the 20 mocks at the
  current point and the cosmic variance from 48 sub-cubes of 1 h⁻¹Gpc,
  χ² = Δᵀ[C_data/(1 − D_data) + C_model/(1 − D_model)]⁻¹Δ with D the Hartlap
  factor of each part (arXiv:2306.06319, Eq. 11) [src].
- **Jackknife with Hartlap, lensing.** DES Y3: 150 k-means patches at least
  as large as the largest angular scale; N_θ/N_JK = 0.2, Hartlap factor
  applied; the authors note that it unbiases C⁻¹ but can still inflate the
  intervals [src: arXiv:2106.08438, Sect. 5.2].
- **Few regions, pseudo-inverse.** DESI BGS: 20 jackknife regions, "somewhat
  noisy" but smaller regions would break independence and cut CiC edges;
  the Moore–Penrose pseudo-inverse handles the singular matrix, after
  rescaling to unit diagonal so that n_gal is not lost to machine precision
  [src: arXiv:2309.08675, Sects. II.3.1, IV].

### Step 6. Sample and check convergence
<!-- key: step-6-sample-and-check-convergence -->

| Analysis | Sampler | Settings and convergence | Place read |
|---|---|---|---|
| SDSS DR7 | Metropolis random walk, Gaussian steps; acceptance written exp[−(χ²_new − χ²_old)] | ~10 000 steps per sample; convergence by comparing chains | arXiv:1005.2413, Sect. II.3 |
| SDSS decorated HOD | emcee | ~3–10 × 10⁶ samples | arXiv:1606.07817, Sect. 2.3 |
| AbacusHOD CMASS | dynesty, also for evidences | 500 live points, uniform sampler, stop at d log 𝒵 > 0.01 | arXiv:2110.11412, Sect. 5.2 |
| DESI One-Percent LRG/QSO | dynesty, after optimisation | Gaussian priors with bounds | arXiv:2306.06314, Sect. 6.1 |
| DESI One-Percent ELG | GP surrogate + MCMC | 800 Hammersley points, then 800 iterations; converged when the KL divergence between successive chains is < 0.1 for 20 consecutive iterations, after removing points whose GP χ² error exceeds 10 | arXiv:2306.06319, Sect. 5.1 |
| HSC-Y1 × SDSS | MultiNest | nestcheck; four seeds give S8, σ8, Ω_m scatter < ~0.1% of the central values (< ~2% of σ) | arXiv:2111.02419, App. D |
| DES Y3 γ_t | MultiNest | Hartlap-corrected Gaussian likelihood | arXiv:2106.08438, Sect. 6 |
| KiDS-1000 | emcee, stretch and KDE moves mixed 50/50 | more walkers, shorter autocorrelation times | arXiv:2210.03110, Sect. 3.6 |
| DESI One-Percent BGS | emcee, 20 walkers × 3000 iterations, burn-in 2000 trial points | autocorrelation 100–300, about half that of Monte Carlo CiC; deterministic likelihood | arXiv:2309.08675, Sect. IV |

The acceptance rule of the SDSS DR7 code as printed lacks the factor ½ of
a likelihood ∝ exp(−χ²/2) [der: compare arXiv:1005.2413, Sect. II.3 with
Eq. 8 there]; a reader reproducing it should check which was used.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Priors: flat, Gaussian, bounded
<!-- key: priors-flat-gaussian-bounded -->

| Analysis | Parameter | Prior | Place read |
|---|---|---|---|
| SDSS DR7 | mass scales flat in log, σ_log M and α flat in linear | — | arXiv:1005.2413, Sect. II.3 |
| SDSS decorated HOD | log M_min, log M_0 [9, 14]; log M_1 [10.7, 15]; σ_log M [0.01, 1.5]; α [0, 2] (uniform) | only log M_0 and σ_log M priors matter | arXiv:1606.07817, Table 1 |
| AbacusHOD CMASS | log M_cut N(13.3, 0.5); log M_1 N(14.3, 0.5); σ N(0.5, 0.2); α N(1.0, 0.3); κ N(0.5, 0.2) | "broad non-informative width" | arXiv:2110.11412, Table 1 |
| DESI One-Percent LRG | log M_cut N(13.0, 1.0) in [12, 13.8]; log M_1 N(14.0, 1.0) in [12.5, 15.5]; σ N(0.5, 0.5) in [0, 3]; α N(1.0, 0.5) in [0, 2]; κ N(0.5, 0.5) in [0, 10]; α_c N(0.4, 0.4) in [0, 1]; α_s N(0.8, 0.4) in [0, 2] | columns read as prior then bounds; header not rendered | arXiv:2306.06314, Table 2 |
| DESI One-Percent QSO | log M_cut N(12.7, 1) in [11.2, 14]; log M_1 N(15.0, 1) in [12, 16]; σ N(0.5, 0.5) in [0, 3]; α N(1.0, 0.5) in [0.3, 2]; κ N(0.5, 0.5) in [0.3, 3]; α_c N(1.5, 1.0) in [0, 2]; α_s N(0.2, 1.0) in [0, 2] | same | arXiv:2306.06314, Table 2 |
| HSC-Y1 × SDSS | ω_b BBN Gaussian; n_s Planck mean with 3 × its σ; Ω_de, ω_c flat over the emulator range (~±30σ, ±15σ of Planck); α_mag Gaussian width 0.5 | 25 parameters in all | arXiv:2111.02419, Sect. IV.2 |
| SDSS CLF | uniform on Ω_m, σ8 and all CLF parameters; WMAP7 covariance on Ω_b h², n_s, h; Gaussian nuisances | — | arXiv:1207.0503, Sect. 4 |
| DESI One-Percent BGS | uniform: log M_min [9, 16], σ_log M [10⁻⁵, 5], log M_1 [10, 16], Q_0 [0, 1], α [10⁻⁵, 5], A_cen, A_sat [−1, 1] | wide; only the upper A_cen bound matters | arXiv:2309.08675, Sect. II.2.2 |
| DES Y3 redMaGiC | HOD priors from earlier red-galaxy work; flat [0, 0.2] satellite prior in the highest-z bin | Gaussian Δz, m priors | arXiv:2106.08438, Sect. 6 |

What the prior does: on DESI LRGs at 0.6 < z < 0.8, Gaussian priors tighten
mainly the satellite parameters (log M_1, α, κ), "help to eliminate isolated
regions in the contour", hardly touch f_ic, and leave the 2σ HOD band nearly
unchanged; the flat-prior best fit shows a step at the low-mass end [src:
arXiv:2306.06314, App. B]. In SDSS w_p fits, log M_0 is "often very poorly
constrained" and its prior can move inferred parameters [src:
arXiv:1606.07817, Sect. 2.3].

### w_p or redshift-space clustering
<!-- key: wp-or-redshift-space-clustering -->

On CMASS the w_p-only posterior is degenerate: log M_cut correlates with
log M_1 (positively) and α (negatively), which fixes the satellite fraction,
and with σ, which fixes the mean central bias; the authors suggest mean
bias and f_sat as a more orthogonal basis [src: arXiv:2110.11412, Sect.
5.2]. The best w_p fit has χ² = 11 for 10 d.o.f. but σ = 2.7 × 10⁻³ at the
maximum likelihood against a posterior median 0.26, so the maximum-
likelihood point may be "a relative outlier" [src: Sect. 5.2, Table 1].
ξ(r_p, π) "gives much tighter constraints on parameters and breaks multiple
parameter degeneracies" [src: Fig. 5 caption]. On DESI BGS, adding CiC
to n_gal and w_p "drastically" tightens the HOD; without CiC the fit
yields "very little information about assembly bias" [src:
arXiv:2309.08675, abstract, Fig. 6 caption]. Aemulus V fits ξ_0, ξ_2 and
w_p down to 0.1 h⁻¹Mpc and finds fσ8 = 0.413 ± 0.031, 0.470 ± 0.026,
0.396 ± 0.022 at z = 0.25, 0.4, 0.55, lower than Planck ΛCDM by 1.9σ,
0.3σ, 3.4σ; the authors "cannot rule out an unknown systematic error in
the galaxy bias model at non-linear scales" [src: arXiv:2203.08999,
abstract].

### Direct population or surrogate
<!-- key: direct-population-or-surrogate -->

On the same ELG data, statistics and data covariance, the GP pipeline
(strict conformity, satellite velocity scaling f_σv) and AbacusHOD
(conformity through M_1,EE, central and satellite velocity bias α_c, α_s,
satellites on particles) give "quite similar" best-fit clustering and
goodness of fit; parameters treated alike agree except γ, the asymmetry of
the central HOD, which the data hardly constrain [src: arXiv:2306.06319,
Sect. 7.3]. AbacusHOD best fits there come from global optimisation with
Gaussian priors and carry no error bars [src: same]. The GP route was chosen
to obtain both "an accurate minimisation of the χ²" and "reliable error
contours" at 20 mocks per point [src: Sect. 5.1]. An emulator over
cosmology adds the emulator error: Aemulus III reaches 0.9% for w_p over 1–10
h⁻¹Mpc on 700 test models, and its training set needed 2000 HOD designs
because 400 did not sample the 15-dimensional space [src: arXiv:1804.05867,
Sect. III, abstract].

### Analytic model or simulation
<!-- key: analytic-model-or-simulation -->

The analytic halo model with exclusion and scale-dependent bias is accurate
to ~10% on w_p (SDSS DR7) [src: arXiv:1005.2413, Sect. II.3]; the CLF
analysis puts no model error into the likelihood on that basis [src:
arXiv:1207.0503, Sect. 4]. KiDS-1000 adds non-linear halo bias, exclusion,
scale-dependent galaxy bias and baryon feedback to the halo model and gets
S8 = 0.773 (+0.028/−0.030), comparable to 3×2pt analyses with cosmic shear
[src: arXiv:2210.03110, abstract]. Simulation-based population inherits the
simulation cosmology and snapshot; the ELG fits in two alternative
AbacusSummit cosmologies (high N_eff, low σ8) fit equally well, shift log₁₀M_c
and f_σv by 1–2σ, and move the mean halo mass by at most 2.7σ (0.08 dex),
with consistent satellite and one-halo fractions [src: arXiv:2306.06319,
Sect. 9, Table 8].

### Central position and satellite tracers
<!-- key: central-position-and-satellite-tracers -->

DESI and AbacusHOD put centrals at the centre of mass of the largest
(L2) subhalo and satellites on halo particles with equal weights; at most one
central per halo and one satellite per particle across tracers; no
conformity by default [src: arXiv:2110.11412, Sect. 2.1; arXiv:2306.06314,
Sect. 4.1]. The ELG GP pipeline instead draws satellites from an NFW
profile with r_25 as r_s proxy, truncated at r_98 as r_vir proxy, chosen
because it reproduces the clustering of particle-based placement [src:
arXiv:2306.06319, Sect. 5.1, App. A]. The BGS fit draws satellites from
the host NFW profile, centrals at the centre, Bernoulli and Poisson counts
[src: arXiv:2309.08675, Sect. II.2.2]; DES Y3 frees a = c_sat/c_dm and
models tidal stripping of satellite haloes for γ_t [src: arXiv:2106.08438,
Sect. 6 and the Sect. 3.3 heading]; KiDS-1000 frees the satellite Poisson parameter and prefers
sub-Poisson variance, reduced χ² better by 0.18 [src: arXiv:2210.03110,
abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Baseline parameter count | 8 (5 vanilla + f_ic + α_vel,c + α_vel,s) | DESI One-Percent LRG/QSO | arXiv:2306.06314 | Sect. 4.1 |
| CLF parameter count | 9 | SDSS | arXiv:1207.0503 | Eq. 10 |
| Cost per call | 0.17 s population + 0.18 s ξ(r_p, π); < 0.4 s total, 32 cores | AbacusHOD, CMASS density | arXiv:2110.11412 | Sect. 4.4 |
| Downsampling | halos 3.99 × 10⁸ → 6.18 × 10⁶; particles 3.15 × 10⁸ → 1.77 × 10⁷ | AbacusSummit base box | arXiv:2110.11412 | Sect. 4.4 |
| Density uncertainty | 5% (Gaussian) | SDSS DR7 | arXiv:1005.2413 | Eq. 8 |
| Density uncertainty | σ_n = 0.1 n_data (one-sided) | DESI One-Percent | arXiv:2306.06314 | Eq. 11 |
| Density uncertainty | σ_n = 4 × 10⁻⁵ at n = 3 × 10⁻⁴ h³Mpc⁻³ (one-sided) | AbacusHOD CMASS | arXiv:2110.11412 | Sect. 5.2 |
| Jackknife regions | 144 (~55 deg² each) | SDSS DR7 | arXiv:1005.2413 | Sect. II.2 |
| Jackknife regions | 128 | DESI One-Percent | arXiv:2306.06314 | Sect. 2.2 |
| Mocks for correlation matrix | 1800 boxes of 500 h⁻¹Mpc | DESI One-Percent | arXiv:2306.06314 | Sect. 5 |
| Model covariance | 1000 realisations; 48 sub-cubes of 1 h⁻¹Gpc; 20 mocks per point | DESI ELG | arXiv:2306.06319 | Sect. 5.1–5.2 |
| GP training | 800 Hammersley points + 800 iterations; KL < 0.1 over 20 iterations | DESI ELG | arXiv:2306.06319 | Sect. 5.1 |
| dynesty settings | 500 live points, d log 𝒵 > 0.01 | AbacusHOD | arXiv:2110.11412 | Sect. 5.2 |
| Emulator accuracy | 0.9% (w_p, 1–10 h⁻¹Mpc); training 2000 HOD designs | Aemulus III | arXiv:1804.05867 | Sect. III |
| Cosmology swap | log ⟨M_h⟩ shift ≤ 0.08 dex (2.7σ) | DESI ELG | arXiv:2306.06319 | Sect. 9 |
| Sampler reproducibility | < ~2% of σ across four seeds | HSC-Y1 × SDSS | arXiv:2111.02419 | App. D |
| Jackknife regions | 150 (k-means), N_θ/N_JK = 0.2 | DES Y3 γ_t | arXiv:2106.08438 | Sect. 5.2 |
| Jackknife regions | 20, pseudo-inverse | DESI One-Percent BGS | arXiv:2309.08675 | Sect. II.3.1 |
| Chain | 20 walkers × 3000 iterations; autocorrelation 100–300 | DESI One-Percent BGS | arXiv:2309.08675 | Sect. IV |
| Central assembly bias | positive at 99.9% (M_r < −20.0) and 99.5% (< −20.5), z ~ 0.15 | DESI One-Percent BGS, with CiC | arXiv:2309.08675 | abstract |
| Typical halo mass | log M_h ≈ 13.7 (redMaGiC), 13.3–13.5 (MagLim), ~15% precision; f_sat 0.1–0.2 and 0.1–0.3 | DES Y3 γ_t | arXiv:2106.08438 | abstract |
| S8 from SMF + ΔΣ + w_p | 0.773 (+0.028/−0.030) | KiDS-1000 CSMF halo model | arXiv:2210.03110 | abstract |
| fσ8 from ξ_0, ξ_2, w_p (0.1–60 h⁻¹Mpc) | 0.413 ± 0.031, 0.470 ± 0.026, 0.396 ± 0.022 (z = 0.25, 0.4, 0.55) | Aemulus V, BOSS | arXiv:2203.08999 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **M_1, M_min, M_cut compared across forms.** The satellite normalisation
  M_1′ of the SDSS form is not the mass with one satellite [src:
  arXiv:1005.2413, Sect. II.3]; M_cut and M_min play the same role in
  different notations. Test: compare derived quantities (mean halo mass,
  f_sat, bias, one-halo fraction), which the ELG paper shows are stable
  where individual parameters are not (see L2, `results.md#satellites`).
- **Maximum-likelihood point quoted as the result.** On w_p alone the best
  fit can sit in a corner (σ ≈ 0 for CMASS) [src: arXiv:2110.11412, Sect.
  5.2]. Test: report posterior medians and the derived f_sat and bias.
- **Prior-driven satellite parameters.** Test: rerun with flat priors as in
  arXiv:2306.06314, App. B, and compare HOD bands, not parameters.
- **Noisy realisations biasing the fit.** One stochastic population per call
  adds noise to χ²; remedies are tabulated mean predictions
  (arXiv:2306.06314, App. A) or averaging 20 mocks and a model covariance
  (arXiv:2306.06319, Sect. 5.1–5.2).
- **Singular jackknife covariance for ξ(r_p, π).** Small footprints give
  noisy matrices [src: arXiv:2306.06314, Sect. 5]. Test: compare mock and
  jackknife correlation matrices (ELG paper, Fig. 5), and apply Hartlap to
  each part.
- **Fixed snapshot and cosmology.** The occupation is tied to the
  simulation cosmology and snapshot redshift (L2,
  `results.md#occupation-of-haloes-by-tracer` for the DESI snapshot bias).
  Test: refit in a second cosmology [src: arXiv:2306.06319, Sect. 9].
- **Number density treated as exact.** A Gaussian density term with a small
  σ forces the satellite and central amplitudes; one-sided terms allow
  incompleteness. Test: rerun with the alternative treatment and report
  f_ic.
- **Too few jackknife regions for a long data vector.** The BGS fit has
  20 jackknife regions for n_gal, w_p in 12 bins and counts-in-cylinders in
  28 bins [src: arXiv:2309.08675, Sect. II.3.1]; a covariance is singular
  when the statistics are at least as many as the realisations, and the fit
  uses a pseudo-inverse and unit-diagonal rescaling [src: arXiv:2309.08675,
  Sect. IV];
  DES Y3 keeps N_θ/N_JK = 0.2 and applies Hartlap [src: arXiv:2106.08438,
  Sect. 5.2]. Test: report the ratio of data points to regions.
- **Velocity-bias sign.** α_vel,c is defined non-negative because ± are
  degenerate [src: arXiv:2306.06314, Sect. 4.1]; a posterior piled at 0 is
  a boundary effect, not a measurement of zero.

## Reading list
<!-- key: reading-list -->

- Method, analytic: Zehavi et al. 2011, arXiv:1005.2413 — five-parameter
  HOD, exclusion scheme, jackknife covariance, density term, chain.
- Method, CLF: Cacciato et al. 2013, arXiv:1207.0503 — CLF forms, joint
  LF + w_p + ΔΣ likelihood with cosmological priors.
- Method, simulation-based: Yuan et al. 2021 (AbacusHOD), arXiv:2110.11412
  — population algorithm, timing, one-sided density term, dynesty set-up,
  w_p degeneracies.
- Application: Yuan et al. 2024, arXiv:2306.06314 — DESI LRG/QSO
  statistic and binning, covariance construction, priors, tabulation.
- Application: Rocher et al. 2023, arXiv:2306.06319 — GP surrogate, model
  covariance, density normalisation, cross-check against AbacusHOD,
  cosmology swap.
- Method, emulator: Zhai et al. 2018, arXiv:1804.05867 — HOD + cosmology
  emulator design and accuracy.
- Application, emulator at equation level: Miyatake et al. 2022,
  arXiv:2111.02419 — Dark Emulator HOD, priors, MultiNest convergence.
- Application, BGS: Pearl et al. 2024, arXiv:2309.08675 — DESI One-Percent
  BGS HOD with counts-in-cylinders, galtab, pseudo-inverse covariance.
- Application, lensing: Zacharegkas et al. 2022, arXiv:2106.08438 — DES Y3
  HOD from small-scale γ_t, jackknife + Hartlap, MultiNest.
- Application, CSMF: Dvornik et al. 2023, arXiv:2210.03110 — KiDS-1000
  CSMF halo model with SMF, ΔΣ, w_p; sampler; sub-Poisson satellites.
- Application, emulator: Zhai et al. 2023, arXiv:2203.08999 — Aemulus V on
  BOSS ξ_0, ξ_2, w_p.
- Code: Hearin et al. 2017, arXiv:1606.04106 — Halotools.
- Critique: Hadzhiyska et al. 2020, arXiv:1911.02610 — the mass-only HOD
  misses ~15% of the real-space clustering at 1–20 h⁻¹Mpc in TNG300
  (abstract) (see `deep/assembly-bias.md`).

## Not verified
<!-- key: not-verified -->

- Zheng et al. 2007 (origin of the M_cut form), Zheng & Guo 2016 and
  Neistein et al. 2011 (tabulation), Zhang et al. 2022 (tabulation for
  AbacusSummit) and Norberg et al. (jackknife tests) are cited in the papers
  read; not read, no identifiers recorded.
- Aemulus V (arXiv:2203.08999): only the abstract was usable; its HOD
  parameters, covariance and emulator error were not located in the
  rendering. Halotools: abstract only.
- Searched for a DESI DR1 BGS HOD fit beyond arXiv:2512.15962 and
  arXiv:2309.08675: none found by title or abstract.
- The header row of Table 2 of arXiv:2306.06314 was not rendered; the
  assignment of the columns to LRG and QSO prior and bounds is inferred
  from its caption and layout.
