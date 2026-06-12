# Correlated Inputs in Monte Carlo — An Advanced Case
## When your uncertainties are not independent, and what to do about it

Most Monte Carlo simulations you will run in this course draw each uncertain input independently — and that assumption is correct for most of the experiments you will encounter in E2.

This reading is for the cases where it is not.

---

**This reading is an advanced topic and is beyond the scope of the standard E2 workflow.** Most groups in ASEN 3501 have input uncertainties that are genuinely independent — each sensor was calibrated separately, each material property was measured from a different source, each environmental factor varies for different reasons. If that describes your experiment, you do not need the material in this reading. Standard Monte Carlo, with independent draws for each input, gives you the correct result.

Read this if, and only if, two or more of your input uncertainties come from the same source. The most common cases: two sensor outputs that were both derived from the same calibration procedure, or two model parameters that were both estimated from the same batch of material tests. In those situations, the uncertainties on the two inputs are not independent: when one is higher than its nominal value, the other tends to be too. Sampling them independently ignores that structure. The result is a Monte Carlo distribution that is too narrow: it includes combinations (input A high, input B low simultaneously) that are physically improbable, and those combinations dilute the worst-case tail of the output distribution.

![A two-by-two grid of scatter plots showing two-dimensional input distributions. Top left: "Independent inputs — circular cloud." Points form a roughly circular cluster centered at the origin, with no preferred direction. Top right: "Positively correlated inputs — elongated ellipse." Points form a diagonal ellipse tilted at roughly 45 degrees, indicating that when Variable 1 is above average, Variable 2 tends to be above average as well. Bottom left: "Negatively correlated inputs — elongated ellipse, opposite tilt." Ellipse tilted at negative 45 degrees. Bottom right: "Independent sampling of correlated inputs — incorrect circular cloud imposed on the true ellipse." The circular cloud is overlaid on the true ellipse outline to show how independent sampling underrepresents the high-high and low-low corners where the actual worst-case combinations live. Each panel has axis labels "Variable 1" and "Variable 2" and a brief caption describing the implication. Clean, black-and-white engineering diagram style.](../images/E2_W9_R2_image1.png)

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

**The Takeaway:** Correlated inputs require correlated sampling, and the Cholesky decomposition is the standard mechanism for generating that structure in MATLAB. For most E2 experiments, independent sampling is appropriate and correct. If you have reason to believe two of your inputs are correlated — and you can quantify the correlation — apply this approach, document the correlation coefficient, and verify that the resulting output distribution is wider than the independent-sampling result in the direction of the correlated worst case.
