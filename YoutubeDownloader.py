from pytube import YouTube

#ask for the link from user
link = input("Insira o link do Vídeo:  ")
yt = YouTube(link)

#Showing details
print("Título: ",yt.title)
print("Número de Views: ",yt.views)
print("Tamanho do video: ",yt.length)
print("Avaliação do video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completo!!")

input("Aperte qualquer tecla para fechar o programa! Obrigado por usá-lo")