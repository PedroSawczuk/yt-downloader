from functions.clearTerminal import clearConsole
from functions.getYTDownload import getYouTubeDownload
import os
from functions.getFolders import *

def createFolders():
    os.makedirs(getMidiaFolderPath(), exist_ok=True)
    os.makedirs(getAudioFolderPath(), exist_ok=True)
    os.makedirs(getVideoFolderPath(), exist_ok=True)

clearConsole()

url = str(input("Digite a URL do vídeo do YouTube: "))
type = str(input("Digite o tipo de download (1 para áudio, 2 para vídeo): "))
getYouTubeDownload(url, type)