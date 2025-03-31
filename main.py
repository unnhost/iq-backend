
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from deta import Deta

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Deta Base
deta = Deta()
db = deta.Base("questions")

# Example questions to seed
seed_questions = [
    {
        "key": "1",
        "question": "What comes next in the sequence? 2, 4, 8, 16, ?",
        "options": ["18", "24", "32", "20"],
        "answer": "32"
    },
    {
        "key": "2",
        "question": "Which shape is different from the others?",
        "options": ["Circle", "Square", "Triangle", "Apple"],
        "answer": "Apple"
    },
    {
        "key": "3",
        "question": "If all Bloops are Razzies and all Razzies are Lazzies, are all Bloops definitely Lazzies?",
        "options": ["Yes", "No", "Cannot be determined", "Only some"],
        "answer": "Yes"
    }
]

@app.on_event("startup")
async def seed_on_startup():
    existing = db.fetch().items
    if not existing:
        for q in seed_questions:
            db.put(q)
        print("✅ Questions seeded to database.")
    else:
        print("ℹ️ Questions already exist. Skipping seeding.")

@app.get("/")
async def root():
    return {"message": "IQ Test Backend"}

@app.get("/question")
async def get_questions():
    res = db.fetch()
    return res.items
