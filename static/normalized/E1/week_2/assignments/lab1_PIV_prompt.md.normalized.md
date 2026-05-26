# ASEN 3501 — Lab 1: Power, Voltage, and the Language of Uncertainty
## Student-Facing Assignment

**Segment:** E1 — Execution & Quantification
**Week:** 2
**CLO Alignment:** CLO 1, CLO 2, CLO 5
**Assessment:** Brief lab report (support document) + 3-minute oral interview
**Estimated time:** 3–5 hours total (in-lab activity: ~1 hour; report preparation: 2–4 hours)

---

## Why This Lab Exists

Every engineering measurement you will ever take comes with a number and an uncertainty. The
number without the uncertainty is incomplete — it tells you what the instrument displayed, not
what the physical quantity actually is or how confident you should be in that display.

This lab is your first chance to practice treating uncertainty as a required output, not an
afterthought. The physical setup is deliberately simple: a resistor, a power supply, and a
multimeter. The simplicity is intentional. There is nothing here to distract you from the
core question: *given that your instruments have limits, what can you actually claim about
the power dissipated in this circuit?*

That question — and the rigorous way to answer it — is the foundation on which everything
else in this course is built.

---

## Learning Goals

By the end of this lab and its associated activities, you should be able to:

1. Measure voltage and current using a digital multimeter and correctly read and record the result — including an appropriate uncertainty assigned from the instrument datasheet.
2. Apply first-order uncertainty propagation (the general method using partial derivatives) to compute the uncertainty in a derived quantity — electrical power — from measurements of voltage and current.
3. Explain why different algebraic forms of the same physical law (P = IV, P = V²/R, P = I²R) produce different uncertainty estimates for the same quantity, and articulate which form is most sensitive to which measured input.
4. Run a Monte Carlo simulation in MATLAB to estimate uncertainty using the same manufacturer specifications, and compare the Monte Carlo result to the partial-derivative result.
5. State a result in the correct engineering form: *estimate ± uncertainty (units, confidence level or method)*.
6. Explain the core concepts of this lab clearly and concisely to someone who has not taken this course.

---

## Background: The Circuit

You will build a simple series circuit: a DC power supply, a known resistor, and a
multimeter. You will measure:

- **V** — voltage across the resistor (voltmeter, in parallel)
- **I** — current through the resistor (ammeter, in series)

From these measurements you will compute electrical power three ways:

| Equation | Measured inputs | What you derive |
|---|---|---|
| P = IV | I and V directly | Power from both measurements |
| P = V²/R | V and R (nominal) | Power using voltage and resistance |
| P = I²R | I and R (nominal) | Power using current and resistance |

Each form uses different measured inputs. Different inputs have different uncertainties.
Different forms therefore produce different uncertainty estimates for the same quantity P.
This is not an error — it is the physics of error propagation.

---

## The Instrument — Reading Your Multimeter

### What the display is telling you

A digital multimeter display shows a numerical reading that is updated at a fixed rate.
On most benchtop multimeters, the least significant digit — the rightmost digit — will
fluctuate during a measurement. This is not noise in the measurement. It is the instrument's
resolution limit combined with real variation in the signal.

**The rule for recording measurements from a fluctuating display:**

> Cover the fluctuating digit with your finger. Read and record the stable digits. Assign
> an uncertainty of ±½ of the last stable digit's place value.

**Example:** Your voltmeter reads 4.9_3_, 4.9_2_, 4.9_4_ — the units digit in the tenths
place is stable (4.9) but the hundredths digit fluctuates (2, 3, 4). You record **4.9 V**
and assign an uncertainty of **±0.05 V** (half of one unit in the tenths place).

This is a *conservative but not overcautious* recording strategy. You are not ignoring
variation — you are bounding it at the resolution of the instrument. The tradeoff matters:
if you assign unnecessarily large uncertainties, the systems designed around your measurements
will be over-engineered and expensive. If you assign uncertainties that are too small, those
systems will fail. The correct answer is the smallest defensible bound.

### Using the datasheet

The instrument datasheet specifies accuracy in the form:

```
± (% of reading + % of range)
```

For example: ± (0.5% of reading + 0.1% of range). This is the *manufacturer specification* for
the maximum systematic error. You will use this specification — not the fluctuating digit
alone — as your formal uncertainty estimate for the partial-derivative and Monte Carlo
analyses.

You will receive the multimeter datasheet at the start of the lab session. Before you begin
any measurements, locate the specification for:
- DC voltage accuracy in the range you are using
- DC current accuracy in the range you are using

Write these down. They are your primary uncertainty inputs.

---

## In-Lab Procedure

The procedure has three parts: building and measuring (steps 1–4), uncertainty analysis from the datasheet (steps 5–7), and Monte Carlo simulation in MATLAB (steps 8–9).

