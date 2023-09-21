import pyttsx3

engine = pyttsx3.init()

# List available voices
voices = engine.getProperty('voices')

# Find a voice by language (e.g., Danish)
desired_language = 'da-DK'  # Replace with the language code you want
selected_voice = None

for voice in voices:
    if desired_language in voice.languages:
        selected_voice = voice
        break

if selected_voice:
    engine.setProperty('voice', selected_voice.id)
else:
    print("Desired language voice not found.")

# Set the text to be spoken
text = "Hej, hvordan har du det?"

# Convert text to speech
engine.say(text)

engine.runAndWait()