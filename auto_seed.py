
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from main import Question, get_db

def seed_questions(db: Session):
    questions = []

    for i in range(1, 51):
        questions.append(Question(
            question=f"What is {i} + {i}?",
            options=str({
                "A": str(i * 2 - 1),
                "B": str(i * 2),
                "C": str(i * 2 + 1),
                "D": str(i + 1)
            }),
            answer="B",
            difficulty="Easy" if i <= 20 else "Medium" if i <= 40 else "Hard",
            category="Math",
            weight=1
        ))

    for q in questions:
        db.add(q)
    db.commit()
    print(f"✅ Seeded {len(questions)} questions.")

# For auto-run if script is executed directly
if __name__ == "__main__":
    from main import SessionLocal
    db = SessionLocal()
    seed_questions(db)
    db.close()
