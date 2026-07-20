# Data Notes — Unbalanced Wheel: Inertia Distribution and Rolling Dynamics

---

## Data Access Policy For The Course Site

Raw and sample data files should **not** be bundled into the public course site
for this lab. Instead, the student-facing lab page should point to an external
SharePoint location managed manually by the instructional team.

**Student-facing data link:**

- [Data - Link to Sharepoint - NEEDS UPDATE](https://o365coloradoedu.sharepoint.com/:f:/r/sites/AEROENGR-Labspace-Labs/Shared%20Documents/Labs/Extra%20Historical%20Labs/Unbalanced%20Wheel%20Lab/ASEN%202003%20Archived%20Unbalanced%20Wheel%20Lab/Data?csf=1&web=1&e=UcOUdQ)

---

## What the VI Records

The LabVIEW VI `UnbalancedWheel.vi` outputs:

| Channel | Symbol | Units | Description |
|---------|--------|-------|-------------|
| Time | t | s | Present in historical exported files; expected as column 1 |
| Angular position | θ | rad | Measured by wheel encoder; historical exports use column 2 |
| Angular velocity | ω | rad/s | Computed numerically from encoder output; historical exports use column 3 |

The staged historical solution report includes MATLAB code that loads files with:

```matlab
data = load(filename);
th_exp = data(:,2);
w_exp  = data(:,3);
```

This is strong evidence that the historical export format used:

- plain text numeric files readable by MATLAB `load(...)`
- column 1 = time
- column 2 = theta
- column 3 = omega

`[NEEDS INSTRUCTOR REVIEW: Confirm that the current export format still matches the historical 3-column text format before publishing student instructions as final.]`

---

## Data Collection Summary

| Trial | Configuration | Count |
|-------|---------------|-------|
| 1–2 | Balanced wheel (no eccentric mass) | 2 trials in the current handout lineage |
| 3–4 | Unbalanced wheel (eccentric mass installed) | 2 trials in the current handout lineage |

**Total current expectation:** 4 data files per lab session

**Historical note:** the staged 2013 sample solution uses 3 balanced and 3
unbalanced trials. That older structure is useful as a reference for analysis
workflow, but it should not override the more recent handout lineage without an
explicit instructor decision.

---

## Reliable Data Range

Per the catalog, prior compilation, staged handout, and staged historical code:
**0.5 rad < θ < 15 rad**

- **θ < 0.5 rad:** startup transient region
- **θ > 15 rad:** likely end-of-ramp effects or stop timing effects

The staged historical MATLAB code explicitly trims data to this range.

---

## File Naming Conventions

The staged historical solution uses names like:

- `balanced_trial1.txt`
- `balanced_trial2.txt`
- `balanced_trial3.txt`
- `unbalanced_trial1.txt`
- `unbalanced_trial2.txt`
- `unbalanced_trial3.txt`

These names should be treated as **historical examples**, not necessarily the
current required naming convention.

`[INSTRUCTOR TO PROVIDE: Final naming convention if the lab team wants students to use a standard export/file-naming pattern.]`

---

## Angular Acceleration

`[NEEDS INSTRUCTOR REVIEW — whether angular acceleration computation belongs in the 3501 version of this lab]`

The staged 2019 `.tex` still includes angular acceleration language, but also
contains an instructor red-note suggesting that part should be removed.

Recommendation for 3501: keep the core workflow focused on:

- loading data
- trimming to the reliable θ range
- comparing ω vs. θ
- computing residuals and statistics

unless the teaching team wants angular acceleration for a specific pedagogical
reason.

---

## MATLAB Data Loading

Students should write or adapt MATLAB code that:

- loads one trial file
- extracts θ and ω
- trims to the reliable range
- plots ω vs. θ
- computes residuals against the selected model

The staged historical report confirms that a simple `load(filename)` approach
was used successfully for earlier text exports.

See `matlab/README_agent.md` for the expected analysis workflow.

---

## Sample Data Status

The staged materials now include a **historical sample solution report**, which
confirms likely file structure and analysis habits, but the staging folder still
does **not** contain a confirmed raw balanced export file and confirmed raw
unbalanced export file for direct validation.

The catalog points to historical data folders, but this ingestion pass still does
not copy raw data into the planning package or publish it to the site. Students
should use the SharePoint folder linked above for data access.

`[MISSING_DATA: At least one confirmed current balanced trial file and one confirmed current unbalanced trial file are still needed if the team wants the data format documented with full confidence.]`

---

## Known Anomalies and Quirks

- Wireless packet drops can create gaps, plateaus, or spikes in the data
- Very low-θ data may not match the rolling model well because of startup effects
- Balanced and unbalanced runs should be named clearly and consistently

---

*This file was updated on July 20, 2026 by Codex GPT-5*
