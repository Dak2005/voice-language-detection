from fastapi import FastAPI
from speech_to_text import recognize_speech
from detect_language import detect_language

app = FastAPI()

@app.get("/detect_language/")
def get_language():
    text = recognize_speech()
    language = detect_language(text)
    return {"text": text, "language": language}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # This handles requests to the root URL
def home():
    return {"message": "Language Detection API is running!"}
