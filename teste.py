from pytubefix import YouTube
from moviepy.editor import concatenate_videoclips, AudioFileClip, VideoFileClip
import shutil

file = YouTube(input("Introduza o seu video: "))

# little utility to parse out the resolution from a stream description like 1440p
def get_resolution(s):
    return int(s.resolution[:-1])


video = max(
    filter(lambda s: get_resolution(s) <= 1080,  # filter out sub-1080p streams
           filter(lambda s: s.type == 'video', file.streams)), # filter out the video streams
    key=get_resolution  # maximum resolution among those streams
)

##video = file.streams.get_highest_resolution()
audio = file.streams.get_audio_only()

video.download('cache', filename='teste.mp4')
audio.download('cache',filename='teste1.mp3')

audio = AudioFileClip('cache/teste1.mp3')
video = VideoFileClip('cache/teste.mp4')
final_clip = video.set_audio(audio)
final_clip.write_videofile('videocomsom.mp4', codec='libx264')


shutil.rmtree('cache')

