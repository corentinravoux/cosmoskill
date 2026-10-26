# open-questions — cosmo-inflation-primordial

Snapshot: 2026-10-07

Scope: the live controversies in observational primordial physics with both sides cited, internal tensions between analyses, method debates, what the next data will decide (forecasts labelled), and the misconceptions and stale claims that still circulate, each with the paper that corrects it.

Flags as in the other files. Numbers are repeated here only when the argument needs them; tables are in `results.md`.

## 1. Has n_s moved, and does it exclude Starobinsky-type inflation?
<!-- key: has-ns-moved-and-does-it-exclude-starobinsky -->

**The claim.** ACT DR6 combined with a truncated Planck, CMB lensing and DESI DR1 BAO gives n_s = 0.974 ± 0.003 in ΛCDM (arXiv:2503.14452) [src: abstract], and the Starobinsky R² model then sits at the edge of the 2σ region for N⋆ around 60 with the usual analytical approximations (arXiv:2504.20757) [src: abstract]. For 50 ≤ N ≤ 60 the leading-order prediction n_s ≈ 1 − 2/N gives n_s = 0.9667 at N = 60 (arXiv:2607.28445) [src: Sect. 1]. A literature of "ACT-compatible" models followed: Higgs inflation with vector-like quark stabilisation (McDonald 2025, arXiv:2505.07488), extensions of the α-Starobinsky model (Shobcha et al. 2026, arXiv:2606.24131), polynomial and α-attractor variants reviewed by Kallosh and Linde (arXiv:2505.13646).

**The objections.**

1. The shift is a CMB + BAO effect in a model where CMB and BAO disagree. CMB data have a degeneracy between n_s and the BAO parameters; the DESI–CMB tension in ΛCDM moves n_s along it. Ferreira et al. "urge caution in interpreting CMB+BAO constraints on n_s until the BAO-CMB tension is resolved" (arXiv:2507.12459). The three-experiment CMB-only value is 0.9679 ± 0.0033 (arXiv:2506.20707) [src: Sect. II].
2. The shift depends on the cosmological model. With Ω_K free, n_s = 0.9667 ± 0.0041 (Planck + DESI) or 0.9692 ± 0.0035 (with ACT and SPT); with w0wa free, 0.9716 ± 0.0032; the authors conclude that the tension with Starobinsky, Higgs and the simplest α-attractors "holds only for ΛCDM" (arXiv:2607.28445) [src: abstract]. With α_s, N_eff and Σm_ν free, n_s = 0.9758 ± 0.0064 (arXiv:2609.35964) [src: abstract] and both Starobinsky inflation and the Bi-thermal Big Bang model are allowed again, although both are "ruled out at about the 95% confidence level" in six-parameter ΛCDM (arXiv:2609.35964).
3. The prediction itself moves. Beyond the usual analytical approximations, Starobinsky inflation stays within 2σ for N⋆ ≳ 58 (Drees and Xu 2025, arXiv:2504.20757) [src: abstract].

**The reheating route and its cost.** A larger N requires a stiff post-inflationary phase. Drees and Xu find that the ACT-era n_s implies an effective reheating equation of state ω ≳ 0.462, which excludes purely perturbative reheating (ω ≈ 0), and T_rh ≲ 2 × 10¹⁰ GeV for ω ≤ 1; agreement within 1σ needs 4 MeV ≲ T_rh ≲ 10 GeV with 0.8 ≲ ω ≤ 1 (arXiv:2504.20757) [src: abstract]. Dorsch et al. show that a stiff epoch blue-tilts the primordial gravitational-wave spectrum, that the 1σ region allowed by CMB + BAO is "already excluded" by the BBN bound on extra radiation, and that part of the 2σ region would be detectable by Einstein Telescope, LISA, DECIGO or BBO (**forecast**; arXiv:2606.28502) [src: abstract].

**Where it stands.** Three numbers are in use for the same quantity: 0.9649 (Planck 2018, arXiv:1807.06211) [src: abstract], 0.9679 (CMB-SPA, arXiv:2506.20707) [src: Sect. II], 0.974 (P-ACT-LB, arXiv:2503.14452) [src: abstract]. A statement that a model is excluded is a statement about one of them, in ΛCDM, for an assumed N. What will decide: whether the DESI–CMB distance tension survives the DESI full-survey BAO and the dark-energy debate (`cosmo-dark-energy-modified-gravity`), and the SO and SPT-3G small-scale spectra.

