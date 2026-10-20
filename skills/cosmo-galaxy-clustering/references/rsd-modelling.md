# Galaxy clustering — redshift-space-distortion modelling as used in analyses

Scope: how the RSD model of spectroscopic clustering analyses evolved, from
the linear Kaiser limit with a dispersion term to the perturbative templates
of BOSS and eBOSS and the EFT models of DESI and Euclid; which model each
collaboration used, on which scales, and what its mock challenges found.
Equations, kernels and the theory behind each model are in
`cosmo-theory-foundations` (`references/physics-and-methods.md`, Sects. 8–10,
and `deep/eft-perturbation-theory.md`); the DESI full-shape pipeline is in
`deep/full-shape-modelling.md`. Snapshot: 2026-10-20.

Flags: `[src]` read this session in the cited paper (abstract); `[src: …]`
read in the body at the place given; `[sec]` taken from a named secondary
source; `[der]` derived here.

## 1. What the RSD measurement is
<!-- key: what-the-rsd-measurement-is -->

- In linear theory the redshift-space galaxy power spectrum is
  P_g(k, μ) = [b_g(z) + μ² f(z)]² P(k), and the strength of the anisotropy is
  β = f/b_g (Kaiser 1987, doi:10.1093/mnras/227.1.1) [src: arXiv:1201.2434,
  Sect. 7.2, quoting its Eq. 44]. The full redshift-space spectrum constrains
  the combination f(z)σ8(z) [src: arXiv:1201.2434, Sect. 7.2].
- That fσ8 is the combination to quote because it tests dark-energy models
  "even without the knowledge of bias or σ8" is the argument of Song &
  Percival 2009, arXiv:0807.0810 [src].
- RSD "directly measure the rate at which structure is growing at the
  redshift of observation", whereas lensing and clusters constrain the
  amplitude at several redshifts [src: arXiv:1201.2434, Sect. 7.2].
- Huterer's growth review treats RSD under cosmic velocities, not under
  galaxy clustering: the Kaiser squashing on large scales and the fingers of
  God on small scales, with the improved form
  P^(s) = [b² P_δδ + 2 b f μ² P_δv + f² μ⁴ P_vv] F(k² σ_v² μ²) attributed to
  de la Torre & Guzzo 2012 [src: arXiv:2212.05003, Sect. 3.5, Fig. 4 and
  footnote 5].
- The EFT review derives the Kaiser formula as the linear expansion of the
  exact mapping from real to redshift space; the higher powers of the velocity
  generate contact operators "that have uncontrolled UV sensitivity", removed
  by coarse-graining, which produces new effective operators [src:
  arXiv:2212.08488, Sect. 7, Eqs. 124–127].

## 2. Why the linear model fails, and the dispersion model
<!-- key: why-the-linear-model-fails-and-the-dispersion -->

Weinberg et al. 2013 (arXiv:1201.2434), Sect. 7.2 [src: Sect. 7.2]:

- The linear formula "is an inadequate approximation even on scales of
  50 h⁻¹ Mpc or more", because of non-linear effects including the fingers of
  God, opposite in sign to the linear distortion.
- The common fix, an incoherent small-scale velocity dispersion added to the
  linear distortion, is "physically incomplete" and "typically leaves 5-10 %
  systematic errors in β estimates" (the review cites Hatton & Cole 1998 for
  this [sec]).
- Higher-order perturbation theory refines large scales but does not capture
  the small-scale dispersion, which differs between galaxies and dark matter;
  halo-occupation-based modelling and the analytic streaming scheme of Reid &
  White 2011 (arXiv:1105.4165) are the two routes it names.
- The theoretical systematic is usually expressed as a k_max; most forecasts
  assume perfect modelling up to k_max and no information beyond.
- An orientation-dependent selection combined with tidal alignments "exactly
  mimics RSD, even in the linear regime", but appears negligible for present
  surveys; it is predicted to be larger for Lyα emitters [src: Sect. 7.2].

The pairwise-dispersion conventions (Gaussian or Lorentzian damping, the
factor √2 between single-galaxy and pairwise dispersion) are in
`cosmo-theory-foundations`, `references/physics-and-methods.md`, Sect. 8.2.

## 3. The first growth measurements
<!-- key: the-first-growth-measurements -->

