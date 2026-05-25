# StockSense AI 🚀

An end-to-end Agentic RAG system for real-time financial research and stock Q&A — built to production standards.

## What it does
- Ingests live financial news automatically
- Embeds documents using HuggingFace sentence-transformers
- Indexes them in FAISS for fast semantic search
- Uses a LangChain agent to retrieve and generate grounded answers
- Returns cited, hallucination-free responses via FastAPI REST API

## Tech Stack
Python · LangChain · Groq (Llama 3.3) · FAISS · HuggingFace · FastAPI · Prompt Engineering

## How to Run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your GROQ_API_KEY in .env file
4. Run: `python vectorstore.py`
5. Run: `python -m uvicorn api:app --reload`
6. Open: `http://127.0.0.1:8000/docs`

## Project Structure
- `ingest.py` — Live financial news ingestion pipeline
- `vectorstore.py` — FAISS vector store builder
- `agent.py` — LangChain RAG agent
- `api.py` — FastAPI REST service