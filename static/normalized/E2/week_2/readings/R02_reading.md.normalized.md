# DAQ Configuration Choices & Practical Setup — A Decision Reference
## Every configuration choice is a claim about your signal. Treat it that way.

A data acquisition system handed to you with factory defaults is not a neutral tool. It is a collection of someone else's assumptions about what you are measuring.

**Quick-Reference: DAQ Configuration Decisions**

| Choice | Key Question | Decision Rule |
|---|---|---|
| Channel configuration | Is the signal source floating or subject to ground loop noise? | Default differential; use single-ended only for large signals with shared ground and short cables |
| Input range | What is the expected signal amplitude? | Set to the smallest range that comfortably brackets the signal; do not accept ±10 V defaults for millivolt signals |
| Sample rate | What is the signal bandwidth, and what anti-aliasing margin is required? | Sample at 5× to 10× the signal bandwidth; document the Nyquist argument explicitly |
| Anti-aliasing filter cutoff | What is the transition band of the filter relative to the chosen sample rate? | Set cutoff at ≤ 0.4 × sample rate; document relationship to signal bandwidth |
| Triggering | Does the event onset need to be captured, or is the signal slowly varying? | Hardware trigger for transient events; software trigger acceptable for quasi-static signals |

Understanding those assumptions (channel configuration, resolution, sample rate, triggering) is not optional bookkeeping. Each choice encodes a constraint on what the system can faithfully represent, and each constraint contributes its own error source to your measurement. This reading is a reference document. Use it when setting up your Tier 2 experiment and again when drafting the DAQ configuration justification section of the Tier 2 group report. Unlike the companion reading (R1), which builds physical intuition for aliasing and sampling, this reading is deliberately dense: it is meant to be consulted, not just read once.

---

## Channel Configuration: Single-Ended vs. Differential

Most DAQ systems offer two channel configuration modes, and the difference matters whenever noise or ground potential is a concern.

**Single-ended configuration** measures voltage between the signal line and a shared system ground. It uses twice as many channels for a given number of signals compared to differential, which makes it attractive when channel count is a constraint. The vulnerability: any noise voltage that appears between the sensor's ground reference and the DAQ system's ground reference is measured as signal. In environments with multiple power supplies, motors, or long cable runs, this ground-referencing error, called a **ground loop**, can swamp a low-level sensor signal.

**Differential configuration** measures voltage between two dedicated signal lines, rejecting any voltage that appears equally on both (called **common-mode rejection**). Differential inputs are the right choice whenever your signal source is floating, or whenever the signal amplitude is small enough that ground loop noise is a significant fraction of the signal magnitude. A **floating signal source** has no connection to the local measurement ground: battery-powered sensors and isolated transducers are common examples, and their reference point may drift relative to the DAQ ground. Most precision measurement applications — strain gauges, thermocouples, load cells — use differential configuration for this reason.

The practical decision: single-ended is acceptable when the signal is large (volts, not millivolts), cable runs are short, and all equipment shares a common ground. In any other case, default to differential.

---

## Resolution: Quantization Error and Its Contribution to Uncertainty

Every analog-to-digital converter (**ADC**) maps a continuous voltage range onto a finite number of discrete digital levels. A 12-bit ADC divides its input range into 2¹² = 4,096 discrete levels. A 16-bit ADC divides the same range into 65,536 levels. The voltage difference between adjacent levels is the **quantization step size** — also called the **least significant bit (LSB)** voltage.

For a ±10 V input range on a 12-bit ADC, the quantization step size is 20 V / 4,096 ≈ 4.9 mV. That is the smallest voltage change the system can detect. Any signal change smaller than one LSB is invisible — it either rounds up to the next level or rounds down. The resulting error is **quantization error**, and it contributes to the total measurement uncertainty.

For most well-designed experiments, quantization error is dominated by other error sources (sensor noise, thermal drift, amplifier noise). But there are important exceptions. If you are measuring a slowly varying, low-amplitude signal (structural creep, thermal expansion, very low-level acoustic vibration) and your input range is set far wider than the signal amplitude, the effective resolution shrinks dramatically. A signal that occupies only 1% of the ADC input range is being measured with roughly 100 times worse effective resolution than the ADC spec implies.

The practical decision: set the input range to the smallest value that comfortably brackets your expected signal. Do not accept ±10 V defaults when your signal is ±100 mV.

![A diagram illustrating quantization for two different ADC input range settings. On the left, a ±10V input range is divided into discrete levels, with a small signal occupying only the bottom fraction of the range — the signal is shown as a small-amplitude sine wave that spans only a few quantization levels. On the right, the input range is set to ±200 mV to match the signal amplitude, and the same signal now spans many quantization levels. Both panels show the step-staircase digitized output overlaid on the smooth true signal. A caption reads: "Resolution is a function of both the ADC bit depth and the ratio of signal amplitude to input range." Engineering diagram style, clean black and white with annotation labels.](../images/E2_W7_R2_image1.png)
*This image shows that DAQ resolution is not only a datasheet number; your range choice directly decides how much of that resolution the signal actually gets to use.

