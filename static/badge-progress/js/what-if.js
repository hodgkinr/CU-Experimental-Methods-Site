import { BADGE_STATE_THRESHOLDS, PROTOTYPE_STATE_LEVELS, loadCourseModel } from "./course-config.js";
import { decodeProgressCode, validatePacket } from "./packet.js";
import { verifyEnvelope } from "./verification.js";

let course;
let event;
let simulated = {};
let reqSimulated = {};
const form = document.querySelector("#progress-form");

init().catch((error) => message(error.message, true));

async function init() {
  const isEmbed = location.hash.toLowerCase() === "#embed";
  if (isEmbed) document.documentElement.classList.add("embed-view");
  course = await loadCourseModel();
  document.querySelector("#all-proficient").addEventListener("click", () => bulkClo(BADGE_STATE_THRESHOLDS.proficient));
  document.querySelector("#all-mastery").addEventListener("click", () => bulkClo(BADGE_STATE_THRESHOLDS.mastery));
  document.querySelector("#all-passed").addEventListener("click", () => {
    course.majorAssessments.forEach((a) => { if (event?.majorAssessmentStates[a.id] !== 1) reqSimulated[a.id] = 1; });
    render();
  });
  form.addEventListener("submit", async (e) => { e.preventDefault(); await loadCode(document.querySelector("#progress-code").value); });
  const code = new URLSearchParams(location.search).get("progress");
  if (code) { document.querySelector("#progress-code").value = code; await loadCode(code); }
}

async function loadCode(code) {
  try {
    message("Checking signed progress code…");
    const envelope = decodeProgressCode(code);
    if (!await verifyEnvelope(envelope)) throw new Error("This progress code is invalid or has been modified.");
    validatePacket(envelope.payload, course);
    event = envelope.payload.events.at(-1);
    const back = new URL("./badge-progress.html", location.href);
    back.searchParams.set("progress", code.trim());
    if (location.hash.toLowerCase() === "#embed") back.hash = "embed";
    document.querySelector("#progress-page-link").href = back.href;
    simulated = { ...event.subCLOStates };
    reqSimulated = { ...event.majorAssessmentStates };
    document.querySelector("#packet-status").textContent = "Signed packet verified";
    document.querySelector("#checkpoint-status").textContent = event.eventLabel || "Current checkpoint";
    render();
    message("Progress loaded. Adjust future results to explore possible grade ranges.");
  } catch (error) { event = null; message(error.message || "Unable to load progress code.", true); }
}