| Survey | z_eff | Result | Model | Citation | Flag |
|---|---|---|---|---|---|
| VVDS | 0.8 | β = 0.70 ± 0.26, f = 0.91 ± 0.36; > 10,000 galaxies | anisotropic ξ | Guzzo et al. 2008, arXiv:0802.1944 | [src] |
| 6dFGS | 0.067 | fσ8 = 0.423 ± 0.055; 81,971 galaxies over 17,000 deg²; insensitive to the non-linear RSD model | ξ(r_p, π) | Beutler et al. 2012, arXiv:1204.4725 | [src] |
| BOSS DR9 CMASS | 0.57 | fσ8 = 0.43 ± 0.069; 0.415 ± 0.034 assuming a ΛCDM expansion history; 264,283 galaxies | ξ_0, ξ_2 with BAO and AP | Reid et al. 2012, arXiv:1203.6641 | [src] |
| WiggleZ | 0.44, 0.6, 0.73 | D_A = 1205 ± 114, 1380 ± 95, 1534 ± 107 Mpc; H = 82.6 ± 7.8, 87.9 ± 6.1, 97.3 ± 7.0 km/s/Mpc (BAO + AP, joint) | — | Blake et al. 2012, arXiv:1204.3674 | [src] |
| GAMA | 0.18, 0.38 | fσ8 = 0.36 ± 0.09, 0.44 ± 0.06; first multi-tracer RSD analysis, 10–20% gain over one tracer | P(k) multi-tracer | Blake et al. 2013, arXiv:1309.5556 | [src] |
| SDSS DR7 MGS | 0.15 | fσ8 = 0.49 (+0.15, −0.14) without AP; 63,163 galaxies | ξ_0, ξ_2 | Howlett et al. 2015, arXiv:1409.3238 | [src] |
| FastSound | ≈ 1.4 | fσ8 = 0.482 ± 0.116 (σ_v = 0), 0.494 (+0.126, −0.120) with σ_v free; 2783 emission-line galaxies, 4.2σ RSD detection | ξ above 8 h⁻¹ Mpc | Okumura et al. 2016, arXiv:1511.08083 | [src] |
| VIPERS PDR-2 | 0.6, 0.86 | fσ8 = 0.55 ± 0.12, 0.40 ± 0.11; negligible bias down to 5 h⁻¹ Mpc on mocks | ξ_0, ξ_2 with P_θθ, P_δθ fits | Pezzotta et al. 2017, arXiv:1612.05645 | [src] |

The same set (6dFGS, GAMA, WiggleZ, VIPERS, MGS, FastSound, BOSS+eBOSS) is
the RSD part of the fσ8 compilation of Huterer 2023 [src: arXiv:2212.05003,
Sect. 3.7, Fig. 5]. The Weinberg et al. review lists the earlier generation
(VVDS, SDSS DR7, WiggleZ, BOSS DR9, 6dFGS) and notes that all assume a ΛCDM
geometry when inferring fσ8 [src: arXiv:1201.2434, Sect. 7.2]. The WiggleZ
fσ8 values of Blake et al. 2011 were not read. Low-redshift fσ8 from peculiar
velocities is in `cosmo-peculiar-velocities`.

## 4. Perturbative templates of the BOSS era
<!-- key: perturbative-templates-of-the-boss-era -->

### 4.1 TNS
<!-- key: tns -->

Taruya, Nishimichi & Saito 2010 (arXiv:1006.0699) add to the non-linear
Kaiser terms two corrections C_A, C_B from the density–velocity coupling,
times a phenomenological damping. As written by the eBOSS LRG analysis
[src: arXiv:2007.08993, Sect. 3.2.2, Eqs. 19–22]:

- P^s_g(k, μ) = D(kμσ_v)[P_gg + 2μ² f P_gθ + μ⁴ f² P_θθ + C_A(k, μ, f, b_1)
  + C_B(k, μ, f, b_1)], with a Lorentzian D = (1 + k²μ²σ_v²)⁻¹ chosen
  because it fits the LRG data and mocks better; σ_v is "an effective pairwise
  velocity dispersion" treated as a nuisance parameter.
- Bias: the renormalised one-loop scheme with δ_g = b_1 δ + (b_2/2)δ² +
  b_G2 G_2 + b_Γ3 Γ_3 (Eq. 22).

de la Torre & Guzzo 2012 (arXiv:1202.5559) compared the models on
HOD-populated N-body catalogues at z = 0.1 and 1: TNS gave "the most
unbiased estimates", with systematic errors within 4% on f for L > L* to
L > 3L* galaxies, and scale-dependent bias matters most for the most luminous
galaxies [src]. Which BOSS DR12 and eBOSS analyses used it: Sects. 5–6.

### 4.2 Lagrangian models: CLPT and Gaussian streaming
<!-- key: lagrangian-models-clpt-and-gaussian-streaming -->

