from view import *

class Controller:
    def __init__(self, master):
        self.view = View(master)

    def get_resolution(s):
        return int(s.resolution[:-1])
    
    def list_res(file):
        file=YouTube(file)
        lista=[]
        for j in filter(lambda s: Controller.get_resolution(s), filter(lambda s: s.type == 'video', file.streams)):
            lista.append(j)
        lista.sort(key=Controller.get_resolution, reverse=True)
        return lista
    
    def download_ambos(file):
        video = max(
            filter(lambda s: Controller.get_resolution(s) <= 1080,
                filter(lambda s: s.type == 'video', file.streams)),
            key=Controller.get_resolution
        )

        audio = file.streams.get_audio_only()

        video.download('cache', filename='teste.mp4')
        audio.download('cache',filename='teste1.mp3')

        if not os.path.exists('final'):
            os.makedirs('final')

        name='final/' + input("Nome do video: ") + '.mp4'

        audio = AudioFileClip('cache/teste1.mp3')
        video = VideoFileClip('cache/teste.mp4')
        final_clip = video.set_audio(audio)
        final_clip.write_videofile(filename= name, codec='libx264')

        shutil.rmtree('cache')