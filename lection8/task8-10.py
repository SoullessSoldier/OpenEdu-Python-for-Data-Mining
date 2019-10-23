'''
Скачайте с помощью скрипта область карты OSM, где минимальная широта равна 55.5586, минимальная долгота 37.5649,
максимальная широта 55.5728, максимальная долгота 37.5803.

Чтобы вспомнить, как добыть адрес api, который возвращает вам нужный кусок карты,
пройдите по ссылке https://www.openstreetmap.org/export, включите режим разработчика в браузере (ctrl+shift+i),
откройте вкладку "Network", затем выберите слева Manually select a different area,
выберите какую-нибудь область и нажмите кнопку Export.
Во вкладке Network появится адрес ссылки, по которой добывается xml файл.
Исправьте в нем координаты на данные в условии задачи и вы получите адрес того файла, который нужно сдать на проверку.
'''
minlat="55.5586"
maxlat="55.5728"
minlon="37.5649"
maxlon="37.5803"
from urllib.request import urlopen

url = "https://www.openstreetmap.org/api/0.6/map?bbox=" + str(minlon) + "%2C" + str(minlat) + "%2C" + str(
    maxlon) + "%2C" + str(maxlat)
response = urlopen(url)
xml = response.read().decode('utf8')
fout=open('out8-10.osm','w',encoding='utf8')
print(xml,file=fout)
fout.close()