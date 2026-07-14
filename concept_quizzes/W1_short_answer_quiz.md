# W1 Short Answer Quiz

## Week Focus

AMVF, verification vs. validation, measurement vs. inference, and formal experiment design.

## Reusable AI Grader Prompt

```text
You are grading an ASEN 3501 Week 1 concept-check response.

Question: {{question}}
Question type: {{question_type}}
Options (if multiple choice): {{options}}
Expert response: {{expert_response}}
Student response: {{student_response}}

Your task:
1. Judge the response only against the expert response and Week 1 course material.
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

**Learner-facing question:** In the course framing, what is the main job of validation?

A. Checking whether the experiment was performed safely  
B. Checking whether the equations were solved correctly  
C. Checking whether the model is an adequate representation of the real physical system  
D. Checking whether the sensor was calibrated correctly

**Expert response:** C is the best answer. Validation asks whether the model is the right model for the physical system and intended use. Solving equations correctly is verification, while sensor calibration is a measurement task rather than model validation.

### Q2

**Type:** Multiple choice

**Learner-facing question:** Which statement best captures the difference between what a sensor measures and what an engineer often cares about?

A. A sensor always measures the final engineering quantity directly.  
B. A sensor measures a raw signal, and the engineering quantity is often inferred through a calibration or model.  
C. A sensor only measures noise, and the engineer removes it later.  
D. A sensor and a model are unrelated parts of the workflow.

**Expert response:** B is the best answer. Many sensors output a voltage, resistance change, or other intermediate signal, and the quantity of interest is inferred through calibration and assumptions. That is why measurement is not just data collection; it is model realization.

### Q3

**Type:** Multiple choice

**Learner-facing question:** Which hypothesis is the most testable in the Week 1 sense?

A. “The system will probably change when we run the experiment.”  
B. “We expect interesting behavior.”  
C. “If input voltage is increased from 3 V to 9 V while resistance is held constant, measured power will increase by a factor of nine because power scales with V^2/R.”  
D. “The data should make sense if we do the procedure correctly.”

**Expert response:** C is the best answer because it specifies the manipulated variable, the expected response, and the physical reasoning. The other choices are too vague to be falsifiable in a useful engineering sense.

### Q4

**Type:** Open response

**Learner-facing question:** Explain the difference between verification and validation in your own words, and give one short engineering-style example of each.

**Expert response:** A strong response explains that verification asks whether you solved the chosen equations correctly, while validation asks whether those equations are an adequate description of the real system for the intended use. An acceptable example of verification is checking that a code or calculation implements the model correctly. An acceptable example of validation is comparing model predictions to measured outcomes with uncertainty bounds to decide whether the model matches reality well enough.

### Q5

**Type:** Open response

**Learner-facing question:** A team says their sensor reads force directly. Based on Week 1, what would you want to ask before accepting that claim?

**Expert response:** A strong response should question what the sensor actually outputs, what calibration equation converts that output to force, and what assumptions support that conversion. It should also mention possible installation effects, bias, or confounding factors that could make the inferred force wrong even if the raw sensor reading is consistent. The key Week 1 idea is that the measured signal and the engineering quantity are not automatically the same thing.
