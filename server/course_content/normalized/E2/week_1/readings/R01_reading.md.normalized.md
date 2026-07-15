# The Problem with Postdiction — Why Prediction Must Come First
## How hindsight bias turns curve-fitting into fake validation

The most dangerous validation failure in engineering looks exactly like success.

A team runs an experiment, collects data, and builds a model that fits the data beautifully. R² (a measure of how well the model's curve fits the data it was computed from) is high. The curves overlap. Everyone is satisfied. But here is what actually happened: the team saw the data first, then built the model to match it. What they produced was not a validated model — it was a very sophisticated description of the data they already had. The moment they call it "validated," they have committed one of the oldest epistemic errors in science: **postdiction**.

---

Postdiction is the practice of building a model *after* seeing the data and then treating the quality of the fit as evidence that the model is predictively valid. It feels like validation. It produces outputs that look like validation. But it is structurally indistinguishable from curve fitting — and curve fitting has no predictive content whatsoever. A polynomial of sufficient degree will fit any dataset perfectly. That does not mean the polynomial predicts anything.

![A side-by-side illustration contrasting genuine prediction and postdiction. On the left, a timeline arrow runs left to right: "Model developed" → "Experiment run" → "Data compared to prediction." A bold vertical line separates the model from the data, labeled "No data crosses this line." On the right, the same timeline but reversed: "Data collected" → "Model fit to data" → "Fit presented as validation." A double-headed arrow loops between the data and the model, labeled "Model adjusted until fit is good." Both panels show the same scatter plot of data and the same fitted curve — visually identical results — but one is prediction and one is postdiction. The contrast makes the invisible structural difference visible. Clean infographic style with black and gold color scheme.](../images/E2_W6_R1_image1.png)

The cognitive mechanism behind postdiction has been studied extensively in psychology. **Hindsight bias**, the tendency to believe after learning an outcome that you would have predicted it all along, is so deeply embedded in human reasoning that it operates even when people are explicitly warned against it. When you see data and then build a model, your brain cannot un-see the data. Every modeling decision you make is shaped by what you know the answer should look like. The model converges toward the data not because the physics demands it, but because your judgment is contaminated. Example: a team builds a model after seeing that their experiment produced a nonlinear curve. They are convinced they would have predicted the nonlinearity. They almost certainly would not have.

**Confirmation bias** compounds the problem as the second mechanism reinforcing the first. Once you have a model that fits the data, you notice the agreements and rationalize the discrepancies. Small systematic trends in the residuals become "experimental scatter." Anomalous points become "outlier runs." The model is right, and anything that says otherwise must be explained away. The validation report is filled with language like "agreement is within 10%, which is acceptable given the measurement uncertainty." The 10% tolerance was chosen after looking at the data, not before.

---

These failures are not hypothetical. The history of engineering is littered with models that were extensively "validated" against the same data used to build them, then broke down at the first encounter with conditions outside that dataset. Structural load models validated against data from the test specimens they were built on. Aerodynamic performance models tuned to match existing flight data and then used to predict configurations that behaved completely differently. In each case, the validation was sincere — the engineers believed it — and the failure was still catastrophic.

The insidiousness of postdiction is that it is invisible from the inside. If you have already seen the data, you cannot know how much your modeling choices were shaped by it. You cannot subtract the contamination. The only protection is structural: the model must be committed before any data is collected, and that commitment must be documented.

![A diagram showing two experimental timelines on parallel horizontal tracks. The upper track, labeled "Credible Validation," shows: System conceptualized → Predictive model built → Acceptance criterion written → Experiment run → Data compared. The lower track, labeled "Postdiction," shows: Experiment run → Data collected → Model fit to data → Acceptance criterion chosen to match → Claimed as validation. Both tracks produce the same endpoint — a report with a graph showing model and data overlapping — but the lower track is shaded in warning orange with the label "The commitment came after the data." The key label: "The sequence is the validation, not the fit."](../images/E2_W6_R1_image2.png)

This is why prediction-before-exposure is not a stylistic preference or an academic exercise. It is the mechanism that makes validation meaningful. A model that accurately predicts data it has never seen is evidence of something real. A model that fits data it was built on is evidence of nothing except the modeler's ability to adjust parameters.

---

This is the same discipline you practiced in Tier 1 Phase 2 — your prediction memo was due before data was released for exactly this reason. The discipline has a formal structure, and you will practice it throughout E2. Before any Tier 2 experiment is run, your group commits to a specific prediction: the expected value of the primary output quantity, the expected shape of the system response, the estimated uncertainty in your prediction, and a numerical criterion for what counts as adequate agreement. That commitment is documented, shown to the instructor or TA, and then frozen. It is not revised when the data comes in. It is not adjusted when the fit is off.

When the data is released in Week 8, you will compare your committed prediction to what was actually measured. If the agreement is poor — if your model missed — that is not a failed experiment. A poor prediction from a well-reasoned model is rich diagnostic information. It tells you something true about the physics that your model did not capture. That kind of information is useful. A "successful validation" produced by postdiction tells you only what you already knew.

In professional test engineering, prediction-before-exposure is not optional. A validation report that does not document when the model was committed relative to when the data was collected is not a credible validation report. It is an anecdote. The sequence — model first, data second — is the line between engineering analysis and storytelling.

---

**The Takeaway:** Postdiction is not a mistake you make by accident — it is a failure mode that feels exactly like success, and the only structural protection against it is committing your prediction, in writing, before the data exists. In E2, that commitment is a required gate, not a formality; understanding why it exists is what separates a test engineer from a curve-fitter. The Week 6 lectures walk through the mechanics of the prediction document itself — the five required elements and the gate procedure — if you want the structural detail behind this principle.
