from tkinter import *
from datetime import date

root=Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("Age Calculator")

photo=PhotoImage(file="age_calculator.png")
myimage=Label(image=photo)
myimage.pack(padx=15,pady=15)

def calculateAge():
    today=date.today()
    birthDate=date(int(yearValue.get()),int(monthValue.get()),int(dayValue.get()))
    age=today.year - birthDate.year - ((today.month, today.day) < ( birthDate.month, birthDate.day))
    Label(text=f"{nameValue.get()} is {age} years old",font=23).place(x=300,y=500)

Label(text="Name", font=23).place(x=200,y=250)
Label(text="Year", font=23).place(x=200,y=300)
Label(text="Month", font=23).place(x=200,y=350)
Label(text="Day", font=23).place(x=200,y=400)

nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()

nameEntry=Entry(textvariable=nameValue,width=30,bd=3,font=23).place(x=300,y=250)
yearEntry=Entry(textvariable=yearValue,width=30,bd=3,font=23).place(x=300,y=300)
monthEntry=Entry(textvariable=monthValue,width=30,bd=3,font=23).place(x=300,y=350)
dayEntry=Entry(textvariable=dayValue,width=30,bd=3,font=23).place(x=300,y=400)


Button(text="Calculate Age",font=23,bg="black",fg="white",width="11",height="2",command=calculateAge()).place(x=300,y=450)


root.mainloop()