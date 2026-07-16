slide 1: Title Slide
Title: V&V Plan Components & Intended Use as Framing Constraint
Talking Point: Week 13 is where E3 becomes a complete engineering argument. You have a proposed experiment, references, and instrumentation choices; now you have to organize them into a V&V plan. The plan is not paperwork after design. It is the logic that explains why the design would produce useful evidence.

slide 2: What a V&V Plan Does
(Image: A structured V&V plan document shown as a spine with sections branching off: conceptual model, hypothesis, response features, validation metrics, accuracy requirements, uncertainty, calibration, AMVF mapping, intended use.)
Talking Point: A V&V plan tells a reviewer what model is being evaluated, what evidence will be collected, how agreement will be judged, and why that judgment is sufficient for the intended use. It is prospective, meaning it is written before the data exists. That matters because it prevents us from moving the goalposts after seeing results. A good V&V plan makes the comparison honest before the experiment begins.

slide 3: Intended Use Comes First
(Image: Three model-use cards for the same system: classroom trend explanation, preliminary design sizing, and safety-critical decision. Each card has a different acceptable agreement threshold and required evidence level.)
Talking Point: Intended use is the framing constraint for the entire plan. The same model can be adequate for one purpose and inadequate for another. If the model is only being used to rank concepts, rough agreement may be enough. If it is being used to make a high-consequence design decision, the validation evidence must be much stronger. Without intended use, "valid" has no engineering meaning.

slide 4: Conceptual Model and Formal Hypothesis
(Image: A conceptual model sketch with input variables, assumptions, governing relationship, and predicted response. Beside it is a hypothesis card that states expected trend, confirming data pattern, and challenging data pattern.)
Talking Point: The conceptual model describes what you believe the system is and which physics matter. The hypothesis turns that model into a testable claim. I want the hypothesis to say more than "the model will match the data." It should identify what pattern, parameter, trend, or response feature the experiment is designed to confirm or challenge. That is how the experiment informs the model rather than simply stamps it pass or fail.

slide 5: System Response Features
(Image: A complex response curve with three highlighted features: peak value, slope in a linear region, and resonant frequency. Each feature is connected to a different model assumption.)
Talking Point: A system response feature is the specific thing in the data that the model must predict. It might be a peak force, a time constant, a slope, a frequency, an efficiency, or a threshold. Choosing the response feature is one of the most important design decisions because it decides what evidence counts. If your response feature is vague, your validation metric will be vague too.

slide 6: Validation Metrics
(Image: A table mapping response features to metrics: percent error for peak value, RMSE for curve agreement, confidence interval overlap for means, residual trend for model form. A warning note says "metric must match the question.")
Talking Point: The validation metric is how you measure agreement. Different response features need different metrics. A single peak value might use percent difference with uncertainty bounds. A full curve might use residual analysis or RMSE. A repeated condition might use confidence intervals. The metric should be chosen because it answers the intended-use question, not because it is familiar.

slide 7: Accuracy Requirements and Acceptable Agreement
(Image: A prediction-data comparison plot with a shaded acceptable agreement band set before testing. A lock icon labels the band "committed before measurement.")
Talking Point: Accuracy requirements define how close is close enough. This is where engineering significance enters the V&V plan. A statistically detectable difference may still be acceptable, and a statistically inconclusive result may reveal that the experiment is too weak. The acceptable agreement criterion must be stated before data collection because it represents the intended use, not the result you hope to get.

slide 8: Calibration Is Not Validation
(Image: Two separate loops. One loop shows sensor output compared to a known reference labeled calibration. The other shows model prediction compared to independent system response data labeled validation. A red X blocks an arrow that tries to substitute calibration for validation.)
Talking Point: Calibration and validation answer different questions. Calibration asks whether an instrument reports a known quantity correctly. Validation asks whether a model predicts system behavior adequately for its intended use. A calibrated sensor is necessary for many experiments, but it does not validate the model. Your V&V plan must identify which activities are calibration activities and which are validation activities.

slide 9: Hierarchical Validation
(Image: A pyramid with component tests at the bottom, subsystem tests in the middle, and full system validation at the top. Arrows show evidence building upward, with uncertainty increasing as complexity grows.)
Talking Point: Hierarchical validation means building credibility from simpler pieces toward more complex systems. You may validate a sensor calibration, then a component response, then a subsystem prediction, and only later a full-system behavior. E3 projects are small, but the logic still applies. Your planned experiment should state what level of the hierarchy it addresses and what it does not claim.

slide 10: AMVF Annotation
(Image: The AMVF flowchart with sticky-note annotations attached to nodes: conceptual model, physical realization, data, uncertainty quantification, comparison, model update. Each sticky note references a V&V plan section.)
Talking Point: The AMVF annotation is your map showing where each part of the plan lives in the course framework. It should identify the model branch, the physical experiment branch, the uncertainty work, the comparison metric, and the model-improvement step. This is not just a decorative figure. It is a check that your plan has all the logical pieces connected.

slide 11: Closure
A V&V plan is a promise about how evidence will be created and interpreted. Intended use sets the standard, the conceptual model and hypothesis define the claim, response features and metrics define the comparison, and uncertainty analysis tells us whether the planned evidence is strong enough. In the next lecture we focus on that uncertainty analysis as a design tool. That is the moment where your proposed experiment either earns credibility or shows you what must be redesigned.

## Agent Notes
- Grounded in E3 W13 Lecture 1 purpose: V&V plan structure, intended use, response features, validation metrics, calibration versus validation, hierarchy, AMVF.
