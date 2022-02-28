from playsound import playsound

def ps():
    playsound('mussik/sail.mp3', block=False)


ps()

while True:
    stopp = input('Stop?')
    if stopp =='y':
        break


