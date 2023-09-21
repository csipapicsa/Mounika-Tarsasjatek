import win32com.client

def text_to_speech(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Voice = speaker.GetVoices().Item(0)  # Select the first Danish voice
    
    
    voices = speaker.GetVoices()
    for i in range(voices.Count):
        print(voices.Item(i))
        
    speaker.Speak(text)

text_to_speech("Hej, hvordan har du det?")