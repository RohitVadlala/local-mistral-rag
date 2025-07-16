import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import requests

# ✅ Load FAISS index and document chunks
index = faiss.read_index("faiss_index.bin")
with open("chunks.txt", "r", encoding="utf-8") as f:
    chunks = f.read().split("\n---\n")

# ✅ Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# ✅ Retrieve top-k relevant chunks
def retrieve_context(question, top_k=3):
    q_embedding = model.encode([question])
    distances, indices = index.search(q_embedding, top_k)
    return [chunks[i] for i in indices[0]]

# ✅ Build prompt from context
def generate_prompt(question, context_chunks):
    context = "\n\n".join(context_chunks)
    return f"""You are an AI assistant. Answer the following question based on the context below.

Context:
{context}

Question: {question}

Answer:"""

# ✅ Send prompt to Ollama-hosted Mistral model
def call_mistral(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    try:
        print("📤 Sending prompt to Ollama...")
        response = requests.post(url, json=payload, timeout=300)
        response.raise_for_status()
        result = response.json()
        return result["response"]
    except requests.exceptions.RequestException as e:
        return f"❌ Request failed: {e}"
    except KeyError:
        return "❌ Invalid response format."

# ✅ Streamlit UI
st.set_page_config(page_title="📄 Local PDF Q&A with Mistral", layout="centered")
st.title("📄 PDF Q&A Assistant (powered by Local Mistral)")

question = st.text_input("💬 Ask your question about the PDF content")

if question:
    with st.spinner("🔍 Retrieving relevant context and generating answer..."):
        context_chunks = retrieve_context(question)
        prompt = generate_prompt(question, context_chunks)
        answer = call_mistral(prompt)

    st.markdown("### 🤖 Mistral's Answer")
    st.success(answer)
