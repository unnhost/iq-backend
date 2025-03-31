from main import Question, SessionLocal
import json

def seed_questions():
    questions = [
  {
    "question": "Which number should come next in the series? 2, 4, 8, 16, ...",
    "options": {
      "A": "18",
      "B": "24",
      "C": "32",
      "D": "30"
    },
    "answer": "C",
    "difficulty": "Easy",
    "category": "Patterns",
    "weight": 1
  },
  {
    "question": "What is the missing number in the sequence? 1, 4, 9, 16, __, 36",
    "options": {
      "A": "20",
      "B": "25",
      "C": "30",
      "D": "27"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Sequences",
    "weight": 2
  },
  {
    "question": "Which word does NOT belong: Apple, Banana, Carrot, Grape?",
    "options": {
      "A": "Banana",
      "B": "Carrot",
      "C": "Apple",
      "D": "Grape"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Verbal",
    "weight": 1
  },
  {
    "question": "If all bloops are razzies and all razzies are lazzies, are all bloops definitely lazzies?",
    "options": {
      "A": "Yes",
      "B": "No",
      "C": "Maybe",
      "D": "Can't Say"
    },
    "answer": "A",
    "difficulty": "Medium",
    "category": "Logic",
    "weight": 2
  },
  {
    "question": "What comes next: J, F, M, A, M, J, __?",
    "options": {
      "A": "J",
      "B": "A",
      "C": "S",
      "D": "D"
    },
    "answer": "A",
    "difficulty": "Easy",
    "category": "Patterns",
    "weight": 1
  },
  {
    "question": "Which shape is different from the rest: Square, Triangle, Cube, Circle?",
    "options": {
      "A": "Square",
      "B": "Triangle",
      "C": "Cube",
      "D": "Circle"
    },
    "answer": "C",
    "difficulty": "Easy",
    "category": "Visual",
    "weight": 1
  },
  {
    "question": "What number is 1/4 of 1/2 of 1/5 of 200?",
    "options": {
      "A": "5",
      "B": "10",
      "C": "20",
      "D": "25"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Math",
    "weight": 3
  },
  {
    "question": "Which letter comes next in this pattern: A, C, F, J, O, __?",
    "options": {
      "A": "Q",
      "B": "T",
      "C": "U",
      "D": "V"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Sequences",
    "weight": 2
  },
  {
    "question": "Find the analogy: Bird is to Fly as Fish is to __?",
    "options": {
      "A": "Water",
      "B": "Swim",
      "C": "Lake",
      "D": "Gills"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Analogy",
    "weight": 1
  },
  {
    "question": "What day comes after Monday if the day before yesterday was Saturday?",
    "options": {
      "A": "Sunday",
      "B": "Tuesday",
      "C": "Wednesday",
      "D": "Monday"
    },
    "answer": "C",
    "difficulty": "Hard",
    "category": "Logic",
    "weight": 3
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
        print("✅ Real IQ questions seeded")
    else:
        print("⚠️ Questions already exist")
