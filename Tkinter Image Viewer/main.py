from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os

def showimage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",filetypes=(("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
    img=Image.open(filename)
    img.ImageTk.PhotoImage(img)
    lbl.configure(image=img)


root=Tk()

fram=Frame(root)
fram.pack(side="bottom",padx=15,pady=15)

lbl=Label(root)
lbl.pack()

btn=Button(fram,text="Select Image",command=showimage)
btn.pack(side=Tk.LEFT)

btn=Button(fram,text="Exit",command=lambda:exit())
btn.pack(side=Tk.LEFT,padx=12)

root.title("Image Viewer")
root.geometry("400x450")



root.mainloop()