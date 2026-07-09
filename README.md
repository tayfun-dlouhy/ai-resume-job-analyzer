# 🤖 AI Resume & Job Analyzer

![Application](assets/app-screenshot.png)

An AI-powered Resume & Job Analyzer built with **Python**, **Streamlit** and **OpenAI**.

The application compares a resume with a job description, calculates an ATS-style compatibility score, identifies missing skills, generates improvement suggestions and creates a personalized cover letter draft.

---

# 🚀 Live Demo

https://DEINE-STREAMLIT-URL.streamlit.app

---

# ✨ Features

- 📄 Upload resume as PDF
- 💼 Upload or paste a job description
- 🤖 AI-powered resume analysis
- 📊 ATS-style compatibility score
- ✅ Matching skills detection
- ⚠️ Missing skills analysis
- 🧠 Resume improvement suggestions
- ✉️ Automatic cover letter generation
- 📥 Export analysis as Markdown
- 🌙 Modern dark mode interface

---

# 🖼️ Application Preview

![Screenshot](assets/app-screenshot.png)

---

# 🛠️ Tech Stack

## Backend

- Python 3.11
- Streamlit
- OpenAI API
- SQLite
- PyPDF2

## AI

- GPT-4o-mini
- Natural Language Processing
- Resume Analysis
- Keyword Matching

## Development

- Git
- GitHub
- Docker
- GitHub Actions
- Streamlit Cloud

---

# 📂 Project Structure

```
ai-resume-job-analyzer
│
├── assets/
│   └── app-screenshot.png
│
├── src/
│   ├── answer_service.py
│   ├── config.py
│   ├── openai_engine.py
│   ├── local_answer_engine.py
│   ├── semantic_retriever.py
│   ├── ui_components.py
│   └── ...
│
├── tests/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── Dockerfile
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/tayfun-dlouhy/ai-resume-job-analyzer.git
```

Open the project

```bash
cd ai-resume-job-analyzer
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

macOS / Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start the application

```bash
streamlit run app.py
```

---

# 💻 Usage

1. Upload your resume as PDF.
2. Upload or paste a job description.
3. Click **Analyze Match**.
4. Review:
   - ATS Score
   - Matching Skills
   - Missing Skills
   - Resume Suggestions
   - Cover Letter Draft
5. Export the report as Markdown.

---

# 📈 Example Analysis

The application evaluates:

- ATS compatibility
- Technical skills
- Missing technologies
- Resume quality
- Personalized recommendations
- Cover letter generation

---

# 🧪 Testing

Run all tests

```bash
pytest
```

---

# 📦 Deployment

The application is deployed using **Streamlit Community Cloud**.

To deploy:

1. Push the repository to GitHub.
2. Connect the repository to Streamlit Cloud.
3. Select:

```
Main file:
app.py
```

Python Version

```
3.11
```

Deploy.

---

# 🔮 Future Improvements

- Semantic vector embeddings
- Multi-language support
- Multiple resume comparison
- Recruiter dashboard
- Resume scoring history
- OpenAI function calling
- Company-specific ATS optimization
- PDF report export
- User authentication
- PostgreSQL database

---

# 👨‍💻 Author

**Tayfun Dlouhy**

GitHub

https://github.com/tayfun-dlouhy

---

# ⭐ Why this project?

This project demonstrates practical skills in

- Python
- AI Integration
- Prompt Engineering
- PDF Processing
- Streamlit
- REST-ready Architecture
- SQL
- Software Architecture
- Git & GitHub
- Modern UI Design

It was built as part of a portfolio showcasing AI-powered software engineering projects.

---

# 📄 License

MIT License