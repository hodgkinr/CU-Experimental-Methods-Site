# Status Report — Tier 1 Ingestion Second Pass: Unbalanced Wheel

**Run date:** July 20, 2026
**Workflow:** `CLAUDE_CODE_TASK_TIER1_LAB_INGEST.md`
**Source directory:** `/Users/hodgkinr/Documents/GitHub/AES-Labs-Catalog/curriculum_2000_labs/Unbalanced_wheel`
**Manual staging root:** `/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Planning/detailed_design/baseline_design/agentic_course_creation/manual_source_staging/unbalanced_wheel`
**Run type:** Second pass with staged restricted materials

---

## Summary

The second pass materially improved the Unbalanced Wheel planning package.

New staged materials included:

- encoder datasheet PDF
- TA FAQ PDF
- 2019 handout bundle with `.tex` source
- setup images in the handout bundle
- historical sample solution report docx

The staged `.tex` and historical report were especially useful. They confirmed:

- the current 2 balanced + 2 unbalanced trial structure
- the NI USB-6008 / `Dev 2` requirement
- exact `UnbalancedWheel.vi` naming
- the 9V battery placement
- the historical data-column pattern: time, theta, omega
- the historical MATLAB loading/trimming workflow

The encoder PDF plus instructor confirmation identified the encoder as
`HEDS-5505`, but full
spec extraction is still incomplete. The staged FAQ PDF was not successfully
text-extracted in this pass, so it still needs manual review or a better local
extraction path if we want to fully absorb its contents.

**Current status:** `READY FOR DEPLOYMENT`

---

## What Improved In This Pass

### Data

- `data/data_notes_agent.md`
  - now documents the historically supported 3-column text layout
  - preserves the external SharePoint placeholder policy
  - distinguishes historical trial conventions from current trial expectations

### Instrumentation

- `instrumentation/sensor_specs_summary_agent.md`
  - now confirms the `UnbalancedWheel.vi` name, NI USB-6008 role, 9V battery,
    and `Dev 2` setup requirement from the staged 2019 handout
  - now records the encoder model as `HEDS-5505`

### MATLAB

- `matlab/README_agent.md`
  - now reflects historically confirmed function patterns and file loading logic

### Workflow State

- missing-file requests were narrowed to what remains genuinely unresolved

---

## Remaining Gaps

### Still useful but not blockers

- current raw export files, if the team later wants to document the present-day
  export format with higher confidence
- full numerical encoder specifications from the staged encoder PDF
- TA FAQ content extracted into text
- any official starter MATLAB code if the teaching team wants students to receive it

---

## Publish Readiness Assessment

### Good enough now for deployment

- procedure
- theory/model structure
- instrumentation overview
- data policy
- MATLAB workflow outline

### Remaining refinement opportunities

- validate the raw export format against actual current files
- optionally extract the FAQ PDF into usable notes

---

## Recommended Next Step

1. If possible in the future, add either:
   - a text-extracted version of the FAQ PDF, or
   - a short human summary of the important FAQ points

The Unbalanced Wheel package is now in good enough shape to deploy through
`./scripts/deploy_planning_to_site.sh`.

---

*This file was updated on July 20, 2026 by Codex GPT-5*
