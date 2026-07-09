import sqlite3
from datetime import datetime

DB_PATH = "analyses.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            score INTEGER NOT NULL,
            matched_skills TEXT,
            missing_skills TEXT
        )
        """)

def save_analysis(score: int, matched_skills: list[str], missing_skills: list[str]):
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO analyses (created_at, score, matched_skills, missing_skills) VALUES (?, ?, ?, ?)",
            (datetime.now().isoformat(timespec="seconds"), score, ", ".join(matched_skills), ", ".join(missing_skills)),
        )

def get_recent_analyses(limit: int = 5):
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute(
            "SELECT created_at, score, matched_skills, missing_skills FROM analyses ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
