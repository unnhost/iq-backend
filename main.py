
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
