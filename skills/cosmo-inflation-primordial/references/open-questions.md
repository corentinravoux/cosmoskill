# open-questions — cosmo-inflation-primordial

Snapshot: 2026-10-07

Scope: the live controversies in observational primordial physics with both sides cited, internal tensions between analyses, method debates, what the next data will decide (forecasts labelled), and the misconceptions and stale claims that still circulate, each with the paper that corrects it.

Flags as in the other files. Numbers are repeated here only when the argument needs them; tables are in `results.md`.

## 1. Has n_s moved, and does it exclude Starobinsky-type inflation?
<!-- key: has-ns-moved-and-does-it-exclude-starobinsky -->

**The claim.** ACT DR6 combined with a truncated Planck, CMB lensing and DESI DR1 BAO gives n_s = 0.974 ± 0.003 in ΛCDM, and the Starobinsky R² model then sits on the 2σ boundary for 50–60 e-folds (arXiv:2503.14452, arXiv:2503.14454). The leading-order prediction n_s ≈ 1 − 2/N gives 0.960–0.967 for N = 50–60 [der], which is 2.3 to 4.7σ below 0.974 if the error 0.003 is taken at face value [der: (0.974 − 0.967)/0.003 and (0.974 − 0.960)/0.003]. A literature of "ACT-compatible" models followed: Higgs inflation with vector-like quark stabilisation (McDonald 2025, arXiv:2505.07488), extensions of the α-Starobinsky model (Shobcha et al. 2026, arXiv:2606.24131), polynomial and α-attractor variants reviewed by Kallosh and Linde (arXiv:2505.13646).

**The objections.**

1. The shift is a CMB + BAO effect in a model where CMB and BAO disagree. CMB data have a degeneracy between n_s and the BAO parameters; the DESI–CMB tension in ΛCDM moves n_s along it. Ferreira et al. "urge caution in interpreting CMB+BAO constraints on n_s until the BAO-CMB tension is resolved" (arXiv:2507.12459). The three-experiment CMB-only value is 0.9679 ± 0.0033 (arXiv:2506.20707).
2. The shift depends on the cosmological model. With Ω_K free, n_s = 0.9667 ± 0.0041 (Planck + DESI) or 0.9692 ± 0.0035 (with ACT and SPT); with w0wa free, 0.9716 ± 0.0032; the authors conclude that the tension with Starobinsky, Higgs and the simplest α-attractors "holds only for ΛCDM" (arXiv:2607.28445). With α_s, N_eff and Σm_ν free the error doubles to 0.0064 and both Starobinsky inflation and the Bi-thermal Big Bang model are allowed again, although both are "ruled out at about the 95% confidence level" in six-parameter ΛCDM (arXiv:2609.35964).
3. The prediction itself moves. Beyond the usual analytical approximations, Starobinsky inflation stays within 2σ for N⋆ ≳ 58 (Drees and Xu 2025, arXiv:2504.20757) [src].

**The reheating route and its cost.** A larger N requires a stiff post-inflationary phase. Drees and Xu find that the ACT-era n_s implies an effective reheating equation of state ω ≳ 0.462, which excludes purely perturbative reheating (ω ≈ 0), and T_rh ≲ 2 × 10¹⁰ GeV for ω ≤ 1; agreement within 1σ needs 4 MeV ≲ T_rh ≲ 10 GeV with 0.8 ≲ ω ≤ 1 (arXiv:2504.20757) [src]. Dorsch et al. show that a stiff epoch blue-tilts the primordial gravitational-wave spectrum, that the 1σ region allowed by CMB + BAO is "already excluded" by the BBN bound on extra radiation, and that part of the 2σ region would be detectable by Einstein Telescope, LISA, DECIGO or BBO (**forecast**; arXiv:2606.28502) [src].

**Where it stands.** Three numbers are in use for the same quantity: 0.965 (Planck 2018), 0.968 (CMB-SPA), 0.974 (P-ACT-LB). A statement that a model is excluded is a statement about one of them, in ΛCDM, for an assumed N. What will decide: whether the DESI–CMB distance tension survives the DESI full-survey BAO and the dark-energy debate (`cosmo-dark-energy-modified-gravity`), and the SO and SPT-3G small-scale spectra.

## 2. Running of the spectral index
<!-- key: running-of-the-spectral-index -->