## 2. Running of the spectral index
<!-- key: running-of-the-spectral-index -->

- eBOSS Lyα P1D with Planck gave dn_s/dln k = −0.010 ± 0.004 (arXiv:1911.09073) [src: abstract]. P-ACT alone excludes that value at more than 3σ (arXiv:2503.14454) [src: Sect. IV.1], and the DESI DR1 P1D with CMB and BAO gives 0.0014 ± 0.0041 (arXiv:2601.21432) [src: abstract]. The negative running is superseded; the cause on the Lyα side is discussed in `cosmo-lyman-alpha`.
- Planck prefers a slightly negative running and ACT alone gives 0.034 ± 0.022; P-ACT-LB gives 0.0062 ± 0.0052 (arXiv:2503.14454) [src: Sect. IV.1; abstract].
- The slow-roll expectation, |α_s| of order (1 − n_s)², lies well below the present error [der].
- **Forecasts**: Euclid σ(α_s) = 0.004 (pessimistic) and 0.0015 (optimistic) for a fiducial α_s = −0.001 (arXiv:2507.15819) [src: abstract]; SO-like and CMB-HD-like surveys would tighten the binned spectrum at k = 0.2 Mpc⁻¹ from 0.5% (current CMB) to 0.1% (arXiv:2609.35964) [src: abstract]. A detection of slow-roll running is therefore not expected from the experiments now funded, unless the optimistic Euclid case is combined with a future CMB data set.

## 3. Tensor modes: how far can r be pushed, and by whom?
<!-- key: tensor-modes-how-far-can-r-be-pushed-and-by-whom -->

- **Current floor.** r < 0.036 from BK18, σ(r) = 0.009 (arXiv:2110.00483) [src: abstract]. No newer B-mode limit on inflationary r exists at the snapshot (search of 2026-10-09). SPT-3G's independent r < 0.25 confirms the method, not the depth (arXiv:2505.02827) [src: abstract].
- **The target.** Starobinsky-type models predict r falling as 1/N², far below the current limit; reaching it needs σ(r) well below the BK18 value [der, textbook formula].
- **Who gets there (all forecasts).** SO with six SATs to 2035: σ(r) = 1.2 × 10⁻³ for ℓ_knee = 50, moderately complex foregrounds and 70% delensing; 7 × 10⁻⁴ in the optimistic case (arXiv:2512.15833) [src: abstract]. LiteBIRD after reformation: total δr < 0.002 at 68% (arXiv:2607.25285) [src: abstract], weaker than the pre-reformation target. CMB-S4 lost agency support in July 2025 (per `cosmo-cmb`).
- **What limits it.** Dust complexity can bias r by up to r ∼ 0.03 with a low-order moment expansion in the most extreme case considered, σ(β_d) ≃ 0.3 (arXiv:2508.00073) [src: abstract], far above the statistical target, so the forecast is conditional on the foreground model; residual beam leakage in BICEP3 at 95 GHz is equivalent to r = (1.12 ± 0.06) × 10⁻³ after the extended deprojection (arXiv:2608.25016) [src: abstract], comparable to the next-generation σ(r).
- **Would a detection prove inflation?** Komatsu argues that sourced tensor modes from matter fields are an alternative to vacuum fluctuations and that distinguishing them should shape experiment design (arXiv:2202.13919). Causal post-inflationary sources are constrained separately (arXiv:2601.20958).
- **The Lyth bound** ties a detection at the current level to a super-Planckian field excursion (arXiv:hep-ph/9606387); a null result at the next generation's sensitivity would leave small-field models untouched.

## 4. Can large-scale structure overtake the CMB on f_NL?
<!-- key: can-large-scale-structure-overtake-the-cmb-on -->

**For.** DESI DR1 reaches σ(f_NL^local) = 9 from scale-dependent bias (arXiv:2411.17623); an external power spectrum + bispectrum reanalysis of DESI DR1 quotes −0.1 ± 7.4, and −0.0 ± 4.1 combined with the CMB, "the strongest bound on multi-field inflation yet obtained" (arXiv:2512.04266) [src: abstract]. SPHEREx is designed for Δf_NL < 0.5 (**forecast**, arXiv:2511.02985) and Euclid forecasts 2.2 (**forecast**, arXiv:2507.15819).

