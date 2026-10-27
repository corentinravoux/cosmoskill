# Chromatic effects and Milky Way extinction — cosmo-photometry-photoz dossier

Scope: how extinction coefficients are computed for a passband and a
source spectrum, how the SFD, recalibrated SFD, CSFD and DESI stellar
reddening maps are built and what each assumes, how an extinction or
passband error propagates into colours, photo-z and galaxy counts, how
passband variations are corrected inside a photo-z code, and how a dust
map is tested before an analysis uses it.
Snapshot: 2026-10-19.
From: Scope file; DES and Rubin calibration programmes; Newman & Gruen
2022 review, Sect. 4.2.4 (copied from `references/subtopics.tsv`).

Already in L2, not repeated here: the families of maps and their headline
properties (`physics-and-methods.md#milky-way-extinction`), the size of
chromatic errors and of dust-map errors with their mitigations
(`systematics.md#chromatic-errors`, `systematics.md#galactic-extinction`),
the open question of which map to adopt
(`open-questions.md#which-dust-map`). Chromatic corrections inside the
global calibration (FGCM linearised corrections, sizes per band) are in
`deep/photometric-calibration.md`, Step 5. Imaging-systematics
regressions that use E(B−V) as a template map belong to
`cosmo-data-pipelines` (`deep/lss-catalogues.md`); supernova colour and
host dust to `cosmo-supernovae`.

Symbols. E(B−V): colour excess, in the SFD calibration unless stated
(E(B−V)_SFD); A_b: extinction in band b, A_b = R_b E(B−V); R_b: extinction
coefficient of band b; R_V = A_V/E(B−V); W_b(λ) or T(λ): system
throughput of band b; S(λ): source spectrum; F99: the Fitzpatrick (1999)
extinction law; Δλ: shift of the mean wavelength of a passband between
the standard and the actual one; s(z) = d log₁₀ N(z, > m)/dm and α =
2.5 d log N/dm: number-count slopes in the notation of the two papers
that use them; b_g, b_r: linear clustering bias of a galaxy sample and of
a reference sample. <!-- num: not a value -->

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Pick the reddening map and know its unit
<!-- key: step-1-pick-the-reddening-map-and-know-its-unit -->

- **SFD and its recalibration.** The blue-tip work recommended
  E(B−V) = 0.86 E(B−V)_SFD, confirmed with SDSS stellar spectra, and an
  R_V = 3.1 F99 law rather than O'Donnell or Cardelli; spectrum-based and
  blue-tip reddening coefficients agree to −3%, 1%, 1%, 2% in u−g, g−r,
  r−i, i−z after removing a 4% normalisation difference (Schlafly &
  Finkbeiner 2011, arXiv:1012.4804) [src: abstract, Sect. I]. Per-star
  uncertainties are 56, 34, 25 and 29 mmag in those colours [src:
  abstract]. Reddening found for K stars at ~1 kpc matches that of
  standard stars at ~4 kpc, so the dust lies mostly within 1 kpc over the
  SDSS footprint; this matters because SFD was calibrated on galaxies,
  which lie behind all the dust [src: Sect. V.3.2].
- **CSFD.** SFD minus a reconstructed large-scale-structure (CIB) map: a
  linear combination of WISE galaxy-density templates (plus AKARI
  far-infrared galaxies, coefficient fixed) is fitted so that its
  tomographic cross-correlations with SDSS galaxies and quasars match
  those of SFD, 180 coefficients, 200 block-bootstrap end-to-end
  realisations, the median map at 6.1′ resolution (N_side = 2048) and its
  standard deviation as error (Chiang 2023, arXiv:2306.03926)
  [src: Sect. III.4]. The correction has no monopole by construction, a
  typical amplitude of 0.7 mmag per beam, about 3.5% of SFD at high
  latitude with a tail to 40% on a few sight lines, mostly towards nearby
  clusters; the typical reconstruction error is 0.2 mmag [src:
  Sect. III.5, Fig. 3]. In the Galactic plane, the Magellanic Clouds and
  M31 the original SFD values are kept [src: Sect. III.4]. Map unit and
  calibration are those of SFD, so CSFD can be swapped in directly [src:
  Sect. V.3].
