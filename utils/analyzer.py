import json
import os
from unittest import result
from urllib import response
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def analyze_resume(resume_text):

    # Limit resume size to avoid sending extremely large requests
    resume_text = resume_text[:12000]

    # Debug: Print resume length in terminal
    print("Resume length:", len(resume_text))

    prompt = f"""
    You are an experienced Applicant Tracking System (ATS) and Senior Technical Recruiter.

    Analyze the resume exactly like a modern ATS would.

    Evaluate these categories independently:

    1. Resume Formatting (20 marks)
    2. Technical Skills (25 marks)
    3. Projects (25 marks)
    4. Experience / Internships (15 marks)
    5. Education & Certifications (15 marks)

    Rules:

    • Give realistic scores.
    • Do NOT give average/default scores.
    • If a section is excellent, give high marks.
    • If a section is missing, deduct marks.
    • ATS Score must equal the sum of all section scores.

    Return ONLY valid JSON.

    {{
        "ats_score": 0,

        "section_scores": {{
            "formatting": 0,
            "skills": 0,
            "projects": 0,
            "experience": 0,
            "education": 0
        }},

        "summary": "",

        "strengths": [],

        "weaknesses": [],

        "missing_skills": [],

        "suggestions": [],

        "interview_questions": []
    }}

    Resume:

    {resume_text}
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
        )

        print("========== GEMINI RESPONSE ==========")
        print(response.text)
        print("=====================================")

        result = json.loads(response.text)

        return result

    except Exception as e:
        raise Exception(f"Gemini API Error: {e}")