# Photometry and photometric redshifts — physics and methods

Scope: how survey photometry is calibrated and how redshifts and redshift
distributions are inferred from it: methods, defining equations, codes.
Snapshot: 2026-10-16

Flags: `[src]` read this session in the abstract of the cited paper;
`[src: Sect. n]`, `[src: Table n]`, `[src: Eq. n]` read in the body at that
place; `[sec]` from a named secondary source; `[der]` derived here.

## 1. Why photometric redshifts limit imaging cosmology
<!-- key: why-photometric-redshifts-limit-imaging -->

Photometric redshifts rely on integrated fluxes in a set of filters, with an
effective spectral resolution R ≲ 50 even with many narrow bands and R < 10 for
the broad-band filters of DES, HSC, KiDS and Rubin LSST (Newman & Gruen 2022,
arXiv:2206.13633) [src: Sect. 1.1]. The review separates two properties that
are often confused: **performance** (the scatter and outlier rate of individual
redshifts) and **characterisation** (how well the redshift distribution n(z) of
an ensemble is known). A method can be well characterised despite poor
performance, and the reverse [src: Sect. 1.1]. Typical numbers quoted there:
σ_z ~ 0.01(1+z) is reached for uniform, high-quality photometry with many
narrow bands or for populations with strong broad features, and σ_z ~ 0.05(1+z)
or larger for diverse galaxies with few broad bands [src: Sect. 1.1].

Because weak lensing and angular clustering use a few broad bins, they tolerate
poor individual redshifts but demand that the mean, width and shape of each
n(z) be known with minimal bias; the review calls redshift characterisation
"perhaps the leading systematic uncertainty" of these analyses
[src: Sect. 1.1].

Degeneracies are intrinsic at low R: with riz alone, an elliptical at z = 0.3
and a spiral at z = 0.52 are nearly indistinguishable, and the 4000 Å break can
be mistaken for the Lyman break [src: Sect. 1.1]. The resulting p(z) is
multimodal and the relative weight of the modes is set by a prior on the galaxy
population.

## 2. Photometric calibration
<!-- key: photometric-calibration -->

### 2.1 Relative calibration from repeated stars ("ubercalibration")
<!-- key: relative-calibration-from-repeated-stars -->

The global approach solves simultaneously for calibration parameters
(per-exposure zero points, flat-field terms, atmospheric transparency) and the
fluxes of stars observed more than once, using overlaps between exposures. It
separates the relative calibration, a large linear least-squares problem, from
the absolute calibration, a few numbers for the whole survey (Padmanabhan et
al. 2008, arXiv:astro-ph/0703454) [src]. Applied to SDSS it reached about 1%
relative errors over 8500 deg² in griz and about 2% in u, limited by unmodelled
atmospheric variation at Apache Point [src]. Pan-STARRS1 extended the method,
solving for system throughput, atmospheric transparency and the large-scale
flat field together, with relative precision below 10 mmag in g, r, i and about
10 mmag in z and y (Schlafly et al. 2012, arXiv:1201.2208) [src]. The Deep Lens
Survey showed that sky flats can be non-uniform by up to 0.13 mag peak to
valley, reduced to 0.01–0.02 mag after ubercal (Wittman et al. 2012,
arXiv:1111.2058) [src].

### 2.2 Forward calibration
<!-- key: forward-calibration -->

The Forward Global Calibration Method (FGCM) of DES models the instrument and
the atmosphere, together with auxiliary measurements taken at the observatory,
to predict the passband of every exposure; a standard passband is defined, and
each magnitude is moved to it with a "chromatic correction" that depends on the
source spectrum (Burke et al. 2018, arXiv:1706.01542) [src]. On DES Y3 the
residual random error is 5–6 mmag per exposure, the uniformity over 5000 deg²
is 7 mmag, and the source-spectrum systematic is below 5 mmag for main-sequence
stars with 0.5 < g − i < 3.0 [src]. The DES Y6 FGCM reference catalogue holds
17 million stars (16 < i < 21) calibrated to a uniformity better than 1.8 mmag
RMS; the absolute scale is tied to the HST CALSPEC spectrum of C26202 and is
known to about 1% (Rykoff et al. 2023, arXiv:2305.01695) [src].

### 2.3 Hardware metrology
<!-- key: hardware-metrology -->

