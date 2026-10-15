# Aeroelasticity Tier 2: Sensor Inputs and Data Release Status

This sheet distinguishes confirmed equipment facts from the designated provisional calculation scenario. Use the scenario below for the required student calculations. It is not evidence that the listed candidate sensors are installed or calibrated.

## Measurement chain and limits

| Measurement | Equipment or working model | Range / uncertainty input | Status and role |
|---|---|---|---|
| Tunnel speed | PILOT low-speed wind tunnel | Maximum 60 m/s | **Confirmed tunnel limit.** This does not imply that every sensor measures through 60 m/s. |
| Airfoil surface pressure | Scanivalve DSA3217 | Configured ±10 inH₂O (±2490.9 Pa); stated accuracy ±0.20% of 10 inH₂O = ±4.9818 Pa | **Configuration confirmed.** Accuracy row matched to the configured range. Treat ±4.9818 Pa as a rectangular bound only for this exercise; resulting standard uncertainty is 2.876 Pa. Calibration date, zero, resolution, channel covariance, and individual channel behavior remain open. |
| Pitot dynamic pressure (q) | Honeywell ABP2DDAN005NDAA3XX candidate | Candidate positive range 0 to +5 inH₂O (1245.44 Pa); scenario error bound ±49.8 Pa | **Provisional calculation scenario.** Installed identity, range, zero, calibration, and conversion path are unverified. At the reference state, requiring nominal (q) plus this bound to remain below full scale gives an approximate planning edge of 49.6 m/s; this is not a confirmed usable limit. |
| Atmospheric pressure (p) | MPX4250A candidate | Candidate maximum-error bound ±3.45 kPa | **Provisional candidate.** Installed identity, channel conversion, and suitability over local pressure conditions are unverified. |
| Temperature (T) | LM35D conservative candidate | Candidate bound ±1.5 K | **Provisional candidate.** Installed variant and conversion are unverified. Use the instructor-designated case. |
| Angle of attack α | Recorded angle channel / fixture | Working bound ±0.5° | **Provisional analysis assumption.** Source and uncertainty meaning are unverified. |

For the designated airspeed calculation scenario, model the stated $q,p,T$ bounds as independent rectangular distributions. Convert each bound $a$ to standard uncertainty $u=a/\sqrt3$, then use the $q,p,T$ airspeed model in the detailed instructions. Independence is an analysis assumption, not a demonstrated property of the installed system. Do not use the scanner uncertainty in the airspeed calculation. For coefficient Monte Carlo, use 10,000 trials per plotted measured angle, independent uniform/rectangular scanner bounds of ±4.9818 Pa, a uniform/rectangular angle bound of ±0.5°, and one shared Pitot $q$ draw per trial from its ±49.8 Pa bound.

## Historical measurement file and data dictionary

The current instructional-team source file is `ASEN2802_InfiniteWing_FullRange (1).csv`. It contains 640 measured rows, 30 columns, 20 samples at each integer angle from −15° through +16°, and airspeed from 29.990 to 30.750 m/s (mean about 30.37 m/s). It is historical single-speed data, not a new multi-speed test matrix. The approved student-accessible file and dictionary will be linked in the Aero procedure pre-release checklist; students must not retrieve it from an instructor-only solution directory.

The source column order and units are:

1. Atmospheric Temperature [K]
2. Atmospheric Pressure [Pa]
3. Atmospheric Density [kg/m^3]
4. Airspeed [m/s]
5. Pitot Dynamic Pressure [Pa]
6. Aux Dynamic Pressure [Pa]
7. Actual Voltage [V]
8. Angle of Attack [deg]
9. Spanwise Position [in]
10. Sting Axial Force [N]
11. Sting Normal Force [N]
12. Sting Pitching Moment [Nm]
13–14. ELD Probe X-Axis, Y-Axis [mm]
15–30. Scanivalve Pressure 1–16 [Pa]

Surface-pressure fields are in Pa. The approved data package will state pressure reference, exact column names, and any flags. The current reduction uses Pitot (q) and the connected surface-pressure channels. The auxiliary-pressure field is not used pending its definition. The historical file has no timestamps or unique run IDs.

## Airfoil geometry and reference release

The model is a Clark Y-14 infinite wing with nominal 3.5 in (0.0889 m) chord. The detailed student procedure contains the connected channel/port map and coordinates. Channels 1–8 map to ports 1–8; channel 9 to port 10; channel 10 to port 12; channel 11 to port 14; channels 12–16 to ports 16–20. Ports 9, 13, and 15 are disconnected; port 11 is the theoretical trailing-edge point. The pending student data and reference package links are listed in the procedure's pre-release checklist.

The current comparison uses empirical Clark Y-14 data from NACA TR 628 near $Re\approx3.02\times10^6$. The historical tunnel sweep is near $Re\approx1.46\times10^5$; students should evaluate agreement and disagreement while recognizing this condition mismatch, not treat the comparison as same-condition validation. Current analysis uses −8° through +12°. The reference file and citation will be linked in the Aero procedure pre-release checklist.
