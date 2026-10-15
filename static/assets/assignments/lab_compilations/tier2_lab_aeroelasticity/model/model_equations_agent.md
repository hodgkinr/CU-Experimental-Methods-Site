# Aeroelasticity Tier 2: Measurement Model and Coefficient Derivation

Use this reference with the [Aero procedure](../procedure/procedure_agent.md), designated provisional sensor scenario, student data dictionary, connected-port map, and supplied reference data. The equations below follow the pressure-integration method used in the instructor implementation. The sensor scenario supports the calculation; it does not verify installed hardware identities.

## 1. Measurement system and airspeed model

The Pitot-static system measures dynamic pressure, the difference between stagnation pressure and freestream static pressure:

$$
q=p_0-p_\infty.
$$

Here, $q$ is dynamic pressure in pascals (Pa), $p_0$ is stagnation pressure in Pa, and $p_\infty$ is freestream static pressure in Pa. Atmospheric pressure $p$ and absolute temperature $T$ determine low-speed air density $\rho$:

$$
\rho=\frac{p}{R_{air}T},\qquad
V=\sqrt{\frac{2q}{\rho}}=\sqrt{\frac{2qR_{air}T}{p}},\qquad
R_{air}=287.05\;\mathrm{J/(kg\,K)}.
$$

In these equations, $p$ is absolute atmospheric pressure in Pa, $T$ is absolute temperature in kelvins (K), $\rho$ is density in kg/m$^3$, $V$ is derived freestream speed in m/s, and $R_{air}$ is the specific gas constant for air. In this low-speed model, the atmospheric pressure $p$ is the freestream static pressure $p_\infty$.

Use measured $q,p,T$ once as the primitive airspeed inputs. Logged airspeed and density calculated from these inputs are derived values, not additional independent measurements. The Scanivalve measures airfoil surface pressure; it does not enter this Pitot-static airspeed model.

## 2. Airspeed uncertainty propagation

For independent primitive inputs, the first-order Taylor sensitivities are:

$$
\frac{\partial V}{\partial q}=\frac{V}{2q},\qquad
\frac{\partial V}{\partial p}=-\frac{V}{2p},\qquad
\frac{\partial V}{\partial T}=\frac{V}{2T}.
$$

Each sensitivity says how much the calculated speed changes per unit change in one input near its nominal value. For example, $(\partial V/\partial q)u_q$ is the speed uncertainty contribution from dynamic pressure. The sensitivities have units of (m/s)/Pa for $q$ and $p$, and (m/s)/K for $T$. Combining independent contributions by root-sum-square gives the absolute standard uncertainty:

$$
u_V=
\sqrt{
\left(\frac{V}{2q}u_q\right)^2+
\left(\frac{V}{2p}u_p\right)^2+
\left(\frac{V}{2T}u_T\right)^2
}.
$$

Dividing by nominal speed gives normalized standard uncertainty:

$$
\frac{u_V}{V}
=\frac{1}{2}
\sqrt{
\left(\frac{u_q}{q}\right)^2+
\left(\frac{u_p}{p}\right)^2+
\left(\frac{u_T}{T}\right)^2
}.
$$

Here $u_q$ and $u_p$ are standard uncertainties in Pa, $u_T$ is in K, and $u_V$ is in m/s. Absolute uncertainty describes the expected speed error in m/s; normalized uncertainty is dimensionless and is often reported as a percentage. These expressions are not evaluated at exactly $V=0$.

For the designated calculation scenario, treat each stated plus/minus bound $a$ as an independent rectangular distribution from $-a$ to $+a$. Its standard uncertainty is $u=a/\sqrt{3}$. Independence is a model assumption, not a demonstrated property of the installed instruments. The DSA3217 surface-pressure scanner is separate from the $q,p,T$ airspeed chain. The confirmed tunnel maximum is 60 m/s; the confirmed scanner configuration is ±10 inH$_2$O. Candidate Pitot, atmospheric-pressure, and temperature sensor identities remain provisional.

## 3. Pressure forces on a two-dimensional airfoil

Pressure pushes normal to a surface. To obtain the aerodynamic force per unit span on a two-dimensional airfoil, add the pressure-force contributions over its complete closed contour. The sign of a contribution depends on the surface direction and the pressure difference across it.

Use chordwise coordinate $x$ positive from leading edge to trailing edge and thickness coordinate $y$ positive upward. Traverse the contour clockwise: along the upper surface from leading edge to trailing edge, then along the lower surface back toward the leading edge, and finally across the small leading-edge closing segment. The airfoil interior stays to the right of the direction of travel. Define axial force as positive in the $+x$ direction and normal force as positive in the $+y$ direction.

For tap or contour point $i$:

