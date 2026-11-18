from tkinter import * 
import qrcode #pip install qrcode


root=Tk()
root.title("QR Code Generator")
root.geometry("1000x550")
root.configure(bg="#AE2321")
root.resizable(False,False)


#icon image
image_icon=PhotoImage(file="")
root.iconphoto(False,image_icon)


def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("qrcode/"+ str(name)+".png")

    global Image
    Image=PhotoImage(file="qrcode/"+ str(name)+".png")
    Image_view.config(image=Image)


Image_view=Label(root,bg="#AE2321").pack(padx=50,pady=10,side="right")


Label(root,text="title",fg="white",bg="#AE2321",font=15).place(x=50,y=170)

title=Entry(root,width=13,font=("arial 15")).place(x=50,y=200)

entry=Entry(root,width=28,font="arial 15").place(x=50,y=250)

Button(root,text="Gneerate",width=20,height=2,bg="black",fg="white",command=generate).place(x=50,y=300)


root.mainloop()
