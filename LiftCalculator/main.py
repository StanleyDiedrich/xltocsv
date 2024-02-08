import tkinter

import dfFabric
import liftcalc
from tkinter import *
from tkinter import ttk
import re
root = Tk()
root.title("Lift Calculator")
root.geometry("800x1200")
#функции
#функция выбора из комбобокса

def selected(event):
    selection=btypescombobox.get()
    return selection

def doorwidth():
    minwidth=0.0
    maxwidth=0.0
    if "Офис" in btypescombobox.get:
        minwidth=1100
        maxwidth=1200
    if "Гостиница" in btypescombobox.getn:
        minwidth=1100
        maxwidth=1200

    if "Квартиры" in btypescombobox.getn:
        minwidth = 800
        maxwidth = 1100

    return maxwidth,minwidth


def createBuilding():
    building=liftcalc.Building(buildingname.get(),btypescombobox.get(),\
                                        peoples.get(),floornumber.get(),floorheightentry.get(),appartment.get())
def createLift():
    lift=liftcalc.Lift(doorwidthentry.get(),movdelayentry,movtimeentry,preopendoorentry,opendoorentry,closedoordelayentry,vnomentry)
    lift.showdata()
    #building.showdata()
#Создаем набор вкладок
notebook=ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
#Создаем фреймы
buildingframe=ttk.Frame(notebook)
liftframe=ttk.Frame(notebook)

buildingframe.pack(fill=BOTH, expand=True)
liftframe.pack(fill=BOTH, expand=True)

#Добавляем фреймы в качестве вкладок

notebook.add(buildingframe,text="Building")
notebook.add(liftframe,text="Lift")
#Этажи
#Наименование корпуса
buildingnamelbl=ttk.Label(buildingframe,text="Введи имя корпуса")
buildingnamelbl.pack(anchor=NW)
buildingname=ttk.Entry(buildingframe)
buildingname.pack(anchor=NW, padx=8,pady=8)
#Тип здания
btypelbl=ttk.Label(buildingframe,text="Тип здания")
btypelbl.pack(anchor=NW)
btypes=["Офис", "Квартиры", "Гостиница"]
btypescombobox = ttk.Combobox(buildingframe,values=btypes)
btypescombobox.pack(anchor=NW, padx=8,pady=8)
btypescombobox.bind("<<ComboboxSelected>>",selected)
#Кол-во людей
peoplelabel=ttk.Label(buildingframe, text="Введи количество людей")
peoplelabel.pack(anchor=NW)
peoples= ttk.Entry(buildingframe)
peoples.pack(anchor=NW, padx=8,pady=8)

#Количество этажей
floornumberlbl = ttk.Label(buildingframe, text="Кол-во этажей")
floornumber=ttk.Entry(buildingframe)
floornumberlbl.pack(anchor=NW)
floornumber.pack(anchor=NW,padx=8,pady=8)
#Высота типового этажа
floorheightlbl=ttk.Label(buildingframe,text="Высота этажа")
floorheightentry=ttk.Entry(buildingframe)
floorheightlbl.pack(anchor=NW)
floorheightentry.pack(anchor=NW, padx=8,pady=8)
# число квартир
appartmentlbl=ttk.Label(buildingframe, text="Число квартир")
appartmentlbl.pack(anchor=NW)
appartment=ttk.Entry(buildingframe)
appartment.pack(anchor=NW, padx=8, pady=8)

#Кнопка создания
createliftbtn= ttk.Button(buildingframe,text="Создать здание",command=createBuilding)
createliftbtn.pack(anchor=S, expand=True)



### Создание лифта

doorwidthlbl=ttk.Label(liftframe,text="Ширина дверей")
doorwidthentry=ttk.Entry(liftframe)
doorwidthlbl.pack(anchor=NW,padx=8,pady=8)
doorwidthentry.pack(anchor=NW,padx=8,pady=8)

closedoortime=ttk.Label(liftframe, text="Время закрывания двери")
closedoortimeentry=ttk.Entry(liftframe)
closedoortime.pack(anchor=NW, padx=8,pady=8)
closedoortimeentry.pack(anchor=NW,padx=8,pady=8)

movdelay=ttk.Label(liftframe,text="Время задержки начала движения лифта")
movdelayentry=ttk.Entry(liftframe)
movdelay.pack(anchor=NW, padx=8,pady=8)
movdelayentry.pack(anchor=NW,padx=8,pady=8)

movtimelbl=ttk.Label(liftframe,text="Время движения лифта между соседними этажами с учетом стадий разгона и торможения")
movtimeentry=ttk.Entry(liftframe)
movtimelbl.pack(anchor=NW, padx=8,pady=8)
movtimeentry.pack(anchor=NW,padx=8,pady=8)

preopendoorlbl=ttk.Label(liftframe,text="Время предварительного открывания двери")
preopendoorentry=ttk.Entry(liftframe)
preopendoorlbl.pack(anchor=NW,padx=8,pady=8)
preopendoorentry.pack(anchor=NW,padx=8,pady=8)

opendoorlbl=ttk.Label(liftframe,text= "Время открывания двери")
opendoorentry=ttk.Entry(liftframe)
opendoorlbl.pack(anchor=NW,padx=8,pady=8)
opendoorentry.pack(anchor=NW,padx=8,pady=8)

closedoordelaylbl=ttk.Label(liftframe,text="Время задержки закрывания двери")
closedoordelayentry=ttk.Entry(liftframe)
closedoordelaylbl.pack(anchor=NW,padx=8,pady=8)
closedoordelayentry.pack(anchor=NW,padx=8,pady=8)

vnomlbl = ttk.Label(liftframe,text="Номинальная скорость движения лифта")
vnomentry=ttk.Entry(liftframe)
vnomlbl.pack(anchor=NW, padx=8,pady=8)
vnomentry.pack(anchor=NW,padx=8,pady=8)
liftbutton = ttk.Button(liftframe, text="Создать лифт", command =createLift)
liftbutton.pack(anchor=NW,padx=8,pady=8)








dfFabric.startdatas()
root.mainloop()
#Тип здания







#настройки лифта
