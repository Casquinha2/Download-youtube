from pytubefix import YouTube
from moviepy.editor import AudioFileClip, VideoFileClip
import shutil
import os


file = YouTube(input("Introduza o seu video: "))

def get_resolution(s):
    return int(s.resolution[:-1])


video = max(
    filter(lambda s: get_resolution(s) <= 1080,
           filter(lambda s: s.type == 'video', file.streams)),
    key=get_resolution
)

audio = file.streams.get_audio_only()

video.download('cache', filename='teste.mp4')
audio.download('cache',filename='teste1.mp3')

if not os.path.exists('final'):
    os.makedirs('final')

name='final/' + "Nnome" + '.mp4'

audio = AudioFileClip('cache/teste1.mp3')
video = VideoFileClip('cache/teste.mp4')
final_clip = video.set_audio(audio)
final_clip.write_videofile(filename= name, codec='libx264')


shutil.rmtree('cache')