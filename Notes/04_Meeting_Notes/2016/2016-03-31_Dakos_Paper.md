# (dakos2008)

## potential of ACF technique

In (dakos2008) real climate data is studied for signs of **slowing
down** as indicated by a change in **auto-correlation**. Which is what
I've already been doing. The paper concludes that:

> "our techniques might in principle be used to construct
> **operational** early warning systems for critical transitions in a
> wider range of complex systems where tipping points are suspected to
> exist, ranging from disease dynamics and physiology to **social and
> ecological systems**."

So they clearly see a very broad potential.\

## using a smoothing filter

The technique used in (dakos2008) differs from that in some other
papers by using a **Gaussian Kernel function** to smooth the data, then
subtract this from the raw data, effectively removing long-time trends.
This is similar to the **detrending** step in implementations of the
**DFA** technique.\

![The top plot is the first EOF (blue) and its smoothing function (red).
The bottom plot is the sliding ACF-1 of the data (blue) and the same of
the filtered data, i.e. the data minus the smoothing function
(red)](../images/Smoothing_Katrina.png)

In figure [1](#smooth_K) we
have used the Gaussian kernel with bandwidth 1,

$$
K(x^*, x_i) = \exp\left(\frac{-(x^*-x_i)^2}{2b^2}\right), ~~~~~~~~ b=1,
$$

to smooth the data $\{Y(X_i)\}$ to obtain $\hat{Y}$, according to

$$
\hat{Y}(x) = \frac{\sum_{i=1}^N K(x, X_i)Y(X_i) }{\sum_{i=1}^N K(x, X_i)}
$$

where the $X_i$ are the points where the observations are given (points
in time in this case) and the $Y(X_i)$ are the values of the
observations at the points $X_i$. The red line in the bottom plot shows
the sliding ACF indicator applied to the filtered or "detrended" data
(smoothing subtracted). It appears that the technique applied to the
filtered data gives an indicator which rises later and not as much,
which is not what we want. With a greater bandwidth (thus the smoothing
function is less well fitted to the data) the ACF is higher but still
rises later than without the filtering. See figure
[2](#DBW_K).

![The ACF-1 propagator of the Katrina data filtered using different
bandwidths $b$.](../images/DifferentBandwidths_K.png){#DBW_K


![The top plot is the first EOF (blue) and its smoothing function (red).
The bottom plot is the sliding ACF-1 of the data (blue) and the same of
the filtered data, i.e. the data minus the smoothing function (red).
This uses a bandwidth of
$1.5$.](../images/Smoothing_Isabel.png)

# A different Hurricane

Having a look at Hurricane Isabel in September 2003. figure
[3](#smooth_I) shows the same
as figure [1](#smooth_K)
applied to this different storm. The rise in ACF is much less pronounced
here, but this is possibly because of a bad choice of **geographical
area**, it may be that looking at an area to the west would have been
better, since the storm may have been stronger. There is clearly more
variability in the mslp before the large drop in pressure (on
11/12-Sept) than there is in the 2005 (Katrina) data.
