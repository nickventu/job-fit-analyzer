from database import save_analysis, get_analyses
from fastapi import FastAPI
from matcher import get_match


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Job Fit Analyzer API is running"}

@app.post("/analyze")
def analyze(resume: str, job_description: str):
    result = get_match(resume, job_description)
    save_analysis(resume, job_description, result["match_score"], result["missing_keywords"])
    return result

@app.get("/history")
def history():
    return get_analyses()
