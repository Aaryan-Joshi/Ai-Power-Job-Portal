import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
STOP_WORDS = set(stopwords.words("english"))

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", " ", text)
    words = text.split()
    words = [word for word in words if word not in STOP_WORDS and len(word) > 2]
    return " ".join(words)
