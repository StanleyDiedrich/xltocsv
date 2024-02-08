import html

from bs4 import  BeautifulSoup
import lxml
import requests
import csv
names=[]
metros=[]
adresses=[]
url ='https://www.mr-group.ru/projects/apartments/'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup=BeautifulSoup(response.text,'lxml')
names=["".join(x.text.strip()) for x in soup.find_all('div', attrs={'class':'main-projects-item-titles__title js-main-projects-item-titles__title'})]
metrs=["".join(x.text.strip()) for x in soup.find_all('span',attrs={'class':'metro-name'})]
adresses=["".join(x.text.strip()) for x in soup.find_all('span',attrs={'class':'address'})]
prices = ["".join(x.text.strip()) for x in soup.find_all('div',attrs={'class':'price'})]
dlist=[]
with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    for i, j, k, l in zip(names,metrs,adresses,prices):
        data=[i,j,k,l]
        dlist.append(data)
    writer.writerows(dlist)
print("csv is done!")
#     for name, metro, address, price in zip(names, metrs, adresses, prices):
#
#         # Формируем строку для записи
#         flatten= name+metro+address+price
#         writer.writerow(flatten)
#
# print('Файл res.csv создан')













