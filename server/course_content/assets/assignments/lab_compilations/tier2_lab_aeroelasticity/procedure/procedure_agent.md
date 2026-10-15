# Tier 2: Choose Useful Wind-Tunnel Conditions

## Purpose and sequence

Use uncertainty analysis **before testing** to decide which wind-tunnel conditions are likely to provide useful airspeed and airfoil-pressure measurements. Then use the released Clark Y-14 pressure data, estimate uncertainty in the aerodynamic coefficients, and interpret the results against the supplied reference.

The required sequence is:

**Airspeed measurement uncertainty → favorable-condition selection → airfoil pressure measurements → aerodynamic coefficients → coefficient uncertainty and model/data interpretation.**

The tunnel maximum is 60 m/s. This is the tunnel's operating capability, not the range of every sensor. Work only within approved test directions and released measurement limits.

## A. Measurement system and airspeed model

A Pitot-static system measures dynamic pressure, the difference between stagnation pressure and freestream static pressure:

$$
q=p_0-p_\infty.
$$

Here, $q$ is dynamic pressure in pascals (Pa), $p_0$ is stagnation pressure in Pa, and $p_\infty$ is freestream static pressure in Pa. Atmospheric pressure $p$ and absolute temperature $T$ determine low-speed air density $\rho$:

$$
\rho=\frac{p}{R_{air}T},\qquad
V=\sqrt{\frac{2q}{\rho}}=\sqrt{\frac{2qR_{air}T}{p}},\qquad
R_{air}=287.05\;\mathrm{J/(kg\,K)}.
$$

In these equations, $p$ is absolute atmospheric pressure in Pa, $T$ is in kelvins (K), $\rho$ is density in $kg/m^3$, $V$ is derived freestream speed in $m/s$, and $R_{air}$ is the specific gas constant for air. For this low-speed model, atmospheric pressure $p$ is the freestream static pressure $p_\infty$.

Use measured $q,p,T$ once as the primitive airspeed inputs. Logged airspeed and density calculated from these inputs are derived values, not additional independent measurements. The Scanivalve measures airfoil surface pressure; it does not enter this Pitot-static airspeed model.

The DSA3217 is confirmed in the ±10 inH₂O configuration. Keep this scanner range distinct from the tunnel's confirmed 60 m/s maximum and the candidate Pitot sensor range. 

## B. Airspeed uncertainty and condition selection

For independent primitive inputs, the first-order Taylor sensitivities of the speed model are:

$$
\frac{\partial V}{\partial q}=\frac{V}{2q},\qquad
\frac{\partial V}{\partial p}=-\frac{V}{2p},\qquad
\frac{\partial V}{\partial T}=\frac{V}{2T}.
$$

Each sensitivity describes the local change in calculated speed per unit change in one input. For example, $(\partial V/\partial q)u_q$ is the speed-uncertainty contribution from dynamic pressure. For independent inputs, combine their contributions by root-sum-square:

$$
u_V=\sqrt{\left(\frac{V}{2q}u_q\right)^2+
                 \left(\frac{V}{2p}u_p\right)^2+
                 \left(\frac{V}{2T}u_T\right)^2},\qquad
\frac{u_V}{V}=\frac12\sqrt{\left(\frac{u_q}{q}\right)^2+
                               \left(\frac{u_p}{p}\right)^2+
                               \left(\frac{u_T}{T}\right)^2}.
$$

Here, $u_q$ and $u_p$ are standard uncertainties in Pa, $u_T$ is in K, and $u_V$ is in m/s. Absolute uncertainty describes expected speed uncertainty in m/s; normalized uncertainty is dimensionless and is often reported as a percentage. The normalized contribution from input $i$ is its individual Taylor contribution divided by $V$. The Taylor expressions for $u_V$ and $u_V/V$ are undefined at exactly $V=0$; do not evaluate them there.

Treat each released plus/minus bound $a$ as a rectangular distribution from $-a$ to $+a$, so the standard uncertainty is $u=a/\sqrt{3}$. Independence is a modeling assumption, not a demonstrated property of the installed instruments. Use the instructor-designated temperature case if more than one candidate bound is listed.

For the full 0–60 m/s tunnel envelope, make these plots:

