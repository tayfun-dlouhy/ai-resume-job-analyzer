import re
from collections import Counter

STOPWORDS = {
    "the","and","or","a","an","to","of","in","for","with","on","at","by","from",
    "der","die","das","und","oder","mit","für","von","im","in","zu","auf"
}

def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()

def tokenize(text: str) -> list[str]:
    words = re.findall(r"[a-zA-ZäöüÄÖÜß0-9+#.]+", normalize_text(text))
    return [w for w in words if w not in STOPWORDS and len(w) > 1]

def keyword_frequency(text: str) -> Counter:
    return Counter(tokenize(text))
