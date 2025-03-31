
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# CORS setup (adjust if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load questions from file
with open("questions.json", "r") as f:
    QUESTIONS = json.load(f)

@app.get("/")
def root():
    return {"message": "IQ Test Backend is running."}

@app.get("/questions")
def get_questions():
    return QUESTIONS
