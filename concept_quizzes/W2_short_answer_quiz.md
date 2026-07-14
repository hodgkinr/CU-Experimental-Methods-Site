# W2 Short Answer Quiz

## Week Focus

Variability, measurement error, uncertainty propagation, Monte Carlo reasoning, and correct engineering result statements.

## Reusable AI Grader Prompt

```text
You are grading an ASEN 3501 Week 2 concept-check response.

Question: {{question}}
Question type: {{question_type}}
Options (if multiple choice): {{options}}
Expert response: {{expert_response}}
Student response: {{student_response}}

Your task:
1. Judge the response only against the expert response and Week 2 course material.
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

**Learner-facing question:** Which statement best matches the Week 2 distinction?

A. Variability, measurement error, and uncertainty all mean the same thing.  
B. Variability is physical scatter, measurement error is instrument-related deviation, and uncertainty is the quantified bound on what we do not know about the reported result.  
C. Uncertainty is only used when the instrument is broken.  
D. Measurement error disappears if you repeat the measurement enough times.

**Expert response:** B is the best answer. Week 2 treats these as different ideas with different roles in an engineering claim. Variability belongs to the system, measurement error belongs to the measurement process, and uncertainty is the quantified statement attached to the final reported result.

### Q2

**Type:** Multiple choice

**Learner-facing question:** Why can two algebraically equivalent power equations produce different uncertainty estimates?

A. Because one of the equations must be physically wrong  
B. Because uncertainty propagation depends on which measured inputs appear in the chosen form and how sensitive the result is to each input  
C. Because engineers are free to choose whichever result they like better  
D. Because uncertainty only applies to nonlinear equations

**Expert response:** B is the best answer. The physics quantity is the same, but the propagated uncertainty depends on the input variables used and the partial derivatives of the chosen form. Different forms emphasize different measurement uncertainties.

### Q3

**Type:** Multiple choice

**Learner-facing question:** Which result is written in the most appropriate Week 2 engineering form?

A. “The answer is 4.98.”  
B. “The power is about 5 watts, probably.”  
C. “P = 4.98 +/- 0.12 W based on partial-derivative propagation.”  
D. “The power should be close to what the meter said.”

**Expert response:** C is the best answer because it includes the estimate, uncertainty, units, and method. The other options leave out key information needed to interpret the claim.

### Q4

**Type:** Open response

**Learner-facing question:** Suppose your Monte Carlo result and your partial-derivative result are close but not identical. Based on Week 2, how should you interpret that?

**Expert response:** A strong response says that the two methods estimate the same underlying uncertainty but use different mechanisms. Small differences are not automatically a problem; they may reflect sampling variation, nonlinearity, or distribution assumptions. The important point is to compare them thoughtfully rather than assuming one is “the truth” and the other is “wrong.”

### Q5

**Type:** Open response

**Learner-facing question:** In the P=IV lab, why might one form of the power equation lead you to care more about improving the current measurement than the resistance measurement?

**Expert response:** A strong response should explain that sensitivity depends on how the output changes with each input, which is captured by the partial derivatives. In a form like P = I^2 R, current appears squared, so uncertainty in current can have a larger influence on the uncertainty in power than uncertainty in resistance. The key idea is that instrument-improvement priorities should follow sensitivity, not habit.
