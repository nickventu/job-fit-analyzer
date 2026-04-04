from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

def get_match(resume: str, job_description: str):
    resume_clean = clean_text(resume)
    job_clean = clean_text(job_description)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_clean, job_clean])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    match_score = round(score * 100, 1)

    job_keywords = set(job_clean.split())
    resume_keywords = set(resume_clean.split())
    missing = job_keywords - resume_keywords

    stopwords = {"and", "or", "the", "a", "an", "in", "of", "to", "with", "for", "is", "are", "we", "you", "on", "at"}
    missing_keywords = [w for w in missing if len(w) > 3 and w not in stopwords]

    return {
        "match_score": match_score,
        "missing_keywords": sorted(missing_keywords)[:15]
    }