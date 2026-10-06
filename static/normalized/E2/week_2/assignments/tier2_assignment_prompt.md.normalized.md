# ASEN 3501 - Tier 2 Experimental Investigation
## Define the Test Envelope: Predict, Measure, Quantify, Recommend

**Role:** You are an engineering consultant hired to evaluate an aerospace experiment.

**Client question:** At what test conditions can this experiment produce results that are reliable enough for its intended use? Which conditions should be avoided, and what improvement(s) to the instrumentation or setup would move the useful test envelope?

**Format:** Large group, one assigned laboratory branch, four in-person lab working days, two in-person lectures, one technical report, and one short client briefing.

**Experiment assignments:**

- **Aeroelasticity:** Use the tunnel sensor values and uncertainty information to select informative conditions, then apply the selected conditions to infinite-wing data over angle of attack and determine \(C_l\) and \(C_d\) with uncertainty.
- **Spin Modules:** Fit inertia and dynamic retardance from SC base-motor support records, predict base angular acceleration and relative uncertainty versus reaction-wheel torque, and select a candidate torque region. Historical RW records hold the base stationary and cannot validate the free-base prediction.

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
| 2 | Collect primary data | Wind-tunnel data at selected conditions, or inspect the SC support and fixture-held RW records; collect additional data only as assigned | Raw data, field notes, condition log |
| 3 | Complete the model and uncertainty sweep | \(C_l/C_d\) reduction and uncertainty analysis, or SC support fit, RW-input acceleration prediction, and uncertainty sweep | Preliminary uncertainty envelope and identified gaps |
| 4 | Compare evidence and recommend | Targeted checks where data exist; for spin, state what a future free-base RW validation must measure | Final evidence and limits for the test-envelope recommendation |

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

Compare the committed prediction with a measured result when the branch data contain the corresponding physical response. Use residuals or equivalent comparison plots and classify discrepancies. **Spin-module exception:** existing RW records hold the base stationary and do not measure the free-base RW response, so they cannot be used for model validation or RW/base-acceleration residuals. The spin prediction is transferred from SC base-motor support data; identify the transfer assumption and specify the data needed for a later free-base validation.

### 3.2 Condition-dependent uncertainty envelope

For branches with a measured response, produce both:

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

The required spin analysis is a prediction of **base angular acceleration** from reaction-wheel torque. First identify support parameters from existing SC (bare-spacecraft) records in which the **base motor** accelerates the free base. Then transfer those parameters provisionally to a future test in which reaction-wheel torque accelerates the free base. The historical reaction-wheel records hold the base stationary: they can characterize reaction-wheel torque/current and wheel speed, but they do not measure free-base angular acceleration and do not validate the transfer prediction.

For the moving branch, use the simplified constant-retarding-torque model

\[
|\alpha_{\mathrm{base}}|=\frac{|\tau_{\mathrm{RW}}|-\tau_r}{1000 I},
\qquad |\tau_{\mathrm{RW}}|>\tau_r,
\]

when torque is in mN\,m, inertia is in kg\,m\(^2\), and acceleration is in rad/s\(^2\). The factor 1000 converts mN\,m to N\,m. In signed form, the motor torque on the wheel and reaction torque on the base have opposite signs; the retarding torque opposes the direction of base motion. The fitted \(\tau_r\) is an effective **dynamic** retardance. Static breakaway is not identified, so this moving-branch equation does not describe a stationary base or establish a breakaway threshold.

Students will:

