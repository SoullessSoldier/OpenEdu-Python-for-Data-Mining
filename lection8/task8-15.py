"""
Вам дана область карты https://stepik.org/media/attachments/lesson/266078/mapcity.osm

Пройдите по всем way в этой области, выделите среди них замкнутые
(те, у которых совпадает ссылка на первый и последний node),
среди всех замкнутых выделите те, у которых установлен tag с ключом building и произвольным значением.

Запомните id для way и список кортежей, содержащих координаты (широту и долготу) всех node, входящих в этот way.

Вам предложена функция, которая определяет нечто похожее на площадь замкнутой ломаной.

import math

def getsqr(coordlist):
     baselat = coordlist[0][0]
     baselon = coordlist[0][1]
     degreelen = 111300
     newcoord = []
     for now in coordlist:
          newcoord.append(((now[0] - baselat) * degreelen, (now[1] - baselon) * degreelen * math.cos(baselat)))
     sqr = 0
     for i in range(len(newcoord) - 1):
          sqr += newcoord[i][0] * newcoord[i + 1][1] - newcoord[i + 1][0] * newcoord[i][1]
     sqr += newcoord[-1][0] * newcoord[0][1] - newcoord[0][0] * newcoord[-1][1]
     return abs(sqr)
Она принимает на вход список с координатами точек так, как вы выводили его в предыдущей задаче
(обратите внимание, что числа внутри кортежей должны иметь тип float).

С помощью этой функции найдите id для самого большого площади здания.
"""
import math
from bs4 import BeautifulSoup as BS

def getsqr(coordlist):
     baselat = coordlist[0][0]
     baselon = coordlist[0][1]
     degreelen = 111300
     newcoord = []
     for now in coordlist:
          newcoord.append(((now[0] - baselat) * degreelen, (now[1] - baselon) * degreelen * math.cos(baselat)))
     sqr = 0
     for i in range(len(newcoord) - 1):
          sqr += newcoord[i][0] * newcoord[i + 1][1] - newcoord[i + 1][0] * newcoord[i][1]
     sqr += newcoord[-1][0] * newcoord[0][1] - newcoord[0][0] * newcoord[-1][1]
     return abs(sqr)

xml=open('mapcity.osm','r',encoding='utf8').read()
soup = BS(xml, 'lxml')

nodes = {}#нам понадобятся все ноды
for node in soup.find_all('node'):

        lat=float(node['lat'])
        lon=float(node['lon'])
        id=node['id']
        nodes[id]=(lat,lon)
wayz=[]
for way in soup.find_all('way'):

    for tag in way('tag'):
        if tag['k'] == 'building':
            # нам надо узнать все id нодов, входящих в этот way
            rnodes = []  # список нодов
            for nd in way('nd'):
                ref = nd['ref']
                rnodes.append(ref)
            if rnodes[0]==rnodes[len(rnodes)-1]:
                #print(way['id'])
                temp_list1=[]
                for rnode in rnodes:
                    temp_list1.append(nodes[rnode])
                temp_sqr=getsqr(temp_list1)
                wayz.append([way['id'],temp_sqr])
#print(*wayz)
print(sorted(wayz,key=lambda x: -x[1])[0][0])#316777075