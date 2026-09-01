# Sample Data - Unbalanced Wheel

---

## Data Access

Use the SharePoint folder containing sample data:

- [Unbalanced Wheel Data Folder](https://o365coloradoedu.sharepoint.com/:f:/r/sites/AEROENGR-Labspace-Labs/Shared%20Documents/Labs/01_Junior%20Level%20Labs/3501%20-%20Experimental%20Methods/Summer%202026%20-%20Course%20Development/Tier%201%20Lab%20Snapshots%20-%20STUDENT%20FACING/Unbalanced%20Wheel?d=w62fd27c495c14e6282446c9f6737c28b&csf=1&web=1&e=z9P8Yt)

Do not expect raw data files to be attached directly to this course page. The student-facing folder should contain data and starter materials only, not solution scripts such as `encoder_plot_SOLUTIONS.m`.

---

## What the Current ESP32 System Records

The current Summer 2026 hardware uses an ESP32 web interface. The encoder
monitor website saves CSV files to a student's phone using names such as
`encoder_data_#`.

Per the updated lab catalog, the current CSV columns are:

| Channel | Symbol | Units | Description |
|---------|--------|-------|-------------|
| Index | — | unitless | Sample counter |
| Time | t | ms | Timestamp at capture |
| QuadEncoder | — | pulse count | Current relative position of the quadrature encoder |
| LS7184Encoder | — | pulse count | Current relative position of the step/direction encoder |

Older LabVIEW/NI exports used a different processed format
(`time, theta, omega`). That format should be treated as historical reference
only unless your instructor intentionally provides old-hardware data.

---

## Data Collection Summary

| Trial | Configuration | Count |
|-------|---------------|-------|
| 1–2 | Balanced wheel (no eccentric mass) | 2 trials in the current handout lineage |
| 3–4 | Unbalanced wheel (eccentric mass installed) | 2 trials in the current handout lineage |

**Total current expectation:** 4 data files per lab session

## Reliable Data Range

Per the catalog, prior compilation, staged handout, and staged historical code:
**0.5 rad < θ < 15 rad**, unless the teaching team updates this range for the outside-ramp setup

- **θ < 0.5 rad:** startup transient region
- **θ > 15 rad:** likely stopping or ramp-end effects; confirm the final cutoff for the outside-ramp setup

The staged historical MATLAB code explicitly trims data to this range.

---

## File Naming Conventions

The current encoder monitor website automatically saves files as:

- `encoder_data_#`

After saving, rename files using the updated catalog convention:

- `encoder_data_test#_balanced.csv`
- `encoder_data_test#_unbalanced.csv`

Use test numbers that make the two balanced trials and two unbalanced trials
unambiguous.

---

## MATLAB Data Loading

Students should write or adapt MATLAB code that:

- loads one CSV trial file from the ESP32 encoder monitor
- converts encoder counts and timestamps into θ and ω as required by the current analysis workflow
- trims to the reliable range
- plots ω vs. θ
- computes residuals against the selected model

The historical `load(filename)` workflow applies to old processed text exports.
For current CSV files, use a CSV-aware reader and the current data dictionary
above.

See `matlab/README_agent.md` for the expected analysis workflow.

---

## Known Anomalies and Quirks

- Wireless packet drops can create gaps, plateaus, or spikes in the data
- Very low-θ data may not match the rolling model well because of startup effects
- Balanced and unbalanced runs should be named clearly and consistently

---