- $p_i$ is the local airfoil surface pressure in Pa.
- $p_\infty$ is freestream static pressure in Pa.
- $\Delta p_i=p_i-p_\infty$ is the local pressure difference in Pa.
- $(x_i,y_i)$ is the point coordinate. Coordinates may be in inches or metres, but use one consistent unit system within each calculation.
- $c$ is airfoil chord length in the same length units as the coordinates.
- $\Delta s_i$ is the length of the straight surface element from point $i$ to point $i+1$.
- $\Delta x_i=x_{i+1}-x_i$ and $\Delta y_i=y_{i+1}-y_i$ are signed coordinate changes.
- $\theta_i$ is the signed angle measured counterclockwise from the positive $x$ axis to the directed segment from point $i$ to point $i+1$.
- $F_a'$ and $F_n'$ are axial and normal forces per unit span, respectively, in N/m.

The average pressure difference on element $i$ is $\overline{\Delta p}_i=(\Delta p_i+\Delta p_{i+1})/2$. 

## 4. Elemental force derivation

The tangent segment follows the contour from point $i$ to point $i+1$. With the angle convention above:

$$
\cos\theta_i=\frac{\Delta x_i}{\Delta s_i},\qquad
\sin\theta_i=\frac{\Delta y_i}{\Delta s_i}.
$$

Because the contour is clockwise, the inward unit normal is the right-hand normal to the tangent:

$$
\hat{\mathbf n}_{in,i}
=\sin\theta_i\,\hat{\mathbf x}
-\cos\theta_i\,\hat{\mathbf y}.
$$

For a straight element, approximate the pressure difference as its endpoint average. Pressure force per unit span equals pressure difference times element length, directed inward:

$$
\Delta\mathbf F'_{p,i}
=\overline{\Delta p}_i\,\Delta s_i\,\hat{\mathbf n}_{in,i}.
$$

Project onto the positive axial and normal axes:

$$
\Delta F'_{a,i}
=\overline{\Delta p}_i\,\Delta s_i\sin\theta_i
=\overline{\Delta p}_i\,\Delta y_i,
$$

$$
\Delta F'_{n,i}
=-\overline{\Delta p}_i\,\Delta s_i\cos\theta_i
=-\overline{\Delta p}_i\,\Delta x_i.
$$

The segment length and angle cancel because $\Delta s_i\sin\theta_i=\Delta y_i$ and $\Delta s_i\cos\theta_i=\Delta x_i$. The implementation therefore needs the endpoint coordinates, not a separately calculated segment angle. Each force contribution has units Pa·m = N/m.

## 5. Sum forces and nondimensionalize

Sum the elemental contributions around the entire closed contour before forming coefficients:

$$
F'_a=\sum_i\overline{\Delta p}_i\,\Delta y_i,\qquad
F'_n=-\sum_i\overline{\Delta p}_i\,\Delta x_i.
$$

Completing the contour matters. A constant freestream pressure acting around a closed contour contributes no net force because the signed coordinate changes sum to zero:

$$
\sum_i\Delta x_i=0,\qquad \sum_i\Delta y_i=0.
$$

Thus the constant $p_\infty$ terms cancel, and the measured surface-to-freestream differences $\Delta p_i$ can be used. Disconnected ports are not measurements: do not invent values for them or include them as tap locations.

The freestream dynamic pressure is

$$
q_\infty=\frac{1}{2}\rho_\infty V_\infty^2,
$$

where $\rho_\infty$ is freestream density in kg/m$^3$ and $V_\infty$ is freestream speed in m/s. Define the pressure coefficient at point $i$ as

$$
C_{p,i}=\frac{p_i-p_\infty}{q_\infty}
=\frac{\Delta p_i}{q_\infty}.
$$

The sectional normal and axial coefficients are force per unit span divided by $q_\infty c$:

