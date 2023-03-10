from pytube import YouTube, Playlist
import os
from time import time
start = time()

print("Type V for single piece of video | Type MP for music playlist | Type M for music piece")
decide = input("What format you want to download: ")
videoDownload = "C:\\Users\\levym.LAPTOP-4G8NP567\\Videos\\Raw video"
songDownload = "C:\\Users\\levym.LAPTOP-4G8NP567\\Music\\Levy Music"

def Download(l):
    if (decide.lower() == "v"):
        yt = YouTube(l)
        yt = yt.streams.get_highest_resolution()
        try: 
            yt.download(output_path=videoDownload)
        except:
            print("The downlaod failed")
        print("the download is completed")
    elif (decide.lower() == "mp"):
        try:
            playlist = Playlist(l)
            print("The Playlist have a "+ str(len(playlist.video_urls))+ " songs ")
            urls = playlist.video_urls

            for url in urls:
                title = YouTube(url).title
                print(title)

            for video in playlist.videos:
                audioStream = video.streams.filter(only_audio=True).first()
                levy = audioStream.download(output_path=songDownload)
                base, ext = os.path.splitext(levy)
                new_file = base + '.mp3'
                os.rename(levy, new_file)
        except:
            print("Code Mp fail")

    elif (decide.lower() == "m"):
        yet = YouTube(l)
        video = yet.streams.filter(only_audio=True).first()
        try:
            oneMusic = video.download(output_path=songDownload)
            base, ext = os.path.splitext(oneMusic)
            new_file = base + '.mp3'
            os.rename(oneMusic, new_file)     
        except:
            print("The downlaod failed")
        print("the download is completed")
   


l = input("Input the link: ")
Download(l)
print(f'Time taken: {time() - start}')