- eBOSS Lyα P1D with Planck gave dn_s/dln k = −0.010 ± 0.004 (arXiv:1911.09073). P-ACT alone excludes that value at more than 3σ, and the DESI DR1 P1D with CMB and BAO gives 0.0014 ± 0.0041 (arXiv:2503.14454, arXiv:2601.21432). The negative running is superseded; the cause on the Lyα side is discussed in `cosmo-lyman-alpha`.
- Planck prefers a slightly negative running, ACT alone a positive one at 1.5σ (0.034 ± 0.022) [der]; combined they give zero within 1.2σ (arXiv:2503.14454).
- The slow-roll expectation, |α_s| of order 10⁻³, is five times below the present error. **Forecasts**: Euclid σ(α_s) = 0.004 (pessimistic) to 0.0015 (optimistic) (arXiv:2507.15819); SO-like and CMB-HD-like surveys tighten the binned spectrum at k = 0.2 Mpc⁻¹ from 0.5% to 0.1% (arXiv:2609.35964). A detection of slow-roll running is therefore not expected from the experiments now funded, unless the optimistic Euclid case is combined with a future CMB data set.

## 3. Tensor modes: how far can r be pushed, and by whom?
<!-- key: tensor-modes-how-far-can-r-be-pushed-and-by-whom -->

- **Current floor.** r < 0.036 from BK18, σ(r) = 0.009 (arXiv:2110.00483). No newer B-mode limit on inflationary r exists at the snapshot (search of 2026-10-09). SPT-3G's independent r < 0.25 confirms the method, not the depth (arXiv:2505.02827).
- **The target.** For Starobinsky-type models r ≈ 12/N² is 0.003–0.005 [der, textbook formula]. Reaching it at 3σ needs σ(r) near 10⁻³.
- **Who gets there (all forecasts).** SO with six SATs to 2035: σ(r) = 1.2 × 10⁻³ for ℓ_knee = 50, moderately complex foregrounds and 70% delensing; 7 × 10⁻⁴ in the optimistic case (arXiv:2512.15833). LiteBIRD after reformation: total δr < 0.002 at 68% (arXiv:2607.25285), weaker than the pre-reformation target. CMB-S4 lost agency support in July 2025 (per `cosmo-cmb`). On these numbers a Starobinsky-level signal would be a 2.8–4σ result for SO in its baseline forecast [der: 0.0033–0.0048 divided by 1.2 × 10⁻³], and 1.7–2.4σ for LiteBIRD alone if δr = 0.002 is read as a 1σ error [der].
- **What limits it.** Dust complexity can bias r by up to 0.03 with a low-order moment expansion in the worst allowed case (arXiv:2508.00073), far above the statistical target, so the forecast is conditional on the foreground model; residual beam leakage in BICEP3 is equivalent to r ≈ 10⁻³ after the improved deprojection (arXiv:2608.25016), comparable to the next-generation σ(r).
- **Would a detection prove inflation?** Komatsu argues that sourced tensor modes from matter fields are an alternative to vacuum fluctuations and that distinguishing them should shape experiment design (arXiv:2202.13919). Causal post-inflationary sources are constrained separately (arXiv:2601.20958).
- **The Lyth bound** ties a detection at the current level to a super-Planckian field excursion (arXiv:hep-ph/9606387); a null result at r of order 10⁻³ would leave small-field models untouched.

## 4. Can large-scale structure overtake the CMB on f_NL?
<!-- key: can-large-scale-structure-overtake-the-cmb-on -->

**For.** DESI DR1 reaches σ(f_NL^local) = 9 from scale-dependent bias (arXiv:2411.17623); an external power spectrum + bispectrum reanalysis of DESI DR1 quotes −0.1 ± 7.4, and −0.0 ± 4.1 combined with the CMB, "the strongest bound on multi-field inflation yet obtained" (arXiv:2512.04266). SPHEREx is designed for Δf_NL < 0.5 (**forecast**, arXiv:2511.02985) and Euclid forecasts 2.2 (**forecast**, arXiv:2507.15819).

**Against.** The measured quantity is f_NL · b_φ. Barreira's position is that "the error bar σ(f_NL) remains undetermined and the results cannot be compared with the CMB" without independent knowledge of b_φ, and that wide b_φ priors bias the result (arXiv:2205.05673). Assembly bias can change b_φ by a large factor and even its sign (arXiv:2209.07251). Every forecast above assumes universality.

**Middle ground.** Priors on p from hydrodynamical simulations for the actual selection: p̄ ≈ 1.4 for DESI quasars gives −3.3 ± 9.2 (arXiv:2602.12357), between the two DESI collaboration values. Multi-tracer and cross-correlation analyses test systematics but share the b_φ dependence (arXiv:2604.05213, arXiv:2512.17865).

