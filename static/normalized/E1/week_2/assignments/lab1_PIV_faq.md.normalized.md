# Lab 1 (P=IV) — Frequently Asked Questions
## ASEN 3501: Aerospace Experimental Methods

*This document answers questions that come up frequently during Lab 1 preparation,
execution, and report writing. If your question isn't here, ask your TA or the course AI
tutor.*

---

## Before the lab

**Should I use the nominal resistance value (from the label) or the measured resistance
(from a pre-assembly DMM reading) when I compute power and propagate uncertainty?**

Use the measured value with u_R propagated from the DMM voltage accuracy specification.
The measured value is more accurate than the nominal ±5% label. The nominal value is
still useful for a sanity check — your measured value should fall within the stated
tolerance. If it doesn't, something is wrong with the measurement or the component.

---

**Do I need to memorize my report for the oral interview?**

No. You may bring your lab report and refer to it freely. What the interviewer is
assessing is whether you can explain the *reasoning* behind a result, not whether you can
recall a formula from memory. If asked to walk through the partial derivative computation,
it is completely fine to look at the formula in your report. The question is whether you
can explain what each term means and why the form matters.

The rubric requires you to demonstrate understanding in 3 of 5 categories. See
`LAB1_PIV_rubric_student.md` for what "understanding" looks like in each category.

---

## During the lab

**Should I average the three voltage and current readings, or use each trial separately?**

Use the mean of your three readings as your measured value of V and I. The standard error
of the mean from three readings (σ/√3) is typically much smaller than the manufacturer
specification uncertainty, so the spec will dominate your formal uncertainty estimate.
Record all three individual readings in your report to demonstrate repeatability — but
compute P and propagate uncertainty using the mean values.

---

## Monte Carlo simulation

**Which distribution should I use for V and I in the Monte Carlo simulation —
Gaussian or uniform?**

Both are defensible. The choice depends on what you know about the error source:

- **Uniform distribution** [measured value − u, measured value + u]: use this when all
 you know is a tolerance bound from the datasheet, with no information about the
 distribution shape. This is the more conservative and technically honest choice for a
 manufacturer specification.

- **Gaussian distribution** with σ = u/2: use this when you are treating the manufacturer
 spec as an approximately 95% confidence bound (k=2 coverage factor), which is common
 for precision instrument specifications. The factor of 2 means σ = u/2, not σ = u.

See W2_L2 slide 7 for the full reasoning. Either choice is acceptable — what matters is
that you state your choice explicitly in Section 5 of your report and justify it in one
sentence.

If you want a single defensible default: **use uniform**. It makes fewer assumptions.

---

**Why does my Monte Carlo standard deviation look like it's about half of my
partial-derivative uncertainty? Did I do something wrong?**

Probably not — this is a σ-convention issue. Here's what's happening:

The partial-derivative method computes δP using the full manufacturer spec value u as the
input uncertainty. The result δP represents the maximum bound.

If you set σ = u/2 in your Gaussian Monte Carlo (treating u as a ±2σ bound), then your
simulation input standard deviation is half the spec value. The output distribution
standard deviation will therefore also be approximately half of δP.

This is not an error — it's a consistent consequence of your σ-convention. To make the
two methods give comparable magnitudes directly, either:
- Use uniform distributions (the bounds match the spec value directly), or
- Use Gaussian with σ = u (treating the spec as a 1σ bound — less standard but makes
 the comparison numerically direct)

The key requirement is to state your convention explicitly in Section 5 and check
consistency when writing Section 6. The comparison should explain *why* the numbers
relate the way they do, not just assert that they agree or disagree.

---

## Report writing

**I computed three different values of P — 0.2425 W, 0.2447 W, and 0.2404 W.
They're close but not the same. Which one is my "best estimate" for Section 7?**

Report the result from the form with the smallest propagated uncertainty. In this lab
that is typically P = IV, because both V and I are directly measured inputs and the
sensitivity coefficients are smaller than in the forms that involve R² terms.

Your choice should be *consistent* with your Section 4 sensitivity analysis. If you
concluded in Section 4 that P = IV has the smallest uncertainty, your Section 7 result
should use that form. The point of the sensitivity analysis is not just arithmetic — it
is to make a reasoned choice about which result to report.

You may report all three forms for completeness, but designate one as your primary result
and explain why.

---

**Should I say "95% CI" or "manufacturer spec bound" when stating my result in
engineering form in Section 7?**

For Lab 1, use **"manufacturer spec bound"** as your default. Here's the distinction:

- **"Manufacturer spec bound"** means the uncertainty was derived directly from the
 instrument datasheet specification, without a statistical sampling argument. This is
 accurate for what you did.

- **"95% CI"** means you can trace the bound to a specific probability statement — either
 from repeated measurements and a t-distribution, or from a manufacturer spec that
 explicitly states it corresponds to 95% coverage.

Some multimeter datasheets do state that their accuracy specification corresponds to a
95% or 99% confidence level. If yours does, you may write "95% CI (manufacturer spec)."
If it doesn't state the confidence level explicitly, write "manufacturer spec bound."

The general format is:
*P = [value] ± [uncertainty] W (manufacturer spec bound, partial derivative propagation)*

---

*Lab 1 FAQ | ASEN 3501 | E1 Week 2*
*Generated from simulated student gap analysis — 2026-05-26*
*Questions or corrections: contact the teaching team*
