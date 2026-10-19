# Gas-mass fraction — cosmo-clusters dossier

Scope: how a gas-mass-fraction (f_gas) analysis is built (relaxed-sample
selection, the hydrostatic and gas-mass measurement, the measurement
shell, the model with its depletion, calibration and aperture terms, the
priors and where they come from, the lensing calibration of the mass
scale, blinding), how the model has changed between analyses, and how
the same equation is used the other way round to constrain the
hydrostatic bias.
Snapshot: 2026-10-18.
From: Relaxed-cluster series (arXiv:1502.06020, arXiv:1402.6212,
arXiv:2111.09343); Pierre 2022 review (arXiv:2205.05499), Sect. 1.

Already in L2, not repeated here: the cosmological results (Ω_m, h,
Ω_Λ, w) of each analysis and the 7.4% and 3% scatter figures in
`results.md#gas-mass-fraction-of-relaxed-clusters-a`; the principle
(f_gas ∝ d^1.5, a distance and Ω_b/Ω_m probe) and the lensing/X-ray
ratio of 0.96 at r2500 in `physics-and-methods.md#gas-mass-fraction`;
simulated hydrostatic bias and the Chandra–XMM calibration offset in
`systematics.md#hydrostatic-bias-and-x-ray-temperature`; the X-COP and
Planck-ESZ bias values in `results.md#hydrostatic-bias-what-simulations-and-x-ray`.
How feedback sets the baryon content of simulated haloes is in
`cosmo-simulations-mocks` (`deep/hydro-subgrid-calibration.md`).

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Select the most relaxed, hottest clusters
<!-- key: step-1-select-the-most-relaxed-hottest-clusters -->

The relaxed-cluster analyses keep clusters that pass the
Symmetry–Peakiness–Alignment (SPA) test on Chandra images and have a
temperature ≥ 5 keV in the isothermal part of the profile; the stated
reasons are to minimise departures from hydrostatic equilibrium and
spherical symmetry, and to keep systems whose dynamics at ≈ r2500 are
gravitationally rather than astrophysically dominated, with smaller
AGN-feedback uncertainty [src: Sect. 2.1, arXiv:2111.09343].

The SPA test measures three image statistics designed to be fair across
redshift and exposure: the sharpness of the surface-brightness peak (p),
the shifting of isophotes relative to each other (symmetry s), and the
offset between the large-scale and small-scale centres (alignment a);
uncertainties come from bootstrapping the photon images [src: Sects. 3.1
and 4.1, arXiv:1502.06020]. A cluster is relaxed if more than 50% of
its bootstrap (s, p, a) triplets satisfy s > 0.87, p > −0.82 and a >
1.00 simultaneously; the cuts were placed with reference to earlier
subjective selections, then applied blindly, and the aim is a pure rather
than complete sample [src: Sect. 5.4, same]. The algorithmic sample was
accepted after checking that its f_gas scatter is smaller than that of
the earlier subjective sample, a comparison made only after the sample
was frozen [src: Sect. 3.1, same].

### Step 2. Measure gas mass and hydrostatic mass
<!-- key: step-2-measure-gas-mass-and-hydrostatic-mass -->

The 2014 analysis fits each cluster with a model that is non-parametric
for the gas (concentric isothermal shells) and NFW for the total mass,
under hydrostatic equilibrium; the central region is excluded from the
fit [src: Sect. 2.3, arXiv:1402.6212]. The authors argue that such
"semi-parametric" models are the least biased choice, because
parametrised forms for both density and temperature impose "a complex and
non-intuitive prior on the mass profile" [src: same]. The same procedure
is kept in 2022, with gas mass non-parametric and total mass NFW [src:
Sect. 2.1, arXiv:2111.09343]. The hydrostatic equation itself,
M_HE(<r) = −(r k_B T/G μ m_p)(d ln ρ/d ln r + d ln T/d ln r), is written
as Eq. 4 of arXiv:2204.12823 [src: Sect. 2.1].

