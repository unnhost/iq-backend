from main import Question, SessionLocal
import json

questions = [
    {
        "question": "What is 2 + 2?",
        "options": {"A": "3", "B": "4", "C": "5", "D": "22"},
        "answer": "B",
        "difficulty": "Easy",
        "category": "Math",
        "weight": 1
    },
    {
        "question": "Which is the odd one out: Apple, Banana, Car, Orange?",
        "options": {"A": "Apple", "B": "Banana", "C": "Car", "D": "Orange"},
        "answer": "C",
        "difficulty": "Easy",
        "category": "Logic",
        "weight": 1
    }
]

db = SessionLocal()
if db.query(Question).count() == 0:
    for q in questions:
        obj = Question(
            question=q["question"],
            options=json.dumps(q["options"]),
            answer=q["answer"],
            difficulty=q["difficulty"],
            category=q["category"],
            weight=q["weight"]
        )
        db.add(obj)
    db.commit()
    print("✅ Sample questions seeded")
else:
    print("⚠️ Questions already exist")
