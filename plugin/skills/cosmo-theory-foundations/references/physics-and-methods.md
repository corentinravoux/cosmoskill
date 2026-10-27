# Theory foundations — definitions and formulae, each with the paper that fixes the convention

Snapshot: 2026-10-15

Formulae are in plain text with the equation number of the cited paper where one was read. Every equation number marked [src: Eq. n] was read in the paper's HTML rendering, where the printed numbering can differ from the journal version. The hub file `observational-cosmology/references/conventions.md` holds the suite-wide notation and is not repeated here.

## 1. FLRW distances
<!-- key: flrw-distances -->

All formulae were read in Hogg 1999, arXiv:astro-ph/9905116; the equation numbers were re-read in its HTML rendering on 2026-10-14 [src: Eqs. 2–30].

| Quantity | Definition as written | Where | Note |
|---|---|---|---|
| Hubble constant | H0 = 100 h km/s/Mpc | "Cosmographic parameters", Eq. 2 | h is "a dimensionless number parameterizing our ignorance" |
| Hubble time | t_H ≡ 1/H0 = 9.78 × 10^9 h⁻¹ yr [src] | Eq. 3 | |
| Hubble distance | D_H ≡ c/H0 = 3000 h⁻¹ Mpc [src] (rounded) | Eq. 4 | today's value; BAO papers write D_H(z) ≡ c/H(z) |
| Density parameters | Ω_M ≡ 8πGρ0/(3H0²); Ω_Λ ≡ Λc²/(3H0²); Ω_M + Ω_Λ + Ω_k = 1 | Eqs. 5–7 | **Ω_k > 0 is the open (sinh) case** |
| Expansion function | E(z) ≡ sqrt[Ω_M(1+z)³ + Ω_k(1+z)² + Ω_Λ]; H(z) = H0 E(z) | Eq. 14 | matter, curvature and Λ only |
| Line-of-sight comoving distance | D_C = D_H ∫₀^z dz'/E(z') | Eq. 15 | "the fundamental distance measure in cosmography" |
| Transverse comoving distance | D_M = D_H Ω_k^(−1/2) sinh[Ω_k^(1/2) D_C/D_H] for Ω_k > 0; D_C for Ω_k = 0; D_H abs(Ω_k)^(−1/2) sin[abs(Ω_k)^(1/2) D_C/D_H] for Ω_k < 0 | Eq. 16 | equals the proper-motion distance |
| Angular diameter distance | D_A = D_M/(1+z) | Eq. 18 | physical, not comoving; Planck's θ_* uses the comoving one (section 2) |
| Luminosity distance | D_L = (1+z) D_M = (1+z)² D_A | Eq. 21 | |
| Comoving volume element | dV_C = D_H (1+z)² D_A² dΩ dz/E(z) | Eq. 28 | |
| Lookback time | t_L = t_H ∫₀^z dz'/[(1+z')E(z')] | Eq. 30 | |
| Peculiar velocity from redshift | v_pec = c (z_obs − z_cos)/(1+z) | Eq. 10 | |

- E(z) as written has no radiation, no massive neutrinos and no w ≠ −1; every r_d or θ_* calculation needs the fuller form (`#the-desi-dr2-form`).
- Hogg warns that Peebles calls D_M the "angular size distance", which is not the angular diameter distance, and that calling D_M a "proper distance" is wrong: it is a proper distance divided by a ratio of scale factors.
- D_L = (1+z) D_M was read in DESI Collaboration 2025 (arXiv:2503.14738, Sect. 1) and in Aubourg et al. 2015 (arXiv:1411.1074, Sect. II.1); the factor (1+z)² between D_A² and D_M² appears in Planck's D_V (section 3.3). Hogg's D_A (Eq. 18) is the physical angular diameter distance: the "D_A" of a CMB paper that calls it comoving (Planck 2013, θ_*) is Hogg's D_M.
- The symbol D_H means c/H0 in Hogg and c/H(z) in every BAO paper. The applied side (BAO tables, Alcock–Paczynski) is in `cosmo-galaxy-clustering`.

## 2. Parameter basis and derived parameters
<!-- key: parameter-basis-and-derived-parameters -->

Definitions of Planck Collaboration 2013, arXiv:1303.5076, Sect. 2 and Table 1 [src]; every equation number in the "Where" column re-read in the HTML rendering on 2026-10-14 [src: Eqs. 1–9], inherited by the later Planck papers and by most large-scale-structure analyses.

| Symbol | Definition as written | Where | Trap |
|---|---|---|---|
| ω_c, ω_b | Ω_c h², Ω_b h² | Sect. 2.1.1 | physical densities, no h ambiguity |
| T_0 | 2.7255 K adopted [src] | Sect. 2.1.1 | |
| N_eff | ρ_ν = N_eff (7/8)(4/11)^(4/3) ρ_γ, N_eff = 3.046 in the baseline [src] | Eq. 1 | 3.044 in DESI (section 3.4) |
| Neutrino mass | "a single massive eigenstate with m_ν = 0.06 eV"; Ω_ν h² ≈ Σm_ν/93.04 eV ≈ 0.0006 [src] | Sect. 2.1.1 | with extra radiation the massive state keeps N_eff = 3.046/3 ≈ 1.015 |
| Primordial spectrum | P_R(k) = A_s (k/k_0)^(n_s − 1 + (1/2)(dn_s/dlnk) ln(k/k_0)), k_0 = 0.05 Mpc⁻¹ [src] | Eq. 2 | pivot in Mpc⁻¹, no h; r_0.002 is quoted at 0.002 Mpc⁻¹ |
| Ω_m | "Matter density (inc. massive neutrinos) today divided by the critical density" | Table 1 | Ω_c + Ω_b does not include ν |
| H0 | derived, in km/s/Mpc, prior [20, 100] | Table 1 | the CMB samples θ, not H0 |
| z_eq | "Redshift of matter-radiation equality (massless neutrinos)" | Table 1 | computed as if neutrinos were massless |
| z_* | optical depth τ(η) ≡ ∫_η0^η τ̇ dη' equals one at z_*, recombination only | Eq. 5 | not the visibility peak |
| Dark-energy equation of state | w(a) ≡ p/ρ = w0 + (1 − a) wa | Eq. 4 | same form as DESI Eq. 9 |
| Tensor spectrum | P_t(k) = A_t (k/k_0)^(n_t) | Eq. 3 | |
| r_s(z) | ∫₀^η(z) dη'/sqrt[3(1+R)], R ≡ 3ρ_b/(4ρ_γ) | Eq. 6 | |
| θ_* | r_s(z_*)/D_A(z_*), D_A the comoving angular diameter distance | Sect. 2.2.2 | |
| θ_MC | "an approximation to θ_* that is used in CosmoMC and is based on fitting formulae given in Hu & Sugiyama (1996)" | Sect. 2.2.2 | a sampling variable, not θ_* |
| z_drag | τ_d(η(z_drag)) = 1, τ_d(η) ≡ ∫ τ̇ dη'/R | Eq. 7 | |
| r_drag | r_s(z_drag), "computed numerically from camb" | Sect. 2.2.2 | the r_d of BAO papers |
| k_D, θ_D | k_D⁻²(η) = −(1/6) ∫₀^η dη' (1/τ̇)[R² + 16(1+R)/15]/(1+R)²; θ_D = π/(k_D D_A) | Eq. 8 | k_D in Mpc⁻¹ |
| σ8 | "the rms fluctuation in total matter (baryons + CDM + massive neutrinos) in 8 h⁻¹ Mpc spheres at z = 0, computed in linear theory" | Sect. 2.2.2 | total matter; DESI uses cb (section 6) |
| σ_R | σ_R² = ∫ (dk/k) P_m(k) [3 j1(kR)/(kR)]², P_m dimensionless | Eq. 9 | top-hat window |
| Ω_m h³ | "a well-determined combination orthogonal to the acoustic scale degeneracy in flat models" | Sect. 2.2.2 | the CMB degeneracy direction in DESI DR2 Sect. 6 |
| Acoustic-scale degeneracy, Planck 2013 values | θ_* = (1.04148 ± 0.00066) × 10⁻²; Ω_m h^3.2 (Ω_b h²)^(−0.54) = 0.695 ± 0.002; Ω_m h³ = 0.0959 ± 0.0006 | Eqs. 10–12 | 2013 data; Eq. 11 carries the ω_b dependence, Eq. 12 is the simpler combination |

- The sampled parameters are ω_b, ω_c, θ_MC, τ, n_s, ln(10^10 A_s); DESI DR2 (arXiv:2503.14738, Sect. 5) and ACT DR6 (arXiv:2503.14452) keep the same six. H0, Ω_m, σ8 are derived, so a "Planck prior on H0" is model-dependent by construction.
- Planck 2018 values that show the size of the distinctions (Planck Collaboration 2018, arXiv:1807.06209, Tables 1 and 2, TT,TE,EE+lowE+lensing) [src]: 100 θ_MC = 1.04092 ± 0.00031 against 100 θ_* = 1.04110 ± 0.00031; r_* = 144.43 ± 0.26 Mpc against r_drag = 147.09 ± 0.26 Mpc; z_* = 1089.92 ± 0.25. The same paper defines S8 ≡ σ8 (Ω_m/0.3)^0.5.
- Ω_m, σ8 and S8 from a CMB chain are total-matter quantities with one 0.06 eV state (arXiv:1807.06209, Sect. 2.1). An analysis that varies Σm_ν or defines the amplitude on the CDM+baryon field is not quoting the same parameter (`#massive-neutrinos`).

## 3. Sound horizon: r_s, r_d, z_*, z_d and fitting formulae
<!-- key: sound-horizon-rs-rd-z-zd-and-fitting-formulae -->

### 3.1 Two sound horizons, two epochs
<!-- key: two-sound-horizons-two-epochs -->

- The CMB acoustic scale uses r_* = r_s(z_*), with θ_* = r_*/D_A(z_*) (arXiv:1303.5076, Sect. 2.2.2). BAO use r_d ≡ r_s(z_drag): "Baryon velocities decouple from the photon dipole when Compton drag balances the gravitational force, which happens at τ_d ~ 1" (same section).
- Eisenstein & Hu 1998 note that for Ω_b h² ≲ 0.03 the drag epoch "follows last scattering of the photons", so "the sound and Silk scales in the transfer function are larger than those in the CMB" (arXiv:astro-ph/9709112, Sect. 2.1). Hence r_d > r_*: 147.09 ± 0.26 against 144.43 ± 0.26 Mpc in Planck 2018 (arXiv:1807.06209, Table 2). Converting a BAO measurement with r_* instead of r_drag mixes the two rulers.
- The drag redshift is quoted as z_d ≈ 1060 by DESI DR2 (arXiv:2503.14738, Sect. 1) and as "around a redshift z = 1020" by eBOSS (eBOSS Collaboration 2021, arXiv:2007.08991, Sect. 2) [src for both]; neither paper comments on the other value. They are two definitions, not two cosmologies: `deep/sound-horizon.md#step-3-read-1020-and-1060-as-two-definitions`. DESI quotes z_* ≈ 1089.

### 3.2 r_d as BAO analyses define it
<!-- key: rd-as-bao-analyses-define-it -->

From Aubourg et al. 2015, arXiv:1411.1074, Sect. II.2, equation numbers re-read 2026-10-14 [src]:

- r_d = ∫_{z_d}^∞ c_s(z)/H(z) dz [src: Eq. 10], with c_s(z) = 3^(−1/2) c [1 + (3/4) ρ_b(z)/ρ_γ(z)]^(−1/2). eBOSS (Eq. 13) and DESI DR2 (Eq. 1) write the same integral.
- "There are different conventions in use for defining r_d, which differ at the 1-2% level, but ratios of r_d for different cosmologies are independent of the convention provided one is consistent throughout." The paper adopts "the CAMB convention".
- Calibrated approximation (arXiv:1411.1074): r_d ≈ 55.154 exp[−72.3 (ω_ν + 0.0006)²] / (ω_cb^0.25351 ω_b^0.12807) Mpc [src: Eq. 16], "accurate to 0.021%" for N_eff = 3.046, Σm_ν < 0.6 eV and ω_b, ω_cb within 3σ of Planck; it "supersedes a somewhat less accurate (but still sufficiently accurate) approximation" of an earlier paper (its eq. 55) [src: Sect. II.2].
- With free relativistic species (arXiv:1411.1074): r_d ≈ 56.067 exp[−49.7 (ω_ν + 0.002)²] / {ω_cb^0.2436 ω_b^0.128876 [1 + (N_eff − 3.046)/30.60]} Mpc [src: Eq. 17], "accurate to 0.119%" for 0 < Σm_ν < 0.6 eV and 3 < N_eff < 5 [src]. The CMB constrains ω_cb, not ω_cb + ω_ν, "because neutrinos remain relativistic at recombination" [src: Sect. II.2].
- ω_ν = 0.0107 (Σm_ν/1.0 eV) [src: arXiv:1411.1074, Sect. II.2]; the paper's default, 0.06 eV in one massive state, gives ω_ν = 6.45 × 10⁻⁴ [src: arXiv:1411.1074, Sect. II.1].

Aubourg et al. do not name the conventions behind the 1–2% [src: Sect. II.2]; the documented case is the Eisenstein–Hu fitting formula against the Boltzmann value. Planck 2013 (arXiv:1303.5076, Sect. 5.2) records that the BAO groups of the time "use the approximate formulae of Eisenstein & Hu (1998) to compute z_drag and r_s(z_drag), though they fit power spectra computed with Boltzmann codes", and that "in CosmoMC we multiply the accurate numerical value of r_s(z_drag) by a constant factor of 1.0275 to match the Eisenstein-Hu approximation in the fiducial model" [src]. The BAO values used in that paper (6dFGS, SDSS DR7, WiggleZ, BOSS DR9) therefore carry an r_s larger than the Boltzmann one by that factor.

### 3.3 The BAO distance combinations
<!-- key: the-bao-distance-combinations -->

From arXiv:1411.1074, every number in the Eq. column re-read in the rendering [src: Eqs. 5–15]:

| Quantity | Definition | Eq. |
|---|---|---|
| D_C(z) | (c/H0) ∫₀^z dz' H0/H(z') | 6 |
| D_M, small curvature | ≈ D_C(z)[1 + (1/6) Ω_k (D_C/(c/H0))²] | 5 |
| D_M(z) | (c/H0) S_k(D_C/(c/H0)); S_k(x) = sin(sqrt(−Ω_k) x)/sqrt(−Ω_k) for Ω_k < 0, sinh(sqrt(Ω_k) x)/sqrt(Ω_k) for Ω_k > 0, x for Ω_k = 0 | 5, 7 |
| D_H(z) | c/H(z) | 12 |
| D_V(z) | [z D_H(z) D_M²(z)]^(1/3) | 14 |
| α_⊥, α_∥ | D_M/r_d = α_⊥ D_M,fid/r_d,fid; D_H/r_d = α_∥ D_H,fid/r_d,fid | 11, 13 |
| α (isotropic) | D_V/r_d = α D_V,fid/r_d,fid | 15 |

