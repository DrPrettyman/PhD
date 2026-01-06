# Ridge Regression

Valerie has sent a chapter on Ridge Regression and suggested that this
may be useful when dealing with observed variables with a strong linear
near-dependence, as is the case with for example windspeed and slp:
since they are physically connected, using both does not particularly
add anything (over using just one of these). Therefore it is pointless
to utilise the multi-dimensional degenerate fingerprinting approach.\
I have read the chapter, but still don't understand how to use this.
Will **insert more comment here**.

# Using weather station Data

I have received the HadISD data from the metoffice, this is raw (hourly)
data from weather stations around the world. In particular, look at the
southern tip of Florida, where Hurricane Katrina passed through in 2005.
Figure [1](#mapFlorida)
shows the locations of the six stations closest to the path of the
hurricane (in red).\
The HadISD data contains many missing points, therefore linear
interpolation has been used to map the time series data onto an hourly
scale.\
The slp data from these six stations is shown over the four month 2005
hurricane season in fig [2](#sixstations)
. Notice the four large dips in pressure which
are related to the occurrences of hurricanes Emily, Katrina, Rita and
Wilma resp.. The first EOF score of these six time series is shown in
fig [3](#F-pca) around the time
of Katrina (25th-August) along with the ACF-1 indicator. We can see an
increase in lag-1 autocorrelation just before the hurricane event,
although there is a similar increase at around the 25th-July, when there
is no large change in the slp. The ACF-1 value at the start of figure
[3](#F-pca) is very high, this
is a left-over effect from Hurricane Emily at the start of July. Figure
[4](#F-pca-long) shows the
same thing over the entire season, but with a shorter window length -for
the sliding-ACF calculation- of five days. The reason for this is the
Hurricanes Rita and Wilma which happen, together with Katrina, very
close together and somewhat complicate the whole thing. It is impossible
to tell whether the autocorrelation is 'increasing' because it doesn't
have time to settle down, so to speak, between events. With a shorter
window size there is better opportunity for this, although a smaller
window size also means more fluctuations in the autocorrelation.

![Map showing locations of six weather stations in south Florida, and
the path of hurricane Katrina (red) which passed from east to
west](../images/mapflorida.png)

![The raw slp data from the six stations plotted in fig
[1](#mapFlorida). Notice
the four large dips in pressure which are related to the occurrences of
hurricanes Emily, Katrina, Rita and Wilma
resp..](../images/florida_sixstations.png)

![The first EOF score calculated from the {interpolated versions of the}
six time series in fig [2](#sixstations)
. Also shown is the sliding-window ACF-1
coefficient, with a window size of 240 points (ten
days).](../images/florida_pca.png)

![The first EOF score and ACF-1 indicator, shown over the whole 2005
hurricane season. ACF-1 with a window size of 120 points (five
days).](../images/florida_pca_long.png)
