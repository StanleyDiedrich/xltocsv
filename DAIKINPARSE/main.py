from tkinter import*
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
import xml.dom.minidom as xdm
from bs4 import BeautifulSoup
from prettifydocx import openfile
root =Tk()
root.title('DaikinParse')
icon=PhotoImage(file="capibara.png")
root.iconphoto(False,icon)
root.geometry('800x250')

label = Label(text="Выбери файл Daikin в формате .docx ")
label2 = Label(text="Если эта штука собирает ХОВС сама, то это не значит, что данные собирал грамотный пряморукий специалист")
label3 = Label(text="Проверь за собой и будь осторожен")
openfilebtn = Button(root,text="Choose files",command=openfile)
# prettifybtn = Button(text="Prepare datas")
# xlbtn = Button(text="Export in Excel",command=savefile)

label.pack()
label2.pack()
label3.pack()
openfilebtn.pack()
#xlbtn.pack()
root.mainloop()


