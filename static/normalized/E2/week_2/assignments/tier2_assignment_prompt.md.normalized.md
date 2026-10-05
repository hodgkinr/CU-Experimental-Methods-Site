# ASEN 3501 - Tier 2 Experimental Investigation
## Define the Test Envelope: Predict, Measure, Quantify, Recommend

**Role:** You are an engineering consultant hired to evaluate an aerospace experiment.

**Client question:** At what test conditions can this experiment produce results that are reliable enough for its intended use? Which conditions should be avoided, and what improvement(s) to the instrumentation or setup would move the useful test envelope?

**Format:** Large group, one assigned laboratory branch, four in-person lab working days, two in-person lectures, one technical report, and one short client briefing.

**Experiment assignments:**

- **Aeroelasticity:** Use the tunnel sensor values and uncertainty information to select informative conditions, then apply the selected conditions to infinite-wing data over angle of attack and determine \(C_l\) and \(C_d\) with uncertainty.
- **Spin Modules:** Analyze uncertainty in base rotational velocity as a function of applied reaction-wheel torque, use that result to select torque conditions, predict base rate with a rotational model, and compare the prediction with encoder base-rate measurements.

## Why Tier 2 is different from Tier 1

Tier 1 focused on understanding an existing experiment and performing pointwise analysis. Tier 2 asks you to evaluate the experiment as a measurement system over a range of possible test conditions.

The central question is no longer only:

> What value did we measure at this condition?

It is:

> How does the quality of the derived result change as the test condition changes, and what
> should an engineer do about that?

You will use a physics-based prediction, sensor specifications, calibration information, and measured data to construct a **condition-dependent uncertainty envelope**. The envelope will show where the experiment is informative and where sensor resolution, calibration, friction, signal processing, or model assumptions make the result difficult to interpret.

The assignment is motivated by the uncertainty-analysis approach used in ASEN 6011, Experimental Fluid Mechanics, taught by Professor John Farnsworth. Students interested in experimental methods, fluid mechanics, aerospace testing, or measurement science are strongly encouraged to consider ASEN 6011. That course develops these ideas in substantially greater depth, both through its assignments and through the broader course sequence.

## Learning goals

By the end of Tier 2, you should be able to:

1. Build a predictive measurement model before collecting data.
2. Trace uncertainty from sensor and DAQ information to an aerospace quantity of interest.
3. Explain normalized standard uncertainty using dimensionless sensitivity coefficients.
4. Use Monte Carlo analysis to propagate realistic sensor and parameter distributions.
5. Identify appropriate and inappropriate test conditions from an uncertainty envelope.
6. Propose a specific, quantitatively justified improvement to the experiment that would move the useful test envelope.
7. Distinguish measurement uncertainty from model-form discrepancy and setup limitations.

## Student support handouts

These standalone handouts provide the uncertainty concepts and power-lab bridge used to prepare for Tier 2. They are separate from the assignment page so they can also be shared independently:

- [From Pointwise Uncertainty to a Test Envelope](student-guides/TIER2_normalized_uncertainty_guide.pdf)
- [The Power Lab as a Bridge to a Test Envelope](student-guides/power-lab-example/TIER2_power_lab_bridge.pdf)
- [Power-lab MATLAB code](student-guides/power-lab-example/power-lab-example-matlab/matlab_code.html)
- [Download the raw MATLAB file](student-guides/power-lab-example/power-lab-example-matlab/matlab_code.m)

## Vocabulary for this assignment

Use the following terms consistently:

- **Standard uncertainty:** A one-standard-deviation uncertainty estimate for a quantity.
- **Relative standard uncertainty:** Standard uncertainty divided by the nominal quantity, such as \(u_y/|y|\).
- **Condition-dependent uncertainty envelope:** A plot of absolute or relative standard uncertainty versus a test condition, such as freestream velocity or applied torque.
- **Sensitivity coefficient:** The dimensionless factor that describes how a fractional input change affects a fractional output change.
- **Useful test envelope:** The region where the predicted result has acceptable uncertainty, the hardware is operating within limits, and the model remains appropriate.

The phrase “sensitivity of the uncertainty” is understandable but imprecise. In your report, use **condition-dependent uncertainty envelope** for the overall plot and **dimensionless sensitivity coefficient** for the mathematical factors.

## Two in-person lectures

### Lecture 1 - From Tier 1 pointwise uncertainty to an uncertainty envelope

This lecture makes the cognitive transition from a single Monte Carlo analysis at one data point to an aerospace test-condition study. It introduces:

- the complete measurement chain from physical system to sensor to DAQ to derived result;
- the difference between pointwise random variation and setup-level or calibration errors;
- normalized standard uncertainty;
- dimensionless sensitivity coefficients;
- why a fixed sensor resolution can be insignificant at one condition and dominant at another;
- how to compare Taylor-series propagation and Monte Carlo propagation;
- how an uncertainty curve becomes an engineering recommendation.

The [power-lab bridge handout](student-guides/power-lab-example/TIER2_power_lab_bridge.pdf) should be completed before or during this lecture. The [normalized-uncertainty handout](student-guides/TIER2_normalized_uncertainty_guide.pdf) provides the general framework used in both experiment branches.

