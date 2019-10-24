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
"""
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen,urlretrieve
minlat=55.5671
maxlat=55.9107
minlon=37.3611
maxlon=37.8638
dlat=(maxlat-minlat)/100#размер окна по широте
dlon=(maxlon-minlon)/100#размер окна по широте

for i in range(100):
    for j in range(100):
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
        names = {}
        for node in soup.find_all('node'):
            flag = False
            name = ''
            for tag in node('tag'):
                if tag['k'] == 'shop' and tag['v'] == 'supermarket':
                    # if tag['k']=='amenity' and tag['v']=='cafe':
                    flag = True
                if tag['k'] == 'name':
                    name = tag['v']
            if flag:
                if name not in names:
                    names[name] = 0
                names[name] += 1
        # print(names)
        supermarkets = list(names.items())
        print(f"Sector {i},{j}")
        for now in sorted(supermarkets, key=lambda x: (-x[1], x[0])):
            print(*now)
