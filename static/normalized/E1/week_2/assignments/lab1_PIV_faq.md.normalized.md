# Lab 1 (P=IV) — Frequently Asked Questions
## ASEN 3501: Aerospace Experimental Methods

*This document answers questions that come up frequently during Lab 1 preparation,
execution, and report writing. If your question isn't here, ask your TA or the course AI
tutor.*

---

## Before the lab

**Should I use the nominal resistance value (from the label) or the measured resistance
(from a pre-assembly DMM reading) when I compute power and propagate uncertainty?**

Both. You're required to run the analysis both ways and compare, not pick one:

- **Case 1:** nominal resistance and its printed tolerance (e.g., 200 Ω ± 5%)
- **Case 2:** DMM-measured resistance and the DMM's resistance-measurement accuracy spec

These are two independent, valid estimates of R and u_R, and they will generally give you
slightly different P ± u_P results for P = V²/R and P = I²R. That's expected. The point of
comparing them is to check internal consistency, not to locate the true value from their
overlap. The cases share measurements and are not independent. If they disagree, inspect
self-heating, meter loading, non-simultaneous readings, drift, and the Type B assumptions.

---

**My three trial readings for V (or I) aren't just scattered. They seem to be trending
steadily in one direction (e.g., drifting downward). Is something wrong?**

Probably not. This is likely warm-up drift, not a mistake. The power supply and DMM take
a few minutes to reach a stable operating point after power-on, and it's common to see
voltage readings settle gradually (for example, starting a little high right after power-on
and drifting down slightly over the first several minutes) before leveling off. This is a
different phenomenon from the fluctuating-digit noise described in the assignment, and a
different phenomenon from instrument accuracy error. It's a slow, directional trend rather
than a random jitter around a stable value.

What to do about it:
- Take your three repeated readings close together in time (within a minute or two of each
 other) rather than spread across the full lab session. This keeps your "repeatability"
 trials measuring genuine repeatability, not warm-up drift dressed up as repeatability.
- If you want to confirm the drift is coming from the power supply rather than the circuit
 or DMM, you can power-cycle the supply (off, then back on) with the circuit still
 connected. If the reading jumps back up toward its initial value and begins drifting
 again, that points to the supply as the source.
- You don't need to model or correct for this drift mathematically. Just be aware of it,
 take your readings in a tight time window, and if you notice a strong trend, it's worth a
 sentence in your report noting that you observed it and controlled for it by timing your
 trials closely together.

If you're using **Case 2** (DMM-measured resistance) for your resistor value, there's a
related wrinkle: if you measured R with the DMM *before* the resistor was in the powered
circuit, that's a "cold" measurement. Once current flows for a while, the resistor will
self-heat slightly and its true in-circuit resistance may drift from that cold value. You
don't need to correct for this either, but it's a reasonable thing to mention if your Case 1
and Case 2 results don't overlap as cleanly as expected.

---

**My propagated uncertainty came out way too large, like the same order of magnitude
as P itself. What did I do wrong?**

The most common cause is a percent-to-decimal error. The datasheet specification is given
as a percentage (e.g., 0.5% of reading), which means 0.005, not 0.5. If you plug in 0.5
directly, your uncertainty will be inflated by a factor of 100. Go back to your u_V and
u_I calculations and confirm you converted the percentage to a decimal before multiplying.

---

**Do I need to memorize my report for the oral interview?**

No. You may bring your lab report and refer to it freely. What the interviewer is
assessing is whether you can explain the *reasoning* behind a result, not whether you can
recall a formula from memory. If asked to walk through the partial derivative computation,
it's completely fine to look at the formula in your report. The question is whether you
can explain what each term means and why the form matters.

The rubric requires you to demonstrate understanding in 3 of 5 categories. See
`LAB1_PIV_rubric_student.md` for what "understanding" looks like in each category.

---

## During the lab

**Should I average the three voltage and current readings, or use each trial separately?**

