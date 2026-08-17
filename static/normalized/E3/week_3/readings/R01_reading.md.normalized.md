# Instrumentation and DAQ Design Worksheet
## A sensor choice is only credible when the whole measurement chain closes

The easiest way to fool yourself in experimental design is to choose a sensor before you know what the measurement must prove.

---

Use this worksheet before writing the Instrumentation Justification Report. The goal is not to fill every blank with impressive numbers. The goal is to make each instrumentation choice trace to intended use, expected signal behavior, uncertainty, and feasibility. If a value comes from a datasheet, standard, handbook, prior paper, or assumption, name the source.

<image description: A worksheet-style measurement chain running left to right: physical quantity, sensor, mounting, signal conditioning, filter, DAQ, data reduction, validation metric. Under each block is a blank field for specification, source, uncertainty contribution, and design risk. The visual communicates that instrumentation credibility comes from the complete chain, not one component.>

## Part 1 - Measurement Requirement

**Intended use** — What decision or model claim will this measurement support?

Response:

**Primary measurement quantity** — What physical quantity, trend, or response feature must be measured?

Response:

**Expected signal range** — What minimum and maximum values do you expect? What source or model supports this estimate?

Response:

**Required accuracy or resolution** — How small a difference must the experiment distinguish for the validation claim to matter?

Response:

**Expected bandwidth** — Is the response steady, slowly varying, transient, oscillatory, or noisy? Estimate the highest frequency content you need to preserve.

Response:

## Part 2 - Sensor And Installation

| Field | Baseline sensor | Beyond-provided alternative |
|---|---|---|
| Source consulted | | |
| Range | | |
| Accuracy / bias | | |
| Resolution / noise floor | | |
| Bandwidth / response time | | |
| Mounting or installation effects | | |
| Environmental risks | | |
| Calibration information | | |
| Cost / availability / feasibility | | |
| Effect on validation credibility | | |

**Decision** — Which option is adequate for the intended use, and why?

Response:

## Part 3 - DAQ And Signal Conditioning

**DAQ input range and resolution** — What voltage or digital range will be used? What is the quantization step size?

Response:

**Gain or conditioning** — Is amplification, bridge completion, excitation, shielding, grounding, or isolation required?

Response:

**Sampling rate** — What sample rate will you use, and how does it relate to expected signal bandwidth?

Response:

**Filtering or anti-aliasing** — What cutoff is needed before sampling? Explain the cutoff relative to signal bandwidth and sample rate.

Response:

**Dominant practical noise risk** — What noise, drift, cable, grounding, vibration, temperature, or installation effect worries you most?

Response:

## Part 4 - Compact Mini-Example

Suppose your proposed experiment measures vibration amplitude of a small cantilevered component. Your model predicts a dominant response near 18 Hz, and prior work suggests useful information up to about 40 Hz. You choose a sample rate of 200 Hz. The Nyquist limit is 100 Hz, which is above the 40 Hz signal content with margin. A reasonable anti-alias filter might pass the measurement band while attenuating content well above it; the exact cutoff depends on the filter roll-off, not an ideal brick wall.

Now check DAQ resolution. If the sensor output is expected to vary from -2 V to +2 V and the DAQ is set to a +/-10 V range, much of the ADC range is unused. A narrower input range, if available and safe from clipping, can reduce quantization uncertainty. But resolution is not total accuracy: sensor calibration, mounting, temperature drift, and signal conditioning may still dominate the uncertainty budget. The design decision is not "sample fast and use many bits." The design decision is whether the complete chain can distinguish the model-relevant difference.

<image description: A compact dynamic-response example with a frequency spectrum labeled useful signal 0 to 40 Hz, sample rate 200 Hz, Nyquist 100 Hz, and an anti-alias filter curve with roll-off. Beside it, a DAQ range graphic compares a +/-10 V range wasting resolution with a tighter range that captures a -2 V to +2 V signal without clipping.>

## Part 5 - Prospective Uncertainty Starter

List the uncertainty inputs that belong in your MATLAB model:

- Sensor accuracy or calibration uncertainty:
- DAQ quantization contribution:
- Repeatability estimate:
- Environmental or installation effect:
- Geometry, mass, voltage, timing, or other model input:
- Assumption that still needs verification:

**Adequacy statement** — Based on the current information, is the proposed measurement chain likely to evaluate the acceptance criterion? If not, what must change first?

Response:

---

**The Takeaway:** A complete instrumentation plan justifies the sensor, installation, conditioning, sampling, filtering, DAQ settings, and uncertainty together. Any blank link in the chain is a place where a polished experiment can stop producing trustworthy evidence.
