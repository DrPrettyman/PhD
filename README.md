# PhD Research Repository

**Early Warning Signals for Critical Transitions**

This repository contains all materials from my PhD research on detecting early warning signals (EWS) that precede critical transitions in complex systems. The work spans theoretical analysis, numerical simulations, and applications to real-world climate and weather data.

> **Note:** The MATLAB analysis code is maintained in a separate repository: [PhD_Matlab](https://github.com/DrPrettyman/PhD_Matlab)

## Repository Structure

```
PhD/
├── MatlabCode/          # Analysis code and core functions
├── PythonCode/          # Python scripts and notebooks
├── Papers/              # Published and in-progress papers
├── Thesis/              # PhD thesis (LaTeX source)
├── Notes/               # Research notes and documentation
├── Literature/          # Reference papers and resources
├── Presentations/       # Conference talks and posters
├── GraphicsProjects/    # Figure design files
├── Assets/              # Shared images and resources
├── Admin/               # Administrative documents
└── *.pdf                # Final thesis and publications
```

## Key Outputs

| Document | Description |
|----------|-------------|
| `JPrettyman_PhD.pdf` | Final submitted PhD thesis |
| `Prettyman_Thesis.pdf` | Thesis with corrections |

## Publications

### Paper 1 - EPL (Europhysics Letters)
Early warning signals using scaling indicators (DFA, PSE) applied to model systems.

### Paper 2 - Chaos
Multidimensional early warning signals using EOF-based methods.

### Paper 3 - ERL (Environmental Research Letters)
Application to paleoclimate transitions (African Humid Period).

## Code

### MatlabCode/
Primary codebase containing:
- **Core_Functions/** - Reusable EWS analysis functions (ACF, DFA, PSE, EOF)
- **Projects/** - Paper-specific analysis scripts
- **Data/** - HadISD weather data, ice cores, processed datasets
- **Tests/** - Unit tests for core functions

See [MatlabCode/README.md](MatlabCode/README.md) for detailed documentation.

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
   cd MatlabCode
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