1. Use the five SC base-motor support records (nominal 4, 5, 6, 8, and 10 mN\,m) to estimate base acceleration by fitting encoder rate against recorded time over the documented steady command window. Check timestamps and gaps.
2. Infer support torque from baseline-corrected base-motor current using \(\tau_{base}=K_{t,base}(I_{base}-I_0)\); fit inertia and effective dynamic retardance using \(\tau_{\mathrm{base,mN\,m}}=1000I\alpha+\tau_r\).
3. Label \(I\) as the value fitted from this support configuration. The model assumes it is appropriate for the base response to internal reaction-wheel torque; the supplied derivation identifies a separate reaction-wheel inertia and angular-momentum exchange, and the hardware documentation does not establish that the fitted support inertia equals the base inertia in that case. Keep this transfer assumption unresolved and state what hardware or free-base experiment would test it.
4. Characterize RW current/torque and wheel speed with the historical fixture-held RW records. When torque is inferred from current, use \(\tau_{RW}=K_{t,RW}I_{RW}\), keeping the RW constant distinct from \(K_{t,base}\). Do not use their near-zero base-rate channel as a free-base acceleration measurement.
5. Propagate the documented first-pass uncertainty terms and assumptions through the RW-torque prediction. Plot predicted relative (percent) standard uncertainty in base angular acceleration versus applied RW torque. Use the working decision rule “good” = relative standard uncertainty ≤25% to select a candidate torque region, unless the instructor supplies another criterion. This cutoff is a chosen uncertainty criterion, not evidence of experimental validation or universal safety.
6. Discuss included uncertainty sources, terms treated as negligible by explicit first-pass assumption, and unresolved encoder scale/decoding, current calibration, timing, systematic, and between-run repeatability uncertainties. Keep base-motor and RW-motor torque constants in their separate roles.
7. State what a later free-base RW validation must record: signed RW current or independently measured torque, RW speed, base encoder rate, synchronized timestamps, command transitions, and repeated trials; derive acceleration with a predeclared fit window and compare it with the prediction.

The required spin uncertainty deliverable is the predicted relative (percent) standard uncertainty in base angular acceleration versus applied RW torque. An absolute uncertainty table or curve may support interpretation, but do not describe historical stationary-base RW measurements as an empirical acceleration-uncertainty curve.

The bare-minimum deliverable is the SC support fit, RW-input model prediction, uncertainty propagation, required plot, and candidate torque-region recommendation. A 3000 rpm RW speed limit and a MEMS gyro comparison are optional advanced extensions. Wheel-speed feasibility depends on applied torque, duration, and initial wheel speed; 3000 rpm is not a universal torque ceiling. A gyro may change empirical acceleration uncertainty, but does not automatically change the theoretical parameter/input-uncertainty curve. Solar-panel comparison, saturation-time analysis, and controller design are outside the required scope unless explicitly assigned.

## Deliverables

### 1. Technical report

Submit one group report containing:

1. consulting objective, intended use, and decision rule;
2. committed pre-test prediction;
3. measurement-chain diagram and assumptions;
4. test matrix and actual test conditions;
5. prediction-versus-measurement comparison and residual interpretation where the branch data contain the corresponding physical response; for spin, explain why no historical free-base RW comparison exists and identify the future validation measurements;
6. normalized sensitivity derivation;
7. Monte Carlo method and distribution assumptions;
8. absolute and relative uncertainty envelopes;
9. dominant-source interpretation;
10. appropriate/inappropriate test-condition recommendations;
11. one quantitatively justified setup alteration where required by the assigned branch; for the bare-minimum spin task, prioritize the SC fit, RW prediction, uncertainty plot, candidate-region decision, and transfer/data limitations;
12. limitations, unresolved placeholders, and conclusion;
13. individual contribution statement.

The report should be concise enough that a client could find the recommendation quickly.

### 2. Client briefing

Prepare one quad chart or equivalent single-page briefing with:

- client question and predicted result;
- uncertainty envelope with useful and inappropriate regions marked;
- measured comparison when corresponding data exist; for spin, label the RW response as a prediction and state the missing free-base validation data;
- recommended setup change and expected effect when required by the assigned branch;
- final test-envelope recommendation.

Each group gives a short briefing followed by questions. The purpose is technical decision-making, not a complete reproduction of the report.

### 3. Individual evidence

Each student must be able to explain the measurement chain, the normalized uncertainty, the Monte Carlo result, and the group recommendation. The instructor may use a short individual check or targeted question during the briefing.
