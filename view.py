import controller as Controller

import tkinter as tk

from pytubefix import YouTube
from moviepy.editor import AudioFileClip, VideoFileClip
import shutil
import os

class View:
    def __init__(self, master):
        

        self.master = master

        #Frame
        self.master.resizable(False, False)
        self.frame = tk.Frame(self.master, width=1200, height=800, bg='#99D9EA')
        self.frame.pack_propagate(False)
        self.frame.pack()

        #botao
        botaoambos = tk.Button(self.frame, text="Download do video e do audio", width= 25, height=5, command=self.ambos)
        botaoaudio = tk.Button(self.frame, text = "Download do audio", width= 25, height=5, command=self.audio)
        botaovideo = tk.Button(self.frame, text = "Download do video", width= 25, height=5, command=self.video)
        botaoplaylist = tk.Button(self.frame, text = "Playlist", width=25, height=5, command=self.playlist)

        #Text box
        self.texto = tk.Entry(self.frame, width=100)

        label = tk.Label(self.frame, text="Introduza, aqui em baixo, o URL do video que quer fazer download do YouTube",font=('areal black',13), bg='#99D9EA')
        
        #packs
        label.place(x=600, y=125,anchor=tk.CENTER)
        self.texto.place(x=600, y=175,anchor=tk.CENTER)
        botaoambos.place(x=600,y=400, anchor=tk.CENTER)
        botaoaudio.place(x=900, y=400, anchor=tk.CENTER)
        botaovideo.place(x=300, y=400, anchor=tk.CENTER)
        botaoplaylist.place(x=600, y=650, anchor=tk.CENTER)

        #vars
        self.bvideo = False
        self.baudio = False
        self.link_playlist = False

    def playlist(self):
        self.frame.destroy()

        self.pl_janela = tk.Frame(self.master, width=1200, height=800, bg='#99D9EA')
        self.pl_janela.pack_propagate(False)
        self.pl_janela.pack()

        #botao
        ##botaoambos = tk.Button(self.pl_janela, text="Download do video e do audio", width= 25, height=5, command=self.ambos)
        botaoaudio = tk.Button(self.pl_janela, text = "Download do audio", width= 25, height=5, command=self.audio)
        ##botaovideo = tk.Button(self.pl_janela, text = "Download do video", width= 25, height=5, command=self.video)
        botaoalone = tk.Button(self.pl_janela, text = "Só um video", width=25, height=5, command=self.inicio)

        #Text box
        self.texto = tk.Entry(self.pl_janela, width=100)

        label = tk.Label(self.pl_janela, text="Introduza, aqui em baixo, o URL da playlist que quer fazer download do YouTube",font=('areal black',13), bg='#99D9EA')
        
        #packs
        label.place(x=600, y=125,anchor=tk.CENTER)
        self.texto.place(x=600, y=175,anchor=tk.CENTER)
        ##botaoambos.place(x=600,y=400, anchor=tk.CENTER)
        botaoaudio.place(x=600, y=400, anchor=tk.CENTER)
        ##botaovideo.place(x=300, y=400, anchor=tk.CENTER)
        botaoalone.place(x=600, y=650, anchor=tk.CENTER)

        #vars
        self.bvideo = False
        self.baudio = False
        self.link_playlist = True

    
    def ambos(self):

        self.file = self.texto.get()
        self.lista = Controller.Controller.list_res(self.file)

        self.nova_janela = tk.Toplevel(self.master)

        frame1 = tk.Frame(self.nova_janela, width=960, height=600, bg='#FFFFFF')
        frame1.pack_propagate(False)
        frame1.pack()
        
        #listbox
        self.listbox = tk.Listbox(frame1, width= 50, height= 20)

        #botao
        botao = tk.Button(frame1, text="Selecionar qualidade", width= 25, height=5, command=self.download)

        #Text box
        self.name = tk.Entry(frame1, width=100)

        #label
        label = tk.Label(frame1, text="Nome do ficheiro",font=('areal black',13), bg='#FFFFFF')

        #set listbox
        i=1
        for j in self.lista:
            res = f'''res: {j.resolution}; {str(j.fps)}fps; {j.mime_type}; vcodec: "{j.video_codec}"'''
            self.listbox.insert(i, res)
            i+=1
        
        #packs
        self.listbox.place(x=480, y=200, anchor=tk.CENTER)
        label.place(x=480, y=400, anchor=tk.CENTER)
        self.name.place(x=480, y=450, anchor=tk.CENTER)
        botao.place(x=480, y = 525, anchor=tk.CENTER)

        #var
        self.bvideo = True
        self.baudio = True

    def audio(self):   ##fazer isto em casa!!!
        self.file = self.texto.get()

        self.nova_janela = tk.Toplevel(self.master)

        frame2 = tk.Frame(self.nova_janela, width=960, height=600, bg='#FFFFFF')
        frame2.pack_propagate(False)
        frame2.pack()

        
               

        #botao
        botao = tk.Button(frame2, text="Selecionar qualidade", width= 25, height=5, command=self.download)

        #Text box
        self.name = tk.Entry(frame2, width=100)

        #label
        label = tk.Label(frame2, text="Nome do ficheiro",font=('areal black',13), bg='#FFFFFF')

        if self.link_playlist != True:
            self.lista = Controller.Controller.list_res_audio(self.file)

            #listbox
            self.listbox = tk.Listbox(frame2, width= 50, height= 20)

            #set listbox
            i=1
            for j in self.lista:
                res = f'''res: {j.abr}; {j.mime_type}"'''
                self.listbox.insert(i, res)
                i+=1

            #packs
            self.listbox.place(x=480, y=200, anchor=tk.CENTER)
            label.place(x=480, y=400, anchor=tk.CENTER)
            self.name.place(x=480, y=450, anchor=tk.CENTER)
            botao.place(x=480, y = 525, anchor=tk.CENTER)

        else:
            label.place(x=480, y=100, anchor=tk.CENTER)
            self.name.place(x=480, y=150, anchor=tk.CENTER)
            botao.place(x=480, y = 225, anchor=tk.CENTER)

        #var
        self.bvideo = False
        self.baudio = True


    
    def video(self):
        self.file = self.texto.get()
        self.lista = Controller.Controller.list_res(self.file)

        self.nova_janela = tk.Toplevel(self.master)

        frame1 = tk.Frame(self.nova_janela, width=960, height=600, bg='#FFFFFF')
        frame1.pack_propagate(False)
        frame1.pack()
        
        #listbox
        self.listbox = tk.Listbox(frame1, width= 50, height= 20)

        #botao
        botao = tk.Button(frame1, text="Selecionar qualidade", width= 25, height=5, command=self.download)

        #Text box
        self.texto = tk.Entry(frame1, width=100)

        #label
        label = tk.Label(frame1, text="Nome do ficheiro",font=('areal black',13), bg='#FFFFFF')

        #set listbox
        i=1
        for j in self.lista:
            res = f'''res: {j.resolution}; {str(j.fps)}fps; {j.mime_type}; vcodec: "{j.video_codec}"'''
            self.listbox.insert(i, res)
            i+=1
        
        #packs
        self.listbox.place(x=480, y=200, anchor=tk.CENTER)
        label.place(x=480, y=400, anchor=tk.CENTER)
        self.name.place(x=480, y=450, anchor=tk.CENTER)
        botao.place(x=480, y = 525, anchor=tk.CENTER)

        #var
        self.bvideo = True
        self.baudio = False

    def download(self):
        if self.link_playlist:  ##acaaber casa

            Controller.Controller.download_audio(self.file, self.name.get())
        else:

            opcion = self.listbox.curselection()
            
            if opcion:
                opcion = self.listbox.get(opcion)
            
            if self.bvideo:
                for j in self.lista:
                    correto = f'''res: {j.resolution}; {str(j.fps)}fps; {j.mime_type}; vcodec: "{j.video_codec}"'''
                    if opcion == correto:
                        for i in YouTube(self.file).streams:
                            if j.resolution == i.resolution and j.fps == i.fps and j.mime_type == i.mime_type and j.video_codec == i.video_codec:
                                itagvideo = i.itag
                itagaudio = None
            elif self.baudio:
                for j in self.lista:
                    correto = f'''res: {j.abr}; {j.mime_type}"'''
                    if opcion == correto:
                        for i in YouTube(self.file).streams:
                            if j.abr == i.abr and j.mime_type == i.mime_type:
                                itagaudio = i.itag
                itagvideo = None

            Controller.Controller.download_ambos(self.file, itagvideo, itagaudio, self.bvideo, self.baudio, self.name.get())

            

        self.nova_janela.destroy()

        self.bvideo = False
        self.baudio = False
        self.link_playlist = False

    

    def inicio(self):
        self.pl_janela.destroy()
        self.__init__(self.master)