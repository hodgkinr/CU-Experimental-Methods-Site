---
marp: true
theme: 3501
class: default
paginate: false
style: |
 @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css');
---

<!-- _class: title-slide -->

# Measurement Fundamentals & Formal Experiment Design
## ASEN 3501: Aerospace Experimental Methods | Week 1, Lecture 2

---

<!-- _class: default -->

# Measurement Is Model Realization

- Measurement is not passive data collection — it is model realization
- A sensor does not directly record physical truth — it produces an inference
- Transduction → signal conditioning → digitization → calibration: each step introduces error
- The voltage on your screen is a model of the physical quantity, realized through hardware
- Understanding this chain is prerequisite to knowing what your measurement tells you

<!-- Here is the most important concept in this lecture, and I want it to land early: measurement is not data collection. Measurement is model realization. When you place a sensor on a structure or a system, you are not directly recording a physical truth — you are producing an inference about the physical world through a chain of transduction, conditioning, digitization, and calibration assumptions. Every step in that chain introduces error. Every step reflects a modeling choice. The voltage you read on your screen is not the angular velocity or the force or the temperature — it is the output of a physical model of how your sensor responds to that quantity. If you do not understand that chain, you cannot know what your measurement is actually telling you. The physical modeling branch of the AMVF starts here — in this chain. -->

---

<!-- _class: flow -->

# The Transducer Chain

<div class="flow-row">
<div class="flow-step">
<span class="icon"><i class="fa-solid fa-microchip"></i></span>
<span class="step-label">Transducer Element</span>
</div>
<span class="flow-arrow">→</span>
<div class="flow-step">
<span class="icon"><i class="fa-solid fa-gears"></i></span>
<span class="step-label">Signal Conditioning</span>
</div>
<span class="flow-arrow">→</span>
<div class="flow-step">
<span class="icon"><i class="fa-solid fa-chart-area"></i></span>
<span class="step-label">A/D Conversion</span>
</div>
<span class="flow-arrow">→</span>
<div class="flow-step">
<span class="icon"><i class="fa-solid fa-file-csv"></i></span>
<span class="step-label">Recorded Value</span>
</div>
</div>

<!-- The transducer chain is the sequence of physical and electronic processes that converts a real-world quantity into a recorded number. It starts at the phenomenon you care about — a force, a temperature, an angular velocity — and ends in a file somewhere on your computer. Every stage in between is a transformation, and every transformation can introduce error. The transducer converts energy from one form to another: a piezoelectric crystal produces voltage in response to strain, a thermocouple generates voltage proportional to temperature difference, a MEMS accelerometer changes capacitance in response to inertial force. Signal conditioning amplifies, filters, and excites. The analog-to-digital converter discretizes the continuous signal. I will not go deep into sampling theory today — that is Week 7 in Phase II. But I want you to see this chain clearly right now, because when your measurement looks wrong, this chain is where you look for the cause. -->

---

<!-- _class: comparison -->

# What We Measure vs. What We Infer

<div class="tile-row">
<div class="tile">
<div class="tile-title">What the Sensor Reports</div>

- Voltage, resistance change, capacitance shift
- Directly recorded by the hardware at the transducer stage
- Accurate but not the quantity you care about
</div>
<div class="tile">
<div class="tile-title">What We Care About</div>

- Force, temperature, pressure — the physical quantity
- Inferred via calibration equation built on physical assumptions
- Inference fails if any assumption breaks down
</div>
</div>

<!-- Sensors almost never directly measure the quantity you care about. A strain gauge measures resistance change. A thermocouple measures voltage. A pressure transducer measures membrane deflection. What you actually want is strain, temperature, or pressure. The conversion from what you measure to what you infer is not automatic — it is a calibration equation built on physical assumptions. If any of those assumptions break down — the sensor drifts with temperature, the mounting point shifts, the electrical excitation fluctuates — the inference breaks too, even though the raw voltage reading is perfectly accurate. This is why calibration is not optional, and it is why I will ask you in every lab report to state explicitly what your sensor measured versus what you inferred from that measurement. The distinction is the beginning of experimental honesty. -->

---

<!-- _class: default -->

# Bias vs. Precision — Different Problems, Different Remedies

- Bias: systematic offset — consistent, directional, does not average away
- Sources: poor zeroing, bad reference junction, mechanical preload
- Precision: scatter of repeated measurements around the mean
- Low precision is reduced by more measurements, better isolation, tighter control
- Knowing which problem you have determines the solution

