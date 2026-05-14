import os
import pandas as pd


skills_list = [
    "python","java","c++","sql","machine learning","deep learning",
    "data structures","algorithms","system design",
    "aws","docker","kubernetes","html","css","javascript",
    "react","node","git","linux","pandas","numpy","tensorflow","pytorch"
]

resume_folder = "./data/resumes/processed/"

resume_skills = {}

for file in os.listdir(resume_folder):

    if file.endswith(".txt"):

        with open(resume_folder + file, "r", encoding="utf-8") as f:
            text = f.read().lower()

        found_skills = []

        for skill in skills_list:
            if skill in text:
                found_skills.append(skill)

        resume_skills[file] = found_skills


for resume, skills in resume_skills.items():
    print(resume, "->", skills)



data = []

for resume, skills in resume_skills.items():
    data.append({
        "resume": resume,
        "skills": ", ".join(skills)
    })

df = pd.DataFrame(data)

df.to_csv("./data/resume_skills_dataset.csv", index=False)

print("Resume skills dataset saved successfully")