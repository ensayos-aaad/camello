# https://github.com/markhliu/mpt/blob/master/ch03/voice_browse.py

import webbrowser
import speech_recognition as sr

speech = sr.Recognizer()

def voice_to_text():
    voice_input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input

while True:
    print('Python is listening...')
    inp = voice_to_text()
    print(f'You just said {inp}.')
    if inp == "stop listening":
        print('Goodbye!')
        break
    elif "browser" in inp:
        inp = inp.replace('browser ','')
        # webbrowser.open("http://"+inp)
        
        continue

"""
Important: 
Don’t start speaking into the microphone before you see the message Python is
listening..., or part (or even all) of your speech may not be captured by the speech
recognition software.
"""