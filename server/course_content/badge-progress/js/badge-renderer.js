import { PROTOTYPE_STATE_LEVELS } from "./course-config.js";

export function getBadgeStatus(clo, subCLOStates) {
  const states = clo.subCLOs.map((sub) => subCLOStates[sub.id] ?? 0);
  const earned = states.every((state) => state >= 2);
  const masteryCount = states.filter((state) => state === 3).length;
  const total = states.length;
  const mastered = earned && masteryCount === total;
  const partial = earned && masteryCount > 0 && !mastered;

  return {
    earned,
    mastered,
    partial,
    masteryCount,
    total,
    stateLabel: mastered ? "Mastery" : earned ? "Proficient Badge Earned" : "Developing / Not Yet Earned",
    ratio: total ? masteryCount / total : 0
  };
}

export function renderSummary({ courseModel, event }) {
  const statuses = courseModel.clos.map((clo) => getBadgeStatus(clo, event.subCLOStates));
  const earned = statuses.filter((status) => status.earned).length;
  const mastered = statuses.filter((status) => status.mastered).length;
  const passed = courseModel.majorAssessments.filter((assessment) => event.majorAssessmentStates[assessment.id] === 1).length;

  document.querySelector("#badges-earned").textContent = `${earned} of ${courseModel.clos.length}`;
  document.querySelector("#badges-mastered").textContent = String(mastered);
  document.querySelector("#requirements-passed").textContent = `${passed} of ${courseModel.majorAssessments.length}`;
}

export function renderBadges({ courseModel, event, previousEvent }) {
  const grid = document.querySelector("#badge-board-grid");
  const template = document.querySelector("#badge-template");
  grid.replaceChildren();

  courseModel.clos.forEach((clo) => {
    const status = getBadgeStatus(clo, event.subCLOStates);
    const previousStatus = previousEvent ? getBadgeStatus(clo, previousEvent.subCLOStates) : null;
    const card = template.content.firstElementChild.cloneNode(true);
    const button = card.querySelector(".badge-toggle");
    const img = card.querySelector("img");
    const panel = card.querySelector(".subclo-panel");

    card.classList.toggle("is-earned", status.earned);
    card.classList.toggle("is-partial", status.partial);
    card.classList.toggle("is-mastery", status.mastered);
    card.style.setProperty("--mastery-ratio", status.ratio.toFixed(3));

    if (previousStatus && (previousStatus.stateLabel !== status.stateLabel || previousStatus.masteryCount !== status.masteryCount)) {
      card.classList.add("updated");
      window.setTimeout(() => card.classList.remove("updated"), 650);
    }

    img.src = clo.badgeImage;
    img.alt = `${clo.id} badge artwork`;
    card.querySelector(".badge-kicker").textContent = clo.id.replace("CLO", "CLO ");
    card.querySelector(".badge-title").textContent = clo.title;
    card.querySelector(".badge-status").textContent = status.stateLabel;
    card.querySelector(".badge-mastery").textContent = `Mastery: ${status.masteryCount} of ${status.total}`;

    const panelId = `details-${clo.id}`;
    panel.id = panelId;
    button.setAttribute("aria-expanded", "false");
    button.setAttribute("aria-controls", panelId);
    button.setAttribute("aria-label", `${clo.id}, ${clo.title}, ${status.stateLabel}. Mastery ${status.masteryCount} of ${status.total}. Toggle sub-CLO details.`);
    button.addEventListener("click", () => {
      const expanded = button.getAttribute("aria-expanded") === "true";
      button.setAttribute("aria-expanded", String(!expanded));
      panel.hidden = expanded;
    });

    panel.innerHTML = renderSubCLOPanel(clo, event.subCLOStates, status);
    grid.append(card);
  });
}

export function renderRequirements({ courseModel, event }) {
  const list = document.querySelector("#requirements-list");
  list.replaceChildren();

  courseModel.majorAssessments.forEach((assessment) => {
    const passed = event.majorAssessmentStates[assessment.id] === 1;
    const item = document.createElement("div");
    item.className = "requirement-item";
    item.classList.toggle("is-passed", passed);
    item.innerHTML = `
      <span class="requirement-name">${escapeHtml(assessment.label)}</span>
      <span class="requirement-state">${passed ? "Passed" : "Not Yet Passed"}</span>
    `;
    list.append(item);
  });
}

function renderSubCLOPanel(clo, subCLOStates, status) {
  const rows = clo.subCLOs.map((sub) => {
    const state = subCLOStates[sub.id] ?? 0;
    const stateMeta = PROTOTYPE_STATE_LEVELS[state];
    return `
      <li>
        <span class="subclo-name">
          <span class="subclo-id">${escapeHtml(sub.id)}</span>
          ${escapeHtml(sub.title)}
        </span>
        <span class="state-token state-${state}">${escapeHtml(stateMeta.label)}</span>
      </li>
    `;
  }).join("");

  return `
    <strong>${escapeHtml(clo.id)} - ${escapeHtml(clo.title)}</strong>
    <p>${escapeHtml(clo.statement)}</p>
    <p><strong>Badge status:</strong> ${escapeHtml(status.stateLabel)}. <strong>Mastery progress:</strong> ${status.masteryCount} of ${status.total}.</p>
    <ul class="subclo-list">${rows}</ul>
  `;
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    "\"": "&quot;",
    "'": "&#39;"
  })[char]);
}
