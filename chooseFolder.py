import promptlib


def chooseFolder():
    prompter = promptlib.Files()
    dir = prompter.dir()
    return dir
