import speech_recognition as sr  

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone(3) as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Could not request results"

if __name__ == "__main__":
    print("You said:", recognize_speech())
