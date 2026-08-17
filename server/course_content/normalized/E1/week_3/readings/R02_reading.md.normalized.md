# Course Convention for Reporting Uncertainty and Intervals
## A Coleman & Steele–aligned reference for every ASEN 3501 result

The symbol after the ± sign is never self-explanatory; your reader must know what quantity it represents and how you obtained it.

---

This course follows the terminology used by Coleman & Steele, *Experimentation, Validation, and Uncertainty Analysis for Engineers*, 4th edition, with the GUM distinction between standard and expanded uncertainty. Use this page whenever you prepare a calculation, table, plot, caption, report, or presentation.

**Sample standard deviation, `s`** — the observed spread of individual repeated measurements. Report it when the variability of individual observations matters.

**Standard error, `s/√n`** — the estimated standard deviation of the sample mean when the observations support that calculation. It describes precision of the estimated mean, not the spread of individual observations.

**Standard uncertainty, `u_i`** — an elemental uncertainty expressed as an estimated standard deviation. Coleman & Steele distinguish **random standard uncertainty**, associated with effects that vary during the measurement period, from **systematic standard uncertainty**, associated with effects that remain invariant during that period. A Type A or Type B label describes *how the uncertainty was evaluated*, not whether the underlying effect is random or systematic.

**Type A evaluation** — evaluation by statistical analysis of observations. **Type B evaluation** — evaluation using other evidence, such as a calibration certificate, manufacturer limit, resolution, prior data, or engineering judgment. A manufacturer limit is not automatically a standard uncertainty. State the assumed probability model or coverage statement used to convert the limit. For example, a symmetric hard bound `±a` modeled as uniform gives `u=a/√3`; a certificate value `U` with coverage factor `k` gives `u=U/k`.

**Combined standard uncertainty, `u_c`** — the standard uncertainty of a result after propagating all relevant elemental standard uncertainties through the data-reduction equation. Combine components only after putting them on a common standard-uncertainty basis. Include covariance terms when there is evidence that inputs share an error source; in introductory work, identify plausible shared sources even when a covariance estimate is not available.

**Expanded uncertainty, `U = k u_c`** — an interval half-width formed from the combined standard uncertainty and a stated coverage factor. The course default for a final Taylor-series-method result is `estimate ± U`, with `k=2`, when that approximation is justified. Write the basis explicitly: for example, `P = 25.7 ± 1.2 W (expanded uncertainty, k=2, Taylor-series method)`. Do not call every `k=2` result a “95% confidence interval.”

**Confidence interval** — a frequentist interval produced by a statistical procedure for a parameter such as a population mean or a difference of means. A 95% confidence procedure produces intervals that contain the fixed parameter in 95% of repeated applications under its assumptions. It is not a 95% probability statement about the realized interval.

**Prediction interval** — an interval for a future observation or outcome. It is usually wider than a confidence interval for the mean because it includes observation-to-observation variability as well as uncertainty in the estimated mean.

**Monte Carlo coverage interval** — an interval containing a stated percentage of the simulated output distribution. Report the input distributions, dependence assumptions, sample count, and interval rule. For example: `central 95% Monte Carlo coverage interval, 2.5th–97.5th percentiles`. Do not relabel it as a frequentist confidence interval.

For plots, replace the generic phrase **error bars** with the quantity actually shown: `±1 standard uncertainty`, `expanded uncertainty, k=2`, `95% confidence interval for the mean`, or `central 95% Monte Carlo coverage interval`. For comparisons, build an interval for the *difference* when statistical inference is needed, then compare that interval with a pre-specified engineering acceptance or equivalence region. Overlap of two separate intervals is only a visual clue, not the decision rule.

---

**The Takeaway:** Reduce every component to a standard-uncertainty basis before propagation, distinguish statistical confidence from uncertainty coverage, and label every interval with its method and meaning.
