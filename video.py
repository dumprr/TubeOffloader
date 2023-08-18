from pytube import Playlist, YouTube
import time

print("\n\nRunning single-video downloader.\nMade by Dumprr | Powered by PyTube\n")

def Download(link):
    youtubeVideo = YouTube(link)
    youtubeVideo = youtubeVideo.streams.get_highest_resolution()
    print("\n\nDownloading \"" + youtubeVideo.title + "\"")
    time.sleep(1)
    try:
        youtubeVideo.download()
    except:
        print("Whoops, something went wrong!")
    print("\n\nTask finished. Video saved in script directory.")



link = input("Video URL?\n")
Download(link)