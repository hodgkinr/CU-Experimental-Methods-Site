# ASEN 3501 — Tier 1 Lab Assignment
## Forward Analysis, Reverse Prediction, and Combined Synthesis

**Segment:** E1 — Execution & Quantification
**Weeks:** Course Weeks 5–8
**CLO Alignment:** CLO 1, CLO 2, CLO 3, CLO 5
**Structure:** Three phases — Individual → Individual → Paired (→ Group of 4)
**Assessment:** Phase 1 report (individual) + Phase 2 prediction memo (individual) +
Phase 3 combined presentation (paired or group of 4)

---

## What This Assignment Is

The Tier 1 assignment is the primary lab sequence of E1. Every student completes all
three phases. The physical experiments differ: you'll be assigned a specific experiment
for each phase. But the analytical framework, the deliverables, and the expectations are
identical for all students, regardless of which experiment they're assigned.

Throughout all phases, use the course uncertainty convention in `E1_W2_R3_reading.md`:
put inputs on a standard-uncertainty basis before propagation and label every reported or
plotted interval by type, method, and coverage.

Read this document carefully before you touch any hardware. The structure is intentional,
and understanding why each phase exists will make each one more productive.

---

## Learning Goals

By the end of this assignment and its associated activities, you should be able to:

1. Execute an assigned experiment, record the relevant measurements in the required engineering format, and state a defensible uncertainty basis for each primary quantity.
2. Compare two sensor types or measurement methods for the same physical quantity and argue, with a named validation metric, whether the results are consistent enough for the intended use.
3. Build a blind prediction from theory, sensor specifications, and DAQ information before seeing data, then state what agreement threshold and anomalous pattern would matter.
4. Interpret discrepancies between prediction and measurement without post-hoc guesswork, using the comparison to identify model limitations, uncertainty drivers, and at least one experimentally informed improvement.
5. Synthesize evidence across two related experiments in a short technical presentation and explain what the predictions got right, what they missed, and why.

---

## Why Three Phases?

Most experimental courses ask you to run an experiment and analyze the data. That is Phase 1.
It's the natural order. It's also a good starting point, but that's only the beginning.

A test engineer's job is much more than collecting data and placing it on top of a prediction.
Before a test ever runs, a test engineer asks: *what should the data look like?* They build
a model of the experiment itself, accounting for the sensors, the data acquisition, and the
signal chain, then commit to a prediction. That prediction isn't decoration. It's used to
design the experiment. It determines whether the sensors can resolve the quantity of
interest, anticipates failure modes, and defines in advance what a meaningful result looks
like. The ability to watch data come in during a live test, immediately know whether it
matches expectation, and act on that in real time is one of the most important skills a
test engineer develops.

This course will get there. The full experimental design workflow, where your prediction
shapes the design of the test, is the focus of E3. For now, in E1 and E2, you are building
the foundational mindset: the habit of pre-committing to a prediction before you see the data.

This pre-commitment changes everything about how you interpret discrepancy. When you see
a gap between your model and your data, and you committed to the model *before* you saw
the data, you can't dismiss the gap as a modeling choice made after the fact. The gap is
real. You have to explain it.

That is Phase 2.

Phase 3 takes the prediction mindset one step further. You ran one experiment. Your partner
ran a different one. You each predicted the other's experiment before seeing the data: an
experiment you never ran, using only the setup description and sensor specs. This is
deliberate. The goal is not to mimic the full test engineer workflow, but to develop the
prediction-first mindset by working through it in the most challenging form: predicting an
experiment you have no direct experience with.

Think of Phase 3 as reverse-engineering the experiment. You are reconstructing what the data
should look like from the physics and the instrument chain alone, without the shortcut of
having been in the room when the data was collected. This mindset, building a forward model
before you have the answer, is exactly what you'll need when you design your own experiment
from scratch in E3.

The three-phase structure is not the actual workflow of a test engineer. It is a scaffold for
developing the mindset of one.

---

## Assignment Overview

### Phase 1 — Forward Analysis (Individual)

