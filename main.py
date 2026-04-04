from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Job Fit Analyzer API is running"}

@app.post("/analyze")
def analyze(resume: str, job_description: str):
    # placeholder — real logic goes in matcher.py later
    return {
        "match_score": 72,
        "missing_keywords": ["Docker", "React"]
    }