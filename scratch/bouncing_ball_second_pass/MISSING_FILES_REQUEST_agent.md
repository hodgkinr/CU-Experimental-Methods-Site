# Missing Files Request — Bouncing Ball After Second Pass

This document records the remaining gaps after the staged second-pass review.

Target staging root, if additional recovery is attempted:

```text
/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Planning/detailed_design/baseline_design/agentic_course_creation/manual_source_staging/bouncing_ball/
```

---

## STILL MISSING

### 1. Logger Pro tutorial PDF

- **Why needed:** supports the historical ITLL-only alternate video-tracking
  workflow referenced in the 2018 handout appendix
- **Expected filename:** `Bouncing_Ball_Logger_Pro.PDF`
- **Stage to:** `tutorials/`
- **Expected to enrich:**
  - `instrumentation/sensor_specs_summary_agent.md`
  - `instrumentation/datasheets/README_agent.md`
  - `procedure/procedure_agent.md`

---

## OPTIONAL FOLLOW-ON MATERIALS

### 2. Curated public sample video set

- **Why helpful:** could give students an external example footage set through
  SharePoint without bundling large files into the course site
- **Stage to:** `sample_media/`
- **Expected to enrich:**
  - `data/data_notes_agent.md`
  - `procedure/procedure_agent.md`

### 3. Historical instructor notes or worked examples

- **Why helpful:** useful for planning-side context and expectation-setting
- **Stage to:** `notes/`
- **Expected to enrich:**
  - `notes/additional_notes_agent.md`

---

## RESOLVED IN THIS PASS

- Tracker tutorial PDF recovered
- 2018 handout PDF recovered
- LaTeX source bundle recovered
- variable-definition figure recovered in source context
- final student-facing SharePoint data link provided

---

## RESIDUAL POLICY NOTE

Historical internal CSV files are still present inside the canonical Bouncing
Ball planning compilation. They are not currently linked from the generated
public lab page, but they do continue to sync into the Forward bundle. If the
teaching team wants a stricter no-bundled-data policy, review those files in a
later cleanup pass.
