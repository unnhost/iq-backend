from fastapi import FastAPI, HTTPException, Depends, Header, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware


# CORS Middleware
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
    difficulty = Column(String, nullable=False)
    category = Column(String, nullable=False)
    weight = Column(Integer, nullable=False)

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    user_token = Column(String, nullable=False)
    score = Column(Integer)
    max_score = Column(Integer)
    iq = Column(Integer)

Base.metadata.create_all(bind=engine)

# In-memory token store (for demo purposes)
VALID_TOKENS = {"admin-token", "user-token"}

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_token(x_token: str = Header(...)):
    if x_token not in VALID_TOKENS:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return x_token

# Request models
class AnswerItem(BaseModel):
    question_id: int
    selected: Optional[str]
    time_taken: int

class Submission(BaseModel):
    answers: List[AnswerItem]

class QuestionIn(BaseModel):
    question: str
    options: Dict[str, str]
    answer: str
    difficulty: str
    category: str
    weight: int

@app.get("/questions")
def get_questions(db: Session = Depends(get_db)):
    qs = db.query(Question).all()
    return [
        {
            "id": q.id,
            "question": q.question,
            "options": eval(q.options),
            "difficulty": q.difficulty,
            "category": q.category,
            "weight": q.weight
        } for q in qs
    ]

@app.post("/submit")
def submit_answers(payload: Dict, x_token: str = Header(...), db: Session = Depends(get_db)):
    if x_token != "user-token":
        raise HTTPException(status_code=403, detail="Unauthorized")

    answers = payload.get("answers", [])

    total_score = 0
    max_score = 0
    log = []

    for ans in answers:
        q = db.query(Question).filter(Question.id == ans["question_id"]).first()
        if not q:
            continue

        correct = ans["selected"] == q.answer and ans["time_taken"] <= 30
        if correct:
            total_score += q.weight
        max_score += q.weight

        log.append({
            "question": q.question,
            "correct": q.answer,
            "selected": ans["selected"],
            "is_correct": correct,
            "time": ans["time_taken"]
        })

    estimated_iq = 85 + int((total_score / max_score) * 60) if max_score else 85

    return {
        "score": total_score,
        "max_score": max_score,
        "estimated_iq": estimated_iq,
        "log": log
    }


# Admin Endpoints
@app.post("/admin/questions")
def add_question(q: QuestionIn, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    if token != "admin-token":
        raise HTTPException(status_code=403, detail="Admin access required")
    q_obj = Question(
        question=q.question,
        options=str(q.options),
        answer=q.answer,
        difficulty=q.difficulty,
        category=q.category,
        weight=q.weight
    )
    db.add(q_obj)
    db.commit()
    return {"message": "Question added", "id": q_obj.id}

@app.delete("/admin/questions/{qid}")
def delete_question(qid: int, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    if token != "admin-token":
        raise HTTPException(status_code=403, detail="Admin access required")
    q = db.query(Question).filter(Question.id == qid).first()
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    db.delete(q)
    db.commit()
    return {"message": f"Question {qid} deleted"}

@app.get("/admin/results")
def get_results(
    token: str = Depends(verify_token),
    db: Session = Depends(get_db),
    min_score: Optional[int] = Query(None),
    max_score: Optional[int] = Query(None)
):
    if token != "admin-token":
        raise HTTPException(status_code=403, detail="Admin access required")

    query = db.query(Result)
    if min_score is not None:
        query = query.filter(Result.score >= min_score)
    if max_score is not None:
        query = query.filter(Result.score <= max_score)

    return query.all()
