import streamlit as st
import pdfplumber
import os

from utils.llm import generate_llm_response
from scripts.resume_jd_similarity import get_similarity_score
from scripts.skill_gap_analysis import find_skill_gap


# ================================
# LOAD INTERVIEW DATA
# ================================
def load_interview_data():
    folder = "data/interview_experiences/raw"
    data = {}

    for file in os.listdir(folder):
        with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
            content = f.read()

            for line in content.split("\n"):
                if "Company:" in line:
                    company = line.split("Company:")[1].strip().lower()
                    data[company] = content
                    break

    return data


interview_data = load_interview_data()


# ================================
# IMPROVED COMPANY DETECTION
# ================================
def detect_company(user_input):
    user_input = user_input.lower()

    for company in interview_data.keys():
        if company in user_input:
            return company

    return None


# ================================
# EXTRACT COMPANY FROM JD NAME
# ================================
def extract_company_from_title(title):
    title = title.lower()

    for company in interview_data.keys():
        if company in title:
            return company

    return None


# ================================
# READ PDF
# ================================
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# ================================
# COMPANY NAME MAPPING
# ================================
company_names = {
    "jd_01.txt": "Software Development Engineer Intern Amazon",
    "jd_02.txt": "Software Engineer Intern Microsoft",
    "jd_03.txt": "Machine Learning Intern Google",
    "jd_04.txt": "Data Scientist Intern IBM",
    "jd_05.txt": "Software Engineer Intern META",
    "jd_06.txt": "Data Analyst Intern Deloitte",
    "jd_07.txt": "Associate Software Engineer Accenture",
    "jd_08.txt": "Software engineer TCS",
    "jd_09.txt": "Software Engineer Flipkart",
    "jd_10.txt": "Data Engineer Intern Walmart",
    "jd_11.txt": "Cloud Engineer Intern Oracle",
    "jd_12.txt": "Backend Developer intern Paytm",
    "jd_13.txt": "Software Engineer Intern Adobe",
    "jd_14.txt": "Data Analyst Capgemini",
    "jd_15.txt": "Machine Learning Engineer Intern NVIDIA",
    "jd_16.txt": "Software Engineer Infosys",
    "jd_17.txt": "AI engineer Intern OpenAI",
    "jd_18.txt": "Data Scientist Intern Goldman Sachs",
    "jd_19.txt": "Software Engineer Intern uber",
    "jd_20.txt": "Product Engineer Intern Zoho Corporation",
    "jd_21.txt": "Software Engineer Intern Google",
    "jd_22.txt": "Software Engineer Intern Apple",
    "jd_23.txt": "Data Engineer Intern Netflix",
    "jd_24.txt": "Software Engineer Intern Samsung",
    "jd_25.txt": "Devops Engineer Intern Atlasssian",
    "jd_26.txt": "Business Intelligence Analyst Intern Intel"
}


# ================================
# UI
# ================================
st.title("💼 AI Virtual Senior Mentor")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:

    st.success("Resume uploaded successfully")

    resume_text = extract_text_from_pdf(uploaded_file)

    # ================================
    # MATCHING
    # ================================
    jd_folder = "data/job_descriptions/raw"
    results = []

    for file in os.listdir(jd_folder):
        with open(os.path.join(jd_folder, file), "r", encoding="utf-8") as f:
            jd_text = f.read()

            score = get_similarity_score(resume_text, jd_text)
            results.append((file, score, jd_text))

    results.sort(key=lambda x: x[1], reverse=True)

    best_file, best_score, best_jd_text = results[0]
    best_company_title = company_names.get(best_file, best_file)

    st.subheader("🔥 Best Match")
    st.write(f"🏢 {best_company_title}")
    st.progress(best_score)
    st.write(f"{round(best_score*100,2)}% match")

    # ================================
    # TOP COMPANIES
    # ================================
    st.subheader("🏆 Top Companies")

    for file, score, _ in results[:3]:
        name = company_names.get(file, file)
        st.write(f"{name} → {round(score*100,2)}%")

    # ================================
    # SKILL GAP
    # ================================
    missing_skills = find_skill_gap(resume_text, best_jd_text)

    st.subheader("📉 Skill Gap")
    st.write(missing_skills)

    # ================================
    # CHAT
    # ================================
    st.subheader("💬 Ask your mentor")

    user_input = st.text_input("Ask anything about placements")

    if user_input:
        

        # 1️⃣ detect company from user input
        user_company = detect_company(user_input)

        # 2️⃣ fallback → best match company
        if not user_company:
            user_company = extract_company_from_title(best_company_title)

        interview_context = interview_data.get(user_company, "No interview data found.")

        # ================================
        # CONTEXT (🔥 MOST IMPORTANT)
        # ================================
        context = f"""
Target Company: {user_company}

Best Match Role: {best_company_title}
Match Score: {round(best_score*100,2)}%

Resume:
{resume_text[:800]}

Missing Skills:
{missing_skills}

Interview Experience:
{interview_context}
"""

        answer = generate_llm_response(context, user_input)

        st.subheader("🤖 Mentor Response")
        st.write(answer)