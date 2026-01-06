# Is the ACF a good thing to look at?

I am wondering if the apparent rise in the ACF-1 indicator, which can be
seen in the cases of Katrina, Jeanne and Floyd, but not in the case of
Frances -where there is no change- nor Andrew -where there is a
decrease- is telling us anything general or if it may be down to
chance.\
I have taken the data from station 2 (from where the data used to
produce the plots in the previous notes was taken) in a 16 year period
from 1990-2005. Figure [1](#16_years)
 (top) shows all 16 years pressure data plotted
together. Note that there are a few steep valleys at around 5500 to 7500
hours (which is mid-August to early-November). Below, the ACF-1
indicator with a 240 hour (ten day) window is plotted fro each year (in
corresponding colours). Below this is the mean variance. To obtain this
we have used a sliding window of 28 days (672 hours); in each time
window the variance of each of the 16 ACF signals is taken; we then take
the mean of these 16 variances to get the mean variance. The plot shows
a clear rise in the variance between 4000 and 7000 hours (mid-June to
mid-October). Figure [1](#16_years)
 (bottom) shows the mean mean, that is, we have
used to same process as described above but taken the mean instead of
the variance. As can be clearly seen, the mean drops during the 4-month
period that the variance rises.\
We can conclude, therefore, that in general, over these 16 years, the
ACF indicator is *lower* during the 'hurricane season', and has greater
variance. There are two possibilities I would like to address:

1.  The pressure signal is noisier during the June-October period (hence
    the lower mean ACF) but the ACF signal has frequent spikes which
    predicate hurricanes, or 'tipping points in the system', (hence the
    higher variance in the ACF).

2.  The ACF signal, during this period, is at pretty much the same level
    as the rest of the year but has frequent valleys (rather then being
    lower and having spikes).

Option 1 is what I vaguely expected based on the other systems that have
been analysed in this way and that I have read about. Option 2 is what
is suggested by an inspection of Figure
[1](#16_years). Note that the
mean ACF drops during this period but *not very much*: it is being
dragged down by a few valleys in the ACF signal.\
Because this is all quite confusing, I have repeated the analysis from
Figure [1](#16_years) but
using only the years 1992, 1999, 2004 and 2005: these are the years in
which we find the five *significant* hurricanes which were inspected in
the previous notes. This is shown in Figure
[2](#5_years), as we can see,
it's pretty much the same story.\

![16 years](../images/Var_many_years.png)

![Years 1992, 1999, 2004 and
2005](../images/Var_five_years.png)
