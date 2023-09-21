import wizzi_utils as wu  # pip install wizzi_utils


def tts():
    # pip install pyttsx3 # needed
    machine_buddy = wu.tts.MachineBuddy(rate=150)
    all_voices = machine_buddy.get_all_voices(ack=True)

    print('\taudio test')
    for i, v in enumerate(all_voices):
        machine_buddy.change_voice(new_voice_ind=i)
        machine_buddy.say(text=v.name)
        print(v.name)
        if 'Hebrew' in str(v.name):
            t = 'שלום, מה קורה חברים?'
            machine_buddy.say(text=t)
    return


tts()