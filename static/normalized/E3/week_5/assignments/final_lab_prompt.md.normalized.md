# ASEN 3501 — Tier 3 Final Lab Assignment
## Paper Experimental Design and V&V Plan

**Segment:** E3 — Experimental Design & V&V Planning
**Weeks:** 11–15
**CLO Alignment:** CLO 1, CLO 2, CLO 3, CLO 4, CLO 5, CLO 6
**Structure:** Student-chosen paper design — proposal → instrumentation plan → V&V plan → oral defense → reflection
**Assessment:** Written design artifacts + oral defense + peer evaluations + CLO 6 reflection

---

## What This Assignment Is

The Tier 3 final lab is the culminating assignment of ASEN 3501. Unlike Tier 1 and Tier 2,
you will not be assigned a fully specified experiment. You will design one.

This is a paper design assignment. You are not expected to build and run the experiment
during this course. You are expected to produce a technically defensible experimental
design and V&V plan: a plan detailed enough that a knowledgeable engineering team could
decide whether the experiment is worth building, what hardware it would require, what
data it would produce, and whether those data would be capable of informing the predictive
model you care about.

The physical systems will differ across students and groups. One design may involve
thermal behavior, another structural vibration, another power measurement, another
attitude dynamics, another propulsion or fluids measurement. The equations will differ.
The process is the same.

You will:

- define a predictive model claim or engineering question;
- design an experiment that would produce data relevant to that claim;
- identify variables, controls, confounding factors, and a feasible test matrix;
- select instrumentation and DAQ/signal-conditioning choices;
- predict measurement performance using uncertainty analysis;
- define validation metrics and acceptance criteria before any data would be collected;
- cite standards, handbooks, manufacturer specifications, and prior art;
- investigate at least one method, sensor, or platform beyond the provided course resources;
- defend the design orally to a technical audience.

This assignment evaluates your process. A polished idea with vague reasoning does not pass.
A modest experiment with a clear model, defensible instrumentation, quantified uncertainty,
and honest limitations can be excellent.

---

## Why This Assignment Exists

In Tier 1, you learned to execute and analyze experiments. In Tier 2, you learned to predict
before measuring, compare results to models, interpret discrepancy, and propose improvements
to an existing experimental setup.

Tier 3 asks you to take ownership of the step that comes before all of that:

> What experiment should be run in the first place?

That question is harder than it sounds. An experiment is not valuable because it produces
data. It is valuable because it produces data that can inform a model, reduce uncertainty,
expose a limitation, or support an engineering decision. A test engineer has to decide
what to measure, how accurately it must be measured, what hardware can do the job, what
data patterns would matter, and what conclusion would actually be justified.

This is also the main CLO 6 demonstration in the course. You must go beyond the methods
and instrumentation handed to you by the instructor. That does not mean inventing a
capstone-scale project. It means showing independent professional judgment: finding
resources, evaluating options, comparing alternatives, and explaining why your choices
are appropriate for your experiment.

---

## Assignment Overview

### Phase 1 — Experimental Design Proposal

**What you do:** Choose an experiment idea, connect it to a predictive model, state a
formal hypothesis, identify variables and confounders, and summarize relevant prior art.

**What you produce:** Preliminary Experimental Design Proposal.

**When:** Week 11.

### Phase 2 — Instrumentation Justification

**What you do:** Select sensors, DAQ configuration, signal conditioning, sampling strategy,
and at least one beyond-provided hardware or method alternative.

**What you produce:** Instrumentation Justification Report.

**When:** Week 12.

### Phase 3 — Full V&V Plan

**What you do:** Assemble the full experiment design into a V&V plan, including system
response features, validation metrics, acceptance criteria, prospective uncertainty
analysis, calibration-vs-validation distinction, AMVF annotation, and safety/test-plan
considerations.

**What you produce:** Full V&V Plan Document.

**When:** Week 13.

### Phase 4 — Oral Defense and Peer Review

**What you do:** Defend your experimental design to a technical audience and evaluate
other students' designs using a structured rubric.

**What you produce:** Oral defense presentation and written peer evaluations.

**When:** Week 14.

### Phase 5 — CLO 6 and Course Reflection

**What you do:** Explain what you investigated beyond the provided course materials and
how your understanding of uncertainty, prediction, and validation changed across the course.

**What you produce:** CLO 6 Reflection and Course Reflection.

**When:** Week 15.

---

## Choosing Your Experiment

Your experiment must be open-ended enough to require design judgment but bounded enough
to support a defensible paper design in the time available.

A passing experiment idea has:

