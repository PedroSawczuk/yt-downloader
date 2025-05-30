import os

def getDocumentsFolderPath():
    return os.path.join(os.path.expanduser("~"), "Documents")

def getMidiaFolderPath():
    return os.path.join(getDocumentsFolderPath(), "Midia")

def getAudioFolderPath():
    return os.path.join(getMidiaFolderPath(), "Audio")

def getVideoFolderPath():
    return os.path.join(getMidiaFolderPath(), "Video")