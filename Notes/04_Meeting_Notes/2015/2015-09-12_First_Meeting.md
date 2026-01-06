# Meeting with Valerie and Tobias

We discussed 'Degenerate Fingerprinting' which gives an 'Early Warning
Signal'. The jist is that there is a change in the autocorrelation of a
time series when approaching a bifurcation. The autocorrelation ought to
decrease with increasing lag and the rate of this decrease is greater
when there is less memory in the series. In a completely memory-less
series the lag-1 autocorrelation is $\approx 0$. We expect that the
autocorrelation will increase if the series is about to change, this is
the 'early warning signal'.\
We did not discuss 'Potential Analysis' in details.\
I have written a note to myself: "The power spectrum is the Fourier
transform of the autocorrelation".\
We have agreed that I will:

- Write up everything each Friday that I have done that week. The
  write-up should be as if to explain to Tobias what Valerie has
  explained to me or what I have learnt otherwise.

- Send this to Tobias and Valerie.

- Go to NPL sometime and register there.

- Download and use xmgrace for plots.

- Use CITRIX to access my desktop at NPL remotely (after registering at
  NPL.

- Ask questions frequently.

# Becoming familiar with MatLab

This week I have installed MatLab and have tried to re-familiarise
myself with it. I have tried to reproduce Figure 3 (a) in Valerie's
paper *Changing climate states and stability: from Pliocene to present,
2011*, which is shown in Figure [1](#Figure3a)
. The data is artificially generated with a
double-well potential given by $$
U(z) = z^4 - 2z^2
$$ and has added time-dependent noise so that the system is
defined by $$
\dot{z}(t) = -(z^4 - 2z^2)' + \sigma(t)\eta,
$$ where $\eta$ is Gaussian noise and
$\sigma(t)= -0.00007t+1.50045$ so that the noise level decreases from
$1.5$ to $0.1$ as $t$ goes from $1$ to $20 000$. The field $\dot{z}(t)$
is plotted (using MatLab) for a few values of $t$ in Figure
[2](#vectorField). The
noise-less system has stable 'wells' at $z=\pm 1$ and a not-stable
stationary point at $z=0$.\


![](../images/Figure3a.png)




![](../images/vectorField.png)



So I don't understand where Figure [1](#Figure3a)
 comes from because rather than the noise-level
decreasing it appears that the potential wells are moving closer to zero
(and the noise is also decreasing, on closer inspection).\
I used the system $$
\dot{z}(t) = -(z^4 - 2z^2)' + \sigma(t)\eta,
$$ to plot the signal $z$ shown in Figure
[3](#signal), which makes more
sense because the wells stay at $\pm 1$ but the noise level decreases.
When the noise level is too small the signal stays in just one of the
wells because it can't get out.\


![](../images/signalPlot1.png)



Anyway, I have also tried to write a MatLab script that calculates the
autocorrelation in a sliding window, but I'm getting a little confused,
the MatLab I knew back in second year has been replaced by python and
C++ since then. MatLab handles lists, arrays and structures in a strange
way I have decided, but I'll get used to it.

# To do list

- reread *Held and Kleinen, 2004* and *Livina and Lenton 2007*.

- become better acquainted with MatLab.

- plot the Autocorrelation of a time series.

- plot the Power Spectrum.

- read about the Fourier transform and the Power spectrum to the point
  of being able to ask questions.
