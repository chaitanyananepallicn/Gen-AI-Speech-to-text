import streamlit as st
import os
import tempfile
from pydub import AudioSegment
from moviepy.editor import VideoFileClip
import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
    return recognizer.recognize_google(audio_data)

def summarize_text(text):
    response = model.generate_content(f"Summarize this professionally:\n{text}")
    return response.text

def convert_video_to_audio(video_path):
    clip = VideoFileClip(video_path)
    audio_path = tempfile.mktemp(suffix=".wav")
    clip.audio.write_audiofile(audio_path)
    return audio_path

st.title("🎙️ Voice & Video Summarizer (Gemini)")

uploaded_file = st.file_uploader("Upload audio/video file", type=["wav", "mp3", "m4a", "mp4", "mov"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    file_type = uploaded_file.type

    if "video" in file_type:
        st.info("Extracting audio from video...")
        audio_path = convert_video_to_audio(tmp_path)
    else:
        audio_path = tmp_path

    st.success("Transcribing...")
    try:
        transcript = transcribe_audio(audio_path)
        st.subheader("📝 Transcript:")
        st.write(transcript)

        summary = summarize_text(transcript)
        st.subheader("🧠 Professional Summary:")
        st.write(summary)
    except Exception as e:
        st.error(f"Error: {e}")