**Against.** The measured quantity is f_NL · b_φ. Barreira's position is that "the error bar σ(f_NL) remains undetermined and the results cannot be compared with the CMB" without independent knowledge of b_φ, and that wide b_φ priors bias the result (arXiv:2205.05673). Assembly bias can change b_φ by a large factor and even its sign (arXiv:2209.07251). Every forecast above assumes universality.

**Middle ground.** Priors on p from hydrodynamical simulations for the actual selection: p̄ ≃ 1.4 for DESI quasars gives −3.3 ± 9.2 (arXiv:2602.12357) [src: abstract], between the two DESI collaboration values. Multi-tracer and cross-correlation analyses test systematics but share the b_φ dependence (arXiv:2604.05213, arXiv:2512.17865).

**Internal consistency today.** Five DESI DR1 analyses with different statistics (arXiv:2411.17623, arXiv:2602.12357, arXiv:2604.05213, arXiv:2606.24651, arXiv:2512.04266) give mutually consistent values; each is listed with its place in `results.md`, section 5. They use the same catalogues and are not independent. eBOSS DR16 analyses hint at unexplained large-scale systematics (arXiv:2309.15814).

**Equilateral and orthogonal shapes.** The strongest large-scale-structure values, from BOSS + high-redshift DESI with simulation-based bias priors, are f_NL^equil = 200 ± 230 and f_NL^orth = −24 ± 86, and DESI DR1 alone gives f_NL^equil = 719 ± 390 (arXiv:2512.04266) [src: abstract]; Planck 2018 gives −26 ± 47 and −38 ± 24 (arXiv:1905.05697) [src: abstract]. The galaxy bispectrum is prior-dependent (arXiv:2201.07238).

**Beyond templates.** A 2.4σ global excess for a spin-0 cosmological-collider template in Planck (arXiv:2511.17500) [src: abstract], no detection for strongly mixed collider models in PR4 (arXiv:2511.19179). Neither is a claim of detection.

**What decides.** DESI full-survey samples (2027), then SPHEREx; for both the limiting issue is b_φ and imaging systematics, not volume.

## 5. Spatial curvature: closed, flat or open?
<!-- key: spatial-curvature-closed-flat-or-open -->

- **Closed (2019–2020).** Planck 2018 spectra alone prefer positive curvature (Ω_K < 0) at more than 99% C.L. (arXiv:1807.06209; arXiv:1911.02087 [src: abstract]), in 2.5 to 3σ tension with lensing and BAO in the curved model (arXiv:1908.09139) [src: abstract]. Counter-position: with a different Planck likelihood the spectra are consistent with flatness and CMB + BAO give 0.0004 ± 0.0018 (arXiv:2002.06892) [src: abstract]. The preference is the A_L feature in another parameter (arXiv:1807.06209); its later history is in `cosmo-cmb`.
- **Open (2025–2026).** DESI DR2 + CMB give Ω_K = +0.0023 ± 0.0011 (arXiv:2503.14738) [src: Table 5 (Sect. VI), given as 10³Ω_K = 2.3 ± 1.1]; low-redshift data alone are claimed to prefer an open universe: 2σ from DESI BAO + SNe Ia whatever the SN sample, above 3σ with θ_* added, reaching 5σ with the DES-Y5 SNe (arXiv:2512.19565) [src: abstract]. Counter-position: the preference exists only inside ΛCDM and vanishes when dark energy is allowed to evolve, so it is "an artifact of limited model flexibility" (arXiv:2604.23492); DESI's own w0waCDM + Ω_K fits are consistent with zero (arXiv:2503.14738).
- **Inflationary reading.** Chudaykin et al. take a small negative curvature, quoted as Ω_k ≃ 3 × 10⁻³ (arXiv:2607.28445) [src: abstract], as a motivation to revisit open-universe inflation and note that it lowers n_s (arXiv:2607.28445). Efstathiou and Gratton read flatness as support for a long inflation (arXiv:2002.06892).
- **Judgment.** Both the 2019 closed hint and the 2025 open hint appear when two data sets that disagree in ΛCDM are forced into ΛCDM + Ω_K. Neither exceeds about 2σ in a combined fit. **Forecast**: Euclid σ(Ω_K) = 0.0044 (0.003) alone (arXiv:2507.15819, abstract), which does not improve on DESI + CMB.

