from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from modules.loader import load_documents
from modules.chunking import split_documents
from modules.embeddings import create_embeddings
from modules.vector_store import create_vector_store

from config import GROQ_API_KEY

import os

def build_rag():

    documents = load_documents("data/documents/company_policy.pdf")
    chunks = split_documents(documents)
    embeddings = create_embeddings()
    vectorstore = create_vector_store(chunks, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k":3})
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.1-8b-instant",
        temperature=0
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

qa_system = build_rag()
def ask_question(question):
    response = qa_system.invoke({"query": question})
    answer = response["result"]
    return answer