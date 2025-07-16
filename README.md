# 🧠 Local RAG with Mistral & Azure Integration

This project showcases a lightweight **Retrieval-Augmented Generation (RAG)** pipeline that runs entirely on your local machine using the **Mistral model via Ollama**, with optional support for Azure Blob Storage and Form Recognizer.

It extracts text from PDFs (either uploaded or pulled from Azure), breaks the content into chunks, embeds them with FAISS for fast semantic search, and uses the local Mistral model to answer user queries based on relevant context.

No cloud inference. No external LLM APIs. Just private, offline GenAI Q&A.
---

## 🔧 What’s Inside

- `app.py` – Orchestrates the RAG pipeline  
- `extract_text_from_pdf.py` – Parses PDF content  
- `build_faiss_index.py` – Creates FAISS index from chunks  
- `ask_mistral.py` – Sends queries to local Mistral via Ollama  
- `download_pdf_from_blob.py` – *(Optional)* Pulls PDFs from Azure Blob Storage  
- `tesla_10k_2024.pdf` – Sample PDF used in this example

---
