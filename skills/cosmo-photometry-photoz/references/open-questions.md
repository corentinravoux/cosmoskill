# Photometry and photometric redshifts — open questions

Scope: live controversies, method debates, what the next data will decide,
forecasts, and claims that still circulate but are stale or wrong.
Snapshot: 2026-10-16

Flags: `[src]` read this session in the abstract of the cited paper;
`[src: Sect. n]` read in the body; `[sec]` from a named secondary source.
Forecasts are labelled.

## 1. Did redshift calibration make Stage-III lensing S8 low?
<!-- key: did-redshift-calibration-make-stage-iii-lensing -->

The question belongs to `cosmo-weak-lensing`, which holds the S8 values; the
photo-z side of it is this. Independent recalibrations move n(z) by amounts
comparable to the quoted priors. DESI redshifts in COSMOS shift the KiDS-1000
bin means by −0.028 on average (Blanco et al. 2025, arXiv:2512.15964) [src];
the unified DESI calibration of DES, HSC and KiDS agrees with DES Y3 and HSC
Y1 but not with the KiDS-1000 means, which it attributes to a mismatch of
photometric noise between COSMOS and the KiDS gold sample, without a
significant change in the KiDS growth estimate (Lange et al. 2025,
arXiv:2510.25419) [src]. The body names three candidate causes: its use of
COSMOS2020 photo-z, which raise mean redshifts even at fixed SOM cell; KiDS
imaging in COSMOS being deeper than the wide survey, which it does not
reweight while KiDS-1000 did through the SOM; and the KiDS gold cut, Eq. 13,
defined and calibrated on the same O(10) spectra per cell, which truncates
bin 1 near z ≈ 0.6 by construction [src: Sect. VI.2]. Bin 1 differs mostly
in its high-z tail: the medians agree (0.229 against 0.234)
[src: Sect. V.3]. Forward modelling of KiDS-1000 with two galaxy
population models (pop-cosmos and the semi-analytic shark) differs by Δz ~
0.05–0.1 in the first and last bins, comparable to the spectroscopic
reweighting uncertainties (Leistedt et al. 2026, arXiv:2602.03935) [src]. A
template-based hierarchical model of KiDS+VIKING-450 raises S8 to 0.756 ±
0.039 and lowers the tension with Planck from 2.3σ to 1.9σ (Kyriacou et al.
2026, arXiv:2605.15078) [src]. Taken together: the method, not only the data,
moves the mean redshifts of the extreme bins by several hundredths. Which
calibration is right is not settled.

## 2. Spectroscopic reweighting versus forward modelling
<!-- key: spectroscopic-reweighting-versus-forward -->

*For spectroscopic calibration.* It is empirical and model-light. Its
failure modes are known and partly quantified: colour selection biases the
weighted mean by Δz ~ 0.015 and redshift-confidence cuts by 0.005–0.05 in
DES Y1 simulations (arXiv:2003.10454) [src]; one wrong redshift per thousand
inflates the inferred width by 0.0024(1+z), in tension with the LSST
tolerance of 0.003(1+z)
(arXiv:2206.13633) [src: Sect. 4.2.2].
*For forward modelling.* It replaces implicit priors with explicit
population models, uses heterogeneous data, and models blending and
selection in the likelihood (Tortorelli & Grün 2026, arXiv:2605.06790)
[src: Sect. 3.0.4]. The same review lists its risks: a flexible prior is
still a prior and can be mis-specified, emulators fail in corners of
parameter space, simulators omit systematics, and amortised posteriors can be
mis-calibrated while point predictions look excellent; it asks for coverage
tests, posterior predictive checks and end-to-end parameter-shift tests
[src: Sect. 3.0.4]. The KiDS-1000 population-model dependence (above) is the
first real-data measure of that risk.
*Hybrid.* Hierarchical models that add clustering to photometry are robust
to a deliberate 0.05 shift of the spectroscopic prior (residual ≲ 0.003,
arXiv:1910.07127) [src], so the camps are converging on joint inference.

## 3. Are clustering redshifts good enough for Stage IV?
<!-- key: are-clustering-redshifts-good-enough-for-stage -->

