from pytube import YouTube
import os

# Passo 1: Ler as url dentro de um arquivo txt
# Passo 2: passar em todas as urls fazendo o download
# Passo 3: Criar um diretorio com base no atual, e salvar os videos
# Passo 4: criar um builder desse projeto para somente executar e fazer download

urlVideo =['https://www.youtube.com/live/xmtDatG6SZk?si=cO7ePDhQovkkEG_G', 'https://www.youtube.com/live/Fdoq7I39xOI?si=w4FEhudgamjMZ5V-']

print("Download iniciado")

for urlvideo in urlVideo:
    yt = YouTube(urlvideo)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    downloaded_file = video.download()
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)

    # yt = YouTube('https://youtu.be/VtdI4sfBE44?si=VpzDvtGLWs33InmT')

    # yt = YouTube('https://youtu.be/IeGSUv-y6UU?si=fusJGtH1zRAfBGiG')
    # yt.streams.filter(file_extension='webm').order_by('abr').desc().first().download()

    # Baixa somente o audio.
    # YouTube(urlvideo).streams.filter(only_audio=True).first().download()

    # obtenho o video
    # video = yt.streams.filter(only_audio=True).first()

    # realizo o dowloand
    # downloaded_file = video.download()
    # downloaded_file = yt.download()

    # Pego o arquivo e o extensão

    # base, ext = os.path.splitext(downloaded_file)

    # renomeio o arquivo para a extão que eu quero
    # new_file = base + '.mp4'

    # crio o novo arquivo.
    # os.rename(downloaded_file, new_file)

print("Download concluido")