# CMB primary anisotropies and lensing — physics and methods

Scope: what the CMB temperature and polarisation spectra and the lensing
reconstruction measure, the estimators and likelihoods used by Planck, ACT and
SPT-3G, the codes, and the conventions that differ between collaborations.
Snapshot: 2026-10-14

Provenance flags: `[src]` read this session in the cited paper; `[sec]` taken
from a named secondary source; `[der]` derived here, derivation stated.
Years attached to author names are arXiv submission years.

## 1. Observables and definitions
<!-- key: observables-and-definitions -->

The CMB is described by three Stokes fields on the sphere, T, Q and U. The
temperature field is expanded in spherical harmonics, T(n) = Σ a_ℓm Y_ℓm(n),
and the spin-2 combination Q ± iU is expanded in spin-weighted harmonics and
rotated into the scalar E and pseudo-scalar B fields (Zaldarriaga & Seljak
1996, arXiv:astro-ph/9609170). The equivalent tensor-harmonic formalism is
Kamionkowski et al. 1996 (arXiv:astro-ph/9611125), who note that for
scalar perturbations one of the four sets of multipole moments vanishes
identically, which allows a clean determination of vector and tensor
contributions [src]. For statistically isotropic Gaussian fields
all information is in the angular power spectra

    ⟨a^X_ℓm a^Y*_ℓ'm'⟩ = δ_ℓℓ' δ_mm' C_ℓ^XY ,   X, Y ∈ {T, E, B}.

Parity conservation sets C_ℓ^TB = C_ℓ^EB = 0, so the cosmological spectra are
TT, TE, EE, BB. Collaborations plot and tabulate

    D_ℓ ≡ ℓ(ℓ+1) C_ℓ / 2π        [μK²]

in thermodynamic (CMB) temperature units. Map depth is quoted in μK-arcmin,
the noise rms in a pixel of one square arcminute. Polarisation depth is
quoted separately and is larger than the temperature depth: the SPT-3G D1
maps reach 5.4, 4.4 and 16.2 μK-arcmin in I at 95, 150 and 220 GHz and 8.4,
6.6 and 25.8 μK-arcmin in Q/U [src] (Quan et al. 2026, arXiv:2603.20163).

The monopole is T₀ = 2.72548 ± 0.00057 K [src] (Fixsen 2009, arXiv:0911.1955).
The dipole is dominated by the solar motion; the NPIPE estimate of its
amplitude is 3366.6 ± 2.7 μK [src] (Planck Collaboration 2020,
arXiv:2007.04997). The orbital and solar dipoles are the primary absolute
calibrators of satellite data, and ground experiments inherit them by
cross-calibrating against Planck maps on their own footprint (Louis et al.
2025, arXiv:2503.14452; Camphuis et al. 2025, arXiv:2506.20707).

Reviews: Hu & Dodelson 2001, arXiv:astro-ph/0110414; Challinor & Peiris
2009, arXiv:0903.5158 (lecture notes, incl. reionisation secondaries). For lensing:
Lewis & Challinor 2006, arXiv:astro-ph/0601594. For polarisation as a probe
of new physics (birefringence, tensor modes): Komatsu 2022, arXiv:2202.13919.

### The six-parameter base model
<!-- key: the-six-parameter-base-model -->

Base ΛCDM is sampled as {Ω_b h², Ω_c h², θ, n_s, ln(10¹⁰A_s), τ}. The angular
acoustic scale is θ* = r*/D_M(z*), the ratio of the comoving sound horizon at
last scattering to the comoving angular-diameter distance to it. Planck
measures 100θ* = 1.0411 ± 0.0003, a 0.03% determination [src] (Planck
Collaboration 2018, arXiv:1807.06209). H₀, Ω_m and σ₈ are derived parameters
and are model dependent.

Three different "θ" are in circulation and they are not interchangeable at
current precision:

| Symbol | Definition | Used by |
|---|---|---|
| θ_MC | CosmoMC approximation to r*/D_M | Planck 2018 chains, ACT DR6 tables (arXiv:2503.14452) |
| θ* | r*/D_M(z*) with z* where the optical depth equals unity | Planck 2018 abstract, PR4 HiLLiPoP (arXiv:2309.10034) |
| θ_s^⋆ | CLASS definition | SPT-3G D1 tables (arXiv:2506.20707) |

Tristram et al. 2023 (arXiv:2309.10034) state explicitly that the definition
of θ* "differs slightly" between CAMB and CLASS [src]. Compare 10⁴θ only
between tables that use the same code definition.

## 2. What each feature constrains
<!-- key: what-each-feature-constrains -->

