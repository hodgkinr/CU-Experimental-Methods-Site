# ASEN 3501 — Tier 2 Lab Assignment
## Predict, Execute, Analyze, Improve

**Segment:** E2 — Predictive Modeling & Comparative Validation
**Weeks:** 6–10
**CLO Alignment:** CLO 1, CLO 2, CLO 3, CLO 4, CLO 5, CLO 6
**Structure:** Group of ~3 — Pre-lab prediction → Lab execution → Analysis → Presentation
**Assessment:** Group report + quad chart presentation (5 min talk + 5 min Q&A) + peer evaluations

---

## What This Assignment Is

The Tier 2 assignment is the primary lab sequence of E2. Every group completes the same
assignment. The specific experiment differs — you will be assigned one of the Tier 2 canned
aerospace experiments — but the analytical framework, the deliverables, and the expectations
are identical for all groups regardless of which experiment is assigned.

This is a different kind of assignment than Tier 1. In Tier 1, you executed an experiment
and analyzed the data, and separately, you predicted someone else's experiment from specs.
Those were two separate activities. In Tier 2, they are one. Before you touch any hardware,
your group must develop a predictive model, commit to a prediction, and show it to the
instructor or TA. Only then do you get on the equipment.

That requirement is not procedural gatekeeping. It is the point — and the reason goes beyond
grading. Predicting the data before you collect it is how you catch fundamental problems with
your experimental setup *before* you waste time running a broken experiment. Consider a
concrete example: suppose your group is using a differential pressure sensor with an accuracy
of ±1 kPa to estimate airspeed from a pitot-static probe, where the expected differential
pressures at your operating condition are on the order of 10 Pa. The sensor simply cannot
produce meaningful results in that configuration — its uncertainty is two orders of magnitude
larger than the signal. The correct way to catch this is to predict the data ahead of time:
run the numbers, propagate the uncertainty, and ask whether your sensor can resolve the
quantity of interest before you ever touch the equipment. The incorrect way is to pick a
sensor, run the experiment, stare at the data, and wonder why nothing makes sense — or worse,
assume the pitot-static probe must be broken and schedule additional run time to repeat an
experiment that was never going to work.

This is not a hypothetical concern. In industry, time on an experiment is expensive.
Professionally operated test equipment routinely costs thousands of dollars per hour of
run time, and that clock runs whether or not your group is prepared. Your employer will
not accept "we didn't think to check the sensor range" as the explanation for an unusable
dataset. The habit of building a quantitative prediction before the experiment begins —
and using that prediction to verify that the experiment is even capable of answering your
question — is one of the most practically valuable skills you will develop in this course.

A test engineer who cannot predict what the data should look like before the test runs is
not prepared to run the test. If your prediction is wildly wrong, you need to understand
why — before you collect data that you will later be unable to interpret. If your prediction
is right but your reasoning was vague, you got lucky and you know it.

The second thing that is different about Tier 2: after you have run the experiment and
analyzed the data, you are required to answer a question that Tier 1 only touched on:
**how would you improve this experiment?** This is not a reflection prompt. It is a
graded deliverable with the same analytical weight as the uncertainty analysis.

This improvement question is also the bridge to E3, where you will design your own
experiment from scratch. The central questions of experimental design are: what are you
trying to achieve, and how do you know your experiment is designed to give you that? Two
of the most powerful mental constructs for building that design intuition are exactly what
this course has been training: reverse-engineering an existing experiment to understand
what makes it work (the core learning outcome of the Tier 1 lab), and critically evaluating
an existing experiment to identify what would make it better (the core learning outcome of
the Tier 2 lab). Both are prerequisites to the harder task of designing something from
nothing.

---

## Your Assignment

You will be assigned one experiment from the Tier 2 experiment pool, in a group of
approximately three students. The assignment is experiment-agnostic: this document specifies
what you are expected to do and produce. The experiment-specific lab document (provided
separately) specifies the theory, system parameters, sensor suite, and DAQ configuration
for your particular experiment.

Read both documents before your pre-lab prediction session. If you have not read the
experiment-specific lab document before attempting the prediction, you will not be able
to produce a defensible prediction — and you will not be cleared to access the equipment.

