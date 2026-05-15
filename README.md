# CU-Experimental-Methods-Site

Deployment repo for the ASEN 3501 course site. Content is pre-generated locally
from [BOBPE-fwd_rev](https://github.com/hodgkinr/BOBPE-fwd_rev) and committed
here. GitHub Pages and Azure App Service read from this repo directly.

For full architecture context see
[DEPLOYMENT_NOTES.md](https://github.com/hodgkinr/BOBPE-fwd_rev/blob/main/Forward/DEPLOYMENT_NOTES.md)
in BOBPE-fwd_rev.

---

## Two-Channel Deployment Model

| Channel | Source folder | Chatbot | Use case |
|---------|--------------|---------|----------|
| GitHub Pages | `static/` | Disabled | Canvas iframe — all students |
| Azure App Service | `server/` + `server/course_content/` | Enabled | Demos, office hours, enhanced access |

GitHub Pages serves `static/` automatically on every push to `main` (see
`.github/workflows/deploy-pages.yml`). Azure is deployed manually or via Azure
Deployment Center pointed at the `server/` folder of this repo.

---

## Regenerating Content

Run both commands from the `BOBPE-fwd_rev` root directory. Set
`ASEN3501_ACCESS_CODE` to the current semester access code.

```bash
# GitHub Pages target — no chatbot widget in any HTML
ASEN3501_ACCESS_CODE=Buff@lo python Forward/generate_html_course.py \
  --input Forward/From_mds/ASEN3501_test_bundle \
  --output ../CU-Experimental-Methods-Site/static \
  --no-chatbot

# Azure target — chatbot widget included in every HTML file
ASEN3501_ACCESS_CODE=Buff@lo python Forward/generate_html_course.py \
  --input Forward/From_mds/ASEN3501_test_bundle \
  --output ../CU-Experimental-Methods-Site/server/course_content \
  --chatbot
```

After running, commit both `static/` and `server/course_content/` to `main`.
Pushing `main` triggers the GitHub Pages deploy automatically.

---

## Running the Azure Server Locally

```bash
cd server/
cp ../.env.example .env       # then fill in real values
pip install -r requirements.txt
uvicorn server:app --reload --port 8003
```

Open `http://localhost:8003` — serves the chatbot-enabled course content.

---

## Repo Structure

```
CU-Experimental-Methods-Site/
├── static/                   ← GitHub Pages output (no chatbot)
├── server/
│   ├── server.py             ← FastAPI app
│   ├── requirements.txt
│   ├── chat/                 ← chat API logic (from BOBPE-fwd_rev)
│   ├── inference/            ← shared LLM router (from BOBPE-fwd_rev/shared)
│   └── course_content/       ← Azure-served output (with chatbot)
└── .github/workflows/
    └── deploy-pages.yml      ← auto-deploys static/ to GitHub Pages
```

---

## Environment Variables

Copy `.env.example` to `server/.env` and fill in values before running locally.
On Azure, set these as App Settings (not committed to this repo):

| Variable | Description |
|----------|-------------|
| `FORWARD_CHAT_MODEL` | LLM provider and model, e.g. `openai:gpt-4o-mini` |
| `OPENAI_API_KEY` | API key for the chosen provider |
| `ASEN3501_ACCESS_CODE` | Access code baked into chatbot JS at build time |
| `APP_SECRET_KEY` | Session secret for the FastAPI app |

---

## Canvas Embedding

Paste into a Canvas Page using the HTML editor:

```html
<!-- Static (GitHub Pages) — recommended for course delivery -->
<iframe
  title="ASEN 3501 Course Site"
  src="https://hodgkinr.github.io/CU-Experimental-Methods-Site/"
  width="100%" height="700px" style="border: none;" loading="lazy">
</iframe>
```

Verify CU Canvas allows iframes before building toward this.
