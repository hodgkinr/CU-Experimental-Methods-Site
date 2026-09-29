# Tier 2 Experimental Investigation - Frequently Asked Questions

## 1. What is the consulting scenario?

Your group is acting as an engineering consulting team. The client wants to know which
conditions produce useful data, which conditions should be avoided, and what setup change
would improve the experiment.

## 2. How is this different from Tier 1?

Tier 1 emphasized pointwise analysis. Tier 2 asks you to repeat the uncertainty analysis
across a range of test conditions and use the resulting uncertainty envelope to make a test
decision.

## 3. What is the uncertainty envelope?

It is a plot of absolute or relative standard uncertainty versus a test condition. Examples
include freestream velocity for the wind tunnel and applied torque for spin-up testing.

## 4. What should we call the new idea?

Use **condition-dependent uncertainty envelope** for the plot and **dimensionless sensitivity
coefficient** for the mathematical factors. Use **relative standard uncertainty** for
u_y/|y| at one condition.

## 5. Is this an individual or group assignment?

The experiment and report are group work. Every student must understand the full measurement
chain and be able to explain the group's uncertainty envelope and recommendation.

## 6. How much testing do we have?

The assignment is designed for four in-person lab working days. Large groups should divide
calibration, data collection, reduction, uncertainty analysis, and documentation tasks in
parallel, while preserving shared raw data and decisions.

## 7. What must be ready before primary testing?

Your group needs a short prediction brief containing the client objective, measurement chain,
predicted response, initial uncertainty envelope, committed test matrix, acceptance criterion,
and risk forecast.

## 8. What if the prediction is wrong?

That is useful. The grade is based on whether the prediction was reasoned and specific and
whether you diagnose the discrepancy honestly. Do not rewrite the original prediction after
seeing the data.

## 9. Do we need to derive every structural equation?

No. In the aeroelasticity branch, the instructor provides the beam, load-to-deflection, and
geometry equations needed to predict tip deflection. Students focus on the aerodynamic
measurement chain, finite-wing load estimate, uncertainty, and test recommendation.

## 10. What exactly is required for the aeroelasticity branch?

Use wind-tunnel pressure, atmospheric, and temperature information to estimate freestream
conditions; compare infinite-wing and finite-wing lift/load estimates; predict tip deflection;
and determine how uncertainty changes across the approved velocity range.

## 11. What exactly is required for the spin-module branch?

Calibrate the gyro, estimate reaction-wheel and spacecraft-body inertia from torque trials,
and characterize coast-down resistance either experimentally or from instructor-provided
data. Then predict rotational response and map uncertainty versus the appropriate rate or
torque condition.

## 12. Should spin-module uncertainty be plotted versus rate or torque?

Use the variable that matches the experiment:

- gyro calibration: angular rate;
- spin-up/inertia testing: applied torque or motor current;
- coast-down: angular rate.

For spin-up, applied torque is usually the better design variable because it is controlled,
while angular rate is a response.

## 13. Can Monte Carlo replace partial derivatives?

Monte Carlo can replace manual derivative calculations for the numerical propagation, but
you still need to state the data-reduction equation and explain the input distributions.
Compare Monte Carlo with the normalized Taylor result at representative conditions.

## 14. How many Monte Carlo samples should we use?

Use at least 10,000 trials per representative condition unless a convergence study justifies
a different number. Check that the reported standard deviation or percentile interval is
stable when the sample count increases.

## 15. Do we redraw systematic errors for every time sample?

Usually no. A calibration, scale-factor, or fixed offset error is shared across a virtual
experiment. Draw it once for that experiment. Redraw sample-to-sample noise only when the
model is intended to represent random measurement noise.

## 16. What makes a setup change convincing?

Name the affected measurement or parameter, identify the limitation, estimate how the
uncertainty envelope changes, and explain why the change is feasible. “Use a better sensor”
is not enough.

## 17. What if a sensor specification or sample dataset is missing?

Use the clearly labeled instructor placeholder and state how the missing information affects
your conclusion. Do not invent a sensor specification or torque constant.

## 18. What should the client briefing show?

Show the client question, predicted result, measured comparison, uncertainty envelope with
useful and inappropriate regions marked, recommended setup alteration, and final test-
envelope recommendation.

## 19. Why mention ASEN 6011?

The assignment is motivated by the uncertainty-analysis perspective used in Professor John
Farnsworth's ASEN 6011 Experimental Fluid Mechanics course. Students who want a deeper
treatment of uncertainty propagation, experimental fluid mechanics, and measurement-system
design are encouraged to consider taking ASEN 6011.

*ASEN 3501 - Tier 2 FAQ | Working draft*
