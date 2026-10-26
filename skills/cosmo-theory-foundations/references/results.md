# Theory foundations — quantified accuracy of the standard approximations

Snapshot: 2026-10-26

Every number is the size of an approximation, a correction or a convention difference, with the range in which the cited paper states it. Flags: [src] read in the cited paper, [der] derived here with the derivation given. Cosmological parameter values belong to the sibling skills.

## 1. Summary table
<!-- key: summary-table -->

The numbers most often needed, each detailed in the section named.

| Question | Answer | Source | Section |
|---|---|---|---|
| Eisenstein–Hu r_s(z_drag) against a Boltzmann code | factor 1.0275 on the numerical value | arXiv:1303.5076 [src: Sect. 5.2] | 2 |
| r_drag against r_* | 147.09 ± 0.26 against 144.43 ± 0.26 Mpc | arXiv:1807.06209 [src: Table 2] | 2 |
| Calibrated r_d formulae | 0.021% (fixed N_eff), 0.119% (free N_eff) | arXiv:1411.1074 [src] | 2 |
| Growth index formula for g(a) | 0.05% (Λ); 0.2% (w = −0.8), 0.4% (w = −0.5), 0.3% (w = −1.2), 0.5% (w = −1.5) | arXiv:astro-ph/0507263 [src: Sect. V.1] | 3 |
| Neutrino effect on the cb growth rate | 0.3–2%, scale-dependent | arXiv:1708.01154 [src] | 8 |
| Small-scale neutrino suppression | ΔP/P ≃ −8 f_ν at fixed ω_m | arXiv:astro-ph/0603494 [src] | 8 |
| Revised halofit | 5% (k ≤ 1 h/Mpc), 10% (1–10 h/Mpc) | arXiv:1208.2701 [src] | 4 |
| HMcode-2020 | RMS 2.5%, worst case 16% | arXiv:2009.01858 [src] | 4 |
| Limber with ℓ + 1/2 | error O(1/ℓ²); with ℓ, O(1/ℓ) | arXiv:0809.5112 [src] | 5 |
| One-loop EFT, real space, BOSS-like | k_max = 0.3 h/Mpc; DESI fits to 0.20 h/Mpc in redshift space | arXiv:1909.05277, arXiv:2411.12021 [src] | 7 |
| Kaiser × damping templates | 1–2% on D_A, H; ~5% on f | arXiv:1006.0699 [src] | 7 |
| Wide-angle corrections | non-negligible beyond opening angles of ~30° | arXiv:2608.19039 [src] | 6 |

## 2. Sound-horizon fitting formulae
<!-- key: sound-horizon-fitting-formulae -->