Convolution Lagrangian perturbation theory (Carlson, Reid & White 2013,
arXiv:1209.0780) is a partial resummation of Matsubara's Lagrangian
perturbation theory that recovers the Zel'dovich approximation at lowest
order; it matches N-body real-space and redshift-space monopoles well, "worse
for higher multipole moments", and explains the strong bias dependence of the
redshift-space multipoles [src]. Combined with the Gaussian streaming model
(Reid & White 2011, arXiv:1105.4165; the streaming equation and its validity
are in `cosmo-theory-foundations`, `references/physics-and-methods.md`,
Sect. 8.4), it is the configuration-space model "CLPT-GS" (or "CLPT-GSRSD")
of BOSS DR12 and eBOSS [src: arXiv:1607.03155, Sect. 6; arXiv:1607.03148].

### 4.3 gRPT and clustering wedges
<!-- key: grpt-and-clustering-wedges -->

The configuration-space and Fourier-space wedge analyses of BOSS DR12 used
one model of non-linearity, bias and RSD, gRPT ("Blas et al. in prep." in
the consensus paper), tested on the Minerva N-body simulations; "these two
complementary analyses represent the first time that the same model is
applied in configuration and Fourier space fits" [src: arXiv:1607.03155,
Sect. 6; Sánchez et al. 2017, arXiv:1607.03147; Grieb et al. 2017,
arXiv:1607.03143].

### 4.4 RegPT and RESPRESSO
<!-- key: regpt-and-respresso -->

The eBOSS quasar analysis used RegPT in Fourier space and RESPRESSO in
configuration space; CLPT was tested in the quasar mock challenge but not
used in the final quasar fits, and "the three models work equally well"
[src: arXiv:2007.09003, Sect. 3.4.1]. The Fourier analysis describes its
model as "based on Regularised Perturbation Theory, which includes Redshift
Space Distortions and the Alcock-Paczynski effect" [src] (Neveux et al.
2020, arXiv:2007.08999).

## 5. BOSS DR12: four methods and a consensus
<!-- key: boss-dr12-four-methods-and-a-consensus -->

Alam et al. 2017 (arXiv:1607.03155) combined four full-shape analyses of the
pre-reconstruction clustering [src: Sect. 6, Table 4]:

| Analysis | Statistic | Model | Scales | Covariance |
|---|---|---|---|---|
| Satpathy et al. 2017, arXiv:1607.03148 | ξ_0, ξ_2 | CLPT + Gaussian streaming | 25–150 h⁻¹ Mpc, 5 h⁻¹ Mpc bins | 997 MD-Patchy mocks |
| Beutler et al. 2017, arXiv:1607.03150 | P_0, P_2, P_4 (FFT estimator) | "based on renormalized perturbation theory (Taruya et al., 2010)", window included | k_max = 0.15 h Mpc⁻¹ (ℓ = 0, 2), 0.10 (ℓ = 4), Δk = 0.01 | 2048 MD-Patchy mocks (2045 NGC) |
| Grieb et al. 2017, arXiv:1607.03143 | three P(k) wedges (ℓ ≤ 4) | gRPT | k < 0.2 h Mpc⁻¹, Δk = 0.005 | 2045 MD-Patchy mocks |
| Sánchez et al. 2017, arXiv:1607.03147 | three ξ wedges | gRPT | 20–160 h⁻¹ Mpc, 5 h⁻¹ Mpc bins | 2045 MD-Patchy mocks |

- fσ8 per method [src: arXiv:1607.03155, Table 4], at z_eff = 0.38, 0.51,
  0.61: Satpathy 0.430 ± 0.054, 0.452 ± 0.058, 0.456 ± 0.052; Beutler
  0.479 ± 0.054, 0.454 ± 0.051, 0.409 ± 0.044; Grieb 0.498 ± 0.045,
  0.448 ± 0.038, 0.409 ± 0.041; Sánchez 0.468 ± 0.053, 0.470 ± 0.042,
  0.440 ± 0.039. The Satpathy abstract gives 0.452 ± 0.057 and 0.457 ±
  0.052 for the last two bins [src: arXiv:1607.03148]; use the table.
- "In all cases the μ-wedges analyses give significantly tighter constraints
  than the multipole analyses, in both configuration space and Fourier
  space" [src: arXiv:1607.03155, Sect. 6].
- The pairwise differences between methods on the data are typical of those
  on the 84 high-resolution cut-sky mocks [src: Sect. 7.2, Fig. 10].
- Beutler et al. find the fσ8 at z_eff = 0.61 about 1.4σ below Planck ΛCDM
  [src: arXiv:1607.03150].
