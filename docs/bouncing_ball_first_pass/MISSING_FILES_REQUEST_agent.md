# Missing Files Request — Bouncing Ball First Pass

This document lists the files that should be recovered manually before the
second pass of the Tier 1 ingestion workflow.

Target staging root:

```text
/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Planning/detailed_design/baseline_design/agentic_course_creation/manual_source_staging/bouncing_ball/
```

---

## HIGH PRIORITY

### 1. Tracker tutorial PDF

- **Why needed:** student-facing support for the preferred free video-tracking workflow
- **Stage to:** `tutorials/`
- **Expected to enrich:**
  - `instrumentation/sensor_specs_summary_agent.md`
  - `procedure/procedure_agent.md`
  - `instrumentation/datasheets/README_agent.md`

### 2. Logger Pro tutorial PDF

- **Why needed:** support for the ITLL-only alternate video-tracking workflow
- **Stage to:** `tutorials/`
- **Expected to enrich:**
  - `instrumentation/sensor_specs_summary_agent.md`
  - `procedure/procedure_agent.md`
  - `instrumentation/datasheets/README_agent.md`

### 3. Variable-definition setup figure / ball-height diagram

- **Why needed:** the current procedure references a missing figure that visually
  defines `h0`, `hn`, `hn-1`, `tn`, `tn-1`, and `ts`
- **Stage to:** `setup_media/`
- **Expected to enrich:**
  - `procedure/procedure_agent.md`

### 4. Final student-facing SharePoint data URL

- **Why needed:** replaces the placeholder data link in the student-facing notes
- **Stage to:** no file required if you simply provide the URL
- **Expected to enrich:**
  - `data/data_notes_agent.md`

---

## MEDIUM PRIORITY

### 5. Richer handout bundle or LaTeX zip

- **Why needed:** may include missing images, tutorial references, or better
  formatting context than the catalog alone
- **Stage to:** `handouts/`
- **Expected to enrich:**
  - procedure
  - instrumentation
  - notes

### 6. Curated public sample video set

- **Why needed:** useful if the team wants to point students to one or two
  representative example videos through SharePoint
- **Stage to:** `sample_media/`
- **Expected to enrich:**
  - `data/data_notes_agent.md`
  - `procedure/procedure_agent.md`

### 7. Archived MATLAB GUI files or teacher reference scripts

- **Why needed:** helpful for instructor reference, even if not distributed to students
- **Stage to:** `analysis_code/`
- **Expected to enrich:**
  - `matlab/README_agent.md`
  - `notes/additional_notes_agent.md`

---

## OPTIONAL

### 8. Historical worked examples or grading notes

- **Why needed:** useful for instructor context and expectation-setting
- **Stage to:** `notes/`
- **Expected to enrich:**
  - `notes/additional_notes_agent.md`

---

## Recommended Staging Tree

```text
manual_source_staging/bouncing_ball/
  tutorials/
  handouts/
  setup_media/
  sample_media/
  analysis_code/
  notes/
```

---

## Resolution Note

Once these materials are staged, the second pass of the ingestion workflow should:

1. re-scan the staging directory
2. update the planning compilation
3. replace or narrow current `[MISSING]` markers
4. confirm whether the package is ready for deployment
