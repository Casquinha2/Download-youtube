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
        self.botaoambos = tk.Button(self.frame, text="Download do video e do audio", width= 25, height=5, command=self.ambos)
        
        self.botaoaudio = tk.Button(self.frame, text = "Download do audio", width= 25, height=5, command=self.audio)
        
        self.botaovideo = tk.Button(self.frame, text = "Download do video", width= 25, height=5, command=self.video)

        #Text box
        self.texto = tk.Entry(self.frame, width=100)

        self.label = tk.Label(self.frame, text="Introduza, aqui em baixo, o URL do video que quer fazer download do YouTube",font=('areal black',13), bg='#99D9EA')
        
        #packs
        self.label.place(x=600, y=125,anchor=tk.CENTER)
        self.texto.place(x=600, y=175,anchor=tk.CENTER)
        self.botaoambos.place(x=600,y=400, anchor=tk.CENTER)
        self.botaoaudio.place(x=900, y=400, anchor=tk.CENTER)
        self.botaovideo.place(x=300, y=400, anchor=tk.CENTER)


    def ambos(self):

        file = self.texto.get()
        lista = Controller.Controller.list_res(file)

        self.nova_janela = tk.Toplevel(self.master)

        self.nova_janela = tk.Frame(self.nova_janela, width=960, height=600, bg='#FFFFFF')
        self.nova_janela.pack_propagate(False)
        self.nova_janela.pack()
        
        self.listbox = tk.Listbox(self.nova_janela, width= 100)

        i=1
        for j in lista:
            self.listbox.insert(i, j)
            i+=1
        
        self.listbox.pack()


        #for i in lista:
        #    print(i)




    def audio(self):
        return None
    
    def video(self):
        return None