| Feature in the spectra | Parameter combination | Remark and source |
|---|---|---|
| Peak positions | θ* | Geometric; the best measured quantity in cosmology (arXiv:1807.06209) |
| Relative peak heights (odd/even, radiation driving) | Ω_b h², Ω_m h² | Break the H₀–Ω_m degeneracy along fixed θ* (arXiv:2503.14452, Sect. VIII.4) |
| Damping tail (ℓ ≳ 1500) | Ω_b h², n_s, N_eff, Y_P | N_eff changes diffusion damping and induces a phase shift (arXiv:2503.14454) |
| Overall amplitude at ℓ ≳ 30 | A_s e^(−2τ) | Reionisation scattering suppresses sub-horizon power by e^(−2τ) |
| Reionisation bump in EE at ℓ ≲ 20 | τ | Amplitude ∝ τ²; only full-sky experiments reach it |
| Smoothing of peaks, transfer of power to the tail | lensing potential amplitude (A_s, Ω_m, Σm_ν) | The "two-point" lensing signature |
| Reconstructed C_L^φφ | σ₈ Ω_m^0.25 | The "four-point" lensing signature |
| Tilt across the whole range | n_s | Needs lever arm; degenerate with Ω_b h² on restricted ranges |

Foundations of the table [src, abstracts]. The peaks are driven acoustic
oscillations of the photon–baryon fluid, and an analytic treatment
reproduces the spectra to 5–10% on all scales (Hu & Sugiyama 1994,
arXiv:astro-ph/9407093); baryon drag produces the alternating peak heights,
and the acoustic amplitudes and diffusion damping lengths are set by the
cosmological parameters (Hu & Sugiyama 1995, arXiv:astro-ph/9510117). The
linear Boltzmann hierarchy for all species in the synchronous and
conformal Newtonian gauges, with a phase-space treatment of photons and
neutrinos, is Ma & Bertschinger 1995 (arXiv:astro-ph/9506072); the
line-of-sight integration that makes spectra fast to compute, a geometric
term times a source term, is Seljak & Zaldarriaga 1996
(arXiv:astro-ph/9603033). Reionisation creates new peaks in the
polarisation spectrum whose position scales as the square root of the
reionisation redshift and whose amplitude is proportional to τ (Zaldarriaga
1996, arXiv:astro-ph/9608050).

Points worth holding precisely, all from the ACT DR6 paper (Louis et al.
2025, arXiv:2503.14452) [src]:

- In ACT data the TE spectrum gives the tightest Ω_b h², Ω_c h² and H₀; TT
  gives the tightest n_s. E-mode polarisation traces the velocity
  perturbation at recombination and has sharper acoustic features than
  intensity.
- The n_s–Ω_b h² correlation changes sign with scale. At Planck scales the
  two are positively correlated (higher Ω_b lowers the second-to-first peak
  ratio, which a redder tilt compensates). In the damping tail both damp
  power, so they are anti-correlated. Combining the two ranges breaks the
  degeneracy; P-ACT reaches 0.4% on each.
- With EE alone on ACT scales, the polarisation efficiency is nearly
  degenerate with Ω_c h²: freeing it in [0.9, 1.1] roughly doubles
  σ(Ω_c h²) and σ(H₀). The mechanism is radiation driving, whose amplitude
  boost depends on the redshift of equality.
- Curvature cannot be measured from unlensed primary spectra (geometric
  degeneracy). Lensing in the spectra, the lensing reconstruction, or BAO
  breaks it.

## 3. Gravitational lensing of the CMB
<!-- key: gravitational-lensing-of-the-cmb -->

Large-scale structure between us and last scattering deflects photons by
the gradient of the lensing potential φ(n), an integral of the Weyl potential
along the line of sight. The observed fields are remapped,
X̃(n) = X(n + ∇φ). ACT describes the lensing kernel as covering z ~ 0.5–5
[src] (Qu et al. 2023, arXiv:2304.05202). The convergence is κ = −∇²φ/2 and
its spectrum is C_L^κκ = [L(L+1)]² C_L^φφ / 4. Capital L is reserved for
lensing multipoles.

Lensing has three observable consequences: it smooths the acoustic peaks and
adds power in the damping tail of TT, TE and EE; it converts E into B; and
it correlates modes of different ℓ, which is what reconstruction exploits.
The first two were computed in the power-spectrum approach by Seljak 1995
(arXiv:astro-ph/9505109): lensing redistributes power and smooths sharp
features [src]. For polarisation the smoothing is larger because the peaks
are narrower, up to 10% at ℓ < 1000, and lensing generates B modes from
pure E (Zaldarriaga & Seljak 1998, arXiv:astro-ph/9803150) [src].

### Quadratic estimators
<!-- key: quadratic-estimators -->

For fixed φ the lensed CMB is statistically anisotropic,
⟨X̃(ℓ₁) Ỹ(ℓ₂)⟩ ∝ f_XY(ℓ₁, ℓ₂) φ(L) with L = ℓ₁ + ℓ₂ ≠ 0. The minimum-variance
quadratic estimator weights pairs of filtered modes by this response (Hu &
Okamoto 2001, arXiv:astro-ph/0111606):

    φ̂(L) = A_L^XY ∫ d²ℓ₁/(2π)²  F_XY(ℓ₁, ℓ₂) X̃(ℓ₁) Ỹ(ℓ₂) − mean field.

