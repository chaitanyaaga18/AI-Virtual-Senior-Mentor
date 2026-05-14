import os

def generate_preparation_advice(files):

    advice = ""

    for file in files:

        path = "./data/job_descriptions/raw/" + file

        if os.path.exists(path):

            with open(path,"r",encoding="utf-8") as f:

                text = f.read()

            advice += text[:800] + "\n\n"

    return advice