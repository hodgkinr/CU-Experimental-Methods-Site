slide 1: Title Slide
Title: Signal Conditioning & DAQ as Design Decisions — Reconnected to CLO 4
Talking Point: In E2 we treated sampling, filtering, and DAQ choices as things to analyze in a provided experiment. In E3 you have to specify those choices yourself. A sensor choice without a compatible signal conditioning and DAQ plan is not an instrumentation design yet.

slide 2: The Measurement Chain
(Image: A block diagram showing physical quantity, sensor/transducer, signal conditioning, anti-alias filter, DAQ, digital data, reduction equation, and validation metric. Each block has a small uncertainty tag.)
Talking Point: The measurement chain turns a physical response into a number used in a validation comparison. Every block can add uncertainty, bias, delay, distortion, or bandwidth limits. If you only justify the sensor, you have left most of the chain undesigned. E3 requires the full chain because credibility depends on the chain, not a single component.

slide 3: Sampling Rate from Signal Bandwidth
(Image: A frequency spectrum with a signal bandwidth marked from 0 to 40 Hz, a Nyquist limit at half the sampling rate, and a selected sampling rate with margin. A warning panel shows aliasing when the Nyquist limit is too low.)
Talking Point: Sampling rate should come from expected signal bandwidth, not from a default setting. Nyquist tells us the sampling rate must exceed twice the highest frequency we need to represent, but engineering practice usually needs margin. If your experiment involves dynamics, transients, or oscillations, your proposed sampling rate must be justified. "The DAQ can do it" is not the same as "the design requires it."

slide 4: Anti-Aliasing Is a Design Requirement
(Image: Two spectral plots. The first shows high-frequency noise folding into the measurement band after sampling without a filter. The second shows an anti-aliasing filter attenuating high-frequency content before sampling.)
Talking Point: Aliasing is dangerous because it creates false low-frequency content that looks real after sampling. An anti-aliasing filter prevents high-frequency components from folding into the band you intend to analyze. In E3, if your proposed measurement has meaningful frequency content, you need to specify the filter cutoff relative to the signal bandwidth and the sampling rate. This is CLO 4 operating as a design responsibility.

slide 5: Gain and Signal Conditioning
(Image: A small sensor voltage signal entering an amplifier. One output uses too little gain and occupies only a tiny part of the ADC range, one uses too much gain and clips, and one fills the usable DAQ range without saturation.)
Talking Point: Signal conditioning prepares the sensor output for the DAQ. Gain can improve use of the ADC range, but too much gain clips the signal and too little wastes resolution. Filtering can remove noise, but an aggressive filter can remove real signal content. Conditioning choices must be matched to the expected signal amplitude and frequency content.

slide 6: DAQ Resolution and Quantization
(Image: A smooth analog signal overlaid with staircase digitized versions for low-bit and high-bit ADCs. A label shows quantization step size and how it contributes to measurement uncertainty.)
Talking Point: DAQ resolution determines the size of the voltage steps used to represent the analog signal. Those steps produce quantization uncertainty. If the sensor output range is poorly matched to the DAQ input range, quantization can become a dominant error source. Your MATLAB uncertainty analysis should include this contribution when it matters.

slide 7: Grounding, Shielding, and Practical Noise
(Image: A test bench with sensor cables routed near a motor power cable in the bad example and separated with shielding and single-point grounding in the good example. Oscilloscope traces show noisy and clean signals.)
Talking Point: Some measurement problems are not solved by better equations. They are solved by wiring, shielding, grounding, and layout. If your expected signal is small, electromagnetic noise and ground loops can matter as much as sensor accuracy. A credible instrumentation plan identifies these risks before the experiment happens.

slide 8: Standards and Manufacturer Specifications
(Image: A datasheet excerpt stylized with highlighted fields for accuracy, bandwidth, excitation, output sensitivity, calibration, and environmental rating. A standards document sits beside it with reporting requirements highlighted.)
Talking Point: Manufacturer specifications are evidence, but they need to be read carefully. Accuracy, nonlinearity, hysteresis, thermal sensitivity, bandwidth, excitation requirements, and calibration conditions may all appear in different parts of a datasheet. Standards or handbooks can tell you which specifications matter for a measurement type. Your report should cite the specs that actually drive the uncertainty and design choice.

slide 9: Prospective Uncertainty Analysis
(Image: A MATLAB workflow diagram where sensor specs, DAQ resolution, calibration uncertainty, and environmental assumptions feed into a Monte Carlo simulation before hardware purchase. The output is a distribution labeled predicted measurement performance.)
Talking Point: In E3, uncertainty analysis is prospective. You use it before hardware is purchased or selected to predict whether the measurement chain will be good enough. If the predicted uncertainty is too large to distinguish model agreement from disagreement, the design has failed in planning, which is the cheapest time to fail. That is exactly why this course has kept returning to MATLAB uncertainty analysis.

slide 10: Completeness Test for an Instrumentation Plan
(Image: A checklist laid over the measurement chain with boxes for sensor range, sensor accuracy, mounting, sampling rate, filter cutoff, DAQ resolution, calibration, environmental risks, and uncertainty propagation. Blank boxes are highlighted in red.)
Talking Point: A complete instrumentation plan answers each link in the chain. What sensor measures each quantity? How is it mounted? What is the expected signal range and bandwidth? What sampling rate and filter are used? What DAQ resolution and input range are required? What uncertainty sources dominate? If any of those questions are blank, the design is not ready for a V&V plan.

slide 11: Closure
Signal conditioning and DAQ are not afterthoughts. They determine whether the sensor output becomes trustworthy data or just a stream of numbers. E3 asks you to specify the measurement chain prospectively, justify it against intended use, and propagate its uncertainty before the experiment exists. Next week we fold the design, instrumentation, and uncertainty analysis into a formal V&V plan.

## Agent Notes
- Grounded in E3 W12 Lecture 2 purpose and explicitly reconnects E2 signal conditioning/DAQ fundamentals to CLO 4 in E3 design.