## 6. Cosmic birefringence: a 4.8σ signal nobody claims
<!-- key: cosmic-birefringence-a-4-8sigma-signal-nobody -->

- **For.** Same sign and size in WMAP, Planck PR3, Planck PR4 and ACT DR6; no frequency dependence over 23 to 353 GHz (arXiv:2205.13962) [src: abstract]; a joint ACT + Planck analysis at 0.277° ± 0.057° (arXiv:2608.06480) [src: abstract] (also arXiv:2509.13654).
- **Against.** Each analysis rests on an assumption about either the Galactic EB or the instrument angles. β falls with larger masks in Planck PR4 (arXiv:2201.07682); ACT has "systematics … that are not understood" (arXiv:2509.13654); the joint 4.8σ takes the ACT priors at face value and falls to 3.5σ in the dust-robust variant (arXiv:2608.06480) [src: abstract].
- **What decides.** Absolute angle calibration at the level of a tenth of a degree or better: SO wire grid (0.08° anticipated, **forecast**, arXiv:2606.11300) [src: abstract]; LiteBIRD (**forecast** 5 to 13σ for β = 0.3°, depending on the pipeline, arXiv:2503.22322 [src: abstract], for the pre-reformation design). BICEP/Keck cannot test a constant β (arXiv:2603.06812).
- **Interpretation** (axion-like dark energy or dark matter, early dark energy) is reviewed by Komatsu (arXiv:2202.13919) and belongs to `cosmo-dark-energy-modified-gravity` and `cosmo-neutrinos-dark-matter`.

## 7. Primordial features: residual hints
<!-- key: primordial-features-residual-hints -->

Planck spectra contain a few frequencies with Δχ² ≃ −10 to −15, at most 2.6σ globally, weaker with PR4 (arXiv:2605.30236) [src: abstract]. The combination of Planck, ACT DR6 and DESI DR2 limits oscillation amplitudes to about 2% and the Bayesian evidence prefers no feature (arXiv:2606.28310). DESI DR1 clustering reaches 3% and shows that a fixed-cosmology search converts the DESI–Planck distance mismatch into a 3σ "feature" (arXiv:2610.10530). **Forecasts**: an order of magnitude from SO + LiteBIRD (arXiv:2605.30236) and from DESI and Euclid relative to BOSS (arXiv:1906.08758); Euclid measures an amplitude of 0.01 to 21% (linear) and 22% (logarithmic) in the pessimistic case (arXiv:2507.15819) [src: abstract]. The open method question is how to combine CMB and galaxy searches when their background cosmologies disagree.

## 8. Isocurvature
<!-- key: isocurvature -->

No hint. The open directions are small scales, where P-ACT significantly improves the blue-tilted CDI limit over the Planck-only 10¹⁰ P_II^(2) < 59 (arXiv:2503.14454) [src: Sect. IV.3.1] and where adding SPT improves the tilt constraint moderately (arXiv:2606.11312), and the dependence of the limits on n_s and on the data combination. **Forecast**: Euclid would tighten blue-tilted isocurvature limits by an order of magnitude (arXiv:2507.15819).

## 9. Internal tensions between analyses
<!-- key: internal-tensions-between-analyses -->