The power spectrum of φ̂ is a four-point function and carries additive
biases that must be subtracted:

    ⟨|φ̂_L|²⟩ = C_L^φφ + N_L^(0) + N_L^(1) + foreground and MC terms.

The full-sky minimum-variance estimators for T and polarisation, with
real-space products in place of harmonic convolutions, are Okamoto & Hu
2003 (arXiv:astro-ph/0301031) [src]. Kesden et al. 2003
(arXiv:astro-ph/0302536), the reference ACT gives for N¹ [sec:
arXiv:2304.05202, Sect. V.9], show that the naive power estimator is
biased upwards and give an iterative scheme to remove the bias [src].
Hanson et al. 2010 (arXiv:1008.4403) find the Okamoto–Hu temperature
estimator biased by 15% at L < 250 from beyond-gradient terms [src];
Planck 2018 uses lensed fiducial spectra in the filter so the estimator is
nearly unbiased non-perturbatively, citing that work [src:
arXiv:1807.06210, Sect. 2.1].

N⁰ is the disconnected (Gaussian) term, N¹ the connected term proportional
to C^φφ itself, and the mean field is the response to the mask and to
anisotropic noise. The ACT DR6 pipeline is the current reference
implementation [src] (Qu et al. 2023, arXiv:2304.05202): the night-time
data are split into eight subsets with independent noise and the four-point
estimator uses only cross-correlations between splits, so that it "is immune
to noise bias" and noise simulations are needed only for the covariance; N⁰
is the realisation-dependent RDN0 computed with noiseless simulations; N¹
comes from pairs of simulations sharing a lensing field; the covariance
uses 792 simulations with a Hartlap correction; the baseline range
40 < L < 763 was fixed before unblinding and an extended range 40 < L < 1300
gives a consistent amplitude.

Reconstruction pipelines as run, read in the method sections:

| Step | ACT DR6 (arXiv:2304.05202, 2304.05196) | Planck 2018 (arXiv:1807.06210) | SPT-3G D1 (arXiv:2608.31136) |
|---|---|---|---|
| Input and filter | inverse-variance coadd of f090, f150; diagonal harmonic filter with C_l^tot = C_l^cmb + N_l^coadd [src: 2304.05196, Sect. V.1] | Wiener filter X^WF = C^fid 𝒯† Cov⁻¹ X^dat, Cov = 𝒯 C^fid 𝒯† + N, diagonal pixel noise, conjugate gradient; T and P filtered separately (+3% noise at L ≤ 400); 100 ≤ ℓ ≤ 2048 [src: Sect. 2.1, Eqs. 1–2] | C⁻¹-filtered maps; GMV is the baseline [src: Sect. V.3.3] |
| Estimator | cross-split estimator, profile-hardened MV [src: 2304.05196, Sect. V.1] | Carron & Lewis 2017 spin-1 displacement, split into gradient and curl; T-only, P-only, MV rather than the five Okamoto–Hu pairs; lensed fiducial spectra make it nearly unbiased non-perturbatively [src: Sect. 2.1, Eqs. 3–6] | GMV, with profile-hardened, cross-ILC and tSZ-deprojected variants as checks [src: Sect. V.3.3] |
| Mean field and normalisation | mean field exceeds the signal near L ~ 20, one reason for L_min = 40; normalisation is the inverse response for fiducial spectra (Planck 2015 TT,TE,EE with updated τ); φ is biased by the ratio of fiducial to true response [src: Sects. V.9–V.10] | mean field (map-level signal of mask, noise and anisotropies) subtracted, then normalisation [src: Sect. 2.1] | κ̂ = ½ L(L+1)(φ̄_LM − φ̄_LM^MF)/R̃_L^αφ, mean field over 498 simulations [src: Eqs. 23–24] |
| Bias subtraction | Ĉ_L^φφ,× = C_L^φ̂φ̂,× − ΔC_L^Gauss − ΔC_L^N1 − ΔC_L^MC: RDN0, N¹ by the Story et al. procedure, additive MC term from 480 simulations [src: Eq. 39] | — | Ĉ_L^κκ = C_L^κ̂κ̂ − N_L^(0) − N_L^(1); N⁰ from pairs of independent realisations, N¹ from a second CMB set lensed by the same φ, RDN0 on data [src: Eqs. 25–27] |
| Blinding | baseline L range fixed before unblinding [src] | — | band powers against theory only after simulation-mean, curl, unlensed and ℓ-range tests; parameters after alternate-cosmology and Agora tests and a CMB/BAO consistency check [src: Sect. V.4] |

Variants in use:

