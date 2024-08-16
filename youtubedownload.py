from pytube import YouTube, Playlist
import os
import requests

print("Type V for single piece of video | Type MP for music playlist | Type M for music piece | Type VP for video playlist")
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
        yon = input("yes i want to create a new folder: ")
        newf = None
        if (yon == "yes"):
            folder_decide = str(input("add the name of you playlist: "))
            newf = videoDownload+"\\"+folder_decide
            print(newf)
        else:
            newf = videoDownload
        playlist = Playlist(l)
        print("The Playlist have a "+ str(len(playlist.video_urls))+ " songs ")
        urls = playlist.video_urls

        for url in urls:
         title = YouTube(url).title
         print(title)

        for video in playlist.videos:
            audioStream = video.streams.filter(only_audio=True).first()
            levy = audioStream.download(output_path=newf)
            base, ext = os.path.splitext(levy)
            new_file = base + '.mp3'
            os.rename(levy, new_file)
        print(playlist.title + "is done downloading")

    elif (decide.lower() == "m"):
        yet = YouTube(l)
        video = yet.streams.filter(only_audio=True).first()
        oneMusic = video.download(output_path=songDownload)
        base, ext = os.path.splitext(oneMusic)
        new_file = base + '.mp3'
        os.rename(oneMusic, new_file)     
        print("the download is completed")

    elif (decide.lower() == "vp"):
        yon = input("yes i want to create a new folder: ")
        newf = None
        if (yon == "yes"):
            folder_decide = str(input("add the name of you playlist: "))
            newf = videoDownload+"\\"+folder_decide
            print(newf)
        else:
            newf = videoDownload
        playlist = Playlist(l)
        print("The Playlist have a "+ str(len(playlist.video_urls))+ " songs ")
        urls = playlist.video_urls

        for url in urls:
         title = YouTube(url).title
         print(title)

        for video in playlist.videos:
            videostream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            levy = videostream.download(output_path=newf)
        print(playlist.title + " is done downloading")

l = input("Input the link: ")
Download(l)

