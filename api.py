from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from agent import ask
import os

app = FastAPI(
    title="StockSense AI",
    description="Agentic RAG system for real-time financial research",
    version="1.0.0"
)

# Only mount static if folder exists
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    if os.path.exists("static/index.html"):
        return FileResponse("static/index.html")
    return JSONResponse({"status": "StockSense AI is running", "docs": "/docs"})

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