1. Combined normalized standard uncertainty $100u_V/V$ in percent versus speed. Plot relative uncertainty only at positive speeds.
2. Absolute standard uncertainty $u_V$ in m/s versus speed, evaluated only where the Taylor model is defined.
3. Individual normalized contributions $100u_{V,q}/V$, $100u_{V,p}/V$, and $100u_{V,T}/V$, together with the combined curve.

Explain the shapes and trends. Compare what the absolute and normalized plots say, identify dominant inputs, and distinguish the tunnel envelope from sensor-valid conditions. Show the sensor-range boundary and mark Taylor or other mathematical extrapolation beyond it. A result calculated outside an instrument's usable range is not a claim about achievable measurement accuracy. Check surface-pressure range separately when evaluating the airfoil data.

Use the plots and practical constraints to recommend favorable and unfavorable or unsupported regions. State your decision rule before applying it. A 3% threshold may be shown as an example only; it is not a universal engineering rule. Also consider whether the measurement signal and aerodynamic response would be useful.

### Limited Monte Carlo check of airspeed

Use the bounded-input Monte Carlo approach to check the Taylor model at three representative speeds: one low speed where the dynamic-pressure bound is large relative to nominal $q$, one midrange speed, and one high speed near or beyond the candidate Pitot limit. The instructor may specify a comparable compact set if operating or verified sensor information changes.

For each trial, draw $q,p,T$ independently from their released uniform bounds, recompute $V$, and calculate the sample standard deviation. About 10,000 trials per speed is sufficient for this check; report the draw count. Compare the Monte Carlo standard deviation with the Taylor value. Count and report nonphysical draws and flag sensor-overrange draws. Do not silently discard them or describe over-range results as realizable measurements. Explain why mathematically valid propagation can still be unusable when an instrument is out of range.

## C. Airfoil pressure measurements and force derivation

Use the approved student-accessible historical measurement file and data dictionary: 640 measured rows, 20 samples at each integer angle from −15° through +16°, at approximately 30.37 m/s. This is a **historical single-speed sweep**, not a newly measured multi-speed dataset.

The source file's 30 fields are: atmospheric temperature (K), atmospheric pressure (Pa), atmospheric density (kg/m³), logged airspeed (m/s), Pitot dynamic pressure (Pa), auxiliary dynamic pressure (Pa), actual voltage (V), angle of attack (deg), spanwise position (in), sting axial force (N), sting normal force (N), sting pitching moment (N·m), ELD probe x/y positions (mm), and Scanivalve pressure channels 1–16 (Pa). Use only columns designated by the approved dictionary. The reduction uses Pitot $q$ and surface pressures; auxiliary pressure and implausible sting loads are not used.

Pressure pushes normal to a surface. To find the aerodynamic force per unit span on a two-dimensional airfoil, add the pressure-force contributions around the complete closed contour. For each straight segment, the endpoint pressures are averaged to approximate the pressure along that segment. The sign of each contribution depends on the contour direction and the direction of the pressure difference across the surface.

Use $x$ positive from leading edge to trailing edge and $y$ positive upward. Traverse the contour clockwise: along the upper surface from leading edge to trailing edge, then along the lower surface back toward the leading edge, and finally across the leading-edge closing segment. The airfoil interior stays to the right of the direction of travel. Define axial force as positive in $+x$ and normal force as positive in $+y$.

For directed element $i$ from point $i$ to point $i+1$, let $\Delta x_i=x_{i+1}-x_i$, $\Delta y_i=y_{i+1}-y_i$, and $\Delta s_i$ be its length. Let $\theta_i$ be the signed angle measured counterclockwise from the positive $x$ axis to the segment. Then

$$
\cos\theta_i=\frac{\Delta x_i}{\Delta s_i},\qquad
\sin\theta_i=\frac{\Delta y_i}{\Delta s_i}.
$$

For this clockwise contour, the inward unit normal is the right-hand normal to the tangent:

$$
\hat{\mathbf n}_{in,i}=\sin\theta_i\,\hat{\mathbf x}-\cos\theta_i\,\hat{\mathbf y}.
$$

Let $p_i$ be local surface pressure, $p_\infty$ freestream static pressure, and $\Delta p_i=p_i-p_\infty$. The average pressure difference on an element is $\overline{\Delta p}_i=(\Delta p_i+\Delta p_{i+1})/2$. Pressure force per unit span equals pressure difference times element length and points inward:

$$
\Delta\mathbf F'_{p,i}=\overline{\Delta p}_i\,\Delta s_i\,\hat{\mathbf n}_{in,i}.
$$