### Lecture 2 - From an uncertainty curve to a test decision

This lecture focuses on engineering judgment. It addresses:

- defining an acceptable test result before collecting data;
- distinguishing low relative uncertainty from physically meaningful or safe operation;
- selecting test points efficiently when lab time is limited;
- separating instrumentation changes from model changes;
- predicting how a sensor range, resolution, calibration, or sampling choice would move the useful test envelope;
- writing a recommendation that a client could act on.

## Four-day laboratory plan

The exact scheduling of groups may vary, but the assignment is designed around four in-person working days.

| Day | Common purpose | Expected branch work | Required evidence |
|---|---|---|---|
| 1 | Understand and plan | Inspect setup, confirm sensors and limits, freeze prediction, begin calibration or baseline measurements | Measurement-chain diagram, prediction, initial test matrix |
| 2 | Collect primary data | Wind-tunnel pressure/airspeed data at selected conditions, or reaction-wheel torque/base-rate data | Raw data, field notes, condition log |
| 3 | Complete the model and uncertainty sweep | \(C_l/C_d\) reduction and uncertainty analysis, or rotational-model prediction, residuals, and Monte Carlo sweep | Preliminary uncertainty envelope and identified gaps |
| 4 | Validate and recommend | Targeted repeat/check measurements, finalize comparisons, test or quantify proposed setup change | Final evidence for test-envelope recommendation |

Large groups should divide the work into parallel roles, but every student must understand the complete measurement chain and the final recommendation.

## Phase 1 - Consulting brief and pre-test prediction

Before collecting primary data, submit or show the instructor/TA a short prediction brief. This is a working document, not a polished report. It must contain:

1. **Client objective:** What quantity will the client use the experiment to estimate or predict, and what test-condition decision must the experiment support?
2. **Measurement chain:** What physical quantity is measured by each sensor, and how does it enter the data-reduction equation?
3. **Predicted response:** Give numerical values or curves over the planned test range.
4. **Initial uncertainty envelope:** Use the supplied specifications to estimate where the result should be reliable or unreliable.
5. **Committed test matrix:** Identify the conditions you will test and why they are useful.
6. **Decision rule:** Define how your group will classify a condition as appropriate, marginal, or inappropriate. If the instructor has not supplied a numerical threshold, state the evidence-based rule you use rather than inventing a limit.
7. **Risk forecast:** Describe one data pattern that would indicate a setup, sensor, or model problem rather than ordinary scatter.

The prediction is frozen when the group begins its primary test. A wrong prediction is useful evidence; silently rewriting it after seeing the data is not.

## Phase 2 - Laboratory execution

Follow the branch-specific procedure. During testing:

- record the actual condition, not only the commanded condition;
- record sensor range, units, calibration information, and any changes to the setup;
- note anomalies while they happen;
- preserve raw data and a clear file naming convention;
- use the uncertainty envelope to decide whether a repeat or additional test point is worth the available time;
- do not spend the final lab day collecting points that your own analysis predicts will be dominated by resolution or model limitations unless the purpose is to demonstrate that limitation.

## Phase 3 - Required analysis

### 3.1 Prediction versus measurement

Compare the committed prediction with the measured result. Use residuals or equivalent comparison plots. Apply the decision rule stated in the prediction brief and classify important discrepancies as likely measurement variation, calibration or bias, setup effect, data-reduction issue, parameter uncertainty, timing/friction/resistance, or model-form discrepancy.

### 3.2 Condition-dependent uncertainty envelope

For the primary derived quantity, produce both:

- absolute scaled systematic standard uncertainty versus test condition; and
- relative systematic standard uncertainty \(\mathrm{NSU}_{y,\mathrm{sys}}=b_{y,\mathrm{sys}}/|y|\) versus test condition.

Identify:

- the low-uncertainty region;
- the high-uncertainty region;
- the dominant uncertainty source in each region;
- any regions that are physically invalid, unsafe, saturated, or outside model validity.

### 3.3 Taylor-series and Monte Carlo methods

Use the method required by your branch document. In general, the report should include:

- a normalized sensitivity derivation for the main data-reduction equation;
- a Monte Carlo implementation with at least 10,000 trials per representative condition or a justified convergence study;
- a comparison of the two methods at selected conditions;
- an explanation of any disagreement based on nonlinearity relative to the uncertainty size, a nominal value near zero, omitted correlations, nonsmooth behavior, or invalid samples.

For a linear model, the Taylor root-sum-square standard deviation is exact for any input distributions with finite variance. Bounded distributions mainly change the shape of the output distribution and therefore affect percentile or coverage intervals, not the standard deviation itself.

Monte Carlo is not a substitute for understanding the data-reduction equation. It is a way to propagate the model and uncertainty distributions without manually differentiating every equation.

### 3.4 Client recommendation and setup modification

Your group must recommend:

1. appropriate test conditions;
2. inappropriate or low-value test conditions;
3. the dominant reason for each decision; and
4. at least one specific setup alteration that would move the useful test envelope.