Stubbs & Tonry 2006 (arXiv:astro-ph/0604285) identify atmospheric transmission
along the line of sight and instrumental artefacts as the two obstacles to
sub-percent ground-based photometry, and propose measuring the relative system
throughput in situ with a tunable monochromatic source normalised to a
calibrated photodiode [src]. Rubin Observatory implements this with a
Collimated Beam Projector that injects monochromatic point sources of known
flux; first results map filter bandpass-edge shifts of several nanometres
across the LSSTCam focal plane, a function of the ray angle of incidence
(Amouroux et al. 2026, arXiv:2606.31822) [src]. StarDICE aims at a metrology
chain from laboratory standards to stellar fluxes at 1 mmag in griz; its
thermal-infrared camera corrects grey (cloud) extinction to about 0.01 mag on 2
arcmin scales (Sommer et al. 2025, arXiv:2511.00182) [src].

### 2.4 Stellar standards
<!-- key: stellar-standards -->

The absolute scale comes from HST CALSPEC spectrophotometry; relative standards
come from Gaia XP synthetic photometry and stellar colour regression. Their
precision and the survey errors they have exposed are in `surveys-and-data.md`
§1.

## 3. Chromatic effects and Milky Way extinction
<!-- key: chromatic-effects-and-milky-way-extinction -->

### 3.1 Chromatic (colour-dependent) calibration errors
<!-- key: chromatic-colour-dependent-calibration-errors -->

Zero points and illumination corrections that ignore source colour leave errors
that depend on the source spectrum, because the atmospheric transmission
(airmass, precipitable water vapour, aerosols) and the instrumental throughput
across the focal plane change the effective passband. For DES these systematic
chromatic errors reach 2% in some bands; corrected with measured atmospheric
and instrumental transmission they fall below 0.3%; for galaxies they are
redshift dependent and can exceed those of stars (Li et al. 2016,
arXiv:1601.00117) [src]. FGCM folds this correction into the calibration itself
(arXiv:1706.01542) [src]. The Rubin filter-edge shifts across the focal plane
(arXiv:2606.31822) [src] are the same effect.

### 3.2 Milky Way extinction
<!-- key: milky-way-extinction -->

Extinction corrections apply A_b = R_b E(B−V) per band, with E(B−V) from a map
and R_b from an extinction law. Three families of maps exist:

| Map | Tracer | Property that matters | Reference |
|---|---|---|---|
| SFD | 100 μm emission from COBE/DIRBE + IRAS, dust temperature from DIRBE 100/240 μm | full sky at IRAS resolution; twice as accurate as Burstein–Heiles at low and moderate reddening | Schlegel et al. 1998, arXiv:astro-ph/9710327 [src] |
| SFD recalibrated | SDSS stellar spectra, predicted colours | SFD normalisation 14% too high; Fitzpatrick (1999) law with R_V = 3.1 preferred; R_b tabulated for 88 passbands | Schlafly & Finkbeiner 2011, arXiv:1012.4804 [src] |
| CSFD | SFD minus a CIB/LSS template built from WISE galaxy density fields | removes extragalactic structure from SFD | Chiang 2023, arXiv:2306.03926 [src] |
| DESI stellar | reddening of 2.6 million stars from DESI imaging versus colours synthesised from DESI spectra | differs from SFD by up to 80 mmag in E(B−V), attributed mostly to SFD; better galaxy-density uniformity; limited by photometric calibration | Zhou et al. 2024, arXiv:2409.05140 [src] |

**Extragalactic contamination.** Clustering-redshift cross-correlations with
spectroscopic tracers find large-scale-structure imprints in nine of ten
Galactic dust maps, including all infrared maps and stellar reddening maps, but
not in the HI-based map; the induced magnitude bias is at the millimagnitude
level, redshift and scale dependent, and matters most for low-amplitude angular
correlations such as magnification (Chiang & Ménard 2019, arXiv:1808.03294)
[src]. Over-correction with SFD is therefore spatially correlated with the very
structure being measured (arXiv:2306.03926) [src].

## 4. Photometric redshifts by template fitting
<!-- key: photometric-redshifts-by-template-fitting -->

### 4.1 Method
<!-- key: method -->

A library of rest-frame spectral energy distributions T(λ) (empirical,
synthetic, or linear combinations) is redshifted, attenuated by dust and by
intergalactic absorption, and integrated through each filter; the likelihood of
the observed fluxes F_b with errors σ_b is

  L(z, T, a) ∝ exp[−χ²/2], χ² = Σ_b (F_b − a F_b^T(z))² / σ_b²,