| Formula or statement | Stated accuracy and range | Source, flag |
|---|---|---|
| Eisenstein–Hu short form, s = 44.5 ln(9.83/Ω_0 h²)/sqrt[1 + 10 (Ω_b h²)^(3/4)] Mpc | ~2% for Ω_b h² ≳ 0.0125, 0.025 ≲ Ω_0 h² ≲ 0.5 | arXiv:astro-ph/9709112, Eq. 26 [src] |
| Eisenstein–Hu z_d and s against CAMB | CAMB r_s(z_drag) × 1.0275 matches the Eisenstein–Hu value in the Planck 2013 fiducial model | arXiv:1303.5076, Sect. 5.2 [src] |
| Validity of that constant factor | "sufficiently accurate over the range of ω_m and ω_b allowed by the CMB in the base ΛCDM cosmology" and the extended models of that paper | arXiv:1303.5076, Sect. 5.2 [src] |
| Spread between r_d conventions | 1–2% | arXiv:1411.1074, Sect. II.2 [src] |
| Aubourg et al. Eq. 16 (N_eff = 3.046) | 0.021% for Σm_ν < 0.6 eV, ω_b and ω_cb within 3σ of Planck | arXiv:1411.1074 [src] |
| Aubourg et al. Eq. 17 (free N_eff) | 0.119% for 0 < Σm_ν < 0.6 eV, 3 < N_eff < 5 | arXiv:1411.1074 [src] |
| Response of r_d to neutrino mass at fixed ω_cb | −0.26% for 0.5 eV, −0.92% for 1.0 eV | arXiv:1411.1074 [src: Sect. II.2] |
| Response of r_d to N_eff | one extra species lowers r_d by about 3.2% | arXiv:1411.1074 [src: Sect. II.2] |
| DESI DR2 Eq. 2, exponents | d ln r_d/d ln ω_bc = −0.23; d ln r_d/d ln ω_b = −0.13; d ln r_d/d ln N_eff = −0.1; pivot 147.05 Mpc at ω_b = 0.02236, ω_bc = 0.1432, N_eff = 3.04 | arXiv:2503.14738 [src] |
| r_d from that formula with CMB ω_b, ω_bc | 0.2% | arXiv:2503.14738, Sect. 1 [src] |
| BBN prior that calibrates r_d without the CMB | ω_b = 0.02218 ± 0.00055 (ΛCDM); 0.02196 ± 0.00063 with free N_eff | arXiv:2503.14738, Sect. 4.1 [src] |
| Precision of θ_* | fractional error ~10⁻⁴ | arXiv:2503.14738, Sect. 1 [src] |

Values of the ruler, to recognise which convention a number belongs to:

| Quantity | Value | Data and model | Source |
|---|---|---|---|
| r_d | 147.49 ± 0.59 Mpc (0.4%) | Planck 2013, ΛCDM, Σm_ν = 0.06 eV, N_eff = 3.046 | arXiv:1411.1074 [src: Sect. II.2]; superseded |
| r_drag | 147.09 ± 0.26 Mpc | Planck 2018 TT,TE,EE+lowE+lensing, base ΛCDM | arXiv:1807.06209, Table 1 [src] |
| r_* | 144.43 ± 0.26 Mpc | same | arXiv:1807.06209, Table 2 [src] |
| z_* | 1089.92 ± 0.25 | same | arXiv:1807.06209, Table 2 [src] |
| 100 θ_MC; 100 θ_* | 1.04092 ± 0.00031; 1.04110 ± 0.00031 | same | arXiv:1807.06209, Table 1 [src] |
| r_d of the DESI DR1 fiducial cosmology | 99.0792 h⁻¹Mpc with h = 0.6736 | Planck 2018 mean parameters | arXiv:2411.12021, Appendix C [src] |
| h r_d | 101.54 ± 0.73 Mpc | DESI DR2 BAO alone, ΛCDM | arXiv:2503.14738, Eq. 17 [src] |
| z_d as quoted | ≈1060 (DESI DR2); "around z = 1020" (eBOSS) | — | arXiv:2503.14738 [src: Sect. I]; arXiv:2007.08991 [src: Sect. II.3.1] |

θ_MC and θ_* are different parameters with different Planck values (row above): a prior written on one cannot be applied to the other [der].

## 3. Growth-rate and growth-index approximations
<!-- key: growth-rate-and-growth-index-approximations -->

Read in Linder 2005, arXiv:astro-ph/0507263, Sect. V.1 [src]. Accuracy of g(a) from Eqs. 16–17:

| Case | Accuracy | Range |
|---|---|---|
| Cosmological constant | better than 0.05% at any redshift, including total growth to today | Ω_m between 0.22 and 1 |
| Cosmological constant | better than 1% | down to Ω_m = 0.01 |
| w = −0.8 (−0.5) | within 0.2% (0.4%) | Ω_m between 0.2 and 1 |
| SUGRA-like, w0 = −0.82, wa = 0.58 | within 0.25% | — |
| w = −1.2 (−1.5), with Eq. 17 | 0.3% (0.5%) | — |
| w < −1 with the slope of Eq. 18 | 0.05% | — |
| Earlier fixed-index formulae normalised to today | "about 1%" on the normalised growth factor | as quoted by Linder |
| Single-integral formula (Heath; Peebles 1980) applied to w ≠ −1 | "only 5%" for w = −0.8 or −1.2, Ω_m = 0.3 | as quoted by Linder |
| DGP against a quintessence model with the same expansion (w0 = −0.78, wa = 0.32) | growth today differs by 7%; distances agree to 0.5% (0.01 mag) to z = 2 | why growth separates gravity from dark energy |

