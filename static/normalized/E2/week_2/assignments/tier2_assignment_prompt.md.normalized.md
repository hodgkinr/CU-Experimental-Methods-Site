# ASEN 3501 - Tier 2 Experimental Investigation
## Define the Test Envelope: Predict, Measure, Quantify, Recommend

**Role:** You are an engineering consultant hired to evaluate an aerospace experiment.

**Client question:** At what test conditions can this experiment produce results that are
reliable enough for its intended use? Which conditions should be avoided, and what change
to the instrumentation or setup would move the useful test envelope?

**Format:** Large group, one assigned laboratory branch, four in-person lab working days,
two common lectures, one technical report, and one short client briefing.

**Laboratory choices:**

- Aeroelasticity branch: wind-tunnel pressure measurements, lift estimation, and finite-wing
 tip-deflection prediction.
- Spin-module branch: gyro calibration, reaction-wheel and spacecraft-body inertia
 estimation, and rotational-dynamics prediction with an experimentally estimated
 resistance model.

## Why Tier 2 is different from Tier 1

Tier 1 focused on understanding an existing experiment and performing pointwise analysis.
Tier 2 asks you to evaluate the experiment as a measurement system over a range of possible
test conditions.

The central question is no longer only:

> What value did we measure at this condition?

It is:

> How does the quality of the derived result change as the test condition changes, and
> what should an engineer do about that?

You will use a physics-based prediction, sensor specifications, calibration information,
and measured data to construct a **condition-dependent uncertainty envelope**. The envelope
will show where the experiment is informative and where sensor resolution, calibration,
friction, signal processing, or model assumptions make the result difficult to interpret.

The assignment is motivated by the uncertainty-analysis approach used in ASEN 6011,
Experimental Fluid Mechanics, taught by Professor John Farnsworth. Students interested in
experimental methods, fluid mechanics, aerospace testing, or measurement science are
strongly encouraged to consider ASEN 6011. That course develops these ideas in substantially
greater depth, both through its assignments and through the broader course sequence.

## Learning goals

By the end of Tier 2, you should be able to:

1. Build a predictive measurement model before collecting data.
2. Trace uncertainty from sensor and DAQ information to an aerospace quantity of interest.
3. Explain normalized standard uncertainty using dimensionless sensitivity coefficients.
4. Use Monte Carlo analysis to propagate realistic sensor and parameter distributions.
5. Identify appropriate and inappropriate test conditions from an uncertainty envelope.
6. Propose a specific, quantitatively justified change to the experiment that would move the
 useful test envelope.
7. Distinguish measurement uncertainty from model-form discrepancy and setup limitations.

## Vocabulary for this assignment

Use the following terms consistently:

- **Standard uncertainty:** A one-standard-deviation uncertainty estimate for a quantity.
- **Relative standard uncertainty:** Standard uncertainty divided by the nominal quantity,
 such as u_y/|y|.
- **Condition-dependent uncertainty envelope:** A plot of absolute or relative standard
 uncertainty versus a test condition, such as freestream velocity or applied torque.
- **Sensitivity coefficient:** The dimensionless factor that describes how a fractional input
 change affects a fractional output change.
- **Useful test envelope:** The region where the predicted result has acceptable uncertainty,
 the hardware is operating within limits, and the model remains appropriate.

The phrase “sensitivity of the uncertainty” is understandable but imprecise. In your report,
use **condition-dependent uncertainty envelope** for the overall plot and **dimensionless
sensitivity coefficient** for the mathematical factors.

## Two common lectures

### Lecture 1 - From Tier 1 pointwise uncertainty to an uncertainty envelope

This lecture makes the cognitive transition from a single Monte Carlo analysis at one data
point to an aerospace test-condition study. It introduces:

- the complete measurement chain from physical system to sensor to DAQ to derived result;
- the difference between pointwise random variation and setup-level or calibration errors;
- normalized standard uncertainty;
- dimensionless sensitivity coefficients;
- why a fixed sensor resolution can be insignificant at one condition and dominant at
 another;
- how to compare Taylor-series propagation and Monte Carlo propagation;
- how an uncertainty curve becomes an engineering recommendation.

The power-measurement bridge in 'TIER2_power_lab_bridge.md' should be completed before or
during this lecture.

