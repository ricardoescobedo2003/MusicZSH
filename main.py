from email import message
from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from plyer import notification

ventna = Tk()
ventna.title("Dowload Music v0.1")
ventna.geometry("290x200")
ventna.resizable(False, False)
   
urlEn = StringVar()
urlEntrada = Entry(ventna, textvariable=urlEn, width=40)
urlEntrada.grid(column=0, row=1)


def dowload():
     yt = YouTube(urlEn.get())
     video = yt.streams.filter(only_audio=True).first()
     out_file = video.download()
     base, ext = os.path.splitext(out_file)
     new_file = base + '.mp3'
     os.rename(out_file, new_file)
     notification.notify(
        title='Descarga Completa :D',
        message=yt.title + ' se descargo de forma correcta.',
        app_icon='/icono.webp'
     )



def dudas():
    messagebox.showinfo("TUTO", "Primero debes de dar click derecho sobre el video que estes reproduciendo; después en COPIAR URL, y finalmente lo pegas en el recuadro que se muestra.")

def mensajes():
    etq1 = Label(ventna, text="Por favor ingresa la URL del video aquí abajo :D", font="Arial 10")
    etq1.grid(column=0, row=0)
 
def cerrar():
    peticion = messagebox.askyesno('¿Salir?', 'Estás seguro que quiere salir?')
    if peticion == True:
        ventna.destroy()

def botones():
    obtener = Button(ventna, text="Comenzar Descarga", font="Arial 10", width=15, command=dowload)
    close = Button(ventna, text="Cerrar", font="Arial 10", width=14, command=cerrar)
    dudosa = Button(ventna, text="¿Como?", font="Arial 10", width=14, command=dudas)
    
    
    obtener.grid(column=0, row=2)
    dudosa.grid(column=0, row=3)
    close.grid(column=0, row=5)

botones()
mensajes()
ventna.mainloop()
