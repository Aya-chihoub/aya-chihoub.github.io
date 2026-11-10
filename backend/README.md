# Ask Aya AI — Phase 1: retrieval backend

This is the first incremental backend for the portfolio assistant. It **does not yet call an LLM**: `POST /ask` performs semantic retrieval and returns grounded excerpts with source links. This avoids presenting generated answers before the retrieval layer is tested. A later phase will add an LLM with explicit grounding and evaluation.

## Run locally

Use Python 3.11 or 3.12, then from the repository root:

```bash
cd backend
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The first launch downloads the embedding model. Open `http://127.0.0.1:8000/docs` for interactive API documentation.

## Try it

```bash
curl -X POST http://127.0.0.1:8000/ask -H "Content-Type: application/json" -d '{"question":"What information retrieval projects has Aya built?"}'
```

## Architecture

- `knowledge/projects.json`: small, editable seed knowledge base; verify and expand it with CV/project documents before launch.
- `app/main.py`: startup-time embeddings, cosine-similarity retrieval, threshold filtering, API routes and source links.
- `CORS_ORIGINS`: comma-separated permitted frontend origins; add the production portfolio domain when deploying.

## Next steps

1. Test retrieval quality with a set of relevant and unanswerable questions.
2. Add chunked CV/project documentation and a persistent vector index (FAISS) as the corpus grows.
3. Add a server-side LLM API with strict source grounding and usage limits.
4. Integrate a chat widget into the existing static `index.html`.

Never place LLM API keys in frontend code or commit them to Git.
