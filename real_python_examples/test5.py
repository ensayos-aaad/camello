import speech_recognition as sr

r = sr.Recognizer()
audio_file = sr.AudioFile('trabalenguas.wav')
with audio_file as source:
    audio = r.record(source)
    text = r.recognize_google(audio, language='es-CO')
    print(text)