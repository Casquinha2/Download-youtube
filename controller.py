from view import *

from pytubefix import YouTube, Playlist
from moviepy.editor import AudioFileClip, VideoFileClip
import shutil
import os
import logging

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
            name='final/' + name + '.mp4'

            audio = AudioFileClip('cache/teste1.mp3')
            video = VideoFileClip('cache/teste.mp4')
            final_clip = video.set_audio(audio)
            final_clip.write_videofile(filename= name, codec='libx264')

            shutil.rmtree('cache')

        elif bvideo:
            if not os.path.exists('final'):
                os.makedirs('final')
            
            if name == "":
                name = str(file.title)
            
            name = name + '.mp4'

            video.download('final', filename=name)


        elif baudio:
            if not os.path.exists('final'):
                os.makedirs('final')
            
            if name == "":
                name = str(file.title)
            
            name = name + '.mp3'

            audio.download('final', filename=name)
    

    def download_audio(file1, name):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        
        try:
            file = Playlist(file1)
            logging.info(f"Playlist title: {file.title}")
            logging.info(f"Number of videos in playlist: {len(file.video_urls)}")

            if name == "":
                chars_to_remove = r'<>:"/\|?*'  # Caracteres inválidos em nomes de arquivo
                name = Controller.remove_special_characters(str(file.title), chars_to_remove)
            location = os.path.join('final', name)

            if not os.path.exists(location):
                os.makedirs(location)


            if not os.path.exists('cache'):
                os.makedirs('cache')


            for index, video_url in enumerate(file.video_urls):
                try:
                    yt = YouTube(video_url)
                    logging.info(f"Processing video {index + 1}/{len(file.video_urls)}: {yt.title}")

                    highest_bitrate_audio = max(filter(lambda s: Controller.get_abr(s),
                                                filter(lambda s: s.mime_type =='audio/mp4', yt.streams)),
                                                key= Controller.get_abr)
                    
                    name_mp3 = f"{yt.title}.mp4"
                    safe_filename = "".join([c for c in name_mp3 if c.isalpha() or c.isdigit() or c in (' ', '-', '_', '.')]).rstrip()
                    
                    #highest_bitrate_audio.download(location, filename=name_mp3)

###########################################################################################################
                    highest_bitrate_audio.download('cache', filename='teste1.mp4')                      ###
                                                                                                        ###
                    if os.path.exists('cache/teste1.mp4'):                                              ###
                        audio = AudioFileClip('cache/teste1.mp4')                                       ###
                        audio.write_audiofile(f"{location}/{yt.title}.m4a", codec='aac')                ###
                    else:                                                                               ###
                        logging.error("File 'cache/teste1.mp4' not found. Unable to extract audio.")    ###
                                                                                                        ###
                    os.remove('cache')                                                                  ###
                                                                                                        ###
###########################################################################################################

                    logging.info(f"Downloaded: {safe_filename}")

                except Exception as e:
                    logging.error(f"Error downloading video {yt.title}: {str(e)}")

        except Exception as e:
            logging.error(f"Error processing playlist: {str(e)}")

        logging.info("Playlist download completed")
    
    def remove_special_characters(text, chars_to_remove):

        trans_table = str.maketrans('', '', chars_to_remove)
        return text.translate(trans_table)