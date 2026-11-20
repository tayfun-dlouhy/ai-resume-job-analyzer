import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def has_openai_key() -> bool:
    return bool(os.getenv("OPENAI_API_KEY"))

def generate_ai_feedback(resume_text: str, job_text: str, score_data: dict) -> str:
    if not has_openai_key():
        missing = ", ".join(score_data.get("missing_skills", [])[:8])
        if missing:
            return f"Local feedback: Review these job skills not found in your resume: {missing}. Add examples only where accurate."
        return "Local feedback: No additional skills from the recognized list. Review the full job requirements for context."

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"""
Analyze the resume against the job description.
Give concise, practical improvement suggestions.

ATS data:
{score_data}

Resume:
{resume_text[:5000]}

Job description:
{job_text[:5000]}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()

def generate_cover_letter(resume_text: str, job_text: str) -> str:
    if not has_openai_key():
        return (
            "Dear Hiring Team,\n\n"
            "I am applying for the advertised working student position. "
            "My studies in computer science and practical project experience with Python, data processing, "
            "document analysis and automation make me motivated to contribute to your team.\n\n"
            "Kind regards\nTayfun Volkan Dlouhy"
        )

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"""
Write a concise professional cover letter for a working student IT position.
Use only truthful information from the resume and job description.

Resume:
{resume_text[:5000]}

Job description:
{job_text[:5000]}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )
    return response.choices[0].message.content.strip()
