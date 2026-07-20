# Data Notes — Unbalanced Wheel: Inertia Distribution and Rolling Dynamics

---

## Data Access Policy For The Course Site

Raw and sample data files should **not** be bundled into the public course site
for this lab. Instead, the student-facing lab page should point to an external
SharePoint location managed manually by the instructional team.

**Placeholder link for current publication pass:**

- [Data - Link to Sharepoint - NEEDS UPDATE](#)

This placeholder should be replaced later with the correct SharePoint link once
the instructional team chooses the final data location.

---

## What the VI Records

The LabVIEW VI `UnbalancedWheel.vi` outputs:

| Channel | Symbol | Units | Description |
|---------|--------|-------|-------------|
| Angular position | θ | rad | Measured by HEDS optical encoder on wheel |
| Angular velocity | ω | rad/s | Computed numerically from encoder output |

Both channels are recorded vs. time. Based on the catalog description, the time
channel is expected to be included or implicit in the exported file, but this is
not yet confirmed from a real output file.

`[MISSING: Data file format not yet verified from a real export. Confirm file extension, delimiter, column order, whether time is included explicitly, and whether header lines are present.]`

---

## Data Collection Summary

| Trial | Configuration | Count |
|-------|---------------|-------|
| 1–2 | Balanced wheel (no eccentric mass) | 2 trials |
| 3–4 | Unbalanced wheel (eccentric mass installed) | 2 trials |

**Total:** 4 data files per lab session

**Version note:** The catalog and current compilation align to 2 balanced and 2
unbalanced trials for the more recent version of the lab.

---

## Reliable Data Range

Per the catalog and prior compiled notes: **0.5 rad < θ < 15 rad**

- **θ < 0.5 rad:** startup transient region
- **θ > 15 rad:** likely end-of-ramp effects or stop timing effects

Trim all data to the reliable range before computing residuals and statistics.

---

## Angular Acceleration

`[NEEDS INSTRUCTOR REVIEW — whether angular acceleration computation belongs in the 3501 version of this lab]`

The historical source lineage suggests this step was included in some versions of
the lab and questioned in later revisions. Keep it out of the student-facing core
workflow unless the teaching team explicitly wants it.

---

## MATLAB Data Loading

Students should write or adapt MATLAB code that:

- loads one trial file
- extracts θ and ω
- trims to the reliable range
- plots ω vs. θ
- computes residuals against the selected model

See `matlab/README_agent.md` for the expected analysis workflow.

---

## Sample Data Status

The catalog points to historical data folders, but this ingestion pass does not
copy raw data into the planning package or publish it to the site.

`[INSTRUCTOR TO PROVIDE: Final SharePoint location for student-facing data access.]`

`[MISSING_DATA: At least one confirmed balanced trial file and one confirmed unbalanced trial file are still needed during the second pass so the exact export format can be validated.]`

---

## Known Anomalies and Quirks

- Wireless packet drops can create gaps, plateaus, or spikes in the data
- Very low-θ data may not match the rolling model well because of startup effects
- Balanced and unbalanced runs should be named clearly and consistently

---

*This file was updated on 2026-07-20 by Codex GPT-5*
