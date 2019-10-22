'''
Передача параметров в URL
'''

from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
'''#Gdansk example1
minlat="54.3800"#minimal latitude#широта, Координаты для прямоугольника выборки
maxlat="54.3862"#maximum latitude
minlon="18.5886"#minimal longitude
maxlon="18.6085"#maximal longitude
'''
'''#Gdansk example2
minlat="54.3475"
maxlat="54.3507"
minlon="18.6469"
maxlon="18.6613"
'''
#Если нарезать большую местность на квадратики
#Берем Масскву
#OSM не умеет отдавать большие куски, будет HTTP Error 400
minlat="55.5671"
maxlat="55.9107"
minlon="37.3611"
maxlon="37.8638"
url="https://www.openstreetmap.org/api/0.6/map?bbox="+minlon+"%2C"+minlat+"%2C"+maxlon+"%2C"+maxlat
response=urlopen(url)
xml=response.read().decode('utf8')
soup=BS(xml,'lxml')
names={}
for node in soup.find_all('node'):
    flag=False
    name=''
    for tag in node('tag'):
        if tag['k']=='shop' and tag['v']=='supermarket':
        #if tag['k']=='amenity' and tag['v']=='cafe':

            flag=True
        if tag['k']=='name':
            name=tag['v']
    if flag:
        if name not in names:
            names[name]=0
        names[name]+=1
#print(names)
supermarkets=list(names.items())
for now in sorted(supermarkets,key=lambda x:(-x[1],x[0])):
    print(*now)
