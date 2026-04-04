from fastapi import FastAPI
from matcher import get_match


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Job Fit Analyzer API is running"}

@app.post("/analyze")
def analyze(resume: str, job_description: str):
    return get_match(resume, job_description)
