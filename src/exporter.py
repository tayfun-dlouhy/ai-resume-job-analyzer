from datetime import datetime

def export_report(score_data: dict, feedback: str, cover_letter: str) -> str:
    lines = [
        "# AI Resume & Job Analyzer Report",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        f"## ATS Score: {score_data.get('score', 0)}%",
        "",
        "## Matched Skills",
        ", ".join(score_data.get("matched_skills", [])) or "None detected",
        "",
        "## Missing Skills",
        ", ".join(score_data.get("missing_skills", [])) or "None detected",
        "",
        "## Feedback",
        feedback,
        "",
        "## Draft Cover Letter",
        cover_letter,
    ]
    return "\n".join(lines)
