from langdetect import detect  

def detect_language(text):
    try:
        return detect(text)
    except:
        return "Unknown"

if __name__ == "__main__":
    sample_text = "Bonjour, comment ça va?"
    print("Detected Language:", detect_language(sample_text))
