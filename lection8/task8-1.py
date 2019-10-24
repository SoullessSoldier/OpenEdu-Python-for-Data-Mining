'''
В этой задаче вам предстоит изучить, как устроен XML для описания объектов OpenStreetMap.
Вручную откройте скаченный файл с помощью текстового редактора и найдите в нём широту (атрибут lat) для тега node
с id равным 6428535115 (удобно поискать это число поиском в текстовом редакторе).

Файл для скачивания: https://stepik.org/media/attachments/lesson/266068/map2.osm

В качестве ответа необходимо ввести содержимое параметра lat без кавычек (вещественное число с 7 знаками после точки).
'''
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
s=open('input8-1.osm','r',encoding='utf8')
#xml=urlopen('https://stepik.org/media/attachments/lesson/266068/map2.osm').read()
xml=s.read()
#soup=BS(xml.text,'lxml')
soup=BS(xml,'lxml')

lat=soup.find('node',{'id':'6428535115'})['lat']
print(lat)#55.4166358
s.close()


