# ASEN 3501 — Tier 2 Experimental Investigation
## Choose Useful Wind-Tunnel Conditions

**Fall 2026 experiment:** Wind Tunnel

**Role:** You are an engineering consultant evaluating an aerospace experiment.

**Client question:** Which wind-tunnel conditions produce useful aerodynamic results for the intended measurement, which conditions should be avoided or treated cautiously, and what feasible change could improve the useful test envelope?

**Format:** Large group, four in-person lab working days, two in-person lectures, one group technical report, and one short client briefing.

## Purpose

Tier 1 focused on understanding an existing experiment and performing pointwise and residual analysis. Tier 2 asks you to evaluate a measurement system across operating conditions and recommend improvements.

You will use quantitative uncertainty analysis to make an informed choice about wind-tunnel conditions. You will characterize the airspeed measurement chain, identify useful and unsupported regions, then apply the supplied airfoil pressure measurements to aerodynamic coefficients. The airspeed decision is the centerpiece: a low relative uncertainty alone does not make a condition useful.

Keep the two evidence streams distinct: the operating-region recommendation comes from airspeed uncertainty and practical limits; the available aerodynamic coefficient data are a historical single-speed sweep. Do not present that sweep as experimental verification of other recommended speeds.

## Learning goals

By the end of Tier 2, you should be able to:

1. Identify measured inputs in the wind-tunnel airspeed model and explain their uncertainty assumptions and ranges.
2. Calculate and interpret absolute and normalized standard uncertainty in airspeed across the tunnel envelope.
3. Use uncertainty and practical sensor limits to justify favorable and unfavorable test conditions as well as potential improvements.
4. Reduce airfoil pressure data to $C_p$, $C_n$, $C_a$, $C_l$, and $C_d$, and estimate uncertainty in measured $C_l$ and $C_d$.
5. Compare measured aerodynamic behavior with the supplied reference and explain physical trends and limitations.

## Required investigation

Complete the sequence in the [Aero Tier 2 instructions](../lab_compilations/tier2_lab_aeroelasticity/procedure/procedure_agent.md):

1. **Model the airspeed measurement.** Use Pitot dynamic pressure, atmospheric pressure, and temperature as the primitive inputs. Keep the confirmed 60 m/s tunnel maximum distinct from the range of each sensor; surface-pressure scanner uncertainty does not enter the airspeed calculation.
2. **Map airspeed uncertainty across conditions.** Plot combined normalized standard uncertainty (%) and absolute standard uncertainty (m/s) across 0–60 m/s, and show the individual normalized contributions from dynamic pressure, atmospheric pressure, and temperature. Do not evaluate the Taylor airspeed uncertainty expressions at exactly zero speed; relative uncertainty is also undefined there. Mark mathematical extrapolation and sensor limits clearly.
3. **Check the airspeed model with Monte Carlo.** At no less than five representative speeds, use approximately 10,000 trials per speed, compare Monte Carlo standard deviations with Taylor predictions, and explain low-speed nonlinearity and any sensor over-range results. The detailed Aero procedure defines this Monte Carlo scope; the general uncertainty guide is supplemental.
4. **Make a test-condition recommendation.** Identify favorable and unfavorable or unsupported regions using uncertainty, signal and sensor ranges, the tunnel limit, and the intended measurement. State a decision rule; a 3% line, if used, is an illustration rather than a course-wide acceptance rule. Recommend one feasible improvement to the experimental setup or measurement process, supported by your uncertainty analysis or experimental observations.
5. **Reduce and interpret the airfoil measurements.** Use the released pressure-port map, geometry, and data dictionary to calculate $C_p$, $C_n$, $C_a$, $C_l$, and $C_d$. Apply 10,000 Monte Carlo trials per angle of attack for every measured angle included in your final coefficient plots; estimate standard uncertainty in $C_l$ and $C_d$ and plot ±1 combined standard-uncertainty bars. Compare agreement and disagreement with the supplied reference while accounting for differences in Reynolds number and experimental conditions. Agreement is not presumed.
6. **Connect the results.** Explain how the initial airspeed uncertainty analysis informs the selected conditions and how the coefficient data support and limit the aerodynamic conclusions.

## Deliverables and assessment

There are two Tier 2 assessment components.

### Group technical report

Submit one concise report communicating the airspeed model and uncertainty plots, your test-region recommendation, one feasible setup or measurement-process improvement supported by your analysis or observations, the relevant coefficient reduction and uncertainty method, the measured aerodynamic trends, comparison with the supplied reference, and limitations. Use labeled figures or tables with units.

### Client briefing

Present one quad chart or equivalent concise briefing that makes the decision, supporting uncertainty and aerodynamic evidence.

## Additional resources

- [Detailed Aero lab instructions, measurement models, equations, and analysis workflow](../lab_compilations/tier2_lab_aeroelasticity/procedure/procedure_agent.md)
- [Aero sensor and data-input summary](../lab_compilations/tier2_lab_aeroelasticity/instrumentation/sensor_specs_summary_agent.md)
- [Normalized uncertainty guide](student-guides/TIER2_normalized_uncertainty_guide.pdf)