| Estimator | Purpose | Reference |
|---|---|---|
| Bias-hardened (source- or profile-hardened) | Null the response to point sources or to cluster-like profiles at small noise cost | Namikawa et al. 2012, arXiv:1209.0091; applied in arXiv:2304.05196 |
| Gradient-cleaned | Use a foreground-cleaned map only in the gradient leg | Madhavacheril & Hill 2018, arXiv:1802.08230 |
| Global minimum variance (GMV) | Jointly optimal weights for T, E, B rather than a sum of pair estimators | used for SPT-3G D1 (Omori et al. 2026, arXiv:2608.31136) |
| Maximum a posteriori (iterative) | Beyond-quadratic optimality at low polarisation noise | Carron & Lewis 2017, arXiv:1704.08230 |
| MUSE (marginal unbiased score expansion) | Joint Bayesian estimate of unlensed EE and φφ band powers with their covariance | Millea & Seljak 2021, arXiv:2112.09354; data: Ge et al. 2024, arXiv:2411.06000 |

Range of validity. Quadratic estimators are close to optimal when the
lensing B-mode power is below the noise; for deep polarisation maps they
lose information, and Carron & Lewis 2017 forecast a factor ≃2 improvement
on σ(r) from delensing with the optimal map in a Stage-4 configuration
(forecast) [src] (arXiv:1704.08230). The SPT-3G D1 reconstruction is
dominated by polarisation information at L ≲ 600 [src]
(arXiv:2608.31136).

### Three lensing amplitudes that must not be confused
<!-- key: three-lensing-amplitudes-that-must-not-be -->

| Symbol | What it rescales | Measured from |
|---|---|---|
| A_L (Planck), A_lens (ACT), A_2pt (SPT) | C_L^φφ only as it enters the lensed TT/TE/EE (peak smoothing) | primary spectra |
| A_recon (SPT), A_lens^recon (Qu et al. 2025) | the predicted reconstructed C_L^φφ | four-point reconstruction |
| A_lens (SPT, joint) | both at once, A_2pt = A_recon | spectra + reconstruction |

A_L was introduced as a consistency parameter by Calabrese et al. 2008
(arXiv:0803.2309): A_L = 0 is unlensed, A_L = 1 the expected lensing. It is
not a physical parameter. The split into A_2pt and A_recon is spelled out in
Camphuis et al. 2025 (arXiv:2506.20707, Sect. VII.2.3). In addition, every
lensing reconstruction paper quotes an amplitude "relative to" a fiducial
model, and the fiducial differs: Planck 2018 best fit for Planck PR4 and ACT
DR6, the P-ACT best fit for the three-experiment combination
(arXiv:2504.20038), the CMB-SPA best fit for SPT-3G D1 (arXiv:2608.31136).

## 4. From time-ordered data to band powers
<!-- key: from-time-ordered-data-to-band-powers -->

Satellite pipelines (Planck) solve for maps with destriping and, for the
latest reprocessings, with explicit templates for instrumental effects:
SRoll2 fits the non-linearity of the HFI analogue-to-digital converters and
polarisation efficiencies from data redundancy (Delouis et al. 2019,
arXiv:1901.11386); NPIPE processes LFI and HFI jointly and delivers 600
end-to-end simulations [src] (arXiv:2007.04997).

Ground pipelines differ in how they treat atmosphere and ground pickup.

- ACT makes maximum-likelihood maps and then removes ground pickup in
  Fourier space, discarding modes with |ℓ_x| < 90 and |ℓ_y| < 50; the
  resulting bias is calibrated on 800 simulations per array-band and
  corrected with a transfer matrix [src] (arXiv:2503.14452, Sect. III.3.1).
- SPT high-pass filters each detector timestream and bins. The filter acts
  mainly in the azimuthal number m. The transfer function is calibrated on
  500 full time-domain simulations ("Fullmock") and 4000 fast ones
  ("Quickmock") [src] (arXiv:2506.20707, Sect. IV; maps in Quan et al. 2026,
  arXiv:2603.20163).

Power spectra are pseudo-C_ℓ cross-spectra between data splits with
independent noise, so that no noise bias has to be subtracted. The MASTER
relation (Hivon et al. 2001, arXiv:astro-ph/0105302)

    ⟨C̃_ℓ⟩ = Σ_ℓ' M_ℓℓ' F_ℓ' B²_ℓ' C_ℓ'

links the masked-sky pseudo-spectrum to the true one through the
mode-coupling matrix M (from the mask), the filter transfer function F and
the beam B. A general public implementation with E/B purification is
NaMaster (Alonso et al. 2018, arXiv:1809.09603). Where the pixel count is
small (low ℓ) the quadratic maximum-likelihood (QML) estimator is used
instead: Tegmark 1996 (arXiv:astro-ph/9611174) introduced it as unbeatable
in variance, quadratic, applicable to any geometry and scaling as n² in
pixels [src]; Bond, Jaffe & Knox 1997 (arXiv:astro-ph/9708203) showed that
the iterated minimum-variance quadratic estimator converges to the
maximum-likelihood C_ℓ [src]; Tegmark & de Oliveira-Costa 2000
(arXiv:astro-ph/0012120) extended it to polarisation with E/B
disentangling on a cut sky [src]. The PR4 large-scale spectra use a
cross-spectrum QML variant at N_side 16 [src: arXiv:2309.10034, Sect. 3.1]. ACT publishes its pipeline
as PSpipe [src] (arXiv:2503.14452). SPT-3G D1 uses HEALPix maps
(Górski et al. 2004, arXiv:astro-ph/0409513), bins in Δℓ = 50 and debiases
for pixel window, transfer function and temperature beam, while the
polarised beam and the quadrupolar temperature-to-polarisation leakage are
left as likelihood-level parameters [src] (arXiv:2506.20707).

