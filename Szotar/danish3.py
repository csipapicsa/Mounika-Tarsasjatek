import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.8)  # Volume (0.0 to 1.0)
    engine.setProperty('voice', 'da')  # Danish voice
    engine.say(text)
    engine.runAndWait()

text_to_speech("Hej, hvordan har du det?")