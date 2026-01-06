# Sensitivity analysis

Here we test the sensitivity of the data to the PS-indicator method by
calculating the indicator with a range of sliding window sizes. We hope
to use a sliding window of roughly 100 time points (hours) because any
longer would mask the indicator signal and a window much shorter than
100 points will introduce too much noise and distort the signal. This
has already been investigated in the paper (prettyman2018). In this
same paper it is noted that the indicator is strogest when the size of
the sliding window is an odd multiple of 6 hours, propably due to tidal
oscillations, this is confirmed by our brief analysis here.

Figure (top row) shows the the sea-level pressure time series for all
stations in the region for Katrina (left) and Gustav (right). The series
from all stations are aligned to the point of minimum pressure for that
particular series (time zero). Figure (bottom row) shows the
corresponding PS-indicator series where a 102-point sliding window has
been used for Katrina (left) and a 90-point window has been used for
Gustav (right). The solid black line in both panels shows the mean
PS-indicator. We note that the rise in the mean is barely visible and
certainly not significant. However, the plot does include the time
series from all stations in the region, some of which will be far from
the path of the hurricane and will have a weaker indicator signal, thus
affecting the average.



![](figures/allStations_Katrina.png)


![](figures/allStations_Gustav.png)

The sea-level pressure data from all weather stations in the
region are considered together, centered on the minimum pressure point,
during the occurence of hurricane Katrina (left) and Gustav (right). The
top panels show the sea-level pressure time series, the bottom panels
shown the PS-indicators calculated in a sliding window of 102 points
(Katrina) and 90 points (Gustav).


The contour plots in figure [2](#fig_sensitivity)
 show the PS-indicator values (for Katrina,
left, and Gustav, right) over time for various sliding window sizes in
the range 80 to 120 hours. These plots use the pressure series from all
the stations in the area, the same that are plotted in figure
[1](#fig_timeseries),
similarly centered on the point of minimum pressure. For Katrina we see
that choosing a window size of 102 or 114 points gives the most visible
indicator. We have chosen 102 because we do not want the window size to
be similar to the length of the series with which we are concerned.
Choosing, for example, a window size of 84 points (an even multiple of
6) gives an indicator which is very hight (2.5) at -100 hours, then
falls slightly, then rises again in the range 30 to 40 hours before the
minimum pressure, then falls again in the 30 hours before the minimum
pressure occurs. Such a signal does not provide an informative EWS.



![](figures/sensitivity_Katrina.png)


![](figures/sensitivity_Gustav.png)

Sensitivity analysis of PS-indicator. The PS-indicator for
the sea-level pressure series from hurricanes Katrina (left) and Gustav
(right) are calculated using sliding window lengths in the range 80 to
120 hours. Note that the strongest indicators are seen when using window
lengths of 102 hours (Katrina) and 90 hours (Gustav).


# calculating the Mann Kendall coefficient

We use the Mann-Kendall coefficient given by $$
\sum_{i=1}^{N-1}\sum_{j=i+1}^{N}\text{sign}(X_j-X_i)
$$ to asses the trend of the PS-indicator in a 36-hour
window before the time when the minimum pressure is reached at the first
station to feel the effect of the hurricane. A 36-hour window was chosen
by considering the contour plots presented in figure
[2](#fig_sensitivity).
It appears that this is the time window in which the indicator rises
most significantly (if at all).

At this time, we would expect to see the indicator at a high value at
the point of the first station, since the PS-indicator value we expect
to rise just before the hurricane arrives. At the stations further away
we expect to see lower values. In reality we do not see this expected
pattern due to the very high variability in the PS-indicator, it is
noted in (prettyman18) that while the PS-indicator appears to rise in
the mean, over 14 hurricanes considered, the signal in any one case
cannot be a reliable forcasting tool.
