from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb #pip install stegano

root=Tk()
root.title("Steganography - Hide a a message in an Image")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#2f4155")



#icon
image_icon=PhotoImage(file="")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="")
Label(root,image=logo,bg="#2f4145").place(x=10,y=0)

Label(root,text="CYBER SCIENCE", bg="#2d4145",fg="white",font="arial 15 bold").place(x=100,y=20)

#first frame
f=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
f.place(x=10,y=80)

#second frame




root.mainloop()