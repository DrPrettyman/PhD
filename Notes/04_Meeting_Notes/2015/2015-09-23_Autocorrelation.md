# 1

I have looked at the lag-1 autocorrelation of a time series.


![](../../images/decresing_noise.png)





![](../../images/lag1.png)



Figure [1](#series) shows a
series produced by the system $$
\dot{z}(t) & = -(z^4 - 2z^2)' + \sigma(t)\eta \\
\sigma(t) & = -0.00007t+1.50045
$$ Figure [2](#auto_correlation)
 shows the lag-1 autocorrelation (AC) of
the series in a sliding window of length $5000$. The AC increases
towards $1$ as the series spends more time in each state, until the
point just after $t=10^4$ when the series spends all the time in just
one state. At this point the AC drops to a value of $0$.

# 2

I have also tried to reproduce Figure 3 (b) in Valerie's paper *Changing
climate states and stability: from Pliocene to present, 2011*, which is
shown in Figure [3](#Figure3b)
. The figure is stated to be produced by the system
$$
\dot{z}(t) & = -(z^4 - 2z^2)' + F(t) + \sigma\eta \\
F(t) & = (5\times 10^{-9}) t^2
$$ In the paper it says "a deterministic forcing with a
parabolic trend varying from 0 to 2 is added to the dynamical equation,
driving the mean value of the time series." but what is shown in Figure
[3](#Figure3b) is the
parabolic trend $F(t)$ added to the time series, not added to the
dynamical equation. The system given by the equation changes from a
double-well to a single well potential at the point when
$$F(t) > \min_{z\in [-1,0]}\left\{-(z^4 - 2z^2)'\right\} = \frac{1}{\sqrt{3}},$$
that is, $t \geq 10746$. An example series has been produced in Figure
[4](#forcing). At $t=0$,
$F(t)\approx 0$ the stable positions of the system are at
$z\in \{-1,0,1\}$ which is the solution to $-(z^4 - 2z^2)'=0$. When
$F(t)=2$ the (single) stable position is at $z=1.19$ which is the
solution to $-(z^4 - 2z^2)'+2=0$. So the time series does not show the
dramatic parabolic trend shown in Figure
[3](#Figure3b), but rather
the stable position at $z=1$ increases to $z=1.19$.\
Or maybe I have completely failed to see something here, please let me
know.


![](../../images/Figure3b.png)




![](../../images/deterministic_forcing.png)




# 3

I'm not sure what to do now. I've had a look at the other system (with
the forcing) to look at the autocorrelation, but I'm not sure how useful
that is. Clearly the autocorrelation approaching 1 is an indicator of a
change (as in Figure [2](#auto_correlation)
, so it's good that I appreciate that.\
I have also been attempting to figure out how the power spectrum relates
to anything. We said that we should look at the fourier transform of the
autocorrelation. Does this mean to do a FFT on the data in Figure
[2](#auto_correlation)
? There does not appear to be any frequency
patterns in that data. Maybe with other data produced by other systems
(or maybe real data).\
I feel like it is good to be at the messing-around stage, but I would
like some hints on what to mess around with next. Obviously I have not
done very much work recently; I don't want to bugger off to the library
all day yet and leave Amber with the 5-day-old, so I'm working at home,
which is quite distracting. As I say, it would be good to have some
advice about what to do next, and to have some closure on Figures 3a and
3b in *Changing climate states and stability: from Pliocene to present,
2011*.
