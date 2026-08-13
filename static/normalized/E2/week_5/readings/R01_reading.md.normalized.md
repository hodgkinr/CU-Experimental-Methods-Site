# From One Point to Many — Regression, Confidence & What They Don't Tell You
## Three statistical ideas that engineers consistently misapply — and what they actually mean

A high R² does not mean your model is right. A 95% confidence interval does not mean there is a 95% probability the true value is inside it. A statistically significant result does not mean the result is important. If any of those three statements surprised you, read carefully. Each represents a misuse common enough that you will see versions of it in reports, presentations, and sometimes even published technical work.

---

In E1, the statistical work focused on a single operating point: measure a quantity, propagate uncertainty through a formula, and report a result with bounds. The comparison was straightforward. Does the predicted value lie within the measurement's uncertainty interval? Week 9 extends this to a harder problem: comparing a model to experimental data across a range of conditions, with statistical rigor that says something truthful about whether the model is adequate.

Three tools dominate this work. Each is powerful. Each is routinely misapplied. This reading focuses on where the misapplications happen and what correct interpretation looks like.

---

## Regression: What R² Actually Measures

**Regression** is the process of fitting a mathematical relationship to a set of data points. It finds the line, curve, or model form that minimizes some measure of the distance between the model and the data. The most familiar result of a regression is the **coefficient of determination, R²**, which reports what fraction of the variance in the observed data is explained by the model.

R² = 0.97 sounds excellent. But R² cannot tell you whether the model is physically correct. A cubic polynomial fitted to data from a system that follows simple linear physics will have high R² because the polynomial is flexible enough to follow any smooth curve. That does not mean cubic dynamics are real. **Goodness of fit measures how well the model matches the data it was fitted to. It says nothing about whether the model would match data from a different experiment, a different operating range, or a different system.**

Look at the residuals. A model with R² = 0.97 but systematic trends in the residuals, such as positive values at low loads and negative values at high loads, is missing structural physics despite the high R². A model with R² = 0.82 but purely random residuals may be a better physical model. It may capture the right functional form even if parameter uncertainty prevents a tighter fit. The reading from W8 established this framework. Week 9 applies it across a full dataset rather than a single comparison point.

The correct practice: report R² alongside a residual plot, and let the residual plot carry the interpretive weight.

![A two-panel figure. Left panel: a scatter plot of measured data (circles) with two fitted curves — a solid line labeled "Model A: correct functional form, R² = 0.82" that tracks the data with small random scatter around it, and a dashed line labeled "Model B: polynomial fit, R² = 0.97" that tracks the data more tightly. Both curves appear close to the data. Right panel: two residual plots stacked vertically, one for Model A (random scatter around zero, small amplitude) and one for Model B (systematic S-curve trend around zero, similar amplitude). A caption reads: "R² favors Model B. Residuals reveal that Model A has better physical structure." Engineering plot style, clean black and white with labeled axes.](../images/E2_W9_R1_image1.png)
*This image makes the trap visible: a better fit statistic can still hide a worse engineering model if the residual structure is trying to tell you something important.

---

## Confidence Intervals: What "95%" Actually Means

**Practical rule:** When comparing two means, construct a confidence interval for their difference. Treat overlap between two separate intervals only as a visual clue.

A **confidence interval** comes from a statistical estimation procedure, not from a single experiment. A "95% confidence interval" means this: if you repeated the experiment many times, each time constructing an interval using the same procedure, 95% of those intervals would contain the true value. It does not mean there is a 95% probability that the true value lies within *this particular* interval. Once the interval is calculated, the true value either is or is not inside it. Probability no longer applies.

This distinction matters in engineering practice. You cannot look at a 95% confidence interval and declare that you are "95% confident" the true mean is inside it. You can say that your estimation procedure is calibrated to contain the true value 95% of the time over many repetitions. For a single experiment, the interval is either right or wrong, and you do not know which. Imagine using this same estimation procedure on 100 different experiments. In 95 of them, the CI you calculated would contain the true value. In 5 of them, it would not, and you would not know which 5. Your specific CI either captured the true value or it did not. The "95%" describes your method's long-run reliability, not this particular result.

In practice, interpret confidence intervals in terms of the estimation process, not the individual result. When comparing two results, form an interval for the difference. Use a Welch interval for independent groups when equal variance is not established, or an interval for paired differences when observations are matched. Ask whether that interval includes zero. Then compare the same interval with the engineering acceptance or equivalence region specified before the data were inspected. Two separate confidence intervals can overlap even when the difference interval excludes zero, so overlap alone is not the decision rule.

This distinction between **statistical significance** and **engineering significance** leads to the third common misapplication. Statistical significance means results are distinguishable given the measurement noise level. Engineering significance means the difference is large enough to matter for the intended use.

---

## Statistical vs. Engineering Significance

A result can be statistically significant and engineering-irrelevant. If your uncertainty is small enough, you can detect a difference in mean structural stiffness of 0.01% between two configurations. That difference is real. The statistical machinery confirmed it is not sampling noise. But if your structural model requires agreement to within 5% for its intended use, a 0.01% discrepancy is well within acceptance. The statistical significance of the difference is beside the point.

Conversely, a result can be statistically non-significant and engineering-critical. If your experiment has high noise and your confidence intervals are wide, you may be unable to distinguish a 15% stiffness difference from sampling variation. The two means are statistically indistinguishable. But a 15% stiffness difference in a load-bearing structure is an engineering problem regardless of what the statistics say. The experiment was not sensitive enough to detect the relevant difference. This is a measurement design failure, not a physical finding.

![A diagram showing four scenarios of model-prediction comparison using overlapping or non-overlapping confidence intervals. Two vertical number lines represent "Predicted value" (dashed line) and a range of "Measured mean ± 95% CI" (solid horizontal bar). Scenario 1: CI contains the predicted value AND the difference is within the engineering acceptance criterion — labeled "Agreement: statistically AND engineeringly adequate." Scenario 2: CI contains the predicted value but the difference exceeds the engineering criterion — labeled "Statistically indistinguishable but engineeringly inadequate." Scenario 3: CI does not contain the predicted value but the difference is small relative to engineering criterion — labeled "Statistically significant but engineering-irrelevant." Scenario 4: CI does not contain the predicted value and exceeds engineering criterion — labeled "Statistically AND engineeringly inadequate." The diagram makes visible that the four scenarios require different engineering conclusions. Clean 2×2 conceptual grid style.](../images/E2_W9_R1_image2.png)
*This image shows why statistical significance and engineering adequacy cannot be collapsed into one yes-or-no judgment.

Effect size, the magnitude of the difference relative to the variability in the data, is the quantitative bridge between statistical significance and engineering significance. A small effect size with a large sample may be statistically significant but engineering-irrelevant. A large effect size with a small sample may not reach statistical significance but still be clearly engineering-critical. The connection back to Week 6 is direct: the acceptance criterion you wrote in your pre-lab prediction is the engineering significance threshold. When you compare your Tier 2 results to your committed prediction, that criterion is the frame. Statistical distinguishability is a prerequisite, because you need to know whether the discrepancy is real or just noise. Passing the statistical test is not the same as passing the engineering test. Both questions must be answered, and both must be answered against the criteria written before the data was collected.

---

**The Takeaway:** Regression, confidence intervals, and hypothesis testing are powerful tools with specific and limited meanings. Applying them correctly means knowing what each one cannot tell you, then connecting statistical results back to the intended-use criteria written before the experiment began.
