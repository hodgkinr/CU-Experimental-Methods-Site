# MATLAB — Unbalanced Wheel Lab

No instructor-provided `.m` files were staged in this pass, but the staged
historical solution report gives a clearer picture of the expected workflow and
historical function structure.

---

## Required Functions (Student-Written Or Instructor-Adapted)

The staged source lineage supports three core MATLAB responsibilities:

### 1. `computeModel.m` (or equivalent)

**Purpose:** Compute model angular velocity ω for a given array of θ values.

**Specification:**

- Inputs: θ array [rad], model selector, friction moment Q [N·m] where needed
- Output: ω array [rad/s]
- Implements the balanced and unbalanced model forms
- Physical parameters defined as named variables inside the code
- Used to generate ω vs. θ comparison curves

The staged historical solution used separate functions for balanced and
unbalanced cases rather than one master function. Either structure is acceptable
if the code is clear and well documented.

### 2. `loadWheelData.m` (or equivalent)

**Purpose:** Load one experimental file and extract θ and ω.

**Historically confirmed pattern from staged solution report:**

```matlab
data = load(filename);
th_exp = data(:,2);
w_exp  = data(:,3);
```

**Expected behavior:**

- load a text-exported data file
- extract θ and ω
- trim data to `0.5 < θ < 15`
- return cleaned arrays for plotting and residual analysis

### 3. `computeResiduals.m` (or equivalent)

**Purpose:** Compute residual statistics and support histogram plotting.

**Expected outputs:**

- mean residual
- standard deviation
- uncertainty of the mean
- observation count
- count of residuals above `3σ`

The staged 2019 handout explicitly asks for these statistics, and the staged
historical solution report confirms histogram-based residual inspection.

---

## Historically Confirmed Analysis Pattern

From the staged historical solution report:

- files were loaded with MATLAB `load(...)`
- column 2 was theta
- column 3 was omega
- trimming was done by removing data below `0.5 rad` and above `15 rad`
- residuals were computed as `Observed - Predicted`
- normalized residual histograms were used

This is strong guidance for the student-facing analysis workflow, even though the
raw export files themselves still have not been staged.

---

## Suggested Student Analysis Order

1. Load one trial file
2. Extract and trim θ and ω
3. Plot ω vs. θ
4. Compute model predictions at the measured θ values
5. Compute residuals as `Observed - Predicted`
6. Compute summary statistics
7. Plot residual histograms

---

## Still Missing

- `[MISSING: current raw export files to confirm that the historical load(filename) workflow still matches the present apparatus export format]`
- `[MISSING: any instructor-intended starter code or official analysis skeleton, if such files exist]`

---

*This file was updated on July 20, 2026 by Codex GPT-5*