The alteration may involve sensor range, sensor resolution, calibration, signal conditioning, sampling, test-point selection, geometry, or an additional measurement. Estimate the effect of the improvement quantitatively. “Use a better sensor” is not sufficient.

## Branch requirements

### Aeroelasticity branch

The primary student application is the infinite-wing aerodynamic measurement system. The uncertainty analysis comes first: use the differential-pressure, atmospheric-pressure, temperature, angle-of-attack, pressure-port, and other available sensor channels to determine which tunnel conditions are informative.

Students will:

1. Map the measurement chain from commanded tunnel condition to measured differential pressure, atmospheric pressure, temperature, tunnel airspeed, angle of attack, surface pressures, and data reduction.
2. Distinguish commanded from measured tunnel conditions and use the measured values in all calculations.
3. Use the sensor specifications and uncertainty model to sweep primarily over tunnel airspeed or dynamic pressure and identify informative, marginal, and uncertainty-dominated conditions.
4. Apply the selected conditions to infinite-wing data over the assigned angles of attack.
5. Use the pressure-port mapping and supplied geometry to calculate \(C_p\), \(C_n\), \(C_a\), \(C_l\), and \(C_d\) versus angle of attack.
6. Propagate uncertainty to the relevant sensor inputs and derived quantities, using Taylor/sensitivity analysis and Monte Carlo where required.
7. Compare the physics-based prediction with measured coefficients, use residuals to distinguish measurement uncertainty from model-form differences, and recommend a justified test envelope.
8. Quantify one feasible instrumentation or setup improvement and explain how it would change the envelope.

The decision rule for “appropriate” conditions must be stated by the group. Do not invent an acceptance threshold or operating limit; use an instructor-provided value when available or identify the evidence and limitations supporting an open-ended recommendation.

Finite-wing spanwise loading, finite-wing validation, spar/beam parameters, structural deflection, whiffle-tree analysis, and finite-wing structural uncertainty are not required student work for this branch. Related files may remain in the repository as reference material.

### Spin-module branch

The primary student application is prediction of base rotational velocity from reaction-wheel torque. The uncertainty analysis comes first: determine how uncertainty in applied torque, current, motor torque constant, inertia, resistance, timing, and rate measurement changes with the applied reaction-wheel torque.

Students will:

1. Map the reaction-wheel motor current, torque constant, wheel-rate, base-rate encoder, timing, DAQ, and data-reduction chain.
2. Define the applied-torque quantity explicitly. Distinguish commanded torque \(\tau_{\mathrm{cmd}}\) from torque inferred through current, \(\tau_{\mathrm{inf}}=k_{t,\mathrm{RW}}I_{\mathrm{RW,motor}}\), and state which one enters the model.
3. Analyze uncertainty in base rotational velocity as a function of applied reaction-wheel torque.
4. Use that uncertainty envelope to select appropriate, marginal, and inappropriate torque conditions.
5. Use the supplied or fitted rotational model to predict base rotational rate, including clearly labeled inertia and resistance parameters.
6. Compare predicted base rate with the encoder base-rate measurement, treating the encoder as the truth/reference sensor for this comparison.
7. Produce residuals between predicted and encoder base rate versus applied reaction-wheel torque.
8. Interpret residual trends as possible sensor uncertainty, torque uncertainty, parameter uncertainty, friction/resistance, timing, or model-form error.
9. Quantify one feasible instrumentation or setup improvement and explain how it would change the envelope.

Gyro calibration may be used as supporting work when it is needed to establish base-rate uncertainty, but it is not the central deliverable unless the instructor assigns it. Reaction-wheel and spacecraft-body inertia, resistance, motor constants, encoder, and current-sensor material should be retained only to support the reaction-wheel-to-base-rate model. Solar-panel comparison, saturation-time analysis, and controller design are outside the required scope unless explicitly assigned.

## Deliverables

### 1. Technical report

Submit one group report containing:

1. consulting objective, intended use, and decision rule;
2. committed pre-test prediction;
3. measurement-chain diagram and assumptions;
4. test matrix and actual test conditions;
5. prediction-versus-measurement comparison and residual interpretation;
6. normalized sensitivity derivation;
7. Monte Carlo method and distribution assumptions;
8. absolute and relative uncertainty envelopes;
9. dominant-source interpretation;
10. appropriate/inappropriate test-condition recommendations;
11. one quantitatively justified setup alteration;
12. limitations, unresolved placeholders, and conclusion;
13. individual contribution statement.

The report should be concise enough that a client could find the recommendation quickly.

### 2. Client briefing

Prepare one quad chart or equivalent single-page briefing with:

- client question and predicted result;
- uncertainty envelope with useful and inappropriate regions marked;
- comparison with measured data;
- recommended setup change and expected effect;
- final test-envelope recommendation.

Each group gives a short briefing followed by questions. The purpose is technical decision-making, not a complete reproduction of the report.

### 3. Individual evidence

Each student must be able to explain the measurement chain, the normalized uncertainty, the Monte Carlo result, and the group recommendation. The instructor may use a short individual check or targeted question during the briefing.
