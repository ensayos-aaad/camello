# https://realpython.com/python-speech-recognition/
# https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages?hl=es-419

import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
# names_mic = sr.Microphone.list_microphone_names()
# print(names_mic)
# print(mic)
with mic as source:
    r.adjust_for_ambient_noise(source)
    print('Diga algo...')
    audio = r.listen(source)
    text = r.recognize_google(audio, language='es-CO')
    print("Text: "+ text)