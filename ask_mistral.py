from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import requests

# ✅ Load FAISS index
index = faiss.read_index("faiss_index.bin")

# ✅ Load document chunks
with open("chunks.txt", "r", encoding="utf-8") as f:
    chunks = f.read().split("\n---\n")

# ✅ Load sentence transformer model for embedding
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# ✅ Retrieve top-k relevant chunks using FAISS + embedding
def retrieve_context(question, top_k=3):
    q_embedding = model.encode([question])
    distances, indices = index.search(q_embedding, top_k)
    return [chunks[i] for i in indices[0]]

# ✅ Format retrieved chunks + question into a prompt
def generate_prompt(question, context_chunks):
    context = "\n\n".join(context_chunks)
    return f"""You are an AI assistant. Answer the following question based on the context below.

Context:
{context}

Question: {question}

Answer:"""

# ✅ Send prompt to Ollama-hosted Mistral model via HTTP API
def call_mistral(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['response']
    except requests.exceptions.RequestException as e:
        return f"❌ Request failed: {e}"
    except KeyError:
        return "❌ Unexpected response format."

# ✅ Entry point
if __name__ == "__main__":
    question = input("💬 Ask a financial question: ")
    context_chunks = retrieve_context(question)
    prompt = generate_prompt(question, context_chunks)
    print("\n📨 Prompt sent to Mistral:\n")
    print(prompt)
    print("\n🤖 Mistral's Answer:\n")
    print(call_mistral(prompt))
