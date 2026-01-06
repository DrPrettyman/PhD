# Visit to Valerie's office: 08/12/16

Valerie has remarked, based on the comments from the seminar I gave at
NPL, that I should start to work on a multidimensional stochastic model
for early warning signals.\
What does this mean? We want to fit a model to the data (tropical
cyclone, or in general) and the model wants to look like:
$$
\frac{dx}{dt} = -\frac{\partial}{\partial x} U(x,t) + A_1(x,t)  + A_2(x,t) + T(x,t) + \eta
$$ Where $U$ is a potential and $A_1$, $A_2$ are maybe tidal
and seasonal oscillations and $T$ is a trend. Maybe not all will have a
dependence on both $x$ and $t$. $eta$ is a noise term but so far we
won't make any commitments, it could be Brownian noise. It is suggested
to estimate the shapes of $U$, $A_1$, $A_2$, $T$ using Kalman filter.
Read papers by Kwasniok.\
Then what about having a system of such equations, where we also write
the same thing for another variable $y$? Maybe $x$ is pressure and $y$
is wind speed. Possibly we can expand to even more variables.\
Then when we have this system of equations we use a method similar to
that in (williamson2015) to compute some eigenvalues of something
derived analytically from the equations and maybe these eigenvalues will
somehow provide an early warning signal.

# Identifying things on which to focus

This PhD seems to have many parts and this is distracting. I would like
to concentrate on each part and keep track of what I am doing. I have
therefore decided to identify different focal points.

## 1 - Understanding EOF

I am referring to the question posed by Tobias: "Does it make sense to
use the principal EOF component to summarise an entire data-set in the
way that is suggested by (held2004)?" Or, under what circumstances
(i.e. for which type of dynamical system) does the first EOF give useful
information? In (held2004) the sliding-window ACF of the first EOF is
calculated. The traditional justification for this is that the first EOF
"captures" the interesting features of the system because it "captures"
the majority of the variance. However, it is not clear that this
variance tells us very much about a bifurcation - or is it? How likely
is this? Surely for some systems the orthogonal component with the most
variance might contain no information about a bifurcation, one can
certainly think of obtuse cases to illustrate.

## 2 - The ACF method

Does the ACF of a time series give useful information (or even an EWS)
about an up-coming event? Which method should be used? There are three
that I have tried:

1.  The straight-forward ACF estimator. This could probably be improved
    with a few alterations (see previous discussion with Tobias about
    rank correlation). Or maybe we can construct a new estimator by
    using maximum likelihood or something.

2.  The power-spectrum scaling exponent. Currently have only estimated
    the PS from the 'periodogram', probably could improve this by using
    a low-pass filter or 'binning' to reduce noise; or just using a
    different estimator such as multi-taper (see notes from Tromsø).

3.  The DFA method. Not really much to muse about.

All of these methods are employing a sliding-window of points, so the
size of the window is also to be decided (uncertainty quantification).
Also, can we up-grade our insights to more than one variable, as in
(williamson2015)? There seem to be many questions raised by this paper.

## 3 - The Power Spectrum

Related to point (2). I have not exploited the relationship between the
time and frequency domains (this sounds like wavelets), maybe something
useful here. The point is that maybe there are other signatures within
the PS that are not just the scaling exponent. At least I think that is
the point.

## 4 - Tropical cyclone data and potentially other data

Can we make a model (SDE) to fit the data? Do we want to? (See all notes
from April 2016 onwards, including today's). More simply: does the ACF
tell us anything (now we have tested it on a lot of data we should be
able to say something about this.

## 5 - Simple SDE models

Can you calculate the ACF "on paper" if you have the model? Probably
easier to turn the ACF formula into an SDE than solve the SDE for the
dynamical system. Also, can we classify dynamical systems according to
how much the ACF can tell us about upcoming events/bifurcations? Is it
useful to do this? (i.e. which sort of systems should be considered?)
