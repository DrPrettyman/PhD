# Thoughts on the uses of ACF and PSE

What is the reason for ACF?\
We say that we have a constant function with added noise. Really this is
a single-well potential. We say that when the system is perturbed it
returns to the bottom of the well (equilibrium) with rate $\kappa$. As a
bifurcation approaches the well becomes shallower, thus the system takes
longer to return ($\kappa\rightarrow 0$).\
The auto-correlation is used because we suppose that the system just
after the disturbance is modelled by the AR1 model: $$

y_{n+1} = e^{\kappa\Delta t}y_{n} + \eta_n
$$ (held2004; @scheffer2009). Where $\eta_n$ are independent
and Gaussian, the state $y_n=0$ is the equilibrium.\
OK, here are some questions and remarks:

1.  The system must be very badly modelled by
    eqn.[\[AR1\]](#AR1). The real
    system will return to equilibrium in some manner described by the
    shape of the potential well (if one can even make the comparison to
    a well-potential at all).

2.  Whatever governs the return of the system, it is often a continuous
    function. If we apply the ACF$_1$ formula to $\{y_n\}$ from
    eqn.[\[AR1\]](#AR1) we recover
    $\exp(\kappa\Delta t)$. If we have a discretely-sampled continuous
    function we will get something depending on the sampling rate.

3.  From the previous point, there is no reason to suppose that ACF$_1$
    (lag 1) is giving us any more useful information that ACF$_2$ (or
    higher) except for the fact that it is less likely to be noisy and
    more likely to be an indicator of short-term memory.

4.  I'm not sure what we really what we really want to find. I would
    guess $\lim[\text{ACF}_l]_{l\rightarrow 0}$ but that would just be
    1.

Possibly it would be a good idea to use a combination of many lags to
create a function such as $$
F(X) = \text{ACF}_1(X) + \frac{1}{2}\text{ACF}_2(X) + \frac{1}{3}\text{ACF}_3(X) + \dots
$$ but this is just a guess. What would it mean to combine
the differently lagged functions?\
How does the lag relate to the supposed Critical Slowing Down (CSD)? We
know that the classic stationary-system example predicts a shift from
short-term memory (white noise) to long-term memory (AR(1) process) as
the bifurcation is approached. \[? is this correct ?\] We want to detect
this. Possibly we should measure the relative sizes of small-lag and
large-lag ACF values, such as $$
F(X) = \frac{\text{ACF}_1(X)}{\text{ACF}_2(X)} + \frac{\text{ACF}_2(X)}{\text{ACF}_3(X)} + \frac{\text{ACF}_3(X)}{\text{ACF}_4(X)} + \dots,
$$ but again, this is a guess for now.\
Say we have an AR1 process and an AR2 process described by
$$
X_1: ~~x_n &= \phi_1 x_{n-1} + \eta\\
\text{and~~} X_2: ~~x_n &= \phi_1 x_{n-1} + \phi_2 x_{n-2} + \eta
$$ resp.. We can calculate the ACF of each using different
lags, $$
&ACF_1(X_1) = \phi_1 &&ACF_2(X_1) = \phi_1^2\\
&ACF_1(X_2) = \frac{\phi_1}{1-\phi_2} &&ACF_2(X_2) = \frac{\phi_1^2}{1-\phi_2}+\phi_2,
$$ note that these are expected values. In fact we find that
this is quite simple: $$
ACF_l(X_1) &= \phi_1^l\\
ACF_l(X_2) &= \phi_1 ACF_{l-1}(X_2) + \phi_2 ACF_{l-2}(X_2)\\
\text{even~~} ACF_{l}(X_k) &= \sum_{j=1}^l ACF_{j}(X_k)
$$ probably there's a way to formulate a closed form that has
already been done.\
Anyway, the original motivation for using ACF was the idea that we have
a ball in a potential well, moving around with random noise, as the well
gets shallower the perturbations get larger and therefore the ball takes
longer to return to the bottom of the well. These longer return times
imply an increase in ACF$_1$.\
So with this in mind, maybe let's model it with an actual well-potential
system. Does this imply that we should take higher-laged ACF into
account?

# What do they do in (held2004)?

1.  We suggest to measure the smallest decay rate of the system under
    investigation and to consider its trend. We argue that this is the
    diagnostic variable most directly linked to the distance from a
    bifurcation threshold.

2.  Claim: multi-stability is an important concept. Therefore we study a
    system that may switch equilibria under global warming (GW)
    conditions. i.e. GW may shift a parameter $\mu$ over a critical
    value $\mu^*$, called bifurcation point

3.  We base our approach on the most fundamental, model-independent
    property of ??*any*?? bifurcation: the fact that the smallest
    system-immanent decay rate $\kappa$ for perturbations of the
    equilibrium vanishes and the variability of the related mode
    diverges.

4.  one implicitly assumes that the quasi-stationary dynamics can be
    simplified as an equilibrium of a deterministic dynamics which is
    stochastically perturbed by weather-generated noise.

5.  In the small-noise limit, the response to noise can be approximated
    by the dynamics of linear modes. As a fundamental insight from
    dynamical systems theory, at any bifurcation, one mode becomes
    unstable, hence, the smallest decay rate $\kappa$ of a perturbation
    vanishes \[e.g., Wiggins, 1990\].

<!-- -->

1.  Summary: Measure the smallest decay rate of the system and consider
    its trend. Claim: this is the diagnostic variable most directly
    linked to the distance from a bifurcation threshold.

2.  We want a system with multi-stability. Abrupt climate changes in
    response to gradual changes in forcing.

3.  Takes longer to return to equilibrium as the bifurcation
    approaches - this is true for "any" bifurcation.

4.  Any (quasi-stationary) dynamics can be thought of as the equilibrium
    state of a deterministic dynamical system with stochastic noise.

5.  In the small-noise limit, the response to noise can be approximated
    by the dynamics of linear modes. As a fundamental insight from
    dynamical systems theory, at any bifurcation, one mode becomes
    unstable, hence, the smallest decay rate $\kappa$ of a perturbation
    vanishes \[e.g., Wiggins, 1990\].
