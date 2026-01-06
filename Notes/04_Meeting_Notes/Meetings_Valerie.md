# 5 June 2017 (before meeting)

## Tipping points definition

With Tobias I have been discussing the definition of a tipping point,
starting with the "three types of tipping points" in (livina2011).
Maybe the concept of a tipping point is from observations in nature, so
there cannot be a good mathematical definition.\
The typical tipping from one state to another in a double well system is
a combination of noise (c.f. "noise induced transition") and a
becoming-shallower of the well (c.f. "genuine bifurcation"). A
transition caused only by the white noise, we cannot predict, because it
happens at random. However, if the potential changes shape, we can see
that the noise moves all in one direction. Hence autocorrelation.\
I commented some time ago about the example in (livina2011):
$$


\dot{z}(t) & = -(z^4 - 2z^2)' + \sigma(t)\eta \\
\sigma(t) & = -0.00007t+1.50045.

$$ In this system, the noise term grows smaller, but the
exact same output is found by making the wells steeper. Essentially, to
increase the noise is the same as to make the well shallower (in this
sort of system at least). There are three parameters (the coefficients
of $z^4$, $z^2$ and $\eta$) and we are able to change what we see by
rescaling $z$ and $t$, so really we are able to eliminate two parameters
and see that the whole thing is governed by a single parameter dictating
the steepness of the wells -- at least up to a rescaling of $z$ and
$t$.\
I think there is a separate problem where we can estimate the shape of
the potential, then we can see if we are already close to a saddle and
so more likely to tip over into the other well.\

1.  If we see that $x$ has increased 5 time-steps in a row, is this by
    chance? and then it will just as likely decrease next time as
    continue too increase. Or is it because the well has become
    shallower (or convex) and so we can say \"yes, it will continue to
    increase.\"\

2.  A separate problem: we see that $x$ is close to a value for some
    time, so it is in well. How steep is the well? How close is the
    saddle to the trough?

## Autocorrelation

To measure the autocorrelation is to approximate the system by a linear
model. I have previously been concerned by this but, it seems, this is
usually all right if the system doesn't change much inside the time
window. However, note that we need an infinitely large window for the
statistics to be correct. Also note that the system looks less linear as
we leave the bottom of the well: as we approach the tipping point the
ACF (the method for detecting the tipping point) becomes less accurate.\
Also, close to the saddle point the curvature decreases, it becomes
easier to approach the saddle the close we get.\
It all is worth considering.

## Writing a paper

The most important point to come out of the monitoring meeting is that
by this time I should have produced a \"body of work\". Either a thesis
chapter or a paper (or a draft).\
There is the project of the cyclone tipping point. What is there so
far?\

1.  Background reading about fingerprinting methods.

2.  Downloaded weather station data from points close to cyclone
    "landfall".

3.  Removing 12-hour (possibly tidal) oscillations from data. This was
    interesting because using a Fourier method to remove the peak at the
    exact frequency gave a near-identical result to using the naive
    method 'de-seasonalising'. See figure
    [1](#fig_jun17_oscilations)
    reference="fig_jun17_oscilations"}

4.  Applying methods to the data, experimenting with different window
    size and time lag (these can be plotted together as contour plots).

![[]Showing the
pressure in the run-up to Hurricane Rita. The oscillation is removed
from the signal by subtracting a sine wave (top) and this is compared to
the naive "de-seasonalising" method (bottom). The two methods produce a
very similar
result.](../images/remove_osc_2mthRITA.png){#fig_jun17_oscilations
width="90%"}

# 8 June (meeting at Tobias' office)

To summarise our discussion, please prepare the figures for the paper,
with real and artificial data (ACF, PS) and send them by Monday, 13th
June, for comments. Then work on the content of Methodology-Data-Results
based on your recent report and email the draft by Friday, 16th June.\
XMGrace is often more convenient than Matlab in making figures (and it
supports high-quality eps-format):
http://plasma-gate.weizmann.ac.il/Grace/

# 11 June (week)

The week of 11th June was spent replotting hurricane data.\
Valerie has some plots that look somewhat different to mine. We are
plotting the PSE indicator - power spectrum scaling exponent. This is
from an estimation of the slope of the log-log plot of the power
spectrum of a signal.\
The easiest way to approximate the power spectrum is with the
periodogram - simply the square of the absolute value of the fast
Fourier transform (fft) plotted against frequency. There are other
methods, including Welch's method which is built into MatLab, but it
seems reasonable to stick with the simplest method that at least we
understand well.\

## From Valerie:

In your figures, I can see that there is a clear result for the model,
but the indicators for the real data oscillate at very high level
(0.96), which is most likely because the window size is too small. In my
figure, I cut the data 100 datapoints before the pressure deep, so that
the declining trend in the last part of data would not affect the early
warning signal, and used a sliding window of 150 points (what are the
time units here, hours?) I guess you can take even window of 200 points
to get a clear trend in the indicators. Can you please do this for
figure 3? Let's stick with figures 1-4 for now.\
Concentrate on figure 3 now and recalculate it with a bigger window size
-- I would like to see the average curve with errorbar for wl=150 and
200. I think you miss the signal because in smaller windows weather
noise dominates.\
I remember you earlier did contour plots with sensitivity analysis
regarding the choice of the window (how the trend in the indicator
depends on the size of the sliding window) -- can you please find it and
include in the draft?

# Summary of emails from June 2017

For two hurricanes I have, Katrina and Rita, I just plotted the
power-spectrum-based indicator, see the attached figure. Note that I
used large enough window to calculate the indicator.\
As I look at your figures, it is not clear to me how you got values of
this indicator, on average, around 2.5-3. It seems too high. Can you
please send me a plot of a single power spectrum of one hurricane, and
show in some way (colour or markers) what frequency interval you
consider for estimation of the slope. Your high values may be due to a
very noisy power spectrum for a subset of the data in a small window,
and we have to check it to ensure there is no other technical reason,
like a code bug.