---

## Sample Rate: Nyquist Argument Plus Engineering Margin

The Nyquist-Shannon sampling theorem (covered in R1) establishes a lower bound: sample at least twice the highest frequency in your signal. In practice, that lower bound is a starting point, not a design target.

A signal sampled at exactly twice its highest frequency requires a perfect, infinitely sharp anti-aliasing filter — which does not exist in hardware. Real anti-aliasing filters have a transition band: a frequency range over which the attenuation rolls off gradually from passband to stopband. To accommodate this transition band, the practical rule is to sample at a rate **5× to 10× the signal bandwidth**, not 2×. This margin relaxes the filter requirements and provides buffer against uncertainty in the exact upper frequency of the signal.

When documenting your sample rate choice in the Tier 2 report, the required argument is: (1) the estimated signal bandwidth (from physical reasoning, not from the data), (2) the anti-aliasing filter cutoff frequency, (3) the chosen sampling rate and the margin it provides over the Nyquist minimum, and (4) any known limitations if the margin is tight.

---

## Triggering and Synchronization

Many aerospace experiments involve transient events — a structure loaded to failure, a motor spun up to operating speed, a thermal cycle initiated. In these cases, data collection must be synchronized to the event.

**Software triggering** starts acquisition when a command is issued. The delay between the command and the first sample is on the order of milliseconds — acceptable for slow-varying signals, problematic for transient events. **Hardware triggering** starts acquisition when an analog voltage crosses a threshold or a digital line goes high, with sub-microsecond response. For any experiment where the timing of data collection relative to the physical event matters, hardware triggering is required.

**Pre-trigger buffers** allow the DAQ system to capture data that occurred before the trigger event — the system records continuously, and the trigger selects the retention window. This is essential for capturing the onset of a transient before the threshold condition is detected.

For example: if you want to capture the onset of a structural impact, hardware triggering on a load cell threshold ensures data collection starts the moment the load exceeds a set value, not a few milliseconds later when the computer catches up. For slowly varying signals (thermal measurements, quasi-static loading), software triggering is usually sufficient.

---

## A Worked Example: The Bit-Rollover Artifact

This example requires knowing that some sensors count events as unsigned integers (always positive, values 0 to 65,535) while many DAQ systems record data as signed integers (positive and negative). When a sensor wraps from its maximum count back to zero, a signed integer recording sees a large negative jump.

Consider a counter-based displacement sensor that outputs a count value from 0 to 65,535 (a 16-bit unsigned integer) representing a full rotation. The sensor counts up as the shaft rotates in one direction. If the shaft reverses just past the 65,535 count, the next reading is 0 — a rollover. When that value is recorded by a DAQ system that stores the output as a signed 16-bit integer, the jump from 65,535 to 0 appears in the data as a sudden, large negative-going step.

In a time-series plot, this step looks like a real physical event — a rapid reversal, a discontinuity, an impulse. It is not. It is a sensor counter rollover recorded by a DAQ system that was not configured to handle unsigned output. Only knowledge of the sensor's output format and awareness of the DAQ configuration reveals the artifact for what it is. Uncertainty analysis cannot identify this type of artifact — it looks like a physical reading that is within sensor range. The defense is documentation: reading the DAQ configuration against the sensor datasheet before collecting data, not after.

![A time-series plot showing sensor output versus time. The signal generally trends upward smoothly, then abruptly drops from near-maximum to near-zero at one time instant, then continues rising. The drop is labeled "Apparent reversal event." A callout box notes: "Sensor counter rollover: 65535 → 0, recorded as negative step in signed integer format. Physical shaft motion was continuous." The x-axis is labeled "Time (s)" and the y-axis "Sensor output (counts)." The smooth expected trajectory (without the rollover) is shown as a dashed continuation curve through the drop. Clear engineering plot style with annotation.](../images/E2_W7_R2_image2.png)
*This image helps you see how a data-system artifact can masquerade as a physical event if you do not understand how the sensor and acquisition chain encode the signal.

---

## Documentation Requirement

Every DAQ configuration choice must be documented in your Tier 2 report with justification, not just a list of settings. The required entries for each choice:

| Choice | What to document |
|---|---|
| Channel configuration | Single-ended or differential; reason |
| Input range | Value; why this range was chosen for the signal amplitude |
| Sample rate | Value; Nyquist argument; margin above minimum |
| Anti-aliasing filter cutoff | Value; relationship to signal bandwidth and sample rate |
| Triggering | Type; reason; pre-trigger buffer if applicable |
| Resolution | ADC bit depth; quantization step size; assessment of whether it limits the measurement |

A DAQ configuration section that lists settings without justification does not demonstrate that the choices were made defensibly. The goal is to show that you understood what each setting controls and chose it on physical grounds.

---

**The Takeaway:** DAQ configuration is not a setup task to complete before the real work begins. It is part of the measurement design, and every undocumented default is an undocumented assumption about your signal that may or may not be valid for your experiment.
