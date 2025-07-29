# app/voice/whisper_handler.py

import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/audio/transcriptions"

def transcribe_with_whisper(file_path: str) -> str:
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY not set in environment.")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    data = {
        "model": "whisper-large-v3",
        "language": "en"
    }

    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(GROQ_ENDPOINT, headers=headers, data=data, files=files)

    if response.status_code == 200:
        return response.json()["text"]
    else:
        raise Exception(f"Groq API Error: {response.status_code} — {response.text}")
