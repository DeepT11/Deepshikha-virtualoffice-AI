# main.py

import streamlit as st
from app.transcriber import transcribe_audio
from app.summarizer import summarize_text
import os
import tempfile

st.set_page_config(page_title="Meeting Transcriber & Summarizer")

st.title("📋 Meeting Transcriber & Summarizer")
st.write("Upload your meeting audio (.mp3, .wav, etc.), and get a transcript and summary.")

# File uploader
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file:
    with st.spinner("Processing..."):
        # Save uploaded file to temp
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        try:
            # Transcribe
            st.subheader("📝 Transcript")
            transcript = transcribe_audio(tmp_path)
            st.text_area("Transcript", transcript, height=300)

            # Summarize
            st.subheader("📌 Summary")
            summary = summarize_text(transcript)
            st.text_area("Summary", summary, height=200)

            # Download buttons
            st.download_button("📥 Download Transcript", transcript, file_name="transcript.txt")
            st.download_button("📥 Download Summary", summary, file_name="summary.txt")

        except Exception as e:
            st.error(f"An error occurred: {e}")

        finally:
            os.remove(tmp_path)
