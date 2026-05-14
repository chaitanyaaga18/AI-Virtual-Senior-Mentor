import re

# simple skill extraction (you can upgrade later)
def extract_skills(text):
    text = text.lower()

    skills = [
        "python", "java", "c++", "sql", "machine learning",
        "data structures", "algorithms", "html", "css",
        "javascript", "react", "node", "aws", "docker"
    ]

    found = set()

    for skill in skills:
        if skill in text:
            found.add(skill)

    return found


# =========================================
# ✅ FUNCTION REQUIRED BY app.py
# =========================================
def find_skill_gap(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    missing = jd_skills - resume_skills

    return list(missing)