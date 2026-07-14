# W3 Short Answer Quiz

## Week Focus

Validation metrics, calibration vs. validation, multi-sensor comparison, residuals, and critique quality.

## Reusable AI Grader Prompt

```text
You are grading an ASEN 3501 Week 3 concept-check response.

Question: {{question}}
Question type: {{question_type}}
Options (if multiple choice): {{options}}
Expert response: {{expert_response}}
Student response: {{student_response}}

Your task:
1. Judge the response only against the expert response and Week 3 course material.
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

**Learner-facing question:** Why is visual overlap on a plot alone not enough to support an engineering comparison claim?

A. Because engineers are not allowed to use plots  
B. Because agreement should be argued using a defined metric and uncertainty-bounded reasoning, not just by eyeballing the figure  
C. Because every plot must have a regression line  
D. Because visual inspection is only useful in chemistry

**Expert response:** B is the best answer. Week 3 emphasizes that engineering comparison claims must be numerical and traceable. A plot can help communicate the result, but it is not the full argument by itself.

### Q2

**Type:** Multiple choice

**Learner-facing question:** Which statement best captures the Week 3 distinction between calibration and validation?

A. Calibration and validation are the same thing with different names  
B. Calibration tests whether a model is predictive, while validation adjusts a sensor to a reference  
C. Calibration is a measurement activity that aligns sensor output to a reference, while validation tests whether a model adequately predicts reality  
D. Validation is only needed if calibration fails

**Expert response:** C is the best answer. Calibration concerns the measurement chain, while validation concerns the model-to-reality comparison. Treating a calibrated instrument as proof that a model is valid is a category error.

### Q3

**Type:** Multiple choice

**Learner-facing question:** If two sensors measuring the same quantity disagree outside the accepted comparison bound, what is the best Week 3 conclusion?

A. One sensor must be lying, so delete that dataset immediately  
B. The disagreement is evidence that needs explanation, using uncertainty, sensor behavior, or model limitations  
C. The comparison is irrelevant because two sensors never match perfectly  
D. Validation is complete because two sensors were used

**Expert response:** B is the best answer. Week 3 treats discrepancy as something to explain, not hide. The next step is to investigate whether the disagreement comes from measurement uncertainty, bias, installation effects, or model-form limitations.

### Q4

**Type:** Open response

**Learner-facing question:** What does a residual pattern tell you that a single overall error number might not tell you?

**Expert response:** A strong response says that residual structure can reveal systematic trends, such as bias, missing physics, or condition-dependent model failure. A single summary number can hide that structure. Week 3 uses residual inspection to move from “how big is the error?” to “what kind of mistake is this?”

### Q5

**Type:** Open response

**Learner-facing question:** If you were critiquing a sample lab report in the Week 3 style, what four things should your critique try to identify?

**Expert response:** A strong response should include the four-part critique structure: what is correct and well-supported, what is incorrect or unsupported, what is missing, and what specific change would improve the report. The point is not to say “good” or “bad” in general; it is to give an evidence-based technical evaluation.