The information content is sufficient in principle, but it has not been
demonstrated that the required accuracy survives astrophysical systematics
(magnification, bias evolution, small-scale non-linearity)
(arXiv:2206.13633) [src: Sect. 4.2.6]. On Euclid mocks the statistical error
beats the requirement by a factor ≥ 3 while systematic biases limit the
accuracy (arXiv:2208.10503) [src]; the newer Euclid pipeline meets the
requirement for bins to z_phot = 1.6 with a 1.5 Mpc minimum scale
(arXiv:2505.10416) [src], with its optimistic shifted-stretched n(z)
model; the conservative Gaussian-process model misses it slightly in three
of ten bins on 1000 deg² patches [src: Sect. 5]. In data, clustering redshifts have so far served
as a cross-check or as importance weights on SOM realisations, not as the
sole calibration (arXiv:2510.23565, arXiv:2503.19440) [src]. Two extensions
target the weak points: Lyα-forest cross-correlations for the 2 < z < 3 tail
(σ_z/(1+z̄) = 0.006 at z̄ = 2 on DESI-5yr × LSST-10yr mocks, **forecast**;
Hang et al. 2026, arXiv:2601.16962) [src], and a public framework,
Tomographer, with precomputed pair information for 3 million SDSS
spectroscopic galaxies and quasars to z ~ 4 over 10,000 deg², which returns
b(z) dN/dz for any catalogue or intensity map (Chiang et al. 2026,
arXiv:2608.03415) [src].

## 4. What n(z) uncertainty model to propagate
<!-- key: what-n-z-uncertainty-model-to-propagate -->

Mean shifts per bin were the Stage-III default. An LSST DESC study of
shift, shift-and-stretch, Gaussian-process and PCA models argues that
Stage-IV 3×2pt must go beyond shift and stretch; a five-parameter PCA model
costs 5% on S8 but halves the bias in Ω_m and σ8, and all models can be
marginalised analytically (Ruiz-Zapatero et al. 2026, arXiv:2604.24425)
[src: abstract]. For the Euclid DR1 photometric clustering sample the mean must be
known to 0.004(1+z) to keep 80% of the w0wa 3×2pt constraining power, and
the width then matters little (Euclid Collaboration: Bertmann et al. 2026,
arXiv:2604.00805) [src: abstract] (**forecast**). Against the "width does not matter"
reading: spatially varying (anisotropic) n(z) from observing conditions
biases σ8 low by 1.7σ and Ω_m high by 1.4σ in an LSST-like 2×2pt set-up with
KiDS-like selection, while staying below 1σ for KiDS- and DES-like set-ups
(Zhang et al. 2026, arXiv:2609.15542) [src: abstract] (**forecast**).

## 5. Can machine-learning photo-z deliver usable PDFs?
<!-- key: can-machine-learning-photo-z-deliver-usable-pdfs -->

In the Euclid challenge all methods gave reliable point estimates but
several machine-learning methods failed to give useful PDFs
(arXiv:2009.12112) [src]; in the LSST DESC comparison many codes were biased
or over/under-broad even with perfect inputs (arXiv:2001.03621) [src]. The
argument of Malz & Hogg 2020 that posteriors under implicit priors cannot be
used for inference (arXiv:2007.12178) [src] applies to every discriminative
method (arXiv:2605.06790) [src: Sect. 2.0.5]. The counter-trend is domain
adaptation (arXiv:2512.11700) [src] and manifold methods robust to biased
training sets (arXiv:2512.09032) [src], judged so far on point metrics.

PDF calibration in the bodies. In CANDELS the fraction of true redshifts
inside the nominal 68.3% interval ranged from 2.5% to 89% across eleven
codes with comparable point scatter, and inside the 95.4% interval from 2.9%
to 97%; in the LSST DESC test with perfect inputs every code's PIT deviated
from uniform by an order of magnitude more than the trainZ control, which
returns the training-set histogram for every galaxy (Newman & Gruen 2022,
arXiv:2206.13633) [src: Sect. 4.1.1]. Nominally Bayesian codes can also fail
to marginalise over template type, so their output matches no definition of
a PDF [src: Sect. 4.1.1].

**Storage of joint posteriors.** One-dimensional compression schemes
(arXiv:1404.6442, arXiv:1806.00014) break down for p(z, G | photometry): a
100-point grid in five dimensions (z, mass, sSFR, metallicity, dust) is 10⁸
numbers per object, nearly an exabyte per billion objects; the review's
options are posterior samples (10–100 per object), emulators fast enough to
avoid storage, or p(z) plus a compact model of p(G | z, photometry), and
aggregate distributions should combine likelihoods, not posteriors
(arXiv:2206.13633) [src: Sect. 4.1.4]. Which option a Rubin- or Euclid-scale
catalogue adopts is open.

## 6. Which dust map
<!-- key: which-dust-map -->

SFD over-corrects in a way correlated with large-scale structure
(arXiv:1808.03294, arXiv:2306.03926) [src], and the DESI stellar map differs
from SFD by up to 80 mmag in E(B−V) (arXiv:2409.05140) [src: abstract]. Whether the
corrected infrared map (CSFD) or stellar-reddening maps should be the
default is open; stellar maps are limited by the photometric calibration they
are meant to serve (arXiv:2409.05140) [src].

