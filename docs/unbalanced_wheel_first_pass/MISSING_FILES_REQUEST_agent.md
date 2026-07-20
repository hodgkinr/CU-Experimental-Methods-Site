# Missing Files Request — Unbalanced Wheel First Pass

This document lists the files that should be recovered manually before the second
pass of the Tier 1 ingestion workflow.

Target staging root:

```text
/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Planning/detailed_design/baseline_design/agentic_course_creation/manual_source_staging/unbalanced_wheel/
```

---

## HIGH PRIORITY

### 1. HEDS encoder datasheet

- **Why needed:** confirms manufacturer, model number, counts per revolution,
  output type, and any accuracy/resolution notes needed for the instrumentation
  section
- **Stage to:** `datasheets/`
- **Expected to enrich:**
  - `instrumentation/sensor_specs_summary_agent.md`
  - `instrumentation/datasheets/README_agent.md`

### 2. TA FAQ / troubleshooting PDF

- **Why needed:** should improve bad-run detection guidance, packet-loss symptoms,
  and rerun criteria
- **Stage to:** `faqs/`
- **Expected to enrich:**
  - `procedure/procedure_agent.md`
  - `notes/additional_notes_agent.md`

### 3. One confirmed balanced sample export

- **Why needed:** validates actual file format and export structure
- **Stage to:** `sample_data/`
- **Expected to enrich:**
  - `data/data_notes_agent.md`
  - `matlab/README_agent.md`

### 4. One confirmed unbalanced sample export

- **Why needed:** same as above, and useful for confirming naming conventions and
  expected θ/ω behavior
- **Stage to:** `sample_data/`
- **Expected to enrich:**
  - `data/data_notes_agent.md`
  - `matlab/README_agent.md`

### 5. Final student-facing SharePoint destination for data

- **Why needed:** the public site should show an external data link rather than
  shipping raw data files
- **Stage to:** no file required if you simply provide the final URL
- **Expected to enrich:**
  - `data/data_notes_agent.md`
  - any future student-facing data callout on the rendered site

---

## MEDIUM PRIORITY

### 6. Latest handout or draft handout

- **Why needed:** may tighten wording around procedure, trial counts, and report
  expectations
- **Stage to:** `handouts/`
- **Expected to enrich:**
  - `procedure/procedure_agent.md`
  - `model/derivation_agent.md`
  - `notes/additional_notes_agent.md`

### 7. Setup photos or short setup videos

- **Why needed:** reduces ambiguity in ramp setup, eccentric-mass orientation,
  and DAQ placement
- **Stage to:** `setup_media/`
- **Expected to enrich:**
  - `procedure/procedure_agent.md`

### 8. Reference MATLAB scripts or solution skeletons

- **Why needed:** clarifies whether any code is intended to be instructor-supplied
  rather than entirely student-authored
- **Stage to:** `analysis_code/`
- **Expected to enrich:**
  - `matlab/README_agent.md`

---

## OPTIONAL

### 9. Lecture notes or supplemental theory documents

- **Why needed:** may provide stronger explanation of modeling assumptions or the
  rationale for MODEL_3 vs. MODEL_4
- **Stage to:** `notes/`
- **Expected to enrich:**
  - `model/derivation_agent.md`
  - `notes/additional_notes_agent.md`

### 10. Archive-only historical writeups

- **Why needed:** mostly useful for instructor context rather than core student
  delivery
- **Stage to:** `notes/` or `handouts/`
- **Expected to enrich:**
  - `notes/additional_notes_agent.md`

---

## Recommended Staging Tree

```text
manual_source_staging/unbalanced_wheel/
  datasheets/
  faqs/
  handouts/
  sample_data/
  setup_media/
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
