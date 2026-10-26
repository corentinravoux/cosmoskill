# Strong-lensing substructure — cosmo-neutrinos-dark-matter dossier

Scope: how a dark-matter limit is produced from quadruply imaged quasars
(flux measurement, forward model of halo populations, per-lens likelihood,
combination over lenses, conversion to a particle mass), and how to choose
between likelihood constructions, macromodel freedoms and subhalo-abundance
priors. The worked example is the forward model of the Gilman, Treu,
Birrer and Nierenberg teams (pyHalo, lenstronomy), the source of most
current quad limits; beside it: the SHARP flux-ratio analysis (Hsueh,
Vegetti, Fassnacht et al.), gravitational imaging of extended arcs (Vegetti
and Koopmans; the Durham automated scan; ALMA and VLBI data), and the dense
perturbers read as tests of SIDM.
Snapshot: 2026-10-22.
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
| Hot dust, ~1500 K, sublimation zone | 0.05–0.2 pc at 10⁴⁴–10⁴⁵ erg/s | can be microlensed; modelled and removed | arXiv:2511.07765, Sect. V |
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
between images [src: arXiv:2511.07765, Sect. V]. The hot-dust temperature prior was raised
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
prior" [src: arXiv:2511.07513, Sect. IV.3]. Sect. IV.1.1 of the same paper describes δ_LOS
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
  [src: arXiv:2511.07513, Sect. IV.1]. Earlier work stopped at 10¹⁰ M⊙ [src: Sect. VII.1].
- **Field haloes.** Double cone opening to six Einstein radii, planes
  every Δz = 0.02, uniform positions; mass function
  d²N/dm dV = δ_LOS [1 + ξ(m_host, z_d)] d²N_ST/dm dV (Eq. 13), where
  ξ is the two-halo term of the group host, adding ~20% haloes near the
  deflector, computed with colossus [src: arXiv:2511.07513, Sect. IV.1.1]. Profiles are
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
  on galacticus (Eq. 16) [src: arXiv:2511.07513, Sect. IV.1.2]. Each subhalo gets an infall
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
lens equation becomes linear in the macromodel deflection (Eq. 6) [src: arXiv:2511.07513, 
Sect. II.1].

Peers: SHARP VII models seven quads with stellar discs and luminous
satellites explicitly in the macromodel and, "for the first time",
line-of-sight haloes of 10⁶–10⁹ M⊙ [src: Hsueh et al. 2020,
arXiv:1905.04182, abstract]. A study with Aquarius-style CDM haloes found
that substructure matters for close image pairs and triples, while
anomalies in large-separation systems are attributed to simplifications
of the smooth models [src: Xu et al. 2015, arXiv:1307.4220, abstract].

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
integrated over realisations and q [src: arXiv:2511.07513, Sect. II.2.3]. The authors'
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

Gravitational-imaging analyses quote the bound differently: detections and
non-detections, weighted by each lens's sensitivity function, enter a
Poisson likelihood whose expectation is the (sub)halo mass function of the
dark-matter model tested [src: Vegetti et al. 2023 review,
arXiv:2306.11781, Sect. 4.4.1].

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

Other groups on the same degeneracy, one line each:

- Mock quads perturbed by 10–40% by CDM haloes are fitted equally well by
  m = 3, 4 multipoles of amplitude ≤ 0.01; "flux-ratio anomalies in lensed
  quasars alone cannot be used to place strong constraints" without
  information that informs the priors [src: Cohen et al. 2024,
  arXiv:2403.08895, abstract]. The forward model above answers with
  isophote-based priors on a_m (this section).
- In arcs, subhalo detectability depends on the azimuthal freedom of the
  lens model; separate dark and stellar components turn up two candidates
  and remove four false positives of the single power law [src:
  Nightingale et al. 2024, arXiv:2209.10566, abstract].
- In ALMA data of SDP.81, the earlier ~10⁹ M⊙ subhalo inference "was most
  likely spurious", from poorly fitting multipoles, although mocks show it
  would have been found with log Bayes factor 29 had it existed; the
  authors ask for multipoles up to m = 4 and a good smooth fit as a
  prerequisite [src: Stacey et al. 2025, arXiv:2508.02776, abstract].

