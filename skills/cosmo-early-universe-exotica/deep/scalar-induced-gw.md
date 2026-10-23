# Scalar-induced gravitational waves: from a curvature spectrum to a PTA fit and a PBH check — cosmo-early-universe-exotica dossier

Scope: how a scalar-induced gravitational-wave (SIGW) interpretation of a
PTA signal is computed and fitted (curvature-spectrum template, induced
kernel, transfer to today, likelihood on the PTA data), how the companion
primordial-black-hole (PBH) abundance is computed to test overproduction
(Press–Schechter on a smoothed density or threshold statistics on the
compaction function), and how non-Gaussianity and the QCD equation of state
change both; what each choice costs and where two analyses disagree.
Snapshot: 2026-10-22.
From: Carr et al. 2026, Sect. VII.1; LISA Cosmology WG 2022, Sect. 10.3; PTA
new-physics papers.

Already in L2, not repeated here: the physical picture and the PBH link in
`physics-and-methods.md#scalar-induced-gravitational-waves`; the NANOGrav
Bayes factors and the 2σ/3σ overproduction verdict in
`results.md#scalar-induced-gravitational-waves`; the source-model and
PBH-tail systematics in
`systematics.md#theory-templates-for-cosmological-backgrounds`; the
distortion test of the SIGW reading in
`open-questions.md#spectral-distortions-what-a-next-generation`. How an
f_PBH(M) exclusion curve is built from microlensing and mergers is in
`deep/primordial-black-holes.md`; the PTA likelihood itself (noise model,
Fourier basis, Bayes factors, optimal statistic) in `deep/sgwb-pta.md`.

## How it is done
<!-- key: how-it-is-done -->

Notation. 𝒫_ℛ(k) (NANOGrav) or 𝒫_ζ(k) (Franciolini et al., EPTA) is the
dimensionless power spectrum of the primordial comoving curvature
perturbation; the two symbols denote the same quantity on super-horizon
scales in these papers. A is the amplitude of its enhanced feature, k_* the
wavenumber of the peak and f = k/(2π a₀) the GW frequency today. Ω_GW(f) is
the GW energy density per logarithmic frequency in units of the critical
density. g_* and g_*,s are the effective numbers of relativistic degrees of
freedom in energy and entropy, evaluated when mode k re-enters the horizon
(superscript 0: today). The equations follow NANOGrav 15 yr new physics
(Afzal et al. 2023, arXiv:2306.16219) unless stated.

### Step 1. Choose a template for the curvature spectrum
<!-- key: step-1-choose-a-template-for-the-curvature -->

The collaborations do not fit an inflation model; they fit shapes "that
reflect the range of possibilities that one may expect in realistic models"
(arXiv:2306.16219) [src: Sect. V.2]:

- sigw-delta: 𝒫_ℛ(k) = A δ(ln k − ln k_*) [src: Eq. 29], two parameters.
- sigw-gauss: 𝒫_ℛ(k) = A/(√(2π) Δ) exp[−(ln k − ln k_*)²/(2Δ²)] [src:
  Eq. 30], a log-normal in linear k with width Δ.
- sigw-box: 𝒫_ℛ = A between k_min and k_max, zero outside [src: Eq. 31].

Franciolini et al. 2023 (arXiv:2306.17149) add a broken power law (BPL),
𝒫_ζ = A (α+β)^γ / [β (k/k_*)^(−α/γ) + α (k/k_*)^(β/γ)]^γ [src: Eq. 1],
where α and β set the growth and decay around the peak and γ its flatness;
they state α ≲ 4, β ≳ 0.5 for quasi-inflection-point models producing
stellar-mass PBHs and β ≳ 2 for curvaton models [src: text after Eq. 1].
EPTA DR2 fits a δ function [src: arXiv:2306.16227, Eq. 25] and a power law
𝒫_ζ = A_ζ^10yr (k/k_10yr)^(n_s−1), normalised at k_10yr = 2π/(10 yr × c)
[src: Eq. 26]; here n_s is a local slope in the PTA band, not the CMB
spectral index.

Why a δ function at all: EPTA calls it "nonphysical" but notes it
approximately describes the maximum GW signal of the steepest possible k⁴
growth of a peak in single-field inflation [src: arXiv:2306.16227, Sect.
4.4]. NANOGrav uses it because an exact analytic Ω_GW exists for it [src:
arXiv:2306.16219, Sect. V.2].

### Step 2. Compute the induced spectrum at production
<!-- key: step-2-compute-the-induced-spectrum-at -->