- The accuracy is on the growth factor g, not on f at one redshift, and holds for smooth dark energy in general relativity.
- Neutrinos change the growth rate of CDM + baryons by 0.3% to 2%, scale-dependent (arXiv:1708.01154, abstract; section 8), larger than the fitting error above: with Σm_ν free, the index formula is not the limiting approximation, the scale-independence is.
- Exponent 0.6 against 0.55: "Using Ω_m^0.6 introduces a needless 6% error in β, or a systematic bias of 0.03 (11%) in the value of Ω_m derived", for the concordance model (Linder & Cahn 2007, arXiv:astro-ph/0701317, Sect. III) [src].

σ8 against σ12, from Sánchez 2020, arXiv:2002.07829 [src: Sect. IV] (ΛCDM, the same wide priors, 2018–2019 data; quoted for the method, not as current measurements):

| Quantity | Planck | DES 3×2pt | BOSS |
|---|---|---|---|
| S12 = σ12 (ω_m/0.14)^0.4 | 0.815 ± 0.013 | 0.798 ± 0.043 | 0.716 ± 0.047 |

- fσ8 recovered from synthetic CMASS-like multipoles depends on the fixed h (tested at ±20% around 0.67; arXiv:2002.07829, Sect. V), and its uncertainty "derived under a fixed h" is "significantly underestimated"; expressed as fσ12 the constraints do not depend on whether h is fixed or marginalised.
- Across simulated catalogues in non-standard cosmologies, fσ12 "exhibits a notable robustness to the choice of cosmological template" (Euclid Collaboration 2026, arXiv:2603.13148) [src, abstract].
- The σ8 radius is fixed in h⁻¹Mpc, so its value in Mpc moves with h across any h prior; σ12 is defined in spheres of radius 12 Mpc, "whose value is similar to the standard σ8 for h ∼ 0.67" (arXiv:2002.07829, abstract) [src].
- DESI fiducial amplitude: σ8 = 0.811355, defined "excluding neutrinos" (arXiv:2411.12021) [src]; Planck 2018 quotes σ8 = 0.8111 ± 0.0060 for total matter (arXiv:1807.06209, Table 1) [src]. The two fields differ by roughly f_ν in amplitude (section 8), so equal numbers do not mean equal definitions.

## 4. Transfer-function and non-linear prescriptions
<!-- key: transfer-function-and-non-linear-prescriptions -->

Read in Eisenstein & Hu 1998, arXiv:astro-ph/9709112 [src]:

| Statement | Size | Where |
|---|---|---|
| Range of the full fitting formula | 0.025 ≲ Ω_0 h² ≲ 0.25, 0 ≤ Ω_b/Ω_0 ≤ 1; "better than 10%" overall (abstract) | Sect. 3.3 |
| Residuals for fully baryonic models | "nearly always under 10%"; improves as the baryon fraction decreases | Sect. 3.3 |
| Worst case | Ω_0 h² ≳ 0.25: first valley "significantly overestimated" | Sect. 3.3 |
| Zero-baryon form (Eq. 29) against CMBfast | 1% "through the CMB and large-scale structure regimes" | Sect. 4.2 |
| Phase of the oscillations at the shortest scales | small errors in the sound horizon give "order unity residuals" relative to the oscillation envelope | Sect. 3.3 |
| Baryonic oscillations | prominent only if the baryon fraction exceeds Ω_0 h² + 0.2; otherwise the main effect is a suppression below the sound horizon, "not well approximated by a change in the shape parameter Γ" | abstract |

