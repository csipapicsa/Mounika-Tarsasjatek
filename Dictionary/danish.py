import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

#voices = engine.getProperty('voices')

# print(voice for voice in voices)
# Set the voice to Danish
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_daDK_Helle')
engine.setProperty('rate', 120)  # Speed of speech

# Set the text to be spoken
text = "Hej, hvordan har du det?"


engine.say(text)

engine.runAndWait()