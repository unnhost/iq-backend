
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for questions
questions = []

# Example questions to seed
seed_questions = [
    {
        "id": 1,
        "question": "What comes next in the sequence? 2, 4, 8, 16, ?",
        "options": ["18", "24", "32", "20"],
        "answer": "32"
    },
    {
        "id": 2,
        "question": "Which shape is different from the others?",
        "options": ["Circle", "Square", "Triangle", "Apple"],
        "answer": "Apple"
    },
    {
        "id": 3,
        "question": "If all Bloops are Razzies and all Razzies are Lazzies, are all Bloops definitely Lazzies?",
        "options": ["Yes", "No", "Cannot be determined", "Only some"],
        "answer": "Yes"
    }
]

@app.on_event("startup")
async def startup_event():
    if not questions:
        questions.extend(seed_questions)
        print("✅ Questions seeded in memory.")

@app.get("/")
async def root():
    return {"message": "IQ Test Backend (in-memory)"}

@app.get("/question")
async def get_questions():
    return questions