The phase row is why the Eisenstein–Hu formula is used today for its no-wiggle limit and as a fast shape, never as a BAO template.

| Prescription | Stated accuracy | Range | Calibration | Source [src] |
|---|---|---|---|---|
| halofit, original | more accurate than the Peacock–Dodds formula | — | scale-free and CDM N-body | Smith et al. 2003, arXiv:astro-ph/0207664 |
| halofit, revised | 5% for k ≤ 1 h/Mpc, 0 ≤ z ≤ 10; 10% for 1 ≤ k ≤ 10 h/Mpc, 0 ≤ z ≤ 3 | k ≤ 30 h/Mpc | 16 models around WMAP best fits, constant w | Takahashi et al. 2012, arXiv:1208.2701, abstract |
| halofit + neutrino correction | original halofit over-predicts the suppression, most at k ~ 1 h/Mpc, by 10% of the total suppression | k < 10 h/Mpc, z < 3, 0.15–0.6 eV | N-body with neutrino particles | Bird, Viel & Haehnelt 2012, arXiv:1109.4416, abstract |
| HMcode (2015) | ≃5%; feedback models fitted at 5% with two parameters | k ≤ 10 h/Mpc, z ≤ 2 | ΛCDM, wCDM; OWLS | Mead et al. 2015, arXiv:1505.07833, abstract |
| HMcode-2020 | RMS 2.5%; rarely >5%; never >16%; worst at z ≃ 2 or unusual w | k < 10 h/Mpc, z < 2 | incl. massive ν | Mead et al. 2021, arXiv:2009.01858, abstract |
| HMcode-2020 feedback response | <1% | z < 1, k < 20 h/Mpc | hydrodynamical runs, six parameters | arXiv:2009.01858, abstract |
| As judged by KiDS-Legacy | HMCode2020 "twice as accurate" as revised halofit; HMCode2015 "~30% less accurate than HMCode2020" | 0.1 ≲ k ≲ 1 h/Mpc carries the shear signal | — | Wright et al. 2025, arXiv:2503.19441, Sect. 2.2 |
| Aletheia (σ12-based, h-free parameters) | sub-per-cent; variance ≈0.2% on dynamical dark energy against ≈1% for EuclidEmulator2 | 0.006 < k < 2 Mpc⁻¹; 0.2 < σ12 < 1.0; shape within ±5σ of Planck | N-body, evolution mapping | Sánchez et al. 2025, arXiv:2511.13826, abstract |
| CCL (library) | predictions "within a fraction of the expected statistical uncertainty" for LSST | LSST scales | cross-code validation | Chisari et al. 2019, arXiv:1812.05995 |

Halo-model ingredients [src: abstract of each paper]: Tinker mass function calibrated to ≲5% at z = 0 over 10^11–10^15 M_⊙/h, 10–20% better than earlier fits, with a "universal" amplitude that falls 20–50% from z = 0 to 2.5 (arXiv:0803.2706); Tinker bias with ~6% scatter, friends-of-friends bias ~10% below Δ = 200, peak-background split leaving ~20% residuals (arXiv:1001.3162).

Reading rule: each figure is a fit error against one simulation set. Outside the calibrated range of each row (w0wa far from −1, heavy neutrinos, redshifts and wavenumbers beyond the stated ones) none is a bound. Aletheia is quoted in Mpc⁻¹, the others in h/Mpc: converting a k_max needs h. The N-body and emulator floor is in `cosmo-simulations-mocks`.

## 5. Limber approximation
<!-- key: limber-approximation -->

