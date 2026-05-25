from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from ingest import fetch_financial_news

def build_vectorstore():
    print("📰 Fetching articles...")
    articles = fetch_financial_news()
    
    # Convert articles to Documents
    docs = [
        Document(
            page_content=a["title"] + ". " + a["content"],
            metadata={"title": a["title"], "source": a["link"]}
        )
        for a in articles
    ]
    
    print("🧠 Creating embeddings (1-2 mins first time)...")
    
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_index")
    
    print("✅ Vector store built and saved!")
    return vectorstore

if __name__ == "__main__":
    build_vectorstore()