from pytimedinput import timedKey


def closeInput(reminder, sec, callback):
    userText, timedOut = timedKey(reminder, timeout=sec, allowCharacters='yn')
    while True:
        if(timedOut):
            break
        else:
            if (userText == 'y'):
                callback()
                break
            elif (userText == 'n'):
                break
            else:
                break
