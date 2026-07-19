import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_resume(resume_text):

    prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze the following resume and return the response in this format.

ATS Score:
Resume Summary:
Strengths:
Weaknesses:
Missing Skills:
Suggestions:
Interview Questions:

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text