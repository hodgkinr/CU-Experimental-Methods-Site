# ASEN 3501 — Lab 1: Power, Voltage, and the Language of Uncertainty
## Student-Facing Assignment

**Segment:** E1 — Execution & Quantification
**Week:** 2
**CLO Alignment:** CLO 1, CLO 2, CLO 5
**Assessment:** Brief lab report (support document) + 3-minute oral interview
**Estimated time:** 3–5 hours total (in-lab activity: ~1 hour; report preparation: 2–4 hours)

---

## Why This Lab Exists

Every engineering measurement you take comes with a number and an uncertainty. The number
alone is incomplete. It tells you what the instrument displayed, not what the physical
quantity actually is or how confident you should be in that display.

This lab is your first chance to practice treating uncertainty as a required output, not an
afterthought. The physical setup is deliberately simple: a resistor, a power supply, and a
multimeter. The simplicity is intentional. There is nothing here to distract you from the
core question: *given that your instruments have limits, what can you actually claim about
the power dissipated in this circuit?*

That question, and the rigorous way to answer it, is the foundation this course is built on.

---

## Learning Goals

By the end of this lab and its associated activities, you should be able to:

1. Measure voltage and current using a digital multimeter, correctly read and record the result, and assign an appropriate uncertainty from the instrument datasheet.
2. Apply first-order uncertainty propagation (the general method using partial derivatives) to compute the uncertainty in a derived quantity, electrical power, from measurements of voltage and current.
3. Explain why different algebraic forms of the same physical law (P = IV, P = V²/R, P = I²R) produce different uncertainty estimates for the same quantity, and articulate which form is most sensitive to which measured input.
4. Run a Monte Carlo simulation in MATLAB to estimate uncertainty using the same manufacturer specifications, and compare the Monte Carlo result to the partial-derivative result.
5. State a result in the course reporting form: *estimate ± interval (units; interval type, method, and coverage basis)*.

### Course reporting convention

Use `E1_W2_R3_reading.md` for every uncertainty statement. Convert all elemental inputs
to standard uncertainties before propagation. Report Taylor-series results as combined
standard uncertainty `u_c`, and, when requested, as expanded uncertainty `U = k u_c` with
`k` stated. Report Monte Carlo percentile bounds as coverage intervals, not confidence
intervals. Label every plotted interval with its basis.

Type A and Type B describe **how an uncertainty is evaluated**, not whether an effect is
random or systematic. A Type A evaluation uses data from repeated observations. A Type B
evaluation uses other information, such as a datasheet, calibration certificate, manual,
prior measurements, or engineering judgment. After converting each input to a standard-
uncertainty basis, combine them as `u_c`. A stated coverage factor `k` is the multiplier
used to form expanded uncertainty, `U = k u_c`; `k = 2` is not automatically a 95%
frequentist confidence interval unless the coverage basis supports that interpretation.
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
| P = V²/R | V and R | Power using voltage and resistance |
| P = I²R | I and R | Power using current and resistance |

Each form uses a different set of measured inputs. These are different **measurement
models**, even though the circuit law is algebraically equivalent under ideal conditions.
The estimates can differ because V, I, and R are acquired differently, at different times,
with shared inputs and different loading or thermal effects. Algebra alone does not create
new information.

### Which resistance value to use: two valid cases

For the two forms that use R (P = V²/R and P = I²R), there are two defensible ways to get
a value for R and its uncertainty:

- **Case 1: Nominal + manufacturer tolerance.** Use the resistor's labeled nominal value
 and the tolerance printed on it (e.g., 200 Ω ± 5%). Treat the printed tolerance as a
 symmetric half-width `a_R`; with a uniform Type B model, use `u_R = a_R/√3`.
- **Case 2: DMM-measured + instrument accuracy.** Measure the resistor's resistance
 directly with the multimeter and use the DMM's resistance-measurement accuracy
 specification (from the datasheet) to calculate its symmetric half-width `a_R`, then
 convert it to `u_R = a_R/√3` under the same uniform Type B model.

**You are required to compute both cases** for P = V²/R and P = I²R, not just pick one.
This is intentional, and it's the real point of this part of the lab: Case 1 and Case 2 use
different information about R and will generally produce different point estimates and
different uncertainty bounds. Compare their point estimates and labeled intervals, but do
not interpret overlap as locating the true value. These estimates are not independent: they
share measurements and may share instrument effects. Agreement is an internal-consistency
check; disagreement is a prompt to inspect assumptions, timing, loading, self-heating, and
the uncertainty model.

### A note on system warm-up and drift