During radiation domination and for Gaussian perturbations (arXiv:2306.16219)
[src: Eqs. 27–28]:

Ω̄_GW(f) = ∫₀^∞ dv ∫_{|1−v|}^{1+v} du 𝒦(u, v) 𝒫_ℛ(uk) 𝒫_ℛ(vk),

with the kernel

𝒦(u,v) = 3 [4v² − (1+v²−u²)²]² (u²+v²−3)⁴ / (1024 u⁸ v⁸) ×
{ [ln|(3−(u+v)²)/(3−(u−v)²)| − 4uv/(u²+v²−3)]² + π² Θ(u+v−√3) }.

u and v are the wavenumbers of the two scalar modes in units of k; Θ is the
Heaviside function. Ω_GW ∝ 𝒫_ℛ², so the amplitude A enters squared [src:
text after Eq. 28]. For the Gaussian and box templates the double integral
is done numerically; for the δ template an exact expression is used [src:
Sect. V.2]. EPTA writes that expression explicitly with k̃ = k/k_* [src:
arXiv:2306.16227, Eq. 27]: it vanishes for k̃ > 2 (momentum conservation)
and has a resonant π² term for k̃ < 2/√3. For its power-law template EPTA
uses Ω_GW = Q(n_s) (A_ζ^10yr)² (k/k_10yr)^(2(n_s−1)), with Q(n_s)
interpolated from Table 1 of Kohri & Terada 2018 [src: Eq. 28]; the
interpolation range is why its n_s prior stops at [0.4, 2.6] [src: text
after Eq. 30].

Franciolini et al. write the same physics in variables t, s with a transfer
function ℐ²_{t,s} [src: arXiv:2306.17149, Eqs. 6–7]; the two forms are
changes of variables of one integral (the kernel in both is attributed to
the same 2018 papers).

### Step 3. Redshift to today
<!-- key: step-3-redshift-to-today -->

NANOGrav: Ω_GW(f) = Ω_r (g_*(f)/g_*⁰) (g_*,s⁰/g_*,s(f))^(4/3) Ω̄_GW(f) [src:
arXiv:2306.16219, Eq. 26], with Ω_r the radiation density today and the g's
evaluated at horizon re-entry of the mode. Franciolini et al. write h²Ω_GW =
(h²Ω_r/24) (g_*/g_*⁰)(g_*,s/g_*,s⁰)^(−4/3) 𝒫_h(k), with h²Ω_r = 4.2 × 10⁻⁵,
𝒫_h the tensor power spectrum [src: arXiv:2306.17149, Eq. 3], and the
mode–temperature and mode–frequency relations

k = 1.5 × 10⁷ Mpc⁻¹ (g_*/106.75)^(1/2) (g_*,s/106.75)^(−1/3) (T_k/GeV) [src:
Eq. 4]; f = 1.6 nHz (k/10⁶ Mpc⁻¹) [src: Eq. 5].

EPTA multiplies by 2Ω_r⁰ with the g ratios taken against matter–radiation
equality [src: arXiv:2306.16227, Eq. 29] and converts to residual power with
S(f) = H₀² Ω_GW⁰(f)/(8π⁴ f⁵) [src: Eq. 30]. The prefactor conventions
differ between the three papers (Ω_r, Ω_r/24 with 𝒫_h, 2Ω_r), so a
normalisation copied from one paper must be used with that paper's
definition of the integral, not mixed.

### Step 4. Fit the PTA data
<!-- key: step-4-fit-the-pta-data -->

- **Full PTA likelihood.** NANOGrav and EPTA add the SIGW spectrum as a
  common process in the timing-residual likelihood, Hellings–Downs
  correlated, alongside per-pulsar noise; NANOGrav runs each model alone
  and with the SMBHB term (prior in Step 6) [src: arXiv:2306.16219, Sects.
  III, V.2]. EPTA uses 9 Fourier components on DR2new, the most recent 10.3
  yr, and assumes the whole common signal is SIGW [src: arXiv:2306.16227,
  Sect. 4.4].
- **Fit to free-spectrum posteriors.** Franciolini et al. fit the posterior
  of Ω_GW in the 14 NANOGrav bins and 9 EPTA bins; they call this
  "simplified" relative to fitting time delays with pulsar noise and
  correlations, but find it consistent with the collaboration fits [src:
  arXiv:2306.17149, text after Eq. 7]. It neglects astrophysical
  foregrounds.
