# Set aside from skills/cosmo-lyman-alpha/references/results.md (numbers run 2026-10-23)

Agent-computed values removed under the rule of 2026-10-23 (no number computed by an agent). Verbatim, with the line number they had.

Line 131:

Conversions for the DR1 row, derived here with c = 299 792.458 km/s and the paper's 147.09 Mpc normalisation: D_H/r_d = c/(239.2 × 147.09) = 8.52, with the stated 2% giving ±0.17; D_M/r_d = 5840/147.09 = 39.70, with the stated 2.4% giving ±0.95 [der].

Line 172:

The upper limit in numbers, derived here from that formula with c = 299 792.458 km/s and λ_α = 1215.67 Å: R_z = 197.3/(1+z) km/s, so k_max = 0.5π/R_z = 0.0255 s/km at z = 2.2, 0.0318 at z = 3.0 and 0.0414 at z = 4.2 [der].

Line 183:

The two k_max conventions agree: 2.0 Å⁻¹ is 0.0260 s/km at z = 2.2 and 0.0422 s/km at z = 4.2 [der: 2.0 × 1215.67 × (1+z)/299 792.458], against 0.0255 and 0.0414 s/km for 0.5π/R_z, which is 0.5π/0.8 Å = 1.96 Å⁻¹ [der]. The difference between the upper redshift of the QMLE measurement paper (bins to 4.4 [der]) and the 4.2 quoted by the cosmology paper was not resolved here.

Fragments removed from other statements (verbatim):

- `Both DESI DR2 errors are about half the eBOSS DR16 ones [der: 0.098/0.19, 0.52/1.1].`
- `(1.6% [der: 0.071/4.525])`
- `The eBOSS value was low at about 1.7σ from the DR1 value [der: (68.3 − 63.2)/sqrt(2.5² + 1.6²) = 1.7, treating them as independent; this is an upper bound on the significance if the two surveys share sky area and quasars].`
- `(10 bins [der])`
- `: band edges to 0.010 s/km, then to 0.045 s/km [der, below]`
- `, so z = 2.2–4.4 [der]`
- `: band edges to 0.030 s/km, then to 0.053 s/km [der, below]`
- `≈ 0.026–0.041 s/km [der, below]`
- `, so bins z = 2.2–4.2 [der]`
- `(11 bins [der])`
- `Band edges: 20 × 0.0005 = 0.010 s/km, then 0.010 × 10^(13 × 0.05) = 0.045 s/km [der, assuming the linear bins start at k = 0 and a base-10 logarithm; the paper states the binning, not the end points].`
- `Band edges: 60 × 0.0005 = 0.030 s/km, then 0.030 × 10^(25 × 0.01) = 0.053 s/km [der, same assumptions].`
- `The DESI DR1 amplitude carries an 8.4% error and the slope 0.8% [der: 0.032/0.379, 0.019/2.309].`
- `- D_M/r_d moved up from 35.7–37.5 (SDSS, 2017–2020) to 38.99 (DESI DR2). D_H/r_d moved down from about 9.0 to 8.63.`

# Set aside from other files of cosmo-lyman-alpha (same run), verbatim fragments

- surveys-and-data.md:142 cell `3.1% on D_H/r_d [der: 0.28/9.18]`
- surveys-and-data.md:143 cell `2.5% combined [der: 0.22/8.94]`
- surveys-and-data.md:144 cell `2.1% [der: 0.19/8.99]`
- surveys-and-data.md:49 `the DR1 forest sample is about twice the eBOSS DR16 one [der: 420,000 / 210,005 = 2.0] and`
- systematics.md:118 `i.e. about 0.026–0.041 s/km over z = 2.2–4.2 [der, see `results.md` §3]`
- open-questions.md:154 `gives −0.127 at z = 2.33 [der: (3.33/4)^2.96 = 0.581], against −0.135 to −0.149 from the 3D fits above`
- open-questions.md:155 `fiducial 4.548 [der: 39.1879/8.6172]`
- theory-sbi-field-level.md:379 `The DESI DR1 P1D upper limit, 0.0318 s/km at z = 3 (...), is about 3.6 h/Mpc [der: k[h/Mpc] = k[s/km] × H(z)/((1+z) h), with H(3)/(4h) ≈ 113 km/s per h⁻¹Mpc for flat Ω_m = 0.31]`
- tomography-voids.md:122 `i.e. σ_∥ ≈ 2.1 [der]`
- p1d-emulators.md:41 `i.e. 60 LF and 3 HF runs [der]; the 48 LF of ... plus the 12 LF added here`
- continuum-distortion.md:81 `150 × 0.8 Å = 120 Å [der]`; continuum-distortion.md:264 `(= 120 Å [der])`
