# app/transcriber.py

import whisper
from pathlib import Path

# Load model once globally (can switch to 'medium' or 'large' if needed)
model = whisper.load_model("base")  # or "small", "medium", "large"

def transcribe_audio(file_path: str) -> str:
    """
    Transcribes an audio file to text using Whisper.
    
    Args:
        file_path (str): Path to audio file (.mp3, .wav, etc.)

    Returns:
        str: Transcribed text
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    print(f"[Transcriber] Transcribing: {file_path}")
    result = model.transcribe(file_path)
    return result['text']