The power supply and multimeter in this circuit are not perfectly static the moment you
turn them on. It's common to observe the voltage reading drift gradually over the first
several minutes of operation. For example, it might start a little high right after
power-on and settle to a slightly lower, stable value after about five minutes. This is
typically caused by the power supply warming up to its normal operating temperature, not by
an error in your circuit or technique. If you power-cycle the supply (turn it off and back
on) with the circuit still connected, the reading will usually jump back up and begin
drifting again. That's a useful check if you want to confirm the supply, rather than the
resistor or DMM, is the source of the drift.

**Practical implication for data collection:** take your five repeated V and I readings
close together in time (within a minute or two of each other), rather than spacing them out
over the full lab session. This keeps your repeatability trials measuring genuine
instrument/reading variation, rather than accidentally capturing warm-up drift and
mistaking it for repeatability.

If you are using **Case 2** (DMM-measured resistance), there is an additional interaction to
be aware of: if you measure R with the DMM *before* the resistor is in the powered circuit,
that measurement reflects the resistor at room temperature ("cold"). Once current flows
through the resistor for an extended period, it will self-heat slightly, and its actual
in-circuit ("hot") resistance may differ from your cold measurement. You don't need to
correct for this quantitatively, but flag it as a limitation if your Case 1 and Case 2
results in Section 6 don't overlap as cleanly as you'd expect.

---

## The Instrument — Reading Your Multimeter

### What the display is telling you

A digital multimeter display shows a numerical reading that is updated at a fixed rate.
On most benchtop multimeters, the least significant digit, the rightmost digit, will
fluctuate during a measurement. This isn't noise in the measurement. It's the instrument's
resolution limit combined with real variation in the signal.

**Recording rule:** Cover the fluctuating digit with your finger. Read and record the
stable digits. Assign an uncertainty of ±½ of the last stable digit's place value.

**Example:** Your voltmeter reads 4.9<em>3</em>, 4.9<em>2</em>, 4.9<em>4</em>. The units digit in the tenths
place is stable (4.9), but the hundredths digit fluctuates (2, 3, 4). You record **4.9 V**
and assign an uncertainty of **±0.05 V** (half of one unit in the tenths place).

This is a *conservative but not overcautious* recording strategy. You aren't ignoring
variation. You're bounding it at the resolution of the instrument. The tradeoff matters:
if you assign unnecessarily large uncertainties, the systems designed around your measurements
will be over-engineered and expensive. If you assign uncertainties that are too small, those
systems might fail. The correct answer is the smallest defensible bound.

### Two methods, two different jobs

You now have two different ways to assign an uncertainty to a measurement: the
fluctuating-digit procedure above, and the manufacturer datasheet specification below.
They aren't competing methods where you pick your favorite. They answer different
questions:

- **The fluctuating-digit method is a field technique.** It's what you do at the bench,
 in real time, with no datasheet in hand, just by watching the display. It's a fast,
 physical sanity check on resolution, and it's what you record and describe in Section 2
 of your report to demonstrate you can read an instrument correctly.
- **The datasheet specification is evidence for a specification-based Type B evaluation.** It's what you use for every partial-derivative and Monte Carlo calculation in this lab. The reason it takes priority over the fluctuating digit is that a display can look perfectly stable and still be systematically wrong by more than the resolution suggests. The datasheet's accuracy spec captures that systematic error, which the fluctuating digit alone cannot.

If you ever find that your fluctuating-digit uncertainty is *larger* than the datasheet
spec, that's worth a sentence of discussion in your report. It usually means the signal
itself is genuinely noisy (e.g., an unstable supply or a marginal connection), not that the
instrument's formal accuracy is worse than advertised.

### Using the datasheet

The instrument datasheet specifies accuracy in the form:

```
± (% of reading + % of range)
```

For example: ± (0.5% of reading + 0.1% of range). This is a manufacturer limit, not
automatically a standard uncertainty. Unless current calibration is verified, label this
exercise **specification-based**. Treat the symmetric limit `±a` as a Type B input with a
uniform model, so the standard uncertainty is `u=a/√3`, unless the datasheet states another
coverage basis. State that assumption before propagation.

**Careful:** these are percentages, not fractions. 0.5% means 0.005, not 0.5. A common
mistake is to use 0.5 directly in the calculation, which inflates the uncertainty by a
factor of 100. Double-check your decimal conversion before propagating.

Use the bundled [Keysight 34460A/34461A/34465A/34470A datasheet](<Digital Multimeters 34460A, 34461A, 34465A (6½ digit), 34470A (7½ digit).pdf>). Before you begin any measurements,
locate the 34461A specification for:
- DC voltage accuracy in the range you are using
- DC current accuracy in the range you are using

Write these down. They are your primary uncertainty inputs.

Datasheets typically list several tolerance columns depending on how long it has been
since the instrument's last calibration (e.g., 90-day, 1-year, 2-year). Use the **2-year
column** unless your instructor tells you otherwise. The DMMs in this lab were purchased
in **2019**, and their listed accuracy specification assumes the stated calibration
conditions. If current calibration cannot be verified, the exercise remains a
specification-based estimate rather than a calibration-supported result. Do not invent a
drift correction; state this limitation in Section 6.

