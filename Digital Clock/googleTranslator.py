from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='aqua')

lab_txt=Label(root,text="Translator",font=("Time New Roman",40,"bold"),fg="White",bg="Black")
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg="White",bg="Black")
lab_txt.place(x=100,y=100,height=30,width=300)


root.mainloop()


