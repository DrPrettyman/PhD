# Valerie's Email - Williamson Paper Exercise

Hello Joshua,

I see that in this exercise you have worked out example of Eq.24 of Williamson's paper with noise terms in the equations for X and Y.

## Questions/Suggestions:

- I wonder why noise level and amplitude in the your time series is much lower than in Fig.5? Did you use all the same parameter values?
- Plot phase portrait like in Fig. 3 of Williamson15 - maybe as 3D plot with variable mu?
- Take the obtained time series and attempt the estimation of the slowing down in the general system (Eq.9)

## Code style suggestions:

- Add labels and titles in plots (instead of just comments in the code) use commands `xlabel`, `ylabel`, `title`, where char variables can be substituted using `sprintf` command
- Start main script with commands:
  ```matlab
  clear all
  close all
  ```
  This allows one to run the script clearly multiple times during debugging and model adjustment

Best,
Valerie