**Internal consistency today.** Five DESI DR1 analyses with different statistics give central values between −3.6 and +3.5 with errors of 7 to 12 (arXiv:2411.17623, arXiv:2602.12357, arXiv:2604.05213, arXiv:2606.24651, arXiv:2512.04266). They use the same catalogues and are not independent. eBOSS DR16 analyses hint at unexplained large-scale systematics (arXiv:2309.15814).

**Equilateral and orthogonal shapes.** Large-scale structure is a factor of five (equilateral: 230 against 47) and four (orthogonal: 86 against 24) behind Planck [der, from `results.md` sections 5 and 6.3], and the DESI-only equilateral value 719 ± 390 is 1.8σ from zero [der]. The galaxy bispectrum is prior-dependent (arXiv:2201.07238).

**Beyond templates.** A 2.4σ global excess for a spin-0 cosmological-collider template in Planck (arXiv:2511.17500), no detection for strongly mixed collider models in PR4 (arXiv:2511.19179). Neither is a claim of detection.

**What decides.** DESI full-survey samples (2027), then SPHEREx; for both the limiting issue is b_φ and imaging systematics, not volume.

## 5. Spatial curvature: closed, flat or open?
<!-- key: spatial-curvature-closed-flat-or-open -->

- **Closed (2019–2020).** Planck 2018 spectra alone prefer Ω_K < 0 at more than 99% (arXiv:1807.06209, arXiv:1911.02087), in 2.5–3σ tension with lensing and BAO in the curved model (arXiv:1908.09139). Counter-position: with a different Planck likelihood the spectra are consistent with flatness and CMB + BAO give 0.0004 ± 0.0018 (arXiv:2002.06892). The preference is the A_L feature in another parameter (arXiv:1807.06209); its later history is in `cosmo-cmb`.
- **Open (2025–2026).** DESI DR2 + CMB give Ω_K = +0.0023 ± 0.0011 (arXiv:2503.14738); low-redshift data alone are claimed to prefer an open universe at 2σ to 5σ depending on the supernova sample (arXiv:2512.19565). Counter-position: the preference exists only inside ΛCDM and vanishes when dark energy is allowed to evolve, so it is "an artifact of limited model flexibility" (arXiv:2604.23492); DESI's own w0waCDM + Ω_K fits are consistent with zero (arXiv:2503.14738).
- **Inflationary reading.** Chudaykin et al. take Ω_K ≈ 3 × 10⁻³ as a motivation to revisit open-universe inflation and note that it lowers n_s (arXiv:2607.28445). Efstathiou and Gratton read flatness as support for a long inflation (arXiv:2002.06892).
- **Judgment.** Both the 2019 closed hint and the 2025 open hint appear when two data sets that disagree in ΛCDM are forced into ΛCDM + Ω_K. Neither exceeds about 2σ in a combined fit. **Forecast**: Euclid σ(Ω_K) = 0.0044 (0.003) alone (arXiv:2507.15819), which does not improve on DESI + CMB.

## 6. Cosmic birefringence: a 4.8σ signal nobody claims
<!-- key: cosmic-birefringence-a-4-8sigma-signal-nobody -->

- **For.** Same sign and size in WMAP, Planck PR3, Planck PR4 and ACT DR6; no frequency dependence over 23–353 GHz; a joint ACT + Planck analysis at 0.277° ± 0.057° (arXiv:2205.13962, arXiv:2509.13654, arXiv:2608.06480).
- **Against.** Each analysis rests on an assumption about either the Galactic EB or the instrument angles. β falls with larger masks in Planck PR4 (arXiv:2201.07682); ACT has "systematics … that are not understood" (arXiv:2509.13654); the joint 4.8σ takes the ACT priors at face value and falls to 3.5σ in the dust-robust variant (arXiv:2608.06480).
- **What decides.** Absolute angle calibration at the 0.1° level or better: SO wire grid (0.08° **forecast**, arXiv:2606.11300); LiteBIRD (**forecast** 5–13σ for β = 0.3°, arXiv:2503.22322, for the pre-reformation design). BICEP/Keck cannot test a constant β (arXiv:2603.06812).
- **Interpretation** (axion-like dark energy or dark matter, early dark energy) is reviewed by Komatsu (arXiv:2202.13919) and belongs to `cosmo-dark-energy-modified-gravity` and `cosmo-neutrinos-dark-matter`.

