slide 1: Title Slide
Title: MATLAB-Based Uncertainty Analysis for V&V Planning
Talking Point: Today we use uncertainty analysis in its most powerful form: before the experiment exists. In E1 and E2, MATLAB helped you interpret measurements after or during an experiment. In E3, MATLAB helps you decide whether the proposed experiment is worth doing.

slide 2: Prospective Instead of Retrospective
(Image: Two timelines. The first is labeled retrospective: build, measure, analyze uncertainty, discover design was not sensitive enough. The second is labeled prospective: model specs, simulate uncertainty, revise design, then measure.)
Talking Point: Retrospective uncertainty analysis tells you how much confidence to place in data you already collected. Prospective uncertainty analysis predicts how well the measurement chain should perform before you commit to it. That shift is central to E3. If you can discover a weak design on paper, you can improve it before wasting time, money, or credibility.

slide 3: Inputs to the Uncertainty Model
(Image: A MATLAB input dashboard with fields for sensor accuracy, calibration uncertainty, DAQ resolution, repeatability estimate, environmental drift, and model parameters. Each field feeds into a measurement equation.)
Talking Point: Your uncertainty model starts with the same things your instrumentation report should specify. Sensor accuracy, calibration uncertainty, DAQ resolution, expected repeatability, environmental effects, and model parameters all become inputs. Some are numbers from datasheets. Some are estimates from standards or prior art. Some are assumptions that must be named because unnamed assumptions are hidden risk.

slide 4: Measurement Equation
(Image: A central equation box labeled measured outcome = f(sensor signals, calibration constants, geometry, environmental corrections). Colored arrows from each variable point to its uncertainty contribution.)
Talking Point: The measurement equation connects raw measurements to the final quantity used in the validation metric. It might be as simple as P equals IV or as complex as a reduced aerodynamic coefficient. The uncertainty analysis must propagate uncertainty through this equation. If the V&V plan compares a model to a derived quantity, the derived quantity's uncertainty is what matters.

slide 5: Partial Derivatives and Sensitivity
(Image: A tornado chart ranking uncertainty contributors by their effect on final output. Beside it is a small symbolic derivative graphic showing each input pushing on the output.)
Talking Point: Partial-derivative propagation gives you a local sensitivity picture. It tells you which input uncertainty matters most near the operating point. That is useful because it points directly to design improvements. If DAQ resolution barely matters but sensor calibration dominates, buying a higher-bit DAQ is not the fix. The fix is calibration, sensor accuracy, or a different measurement strategy.

slide 6: Monte Carlo for the Full Chain
(Image: A Monte Carlo workflow with random samples drawn from input distributions, passed through the measurement equation, and collected into an output histogram. The histogram is marked with mean, 95% interval, and acceptance band.)
Talking Point: Monte Carlo lets you propagate uncertainties through nonlinear equations, mixed distributions, and more complicated measurement chains. Instead of linearizing everything, you sample plausible input values and compute the resulting output many times. The output distribution shows the predicted measurement performance. This is the distribution you compare to the validation requirement.

slide 7: Distinguishing Model Agreement from Disagreement
(Image: A plot with model prediction, predicted measurement uncertainty band, and acceptable agreement region. One case shows uncertainty small enough to distinguish pass/fail; another shows uncertainty so wide that both agreement and disagreement are plausible.)
Talking Point: The key E3 question is not simply "what is the uncertainty?" It is "is the uncertainty small enough to make the planned comparison meaningful?" If the uncertainty band is wider than the difference your intended use cares about, the experiment cannot distinguish model agreement from disagreement. That does not mean the model is wrong. It means the experimental design is underpowered for the claim.

slide 8: Design Iteration from Uncertainty Results
(Image: A decision loop: run prospective uncertainty analysis, identify dominant contributor, modify sensor/DAQ/test matrix/model response feature, rerun analysis. The loop exits only when predicted uncertainty supports the validation metric.)
Talking Point: The uncertainty result should change the design if it exposes a weakness. You might choose a more accurate sensor, increase replication, change the response feature, narrow the intended use, improve calibration, or redesign the test matrix. This is where E3 becomes engineering design rather than document production. The analysis must have consequences.

slide 9: MATLAB Outputs to Include in the V&V Plan
(Image: A V&V plan figure set: input uncertainty table, tornado sensitivity chart, Monte Carlo histogram, and validation comparison plot. A caption note says "figures make the argument.")
Talking Point: Your V&V plan should include the outputs that support the argument. At minimum, I expect a table of uncertainty inputs, a ranking or sensitivity statement for dominant sources, a Monte Carlo output distribution when appropriate, and an interpretation against the validation criterion. Figures should not merely show that MATLAB ran. They should answer whether the proposed experiment can do the job.

slide 10: Common Failure Modes
(Image: Four warning cards: using resolution as accuracy, omitting calibration uncertainty, ignoring bandwidth, and reporting uncertainty without interpreting it. Each card has a small example icon.)
Talking Point: The common failures are predictable. Students use DAQ resolution as if it were total accuracy. They omit calibration uncertainty. They ignore bandwidth and sampling even when the response is dynamic. Or they compute a beautiful uncertainty number and never say whether it is good enough. Avoiding these failures is mostly about remembering that uncertainty analysis serves the validation decision.

slide 11: Closure
Prospective uncertainty analysis is the quantitative engine of E3. It connects sensor specifications, DAQ choices, calibration assumptions, and model comparison into one design decision: will this experiment produce evidence strong enough for the intended use? If the answer is no, that is not a disaster. It is the design telling you where to improve before the real costs arrive. That is exactly the kind of judgment professional experimental engineers are paid to develop.

## Agent Notes
- Grounded in E3 W13 Lecture 2 purpose: MATLAB uncertainty analysis before hardware selection, Monte Carlo propagation, interpretation against intended use.
