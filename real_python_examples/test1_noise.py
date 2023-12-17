# https://realpython.com/python-speech-recognition/
# https://www.voiptroubleshooter.com/open_speech/index.html

import speech_recognition as sr

r = sr.Recognizer()
jackhammer = sr.AudioFile('jackhammer.wav')
with jackhammer as source:
    audio = r.record(source)
    print(r.recognize_google(audio))
