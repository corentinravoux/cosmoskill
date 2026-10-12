# Theory foundations — which convention each major analysis adopts, read at source

Snapshot: 2026-10-07

## 1. Summary table

This file is not a list of surveys (that is `cosmo-surveys-facilities`): it records, for the analyses whose numbers circulate most, which theory conventions they adopted. Every cell was read in the cited paper [src] unless it says "not read".

| Analysis | Length units | Amplitude parameter and field | Neutrinos | N_eff | Non-linear model | Acoustic or distance variable |
|---|---|---|---|---|---|---|
| Planck 2013, arXiv:1303.5076 | Mpc and Mpc⁻¹ for scales and pivots; σ8 radius 8 h⁻¹Mpc | σ8, total matter, linear, z = 0 | one state of 0.06 eV | 3.046 | not read | θ_MC sampled; r_drag from CAMB × 1.0275 for old BAO |
| Planck 2018, arXiv:1807.06209 | same | σ8 total matter; S8 ≡ σ8 (Ω_m/0.3)^0.5 | "two massless states and a single massive neutrino of mass 0.06 eV" | 3.046 | HMcode (2015 version) replacing Takahashi halofit | θ_MC sampled; θ_*, r_*, r_drag derived |
| ACT DR6, arXiv:2503.14452 | km/s/Mpc for H0 | σ8 derived | 0.06 eV in one massive state | not read | "non-linear matter power spectrum modeling" in CAMB, version not read | θ_MC sampled |
| eBOSS 2021, arXiv:2007.08991 | h⁻¹Mpc | fσ8, σ8 on 8 h⁻¹Mpc; f = ∂ln σ8/∂ln a | not read | not read | per-tracer templates (not read) | D_M/r_d, D_H/r_d, D_V/r_d; z_d "around 1020" |
| DESI DR1 full shape, arXiv:2411.12021 | h⁻¹Mpc of the fiducial cosmology | σ8 "excluding neutrinos" (cb); fσ_s8 in ShapeFit | not read for the chains | 3.044 | one-loop EFT (velocileptors), k < 0.20 h/Mpc | q_∥, q_⊥ against the catalogue cosmology |
| DESI DR2 BAO, arXiv:2503.14738 | h⁻¹Mpc for separations; results as ratios to r_d | none (geometry only) | 0.06 eV, one massive state when fixed; three degenerate when varied | 3.044 (3.04 as pivot of the r_d formula) | BAO template with broadband marginalised | α_iso, α_AP; h r_d sampled without calibration |
| DES Y3 3×2pt, arXiv:2105.13548 | h units (M_⊙/h, R_min = 8 Mpc/h) | S8 in the results paper (DES Collaboration 2021, arXiv:2105.13549, not re-read) | varied in the DES chains [sec: DESI DR2 Sect. 5 fixes Σm_ν to 0.06 eV as an exception to the DES priors]; halofit with the Bird correction | not read | Takahashi halofit, gravity only, scale cuts | Limber for shear, non-Limber for clustering |
| KiDS-Legacy, arXiv:2503.19441 | h/Mpc; θ in arcmin | S8 sampled directly; Σ8 with α = 0.58 | fixed, Σm_ν = 0.06 eV | not read | HMCode2020 with free T_AGN | — |

Reading the table across: no two rows share all columns. The cells that most often invalidate a naive comparison are the field of σ8 (Planck total, DESI cb), the neutrino treatment (fixed against varied), and the non-linear model (halofit against HMCode2020).

## 2. Planck

Read in Planck Collaboration 2013 (arXiv:1303.5076), Sect. 2 and 5.2. Planck 2018 keeps this parameter basis; what was read in the 2018 paper follows the table.

