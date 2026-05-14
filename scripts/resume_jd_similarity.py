import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# load model once (fast reuse)
model = SentenceTransformer("all-MiniLM-L6-v2")


# =========================================
# ✅ FUNCTION 1: USED BY YOUR APP (IMPORTANT)
# =========================================
def get_similarity_score(resume_text, jd_text):
    resume_embedding = model.encode(resume_text)
    jd_embedding = model.encode(jd_text)

    score = cosine_similarity([resume_embedding], [jd_embedding])[0][0]
    return float(score)


# =========================================
# OPTIONAL: KEEP YOUR OLD FUNCTION (NO BREAK)
# =========================================
def get_job_matches():
    resume_folder = "./data/resumes/processed/"
    jd_folder = "./data/job_descriptions/raw/"

    resume_texts = {}

    for file in os.listdir(resume_folder):
        if file.endswith(".txt"):
            with open(os.path.join(resume_folder, file), "r", encoding="utf-8") as f:
                resume_texts[file] = f.read()

    jd_texts = {}

    for file in os.listdir(jd_folder):
        if file.endswith(".txt"):
            with open(os.path.join(jd_folder, file), "r", encoding="utf-8") as f:
                jd_texts[file] = f.read()

    resume_name = list(resume_texts.keys())[0]
    resume_text = resume_texts[resume_name]

    resume_embedding = model.encode(resume_text)

    similarity_results = []

    for jd_name, jd_text in jd_texts.items():
        jd_embedding = model.encode(jd_text)
        score = cosine_similarity([resume_embedding], [jd_embedding])[0][0]
        similarity_results.append((jd_name, score))

    similarity_results.sort(key=lambda x: x[1], reverse=True)

    return similarity_results[:5]