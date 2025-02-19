RENDER_BACKEND_URL = "https://your-app.onrender.com/detect_language/"

import streamlit as st
import requests

st.title("Voice-Based Language Detection AI")

if st.button("Speak & Detect"):
    response = requests.get(RENDER_BACKEND_URL)
    if response.status_code == 200:
        data = response.json()
        st.write(f"Detected Text: {data['text']}")
        st.write(f"Detected Language: {data['language']}")
    else:
        st.write("Error in processing")
