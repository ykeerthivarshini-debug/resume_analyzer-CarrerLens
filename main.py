import os
import sqlite3
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="Resume Analyzer - CareerLens")

# Database and file path configurations
DB_NAME = "resume_database.db"
CSV_FILE = "jobs.csv" # Update with your actual CSV file name if different

def init_database():
    """Initializes the database tables (equivalent to init_db.py)"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analyzed_resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            score REAL,
            matched_skills TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def check_csv_data():
    """Validates and checks CSV data (equivalent to check_csv.py)"""
    if os.path.exists(CSV_FILE):
        try:
            df = pd.read_csv(CSV_FILE)
            print(f"CSV file loaded successfully. Shape: {df.shape}")
            return df
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return None
    else:
        print(f"CSV file '{CSV_FILE}' not found. Please ensure it is uploaded.")
        return None

# Run initialization steps on startup
init_database()
check_csv_data()

# Frontend User Interface served directly from the main file
HTML_HOMEPAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Resume Analyzer - CareerLens</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }
        .container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h2 { color: #333; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Welcome to Resume Analyzer (CareerLens)</h2>
        <p>Your single-file application is running successfully!</p>
        <form action="/analyze" method="post" enctype="multipart/form-data">
            <label>Upload Resume:</label><br><br>
            <input type="file" name="file"><br><br>
            <button type="submit" style="padding: 10px 15px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;">Analyze Resume</button>
        </form>
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return HTML_HOMEPAGE

@app.post("/analyze")
async def analyze_endpoint(request: Request):
    # Handle resume analysis logic here
    return {"message": "Resume received and processed!"}

if __name__ == "__main__":
    # Run the application using Uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