**What you are assigned:** One experiment from the Tier 1 experiment pool.
**What you do:** Execute the experiment, collect data, analyze uncertainty, compare to a
predictive model, and propose at least one experimentally informed model improvement.
**What you produce:** A Phase 1 Individual Report.
**When:** Course Weeks 5–7 (Sep 14 through Sep 30; see Canvas for your assigned experiment and specific due dates).

### Phase 2 — Reverse Prediction (Individual, Blind)

**What you are assigned:** A *different* experiment from the Tier 1 pool: one you did
not run in Phase 1.
**What you do:** Given only the theory, the sensor specifications, and the DAQ setup
description for this unfamiliar experiment, predict what the data should look like.
You do not have access to the actual data. You do not touch the hardware.
**What you produce:** A Phase 2 Prediction Memo, submitted before data is released.
**When:** Course Week 7 (prediction submitted before data release).

### Phase 3 — Combined Synthesis (Paired, with optional group of 4)

**Who you work with:** You'll be paired with a student who did the opposite assignment.
They ran your Phase 2 experiment as their Phase 1 and predicted your Phase 1 experiment
as their Phase 2.
**What you do:** Compare predictions to real data across both experiments. Identify what
the predictions got right, what they missed, and why. Synthesize across both experiments.
**What you produce:** A combined oral presentation (lightning talk). You and your partner
present together. If logistics allow, your pair joins one other pair for a group of 4
presentation.
**When:** Course Week 8, during the Tier 1 interview window on Monday, Oct 5 and Wednesday, Oct 7 (see Canvas for sign-up instructions).

---

## Phase 1 — Forward Analysis: Full Instructions

### The assignment in one sentence

Run your assigned experiment, characterize the uncertainty in your measurements, compare
your data to a predictive model, and use the data to improve that model.

### Before the lab session and during the lab session

Complete items 1–4 before you arrive; items 5–8 are in-lab steps. Items 1–4 aren't graded as a separate pre-lab deliverable. They're required inputs to your Phase 1 report, and students who arrive without them typically need significantly more time to complete the lab.

1. **Read the experiment-specific lab document** for your assigned experiment. This document (provided separately) contains the theory primer, sensor specifications, and equipment list for your experiment. It is not this document.
2. **Write a hypothesis**: a one-sentence, falsifiable prediction of the experimental outcome. A hypothesis is not "I think it will work." It is "I predict the measured value of [quantity] will be [value or range], because [brief physical reasoning]."
3. **Sketch an AMVF diagram** for your experiment. Map each step of your planned procedure to a node in the Aerospace Modeling & Validation Framework. You don't need to be perfect. You'll refine this after the lab.
4. **Identify your independent and dependent variables.** Identify at least one control condition and at least one potential confounding factor.
5. **Use at least two sensor types or measurement methods** to measure the same physical quantity. This is required, not optional. The comparison between sensors is part of the analysis.
6. **Record your measurements** using the correct format: value, units, uncertainty. Every measurement in your report must carry an uncertainty estimate with a stated basis (e.g., manufacturer spec, resolution, or statistical bound).
7. **Use MATLAB** for data collection, processing, and plotting. MATLAB Mobile is available for phone-based data acquisition where applicable to your experiment. The experiment-specific lab document will indicate whether MATLAB Mobile is used.
8. **Note anomalies in real time.** If your data looks unexpected, write it down immediately: when it happened, what changed, and what you observed. These notes are evidence.

### Phase 1 report — required sections

**1. Experimental design**
Hypothesis (from pre-lab), independent and dependent variables, control conditions, at least
one confounding factor identified and addressed.

**2. AMVF annotation**
Your annotated AMVF diagram, mapping each step of the actual procedure (not the planned one)
to a framework node. Note any steps that did not match your pre-lab plan.

**3. Theory — confirm the model and understand it**
The experiment-specific lab document provides a theoretical model for the physical phenomenon
you are measuring. You are not expected to re-derive it from scratch, but you are expected
to demonstrate that you understand it well enough to use it.