![](ValsPlots/ValsPlots_KandR_pse.jpg)

# After Valerie's visit to Exeter

Now we are both looking at the same thing when we plot the PSE
indicator. Let's look at it in detail.\
We calculate the indicator for a variety of window sizes to see which
will best give an EWS, some of them give a good EWS and some show no
significant increase before the \"event\". We expect that for a very
small window size the signal will be too noisy, and for a very large
window size the effect will be smoothed out - there should be a balance
point where there is the best possible signal.\
In fact we find a strange pattern. Figure
[2](#PSEcontoursensitivity)
 shows a contour plot comparing the
different PSE indicators for varying window sizes. We see that some
(such as at window size $=100$) happily show expected signals: a low
value near $0$ which rises to a value close to $1$ at the end of the
series. Whereas others (such as window size $=190$) show a value above
$1$ for the whole series. In fact we see that there is a pattern, a
periodicity of 60. Figure [3](#PSEgoodones)
 shows the PSE indicators for window sizes 40,
100, 160 and 220 (notice the separation of 60), which show the expected
behaviour. Figure [4](#PSEbadones)
 shows the indicator for window sizes 70, 130 and
190.

![Showing the PSE indicator for many different window sizes separated by
10.](../images/PSEcontoursensitivity.png){#PSEcontoursensitivity


![Showing PSE indicator for window sizes 40, 100, 160 and 220 (blue,
red, yellow, purple resp.). Labels could be added. There is a clear
rising EWS.](../images/PSEgoodones.png){#PSEgoodones


![Showing PSE indicator for window sizes 70, 130 and 190 (blue, red,
yellow resp.). Labels could be added. There is no obvious EWS,
especially for ws=190. Notice also that the values are higher than
expected ($>1$). ](../images/PSEbadones.png){#PSEbadones


Now, we have noted before that there is a clear 12-hour oscillation
pattern in the raw data, and our pattern here has a periodicity of 60.
60 happens to be the common multiple of 12 and 10 (10 is the separation
of window sizes). Something is up.\
Figure [5](#fig_PSEcontoursensitivityRO)
 shows the same as figure
[2](#PSEcontoursensitivity)
 for the "oscillations removed" data.
We see that this obviously destroys the 60 pattern. But we also see that
there is no EWS in any of the window sizes, and also the values are
really high. This is exactly the problem we previously had, but expected
we had solved because we checked our code against Valerie's for
calculating PSE and found that they were identical (after some trial and
error). However, we remember that the sample of data we were testing on
was raw data from hurricane Katrina, not the oscillation-removed data.\
Possibly there is something wrong with the way we calculate PSE. Also
likely is that there is something incorrect about the way we remove the
oscillations.

![ Showing the PSE indicator for many different window sizes separated
by 10, for the "oscillations removed" data. Notice that all the values
are $>1$ and there is no clear
pattern](../images/PSEcontoursensitivityRO.png){#fig_PSEcontoursensitivityRO


## Note

Note that for the figures in this section we have followed the following
method:

1.  Select a window size.

2.  Using this window size, calculate the sliding PSE indicator,
    separately, for all of the cyclones (sea level pressure time
    series).

3.  Take the mean of all 14 PSE-indicator series, giving one mean PSE
    series.

4.  Repeat for a variety of window sizes.

In this experiment we chose window sizes 40, 50, 60, 70, \..., 240, 250.
Possibly it would be interesting to investigate window sizes separated
by 12 instead of 10.

## Valerie's comments on this section

Regarding the removed oscillations. I took the 1st time series from your
mat-file (hurricane Andrew) and considered the raw data, from which I
just subtracted its mean value (so that mean=0). I plotted it together
with the data obtained with 12-hour-periodicity removal ? see the
attached ?fig1.pdf?. If you rescale this figure to look closer, you can
see much smoothened curve, which lost that high-frequency periodicity.
And this also creates higher dependence of the neighbourhood points,
i.e. increases correlations. This is why the slope of the power spectrum
changes, and you see higher PS exponent after this procedure. In
addition to this effect, the 12-point periodicity appears to happen
exactly inside our window of interest, where we measure the slope:
10-100 time units (in frequency, it is value 0.08). Moreover, we are
also dealing with the case of short time series where we estimate the
exponent, i.e. there is finite size effect, which particularly affects
the very first points of the power spectrum. For a large data, power
spectrum would have sufficient statistics in the range of interest
despite the periodicity peak (?fig2.pdf?). See also the attached figures
?fig3.pdf?, ?fig4.pdf?, ?fig5.pdf? for comparison of spectra for subsets
of data, to see how the size of the small set affects the spectra.\
Note also that when you remove the 12-point periodicity, not only it
removes the spike at frequency 0.08, but it also produces perturbation
at frequency 0.025, which corresponds to about 36-hour cycle. For a
bigger window, there is also a new deep oscillation at frequency 0.04
(24 points cycle).\
For the purposes of the paper, all this should be 1) illustrated on
artificial data alongside with real data; 2) explained in detail with
figures (in particular, figures with power spectrum itself)\
I would suggest you to use raw data for the EWS analysis. And bigger
windows, based on the sensitivity plots. Remember that our purpose is
not to filter the data out of the periodicity of any kind. Our purpose
is to uncover the EWS signal, which is hidden in the data. Sensitivity
analysis helps to identify the right parameters for this purpose.\
Generate artificial data with similar properties and repeat the analysis
for an ensemble of sample. For artificial data, you can do logarithmic
binning of the power spectrum, which would help you to estimate the
correct slope value (you can try this with and without removal of the
periodicity).\
