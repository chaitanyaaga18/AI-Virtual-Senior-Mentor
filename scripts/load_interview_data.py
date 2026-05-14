import os

def load_interview_data():
    folder = "data/interview_experiences/raw"
    data = {}

    for file in os.listdir(folder):
        with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
            content = f.read()

            # extract company name
            lines = content.split("\n")
            company = None

            for line in lines:
                if "Company:" in line:
                    company = line.split("Company:")[1].strip().lower()
                    break

            if company:
                if company not in data:
                    data[company] = []

                data[company].append(content)

    return data