## 7. Primordial features: residual hints
<!-- key: primordial-features-residual-hints -->

Planck spectra contain a few frequencies with Δχ² ≈ −10 to −15, at most 2.6σ globally, weaker with PR4 (arXiv:2605.30236). The combination of Planck, ACT DR6 and DESI DR2 limits oscillation amplitudes to about 2% and the Bayesian evidence prefers no feature (arXiv:2606.28310). DESI DR1 clustering reaches 3% and shows that a fixed-cosmology search converts the DESI–Planck distance mismatch into a 3σ "feature" (arXiv:2610.10530). **Forecasts**: an order of magnitude from SO + LiteBIRD (arXiv:2605.30236) and from DESI and Euclid relative to BOSS (arXiv:1906.08758); Euclid measures an amplitude of 0.01 to about 20% (arXiv:2507.15819). The open method question is how to combine CMB and galaxy searches when their background cosmologies disagree.

## 8. Isocurvature
<!-- key: isocurvature -->

No hint. The open directions are small scales, where ACT improved the blue-tilted CDI limit by more than a factor of two (59 to 26 in units of 10⁻¹⁰ at k = 0.1 Mpc⁻¹; arXiv:2503.14454) and where adding SPT improves the tilt constraint moderately (arXiv:2606.11312), and the dependence of the limits on n_s and on the data combination. **Forecast**: Euclid would tighten blue-tilted isocurvature limits by an order of magnitude (arXiv:2507.15819).

## 9. Internal tensions between analyses
<!-- key: internal-tensions-between-analyses -->

| Quantity | Analysis A | Analysis B | Size | Status |
|---|---|---|---|---|
| n_s in ΛCDM | 0.9649 ± 0.0042, Planck 2018 (arXiv:1807.06211) | 0.974 ± 0.003, P-ACT-LB (arXiv:2503.14452) | 0.009 [der]; no σ can be quoted, Planck data are in both | explained by small-scale data plus the CMB–BAO tension (section 1) |
| n_s, CMB only against CMB + BAO | 0.9679 ± 0.0033, CMB-SPA (arXiv:2506.20707) | 0.974 ± 0.003, P-ACT-LB | 0.006 [der] | BAO pull (arXiv:2507.12459) |
| Running | −0.010 ± 0.004, eBOSS Lyα + Planck (arXiv:1911.09073) | 0.0060 ± 0.0055, P-ACT (arXiv:2503.14454) | more than 3σ, as stated by ACT | resolved against the old value |
| Sign of the running | Planck: slightly negative | ACT alone: 0.034 ± 0.022 | 1.5σ positive [der] | statistical |
| f_NL^local from one DESI DR1 data vector | −3.6 +9.0/−9.1 with p = 1.6 for quasars | +3.5 +10.7/−7.4 with p = 1 (arXiv:2411.17623) | shift of 7, comparable to σ [der] | b_φ, unresolved |
| f_NL^local from eBOSS DR16 quasars | −12 ± 21 (arXiv:2106.13725) | −4 to +27 at 68% (arXiv:2309.15814) | shift of about one σ between analyses of the same quasars [der: centre +11.5 against −12] | weights and systematics treatment |
| f_NL^equil | 719 ± 390, DESI DR1 alone (arXiv:2512.04266) | −26 ± 47, Planck 2018 (arXiv:1905.05697) | 1.9σ [der: 745/393] | bias priors; falls to 200 ± 230 with simulation priors |
| Ω_K | −0.0107 +0.0064/−0.0053, CMB alone | +0.0023 ± 0.0011, DESI DR2 + CMB (arXiv:2503.14738) | sign change | geometric degeneracy; CMB–BAO tension |
| β | 0.215 ± 0.074, ACT DR6 (arXiv:2509.13654) | 0.342 +0.094/−0.091, WMAP + Planck (arXiv:2205.13962) | 1.1σ [der: 0.127/0.118] | consistent |
| Logarithmic feature in DESI DR1 | 3σ global at fixed Planck cosmology | absent with cosmology varied (arXiv:2610.10530) | — | artefact of the distance tension |
| Neutrino-density isocurvature | small peak at non-zero amplitude, Planck alone | gone with ACT DR6 (arXiv:2503.14454) | insignificant | resolved |

No tension exists between B-mode analyses: all current r limits below 0.05 use the BICEP/Keck maps.

## 10. Method debates
<!-- key: method-debates -->