function render() {
  const cloRoot = document.querySelector("#clo-controls");
  cloRoot.replaceChildren();
  course.clos.forEach((clo) => {
    const card = document.createElement("article"); card.className = "what-if-card";
    const heading = document.createElement("h3"); heading.textContent = `${clo.id}: ${clo.title}`; card.append(heading);
    clo.subCLOs.forEach((sub) => {
      const current = event.subCLOStates[sub.id] ?? -1;
      const selected = Math.max(current, simulated[sub.id] ?? current);
      const row = document.createElement("label"); row.className = "what-if-row";
      const name = document.createElement("span"); name.textContent = `${sub.id} ${sub.title}`;
      const select = document.createElement("select"); select.setAttribute("aria-label", `${sub.id} projected score`);
      const currentOption = document.createElement("option"); currentOption.value = String(current); currentOption.textContent = current < 0 ? "Not yet assessed" : `Current: ${PROTOTYPE_STATE_LEVELS[current].label}`; select.append(currentOption);
      for (let value = Math.max(0, current + 1); value <= 3; value++) { const opt = document.createElement("option"); opt.value = String(value); opt.textContent = `Future: ${PROTOTYPE_STATE_LEVELS[value].label}`; select.append(opt); }
      select.value = String(selected); select.disabled = current === 3;
      select.addEventListener("change", () => { simulated[sub.id] = Number(select.value); updateGrade(); });
      row.append(name, select); card.append(row);
    });
    cloRoot.append(card);
  });
  const reqRoot = document.querySelector("#requirement-controls"); reqRoot.replaceChildren();
  const examGroup = document.createElement("fieldset"); examGroup.className = "what-if-exam-group";
  const examLegend = document.createElement("legend"); examLegend.textContent = "Either In-class Exam or Final Assessment"; examGroup.append(examLegend);
  course.majorAssessments.forEach((assessment) => {
    const passed = event.majorAssessmentStates[assessment.id] === 1;
    const row = document.createElement("label"); row.className = `requirement-item what-if-requirement${passed ? " is-passed" : ""}`;
    const name = document.createElement("span"); name.className = "requirement-name"; name.textContent = assessment.label;
    const input = document.createElement("input"); input.type = "checkbox"; input.checked = passed || reqSimulated[assessment.id] === 1;
    const alternate = ["in_class_exam", "final_assessment"].includes(assessment.id);
    const alternatePassed = reqSimulated[assessment.id === "in_class_exam" ? "final_assessment" : "in_class_exam"] === 1 || event.majorAssessmentStates[assessment.id === "in_class_exam" ? "final_assessment" : "in_class_exam"] === 1;
    input.disabled = passed || (alternate && alternatePassed);
    input.setAttribute("aria-label", `Mark ${assessment.label} as passed`);
    input.addEventListener("change", () => { reqSimulated[assessment.id] = input.checked ? 1 : 0; render(); });
    const status = document.createElement("span"); status.className = "requirement-state"; status.textContent = passed ? "Completed" : "Mark pass";
    row.append(name, status, input);
    if (alternate) examGroup.append(row); else reqRoot.append(row);
  });
  reqRoot.append(examGroup);
  updateGrade();
}

function bulkClo(target) {
  course.clos.forEach((clo) => clo.subCLOs.forEach((sub) => {
    const current = event.subCLOStates[sub.id] ?? -1;
    if (current < target) simulated[sub.id] = target;
  }));
  render();
}

function updateGrade() {
  const allProficient = course.clos.every((clo) => clo.subCLOs.every((sub) => (simulated[sub.id] ?? event.subCLOStates[sub.id] ?? -1) >= BADGE_STATE_THRESHOLDS.proficient));
  const masteredClos = course.clos.filter((clo) => clo.subCLOs.length && clo.subCLOs.every((sub) => (simulated[sub.id] ?? event.subCLOStates[sub.id] ?? -1) >= BADGE_STATE_THRESHOLDS.mastery)).length;
  const requiredPassed = course.majorAssessments.every((a) => ["final_assessment", "in_class_exam"].includes(a.id) || reqSimulated[a.id] === 1 || event.majorAssessmentStates[a.id] === 1);
  const examPassed = reqSimulated.in_class_exam === 1 || event.majorAssessmentStates.in_class_exam === 1;
  const finalPassed = reqSimulated.final_assessment === 1 || event.majorAssessmentStates.final_assessment === 1;
  const allReq = requiredPassed && (examPassed || finalPassed);
  let grade = "Below C range"; let reason = "A C-range outcome requires proficiency in all six CLOs and passing the core requirements.";
  if (allProficient && allReq) {
    grade = "C range"; reason = "All six CLOs are proficient and the required assessments are marked passed.";
    if (masteredClos > 0) { grade = "B range"; reason = `${masteredClos} of ${course.clos.length} CLOs currently show full mastery. The B-range description also includes generally strong professional performance.`; }
    if (masteredClos >= Math.ceil(course.clos.length * 2 / 3)) { grade = "A range possible"; reason = `${masteredClos} of ${course.clos.length} CLOs show full mastery. The A-range description also considers sustained, integrative performance, especially in culminating work.`; }
  } else if (!allReq) reason = "Pass all required major course requirements to meet the C-range description. The Final Assessment is optional if the In-class Exam is passed.";
  else reason = "Every sub-CLO must reach Proficient for all six CLOs before the C-range description is met.";
  document.querySelector("#grade-heading").textContent = grade;
  document.querySelector("#grade-reason").textContent = reason;
}

function message(text, error = false) { const node = document.querySelector("#message"); node.textContent = text; node.classList.toggle("error", error); }