| Item | Planck convention | Where read |
|---|---|---|
| Units | H0 in km s⁻¹ Mpc⁻¹; k_D and the pivots in Mpc⁻¹ (no h); σ8 in 8 h⁻¹Mpc spheres | 2013 Table 1 |
| Sampled acoustic parameter | 100 θ_MC, the CosmoMC approximation to θ_* | 2013 Sect. 2.2.2 |
| σ8 | total matter (baryons + CDM + massive neutrinos), z = 0, linear theory, top-hat of 8 h⁻¹Mpc | 2013 Sect. 2.2.2, eq. 9 |
| Ω_m | includes massive neutrinos | 2013 Table 1 |
| Neutrinos | N_eff = 3.046; one massive eigenstate of 0.06 eV, two massless; Ω_ν h² ≈ Σm_ν/93.04 eV | 2013 Sect. 2.1.1 |
| r_drag | numerical, from CAMB; multiplied by 1.0275 when compared with BAO data that used the Eisenstein–Hu formula | 2013 Sect. 5.2 |
| Pivot scales | A_s at 0.05 Mpc⁻¹; r at 0.002 Mpc⁻¹ | 2013 Table 1 |
| Boltzmann code | CAMB (Lewis, Challinor & Lasenby 2000, arXiv:astro-ph/9911177) | 2013 Sect. 2 |


**Planck 2018** (Planck Collaboration 2018, arXiv:1807.06209, Sect. 2.1, 5.4 and Tables 1–2) [src]:

- Baseline: "three neutrinos species, approximated as two massless states and a single massive neutrino of mass m_ν = 0.06 eV"; flat priors on ω_b, ω_c, θ_MC, τ; A_s at k = 0.05 Mpc⁻¹; N_eff = 3.046 as the Standard Model value.
- Non-linear lensing: "we use the halofit technique … but now replace the Takahashi et al. 2012 approach with HMcode, the fitting method of Mead et al. 2015" (arXiv:1505.07833), as implemented in CAMB.
- Derived values, Plik TT,TE,EE+lowE+lensing: 100 θ_MC = 1.04092 ± 0.00031; 100 θ_* = 1.04110 ± 0.00031; r_drag = 147.09 ± 0.26 Mpc; r_* = 144.43 ± 0.26 Mpc; z_* = 1089.92 ± 0.25; σ8 = 0.8111 ± 0.0060; S8 ≡ σ8 (Ω_m/0.3)^0.5 = 0.832 ± 0.013. These are quoted here as the reference point of the conventions (they are the DESI fiducial cosmology, section 5), not as current constraints; current CMB values are in `cosmo-cmb`.
- Growth: fσ8 ≡ [σ8^(vd)(z)]²/σ8^(dd)(z) (Eq. 27), with "d ln D/d ln a ≈ Ω_m^0.55(z)" for ΛCDM; F_AP(z) = D_M(z) H(z)/c (Eq. 28).

## 3. ACT

### ACT DR6 power spectra and ΛCDM parameters (Louis et al. 2025, arXiv:2503.14452, Sect. 7.1, read in the LaTeX source)

| Item | ACT DR6 choice [src] |
|---|---|
| Sampled parameters | Ω_b h², Ω_c h², the acoustic scale θ_MC, A_s, n_s, τ |
| Derived | "the local Hubble constant, H0 in units of km/s/Mpc, the amplitude of fluctuations today, σ8, and the matter density Ω_m" |
| Neutrinos | "three neutrinos species with a total mass sum of 0.06 eV carried by one massive eigenstate" |
| Helium | BBN consistency relation |
| Code | Cobaya calling CAMB, with accuracy settings tuned to the ACT multipole range, "high-precision recombination calculations and non-linear matter power spectrum modeling" |
| Lensing consistency parameter | A_lens rescales the lensing potential spectrum: C_ℓ^ψ → A_lens C_ℓ^ψ |

ACT shares the Planck basis (θ_MC, one massive state of 0.06 eV, σ8 and Ω_m derived), so the two can be combined without translating parameters. The value of N_eff adopted and the non-linear prescription are described in the companion extended-models paper, not read this session. Results are in `cosmo-cmb`.

