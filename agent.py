from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def load_agent():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.load_local(
        "faiss_index", 
        embeddings,
        allow_dangerous_deserialization=True
    )
    
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"
    )
    
    return vectorstore, llm

def ask(question: str):
    vectorstore, llm = load_agent()
    
    docs = vectorstore.similarity_search(question, k=3)
    
    context = "\n\n".join([d.page_content for d in docs])
    sources = [d.metadata["title"] for d in docs]
    
    prompt = f"""You are a financial research assistant.
Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't have enough data on this."

Context:
{context}

Question: {question}

Answer:"""
    
    response = llm.invoke(prompt)
    
    return {
        "answer": response.content,
        "sources": sources
    }

if __name__ == "__main__":
    result = ask("What is happening with Apple stock?")
    print("💬 Answer:", result["answer"])
    print("📰 Sources:", result["sources"])