**Come prepared — this is not optional.** There are two reasons, both real.

First, the practical constraint: this is a large class with limited equipment and limited
lab time. If your group is not ready to run the experiment during your allocated slot, we
cannot hold the line for you out of fairness to your classmates and to the paid personnel
who staff the lab. The slot will move on.

Second, and more important for your professional development: in industry, lack of
preparation is not an acceptable explanation for a failed experiment. Test time on
professional-grade equipment is expensive — often thousands of dollars per hour or more
once you account for the equipment, the facility, and the personnel. Your future employer
will not absorb that cost because a team member did not read the manual in advance. The
habit of thorough pre-experiment preparation is not a course requirement — it is an
employability skill.

---

## Assignment Timeline

| Phase | Activity | Format | When |
|---|---|---|---|
| Pre-lab | Develop group prediction | Documented, shown to TA/instructor | Before W6 or W8 lab session (see Canvas) |
| Lab | Run the experiment | In-lab | W6 and/or W8 lab sessions |
| Analysis | Complete uncertainty analysis, calibration review, improvement proposal | Out of class | W8–W9 |
| Report | Group lab report | Written, Canvas submission | Due W9 (see Canvas) |
| Presentation | Quad chart + 5+5 presentation | In-class | W10 |
| Peer evaluations | Written peer evaluations | Written, submitted same day | W10 |

---

## Phase 1 — Pre-Lab Prediction

### The requirement

Before your group accesses the equipment, you must show your prediction to the lab
instructor or TA. This is a required gate. Groups that arrive without a documented
prediction will be asked to develop one before they may proceed — that time comes out
of your lab session.

The prediction is a group product. All group members are expected to be able to explain
any part of it.

### What the prediction must contain

Your prediction document does not need to be polished. It can be handwritten, a MATLAB
script with outputs, or a brief typed document. It must contain all of the following:

**1. System response features**
What specific physical quantities do you expect to observe, and what are their expected
magnitudes or ranges? Be specific: not "the force will increase" but "we expect the thrust
force to reach approximately X N at operating condition Y, based on [physical reasoning]."
State the expected shape of any time-series outputs — where peaks occur, whether the
response is monotonic, where you expect transient vs. steady-state behavior.

**2. Theoretical model — confirm the derivation, show the working form**
The experiment-specific lab document provides the theoretical model for your experiment.
You are not expected to re-derive it from scratch. You are expected to confirm that
the derivation is reasonable and that you understand it well enough to use it.

Concretely, this means:
- Trace the key steps of the derivation. Identify the physical principles it applies
 (conservation laws, constitutive relationships, geometry). Confirm that the dimensions
 are consistent at each step.
- Identify the assumptions embedded in the model. Every analytical model makes
 simplifying assumptions — linearity, steady state, negligible losses, idealized
 geometry. Name at least two that apply to your experiment and note what conditions
 would cause them to break down.
- Extend the model as needed for your specific experiment conditions. The provided
 theory gives the general form. You may need to substitute in your specific geometry,
 operating condition, or boundary conditions to arrive at the numerical prediction
 your experiment will actually test. That extension is yours to do.

In the prediction document, show the final working equation with your values substituted.
If you needed to extend or adapt the provided theory to reach that equation, show how
you did it. If you cannot trace the steps or explain the assumptions, that is the signal
that you are not ready for the gate check — not a reason to skip the section.

**3. Estimated uncertainty in the primary derived quantity**
Using the sensor specifications from the experiment-specific lab document, apply first-order
error propagation to estimate the uncertainty in your primary output quantity before the
experiment runs. Identify which input dominates the uncertainty budget. State the result
as: *[quantity] ≈ [predicted value] ± [predicted uncertainty] [units].*

**4. Acceptance criterion**
Define the threshold that will tell you whether your prediction is confirmed. State it
numerically: "We will consider the prediction confirmed if the measured value falls within
±X% of our predicted value" or "if the measured result falls within our predicted
uncertainty bounds." The acceptance criterion must be committed before data is collected.

