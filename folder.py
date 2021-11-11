import os
import promptlib


# choose folder via prompter
def chooseFolder():
    prompter = promptlib.Files()
    dir = prompter.dir()
    return dir


# create folder
def createFolder(fldrName):
    cwd = os.getcwd()
    dir = os.path.join(cwd, fldrName)
    print(dir)
    # virgin create
    if not (os.path.exists(dir)):
        os.mkdir(dir)
        os.chdir(dir)
        return True
    else:
        print('folder existed')
        os.chdir(dir)
        return False


def goMainFolder():
    os.chdir(os.pardir)