# Data Notes — Bouncing Ball: Coefficient of Restitution

---

## Data Access Policy For The Course Site

Raw and sample data files should **not** be bundled into the public course site
for this lab. Instead, the student-facing lab page should point to an external
data location managed manually by the instructional team.

**Student-facing data link for current publication pass:**

- [Data - Link to Sharepoint - NEEDS UPDATE](https://o365coloradoedu.sharepoint.com/:f:/r/sites/AEROENGR-Labspace-Labs/Shared%20Documents/Labs/Extra%20Historical%20Labs/Bouncing%20Ball%20Lab/SampleData?csf=1&web=1&e=7rNDKj)

---

## What Is Measured Per Method

### Method 1 — Height of Bounce

**Per trial:**

- initial drop height `h0`
- one or more bounce heights `h1, h2, ... hn`
- ball identity and ball characteristics

**Expected output:**

- one or more estimates of `e` from height ratios

### Method 2 — Time of Adjacent Bounces

**Per trial:**

- bounce durations `t1, t2, ... tn`
- optionally `h0` for context
- ball identity

**Expected output:**

- one or more estimates of `e` from adjacent bounce-time ratios

### Method 3 — Time to Stop

**Per trial:**

- initial drop height `h0`
- total time to stop `ts`
- ball identity

**Expected output:**

- one estimate of `e` per trial

### Video Tracking

**Per trial:**

- recorded video file
- extracted position/time data from Tracker, Logger Pro, or another approved workflow

**Expected output:**

- video-derived estimates of `e` using the same method logic

---

## Trial Structure From Source

| Dataset | Ball | Method | Min. Trials |
|---------|------|--------|-------------|
| Preliminary | Ping-pong | Method 1 | 10 |
| Preliminary | Ping-pong | Method 2 | 10 |
| Preliminary | Ping-pong | Method 3 | 10 |
| Video tracking | Ping-pong | All 3 from video | 3 |
| Refined | Ping-pong | Best method only | 10 |
| Second ball | Student-chosen | Best method | 10 |

**Total minimum trials:** 53

---

## Historical Internal Reference Files

The existing planning compilation already contains internal CSV examples such as:

- `method1_height_preliminary.csv`
- `method1_height_refined_and_secondball.csv`
- `method2_time_preliminary.csv`
- `method3_timetostop_preliminary.csv`
- `video_tracking_trials.csv`

These may be useful for internal review, but they should **not** be treated as
the public student-facing data delivery mechanism for the course site.

`[NEEDS INSTRUCTOR REVIEW: Historical internal CSV files remain in the canonical Bouncing Ball compilation. The current downstream sync copies them into the Forward bundle even though the generated public lab page does not currently link them. Decide later whether they should remain planning-side reference artifacts or be removed entirely.]`

---

## Recommended Student Data Structure

The historical source and current compilation support a simple structure:

- raw measurements stored by method
- reusable MATLAB function(s) to compute `e`
- reusable MATLAB function(s) to compute summary statistics

For student-facing guidance, the most important rule is to preserve raw measured
quantities rather than only storing computed `e` values.

---

## Ball Characteristics To Record

For each ball used, record:

- mass
- diameter
- material / surface type
- manufacturer / type if known
- condition / visible wear

---

## Known Measurement Considerations

- height measurements are vulnerable to parallax and peak-height judgment error
- time measurements by hand are dominated by human reaction time
- video methods reduce reaction-time error but depend on frame rate and scale calibration
- the definition of "stopped" in Method 3 introduces systematic bias unless stated clearly
- ball spin is a model limitation and should be minimized

---

## External Data Resources

- final student-facing data location has been provided through SharePoint
- if the teaching team later wants a public worked example, provide it through
  SharePoint rather than bundling raw files into the course-site build

---

*This file was updated on July 20, 2026 by Codex GPT-5*
