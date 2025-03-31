
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Dict

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./iq_test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    options = Column(String, nullable=False)  # JSON stringified dict
    answer = Column(String, nullable=False)
    difficulty = Column(String)
    category = Column(String)
    weight = Column(Integer, default=1)

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    score = Column(Integer)
    total = Column(Integer)
    estimated_iq = Column(Integer)

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.get("/questions")
def get_questions(db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    return [{
        "id": q.id,
        "question": q.question,
        "options": eval(q.options),
        "answer": q.answer,
        "difficulty": q.difficulty,
        "category": q.category,
        "weight": q.weight
    } for q in questions]

@app.post("/submit")
def submit_answers(payload: Dict, db: Session = Depends(get_db)):
    name = payload.get("name", "Anonymous")
    answers = payload.get("answers", [])

    correct = 0
    total = 0
    category_scores = {}

    for item in answers:
        q = db.query(Question).filter_by(id=item["question_id"]).first()
        if not q:
            continue
        total += q.weight
        if item["selected"] == q.answer:
            correct += q.weight
            category_scores[q.category] = category_scores.get(q.category, 0) + q.weight

    estimated_iq = 85 + int((correct / total) * 30) if total else 85
    feedback = []

    if estimated_iq > 125:
        feedback.append("Genius level! Incredible reasoning.")
    elif estimated_iq > 110:
        feedback.append("Above average intellect.")
    elif estimated_iq > 95:
        feedback.append("Average intelligence.")
    else:
        feedback.append("Keep practicing! You can improve.")

    result = Result(name=name, score=correct, total=total, estimated_iq=estimated_iq)
    db.add(result)
    db.commit()

    return {
        "estimated_iq": estimated_iq,
        "score": correct,
        "max_score": total,
        "category_scores": category_scores,
        "feedback": feedback,
    }

# Auto-seed when backend boots (only once, comment this after)
from auto_seed import seed_questions
with next(get_db()) as db:
    seed_questions(db)
    