- **DESI stellar reddening.** E(a−b) = (a−b)_obs − (a−b)_E=0 (Eq. 1), the
  intrinsic colour synthesised from the best-fit stellar model of the DESI
  spectrum, measured for g−r and r−z; converted to E(B−V) in the SFD
  normalisation by E(B−V) = E(g−r)/1.049 and E(r−z)/0.954 (Eqs. 5–6),
  1.049 and 0.954 being R_g − R_r and R_r − R_z for DECam (Zhou et al.
  2024, arXiv:2409.05140) [src: Sect. 3.1]. The authors keep the original
  SFD normalisation because "the exact definition of E has no effect on
  our E(g−r) and E(r−z) measurements" [src: Sect. 3.1, footnote 6]. North
  (BASS/MzLS) measurements are shifted by −9.5 mmag (g−r) and −5.2 mmag
  (r−z) to the South zero point and rescaled to DECam coefficients;
  inverse-variance-weighted HEALPix maps are given at N_side 128, 256 and
  512 (27.5′, 13.7′, 6.9′); empty pixels are inpainted only for power
  spectra, and the authors "advise caution" in using inpainted values
  [src: Sect. 3.4].

### Step 2. Compute R_b for your passband
<!-- key: step-2-compute-rb-for-your-passband -->

Schlafly & Finkbeiner (arXiv:1012.4804) tabulate, for 88 passbands
[src: abstract] and R_V = 2.1, 3.1, 4.1, 5.1 [src: App. A],

  Δm_b = −2.5 log [∫ dλ W_b S 10^(−A(λ) Δm_1μm/2.5) / ∫ dλ W_b S]
  (arXiv:1012.4804, Eq. A1),

with A(λ) the F99 law normalised to 1 at 1 μm (arXiv:1012.4804), Δm_1μm equal to N = 0.78
times the 1 μm extinction of SFD under SFD's O'Donnell R_V = 3.1 law, S a
7000 K, log Z = −1, log g = 4.5 synthetic spectrum, in the limit of small
E(B−V)_SFD; the coefficients in Table 6 multiply E(B−V)_SFD directly
[src: App. A, Table 6 note]. Two caveats from the paper: the synthetic
spectra cover 2500–10500 Å and are extrapolated as a blackbody, which biases
near-infrared coefficients "somewhat high", about 1% for UKIRT against a
λ⁻¹ spectrum; and SFD's own table had multiplied some source spectra by a
spurious factor λ, corrected there [src: App. A]. Two numbers to keep
apart: 0.86 rescales E(B−V)_SFD, 0.78 normalises the 1 μm extinction
inside Eq. A1 [src: Sect. I; App. A].

DESI computes its coefficients the same way (F99, R_V = 3.1, a 7000 K,
[Fe/H] = −1 F dwarf) with airmass 1.3 for DECam and 1.1 for BASS/MzLS,
because filter curves and mean airmass differ between the two imaging
sets; R_x = A_x/E is "an approximation for broad-band filters as R_x will
be different at high extinction" [src: arXiv:2409.05140, Sect. 3.1,
Table 3, footnote 5].

### Step 3. Decide whether the source SED matters
<!-- key: step-3-decide-whether-the-source-sed-matters -->

- *Stars.* For a fixed E(B−V), the hottest DESI star (6500 K) has ~4%
  more reddening in g−r and ~1% in r−z than the coolest (5000 K); at the
  median E(B−V) = 0.05 of the footprint this is 2 mmag in E(g−r) and 0.5
  mmag in E(r−z), below the random errors and averaged over many stars per
  pixel, so it is neglected [src: arXiv:2409.05140, Sect. 5.4]. Synthetic
  colours shift by less than 0.5 mmag when 0.05-mag steps of extinction
  are added to or removed from the spectra (−0.05 < E(B−V) < 0.25) [src:
  Sect. 5.3].
- *Galaxies.* A colour term that depends only on the dust column ignores
  the unknown galaxy SED, which "needs to be taken into account in order
  to compute an accurate correction"; Phosphoros computes SED-dependent
  flux corrections for each template, following Galametz et al. 2017
  (Euclid Collaboration: Paltani et al. 2024, arXiv:2310.14716)
  [src: App. B.1]. The same principle as the passband correction of
  Step 5, applied to every model in the grid.

### Step 4. Apply the correction to the catalogue
<!-- key: step-4-apply-the-correction-to-the-catalogue -->