Resolve this elemental force into axial and normal components. Using $\Delta s_i\sin\theta_i=\Delta y_i$ and $\Delta s_i\cos\theta_i=\Delta x_i$ gives

$$
\Delta F'_{a,i}=\overline{\Delta p}_i\,\Delta y_i,\qquad
\Delta F'_{n,i}=-\overline{\Delta p}_i\,\Delta x_i.
$$

The length and angle cancel, so the implementation needs signed coordinate changes rather than a separately calculated angle. A prime denotes force per unit span; each elemental term has units Pa·m = N/m when SI units are used.

Sum all elements around the closed contour before forming coefficients:

$$
F'_a=\sum_i\overline{\Delta p}_i\,\Delta y_i,\qquad
F'_n=-\sum_i\overline{\Delta p}_i\,\Delta x_i.
$$

Completing the contour matters. On a closed contour, $\sum_i\Delta x_i=0$ and $\sum_i\Delta y_i=0$, so a constant freestream pressure contributes no net force. Thus the measured surface-to-freestream differences $\Delta p_i$ can be used directly. Disconnected ports are not measurements: do not invent values for them or include them as tap locations.

Freestream dynamic pressure is $q_\infty=\tfrac12\rho_\infty V_\infty^2$. Define pressure coefficient at point $i$ as

$$
C_{p,i}=\frac{p_i-p_\infty}{q_\infty}=\frac{\Delta p_i}{q_\infty}.
$$

The sectional normal and axial coefficients are force per unit span divided by $q_\infty c$, where chord $c$ is in the same length units as the coordinates:

$$
C_n=\frac{F'_n}{q_\infty c},\qquad C_a=\frac{F'_a}{q_\infty c}.
$$

The denominator has units Pa·m = N/m, so these coefficients are dimensionless. Substituting the force sums and applying the trapezoidal rule gives the discrete contour equations:

$$
C_n=-\sum_i\frac{C_{p,i}+C_{p,i+1}}{2}\frac{\Delta x_i}{c},\qquad
C_a=+\sum_i\frac{C_{p,i}+C_{p,i+1}}{2}\frac{\Delta y_i}{c}.
$$

For closely spaced elements, these sums approach the corresponding contour integrals:

$$
C_n=-\oint C_p\,\frac{dx}{c},\qquad C_a=+\oint C_p\,\frac{dy}{c}.
$$

These are two-dimensional sectional coefficients based on force per unit span, not finite-wing planform lift or drag coefficients.

Finally, rotate the chord-axis force components into lift and drag axes referenced to the freestream. Let $\alpha$ be angle of attack, the angle between the chord reference and freestream direction using the course data's sign convention:

$$
C_l=C_n\cos\alpha-C_a\sin\alpha,\qquad
C_d=C_n\sin\alpha+C_a\cos\alpha.
$$

The normal-force component projects mostly into lift; its drag projection grows with angle of attack. The axial-force component projects mostly into drag and subtracts from lift for positive $\alpha$ under this convention. MATLAB's `sin` and `cos` expect radians; convert measured degrees with `deg2rad`, or use `sind` and `cosd`.

## D. Apply the method to the connected pressure taps

The model is a Clark Y-14 infinite wing with nominal chord $c=3.5$ in (0.0889 m). Coordinates $x$ and $y$ are in inches in the map below. Channel numbers and physical port numbers are not interchangeable.

| Channel | Port | $x$ (in) | $y$ (in) | Surface |
|---:|---:|---:|---:|---|
|1|1|0.000|0.14665|Upper|
|2|2|0.175|0.33075|Upper|
|3|3|0.350|0.40180|Upper|
|4|4|0.700|0.47600|Upper|
|5|5|1.050|0.49000|Upper|
|6|6|1.400|0.47740|Upper|
|7|7|1.750|0.44030|Upper|
|8|8|2.100|0.38325|Upper|
|9|10|2.800|0.21875|Upper|
|10|12|2.800|0.00000|Lower|
|11|14|2.100|0.00000|Lower|
|12|16|1.400|0.00000|Lower|
|13|17|1.050|0.00000|Lower|
|14|18|0.700|0.00140|Lower|
|15|19|0.350|0.01750|Lower|
|16|20|0.175|0.03885|Lower|

