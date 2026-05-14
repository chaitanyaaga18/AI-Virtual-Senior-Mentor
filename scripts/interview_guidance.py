import pandas as pd

def get_interview_topics():

    df = pd.read_csv("./data/interview_topics_dataset.csv")

    topics = []

    for row in df["topics"]:

        if pd.isna(row):
            continue

        topics.extend(str(row).split(", "))

    topics = list(set(topics))

    return topics