### Lecture 2 - From an uncertainty curve to a test decision

This lecture focuses on engineering judgment. It addresses:

- defining an acceptable test result before collecting data;
- distinguishing low relative uncertainty from physically meaningful or safe operation;
- selecting test points efficiently when lab time is limited;
- separating instrumentation changes from model changes;
- predicting how a sensor range, resolution, calibration, or sampling choice would move the
 useful test envelope;
- writing a recommendation that a client could act on.

## Four-day laboratory plan

The exact scheduling of groups may vary, but the assignment is designed around four in-person
working days.

| Day | Common purpose | Expected branch work | Required evidence |
|---|---|---|---|
| 1 | Understand and plan | Inspect setup, confirm sensors and limits, freeze prediction, begin calibration or baseline measurements | Measurement-chain diagram, prediction, initial test matrix |
| 2 | Collect primary data | Wind-tunnel pressure/airspeed data, or gyro and spin-up data | Raw data, field notes, condition log |
| 3 | Complete the model and uncertainty sweep | Finite-wing/deflection analysis, or coast-down/resistance characterization and Monte Carlo sweep | Preliminary uncertainty envelope and identified gaps |
| 4 | Validate and recommend | Targeted repeat/check measurements, finalize comparisons, test or quantify proposed setup change | Final evidence for test-envelope recommendation |

Large groups should divide the work into parallel roles, but every student must understand
the complete measurement chain and the final recommendation.

## Phase 1 - Consulting brief and pre-test prediction

Before collecting primary data, submit or show the instructor/TA a short prediction brief.
This is a working document, not a polished report. It must contain:

1. **Client objective:** What quantity will the client use the experiment to estimate or
 predict?
2. **Measurement chain:** What physical quantity is measured by each sensor, and how does it
 enter the data-reduction equation?
3. **Predicted response:** Give numerical values or curves over the planned test range.
4. **Initial uncertainty envelope:** Use the supplied specifications to estimate where the
 result should be reliable or unreliable.
5. **Committed test matrix:** Identify the conditions you will test and why they are useful.
6. **Acceptance criterion:** Define what agreement between prediction and measurement would
 be adequate for the stated client objective.
7. **Risk forecast:** Describe one data pattern that would indicate a setup, sensor, or model
 problem rather than ordinary scatter.

The prediction is frozen when the group begins its primary test. A wrong prediction is useful
evidence; silently rewriting it after seeing the data is not.

## Phase 2 - Laboratory execution

Follow the branch-specific procedure. During testing:

- record the actual condition, not only the commanded condition;
- record sensor range, units, calibration information, and any changes to the setup;
- note anomalies while they happen;
- preserve raw data and a clear file naming convention;
- use the uncertainty envelope to decide whether a repeat or additional test point is worth
 the available time;
- do not spend the final lab day collecting points that your own analysis predicts will be
 dominated by resolution or model limitations unless the purpose is to demonstrate that
 limitation.

## Phase 3 - Required analysis

### 3.1 Prediction versus measurement

Compare the committed prediction with the measured result. Use residuals or equivalent
comparison plots. State whether the acceptance criterion was met and classify important
discrepancies as likely measurement variation, calibration or bias, setup effect, data-
reduction issue, parameter uncertainty, or model-form discrepancy.

### 3.2 Condition-dependent uncertainty envelope

For the primary derived quantity, produce both:

- absolute standard uncertainty versus test condition; and
- relative standard uncertainty u_y/|y| versus test condition.

Identify:

- the low-uncertainty region;
- the high-uncertainty region;
- the dominant uncertainty source in each region;
- any regions that are physically invalid, unsafe, saturated, or outside model validity.

### 3.3 Taylor-series and Monte Carlo methods

Use the method required by your branch document. In general, the report should include:

- a normalized sensitivity derivation for the main data-reduction equation;
- a Monte Carlo implementation with at least 10,000 trials per representative condition or
 a justified convergence study;
- a comparison of the two methods at selected conditions;
- an explanation of any disagreement based on nonlinearity, bounded distributions, shared
 parameters, or invalid samples.

Monte Carlo is not a substitute for understanding the data-reduction equation. It is a way
to propagate the model and uncertainty distributions without manually differentiating every
equation.