| Statement | Size | Source [src] |
|---|---|---|
| Ordinary Limber, series in 1/(ℓ + 1/2) | error O(1/ℓ²) | LoVerde & Afshordi 2008, arXiv:0809.5112 |
| With the second-order term | O(1/ℓ⁴) | arXiv:0809.5112 |
| Using ℓ instead of ℓ + 1/2 | O(1/ℓ) | arXiv:0809.5112 |
| Where it fails | ν ≳ r̄/max[σ_A, σ_B] needed; for separated kernels ν ≳ r̄(r_A − r_B)/(σ_A σ_B): narrow bins and bins with small overlap | arXiv:0809.5112, body |
| Flat sky + Limber + Hankel together, cosmic shear | >1% power suppression at ℓ < 40; at least 11% of the systematic budget of a Euclid-like analysis | Kitching et al. 2017, arXiv:1611.04954, abstract |
| Spherical second-order Limber, cosmic shear | sub-per-cent for ℓ > 3; an order of magnitude below cosmic variance at all ℓ | Kilbinger et al. 2017, arXiv:1702.05301 |
| Flat-sky Hankel transform to ξ± | below 2% against the spherical transform (abstract); the body gives better than 5% for ξ+ and 0.2% for ξ− [src: Sect. 4.2] | arXiv:1702.05301 |
| Effect on CFHTLenS-class parameters | negligible; does not explain the lensing–Planck difference | arXiv:1702.05301; Lemos, Challinor & Efstathiou 2017, arXiv:1704.01054 |
| Limber for clustering, LSST Y1 or DES Y6 class | "may cause significant biases" | Fang et al. 2020, arXiv:1911.11947 |
| First-order Limber, LSST Y10 3×2pt (**forecast**) | insufficient at ℓ = 200–1000; second-order suffices there with a non-Limber method below | Leonard et al. 2023, arXiv:2212.04291, abstract |
| Limber, no RSD, or a poorer non-linear spectrum, Roman and Rubin 3×2pt (**forecast**) | each "can induce biases in cosmological constraints approaching or exceeding 1σ, and exceeding 2σ for Rubin in several cases" | Zhang et al. 2026, arXiv:2606.23781 |

The asymmetry to remember: for cosmic shear, with broad kernels, Limber has been safe for every survey analysed so far; for galaxy clustering in tomographic bins it is not, and DES Y3 already computed clustering without it (arXiv:2105.13548). Differentiable non-Limber codes now include RSD, magnification, f_NL, intrinsic alignments, CMB lensing and ISW (Chiarenza et al. 2026, arXiv:2609.01855).

## 6. Wide-angle and relativistic terms
<!-- key: wide-angle-and-relativistic-terms -->

| Statement | Size | Source [src, abstracts] |
|---|---|---|
| Geometry, non-linearities and radial selection on large-scale RSD, SDSS-II LRG mocks | "at the level of 20 per cent" on 30–200 Mpc/h | Samushia, Percival & Raccanelli 2012, arXiv:1102.1014, abstract |
| Odd multipoles from the end-point line of sight | detected "with high significance" in BOSS DR12 | Beutler, Castorina & Zhang 2019, arXiv:1810.05051 |
| Momentum (density-weighted velocity) statistics | deviations from plane-parallel "are large and could become important" at low redshift; even multipoles of the density–momentum cross-correlation are non-zero for any line of sight | Castorina & White 2020, arXiv:1911.08353 |
| Threshold in a full-sky calculation of density, velocity and ellipticity correlations | "non-negligible for opening angles Θ ≳ 30°" | Mikura et al. 2026, arXiv:2608.19039, abstract |
| Neglecting relativistic and wide-angle terms, SPHEREx-like survey with σ(f_NL) ~ 1 (**forecast**) | shifts f_NL "by an amount of order its own uncertainty" | Lukens & Jeong 2026, arXiv:2608.18334 |
| Optimal wide-angle (two-ℓ) estimator against Yamamoto | "order-unity improvements in the signal-to-noise ratio of ultra-large-scale power spectrum measurements" | Sailer et al. 2026, arXiv:2607.05513 |
| Redshift-space term in the relativistic count | "the largest single correction on intermediate scales" | Bonvin & Durrer 2011, arXiv:1105.5280, body |

