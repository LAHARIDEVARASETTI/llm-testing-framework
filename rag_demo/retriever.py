from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load document
with open("documents/sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = text.split(". ")

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype("float32"))

def retrieve(query):
    q_embedding = model.encode([query])
    distances, indices = index.search(np.array(q_embedding).astype("float32"), k=2)

    retrieved = []
    for i in indices[0]:
        if i < len(chunks):
            retrieved.append(chunks[i])

    return "\n".join(retrieved)