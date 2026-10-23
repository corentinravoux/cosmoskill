# Learned simulation corrections — cosmo-machine-learning dossier

Scope: how a network that corrects or replaces a gravity or hydrodynamics solver at the field level
is built and validated (what it predicts, from which cheap input, with which loss, network,
training simulations and crop-and-pad scheme, against which statistics), and how to choose between
correcting a fast solver and learning from linear theory, between one-shot maps and integrated
dynamics, between deterministic and stochastic super-resolution, and between learned force kernels,
U-Nets and halo-level painting.
Snapshot: 2026-10-18.
From: Huertas-Company & Lanusse 2022 review (arXiv:2210.01813), Sect. 6.1; Dvorkin et al. 2022
Snowmass white paper (arXiv:2203.08056), Sect. 4.

Already in L2, not repeated here: the table of approaches with their headline accuracies and the
"residual on a physical approximation" pattern
(`physics-and-methods.md#learned-corrections-of-fast-simulations`); the COLA, FastPM and LPT codes
being corrected and their own accuracy (`cosmo-simulations-mocks`, with its `deep/fast-mocks.md`);
stochastic generative models of fields (`deep/generative-models.md` of this skill); emulators of
summary statistics (`deep/emulators.md`). How baryonic corrections enter a lensing analysis is in
`cosmo-weak-lensing`.

Symbols. q: Lagrangian (initial grid) position; x = q + Ψ(q): final position; Ψ: displacement;
Ψ_ZA: Zel'dovich (linear) displacement; v, p: velocity and momentum; δ: overdensity; n(x): particle
count in voxel x; T(k) = √(P_pred/P_true): transfer function; r(k) = P_pred×true/√(P_pred P_true):
cross-correlation coefficient (arXiv:2111.02441, Eq. 3); LR/HR/SR: low, high and super resolution.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the cheap input and what the network adds
<!-- key: step-1-choose-the-cheap-input-and-what-the -->

| Approach | Input → target | What the network learns | Place read |
|---|---|---|---|
| D³M | ZA displacements → FastPM displacements, 32³ grids | the full non-linear displacement | arXiv:1811.06533, Sects. Setup, Dataset |
| Styled U-Net (Jamieson et al.) | ZA displacement and velocity at z = 0, plus Ω_m → Quijote N-body displacement and velocity | the residual N-body − ZA (input added to output) | arXiv:2206.04594, Setup, Physical Considerations |
| NECOLA, MG-NECOLA | COLA (MG-PICOLA) displacement → Quijote (Quijote-MG) displacement, same seed and particle number | the residual x_f,Nbody − x_f,COLA | arXiv:2111.02441, Sect. II.2.1; arXiv:2604.19613, Eqs. 5–6 |
| Hybrid physical–neural ODE | particle-mesh forces → CAMELS N-body trajectories | an isotropic Fourier filter on the PM potential | arXiv:2207.05509, Eqs. 2–3 |
| LNCA | ZA initial field at a = 1/128 → Quijote at z = 3, 2, 1, 0.5, 0 | residual accelerations integrated in time, with latent fields | arXiv:2607.27320, Eqs. 1–3, 7 |
| Super-resolution GAN | 64³ LR displacement → 512³ HR displacement, same seed | small-scale displacements, with injected noise | arXiv:2010.06608, Physical considerations |
| LDL | FastPM dark matter → TNG300-1 stellar mass, n_e, T maps | displacement layers S = α∇Ô_G (1 + δ)^γ (Eqs. 1–3) with a few parameters | arXiv:2010.02926, Sect. LDL |
| BIND | projected dark-matter-only halo patch + 35 parameters → projected dark matter, gas, stars | a conditional flow-matching map, per halo of M_200c ≥ 10¹³ M_⊙/h | arXiv:2609.10709, Sect. III.1 |