Ranges actually used in the 2025 likelihoods [src]:

| Data set | TT | TE, EE | Sky used | Source |
|---|---|---|---|---|
| ACT DR6 | ℓ_min 600–1000 by array-band, ℓ_max 8500 | same ℓ_min after unblinding (500 before) | 10,000 deg² of 19,000 deg² mapped | arXiv:2503.14452 |
| SPT-3G D1 | 400–3000 | 400–4000 | 4% of the sky | arXiv:2506.20707 |
| Planck in P-ACT | ℓ < 1000 | ℓ < 600 | PR3 likelihood masks | arXiv:2503.14452 |
| Planck 2018 Plik | 30–1197 (100), 30–1996 (143), 30–2508 (143×217, 217); no 100×143, 100×217 | 30–999 with 100 GHz, 505–999 or 505–1996 with 217 GHz, 30–1996 (143) [src: Table 13] | half-mission cross-spectra | arXiv:1907.12875, Sect. 3.2.4 |
| Planck PR4 HiLLiPoP | 30–1500 with 100 GHz (250–1500 for 100×217), 50–2000 (143), 250–2500 (143×217, 217) | TE 30–2000, EE 30–2000 (EE 100×100: 100–1200) [src: Table 1] | up to 75%; 29 758 multipoles | arXiv:2309.10034, Sect. 3.2.3 |
| Planck CamSpec (2019 reanalysis) | — | — | 80% | arXiv:1910.00483 |

## 5. Foregrounds and component separation
<!-- key: foregrounds-and-component-separation -->

Two strategies coexist.

Parametric modelling at the spectrum level is the standard for TT/TE/EE
parameter work. Multi-frequency auto- and cross-spectra are fitted with the
CMB plus templates for thermal SZ, kinematic SZ, clustered and Poisson CIB,
the tSZ–CIB correlation, radio sources and Galactic dust. The template set
goes back to the nine-parameter ACT model of Dunkley et al. 2013
(arXiv:1301.0776). Sizes of the current nuisance sectors [src]:

| Likelihood | Nuisance parameters | Source |
|---|---|---|
| ACT DR6 MFLike | 14 foreground, 10 calibration, 5 bandpass shift | arXiv:2503.14452, App. G |
| SPT-3G D1 multi-frequency | 43 in total; 2 in the compressed SPT-lite | arXiv:2506.20707 |
| Planck PR4 HiLLiPoP | 6 inter-calibrations, 7 temperature foreground amplitudes, 1 in polarisation, 3 spectral indices | arXiv:2309.10034 |

Map-level component separation is used for lensing inputs, for Compton-y
and CIB maps, for low-ℓ polarisation and for B-mode searches. Planck 2018
used Commander, NILC, SEVEM and SMICA for the CMB and Commander, GNILC and
SMICA for the astrophysical components, and measured mean polarised
spectral indices β_d = 1.55 ± 0.05 for dust and β_s = −3.1 ± 0.1 for
synchrotron [src] (Planck Collaboration 2018, arXiv:1807.06208). The four
pipelines descend from four method papers [src, abstracts]: a blind
internal linear combination by harmonic band (Tegmark et al. 2003,
arXiv:astro-ph/0302496); SMICA, spectral matching of a multi-component
model to multi-detector spectra (Delabrouille et al. 2002,
arXiv:astro-ph/0211504); NILC, a minimum-variance constrained linear
combination on needlets (Delabrouille et al. 2008, arXiv:0807.0773); and
Commander, joint Bayesian component separation and C_ℓ estimation by Gibbs
sampling (Eriksen et al. 2007, arXiv:0709.1058). For primordial B modes, BICEP/Keck fits a seven-parameter
dust + synchrotron model to all auto- and cross-spectra between its bands
and WMAP and Planck maps from 23 to 353 GHz [src] (BICEP/Keck 2021,
arXiv:2110.00483).

"CMB-only" or "lite" likelihoods compress the multi-frequency data into
foreground-marginalised CMB band powers with a covariance. They are the
right product for combining experiments and for extended models, provided
the marginalisation was done over the multipole range one actually uses:
Jense et al. 2025 (arXiv:2510.09430) show that marginalising CamSpec
foreground parameters after truncating scales can change parameter
inference, and release a CamSpec-NPIPE-lite likelihood for that reason
[src].

## 6. Covariance and likelihood
<!-- key: covariance-and-likelihood -->

High ℓ. All three collaborations use a Gaussian likelihood in the band
powers with a fixed fiducial covariance,

    −2 ln L = (D̂ − D^th)ᵀ Σ⁻¹ (D̂ − D^th) + const.