with a free amplitude a (Benítez 2000 writes the same χ² as his Eq. 5, then
normalises fluxes to a base band so that a prior can be put on colours and
magnitude m₀; arXiv:astro-ph/9811189) [src: Sect. 3]. The point estimate
minimises χ², the p(z) follows from marginalising over template and amplitude.
Codes differ in the template set, in priors and in how template mismatch enters
the error budget:

| Code | Feature introduced | Reference |
|---|---|---|
| hyperz | public χ² SED fitting; accuracy and catastrophic rate studied versus template set (age, metallicity, reddening, Lyman-forest absorption), filters and photometric depth | Bolzonella et al. 2000, arXiv:astro-ph/0003380 [src] |
| BPZ | Bayesian marginalisation with priors on redshift and type mix, calibratable on the data themselves; rms Δz/(1+z) = 0.08 to z < 6 on 108 HDF spectra; p(z|C,m₀) ∝ Σ_T p(T|m₀) p(z|T,m₀) p(C|z,T), so noise peaks of an implausible (z, T) are down-weighted where maximum likelihood would pick them | Benítez 2000, arXiv:astro-ph/9811189 [src: Eqs. 11–12, Sect. 4.1] |
| LePhare (CFHTLS calibration) | template zero-point and systematic-trend correction trained on 3241 VVDS spectra; σ_Δz/(1+z) = 0.037 with 3.7% catastrophic errors at i < 24; starbursts are 18% of the spectra and 54% of the catastrophic errors; cosmic variance visible on 0.8 deg² fields; per-band offsets s^f fitted to 468 spectroscopic galaxies at i′ ≤ 21.5 at fixed z (average 0.042 mag, never above 0.1 mag, converged after three iterations), CWW templates optimised from rest-frame fluxes of the spectroscopic sample, then a redshift prior that cuts catastrophic errors by 2.3× [src: Sect. 4.1–4.2, 5.1] | Ilbert et al. 2006, arXiv:astro-ph/0603217 [src] |
| EAZY | linear combinations of templates; templates and priors from semi-analytic models rather than biased spectroscopic samples; rest-frame template error function; quality parameter Q_z; scatter 0.034 in K-selected deep fields; χ² in linear flux space (negative fluxes kept) over T_z = Σ α_i T_{z,i} with α_i ≥ 0, because template mismatch is the primary error; the error function, from GOODS-CDFS residuals, is lowest at rest-frame 3500–9000 Å; prior p(z|m₀) from a light-cone | Brammer et al. 2008, arXiv:0807.1533 [src: Eqs. 1–2, Sect. II.1, II.3–II.4] |

### 4.2 What template methods need to be right
<!-- key: what-template-methods-need-to-be-right -->

Template fitting extrapolates beyond the spectroscopic samples, which is why it
remains the default at faint magnitudes and high redshift, but it is only as
good as (i) the template set's coverage of real SEDs, (ii) the priors on
redshift and type, and (iii) the photometric calibration and filter curves
(§2–3). The zero-point "training" of Ilbert et al. 2006 is a calibration step
that already mixes template fitting and empirical learning
(arXiv:astro-ph/0603217) [src].

### 4.3 How the Stage-III lensing surveys used these codes
<!-- key: how-the-stage-iii-lensing-surveys-used-these -->

DES, HSC and KiDS did not trust the output of any single template or empirical
code: where they used one, they calibrated it against spectroscopic or
high-quality photometric reference redshifts; otherwise they re-weighted
reference redshift histograms to the source sample. Either way the result is a
frequentist p(z) or, stacked, n(z) (Newman & Gruen 2022, arXiv:2206.13633)
[src: Sect. 2.3]. The estimated uncertainty of the mean redshift from these
characterisation methods under idealised conditions ranged from 0.004 to 0.05
for earlier methods and from 0.001 to 0.006 for the most recent ones, before
the effects of incomplete or biased reference samples, which "can be several
times larger" [src: Sect. 2.3]. In community challenges with representative
training data, most template and machine-learning methods fail LSST Y1
characterisation requirements even under idealised conditions [src: Sect. 2.3].

## 5. Photometric redshifts by machine learning
<!-- key: photometric-redshifts-by-machine-learning -->

### 5.1 Method families
<!-- key: method-families -->

