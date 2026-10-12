# Weak lensing — physics and methods

Scope: what cosmic shear and galaxy–galaxy lensing measure, the estimators and
their defining equations, the theory models in current use, covariance,
likelihood and blinding practice, and the public codes.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here. Equations in this file are textbook
definitions (Bartelmann & Schneider 2001, arXiv:astro-ph/9912508; Kilbinger
2015, arXiv:1411.0115; Mandelbaum 2018, arXiv:1710.03235) and carry no flag.

## 1. What is measured
<!-- key: what-is-measured -->

Light from a source at comoving distance χ_s is deflected by the tidal field
of the matter along the line of sight. To first order the image distortion is
described by the convergence κ and the complex shear γ = γ1 + iγ2. For a
source population with normalised redshift distribution n_i(z), the
convergence is a weighted projection of the density contrast δ:

    κ_i(θ) = ∫ dχ q_i(χ) δ(χθ, χ),
    q_i(χ) = (3/2) Ωm (H0/c)² [χ / a(χ)] ∫_χ dχ' n_i(χ') (χ' − χ)/χ'      (flat space)

The observable in cosmic shear is the two-point function of galaxy
ellipticities between tomographic bins i and j. In the Limber approximation

    C_ℓ^{ij} = ∫ dχ q_i(χ) q_j(χ) / χ² · P_m(k = (ℓ + 1/2)/χ, z(χ)).

Because the kernel is broad and proportional to Ωm, and the power spectrum to
σ8², cosmic shear constrains mainly the combination S8 ≡ σ8 (Ωm/0.3)^0.5; the
exponent that best matches the degeneracy direction is survey-dependent:
KiDS-Legacy finds α = 0.58 and quotes Σ8 = σ8(Ωm/0.3)^0.58 alongside S8
(Wright et al. 2025, arXiv:2503.19441) [src].

The measured ellipticity is an estimate of the reduced shear g = γ/(1 − κ),
not of γ; the difference is second order and is modelled explicitly in
third-order analyses (Linke et al. 2026, arXiv:2606.12389) [src].

Galaxy–galaxy lensing measures the mean tangential shear γ_t(θ) of sources
around lens galaxies, or the excess surface density ΔΣ(R) = Σ̄(<R) − Σ(R) =
Σ_crit γ_t when lens redshifts are known. ΔΣ needs a fiducial cosmology to
convert angles and redshifts into R and Σ_crit; γ_t(θ) does not. "3×2pt" is
the joint data vector of cosmic shear, galaxy–galaxy lensing and galaxy
clustering; "6×2pt" adds CMB lensing and its two cross-correlations (DES Y3 ×
SPT/Planck: arXiv:2203.12440, arXiv:2206.10824; DES Y3 × Planck PR4:
arXiv:2510.25596).

## 2. Estimators
<!-- key: estimators -->

Each galaxy has a measured ellipticity ε = ε1 + iε2 and a weight w. Around a
direction joining two galaxies, the tangential and cross components are ε_t =
−Re(ε e^{−2iφ}) and ε_× = −Im(ε e^{−2iφ}). The correlation-function estimator
is

    ξ̂±^{ij}(θ) = Σ_ab w_a w_b [ε_t,a ε_t,b ± ε_×,a ε_×,b] / Σ_ab w_a w_b · 1/[(1 + m_i)(1 + m_j)]

for pairs ab in the angular bin, with the multiplicative calibration applied
to the ensemble, not per galaxy. For a metacalibration catalogue the factor (1
+ m) is replaced by the mean shear response ⟨R⟩ = ⟨R_γ⟩ + ⟨R_S⟩, the sum of
the shear response and the selection response, both measured from artificially
sheared images (Sheldon & Huff 2017, arXiv:1702.02601).

The theory relations are

    ξ±(θ) = (1/2π) ∫ dℓ ℓ J_{0/4}(ℓθ) [C_ℓ^{EE} ± C_ℓ^{BB}],

and the tangential shear around lenses of bin a with sources of bin i is

    γ_t^{ai}(θ) = (1/2π) ∫ dℓ ℓ J_2(ℓθ) C_ℓ^{g_a κ_i},   γ̂_t = Σ w_l w_s ε_t / Σ w_l w_s − (same around random points).

A lensing-only signal has C^{BB} = 0 to first order, so B modes are a null
test. In NLA the intrinsic shape field is proportional to the tidal field,
giving

    P_GI(k,z) = −A_IA C1 ρ_crit Ωm / D(z) · [(1+z)/(1+z0)]^η P_m(k,z),   P_II = (same prefactor)² P_m,

with amplitude A_IA and redshift index η (Bridle & King 2007, arXiv:0705.0166;
conventions compared in Lamman et al. 2024, arXiv:2309.08605). The sign and
normalisation conventions of C1 differ between codes; check before comparing
A_IA across papers.

## 3. Two-point statistics
<!-- key: two-point-statistics -->

| Statistic | Definition | Properties | Used by | Reference |
|---|---|---|---|---|
| ξ±(θ) | ⟨γ_t γ_t⟩ ± ⟨γ_× γ_×⟩ at separation θ; Hankel transforms of C_ℓ with J0 and J4 | simple, mask-insensitive estimator; mixes E and B modes and all ℓ, ξ− reaches very small scales | DES Y1/Y3/Y6, HSC, KiDS, UNIONS | Schneider et al. 2002, arXiv:astro-ph/0206182 |
| COSEBIs E_n, B_n | integrals of ξ± over a finite [θ_min, θ_max] with weights that separate E and B exactly | clean E/B split, compact data vector, well-defined scale range | KiDS-1000 fiducial; KiDS-Legacy 2+3pt; UNIONS B-mode test | Schneider et al. 2010, arXiv:1002.2136; Asgari et al. 2020, arXiv:1910.05336 |
| Band powers | band-averaged C_ℓ obtained from ξ± with apodised filters | approximately local in ℓ | KiDS-1000 (complementary), KiDS-Legacy | Asgari et al. 2021, arXiv:2007.15633; Joachimi et al. 2021, arXiv:2007.01844 |
| Pseudo-Cℓ | harmonic transform of the masked shear field, corrected by a mode-coupling matrix | natural for theory, needs noise-bias subtraction and mask handling | HSC, UNIONS, KiDS-Legacy cross-check | Hivon et al. 2002, arXiv:astro-ph/0105302; Alonso et al. 2019, arXiv:1809.09603 |

KiDS-Legacy compares the two-point statistics on the same catalogue as part of
its consistency tests (Stölzner et al. 2025, arXiv:2503.19442) [src]. UNIONS
validates B modes with three statistics (pure-mode ξ±^B, COSEBI B_n, C_ℓ^BB)
and finds that scale cuts do not translate between them (Daley et al. 2026,
arXiv:2604.03227) [src].

A separate idea is to localise the lensing kernel: the
Bernardeau–Nishimichi–Taruya (BNT) transform builds combinations of
tomographic bins with narrow kernels so that a cut in ℓ becomes a cut in k
(first KiDS application: Gu et al. 2026, arXiv:2607.04384) [src].

## 4. Shape measurement
<!-- key: shape-measurement -->

See `systematics.md` sections 1–3. In brief: moments with PSF correction (KSB;
Kaiser, Squires & Broadhurst 1995, arXiv:astro-ph/9411005), model fitting
calibrated on image simulations (lensfit, arXiv:1210.8201; im3shape in DES SV
and Y1, arXiv:1507.05603 and arXiv:1708.01533; the HSC catalogues,
arXiv:1705.06745 and arXiv:2107.00136), and
self-calibrating estimators (metacalibration, arXiv:1702.02600 and
arXiv:1702.02601; metadetection, arXiv:1911.02505). Community blind challenges
began with STEP (Heymans et al. 2006, arXiv:astro-ph/0506112). The requirement
on PSF model accuracy is set in Paulin-Henriksson et al. 2008
(arXiv:0711.4886).

## 5. Theory model of a current analysis
<!-- key: theory-model-of-a-current-analysis -->

| Ingredient | Choices in use | References |
|---|---|---|
| Linear P(k) | CAMB or CLASS (see `cosmo-software-ecosystem`) | — |
| Non-linear P(k) | HALOFIT (Takahashi et al. 2012, arXiv:1208.2701), HMcode (arXiv:1505.07833, arXiv:2009.01858), emulators (EuclidEmulator2, arXiv:2010.11288) | — |
| Baryons | scale cuts; HMcode feedback parameter; baryonification emulators; PCA; external gas priors | `systematics.md` section 6 |
| Intrinsic alignments | NLA, TATT, halo-model or mass-dependent variants | `systematics.md` section 5 |
| Projection | Limber; corrections at low ℓ | arXiv:0809.5112, arXiv:1702.05301 |
| Galaxy bias (3×2pt) | linear bias with large-scale cuts, or non-linear bias with smaller cuts | DES Y6: R_min = 6 (4) h⁻¹Mpc for linear (non-linear) bias in γ_t (arXiv:2601.15175) [src] |
| Magnification | fixed coefficients per lens bin | arXiv:2209.09782, arXiv:2601.14833 |
| Nuisance | m_i, Δz_i or n(z) realisations, IA parameters, bias parameters, baryon parameters | arXiv:2105.13548, arXiv:2601.14859 |

An alternative theory route keeps only perturbative scales and uses the
effective field theory of large-scale structure at two loops with lensing
counterterms and a spin-2 EFT for alignments (Chen et al. 2026,
arXiv:2603.28761) [src]. A simulation-based route fits clustering and lensing
to non-linear scales with an HOD on AbacusSummit (Lange et al. 2025,
arXiv:2512.15962) [src].

## 6. Covariance and likelihood
<!-- key: covariance-and-likelihood -->

Stage-III analyses use an analytic covariance with three terms: Gaussian
(including shape noise and the survey geometry), connected non-Gaussian
(trispectrum, from the halo model), and super-sample covariance (Takada & Hu
2013, arXiv:1302.6994). Implementations: CosmoLike (Krause & Eifler 2017,
arXiv:1601.05779), the DES Y3 covariance (Friedrich et al. 2021,
arXiv:2012.08568), KiDS-1000 (arXiv:2007.01844), and OneCovariance for
KiDS-Legacy (Reischke et al. 2024, arXiv:2410.06962). When a covariance is
estimated from a finite number of mocks, the inverse must be debiased (Hartlap
et al. 2007, arXiv:astro-ph/0608064) or the likelihood replaced by the
appropriate t-distribution (Sellentin & Heavens 2016, arXiv:1511.05969); see
`cosmo-statistics-inference`.

The likelihood is Gaussian in the data vector. The covariance is evaluated at
a fiducial cosmology and usually iterated once at the best fit. The choice of
the data vector that enters the Gaussian term is not innocuous: in the
KiDS-Legacy k-cut analysis it moves S8 by about 0.08 (arXiv:2607.04384) [src].

Internal-consistency tests are part of the method: KiDS-Legacy applies three
tiers of metrics to splits by redshift, scale, colour and region
(arXiv:2503.19442) [src]; DES uses posterior-predictive distributions, in Y6
through a fast Gaussian-mixture metric Δ_PPD (Doux et al. 2026,
arXiv:2610.03447) [src].

## 7. Blinding
<!-- key: blinding -->

All Stage-III collaborations blind. KiDS blinds at the shear-catalogue level
(Kuijken et al. 2015, arXiv:1507.00738) [src]. DES developed a transformation
of the summary statistics themselves: the measured two-point functions are
shifted to values consistent with hidden shifted cosmological parameters while
internal consistency, measured by χ², is preserved (Muir et al. 2020,
arXiv:1911.05929) [src]. The KV450, DES Y3, HSC Y3, DES Y6 cosmic-shear and
HSC shear-ratio analyses all state that they were conducted blind
(arXiv:1812.06076, arXiv:2105.13543, arXiv:2304.00702, arXiv:2602.10065,
arXiv:2508.21681) [src].

## 8. Codes and pipelines
<!-- key: codes-and-pipelines -->

| Code | Purpose | Reference |
|---|---|---|
| TreeCorr | two- and three-point correlation functions | the paper usually cited is Jarvis et al. 2004, arXiv:astro-ph/0307393, whose subject is the aperture-mass skewness |
| NaMaster | pseudo-Cℓ for any pair of spin-0 or spin-2 fields, with contaminant deprojection and E/B purification | Alonso et al. 2019, arXiv:1809.09603 |
| CosmoSIS | modular parameter-estimation framework connecting CAMB, cosmic-shear modules and samplers | Zuntz et al. 2015, arXiv:1409.3409 |
| CosmoLike | likelihood and covariance for multi-probe analyses | arXiv:1601.05779 |
| CCL | theory predictions for LSST DESC | Chisari et al. 2019, arXiv:1812.05995 |
| OneCovariance | covariance of arbitrary two-point statistics | arXiv:2410.06962 |
| GalSim | image simulation | Rowe et al. 2015, arXiv:1407.7676 |
| ngmix | Bayesian shear measurement; one of the two DES SV pipelines (arXiv:1507.05603) | Sheldon 2014, arXiv:1403.7669 |
| PIFF | PSF modelling in DES Y3 and Y6; default PSF software planned for Rubin weak lensing [src: arXiv:2501.05781] | arXiv:2011.03409, arXiv:2501.05781 |
| HMcode, BCemu, BACCO | non-linear and baryonic power spectra | arXiv:2009.01858, arXiv:2108.08863, arXiv:2011.15018 |

## 9. Conventions that split the community
<!-- key: conventions-that-split-the-community -->

- **Point estimate.** Marginal mean, marginal mode, or maximum a posteriori.
  KiDS-1000 warned that marginal S8 point estimates "are easily misinterpreted
  to be biased low" and proposed an alternative estimator and credible
  interval (arXiv:2007.01844) [src]. In the DES Y3 + KiDS-1000 joint analysis
  the marginal mean is 0.790 and the MAP 0.801, a difference caused by
  skewness and projection effects (arXiv:2305.17173) [src]. State which
  estimate a number is.
- **S8 exponent.** 0.5 by convention; the best-constrained combination has a
  survey-dependent exponent (0.58 for KiDS-Legacy) [src: arXiv:2503.19441].
- **Tension metric.** One-dimensional S8 difference, full-parameter-space
  shift, or evidence-based; DES Y6 quotes two for the same data (2.6σ and
  1.8σ) (arXiv:2601.14559) [src].
- **ΔΣ or γ_t.** ΔΣ embeds a fiducial cosmology and h-dependent units (h M⊙
  pc⁻²); γ_t does not.
- **Ellipticity definition.** |ε| = (a − b)/(a + b) or |e| = (a² − b²)/(a² +
  b²); the responsivity differs by about a factor two.
- **n_eff and σ_ε.** Several definitions of effective source density exist;
  quote the one the survey paper uses.

## Not verified
<!-- key: not-verified -->

- Which Boltzmann code and non-linear prescription each of DES Y6, KiDS-Legacy
  and HSC Y3 uses in its fiducial run.
- Exact scale ranges of each survey's fiducial data vector.