Plik writes it as −ln L(Ĉ|C(θ)) = ½ [Ĉ − C(θ)]ᵀ Σ⁻¹ [Ĉ − C(θ)] + const.
over all relevant cross-frequency spectra of the 100, 143 and 217 GHz
channels, with Σ for a fiducial model including foregrounds, MASTER-type
treatment of the Galactic mask, a Monte Carlo correction for point-source
masks and a heuristic one for anisotropic noise, foregrounds treated as
Gaussian; the Gaussian shape biases n_s by about 0.1σ through
30 ≤ ℓ < 100 [src: arXiv:1907.12875, Sect. 3.1, Eq. 20]. HiLLiPoP uses the
same form per detset cross-spectrum (Eq. 7) and drops ln|Σ| for a fixed
covariance; it expects χ² with mean n_ℓ − n_p and variance 2(n_ℓ − n_p)
[src: arXiv:2309.10034, Sect. 5.1, Eq. 7].

The covariance is semi-analytic, corrected with simulations. Camphuis et al.
2022 (arXiv:2204.13721) give the exact calculation for small footprints and
find that earlier fast approximations are accurate to about 5% on the SPT-3G
footprint for wide bins, their improved approximation to 1% [src]. Atkins et
al. 2024 (arXiv:2412.07068) find their analytic ACT DR6 prescription within
3% of Monte Carlo, against about 16% for the simpler earlier prescription,
and 1% after a simulation-based correction [src].

Covariance construction as run:

| Analysis | Construction | Place |
|---|---|---|
| ACT DR6 | (1) analytic pseudo-D_ℓ Gaussian term, homogeneous noise; (2) Monte Carlo correction from 1640 simulations for striped noise and the ground filter; (3) beam term ∝ D_ℓ D_ℓ ⟨δB δB/B B⟩ from Uranus, arrays uncorrelated; (4) leakage-beam term from 10 000 simulated leakage beams, +50% on TE errors at ℓ < 800, which motivated the polarisation ℓ cut; (5) non-Gaussian lensing terms incl. super-sample variance; (6) tSZ (halo model) and Poisson-source trispectra. Terms 5–6 change parameter errors by < 10% | [src: arXiv:2503.14452, Sect. III.4] |
| ACT DR6 leakage | Ẽ_ℓm = E_ℓm + γ_ℓ,TE T_ℓm, B̃_ℓm = B_ℓm + γ_ℓ,TB T_ℓm; induced ΔD_ℓ from the best fit subtracted from the spectra | [src: Eqs. 1–2, Sect. III.3.2] |
| SPT-3G D1 | semi-analytic covariance of the pseudo-spectra with mask-coupling kernels of the border-only apodised mask, debiased like the spectra; signal at the best fit; isotropic noise, no anisotropic correction | [src: arXiv:2506.20707, Sect. IV.6, Eqs. 31–33] |
| SPT-3G D1 model operators | super-sample lensing [S(κ)C]_ℓ = C_ℓ − (∂ℓ²C_ℓ/∂ln ℓ) κ/ℓ², κ ~ N(0, 0.00045); aberration [A C]_ℓ = C_ℓ − β_ab ℓ ∂C_ℓ/∂ℓ, β_ab = −0.0004826, CMB only; nine beam eigenmodes; polarised-beam ratio B^T/B^P(β_pol); quadrupolar leakage. Beam errors are parameters here and covariance terms in ACT; Planck 2018 ignores beam-determination uncertainty [src: arXiv:1907.12875, Sect. 3.3.5] | [src: Sect. V.2.1, Eqs. 41–45] |

Low ℓ. At ℓ < 30 the likelihood is non-Gaussian and noise is correlated.
Planck 2018 uses a simulation-based EE likelihood built on the 100×143 GHz
cross-spectrum, labelled "lowE" (arXiv:1907.12875, arXiv:1807.06209). Alternatives tested on SRoll2 maps
include a maximum-entropy approximation (momento) and a density-estimation
scheme (de Belsunce et al. 2021, arXiv:2103.14378). The analytic form for
correlated T and E on a cut sky is Hamimeche & Lewis 2008 (arXiv:0801.0554).

Planck low-ℓ polarisation likelihoods as run [src]. lowE (SimAll, PR3):
QML cross-spectrum of the cleaned 100 and 143 GHz maps, ℓ = 2–29, EE only,
each C_ℓ given an empirical distribution from 300 end-to-end simulations,
ℓ-to-ℓ correlations ignored; low-ℓ TT uses the Commander Blackwell–Rao
likelihood (arXiv:1807.06209, Sect. 2.2.3). LoLLiPoP (PR4): Commander-
cleaned detset cross-spectra, ℓ = 2–30, Hamimeche–Lewis variable change
adapted to cross-spectra as in Mangilli et al. 2015 (arXiv:1503.01347;
cross-spectra remove noise bias [src]):
X_ℓ = √(C_ℓ^f + O_ℓ) g[(C̃_ℓ + O_ℓ)/(C_ℓ + O_ℓ)] √(C_ℓ^f + O_ℓ),
g(x) = √(2(x − ln x − 1)), −2 ln P = Σ X_ℓᵀ M⁻¹_ℓℓ' X_ℓ', offsets from the
noise variance ΔC_ℓ ≡ √(2/(2ℓ+1)) O_ℓ (arXiv:2309.10034, Eqs. 4–6).