Empirical (training-based) methods learn p(z | photometry) from a reference
sample with known redshifts. They are accurate inside the colour–magnitude
volume the training set covers and uncontrolled outside it.

| Family | Code | What the paper establishes | Reference |
|---|---|---|---|
| Neural network | ANNz | rms error 0.023 for SDSS DR1 at 0 < z < 0.7; competitive with templates when the training set is large and representative; degraded when it is small or brighter than the target sample | Collister & Lahav 2004, arXiv:astro-ph/0311058 [src] |
| Trees / random forest | TPZ | p(z) from prediction trees; propagates measurement errors, handles missing values, flags poorly trained regions of parameter space | Carrasco Kind & Brunner 2013, arXiv:1303.7269 [src] |
| Nearest neighbours | DNF | directional neighbourhood metric plus local fit; the DES reference estimator; the metric DN = D² sin²α multiplies the Euclidean magnitude distance by the angle between multi-magnitude vectors, so neighbours keep the target's flux proportions [src: Sect. 2.3, Eq. 3]; a hyperplane fit to ~60 neighbours beats a 25-neighbour kNN average and approaches ANNz [src: Sect. 5.1] | De Vicente et al. 2016, arXiv:1511.07623 [src]; DES Y6 Gold use: arXiv:2607.07771 [src] |
| Gaussian process | GPz | heteroscedastic predictive variance from both data density and photometric noise; outperforms TPZ and ANNz2 on SDSS DR12; the variance is a model term ν*, which shrinks where training data are dense, plus a noise term β⁻¹ made input-dependent, β_i = exp(φ(x_i)u + b) [src: Sect. 5, Eqs. 5.1–5.4] | Almosallam et al. 2016, arXiv:1604.03593 [src] |
| Images (CNN) | Pasquet et al. | 64 × 64 ugriz cutouts plus reddening; σ_MAD < 0.01 with ≥ 100k training objects, bias < 10⁻⁴, SDSS main sample z < 0.4; precision limited by image S/N | Pasquet et al. 2019, arXiv:1806.06607 [src] |
| Domain adaptation | CNN + adversarial network | CNN trained on the COSMOS Ultra Deep Field at i < 25 failed on other HSC-CLAUDS fields until an unsupervised adversarial domain-adaptation branch was added; catalogues for ~4 million sources | Treyer et al. 2025, arXiv:2512.11700 [src] |
| Manifold learning | UMAP-kNN-z | UMAP compression of ugrizyJH colours; with a highly biased spec-z training set it keeps its performance while SOM- and colour-space methods degrade, notably at z > 1.5 | Ashmead et al. 2025, arXiv:2512.09032 [src] |

### 5.2 Implicit priors and imperfect training sets
<!-- key: implicit-priors-and-imperfect-training-sets -->

Tortorelli & Grün 2026 (arXiv:2605.06790) frame every machine-learning
estimator as an approximation to the Bayesian p(z | data) that imposes an
implicit, and in general imperfect, prior on the observable–redshift relation
p(z, t); the extreme case trainZ assumes p(z, t) = p(z), independent of the
observables, and no method of their Sect. 2 infers p(z, t) consistently
[src: Sect. 2.0.5]. They name four mechanisms by which training samples bias
learned redshifts: volume-limited numbers of low-redshift galaxies in a small
field; photometric pre-selection of spectroscopic targets; selection by
redshift confidence, where at fixed photometry the success rate depends on the
true redshift because features move out of the spectral range; and incorrect
but confident redshifts, notably for blends that receive the redshift of the
photometrically minor component [src: Sect. 2.0.6].

The LSST DESC study of degraded training sets (CMNN, GPz, FlexZBoost, PZFlow,
with trainZ as control) finds the Kullback–Leibler divergence, the Wasserstein
distance and the probability integral transform the most informative metrics of
training-set damage, and that inverse redshift incompleteness alone is too
simple a model of real incompleteness (Crafford et al. 2026, arXiv:2601.10797)
[src].

## 6. Hierarchical and forward population models
<!-- key: hierarchical-and-forward-population-models -->

These methods infer the galaxy population (and hence n(z)) jointly with
individual redshifts, instead of stacking per-galaxy posteriors computed under
a fixed prior.

