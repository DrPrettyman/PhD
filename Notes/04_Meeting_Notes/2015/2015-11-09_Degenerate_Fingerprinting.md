# Summary

I feel like I've read a bit about Degenerate Fingerprinting, DFA and
ARMA models now. I keep getting distracted reading about Chaotic
Dynamical Systems and other thing that seem relevant to the overall
project but maybe they're not and maybe I'm just easily distracted.
Anyway, this seems like a good point to summarise what I've done so far.

## Degenerate Fingerprinting

As I understand it, degenerate fingerprinting is:

1.  Calculate the ACF in a sliding window

2.  If the ACF is approaching a "critical value" i.e. 1, speculate that
    a bifurcation is immanent.

(held2004) states that in each window the series is modeled by the
AR(1) process $$
y_{n+1} = cy_n + \eta_n  ~~~~~ c=\exp(-\kappa\Delta t)
$$ where $\eta$ is some Gaussian noise. I think by "modeling
the data" they are simply estimating $c$ from the ACF. It is then this
value of $c$, or the value of the ACF, which is analysed and found to be
close to some critical value. (livina2007) used DFA instead of ACF but
I think the general idea is essentially the same.

## DFA

Detrended fluctuation analysis involves chopping the data into segments,
detrending each segment by subtracting a polynomial fit, finding the
variance of each segment, take the root mean square of all of these
variances. This gives you the fluctuation function $F^{(n)}(s)$ where
$n$ is the order of the polynomial fit used, and $s$ is the
segment-length.\
DFA allows you to estimate the correlation exponent, which is related to
the value $\alpha$, which is related to $F^{(n)}(s)$ by the equation
$$
F^{(n)}(s) \propto s^\alpha.
$$