The τ input. Ground experiments cannot measure τ and every current analysis
takes it from Planck large-scale polarisation, in one of three ways [src]:

| Analysis | τ information | Source |
|---|---|---|
| ACT DR6 "ACT", "P-ACT", "W-ACT" | SRoll2 low-ℓ EE likelihood; equivalent prior τ = 0.0566 ± 0.0058 | arXiv:2503.14452, Sect. VI.3 |
| SPT-3G D1, "SPT+ACT", "CMB-SPA" | Gaussian prior from the PR4 analysis (NPIPE gives 0.051 ± 0.006) | arXiv:2506.20707, arXiv:2007.04997 |
| Planck 2018 baseline | simulation-based low-ℓ EE likelihood ("lowE") | arXiv:1907.12875 |
| Planck PR4 (Tristram et al.) | LoLLiPoP | arXiv:2309.10034 |

This is a shared dependence: Sailer et al. 2025 (arXiv:2504.16932) call it a
"single-point failure" for analyses that include CMB data. It also means
that ln(10¹⁰A_s) from different papers differs partly because the τ input
differs.

Lensing likelihoods are Gaussian in the C_L^φφ band powers with
perturbative corrections for the dependence of the band powers on
cosmology; Planck 2018 uses the conservative range 8 ≤ L ≤ 400 and neglects
the correlation between the two- and four-point functions [src]
(arXiv:1807.06209, arXiv:1807.06210).

Samplers and theory. Cobaya (Torrado & Lewis 2020, arXiv:2005.05290) is the
common sampler front end. Theory spectra come from CAMB (Lewis et al. 1999,
arXiv:astro-ph/9911177) or CLASS (Blas et al. 2011, arXiv:1104.2933), with
recombination from HyRec (Ali-Haïmoud & Hirata 2010, arXiv:1011.3758) or an
equivalent code. Emulators replace the Boltzmann code inside chains:
CosmoPower (Spurio Mancini et al. 2021, arXiv:2106.03846) runs about 10⁵
times faster than CAMB or CLASS according to the SPT-3G D1 paper [sec]
(arXiv:2506.20707). SPT analyses use candl, a JAX-based differentiable
likelihood (Balkenhol et al. 2024, arXiv:2401.13433).

Accuracy settings matter at DR6/D1 precision. ACT DR6 states that non-linear
corrections to the lensing potential are non-negligible even in the primary
spectra and adopts the dark-matter-only HMcode model rather than Halofit
[src] (arXiv:2503.14454). McCarthy et al. 2021 (arXiv:2103.05582) show that
mis-modelling C_L^κκ can bias H₀ by up to 1.6σ and N_eff by 1.2σ for a
CMB-S4-like survey (forecast) and that default Boltzmann precision settings
are insufficient [src]. SPT-3G D1 uses the ACT DR6 accuracy settings [src].

## 7. Extension parameters as actually defined
<!-- key: extension-parameters-as-actually-defined -->

- N_eff: ρ_rad = ρ_γ [1 + (7/8)(4/11)^(4/3) N_eff]. The standard-model value
  used by ACT DR6 and SPT-3G D1 is 3.044 (arXiv:2506.20707, arXiv:2503.14454); Planck 2018
  used 3.046 (arXiv:1807.06209). ACT notes it had to correct for this small
  difference between its BBN table and CLASS [src]. Constraints quoted with
  "BBN consistency" tie Y_P to (Ω_b h², N_eff); those with Y_P free are
  weaker and should not be compared with them. Physics [src, abstracts]:
  the WMAP+SPT N_eff constraint came almost entirely from the expansion
  rate changing the ratio of the photon diffusion scale to the sound
  horizon, with little from the early ISW effect (Hou et al. 2011,
  arXiv:1104.2333); free-streaming neutrinos also shift the phase of the
  acoustic oscillations (Bashinsky & Seljak 2003, arXiv:astro-ph/0310198),
  first detected in the CMB temperature spectrum by Follin et al. 2015
  (arXiv:1503.07863).
- Σm_ν: base ΛCDM fixes one massive eigenstate with 0.06 eV. When the mass
  is varied, Planck, ACT and DESI use three degenerate states
  (arXiv:2503.14454, arXiv:2503.14744). Limits are 95% one-sided and depend
  on the prior boundary at zero.
- Ω_K < 0 is a closed universe. A_L, A_2pt and A_recon: see Section 3.

## 8. Blinding practice
<!-- key: blinding-practice -->

Blinding is now standard for ground-based power-spectrum work and has not
prevented post-unblinding changes; both must be reported together.

