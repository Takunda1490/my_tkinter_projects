from tkinter import *

#initialize the main window
root=Tk()
root.title("Registration Form")
root.geometry("600x470")
root.resizable(False,False)

def register():
    name_info=nameValue.get()
    phone_info=phoneValue.get()
    gender_info=genderValue.get()
    email_info=emailValue.get()

    file=open(name_info+".txt","w")
    file.write("Name: "+name_info+"\n")
    file.write("Phone: "+phone_info+"\n")
    file.write("Gender: "+gender_info+"\n")
    file.write("Email: "+email_info+"\n")
    file.close()

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    genderEntry.delete(0,END)
    emailEntry.delete(0,END)


    Label(text="Registration Success",fg="green",font=("arial 20")).place(x=250,y=430)

#labels
Label(root,text="Registration Form",font=("arial 25 bold")).pack(pady=50)
Label(text="Name",font=("arial 23")).place(x=100,y=150)
Label(text="Phone",font=("arial 23")).place(x=100,y=200)
Label(text="Gender",font=("arial 23")).place(x=100,y=250)
Label(text="Email",font=("arial 23")).place(x=100,y=300)

#entries
nameValue=StringVar()
phoneValue=StringVar()
genderValue=StringVar()
emailValue=StringVar()

nameEntry=Entry(root,textvariable=nameValue,width=30,font=("arial 20"),bd=2).place(x=200,y=150)
phoneEntry=Entry(root,textvariable=phoneValue,width=30,font=("arial 20"),bd=2).place(x=200,y=200)
genderEntry=Entry(root,textvariable=genderValue,width=30,font=("arial 20"),bd=2).place(x=200,y=250)
emailEntry=Entry(root,textvariable=emailValue,width=30,font=("arial 20"),bd=2).place(x=200,y=300)

#check button
checkValue=IntVar()
checkbtn=Checkbutton(text="remember me?",variable=checkValue,font=("arial 15")).place(x=200,y=340)
Button(root,text="Register",width="11",height="2",font=("arial 20"),command=register).place(x=250,y=380)



root.mainloop()