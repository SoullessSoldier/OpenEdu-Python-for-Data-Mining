'''
В этой задаче вам предстоит изучить, как устроен XML для описания объектов OpenStreetMap.
Вручную откройте скаченный файл с помощью текстового редактора и найдите в нём
тэг tag с атрибутом k="public_transport" в node с id равным 203573042
(удобно поискать это число поиском в текстовом редакторе).

Файл для скачивания: https://stepik.org/media/attachments/lesson/266068/map2.osm

В качестве ответа необходимо ввести содержимое атрбута v для найденного тэга tag без кавычек.
'''
url="https://stepik.org/media/attachments/lesson/266068/map2.osm"
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
#s=open('input8-2.osm','r',encoding='utf8')
xml=urlopen('https://stepik.org/media/attachments/lesson/266068/map2.osm').read()

soup=BS(xml,'lxml')
#soup=BS(xml,'lxml')

node=soup.find('node',{'id':'203573042'})
#print(node)
for tag in node('tag'):
    if tag['k']=='public_transport':
        print(tag['v'])
