from tkinter import *
import os


root=Tk()
root.title("Shutdown app")
root.geometry("400x580")


def restarttime():
    os.system("shutdown /r /t 30")

def restart():
    os.system("shutdown /r /t 1")

def shutdown():
    os.system("shutdown /s /t 1")

def logout():
    os.system("shutdown -l")


#first button
restart_time_button=PhotoImage(file="restart_time.png")
first_button=Button(root,image=restart_time_button,borderwidth=0,cursor="hand2",command=restarttime)
first_button.place(x=10,y=10)

#second button
close_button=PhotoImage(file="close.png")
second_button=Button(root,image=close_button,borderwidth=0,cursor="hand2",command=root.destroy)
second_button.place(x=200,y=10)

#third button
restart_button=PhotoImage(file="restart.png")
third_button=Button(root,image=restart_button,borderwidth=0,cursor="hand2",command=restart)
third_button.place(x=10,y=200)

#fourth button
shutdown_button=PhotoImage(file="shutdown.png")
fourth_button=Button(root,image=shutdown_button,borderwidth=0,cursor="hand2",command=logout)
fourth_button.place(x=200,y=200)

#fifth button
logout_button=PhotoImage(file="logout.png")
fifth_button=Button(root,image=logout_button,borderwidth=0,cursor="hand2",command=shutdown)
fifth_button.place(x=10,y=400)


root.mainloop()