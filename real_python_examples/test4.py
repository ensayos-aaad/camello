import speech_recognition as sr

r = sr.Recognizer()
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source, offset=4.7, duration=2.8)
    text = r.recognize_google(audio)
    print(text)