Fluxes and their errors are divided by the transmission 10^(−0.4 A_b)
before any colour is formed; the Legacy Surveys DR8 photo-z do this with
SFD and the catalogue coefficients before computing asinh magnitudes
(arXiv:2203.01949) [src: Sect. 2.1.2]. If the reddening map comes from
the same imaging as the sources (DESI imaging for both), the spatially
varying zero-point errors cancel in dereddened colours, but not in
dereddened magnitudes, and the absolute zero-point error remains in both
[src: arXiv:2409.05140, Sect. 5.1].

### Step 5. Correct passband (chromatic) variations inside the photo-z fit
<!-- key: step-5-correct-passband-chromatic-variations -->

Paltani et al. multiply each model flux r_T^α in the template χ² by a
correction factor

  C_{T→T′}^α = [∫ s^α T′ λ dλ / ∫ s^α T λ dλ] × [∫ T dλ/λ / ∫ T′ dλ/λ]
  (arXiv:2310.14716, Eq. 7),

so that χ²_α = Σ_T (f_T′ − a C r_T^α)² / σ_T′² (Eq. 6) [src: Sect. 5.2].
Assuming the mean-wavelength shift Δλ = ∫ (T′ − T) λ dλ (Eq. 8) carries the
effect, C becomes a function of Δλ alone, approximated by
a_T^α Δλ² + b_T^α Δλ + 1 (Eq. 9) for all parameters, redshifts and the
four CWW templates; a and b are precomputed per passband and model, and
for stacked exposures Δλ is the exposure-time-weighted mean [src: Sect.
5.2]. The point of this choice: Δλ "does not depend on the SED", so the
catalogue only needs one number per band per object [src: Sect. 5.2].

Why it is needed (arXiv:2310.14716): in a step-function toy model, Δz = −0.0033 Δμ per nm of
mean-wavelength shift of the band containing the Balmer break, so 1 nm
already matches Euclid's Δz/(1+z) = 0.002 requirement; off-axis passbands
move blue, so using the central passband biases photo-z high [src: Sect.
4.2.1].

Size per band for galaxies. With a 2 nm instrumental shift, peak-to-valley
synthetic chromatic errors for an elliptical over 0 < z < 2 are 79, 36,
28, 26, 17 and 22 mmag in ugrizY; a PWV change from 3 to 10 mm gives 4, 4,
26, 20 mmag in r, i, z, Y; airmass 1.2 → 1.8 gives 26 and 21 mmag in u
and g (Li et al. 2016, arXiv:1601.00117) [src: Table 4]. Drops in Δr, Δi,
Δz, ΔY near z = 0.4, 0.8, 1.1, 1.3 come from the 4000 Å break; star-derived
corrections at fixed g − i only partly correct galaxies, and a colour
closer to the band (g−r for g, z−Y for z and Y) "might be better" [src:
Sect. V.2]. Residuals below ~1 mmag need PWV known to ~10% and AOD and α
to 0.02 and 0.1; below 2 mmag in most bands needs bandpass shifts known
to ~0.2 nm [src: Sect. IV.3, Table 2]. Δm is defined relative to a G2V
reference star, Eq. 9 [src: Sect. III].

### Step 6. Test the map against the extragalactic sky
<!-- key: step-6-test-the-map-against-the-extragalactic -->

- **Cross-correlation with reference objects.** ⟨δ_r(φ, z) δE(B−V)(φ+θ)⟩
  = ⟨δE^EG(θ, z)⟩_r (Eq. 18): Galactic dust does not correlate with
  extragalactic references, so any excess reddening around them, measured
  in redshift slices after subtracting a 1° running mean, is
  extragalactic contamination (Chiang & Ménard 2019, arXiv:1808.03294)
  [src: Sect. II.2]. Stacks around samples not used to build the map
  (2MASS galaxies, Gaia AGN) are the independent check of CSFD; Gaia stars
  show no correlation in either map [src: arXiv:2306.03926, Sect. IV.2].
- **Galaxies as back light.** Reselect a target class with each map and
  compare density maps; the DESI ELG density correlates with
  E(B−V)_SFD − E(B−V)_DESI at ~80% on the largest scales, and ELGs
  reselected with the DESI map (fibre g < 23.6, 0.5 mag brighter than
  nominal, to suppress depth effects) are "significantly more uniform"
  [src: arXiv:2409.05140, Sect. 4.2].
