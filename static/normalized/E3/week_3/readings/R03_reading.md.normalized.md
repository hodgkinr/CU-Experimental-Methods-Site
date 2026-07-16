# V&V Plan and Oral Defense Worksheet
## Turn the plan into an argument you can defend out loud

A V&V plan is not finished when every section exists; it is finished when every section helps answer the same question.

---

By Week 13, you have a proposed experiment, an instrumentation plan, and a prospective uncertainty analysis. The task now is to assemble those pieces into one defensible engineering argument. The written **V&V plan** and the oral defense should tell the same story: this is the model claim, this is the evidence the experiment would produce, this is how agreement would be judged, and this is why the result would matter for the intended use.

<image description: A worksheet-style engineering document map. A central spine labeled V&V plan connects thirteen section cards: executive summary, intended use, model, experimental design, instrumentation, calibration versus validation, uncertainty, metrics, residual risks, model update, AMVF, safety, references. Arrows show intended use feeding metric, uncertainty feeding adequacy, and residuals feeding model update.>

Use this worksheet before you write the final plan and again before the oral defense. If you cannot answer a prompt in a sentence or two, the plan probably needs more engineering work before it needs more prose.

## Part 1 - Section-By-Section Plan Check

**1. Executive summary** — What is the experiment, what model does it inform, what is the primary uncertainty result, and is the design adequate for the intended use?

Notes:

**2. Purpose and intended use** — What decision, model question, or design context would this experiment support? What would the future data be used to decide?

Notes:

**3. Predictive model and assumptions** — What equation, simulation, scaling law, empirical relation, or physical argument predicts the response? Which assumptions are most likely to fail?

Notes:

**4. Experimental design** — What are the independent variables, dependent variables, controls, confounders, test matrix, repetitions, randomization, or blocking strategy?

Notes:

**5. Instrumentation and DAQ plan** — What sensors, signal conditioning, DAQ range/resolution, sampling rate, filtering, mounting approach, and environmental controls are specified?

Notes:

**6. Calibration versus validation** — Which activities check instruments against known references, and which activities compare model predictions to independent system behavior?

Notes:

**7. Uncertainty analysis** — What inputs enter the uncertainty model, what method is used, what dominates the result, and what does the result mean?

Notes:

**8. Validation metrics and acceptance criteria** — What numerical metric will judge agreement, and why is the acceptance criterion meaningful for intended use?

Notes:

**9. Expected residuals and risk assessment** — What data pattern would suggest model-form error, measurement error, poor calibration, aliasing/noise, or uncontrolled confounding?

Notes:

**10. Experimentally informed model update** — What parameter, assumption, boundary condition, or functional form could change after the experiment? What data pattern would trigger that change?

Notes:

**11. AMVF annotation** — Where do the model, physical experiment, data, uncertainty, comparison, and model update appear on the AMVF?

Notes:

**12. Safety, resources, and feasibility** — What hazards, resources, costs, availability limits, time limits, and operating constraints would a reviewer need to approve the test?

Notes:

## Part 2 - Common Failure Modes

Mark any box that applies, then revise before submission.

- [ ] The intended use is too vague to set an acceptance criterion.
- [ ] Sensor, DAQ, sampling, or filtering choices are named but not justified quantitatively.
- [ ] The uncertainty result is reported but not interpreted against the validation criterion.
- [ ] Calibration is treated as if it validates the model.
- [ ] The model-update pathway does not name what would change.
- [ ] Safety and feasibility read like boilerplate rather than a reviewable test plan.

<image description: A two-column oral defense rehearsal board. The left column is labeled claim I will defend and contains model, measurement, uncertainty, metric, feasibility, and CLO 6. The right column is labeled skeptical question and shows instructor-style prompts connected to each claim. A small clock icon indicates short, direct answers.>

## Part 3 - Oral Defense Question Bank

Practice answering these out loud. Use notes to prepare, but do not write a script.

1. What specific part of the predictive model does this experiment inform?
2. What intended use sets the required level of agreement?
3. Why is your selected response feature the right evidence?
4. Which instrumentation choice matters most to credibility?
5. How did expected bandwidth affect sample rate and filtering?
6. What dominates the uncertainty budget, and what would reduce it most?
7. Is the predicted uncertainty small enough for the acceptance criterion?
8. What residual pattern would suggest model-form error?
9. What needs calibration, and what is being validated?
10. What did you investigate beyond the provided course materials?
11. Which AI-assisted technical claim, if any, did you verify from an authoritative source?

## Part 4 - Final Readiness Test

Write the one-sentence version of your design argument:

"This experiment would inform [model/decision] by measuring [response feature] with [measurement chain], comparing it using [validation metric] against [acceptance criterion], with predicted uncertainty of [result], which is [adequate/not adequate] for [intended use]."

Your sentence:

---

**The Takeaway:** If the written plan and oral defense cannot be reduced to one coherent evidence argument, keep tightening. The goal is not more sections; the goal is a design a technical reviewer can trust.