**Why stacking is not enough.** Summing posteriors that share a model does not
propagate model uncertainty into n(z); in a Bayesian treatment likelihoods, not
posteriors, are combined (Newman & Gruen 2022, arXiv:2206.13633)
[src: Sect. 1.1]. Malz & Hogg 2020 show that the stacked estimator of n(z) is
systematically biased, worse at low S/N, and introduce CHIPPR, a probabilistic
graphical model they argue is the only self-consistent way to recover n(z) from
photo-z PDFs; posteriors produced under an implicit prior cannot be used for
inference, so they recommend that codes provide likelihoods or an explicit
prior (arXiv:2007.12178) [src].

| Approach | What it infers | Result | Reference |
|---|---|---|---|
| Hierarchical template model | piecewise-constant joint distribution of type and redshift, with individual redshifts | correct posteriors on type and redshift distributions in simulations, even with uninformative priors | Leistedt et al. 2016, arXiv:1602.05960 [src] |
| Hierarchical model with clustering | n(z) from photometry plus cross-correlation with a tracer; reduces to clustering redshifts without photometry | tightens posteriors and overcomes gaps in the spectroscopic prior | Sánchez & Bernstein 2019, arXiv:1807.11873 [src] |
| Same, on N-body simulations | adds marginalisation over the clustering–density mapping | a deliberate shift of Δz̄ ≈ 0.05 in the spectroscopic prior leaves a posterior bias Δz̄ ≲ 0.003 | Alarcon et al. 2020, arXiv:1910.07127 [src] |
| Forward population model (SPS + data model + selection) | tomographic n(z) without spectroscopic calibration | bias of the mean Δz ≲ 0.003 (GAMA) and ≃ 0.01 (VVDS) without tuning; generative chain: draw SPS parameters and z from the population model, emulated SPS photometry, noise from an uncertainty model, selection cuts on noisy photometry, bin labels from the photo-z estimator, repeated until N objects pass; in the validation the hyper-parameters are fixed, not inferred; GAMA biases 0.003 and 0.001 in two bins | Alsing et al. 2023, arXiv:2207.05819 [src: Sect. II.2, II.4, IV.3] |
| pop-cosmos | diffusion-model population prior fitted to 140,938 COSMOS galaxies (r < 25, 26 bands) by optimal transport | predicts colours for z < 4 | Alsing et al. 2024, arXiv:2402.00935 [src] |
| pop-cosmos on KiDS-1000 | SED-fitting posteriors for 4 million galaxies at 8.2 GPU s per galaxy | against ~185,000 DESI DR1 matches: BGS bias 2 × 10⁻³, σ_MAD = 0.03, 3.2% outliers; LRG bias 3 × 10⁻², σ_MAD = 0.05, 1.0% outliers | Halder et al. 2026, arXiv:2602.03930 [src] |
| GalSBI (phenomenological, image-level SBI) | luminosity functions, morphology, SEDs constrained with ABC against HSC deep images through UFig simulations | n(z) agrees with COSMOS photo-z within 1.5σ for all magnitude cuts | Fischbacher et al. 2024, arXiv:2412.08701 [src]; code arXiv:2412.08722 [src] |
| GalSBI-SPS | SPS-based population with literature parameters only | colours and magnitudes within 0.14 mag to i < 23; mean-n(z) offset 0.01–0.08 before fitting | Tortorelli et al. 2025, arXiv:2505.21610 [src] |
| GalSBI with clustering | adds subhalo abundance matching; constrained on DES Y3 images | mean redshifts agree with HSC COSMOS photo-z within 0.2–1.6σ; sample variance dominates for bright (< 24 mag) samples, population-model uncertainty for fainter ones | Fischbacher et al. 2026, arXiv:2606.23783 [src] |
| Learned SED prior | generative model (probabilistic autoencoder + normalising flow) of spectra, luminosities and redshifts trained on GalSBI-SPS mocks | SOM-bin mean redshifts within |Δ⟨z⟩| ≲ 0.0007(1+z) under controlled conditions | Frediani et al. 2026, arXiv:2609.26594 [src] |

Most numbers in the table come from simulations or from fields where many-band
photo-z serve as truth; the debate is in `open-questions.md` §2.

## 7. Calibration of n(z): direct and self-organising-map methods
<!-- key: calibration-of-n-z-direct-and-self-organising -->