The reason given for residual learning is the same in all of them: large scales, where perturbation
theory or the fast solver is right, are kept by construction; a CNN has a finite receptive field
and should only add "small-scale textures"; and the large-scale cosmology dependence is already in
the input, so the network only models its small-scale modulation [src: arXiv:2206.04594, Physical
Considerations]. Working with displacements rather than positions keeps translational equivariance
[src: arXiv:2111.02441, Sect. II.2.1].

### Step 2. Choose and prepare the training simulations
<!-- key: step-2-choose-and-prepare-the-training -->

| Model | Training set | Split | Place read |
|---|---|---|---|
| D³M | 10 000 ZA/FastPM pairs, effective volume 20 (Gpc/h)³; trained at one cosmology | 80/10/10 | arXiv:1811.06533, Dataset |
| Styled U-Net | 2000 Quijote Latin-hypercube runs (5 parameters, distinct seeds), 512³ in 1 Gpc/h | 1757/122/121 | arXiv:2206.04594, Setup |
| NECOLA | 100 Quijote fiducial runs with matched COLA runs (30 log-spaced steps from z = 9) | 70/20/10 | arXiv:2111.02441, Sects. II.1.2, II.2.2 |
| MG-NECOLA | 25 runs from each of four f(R) labels, 100 in all | 70/20/10 | arXiv:2604.19613, Sect. III.3 |
| Hybrid ODE | CAMELS dark-matter-only runs, 25 h⁻¹Mpc, downsampled from 256³ to 64³; trained at Ω_m = 0.3 | — | arXiv:2207.05509, Sect. 4 |
| LNCA | Quijote Latin hypercube, five snapshots | — | arXiv:2607.27320, Training Data |
| SR GAN | 16 LR/HR pairs of (100 h⁻¹Mpc)³ at one cosmology; 1 pair for testing | 16/1 | arXiv:2010.06608, Dataset, Training |
| LDL | one TNG300-1 box, split spatially ("global cut") into 77.7/13.8/8.5% of a 625³ mesh | sub-boxes | arXiv:2010.02926, Model Training |
| BIND | CAMELS SB35, 1024 paired 50 h⁻¹Mpc runs; haloes at 8 redshifts, 10 random rotations each | — | arXiv:2609.10709, Sect. III.1 |

**Crop, pad, augment.** A 3 × 512³ field does not fit a GPU, so it is cut into 128³ crops (250
h⁻¹Mpc), convolutions are unpadded to keep translational equivariance, and each crop is
periodically padded (20 voxels for NECOLA and MG-NECOLA, 48 for the styled U-Net) so the output
regains the crop size [src: arXiv:2111.02441, Sect. II.2.2; arXiv:2206.04594, Network and
Training]. Rotations and reflections of the cube are applied as augmentation; under periodic
boundaries SO(3) reduces to the 48-element octahedral group [src: arXiv:2010.06608, Physical
considerations]. The LNCA trains on non-periodic 200 Mpc/h crops, evolves a padded 96³ volume and
discards a margin of N_steps voxels per face before the loss, because errors from the finite
stencils propagate inward by one cell per step [src: arXiv:2607.27320, Training Data]. The styled
U-Net's 12 TB of training data required a dedicated loader (map2map) so that GPUs were not starved
by I/O [src: arXiv:2206.04594, Network and Training].

### Step 3. Write the loss
<!-- key: step-3-write-the-loss -->

