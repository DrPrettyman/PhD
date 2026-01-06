# Having a look at all the data

So now we have 18 tropical cyclones, or maybe a few fewer than that
since some of them have not such a strong signal. If we have a look at
all of them and the statistics ACF-1, DFA and the scaling exponent of
the power spectrum. It doesn't seem that the ACF indicator is very
informative. Measuring "rise" in a couple of different ways, we see that
about 10 of the signals have a rising ACF-1 indicator and 10 have a
falling. So it's fairly mixed.

1.  One way to say if it rises or falls is to have a look,

2.  another is to do a linear fit and get the slope of the line.

3.  Yet another is to approximate the ACF-1 signal as a step function,
    which jumps at the point of the largest or steepest jump in the
    signal, then it is a question of whether the step function is an
    up-step or down-step.

And when I say ten rise and ten fall, in fact to the naked eye it seems
that many do not do either, but an analytical method may pick up on a
very small positive or negative slope. The figure (Fig.
[1](#ACF_all20)) shows the
fairly random nature of this statistic in this case. There is a downward
trend at the very end which mirrors the trend in the slp signal, this is
because of the change in the nature of the signal at this point and
tells us nothing new.\
When I look at the colour of the signal, which means I say that the
signal is noise and what colour is the noise, I see similar. We can also
smooth the signal using a Gauss smoother and subtract this from the raw
signal, to get 'just the noise' as I think I probably can't say but I
have said anyway. In this case the colour of the noise rises in some and
falls in others also.\
The noise colour, unlike the ACF-1 which is a bit random, does seem more
uniformly *rising*, that is, it rises more often then not and the mean
off all the noise-colour signals shows a bit of an upward trend. At
least it is not completely flat. Therefore **it may be a good idea for a
model to include noise which changes colour as time progresses**.

![All 20 storms sea-level pressure (left) and ACF-1 indicator (right).
The maroon line shows the mean of all the slp signals (left) and the
mean of all the ACF-1 signals (right). The black dashed line shows the
ACF-1 indicator *of* the mean of all the slp
signals.](../images/ACF_all20storms.png)

![All 20 storms sea-level pressure (left) and DFA propagator (right).
The maroon line shows the mean of all the slp signals (left) and the
mean of all the DFA signals (right). The black dashed line shows the DFA
propagator *of* the mean of all the slp
signals.](../images/DFA_all20storms.png)

![All 20 storms sea-level pressure (left) and the power spectrum scaling
exponent (right). The maroon and black dashed lines are similar to in
figures [1](#ACF_all20) and
[2](#DFA_all20). Unlike the
other two figures, there appears to be a pattern here. The Scaling
Exponent appears to rise, in general, over
time.](../images/SEX_all20storms.png)
