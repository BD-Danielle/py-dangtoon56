import os


# create subfolder
def createFolder(fldrName):
    cwd = os.getcwd()
    dir = os.path.join(cwd, fldrName)
    print(dir)
    if not os.path.exists(dir):
        os.mkdir(dir)
        os.chdir(dir)
    else:
        print('folder existed')
        os.chdir(dir)