from datetime import datetime

def export_report(score_data: dict, feedback: str, cover_letter: str) -> str:
    lines = [
        "# AI Resume & Job Analyzer Report",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        f"## Keyword Overlap: {score_data.get('score', 0)}%",
        "",
        "Share of the up to 40 most frequent job-posting terms found in the resume after tokenization and stopword filtering.",
        "",
        "## Matched Skills",
        ", ".join(score_data.get("matched_skills", [])) or "None detected",
        "",
        "## Skills not found in resume",
        ", ".join(score_data.get("missing_skills", [])) or "None detected",
        "",
        "## Feedback",
        feedback,
        "",
        "## Draft Cover Letter",
        cover_letter,
    ]
    return "\n".join(lines)