### 3.4 Client recommendation and setup modification

Your group must recommend:

1. appropriate test conditions;
2. inappropriate or low-value test conditions;
3. the dominant reason for each decision; and
4. at least one specific setup alteration that would move the useful test envelope.

The alteration may involve sensor range, sensor resolution, calibration, signal conditioning,
sampling, test-point selection, geometry, or an additional measurement. Estimate the effect of
the change quantitatively. “Use a better sensor” is not sufficient.

## Branch requirements

### Aeroelasticity branch

The primary quantity is finite-wing tip deflection predicted from aerodynamic loading.
Students will:

1. Use differential-pressure, atmospheric-pressure, and temperature information to predict
 freestream velocity and dynamic pressure.
2. Use the infinite-wing pressure distribution to estimate sectional C_l and a baseline
 load distribution.
3. Use the finite-wing/spanwise information to estimate the actual spanwise lift distribution.
4. Convert the lift distribution to structural load intensity and predict tip deflection using
 the supplied beam equations.
5. Compare infinite-wing and finite-wing predictions with measured data.
6. Propagate uncertainty to lift and tip deflection as a function of freestream velocity or
 another instructor-approved operating condition.
7. Recommend a useful wind-tunnel velocity envelope and a sensor or setup change that would
 move it.

Students are not required to derive the whiffle-tree geometry or repeat the structural
derivation. The instructor provides the structural equations and the needed geometry.

### Spin-module branch

The primary quantities are calibrated angular rate, reaction-wheel inertia, spacecraft-body
inertia, and predicted rotational response.

Students will:

1. Calibrate the gyro against the encoder reference over the assigned rate range.
2. Use reaction-wheel torque and angular acceleration data to estimate reaction-wheel inertia.
3. Use base-motor torque and spacecraft angular acceleration data to estimate spacecraft-body
 inertia.
4. Conduct or analyze a coast-down segment to estimate lumped resistance parameters c and
 tau_0, or use instructor-provided estimates if time or hardware availability requires.
5. Use
 I*omega_dot + c*omega + tau_0*sgn(omega) = tau_applied
 to predict rotational performance.
6. Propagate uncertainty versus applied torque for spin-up/inertia testing and versus angular
 rate for gyro or coast-down testing.
7. Recommend useful and inappropriate torque/rate conditions and a setup change that would
 move the useful test envelope.

The minimum Tier 2 spin dataset is gyro calibration, multiple reaction-wheel torque trials,
multiple base-motor torque trials, and one coast-down or instructor-provided resistance
characterization. Torque constants, sample data, exact sensor specifications, and final
test limits remain instructor-provided placeholders until verified.

## Deliverables

### 1. Technical report

Submit one group report containing:

1. consulting objective and intended use;
2. committed pre-test prediction;
3. measurement-chain diagram and assumptions;
4. test matrix and actual test conditions;
5. prediction-versus-measurement comparison;
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

Each group gives a short briefing followed by questions. The purpose is technical decision-
making, not a complete reproduction of the report.

### 3. Individual evidence

Each student must be able to explain the measurement chain, the normalized uncertainty, the
Monte Carlo result, and the group recommendation. The instructor may use a short individual
check or targeted question during the briefing.

## Scope control for four lab days

The following are intentionally not required unless the instructor assigns them as enrichment:

- complete whiffle-tree structural design;
- deriving all beam equations from first principles;
- full aerodynamic model development beyond the supplied equations;
- reaction-wheel saturation-time studies;
- solar-panel comparison;
- exhaustive sensor calibration-status research;
- testing every possible operating condition;
- deriving Taylor-series partial derivatives for every intermediate quantity.

The goal is a defensible engineering recommendation, not a complete redesign of either
laboratory.

## Resources

- 'TIER2_normalized_uncertainty_guide.md'
- 'TIER2_power_lab_bridge.md'
- 'TIER2_teaching_sequence.md'
- the assigned branch document in 'lab_compilations/'
- Tier 1 uncertainty resources, especially the pointwise Monte Carlo and residual-analysis
 documents
- ASEN 6011 HW04 solution, provided as instructor background and motivation, not as a
 student-facing worked solution

*ASEN 3501 - Tier 2 Experimental Investigation | Working draft for instructor review*
