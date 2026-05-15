---
marp: true
theme: 3501
class: default
paginate: false
style: |
 @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css');
---

<!-- _class: title-slide -->

# The Aerospace Modeling & Validation Framework
## ASEN 3501: Aerospace Experimental Methods | Week 1, Lecture 1

---

<!-- _class: comparison -->

# The Two Questions This Course Answers

<div class="tile-row">
<div class="tile">
<div class="tile-title">Is this prediction right?</div>

- Simulations and models generate quantitative predictions
- Prediction without validation is a guess with better vocabulary
- Experiments check whether the prediction holds
</div>
<div class="tile">
<div class="tile-title">Will this do what we want?</div>

- Physical testing confirms real-world system behavior
- Quantify how closely prediction and reality agree
- Know what to do when agreement fails
</div>
</div>

<!-- These two questions are the organizing logic of everything you will do in this course and, I would argue, a significant fraction of what you will be paid to do as aerospace engineers. Your other coursework builds your capacity to generate predictions — to say "based on this model, the system should behave like this." That skill is genuinely valuable. But prediction without validation is a guess with better vocabulary. The skill this course builds is the second half: using physical reality to check whether the prediction holds, quantifying how closely it holds, and knowing what to do when it does not. By the time you leave this course, you will be able to answer both questions with a number, a confidence interval, and a defensible argument. -->

---

<!-- _class: grid -->

# You Are Training to Be a Test Engineer

<div class="card-row">
<div class="card">
<div class="icon"><i class="fa-solid fa-calculator"></i></div>
<div class="card-title">Analyst / Modeler</div>
<div class="card-body">Generates predictions from mathematical and computational models.</div>
</div>
<div class="card">
<div class="icon"><i class="fa-solid fa-microchip"></i></div>
<div class="card-title">Instrumentation</div>
<div class="card-body">Designs sensor systems and measurement infrastructure.</div>
</div>
<div class="card">
<div class="icon"><i class="fa-solid fa-flask"></i></div>
<div class="card-title">Test Engineer</div>
<div class="card-body">Reads a model, designs the test, quantifies confidence, produces defensible conclusions.</div>
</div>
</div>

<!-- A test engineer is not someone who just runs experiments and records numbers — that is a technician. A test engineer is someone who reads a mathematical model, asks what that model is claiming about physical reality, designs a test that can confirm or refute that claim with quantified confidence, instruments it properly, propagates uncertainty through the data reduction, and produces a defensible conclusion. That is the full stack, and every activity in this course is practicing some piece of it. In Phase I you will walk the measurement and comparison steps. In Phase II you will add the predictive modeling and pre-commitment steps. In Phase III you will own the design from the beginning. All of it is test engineering. All of it is what employers will hire you to do. -->

---

<!-- _class: default -->

# The AMVF — Two Branches, One Validation Goal

- Left branch: conceptual → mathematical → computational model → simulation outcomes
- Right branch: physical realization → measurement → data reduction → experimental outcomes
- Both branches originate at the same system or phenomenon of interest
- Validation occurs where both branches converge at quantitative comparison
- Neither branch is credible without the other

<!-- This is the Aerospace Modeling and Validation Framework — the AMVF — and it is the organizing spine of this course. The left branch is what your other classes develop: you take a physical phenomenon, build a conceptual model, translate it into mathematics, run a simulation, and produce a prediction. The right branch is what this course teaches: you take the same phenomenon, design a physical realization of it, instrument and measure it carefully, reduce the data, propagate uncertainty, and produce an experimental outcome. Validation is what happens when both branches meet at the bottom of this diagram. The critical insight is that neither branch is complete without the other — a simulation without experimental grounding is an educated guess, and data without a model to compare against is just observation. The meeting point is where engineering credibility lives. -->

---

<!-- _class: comparison -->

# Verification vs. Validation — Not the Same Thing

<div class="tile-row">
<div class="tile">
<div class="tile-title">Verification</div>

- "Are we solving the equations correctly?"
- Internal consistency: does the code do what the math says?
- A perfectly verified simulation can still have completely invalid physics
</div>
<div class="tile">
<div class="tile-title">Validation</div>

- "Are we solving the right equations?"
- External correspondence: does the model represent physical reality?
- This course lives almost entirely in validation territory
</div>
</div>