This means identifying the physical principle(s) the model applies and confirming that the
dimensions are consistent. Name at least one simplifying assumption the model makes, and
describe the condition under which that assumption would break down. Then show the working
equation with your specific experimental values substituted in. This is the prediction your
model makes for your particular setup. If you cannot do this, you are not ready to run the
analysis in the sections that follow.

**4. Measurement record**
Your recorded values for all primary measurements, with units and uncertainty for each.
Describe the basis for each uncertainty estimate. Present in a table.

**5. Multi-sensor comparison**
Side-by-side comparison of the measurements from your two sensor types or methods. Apply a
named validation metric to determine whether they agree. State the metric, the threshold,
and the conclusion numerically, not just visually.

**6. Uncertainty propagation**
For the primary derived quantity in your experiment: apply first-order error propagation
using partial derivatives to compute uncertainty. Identify and rank the dominant error
sources. Show your work.

**7. Model comparison**
Compare your experimental result (with uncertainty bounds) to your predictive model. Use a
named validation metric. State whether the comparison meets your pre-defined acceptance
criterion. Interpret any discrepancy: is it attributable to measurement uncertainty, model
form limitations, or both?

**8. Experimentally informed model**
Identify at least one way your experimental results suggest the predictive model should be
updated or refined. This isn't about accepting or rejecting the model. It's about using
the data to make the model better. Describe specifically what you would change, and what
physical reasoning supports that change.

**9. MATLAB figures**
All plots must have: title, labeled axes with units, legend if multiple datasets, uncertainty
bounds where applicable, and a caption that states the takeaway in one sentence. Apply the
graph presentation framework from E1 W2.

**10. Plain-language summary**
A 3–5 sentence summary of what you did and what your result means, written for a non-engineer.
This section belongs in your introduction or conclusion, not as an appendix.

**11. Predict-from-specs**
Using only the sensor specifications and DAQ configuration provided in your experiment-specific lab document for the primary sensor identified by the instructional team, estimate what the uncertainty in your primary derived quantity should be before you use any measured data.
Propagate the uncertainty from the stated spec-sheet parameters.
Sketch the expected output range with labeled axes and approximate uncertainty bounds.
This workflow is the conceptual foundation for Phase 2, where you will apply the same predict-from-specs procedure to a complete experiment you have never run.

### Phase 1 report — format and submission

- Length: No page limit. There is no credit for length. The value is in the quality of argument and the completeness of required sections.
- Format: LaTeX. Submit a single `.zip` archive containing your LaTeX source (`.tex` file(s) and any figure files) and the compiled PDF. Figures should be embedded in the compiled PDF.
- See **E0 Supplemental: Getting Started with Overleaf and LaTeX** if you haven't used LaTeX before.
- Submission: See Canvas for due date.

---

## Phase 2 — Reverse Prediction: Full Instructions

### The assignment in one sentence

Given only the theory, sensor specs, and DAQ configuration of an experiment you've never
run: predict what the data will look like, commit to that prediction in writing, and submit
it before you see any real data.

### What "reverse" means

In Phase 1, you followed the natural order: build the experiment, collect data, analyze it.
In Phase 2, the order is reversed. You start with the experimental setup on paper and work
backwards to the expected output. You are building a model of the experiment itself, not
just of the physical phenomenon. You are essentially reverse-engineering the experiment.

Note that in Phase 2 you are predicting the output of a single, specified sensor: the one
described in your experiment packet. Phase 1 required you to use two sensors and compare
them; Phase 2 is a prediction exercise, and your packet will identify which sensor and
configuration to base your analysis on. Use only that sensor's specifications for your
uncertainty propagation.

This requires you to think about:
- What physical quantity is being measured, and what is its expected range given the physical setup?
- What is the uncertainty in each sensor measurement, given the specs?
- How does that uncertainty propagate to the derived quantity?
- What would a time-series or distribution plot of the output actually look like, given those inputs?
- Where are the likely failure modes, and what could produce data that looks anomalous?

