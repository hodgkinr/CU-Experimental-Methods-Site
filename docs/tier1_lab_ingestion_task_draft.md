# Claude Code Task — Tier 1 Lab Ingestion From Labs Catalog

> **STATUS: DRAFT**
> This task is intended to replace per-lab first-pass compile prompts with a
> single reusable workflow that starts from `AES-Labs-Catalog`, produces the
> canonical Tier 1 lab compilation package in `CU-Experimental-Methods-Planning`,
> and then relies on the existing deployment flow to push the content through
> `BOBPE-fwd_rev` and into `CU-Experimental-Methods-Site`.

---

## Purpose

This task ingests one Tier 1 candidate lab from `AES-Labs-Catalog` and turns it
into the structured student-facing compilation package expected by the ASEN 3501
site generator.

The workflow is intentionally split into **two agent passes**:

1. **First pass:** Use the lab catalog markdown and any locally readable source
   files already present in the catalog directory to build the best possible
   canonical package in `-Planning`.
2. **Manual source recovery:** Emit a precise list of missing files that the
   instructional team must pull manually from restricted locations.
3. **Second pass:** Re-read the manual staging directory and enrich the canonical
   package using the newly provided materials.

The task does **not** publish directly to the course site. After the canonical
package is updated in `-Planning`, use:

```bash
./scripts/deploy_planning_to_site.sh
```

from the Planning repo root to push the content downstream.

---

## Repos and Roles

```
AES-Labs-Catalog                ← upstream lab source, links, local source folders
CU-Experimental-Methods-Planning ← canonical staged content for course delivery
BOBPE-fwd_rev                   ← Forward bundle + generator
CU-Experimental-Methods-Site    ← generated site output only
```

**Authoritative write target for this task:**

```
CU-Experimental-Methods-Planning/
  detailed_design/baseline_design/agentic_course_creation/claude_V1/
    assignments/lab_compilations/tier1_lab_[LAB_KEY]/
```

**Manual file staging directory:**

```
CU-Experimental-Methods-Planning/
  detailed_design/baseline_design/agentic_course_creation/manual_source_staging/[LAB_KEY]/
```

---

## Inputs

The task takes these inputs:

```text
LAB_KEY                 machine name, e.g. unbalanced_wheel
LAB_DISPLAY_NAME        human name, e.g. Unbalanced Wheel
CATALOG_DIR             path to the lab folder in AES-Labs-Catalog
CATALOG_MD              main Lab Catalog markdown file
PLANNING_OUTPUT_DIR     canonical Tier 1 compilation output folder
MANUAL_STAGING_DIR      folder for manually recovered restricted files
TIER_KEY                tier1
```

Example:

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

## Output Structure

The task must create or update this exact structure:

```text
tier1_lab_[LAB_KEY]/
  procedure/
    procedure_agent.md
    setup_photos/
  model/
    derivation_agent.md
    model_equations_agent.md
  instrumentation/
    sensor_specs_summary_agent.md
    datasheets/
      README_agent.md
  data/
    data_notes_agent.md
  matlab/
    README_agent.md
  notes/
    additional_notes_agent.md
  STATUS_REPORT_agent.md
  MISSING_FILES_REQUEST_agent.md
```

`MISSING_FILES_REQUEST_agent.md` is new and is the handoff artifact for manual
file recovery between first pass and second pass.

---

## Core Rule

The task should treat the `AES-Labs-Catalog` lab folder as the **starting point**
but should not assume the lab catalog markdown alone is enough for student-facing
delivery.

The agent must:

- use the catalog markdown as the organizing spine
- read any locally accessible supporting files in the lab folder
- preserve useful file links and references
- identify what content is still missing for a robust Tier 1 student experience
- request those missing source files explicitly

---

## Phase A — First Pass From Labs Catalog

### Step A1 — Read available source materials

Read:

- the main `*_Lab_Catalog.md`
- any companion checklists or plain-text notes in the same lab folder
- any readable `.md`, `.txt`, `.json`, `.tex`, `.csv` files in the lab folder
- any existing planning-side compilation package, if present, for diff/reference

Do not attempt to invent content from unreadable binaries.

### Step A2 — Build content inventory

Create an internal inventory with these buckets:

- procedure / execution
- theory / models
- instrumentation / DAQ
- data format / sample data
- MATLAB / analysis expectations
- instructor notes / pitfalls
- source links / restricted files / attachments

### Step A3 — Populate canonical planning package

Write or update the compilation files using only content supported by the
catalog and locally readable source materials.

