from src.text_processing import keyword_frequency
from src.skills import compare_skills

def ats_score(resume_text: str, job_text: str) -> dict:
    resume_words = keyword_frequency(resume_text)
    job_words = keyword_frequency(job_text)

    if not job_words:
        return {"score": 0, "matched_keywords": [], "missing_keywords": [], **compare_skills(resume_text, job_text)}

    important_keywords = [word for word, _ in job_words.most_common(40)]
    matched = [word for word in important_keywords if word in resume_words]
    missing = [word for word in important_keywords if word not in resume_words]

    score = round((len(matched) / len(important_keywords)) * 100)
    skill_result = compare_skills(resume_text, job_text)

    return {
        "score": score,
        "matched_keywords": matched,
        "missing_keywords": missing[:20],
        **skill_result,
    }