- **Priors.** NANOGrav: log₁₀ A ∈ [−3, 1], log₁₀(f_*/Hz) ∈ [−11, −5]
  (log-uniform), Δ ∈ [0.1, 3] (uniform), the same frequency range for
  f_min and f_max [src: arXiv:2306.16219, Table 3]. EPTA: log₁₀ A_ζ ∈ [−6,
  3], log₁₀(k_*/Mpc⁻¹) ∈ [4, 12], n_s ∈ [0.4, 2.6], all uniform [src:
  arXiv:2306.16227, Sect. 4.4].

Fits by other groups and to other arrays' data:

- **PPTA DR3, full likelihood** (Han et al. 2024, arXiv:2412.09755, with
  PPTA members): 30 of the 32 pulsars, the PPTA noise models in Enterprise
  through PTArcade, an HD-correlated common process on 15 frequency
  components, H₀ = 67.4, product-space Bayes factors; the curvature
  spectrum comes from a non-minimal-derivative-coupling inflation model
  with three parameters, not a template [src: Sect. III]. Against an SMBHB
  power law (γ = 13/3) the Bayes factor is 0.9: PPTA "is insufficient to
  distinguish between these scenarios" [src: Sect. IV].
- **Three arrays' free spectra** (Liu, Chen & Huang 2023, arXiv:2307.01102):
  the HD free spectra of NANOGrav 15 yr (14 bins), PPTA DR3 (28) and EPTA
  DR2 (24), 66 frequencies from 1.28 to 49.1 nHz, each bin's posterior
  turned into a kernel density and the log-likelihoods summed; the
  integrated bound ∫ h²Ω_GW d ln k ≲ 2.9 × 10⁻⁷ from BAO and CMB is added
  [src: main text].
- **NANOGrav + EPTA free spectra** (Figueroa et al. 2023, arXiv:2307.02399):
  the two sets treated as independent "though we acknowledge the impact of
  overlapping pulsars"; Gaussian kernel smoothing of free-spectrum chains,
  bins independent, templates averaged over bins of width Δf = 1/T because
  SIGW spectra vary on scales finer than the resolution, and a flat
  white-noise-like component added to every model so that the
  high-frequency bins are absorbed; PolyChord through Cobaya [src: main
  text; SM Sect. I].
- **NANOGrav only, many models** (Ellis et al. 2023, arXiv:2308.08546):
  best fits ranked by BIC = −2ℓ + k ln 14 against SMBHBs with environmental
  effects [src: Table 1].
- **Broken power law on three arrays** (Cai et al. 2023, arXiv:2306.17822):
  a parametrised BPL for Ω_GW fitted to NANOGrav, PPTA and EPTA [src:
  abstract]. Bian et al. 2023 (arXiv:2307.02376) fit the HD free spectra of
  EPTA, PPTA and NANOGrav with SIGW and other sources and find "no strong
  preference for any specific SGWB source" [src: abstract].
- One date-limited search (2024 onwards) found no SIGW fit to MPTA or CPTA
  data.

### Step 5. Compute the PBH abundance of the same spectrum
<!-- key: step-5-compute-the-pbh-abundance-of-the-same -->

Two prescriptions are in use.

**(a) Press–Schechter on a smoothed density (NANOGrav, App. C.2).**
f_PBH = ∫ (dM/M) f(M) [src: Eq. C4], with

f(M) ≃ γ^(3/2) (β(M)/1.6 × 10⁻⁹) (10.75/g_*(T))^(1/4) (0.12/Ω_DM h²)
(M_⊙/M)^(1/2) [src: Eq. C5],

where γ is the ratio of PBH mass to horizon mass and β(M) the mass fraction
collapsing at formation; M = γ M_H ≃ γ M_⊙ (g_*/10.75)^(−1/6) (4.2 × 10⁶
Mpc⁻¹/k)² [src: Eq. C6]. For Gaussian density fluctuations β(M) =
∫_{δ_c} dδ/(√(2π)σ) exp(−δ²/2σ²) ≃ σ/(√(2π) δ_c) exp(−δ_c²/2σ²) [src:
Eq. C7], with σ² = (16/81) ∫ (dq/q)(q/k)⁴ W²(q/k) 𝒯²(q, 1/k) 𝒫_ℛ(q)
[src: Eq. C8], W the window function and 𝒯 the radiation-era transfer
function [src: Eq. C9]. Choices: γ = 0.356, δ_c = 0.45 for all three
templates "for computational reasons", Gaussian window W(x) = e^(−x²/2)
[src: App. C.2].

