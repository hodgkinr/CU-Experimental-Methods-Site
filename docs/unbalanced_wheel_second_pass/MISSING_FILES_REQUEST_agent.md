# Missing Files Request — Unbalanced Wheel After Second Pass

This list has been narrowed after reviewing the staged materials.

Target staging root:

```text
/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Planning/detailed_design/baseline_design/agentic_course_creation/manual_source_staging/unbalanced_wheel/
```

---

## OPTIONAL FUTURE IMPROVEMENTS

### 1. Manual summary or extracted text from the TA FAQ PDF

- **Why needed:** would improve troubleshooting and bad-run examples
- **Stage to:** `faqs/` or `notes/`
- **Expected to enrich:**
  - `procedure/procedure_agent.md`
  - `notes/additional_notes_agent.md`

### 2. Encoder spec summary

- **Why needed:** fills in counts/rev, output type, and stated accuracy without needing a full PDF extraction tool
- **Stage to:** `datasheets/` or `notes/`
- **Expected to enrich:**
  - `instrumentation/sensor_specs_summary_agent.md`

---

### 3. Current raw export files

- **Why useful:** would confirm the present export format rather than relying on
  the historical solution report
- **Stage to:** `sample_data/`
- **Expected to enrich:**
  - `data/data_notes_agent.md`
  - `matlab/README_agent.md`

---

## RESOLVED IN THIS PASS

- final SharePoint data URL
- exact encoder model: `HEDS-5505`
- staged handout / richer procedure source
- confirmation of NI USB-6008 and `Dev 2` workflow
- historical MATLAB/data-loading pattern
- stronger evidence for wheel/encoder/DAQ operational structure
