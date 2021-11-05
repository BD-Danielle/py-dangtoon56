from typing import Callable
from pytimedinput import timedKey


def closeInput(reminder, sec, *args):
    userText, timedOut = timedKey(reminder, timeout=sec, allowCharacters='yn')
    while True:
        if(timedOut):
            break
        else:
            if (userText == 'y'):
                # displaying non keyword arguments
                for arg in args:
                    arg()
                break
            elif (userText == 'n'):
                break
            else:
                break