| Model | Loss | Stated reason | Place read |
|---|---|---|---|
| D³M | MSE on Ψ (Eq. 9) | by Parseval it penalises both 1 − T and 1 − r (Eq. 10) | arXiv:1811.06533, Loss Function |
| NECOLA | L = ln(L_δ L_Ψ^λ), λ = 1; L_δ on n(x), L_Ψ on Ψ | accuracy in both Eulerian and Lagrangian space; the log product balances terms of different magnitude | arXiv:2111.02441, Sect. II.2.2 |
| Styled U-Net | log L_δ + 3 log L_Ψ; velocity: log L_v(q) + log L_v(x) + log L_v²(x) (Eq. 13) | λ = 3 trains faster; the v² (dispersion) term is "crucial" for redshift-space fingers of God | arXiv:2206.04594, Network and Training |
| MG-NECOLA | w_lag L_lag + w_eul L_eul + w_grad L_grad with (1, 3, 2) (Eq. 7), plus ⟨w(k)[log P_pred − log P_targ]²⟩ with w = (k/k_Ny)² Θ(k − 0.3 h Mpc⁻¹) (Eqs. 8–9) | the gradient term recovers small scales; the spectral term targets the scales COLA gets wrong | arXiv:2604.19613, Sect. III.3.1 |
| Hybrid ODE | Σ_s ‖x_s − x_s^Nbody‖² + λ‖P_s/P_s^Nbody − 1‖², λ = 0.1 (Eq. 4) | positions alone gave less small-scale power for this low-capacity model; P alone does not fix positions | arXiv:2207.05509, Sect. 3 |
| LNCA | displacement, momentum, density and halo-moment terms, each divided by the Zel'dovich value (Eqs. 8–11) | L = 1 means parity with ZA; the halo term rewards collapse without matching particle by particle | arXiv:2607.27320, Multi-Objective Loss |
| SR GAN | 5 epochs of L2 (Eq. 2), then WGAN-gp (Eq. 3) with LR and density fields given to the critic | L2 alone blurs scales below the input resolution; density channels "crucial" for sharp maps and small-scale P(k) | arXiv:2010.06608, Network architecture, Training |
| LDL | L2 of Ô_s F with Ô_s = 1 + (k/1 h Mpc⁻¹)^{−n}, n = 1 (0.85 for X-ray n_e) (Eqs. 8–9); n_e·T products for tSZ (Eqs. 10–11) | without Ô_s the many small-scale modes bias the large-scale power | arXiv:2010.02926, Model Training |

### Step 4. Build the network
<!-- key: step-4-build-the-network -->

- **V-Net/U-Net for displacements.** NECOLA: two down- and two up-sampling stages, blocks of two 3³
  convolutions with 1³ residual shortcuts, batch normalisation, leaky ReLU (slope 0.01), 64
  channels, input added to output [src: arXiv:2111.02441, Sect. II.2.2]. The styled U-Net has four
  resolution levels and modulates every convolution kernel by an affine transform of Ω_m, as in
  StyleGAN2; h enters through h-units, so Ω_m is the only style parameter at z = 0 [src:
  arXiv:2206.04594, Network and Training].
- **A learned force filter.** The hybrid ODE adds (1 + f_θ(a, k)) to the PM potential, with f_θ a
  cubic B-spline over 16 knots whose coefficients a network outputs; isotropy preserves
  translations and rotations; training differentiates through the ODE solver with the adjoint
  method [src: arXiv:2207.05509, Sect. 3].
- **A local recurrent rule.** The LNCA keeps a fixed Lagrangian grid topology, so 3D convolutions
  replace graph operations, carries latent scalars and vectors per node, and is equivariant; about
  4 × 10³ parameters against ~3 × 10⁶ for the styled U-Net [src: arXiv:2607.27320, Comparison to
  Existing Emulators].
- **Noise injection for super-resolution.** White noise with learned amplitude is added after every
  convolution of a StyleGAN2-like generator, because HR small scales are not determined by the LR
  input [src: arXiv:2010.06608, Physical considerations].

### Step 5. Train
<!-- key: step-5-train -->