1. **Which n_s goes to model builders.** CMB + BAO in ΛCDM (the tightest; arXiv:2503.14452), CMB only (arXiv:2507.12459), or a posterior marginalised over late-time and neutrino extensions (arXiv:2607.28445, arXiv:2609.35964). The choice changes the verdict on the most-cited models.
2. **Fixing or marginalising b_φ.** Fixed p per tracer (arXiv:2411.17623); narrow Gaussian priors on p (arXiv:2606.24651); simulation priors (arXiv:2602.12357); or reporting f_NL · b_φ only (arXiv:2205.05673).
3. **Fixed or free cosmology in large-scale-structure searches.** D'Amico et al. fix ΛCDM to Planck for the BOSS bispectrum (arXiv:2201.11518); Cabass et al. vary it (arXiv:2201.07238); the DESI feature search shows that fixing it can create a signal (arXiv:2610.10530).
4. **Foreground modelling for r.** Parametric fits per patch (arXiv:2110.00483) against moment expansions and extended parametric models designed for spatially varying dust (arXiv:2508.00073). The debate is how much flexibility can be added before σ(r) degrades beyond the forecast.
5. **Calibrating the polarisation angle.** Galactic foregrounds (arXiv:2011.11254), optics models (arXiv:2509.13654), hardware plus cross-experiment transfer (arXiv:2606.11300). Each fails in a different way, which is the argument for combining them (arXiv:2608.06480).
6. **Δχ² against Bayesian evidence.** Feature models improve the fit and lose on evidence (arXiv:2605.30236, arXiv:2606.28310); the Planck curvature preference had Δχ² = −11 for one parameter (arXiv:1807.06209) and was judged with a tension statistic and betting odds (arXiv:1908.09139).
7. **Templates against reconstruction.** Three bispectrum templates and two oscillation templates do not span model space; modal, binned and learned-basis methods (arXiv:2511.19179) and non-parametric P(k) reconstructions (arXiv:2503.14454, arXiv:2605.18615) trade sensitivity for generality.
8. **Limit construction.** Bayesian with a flat prior on r against Feldman–Cousins (arXiv:2103.13334).

## 11. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

| Question | Data | Expected (all **forecasts** unless marked) | Source |
|---|---|---|---|
| n_s to ±0.002 without BAO | SO, SPT-3G later seasons | not quantified in the sources read | — |
| Binned P_R(k) | SO-like, CMB-HD-like | 0.1% at k = 0.2 Mpc⁻¹ | arXiv:2609.35964 |
| r | BK24; SO six SATs; LiteBIRD | σ(r) = 1.2 × 10⁻³ (SO); δr < 0.002 (LiteBIRD) | arXiv:2512.15833, arXiv:2607.25285 |
| f_NL^local | DESI full survey; SPHEREx; Euclid | Δf_NL < 0.5 (SPHEREx requirement); 2.2 (Euclid) | arXiv:2511.02985, arXiv:2507.15819 |
| f_NL^equil, f_NL^ortho | Euclid P + B | 108, 33 | arXiv:2507.15819 |
| Ω_K | Euclid alone | 0.0044 (0.003) | arXiv:2507.15819 |
| β | SO, LiteBIRD | uncertainty reduced by about 7; 0.02° total error (LiteBIRD best pipeline) | arXiv:2507.16714, arXiv:2503.22322 |
| Features | SO + LiteBIRD; DESI, Euclid | order-of-magnitude gains | arXiv:2605.30236, arXiv:1906.08758 |

Forecasts that cite CMB-S4 (for example the Euclid combinations in arXiv:2507.15819 and the "wishful CMB-Stage 4" of arXiv:2507.16714) describe an experiment that is no longer funded.

## 12. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

