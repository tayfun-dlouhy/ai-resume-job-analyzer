from src.scoring import ats_score

def test_ats_score_detects_keywords():
    result = ats_score("Python SQL Git", "Python SQL Docker")
    assert result["score"] > 0
    assert "python" in result["matched_keywords"]
