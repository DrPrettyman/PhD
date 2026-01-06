# Further investigation into HadISD data auto-correlations 

First we look at a selection of hurricanes which pass over southern
Florida. This is so that the same station is selected from the HadISD
dataset for all time series. It would of course be possible to look at
other hurricanes in other areas, one would have to select a station
somewhere on its path. This will probably be considered if this Florida
trial looks like it may have some useful result.\
The hurricanes considered are:\

  Andrew:                24-Sep-1992 09:00:00
  ---------------------- ----------------------
  Floyd:                 14-Sep-1999 21:00:00
  (preceeds TS Harvey)    
  Charley:               13-Aug-2004 12:00:00
  Frances:               05-Sep-2004 10:00:00
  Jeanne:                26-Sep-2004 09:00:00
  Katrina:               26-Aug-2005 12:00:00
  Rita:                  20-Sep-2005 18:00:00
  Ernesto:               30-Aug-2006 09:00:00
  TS Bonnie:             10-Aug-2010 08:00:00

\
Where "TS" stands for "Tropical Storm" (a lower category storm than
"Hurricane"). The dates and times shown indicate the time when the
hurricane passed over station 2 (at lat/lon coordinates $24.56^o$ N,
$-81.75^o$ E) This time is detected by looking for the low pressure
spike in the slp (sea level pressure) time series.\

![A selection of Florida storms. SLP (top) and ACF-1 coefficient in a
240 point (ten-day) sliding window, (bottom).
](../images/Allstorms_strong_st2.png){#strong_storms


Figure [1](#strong_storms)
 shows a selection of these storms plotted
together, centred about the low-pressure spike. The storms not shown in
this plot are of a very different nature and have a much weaker 'spike',
it may be advisable to analyse these separately or not at all. In any
case, it confuses me to have too many series all plotted together, so
doing some separately would be advisable anyway.\
In Figure [1](#strong_storms)
 we can see a clear 12-hourly (bi-daily)
oscillation in all the time series, maybe something to do with tides or
something physical like that. Maybe (!) this is influencing the
autocorrelations. Let's have a look at the same thing, but with the
oscillations removed (by subtracting the mean deseasonalising method),
this is shown in Figure [2](#strong_storms_RO)
.

![A selection of Florida storms. SLP with oscillating trend removed
(top) and ACF-1 coefficient in a 240 point (ten-day) sliding window,
(bottom). ](../images/Allstorms_strong_st2_RO.png){#strong_storms_RO


Note from Valerie:

> "In the first plot, the lowering of pressure starts about 50hr before
> the deep, which is interesting. Two days in advance, and this is when
> the trend becomes visible. For early warning signal, we would need to
> look at time scale earlier than that, I think. It may be that the
> necessary information is in the Fig.2, but to see it clearly, we would
> need to rescale that plot, for interval \[-150, -50\]."

Following Valerie's advice, we rescale the plots (shown in Figure
[3](#strong_storms_RO_zoom)
) which makes it more obvious the
completely opposite reactions in the ACF-1 indicators of Andrew and
Katrina. It does seem, though, that Floyd and Jeanne exhibit a similar
reaction to Katrina, i.e. the indicator rises before the spike. There is
certainly no visible change in the indicator for Frances, and Andrew's
actually decreases. (Frances and Andrew are shown in light and dark blue
resp.).\

![The same as Figure [2](#strong_storms_RO)
 (with top-left, bottom-right
reorientation) only with the $x$ axis restricted to the 150 hour period
before the storm (at time zero).
](../images/Allstorms_strong_st2_RO_zoom.png){#strong_storms_RO_zoom


We also show the DFA indicator (Figure
[4](#strong_storms_RO_DFA)
), but this doesn't seem to show us
very much. I have also plotted the DFA indicator where the raw data is
used as input (that is, without removing the bi-daily oscillations) but
this is clearly unhelpful so I have not included it here.

![The slp data shown alongside the DFA indicator in a sliding 120-point
window. The DFA uses $2^\text{nd}$ order polynomial
detrending.](../images/Allstorms_strong_st2_RO_DFA.png){#strong_storms_RO_DFA


# Next step

The next step will be to create a model by adding noise to a sine wave
with a dip at the end, something like Figure
[5](#badmodel). As it is,
this model isn't going to be very useful. More work to be done.

![A 'model' hurricane pressure signature. A 12-hourly oscillation has a
parabolic trend imposed at the end (48 hours from the
end).](../images/verybadmodel.png)