The datasheet also lists an additional accuracy derating as a function of deviation from a
reference room temperature. **For this lab, assume the lab room is at the datasheet's
reference temperature and do not compute a temperature correction term.** This is an
intentional scope decision, not an oversight: part of engineering judgment is recognizing
which sources of uncertainty are negligible for a given situation and which are not. You are
still expected to **state this assumption explicitly** in your report (Section 1 or 3) as
your justification for excluding the temperature term. A documented assumption, even a
simple one, is part of a complete uncertainty analysis.

### Measurement-system limitations to identify

At a conceptual level, note four effects: voltmeter and ammeter **loading** can alter the
circuit; using one DMM sequentially makes V, I, and R non-simultaneous while the supply and
resistor drift; resistor **self-heating** changes the hot resistance from the cold ohmmeter
measurement; and quantities derived from shared V, I, or R inputs are correlated. You do
not need to estimate covariance numerically in Lab 1, but you must not call the three power
estimates independent.

---

## In-Lab Procedure

The procedure has three parts: building and measuring (steps 1–5), uncertainty analysis
from the datasheet (steps 6–8), and Monte Carlo simulation in MATLAB (steps 9–10).

**Note:** a single multimeter can't measure voltage and current at the same time. It must
be configured and connected differently for each. You'll measure V and I as two separate
steps, not simultaneously.

### Lab configuration

| Nominal resistance | Tolerance | Power rating | Supply target | Expected current | Expected power | Power-rating factor of safety |
|---:|---:|---:|---:|---:|---:|---:|
| 200 Ω | ±5% | 0.25 W | 5.00 V | 25 mA | 0.125 W | 2× |

Keep the power supply **off** while building or changing the circuit. Before applying
power, verify the resistor rating, DMM lead jacks, measurement mode, and wiring. The
expected values are pre-lab checks, not substitutes for your measured values.

