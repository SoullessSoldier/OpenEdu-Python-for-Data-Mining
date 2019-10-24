'''
Сейчас вам нужно установить библиотеку lxml для обработки xml с помощью BeatifulSoup. Чтобы проверить, что всё установилось хорошо, необходимо запусить код, представленный ниже и сдать в качестве ответа то, что он выводит.

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm') # скачиваем файл
xml = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(xml, 'xml') # делаем суп с помощью lxml
cnt = 0
for way in soup.find_all('way'): # идем по всем тэгам way
    cnt += 1 # и просто считаем их количество
print(cnt)
'''
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm') # скачиваем файл
xml = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(xml, 'xml') # делаем суп с помощью lxml
cnt = 0
for way in soup.find_all('way'): # идем по всем тэгам way
    cnt += 1 # и просто считаем их количество
print(cnt)#3181