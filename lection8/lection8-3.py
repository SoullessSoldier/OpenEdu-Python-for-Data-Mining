#Вложенные теги и атрибуты
#В лекции посчитаем количество супермаркетов каждой сети
'''
<tag k="shop" v="supermarket"/>
<tag k="name" v="Ю-маркет"/>
Для всех супермаркетов запомнить их названия и прибавить 1 соответствующему элементу
'''
from bs4 import BeautifulSoup as BS

xml=open('warsaw.osm','r',encoding='utf8').read()
soup=BS(xml,'lxml')
cnt=0
names={}
for node in soup.find_all('node'):
    flag=False
    name=''
    for tag in node('tag'):
        if tag['k']=='shop' and tag['v']=='supermarket':
            flag=True
        if tag['k']=='name':
            name=tag['v']
    if flag:
        if name not in names:
            names[name]=0
        names[name]+=1
supermarkets=list(names.items())
supermarkets.sort(key=lambda x:(-x[1],x[0]))
for now in supermarkets:
    print(*now)
#Эти карты мы качали вручную. В следующем видео будем автоматизировать загрузку