**Blinding.** The fit is cosmology-independent: profiles come out in
units that a cosmology-dependent factor converts to physical ones, and
the gas-density and mass profiles of each cluster were multiplied by
different random values until all fits were final, hiding each cluster's
f_gas, the agreement between clusters and any redshift trend [src:
Sect. 2.3, arXiv:1402.6212].

### Step 3. Choose the measurement shell
<!-- key: step-3-choose-the-measurement-shell -->

Differential f_gas profiles converge and have small scatter at Δ < 10⁴
(r ≳ 0.5 r2500), rising as f_gas ∝ r^0.43 for 0.5 ≤ r/r2500 ≤ 1.6; the
fractional intrinsic scatter in shells of width 0.4 r2500 is smallest,
7–8%, near r2500 and grows inwards [src: Sect. 3.1, Fig. 3,
arXiv:1402.6212]. The cosmological measurement uses the shell 0.8 <
r/r2500 < 1.2: excluding smaller radii reduces both the scatter and the
uncertainty of the simulated depletion, while temperatures cannot be
measured much beyond 1.6 r2500 for most clusters [src: same]. Simulated
depletion from two independent codes agrees to about 5% in this shell but
much less well in the full sphere including the centre [src: Sect. 4.2,
same]. The X-ray results are passed to the likelihood as M2500^ref and
f_gas^ref in the shell, as bivariate lognormals including their
"generally substantial" anti-correlation [src: Sects. 2.1 and 3,
arXiv:2111.09343].

### Step 4. Write the model
<!-- key: step-4-write-the-model -->

The 2022 model, which this dossier follows [src: Sect. 3,
arXiv:2111.09343]:

- true shell gas fraction f_gas(z, M2500) = Υ(z, M2500) Ω_b/Ω_m (Eq. 1),
  with the gas depletion Υ = Υ0 (1 + Υ1 z) (M2500/3 × 10¹⁴ M_sun)^α
  (Eq. 2) and a lognormal intrinsic scatter σ_f;
- measured value f_gas^ref = K(z) A(z)^η_f [d^ref(z)/d(z)]^{3/2}
  f_gas(z, M2500) (Eq. 3), where d is the distance, "ref" the reference
  flat ΛCDM with h = 0.7 and Ω_m = 0.3, A(z) = θ2500^ref/θ2500 =
  H(z) d(z)/[H(z) d(z)]^ref (Eq. 4) the change of aperture with
  cosmology, η_f the slope of the shell f_gas with aperture, and K(z) =
  K0 (1 + K1 z) (Eq. 5) the bias of the X-ray total mass;
- reference mass M2500^ref = A^η_M [d^ref/d] M2500 (Eq. 6), with the
  mass-profile slope η_m.

The normalisation constrains h^{3/2} Ω_b/Ω_m and is limited by K0 and
Υ0; the redshift dependence constrains d(z), limited by Υ1, K1 and the
sparsity of clusters at z ≳ 0.5, the last dominating the dark-energy
error in 2014 [src: Sect. 4.4, arXiv:1402.6212]. Ω_m enters both the
normalisation and the shape; with the normalisation priors widened, the
shape alone gives Ω_m = 0.200 ± 0.044 in flat ΛCDM, "consistent with
but marginally lower than" the normalisation result [src: Sect. 4.2,
arXiv:2111.09343].

### Step 5. Set the depletion prior from simulations
<!-- key: step-5-set-the-depletion-prior-from-simulations -->

2014: a uniform prior on Υ0 centred on 0.848, the mean of two
cooling + AGN-feedback SPH suites in the shell, with a full width of
20%, and −0.05 < Υ1 < 0.05 because neither suite shows evolution in
massive clusters at these radii [src: Sect. 4.2, Table 3,
arXiv:1402.6212]. 2022: the centre is corrected to 0.79, because "a
misinterpretation of one of the results" of one suite had pushed it
high; the width stays 20% (2.3 times the difference between the
suites) [src: Sect. 3, Table 7, arXiv:2111.09343]. The posterior on Υ0
essentially reproduces this prior [src: Table 7 note, same], so it
directly sets the error on Ω_b/Ω_m and Ω_m from the normalisation.

