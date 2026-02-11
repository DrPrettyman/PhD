# PhD Research Repository

**Early Warning Signals for Critical Transitions**

This repository contains all materials from my PhD research on detecting early warning signals (EWS) that precede critical transitions in complex systems. The work spans theoretical analysis, numerical simulations, and applications to real-world climate and weather data.

PhD completed at the University of Reading, 2021, in collaboration with the National Physical Laboratory (NPL), London. Supervised by Dr. Tobias Kuna and Dr. Valerie Livina.

## Repository Structure

```
PhD/
├── MatlabCodePhD/       # MATLAB analysis code (git submodule)
├── PythonCode/          # Python EWS library, thesis figure reproduction, and docs
├── Thesis/              # PhD thesis (LaTeX source)
├── Papers/              # Published papers (manuscripts, reviews, proofs)
├── Literature/          # Reference papers and resources
├── Notes/               # Research notes and documentation
├── Presentations/       # Conference talks and posters
├── GraphicsProjects/    # Figure design files (Grace, Affinity, GIMP)
├── Assets/              # Shared images and resources
└── Admin/               # Administrative documents
```

> **Cloning:** The MATLAB code is a [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules). Clone with:
> ```bash
> git clone --recurse-submodules https://github.com/DrPrettyman/PhD.git
> ```
> Or, if already cloned: `git submodule update --init`

## Publications

**Prettyman, J.**, Kuna, T., & Livina, V. (2018). A novel scaling indicator of early warning signals helps anticipate tropical cyclones. *EPL (Europhysics Letters)*, 121(1), 10002.
[doi:10.1209/0295-5075/121/10002](https://doi.org/10.1209/0295-5075/121/10002)

**Prettyman, J.**, Kuna, T., & Livina, V. (2019). Generalized early warning signals in multivariate and gridded data with an application to tropical cyclones. *Chaos: An Interdisciplinary Journal of Nonlinear Science*, 29(7), 073105.
[doi:10.1063/1.5093495](https://doi.org/10.1063/1.5093495)

**Prettyman, J.**, Kuna, T., & Livina, V. (2022). Power spectrum scaling as a measure of critical slowing down and precursor to tipping points in dynamical systems. *Environmental Research Letters*, 17(3), 035004.
[doi:10.1088/1748-9326/ac526f](https://doi.org/10.1088/1748-9326/ac526f)

## Code

### MatlabCodePhD/ (submodule)

Primary analysis codebase containing:
- **Core_Functions/** -- Reusable EWS functions (ACF, DFA, PSE, EOF)
- **Projects/** -- Paper-specific analysis scripts
- **Data/** -- HadISD weather data, ice cores, processed datasets
- **Tests/** -- Unit tests for core functions

See [MatlabCodePhD/README.md](MatlabCodePhD/README.md) for detailed documentation.

### PythonCode/

Python implementation of the EWS analysis methods, including:
- **tippingpoints/** -- Core library (autocorrelation, DFA, power spectrum scaling, numerical integration, noise generation)
- **thesisfigures/** -- Code to reproduce thesis figures and tables
- **docs/** -- Sphinx documentation source

See [PythonCode/README.md](PythonCode/README.md) for usage details.

## Research Topics

### Critical Slowing Down

Systems approaching a tipping point recover more slowly from perturbations, manifesting as:
- Increased autocorrelation (ACF)
- Increased variance
- Spectral reddening (PSE)
- Changed scaling behavior (DFA)

### Methods Developed

1. **Sliding window indicators** -- Track EWS evolution over time
2. **Scaling exponents** -- DFA and spectral analysis for long-range correlations
3. **Multidimensional EWS** -- EOF-based methods for multivariate systems
4. **Alternative EOF** -- Projection maximizing autocorrelation rather than variance

### Applications

- **Dynamical systems** -- Hopf, homoclinic, pitchfork bifurcations
- **Climate** -- African Humid Period termination, Sahara greening
- **Weather** -- Hurricane intensification using HadISD pressure data

## Dependencies

### MATLAB
- R2016b or later
- Statistics and Machine Learning Toolbox
- Signal Processing Toolbox

### Python
- Python 3.9+
- NumPy
- Matplotlib

### LaTeX
- TeX Live or similar distribution
- BibTeX for bibliography

## Contact

Joshua Prettyman\
joshua@prettyman.me\
PhD in Applied Mathematics\
*Research on critical transitions and early warning signals*

---

*This repository represents completed PhD research. Code is provided for reference and reproducibility.*
