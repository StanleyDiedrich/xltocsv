from bs4 import BeautifulSoup
import pandas as pd
from tkinter import filedialog as fd

def createsystemlist(list):
    coolrows=[]
    reslist=[]
    grouptotallist=[]
    count=1
    for table in list:
        rows=table.find_all("tr")
        totallist = []
        for row in rows:
            rowtext = []
            rowtext.append(f'Система К{count}')
            columns=row.find_all('td')
            for column in columns:
                if "Ind" in column.text.split()  :
                    all_p=row.find_all('p')
                    for p in all_p:
                        rowtext.append(p.text.replace('\n    ',''))
            if len(rowtext)!=1 and len(rowtext)!=0:
                totallist.append(rowtext)

        if len(totallist)!=0:
            grouptotallist.append(totallist)
        count += 1
    return grouptotallist

def destroygrouptotallist(grouptotallist):
    newlist = []
    for list in grouptotallist:

        for li in list:
            newlist.append(li)
    return newlist

def createFCU():
    filename = "resfile.html"
    tableslist=[]
    subtableslist=[]
    heatlist=[]
    coollist=[]
    soundlist=[]
    rescool = []
    with(open(filename,"r")as file):
        soups=BeautifulSoup(file,"html.parser")
        all_tables=(soups.find_all("table"))
        for table in all_tables:
            all_p=table.find_all("p")
            for p in all_p:
                if "Охлаждение" in p.text:
                    coollist.append(table)
                if "Нагрев" in p.text:
                    heatlist.append(table)
                if "Помещение" in p.text:
                    soundlist.append(table)
    coolcolumnsnames = ["Система", "Название", "FCU", "TmpC", "Rq TC", "Rv Tc", "Max Tc", "Rq Sc", "T evap", "Tdis",
                        "Max SC", "PIC"]

    #print(destroygrouptotallist(createsystemlist(coollist)))
    alist = destroygrouptotallist(createsystemlist(coollist))
    for a in alist:
        rescool.append(a)
    df1 = pd.DataFrame(data=rescool)
    df1 = pd.DataFrame(data=rescool, columns=coolcolumnsnames)
    #print (df1)
    df1["Index"] = df1["Система"] + df1["Название"]
    df1.set_index("Index")
    #print(df1)
    # with(open("collres.csv", "w") as file):
    #     #df = pd.DataFrame(data=rescool)
    #     df = pd.DataFrame(data=rescool,columns=coolcolumnsnames)
    #     df.to_csv("collres.csv")
    heatcolumnsnames = ["Система", "Название", "FCU", "Tmp H", "Rq Hc", "Max HC", "Tdis H", "PIH", "Min coil",
                        "Max coil", "Расход воздуха"]
    resheat= []
    #
    blist = destroygrouptotallist(createsystemlist(heatlist))

    for b in blist:
        resheat.append(b)
    df2 = pd.DataFrame(data=resheat, columns=heatcolumnsnames)
    print(df2)
    df2["Index"] = df2["Система"] + df2["Название"]
    df2.set_index("Index")
    # # with(open("heatres.csv", "w") as file):
    # #     df = pd.DataFrame(data=resheat,columns=heatcolumnsnames)
    # #     df.to_csv("heatres.csv")
    soundcolumnsnames = ["Система", "Название", "FCU", "Звук dBA", "Напряжение, В", "Сила тока, A", "MOP", "ШхВхГ",
                         "Вес"]
    ressound = []
    clist = destroygrouptotallist((createsystemlist(soundlist)))
    for c in clist:
        ressound.append(c)
    df3 = pd.DataFrame(data=ressound, columns=soundcolumnsnames)

    df3["Index"] = df3["Система"] + df3["Название"]
    df3.set_index("Index")
    #
    df4 = pd.merge(pd.merge(df1, df2, on="Index"), df3, on="Index")
    filename = fd.asksaveasfilename()
    #print(df4)
    df4.to_csv(filename)


