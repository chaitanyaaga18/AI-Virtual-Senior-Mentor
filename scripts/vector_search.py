import faiss
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vector_index.faiss")

with open("doc_mapping.pkl","rb") as f:
    doc_names = pickle.load(f)

def search_documents(query):

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding,3)

    results = []

    for i in indices[0]:
        results.append(doc_names[i])

    return results