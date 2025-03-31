
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SQLALCHEMY_DATABASE_URL = "sqlite:///./iq_test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    options = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    difficulty = Column(String)
    category = Column(String)
    weight = Column(Integer, default=1)

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    score = Column(Integer)
    max_score = Column(Integer)
    estimated_iq = Column(Integer)
    category_scores = Column(Text)  # JSON
    feedback = Column(Text)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/questions")
def get_questions(db: Session = Depends(get_db)):
    return [
        {
            "id": q.id,
            "question": q.question,
            "options": json.loads(q.options),
            "answer": q.answer,
            "difficulty": q.difficulty,
            "category": q.category,
            "weight": q.weight,
        }
        for q in db.query(Question).all()
    ]

@app.get("/results")
def get_all_results(db: Session = Depends(get_db)):
    return db.query(Result).all()

@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    count = db.query(Result).count()
    avg_iq = db.query(Result).with_entities(func.avg(Result.estimated_iq)).scalar()
    return {"total_tests": count, "average_iq": int(avg_iq or 0)}

@app.post("/submit")
def submit_answers(payload: Dict, x_token: str = Header(...), db: Session = Depends(get_db)):
    if x_token != "user-token":
        raise HTTPException(status_code=403, detail="Unauthorized")
    answers = payload.get("answers", [])
    total_score = 0
    max_score = 0
    log = []
    category_scores = {}

    for ans in answers:
        q = db.query(Question).filter(Question.id == ans["question_id"]).first()
        if not q:
            continue
        correct = ans["selected"] == q.answer and ans["time_taken"] <= 30
        if correct:
            total_score += q.weight
            category_scores[q.category] = category_scores.get(q.category, 0) + q.weight
        max_score += q.weight
        log.append({
            "question": q.question,
            "correct": q.answer,
            "selected": ans["selected"],
            "is_correct": correct,
            "time": ans["time_taken"]
        })

    estimated_iq = 85 + int((total_score / max_score) * 60) if max_score else 85

    # Feedback system
    feedback = []
    for cat in category_scores:
        score = category_scores[cat]
        if score >= 4:
            feedback.append(f"Strong in {cat}")
        elif score >= 2:
            feedback.append(f"Average in {cat}")
        else:
            feedback.append(f"Needs improvement in {cat}")

    # Save result
    result = Result(
        score=total_score,
        max_score=max_score,
        estimated_iq=estimated_iq,
        category_scores=json.dumps(category_scores),
        feedback=json.dumps(feedback),
    )
    db.add(result)
    db.commit()

    return {
        "score": total_score,
        "max_score": max_score,
        "estimated_iq": estimated_iq,
        "log": log,
        "category_scores": category_scores,
        "feedback": feedback
    }

@app.post("/admin/questions")
def add_question(q: Dict, x_token: str = Header(...), db: Session = Depends(get_db)):
    if x_token != "admin-token":
        raise HTTPException(status_code=403, detail="Unauthorized")
    obj = Question(
        question=q["question"],
        options=json.dumps(q["options"]),
        answer=q["answer"],
        difficulty=q.get("difficulty"),
        category=q.get("category"),
        weight=q.get("weight", 1),
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return {"message": "Question added", "id": obj.id}
