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
        text_all = r.recognize_google(audio, show_all=True)
    except:
        text_all = ""
    print(text_all)
