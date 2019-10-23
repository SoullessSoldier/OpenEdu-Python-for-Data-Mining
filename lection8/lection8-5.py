#Загрузка данных по частям
#Скрипт нарезания Москвы на 100 одинаковых прямоугольников

from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

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
        response = urlopen(url)
        xml = response.read().decode('utf8')
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
'''
Следующая задача - подсчет длины дорог в квадратах
Для неоднократной работы с сайтом - сохранять куски в файл
'''