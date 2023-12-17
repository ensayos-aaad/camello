# https://realpython.com/python-speech-recognition/
# https://www.voiptroubleshooter.com/open_speech/index.html

import speech_recognition as sr

r = sr.Recognizer()
jackhammer = sr.AudioFile('jackhammer.wav')
with jackhammer as source:
    # r.adjust_for_ambient_noise(source)  # Genera que todo el audio se moche
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.record(source)
    try:
        text = r.recognize_google(audio)
    except:
        text = ""
    print(text)