- ACT DR6 used a two-phase procedure: comparison of polarisation spectra
  with Planck was unblinded on 7 December 2023 and cosmological parameters
  on 18 April 2024. After unblinding the minimum multipole in polarisation
  was raised from 500 to the temperature value (600–1000 by array-band),
  motivated by shaped EE null-test residuals and borderline parameter-level
  nulls. About 2000 null tests were run; one array-band (PA4 f150) was
  dropped [src] (arXiv:2503.14452, Sect. IV.1 and App. A–B).
- SPT-3G D1 was unblinded on 9 September 2024 after all pre-defined tests
  passed. Two systematic effects were then identified and modelled:
  quadrupolar temperature-to-polarisation leakage and depolarisation of
  beam sidelobes. The foreground model was also updated [src]
  (arXiv:2506.20707, Sect. VI.1 and App. B).
- ACT DR6 lensing was analysed within a blinded framework with an extensive
  null-test suite, and its baseline multipole range was chosen before
  unblinding [src] (arXiv:2304.05202).

## 9. Public codes and pipelines
<!-- key: public-codes-and-pipelines -->

| Code | Role | Reference |
|---|---|---|
| CAMB, CLASS; HyRec | Einstein–Boltzmann solvers; recombination | arXiv:astro-ph/9911177, arXiv:1104.2933; arXiv:1011.3758 |
| HEALPix | Pixelisation and harmonic transforms | arXiv:astro-ph/0409513 |
| MASTER / NaMaster | Pseudo-C_ℓ estimation | arXiv:astro-ph/0105302, arXiv:1809.09603 |
| PSpipe; MFLike, ACT-lite | ACT DR6 spectrum pipeline; multi-frequency and compressed likelihoods | arXiv:2503.14452 |
| candl, SPT-lite | SPT differentiable likelihood and compressed D1 likelihood | arXiv:2401.13433, arXiv:2506.20707 |
| Plik, CamSpec; CamSpec PR4 | Planck 2018 high-ℓ likelihoods; NPIPE high-ℓ likelihood | arXiv:1907.12875, arXiv:1910.00483; arXiv:2205.10869 |
| HiLLiPoP, LoLLiPoP | PR4 high-ℓ and low-ℓ likelihoods | arXiv:2309.10034 |
| SRoll2 low-ℓ EE | τ likelihood | arXiv:1908.09856 |
| CamSpec-NPIPE-lite | Nuisance-marginalised PR4 | arXiv:2510.09430 |
| Cobaya; CosmoPower | Sampler and likelihood framework; neural emulator of spectra | arXiv:2005.05290; arXiv:2106.03846 |
| LensIt; MUSE | Iterative lensing reconstruction; hierarchical Bayesian lensing + unlensed EE | arXiv:1704.08230; arXiv:2112.09354 |

## 10. Conventions and community splits
<!-- key: conventions-and-community-splits -->

- Planck likelihood. Four high-ℓ products are in use (Plik PR3, CamSpec PR3,
  CamSpec PR4, HiLLiPoP PR4) and three low-ℓ EE products (the 2018 lowE,
  SRoll2, LoLLiPoP). ACT pairs the truncated PR3 likelihood with SRoll2; SPT
  pairs PR3 TT/TE/EE with a PR4 τ prior and PR4 lensing. Jense et al. 2025
  (arXiv:2510.09430) find that for the Planck range retained alongside
  ground data the choice barely matters, and that extended-model
  constraints become insensitive to it once ground data are added [src].
- Name of the combined data set. "P-ACT" is ACT DR6 plus Planck cut at
  ℓ < 1000 (TT) and ℓ < 600 (TE, EE). "CMB-SPA" is SPT-3G D1 + ACT DR6 +
  Planck, each with lensing. They are different objects; P-ACT-LB adds
  lensing and DESI DR1 BAO, P-ACT-LB2 uses DESI DR2 [src] (arXiv:2503.14452,
  arXiv:2506.20707).
- S₈ versus the lensing combination. Lensing papers define
  S₈^CMBL ≡ σ₈(Ω_m/0.3)^0.25 (arXiv:2304.05202) or quote σ₈Ω_m^0.25
  (arXiv:1807.06210, arXiv:2608.31136). Neither is the galaxy-lensing
  S₈ = σ₈(Ω_m/0.3)^0.5.
- Frequency labels. ACT f090/f150/f220 are centred on 98, 150, 220 GHz
  (arXiv:2503.14451); SPT-3G bands are 95, 150, 220 GHz (arXiv:2603.20163).

## Not verified
<!-- key: not-verified -->

- Which Planck likelihood each DESI paper adopts was not re-read; check the
  paper before comparing a DESI+CMB number with an ACT or SPT one.
- Not re-read this session and therefore not quoted: whether Planck
  analyses were blinded; the redshift of last scattering and the rms
  lensing deflection. Plik ranges: closed (Section 4).
- Silk 1968, "Cosmic Black-Body Radiation and Galaxy Formation" (ApJ;
  confirmed on Crossref), is not cited for damping: no abstract readable.
