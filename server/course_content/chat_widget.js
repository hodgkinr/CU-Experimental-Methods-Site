window.BOBPE_CHATBOT_CONFIG = {"enabled": true, "access_code": "Buff@lo", "require_name": true};
(function () {
  function getPageContext() {
    const node = document.getElementById("bobpe-page-context");
    if (!node) return null;
    try {
      return JSON.parse(node.textContent || "{}");
    } catch (error) {
      console.error("Invalid bobpe page context", error);
      return null;
    }
  }

  function escapeHtml(text) {
    return String(text || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/\"/g, "&quot;");
  }

  const pageContext = getPageContext();
  if (!pageContext) return;

  const chatbotConfig = (typeof window !== "undefined" && window.BOBPE_CHATBOT_CONFIG) || null;
  const requireGate = chatbotConfig && chatbotConfig.access_code;
  const requireName = chatbotConfig && chatbotConfig.require_name;
  const SESSION_KEY = "bobpe_chat_unlocked";

  function isUnlocked() {
    if (!requireGate) return true;
    try {
      const data = JSON.parse(sessionStorage.getItem(SESSION_KEY) || "{}");
      return data.unlocked === true;
    } catch (_) {
      return false;
    }
  }

  function getStoredName() {
    try {
      const data = JSON.parse(sessionStorage.getItem(SESSION_KEY) || "{}");
      return data.name || "";
    } catch (_) {
      return "";
    }
  }

  const root = document.createElement("aside");
  root.id = "bobpe-chat-root";

  const gateFormHtml = requireGate
    ? `<div id="bobpe-chat-gate">
        <div id="bobpe-gate-inner">
          <p id="bobpe-gate-heading"><strong>Course Tutor Access</strong></p>
          <p id="bobpe-gate-desc">Enter your details to unlock the course tutor.</p>
          <form id="bobpe-gate-form" autocomplete="off">
            ${requireName ? `<label for="bobpe-gate-name">Your name</label>
            <input id="bobpe-gate-name" type="text" placeholder="First name" autocomplete="off" required>` : ""}
            <label for="bobpe-gate-code">Access code</label>
            <input id="bobpe-gate-code" type="password" placeholder="Access code" autocomplete="off" required>
            <p id="bobpe-gate-error" hidden>Incorrect access code. Please try again.</p>
            <button type="submit">Unlock</button>
          </form>
        </div>
      </div>`
    : "";

  root.innerHTML = `
    <button id="bobpe-chat-toggle" type="button" aria-expanded="false">Course Tutor</button>
    <section id="bobpe-chat-panel" hidden>
      ${gateFormHtml}
      <div id="bobpe-chat-main">
        <div id="bobpe-chat-header">
          <div>
            <strong>Course Tutor</strong>
            <p>Ask about this page or search the course.</p>
          </div>
          <select id="bobpe-chat-mode" aria-label="Chat mode">
            <option value="page">Page tutor</option>
            <option value="course_rag">Course search</option>
          </select>
        </div>
        <div id="bobpe-chat-messages" aria-live="polite"></div>
        <div id="bobpe-chat-sources"></div>
        <form id="bobpe-chat-form">
          <input id="bobpe-chat-input" type="text" maxlength="1000" placeholder="Ask a question about this material">
          <button type="submit">Send</button>
        </form>
      </div>
    </section>
  `;
  document.body.appendChild(root);

  const toggle = document.getElementById("bobpe-chat-toggle");
  const panel = document.getElementById("bobpe-chat-panel");
  const chatMain = document.getElementById("bobpe-chat-main");
  const form = document.getElementById("bobpe-chat-form");
  const input = document.getElementById("bobpe-chat-input");
  const messagesNode = document.getElementById("bobpe-chat-messages");
  const sourcesNode = document.getElementById("bobpe-chat-sources");
  const modeNode = document.getElementById("bobpe-chat-mode");
  const gateNode = document.getElementById("bobpe-chat-gate");
  const gateForm = document.getElementById("bobpe-gate-form");
  const gateError = document.getElementById("bobpe-gate-error");

  const history = [];

  function showGateOrChat() {
    if (!requireGate || isUnlocked()) {
      if (gateNode) gateNode.hidden = true;
      chatMain.hidden = false;
    } else {
      chatMain.hidden = true;
      if (gateNode) gateNode.hidden = false;
    }
  }

  function addMessage(role, text, isPending) {
    const node = document.createElement("div");
    node.className = `bobpe-msg bobpe-${role}${isPending ? " is-pending" : ""}`;
    node.innerHTML = `<div class="bobpe-msg-role">${role === "user" ? "You" : "Tutor"}</div><div>${escapeHtml(text)}</div>`;
    messagesNode.appendChild(node);
    messagesNode.scrollTop = messagesNode.scrollHeight;
    return node;
  }

  function setIntro(userName) {
    const greeting = userName
      ? `Hi ${escapeHtml(userName)}! Page tutor stays grounded in this page. Course search looks across the generated course and returns links.`
      : "Page tutor stays grounded in this page. Course search looks across the generated course and returns links.";
    const node = document.createElement("div");
    node.className = "bobpe-msg bobpe-assistant";
    node.innerHTML = `<div class="bobpe-msg-role">Tutor</div><div>${greeting}</div>`;
    messagesNode.appendChild(node);
  }

  function renderSources(items) {
    sourcesNode.innerHTML = "";
    if (!items || !items.length) return;
    const heading = document.createElement("div");
    heading.className = "bobpe-sources-heading";
    heading.textContent = "Sources";
    sourcesNode.appendChild(heading);
    const list = document.createElement("ul");
    items.forEach((item) => {
      const entry = document.createElement("li");
      const link = document.createElement("a");
      link.href = item.url && item.url.startsWith("/") ? item.url : `/${String(item.url || "").replace(/^\/+/, "")}`;
      link.textContent = item.title || item.url;
      entry.appendChild(link);
      if (item.snippet) {
        const snippet = document.createElement("div");
        snippet.className = "bobpe-source-snippet";
        snippet.textContent = item.snippet;
        entry.appendChild(snippet);
      }
      list.appendChild(entry);
    });
    sourcesNode.appendChild(list);
  }

  async function sendMessage(text) {
    addMessage("user", text);
    const pending = addMessage("assistant", "Thinking…", true);
    renderSources([]);
    input.disabled = true;

    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          course_id: pageContext.course_id,
          current_page_url: pageContext.url,
          mode: modeNode.value,
          message: text,
          page_context: pageContext,
          history
        })
      });
      const data = await response.json();
      pending.remove();
      if (!response.ok) {
        addMessage("assistant", data.detail || "The chat request failed.");
        return;
      }
      addMessage("assistant", data.answer || "");
      renderSources(data.sources || []);
      history.push({ role: "user", content: text });
      history.push({ role: "assistant", content: data.answer || "" });
    } catch (error) {
      pending.remove();
      addMessage("assistant", error && error.message ? error.message : "Unable to reach the chat API.");
    } finally {
      input.disabled = false;
      input.focus();
    }
  }

  toggle.addEventListener("click", function () {
    panel.hidden = !panel.hidden;
    toggle.setAttribute("aria-expanded", String(!panel.hidden));
    if (!panel.hidden) {
      showGateOrChat();
      if (!requireGate || isUnlocked()) input.focus();
    }
  });

  if (gateForm) {
    gateForm.addEventListener("submit", function (event) {
      event.preventDefault();
      const codeInput = document.getElementById("bobpe-gate-code");
      const nameInput = document.getElementById("bobpe-gate-name");
      const enteredCode = codeInput ? codeInput.value.trim() : "";
      const enteredName = nameInput ? nameInput.value.trim() : "";
      if (enteredCode !== chatbotConfig.access_code) {
        if (gateError) gateError.hidden = false;
        codeInput.value = "";
        codeInput.focus();
        return;
      }
      const payload = { unlocked: true };
      if (enteredName) payload.name = enteredName;
      try {
        sessionStorage.setItem(SESSION_KEY, JSON.stringify(payload));
      } catch (_) {}
      showGateOrChat();
      setIntro(enteredName);
      input.focus();
    });
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    const text = input.value.trim();
    if (!text) return;
    input.value = "";
    sendMessage(text);
  });

  // Show intro immediately if already unlocked (persistent within session)
  if (!requireGate || isUnlocked()) {
    setIntro(getStoredName());
  }
})();
