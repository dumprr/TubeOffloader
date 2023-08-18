from pytube import Playlist
import time

print("\n\nRunning playlist downloader.\nMade by Dumprr | Powered by PyTube\n")

def Download(link):
    list = Playlist(link)
    print("\n\nDownloading \"" + list.title + "\"")
    time.sleep(1)
    try:
        for video in list.videos:
            video.streams.first().download()
            print(video.streams.first().title)
    except:
        print("Whoops, something went wrong!")
    print("\n\nTask finished. Video saved in script directory.")



link = input("Video URL?\n")
Download(link)