| Model | Optimiser and schedule | Hardware or cost | Place read |
|---|---|---|---|
| NECOLA | Adam 10⁻⁴, halved after 3 epochs without gain; 100 epochs | inference ~125 GPU s per 512³ box | arXiv:2111.02441, Sects. II.2.2, III.3 |
| MG-NECOLA | Adam 10⁻⁴, halved after 3 stagnant epochs; 100 epochs | inference ~180 s per realisation on one GPU | arXiv:2604.19613, Sects. III.3, IV.4.1 |
| Styled U-Net | Adam 4 × 10⁻⁴, ÷10 after 3 stagnant epochs; batch 16 | 16 V100 GPUs | arXiv:2206.04594, Network and Training |
| SR GAN | Adam 10⁻⁵ (β1 = 0, β2 = 0.99); 5 supervised + 150 adversarial epochs; gradient penalty every 16 batches | 5120³ SR field for 1 h⁻¹Gpc in 16 GPU hours | arXiv:2010.06608, Training, Discussion |
| Hybrid ODE | Adam 10⁻²; JAX Dormand–Prince solver | one GPU, 64³ particles | arXiv:2207.05509, Sects. 3–4 |
| BIND | AdamW, up to 200 epochs, batch 64 per GPU on 8 H100, bfloat16, EMA weights | ~150 GPU hours; a 50 h⁻¹Mpc box with ~45 haloes in ~40 s | arXiv:2609.10709, Sect. III.4 |

### Step 6. Validate on statistics, then outside the training cosmology
<!-- key: step-6-validate-on-statistics-then-outside-the -->

The tests read in the bodies, in the order they are usually run:

1. **Particle-level residuals.** D³M: mean relative displacement error 2.8% against 9.3% for 2LPT
   [src: arXiv:1811.06533, Point-Wise Comparison]. MG-NECOLA: mean |d_pred − d_truth| falls from
   ≈ 0.68 to ≈ 0.47 h⁻¹Mpc, about 30% (Eq. 14) [src: arXiv:2604.19613, Sect. IV.3].
2. **T(k) and r(k).** NECOLA: r within 1% to k = 1 h Mpc⁻¹ [src: arXiv:2111.02441, Sect. III.1.3].
   A matched P(k) is not enough: the hybrid ODE and PGD recover similar small-scale power at the
   fiducial cosmology but very different r(k) [src: arXiv:2207.05509, Sect. 5].
3. **Bispectrum, haloes, profiles, RSD.** The styled U-Net's low-mass haloes (M < 5 × 10¹³ M_⊙/h)
   are 10–20% too abundant; profiles of 500 haloes of ~5 × 10¹⁴ M_⊙/h beat COLA [src:
   arXiv:2206.04594, Halos]. [src: Sect. "Halos"]
4. **Outside the training cosmology.** NECOLA, trained at one cosmology, is tested on 100
   Latin-hypercube runs (five parameters varied), on M_ν = 0.1, 0.2, 0.4 eV and on w = −0.95,
   −1.05 runs, below ~1% to k = 1 h Mpc⁻¹ [src: arXiv:2111.02441, Sect. III.2]. MG-NECOLA is
   checked against the fRemu emulator for |f_R0| from 10⁻⁷ to 10⁻⁴ and across 98 hypercube
   cosmologies, restricted to k > 0.1 h Mpc⁻¹ because a single realisation is compared with a
   smooth mean [src: arXiv:2604.19613, Sects. IV.5.1–IV.5.2].
5. **Outside the training resolution and volume.** The hybrid ODE is tested at Ω_m = 0.1, at 128³
   particles in the same box, and at 128³ in a 200 h⁻¹Mpc box against HaloFit [src:
   arXiv:2207.05509, Sect. 5]. The SR GAN is run on a 1000 times larger volume and checked on P(k)
   and the halo mass function [src: arXiv:2010.06608, Discussion].
