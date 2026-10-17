# Strong-lensing substructure — cosmo-neutrinos-dark-matter dossier

Scope: how a dark-matter limit is produced from quadruply imaged quasars
(flux measurement, forward model of halo populations, per-lens likelihood,
combination over lenses, conversion to a particle mass), and how to choose
between likelihood constructions, macromodel freedoms and subhalo-abundance
priors.
Snapshot: 2026-10-17.
From: Snowmass 2021 halo-measurements white paper (Bechtol et al.,
arXiv:2203.07354), Sects. 4.2.1 and 5.2.4.

Already in L2, not repeated here: the subhalo-abundance priors, tidal model,
source sizes, macromodel components and M_hm prior range with their effect
on the limit in `systematics.md#strong-lensing-flux-ratios-and-arcs` and
`systematics.md#dark-matter-budgets-by-analysis-read-in-paper`; the
half-mode-to-keV relations and the confidence criteria in
`physics-and-methods.md#half-mode-scale-and-the-kev-conversion`; the
headline limits and their history in
`results.md#milky-way-satellites-strong-lensing-stellar` and
`results.md#thermal-relic-warm-dark-matter-mass-strong`.

## How it is done
<!-- key: how-it-is-done -->

The notation follows Gilman et al. 2025 (arXiv:2511.07513), the JWST
analysis with arcs; the 2019 eight-lens analysis (Gilman et al. 2019,
arXiv:1908.06983) uses the same structure with ABC.

### Step 1. Measure flux ratios free of microlensing
<!-- key: step-1-measure-flux-ratios-free-of-microlensing -->

Stars in the lens galaxy act on scales of order microarcseconds, so the
emission used must be much larger than that [src: arXiv:2511.07765,
Sect. V]. Two kinds of source are in use:

| Source | Size | Why | Place read |
|---|---|---|---|
| Warm dust, rest frame ~8–12 μm, ~hundreds of K | ~0.5–10 pc, little dependence on luminosity, ~mas | not microlensed | arXiv:2511.07765, Sect. V |
| Hot dust, ~1500 K, sublimation zone | 0.05–0.2 pc at 10⁴⁴–10⁴⁵ erg/s | can be microlensed; modelled and removed | same |
| Nuclear narrow-line region | sampled 20–80 pc FWHM in the model | not microlensed; older samples | arXiv:2511.07513, Sect. V.4 |

The JWST MIRI fluxes are measured by forward-modelling each image as a point
source with a webbpsf PSF (temperature and jitter fitted; in F560W a free
fractional weight f of the cruciform artefact), jointly with a lensed
Sérsic host (shapelets where needed) and an elliptical Sérsic lens with
index fixed to 4, in lenstronomy; the lens-model constraint on the image
positions is relaxed in the last step "to reduce the dependence of the
measured fluxes on the underlying lens model" [src: arXiv:2511.07765,
Sect. III].

