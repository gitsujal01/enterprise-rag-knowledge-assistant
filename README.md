# 🏢 Enterprise RAG Knowledge Assistant

## 🚀 Overview
This project is an **Enterprise-grade Retrieval-Augmented Generation (RAG) Assistant** that enables employees to query internal company documents (PDFs, reports, manuals, policies) using AI. It combines **semantic search** with **generative AI**, delivering accurate, citation-backed answers in a chat interface.

[Live Demo](https://enterprise-rag-knowlege-assistant.onrender.com/)

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
- **Vector Database:** FAISS / ChromaDB  
- **Embeddings:** OpenAI / Groq  
- **LLM Model:** Llama 3.1 (via Groq)  
- **Database:** SQLite / PostgreSQL (optional)  
- **Deployment:** Render / HuggingFace  

---

## 📂 Features
- Multi-document upload and management  
- PDF text extraction and chunking  
- Embedding generation & vector store creation  
- Semantic search + RAG-based question answering  
- Chat interface with **conversation history**  
- Role-based authentication (Admin / User)  
- Admin dashboard for document management and analytics  
- Cloud-ready deployment with environment variables support  

---

## ⚙️ Setup
```bash
# Clone the repository
git clone https://github.com/gitsujal01/enterprise-rag-knowlege-assistant.git
cd enterprise-rag-knowlege-assistant

# Install dependencies
pip install -r requirements.txt

# Create a .env file
echo "GROQ_API_KEY=your_api_key_here" > .env

# Run the Streamlit app
streamlit run app.py --server.port $PORT --server.headless true
