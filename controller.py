from view import *

from pytubefix import YouTube
from moviepy.editor import AudioFileClip, VideoFileClip
import shutil
import os

class Controller:
    def __init__(self, master):
        self.view = View(master)

    def get_resolution(s):
        return int(s.resolution[:-1])
    
    def get_abr(s):
        return int(s.abr.replace('kbps', ''))
    
    def list_res(file):
        file=YouTube(file)
        lista=[]
        for j in filter(lambda s: Controller.get_resolution(s), filter(lambda s: s.type == 'video', file.streams)):
            lista.append(j)
        lista.sort(key=Controller.get_resolution, reverse=True)
        for j in lista:
            if j.mime_type == "video/webm":
                lista.remove(j)
        return lista
    
    def list_res_audio(file):
        file=YouTube(file)
        lista=[]
        for j in filter(lambda s: Controller.get_abr(s), filter(lambda s: s.type == 'audio', file.streams)):
            lista.append(j)
        lista.sort(key=Controller.get_abr, reverse=True)
        return lista
    
    def download_ambos(file, itagvideo, itagaudio, bvideo, baudio, name):
        file=YouTube(file)
        
        if itagvideo != None:
            video = file.streams.get_by_itag(itagvideo)
        if itagaudio == None:
            audio = file.streams.get_audio_only()
        else:
            audio = file.streams.get_by_itag(itagaudio)
         
        

        if bvideo and baudio:
            video.download('cache', filename='teste.mp4')
            audio.download('cache',filename='teste1.mp3')

            if not os.path.exists('final'):
                os.makedirs('final')

            if name == "":
                name = str(file.title)
                name = 'final/' + name + '.mp4'
            else:
                name='final/' + name + '.mp4'

            audio = AudioFileClip('cache/teste1.mp3')
            video = VideoFileClip('cache/teste.mp4')
            final_clip = video.set_audio(audio)
            final_clip.write_videofile(filename= name, codec='libx264')

            shutil.rmtree('cache')

        elif bvideo:
            if not os.path.exists('final'):
                os.makedirs('final')
            
            name = name + '.mp4'

            video.download('final', filename=name)


        elif baudio:
            if not os.path.exists('final'):
                os.makedirs('final')
            
            name = name + '.mp3'

            audio.download('final', filename=name)
    
    def download_audio(file): ##acabar casa
        file.video
