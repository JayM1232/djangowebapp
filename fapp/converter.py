import moviepy.editor as mp
import os
class Conv:
    def __init__(self,fil,user_file):
        if user_file == '' or user_file == None:
            self.clip = mp.VideoFileClip(f'Download/{fil}.mp4')
            if os.path.isdir('Download/YoutubeAllAudios') == False:
                path = os.path.join('Download/YoutubeAllAudios')
                os.mkdir(path)
            self.clip.audio.write_audiofile(f'Download/YoutubeAllAudios/{fil}.wav', codec='pcm_s16le')
        else:
            self.clip = mp.VideoFileClip(f'Download/{fil}.mp4')
            if os.path.isdir('Download/YoutubeAllAudios') == False:
                path = os.path.join('Download/YoutubeAllAudios')
                os.mkdir(path)
            self.clip.audio.write_audiofile(f'Download/YoutubeAllAudios/{user_file}.wav', codec='pcm_s16le')