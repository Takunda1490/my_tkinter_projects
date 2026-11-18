from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox,filedialog
import tkinter as tk

import speech_recognition as sr
import PyPDF2
import pyttsx3
import os

import googletrans
from googletrans import Translator

import datetime
from gtts import gTTS
from playsound import playsound
import threading


framebg="#161d3f"
bodybg="#84a1e8"


root=Tk()
root.title("Text Manipulation Tool")
root.geometry("1030x570+290+140")
root.resizable(False,False)


#icon
image_icon=PhotoImage(file="")
root.iconphoto(False,image_icon)

#Top frame
Top_frame = Frame(root,bg=framebg,width=1100,height=130,)
Top_frame.place(x=0,y=0)

logo_icon=PhotoImage(file="")
Label(Top_frame,image=logo_icon,bg=framebg).place(x=40,y=20)


Label(Top_frame,text="TEXT MANIPULATION TOOL",font="arial 20 bold",bg=framebg,fg="#fff").place(x=190,y=40)

#Text Area
text_area=Text(root,font="Roboto 20",bg="#cbe7c2",relief="groove",wrap=WORD)
text_area.place(x=40,y=140,width=600,height=200)


#languages comboboxes
language = googletrans.LANGUAGES
languageV = list(language.values())


combo1=ttk.Combobox(root,values=languageV,font="Roboto 10",state="r",width="10")
combo1.place(x=200,y=100)
combo1.set("ENGLISH")

combo=ttk.Combobox(root,values=languageV,font="Roboto 10",state="r",width="10")
combo.place(x=330,y=100)
combo.set("ENGLISH")


text_area=Text(root,font="Roboto 20",bg="#dddaf5",relief="groove",wrap=WORD)
text_area.place(x=40,y=140,width=600,height=200)


#voice and speed labels and controls
Label(root,text="VOICE",font="arial 15 bold",bg=bodybg,fg="white").place(x=700,y=200)
Label(root,text="SPEED",font="arial 15 bold",bg=bodybg,fg="white").place(x=700,y=250)


gender_combobox=Combobox(root,values=["Male","Female"],font="arial 14",state="r",width=40)
gender_combobox.place(x=800,y=200)
gender_combobox.set("Male")

#voice speed slider

current_value=tk.DoubleVar()

def get_current_value():
    return "{: .2f}".format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())


style=ttk.Style()
style.configure("TScale",background=bodybg)

slider=ttk.Scale(root,from_=30,to_=50,orient="horizontal",command=slider_changed,variable=current_value)

value_label=ttk.Label(root,text=get_current_value())
value_label.place(x=905,y=255)

#Buttons
image_icon=PhotoImage(file="")
btn=Button(root,compound=LEFT,image=image_icon,width=130,bg=bodybg,bd=0)
btn.place(x=700,y=380)


image_icon2=PhotoImage(file="")
save=Button(root,compound=LEFT,image=image_icon2,width=130,bg=bodybg,bd=0)
save.place(x=850,y=380)


pdfupload=PhotoImage(file="")
upload_pdf_btn=Button(root,image=pdfupload,bg=bodybg,bd=0)
upload_pdf_btn(x=700,y=57)


audioupload=PhotoImage(file="")
upload_audio_btn=Button(root,image=audioupload,bg=bodybg,bd=0)
upload_audio_btn(x=630,y=57)


transimage=PhotoImage(file="")
trans_btn=Button(root,image=transimage,bg=bodybg,bd=0)
trans_btn(x=550,y=60)


speakimage=PhotoImage(file="")
speak_btn=Button(root,image=speakimage,bg="#dddaf5",bd=0)
speak_btn(x=50,y=525)


micimage=PhotoImage(file="")
mic_btn=Button(root,image=micimage,bg="#dddaf5",bd=0)
mic_btn(x=50,y=305)


#PDF and Text mode button
button_mode=True
choice="Text"


def changemode():

    global button_mode
    global choice

    if button_mode:
        choice="PDF"
        mode.config(image=pdfmode,activebackground="white")
        button_mode=False
    else:
        choice="Text"
        mode.config(image=textmode,activebackground="white")
        button_mode=True


textmode=PhotoImage(file="")
pdfmode=PhotoImage(file="")
mode=Button(root,image=textmode,bg=framebg,bd=0,command=changemode)
mode.place(x=780,y=40)


root.mainloop()
#pip install virtualenv
