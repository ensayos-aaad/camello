# https://realpython.com/python-speech-recognition/

import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
# names_mic = sr.Microphone.list_microphone_names()
# print(names_mic)
print(mic)
with mic as source:
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)