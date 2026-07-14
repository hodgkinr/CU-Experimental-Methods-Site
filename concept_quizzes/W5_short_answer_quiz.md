# W5 Short Answer Quiz

## Week Focus

Prediction before data release, committed reasoning, discrepancy interpretation, and cross-prediction.

## Reusable AI Grader Prompt

```text
You are grading an ASEN 3501 Week 5 concept-check response.

Question: {{question}}
Question type: {{question_type}}
Options (if multiple choice): {{options}}
Expert response: {{expert_response}}
Student response: {{student_response}}

Your task:
1. Judge the response only against the expert response and Week 5 course material.
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

**Learner-facing question:** Why does the course require a prediction memo before students see the data?

A. To make the assignment longer  
B. To force students to commit to reasoning before hindsight can reshape the story  
C. To prevent any use of uncertainty analysis  
D. To guarantee that every prediction is correct

**Expert response:** B is the best answer. The point of pre-commitment is not to guarantee correctness. It is to make later discrepancy interpretation honest and technically meaningful.

### Q2

**Type:** Multiple choice

**Learner-facing question:** Which of the following is the strongest prediction in the Week 5 sense?

A. “The result will probably be close.”  
B. “The sensor should give reasonable data.”  
C. “The measured response should peak near X with uncertainty about Y, and we will consider agreement acceptable if the data falls within the committed bound.”  
D. “We will know whether the model is good after we look at the data.”

**Expert response:** C is the best answer because it includes a committed predicted feature, an uncertainty-aware expectation, and an acceptance criterion. The other answers remain too vague or wait until after the data is seen.

### Q3

**Type:** Multiple choice

**Learner-facing question:** If a prediction is wrong but the reasoning was careful and committed in advance, what is the best Week 5 interpretation?

A. The work was useless  
B. The student should hide the prediction and rewrite it  
C. The discrepancy is valuable because it can reveal model limitations or missing physics  
D. The experiment automatically failed

**Expert response:** C is the best answer. Week 5 explicitly frames a wrong but well-reasoned prediction as analytically valuable because it creates a real basis for learning from discrepancy.

### Q4

**Type:** Open response

**Learner-facing question:** Why is predicting someone else’s experiment from specs a useful training exercise, even though it is not the same as running the experiment yourself?

**Expert response:** A strong response says that it forces you to reason forward from theory, sensor specs, and measurement setup without relying on memory of the data or the physical run. That builds the prediction-first mindset the course wants before E3. The exercise is difficult on purpose because it removes hindsight shortcuts.

### Q5

**Type:** Open response

**Learner-facing question:** A team says, “Our prediction was off, but that just means the experiment was bad.” What would Week 5 push you to ask next?

**Expert response:** A strong response should ask whether the discrepancy is more plausibly due to measurement uncertainty, model-form limitations, or some other identifiable cause, rather than treating “bad experiment” as a catch-all label. Week 5 wants students to interpret discrepancy structurally and specifically, not dismiss it with a vague complaint.
