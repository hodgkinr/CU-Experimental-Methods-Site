# Instrumentation Summary — Bouncing Ball: Coefficient of Restitution

**Lab:** Bouncing Ball — Coefficient of Restitution  
**Source:** ASEN 2003 Lab 2, CU Boulder (2014 and 2018/2019 versions)  
**Compilation bin:** instrumentation/

---

## Electronic Instrumentation

[NOT APPLICABLE: This lab uses manual measurement tools and/or video tracking software. No
electronic sensors, DAQ hardware, signal conditioning, or sampling rate considerations are
involved. The "sensors" in this lab are physical measurement tools (ruler, stopwatch, camera)
selected by the student as part of the experimental design task.]

---

## Measurement Tools Described in Source

| Tool | Version | Notes |
|------|---------|-------|
| Ruler / meter stick | Both (implied) | For height measurement; not specified — students select their own |
| Stopwatch / timer | Both (implied) | For time measurement; not specified — students select their own |
| Cell phone camera | 2018/2019 .tex | Used for 3 video-tracked trials; any modern smartphone |
| ITLL camera | 2018/2019 .tex | Alternative to phone camera; ITLL-provided |
| Tracker software | 2018/2019 .tex (Appendix A) | Free image tracking; Physlets; requires Java 1.6+ |
| Logger Pro | 2018/2019 .tex (Appendix A) | ITLL computers only; not for personal installation |
| Automatic tracking system | 2014 .md only | Lab-demonstrated; details not specified in source |

---

## Tool Detail: Tracker Software

- **Type:** Image tracking / video analysis software
- **Manufacturer / source:** Physlets (open source)
- **Download:** https://physlets.org/tracker/
- **System requirement:** Java 1.6 or higher
- **Cost:** Free
- **Tutorial:** `Bouncing_Ball_Tracker_Tutorial.pdf`
  [RECOVERED IN MANUAL STAGING: available in `manual_source_staging/bouncing_ball/tutorials/`
  and confirmed from the second-pass source review.]
- **Capability:** Frame-by-frame tracking of ball position; exports position vs. time data
- **Resolution:** Determined by camera frame rate and pixel resolution of recording

## Tool Detail: Logger Pro

- **Type:** Video analysis and data logging software
- **Manufacturer:** Vernier
- **Availability:** ITLL lab computers only — NOT available for personal installation
- **Tutorial:** `Bouncing_Ball_Logger_Pro.PDF`
  [MISSING: Referenced in source as a Canvas download; not recovered in the staged materials.]
- **Capability:** Similar to Tracker; performs image tracking on video recordings

## Tool Detail: Automatic Tracking System (2014 version only)

- **Type:** Unknown — referenced as "the automatic tracking system demonstrated in lab"
- **Source:** 2014 version of lab assignment
- **Details:** Not specified in source. The 2018/2019 version replaces this with student-
  owned phone camera + Tracker or Logger Pro. The 2018/2019 approach is recommended for
  3501 use as it is more accessible and self-contained.
  [MISSING: Details of the 2014 automatic tracking system — make, model, operation,
  and uncertainty characteristics are unspecified in source documents.]

---

## What Is Explicitly Missing

The following specification information is absent from the source and is a student design
decision in the original lab:

- [MISSING: Ruler/meter stick specifications — length, graduation resolution, and uncertainty
  (students choose their own ruler; uncertainty is part of their error analysis)]
- [MISSING: Stopwatch/timer specifications — resolution and uncertainty (students choose their
  own stopwatch; reaction time error is the dominant source, not device resolution)]
- [MISSING: Ball specifications — ping-pong ball mass and diameter are not given; students
  measure these as part of the pre-lab preparation]
- [MISSING: Cell phone camera specifications — frame rate and resolution affect time resolution
  for video tracking; students should record their camera model and settings]
- [MISSING: Logger Pro tutorial PDF (`Bouncing_Ball_Logger_Pro.PDF`) referenced as a Canvas
  download in source]

---

## Predictive Model Value — Source and Interpretation

The typical CoR range for a regulation ping-pong ball on a hard floor is **0.85–0.90**
(dimensionless). This value reflects an experimentally established material property for
standard impact conditions — it is not derivable from the method equations above and cannot
be predicted from first principles using the constant-e model alone.

For Phase 1 students: use this range as your predictive model anchor in Section 7. Treat
e_predicted = 0.875 +/- 0.025 (midpoint and half-range) and cite this file as the source.

For Phase 2 students: your Phase 2 experiment packet will include this same range. It is
an appropriate basis for your predicted system response — but note the distinction: this is
a material reference property, not a calibrated instrument output. State explicitly that
your predicted e is based on published material behavior for this ball and surface type,
and that the actual value may vary with temperature, ball age, and surface compliance.

---

## Uncertainty Considerations by Measurement Tool

Since measurement tool selection is a student design task, the uncertainty characteristics
are also student-determined. The following are known from the source and general measurement
principles:

| Measurement | Primary error source | Notes |
|-------------|---------------------|-------|
| Height (ruler, manual) | Ruler resolution + parallax + judgment of peak | Dominant error for Method 1 |
| Time (stopwatch, manual) | Human reaction time (~0.1–0.3 s) | Dominant error for Methods 2 and 3 |
| Time (video, 30 fps) | Frame rate -> +/-1/30 s per event | Significantly reduces reaction time error |
| Height (video tracking) | Pixel resolution + scale calibration | Depends on camera distance and reference scale |

---

*This file was updated on July 20, 2026 by Codex GPT-5*
