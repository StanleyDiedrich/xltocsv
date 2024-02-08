import pandas as pd
from roomclass import Room
from ofile import openfile
filename=openfile()
def proc():

    df = pd.read_excel(filename,sheet_name="EXP_Микроклимат", usecols=[0,1,3,4,5,6,8,39,40])
    df = df.drop(index=0)
    df2 = df[['ID пространства', 'Номер Revit', 'Номер секции', 'Номер АР', 'Назначение помещения',
             'Наименование помещения АР','Этаж', 'Номер приточной системы EXCEL', 'Номер вытяжной системы EXCEL']].fillna('-')
    #print (df2)
    rooms = []
    newrooms = []
    for index, row in df2.iterrows():
        newroom = Room(row['ID пространства'], row['Номер Revit'], row['Номер секции'],row['Номер АР'],\
                       row['Назначение помещения'],row['Наименование помещения АР'],row['Этаж'],\
                       row['Номер приточной системы EXCEL'],row['Номер вытяжной системы EXCEL'])
        newrooms.append(newroom)

    #print (f'newroom+{newrooms[0].Id}')
    count=0
    for i in newrooms:
        if i.Id!='-':
            count+=1
    for i in newrooms[:count]:
        if i.Id not in rooms:
            rooms.append(i)
    #return print(len(rooms))
    for r in rooms:
        supplyf = ''
        exhaustf = ''
        for n in newrooms:
            if r.Id == n.Id:
                if n.supply=='-':
                    supplyf='-'
                else:
                    supplyf += n.supply + ';'
                if n.exhaust=='-':
                    exhaustf='-'
                else:
                    exhaustf += n.exhaust + ';'
        r.supply = supplyf
        r.exhaust = exhaustf
    #print(f'room+{rooms[0].Id}')
    # return
    nnlist = []

    d = {}
    for r in rooms:
        if r.Id not in d:
            d[r.Id] = r
    desired_list = d.values()
    datalist=[]

    for dlist in desired_list:
         slist=dlist.supply.split(';')
         #return print(slist)
         elist=dlist.exhaust.split(';')
         syslistsup = []
         syslistexh=[]
         count=0
         for sl in slist:
             if sl=="-" or sl=='':
                 continue
             else:
                syslistsup.append(sl)


         for el in elist:
             if el == "-" or el=='':
                 continue
             syslistexh.append(el)

         dlist = [dlist.Id, dlist.spacenum, dlist.secnum, dlist.arnum, dlist.roomdef, dlist.arname,dlist.floor]
         for sl in syslistsup:
             dlist.append(sl)
         for el in syslistexh:
             dlist.append(el)

         datalist.append(dlist)
    for i in datalist:
        if len(i)-1<16:
            a = len(i)-1
            while len(i)-1<16:
                i.append('-')
    # for i in datalist:
    #     print(i)
    # return
         #return print(datalist[0])
    # for i in datalist:
    #      print(datalist)
    # datalist=[]
    # for nn in desired_list:
    #     nlist=[nn.Id,nn.spacenum, nn.secnum,nn.arnum,nn.roomdef,\
    #                    nn.arname,nn.supply, nn.exhaust]
    #     datalist.extend(nlist)
    columns=['ID пространства', 'Номер Revit', 'Номер секции','Номер АР',\
            'Назначение помещения','Наименование помещения АР','Этаж',\
            'Система1','Система2','Система3','Система4','Система5','Система6','Система7',\
             'Система8','Система9','Система10']
    #return print(datalist)
    df3=pd.DataFrame(data=datalist, columns=columns)
    return df3