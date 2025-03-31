
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load questions
with open("questions.json", "r") as f:
    QUESTIONS = json.load(f)

RESULTS_FILE = "results.json"

@app.get("/")
def root():
    return {"message": "IQ Test Backend is running."}

@app.get("/questions")
def get_questions():
    return QUESTIONS

@app.post("/submit")
async def submit_results(request: Request):
    data = await request.json()
    print("New result submitted:", data)

    # Append result to results.json
    try:
        if os.path.exists(RESULTS_FILE):
            with open(RESULTS_FILE, "r") as f:
                results = json.load(f)
        else:
            results = []

        results.append(data)

        with open(RESULTS_FILE, "w") as f:
            json.dump(results, f, indent=2)

        return {"status": "success", "message": "Result saved"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

import requests  # Ensure this is imported at the top of main.py

SUPABASE_URL = "https://gsffsoqpuovvehvrkzos.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdzZmZzb3FwdW92dmVodnJrem9zIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM0NDcyNzQsImV4cCI6MjA1OTAyMzI3NH0.lJvQLG7AGfh4jFELn8529yXnXnYepKEDh8A3kqBBqKE"

@app.get("/leaderboard")
def get_leaderboard():
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}"
    }
    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/results?select=name,iq,score,max_score&order=iq.desc&limit=10",
        headers=headers
    )
    response.raise_for_status()
    return response.json()
