# Last meeting

Meeting with Valeria and Tobias in Reading, 11th December 2017.

- We have discussed the hurricane model in (holland1980), probably it
  is possible to adapt this model to what we want - a model of the sea
  level pressure at a fixed point in the vicinity of a hurricane,
  changing over time as the hurricane approaches.

- When designing a model, we should play with the parameters (including
  adding noise) until the PS-, ACF- and DFA-indicators behave
  realistically. Maybe this will give an insight into why some
  hurricanes show a strong increasing PS-indicator and others do not at
  all (although in the mean over all hurricanes, there is an increase).

- Also, we want to move to look at the EOF components of gridded data -
  i.e. to reduce the dimension of gridded data. Maybe it will be nice to
  see an EWS in this, the same as we can see with the weather station
  data.

- Also, having sourced some gridded data, maybe from ECMWF, we can
  attempt to triangulate the trajectory of a hurricane be observing the
  strength of the EWS in two or three different locations nearby. Maybe
  this will also involve EOF.

- I have already experimented trying to see an EWS from two variables.
  In the case of wind speed + pressure there was no noticable benefit
  over just using pressure. I should write this up -with plots.

# Work since

See work in the file `4_holland80model.pdf` which changes the attention
of the model in (holland1980) so that we model a cyclone at a distance
$d$ from a fixed point, rather than the profile of the cyclone at a
fixed point in time. There are many unknowns. Discussed over skype:
should play with the model until the ACF(1), PS (etc.) signatures look
similar to data. This will **allow us to investigate which parts of the
model (/physical system) are important**.

Making a model will also be useful for the purpose of **providing model
data on which to test methods**. Is this tautology since we have tuned
the model based on the results of these same methods (ACF etc.)?

Also, have but together some different work into the file
`2_extensionmultivariate.pdf`, because of thinking about thesis
chapters.

## strange method for multivariable systems

Finally, since New Year I have looked again at the paper
(williamson2015) where the method for studying a coupled system is
explained. The method is easy to follow: For data $\{x_t\}$ we find the
matrices $$
B = \mathbb{E}(x_{t+1}x_t^\top) - \mu \mu^\top ~~\text{and}~~ \Sigma = \mathbb{E}(x_{t}x_t^\top) - \mu \mu^\top
$$ where $\mu$ is the mean of the data. They are a bit
loose with things like "mean" and "$\mathbb{E}(X)$". Then we get the
matrix $A = B\Sigma^\top$, which can be decomposed
$A = U^{-1}\tilde{A}U$, where
$\tilde{A}=\text{diag}(\tilde{a_1}, \tilde{a_2}...)$ and each
$\tilde{a_j}$ is typically complex and we say
$\tilde{a_j} = |a_j|\exp(i\phi_j)$. But we are mainly interested in the
decay rate which is apparently given by the Jacobian of the system
equation evaluated at the saddle point. The eigenvalues $\lambda_j$ of
this Jacobian are given by
$\lambda_j = \frac{1}{\Delta t}\log(\tilde{a}_j)$, so we can separately
plot the real and imaginary parts.

Now, the problem comes in Matlab, I get different results to the paper,
especially with the \"homoclinic bifurcation\" example. My matrix $A$
has real eigenvalues, apparently the bifurcation is predicted by a
change in the imaginary part, so this is no good.