Use the mean of your three readings as your measured value of V and I. The standard error
of the mean from three readings (σ/√3) is typically much smaller than the manufacturer
specification uncertainty, so the spec will dominate your formal uncertainty estimate.
Record all three individual readings in your report to demonstrate repeatability, but
compute P and propagate uncertainty using the mean values.

---

## Monte Carlo simulation

**Which distribution should I use for V and I in the Monte Carlo simulation: Gaussian
or uniform?**

Both are defensible. The choice depends on what you know about the error source:

- **Uniform distribution** [measured value − u, measured value + u]: use this when all
 you know is a tolerance bound from the datasheet, with no information about the
 distribution shape. This is the more conservative and technically honest choice for a
 manufacturer specification.

- **Gaussian distribution** with σ = u/2: use this when you are treating the manufacturer
 spec as an approximately 95% confidence bound (k=2 coverage factor), which is common
 for precision instrument specifications. The factor of 2 means σ = u/2, not σ = u.

See W2_L2 slide 7 for the full reasoning. Either choice is acceptable. What matters is
that you state your choice explicitly in Section 5 of your report and justify it in one
sentence.

If you want a single defensible default: **use uniform**. It makes fewer assumptions.

---

**Why does my Monte Carlo standard deviation look like it's about half of my
partial-derivative uncertainty? Did I do something wrong?**

Probably not. This is a σ-convention issue. Here's what's happening:

The partial-derivative method computes δP using the full manufacturer spec value u as the
input uncertainty. The result δP represents the maximum bound.

If you set σ = u/2 in your Gaussian Monte Carlo (treating u as a ±2σ bound), then your
simulation input standard deviation is half the spec value. The output distribution
standard deviation will therefore also be approximately half of δP.

This isn't an error. It's a consistent consequence of your σ-convention. To make the
two methods give comparable magnitudes directly, either:
- Use uniform distributions (the bounds match the spec value directly), or
- Use Gaussian with σ = u (treating the spec as a 1σ bound: less standard, but it makes
 the comparison numerically direct)

The key requirement is to state your convention explicitly in Section 5 and check
consistency when writing Section 6. The comparison should explain *why* the numbers
relate the way they do, not just assert that they agree or disagree.

---

## Report writing

**I computed three different values of P: 0.2425 W, 0.2447 W, and 0.2404 W.
They're close but not the same. Which one is my "best estimate" for Section 7?**

Report the result from the form with the smallest propagated uncertainty. In this lab
that is typically P = IV, because both V and I are directly measured inputs and the
sensitivity coefficients are smaller than in the forms that involve R² terms.

Your choice should be *consistent* with your Section 4 sensitivity analysis. If you
concluded in Section 4 that P = IV has the smallest uncertainty, your Section 7 result
should use that form. The point of the sensitivity analysis isn't just arithmetic. It's
to make a reasoned choice about which result to report.

You may report all three forms for completeness, but designate one as your primary result
and explain why.

---

**Should I say "95% CI" or "manufacturer spec bound" when stating my result in
engineering form in Section 7?**

For Lab 1, use **"specification-based Type B standard uncertainty"** as your default after
converting the manufacturer limit using your stated distribution assumption.

- **"Manufacturer spec bound"** means the uncertainty was derived directly from the
 instrument datasheet specification, without a statistical sampling argument. This is
 accurate for what you did.

- **"95% CI"** means you can trace the bound to a specific probability statement, either
 from repeated measurements and a t-distribution, or from a manufacturer spec that
 explicitly states it corresponds to 95% coverage.

If a datasheet or calibration certificate gives an expanded uncertainty and coverage factor,
convert with `u=U/k` and preserve that stated basis. Do not relabel a manufacturer bound as
a frequentist confidence interval.

The general format is:
*P = [value] ± [uncertainty] W (combined standard uncertainty; specification-based Type B inputs; Taylor-series method)*

---

*Lab 1 FAQ | ASEN 3501 | E1 Week 2*
*Generated from simulated student gap analysis — 2026-05-26*
*Questions or corrections: contact the teaching team*
