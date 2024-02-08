# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import lxml
import csv
html_doc= "test-1-4.html"
namelist=[]
vallist=[]
definelist=['ND','ул.','Россия']
with open(html_doc,"r",encoding="utf-8") as file:
    soup = BeautifulSoup(file,"html.parser")
    # table= soup.find_all('table')
    # print(len(table))
    # for tab in table:
    #     rows=tab.find_all('td')
    #     for i in rows:
    #         name = i.text
    #
    #         print(f'{name} ')

    ptext=[x.text for x in soup.find('p')]
    print (ptext)


    # rows = soup.find_all('tr')
    # for row in rows[:]:
    #     columns = row.find_all('td')
    #     name = columns[0].text
    #     try:
    #         value = columns[1].text
    #     except:
    #         continue
    #     if namelist.__contains__(name):
    #         continue
    #     else:
    #         namelist.append(name)
    #     vallist.append(value)
    #     print(f'{name}: {value}')



#print(namelist)
#print(vallist)
# text_s2=soup.find_all('p',attrs={"class":'s2'})
# for j in text_s2:
#     print(j.text)
# with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(namelist)
#     writer.writerow(vallist)


