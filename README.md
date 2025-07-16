# 🧠 Local Mistral RAG

This project demonstrates a simple **Retrieval-Augmented Generation (RAG)** pipeline that runs entirely locally using the **Mistral model via Ollama**.

It extracts content from a PDF, breaks it into chunks, builds a FAISS index for semantic search, and uses Mistral to answer questions based on relevant content. No external APIs — everything runs on your machine.

---

## 🔧 What’s Inside

- `app.py` – Orchestrates the RAG pipeline  
- `extract_text_from_pdf.py` – Parses PDF content  
- `build_faiss_index.py` – Creates FAISS index from chunks  
- `ask_mistral.py` – Sends queries to local Mistral via Ollama  
- `download_pdf_from_blob.py` – *(Optional)* Pulls PDFs from Azure Blob Storage  
- `tesla_10k_2024.pdf` – Sample PDF used in this example

---
