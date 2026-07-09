COMMON_SKILLS = [
    "python", "java", "c", "sql", "git", "github", "docker", "linux",
    "streamlit", "flask", "fastapi", "rest", "api", "pandas", "numpy",
    "matplotlib", "power bi", "excel", "sharepoint", "power automate",
    "machine learning", "ki", "ai", "openai", "llm", "nlp",
    "softwareentwicklung", "datenanalyse", "automatisierung",
    "digitalisierung", "cloud", "azure", "aws", "testing", "pytest"
]

def extract_skills(text: str) -> set[str]:
    lower = text.lower()
    found = set()
    for skill in COMMON_SKILLS:
        if skill in lower:
            found.add(skill)
    return found

def compare_skills(resume_text: str, job_text: str) -> dict:
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)
    matched = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)
    return {
        "resume_skills": sorted(resume_skills),
        "job_skills": sorted(job_skills),
        "matched_skills": matched,
        "missing_skills": missing,
    }
