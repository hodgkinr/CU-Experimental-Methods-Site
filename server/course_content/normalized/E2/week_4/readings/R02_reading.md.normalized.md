# Correlated Inputs in Monte Carlo — An Advanced Case
## When your uncertainties are not independent, and what to do about it

Most introductory Monte Carlo simulations begin with independent inputs, but independence is an assumption to inspect, not a fact supplied by the software.

This reading is for the cases where it is not.

---

**This reading is an advanced topic and is beyond the required E2 workflow.** In E2, your required task is to identify whether inputs might share a calibration reference, environment, data-reduction step, or instrument. You are not required to calculate covariance or implement correlated sampling unless evidence and an estimate are provided.

Read this if two or more input uncertainties come from the same source. The most common cases are sensor outputs derived from the same calibration procedure or parameters estimated from the same material tests. Sampling them independently ignores that structure. The effect on output uncertainty depends on the covariance sign and on the signs and magnitudes of the model sensitivities; it can widen or narrow the output distribution.

![A two-by-two grid of scatter plots showing two-dimensional input distributions. Top left: "Independent inputs — circular cloud." Points form a roughly circular cluster centered at the origin, with no preferred direction. Top right: "Positively correlated inputs — elongated ellipse." Points form a diagonal ellipse tilted at roughly 45 degrees, indicating that when Variable 1 is above average, Variable 2 tends to be above average as well. Bottom left: "Negatively correlated inputs — elongated ellipse, opposite tilt." Ellipse tilted at negative 45 degrees. Bottom right: "Independent sampling of correlated inputs — incorrect circular cloud imposed on the true ellipse." The circular cloud is overlaid on the true ellipse outline to show how independent sampling underrepresents the high-high and low-low corners where the actual worst-case combinations live. Each panel has axis labels "Variable 1" and "Variable 2" and a brief caption describing the implication. Clean, black-and-white engineering diagram style.](../images/E2_W9_R2_image1.png)
*Why this image is here:* It makes input correlation visible so you can see exactly what gets lost when a Monte Carlo model samples coupled variables as if they were independent.

---

The correction requires two pieces: a **correlation matrix** and a **Cholesky decomposition**.

The correlation matrix encodes the statistical relationships between your inputs. For two inputs with a correlation coefficient ρ, the matrix is simply [[1, ρ], [ρ, 1]]. A correlation of +1 means the two inputs move together perfectly; a correlation of 0 means they are independent; a correlation of −1 means when one is high, the other is low. You estimate ρ from the physical relationship between the two sources, or from the calibration records if both sensors were calibrated against the same reference artifact.

The **Cholesky decomposition** is the matrix equivalent of taking a square root. Applied to the correlation matrix, it produces a lower triangular matrix L such that L × Lᵀ = R. Multiplying a set of independent standard normal draws by L transforms them into draws with the correct correlated structure. In MATLAB:

```matlab
R = [1 0.7; 0.7 1]; % Correlation matrix (ρ = 0.7)
L = chol(R, 'lower'); % Cholesky decomposition
X = randn(N, 2) * L'; % N correlated sample pairs
```

The rows of X are sample pairs with the correct joint distribution: they form an elongated ellipse in two dimensions, not a circular cloud. Each row is then scaled by the appropriate standard uncertainty for each input before being passed into the model.

Geometrically, the Cholesky factor is the matrix that stretches and rotates the independent standard normal cloud into the correct correlated shape. It does not change the marginal distributions — each input still has its correct individual uncertainty — but it links the samples so that the joint behavior matches the physical relationship between the sources.

---

**The Takeaway:** First identify shared sources. Correlated sampling is an advanced option only when the dependence can be supported; its effect is not necessarily to widen the result because covariance sign and model sensitivities both matter.
