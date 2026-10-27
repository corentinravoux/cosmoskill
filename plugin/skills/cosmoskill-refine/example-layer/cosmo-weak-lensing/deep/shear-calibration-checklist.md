# Shear calibration checklist

Scope: the order in which this researcher checks a shear-calibration
section before trusting an S8; the package's `deep/shear-calibration.md`
describes the methods one by one but does not put them in one working order.
Snapshot: 2026-10-21.

## How it is done

The methods are in the package; this dossier points to them instead of
copying them, so that it stays right when the package is updated.

1. Shear measurement and its multiplicative bias m: the package's
   `systematics#shear-measurement-bias-noise-model-selection` and
   `deep/shear-calibration.md`.
2. Blending, which the image simulations must reproduce:
   `systematics#blending`.
3. PSF modelling and leakage: `systematics#psf-modelling-and-leakage`.
4. Redshift distributions, calibrated jointly with m where the analysis
   does so: `systematics#redshift-distributions`.

## Choices and what they cost

My own practice, not a statement about the field: I read the input
catalogue of the image simulations before their m values, because a
simulation that misses the blending of the data calibrates the wrong sample.

## Numbers

No number here: the values are in the package, each with its place read.

## What goes wrong

- A calibration quoted without the simulation it comes from.
- An m prior copied from one survey into another.

## Reading list

The papers are those of the package's `deep/shear-calibration.md`.

## Not verified

The working order and the two failure modes above are this researcher's
experience, not read in a paper.
