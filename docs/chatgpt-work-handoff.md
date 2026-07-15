# ChatGPT Project Handoff

## Project Goal

This repo is the deployment target for the CU Boulder ASEN 3501 Experimental Methods course site. It serves two closely related outputs:

- `static/`: GitHub Pages version for student delivery, with no chatbot.
- `server/` + `server/course_content/`: FastAPI/Azure App Service version, with the chatbot enabled.

The content itself is generated upstream in another repo (`BOBPE-fwd_rev`) and committed here as built artifacts.

## Current Status

- The site has substantial generated content for `E1` and `E2`.
- `E3` is still a placeholder on the home page (`Content coming soon`).
- The repo appears clean at handoff time.
- GitHub Pages deployment is wired and triggers on pushes to `main` that change `static/**`.
- The chatbot-backed server is present and lightweight: it serves generated HTML, exposes `POST /api/chat`, and uses a simple local retrieval index plus a provider-based LLM router.
- There are concept quiz source markdown files in `concept_quizzes/`, and preview data is already exposed in `static/concept_quizzes_preview.json` and `server/course_content/concept_quizzes_preview.json`.

## Repo Structure And Important Files

### Top level

- [`README.md`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/README.md): deployment model, regeneration commands, local server instructions.
- [`planning-status-tracker.md`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/planning-status-tracker.md): planning-oriented status summary.
- [`.env.example`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/.env.example): expected environment variables for local server use.
- [`.github/workflows/deploy-pages.yml`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/.github/workflows/deploy-pages.yml): Pages deploy on push to `main` when `static/**` changes.

### Static student site

- [`static/index.html`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/static/index.html): generated course homepage; confirms current course shape and that `E3` is not built out yet.
- [`static/app.js`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/static/app.js): client-side behavior for quiz storage, results summaries, dashboard expand/collapse, and concept quiz previews.
- [`static/style.css`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/static/style.css): main styling for the static site.
- [`static/modules/`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/static/modules): generated learner-facing module pages.
- [`static/E1/`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/static/E1) and [`static/E2/`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/static/E2): lecture slide HTML and related generated assets.
- [`static/labs/`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/static/labs): lab simulations and assignment pages.
- [`static/admin/status-tracker.md`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/static/admin/status-tracker.md): repo-local content coverage/status snapshot.

### Server/chatbot path

- [`server/server.py`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/server/server.py): FastAPI app entrypoint; serves `server/course_content/` unless `FORWARD_STATIC_DIR` overrides it.
- [`server/requirements.txt`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/server/requirements.txt): minimal Python dependencies.
- [`server/chat/chat_api.py`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/server/chat/chat_api.py): `/api/chat` route, mode handling, retriever loading, fallback behavior.
- [`server/chat/retrieval.py`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/server/chat/retrieval.py): simple token/BM25-like chunk retrieval over `course_index.json`.
- [`server/chat/indexer.py`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/server/chat/indexer.py): builds the local retrieval index JSON.
- [`server/chat/llm_service.py`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/server/chat/llm_service.py): converts chat messages to a plain prompt and calls the shared inference router.
- [`server/inference/router.py`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/server/inference/router.py): `provider:model` dispatch.
- [`server/inference/provider.py`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/server/inference/provider.py): OpenAI, Gemini, DeepSeek, Kimi, and Ollama provider implementations.
- [`server/course_content/`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/server/course_content): chatbot-enabled generated site served by FastAPI.
- [`server/course_content/chat_widget.js`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/server/course_content/chat_widget.js): injected client chat widget with access-code gate and `/api/chat` calls.

### Content sources in this repo

- [`concept_quizzes/`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/concept_quizzes): weekly quiz source markdown currently present for weeks 1 through 10.
- [`static/normalized/`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/static/normalized) and [`server/course_content/normalized/`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/server/course_content/normalized): normalized text artifacts used for search/indexing context.

## Decisions Already Made

- This repo is a deployment/artifact repo, not the primary authoring repo.
- The project uses a two-channel deployment model rather than a single app:
  - `static/` for GitHub Pages and Canvas embedding.
  - `server/course_content/` plus FastAPI for chatbot-enabled demos or enhanced access.
- The static student-facing site intentionally excludes the chatbot.
- The chatbot is page-grounded by default and optionally supports course-wide retrieval (`page` vs `course_rag`).
- Retrieval is intentionally simple and file-based, using generated `course_index.json` rather than an external vector database.
- The chatbot access gate uses a semester access code embedded into generated frontend JS, so changing the code requires regeneration rather than just a runtime env change.
- Generated HTML is meant to be updated upstream in `BOBPE-fwd_rev`, then copied here by regeneration rather than hand-edited extensively in this repo.

