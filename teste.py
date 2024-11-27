from pytubefix import YouTube, Playlist
from moviepy.editor import AudioFileClip, VideoFileClip
import shutil
import os


file = Playlist("https://youtube.com/playlist?list=PLeFKoQ75KesBk7F1sJGSG5hEiPcw55L8t&si=NSrWYMYoCIuy_VDe")

def get_resolution(s):
    return int(s.abr.replace('kbps', ''))

for i in file.video_urls:
    i = YouTube(i)
    t = i.streams.mime_type('audio/mp4')
    print (t)


lista=[]


'''

for i in file.videos:
    for j in i.streams:

        video = max(
    filter(lambda s: get_resolution(s),
           filter(lambda s: s.type == 'audio', j)),
    key=get_resolution
)
        lista.append(video)

lista.sort(key=get_resolution, reverse=True)

i = 1
for j in lista:
    print(i, ' - ', j)
    i+=1


name = str(file.title)



def list_res(file):
        lista=[]
        for j in filter(lambda s:get_resolution(s), filter(lambda s: s.type == 'audio', file.streams)):
            lista.append(j)
        lista.sort(key=get_resolution, reverse=True)
        return lista



lista = list_res(file)


for i in file.streams:
    print(i)


##print(file.streams.get_audio_only())


temp = ""

for a in name:
    if a == ' ':
        continue
    else:
        temp += a
        ##
name = temp

print("Resultado:  "+ name)


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
'''