'''
Вася решил открыть АЗС (заправку).
Чтобы оценить уровень конкуренции он хочет изучить количество заправок в интересующем его районе.
Вася скачал интересующий его кусок карты OSM https://stepik.org/media/attachments/lesson/245681/map2.osm
и хочет посчитать, сколько на нём отмечено точечных объектов (node), являющихся заправкой.
В качестве ответа вам необходимо вывести одно число - количество АЗС.

Заправка в OSM обозначается парой ключ-значение amenity=fuel. Эта пара находится среди тегов tag внутри node.
'''
from bs4 import BeautifulSoup as BS
response=open('map2.osm','r',encoding='utf8')
xml=response.read()
response.close()
soup=BS(xml,'lxml')
names={}
for node in soup.find_all('node'):
    flag=False
    name=''
    for tag in node('tag'):
        #if tag['k']=='shop' and tag['v']=='supermarket':
        if tag['k']=='amenity' and tag['v']=='fuel':

            flag=True
        if tag['k']=='name':
            name=tag['v']
    if flag:
        if name not in names:
            names[name]=0
        names[name]+=1
#print(names)
supermarkets=list(names.items())
sum=0
for now in sorted(supermarkets,key=lambda x:(-x[1],x[0])):
    print(*now)
    sum+=now[1]
print(f"Total fuels: {sum}")#15