1. **A predictive model.** There must be an equation, simulation, scaling law, empirical
 model, or physical argument that predicts something measurable.
2. **A measurable system response.** You must identify what quantity or feature the
 experiment would measure.
3. **A validation purpose.** You must explain how the data would inform, challenge, or
 improve the model.
4. **A feasible measurement path.** You must identify plausible sensors, DAQ needs, and
 test conditions.
5. **A bounded scope.** The experiment must be designable on paper within this course.

The course will provide a catalog of available resources and suggested starting points:
example physical systems, available lab resources, common sensor types, data acquisition
options, standards and handbooks, prior course examples, and approved reference links.
You may use these resources directly, adapt them, or propose a different experiment.

You may use a chatbot or other AI tool to brainstorm experiment ideas, compare sensor
options, draft checklists, or identify possible failure modes. You are responsible for
every technical claim in your submission. If an AI tool suggests a sensor, equation,
standard, or design option, you must verify it using a reliable source before using it
as evidence.

An optional starting prompt is provided in `TIER3_ai_assistant_prompt.md`. Use it to
generate and stress-test ideas, not to produce final assignment prose.

---

## Phase 1 — Experimental Design Proposal

### Required sections

**1. Problem statement and intended use**
State the engineering question. What model, decision, or design context motivates the
experiment? What would the results be used for?

**2. Predictive model**
Describe the model your experiment is meant to inform. Include the governing equation,
simulation output, empirical relation, or physical reasoning. Identify at least two
assumptions in the model and one condition under which each assumption could fail.

**3. Formal hypothesis**
State a falsifiable hypothesis. It must specify what you expect the experiment to show,
what data would support that expectation, and what data would challenge it.

**4. System response features**
Identify the specific quantities, trends, distributions, or time-series features the
experiment would measure. Give expected values or ranges where possible.

**5. Variables, controls, and confounders**
Identify independent variables, dependent variables, controlled variables, and at least
three plausible confounding factors. Explain how the design would control, randomize,
block, or document them.

**6. Prior art and standards**
Cite ASME V&V 10-2006 and at least one additional relevant standard, handbook, datasheet,
technical manual, or prior publication. Annotate each source: what does it contribute to
your design?

**7. Initial test matrix**
Propose a small, feasible test matrix: conditions, repetitions, and what each condition
is intended to reveal. Include replication or repeated measurements where appropriate.

---

## Phase 2 — Instrumentation Justification Report

### Required sections

**1. Measurement chain**
Draw or describe the full measurement chain from physical quantity to reported data:
physical phenomenon → sensor/transducer → signal conditioning → DAQ → processing →
reported quantity.

**2. Sensor selection**
Select sensors for each primary measurement. For each sensor, cite specifications from a
manufacturer datasheet, standard, handbook, or other reliable source. Discuss range,
resolution, accuracy, bandwidth, installation effects, environmental sensitivity, and
cost or availability where relevant.

**3. DAQ and signal conditioning**
Specify sample rate, DAQ range/resolution, channel configuration, filtering or anti-aliasing
strategy, gain, grounding/shielding considerations, and synchronization/triggering if
needed. Justify sampling rate using expected signal bandwidth and Nyquist reasoning.

**4. Prospective uncertainty analysis**
Before the experiment exists, estimate the expected uncertainty in the primary output.
Use first-order error propagation where appropriate. Use Monte Carlo simulation when the
model is nonlinear, multi-input, or distribution assumptions matter. Identify dominant
uncertainty sources.

**5. Sensitivity and adequacy**
State whether the proposed measurement chain is sensitive enough to evaluate the acceptance
criterion from your design proposal. If not, revise the design or explain why the proposed
experiment is not adequate.

**6. Beyond-provided-method investigation**
Investigate at least one sensor, measurement method, platform, standard, or analysis
approach beyond the provided course catalog. Compare it to your baseline option. Explain
whether it improves the design, is unnecessary, is infeasible, or changes your thinking.

---

## Phase 3 — Full V&V Plan Document

The V&V plan is the primary written deliverable of Tier 3. It should read like a coherent
engineering document, not a stack of disconnected homework answers.

### Required sections

**1. Executive summary**
One page maximum. State the experiment, model, measurement strategy, primary uncertainty
result, validation metric, and conclusion on whether the design is adequate for its
intended use.

**2. Experiment purpose and intended use**
Explain what decision or model question the experiment informs. State what would be learned
from running it.

**3. Predictive model and assumptions**
Present the model, assumptions, expected outputs, and likely model-form limitations.

**4. Experimental design**
Describe variables, controls, confounders, test matrix, replication, randomization or
blocking where applicable, and planned operating conditions.