- Consensus: the posteriors are combined as correlated Gaussians with
  cross-correlations measured on MD-Patchy mocks (Sánchez et al. 2017,
  arXiv:1607.03146) [src: arXiv:1607.03155, Sects. 8.1–8.2]; the consensus
  improves on the best single method by about 15% on D_M, 20% on H and 10% on
  fσ8 [src: Sect. 8.2]. The final values are in `boss-eboss-euclid.md`.

## 6. eBOSS DR16: two models per tracer
<!-- key: eboss-dr16-two-models-per-tracer -->

| Tracer | Configuration space | Fourier space | Mock challenge |
|---|---|---|---|
| LRG (0.6–1.0) | CLPT-GS and TNS on ξ_0, ξ_2, ξ_4 (Bautista et al. 2020, arXiv:2007.08993) | P_0, P_2, P_4, model not read here (Gil-Marín et al. 2020, arXiv:2007.08994) | Rossi et al. 2020, arXiv:2007.09002 |
| ELG (0.6–1.1) | CLPT-GS with a modified estimator that cancels angular modes (Tamone et al. 2020, arXiv:2007.09009) | P_0, P_2, P_4 with integral constraints (de Mattia et al. 2020, arXiv:2007.09008) | Alam et al. 2020, arXiv:2007.09004; HOD study Avila et al. 2020, arXiv:2007.09012 |
| QSO (0.8–2.2) | RESPRESSO (Hou et al. 2020, arXiv:2007.08998) | RegPT (Neveux et al. 2020, arXiv:2007.08999) | Smith et al. 2020, arXiv:2007.09003 |

