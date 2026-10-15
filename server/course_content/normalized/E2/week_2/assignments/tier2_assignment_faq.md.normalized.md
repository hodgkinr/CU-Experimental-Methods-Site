# ASEN 3501 Tier 2: Frequently Asked Questions

## Which experiment will we do?

All students complete the Aeroelasticity / Wind Tunnel experiment for Fall 2026.

## What is the central task?

Use airspeed measurement uncertainty before testing to identify favorable, unfavorable, and unsupported wind-tunnel regions. Then reduce the released Clark Y-14 pressure measurements to aerodynamic coefficients, estimate coefficient uncertainty, and explain how the measurements compare with the supplied reference. The airspeed-informed condition choice is the centerpiece.

## Which airspeed measurements enter the model?

Use Pitot dynamic pressure (q), atmospheric pressure (p), and temperature (T) once in the released airspeed model. Do not count logged speed or derived density as additional independent inputs. The Scanivalve DSA3217 measures airfoil surface pressures; it does not enter the airspeed uncertainty calculation. The confirmed tunnel maximum is 60 m/s, distinct from individual sensor ranges.

## What uncertainty plots and Monte Carlo work are required?

Follow the [Aero procedure](../lab_compilations/tier2_lab_aeroelasticity/procedure/procedure_agent.md), which defines the required Monte Carlo workload. Plot combined normalized and absolute standard uncertainty in airspeed across 0–60 m/s, and the individual normalized (q,p,T) contributions. Do not evaluate either Taylor expression at exactly zero speed. Complete a limited Monte Carlo check with about 10,000 trials at each of three representative speeds; large convergence studies are not required. The generic normalized-uncertainty guide is supplemental and adds no Aero analyses.

## What airfoil data are provided?

The currently available source dataset is historical, with 20 measurements at each angle from −15° to +16° and speed near 30.37 m/s. It is a single-speed measured sweep, not a multi-speed experiment. The approved student data copy and reference materials will be linked in the Aero procedure pre-release checklist; do not look for them in instructor-only solution files. The historical coefficient data do not experimentally verify other recommended speeds.

## What should the coefficient uncertainty bars mean?

Use 10,000 trials for every measured angle included in your final coefficient plots. Use the provisional rectangular bounds of ±49.8 Pa for Pitot q, ±4.9818 Pa for each scanner channel, and ±0.5° for angle of attack; share one q realization across all 16 taps per trial. Use the sample standard deviation as ±1 combined standard uncertainty, not a 95% interval. The coefficient calculation does not re-perturb atmospheric pressure or temperature. These are provisional propagation assumptions, not confirmation of installed hardware.

## Is low relative uncertainty enough to recommend a test point?

No. Also consider absolute uncertainty, signal level, aerodynamic behavior, sensor range, tunnel limits, model validity, and intended use. Any 3% threshold is an illustration unless a specific decision rule is supplied.

## What goes in the report and presentation?

The group report communicates the airspeed uncertainty analysis, test-region recommendation, relevant pressure reduction and coefficient uncertainty, measured aerodynamic trends, reference comparison, limitations, and one feasible setup or measurement-process improvement supported by analysis or observations. Evaluate both agreement and disagreement with the reference while considering Reynolds number and other condition differences. The client briefing presents the decision and evidence concisely. The report remains assessed for CLO5.1; the presentation remains assessed for CLO1.5, CLO3.1, CLO3.2, and CLO5.2. These are the only Tier 2 assessments; no individual log, interview, contribution statement, or peer evaluation is added.

## What if an input or file is missing?

Use the designated provisional calculation scenario in the sensor summary and identify it as an instructional assumption, not verified calibration evidence or confirmation of installed hardware. Do not invent a sensor specification, channel meaning, calibration value, or operating limit. See the Aero procedure pre-release checklist for the two pending student packages.