Channels 1–9 follow the upper surface from the leading edge toward the trailing edge (ports 1–8 and 10). Channels 10–16 follow the lower surface back toward the leading edge (ports 12, 14, 16, 17, 18, 19, and 20). Ports 9, 13, and 15 are disconnected. Port 11 is the theoretical trailing-edge point at $(x_{TE},y_{TE})=(3.5\text{ in},0)$, not a measured channel. The upper contour proceeds from channel 9 to this trailing-edge point; the lower contour returns through channel 10 and the remaining lower taps. Close the contour with a straight segment from the last connected lower tap (port 20) to port 1.

### Trailing-edge pressure closure

Extrapolate each surface's pressure coefficient from its two nearest connected taps using the general two-point linear formula evaluated at $x_{TE}$:

$$
C_{p,TE}=C_{p,a}+(C_{p,b}-C_{p,a})\frac{x_{TE}-x_a}{x_b-x_a}.
$$



Average the two extrapolations to obtain the theoretical trailing-edge coefficient:

$$
C_{p,TE}=\frac{C_{p,TE,u}+C_{p,TE,l}}{2}.
$$

For each selected angle, calculate $C_{p,i}=\Delta p_i/q_\infty$. The supplied surface-pressure channels are already surface-to-freestream pressure differences in Pa; do not subtract atmospheric pressure a second time. Use the measured Pitot dynamic pressure for the corresponding angle group. Plot $C_p$ versus $x/c$ for representative angles, and measured $C_l$ and $C_d$ versus angle of attack. Reduce enough points to show the measured trend; exhaustive repeated reductions or multi-speed coefficient maps are not required.

## E. Coefficient uncertainty and reference comparison

For every measured angle included in the final coefficient plots, use 10,000 Monte Carlo trials and the designated provisional rectangular bounds from the sensor summary. In each trial:

1. Add one uniform perturbation from −49.8 Pa to +49.8 Pa to measured Pitot dynamic pressure. Share this same perturbed $q$ across all 16 taps.
2. Independently add a uniform perturbation from −4.9818 Pa to +4.9818 Pa to each measured surface-pressure channel.
3. Add one uniform perturbation from −0.5° to +0.5° to measured angle of attack.
4. Recalculate pressure coefficients, trailing-edge closure, full-contour $C_n$ and $C_a$, and rotated $C_l$ and $C_d$.
5. Repeat for all 10,000 trials at that angle and calculate sample standard deviations $s_{C_l}$ and $s_{C_d}$.

Plot the sample standard deviations as ±1 combined-standard-uncertainty bars centered on the nominal measured coefficients. These are standard uncertainty bars, not 95% intervals. Independent channel errors are the provisional baseline because channel covariance has not been measured. These bounds and distributions are propagation assumptions, not confirmed calibration values. Do not perturb atmospheric pressure, temperature, density, or derived airspeed again: the coefficient calculation uses measured $q$ as its denominator.

Compare measured sectional $C_l(\alpha)$ and $C_d(\alpha)$ with the supplied Clark Y-14 reference data over its stated validity range. Evaluate agreement and disagreement; do not assume agreement is required. Consider Reynolds-number and other condition differences, and distinguish coefficient uncertainty from model/reference discrepancy. The current historical pressure dataset is a single-speed sweep near 30.37 m/s; the empirical NACA TR 628 reference is near $Re\approx3.02\times10^6$, while the measured sweep is near $Re\approx1.46\times10^5$. The comparison is limited to −8° through +12°. These data do not establish aerodynamic response at other speeds or experimentally verify a recommended operating region.

## F. Engineering conclusion and report

Connect the airspeed uncertainty plots and selected favorable region to the aerodynamic measurements available. State clearly whether each aerodynamic condition is newly measured, historical, or a calculation. Explain how speed and sensor constraints inform a current or future test choice, and what the coefficient data support. Because the available pressure sweep is at one historical speed, it does not experimentally verify the recommended operating region or establish a multi-speed aerodynamic response.

In the group report, recommend **one feasible improvement to the experimental setup or measurement process**, supported by your uncertainty analysis or experimental observations. Submit one concise report communicating the airspeed model and uncertainty plots, test-region recommendation, relevant coefficient reduction and uncertainty method, measured aerodynamic trends, reference comparison, and limitations. The client briefing presents the decision and evidence concisely. The scheduled **group report** and **client briefing** are the only Tier 2 assessments.