### Step 6. Calibrate the mass scale with lensing
<!-- key: step-6-calibrate-the-mass-scale-with-lensing -->

In 2014, 12 clusters with Weighing the Giants shear gave a lensing to
X-ray mass ratio K = 0.90 ± 0.09; the shear data are included in the
likelihood directly rather than as a prior because lensing masses depend
on cosmology through source distances [src: Sect. 4.3,
arXiv:1402.6212]. The authors note that K < 1, opposite to what
non-thermal support would give, suggests Chandra continuum temperatures
overestimated by ≳ 10% at 5–12 keV [src: footnote in Sect. 4.3, same].
In 2022 the same 12 clusters are used with colour-cut source selection
for all, a lognormal lensing/X-ray ratio of mean ln K(z) and scatter
σ_K, NFW for both, a simulation-motivated concentration prior for
lensing only, and a lensing mass bias W(z) = W0 + W1 (z − 0.4) with W0 =
0.96 ± 0.09 and W1 = −0.09 ± 0.03 [src: Sects. 2.3 and 3, Table 7,
arXiv:2111.09343]. Results: K0 = 0.93 ± 0.11 from f_gas alone, 0.99 ±
0.06 with CMB, BAO and SN (K0 is degenerate with Ω_m); σ_K = 0.14
+0.09/−0.07, "consistent with expectations for the impact of halo
triaxiality" [src: Sect. 4.5, same].

### Step 7. Likelihood
<!-- key: step-7-likelihood -->

Per cluster, a Gaussian in ln f_gas with mean the log of the model and
variance σ_f² plus the squared fractional measurement error; a Gaussian
scatter gave identical constraints [src: Sect. 4.3, footnote,
arXiv:1402.6212]. Priors on h and Ω_b h² are used for f_gas alone and
dropped when combining with the CMB [src: Table 4, same; Table 8,
arXiv:2111.09343].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### How the model evolved
<!-- key: how-the-model-evolved -->

| Element | Allen et al. 2008 (arXiv:0706.0033) | Mantz et al. 2014 (arXiv:1402.6212) | Mantz et al. 2022 (arXiv:2111.09343) |
|---|---|---|---|
| Quantity | cumulative f_gas(< r2500) | shell 0.8–1.2 r2500 | shell 0.8–1.2 r2500 |
| Depletion | baryon depletion b(z) = b0 (1 + α_b z), 0.65 < b0 < 1.0 from non-radiative simulations (b0 = 0.83 ± 0.04), −0.1 < α_b < 0.1; stars s(z) = s0 (1 + α_s z), s0 = (0.16 ± 0.05) h70^0.5 | hot-gas depletion Υ0 U(0.763, 0.932), Υ1 U(−0.05, 0.05), from cooling + feedback simulations | Υ0 U(0.71, 0.87), Υ1 U(−0.05, 0.05), plus mass slope α U(−1, 1) |
| Non-thermal support | γ, 1.0 < γ < 1.1 (1.2 as variant), from a ≈ 9% simulated bias at r2500 | absorbed in K, calibrated by lensing | same, with W(z) on lensing |
| Calibration | K = 1.0 ± 0.1 (instrument, abundances, clumping) | K(z) = K0 (1 + K1 z), K0 from 12 lensing clusters | same, K0 = 0.93 ± 0.11 |
| Aperture term | A with η = 0.214 ± 0.022 | A with η = 0.442 ± 0.035 | A^η_f with η_f = 0.390 ± 0.024; mass term η_m = 1.065 ± 0.016 |
| Place read | Sect. 4.2, Eq. 3 | Sects. 4.2–4.3, Eqs. 2–3, Table 3 | Sect. 3, Eqs. 1–6, Table 7 |

