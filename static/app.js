const STORAGE_KEY = "forwardLmsQuizScores";
let conceptQuizPreviewCache = null;

function loadScores() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
  } catch (_error) {
    return {};
  }
}

function saveScores(scores) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(scores));
}

function renderModuleSummaries() {
  const scores = loadScores();
  document.querySelectorAll("[data-module-id].module-quiz-summary").forEach((node) => {
    const moduleId = node.dataset.moduleId;
    const entries = Object.values(scores).filter((entry) => entry.moduleId === moduleId);
    if (!entries.length) {
      node.innerHTML = "<p class=\"muted\">No quiz attempts recorded yet for this module.</p>";
      return;
    }
    const correct = entries.reduce((sum, entry) => sum + entry.correct, 0);
    const total = entries.reduce((sum, entry) => sum + entry.total, 0);
    node.innerHTML = `<p><strong>Quiz progress:</strong> ${correct}/${total} correct across ${entries.length} quiz page(s).</p>`;
  });
}

function renderResultsPage() {
  const target = document.querySelector("[data-results-root]");
  if (!target) return;
  const scores = loadScores();
  const entries = Object.entries(scores);
  if (!entries.length) {
    target.innerHTML = "<p class=\"muted\">No quiz scores stored yet. Complete a quiz page to populate this summary.</p>";
    return;
  }
  const rows = entries.map(([quizId, entry]) => `
    <tr>
      <td>${quizId}</td>
      <td>${entry.moduleId}</td>
      <td>${entry.correct}/${entry.total}</td>
    </tr>
  `).join("");
  target.innerHTML = `
    <table>
      <thead>
        <tr>
          <th>Quiz</th>
          <th>Module</th>
          <th>Score</th>
        </tr>
      </thead>
      <tbody>${rows}</tbody>
    </table>
  `;
}

function enableLockedNextButton(form) {
  const nextButton = document.querySelector(".next-button[data-requires-quiz]");
  if (!nextButton) return;
  nextButton.classList.remove("is-disabled");
  nextButton.removeAttribute("aria-disabled");
}

function setupQuizzes() {
  document.querySelectorAll(".quiz-form").forEach((form) => {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const questions = Array.from(form.querySelectorAll(".quiz-question"));
      let correct = 0;
      questions.forEach((question) => {
        question.classList.remove("is-correct", "is-incorrect");
        const selected = question.querySelector("input[type=radio]:checked");
        const feedbackNode = question.querySelector(".quiz-feedback");
        if (!selected) {
          feedbackNode.hidden = false;
          feedbackNode.textContent = "Select an answer to see feedback.";
          question.classList.add("is-incorrect");
          return;
        }
        const isCorrect = selected.dataset.correct === "true";
        if (isCorrect) correct += 1;
        question.classList.add(isCorrect ? "is-correct" : "is-incorrect");
        feedbackNode.hidden = false;
        feedbackNode.innerHTML = `${isCorrect ? "<strong>Correct.</strong> " : "<strong>Not quite.</strong> "}${selected.dataset.feedback || ""}`;
      });

      const total = questions.length;
      const scoreNode = form.querySelector(".quiz-score");
      if (scoreNode) {
        scoreNode.textContent = `Score: ${correct}/${total}`;
      }

      const scores = loadScores();
      scores[form.dataset.quizId] = {
        moduleId: form.dataset.moduleId,
        correct,
        total,
      };
      saveScores(scores);
      enableLockedNextButton(form);
      renderModuleSummaries();
      renderResultsPage();
    });
  });
}

function setupDashboard() {
  document.querySelectorAll(".dash-week-cell").forEach((cell) => {
    const header = cell.querySelector(".dash-week-header");
    const detail = cell.querySelector(".dash-week-detail");
    if (!header || !detail) return;
    header.addEventListener("click", () => {
      const isOpen = !detail.hidden;
      detail.hidden = isOpen;
      header.setAttribute("aria-expanded", String(!isOpen));
      cell.classList.toggle("is-active", !isOpen);
    });
  });
}

