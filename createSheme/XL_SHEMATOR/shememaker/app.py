from tkinter import *
from ofile import openfile
from export import export




root=Tk()
root.title("Prepare csv")
root.geometry("300x200")

label=Label(text="Choose the HOVS in xlsx")
label.pack()

openfilebtn = Button(root,text="Open", command = openfile)
openfilebtn.pack()
exportbtn=Button(root,text="Export file", command =export)
exportbtn.pack()
root.mainloop()