## 7. SOM tomography: by cell spec-z or by photo-z?
<!-- key: som-tomography-by-cell-spec-z-or-by-photo-z -->

On Euclid DR3-like mocks, defining bins by the mean spec-z of SOM cells
leaves no bin within requirement, while binning on individual photo-z
leaves eight of ten within it (six with a C3R2-like calibration sample)
(arXiv:2508.02779) [src] (**forecast**). This reverses a common Stage-III
choice. The reason given is that SOM cells can hold heterogeneous, even
bimodal, populations whose cell-mean redshift represents neither, while
individual photo-z PDFs are mostly unimodal and sub-sample the cell
[src: arXiv:2508.02779, Sect. 4.4]. Against it, DES Y6 keeps SOM-cell
binning (by the mode of the cell n(z)): the gain relies on unbiased
individual photo-z, which DES cannot assume, and a study it cites (Kang et
al., in preparation) finds the gain marginal for DES-like photometry once a
realistic transfer function such as Balrog is included
(arXiv:2510.23566) [src: Sect. 4.1].

## 8. How much spectroscopy, and where
<!-- key: how-much-spectroscopy-and-where -->

The fiducial training sample of Newman et al. (30,000 objects to i = 25.3
over 15 fields of ≥ 20 arcmin, ≥ 75% success, [OII] resolved at z ≳ 0.7)
would take more than 1800 dark nights with DESI or DEIMOS, roughly 400 with
Subaru/PFS, and fewer than 200 with proposed facilities such as MSE, the ESO
SpecTel project or GMT/MANIFEST (Newman & Gruen 2022, arXiv:2206.13633)
[src: Sect. 5.2] (**forecast**). The DESI-Deep pilot finds DESI far more
efficient at m_i ≤ 24.5 than aperture scaling predicts, and proposes it as
the definitive sample for early LSST (arXiv:2604.06143) [src]. C3R2 has
raised coverage of Euclid colour space to 91% (arXiv:2106.11367) [src];
DESI DC3R2 spans 56% of the Euclid/LSST colour space (arXiv:2309.13109)
[src].

## 9. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

- **Rubin LSST**: first ComCam photo-z already meet Y1 bias and scatter
  requirements on small fields (arXiv:2510.07370) [src]; n(z)
  characterisation at the level the DESC SRD asks for is untested on data.
- **Euclid**: Q1 photo-z need a bias correction for cosmology
  (arXiv:2503.15306) [src]; DR1 will be the first test of SOM plus
  clustering calibration at Euclid depth.
- **SPHEREx**: all-sky low-resolution spectra forecast 19 million galaxies
  with σ_z < 0.003(1+z) (**forecast**, arXiv:2312.04636) [src: abstract].
- **DESI**: deep and secondary-target samples (DESI-Deep, DC3R2) and
  clustering references to z ~ 3 through the Lyα forest
  (arXiv:2601.16962) [src].

## 10. Stale or wrong claims that circulate
<!-- key: stale-or-wrong-claims-that-circulate -->

- "Photo-z precision is the problem." For lensing and angular clustering the
  limiting quantity is characterisation of n(z), not per-galaxy scatter
  (arXiv:2206.13633) [src: Sect. 1.1].
- "Stacking per-galaxy PDFs gives n(z)." Biased, worse at low S/N
  (arXiv:2007.12178) [src]; only frequentist p(z) under a fixed model stack
  (arXiv:2206.13633) [src: Sect. 1.1].
- "SFD E(B−V) can be used as is." It needs a 14% recalibration,
  E(B−V) = 0.86 E(B−V)_SFD (arXiv:1012.4804) [src: abstract, Sect. I], and
  it contains extragalactic structure (arXiv:1808.03294) [src: abstract].
- "1% photometric calibration is the state of the art." DES Y6 relative
  uniformity is below 1.8 mmag; the ~1% figure is the absolute scale
  (arXiv:2305.01695) [src].
- "A representative spectroscopic sample fixes everything." Even confident
  redshifts fail at 0.15–1%, and f_inc ≲ 10⁻³ is needed for LSST
  (arXiv:2206.13633) [src: Sect. 4.2.2].
- "Only the mean of n(z) matters." True for the Euclid DR1 clustering sample
  in their tests (arXiv:2604.00805) [src], not for anisotropic n(z) in
  LSST-like set-ups (arXiv:2609.15542) [src] nor for Stage-IV 3×2pt
  uncertainty models (arXiv:2604.24425) [src].

## Not verified
<!-- key: not-verified -->

- The current status and dates of Euclid DR1 and Rubin LSST data releases
  were not read this session; see `cosmo-surveys-facilities`.
- Whether KiDS has published the full cosmology re-analysis with pop-cosmos
  n(z) announced in arXiv:2602.03935 was not checked.
