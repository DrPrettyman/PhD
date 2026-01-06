# PhD Research Repository

**Early Warning Signals for Critical Transitions**

This repository contains all materials from my PhD research on detecting early warning signals (EWS) that precede critical transitions in complex systems. The work spans theoretical analysis, numerical simulations, and applications to real-world climate and weather data.

PhD completed at the University of Reading 2021 in collaboration with the National Physical Laboratory (NPL), London. Supervised by Dr. Tobias Kuna and Dr. Valerie Livina. 

## Repository Structure

> **Note:** The MATLAB analysis code is maintained in a separate repository: [MatlabCodePhD](https://github.com/DrPrettyman/MatlabCodePhD)

```
PhD/
├── PythonCode/          # Python scripts and notebooks
├── Papers/              # Published and in-progress papers
├── Thesis/              # PhD thesis (LaTeX source)
├── Notes/               # Research notes and documentation
├── Literature/          # Reference papers and resources
├── Presentations/       # Conference talks and posters
├── GraphicsProjects/    # Figure design files
├── Assets/              # Shared images and resources
└── Admin/               # Administrative documents

```

## Publications

This research resulted in three journal publications, listed here:

**Prettyman, J.**, Kuna, T., & Livina, V. (2018). A novel scaling indicator of early warning signals helps anticipate tropical cyclones. *EPL (Europhysics Letters)*, 121(1), 10002.
[doi:10.1209/0295-5075/121/10002](https://doi.org/10.1209/0295-5075/121/10002)

**Prettyman, J.**, Kuna, T., & Livina, V. (2019). Generalized early warning signals in multivariate and gridded data with an application to tropical cyclones. *Chaos: An Interdisciplinary Journal of Nonlinear Science*, 29(7), 073105.
[doi:10.1063/1.5093495](https://doi.org/10.1063/1.5093495)

**Prettyman, J.**, Kuna, T., & Livina, V. (2022). Power spectrum scaling as a measure of critical slowing down and precursor to tipping points in dynamical systems. *Environmental Research Letters*, 17(3), 035004.
[doi:10.1088/1748-9326/ac526f](https://doi.org/10.1088/1748-9326/ac526f)

## Code

### MatlabCodePhD/
Primary codebase containing:
- **Core_Functions/** - Reusable EWS analysis functions (ACF, DFA, PSE, EOF)
- **Projects/** - Paper-specific analysis scripts
- **Data/** - HadISD weather data, ice cores, processed datasets
- **Tests/** - Unit tests for core functions

See [MatlabCodePhD/README.md](MatlabCodePhD/README.md) for detailed documentation.

### PythonCode/
Supplementary Python analysis and visualization scripts.

## Research Topics

### Critical Slowing Down
The phenomenon where systems approaching a tipping point recover more slowly from perturbations, manifesting as:
- Increased autocorrelation (ACF)
- Increased variance
- Spectral reddening (PSE)
- Changed scaling behavior (DFA)

### Methods Developed
1. **Sliding window indicators** - Track EWS evolution over time
2. **Scaling exponents** - DFA and spectral analysis for long-range correlations
3. **Multidimensional EWS** - EOF-based methods for multivariate systems
4. **Alternative EOF** - Projection maximizing autocorrelation rather than variance

### Applications
- **Dynamical systems** - Hopf, homoclinic, pitchfork bifurcations
- **Climate** - African Humid Period termination, Sahara greening
- **Weather** - Hurricane intensification using HadISD pressure data

## Notes Organization

| Folder | Contents |
|--------|----------|
| `01_Methods/` | EWS methodology notes |
| `02_Theory/` | Mathematical background |
| `03_Applications/` | Case study documentation |
| `04_Meeting_Notes/` | Supervisor meeting records |
| `05_Summaries/` | Paper summaries and reviews |
| `06_Feedback/` | Reviewer comments and responses |

## Getting Started

1. **Run MATLAB analysis:**
   ```matlab
   cd MatlabCodePhD
   addpath(genpath('Core_Functions'))
   % Run any project script
   ```

2. **Build thesis:**
   ```bash
   cd Thesis
   pdflatex main.tex
   bibtex main
   pdflatex main.tex
   pdflatex main.tex
   ```

## Dependencies

### MATLAB
- R2016b or later
- Statistics and Machine Learning Toolbox
- Signal Processing Toolbox

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