<!-- Bias and precision are two distinct properties of a measurement system, and they require completely different interventions. Bias is a systematic offset — every reading is shifted by a consistent amount in the same direction. A poorly zeroed load cell, a thermocouple with a bad reference junction, a sensor mounted with mechanical preload — these all introduce bias. Bias can sometimes be corrected by calibration against a known reference, but only if you have that reference. Precision is about scatter — how much do repeated measurements of the same quantity disagree with each other? High precision means your measurements cluster tightly even if they're all biased. Low precision means your measurements scatter widely. Knowing which problem you have determines the solution: bias problems call for better calibration; precision problems call for more repetition, better isolation, and better experimental control. You will characterize both in your Phase 1 experiment. -->

---

<!-- _class: default -->

# Installation Effects — The Silent Error Source

- Conduction error: sensor body conducts heat away from the measurement point
- Mounting stress: over-tightening alters mechanical boundary conditions at the gauge
- Electromagnetic interference: signal wires near power leads induce noise
- Installation errors often exceed the sensor's published specification error
- These are design choices made before data collection, not random events after

<!-- A sensor that has been perfectly calibrated in a laboratory can still produce terrible data if it is installed incorrectly in the field. Installation effects are the category of errors introduced by how and where a sensor is placed in the physical environment, and they are chronically underestimated by students and sometimes by professionals. Conduction error occurs when the sensor body conducts thermal energy away from the measurement point, pulling the reading toward ambient temperature. Mounting stress changes the mechanical state at the sensor location — a classic problem with strain gauges on thin or flexible structures. Electromagnetic interference is a signal contamination problem introduced by running wires near power sources. These are not exotic failure modes. They are routine problems in aerospace laboratory work, and your experimental design this week must anticipate them before you take the first reading. If you discover an installation effect after the data is collected, you have a confound — not a measurement. -->

---

<!-- _class: default -->

# Calibration Basics — What It Is and What It Is Not

- Calibration compares sensor output to a known reference and derives a correction equation
- Removes or reduces systematic bias across the measurement range
- A best-fit equation: Output = a·Input + b, applied to convert raw readings
- Calibration ≠ validation: calibration improves measurement fidelity
- Validation tests whether your model accurately predicts system behavior — distinct claim

<!-- Calibration is the process of comparing a sensor's output to a known reference standard and using that comparison to derive a correction equation — a scale factor, an offset, a polynomial fit. It removes or reduces systematic bias. If your force sensor reads five percent high across its full range, calibration corrects that. Calibration is a measurement activity — it improves the fidelity of what the sensor reports about the physical world. I want to be explicit about what calibration is not: it is not validation. Calibration tells you the sensor is correctly reporting the physical quantity. Validation tells you whether your model accurately predicts system behavior. These are different claims about different things, and we will develop this distinction carefully in Week 3. For now, just carry this: calibrating a sensor improves your measurement. It does not test your model. -->

---

<!-- _class: default -->

# Confounding Factors — Threats to Causal Inference

- A confounder causes the dependent variable to change for reasons other than your IV
- Can produce real, repeatable, statistically consistent effects unrelated to the study variable
- Airflow changes between trials, temperature drift altering material modulus — both confound
- Antidote: controlled conditions, documented environment, randomized trial order
- Identify at least one confounder in your design deliverable before any data collection

<!-- A confounding factor is anything that causes your dependent variable to change for reasons other than the independent variable you're manipulating. If you're measuring the period of a pendulum while someone opens a window, and the airflow changes the drag on the pendulum bob, that's a confound. If you're measuring structural deflection and the temperature in the lab changes between trials, altering the material modulus, that's a confound. Confounders are dangerous because they can produce real, repeatable, statistically consistent apparent effects that have nothing to do with the phenomenon you are studying. The antidote to confounding is experimental design: controlled conditions, documented environment, randomized trial order, and careful isolation of the variable you are trying to manipulate. One of the required elements of your Phase 1 design deliverable this week is to identify at least one confounding factor in your assigned experiment before you run it — because after you have collected the data is the wrong time to remember them. -->

---

<!-- _class: grid -->

# Formal Experiment Design — The Vocabulary

