import os
import re
import yt_dlp

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def formattedYoutubeTitle(title):
    title = re.sub(r'[^\w\s-]', '', title).strip().lower()
    title = re.sub(r'[-\s]+', '-', title)
    return title

def getDocumentsFolderPath():
    return os.path.join(os.path.expanduser("~"), "Documents")

def getMidiaFolderPath():
    return os.path.join(getDocumentsFolderPath(), "Midia")

def getAudioFolderPath():
    return os.path.join(getMidiaFolderPath(), "Audio")

def getVideoFolderPath():
    return os.path.join(getMidiaFolderPath(), "Video")

def createFolders():
    os.makedirs(getMidiaFolderPath(), exist_ok=True)
    os.makedirs(getAudioFolderPath(), exist_ok=True)
    os.makedirs(getVideoFolderPath(), exist_ok=True)

def getYouTubeDownload(url, type):
    audioPath = getAudioFolderPath()
    videoPath = getVideoFolderPath()
    createFolders()
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
        
        orignalTitle = info.get('title', 'video')
        formattedTitle = formattedYoutubeTitle(orignalTitle)

        if type == '1':
            outputAudioFilePath = os.path.join(audioPath, f"{formattedTitle}.%(ext)s")
            ydlOptions = {
                'format': 'bestaudio/best',
                'outtmpl': outputAudioFilePath,
                'quiet': False,
                'noplaylist': True,
                'no_warnings': True,
                'progress_with_newline': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'm4a',
                    'preferredquality': '192',
                }]
            }

                    
            with yt_dlp.YoutubeDL(ydlOptions) as ydl:
                ydl.download([url])

            clearConsole()
            print(f"Áudio '{formattedTitle}.m4a' baixado com sucesso em: {audioPath}")

        elif type == '2':
            outputVideoFilePath = os.path.join(videoPath, f"{formattedTitle}.%(ext)s")
            ydlOptions = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': outputVideoFilePath,
                'quiet': False,
                'noplaylist': True,
                'no_warnings': True,
                'progress_with_newline': True,
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }]
            }

            with yt_dlp.YoutubeDL(ydlOptions) as ydl:
                ydl.download([url])

            clearConsole()
            print(f"Vídeo '{formattedTitle}.mp4' baixado com sucesso em: {videoPath}")
        
        else:
            clearConsole()
            print("Tipo de download inválido! Digite 1 para áudio ou 2 para vídeo.")

    except Exception as e:
        clearConsole()
        print(f"Erro ao fazer o download do áudio! {e}")

clearConsole()
url = str(input("Digite a URL do vídeo do YouTube: "))
type = str(input("Digite o tipo de download (1 para áudio, 2 para vídeo): "))
getYouTubeDownload(url, type)