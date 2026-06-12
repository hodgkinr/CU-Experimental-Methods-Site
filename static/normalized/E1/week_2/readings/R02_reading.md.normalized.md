# Technical Writing in Engineering
## Say What You Mean, Prove What You Say

The hardest thing about technical writing is not grammar. It is the discipline of making a claim and then stopping, without hedging or over-explaining, and letting the evidence speak for itself.

---

You have been writing for years. You know how to tell a story, argue a point, describe something you observed. Technical writing uses none of those skills in quite the same way. It's a different genre with different rules, and the rules exist for a specific reason: engineering writing isn't read for enjoyment. It's read by someone who needs to make a decision, verify a result, reproduce a measurement, or check your work. Every sentence exists to support that purpose, or it should not exist at all.

This reading gives you the practical framework for engineering writing that you'll apply throughout this course, starting with the Lab 1 brief report this week.

---

## The Reader You Are Writing For

Before writing a single sentence, ask yourself: *who reads this, and what do they need from it?*

In professional engineering, your reader is a technical person who has never seen your specific work before. They are competent; they understand the physics, the methods, the vocabulary. They are not, however, clairvoyant. They cannot infer what you measured from how you describe your setup. They cannot reconstruct your uncertainty calculation from a result with no error bars. They cannot evaluate your conclusion without knowing how you got there.

**Write for the skeptical expert, not the sympathetic friend.** The sympathetic friend fills in gaps; the skeptical expert points at them. The goal is a document that survives the skeptical expert: one where every claim is supported, every result is reproducible, and no reader has to guess at anything essential.

A second audience worth naming explicitly: the non-engineer. Several assignments in this course ask you to explain a technical result to someone without an engineering background. This is not dumbing down. It's a different technical skill. Plain-language communication requires you to identify the *essential idea* underneath the technical apparatus and express it without jargon. If you cannot do that, it is a signal that your own understanding is not yet complete.

