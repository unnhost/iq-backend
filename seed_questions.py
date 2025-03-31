from main import Question, SessionLocal
import json

def seed_questions():
    questions = [
  {
    "question": "Sample IQ Question #1: What is 1 + 1?",
    "options": {
      "A": "1",
      "B": "2",
      "C": "3",
      "D": "4"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Sequences",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #2: What is 2 + 2?",
    "options": {
      "A": "3",
      "B": "4",
      "C": "5",
      "D": "6"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Verbal",
    "weight": 3
  },
  {
    "question": "Sample IQ Question #3: What is 3 + 3?",
    "options": {
      "A": "5",
      "B": "6",
      "C": "7",
      "D": "8"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Patterns",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #4: What is 4 + 4?",
    "options": {
      "A": "7",
      "B": "8",
      "C": "9",
      "D": "10"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Verbal",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #5: What is 5 + 5?",
    "options": {
      "A": "9",
      "B": "10",
      "C": "11",
      "D": "12"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Logic",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #6: What is 6 + 6?",
    "options": {
      "A": "11",
      "B": "12",
      "C": "13",
      "D": "14"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Patterns",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #7: What is 7 + 7?",
    "options": {
      "A": "13",
      "B": "14",
      "C": "15",
      "D": "16"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Verbal",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #8: What is 8 + 8?",
    "options": {
      "A": "15",
      "B": "16",
      "C": "17",
      "D": "18"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Sequences",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #9: What is 9 + 9?",
    "options": {
      "A": "17",
      "B": "18",
      "C": "19",
      "D": "20"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Sequences",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #10: What is 10 + 10?",
    "options": {
      "A": "19",
      "B": "20",
      "C": "21",
      "D": "22"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Verbal",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #11: What is 11 + 11?",
    "options": {
      "A": "21",
      "B": "22",
      "C": "23",
      "D": "24"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Verbal",
    "weight": 3
  },
  {
    "question": "Sample IQ Question #12: What is 12 + 12?",
    "options": {
      "A": "23",
      "B": "24",
      "C": "25",
      "D": "26"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Sequences",
    "weight": 3
  },
  {
    "question": "Sample IQ Question #13: What is 13 + 13?",
    "options": {
      "A": "25",
      "B": "26",
      "C": "27",
      "D": "28"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Patterns",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #14: What is 14 + 14?",
    "options": {
      "A": "27",
      "B": "28",
      "C": "29",
      "D": "30"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Verbal",
    "weight": 3
  },
  {
    "question": "Sample IQ Question #15: What is 15 + 15?",
    "options": {
      "A": "29",
      "B": "30",
      "C": "31",
      "D": "32"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Sequences",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #16: What is 16 + 16?",
    "options": {
      "A": "31",
      "B": "32",
      "C": "33",
      "D": "34"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Logic",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #17: What is 17 + 17?",
    "options": {
      "A": "33",
      "B": "34",
      "C": "35",
      "D": "36"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Math",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #18: What is 18 + 18?",
    "options": {
      "A": "35",
      "B": "36",
      "C": "37",
      "D": "38"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Logic",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #19: What is 19 + 19?",
    "options": {
      "A": "37",
      "B": "38",
      "C": "39",
      "D": "40"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Verbal",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #20: What is 20 + 20?",
    "options": {
      "A": "39",
      "B": "40",
      "C": "41",
      "D": "42"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Logic",
    "weight": 3
  },
  {
    "question": "Sample IQ Question #21: What is 21 + 21?",
    "options": {
      "A": "41",
      "B": "42",
      "C": "43",
      "D": "44"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Math",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #22: What is 22 + 22?",
    "options": {
      "A": "43",
      "B": "44",
      "C": "45",
      "D": "46"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Sequences",
    "weight": 3
  },
  {
    "question": "Sample IQ Question #23: What is 23 + 23?",
    "options": {
      "A": "45",
      "B": "46",
      "C": "47",
      "D": "48"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Math",
    "weight": 3
  },
  {
    "question": "Sample IQ Question #24: What is 24 + 24?",
    "options": {
      "A": "47",
      "B": "48",
      "C": "49",
      "D": "50"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Sequences",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #25: What is 25 + 25?",
    "options": {
      "A": "49",
      "B": "50",
      "C": "51",
      "D": "52"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Math",
    "weight": 3
  },
  {
    "question": "Sample IQ Question #26: What is 26 + 26?",
    "options": {
      "A": "51",
      "B": "52",
      "C": "53",
      "D": "54"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Logic",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #27: What is 27 + 27?",
    "options": {
      "A": "53",
      "B": "54",
      "C": "55",
      "D": "56"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Patterns",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #28: What is 28 + 28?",
    "options": {
      "A": "55",
      "B": "56",
      "C": "57",
      "D": "58"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Logic",
    "weight": 3
  },
  {
    "question": "Sample IQ Question #29: What is 29 + 29?",
    "options": {
      "A": "57",
      "B": "58",
      "C": "59",
      "D": "60"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Math",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #30: What is 30 + 30?",
    "options": {
      "A": "59",
      "B": "60",
      "C": "61",
      "D": "62"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Verbal",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #31: What is 31 + 31?",
    "options": {
      "A": "61",
      "B": "62",
      "C": "63",
      "D": "64"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Sequences",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #32: What is 32 + 32?",
    "options": {
      "A": "63",
      "B": "64",
      "C": "65",
      "D": "66"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Verbal",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #33: What is 33 + 33?",
    "options": {
      "A": "65",
      "B": "66",
      "C": "67",
      "D": "68"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Sequences",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #34: What is 34 + 34?",
    "options": {
      "A": "67",
      "B": "68",
      "C": "69",
      "D": "70"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Verbal",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #35: What is 35 + 35?",
    "options": {
      "A": "69",
      "B": "70",
      "C": "71",
      "D": "72"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Math",
    "weight": 3
  },
  {
    "question": "Sample IQ Question #36: What is 36 + 36?",
    "options": {
      "A": "71",
      "B": "72",
      "C": "73",
      "D": "74"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Sequences",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #37: What is 37 + 37?",
    "options": {
      "A": "73",
      "B": "74",
      "C": "75",
      "D": "76"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Verbal",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #38: What is 38 + 38?",
    "options": {
      "A": "75",
      "B": "76",
      "C": "77",
      "D": "78"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Sequences",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #39: What is 39 + 39?",
    "options": {
      "A": "77",
      "B": "78",
      "C": "79",
      "D": "80"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Logic",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #40: What is 40 + 40?",
    "options": {
      "A": "79",
      "B": "80",
      "C": "81",
      "D": "82"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Math",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #41: What is 41 + 41?",
    "options": {
      "A": "81",
      "B": "82",
      "C": "83",
      "D": "84"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Sequences",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #42: What is 42 + 42?",
    "options": {
      "A": "83",
      "B": "84",
      "C": "85",
      "D": "86"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Sequences",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #43: What is 43 + 43?",
    "options": {
      "A": "85",
      "B": "86",
      "C": "87",
      "D": "88"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Math",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #44: What is 44 + 44?",
    "options": {
      "A": "87",
      "B": "88",
      "C": "89",
      "D": "90"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Verbal",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #45: What is 45 + 45?",
    "options": {
      "A": "89",
      "B": "90",
      "C": "91",
      "D": "92"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Logic",
    "weight": 1
  },
  {
    "question": "Sample IQ Question #46: What is 46 + 46?",
    "options": {
      "A": "91",
      "B": "92",
      "C": "93",
      "D": "94"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Sequences",
    "weight": 3
  },
  {
    "question": "Sample IQ Question #47: What is 47 + 47?",
    "options": {
      "A": "93",
      "B": "94",
      "C": "95",
      "D": "96"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Sequences",
    "weight": 2
  },
  {
    "question": "Sample IQ Question #48: What is 48 + 48?",
    "options": {
      "A": "95",
      "B": "96",
      "C": "97",
      "D": "98"
    },
    "answer": "B",
    "difficulty": "Hard",
    "category": "Patterns",
    "weight": 3
  },
  {
    "question": "Sample IQ Question #49: What is 49 + 49?",
    "options": {
      "A": "97",
      "B": "98",
      "C": "99",
      "D": "100"
    },
    "answer": "B",
    "difficulty": "Easy",
    "category": "Sequences",
    "weight": 3
  },
  {
    "question": "Sample IQ Question #50: What is 50 + 50?",
    "options": {
      "A": "99",
      "B": "100",
      "C": "101",
      "D": "102"
    },
    "answer": "B",
    "difficulty": "Medium",
    "category": "Logic",
    "weight": 2
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
        print("✅ 50 Sample IQ questions seeded")
    else:
        print("⚠️ Questions already exist")
