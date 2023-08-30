from pytube import Playlist, YouTube
import tkinter as tk
from tkinter import font 
import time
import webbrowser

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


def window():
    window = tk.Tk()
    window.title("TubeOffloader")
    window.geometry("540x250")
    window.resizable(False, False)

    titletextsize = 12
    desctextsize = 8
    
  
    textfont = "Verdana"


    def callback(url):
     webbrowser.open_new_tab(url)

    title = tk.Label(window, text="Tube Offloader by Dumprr", font=(textfont, titletextsize))
    title.pack(pady=20)
    title.bind("<Button-1>", lambda e:
    callback("https://github.com/dumprr/TubeOffloader"))

  
    desc = tk.Label(window, text="Download any YouTube video!", font=(textfont, desctextsize))
    desc.pack(pady=0)
    desc = tk.Label(window, text="Put the Video URL in the link below:", font=(textfont, desctextsize))
    desc.pack(pady=10)
   
    URL_box = tk.Text(window, height=2, width=60, font=("Verdana", 10))
    URL_box.pack()
    desc = tk.Label(window, text="The app will freeze while downloading the video, don't worry, it won't take that long.", font=(textfont, desctextsize))
    desc.pack(pady=10)
    button = tk.Button(window, text="Download", command=lambda: Download(URL_box.get("1.0",'end-1c')))
    button.pack(pady=10)
    
    
    window.mainloop()

window()

