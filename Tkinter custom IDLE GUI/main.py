from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
import subprocess
import os

root=Tk()
root.title("Python IDLE")
root.geometry("1280x720+150+80")
root.configure(bg="#323846")
root.resizable(False,False)


#icon
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)


#code input
code_input = Text(root,font="consolas 18")
code_input.place(x=180,y=0,width=680,height=720)

#code output
code_output=Text(root,font="consolas 18",bg="#323846",fg="lightgreen")
code_output.place(x=860,y=0,width=420,height=720)


#buttons
Open=PhotoImage(file="open.png")
Save=PhotoImage(file="save.png")
Run=PhotoImage(file="run.png")

Button(root,image=Open,bg="#323846",bd=0,command=lambda:open_file()).place(x=30,y=30)
Button(root,image=Save,bg="#323846",bd=0,command=lambda:open_file()).place(x=30,y=145)
Button(root,image=Run,bg="#323846",bd=0,command=lambda:open_file()).place(x=30,y=260)





root.mainloop()