Model attributions: LRG from arXiv:2007.08993, Sects. 3.2.1–3.2.2; QSO from
arXiv:2007.09003, Sect. 3.4.1; ELG from the abstracts of arXiv:2007.09009
and arXiv:2007.09004 (the ELG challenge analysed "the TNS RSD model in
Fourier space and the CLPT in configuration space") [src].

Mock-challenge results [src, abstracts unless a place is given]:

- LRG (OuterRim-based HOD mocks): all three models recover α_∥ and α_⊥
  within 0.9% and fσ8 within 1.5% (arXiv:2007.09002).
- ELG: conservative theoretical systematics of 3.3% on fσ8, 1.8% on α_∥,
  1.5% on α_⊥, "an order of magnitude smaller than the statistical error"
  of the sample (arXiv:2007.09004).
- QSO: non-blind mocks recover fσ8 within 3% and the α within 1%; the
  systematic error of the consensus is σ(fσ8) = 0.011, σ(α_∥) = 0.008,
  σ(α_⊥) = 0.005 (arXiv:2007.09003).
- ELG HOD variations (satellite fraction, profiles, velocity bias, infall):
  w_p carries most of the PDF and profile effects, ξ_2 most of the velocity
  effects; the companion analyses are "insensitive to the details of galaxy
  physics considered here" (arXiv:2007.09012).

**The σ8 normalisation scale.** SDSS RSD fits shift a template by α_⊥, α_∥
and normalise it by bσ8 and fσ8; whether the template is rescaled before the
normalisation is fixed changes the cosmology dependence. Rescaling first
"significantly reduces the dependence on fiducial cosmology" for BOSS and
eBOSS galaxies; MGS and eBOSS quasars used the simpler unrescaled procedure
with a slightly larger systematic [src: arXiv:2007.08991, App. A, Fig. 15].
The DESI fσ_s8 convention that grew out of this is in
`physics-and-methods.md`, Sect. 3. The appendix ends: "it may be best to
directly fit models to the two-point multipoles without an intermediate data
compression step" for DESI and Euclid [src: App. A].

## 7. Modelling budgets in numbers
<!-- key: modelling-budgets-in-numbers -->

| Analysis | Modelling / theory term | Total RSD systematic | Place read |
|---|---|---|---|
| BOSS DR12 consensus | high-resolution mocks: bias 0.0037 (standard error of 84 mocks), HOD spread 0.008 → 0.009 rms | σ_sys(fσ8) = 0.024, 0.015, 0.009 at z_eff = 0.38, 0.51, 0.61 (maximum of MD-Patchy bias and high-resolution estimate) | arXiv:1607.03155, Sects. 7.2, 7.4 |
| BOSS DR12, MD-Patchy | consensus fσ8 bias −0.024, −0.016, −0.003 (up to 0.6σ of the mock scatter) | — | arXiv:1607.03155, Table 6 |
| eBOSS LRG, ξ | modelling 0.010 (CLPT-GS), 0.009 (TNS) on fσ8 | 0.024 (CLPT-GS), 0.023 (TNS), 0.024 (P_ℓ) on fσ8; 54–58% of σ_stat | arXiv:2007.08993, Table 10 |
| eBOSS QSO | modelling from the blind N-body challenge | systematics "amount to 1/3 of the statistical error" | arXiv:2007.08999, abstract |
| eBOSS ELG | 3.3% on fσ8 | negligible against σ_stat | arXiv:2007.09004, abstract |

The eBOSS LRG budget splits into modelling, fiducial cosmology (0.014 and
0.012 on fσ8) and observational effects (0.017 and 0.018), summed in
quadrature as independent [src: arXiv:2007.08993, Sect. 4.2.5, Table 10]. In
that analysis the systematic is not negligible: "more than 50 per cent of
the statistical errors for all parameters" [src].

For the DESI DR1 EFT budget (theory and HOD terms in units of σ_DR1) see
`systematics.md`, Sects. 0–2; for the BOSS EFT reanalyses and the prior
debate see `physics-and-methods.md`, Sect. 3, and `open-questions.md`, Sect. 3.

## 8. From templates to EFT
<!-- key: from-templates-to-eft -->

- The first EFT analyses of the BOSS DR12 data (Ivanov et al. 2020,
  arXiv:1909.05277; D'Amico et al. 2020, arXiv:1909.05271) fit the
  cosmological parameters directly instead of compressing to fσ8; the model
  ingredients are in `cosmo-theory-foundations`, Sect. 9, and the DESI
  pipeline in `deep/full-shape-modelling.md`.
- In the EFT the fingers of God become counterterms: the quadrupole
  counterterm is "dominated by fingers of God" and its link to σ_v is given
  in `cosmo-theory-foundations`, `references/physics-and-methods.md`,
  Sect. 9.
- On dark matter the one- and two-loop IR-resummed EFT fit the Horizon Run
  z = 0 matter spectrum to k ≈ 0.12 and 0.27 h Mpc⁻¹, where linear theory
  fails at k ≈ 0.03 h Mpc⁻¹ [src: arXiv:2212.08488, Sect. 6, Fig. 11].
- Euclid's forecast recipe of 2020 was still phenomenological: a Lorentzian
  FoG factor in fσ_p, a de-wiggled spectrum with the BAO damping g_μ =
  σ_v²[1 − μ² + μ²(1 + f)²] of Eisenstein et al. 2007, both σ_p and σ_v
  scaled with D(z), and a free shot-noise term standing in for the broadband
  non-linearity; the authors call it "at least practical, all models being in
  any case only an approximation" [src: arXiv:1910.09273, Sect. 3.2.2,
  Eqs. 81–87]. The Euclid likelihood code CLOE replaces it with an
  EFTofLSS-based model for the spectroscopic multipoles [src:
  arXiv:2510.09118, Sect. 4.1]; detail in `boss-eboss-euclid.md`, Sect. 6.

## 9. What to check in an RSD claim
<!-- key: what-to-check-in-an-rsd-claim -->

- Which model, which scales (k_max or s_min) and which multipoles or wedges;
  whether the hexadecapole is used.
- Whether fσ8 is a compressed template parameter (BOSS, eBOSS: template
  rescaled by α; DESI: fσ_s8) or derived from a full-model fit.
- Whether the quoted error includes the modelling systematic, and how it was
  set (mock challenge, HOD spread, maximum of several estimates).
- For a compilation: the BOSS DR12 bins overlap (0.4 < z < 0.6 shares
  galaxies with both neighbours) and the eBOSS LRG sample contains the
  z > 0.6 BOSS CMASS tail [src: arXiv:1607.03155, Sect. 2.2,
  Table 2; arXiv:2007.08991, Sect. III.1].
- The geometry assumed: VVDS-to-BOSS DR9 fσ8 values assume ΛCDM distances
  [src: arXiv:1201.2434, Sect. 7.2].

## Not verified
<!-- key: not-verified -->

- The WiggleZ fσ8 values (Blake et al. 2011) and the 2dFGRS β (Peacock et
  al. 2001): papers not fetched.
- The arXiv identifier of the gRPT paper ("Blas et al. in prep." in
  arXiv:1607.03155) and of the BOSS DR12 high-resolution mock challenge
  ("Tinker et al. 2016"): none found.
- Wang, Reid & White 2014 (CLPT with Gaussian streaming): identifier not
  found this session.
- The exact RSD model of the eBOSS ELG Fourier-space fit (arXiv:2007.09008)
  beyond what the ELG mock challenge abstract states.
