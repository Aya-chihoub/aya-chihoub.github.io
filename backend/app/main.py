"""Minimal retrieval API for the Ask Aya AI portfolio feature."""
from contextlib import asynccontextmanager
from pathlib import Path
import json
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sentence_transformers import SentenceTransformer, util

DATA_PATH = Path(__file__).resolve().parents[1] / "knowledge" / "projects.json"
MODEL_NAME = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=500)

class Source(BaseModel):
    title: str
    url: str
    score: float

class AskResponse(BaseModel):
    answer: str
    sources: list[Source]
    mode: str = "retrieval_only"

@asynccontextmanager
async def lifespan(app: FastAPI):
    documents = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    model = SentenceTransformer(MODEL_NAME)
    vectors = model.encode([d["text"] for d in documents], convert_to_tensor=True, normalize_embeddings=True)
    app.state.documents = documents
    app.state.model = model
    app.state.vectors = vectors
    yield

app = FastAPI(title="Ask Aya AI", version="0.1.0", lifespan=lifespan)
origins = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "http://localhost:5173,http://localhost:8000").split(",") if origin.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["GET", "POST"], allow_headers=["Content-Type"])

@app.get("/health")
def health():
    return {"status": "ok", "documents": len(app.state.documents)}

@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest):
    query_vector = app.state.model.encode(payload.question, convert_to_tensor=True, normalize_embeddings=True)
    scores = util.cos_sim(query_vector, app.state.vectors)[0]
    top = scores.topk(k=min(3, len(app.state.documents)))
    matches = [(app.state.documents[i], float(score)) for score, i in zip(top.values.tolist(), top.indices.tolist()) if score >= 0.30]
    if not matches:
        return AskResponse(answer="I don't have enough information in my portfolio documents to answer that yet.", sources=[])
    sources = [Source(title=doc["title"], url=doc["url"], score=round(score, 3)) for doc, score in matches]
    summary = " ".join(doc["text"] for doc, _ in matches[:2])
    return AskResponse(answer=summary, sources=sources)
