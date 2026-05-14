import os
from dotenv import load_dotenv
from openai import OpenAI



load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY")



# Initialize client safely
client = None
if api_key:
    client = OpenAI(api_key=api_key)


def generate_llm_response(context, question):
    """
    Generates response using OpenAI.
    If API fails → fallback to dummy response (so app never crashes)
    """

    prompt = f"""
You are an AI Placement Mentor.

Context:
{context}

User Question:
{question}

Give a clear, structured answer including:
- Preparation strategy
- Important topics
- Company-specific tips (if any)
"""

    # 🚨 If API key missing → fallback
    if not client:
        return f"""
⚠️ OpenAI API not configured.

Question: {question}

👉 Your system is working correctly.
👉 Add API key to enable real AI answers.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful placement mentor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        # 🔥 IMPORTANT: prevent crash + show useful debug
        return f"""
❌ API Error (Handled Safely)

Error:
{str(e)}

👉 Fix:
1. Check API key in .env
2. Ensure billing is added
3. Restart app after updating key

Meanwhile your app is working perfectly.
"""