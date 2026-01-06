# Valerie's Email - ACF Indicators Feedback

Regarding the ACF-indicators. The values are fluctuating at high level (0.95-99), which may mean that weather noise is dominating the signal. Held & Kleinen (GRL 2004), for example, applied aggregation to their data to reduce the influence of weather noise on the dynamics of the ACF-indicator. Can you test if in your case this could help? Just write a short test script that sums up values of the pressure data in windows of, let's say, 5 points, and see if this shows a better signal in the ACF-indicator in Fig.1b? I have a feeling that the current top curves of ACF-indicator may noticeably improve in terms of increasing trend.

I think you could plot your figures 1-3 as average curve with grey area of error-bars, which would make you less depressed about the results you have obtained. I can see that there is a signal of rising memory, indeed.

I agree that this effect of rising memory before a hurricane event should be incorporated in the model. Have you tried generating noise with various scaling exponents by transforming white noise in the Fourier domain? You will need a function that could generate a prescribed red noise, so that you could use it for building the model.