$$
C_n=\frac{F'_n}{q_\infty c},\qquad
C_a=\frac{F'_a}{q_\infty c}.
$$

This denominator has units Pa·m = N/m, so the coefficients are dimensionless. Substituting the force sums and using $\overline{C}_{p,i}=(C_{p,i}+C_{p,i+1})/2$ gives the discrete trapezoidal-rule equations:

$$
C_n=-\sum_i\frac{C_{p,i}+C_{p,i+1}}{2}\frac{\Delta x_i}{c},
$$

$$
C_a=+\sum_i\frac{C_{p,i}+C_{p,i+1}}{2}\frac{\Delta y_i}{c}.
$$

In the limit of closely spaced elements, these sums are the corresponding closed-contour integrals:

$$
C_n=-\oint C_p\,\frac{dx}{c},\qquad
C_a=+\oint C_p\,\frac{dy}{c}.
$$

These are two-dimensional sectional coefficients based on force per unit span. They are not finite-wing planform lift or drag coefficients.

## 6. Rotate normal and axial into lift and drag

$C_n$ and $C_a$ are referenced to the airfoil chord axes. Lift and drag are referenced to the freestream axes. Let $\alpha$ be angle of attack: the angle between the chord reference and freestream direction, using the course data's sign convention. Project the chord-axis force components onto the freestream lift and drag axes:

$$
C_l=C_n\cos\alpha-C_a\sin\alpha,
$$

$$
C_d=C_n\sin\alpha+C_a\cos\alpha.
$$

The normal-force contribution projects mostly into lift, while its projection into drag grows with angle of attack. The axial-force contribution projects mostly into drag and subtracts from lift for positive $\alpha$ under this convention. MATLAB's sin and cos functions expect radians; convert measured degrees with deg2rad, or use the degree-specific sind and cosd functions.

## 7. Apply the derivation to the Tier 2 pressure taps

Use the complete connected-port coordinates and ordering in the [Aero procedure](../procedure/procedure_agent.md); this document does not define a competing geometry map. In that map, channels 1–9 follow the upper surface from the leading edge toward the trailing edge (ports 1–8 and 10). Channels 10–16 follow the lower surface back toward the leading edge (ports 12, 14, 16, 17, 18, 19, and 20). Channel numbers and physical port numbers are not interchangeable.

Ports 9, 13, and 15 are disconnected and provide no measured pressures. Port 11 is the theoretical trailing-edge point at $(x_{TE},y_{TE})=(3.5\text{ in},0)$, not a measured channel. The upper contour goes from channel 9 to this theoretical trailing-edge point; the lower contour returns from it through channel 10 and the remaining lower taps. After the last connected lower tap, port 20, close the contour with the specified straight segment to port 1.

### Trailing-edge pressure closure

Extrapolate each surface's pressure coefficient from its two nearest connected taps using the general two-point linear formula evaluated at $x_{TE}$:

$$
C_{p,TE}=C_{p,a}
+(C_{p,b}-C_{p,a})\frac{x_{TE}-x_a}{x_b-x_a}.
$$

For the upper surface, use channel 8 at port 8 ($x_a=2.1$ in) and channel 9 at port 10 ($x_b=2.8$ in). For the lower surface, order the points by increasing $x$: channel 11 at port 14 ($x_a=2.1$ in) and channel 10 at port 12 ($x_b=2.8$ in). In both cases, $x_{TE}=3.5$ in. The measured spacing is 0.7 in, and the trailing edge is one more 0.7 in step from the aft tap, so the extrapolation ratio is 2. Therefore the general formula simplifies to:

$$
C_{p,TE,u}=C_{p,8}+(C_{p,9}-C_{p,8})\frac{3.5-2.1}{2.8-2.1}
=2C_{p,9}-C_{p,8},
$$

$$
C_{p,TE,l}=C_{p,11}+(C_{p,10}-C_{p,11})\frac{3.5-2.1}{2.8-2.1}
=2C_{p,10}-C_{p,11}.
$$

Average the upper and lower extrapolations for the theoretical trailing-edge coefficient:

$$
C_{p,TE}=\frac{C_{p,TE,u}+C_{p,TE,l}}{2}.
$$

### Convert the measurements to pressure coefficients

For each selected angle, calculate:

$$
C_{p,i}=\frac{\Delta p_i}{q_\infty}.
$$

Here, $\Delta p_i$ is already the surface-to-freestream pressure difference. Do not subtract atmospheric pressure from these columns a second time. Use the measured Pitot dynamic pressure as $q_\infty$ for the corresponding angle group.

## 8. Coefficient uncertainty by Monte Carlo

For every measured angle of attack included in the final coefficient plots, use 10,000 trials and the designated provisional rectangular bounds. These bounds are propagation assumptions, not confirmed calibration values. For each trial:

1. Add one uniform perturbation from -49.8 Pa to +49.8 Pa to the measured Pitot dynamic pressure. Share this same perturbed $q$ across all 16 taps.
2. Independently add a uniform perturbation from -4.9818 Pa to +4.9818 Pa to each measured surface-pressure channel.
3. Add one uniform perturbation from -0.5° to +0.5° to the measured angle of attack.
4. Recalculate the pressure coefficients, trailing-edge closure, full-contour $C_n$ and $C_a$, and rotated $C_l$ and $C_d$.
5. Repeat for all 10,000 trials at that angle. Calculate the sample standard deviations $s_{C_l}$ and $s_{C_d}$.

Plot the sample standard deviations as ±1 combined-standard-uncertainty bars centered on the nominal measured coefficients. They are standard uncertainty bars, not 95% intervals. Independent channel errors are the provisional baseline because channel covariance has not been measured. Do not perturb atmospheric pressure, temperature, density, or derived airspeed again: the coefficient calculation uses measured $q$ as its denominator.

## 10. Reference comparison and limitations

Compare measured sectional $C_l(\alpha)$ and $C_d(\alpha)$ with the supplied Clark Y-14 reference data over its stated validity range. Evaluate agreement and disagreement; do not assume that agreement is required. Consider Reynolds-number and other condition differences, and distinguish coefficient uncertainty from model/reference discrepancy. The current historical pressure dataset is a single-speed sweep near 30.37 m/s, while the empirical NACA TR 628 reference is near $Re\approx3.02\times10^6$ and the measured sweep is near $Re\approx1.46\times10^5$. The comparison is limited to -8° through +12°. These data do not establish an aerodynamic response at other speeds or experimentally verify a recommended operating region.

Finite-wing planform coefficients, structural deflection, beam or spar calculations, and whiffle-tree analysis are outside this student task.
