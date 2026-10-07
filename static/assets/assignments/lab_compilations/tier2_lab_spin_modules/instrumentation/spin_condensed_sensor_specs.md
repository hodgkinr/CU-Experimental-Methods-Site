# Tier 2 Spin Module: equipment and uncertainty information

## Measurement task

Use SC (bare-spacecraft) free-base records collected with the **base motor** to fit support inertia and effective base retardance. Use the separate `RW_freespin` records, collected with RW torque applied and the base free according to the supplied setup description, to estimate an effective wheel-side retardance and compare base acceleration with the corrected model. Historical `RW_*` records hold the base stationary; they support RW current/torque and wheel-speed characterization only. The free-base set has one run per torque and does not establish repeatability or validate all model-transfer assumptions.

## Equipment specifications and evidence status

| Quantity or channel | Source evidence | Value/status | Analysis role and limitation |
|---|---|---|---|
| Base motor torque constant | Maxon EC 45 flat motor catalog, part 200142, motor datasheet | Nominal \(K_{t,base}=25.5\) mN\,m/A. Datasheet lists nominal values; no ±0.05 tolerance or calibration uncertainty is stated. | Converts SC base-motor current to support torque. Any ±0.05 mN\,m/A used in the current first-pass analysis is an assumed working bound, not a verified calibration uncertainty. |
| RW motor torque constant | Maxon EC 45 flat motor catalog, part 251601, motor datasheet | Nominal \(K_{t,RW}=33.5\) mN\,m/A. Datasheet lists nominal values; no ±0.05 tolerance or calibration uncertainty is stated. | Converts RW motor current to the RW torque input. Any ±0.05 mN\,m/A used in the current first-pass analysis is an assumed working bound, not a verified calibration uncertainty. Keep separate from the base-motor constant. |
| Base encoder | Maxon MILE encoder, part 462005, associated with base motor | 2048 CPT, two-channel line-driver output. | Base-rate reference in the supplied processed records. One-, two-, or four-edge decoding convention and processed-rate scale/systematic accuracy are unresolved. |
| RW rate channel | Historical and `RW_freespin` data files | Rate logged in rpm; observed quantization is about 1.9536 rpm in the supplied data. | Historical records characterize wheel speed. Free-base records support wheel acceleration and base comparison, but absolute/relative rate reference and sign are not independently documented in available files. Hardware accuracy is unresolved. |
| Current channels | Historical data files and controller logging | Current range, calibration, transfer function, and accuracy are not documented in available sources. | First-pass calculation treats current uncertainty as negligible by assumption. This is not a sensor specification. |
| Time and DAQ | Timestamped records; nominal sampling near 50 Hz | Use recorded timestamps and inspect gaps/dropouts. No numerical timing uncertainty is specified. | Current solution estimates acceleration from rate versus actual time and treats DAQ/timing uncertainty as negligible by assumption. |
| MEMS gyro | ST LSM9DS1 datasheet | Device datasheet provides selectable ranges and sensitivity; lab values ±245 deg/s and 8.75 mdps/LSB are working settings/assumptions, not complete system accuracy. ODR, filter, alignment, synchronization, bias, and calibrated accuracy remain unresolved. | Optional sensor comparison only. It can change empirical acceleration uncertainty, not automatically the theoretical model/input uncertainty. |
| Motor current and wheel-speed operating limits | Current lab working instructions, pending instructor confirmation | ±2 A per motor and 3000 rpm RW speed are working limits, not verified here from the motor datasheets. | Use only with instructor approval. Wheel-speed feasibility depends on torque, duration, and initial speed; 3000 rpm is not a torque ceiling. |

## Uncertainty-source status for the first-pass model

- **Quantified in the current analysis:** SC and free-base within-record rate-slope errors; working assumed bounds for base and RW motor torque constants; SC support-fit and RW wheel torque-balance residual scatter. The residual-based empirical error scale uses only four branch-valid single-run points and includes bias; it is diagnostic, not repeatability.
- **Treated as negligible by explicit first-pass assumption:** current-channel uncertainty and DAQ/timing uncertainty. Students must label this assumption.
- **Unresolved:** encoder decoding, absolute/relative reference, sign, and processed-rate systematic accuracy; current calibration; independent between-run repeatability (one SC and one free-base RW record per torque); validity of transferring fitted support inertia/retardance to internal RW torque; wheel-loss constancy and adequacy/independence assumptions for residual-based discrepancy.

The manufacturer torque constants are **nominal specifications**, not traceable calibrations with the working ±0.05 mN\,m/A bounds. Do not describe the bounds as verified unless a calibration certificate or other supporting evidence is supplied.

## Historical data distinction

SC support files at nominal 4, 5, 6, 8, and 10 mN\,m contain free-base response to base-motor torque. New `RW_freespin` records at nominal labels 3, 4, 5, 6, 8, 10, and 12 mN\,m contain RW current/rate and base rate during user-described free-base RW runs. Historical `RW_*` files at 4, 5, 6, 8, and 10 mN\,m hold the base stationary. Stronger validation needs repeated free-base trials, documented encoder reference/sign, calibrated torque/current, synchronized timestamps, and base/wheel rates.

## Datasheet source documents

- Base motor: `../../../solution-agent/tier2-solution-agent/spins/data/Component Data Sheets/motor_base.pdf` (part 200142, catalog p. 265).
- Reaction-wheel motor: `../../../solution-agent/tier2-solution-agent/spins/data/Component Data Sheets/motor_reaction_wheel.pdf` (part 251601, catalog p. 300).
- Gyro: `../../../solution-agent/tier2-solution-agent/spins/data/Component Data Sheets/LSM9DS1_Datasheet_IMU.pdf`.

*Working specification for instructor review. Confirm channel definitions, encoder decoding, motor-current limits, and uncertainty inputs before release.*
