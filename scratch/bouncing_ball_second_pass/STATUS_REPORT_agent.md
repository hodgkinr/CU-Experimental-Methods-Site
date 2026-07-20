# Status Report — Tier 1 Ingestion Second Pass: Bouncing Ball

**Run date:** July 20, 2026
**Workflow:** `CLAUDE_CODE_TASK_TIER1_LAB_INGEST.md`
**Source directory:** `/Users/hodgkinr/Documents/GitHub/AES-Labs-Catalog/curriculum_2000_labs/Bouncing_ball`
**Primary catalog file:** `Bouncing_ball_Lab_Catalog.md`
**Companion file:** `bouncing_ball_master_checklist.md`
**Manual staging root:** `/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Planning/detailed_design/baseline_design/agentic_course_creation/manual_source_staging/bouncing_ball/`
**Run type:** Second pass with manually staged source files

---

## Summary

The second pass recovered enough source material to make the Bouncing Ball
planning compilation substantially more complete for Tier 1 student-facing use.
The staged materials confirmed or supplied:

- the 2018 handout PDF
- the LaTeX source for the 2018 handout
- the variable-definition figure image referenced by the handout
- the Tracker tutorial PDF
- the final external SharePoint data destination for student data access

This pass updates the planning package so the public-facing lab content can rely
on an external data link instead of bundled raw data while narrowing the missing
materials list to the small number of gaps that actually remain.

**Current status:** `READY FOR PLANNING REVIEW AND DEPLOYMENT CHECK`

---

## Recovered In Manual Staging

### Confirmed files

- `handouts/ASEN2003_Lab2_Intro_2018.pdf`
- `setup_media/ASEN2003_Lab2_Bouncing_Ball_LaTeX/ASEN2003_Lab2_Bouncing_Ball.tex`
- `setup_media/ASEN2003_Lab2_Bouncing_Ball_LaTeX/img/bouncing_ball.PNG`
- `tutorials/Bouncing_Ball_Tracker_Tutorial.pdf`

### Confirmed manually provided URL

- student-facing SharePoint data destination for Bouncing Ball sample data

---

## Second-Pass Changes Made In This Run

### Updated

- `data/data_notes_agent.md`
  - replaced placeholder data URL with the provided SharePoint link
  - preserved the required public policy of linking externally rather than
    bundling raw data into the course site
  - added a note that historical internal CSV files still exist in the planning
    compilation and should be reviewed separately if the team wants a stricter
    no-bundled-data policy

- `instrumentation/sensor_specs_summary_agent.md`
  - marked the Tracker tutorial as recovered from manual staging
  - kept Logger Pro tutorial as the remaining missing tutorial artifact

- `instrumentation/datasheets/README_agent.md`
  - marked the Tracker tutorial as recovered
  - narrowed the missing software-resource list to Logger Pro only

- `MISSING_FILES_REQUEST_agent.md`
  - reduced the handoff to the true remaining gaps after staged-file review

- `STATUS_REPORT_agent.md`
  - rewritten to reflect second-pass completion state

---

## Remaining Gaps After Second Pass

### Still missing

- Logger Pro tutorial PDF referenced in the historical handout appendix

### Worth a later decision

- whether to keep or remove historical internal CSV files from the canonical
  Bouncing Ball planning compilation, since the downstream sync still copies
  those files into the Forward bundle even though they are not currently linked
  from the generated public lab page

### Optional

- a curated public sample video set, if the teaching team wants students to have
  example footage through SharePoint

---

## Notes On The Recovered Figure

The variable-definition figure was recovered in the staged LaTeX source as
`img/bouncing_ball.PNG`. That is enough to confirm the historical source and to
support future packaging work, but the current lab-compilation sync path does
not automatically publish nested setup assets from the staging directory.

For this pass, the figure is treated as recovered source context rather than a
guaranteed published site asset.

---

## Publish Readiness Assessment

### Ready now

- student-facing data link policy
- procedure and model review
- instrumentation summary review
- planning-side documentation review

### Needs awareness before deployment

- Logger Pro tutorial is still absent
- historical internal CSV files remain in the canonical package and may merit a
  cleanup decision later if the team wants a stricter planning-to-site data rule

---

*This file was updated on July 20, 2026 by Codex GPT-5*
