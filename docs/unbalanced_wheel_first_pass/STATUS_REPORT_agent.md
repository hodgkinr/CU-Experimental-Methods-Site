# Status Report — Tier 1 Ingestion First Pass: Unbalanced Wheel

**Run date:** 2026-07-20
**Workflow:** `CLAUDE_CODE_TASK_TIER1_LAB_INGEST.md`
**Source directory:** `/Users/hodgkinr/Documents/GitHub/AES-Labs-Catalog/curriculum_2000_labs/Unbalanced_wheel`
**Primary catalog file:** `Unbalanced_wheel_Lab_Catalog.md`
**Companion file:** `unbalanced_wheel_master_checklist.md`
**Run type:** First pass from Labs Catalog

---

## Summary

The existing Unbalanced Wheel planning compilation was already strong and broadly
consistent with the current `AES-Labs-Catalog` entry. This first-pass ingestion
therefore focuses on:

1. reaffirming the catalog as the upstream source of truth
2. preserving the existing high-value student-facing structure
3. adding a formal missing-files handoff for manual recovery
4. updating the data policy so the course site points to an external SharePoint
   link rather than bundling raw data files

The package is useful for review and refinement, but it is **not yet ready for
full deployment** because several important supporting materials still need to be
manually recovered.

**Current status:** `READY FOR LIMITED REVIEW ONLY`

---

## What Was Confirmed From Catalog Sources

The catalog and checklist support the following as stable first-pass content:

- high-level experiment description
- four-model hierarchy (balanced frictionless, balanced with friction, unbalanced
  particle, unbalanced rigid body)
- apparatus concept (ramp, wheel, encoder, DAQ, LabVIEW)
- recent trial structure (2 balanced + 2 unbalanced)
- major procedural warning about blocking the wireless line of sight
- data-analysis emphasis on residuals and model comparison
- existence of historical handouts, videos, analysis folders, and FAQs via linked
  external resources

---

## First-Pass Changes Made In This Run

### Updated

- `data/data_notes_agent.md`
  - added course-site data policy
  - added placeholder student-facing SharePoint link:
    `Data - Link to Sharepoint - NEEDS UPDATE`
  - removed expectation that raw sample files are published directly with the site

### Added

- `MISSING_FILES_REQUEST_agent.md`
  - explicit handoff document for manual source recovery

### Refreshed

- `STATUS_REPORT_agent.md`
  - rewritten to reflect the new catalog-first ingestion workflow

---

## Remaining Gaps After First Pass

### High Priority

- encoder datasheet and measurement specs
- TA FAQ / troubleshooting PDF
- one verified balanced sample export
- one verified unbalanced sample export
- final SharePoint data destination for students

### Medium Priority

- richer current handout or draft handout
- setup photos or short setup videos
- reference MATLAB scripts if the teaching team wants exemplars available

### Optional

- lecture notes or supplemental theory docs
- archive materials that improve historical context but do not change execution

---

## Publish Readiness Assessment

### Ready now

- theory/model pages for review
- procedure page for review
- instrumentation page as a partial first pass
- notes page for review

### Not ready yet

- final student-facing data access details
- complete instrumentation specs
- best-available troubleshooting guidance

---

## Required Next Step

Use `MISSING_FILES_REQUEST_agent.md` to collect manual source materials into:

```text
/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Planning/detailed_design/baseline_design/agentic_course_creation/manual_source_staging/unbalanced_wheel/
```

Then run the second pass of the ingestion workflow over that staging directory.

---

*This file was updated on 2026-07-20 by Codex GPT-5*
