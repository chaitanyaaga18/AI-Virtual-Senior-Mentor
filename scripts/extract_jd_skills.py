import os
import pandas as pd

skills_list = [
    "python","java","c++","sql","machine learning","deep learning",
    "data structures","algorithms","system design",
    "aws","docker","kubernetes","html","css","javascript",
    "react","node","git","linux","pandas","numpy","tensorflow","pytorch"
]

jd_folder = "./data/job_descriptions/raw/"

jd_skills = {}

for file in os.listdir(jd_folder):

    if file.endswith(".txt"):

        with open(jd_folder + file,"r",encoding="utf-8") as f:
            text = f.read().lower()

        found_skills = []

        for skill in skills_list:
            if skill in text:
                found_skills.append(skill)

        jd_skills[file] = found_skills



for jd, skills in jd_skills.items():
    print(jd, "->", skills)



data = []

for jd, skills in jd_skills.items():
    data.append({
        "jd": jd,
        "skills": ", ".join(skills)
    })

df = pd.DataFrame(data)

df.to_csv("./data/jd_skills_dataset.csv", index=False)

print("JD skills dataset saved successfully")