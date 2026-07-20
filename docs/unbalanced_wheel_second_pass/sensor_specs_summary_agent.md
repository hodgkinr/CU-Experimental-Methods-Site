# Sensor and Instrumentation Summary — Unbalanced Wheel: Inertia Distribution and Rolling Dynamics

---

## Primary Sensor — Wheel Encoder

| Property | Value | Source |
|----------|-------|--------|
| Sensor model | `HEDS-5505` | instructor-provided confirmation + staged encoder PDF lineage |
| Measurement role | Rotation angle θ [rad]; angular velocity ω derived numerically | catalog + staged handout lineage |
| Mounting | On the wheel; rotates with the wheel | catalog + staged handout lineage |
| Communication | Wireless transmission to receiver on lab computer | catalog + staged handout lineage |
| Power supply | 9V battery in wheel along training wheel bar | staged 2019 `.tex` |
| Reliable analysis range | 0.5 rad < θ < 15 rad | staged handout + historical code |
| Counts per revolution | `[MISSING: confirm from datasheet extraction]` | staged encoder PDF not fully text-extracted |
| Output type | `[MISSING: confirm from datasheet extraction]` | staged encoder PDF not fully text-extracted |
| Voltage range | `[MISSING: confirm from datasheet extraction]` | staged encoder PDF not fully text-extracted |
| Accuracy / resolution | `[MISSING: confirm from datasheet extraction]` | staged encoder PDF not fully text-extracted |

The staged encoder PDF plus instructor confirmation identify the encoder as
`HEDS-5505`, but a clean text extraction or manual review is still needed to
fill in the actual spec values.

**Known issue:** Wireless line-of-sight matters. Packet drops can produce large
gaps, plateaus, or spikes in the recorded data.

---

## DAQ Hardware — NI USB-6008

| Property | Value | Source |
|----------|-------|--------|
| Manufacturer | National Instruments | staged handout lineage |
| Model | USB-6008 | staged handout lineage |
| Interface | USB to computer | staged 2019 `.tex` |
| Electronics box | Included with apparatus | staged 2019 `.tex` |
| Required device ID | Must appear as `Dev 2` in NIMax | staged 2019 `.tex` |
| Analog input channels | `[MISSING: confirm from NI datasheet]` | external spec not yet staged |
| Resolution | `[MISSING: confirm from NI datasheet]` | external spec not yet staged |
| Sampling rate | `[MISSING: confirm from NI datasheet]` | external spec not yet staged |
| Quantization uncertainty | `[MISSING: confirm from NI datasheet]` | external spec not yet staged |

**Configuration note:** The NI USB-6008 must be listed as `Dev 2` in NIMax for
the LabVIEW VI to communicate correctly with it.

---

## DAQ Software — LabVIEW VI

| Property | Value | Source |
|----------|-------|--------|
| Application name | `UnbalancedWheel.vi` | staged 2019 `.tex` |
| Location | Shortcut in ASEN 2003 folder on lab computer | staged 2019 `.tex` |
| Output channels | θ and ω vs. time | catalog + staged handout lineage |
| Recording trigger | Data is not recorded until the wheel begins to move | staged 2019 `.tex` |
| Stop condition | Stop the VI once the wheel reaches the bottom of the ramp | staged 2019 `.tex` |
| Reference video | `https://www.youtube.com/watch?v=28rrILZLlqM&t=0s` | staged 2019 `.tex` |

---

## Full DAQ Chain Summary

```text
Wheel rotation
    → wheel encoder (HEDS-5505)
    → wireless transmission to receiver on lab computer
    → NI USB-6008 + electronics box
    → USB connection to computer
    → UnbalancedWheel.vi (LabVIEW)
    → exported text data file (historically time, theta, omega)
```

Students are end-users of the DAQ chain. They operate the apparatus and VI but
do not program the NI device or the LabVIEW VI.

---

## Second-Pass Improvements From Staged Files

The staged handout confirms:

- NI USB-6008 usage
- `Dev 2` requirement in NIMax
- 9V battery location
- operational dependency on wireless line-of-sight
- exact `UnbalancedWheel.vi` naming

The staged encoder materials confirm the model:

- `HEDS-5505`

but further manual extraction is still needed for numerical specifications.

---

## Remaining Gaps

- `[MISSING: encoder counts/rev, output type, voltage range, and stated accuracy from the encoder PDF]`
- `[MISSING: NI USB-6008 datasheet or extracted spec values]`

---

*This file was updated on July 20, 2026 by Codex GPT-5*