| Quantity | Analysis A | Analysis B | Size | Status |
|---|---|---|---|---|
| n_s in ΛCDM | 0.9649 ± 0.0042, Planck 2018 (arXiv:1807.06211) [src: abstract] | 0.974 ± 0.003, P-ACT-LB (arXiv:2503.14452) [src: abstract] | no σ can be quoted, Planck data are in both | explained by small-scale data plus the CMB–BAO tension (section 1) |
| n_s, CMB only against CMB + BAO | 0.9679 ± 0.0033, CMB-SPA (arXiv:2506.20707) [src: Sect. II] | 0.974 ± 0.003, P-ACT-LB (arXiv:2503.14452) [src: abstract] | — | BAO pull (arXiv:2507.12459) |
| Running | −0.010 ± 0.004, eBOSS Lyα + Planck (arXiv:1911.09073) [src: abstract] | 0.0060 ± 0.0055, P-ACT (arXiv:2503.14454) [src: Sect. IV.1, Eq. 2] | more than 3σ, as stated by ACT | resolved against the old value |
| Sign of the running | Planck: slightly negative | ACT alone: 0.034 ± 0.022 (arXiv:2503.14454) [src: Sect. IV.1] | — | statistical |
| f_NL^local from one DESI DR1 data vector | −3.6 +9.0/−9.1 with p = 1.6 for quasars | +3.5 +10.7/−7.4 with p = 1 (arXiv:2411.17623) [src: abstract; Table 11] | comparable to σ | b_φ, unresolved |
| f_NL^local from eBOSS DR16 quasars | −12 ± 21 (arXiv:2106.13725) [src: abstract] | −4 < f_NL < 27 at 68% (arXiv:2309.15814) [src: abstract] | — (same quasars, different weights) | weights and systematics treatment |
| f_NL^equil | 719 ± 390, DESI DR1 alone (arXiv:2512.04266) [src: abstract] | −26 ± 47, Planck 2018 (arXiv:1905.05697) [src: abstract] | — | bias priors; 200 ± 230 with BOSS added and simulation priors (arXiv:2512.04266) [src: abstract] |
| Ω_K | −0.0107 +0.0064/−0.0053, CMB alone (arXiv:2503.14738) [src: Table 5 (Sect. VI), given as 10³Ω_K = −10.7 +6.4/−5.3] | +0.0023 ± 0.0011, DESI DR2 + CMB (arXiv:2503.14738) [src: Table 5 (Sect. VI), given as 10³Ω_K = 2.3 ± 1.1] | sign change | geometric degeneracy; CMB–BAO tension |
| β | 0.215 ± 0.074, ACT DR6 (arXiv:2509.13654) [src: abstract] | 0.342 +0.094/−0.091, WMAP + Planck (arXiv:2205.13962) [src: abstract] | — | consistent, as stated by ACT (arXiv:2509.13654) [src: abstract] |
| Logarithmic feature in DESI DR1 | 3σ global at fixed Planck cosmology | absent with cosmology varied (arXiv:2610.10530) | — | artefact of the distance tension |
| Neutrino-density isocurvature | small peak at non-zero amplitude, Planck alone | gone with ACT DR6 (arXiv:2503.14454) | insignificant | resolved |

No tension exists between B-mode analyses: all current r limits tighter than SPT-3G's use the BICEP/Keck maps.

## 10. Method debates
<!-- key: method-debates -->

1. **Which n_s goes to model builders.** CMB + BAO in ΛCDM (the tightest; arXiv:2503.14452), CMB only (arXiv:2507.12459), or a posterior marginalised over late-time and neutrino extensions (arXiv:2607.28445, arXiv:2609.35964). The choice changes the verdict on the most-cited models.
2. **Fixing or marginalising b_φ.** Fixed p per tracer (arXiv:2411.17623); narrow Gaussian priors on p (arXiv:2606.24651); simulation priors (arXiv:2602.12357); or reporting f_NL · b_φ only (arXiv:2205.05673).
3. **Fixed or free cosmology in large-scale-structure searches.** D'Amico et al. fix ΛCDM to Planck for the BOSS bispectrum (arXiv:2201.11518); Cabass et al. vary it (arXiv:2201.07238); the DESI feature search shows that fixing it can create a signal (arXiv:2610.10530).
4. **Foreground modelling for r.** Parametric fits per patch (arXiv:2110.00483) against moment expansions and extended parametric models designed for spatially varying dust (arXiv:2508.00073). The debate is how much flexibility can be added before σ(r) degrades beyond the forecast.
5. **Calibrating the polarisation angle.** Galactic foregrounds (arXiv:2011.11254), optics models (arXiv:2509.13654), hardware plus cross-experiment transfer (arXiv:2606.11300). Each fails in a different way, which is the argument for combining them (arXiv:2608.06480).
6. **Δχ² against Bayesian evidence.** Feature models improve the fit and lose on evidence (arXiv:2605.30236, arXiv:2606.28310); the Planck curvature preference had Δχ²_eff = −11 for one parameter (arXiv:1807.06209) [src: Sect. 7.3] and was judged with a tension statistic and betting odds (arXiv:1908.09139).
7. **Templates against reconstruction.** Three bispectrum templates and two oscillation templates do not span model space; modal, binned and learned-basis methods (arXiv:2511.19179) and non-parametric P(k) reconstructions (arXiv:2503.14454, arXiv:2605.18615) trade sensitivity for generality.
8. **Limit construction.** Bayesian with a flat prior on r against Feldman–Cousins (arXiv:2103.13334).