The warm-dust flux is then separated by a three-component SED fit per
image: a power law νF_ν ∝ ν^β_q with β_q in [−0.8, 0] around the typical
−0.3 (range widened "to account for distortions in the continuum due to
microlensing"), and hot and warm blackbodies whose amplitudes may differ
between images [src: Sect. V]. The hot-dust temperature prior was raised
from 900–1600 K to a lower limit of 1200 K because several systems drove
the warm-dust flux to zero; all 31 lenses were refitted and these flux
ratios supersede the earlier ones [src: Sect. V]. Flux-ratio uncertainties
are dominated by the PSF and host model and are treated as Gaussian; the
mean and covariance come from 1000 MCMC draws (emcee) [src: Sect. V].

### Step 2. Define the hyper-parameters q
<!-- key: step-2-define-the-hyper-parameters-q -->

q is a set of population parameters that do not map one-to-one onto
observables but set the distribution of halo realisations r [src:
arXiv:2511.07513, Sect. II]. In the 2025 analyses:

| Symbol | Meaning | Sampling distribution | Place read |
|---|---|---|---|
| m_hm | half-mode mass | log10 m_hm/M⊙ uniform in [4, 10] | arXiv:2511.07513, Sect. IV.3 |
| Σ_sub | infall subhalo mass-function amplitude, kpc⁻², common to all lenses | log10 Σ_sub uniform in [−2.2, 0.2] | same |
| α | logarithmic slope of the subhalo mass function | uniform [−1.95, −1.85] | same |
| δ_LOS | amplitude of the line-of-sight halo mass function relative to Sheth–Tormen | uniform [0.9, 1.1] | same |
| m_host | host halo mass, per lens nuisance | log10 m_host/M⊙ ~ N(13.3, 0.3), marginalised per lens before the product | same |

The narrow ranges on α and δ_LOS are justified as "very robust predictions
of collisionless dark matter above the free-streaming scale"; Σ_sub is
wide because of tidal-evolution uncertainty, and was extended upward
relative to earlier analyses "to test the dependence of the results on the
prior" [src: Sect. IV.3]. Sect. IV.1.1 of the same paper describes δ_LOS
as allowing "up to 20%" differences, against 10% in Sect. IV.3 [src: both
places]; the sampling range [0.9, 1.1] is the operative statement.

### Step 3. Render halo populations
<!-- key: step-3-render-halo-populations -->

For each draw of q, pyHalo generates a realisation [src: arXiv:2511.07513,
Sects. II, IV.1]:

- **Mass range.** 10⁶–10^10.7 M⊙ (m_200 relative to ρ_crit at the halo
  redshift, or at infall for subhaloes). Below 10⁶ M⊙ haloes are too small
  to affect the flux ratios for the source sizes used; above 10^10.7 M⊙
  they would usually host visible light and are modelled explicitly
  [src: Sect. IV.1]. Earlier work stopped at 10¹⁰ M⊙ [src: Sect. VII.1].
- **Field haloes.** Double cone opening to six Einstein radii, planes
  every Δz = 0.02, uniform positions; mass function
  d²N/dm dV = δ_LOS [1 + ξ(m_host, z_d)] d²N_ST/dm dV (Eq. 13), where
  ξ is the two-halo term of the group host, adding ~20% haloes near the
  deflector, computed with colossus [src: Sect. IV.1.1]. Profiles are
  truncated NFW (Eq. 14) with the Diemer–Joyce concentration and 0.2 dex
  scatter, truncated at r_200.
- **Negative convergence sheets.** Each plane gets
  κ_⟨m⟩ = ⟨m⟩/(Σ_crit A) so that light rays travel straight on average;
  without it the model acquires a bending towards the mass centre that
  grows with substructure [src: Sect. IV.1.1]. In WDM ⟨m⟩ uses the
  suppressed mass function [src: footnote 13].
- **Subhaloes.** Uniform in projection out to 3θ_E (θ_E ≪ host r_s);
  infall mass function d²N/dm dA = (Σ_sub/m_0)(m/m_0)^(−α) F(m_host, z)
  with m_0 = 10⁸ M⊙ (Eq. 15) and
  F = (m_host/10¹³ M⊙)^k1 (z + 0.5)^k2, k1 = 0.55, k2 = 0.37, calibrated
  on galacticus (Eq. 16) [src: Sect. IV.1.2]. Each subhalo gets an infall
  redshift, an infall concentration, a bound-mass fraction drawn from
  p(f_bound | c, z_infall, c_host) of the Du et al. tidal model, then a
  truncation radius and normalisation factor f_t from tidal tracks; most
  subhaloes have lost over 90% of their infall mass [src: same].
- **WDM.** Halo and subhalo abundances and concentrations are suppressed
  (relations in L2); WDM subhaloes lose more mass because of their lower
  infall concentration, an extra suppression of the bound mass function
  [src: Sects. IV.1.2, IV.2, Fig. 4 caption].
- **Globular clusters** are rendered as an additional perturber class
  [src: Sects. IV.4, VII.1].

### Step 4. Solve the lens equation for each realisation
<!-- key: step-4-solve-the-lens-equation-for-each -->

Image positions are known to ~5 mas, so random macromodels almost never
match them. For each realisation a subset of macromodel parameters is
solved for (COBYQA) so that the lens equation holds at the observed
positions plus a random 5 mas perturbation [src: arXiv:2511.07513,
Sect. II.2.1]. Solved: θ_E, the mass centroid, the ellipticity angle φ_q,
γ_ext, φ_ext and the source position (eight constraints from four images).
Held at prior draws: axis ratio q, slope γ, multipoles, satellite masses
and positions [src: Sect. V.1]. If the solver fails, which happens at very
high (sub)halo abundance, the realisation is rejected and redrawn [src:
Sect. II.2.1].

The main deflector is an elliptical power law,
κ_EPL(R) = ((3 − γ)/2)(θ_E/R)^(γ−1), R = √(q x² + y²/q) (Eq. 23), plus
external shear and elliptical multipoles δR = a_m cos(m(φ − φ_m)) for
m = 1, 3, 4 (Eq. 24) [src: Sect. V.1].

Multi-plane ray tracing (Eq. 4) with ~10⁴ background haloes is made
tractable by the decoupled multi-plane approximation: the deflection by
haloes behind the deflector is computed once for an initial macromodel
that fits the images without substructure and then held fixed, so the
lens equation becomes linear in the macromodel deflection (Eq. 6) [src:
Sect. II.1].

### Step 5. Compute magnifications and the flux-ratio likelihood
<!-- key: step-5-compute-magnifications-and-the-flux -->

Magnifications are integrals over a circular Gaussian source of the
sampled size, ray-traced on a fine grid around each image [src:
Sects. II.2.2, V.4]. With JWST flux ratios the likelihood is a
three-dimensional Gaussian in the flux ratios with the measured covariance
Σ_fr (Eq. 7) [src: Sect. II.2.2]. (The HTML rendering read here prints the
exponent without the factor −½; the text calls it a Gaussian.)

### Step 6. Add the imaging data by importance weights
<!-- key: step-6-add-the-imaging-data-by-importance -->

The arcs are not reconstructed for each forward-modelled realisation.
Instead a separate set of lens models fitted to arcs + positions provides
weights w_img(n_mac | d_ptsrc, d_I) on the macromodel parameters (Eq. 9):
the ratio of the macromodel posterior with imaging to that without,
integrated over realisations and q [src: Sect. II.2.3]. The authors'
reason: modelling imaging data in the presence of substructure risks
systematic bias, so the arcs are used only to constrain the deflector on
scales larger than a pixel [src: Sects. II, II.2.3]. Substructure is
included when computing w_img because the macromodel absorbs large-scale
effects of a realisation (example: several 10¹⁰ M⊙ haloes inside θ_E are
absorbed by θ_E), which widens the macromodel uncertainties [src:
Sect. II.2.3]. The likelihood per lens is then Eq. 3.

### Step 7. Turn samples into a likelihood per lens and combine
<!-- key: step-7-turn-samples-into-a-likelihood-per-lens -->

Samples of q are drawn from uniform or log-uniform sampling distributions
and weighted by the likelihood; 0.3–21 million realisations per lens
(Table 2 lists N_real per system) [src: Sects. II.2, V.1]. Each lens's
weighted samples become a continuous likelihood through a Gaussian kernel
density estimator (Eq. 28), with a boundary correction that divides by the
KDE of uniform samples from the sampling distribution, and a bandwidth
from Silverman's rule h = (n(d + 2)/4)^(−2/(d+4)) (Eq. 29), n being the
effective sample size; the bandwidth is increased by 10%, weakening the
m_hm bound by ~0.1 dex but removing islands of probability attributed to
shot noise [src: App. B]. The posterior is the prior times the product of
the per-lens likelihoods (Eq. 1). Uniform sampling is required so that the
prior is not used once per lens; any other prior is applied afterwards by
reweighting [src: arXiv:1908.06983, Sect. 2.3].

### Step 8. Quote the bound
<!-- key: step-8-quote-the-bound -->

The m_hm bound is quoted as a 10:1 Bayes factor (ratio of posterior at the
peak region to the excluded value) and at 95%, for a log-uniform Σ_sub and
for the galacticus and N-body priors (values in L2). The keV number follows
from the relation each paper adopts (L2).

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Likelihood: ABC or Gaussian
<!-- key: likelihood-abc-or-gaussian -->

| | ABC rejection (2019 and earlier) | Gaussian likelihood (JWST, 2025) |
|---|---|---|
| Statistic | S = √Σ(f′_i − f_obs,i)² over three flux ratios (arXiv:1908.06983, Eq. 4) | Eq. 7 of arXiv:2511.07513 |
| Acceptance | 800 lowest S per lens out of 0.3–1.2 million (arXiv:1908.06983, Sect. 2.3) | all samples weighted |
| Why | narrow-line flux errors become non-Gaussian on the ratios (arXiv:2511.07513, Sect. II.2.2) | JWST ratios have approximately Gaussian errors (arXiv:2511.07765, Sect. V) |
| Cost | approximation that converges only as samples grow at fixed acceptance; implicit tolerance | requires the Gaussian assumption to hold |

The 2025 analysis still uses ABC for one lens, J0924, because its flux
ratios deviate so strongly from smooth models that the Gaussian likelihood
leaves too few effective samples; it keeps the 6000 lowest-S samples out of
~6 million, an implicit tolerance [src: arXiv:2511.07513, Sect. II.2.2].
The 2019 paper argues that S carries the full information because matching
all three ratios at once forces the accepted samples to carry the data's
correlations [src: arXiv:1908.06983, Sect. 2.3].

### Macromodel: how much angular freedom
<!-- key: macromodel-how-much-angular-freedom -->

| Analysis | Angular structure | Place read |
|---|---|---|
| Gilman et al. 2019; Hsueh et al. | none | arXiv:2511.07513, Sect. VII.1 |
| Keeley et al. 2024 (as cited) | fewer degrees of freedom | same |
| Keeley et al. 2025; Gilman et al. 2025 | elliptical m = 1, 3, 4, free amplitudes and orientations | arXiv:2511.07765 abstract; arXiv:2511.07513, Sect. V.1 |

Priors in 2025: a_m ~ N(0, σ_m), σ_1 = σ_3 = 0.005, σ_4 = 0.01, from
isophote shapes of massive ellipticals; orientations free within ±π/(2m),
except φ_4 = 0 when a_4 > 0.02 because very disky contours align with the
major axis; γ ~ N(2.1, 0.1), with two exceptions where the data prefer a
slope more than 2σ away; q ~ truncated normal with mean q_light, lower
bound min(0.4, q_light − 0.15), σ = 0.2 [src: arXiv:2511.07513,
Sect. V.1]. Caveat stated by the authors: the a_m priors were derived for
circular multipoles, applied here to elliptical ones, whose effect is
expected comparable or smaller [src: same]. Elliptical multipoles impart
weaker flux-ratio perturbations than circular ones in highly flattened
systems [src: Sect. VII.1].

Earlier practice used flat external-shear priors per lens up to
U(0.12, 0.35) for B1422+231 and U(0.13, 0.32) for WFI 2033 [src:
arXiv:1908.06983, Table 2]. A 2026 critique argues that external shear far
above cosmic-shear expectations can always resolve position anomalies and
partly absorb flux-ratio anomalies, so that it conceals substructure
signals when not "sensibly incorporated" (Alfred et al. 2026,
arXiv:2607.07709 [src]). In the 2025 analysis γ_ext is solved for, not
drawn from a prior [src: arXiv:2511.07513, Sect. V.1]; the sections read
do not state a bound on it.

A macromodel-free alternative replaces the global profile by a local
curved-arc basis (CAB) fitted to the arcs: on mocks it predicts flux
ratios to ~3–5%, less precise than macromodel predictions but robust to
angular structure, and does not absorb injected halo perturbations
(Paugnat, Treu & Gilman 2025, arXiv:2509.05416 [src]).

### Imaging data
<!-- key: imaging-data -->

Adding arcs improves the bound by 0.4 dex (L2). The mechanism: arcs
constrain q, γ_ext, γ and the m = 3, 4 amplitudes, narrowing the
model-predicted flux ratios (Figs. 2–3) and breaking the Σ_sub–m_hm
covariance [src: arXiv:2511.07513, Sect. II.2.3; abstract]. Eight of the
28 lenses have HST imaging, three NIRCam, eleven MIRI F560W and four none
listed [src: Table 2, counted here [der]]; systems without imaging enter
through positions and flux ratios only.

### Subhalo-abundance prior: what is being calibrated
<!-- key: subhalo-abundance-prior-what-is-being-calibrated -->

Σ_sub is the infall amplitude. The priors are built by matching the bound
mass function in a 10 kpc annulus of dark-matter-only hosts [src:
arXiv:2511.07513, Sect. IV.3]: f̄_bound = 0.05 for a 10¹³ M⊙ host at
z = 0.5; galacticus gives f̄_bound Σ_sub = 0.009 kpc⁻², 0.0075 after a 15%
central-galaxy suppression, hence Σ_sub = 0.15 kpc⁻²; Symphony N-body
gives 0.006 kpc⁻², hence Σ_sub = 0.1 kpc⁻² [src]. Galacticus matches the
infall amplitude by construction because it calibrates the tidal model;
for the N-body runs only the bound amplitude is known [src]. Keeley et al.
state the same 0.15 and 0.1 kpc⁻² but give the prior width as 0.2 dex in
the text and 0.3 dex in the caption of their Fig. 3 [src:
arXiv:2511.07765, Sect. VIII.1].

Because the tidal model changed, Σ_sub values are not comparable with
earlier papers: evaluating subhalo structure at infall (typical z ~ 4)
makes subhaloes denser by a factor 10–200 than evaluating it at z = 0
[src: arXiv:2511.07513, Sect. VII.1].

### Changes since 2019 and their direction
<!-- key: changes-since-2019-and-their-direction -->

The 2025 paper lists, with direction [src: arXiv:2511.07513,
Sect. VII.1]: tidal model (strengthens WDM limits through the
concentration dependence of stripping); m = 1, 3, 4 elliptical multipoles
(adds perturbations, weakens); subhalo upper mass 10^10.7 M⊙ (weakens);
halo-mass-function suppression of a newer model, less suppressed at fixed
m_hm than the one used in 2019 (weakens at fixed m_hm); globular clusters
(weakens); a prior on q from the light, which also fixes an
underestimate of flux-ratio uncertainties that a particle-swarm start
could cause. A limit comparison across years therefore mixes data and
model changes.

### Statistic: full forward model or cusp relation
<!-- key: statistic-full-forward-model-or-cusp-relation -->

A different 2026 analysis uses the cusp relation R_cusp of 17 cusp quads
with microlensing-free flux ratios against mock populations under CDM,
SIDM and FDM, with SIE + shear lenses and then with m = 3, 4 multipoles
drawn from isophote-based priors (Hou et al. 2026, arXiv:2601.16818
[src: abstract; Methods, "Lens population: multipoles"]). Multipoles move
several major-axis cusps into the CDM/SIDM 1σ region; B2045 and J1042
remain anomalous, J1042 at > 3σ for CDM and SIDM; the authors report a
Bayes factor above 100 for FDM [src: "Statistical test with a SIE lens,
shear, and multipoles"; abstract]. They note a selection effect: strongly
flattened or multipole-rich lenses preferentially produce major-axis cusps
[src: same], and that only 11 lenses lie in their region of interest
[src: abstract]. The forward-model analyses above find no departure from
CDM at the level of their bounds; the two approaches differ in statistic,
lens priors and dark-matter models, and the sections read do not compare
them on common lenses.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Image-position precision | ~5 mas | JWST sample | arXiv:2511.07513 | Sect. II.2.1 |
| Realisations per lens | 0.3–21 × 10⁶ | JWST + arcs | arXiv:2511.07513 | Sect. II.2, Table 2 |
| Realisations per lens (2019) | 0.3–1.2 × 10⁶, 800 accepted | 8 narrow-line quads | arXiv:1908.06983 | Sect. 2.3 |
| Lenses in the 2025 inference | 28 (26 mid-IR + 2 narrow-line) of 31 measured | JWST | arXiv:2511.07765 | Fig. 3 caption, abstract |
| Rendered halo masses | 10⁶–10^10.7 M⊙ | JWST + arcs | arXiv:2511.07513 | Sect. IV.1 |
| Line-of-sight geometry | cone 6 θ_E, Δz = 0.02 | same | arXiv:2511.07513 | Sect. IV.1.1 |
| Two-halo boost near deflector | ~20% more haloes | same | arXiv:2511.07513 | Sect. IV.1.1 |
| Subhalo footprint | uniform to 3 θ_E (~30 kpc) | same | arXiv:2511.07513 | Sect. IV.1.2 |
| F(m_host, z) exponents | k1 = 0.55, k2 = 0.37 | same | arXiv:2511.07513 | Eq. 16 |
| Multipole prior widths | σ_1 = σ_3 = 0.005, σ_4 = 0.01 | same | arXiv:2511.07513 | Sect. V.1 |
| Slope prior | γ ~ N(2.1, 0.1) | same | arXiv:2511.07513 | Sect. V.1 |
| Source size FWHM | 1–10 pc (warm dust), 20–80 pc (narrow line) | same | arXiv:2511.07513 | Sect. V.4 |
| Hot-dust temperature floor | 1200 K (was 900 K) | JWST fluxes | arXiv:2511.07765 | Sect. V |
| KDE bandwidth | Silverman × 1.1; costs ~0.1 dex | JWST + arcs | arXiv:2511.07513 | App. B |
| Convergence of 10:1 bound | ~0.2 dex | JWST + arcs | arXiv:2511.07513 | App. A |
| ABC lens | J0924: 6000 of ~6 × 10⁶ | JWST + arcs | arXiv:2511.07513 | Sect. II.2.2 |
| CDM-indistinguishable region | m_hm ≲ 10⁵ M⊙ (<10% change at 10⁶ M⊙ for 10⁴) | same | arXiv:2511.07513 | Sect. IV.3 |
| Projected subhalo mass, CDM | 1.7 (+2.6/−1.2) × 10⁷ M⊙ kpc⁻² (95%); galacticus 0.9, N-body 0.6 × 10⁷ | same | arXiv:2511.07513 | abstract |
| Flux-ratio-only bounds, broad Σ_sub | log10 m_hm < 9.3 (10:1), < 8.5 (95%) | JWST flux ratios | arXiv:2511.07765 | Sect. VIII.1 |
| Same, galacticus / N-body prior, 95% | < 7.3 / < 7.0 | JWST flux ratios | arXiv:2511.07765 | Sect. VIII.1 |

The 95% values of the last row are not in L2, which quotes the 10:1
values; for the conversion to keV see L2.

## What goes wrong
<!-- key: what-goes-wrong -->

- **Too few effective samples.** Shows up as islands in the posterior and
  bounds that move when samples are discarded. Test: discard random
  subsets and recompute the 10:1 bound; the 2025 analysis is converged at
  ~0.2 dex, and differential criteria (Bayes factor) are more sensitive
  to shot noise than integral ones (confidence intervals) [src:
  arXiv:2511.07513, App. A].
- **KDE edge bias.** Gaussian kernels downweight the edges of the sampling
  range, exactly where a bound lives. Fix: divide by the KDE of uniform
  samples; this is a leading-order correction, unbiased only if the target
  has zero gradient at the edge [src: App. B].
- **Prior used once per lens.** Non-uniform sampling multiplies the prior
  N times. Fix: sample uniformly, reweight afterwards [src:
  arXiv:1908.06983, Sect. 2.3].
- **Macromodel too rigid.** Spurious anomalies from missing angular
  structure. Tests: m = 1, 3, 4 multipoles varied jointly with the halo
  population [src: arXiv:2511.07513, Sect. V.1]; a CAB fit as a
  macromodel-free check [src: arXiv:2509.05416].
- **Macromodel too flexible.** Large external shear absorbs anomalies
  [src: arXiv:2607.07709]. Test: compare inferred γ_ext with sightline
  expectations.
- **Lensed disks and merging images.** The 2019 analysis excluded lenses
  with stellar disks (they need explicit disk models) and HS 0810, whose
  merging images blend for source sizes above 20 pc; radio-flux lenses
  were excluded [src: arXiv:1908.06983, Sect. 4.2].
- **Microlensed component left in the flux.** Shows as unphysical SED
  solutions (warm-dust flux to zero). Fix used: raise the hot-dust
  temperature floor [src: arXiv:2511.07765, Sect. V].
- **Missing mass sheet.** Without negative convergence sheets the model
  bends rays towards the centre, increasingly with substructure [src:
  arXiv:2511.07513, Sect. IV.1.1].
- **Comparing Σ_sub across papers.** The parameter's meaning changed with
  the tidal model [src: Sect. VII.1].
- **Unmodelled compact perturbers.** A ~10⁶ M⊙ compact object detected in
  an arc could indicate a population that is not in the model if it is not
  a globular cluster [src: Sect. VII.1].

## Reading list
<!-- key: reading-list -->

- Foundation: Dalal & Kochanek 2002, arXiv:astro-ph/0111456 — first
  measurement of the substructure fraction from seven lenses, f = 0.02
  (0.006 < f < 0.07, 90%).
- Method: Gilman et al. 2019, arXiv:1908.06983 — the ABC forward-model
  framework, sampling and KDE rules, lens selection.
- Data: Keeley et al. 2025, arXiv:2511.07765 — JWST MIRI flux and SED
  method, flux-ratio-only bounds.
- Application: Gilman et al. 2025, arXiv:2511.07513 — Gaussian likelihood,
  arcs by importance weights, tidal model, priors, KDE and convergence.
- Method: Paugnat, Treu & Gilman 2025, arXiv:2509.05416 — macromodel-free
  flux-ratio prediction.
- Critique: Alfred et al. 2026, arXiv:2607.07709 — external shear hiding
  anomalies.
- Competing interpretation: Hou et al. 2026, arXiv:2601.16818 — cusp
  statistic favouring FDM.
- Review: Bechtol et al. 2022, arXiv:2203.07354 — place of lensing among
  halo probes.

## Not verified
<!-- key: not-verified -->

- The WDM suppression model "of [92]" adopted in 2025 and the one "of
  [137]" used in 2019 were not identified by name or read.
- The Du et al. tidal model, the Gannon et al. abundance calibration and
  the Symphony halo finders were read only as described in
  arXiv:2511.07513.
- No ablation of the multipole priors or of the source-size range on the
  bound was found in the sections read.
- Hou et al. 2026: the Bayesian decision criterion and the SIDM and FDM
  substructure models (Methods g–h, d) were not read.
- Gravitational-imaging analyses of individual arcs, cited as broadly
  consistent in arXiv:2511.07513 Sect. VII.1, were not read.
