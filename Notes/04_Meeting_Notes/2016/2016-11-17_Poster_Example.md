I made a poster with an example dynamical system described by the
equation:

$$
\dot{z}(t) & = -\frac{\partial}{\partial z}(z^4 + \left(3-\frac{t}{200}\right)z^2) + \sigma\frac{dW(t)}{dt}

$$

which starts as a single well potential system and then bifurcates
gradually to for a double well potential. The bifurcation occurs at
$t=600$, when the $z^2$ term of the potential function is zero.

I think I should try to compute the theorectical ACF-1, DFA and Scaling
Exponent. The ACF-1 will be easiest, DFA is probably impossible. Scaling
Exponent will involve the Fourier transform.\
Here is a rubbish attempt at one particular system. Maybe it's possible
to do it for the general case.\
$$
\dot{z}(t) & = -\frac{\partial}{\partial z}(z^4 + \left(3-\frac{t}{200}\right)z^2) + \eta_t\\
& = -(4z^3 + \left(6-\frac{t}{100}\right)z) + \frac{dW(t)}{dt}

$$

$$
z(t) & = \left(\frac{1}{200}t^2 - 6t\right) z - 4tz^3 + W(t)
$$

$$
z^3 + \left(\frac{200+400t-t^2}{800t}\right)z - W(t) = 0
$$
