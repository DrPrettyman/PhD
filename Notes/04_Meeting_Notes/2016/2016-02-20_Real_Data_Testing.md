# Testing on (almost) real data


![](../images/katrinatrack.png)
Showing the path of hurricane Katrina from 23/08/2005 to
30/08/2005 (red).


Here we have used data from the ECMWF ERA_20c reanalysis dataset. The
data is 3-hourly from 12/07/2005 to 15/09/2005 in a 'square' region from
22.5 to 27.5 degrees north and 89.5 to 84.5 degrees east. The square
region is shown as a black outline in figure
[1](#katrinatrack) and
the path of hurricane Katrina from 23/08/2005 to 30/08/2005 is shown in
red. The Hurricane entered the right-hand edge of the region at 3pm on
the 27th of August and exited the top edge at 3am on the 29th of
August.\
The data is on a 0.5 degree grid, giving a grid of $11\times 11$ points
over the $5'$ by $5'$ region. All these 121 points are considered as
variables giving 121 separate time series. Principle Component Analysis
(PCA) is performed on the 121 series and the first PCA score is
considered to capture the behaviour of the entire region. This PCA is
done for mean sea-level pressure (mslp) and wind-speed (ws) so that we
have two time series: the first PCA score for mslp and the first PCA
score for ws. These two time series are taken to represent a 2D
dynamical system where these are the two variables.\
Using this 2D dynamical system we then use the method described in
(williamson2015) to parametrise the system as a linear system with
added noise by estimating the value of the matrix $A$. This is done in a
sliding window of 150 points and the first eigenvalue of $A$ is shown in
figure [2](#katrina_eigenvals)
 (imaginary part shown in the top plot and
real part shown in the bottom plot).\
It is clear when the hurricane occurs! The pressure drops suddenly and
the wind speed rises also. It is not obvious that the hurricane is
*about* to happen though. Immediately before the sudden drop the
pressure (red line) drops slightly, then rises very slightly, and this
could easily be natural variability. The wind speed drops slightly
before the sudden rise, but this is also in line with the previous
variability. However, the eigenvalues - both the real part which
increases and the imaginary part which becomes non-zero - appear to
predicate the hurricane's arrival. The maroon dashed line in fig
[2](#katrina_eigenvals)
 marks the point where the imaginary part
becomes non-zero (at 9pm, 23-Aug), at the same time the real part
reaches a peak at $\sim 0.9$, although is starts rising a short while
before this (maybe 6 or 9 hours before). It happens that 23-Aug-9pm is
the exact time that "Tropical Storm" Katrina first formed approximately
10 degrees to the east of the eastern edge of the square region we
consider (The beginning of the red line in fig
[1](#katrinatrack)).\

![Showing the first Eigenvalue of the matrix $A$ estimated using the
method from (williamson2015), using the first PCA scores of the mslp
and the wind speed over the region as the input, giving a 2D dynamical
system in these two variables. Showing the imaginary part (top) and the
real part (bottom) of $A$ separately. Both are shown with first PCA
scores of the (unitless) mslp and wind
speed.](../images/eigenvalue_katrina_grace.png){#katrina_eigenvals
width="5.6in"}

# next steps

I have also looked at different parts of this region, which I will write
up. I have also looked at the paper (gao et al) that Valerie sent and
will look at some of these ideas. I wonder if this method is any
different from studying the lag-1 autocorrelation of these two 1D
systems (first PCA score of mslp and first PCA score of ws) and
considering both together? Something to investigate. Also, it could be a
more sophisticated method then just looking at the lag-1, maybe like
DFA.
