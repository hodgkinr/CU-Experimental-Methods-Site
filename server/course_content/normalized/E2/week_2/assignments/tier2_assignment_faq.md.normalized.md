# Tier 2 Experimental Investigation - Frequently Asked Questions

## 1. What is the consulting scenario?

Your group is acting as an engineering consulting team. The client wants to know which conditions produce useful data, which conditions should be avoided, and what improvement(s) would improve the experiment.

## 2. How is this different from Tier 1?

Tier 1 emphasized pointwise analysis. Tier 2 asks you to repeat the uncertainty analysis across a range of test conditions and use the resulting uncertainty envelope to make a test decision.

## 3. What is the uncertainty envelope?

It is a plot of scaled systematic standard uncertainty or normalized systematic standard uncertainty versus a test condition. Examples include freestream velocity for the wind tunnel and applied torque for spin-up testing.

## 4. What should we call the new idea?

Use **condition-dependent uncertainty envelope** for the plot and **dimensionless sensitivity coefficient** for the mathematical factors. Use **relative standard uncertainty** for \(\mathrm{NSU}_{y,\mathrm{sys}}=b_{y,\mathrm{sys}}/|y|\) at one condition.

## 5. Is this an individual or group assignment?

The experiment and report are group work. Every student must understand the full measurement
chain and be able to explain the group's uncertainty envelope and recommendation.

## 6. How much testing do we have?

The assignment is designed for four in-person lab working days. Large groups should divide
calibration, data collection, reduction, uncertainty analysis, and documentation tasks in
parallel, while preserving shared raw data and decisions.

## 7. What must be ready before primary testing?

Your group needs a short prediction brief containing the client objective, measurement chain,
predicted response, initial uncertainty envelope, committed test matrix, decision rule,
and risk forecast.

## 8. What if the prediction is wrong?

That is useful. The grade is based on whether the prediction was reasoned and specific and
whether you diagnose the discrepancy honestly. Do not rewrite the original prediction after
seeing the data.

## 9. What is required in the wind-tunnel branch?

First use the tunnel sensor values and uncertainty information to select appropriate
airspeed or dynamic-pressure conditions. Then apply those conditions to infinite-wing data
over angle of attack and calculate \(C_l\) and \(C_d\), with uncertainty. Include the
pressure-port mapping, measured-versus-commanded condition comparison, residuals, and a
stated rule for classifying conditions.

## 10. Is finite-wing structural analysis required?

No. Finite-wing spanwise loading, spar/beam calculations, structural deflection,
whiffle-tree analysis, finite-wing validation, and finite-wing structural uncertainty are
reference material only for this revised student objective.

## 11. What exactly is required for the spin-module branch?

Analyze uncertainty in base rotational velocity versus applied reaction-wheel torque, use it
to select torque conditions, predict base rate with the rotational model, compare it with the
encoder base-rate channel, and plot residuals versus applied torque. Distinguish commanded
torque from current-inferred torque using the motor torque constant. Interpret residuals using
sensor, torque, parameter, resistance, timing, and model-form explanations.

## 12. Is gyro calibration required?

Not as the primary application. Use it as supporting work if it is needed to establish
base-rate uncertainty or if the instructor assigns it. The central comparison uses the
encoder as the base-rate truth/reference sensor.

## 13. What is the applied torque in the spin analysis?

State whether you use commanded torque \(\tau_{\mathrm{cmd}}\) or torque inferred from
motor current, \(\tau_{\mathrm{inf}}=k_t I_{\mathrm{motor}}\). Do not treat them as
interchangeable without explaining the motor constant, current uncertainty, and any command
calibration.

## 14. Can Monte Carlo replace partial derivatives?

Monte Carlo can replace manual derivative calculations for the numerical propagation, but you still need to state the data-reduction equation and explain the input distributions. Compare Monte Carlo with the normalized Taylor result at representative conditions.

## 15. How many Monte Carlo samples should we use?

Use at least 10,000 trials per representative condition unless a convergence study justifies
a different number. Check that the reported standard deviation or percentile interval is
stable when the sample count increases.

## 16. Do we redraw systematic errors for every time sample?

Usually no. A calibration, scale-factor, or fixed offset error is shared across a virtual experiment. Draw it once for that experiment. Redraw sample-to-sample noise only when the model is intended to represent random measurement noise.

## 17. What makes a setup change convincing?

Name the affected measurement or parameter, identify the limitation, estimate how the uncertainty envelope changes, and explain why the change is feasible. “Use a better sensor” is not enough.

## 18. What if a sensor specification or sample dataset is missing?

Use the clearly labeled instructor placeholder and state how the missing information affects your conclusion. Do not invent a sensor specification or torque constant.

## 19. What should the client briefing show?

Show the client question, predicted result, measured comparison, uncertainty envelope with useful and inappropriate regions marked, recommended setup alteration, and final test-envelope recommendation.

## 20. Why mention ASEN 6011?

The assignment is motivated by the uncertainty-analysis perspective used in Professor John Farnsworth's ASEN 6011 Experimental Fluid Mechanics course. Students who want a deeper treatment of uncertainty propagation, experimental fluid mechanics, and measurement-system design are encouraged to consider taking ASEN 6011.

*ASEN 3501 - Tier 2 FAQ | Working draft*
