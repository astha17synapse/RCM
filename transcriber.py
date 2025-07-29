import os
import sounddevice as sd
import numpy as np
import scipy.io.wavfile
import tempfile
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Ensure it's set in your system or shell
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/audio/transcriptions"

def record_audio(duration=5, samplerate=16000):
    print(f"🎙️ Recording for {duration} seconds...")
    recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    print(" Recording finished")
    return recording, samplerate

def save_temp_wav(recording, samplerate):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    scipy.io.wavfile.write(temp_file.name, samplerate, recording)
    return temp_file.name

def transcribe_audio(file_path):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }
    files = {
        "file": open(file_path, "rb"),
    }
    data = {
        "model": "whisper-large-v3",
        "language": "en"
    }

    response = requests.post(GROQ_ENDPOINT, headers=headers, data=data, files=files)

    if response.status_code == 200:
        return response.json()["text"]
    else:
        raise Exception(f"Groq API Error: {response.status_code} — {response.text}")