Boundary: the per-bin mean-redshift priors adopted by KiDS, DES, HSC and the
shift each one produces in S8 are tabulated in `cosmo-weak-lensing`
(`references/systematics.md`, "Redshift distributions"). In short, DES Y6
reaches σ⟨z⟩ = 0.008–0.024 per bin and KiDS-Legacy SOM and clustering estimates
agree to better than 2σ in every bin (arXiv:2510.23566, arXiv:2503.19440)
[src]. This section describes the methods.

### 7.1 Direct reweighting
<!-- key: direct-reweighting -->

The calibration sample (spectroscopic, or many-band photometric) is reweighted
so that its distribution of photometric observables matches the target sample,
and the weighted redshift histogram estimates n(z); no individual photo-z is
needed. Lima et al. 2008 introduced the nearest-neighbour weights in
colour–magnitude space and showed that the method recovers n(z) better than
neural-network photo-z, provided the calibration sample spans the observables
of the target sample (arXiv:0801.3822) [src]. That proviso is the whole
difficulty at lensing depth.

### 7.2 Self-organising maps (SOM)
<!-- key: self-organising-maps-som -->

A SOM projects the multi-band colour space onto a 2D grid of cells; each cell
is a "phenotype" whose redshift distribution is read from calibration galaxies
in that cell. Weighting cell by cell by the wide-sample occupation gives n(z).

- **Coverage diagnostic.** Masters et al. 2015 used COSMOS photometry selected
  like the Euclid lensing sample to map where existing spectroscopy covers
  colour space and where it is systematically missing, and to plan targeted
  spectroscopy (arXiv:1509.03318) [src]; this is the origin of C3R2.
- **Gold selection (KiDS).** The KiDS spectroscopic compilation represents 99%
  of the effective 2D cosmic-shear sample; cells without spectra define a
  100%-represented "gold" sample per bin. On mocks, photometric noise, sample
  variance and spectroscopic selection give σ_Δ⟨z⟩ ≤ 0.006 per bin, and a
  maximal bias Δ⟨z⟩ = 0.013 ± 0.006 (≤ 0.025 at 97.5%) after quality flags
  (Wright et al. 2020, arXiv:1909.09632) [src]. KiDS-Legacy and HSC Y3 methods:
  `results.md` §3, error budgets.
- **Deep-field intermediary (DES SOMPZ).** A deep SOM built on many-band deep
  fields links the few-band wide SOM to redshifts, reducing sample variance,
  shot noise and selection effects: σ_Δz = 0.007 per bin in an idealised DES Y3
  simulation, 60% better than Y1 (Buchs et al. 2019, arXiv:1901.05005) [src].
  DES Y3 combines SOMPZ with clustering redshifts and shear ratios to σ⟨z⟩ ~
  0.01 (Myles et al. 2021, arXiv:2012.08566) [src]; DES Y6 adds near-infrared
  photometry to SOMPZ and names the lack of faint representative spectra the
  dominant uncertainty (Yin et al. 2025, arXiv:2510.23566) [src]. Its pipeline
  (SOMs, Eqs. 5–11, blending) is in `results.md` §3, error budgets.
- **HSC Y3.** A Bayesian hierarchical combination of two empirical methods
  (calibrated on spectroscopic and many-band photometric data over part of the
  footprint, with the resulting cosmic variance included) and
  cross-correlations with LRGs up to z < 1.2 (Rau et al. 2023,
  arXiv:2211.16516) [src].
- **Euclid.** With DR3-like mocks, defining tomography by the mean spec-z of
  SOM cells leaves none of ten bins within |Δ⟨z⟩| ≤ 0.002(1+z); defining it by
  individual photo-z puts eight of ten within requirement, and at most six when
  the calibration sample is degraded towards C3R2 (Roster et al. 2025,
  arXiv:2508.02779) [src]. A deep-to-wide transfer function that degrades deep
  photometry to wide-survey noise while keeping flux–error correlations reduces
  the mean biases in all bins and outperforms Balrog-type image injection on
  their metrics (Kang et al. 2026, arXiv:2601.02005) [src].

## 8. Clustering redshifts and shear ratios
<!-- key: clustering-redshifts-and-shear-ratios -->

### 8.1 Clustering redshifts
<!-- key: clustering-redshifts -->

