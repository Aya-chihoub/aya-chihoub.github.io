# Development guidance for Codex — Aya AI portfolio

Read `docs/PROJECT_CONTEXT.md` and `backend/README.md` before editing.

- Work on branch `feature/ask-aya-ai`. Do not merge to `main` or publish incomplete features without the owner's approval.
- This repository hosts the *existing* live portfolio at https://aya-chihoub.github.io/. Preserve its style, content, navigation, accessibility and responsive behavior. The site is a single static `index.html`; do not assume React is already installed.
- Build incrementally: first validate the backend, then add the hosted LLM, then a small frontend chat UI, and only later the computer-vision demo.
- Explain architectural decisions and significant code changes in straightforward language so the owner can present the project in ML/AI engineering interviews.
- Do not invent education, employment or project claims. Prefer sources from the site and user-verified CV/project documentation. Add explicit citations to answers; if no support exists, say so.
- Never put API keys in the static site or commit them. Add `.env.example` with placeholders if configuration is needed; keep real `.env` ignored. Restrict CORS origins, apply request validation and basic abuse protection before public deployment.
- Keep recurring hosted inference expenses low. The owner has no GPU budget; CPU embeddings and a hosted LLM API are preferred.
- Run available tests and clearly state what was tested and what is unverified. Do not claim the current retrieval prototype is a complete RAG or LLM-backed application.
- Before major dependencies, framework migration, hosting choice or deployment changes, explain tradeoffs and request a decision.