1. **"ACT measured n_s = 0.974."** ACT + truncated Planck give 0.9709 ± 0.0038; 0.974 needs CMB lensing and DESI BAO in ΛCDM; the CMB-only three-experiment value is 0.9679 ± 0.0033 (arXiv:2503.14452, arXiv:2506.20707, arXiv:2507.12459).
2. **"Starobinsky inflation is ruled out."** On the 2σ boundary for one data combination in ΛCDM; allowed in extended models, with refined predictions for N⋆ ≳ 58, and with the CMB-only n_s (arXiv:2607.28445, arXiv:2609.35964, arXiv:2504.20757).
3. **"The Lyα forest shows a negative running."** eBOSS-era result; superseded by ACT and DESI DR1 (arXiv:2503.14454, arXiv:2601.21432).
4. **"r < 0.032 is a newer measurement than r < 0.036."** Same BK18 B modes with Planck PR4 and BAO added (arXiv:2112.07961). Likewise r < 0.038 from ACT (arXiv:2503.14454).
5. **"r < 0.06" or "r < 0.09" as the current limit.** These are Planck 2018 + BK15 (r_0.002 < 0.056, arXiv:1807.06211) and BK14 (r_0.05 < 0.090, arXiv:2011.08163); superseded since 2021 (arXiv:2110.00483).
6. **"SPT-3G constrains r to 0.0077."** That is r_ect for causal sources (arXiv:2601.20958); SPT-3G's inflationary limit is 0.25 (arXiv:2505.02827).
7. **Citing CMB-S4 targets for r, or the pre-reformation LiteBIRD requirement, as upcoming.** CMB-S4 is not funded (per `cosmo-cmb`); LiteBIRD's requirement after reformation is δr < 0.002 with one telescope and 12 bands (arXiv:2607.25285). SO forecasts made for three SATs over five years are superseded by the six-SAT plan (arXiv:2512.15833).
8. **"f_NL^local = 0.8 ± 5.0 is the Planck result."** That is the 2015 preliminary T + E value; the 2018 value is −0.9 ± 5.1, and PR4 gives −0.1 ± 5.0 (arXiv:1905.05697, arXiv:2504.00884).
9. **"DESI measured f_NL = −3.6 ± 9."** It measured f_NL · b_φ; with universality for quasars the same data give +3.5 +10.7/−7.4 (arXiv:2411.17623, arXiv:2205.05673).
10. **"Large-scale structure now beats the CMB on f_NL (σ = 4.1)."** 4.1 is a CMB + DESI combination from an external reanalysis, conditional on b_φ (arXiv:2512.04266).
11. **"A detection of f_NL would confirm inflation."** A detection of local f_NL of order one would rule out single-field models, by the consistency relation (arXiv:astro-ph/0407059); it is a discriminator among models, and single-field inflation predicts a value too small to see (arXiv:astro-ph/0210603).
12. **"Planck shows the Universe is closed."** Planck 2018 spectra alone, Plik likelihood; flat with lensing and BAO, and DESI-era fits lean open (arXiv:1807.06209, arXiv:2002.06892, arXiv:2503.14738).
13. **"Negative curvature" for Ω_K < 0.** Ω_K < 0 is positive spatial curvature (closed).
14. **"Cosmic birefringence is detected at 3.6σ / 4.8σ."** The authors of both results decline to claim a detection because of foreground and instrument systematics (arXiv:2205.13962, arXiv:2608.06480).
15. **"β = 0.30 ± 0.05" as a 6σ measurement.** The error omits the polarisation-angle systematic (arXiv:2507.16714).
16. **"BICEP/Keck sees no birefringence."** It self-calibrates on EB and is blind to a constant β (arXiv:2603.06812).
17. **"DESI sees a primordial feature at 3σ."** Only at fixed Planck cosmology; it disappears when the cosmology is varied (arXiv:2610.10530).
18. **"SPHEREx: R = 40 over 0.75–4.1 μm and R = 150 over 4.1–4.8 μm."** Proposal values (arXiv:1412.4872); the flown mission has 102 bands over 0.75–5.0 μm and was launched on 11 March 2025 (arXiv:2511.02985).
19. **Quoting an isocurvature limit as "less than a few per cent" without the mode.** Planck limits range from β_iso < 0.001 (fully correlated CDI) to 7.4% (NDI at k = 0.002 Mpc⁻¹) (arXiv:1807.06211).

## 13. Not verified
<!-- key: not-verified -->

- Whether a BK24 r result has been presented in talks; only arXiv was searched.
- Any Simons Observatory measurement (first B-mode spectra, n_s) announced outside arXiv.
- The pre-reformation LiteBIRD requirement (usually quoted as δr < 0.001) and the CMB-S4 σ(r) target referred to in the list of stale claims were not read at source this session.
- The status of the 2025–2026 papers proposing higher-curvature corrections to Starobinsky inflation and critiques of them: several were identified by title but could not be included within the source cap.
- SPT-3G D1 constraints on running and curvature, and any SPT statement on inflation models.
- The large-angle CMB anomalies and their possible primordial origin: belongs to `cosmo-tensions-anomalies`, not researched here.
- Primordial black holes, scalar-induced gravitational waves and pulsar-timing constraints on the small-scale primordial spectrum: outside the budget.
- CMB spectral distortions as a probe of the primordial spectrum at k ≫ 1 Mpc⁻¹: not researched.
