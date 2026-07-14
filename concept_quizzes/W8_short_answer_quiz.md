# W8 Short Answer Quiz

## Week Focus

Model adequacy, residual taxonomy, calibration status review, and experimentally informed model updates.

## Reusable AI Grader Prompt

```text
You are grading an ASEN 3501 Week 8 concept-check response.

Question: {{question}}
Question type: {{question_type}}
Options (if multiple choice): {{options}}
Expert response: {{expert_response}}
Student response: {{student_response}}

Your task:
1. Judge the response only against the expert response and Week 8 course material.
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

**Learner-facing question:** If residuals show a systematic pattern instead of random scatter, what is the strongest Week 8 inference?

A. The pattern is unimportant if the plot looks nice  
B. The model or setup may be missing a structured physical effect, not just showing random noise  
C. Residuals should always be ignored after calibration  
D. The data must be deleted

**Expert response:** B is the best answer. Week 8 treats structured residuals as diagnostic evidence. They can point toward boundary-condition problems, missing physics, or other model-form issues.

### Q2

**Type:** Multiple choice

**Learner-facing question:** Which statement best captures calibration status review?

A. If the instrument turned on, calibration status is irrelevant  
B. Calibration status review asks whether the instrument’s calibration documentation, interval, and uncertainty support the credibility of the measurement claim  
C. Calibration status review proves the model is valid  
D. Calibration status review replaces uncertainty analysis

**Expert response:** B is the best answer. Week 8 asks students to review calibration date, interval, and related uncertainty information as part of measurement credibility. That supports, but does not replace, model comparison.

### Q3

**Type:** Multiple choice

**Learner-facing question:** Which is the best example of an experimentally informed model update?

A. “The data was noisy, so we will keep the same model and say the experiment went fine.”  
B. “The residual pattern suggests the model is missing a boundary-condition effect, so the next model revision should explicitly include that effect.”  
C. “We changed the plot color and the model looks better.”  
D. “Calibration and validation are the same, so no update is needed.”

**Expert response:** B is the best answer. An experimentally informed model uses data to identify a specific missing mechanism or flawed assumption and then proposes a targeted revision.

### Q4

**Type:** Open response

**Learner-facing question:** What is the difference between saying “the model is wrong” and saying “the residual pattern suggests model-form error”?

**Expert response:** A strong response says that the second statement is more precise and diagnostic. It points to a structured mismatch between the model and data and invites a specific explanation, while “the model is wrong” is too vague to guide improvement. Week 8 wants students to diagnose discrepancy, not just react to it emotionally.

### Q5

**Type:** Open response

**Learner-facing question:** Why doesn’t a current calibration sticker automatically settle the validation question?

**Expert response:** A strong response should explain that calibration speaks to the measurement chain, while validation asks whether the model predicts the real system adequately. A well-calibrated instrument can still produce data that disagrees with a poor model. Week 8 revisits this boundary deliberately.