Reasons stated for the changes: in 2008 non-radiative simulations were
the benchmark because simulations with cooling "tend to significantly
over-produce young stars" [src: Sect. 4.2, arXiv:0706.0033]; by 2014
simulations with AGN feedback were judged realistic enough to predict the
hot-gas depletion directly, and the shell made the prediction "yet more
reliable" [src: Sect. 4.2, arXiv:1402.6212]; in 2022 the mass slope α
was freed and found to be 0.025 ± 0.033, consistent with no mass trend
for these massive clusters at these radii [src: Sects. 3 and 4.5,
arXiv:2111.09343]. The η values are not comparable between rows: 2008
measures the slope of cumulative f_gas with radius, 2014 and 2022 that
of the shell value with aperture, and 2022 notes explicitly that η_f "is
not the slope of f_gas(r)" [src: Sect. 3, same].

### Instrument calibration
<!-- key: instrument-calibration -->

The 2022 reprocessing with newer Chandra calibration (ciao 4.9, caldb
4.7.5.1, including a retroactive change to the ACIS contaminant model)
lowered temperatures marginally at z < 0.6 and raised f_gas by about 4%
on average; gas densities were unchanged, so the shift is a temperature
effect, within the systematic allowances of earlier work [src: Sect. 2.1,
arXiv:2111.09343]. Because K0 is fitted to lensing, a temperature shift
moves K0 rather than the cosmology, as long as the lensing clusters share
the calibration of the full sample [der: from Eqs. 3 and 5 of
arXiv:2111.09343].

### Gas-mass bias from clumping
<!-- key: gas-mass-bias-from-clumping -->

Azimuthal density variations make the measured rms density exceed the
mean; simulations put the bias at ≲ 5% near r2500 in relaxed clusters.
It is not modelled in 2022; a +5% bias would move Ω_m from the
normalisation by 0.01, a quarter of its posterior error [src: Sect. 3,
arXiv:2111.09343].

### Relaxed shell at r2500 versus all clusters at R500
<!-- key: relaxed-shell-at-r2500-versus-all-clusters-at -->

The same equation, with a stellar term, is used with 120 Planck-ESZ
clusters with XMM data to R500 to constrain the hydrostatic bias B =
M_HE/M_true instead of cosmology: f_gas,Th = K Υ/B A (Ω_b/Ω_m)
(D_A^ref/D_A)^{3/2} − f_* (Eq. 6), with K = 1 ± 0.1, η = 0.442 from the
2014 analysis, and Υ0 = 0.85 ± 0.03 [src: Sects. 2.1–2.2 and Appendix C,
arXiv:2204.12823]. R500 was chosen because the simulated depletion is
stable with radius there, while it declines near r2500, so an error in
the radius biases Υ less; the price is a larger scatter, σ_f ≈ 0.129
[src: Sect. 5.2.2 and Table 6, same]. A 10% shift of Υ0 (0.85 to 0.94)
did not move the bias parameters, with or without a prior on the total
bias, the posteriors being wide without it [src: Appendix C, same].

X-COP takes the third route: a universal gas fraction f_gas,univ = Y_b
Ω_b/Ω_m − f_* (Eq. 3), with Y_b from 295 simulated clusters of M500 > 3 ×
10¹⁴ M_sun in The Three Hundred (median 0.938 at R500, 16th–84th
percentiles 0.897–0.966) and f_* = 0.015 ± 0.005, giving f_gas,500 =
0.131 ± 0.009; the excess of the hydrostatic f_gas over this value
measures non-thermal pressure [src: Sects. 3.1.1–3.1.2, Table 1,
arXiv:1805.00034]. The depletion is taken from large radii because
there codes agree, whereas inside ≈ 0.5 R500 they differ substantially
[src: Sect. 3.1.1, same].