**(b) Threshold statistics on the compaction function (Franciolini et al.).**
The compaction 𝒞 is twice the local mass excess over the areal radius,
evaluated at the radius r_m where it peaks [src: arXiv:2306.17149, Eq. S3].
Steps: (i) solve ∫ (dk/k)[(k²r_m² − 1) sin(kr_m)/(kr_m) + cos(kr_m)]
𝒫_ζ^T(k) = 0 for r_m [src: Eq. S4], 𝒫_ζ^T being 𝒫_ζ times the squared
radiation transfer function; (ii) get the shape parameter α_s from Eq. S5;
(iii) get the threshold δ_th from α_s [src: Eq. S6]; (iv) include the
non-linear curvature–density relation δ = −(2/3)Φ (aH)⁻² e^(−2ζ)[∇²ζ +
½ ∂_iζ ∂_iζ], with Φ = 3(1+w)/(5+3w) for constant equation of state w [src:
Eq. 9], so that 𝒞 = 𝒞₁ − 𝒞₁²/(4Φ) with 𝒞₁ the linear compaction [src:
text after Eq. 16]; (v) integrate the joint Gaussian distribution of
(𝒞_G, ζ_G) over the collapsing domain with the critical-collapse factor
𝒦(𝒞 − 𝒞_th)^γ [src: Eqs. 16–17]; (vi) sum over horizon masses with f_PBH ∝
∫ d ln M_H (M_H/M_⊙)^(−1/2) (g_*/106.75)^(3/4) (g_*,s/106.75)^(−1)
β(M_H)/(7.9 × 10⁻¹⁰) [src: Eq. 14]. Near the QCD epoch γ, 𝒦, 𝒞_th and Φ
are taken as functions of horizon mass [src: text after Eq. 18].

Why the threshold depends on the spectrum: narrower spectra raise δ_th by up
to ~20% because fewer modes take part in the collapse and pressure gradients
are larger [src: SM Sect. II].

### Step 6. Report
<!-- key: step-6-report -->

NANOGrav reports three kinds of output [src: arXiv:2306.16219, Sect. V.2,
App. A]: Bayes factors against the SMBHB-only model; 95% lower limits on A
from highest-posterior-density intervals; and exclusion regions where the K
ratio, K(θ) = P(D|θ)/P(D|θ₀) — the likelihood at θ over the likelihood
without the new-physics signal — falls below 1/10 [src: Eq. A5]. The K
regions hold "independent of the origin of the NANOGrav signal" and, being a
likelihood ratio, are "robust against our prior assumptions" [src: Sect.
V.2; App. A]. The SMBHB prior is a bivariate normal in (log₁₀ A_BHB, γ_BHB)
with mean (−15.6, 4.7) [src: Eq. A1], fitted to population simulations. The
f_PBH = 1 contour is overlaid on the posterior, not folded into it [src:
Figs. 6–7 captions].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Template shape
<!-- key: template-shape -->

- δ and Gaussian are nested (Δ → 0), so their posteriors in (A, f_*) are
  similar, the Gaussian slightly broader [src: arXiv:2306.16219, Sect.
  V.2]. The box needs f_max marginalised, so no K bound can be placed in
  the (A, f_min) plane: the signal can be made arbitrarily small by f_max →
  f_min [src: Sect. V.2].
- With BPL and log-normal shapes, the posteriors depend weakly on shape as
  long as the spectrum is narrow on the infrared side, α ≳ 1.1 and Δ ≲ 2.1
  at 2σ [src: arXiv:2306.17149, text after Eq. 7].
- What all fits share: the data are fitted by the low-frequency tail of the
  spectrum, with the peak above the band; posteriors on f_* extend to the
  prior edge and A and f_* are degenerate along a line that moves the peak
  without changing the tail [src: arXiv:2306.16219, Sect. V.2]. EPTA finds
  the same degeneracy and can quote only lower limits, log₁₀(k_*/Mpc⁻¹) >
  7.6 and log₁₀ A_ζ > −1.7 (5% quantiles) [src: arXiv:2306.16227, Sect.
  4.4]; Franciolini et al. have k_* ≥ 2 × 10⁷ Mpc⁻¹ at 2σ [src:
  arXiv:2306.17149, text after Eq. 8].
