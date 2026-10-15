# ASEN 3501 Tier 2: Frequently Asked Questions

## Which experiment will we do?

All students complete the Wind Tunnel experiment for Fall 2026.

## What is the central task?

Use airspeed measurement uncertainty before testing to identify favorable, unfavorable, and unsupported wind-tunnel regions. Then reduce the released Clark Y-14 pressure measurements to aerodynamic coefficients, estimate coefficient uncertainty, and explain how the measurements compare with the supplied reference. The airspeed-informed condition choice is the centerpiece.

## Which airspeed measurements enter the model?

Use Pitot dynamic pressure (q), atmospheric pressure (p), and temperature (T) once in the released airspeed model. Do not count logged speed or derived density as additional independent inputs. The Scanivalve DSA3217 measures airfoil surface pressures; it does not enter the airspeed uncertainty calculation. The confirmed tunnel maximum is 60 m/s, distinct from individual sensor ranges.

## What uncertainty plots and Monte Carlo work are required?

Plot combined normalized and absolute standard uncertainty in airspeed across the tunnel operating range, along with the individual normalized contributions from dynamic pressure, atmospheric pressure, and temperature. Do not evaluate Taylor uncertainty expressions at exactly zero speed. Use three representative airspeeds and approximately 10,000 Monte Carlo trials per speed: a low speed where the dynamic-pressure bound is large relative to nominal pressure, a midrange speed, and a high speed near or beyond the candidate Pitot limit. Compare Monte Carlo standard deviations with Taylor predictions, report nonphysical draws, and flag sensor-overrange results. This limited check complements the full airspeed uncertainty plots; it does not replace them.

## What airfoil data are provided?

The available source dataset is historical, with 20 measurements at each angle from −15° to +16° and speed near 30.37 m/s. It is a single-speed measured sweep, not a multi-speed experiment. The dataset, data dictionary, and reference materials are available to students through Canvas. The historical data do not experimentally verify other recommended speeds.

## What should the coefficient uncertainty bars mean?

Use 10,000 trials for every measured angle included in your final coefficient plots. Use the designated rectangular bounds of ±49.8 Pa for Pitot q, ±4.9818 Pa for each scanner channel, and ±0.5° for angle of attack; share one q realization across all 16 taps per trial. Use the sample standard deviation as ±1 combined standard uncertainty, not a 95% interval.

## Is low relative uncertainty enough to recommend a test point?

No. A test condition must satisfy the experimental measurement requirement while also remaining within sensor ranges, tunnel operating limits, and applicable model assumptions. Consider absolute uncertainty, sensor range, aerodynamic behavior, and intended use. The minimum absolute uncertainty does not necessarily identify the best operating condition. A proposed sensor change may improve low-speed uncertainty while reducing the maximum measurable airspeed.

## What goes in the report and presentation?

The group report communicates the airspeed uncertainty analysis, test-region recommendation, relevant pressure reduction and coefficient uncertainty, measured aerodynamic trends, reference comparison, limitations, and one feasible setup or measurement-process improvement supported by analysis or observations. Evaluate both agreement and disagreement with the reference while considering Reynolds number and other condition differences. The client briefing presents the decision and evidence concisely.