1. Build the circuit: connect the resistor to the power supply so current can flow through it. Record the nominal resistor value and tolerance from its label. Also measure the resistor's resistance directly with the DMM (easiest done before wiring it into the powered circuit) and record this measured value. You'll need both the nominal and measured values for the resistance-uncertainty comparison described above.
2. With the circuit verified and the supply still off, set the power supply target to **5.00 V** as specified in the Lab configuration table, then apply power.
3. **Measure voltage first.** Configure the multimeter as a voltmeter and connect it in parallel across the resistor. Read and record V from the display using the fluctuating-digit procedure above. Take five repeated V readings, close together in time (see the warm-up note above), to check for repeatability. ![Digital multimeter configured as a voltmeter, connected in parallel across the resistor, displaying a voltage reading.](images/voltage1.png)
4. **Then measure current.** Reconfigure the multimeter as an ammeter and reconnect it in series in the loop (this requires briefly breaking the circuit to insert the meter in the current path; it can't stay connected the way it was for the voltage measurement). Read and record I from the display using the same fluctuating-digit procedure. Take five repeated I readings, close together in time. ![Digital multimeter configured as an ammeter, connected in series with the resistor, displaying a current reading.](images/current1.png)
5. Compute P three ways from your recorded V and I values. Note the differences.
6. Using the manufacturer specifications from the datasheet, calculate the symmetric limits `a_V` and `a_I`, then convert them to the Type B standard uncertainties `u_V = a_V/√3` and `u_I = a_I/√3` under the uniform model.
7. Apply first-order uncertainty propagation (partial derivatives) to compute the combined standard uncertainty `u_P` for each of the three forms. Show your work: write out the partial derivatives, substitute standard uncertainties, and state the result as P ± u_P.
8. Answer: which form of the power equation is most sensitive to uncertainty in V? In I? Where would you spend money on a better instrument if minimizing uncertainty in P was the goal?
9. Using the same manufacturer limits, run a Monte Carlo simulation in MATLAB for each of the three power measurement models. For each manufacturer input, sample uniformly over its original bounds, such as `[V-a_V, V+a_V]` and `[I-a_I, I+a_I]`. Use the corresponding original tolerance bounds for each resistance case. Do not use `u_V`, `u_I`, or `u_R` as the uniform half-widths; those symbols are standard uncertainties after division by `√3`. Use at least 10,000 samples. Plot the resulting distribution of P for each model with appropriate labels and captions. If a manufacturer or calibration source explicitly supplies a Gaussian standard deviation or coverage basis, you may use that documented model instead and must cite it; do not invent a Gaussian `σ` from an unlabeled tolerance.
10. Compare like quantities across methods: compare the Monte Carlo output standard deviation with the Taylor-series combined standard uncertainty `u_P`, and report any Monte Carlo percentile bounds as clearly labeled coverage intervals. State whether the results are consistent and explain meaningful differences.

---

## Deliverable: Brief Lab Report

You'll prepare a brief lab report to bring to your oral interview. This document is your
support material for the interview. You may refer to it during the conversation, but the
interview questions will probe your understanding, not your ability to read your own document.

**The report isn't graded independently. It's evidence that you prepared.**

### Required sections

**1. Circuit description and measurement record**
One paragraph and a simple schematic or sketch. What did you build? What did you measure?
Include your recorded V and I values with units. Include the datasheet specification you used.

**2. Fluctuating digit — what you did and why**
Describe the fluctuating digit procedure in your own words. What did the display show?
What did you record? What uncertainty did you assign from the display, and why?

**3. Uncertainty propagation — partial derivatives**
Show the three partial derivative derivations for u_P under each power equation form.
For the two forms that depend on R (P = V²/R and P = I²R), compute u_P **twice each**:
once using Case 1 (nominal R and its tolerance) and once using Case 2 (DMM-measured R and
its measurement uncertainty). Present the final result for each as P ± u_P with units. A
table is the clearest way to present this (one row per form/case combination).

**4. Sensitivity analysis**
Which form is most sensitive to uncertainty in V? In I? Answer with numbers, not just words.
Where would you invest in a better instrument, and why?

**5. Monte Carlo simulation**
Include your MATLAB figure(s) showing the distributions of P for each equation form.
Each figure must have a title, labeled axes with units, a legend, and a caption that states
the key takeaway in one sentence. Include the key MATLAB code (the simulation loop and
distribution plot — not every setup line). **State the original manufacturer half-widths
`a`, show the uniform bounds you sampled, and report the simulated output standard
deviation and any selected percentile coverage interval.**

**6. Comparison: partial derivatives vs. Monte Carlo**
Are the results consistent? State the comparison numerically. Don't just say "yes they
agree." What does the comparison tell you about when you might prefer one method over the
other? Also briefly address: given that the DMMs were purchased in 2019, is it reasonable
to trust the datasheet's 2-year-column specification at face value, or should you flag
possible drift beyond spec as an additional (unquantified) source of uncertainty? Finally,
compare your Case 1 and Case 2 results for P = V²/R and P = I²R: do the two P ± u_P ranges
overlap? Treat overlap only as an internal-consistency clue under your stated assumptions;
it does not locate the true value. State what you observed and identify shared inputs or
effects that prevent the cases from being independent.

**7. Result statement**
State your best estimate of P in the correct engineering form:
*P = [value] ± [uncertainty] [units] ([interval type; method; coverage basis])*

**8. Plain-language explanation**
In 3–5 sentences, explain what you did in this lab and what your result means to someone
who has never taken an engineering course. Assume your audience is a curious high school
student. This section should be in your introduction or conclusion, not appended as an
afterthought.

### Format and submission

Submit your report as a single `.zip` archive containing your LaTeX source (`.tex` file(s)
and any figure files) and the compiled PDF, uploaded to Canvas before your scheduled
interview slot. Bring the compiled PDF (printed or on a device) to your interview; the
LaTeX source lets the AI-assisted grading pipeline check your work against the required
sections consistently.

See **E0 Supplemental: Getting Started with Overleaf and LaTeX** if you haven't used LaTeX
before.

**Submission:** See Canvas for the due date.

---

## Oral Interview

The oral interview is a 3-minute, one-on-one conversation with a member of the teaching team.
You may bring your lab report. No other materials are permitted.

The interview is a pass/fail assessment. You must pass this interview to satisfy the Lab 1
requirement.

Note that Learning Goal 6, explaining this lab's core concepts to someone without an
engineering background, isn't just a report-writing exercise. It's one of the categories
the interviewer may probe (see Category 5 in the student rubric), so it's worth practicing
your plain-language explanation out loud, not just writing it in Section 8.

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
- [Keysight 34460A/34461A/34465A/34470A multimeter datasheet](<Digital Multimeters 34460A, 34461A, 34465A (6½ digit), 34470A (7½ digit).pdf>) — use the 34461A accuracy tables and 2-year column
- MATLAB starter script — available on Canvas (sets up the Monte Carlo loop structure;
 you complete the equation forms and plotting)
- E0 Supplemental: Virtual Multimeter Simulator (optional bonus activity)
- E0 Supplemental: AI Tutor Setup and Practice
- E0 Supplemental: Getting Started with Overleaf and LaTeX
- For multimeter technique when measuring voltage and current as separate steps in the
 same circuit: https://www.youtube.com/watch?v=Y6xnLkiUMn8

---

*ASEN 3501 — Lab 1 Assignment | E1 Week 2*
*Evergreen — physics content; Update-friendly — multimeter datasheet specifications,
MATLAB starter script, power supply target voltage*