The angular cross-correlation w_ps(θ, z_i) between the photometric sample and a
spectroscopic reference sample in thin slices z_i is proportional to n_p(z_i)
b_p(z_i) b_s(z_i) w_DM(z_i). The reference need not resemble the photometric
sample in galaxy properties, only overlap it on the sky and in redshift (Newman
2008, arXiv:0805.1409) [src]. Newman's simulations give RMS errors on the mean
and width of a Gaussian bin of 1.4 × 10⁻³ (σ_z/0.1) (Σ_p/10 arcmin⁻²)^−0.3
(dN_s/dz / 25,000)^−0.5 [src]. The estimator starts from the excess surface
density Σ_p(1 + w_sp(θ, z)) around reference objects at z, inverted with
power-law, linear-bias correlations [src: Sect. II.1, Eqs. 1–3]; ignoring a
linear bias evolution shifts ⟨z⟩ by (db/dz)/(2b_p) σ_z², at most 0.0025 for σ_z
= 0.1 [src: Sect. IV.1, Eq. 21]. Ménard et al. 2013 advocate using all scales,
not only linear ones, and applying the estimator cell by cell in photometric
space, which yields a clustering p(z) per galaxy type (arXiv:1303.4722) [src].
In the limit where every unknown source sits at one redshift, dN_u/dz ∝
w_ur(z_i), normalised to N_u, is unbiased; departures from it are why the
sample should be split into narrow voxels of photometric space first
[src: Sect. II.2.1, Eqs. 3–6; Sect. II.2.3].

The limitation is the unknown redshift evolution of the photometric sample's
bias b_p(z) (and magnification). Measured performance:

| Analysis | Reference sample | Result | Reference |
|---|---|---|---|
| KiDS mocks (MICE) | KiDS-like spectroscopic overlap | mean redshifts unbiased at |Δz| < 0.006 with bias evolution mitigated by auto-correlations; up to |Δz| ~ 0.04 when a colour-based n(z) replaces the truth as the model | van den Busch et al. 2020, arXiv:2007.01846 [src] |
| DES Y3 | redMaGiC + BOSS/eBOSS | mean z of bins recovered to RMS ~ 0.014 in simulations; marginalises magnification and bias evolution | Gatti et al. 2022, arXiv:2012.08569 [src] |
| DES Y6 | BOSS, eBOSS galaxies and quasars; 1.5–5 Mpc | importance sampling of SOM n(z) realisations with a WZ likelihood; weak at z > 1.1; S8 improves by ~10% (cosmic shear and 3×2pt); model w_xy = ∫dz b_x b_y n_x n_y w_m(z) + w^μ_xy with linear bias, a θ⁻¹ scale weight and halofit P(k) from CCL [src: Sect. II.1.1, Eqs. 2–5] | d'Assignies et al. 2025, arXiv:2510.23565 [src] |
| Euclid mocks (Flagship) | BOSS, DESI, NISP-like | mean z of ten bins to ~0.01 or better on the mock area; extrapolated to ~6000 deg² the statistical error beats σ(⟨z⟩) < 0.002(1+z) by at least 3×, but systematic biases limit accuracy | Naidoo et al. 2023, arXiv:2208.10503 [src] |
| Euclid mocks (Flagship 2) | BOSS, DESI, NISP | means and widths of all bins to z_phot ≤ 1.6 within requirement; photometric-sample bias is the main limitation; 1-halo term forces a minimum separation of 1.5 Mpc; each bin correlated with one tracer (DESI BGS, BOSS, DESI LRG, ELG, NISP) on 1000–2500 deg² patches; requirement met in every bin with the shifted-stretched model, while the conservative Gaussian-process model exceeds it slightly in bins 1, 3 and 7 unless patches are doubled [src: Sect. 5] | d'Assignies et al. 2025, arXiv:2505.10416 [src] |

### 8.2 DESI as a common calibrator
<!-- key: desi-as-a-common-calibrator -->

DESI spectra serve as colour-space calibration sample (COSMOS, XMM/VVDS, DC3R2)
and clustering reference; the DES, HSC, KiDS recalibrations (arXiv:2510.25419,
arXiv:2512.15964) [src] are in `results.md` §3 and `open-questions.md` §1,
their S8 effects in `cosmo-weak-lensing`.

### 8.3 Shear ratios
<!-- key: shear-ratios -->

At fixed lenses, the ratio of tangential shears in two source bins depends, in
the geometric limit, only on ratios of angular-diameter distances (Jain &
Taylor 2003, arXiv:astro-ph/0306046) [src]. DES Y3 models the small-scale
ratios in full (power-spectrum integration, intrinsic alignments,
magnification) and uses them as an extra likelihood: source-redshift
constraints tighten by up to 38% over the prior in some bins, cosmic-shear S8
by up to 31% and 3×2pt by up to 10% (Sánchez et al. 2022, arXiv:2105.13542)
[src]. The ratios are a cross-check on redshifts and intrinsic alignments
together, not a stand-alone redshift calibration.

