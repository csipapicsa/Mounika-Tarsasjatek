import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# List available voices
voices = engine.getProperty('voices')

# Find a Danish voice (you can adjust the language and name to match your installed Danish voice)
danish_voice = None
for voice in voices:
    print(voice)
    if 'Danish' in voice.languages and 'your_danish_voice_name' in voice.name:
        danish_voice = voice
        break

# Set the voice to the Danish voice
print(danish.voice)
if danish_voice:
    engine.setProperty('voice', danish_voice.id)
else:
    print("Danish voice not found on your system.")

# Set the text to be spoken
text = "Hej, hvordan har du det?"

# Convert text to speech
engine.say(text)


engine.runAndWait()