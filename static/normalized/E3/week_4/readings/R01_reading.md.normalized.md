# Peer Evaluation and Engineering Critique Worksheet
## A technical critique is useful only when it names the evidence

A good critique does not sound impressive; it helps the next engineer make a better decision.

---

Week 14 asks you to evaluate experimental designs from two directions. First, you will evaluate peer oral defenses. Second, you may evaluate sample, prior-student, professional, or AI-generated experimental design work. Use the same technical standard for both. The question is not whether the work is polished, confident, or easy to like. The question is whether the design would produce data capable of informing the model claim it identifies.

<image description: A clean worksheet-style visual with two side-by-side panels. The left panel is labeled peer oral defense and shows a student presentation slide with callouts for hypothesis, instrumentation, uncertainty, and validation metric. The right panel is labeled sample or AI-generated design and shows a polished report page with the same callouts. A shared rubric bar underneath says same engineering standard, different source of work.>

Use the prompts below while you listen, read, or review. Write in complete but compact engineering sentences. Avoid praise that could apply to any presentation. Avoid critique that only says something is missing. Name the consequence: why does the missing or weak element affect model credibility, measurement quality, uncertainty, feasibility, or intended use?

## Part 1 - What Is Being Claimed?

**Model or decision being informed** — What model, requirement, parameter, design decision, or engineering question does this experiment address?

Response:

**Hypothesis testability** — Is the hypothesis specific enough that future data could support or challenge it? What exact result would count as a challenge?

Response:

**System response feature** — What quantity, trend, time-series feature, distribution, residual pattern, or threshold is being measured? Is it the right evidence for the model claim?

Response:

## Part 2 - Is The Measurement Chain Credible?

**Instrumentation adequacy** — Are the sensors matched to the required range, accuracy, bandwidth, environment, and installation constraints? Name the strongest instrumentation choice and the weakest one.

Response:

**DAQ, sampling, and filtering** — Is the sample rate justified by expected signal bandwidth? Is filtering or anti-aliasing addressed where it matters? Is DAQ range or resolution connected to uncertainty rather than just named?

Response:

**Calibration versus validation** — Does the design distinguish checking an instrument against a known reference from validating the predictive model against independent system behavior?

Response:

## Part 3 - Does The Uncertainty Support The Claim?

**Dominant uncertainty source** — What appears to dominate the uncertainty budget? Is the source identified with enough evidence to be believable?

Response:

**Adequacy conclusion** — Is the predicted uncertainty small enough to evaluate the acceptance criterion or intended-use decision? If the work does not answer this, say so directly.

Response:

**Validation metric and acceptance criterion** — Is the metric matched to the response feature? Is the criterion defined before data collection, and is it justified by intended use rather than convenience?

Response:

<image description: A compact critique matrix with rows labeled hypothesis, measurement chain, uncertainty, validation metric, feasibility, and model update. Columns are labeled evidence present, concern, consequence, and recommended improvement. One row is partially filled to show how a vague concern becomes an actionable engineering critique.>

## Part 4 - Feasibility, Safety, And Model Update

**Feasibility and safety** — Are resources, hazards, operating limits, time, and practical constraints specific enough that a reviewer could decide whether the experiment is buildable and responsible?

Response:

**Experimentally informed model update** — Does the design state what data pattern would change a parameter, assumption, boundary condition, or model form? If not, what update pathway is missing?

Response:

## Part 5 - Your Required Critique

**One specific strength** — Name one feature of the work that improves the design's credibility. Explain why it matters technically.

Response:

**One specific weakness or unresolved risk** — Name one issue that would most limit confidence in the design. Connect it to model, instrumentation, uncertainty, validation, feasibility, or communication.

Response:

**One actionable improvement** — Give one concrete change the team or author could make. A strong recommendation names what to change, where, and why it would improve the design.

Response:

## AI-Generated Or Sample Work Check

If the work being reviewed was AI-generated or otherwise supplied as sample work, add this final check:

- What looked plausible on the surface?
- What technical claim needed verification from a source?
- What was correct, incorrect, missing, or unsupported?
- What is the single most important revision before this work could be trusted?

Response:

---

**The Takeaway:** Your critique is graded on engineering judgment. Specific, evidence-based, actionable feedback is a technical contribution; generic approval or vague dissatisfaction is not.