## 11. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

| Question | Data | Expected (all **forecasts** unless marked) | Source |
|---|---|---|---|
| n_s without BAO | SO | σ(n_s) = 0.002 (SO LAT) | arXiv:2512.15833 [src: Sect. 3.2] |
| Binned P_R(k) | SO-like, CMB-HD-like | 0.1% at k = 0.2 Mpc⁻¹ | arXiv:2609.35964 [src: abstract] |
| r | BK24; SO six SATs; LiteBIRD | σ(r) = 1.2 × 10⁻³ (SO); δr < 0.002 (LiteBIRD) | arXiv:2512.15833 [src: abstract], arXiv:2607.25285 [src: abstract] |
| f_NL^local | DESI full survey; SPHEREx; Euclid | Δf_NL < 0.5 (SPHEREx requirement); 2.2 (Euclid) | arXiv:2511.02985 [src: Sect. III.2], arXiv:2507.15819 [src: abstract] |
| f_NL^equil, f_NL^ortho | Euclid P + B | 108, 33 | arXiv:2507.15819 [src: abstract] |
| Ω_K | Euclid alone | 0.0044 (0.003) | arXiv:2507.15819 [src: abstract] |
| β | SO, LiteBIRD | uncertainty reduced by about 7 (arXiv:2507.16714); 0.02° total error (LiteBIRD best pipeline; arXiv:2503.22322 [src: abstract]) | arXiv:2507.16714, arXiv:2503.22322 |
| Features | SO + LiteBIRD; DESI, Euclid | order-of-magnitude gains | arXiv:2605.30236, arXiv:1906.08758 |

Forecasts that cite CMB-S4 (for example the Euclid combinations in arXiv:2507.15819 and the "wishful CMB-Stage 4" of arXiv:2507.16714) describe an experiment that is no longer funded.

## 12. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

