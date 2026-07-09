import streamlit as st
from src.pdf_reader import extract_pdf_text
from src.scoring import ats_score
from src.openai_service import generate_ai_feedback, generate_cover_letter
from src.database import save_analysis, get_recent_analyses
from src.exporter import export_report

st.set_page_config(page_title="AI Resume & Job Analyzer", page_icon="🤖", layout="wide")

st.markdown("""
<style>
.block-container {max-width: 1200px; padding-top: 2rem;}
.hero {padding: 1.5rem; border-radius: 18px; background: linear-gradient(135deg, rgba(34,139,230,.18), rgba(132,94,247,.14)); margin-bottom: 1rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🤖 AI Resume & Job Analyzer</h1>
<p>Analyze a resume against a job description, calculate an ATS-style score and generate improvement suggestions.</p>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1, 1])

with left:
    st.subheader("📄 Resume")
    resume_pdf = st.file_uploader("Upload resume PDF", type=["pdf"])
    resume_text_input = st.text_area("Or paste resume text", height=180)

with right:
    st.subheader("💼 Job Description")
    job_pdf = st.file_uploader("Upload job description PDF", type=["pdf"])
    job_text_input = st.text_area("Or paste job description", height=180)

resume_text = extract_pdf_text(resume_pdf) if resume_pdf else resume_text_input
job_text = extract_pdf_text(job_pdf) if job_pdf else job_text_input

if st.button("Analyze Match", type="primary"):
    if not resume_text.strip() or not job_text.strip():
        st.error("Please provide both resume and job description.")
        st.stop()

    with st.spinner("Analyzing resume and job description..."):
        score_data = ats_score(resume_text, job_text)
        feedback = generate_ai_feedback(resume_text, job_text, score_data)
        cover_letter = generate_cover_letter(resume_text, job_text)
        save_analysis(score_data["score"], score_data["matched_skills"], score_data["missing_skills"])

    st.subheader("📊 Results")
    col1, col2, col3 = st.columns(3)
    col1.metric("ATS Score", f"{score_data['score']}%")
    col2.metric("Matched Skills", len(score_data["matched_skills"]))
    col3.metric("Missing Skills", len(score_data["missing_skills"]))

    st.markdown("### ✅ Matched Skills")
    st.write(", ".join(score_data["matched_skills"]) or "No matching skills detected.")

    st.markdown("### ⚠️ Missing Skills")
    st.write(", ".join(score_data["missing_skills"]) or "No missing skills detected.")

    st.markdown("### 🧠 Improvement Suggestions")
    st.write(feedback)

    st.markdown("### ✉️ Cover Letter Draft")
    st.text_area("Generated cover letter", cover_letter, height=260)

    report = export_report(score_data, feedback, cover_letter)
    st.download_button("Download Report as Markdown", report, "resume_job_analysis.md", "text/markdown")

with st.expander("Recent local analyses"):
    for row in get_recent_analyses():
        st.write(f"{row[0]} · Score: {row[1]}% · Matched: {row[2]} · Missing: {row[3]}")