- **Two colours, one dust column.** If the extinction law is universal,
  E(B−V) from g−r and from r−z must agree; their difference map traces
  zero-point errors and mostly disappears after a Gaia-based zero-point
  correction [src: arXiv:2409.05140, Sect. 5.1, Fig. 15].
- **Power spectra.** DESI and SFD maps differ by ~10% at ℓ ≲ 100, mostly
  SFD systematics; the DESI map has more power at ℓ ≳ 100, which noise
  (dominant only at ℓ ≳ 800) and the SFD beam (6.1′, ℓ ≈ 1800) do not
  explain [src: arXiv:2409.05140, Sect. 4.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

| Map | Assumes | Buys | Costs | Used or advocated by | Comparison |
|---|---|---|---|---|---|
| SFD with 0.86 and F99 coefficients | dust emission traces reddening; one temperature correction | full sky, high S/N, ~6′ | CIB/LSS imprint; normalisation and law need the recalibration | the default since 1998 [src: arXiv:2306.03926, Sect. V.3] | spectra prefer F99 R_V = 3.1 [src: arXiv:1012.4804, abstract] |
| CSFD | the CIB is linear in WISE density templates | SFD properties with detectable LSS removed, tested to at least z = 3 and θ = 4° | one-halo residuals: 7% of the SFD peak around 2MASS galaxies, 13% around BGS | DESI agreed to adopt it [src: arXiv:2306.03926, Sect. V.1] | extragalactic excess consistent with zero against SDSS references [src: Sect. IV.2] |
| DESI stellar | stellar models predict intrinsic colours | direct reddening; finer structure than SFD | limited by imaging zero points, ~6 mmag; sparse pixels; DESI imaging footprint only | DESI ELG systematics modelling [src: arXiv:2409.05140, Sect. 4.2] | up to 80 mmag from SFD in the NW NGC [src: Sect. 4.1] |

Why SFD stayed the default, as Chiang argues: less CIB than most Planck
emission maps, higher S/N than Pan-STARRS or Gaia stellar maps, higher
resolution and a more direct dust tracer than HI maps [src:
arXiv:2306.03926, Sect. V.3]. DESI did not apply the Gaia zero-point
correction to its map because it imprints Gaia scan patterns; the
correction lowers the DESI−SFD difference power by only 5–20% at ℓ ≲ 300
[src: arXiv:2409.05140, Sect. 5.1].

**Colour term or SED-based passband correction.** A colour term
m_|x₀ ≈ m_|x − δk(x)(c_|x₀ − c⁰(x)) (Eq. 10, after Betoule et al. 2013)
approximates the SED by g − i, which may not suit passbands far from g and
i such as Euclid Y_E J_E H_E, and correlates the correction with g and i;
the SED-based correction uses all bands through the templates and needs no
SED at the photometric extraction stage, which matters when catalogues
from several telescopes are combined [src: arXiv:2310.14716, Sect. 7.2].
For machine-learning photo-z only k-nearest-neighbour methods take the
correction easily, by correcting the training fluxes to each target's
passbands; others would need retraining per colour space [src:
Sect. 7.4].

## How an error propagates
<!-- key: how-an-error-propagates -->

- **Counts.** A magnitude bias δm changes counts as N̂(m) = N(m + δm) ≈
  (1 + α δμ) N(m), δμ ≈ −0.92 δm (Eqs. 9–12); the dereddened overdensity
  is δ̂ ≃ δ + α δμ (Eq. 15) and a cross-correlation acquires terms α₂⟨δ₁
  δμ⟩ + α₁⟨δ₂ δμ⟩ + α₁α₂⟨δμ²⟩ (Eq. 16) [src: arXiv:1808.03294,
  Sect. II.1]. In Huterer's notation (δN/N)_sys = ln(10) s(z) R
  δE(B−V) (Eq. 37), "very roughly of order δE(B−V)" for s ~ 0.1–1 and R ~
  1–5 (Huterer et al. 2012, arXiv:1211.1015) [src: Sect. IV.1].
- **Cosmology from counts.** Parameter biases scale as s(z)², because the
  calibration field adds power ∝ |c_ℓm|² (Eq. 40); taking the Peek &
  Graves SFD corrections as the error map in DES i (R = 1.595), the bias
  exceeds the tolerated bias/error for f_NL at s ≈ 0.3 and for the dark
  energy figure of merit at s ≈ 0.8 [src: arXiv:1211.1015, Sect. IV.3,
  Fig. 5]. These are **forecast** settings.
- **Magnification.** For foreground galaxies at z = 0.2 and background
  quasars at z = 1.5 with α_q − 1 ≈ 0.2 (SDSS depth), the SFD-induced
  correlation is about 50% of the lensing one [src: arXiv:1808.03294,
  Sect. V.1].
- **Per-object magnitude bias from the CIB.** ⟨δm(z)⟩_g = −R_λ C
  ΔE(B−V)(z) b_g / b_r (Eq. 27), with C ≈ 2 for ~5′ maps such as SFD or
  Planck, and for SFD ≃ −0.024 R_λ b_g (z + 0.16)^−1.8 "in mmag" (Eq. 28);
  the correction is to subtract it [src: arXiv:1808.03294, Sect. V.3].
- **Target density.** +10 mmag in E(B−V) changes the DESI ELG target
  density by +11.0% and the LRG density by −1.4% [src: arXiv:2409.05140,
  Sect. 4.2].
- **Colours** [der]: from Eq. 4 of arXiv:2409.05140, a map error δE moves
  g − r by (R_g − R_r) δE and r − z by (R_r − R_z) δE, with the DECam
  coefficients of the Numbers table below, so the zero-point floor of the
  DESI map and the amplitude of the CSFD correction (both in that table)
  are colour errors of the same order; the effect on photo-z of a given
  colour error is not quantified in the papers read (see Not verified).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| SFD rescaling | E(B−V) = 0.86 E(B−V)_SFD | SDSS | arXiv:1012.4804 | Sect. I |
| Normalisation inside Eq. A1 | N = 0.78 | SDSS | arXiv:1012.4804 | App. A |
| R_b, R_V = 3.1 (per E(B−V)_SFD) | DES g, r, i, z, Y: 3.237, 2.176, 1.595, 1.217, 1.058 | SF11 Table 6 | arXiv:1012.4804 | Table 6 |
| R_b, R_V = 3.1 | LSST u, g, r, i, z, y: 4.145, 3.237, 2.273, 1.684, 1.323, 1.088 | SF11 Table 6 | arXiv:1012.4804 | Table 6 |
| R_b, DECam (DESI) | g 3.214, r 2.165, z 1.211 | DESI | arXiv:2409.05140 | Table 3 |
| R_b, BASS/MzLS | g 3.258, r 2.176, z 1.199 | DESI | arXiv:2409.05140 | Table 3 |
| R_g − R_r, R_r − R_z (DECam) | 1.049, 0.954 | DESI | arXiv:2409.05140 | Eqs. 5–6 |
| North–South reddening offsets | −9.5 mmag (g−r), −5.2 mmag (r−z) | DESI | arXiv:2409.05140 | Sect. 3.4 |
| DESI map zero-point floor | ~6 mmag in E(g−r), E(r−z), from 4.7, 3.7, 4.4 mmag grz zero points | DESI | arXiv:2409.05140 | Sect. 5.1 |
| Smallest statistical error per 13.7′ pixel | 1.9 mmag | DESI | arXiv:2409.05140 | Sect. 5.3 |
| SED dependence of stellar reddening | ~4% (g−r), ~1% (r−z) between 6500 and 5000 K | DESI | arXiv:2409.05140 | Sect. 5.4 |
| CSFD correction | 0.7 mmag per beam (σ), 3.5% at high latitude, error 0.2 mmag | CSFD | arXiv:2306.03926 | Sect. III.5 |
| CSFD per-beam S/N | 2.9 or 2.5 (two estimators) | CSFD | arXiv:2306.03926 | Sect. III.5 |
| E(B−V) to 100 μm | E(B−V) = 0.0184 I_100μm (temperature-corrected) | conversion adopted in CSFD | arXiv:2306.03926 | Sect. III.4 |
| Passband shift → photo-z | Δz = −0.0033 per nm (toy model, z = 0.15) | Euclid | arXiv:2310.14716 | Sect. 4.2.1 |
| Bandpass knowledge for < 2 mmag | ~0.2 nm | DES | arXiv:1601.00117 | Sect. IV.3 |
| PWV knowledge for < 1 mmag | ~10% | DES | arXiv:1601.00117 | Sect. IV.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Mixed normalisations.** Applying F99 coefficients from Table 6 to an
  E(B−V) already rescaled by 0.86 double-counts the recalibration: the
  table multiplies E(B−V)_SFD [src: arXiv:1012.4804, Table 6 note]. Check
  which E a catalogue's transmission column used (LS DR8: SFD with the
  catalogue coefficients, arXiv:2203.01949, Sect. 2.1.2).