**5. Instrumentation and DAQ plan**
Summarize sensors, DAQ configuration, signal conditioning, sampling, filtering, and
installation considerations.

**6. Calibration vs. validation**
State what would need to be calibrated, how calibration status would be documented, and
which parts of the experiment are validation activities rather than calibration activities.

**7. Uncertainty analysis**
Present the prospective uncertainty analysis. Include equations, assumptions, dominant
sources, MATLAB outputs or plots, and interpretation. Do not report uncertainty without
explaining what it means.

**8. Validation metrics and acceptance criteria**
Define the numerical metric(s) used to assess model-experiment agreement. State acceptance
criteria before data collection. Justify why those criteria are meaningful for the intended
use.

**9. Expected residuals and risk assessment**
Describe what data would look like if the model is adequate. Then describe at least two
specific anomalous data patterns that would suggest model-form error, measurement error,
poor calibration, aliasing/noise, or uncontrolled confounding.

**10. Experimentally informed model update**
State how the experimental results would be used to update the model. What parameter,
assumption, boundary condition, or functional form might change? What data pattern would
trigger that change?

**11. AMVF annotation**
Map your design to the Aerospace Modeling & Validation Framework. Show how the model,
experiment, uncertainty analysis, validation metric, and model update fit together.

**12. Safety, resources, and feasibility**
Identify hazards, required equipment, approximate cost or availability, time requirements,
and practical constraints. A paper design can still be infeasible; identify those limits
honestly.

**13. References**
Cite all standards, handbooks, datasheets, papers, manuals, and AI-assisted resources used.
AI tools are not authoritative sources. Cite them only as process aids if required by
course policy; verify technical claims elsewhere.

---

## Phase 4 — Oral Defense

Your oral defense is a technical defense of your design, not a project pitch.

### Presentation format

See Canvas for exact timing. Expect approximately 10–12 minutes of presentation followed
by Q&A.

Your presentation must answer:

1. What model or decision does this experiment inform?
2. What would be measured, and why those quantities?
3. Why are the selected sensors and DAQ choices adequate?
4. What uncertainty do you expect, and what dominates it?
5. What validation metric and acceptance criterion would be used?
6. What data pattern would tell you the model needs to change?
7. What did you investigate beyond the provided course resources?

### Q&A expectation

Every team member must be able to defend the design. You may use notes, but you may not
read answers directly from the written plan. The point of Q&A is to test whether you
understand the reasoning behind your design choices.

---

## Phase 5 — Reflections

### CLO 6 Reflection

Describe the method, sensor, platform, standard, or resource you investigated beyond the
provided course materials. Your reflection must answer:

1. What did you investigate and why?
2. What sources did you consult?
3. What did you find?
4. Did it change your design? If not, did it strengthen your confidence in the original
 choice?
5. What does this investigation tell you about how you will approach unfamiliar measurement
 problems in professional practice?

### Course Reflection

Write a short reflection on how your understanding changed across the course. Address:

- uncertainty: what you misunderstood early and understand now;
- prediction: how committing before data changed your reasoning;
- validation: what it means to validate or evaluate a model;
- experimental design: what you would do differently if you were starting Week 1 again.

---

## Submission Format

Submit the following, according to Canvas deadlines:

1. Experimental Design Proposal
2. Instrumentation Justification Report
3. Full V&V Plan Document
4. Oral Defense Slides
5. Written Peer Evaluations
6. CLO 6 Reflection
7. Course Reflection

Unless otherwise specified, written documents should be submitted as compiled PDFs with
source files included when equations, figures, or MATLAB outputs are used. MATLAB scripts
used for uncertainty calculations must be submitted with the relevant deliverable.

---

## What Passing Work Looks Like

Passing work is specific, traceable, and honest.

It does not need to be expensive, flashy, or complicated. It does need to show that you
can design an experiment by reasoning from the model to the measurement chain to the
uncertainty to the validation claim.

A weak Tier 3 project says: "We would use better sensors and compare to theory."

A passing Tier 3 project says: "We need to distinguish a 6% change in the predicted
response. With the proposed sensor and DAQ chain, the propagated uncertainty in the
primary response is approximately 2.1%, dominated by sensor bias. That is small enough
to evaluate the acceptance criterion. If residuals show a monotonic trend with operating
condition, we would interpret that as model-form error rather than random measurement
noise and revise the assumed boundary condition."

That is the level of reasoning this assignment is designed to assess.

---

*ASEN 3501 — Tier 3 Final Lab Assignment | E3 Weeks 11–15*
