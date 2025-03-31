from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

SUPABASE_URL = "https://gsffsoqpuovvehvrkzos.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdzZmZzb3FwdW92dmVodnJrem9zIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM0NDcyNzQsImV4cCI6MjA1OTAyMzI3NH0.lJvQLG7AGfh4jFELn8529yXnXnYepKEDh8A3kqBBqKE"

@app.get("/leaderboard")
def get_leaderboard():
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}"
    }
    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/results?select=name,iq,score,max_score&order=iq.desc&limit=10",
        headers=headers
    )
    response.raise_for_status()
    return response.json()