<div class="card-row">
<div class="card">
<div class="icon"><i class="fa-solid fa-question"></i></div>
<div class="card-title">Hypothesis</div>
<div class="card-body">Specific, falsifiable, causal: if [IV], then [DV], because [mechanism].</div>
</div>
<div class="card">
<div class="icon"><i class="fa-solid fa-table"></i></div>
<div class="card-title">Variables</div>
<div class="card-body">Independent, dependent, and controlled variables defined explicitly.</div>
</div>
<div class="card">
<div class="icon"><i class="fa-solid fa-arrows-left-right"></i></div>
<div class="card-title">Confounders</div>
<div class="card-body">Known confounders and how they are controlled or documented.</div>
</div>
</div>

<!-- Formal experiment design requires specific vocabulary, and I want to give you that vocabulary precisely. A hypothesis is a specific, falsifiable, causal statement — it is not a question, it is not a guess, and it is not a vague expectation. An independent variable is the quantity you intentionally change. A dependent variable is the quantity you measure in response. Controlled variables are the quantities you hold constant so they do not contaminate the relationship you are studying. Together these three elements define the scope of the experiment — they tell you and everyone who reads your report what you were actually testing. This week's Phase 1 design deliverable requires all three, along with a hypothesis and at least one identified confounder. Come to the lab session this week ready to write these down for your assigned experiment, because that design work is what drives everything that follows. -->

---

<!-- _class: comparison -->

# Hypothesis Quality — A Direct Comparison

<div class="tile-row">
<div class="tile">
<div class="tile-title">Weak Hypothesis</div>

- "If we change the input voltage, the measured power will change."
- Direction unspecified; no physical reasoning stated
- Not falsifiable in a useful sense — any change confirms it
</div>
<div class="tile">
<div class="tile-title">Strong Hypothesis</div>

- "If voltage increases from 3V to 9V at fixed R, power increases by a factor of nine (P = V²/R)."
- Quantitative prediction with physical mechanism stated
- Clearly falsifiable — a threefold increase would be a discrepancy to explain
</div>
</div>

<!-- The quality of your hypothesis determines the quality of your experiment. Let me show you exactly what I mean. The weak hypothesis — "if we change the input voltage, the power will change" — is technically true but scientifically useless. It predicts a directional change without specifying how much, and it gives no physical reasoning. If the power changes by five percent or by nine hundred percent, both confirm the weak hypothesis. The strong hypothesis specifies a quantitative prediction, states the physical mechanism, and is falsifiable in the sense that a specific measurement could clearly contradict it. If I measure a power increase of three-fold instead of nine-fold, I have a discrepancy I need to explain — and explaining it will teach me something. The strong hypothesis is the one worth testing. In your experiment design this week, your hypothesis must commit to a mechanism, not just a direction. -->

---

<!-- _class: default -->

# Connecting Your Design to the AMVF

- Hypothesis and procedure → Physical Realization node
- Sensor selection, installation plan, calibration → Experimental Measurement node
- MATLAB analysis and uncertainty propagation → Data Reduction node
- Final reported values with uncertainty → Experimental Outcomes node
- Comparison to the predictive model → Quantitative Comparison node

<!-- Before you leave this lecture, I want to draw the explicit connection between everything we just discussed and the AMVF from Lecture 1. Your hypothesis and experimental procedure map to the physical realization node. Your sensor selection, installation decisions, and calibration plan map to the instrumentation node. Your MATLAB analysis and uncertainty propagation map to data reduction. Your final reported values with uncertainty map to experimental outcomes. And your comparison to the predictive model maps to the quantitative comparison node. The Phase 1 design deliverable this week asks you to annotate an AMVF diagram with your actual design decisions at each node. That exercise is not bureaucratic — it is the most direct way to check whether every measurement decision you are making has a purpose in the framework and connects to the model you are trying to evaluate. -->

---

<!-- _class: closure -->

# Closure

You now have two foundational layers for this course: the AMVF gives you the structural map, and measurement fundamentals give you the language for what happens at every node on that map. Measurement is not passive data collection — it is an active chain of physical and electronic modeling choices that each carry their own error. Designing an experiment means anticipating that chain before you run it: writing a hypothesis that commits to a mechanism, identifying what you are measuring versus what you are inferring, and naming the confounders before they corrupt your result. This week's design deliverable is intentionally simple — the discipline of doing it carefully is not. The habits you build this week — hypothesis-first, confounder-aware, AMVF-connected — are the habits of a test engineer, and this is where they begin.

---
