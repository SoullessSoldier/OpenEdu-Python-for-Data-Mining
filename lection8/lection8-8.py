"""
Пример решения задачи на обработку геоданных
Дороги в OSM кодируются тегом way и тегом tag с атрибутами k:v=highway:что-нибудь
дороги бывают primary и secondary
попробуем посчитать длину по типу дороги
Надо знать, из каких точек состоит ломаная, у точек есть своя широта и долгота
<nd ref="***"/>
nd.ref=node.id
Порядок может быть произвольный
Надо для каждой дороги сохранить список Id точек
в отдельный словарь для каждой точки сложим ее широту и долготу, в качестве ключа - ее id
потом по списку дорог пройтись по их точкам и узнать расстояния между соседними точками
потом пройтись по всему квадрату в зависимости от типа и узнаем, как развита дорожная сеть в квадрате
Широта - по вертикали, долгота - по горизонтали
"""
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen,urlretrieve
import math
def dist(coord1,coord2):
    #функция будет считать расстояние в км между координатами двух точек
    #Определяем расстояние в градусах по широте и долготе
    dlat=abs(coord1[0]-coord2[0])
    dlon=abs(coord1[1]-coord2[1])
    #расстояние в км по теореме Пифагора, т.к. нам известны стороны - изменения в долготе и широте
    # причем градус долготы меняется в зависимости от широты :
    # через косинус широты, причем надо перевести градусы в радианы через Pi/180
    # предполагаем, что окно выборки небольшое, поэтому в коссинус дадим координаты первой точки
    d = math.sqrt((dlat*111.11)**2+(dlon*111.11*math.cos(coord1[0]/180 * math.pi))**2)
    return d

minlat=55.5671
maxlat=55.9107
minlon=37.3611
maxlon=37.8638
dlat=(maxlat-minlat)/100#размер окна по широте
dlon=(maxlon-minlon)/100#размер окна по широте

for i in range(100):
    for j in range(100):
        #Создадим словарь, ключ - тип дороги, значение - суммарная длина дорог этого типа в квадратике
        #для каждого квадратика - заново словарь
        roads={}
        nminlat = minlat + dlat * i # новая минимальная широта
        nmaxlat = minlat + dlat * (i + 1) #новая минимальная широта
        nminlon = minlon + dlon * j  # новая минимальная долгота
        nmaxlon = minlon + dlon * (j + 1)  # новая минимальная долгота
        #окно определено
        url = "https://www.openstreetmap.org/api/0.6/map?bbox=" + str(nminlon) + "%2C" + str(nminlat) + "%2C" + str(nmaxlon) + "%2C" + str(nmaxlat)
        #response = urlopen(url)
        #xml = response.read().decode('utf8')
        #Сделаем папку osm внутри проекта и будем кидать 10000 файлов туда
        filename=str(i)+'-'+str(j)+'.osm'
        #urlretrieve(url,'osm/map'+filename)
        urlretrieve(url, 'osm/map.osm')#пока все будем лепить в один файл
        #xml=open('osm/map'+filename,'r',encoding='utf8').read()
        xml=open('osm/map.osm','r',encoding='utf8').read()
        soup = BS(xml, 'lxml')
        nodes = {}#нам понадобятся все ноды
        for node in soup.find_all('node'):
            lat=float(node['lat'])
            lon=float(node['lon'])
            id=int(node['id'])
            nodes[id]=(lat,lon)
        #Теперь пройдем по всем way'ям

        for way in soup.find_all('way'):
            flag = False#вдруг "дорога" - не хайвей
            for tag in way('tag'):
                if tag['k']=='highway':
                    rtype=tag['v']#rtype - road type - тип дороги primary или secondary
                    #print(f"road type {rtype}")
                    flag=True
            if flag:
                #нам надо узнать все id нодов, входящих в этот way
                rnodes=[]#список нодов
                for nd in way('nd'):
                    ref=int(nd['ref'])
                    rnodes.append(ref)
                    #Как посчитать длину дороги?
                    #Возьмем разницу широты и долготы и умножим на длину градуса
                    #пройдемся по всему списку
                    for k in range(len(rnodes)-1):#будем брать i-ую и i+1 ую точки
                        coord1=nodes[rnodes[k]]#не забыл, что в словаре nodes пара значений?
                        coord2=nodes[rnodes[k+1]]
                        #проверяем, есть ли тип дороги в нашем словаре
                        if rtype not in roads:
                            roads[rtype]=0
                        roads[rtype]+=dist(coord1,coord2)
        print('Sector ', i, j)
        for now in roads:
            print(now, roads[now])
        """
        Можно сохранить данные в формате csv, собрать все типы дорог, потом строить графики
        """


