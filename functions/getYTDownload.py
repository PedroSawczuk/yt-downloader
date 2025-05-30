import os
import yt_dlp
from functions import *
from functions.clearTerminal import clearConsole
from functions.formattedYtTile import *
from functions.getFolders import *

def getYouTubeDownload(url, type):
    audioPath = getAudioFolderPath()
    videoPath = getVideoFolderPath()
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
