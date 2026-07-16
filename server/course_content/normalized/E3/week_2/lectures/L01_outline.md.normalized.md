slide 1: Title Slide
Title: Sensor Selection Tradeoffs & Matching Sensors to Intended Use
Talking Point: Today we make the E3 design problem concrete: how do you choose a sensor when the experiment is yours? The answer is not "pick the familiar one" or "pick the most expensive one." The answer is to match the sensor to the model question, the accuracy requirement, and the environment in which the measurement must survive.

slide 2: Sensor Choice Is a Validation Choice
(Image: A validation chain from model prediction to physical response to sensor to DAQ to comparison metric. The sensor box is enlarged and labeled "this choice shapes what validation is possible.")
Talking Point: Sensor selection is not a shopping step after the real design work is done. It is part of the validation logic. If the sensor cannot resolve the difference that matters for the intended use, the experiment cannot support the claim. If the sensor changes the system while measuring it, the data may describe the sensor installation more than the original system.

slide 3: Start with the Required Measurement
(Image: A requirements card showing "quantity: force," "range: 0-50 N," "needed agreement: +/-2 N," "bandwidth: 0-20 Hz," and "environment: vibration and temperature drift." Several candidate sensors sit below the card, with only one highlighted.)
Talking Point: Before comparing datasheets, write the measurement requirement. What quantity do you need, over what range, with what accuracy, at what bandwidth, and in what environment? The intended use sets the required fidelity. A sensor that is excellent for a slow calibration load may be useless for a dynamic vibration measurement.

slide 4: Dynamic Range
(Image: A number line from tiny signals to large signals with three sensors represented as windows of measurable range. One sensor saturates at high input, one loses low signals in noise, and one covers the relevant band with margin.)
Talking Point: Dynamic range is the span between the smallest and largest signal a sensor can measure usefully. If your signal exceeds the range, the output saturates. If your signal is too small relative to the sensor noise floor or resolution, the measurement becomes meaningless. In E3, your design needs to show that the expected response fits inside the sensor's useful range with margin.

slide 5: Resolution Is Not Accuracy
(Image: A target diagram with two instruments. One has tightly clustered shots offset from the bullseye labeled "high resolution, poor accuracy." Another has coarser but centered shots labeled "lower resolution, better accuracy." A small digital readout shows many decimal places with a warning label.)
Talking Point: Resolution is the smallest change the sensor or DAQ can display. Accuracy is closeness to the true value. A device can report many decimal places and still be biased. In your instrumentation justification, do not treat a high-resolution number as proof of accuracy. You need the datasheet accuracy, calibration information, and uncertainty propagation to know whether the measurement supports the model comparison.

slide 6: Mounting Effects
(Image: A strain gauge, accelerometer, and pressure tap shown in three mini-panels. Each panel has a correct installation and an incorrect installation, with arrows showing altered load path, mass loading, or flow disturbance.)
Talking Point: Sensors are physical objects, and installing them can change the thing you are trying to measure. A strain gauge depends on bonding and alignment. An accelerometer adds mass and can alter dynamics. A pressure tap can disturb a flow if the geometry is poor. Mounting effects are often the difference between a measurement that is technically defensible and one that only appears precise.

slide 7: Environmental Contamination
(Image: A sensor signal trace surrounded by interference sources labeled temperature drift, vibration cross-axis sensitivity, electromagnetic noise, humidity, and cable motion. Each source injects a different colored disturbance into the signal.)
Talking Point: Real laboratories are not clean mathematical spaces. Temperature, vibration, electromagnetic interference, humidity, and cable motion can all contaminate a measurement. Some contamination looks random, but some produces systematic bias. Your design should identify the likely environmental threats and specify how you will reduce, monitor, or account for them.

slide 8: Resource Constraints Are Real Constraints
(Image: A trade-space plot with axes technical performance and feasibility. Candidate sensors are plotted with tags for cost, lead time, available DAQ compatibility, calibration effort, and student access.)
Talking Point: The best theoretical sensor is not always the best design choice. Cost, availability, lead time, calibration access, compatibility with available DAQ hardware, and setup complexity are legitimate engineering constraints. A strong E3 proposal can choose a less glamorous sensor if it explains why that sensor is adequate for the intended use. Adequacy is the standard, not luxury.

slide 9: Beyond Provided Hardware
(Image: A comparison table between a course-provided sensor and an externally researched alternative. Rows include range, accuracy, bandwidth, mounting burden, cost, calibration, and expected effect on validation credibility.)
Talking Point: CLO 6 asks you to investigate at least one method, sensor, or platform beyond what was handed to you. That does not mean you must adopt it. It means you must evaluate it seriously. Sometimes the outside option will improve the design; sometimes it will reveal that the provided option is already sufficient. Either conclusion is acceptable if the comparison is technical and specific.

slide 10: Matching Sensor to Intended Use
(Image: Three validation scenarios for the same physical quantity: rough trend check, design decision threshold, and certification-level claim. Each scenario maps to increasingly stringent sensor accuracy and documentation requirements.)
Talking Point: Intended use determines how good the measurement needs to be. A sensor adequate for seeing a trend may not be adequate for deciding whether a design passes a requirement. A sensor adequate for a classroom demonstration may not support a high-consequence validation claim. In E3, you must state the intended use before claiming that the instrumentation is good enough.

slide 11: Closure
Sensor selection is a chain of justification: measurement requirement, expected range, accuracy need, dynamic behavior, installation effects, environmental threats, and feasibility. The right sensor is the one that makes the validation comparison credible for the intended use, not the one with the nicest catalog page. In the next lecture, we connect the sensor to the rest of the measurement chain: signal conditioning, sampling, filtering, and DAQ choices.

## Agent Notes
- Grounded in E3 W12 Lecture 1 purpose: dynamic range, resolution versus accuracy, mounting, environmental contamination, resource constraints, intended use.