<!-- Verification and validation are two distinct activities that get conflated constantly, and I want to be precise about this from Day 1. Verification asks whether we are solving the equations correctly — it is a question about numerical implementation, about whether the code faithfully represents the mathematics. Validation asks whether we are solving the right equations — whether the mathematical model actually corresponds to the physical phenomenon it claims to describe. You can write flawless, bug-free code that perfectly implements a model, and if that model has wrong physics in it, you have a perfectly verified, completely invalid simulation. This course lives almost entirely in the validation territory. The right branch of the AMVF is how we gather the physical evidence needed to answer the validation question. -->

---

<!-- _class: flow -->

# Outcomes vs. Results — A Distinction You Will Use Every Week

<div class="flow-row">
<div class="flow-step">
<span class="icon"><i class="fa-solid fa-microchip"></i></span>
<span class="step-label">Raw Sensor Output</span>
</div>
<span class="flow-arrow">→</span>
<div class="flow-step">
<span class="icon"><i class="fa-solid fa-gears"></i></span>
<span class="step-label">Data Reduction</span>
</div>
<span class="flow-arrow">→</span>
<div class="flow-step">
<span class="icon"><i class="fa-solid fa-table"></i></span>
<span class="step-label">Result</span>
</div>
<span class="flow-arrow">→</span>
<div class="flow-step">
<span class="icon"><i class="fa-solid fa-check-double"></i></span>
<span class="step-label">Outcome</span>
</div>
</div>

<!-- The AMVF maps physical measurements to experimental outcomes — not experimental results. These are not the same thing. A result is a number that comes out of your data reduction: 9.76 meters per second squared. An outcome is a result that also carries its uncertainty, a stated confidence level, and a method statement — 9.76 plus or minus 0.14 meters per second squared at 95% confidence, computed by partial derivative propagation. The distinction matters because the outcome is what allows comparison. Without the uncertainty bounds, I cannot determine whether 9.76 agrees with a model that predicts 9.81. With the bounds, I can make a defensible quantitative argument. From this point forward, every numerical claim you make in this course must be expressed as an outcome. -->

---

<!-- _class: default -->

# Uncertainty Is Mandatory — Here Is Why

- Same measured value: 44.1 N·m; model predicts 42.3 N·m
- Outcome A: 44.1 ± 0.4 N·m — gap exceeds uncertainty, significant discrepancy
- Outcome B: 44.1 ± 2.8 N·m — gap within uncertainty, agreement is defensible
- Same number, completely different engineering conclusions
- Uncertainty is not a footnote — it is the argument (ASME V&V 10-2006)

<!-- Here is the most important visual in this lecture. Both outcomes show the same measured value — 44.1 Newton-meters. The model predicts 42.3. Do they agree? The answer depends entirely on the uncertainty. In Outcome A, the uncertainty is tiny — the gap between 44.1 and 42.3 is much larger than the bounds, and I have a significant discrepancy I need to explain. In Outcome B, the uncertainty is larger — the gap falls within the bounds, and agreement is defensible. The same number, measured by the same instrument, leads to completely different engineering conclusions depending on the uncertainty. This is why uncertainty is not optional in this course, and it is why professional standards like ASME V&V 10-2006 require it. Uncertainty is not a sign of weakness. It is the argument. -->

---

<!-- _class: default -->

# Where Phase I Sits in the AMVF

- Phase I (Weeks 1–5): right branch only — physical modeling and quantification
- Mathematical model is given; your job is to execute the right branch with discipline
- Your work spans: physical realization → measurement → data reduction → outcomes
- A carelessly executed experiment cannot validate a good mathematical model
- Phase II adds predictive modeling; Phase III adds full design ownership

<!-- For the next five weeks — Phase I of this course — your job is to walk the right branch of the AMVF with discipline. The mathematical model is given to you. Your job is to take the physical phenomenon, design and execute the measurement, reduce the data, propagate your uncertainty, and produce an experimental outcome that can be compared to the model prediction. You are not designing the experiment from scratch yet — that is Phase III. You are not developing the mathematical model independently — that is Phase II. But Phase I is not just a warmup. The physical modeling branch is where experimental credibility is earned or lost. A perfectly good mathematical model cannot be validated by a carelessly executed experiment. Phase I builds the foundation everything else rests on. -->

---

<!-- _class: grid -->

