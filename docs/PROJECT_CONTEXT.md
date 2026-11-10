# Aya AI portfolio — project handoff (2026-11-10)

## Goal

Upgrade the existing public portfolio (https://aya-chihoub.github.io/) into a demonstrable AI/ML engineering project. It should help internship recruiters **experience** the owner's skills, not merely read a CV.

Primary feature: **Ask Aya AI**, a source-grounded chatbot answering questions about education, experience, skills and projects through retrieval-augmented generation (RAG).

Secondary feature (later): a small **interactive computer-vision demo** using a genuine, reproducible model from the owner's projects. The model and artifact availability have not been confirmed, so do not promise a particular demo until inspected.

## Repository and branch

- Repo: https://github.com/Aya-chihoub/aya-chihoub.github.io
- Production site: https://aya-chihoub.github.io/
- Default branch: `main` (live GitHub Pages portfolio).
- Working branch: `feature/ask-aya-ai`. **Keep work here until reviewed.**
- Frontend today: *single static `index.html` with inline HTML/CSS*, deployed via GitHub Pages. Do not assume a React project exists. Preserve the layout and visual identity.
- Current backend prototype: `backend/app/main.py`, `backend/knowledge/projects.json`, `backend/requirements.txt`. Read `backend/README.md`.

## What's already implemented (prototype; not yet tested locally)

1. A FastAPI application with `GET /health` and `POST /ask`.
2. Local CPU-capable SentenceTransformers embeddings (`all-MiniLM-L6-v2`).
3. In-memory cosine similarity retrieval (not FAISS yet) over a small JSON document collection.
4. Threshold filtering and a retrieval-only response with source links (not natural LLM generations).
5. Basic environment-configurable CORS, requirements and backend setup instructions.

**Important:** No LLM API call, frontend widget, persistent FAISS index, test suite, public backend deployment, rate limiting or computer-vision demo exists yet. Previous changes were committed through GitHub, not executed locally. Verify startup, paths, imports, API responses and embedding dependencies.

## Practical requirements and constraints

- Student portfolio for 2027 final-year internship applications in AI/ML Engineering, Data Science and Computer Vision; preference for applied engineering and Paris area.
- User knows Python, PyTorch, OpenCV, React, Node.js, information retrieval, TF-IDF/BM25+/SentenceTransformers, Git. They want code explained enough to discuss in interviews.
- Free/low-cost deployment is preferred. No personal GPU required. Generate the answer through a **hosted LLM API** (provider not chosen yet), and keep the API key server-side.
- A reliable, grounded system is more important than flashy UX. Build a tiny, working product first.
- Preserve live website and do not publish the prototype until end-to-end testing and explicit approval.
- Be conscious of quota abuse on a public site: server-side rate limiting, reasonable token budgets, timeout/error handling and safe fallbacks.
- Make answers explicitly tied to retrieved sources and refuse unsupported or personal/private questions.
- For production privacy: avoid logging visitors' questions unnecessarily; do not include personal or unpublished CV contents without consent.
- Do not represent inference scores as calibrated confidence unless justified.

## Source material to expand the knowledge base

Public site and projects should be authoritative:
- Portfolio: https://aya-chihoub.github.io/
- GitHub profile: https://github.com/Aya-chihoub
- IR engine: https://github.com/Aya-chihoub/Data-Science-IR-Retrieval-Engine
- Age-prediction CNN: https://github.com/Aya-chihoub/Age--prediction-using-deep-convolutional-neural-networks

Current seed facts in `projects.json` are intentionally incomplete and must be reviewed before public use. Ask for a current CV or project notes when necessary instead of guessing.

## Suggested next milestones

1. **Audit/verify** repository structure, backend app, Python compatibility, startup and sample API calls; add minimal automated tests (including unknown questions).
2. **Improve retrieval**: prepare curated source docs, chunk appropriately, assess retrieval with a small evaluation set; move to FAISS only if it adds value at this corpus size.
3. **Hosted LLM**: propose a free-tier-friendly provider (Gemini, Groq or another applicable hosted API), ask owner to configure a secret key locally, return clear answers with source references and explicit abstention; protect cost/quotas.
4. **UI integration**: add a lightweight accessible chat widget to existing `index.html`, with loading/error states and a mobile layout. Prefer vanilla JS unless a strong reason for a framework migration.
5. **Backend deployment**: recommend free/low-cost options, account for cold starts and embedding-model RAM limits. Set exact production CORS origin and document secrets.
6. **Interactive ML demo**: identify an existing lightweight image model/weights, build safe image upload + CPU inference endpoint, benchmark memory/latency, add a showcase page/section.
7. **Portfolio polish**: architecture diagram, metrics, user-facing limitations, tests, GitHub documentation and screenshots.

## What to do first in Codex

Inspect the branch and audit `backend/app/main.py`. Explain any likely bugs, run available checks and propose the smallest testable improvement. **Do not implement everything at once.** Ask before committing architecture changes or merging.