- Degeneracy with SMBHBs: a δ-function SIGW injected and recovered with a
  power law gives γ ≈ 3.5 for large k_*, consistent both with EPTA's fitted
  slope and with 13/3 [src: arXiv:2306.16227, Sect. 4.4, Fig. 19].

### Which data, which likelihood
<!-- key: which-data-which-likelihood -->

- **Full likelihood** (NANOGrav, EPTA, the PPTA DR3 fit) keeps pulsar noise
  and correlations; **free-spectrum fits** (Franciolini et al., Liu et al.,
  Figueroa et al., Ellis et al.) are fast enough for many models and for
  combining arrays, but assume independent bins, and combining NANOGrav
  with EPTA as independent double-counts the shared pulsars, which
  Figueroa et al. acknowledge [src: arXiv:2307.02399, main text].
- **Evidence differs by array.** Against the NANOGrav SMBHB prior, Figueroa
  et al. find Gaussian SIGW bump BF = 120 (NANOGrav) and 15 (EPTA), the
  non-Gaussian bump 66 and 8.7, and a plain power law with n_t = 2/3 only
  ~2–3; they add that these depend on modelling assumptions [src:
  arXiv:2307.02399, Table 1 and text]. On PPTA DR3 a model-based SIGW
  spectrum has BF 0.9 against SMBHBs [src: arXiv:2412.09755, Sect. IV].
  Ellis et al. give the SIGW best fit k_* = 10^7.7 Mpc⁻¹, A = 0.06, Δ =
  0.21 with ΔBIC = −2.1 (5.8 when SMBHBs are added), while phase
  transitions and domain walls fit better (−4.9, −5.7) [src:
  arXiv:2308.08546, Table 1].

### Press–Schechter or compaction thresholds
<!-- key: press-schechter-or-compaction-thresholds -->

Cost of (a): one fixed δ_c and a Gaussian window. Franciolini et al. find
that NANOGrav's PBH bounds differ from theirs because NANOGrav omits critical
collapse and the non-linear ζ–δ relation, uses a threshold independent of
the spectrum, and a Gaussian window "incompatible with their choice of
threshold"; QCD corrections are a minor further difference [src:
arXiv:2306.17149, closing paragraph before Conclusions]. NANOGrav itself
warns that "slight changes in the computational strategy may result in very
different results for f_PBH" and that the bounds should be "treated with
caution" [src: arXiv:2306.16219, Sect. V.2], and lists the same caveats
(threshold depends on spectrum and window, QCD equation of state ignored)
[src: App. C.2].

Cost of (b): numerical solution of Eqs. S4–S6 for every spectrum. Peak
theory and threshold statistics still differ slightly; peak theory gives
slightly smaller amplitudes, so Franciolini et al. call their threshold-
statistics conclusions conservative [src: arXiv:2306.17149, footnote 1].

Outcome on the same data: NANOGrav leaves small regions where f_PBH = 1
lies inside the 68% credible region for sigw-delta and sigw-gauss [src:
arXiv:2306.16219, Sect. V.2]; Franciolini et al. find that even without
primordial non-Gaussianity the region avoiding overproduction is excluded at
over 2σ by NANOGrav 15 yr (EPTA less constraining) [src: arXiv:2306.17149,
discussion of Fig. 3].

### Primordial non-Gaussianity
<!-- key: primordial-non-gaussianity -->

ζ = F(ζ_G) relates the curvature field to a Gaussian one [src:
arXiv:2306.17149, Eq. 10]. Options:

- Quadratic: ζ = ζ_G + (3/5) f_NL ζ_G² [src: Eq. 11].
- Quasi-inflection point (ultra-slow roll then constant roll): ζ =
  −(2/β) log(1 − β ζ_G/2), β being the large-k slope of the spectrum [src:
  Eq. 12].
- Curvaton: ζ = log X(r_dec, ζ_G), r_dec setting the curvaton's share at
  decay [src: Eq. 13].

Effect on the GW side: the leading-order Ω_GW is kept; the next-order
correction scales as A(3f_NL/5)², and both signs of f_NL raise Ω_GW; the
perturbative regime holds while A(3f_NL/5)² ≪ 1 [src: text after Eq. 7].
Effect on the PBH side: quasi-inflection-point non-Gaussianity assists
collapse and pushes the overproduction limit below the 3σ region of
NANOGrav; curvaton models with r_dec ≳ 0.9 or f_NL ≈ −2 suppress PBHs and
relax the tension [src: discussion of Fig. 3]. Two independent bounds on
local non-Gaussianity at PTA scales, each in its authors' notation:
|f_nl| ≲ 2.34 at 95% from NANOGrav + EPTA (arXiv:2307.02399) [src:
abstract]; |F_NL| ≲ 13.9 for a log-normal spectrum from NANOGrav + PPTA +
EPTA, and −13.9 ≲ F_NL ≲ −0.1 to avoid PBH overproduction
(arXiv:2307.01102) [src: abstract]. NANOGrav, with Gaussian
perturbations only, notes that non-Gaussianity "can dramatically affect the
PBH bounds" [src: arXiv:2306.16219, App. C.2].

