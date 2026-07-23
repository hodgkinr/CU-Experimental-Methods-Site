# Tier 2 Lab Assignment — Frequently Asked Questions

## 1. Is Tier 2 an individual assignment or a group assignment?

Tier 2 is a group assignment.
You develop the pre-lab prediction as a group, run the experiment as a group, submit one group report, and present one quad chart as a group.
However, every student is still responsible for understanding the full workflow and contributing meaningfully to the analysis and presentation.

## 2. What exactly has to be ready before we can touch the equipment?

Your group must arrive with a documented pre-lab prediction that includes all five required elements:
- system response features
- theoretical model / working equation
- estimated uncertainty in the primary derived quantity
- numerical acceptance criterion
- risk assessment

If one of those pieces is missing, the prediction is incomplete and the group may be asked to finish it before proceeding.

## 3. Does the prediction have to be polished?

No.
It can be handwritten, a short typed document, or a MATLAB script with clearly labeled outputs.
What matters is that it is complete, legible, and defensible.

## 4. What makes an acceptance criterion good enough?

It must be numerical and committed before data collection.
“Looks close” is not enough.
A good criterion states what level of agreement would count as adequate for the intended use, such as a percent threshold or whether the measured result falls within a labeled uncertainty interval.

## 5. What if our prediction turns out to be wrong?

That is not automatically a problem.
Tier 2 is not graded on whether your first prediction was lucky.
It is graded on whether the prediction was reasoned, whether the comparison is technically honest, and whether you can explain what the discrepancy means.

## 6. Are we allowed to revise the prediction after we see the data?

You may refine your interpretation later, but the original prediction must remain intact.
The report reproduces the committed pre-lab prediction as evidence of what you believed before the experiment ran.
Do not quietly rewrite it after the fact.

## 7. How detailed does the calibration section need to be?

It needs more than a note that an instrument was “calibrated.”
You must document the calibration date, the required interval, whether the instrument is still within that interval, and what calibration uncertainty means for your primary result.
The point is to connect calibration status to the validation argument, not just to record paperwork.

## 8. What counts as a real improvement proposal?

A real improvement proposal is specific and tied to your evidence.
It should name a quantity, sensor, DAQ choice, operating condition, model assumption, or measurement strategy that should change, and it should explain why that change follows from your data or uncertainty analysis.
“Use better sensors” is too generic by itself.

## 9. Do we have to use MATLAB?

MATLAB is the course-supported path, especially when the experiment-specific lab document uses a MATLAB-based DAQ workflow.
If your group uses another tool for processing or figure generation, the work still needs to be organized, reproducible, and compatible with the required deliverables.
Follow the experiment-specific lab document for any hard setup requirements.

## 10. What should the quad chart actually show?

Each cell should stand on its own:
- prediction vs. outcome
- uncertainty analysis
- calibration status
- top improvement recommendation

A reader who sees only one cell should still understand what that cell is claiming and why it matters.

## 11. How should we use the student rubric?

Use `TIER2_rubric_student.md` alongside this assignment from the beginning, not just before submission.
The assignment tells you what to produce.
The rubric tells you what a passing and excellent response look like in the report, the quad chart, the Q&A, and the peer evaluations.

## 12. Are peer evaluations really graded?

Yes.
Peer evaluations are graded on quality, not on generosity.
A useful evaluation names a specific strength, a specific weakness, and a concrete improvement recommendation supported by evidence from the presentation.

---

*ASEN 3501 — Tier 2 FAQ | Companion to `TIER2_assignment.md` and `TIER2_rubric_student.md`*
*Evergreen — structure, expectations, and grading logic are stable across experiment assignments*
