# ASEN 3501 — Tier 2 Experimental Investigation
## Choose Useful Wind-Tunnel Conditions

**Fall 2026 experiment:** Wind Tunnel

**Role:** You are an engineering consultant evaluating an aerospace experiment.

**Client question:** Which wind-tunnel conditions produce useful aerodynamic results for the intended measurement, which conditions should be avoided or treated cautiously, and what feasible change could improve the useful test envelope?

**Format:** Large group, four in-person lab working days, two in-person lectures, one group technical report, and one short client briefing.

## Purpose

Tier 1 focused on understanding an existing experiment and performing pointwise and residual analysis. Tier 2 asks you to evaluate a measurement system across operating conditions and recommend improvements.

You will use quantitative uncertainty analysis to evaluate the capabilities of the existing wind-tunnel measurement system and determine whether it can satisfy specific experimental requirements. First, you will characterize the airspeed measurement chain across its operating range, identifying favorable, unfavorable, and unsupported conditions. Then, you will investigate how changing the differential-pressure instrumentation could improve low-speed measurement capability, and what limitations that change might introduce at higher speeds.

You will also analyze the supplied airfoil pressure measurements to determine aerodynamic coefficients and interpret the results. The central engineering challenge is to use uncertainty analysis to make defensible decisions about experimental conditions and instrumentation, rather than simply identifying the minimum of an uncertainty curve.

Keep the two evidence streams distinct: the operating-region recommendation comes from airspeed uncertainty and practical limits; the available aerodynamic coefficient data are a historical single-speed sweep. Do not present that sweep as experimental verification of other recommended speeds.

## Learning goals

By the end of Tier 2, you should be able to:

1. Identify measured inputs in the wind-tunnel airspeed model and explain their uncertainty assumptions and ranges.
2. Calculate and interpret absolute and normalized standard uncertainty in airspeed across the tunnel operating envelope, explaining the physical origins of their different trends.
3. Determine whether the existing instrumentation satisfies a specified experimental requirement, and evaluate how a change in pressure-sensor accuracy or full-scale range affects the usable operating envelope.
4. Reduce airfoil pressure data to pressure coefficients and estimate uncertainty in measured lift and drag coefficients.
5. Compare measured aerodynamic behavior with the supplied reference and explain physical trends and limitations.

## Required investigation

See Canvas documents for more information and specific guides.

1. **Model the airspeed measurement.** Use Pitot dynamic pressure, atmospheric pressure, and temperature as the primitive inputs. Keep the confirmed 60 m/s tunnel maximum distinct from the range of each sensor; surface-pressure scanner uncertainty does not enter the airspeed calculation.
2. **Map airspeed uncertainty across conditions.** Plot combined normalized standard uncertainty (%) and absolute standard uncertainty (m/s) across 0–60 m/s, and show the individual normalized contributions from dynamic pressure, atmospheric pressure, and temperature. Do not evaluate the Taylor airspeed uncertainty expressions at exactly zero speed; relative uncertainty is also undefined there. Mark mathematical extrapolation and sensor limits clearly.
3. **Check the airspeed model with Monte Carlo.** At three representative speeds, use approximately 10,000 trials per speed, compare Monte Carlo standard deviations with Taylor predictions, and explain low-speed nonlinearity and sensor-range limitations. Select a low speed where the dynamic-pressure bound is large relative to nominal pressure, a midrange speed, and a high speed near or beyond the candidate Pitot limit. The detailed Aero procedure defines this Monte Carlo scope; the general uncertainty guide is supplemental.
4. **Reduce and interpret the airfoil measurements.** Use the released pressure-port map, geometry, and data dictionary to calculate pressure coefficients and use those to determine lift and drag coefficients. Apply 10,000 Monte Carlo trials per angle of attack for every measured angle included in your final coefficient plots; estimate standard uncertainty in lift and drag coefficients and plot ±1 combined standard-uncertainty bars. Compare agreement and disagreement with the supplied reference while accounting for differences in Reynolds number and experimental conditions.
5. **Connect the results.** Explain how the initial airspeed uncertainty analysis informs the selected conditions and how the coefficient data support and limit the aerodynamic conclusions.
6. **Evaluate an experimental requirement and recommend an improvement.**

Using your uncertainty analysis, identify favorable, unfavorable, and unsupported operating regions based on measurement uncertainty, signal strength, sensor ranges, the 60 m/s tunnel limit, and the intended measurement. Clearly state and justify your decision rule; a 3% uncertainty threshold, if used, is illustrative rather than a universal acceptance criterion.
 **Example client requirement**
 The client wishes to conduct a wind-tunnel experiment at **10 m/s**, with normalized standard uncertainty in airspeed **no greater than 1%**.
 To evaluate this requirement:
 - **Assess current capability:** Determine whether the existing measurement system can satisfy the requirement.
 - **Determine required accuracy:** Calculate the maximum allowable standard uncertainty in differential pressure, accounting for temperature and atmospheric-pressure uncertainty.
 - **Evaluate alternatives:** Identify a feasible alternative differential-pressure sensor or measurement configuration that could meet the requirement.
 - **Quantify the tradeoff:** Determine how the proposed change affects the maximum measurable airspeed and the overall usable operating range.

 **Final recommendation:** Recommend an instrumentation or measurement-process improvement supported by your quantitative analysis. Explain the expected benefit and any associated tradeoffs, distinguishing predicted improvements from experimentally verified performance.

## Deliverables and assessment

There are two Tier 2 assessment components.

### Group technical report

Submit one concise technical report communicating the airspeed measurement model, absolute and normalized uncertainty plots, and the resulting usable operating envelope. Evaluate the client's 10 m/s measurement requirement and present an evidence-based instrumentation recommendation, including the expected effect on both low-speed uncertainty and maximum measurable airspeed.

Also include the relevant aerodynamic coefficient reduction and uncertainty methodology, measured aerodynamic trends, comparison with the supplied reference, and limitations. Use labeled figures or tables with appropriate units. Clearly distinguish predictions about alternative instrumentation from conclusions supported by the historical aerodynamic measurements.

### Client briefing

Present one concise briefing that communicates the recommended operating conditions, how the 10 m/s requirement can be satisfied, the proposed instrumentation improvement and its tradeoffs, and the supporting uncertainty and aerodynamic evidence.

## Additional resources

See Canvas documents for more information and specific guides.

### Acknowledgment

The assignment is inspired by the uncertainty-analysis approach used in ASEN 6011, Experimental Fluid Mechanics, taught by Professor John Farnsworth. Students interested in experimental methods, fluid mechanics, aerospace testing, or measurement science are strongly encouraged to consider ASEN 6011. That course develops these ideas in substantially greater depth, both through its assignments and through the broader course sequence.
