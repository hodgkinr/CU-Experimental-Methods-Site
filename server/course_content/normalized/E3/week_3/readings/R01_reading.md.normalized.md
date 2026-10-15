# Measurement Approach: Proposal Checkpoint Guide
## Add only the instrumentation detail that matters to your experiment

Use this guide while refining the existing Tier 3 proposal. It is not a separate report or form. You do not need to complete every prompt when it does not apply to your experiment.

## Describe the measurement chain

For each primary response, briefly trace:

> Physical quantity → sensor or method → relevant conditioning → DAQ or recording → processing → reported response

Name the method or instrument and cite a credible source for important specifications. Explain why its range and accuracy are appropriate. Address response speed/bandwidth, mounting, environment, or calibration only when they affect the intended measurement.

## Dynamic and sampled measurements

If the signal changes with time or contains meaningful frequency content, estimate the frequency or bandwidth that must be represented. Use it to justify a reasonable sample rate and identify an anti-aliasing or filtering need. Explain any gain or conditioning choice that materially affects the signal. For static or slow measurements, say briefly why a dynamic sampling analysis is not relevant.

## DAQ and practical limits

Identify the DAQ input range and resolution when they could limit the measurement. Mention channel setup, triggering, synchronization, grounding, or shielding only when they affect data quality. Note relevant calibration status and the main limitation of the full chain.

## Uncertainty and adequacy

Name the uncertainty sources most likely to affect the conclusion. A simple estimate or first-order propagation is sufficient when it answers the design question. Monte Carlo may be useful for a nonlinear or nonstandard case, but it is not required by default. Do not submit MATLAB code or a full uncertainty budget unless your instructor has specifically assigned it.

## Checkpoint review

- [ ] The selected method can measure the intended quantity and expected range.
- [ ] The most relevant specifications are supported by a source.
- [ ] Conditioning, sampling, or DAQ choices are explained where they matter.
- [ ] The dominant uncertainty or measurement limitation is identified.
- [ ] These choices support the model comparison in the proposal.

Add the relevant reasoning to the existing proposal at its scheduled refinement checkpoint. Do not submit this guide separately, create a component procurement list, or repeat the proposal in a standalone instrumentation report.
