# AI Virtual Senior Mentor

An AI-powered placement preparation platform that helps students analyze resumes, match job descriptions, identify skill gaps, and receive company-specific interview guidance using LLMs and semantic similarity.


# Features

- Resume PDF Upload
- Resume Parsing
- Semantic Resume-JD Matching
- Skill Gap Analysis
- Company-wise Interview Experiences
- AI Mentor Chatbot
- OpenAI LLM Integration
- Streamlit Interactive UI
- Vector Search using FAISS


# Technologies Used

## Frontend
- Streamlit

## Backend
- Python

## AI/ML
- OpenAI API
- Sentence Transformers
- Cosine Similarity
- FAISS Vector Search

## Libraries
- pdfplumber
- scikit-learn
- sentence-transformers
- python-dotenv



# Project Structure

```bash
AI-VIRTUAL-SENIOR-MENTOR/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── data/
├── scripts/
├── utils/
│
├── vector_index.faiss
└── doc_mapping.pkl
```



# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/AI-Virtual-Senior-Mentor.git
```

## Move into project

```bash
cd AI-Virtual-Senior-Mentor
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Create `.env`

```env
OPENAI_API_KEY=your_api_key
```



# Run Project

```bash
streamlit run app.py
```


# Workflow

1. User uploads resume
2. Resume text extracted
3. Resume matched with multiple job descriptions
4. Semantic similarity score generated
5. Skill gaps identified
6. Interview experiences fetched
7. Context sent to OpenAI LLM
8. AI mentor generates preparation guidance


# AI Features

## Resume Matching
Uses SentenceTransformer embeddings and cosine similarity.

## Skill Gap Analysis
Compares extracted skills between resume and job descriptions.

## Interview Guidance
Uses stored company interview experiences for contextual responses.

## LLM Integration
Uses OpenAI GPT models for intelligent mentorship.


# Security

- API keys stored securely in `.env`
- `.env` excluded using `.gitignore`


# Sample Output

- Resume Match Percentage
- Top Company Recommendations
- Missing Skills
- AI Mentor Responses


# Future Scope

- Heatmaps & Analytics
- Resume Improvement Suggestions
- PDF Report Generation
- Multi-user Authentication
- Real-time Interview Tracking


# Author

Chaitanya Agarwal


# License

This project is for educational and research purposes.