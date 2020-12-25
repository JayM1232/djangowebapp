import youtube_dl
import speech_recognition as sr
        
class Load:
    def __init__(self,value_user):
        ydl_opts = {'outtmpl':'YoutubeAllDownloads/%(title)s.%(ext)s'}

        def dwl_vid():
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([zxt])

        channel = 1
        while (channel == int(1)):
            # link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download:- ")
            zxt = value_user.strip()

            dwl_vid()
            channel = int(0)