A test engineer answers these questions before the test runs. This is how you evaluate
whether an experiment is worth running and whether the sensors can resolve the quantity of
interest. It's also how you determine whether you'll be able to detect anomalies in real
time during the test.

### What you receive for Phase 2

You will receive a Phase 2 Experiment Packet for your assigned experiment.
The theory primer in that packet is the same document the students who ran the experiment received.
It contains:
- The theory primer for the experiment
- The sensor specifications (manufacturer datasheets or equivalent)
- The DAQ configuration (sample rate, resolution, channel assignments)
- A description of the physical setup and nominal operating conditions
- The hypothesis that the student who ran the experiment submitted in pre-lab

You do **not** receive: the actual data, any plots, any results, or any lab report from the
student who ran the experiment. Your prediction must be made entirely from the packet.

### Phase 2 prediction memo — required sections

**1. Predicted system response**
What do you expect the data to look like? Describe the expected trend, range, and key
features. For example: "I expect the measured angular velocity to increase from 0 to approximately X rad/s during the first 5 s, with a decay phase beginning around t = 7 s due to friction." Commit to specific values and ranges. Vague predictions are not predictions.

**2. Predicted uncertainty in the primary derived quantity**
Apply first-order error propagation using the sensor specifications from the packet.
Compute u for the primary derived quantity. Show the partial derivatives. State the result
as: *[quantity] = [predicted value] ± [predicted uncertainty] [units].*

**3. Predicted plot sketch**
Sketch (by hand or in MATLAB) what you expect a plot of the primary output quantity vs.
time (or vs. the independent variable) to look like, with uncertainty bounds included.
Label all axes with units. This sketch is your committed prediction.

**4. Dominant uncertainty sources**
List the top two or three sources of uncertainty in order of expected contribution.
Justify the ranking using your propagation results.

**5. Acceptance criterion**
Define a numerical acceptance criterion: if the actual data falls within [threshold] of
your predicted value, you will consider the prediction reasonably supported. State this threshold
before you see the data.

**6. Risk assessment**
Identify one or two scenarios that would produce anomalous data, not because of a faulty
experiment, but because of a model limitation or an edge case in the physics. Use the Week 3
anomalous-data-signature framework here: name what “wrong” would look like physically, not a
generic equipment-failure scenario. Describe what anomalous data would look like and what you
would investigate first.

**Submission:** The prediction memo is submitted through Canvas before the data release
date. Once submitted, the version you turn in is frozen for the blind comparison and is the
version that will be graded as your original commitment. After data is released, you are
encouraged to keep iterating on your thinking, but preserve the original memo and track how
your interpretation changes so the evolution of your reasoning remains traceable.

### Grading philosophy for Phase 2

**A prediction that turns out to be wrong, but was derived from sound physical reasoning
and committed uncertainty analysis, is more valuable than a prediction that turns out to be
right but was derived from vague intuition.**

The grade is on the quality of your reasoning, not the accuracy of your prediction. This
isn't arbitrary. It's the actual professional standard. An engineer who commits to a
wrong prediction for good reasons learns from the discrepancy and demonstrates a deeper
attempt at understanding. An engineer who gets lucky learns nothing durable from the result.

This philosophy will be stated explicitly in class before Phase 2 begins. If you have
questions about it, ask before you submit.

---

## Phase 3 — Combined Synthesis: Presentation Instructions

### The pairing

You will be paired with a student who has the complementary assignment set: they ran your
Phase 2 experiment as their Phase 1, and predicted your Phase 1 experiment as their Phase 2.
This means:
- You have the Phase 1 data for Experiment A
- Your partner has the Phase 2 prediction for Experiment A
- You have the Phase 2 prediction for Experiment B
- Your partner has the Phase 1 data for Experiment B

Phase 3 is the moment when these are compared.

### The presentation structure

Your paired presentation has three segments, delivered jointly. Aim for approximately
8–10 minutes total (instructor will confirm against enrollment and available class time).

