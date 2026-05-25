from fastapi import FastAPI
from pydantic import BaseModel
from agent import ask

app = FastAPI(
    title="StockSense AI",
    description="Agentic RAG system for real-time financial research",
    version="1.0.0"
)

class Query(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "running", "system": "StockSense AI"}

@app.post("/ask")
def ask_question(query: Query):
    result = ask(query.question)
    return {
        "question": query.question,
        "answer": result["answer"],
        "sources": result["sources"],
        "grounded": True
    }