**5. Risk assessment**
Identify at least one anomalous data pattern — beyond random scatter — that would indicate
a model-form limitation rather than measurement noise. What would that pattern look like?
What would you investigate first if you saw it?

### What the TA/instructor is looking for

The gate check is not a quiz. The instructor or TA will review your prediction for:
- Specific, committed predicted values (not ranges so wide as to be unfalsifiable)
- A traceable connection between the theory and the predicted numbers
- A stated acceptance criterion
- Evidence that the group understands what "wrong" data would look like

A group that arrives with all five elements, even with modest numerical precision, will
be cleared. A group that arrives with vague qualitative statements ("we think it will go
up") will be asked to revise before proceeding.

---

## Phase 2 — Lab Execution

Follow the procedure specified in your experiment-specific lab document. The following
apply to all Tier 2 experiments regardless of which one you are assigned.

**Use MATLAB for data collection and processing.** All data files, processing scripts,
and figure generation must be in MATLAB. See the experiment-specific lab document for
DAQ configuration details.

**Record your prediction before you see any data.** Your pre-lab prediction document
is frozen at the point of the gate check. You may not revise it after the experiment
begins. If something unexpected happens during the experiment, document it in real time —
when it occurred, what changed, and what you observed. These notes are primary evidence.

**Note anomalies as they happen.** If the live data looks unexpected relative to your
prediction, write it down immediately. Do not wait until the post-processing phase to
interpret what happened. Real-time anomaly recognition is a test engineer competency,
and your real-time notes will be evaluated in the report. A useful field-note format:
*[time or condition] — [what was observed] — [how it differed from prediction] —
[immediate hypothesis].* Two sentences written during the experiment are worth more
than two paragraphs reconstructed afterward.

**Document the calibration status.** Before the experiment begins, record:
- The calibration date for each primary sensor (from the instrument documentation)
- The calibration interval specified by the manufacturer or the lab's calibration procedure
- Whether the current calibration is within the required interval

You will analyze this documentation in Phase 3. Record it now — it will not be available
for reconstruction after the fact.

> **Note if your lab session is in W6:** The formal lecture on calibration procedures
> and calibration uncertainty (E2 W8) occurs after your lab session. For W6 lab groups,
> focus on recording the calibration date and interval accurately — the analysis of what
> that documentation means for your result is a Phase 3 activity you will complete after
> W8. If you are unsure how to locate calibration documentation for your instrument, ask
> the TA before the experiment begins.

---

## Phase 3 — Analysis

### 3A — Prediction vs. outcome comparison

Compare your committed pre-lab prediction to the measured data using your pre-defined
acceptance criterion. The comparison must be numerical — state whether the acceptance
criterion was met, and by how much. If the criterion was not met, classify the discrepancy:
is it consistent with measurement uncertainty (random scatter bounded by your propagated
uncertainty), or does it suggest a model-form limitation (systematic trend, wrong shape,
wrong magnitude beyond the uncertainty bounds)?

Apply residual analysis: plot the residuals (measured minus predicted) over the relevant
independent variable. A residual plot with random scatter around zero is consistent with
measurement noise. A systematic trend in the residuals is evidence of model-form error —
the model is missing something structural. Identify which pattern you observe and articulate
its implication.

### 3B — Uncertainty analysis on the experiment's theory

This is the analytical core of Tier 2. The experiments in E2 involve more complex physical
models than the P=IV circuit of Lab 1 — multiple inputs, nonlinear relationships, and more
possible sources of error. Your uncertainty analysis must reflect that complexity.

Required:
1. **Partial derivative propagation** for the primary derived quantity — derive the uncertainty expression, substitute your measured values and instrument specifications, and compute u for your primary output. Show the derivation.
2. **Dominant error source ranking** — rank the top three sources of uncertainty by contribution to total uncertainty. Justify the ranking numerically.
3. **Monte Carlo simulation in MATLAB** — using the same instrument specifications as input distribution parameters, run a Monte Carlo simulation (minimum 10,000 samples) for your primary derived quantity. Plot the resulting distribution. Compare the Monte Carlo result to your partial-derivative result numerically — state whether they are consistent and explain any discrepancy.
4. **Interpretation** — does your uncertainty bound allow you to evaluate your acceptance criterion? That is: is the experiment sensitive enough, given the instrument suite, to distinguish model agreement from disagreement for the stated intended use? If not, what would need to change?

### 3C — Calibration status review

Using the calibration documentation you recorded during the lab session, answer the
following questions in 1–3 paragraphs:

1. Are the primary sensors within their calibration interval? State the calibration date, the required interval, and whether the current status is compliant.
2. If the calibration interval has elapsed — or if it is approaching — what is the practical consequence for your result? Propagate the calibration uncertainty (from the instrument documentation) into your primary output. Does the out-of-calibration condition make your result unusable for your stated intended use, or does the calibration uncertainty remain small relative to your total uncertainty budget?
3. State a conclusion: is the calibration status of this experiment adequate for the intended use, or should recalibration be performed before the next use?

This is an analysis section, not a lab activity. You are evaluating whether the existing
calibration is sufficient — not performing a new calibration.

### 3D — How would you improve this experiment?

This section has the same analytical weight as the uncertainty analysis. Vague suggestions
("use better sensors") will not receive credit. A specific, reasoned proposal grounded in
what your data revealed will.

Your group must address **at least two** of the following improvement categories. State
which categories you are addressing.

**(a) Instrumentation** — Would a different sensor, or a sensor with different
specifications, meaningfully reduce uncertainty in the primary output or enable measurement
of a quantity you could not access with the current suite? Be specific: name the
measurement quantity, identify the limitation of the current sensor, describe what
alternative would address it, and estimate what improvement in uncertainty you would expect.

**(b) DAQ and signal conditioning** — Is the current sampling rate adequate given the
signal bandwidth? Is the anti-aliasing filter cutoff appropriate? Would a different
channel configuration reduce noise? Justify any proposed change with a Nyquist argument
or noise analysis.

**(c) Experimental design** — Would a different test matrix (different operating
conditions, different number of trials, different range of the independent variable)
yield more informative data for model validation? For example: if your current data
covers a narrow range of the independent variable, the model comparison is only valid
in that range. A broader test matrix would extend the validation domain.

**(d) Model** — Does the residual analysis reveal a systematic trend that suggests the
current model is missing a physical effect? What physical effect would you add? What
additional measurement would you need to parameterize it?

**(e) Measurement strategy** — What additional quantity, if measured alongside the
current outputs, would most reduce uncertainty in the primary result or most directly
expose the model-form limitation you observed? Why is that quantity more informative
than what is currently measured?

There is no single right answer for any of these categories. The range of experiments in
the Tier 2 pool means that for some experiments, the dominant opportunity is in
instrumentation; for others, it is in the test matrix or the model. Your answer should
be grounded in your specific data and your specific uncertainty analysis — not in a
generic checklist.

---

## Deliverable 1 — Group Report

The group report is the primary written deliverable. All group members are responsible
for the full content.

### Required sections

**1. Pre-lab prediction (reproduced)**
Reproduce your committed pre-lab prediction: system response features, predicted values,
estimated uncertainty, acceptance criterion, and risk assessment. Do not revise it — if
the prediction turned out to be wrong, that is fine. The prediction is evidence of your
pre-experiment state of understanding.

**2. Experimental setup summary**
One paragraph describing what was measured, how, and under what conditions. Do not
reproduce the experiment-specific lab document — summarize it. Include a simple schematic
or block diagram if useful.

**3. Prediction vs. outcome comparison**
Numerical comparison using your pre-defined acceptance criterion. Residual plot with
systematic trend assessment. Classification of any discrepancy as measurement uncertainty
or model-form limitation, with physical reasoning.

**4. Uncertainty analysis**
The full analysis from Phase 3B: partial derivative derivation, dominant error source
ranking, Monte Carlo simulation with distribution plot, comparison of methods, and
interpretation of whether the experiment is sensitive enough for its stated intended use.

**5. Calibration status review**
The analysis from Phase 3C: calibration dates, interval compliance, propagated calibration
uncertainty, and conclusion on adequacy.

**6. How would you improve this experiment?**
The analysis from Phase 3D: at least two improvement categories addressed, each with a
specific proposal, physical or analytical justification, and connection to the data or
uncertainty analysis.

**7. MATLAB figures**
All figures must have: title, labeled axes with units, uncertainty bounds where applicable,
legend if multiple datasets, and a caption that states the takeaway in one sentence. Apply
the graph presentation framework from E1 W2. Figures without captions receive no credit.

**8. Conclusion**
Two to four sentences: what did the experiment reveal about the model, and is the model
adequate for the stated intended use? State the conclusion with uncertainty bounds — not
just "the model agreed."

### Format and submission

- Markdown or PDF submitted to Canvas as a group.
- Figures embedded in the document.
- Include a brief author contribution statement at the end — one sentence per group member
 describing their primary contribution.
- See Canvas for the due date.

---

## Deliverable 2 — Quad Chart Presentation

Your group will present using a single quad chart slide. The quad chart template
(PowerPoint file) is provided on Canvas.

**[PLACEHOLDER — quad chart PowerPoint template to be provided on Canvas]**

### Quad chart structure

| Top left | Top right |
|---|---|
| **Prediction vs. outcome** — your committed prediction overlaid on the measured data, with uncertainty bounds, and your acceptance criterion stated | **Uncertainty analysis** — dominant error source ranking and Monte Carlo distribution of the primary output |

| Bottom left | Bottom right |
|---|---|
| **Calibration status** — one-sentence conclusion on whether the current calibration is adequate, with the key number that supports it | **Top improvement recommendation** — your single most impactful proposed improvement, stated specifically, with the reasoning in one or two sentences |

Every cell of the quad chart must be self-contained — a reader who sees only that cell
should understand what it is showing. No cell should require reading another cell to
interpret.

### Presentation format

**5 minutes talk, 5 minutes Q&A.**

The talk should walk the quad chart in order: prediction vs. outcome, uncertainty analysis,
calibration status, top improvement. You do not need slides beyond the quad chart. You may
bring your group report as a reference document for the Q&A — the Q&A is where you will
be expected to answer questions that go deeper than the quad chart.

You will not know the exact questions in advance. Expect questions on: why you chose your
acceptance criterion, how you identified the dominant uncertainty source, what the Monte
Carlo distribution tells you that the partial derivative result does not, what physical
effect your residual trend suggests is missing, and what specifically would change if you
implemented your top improvement recommendation.

All group members are expected to be able to answer questions. The Q&A is not a division
of labor exercise.

### Peer evaluation

Every student in the audience completes a written peer evaluation for each presentation.
Your grade includes both your own presentation score and the quality of your peer
evaluations. The peer evaluation criteria are identical to Tier 1 — see
`TIER2_rubric_student.md` for the full criteria. A peer evaluation that says "good
presentation, nice figures" receives no credit.

---

## Resources

- E2 Week 6 Lecture: Why Prediction Must Precede Measurement
- E2 Week 6 Lecture: Formal Hypothesis Framing for Complex Systems
- E2 Week 8 Lecture: Model-Form Error & Discrepancy as Diagnostic Information
- E2 Week 8 Lecture: Calibration Revisited — Formal Procedure & Uncertainty Budget
- E2 Week 9 Lecture: Regression, Goodness-of-Fit & Monte Carlo for Multi-Variable Systems
- E2 Week 7 Lectures: Nyquist Sampling, Signal Conditioning & DAQ Configuration
 (relevant for category (b) improvement proposals)
- Coleman & Steele, 4th ed. — uncertainty propagation reference
- Experiment-specific lab document (provided separately for your assigned experiment)
- Quad chart PowerPoint template — Canvas
- E0 Supplemental: AI Tutor Setup and Practice

---

*ASEN 3501 — Tier 2 Lab Assignment | E2 Weeks 6–10*
*Evergreen — structure, phases, analytical requirements, improvement categories*
*Update-friendly — experiment names, Canvas due dates, quad chart template,
TA gate-check logistics, specific acceptance criterion thresholds*
