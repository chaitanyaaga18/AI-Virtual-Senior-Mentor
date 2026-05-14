import pdfplumber
import os
print("Script started...")
input_folder = "./data/resumes/raw/"
output_folder = "./data/resumes/processed/"

print("Files inside folder:", os.listdir(input_folder))

for file in os.listdir(input_folder):

    print("Found file:", file)

    if file.endswith(".pdf"):

        print("Processing:", file)

        with pdfplumber.open(input_folder + file) as pdf:

            text = ""

            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text()

        output_file = output_folder + file.replace(".pdf", ".txt")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)

print("Resume text extraction complete")