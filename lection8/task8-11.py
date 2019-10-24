"""
Вам дана область карты https://stepik.org/media/attachments/lesson/266078/mapcity.osm

Пройдите по первым ста node в этой области и выведите для каждого три числа: id, широту (атрибут lat) и долготу (атрибут lon).

Числа для каждого node выводите в отдельной строке, разделяя одним пробелом.
Обрабатывать node нужно в том же порядке, в котором они встречаются во входном файле.

Если вы все делаете правильно, то ваш ответ должен начинаться со строк:

60276311 55.5695795 37.5764692
60276312 55.5682232 37.5754573
"""
from bs4 import BeautifulSoup as BS
"""
from urllib.request import urlopen
url='https://stepik.org/media/attachments/lesson/266078/mapcity.osm'
response = urlopen(url)
xml = response.read().decode('utf8')
"""
fout=open('out8-11.txt','w',encoding='utf8')
xml=open('mapcity.osm','r',encoding='utf8').read()
soup = BS(xml, 'lxml')
cnt=100
i=0
#nodes = {}#нам понадобятся все ноды
for node in soup.find_all('node'):
    if i<cnt:
        lat=node['lat']
        lon=node['lon']
        id=node['id']
        print(id,lat,lon,file=fout)
        i+=1
    else:
        break
fout.close()