The three uses differ in which term is fixed: the cosmology analyses fix
Υ by simulation and K by lensing and fit Ω_b/Ω_m and d(z); the bias
analyses fix Ω_b/Ω_m and Υ and fit the mass bias. A depletion prior that
is wrong by x% therefore moves Ω_b/Ω_m by x% in one case and the
hydrostatic bias by x% in the other [der: Eq. 1 of arXiv:2111.09343 and
Eq. 6 of arXiv:2204.12823].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| SPA cuts | s > 0.87, p > −0.82, a > 1.00, > 50% of bootstrap triplets | relaxed-cluster series | arXiv:1502.06020 | Sect. 5.4 |
| Temperature cut | ≥ 5 keV | 2022 sample | arXiv:2111.09343 | Sect. 2.1 |
| Sample | 44 clusters (40 + Perseus, RCS J1447+0828, SPT J0615−5746, SPT J2215−3537); 4.9 Ms of cleaned Chandra time against 3.1 Ms in 2014 | 2022 | arXiv:2111.09343 | Sect. 2.1 |
| Redshift range | 0.018 (Perseus) to 1.160 (SPT J2215−3537) | 2022 | arXiv:2111.09343 | Table 1 |
| Shell | 0.8–1.2 r2500 | 2014, 2022 | arXiv:1402.6212 | Sect. 3.1 |
| Profile slope | f_gas ∝ Δ^−0.22, ∝ r^0.43 for 0.5–1.6 r2500 | 2014 | arXiv:1402.6212 | Sect. 3.1 |
| Depletion prior | Υ0 U(0.71, 0.87) (centre 0.79); 2014 centre 0.848 superseded | 2022; 2014 | arXiv:2111.09343; arXiv:1402.6212 | Table 7; Sect. 4.2 |
| Evolution priors | Υ1, K1 U(−0.05, 0.05) | 2014, 2022 | as above | Tables 3, 7 |
| Aperture slopes | η_f = 0.390 ± 0.024; η_m = 1.065 ± 0.016 | 2022 | arXiv:2111.09343 | Sect. 3 |
| Lensing mass bias | W0 = 0.96 ± 0.09, W1 = −0.09 ± 0.03 | 2022 | arXiv:2111.09343 | Sect. 3 |
| Mass calibration | K0 = 0.93 ± 0.11 (f_gas alone); 0.99 ± 0.06 (with CMB, BAO, SN); σ_K = 0.14 +0.09/−0.07 | 2022 | arXiv:2111.09343 | Sect. 4.5 |
| Intrinsic scatter | σ_f = 0.043 +0.020/−0.032 (95.4% upper limit 0.089), against 0.074 ± 0.023 in 2014 | 2022 | arXiv:2111.09343 | Sect. 4.5 |
| Mass slope of f_gas | α = 0.025 ± 0.033 | 2022 | arXiv:2111.09343 | Sect. 4.5 |
| Calibration update | ≈ +4% on f_gas at z < 0.6 | 2022 | arXiv:2111.09343 | Sect. 2.1 |
| Simulated depletion, R500 | Y_b = 0.938 (0.897–0.966), M500 > 3 × 10¹⁴ M_sun | The Three Hundred | arXiv:1805.00034 | Table 1 |
| Stellar fraction | f_* = 0.015 ± 0.005 within R500 | X-COP | arXiv:1805.00034 | Eq. 4 |

The 2022 scatter of 4.3% corresponds, in the authors' words, to 2.9% in
distance per cluster, compared with about 4.6% for SN Ia [src: Sect. 4.5,
arXiv:2111.09343]; L2 rounds this to 3%.

## What goes wrong
<!-- key: what-goes-wrong -->