- **Coefficients for the wrong filters or airmass.** North and South
  imaging need different R_b [src: arXiv:2409.05140, Sect. 3.1]; North−South
  g-band offsets reach +0.1 for the reddest sources from filter curves
  alone [src: arXiv:2203.01949, Sect. 2.1.3].
- **Over-correction correlated with structure.** SFD raises E(B−V)
  around every extragalactic sample tested, so dereddened densities carry
  the CIB pattern; test: stacks or Eq. 18 cross-correlations with
  references [src: arXiv:1808.03294, Sect. II.2; arXiv:2306.03926,
  Sect. IV.2].
- **Selection against dusty sky.** Around faint targets (LRG, ELG, QSO)
  CSFD shows negative ΔE(B−V) on sub-degree scales: they avoid high
  extinction because they sit at the imaging limit; in SFD the CIB term
  hides it. Re-threshold the sample with CSFD, or put the effect into the
  randoms [src: arXiv:2306.03926, Sect. V.1].
- **Inpainted pixels used as data.** Inpainted DESI values are less
  reliable than measured ones [src: arXiv:2409.05140, Sect. 3.4].
- **Star-calibrated chromatic corrections applied to galaxies** leave
  residuals with redshift structure at the 4000 Å break crossings [src:
  arXiv:1601.00117, Sect. V.2].