1. Build the series circuit using the provided resistor, power supply, and multimeter. Record the nominal resistor value and tolerance from its label.
2. Set the power supply to a target voltage (specified by your lab instructor).
3. Read and record V and I from the multimeter displays using the fluctuating-digit procedure above. Record each reading three times to check for repeatability.
4. Compute P three ways from your recorded values. Note the differences.
5. Using the manufacturer specifications from the datasheet, compute the uncertainty in V and the uncertainty in I.
6. Apply first-order error propagation (partial derivatives) to compute the uncertainty in P for each of the three forms. Show your work: write out the partial derivatives, substitute values, and state the result as P ± u_P.
7. Answer: which form of the power equation is most sensitive to uncertainty in V? In I? Where would you spend money on a better instrument if minimizing uncertainty in P was the goal?
8. Using the same manufacturer specifications as probability distribution parameters, run a Monte Carlo simulation in MATLAB for each of the three power equation forms. Model V and I as independent random variables drawn from distributions consistent with the datasheet (Gaussian or uniform — justify your choice). Use at least 10,000 samples. Plot the resulting distribution of P for each form on the same figure with appropriate labels and captions.
9. Compare the Monte Carlo result to your partial-derivative result. Are they consistent? If not, explain why they might differ.

---

## Deliverable: Brief Lab Report

You will prepare a brief lab report to bring to your oral interview. This document is your
support material for the interview — you may refer to it during the conversation, but the
interview questions will probe your understanding, not your ability to read your own document.

**The report is not graded independently. It is evidence that you have prepared.**

### Required sections

**1. Circuit description and measurement record**
One paragraph and a simple schematic or sketch. What did you build? What did you measure?
Include your recorded V and I values with units. Include the datasheet specification you used.

**2. Fluctuating digit — what you did and why**
Describe the fluctuating digit procedure in your own words. What did the display show?
What did you record? What uncertainty did you assign from the display, and why?

**3. Uncertainty propagation — partial derivatives**
Show the three partial derivative derivations for u_P under each power equation form.
Present the final result for each as P ± u_P with units. One table or three clearly labeled
calculations is acceptable.

**4. Sensitivity analysis**
Which form is most sensitive to uncertainty in V? In I? Answer with numbers, not just words.
Where would you invest in a better instrument, and why?

**5. Monte Carlo simulation**
Include your MATLAB figure(s) showing the distributions of P for each equation form.
Each figure must have a title, labeled axes with units, a legend, and a caption that states
the key takeaway in one sentence. Include the key MATLAB code (the simulation loop and
distribution plot — not every setup line).

**6. Comparison: partial derivatives vs. Monte Carlo**
Are the results consistent? State the comparison numerically — do not just say "yes they
agree." What does the comparison tell you about when you might prefer one method over the
other?

**7. Result statement**
State your best estimate of P in the correct engineering form:
*P = [value] ± [uncertainty] [units] ([confidence level or method, e.g., 95% CI or
manufacturer spec bound])*

**8. Plain-language explanation**
In 3–5 sentences, explain what you did in this lab and what your result means to someone
who has never taken an engineering course. Assume your audience is a curious high school
student. This section should be in your introduction or conclusion — not appended as an
afterthought.

---

## Oral Interview

The oral interview is a 3-minute, one-on-one conversation with a member of the teaching team.
You may bring your lab report. No other materials are permitted.

The interview is a pass/fail assessment. You must pass this interview to satisfy the Lab 1
requirement.

**See the separate file `LAB1_PIV_rubric_student.md` for the question categories and what
a passing response looks like.** Prepare by reviewing that document before your interview.

### Preparing with the course AI tutor

The course AI tutor persona is described in the E0 supplemental materials. You can upload
this assignment document and the student rubric to a Claude or ChatGPT session configured
with the tutor persona, and practice your oral responses before the interview. Example prompts:

- *"Ask me an oral interview question about why P = IV and P = V²/R give different
 uncertainty estimates."*
- *"Pretend you are the instructor and ask me to explain the fluctuating digit procedure."*
- *"Give me a harder version of a question about when Monte Carlo is preferable to the
 partial derivative method."*

The AI tutor cannot predict the exact questions you will be asked, but it can give you
targeted practice on the core concepts. Use it.

---

## Resources

- E1 Week 2 Lecture: Error Propagation, Sensitivity Analysis & Monte Carlo
- E1 Week 2 Lecture: Variability, Error, and Uncertainty
- Coleman & Steele, *Experimentation, Validation, and Uncertainty Analysis for Engineers*,
 4th ed. — Chapter on uncertainty propagation (reference copy on course page)
- Multimeter datasheet — provided at lab session
- MATLAB starter script — available on Canvas (sets up the Monte Carlo loop structure;
 you complete the equation forms and plotting)
- E0 Supplemental: Virtual Multimeter Simulator (optional bonus activity)
- E0 Supplemental: AI Tutor Setup and Practice
- For multimeter to measure current and voltage simultaneous: https://www.youtube.com/watch?v=Y6xnLkiUMn8

---

*ASEN 3501 — Lab 1 Assignment | E1 Week 2*
*Evergreen — physics content; Update-friendly — multimeter datasheet specifications,
MATLAB starter script, power supply target voltage*