The critique (Iovino et al. 2024, arXiv:2412.06764): with ζ = −μ ln|1 −
ζ_g/μ| (μ ≈ 1.5–6.6 in ultra-slow roll, O(0.1) for curvatons; f_NL =
5/(6μ)) [src: Eq. 8 and text], the super-horizon source carries a factor
|1 − ζ_g/μ|^(2(μ−1)) [src: Eq. 9]; μ = 1, i.e. f_NL = 5/6, reproduces
exactly the Gaussian quadratic source [src: text after Eq. 11]. Their
estimate multiplies the standard integral by 𝒜⁴, 𝒜 = |1 ∓ ⟨ζ_g²⟩^(1/2)/μ|⁻¹
[src: Eqs. 16, 18], so Ω_GW can be enhanced when ⟨ζ_g²⟩^(1/2) ~ μ ≪ 1 or
suppressed when it is ≫ μ, effects that an f_NL expansion does not capture
[src: text after Eq. 11]. They present this as an estimate, not a full
calculation [src: text before Eq. 12].

### Radiation domination or the QCD equation of state
<!-- key: radiation-domination-or-the-qcd-equation-of -->

Both PTA collaborations and Franciolini et al. assume perfect radiation
domination for the GW integral [src: arXiv:2306.17149, text after Eq. 7;
arXiv:2306.16219, App. C.2]. During the QCD crossover w(T) = (4/3)(g_*,s/g_*)
− 1 dips [src: arXiv:2306.17136, Sect. II], which changes the infrared
("causality") tail of any causal GW source: for constant w the tail scales
as f^(3 + 2(3w−1)/(3w+1)) [src: Eq. 2], and modes re-entering at the
crossover land at f ≃ 3.0 nHz (g_*,s/20)^(1/6)(T/150 MeV) [src: Eq. 3]. Fitted
to NANOGrav 15 yr (14 bins, autocorrelations only), the QCD-modified tail
beats a pure f³ tail with log₁₀ B = 1.0 [src: Sect. IV, Table 1]. For SIGWs
the k³ causality tail alone is disfavoured by over 3σ, a tension that "may be
relieved by QCD effects" [src: arXiv:2306.17149, text after Eq. 8]. On the
PBH side, the QCD-induced enhancement of f_PBH near k_* ≈ 10⁷ Mpc⁻¹ is
negligible for the NANOGrav-preferred region [src: discussion of Fig. 3].

### Inflation-side consistency
<!-- key: inflation-side-consistency -->

