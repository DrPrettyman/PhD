To summarise quickly: I have so far looked at the methods used by
Valerie and others to detect tipping points from data. these are:

## Degenerate Fingerprinting

As I understand it, degenerate fingerprinting is:

1.  Calculate the Auto Correlation Function (ACF) in a sliding window

2.  When they get more correlated (approaching a "critical value"
    i.e. 1) something may or may not be about to happen or has probably
    started happening. Or may it already happened.

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
$$ and you can use your estimate of this "correlation
exponent" to say how correlated the data is, therefore the same as
Finger Printing after this point.

## Potential Analysis

Assume the data is the observable from some noisy double-well potential
system and that we want to detect a genuine bifurcation in the system
(like one well $\rightarrow$ two wells or the other way around) or some
sort of external forcing being added to the system.\
We can estimate the shape of the potential function by using a kernel
function and some sample data. at least that is is what I understood
from the following email Q&A with Valerie

- Do you mean that the potential function is estimated from the
  kernel-fitted pdf of a sample taken from a time-window?

- One can do both. From the kernel pdf, one can estimate the shape of
  the potential function. It can be kernel of the entire time series, or
  a sub-set in a time window. Furthermore, you can estimate coefficients
  of the potential function, from the sub-sets in time windows, and see
  how they change along the time series.

- I suppose then we can interpret \"unstable mode\" as a vanishing peak
  (as the window moves forwards in time).

- Correct.

## Decay rate

What is meant by **decay rate**? This is a property of a time series.
Valerie says "for a system approaching a bifurcation, a near-universal
property is that the **decay rate** will tend to infinity - a phenomenon
known as **critical slowing down**".\
Held remarks: "One then strives at isolating the dynamics of the most
unstable mode or 'critical mode'[^1], this being characterized by the
smallest decay rate." And also: "the knowledge of the decay rate
decisively reduces uncertainty about the proximity to the bifurcation
threshold." which sounds very relevant to this project.\
As far as I have found out, I think that the **decay rate** (of series
$X$ for example) refers to the rate at which $$
ACF_{\text{lag}~n}(X)\xrightarrow[n\rightarrow\infty]{}0.
$$ The rate at which the lag-$n$ autocorrelations decay to
zero as $n\rightarrow\infty$. Which isn't the same thing we were doing
with Degenerate Finger Printing, although autocorrelation is involved in
both. However, the papers which mention them seem to talk about them as
if they are doing the same thing.\
When Valerie says "for a system approaching a bifurcation, a
near-universal property is that the **decay rate** will tend to
infinity\" the ACF is therefore going to zero very quickly, i.e. there
may be strong lag-0 correlation but no lag-1 correlation but this is at
odds with everything that makes sense. Surely it's the other way around:
the decay rate goes to zero? i.e. the ACF is going to zero very slowly.
This seems to fit nicely with the other aspects of Degenerate
Fingerprinting.\
I think then that in Finger Printing we should maybe look at lag-2
correlations as well to get a more comprehensive picture.

## ARIMA models

Also I have spent a lot of time reading about how to generate noisy data
with different types of noise. This felt quite tangential but I ended up
following through for a quite a long time. I'm not really sure if this
has helped me to figure out tipping points, but at least I know there's
more to noise than white noise.\
Also, one can try to fit data to a model and use the model to study the
system.

# Dynamical Systems

All this talk of dynamical systems (cf. decay rate) makes me think I
need to read up a bit. These *Time Series Analysis* books (eg Box
Jenkins) don't mention anything but the time series we're looking at are
supposed to be the observables of some chaotic dynamical system (the
climate), so it can't hurt to know a bit about them.\
The last few days I've been reading about dynamical systems but it's
quite a big area. I've been reading about bifurcations but I had to go
back to some introductory stuff to understand, so not much progress.

[^1]: I think I have answered the question of what a critical mode is in
    the discussion on Potential Analysis. That is, a critical mode is a
    potential well that looks like it might not be a potential well for
    much longer