## Pending Tasks

- Build out `E3` content; the current homepage still marks it as coming soon.
- Decide whether concept quizzes remain preview-only or become first-class student-facing graded/trackable experiences.
- Keep `static/` and `server/course_content/` in sync whenever upstream content is regenerated.
- If chatbot quality becomes important, improve retrieval and prompt behavior; current implementation is intentionally minimal.
- Validate the full local and deployed chatbot flow after any environment or model-provider changes.
- If course status tracking matters operationally, keep `planning-status-tracker.md` and `static/admin/status-tracker.md` aligned with actual content maturity.

## Known Bugs Or Risks

- There are no automated tests in this repo right now, so regressions are likely to be caught only by manual verification.
- This repo stores generated artifacts in two places (`static/` and `server/course_content/`), which creates drift risk if only one side is regenerated or committed.
- The chatbot falls back to page text when model access or retrieval is unavailable; that is safe-ish but can mask real backend problems if nobody checks logs.
- The access code is embedded in generated client JS for the chatbot-enabled build, so it should be treated as a soft gate rather than a strong secret.
- `course_id` and page context are embedded in page HTML; if generation changes those shapes, chat retrieval may quietly degrade.
- `E3` is not yet present, so any work assuming full-course completeness will be wrong.
- The OpenAI path includes a compatibility workaround for the installed OpenAI SDK and `httpx`; dependency upgrades could affect that behavior.

## Commands Used To Run, Test, And Build

### Local server

From the repo root:

```bash
cd server
cp ../.env.example .env
pip install -r requirements.txt
uvicorn server:app --reload --port 8003
```

Then open `http://localhost:8003`.

### Static preview

There is no dedicated local static dev server in the repo. A simple option is:

```bash
cd static
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

### Regenerate built content

Run these from the upstream `BOBPE-fwd_rev` repo root, not from this repo:

```bash
ASEN3501_ACCESS_CODE=... python Forward/generate_html_course.py \
  --input Forward/From_mds/ASEN3501_test_bundle \
  --output ../CU-Experimental-Methods-Site/static \
  --no-chatbot

ASEN3501_ACCESS_CODE=... python Forward/generate_html_course.py \
  --input Forward/From_mds/ASEN3501_test_bundle \
  --output ../CU-Experimental-Methods-Site/server/course_content \
  --chatbot
```

### Deployment

- GitHub Pages deploys automatically from `static/` on push to `main`.
- Azure/App Service deployment is expected to point at the `server/` app.

### Testing

- No formal test suite is present in this repo.
- Practical verification is manual: load static pages, load the FastAPI-served site, open the chat widget, and exercise both `page` and `course_rag` modes.

## Environment Assumptions

- Python environment is available locally for the FastAPI server.
- A `.env` file is expected in `server/` for local server runs.
- Supported model identifiers use `provider:model`, for example `openai:gpt-4o-mini` or `ollama:llama3.2`.
- Relevant env vars from `.env.example`:
  - `FORWARD_CHAT_MODEL`
  - `OPENAI_API_KEY`
  - `ASEN3501_ACCESS_CODE`
  - `APP_SECRET_KEY`
- Optional provider env vars also exist in code:
  - `GEMINI_API_KEY`
  - `DEEPSEEK_API_KEY`
  - `KIMI_API_KEY`
  - `OLLAMA_HOST`
- The local server defaults to serving `server/course_content/`, unless `FORWARD_STATIC_DIR` is set.

## What A Fresh Assistant Should Know

- Start by reading [`README.md`](/Users/hodgkinr/Documents/GitHub/CU-Experimental-Methods-Site/README.md) before making structural changes; it captures the intended deployment split.
- Do not assume this repo is the source of truth for authored course content. Most major content changes should probably happen upstream in `BOBPE-fwd_rev` and then be regenerated here.
- If a request is about student-facing pages only, inspect `static/` first.
- If a request is about the chatbot, inspect both `server/course_content/chat_widget.js` and the backend path through `server/chat/chat_api.py`.
- If search quality looks bad, check that `course_index.json` exists in the served content and that page context JSON is present in the generated HTML.
- If the user asks why content differs between the Pages site and the chatbot-enabled server, the most likely cause is out-of-sync generated outputs.
- If a machine change breaks local work, the most likely missing piece is local Python env plus `server/.env`.
- There were no in-progress code edits at handoff time; this handoff is for continuity, not to preserve a partially applied patch.
