from sentence_transformers import SentenceTransformer
import faiss
import os

# Load the extracted text file
with open("extracted_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Simple chunking logic
def chunk_text(text, chunk_size=500, overlap=100):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

chunks = chunk_text(text)

# Load a financial-domain embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Create embeddings
embeddings = model.encode(chunks)

# Create a FAISS index (using L2 distance)
dimension = embeddings[0].shape[0]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save FAISS index and chunks
faiss.write_index(index, "faiss_index.bin")

with open("chunks.txt", "w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write(chunk + "\n---\n")

print(f"✅ {len(chunks)} chunks embedded and FAISS index saved.")