1. **"ACT measured n_s = 0.974."** ACT + truncated Planck give 0.9709 ± 0.0038 (arXiv:2503.14452) [src: Sect. VIII.3]; 0.974 needs CMB lensing and DESI BAO in ΛCDM (arXiv:2503.14452) [src: abstract]; the CMB-only three-experiment value is 0.9679 ± 0.0033 (arXiv:2506.20707) [src: Sect. II] (also arXiv:2507.12459).
2. **"Starobinsky inflation is ruled out."** On the 2σ boundary for one data combination in ΛCDM; allowed in extended models, with refined predictions for N⋆ ≳ 58 (arXiv:2504.20757) [src: abstract], and with the CMB-only n_s (arXiv:2607.28445, arXiv:2609.35964).
3. **"The Lyα forest shows a negative running."** eBOSS-era result; superseded by ACT and DESI DR1 (arXiv:2503.14454, arXiv:2601.21432).
4. **"r < 0.032 is a newer measurement than r < 0.036."** Same BK18 B modes with Planck PR4 and BAO added (arXiv:2112.07961) [src: abstract]; BK18 itself gives r < 0.036 (arXiv:2110.00483) [src: abstract]. Likewise r < 0.038 from P-ACT-LB-BK18 (arXiv:2503.14454) [src: Sect. IV.4].
5. **"r < 0.06" or "r < 0.09" as the current limit.** These are Planck 2018 + BK15 (r_0.002 < 0.056, arXiv:1807.06211 [src: abstract]) and BK14 (r_0.05 < 0.090, arXiv:2011.08163 [src: abstract]); superseded since 2021 (arXiv:2110.00483).
6. **"SPT-3G constrains r to 0.0077."** That is r_ect for causal sources (arXiv:2601.20958) [src: abstract]; SPT-3G's inflationary limit is 0.25 (arXiv:2505.02827) [src: abstract].
7. **Citing CMB-S4 targets for r, or the pre-reformation LiteBIRD requirement, as upcoming.** CMB-S4 is not funded (per `cosmo-cmb`); LiteBIRD's requirement after reformation is δr < 0.002 with one telescope and 12 bands (arXiv:2607.25285) [src: abstract]. SO forecasts made for three SATs over five years are superseded by the six-SAT plan (arXiv:2512.15833).
8. **"f_NL^local = 0.8 ± 5.0 is the Planck result."** That is the 2015 preliminary T + E value; the 2018 value is −0.9 ± 5.1 (arXiv:1905.05697) [src: abstract], and PR4 gives −0.1 ± 5.0 (arXiv:2504.00884) [src: abstract].
9. **"DESI measured f_NL = −3.6 ± 9."** It measured f_NL · b_φ; with universality for quasars the same data give +3.5 +10.7/−7.4 (arXiv:2411.17623) [src: abstract] (see also arXiv:2205.05673).
10. **"Large-scale structure now beats the CMB on f_NL (σ = 4.1)."** 4.1 is a CMB + DESI combination from an external reanalysis, conditional on b_φ (arXiv:2512.04266) [src: abstract].
11. **"A detection of f_NL would confirm inflation."** A detection of local f_NL of order one would rule out single-field models, by the consistency relation (arXiv:astro-ph/0407059); it is a discriminator among models, and single-field inflation predicts a value too small to see (arXiv:astro-ph/0210603).
12. **"Planck shows the Universe is closed."** Planck 2018 spectra alone, Plik likelihood; flat with lensing and BAO, and DESI-era fits lean open (arXiv:1807.06209, arXiv:2002.06892, arXiv:2503.14738).
13. **"Negative curvature" for Ω_K < 0.** Ω_K < 0 is positive spatial curvature (closed).
14. **"Cosmic birefringence is detected at 3.6σ / 4.8σ."** The authors of both results decline to claim a detection because of foreground and instrument systematics (arXiv:2205.13962 [src: abstract, 3.6σ], arXiv:2608.06480 [src: abstract, 4.8σ]).
15. **"β = 0.30 ± 0.05" as a 6σ measurement.** The error omits the polarisation-angle systematic (arXiv:2507.16714, abstract).
16. **"BICEP/Keck sees no birefringence."** It self-calibrates on EB and is blind to a constant β (arXiv:2603.06812).
17. **"DESI sees a primordial feature at 3σ."** Only at fixed Planck cosmology; it disappears when the cosmology is varied (arXiv:2610.10530).
18. **"SPHEREx: R = 40 over 0.75–4.1 μm and R = 150 over 4.1–4.8 μm."** Proposal values (arXiv:1412.4872) [src: abstract]; the flown mission has 102 bands over 0.75 to 5.0 μm and was launched on 11 March 2025 (arXiv:2511.02985) [src: abstract].
19. **Quoting an isocurvature limit as "less than a few per cent" without the mode.** Planck gives β_iso(k_low) < 2.5% for CDI and 7.4% for NDI in the generally correlated case (arXiv:1807.06211) [src: Sect. 9.2], and much tighter limits for fully correlated CDI.

## 13. Not verified
<!-- key: not-verified -->

- Whether a BK24 r result has been presented in talks; only arXiv was searched.
- Any Simons Observatory measurement (first B-mode spectra, n_s) announced outside arXiv.
- The CMB-S4 σ(r) target referred to in the list of stale claims was not read at source this session.
- The status of the 2025–2026 papers proposing higher-curvature corrections to Starobinsky inflation and critiques of them: several were identified by title but could not be included within the source cap.
- SPT-3G D1 constraints on running and curvature, and any SPT statement on inflation models.
- The large-angle CMB anomalies and their possible primordial origin: belongs to `cosmo-tensions-anomalies`, not researched here.
- Primordial black holes, scalar-induced gravitational waves and pulsar-timing constraints on the small-scale primordial spectrum: outside the budget.
- CMB spectral distortions as a probe of the primordial spectrum at k ≫ 1 Mpc⁻¹: not researched.