The sibling clustering skill does not list wide-angle terms among the BAO or RSD systematics; they matter for f_NL and dipole analyses and are on the referee list of `cosmo-peculiar-velocities`.

## 7. Perturbation theory and EFTofLSS validity ranges
<!-- key: perturbation-theory-and-eftoflss-validity-ranges -->

| Model or analysis | Range | Statement | Source [src] |
|---|---|---|---|
| One-loop EFT matter P(k) | k ~ 0.24 h/Mpc | per cent precision | Carrasco, Hertzberg & Senatore 2012, arXiv:1206.2926, abstract |
| Two-loop IR-resummed EFT matter P(k) | k ~ 0.6 h/Mpc | within 1%; 2% BAO residual before resummation | Senatore & Zaldarriaga 2015, arXiv:1404.5954, abstract |
| One-loop EFT, biased tracers, real space | k_max = 0.3 h/Mpc | "sufficient … for the volume and redshifts typical to the BOSS survey" | arXiv:1909.05277, Sect. 3.1 |
| Quadrupole counterterm estimate | c_2² ≈ 2.5 σ_v² ~ 60 Mpc²/h² for σ_v ~ 5 Mpc/h, b1 = 2, f = 0.75 | "order-of-magnitude estimate" | arXiv:1909.05277, Sect. 3.1 |
| IR separation scale | k_S = 0.2 h/Mpc, same result as k_S = k/2 | residual dependence is theory error | arXiv:1909.05277, App. A |
| DESI DR1 full shape, velocileptors EPT | 0.02 < k < 0.20 h/Mpc, ℓ = 0, 2 | exact k_max has no significant impact; counterterm prior width 12.5 h⁻²Mpc² | Adame et al. 2024, arXiv:2411.12021, Sects. 4.5 and 4.7 |
| velocileptors, PyBird, FOLPSν on AbacusSummit | one-loop range | consistent; "no systematic error associated with the modeling" at DESI Y1 volume | Maus et al. 2024, arXiv:2404.07272 |
| One-loop LPT with full resummation | quasi-linear | per cent on halo and mock-galaxy P(k) and ξ | Chen et al. 2021, arXiv:2012.04636 |
| EFT blind challenge | 100 × BOSS volume | H0, Ω_m, amplitude within sub-per-cent statistical errors, two teams | Nishimichi et al. 2020, arXiv:2003.08277, abstract |
| CLASS-PT | — | ~0.3 s per evaluation | Chudaykin et al. 2020, arXiv:2004.10607, abstract |
| elf (JAX, EPT and LPT) | k ≲ 1 h/Mpc | numerical error ~0.01% against brute-force integration: accuracy of the integrals, not of one-loop theory | Kobayashi & Akitsu 2026, arXiv:2610.08023, abstract |
| Gaussian streaming model, mapping only | s > 10 (25) Mpc/h | <0.5% (2%) for monopole (quadrupole) | Reid & White 2011, arXiv:1105.4165, abstract |
| Gaussian streaming model with PT inputs | s > 40 Mpc/h, b = 1.4–2.8 | 2% | arXiv:1105.4165, abstract |
| Kaiser × damping templates against TNS | BAO scales | 1–2% on D_A, H; ~5% on f | Taruya, Nishimichi & Saito 2010, arXiv:1006.0699 |
| First BOSS EFT analysis | BOSS DR12 | ln(10^10 A_s), Ω_m, H0 to 13%, 3.2%, 3.2% with fixed n_s and Ω_b/Ω_c | D'Amico et al. 2020, arXiv:1909.05271, abstract |
| Two-loop EFT, redshift-space galaxy P(k) | k_max 0.2 → 0.34 h/Mpc, LRG sample at z = 0.5 | 49 free coefficients; "constraints on σ8 are not significantly enhanced by the inclusion of two-loop terms" | Philcox 2026, arXiv:2610.13867 [src: abstract] |
| Shape template held fixed against shape parameters varied (emulated hybrid PT + N-body model), DESI DR1 LRG2 | α_⊥, α_∥, fσ8 | with a tight Planck prior the constraints differ "by less than a twentieth of their own uncertainties" | Song et al. 2026, arXiv:2610.21235 [src: abstract] |
| Priors in Mpc/h against Mpc, Stage-IV synthetic data (**forecast**) | ΛCDM to w0waCDM | shifts from marginalisation fall "from several standard deviations to well within 1σ" | Pezzotta et al. 2026, arXiv:2610.08751 |

