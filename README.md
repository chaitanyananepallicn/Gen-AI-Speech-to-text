# Gemini Speech-to-Text Transcriber

A web application built with Python and Streamlit that uses Google's Gemini Pro model to transcribe spoken words from audio files into text.



***

## Live Application

**You can access a live deployed demo here:**
[**➡️ Live Transcription App**](https://gen-ai-speech-to-text.onrender.com) ***

## Features

* **Accurate Transcription**: Leverages the powerful multimodal capabilities of the Gemini API to achieve high-quality transcriptions.
* **Audio File Uploader**: Allows users to easily upload their audio files (e.g., MP3, WAV, OGG) directly in the browser.
* **Simple Interface**: A clean and straightforward UI built with Streamlit for a seamless user experience.
* **Copy to Clipboard**: Easily copy the transcribed text with a single click.

***

## Tech Stack

* **Core Language**: Python
* **Web Framework**: Streamlit
* **AI Model**: Google Gemini Pro
* **Libraries**: `google-generativeai`

***

## Getting Started

To run this project on your local machine, follow these steps.

### Prerequisites

Make sure you have Python 3.8+ and pip installed on your system.

### Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/chaitanyananepallicn/Gen-AI-Speech-to-text.git
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd gemini-speech-to-text
    ```

3.  **Create and activate a virtual environment (Recommended):**
    * **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

4.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up your environment variables:**
    * Get your free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
    * Create a file named `.env` in the root project directory.
    * Add your API key to the `.env` file:
        ```
        GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```

6.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    * After running the command, open your web browser and navigate to the local URL provided (usually `http://localhost:8501`).
