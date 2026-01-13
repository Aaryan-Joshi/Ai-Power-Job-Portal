from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def match_resumes(job_description: str, resumes: list):
    """
    resumes = list of tuples -> [(filename, resume_text), ...]
    """
    documents = [job_description] + [text for _, text in resumes]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_scores = cosine_similarity(
        tfidf_matrix[0:1], tfidf_matrix[1:]
    ).flatten()

    ranked_results = []
    for i, (filename, _) in enumerate(resumes):
        ranked_results.append({
            "resume": filename,
            "score": round(similarity_scores[i] * 100, 2)
        })

    ranked_results.sort(key=lambda x: x["score"], reverse=True)

    with open("models/tfidf_vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    return ranked_results
