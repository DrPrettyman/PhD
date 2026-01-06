# Generalised Early Warning Signals in Multivariate and Gridded Data with an Application to Tropical Cyclones

**Authors:** J. Prettyman, T. Kuna, V. Livina

**Published in:** Chaos (AIP Publishing)

## Code

The MATLAB code for reproducing the figures and analysis is available at:
[MatlabCodePhD/Projects/Paper2_Chaos](https://github.com/DrPrettyman/MatlabCodePhD/tree/main/Projects/Paper2_Chaos)

## Abstract

Methods for detecting early warning signals (EWS) of tipping events in multi-dimensional systems are reviewed and expanded. This paper provides an analytical justification of the use of dimension-reduction by empirical orthogonal functions (EOF) in the context of early warning signals, and extends one-dimensional techniques to spatially separated time series over a 2D field. The challenge of predicting an approaching tropical cyclone by a tipping-point analysis of sea-level pressure is used as the primary example, and an analytical model of a moving cyclone is developed to test predictions.

## Key Contributions

- **Analytical justification for EOF in EWS**: Demonstrates that EOF dimension-reduction preserves early warning signal properties for systems approaching bifurcation
- **Multivariate EWS methods**: Reviews and applies the Williamson method for approximating Jacobian eigenvalues from 2D time series
- **Spatial EWS analysis**: Extends 1D indicators to gridded data over geographic areas
- **Moving cyclone model**: Novel stochastic model of a moving cyclone for testing EWS methods

## Methods

1. **Empirical Orthogonal Functions (EOF)**: Dimension reduction preserving variance, with analytical proof that the first loading vector captures the bifurcating component
2. **Jacobian eigenvalue approximation**: 2D analogue of ACF1 indicator following Williamson et al.
3. **Power Spectrum (PS) indicator**: Applied over 2D spatial fields using Mann-Kendall coefficient to assess slope

## Data

- Sea-level pressure (SLP) and wind speed (WS) from HadISD 2017 dataset
- 14 tropical cyclones (same as Paper 1)
- 9 Atlantic hurricanes for spatial analysis (Andrew, Katrina, Wilma, Gustav, Matthew, Harvey, Irma, Nate)

## Key Findings

- EOF successfully combines SLP and WS variables, giving indicator performance between the two separate variables
- Jacobian eigenvalue method shows real part increasing before cyclone events (similar to Hopf bifurcation approach)
- PS indicator applied spatially shows gradient patterns consistent with cyclone approach direction
- The moving cyclone model reproduces observed indicator behaviour

## Files

- `msPrettyman_final.tex` - Main manuscript LaTeX source
- `SuppelmentaryMaterial.tex` - Supplementary material (sensitivity analysis)
- `msPrettyman_finalNotes.bib` - References
- `figures/` - Figures (01-08 as EPS files)
- `revtex4-1.cls` - RevTeX journal class file
