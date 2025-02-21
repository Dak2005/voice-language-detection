import speech_recognition as sr
from langdetect import detect
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        language = detect(text)
        return text, language
    except Exception as e:
        return None, str(e)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Speech Language Detector</title>
        <script>
            async function detectLanguage() {
                const response = await fetch('/detect', { method: 'POST' });
                const data = await response.json();
                document.getElementById('output').innerText = 'Detected Language: ' + data.language + '\\nText: ' + data.text;
            }
        </script>
    </head>
    <body>
        <h1>Speak to Detect Language</h1>
        <button onclick="detectLanguage()">Start Detection</button>
        <p id="output"></p>
    </body>
    </html>
    '''

@app.route('/detect', methods=['POST'])
def detect_language():
    text, language = recognize_speech()
    return jsonify({'text': text, 'language': language})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
