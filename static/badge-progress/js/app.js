import { loadCourseModel } from "./course-config.js";
import { decodeProgressCode, summarizePacket, validatePacket } from "./packet.js";
import { verifyEnvelope } from "./verification.js";
import { renderBadges, renderRequirements, renderSummary } from "./badge-renderer.js";

const state = {
  courseModel: null,
  packet: null,
  selectedIndex: 0,
  previousIndex: null
};

init().catch((error) => {
  showMessage(error.message, true);
});

async function init() {
  state.courseModel = await loadCourseModel();
  bindProgressForm();
  resetDisplay();

  const progressFromUrl = new URLSearchParams(window.location.search).get("progress");
  if (progressFromUrl) {
    await loadProgressCode(progressFromUrl, "URL progress code");
  } else {
    showMessage("Paste a signed progress code to view the badge board.", false);
  }
}

function bindProgressForm() {
  document.querySelector("#progress-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    const code = document.querySelector("#progress-code").value;
    await loadProgressCode(code, "Manual progress code");
  });

  document.querySelector("#timeline").addEventListener("input", (event) => {
    state.previousIndex = state.selectedIndex;
    state.selectedIndex = Number(event.target.value);
    renderCurrentCheckpoint();
  });
}

async function loadProgressCode(code, sourceLabel) {
  try {
    showMessage("Checking progress code signature...", false);
    const envelope = decodeProgressCode(code);
    const verified = await verifyEnvelope(envelope);
    if (!verified) {
      throw new Error("This progress code is invalid or has been modified. Please use the most recent progress link provided by the instructional team.");
    }
    validatePacket(envelope.payload, state.courseModel);
    state.packet = envelope.payload;
    state.selectedIndex = state.packet.events.length - 1;
    state.previousIndex = null;
    document.querySelector("#progress-code").value = code;
    document.querySelector("#packet-status").textContent = "Signed packet verified";
    setupTimeline();
    renderCurrentCheckpoint();
    const summary = summarizePacket(state.packet, state.courseModel);
    showMessage(`${sourceLabel} loaded. ${summary.eventCount} checkpoints, ${summary.subCLOCount} sub-CLOs, ${summary.assessmentCount} requirements.`, false);
  } catch (error) {
    state.packet = null;
    document.querySelector("#packet-status").textContent = "Code rejected";
    resetDisplay();
    showMessage(error.message.includes("invalid or has been modified") ? error.message : "This progress code is invalid or has been modified. Please use the most recent progress link provided by the instructional team.", true);
  }
}

function setupTimeline() {
  const timeline = document.querySelector("#timeline");
  timeline.max = String(state.packet.events.length - 1);
  timeline.value = String(state.selectedIndex);
  const labels = document.querySelector("#timeline-labels");
  labels.replaceChildren(...state.packet.events.map((event) => {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = event.eventLabel || event.eventId || "Checkpoint";
    button.addEventListener("click", () => {
      state.previousIndex = state.selectedIndex;
      state.selectedIndex = state.packet.events.indexOf(event);
      renderCurrentCheckpoint();
    });
    return button;
  }));
}

function renderCurrentCheckpoint() {
  if (!state.packet) return;
  const event = state.packet.events[state.selectedIndex];
  const previousEvent = Number.isInteger(state.previousIndex) ? state.packet.events[state.previousIndex] : null;
  document.querySelector("#timeline").value = String(state.selectedIndex);
  document.querySelector("#timeline-output").textContent = event.eventLabel || "Current";
  document.querySelector("#checkpoint-status").textContent = `${event.eventLabel || "Checkpoint"} selected`;
  document.querySelectorAll("#timeline-labels button").forEach((button, index) => {
    button.setAttribute("aria-current", String(index === state.selectedIndex));
  });
  renderSummary({ courseModel: state.courseModel, event });
  renderBadges({ courseModel: state.courseModel, event, previousEvent });
  renderRequirements({ courseModel: state.courseModel, event });
}

function showMessage(message, isError) {
  const element = document.querySelector("#message");
  element.textContent = message;
  element.classList.toggle("error", isError);
}

function resetDisplay() {
  document.querySelector("#timeline").max = "0";
  document.querySelector("#timeline").value = "0";
  document.querySelector("#timeline-output").textContent = "No code loaded";
  document.querySelector("#checkpoint-status").textContent = "No checkpoint loaded";
  document.querySelector("#timeline-labels").replaceChildren();
  document.querySelector("#badges-earned").textContent = `0 of ${state.courseModel?.clos.length || 6}`;
  document.querySelector("#badges-mastered").textContent = "0";
  document.querySelector("#requirements-passed").textContent = `0 of ${state.courseModel?.majorAssessments.length || 5}`;
  document.querySelector("#badge-board-grid").replaceChildren();
  document.querySelector("#requirements-list").replaceChildren();
}