A k_max is not a property of the theory alone: it depends on the tracer's bias and density, the redshift, the multipoles fitted and the nuisance priors.

## 8. Neutrino effects on σ8, growth and the power spectrum
<!-- key: neutrino-effects-on-sigma8-growth-and-the-power -->

| Statement | Size | Condition | Source [src] |
|---|---|---|---|
| Growth of δ_cdm below the free-streaming scale | ∝ a^(1 − (3/5) f_ν) | matter domination, f_ν ≪ 1 | arXiv:astro-ph/0603494, Sect. 4.5.6 |
| Small-scale suppression | ΔP/P ≃ −8 f_ν; exact form (1 − f_ν)³[1.9 × 10^5 g(a0) ω_m f_ν/N_ν]^(−(6/5) f_ν) | fixed (ω_m, ω_b, Ω_Λ, A, n_s, τ); f_ν < 0.07; k ≫ k_nr, k_eq | arXiv:astro-ph/0603494, Sect. 4.5.6 |
| Large scales | no dependence on f_ν at fixed ω_m | k < k_nr | arXiv:astro-ph/0603494 |
| Non-relativistic transition | a0/a_nr = 2000 m_ν/(1 eV) | per species | arXiv:astro-ph/0603494 |
| Growth rate of CDM+baryons | changed by 0.3% to 2% | k = 0.01–0.5 h/Mpc, M_ν ≤ 0.15 eV | Villaescusa-Navarro et al. 2018, arXiv:1708.01154, abstract |
| Momentum bias of haloes relative to cb | 1 on large scales | implies a velocity bias relative to total matter | arXiv:1708.01154 |
| Universality of mass function and bias | better with σ²_cdm than with σ²_m | N-body with ν particles | Castorina et al. 2014, arXiv:1311.1212; Villaescusa-Navarro et al. 2014, arXiv:1311.0866 |
| r_d | −0.26% for Σm_ν = 0.5 eV at fixed ω_cb | — | arXiv:1411.1074, Sect. II.2 |

If neutrinos are unclustered at the σ8 radius, δ_m = (1 − f_ν) δ_cb there, so the total-matter σ8 is below the cb σ8 by about f_ν: that is the size of the Planck-versus-DESI definition difference [der]. No paper giving its size from a Boltzmann code was read.

## 9. History of the key approximations
<!-- key: history-of-the-key-approximations -->

What replaced what, so that a stale convention can be recognised.

