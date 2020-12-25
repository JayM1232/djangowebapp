import moviepy.editor as mp
import os
class Conv:
    def __init__(self,fil,user_file):
        if user_file == '' or user_file == None:
            self.clip = mp.VideoFileClip(f'YoutubeAllDownloads/{fil}.mp4')
            if os.path.isdir('YoutubeAllAudios') == False:
                path = os.path.join('YoutubeAllAudios')
                os.mkdir(path)
            self.clip.audio.write_audiofile(f'YoutubeAllAudios/{fil}.wav', codec='pcm_s16le')
        else:
            self.clip = mp.VideoFileClip(f'YoutubeAllDownloads/{fil}.mp4')
            if os.path.isdir('YoutubeAllAudios') == False:
                path = os.path.join('YoutubeAllAudios')
                os.mkdir(path)
            self.clip.audio.write_audiofile(f'YoutubeAllAudios/{user_file}.wav', codec='pcm_s16le')