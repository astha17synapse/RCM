# app/main.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.audio.transcriber import record_audio, save_temp_wav, transcribe_audio
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.audio.transcriber import transcribe_audio, record_audio, save_temp_wav
from app.routes.intake import router as intake_router  

app = FastAPI()

app.include_router(intake_router)  #  Register the routes here

@app.get("/")
def root():
    return {"message": " Voice-to-Text API using Groq Whisper is running!"}

@app.get("/record-and-transcribe/")
def record_and_transcribe():
    try:
        recording, samplerate = record_audio()
        file_path = save_temp_wav(recording, samplerate)
        text = transcribe_audio(file_path)
        os.remove(file_path)
        return JSONResponse(content={"transcription": text})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