![A two-panel illustration. Left panel, labeled "The Sympathetic Friend," shows a reader leaning forward, nodding, filling in a thought bubble with a complete version of an incomplete sentence: the written text trails off mid-sentence but the reader's thought bubble finishes it generously. Right panel, labeled "The Skeptical Expert," shows a reader with a red pen, question marks in their thought bubble, circling the same incomplete sentence and writing "Insufficient detail — how was this measured?" Clean editorial illustration style, black and white with one accent color.](../images/E1_W2_R2_image1.png)

### Worked Example: From Engineering Form to Plain Language

Here is the same result written two ways.

**Engineering form (for the skeptical expert):**
> "The measured electrical power dissipated in a 5 Ω resistor with a 12 V input is 25.7 ± 1.3 W at 95% confidence, derived using partial derivative uncertainty propagation from voltage and current measurements with a ±0.2 V voltmeter and ±0.05 A ammeter."

This version is correct and complete. Every number is supported. Every bound is traceable to a method. A colleague can reproduce the result.

**Plain-language version (for the non-engineer):**
> "We measured how much electrical power a small resistor was consuming when connected to a 12-volt source — similar to a standard lantern battery. The result was about 26 watts, roughly the energy a dim incandescent bulb uses. Our measurement has an uncertainty of about 5%, which means the true value is almost certainly somewhere between 24 and 27 watts."

**What changed and why:**
- *Uncertainty expressed as consequence, not as a statistical bound.* "±1.3 W at 95% confidence" is meaningless to a non-engineer; "about 5%" gives a sense of scale, and "almost certainly between 24 and 27 watts" states the consequence in plain language.
- *Physical result grounded in an everyday reference.* "25.7 W" is a number; "roughly the energy a dim incandescent bulb uses" is a physical anchor that makes the magnitude interpretable.
- *Technical method removed.* The non-engineer reader does not need to know about partial derivative propagation; they need to trust that the measurement was done carefully. That trust is built through the framing ("our measurement has an uncertainty of about 5%"), not through the method details.

The skeptical expert version and the plain-language version contain the same core result. Writing both isn't redundant. It's evidence that you understand the result well enough to translate it. Several deliverables in this course require both: the Lab 1 brief report, the Phase 1 report (Section 9), and the Phase 3 presentation.

---

## The Architecture of a Technical Document

Every technical document (lab report, memo, technical note) is a narrative. Not a story with plot and character, but a logical argument that has a beginning, a middle, and an end. Readers orient by structure. A document without clear structure wastes the reader's time.

The standard structure for an engineering report maps directly onto the logical arc of a technical argument:

**Introduction** — Three things, in this order: (1) what this document is about and why it was written; (2) what new information it contains that the reader did not have before; (3) why the results matter. The introduction is not background for its own sake; it is a contract with the reader about what they are about to receive.

**Body** — The evidence: your method, your measurements, your analysis. Sufficient detail that someone else could reproduce your results. This is where your figures, tables, and equations live, each one integrated into the narrative, not appended to it.

**Conclusion** — Not a summary of the introduction. A conclusion states: (1) what was found; (2) what that finding implies; (3) what remains uncertain or unresolved; (4) what comes next. Conclusions that merely restate the introduction have done nothing.

If a section of your report does not serve one of these three purposes, it probably should not be there.

---

## Figures: The Core Unit of Technical Communication

Most technical writing errors are not in the prose. They are in the figures and in the prose that surrounds them. A figure in an engineering report is not a visual aid. It is an argument. It exists to support a specific claim, and every element of the figure must serve that claim.

When you produce any figure in this course, the following elements are required, not optional:

- **Labeled axes with units.** "Force (N)" not "Force." "Time (s)" not "seconds." No axis is unlabeled, no unit is omitted.
- **A caption that identifies and explains.** The caption must name every plotted element and explain what the figure shows. "Figure 2. Measured power vs. voltage for all three configurations" is a label. "Figure 2. Measured power as a function of applied voltage for the P = IV, P = V²/R, and P = I²R configurations. Error bars represent ±1σ from partial-derivative uncertainty propagation. The three configurations converge at low voltages but diverge above 5V, consistent with resistance variation as a function of temperature." That is a caption.
- **Reference in the text.** Every figure is referenced before it appears. "Figure 2 shows..." or "as shown in Figure 2..." Never let a figure float in the document without a textual anchor that explains why it is there.
- **Conclusions drawn explicitly.** Do not leave the reader to extract the point. After referencing the figure, state what it shows, what it implies, and whether any anomalies require explanation.

![Two versions of the same MATLAB-style scatter plot with a best-fit line. Top version, labeled "Insufficient," has unlabeled axes ("x" and "y"), no units, a title that says "Data," and no caption below. Bottom version, labeled "Sufficient," has the same data but with fully labeled axes ("Applied Voltage (V)" and "Measured Power (W)"), a legend, error bars on data points, a figure number, and a two-sentence caption that names the trend and identifies what the error bars represent. Same data, entirely different level of communication. Clean technical diagram style.](../images/E1_W2_R2_image2.png)

---

## The Language of Technical Writing

Engineering writing has a distinctive voice, and it is not stuffy or passive by accident. The conventions exist because precision matters more than personality.

**No contractions.** "Do not" not "don't." "Cannot" not "can't." This isn't pedantry; contractions signal informality and undermine technical credibility in a professional document.

**Define before you use.** Every acronym is spelled out on first use: "National Aeronautics and Space Administration (NASA)." Every non-obvious symbol is defined. Assume the reader can look up a word; do not assume they will know what your variable names mean.

**Be specific.** Vague claims invite skepticism. "The measurement was close to the predicted value" tells the reader nothing useful. "The measured power (4.32 W) fell within the 95% confidence interval of the propagated uncertainty estimate (4.18 to 4.51 W)" makes a falsifiable claim. Every quantitative result should be stated with its uncertainty in engineering form: *estimate ± uncertainty (units, method, confidence level).*

**Active voice, lean sentences.** "The apparatus was connected, and three sets of data were collected" is cleaner than "I plugged in the apparatus and successfully collected three sets of data." The passive voice is appropriate when the actor is irrelevant or unknown, not as a default. The goal is directness, not impersonality.

**Remove what does not earn its place.** Technical writing is edited ruthlessly. Words like "very," "basically," "actually," "in order to," "it should be noted that," and "as previously mentioned" add length without adding meaning. The revision process is not about polishing prose. It's about cutting everything that does not serve the reader's need to understand your result.

---

## Numbers, Equations, and Units

Numbers and equations follow conventions that are enforced uniformly in professional engineering writing, and they will be enforced in this course.

- **Space between number and unit.** Write `9.81 m/s²` not `9.81m/s²`. Write `2.4 mm` not `2.4mm`. No exceptions.
- **Consistent units.** Do not switch between metric and imperial mid-document. If your data is in N, your results are in N.
- **Variables are italicized; numbers and units are not.** The variable *P* represents power; the value 4.32 W is a measurement. Only variables are italicized.
- **Equations are part of the text.** Introduce every equation in a sentence: "Power dissipated in the resistor is given by..." Equations aren't standalone objects; they are statements that the surrounding prose must set up and interpret.
- **Every result carries uncertainty.** A number without uncertainty bounds is not an engineering result; it is a reading. State method, confidence level, and bounds every time.

---

## The Revision Mindset

Good technical writing isn't written; it's revised. The document you produce in the first pass is a draft that organizes your thinking, not a product that communicates it. Every professional communicator, engineers included, treats revision as the actual work.

A practical three-pass approach: **First pass**, check structure. Does the document have a clear introduction, body, and conclusion that form a complete logical argument? **Second pass**, check claims. Is every quantitative statement supported? Is every figure correctly referenced and captioned? Is every conclusion drawn explicitly from evidence? **Third pass**, check language. Are there contractions? Vague terms? Redundant words? Sentences that could be cut in half without losing meaning?

This course's use of AI for drafting does not change this framework. It intensifies it. An AI-generated draft may have perfect grammar and confident tone while being subtly wrong about the physics, imprecise about the uncertainty, or logically disconnected in its conclusions. **Your job isn't to produce the draft; it is to know what right looks like so you can recognize when the draft is wrong.** The revision mindset is the professional skill this course is building.

![A horizontal flow diagram with three labeled stages. Stage 1, "Draft," shows a rough document icon with a thought bubble that says "organized my ideas." Stage 2, "Revision," shows a document with red ink marks, strikethroughs, and margin notes — labels point to specific types of edits: "structural," "claims," "language." Stage 3, "Final," shows a clean document icon with a checkmark. An arrow beneath all three stages reads: "The revision IS the work." Flat illustration style, clean typography, CU Boulder gold accent color on the arrow.](../images/E1_W2_R2_image3.png)

---

## A Checklist for Every Deliverable

Before submitting any written work in this course, confirm:

- [ ] Every figure has labeled axes with units, a complete caption, and an explicit reference in the text
- [ ] Every quantitative result is stated in engineering form: estimate ± uncertainty (units, method, confidence level)
- [ ] The introduction states purpose, new information, and significance
- [ ] The conclusion states findings, implications, uncertainties, and next steps, not a restatement of the introduction
- [ ] No contractions appear anywhere in the document
- [ ] Every acronym is defined on first use; every symbol is defined before use
- [ ] There is a space between every number and its unit
- [ ] Units are consistent throughout
- [ ] Every claim that needs evidence has it
- [ ] The document has been read aloud at least once; sentences that are hard to say aloud are hard to read

---

**The Takeaway:** Technical writing is not a soft skill bolted onto engineering. It is the mechanism by which your results become claims that others can evaluate, reproduce, and build on. A result that cannot be communicated clearly is a result that does not yet exist as engineering knowledge.

---

*CLO Alignment: CLO 5 — Communicate experimental results effectively using standard technical writing conventions*
*Assigned: E1, Week 2 | Companion deliverable: Lab 1 Brief Report*
*Sources: Write More Good Club Technical Writing Checklist (UTEP/Rumpf Lab); Technical Writer's Checklist, TSC 2007; ASEN 2003 Lab Report Guide (Scheeres/Park, CU Boulder)*
