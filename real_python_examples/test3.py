# https://realpython.com/python-speech-recognition/
# https://www.voiptroubleshooter.com/open_speech/index.html

import speech_recognition as sr

r = sr.Recognizer()
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source, offset=4, duration=3)
    text = r.recognize_google(audio)
    print(text)