A claimed no-go theorem says that large small-scale enhancements in single-
field inflation produce one-loop corrections exceeding A_s at CMB scales,
which would require log₁₀ A ≪ −2 and clash with the fitted lower limits;
NANOGrav reports this claim as debated [src: arXiv:2306.16219, Sect. V.2].
A 2026 lattice study of a scalar Gauss–Bonnet ultra-slow-roll model finds
lattice spectra above perturbative ones, with corrections significant once
the peak reaches ~10⁻² (Chen et al. 2026, arXiv:2608.20219) [src: abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| SIGW priors | log₁₀ A ∈ [−3, 1]; log₁₀ f_* (Hz) ∈ [−11, −5]; Δ ∈ [0.1, 3] | NANOGrav 15 yr | arXiv:2306.16219 | Table 3 |
| 95% lower limits on A | log₁₀ A ≳ −1.55 (delta), −1.43 (gauss), −1.90 (box) | NANOGrav 15 yr | arXiv:2306.16219 | Sect. V.2 |
| Posterior, sigw-gauss | log₁₀ A = −0.38 ± 0.58; log₁₀ f_* = −6.32 ± 0.71; Δ = 1.35 ± 0.70 (Bayes estimator ± s.d.) | NANOGrav 15 yr | arXiv:2306.16219 | Table 4 |
| Posterior, sigw-box | log₁₀ A = −1.06 ± 0.52; log₁₀ f_min = −7.34 ± 0.48 | NANOGrav 15 yr | arXiv:2306.16219 | Table 4 |
| PBH settings | γ = 0.356; δ_c = 0.45 (range 0.4–0.6); Gaussian window | NANOGrav PS | arXiv:2306.16219 | App. C.2 |
| SMBHB prior | (log₁₀ A_BHB, γ_BHB) normal, mean (−15.6, 4.7) | NANOGrav | arXiv:2306.16219 | Eq. A1 |
| Exclusion criterion | K < 1/10 | NANOGrav | arXiv:2306.16219 | Eq. A5 |
| EPTA priors | log₁₀ A_ζ ∈ [−6, 3]; log₁₀ k_* ∈ [4, 12]; n_s ∈ [0.4, 2.6] | EPTA DR2new | arXiv:2306.16227 | Sect. 4.4 |
| EPTA power-law fit | log₁₀ A_ζ = −2.94 (+0.42/−0.46); n_s = 2.11 (+0.25/−0.32) (68%) | EPTA DR2new | arXiv:2306.16227 | Sect. 4.4 |
| EPTA δ-template limits | log₁₀ k_* > 7.6, log₁₀ A_ζ > −1.7 (5% quantiles) | EPTA DR2new | arXiv:2306.16227 | Sect. 4.4 |
| Shape insensitivity | α ≳ 1.1 (BPL), Δ ≲ 2.1 (LN) at 2σ | NANOGrav + EPTA fit | arXiv:2306.17149 | text after Eq. 7 |
| Peak location | k_* ≥ 2 × 10⁷ Mpc⁻¹ (2σ) | same | arXiv:2306.17149 | text after Eq. 8 |
| Threshold shift with width | up to ~20% higher for narrow spectra | compaction method | arXiv:2306.17149 | SM Sect. II |
| Perturbativity of NG | A(3f_NL/5)² ≪ 1 | — | arXiv:2306.17149 | text after Eq. 7 |
| Radiation today | h²Ω_r = 4.2 × 10⁻⁵ | — | arXiv:2306.17149 | text after Eq. 3 |
| SIGW BF vs SMBHB | gSIGW bump 120 (NG15), 15 (EPTA); ngSIGW 66, 8.7 | NG15 + EPTA free spectra | arXiv:2307.02399 | Table 1 text |
| SIGW BF vs SMBHB | 0.9 (inflation-model spectrum) | PPTA DR3, 15 bins | arXiv:2412.09755 | Sect. IV |
| SIGW best fit | k_* = 10^7.7 Mpc⁻¹, A = 0.06, Δ = 0.21; ΔBIC −2.1 | NG15, Ellis et al. | arXiv:2308.08546 | Table 1 |
| Joint free spectrum | 66 bins, 1.28–49.1 nHz (NG15 14, PPTA 28, EPTA 24) | three arrays | arXiv:2307.01102 | main text |
| Local NG bounds | abs(f_nl) ≲ 2.34 (95%); abs(F_NL) ≲ 13.9, −13.9 ≲ F_NL ≲ −0.1 without PBH overproduction | NG15+EPTA; NG15+PPTA+EPTA | arXiv:2307.02399; arXiv:2307.01102 | abstracts |
| QCD tail versus f³ | log₁₀ B = 1.0 (NG15), 0.8 (IPTA DR2) | causality tail | arXiv:2306.17136 | Table 1 |
| CMB-driven limit on a QCD-epoch tail | new data sets: excluded at 3σ only for f_CT ≳ 100 nHz, affected for ≳ 50 nHz; IPTA DR2 decisively disfavours f_CT ≳ 32 nHz | causality tail + ΔN_eff | arXiv:2306.17136 | Sect. IV |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Peak outside the band.** The fit constrains only the infrared tail; a
  quoted "best-fit k_*" or "PBH mass" sits on a prior edge. Test: report the
  prior range and the (A, f_*) degeneracy; NANOGrav's maximum-posterior f_*
  for sigw-delta is the prior boundary 10⁻⁵ Hz [src: arXiv:2306.16219,
  Table 4].
- **f_PBH from a Gaussian-window Press–Schechter with fixed δ_c.** Shows up
  as PBH bounds that differ from compaction-based ones on the same posterior
  [src: arXiv:2306.17149]. Test: recompute with the spectrum-dependent
  threshold of Eqs. S4–S6 and the non-linear relation (Eq. 9).
- **Non-Gaussianity ignored on one side only.** Gaussian Ω_GW combined with
  non-Gaussian β(M), or the reverse, mixes models. Test: state F(ζ_G) and
  apply it to both; check A(3f_NL/5)² ≪ 1 [src: arXiv:2306.17149], and for
  log-type models note that f_NL truncation can miss order-one changes of
  Ω_GW [src: arXiv:2412.06764].
- **Pure radiation domination near T ~ 0.1–1 GeV.** The infrared tail shape
  at nHz is altered by the QCD crossover [src: arXiv:2306.17136, Sect. II].
  Test: use tabulated g_*(T), g_*,s(T) and w(T) from lattice QCD, as that
  paper does.
- **Mixed normalisations.** Ω_r versus Ω_r/24 × 𝒫_h versus 2Ω_r prefactors
  (Step 3). Test: reproduce one published curve before fitting.
- **Bayes factor read as evidence.** Each SIGW Bayes factor depends on the
  SMBHB prior (Eq. A1). Test: quote K-ratio exclusions, which are prior-
  robust [src: arXiv:2306.16219, App. A].
- **Extra radiation.** A primordial background counts toward N_eff. For
  NANOGrav 15 yr frequencies the contribution is negligible; projected PTAs
  reaching 1 μHz could produce a ΔN_eff detectable by Simons Observatory
  for SIGWs (Ben-Dayan et al. 2025, arXiv:2508.15134) [src: abstract] —
  **forecast**.

## Reading list
<!-- key: reading-list -->

- Method and application: Afzal et al. 2023, arXiv:2306.16219 — templates,
  kernel, priors, K-ratio exclusions, Press–Schechter f_PBH (Sect. V.2,
  App. A, C.2).
- Application: Antoniadis et al. 2023, arXiv:2306.16227 — EPTA δ and
  power-law templates, the δ–SMBHB slope degeneracy (Sect. 4.4).
- Method and critique: Franciolini et al. 2023, arXiv:2306.17149 —
  compaction-function thresholds, non-Gaussian models, why NANOGrav's PBH
  bounds differ.
- Critique: Iovino et al. 2024, arXiv:2412.06764 — limits of the f_NL
  expansion for the GW source.
- Method: Franciolini, Racco & Rompineve 2023, arXiv:2306.17136 — QCD
  crossover in the causality tail and its Bayes factor on PTA data.
- Foundation: Ananda et al. 2006, arXiv:gr-qc/0612013, and Kohri & Terada
  2018, arXiv:1804.08577 — the second-order source and the analytic kernel
  (abstracts read for L2).
- Application: Han et al. 2024, arXiv:2412.09755 — full-likelihood SIGW fit
  to PPTA DR3.
- Application: Liu, Chen & Huang 2023, arXiv:2307.01102 — joint NANOGrav,
  PPTA, EPTA free-spectrum fit; non-Gaussianity bound.
- Application: Figueroa et al. 2023, arXiv:2307.02399 — NANOGrav + EPTA,
  many sources, Bayes factors and AIC, bin smoothing.
- Comparison: Ellis et al. 2023, arXiv:2308.08546 — multi-model BIC ranking
  on NANOGrav 15 yr.
- Application: Cai et al. 2023, arXiv:2306.17822; Bian et al. 2023,
  arXiv:2307.02376 — broken-power-law and multi-source fits (abstracts).
- Critique: Chen et al. 2026, arXiv:2608.20219 — lattice versus
  perturbative curvature spectra (abstract only).

## Not verified
<!-- key: not-verified -->

- The Kohri & Terada 2018 body (kernel derivation, Table 1 of Q(n_s)) was
  not read; its use is reported through arXiv:2306.16227 and
  arXiv:2306.16219.
- NANOGrav's Eq. 17 (the redshift factors) and Eq. 10 (K-ratio definition)
  were read only as reused in Eq. 26 and App. A.
- The numerical values of 𝒦, γ and Φ near the QCD epoch used by
  Franciolini et al. (their Ref. [227]) and the curvaton function
  X(r_dec, ζ_G) (their Eq. S7) were not read.
- The one-loop no-go papers and their rebuttals cited by NANOGrav were not
  read; no identifiers recorded.
- No SIGW fit to MPTA, CPTA or the five-array combination was found (one
  search, 2024 onwards); fits to IPTA data were not searched separately.
- Bodies of arXiv:2306.17822 and arXiv:2307.02376 (abstracts only); the
  Liu et al. kernel-density details and the Ellis et al. SIGW section.
