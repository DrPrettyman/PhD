# Decay rate

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
both.

## Critical Slowing Down

(wagner2015) refers to critical slowing down as a "universal" EWS
(their emphasis).\
"However, the exact conditions under which CSD can be deduced from
observational time series are disputed in some recent studies\..."\
Apparently "it has been suggested that rising autocorrelation alone does
not indicate CSD". So presumably is has been suggested that rising
autocorrelation alone *does* indicate CSD, or they wouldn't have made
the previous comment.\
They give an example from an ice-albedo feedback, transition to snowball
earth model where "both variance and autocorrelation increase as the
instability draws near: both EWS indicators accurately give early
warning here that the cooling system is approaching a bifurcation."

# notes from (nicolis2007)

From the book *Foundations of Complex Systems*, (nicolis2007).\
The following quote is taken from the beginning of sec. 1.3.

\...the response of a system to changes of a control parameter is that
the onset of complexity \... is manifested by a cascade of transition
phenomena of an explosive nature to which is associated the universal
model of *bifurcation* and the related concepts of *instability* and
*chaos*. These are not foreseen in the laws of physics in which the
dependence on parameters is perfectly smooth. To use a colloquial term,
**one might say that they come as a "surprise"**.

Particularly interesting is the idea that the suddenness of a
bifurcation is somewhat *unexpected*, apparently one might expect the
transition to complexity to happen smoothly. The bifurcation itself
"comes as a surprise", which lends some irony to this PhD project, which
aims to predict and even to *expect* the transitions.\
I have been thinking (especially when experimenting with MatLab) about
smooth changes. In particular I have been looking at a 'one-hump' kernal
evolving into a 'two-hump' kernal. However, I have also seen the classic
"pitch fork bifurcation" picture, which I am reminded of by the figure
Fig. 3.4 on page 80 (recreated by me, Fig
[1](#bad_drawing)). Rather
than a smooth evolution, the one-hump, bell-shaped distribution suddenly
collapses into a two-hump.\

![Probabilistic analogue of bifurcation. Solid line: two-humped
distribution in the regime of two simultaneously stable states.
Dashed-line: distribution at
criticality.](../images/bad_drawing.png){#bad_drawing width="10cm"}

[^1]: I think I have answered the question of what a critical mode is in
    the discussion on Potential Analysis. That is, a critical mode is a
    potential well that looks like it might not be a potential well for
    much longer