# The AMVF Connects to Professional Engineering Standards

<div class="card-row">
<div class="card">
<div class="icon"><i class="fa-solid fa-check-double"></i></div>
<div class="card-title">ASME V&V 10-2006</div>
<div class="card-body">Guide for V&V in Computational Fluid Dynamics and Heat Transfer.</div>
</div>
<div class="card">
<div class="icon"><i class="fa-solid fa-crosshairs"></i></div>
<div class="card-title">AIAA Standards</div>
<div class="card-body">Aerospace measurement and reporting standards for experimental data.</div>
</div>
<div class="card">
<div class="icon"><i class="fa-solid fa-ruler"></i></div>
<div class="card-title">ASME PTC</div>
<div class="card-body">Measurement uncertainty standards for performance testing.</div>
</div>
</div>

<!-- The AMVF is not something invented for this class. It reflects a framework that appears throughout professional aerospace and mechanical engineering and that is grounded in published engineering standards. The primary anchor for this course is ASME V&V 10-2006 — the American Society of Mechanical Engineers' Guide for Verification and Validation in Computational Fluid Dynamics and Heat Transfer. You will be assigned a reading on this document this week, and it will be a reference throughout the course. The other standards on this slide — AIAA measurement standards, ASME measurement uncertainty standards — will be cited as we progress through the semester, and by Phase III you will be required to reference them in your V&V plan. Professional engineers do not make up their validation methodology from scratch — they anchor it to standards that the broader community recognizes. -->

---

<!-- _class: default -->

# The Experimentally Informed Model

- The goal of an experiment is not to confirm the model — it is to learn from comparison
- Discrepancy is not failure; it reveals what physics the model is missing
- A disagreement tells you what the model needs to account for
- Most valuable output: an experimentally informed model, updated by data
- This concept becomes the central deliverable in Phase II and Phase III

<!-- There is a common misconception I want to address on the first day: the goal of an experiment is not to confirm the model. The goal is to learn from the comparison. When your experimental outcome disagrees with the model prediction, that discrepancy is not a failure — it is information. It tells you what physics the model is missing, or what physical effect you did not account for in your experimental setup. The most valuable output of the right branch of the AMVF is not a verdict of "confirmed" or "rejected" — it is an experimentally informed model, one that has been updated based on what the data revealed. This concept runs through all five weeks of E1 and becomes the central deliverable in E2 and E3. In the first lab session this week, you will begin designing your canned experiment with this outcome explicitly in mind. -->

---

<!-- _class: default -->

# What the Next Five Weeks Look Like

- Week 1: Framework + Design — AMVF, hypothesis, experiment design deliverable
- Week 2: Uncertainty Tools — partial derivatives, Monte Carlo, confidence intervals
- Week 3: Quantitative Comparison — validation metrics, comparative analysis memo
- Week 4: Full Pipeline — hypothesis through AMVF annotation, largest E1 report
- Week 5: Cross-Prediction — predict an experiment you did not run; bridge to Phase II

<!-- Here is the Phase I arc at a glance. This week you design your experiment and annotate an AMVF diagram. Next week you acquire the mathematical tools for uncertainty quantification — partial derivatives, Monte Carlo, confidence intervals — and begin collecting data on your assigned canned experiment. In Week 3 you learn how to make a quantitative comparison argument using a named validation metric. Week 4 integrates everything into a complete pipeline from hypothesis to AMVF annotation — that is the biggest report of E1. Then in Week 5 you do something that changes how you think about experiments: before anyone releases the data, you construct a predictive model for an experiment you did not run and commit to a prediction in writing. That is the cognitive bridge into Phase II. Each week builds directly on the last — and you cannot skip steps. -->

---

<!-- _class: closure -->

# Closure

The Aerospace Modeling and Validation Framework is not a diagram you memorize and move on from. It is the decision-making structure that a test engineer returns to every time they need to argue that a result is credible — when they design an experiment, when they argue for or against agreement between data and model, and when they plan a V&V strategy for a complex system. Today you have seen where this course sits in that structure, why verification and validation are different things, and why uncertainty is not optional but mandatory. Over the next fifteen weeks you will internalize all of it — not by memorizing the framework but by using it, week after week, to make defensible engineering claims about physical systems. That is the skill employers pay for. That is what we are building together. Welcome to Aerospace Experimental Methods.

---
