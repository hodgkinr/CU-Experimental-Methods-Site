# Tier 3 Final Lab Assignment — Frequently Asked Questions

## Is this a real lab or a paper design?

It is a paper design. You are not expected to build and run the experiment during ASEN
3501. Design it with enough technical detail that someone could judge whether it is worth
building.

## Do I get to choose my own experiment?

Yes, within constraints. Your experiment must connect to a predictive model, produce
measurable data, have a plausible instrumentation path, and be narrow enough to design
well in the available time. The instructor may ask you to narrow, revise, or replace an
idea if it is too broad, unsafe, too expensive, or not tied to a model.

## Can two groups choose similar experiments?

Yes. Similar physical systems are allowed if the model question, instrumentation strategy,
or validation plan differs meaningfully. The process is what is being assessed.

## Do I have to buy hardware?

No. You may investigate hardware and include cost or availability in your feasibility
discussion, but purchase is not required. If you already own components or want to buy
low-cost parts for personal learning, keep them. They may be useful later in senior design
or independent projects.

## What counts as "beyond provided" for CLO 6?

Examples include a sensor not listed in the course catalog, a measurement method from a
paper or handbook, a relevant engineering standard, a manufacturer application note, a
different DAQ platform, a calibration method, or an analysis approach not directly handed
to you. You need to show that you found it, evaluated it, and explained whether it improves
your design.

## Can I use a chatbot to brainstorm ideas?

Yes. You may use AI tools to brainstorm experiment ideas, generate checklists, compare
options, or identify possible failure modes. You are responsible for verifying technical
claims using authoritative sources. Do not cite a chatbot as evidence that a sensor works,
a standard exists, or an equation is valid.

## What should I ask a chatbot?

Ask for alternatives, not answers. A useful prompt asks the chatbot to generate possible
experiment ideas, list assumptions, identify measurable quantities, suggest candidate
sensors, and name failure modes. Then you verify and choose. A polished chatbot response
that you cannot defend will hurt you in the oral defense.

Use `TIER3_ai_assistant_prompt.md` as a starting point. It is designed to make the chatbot
act like a design coach rather than a ghostwriter.

## Does my experiment need to be aerospace-specific?

It should be aerospace-relevant. That can mean the system itself is aerospace hardware.
It can also mean the measurement problem is common in aerospace contexts: thermal behavior,
vibration, power, thrust, flow, pressure, attitude dynamics, structural response, materials
testing, controls, or environmental effects.

## What if my experiment is too simple?

Simple is fine if the design reasoning is strong. A thermal or power experiment can be
excellent if the model, instrumentation, uncertainty analysis, and validation logic are
clear. A complicated experiment with vague measurement reasoning will not pass.

## What if my experiment is too ambitious?

Narrow it. You do not need to design an entire test campaign. Choose one model claim, one
or two primary response features, and a feasible measurement path.

## Do I need to use ASME V&V 10-2006?

Only when its computational solid-mechanics scope is relevant to your project. V&V 20 is
the ASME guide for CFD and heat transfer; PTC 19.1 and the GUM are the measurement-
uncertainty references used in this course. You must cite at least one relevant standard
or professional guide and one additional technical source, and explain what each source
contributes and what it does not establish.

## Do I need to do uncertainty analysis if no data are collected?

Yes. This is prospective uncertainty analysis. You estimate how well the proposed
measurement chain would perform before the experiment is built. This is one of the main
skills of the assignment.

## Do I need a Monte Carlo simulation?

Use Monte Carlo when it is appropriate: nonlinear equations, multiple uncertain inputs,
non-normal distributions, or a need to visualize the output distribution. If first-order
propagation is sufficient, explain why.

## What does "validation metric" mean in a paper design?

It is the numerical rule you would use to compare the future data to the model. Examples
include percent error in a primary response, normalized residuals, RMS error across a time
series, slope/intercept agreement in a regression, or whether a measured response falls
within a predefined uncertainty bound.

## What if I find that my proposed experiment would not be sensitive enough?

That can be a strong result if you show it clearly. You should then revise the design or
state exactly what would need to change: better sensor, different range, different test
condition, more repetitions, different response feature, or a narrower validation claim.

## How is this different from Tier 2's improvement proposal?

Tier 2 asks you to improve an experiment that was already given to you. Tier 3 asks you to
design the experiment from the start. You are responsible for the model question, the
measurement chain, the uncertainty, and the validation plan.

## What is the most common way to do poorly on this assignment?

Choosing an interesting topic but not turning it into a measurable, testable design. The
assignment is not asking for a project idea. It is asking for a defensible experimental
design and V&V plan.

## What is the most important habit to carry from Tier 1 and Tier 2?

Commit before measuring. Define what data should look like, what agreement means, what
uncertainty you expect, and what data pattern would change your mind before the experiment
is run.

---

*ASEN 3501 — Tier 3 FAQ | Course Weeks 12–15*
