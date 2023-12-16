# https://github.com/markhliu/mpt/blob/master/ch03/stand_by.py

import speech_recognition as sr

speech = sr.Recognizer()
while True:
    print('Python is listening...')
    inp = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            inp = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    print(f'You just said {inp}.')
    if inp == "stop listening":
        print('Goodbye!')
        break

'''
Important:
Sometimes the speech recognition takes a long time to process, especially if there is
ambient noise and the internet connection is slow. Try to test the script in a quiet
place with a good internet connection.
'''