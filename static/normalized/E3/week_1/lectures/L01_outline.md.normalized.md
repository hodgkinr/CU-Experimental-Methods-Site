slide 1: Title Slide
Title: Formal Experimental Design — Variables, Replication & Control
Talking Point: Today we move from running experiments that someone else designed to designing experiments ourselves. The core question is no longer just "what did the data say?" but "what experiment would produce data that can actually inform the model?" Experimental design is modeling in hardware, and every choice we make reveals what we think matters.

slide 2: Returning to the AMVF
(Image: A clean AMVF flowchart with the physical modeling branch highlighted in gold and the mathematical modeling branch highlighted in blue. A callout points to the validation comparison node with the question "What would count as evidence?" and arrows show E1 labeled "measure," E2 labeled "predict," and E3 labeled "design.")
Talking Point: We have been using the AMVF all semester, but E3 changes your role inside it. In E1, the experiment was given to you and your job was to measure honestly. In E2, the system was given to you and your job was to predict before measuring. Now the design responsibility shifts to you. You must decide what data the model needs, what response feature matters, and what measurement would be credible enough to support an engineering decision.

slide 3: Experimental Design Is Modeling in Hardware
(Image: Split-screen visual. Left side shows a symbolic predictive model with variables highlighted. Right side shows a physical test setup with matching labels on sensors, inputs, and controlled conditions. A bridge between the panels is labeled "design decisions encode assumptions.")
Talking Point: A model says which variables matter and how they are related. An experiment is the physical arrangement we build to challenge, refine, or support that model. If your model predicts thrust as a function of voltage, airspeed, and propeller geometry, your experiment must create trustworthy information about those quantities. If the experiment ignores a variable the model depends on, the comparison will be weak before you collect a single point of data.

slide 4: Independent, Dependent, and Controlled Variables
(Image: A tabletop wind-tunnel-style test matrix diagram with an input knob labeled "independent variable: airspeed," a measured plot labeled "dependent variable: drag force," and surrounding constraint tags labeled temperature, angle of attack, mounting, and sensor calibration as controlled variables.)
Talking Point: The independent variable is what you intentionally vary. The dependent variable is the system response you measure. Controlled variables are the conditions you try to hold fixed because they could otherwise change the response. In classroom problems these categories look obvious, but in physical experiments they blur quickly. A mounting bracket, a room temperature drift, or a sensor alignment angle can become an uncontrolled variable if you do not design for it.

slide 5: Confounding Factors
(Image: A cause-and-effect diagram showing two arrows entering one measured output. One arrow is labeled "intended cause: input voltage" and the second is labeled "confounder: motor temperature." The measured output is labeled "RPM," with a warning sign reading "apparent causal effect may be mixed.")
Talking Point: A confounding factor is something that changes along with the variable you care about and makes the result hard to interpret. Suppose motor RPM changes as voltage increases, but the motor also heats up during the test sequence. If the heating always happens at the higher voltages, you cannot tell whether the RPM change came from voltage alone or from voltage plus temperature effects. Confounding is dangerous because it does not look like random noise. It looks like evidence until you realize the design allowed two causes to move together.

slide 6: Replication as Defense Against Random Error
(Image: Three side-by-side plots of repeated measurements at the same condition. The first has two scattered points with a wide uncertainty band, the second has ten points with a narrower mean confidence interval, and the third has thirty points with a much tighter confidence interval. A label reads "replication reduces uncertainty in the estimated mean, not the physics of the scatter.")
Talking Point: Replication means repeating a measurement under the same nominal condition so you can estimate random variability. It is not busywork and it is not just a way to make plots look full. Replication tells you whether an observed difference is larger than the noise floor of your measurement process. If your design cannot distinguish the effect you care about from random scatter, then the experiment cannot inform the model at the required level.

slide 7: Randomization and Blocking
(Image: A test schedule board with condition cards A, B, C, and D. One schedule is ordered A-A-B-B-C-C-D-D with a red arrow labeled "time drift risk." A second schedule is randomized within two blocks labeled morning and afternoon, with a blue checkmark labeled "separate treatment effects from drift.")
Talking Point: Randomization protects you from systematic bias caused by time, order, operator fatigue, or environmental drift. Blocking is what you do when you know a nuisance factor exists and you cannot eliminate it, so you group trials in a way that lets you account for it. In aerospace experiments, blocking might mean separating runs by tunnel configuration, battery state, specimen batch, or day of testing. These choices are part of the design, not statistical decoration added later.

slide 8: Control Is Never Perfect
(Image: A physical test stand surrounded by translucent uncertainty clouds labeled alignment, temperature, sensor zero, fixture compliance, and operator setup. A checklist panel beside it shows "measure, monitor, constrain, document.")
Talking Point: Control does not mean the world stops moving. It means you have identified which conditions matter, constrained them as much as practical, and documented what remains. A mature experimental design admits that some variables cannot be perfectly controlled and then decides how to monitor or bound their influence. That honesty is what makes the resulting comparison credible.

slide 9: DOE at Awareness Level
(Image: A simple two-factor grid with factor A on one axis and factor B on the other. Four corner test points are highlighted as a 2x2 factorial design, and a small note says "screening: which factors matter most?" A second mini-panel shows a Taguchi-style orthogonal array as a compact test matrix.)
Talking Point: Design of experiments, or DOE, is a formal way to plan test matrices so that you learn efficiently from a limited number of runs. We are not going deep into factorial design or Taguchi methods in this course, but you need to recognize the idea. When there are multiple possible inputs, a thoughtful test matrix can reveal interactions that one-variable-at-a-time testing would miss. For E3, the practical takeaway is this: your proposed measurements should be chosen because they answer the model question, not because they are the easiest sequence to imagine.

slide 10: Hypothesis Before Hardware
(Image: A design notebook page with three boxed statements: "Model claim," "Data that would support it," and "Data that would challenge it." Below the boxes is a locked equipment cabinet labeled "hardware access comes after the claim is defined.")
Talking Point: A hypothesis is not a guess about what you hope happens. It is a structured claim about what the model predicts and what evidence would support or challenge that prediction. Before you specify hardware, you should be able to say what result would make the model more credible, what result would expose a model limitation, and what uncertainty level would make the comparison meaningful. If you cannot say those things, you are not ready to choose sensors.

slide 11: From E2 Improvement to E3 Design
(Image: A before-and-after storyboard. Left panel shows an E2 report section titled "Improve this experiment" with annotations around residuals and uncertainty bottlenecks. Right panel shows an E3 design proposal with the same annotations converted into design requirements, sensor choices, and validation metrics.)
Talking Point: The improvement proposal in Tier 2 was not an isolated deliverable. It was rehearsal for E3. In E2 you looked at an existing experiment and asked how it could be made more credible. In E3 you start from that same logic but move one step upstream: you design the experiment so the credibility is built in from the beginning. That is a different level of ownership.

slide 12: Closure
The main idea today is that experimental design is not a list of equipment choices. It is a chain of reasoning from model claim, to variables, to controls, to replication, to comparison. Your design decisions determine whether the data can say anything useful about the model before the first measurement is taken. Next we will add the professional reference layer: standards, handbooks, and prior art. That is where your design stops being just your idea and starts becoming part of engineering practice.

## Agent Notes
- Grounded in E3 W11 Lecture 1 purpose: variables, control, confounding, replication, randomization, blocking, DOE awareness, and AMVF return.
- Treats E3 as paper experimental design while keeping the language tied to credible physical implementation.