6. **Against the ceiling of the method.** BIND compares its pasted map with a "hydro-replace"
   control that pastes the true hydrodynamical haloes through the same machinery, which isolates
   the pasting from the emulator [src: arXiv:2609.10709, Sect. VII.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Correct a fast solver, or learn from linear theory
<!-- key: correct-a-fast-solver-or-learn-from-linear -->

- **Extrapolation in cosmology.** The COLA-trained NECOLA shows much weaker extrapolation features
  across the Latin hypercube than the same network trained on Zel'dovich input [src:
  arXiv:2111.02441, Sect. III.2]. The cost is the COLA run itself: ~10⁴ CPU s against ~125 GPU s for
  the network, so COLA dominates and the speed-up over N-body is about 100 [src: Sect. III.3]. For
  MG-NECOLA the total is ~1.2 × 10³ s against ~1.8 × 10⁶ s for Quijote-MG, about 1500 [src:
  arXiv:2604.19613, Table 1].
- **Learning from ZA across cosmologies.** The styled U-Net instead trains on 2000 cosmologies with
  Ω_m as a style; a fiducial-only network (FNN) loses accuracy in halo interiors even for small
  Ω_m changes [src: arXiv:2206.04594, Halos]. Early-universe extensions (primordial non-Gaussianity)
  transfer without retraining because they enter only through the linear input [src:
  arXiv:2206.04594, Conclusion].
- **Trained at one cosmology, tested at others.** D³M at Ω_m = 0.5 and 0.1 keeps 3.8% and 2.5%
  displacement errors (2LPT: 15.2% and 4.3%), and at A_s = 1.8 A_0 and 0.2 A_0 stays below 4%;
  at small A_s, 2LPT is better on the largest scales [src: arXiv:1811.06533, Generalizing].

### One-shot map or integrated dynamics
<!-- key: one-shot-map-or-integrated-dynamics -->

The LNCA reaches |ΔT/T| < 0.01 and 1 − r < 0.01 to k ~ 0.5 h Mpc⁻¹, against ~1 h Mpc⁻¹ for the
styled U-Net, with comparable halo recovery and degradation only at the hypercube corners, using
about four orders of magnitude fewer parameters [src: arXiv:2607.27320, Comparison to Existing
Emulators]. Integration gives positions and velocities at every step, so light-cones need no
extra passes, and a local rule scales with surface communication; it claims no wall-clock gain
over FastPM or pmwd (~10–20 s for 512³ on one A100) [src: same]. Its cost: the finite Lagrangian
receptive field caps the recoverable inner halo structure, and backpropagation through time limits
the number of substeps [src: Limitations].

### Learned force kernel or free-form network
<!-- key: learned-force-kernel-or-free-form-network -->

A B-spline force filter is robust to changes of Ω_m (0.1 against 0.3), particle number and box size
where PGD, with three fitted parameters, stops correcting; it overshoots small-scale power near
k ~ 7 h Mpc⁻¹ at higher resolution and gains little in r(k) there [src: arXiv:2207.05509, Sects. 5,
6]. LDL needs "a handful of parameters only" and is "stable and easy to train", but loses small scales
below its 0.328 h⁻¹Mpc mesh [src: arXiv:2010.02926, Discussion].

### Deterministic or stochastic super-resolution
<!-- key: deterministic-or-stochastic-super-resolution -->

L2 or perceptual losses give one blurred output; HR small scales are a one-to-many function of the
LR input, so the SR model injects noise and trains adversarially, which yields several small-scale
realisations for one large-scale field [src: arXiv:2010.06608, A Survey of Models, Discussion].

### Composite losses
<!-- key: composite-losses -->

On MG-NECOLA's test realisation, the NECOLA log-product loss with λ = 1, 2, 3 gives errors up to
2.5% larger than the gradient-plus-spectral loss at k > 0.5 h Mpc⁻¹ [src: arXiv:2604.19613,
Sect. IV.2, Fig. 2]. This is one realisation, and the comparison does not separate the gradient
from the spectral term [der].

### Halo painting or full-field painting
<!-- key: halo-painting-or-full-field-painting -->

