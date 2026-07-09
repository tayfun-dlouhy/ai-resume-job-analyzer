from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def export_pdf(text: str, filename: str = "resume_analysis_report.pdf") -> str:
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()

    story = [
        Paragraph("AI Resume & Job Analyzer Report", styles["Title"]),
        Spacer(1, 16),
    ]

    for line in text.split("\n"):
        if line.strip():
            story.append(Paragraph(line, styles["BodyText"]))
            story.append(Spacer(1, 8))

    doc.build(story)
    return filename