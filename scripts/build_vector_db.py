import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
doc_names = []


jd_folder = "./data/job_descriptions/raw/"

for file in os.listdir(jd_folder):

    if file.endswith(".txt"):

        with open(jd_folder + file,"r",encoding="utf-8") as f:

            text = f.read()

        documents.append(text)
        doc_names.append(file)


embeddings = model.encode(documents)


dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


faiss.write_index(index,"vector_index.faiss")


with open("doc_mapping.pkl","wb") as f:
    pickle.dump(doc_names,f)

print("Vector database created successfully")