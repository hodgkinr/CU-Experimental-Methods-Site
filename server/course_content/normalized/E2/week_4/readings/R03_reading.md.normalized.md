# Evaluating a Validation Report — A Checklist for the Comparative Analysis Discussion
## What a credible validation report does that an inadequate one does not

Before you can evaluate someone else's validation report, you need a checklist grounded in the framework you have been building since Week 6. This reading organizes that checklist. It is written from the perspective of an evaluator — someone reading the report to determine whether its validation claim is credible — not from the perspective of the author defending it.

This is the reference document for the Week 9 in-class comparative analysis discussion. The sample report contains deliberate weaknesses. Your job is to identify them using the categories below, name the specific failure each represents, and propose what a corrected version would show.

---

## Category 1: The Prediction Commitment

A credible validation report documents that the model was committed before the data was collected. The key questions an evaluator asks:

- Is there a pre-experiment prediction with a specific numerical value or range?
- Is there a committed acceptance criterion with a stated threshold?
- Is the prediction dated or timestamped before data collection?

**Failure mode to look for:** The prediction is present but the acceptance criterion appears in the discussion section — after the data is analyzed. This is a signal that the criterion was chosen to match the outcome rather than to define what would constitute success in advance. The cure is a committed criterion in the pre-lab prediction document, signed before data collection begins.

**Also watch for:** The prediction matches the data suspiciously well across all conditions. A model calibrated to a dataset will fit it well. Without evidence that the model was committed before the data was collected, a good fit is evidence only of curve-fitting skill.

---

## Category 2: Residual Analysis

A credible validation report presents residuals explicitly, not just the overlay of prediction and data.

- Are residuals plotted versus the independent variable (not just shown as a percentage error)?
- Is the shape of the residual pattern described (random vs. systematic)?
- Is the residual magnitude compared to the propagated uncertainty band?

**Failure mode to look for:** R² reported as the primary validation metric without a residual plot. A high R² means the model explains variance in the data. It does not mean the residuals are random, and it does not mean the model is adequate for the intended use. A polynomial of sufficient degree achieves R² = 1 on any dataset. The diagnostic content is in the residuals, not the R² value.

**Also watch for:** Residuals described as "within scatter" or "within experimental error" without showing the uncertainty band. This qualitative assessment cannot be evaluated — the reader cannot tell whether the author's definition of "acceptable scatter" matches the propagated uncertainty or was chosen after examining the data.

---

## Category 3: Statistical vs. Engineering Significance

A credible validation report distinguishes between these two independent criteria.

- Is the acceptance criterion stated in engineering terms (a specific threshold with physical units and a stated intended use)?
- Is statistical significance tested separately from engineering significance?
- Does the report acknowledge cases where the two diverge?

**Failure mode to look for:** Statistical significance treated as validation. A p-value below 0.05 means that, under the null model and the test assumptions, a test statistic at least as extreme as the observed one would occur with probability below 0.05. It is not the probability that the result occurred by chance or that the null hypothesis is true. It also says nothing about whether the difference is large enough to matter for the intended use. Compare a confidence interval for the difference with a pre-specified engineering region.

**Also watch for:** Engineering significance asserted without a stated acceptance criterion. "The model agrees reasonably well" is not an engineering statement. "The model agrees within ±5%, and the design requirement is ±10%" is an engineering statement.

---

## Category 4: Uncertainty Budget and Calibration Status

A credible validation report documents the dominant uncertainty sources with a propagated budget.

- Are the dominant uncertainty sources identified and ranked?
- Is calibration uncertainty included in the budget (not just random measurement noise)?
- Is the calibration status of each primary sensor stated — date, interval, compliance?

**Failure mode to look for:** The uncertainty budget includes only Type A (random) uncertainty. Systematic sources — calibration uncertainty, model input uncertainty, environmental drift — are absent. This produces an artificially narrow uncertainty band that makes the model look better than the measurement system can actually support.

**Also watch for:** Calibration status listed as "calibrated" without documentation of when, by whom, and against what standard. "Calibrated" is not a calibration record. The record should include the calibration date, calibration interval, and the resulting uncertainty in the measurand.

---

## Category 5: Confidence Intervals

A credible report uses confidence intervals correctly and interprets them precisely.

- Are CIs computed from the standard error of the mean (not the standard deviation of individual measurements)?
- Is the confidence level stated explicitly?
- Are CIs interpreted as statements about the estimation procedure, not about the probability that the true value is inside a specific interval?
- For a two-result comparison, is the CI formed for the difference (Welch or paired as appropriate) rather than judged from separate-CI overlap?

**Failure mode to look for:** "There is a 95% probability that the true value is between X and Y." This is the Bayesian posterior interpretation, not the frequentist confidence interval. The frequentist interpretation is: "If we used this procedure on 100 experiments, 95 of the resulting intervals would contain the true value." These are not the same statement. The frequentist CI is a statement about the procedure, not about any specific interval.

**Also watch for:** Reporting the standard deviation of repeated measurements and calling it the confidence interval. The SD describes individual measurement scatter. The CI of the mean narrows as n increases, because more measurements improve your estimate of the mean.

---

## Category 6: Improvement Proposal Quality

A credible improvement proposal is grounded in the data and uncertainty analysis, not generic.

- Does the proposal name a specific sensor, parameter, model term, or test condition?
- Is the proposal motivated by something in the data: a residual trend, a dominant uncertainty source, a calibration gap?
- Does the proposal estimate the improvement quantitatively (even roughly)?

**Failure mode to look for:** "More trials would reduce uncertainty." This is always true and says nothing. A credible proposal is: "The load cell contributes 68% of the total uncertainty budget. Replacing the LCL-010 (u_cal = ±0.12 N) with a higher-precision alternative (estimated u_cal = ±0.03 N) would reduce the combined uncertainty by approximately 40%, which is sufficient to resolve the acceptance criterion at the current model-data discrepancy of 0.18 N."

---

## Summary: What Separates Credible from Inadequate

| Dimension | Inadequate | Credible |
|---|---|---|
| Prediction commitment | Present but criterion appears post-hoc | Committed criterion with date, before data |
| Residual analysis | R² only, or percent error only | Residual plot vs. independent variable, compared to uncertainty band |
| Statistical vs. engineering significance | p < 0.05 treated as validation | Both tested separately; divergence acknowledged |
| Uncertainty budget | Random noise only | All sources: random, calibration, model input |
| Calibration status | "Calibrated" with no documentation | Date, interval, compliance, propagated u_cal |
| CI interpretation | "95% probability true value is in range" | Correct frequentist statement |
| Improvement proposal | Generic ("more trials") | Specific, grounded in data, with rough quantitative estimate |

**For the discussion:** For each identified failure, state (1) the specific text or figure that shows the problem, (2) which category it falls into from the table above, and (3) what a corrected version would show. Observations without category names and proposed corrections do not count as analysis.

---

**The Takeaway:** A validation report is a credibility argument, not a results summary. Every claim in it is subject to the question: how do you know? The framework you have built in Weeks 6–9 — prediction commitment, residual analysis, uncertainty propagation, statistical comparison, calibration status — is the complete toolkit for asking that question systematically.