## 4. BOSS and eBOSS

Read in eBOSS Collaboration 2021, arXiv:2007.08991 [src], and in the descriptions of the BOSS-era method given by DESI (arXiv:2411.12021, Sect. 4.2) and by Planck 2013 (arXiv:1303.5076, Sect. 5.2).

| Item | BOSS and eBOSS convention |
|---|---|
| Compression | three parameters per redshift bin: the BAO position along and across the line of sight and fσ8 ("standard compression" in DESI's terms) |
| r_d | r_d = ∫_{z_d}^∞ c_s(z)/H(z) dz (eBOSS Eq. 13); the drag epoch "around a redshift z = 1020" |
| Growth | f = ∂ ln σ8/∂ ln a (Eq. 19); σ8(z) "the amplitude of linear matter fluctuations on a comoving scale of 8 h⁻¹Mpc"; fσ8 "characterizes the amplitude of the velocity power spectrum" |
| σ8 and the template | for the BOSS and eBOSS galaxy samples the template is rescaled by the best-fit α_iso before the normalisation is fixed, so that fσ8 is built from a rescaled σ8; with this, the dependence on the template is "significantly smaller than the statistical errors" (Appendix A) |
| Early BAO (to about 2013) | r_s from the Eisenstein–Hu fitting formulae, with spectra from Boltzmann codes; Planck applied the factor 1.0275 |
| Own verdict | "This analysis of the clustering might not be the best approach for future surveys including DESI and Euclid … it may be best to directly fit models to the two-point multipoles without an intermediate data compression step" |

- The rescaling of σ8 by α_iso is the BOSS/eBOSS answer to the 8 h⁻¹Mpc problem of Sánchez 2020 (arXiv:2002.07829); DESI's σ_s8 (section 5) is its formal successor. According to the second pass of this build, the rescaling was applied to the galaxy samples and not to the MGS and quasar points [sec: reading of Appendix A by the second writer, not re-read].
- An earlier example of what the fiducial choices do: Samushia, Percival & Raccanelli 2012 (arXiv:1102.1014) fit SDSS-II LRGs with the background fixed to ΛCDM under WMAP + SN priors and quote f(z)σ8(z) at z = 0.25 and 0.37; the "fσ8" is conditional on that background.
- EFT reanalyses of the same BOSS data (Ivanov, Simonović & Zaldarriaga 2020, arXiv:1909.05277; D'Amico et al. 2020, arXiv:1909.05271) vary the cosmology directly and are compared in `open-questions.md` section 2; Brieden, Gil-Marín & Verde 2022 (arXiv:2204.11868) is the ShapeFit reanalysis of BOSS + eBOSS.

## 5. DESI

### DESI DR2 BAO (DESI Collaboration 2025, arXiv:2503.14738), read in Sect. 3.1, 5 and 6 of the LaTeX source

- **Distances and units.** Separations are binned in h⁻¹Mpc (4 h⁻¹Mpc bins in s, 200 bins in μ over [−1, 1]) [src]; the fitted minimum scale is s_min = 60 h⁻¹Mpc (50 in DR1) [src]. The h⁻¹Mpc unit is that of the fiducial cosmology used to convert redshifts to distances; the published results are the dimensionless ratios D_M/r_d, D_H/r_d, D_V/r_d, which carry no h.
- **Scaling parameters** (Sect. 3.1, eqs. labelled `alpha_defs` and `aisoap_defs`): α_∥ = D_H(z) r_d^fid / [D_H^fid(z) r_d]; α_⊥ = D_M(z) r_d^fid / [D_M^fid(z) r_d]; α_iso = (α_∥ α_⊥²)^(1/3); α_AP = α_∥/α_⊥; D_V(z) ≡ (z D_M(z)² D_H(z))^(1/3). The baseline sampling basis is (α_iso, α_AP), "less correlated".
- **What BAO alone constrains.** Fitting BAO only, DESI samples Ω_m and h r_d with h = H0/(100 km/s/Mpc); the ΛCDM result is Ω_m = 0.2975 ± 0.0086, h r_d = (101.54 ± 0.73) Mpc, correlation coefficient −0.92 [src]. H0 appears only after r_d is calibrated (BBN prior on ω_b, or the CMB); the paper states that the DESI + BBN H0 "does assume standard pre-recombination physics to determine r_d" through its r_d formula.
- **CMB runs.** Base parameters (ω_cdm, ω_b, 100 θ_MC, ln(10¹⁰ A_s), n_s, τ). θ_MC "is an approximation to the acoustic angular scale θ_*" built on fitting formulae; the paper's footnote says the difference between θ_MC and θ_* "only slightly affects the efficiency of the sampling while having no effect on the accuracy of the likelihood evaluation".
- **Neutrinos.** When Σm_ν is not varied it is fixed to 0.06 eV "assuming a single non-zero mass eigenstate"; when varied, three degenerate mass eigenstates are assumed unless a mass ordering is tested [src].
- **Codes and reporting.** Cobaya with CAMB; convergence R − 1 < 0.01; limits at 68% except Σm_ν at 95%; best fits with iminuit from the MAP of each chain; Δχ²_MAP ≡ −2 Δ ln L at the maximum posterior points [src].
- **Fiducial-cosmology systematic.** Raised on α_AP from 0.1% (DR1) to 0.18% (DR2), after adding an evolving-dark-energy case to the test; systematics inflate the α_iso error by 1% (BGS) to 9% (the combined LRG+ELG bin) [src]. The DR1 study is Pérez-Fernández et al. 2024, arXiv:2406.06085.

- **Radiation and neutrino constants** (Sect. 1 and 4.1): standard neutrino content is N_eff = 3.044 and Σm_ν = 0.06 eV; Ω_ν h² = Σm_ν/93.14 eV (eq. 7); the r_d formula is normalised at N_eff = 3.04 [src]. Planck 2013 used N_eff = 3.046 and 93.04 eV (section 2): the two collaborations do not use the same constants, at a level (0.1%) that is harmless for r_d but visible in a reproduction test.
- **Matter density.** Ω_m "includes neutrinos when they are non-relativistic"; Ω_bc = Ω_b + Ω_cdm is the quantity that enters r_d (eq. 2) [src].


### DESI DR1 full shape (Adame et al. 2024, arXiv:2411.12021), Sect. 4.2 read in the LaTeX source

- **Catalogue cosmology and AP.** "We keep the cosmology used to convert redshifts to comoving distances fixed"; the model is distorted with q_∥ = k_∥/k'_∥ = D_H(z)/D_H^fid(z) and q_⊥ = k_⊥/k'_⊥ = D_M(z)/D_M^fid(z), D_H(z) ≡ c/H(z). In full modelling the q are derived; in the compressed approaches the α are fitted parameters.
- **Compressed BAO parameters.** α_∥ = [D_H/r_d]/[D_H/r_d]^fid, α_⊥ = [D_M/r_d]/[D_M/r_d]^fid, α_iso ≡ (α_∥ α_⊥²)^(1/3) = [D_V/r_d]/[D_V/r_d]^fid, α_AP ≡ α_∥/α_⊥, D_V ≡ [z D_H D_M²]^(1/3).
- **σ8.** "the amplitude of dark matter fluctuations smoothed on a 8 h⁻¹Mpc scale".
- **ShapeFit template deformation.** P'_lin(k) = P_lin^fid(k) exp{ (m/a) tanh[a ln(k/k_p)] + n ln(k/k_p) }, with k_p = π/r_d^fid ≃ 0.03 h^fid Mpc⁻¹ and a = 0.6; only m is varied, n fixed [src].
- **σ_s8, the amplitude DESI actually quotes with f.** "for ShapeFit the amplitude of dark matter perturbations is not regulated by σ8, but rather by a slightly different parameter, σ_s8 … in part because σ8 becomes a function of m, but also because of the ambiguity of defining a scale of 8 h⁻¹Mpc when the cosmology that defines h is in principle unknown". Definition: σ_s8 = σ_s8^fid A^(1/2) exp{ (m/2a) tanh[a ln(r_d^fid/s_8)] }, with s_8 ≡ 8 h⁻¹Mpc, A ≡ A_sp/A_sp^fid, A_sp = (r_d^fid/r_d)³ P_lin,nw(k_p r_d^fid/r_d); "both r_d^fid and s_8 are expressed in units of h⁻¹Mpc, where h stands for the value of the chosen fiducial template cosmology" [src].
- **How fσ_s8 is obtained.** The template amplitude is held fixed, only f is fitted, and f is multiplied afterwards by the fixed σ_s8^fid. "This procedure is exact at first-order of perturbation theory, where f and σ_s8 only enter as a product"; beyond that it is an approximation. Raw results are quoted as f/f^fid. Converting fσ_s8 into the usual fσ8 requires the rescaling by q_iso described in eq. 40 of the eBOSS LRG paper cited there (not read this session).
- **Fixed-template caveat.** Standard compression and ShapeFit "assume a fiducial cosmology to compute the non-linear corrections to the linear power spectrum (the one-loop terms), unlike the full modelling approach"; ShapeFit applies an approximate cosmology dependence to those terms.
- **Footnote on σ12.** The paper cites Sánchez 2020 (arXiv:2002.07829) as "an alternative approach through the definition of the smoothing scale in units of Mpc"; DESI did not adopt it.

- **Baseline model and scales** (Sect. 4.3.1 and 4.7) [src]: velocileptors in its Eulerian (EPT) flavour, one-loop, with IR resummation by the wiggle/no-wiggle split; the Lagrangian flavour resums displacements up to a scale k_IR (Chen et al. 2021, arXiv:2012.04636). Bias parameters b1, b2, b_s, b3 with b3 fixed to zero; three stochastic and three counterterm parameters. Fitting range 0.02 < k < 0.20 h Mpc⁻¹; monopole and quadrupole only (the hexadecapole is left out to reduce prior-weight effects).
- **Bias sampled with σ8 attached.** The sampled basis is {(1 + b1) σ8(z), b2 σ8²(z), b_s σ8²(z)}, uniform prior on the first, Gaussian on the others; the Eulerian parameters are sampled as reparametrisations of the Lagrangian ones so that the non-linear bias priors are centred on zero Lagrangian bias.
- **Template field.** The ShapeFit reference spectrum is "the linear cold dark matter + baryon power spectrum": the cb field, not total matter.
- **Catalogue cosmology.** The fiducial cosmology "is the cosmology used to transform the redshifts into comoving distances expressed in h⁻¹Mpc", also called catalogue or grid cosmology; its values are given below.
- **Priors.** Flat on cosmological parameters except n_s and ω_b; N_eff fixed to 3.044; for DESI-alone full modelling ω_b = 0.02198 ± 0.00053 [src].
- **Why only full modelling goes to the cosmology paper.** "Projection effects can impact how the compressed parameters of the ShapeFit method are interpreted under a cosmological model, especially when the MAP value does not coincide with the mean of the posterior."

- **Field and fiducial values** (Sect. 3 and Appendix C) [src]: the fiducial cosmology is "the mean estimates of the Planck TT,TE,EE+lowE+lensing likelihood chains": Ω_c h² = 0.1200, Ω_b h² = 0.02237, σ8 = 0.811355, n_s = 0.9649, h = 0.6736, w0 = −1, wa = 0; footnote 3: "Throughout this paper we refer as σ8 to the amplitude of matter fluctuations excluding neutrinos". The fiducial r_d = 99.0792 Mpc/h; σ_s8 is "the amplitude of cold+baryon matter fluctuations smoothed in units of 8 Mpc/h of the fiducial cosmology". The counterterm prior is Gaussian, centred on zero, of width 12.5 h⁻²Mpc².

## 6. DES

### DES Y3 3×2pt modelling (Krause et al. 2021, arXiv:2105.13548, Sect. II.B and III, read in the LaTeX source; results paper DES Collaboration 2021, arXiv:2105.13549)

| Item | DES Y3 baseline choice [src] |
|---|---|
| Model space | flat νwCDM for the modelling tests; spatially flat, leading order in the lensing deflection |
| Boltzmann codes | CAMB and CLASS (Blas, Lesgourgues & Tram 2011, arXiv:1104.2933), "in excellent agreement at the level of accuracy of this analysis" |
| Non-linear matter spectrum | halofit as recalibrated by Takahashi et al. 2012 (arXiv:1208.2701), with the Bird, Viel & Haehnelt 2012 (arXiv:1109.4416) prescription for massive neutrinos; gravity only |
| Baryons | not modelled; removed by scale cuts chosen against strong-feedback models |
| Galaxy bias | linear b1 per tomographic bin relative to the **non-linear** matter spectrum: P_δg,A(k,z) = b1(z) P_mA(k,z); scale-dependent bias from massive neutrinos neglected, tested |
| Intrinsic alignments | TATT, five parameters, normalisation C̄1 = 5 × 10⁻¹⁴ M_⊙ h⁻² Mpc² |
| Projection | non-Limber with RSD and magnification for clustering; Limber with k = (ℓ + 0.5)/χ for shear and galaxy–galaxy lensing |
| Small-scale galaxy–galaxy lensing | point-mass marginalisation, σ(B) = 10¹⁷ M_⊙/h |
| Units | masses in M_⊙/h and M_⊙ h⁻² Mpc² (IA normalisation): h units throughout |

The stated deficiencies of the matter-spectrum model are the authors' own: no non-gravitational physics, and "finite accuracy in representing the true gravity-only power spectrum", checked against emulators in their stress tests. The DES Y6 3×2pt analysis is DES Collaboration 2026, arXiv:2601.14559; its modelling choices were not re-read this session (see "Not verified"), and its S8 results are in `cosmo-weak-lensing`.


Two further points from the same paper [src]: the clustering scale cut is R_min,w = 8 Mpc/h, an h-unit scale; and on projection effects the paper notes that they arise "when parameters of interest are not fully constrained by the data or are degenerate with other parameters that are prior informed", that they "decrease as the data's constraining power increases and are thus not a systematic bias".

## 7. KiDS

### KiDS-Legacy cosmic shear (Wright et al. 2025, arXiv:2503.19441, Sect. 2.2 and 5.1, read in the LaTeX source)

| Item | KiDS-Legacy choice [src] |
|---|---|
| Sampled cosmological parameters | five: **S8 itself** (flat prior [0.5, 1.0]), Ω_c h² [0.051, 0.255], Ω_b h² [0.019, 0.026], h [0.64, 0.82], n_s [0.84, 1.10] |
| Fixed | Ω_K = 0, w0 = −1, wa = 0, **Σm_ν = 0.06 eV** |
| S8 | S8 ≡ σ8 sqrt(Ω_m/0.3) (abstract); also Σ8 = σ8 (Ω_m/0.3)^α with α fitted to the Ω_m–σ8 contour |
| Linear spectrum | CAMB |
| Non-linear spectrum | HMCode2020 (Mead et al. 2021, arXiv:2009.01858), emulated with CosmoPower; feedback parameter log10(T_AGN/K) in [7.3, 8.3] |
| Scales probed | "mostly sensitive to" 0.1 ≲ k ≲ 1 h/Mpc |
| Angular range | 2.0′ ≤ θ ≤ 300′, COSEBIs and band powers |
| Point estimates reported | marginal mean ± s.d. 0.813 ± 0.018; marginal mode + HPDI 0.815 +0.016/−0.021; MAP + PJ-HPD 0.811 +0.022/−0.015 (COSEBIs) |
| Sampler | nautilus within CosmoSIS, Gaussian likelihood; MAP by Nelder–Mead |

What the paper says about the non-linear prescription: HMCode2020 "has a similar level of accuracy as popular emulators trained directly on N-body simulations (2.5%)" and "is twice as accurate as Halofit from Takahashi et al. (2012)"; in the DES + KiDS joint study it cites, "Halofit tends to overestimate power for lower values of S8, resulting in an underestimated S8 value"; HMCode2015 (Mead et al. 2015, arXiv:1505.07833), used in earlier KiDS analyses, "is ~30% less accurate than HMCode2020", the main difference being the treatment of baryon feedback, "which results in a slightly higher S8 using HMCode2020" [src]. The priors on h²Ω_m extend beyond the range over which HMCode was fitted; the authors report no effect.

Two convention points follow. The prior is flat in S8, not in A_s or σ8; the sampled amplitude variable is a per-collaboration choice and sets the prior volume behind any projection effect. And h is bounded to [0.64, 0.82]: the σ8 radius of 8 h⁻¹Mpc ranges over 9.8–12.5 Mpc across the prior [der: 8/0.82 and 8/0.64].


The abstract also quotes Σ8 ≡ σ8 (Ω_m/0.3)^α = 0.821 +0.014/−0.016 with α = 0.58 "optimised to match the revised degeneracy direction" [src]: a third exponent next to the 0.5 of S8 and the 0.4 of S12.

## 8. Boltzmann codes and their defaults

What was read about the codes behind the analyses above; version-level defaults are in `cosmo-software-ecosystem`.

| Code | Reference | What the analyses read here say of it |
|---|---|---|
| CAMB | Lewis, Challinor & Lasenby 2000, arXiv:astro-ph/9911177 | Planck's z_drag and r_drag are computed "numerically from camb"; used by ACT DR6, DESI (through Cobaya) and KiDS-Legacy; HMcode is available inside it (arXiv:2009.01858) |
| CLASS | Blas, Lesgourgues & Tram 2011, arXiv:1104.2933 | approximation schemes: tight coupling, ultra-relativistic fluid, radiation streaming; DES Y3 finds CAMB and CLASS "in excellent agreement at the level of accuracy of this analysis" |
| Eisenstein–Hu formulae | arXiv:astro-ph/9709112; arXiv:astro-ph/9710252 | lengths in Mpc from Ω_0 h², Ω_b h²; r_s larger than CAMB's by 2.75% in the Planck 2013 fiducial model |
| CCL | Chisari et al. 2019, arXiv:1812.05995 | validated against independent codes; the convention source for the DES non-Limber expressions |
| CLASS-PT | Chudaykin et al. 2020, arXiv:2004.10607 | one-loop spectra "for matter fields and biased tracers in real and redshift space" on top of CLASS |

Three defaults a user must set rather than inherit: the neutrino mass splitting (one massive state or three degenerate), N_eff (3.046 or 3.044), and the field for which σ8 is returned (total matter or cb). None of the papers read here states the code version in the passages read.

## Not verified

- N_eff and the non-linear prescription of ACT DR6: stated in a companion paper that was not read.
- Neutrino treatment of the DESI DR1 full-shape chains, and whether the DESI DR1 cosmology paper converts fσ_s8 with the eBOSS rescaling: not read.
- DES Y3 neutrino prior and N_eff, and all DES Y6 modelling choices (DES Collaboration 2026, arXiv:2601.14559): not read; the Y6 results are in `cosmo-weak-lensing`.
- BOSS DR12 consensus conventions were not read in the BOSS papers themselves, only through eBOSS, DESI and Planck.
- The MGS and quasar exception to the eBOSS σ8 rescaling comes from the second writer's reading and was not re-read.
- Code versions of CAMB, CLASS and HMcode in each analysis.
