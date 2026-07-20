# Status Report — Tier 1 Ingestion First Pass: Bouncing Ball

**Run date:** July 20, 2026
**Workflow:** `CLAUDE_CODE_TASK_TIER1_LAB_INGEST.md`
**Source directory:** `/Users/hodgkinr/Documents/GitHub/AES-Labs-Catalog/curriculum_2000_labs/Bouncing_ball`
**Primary catalog file:** `Bouncing_ball_Lab_Catalog.md`
**Companion file:** `bouncing_ball_master_checklist.md`
**Run type:** First pass from Labs Catalog

---

## Summary

The existing Bouncing Ball planning compilation is already fairly complete and
substantially richer than the `bouncing_ball_master_checklist.md` companion file.
The catalog markdown remains a strong upstream source because it includes:

- the three restitution methods
- video-tracking workflow
- expected datasets and trial counts
- software/tool references
- common mistakes and troubleshooting guidance

This first-pass ingestion therefore focuses on:

1. reaffirming the catalog as the upstream source of truth
2. preserving the strong existing student-facing structure
3. adding a formal missing-files handoff for manual recovery
4. updating the data section so public data delivery happens through an external
   SharePoint link rather than bundled raw files

**Current status:** `READY FOR LIMITED REVIEW ONLY`

---

## What Was Confirmed From Catalog Sources

The catalog and available planning materials support the following as stable:

- three-method coefficient-of-restitution workflow
- phone-camera / Tracker / Logger Pro video analysis option
- 10-trial preliminary structure per method
- refined best-method follow-up and second-ball comparison
- major student pitfalls around spin, reaction time, and scale calibration
- expected MATLAB/statistical workflow at a high level

---

## First-Pass Changes Made In This Run

### Updated

- `data/data_notes_agent.md`
  - added course-site data policy
  - added placeholder student-facing SharePoint link:
    `Data - Link to Sharepoint - NEEDS UPDATE`
  - clarified that public data access should be external, not bundled

### Added

- `MISSING_FILES_REQUEST_agent.md`
  - explicit handoff document for manual source recovery

### Refreshed

- `STATUS_REPORT_agent.md`
  - rewritten to reflect the catalog-first ingestion workflow

---

## Remaining Gaps After First Pass

### High Priority

- Tracker tutorial PDF
- Logger Pro tutorial PDF
- setup/diagram image showing the variable definitions
- final student-facing SharePoint data destination

### Medium Priority

- richer current handout bundle or LaTeX zip if not already represented fully
- curated sample videos or a recommended public subset
- any starter MATLAB GUI or supporting code the team wants treated as instructor reference

### Optional

- additional instructor notes or archived worked examples

---

## Publish Readiness Assessment

### Ready now

- procedure page for review
- theory/model pages for review
- instrumentation overview for review
- notes page for review

### Not ideal yet

- public data-link destination not finalized
- tutorial attachments not yet staged
- setup diagram still missing

---

## Required Next Step

Use `MISSING_FILES_REQUEST_agent.md` to collect manual source materials into:

```text
/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Planning/detailed_design/baseline_design/agentic_course_creation/manual_source_staging/bouncing_ball/
```

Then run the second pass of the ingestion workflow over that staging directory.

---

*This file was updated on July 20, 2026 by Codex GPT-5*
