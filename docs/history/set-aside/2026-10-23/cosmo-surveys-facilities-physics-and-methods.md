# Set aside from skills/cosmo-surveys-facilities/references/physics-and-methods.md

Numbers run of 2026-10-24/25. Agent-computed etendue (AΩ), fibre-density and A × N_fibre values, removed from the skill under the owner's rule of 2026-10-23 (no number computed by an agent). Kept verbatim for the record.

## Sect. 1.1 Imaging (lines 25-54 before the run)

| Facility | Aperture used | Field | AΩ | Flag |
|---|---|---|---|---|
| Rubin (Simonyi) | 6.5 m effective (8.4 m primary) | 9.6 deg² | 319 m² deg² | inputs [src] arXiv:0805.2366; product [der], and stated as 319 m² deg² in its Table 1 [src: Table 1] |
| HSC on Subaru | 8.2 m | 1.5° diameter, 1.77 deg² as a full disc | 93 m² deg² | inputs [src: Table 1] arXiv:1704.05858; product [der]; the paper calls HSC's étendue "the largest of all existing wide-field optical imaging cameras" before LSST [src: Sect. 2] |
| ZTF (Palomar 48-inch) | 1.22 m | 47 deg² | 55 m² deg² | inputs [src] arXiv:1902.01932; product [der] |
| DECam on Blanco | 4 m | 2.2° diameter (3.8 deg² as a full disc [der]); "3 sq. deg." stated as the field of view [src: Sect. I] | 38 m² deg² with 3 deg² (48 with the full disc) | inputs [src] arXiv:1504.02900; product [der] |
| CSST | 2 m | about 1.1 deg² | 3.5 m² deg² | inputs [src] arXiv:2507.04618; product [der] |
| Roman WFI | 2.4 m | 0.281 deg² | 1.3 m² deg² | inputs [src] arXiv:1902.05569; product [der] |
| Euclid NISP | 1.20 m | 0.57 deg² | 0.64 m² deg² | inputs [src: Sect. 2] arXiv:2405.13493; product [der] |
| Euclid VIS | 1.20 m | 0.54 deg² | 0.61 m² deg² | aperture [src: Sect. 2] arXiv:2405.13493, field [src] arXiv:2405.13492; product [der] |

Assumption for every [der] product: unobstructed circular aperture of the
quoted diameter, A = π(D/2)². For Rubin the paper itself supplies the
effective diameter; with the full 8.4 m the product would be 532 m² deg²,
which is not the number to quote.

Three consequences that the table makes visible:

- Rubin's etendue is about six times that of ZTF and six to eight times
  that of DECam, depending on the DECam field adopted [der], which is
  why it can revisit 18,000 deg² about 800 times in ten years
  (arXiv:0805.2366) [src].
- ZTF matches DECam in etendue with a telescope of one tenth the area [der]:
  it buys cadence, not depth. Its design paper states "more than an order of
  magnitude improvement in survey speed" over its predecessor
  (arXiv:1902.01932) [src].
- Space imagers have etendues one to two orders of magnitude below the
  ground surveys [der]. They compete on resolution (0.18″ for VIS
  [src], 0.074″ pixels for CSST [src]), on infrared background, and on
  stability of the point-spread function, none of which enter AΩ.

## Sect. 1.2 Multi-object spectroscopy (lines 59-89 before the run)

For fibre spectrographs the analogue is collecting area times the number of
fibres, with the fibre density on the sky deciding how many passes a target
class needs.

| Facility | Aperture | Field | Fibres | Fibres per deg² | A × N_fibre [m²] | Flag for inputs |
|---|---|---|---|---|---|---|
| SDSS-V | 2.5 m | — | 500 per site | — | 2.5 × 10³ | [src: abstract] arXiv:2507.06989 |
| WEAVE | 4.2 m | 2° diameter, 3.1 deg² | 960 (MOS-A) | about 310 | 1.3 × 10⁴ | [src: Table 2] arXiv:2212.03981 |
| 4MOST | 4 m class | 4.2 deg² | 2436 | 580 | 3.1 × 10⁴ | [src] arXiv:1903.02464, arXiv:2606.27882 |
| MOONS | 8 m class | 25′ diameter, 0.14 deg² | about 1000 | about 7300 | 5.0 × 10⁴ | [src] arXiv:2009.00628, arXiv:2009.00635 |
| DESI | 4 m | 3.2° diameter, 8.0 deg² (requirement ≥ 7.65 deg²) | 5020 | 624 (requirement < 700) | 6.3 × 10⁴ | [src: abstract, Table 4] arXiv:2205.10939 |
| PFS | 8.2 m | 1.25 deg² | 2386 | 1909 | 1.3 × 10⁵ | [src: abstract, Sect. 2] arXiv:2606.14012 |
| Spec-S5 (**design**) | 6 m, two telescopes | — | 13,000 each | — | 3.7 × 10⁵ each | [sec: GC] arXiv:2608.07927 |
| MUST (**design**) | 6.5 m | about 5 deg² | more than 20,000 | 4000 | 6.6 × 10⁵ | [src] arXiv:2605.10102 |
| MSE (**design**, 2025) | 11.5 m | 1.5 deg² | more than 18,000 | 12,000 | 1.9 × 10⁶ | [src] arXiv:2503.15553 |
| WST (**design**) | 12 m class | 3 deg² | 20,000 | 6700 | 2.3 × 10⁶ | [src] arXiv:2403.05398, arXiv:2607.01150 |

The last two columns are [der] with the same unobstructed-aperture
assumption. They ignore throughput, fibre diameter, wavelength coverage,
spectral resolution, reconfiguration time and the fraction of time awarded
to cosmology, so they rank hardware, not surveys. What they show:

- A "Stage-V" facility in the sense used by the MUST and WST papers is one
  to two orders of magnitude above DESI in A × N_fibre [der].
- DESI's fibre density, 624 per deg² [der], equals the density of its LRG
  targets alone (624 per deg², arXiv:2404.03002) [sec: GC]. With BGS Bright
  at 854 per deg² and QSO at 310 per deg² [sec: GC], every tile is
  over-subscribed and completeness is built up by overlapping passes
  (Sect. 5).
- PFS and MOONS trade field for aperture: high fibre density on small
  fields suits deep, dense samples, not 14,000 deg² footprints.
