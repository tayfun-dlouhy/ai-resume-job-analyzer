from src.skills import extract_skills, compare_skills

def test_extract_skills():
    assert "python" in extract_skills("I use Python and SQL.")

def test_compare_skills():
    result = compare_skills("Python SQL", "Python Docker")
    assert "python" in result["matched_skills"]
    assert "docker" in result["missing_skills"]