- **Central passbands for off-axis sources** bias photo-z positive [src:
  arXiv:2310.14716, Sect. 4.2.1].
- **Magnification and auto-correlations.** Unlike lensing, extinction
  over-correction has constant line-of-sight efficiency and also biases
  auto-correlations [src: arXiv:1808.03294, Sect. V.1].

## Reading list
<!-- key: reading-list -->

- Foundation: Schlafly & Finkbeiner 2011, arXiv:1012.4804, App. A — how
  R_b is computed (Eq. A1) and Table 6 for 88 passbands.
- Method: Zhou et al. 2024, arXiv:2409.05140 — a stellar reddening map end
  to end, its zero-point floor and the back-light test.
- Method: Chiang 2023, arXiv:2306.03926 — CSFD reconstruction, validation
  stacks, the selection-against-dust effect.
- Critique: Chiang & Ménard 2019, arXiv:1808.03294 — the cross-correlation
  test, count and magnification biases, Eq. 28 correction.
- Method: Li et al. 2016, arXiv:1601.00117 — synthetic chromatic errors
  for stars, supernovae and galaxies, and the auxiliary-measurement
  precision needed.
- Method: Euclid Collaboration: Paltani et al. 2024, arXiv:2310.14716 —
  passband-variation correction inside template fitting, colour-term
  comparison, App. B.1 on SED-dependent reddening.
- Forecast: Huterer et al. 2012, arXiv:1211.1015 — from calibration and
  dust-map errors to galaxy counts and cosmological biases.

## Not verified
<!-- key: not-verified -->

- The SFD paper itself (arXiv:astro-ph/9710327) was not re-read in its
  body: its temperature correction and its own coefficient table are
  known here only through the corrections Schlafly & Finkbeiner list.
- Galametz et al. 2017 (SED-dependent Galactic extinction in template
  fitting), Peek & Graves 2010, Betoule et al. 2013 and Fitzpatrick 1999
  were cited by papers read but not read themselves; no arXiv search
  located Galametz et al. 2017 this session.
- No paper read quantifies the shift of photo-z or of a tomographic n(z)
  mean per mmag of E(B−V) error; the propagation above stops at colours,
  counts and clustering. The joint estimation of dust and large-scale
  structure from one photometric survey (Bravo et al. 2021,
  arXiv:2106.08818) was seen by title and listing summary only.
- Planck-based and HI-based maps were not read at source; their
  comparison with SFD rests on the CSFD paper (Sect. V.3) and on
  `physics-and-methods.md#milky-way-extinction`.
