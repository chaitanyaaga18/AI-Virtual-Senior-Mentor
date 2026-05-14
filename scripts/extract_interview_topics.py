import os
import pandas as pd

topics_list = [
    "arrays","hashmap","graphs","trees","dynamic programming",
    "system design","databases","sql","operating systems",
    "networking","object oriented programming",
    "data structures","algorithms","scalability","distributed systems"
]

interview_folder = "./data/interview_experiences/raw/"

interview_topics = {}

for file in os.listdir(interview_folder):

    if file.endswith(".txt"):

        with open(interview_folder + file,"r",encoding="utf-8") as f:
            text = f.read().lower()

        found_topics = []

        for topic in topics_list:
            if topic in text:
                found_topics.append(topic)

        interview_topics[file] = found_topics


data = []

for interview, topics in interview_topics.items():
    data.append({
        "interview": interview,
        "topics": ", ".join(topics)
    })

df = pd.DataFrame(data)

df.to_csv("./data/interview_topics_dataset.csv",index=False)

print("Interview topics dataset saved")