# https://github.com/markhliu/mpt/blob/master/ch03/stand_by1.py

from mysr import voice_to_text

while True:
    print('Python is listening...')
    inp = voice_to_text()
    print(f'You just said {inp}.')
    if inp == "stop listening":
        print('Goodbye!')
        break