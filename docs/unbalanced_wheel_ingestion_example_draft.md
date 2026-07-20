# Worked Example — Tier 1 Lab Ingestion for Unbalanced Wheel

This document shows how the generic Tier 1 ingestion task should be applied to
the Unbalanced Wheel lab.

---

## Example Inputs

```text
LAB_KEY:             unbalanced_wheel
LAB_DISPLAY_NAME:    Unbalanced Wheel
CATALOG_DIR:         /Users/hodgkinr/Documents/GitHub/AES-Labs-Catalog/curriculum_2000_labs/Unbalanced_wheel
CATALOG_MD:          /Users/hodgkinr/Documents/GitHub/AES-Labs-Catalog/curriculum_2000_labs/Unbalanced_wheel/Unbalanced_wheel_Lab_Catalog.md
PLANNING_OUTPUT_DIR: /Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Planning/detailed_design/baseline_design/agentic_course_creation/claude_V1/assignments/lab_compilations/tier1_lab_unbalanced_wheel
MANUAL_STAGING_DIR:  /Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Planning/detailed_design/baseline_design/agentic_course_creation/manual_source_staging/unbalanced_wheel
TIER_KEY:            tier1
```

---

## What We Already Know

There is already a planning-side canonical package here:

```text
.../claude_V1/assignments/lab_compilations/tier1_lab_unbalanced_wheel/
```

There is also an older task-specific compile recipe here:

```text
.../tasks/labs/LAB_COMPILE_PARAMS_unbalanced_wheel.md
```

That older file is useful as historical guidance, but the new ingestion workflow
should prefer `AES-Labs-Catalog` as the live upstream source.

---

## First Pass Expectations

The agent should read:

- `Unbalanced_wheel_Lab_Catalog.md`
- `unbalanced_wheel_master_checklist.md`
- any readable text files in the same folder

From those sources, the agent should be able to recover at least:

- high-level lab description
- model hierarchy
- apparatus overview
- likely data channels
- likely common mistakes
- linked historical source references

The first pass should update:

- `procedure/procedure_agent.md`
- `model/derivation_agent.md`
- `model/model_equations_agent.md`
- `instrumentation/sensor_specs_summary_agent.md`
- `data/data_notes_agent.md`
- `matlab/README_agent.md`
- `notes/additional_notes_agent.md`
- `STATUS_REPORT_agent.md`
- `MISSING_FILES_REQUEST_agent.md`

---

## Likely Missing Files Request For Unbalanced Wheel

The first pass should probably request at least the following:

### High Priority

- HEDS encoder datasheet
  - Why: needed for instrumentation details and uncertainty context
  - Stage to: `manual_source_staging/unbalanced_wheel/datasheets/`
  - Enriches: `instrumentation/sensor_specs_summary_agent.md`

- TA FAQs PDF
  - Why: likely contains run-time troubleshooting and bad-data examples
  - Stage to: `manual_source_staging/unbalanced_wheel/faqs/`
  - Enriches: `procedure/procedure_agent.md`, `notes/additional_notes_agent.md`

- sample balanced and unbalanced data files
  - Why: confirms actual file format, delimiter, columns, and trimming logic
  - Stage to: `manual_source_staging/unbalanced_wheel/sample_data/`
  - Enriches: `data/data_notes_agent.md`, possibly `matlab/README_agent.md`

### Medium Priority

- latest handout or draft document if richer than the catalog
  - Stage to: `manual_source_staging/unbalanced_wheel/handouts/`
  - Enriches: procedure, theory, data, notes

- setup photos or short setup videos
  - Stage to: `manual_source_staging/unbalanced_wheel/setup_media/`
  - Enriches: `procedure/procedure_agent.md`

- reference MATLAB scripts if any exist
  - Stage to: `manual_source_staging/unbalanced_wheel/analysis_code/`
  - Enriches: `matlab/README_agent.md`

### Optional

- lecture notes or extra theory docs
  - Stage to: `manual_source_staging/unbalanced_wheel/notes/`
  - Enriches: `model/derivation_agent.md`, `notes/additional_notes_agent.md`

---

## Manual Staging Folder Shape

Recommended structure:

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

## Second Pass Expectations

Once the staged files are present, the agent should:

1. scan the staging tree
2. resolve previous `[MISSING]` tags where justified
3. tighten instrumentation and data-format details
4. update the status report to indicate deployment readiness

The agent should avoid padding the content. The goal is a clearer, more reliable
student-facing Tier 1 package, not maximum length.

---

## Publish Path After Second Pass

After the planning-side package is ready:

```bash
cd /Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Planning
./scripts/deploy_planning_to_site.sh
```

This will:

- sync the updated planning package into the Forward bundle
- regenerate `static/`
- regenerate `server/course_content/`

The resulting rendered page should appear at:

```text
CU-Experimental-Methods-Site/static/labs/tier1/unbalanced_wheel/index.html
CU-Experimental-Methods-Site/server/course_content/labs/tier1/unbalanced_wheel/index.html
```

---

## Definition of Done For This Pilot

For Unbalanced Wheel, the pilot is done when:

1. the planning compilation package is refreshed from `AES-Labs-Catalog`
2. the manual-file request is explicit and usable
3. the second pass can absorb staged restricted files cleanly
4. the package deploys through `deploy_planning_to_site.sh` without requiring site-only edits