- The paper warns that "some of the referenced papers quote values of D_A/r_d rather than D_M/r_d, differing by a factor (1+z)". Older work quotes the inverse ratio: Planck 2013 writes d_z = r_s(z_drag)/D_V(z) with D_V(z) = [(1+z)² D_A²(z) cz/H(z)]^(1/3) (arXiv:1303.5076) [src: Eqs. 50–51], the same D_V with the physical D_A; WiggleZ used A(z) = D_V(z) sqrt(Ω_m H0²)/(cz) [src: Eq. 54].
- The effective redshift of a BAO point "can be treated as exact" because the measurement is a ratio to the fiducial model (arXiv:1411.1074).
- The Friedmann equation used with these distances includes radiation and neutrinos (arXiv:1411.1074, Eq. 8), with T_ν = T_CMB (4/11)^(1/3) g_c, g_c = (3.046/3)^(1/4), and Ω_m at z = 0 includes the neutrinos, "so that Ω_m + Ω_de + Ω_k ≡ 1".

### 3.4 The DESI DR2 form
<!-- key: the-desi-dr2-form -->

DESI Collaboration 2025, arXiv:2503.14738, Sect. 1, 3.1 and 6; every equation number below re-read in the rendering on 2026-10-14 [src]:

- Eq. 2: r_d = 147.05 Mpc × (ω_b/0.02236)^(−0.13) (ω_bc/0.1432)^(−0.23) (N_eff/3.04)^(−0.1), "scaled to the best-fit values from Planck" and to "three neutrino species that are fully relativistic at z > z_d"; ω_bc ≡ (Ω_b + Ω_cdm) h² [src: Eq. 2]. With CMB ω_b and ω_bc it gives "a 0.2% determination of r_d" for N_eff = 3.04 [src: Sect. 1]; Eq. 1 is the integral r_d = ∫_{z_d}^∞ c_s(z)/H(z) dz [src: Eq. 1]. DESI cites it to a reference list entry; the same power law is Eq. 4 of Brieden, Gil-Marín & Verde 2023 (arXiv:2212.04522), written there with Ω_m h² in place of ω_bc and attributed to "eq. 2.4" of Schöneberg et al. 2022 [src: Sect. 3.1]. In the HTML rendering of Schöneberg et al. 2022 (arXiv:2209.14330, Sect. 2.1.1) the numerical scaling reads H0 r_s ∝ Ω_m^(−0.23) h^(+0.52) N_eff^(−0.1) (Ω_b h²)^(−0.11) [src: Eq. 4], from numerical calculations near the Planck best fit; its footnote obtains Ω_m^(−0.23) h^(0.54) (Ω_b h²)^(−0.13) by power-law expansion of an analytic sound-horizon formula, "within the accuracy of the numerical formula" [src: Sect. 2.1.1, footnote 3]. Neither paper states the accuracy against a Boltzmann code in the passages read.
- DESI's power law has the exponents of the footnote version of Schöneberg et al., once Ω_m and h are combined into the physical density [der].
- D_M(z) = [c/(H0 sqrt(Ω_K))] sinh[sqrt(Ω_K) ∫₀^z dz' H0/H(z')] [src: Eq. 3], its flat limit [src: Eq. 4]; D_H(z) = c/H(z) [src: Eq. 5]; D_V(z) ≡ [z D_M(z)² D_H(z)]^(1/3), unnumbered [src: Sect. 3.1]; D_L(z) = (1+z) D_M(z) [src: Sect. 1].
- H(z)/H0 (arXiv:2503.14738) = [Ω_bc(1+z)³ + Ω_γ(1+z)⁴ + Ω_K(1+z)² + Ω_ν ρ_ν(z)/ρ_ν,0 + Ω_DE ρ_DE(z)/ρ_DE,0]^(1/2); Ω_m "includes neutrinos when they are non-relativistic"; the neutrino density turns from (1+z)³ to (1+z)⁴ at (1+z) ~ m_ν/(5 × 10⁻⁴ eV) [src: Eq. 6]. Ω_ν h² = Σm_ν/(93.14 eV) [src: Eq. 7].
- ρ_DE(z)/ρ_DE,0 = exp{3 ∫₀^z [1 + w(z')] dz'/(1+z')} [src: Eq. 8]; w(a) = w0 + wa(1 − a) [src: Eq. 9]; ρ_DE(a)/ρ_DE,0 = a^(−3(1+w0+wa)) e^(−3wa(1−a)) [src: Eq. 10].
- α_∥ = D_H(z) r_d^fid/[D_H^fid(z) r_d], α_⊥ = D_M(z) r_d^fid/[D_M^fid(z) r_d] [src: Eq. 11]; α_iso = (α_∥ α_⊥²)^(1/3), α_AP = α_∥/α_⊥ [src: Eq. 12], the sampled basis because "less correlated".
- A BAO-only fit (arXiv:2503.14738) samples Ω_m and h r_d and gives Ω_m = 0.2975 ± 0.0086, h r_d = (101.54 ± 0.73) Mpc [src: Eq. 17], correlation −0.92 [src]. The CMB prior DESI uses is 100θ_* = 1.04110 ± 0.00053 [src: Eq. 16], wider than Planck's own ± 0.00031 on the same quantity (arXiv:1807.06209) [src: Sect. 3 tables]; the BBN prior is ω_b = 0.02218 ± 0.00055 [src: Eq. 14]. BAO alone give no H0: "an uncalibrated ruler" (Sect. 4.1).

Three points to hold. (i) The matter variable of Eq. 2 is ω_bc, not ω_m. (ii) The formula assumes "standard pre-recombination physics", and the DESI + BBN H0 inherits that. (iii) The pivot of Eq. 2 is N_eff = 3.04 while the standard value used in Sect. IV.1 is 3.044 (arXiv:2503.14738, Sects. I and IV.1). The CMB counterpart is θ_*, measured to a "fractional error ~10⁻⁴" [src: Sect. I]. Inverse-distance-ladder uses are in `cosmo-distance-ladder-h0`.

## 4. Linear growth and its approximations
<!-- key: linear-growth-and-its-approximations -->

All equations from Linder 2005, arXiv:astro-ph/0507263; equation numbers re-read in the HTML rendering on 2026-10-14 [src: Eqs. 7–18].

- Growth equation in general relativity, every other component smooth: δ̈ + 2H δ̇ − 4πG ρ_m δ = 0 [src: Eq. 7]. With g ≡ δ/a and primes for d/d ln a [src: Eq. 11]: g'' + [5/2 − (1/2)(ln Ω_m(a))'] g' + [3/2 − (1/2)(ln Ω_m(a))' − (3/2) G Ω_m(a)] g = 0; an equivalent form (Eq. 10) is g'' + [5/2 − (3/2) w(a) Ω_w(a)] g' + (3/2)[1 − w(a)] G Ω_w(a) g = 0, G in units of Newton's constant.
- "Within general relativity the linear theory growth factor depends purely on the expansion history": this is what makes growth a test of gravity. It holds for smooth dark energy and scale-independent growth; massive neutrinos break it (`#massive-neutrinos`).
- Growth index: g(a) = exp{∫₀^a d ln a [Ω_m(a)^γ − 1]} [src: Eq. 16], Ω_m(a) = Ω_m a⁻³/(H/H0)²; hence f ≡ d ln δ/d ln a = Ω_m(a)^γ [der: f = 1 + d ln g/d ln a].
- γ = 0.55 + 0.05[1 + w(z=1)] [src: Eq. 17]; for w < −1, γ = 0.55 + 0.02[1 + w(z=1)] [src: Eq. 18]. Linder states that the formula's "primary purpose is not a fit as such (the exact solution requires only solving a second order differential equation)" but physical intuition and a parametrisation of modified growth [src: Sect. V.1]. So 0.55 is the ΛCDM value, not a constant of general relativity. γ is "the growth index, encompassing deviations in the theoretical framework"; Linder & Cahn 2007 (arXiv:astro-ph/0701317) show it is "restricted to a very narrow range" for dark energy in general relativity and extend it to DGP, scalar–tensor and time-varying gravity.

Three things the formula is not. (i) It uses Ω_m(a) at the epoch considered, not Ω_m today. (ii) It assumes scale-independent growth. (iii) It is not the older f ≈ Ω^0.6 of the pre-2000 literature (β ≈ Ω_0^0.6/b in Hamilton 1998, arXiv:astro-ph/9708102; Peacock & Dodds 1994, arXiv:astro-ph/9311057; Fisher 1995, arXiv:astro-ph/9412081): "Using Ω_m^0.6 introduces a needless 6% error in β" for the concordance model (Linder & Cahn 2007, arXiv:astro-ph/0701317, Sect. III) [src].

The symbol γ has a second meaning. Linder cites Wang & Steinhardt 1998 (arXiv:astro-ph/9804015) among the earlier fixed-index growth formulae; the abstract of that paper uses γ for the exponent of the cluster-abundance degeneracy, σ8 Ω_m^γ = 0.5 ± 0.1 [src], the same kind of exponent as in S8.

How analyses define fσ8 [src]:

- Planck 2018 (arXiv:1807.06209, Eq. 27): fσ8 ≡ [σ8^(vd)(z)]²/σ8^(dd)(z), "where σ8^(vd) is the density-velocity correlation in spheres of radius 8 h⁻¹ Mpc in linear theory"; "for ΛCDM, d ln D/d ln a ≈ Ω_m^0.55(z)". This stays defined when growth is scale-dependent; a product f × σ8 does not.
- eBOSS (arXiv:2007.08991, Eq. 19): f = ∂ ln σ8/∂ ln a, and fσ8 "characterizes the amplitude of the velocity power spectrum".
- The Alcock–Paczynski parameter that travels with fσ8 in BOSS-era results is F_AP(z) = D_M(z) H(z)/c (arXiv:1807.06209, Eq. 28).

Measured γ and μ–Σ are in `cosmo-dark-energy-modified-gravity`; β = f/b and the velocity uses in `cosmo-peculiar-velocities`.

## 5. Transfer functions
<!-- key: transfer-functions -->

Definition (Eisenstein & Hu 1998, arXiv:astro-ph/9709112) [src: Eq. 1]: T(k) ≡ [δ(k, z=0)/δ(k, z=∞)] × [δ(0, z=∞)/δ(0, z=0)], synchronous or comoving gauge, so that T → 1 as k → 0; the power spectrum is the initial spectrum times T². Scales that shape T(k), same paper, every number in the Eq. column re-read in the HTML rendering on 2026-10-14 [src: Eqs. 2–7, 25, 26, 29], Ω_0 the total matter density and Θ_2.7 the CMB temperature in units of 2.7 K:

| Scale | Fitting formula as written | Eq. |
|---|---|---|
| Equality redshift | z_eq = 2.50 × 10^4 Ω_0 h² Θ_2.7^(−4) | 2 |
| Equality wavenumber | k_eq ≡ (2 Ω_0 H0² z_eq)^(1/2) = 7.46 × 10⁻² Ω_0 h² Θ_2.7^(−2) Mpc⁻¹ | 3 |
| Drag epoch | z_d = 1291 (Ω_0 h²)^0.251/[1 + 0.659 (Ω_0 h²)^0.828] × [1 + b1 (Ω_b h²)^b2], b1 = 0.313 (Ω_0 h²)^(−0.419) [1 + 0.607 (Ω_0 h²)^0.674], b2 = 0.238 (Ω_0 h²)^0.223 | 4 |
| Baryon-to-photon momentum ratio | R ≡ 3ρ_b/(4ρ_γ) = 31.5 Ω_b h² Θ_2.7^(−4) (z/10³)⁻¹ | 5 |
| Sound horizon at the drag epoch | s = ∫₀^t(z_d) c_s (1+z) dt = [2/(3 k_eq)] sqrt(6/R_eq) ln{[sqrt(1+R_d) + sqrt(R_d+R_eq)]/[1 + sqrt(R_eq)]}, c_s = 1/sqrt[3(1+R)] | 6 |
| Silk damping | k_Silk = 1.6 (Ω_b h²)^0.52 (Ω_0 h²)^0.73 [1 + (10.4 Ω_0 h²)^(−0.95)] Mpc⁻¹ | 7 |
| First acoustic peak | k_peak = [5π/(2s)] (1 + 0.217 Ω_0 h²) | 25 |
| Sound horizon, short form | s = 44.5 ln(9.83/Ω_0 h²)/sqrt[1 + 10 (Ω_b h²)^(3/4)] Mpc, "∼2%" for Ω_b h² ≳ 0.0125 and 0.025 ≲ Ω_0 h² ≲ 0.5 | 26 |
| CDM + baryon split | T(k) = (Ω_b/Ω_0) T_b(k) + (Ω_c/Ω_0) T_c(k) | 8, 16 |
| Zero-baryon shape | T_0(q) = L_0/(L_0 + C_0 q²), L_0 = ln(2e + 1.8 q), C_0 = 14.2 + 731/(1 + 62.5 q) | 29 |

- These lengths are in Mpc, not h⁻¹Mpc: the physics depends on Ω_0 h² and Ω_b h². z_d was "reduced by a factor of 0.96" from the Hu & Sugiyama 1996 value "on phenomenological grounds", and k_Silk carries a "±20% phenomenological correction" (arXiv:astro-ph/9709112, Sect. 2.1): fits to 1990s recombination codes. A modern analysis takes z_d and r_d from a Boltzmann code (`#sound-horizon-rs-rd-z-zd-and-fitting-formulae`).
- Above the sound horizon the shape follows Γ_0 ≡ Ω_0 h; below it baryons suppress power and "the transition around the sound horizon cannot be fit by a single Γ" (Sect. 4.2). The Γ-era phenomenology (Peacock & Dodds 1994; Feldman, Kaiser & Peacock 1994, arXiv:astro-ph/9304022, both fitting Ωh) is why old "shape parameter" values cannot be read as Ω_m h. Eq. 29 agrees with numerical calculations "to 1% through the CMB and large-scale structure regimes"; of its coefficients 1.8 and 14.2 are "derived theoretically" and 731 is fitted [src: Sect. 4.2]. It replaces the BBKS formula, which the paper says "fits neither the exact small-scale solution" nor has the quadratic small-k behaviour that causality requires.
- Massive neutrinos: Eisenstein & Hu 1999 (arXiv:astro-ph/9710252), a function of k, time and six parameters including the massive-neutrino density and the number of degenerate species.
- The modern descendant of Γ is the ShapeFit slope m, defined at k_p = π/r_d^fid ≃ 0.03 h^fid Mpc⁻¹, "approximately at the matter-radiation equality scale" (arXiv:2411.12021, Sect. 4.2.3; `surveys-and-data.md` section 5).
- Boltzmann codes: CAMB (Lewis, Challinor & Lasenby 2000, arXiv:astro-ph/9911177) and CLASS (Blas, Lesgourgues & Tram 2011, arXiv:1104.2933, whose three approximation schemes are tight coupling, an ultra-relativistic fluid approximation and a radiation-streaming approximation); DES Y3 found them "in excellent agreement at the level of accuracy of this analysis" (arXiv:2105.13548). Accuracy figures are in `results.md` section 4.

## 6. σ8, σ12 and the R = 8 h⁻¹Mpc definition
<!-- key: sigma8-sigma12-and-the-r-8-h-1mpc-definition -->

**Definition.** σ_R² = ∫ (dk/k) P_m(k) [3 j1(kR)/(kR)]² with R = 8 h⁻¹Mpc, linear theory, z = 0, total matter (arXiv:1303.5076, Eq. 9) [src]. Four choices are packed in the symbol: the radius and its unit, linear versus non-linear, the redshift, and the matter field. On the last one the two largest current data sets differ: Planck uses total matter; DESI DR1 full shape states "we refer as σ8 to the amplitude of matter fluctuations excluding neutrinos" (arXiv:2411.12021, footnote 3) [src].

**The h problem** (Sánchez 2020, arXiv:2002.07829) [src]:

- "When h varies, σ8 changes due to two effects: i) the change in the amplitude of P(k) itself, and ii) the change in the reference scale R = 8 h⁻¹ Mpc, which corresponds to a different scale in Mpc for different values of h." A posterior on σ8 is an average over the scales allowed by the posterior on h: σ8 = ∫ σ(R = (8/h) Mpc | h) P(h) dh [src: Eq. 6].
- Proposal: σ12, "the rms linear theory variance at R = 12 Mpc", whose value "is similar to the standard σ8 for h ∼ 0.67" (arXiv:2002.07829, abstract). Models with the same ω_b, ω_c, ω_ν, n_s and σ12 have identical linear P(k) in Mpc units whatever h, and their halofit spectra agree to "a few percent at high k" [src: Sect. III]. Companion lensing parameter: S12 = σ12 (ω_m/0.14)^0.4 [src: Sect. IV].
- RSD: P_g(k, μ, z) = [bσ8(z) + fσ8(z) μ²]² P(k, z)/σ8²(z) [src: Eq. 7]. Quoting fσ8 needs P/σ8² to depend on shape only (the argument of Percival & White 2009, arXiv:0808.0003, whose abstract says the anisotropy "provides a constraint on the derivative of the linear growth rate through f.sigma_8"); but that ratio depends on h, while P/σ12² does not. Hence "fσ12 is the most relevant quantity to describe RSD".
- What does not change: "Using h⁻¹ Mpc units or simply Mpc would lead to identical parameter constraints" if h is carried through the Alcock–Paczynski factors q_∥ = H'(z_m)/H(z_m), q_⊥ = D_M(z_m)/D'_M(z_m), primes fiducial, which rescale s_∥ = q_∥ s'_∥ and s_⊥ = q_⊥ s'_⊥ [src: Eqs. 2–5]. The illustrative spectra of the paper vary h at fixed ω_b, ω_c, ω_ν, A_s, n_s, computed with CAMB [src: Sect. III].

**What DESI does.** ShapeFit quotes fσ_s8, with σ_s8 tied to r_d^fid rather than to h; the definition is in `surveys-and-data.md` section 5. **Units.** Croton 2013 (arXiv:1308.4150) is the general reference on h in observed and simulated quantities; its abstract calls little h "an anachronism" and gives nine rules. Numbers are in `results.md` section 3; the community choice in `open-questions.md` section 1.

## 7. Fourier and multipole conventions
<!-- key: fourier-and-multipole-conventions -->

The reference that writes out the whole chain is Hamilton 1998, arXiv:astro-ph/9708102; Eqs. 3.3, 3.5 and 5.10 re-read in the HTML rendering on 2026-10-14, Eqs. 5.5 and 5.9 (Sect. 5.2) on 2026-10-15 [src: Eqs. 3.3, 3.5, 5.5, 5.9, 5.10]:

| Object | Convention | Eq. |
|---|---|---|
| Fourier transform | δ̂(k) ≡ ∫ e^(i k·r) δ(r) d³r; δ(r) = ∫ e^(−i k·r) δ̂(k) d³k/(2π)³ | 3.3 |
| Power spectrum | ⟨δ̂(k1) δ̂*(k2)⟩ = (2π)³ δ_D(k1 − k2) P(k1) (footnote; the main text uses δ_D(k1 + k2)) | 3.5 |
| Multipoles of P | P^s(k) = Σ_{ℓ even} L_ℓ(μ_k) P^s_ℓ(k); P^s_ℓ(k) ≡ (2ℓ+1) ∫ L_ℓ(μ_k) P^s(k) do_k/(4π), μ_k the cosine between k and the line of sight | 5.5 |
| Multipoles of ξ | ξ^s_ℓ(r) ≡ (2ℓ+1) ∫ L_ℓ(μ_r) ξ^s(r) do_r/(4π) | 5.9 |
| Hankel pair | P^s_ℓ(k) = i^ℓ 4π ∫₀^∞ j_ℓ(kr) ξ^s_ℓ(r) r² dr; ξ^s_ℓ(r) = i^(−ℓ) 4π ∫₀^∞ j_ℓ(kr) P^s_ℓ(k) k² dk/(2π)³ | 5.10 |

- The same normalisation in μ: P_ℓ(k) ≡ [(2ℓ+1)/2] ∫₋₁¹ dμ P(k, μ) L_ℓ(μ), as written by Ivanov, Simonović & Zaldarriaga 2020 (arXiv:1909.05277) [src: Eq. 3.2], who also state ⟨δ_k δ_k'⟩ = (2π)³ P(k) δ_D(k + k'). A code that omits the (2ℓ+1) is not equivalent.
- The factor i^ℓ gives the quadrupole of ξ the opposite sign to that of P: "the large scale squashing effect of the redshift correlation function, a negative quadrupole, corresponds to a stretching of the redshift power spectrum along the line of sight, a positive quadrupole".
- "The odd harmonics vanish by pair exchange symmetry" in the plane-parallel limit only (`#relativistic-and-wide-angle-terms`).
- Dimensionless spectrum: Δ²(k) = 4π (k/2π)³ P(k) (Asgari, Mead & Heymans 2023, arXiv:2303.08752) [src: Eq. 9], i.e. k³P/(2π²); a unitary convention with (2π)^(−3/2) on both transforms changes P by (2π)³ [der].
- The Fourier sign differs between papers: LoVerde & Afshordi 2008 use A(k) = ∫ d³x e^(−i k·x) A(x) (arXiv:0809.5112, Eq. 2), the opposite of Hamilton. Power spectra are unaffected; phases of cross-correlations with odd fields (velocity, dipoles) are not.

**Estimators** (equations as DESI uses them are in `cosmo-galaxy-clustering`). Weights: Feldman, Kaiser & Peacock 1994. Multipoles with a varying line of sight: Yamamoto et al. 2006 (arXiv:astro-ph/0505115). FFT implementations, which approximate "the LOS to each pair of galaxies by the LOS to one of them": Bianchi et al. 2015 (arXiv:1505.05341), Scoccimarro 2015 (arXiv:1506.02729), and Hand et al. 2017 (arXiv:1704.02357; 2ℓ+1 FFTs per multipole). Window convolution through the Hankel pair: Wilson et al. 2017 (arXiv:1511.07799); with wide-angle terms: Beutler, Castorina & Zhang 2019 (arXiv:1810.05051).

## 8. Redshift-space distortions: Kaiser, fingers of God, streaming models
<!-- key: redshift-space-distortions-kaiser-fingers-of -->

### 8.1 Linear theory (Kaiser)
<!-- key: linear-theory-kaiser -->

From Hamilton 1998, arXiv:astro-ph/9708102 [src], plane-parallel limit:

- δ̂^s(k) = (1 + β μ_k²) δ̂(k) (Eq. 4.35) and P^s(k) = (1 + β μ_k²)² P(k) (Eq. 4.36), "an elegant formula first pointed out by Kaiser (1987, eq. [3.5])" (Kaiser 1987, doi:10.1093/mnras/227.1.1 [sec: via Hamilton]). β is the growth rate over the linear bias; P(k) is the real-space spectrum of the tracer. In today's notation, P_g(k, μ) = (b1 + f μ²)² P_lin(k) (arXiv:1909.05277, Sect. 3.1).
- Multipoles (arXiv:astro-ph/9708102): P^s_0 = (1 + (2/3)β + (1/5)β²) P; P^s_2 = ((4/3)β + (4/7)β²) P; P^s_4 = (8/35)β² P [src: Eq. 5.7]. The monopole boost P^s/P = 1 + (2/3)β + (1/5)β² [src: Eq. 5.1]; the ratio P^s_2/P^s_0 = [(4/3)β + (4/7)β²]/[1 + (2/3)β + (1/5)β²] [src: Eq. 5.8] is the classic β estimator, and in configuration space the same ratio is ξ^s_2/(ξ^s_0 − ξ̄^s_0), with ξ̄ the volume-averaged monopole [src: Eq. 8.1]; the hexadecapole is "≲ 0.1 of the monopole and quadrupole harmonics for β ≤ 1".
- The general radial operator is S = 1 + β (∂²/∂r² + α(r) ∂/(r ∂r)) ∇⁻² with α(r) ≡ ∂ ln[r² n̄(r)]/∂ ln r [src: Eq. 4.24; Eq. 4.23 not re-located]: the α term depends on the selection function, is absent from the plane-parallel formula, and holds in the CMB rest frame.
- Percival & White 2009 recast the anisotropy as a measurement of fσ8 "independent of galaxy bias", and note that RSD "probe non-relativistic velocities and therefore the temporal metric perturbations, while weak lensing tests the sum of the temporal and spatial metric perturbations" [src, abstract], the basis of the μ–Σ split.

### 8.2 Fingers of God: dispersion models
<!-- key: fingers-of-god-dispersion-models -->

Hamilton describes the standard model as "the result of convolving the linear redshift correlation function ξ^s_L with the line-of-sight component of a random isotropic pairwise velocity distribution f(v)" (Eq. 7.1), in Fourier space P^s(k) = f̂(kμ_k)(1 + β μ_k²)² P(k) (Eq. 7.2) (arXiv:astro-ph/9708102) [src]:

| Pairwise velocity distribution | Damping factor | Eq. |
|---|---|---|
| Gaussian, f(v) = [(2π)^(1/2) σ]⁻¹ exp[−(v/σ)²/2] | exp[−(σ k μ)²/2] [src: Eq. 7.3] | 7.3 |
| Exponential, f(v) = (2^(1/2) σ)⁻¹ exp(−2^(1/2) abs(v)/σ) | 1/[1 + (1/2)(σ k μ)²] [src: Eq. 7.4] | 7.4 |

- This σ is a one-dimensional pairwise dispersion, "2^(1/2) larger than a random 1-dimensional single-point (galaxy) dispersion, and 3^(1/2) smaller than a 3-dimensional pairwise dispersion" [src]. A model written with the single-galaxy σ_1 has exp[−(σ_1 k μ)²] with no factor 1/2 [der]. In products with k the dispersion is a length (velocity over the Hubble rate). Check which σ a paper fits before comparing values.
- Hamilton calls the approach "phenomenological rather than based on any rigorous theory". Scoccimarro 2004 (arXiv:astro-ph/0407214) shows the pairwise velocity distribution "is strongly non-Gaussian at all scales" and that the usual ansatz "gives rise to an unphysical distribution of pairwise velocities" [src, abstract]. Chen & Aviles 2026 (arXiv:2609.35757) find that such damping functions are "the mean-field limit of the single-particle characteristic function" of small-scale velocities and that the environmental dependence "generates equally large corrections that break the simple damping form"; a rigorous resummation is possible only "at the cost of significantly expanding the operator basis and promoting free coefficients to free functions" [src, abstract].
- In the EFT the same physics is a counterterm (section 9). The velocity-survey analogue, the sinc damping D_u with σ_u, is in `cosmo-peculiar-velocities`.

### 8.3 Beyond Kaiser times damping
<!-- key: beyond-kaiser-times-damping -->

- Scoccimarro 2004: the exact mapping through the pairwise velocity distribution; the large-scale limit "differs from the Kaiser formula by terms that depend on Gaussian and non-Gaussian contributions to the velocity dispersion of large-scale flows".
- Taruya, Nishimichi & Saito 2010 (arXiv:1006.0699, TNS): Kaiser terms with non-linear spectra plus correction terms from the density–velocity coupling, times a damping factor.
- Lagrangian perturbation theory with resummed displacements and velocities, as in velocileptors: Chen et al. 2021 (arXiv:2012.04636), which also compares the moment expansion and the Gaussian streaming model.

### 8.4 Streaming models
<!-- key: streaming-models -->

The streaming model convolves the real-space correlation function with the pairwise line-of-sight velocity distribution. Fisher 1995 (arXiv:astro-ph/9412081) shows it "can be made consistent with linear theory provided that the model for the streaming has the functional form predicted by linear theory and that velocity distribution is chosen to be a Gaussian with the correct linear theory dispersion" [src, abstract]. Fisher's exact result for Gaussian density and velocity fields related as in linear theory, as written by Reid & White 2011 (arXiv:1105.4165, quoting Fisher's eq. 20) [src: Eq. 15, re-read in the HTML rendering on 2026-10-15], with r_σ and r_π the separations across and along the line of sight, y the real-space line-of-sight separation, r² = r_σ² + y²:

1 + ξ^s_g(r_σ, r_π) = ∫ dy [2π σ12²(y)]^(−1/2) exp[−(r_π − y)²/(2σ12²(y))] × [1 + ξ^r_g(r) + (y/r)(r_π − y) v12(r)/σ12²(y) − (1/4)(y²/r²)(v12²(r)/σ12²(y))(1 − (r_π − y)²/σ12²(y))].

Its linear expansion (arXiv:1105.4165) [src: Eq. 16] is ξ^s_g = ξ^r_g(s) − d/dy[v12(r) y/r] + (1/2) d²/dy²[σ12²(y)], both derivatives at y = r_π: the infall term carries bf, the dispersion term f². Reid & White then resum the infall term into the exponential, giving the scale-dependent Gaussian streaming model 1 + ξ^s_g(r_σ, r_π) = ∫ [1 + ξ^r_g(r)] exp{−[r_π − y − μ v12(r)]²/[2σ12²(r, μ)]} dy/sqrt[2π σ12²(r, μ)], μ = y/r [src: Eq. 25], which they call "not mathematically rigorous" but an attempt "to capture the most important non-perturbative effects" [src: Sect. 2.5]; even with linear-theory inputs it changes ξ2 and ξ4 substantially at 30–80 h⁻¹Mpc, more so at higher bias [src: Sect. 2.5, Fig. 4]. With perturbation-theory inputs, the agreement on ξ2 with N-body haloes is "excellent for the HOD halo subsample" while "the accuracy of the model is worse than 2 per cent for scales smaller than ∼40 h⁻¹ Mpc", an error "traced almost entirely" to the perturbative v12 [src: Sect. 6]. They find that "the dominant correction to the Kaiser limit in this model scales like b³", and confirm "at the per cent level" that the real-space bias is the one that sets the pairwise infall. Here σ12 is again a pairwise dispersion, in length units.

## 9. Perturbation theory and EFTofLSS ingredients
<!-- key: perturbation-theory-and-eftoflss-ingredients -->

Read in Ivanov, Simonović & Zaldarriaga 2020, arXiv:1909.05277, Sect. 3.1 and appendix "Theory Model" [src]; equation numbers re-read in the HTML rendering on 2026-10-15 [src: Eqs. 3.1–3.10, A.1–A.12]; this model became CLASS-PT (Chudaykin et al. 2020, arXiv:2004.10607).

- Structure: P_g,ℓ(k) = P^tree + P^1-loop + P^noise + P^ctr, per multipole [src: Eq. 3.1]; tree level (b1 + f μ²)² P_lin [src: Eq. 3.3].
- Stochastic term: P^noise_0 = P_shot, P^noise_2 = 0 without a window [src: Eq. 3.6].
- Leading counterterms: P^ctr,LO_ℓ(k) ≡ −2 c_ℓ² k² P_lin(k), ℓ = 0, 2 [src: Eq. 3.7]. "The scale-dependence of the counterterms is not free. It is fully fixed by symmetry arguments"; "the true amplitude (and even the sign) of the counterterms cannot be predicted". The monopole one absorbs the higher-derivative bias b_∇² ∇²δ; the quadrupole one is dominated by fingers of God.
- Link to the dispersion models (arXiv:1909.05277): c_2² = [f(5f² + 12 f b1 + 7 b1²)/14] σ_v² ≈ 2.5 σ_v² for b1 = 2, f = 0.75 [src: Eq. 3.8]; σ_v ~ 5 Mpc/h gives c_2² ~ 60 Mpc²/h² [src]. It follows from P^FoG(k, μ) ≈ −(μ f k σ_v)² P^tree_g(k, μ) [src: Eq. 3.9], the Taylor expansion of a Gaussian or Lorentzian damping.
- Next-to-leading counterterm: P^ctr,NLO(k, μ) ≡ c̃ k⁴ μ⁴ f⁴ (b1 + f μ²)² P_lin(k) [src: Eq. 3.10], needed because the velocity scale σ_v⁻¹ "can be significantly lower than the non-linear scale k_NL controlling gravitational non-linearities"; the authors also read it as "a simple model for the theoretical error".
- Validity (arXiv:1909.05277) [src: Sect. 3.1]: "sufficient to describe the statistics of biased tracers in real space up to k_max = 0.3 h/Mpc for the volume and redshifts typical to the BOSS survey"; redshift space is more restrictive. Seven nuisance parameters per sample: b1, b2, b_G2, c_0², c_2², c̃, P_shot (b_Γ3 fixed to zero as degenerate).
- Full expression (appendix): P_g(k, μ) = Z1²(k) P_lin(k) + 2 ∫_q Z2²(q, k−q) P_lin(abs(k−q)) P_lin(q) + 6 Z1(k) P_lin(k) ∫_q Z3(q, −q, k) P_lin(q) − 2c̃0 k² P_lin − 2c̃2 f μ² k² P_lin − 2c̃4 f² μ⁴ k² P_lin − c̃ f⁴ μ⁴ k⁴ (b1 + f μ)² P_lin + P_shot [src: Eq. A.1, as printed], with Z1 = b1 + f μ² [src: Eq. A.2a] and Z2(k1, k2) = b2/2 + b_G2[(k1·k2)²/(k1² k2²) − 1] + b1 F2 + f μ² G2 + (f μ k/2)[(μ1/k1)(b1 + f μ2²) + (μ2/k2)(b1 + f μ1²)] [src: Eq. A.2b]; Z3 is Eq. A.3. Three μ-dependent counterterms here against two multipole ones in the main text, and the c̃ term differs between the two places as printed: sign + in Eq. 3.10, − in Eq. A.1, and (b1 + f μ²)² in Eq. 3.10 against (b1 + f μ)² in Eq. A.1, the latter a slip by the μ-power counting of Eq. 3.10 [der]. "The counterterm" is not one convention even inside one paper.

**IR resummation** (same appendix). Bulk flows broaden the BAO feature; without resummation the EFT leaves "a 2% residual which appeared related to the BAO oscillations" (Senatore & Zaldarriaga 2015, arXiv:1404.5954, abstract).

- Split: P_lin = P_nw + P_w [src: Eq. A.4]. Leading order: P_LO(k, μ) ≡ P_nw(k, μ) + exp[−k² Σ²_tot(μ)] P_w(k, μ) [src: Eq. A.5].
- Damping: Σ²_tot(μ) = [1 + f μ²(2 + f)] Σ² + f² μ²(μ² − 1) δΣ² [src: Eq. A.6], with Σ² ≡ (1/6π²) ∫₀^k_S dq P_nw(q)[1 − j0(q/k_osc) + 2 j2(q/k_osc)] and δΣ² ≡ (1/2π²) ∫₀^k_S dq P_nw(q) j2(q/k_osc) [src: Eq. A.7].
- One loop: P_g → P_nw,lin + P_nw,1-loop + exp[−k² Σ²_tot]{P_w,lin (1 + k² Σ²_tot) + P_w,1-loop}, P_w,1-loop ≡ P_1-loop[P_nw + P_w] − P_1-loop[P_nw] [src: Eqs. A.8–A.9].
- (arXiv:1909.05277) "k_S is arbitrary, and any dependence on it should be treated as a theoretical error"; the paper takes k_S = 0.2 h/Mpc, which "gives the same result as an alternative choice k_S = k/2" [src: App. A]. It prints "k_osc is the BAO wavelenght ~110 h/Mpc" [src: App. A, as printed]; the Bessel argument q/k_osc requires a wavenumber, the inverse of a ~110 Mpc/h length.
- The systematic derivation is Blas et al. 2016 (arXiv:1605.02149). Codes differ: a k_IR split in velocileptors LPT and PyBird, wiggle/no-wiggle damping in velocileptors EPT and FOLPSν (Maus et al. 2024, arXiv:2404.07272, Sect. 3) [src].

**Alcock–Paczynski mapping** (same appendix): P_obs(k_obs, μ_obs) = P_g(k_true, μ_true) × D²_A,fid H_true/(D²_A,true H_fid) [src: Eq. A.10], with k²_true = k²_obs[(H_true/H_fid)² μ²_obs + (D_A,fid/D_A,true)²(1 − μ²_obs)] and μ²_true = (H_true/H_fid)² μ²_obs/[same bracket] [src: Eq. A.11]; the multipoles are then taken in μ_obs with the (2ℓ+1)/2 normalisation [src: Eq. A.12]. The volume prefactor is the term most easily dropped in a re-implementation.

**Other code-level differences** (Maus et al. 2024) [src]: the LPT flavour of velocileptors writes P_s = P_s^LPT + k²(α0 + α2 μ² + α4 μ⁴) P_s,Zel + R_h³(1 + σ2 k² μ² + σ4 k⁴ μ⁴) [src: Eq. 12], counterterms of the form k² P_Zel, the other codes k² P_lin, which "differ at high k"; PyBird carries an extra stochastic term in k²/k_M².

**Origins.** The effective-fluid treatment of short modes is Baumann et al. 2012 (arXiv:1004.2488) and Carrasco, Hertzberg & Senatore 2012 (arXiv:1206.2926), who measured c_s² of order 10⁻⁶ [src, abstract]; standard perturbation theory is reviewed by Bernardeau et al. 2002 (arXiv:astro-ph/0112551); the companion first BOSS analysis is D'Amico et al. 2020 (arXiv:1909.05271); Ivanov 2026 (arXiv:2607.28314) is the lecture-note treatment.

## 10. Bias expansions
<!-- key: bias-expansions -->

**Eulerian basis of the first EFT analysis** (arXiv:1909.05277, Sect. 3.1): δ_g = b1 δ + (b2/2) δ² + b_G2 G2 [src: Eq. 3.4], with G2(k) = ∫ d³p/(2π)³ [(p·(k − p))²/(p² abs(k − p)²) − 1] δ_lin(p) δ_lin(k − p) [src: Eq. 3.5]. One more operator, b_Γ3, enters the one-loop spectrum; operators non-local in time appear "only at fourth order".

**Equivalent bases.** McDonald & Roy 2009 (arXiv:0902.0991): "only two new free parameters are needed to model the power spectrum and bispectrum up to 4th order", one multiplying s_ij s_ji with s_ij = [∇_i∇_j∇⁻² − (1/3)δ^K_ij] δ, the other s_ij t_ji with t_ij the same operator on (θ − δ); short-range non-locality starts with R² ∇²δ [src, abstract]. Assassi et al. 2014 (arXiv:1402.5916): Eulerian bias is consistent under renormalisation only with non-local and higher-derivative terms, organised with Galileon operators [src, abstract]. DESI's velocileptors baseline is Lagrangian: b1, b2, b_s, b3, with b_s multiplying "the initial shear field" (arXiv:2411.12021, Sect. 4.3.1).

**Conversions and co-evolution relations** (Maus et al. 2024, arXiv:2404.07272, Sect. 3.1 and 3.5; equations numbered 1–17 in the HTML rendering read 2026-10-15, cited earlier in this skill as 3.10–3.17 by count):

- Lagrangian bias functional of velocileptors: F(q) = 1 + b1 δ0 + (1/2) b2 (δ0² − ⟨δ0²⟩) + b_s (s0² − ⟨s²⟩), with 1 + δ_g(k) = ∫ d³q e^(i k·(q+Ψ)) F[δ^(1)(q)] [src: Eqs. 9–10].
- Co-evolution means b_s^L = b3^L = 0 at initial times, so that the Eulerian b_s and b3 are proportional to b1^L = b1^E − 1 [src: Sect. 3.5].
- velocileptors EPT: b2^E = b2^L + (8/21) b1^L; b_s^E = −(2/7)(b1^E − 1); b3^E = b1^E − 1 [src: Eq. 15].
- FOLPSν (arXiv:2404.07272): b_s2 = −(4/7)(b1^E − 1); b_3nl = (32/315)(b1^E − 1) [src: Eq. 16].
- PyBird, through the "monkey bias" formalism with b3^L = b_s^L = 0: b̃1 = b1^v + 1; b̃2 = (7/2)(2/7 + b_s^L) = 1; b̃3 = [294 − 1015(b1 − 1)]/441; b̃4 = −(7/5)(b1 − 1) − (7/10) b2^v, b^v the velocileptors parameters [src: Eq. 17]; the paper puts a flat prior on b̃4 directly.
- The co-evolution value of the tidal coefficient is −2/7 or −4/7 times (b1^E − 1) depending on the operator normalisation [der from the two equations]: "tidal bias" values are not comparable across codes without this table.
- Linear bias: the Lagrangian b1 and the Eulerian one differ by 1; DESI samples (1 + b1)σ8(z) (arXiv:2411.12021, Sect. 4.7).
- DESI does not impose co-evolution on b_s, because doing so "would add cosmological information on A_s and ω_cdm".

**Other meanings of "bias".** Gravity alone generates a tidal term "even if this term is absent in the initial conditions"; it enters P(k) as a loop correction but the bispectrum at leading order (Baldauf et al. 2012, arXiv:1201.4827) [src, abstract]. DES Y3 uses P_δg,A(k, z) = b1(z) P_mA(k, z) with the non-linear matter spectrum (Krause et al. 2021, arXiv:2105.13548): a different object from the perturbative b1. Local f_NL gives a "strongly scale-dependent bias" (Dalal et al. 2008, arXiv:0710.4560; limits in `cosmo-inflation-primordial`). Assembly bias: at 10^11 M_⊙/h the oldest 10% of haloes are "more than 5 times more strongly correlated" than the youngest 10%, which "contradicts a fundamental assumption of the halo occupation distribution models" (Gao, Springel & White 2005, arXiv:astro-ph/0506510) [src, abstract]; the perturbative expansion absorbs it in its coefficients, HOD mocks do not (`cosmo-simulations-mocks`). The general reference is Desjacques, Jeong & Schmidt 2018 (arXiv:1611.09787).

## 11. Halo model
<!-- key: halo-model -->

Read in Asgari, Mead & Heymans 2023, arXiv:2303.08752, Sect. 2.1 and 3 [src]; every equation number below re-read in the HTML rendering on 2026-10-15 [src: Eqs. 1–19, 36–50].

- A field is a sum over haloes, θ_u(x) = Σ_i N_i W_u,i(abs(x − x_i)) (Eq. 1), with profile transform Ŵ_u(k) = ∫₀^∞ [sin(kr)/(kr)] W_u(r) 4π r² dr (Eq. 4); W_u(M, x) = W_u(M) U_u(M, x), U normalised to unit volume integral so that Û(M, k→0) = 1.
- Convention (Eq. 8): ⟨θ̂_u(k) θ̂*_v(k')⟩ = (2π)³ δ_D(k − k') P_uv(k), with θ̂_u(k) = ∫ θ_u(x) e^(−i k·x) d³x (Eq. 2), the sign of LoVerde & Afshordi, not of Hamilton (section 7).
- One-halo term (Eq. 13): P^1h_uv(k) = ∫₀^∞ Ŵ_u(M, k) Ŵ_v(M, k) n(M) dM; at low k it tends to a constant, "so-called shot noise".
- Two-halo term (Eq. 16): P^2h_uv(k) = ∫∫ dM1 dM2 P_hh(M1, M2, k) Ŵ_u(M1, k) Ŵ_v(M2, k) n(M1) n(M2), with P_hh the spectrum of halo centres, shot noise subtracted; approximated (Eq. 17) as P_hh = b(M1) b(M2) P^lin_mm(k)[1 + β^nl(M1, M2, k)], β^nl → 0 as k → 0; then P^2h_uv = P^lin_mm I^nl_uv + P^lin_mm Π_{n=u,v} ∫ Ŵ_n(M, k) b(M) n(M) dM (Eq. 18), I^nl the β^nl-weighted double integral (Eq. 19).
- Ingredients as the review writes them (arXiv:2303.08752, Sect. 3): σ²(R) = ∫ 4π (k/2π)³ P^lin(k) T²(kR) d ln k, T(x) = (3/x³)(sin x − x cos x) (Eqs. 36–37); M = (4/3)π R³ ρ̄ (Eq. 38), ρ̄ the mean matter density; peak height ν = δ_c/σ(M) (Eq. 39); multiplicity f(ν) dν = (M/ρ̄) n(M) dM (Eq. 40), Sheth–Tormen form f(ν) = A[1 + (q ν²)^(−p)] e^(−q ν²/2) (Eq. 41); peak-background-split bias b(ν) = 1 − (1/δ_c)[1 + d ln f(ν)/d ln ν] (Eq. 42); NFW ρ(r) = ρ_s/[(r/r_s)(1 + r/r_s)²] (Eq. 45), truncated at r_h with M = (4/3)π r_h³ Δ_h ρ̄ (Eq. 46), Δ_h relative to the background density "usually either 200, or 200 times the critical density, or else the virial definition", ρ_s = [M/(4π r_h³)] c³/[ln(1 + c) − c/(1 + c)] (Eq. 48), c the concentration r_h/r_s; friends-of-friends linking length b against SO threshold, (b/0.2)^(−3) ≃ Δ_h/180 (Eq. 50).
- The review's Table 1 records that the mass function "is a strong function" of the halo finder and mass definition, and that a peak-background-split bias derived from a mass function "may not be an accurate description" of the measured one [src: Sect. 3.2].

Ingredients and their defining papers: mass function and its non-universality (Tinker et al. 2008, arXiv:0803.2706), linear halo bias calibrated to normalise the bias of all matter to unity (Tinker et al. 2010, arXiv:1001.3162), the peak-background split linking the two (Sheth & Tormen 1999, arXiv:astro-ph/9901122), the universal profile (Navarro, Frenk & White 1997, arXiv:astro-ph/9611107), the central–satellite occupation (Zheng et al. 2005, arXiv:astro-ph/0408564: a step function for centrals plus a power law for satellites, Poisson satellites, M1 ≈ 14–18 M_min) [src, abstracts]. Conventions to state: the mass definition (spherical overdensity Δ times the background density in Tinker; friends-of-friends bias is ~10% lower than Δ = 200), masses in M_⊙/h, and, with massive neutrinos, the cb field in σ(M) (section 14). halofit (Smith et al. 2003, arXiv:astro-ph/0207664) and HMcode (Mead et al. 2015, arXiv:1505.07833; Mead et al. 2021, arXiv:2009.01858) are halo-model-inspired fits to simulations, not evaluations of these integrals. The older review is Cooray & Sheth 2002 (arXiv:astro-ph/0206508).

## 12. Limber approximation and angular power spectra
<!-- key: limber-approximation-and-angular-power-spectra -->

From LoVerde & Afshordi 2008, arXiv:0809.5112; equation numbers re-read in the HTML rendering on 2026-10-15 [src: Eqs. 2–14]: fields with ⟨A(k1) B*(k2)⟩ = (2π)³ δ³(k1 − k2) P_AB(k1) (Eq. 3) projected as Ã(n̂) = ∫ dr F_A(r) A(r n̂) (Eq. 4).

- Exact (Eq. 5): C_AB(ℓ) = ∫ dr1 dr2 F_A(r1) F_B(r2) ∫ (2k² dk/π) j_ℓ(kr1) j_ℓ(kr2) P_AB(k).
- Limber series (Eq. 12), ν ≡ ℓ + 1/2, f(r) ≡ F(r)/sqrt(r) (Eq. 6): C_AB(ℓ) = ∫ (dr/r) P_AB(ν/r) f_A(r) f_B(r){1 − (1/ν²)[(r²/2)(f_A''/f_A + f_B''/f_B) + (r³/6)(f_A'''/f_A + f_B'''/f_B)] + O(ν⁻⁴)}; the leading term is C_AB(ℓ) = ∫ dr F_A F_B r⁻² P_AB(k = (ℓ + 1/2)/r) [der].
- First correction (Eqs. 13–14): C_AB(ℓ) = ∫ (dk/k) P_AB(k) f_A(r) f_B(r){1 + (ν⁻²/2)[(d ln f_A/d ln r)(d ln f_B/d ln r) s(k) − p(k)] + O(ν⁻⁴)}, r = ν/k, s = d ln P_AB/d ln k, p = k²[3P_AB'' + k P_AB''']/(3P_AB).
- Convergence: for kernels peaked at the same distance r̄ with widths σ_A, σ_B the correction is subdominant when ν ≳ r̄/max[σ_A, σ_B]; for kernels peaked at r_A ≠ r_B the condition is ν ≳ r̄(r_A − r_B)/(σ_A σ_B). Narrow or barely overlapping bins push validity to high ℓ.
- Why ℓ + 1/2: k r̄ → sqrt[ℓ(ℓ+1)] = ℓ + 1/2 + O(1/ℓ), from comparing the flat-sky ℓ(ℓ+1)C_ℓ ≈ k_⊥² P_2D(k_⊥) (Eq. 19) with Eq. 13 [src: Sect. III]; replacing ν by ℓ "will increase the error from O(ℓ⁻²) to O(ℓ⁻¹)" [src: Sect. V].
- Worked size (arXiv:0809.5112) [src: Sect. IV.1, Fig. 1]: for a Gaussian bin of σ_z = 0.01 the expansion converges only above ν_c ~ r(z0)/σ_r, about 15 at z0 = 0.3 and 30 at z0 = 0.6; "very roughly, for ℓ > 5 r(z0)/σ_r the 0th order Limber approximation is accurate to ∼1%". Cross-spectra of bins with small overlap are worse and gain most from the second-order term; a broad kernel crossed with a narrow one stays accurate [src: Sect. IV.2–IV.3]. The examples use linear theory with Ω_m = 0.27, σ8 = 0.8.

As used today (Krause et al. 2021, arXiv:2105.13548, DES Y3), equation numbers re-read in the HTML rendering on 2026-10-15 [src: Eqs. 3–5, 16, 25, 29–34]:

- Limber (arXiv:2105.13548, Eq. 16): C^ij_AB(ℓ) = ∫ dχ [W^i_A(χ) W^j_B(χ)/χ²] P_AB(k = (ℓ + 0.5)/χ, z(χ)), flat universe.
- Non-Limber clustering (Eqs. 29–34, following Fang et al. 2020, arXiv:1911.11947, and the conventions of CCL, Chisari et al. 2019, arXiv:1812.05995): Δ_D(k, ℓ) = ∫ dχ W_δ,g(χ) T_δg(k, z) j_ℓ(kχ); Δ_RSD(k, ℓ) = −∫ dχ f(z) W_δ,g(χ) T_δ(k, z) j_ℓ''(kχ); Δ_μ(k, ℓ) = [ℓ(ℓ+1)/k²] C_g ∫ (dχ/χ²) W_κ,g(χ) T_δ(k, z) j_ℓ(kχ); C^ij(ℓ) = (2/π) ∫ (dk/k) k³ P_Φ(k) Δ^i_obs Δ^j_obs, Δ_obs = Δ_D + Δ_RSD + Δ_μ, with T_δg ≈ b1(z) T_δ and P_Φ the primordial spectrum [src: Eqs. 29–32]. Only the linear part b1² P_lin is integrated with two Bessel functions; the non-linear remainder P_gg − b1² P_lin is put back in Limber, because it "is significant only on small scales where the Limber approximation is sufficiently accurate" [src: Sect. III.2, Eqs. 33–34]; the integrals use a generalised FFTLog.
- DES Y3 computes clustering without Limber and uses Limber for shear and galaxy–galaxy lensing, for which it "is sufficient … beyond the accuracy of the DES-Y3 analysis".

Kitching et al. 2017 (arXiv:1611.04954) list the three approximations usually made together in cosmic shear (flat sky, Limber as the "Bessel-to-delta function limit", Hankel transform) and the exact replacement, Wigner small-d matrices. Non-Limber codes are compared in Leonard et al. 2023 (arXiv:2212.04291). Sizes are in `results.md` section 5; lensing-specific projections in `cosmo-weak-lensing`.

## 13. Relativistic and wide-angle terms
<!-- key: relativistic-and-wide-angle-terms -->

**What a survey measures.** The observed number-count fluctuation in direction n at redshift z, linear order, Bardeen potentials Φ and Ψ (Bonvin & Durrer 2011, arXiv:1105.5280, Sect. II.2) [src: Eq. 31, re-read in the HTML rendering on 2026-10-15; Δ_Ω written out in Eq. 28]; ℋ = aH, r_S the comoving distance to the source, V the gauge-invariant velocity, dots conformal-time derivatives, Δ_Ω the angular Laplacian:

Δ(n, z) = D_g + Φ + Ψ + (1/ℋ)[Φ̇ + ∂_r(V·n)] + (ℋ̇/ℋ² + 2/(r_S ℋ))(Ψ + V·n + ∫₀^r_S dλ (Φ̇ + Ψ̇)) + (1/r_S) ∫₀^r_S dλ [2 − ((r_S − r)/r) Δ_Ω](Φ + Ψ).

| Term | The authors' name for it |
|---|---|
| D_g | gauge-invariant density (flat slicing); D_g = D_s − 3Φ with D_s the Newtonian-gauge density |
| (1/ℋ) ∂_r(V·n) | redshift-space distortion, "the largest single correction on intermediate scales" |
| (ℋ̇/ℋ² + 2/(r_S ℋ)) V·n | Doppler term; the 2/(r_S ℋ) factor makes it largest at low redshift [der from the formula] |
| the same prefactor on Ψ and ∫(Φ̇ + Ψ̇) | ordinary and integrated Sachs–Wolfe terms |
| (2/r_S) ∫ dλ (Φ + Ψ) | radial volume distortion |
| −(1/r_S) ∫ dλ ((r_S − r)/r) Δ_Ω(Φ + Ψ) | lensing distortion, "especially relevant on large scales" |

The expression has no galaxy bias, no magnification bias from a flux limit and no evolution bias. Challinor & Lewis 2011 (arXiv:1105.5292) give the result "for sources observed as a function of flux, including magnification bias and radial-displacement effects"; Yoo, Fitzpatrick & Zaldarriaga 2009 (arXiv:0907.0707) the gauge-invariant generalisation of linear bias [src, abstracts]. In practice the lensing term enters with a coefficient set by the sample selection: DES Y3 writes δ_g,μ = C_g κ_g, κ_g = ∫ dχ W_κ,g δ_m [src: Eqs. 3–4], with C_g = 5 ∂ln n_g/∂m + ∂ln n_g/∂ln r − 2 at the magnitude and size limits, estimated from the data and held fixed (arXiv:2105.13548) [src: Eq. 25].

**Wide-angle effects** are distinct: they arise in the Kaiser term alone because the line of sight differs between the two galaxies of a pair. Szalay, Matsubara & Landy 1998 (arXiv:astro-ph/9712007) give the closed linear form for arbitrary geometry, which "in the limit of small angles … reduces to the plane-parallel approximation". Castorina & White 2018 (arXiv:1709.09730) compute the multipole signatures including "the terms generated by the galaxy selection function" (Hamilton's α(r) term of section 8.1); Beutler, Castorina & Zhang 2019 carry them through the window and show that tying the line of sight to one galaxy generates the odd multipoles ℓ = 1, 3. For velocities see Castorina & White 2020 (arXiv:1911.08353) and `cosmo-peculiar-velocities`. An analysis on large scales must state its pair line-of-sight definition and whether the induced dipole is modelled.

## 14. Massive neutrinos
<!-- key: massive-neutrinos -->

Read in Lesgourgues & Pastor 2006, arXiv:astro-ph/0603494, Sect. 4.5.6 and 4.6.1 [src]; equation numbers re-read in the HTML rendering on 2026-10-15 [src: Eqs. 12, 132–144].

- f_ν ≡ ρ_ν/(ρ_cdm + ρ_b + ρ_ν) = Ω_ν/Ω_m. Below the free-streaming scale neutrinos "contribute to the homogeneous expansion through Friedmann equation" but not to the Poisson equation, so δ̈_cdm + (2/τ) δ̇_cdm − (6/τ²)(1 − f_ν) δ_cdm = 0 [src: Eq. 132], exponents p± = [−1 ± sqrt(1 + 24(1 − f_ν))]/4 [src: Eq. 133], with growing mode δ_cdm ∝ a^(1 − (3/5) f_ν) for f_ν ≪ 1; with Λ, δ_cdm ∝ [a g(a)]^(1 − (3/5) f_ν). The potential decays as a^(−(3/5) f_ν).
- Large scales (k < k_nr): "for fixed ω_m, this branch of the spectrum is completely insensitive to the value of f_ν".
- Small scales (k ≫ k_nr, k_eq; arXiv:astro-ph/0603494), at fixed (ω_m, ω_b, Ω_Λ, A, n_s, τ): P^(f_ν)/P^(f_ν=0) = (1 − f_ν)³ [a0 g(a0)/a_nr]^(−(6/5) f_ν) [src: Eq. 142], i.e. (1 − f_ν)³ [1.9 × 10^5 g(a0) ω_m f_ν/N_ν]^(−(6/5) f_ν) [src: Eq. 143], using a0/a_nr = 2000 m_ν/(1 eV) and m_ν = (ω_ν/N_ν) × 93.2 eV [src: Sect. 4.5.6]; for f_ν < 0.07 this is "the well-known linear expression" ΔP/P ≃ −8 f_ν. The paper prints Eq. 144 as P^(f_ν)/P^(f_ν=0) ≃ −8 f_ν, the ratio itself, an evident slip. Its Fig. 12 checks Eq. 143 numerically at k = 5 h Mpc⁻¹ for fixed (ω_m, Ω_Λ) = (0.147, 0.70), "in excellent agreement"; g(a0) ≃ 0.8 "can even be replaced by one" [src: Sect. 4.5.7]. The CDM growth with neutrinos maps onto the massless case as δ_cdm^(f_ν)[a] = δ_cdm^(f_ν=0)[(1 − f_ν) a] before a_nr [src: Eq. 137].
- a_eq/a0 = ω_r/(ω_b + ω_cdm) = (1 − f_ν)⁻¹ ω_r/ω_m [src: Sect. 4.5.6], ω_r computed "assuming that all neutrinos would remain massless"; at fixed ω_m, a_eq grows as (1 − f_ν)⁻¹.
- The −8 f_ν holds for fixed ω_m with ω_cdm reduced; the paper's next figure fixes ω_b and ω_cdm and shifts h or Ω_Λ instead. A quoted suppression needs that statement.

Free-streaming scale of one species, as written by Pezzotta et al. 2025 (arXiv:2503.16160): λ_s(z) = 2π sqrt(2/3) c_ν(z)/H(z) ≃ 7.7 sqrt[ω_m(z)/(ω_m,0 (1+z))] (1 eV/m_ν) Mpc [src: Eq. 8]; the suppression factor S(k) ≡ P(k)/P_⋆(k) is taken against a cosmology with ω_c,⋆ = ω_c + ω_ν and no massive neutrinos, i.e. at fixed total matter [src: Eq. 7].

**Three constants for one conversion**, each read at source: 93.2 eV (Lesgourgues & Pastor 2006, Sect. 4.5.6; the same review writes Ω_ν = Σm_i/(93.14 h² eV) in its Eq. 12 [src]), 93.04 eV (arXiv:1303.5076, Sect. 2.1.1), 93.14 eV (arXiv:2503.14738, Eq. 7); Aubourg et al. write ω_ν = 0.0107 Σm_ν/eV (arXiv:1411.1074, Sect. II.2).

**Mass splitting actually used** (see `surveys-and-data.md`): one massive state of 0.06 eV plus two massless (Planck, arXiv:1807.06209, Sect. 2.1; ACT DR6, arXiv:2503.14452, Sect. 7.1; DESI with Σm_ν fixed, arXiv:2503.14738, Sect. V); three degenerate states (DESI with Σm_ν varied, same section); Σm_ν fixed to 0.06 eV (KiDS-Legacy, arXiv:2503.19441, Sects. 2.2 and 5.1).

**Which field: cb or total matter.** The halo mass function is more universal with σ²_cdm(M, z) than with the total-matter variance, and halo bias is "both more universal, and less scale- or k-dependent" against the CDM spectrum (Castorina et al. 2014, arXiv:1311.1212); the Tinker bias works "once the linear cold dark matter power spectrum is used" (Villaescusa-Navarro et al. 2014, arXiv:1311.0866); the momentum bias of haloes relative to CDM+baryons is 1, implying "a velocity bias between halos and total matter" (Villaescusa-Navarro et al. 2018, arXiv:1708.01154) [src, abstracts]. So bias, growth rate and the template of a clustering model belong to the cb field (DESI: "the linear cold dark matter + baryon power spectrum", and σ8 "excluding neutrinos"), Planck's σ8 is total matter, and lensing responds to total matter. Bounds on Σm_ν are in `cosmo-neutrinos-dark-matter`.

## 15. Codes
<!-- key: codes -->

Each with the paper read or cited above; installation and versions are in `cosmo-software-ecosystem`.

| Purpose | Codes |
|---|---|
| Boltzmann | CAMB (arXiv:astro-ph/9911177); CLASS (arXiv:1104.2933) |
| Non-linear matter | halofit (arXiv:astro-ph/0207664, arXiv:1208.2701, neutrinos arXiv:1109.4416); HMcode (arXiv:1505.07833, arXiv:2009.01858); pyhalomodel (arXiv:2303.08752); Aletheia (Sánchez et al. 2025, arXiv:2511.13826) |
| One-loop galaxy P(k) | CLASS-PT (arXiv:2004.10607); velocileptors (arXiv:2012.04636); PyBird and FOLPSν (compared in arXiv:2404.07272); elf (Kobayashi & Akitsu 2026, arXiv:2610.08023); all DESI options sit in desilike |
| Angular spectra | CCL (arXiv:1812.05995); non-Limber FKEM in CosmoLike, Levin, matter (arXiv:2212.04291); nicaea (Kilbinger et al. 2017, arXiv:1702.05301); Blast.jl (Chiarenza et al. 2026, arXiv:2609.01855) |
| Samplers and frameworks named in the analyses read | Cobaya (DESI, ACT), CosmoSIS (DES, KiDS), CosmoMC (Planck) |

## Not verified
<!-- key: not-verified -->

- The accuracy of DESI's power-law r_d formula against a Boltzmann code: not stated in arXiv:2209.14330 or arXiv:2212.04522 (body searched 2026-10-15); not found elsewhere.
- Growth approximations of Lahav et al. 1991 and Carroll, Press & Turner 1992, and the BBKS formula itself: not on arXiv, not read, not written.
- Mass-function, bias and NFW profile formulae in their original papers (Tinker, Sheth–Tormen, NFW: abstracts only); they are written in `#halo-model` as the Asgari et al. review gives them, and the Sheth–Tormen values of A, p, q were not read.
- The full Challinor–Lewis expression with magnification and evolution bias.
