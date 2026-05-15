const STORAGE_KEY = "forwardLmsQuizScores";

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

document.addEventListener("DOMContentLoaded", () => {
  setupQuizzes();
  renderModuleSummaries();
  renderResultsPage();
});