**Segment 1 — Forward (each student presents their own Phase 1)**
Each student in the pair briefly presents their own experiment: what they measured, what
their result was, and what it revealed about the system. 2–3 minutes per student.

**Segment 2 — Reverse (each student presents their prediction of the other's experiment)**
Each student presents their Phase 2 prediction for the other's experiment: what they
expected, what the acceptance criterion was, and then what the actual data showed.
Did the prediction hold? Where did it diverge? Why? 2–3 minutes per student.

**Segment 3 — Synthesis (presented jointly)**
The pair synthesizes across both experiments. This is the most important segment and will
likely be the most distinctive across presentations. What do these two experiments together
tell you about the physical phenomena, the models, or the measurement approach that neither
experiment alone could tell you? If you were designing a follow-on test, what would you
change and why? 2–3 minutes for the pair.

*One useful starting point for Segment 3: what assumption does your experiment’s model make
that the other experiment’s model also makes, and where do those assumptions diverge?
The most interesting synthesis often lives in that gap.*

### Group of 4 (if applicable)

If resources and enrollment allow, your pair will be combined with another pair that worked
on the same two experiments. The group of 4 presents jointly. Each pair presents Segments
1 and 2 from their own perspective, and the full group of 4 delivers Segment 3 together.
This creates a richer synthesis: four data points, four predictions, two experiments.

The instructor will confirm whether group-of-4 presentations are scheduled for your section
before the Course Week 8 interview window.

### Peer evaluation

Every student in the audience completes a written peer evaluation for each presentation.
Your grade includes both your own presentation score and the quality of your peer evaluations.
A strong peer evaluation: names a specific strength with evidence, names a specific weakness
with evidence, and gives a concrete and actionable improvement recommendation. Vague
evaluations ("good job, maybe add more data") receive no credit.

**See the Tier 1 student rubric in this assignment package for the presentation rubric and peer evaluation criteria.**

---

## Assignment Timeline Summary

| Phase | Activity | Format | When |
|---|---|---|---|
| Release | Tier 1 assignment released | Canvas / course site | Course Week 5, Monday Sep 14 |
| Phase 1 | Run experiment, analyze data | Lab sessions | Course Weeks 5–7 |
| Phase 1 | Individual report | Written, Canvas | Due before the Course Week 8 interview window (see Canvas) |
| Phase 2 | Receive experiment packet | — | Course Week 7 release date |
| Phase 2 | Prediction memo (submitted before data release) | Written, Canvas | Course Week 7 deadline (before data release) |
| Phase 3 | Paired presentation / interview | In-person, in lab | Course Week 8: Mon Oct 5 and Wed Oct 7 |
| Phase 3 | Peer evaluations | Written, submitted same day | Course Week 8: Mon Oct 5 and Wed Oct 7 |

---

## Resources

- E1 Week 2 Lecture: Error Propagation, Sensitivity Analysis & Monte Carlo
- E1 Week 3 Lecture: Structured Comparison & Validation Metrics
- E1 Week 3 Reading: How to Present a Graph — Kathryn's Framework
- E1 Week 4 Lab: Full Phase I Pipeline (this is Phase 1 of the Tier 1 assignment)
- E1 Week 5 Discussion: Lightning Talks & Peer Assessment
- E0 Supplemental: Technical Writing Basics and Presentation Best Practices
- E0 Supplemental: AI Tutor Setup and Practice
- E0 Supplemental: Getting Started with Overleaf and LaTeX
- Experiment-specific lab document (provided separately for your assigned experiment)
- Coleman & Steele, 4th ed. — reference for uncertainty propagation

## Student Package Note

Use this assignment together with the **Tier 1 student rubric** included in the student-facing assignment package. The rubric gives the pass criteria and evidence standards for the written report, prediction memo, presentation, and peer evaluations.

---

*ASEN 3501 — Tier 1 Lab Assignment | Course Weeks 5–8*
*Evergreen — structure, phases, analytical requirements*
*Update-friendly — experiment names, Canvas due dates, group of 4 logistics,
experiment packet contents*
