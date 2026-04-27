import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME")
    )

def save_analysis(resume: str, job_description: str, match_score: float, missing_keywords: list):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO analyses (resume, job_description, match_score, missing_keywords) VALUES (%s, %s, %s, %s)",
        (resume, job_description, match_score, str(missing_keywords))
    )
    conn.commit()
    cursor.close()
    conn.close()

def get_analyses():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT * FROM analyses ORDER BY created_at DESC")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results