BIND paints only haloes above 10¹³ M_⊙/h on 2D projections: integrated dark matter and total mass
within 1%, gas ~1%, stars ~10%, profiles ≲ 10% to 3.125 h⁻¹Mpc [src: arXiv:2609.10709, Table 3].
Even perfect haloes recover only ~65% (CV) of the true suppression 1 − S(k) at k = 10–20 h Mpc⁻¹,
because lower-mass haloes and baryons beyond several R_200c matter [src: Sect. VII.1]. LDL paints
the full field but with the resolution limit above.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Model | Source | Place read |
|---|---|---|---|---|
| Training runs | 70 of 100 matched Quijote/COLA pairs | NECOLA | arXiv:2111.02441 | Sect. II.2.2 |
| COLA setting | 30 log-spaced steps from z = 9, ~3 CPU h | NECOLA | arXiv:2111.02441 | Sect. II.1.2 |
| Cost per box | N-body 10⁶ CPU s, COLA 10⁴ CPU s, network 125 GPU s | NECOLA | arXiv:2111.02441 | Table 1 |
| Crop and pad | 128³ crops, 20-voxel periodic pad | NECOLA, MG-NECOLA | arXiv:2111.02441; arXiv:2604.19613 | Sects. II.2.2; III.3 |
| Training split | 1757/122/121 Latin-hypercube cosmologies | styled U-Net | arXiv:2206.04594 | Setup |
| Low-mass halo bias | +10–20% below 5 × 10¹³ M_⊙/h | styled U-Net | arXiv:2206.04594 | Halos |
| Loss weights | (w_lag, w_eul, w_grad) = (1, 3, 2); spectral k_min = 0.3 h Mpc⁻¹ | MG-NECOLA | arXiv:2604.19613 | Eqs. 7–9 |
| Position error | 0.68 → 0.47 h⁻¹Mpc | MG-NECOLA | arXiv:2604.19613 | Sect. IV.3 |
| Neutrino transfer | < 1% (0.1 eV), < 2% (0.2 eV), < 4% (0.4 eV) | MG-NECOLA | arXiv:2604.19613 | Fig. 8 |
| D³M training set | 10 000 ZA/FastPM pairs, 20 (Gpc/h)³ | D³M | arXiv:1811.06533 | Dataset |
| Hybrid ODE loss weight | λ = 0.1; 16 B-spline knots | hybrid ODE | arXiv:2207.05509 | Sect. 3 |
| LNCA accuracy reach | 1% in T and r to k ~ 0.5 h Mpc⁻¹; ~4 × 10³ parameters | LNCA | arXiv:2607.27320 | Comparison |
| SR training | 16 pairs, 64³ → 512³ in 100 h⁻¹Mpc; mass resolution × 512 | SR GAN | arXiv:2010.06608 | Dataset |
| SR cost | HR 560 core h vs LR 0.6 core h to z = 2 | SR GAN | arXiv:2010.06608 | Discussion |
| LDL smoothing | Ô_s = 1 + (k/1 h Mpc⁻¹)^{−1} | LDL | arXiv:2010.02926 | Eq. 9 |
| BIND ceiling | hydro-replace recovers ~65% of 1 − S(k) at k = 10–20 h Mpc⁻¹ | BIND | arXiv:2609.10709 | Sect. VII.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Good power, wrong phases.** A correction can restore P(k) while leaving r(k) low (PGD in
  arXiv:2207.05509, Sect. 5). Test: report T(k) and r(k) together, and particle residuals.
- **Not enough room for small-scale information.** LDL and the hybrid ODE stay below the HR
  simulation at small scales because the input mesh lacks that information [src: arXiv:2010.02926,
  Discussion; arXiv:2207.05509, Sect. 6]. Test: compare with a same-resolution full simulation
  (TNG300-3 for LDL), not only with the HR target.
- **Halo abundances.** U-Net emulators over-produce low-mass haloes (+10–20%) while P(k) is at the
  per-cent level [src: arXiv:2206.04594, Halos]. Test: halo mass function and profiles with the
  same halo finder on both outputs.
