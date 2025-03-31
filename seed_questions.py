
import requests

# Replace with your actual backend URL
BACKEND_URL = "https://iq-backend.unnhost.com/doc"

# Example IQ test questions
questions = [
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

def seed_questions():
    for q in questions:
        response = requests.post(BACKEND_URL, json=q)
        print(f"Seeding question {q['id']} - Status: {response.status_code}")
        if response.status_code != 200:
            print("Error:", response.text)

if __name__ == "__main__":
    seed_questions()
