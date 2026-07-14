# W7 Short Answer Quiz

## Week Focus

Sampling, aliasing, signal bandwidth, anti-aliasing filters, and DAQ justification.

## Reusable AI Grader Prompt

```text
You are grading an ASEN 3501 Week 7 concept-check response.

Question: {{question}}
Question type: {{question_type}}
Options (if multiple choice): {{options}}
Expert response: {{expert_response}}
Student response: {{student_response}}

Your task:
1. Judge the response only against the expert response and Week 7 course material.
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

**Learner-facing question:** What is aliasing in the Week 7 sense?

A. Random noise caused by a broken sensor  
B. High-frequency signal content folding into a false lower-frequency signal because the sampling rate is too low  
C. A plotting mistake caused by bad axis labels  
D. Any disagreement between a model and experiment

**Expert response:** B is the best answer. Aliasing is a sampling artifact, not just ordinary noise. It is dangerous because the false signal can look physically real.

### Q2

**Type:** Multiple choice

**Learner-facing question:** Signal bandwidth is primarily a property of:

A. The physical phenomenon being measured  
B. The font size on the DAQ screen  
C. The student’s preferred spreadsheet format  
D. The color of the sensor cable

**Expert response:** A is the best answer. Week 7 emphasizes that bandwidth belongs to the phenomenon, not to the DAQ by itself. The DAQ settings must be chosen to match the signal’s physics.

### Q3

**Type:** Multiple choice

**Learner-facing question:** Why must anti-aliasing happen before the analog-to-digital conversion?

A. Because once aliased data is sampled, the false low-frequency content is already inside the recorded dataset  
B. Because digital filters always increase noise  
C. Because analog components are cheaper than digital ones  
D. Because MATLAB cannot read filtered data

**Expert response:** A is the best answer. Week 7 teaches that anti-aliasing is an analog-domain protection step. After sampling, the corrupted low-frequency artifact is already mixed into the recorded signal.

### Q4

**Type:** Open response

**Learner-facing question:** Why is choosing a sampling rate a modeling commitment rather than just a technical setting?

**Expert response:** A strong response says that a sampling rate implicitly claims the signal has no important content above half that rate. That is a statement about the physics of the phenomenon, not just about the DAQ hardware. If the claim is wrong, the recorded data can be clean-looking but false.

### Q5

**Type:** Open response

**Learner-facing question:** A dataset shows a clean 120 Hz oscillation. Based on Week 7 alone, why should you still be cautious before concluding the physical system truly contains a 120 Hz mode?

**Expert response:** A strong response should note that an aliased higher-frequency signal can appear as a believable lower-frequency oscillation when sampled too slowly. The clean appearance of the data is not proof of correctness. Week 7’s central warning is that aliasing is silent corruption.
