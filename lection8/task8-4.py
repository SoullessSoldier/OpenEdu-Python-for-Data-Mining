'''
В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте.
Ноды могут не только обозначать какой-то точечный объект, но и входить в состав way
(некоторой линии, возможно замкнутой) и не иметь собственных тегов.
Для доступного по ссылке https://stepik.org/media/attachments/lesson/245681/map2.osm фрагмента карты посчитайте,
сколько всего тегов node встречается на этой карте. В качестве ответа введите одно число.
'''
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm') # скачиваем файл
xml = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(xml, 'xml') # делаем суп с помощью lxml
cnt = 0
for node in soup.find_all('node'): # идем по всем тэгам node
    cnt += 1 # и просто считаем их количество
print(cnt)#25189