function getAssetBaseUrl() {
  const appScript = document.querySelector('script[src$="app.js"]');
  if (!appScript) return new URL("./", window.location.href);
  return new URL("./", appScript.src);
}

function getPageContext() {
  const node = document.getElementById("bobpe-page-context");
  if (!node) return null;
  try {
    return JSON.parse(node.textContent || "{}");
  } catch (_error) {
    return null;
  }
}

async function loadConceptQuizPreviews() {
  if (conceptQuizPreviewCache) return conceptQuizPreviewCache;
  const response = await fetch(new URL("concept_quizzes_preview.json", getAssetBaseUrl()));
  if (!response.ok) {
    throw new Error(`Failed to load concept quiz previews: ${response.status}`);
  }
  conceptQuizPreviewCache = await response.json();
  return conceptQuizPreviewCache;
}

function createQuestionCard(question, index) {
  const item = document.createElement("li");
  item.className = "concept-preview-item";

  const header = document.createElement("div");
  header.className = "concept-preview-item-header";

  const number = document.createElement("span");
  number.className = "concept-preview-number";
  number.textContent = `Q${index + 1}`;

  const badge = document.createElement("span");
  badge.className = "concept-preview-badge";
  badge.textContent = question.type === "multiple_choice" ? "Multiple Choice" : "Open Response";

  header.append(number, badge);

  const prompt = document.createElement("p");
  prompt.className = "concept-preview-prompt";
  prompt.textContent = question.prompt;

  item.append(header, prompt);

  if (question.options?.length) {
    const options = document.createElement("ol");
    options.className = "concept-preview-options";
    options.type = "A";
    question.options.forEach((optionText) => {
      const option = document.createElement("li");
      option.textContent = optionText;
      options.appendChild(option);
    });
    item.appendChild(options);
  }

  return item;
}

function renderConceptQuizPreview(preview) {
  const pageShell = document.querySelector(".page-shell");
  const moduleGrid = document.querySelector(".module-overview-grid");
  const sequenceCard = document.querySelector(".module-page-list")?.closest(".content-card");
  if (!pageShell || !moduleGrid || !sequenceCard) return;

  const existing = document.querySelector("[data-concept-preview]");
  if (existing) existing.remove();

  const section = document.createElement("section");
  section.className = "content-card concept-preview-card";
  section.dataset.conceptPreview = "true";

  const title = document.createElement("h2");
  title.textContent = "Questions to Think Through Before Class";

  const intro = document.createElement("p");
  intro.className = "concept-preview-intro";
  intro.textContent = "These are possible in-class concept questions for this week. They are here to help you think ahead; answers are intentionally hidden.";

  const focus = document.createElement("p");
  focus.className = "concept-preview-focus";
  focus.innerHTML = `<strong>${preview.week_label} focus:</strong> ${preview.week_focus}`;

  const list = document.createElement("ol");
  list.className = "concept-preview-list";
  preview.questions.forEach((question, index) => {
    list.appendChild(createQuestionCard(question, index));
  });

  section.append(title, intro, focus, list);
  pageShell.insertBefore(section, sequenceCard);

  const metaList = document.querySelector(".meta-list");
  if (metaList && !metaList.querySelector("[data-concept-count]")) {
    const row = document.createElement("div");
    row.dataset.conceptCount = "true";
    row.innerHTML = `<dt>Concept questions</dt><dd>${preview.questions.length}</dd>`;
    metaList.appendChild(row);
  }
}

async function setupConceptQuizPreviews() {
  const context = getPageContext();
  if (!context || context.source_type !== "module_index" || !context.module_id) return;
  try {
    const previews = await loadConceptQuizPreviews();
    const preview = previews[context.module_id];
    if (!preview) return;
    renderConceptQuizPreview(preview);
  } catch (error) {
    console.error(error);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  setupQuizzes();
  renderModuleSummaries();
  renderResultsPage();
  setupDashboard();
  setupConceptQuizPreviews();
});
