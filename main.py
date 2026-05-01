from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from matcher import get_match
from database import save_analysis, get_analyses


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Job Fit Analyzer API is running"}

@app.post("/analyze")
def analyze(resume: str = Form(...), job_description: str = Form(...)):
    result = get_match(resume, job_description)
    save_analysis(resume, job_description, result["match_score"], result["missing_keywords"])
    return result

@app.get("/history")
def history():
    return get_analyses()