| Item | Older form | Current form | Size of the change | Sources |
|---|---|---|---|---|
| Growth rate | f ≈ Ω^0.6, β = Ω_0^0.6/b (1987–1998) | f = Ω_m(z)^0.55 for ΛCDM (2005); fσ8 from 2009 | "needless 6% error in β" (arXiv:astro-ph/0701317, Sect. III) | arXiv:astro-ph/9708102; arXiv:astro-ph/0507263; arXiv:0808.0003 |
| Shape of P(k) | one parameter Γ = Ωh (1994) | Eisenstein–Hu with baryons (1998), Boltzmann codes | "cannot be fit by a single Γ" | arXiv:astro-ph/9311057; arXiv:astro-ph/9709112 |
| Sound horizon | Eisenstein–Hu formula (to ~2013) | Boltzmann r_drag; calibrated formulae (2015, 2023) | factor 1.0275 (arXiv:1303.5076, Sect. 5.2) | arXiv:1303.5076; arXiv:1411.1074; arXiv:2212.04522 |
| BAO observable | r_s/D_V, D_A, A(z) | D_M/r_d, D_H/r_d, D_V/r_d | factor (1+z) between D_A and D_M | arXiv:1303.5076; arXiv:1411.1074 |
| r_d value | 147.49 ± 0.59 Mpc (Planck 2013; arXiv:1411.1074, Sect. II.2) | 147.09 ± 0.26 Mpc (Planck 2018; arXiv:1807.06209, Table 2) | — | arXiv:1411.1074; arXiv:1807.06209 |
| N_eff | 3.046 (Planck 2013, 2018; abstracts of each) | 3.044 (DESI DR1 full shape, DESI DR2; arXiv:2503.14738, Sect. IV.1) | — | arXiv:1303.5076; arXiv:1807.06209; arXiv:2503.14738 |
| Non-linear P(k) | halofit 2003 | Takahashi 2012 + Bird; HMcode 2015 (Planck 2018); HMcode-2020 (KiDS-Legacy) | 5% and 10% → RMS 2.5% stated errors (arXiv:1208.2701, abstract; arXiv:2009.01858, abstract) | arXiv:astro-ph/0207664; arXiv:1208.2701; arXiv:2009.01858 |
| RSD template | Kaiser × damping | TNS (2010); streaming (2011); one-loop EFT (2020) | 5% on f | arXiv:1006.0699; arXiv:1105.4165; arXiv:1909.05277 |
| Compression | α_∥, α_⊥, fσ8 (BOSS, eBOSS) | ShapeFit and full modelling (DESI) | eBOSS itself: the compression "might not be the best approach for future surveys" | arXiv:2007.08991; arXiv:2106.07641; arXiv:2411.12021 |
| Amplitude | σ8 | σ_s8 (DESI ShapeFit), σ12 (proposed 2020, used by Euclid preparation and Aletheia) | radius fixed in h⁻¹Mpc against fixed in Mpc | arXiv:2002.07829; arXiv:2603.13148 |
| Limber | ℓ, flat sky | ℓ + 1/2; non-Limber for clustering | O(1/ℓ) → O(1/ℓ²) | arXiv:0809.5112; arXiv:1911.11947 |
| Multipole estimator | plane-parallel, per-pair sums | Yamamoto with FFTs (2015–2017); wide-angle window (2019); optimal two-ℓ (2026) | odd multipoles appear | arXiv:astro-ph/0505115; arXiv:1810.05051; arXiv:2607.05513 |

## Not verified
<!-- key: not-verified -->

- The accuracy of DESI's power-law r_d formula against a Boltzmann code: not stated in arXiv:2209.14330 or arXiv:2212.04522, whose bodies were searched on 2026-10-15 (`systematics.md` section 3).
- The size of the wide-angle correction for DESI. For BOSS DR12 it is now read: window and wide-angle terms reach "up to 5% of the measurement uncertainties in the even multipoles" and dominate the odd ones (Beutler, Castorina & Zhang 2019, arXiv:1810.05051) [src: Sect. 4]; details in `systematics.md` section 9.
- The size of the difference between cb and total-matter σ8 from a Boltzmann code: not read in a paper.
- The accuracy of θ_MC as an approximation of θ_* beyond the one Planck 2018 pair of values.
- A remark of Planck 2018 on a systematic uncertainty, reported by the second pass of this build, could not be located again and is not used.
- Accuracy of the Limber approximation for CMB lensing cross-correlations: searched on 2026-10-26, no paper quantifying it found beyond the non-Limber codes (arXiv:2609.01855).