## 9. Redshift PDFs: meaning and storage
<!-- key: redshift-pdfs-meaning-and-storage -->

Newman & Gruen 2022 distinguish three objects that are all written p(z):
Bayesian posteriors (degree of belief, can marginalise model uncertainty),
frequentist probabilities (fraction of indistinguishable galaxies at each z
under a fixed model; these may be stacked), and likelihoods p(photometry | z)
for a fixed template (arXiv:2206.13633) [src: Sect. 1.1]. Point estimates
(mode, mean, mean of the main peak) are being abandoned for cosmology
[src: Sect. 1.1]. Malz & Hogg 2020 add that a posterior produced under an
implicit prior cannot be used for inference (arXiv:2007.12178) [src].

Storage of PDFs for billions of galaxies is a design choice with measurable
cost:

- A sparse basis of Gaussian and Voigt functions chosen by orthogonal matching
  pursuit needs about half the parameters of a multi-Gaussian fit; 10–20
  integers per galaxy rebuild CFHTLenS PDFs and N(z) to 99.9% of the 200-value
  originals (Carrasco Kind & Brunner 2014, arXiv:1404.6442) [src]. Each PDF is
  pz_k = D δ_k + ε_k over an over-complete dictionary, δ_k sparse, found by OMP
  [src: Sect. 3.3, Eq. 2]; packing basis index and 16-bit amplitude into one
  4-byte integer, ten bases rebuild a 200-point PDF to 99.5% in 40 bytes;
  multi-Gaussian fits need 14 floats on average [src: Sect. 4].
- `qp` compares quantiles, samples and step functions: quantiles and samples
  outperform step functions, and the best format depends on the PDFs and on the
  fidelity metric (Malz et al. 2018, arXiv:1806.00014) [src]. Judged by the KLD
  and moment errors of individual PDFs and of the stacked n̂(z), the histogram,
  the most common format, loses most unless many parameters are stored, so it
  is not recommended for LSST; with ~100 numbers per galaxy LSST can store more
  than one code's output without significant loss, and the best format for
  single PDFs need not be the best for a science metric [src: Sect. II.2, V].

## 10. Metrics, requirements and codes
<!-- key: metrics-requirements-and-codes -->

**Metrics.** Point-estimate metrics (bias, σ_NMAD, outlier fraction) say little
about PDFs. The LSST DESC comparison of twelve codes with perfect priors found
systematic biases and over- or under-broad PDFs in many popular codes, proposed
the conditional density estimate (CDE) loss when true redshifts but not true
PDFs are known, and called for science-specific metrics (Schmidt et al. 2020,
arXiv:2001.03621) [src]. KL divergence, Wasserstein distance and the PIT are
the most sensitive to training-set damage (arXiv:2601.10797) [src]. The Euclid
challenge defines PIT values C_i = CDF_i(z_i) and the CRPS [src: Eqs. 4–5],
plus the fractions F_005 and F_015 of shifted, stacked PDFs within ±0.05(1+z)
and ±0.15(1+z) of the mode, the Euclid requirement metric; no code gave a flat
PIT, template PDFs were too narrow (U-shaped PIT), GPz, ANNz and GBRT too
broad, and the CRPS cannot separate bias from scatter (arXiv:2009.12112)
[src: Sect. 4.2].

**Requirements.** The per-survey requirements on the mean and width of n(z) are
tabulated in `results.md` §6.

**Frameworks.** RAIL (LSST DESC) provides forward-modelled degraded photometry,
a common interface to many per-galaxy and ensemble estimators, and built-in
metrics; it is not specific to LSST (The RAIL Team 2025, arXiv:2505.02928)
[src]. Euclid's PHZ processing function produces classification, photo-z and
physical properties (arXiv:2503.15306) [src]; Phosphoros includes the
passband-variation correction (arXiv:2310.14716) [src]. The template and
machine-learning codes are in §4–5.

## Not verified
<!-- key: not-verified -->

- Closed: the LSST DESC SRD photo-z requirements were read in the SRD body
  (arXiv:1809.01669, Sect. 5.1–5.3); see `results.md` §6.
