# W9 Short Answer Quiz

## Week Focus

Statistical vs. engineering significance, regression limits, confidence intervals, and data-grounded improvement proposals.

## Reusable AI Grader Prompt

```text
You are grading an ASEN 3501 Week 9 concept-check response.

Question: {{question}}
Question type: {{question_type}}
Options (if multiple choice): {{options}}
Expert response: {{expert_response}}
Student response: {{student_response}}

Your task:
1. Judge the response only against the expert response and Week 9 course material.
2. Classify the response as Correct, Partially Correct, Incorrect, or Off-Topic.
3. Give 3-5 sentences of constructive feedback.
4. If the student got something right, name it explicitly.
5. Identify the most important missing or incorrect idea.
6. Do not introduce later-course material that has not appeared yet.
7. If the question is multiple choice, explain why the selected answer is or is not the best choice.

Output format:
Verdict: <one label>
Feedback: <3-5 sentences>
```

## Questions

### Q1

**Type:** Multiple choice

**Learner-facing question:** Which statement best reflects Week 9’s warning about R^2?

A. A high R^2 proves the model is physically correct  
B. A high R^2 means the model explains variance in the fitted data, but it does not by itself prove the model is physically adequate  
C. R^2 is only useful for finance  
D. R^2 replaces residual analysis

**Expert response:** B is the best answer. Week 9 treats regression as a diagnostic tool, not a final validation certificate. Good fit and correct physics are related but not identical.

### Q2

**Type:** Multiple choice

**Learner-facing question:** Which statement best captures the difference between statistical significance and engineering significance?

A. They are always identical  
B. Statistical significance concerns whether a difference is distinguishable in the data, while engineering significance concerns whether that difference matters for the intended use or requirement  
C. Engineering significance only matters in civil engineering  
D. Statistical significance only matters when a model fails

**Expert response:** B is the best answer. Week 9 emphasizes that a result can be statistically detectable but still too small to matter for the engineering decision, or vice versa.

### Q3

**Type:** Multiple choice

**Learner-facing question:** What is the strongest Week 9 reason to use Monte Carlo for a multi-variable system?

A. It avoids having to think about uncertainty sources  
B. It helps propagate multiple uncertain inputs through the model and examine the resulting output distribution, including cases that are awkward for simple closed-form reasoning  
C. It guarantees the prediction will match the experiment  
D. It removes the need to interpret residuals

**Expert response:** B is the best answer. Week 9 extends Monte Carlo from the simpler E1 setting to more complex systems with several uncertain inputs and richer output behavior.

### Q4

**Type:** Open response

**Learner-facing question:** A comparison is statistically different, but the gap is still inside the allowed engineering tolerance for the intended use. How should you describe that result?

**Expert response:** A strong response should say that the data and prediction are distinguishable in a statistical sense, but the discrepancy may still be acceptable for the engineering purpose. The response should explicitly separate those two judgments instead of collapsing them into one. Week 9 wants students to keep both lenses active.

### Q5

**Type:** Open response

**Learner-facing question:** Why is a data-grounded improvement proposal stronger than a generic suggestion like “use better sensors”?

**Expert response:** A strong response explains that a data-grounded proposal ties the recommendation to a specific residual pattern, uncertainty bottleneck, calibration issue, or statistical finding. A generic suggestion sounds plausible but does not show that the group learned something precise from the experiment. Week 9 pushes students toward evidence-based improvement claims.
