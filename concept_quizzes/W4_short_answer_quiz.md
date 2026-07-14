# W4 Short Answer Quiz

## Week Focus

Reading models to design tests, ranking error sources, sensor selection logic, and integrating the full Phase I pipeline.

## Reusable AI Grader Prompt

```text
You are grading an ASEN 3501 Week 4 concept-check response.

Question: {{question}}
Question type: {{question_type}}
Options (if multiple choice): {{options}}
Expert response: {{expert_response}}
Student response: {{student_response}}

Your task:
1. Judge the response only against the expert response and Week 4 course material.
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

**Learner-facing question:** If a model output has to be known within a certain tolerance, what is the most useful Week 4 design move?

A. Start collecting data and hope the uncertainty is small enough  
B. Work backward from the output requirement to determine what measurement quality the inputs must have  
C. Ignore sensor choice because analysis can fix it later  
D. Replace the model with a qualitative description

**Expert response:** B is the best answer. Week 4 emphasizes reading the model backward from the required output quality to the needed input accuracy and sensor performance. This is how measurement requirements become design requirements.

### Q2

**Type:** Multiple choice

**Learner-facing question:** Why is ranking dominant error sources useful?

A. It tells you where improvement effort is most likely to matter  
B. It proves the model is valid  
C. It removes the need for uncertainty propagation  
D. It guarantees all sensors will agree

**Expert response:** A is the best answer. Once you know which terms dominate the uncertainty budget, you can focus on the highest-leverage improvement rather than guessing where to spend effort or money.

### Q3

**Type:** Multiple choice

**Learner-facing question:** Which statement best reflects the Week 4 full-pipeline mindset?

A. Experimental design, measurement, uncertainty analysis, and model comparison are separate chores that happen to be in the same report  
B. The report is a single argument from setup to conclusion, and each section depends on the analytical work before it  
C. The most important section is whichever one has the nicest figure  
D. Once data is collected, the AMVF is no longer useful

**Expert response:** B is the best answer. Week 4 emphasizes the Phase I report as an integrated argument, not a checklist of disconnected sections.

### Q4

**Type:** Open response

**Learner-facing question:** Suppose one error term dominates your uncertainty budget by a wide margin. What does Week 4 suggest you should do with that information?

**Expert response:** A strong response says that the dominant term should guide design improvement, sensor selection, or measurement strategy. If one source overwhelms the rest, reducing smaller terms first is unlikely to matter much. The key Week 4 idea is that uncertainty analysis should drive decisions, not just decorate the report.

### Q5

**Type:** Open response

**Learner-facing question:** In your own words, what does it mean to say that the Phase I report is a “single integrated argument”?

**Expert response:** A strong response explains that the report moves logically from what was measured and why, to how the data was collected, to how uncertainty was quantified, to how the result compares with the model, and finally to what the data suggests should change. Each later claim depends on earlier sections being technically sound. The report is therefore not just a format requirement; it is the structure of the engineering reasoning itself.