### Imaging data
<!-- key: imaging-data -->

Adding arcs improves the bound by 0.4–0.5 dex [src: arXiv:2511.07513 Sect. VI.2]. The mechanism: arcs
constrain q, γ_ext, γ and the m = 3, 4 amplitudes, narrowing the
model-predicted flux ratios (Figs. 2–3) and breaking the Σ_sub–m_hm
covariance [src: arXiv:2511.07513, Sect. II.2.3; abstract]. Table 2 of that paper lists, lens by lens, the imaging
used (HST, NIRCam or MIRI F560W) [src: Table 2]; systems without imaging enter
through positions and flux ratios only.

### Extended arcs: gravitational imaging and its variants
<!-- key: extended-arcs-gravitational-imaging-and-its -->

The arc route is a separate family, with its own steps [src:
arXiv:2306.11781, Sects. 4.4.1, 4.4.3, 7.2]:

| Step | Gravitational imaging (Koopmans 2005; Vegetti & Koopmans 2009) | Alternatives |
|---|---|---|
| Model | pixellated source; low-mass haloes as linear, pixellated corrections to the parametric potential, so no assumption on their number, mass or position | power spectrum of a Gaussian random field of density fluctuations (Hezaveh et al. 2016), valid only below ~5 × 10⁷ M⊙; trans-dimensional probabilistic cataloguing (Brewer et al. 2016, Daylan et al. 2018) |
| Detection | free-form correction consistent with a parametric halo fit, and Bayes factor ≥ 50 over the smooth model, roughly ≥ 10σ | — |
| Why so strict | false positives fall from 40% at a 4σ threshold to 20% at 5σ; false negatives from 60% at 4σ to 30% at 6σ (Ritondale et al. 2019, as summarised) | — |
| Non-detections | sensitivity function: lowest detectable mass per image pixel | machine-learning estimate (O'Riordan et al. 2023) |
| Inference | Poisson likelihood of detections given the model's mass functions | forward or statistical comparison of the measured power spectrum |

The method is "not fully forward": detections must be assessed and then
interpreted against theory in two further steps [src: Sect. 4.4.1].
Sensitivity: the lowest detectable mass falls linearly with S/N and more
strongly with angular resolution; HST data reach ~10⁹ M⊙, which is why
arc limits are "less stringent (though possibly more robust)" than quad
limits [src: Sect. 7.2, after Despali et al. 2022]. A 10σ criterion on
17 BELLS-GALLERY lenses gives no detection, against 1.17 ± 1.08 expected
CDM line-of-sight haloes; a 5σ threshold would expect 9.0 ± 3.0 but yields
many spurious detections and non-detections [src: Ritondale et al. 2019,
arXiv:1811.03627, abstract]. Milli-arcsecond VLBI changes the regime: a
(1.13 ± 0.04) × 10⁶ M⊙ object within 80 pc detected at 26σ, found
non-parametrically and confirmed parametrically [src: Powell et al. 2025,
arXiv:2510.07382, abstract].

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

### Dense perturbers and SIDM: the competing readings
<!-- key: dense-perturbers-and-sidm-the-competing-readings -->

Two arc detections carry most of the SIDM argument; each paper's reading:

- **SDSS J0946+1006 (subhalo H).** Projected mass ~2–3.7 × 10⁹ M⊙ within
  1 kpc, slope steeper than isothermal; under 1% of TNG100 mocks are steep
  enough and all are too luminous, so the object is "unexpected" in ΛCDM,
  also as a line-of-sight halo [src: Minor et al. 2021, arXiv:2011.10627,
  abstract]. Fitting its redshift gives 0.207 ± 0.019, a subhalo, a > 5σ
  outlier from the ΛCDM v_max–r_max relation, slope γ_2D close to the
  −2 of gravothermal collapse [src: Enzi et al. 2024, arXiv:2411.08565,
  abstract]. It is one of two compelling candidates in the Durham scan of
  54 HST lenses [src: arXiv:2209.10566, abstract].
- **JVAS B1938+666, object A (~10⁸ M⊙).** First reported as a
  1.9 × 10⁸ M⊙ satellite [src: Vegetti et al. 2012, arXiv:1201.3643,
  abstract]; refitted as a line-of-sight halo behind the lens at
  z = 1.42, an order of magnitude more massive [src: Şengül et al. 2022,
  arXiv:2112.00749, abstract]; refitted again as a foreground halo at
  z = 0.13 ± 0.07, with TNG50 analogues "atypical but possible" in ΛCDM
  [src: Tajalli et al. 2025, arXiv:2505.07944, abstract]. Both objects may
  match SIDM gravothermal profiles for σ_c,0/m ≳ 300 cm²/g [src: same].
- **JVAS B1938+666, the 10⁶ M⊙ object.** Best models: a point mass within
  ≤ 10 pc on a near-constant surface density truncated at 139 pc; if dark,
  "incompatible with cold dark matter", possibly an SIDM halo whose centre
  collapsed to a black hole [src: Vegetti et al. 2026, arXiv:2601.02466,
  abstract]. Gravothermal fluid simulations reproduce it in deep core
  collapse; CDM with an intermediate-mass black hole needs a progenitor
  stripped by five orders of magnitude [src: Zhang & Yu 2026,
  arXiv:2606.12909, abstract]. SIDM zoom-ins (Concerto) contain analogues
  of the observed perturbers through core collapse [src: Kong, Nadler &
  Yu 2025, arXiv:2510.01491, abstract].
- **Quads.** As summarised by the review, existing quad data disfavour SIDM
  models with large amplitudes at low speeds, if those drive low-mass
  haloes to core collapse (Gilman et al. 2022) [src: arXiv:2306.11781,
  Sect. 7.1]; that primary paper was not read here.

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
| f_sub (CDM); m_th | 0.012 (+0.007/−0.004); > 5.58 keV (95%) | 7 quads, discs and LOS haloes | arXiv:1905.04182 | abstract |
| Substructure fraction, SLACS | f = 0.0076 (+0.0208/−0.0052) uniform prior; 0.0064 (+0.0080/−0.0042) CDM prior on α | 11 SLACS arcs + J0946 | arXiv:1405.3666 | abstract |
| B1938 satellite; slope, fraction | 1.9 ± 0.1 × 10⁸ M⊙; α = 1.1 (+0.6/−0.4), f = 3.3 (+3.6/−1.8)% | two arc detections | arXiv:1201.3643 | abstract |
| Arc-only half-mode bound | log M_hm < 12.26 (2σ) | 17 BELLS + 11 SLACS | arXiv:1811.03627 | abstract |
| Joint thermal relic | m_th > 6.048 keV, M_hm < 3 × 10⁷ M⊙/h (95%); lensing alone > 0.6 (SLACS), > 0.1 keV (BELLS) | arcs + Lyα + MW satellites | arXiv:2010.13802; arXiv:2306.11781 | abstract; Sect. 7.2 |
| Quads + MW satellites | M_hm < 10⁷ M⊙, m_WDM > 9.7 keV (95%) (Nadler et al. 2021, as summarised) | — | arXiv:2306.11781 | Sect. 7.1 |
| FDM from one VLBI arc | m ≤ 4.4 × 10⁻²¹ eV excluded (Powell et al. 2023, as summarised) | MG J0751+2716 | arXiv:2306.11781 | Sect. 7.2 |
| Lowest-mass detection | m_80 = (1.13 ± 0.04) × 10⁶ M⊙, 26σ, astrometry 194 μas | B1938 VLBI arc | arXiv:2510.07382 | abstract |
| J0946 subhalo | z = 0.207 ± 0.019; γ_2D = −1.81 (+0.15/−0.11) at 0.75–1.25 kpc | HST arcs | arXiv:2411.08565 | abstract |
| B1938 object A redshift | 1.42 (+0.10/−0.15) vs 0.13 ± 0.07 | same data, two analyses | arXiv:2112.00749; arXiv:2505.07944 | abstract (both) |
| HST arc candidates | 5 candidates, 2 compelling, 45 lenses without substructure, of 54 | HST | arXiv:2209.10566 | abstract |

The 95% values of the JWST flux-ratio rows with the galacticus / N-body
priors are not in L2, which quotes the 10:1 values; for the conversion to
keV see L2.

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
  a globular cluster [src: arXiv:2511.07513, Sect. VII.1].
- **Multipoles read as subhaloes, in quads and arcs.** m = 3, 4 at ≤ 0.01
  reproduce CDM-level anomalies [src: arXiv:2403.08895, abstract]; a reported ALMA
  subhalo did not survive multipoles [src: arXiv:2508.02776]. Test: fit
  multipoles to m = 4 before claiming a detection.
- **Perturber redshift assumed.** The same B1938 object was placed at the
  lens, behind it (z = 1.42) and in front (z = 0.13), with mass changing
  by an order of magnitude [src: arXiv:2112.00749, abstract; arXiv:2505.07944, abstract].
  Test: fit the redshift.
- **Detection threshold too low.** At 5σ, arcs give many spurious
  detections and non-detections [src: arXiv:1811.03627]. Test: Bayes
  factor ≥ 50 and agreement of free-form and parametric fits [src:
  arXiv:2306.11781, Sect. 4.4.1].

## Reading list
<!-- key: reading-list -->

- Foundation: Dalal & Kochanek 2002, arXiv:astro-ph/0111456 — first substructure fraction from seven lenses, f = 0.02 (0.006 < f < 0.07, 90%). [src: abstract]
- Method (quads): Gilman et al. 2019, arXiv:1908.06983 — ABC forward model, sampling and KDE rules, lens selection.
- Data (quads): Keeley et al. 2025, arXiv:2511.07765 — JWST MIRI fluxes, SED method, flux-ratio-only bounds.
- Application (quads): Gilman et al. 2025, arXiv:2511.07513 — Gaussian likelihood, arcs by importance weights, tidal model, priors, KDE.
- Application (quads, other team): Hsueh et al. 2020, arXiv:1905.04182 — SHARP VII, discs and line-of-sight haloes, m_th > 5.58 keV. [src: abstract]
- Method: Paugnat, Treu & Gilman 2025, arXiv:2509.05416 — macromodel-free flux-ratio prediction.
- Critique: Alfred et al. 2026, arXiv:2607.07709 — external shear hiding anomalies; Cohen et al. 2024, arXiv:2403.08895 — multipoles mimic haloes; Xu et al. 2015, arXiv:1307.4220 — which anomalies CDM substructure explains.
- Competing interpretation: Hou et al. 2026, arXiv:2601.16818 — cusp statistic favouring FDM.
- Review: Vegetti et al. 2023, arXiv:2306.11781 — both routes, modelling approaches, detection criteria, constraints; Bechtol et al. 2022, arXiv:2203.07354 — lensing among halo probes.
- Arcs: Vegetti et al. 2012, arXiv:1201.3643; Vegetti et al. 2014, arXiv:1405.3666; Ritondale et al. 2019, arXiv:1811.03627; Nightingale et al. 2024, arXiv:2209.10566; Stacey et al. 2025, arXiv:2508.02776 (ALMA); Powell et al. 2025, arXiv:2510.07382 (VLBI).
- Joint WDM: Enzi et al. 2021, arXiv:2010.13802 — arcs with Lyα and Milky Way satellites.
- Dense perturbers and SIDM: Minor et al. 2021, arXiv:2011.10627; Şengül et al. 2022, arXiv:2112.00749; Enzi et al. 2024, arXiv:2411.08565; Tajalli et al. 2025, arXiv:2505.07944; Vegetti et al. 2026, arXiv:2601.02466; Kong, Nadler & Yu 2025, arXiv:2510.01491; Zhang & Yu 2026, arXiv:2606.12909.

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
- Gravitational-imaging analyses (called broadly consistent in
  arXiv:2511.07513, Sect. VII.1): read at abstract level, with the review's
  method and constraint sections (arXiv:2306.11781, Sects. 4.4, 7); their
  method sections, and the primary papers the review summarises (Hezaveh
  et al. 2016, Nadler et al. 2021, Powell et al. 2023, Gilman et al. 2022
  SIDM, Despali et al. 2022), were not read.
- That object A of arXiv:2505.07944 is the 2012 satellite of
  arXiv:1201.3643 follows from the papers' descriptions of earlier
  analyses [der], not from a statement read.