| Failure | How it shows | Test that catches it | Source |
|---|---|---|---|
| Unrelaxed clusters in the sample | larger f_gas scatter, hydrostatic bias | SPA on bootstrapped images; compare scatter with the previous sample after freezing | arXiv:1502.06020, Sects. 3.1, 5.4 |
| Wrong depletion prior | normalisation, hence Ω_m and Ω_b/Ω_m, shifted; posterior equals prior | cross-check between simulation suites in the same shell; the 2014 centre had to be corrected from 0.848 to 0.79 | arXiv:1402.6212, Sect. 4.2; arXiv:2111.09343, Sect. 3 |
| Radius error at r2500 | depletion changes with radius there | measure in a shell; or work at R500 where Υ is flatter | arXiv:2204.12823, Sect. 5.2.2 |
| Temperature calibration | f_gas changes (≈ 4% from one calibration update) | lensing calibration K0; comparison of Chandra and XMM | arXiv:2111.09343, Sect. 2.1; arXiv:1402.6212, Sect. 4.3 |
| Gas clumping | f_gas high by ≲ 5% | simulations; azimuthal-median surface brightness | arXiv:2111.09343, Sect. 3; arXiv:1805.00034, Sect. 5.1 |
| Profile-shape assumption in the mass | ≈ 5% on hydrostatic f_gas between backward NFW and non-parametric methods at 1.5 Mpc | compare reconstruction methods | arXiv:1805.00034, Sect. 5.1 |
| Sparse data at high redshift | weak dark-energy constraints | deeper exposures at 0.6 < z < 0.9 (2022) | arXiv:1402.6212, Sect. 4.4; arXiv:2111.09343, Sect. 2.1 |
| Confirmation bias | trends tuned to expectations | random rescaling of each cluster's profiles until all fits are final | arXiv:1402.6212, Sect. 2.3 |
| Sample dependence of a bias trend | 3.8σ redshift trend "entirely dependent on the cluster sample" (L2) | sample-split tests | arXiv:2204.12823, Sect. 3.3 |

Consistency checks stated: Ω_m from the shape of f_gas(z) against Ω_m
from its normalisation (0.200 ± 0.044, consistent) [src: Sect. 4.2,
arXiv:2111.09343]; shape of the measured cumulative profiles against
simulated relaxed clusters [src: Sect. 3.1, Fig. 3, arXiv:1402.6212].

## Reading list
<!-- key: reading-list -->

- Method, current model and priors: Mantz et al. 2022 (arXiv:2111.09343),
  Sects. 2–3, Table 7.
- Method, shell and depletion choices with their reasons: Mantz et al.
  2014 (arXiv:1402.6212), Sects. 2.3, 3.1, 4.2–4.4.
- Foundation of the modern model: Allen et al. 2008 (arXiv:0706.0033),
  Sect. 4.2, Eq. 3, for the K, γ, b(z), s(z) parametrisation.
- Original proposal: Sasaki 1996 (arXiv:astro-ph/9611033), in L2.
- Sample selection: Mantz et al. 2015 (arXiv:1502.06020), Sects. 3–5.
- Lensing calibration: Applegate et al. 2016 (arXiv:1509.02162), in L2.
- Inverse use for the hydrostatic bias: Wicker et al. 2023
  (arXiv:2204.12823), Sects. 2 and 5, Appendix C.
- Universal gas fraction and depletion from simulations: Eckert et al.
  2019 (arXiv:1805.00034), Sects. 3.1 and 5.1.

## Not verified
<!-- key: not-verified -->

- The two simulation suites behind the depletion prior (Battaglia et
  al. 2013, Planelles et al. 2013) and the nature of the
  "misinterpretation" corrected in 2022: not read at source.
- The source of the W(z) lensing-bias model cited by arXiv:2111.09343:
  not identified in the sections read.
- The Pierre 2022 review section named in `subtopics.tsv` was not
  re-read for this dossier.
- Analyses that use published f_gas compilations to test varying
  constants or Ω_m(z) (2026 titles seen in a date-sorted search) and
  FLAMINGO and COLIBRE gas-fraction studies: titles only.
- No new f_gas cosmology sample after the 2022 analysis was found in a
  date-sorted search from June 2025 (2026-10-18).