- **Untested resolution or volume.** The styled U-Net and LNCA are trained only on 512³ in 1 Gpc/h,
  so transfer to other force resolutions is untested [src: arXiv:2607.27320, Limitations]; BIND
  works at one map resolution only [src: arXiv:2609.10709, Sect. VIII]; the hybrid ODE overshoots
  near k ~ 7 h Mpc⁻¹ at higher resolution [src: arXiv:2207.05509, Sect. 5].
- **One sub-grid model.** BIND learns IllustrisTNG only; applying it to SIMBA- or EAGLE-like feedback
  needs retraining or a cross-code test [src: arXiv:2609.10709, Sect. VIII]. See
  `systematics.md#simulator-dependence` for the measured cost of such transfers.
- **Rare objects absent from training.** Sixteen 100 h⁻¹Mpc pairs hold few massive clusters; the SR
  authors propose separate-universe or constrained runs to enrich them [src: arXiv:2010.06608,
  Discussion]. [src: Sect. "Keywords:"]
- **Projection effects.** BIND's 50 h⁻¹Mpc projections include foreground and background matter and
  sometimes several haloes [src: arXiv:2609.10709, Sect. III.1]. Test: retrain on halo-centred
  6.25 h⁻¹Mpc cubes, as in its App. C.
- **Comparing a realisation with a mean.** At k < 0.1 h Mpc⁻¹ a single realisation differs from a
  mean emulator by cosmic variance; MG-NECOLA restricts that comparison to k > 0.1 h Mpc⁻¹ [src:
  arXiv:2604.19613, Sect. IV.5.1].
- **Velocities.** Displacement-only training does not fix redshift-space structure; the styled U-Net
  needed a velocity-dispersion loss for fingers of God [src: arXiv:2206.04594, Network and
  Training]. Test: redshift-space multipoles and stacked profiles.
- **Baryons absent.** Gravity-only emulators omit baryons, which limits comparison with data [src:
  arXiv:2607.27320, Limitations].

## Reading list
<!-- key: reading-list -->

- Foundation: He et al. 2019, arXiv:1811.06533 — first U-Net from ZA to non-linear displacements;
  why an MSE on Ψ controls T and r.
- Method: Jamieson et al. 2023, arXiv:2206.04594 — residual learning, style parameters, crop and
  pad, velocity-dispersion loss.
- Method: Kaushal et al. 2022, arXiv:2111.02441 — correcting COLA; extrapolation across cosmology
  and to neutrinos from one training cosmology.
- Method: Lanzieri et al. 2022, arXiv:2207.05509 — learned force filter inside a PM ODE; P(k)
  against r(k).
- Method: Li et al. 2021, arXiv:2010.06608 — stochastic super-resolution with a conditional WGAN.
- Method: Dai et al. 2021, arXiv:2010.02926 — few-parameter Lagrangian layers for baryon maps;
  scale-weighted loss.
- Application: Orjuela-Quintana et al. 2026, arXiv:2604.19613 — f(R) extension; composite loss
  ablation; tests against a power-spectrum emulator.
- Application: Lee et al. 2026, arXiv:2609.10709 — halo-level baryon inpainting and the ceiling set
  by pasting.
- Critique and alternative: Jacobus et al. 2026, arXiv:2607.27320 — integrated local dynamics, a
  head-to-head with the styled U-Net, and the limits shared by all such emulators.

## Not verified
<!-- key: not-verified -->

- The Alves de Oliveira et al. NN(ZA) benchmark that NECOLA compares with: cited inside
  arXiv:2111.02441, not read; no identifier recorded.
- The Quijote-PNG transfer test of the styled U-Net beyond what L2 records.
- BIND architecture and optimisation appendices (A, B), and the halo-centred projection test
  (App. C).
- The LNCA training curriculum (App. V.1) and its evolutionary optimiser.
- Whether any survey analysis has used a learned correction of a fast solver for its covariance or
  inference.