### Step A4 — Mark uncertainty honestly

Use inline tags where needed:

- `[MISSING: ...]`
- `[MISSING_DATA: ...]`
- `[SETUP_PHOTO NEEDED: ...]`
- `[NEEDS INSTRUCTOR REVIEW]`
- `[INSTRUCTOR TO PROVIDE: ...]`
- `[STUDENT TASK — ...]`

### Step A5 — Emit missing-files handoff

Create `MISSING_FILES_REQUEST_agent.md` listing exactly which external files are
needed to improve the package. Group them by priority:

- `HIGH PRIORITY`
- `MEDIUM PRIORITY`
- `OPTIONAL`

For each missing file include:

- display name
- likely purpose
- where it should be placed in `MANUAL_STAGING_DIR`
- what planning files it is expected to enrich

### Step A6 — Update status report

`STATUS_REPORT_agent.md` must state:

- what was derived from catalog-only sources
- what remains missing after first pass
- whether the package is sufficient for provisional publication or still too thin

---

## Phase B — Manual Recovery Step

This is the human handoff point.

The instructional team manually copies restricted or external materials into:

```text
manual_source_staging/[LAB_KEY]/
```

Recommended subfolders:

```text
manual_source_staging/[LAB_KEY]/
  datasheets/
  handouts/
  faqs/
  sample_data/
  setup_media/
  analysis_code/
  notes/
```

The agent does nothing in this phase except wait for the files to appear.

---

## Phase C — Second Pass Over Manual Staging

### Step C1 — Scan staging directory

Read all readable staged files. Inventory binaries even when text extraction is
not possible.

### Step C2 — Enrich canonical package

Use the staged files to:

- fill instrumentation gaps
- improve procedures
- confirm data formats
- copy or reference sample files where appropriate
- refine notes and troubleshooting sections
- reduce prior `[MISSING]` markers

### Step C3 — Preserve provenance

When the second pass changes a section materially, note the added source in:

- `STATUS_REPORT_agent.md`
- `MISSING_FILES_REQUEST_agent.md` as resolved

### Step C4 — Reassess publish readiness

At the end of second pass, the status report must clearly say one of:

- `READY FOR DEPLOYMENT`
- `READY FOR LIMITED REVIEW ONLY`
- `BLOCKED — MORE SOURCE RECOVERY NEEDED`

---

## Canonical Writing Targets

### `procedure/procedure_agent.md`

Reader: student or lab assistant.

Must include:

- experiment overview
- pre-lab requirements
- apparatus / setup
- data collection sequence
- safety and failure modes
- known pitfalls

### `model/derivation_agent.md`

Reader: student doing theory work.

Must include:

- physical setup
- assumptions
- derivation framing
- model hierarchy
- residual-analysis logic where relevant

### `model/model_equations_agent.md`

Reader: student needing quick reference.

Must include:

- equations only
- symbols and units
- clean organization

### `instrumentation/sensor_specs_summary_agent.md`

Reader: student configuring or understanding the measurement chain.

Must include:

- sensor names
- measurement role
- DAQ chain
- known specs / missing specs

### `data/data_notes_agent.md`

Reader: student preparing to analyze results.

Must include:

- file format expectations
- columns / units
- trimming guidance
- known quirks
- sample data availability status

### `matlab/README_agent.md`

Reader: student coding analysis.

Must include:

- required functions or scripts
- expected plots
- analysis order
- provided code vs. student-written code

### `notes/additional_notes_agent.md`

Reader: instructor or advanced reviewer.

Must include:

- adaptation notes for 3501
- discussion prompts
- unresolved issues
- original lab provenance

---

## Downstream Deployment

Once the canonical planning package is satisfactory, use:

```bash
cd /Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Planning
./scripts/deploy_planning_to_site.sh
```

That downstream flow already performs:

1. `-Planning` → Forward bundle sync
2. bundle → `static/`
3. bundle → `server/course_content/`

This task should **not** patch generated site HTML directly except for debugging.

---

## Success Criteria

The task succeeds when:

1. The canonical Tier 1 lab package exists in `-Planning`
2. All available catalog-derived content has been organized into the expected bins
3. Missing external files are requested in a precise, actionable handoff doc
4. A second pass can enrich the package using a known staging directory
5. The package is in the exact shape expected by `sync_bundle.py` and the site generator

---

## Non-Goals

- Fetching protected SharePoint content automatically
- Editing final site HTML as the source of truth
- Maintaining a different generic task file for every lab
- Requiring the catalog markdown alone to contain every needed student-facing detail
